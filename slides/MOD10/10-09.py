"""Spec do deck 10.9. Gera 10-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
CINZA = "#C9CFD4"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"

dias = ["seg", "ter", "qua", "qui", "sex", "sáb"]
cores = [AZUL, OXID, GLIC, FOSF]

# 1. o corte
p = [svg_abre(1664, 500, "Linha do tempo partida: antes, uma semana cheia com trinta horas de treino; depois, a mesma semana em branco; no corte, uma trave de equilíbrio vazia")]
rs = []
for lado, x0 in [(0, 0), (1, 960)]:
    for j, d in enumerate(dias):
        x = x0 + j * 116
        if lado == 0:
            rs.append(rot(x, 0, d, w=106, tam=22, cor=MUDO, alinha="center"))
        for k in range(3):
            y = 44 + k * 110
            if lado == 0 and not (j == 5 and k == 2):
                p.append(f'<rect x="{x}" y="{y}" width="106" height="96" rx="10" fill="{cores[(j + k) % 4]}" opacity="0.85"/>')
            else:
                p.append(f'<rect x="{x}" y="{y}" width="106" height="96" rx="10" fill="none" stroke="{CINZA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<path d="M760 20 L800 120 L740 220 L810 330 L760 400" fill="none" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<rect x="700" y="420" width="220" height="18" rx="6" fill="#B08A5A"/>')
p.append(f'<rect x="720" y="438" width="12" height="50" fill="#8A6A44"/><rect x="888" y="438" width="12" height="50" fill="#8A6A44"/>')
p.append("</svg>")
rs += [rot(0, 400, "quinze anos: cerca de 30 horas por semana", w=680, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(960, 400, "a segunda-feira seguinte", w=690, tam=26, cor=MUDO, peso=700, alinha="center")]
S.append({"id": "corte", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Uma ginasta no começo da casa dos vinte anos", "titulo": "O fim da carreira é uma transição, não um evento",
          "fonte": "Terceira lesão em dois anos, desta vez na coluna · caso ilustrativo, sem desfecho"})

# 2. a estrada
p = [svg_abre(1664, 540, "Estrada que se bifurca: saída planejada, saída forçada, e uma saída lateral sem placa, a do amador que o corpo aposentou")]
p.append(f'<path d="M0 470 C 300 470, 420 420, 560 330" fill="none" stroke="#B9B2A2" stroke-width="60" stroke-linecap="round"/>')
p.append(f'<path d="M560 330 C 700 240, 900 120, 1250 90" fill="none" stroke="#B9B2A2" stroke-width="50" stroke-linecap="round"/>')
p.append(f'<path d="M560 330 C 720 330, 950 360, 1250 380" fill="none" stroke="#B9B2A2" stroke-width="50" stroke-linecap="round"/>')
p.append(f'<path d="M380 440 C 440 500, 520 520, 640 530" fill="none" stroke="#D8D3C4" stroke-width="34" stroke-linecap="round" stroke-dasharray="4 0"/>')
p.append(caixa(1260, 30, 404, 150, OXID, OXID_T))
p.append(caixa(1260, 310, 404, 150, FOSF, FOSF_T))
p.append(icone("t:road-sign", 1280, 60, 60, OXID))
p.append(icone("t:alert-triangle", 1280, 340, 60, FOSF))
p.append("</svg>")
rs = [rot(1350, 50, "saída planejada", w=300, tam=28, cor=OXID, peso=700, serif=True),
      rot(1350, 100, "escolha · momento · plano", w=300, tam=24, cor=TINTA),
      rot(1350, 330, "saída forçada", w=300, tam=28, cor=FOSF, peso=700, serif=True),
      rot(1350, 380, "lesão · corte · fim de contrato", w=300, tam=24, cor=TINTA),
      rot(660, 470, "o amador que o corpo aposentou, sem ninguém chamar de aposentadoria", w=560, tam=24, cor=MUDO, peso=600, lh=1.3),
      rot(0, 20, "O que pesou na adaptação:", w=560, tam=28, cor=TINTA, peso=700, serif=True),
      rot(0, 70, "planejamento antes da saída · controle sobre o momento · sensação de metas atingidas · força da identidade de atleta", w=560, tam=24, cor=TINTA, lh=1.4)]
S.append({"id": "estrada", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Nem toda saída é igual", "titulo": "Quem escolhe a hora de sair sai melhor",
          "fonte": "Revisão sistemática de 2013: 126 estudos sobre a transição para fora do esporte"})

# 3. as barras
p = [svg_abre(1664, 460, "Barras de ansiedade ou depressão: 34% em atletas de elite em atividade, 26% em ex-atletas; sofrimento psíquico em 16% dos ex-atletas")]
base, esc = 400, 9
dados = [(34, "em atividade", AZUL), (26, "ex-atletas", FOSF)]
rs = []
for i, (v, t, c) in enumerate(dados):
    x = 120 + i * 320
    p.append(f'<rect x="{x}" y="{base - v*esc}" width="240" height="{v*esc}" rx="10" fill="{c}"/>')
    rs.append(rot(x, base - v * esc - 70, f"{v}%", w=240, tam=56, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x, base + 14, t, w=240, tam=26, cor=TINTA, peso=700, alinha="center"))
p.append(f'<line x1="60" y1="{base}" x2="760" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
p.append(icone("t:door-exit", 1080, 60, 200, MUDO))
p.append("</svg>")
rs += [rot(900, 290, "parar não zera o risco", w=580, tam=40, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(900, 360, "sofrimento psíquico em 16% dos ex-atletas · e o atleta que parou some do cuidado", w=580, tam=24, cor=TINTA, alinha="center", lh=1.35),
       rot(60, 0, "ansiedade ou depressão", w=700, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "barras", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número da transição", "titulo": "Parar não zera o risco",
          "fonte": "Metanálise de 2019, atletas de elite em atividade e ex-atletas · Br J Sports Med"})

# 4. a agenda vazia
p = [svg_abre(1664, 520, "Agenda semanal com blocos fantasmas onde antes havia treino, e sobre cada bloco uma perda: rotina, grupo, uma voz que organizava, sentido, o nome")]
perdas = [("t:clock", "rotina", "o ginásio decidia a hora de acordar, comer, dormir"),
          ("t:users-group", "grupo", "as colegas eram as amigas, e continuam treinando"),
          ("t:message-circle", "uma voz de fora", "a técnica organizava cada dia"),
          ("t:target", "sentido", "cada sessão servia a uma meta"),
          ("t:user", "o nome", "“sou ginasta”")]
rs = []
for i, (ic, t, x_) in enumerate(perdas):
    x = i * 334
    p.append(f'<rect x="{x}" y="0" width="310" height="380" rx="16" fill="none" stroke="{CINZA}" stroke-width="4" stroke-dasharray="14 10"/>')
    p.append(icone(ic, x + 115, 40, 80, FOSF))
    rs.append(rot(x + 10, 150, t, w=290, tam=32, cor=FOSF, peso=700, alinha="center", serif=True))
    rs.append(rot(x + 20, 210, x_, w=270, tam=24, cor=TINTA, alinha="center", lh=1.35))
p.append(f'<rect x="0" y="410" width="1664" height="100" rx="14" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append("</svg>")
rs.append(rot(30, 438, "Ajuda: um horário fixo para alguma atividade, e alguém que pergunte, com data marcada", w=1604, tam=28, cor=OXID, peso=700, alinha="center"))
S.append({"id": "agenda", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As primeiras semanas", "titulo": "Com o treino, vão embora a rotina, o grupo e o nome",
          "fonte": "“Eu acordo e não sei o que fazer com o dia”"})

# 5. o corpo
p = [svg_abre(1664, 500, "Esquema: depois da saída, o gasto de energia cai de uma vez e o apetite desce devagar; entre os dois, uma área sombreada; ao lado, a ex-atleta sem saber treinar sem técnico")]
x0, x1, y0 = 80, 1080, 420
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="40" stroke="{MUDO}" stroke-width="3"/>')
gasto = f"M{x0} 80 H 300 V 300 H {x1}"
ap = " ".join(f"{x0 + k*10},{80 + 220*(1-math.exp(-max(0, k*10+x0-300)/380)) if k*10+x0 > 300 else 80:.0f}" for k in range(0, 101))
area = f"M300 80 " + " ".join(f"L{x0 + k*10} {80 + 220*(1-math.exp(-max(0, k*10+x0-300)/380)):.0f}" for k in range(22, 101)) + f" L{x1} 300 L300 300 Z"
p.append(f'<path d="{area}" fill="{GLIC_T}"/>')
p.append(f'<path d="{gasto}" fill="none" stroke="{AZUL}" stroke-width="7"/>')
p.append(f'<polyline points="{ap}" fill="none" stroke="{GLIC}" stroke-width="7"/>')
p.append(f'<line x1="300" y1="30" x2="300" y2="{y0}" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 8"/>')
p.append(icone("h:person", 1260, 90, 180, MUDO))
p.append(icone("t:question-mark", 1460, 60, 100, FOSF))
p.append("</svg>")
rs = [rot(310, 30, "a saída", w=200, tam=24, cor=TINTA, peso=700),
      rot(820, 312, "gasto de energia", w=260, tam=26, cor=AZUL, peso=700, alinha="right"),
      rot(620, 100, "apetite e hábitos de comer", w=440, tam=26, cor=GLIC, peso=700),
      rot(1180, 300, "nunca treinou sem técnico: não sabe se exercitar por prazer", w=460, tam=26, cor=TINTA, peso=600, alinha="center", lh=1.3),
      rot(x0, y0 + 20, "meses depois da saída →", w=600, tam=24, cor=MUDO)]
S.append({"id": "corpo", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os meses seguintes", "titulo": "O corpo também se aposenta, e ninguém explica como",
          "fonte": "Esquema, sem valores medidos · o destreino está no módulo de endocrinologia; a alimentação desordenada, no de nutrição"})

# 6. as pizzas da identidade
TRACO = ' stroke-dasharray="10 8"'
def pizza(cx, cy, r, fatias):
    out, a = [], -math.pi / 2
    for frac, cor, trac in fatias:
        b = a + frac * 2 * math.pi
        large = 1 if frac > 0.5 else 0
        out.append(f'<path d="M{cx} {cy} L{cx + r*math.cos(a):.1f} {cy + r*math.sin(a):.1f} A{r} {r} 0 {large} 1 {cx + r*math.cos(b):.1f} {cy + r*math.sin(b):.1f} Z" fill="{cor}" stroke="{PAPEL}" stroke-width="4"{TRACO if trac else ""}/>')
        a = b
    return out
p = [svg_abre(1664, 500, "Dois gráficos de pizza da identidade: antes, uma fatia quase inteira de ginasta; depois, várias fatias parecidas e espaços ainda em branco"), defs(TINTA)]
p += pizza(330, 250, 210, [(0.86, FOSF, False), (0.05, AZUL, False), (0.05, OXID, False), (0.04, GLIC, False)])
p += pizza(1250, 250, 210, [(0.22, FOSF, False), (0.18, AZUL, False), (0.16, OXID, False), (0.14, GLIC, False), (0.30, "#E6E3DA", True)])
p.append(seta(600, 250, 980, 250, TINTA, "m0", esp=6))
p.append("</svg>")
rs = [rot(279, 334, "ginasta", w=200, tam=34, cor=PAPEL, peso=700, alinha="center", serif=True),
      rot(0, 470, "antes: estudante, amiga, filha em fatias finas", w=660, tam=24, cor=TINTA, alinha="center"),
      rot(640, 200, "anos", w=300, tam=30, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(640, 270, "carreira dupla, amizades de fora, interesses que não dependem do corpo", w=300, tam=22, cor=MUDO, alinha="center", lh=1.3),
      rot(1048, 160, "ainda em branco", w=200, tam=24, cor=MUDO, peso=700, alinha="center"),
      rot(920, 470, "depois: fatias parecidas, e espaço para preencher", w=660, tam=24, cor=TINTA, alinha="center")]
S.append({"id": "pizza", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quem ela é agora", "titulo": "A transição começa anos antes, na identidade",
          "fonte": "Esquema, sem valores medidos · identidade de atleta forte se associa a mais dificuldade na saída e a menos planejamento"})

# 7. o funil da base
p = [svg_abre(1664, 540, "Funil de crianças entrando no esporte e saindo pelos lados, com os motivos; as saídas da diversão e da competência maiores")]
p.append(f'<path d="M200 40 H1460 L1080 440 H580 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
for k in range(8):
    p.append(icone("h:child-program", 300 + k * 140, 60, 80, AZUL))
saidas = [("deixou de ser divertido", 16, 180, 60, "e"), ("não me sinto bom nisso", 12, 320, 36, "e"),
          ("pressão de adulto", 8, 180, 40, "d"), ("outras prioridades", 8, 320, 40, "d")]
rs = []
for t, esp, y, w, lado in saidas:
    if lado == "e":
        xa = 200 + (y - 40) * (380 / 400)
        p.append(f'<path d="M{xa + 20:.0f} {y} C {xa - 80:.0f} {y}, {xa - 120:.0f} {y + 40}, {xa - 160:.0f} {y + 70}" fill="none" stroke="{FOSF}" stroke-width="{esp}" stroke-linecap="round"/>')
        rs.append(rot(0, y + 80, t, w=380, tam=26 if esp > 10 else 24, cor=FOSF, peso=700 if esp > 10 else 600))
    else:
        xa = 1460 - (y - 40) * (380 / 400)
        p.append(f'<path d="M{xa - 20:.0f} {y} C {xa + 80:.0f} {y}, {xa + 120:.0f} {y + 40}, {xa + 160:.0f} {y + 70}" fill="none" stroke="{MUDO}" stroke-width="{esp}" stroke-linecap="round"/>')
        rs.append(rot(1300, y + 80, t, w=364, tam=24, cor=MUDO, peso=600, alinha="right"))
p.append(icone("h:girl-1015y", 790, 350, 90, FOSF))
p.append("</svg>")
rs += [rot(580, 460, "a ginasta ficou; muitas colegas saíram antes dos doze", w=500, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.3),
       rot(560, 200, "motivos pessoais e das relações pesam mais que custo e transporte", w=540, tam=24, cor=AZUL, peso=700, alinha="center", lh=1.3)]
S.append({"id": "base", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O encerramento mais comum", "titulo": "Na base, a criança vai embora quando deixa de ser divertido",
          "fonte": "Revisão sistemática de 2015: 43 estudos incluídos de 557 · o módulo do atleta adolescente volta ao tema"})

# 8. a ponte
p = [svg_abre(1664, 520, "Ponte entre a margem atleta e a margem depois; cada tábua é uma tarefa de um profissional; uma tábua começa antes da margem: carreira dupla")]
p.append(f'<rect x="0" y="300" width="260" height="220" fill="#D8D3C4"/><rect x="1404" y="300" width="260" height="220" fill="#D8D3C4"/>')
p.append(f'<path d="M260 300 Q 832 380 1404 300" fill="none" stroke="#9C8E74" stroke-width="6"/>')
tab = [("t:clipboard-check", "rastrear humor", AZUL), ("t:clock", "dar estrutura", GLIC), ("t:run", "reconstruir o exercício", OXID),
       ("t:salad", "recalibrar a comida", GLIC), ("h:bandaged", "acompanhar as lesões", AZUL), ("t:puzzle", "alargar a identidade", FOSF)]
rs = []
for i, (ic, t, c) in enumerate(tab):
    x = 280 + i * 186
    tt = (x + 85 - 260) / 1144
    y = (1 - tt) ** 2 * 300 + 2 * (1 - tt) * tt * 380 + tt ** 2 * 300
    p.append(f'<rect x="{x}" y="{y - 30:.0f}" width="170" height="30" rx="6" fill="{c}"/>')
    p.append(icone(ic, x + 45, y - 230, 80, c))
    rs.append(rot(x - 5, y - 130, t, w=180, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2))
p.append(f'<rect x="40" y="250" width="200" height="30" rx="6" fill="{TINTA}"/>')
p.append("</svg>")
rs += [rot(20, 330, "atleta", w=220, tam=32, cor=TINTA, peso=700, alinha="center", serif=True),
       rot(1424, 330, "depois", w=220, tam=32, cor=TINTA, peso=700, alinha="center", serif=True),
       rot(20, 190, "carreira dupla, antes da margem", w=240, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.2),
       rot(280, 440, "e alguém que combine de perguntar, com data marcada: o atleta que parou some", w=1100, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.3)]
S.append({"id": "ponte", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que cada um faz", "titulo": "Cada profissional põe uma tábua na ponte"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Transição de carreira e encerramento precoce", "titulo": "Um ano depois, no meio da ponte",
          "regras": ["A saída é uma transição, não um evento",
                     "Quem escolhe a hora e planeja sai melhor; parar não zera o risco",
                     "Na base, a criança vai embora quando deixa de ser divertido"],
          "cards": [{"ic": "t:users", "t": "Quem treina e prepara", "x": "Reconstrói o exercício sem meta de competição e mantém contato."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Trata a transição como momento de risco e segue as lesões."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Ajuda a preencher as fatias em branco da identidade."}]})

spec = {"arquivo": "aulas/MOD10/10-09-transicao-de-carreira-e-encerramento-precoce.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Transição de carreira e encerramento precoce", "subtitulo": "O que acaba quando o esporte acaba",
        "nota_capa": "Uma ginasta, a terceira lesão, e a primeira segunda-feira sem ginásio.",
        "secoes": {"corte": ["Como a carreira acaba.", "capa"], "agenda": ["As semanas e o corpo.", "agenda"],
                   "pizza": ["Identidade e base.", "pizza"], "ponte": ["A ponte.", "ponte"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-09.json"), "w"), ensure_ascii=False, indent=1)
print("10-09.json:", len(S), "slides")
