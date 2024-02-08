import flet as ft
from flet import *

import flet.canvas as Cv

#perol = Cv.Rect(0, 0, 573, 174, border_radius=60, paint=ft.Paint(color="#925219"))
#barras = Cv.Rect(0, 0, 54, 28, border_radius=0, paint=ft.Paint(color="#565656"))

#rincom = ft.Row(controls=[ft.Stack([Cv.Canvas([perol, barras])])], )

def main(page: ft.Page):

    perol = Cv.Rect(page.width/3, 0, 573, 174, border_radius=60, paint=ft.Paint(color="#925219"))
    Contactos = Cv.Rect(page.width/3.5, 80, 677, 28, border_radius=0, paint=ft.Paint(color="#565656"))

    rincom = ft.Row(controls=[ft.Stack([Cv.Canvas([Contactos, perol], expand=True)])], )

    page.add(rincom)

ft.app(target=main)