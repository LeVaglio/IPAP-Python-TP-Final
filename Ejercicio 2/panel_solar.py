from dispositivo import DispositivoEcológico

class PanelSolar(DispositivoEcológico):
    def __init__(
        self,
        nombre,
        precio,
        stock,
        potencia_w,
        eficiencia
    ):

        super().__init__(nombre, precio, stock)

        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    def ficha_tecnica(self):
        return (
            f"=== PANEL SOLAR ===\n"
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}\n"
            f"Potencia: {self.potencia_w} W\n"
            f"Eficiencia: {self.eficiencia}%"
        )

    def to_dict(self):
        datos = super().to_dict()

        datos["potencia_w"] = self.potencia_w
        datos["eficiencia"] = self.eficiencia

        return datos
