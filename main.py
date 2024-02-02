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

    # Bandas

    B_1 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_2 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_3 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_4 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_5 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )
    B_6 = ft.Container(bgcolor="#ffffff", width=15, height=170, border=ft.border.all(2, "#000000"), )

    # Función para cambiar la cantidad de bandas
    def Resistor(e):

        # Los valores que aparecen en cada condicional, es decir "e.control.value" son introducidos
        # por los selectores en forma de punto. Los que se guardan en la variable "Selector".
        # "e" es la letra que representa el "evento" en la aplicación, específicamente en esta función
        # se trabaja con los eventos que envian los selectores de punto.

        # Cada punto agrega la cantidad de bandas sobre el dibujo del resistor. 
        # Es lo que hace cada condicional a continuación:

        if e.control.value == "1": 

            SelColores.controls = [S1, S2, ft.VerticalDivider(width=50), SMultiplicador_3]
            
            Colores.controls = [ft.VerticalDivider(width=160, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=55, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=130, opacity=0),
                                B_3
                                ]
            
            page.update()
            
        elif e.control.value == "2":

            SelColores.controls = [S1, S2, SMultiplicador_4, ft.VerticalDivider(width=50), STolerancia]
            
            Colores.controls = [ft.VerticalDivider(width=120, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=70, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=120, opacity=0),
                                B_4
                                ]
                        
            page.update()

        elif e.control.value == "3":

            SelColores.controls = [S1, S2, S3, SMultiplicador_4, ft.VerticalDivider(width=10), STolerancia]
            
            Colores.controls = [ft.VerticalDivider(width=80, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_4,
                                ft.VerticalDivider(width=120, opacity=0),
                                B_5
                                ]
            
            page.update()

        elif e.control.value == "4":
            
            SelColores.controls = [S1, S2, S3, SMultiplicador_4, ft.VerticalDivider(width=5), STolerancia, STCR]
            
            Colores.controls = [ft.VerticalDivider(width=70, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_3,
                                ft.VerticalDivider(width=60, opacity=0),
                                B_4,
                                ft.VerticalDivider(width=100, opacity=0),
                                B_5,
                                ft.VerticalDivider(width=40, opacity=0),
                                B_6
                                ]

            page.update()
    
    # Selectores del color para cada banda
    # Nota: Hay que buscar una forma de colocar colores en cada lista. Por ahora tienen emojis.

    S1 = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛")

            ], width=100, label="Color 1", bgcolor="#ffffff")
    
    S2 = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛")

            ], width=100, label="Color 2", bgcolor="#ffffff")
    
    S3 = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛")

            ], width=100, label="Color 3", bgcolor="#ffffff")
    
    SMultiplicador_3 = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛"),
                

            ], width=150, label="Multiplicador", bgcolor="#ffffff")
    
    SMultiplicador_4 = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛"),
                ft.dropdown.Option("Dorado"),
                ft.dropdown.Option("Plateado")

            ], width=150, label="Multiplicador", bgcolor="#ffffff")
    
    STolerancia = ft.Dropdown(options=[

                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                ft.dropdown.Option("⬛"),
                ft.dropdown.Option("Dorado"),
                ft.dropdown.Option("Plateado")

            ], width=120, label="Tolerancia", bgcolor="#ffffff")
    
    STCR = ft.Dropdown(options=[

                ft.dropdown.Option("⬜"),
                ft.dropdown.Option("🟫"),
                ft.dropdown.Option("🟥"),
                ft.dropdown.Option("🟧"),
                ft.dropdown.Option("🟨"),
                ft.dropdown.Option("🟩"),
                ft.dropdown.Option("🟦"),
                ft.dropdown.Option("🟪"),
                ft.dropdown.Option("🌫️"),
                

            ], width=60, label="TCR", bgcolor="#ffffff")
     
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
    
    
    , on_change=Resistor)], alignment=MainAxisAlignment.CENTER)
    
    
    # Acá se añaden los elementos a la interfaz. 

    page.add(Titulo(), SelColores)
    page.add(ft.Divider(opacity=0, height=25))
    page.add(Imagen)
    page.add(ft.Divider(opacity=0, height=25))
    page.add(Selector)
    
    page.add(Colores)

ft.app(target=main) # Arranque de la aplicación
