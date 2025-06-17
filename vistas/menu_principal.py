import os
import sys
import msvcrt
from colorama import Fore, Style, init
from vistas.utilidades_vista import limpiar_pantalla

init(autoreset=True)

opciones = ["Menú Productos", "Menú Kits", "Menú Cotización", "Salir"]

def imprimir_menu(seleccion):
    limpiar_pantalla()
    ancho_terminal = os.get_terminal_size().columns

    print("\n" * 3)
    titulo = "SISTEMA DE VENTAS DE MATERIALES ELÉCTRICOS"
    print(titulo.center(ancho_terminal))
    print(("=" * len(titulo)).center(ancho_terminal))


    print("\n")
    for i, opcion in enumerate(opciones):
        prefijo = "→" if i == seleccion else "  "
        color = Fore.GREEN if i == seleccion else Fore.WHITE
        linea = f"{prefijo} {opcion}"
        print(color + linea.center(ancho_terminal) + Style.RESET_ALL)

def menu_interactivo():
    seleccion = 0
    imprimir_menu(seleccion)

    while True:
        tecla = msvcrt.getch()
        if tecla == b'\xe0':
            subtecla = msvcrt.getch()
            if subtecla == b'H':
                seleccion = (seleccion - 1) % len(opciones)
                imprimir_menu(seleccion)
            elif subtecla == b'P':
                seleccion = (seleccion + 1) % len(opciones)
                imprimir_menu(seleccion)
        elif tecla == b'\r':
            return seleccion

def mostrar_menu_principal():
    return menu_interactivo()
