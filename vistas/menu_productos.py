from vistas.utilidades_vista import menu_interactivo, limpiar_pantalla
from controladores import controlador_producto

def menu_productos():
    opciones = ["Registrar Producto", "Listar Productos", "Editar Producto", "Eliminar Producto", "Volver al Menú Principal"]
    titulo = ["GESTIÓN DE PRODUCTOS"]
    while True:
        productos = controlador_producto.cargar_productos()
        opcion = menu_interactivo(opciones, titulo)

        if opcion == 0:
            controlador_producto.registrar_producto(productos)
        elif opcion == 1:
            controlador_producto.listar_productos(productos)
        elif opcion == 2:
            controlador_producto.editar_producto(productos)
        elif opcion == 3:
            controlador_producto.eliminar_producto(productos)
        elif opcion == 4:
            break

        input("\nPresiona Enter para continuar...")
