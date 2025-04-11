from turtle import bgcolor, onkeypress
import flet as ft



to_do = {}



def Adicionar_Tarefa():

    pass







def main(page: ft.Page):

    def Create_Task():
        page.route = "/Criar_Task"
        #pass
    
    def route_change():

    
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def todo(to_do):
        pass

    page.title = "Visualização"
    
    page.appbar = ft.AppBar(
        
        leading= ft.IconButton(ft.icons.MENU),
        leading_width= 75,
        title=  ft.Text(page.title),color=ft.colors.BACKGROUND,
        bgcolor= ft.Colors.INVERSE_SURFACE,center_title= True,



    )
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click= Create_Task())
    page.update()

    
    

ft.app(main)
