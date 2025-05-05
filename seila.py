#Importação da página
from flet import *

#Configurações da página
def main(page: Page):
    page.window.center()
    page.window.width = 768
    page.window.height = 527
    page.bgcolor = "#ffffff"
    page.padding = 0
    page.window_resizable = False
    page.window_maximizable = False

    def logg(e):
        if email.value == "mariadasilvaserafim42@gmail.com" and password == "maria123":
            page.go()
        else:
            page.snack_bar = SnackBar(Text("Login Inválido"))
            page.snack_bar.open = True
            page.update

    def cadast(e):

        login.visible = False
        cadastro.visible = True
        page.update()

    #Objetos de login da página de Login
    lgn = Text("Login", height = 150, color = "#000000", size = 60, weight = FontWeight.W_900)
    lgn2 = TextButton(text = "Ou se não tem cadastro, fazer cadastro agora!", style = ButtonStyle(color = "#000000"))
    email = TextField(label = "Email", prefix_icon = icons.EMAIL, width = 300, border_radius = 20)
    password = TextField(label = "Senha", prefix_icon = icons.PASSWORD, can_reveal_password = True, password = True, width = 300, border_radius = 20)
    button2 = CupertinoButton(text = "Voltar", color = "#000000", bgcolor = "#ffffff", on_click = logg)
    
    #Imagem de login
    img1 = Image(
        src = "sistema escolar\hacker.png",
        width = 300,
        height = 10,
        fit = ImageFit.CONTAIN,
    )

    btn1 = ElevatedButton(text = "Login", bgcolor = "#000000", color = "#ffffff")

    #-------------------------------------------------------------------------------------------------------------------------------

    #Objetos de cadastro da página de Cadastro
    cad = Text("Cadastro", height = 150, color = "#000000", size = 60, weight = FontWeight.W_900)
    log = Text("Possui cadastro? Fazer login!", color = "#000000", size = 20)
    cademail = TextField(label = "Cadastre seu email", prefix_icon = icons.EMAIL, width = 300, border_radius = 20)
    password1 = TextField(label = "Crie sua senha", prefix_icon = icons.PASSWORD, can_reveal_password = True, password = True, width = 300, border_radius = 20)
    password2 = TextField(label = "Confirme sua senha", prefix_icon = icons.PASSWORD, can_reveal_password = True, password = True, width = 300, border_radius = 20)
    button1 = CupertinoFilledButton(text = "Entrar", on_click = cadast)
    
    #Imagem de cadastro
    img2 = Image(
        src = "sistema escolar\imglogin.png",
        width = 150,
        height = 150,
        fit = ImageFit.CONTAIN,
    )

    btn2 = ElevatedButton(text = "Cadastrar", bgcolor = "#000000")

    login = Row([

         Container(height = 490, width = 358, bgcolor = "#ffffff",
                  
                  content = Column([lgn, email, password, btn1, lgn2], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER)),

        Container(height = 490, width = 385, bgcolor = "#000000", 
                  border_radius = border_radius.only(top_left = 150, bottom_left= 150), padding = 100,
                  
                  content = Column([img2, button1
                                 
                                 ], alignment = MainAxisAlignment.CENTER, horizontal_alignment = CrossAxisAlignment.CENTER))

    ], vertical_alignment = CrossAxisAlignment.CENTER, alignment = MainAxisAlignment.CENTER)
    

    cadastro = Row([

        Container(height = 490, width = 385, bgcolor = "#000000",
                  border_radius = border_radius.only(top_right = 150, bottom_right = 150), padding = 100,

                  content = Row([img2, button2
                                 
                                 ], alignment = MainAxisAlignment.CENTER, vertical_alignment = CrossAxisAlignment.END)), 

        Container(height = 490, width = 358, bgcolor = "#ffffff", padding = 30,
                  content = Column([cad, log, cademail, password1, password2, btn2
                                    ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER))
                                
                  
    ], vertical_alignment = CrossAxisAlignment.CENTER, alignment = MainAxisAlignment.CENTER)


   
    
    page.add(login, cadastro)
app(target = main)
