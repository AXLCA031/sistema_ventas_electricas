# controlador_reporte.py
from collections import Counter, defaultdict
from modelos.venta import Venta
from modelos.cliente import Cliente
import matplotlib.pyplot as plt


def productos_mas_vendidos(ventas, top_n=5):
    contador = Counter()
    for venta in ventas:
        for producto in venta.productos:
            contador[producto['nombre']] += producto['cantidad']

    top = contador.most_common(top_n)

    print(f"\nTop {top_n} productos más vendidos:\n")
    for producto, cantidad in top:
        print(f"{producto}: {cantidad} unidades")

    if top:
        nombres = [p[0] for p in top]
        cantidades = [p[1] for p in top]

        plt.figure(figsize=(10, 6))
        plt.bar(nombres, cantidades, color='skyblue')
        plt.title(f"Top {top_n} productos más vendidos")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad vendida")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay datos suficientes para generar el gráfico.")

    input("\nPresione Enter para continuar...")


def kits_mas_vendidos(ventas, top_n=5):
    contador_kits = Counter()
    for venta in ventas:
        for kit in getattr(venta, "kits", []):
            clave = kit["nombre"]
            contador_kits[clave] += kit["cantidad"]

    top = contador_kits.most_common(top_n)

    print(f"\nTop {top_n} kits más vendidos:\n")
    for nombre_kit, cantidad in top:
        print(f"Kit: {nombre_kit} - Cantidad vendida: {cantidad}")

    if top:
        nombres = [k[0] for k in top]
        cantidades = [k[1] for k in top]

        plt.figure(figsize=(10, 6))
        plt.bar(nombres, cantidades, color='salmon')
        plt.title(f"Top {top_n} Kits más vendidos")
        plt.xlabel("Kit")
        plt.ylabel("Cantidad vendida")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay datos suficientes para generar el gráfico.")

    input("\nPresione Enter para continuar...")


def clientes_con_mas_ventas(clientes, top_n=5):
    clientes_ordenados = sorted(clientes, key=lambda c: c.cantidad_ventas, reverse=True)[:top_n]

    print(f"\nTop {top_n} clientes con más ventas:\n")
    for cliente in clientes_ordenados:
        print(f"{cliente.nombre} - Ventas: {cliente.cantidad_ventas}")

    if clientes_ordenados:
        nombres = [c.nombre for c in clientes_ordenados]
        ventas = [c.cantidad_ventas for c in clientes_ordenados]

        plt.figure(figsize=(10, 6))
        plt.bar(nombres, ventas, color='lightgreen')
        plt.title(f"Top {top_n} clientes con más ventas")
        plt.xlabel("Cliente")
        plt.ylabel("Cantidad de ventas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay datos suficientes para generar el gráfico.")

    input("\nPresione Enter para continuar...")


def total_ventas_diarias(ventas):
    resumen = defaultdict(float)
    for venta in ventas:
        fecha = venta.fecha.split(" ")[0]
        resumen[fecha] += venta.total

    print("\nTotal de ventas por día:")
    for fecha, total in resumen.items():
        print(f"{fecha}: S/. {total:.2f}")

    if resumen:
        fechas = sorted(resumen.keys())
        totales = [resumen[fecha] for fecha in fechas]

        plt.figure(figsize=(10, 6))
        plt.plot(fechas, totales, marker='o', linestyle='-', color='orange')
        plt.title("Total de ventas por día")
        plt.xlabel("Fecha")
        plt.ylabel("Total (S/.)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay datos suficientes para generar el gráfico.")

    input("\nPresione Enter para continuar...")


def total_ingresos(ventas):
    total = sum(v.total for v in ventas)
    print(f"\nIngresos totales: S/. {total:.2f}")
    input("\nPresione Enter para continuar...")


def categorias_mas_vendidas(ventas, productos_disponibles, top_n=5):
    categoria_counter = Counter()

    productos_dict = {p.codigo: p for p in productos_disponibles}

    for venta in ventas:
        for prod in venta.productos:
            codigo = prod["codigo"]
            if codigo.startswith("P"):
                producto = productos_dict.get(codigo)
                if producto:
                    categoria = producto.categoria
                    cantidad = prod["cantidad"]
                    categoria_counter[categoria] += cantidad

    top = categoria_counter.most_common(top_n)

    print(f"\nTop {top_n} categorías más vendidas:\n")
    for categoria, cantidad in top:
        print(f"{categoria}: {cantidad} unidades vendidas")

    if top:
        categorias = [c[0] for c in top]
        cantidades = [c[1] for c in top]

        plt.figure(figsize=(10, 6))
        plt.bar(categorias, cantidades, color='mediumseagreen')
        plt.title(f"Top {top_n} Categorías más vendidas")
        plt.xlabel("Categoría")
        plt.ylabel("Unidades vendidas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay datos suficientes para generar el gráfico.")

    input("\nPresione Enter para continuar...")