class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - S/ {self.precio} - Stock: {self.stock}"

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["codigo"],
            data["nombre"],
            data["categoria"],
            data["precio"],
            data["stock"]
        )