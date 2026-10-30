# Prompts das artes: slot "Andre"

Instruções para o Codex gerar todas as imagens do jogo. O plano completo está em
`docs/PLANO-ANDRE.md`.

## Como usar

1. **Referências.** Anexar sempre as fotos de referência indicadas em cada prompt:
   - `art/referencias/andre.jpg`: cara do Andre (foto a preto e branco);
   - `art/referencias/beat.jpg`: o Beat, o cão.

   Estas fotos não estão no repositório porque ele é público. Têm de ser anexadas à
   mão no Codex ou postas na pasta localmente.
2. **Ordem.** Gerar primeiro as duas folhas de personagem (secção 1). Só depois de
   aprovadas se passa ao resto, e a partir daí **anexa-se a folha aprovada** em vez
   da foto. É isto que mantém a cara igual em todas as imagens.
3. **Montar o prompt.** Cada prompt final é: `[ESTILO]` + o bloco da personagem
   (`[ANDRE]` e/ou `[BEAT]`) quando aparece + o texto do asset.
4. **Formato.** PNG com fundo transparente, salvo quando diz "fundo opaco". Guardar
   no caminho indicado, com o nome exato.
5. **Variações.** Gerar 3 a 4 variações de cada asset e guardar a escolhida. As
   outras podem ir para `art/_rascunhos/`, que não vai para o jogo.
6. **Texto nas imagens.** Só os títulos (logótipo, bónus, escalões de ganho) levam
   texto. Os números, os contadores e as frases das cartas são escritos pelo código.

---

## Blocos reutilizáveis

### [ESTILO]

```
Semi-cartoon caricature illustration for a gritty, adult-humour online slot game.
Thick, uneven black ink outlines; hard cel-shaded shadows; grainy painterly texture
with subtle grime, scratches and worn-paper noise. Slightly exaggerated proportions
(bigger head and hands) but realistic, recognisable facial features. Desaturated
base palette of charcoal, concrete grey, dirty brown and olive, lit by strong neon
accents. Punchy contrast, dramatic rim light, cinematic and professional AAA slot
quality. Dry, sarcastic humour. Not childish, not cute, not glossy 3D, not anime.
No watermark, no signature, no brand logos.
```

### [ANDRE]

```
ANDRE: man in his early 30s, based on the attached reference. Closely shaved
head with a faint dark buzz, short full dark-brown beard trimmed tight along the
jaw, thick straight dark eyebrows, slightly heavy-lidded eyes with a cool,
unimpressed side glance, defined jawline, straight nose. Fair skin. Usual outfit:
black hoodie under a dark jacket. Street look, calm "I know" attitude.
Keep the face consistent with the attached reference in every image.
```

### [BEAT]

```
BEAT: the dog from the attached reference. Pitbull-type dog, mostly white short
coat. A chestnut-brown patch covers the top of the head and runs down over the
ear on the left side of the image; that ear is dark brown, almost black, and
folded. The other ear is white. A large chestnut-brown patch on the shoulder and
chest on the same side. Pale icy grey-blue eyes with pinkish rims, wide black
nose with a pink patch on the bridge and a small grey spot above it. Long
muzzle. Signature expression: a serious, judging, deadpan stare.
Keep the markings exactly the same in every image.
```

### Paleta (para todos)

| Uso | Cor |
|---|---|
| Fundo base | carvão #17141a, betão #3a3a3e |
| Jogo base | magenta néon #ff3d8b para ganhos |
| Vai Tomar Banho | ciano/vapor #3de3ff, azulejo verde-água sujo |
| Vai Trabalhar | azul elétrico #2a7bff, branco de faísca, amarelo de aviso #ffc21a |

---

## 1. Folhas de personagem (primeiro de tudo)

### `art/personagens/andre_folha.png`: 2048×2048, fundo opaco cinzento-claro
Referência: `andre.jpg`

```
[ESTILO] [ANDRE]
Character model sheet on a plain light-grey background. Top row: full body
standing in front view, three-quarter view and side profile, wearing the black
hoodie, dark jacket, dark jeans and worn sneakers. Bottom row: six head close-ups
with expressions: 1 smug side-eye smirk, 2 bored and tired, 3 shocked with eyes
popping, 4 furious shouting, 5 celebrating with mouth wide open, 6 singing with
eyes closed. Same face in every drawing. Clean layout, no text labels.
```

### `art/personagens/beat_folha.png`: 2048×2048, fundo opaco cinzento-claro
Referência: `beat.jpg`

```
[ESTILO] [BEAT]
Character model sheet on a plain light-grey background. Top row: full body
standing side view, sitting front view, lying down asleep. Bottom row: six head
close-ups: 1 deadpan judging stare (signature), 2 barking loud, 3 tongue out
happy, 4 suspicious squint, 5 leaping mid-air, 6 sleeping. Identical markings in
every drawing. Clean layout, no text labels.
```

---

## 2. Símbolos

Todos com **512×512**, fundo transparente, o objeto centrado a ocupar ~85% do
quadrado, com um ligeiro contorno escuro exterior para ler bem por cima dos rolos.
Prefixo comum a juntar a cada um:

```
[ESTILO] Single slot machine symbol, centred, bold silhouette that reads
instantly at small size, transparent background, no frame, no text.
```

### Altos

| Ficheiro | Referência | Prompt |
|---|---|---|
| `art/simbolos/andre.png` | folha do Andre | `[ANDRE] Bust portrait, head slightly tilted, smug side-eye smirk, hood up halfway, gaming headset around his neck, cold blue monitor light on one side of the face and magenta rim light on the other. Premium top symbol: add a thin gold-chrome border ring behind him.` |
| `art/simbolos/unhas.png` | folha do Andre | `Close-up of a man's hand with absurdly long, chunky, slightly dirty fingernails smashing a mechanical keyboard key, motion lines, a few keycaps flying. Magenta neon glow.` |
| `art/simbolos/kebab.png` | nenhuma | `Huge overstuffed kebab wrap in crumpled aluminium foil, dripping white garlic sauce and red chilli sauce, chunks of meat and lettuce falling out, steam rising. Warm orange light.` |
| `art/simbolos/lasanha.png` | nenhuma | `Square slab of lasagna on a small dented metal tray, layers visible, melted cheese stretching, a fork stabbed in the top, steam rising. Warm orange-red light.` |

### Baixos (cartas)

Prefixo extra para os cinco:

```
Graffiti-style playing card letter, thick spray-paint strokes with drips, hard
black outline, painted onto a small chunk of cracked concrete wall. Slight 3D
depth. Exactly one character, nothing else written.
```

| Ficheiro | Cor e pormenor |
|---|---|
| `art/simbolos/a.png` | `The letter "A". Dirty red paint, a bitten kebab-sauce splash on one leg.` |
| `art/simbolos/k.png` | `The letter "K". Electric blue paint, a black electrical cable wrapped around it.` |
| `art/simbolos/q.png` | `The letter "Q". Mustard yellow paint, the tail of the Q is a chip (french fry).` |
| `art/simbolos/j.png` | `The letter "J". Toxic green paint, a strip of black insulating tape across it.` |
| `art/simbolos/10.png` | `The number "10". Purple paint, a crushed energy-drink can leaning on it.` |

### Wild

| Ficheiro | Tamanho | Prompt |
|---|---|---|
| `art/simbolos/beat.png` | 512×512 | `[BEAT] Head and shoulders, signature deadpan judging stare straight at the viewer, spiked black leather collar. Bold chunky graffiti word "WILD" painted across the bottom in white with a magenta outline. Exactly the word WILD, correctly spelled.` |
| `art/simbolos/beat_rolo.png` | 512×1792 (vertical) | `[BEAT] Full body leaping vertically upward through the frame, front paws stretched up, ears flapping, mouth open mid-bark, motion smears and torn-paper edges. Vertical composition that fills a whole slot reel. No text.` |

### Scatters

| Ficheiro | Prompt |
|---|---|
| `art/simbolos/chuveiro.png` | `Chrome shower head on a bent pipe, water bursting out in glowing cyan streams, droplets and steam, a few soap bubbles. Strong cyan neon glow. Feels special and valuable.` |
| `art/simbolos/quadro.png` | `Small open electrical fuse box (breaker panel) with a yellow-black hazard stripe, wires hanging out, a big electric-blue spark arcing between two wires, lightning crackle. Strong electric blue glow. Feels rare and dangerous.` |

---

## 3. O Andre ao PC (peças para animar)

A animação é feita no código, mexendo peças separadas. Primeiro gera-se a cena
completa, que serve de guia. Depois as peças, todas com o **mesmo ângulo, escala e
luz** que a cena, cada uma isolada, fundo transparente, com uma margem extra nas
articulações para as peças se sobreporem.

### Cena-guia

`art/andre_pc/cena_guia.png`: 1536×1536, fundo opaco. Referência: folhas do Andre e do Beat

```
[ESTILO] [ANDRE] [BEAT]
Three-quarter rear-side view of ANDRE slouched in a cheap black gaming chair at a
messy desk in a dark bedroom, face lit blue by a large monitor, one hand on the
mouse, other hand on the keyboard. On the desk: half-eaten kebab in foil, empty
lasagna tray, energy-drink cans, insulating tape, a pair of pliers. BEAT lies
asleep on a blanket next to the chair. Graffiti poster on the wall. The monitor
screen is plain dark (it will be replaced in code). Moody neon magenta and blue
lighting.
```

### Peças

Prefixo comum:

```
[ESTILO] Isolated cut-out puppet piece for 2D skeletal animation, matching the
exact angle, scale and lighting of the attached guide scene. Transparent
background. Include extra overlap at the joint. Nothing else in the image.
```

| Ficheiro | Peça |
|---|---|
| `art/andre_pc/cabeca_neutra.png` | `[ANDRE] Head and neck only, three-quarter rear-side view looking at a monitor, bored focus.` |
| `art/andre_pc/cabeca_contente.png` | `[ANDRE] Same head, same angle, smug grin.` |
| `art/andre_pc/cabeca_furiosa.png` | `[ANDRE] Same head, same angle, furious, teeth showing.` |
| `art/andre_pc/cabeca_festa.png` | `[ANDRE] Same head, same angle, mouth wide open celebrating.` |
| `art/andre_pc/cabeca_desconfiada.png` | `[ANDRE] Same head turned back over the shoulder towards the viewer, suspicious squint.` |
| `art/andre_pc/cabeca_choque.png` | `[ANDRE] Same head, eyes popping, mouth open in shock.` |
| `art/andre_pc/tronco.png` | `Seated torso in black hoodie and dark jacket, no head, no arms.` |
| `art/andre_pc/braco_dir_cima.png`, `braco_dir_baixo.png`, `mao_dir_rato.png` | `Right upper arm / right forearm / right hand holding a gaming mouse, hoodie sleeve.` |
| `art/andre_pc/braco_esq_cima.png`, `braco_esq_baixo.png`, `mao_esq_teclado.png` | `Left upper arm / left forearm / left hand on keyboard keys, long fingernails.` |
| `art/andre_pc/mao_punho.png` | `Right hand clenched in a fist, celebrating.` |
| `art/andre_pc/pernas.png` | `Seated legs in dark jeans and worn sneakers, one knee up.` |
| `art/andre_pc/cadeira.png` | `Cheap black gaming chair, three-quarter rear-side view, empty.` |
| `art/andre_pc/secretaria.png` | `Messy desk with keyboard, kebab, lasagna tray, cans, pliers, tape; monitor frame with an empty transparent screen area.` |
| `art/andre_pc/beat_dorme.png` | `[BEAT] Asleep on a crumpled blanket, same angle as the guide.` |
| `art/andre_pc/beat_ladra.png` | `[BEAT] Same position, head up, barking.` |
| `art/andre_pc/beat_senta.png` | `[BEAT] Same spot, sitting up, deadpan judging stare at the viewer.` |

Os ecrãs do monitor (keno, limbo, blackjack, mines, plinko) são desenhados no
código. Não é preciso gerar imagens deles.

---

## 4. Bónus "VAI TOMAR BANHO!"

| Ficheiro | Tamanho | Referência | Prompt |
|---|---|---|---|
| `art/banho/fundo.jpg` | 1920×1080, opaco | nenhuma | `[ESTILO] Grimy small bathroom: cracked teal tiles, mouldy grout, cheap shower curtain half open, foggy mirror, steam everywhere, cyan neon light. Wide empty centre area for slot reels. No people.` |
| `art/banho/fundo_vertical.jpg` | 1080×1920, opaco | nenhuma | O mesmo prompt, composição vertical, espaço vazio ao centro. |
| `art/banho/andre_banho.png` | 1536×1536 | folha do Andre | `[ESTILO] [ANDRE] Full body in plain dark swim shorts standing under a running shower, covered in soap foam on head and shoulders, eyes closed singing dramatically into a shampoo bottle used as a microphone, water streams and cyan steam. Comedic, non-sexual. Transparent background.` |
| `art/banho/andre_banho_cabeca_a.png`, `_b.png` | 768×768 | folha do Andre | `[ESTILO] [ANDRE] Just his foamy head from the shower scene, same angle: (a) mouth open singing a high note, (b) mouth closed mid-song, eyes shut. Transparent background.` |
| `art/banho/espuma.png` | 1024×1024 | nenhuma | `[ESTILO] Cluster of soap foam and bubbles, white with cyan reflections, transparent background.` |
| `art/banho/vapor.png` | 2048×1024 | nenhuma | `Soft white-cyan steam cloud, semi-transparent, seamless edges, transparent background.` |
| `art/banho/andre_toalha.png` | 1536×1536 | folha do Andre | `[ESTILO] [ANDRE] Waist-up wearing a towel wrapped on his head like a turban and another over the shoulders, smug satisfied face, thumbs up. Transparent background. (End screen.)` |

---

## 5. Super bónus "VAI TRABALHAR!"

| Ficheiro | Tamanho | Referência | Prompt |
|---|---|---|---|
| `art/trabalho/fundo.jpg` | 1920×1080, opaco | nenhuma | `[ESTILO] Dark concrete basement / construction site: exposed cables hanging from the ceiling, flickering work lamp, hazard tape, big open electrical panels on the wall, puddles reflecting electric blue light. Wide empty centre area for slot reels. No people.` |
| `art/trabalho/fundo_vertical.jpg` | 1080×1920, opaco | nenhuma | O mesmo prompt, composição vertical. |
| `art/trabalho/andre_trabalho.png` | 1536×1536 | folha do Andre | `[ESTILO] [ANDRE] Full body as an electrician: hi-vis orange vest over the black hoodie, tool belt with pliers and screwdrivers, white hard hat, insulated gloves, carefully poking a screwdriver into an open electrical panel, tongue out in concentration. Transparent background.` |
| `art/trabalho/andre_choque.png` | 1536×1536 | `andre_trabalho.png` | `[ESTILO] [ANDRE] Exact same pose and framing as the attached image, but being electrocuted: body rigid, eyes popping, beard and eyebrows standing on end, hard hat flying off, bright electric blue arcs wrapping his body. Transparent background.` |
| `art/trabalho/andre_raiox.png` | 1536×1536 | `andre_choque.png` | `Classic cartoon x-ray electrocution frame of the attached image: same pose and silhouette, body turned into a flat glowing blue-white negative with a goofy cartoon skeleton visible inside, hard hat and tools as dark outlines. Transparent background.` |
| `art/trabalho/andre_chamuscado.png` | 1536×1536 | folha do Andre | `[ESTILO] [ANDRE] Waist-up after the shock: face covered in soot, smoke rising from his head, hard hat melted, beard frizzy, dazed proud thumbs up. Transparent background. (End screen.)` |
| `art/trabalho/quadro_grande.png` | 1024×1536 | nenhuma | `[ESTILO] Large open electrical breaker panel with hazard stripes, rows of breakers, tangled wires, one breaker sparking. Transparent background.` |

---

## 6. Fundo do jogo base

| Ficheiro | Tamanho | Prompt |
|---|---|---|
| `art/fundos/base.jpg` | 1920×1080, opaco | `[ESTILO] Dark messy bedroom at night: graffiti-tag poster wall, LED strip glowing magenta along the ceiling, pizza boxes, clothes on the floor, window with city lights. Leave the centre-right empty for slot reels and the left third darker for the animated character. No people.` |
| `art/fundos/base_vertical.jpg` | 1080×1920, opaco | O mesmo, vertical: a parte de cima livre para o Andre ao PC e o centro-baixo para os rolos. |

---

## 7. Interface e títulos

| Ficheiro | Tamanho | Prompt |
|---|---|---|
| `art/ui/logo.png` | 1600×600 | `[ESTILO] Game logo with the single word "ANDRE" in huge chunky graffiti letters, chrome-and-magenta fill, thick black outline, drips, a small lightning bolt through the A and a dog-paw print on the E. Exactly the word ANDRE, correctly spelled. Transparent background.` |
| `art/ui/titulo_banho.png` | 1600×600 | `[ESTILO] Title text "VAI TOMAR BANHO!" in bold graffiti letters, wet cyan glossy fill dripping water, soap bubbles around it, thick black outline. Exact spelling: VAI TOMAR BANHO! Transparent background.` |
| `art/ui/titulo_trabalho.png` | 1600×600 | `[ESTILO] Title text "VAI TRABALHAR!" in bold industrial stencil-graffiti letters, electric blue fill with crackling lightning, hazard stripes behind, thick black outline. Exact spelling: VAI TRABALHAR! Transparent background.` |
| `art/ui/big_win.png` | 1600×500 | `[ESTILO] Title text "BIG WIN" in chunky metallic gold letters with magenta outline and coins bursting. Exact text: BIG WIN. Transparent background.` |
| `art/ui/mega_win.png` | 1600×500 | O mesmo com o texto "MEGA WIN", cromado com fogo magenta e explosão. |
| `art/ui/epic_win.png` | 1600×500 | O mesmo com o texto "EPIC WIN", relâmpagos azuis e estilhaços. |
| `art/ui/andre_win.png` | 1600×700 | `[ESTILO] Title text "ANDRE WIN" in enormous cracked-chrome graffiti letters, the letters shattering the background, fireworks, lightning and a dog-paw print. Exact text: ANDRE WIN. Transparent background.` |
| `art/ui/moldura_rolos.png` | 2048×1536 | `[ESTILO] Slot reel frame: rough dark steel border with rivets, spray-paint tags, hazard tape at the corners and a thin magenta neon tube along the inside edge. Transparent centre for 6 reels. Transparent background.` |
| `art/ui/etiqueta_frase.png` | 1024×384 | `[ESTILO] Blank torn sticker / tape label, slightly crumpled, off-white with black outline, empty, for text to be added later. Transparent background.` |
| `art/ui/multi.png` | 512×512 | `[ESTILO] Empty round badge for a multiplier number: dented steel ring, magenta neon glow, empty centre. Transparent background.` |
| `art/ui/botao_spin.png` | 512×512 | `[ESTILO] Big round slot spin button, dark steel with magenta neon ring and a circular-arrow icon in the middle. No text. Transparent background.` |
| `art/ui/icones.png` | 2048×512 | `[ESTILO] Row of 8 matching game UI icons on transparent background, evenly spaced: turbo lightning bolt, autoplay, plus, minus, info "i", speaker on, speaker off, shopping bag (bonus buy). Same steel-and-neon style, no text.` |

---

## 8. Texturas para partículas e efeitos

Todas pequenas (256×256 ou 512×512), fundo transparente, uma por ficheiro, para o
código multiplicar.

| Ficheiro | Prompt |
|---|---|
| `art/fx/estilhaco_1.png` … `_4.png` | `[ESTILO] Single jagged shard of a shattered painted tile, 4 different shapes, one per image.` |
| `art/fx/moeda.png` | `[ESTILO] Single gold coin with a dog-paw print stamped on it, slight tilt.` |
| `art/fx/faisca.png` | `Single bright electric blue-white spark burst, glowing core, additive-blend friendly, black edges fade to transparent.` |
| `art/fx/raio.png` | `Single jagged electric lightning bolt, blue-white glow, transparent background.` |
| `art/fx/gota.png` | `Single water droplet, cyan highlight.` |
| `art/fx/bolha.png` | `Single soap bubble with rainbow-cyan sheen.` |
| `art/fx/fumo.png` | `Soft grey smoke puff, semi-transparent.` |
| `art/fx/explosao.png` | `[ESTILO] Comic-style explosion burst, magenta and orange with black outline, transparent background.` |
| `art/fx/fogo_artificio.png` | `Single firework burst, gold and magenta sparks, transparent background.` |
| `art/fx/racha.png` | `Screen-crack overlay, white glass cracks radiating from the centre, transparent background.` |

---

## Checklist de aprovação

- [ ] A cara do Andre é reconhecível em todas as imagens.
- [ ] O Beat tem sempre as manchas no mesmo sítio e o olhar sério.
- [ ] Todos os símbolos se percebem bem a 100 px.
- [ ] Os altos distinguem-se claramente dos baixos.
- [ ] O texto dos títulos está bem escrito (VAI TOMAR BANHO!, VAI TRABALHAR!, ANDRE, BIG/MEGA/EPIC/ANDRE WIN).
- [ ] Todas as peças do Andre ao PC têm o mesmo ângulo e escala da cena-guia.
- [ ] Os fundos transparentes estão mesmo transparentes (sem fundo branco ou xadrez desenhado).
