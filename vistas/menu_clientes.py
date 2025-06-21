from controladores import controlador_cliente
from vistas.utilidades_vista import menu_interactivo, limpiar_pantalla

def menu_clientes():
    clientes = controlador_cliente.cargar_clientes()
    opciones = [
        "Registrar nuevo cliente",
        "Listar clientes",
        "Buscar cliente por código",
        "Editar cliente",
        "Eliminar cliente",
        "Volver al menú principal"
    ]
    titulo = [
        "GESTIÓN DE CLIENTES",
    ]

    while True:
        seleccion = menu_interactivo(opciones, titulo)

        if seleccion == 0:
            controlador_cliente.registrar_cliente(clientes)
        elif seleccion == 1:
            controlador_cliente.listar_clientes(clientes)
        elif seleccion == 2:
            controlador_cliente.buscar_cliente(clientes)
        elif seleccion == 3:
            controlador_cliente.editar_cliente(clientes)
        elif seleccion == 4:
            controlador_cliente.eliminar_cliente(clientes)
        elif seleccion == 5:
            break