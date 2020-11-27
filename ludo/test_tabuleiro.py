import pytest

from tabuleiro import *

def test_tabuleiro():
    tabuleiro = Tabuleiro()
    assert tabuleiro.posicao(jogador=1, pino=1) == 0
    assert tabuleiro.posicao(jogador=4, pino=4) == 0

def test_movimentos_iniciais_validos():
    tabuleiro = Tabuleiro()
    tabuleiro.mover(jogador=1, pino=1, passos=1)
    assert tabuleiro.posicao(jogador=1, pino=1) == 1

    tabuleiro.mover(jogador=2, pino=1, passos=6)
    assert tabuleiro.posicao(jogador=2, pino=1) == 6

@pytest.mark.parametrize('passos', (2, 3, 4, 5))
def test_movimentos_iniciais_ilegais(passos):
    tabuleiro = Tabuleiro()
    with pytest.raises(MovimentoInicialInvalido):
        tabuleiro.mover(jogador=1, pino=1, passos=passos)
    assert tabuleiro.posicao(jogador=1, pino=1) == 0

def test_movimento_valido_para_casa_ocupada():
    tabuleiro = Tabuleiro()
    tabuleiro.mover(jogador=1, pino=1, passos=1)

    with pytest.raises(CasaOcupada):
        tabuleiro.mover(jogador=2, pino=1, passos=1)

def test_nao_entra_no_podio_com_pinos_ainda_na_base():
    tabuleiro = Tabuleiro()
    tabuleiro.mover(jogador=1, pino=1, passos=6)

    with pytest.raises(JogadorAindaTemPinosNaBase):
        tabuleiro.mover(jogador=1, pino=1, passos=31)

def test_nao_entra_no_podio():
    tabuleiro = Tabuleiro()

    for pino in tabuleiro._PINOS:
        tabuleiro.mover(jogador=1, pino=pino, passos=6)
        tabuleiro.mover(jogador=1, pino=pino, passos=pino)

    with pytest.raises(PinoPassouDoPodio):
        tabuleiro.mover(jogador=1, pino=1, passos=31)

def test_pino_entra_no_podio():
    tabuleiro = Tabuleiro()

    for pino in tabuleiro._PINOS:
        tabuleiro.mover(jogador=1, pino=pino, passos=6)
        tabuleiro.mover(jogador=1, pino=pino, passos=pino)

    tabuleiro.mover(jogador=1, pino=1, passos=30)

    assert tabuleiro.posicao(jogador=1, pino=1) == tabuleiro._PODIO

def test_jogador_tem_pino_na_base():
    tabuleiro = Tabuleiro()
    assert tabuleiro._tem_pinos_na_base(jogador=1)

def test_jogador_nao_tem_pino_na_base():
    tabuleiro = Tabuleiro()

    for pino in tabuleiro._PINOS:
        tabuleiro.mover(jogador=1, pino=pino, passos=6)
        tabuleiro.mover(jogador=1, pino=pino, passos=pino)

    assert not tabuleiro._tem_pinos_na_base(jogador=1)
