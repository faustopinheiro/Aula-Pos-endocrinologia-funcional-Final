# Mapa das 158 aulas escritas → matriz de 400h

**Documento de trabalho.** A matriz de referência passa a ser a de
**Ciências do Esporte Aplicadas à Saúde — 400h · 14 módulos · 157 aulas**
(`00-matriz-400h.md`). Este arquivo diz, slot por slot, **qual roteiro já
escrito serve**, o que precisa ser fundido e o que ainda não existe.

**Legenda.**
`PRONTA` — existe roteiro que cobre o slot; precisa só de edição de formato.
`FUNDIR` — dois ou mais roteiros escritos alimentam o slot.
`PARCIAL` — existe material, mas o slot pede conteúdo que não está escrito.
`NOVA` — nada escrito.
`[M]` — aula-mestra de 75 min (~8.800 palavras faladas a 118 ppm).

---

## Módulo 1 — Fundamentos e Trabalho Multiprofissional · 8 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES.** O módulo foi reescrito inteiro depois
do Módulo 7, com as regras de fala travadas ali (sem travessões na fala, sem
número de aula na fala nem na tela, sem vocabulário de IA, citação por nome só
em estudo marcante) e com o objetivo explícito do coordenador de deixar a
abertura menos pesada. Três mudanças de estrutura:

- **As antigas 1.8, 1.9 e 1.10** (prática baseada em evidências, como ler um
  estudo e armadilhas da literatura, ~80 min somados) **viraram uma aula só**,
  a nova 1.8, com cinco histórias e cinco perguntas. Saíram pirâmide, GRADE,
  critérios de Hill e o ensaio CAST.
- **Toda aula abre por uma cena** e ganhou título que o aluno reconhece.
- **Repetições entre aulas foram cortadas**: os números da diretriz da OMS
  ficam só na 1.4; a curva de dose de Ekelund só na 1.3; os "três nomes na
  agenda" só na 1.7.

| Slot | Aula | Min | Arquitetura | Deck |
|---|---|---|---|---|
| 1.1 | Saúde e desempenho em quem treina | 13 | ERRO | [slides](https://claude.ai/artifact/2AVKVcxrxXqMYFZUkoEjnH) |
| 1.2 | Objetivo de desempenho e saúde | 14 | DECISÃO | [slides](https://claude.ai/artifact/4ViKgtc4uvKZ1qQNeXGz8Q) |
| 1.3 | Exercício como dose | 13 | NÚMERO | [slides](https://claude.ai/artifact/EytwbMrzjU7MPgqnUGnvJR) |
| 1.4 | Diretrizes de atividade física da OMS | 9 | PROCEDIMENTO | [slides](https://claude.ai/artifact/AjFXZne76LCoB9BnJa38e9) |
| 1.5 | A equipe de saúde no esporte | 12 | ERRO | [slides](https://claude.ai/artifact/5nH9JLGCpjdNcVkeXeKtZs) |
| 1.6 | Responsabilidades na equipe multiprofissional | 15 | DECISÃO | [slides](https://claude.ai/artifact/WQFyGTtDWAKgKrurUqva4q) |
| 1.7 | Encaminhamento entre profissionais | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/ApRMHJR1s9ZesYQHk4e7Cr) |
| 1.8 | Leitura crítica da literatura científica | 21 | ERRO | [slides](https://claude.ai/artifact/XyUpyLbciCTcyc5xVnrqwa) |

Total: 1 h 47 min (antes: 3 h 16 min em 10 aulas). Um caso clínico no módulo
(1.6, o homem de 37 anos com depressão e o personal). A 1.8 fecha o módulo com
a camada de integração nos três níveis.

**Calendário.** Com 14 módulos, o **mês 1 reúne os Módulos 1 e 2**. A abertura
curta foi pensada para caber ao lado da fisiologia do exercício no mesmo mês.

**Slides.** Cada aula tem um deck com a marca, gerado por
`ferramentas/slides/gerar_deck.py` a partir de `slides/MOD01/*.json`. As notas
do apresentador de cada slide trazem o texto falado daquele trecho da aula.

## Módulo 2 — Fisiologia do Exercício Aplicada · 12 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Módulo que pede imagem:
cada deck traz gráficos, esquemas e diagramas desenhados em SVG
(`ferramentas/slides/desenho.py`). Curvas sem dado medido levam "Esquema, sem
valores medidos"; toda referência foi conferida, e número que não se confirmou
saiu da aula (registro em Notas de produção de cada uma). A pedido do coordenador,
todos os decks foram enxutos (8 a 11 slides, mais fala por slide) para a aula
fluir melhor; nas aulas 2.1 a 2.9 os blocos vizinhos foram fundidos sem mexer
no texto falado.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 2.1 | Bioenergética do exercício | 17 | 8 | NÚMERO | [slides](https://claude.ai/artifact/F5RjLUR53oSM5vJcZmcGQ7) |
| 2.2 | Sistema fosfagênico | 16 | 9 | DECISÃO | [slides](https://claude.ai/artifact/BGbUNGc7DHYu7fBMxC5jKU) |
| 2.3 | Glicólise e lactato | 19 | 10 | ERRO | [slides](https://claude.ai/artifact/UgShkL2Ysw5UFKRsq3shY4) |
| 2.4 | Metabolismo oxidativo | 23 | 10 | NÚMERO | [slides](https://claude.ai/artifact/487nyfgjxJFjj4G8QY3PKY) |
| 2.5 | Respostas cardiovasculares ao exercício | 19 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/KmdNKFwpeFZPF9U2m5BxBs) |
| 2.6 | Sistema respiratório no exercício | 15 | 9 | ERRO | [slides](https://claude.ai/artifact/LYmMh6SoJP6jZaVXxrvRDP) |
| 2.7 | Fisiologia neuromuscular | 18 | 9 | NÚMERO | [slides](https://claude.ai/artifact/EWXRjppx3U1sdHjx7H1hW7) |
| 2.8 | Limiares e VO₂máx | 24 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/8zQKvm2BNvWXC8WWFZW1oD) |
| 2.9 | Treino concorrente | 20 | 11 | DECISÃO | [slides](https://claude.ai/artifact/2xhNJXZXbkbVrRAbEN57F5) |
| 2.10 | Fadiga no exercício | 15 | 9 | PROCEDIMENTO | [slides](https://claude.ai/artifact/64RyFmeWkcAJGuj8ghsrc7) |
| 2.11 | Recuperação e distribuição da carga | 15 | 9 | ERRO | [slides](https://claude.ai/artifact/LtSDiqA37qmrQNzRcz68QL) |
| 2.12 | Exercício em ambiente adverso | 19 | 10 | DECISÃO | [slides](https://claude.ai/artifact/MLGr7WJCvXZWAi1NoYgiNX) |

Total: 3 h 40 min em 12 aulas. Um caso clínico no módulo (2.8, o corredor de
46 anos, dito como caso ilustrativo). A 2.12 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento).

## Módulo 3 — Fisiologia Hormonal e Endocrinologia do Exercício · 12 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão do Módulo 2: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em bordô, a cor do módulo (docs/08).
Casos clínicos no módulo: dois, o teto (3.4, o corretor de 41 anos; 3.7, a corredora de 31 anos; ambos
ditos como caso ilustrativo). As aulas 3.8 a 3.12 ficam sem caso.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 3.1 | Organização dos eixos neuroendócrinos | 17 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/MrVw5tCmtwSeZuiWHjf5zr) |
| 3.2 | Eixo hipotálamo-hipófise-adrenal e exercício | 17 | 10 | ERRO | [slides](https://claude.ai/artifact/Mvtrm1DthCq7wHYATcxMCL) |
| 3.3 | Catecolaminas no exercício | 10 | 8 | NÚMERO | [slides](https://claude.ai/artifact/J5ZAYjYqNYhc2PVpKm7hJK) |
| 3.4 | Testosterona no praticante de exercício | 25 | 12 | DECISÃO | [slides](https://claude.ai/artifact/WGRqeCBPoFWFkjS8gq4fC8) |
| 3.5 | Hipogonadismo masculino | 15 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/KCn3UtBLXJFu32QcuRKu3A) |
| 3.6 | Eixo somatotrófico e exercício | 17 | 11 | ERRO | [slides](https://claude.ai/artifact/4snAKfAufyPTEZkiKjFc84) |
| 3.7 | Função tireoidiana no praticante de exercício | 15 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/Fdj8F2YGauNt6FZuXP5tgm) |
| 3.8 | Excesso de treinamento | 18 | 11 | DECISÃO | [slides](https://claude.ai/artifact/LeKxDaos5k7BhJpBGs9ZvN) |
| 3.9 | Destreino | 11 | 8 | NÚMERO | [slides](https://claude.ai/artifact/8HwHtcLjdAnxGNN42YLijV) |
| 3.10 | O músculo como órgão endócrino | 18 | 10 | ERRO | [slides](https://claude.ai/artifact/EnefAzMp9bQjCPiqpEU4v8) |
| 3.11 | Exercício e sensibilidade à insulina | 15 | 9 | NÚMERO | [slides](https://claude.ai/artifact/V6pg5KWi8jaabJnWoYxKgW) |
| 3.12 | Saúde óssea no praticante de exercício | 14 | 11 | DECISÃO | [slides](https://claude.ai/artifact/TCq25sZe21dQUuFcxxXFic) |

Total: 3 h 32 min em 12 aulas, 120 slides. A 3.12 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
disponibilidade energética, que abre o Módulo 4.

## Módulo 4 — Nutrição Esportiva · 12 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão dos módulos 2 e 3: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em petróleo, a cor do módulo (docs/08).
Casos clínicos no módulo: dois, o teto (4.2, a triatleta amadora de 31 anos; 4.12, o caso de
alimentação desordenada; ambos ditos como caso ilustrativo). As demais aulas usam contas e quadros
típicos, sem pessoa.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 4.1 | Disponibilidade energética | 22 | 11 | NÚMERO | [slides](https://claude.ai/artifact/HEzNWExXWaDNCBb8PQucjb) |
| 4.2 | Estimativa da disponibilidade energética | 13 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/8TMgguW9UuCBVz1zsVuxFD) |
| 4.3 | Carboidrato no exercício | 13 | 9 | ERRO | [slides](https://claude.ai/artifact/SBqG5oTMubaRd86YESYpNX) |
| 4.4 | Periodização de carboidrato | 13 | 10 | DECISÃO | [slides](https://claude.ai/artifact/1x6kVBd2Y4ggVRQ5iyeSAK) |
| 4.5 | Proteína no praticante de exercício | 16 | 10 | NÚMERO | [slides](https://claude.ai/artifact/26zRBhkn5gWvjEPfQquTUH) |
| 4.6 | Lipídios na nutrição esportiva | 13 | 9 | ERRO | [slides](https://claude.ai/artifact/MkfTLcFqWcksD3s1rNkHTf) |
| 4.7 | Micronutrientes no praticante de exercício | 13 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/XfbzmeXdJ53vQFBFVgobnn) |
| 4.8 | Hidratação no exercício | 18 | 10 | NÚMERO | [slides](https://claude.ai/artifact/QSia1kVTZKNsvtVAGBZ1ac) |
| 4.9 | Composição corporal no praticante de exercício | 23 | 10 | DECISÃO | [slides](https://claude.ai/artifact/LkcQEtJ61X8CdgckNHkk5S) |
| 4.10 | Nutrição em dia de competição | 16 | 10 | PROCEDIMENTO | [slides](https://claude.ai/artifact/5FHHGTiH4kRFn9FTkEj7VG) |
| 4.11 | Nutrição na rotina real | 18 | 10 | DECISÃO | [slides](https://claude.ai/artifact/UpVQTM4qJHJdDVtqkpBUsA) |
| 4.12 | Alimentação desordenada no esporte | 20 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/XD4Ln392adhTAcMT8ZvMFJ) |

Total: 3 h 18 min em 12 aulas, 121 slides. A 4.12 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
suplementação, que abre o Módulo 5.

## Módulo 5 — Suplementação, Ergogênicos e Antidoping · 11 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão dos módulos 2 a 4: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em ameixa, a cor do módulo (docs/08).
Um caso clínico no módulo (5.11, dito como caso ilustrativo); as demais aulas usam perfis
típicos, sem idade, e contas feitas em aula.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 5.1 | Avaliação de suplementos no esporte | 18 | 11 | PROCEDIMENTO | [slides](https://claude.ai/artifact/VjtKYknfSt3JsvUxR5wb5d) |
| 5.2 | Creatina | 21 | 12 | NÚMERO | [slides](https://claude.ai/artifact/FMeaA9yx5ky3hJ6XXm61jb) |
| 5.3 | Cafeína no exercício | 16 | 11 | DECISÃO | [slides](https://claude.ai/artifact/3RVdoaD71SuJzaX8Pq61sv) |
| 5.4 | Beta-alanina | 12 | 10 | NÚMERO | [slides](https://claude.ai/artifact/E5W6SrSsiEHKmG3XSnkWVS) |
| 5.5 | Nitrato e bicarbonato de sódio | 13 | 11 | PROCEDIMENTO | [slides](https://claude.ai/artifact/3jXnXk7q8begqZtUXjnMYb) |
| 5.6 | Proteína em pó e aminoácidos | 16 | 12 | ERRO | [slides](https://claude.ai/artifact/FMz7XeMxRzuFXnvsgwsYUj) |
| 5.7 | Ferro, vitamina D e ômega-3 | 18 | 12 | DECISÃO | [slides](https://claude.ai/artifact/AKrUBvR2KvMqRyD1hvqsNF) |
| 5.8 | Suplementos sem evidência | 17 | 12 | ERRO | [slides](https://claude.ai/artifact/E2PGjQBELM7K394zmu1tgL) |
| 5.9 | Contaminação de suplementos | 16 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/X6sPsDxHa4PoipVrNYQfoh) |
| 5.10 | Lista proibida e autorização de uso terapêutico | 22 | 12 | DECISÃO | [slides](https://claude.ai/artifact/29BMVTFdH9a5oCjvYnj3Dw) |
| 5.11 | Hormônios e peptídeos fora de indicação | 21 | 12 | CASO | [slides](https://claude.ai/artifact/DmBQus52PMFGkAQ97Dqi7f) |

Total: 3 h 10 min em 11 aulas, 127 slides. A 5.11 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
medicina esportiva clínica, que abre o Módulo 6.

## Módulo 6 — Medicina Esportiva Clínica · 12 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão dos módulos 2 a 5: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em tinta, a cor dos módulos 1 e 2 (docs/08).
Dois casos no módulo (6.1 e 6.12, ditos como caso ilustrativo); as demais aulas usam perfis
típicos, sem idade, e contas feitas em aula.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 6.1 | Avaliação pré-participação | 19 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/5XNMp9y1t4m4BYxVSr6Bk9) |
| 6.2 | Triagem cardiológica | 15 | 12 | DECISÃO | [slides](https://claude.ai/artifact/RYp1EvgZsQ5ySwRKBtriEu) |
| 6.3 | Coração de atleta versus cardiopatia | 22 | 12 | NÚMERO | [slides](https://claude.ai/artifact/QdE5U2a3EwDxcw37jnMkmC) |
| 6.4 | Morte súbita no esporte | 14 | 11 | ERRO | [slides](https://claude.ai/artifact/AMz2PhjEfQ7EPZHZXysZgG) |
| 6.5 | Emergência em campo | 18 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/G8X3hgaRPHzvh8djbxKvpZ) |
| 6.6 | Concussão relacionada ao esporte | 20 | 13 | DECISÃO | [slides](https://claude.ai/artifact/CyvT4PVvUngEguH3SCQS5n) |
| 6.7 | Broncoespasmo induzido pelo exercício | 15 | 12 | NÚMERO | [slides](https://claude.ai/artifact/DzjnUMt6eFDykUFYPvqaKq) |
| 6.8 | Infecção e retorno ao treino | 14 | 11 | DECISÃO | [slides](https://claude.ai/artifact/DjbTfXDhrMVcAceaX4DGr3) |
| 6.9 | Deficiência de ferro no atleta | 17 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/LsvPEkpGnZgM9HandCEtLs) |
| 6.10 | Rastreio laboratorial no esporte | 16 | 12 | ERRO | [slides](https://claude.ai/artifact/NyAf5c9837UohuqrLkyDZe) |
| 6.11 | Analgesia no esporte | 15 | 12 | DECISÃO | [slides](https://claude.ai/artifact/TuM4SBdrVDgHjTdG23inNQ) |
| 6.12 | Exercício na doença crônica | 18 | 12 | CASO | [slides](https://claude.ai/artifact/U2aKTDu9vRviZ2Jjufwctu) |

Total: 3 h 23 min em 12 aulas, 143 slides. A 6.12 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
prevenção de lesões, que abre o Módulo 7.

Âncoras brasileiras do módulo: SBC/SBMEE 2019 (ECG de repouso classe I mesmo no
amador), substituição adicional e permanente por concussão (IFAB; a CBF foi a
primeira confederação filiada à FIFA a adotá-la, Brasileirão 2024), Lei Lucas
(13.722/2018), levantamento da RBME sobre protocolos dos clubes profissionais de
São Paulo, e lista proibida da WADA 2026 (beta-2 agonistas, glicocorticoides e
infusões acima de 100 mL/12 h).

## Módulo 7 — Lesões: Mecanismos, Epidemiologia e Prevenção · 13 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão dos módulos 2 a 6: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em tinta, a cor dos módulos 1, 2 e 6 (docs/08).
Dois casos no módulo (7.8 e 7.12, ditos como caso ilustrativo); as demais aulas usam perfis
típicos, sem idade, e contas feitas em aula.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 7.1 | Epidemiologia da lesão esportiva | 15 | 12 | NÚMERO | [slides](https://claude.ai/artifact/Md1Wwbr9rd5nrPBptLNC5K) |
| 7.2 | Vigilância de lesão no mundo real | 13 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/P5of1DuarAA8dbWdy4fVwo) |
| 7.3 | Etiologia da lesão esportiva | 15 | 12 | ERRO | [slides](https://claude.ai/artifact/FEiKJAjnjNp8wz7hzrfctM) |
| 7.4 | Lesão muscular no esporte | 12 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/X23ksUD3SjVHvm1cLjg8S5) |
| 7.5 | Prognóstico da lesão muscular | 10 | 12 | NÚMERO | [slides](https://claude.ai/artifact/GyZn5825cPhfyH3cEZ3RUs) |
| 7.6 | Manejo do estiramento muscular | 15 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/Qp7Vxxdy5zKJjBMTSY21Ti) |
| 7.7 | Tendinopatia | 12 | 12 | ERRO | [slides](https://claude.ai/artifact/NvgZ9wpJmvVbovA898kNWU) |
| 7.8 | Tendinopatia do Aquiles | 14 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/YVkhWy3HotbPqkbxiDNGiA) |
| 7.9 | Lesões do joelho no esporte | 13 | 12 | DECISÃO | [slides](https://claude.ai/artifact/WveEpSDiEaG4h2Uc52Z3J2) |
| 7.10 | Entorse de tornozelo e dor no ombro | 11 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/EUB3Stjnd4mr77nZRZR4ky) |
| 7.11 | Lesão óssea por estresse | 11 | 12 | NÚMERO | [slides](https://claude.ai/artifact/CsvGUcTdr2uNfq5EsJqwTS) |
| 7.12 | Imagem no esporte | 13 | 12 | ERRO | [slides](https://claude.ai/artifact/5oFBgQGu14vg1G8bKTzycf) |
| 7.13 | Prevenção de lesões no esporte | 17 | 12 | DECISÃO | [slides](https://claude.ai/artifact/SfsGxkfxMSsGqDbVehmDzw) |

Total: 2 h 51 min em 13 aulas, 156 slides. A 7.13 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
fisioterapia esportiva e reabilitação, que abre o Módulo 8.

Âncoras brasileiras do módulo: consenso brasileiro de definição de lesão em
corredores (Yamato, Saragiotto e Lopes, 2015), modelo de sistemas complexos
vindo da UFMG (Bittencourt, 2016), revisão brasileira do FIFA 11+ (Sadigursky, 2017),
coorte de isquiotibiais em clube brasileiro (Oliveira-Júnior, 2024), crioterapia
em músculo de rato (Vieira Ramos, 2016) e o enquadramento do registro de lesão como dado pessoal sensível sob a LGPD.

## Módulo 8 — Fisioterapia Esportiva e Reabilitação · 12 aulas

**ESCRITO NA VOZ DO CURSO, COM SLIDES VISUAIS.** Mesmo padrão dos módulos 2 a 7: decks enxutos, gráficos
em SVG, referências conferidas. Capa e fecho em tinta, a cor dos módulos 1, 2, 6 e 7 (docs/08).
Régua de altitude: nenhuma aula ensina a executar técnica; cada uma diz o que a intervenção muda,
quando entra, quando sai e como se reconhece que não está funcionando. As duas aulas-mestras (8.3 e
8.11) seguem a regra de que a duração é do tema, não do formato.

| Slot | Aula | Min | Slides | Arquitetura | Deck |
|---|---|---|---|---|---|
| 8.1 | Avaliação funcional em reabilitação | 14 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/F2gRJ8uymTioNLB7D29eRx) |
| 8.2 | Fases da reabilitação | 13 | 12 | DECISÃO | [slides](https://claude.ai/artifact/MKd4uTHQG8rpUtpStavXrU) |
| 8.3 | Mecanotransdução | 14 | 12 | NÚMERO | [slides](https://claude.ai/artifact/8msei3NvpsQdKvWne4JCgh) |
| 8.4 | Progressão de carga | 13 | 12 | ERRO | [slides](https://claude.ai/artifact/9jazBGYEkGZEiJDRUbvKWz) |
| 8.5 | Reabilitação do cruzado anterior | 15 | 12 | CASO | [slides](https://claude.ai/artifact/5KPDnyxoMmsH26zTc6myoz) |
| 8.6 | Posterior da coxa e virilha | 13 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/ML5CD6E185jWJgg2QJGvoV) |
| 8.7 | Tornozelo depois da entorse | 12 | 12 | NÚMERO | [slides](https://claude.ai/artifact/VtcvD5jZMHgS1qhUsauV7f) |
| 8.8 | Ombro e coluna | 13 | 12 | DECISÃO | [slides](https://claude.ai/artifact/NAJh6tG8BbyjVsDaUEHZkY) |
| 8.9 | Recursos terapêuticos passivos | 12 | 12 | ERRO | [slides](https://claude.ai/artifact/PH4baMdP1nAKXX22WVqCBV) |
| 8.10 | Testes de retorno ao esporte | 12 | 12 | PROCEDIMENTO | [slides](https://claude.ai/artifact/Mwv9fJaCucDaSWEBVDQbkG) |
| 8.11 | Decisão de retorno ao esporte | 13 | 12 | DECISÃO | [slides](https://claude.ai/artifact/BetL3N7xVsohkUB3hFYmUh) |
| 8.12 | Risco residual e comunicação | 15 | 12 | NÚMERO | [slides](https://claude.ai/artifact/PUwsWBBSyvWFwpYn2K2wxq) |

Total: 2 h 39 min em 12 aulas, 144 slides. A 8.12 fecha o módulo com a camada de
integração nos três níveis (decisão, contribuição, reconhecimento) e emenda na
preparação física, treinamento e gestão de carga, que abre o Módulo 9.

## Módulo 9 — Preparação Física, Treinamento e Gestão de Carga · 12 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 9.1 | Princípios do treinamento | M1-A02 | PARCIAL |
| 9.2 | Modelos de periodização | M8-A01 + M8-A02 | FUNDIR |
| 9.3 **[M]** | Treino de força por objetivo | M7-A06 + M8-A03 | FUNDIR |
| 9.4 | Velocidade, aceleração e mudança de direção | — | NOVA |
| 9.5 | Treinamento aeróbio contínuo e intervalado | M8-A02 | PRONTA |
| 9.6 | Prescrição por zonas e por percepção de esforço | M6-A02 | PRONTA |
| 9.7 | Carga externa: GPS e métricas de campo | M6-A06 | PRONTA |
| 9.8 | Carga interna: PSE, FC e questionários | M1-A04 + M6-A02 + M6-A03 | FUNDIR |
| 9.9 **[M]** | Índices de carga aguda e crônica: uso, limitação e crítica | M9-A03 + M9-A04 | FUNDIR |
| 9.10 | Testes físicos: escolher, aplicar e interpretar | M6-A05 + M6-A07 | FUNDIR |
| 9.11 | Reintegração ao treinamento coletivo | M18-A05 | PRONTA |
| 9.12 | Sono e recuperação como variáveis de treino | M10-A01 + M10-A07 | FUNDIR |

## Módulo 10 — Psicologia do Esporte e Saúde Mental · 11 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 10.1 | Motivação, autoeficácia e regulação emocional | M11-A07 | PRONTA |
| 10.2 | Atenção, ativação e desempenho sob pressão | — | NOVA |
| 10.3 **[M]** | Saúde mental no rendimento: prevalência e risco | M11-A01 + M11-A03 | FUNDIR |
| 10.4 | Rastreio e instrumentos validados | M11-A02 + M4-A07 | FUNDIR |
| 10.5 | Fluxo de encaminhamento | M11-A08 | PRONTA |
| 10.6 **[M]** | Psicologia da lesão: do impacto ao medo de nova lesão | M18-A06 + M17-A09 | FUNDIR |
| 10.7 | Prontidão psicológica para o retorno | M18-A06 | PRONTA |
| 10.8 | Esgotamento e sobrecarga crônica | M11-A04 | PRONTA |
| 10.9 | Transição de carreira e encerramento precoce | — | NOVA |
| 10.10 | Ambiente seguro: assédio, abuso e proteção | — | NOVA |
| 10.11 | Comunicação, adesão e mudança de comportamento | M11-A07 + M16-A06 | FUNDIR |

## Módulo 11 — A Atleta Mulher · 10 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 11.1 | Fisiologia da mulher e o déficit histórico de evidência | M13-A09 + M3-A03 | FUNDIR |
| 11.2 | Ciclo menstrual: fases e efeitos | M13-A01 | PRONTA |
| 11.3 | Sintomas menstruais: o que de fato limita | M13-A02 | PRONTA |
| 11.4 | Contracepção hormonal no esporte | M13-A03 | PRONTA |
| 11.5 **[M]** | REDs: da tríade ao modelo multissistêmico | M13-A04 + M2-A05 | FUNDIR |
| 11.6 | Reconhecer a deficiência energética fora do consultório médico | M13-A05 parcial | PARCIAL |
| 11.7 | Saúde óssea, disfunção menstrual e fratura por estresse | M13-A05 + M17-A04 | FUNDIR |
| 11.8 | Risco de LCA em mulheres | M13-A06 | PRONTA |
| 11.9 | Exercício na gestação e no pós-parto | M13-A07 | PRONTA |
| 11.10 | Transição da menopausa | M13-A08 | PRONTA |

**Módulo mais bem servido do curso: 7 de 10 slots prontos.**

## Módulo 12 — Atleta Adolescente e Atleta Idoso · 11 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 12.1 | Crescimento e maturação | M12-A01 | PRONTA |
| 12.2 | Pico de velocidade de crescimento e vulnerabilidade | M12-A01 parcial | PARCIAL |
| 12.3 **[M]** | Especialização precoce | M12-A03 | PARCIAL |
| 12.4 | Efeito da idade relativa | M12-A02 | PRONTA |
| 12.5 | Lesões do esqueleto imaturo | M12-A05 + M12-A06 | FUNDIR |
| 12.6 | Treinamento de força no jovem | M12-A04 | PRONTA |
| 12.7 **[M]** | Sarcopenia e exercício como contramedida | M14-A02 + M14-A03 | FUNDIR |
| 12.8 | Prescrição de força no idoso | M14-A02 parcial | PARCIAL |
| 12.9 | O atleta máster | M14-A01 + M14-A05 | FUNDIR |
| 12.10 | Fragilidade, risco de queda e capacidade funcional | — | NOVA |
| 12.11 | Comunicação com pais, treinadores e cuidadores | M12-A09 | PRONTA |

## Módulo 13 — O Atleta Amador e o Praticante Recreacional · 11 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 13.1 | Quem é o praticante amador: perfis e motivações | M1-A01 adaptada | PARCIAL |
| 13.2 | O que muda quando o esporte não paga as contas | M16-A03 → **U7-A03 já editada** | PRONTA |
| 13.3 **[M]** | Atividade concentrada em poucos dias | M16-A03 parcial | PARCIAL |
| 13.4 | Avaliação pré-participação no amador: até onde ir | M14-A08 parcial | PARCIAL |
| 13.5 | Rastreio versus medicalização | M5-A09 | PRONTA |
| 13.6 | Eventos de massa: risco cardiovascular em corrida de rua | — | NOVA |
| 13.7 | Organização da resposta de emergência em prova | — | NOVA |
| 13.8 **[M]** | Epidemiologia de lesão no corredor recreacional | M16-A01 + A02 → **U7-A01/A02** | FUNDIR |
| 13.9 | Lesões em academia, funcional e coletivo amador | M16-A02 + M17-A06 | FUNDIR |
| 13.10 | Progressão para quem treina 4h por semana | M16-A04 → **U7-A04 já editada** | PRONTA |
| 13.11 | Dependência de exercício e automedicação | M11-A06 + M4-A06 | FUNDIR |

## Módulo 14 — Integração, Gestão e Projeto Aplicado · 10 aulas

| Slot | Aula | Origem | Estado |
|---|---|---|---|
| 14.1 **[M]** | Caso integrado 1: atleta profissional com lesão recorrente | — | NOVA |
| 14.2 **[M]** | Caso integrado 2: amador com fadiga e queda de rendimento | M1-A09 + M9-A06 | FUNDIR |
| 14.3 | Caso integrado 3: adolescente em especialização precoce | — | NOVA |
| 14.4 | Caso integrado 4: atleta mulher com fratura por estresse | — | NOVA |
| 14.5 | Como escrever um protocolo de departamento | — | NOVA |
| 14.6 | Documentação de decisão e rastreabilidade | — | NOVA |
| 14.7 | Ética, sigilo e proteção de dados | M3-A07 parcial | PARCIAL |
| 14.8 | Projeto aplicado: como definir o problema | M24 (não escrito) | NOVA |
| 14.9 | Projeto aplicado: método e indicadores | M24 (não escrito) | NOVA |
| 14.10 | Projeto aplicado: estrutura da defesa | M24 (não escrito) | NOVA |

---

## Balanço

| Estado | Slots | % |
|---|---|---|
| **PRONTA** — roteiro existe, só edição de formato | 42 | 27% |
| **FUNDIR** — dois ou mais roteiros escritos alimentam o slot | 38 | 24% |
| **PARCIAL** — há material, falta conteúdo | 26 | 17% |
| **NOVA** — nada escrito | 51 | 32% |
| | **157** | |

**Traduzindo: 80 dos 157 slots (51%) têm roteiro aproveitável.** As 352 mil
palavras escritas não se perdem — elas se redistribuem.

### Onde está o trabalho pesado

1. **Módulo 5 inteiro** (suplementação, ergogênicos, antidoping) — 11 aulas
   novas, 2 delas mestras. M20 e M21 nunca saíram do ementário.
2. **As 27 aulas-mestras.** A 75 min e 118 palavras por minuto, cada uma pede
   **cerca de 8.800 palavras faladas** — quase três vezes o roteiro mais longo
   já escrito. São ~237 mil palavras só nelas. **É a maior decisão de produção
   da grade e precisa ser confirmada antes de qualquer redação.**
3. **Os blocos clínicos que não existem:** coração de atleta × cardiopatia,
   concussão, emergência em campo, analgesia e corticoide, mecanotransdução,
   miocinas.
4. **Módulo 14** — 8 de 10 aulas novas.
