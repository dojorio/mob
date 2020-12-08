from estrategias import Estrategia, veloz, prioridade, sacana

import pytest

@pytest.mark.parametrize('pinos, passos, ordem', (
    # 1  2  3  4
    ((0, 0, 0, 0), 1, [1, 2, 3, 4]),
    ((1, 0, 0, 0), 1, [2, 3, 4, 1]),
    ((2, 0, 0, 0), 1, [2, 3, 4, 1]),
    ((3, 2, 1, 0), 1, [4, 1, 2, 3]),
    # todos fora da base
    ((4, 3, 2, 1), 1, [1, 2, 3, 4]),
    ((6, 3, 2, 1), 1, [2, 3, 1, 4]),
    ((6, 3, 25, 1), 1, [3, 2, 1, 4]),
    ((7, 3, 25, 1), 1, [3, 1, 2, 4]),
    ((7, 3, 25, 1), 3, [2, 3, 1, 4]),
))
def test_estrategia_sacana(pinos, passos, ordem):
    assert sacana(pinos, passos) == ordem

@pytest.mark.parametrize('pinos, passos, ordem', (
    # com pinos na base
    ((0, 0, 0, 0), 1, [1, 2, 3, 4]),
    ((1, 0, 0, 0), 1, [1, 2, 3, 4]),
    ((2, 1, 0, 0), 1, [1, 2, 3, 4]),
    ((3, 2, 1, 0), 1, [1, 2, 3, 4]),
    # todos fora da base
    ((4, 3, 2, 1), 1, [1, 2, 3, 4]),
    ((3, 4, 2, 1), 1, [2, 1, 3, 4]),
    ((35, 4, 3, 2), 2, [1, 2, 3, 4]),
    ((1, 4, 8, 12), 1, [4, 3, 2, 1]),
))
def test_estrategia_prioridade(pinos, passos, ordem):
    assert prioridade(pinos, passos) == ordem


@pytest.mark.parametrize('pinos, passos, ordem', (
    # posicao         #
    ((0, 0, 0, 0), 1, [1, 2, 3, 4]),
    ((1, 0, 0, 0), 1, [2, 3, 4, 1]),
    ((2, 1, 0, 0), 1, [3, 4, 1, 2]),
    ((3, 2, 1, 0), 1, [4, 1, 2, 3]),
    
    ((4, 3, 2, 1), 1, [1, 2, 3, 4]),
    ((3, 4, 2, 1), 1, [2, 1, 3, 4]),
    ((35, 4, 3, 2), 1, [2, 3, 4, 1]),
    ((35, 36, 3, 2), 1, [3, 4, 1, 2]),
    ((35, 36, 33, 34), 1, [2, 1, 4, 3]),
))
def test_estrategia_veloz(pinos, passos, ordem):
    assert veloz(pinos, passos) == ordem

@pytest.mark.parametrize('posicoes, ordenador', (
    ((4, 3, 2, 1), [-4, -3, -2, 1]),
    ((6, 3, 2, 1), [0, -3, -2, 1]),
))
def test_mantem_bloqueio(posicoes, ordenador):
    lista = []
    s = Estrategia.Sacana()
    s.posicoes_dos_pinos = posicoes
    for pino, posicao in enumerate(posicoes, start=1):
        lista.append(s.manter_bloqueio(pino))
    assert ordenador == lista