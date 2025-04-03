import flet as ft



to_do = {}



def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def todo(to_do):
        pass

    page.title = "Visualização"
    
    page.appbar = ft.AppBar(
        

    )
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    page.update()

    
    

ft.app(main)
