from vistas.utilidades_vista import menu_interactivo

opciones = ["Menú Productos", "Menú Kits", "Menú Cotización", "Menú Ventas", "Salir"]

def mostrar_menu_principal():
    titulo = [
        "ELECTROPERU SAC",
        "RUC: 20481234567",
        "Av. Industrial 123, Lima, Perú",
        "Teléfono: (01) 234-5678",
        "SISTEMA DE VENTAS DE MATERIALES ELÉCTRICOS"
    ]
    return menu_interactivo(opciones, titulo)
