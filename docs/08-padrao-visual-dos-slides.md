# Padrão visual dos slides — Ciências do Esporte Aplicadas à Saúde

**Validado no piloto da aula 6.3** (deck: https://claude.ai/artifact/6zK1qQ51RTTWrQwvEWiZP3).
Todo deck dos 14 módulos segue este padrão até que exista identidade de marca própria.

## Origem do conteúdo

O deck é montado a partir do bloco `## Roteiro Gamma.app` de cada aula, sem reescrita:
mesmos números, mesmas fontes, mesmos negritos de ênfase. As linhas
`*Teleprompter:*` do corpo da aula viram **notas do apresentador** de cada slide.

## Tipografia

- Títulos: **Libre Baskerville** (700) — registro acadêmico/institucional.
- Corpo: **IBM Plex Sans** (400/500/600).
- Escala: 92 (capa) · 60 (título de slide) · 48 (número-destaque) · 40 (título de card) ·
  30 (corpo) · 26 (apoio, eyebrow, legenda) · 24 (rodapé). Nada abaixo de 24.

## Paleta

| Papel | Hex | Uso |
|---|---|---|
| Tinta | `#12202E` | fundo da capa e do fecho, texto sobre claro |
| Papel claro | `#F7F6F2` | fundo padrão dos slides |
| Papel quente | `#EDEAE2` | fundo alternado, dá ritmo ao módulo |
| Card | `#FDFCF9` | superfície de card sobre qualquer fundo |
| Acento 1 (vermelho) | `#A8322A` | eyebrow, doença, alerta, cauda destacada |
| Acento 2 (petróleo) | `#1F6F6B` | adaptação, faixa segura, regra positiva |
| Âmbar (só em gráfico) | `#C8922F` | faixa intermediária / zona cinzenta |
| Texto de apoio | `#4A5A68` / `#3A4A57` | corpo secundário sobre claro |
| Sobre fundo escuro | `#BFD0DA`, `#7FC4BE`, `#E88C7D` | apoio, acento frio, acento quente |

Cor nunca diz sozinha: toda faixa, barra ou ponto colorido carrega o texto ao lado.

## Anatomia do slide (1920 × 1080)

- Margens `128px`; slides com rodapé usam `padding:128px 128px 160px`.
- **Eyebrow** (26px, versalete, acento 1): só o assunto do slide, sem número.
- **Título** (h2, 60px, Libre Baskerville 700).
- Corpo: cards em linha, tabela, gráfico + coluna de texto, ou lista.
- **Rodapé fixo** em `bottom:64px`: à esquerda o título da aula, sem número de aula
  nem de módulo; à direita a numeração `N / total` dos slides.
- Capa e slide de fecho no fundo do módulo; miolo alternando papel claro e papel quente.

### Cor da capa e do fecho por módulo

Só a capa e o slide de fecho mudam de cor, para o aluno sentir que trocou de módulo.
O miolo, a tipografia e as cores de dado continuam as mesmas em todo o curso.
No spec, a chave `"tema"` escolhe o conjunto (sem ela, vale tinta).

| Módulo | Tema | Fundo | Card no fecho | Eyebrow | Subtítulo e título de card |
|---|---|---|---|---|---|
| 1 e 2 | `tinta` | `#12202E` | `#1B2E3F` | `#7FC4BE` | `#E88C7D` |
| 3 | `bordo` | `#3A1A22` | `#4A2530` | `#7FC4BE` | `#E6C08A` |
| 4 | `petroleo` | `#0F3432` | `#184442` | `#E6C08A` | `#F2A58F` |

Todas as combinações de texto sobre o fundo passam de 5:1 de contraste.

## Regras travadas

1. **A capa não leva minutagem.** Duração é dado de produção, não de aula.
2. Vocabulário interno (arquitetura da aula, alvo de palavras) não aparece para o aluno.
   **Número de aula e de módulo também não**: a capa mostra o nome do módulo sem
   número e o rodapé mostra o título da aula. O último slide não anuncia a próxima
   aula: o gancho fica só na fala.
3. Gráfico de dado real é **desenhado em vetor**, nunca imagem gerada: régua de faixas,
   curva de distribuição, barras de regressão, traçado de ECG, grade de pontos.
4. Um assunto por slide; texto que não cabe vira outro slide — nada encolhe.
5. Citação de estudo no corpo do slide: autor e ano, sem PMID (o PMID fica no arquivo da aula).
6. Slide de fecho traz as regras da aula e quem faz o quê por profissão, sem "A seguir".
7. Um slide do deck para cada bloco de fala da aula (marcador 📊), mais a capa. As notas
   do apresentador de cada slide são o texto falado daquele bloco.

## Símbolo da marca

**Definido.** O símbolo é o anel aberto atravessado pelo traçado que nasce no centro
e sai pela abertura lateral. Arquivos em `marca/`:

| Arquivo | Uso |
|---|---|
| `marca/simbolo.svg` | tinta `#12202E`, para fundo claro |
| `marca/simbolo-claro.svg` | papel `#F7F6F2`, para fundo tinta |
| `marca/simbolo.png` | PNG transparente, 512 px, para ferramentas que não aceitam vetor |
| `marca/estudos/` | as propostas descartadas, guardadas como histórico |

**Não existe marca d'água.** O símbolo entra uma vez por slide, pequeno e discreto,
nunca atrás do conteúdo.

**Onde ele fica:**

- **Slides de miolo**: canto superior direito, altura 40 px, borda direita alinhada à
  margem de 128 px e topo na mesma linha da eyebrow. Cor `#97A4AE` sobre fundo claro.
- **Capa e slide de fecho** (fundo tinta): mesmo canto, altura 72 px, versão clara em
  `#F7F6F2` a 70% de opacidade, para não competir com o título.
- **Nunca**: no meio do slide, atrás de texto, sobre gráfico, repetido, ou esticado.
  A proporção é fixa, e a área livre ao redor é de meia altura do símbolo.

Quando existir nome de marca, o conjunto de nome e símbolo se monta a partir deste
mesmo desenho, com o símbolo à esquerda do nome, sem redesenhar nada.

## Como gerar um deck

Desde o Módulo 1 reescrito, os decks são gerados, e não montados à mão:

```
python3 ferramentas/slides/gerar_deck.py slides/MOD01/01-01.json <pasta_de_saida>
```

O spec JSON da aula traz título, subtítulo, nome do módulo e um objeto por slide,
com um dos tipos de layout: `cards`, `numeros`, `lista`, `duas` (duas colunas),
`tabela`, `frase` (slide-destaque em petróleo ou tinta), `html` (gráfico em vetor
feito à mão) e `fecho`. O gerador aplica a paleta, a tipografia, as margens, o
rodapé, o símbolo no canto superior direito e as notas do apresentador tiradas do
texto da aula. O número de slides do spec precisa bater com o número de blocos
📊 da aula, ou o gerador recusa.
