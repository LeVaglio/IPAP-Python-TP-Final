import json

class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(
        lista_dispositivos,
        ruta_archivo
    ):

        catalogo = [
            dispositivo.to_dict()
            for dispositivo in lista_dispositivos
        ]

        with open(
            ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado correctamente: {ruta_archivo}")
