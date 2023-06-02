import flet as ft

class Rating(ft.UserControl):

    rating: int = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, 
                 page: ft.Page = None, 
                 readonly: bool = False, 
                 disabled: bool = False,
                 cancel: bool = False,
                 elements: int = 5,
                 rating: int = None,
                 on_change: callable = None):
        
        super().__init__()

        self.page = page
        self.readonly = readonly
        self.disabled = disabled
        self.cancel = cancel
        self.elements = elements
        self.rating = rating-1 if rating is not None else rating
        self.on_change = on_change or (lambda x: None)
        self.row_elements: list[ft.IconButton] = []
        self.references: list[ft.Ref] = []

        self._add_cancel()
        self._add_elements()

    def _add_elements(self):
        for i in range(0, self.elements):
            element_ref = ft.Ref[ft.IconButton]()
            self.references.append(element_ref)
            is_selected = True if self.rating is not None and i <= self.rating else False
            self.row_elements.append(
                ft.IconButton(
                    icon=ft.icons.STAR_BORDER,
                    ref=element_ref,
                    icon_color=ft.colors.GREY,
                    selected_icon=ft.icons.STAR,
                    selected_icon_color=ft.colors.BLUE,    
                    data=i,
                    selected=is_selected,
                    disabled=self.disabled,
                    on_click=self._select
                    )
            )

    def _add_cancel(self):
        if self.cancel:
            self.row_elements.append(
                ft.IconButton(
                    icon=ft.icons.CANCEL_OUTLINED,
                    icon_color=ft.colors.RED,
                    on_click=self._reset
                )
            )

    def _reset(self, e):
        if self.readonly:
            return
        for i in range(self.elements-1, -1, -1):
            ref: ft.Ref[ft.IconButton] = self.references[i]
            ref.current.selected = False
            self.rating = None
        self.update()


    def _select(self, e):
        if self.readonly:
            return
        
        if(self.rating is not None and e.control.data == self.rating):
            self._reset(e)
        else:
            for i in range(self.elements-1, -1, -1):
                if e.control.data >= i:
                    ref: ft.Ref[ft.IconButton] = self.references[i]
                    ref.current.selected = True
                else:
                    ref: ft.Ref[ft.IconButton] = self.references[i]
                    ref.current.selected = False
            self.rating = e.control.data
        self._on_change(self.rating)
        self.update()
        
    def _on_change(self, e) -> None:
        if e is not None:
            self.on_change(e+1)
        else:
            self.on_change(0)

    def build(self):
        self.row = ft.Row(
            self.row_elements,
            spacing=0
        )
        return self.row
    
    def did_mount(self):
        return super().did_mount()

    def will_unmount(self):
        return super().will_unmount()