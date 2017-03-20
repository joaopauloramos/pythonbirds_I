#!/usr/in/python3

from unittest.case import TestCase

from calculadora.oo.framework import Adicao, Calculadora

class CalculadoraParaTeste(Calculadora):
    def obter_inputs(self):
        return 'mock',1,2

class OperacaoMock:
    def calcular(self, p1,p2):
        return p1,p2


class AdicaoCasosDeTeste(TestCase):

    def teste_com_numeros_positivos(self):
        adicao = Adicao()
        for i in range(10):
            self.assertEqual(2*i,adicao.calcular(i,i))

class CalculadoraTestes(TestCase):
    def test_adcionar_operacao(self):
        obj_qq = ''
        calculadora = Calculadora()
        calculadora.adicionar_operacao('string', obj_qq)
        self.assertEqual(calculadora._operacoes['string'], obj_qq)

    def teste_efetuar_operacao(self):
        calculadora = CalculadoraParaTeste()
        calculadora.adicionar_operacao('mock',OperacaoMock())
        self.assertEqual((1,2), calculadora.efetuar_operacao())

