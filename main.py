import sys
from vistas.menu_principal import mostrar_menu_principal
from vistas.menu_productos import menu_productos
from vistas.menu_kits import menu_kits
from vistas.menu_cotizacion import menu_cotizacion
from vistas.menu_ventas import menu_ventas

def main():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == 0:
            menu_productos()
        elif opcion == 1:
            menu_kits()
        elif opcion == 2:
            menu_cotizacion()
        elif opcion == 3:
            menu_ventas()
        elif opcion == 4:
            sys.exit(0)

if __name__ == "__main__":
    main()
