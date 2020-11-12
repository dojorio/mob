## Desafio do Ludo

Considere o seguinte jogo hipotético muito semelhante ao Ludo, onde algumas de suas mecânicas foram modificadas simplificadas.

Numa partida desse jogo, os jogadores se alternam em rodadas, numa ordem definida aleatoriamente no começo da partida. Os jogadores sempre começam uma partida com 4 pinos na base de início do jogo.

Nesse jogo, o tabuleiro é composto por 36 espaços em sequência, conectando a base ao pódio. 

A base ocupa a posição 0 e o pódio a posição 37, não há limites para a quantidade de pinos en eses elementos. Com exceção da base e do pódio, cada espaço só poderá ser ocupado por 1 pino. 

No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantos espaços no tabuleiro o jogador poderá andar. O jogador somente poderá andar com um pino da base caso obtenha o valor 1 ou o valor 6. O jogador somente poderá colocar um pino no pódio caso nao tenha nenhum pino na base. Caso não haja ações disponíveis, o jogador perde a vez. 

As ações disponíveis são:
- Retirar um pino da base a um espaço que não esteja ocupado por outro pino;
- Mover um pino a outro espaço que não esteja ocupado por outro pino;
- Mover um pino ao pódio;

Para um dos pinos chegar ao pódio, é necessário tirar o valor exato para que o pino seja movido para o espaço definido como pódio.

Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente.

O jogo termina quando um dos jogadores consegue colocar todos os seus pinos no pódio. Com isso, esse jogador é declarado o vencedor.

Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos de possíveis jogadores.

Os comportamentos definidos são:
- O jogador novato atuará aleatoriamente, testando a possibilidade de retirar um pino da base e de mover um dos pinos que já estejam nos espaços.
- O jogador veloz primeiro irá retirar todos os pinos da base para então levar todos os pinos para os espaços mais próximos do pódio antes de começar a mover os pinos ao pódio.
- O jogador sacana primeiro irá retirar todos os pinos da base e deixará um pino no espaço 1 e/ou no espaço 6 o máximo de possível, enquanto os outros pinos chegam ao pódio.
- O jogador prioridade irá levar o pino disponível para mais próximo do pódio antes de retirar outro pino da base..

Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada com a vitória do jogador que colocou mais pinos no pódio. O critério de desempate é a ordem de turno dos jogadores nesta partida.
