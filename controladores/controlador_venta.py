import json
import os
from datetime import datetime
from modelos.venta import Venta
from modelos.producto import Producto
from modelos.cliente import Cliente
from controladores.controlador_producto import cargar_productos, guardar_productos
from controladores.controlador_kit import cargar_kits
from controladores.controlador_cliente import cargar_clientes, guardar_clientes, generar_codigo_cliente


RUTA_VENTAS = "data/ventas.json"

def cargar_ventas():
    try:
        with open(RUTA_VENTAS, "r") as f:
            data = json.load(f)
            return [Venta.from_dict(v) for v in data]
    except FileNotFoundError:
        return []

def guardar_ventas(lista_ventas):
    with open(RUTA_VENTAS, "w") as f:
        json.dump([v.to_dict() for v in lista_ventas], f, indent=4)

def listar_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("\nVentas registradas:")
        print("=" * 40)
        for venta in ventas:
            print(f"Código: {venta.codigo} | Cliente: {venta.cliente}")
        print("=" * 40)
    input("Presione Enter para continuar...")

def generar_codigo(ventas):
    max_num = 0
    for venta in ventas:
        if venta.codigo.startswith("V") and venta.codigo[1:].isdigit():
            num = int(venta.codigo[1:])
            max_num = max(max_num, num)
    return f"V{max_num + 1:03d}"

def registrar_venta(ventas):
    productos_disponibles = cargar_productos()
    kits_disponibles = cargar_kits()
    clientes = cargar_clientes()

    if not productos_disponibles:
        print("No hay productos disponibles para registrar una venta.")
        input("Presione Enter para continuar...")
        return

    print("\nClientes disponibles:")
    for c in clientes:
        print(f"Código: {c.codigo} | Nombre: {c.nombre}")

    while True:
        codigo_cliente = input("Ingrese el código del cliente: ").strip()
        cliente = next((c for c in clientes if c.codigo == codigo_cliente), None)

        if cliente:
            break
        else:
            print("Código inválido. ¿Desea registrar un nuevo cliente? (S/N)")
            respuesta = input().strip().lower()
            if respuesta == "s":
                codigo_cliente = generar_codigo_cliente(clientes)
                print(f"\n=== Registro de nuevo cliente (Código: {codigo_cliente}) ===")
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                direccion = input("Dirección: ")
                correo = input("Correo: ")

                cliente = Cliente(codigo_cliente, nombre, telefono, direccion, correo, cantidad_ventas=0)
                clientes.append(cliente)
                guardar_clientes(clientes)
                print("Cliente registrado exitosamente.")
                break
            else:
                print("Debe ingresar un código válido para continuar.")


    cliente.cantidad_ventas += 1

    codigo_venta = generar_codigo(ventas)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    productos_venta = []
    kits_vendidos = []
    total = 0.0

    while True:
        print("\n¿Qué desea vender?")
        print("1. Producto individual")
        print("2. Kit existente")
        print("3. Terminar")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "3":
            break

        elif opcion == "1":
            codigo_producto = input("Ingrese el código del producto: ").strip()
            producto = next((p for p in productos_disponibles if p.codigo == codigo_producto), None)
            if not producto:
                print("Producto no encontrado.")
                continue

            print(f"Producto: {producto.nombre} | Precio unitario: {producto.precio} | Stock: {producto.stock}")
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida.")
                continue

            if cantidad > producto.stock:
                print("Stock insuficiente.")
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

        elif opcion == "2":
            if not kits_disponibles:
                print("No hay kits registrados.")
                continue

            print("\nKits disponibles:")
            for kit in kits_disponibles:
                print(f"- Código: {kit.codigo} | Nombre: {kit.nombre} | Total: S/. {kit.total:.2f}")

            codigo_kit = input("Ingrese el código del kit a vender: ").strip()
            kit = next((k for k in kits_disponibles if k.codigo == codigo_kit), None)
            if not kit:
                print("Kit no encontrado.")
                continue

            try:
                cantidad_kit = int(input("¿Cuántos kits desea vender? "))
            except ValueError:
                print("Cantidad inválida.")
                continue

            stock_suficiente = True
            for item in kit.productos:
                prod = next((p for p in productos_disponibles if p.codigo == item["codigo"]), None)
                if not prod or prod.stock < item["cantidad"] * cantidad_kit:
                    print(f"No hay suficiente stock del producto: {item['nombre']}")
                    stock_suficiente = False
                    break

            if not stock_suficiente:
                print("Venta de kit cancelada.")
                continue

            for item in kit.productos:
                prod = next((p for p in productos_disponibles if p.codigo == item["codigo"]), None)
                prod.stock -= item["cantidad"] * cantidad_kit

                productos_venta.append({
                    "codigo": item["codigo"],
                    "nombre": item["nombre"],
                    "precio_unitario": item["precio_unitario"],
                    "cantidad": item["cantidad"] * cantidad_kit,
                    "subtotal": item["precio_unitario"] * item["cantidad"] * cantidad_kit
                })

            kits_vendidos.append({
                "nombre": kit.nombre,
                "cantidad": cantidad_kit
            })

            total += kit.total * cantidad_kit
            print(f"Kit agregado correctamente: {kit.nombre} x {cantidad_kit}")

        else:
            print("Opción inválida.")

    if not productos_venta:
        print("No se registraron productos o kits para esta venta.")
        input("Presione Enter para continuar...")
        return

    nueva_venta = Venta(
        codigo=codigo_venta,
        cliente=f"{cliente.codigo} - {cliente.nombre}",
        productos=productos_venta,
        total=total,
        fecha=fecha,
        kits=kits_vendidos if kits_vendidos else []
    )

    ventas.append(nueva_venta)
    guardar_ventas(ventas)
    guardar_productos(productos_disponibles)
    guardar_clientes(clientes)

    print(f"\nVenta '{codigo_venta}' registrada exitosamente.")
    input("Presione Enter para continuar...")
