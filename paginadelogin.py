#Importar a Bibliteca Flet
import flet as ft


def main(page: ft.Page):

    #Abrir a página da Biblioteca para tela de Cadastro
    page.bgcolor = '#5A98BF3'
    page.window_center()
    page.window_width = '1000'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = 'start'

    #Entrada de Dados
    r1 = ft.Row([

        ft.Container(
        bgcolor = "#FFFFFF", 
        width = 450, 
        height = 540,
        border_radius = 5,

        content = ft.Column([

            ft.Text("Faça Seu Login", size = 40, color = '#000000', weight = ft.FontWeight.W_900, selectable = True),
            
            ft.Container(content = ft.Column([

                    ft.TextField(label = 'Digite seu E-Mail', prefix_icon = ft.icons.EMAIL, width = 350, border_radius = 30),
                    ft.TextField(label = 'Digite sua Senha', prefix_icon = ft.icons.PASSWORD, width = 350, can_reveal_password = True, password = True, border_radius = 30),
                    
                    ])
            
            ),

            
            ft.FilledButton(content = ft.Text('Entrar'), width = 173, height = 50, on_click = lambda e: entrar (e), style = ft.ButtonStyle(bgcolor = '#000080', color = '#FFFFFF')),           
            ft.CupertinoButton(text = ('Esqueceu sua Senha?'), on_click = True, color = '#191970')

         ],  spacing= 30, horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)
    ),


    #Configuração da Imagem
    
    
    
    ft.Container(

        
        width = 510, 
        height = 540,
        
        content = ft.Column([
    
            ft.Image(src = ("login-seguro.png"), fit = ft.ImageFit.CONTAIN, width = 300, height = 300),
            ft.Text("A melhor experiência de login \n que você já teve na sua vida", size = 22, color = '#FFFFFF'),
            
            
            ], spacing = 50, horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)
        )
    ])
    
    #Sistema de Cadastro
    cadastro = ft.Column([ 
        
            ft.Container(
        
        bgcolor = '#FFFFFF',
        width = 1000,
        height = 280,
        border_radius = 5,
        padding = 30, 

        content = ft.Column([
             
             ft.Text('Dados do Usuário',size = 20, color = '#000000', weight = ft.FontWeight.W_500, selectable = True),
             ft.Row([
                 
                 ft.TextField(label = 'CPF',  width = 250, border_radius = 5,),
                 ft.TextField(label = 'Nome',  width = 350, border_radius = 5),

             ]),
             ft.Row([
                
                 ft.TextField(label = 'Nome da Mãe', width = 350, border_radius= 5),

             ]),

              ft.IconButton(
                    icon = ft.icons.EXIT_TO_APP,
                    icon_color = '#000000',
                    icon_size = 40,
                    on_click = True
                ),

            

        ], spacing= 20,)

    ),

    ft.Container(

                bgcolor = '#FFFFFF',
                width = 1000,
                height = 240,
                border_radius = 5,

                content = ft.Column([
                
                ft.DataTable(
                columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                        ],
                    ),
                ],
            )
        ])
    ) 
])

    
      

    def entrar(e: ft.ControlEvent):
        page.remove(r1)
        page.add(cadastro)

    def Voltar(e: ft.ControlEvent):
        page.remove(cadastro)
        page.add(r1)  

    #def validaracesso(e: ft.ControlEvent):
        #page.remove()    

    #Fechamento da página de Login
    page.add(r1)

ft.app(target = main)
