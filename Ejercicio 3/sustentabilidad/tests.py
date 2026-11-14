import unittest
from .services import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertAlmostEqual(resultado, 40.0)

    def test_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(100, 0.5)
        self.assertAlmostEqual(resultado, 50.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)
