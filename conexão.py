import sqlite3 as db
from sqlite3 import *
import flet as ft

def conectardb():
    try:
        con = db.connect("Bancoteste.db")
        return con, "Conectado com Sucesso!"
    
    except Error as e:
        return None, f"Erro ao Conectar: {e}"
    
def concreate(con, nome):
    try:
        cursor = con.cursor()
        query = "INSERT INTO pessoa (NOME) VALUES (?)"
        cursor.execute(query, (nome,))
        con.commit()
        return "Nome Inserido com Sucesso!"

    except Error as e:
        return f"Acesso Negado! {e}"
    
def main(page: ft.Page):

    tx = ft.TextField(label = "Nome")
    btn2 = btn = ft.ElevatedButton("Salvar", bgcolor = "#000000", on_click = lambda e: create (e))
    text = ft.Text(value = "Banco: Não Conectado", color = "Red")
    btn = ft.ElevatedButton("Testar", bgcolor = "#000000", on_click = lambda e: status(e))
    imprimir = ft.Text(value = "")

    def status(e):
        con, status = conectardb()
        tx.value = ""

        if con:
            text.value = "Banco: Conectado"
            text.color = "Green"
            con.close()
        else:
            text.value = status
            text.color = "Red"

        page.update()

    def create(e):
        nome = tx.value

        if nome:
            conn, status = conectardb()
            if conn:
                result = concreate(conn, nome)
                imprimir.value = result
                conn.close()    # Fechar a conexão após a inserção
            else:
                imprimir.value = status
        else:
            imprimir.value = "Por favor, Insira um Nome."
        page.update()

    page.add(tx, btn2, text, btn, imprimir)
ft.app(target = main)
