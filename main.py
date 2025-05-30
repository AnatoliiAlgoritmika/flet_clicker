import flet as ft

def main(page: ft.Page):
    page.title = "Telegram Clicker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    counter = ft.Text("0", size=50)
    clicks = 0
    
    def on_image_click(e):
        nonlocal clicks
        clicks += 1
        counter.value = str(clicks)
        page.update()
    
    def reset_counter(e):
        nonlocal clicks
        clicks = 0
        counter.value = "0"
        page.update()
    
    clickable_image = ft.GestureDetector(
        content=ft.Image(
            src="assets/p.png",  # или локальный путь (/assets/image.png)
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN
        ),
        on_tap=on_image_click
    )
    
    page.add(
        ft.Column(
            [
                counter,
                clickable_image,
                ft.ElevatedButton("Сброс", on_click=reset_counter, width=200)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# Режим для статического экспорта (без сервера)
ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")