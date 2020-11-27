def veloz(posicoes_dos_pinos, passos):
    """
    O jogador veloz primeiro irá retirar todos os pinos 
    da base para então levar todos os pinos para os 
    espaços mais próximos do pódio antes de começar a 
    mover os pinos ao pódio.
    """
    if 0 not in posicoes_dos_pinos:
        return [2, 1, 3, 4]

    ordem = [1, 2, 3, 4]
    posicoes_reordenadas = sorted(posicoes_dos_pinos, key=lambda x: x if x > 0 else 5)
    ordem.sort(key=lambda x: posicoes_reordenadas[x-1])
    
    return ordem

