from estrategias import veloz

import pytest

@pytest.mark.parametrize('pinos, passos, ordem', (
    # posicao         #
    ((0, 0, 0, 0), 1, [1, 2, 3, 4]),
    ((1, 0, 0, 0), 1, [2, 3, 4, 1]),
    ((2, 1, 0, 0), 1, [3, 4, 1, 2]),
    ((3, 2, 1, 0), 1, [4, 1, 2, 3]),
    ((4, 3, 2, 1), 1, [1, 2, 3, 4]),

    # ((3, 4, 2, 1), 1, [2, 1, 3, 4]),
))
def test_estrategia_veloz(pinos, passos, ordem):
    assert veloz(pinos, passos) == ordem