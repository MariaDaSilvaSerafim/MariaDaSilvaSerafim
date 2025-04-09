import flet as ft
import pandas as pd

#Configuração para Criação da Página de Banco
def main(page: ft.Page):
    #page.bgcolor = '#5A98BF3'
    page.window_center()
    page.window_width = '1000'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False

    nome = ft.TextField(label = 'Nome', border_radius = 30)
    btn = ft.FilledButton(text = 'Salvar', on_click = lambda e: Salvardados())


    def Salvardados (e):

        n = nome.value()




        if n:

            nome.value = ''

        page.add()    
        
                    
    page.add(nome, btn)

ft.app(target = main)
