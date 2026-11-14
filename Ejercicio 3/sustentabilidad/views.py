from django.shortcuts import render
from .services import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 1800},
        {"planta": "Planta Central", "consumo_kwh": 950},
        {"planta": "Planta Norte", "consumo_kwh": 800},
        {"planta": "Planta Sur", "consumo_kwh": 500}
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "consumo_maximo": metricas["consumo_maximo"],
        "consumo_por_planta": metricas["consumo_por_planta"],
        "emisiones_por_planta": metricas["emisiones_por_planta"]
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )
