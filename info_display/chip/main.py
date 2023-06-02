import flet as ft

from chip import Chip

def main(page: ft.Page):

    examples = ft.Column([
        ft.Text("Basic example"),
        Chip(page, text="Homepage"),
        ft.Divider(),
        ft.Text("Custom Icon"),
        Chip(page, text="Alarm", icon=ft.Icon(ft.icons.ALARM)),
        ft.Divider(),
        ft.Text("Removable"),
        Chip(page, text="Homepage", removable=True),
        ft.Divider(),
    ])

    page.add(examples)

ft.app(main)