from datetime import datetime

class Venta:
    def __init__(self, codigo, cliente, productos, total, fecha=None, kits=None):
        self.codigo = codigo
        self.cliente = cliente
        self.productos = productos
        self.total = total
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.kits = kits or []

    def __str__(self):
        productos_str = "\n".join([
            f"  - {p['nombre']} (x{p['cantidad']}): S/ {p['precio_unitario'] * p['cantidad']:.2f}"
            for p in self.productos
        ])
        kits_str = "\n".join([
            f"  - {k['nombre']} (x{k['cantidad']}): S/ {k['subtotal']:.2f}"
            for k in self.kits
        ]) if self.kits else "  - Ninguno"

        return (
            f"Código: {self.codigo}\n"
            f"Cliente: {self.cliente}\n"
            f"Fecha: {self.fecha}\n"
            f"Productos:\n{productos_str}\n"
            f"Kits:\n{kits_str}\n"
            f"Total: S/ {self.total:.2f}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "cliente": self.cliente,
            "productos": self.productos,
            "total": self.total,
            "fecha": self.fecha,
            "kits": self.kits
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            codigo=data["codigo"],
            cliente=data["cliente"],
            productos=data["productos"],
            total=data["total"],
            fecha=data.get("fecha"),
            kits=data.get("kits", [])
        )