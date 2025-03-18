import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#1c1c1c"
    page.window.center()
    page.window.width = 430
    page.window.height = 490
    # page.vertical_alignment = "start"
    page.window.maximizable = False

    p = ft.Row([
        ft.Text("Padrão")
    ])
    
    
    resultado_texto = ft.Text(value = "0", size = 28, color = "white", text_align = "right")

    c = ft.Container(height = 80)


    c1 = ft.Container(
        content = resultado_texto,
        bgcolor = "#4f4f4f",
        padding = 10,
        border_radius = 10,
        height = 70,
        alignment = ft.alignment.center_right
    )


    c2 = ft.Row([

        ft.ElevatedButton(text = ("%"), width = 90),
        ft.ElevatedButton(text = ("CE"), width = 90),
        ft.ElevatedButton(text = ("C"), width = 90),
        ft.ElevatedButton(content = ft.Icon(ft.icons.BACKSPACE), width = 90)
    ])

    c3 = ft.Row([

        ft.ElevatedButton(text = ("7"), width = 90),
        ft.ElevatedButton(text = ("8"), width = 90),
        ft.ElevatedButton(text = ("9"), width = 90),
        ft.ElevatedButton(text = ("÷"), width = 90)
    ])

    c4 = ft.Row([

        ft.ElevatedButton(text = ("4"), width = 90),
        ft.ElevatedButton(text = ("5"), width = 90),
        ft.ElevatedButton(text = ("6"), width = 90),
        ft.ElevatedButton(text = ("×"), width = 90)
    ])

    c5 = ft.Row([

        ft.ElevatedButton(text = ("1"), width = 90),
        ft.ElevatedButton(text = ("2"), width = 90),
        ft.ElevatedButton(text = ("3"), width = 90),
        ft.ElevatedButton(text = ("-"), width = 90)
    ])

    c6 = ft.Row([

        ft.ElevatedButton(text = ("+/-"), width = 90),
        ft.ElevatedButton(text = ("0"), width = 90),
        ft.ElevatedButton(text = (","), width = 90),
        ft.ElevatedButton(text = ("+"), width = 90)
    ])

    c6 = ft.Row([

        ft.ElevatedButton(text = ("="), width = 395)
    ])

    page.add(p, c, c1, c2, c3, c4, c5, c6)
ft.app(target = main)
