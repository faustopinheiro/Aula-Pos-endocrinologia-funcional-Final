"""Spec do deck 2.1. Gera 02-01.json ao lado deste arquivo."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

# 1. curva dos 75 segundos
aer = [(10, 6), (20, 18), (30, 27), (45, 37), (60, 45), (75, 50), (90, 56), (120, 63), (180, 73), (240, 79)]
ana = [(x, 100 - y) for x, y in aer]
svg, rs = linhas(1664, 440, "Contribuição aeróbica subindo de 6% aos 10 segundos para 79% aos 4 minutos e anaeróbica caindo de 94% para 21%; as duas se cruzam em 50% por volta dos 75 segundos",
    [{"nome": "Anaeróbico", "cor": FOSF, "pts": ana, "rotulo_xy": (12, 94), "dx": 10, "dy": -52},
     {"nome": "Aeróbico", "cor": OXID, "pts": aer, "rotulo_xy": (12, 6), "dx": 10, "dy": -52, "marcas": [(75, 50)]}],
    10, 240, 0, 100, [(10, "10 s"), (30, "30 s"), (60, "1 min"), (120, "2 min"), (240, "4 min")], [0, 50, 100], xlog=True,
    destaques=[{"x": 75, "t": "75 s: metade e metade", "w": 330}], margem=(90, 20, 60, 20))
S.append({"id": "curva", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "Esforço máximo e contínuo", "titulo": "Aeróbico e anaeróbico se igualam aos 75 segundos",
          "destaque": "Em 2 minutos de esforço máximo: um terço anaeróbico, dois terços aeróbico.",
          "fonte": "Gastin, Sports Medicine 2001 · Gastin e Suppiah, 2026 (mais de 100 estudos, diferença de 0 a 3%)"})

# 2. a mistura no esporte real
svg, rs, h = barras_empilhadas(1664, "Contribuição anaeróbica e aeróbica: tiro de 10 s, 94 e 6 por cento; série de 40 s, 67 e 33; 400 metros, 55 e 45; 2 minutos, 37 e 63; luta de 4 minutos, 21 e 79",
    [("Tiro de 10 s", [94, 6]), ("Série até a falha, ~40 s", [67, 33]), ("400 m, ~1 min", [55, 45]),
     ("Round ou 800 m, ~2 min", [37, 63]), ("Luta de judô, 4 min", [21, 79])],
    [FOSF, OXID], larg_rotulo=420, alt_barra=60, passo=84, topo=64, min_txt=80)
svg = svg.replace("</svg>", f'<rect x="444" y="8" width="28" height="28" rx="4" fill="{FOSF}"/><rect x="780" y="8" width="28" height="28" rx="4" fill="{OXID}"/></svg>')
rs += [rot(484, 4, "Anaeróbico", w=260, tam=26, cor=TINTA, peso=600), rot(820, 4, "Aeróbico", w=260, tam=26, cor=TINTA, peso=600)]
S.append({"id": "mistura", "tipo": "diagrama", "h": h, "svg": svg, "rotulos": rs,
          "eyebrow": "No esporte de verdade", "titulo": "Não existe esforço puro: existe mistura",
          "fonte": "Estimativas para esforço máximo com essa duração, a partir de Gastin 2001"})

# 3. revezamento x todos ligados
p = [svg_abre(1664, 460, "À esquerda, riscada, a figura do revezamento com três caixas em fila; à direita, as três curvas de contribuição começando juntas no tempo zero"),
     "<defs>" + seta_marker("s3", MUDO) + "</defs>"]
for i, (cor, x) in enumerate([(FOSF, 0), (GLIC, 260), (OXID, 520)]):
    p.append(f'<rect x="{x}" y="150" width="220" height="110" rx="12" fill="#FDFCF9" stroke="{cor}" stroke-width="4"/>')
for x in (220, 480):
    p.append(f'<path d="M{x+4} 205 L{x+34} 205" stroke="{MUDO}" stroke-width="4" marker-end="url(#s3)"/>')
p.append(f'<line x1="-10" y1="110" x2="750" y2="310" stroke="{FOSF}" stroke-width="10" stroke-linecap="round" opacity="0.8"/>')
p.append(f'<line x1="-10" y1="310" x2="750" y2="110" stroke="{FOSF}" stroke-width="10" stroke-linecap="round" opacity="0.8"/>')
p.append(f'<line x1="900" y1="380" x2="1650" y2="380" stroke="{MUDO}" stroke-width="2"/><line x1="900" y1="80" x2="900" y2="380" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<path d="M902 378 C905 120 950 100 1020 190 S1300 360 1640 372" fill="none" stroke="{FOSF}" stroke-width="6" stroke-linecap="round"/>')
p.append(f'<path d="M902 378 C960 300 1030 160 1130 165 S1360 320 1640 352" fill="none" stroke="{GLIC}" stroke-width="6" stroke-linecap="round"/>')
p.append(f'<path d="M902 378 C1100 370 1250 190 1640 110" fill="none" stroke="{OXID}" stroke-width="6" stroke-linecap="round"/>')
for i, cor in enumerate([FOSF, GLIC, OXID]):
    p.append(f'<rect x="{900 + i*250}" y="424" width="36" height="8" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(0, 0, "A figura errada: revezamento", w=760, tam=30, cor=FOSF, peso=600),
      rot(0, 172, "Fosfagênico<br>0 a 10 s", w=220, tam=26, cor=TINTA, alinha="center"),
      rot(260, 172, "Glicolítico<br>até 2 min", w=220, tam=26, cor=TINTA, alinha="center"),
      rot(520, 172, "Oxidativo<br>depois", w=220, tam=26, cor=TINTA, alinha="center"),
      rot(900, 0, "A figura certa: os três ligados desde o início", w=764, tam=30, cor=OXID, peso=600),
      rot(946, 410, "Fosfagênico", w=200, tam=24, cor=TINTA), rot(1196, 410, "Glicolítico", w=200, tam=24, cor=TINTA),
      rot(1446, 410, "Oxidativo", w=200, tam=24, cor=TINTA)]
S.append({"id": "revezamento", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A imagem que quase todo mundo aprendeu", "titulo": "Não é revezamento",
          "destaque": "Muda de qual sistema se tira mais, e não qual está aberto. E “anaeróbico” não é músculo sem oxigênio."})

# 4. ciclo do ATP
p = [svg_abre(1664, 480, "Ciclo do ATP: o ATP vira ADP mais fosfato liberando energia para a contração e é refeito pelos três sistemas; ao lado, estoque de 5 milimoles por quilo, gasto de 3,7 por segundo, menos de 2 segundos"),
     "<defs>" + seta_marker("s4a", FOSF) + seta_marker("s4b", OXID) + "</defs>",
     f'<circle cx="420" cy="90" r="78" fill="#FDFCF9" stroke="{TINTA}" stroke-width="4"/>',
     f'<circle cx="420" cy="390" r="78" fill="#FDFCF9" stroke="{TINTA}" stroke-width="4"/>',
     f'<path d="M500 110 Q640 240 503 368" fill="none" stroke="{FOSF}" stroke-width="7" marker-end="url(#s4a)"/>',
     f'<path d="M340 370 Q200 240 337 112" fill="none" stroke="{OXID}" stroke-width="7" marker-end="url(#s4b)"/>',
     f'<line x1="960" y1="0" x2="960" y2="480" stroke="{GRADE}" stroke-width="2"/>', "</svg>"]
rs = [rot(350, 68, "ATP", w=140, tam=38, cor=TINTA, peso=700, alinha="center"),
      rot(342, 372, "ADP + Pi", w=156, tam=28, cor=TINTA, peso=600, alinha="center"),
      rot(610, 200, "energia para a contração", w=300, tam=26, cor=TINTA),
      rot(0, 190, "refeito pelos três sistemas", w=230, tam=26, cor=TINTA, alinha="right"),
      rot(1010, 10, "5", w=190, tam=88, cor=TINTA, peso=700, serif=True),
      rot(1210, 36, "milimoles de ATP por quilo de músculo: todo o estoque", w=454, tam=26),
      rot(1010, 170, "3,7", w=190, tam=88, cor=TINTA, peso=700, serif=True),
      rot(1210, 196, "milimoles gastos a cada segundo de esforço máximo", w=454, tam=26),
      rot(1010, 330, "< 2 s", w=200, tam=80, cor=FOSF, peso=700, serif=True),
      rot(1210, 356, "até acabar. Ninguém para aí: o ATP é refeito o tempo todo", w=454, tam=26)]
S.append({"id": "atp", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A moeda da contração", "titulo": "ATP não é estoque. É moeda de troca.",
          "destaque": "O que sustenta o esforço é a velocidade de refazer ATP, que sobe até mil vezes acima do repouso."})

# 5. três reservatórios
p = [svg_abre(1664, 480, "Três reservatórios: o fosfagênico pequeno com torneira larga, o glicolítico médio com torneira média e o oxidativo enorme com torneira estreita")]
tanques = [(FOSF, 140, 180, 150, 34), (GLIC, 600, 250, 230, 22), (OXID, 1090, 400, 330, 10)]
base = 340
for cor, x, w, h, esp in tanques:
    y = base - h
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FDFCF9" stroke="{TINTA}" stroke-width="4"/>')
    agua = h * 0.82
    p.append(f'<rect x="{x+6}" y="{base-agua}" width="{w-12}" height="{agua-6}" rx="6" fill="{cor}" opacity="0.85"/>')
    py = base - 110 - esp / 2
    p.append(f'<rect x="{x+w}" y="{py}" width="70" height="{esp}" fill="{TINTA}"/>')
    p.append(f'<rect x="{x+w+70-esp}" y="{py}" width="{esp}" height="{esp+16}" fill="{TINTA}"/>')
    p.append(f'<rect x="{x+w+70-esp}" y="{py+esp+16}" width="{esp}" height="{base-(py+esp+16)}" fill="{cor}" opacity="0.6"/>')
p.append(f'<line x1="0" y1="{base+2}" x2="1664" y2="{base+2}" stroke="{GRADE}" stroke-width="2"/></svg>')
rs = []
for (cor, x, w, h, esp), nome, sub in zip(tanques, ["Fosfagênico", "Glicolítico", "Oxidativo"],
        ["pequeno, torneira larga: segundos", "médio, torneira média: dezenas de segundos a minutos", "enorme, torneira estreita: quase não acaba"]):
    cx = x + w / 2
    rs.append(rot(cx - 230, 368, nome, w=460, tam=30, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(cx - 230, 408, sub, w=460, tam=24, cor=APOIO2, alinha="center"))
S.append({"id": "reservatorios", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os três sistemas", "titulo": "Três reservatórios, três torneiras",
          "destaque": "Potência é a largura da torneira. Capacidade é o tamanho do reservatório. Cada sistema troca uma pela outra."})

# 6. glicose: 2 ou 30 ATP
p = [svg_abre(1664, 460, "A glicose tem dois caminhos: o rápido, fora da mitocôndria, rende 2 ATP; o lento, dentro da mitocôndria, rende cerca de 30"),
     "<defs>" + seta_marker("s6a", GLIC) + seta_marker("s6b", OXID) + "</defs>",
     f'<polygon points="210,220 170,289 90,289 50,220 90,151 170,151" fill="#FDFCF9" stroke="{TINTA}" stroke-width="4"/>',
     f'<polyline points="190,185 300,110 712,110" fill="none" stroke="{GLIC}" stroke-width="7" stroke-linejoin="round" marker-end="url(#s6a)"/>',
     f'<rect x="720" y="60" width="300" height="100" rx="12" fill="#F6EEDD" stroke="{GLIC}" stroke-width="4"/>',
     f'<polyline points="190,255 300,340 602,340" fill="none" stroke="{OXID}" stroke-width="7" stroke-linejoin="round" marker-end="url(#s6b)"/>',
     f'<ellipse cx="800" cy="340" rx="190" ry="72" fill="#E3F1EE" stroke="{OXID}" stroke-width="4"/>',
     f'<path d="M640 340 q20 -40 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" fill="none" stroke="{OXID}" stroke-width="3" opacity="0.6"/>',
     f'<line x1="992" y1="340" x2="1290" y2="340" stroke="{OXID}" stroke-width="7" marker-end="url(#s6b)"/>',
     f'<rect x="1300" y="290" width="340" height="100" rx="12" fill="#E3F1EE" stroke="{OXID}" stroke-width="4"/>', "</svg>"]
rs = [rot(50, 202, "Glicose", w=160, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(320, 54, "rápido, fora da mitocôndria", w=380, tam=26),
      rot(720, 82, "2 ATP", w=300, tam=44, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1060, 86, "rende pouco, rende já", w=560, tam=28, cor=TINTA, peso=600),
      rot(610, 418, "mitocôndria", w=380, tam=24, cor=OXID, peso=600, alinha="center"),
      rot(1300, 312, "~30 ATP", w=340, tam=44, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1300, 400, "rende muito, demora", w=340, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(300, 356, "lento, dentro da mitocôndria", w=290, tam=26)]
S.append({"id": "glicose", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número que resume a lógica", "titulo": "A mesma glicose: 2 ATP ou 30 ATP",
          "destaque": "Rendimento e velocidade são coisas diferentes. Quando o prazo aperta, o músculo paga juros para ter a energia agora."})

# 7. quem recarrega a fosfocreatina
p = [svg_abre(1664, 440, "Ciclo: o tiro gasta a fosfocreatina, a pausa usa a mitocôndria para refazê-la, e a fosfocreatina volta para o próximo tiro"),
     "<defs>" + seta_marker("s7a", FOSF) + seta_marker("s7b", OXID) + seta_marker("s7c", MUDO) + "</defs>",
     f'<rect x="80" y="20" width="400" height="130" rx="16" fill="#FDFCF9" stroke="{FOSF}" stroke-width="5"/>',
     f'<rect x="1184" y="20" width="400" height="130" rx="16" fill="#FDFCF9" stroke="{OXID}" stroke-width="5"/>',
     f'<rect x="632" y="296" width="400" height="130" rx="16" fill="#FDFCF9" stroke="{TINTA}" stroke-width="4"/>',
     f'<line x1="484" y1="85" x2="1174" y2="85" stroke="{FOSF}" stroke-width="7" marker-end="url(#s7a)"/>',
     f'<path d="M1384 154 Q1330 360 1043 361" fill="none" stroke="{OXID}" stroke-width="9" marker-end="url(#s7b)"/>',
     f'<path d="M628 361 Q330 360 283 160" fill="none" stroke="{MUDO}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#s7c)"/>', "</svg>"]
rs = [rot(80, 44, "Tiro", w=400, tam=34, cor=TINTA, peso=700, alinha="center"),
      rot(80, 94, "fosfagênico", w=400, tam=26, cor=FOSF, alinha="center"),
      rot(1184, 44, "Pausa", w=400, tam=34, cor=TINTA, peso=700, alinha="center"),
      rot(1184, 94, "oxidativo", w=400, tam=26, cor=OXID, alinha="center"),
      rot(632, 326, "Fosfocreatina refeita", w=400, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(632, 370, "pronta para o próximo", w=400, tam=24, alinha="center"),
      rot(560, 30, "gasta a fosfocreatina", w=540, tam=26, alinha="center"),
      rot(1430, 196, "a mitocôndria recarrega", w=234, tam=28, cor=TINTA, peso=600),
      rot(60, 250, "próximo tiro", w=220, tam=26, alinha="right")]
S.append({"id": "recarga", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O detalhe que quase ninguém ensina", "titulo": "Quem recarrega o sistema mais rápido é o mais lento",
          "destaque": "O jogador que apaga no fim não precisa de mais tiro: precisa de base aeróbica. O sintoma parece anaeróbico. O buraco é aeróbico."})

# 8. o tamanho dos tanques
p = [svg_abre(1664, 280, "Estoque de glicogênio, 1.600 a 2.000 quilocalorias, desenhado em escala contra o estoque de gordura, mais de 60.000 quilocalorias"),
     f'<rect x="444" y="30" width="40" height="80" rx="4" fill="{GLIC}"/>',
     f'<rect x="444" y="170" width="1200" height="80" rx="4" fill="{OXID}"/>', "</svg>"]
rs = [rot(0, 38, "Glicogênio<br>músculo e fígado", w=420, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(500, 50, "400 a 500 g · 1.600 a 2.000 kcal", w=700, tam=30, cor=TINTA, peso=600),
      rot(0, 178, "Gordura<br>mesmo em adulto magro", w=420, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(1100, 190, "mais de 60.000 kcal", w=520, tam=30, cor="#F7F6F2", peso=700, alinha="right")]
S.append({"id": "tanques", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O tamanho dos tanques, em escala", "titulo": "Acaba o tanque pequeno, o único que serve para a intensidade alta",
          "destaque": "A mistura depende de quatro coisas: quanto dura o esforço, quão forte ele é, o estado de treino e o combustível disponível."})

# 9. esforço subindo com a carga igual
p = [svg_abre(1664, 300, "A mesma sessão em dois dias: na terça, esforço 6 de 10; na quinta, esforço 8 de 10")]
for i, nota in enumerate([6, 8]):
    y = 20 + i * 140
    for c in range(10):
        cor = OXID if c < 6 else FOSF
        fill = cor if c < nota else "#E6E2D8"
        p.append(f'<rect x="{560 + c*92}" y="{y}" width="84" height="84" rx="8" fill="{fill}"/>')
p.append("</svg>")
rs = [rot(0, 26, "Terça · 5 × 1 km a 4:30/km", w=520, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(1500, 30, "6/10", w=164, tam=48, cor=TINTA, peso=700, serif=True, alinha="right"),
      rot(0, 166, "Quinta · o mesmo treino", w=520, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(1500, 170, "8/10", w=164, tam=48, cor=FOSF, peso=700, serif=True, alinha="right")]
S.append({"id": "esforco", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Como perceber, sem exame", "titulo": "A nota de esforço subiu com a carga igual",
          "destaque": "Sem dor, sem infecção, sem noite ruim: a primeira hipótese é combustível não reposto. Pergunte: “o que você comeu antes e depois do treino de ontem?” Quanto e o que comer é da nutrição.",
          "destaque_cor": "ambar"})

# 10. três tipos de esforço
p = [svg_abre(1664, 380, "Três padrões de esforço: intermitente, com picos curtos sobre uma faixa contínua de recuperação; contínuo, uma faixa longa com duas subidas; e fracionado com carga, blocos de séries separados por pausas")]
for c in range(3):
    x0 = c * 572
    p.append(f'<line x1="{x0}" y1="230" x2="{x0+520}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
x0 = 0
p.append(f'<rect x="{x0}" y="196" width="520" height="34" fill="{OXID}" opacity="0.85"/>')
for xs, hh in [(30, 130), (110, 90), (150, 140), (260, 110), (330, 140), (440, 100)]:
    p.append(f'<rect x="{x0+xs}" y="{196-hh}" width="22" height="{hh}" rx="4" fill="{FOSF}"/>')
x0 = 572
p.append(f'<path d="M{x0} 230 L{x0} 150 L{x0+150} 150 Q{x0+200} 70 {x0+250} 150 L{x0+400} 150 Q{x0+460} 80 {x0+520} 150 L{x0+520} 230 Z" fill="{OXID}" opacity="0.85"/>')
p.append(f'<path d="M{x0+150} 150 Q{x0+200} 70 {x0+250} 150 Z" fill="{GLIC}"/><path d="M{x0+400} 150 Q{x0+460} 80 {x0+520} 150 Z" fill="{GLIC}"/>')
x0 = 1144
for k in range(4):
    xs = x0 + k * 132
    p.append(f'<rect x="{xs}" y="80" width="76" height="150" rx="4" fill="{GLIC}"/><rect x="{xs}" y="130" width="76" height="100" rx="4" fill="{FOSF}"/>')
    if k < 3:
        p.append(f'<rect x="{xs+80}" y="196" width="48" height="34" fill="{OXID}" opacity="0.85"/>')
for i, (cor, nome) in enumerate([(FOSF, "explosivo"), (GLIC, "intenso"), (OXID, "recuperação e base (oxidativo)")]):
    p.append(f'<rect x="{i*330}" y="336" width="28" height="28" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(0, 0, "Intermitente", w=520, tam=30, cor=TINTA, peso=700),
      rot(0, 244, "quadra, campo, tatame, ringue", w=520, tam=24),
      rot(572, 0, "Contínuo", w=520, tam=30, cor=TINTA, peso=700),
      rot(572, 244, "corrida, natação longa, pedal", w=520, tam=24),
      rot(1144, 0, "Fracionado com carga", w=520, tam=30, cor=TINTA, peso=700),
      rot(1144, 244, "musculação, levantamento, ginástica", w=520, tam=24),
      rot(38, 333, "explosivo", w=280, tam=24, cor=TINTA), rot(368, 333, "intenso", w=280, tam=24, cor=TINTA),
      rot(698, 333, "recuperação e base (oxidativo)", w=600, tam=24, cor=TINTA)]
S.append({"id": "cenarios", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por tipo de esforço, não por esporte", "titulo": "Em todos, quem paga a recuperação é o oxidativo",
          "destaque": "Base aeróbica faz a sessão de força render mais. É um dos argumentos mais fortes, e menos usados, para não abandonar o aeróbico."})

# 11. o intervalo é variável de treino
p = [svg_abre(1664, 420, "Três linhas do tempo em escala: esforço de 6 segundos com pausa de 60, relação 1 para 10; esforço de 30 com pausa de 30, 1 para 1; esforço de 3 minutos com pausa de 30 segundos")]
esc, x0 = 3.0, 300
padroes = [([(6, FOSF), (60, PAUSA)] * 5, 20), ([(30, GLIC), (30, PAUSA)] * 5, 150), ([(180, OXID), (30, PAUSA), (120, OXID)], 280)]
for seq, y in padroes:
    x = x0
    for dur, cor in seq:
        ww = dur * esc
        p.append(f'<rect x="{x:.1f}" y="{y}" width="{max(ww-2,2):.1f}" height="60" rx="4" fill="{cor}"/>')
        x += ww
p.append(f'<rect x="{x0}" y="384" width="28" height="28" rx="4" fill="{PAUSA}"/></svg>')
rs = [rot(0, 22, "1 : 10", w=260, tam=48, cor=TINTA, peso=700, serif=True),
      rot(1320, 18, "potência: a fosfocreatina volta", w=344, tam=26, cor=TINTA, peso=600),
      rot(0, 152, "1 : 1", w=260, tam=48, cor=TINTA, peso=700, serif=True),
      rot(1320, 148, "empurra para o glicolítico", w=344, tam=26, cor=TINTA, peso=600),
      rot(0, 282, "longo : curto", w=280, tam=40, cor=TINTA, peso=700, serif=True),
      rot(1320, 278, "oxidativo disfarçado de intenso", w=344, tam=26, cor=TINTA, peso=600),
      rot(340, 382, "pausa · a cor do esforço é o sistema que paga a conta · 1 cm ≈ 10 s", w=1000, tam=24, cor=MUDO)]
S.append({"id": "intervalo", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A consequência para a prescrição", "titulo": "O intervalo é variável de treino, não pausa",
          "destaque": "“Descansa o que precisar” entrega ao acaso a variável mais poderosa da sessão.", "destaque_cor": "verm"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Três perguntas antes de qualquer sessão",
          "regras": ["Quanto dura cada esforço?", "Com que intensidade?", "Com quanto intervalo?"],
          "cards": [{"t": "Fosfagênico", "x": "Adapta fosfocreatina e recrutamento. Pede qualidade máxima em cada repetição."},
                    {"t": "Glicolítico", "x": "Adapta a tolerância à acidez. Pede o desconforto."},
                    {"t": "Oxidativo", "x": "Adapta mitocôndria e capilares. Pede volume e frequência."}],
          "quem": "A sessão que serve para tudo não serve direito para nada."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['curva', 'atp', 'reservatorios', 'recarga', 'tanques', 'esforco', 'intervalo', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-01-setenta-e-cinco-segundos.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Setenta e cinco segundos", "subtitulo": "Como o corpo paga a conta de energia do exercício",
        "nota_capa": "Entra pelo número.",
        "secoes": {"mistura": ["A curva dos 75 segundos e a mistura no esporte real.", "capa"],
                   "sistemas": ["ATP, os três reservatórios e o preço da velocidade.", "atp"],
                   "pratica": ["Combustível, tipos de esforço e o intervalo como variável.", "tanques"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-01.json"), "w"), ensure_ascii=False, indent=1)
print("02-01.json:", len(S), "slides")
