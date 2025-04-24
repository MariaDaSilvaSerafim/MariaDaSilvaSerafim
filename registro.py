from flet import *

def main(page: Page):
    page.window.center()
    page.window.width = 768
    page.window.height = 500
    page.bgcolor = "#ffffff"
    page.padding = 0

    lgn = Text("Sign In", color = "#000000", size = 40, weight = FontWeight.W_900)
    lgn2 = Text("Ou se não tem cadastro, fazer cadastro agora!", color = "#000000")
    email = TextField(label = "Email", prefix_icon = icons.EMAIL)
    password = TextField(label = "Senha", prefix_icon = icons.PASSWORD, can_reveal_password = True, password = True)
    button1 = FilledButton(text = "Entrar", on_click = lambda e: entrar(e))
    button2 = FilledButton(text = "Voltar", on_click = lambda e: voltar(e))

    cadastro = Row([

        Container(height = 490, width = 385, bgcolor = "#000000",
                  border_radius = border_radius.only(top_right = 150, bottom_right = 150),

                  content = Row([button2
                                 
                                 ], alignment = MainAxisAlignment.CENTER, vertical_alignment = CrossAxisAlignment.CENTER)), 

        Container(height = 490, width = 385, bgcolor = "#ffffff",
                  content = Column([lgn, lgn2, email, password], ))
                                
                  
    ], vertical_alignment = CrossAxisAlignment.CENTER, alignment = MainAxisAlignment.CENTER)

    login = Row([

         Container(height = 490, width = 385, bgcolor = "#ffffff",
                  
                  content = Row([])),

        Container(height = 490, width = 385, bgcolor = "#000000", border_radius = border_radius.only(top_left = 150, bottom_left= 150),
                  content = Row([button1])
                  
                  )
    ])

    def entrar(e):
        cadastro.visible = True
        login.visible = False
        page.update()

    def voltar(e):

        login.visible = True
        cadastro.visible = False
        page.update()
    
    page.add(cadastro, login)
app(target = main)
