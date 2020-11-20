
# def ludo(jogador, dado):
#     return jogador.pinos

# class Jogador:
#     def __init__(self, pinos=[0, 0, 0, 0]):
#         self.pinos = pinos

class CasaOcupada(Exception):
    ...

class MovimentoInicialInvalido(Exception):
    ...

class MovimentoFinalInvalido(Exception):
    ...

class TemPinoNaBase(Exception):
    ...

class Tabuleiro:
    def __init__(self):
        self.posicoes = [None] * 38

    def posiciona(self, pino, posicao):
        self.posicoes[posicao] = pino

    def movimenta(self, pino, passos):
        posicao_atual = self.posicao(pino)
        nova_posicao = posicao_atual + passos

        if nova_posicao == 37 and self.posicoes[0]:
            raise TemPinoNaBase()

        if nova_posicao > 37:
            raise MovimentoFinalInvalido()

        if posicao_atual == 0 and passos not in (1, 6):
            raise MovimentoInicialInvalido()

        if self.posicoes[nova_posicao]:
            raise CasaOcupada()

        self.posicoes[posicao_atual] = None
        self.posicoes[nova_posicao] = pino

    def posicao(self, pino):
        return self.posicoes.index(pino)
