import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#F2B835"
    page.window_width = 300
    page.window_height = 600
    page.window_resizable = False

    img = ft.Image(
        src=f"/images/my_icon.png",
        width=100,
        height=100, 
    )
    page.add(img)

    page.add(
        ft.Text(
            "\"This app is to help you think "
            "positive and keep those healthy " 
            "affirmations in your head.\"",
            size=19,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
            italic=True,
        )
        
    )

    page.update()


ft.app(target=main, assets_dir="assets")







