#!/usr/bin/python3
from unittest.case import TestCase

def resto(param1,param2):
    return param1%param2

class RestoCasosDeTeste(TestCase):
    def test_assercao_basica(self):
        self.assertEqual(1,1,'Numeros deveriam ser iguais')


    def test_funcao_resto(self):
        self.assertEqual(1, resto(-1,2))

