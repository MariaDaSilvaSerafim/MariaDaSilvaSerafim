import flet as ft

def main(page: ft.Page):

    page.bgcolor = '#808080'
    page.window_center()
    page.window_width = '450'
    page.window_height = '700'
    page.window_resizable = False
    page.padding = 10
    page.window_maximizable = False
    page.horizontal_alignment = 'Center'

    c1 = ft.Container(width = 300, height = 75)
   
    t1 = ft.TextField(label='Email', width = 355, height = 50)
    t2 = ft.TextField(label='Password', width = 355, height = 50)
    btn1 = ft.CupertinoFilledButton(text='Login', width = 355, height = 50)   
   
    
    
    r1 = ft.Row(alignment = ft.MainAxisAlignment.CENTER,
    
    controls=[

          ft.CupertinoFilledButton(text='Google', width = 173, height = 50, padding = 5),
          ft.CupertinoFilledButton(text='Facebook', width = 173, height = 50, padding = 5)   
      
    ])

    img = ft.Image(
        src = f"Roblox.jpg", 
        width = 400, height = 150, 
        fit = ft.ImageFit.CONTAIN,
        border_radius = 45
    )

    c2 = ft.Container(width = 175, height = 75)

    btn_registre = ft.TextButton(text = 'Não possui conta. Rgistre-se Agora', on_click = True)
    btn_registre.width = '500'

    page.add(c1, img, t1, t2, btn1, r1, c2, btn_registre)
ft.app(target = main)    
