from unittest import TestCase

from calculadora.oo.framework import Calculadora


class CalculadoraParaTeste(Calculadora):
    def obter_inputs(self):
        return '+',1,2


class CalculadoraTestes(TestCase):
    def test_adcionar_operacao(self):
        obj_qq=''
        calculadora =Calculadora()
        calculadora.adicionar_operacao('string', obj_qq)
        self.assertEqual(calculadora._operacoes['string'],obj_qq)

    def teste_efetuar_operacao(self):
        calculadora = CalculadoraParaTeste()
        self.assertEqual(3, calculadora.efetuar_operacao())