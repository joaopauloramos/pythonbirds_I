import unittest
from unittest.case import TestCase


def resto(param, param1):
    return param%param1


class RestoCasosDeTeste(TestCase):
    def test_assercao_basica(self):
        self.assertEqual(1, 1, 'Números deveriam ser iguais')

    def test_funcao_resto_numeros_positivos(self):
        self.assertEqual(0, resto(8,2))

    def test_funcao_resto_numeros_negativos(self):
        self.assertEqual(1, resto(-1,2))

if __name__ == '__main__':
    unittest.main()
