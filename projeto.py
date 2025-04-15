import flet as ft

def main(page: ft.Page):
    page.window.center()
    page.window.width = 1200
    page.window.height = 650
    page.bgcolor = "#1c1c1c"
    page.window.title_bar_hidden = True
    page.padding = 0
    
    containermenu = ft.Container(
        width = 200,
        height = 645,
        bgcolor = "#000000",
        padding = 20,
        
        content = ft.Column([
            ft.Row([
                ft.IconButton(icon = ft.icons.HOME, icon_color = "#ffffff", icon_size = 30, on_click =lambda e: ini(e)),
                ft.Text("Início", color = "#ffffff", size = 15),
            ]),

            ft.Row([
                ft.IconButton(icon = ft.icons.PEOPLE_ALT, icon_color = "#ffffff", icon_size = 30, on_click = lambda e: alu(e)),
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

    inicio = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Row([
                          ft.Container(
                              bgcolor = "#4f4f4f",
                              width = 220,
                              height = 200,
                              border_radius = 10
                          ),

                          ft.Container(
                              bgcolor = "#4f4f4f",
                              width = 220,
                              height = 200,
                              border_radius = 10
                          ),

                          ft.Container(
                              bgcolor = "#4f4f4f",
                              width = 220,
                              height = 200,
                              border_radius = 10
                          ),

                          ft.Container(
                              bgcolor = "#4f4f4f",
                              width = 220,
                              height = 200,
                              border_radius = 10
                          )
                      ], alignment = ft.MainAxisAlignment.CENTER, vertical_alignment = ft.CrossAxisAlignment.START)
                        
                      
                    )

    alunos = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.DataTable(
                                columns = [
                                        ft.DataColumn(ft.Text("Nome")),
                                        ft.DataColumn(ft.Text("Matrícula")),
                                        ft.DataColumn(ft.Text("Turma")),
                                        ft.DataColumn(ft.Text("Ações")),
                            ])
                )
    
    responsaveis = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Página dos Responsáveis", color = "#ffffff", size = 30))
    
    financeiro = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Página do Financeiro", color = "#ffffff", size = 30))
    
    turma = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Página da Turma", color = "#ffffff", size = 30))
    
    disciplinas = ft.Container(width = 965, height = 620, padding = 20, 
                      content = ft.Text("Página das Disciplinas", color = "#ffffff", size = 30))
    
    def ini(e:ft.ControlEvent):
        
        page.remove(containermenu)
        page.add(ft.Row([containermenu, inicio]))

    def alu(e: ft.ControlEvent):

        page.close(containermenu)
        page.add(ft.Row([containermenu, alunos]))

    def sair(e):
        page.window.close()

        page.update()

    page.add(containermenu)
ft.app(target = main)
