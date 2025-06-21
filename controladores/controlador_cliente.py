import json
from modelos.cliente import Cliente

RUTA_CLIENTES = "data/clientes.json"

def cargar_clientes():
    try:
        with open(RUTA_CLIENTES, "r") as f:
            data = json.load(f)
            return [Cliente.from_dict(c) for c in data]
    except FileNotFoundError:
        return []

def guardar_clientes(lista_clientes):
    with open(RUTA_CLIENTES, "w") as f:
        json.dump([c.to_dict() for c in lista_clientes], f, indent=4)

def generar_codigo_cliente(clientes):
    max_num = 0
    for cliente in clientes:
        if cliente.codigo.startswith("C") and cliente.codigo[1:].isdigit():
            num = int(cliente.codigo[1:])
            max_num = max(max_num, num)
    return f"C{max_num + 1:03d}"

def registrar_cliente(clientes):
    print("\n=== REGISTRAR CLIENTE ===\n")
    codigo = generar_codigo_cliente(clientes)
    nombre = input("Nombre del cliente: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    correo = input("Correo electrónico: ")

    nuevo = Cliente(codigo, nombre, telefono, direccion, correo, cantidad_ventas=0)
    clientes.append(nuevo)
    guardar_clientes(clientes)

    print(f"\nCliente registrado exitosamente con código: {codigo}")
    input("Presione Enter para continuar...")

def listar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
    else:
        print("\nClientes registrados:")
        print("=" * 40)
        for cliente in clientes:
            print(f"Código: {cliente.codigo} | Nombre: {cliente.nombre}")
        print("=" * 40)
    input("Presione Enter para continuar...")


def buscar_cliente(clientes):
    codigo = input("Ingrese el código del cliente a buscar: ").strip()
    for c in clientes:
        if c.codigo == codigo:
            print("\nCliente encontrado:\n")
            print(c)
            break
    else:
        print("Cliente no encontrado.")
    input("Presione Enter para continuar...")

def editar_cliente(clientes):
    codigo = input("Ingrese el código del cliente a editar: ").strip()
    for cliente in clientes:
        if cliente.codigo == codigo:
            print("\nCliente encontrado. Deje el campo vacío si no desea cambiarlo.\n")

            nuevo_nombre = input(f"Nuevo nombre [{cliente.nombre}]: ") or cliente.nombre
            nuevo_telefono = input(f"Nuevo teléfono [{cliente.telefono}]: ") or cliente.telefono
            nueva_direccion = input(f"Nueva dirección [{cliente.direccion}]: ") or cliente.direccion
            nuevo_correo = input(f"Nuevo correo [{cliente.correo}]: ") or cliente.correo

            cliente.nombre = nuevo_nombre
            cliente.telefono = nuevo_telefono
            cliente.direccion = nueva_direccion
            cliente.correo = nuevo_correo

            guardar_clientes(clientes)
            print("Cliente actualizado correctamente.")
            break
    else:
        print("Cliente no encontrado.")
    input("Presione Enter para continuar...")

def eliminar_cliente(clientes):
    codigo = input("Ingrese el código del cliente a eliminar: ").strip()
    for i, cliente in enumerate(clientes):
        if cliente.codigo == codigo:
            print(f"Cliente encontrado: {cliente.nombre}")
            confirmacion = input("¿Está seguro que desea eliminarlo? (SI para confirmar): ").strip().upper()
            if confirmacion == "SI":
                clientes.pop(i)
                guardar_clientes(clientes)
                print("Cliente eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            break
    else:
        print("Cliente no encontrado.")
    input("Presione Enter para continuar...")