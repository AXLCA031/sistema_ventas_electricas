from vistas.utilidades_vista import menu_interactivo
from vistas.menu_productos import menu_productos
from vistas.menu_kits import menu_kits
from vistas.menu_clientes import menu_clientes
from vistas.menu_ventas import menu_ventas
from vistas.menu_reportes import menu_reportes
import sys

def mostrar_menu_principal():
    opciones = [
        "Menú Productos",
        "Menú Kits",
        "Menú Clientes",
        "Menú Ventas",
        "Menú Reportes",
        "Salir"
    ]

    titulo = [
        "ELECTROPERU SAC",
        "RUC: 20481234567",
        "Av. Industrial 123, Lima, Perú",
        "Teléfono: (01) 234-5678",
        "SISTEMA DE VENTAS DE MATERIALES ELÉCTRICOS"
    ]

    return menu_interactivo(opciones, titulo)


def ejecutar_menu_principal():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == 0:
            menu_productos()
        elif opcion == 1:
            menu_kits()
        elif opcion == 2:
            menu_clientes()
        elif opcion == 3:
            menu_ventas()
        elif opcion == 4:
            menu_reportes()
        elif opcion == 5:
            sys.exit(0)
