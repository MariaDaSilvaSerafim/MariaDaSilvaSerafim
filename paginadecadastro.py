import flet as ft

def main(page: ft.Page):

    page.bgcolor = '#000000'
    page.window_center()
    page.window_width = '1000'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = 'start'

    r1 = ft.Row([

        ft.Container(
        bgcolor = "#FFFFFF", 
        width = 450, 
        height = 540,
        border_radius = 5,
        padding = 80,

        content = ft.Column([

            ft.Text("Faça Seu Cadastro", size = 40, color = '#000000'),
            ft.TextField(label = 'Usuário', icon = ft.icons.ACCOUNT_BOX, width = 460,autofocus=True),
            ft.TextField(label = 'E-Mail', icon = ft.icons.ACCOUNT_BOX, width = 460),
            ft.TextField(label = 'Senha', icon = ft.icons.PASSWORD_SHARP, width = 460, can_reveal_password = True, password = True),
            ft.TextField(label = 'CPF', icon = ft.icons.ACCOUNT_BOX, width = 460),
            ft.TextField(label = 'Endereço', icon = ft.icons.ACCOUNT_BOX, width = 460),
            ft.FilledButton(content = ft.Text('Entrar'), width = 173, height = 50, on_click = True, style = ft.ButtonStyle(bgcolor = '#000080', color = '#FFFFFF')),
            ft.TextButton(text = ('Esqueceu sua Senha?'), on_click = True), 
            ft.TextButton(text = ('Já possui conta. Faça seu Login Agora'), on_click = True)         
            
         ],  horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER,)
    ),

    
    ft.Container(

        
        width = 510, 
        height = 540,
        content = ft.Column([
    
            ft.Image(src = ("hacker2.png"), fit = ft.ImageFit.CONTAIN, width = 200, height = 200),
            ft.Text("Faça Seu Login", size = 40, color = '#000000'),
            
            
            ], spacing = 30, horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)
    )
])

    page.add(r1)

ft.app(target = main)
