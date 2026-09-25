"""Spec do deck 8.4. Gera 08-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "planilha", "tipo": "frase", "fundo": "tinta", "eyebrow": "A conduta que parece prudente",
          "frase": "Dez por cento por semana, religiosamente, há sete semanas. E piorando.",
          "apoio": "Um corredor voltando de tendinopatia de Aquiles. A regra não diz sobre o que se calculam os dez por cento, nem o que mais mudou naquela semana."})

S.append({"id": "regra", "tipo": "numeros", "eyebrow": "O que a evidência diz da regra", "titulo": "Saltos grandes preocupam; a regra sozinha não protegeu",
          "numeros": [{"n": "21% × 20%", "x": "lesionados com e sem a regra dos 10%; 486 iniciantes sorteados", "cor": "ambar"},
                      {"n": "> 30%", "x": "de aumento em duas semanas: mais lesão por distância que abaixo de 10%; 874 iniciantes", "cor": "verm"}],
          "destaque": "Boa heurística de conversa, não lei. E dá para errar respeitando-a à risca.",
          "destaque_cor": "tinta", "fonte": "Am J Sports Med 2008 · J Orthop Sports Phys Ther 2014"})

p = [svg_abre(1664, 300, "Volume semanal: alto antes da lesão, quase zero em seis semanas paradas, e duas progressões depois: ancorada no volume de antes, que salta alto, e ancorada no volume atual, que sobe devagar")]
p.append(f'<line x1="40" y1="270" x2="1620" y2="270" stroke="{MUDO}" stroke-width="3"/>')
w = 56; x0 = 60
vols_antes = [200, 205, 210]
for i, v in enumerate(vols_antes):
    p.append(f'<rect x="{x0 + i*70}" y="{270 - v}" width="{w}" height="{v}" rx="4" fill="{MUDO}" fill-opacity="0.55"/>')
for i in range(6):
    p.append(f'<rect x="{x0 + (3+i)*70}" y="266" width="{w}" height="4" rx="2" fill="{MUDO}"/>')
base = 20
for i in range(7):
    v1 = min(230, 210 * 0.55 * 1.1**i)
    v2 = base * 1.1**i * (1 + 0.35*i)
    xa = x0 + (9+i)*70
    p.append(f'<rect x="{xa}" y="{270 - v1:.0f}" width="{w/2 - 2:.0f}" height="{v1:.0f}" rx="3" fill="{FOSF}"/>')
    p.append(f'<rect x="{xa + w/2:.0f}" y="{270 - v2:.0f}" width="{w/2 - 2:.0f}" height="{v2:.0f}" rx="3" fill="{OXID}"/>')
p.append("</svg>")
rs = [rot(40, 20, "antes da lesão", w=260, tam=22, cor=MUDO, peso=700),
      rot(270, 200, "seis semanas quase paradas", w=420, tam=22, cor=MUDO, peso=700),
      rot(1180, 6, "âncora no volume de antes: salto disfarçado", w=470, tam=22, cor=FOSF, peso=700),
      rot(1180, 150, "âncora no que tolerou nas últimas duas semanas", w=470, tam=22, cor=OXID, peso=700)]
S.append({"id": "ancora", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro um", "titulo": "A âncora errada",
          "destaque": "A base é o que a pessoa fez, sem piora, nas últimas duas semanas. Não o que fazia antes da lesão.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "variavel", "tipo": "lista", "eyebrow": "Erro dois · volume e ladeira na mesma semana", "titulo": "Uma variável por vez, nesta ordem",
          "itens": [{"t": "Frequência", "x": "mais sessões na semana", "cor": "petr"},
                    {"t": "Volume", "x": "mais em cada sessão", "cor": "petr"},
                    {"t": "Densidade", "x": "menos pausa", "cor": "ambar"},
                    {"t": "Intensidade", "x": "ritmo, ladeira, carga: por último", "cor": "verm"}],
          "gap_itens": 6,
          "destaque": "Regra prática, não achado de ensaio: do menos arriscado para o mais. Entre uma mudança e outra, a leitura de 24 a 48 horas.",
          "destaque_cor": "tinta"})

S.append({"id": "degrau", "tipo": "cards", "por_linha": 4, "eyebrow": "Erro três · o protocolo sem “desde que”", "titulo": "Os quatro elementos de um degrau",
          "cards": [{"t": "Estímulo", "x": "elevação de calcanhar numa perna só, 3 séries, 2 repetições antes da falha", "cor": "petr"},
                    {"t": "Dose", "x": "quantas vezes por semana, com que carga", "cor": "petr"},
                    {"t": "Critério de saída", "x": "o que precisa acontecer para subir", "cor": "ambar"},
                    {"t": "Critério de regressão", "x": "o que faz voltar um degrau", "cor": "verm"}],
          "destaque": "O quarto elemento é o mais importante e o menos escrito.",
          "destaque_cor": "verm"})

p = [svg_abre(1664, 280, "Espiral: piora, para tudo, perde condicionamento, volta com a carga antiga, piora de novo")]
p.append("<defs>" + seta_marker("esp", FOSF) + "</defs>")
pts = [(200, 140), (560, 60), (960, 140), (1320, 60), (1560, 180)]
for (a, b), (c, d) in zip(pts, pts[1:]):
    p.append(f'<path d="M{a},{b} Q{(a+c)/2},{(b+d)/2 + 90} {c},{d}" fill="none" stroke="{FOSF}" stroke-width="4" marker-end="url(#esp)"/>')
for x, y in pts:
    p.append(f'<circle cx="{x}" cy="{y}" r="14" fill="{FOSF}"/>')
p.append("</svg>")
rs = [rot(80, 170, "piora", w=240, tam=24, cor=FOSF, peso=700, alinha="center"),
      rot(420, 6, "para tudo", w=280, tam=24, cor=FOSF, peso=700, alinha="center"),
      rot(800, 170, "perde condicionamento", w=320, tam=24, cor=FOSF, peso=700, alinha="center"),
      rot(1150, 6, "volta com a carga antiga", w=340, tam=24, cor=FOSF, peso=700, alinha="center"),
      rot(1400, 212, "piora de novo", w=260, tam=24, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "espiral", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro quatro", "titulo": "Parar tudo quando piora",
          "destaque": "A resposta a uma piora é ajustar a carga, não retirá-la: a carga ótima das siglas do primeiro atendimento vale aqui também.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2012"})

S.append({"id": "degrauabaixo", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Uma piora é um degrau para baixo, não uma queda da escada.",
          "apoio": "A piora vai acontecer; no tendão, quase sempre. A diferença está em a pessoa saber, antes, o que fazer quando ela chegar."})

p = [svg_abre(1664, 240, "Duas linhas do tempo de doze semanas: dez sessões seguidas nas três primeiras semanas, ou as mesmas dez espalhadas em doze semanas, mais densas no começo")]
p.append(f'<line x1="330" y1="70" x2="1620" y2="70" stroke="{GRADE}" stroke-width="3"/>')
p.append(f'<line x1="330" y1="180" x2="1620" y2="180" stroke="{GRADE}" stroke-width="3"/>')
sem = lambda s: 330 + s / 12 * 1290
for s in [0, 0.3, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3]:
    p.append(f'<circle cx="{sem(s):.0f}" cy="70" r="13" fill="{FOSF}"/>')
for s in [0, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12]:
    p.append(f'<circle cx="{sem(s):.0f}" cy="180" r="13" fill="{OXID}"/>')
for s in (0, 3, 6, 9, 12):
    p.append(f'<line x1="{sem(s):.0f}" y1="205" x2="{sem(s):.0f}" y2="215" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(0, 52, "10 seguidas: alta em 3 semanas", w=320, tam=22, cor=FOSF, peso=700),
      rot(0, 162, "as mesmas 10, espaçadas", w=320, tam=22, cor=OXID, peso=700)] + \
     [rot(sem(s) - 50, 216, f"sem {s}", w=100, tam=20, cor=MUDO, alinha="center") for s in (0, 3, 6, 9, 12)]
S.append({"id": "alta", "tipo": "diagrama", "h": 240, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro cinco · a alta administrativa", "titulo": "O mesmo número de sessões, cobrindo doze semanas",
          "destaque": "Primeiras sessões para ensinar e calibrar, programa escrito, revisão com data. Alta sem data de revisão é abandono agendado.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "registro", "tipo": "tabela", "eyebrow": "A ferramenta que corrige os cinco", "titulo": "O registro de cinco colunas",
          "cab": ["Data", "O que fez", "Carga ou volume", "Dor durante (0–10)", "Dor em 24 h (0–10)"],
          "larguras": [14, 26, 20, 20, 20],
          "linhas": [["seg", "trote e caminhada", "20 min", "2", "2"],
                     ["qua", "trote e caminhada", "25 min", "2", "3"],
                     ["sex", "trote com ladeira", "25 min", "3", "6"]],
          "destaque": "Sem registro, a consulta traz memória, puxada pelo último dia ruim. Com registro, a pessoa costuma achar o padrão antes de você.",
          "destaque_cor": "tinta", "fonte": "Linhas ilustrativas"})

S.append({"id": "principios", "tipo": "cards", "por_linha": 3, "eyebrow": "O que sobrevive à crítica dos índices de carga", "titulo": "Três princípios para a reabilitação",
          "cards": [{"t": "A base protege", "x": "carga crônica bem construída tolera mais", "cor": "petr"},
                    {"t": "O pico importa", "x": "a semana em que dobrou pesa mais que a média do mês", "cor": "ambar"},
                    {"t": "Carga não é só treino", "x": "sono, trabalho, estresse e doença entram na conta", "cor": "tinta"}],
          "destaque": "O índice agudo e crônico não serve como número de decisão; o módulo de preparação física volta a ele.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2016 · consenso do COI 2016"})

S.append({"id": "cinco", "tipo": "tabela", "eyebrow": "Juntando", "titulo": "Cinco erros e o que fazer no lugar",
          "cab": ["Erro", "No lugar"],
          "larguras": [34, 66],
          "linhas": [["Âncora errada", "progredir sobre o que tolerou nas últimas duas semanas"],
                     ["Duas variáveis juntas", "uma por vez: frequência, volume, densidade, intensidade"],
                     ["Degrau sem condição", "estímulo, dose, critério de saída e de regressão"],
                     ["Parar tudo quando piora", "regressão escrita antes: um degrau para baixo"],
                     ["Alta administrativa", "sessões espaçadas, programa escrito, revisão marcada"]],
          "destaque": "Por baixo dos cinco, o registro.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Progressão de carga", "titulo": "Nada disso acelera o tecido. Só para de atrapalhá-lo.",
          "regras": ["Base real, uma variável por vez",
                     "Degraus com critério de saída e de regressão",
                     "Registro e revisão marcada"],
          "cards": [{"t": "Fisioterapia", "x": "Escreve os degraus e os critérios."},
                    {"t": "Preparação física", "x": "Traz a base real e assume no campo."},
                    {"t": "Médico", "x": "Traduz “repouso relativo” em carga."}],
          "quem": "Próxima aula: a reconstrução do cruzado anterior, num caso ilustrativo."})

spec = {"arquivo": "aulas/MOD08/08-04-progressao-de-carga-em-tecido-em-cicatrizacao.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Progressão de carga", "subtitulo": "Cinco erros de dose em tecido em cicatrização",
        "nota_capa": "Entra pelo corredor que cumpre os dez por cento e piora.",
        "secoes": {"planilha": ["A regra dos dez por cento e a âncora.", "capa"],
                   "variavel": ["Variáveis, degraus e a espiral.", "variavel"],
                   "alta": ["Alta administrativa e registro.", "alta"],
                   "principios": ["Princípios e o fecho.", "principios"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-04.json"), "w"), ensure_ascii=False, indent=1)
print("08-04.json:", len(S), "slides")
