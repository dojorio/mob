from estrategias import Veloz, prioridade, sacana

import pytest

@pytest.mark.parametrize('pinos, passos, ordem', (
    # com pinos na base
    ((0, 0, 0, 0), 1, [1, 2, 3, 4]),
    # ((1, 0, 0, 0), 1, [2, 3, 4, 1]),
    # ((2, 1, 0, 0), 1, [1, 2, 3, 4]),
    # ((3, 2, 1, 0), 1, [1, 2, 3, 4]),
    # # todos fora da base
    # ((4, 3, 2, 1), 1, [1, 2, 3, 4]),
    # ((3, 4, 2, 1), 1, [2, 1, 3, 4]),
    # ((35, 4, 3, 2), 2, [1, 2, 3, 4]),
    # ((1, 4, 8, 12), 1, [4, 3, 2, 1]),
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
    v = Veloz()
    assert v.veloz(pinos, passos) == ordem