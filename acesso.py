import flet as ft, pyautogui

acesso = []


def inicio(page: ft.Page):

    
    page.bgcolor = '#FFFFFF'
    page.window_center()
    page.window_width = '400'
    page.window_height = '550'
    page.window_resizable = False
    page.padding = 10
    page.window_maximizable = False

    c1 = ft.Container(content = ft.Text(""), 
                    width = 500, height = 100, border_radius = 5)


    
    def acessaredge(e):
        pyautogui.press('Win')
        pyautogui.write('Edge')
        pyautogui.press('Enter')    
        page.update()

    def acessarcal(e):
        pyautogui.press('Win')
        pyautogui.write('Calculadora')
        pyautogui.press('Enter')    
        page.update()



    btn_edge = ft.ElevatedButton(text = "Edge", on_click = acessaredge, width = 100)
    btn_cal = ft.ElevatedButton(text = "Cal", on_click = acessarcal, width = 100)


    page.add(c1, btn_edge, btn_cal)
    
ft.app(inicio)
