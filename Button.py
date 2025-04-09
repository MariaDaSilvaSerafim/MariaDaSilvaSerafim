import flet as ft

def main(page: ft.Page):

    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '350'
    page.window_height = '600'
    page.window_resizable = False
    page.padding = 10
    page.window_maximizable = False

    

    c1 = ft.Container(width = 310, height = 75, bgcolor = "#000000", border_radius=10)

    r1 = ft.Row([

        ft.Container(width = 150, height = 150, bgcolor = "#000000", border_radius=10),  
        

        ft.Container(width = 150, height = 150, bgcolor = "#000000", border_radius=10)

    ])

    rbutton = ft.Row([

        ft.ElevatedButton("Acessar", width = 150),
        ft.ElevatedButton("Acessar", width = 150)
    ])


    r2 = ft.Row([

        ft.Container(width = 150, height = 150, bgcolor = "#000000", border_radius=10), 
        ft.Container(width = 150, height = 150, bgcolor = "#000000", border_radius=10)

    ])

    rbutton2 = ft.Row([

        ft.ElevatedButton("Acessar", width = 150),
        ft.ElevatedButton("Acessar", width = 150)
    ])
    
    page.add(c1, r1, rbutton, r2, rbutton2)


ft.app(target = main)
