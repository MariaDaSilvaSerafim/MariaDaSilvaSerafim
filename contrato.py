import flet as ft

Contrato = []

def main(page: ft.Page):

    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '400'
    page.window_height = '550'
    page.window_resizable = False
    page.padding = 10
    page.window_maximizable = False


    n = ft.TextField(label = "Nome", autofocus = True)

    t = ft.TextField(label = "Telefone", autofocus = True, keyboard_type = ft.KeyboardType.PHONE)

    e = ft.TextField(label = "Email", autofocus = True, keyboard_type = ft.KeyboardType.EMAIL)

    c = ft.TextField(label = "CPF", autofocus = True, keyboard_type = ft.KeyboardType.NUMBER)

    dgl = ft.AlertDialog(
        title = ft.Text("Olá tudo bem?")
    )
    
    btn = ft.FilledButton(content = ft.Text("Imprimir Contrato"), width = 500,
                          on_click = lambda e: page.open(dgl))
    btn.bgcolor = '#4682B4'
    btn.width = '500'


    page.add(n, t, e, c, btn, dgl)
ft.app(target = main)
