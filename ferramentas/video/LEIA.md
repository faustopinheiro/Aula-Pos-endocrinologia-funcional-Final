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
| [`exemplos/*.projeto.json`](exemplos) | O `projeto.json` de cada vídeo aprovado: blocos, peças, cenas e sons | Janela lateral, fundo trocado com slides, Reels |

As cenas usam os textos que estão no topo de cada arquivo (nomes dos tópicos, palavras, etapas). Para outra
aula, troque esses textos pelos do slide e as palavras de tempo (`em("faixas", ...)`) pelas da fala.

## Padrão da pós

| Item | Aula | Reels |
|---|---|---|
| Formato | 16:9 | 9:16 |
| Estilo do Chip | `noite` (azul-marinho) | `laranja` |
| Legenda | `discreta`, sai na moldura | `padrao` (grande) |
| Som | clique ou tique discreto; whoosh em -19 dB; sem trilha | efeitos do plano do Chip |
| Fundo | real do estúdio, ou a foto do estúdio com a pessoa recortada | o real da gravação |
| Fim | slide final em tela cheia | frase final grande, tela limpa |

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
