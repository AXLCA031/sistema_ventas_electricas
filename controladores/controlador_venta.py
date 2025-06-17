import json
import uuid
from datetime import datetime
from modelos.venta import Venta
from modelos.producto import Producto
from controladores.controlador_producto import cargar_productos

RUTA_VENTAS = "data/ventas.json"

def cargar_ventas():
    try:
        with open(RUTA_VENTAS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_ventas(lista_ventas):
    with open(RUTA_VENTAS, "w") as f:
        json.dump(lista_ventas, f, indent=4)
        
def listar_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("\nVentas registradas:")
        print("=" * 40)
        for venta in ventas:
            print(f"Código: {venta['codigo']} | Cliente: {venta['cliente']}")
        print("=" * 40)
    input("Presione Enter para continuar...")


def registrar_venta(ventas):
    from controladores.controlador_producto import cargar_productos, guardar_productos

    productos_disponibles = cargar_productos()
    if not productos_disponibles:
        print("No hay productos disponibles para registrar una venta.")
        input("Presione Enter para continuar...")
        return

    codigo_venta = str(uuid.uuid4())[:8]
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cliente = input("Nombre del cliente: ")
    productos_venta = []
    total = 0.0

    while True:
        codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ").strip()
        if codigo_producto.lower() == "fin":
            break

        producto = next((p for p in productos_disponibles if p.codigo == codigo_producto), None)
        if not producto:
            print("Producto no encontrado. Intente nuevamente.")
            continue

        print(f"Producto: {producto.nombre} | Precio unitario: {producto.precio} | Stock disponible: {producto.stock}")
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            continue

        if cantidad > producto.stock:
            print("No hay suficiente stock para esta cantidad.")
            continue

        subtotal = producto.precio * cantidad
        total += subtotal
        productos_venta.append({
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio_unitario": producto.precio,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

        producto.stock -= cantidad

    if not productos_venta:
        print("No se registraron productos para esta venta.")
        input("Presione Enter para continuar...")
        return

    venta = {
        "codigo": codigo_venta,
        "fecha": fecha,
        "cliente": cliente,
        "productos": productos_venta,
        "total": total
    }

    ventas.append(venta)
    guardar_ventas(ventas)
    guardar_productos(productos_disponibles)

    print("Venta registrada exitosamente.")
    input("Presione Enter para continuar...")


def eliminar_venta(ventas):
    if not ventas:
        print("No hay ventas para eliminar.")
        input("Presione Enter para continuar...")
        return

    codigo = input("Ingrese el código de la venta a eliminar: ").strip()
    for i, venta in enumerate(ventas):
        if venta['codigo'] == codigo:
            print(f"Venta encontrada: Cliente: {venta['cliente']} | Total: S/. {venta['total']:.2f}")
            confirmacion = input("¿Está seguro que desea eliminar esta venta? (SI para confirmar): ").strip().upper()
            if confirmacion == "SI":
                ventas.pop(i)
                guardar_ventas(ventas)
                print("Venta eliminada correctamente.")
            else:
                print("Eliminación cancelada.")
            input("Presione Enter para continuar...")
            return

    print("Venta no encontrada.")
    input("Presione Enter para continuar...")

def buscar_venta_por_codigo(ventas):
    if not ventas:
        print("No hay ventas registradas.")
        input("Presione Enter para continuar...")
        return

    codigo = input("Ingrese el código de la venta a buscar: ").strip()

    for venta in ventas:
        if venta['codigo'] == codigo:
            print("\nVenta encontrada:")
            for clave, valor in venta.items():
                if clave == "productos":
                    print("Productos:")
                    for prod in valor:
                        print(f"  - {prod['nombre']} | Cantidad: {prod['cantidad']} | Subtotal: S/. {prod['subtotal']:.2f}")
                else:
                    print(f"{clave.capitalize()}: {valor}")
            input("Presione Enter para continuar...")
            return

    print("No se encontró ninguna venta con ese código.")
    input("Presione Enter para continuar...")

def generar_boleta(ventas):
    if not ventas:
        print("No hay ventas para generar boleta.")
        input("Presione Enter para continuar...")
        return

    codigo = input("Ingrese el código de la venta: ").strip()
    for venta in ventas:
        if venta['codigo'] == codigo:
            print("\nBOLETA DE VENTA")
            print("Cliente:", venta['cliente'])
            print("Fecha:", venta['fecha'])
            print("Productos:")
            for prod in venta['productos']:
                print(f"- {prod['nombre']} | {prod['cantidad']} x S/. {prod['precio_unitario']} = S/. {prod['subtotal']:.2f}")
            print(f"TOTAL: S/. {venta['total']:.2f}")
            input("Presione Enter para continuar...")
            return

    print("Venta no encontrada.")
    input("Presione Enter para continuar...")
