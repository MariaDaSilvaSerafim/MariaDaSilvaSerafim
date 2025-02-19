#Importar a Bibliteca Flet
import flet as ft
import openai as op


def main(page: ft.Page):

    op.api_key = 'Sk-... pJIA'

    #Abrir a página da Biblioteca para tela de Cadastro
    page.title = 'ChatGPT'
    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '1200'
    page.window_height = '650'
    page.window_resizable = False
    page.window_maximizable = False
    #page.vertical_alignment = 'Center'

    r = ft.Column([

        ft.Text("Como posso ajudar?", size = 30, color = '#000000', weight = ft.FontWeight.W_500),
    
    

        ft.Row([

            ft.CupertinoTextField("Envie uma mensagem para o ChatGPT", width = 450, height = 50, border_radius = 30),

            ft.FilledButton(content = ft.Text("Enviar"), width = 153, height = 45, on_click = lambda e: entrar (e), style = ft.ButtonStyle(bgcolor = '#000000', color = '#FFFFFF')),
        
            ], alignment = ft.MainAxisAlignment.CENTER)

    ], spacing = 30, horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)


    executado = ft.Row([

        ft.Text("Como posso ajudar?", size = 30, color = '#000000', weight = ft.FontWeight.W_500)

    ],  alignment = ft.MainAxisAlignment.END)


    def entrar(e: ft.ControlEvent):
        page.remove(r)
        page.add(executado)

    page.add(r)
ft.app(target = main)
