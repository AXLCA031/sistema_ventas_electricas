class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - S/ {self.precio} - Stock: {self.stock}"
