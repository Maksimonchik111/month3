import flet as ft

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    text_hello = ft.Text("Hello", color=ft.Colors.RED_900, size=20)

    greeting_history = []

    greeting_text = ft.Text("История заполения: ")

    def text_name(e):
        
        name = text_input.value.strip()
        
        if name.isdigit():
            text_hello.value = "Имя не может состоять из цифр!"
            text_hello.color = ft.Colors.RED
            text_input.value = ''
        
        elif len(name) < 2:
            text_hello.value = "Имя не может состоять из менее чем 2х символов"
            text_hello.color = ft.Colors.RED
            text_input.value = ''
        
        elif name in greeting_history:
            text_hello.value = "Это имя уже в истории!"
            text_hello.color = ft.Colors.RED
            text_input.value = ''
    
        elif name:
            text_hello.value = f"Hello, {name}"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ''
            
            greeting_history.insert(0, name)
            
            if len(greeting_history) > 5:
                greeting_history.pop() 
            
            greeting_text.value = "История заполнения:\n" + "\n".join(greeting_history)
            text_input.value = ""
        else:
            text_hello.value = "Введите имя пожалуйста!!!"
            text_hello.color = ft.Colors.RED_900
              

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        elif page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            print("Ошибка")    

    def clear_history(e):
        greeting_history.clear()   
        greeting_text.value = 'История заполнения'
        

    text_input = ft.TextField(label="Введите свое имя", on_submit=text_name, expand=True)

    text_button = ft.ElevatedButton("Send", on_click=text_name)
    
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=change_theme)

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    top_row = ft.Row([theme_button, clear_button], alignment=ft.MainAxisAlignment.END)
    input_row = ft.Row([text_input, text_button])

    layout = ft.Column(
        controls=[
            top_row,
            ft.Divider(), # Визуальный разделитель
            text_hello,
            input_row,
            greeting_text
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=400)


    page.add(layout)

    
ft.app(target=main)