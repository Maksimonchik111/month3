import flet as ft

def main(page: ft.Page):
    page.title = "Проверка возраста"

    def age_validator(e):
        age = age_input.value.strip()
        if not age or not age.isdigit():
            age_info.value = "Введите конкретный возраст"
            age_info.color = ft.Colors.YELLOW
        else:
            if int(age) >= 18:
                age_info.value = 'Доступ разрешен'
                age_info.color = ft.Colors.GREEN
            else:
                age_info.value = "Доступ запрещен"
                age_info.color = ft.Colors.RED
        age_input.value = ''    



    age_info = ft.Text('')

    age_input = ft.TextField(label="Введите ваш возраст: ", on_submit=age_validator)
    
    btn = ft.IconButton(icon=ft.Icons.SEND, on_click=age_validator)

    page.add(age_info, age_input, btn )

ft.app(target=main)
