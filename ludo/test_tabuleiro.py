import pytest

from simulador import *


def test_movimenta_pino_no_tabuleiro():
    tabuleiro = Tabuleiro()
    tabuleiro.posiciona('pino', 0)
    tabuleiro.movimenta('pino', 1)
    assert tabuleiro.posicao('pino') == 1

    tabuleiro.posiciona('outro_pino', 0)
    with pytest.raises(CasaOcupada):
        tabuleiro.movimenta('outro_pino', 1)

def test_pino_nao_sai_da_base():
    tabuleiro = Tabuleiro()
    tabuleiro.posiciona('pino', 0)

    with pytest.raises(MovimentoInicialInvalido):
        tabuleiro.movimenta('pino', 2)

def test_pino_nao_entra_no_podio():
    tabuleiro = Tabuleiro()
    tabuleiro.posiciona('pino', 36)

    with pytest.raises(MovimentoFinalInvalido):
        tabuleiro.movimenta('pino', 2)

def test_pino_nao_entra_no_podio():
    tabuleiro = Tabuleiro()
    tabuleiro.posiciona('pino', 36)
    tabuleiro.posiciona('outro_pino', 0)

    with pytest.raises(TemPinoNaBase):
        tabuleiro.movimenta('pino', 1)