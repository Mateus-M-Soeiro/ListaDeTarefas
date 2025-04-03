import flet as ft



todo = {}


def main(page: ft.Page):
    page.title = "Visualização"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_press = )
    
    

ft.app(main)
