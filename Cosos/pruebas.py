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

            Menu.controls = [S1, S2, ft.VerticalDivider(width=50), SMultiplicador_3]
            
            Colores.controls = [ft.VerticalDivider(width=160, opacity=0),
                                B_1,
                                ft.VerticalDivider(width=55, opacity=0),
                                B_2,
                                ft.VerticalDivider(width=130, opacity=0),
                                BM_3
                                ]
            
            page.update()
            
        elif e.control.value == "2":

            SelColores.controls = [S1, S2, SMultiplicador_4, ft.VerticalDivider(width=50), STolerancia]
            
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

            SelColores.controls = [S1, S2, S3, SMultiplicador_4, ft.VerticalDivider(width=10), STolerancia]
            
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
            
            SelColores.controls = [S1, S2, S3, SMultiplicador_4, ft.VerticalDivider(width=5), STolerancia, STCR]
            
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

    def Cambiar_Colores(e):
        B_1.bgcolor = S1.control.content.key
        B_2.bgcolor = S2.value
        BM_3.bgcolor = SMultiplicador_3.value

        BM_4.bgcolor = SMultiplicador_4.value
        B_T.bgcolor = STolerancia.value

        B_3.bgcolor = S3.value
        B_TCR.bgcolor = STCR.value

        print("A")
        
        page.update()

    Salida_de_valor = ft.Text()
    
    no_c = ft.Row(controls=[ft.Text(value="resultado"), Salida_de_valor])
    
    # Selectores del color para cada banda
    # Nota: Hay que buscar una forma de colocar colores en cada lista. Por ahora tienen emojis.

    Menu = ft.MenuBar(controls=[ft.Text(value="Seleccione la cantidad de barras")], expand=True)

    S1 = ft.SubmenuButton(controls=[ft.MenuItemButton(content=ft.ElevatedButton(bgcolor=C_Negro, key=C_Negro, on_click=Cambiar_Colores))])
    
    S2 = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco)

            ], width=100, label="Color 2", bgcolor="#ffffff", on_change=Cambiar_Colores)
    
    S3 = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco)

            ], width=100, label="Color 3", bgcolor="#ffffff", on_change=Cambiar_Colores)
    
    SMultiplicador_3 = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco)
                

            ], width=150, label="Multiplicador", bgcolor="#ffffff", on_change=Cambiar_Colores)
    
    SMultiplicador_4 = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco),
                ft.dropdown.Option(text="Dorado", key=C_Dorado),
                ft.dropdown.Option(text="Plateado", key=C_Plateado)

            ], width=150, label="Multiplicador", bgcolor="#ffffff", on_change=Cambiar_Colores)
    
    STolerancia = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco),
                ft.dropdown.Option(text="Dorado", key=C_Dorado),
                ft.dropdown.Option(text="Plateado", key=C_Plateado)

            ], width=120, label="Tolerancia", bgcolor="#ffffff", on_change=Cambiar_Colores)
    
    STCR = ft.Dropdown(options=[

                ft.dropdown.Option(text="⬜", key=C_Negro),
                ft.dropdown.Option(text="🟫", key=C_Marron),
                ft.dropdown.Option(text="🟥", key=C_Rojo),
                ft.dropdown.Option(text="🟧", key=C_Naranja),
                ft.dropdown.Option(text="🟨", key=C_Amarillo),
                ft.dropdown.Option(text="🟩", key=C_Verde),
                ft.dropdown.Option(text="🟦", key=C_Azul),
                ft.dropdown.Option(text="🟪", key=C_Violeta),
                ft.dropdown.Option(text="🌫️", key=C_Gris),
                ft.dropdown.Option(text="⬛", key=C_Blanco)
                

            ], width=60, label="TCR", bgcolor="#ffffff", on_change=Cambiar_Colores)
     
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

    page.add(Titulo(), SelColores)
    page.add(ft.Divider(opacity=0, height=25), ft.Row([Menu], alignment=MainAxisAlignment.CENTER))
    page.add(Imagen)
    page.add(ft.Divider(opacity=0, height=25))
    page.add(Selector)
    
    #page.add(Colores)
    #page.add(no_c)

ft.app(target=main) # Arranque de la aplicación
