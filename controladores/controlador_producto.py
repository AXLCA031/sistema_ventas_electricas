import json
from modelos.producto import Producto

RUTA_PRODUCTOS = "data/productos.json"

CATEGORIAS = [
    "Instrumentos de Medicion",
    "Materiales Electricos",
    "Cables",
    "Protección Electrica",
    "Tableros",
    "Accesorios Electricos",
    "Iluminacion",
    "Instalacion",
    "Seguridad Electrica",
    "Otros"
]

def cargar_productos():
    try:
        with open(RUTA_PRODUCTOS, "r") as f:
            data = json.load(f)
            return [Producto.from_dict(p) for p in data]
    except FileNotFoundError:
        return []

def guardar_productos(lista_productos):
    with open(RUTA_PRODUCTOS, "w") as f:
        json.dump([p.to_dict() for p in lista_productos], f, indent=4)

def listar_productos(productos):
    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\n PRODUCTOS EN INVENTARIO:\n")

    suficientes = [p for p in productos if p.stock >= 5]
    bajos = [p for p in productos if p.stock < 5]

    if suficientes:
        print(" Productos con stock suficiente:\n")
        for p in suficientes:
            print(p)
    else:
        print(" No hay productos con stock suficiente.\n")

    print("\n" + "=" * 50 + "\n")

    if bajos:
        print(" Productos con stock bajo (menos de 5 unidades):\n")
        for p in bajos:
            print(f"{p}  <-   Bajo stock")
        print("\n  Se recomienda reabastecer estos productos.")
    else:
        print(" No hay productos con stock bajo.")


def generar_codigo(productos):
    if not productos:
        return "P001"

    codigos = [p.codigo for p in productos if p.codigo.startswith("P") and p.codigo[1:].isdigit()]
    numeros = [int(codigo[1:]) for codigo in codigos]
    siguiente_numero = max(numeros, default=0) + 1
    return f"P{siguiente_numero:03d}"

def seleccionar_categoria():
    print("\nSeleccione la categoría:")
    for idx, cat in enumerate(CATEGORIAS, 1):
        print(f"{idx}. {cat}")

    while True:
        try:
            opcion = int(input("Ingrese el número de la categoría: "))
            if 1 <= opcion <= len(CATEGORIAS):
                return CATEGORIAS[opcion - 1]
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Ingrese un número válido.")

def registrar_producto(productos):
    print("\n=== REGISTRAR PRODUCTO ===\n")
    codigo_generado = generar_codigo(productos)
    print(f"Código generado automáticamente: {codigo_generado}")

    nombre = input("Nombre: ")
    categoria = seleccionar_categoria()

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
    except ValueError:
        print("Error: Precio o stock inválido.")
        return

    nuevo = Producto(codigo_generado, nombre, categoria, precio, stock)
    productos.append(nuevo)
    guardar_productos(productos)

    print(f"\nProducto agregado correctamente con código: {codigo_generado}")

def editar_producto(productos):
    if not productos:
        print("No hay productos para editar.")
        return

    codigo = input("Ingresa el código del producto a editar: ")
    for producto in productos:
        if producto.codigo == codigo:
            print(f"\nProducto encontrado:\n{producto}")
            print("Deja el campo vacío si no deseas cambiarlo.\n")

            nuevo_nombre = input(f"Nuevo nombre [{producto.nombre}]: ") or producto.nombre

            print(f"Categoría actual: {producto.categoria}")
            cambiar_categoria = input("¿Deseas cambiar la categoría? (s/n): ").lower()
            if cambiar_categoria == "s":
                nueva_categoria = seleccionar_categoria()
            else:
                nueva_categoria = producto.categoria

            nuevo_precio_input = input(f"Nuevo precio [{producto.precio}]: ")
            nuevo_precio = float(nuevo_precio_input) if nuevo_precio_input else producto.precio

            nuevo_stock_input = input(f"Nuevo stock [{producto.stock}]: ")
            nuevo_stock = int(nuevo_stock_input) if nuevo_stock_input else producto.stock

            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            producto.stock = nuevo_stock

            guardar_productos(productos)
            print("Producto actualizado correctamente.")
            return

    print("Producto no encontrado.")

def eliminar_producto(productos):
    if not productos:
        print("No hay productos para eliminar.")
        return

    codigo = input("Ingresa el código del producto a eliminar: ")
    encontrado = False

    for i, producto in enumerate(productos):
        if producto.codigo == codigo:
            print(f"¿Estás seguro de eliminar el producto?\n{producto}")
            confirmacion = input("Escribe 'SI' para confirmar: ").strip().upper()
            if confirmacion == "SI":
                productos.pop(i)
                guardar_productos(productos)
                print("Producto eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")

