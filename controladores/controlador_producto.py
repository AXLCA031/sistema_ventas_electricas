import json
from modelos.producto import Producto

RUTA_PRODUCTOS = "data/productos.json"

def cargar_productos():
    try:
        with open(RUTA_PRODUCTOS, "r") as f:
            data = json.load(f)
            return [Producto(**p) for p in data]
    except FileNotFoundError:
        return []

def guardar_productos(lista_productos):
    with open(RUTA_PRODUCTOS, "w") as f:
        json.dump([p.__dict__ for p in lista_productos], f, indent=4)

def listar_productos(productos):
    print("\nProductos en inventario:\n")
    for p in productos:
        print(p)

def agregar_producto(productos):
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    nuevo = Producto(codigo, nombre, categoria, precio, stock)
    productos.append(nuevo)
    guardar_productos(productos)
    print("Producto agregado correctamente.")

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