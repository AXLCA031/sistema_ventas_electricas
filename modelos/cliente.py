class Cliente:
    def __init__(self, codigo, nombre, telefono, direccion, correo, cantidad_ventas=0):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.cantidad_ventas = cantidad_ventas

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "correo": self.correo,
            "cantidad_ventas": self.cantidad_ventas
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            data["codigo"],
            data["nombre"],
            data["telefono"],
            data["direccion"],
            data["correo"],
            data.get("cantidad_ventas", 0)
        )

    def __str__(self):
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Teléfono: {self.telefono}\n"
            f"Dirección: {self.direccion}\n"
            f"Correo: {self.correo}\n"
            f"Cantidad de Ventas: {self.cantidad_ventas}\n"
        )
