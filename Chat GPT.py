#Importar a Bibliteca Flet
import flet as ft
import openai as op

#Comando da Página
def main(page: ft.Page):

    #Minha Chave Secreta
    op.api_key = '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'


    def resposta(mensagem):
        response = op.Completion.create(

            engine = "text-davinci-003",
            prompt = mensagem,
            max_tokens = 150,
            temperature = 0.7

        )
        return response.choices[0].text.strip()

    #Abrir a página da Biblioteca para tela de Cadastro
    page.title = 'ChatGPT'
    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '1200'
    page.window_height = '650'
    page.window_resizable = False
    page.window_maximizable = False
    page.vertical_alignment = 'Center'

    #Configurações de Texto
    t1 = ft.Text("Como posso ajudar?", size = 30, color = '#000000', weight = ft.FontWeight.W_500)
    ctf1 = ft.CupertinoTextField("Envie uma mensagem para o ChatGPT", width = 450, height = 50, border_radius = 30)
    btn1 = ft.FilledButton(content = ft.Text("Enviar"), width = 153, height = 45, on_click = lambda e: enviar (e), style = ft.ButtonStyle(bgcolor = '#000000', color = '#FFFFFF'))

    #Comando Column
    col = ft.Column()

    #Função Enviar
    def enviar(e):
        mensagem = ctf1.value

        if mensagem:

            col.controls.append(ft.Text(f"Você: {mensagem}")),
            col.controls.append(ft.Text(f"Pensando...: ", size = 16, italic = True))
            
            resp = resposta(mensagem)

            resposta.controls.append(ft.Text(f"ChatGPT: {resp}", size = 16))

            ctf1.value = ""
            page.update()



    r = ft.Column([
        t1,
        ft.Row([
            ctf1,
            btn1,
            ], alignment = ft.MainAxisAlignment.CENTER)
            ,col

    ], spacing = 30, horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)


    page.add(r)
ft.app(target = main)
