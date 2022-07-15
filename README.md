# Board game

## Execução

Para executar é necessário a instalação [docker](https://www.docker.com/).

### Build
Antes de iniciar o script é necessário fazer o build para criar a imagem no docker a partir do arquivo *Dockerfile*
```bash
docker build -t board .
```
### Start
```bash
docker run board
```

## Proposta
Crie um boad game semelhante a banco imobiliário onde os jogadores se alteram em rodadas definidas aleatóriamente no começo da partida.

## Requisitos
- Cada jogador inicia com 300 de saldo.
- O jogo deve ser composto por 20 propriedades em sequência.
- Cada propriedade tem um custo de venda, um alugel, um proprietário e seguem uma determinada ordem no tabuleiro.
- No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no tabuleiro o jogador vai andar.
- No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no
tabuleiro o jogador vai andar.
- Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da propriedade.
- Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.
- Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda. Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade.
- Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente.
- Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto podem ser compradas por qualquer outro jogador.
- Termina quando restar somente um jogador com saldo positivo, a qualquer momento da partida. Esse jogador é declarado o vencedor.

- Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida com 4 diferentes tipos de possíveis jogadores. Os comportamentos definidos são:

- **Impulsivo:** O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
- **Exigente:** exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
- **Cauteloso:** compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.
- **Aleatório:** compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra.

- O jogador *aleatório* compra a propriedade que ele parar em cima com probabilidade de 50%.
- Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
partida.

## Saída
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes às execuções. Esperamos encontrar nos dados as seguintes informações:

- Quantas partidas terminam portime out (1000 rodadas);
- Quantos turnos em média demora uma partida;
- Qual a porcentagem de vitórias por comportamento dos jogadores;
- Qual o comportamento que mais vence.
