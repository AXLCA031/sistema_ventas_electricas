import os
import msvcrt
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_menu(seleccion, opciones, titulo):
    limpiar_pantalla()
    ancho_terminal = os.get_terminal_size().columns

    print("\n" * 2)
    for linea in titulo:
        print(linea.center(ancho_terminal))
    print(("=" * len(titulo[-1])).center(ancho_terminal))

    print("\n")
    for i, opcion in enumerate(opciones):
        prefijo = "→" if i == seleccion else "  "
        color = Fore.GREEN if i == seleccion else Fore.WHITE
        print(color + f"{prefijo} {opcion}".center(ancho_terminal) + Style.RESET_ALL)


def menu_interactivo(opciones, titulo):
    seleccion = 0
    imprimir_menu(seleccion, opciones, titulo)

    while True:
        tecla = msvcrt.getch()
        if tecla == b'\xe0':
            subtecla = msvcrt.getch()
            if subtecla == b'H':
                seleccion = (seleccion - 1) % len(opciones)
                imprimir_menu(seleccion, opciones, titulo)
            elif subtecla == b'P':
                seleccion = (seleccion + 1) % len(opciones)
                imprimir_menu(seleccion, opciones, titulo)
        elif tecla == b'\r':
            return seleccion
