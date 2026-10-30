# Plano: slot "Andre"

Estado: **plano, por executar**. Nada do que está aqui foi implementado.

Slot fun com o tema do Andre: eletricista, viciado no PC a jogar jogos de casino,
com o Beat, o cão dele, sempre ao lado. Reaproveita o motor do Candy Riot (Burst Ways, grelha que
cresce, wilds com multiplicador) e muda o tema, os símbolos e os dois bónus.

---

## 1. Conceito

O Andre está sentado ao PC a jogar keno, limbo, blackjack e mines. Os bónus são
alguém fora do ecrã a gritar com ele:

- **"VAI TOMAR BANHO!"**: bónus normal. Ele larga o PC e vai para o chuveiro.
- **"VAI TRABALHAR!"**: super bónus. Veste a farda de eletricista e vai mexer num quadro elétrico.

O Beat, o cão dele (branco com manchas castanhas, orelha castanha), é o wild. Os símbolos de
cartas dizem trocadilhos quando ganham, por exemplo "A dá pena".

---

## 2. Direção de arte

**Estilo:** semi-cartoon, sujo e de alto contraste, ao estilo das slots da Nolimit
City. É caricatura com proporções exageradas mas com um rosto reconhecível, e não
cartoon infantil.

Características que os prompts têm de pedir:

- traço de tinta grosso e irregular, contornos pretos;
- sombras duras e pintura com textura (grão, sujidade, papel gasto);
- paleta dessaturada (cinzentos, castanhos, verde-azeitona) com acentos néon fortes:
  azul elétrico para o super bónus, ciano/vapor para o banho, magenta para vitórias;
- expressões exageradas e humor seco;
- ambiente urbano: grafitis, quarto desarrumado, luz de ecrã na cara.

**Regra para o Codex:** não usar nomes de estúdios, jogos ou marcas nos prompts de
imagem. Descrever sempre o estilo pelas características acima. Nada de logótipos da
Stake ou de outros casinos no ecrã do PC: os jogos aparecem com nomes genéricos
(KENO, LIMBO, BLACKJACK, MINES, PLINKO).

### Referências

| Ficheiro | O que é | Usar para |
|---|---|---|
| `art/referencias/andre.jpg` | Selfie a preto e branco: cabeça rapada, barba curta, sobrancelhas marcadas, olhar de lado, hoodie escuro, grafitis atrás | cara e estilo de roupa do Andre |
| `art/referencias/beat.jpg` | O Beat: cão tipo pitbull, branco com manchas castanhas, orelha esquerda castanha-escura, olhos claros, nariz rosado com mancha | wild |
| `art/referencias/andre-calcoes.jpg` | **Opcional.** Foto de calções de banho | cena do banho |

As fotos **não** estão no repositório. É preciso pô-las em `art/referencias/` antes
de o Codex começar. Ver as notas na secção 8 antes de as pôr num repositório público.

A foto de calções de banho não é obrigatória: o modelo de imagem consegue gerar o
corpo a partir da cara. A foto só ajuda se quiserem o corpo parecido com o real.

### Ordem de produção das artes

1. **Folha de personagem do Andre** (frente, 3/4, perfil, 6 expressões). Fica
   aprovada antes de tudo o resto e serve de referência para todas as outras imagens.
2. **Folha de personagem do Beat.**
3. Símbolos.
4. Cenas e animações.
5. Fundos, logótipo e interface.

Gerar primeiro a folha de personagem é o que mantém o Andre parecido de imagem para
imagem. Sem isso, cada símbolo sai com uma cara diferente.

---

## 3. Símbolos

Os 6 rolos e as vias mantêm-se como no Candy Riot. Ficam 4 altos, 5 baixos, o wild
e 2 scatters.

| ID | Símbolo | Tipo | Descrição para a arte |
|---|---|---|---|
| `andre` | Andre | alto 1 | Busto do Andre a sorrir de lado, hoodie, auscultadores ao pescoço |
| `unhas` | Unhas grandes | alto 2 | Mão com unhas compridas e sujas a bater no teclado |
| `kebab` | Kebab | alto 3 | Kebab enorme a pingar molho, papel de alumínio amarrotado |
| `lasanha` | Lasanha | alto 4 | Tabuleiro de lasanha a fumegar, queijo a escorrer, garfo espetado |
| `a` `k` `q` `j` `10` | Cartas | baixos | Letras grossas pintadas tipo grafiti, cada uma com um pormenor do quarto (cabo elétrico, migalhas, fita isoladora) |
| `beat` | Beat (o cão) | wild | Cabeça do Beat com o olhar sério da foto e a palavra WILD; ao alargar, o Beat salta e enche o rolo inteiro |
| `chuveiro` | Chuveiro | scatter do bónus | Chuveiro cromado a pingar, vapor néon ciano |
| `quadro` | Quadro elétrico | scatter do super bónus | Quadro elétrico aberto com faíscas azuis e fios soltos |

### Frases quando os símbolos baixos ganham

Quando um símbolo de carta faz parte de um ganho, aparece um balão com a frase e
pode haver uma voz curta. São sugestões para o teu irmão escolher ou trocar:

| Carta | Frase |
|---|---|
| A | "A dá pena" |
| K | "K cena!" |
| Q | "Q fome..." |
| J | "J tá!" |
| 10 | "10 graça" |

Os símbolos altos também podem ter falas curtas, por exemplo o Andre a dizer
"Sou eu!". Fica em aberto.

---

## 4. O Andre ao PC (personagem animada ao lado dos rolos)

Fica sempre visível enquanto se joga:

- **Computador (horizontal):** à esquerda dos rolos, sentado de costas meio de lado,
  com o monitor visível.
- **Telemóvel (vertical):** numa faixa por cima dos rolos.

O monitor dele vai mudando entre KENO, LIMBO, BLACKJACK, MINES e PLINKO. Cada jogo
tem uma animação curta e em loop no ecrã: bolas de keno a sair, o número do limbo a
subir e a rebentar, cartas a virar, uma bomba no mines.

### Estados da animação

| Estado | Quando | Animação |
|---|---|---|
| `idle` | sempre | A jogar: clica, abana a perna, come kebab; o Beat dorme ao lado |
| `ganho_pequeno` | ganho < 5x | Acena com a cabeça, "boa" |
| `ganho_grande` | ganho ≥ 20x | Levanta-se, braços no ar; o Beat ladra |
| `seca` | 10 jogadas seguidas sem ganho | Mão na cara, bate no teclado |
| `quase_bonus` | 2 chuveiros na grelha | Olha para trás desconfiado |
| `grito_banho` | entrada no bónus | Ouve "VAI TOMAR BANHO!", revira os olhos e levanta-se |
| `grito_trabalho` | entrada no super bónus | Ouve "VAI TRABALHAR!", cai da cadeira |

### Como animar (decisão técnica importante)

Os modelos de imagem não conseguem gerar muitos frames seguidos com a mesma cara e
o mesmo corpo. Fazer a animação frame a frame com IA dá um boneco que "treme".

Proposta: o Codex gera o Andre **em peças separadas**, com fundo transparente, e a
animação é feita no código, rodando e deslocando as peças. As peças são cabeça (com
3 a 4 expressões), tronco, braço e antebraço de cada lado, mãos, perna e cadeira.
É assim que se fazem muitas slots.

- Ferramenta: PixiJS com tweens simples (ou Spine, se alguém tiver licença).
- O ecrã do PC é um elemento à parte, por isso os minijogos podem ser animados
  diretamente em código.

---

## 5. Os bónus

### Disparo

| Na grelha, no fim das cascatas | Resultado |
|---|---|
| 3 chuveiros | Vai Tomar Banho, 10 rodadas |
| 4 / 5 / 6 chuveiros | Vai Tomar Banho, 12 / 15 / 20 rodadas |
| 3 quadros elétricos | Vai Trabalhar, 10 rodadas |
| 4 / 5 / 6 quadros elétricos | Vai Trabalhar, 12 / 15 / 20 rodadas |

O quadro elétrico é bastante mais raro do que o chuveiro. Os dois contam em
separado: chuveiros e quadros não se somam. Se na mesma jogada houver 3 chuveiros e
3 quadros, ganha o super bónus.

### "VAI TOMAR BANHO!" (bónus normal)

- Começa com multiplicador global **x1**, que nunca desce durante o bónus.
- Cada chuveiro que cai durante o bónus:
  1. o Andre aparece no chuveiro a tomar banho (calções de banho, espuma, a cantar
     ao chuveiro);
  2. o multiplicador sobe **+1**;
  3. o chuveiro conta para dar mais rodadas: 3 de uma vez dão +3.
- A grelha não encolhe entre rodadas, como no Candy Riot.
- Ecrã de entrada: casa de banho com azulejos rachados, vapor ciano.
- Ecrã final: o Andre de toalha na cabeça com o total ganho.

### "VAI TRABALHAR!" (super bónus)

- O mesmo esquema, mas o Andre está com farda de eletricista (colete refletor,
  cinto de ferramentas, capacete) a mexer num quadro elétrico.
- Começa sem multiplicador (x1).
- Cada vez que cai um quadro elétrico, ele leva um choque: flash azul e raio-X com
  o esqueleto à vista, ao estilo dos desenhos animados, cabelo (o pouco que tem) em pé.
  O multiplicador sobe de 5 em 5: **x5 → x10 → x15 → x20...** e nunca desce.
- 3 quadros de uma vez dão também +3 rodadas.
- Durante este bónus não caem chuveiros.
- Fundo: obra, cave com luz a piscar, cabos pendurados.
- Ecrã final: o Andre chamuscado, a fumegar, com o total ganho.

### Compra de bónus

| Opção | Custo previsto |
|---|---|
| Comprar "Vai Tomar Banho" | ~100x |
| Comprar "Vai Trabalhar" | ~400x |

Os custos finais saem da simulação, com o RTP-alvo de 96% para cada opção.

---

## 6. Matemática

Partir de `math/engine.py` e `math/config.json`. Alterações:

1. Novos IDs de símbolos (secção 3) e um segundo scatter (`quadro`), mais raro
   do que o chuveiro e contado em separado.
2. Dois modos de rodadas grátis, `banho` e `trabalho`, cada um com pesos próprios.
3. Multiplicador global por modo: valor inicial, quanto sobe por cada scatter e
   máximo opcional.
4. Os scatters que caem durante o bónus contam ao longo de todas as cascatas e
   aumentam o multiplicador no momento em que caem, não só no fim.
5. Novos eventos para a animação: `shower_hit`, `shock_hit` e `mult_change`.
6. Dois modos de compra de bónus em `simulate.py` e `tune.py`.
7. Metas:

| | Meta |
|---|---|
| RTP | 96% no jogo base e em cada compra de bónus |
| Vai Tomar Banho | 1 em ~250 jogadas |
| Vai Trabalhar | 1 em ~1500 jogadas |
| Ganho máximo | 10 000x (pode subir para 25 000x por causa do super bónus) |
| Volatilidade | alta |

8. Correr mais de 20 milhões de jogadas e confirmar que a versão JS dá os mesmos
   números que a de Python.

Aviso: o multiplicador global que só sobe, juntamente com uma grelha que só cresce,
dispara a volatilidade. Vai ser preciso afinar com cuidado o peso do chuveiro e do
quadro durante os bónus.

---

## 7. Frontend, apresentação e som

### Apresentação profissional

O jogo tem de parecer uma slot de estúdio. Regras:

- **Nenhum texto explicativo no ecrã de jogo.** Nada de "Carrega em GIRAR", "a
  grelha deixa de encolher", secções "Como funciona" por baixo dos rolos, nem frases
  a explicar o que acabou de acontecer. A demo do Candy Riot tem tudo isto e não
  passa para o novo jogo.
- O ecrã mostra só: o logótipo, os rolos, o Andre, o multiplicador, o saldo, a
  aposta, o ganho e os botões.
- As regras e a tabela de pagamentos ficam num menu ⓘ, num painel próprio com o
  estilo do jogo, como nas slots reais.
- Os bónus anunciam-se só com o título ("VAI TOMAR BANHO!") e o número de rodadas,
  com o grito em áudio. Não há legendas a explicar.
- Os números sobem a rolar (contadores animados), nunca aparecem de repente.
- Os botões são desenhados para o jogo (spin, turbo, autoplay, aposta, compra de
  bónus, som, ⓘ), com estados de carregado e desativado.
- As frases das cartas ("A dá pena") são parte da animação de ganho: uma etiqueta
  pintada que salta do símbolo e desaparece. Não são balões de texto.

### Animações

Tudo com zoom, tremor e partículas. Por ordem de intensidade:

| Momento | Animação |
|---|---|
| Rolos a girar | Desfoque de movimento, paragem com ressalto, pequeno pó/faísca no impacto |
| Ganho normal | Símbolos vencedores fazem zoom-in, brilho e linha de ligação entre eles; depois **explodem** em estilhaços com a cor do símbolo |
| Cascata | Os novos símbolos caem com peso; o rolo que cresce estica-se com um "estalo" e um flash |
| Frase da carta | Etiqueta pintada entra com zoom e rotação ("A dá pena") e sai a desfazer-se |
| Wild do Beat | O Beat salta para o rolo, a câmara faz zoom ao rolo, o multiplicador carimba-se em cima com tremor |
| Antecipação | Com 2 scatters na grelha, os restantes rolos abrandam, a câmara aproxima-se, o fundo escurece e há batimento cardíaco |
| Disparo do bónus | Scatters pulsam e explodem em luz, zoom total à grelha, corte para o grito, transição de ecrã |
| Banho (chuveiro cai) | Zoom ao chuveiro, a cena do Andre no banho ocupa o ecrã por ~1,5 s com vapor e espuma, o multiplicador sobe com salpicos |
| Choque (quadro cai) | Flash branco, ecrã treme, raio-X com o esqueleto, faíscas por cima dos rolos, multiplicador sobe com descarga elétrica |
| Ganhos grandes | Escalões com animações cada vez maiores (ver abaixo) |
| Ganho máximo | Ecrã próprio, fogo de artifício, o Beat a ladrar, o Andre a partir o teclado |

**Escalões de ganho** (texto só com o nome do escalão e o valor):

| Escalão | A partir de | Efeito |
|---|---|---|
| BIG WIN | 15x | Zoom, moedas, contador a rolar |
| MEGA WIN | 50x | + explosões, tremor de ecrã, o Andre levanta-se |
| EPIC WIN | 200x | + câmara lenta, raios, o Beat salta |
| ANDRE WIN | 1000x | + ecrã a "rachar", fogo de artifício, música própria |

Um toque no ecrã salta a animação para o valor final (exigido em qualquer slot séria).

Respeitar a opção de movimento reduzido do sistema: menos tremor e flashes, mas
continua a mostrar tudo.

### Tecnologia

- Passar a demo de HTML/CSS para **PixiJS**: as animações por peças, partículas,
  câmara (zoom e tremor) e flashes precisam disso. Confirmar primeiro na
  documentação do Stake Engine o que o SDK de frontend usa, caso venha a ser
  submetido.
- Disposição:
  - computador: Andre ao PC à esquerda, rolos ao centro, multiplicador e rodadas à direita;
  - telemóvel: Andre por cima, rolos, comandos em baixo.
- Ecrãs de entrada e de fim para cada bónus.
- O Codex tem de gerar também as texturas para as partículas: estilhaços, moedas,
  faíscas, gotas, espuma, fumo.

### Som

Os sons vão para `audio/` no repositório. Formato preferido: `.ogg` ou `.mp3`,
44,1 kHz; os efeitos curtos (até 2 s) cortados sem silêncio no início.

| Ficheiro | Uso |
|---|---|
| `musica_base` | Música do jogo base, em loop |
| `musica_banho` | Música do Vai Tomar Banho, em loop |
| `musica_trabalho` | Música do Vai Trabalhar, em loop |
| `musica_bigwin` | Por baixo dos escalões de ganho |
| `grito_banho` | "VAI TOMAR BANHO!" |
| `grito_trabalho` | "VAI TRABALHAR!" |
| `spin`, `paragem_rolo` | Girar e cada rolo a parar |
| `ganho_pequeno`, `explosao` | Ganho e símbolos a rebentar |
| `cascata` | Símbolos a cair |
| `ladrar` | Wild do Beat |
| `scatter_chuveiro`, `scatter_quadro` | Scatter a cair (um som por rolo, a subir de tom) |
| `antecipacao` | Batimento/tensão com 2 scatters |
| `banho` | Água, e o Andre a cantarolar |
| `choque` | Zumbido e "ZZZT" |
| `multi_sobe` | Multiplicador a subir |
| `contador` | Números a rolar |
| `frase_a`, `frase_k`, ... | Voz das frases das cartas (opcional) |
| `clique` | Botões |

Se faltarem sons, o jogo usa os que existirem e fica calado nos outros. Os que não
houver podem ser gerados ou tirados de bibliotecas livres (com licença que o permita).

---

## 8. Lista de artes para o Codex

Formato: PNG com fundo transparente, salvo indicação em contrário.

| Ficheiro | Tamanho | Conteúdo |
|---|---|---|
| `art/personagens/andre_folha.png` | 2048×2048 | Folha de personagem do Andre: frente, 3/4, perfil, 6 expressões |
| `art/personagens/beat_folha.png` | 2048×2048 | Folha de personagem do Beat |
| `art/simbolos/{andre,unhas,kebab,lasanha}.png` | 512×512 | Altos |
| `art/simbolos/{a,k,q,j,10}.png` | 512×512 | Baixos |
| `art/simbolos/beat.png` + `beat_rolo.png` | 512×512, 512×1792 | Wild normal e wild alargado ao rolo |
| `art/simbolos/{chuveiro,quadro}.png` | 512×512 | Scatters |
| `art/andre_pc/*.png` | variável | Peças do Andre ao PC: cabeça ×4 expressões, tronco, braços, mãos, pernas, cadeira, secretária, monitor vazio |
| `art/banho/*.png` | variável | Peças do Andre no banho (calções), chuveiro, espuma, vapor |
| `art/trabalho/*.png` | variável | Peças do Andre eletricista, versão raio-X do choque, quadro, faíscas |
| `art/fundos/{base,banho,trabalho}.jpg` | 1920×1080 + versão vertical 1080×1920 | Quarto, casa de banho, cave/obra |
| `art/ui/logo.png` | 1600×600 | Logótipo "ANDRE" |
| `art/ui/{vai_tomar_banho,vai_trabalhar}.png` | 1600×600 | Títulos dos bónus |

### Prompt base (em inglês, porque os modelos de imagem respondem melhor)

Juntar a todos os prompts:

```
Semi-cartoon caricature for a gritty adult slot game. Thick uneven black ink
outlines, hard cel shadows, grainy painterly texture, slightly grimy look.
Desaturated palette of greys, browns and olive with strong neon accents.
Exaggerated expressions, dry humour. Not childish, not glossy 3D.
Keep the character's face consistent with the attached character sheet.
No text, no logos, no brand names unless asked. Transparent background.
```

Exemplos:

- **Folha de personagem:** `Character sheet of a man in his early 30s based on the
  attached photo: shaved head, short dark beard, strong eyebrows, side-eye smirk,
  dark hoodie. Front, three-quarter and profile views plus six expressions:
  smug, bored, shocked, furious, celebrating, singing.`
- **Wild:** `The dog from the attached photo: white pitbull-type dog with brown
  patches, dark brown left ear, pale eyes, pink nose with a dark spot, serious
  judging stare. Bust portrait, framed as a slot symbol.`
- **Choque:** `The same man as an electrician in hi-vis vest and tool belt being
  electrocuted, classic cartoon x-ray effect showing his skeleton, electric blue
  glow, sparks, eyes popping.`
- **Banho:** `The same man in plain swim shorts in a cracked-tile shower, covered in
  soap foam, singing into a shampoo bottle, cyan steam, comedic and non-sexual.`

---

## 9. Decisões

| Pergunta | Decisão |
|---|---|
| Multiplicador no choque | Sobe de 5 em 5: x5, x10, x15... |
| Super bónus | 3 quadros elétricos |
| Nome do cão | Beat |
| Comida | Kebab e lasanha (podem entrar outras como variantes da arte) |
| Destino | Só para diversão, por agora: demo privada com créditos fictícios |

Ainda em aberto:

1. **Frases das cartas:** o teu irmão escolhe ou ficam as sugestões?
2. **Nome:** "Andre" ou "André"? Por agora fica "Andre".

### Notas importantes

- **Consentimento:** a cara do Andre é de uma pessoa real. Para a demo entre
  família basta ele estar de acordo. Se um dia for para a Stake ou for publicado,
  é preciso autorização escrita dele, e a Stake pode recusar um jogo a dinheiro real
  com uma pessoa real identificável.
- **Fotos no repositório:** se o repositório for público, não pôr lá as fotos
  originais. Fica só a arte gerada, ou então o repositório passa a privado.

---

## 10. Fases

| Fase | O quê | Quem |
|---|---|---|
| 0 | Fechar as 2 perguntas da secção 9 e pôr as fotos em `art/referencias/` | tu e o teu irmão |
| 1 | Folhas de personagem do Andre e do Beat; aprovação | Codex, depois vocês aprovam |
| 2 | Símbolos, fundos e logótipo | Codex |
| 3 | Peças animáveis (PC, banho, trabalho) e texturas de partículas | Codex |
| 4 | Matemática nova, simulação, RTP 96% | Claude |
| 5 | Frontend PixiJS: rolos, Andre animado, bónus, escalões de ganho, efeitos, som | Claude |
| 6 | Testes no telemóvel e no computador, afinações | todos |
| 7 | (Mais tarde, se quiserem) Adaptar ao SDK do Stake Engine | Claude |

As fases 1 a 3 (artes) e a fase 4 (matemática) podem andar em paralelo.
