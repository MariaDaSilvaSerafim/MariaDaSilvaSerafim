import flet as ft

lista = []

def main(page: ft.Page):

    
    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '350'
    page.window_height = '450'
    page.window_resizable = False
    page.padding = 75
    page.window_maximizable = False

    n1 = ft.TextField(label = "Nome",
            width = '400')

    def reservar(e):

        nome = str(n1.value)  
        
            
        if nome:
            
            lista.append(f'Olá seu nome é: {nome}')    
            
            n1.value = ""
            
            


            listar_dados.controls.append(ft.Text(f'Olá seu nome é: {nome}'))
            page.update()





    btn = ft.FilledButton(text = "Salvar", on_click = reservar, width = 200)

    listar_dados = ft.Column()


    page.add(n1, btn, listar_dados)
ft.app(target = main)
