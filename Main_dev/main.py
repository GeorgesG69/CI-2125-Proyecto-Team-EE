import flet as ft
from flet import *
from colorama import Back, Fore, init
init()

def main(page: ft.Page):
    page.title = "Calculadora de Resistores" # Título del borde de la ventana
    #page.bgcolor = "#1a0f2a" # Color del fondo
    def Titulo():

        Title = ft.Text(value="Calculadora de Resistores", size=30) # Título del centro de la apliacción

        return ft.Row(controls=[Column(controls=[

            Title,
        ])], alignment=MainAxisAlignment.CENTER)
    
    SelColores = ft.Row(alignment=MainAxisAlignment.CENTER) # Fila de selectores de colores
    Colores = ft.Row(expand=False, scale=1.25) # Bandas del resistor, cambian de color

    # Colores con sus códigos

    C_Negro = "#000000"     # Negro
    C_Marron = "#883c00"    # Marrón
    C_Rojo = "#ff0000"      # Rojo
    C_Naranja = "#ff872e"   # Naranja
    C_Amarillo = "#f3e800"  # Amarillo
    C_Verde = "#28a700"     # Verde
    C_Azul = "#009bb6"      # Azul
    C_Violeta = "#8200e1"   # Violeta
    C_Gris = "#737373"      # Gris
    C_Blanco = "#ffffff"    # Blanco
    C_Dorado = "#958000"    # Dorado
    C_Plateado = "#b4b4b4"  # Plateado

    # Bandas

    B_1 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_2 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_3 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_4 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    BM_3 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    BM_4 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_T = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
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

            Menu.controls = [ft.VerticalDivider(width=415, opacity=0), 
                             S1, 
                             ft.VerticalDivider(width=50, opacity=0), 
                             S2, 
                             ft.VerticalDivider(width=120, opacity=0), 
                             SMultiplicador_3]
            
            Colores.controls = [ft.VerticalDivider(width=160, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=55, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=130, opacity=0),
                                BM_3
                                ]
            
            page.update()
            
        elif e.control.value == "2":

            Menu.controls = [ft.VerticalDivider(width=360, opacity=0),
                             S1,
                             ft.VerticalDivider(width=50, opacity=0), 
                             S2,
                             ft.VerticalDivider(width=50, opacity=0), 
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=100, opacity=0), 
                             STolerancia]
            
            Colores.controls = [ft.VerticalDivider(width=120, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=70, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=120, opacity=0),
                                B_T
                                ]
                        
            page.update()

        elif e.control.value == "3":

            Menu.controls = [ft.VerticalDivider(width=300, opacity=0),
                             S1,
                             ft.VerticalDivider(width=60, opacity=0), 
                             S2,
                             ft.VerticalDivider(width=60, opacity=0), 
                             S3,
                             ft.VerticalDivider(width=20, opacity=0),
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=110, opacity=0), 
                             STolerancia]
            
            Colores.controls = [ft.VerticalDivider(width=80, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=60, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=120, opacity=0),
                                B_T
                                ]
            
            page.update()

        elif e.control.value == "4":
            
            Menu.controls = [ft.VerticalDivider(width=280, opacity=0),
                             S1,
                             ft.VerticalDivider(width=55, opacity=0), 
                             S2, 
                             ft.VerticalDivider(width=55, opacity=0),
                             S3, 
                             ft.VerticalDivider(width=50, opacity=0),
                             SMultiplicador_4, 
                             ft.VerticalDivider(width=65, opacity=0), 
                             STolerancia, 
                             ft.VerticalDivider(width=35, opacity=0),
                             STCR]
            
            Colores.controls = [ft.VerticalDivider(width=70, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=60, opacity=0),
                                BM_4,
                                ft.VerticalDivider(width=100, opacity=0),
                                B_T,
                                ft.VerticalDivider(width=40, opacity=0),
                                B_TCR
                                ]

            page.update()

    def Cambiar_Color_1(e):
        B_1.bgcolor = e.control.content.key

        page.update()
    
    def Cambiar_Color_2(e):
        B_2.bgcolor = e.control.content.key

        page.update()

    def Cambiar_Multiplicador_3(e):
        BM_3.bgcolor = e.control.content.key

        page.update()

    def Cambiar_Multiplicador_4(e):
        BM_4.bgcolor = e.control.content.key
        
        page.update()

    def Cambiar_Color_3(e):
        B_3.bgcolor = e.control.content.key

        page.update()
    
    def Cambiar_Color_T(e):
        B_T.bgcolor = e.control.content.key

        page.update()
    
    def Cambiar_Color_TCR(e):
        B_TCR.bgcolor = e.control.content.key

        page.update()
    
    Salida_de_valor = ft.Text()
    
    def Resultado():

        Resul = ft.Text(value="Resultados", size=30) # Título de los resultados

        return ft.Row(controls=[Column(controls=[

            Resul,
        ])], alignment=MainAxisAlignment.CENTER)
    
    # Selectores del color para cada banda
    # Nota: Hay que buscar una forma de colocar colores en cada lista. Por ahora tienen emojis.

    Menu = ft.MenuBar(controls=[ft.Text(value="Seleccione la cantidad de barras", width=page.width, text_align=TextAlign.CENTER, size=20, italic=True)], expand=True, style=ft.MenuStyle(alignment=ft.alignment.center_right))

    S1 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Color_1),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Color_1),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Color_1),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Color_1)],

                                                      content=ft.Text("Color 1"))
    
    S2 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Color_2),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Color_2),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Color_2),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Color_2)],

                                                      content=ft.Text("Color 2"))
    
    S3 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Color_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Color_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Color_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Color_3)],

                                                      content=ft.Text("Color 3"))
    
    SMultiplicador_3 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Multiplicador_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Multiplicador_3),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Multiplicador_3),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Multiplicador_3)],

                                                      content=ft.Text("Multiplicador"))
    
    SMultiplicador_4 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Multiplicador_4),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Multiplicador_4),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Multiplicador_4),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Dorado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Dorado),
                                                      on_click=Cambiar_Multiplicador_4),
                                    
                                    ft.MenuItemButton(content=ft.Text(key=C_Plateado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Plateado),
                                                      on_click=Cambiar_Multiplicador_4)],

                                                      content=ft.Text("Multiplicador"))
    
    STolerancia = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Color_T),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Color_T),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Color_T),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Dorado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Dorado),
                                                      on_click=Cambiar_Color_T),
                                    
                                    ft.MenuItemButton(content=ft.Text(key=C_Plateado), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Plateado),
                                                      on_click=Cambiar_Color_T)],

                                                      content=ft.Text("Tolerancia"))
    
    STCR = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.Text(key=C_Negro), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Negro),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Marron), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Marron),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Rojo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Rojo),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Naranja), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Naranja),
                                                      on_click=Cambiar_Color_TCR),

                                    ft.MenuItemButton(content=ft.Text(key=C_Amarillo), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Amarillo),
                                                      on_click=Cambiar_Color_TCR),

                                    ft.MenuItemButton(content=ft.Text(key=C_Verde), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Verde),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Azul), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Azul),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Violeta), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Violeta),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Gris), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Gris),
                                                      on_click=Cambiar_Color_TCR),
                                                      
                                    ft.MenuItemButton(content=ft.Text(key=C_Blanco), 
                                                      
                                                      style=ft.ButtonStyle(bgcolor=C_Blanco),
                                                      on_click=Cambiar_Color_TCR)],

                                                      content=ft.Text("TCR"))
     
    IMG_R = ft.Image(src="Resistor 2.png", scale=1.25) # Dibujo del resistor

    Imagen = ft.Row(controls=[ft.Stack(controls=[      # Fila que contiene un "Stack", un elemento que sirve para poner cosas
                                                       # encima de otras
        IMG_R,
        Colores,
        
    ],)], alignment=MainAxisAlignment.CENTER)
            
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
    
    
    # Acá se añaden los elementos a la interfaz. 

    page.add(Titulo())
    page.add(ft.Divider(opacity=0, height=5), 
             ft.Row([Menu], alignment=MainAxisAlignment.CENTER), 
             ft.Divider(opacity=0, height=25))
    page.add(Imagen)
    page.add(ft.Divider(opacity=0, height=25))
    page.add(Selector)
    page.add(Resultado())
    


ft.app(target=main) # Arranque de la aplicación
