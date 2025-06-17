from datetime import datetime

class Venta:
    def __init__(self, codigo, cliente, productos, total, fecha=None):
        self.codigo = codigo
        self.cliente = cliente
        self.productos = productos 
        self.total = total
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        productos_str = "\n".join([f"  - {p['nombre']} (x{p['cantidad']}): S/ {p['precio'] * p['cantidad']:.2f}" for p in self.productos])
        return (
            f"Código: {self.codigo}\n"
            f"Cliente: {self.cliente}\n"
            f"Fecha: {self.fecha}\n"
            f"Productos:\n{productos_str}\n"
            f"Total: S/ {self.total:.2f}"
        )
