import json
from modelos.kit import Kit
from modelos.producto import Producto
from controladores.controlador_producto import cargar_productos
from datetime import datetime

RUTA_KITS = "data/kits.json"

def cargar_kits():
    try:
        with open(RUTA_KITS, "r") as f:
            data = json.load(f)
            return [Kit.from_dict(k) for k in data]
    except FileNotFoundError:
        return []

def guardar_kits(lista_kits):
    with open(RUTA_KITS, "w") as f:
        json.dump([k.to_dict() for k in lista_kits], f, indent=4)

def generar_codigo_kit(kits):
    max_num = 0
    for kit in kits:
        if kit.codigo.startswith("K") and kit.codigo[1:].isdigit():
            num = int(kit.codigo[1:])
            max_num = max(max_num, num)
    return f"K{max_num + 1:03d}"

def registrar_kit(kits):
    productos_disponibles = cargar_productos()
    if not productos_disponibles:
        print("No hay productos disponibles para crear kits.")
        input("Presione Enter para continuar...")
        return

    codigo_kit = generar_codigo_kit(kits)
    nombre_kit = input("Nombre del kit: ")
    productos_kit = []
    total = 0.0

    while True:
        codigo_producto = input("Ingrese código de producto (o 'fin' para terminar): ").strip()
        if codigo_producto.lower() == "fin":
            break

        producto = next((p for p in productos_disponibles if p.codigo == codigo_producto), None)
        if not producto:
            print("Producto no encontrado.")
            continue

        print(f"Producto: {producto.nombre} | Precio: {producto.precio}")
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            continue

        subtotal = producto.precio * cantidad
        total += subtotal
        productos_kit.append({
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio_unitario": producto.precio,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

    if not productos_kit:
        print("No se agregó ningún producto.")
        input("Presione Enter para continuar...")
        return

    nuevo_kit = Kit(codigo_kit, nombre_kit, productos_kit, total)
    kits.append(nuevo_kit)
    guardar_kits(kits)
    print(f"Kit '{codigo_kit}' registrado exitosamente.")
    input("Presione Enter para continuar...")

def listar_kits(kits):
    if not kits:
        print("No hay kits registrados.")
    else:
        print("\nKITS REGISTRADOS")
        print("=" * 40)
        for kit in kits:
            print(f"Código: {kit.codigo} | Nombre: {kit.nombre}")
        print("=" * 40)
    input("Presione Enter para continuar...")

def eliminar_kit(kits):
    if not kits:
        print("No hay kits para eliminar.")
        input("Presione Enter para continuar...")
        return

    codigo = input("Ingrese el código del kit a eliminar: ").strip()
    for i, kit in enumerate(kits):
        if kit.codigo == codigo:
            print(f"Kit encontrado: {kit.nombre} | Total: S/. {kit.total:.2f}")
            confirmacion = input("¿Eliminar este kit? (SI para confirmar): ").strip().upper()
            if confirmacion == "SI":
                kits.pop(i)
                guardar_kits(kits)
                print("Kit eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            input("Presione Enter para continuar...")
            return

    print("Kit no encontrado.")
    input("Presione Enter para continuar...")

def buscar_kit_por_codigo(kits):
    if not kits:
        print("No hay kits registrados.")
        input("Presione Enter para continuar...")
        return

    codigo = input("Ingrese el código del kit a buscar: ").strip()
    for kit in kits:
        if kit.codigo == codigo:
            print("\nKIT ENCONTRADO\n")
            print(kit)
            input("Presione Enter para continuar...")
            return

    print("No se encontró ningún kit con ese código.")
    input("Presione Enter para continuar...")
