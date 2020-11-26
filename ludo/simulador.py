from itertools import product

class MovimentoInicialInvalido(Exception): pass
class CasaOcupada(Exception): pass
class JogadorAindaTemPinosNaBase(Exception): pass
class PinoPassouDoPodio(Exception): pass

class Tabuleiro(dict):
    _JOGADORES = _PINOS = (1, 2, 3, 4)
    _BASE = 0
    _PODIO = 37
    _MOVIMENTOS_INICIAIS_VALIDOS = (1, 6)

    def __init__(self):
        for jp in product(self._JOGADORES, self._PINOS):
            self[jp] = self._BASE

    def posicao(self, jogador, pino):
        return self[jogador, pino]

    def mover(self, jogador, pino, passos):
        posicao_atual = self[jogador, pino]

        if posicao_atual == self._BASE and not passos in self._MOVIMENTOS_INICIAIS_VALIDOS:
            raise MovimentoInicialInvalido()
        
        nova_posicao = posicao_atual + passos
        if nova_posicao in self.values():
            raise CasaOcupada()

        if nova_posicao > self._PODIO:
            raise PinoPassouDoPodio()

        if nova_posicao == self._PODIO and self._tem_pinos_na_base(jogador):
            raise JogadorAindaTemPinosNaBase()
        
        self[jogador, pino] = nova_posicao
        
    def _tem_pinos_na_base(self, jogador):
        return not all((self[jp] for jp in product([jogador], self._PINOS)))
