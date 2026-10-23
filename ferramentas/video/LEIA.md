# Biblioteca de vídeo da pós

Peças, fundos e receitas para editar as aulas e os Reels da pós com o Chip Editor (EDIT IA PRO), no padrão
testado em outubro de 2026. O Chip em si não fica aqui: ele é instalado no computador pelo instalador do EDIT
IA PRO, e a licença dele não permite redistribuir.

Guia completo de recursos e prompts: [Chip Editor · Recursos e prompts para as aulas da pós](https://claude.ai/artifact/3aWpjwidXPH8cgErbgA3SN).

## Como usar

O jeito mais simples: mande o vídeo (e o PowerPoint, se tiver) e diga "edita". A skill
[`diretor-de-edicao-pos`](../../.claude/skills/diretor-de-edicao-pos/SKILL.md) analisa o material, escolhe a
receita do manual, conta a decisão em poucas linhas e manda o Chip fazer.

Para pedir uma peça específica, numa conversa nova do Claude Code com o Chip instalado, peça pelo nome e aponte
esta pasta:

> Edita a aula da pasta [PASTA] em 16:9 no formato janela lateral. Usa as cenas da biblioteca da pós
> (`ferramentas/video/cenas` do repositório do curso): etiqueta de nome no começo e janela lateral nos
> trechos de lista.

O Claude copia a cena para `compositions/cenas/` do projeto do vídeo e liga no `projeto.json`, em
`cenas_proprias` (os exemplos em `exemplos/` mostram como).

## O que tem aqui

| Arquivo | O que é | Onde já foi usado |
|---|---|---|
| [`cenas/pos_etiqueta_nome.html`](cenas/pos_etiqueta_nome.html) | Etiqueta de nome (lower third): barra azul, "Dr. Fausto Farias", @ e a pós | Demo da janela lateral, 00:00 |
| [`cenas/pos_janela_lateral.html`](cenas/pos_janela_lateral.html) | Formato estúdio: barra de etapas, linha pequena, título e tópicos em cartões com check, ao lado da moldura | Demo da janela lateral, 00:07 |
| [`cenas/pos_palavras_fundo.html`](cenas/pos_palavras_fundo.html) | Palavras da fala com contorno, flutuando nas faixas livres em volta da moldura (9:16) | Reels do PRP, 00:01 a 00:09 |
| [`cenas/pos_palavras_laterais.html`](cenas/pos_palavras_laterais.html) | Duas palavras verticais transparentes nas laterais, em tela cheia (9:16) | Reels do PRP, 00:09 a 00:11 |
| [`fundos/fundo_estudio_fausto.png`](fundos/fundo_estudio_fausto.png) | Foto do estúdio (prateleiras, campo tático, anatomia), 1920x1080 | Aula com troca de fundo, versão A |
| [`fundos/fundo_azul_estudio.png`](fundos/fundo_azul_estudio.png) | Fundo azul-marinho de estúdio com brilho e grade de pontos | Aula com troca de fundo, versão B |
| [`scripts/fundo_azul.py`](scripts/fundo_azul.py) | Gera o fundo azul-marinho de novo (troque as cores no topo) | — |
| [`scripts/trocar_fundo_shorts.py`](scripts/trocar_fundo_shorts.py) | Troca o fundo do vídeo em pé por uma foto de cenário, em escala natural, com a mesa na frente como balcão | Shorts do Legacy (padrão aprovado) |
| [`scripts/itens_ao_lado_do_rosto.py`](scripts/itens_ao_lado_do_rosto.py) | Gera as cenas dos itens que aparecem ao lado do rosto quando a fala cita cada um (cartão escuro, fio dourado, selo ✓ ✕ ? ≈) e o nome do produto no fim | Shorts do Legacy, notas de topo, coração e fundo |
| [`scripts/cenas_reels_classudo.py`](scripts/cenas_reels_classudo.py) | Gera as cenas do Reels classudo da profissão: frases em Playfair com dourado, passo a passo com ícones de traço, listas com selo, documento oficial, placa de nome e fecho com assinatura | Reels "PRP funciona?" no auditório |
| [`exemplos/*.projeto.json`](exemplos) | O `projeto.json` de cada vídeo aprovado: blocos, peças, cenas e sons | Janela lateral, fundo trocado com slides, Reels, Shorts do Legacy, Reels classudo do PRP |

As cenas usam os textos que estão no topo de cada arquivo (nomes dos tópicos, palavras, etapas). Para outra
aula, troque esses textos pelos do slide e as palavras de tempo (`em("faixas", ...)`) pelas da fala.

## Padrão da pós

| Item | Aula | Reels |
|---|---|---|
| Formato | 16:9 | 9:16 |
| Estilo do Chip | `noite` (azul-marinho) | `dourado` (receita abaixo; o `laranja` saiu: "cara de Claude") |
| Legenda | `discreta`, sai na moldura | `padrao` (grande) |
| Som | clique ou tique discreto; whoosh em -19 dB; sem trilha | efeitos do plano do Chip |
| Fundo | real do estúdio, ou a foto do estúdio com a pessoa recortada | foto de cenário com a pessoa recortada em escala natural, ou o real |
| Enquadramento | — | tela cheia o vídeo todo, sem moldura nem quadriculado; zoom 1,15 e 1,25 alternando |
| Fim | slide final em tela cheia | produto/review: medidor com a agulha no veredito (a marca), zoom no produto e o nome dele; Reels da profissão: frase final em tipografia e assinatura, sem medidor |

## Padrão do Reels/Shorts (aprovado em 23/10/2026, Shorts do Legacy)

Ele aprovou com "ficou perfeito" e pediu para valer em todo vídeo, mesmo com outro cenário. Exemplo completo:
[`exemplos/shorts-produto-legacy.projeto.json`](exemplos/shorts-produto-legacy.projeto.json).

1. **Fundo trocado em escala natural.** Recorte do vídeo inteiro (`pessoa_recortada.py --saida ... --crf 12`) e
   `scripts/trocar_fundo_shorts.py` com a foto do cenário. A foto cobre 71% da altura da tela, de cima (`--cobre
   0.71`): os objetos do cenário ficam pequenos perto dele (um frasco na prateleira com uns 1/3 da altura da
   cabeça). Com a foto enchendo a altura (escala 2,04 numa foto de 1672x941) o cenário ficou grande demais. A parte
   com menos coisa da foto fica atrás da cabeça (`--centro-x`), desfoque 4, luz e cor quentes na pessoa. A mesa da
   gravação fica na frente, como balcão (a borda é achada sozinha). Aponte o `"edit"` do projeto para a pasta nova.
2. **Câmera.** Só `tela_cheia`, sem moldura e sem papel quadriculado. Zoom de base 1,15 nos trechos abertos e
   1,25 nos outros, alternando nas trocas de tomada (com 1,0 ele ficou pequeno na imagem aberta). Aproximação no
   rosto (`zooms` sem `caixa`, `escala` 1,42) nas frases fortes ("sensacional", "que cheiro bom", "muito
   elegante"); zoom no produto (`zooms` com `caixa`, `escala` 1,45 a 1,6) quando ele mostra o rótulo, sem legenda
   nesse bloco (`"legenda": false`) para não cobrir o rótulo.
3. **Itens citados ao lado do rosto** (`scripts/itens_ao_lado_do_rosto.py`): cada item entra na palavra, ganha o
   selo e a frase dele, e some. Sem zoom no rosto enquanto os cartões estão na tela.
4. **Peças do Chip** (lettering, rótulo, carimbo) no estilo `dourado`: gancho com a palavra atrás da pessoa
   (`atras_da_pessoa`, topo) e o lettering no peito; carimbo verde para elogio, vermelho para "não é jabá".
5. **Medidor no fim dos vídeos de produto e review: é a marca.** O `k2d_medidor` do kit 2D com a pergunta do
   vídeo no rótulo e a agulha indo para o veredito dele na palavra em que ele diz (parâmetros abaixo). Rótulo e
   veredito só com as palavras dele; se a fala não tiver veredito, pergunte qual é antes de pôr o medidor. No
   Reels da profissão em tom sério ele não entra ("o medidor aí não cabe nesse estilo de vídeo"): veja "Reels
   classudo da profissão", abaixo.
6. **Fecho:** "Vale a pena" (ou a frase final dele) em lettering, depois zoom no produto com o nome em Playfair
   dourado embaixo (cena `fim_legacy` do mesmo script) e `segura_fim` 1,5.

**Estilo `dourado`** (acrescente no `ESTILOS` do `build.py` do projeto; só no projeto, o modelo do Chip fica como
está):

```python
'dourado': dict(
    papel='#14110d', linha='#3a3328', base='#d8b46a', destaque='#e2c27e', tinta='#fbfaf7',
    verde='#58c98d', vermelho='#e5484d', contorno_leg='#0b0907', texto_fundo='#fbfaf7', botao='#d8b46a',
    sombra='0 0 0 1.5px rgba(226,194,126,.7), 0 22px 50px rgba(0,0,0,.55)',
    borda='0 0 0 2px rgba(226,194,126,.75), 0 0 36px 2px rgba(226,194,126,.22), 0 40px 110px rgba(0,0,0,.6)',
    fundo='background-color:#0e0c09;background-image:radial-gradient(90% 45% at 50% 22%,rgba(226,194,126,.16),rgba(0,0,0,0) 72%)',
    sobre_destaque='#1a1307', sobre_base='#1a1307', sobre_verde='#06210f', sobre_vermelho='#ffffff',
    carimbo_fundo='rgba(14,12,9,.92)', cel_aro='#3a3328', cel_corpo='#0b0907', item='#201b15',
    polaroide='#14110d', hud_fundo='rgba(10,9,7,.88)', hud_borda='#3a3328', hud_n='#e2c27e', hud_tc='#9d968a',
    texto_atras='#fbfaf7', marca_texto='#e2c27e', cena_no_fundo_do_estilo=False),
```

Fontes: Montserrat nas peças do Chip; Playfair Display (Google Fonts, OFL) nos nomes dos cartões e no nome do
produto, em `assets/fontes/PlayfairDisplay.ttf`.

## Reels classudo da profissão (23/10/2026, Reels "PRP funciona?" no auditório)

Para vídeo de medicina em tom sério. Receita completa na skill (`receitas.md` › Reels › 7); exemplo em
[`exemplos/reels-classudo-prp.projeto.json`](exemplos/reels-classudo-prp.projeto.json) e cenas com
[`scripts/cenas_reels_classudo.py`](scripts/cenas_reels_classudo.py).

- Fundo real com autoridade (o auditório) e cor de cinema no `cut.mp4` e no recorte da pessoa:
  `huesaturation=colors=r+y:saturation=-0.35:strength=1.4,eq=contrast=1.07:saturation=0.92:gamma=0.97:brightness=-0.02,colorbalance=rs=0.015:bs=-0.025:rm=0.02:bm=-0.02:rh=0.015:bh=-0.03,vignette=angle=PI/4.6`
- Selfie andando: `"acompanhar": true` nos blocos, zoom 1,08/1,16 (1,04 onde ele chega o celular perto).
- Texto no peito em Playfair (dourado itálico na palavra principal), faixa escura suave atrás, legenda
  `discreta` escondida enquanto há texto.
- Fecho em tipografia e assinatura "Dr. Fausto Farias · Medicina do Esporte". Sem medidor: "o medidor aí não cabe
  nesse estilo de vídeo".

## Receitas que resolveram problemas nos testes

**Webcam com chiado e eco** (antes do corte, na fonte; mediu de "ruído forte" para "limpo"):

```
ffmpeg -i fonte.mp4 -c:v copy -af "aresample=48000,highpass=f=90:p=2,asendcmd=c='0.0 afftdn sn start; 0.9 afftdn sn stop',afftdn=nr=24:nf=-58,equalizer=f=300:t=q:w=1.2:g=-3" -c:a aac -b:a 192k limpo.mp4
```

O trecho de 0.0 a 0.9 s tem que ser silêncio (só o ruído da sala): troque pelos segundos de uma pausa da
gravação.

**Fundo trocado com cara de falso** (pessoa clara demais, pequena, fundo nítido demais):
1. Refaça o `pessoa.webm` a partir do `cut.mp4` com luz e cor do cenário e um reforço de nitidez, e a máscara
   do `pessoa.webm` original afinada (`erosion,erosion,gblur=sigma=1.2`):
   - fundo quente (foto do estúdio): `eq=brightness=-0.07:contrast=1.06:saturation=0.9:gamma=0.92,colorbalance=rs=0.0:bs=-0.03:rm=0.05:gm=0.01:bm=-0.06:rh=0.03:bh=-0.04,unsharp=5:5:0.9:3:3:0`
   - fundo azul: `eq=brightness=-0.07:contrast=1.06:saturation=0.88:gamma=0.92,colorbalance=rm=-0.01:bm=0.03:bh=0.02,unsharp=5:5:0.9:3:3:0`
   - codificação: `-c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 10 -cpu-used 2 -metadata:s:v:0 alpha_mode=1`
2. Desfoque o fundo: `gblur=sigma=7` na foto do estúdio, `sigma=2.5` no azul.
3. Na tela verde: `"altura": 1.0` com `"posicao": "centro"` e `0.8` com `"direita"`; `"contorno": false`.
4. Sem `segura_fim` quando o vídeo inteiro é tela verde (o quadro parado do fim sai sem a pessoa).

**Imagem embaçada** (compressão demais): renderize com `python3 build.py hf render --crf 12 --output
renders/final.mp4` e passe um reforço leve no arquivo pronto:

```
ffmpeg -i renders/final.mp4 -vf "unsharp=5:5:0.7:3:3:0" -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p -c:a copy -movflags +faststart renders/final_nitido.mp4
```

Depois rode o portão de qualidade do Chip no arquivo novo.

**Gancho do Reels visível no primeiro instante:** o lettering segura a palavra antes de um "não" até o "não"
ser dito. Separe em duas peças: a primeira só com a palavra ("PRP", ou `atras_da_pessoa` com
`"altura": "topo"`), a segunda com "Não substitui".

**Lista no lugar certo com a pessoa recortada à direita:** `"onde": [90, 120]` na `lista_check` (16:9).

**Texto atrás da pessoa com o fundo trocado** (o `atras_da_pessoa` do gancho): refaça o `assets/pessoa.webm` do
trecho com a cor do `cut.mp4` novo e a máscara do recorte inteiro, e anote o trecho no `assets/pessoa.json`
(`"inicio": 0`, `"fim"`: o fim do trecho):

```
ffmpeg -i EDIT_NOVO/cut.mp4 -c:v libvpx-vp9 -i pessoa_inteira.webm -filter_complex "[0:v]trim=0:3.2,setpts=PTS-STARTPTS,format=rgb24[cc];[1:v]trim=0:3.2,setpts=PTS-STARTPTS,format=rgba,alphaextract,erosion,erosion,gblur=sigma=1.2[aa];[cc][aa]alphamerge,format=yuva420p[v]" -map "[v]" -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 10 -cpu-used 2 -row-mt 1 -auto-alt-ref 0 -metadata:s:v:0 alpha_mode=1 -an assets/pessoa.webm
```

## Peças do kit do Chip ajustadas (recriar a partir do Chip instalado)

Estas duas saem de cenas do kit 2D do Chip. Copie a cena do kit no projeto, como o guia do Chip manda, e use
estes parâmetros no `PARAM`:

**Medidor "Pronto para competir?"** (de `k2d_medidor.html`; Reels do PRP, 00:06 a 00:09):

```js
rotulo: "PRONTO PARA COMPETIR?",
zonas: [{ ate: 0.4, cor: "vermelho" }, { ate: 0.7, cor: "destaque" }, { ate: 1, cor: "verde" }],
inicio: 0.62,
acoes: [{ valor: 0.14, leitura: "NÃO PRONTO", em: { palavra: "pronto", padrao: 0.96 } }],
pausa: 0.4,
entrada: 0,
saida: 0,
```

Em trecho curto, troque também `agenda(momento(PARAM.entra, 0), 0.9)` por `0.55`, para a leitura ficar
pelo menos 0,6 s parada antes da moldura abrir.

**Medidor do fim em tela cheia, a marca dos Reels/Shorts** (de `k2d_medidor.html`; Shorts do Legacy, 01:05 a 01:10).
Cartão deitado na altura do peito, rosto livre, legenda escondida no trecho:

```js
rotulo: "É CHEIROSO?",               // a pergunta do vídeo, com as palavras dele
zonas: [{ ate: 0.4, cor: "vermelho" }, { ate: 0.7, cor: "destaque" }, { ate: 1, cor: "verde" }],
inicio: 0.5,                          // a agulha começa no meio: a dúvida
acoes: [{ valor: 0.9, leitura: "MUITO CHEIROSO", em: { palavra: "muito", padrao: 2.13 } }],
pausa: 0.25,
legenda: false,
fundo: null,
area: [90, 1220, 990, 1680],          // 9:16, no peito, abaixo do queixo com o zoom 1,15
entrada: 0,
saida: 0.25,
```

Também: `agenda(momento(PARAM.entra, 0), 0.9)` por `0.55`, e o cartão com fio fino em vez da borda grossa
(`border: ${Math.max(2, 2 * u)}px solid ${C.cores.base}` e `boxShadow: 0 ${12 * u}px 0 -2px rgba(0,0,0,.35)`).
No `projeto.json`: a cena em `cenas_proprias` com `"esconde_legenda": true`, uns 4,7 s (do começo da pergunta até
antes da frase final), bloco sem `zooms` nesse trecho, e um evento `sucesso` no `eventos.json` na palavra do
veredito.

**Pergunta digitando** (de `k2d_comando.html`; demo da janela lateral, 00:23 a 00:28):

```js
texto: "Quanto tempo ele volta?",
inicio: { palavra: "quanto", padrao: 2.04 },
fim: { palavra: "volta", padrao: 2.54 },
envio: { palavra: "diretor", padrao: 3.78 },
selo: null,
rotulo_topo: "o atleta pergunta",
icone: "?",
pausa: 0.25,
```

No 16:9, a raiz da cena leva `data-width="1920" data-height="1080"`.
