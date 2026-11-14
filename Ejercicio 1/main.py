def limpiar_registro_sensor(registro_raw):
    
    sensor_id = registro_raw["sensor_id"].strip()
    temperatura = float(registro_raw["temperatura"].replace("C", "").strip())
    ubicacion = registro_raw.get("ubicacion", "").strip()

    if not ubicacion:
        ubicacion = "Planta Centro"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    
    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        suma_temperaturas += temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    if len(lista_sensores_limpios) > 0:
        promedio_temperatura = (
            suma_temperaturas / len(lista_sensores_limpios)
        )
    else:
        promedio_temperatura = 0.0

    return lista_sensores_alerta, promedio_temperatura


# ---------------------------------------
# BLOQUE PRINCIPAL: EJECUCIÓN DEL PROGRAMA
# ---------------------------------------

if __name__ == "__main__":

    #Datos crudos de los sensores
    registros_raw = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte"
        },
        {
            "sensor_id": " SENSOR-002 ",
            "temperatura": "32.8C",
            "ubicacion": "Planta Sur"
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": "28.2C",
            "ubicacion": "Planta Centro"
        },
        {
            "sensor_id": " SENSOR-004 ",
            "temperatura": "35.1C"
        }
    ]

    #Limpieza de los registros
    sensores_limpios = []

    for registro in registros_raw:
        sensor_limpio = limpiar_registro_sensor(registro)
        sensores_limpios.append(sensor_limpio)

    #Configuración del umbral
    umbral = 30.0

    #Generación del resumen
    alertas, promedio = generar_resumen_sensores(
        sensores_limpios,
        umbral
    )

    #Impresión del reporte final
    print("\n========== REPORTE DE SENSORES ==========")

    print("\nSensores registrados:")

    for sensor in sensores_limpios:
        print(
            f"ID: {sensor['sensor_id']} | "
            f"Temperatura: {sensor['temperatura']:.2f} °C | "
            f"Ubicación: {sensor['ubicacion']}"
        )

    print("\n---------- RESUMEN ----------")

    print(f"Umbral de temperatura: {umbral:.2f} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")

    print("\nSensores que superan el umbral:")

    if alertas:
        for sensor_id in alertas:
            print(f"¡ALERTA! {sensor_id}")
    else:
        print("No se detectaron temperaturas superiores al umbral.")

    print("\n=========================================")
