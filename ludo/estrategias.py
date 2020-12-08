from tabuleiro import Tabuleiro

class Estrategia:
    class _Base:
        ordem = [1, 2, 3, 4]

        def ordenar_pelo_pino_mais_proximo_ao_podio(self, ordem):
            ordem.sort(key=lambda x: self.posicoes_dos_pinos[x-1], reverse=True)
            return ordem

        # tirar_da_base = lambda self, x: x if x > 0 else 5
        def tirar_da_base(self, posicao):
            return posicao if posicao > 0 else 5

        def tirar_da_base_primeiro(self):
            return sorted(self.posicoes_dos_pinos, key=self.tirar_da_base)


    class Prioridade(_Base):
        """
            O jogador prioridade irá levar o pino disponível para 
            mais próximo do pódio antes de retirar outro pino da base.
        """
        def sequencia(self, posicoes_dos_pinos, passos):
            self.posicoes_dos_pinos = posicoes_dos_pinos
            ordem = [1, 2, 3, 4]
            ordem = self.ordenar_pelo_pino_mais_proximo_ao_podio(ordem)
            return ordem

    class Veloz(_Base):
        """
            O jogador veloz primeiro irá retirar todos os pinos 
            da base para então levar todos os pinos para os 
            espaços mais próximos do pódio antes de começar a 
            mover os pinos ao pódio.
        """
        def sequencia(self, posicoes_dos_pinos, passos):
            self.posicoes_dos_pinos = posicoes_dos_pinos

            ordem = [1, 2, 3, 4]
            if Tabuleiro._BASE in posicoes_dos_pinos:
                # ainda tem pino na base, retira um deles
                # posicoes_reordenadas = sorted(posicoes_dos_pinos, key=tirar_da_base)
                ordem.sort(key=lambda x: self.tirar_da_base_primeiro()[x-1])
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

    class Sacana(_Base):
        """
            O jogador sacana primeiro irá retirar todos os pinos 
            da base e deixará um pino no espaço 1 e/ou no espaço 
            6 o máximo de possível, enquanto os outros pinos 
            chegam ao pódio.
        """
        # lambda x: self.posicoes_dos_pinos[x-1] % 6 if x in (1, 6) else -self.posicoes_dos_pinos[x-1]
        def manter_bloqueio(self, pino):
            pp = self.posicoes_dos_pinos[pino-1]
            return pp % 6 if pp in (1, 6) else -pp
        
        def sequencia(self, posicoes_dos_pinos, passos):
            self.posicoes_dos_pinos = posicoes_dos_pinos

            chave_de_ordenacao = lambda x: self.tirar_da_base_primeiro()[x-1]

            if not Tabuleiro._BASE in posicoes_dos_pinos: # (6, 3, 2, 1) => [2, 3, 1, 4]
                                                          #  2  0  1  3
                chave_de_ordenacao = self.manter_bloqueio

            return sorted(self.ordem, key=chave_de_ordenacao)


def veloz(posicoes_dos_pinos, passos):
    return Estrategia.Veloz().sequencia(posicoes_dos_pinos, passos)

def prioridade(posicoes_dos_pinos, passos):
    return Estrategia.Prioridade().sequencia(posicoes_dos_pinos, passos)

def sacana(posicoes_dos_pinos, passos):
    return Estrategia.Sacana().sequencia(posicoes_dos_pinos, passos)