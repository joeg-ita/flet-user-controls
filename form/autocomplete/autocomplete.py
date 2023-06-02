import flet as ft

class Autocomplete(ft.UserControl):

    rating: int = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 page: ft.Page = None, 
                 selected_item: any = False, 
                 suggestion: any = False,
                 autocoplete: callable = False):
        
        super().__init__()

        self.page = page
        self.selected_item = selected_item, 
        self.suggestion = suggestion,
        self.autocoplete = autocoplete
        self.is_panel_visible = False
        self.tb1 = ft.Container(ft.TextField(label="Autocomplete", hint_text="type to search", dense=True, width=300, on_change=self.search))
        self.lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def build(self):

        
        return ft.Column(
            [
                ft.Stack(
                    [
                        self.tb1,
                        ft.IconButton(icon=ft.icons.ARROW_DROP_DOWN, right=5, on_click=self.open_panel),
                    ]
                ),
                
            ]
        )
    
    def open_panel(self, e:ft.ControlEvent = None, show=None):
        if show or show is None:
            self.page.overlay.append(
                ft.Container(
                    content=self.lv,
                    width=300, height=200, bgcolor=ft.colors.WHITE, top=80, left=10, border=ft.Border(top=ft.BorderSide(1),right=ft.BorderSide(1),bottom=ft.BorderSide(1),left=ft.BorderSide(1))
                )
            )
        else:
            self.page.overlay.clear()
        self.page.update()

    def search(self, e):
        print(e.data)
        if len(e.data)> 2:
            self.open_panel(show=True)
            for i in range(0,10):
                self.lv.controls.append(ft.Row([ft.TextButton(f"{e.data} {i}", on_click=self.select),], alignment=ft.MainAxisAlignment.START))
        self.update()

    def select(self, e):
        print(e.data)
        self.open_panel(show=False)
        self.update()

    def did_mount(self):
        return super().did_mount()

    def will_unmount(self):
        return super().will_unmount()
    