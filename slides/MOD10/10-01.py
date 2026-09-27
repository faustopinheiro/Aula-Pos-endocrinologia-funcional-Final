"""Spec do deck 10.1. Gera 10-01.json ao lado deste arquivo."""
import json, math, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def seta(x1, y1, x2, y2, cor, mk, esp=4, tr=False):
    d = ' stroke-dasharray="10 8"' if tr else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}"{d} marker-end="url(#{mk})"/>'

def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"

# 1. a régua dos tipos de motivação
seg = [("Sem motivação", "não vê sentido", "#9AA5AE"), ("Externa", "manda, premia, pune", FOSF),
       ("Introjetada", "culpa, provar valor", "#C0612F"), ("Identificada", "reconhece o valor", GLIC),
       ("Integrada", "faz parte de quem é", "#3E9C8F"), ("Intrínseca", "é bom em si", OXID)]
w, x0, y0, sw = 1664, 0, 210, 1664 / 6
p = [svg_abre(w, 470, "Régua de seis tipos de motivação, da ausência de motivação à intrínseca, com a regulação controlada à esquerda e a autônoma à direita"), defs(MUDO)]
rs = []
for i, (n, x, c) in enumerate(seg):
    xi = x0 + i * sw
    p.append(f'<rect x="{xi + 3:.1f}" y="{y0}" width="{sw - 6:.1f}" height="70" rx="8" fill="{c}"/>')
    rs.append(rot(xi, y0 + 84, n, w=sw, tam=28, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(xi, y0 + 124, x, w=sw, tam=24, cor=APOIO2, alinha="center"))
for a, b, t, c in [(1, 3, "controlada", FOSF), (3, 6, "autônoma", OXID)]:
    xa, xb = a * sw + 12, b * sw - 12
    p.append(f'<path d="M{xa:.0f} {y0-14} v-18 H{xb:.0f} v18" fill="none" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(xa, y0 - 70, t, w=xb - xa, tam=28, cor=c, peso=700, alinha="center"))
p.append(f'<rect x="560" y="20" width="560" height="64" rx="32" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M840 84 C 860 120, 980 110, 1000 130" fill="none" stroke="{MUDO}" stroke-width="3" stroke-dasharray="8 8"/>')
rs.append(rot(560, 34, "“ele não tem motivação”", w=560, tam=30, cor=TINTA, peso=600, alinha="center", serif=True))
rs.append(rot(1010, 110, "?", w=40, tam=40, cor=MUDO, peso=700))
p.append("</svg>")
S.append({"id": "regua", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro um", "titulo": "Motivação não é quanto. É de que tipo",
          "fonte": "Teoria da autodeterminação, Deci e Ryan · a frase do treinador não cabe em lugar nenhum da régua"})

# 2. adoção e manutenção
def faixas(fx, fy):
    return (f'<rect x="{fx(0):.1f}" y="{fy(1):.1f}" width="{fx(6)-fx(0):.1f}" height="{fy(0)-fy(1):.1f}" fill="{GLIC_T}"/>'
            f'<rect x="{fx(6):.1f}" y="{fy(1):.1f}" width="{fx(24)-fx(6):.1f}" height="{fy(0)-fy(1):.1f}" fill="{OXID_T}" fill-opacity="0.6"/>')
ms = [m / 2 for m in range(0, 49)]
contr = [(m, 0.78 * math.exp(-m / 14) + 0.12) for m in ms]
auton = [(m, 0.82 - 0.46 * math.exp(-m / 6)) for m in ms]
svg, rs = linhas(1664, 440, "Esquema: a presença sustentada por motivação controlada cai ao longo de dois anos; a sustentada por motivação autônoma sobe devagar e se mantém",
    [{"nome": "motivação controlada", "cor": FOSF, "pts": contr, "rotulo_xy": (15, 0.26), "dy": 10, "rw": 380},
     {"nome": "motivação autônoma", "cor": OXID, "pts": auton, "rotulo_xy": (15, 0.80), "dy": -58, "rw": 380}],
    0, 24, 0, 1, [(0, "início"), (6, "6 meses"), (12, "1 ano"), (24, "2 anos")], [], yfmt=lambda v: "",
    margem=(40, 20, 60, 40), extra=faixas)
rs += [rot(60, 30, "adoção: pesa reconhecer o valor", w=420, tam=26, cor="#8A5A10", peso=700),
       rot(560, 30, "manutenção: pesa o prazer em si", w=520, tam=26, cor=OXID, peso=700),
       rot(60, 380 - 30, "presença nos treinos", w=300, tam=22, cor=MUDO)]
S.append({"id": "tempo", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "Por que o tipo importa", "titulo": "Quem treina por culpa treina. E para.",
          "fonte": "Esquema, sem valores medidos · revisão sistemática de 66 estudos, Int J Behav Nutr Phys Act 2012"})

# 3. as três necessidades
nec = [("h:award-trophy", "Competência", "Ele parou de melhorar na serra?", GLIC, GLIC_T),
       ("t:compass", "Autonomia", "A planilha virou uma ordem sem explicação?", OXID, OXID_T),
       ("t:friends", "Vínculo", "O grupo de sábado mudou?", FOSF, FOSF_T)]
p = [svg_abre(1664, 520, "Três necessidades, competência, autonomia e vínculo, cada uma com uma pergunta sobre o ciclista, convergindo para a motivação autônoma"), defs(MUDO)]
rs = []
for i, (ic, t, q, c, ct) in enumerate(nec):
    cy = 80 + i * 175
    p.append(f'<circle cx="80" cy="{cy}" r="72" fill="{ct}"/>')
    p.append(icone(ic, 36, cy - 44, 88, c))
    rs.append(rot(185, cy - 50, t, w=600, tam=40, cor=c, peso=700, serif=True))
    rs.append(rot(185, cy + 4, q, w=820, tam=30, cor=TINTA))
    p.append(seta(1040, cy, 1250, 260 + (cy - 255) * 0.35, MUDO, "m0"))
p.append(caixa(1270, 170, 390, 180, OXID, OXID_T, esp=5))
p.append("</svg>")
rs.append(rot(1270, 214, "Motivação autônoma", w=390, tam=34, cor=OXID, peso=700, alinha="center", serif=True))
rs.append(rot(1270, 262, "a régua anda para a direita", w=390, tam=24, cor=APOIO2, alinha="center"))
S.append({"id": "necessidades", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que desloca a régua", "titulo": "Três necessidades, três perguntas para quem sumiu"})

# 4. a cascata do técnico
p = [svg_abre(1664, 540, "Cascata do modelo da relação técnico e atleta: o que molda o técnico, os comportamentos dele, as três necessidades, a motivação e os desfechos; embaixo, o caminho controlador"), defs(TINTA, FOSF)]
rs = []
col1 = ["orientação pessoal", "contexto e pressão", "leitura do atleta"]
for i, t in enumerate(col1):
    y = 20 + i * 100
    p.append(caixa(0, y, 250, 76, MUDO, CARTAO, esp=3))
    rs.append(rot(0, y + 22, t, w=250, tam=24, cor=TINTA, peso=600, alinha="center"))
    p.append(seta(256, y + 38, 318, 150, TINTA, "m0", esp=3))
p.append(caixa(330, 40, 330, 220, TINTA, CARTAO, esp=4))
rs += [rot(330, 56, "O que o técnico faz", w=330, tam=28, cor=TINTA, peso=700, alinha="center"),
       rot(350, 108, "apoio à autonomia", w=290, tam=26, cor=OXID, peso=600, alinha="center"),
       rot(350, 150, "estrutura clara", w=290, tam=26, cor=OXID, peso=600, alinha="center"),
       rot(350, 192, "envolvimento real", w=290, tam=26, cor=OXID, peso=600, alinha="center")]
for i, (t, c, ct) in enumerate([("competência", GLIC, GLIC_T), ("autonomia", OXID, OXID_T), ("vínculo", FOSF, FOSF_T)]):
    y = 20 + i * 90
    p.append(seta(666, 150, 740, y + 34, TINTA, "m0", esp=3))
    p.append(caixa(750, y, 240, 68, c, ct, esp=3))
    rs.append(rot(750, y + 18, t, w=240, tam=26, cor=TINTA, peso=600, alinha="center"))
    p.append(seta(996, y + 34, 1068, 150, TINTA, "m0", esp=3))
p.append(caixa(1080, 90, 260, 120, OXID, OXID_T, esp=4))
rs.append(rot(1080, 116, "motivação autônoma", w=260, tam=28, cor=OXID, peso=700, alinha="center"))
p.append(seta(1346, 150, 1400, 150, TINTA, "m0", esp=3))
p.append(caixa(1410, 70, 254, 160, TINTA, CARTAO, esp=3))
rs.append(rot(1410, 94, "persistência, desempenho, bem-estar", w=254, tam=26, cor=TINTA, peso=600, alinha="center"))
# caminho controlador
yb = 400
for i, (t, x) in enumerate([("cobrança, prêmio, ameaça", 330), ("necessidades frustradas", 750), ("motivação controlada", 1080), ("abandono", 1410)]):
    ww = 254 if x == 1410 else (330 if x == 330 else 260 if x == 1080 else 240)
    p.append(caixa(x, yb, ww, 90, FOSF, FOSF_T, esp=3))
    rs.append(rot(x, yb + 28, t, w=ww, tam=24, cor=FOSF, peso=700, alinha="center"))
    if i < 3:
        nxt = [750, 1080, 1410][i]
        p.append(seta(x + ww + 6, yb + 45, nxt - 8, yb + 45, FOSF, "m1", esp=3))
p.append("</svg>")
S.append({"id": "cascata", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro dois", "titulo": "Controlar funciona na semana e cobra no ano",
          "fonte": "Modelo motivacional da relação técnico e atleta, J Sports Sci 2003"})

# 5. autoeficácia: nuvem e correspondência
random.seed(7)
pts = []
while True:
    pts = []
    for _ in range(46):
        a = random.gauss(0, 1)
        b = 0.38 * a + math.sqrt(1 - 0.38 ** 2) * random.gauss(0, 1)
        pts.append((a, b))
    mx = sum(a for a, _ in pts) / len(pts); my = sum(b for _, b in pts) / len(pts)
    sxy = sum((a - mx) * (b - my) for a, b in pts); sx = sum((a - mx) ** 2 for a, _ in pts); sy = sum((b - my) ** 2 for _, b in pts)
    r = sxy / math.sqrt(sx * sy)
    if abs(r - 0.38) < 0.02:
        break
W, H, ox, oy = 820, 440, 60, 20
fx = lambda a: ox + (a + 2.6) / 5.2 * (W - ox - 20)
fy = lambda b: oy + (2.6 - b) / 5.2 * (H - oy - 60)
p = [svg_abre(1664, 460, "Esquema: nuvem de pontos com correlação próxima de 0,38 entre autoeficácia e desempenho; ao lado, a relação fica mais forte quando a pergunta corresponde à tarefa medida")]
p.append(f'<line x1="{ox}" y1="{H-40}" x2="{W}" y2="{H-40}" stroke="{MUDO}" stroke-width="2"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="{H-40}" stroke="{MUDO}" stroke-width="2"/>')
for a, b in pts:
    p.append(f'<circle cx="{fx(max(-2.5,min(2.5,a))):.1f}" cy="{fy(max(-2.5,min(2.5,b))):.1f}" r="9" fill="{AZUL}" fill-opacity="0.7"/>')
sl = sxy / sx
p.append(f'<line x1="{fx(-2.4):.1f}" y1="{fy(my + sl*(-2.4-mx)):.1f}" x2="{fx(2.4):.1f}" y2="{fy(my + sl*(2.4-mx)):.1f}" stroke="{TINTA}" stroke-width="5"/>')
# painel da correspondência
bx = 960
p.append(caixa(bx, 110, 700, 330, "#DDD8CC", CARTAO, esp=2))
p.append(f'<rect x="{bx+40}" y="240" width="220" height="30" rx="6" fill="{AZUL}" fill-opacity="0.45"/>')
p.append(f'<rect x="{bx+40}" y="360" width="560" height="30" rx="6" fill="{AZUL}"/>')
p.append("</svg>")
rs = [rot(ox, H - 30, "autoeficácia →", w=300, tam=24, cor=MUDO),
      rot(0, oy, "desempenho ↑", w=200, tam=24, cor=MUDO),
      rot(bx, 10, "r = 0,38", w=700, tam=64, cor=TINTA, peso=700, serif=True),
      rot(bx + 40, 130, "O moderador mais forte: a pergunta bate com a tarefa?", w=620, tam=26, cor=TINTA, peso=700),
      rot(bx + 40, 202, "“Você se sente confiante?”", w=620, tam=26, cor=APOIO2),
      rot(bx + 280, 240, "relação mais fraca", w=320, tam=24, cor=AZUL, peso=600),
      rot(bx + 40, 318, "“De 0 a 10, sobe a serra em 20 minutos?”", w=640, tam=26, cor=TINTA),
      rot(bx + 40, 400, "relação mais forte", w=320, tam=24, cor=AZUL, peso=700)]
S.append({"id": "nuvem", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro três", "titulo": "Autoeficácia é sobre esta tarefa, e prevê desempenho",
          "fonte": "Esquema: nuvem desenhada com correlação próxima de 0,38 · metanálise de 45 estudos, Res Q Exerc Sport 2000 · Bandura, 1977"})

# 6. as quatro fontes
fontes = [("h:award-trophy", "Ter conseguido antes", "já subiu serra parecida neste ritmo", 26, OXID),
          ("t:eye", "Ver alguém parecido", "o colega da mesma idade subiu", 17, OXID),
          ("t:message-circle", "Ouvir que consegue", "“você é fera”", 10, GLIC),
          ("t:heartbeat", "Ler o próprio corpo", "coração acelerado: pronto ou perdido?", 5, GLIC)]
p = [svg_abre(1664, 520, "Quatro fontes de autoeficácia, com setas de espessura decrescente: experiência de domínio, experiência vicária, persuasão verbal e estados fisiológicos"), defs(OXID, GLIC)]
rs = []
for i, (ic, t, x, esp, c) in enumerate(fontes):
    y = 20 + i * 125
    p.append(icone(ic, 0, y + 6, 72, c))
    rs.append(rot(96, y, t, w=560, tam=32, cor=TINTA, peso=700))
    rs.append(rot(96, y + 44, x, w=640, tam=26, cor=APOIO2))
    cy = y + 40
    p.append(f'<path d="M780 {cy} C 1000 {cy}, 1080 260, 1250 260" fill="none" stroke="{c}" stroke-width="{esp}" stroke-linecap="round"/>')
p.append(f'<circle cx="1420" cy="260" r="180" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>')
p.append("</svg>")
rs += [rot(1260, 226, "Autoeficácia", w=320, tam=40, cor=OXID, peso=700, alinha="center", serif=True),
       rot(0, 500 - 10, "", w=10, tam=24)]
rs = rs[:-1]
S.append({"id": "fontes", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As quatro fontes", "titulo": "A frase de incentivo é a fonte mais fraca",
          "fonte": "Ordem de força proposta por Bandura · espessura das linhas ilustrativa"})

# 7. onde regular a emoção
xs = [i for i in range(0, 61)]
emo = [(x, 0.12 + 0.8 / (1 + math.exp(-(x - 38) / 7))) for x in xs]
def pontos(fx, fy):
    out = ""
    for x, c in [(6, OXID), (16, OXID), (28, OXID), (40, OXID), (54, FOSF)]:
        out += f'<line x1="{fx(x):.1f}" y1="{fy(0):.1f}" x2="{fx(x):.1f}" y2="{fy(1.05):.1f}" stroke="{c}" stroke-width="2" stroke-dasharray="6 6"/>'
    return out
svg, rs = linhas(1664, 470, "Esquema: a intensidade da emoção sobe na hora antes da largada; cinco pontos onde é possível regular, o último deles com a emoção já no alto",
    [{"nome": "", "cor": TINTA, "pts": emo, "marcas": [(54, 0.12 + 0.8 / (1 + math.exp(-(54 - 38) / 7)))]}],
    0, 60, 0, 1.1, [(0, "1 h antes"), (30, "30 min"), (60, "largada")], [], yfmt=lambda v: "",
    margem=(20, 110, 60, 30), extra=pontos)
etq = [(6, "escolher a situação"), (16, "modificar a situação"), (28, "direcionar a atenção"), (40, "reavaliar o sentido"), (54, "suprimir a resposta")]
fx = lambda v: 20 + v / 60 * (1664 - 50)
for x, t in etq:
    rs.append(rot(fx(x) - 130, 0, t, w=260, tam=24, cor=FOSF if x == 54 else OXID, peso=700, alinha="center"))
rs += [rot(fx(54) - 330, 150, "“engole o choro”", w=300, tam=30, cor=FOSF, peso=700, alinha="right", serif=True),
       rot(40, 300, "intensidade da emoção", w=320, tam=22, cor=MUDO)]
S.append({"id": "curva", "tipo": "diagrama", "h": 470, "svg": svg, "rotulos": rs,
          "eyebrow": "Erro quatro", "titulo": "Mandar engolir a emoção é regular tarde demais",
          "fonte": "Esquema, sem valores medidos · modelo de processo da regulação emocional, James Gross, 1998"})

# 8. reavaliar contra suprimir
linhas_ = [("emoção positiva", 1, -1), ("emoção negativa", -1, 1), ("funcionamento nas relações", 1, -1), ("bem-estar", 1, -1)]
p = [svg_abre(1664, 470, "Quem reavalia com frequência relata mais emoção positiva, menos negativa, melhores relações e mais bem-estar; quem suprime, o contrário")]
rs = [rot(700, 0, "Quem reavalia", w=380, tam=32, cor=OXID, peso=700, alinha="center", serif=True),
      rot(1200, 0, "Quem suprime", w=380, tam=32, cor=FOSF, peso=700, alinha="center", serif=True)]
def flecha(cx, cy, cima, cor):
    s = 1 if cima else -1
    return (f'<path d="M{cx} {cy - 32*s} L{cx - 34} {cy + 4*s} H{cx - 14} V{cy + 34*s} H{cx + 14} V{cy + 4*s} H{cx + 34} Z" fill="{cor}"/>')
for i, (t, a, b) in enumerate(linhas_):
    y = 110 + i * 92
    p.append(f'<rect x="0" y="{y - 40}" width="1664" height="80" rx="10" fill="{CARTAO if i % 2 == 0 else "#F1EEE6"}"/>')
    rs.append(rot(30, y - 20, t, w=640, tam=30, cor=TINTA, peso=600))
    bom_a = (a == 1) != (t == "emoção negativa")
    bom_b = (b == 1) != (t == "emoção negativa")
    p.append(flecha(890, y, a == 1, OXID if bom_a else FOSF))
    p.append(flecha(1390, y, b == 1, OXID if bom_b else FOSF))
p.append("</svg>")
S.append({"id": "setas", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O custo de suprimir", "titulo": "Reavaliar e esconder não custam o mesmo",
          "destaque": "Cinco estudos com estudantes, e é associação. Em vez de “não fica nervoso”: “o que esse nervosismo está te dizendo?”",
          "destaque_cor": "tinta", "fonte": "J Pers Soc Psychol 2003"})

# 9. os dois ciclos
def ciclo(cx, cy, r, nos, cor, ct, mk):
    out, rr = [], []
    k = len(nos)
    for i in range(k):
        a1, a2 = -90 + 360 * i / k + 22, -90 + 360 * (i + 1) / k - 22
        A1, A2 = math.radians(a1), math.radians(a2)
        out.append(f'<path d="M{cx + r*math.cos(A1):.1f} {cy + r*math.sin(A1):.1f} A{r} {r} 0 0 1 {cx + r*math.cos(A2):.1f} {cy + r*math.sin(A2):.1f}" fill="none" stroke="{cor}" stroke-width="5" marker-end="url(#{mk})"/>')
    for i, t in enumerate(nos):
        a = math.radians(-90 + 360 * i / k)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="16" fill="{cor}"/>')
        dx = math.cos(a)
        if abs(dx) < 0.3:
            rr.append(rot(px - 170, py - 58 if py < cy else py + 22, t, w=340, tam=26, cor=TINTA, peso=600, alinha="center"))
        elif dx > 0:
            rr.append(rot(px + 26, py - 18, t, w=250, tam=26, cor=TINTA, peso=600))
        else:
            rr.append(rot(px - 276, py - 18, t, w=250, tam=26, cor=TINTA, peso=600, alinha="right"))
    return out, rr
p = [svg_abre(1664, 520, "Dois ciclos: o que se sustenta, com apoio à autonomia levando a persistência; e o que se fecha, com controle levando a abandono lido como falta de motivação"), defs(OXID, FOSF)]
a1, r1 = ciclo(400, 270, 170, ["apoio à autonomia", "necessidades atendidas", "motivação autônoma", "persiste e melhora"], OXID, OXID_T, "m0")
a2, r2 = ciclo(1260, 270, 170, ["controle", "necessidades frustradas", "abandono", "“falta de motivação”"], FOSF, FOSF_T, "m1")
p += a1 + a2
p.append("</svg>")
rs = r1 + r2 + [rot(250, 250, "se alimenta", w=300, tam=28, cor=OXID, peso=700, alinha="center", serif=True),
                rot(1110, 250, "se fecha", w=300, tam=28, cor=FOSF, peso=700, alinha="center", serif=True)]
S.append({"id": "ciclos", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro cinco", "titulo": "Motivação não vem da palestra. Vem do ciclo de todo dia",
          "fonte": "A partir do modelo da relação técnico e atleta, J Sports Sci 2003"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Motivação, autoeficácia e regulação emocional", "titulo": "“Sentimos sua falta no sábado. O que mudou?”",
          "regras": ["Motivação tem tipo, e o tipo muda com o ambiente",
                     "Autoeficácia se constrói com sucesso em tarefas calibradas",
                     "Reavaliar a emoção ajuda mais que suprimir"],
          "cards": [{"ic": "t:users", "t": "Quem conduz o treino", "x": "Mexe nas três necessidades todo dia."},
                    {"ic": "h:doctor", "t": "Médico e fisioterapia", "x": "Uma escolha, um progresso visível, um vínculo, em cada consulta."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Quando a emoção atrapalha o desempenho ou a vida."}]})

spec = {"arquivo": "aulas/MOD10/10-01-motivacao-autoeficacia-e-regulacao-emocional.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Motivação, autoeficácia e regulação emocional", "subtitulo": "Cinco erros de quem tenta motivar",
        "nota_capa": "Entra pela mensagem do treinador no grupo do ciclismo.",
        "secoes": {"regua": ["Motivação tem tipo.", "capa"], "cascata": ["Controle e autoeficácia.", "cascata"],
                   "curva": ["Regulação emocional.", "curva"], "ciclos": ["O ciclo de todo dia.", "ciclos"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-01.json"), "w"), ensure_ascii=False, indent=1)
print("10-01.json:", len(S), "slides")
