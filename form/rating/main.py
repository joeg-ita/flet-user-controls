import flet as ft

from rating import Rating

def main(page: ft.Page):
    def rating_cb(e):

        cb.value = f"Callback {e}"
        page.update()

    cb = ft.Text("Callback")

    examples = ft.Column([
        ft.Text("Basic example"),
        Rating(),
        ft.Divider(),
        ft.Text("Cancel"),
        Rating(cancel=True),
        ft.Divider(),
        ft.Text("Readonly"),
        Rating(readonly=True, rating=3),
        ft.Divider(),
        ft.Text("Disabled"),
        Rating(rating=4, disabled=True),
        ft.Divider(),
        cb,
        Rating(on_change=rating_cb)
    ])

    page.add(examples)

ft.app(main)