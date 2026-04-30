import flet as ft

def main(page: ft.Page):
    page.title = "Счетчик нажатий"


    count = 0
    text_hello = ft.Text("Нажато 0 раз:")

    def button_clicker(e):
        nonlocal count
        count += 1
        text_hello.value = f'Нажато {count} раз'
        page.update()
    
    button = ft.ElevatedButton("Click", on_click=button_clicker)

    page.add(text_hello, button)

ft.app(target=main)