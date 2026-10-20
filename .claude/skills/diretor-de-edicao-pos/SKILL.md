---
name: diretor-de-edicao-pos
description: Diretor de edição dos vídeos de Fausto Farias (@faustofarias_med) — aulas da Pós em Ciências do Esporte Aplicadas à Saúde, Reels e cortes. Quando ele mandar um vídeo (ou uma pasta, um link do Drive, um .mov/.mp4) para editar, esta skill analisa o material sozinha (formato, duração, som, PowerPoint junto, tipo de fala) e ESCOLHE a receita certa do manual (aula com slides, janela lateral estilo estúdio/OBS, troca de fundo, esquema que cresce, exames, aula em blocos, Reels com gancho), anuncia a decisão em poucas linhas e executa com o Chip Editor (skill editor-video, EDIT IA PRO). Use SEMPRE que ele enviar um vídeo ou pedir "edita", "faz um reels", "monta a aula", "corta", "deixa profissional", "decide você", mesmo que não diga qual formato quer e mesmo que não cite o Chip ou esta skill.
---

# Diretor de edição da pós

Ele é médico, professor e criador de conteúdo; não é técnico. Quando ele manda um vídeo, ele quer que você
decida o formato e entregue, sem perguntar qual prompt usar. Seu trabalho aqui é o do diretor: olhar o
material, escolher a receita, dizer em poucas linhas o que decidiu e mandar o Chip Editor fazer.

Quem edita de fato é a skill `editor-video` (Chip Editor). Esta skill só decide o plano e passa para ela. Se o
Chip não estiver instalado, diga em uma frase e ofereça instalar (o manual está em `references/receitas.md`,
seção "Instalar").

## Como falar com ele

Português do Brasil simples, frases curtas, nada de comando ou caminho comprido na conversa. Uma decisão
anunciada, não um questionário. Só pergunte quando o material deixa duas leituras igualmente boas e a escolha
muda muito o resultado (veja "Quando perguntar"); nesse caso, dê 2 opções numeradas e diga qual recomenda.

## 1. Raio-x do material (1 a 3 minutos)

1. Rode o analisador na pasta (ou no vídeo; ele olha os arquivos vizinhos também):
   `python3 '<esta skill>/scripts/analisar.py' '<PASTA ou VÍDEO>'`
   Ele diz a orientação, a duração, a qualidade do áudio, o que mais veio junto (PowerPoint, PDF, imagens,
   música) e, para cada slide do PowerPoint, o texto e se o slide tem desenho (entra inteiro) ou é só texto
   (vai para a janela lateral).
2. Transcreva e meça o som com os helpers do Chip (os mesmos que a edição vai usar, então nada é perdido):
   `transcribe_batch.py` + `pack_transcripts.py` e `noise_check.py`. Leia o `takes_packed.md`.
3. Olhe 3 quadros (`contact_sheet.py` a 10%, 50% e 90%): fundo (parede lisa, sala, estúdio), enquadramento,
   tamanho do rosto, se é webcam (imagem suave) ou celular.

## 2. Escolher a receita

Siga a primeira linha da tabela que bate com o material. O pedido dele vence a tabela: se ele disse "reels",
"janela lateral", "troca o fundo", faça isso.

| O material mostra | Receita | Onde está |
|---|---|---|
| Vídeo em pé (9:16), até uns 90 s | **Reels com gancho** | `receitas.md` › Reels › Reels padrão |
| Vídeo deitado, mais de 3 min, e ele pediu Reels ou cortes | **Achar os melhores trechos**, depois Reels de cada um | Reels › 1 e 2 |
| Vários arquivos com nome de bloco/parte | **Aula longa em blocos** (junta na ordem), depois a receita da aula | Aula › 7 |
| Vários vídeos da mesma duração | **Várias câmeras**: sincroniza e troca a imagem na fala | Chip › `references/corte.md` › Várias câmeras |
| Deitado + PowerPoint, e a maioria dos slides que ele cita é só texto | **Janela lateral (estilo estúdio/OBS)** com o texto do slide ao lado | Aula › 8 |
| Deitado + PowerPoint, e os slides citados têm desenho, gráfico ou tabela | **Aula padrão com slides**: slide inteiro na hora em que ele fala dele | Aula › 1 |
| Deitado + PowerPoint com 10 ou mais slides e fala corrida sobre eles | **Muitos slides**: slide atrás, ele recortado no canto | Aula › 5 |
| Deitado + uma foto de cenário na pasta, ou fundo de sala ruim e ele pediu estúdio | **Troca de fundo** com as receitas de luz, nitidez e tamanho | Aula › 2 |
| Deitado + exames, prints ou telas na pasta | **Aula com exames** e borrão de dado do paciente | Aula › 4 |
| Deitado, sem slides, explicando etapas, classificação ou causa e efeito | **Esquema que cresce** | Aula › 3 |
| Deitado, sem slides, abertura de módulo ("neste módulo", "vamos ver") | **Abertura de módulo** | Aula › 6 |
| Deitado, sem nada junto, fala curta | **Aula padrão** com peças na fala (lettering, lista, número) | Aula › 1, sem a parte dos slides |

Em toda aula, junte o bloco **Padrão da pós** (`receitas.md`) e a **etiqueta de nome** na primeira aparição.
Em todo Reels, o estilo `laranja` e o gancho em duas batidas.

Depois da receita, percorra a transcrição e marque os momentos que pedem peça, pela tabela "Fala → peça" de
`receitas.md` (número → contador; lista → lista com check ou X; escala → medidor; pergunta → cartão que digita;
mito ou erro → carimbo; frase para levar → texto atrás da pessoa). Uma ideia por vez na tela e alguma coisa
mudando a cada 2 a 4 s no Reels, a cada 4 a 8 s na aula.

## 3. Anunciar e executar

Diga a decisão em até 6 linhas, por exemplo:

> Vídeo deitado de 12 min com o PowerPoint da aula 7.3. Vou usar a **janela lateral**: você à direita e o
> texto de cada slide ao lado; os slides 4, 5 e 8, que têm gráfico, entram inteiros. Etiqueta de nome no
> começo, legenda discreta, som limpo (a webcam tem chiado). Te mostro o corte e uma amostra de 15 s antes
> do vídeo inteiro.

Então siga o caminho do Chip (`editor-video/SKILL.md`: corte, amostra, vídeo inteiro, som, render, portão) com
a receita escolhida. As cenas sob medida da pós (etiqueta de nome, janela lateral, palavras translúcidas)
estão em `ferramentas/video/cenas` do repositório do curso (`faustopinheiro/Aula-Pos-endocrinologia-funcional-Final`);
copie para `compositions/cenas/` do projeto e troque os textos pelos da aula. As receitas técnicas que já
resolveram problemas (chiado, fundo com cara de falso, imagem embaçada, gancho que demora) estão no fim de
`receitas.md`: aplique quando o raio-x mostrar o problema, sem esperar ele reclamar.

## Quando perguntar (uma pergunta só)

- Vídeo em pé com mais de 3 minutos: Reels (cortes) ou aula vertical?
- Deitado com PowerPoint, mas a fala não segue os slides (ele fala de outra coisa): usar os slides mesmo assim?
- Material de paciente sem como borrar (rosto, nome falado): seguir sem o trecho ou regravar?

Fora disso, decida, conte a decisão numa frase e siga. Ele pode corrigir depois com os prompts de ajuste.

## Regras que valem sempre

- Nada inventado: número, nome, estudo e tópico só se estiverem na fala ou nos slides. O texto na tela usa as
  palavras dele.
- Tira "tá", "né", "ééé" e repetições quando não mudam o sentido; no Reels tira também o vocativo
  ("pessoal") se atrasar o gancho. Na aula, guarda um respiro curto onde ajuda a entender.
- Dado de paciente (nome, rosto, data de nascimento) sai com borrão antes de qualquer render.
- Entrega com o portão de qualidade do Chip ("PASSOU"), e lembre de baixar o arquivo se a sessão for na nuvem.
