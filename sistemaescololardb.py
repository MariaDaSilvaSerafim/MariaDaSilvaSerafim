from flet import *
from sqlite3 import Error
from conexaodb import *

def main(page: Page):

    t1 = TextField(label = "Nome")
    btn1 = FilledButton(text = "Salvar", on_click = lambda e: salvar(e))
    btn2 = FilledButton(text = "Conect", on_click = lambda e: create(e))
    g = Text("", size = 50)

    def salvar(e):

        if t1.value == "Maria":

            g.value = "Correto"
            g.color = "Green"

        else:
            g.value = "Incorreto"
            g.color = "Red"

        page.update()

    def create(e):

        nome = t1.value
        t1.value = ""

        if t1:
            conn, salvar = conectar_banco()
            if conn:
                result = inserir_nome(conn, nome)
                g.value = result
                conn.close()
            else:
                g.value = salvar
        else:
            t1.value = "Por favor, insira um nome!"
        
        page.update()

    page.add(t1, btn1, btn2, g)
app(target = main)
