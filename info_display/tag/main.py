import flet as ft

from tag import Tag

def main(page: ft.Page):

    examples = ft.Column([
        ft.Text("Basic example"),
        Tag(page, text="Top"),
        ft.Divider(),
        ft.Text("Icon"),
        Tag(page, text="Greatest Hits", icon=ft.Icon(ft.icons.ALBUM)),
        ft.Divider(),
        ft.Text("Pill"),
        Tag(page, text="Pop", icon=ft.Icon(ft.icons.ALBUM), pill=True),
        ft.Divider(),
        ft.Text("Severity"),
        ft.Row([
            Tag(page, text="Primary", severity='primary'),
            Tag(page, text="Success", severity='success'),
            Tag(page, text="Warning", severity='warning'),
            Tag(page, text="Danger", severity='danger'),
        ]),
        
        ft.Divider(),
    ])

    page.add(examples)

ft.app(main)