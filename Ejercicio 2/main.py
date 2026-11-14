from dispositivo import DispositivoEcológico
from panel_solar import PanelSolar
from excepciones import StockInvalidoError
from gestor_inventario import GestorInventario

def crear_catalogo():
    dispositivos = [
        DispositivoEcológico(
            "Lámpara LED",
            15000,
            20
        ),

        PanelSolar(
            "Panel Solar EcoTech",
            250000,
            10,
            450,
            21.5
        ),

        PanelSolar(
            "Panel Solar Compacto",
            180000,
            5,
            350,
            19.8
        )
    ]

    return dispositivos


def mostrar_fichas(dispositivos):
    print("\n=== FICHAS TÉCNICAS ===")

    for dispositivo in dispositivos:
        print("\n" + dispositivo.ficha_tecnica())


def probar_stock_invalido(dispositivo):
    print("\n=== PRUEBA DE STOCK ===")

    try:
        dispositivo.stock = -5

    except StockInvalidoError as error:
        print(f"Error controlado: {error}")


def main():
    dispositivos = crear_catalogo()

    mostrar_fichas(dispositivos)

    probar_stock_invalido(dispositivos[0])

    print("\n=== EXPORTACIÓN ===")

    GestorInventario.guardar_catalogo_json(
        dispositivos,
        "catalogo_ecotech.json"
    )


if __name__ == "__main__":
    main()
