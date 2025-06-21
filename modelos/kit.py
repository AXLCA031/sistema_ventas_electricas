from datetime import datetime

class Kit:
    def __init__(self, codigo, nombre, productos, total, fecha_creacion=None):
        self.codigo = codigo
        self.nombre = nombre
        self.productos = productos
        self.total = total
        self.fecha_creacion = fecha_creacion or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        productos_str = "\n".join([
            f"  - {p['nombre']} (x{p['cantidad']}): S/ {p['precio_unitario'] * p['cantidad']:.2f}"
            for p in self.productos
        ])
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Fecha de Creación: {self.fecha_creacion}\n"
            f"Productos:\n{productos_str}\n"
            f"Total: S/ {self.total:.2f}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "productos": self.productos,
            "total": self.total,
            "fecha_creacion": self.fecha_creacion
        }

    @staticmethod
    def from_dict(data):
        return Kit(
            codigo=data["codigo"],
            nombre=data["nombre"],
            productos=data["productos"],
            total=data["total"],
            fecha_creacion=data.get("fecha_creacion")
        )
