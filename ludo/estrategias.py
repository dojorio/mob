from tabuleiro import Tabuleiro

def sacana(posicoes_dos_pinos, passos):
    """
        O jogador sacana primeiro irá retirar todos os pinos 
        da base e deixará um pino no espaço 1 e/ou no espaço 
        6 o máximo de possível, enquanto os outros pinos 
        chegam ao pódio.
    """
    return [1, 2, 3, 4]

class Estrategia:
    def ordenar_pelo_pino_mais_proximo_ao_podio(self, ordem):
        ordem.sort(key=lambda x: self.posicoes_dos_pinos[x-1], reverse=True)
        return ordem

class Prioridade(Estrategia):
    def prioridade(self, posicoes_dos_pinos, passos):
        """
            O jogador prioridade irá levar o pino disponível para 
            mais próximo do pódio antes de retirar outro pino da base.
        """
        self.posicoes_dos_pinos = posicoes_dos_pinos
        ordem = [1, 2, 3, 4]
        ordem = self.ordenar_pelo_pino_mais_proximo_ao_podio(ordem)
        return ordem

tirar_da_base = lambda x: x if x > 0 else 5

def tirar_da_base_primeiro(posicoes_dos_pinos):
    return sorted(posicoes_dos_pinos, key=tirar_da_base)

class Veloz(Estrategia):
    def veloz(self, posicoes_dos_pinos, passos):
        """
            O jogador veloz primeiro irá retirar todos os pinos 
            da base para então levar todos os pinos para os 
            espaços mais próximos do pódio antes de começar a 
            mover os pinos ao pódio.
        """
        self.posicoes_dos_pinos = posicoes_dos_pinos

        ordem = [1, 2, 3, 4]
        if Tabuleiro._BASE in posicoes_dos_pinos:
            # ainda tem pino na base, retira um deles
            # posicoes_reordenadas = sorted(posicoes_dos_pinos, key=tirar_da_base)
            ordem.sort(key=lambda x: tirar_da_base_primeiro(posicoes_dos_pinos)[x-1])
        elif self.todos_ou_nenhum_proximo_ao_podio():
            ordem = self.ordenar_pelo_pino_mais_proximo_ao_podio(ordem)
        else:
            ordem.sort(key=lambda x: -posicoes_dos_pinos[x-1] if posicoes_dos_pinos[x-1] < Tabuleiro._PODIO-6 else posicoes_dos_pinos[x-1])
        
        return ordem

    def algum_proximo_ao_podio(self):
        for posicao in self.posicoes_dos_pinos:
            if posicao >= (Tabuleiro._PODIO-6):
                return True
            
    def todos_ou_nenhum_proximo_ao_podio(self):
        return min(self.posicoes_dos_pinos) >= (Tabuleiro._PODIO-6) or not self.algum_proximo_ao_podio()


def prioridade(posicoes_dos_pinos, passos):
    return Prioridade().prioridade(posicoes_dos_pinos, passos)