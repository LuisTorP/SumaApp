import unittest
from src.logica.Suma import Suma

class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma=Suma()

    def tearDown(self):
        self.suma=None
    def test_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        # Arrange
        self.suma=Suma()
        self.Sumando1=-3
        self.Sumando2=-7
        self.resultadoEsperado=-10

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.Sumando1,self.Sumando2)

        # Assert
        self.assertEqual(self.resultadoEsperado,self.resultadoActual)

