# menu_reportes.py
from vistas.utilidades_vista import menu_interactivo
from controladores import controlador_reporte
from controladores.controlador_venta import cargar_ventas
from controladores.controlador_cliente import cargar_clientes
from controladores.controlador_producto import cargar_productos

def menu_reportes():
    ventas = cargar_ventas()
    clientes = cargar_clientes()
    productos = cargar_productos()

    while True:
        opciones = [
            "Productos más vendidos",
            "Kits más vendidos",
            "Clientes con más ventas",
            "Total de ventas por día",
            "Ingresos totales",
            "Categorías más vendidas",
            "Volver al menú principal"
        ]

        titulo = [
            "GESTIÓN DE REPORTES",
        ]

        seleccion = menu_interactivo(opciones, titulo)

        if seleccion == 0:
            controlador_reporte.productos_mas_vendidos(ventas)
        elif seleccion == 1:
            controlador_reporte.kits_mas_vendidos(ventas)
        elif seleccion == 2:
            controlador_reporte.clientes_con_mas_ventas(clientes)
        elif seleccion == 3:
            controlador_reporte.total_ventas_diarias(ventas)
        elif seleccion == 4:
            controlador_reporte.total_ingresos(ventas)
        elif seleccion == 5:
            controlador_reporte.categorias_mas_vendidas(ventas, productos)
        elif seleccion == 6:
            break
