from controladores import controlador_venta
from vistas.utilidades_vista import menu_interactivo, limpiar_pantalla

def menu_ventas():
    ventas = controlador_venta.cargar_ventas()

    opciones = [
        "Registrar Venta",
        "Eliminar Venta",
        "Buscar Venta",
        "Generar Boleta",
        "Listar Ventas",
        "Volver al Menú Principal"
    ]

    titulo = ["GESTIÓN DE VENTAS"]

    while True:
        seleccion = menu_interactivo(opciones, titulo)

        if seleccion == 0:
            limpiar_pantalla()
            controlador_venta.registrar_venta(ventas)
        elif seleccion == 1:
            limpiar_pantalla()
            controlador_venta.eliminar_venta(ventas)
        elif seleccion == 2:
            limpiar_pantalla()
            controlador_venta.buscar_venta_por_codigo(ventas)
        elif seleccion == 3:
            limpiar_pantalla()
            controlador_venta.generar_boleta(ventas)
        elif seleccion == 4:
            limpiar_pantalla()
            controlador_venta.listar_ventas(ventas)
        elif seleccion == 5:
            break
