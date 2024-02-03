import unittest
from src.Fecha import Fecha

class PruebaFecha(unittest.TestCase):
    def setUp(self):
        self.fecha = Fecha(0,0,0)

    def tearDown(self):
        self.fecha = None

    def test_ValidarFecha_retonaTrueoFalse(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "dia": 20, "mes": 6, "anio": 2008, "correcto": True},
            {"Case": "Caso 02", "dia": 21, "mes": 0, "anio": 3000, "correcto": False},
            {"Case": "Caso 03", "dia": 21, "mes": 13, "anio": 3000, "correcto": False},
            {"Case": "Caso 04", "dia": 0, "mes": 11, "anio": 2000, "correcto": False},
            {"Case": "Caso 05", "dia": 32, "mes": 11, "anio": 2000, "correcto": False},
            {"Case": "Caso 06", "dia": 31, "mes": 11, "anio": 2000, "correcto": False},
            {"Case": "Caso 07", "dia": 31, "mes": 12, "anio": 2000, "correcto": True},
            {"Case": "Caso 08", "dia": 30, "mes": 2, "anio": 2008, "correcto": False},
            {"Case": "Caso 09", "dia": 29, "mes": 2, "anio": 2008, "correcto": True},
            {"Case": "Caso 10", "dia": 29, "mes": 2, "anio": 2000, "correcto": True},
            {"Case": "Caso 11", "dia": 29, "mes": 2, "anio": 2007, "correcto": False},
            {"Case": "Caso 12", "dia": 29, "mes": 2, "anio": 1900, "correcto": False},

        )
        for item in items:
            with self.subTest(item["Case"]):
                self.fecha.dias = item["dia"]
                self.fecha.meses = item["mes"]
                self.fecha.anios = item["anio"]
                resultadoEsperado = item["correcto"]

            # Do
            resultadoActual = self.fecha.valida()

            # Assert
            self.assertEqual(resultadoActual, resultadoEsperado)
