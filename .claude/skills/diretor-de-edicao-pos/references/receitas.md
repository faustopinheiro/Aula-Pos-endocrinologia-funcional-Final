# Receitas de edição da pós

Mesmo conteúdo do manual "Chip Editor · Recursos e prompts para as aulas da pós"
(https://claude.ai/artifact/3aWpjwidXPH8cgErbgA3SN), organizado para a decisão. Cada receita diz o que
fazer; troque os colchetes pelos dados do material.

Sumário: Padrão da pós · Aula (1 a 8) · Reels (1 a 6) · Fala → peça · Efeitos de estúdio · Receitas técnicas ·
Instalar

## Padrão da pós (toda aula)

- Formato 16:9, estilo `noite` (azul-marinho), legenda `discreta` (sai na moldura).
- Ritmo de aula: tira erros, repetições e pausas longas; mantém um respiro curto onde ajuda a entender.
- Tira "tá", "né", "ééé" quando não mudam o sentido. Limpa ruído e eco se o `noise_check` pedir.
- Usa os slides do PowerPoint da pasta: cada slide entra no momento em que ele fala dele.
- Som discreto: clique ou tique quando entra lista, número ou esquema; whoosh em -19 dB; sem trilha.
- Nada inventado. Mostra o corte e uma amostra de 15 s antes do vídeo inteiro.
- Etiqueta de nome (`pos_etiqueta_nome`) na primeira aparição: "Dr. Fausto Farias · Medicina do Esporte ·
  @faustofarias_med · Pós em Ciências do Esporte Aplicadas à Saúde". Esconde a legenda nesse trecho.

Reels: 9:16, estilo `laranja`, legenda `padrao`, efeitos do plano do Chip.

## Aula

**1. Aula padrão com slides.** Abertura com o slide 1 atrás dele e ele no canto direito (tela verde com o slide
como fundo, `altura` 0.55). Cada slide com desenho entra inteiro (`prova` com o PNG do slide) na palavra em que
ele fala dele, e ele volta quando o slide foi explicado. Número importante → contador. Itens listados → lista
com check. Fim: slide de fechamento em tela cheia por 2 s. Slides em PNG: converter o .pptx em PDF e o PDF em
PNG 1920x1080 (LibreOffice + pdftoppm).

**2. Aula com o fundo do estúdio.** Tela verde com a foto do cenário. Antes: teste de 5 s do recorte e mostrar.
Ajuste de luz, cor e nitidez do recorte e fundo desfocado (receitas técnicas, abaixo); ele grande
(`altura` 1.0 no centro, 0.8 à direita), `contorno: false`, sem `segura_fim`. Nos trechos de lista ou esquema,
ele à direita e a peça à esquerda com `"onde": [90, 120]`, legenda desligada nesses blocos.

**3. Aula com esquema que cresce.** Cena `k2d_esquema` do kit do Chip: cada parte entra quando ele fala dela, as
anteriores paradas; no exemplo, acende o caminho; no fim, o esquema inteiro parado 2 s. Amostra com as duas
primeiras partes.

**4. Aula com exames ou telas.** Cada exame em tela cheia (`prova`) com rótulo curto e zoom na região
explicada (`zooms` com `caixa`). Borra nome, data de nascimento e qualquer dado do paciente (`borrar`).
Artigo citado → rótulo com título e ano. Rode o `conferir_dados.py` no arquivo exportado.

**5. Aula com muitos slides.** Slides atrás o tempo todo (tela verde com o slide do momento), ele recortado no
canto inferior direito com o rosto bem visível; se o slide tiver texto embaixo à direita, ele vai para a
esquerda nesse slide.

**6. Abertura de módulo.** Nome do módulo grande atrás dele (`atras_da_pessoa`, `altura` "topo" se o rosto
cobrir). Temas do módulo em lista com check. Fim: cartão "Próxima aula: [TÍTULO]".

**7. Aula longa em vários arquivos.** Junta na ordem do nome, tira tomadas repetidas, mostra o corte inteiro
com a duração de cada bloco antes de qualquer animação. Depois, a receita que o conteúdo pede.

**8. Janela lateral (estilo estúdio/OBS).** Moldura 16:9 (caixa padrão à direita, uns 40% da largura) e a cena
`pos_janela_lateral` no lado livre: barra de etapas no alto (módulo ✓ · aula atual acesa · próxima aula), linha
pequena em caixa alta, título do slide com a parte principal em destaque, tópicos em cartões entrando na palavra
dita com check. Texto direto do PowerPoint (`analisar.py` mostra); slide com desenho entra inteiro no lugar do
texto. A cada 15 a 20 s, volta para ele em tela cheia. Pergunta citada → cena `k2d_comando` digitando com as
palavras da fala (ajustes no LEIA da biblioteca).

## Reels

**1. Achar os melhores trechos** (vídeo longo): liste os 5 trechos de 15 a 40 s com frase de abertura forte e
ideia completa: tempo, frase de abertura e por que prende. Não edite antes de ele escolher, a não ser que ele
tenha dito "decide você".

**2. Reels padrão** (o do PRP, aprovado):
- Corte sem pausas, sem "tá"/"né", sem o vocativo que atrasa o gancho.
- Gancho em duas batidas no primeiro segundo: a palavra principal gigante atrás dele (`atras_da_pessoa`,
  `altura` "topo") e a frase de impacto no peito (`lettering` `posicao` "base"). Separe em duas peças: o
  lettering segura a palavra antes de um "não" até o "não" ser dito.
- Moldura para lista com X ou check (`lista_check`) e medidor (`k2d_medidor`) quando a fala põe algo numa
  escala ("não significa estar pronto").
- Palavras translúcidas da fala em volta da moldura (`pos_palavras_fundo`) e nas laterais em tela cheia
  (`pos_palavras_laterais`), saindo antes do fechamento.
- Fechamento com a frase final grande (`lettering`) e a tela limpa, `segura_fim` 1.2.
- Moldura maior no 9:16: `"moldura": {"caixa": [240, 960, 600, 780]}`.

**3. Lote de ganchos:** 3 versões com aberturas diferentes (pergunta, número, frase polêmica), corpo igual.

**4. Versões:** 4:5 para o feed e 16:9 para o YouTube, sem perder texto (copie o projeto e troque o `formato`).

**5. Série de um módulo:** mesmo visual em todos e um rótulo "Lesão muscular · 1/5" no primeiro segundo.

**6. Copiar estilo:** medir o Reels de referência (`references/referencia-medir.md` do Chip) e mostrar um resumo
de 5 linhas antes de aplicar.

## Fala → peça

| Quando ele diz | Peça |
|---|---|
| Um número que importa ("73 dias", "4 vezes") | contador |
| Uma faixa ou variação ("mais ou menos 60 dias") | medidor ou régua |
| Uma lista ("fortalecimento, reabilitação, acompanhamento") | lista com check (o que tem) ou X (o que não substitui) |
| Etapas, fases, classificação, graus | passo a passo ou esquema que cresce |
| Comparação ("duas semanas boas, seis ruins") | antes e depois |
| Uma pergunta de alguém ("quanto tempo ele volta?") | cartão que digita, ou conversa no celular |
| Mito ou erro comum ("não substitui", "o erro de...") | carimbo vermelho, ou lista com X |
| A frase para o aluno levar ("faixa, nunca ponto", "critério") | lettering grande ou texto atrás da pessoa |
| Um estudo ("Br J Sports Med 2013") | rótulo com a fonte |
| Caso clínico, exame | prova em tela cheia com zoom e borrão |
| Fechamento, próxima aula | slide final e cartão |

## Efeitos de estúdio (referência: vídeo do Rafa Voss)

| Efeito | Como | Situação |
|---|---|---|
| Janela lateral com conteúdo | Aula › 8 | testado |
| Cartão digitando | `k2d_comando` com as palavras da fala | testado |
| Etiqueta de nome | `pos_etiqueta_nome` | testado |
| Palavras espalhadas no cenário, atrás dele | recorte + cena de palavras no fundo (tela verde com o vídeo original de fundo) | falta testar atrás da pessoa |
| Vista em 3 camadas | cena 3D `k3d_explodida` com quadros do vídeo | falta testar |
| Selo de status no canto | peça `hud` | falta testar |

## Receitas técnicas (aplique quando o raio-x mostrar o problema)

**Chiado e eco de webcam** (áudio de 16 kHz, `noise_check` com "ruído forte"): limpe a fonte antes do corte e
use o arquivo limpo no `edl_manual.json`:

```
ffmpeg -i fonte.mp4 -c:v copy -af "aresample=48000,highpass=f=90:p=2,asendcmd=c='INICIO afftdn sn start; FIM afftdn sn stop',afftdn=nr=24:nf=-58,equalizer=f=300:t=q:w=1.2:g=-3" -c:a aac -b:a 192k limpo.mp4
```

INICIO e FIM = uma pausa de verdade da gravação (só o ruído da sala). Meça de novo com o `noise_check`.

**Fundo trocado com cara de falso:** refaça o `pessoa.webm` com a cor do `cut.mp4` e a máscara do recorte
afinada, com luz e cor do cenário e nitidez:

```
ffmpeg -i edit/cut.mp4 -c:v libvpx-vp9 -i assets/pessoa_original.webm -filter_complex "[0:v]format=rgb24,AJUSTE,unsharp=5:5:0.9:3:3:0,format=rgb24[cc];[1:v]format=rgba,alphaextract,erosion,erosion,gblur=sigma=1.2[aa];[cc][aa]alphamerge,format=yuva420p[v]" -map "[v]" -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 10 -cpu-used 2 -row-mt 1 -auto-alt-ref 0 -metadata:s:v:0 alpha_mode=1 assets/pessoa.webm
```

- AJUSTE para cenário quente: `eq=brightness=-0.07:contrast=1.06:saturation=0.9:gamma=0.92,colorbalance=rs=0.0:bs=-0.03:rm=0.05:gm=0.01:bm=-0.06:rh=0.03:bh=-0.04`
- AJUSTE para cenário azul: `eq=brightness=-0.07:contrast=1.06:saturation=0.88:gamma=0.92,colorbalance=rm=-0.01:bm=0.03:bh=0.02`
- Fundo desfocado: `gblur=sigma=7` (foto) ou `2.5` (fundo liso). Confira a transparência (YMIN 0, YMAX 255).

**Imagem embaçada:** `python3 build.py hf render --crf 12 --output renders/final.mp4`, depois
`ffmpeg -i renders/final.mp4 -vf "unsharp=5:5:0.7:3:3:0" -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p -c:a copy -movflags +faststart renders/final_nitido.mp4`
e o portão no arquivo novo.

**Cena própria reprovada no `hf check`:**
- `gsap_cold_seek_hidden_fromto_missing_reveal`: ponha `opacity: 1` também no destino do `fromTo`.
- contraste abaixo de 4.5:1 em texto pequeno: clareie a cor do texto (ex.: `#a9c2ea` em vez de `#6f8fc4`).
- `[cena] uma ação entrou ... depois da palavra`: diminua a `pausa` do kit (0.25).

**Peça que some antes de aparecer:** uma peça cujo começo cai antes do início do bloco é cortada pelo bloco de
antes; comece a peça depois do corte (ex.: primeiro item da lista 0,05 s depois do começo da moldura).

## Instalar

Mac (chip Apple com macOS 13+ ou Intel com macOS 14+) ou Windows 10/11 de 64 bits. No app do Claude, aba Code,
pasta do computador: cole a mensagem de instalação com o link do pacote do EDIT IA PRO; o Claude segue o
INSTALAR. Teste: conversa nova, "Edita o vídeo de teste que está na pasta EDIT-IA-PRO/teste".
