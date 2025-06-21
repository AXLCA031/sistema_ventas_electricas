from controladores import controlador_kit
from vistas.utilidades_vista import menu_interactivo, limpiar_pantalla

def menu_kits():
    kits = controlador_kit.cargar_kits()

    opciones = [
        "Registrar Kit",
        "Eliminar Kit",
        "Buscar Kit",
        "Listar Kits",
        "Volver al Menú Principal"
    ]

    titulo = ["GESTIÓN DE KITS"]

    while True:
        seleccion = menu_interactivo(opciones, titulo)

        if seleccion == 0:
            limpiar_pantalla()
            controlador_kit.registrar_kit(kits)
        elif seleccion == 1:
            limpiar_pantalla()
            controlador_kit.eliminar_kit(kits)
        elif seleccion == 2:
            limpiar_pantalla()
            controlador_kit.buscar_kit_por_codigo(kits)
        elif seleccion == 3:
            limpiar_pantalla()
            controlador_kit.listar_kits(kits)
        elif seleccion == 4:
            break
