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
- **Eyebrow** (26px, versalete, acento 1): `Slide N · assunto`.
- **Título** (h2, 60px, Libre Baskerville 700).
- Corpo: cards em linha, tabela, gráfico + coluna de texto, ou lista.
- **Rodapé fixo** em `bottom:64px`: à esquerda `Módulo X · Aula X.Y — Título`;
  à direita a numeração `N / total`.
- Capa e slide de fecho em fundo tinta; miolo alternando papel claro e papel quente.

## Regras travadas

1. **A capa não leva minutagem.** Duração é dado de produção, não de aula.
2. Vocabulário interno (arquitetura da aula, alvo de palavras) não aparece para o aluno.
3. Gráfico de dado real é **desenhado em vetor**, nunca imagem gerada: régua de faixas,
   curva de distribuição, barras de regressão, traçado de ECG, grade de pontos.
4. Um assunto por slide; texto que não cabe vira outro slide — nada encolhe.
5. Citação de estudo no corpo do slide: autor e ano, sem PMID (o PMID fica no arquivo da aula).
6. Slide de fecho sempre traz as regras da aula, o escopo por profissão e o gancho da próxima.

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
