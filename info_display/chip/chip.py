import flet as ft

class Chip(ft.UserControl):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 page: ft.Page, 
                 text: str = None, 
                 icon : ft.Icon = None,
                 removable : bool = False):
        
        super().__init__()

        self.page = page
        text_padding = ft.Padding(0,10,10,10) if not removable else ft.Padding(0,10,0,10)
        self.text = ft.Container(ft.Text(f"{text}"), padding=text_padding)
        self.icon = icon
        self.removable = removable

        self.components = []
        if (icon is not None and type(icon) == ft.Icon):
            self.components.append(icon)
        else:
            self.components.append(ft.Icon(name=ft.icons.HOME))
            
        self.components.append(self.text)
        if self.removable:
            self.components.append(ft.IconButton(icon=ft.icons.CANCEL_OUTLINED, on_click=self.delete))

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
                    border_radius=ft.border_radius.all(20),
                    bgcolor=ft.colors.GREY_300,
                    padding=ft.Padding(5,0,0,0)
                    )
            ],

                alignment=ft.MainAxisAlignment.CENTER,
                tight=True,
            )
        return self.chip
    
    def delete(self, e):
        if self.removable:
            p = self.page
            self.traverse_controls(p.controls, self)
            p.update()

    def traverse_controls(self, controls, control_to_delete):
        for c in controls:
            if c == control_to_delete:
                controls.remove(c)
                return
            if hasattr(c, 'controls') and len(c.controls)>0:
                self.traverse_controls(c.controls, control_to_delete)
        

    def did_mount(self):
        return super().did_mount()

    def will_unmount(self):
        return super().will_unmount()