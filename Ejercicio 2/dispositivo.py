from excepciones import StockInvalidoError

class DispositivoEcológico:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, cantidad):

        if cantidad < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")

        self.__stock = cantidad

    def ficha_tecnica(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }
