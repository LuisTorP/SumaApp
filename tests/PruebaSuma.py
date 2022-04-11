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
        self.Minuendo=19
        self.sustraendo=50
        self.resultadoEsperado=69

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.Minuendo, self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoEsperado,self.resultadoActual)

class PruebaResta (unittest.TestCase):
    def setUp(self):
        self.resta = Suma ()

    def tearDown(self):
        self.resta = None
    def test_operacionResta_dosNumerosPositivos_retornaResta(self):
        # Arrange
        self.minuendo=19
        self.sustraendo=2
        self.resultadoEsperado=17

        # Do
        self.resultadoActual=self.suma.operacionResta(self.minuendo, self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoEsperado,self.resultadoActual)

