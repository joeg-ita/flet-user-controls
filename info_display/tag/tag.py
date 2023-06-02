import flet as ft

class Tag(ft.UserControl):

    styles={
        'primary': { 'severity': 'primary', 'text_color': 'white', 'icon_color':'white'},
        'success': { 'severity': 'green600', 'text_color': 'white', 'icon_color':'white'},
        'warning': { 'severity': 'orange500', 'text_color': 'white', 'icon_color':'white'},
        'danger': { 'severity': 'red900', 'text_color': 'white', 'icon_color':'white'},
    }

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 page: ft.Page, 
                 text: str = None, 
                 severity: str = "primary",
                 icon : ft.Icon = None,
                 pill: bool = False):
        
        super().__init__()

        self.page = page
        self.style = self.styles[severity] if severity in self.styles else self.styles['primary']
        self.radius = 20 if pill else 5
        padding = ft.Padding(5,5,10,5) if not icon else ft.Padding(0,5,10,5)
        self.text = ft.Container(ft.Text(f"{text}", color=self.style['text_color']), padding=padding)

        self.components = []
        if (icon is not None and type(icon) == ft.Icon):
            icon.color = self.style['icon_color']
            self.components.append(icon)
            
        self.components.append(self.text)


    def build(self):

        self.chip = ft.Row(
                [
                    ft.Container(
                        ft.Row(
                            self.components,
                            alignment=ft.MainAxisAlignment.CENTER,
                            tight=True,
                        ),
            
                    col=ft.colors.GREY,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=ft.border_radius.all(self.radius),
                    bgcolor=self.style['severity'],
                    padding=ft.Padding(5,0,0,0)
                    )
            ],

                alignment=ft.MainAxisAlignment.CENTER,
                tight=True,
            )
        return self.chip
    
    def did_mount(self):
        return super().did_mount()

    def will_unmount(self):
        return super().will_unmount()