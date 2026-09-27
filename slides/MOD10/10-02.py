"""Spec do deck 10.2. Gera 10-02.json ao lado deste arquivo."""
import json, math, os, sys
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

# 1. o peso da cobrança
p = [svg_abre(1664, 480, "Vista de cima do gol e da marca do pênalti; ao lado, barras esquemáticas de acerto que diminuem da cobrança que não decide para a cobrança em que o erro dá a derrota")]
p.append(f'<rect x="40" y="30" width="560" height="420" rx="10" fill="#E4EFE6"/>')
p.append(f'<rect x="160" y="30" width="320" height="110" fill="none" stroke="{PAPEL}" stroke-width="6"/>')
p.append(f'<rect x="230" y="30" width="180" height="40" fill="none" stroke="{PAPEL}" stroke-width="6"/>')
p.append(f'<rect x="250" y="14" width="140" height="16" fill="{TINTA}"/>')
p.append(f'<circle cx="320" cy="230" r="10" fill="{PAPEL}"/><circle cx="320" cy="230" r="22" fill="none" stroke="{TINTA}" stroke-width="5"/>')
p.append(icone("t:ball-football", 298, 208, 44, TINTA))
barras = [("não decide", 300, OXID), ("gol dá a vitória", 270, GLIC), ("erro dá a derrota", 190, FOSF)]
rs = []
for i, (t, h, c) in enumerate(barras):
    x = 780 + i * 290
    p.append(f'<rect x="{x}" y="{400 - h}" width="200" height="{h}" rx="8" fill="{c}"/>')
    rs.append(rot(x - 40, 412, t, w=280, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append(f'<line x1="740" y1="400" x2="1640" y2="400" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs += [rot(740, 40, "acerto nas disputas", w=400, tam=24, cor=MUDO),
       rot(40, 300, "o mesmo pé da semana inteira", w=560, tam=28, cor=TINTA, peso=700, alinha="center", serif=True)]
S.append({"id": "peso", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Disputa de pênaltis", "titulo": "O pé é o mesmo. O peso da cobrança não",
          "fonte": "Esquema, sem valores medidos · J Sports Sci 2007 · J Sport Exerc Psychol 2008 (36 disputas, 359 cobranças)"})

# 2. U invertido contra zonas individuais
p = [svg_abre(1664, 500, "À esquerda, a curva em U invertido, igual para todos; à direita, três atletas com zonas ótimas em alturas diferentes de ativação e os pontos das melhores e piores atuações de um deles")]
xs = [i / 50 for i in range(0, 51)]
pts = " ".join(f"{40 + x*560:.1f},{400 - 320*math.exp(-((x-0.5)/0.22)**2):.1f}" for x in xs)
p.append(f'<line x1="40" y1="400" x2="600" y2="400" stroke="{MUDO}" stroke-width="2"/><line x1="40" y1="60" x2="40" y2="400" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<polyline points="{pts}" fill="none" stroke="{TINTA}" stroke-width="6"/>')
rs = [rot(40, 412, "ativação →", w=300, tam=24, cor=MUDO), rot(52, 50, "desempenho", w=260, tam=24, cor=MUDO),
      rot(40, 450, "Uma curva para todos", w=560, tam=30, cor=TINTA, peso=700, alinha="center", serif=True)]
atl = [("Atleta A", 0.62, 0.85, OXID), ("Atleta B", 0.15, 0.40, GLIC), ("Atleta C", 0.40, 0.62, AZUL)]
x0, x1 = 900, 1640
for i, (n, a, b, c) in enumerate(atl):
    y = 80 + i * 120
    p.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{GRADE}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<rect x="{x0 + a*(x1-x0):.0f}" y="{y-22}" width="{(b-a)*(x1-x0):.0f}" height="44" rx="22" fill="{c}" fill-opacity="0.35" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(720, y - 20, n, w=160, tam=28, cor=TINTA, peso=700, alinha="right"))
for v in [0.66, 0.71, 0.74, 0.79, 0.81]:
    p.append(f'<circle cx="{x0 + v*(x1-x0):.0f}" cy="80" r="9" fill="{OXID}"/>')
for v in [0.30, 0.95]:
    p.append(f'<circle cx="{x0 + v*(x1-x0):.0f}" cy="80" r="9" fill="{FOSF}"/>')
p.append("</svg>")
rs += [rot(x0, 380, "0", w=40, tam=24, cor=MUDO), rot(x1 - 40, 380, "10", w=40, tam=24, cor=MUDO, alinha="right"),
       rot(x0 + 60, 380, "ativação antes do jogo, de 0 a 10", w=560, tam=24, cor=MUDO, alinha="center"),
       rot(720, 450, "Uma zona para cada um", w=920, tam=30, cor=TINTA, peso=700, alinha="center", serif=True),
       rot(x0, 20, "pontos do atleta A: verde, boas atuações · vermelho, ruins", w=740, tam=22, cor=MUDO)]
S.append({"id": "zona", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo um: ler a ativação", "titulo": "Não existe um nível de ativação ideal para todos",
          "fonte": "Esquema · zonas individuais de funcionamento ótimo (Yuri Hanin) · metanálise, J Sports Sci 1999"})

# 3. desafio ou ameaça
p = [svg_abre(1664, 520, "O mesmo coração acelerado abre duas leituras: desafio, quando os recursos dão conta da exigência, e ameaça, quando a exigência passa dos recursos; a frase estou animado empurra de uma para a outra"), defs(OXID, FOSF, MUDO)]
p.append(f'<circle cx="170" cy="260" r="140" fill="{FOSF_T}"/>')
p.append(icone("t:heartbeat", 80, 170, 180, FOSF))
p.append(f'<path d="M320 230 C 420 150, 460 110, 560 110" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m0)"/>')
p.append(f'<path d="M320 290 C 420 370, 460 410, 560 410" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m1)"/>')
p.append(caixa(580, 40, 460, 140, OXID, OXID_T))
p.append(caixa(580, 340, 460, 140, FOSF, FOSF_T))
p.append(caixa(1100, 40, 564, 140, OXID, CARTAO, esp=2))
p.append(caixa(1100, 340, 564, 140, FOSF, CARTAO, esp=2))
p.append(f'<path d="M800 330 C 760 280, 760 240, 800 192" fill="none" stroke="{MUDO}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#m2)"/>')
p.append("</svg>")
rs = [rot(40, 430, "o mesmo coração acelerado", w=260, tam=24, cor=TINTA, peso=600, alinha="center"),
      rot(600, 60, "Desafio", w=420, tam=36, cor=OXID, peso=700, serif=True),
      rot(600, 112, "os recursos dão conta da exigência", w=420, tam=24, cor=TINTA),
      rot(600, 360, "Ameaça", w=420, tam=36, cor=FOSF, peso=700, serif=True),
      rot(600, 412, "a exigência passa dos recursos", w=420, tam=24, cor=TINTA),
      rot(1124, 58, "mais preciso · emoções favoráveis · olhar mais eficiente · movimento mais econômico", w=520, tam=24, cor=TINTA, lh=1.35),
      rot(1124, 380, "menos preciso · emoções desfavoráveis · olhar e movimento menos eficientes", w=520, tam=24, cor=TINTA, lh=1.35),
      rot(820, 236, "“estou animado”", w=300, tam=28, cor=TINTA, peso=700, serif=True)]
S.append({"id": "leitura", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo dois: reavaliar o sentido", "titulo": "Não tente se acalmar. Mude o nome da ativação",
          "fonte": "Desafio e ameaça, 127 participantes, Psychophysiology 2012 · reavaliar como empolgação, J Exp Psychol Gen 2014"})

# 4. monitoramento explícito
p = [svg_abre(1664, 480, "Em cima, o gesto automatizado como uma seta contínua do canto escolhido à bola no gol; embaixo, o mesmo gesto quebrado em etapas conscientes, com a seta se partindo"), defs(OXID, FOSF)]
p.append(caixa(0, 50, 260, 100, TINTA, CARTAO, esp=3)); p.append(caixa(1404, 50, 260, 100, OXID, OXID_T, esp=3))
p.append(f'<path d="M270 100 C 700 20, 960 180, 1394 100" fill="none" stroke="{OXID}" stroke-width="9" marker-end="url(#m0)"/>')
p.append(caixa(0, 300, 260, 100, TINTA, CARTAO, esp=3)); p.append(caixa(1404, 300, 260, 100, FOSF, FOSF_T, esp=3))
etapas = ["pé de apoio", "joelho", "quadril", "ponto da bola", "força"]
rs = [rot(0, 76, "canto escolhido", w=260, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(1404, 76, "gol", w=260, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(0, 326, "canto escolhido", w=260, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(1404, 326, "erro", w=260, tam=28, cor=FOSF, peso=700, alinha="center"),
      rot(300, 0, "automatizado: roda sem precisar de atenção", w=900, tam=26, cor=OXID, peso=600),
      rot(300, 420, "sob pressão: a atenção volta para cada etapa, e o gesto desmonta", w=1100, tam=26, cor=FOSF, peso=600)]
for i, t in enumerate(etapas):
    x = 300 + i * 214
    p.append(caixa(x, 310, 190, 80, FOSF, CARTAO, esp=2, rx=10))
    rs.append(rot(x, 334, t, w=190, tam=24, cor=TINTA, alinha="center"))
    if i < 4:
        p.append(f'<line x1="{x+192}" y1="350" x2="{x+212}" y2="350" stroke="{FOSF}" stroke-width="4" stroke-dasharray="4 5"/>')
p.append("</svg>")
S.append({"id": "gesto", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo três: a atenção no lugar certo", "titulo": "Pensar no gesto desmonta o gesto automático",
          "destaque": "Antes do pênalti não é hora de corrigir técnica. A técnica se corrige no treino.", "destaque_cor": "tinta",
          "fonte": "Quatro experimentos com tacadas de golfe, J Exp Psychol Gen 2001"})

# 5. olhar quieto
p = [svg_abre(1664, 460, "Linha do tempo dos segundos finais antes do gesto: a última fixação do olhar no alvo é mais longa no grupo que treinou o olhar e continua estável sob pressão")]
x0, x1 = 300, 1620
fx = lambda t: x0 + (t + 3) / 4 * (x1 - x0)
p.append(f'<line x1="{x0}" y1="380" x2="{x1}" y2="380" stroke="{MUDO}" stroke-width="2"/>')
for t in [-3, -2, -1, 0, 1]:
    p.append(f'<line x1="{fx(t):.0f}" y1="380" x2="{fx(t):.0f}" y2="392" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<line x1="{fx(0):.0f}" y1="30" x2="{fx(0):.0f}" y2="380" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 8"/>')
grupos = [("Instrução técnica", "sem pressão", -0.8, 0.2, AZUL, 0.55), ("Instrução técnica", "sob pressão", -0.45, 0.05, AZUL, 0.3),
          ("Treino do olhar", "sem pressão", -1.6, 0.35, OXID, 0.9), ("Treino do olhar", "sob pressão", -1.5, 0.3, OXID, 0.9)]
rs = [rot(fx(0) + 12, 34, "o movimento começa", w=320, tam=24, cor=TINTA, peso=700)]
for i, (g, cnd, a, b, c, op) in enumerate(grupos):
    y = 80 + i * 72
    p.append(f'<rect x="{fx(a):.0f}" y="{y}" width="{fx(b)-fx(a):.0f}" height="44" rx="22" fill="{c}" fill-opacity="{op}"/>')
    rs.append(rot(0, y + 6, f"{g} · {cnd}", w=290, tam=22, cor=TINTA, peso=600 if cnd == "sob pressão" else 400, alinha="right"))
for t, lab in [(-3, "−3 s"), (-2, "−2 s"), (-1, "−1 s"), (0, "0"), (1, "+1 s")]:
    rs.append(rot(fx(t) - 50, 396, lab, w=100, tam=22, cor=MUDO, alinha="center"))
p.append("</svg>")
S.append({"id": "olhar", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo três na prática", "titulo": "A atenção precisa de um lugar: o ponto do alvo",
          "destaque": "Escolher o canto antes de pegar a bola e olhar para esse ponto nos segundos antes da corrida.", "destaque_cor": "petr",
          "fonte": "Esquema, sem valores medidos · 40 participantes, treino do olhar quieto, Psychophysiology 2012"})

# 6. não fugir do momento
p = [svg_abre(1664, 470, "Os dez segundos entre o apito e o chute: um cobrador toma o seu tempo e segue a rotina; o outro desvia o olhar e bate logo depois do apito")]
x0, x1 = 60, 1620
fx = lambda t: x0 + t / 10 * (x1 - x0)
p.append(f'<line x1="{x0}" y1="420" x2="{x1}" y2="420" stroke="{MUDO}" stroke-width="2"/>')
for t in range(0, 11, 2):
    p.append(f'<line x1="{fx(t):.0f}" y1="420" x2="{fx(t):.0f}" y2="432" stroke="{MUDO}" stroke-width="2"/>')
rs = []
for t in range(0, 11, 2):
    rs.append(rot(fx(t) - 50, 436, f"{t} s", w=100, tam=22, cor=MUDO, alinha="center"))
p.append(f'<line x1="{fx(0):.0f}" y1="20" x2="{fx(0):.0f}" y2="420" stroke="{TINTA}" stroke-width="3"/>')
rs.append(rot(fx(0) + 10, 0, "apito", w=120, tam=24, cor=TINTA, peso=700))
eventos_a = [(0.2, 1.8, "respira"), (1.9, 3.8, "olha o goleiro"), (3.9, 5.8, "olha o canto"), (5.9, 7.4, "corre")]
for a, b, t in eventos_a:
    p.append(f'<rect x="{fx(a):.0f}" y="90" width="{fx(b)-fx(a):.0f}" height="70" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    rs.append(rot(fx(a), 110, t, w=fx(b) - fx(a), tam=24, cor=TINTA, peso=600, alinha="center"))
p.append(f'<circle cx="{fx(7.6):.0f}" cy="125" r="18" fill="{OXID}"/>')
rs += [rot(fx(7.6) + 30, 108, "chute", w=160, tam=26, cor=OXID, peso=700),
       rot(x0 + 20, 44, "toma o seu tempo e segue a rotina", w=800, tam=26, cor=OXID, peso=700)]
eventos_b = [(0.1, 0.9, "chão"), (0.9, 1.5, "costas")]
for a, b, t in eventos_b:
    p.append(f'<rect x="{fx(a):.0f}" y="290" width="{fx(b)-fx(a):.0f}" height="70" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(fx(a), 310, t, w=fx(b) - fx(a), tam=22, cor=TINTA, peso=600, alinha="center"))
p.append(f'<circle cx="{fx(1.7):.0f}" cy="325" r="18" fill="{FOSF}"/>')
rs += [rot(fx(1.7) + 30, 308, "chute", w=160, tam=26, cor=FOSF, peso=700),
       rot(x0 + 20, 244, "desvia o olhar e bate logo: alivia por dois segundos", w=900, tam=26, cor=FOSF, peso=700)]
p.append("</svg>")
S.append({"id": "tempo", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo quatro: não fugir do momento", "titulo": "Os segundos depois do apito são a rotina",
          "fonte": "Esquema de tempos ilustrativos · evitação e pior desempenho, J Sport Exerc Psychol 2008 · tempo do apito ao chute, J Sports Sci 2009"})

# 7. a rotina e a escada de pressão
p = [svg_abre(1664, 540, "À esquerda, a rotina pré-desempenho em quatro etapas num ciclo; à direita, uma escada de pressão no treino, do treino sem plateia ao treino filmado com consequência"), defs(TINTA)]
cx, cy, r = 330, 290, 170
etap = [("ler a ativação", "t:gauge", OXID), ("dizer a frase", "t:message-circle", GLIC), ("fixar o canto", "t:target", AZUL), ("executar", "t:ball-football", TINTA)]
rs = []
for i, (t, ic, c) in enumerate(etap):
    a = math.radians(-90 + 90 * i)
    px, py = cx + r * math.cos(a), cy + r * math.sin(a)
    a1, a2 = math.radians(-90 + 90 * i + 22), math.radians(-90 + 90 * (i + 1) - 22)
    p.append(f'<path d="M{cx + r*math.cos(a1):.1f} {cy + r*math.sin(a1):.1f} A{r} {r} 0 0 1 {cx + r*math.cos(a2):.1f} {cy + r*math.sin(a2):.1f}" fill="none" stroke="{MUDO}" stroke-width="4" marker-end="url(#m0)"/>')
    p.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="54" fill="{CARTAO}" stroke="{c}" stroke-width="4"/>')
    p.append(icone(ic, px - 30, py - 30, 60, c))
    if i == 0: rs.append(rot(px - 150, py - 110, t, w=300, tam=26, cor=TINTA, peso=700, alinha="center"))
    elif i == 1: rs.append(rot(px + 66, py - 18, t, w=220, tam=26, cor=TINTA, peso=700))
    elif i == 2: rs.append(rot(px - 150, py + 62, t, w=300, tam=26, cor=TINTA, peso=700, alinha="center"))
    else: rs.append(rot(px - 286, py - 18, t, w=220, tam=26, cor=TINTA, peso=700, alinha="right"))
rs.append(rot(cx - 110, cy - 30, "sempre igual, com o mesmo tempo", w=220, tam=22, cor=MUDO, alinha="center"))
degraus = ["sem plateia", "com o grupo olhando", "filmado, com placar", "com consequência combinada"]
for i, t in enumerate(degraus):
    x, h = 840 + i * 205, 110 + i * 100
    c = [OXID, GLIC, "#C0612F", FOSF][i]
    p.append(f'<rect x="{x}" y="{480 - h}" width="195" height="{h}" rx="8" fill="{c}" fill-opacity="0.85"/>')
    rs.append(rot(x + 6, 480 - h + 12, t, w=183, tam=22, cor="#F7F6F2", peso=700, alinha="center"))
p.append(f'<line x1="830" y1="480" x2="1664" y2="480" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs.append(rot(840, 492, "a pressão sobe no treino, antes de subir no jogo", w=820, tam=24, cor=MUDO))
S.append({"id": "rotina", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Juntar os quatro passos", "titulo": "A rotina só aguenta o jogo se foi treinada sob pressão",
          "fonte": "Treino de autoconsciência protegeu o gesto; treino tranquilo, não (J Exp Psychol Gen 2001) · rotina e escada: prática corrente"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Atenção, ativação e desempenho sob pressão", "titulo": "Quatro passos para o momento que decide",
          "regras": ["Ler a ativação na pessoa, não no livro",
                     "Reavaliar o sentido e pôr a atenção no alvo",
                     "Tomar o próprio tempo, com a rotina treinada sob pressão"],
          "cards": [{"ic": "t:users", "t": "Técnico e preparador", "x": "Montam a escada de pressão no treino."},
                    {"ic": "t:ball-football", "t": "Atleta", "x": "Anota a própria zona e ensaia a rotina."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Quando a ativação foge da zona com frequência."}]})

spec = {"arquivo": "aulas/MOD10/10-02-atencao-ativacao-e-desempenho-sob-pressao.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Atenção, ativação e desempenho sob pressão", "subtitulo": "Quatro passos para o momento que decide",
        "nota_capa": "Entra pelo quinto cobrador de uma disputa de pênaltis.",
        "secoes": {"peso": ["A pressão e a ativação.", "capa"], "leitura": ["A leitura e a atenção.", "leitura"],
                   "tempo": ["O tempo e a rotina.", "tempo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-02.json"), "w"), ensure_ascii=False, indent=1)
print("10-02.json:", len(S), "slides")
