import flet as ft
import flet.canvas as cv
import math
from datetime import datetime
import time, threading
import pytz


class AnalogClock(ft.UserControl):

    angles = [450, 420, 390, 360, 330, 300, 270, 240, 210, 180, 150, 120, 90]
    default_timezone = "Europe/Rome"
    default_label = "Rome"

    def __init__(self, clock_label: str =default_label, timezone: str= default_timezone):
        super().__init__()

        self.timezone = pytz.timezone(timezone) 
        self.clock_label = clock_label

        self.cp = cv.Canvas(
            self.clock(),
            width=float("inf"),
            expand=True,
        )

    def build(self):
        return ft.Container(
            self.cp
        )
    
    def add_numbers(self):
        numbers = []
        r = 85
        for i in range(1, 13):
            x, y  =  r*(math.cos(self.angles[i]*math.pi/180)), r*(-math.sin(self.angles[i]*math.pi/180))
            numbers.append(cv.Text((x)+95, (y)+90, str(i), style=ft.TextStyle(weight=ft.FontWeight.BOLD)))
        return numbers
    
    def clock(self):
        stroke_paint = ft.Paint(stroke_width=6, style=ft.PaintingStyle.STROKE)
        fill_paint = ft.Paint(style=ft.PaintingStyle.FILL)
        canvas = []
        canvas.append(cv.Circle(100, 100, 100, stroke_paint))
        canvas = canvas + self.add_numbers()
        canvas.append(cv.Text(100-len(self.clock_label)*3.5, 40, self.clock_label, text_align=ft.MainAxisAlignment.CENTER, style=ft.TextStyle(weight=ft.FontWeight.BOLD, font_family="Helvetica")))
        canvas = canvas + self.draw_time()
        canvas.append(cv.Circle(100, 100, 10, fill_paint))
        canvas.append(cv.Circle(100, 100, 6, ft.Paint(style=ft.PaintingStyle.FILL, color=ft.colors.WHITE)))
        return canvas
    
    def draw_time(self):
        draw = []
        now = datetime.now().astimezone(self.timezone)
        hour = now.hour
        minute = now.minute
        second = now.second
        am_pm = now.strftime("%p")
        day = now.strftime("%d")

        r = 80
        x_pad = 100
        y_pad = 100

        hour = hour%12

        h_angle = self.angles[hour] - minute/2 - second/60/2
        h_x, h_y = (r*0.60)*(math.cos(h_angle*math.pi/180)), (r*0.60)*(-math.sin(h_angle*math.pi/180))

        m_angle = self.angles[math.floor(minute/5)] - (minute%5)*6
        m_x, m_y  = (r*0.80)*(math.cos(m_angle*math.pi/180)), (r*0.80)*(-math.sin(m_angle*math.pi/180))
        
        s_angle = self.angles[math.floor(second/5)] - (second%5)*6
        s_x, s_y  = (r*0.98)*(math.cos(s_angle*math.pi/180)), (r*0.98)*(-math.sin(s_angle*math.pi/180))

        h = cv.Line(100, 100, h_x+x_pad, h_y+y_pad, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=10, style=ft.PaintingStyle.STROKE, color=ft.colors.ORANGE))
        h_sh = cv.Line(102, 102, h_x+x_pad+2, h_y+y_pad+2, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=10, style=ft.PaintingStyle.STROKE, color=ft.colors.BLACK26, 
                                                                          gradient=ft.PaintRadialGradient(ft.Offset(102, 102), 50, [ft.colors.BLACK26, ft.colors.BLACK54])))
        
        m = cv.Line(100, 100, m_x+x_pad, m_y+y_pad, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=6, style=ft.PaintingStyle.STROKE, color=ft.colors.ORANGE))
        m_sh = cv.Line(102, 102, m_x+x_pad+2, m_y+y_pad+2, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=6, style=ft.PaintingStyle.STROKE, color=ft.colors.BLACK26, 
                                                                          gradient=ft.PaintRadialGradient(ft.Offset(102, 102), 50, [ft.colors.BLACK26, ft.colors.BLACK54])))
        
        s = cv.Line(100, 100, s_x+x_pad, s_y+y_pad, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=2, style=ft.PaintingStyle.STROKE, color=ft.colors.RED))
        s_sh = cv.Line(102, 102, s_x+x_pad+2, s_y+y_pad+2, paint=ft.Paint(stroke_cap=ft.StrokeCap.ROUND, stroke_width=2, style=ft.PaintingStyle.STROKE, color=ft.colors.BLACK26, 
                                                                          gradient=ft.PaintRadialGradient(ft.Offset(102, 102), 50, [ft.colors.BLACK26, ft.colors.BLACK54])))
        
        day_bg = cv.Rect(
                146, 88, 25, 20,
                paint=ft.Paint(
                    style=ft.PaintingStyle.STROKE,
                    gradient=ft.PaintRadialGradient(ft.Offset(146, 88), 20, [ft.colors.BLACK, ft.colors.BLACK54])
                ),
            )
        d = cv.Text(150, 89, day, style=ft.TextStyle(foreground=ft.Paint(color=ft.colors.GREY_600)))
        p = cv.Text(100-len(am_pm)*4, 145, am_pm, style=ft.TextStyle(size=12,font_family="Helvetica"))

        draw.append(p)
        # draw.append(day_bg)
        # draw.append(d)
        draw.append(h_sh)
        draw.append(h)
        draw.append(m_sh)
        draw.append(m)
        draw.append(s_sh)
        draw.append(s)
        return draw
    
    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False
    
    def update_timer(self):
        while self.running:
            time.sleep(1)
            self.cp.shapes = self.clock()
            self.cp.update()