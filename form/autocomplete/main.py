import flet as ft

from autocomplete import Autocomplete

def main(page: ft.Page):

    examples = ft.Column([
        ft.Text("Autocomplete basic example"),
        Autocomplete(),
        ft.Divider()
    ])

    page.add(examples)

ft.app(main)