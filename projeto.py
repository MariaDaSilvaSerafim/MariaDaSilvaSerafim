import flet as ft

def main(page: ft.Page):
    page.window.center()
    page.window.width = 1200
    page.window.height = 650
    page.bgcolor = "#ffffff"
    page.window.title_bar_hidden = True
    
    t1 = ft.Container(
        width = 200,
        height = 645,
        bgcolor = "#000000",
        padding = 20,
        
        content = ft.Column([
            ft.Row([
                ft.IconButton(icon = ft.icons.HOME, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Início", color = "#ffffff", size = 15),
            ]),

            ft.Row([
                ft.IconButton(icon = ft.icons.PEOPLE_ALT, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Alunos", color = "#ffffff", size = 15)
            ]),

            ft.Row([
                ft.IconButton(icon = ft.icons.FAMILY_RESTROOM, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Responsáveis", color = "#ffffff", size = 15)
            ]),

            ft.Row([
                ft.IconButton(icon = ft.icons.ATTACH_MONEY, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Financeiro", color = "#ffffff", size = 15)
            ]),

            ft.Row([
                ft.IconButton(icon = ft.icons.SCHOOL_SHARP, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Turma", color = "#ffffff", size = 15)
            ]),
            
            ft.Row([
                ft.IconButton(icon = ft.icons.MENU_BOOK, icon_color = "#ffffff", icon_size = 30),
                ft.Text("Disciplina", color = "#ffffff", size = 15)
            ]),

            ft.Container(height = 180),

            ft.Divider(color = "#ffffff"),

            ft.Row([
                ft.IconButton(icon = ft.icons.EXIT_TO_APP_SHARP, icon_color = "#ffffff", icon_size = 30, on_click = lambda e: sair(e)),
                ft.Text("Sair", color = "#ffffff", size = 15)
            ])

        ])
    )

    def sair(e):
        page.window.close()

        page.update()

    inicio = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Sair", color = "#ffffff", size = 15))
    
    alunos = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.DataTable(
                                columns = [
                                        ft.DataColumn(ft.Text("First name")),
                                        ft.DataColumn(ft.Text("Last name")),
                                        ft.DataColumn(ft.Text("Age"), numeric=True),
                                    ],)
                        )
    
    responsaveis = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Sair", color = "#ffffff", size = 15))
    
    financeiro = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Sair", color = "#ffffff", size = 15))
    
    turma = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Sair", color = "#ffffff", size = 15))
    
    disciplinas = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Sair", color = "#ffffff", size = 15))

    page.add(ft.Row([t1, inicio]))
ft.app(target = main)
