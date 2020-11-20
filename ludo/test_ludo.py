# import pytest

# from simulador import *

# def test_tabuleiro_inicial():
#     j1 = Jogador()
#     j2 = Jogador()
#     j3 = Jogador()
#     j4 = Jogador()
#     jogadores = [j1, j2, j3, j4]
#     tabuleiro = Tabuleiro(jogadores)
#     tabuleiro.movimenta(j1, 1)
#     assert j1.pinos == [1, 0, 0, 0]

# def test_tabuleiro_pino_na_1():
#     j1 = Jogador()
#     j2 = Jogador()
#     j3 = Jogador()
#     j4 = Jogador(pinos=[1, 0, 0, 0])
#     jogadores = [j1, j2, j3, j4]
#     tabuleiro = Tabuleiro(jogadores)
#     tabuleiro.movimenta(j1, 1)
#     assert j1.pinos == [0, 0, 0, 0]


# # @pytest.mark.parametrize('dado,posicao_inicial,nova_posicao', (
# #     (1, Jogador(), Jogador(), Jogador(), Jogador(), [1, 0, 0, 0]),
# #     (6, Jogador(), Jogador(), Jogador(), Jogador(), [6, 0, 0, 0]),
# #     ))
# # def test_base_e_dado_1_ou_6(dado, posicao_inicial, nova_posicao):
# #     assert nova_posicao == ludo(posicao_inicial, dado)

# @pytest.mark.parametrize('dado,posicao_inicial,nova_posicao', (
#     (2, Jogador(), [0,0,0,0]),
#     (3, Jogador(), [0,0,0,0]),
#     (4, Jogador(), [0,0,0,0]),
#     (5, Jogador(), [0,0,0,0]),
#     ))
# def test_nao_move_pino_da_base(dado, posicao_inicial, nova_posicao):
#     assert nova_posicao == ludo(posicao_inicial, dado)


