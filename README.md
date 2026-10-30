# Candy Riot

Slot original para o [Stake Engine](https://stake.com/blog/what-is-stake-engine), inspirada no
estilo da Nolimit City (temas sombrios, humor negro, volatilidade alta, multiplicadores agressivos)
e da AvatarUX (grelha que cresce, cores fortes, personagens).

As mecânicas são originais. Não usam nomes nem regras registadas por esses estúdios
(xWays, xNudge, PopWins, etc.).

## Conceito

Uma fábrica de doces numa cidade decadente, à noite. Os trabalhadores revoltaram-se e
a produção descontrolou-se. Os doces são os símbolos baixos e a malta da revolta é a dos altos.

| Símbolo | Tipo |
|---|---|
| 💀 Boss, 🐀 Rat, 🤡 Clown, 😈 Punk | altos |
| 🍮 Jelly, 🍭 Lolly, 🍬 Mint, 🫧 Gum | baixos |
| 💥 Sugar Rush Wild | wild, só nos rolos 2 a 5 |
| 🎟️ Golden Ticket | scatter |

## Mecânicas

- **Burst Ways**: 6 rolos que começam com 3 linhas (729 vias). Os ganhos são em vias,
  da esquerda para a direita, a partir de 3 rolos. Os símbolos vencedores rebentam e
  cada rolo que perdeu símbolos ganha mais uma linha, até 7 (117 649 vias). Caem
  símbolos novos e o processo repete-se enquanto houver ganhos.
- **Shove Wilds**: um wild alarga-se ao rolo inteiro e recebe um multiplicador
  (x2, x3, x5 ou x10). Os multiplicadores dos rolos wild que entram no mesmo ganho
  somam-se. O rolo wild rebenta juntamente com o ganho.
- **Rodadas grátis**: 3/4/5/6 bilhetes no fim das cascatas dão 8/10/12/15 rodadas.
  Nas rodadas grátis a grelha nunca volta às 3 linhas: só cresce. Mais bilhetes dão
  +3/+5/+8/+10 rodadas.
- **Compra de bónus**: 84x a aposta por 8 rodadas grátis.
- **Ganho máximo**: 10 000x.

## Números (simulação)

| | Valor |
|---|---|
| RTP do jogo base | ~96% (12M jogadas em Python e 12M em JS; margem de ±1%) |
| RTP da compra de bónus | ~96% |
| Frequência de ganho | 1 em 2,96 |
| Rodadas grátis | 1 em ~270, média ~87x |
| Parte do RTP nas rodadas grátis | ~33% |
| Volatilidade | alta (desvio padrão ~17) |

A margem de ±1% vem de a volatilidade ser alta. Para submeter o jogo é preciso calcular
o RTP com mais precisão, com o SDK de matemática do Stake Engine ou com simulações muito
maiores.

## Estrutura

```
math/config.json   paytable, pesos dos símbolos, multiplicadores, regras (fonte única)
math/engine.py     lógica do jogo
math/simulate.py   simulação Monte Carlo: RTP, frequência de ganho, ganhos grandes
math/tune.py       mede base vs. rodadas grátis e sugere a escala do paytable
web/engine.js      a mesma lógica em JavaScript, lê o mesmo config.json
web/index.html     demo jogável (créditos fictícios)
```

## Correr

Simulação:

```bash
cd math && python3 simulate.py --spins 1000000
```

```bash
cd math && python3 simulate.py --mode bonus --spins 50000
```

Demo no navegador (a partir da raiz do repositório):

```bash
python3 -m http.server 8000
```

Depois abre http://localhost:8000/web/

## Próximos passos

1. Criar conta no Stake Engine e ler a documentação do SDK de matemática e do frontend.
2. Passar `math/engine.py` para o formato do SDK de matemática deles e gerar os
   resultados e as tabelas que pedem.
3. Trocar os emojis por arte a sério e acrescentar som.
4. Ligar o frontend ao RGS do Stake em vez de usar `Math.random`.
