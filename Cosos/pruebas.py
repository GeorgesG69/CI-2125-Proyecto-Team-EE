import flet as ft
from flet import *


def main(page: ft.Page):
    page.title = "Calculadora de Resistores" # Título del borde de la ventana
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ALWAYS

    def Titulo():

        Title = ft.Text(value="Calculadora de Resistores", size=33, font_family="Times New Roman") # Título del centro de la apliacción

        return ft.Row(controls=[Column(controls=[

            Title,
        ])], alignment=MainAxisAlignment.CENTER)
    
    
    Colores = ft.Row(expand=True, scale=1.25, width=174, height=677) # Bandas del resistor, cambian de color

    # Colores con sus códigos

    C_Negro = ["#000000", "0", "0", "0", " Ω", " ", "250 ppm/k"]    # Negro
    C_Marron = ["#883c00", "1", "1", "1", "0 Ω", "± 1%", "100 ppm/k"]    # Marrón
    C_Rojo = ["#ff0000", "2", "2", "2", "00 Ω", "± 2%", "50 ppm/k"]      # Rojo
    C_Naranja = ["#ff872e", "3", "3", "3", " kΩ", "± 0,05%", "15 ppm/k"]   # Naranja
    C_Amarillo = ["#f3e800", "4", "4", "4", "0 kΩ", "± 0,02%", "25 ppm/k"]  # Amarillo
    C_Verde = ["#28a700", "5", "5", "5", "00 kΩ", "± 0,5%", "20 ppm/k"]     # Verde
    C_Azul = ["#009bb6", "6", "6", "6", " MΩ", "± 0,25%", "10 ppm/k"]      # Azul
    C_Violeta = ["#8200e1", "7", "7", "7", "0 MΩ", "± 0,1%", "5 ppm/k"]   # Violeta
    C_Gris = ["#737373", "8", "8", "8", " 00 MΩ", "± 0,01%", "1 ppm/k"]      # Gris
    C_Blanco = ["#ffffff", "9", "9", "9", " GΩ", " ", " "]    # Blanco
    C_Dorado = ["#958000", " ", " ", " ", "x0,1 Ω", "± 5%", " "]    # Dorado
    C_Plateado = ["#b4b4b4", " ", " ", " ", "x0,01 Ω", "± 10%", " "]  # Plateado

    # Bandas

    B_1 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_2 = ft.Container(bgcolor="#ffffff", width=15, height=120, border=ft.border.all(2, "#000000"), )
    B_3 = ft.Container(bgcolor="#ffffff", width=15, height=120, border=ft.border.all(2, "#000000"), )
    B_4 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    BM_3 = ft.Container(bgcolor="#ffffff", width=15, height=120, border=ft.border.all(2, "#000000"), )
    BM_4 = ft.Container(bgcolor="#ffffff", width=15, height=120, border=ft.border.all(2, "#000000"), )
    B_T = ft.Container(bgcolor="#ffffff", width=15, height=120, border=ft.border.all(2, "#000000"), )
    B_TCR = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )

    # Función para cambiar la cantidad de bandas
    def Bandas_Resistor(e):

        # Los valores que aparecen en cada condicional, es decir "e.control.value" son introducidos
        # por los selectores en forma de punto. Los que se guardan en la variable "Selector".
        # "e" es la letra que representa el "evento" en la aplicación, específicamente en esta función
        # se trabaja con los eventos que envian los selectores de punto.

        # Cada punto agrega la cantidad de bandas sobre el dibujo del Bandas_Resistor. 
        # Es lo que hace cada condicional a continuación:

        if e.control.value == "1": 
            Menu.controls = [ 
                             S1, 
                             ft.VerticalDivider(width=50, opacity=0), 
                             S2, 
                             ft.VerticalDivider(width=120, opacity=0), 
                             SMultiplicador_3,
                             ]
            
            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            BM_3.bgcolor=C_Blanco[0]

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = "± 20%"
            Salida_de_TCR.value = " "

            Mostrar_Existencia.value = ""

            B_1.height = 120
            B_T.border = ft.border.all(2, "#000000")
            B_TCR.border = ft.border.all(2, "#000000")

            Colores.controls = [ft.VerticalDivider(width=130, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=70, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=130, opacity=0),
                                BM_3
                                ]
            
            
            page.update()
            
        elif e.control.value == "2":

            Menu.controls = [
                             S1,
                             ft.VerticalDivider(width=25, opacity=0), 
                             S2,
                             ft.VerticalDivider(width=40, opacity=0), 
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=40, opacity=0), 
                             STolerancia]
            
            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            BM_4.bgcolor=C_Blanco[0]
            B_T.bgcolor=C_Blanco[0]

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = " "
            Salida_de_TCR.value = " "

            Mostrar_Existencia.value = ""

            B_T.height = 120
            B_1.height = 120
            B_T.border = ft.border.all(2, "#000000")
            B_TCR.border = ft.border.all(2, "#000000")

            Colores.controls = [ft.VerticalDivider(width=130, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=30, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=70, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=67, opacity=0),
                                B_T
                                ]
                        
            page.update()

        elif e.control.value == "3":

            Menu.controls = [
                             S1,
                             ft.VerticalDivider(width=20, opacity=0), 
                             S2,
                             ft.VerticalDivider(width=20, opacity=0), 
                             S3,
                             ft.VerticalDivider(width=20, opacity=0),
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=110, opacity=0), 
                             STolerancia]
            
            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            BM_4.bgcolor=C_Blanco[0]
            B_3.bgcolor=C_Blanco[0]
            B_T.bgcolor=C_Blanco[0]

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = " "
            Salida_de_TCR.value = " "

            Mostrar_Existencia.value = ""

            B_T.height = 170
            B_1.height = 170
            B_T.border = ft.border.all(2, "#000000")
            B_TCR.border = ft.border.all(2, "#000000")

            Colores.controls = [ft.VerticalDivider(width=80, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=30, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=30, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=40, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=140, opacity=0),
                                B_T
                                ]
            
            page.update()

        elif e.control.value == "4":
            
            Menu.controls = [
                             S1,
                             ft.VerticalDivider(width=40, opacity=0), 
                             S2, 
                             ft.VerticalDivider(width=10, opacity=0),
                             S3, 
                             ft.VerticalDivider(width=20, opacity=0),
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=30, opacity=0), 
                             STolerancia, 
                             ft.VerticalDivider(width=35, opacity=0),
                             STCR]
            
            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            B_3.bgcolor=C_Blanco[0]
            BM_4.bgcolor=C_Blanco[0]
            B_TCR.bgcolor=C_Blanco[0]
            B_T.bgcolor=C_Blanco[0]

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = " "
            Salida_de_TCR.value = " "

            Mostrar_Existencia.value = ""

            B_T.height = 120
            B_1.height = 170
            B_T.border = ft.border.all(2, "#000000")
            B_TCR.border = ft.border.all(2, "#000000")

            Colores.controls = [ft.VerticalDivider(width=70, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=45, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=30, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=40, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=70, opacity=0),
                                B_T,
                                ft.VerticalDivider(width=40, opacity=0),
                                B_TCR
                                ]

            page.update()

    
    Salida_de_C1 = ft.Text(size=30, width=5)
    Salida_de_C2 = ft.Text(size=30, width=5)
    Salida_de_C3 = ft.Text(size=30, width=5)
    Salida_de_M = ft.Text(size=30)
    Salida_de_Tol = ft.Text(size=30)
    Salida_de_TCR = ft.Text(size=30)

    def Cambiar_Color_1(e):
        
        B_1.bgcolor = e.control.content.key[0]

        Salida_de_C1.value = e.control.content.key[1]

        page.update()
    
    def Cambiar_Color_2(e):
        
        B_2.bgcolor = e.control.content.key[0]

        Salida_de_C2.value = e.control.content.key[2]

        page.update()

    def Cambiar_Multiplicador_3(e):
        BM_3.bgcolor = e.control.content.key[0]

        Salida_de_M.value = e.control.content.key[4]

        page.update()

    def Cambiar_Multiplicador_4(e):
        BM_4.bgcolor = e.control.content.key[0]

        Salida_de_M.value = e.control.content.key[4]
    
        page.update()

    def Cambiar_Color_3(e):
        B_3.bgcolor = e.control.content.key[0]

        Salida_de_C3.value = e.control.content.key[3]

        page.update()
    
    def Cambiar_Color_T(e):
        B_T.bgcolor = e.control.content.key[0]

        Salida_de_Tol.value = e.control.content.key[5]

        page.update()
    
    def Cambiar_Color_TCR(e):
        B_TCR.bgcolor = e.control.content.key[0]

        Salida_de_TCR.value = e.control.content.key[6]

        page.update()

    def Check_Existencia(e):
        
        if Selector.controls[0].value == "1":
            
            if Salida_de_C1.value > "6" or Salida_de_C1.value == "5":

                Mostrar_Existencia.value = "Valor no comercial"
                Mostrar_Existencia.color = "red"

                page.update()

            elif (Salida_de_C2.value != "0"
                and Salida_de_C2.value != "5"
                and Salida_de_C2.value != "2"
                and Salida_de_C2.value != "3"
                and Salida_de_C2.value != "7"
                and Salida_de_C2.value != "8"):

                Mostrar_Existencia.value = "Valor no comercial"
                Mostrar_Existencia.color = "red"

                page.update()

            else:
                Mostrar_Existencia.value = "Valor comercial"
                Mostrar_Existencia.color = "green"

                page.update()
        

        

    Resultado = ft.Text(value="Resultado: ", size=30) # Título de los resultados

    # Selectores del color para cada banda
    # Nota: Hay que buscar una forma de colocar colores en cada lista. Por ahora tienen emojis.

    Menu = ft.MenuBar(controls=[ft.Text(value="Seleccione el modo de entrada.", 
                                        text_align=TextAlign.CENTER, 
                                        size=22, 
                                        color="red", 
                                        weight=FontWeight.BOLD, 
                                        italic=True)], 
                                        
                                        style=ft.MenuStyle(alignment=ft.alignment.center))

    S1 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Color_1),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Color_1),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Color_1)],

                                                      content=ft.Text("Color 1"))
    
    S2 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Color_2),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Color_2),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Color_2)],

                                                      content=ft.Text("Color 2"))
    
    S3 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Color_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Color_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Color_3)],

                                                      content=ft.Text("Color 3"))
    
    SMultiplicador_3 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Multiplicador_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Multiplicador_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Multiplicador_3)],

                                                      content=ft.Text("Multiplicador"))
    
    SMultiplicador_4 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Multiplicador_4),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Multiplicador_4),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Dorado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Dorado[0]),
                                                      on_click=Cambiar_Multiplicador_4),
                                    
                                    ft.MenuItemButton(content=ft.Text(key=C_Plateado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Plateado[0]),
                                                      on_click=Cambiar_Multiplicador_4)],

                                                      content=ft.Text("Multiplicador"))
    
    STolerancia = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Color_T),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Color_T),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Dorado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Dorado[0]),
                                                      on_click=Cambiar_Color_T),
                                    
                                    ft.MenuItemButton(content=ft.Text(key=C_Plateado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Plateado[0]),
                                                      on_click=Cambiar_Color_T)],

                                                      content=ft.Text("Tolerancia"))
    
    STCR = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja[0]),
                                                      on_click=Cambiar_Color_TCR),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo[0]),
                                                      on_click=Cambiar_Color_TCR),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris[0]),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco[0]),
                                                      on_click=Cambiar_Color_TCR)],

                                                      content=ft.Text("TCR"))
     
    # Dibujo del resistor

    Perol_Izq = ft.canvas.Rect(0, -15, 120, 170, border_radius=20, paint=ft.Paint(color="#925219"))
    Perol_Cen = ft.canvas.Rect(0, 10, 514, 120, border_radius=20, paint=ft.Paint(color="#925219"))
    Perol_Der = ft.canvas.Rect(410, -15, 120, 170, border_radius=20, paint=ft.Paint(color="#925219"))
    Contactos = ft.canvas.Rect(-50, 60, 630, 28, border_radius=0, paint=ft.Paint(color="#565656"))

    Img_R = ft.canvas.Canvas([Contactos, 
                          Perol_Izq, 
                          Perol_Cen, 
                          Perol_Der], expand=False, scale=1.25)

    Imagen = ft.Row(controls=[ft.Stack(controls=[      # Fila que contiene un "Stack", un elemento que sirve para poner cosas
                                                       # encima de otras
        Img_R,
        Colores,
        
    ],)], height=174, width=677)
            
    # Etiquetas de cada selector de punto. Tambien se pueden colocar en la propia función "ft.Radio". Pero preferí ponerla así.

    TBandas = "3 Bandas"
    CuBandas = "4 Bandas"
    CiBandas = "5 Bandas"
    SBandas = "6 Bandas"

    # Fila con los selectores de punto

    Selector = ft.Row(controls=[ft.RadioGroup(content=ft.Row(controls=[

        ft.Radio(value="1"),
        ft.Text(value=f"{TBandas}"),

        ft.Radio(value="2"),
        ft.Text(value=f"{CuBandas}"),

        ft.Radio(value="3"),
        ft.Text(value=f"{CiBandas}"),

        ft.Radio(value="4"),
        ft.Text(value=f"{SBandas}")])
    
    
    , on_change=Bandas_Resistor)], alignment=MainAxisAlignment.CENTER)

    # Parte pa que el usuario introduzca un valor

    def input_Valor_Manual(e):

        if e.control.value == True:

            Menu.controls = [
                             S1,
                             ft.VerticalDivider(width=40, opacity=0), 
                             S2, 
                             ft.VerticalDivider(width=10, opacity=0),
                             S3, 
                             ft.VerticalDivider(width=20, opacity=0),
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=30, opacity=0), 
                             STolerancia, 
                             ft.VerticalDivider(width=35, opacity=0),
                             STCR]
            
            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            B_3.bgcolor=C_Blanco[0]
            BM_4.bgcolor=C_Blanco[0]
            B_TCR.bgcolor=C_Blanco[0]
            B_T.bgcolor=C_Blanco[0]

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = " "
            Salida_de_TCR.value = " "

            B_T.height = 120
            B_1.height = 170
            B_T.border = ft.border.all(2, "#000000")
            B_TCR.border = ft.border.all(2, "#000000")

            Colores.controls = [ft.VerticalDivider(width=70, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=45, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=30, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=40, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=70, opacity=0),
                                B_T,
                                ft.VerticalDivider(width=40, opacity=0),
                                B_TCR
                                ]
            

            
            Fila_Entrada.visible = True
            
            Fila_Boton_Int.visible = True
            
            page.update()

        else:

            Menu.controls = [ft.Text(value="Seleccione el modo de entrada.", 
                                     text_align=TextAlign.CENTER, 
                                     size=22, 
                                     color="red", 
                                     weight=FontWeight.BOLD, 
                                     italic=True)]
            Colores.controls = []

            B_1.bgcolor=C_Blanco[0]
            B_2.bgcolor=C_Blanco[0]
            B_3.bgcolor=C_Blanco[0]
            BM_4.bgcolor=C_Blanco[0]
            B_TCR.bgcolor=C_Blanco[0]
            B_T.bgcolor=C_Blanco[0]

            B_1.height = 170

            Salida_de_C1.value = " "
            Salida_de_C2.value = " "
            Salida_de_C3.value = " "
            Salida_de_M.value = " "
            Salida_de_Tol.value = " "
            Salida_de_TCR.value = " "

            Entrada_valor.value = ""
            Entrada_Multiplicador.value = None
            Entrada_Tolerancia.value = None
            Entrada_TCR.value = None
            
            Fila_Entrada.visible = False
            
            Fila_Boton_Int.visible = False

            page.update()

    Lista_Colores = [C_Negro, C_Marron, C_Rojo, C_Naranja, C_Amarillo, C_Verde, C_Azul, C_Violeta, C_Gris, C_Blanco, C_Dorado, C_Plateado]

    def Calcular_Valor_Manual(e):
        
        
        if Entrada_valor.value != "" and Entrada_Multiplicador.value != None and Entrada_Tolerancia.value != None and Entrada_TCR.value != None:

            
            Entrada_valor.error_text = ""
            Entrada_Multiplicador.error_text = ""
            Entrada_Tolerancia.error_text = ""
            Entrada_TCR.error_text = ""
            
            B_1.bgcolor = Lista_Colores[int(Entrada_valor.value[0])][0]
            B_2.bgcolor = Lista_Colores[int(Entrada_valor.value[1])][0]
            B_3.bgcolor = Lista_Colores[int(Entrada_valor.value[2])][0]
            BM_4.bgcolor = Lista_Colores[int(Entrada_Multiplicador.value)][0]

            

            if Entrada_Tolerancia.value == "0":

                B_T.bgcolor = None
                B_T.border = None

            else:

                B_T.bgcolor = Lista_Colores[int(Entrada_Tolerancia.value)][0]
                B_T.border = ft.border.all(2, "#000000")

            if Entrada_TCR.value == "9":

                B_TCR.bgcolor = None
                B_TCR.border = None

            else:

                B_TCR.bgcolor = Lista_Colores[int(Entrada_TCR.value)][0]
                B_TCR.border = ft.border.all(2, "#000000")

            Salida_de_C1.value = f"{Entrada_valor.value[0]}"
            Salida_de_C2.value = f"{Entrada_valor.value[1]}"
            Salida_de_C3.value = f"{Entrada_valor.value[2]}"
            Salida_de_M.value = f"{Lista_Colores[int(Entrada_Multiplicador.value)][4]}"
            Salida_de_Tol.value = f"{Lista_Colores[int(Entrada_Tolerancia.value)][5]}"
            Salida_de_TCR.value = f"{Lista_Colores[int(Entrada_TCR.value)][6]}"

            page.update()

        

        else:

            Entrada_valor.error_text = "Introduzca un valor válido"
            Entrada_Multiplicador.error_text = "Introduzca un valor válido"
            Entrada_Tolerancia.error_text = "Introduzca un valor válido"
            Entrada_TCR.error_text = "Introduzca un valor válido"

            page.update()


    Switch_Introducir = ft.Switch(label="Introducir un valor", on_change=input_Valor_Manual)
    Info_Función = ft.Tooltip(message="Introducir un valor manualmente para ver el código de colores",
                              content=ft.TextButton(content=ft.Text(value="?", size=20)))
    
    Info_Lect_Resistor = ft.Tooltip(message="""‣ Observe el resistor. Ubique la banda más alejada.
‣ Coloque la banda más alejada a su derecha.
‣ Lea las bandas de izquierda a derecha. """,
                              content=ft.TextButton(content=ft.Text(value="¿Cómo leer un resistor?", size=15)))
    
    Bt_Ver_Exist = ft.Tooltip(content=ft.TextButton(content=ft.Text(value="Verificar existencia", size=13), on_click=Check_Existencia), 
                                     message="Intriduzca un valor")
    
    Mostrar_Existencia = ft.Text(size=18, italic=True, weight=ft.FontWeight.W_500)
    
    Entrada_valor = ft.TextField(label="Valor", hint_text="Formato: 000", 
                                 max_length=3, 
                                 multiline=False, 
                                 keyboard_type=ft.KeyboardType.NUMBER,
                                 input_filter=ft.NumbersOnlyInputFilter(), 
                                 text_align=ft.TextAlign.CENTER,
                                 width=200,
                                 )
    
    Entrada_Multiplicador = ft.Dropdown(label="Multiplicador",
                                        options=[

                                            ft.dropdown.Option(text="Ω", key=0),
                                            ft.dropdown.Option(text="0 Ω ", key=1),
                                            ft.dropdown.Option(text="00 Ω ", key=2),
                                            ft.dropdown.Option(text="kΩ", key=3),
                                            ft.dropdown.Option(text="0 kΩ", key=4),
                                            ft.dropdown.Option(text="00 kΩ", key=5),
                                            ft.dropdown.Option(text="MΩ", key=6),
                                            ft.dropdown.Option(text="0 M ", key=7),
                                            ft.dropdown.Option(text="00 MΩ", key=8),
                                            ft.dropdown.Option(text="GΩ", key=9),
                                            ft.dropdown.Option(text="x0,1Ω", key=10),
                                            ft.dropdown.Option(text="x0,01Ω", key=11),

                                        ], width=200, counter_text=" ")
    
    Entrada_Tolerancia = ft.Dropdown(label="Tolerancia",
                                        options=[
                                            
                                            ft.dropdown.Option(text="± 0%", key=0),
                                            ft.dropdown.Option(text="± 1%", key=1),
                                            ft.dropdown.Option(text="± 2%", key=2),
                                            ft.dropdown.Option(text="± 0,05%", key=3),
                                            ft.dropdown.Option(text="± 0,02%", key=4),
                                            ft.dropdown.Option(text="± 0,5%", key=5),
                                            ft.dropdown.Option(text="± 0,25%", key=6),
                                            ft.dropdown.Option(text="± 0,1%", key=7),
                                            ft.dropdown.Option(text="± 0,01%", key=8),
                                            ft.dropdown.Option(text="± 5%", key=10),
                                            ft.dropdown.Option(text="± 10%", key=11),
                                            

                                        ], width=200, counter_text=" ")
    
    Entrada_TCR = ft.Dropdown(label="TCR",
                                        options=[

                                            ft.dropdown.Option(text="0 ppm/k", key=9),
                                            ft.dropdown.Option(text="250 ppm/k", key=0),
                                            ft.dropdown.Option(text="100 ppm/k", key=1),
                                            ft.dropdown.Option(text="50 ppm/k", key=2),
                                            ft.dropdown.Option(text="15 ppm/k", key=3),
                                            ft.dropdown.Option(text="25 ppm/k", key=4),
                                            ft.dropdown.Option(text="20 ppm/k", key=5),
                                            ft.dropdown.Option(text="10 ppm/k", key=6),
                                            ft.dropdown.Option(text="5 ppm/k", key=7),
                                            ft.dropdown.Option(text="1 ppm/k", key=8),
                                            
                                            
                                            
                                            
                                        ], width=200, counter_text=" ")

    Fila_Entrada = ft.Row(controls=[Entrada_valor,
                                     Entrada_Multiplicador,
                                     Entrada_Tolerancia,
                                     Entrada_TCR], 
                                     
                                     alignment=MainAxisAlignment.CENTER, visible=False)
    
    Fila_Boton_Int = ft.Row(controls=[
        ft.Container(content=ft.FloatingActionButton(content=ft.Text(value="Mostrar código", 
                                                                    size=20), 
                                                                    bgcolor="transparent", 
                                                                    shape=RoundedRectangleBorder(radius=5),
                                                                    on_click=Calcular_Valor_Manual, width=400), 

                                                             border=ft.border.all(2, "#ffffff"), 
                                                             border_radius=5)], 
                                      
                                      alignment=MainAxisAlignment.CENTER, visible=False)
    
    
    # Acá se añaden los elementos a la interfaz.


    page.add(Titulo())
    page.add(ft.Divider(opacity=0, height=1), 
             Menu, 
             ft.Divider(opacity=0, height=10), 
             ft.Row(controls=[Imagen], scroll=ScrollMode.ALWAYS),
             ft.Divider(opacity=0, height=25),
             Selector,
             ft.Row(controls=[
                              
                              Resultado,                      
                              Salida_de_C1, 
                              Salida_de_C2, 
                              Salida_de_C3,
                              Salida_de_M,
                              Salida_de_Tol,
                              Salida_de_TCR,
                              ], 
                              
                              alignment=MainAxisAlignment.CENTER),
                              ft.Row([Bt_Ver_Exist,
                              Mostrar_Existencia], alignment=MainAxisAlignment.CENTER), 
                              

                              ft.Row([Switch_Introducir, Info_Función, Info_Lect_Resistor], 
                                     alignment=MainAxisAlignment.CENTER),
                                     
                              Fila_Entrada, 
                              Fila_Boton_Int)

ft.app(target=main) # Arranque de la aplicación