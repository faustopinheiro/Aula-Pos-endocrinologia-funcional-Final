"""Spec do deck 10.3. Gera 10-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"

# 1. 0,83
p = [svg_abre(1664, 460, "Chance de desenvolver depressão: 1,00 com atividade física baixa, 0,83 com atividade alta; a barra encolhe, mas não some")]
p.append(f'<rect x="0" y="120" width="900" height="90" rx="10" fill="{GRADE}"/>')
p.append(f'<rect x="0" y="280" width="{900*0.83:.0f}" height="90" rx="10" fill="{OXID}"/>')
p.append(f'<line x1="{900*0.83:.0f}" y1="250" x2="{900*0.83:.0f}" y2="400" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 8"/>')
p.append(icone("t:shield", 1180, 90, 300, OXID_T))
p.append(icone("t:shield-check", 1230, 140, 200, OXID))
p.append("</svg>")
rs = [rot(0, 76, "atividade física baixa", w=600, tam=28, cor=TINTA, peso=600),
      rot(920, 140, "1,00", w=200, tam=44, cor=MUDO, peso=700, serif=True),
      rot(0, 236, "atividade física alta", w=600, tam=28, cor=TINTA, peso=600),
      rot(772, 292, "0,83", w=200, tam=56, cor=OXID, peso=700, serif=True),
      rot(0, 400, "chance de desenvolver depressão, relativa", w=900, tam=24, cor=MUDO),
      rot(1080, 360, "menos risco, não risco zero", w=500, tam=32, cor=OXID, peso=700, alinha="center", serif=True)]
S.append({"id": "cinto", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mito do atleta blindado", "titulo": "Proteção parcial não é imunidade",
          "fonte": "49 estudos prospectivos, 266.939 pessoas; razão de chances ajustada 0,83 (0,79 a 0,88) · Am J Psychiatry 2018"})

# 2. um terço
p = [svg_abre(1664, 520, "Grade de cem atletas com um terço destacado: sintomas de ansiedade ou depressão em atletas de elite em atividade")]
for i in range(100):
    x, y = (i % 10) * 54, (i // 10) * 52
    p.append(icone("h:person", x, y, 46, FOSF if i < 33 else "#C9CFD4"))
p.append(f'<line x1="640" y1="0" x2="640" y2="520" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(700, 0, "≈ 1 em 3", w=900, tam=96, cor=FOSF, peso=700, serif=True),
      rot(700, 120, "atletas de elite em atividade com sintomas de ansiedade ou depressão", w=900, tam=30, cor=TINTA, peso=600),
      rot(700, 230, "19,6%", w=400, tam=56, cor=GLIC, peso=700, serif=True),
      rot(960, 244, "com sofrimento psíquico", w=640, tam=28, cor=TINTA),
      rot(700, 330, "16 a 34%", w=400, tam=56, cor=AZUL, peso=700, serif=True),
      rot(1010, 344, "faixa das condições estudadas", w=600, tam=28, cor=TINTA),
      rot(700, 430, "Risco comparável ao da população geral. Comparável, não menor.", w=940, tam=28, cor=OXID, peso=700)]
S.append({"id": "terco", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número central", "titulo": "Um terço",
          "fonte": "Sintoma relatado não é diagnóstico · metanálise, Br J Sports Med 2019 · revisão de 60 estudos, Sports Med 2016"})

# 3. rede de apoio
p = [svg_abre(1664, 520, "O atleta de elite carrega os estressores do esporte com uma rede de apoio embaixo; o amador carrega os mesmos e os da vida, sem rede")]
rs = []
for k, (cx, rede, pesos) in enumerate([(380, True, ["lesão", "resultado", "corpo"]), (1240, False, ["lesão", "resultado", "corpo", "trabalho", "dinheiro", "família"])]):
    for j, t in enumerate(pesos):
        col, lin = j % 3, j // 3
        x, y = cx - 250 + col * 170, 20 + lin * 70
        c = FOSF if j < 3 else GLIC
        p.append(f'<rect x="{x}" y="{y}" width="160" height="58" rx="10" fill="{FOSF_T if j < 3 else GLIC_T}" stroke="{c}" stroke-width="3"/>')
        rs.append(rot(x, y + 14, t, w=160, tam=24, cor=TINTA, peso=600, alinha="center"))
    p.append(icone("h:running", cx - 90, 170, 180, TINTA))
    if rede:
        p.append(f'<path d="M{cx-280} 380 Q {cx} 470 {cx+280} 380" fill="none" stroke="{OXID}" stroke-width="6"/>')
        for dx in range(-240, 260, 60):
            yy = 380 + 90 * (1 - (dx / 280) ** 2) * 0.55
            p.append(f'<line x1="{cx+dx}" y1="380" x2="{cx+dx}" y2="{yy:.0f}" stroke="{OXID}" stroke-width="2"/>')
        rs.append(rot(cx - 300, 450, "médico · psicólogo · afastamento remunerado", w=600, tam=24, cor=OXID, peso=700, alinha="center"))
    else:
        p.append(f'<line x1="{cx-280}" y1="420" x2="{cx+280}" y2="420" stroke="{FOSF}" stroke-width="3" stroke-dasharray="10 10"/>')
        rs.append(rot(cx - 300, 450, "sem rede", w=600, tam=26, cor=FOSF, peso=700, alinha="center"))
p.append(f'<line x1="810" y1="20" x2="810" y2="500" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs += [rot(40, 200, "Elite", w=200, tam=40, cor=TINTA, peso=700, serif=True),
       rot(1440, 200, "Amador", w=220, tam=40, cor=TINTA, peso=700, serif=True)]
S.append({"id": "rede", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "E o nosso público", "titulo": "O amador carrega mais, e sem rede",
          "fonte": "Consenso do Comitê Olímpico Internacional sobre saúde mental em atletas de elite, Br J Sports Med 2019"})

# 4. seis estressores
p = [svg_abre(1664, 560, "Seis estressores próprios de quem treina convergindo para uma figura no centro, com a lesão desenhada maior"), defs(MUDO)]
cx, cy = 832, 290
p.append(f'<circle cx="{cx}" cy="{cy}" r="95" fill="{AZUL_T}"/>')
p.append(icone("h:person", cx - 60, cy - 60, 120, TINTA))
est = [("lesão", "h:bandaged", FOSF, 110, 0), ("transição e perda de papel", "t:door-exit", GLIC, 72, 1),
       ("pressão de desempenho", "t:gauge", GLIC, 72, 2), ("imagem corporal", "t:scale", AZUL, 72, 3),
       ("identidade só de atleta", "t:user", AZUL, 72, 4), ("carga de vida", "t:briefcase", OXID, 72, 5)]
rs = []
for t, ic, c, r, i in est:
    a = math.radians(-90 + i * 60)
    px, py = cx + 360 * math.cos(a) * 1.25, cy + 178 * math.sin(a)
    p.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r}" fill="{CARTAO}" stroke="{c}" stroke-width="{6 if r > 80 else 4}"/>')
    p.append(icone(ic, px - r * 0.55, py - r * 0.55, r * 1.1, c))
    ex, ey = cx + 120 * math.cos(a) * 1.1, cy + 110 * math.sin(a)
    sx, sy = px - (r + 10) * math.cos(a), py - (r + 10) * math.sin(a)
    p.append(seta(f"{sx:.0f}", f"{sy:.0f}", f"{ex:.0f}", f"{ey:.0f}", MUDO, "m0", esp=3))
    if math.cos(a) > 0.3:
        rs.append(rot(px + r + 14, py - 18, t, w=300, tam=26, cor=TINTA, peso=700))
    elif math.cos(a) < -0.3:
        rs.append(rot(px - r - 314, py - 18, t, w=300, tam=26, cor=TINTA, peso=700, alinha="right"))
    else:
        rs.append(rot(px + r + 14, py - 18, t, w=260, tam=28 if r > 80 else 26, cor=FOSF if r > 80 else TINTA, peso=700))
p.append("</svg>")
S.append({"id": "estressores", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde está o risco", "titulo": "Seis estressores próprios de quem treina",
          "fonte": "“Quem você é quando não está treinando?” rastreia a identidade só de atleta"})

# 5. escalas
p = [svg_abre(1664, 470, "Prevalência de depressão: na escala de sintomas masculinos, 26,3% dos homens e 21,9% das mulheres; na escala combinada, 30,6% e 33,3%, sem diferença")]
grupos = [("Escala de sintomas masculinos", 26.3, 21.9), ("Escala combinada: a diferença some", 30.6, 33.3)]
base, esc = 380, 9
rs = []
for g, (t, hm, mu) in enumerate(grupos):
    x = 120 + g * 780
    for k, (v, c, lab) in enumerate([(hm, AZUL, "homens"), (mu, GLIC, "mulheres")]):
        xx = x + k * 250
        p.append(f'<rect x="{xx}" y="{base - v*esc:.0f}" width="210" height="{v*esc:.0f}" rx="8" fill="{c}"/>')
        rs.append(rot(xx, base - v * esc - 56, f"{v:.1f}%".replace(".", ","), w=210, tam=40, cor=c, peso=700, alinha="center", serif=True))
        rs.append(rot(xx, base + 10, lab, w=210, tam=26, cor=TINTA, peso=600, alinha="center"))
    rs.append(rot(x - 40, base + 52, t, w=540, tam=28, cor=TINTA, peso=700, alinha="center"))
p.append(f'<line x1="60" y1="{base}" x2="1640" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
S.append({"id": "escalas", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O homem invisível ao instrumento", "titulo": "Raiva, bebida e risco também são depressão",
          "destaque": "Ao lado de “você tem se sentido triste?”: “você tem se irritado mais do que o normal?”", "destaque_cor": "tinta",
          "fonte": "Pesquisa populacional americana, JAMA Psychiatry 2013"})

# 6. funil
p = [svg_abre(1664, 520, "Funil: entram queixas físicas de desempenho, recuperação, perda de prazer e aumento do treino; passam pelo diferencial de carga, energia, sono e causas clínicas; sai a hipótese de saúde mental no topo"), defs(TINTA)]
p.append(f'<path d="M0 30 H1060 L720 300 H340 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(f'<rect x="340" y="310" width="380" height="80" rx="12" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
p.append(seta(530, 396, 530, 430, TINTA, "m0"))
p.append(f'<rect x="300" y="436" width="460" height="74" rx="37" fill="{FOSF}"/>')
queixas = [("h:running", "“não rendo”"), ("t:battery-1", "“não recupero”"), ("t:mood-empty", "“perdi a vontade”"), ("t:trending-up", "treina cada vez mais")]
rs = []
for i, (ic, t) in enumerate(queixas):
    x = 120 + i * 220
    p.append(icone(ic, x + 65, 46, 64, AZUL))
    rs.append(rot(x, 120, t, w=200, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(icone("t:mood-empty", 1180, 120, 280, "#C9CFD4"))
p.append("</svg>")
rs += [rot(340, 322, "diferencial: carga, energia, sono, causas clínicas", w=380, tam=22, cor=TINTA, peso=600, alinha="center"),
       rot(300, 456, "saúde mental no topo", w=460, tam=28, cor="#F7F6F2", peso=700, alinha="center"),
       rot(1080, 420, "“você ainda gosta de treinar?”", w=560, tam=30, cor=TINTA, peso=700, alinha="center", serif=True)]
S.append({"id": "funil", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As máscaras esportivas", "titulo": "O sofrimento chega com queixa física",
          "fonte": "O excesso de treinamento está no módulo de endocrinologia; as causas clínicas, no de medicina esportiva clínica"})

# 7. o coração
p = [svg_abre(1664, 440, "Dois passos: investigar o coração sempre; depois de um exame normal, não parar em não é o coração"), defs(TINTA)]
p.append(caixa(0, 60, 700, 300, FOSF, FOSF_T, esp=5))
p.append(icone("t:heartbeat", 40, 110, 170, FOSF))
p.append(seta(710, 210, 900, 210, TINTA, "m0", esp=6))
p.append(caixa(920, 60, 744, 300, OXID, OXID_T, esp=5))
p.append(icone("t:message-circle", 960, 110, 150, OXID))
p.append("</svg>")
rs = [rot(230, 90, "1 · Investigar o coração", w=450, tam=34, cor=FOSF, peso=700, serif=True),
      rot(230, 150, "taquicardia, falta de ar, aperto no peito, tontura, sensação de morte: sempre levado a sério", w=450, tam=26, cor=TINTA, lh=1.35),
      rot(1130, 90, "2 · Não parar no exame normal", w=520, tam=34, cor=OXID, peso=700, serif=True),
      rot(1130, 150, "“não é o coração” é metade da resposta; a outra metade é explicar e tratar a ansiedade", w=500, tam=26, cor=TINTA, lh=1.35),
      rot(0, 386, "ansiedade e depressão andam juntas: rastrear uma sem a outra deixa metade do quadro de fora", w=1664, tam=26, cor=TINTA, peso=600, alinha="center")]
S.append({"id": "coracao", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A ansiedade que parece o coração", "titulo": "Os dois passos vão juntos",
          "fonte": "Triagem de sintoma cardíaco no esforço: módulo de medicina esportiva clínica"})

# 8. a semana
p = [svg_abre(1664, 520, "Semana de um atleta amador: o preparador físico aparece três vezes, o fisioterapeuta duas, o nutricionista uma vez por mês e o médico uma vez por ano")]
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
prof = [("Preparador físico", "t:users", [0, 2, 4], OXID), ("Fisioterapeuta", "t:first-aid-kit", [1, 3], AZUL),
        ("Nutricionista", "t:salad", [], GLIC), ("Médico", "h:doctor", [], FOSF)]
x0, cw = 480, 160
rs = []
for j, d in enumerate(dias):
    rs.append(rot(x0 + j * cw, 0, d, w=cw, tam=24, cor=MUDO, peso=600, alinha="center"))
for i, (n, ic, ds, c) in enumerate(prof):
    y = 60 + i * 95
    p.append(f'<rect x="0" y="{y}" width="1664" height="80" rx="10" fill="{CARTAO if i % 2 == 0 else "#F1EEE6"}"/>')
    p.append(icone(ic, 16, y + 12, 56, c))
    rs.append(rot(90, y + 22, n, w=380, tam=28, cor=TINTA, peso=700))
    for d in ds:
        p.append(f'<circle cx="{x0 + d*cw + cw/2:.0f}" cy="{y+40}" r="24" fill="{c}"/>')
    if n == "Nutricionista":
        rs.append(rot(x0, y + 24, "uma vez por mês", w=1100, tam=26, cor=GLIC, peso=600))
    if n == "Médico":
        rs.append(rot(x0, y + 24, "uma vez por ano, se tanto", w=1100, tam=26, cor=FOSF, peso=600))
p.append("</svg>")
rs.append(rot(0, 470, "Quem vê a mudança primeiro é quem está mais perto.", w=1664, tam=28, cor=TINTA, peso=700, alinha="center", serif=True))
S.append({"id": "semana", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por que é de toda a equipe", "titulo": "Rastrear e acolher é de todos. Tratar, não",
          "destaque": "E a tarefa comum que não exige formação: não piorar. Nem “frescura”, nem “treina que passa”.", "destaque_cor": "verm",
          "fonte": "Semana ilustrativa"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Saúde mental no rendimento", "titulo": "“Como você está fora da piscina?”",
          "regras": ["0,83: proteção parcial, não imunidade",
                     "Um terço, e o homem invisível ao instrumento",
                     "Quatro máscaras físicas; o coração investigado, e não só ele"],
          "cards": [{"ic": "t:users", "t": "Quem treina e reabilita", "x": "Vê primeiro, pergunta de outro jeito, encaminha."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Investiga o que precisa, e não para no exame normal."},
                    {"ic": "h:psychology", "t": "Psicologia e psiquiatria", "x": "Diagnosticam e tratam."}]})

spec = {"arquivo": "aulas/MOD10/10-03-saude-mental-no-rendimento-prevalencia-e-risco.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Saúde mental no rendimento", "subtitulo": "Prevalência e risco",
        "nota_capa": "Entra por uma nadadora que chora no carro depois do treino.",
        "secoes": {"cinto": ["O mito e o número central.", "capa"], "estressores": ["Onde está o risco.", "estressores"],
                   "funil": ["As máscaras e o coração.", "funil"], "semana": ["De quem é o tema.", "semana"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-03.json"), "w"), ensure_ascii=False, indent=1)
print("10-03.json:", len(S), "slides")
