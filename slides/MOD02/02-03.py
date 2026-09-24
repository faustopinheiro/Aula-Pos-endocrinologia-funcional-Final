"""Spec do deck 2.3. Gera 02-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA = "#FDFCF9", "#DDD8CC"

# 1. três frases
p = [svg_abre(1664, 400, "Três frases de beira de quadra riscadas: tirar o ácido lático, lactato acumulado causando dor, massagem que drena")]
rs = []
frases = [("“Pedala leve para tirar o ácido lático.”", "errada pelo motivo"),
          ("“Essa dor de dois dias é o lactato acumulado.”", "errada pelo mecanismo"),
          ("“A massagem drena o ácido lático.”", "errada pelas duas coisas")]
for i, (f, pq) in enumerate(frases):
    x = i * 568
    p.append(f'<rect x="{x}" y="0" width="528" height="260" rx="16" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<line x1="{x+30}" y1="226" x2="{x+498}" y2="40" stroke="{FOSF}" stroke-width="5" stroke-linecap="round" opacity="0.6"/>')
    rs.append(rot(x + 40, 60, f, w=448, tam=36, cor=TINTA, peso=400, serif=True, lh=1.3))
    rs.append(rot(x, 290, pq, w=528, tam=30, cor=FOSF, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "frases", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Ditas todo dia, por gente formada", "titulo": "Três frases, três erros",
          "destaque": "O problema não é o vocabulário. É que esse erro muda a conduta."})

# 2. tudo sobe junto
xs = list(range(0, 101, 4))
lac = [(x, 8 + 84 * (x / 100) ** 3.2) for x in xs]
qu = [(x, 4 + 88 * (x / 100) ** 3.6) for x in xs]
fo = [(x, 2 + 86 * (x / 100) ** 4.0) for x in xs]
svg, rs = linhas(1664, 420, "Com a intensidade subindo, o lactato no sangue, a queimação e a queda de força sobem juntos, quase sobrepostos",
    [{"nome": "", "cor": GLIC, "pts": lac}, {"nome": "", "cor": FOSF, "pts": qu}, {"nome": "", "cor": AZUL, "pts": fo}],
    0, 100, 0, 100, [(0, "leve"), (50, "moderado"), (100, "máximo")], [], margem=(40, 20, 60, 30))
svg = svg.replace("</svg>", "".join(f'<rect x="60" y="{150 + i*48}" width="36" height="6" rx="3" fill="{c}"/>' for i, c in enumerate([GLIC, FOSF, AZUL])) + "</svg>")
rs += [rot(60, 20, "Hill e Meyerhof, Nobel de 1922:<br>boa parte em músculo de rã", w=620, tam=28, cor=TINTA, peso=600),
       rot(110, 136, "lactato no sangue", w=400, tam=26, cor=TINTA, peso=600),
       rot(110, 184, "queimação", w=400, tam=26, cor=TINTA, peso=600),
       rot(110, 232, "queda de força", w=400, tam=26, cor=TINTA, peso=600)]
S.append({"id": "juntos", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "Por que o erro convence", "titulo": "Tudo sobe junto. Junto não é por causa.",
          "fonte": "Esquema, sem valores medidos"})

# 3. de onde vem o combustível
p = [svg_abre(1664, 440, "Fibra muscular com glicogênio dentro e um capilar do lado de fora trazendo glicose; as duas entradas levam à glicólise, e a de dentro tem um passo a menos"),
     "<defs>" + seta_marker("c1", GLIC) + seta_marker("c2", FOSF) + "</defs>",
     f'<rect x="420" y="20" width="1224" height="270" rx="135" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>',
     f'<rect x="420" y="360" width="1224" height="64" rx="32" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>',
     f'<rect x="1250" y="110" width="330" height="90" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>']
import random
random.seed(3)
for _ in range(26):
    cx, cy = 560 + random.random() * 260, 70 + random.random() * 170
    p.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{9 + random.random()*6:.0f}" fill="{GLIC}" opacity="0.8"/>')
for k in range(7):
    p.append(f'<circle cx="{520 + k*90}" cy="392" r="9" fill="{FOSF}"/>')
p.append(f'<path d="M840 150 L1240 150" stroke="{GLIC}" stroke-width="7" marker-end="url(#c1)"/>')
p.append(f'<path d="M1180 360 L1180 300 Q1180 230 1240 185" fill="none" stroke="{FOSF}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#c2)"/>')
p.append("</svg>")
rs = [rot(0, 70, "Glicogênio muscular", w=400, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 112, "de casa: um passo a menos", w=400, tam=26, alinha="right"),
      rot(0, 350, "Glicose do sangue", w=400, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 392, "vem de fora", w=400, tam=26, alinha="right"),
      rot(1250, 136, "Glicólise", w=330, tam=34, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(880, 100, "preferido no esforço intenso", w=340, tam=24, cor=TINTA, peso=600),
      rot(1200, 312, "capilar", w=200, tam=24, cor=FOSF, peso=600)]
S.append({"id": "combustivel", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A glicólise pelo que ela faz", "titulo": "Duas fontes de combustível, e elas não são iguais",
          "destaque": "O glicogênio de dentro da fibra se repõe em horas, com comida. O gel no meio do treino ajuda a glicose do sangue, não enche a fibra.",
          "destaque_cor": "ambar"})

# 4. o plano de velocidade
dem = [(t, 20 + 0.8 * t) for t in range(0, 101, 2)]
TETO = 58
def camadas(fx, fy):
    ox = " ".join(f"{fx(t):.1f},{fy(min(v, TETO)):.1f}" for t, v in dem)
    gl = [(t, v) for t, v in dem if v >= TETO]
    t0 = (TETO - 20) / 0.8
    topo = f"{fx(t0):.1f},{fy(TETO):.1f} " + " ".join(f"{fx(t):.1f},{fy(v):.1f}" for t, v in gl)
    base = " ".join(f"{fx(t):.1f},{fy(TETO):.1f}" for t, v in reversed(gl)) + f" {fx(t0):.1f},{fy(TETO):.1f}"
    return (f'<polygon points="{fx(0):.1f},{fy(0):.1f} {ox} {fx(100):.1f},{fy(0):.1f}" fill="{OXID}" fill-opacity="0.85"/>'
            f'<polygon points="{topo} {base}" fill="{GLIC}" fill-opacity="0.9"/>')
svg, rs = linhas(1664, 420, "A demanda de ATP sobe com a intensidade; a parte que a mitocôndria entrega tem um teto naquele instante, e o que passa do teto é coberto pela glicólise",
    [{"nome": "", "cor": TINTA, "pts": dem, "esp": 4},
     {"nome": "", "cor": TINTA, "pts": [(0, TETO), (100, TETO)], "tracejado": True, "esp": 2}],
    0, 100, 0, 100, [(0, "leve"), (100, "máximo")], [], margem=(40, 20, 60, 30), extra=camadas)
rs += [rot(300, 330, "o que a mitocôndria entrega", w=500, tam=28, cor="#F7F6F2", peso=700),
       rot(1240, 96, "a glicólise cobre<br>a diferença", w=380, tam=26, cor=TINTA, peso=700),
       rot(1000, 40, "demanda de ATP", w=300, tam=26, cor=TINTA, peso=600),
       rot(60, 176, "teto oxidativo naquele instante", w=460, tam=24, cor=MUDO)]
S.append({"id": "velocidade", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "A vantagem dela é a velocidade", "titulo": "Não é o plano B. É o plano de velocidade.",
          "destaque": "Quem abre a torneira é contabilidade local: a via acelera quando os produtos da quebra de ATP se acumulam dentro da fibra.",
          "fonte": "Esquema, sem valores medidos"})

# 5. a fibra rápida entra
lent = [(x, min(55, 55 * x / 45)) for x in range(0, 101, 2)]
rap = [(x, 55 + (0 if x < 50 else 40 * ((x - 50) / 50) ** 1.3)) for x in range(0, 101, 2)]
def areas(fx, fy):
    a = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in lent)
    b = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in rap)
    bl = " ".join(f"{fx(x):.1f},{fy(55):.1f}" for x, y in reversed(rap))
    return (f'<polygon points="{fx(0):.1f},{fy(0):.1f} {a} {fx(100):.1f},{fy(0):.1f}" fill="{OXID}" fill-opacity="0.85"/>'
            f'<polygon points="{b} {bl}" fill="{GLIC}" fill-opacity="0.9"/>')
svg, rs = linhas(1664, 420, "Fibras recrutadas conforme a intensidade: as lentas primeiro, até a intensidade moderada; a partir daí entram as rápidas, e o lactato sobe junto com elas",
    [], 0, 100, 0, 100, [(0, "leve"), (50, "moderado"), (100, "máximo")], [], margem=(40, 20, 60, 30),
    destaques=[{"x": 50}], extra=areas)
rs += [rot(560, 300, "fibras lentas: muita mitocôndria", w=520, tam=28, cor="#F7F6F2", peso=700),
       rot(700, 30, "fibras rápidas: mais maquinaria glicolítica", w=620, tam=28, cor=TINTA, peso=700),
       rot(870, 230, "a partir daqui, o lactato sobe", w=460, tam=26, cor="#F7F6F2", peso=700)]
S.append({"id": "fibras", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "Fibras recrutadas conforme a intensidade", "titulo": "Mais lactato mesmo com oxigênio disponível",
          "destaque": "O lactato sobe porque entrou em cena uma fibra que produz mais lactato, e não porque faltou oxigênio.", "destaque_cor": "verm",
          "fonte": "Esquema, sem valores medidos"})

# 6. bioquímica em três frases
p = [svg_abre(1664, 460, "Glicose vira piruvato; o piruvato vai para a mitocôndria ou vira lactato, e essa conversão consome um próton; ao lado, a quebra de ATP liberando ADP, fosfato e um próton"),
     "<defs>" + seta_marker("b1", TINTA) + seta_marker("b2", OXID) + seta_marker("b3", GLIC) + seta_marker("b4", FOSF) + "</defs>"]
def caixa(x, y, w, h, cor, fundo=CARTAO):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fundo}" stroke="{cor}" stroke-width="4"/>'
p += [caixa(0, 190, 220, 90, TINTA), caixa(340, 190, 240, 90, TINTA),
      f'<path d="M224 235 L330 235" stroke="{TINTA}" stroke-width="6" marker-end="url(#b1)"/>',
      f'<ellipse cx="820" cy="80" rx="150" ry="62" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>',
      f'<path d="M584 215 Q640 90 660 84" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#b2)"/>',
      caixa(700, 340, 240, 90, GLIC, GLIC_T),
      f'<path d="M584 255 Q640 380 690 384" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#b3)"/>',
      f'<line x1="1060" y1="0" x2="1060" y2="460" stroke="{GRADE}" stroke-width="2"/>',
      caixa(1110, 60, 160, 90, FOSF, FOSF_T),
      f'<path d="M1274 105 L1356 105" stroke="{FOSF}" stroke-width="6" marker-end="url(#b4)"/>',
      "</svg>"]
rs = [rot(0, 216, "Glicose", w=220, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(340, 216, "Piruvato", w=240, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(670, 62, "Mitocôndria", w=300, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(700, 366, "Lactato", w=240, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(480, 400, "consome 1 H⁺", w=200, tam=26, cor=GLIC, peso=700, alinha="right"),
      rot(1110, 86, "ATP", w=160, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(1370, 84, "ADP + Pi + H⁺", w=294, tam=32, cor=TINTA, peso=700),
      rot(1110, 190, "1. Produz lactato e H⁺, por reações diferentes. Ácido lático quase não existe no pH do corpo.", w=554, tam=26),
      rot(1110, 290, "2. O H⁺ vem em boa parte da quebra do ATP.", w=554, tam=26, cor=FOSF, peso=600),
      rot(1110, 360, "3. Formar lactato consome H⁺: atrasa a acidose.", w=554, tam=26, cor=GLIC, peso=600)]
S.append({"id": "bioquimica", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A bioquímica em três frases", "titulo": "De onde vem o próton que acidifica",
          "fonte": "Robergs, Ghiasvand e Parker, American Journal of Physiology 2004"})

# 7. uma causa, dois sinais
p = [svg_abre(1664, 420, "Uma causa comum, a demanda alta de ATP pela glicólise, com duas setas para lactato sobe e acidez sobe; a seta direta de lactato para acidez está riscada"),
     "<defs>" + seta_marker("u1", TINTA) + seta_marker("u2", MUDO) + "</defs>",
     f'<rect x="432" y="0" width="800" height="110" rx="16" fill="{TINTA}"/>',
     f'<rect x="232" y="290" width="440" height="110" rx="16" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>',
     f'<rect x="992" y="290" width="440" height="110" rx="16" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>',
     f'<path d="M640 114 L470 280" stroke="{TINTA}" stroke-width="7" marker-end="url(#u1)"/>',
     f'<path d="M1024 114 L1194 280" stroke="{TINTA}" stroke-width="7" marker-end="url(#u1)"/>',
     f'<path d="M680 345 L980 345" stroke="{MUDO}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#u2)"/>',
     f'<line x1="780" y1="300" x2="880" y2="390" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>',
     f'<line x1="880" y1="300" x2="780" y2="390" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>', "</svg>"]
rs = [rot(432, 18, "Demanda alta de ATP<br>pela via glicolítica", w=800, tam=32, cor="#F7F6F2", peso=700, alinha="center"),
      rot(232, 318, "Lactato sobe", w=440, tam=34, cor=TINTA, peso=700, alinha="center"),
      rot(992, 318, "Acidez sobe", w=440, tam=34, cor=TINTA, peso=700, alinha="center"),
      rot(0, 160, "o termômetro", w=420, tam=28, cor=GLIC, peso=700, alinha="right"),
      rot(1244, 160, "a febre", w=420, tam=28, cor=FOSF, peso=700),
      rot(690, 250, "a seta de cem anos", w=280, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "causa", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O detalhe está em debate. A conclusão, não.", "titulo": "Uma causa, dois sinais",
          "destaque": "O lactato não é o agente da acidose. É o acompanhante. Ninguém trata febre quebrando o termômetro."})

# 8. a lançadeira
p = [svg_abre(1664, 460, "Lançadeira do lactato: uma fibra glicolítica no centro solta lactato para uma fibra oxidativa vizinha, para o coração, para o cérebro e para o fígado, que devolve glicose"),
     "<defs>" + seta_marker("l1", GLIC) + seta_marker("l2", OXID) + "</defs>",
     f'<ellipse cx="832" cy="230" rx="200" ry="92" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="5"/>']
dest = [(80, 30, "Fibra oxidativa", "vizinha: queima"), (80, 330, "Coração", "queima"),
        (1284, 30, "Cérebro", "queima"), (1284, 330, "Fígado", "faz glicose de novo")]
for x, y, t, s in dest:
    p.append(f'<rect x="{x}" y="{y}" width="300" height="100" rx="14" fill="{CARTAO}" stroke="{OXID}" stroke-width="4"/>')
p += [f'<path d="M660 190 Q520 90 392 82" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#l1)"/>',
      f'<path d="M660 270 Q520 370 392 378" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#l1)"/>',
      f'<path d="M1004 190 Q1144 90 1272 82" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#l1)"/>',
      f'<path d="M1004 270 Q1144 370 1272 378" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#l1)"/>',
      f'<path d="M1300 440 Q832 470 800 334" fill="none" stroke="{OXID}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#l2)"/>',
      "</svg>"]
rs = [rot(632, 196, "Fibra glicolítica", w=400, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(632, 238, "produz lactato", w=400, tam=26, alinha="center"),
      rot(980, 372, "glicose de volta", w=300, tam=24, cor=OXID, peso=600)]
for x, y, t, s in dest:
    rs += [rot(x, y + 14, t, w=300, tam=30, cor=TINTA, peso=700, alinha="center"),
           rot(x, y + 56, s, w=300, tam=24, alinha="center")]
S.append({"id": "lancadeira", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A lançadeira do lactato", "titulo": "Não é resíduo. É combustível.",
          "fonte": "Brooks, Cell Metabolism 2018 · produzido o tempo todo, inclusive em repouso e com oxigênio de sobra"})

# 9. três funções
S.append({"id": "funcoes", "tipo": "cards", "por_linha": 3,
          "eyebrow": "Três funções, as três úteis", "titulo": "O “lixo metabólico” trabalha",
          "cards": [{"t": "Energia", "x": "Queimado por fibras oxidativas, coração e cérebro.", "cor": "petr"},
                    {"t": "Matéria-prima", "x": "O fígado usa o lactato para fazer glicose de novo.", "cor": "ambar"},
                    {"t": "Sinal", "x": "Participa da regulação de processos que incluem a adaptação da mitocôndria.", "cor": "verm"}],
          "destaque": "A substância que a gente aprendeu a chamar de lixo é, em parte, o sinal que avisa o músculo para construir mais mitocôndria."})

# 10. queimação sim, força pouco
p = [svg_abre(1664, 380, "Com a mesma acidez, a queda de força é grande em músculo a 12 graus e pequena a 32 graus; a queimação continua"),
     f'<rect x="420" y="40" width="820" height="90" rx="6" fill="{AZUL}"/>',
     f'<rect x="420" y="190" width="170" height="90" rx="6" fill="{AZUL}"/>',
     f'<line x1="418" y1="10" x2="418" y2="310" stroke="{MUDO}" stroke-width="2"/>',
     f'<line x1="1300" y1="0" x2="1300" y2="380" stroke="{GRADE}" stroke-width="2"/>', "</svg>"]
rs = [rot(0, 44, "A 12 °C<br>temperatura de laboratório", w=390, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(0, 194, "A 32 °C<br>perto da do corpo", w=390, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(610, 216, "o efeito encolhe muito", w=500, tam=28, cor=AZUL, peso=700),
      rot(420, 326, "queda de força com a mesma acidez · barras ilustrativas", w=860, tam=24, cor=MUDO),
      rot(1340, 60, "E a queimação?", w=324, tam=30, cor=FOSF, peso=700),
      rot(1340, 110, "O H⁺ contribui, agindo sobre receptores sensoriais. Essa parte continua.", w=324, tam=26)]
S.append({"id": "temperatura", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Se não é o lactato, o que derruba a força?", "titulo": "Acidez: queimação, sim. Força, bem menos.",
          "fonte": "Westerblad, Allen e Lännergren, News in Physiological Sciences 2002"})

# 11. o fosfato inorgânico
p = [svg_abre(1664, 460, "A fosfocreatina se quebra em creatina e fosfato; o fosfato dentro da fibra sobe de 5 para 30 milimolar; ele atrapalha a ponte cruzada e reduz a liberação de cálcio"),
     "<defs>" + seta_marker("f1", FOSF) + seta_marker("f2", TINTA) + "</defs>",
     f'<rect x="0" y="40" width="300" height="90" rx="14" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>',
     f'<path d="M150 134 L150 206" stroke="{FOSF}" stroke-width="6" marker-end="url(#f1)"/>',
     f'<rect x="0" y="216" width="300" height="90" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>',
     f'<line x1="420" y1="420" x2="900" y2="420" stroke="{MUDO}" stroke-width="2"/>',
     f'<rect x="470" y="{420-50}" width="150" height="50" rx="4" fill="{MUDO}"/>',
     f'<rect x="700" y="{420-300}" width="150" height="300" rx="4" fill="{FOSF}"/>',
     f'<rect x="1080" y="60" width="584" height="120" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>',
     f'<rect x="1080" y="260" width="584" height="120" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>',
     f'<path d="M860 200 Q960 120 1070 120" fill="none" stroke="{TINTA}" stroke-width="6" marker-end="url(#f2)"/>',
     f'<path d="M860 260 Q960 320 1070 320" fill="none" stroke="{TINTA}" stroke-width="6" marker-end="url(#f2)"/>', "</svg>"]
rs = [rot(0, 64, "Fosfocreatina", w=300, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 240, "Creatina + Pi", w=300, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 330, "a moeda do sistema mais potente", w=300, tam=24, alinha="center"),
      rot(470, 318, "~5 mM", w=150, tam=30, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(700, 68, "~30 mM", w=150, tam=30, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(430, 426, "repouso", w=230, tam=24, cor=MUDO, alinha="center"),
      rot(660, 426, "esforço intenso", w=230, tam=24, cor=MUDO, alinha="center"),
      rot(1110, 84, "Atrapalha a ponte cruzada", w=530, tam=30, cor=TINTA, peso=700),
      rot(1110, 126, "a maquinaria que gera força", w=530, tam=24),
      rot(1110, 284, "Reduz a liberação de cálcio", w=530, tam=30, cor=TINTA, peso=700),
      rot(1110, 326, "o sinal que manda contrair", w=530, tam=24)]
S.append({"id": "fosfato", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O candidato que ocupou o lugar", "titulo": "Fosfato inorgânico: seis vezes mais",
          "destaque": "A potência tem um preço, e o preço é pago na moeda do próprio sistema.", "destaque_cor": "verm",
          "fonte": "Allen, Lamb e Westerblad, Physiological Reviews 2008"})

# 12. o relógio de 72 horas
lac72 = [(t / 4, 100 * math.exp(-(t / 4) / 0.45)) for t in range(0, 41)] + [(t, 0) for t in range(11, 73)]
dor = [(t, 0 if t < 8 else 90 * ((t - 8) / 48) ** 3 * math.exp(3 * (1 - (t - 8) / 48))) for t in range(0, 73)]
def faixa(fx, fy):
    return f'<rect x="{fx(48):.1f}" y="{fy(100):.1f}" width="{fx(72)-fx(48):.1f}" height="{fy(0)-fy(100):.1f}" fill="{FOSF_T}"/>'
svg, rs = linhas(1664, 420, "Linha do tempo de 72 horas: o lactato do sangue volta perto do normal nas primeiras horas; a dor começa no dia seguinte e tem pico entre 48 e 72 horas",
    [{"nome": "", "cor": GLIC, "pts": lac72}, {"nome": "", "cor": FOSF, "pts": dor}],
    0, 72, 0, 100, [(0, "fim do treino"), (24, "24 h"), (48, "48 h"), (72, "72 h")], [], margem=(40, 20, 60, 40), extra=faixa)
rs += [rot(90, 30, "lactato do sangue: perto do normal em 1 a 2 horas, sozinho", w=560, tam=26, cor=GLIC, peso=700),
       rot(560, 150, "dor tardia", w=300, tam=28, cor=FOSF, peso=700),
       rot(1090, 290, "pico da dor: 48 a 72 h", w=520, tam=28, cor=TINTA, peso=700)]
S.append({"id": "relogio", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "A dor de dois dias", "titulo": "O que já foi embora não causa o que ainda nem começou",
          "fonte": "Esquema a partir de Menzies e colaboradores 2010 e Hotfiel e colaboradores 2018"})

# 13. a sessão repetida
d1 = [(t / 8, 0 if t / 8 < 0.3 else 90 * ((t / 8 - 0.3) / 1.9) ** 2.5 * math.exp(2.5 * (1 - (t / 8 - 0.3) / 1.9))) for t in range(0, 57)]
d2 = [(x, y * 0.28) for x, y in d1]
svg, rs = linhas(1664, 400, "Dor ao longo de uma semana: alta depois da primeira sessão; bem mais baixa quando a mesma sessão é repetida uma semana depois",
    [{"nome": "", "cor": FOSF, "pts": d1}, {"nome": "", "cor": AZUL, "pts": d2}],
    0, 7, 0, 100, [(0, "sessão"), (1, "1 dia"), (2, "2 dias"), (3, "3 dias"), (5, "5 dias"), (7, "7 dias")], [], margem=(40, 20, 60, 30))
svg = svg.replace("</svg>", f'<rect x="1100" y="30" width="36" height="6" rx="3" fill="{FOSF}"/><rect x="1100" y="78" width="36" height="6" rx="3" fill="{AZUL}"/></svg>')
rs += [rot(1150, 16, "primeira vez", w=480, tam=26, cor=TINTA, peso=600),
       rot(1150, 64, "a mesma sessão, uma semana depois", w=480, tam=26, cor=TINTA, peso=600),
       rot(1100, 150, "excêntrico + não habituado", w=540, tam=34, cor=TINTA, peso=700, serif=True)]
S.append({"id": "repetida", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "Efeito da sessão repetida", "titulo": "Não é intensidade metabólica. É novidade mecânica.",
          "destaque": "“O que eu faço para não sentir isso?” A resposta é dose: gesto novo e excêntrico entram aos poucos, com a primeira vez menor que a vontade.",
          "destaque_cor": "ambar", "fonte": "Esquema · Hyldahl, Chen e Nosaka, Exercise and Sport Sciences Reviews 2017"})

# 14. bandeira vermelha
S.append({"id": "rabdo", "tipo": "cards", "por_linha": 4,
          "eyebrow": "Bandeira vermelha", "titulo": "Isso não é dor muscular tardia",
          "cards": [{"t": "Dor desproporcional", "x": "Que não melhora em três ou quatro dias.", "cor": "verm"},
                    {"t": "Inchaço", "x": "Importante, no músculo trabalhado.", "cor": "verm"},
                    {"t": "Fraqueza", "x": "Marcante, fora do esperado.", "cor": "verm"},
                    {"t": "Urina escura", "x": "Cor de chá ou de refrigerante de cola.", "cor": "verm"}],
          "destaque": "Rabdomiólise até que se prove o contrário: avaliação médica no mesmo dia. A dor tardia comum é o pano de fundo que faz ela passar despercebida.",
          "destaque_cor": "verm"})

# 15. treinar o glicolítico
p = [svg_abre(1664, 440, "Fibra muscular com três adaptações ao treino glicolítico: mais tampões dentro, mais transportadores na membrana levando lactato e próton para fora, e mais tolerância ao desconforto"),
     "<defs>" + seta_marker("t1", GLIC) + "</defs>",
     f'<rect x="0" y="40" width="1000" height="300" rx="150" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>']
for i in range(9):
    cx, cy = 180 + (i % 3) * 110, 96 + (i // 3) * 66
    p.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="{AZUL}" opacity="0.85"/>')
for k in range(4):
    x = 620 + k * 90
    p.append(f'<rect x="{x}" y="28" width="40" height="26" rx="6" fill="{OXID}"/>')
    p.append(f'<path d="M{x+20} 150 L{x+20} 60 L{x+20} 0" fill="none" stroke="{GLIC}" stroke-width="5" marker-end="url(#t1)"/>')
p.append(f'<rect x="1100" y="40" width="564" height="300" rx="16" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/></svg>')
rs = [rot(120, 272, "mais tampões dentro da fibra", w=400, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(560, 200, "mais transportadores:<br>lactato e H⁺ para fora", w=420, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(1130, 70, "Tolerância ao desconforto", w=510, tam=30, cor=TINTA, peso=700),
      rot(1130, 120, "Um lado treinável e um lado de cabeça.", w=510, tam=26),
      rot(1130, 210, "Assinatura em campo: queda de potência no esforço repetido, queimação forte, recuperação lenta.", w=510, tam=26, cor=FOSF, peso=600),
      rot(0, 370, "O que melhora é o quanto se aguenta, não o quanto se produz.", w=1100, tam=30, cor=TINTA, peso=700, serif=True)]
S.append({"id": "tolerancia", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dá para treinar o glicolítico?", "titulo": "Treina tolerância, não produção",
          "destaque": "Decremento alto de propósito é treino glicolítico. Sem querer, é treino de velocidade estragado."})

# 16. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "O que se diz no lugar",
          "regras": ["Desaquecimento: diga o que ele é. Transição, ritual, sensação boa.",
                     "Dor de dois dias: mexa na progressão, não no lactato.",
                     "Diga lactato. O lactato medido é marcador, não veneno."],
          "cards": [{"t": "Todo mundo da equipe", "x": "Desmonta a frase errada, porque todo mundo diz."},
                    {"t": "Dono técnico", "x": "A coleta de sangue e a leitura da curva de lactato."}],
          "quem": "Junto não é por causa."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['juntos', 'combustivel', 'bioquimica', 'causa', 'lancadeira', 'fosfato', 'repetida', 'rabdo', 'tolerancia', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-03-glicolise-e-a-desconstrucao-do-acido-latico.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "O acompanhante inocente", "subtitulo": "Glicólise e a desconstrução do ácido lático",
        "nota_capa": "Entra pela cena do remador.",
        "secoes": {"erro": ["As três frases e por que o erro convence.", "capa"],
                   "sistema": ["O que a glicólise faz e de onde vem o próton.", "combustivel"],
                   "virada": ["Lactato como combustível e o que de fato derruba a força.", "lancadeira"],
                   "pratica": ["A dor de dois dias, a bandeira vermelha e o que treinar.", "repetida"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-03.json"), "w"), ensure_ascii=False, indent=1)
print("02-03.json:", len(S), "slides")
