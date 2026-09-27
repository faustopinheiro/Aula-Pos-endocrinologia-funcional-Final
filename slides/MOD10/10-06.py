"""Spec do deck 10.6. Gera 10-06.json ao lado deste arquivo."""
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

# 1. as quatro estações
p = [svg_abre(1664, 520, "Linha do tempo do caso em quatro estações, com uma linha do joelho e outra da cabeça que começam no mesmo ponto")]
X = [140, 580, 1020, 1460]
p.append(f'<path d="M140 150 H1560" stroke="{AZUL}" stroke-width="6"/>')
p.append(f'<path d="M140 150 C 300 150, 300 330, 460 330 H1560" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<circle cx="140" cy="150" r="22" fill="{TINTA}"/>')
est = [("t:karate", "o dia da lesão", "“acabou o meu ano”"), ("t:bed", "terceira semana", "“fora do tatame eu não sei quem eu sou”"),
       ("t:friends", "quarto mês", "“quando pegam a minha perna, o corpo não deixa”"), ("t:door-exit", "sétimo mês", "“ela pode lutar na próxima?”")]
rs = [rot(1580, 132, "joelho", w=84, tam=24, cor=AZUL, peso=700), rot(1580, 312, "cabeça", w=84, tam=24, cor=FOSF, peso=700)]
for i, (ic, t, fr) in enumerate(est):
    x = X[i]
    if i:
        p.append(f'<circle cx="{x}" cy="150" r="14" fill="{AZUL}"/>')
        p.append(f'<circle cx="{x}" cy="330" r="14" fill="{FOSF}"/>')
    p.append(icone(ic, x - 40, 20, 80, TINTA))
    rs.append(rot(x - 160, 370, t, w=320, tam=28, cor=TINTA, peso=700, alinha="center", serif=True))
    rs.append(rot(x - 170, 420, fr, w=340, tam=24, cor=FOSF, alinha="center", lh=1.3))
p.append("</svg>")
S.append({"id": "estacoes", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Uma judoca na casa dos vinte anos", "titulo": "A lesão acontece no joelho e na cabeça no mesmo segundo",
          "fonte": "Ruptura do ligamento cruzado anterior num randori, três meses antes de uma seletiva · caso ilustrativo, sem desfecho"})

# 2. o modelo integrado
p = [svg_abre(1664, 540, "Cascata do modelo integrado: o que a atleta traz, a lesão, a leitura como dobradiça, emoção e comportamento que se alimentam, a recuperação; por cima, moderadores pessoais e da situação"), defs(TINTA, FOSF)]
p.append(f'<rect x="0" y="0" width="1664" height="70" rx="12" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
p.append(caixa(0, 130, 330, 300, AZUL, AZUL_T))
p.append(seta(340, 280, 420, 280, TINTA, "m0"))
p.append(f'<path d="M560 170 L680 280 L560 390 L440 280 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="6"/>')
p.append(seta(690, 250, 820, 190, TINTA, "m0"))
p.append(seta(690, 310, 820, 370, TINTA, "m0"))
p.append(caixa(830, 130, 380, 120, FOSF, CARTAO))
p.append(caixa(830, 310, 380, 120, FOSF, CARTAO))
p.append(f'<path d="M980 256 V304" stroke="{FOSF}" stroke-width="4" marker-end="url(#m1)"/>')
p.append(f'<path d="M1060 304 V256" stroke="{FOSF}" stroke-width="4" marker-end="url(#m1)"/>')
p.append(seta(1220, 280, 1310, 280, TINTA, "m0"))
p.append(caixa(1320, 130, 344, 300, OXID, OXID_T))
p.append("</svg>")
rs = [rot(20, 18, "Moderadores: fatores pessoais e da situação · momento da temporada · pressão de seleção · apoio em volta", w=1624, tam=26, cor=GLIC, peso=700, alinha="center"),
      rot(20, 150, "Antes da lesão", w=290, tam=28, cor=AZUL, peso=700, serif=True),
      rot(20, 210, "personalidade · história de estresse · recursos para lidar", w=290, tam=24, cor=TINTA, lh=1.4),
      rot(460, 258, "a leitura", w=200, tam=30, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(430, 440, "“acabou o meu ano” ou “disputo a próxima”", w=260, tam=22, cor=MUDO, alinha="center", lh=1.3),
      rot(850, 172, "emoção", w=340, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(850, 352, "comportamento", w=340, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(830, 450, "uma alimenta a outra, o tempo todo", w=380, tam=24, cor=TINTA, alinha="center"),
      rot(1340, 150, "Recuperação", w=310, tam=28, cor=OXID, peso=700, serif=True),
      rot(1340, 210, "física e psicológica", w=300, tam=24, cor=TINTA, lh=1.4)]
S.append({"id": "cascata", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O modelo integrado de resposta à lesão", "titulo": "A leitura da lesão decide o que vem depois",
          "fonte": "Modelo integrado, J Appl Sport Psychol 1998 · a resposta é dinâmica, não segue fases fixas"})

# 3. dois sentidos e identidade
p = [svg_abre(1664, 500, "Dois círculos, lesão e sintomas depressivos, com setas nos dois sentidos; ao lado, um mostrador de identidade atlética"), defs(FOSF)]
p.append(f'<circle cx="190" cy="220" r="170" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="5"/>')
p.append(f'<circle cx="730" cy="220" r="170" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="5"/>')
p.append(f'<path d="M370 170 Q 460 110 550 170" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m0)"/>')
p.append(f'<path d="M550 270 Q 460 330 370 270" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m0)"/>')
p.append(icone("h:bandaged", 140, 120, 100, AZUL))
p.append(icone("t:mood-sad", 680, 120, 100, FOSF))
cx, cy, r = 1330, 330, 230
for k, c in enumerate(["#E6E3DA", GLIC_T, "#E9C88A", FOSF]):
    a0, a1 = math.pi * (1 - k / 4), math.pi * (1 - (k + 1) / 4)
    x0, y0 = cx + r * math.cos(a0), cy - r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
    p.append(f'<path d="M{cx} {cy} L{x0:.0f} {y0:.0f} A{r} {r} 0 0 1 {x1:.0f} {y1:.0f} Z" fill="{c}"/>')
a = math.pi * 0.16
p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 200*math.cos(a):.0f}" y2="{cy - 200*math.sin(a):.0f}" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{TINTA}"/>')
p.append("</svg>")
rs = [rot(40, 300, "lesão", w=300, tam=30, cor=AZUL, peso=700, alinha="center"),
      rot(610, 290, "sintomas depressivos", w=240, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(0, 420, "9 estudos de 3.677 · associação nos dois sentidos · mais sintomas em mulheres", w=920, tam=24, cor=TINTA, alinha="center"),
      rot(1080, 350, "vários papéis", w=200, tam=24, cor=MUDO),
      rot(1480, 350, "só atleta", w=184, tam=24, cor=FOSF, peso=700, alinha="right"),
      rot(1080, 410, "identidade mais forte, sintomas mais graves depois da lesão", w=500, tam=24, cor=TINTA, peso=600, lh=1.3)]
S.append({"id": "sentidos", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceira semana", "titulo": "Lesão e sintoma depressivo andam nos dois sentidos",
          "fonte": "Revisões sistemáticas de 2023: atletas; atletas jovens · a lesão é momento de rastreio de humor"})

# 4. o grupo
p = [svg_abre(1664, 520, "O grupo de treino em círculo no tatame e a atleta lesionada fora dele; três setas trazem ela de volta: apoio emocional, de informação e prático"), defs(OXID)]
p.append(f'<rect x="0" y="20" width="760" height="480" rx="20" fill="{GLIC_T}"/>')
for k in range(9):
    a = 2 * math.pi * k / 9
    x, y = 380 + 220 * math.cos(a), 260 + 170 * math.sin(a)
    p.append(icone("h:person", x - 36, y - 36, 72, AZUL))
p.append(icone("t:karate", 330, 210, 100, "#C9A66B"))
p.append(icone("h:person", 1440, 170, 130, FOSF))
p.append(icone("h:crutches", 1560, 230, 90, FOSF))
apoios = [("emocional", "alguém pergunta e ouve", 140), ("de informação", "prazos honestos, o que é esperado", 290), ("prático", "um lugar e um papel no dojô", 440)]
rs = []
for t, x_, y in apoios:
    p.append(f'<line x1="1380" y1="{y}" x2="800" y2="{y}" stroke="{OXID}" stroke-width="5" marker-end="url(#m0)"/>')
    rs.append(rot(840, y - 80, t, w=300, tam=28, cor=OXID, peso=700, serif=True))
    rs.append(rot(840, y - 40, x_, w=520, tam=24, cor=TINTA))
p.append("</svg>")
rs.append(rot(1400, 330, "“ninguém do dojô me liga”", w=264, tam=26, cor=FOSF, peso=600, alinha="center", lh=1.3))
S.append({"id": "grupo", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O apoio que some", "titulo": "A lesão tira a atleta do grupo quando ela mais precisa dele",
          "fonte": "Fortalecimento no canto do tatame, aquecimento das crianças, observar a pegada de um colega"})

# 5. o ciclo do medo e da evitação
p = [svg_abre(1664, 560, "Ciclo do medo e da evitação: dor, catastrofização, medo, evitação e hipervigilância, desuso e incapacidade, de volta à dor; atalho sem medo para enfrentamento e recuperação"), defs(FOSF, OXID)]
cx, cy, rx, ry = 1060, 290, 440, 220
nos = [("dor", -90), ("catastrofização", -18), ("medo da dor e do movimento", 54), ("evitação e hipervigilância", 126), ("desuso, humor, incapacidade", 198)]
pos = []
for t, ang in nos:
    a = math.radians(ang)
    pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
for i in range(5):
    (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % 5]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ox, oy = (mx - cx) * 0.18, (my - cy) * 0.18
    p.append(f'<path d="M{x1 + (x2-x1)*0.2:.0f} {y1 + (y2-y1)*0.2:.0f} Q {mx+ox:.0f} {my+oy:.0f} {x1 + (x2-x1)*0.8:.0f} {y1 + (y2-y1)*0.8:.0f}" fill="none" stroke="{FOSF}" stroke-width="5" marker-end="url(#m0)"/>')
rs = []
for i, ((t, ang), (x, y)) in enumerate(zip(nos, pos)):
    w = 250
    p.append(f'<rect x="{x - w/2:.0f}" y="{y - 40:.0f}" width="{w}" height="80" rx="40" fill="{FOSF_T if i else TINTA}" stroke="{FOSF}" stroke-width="{0 if i == 0 else 3}"/>')
    rs.append(rot(x - w / 2 + 10, y - 17 if len(t) < 18 else y - 30, t, w=w - 20, tam=24, cor=PAPEL if i == 0 else TINTA, peso=700, alinha="center", lh=1.15))
x0, y0 = pos[0]
p.append(f'<path d="M{x0 - 130:.0f} {y0} H 330" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m1)"/>')
p.append(caixa(0, 20, 320, 110, OXID, OXID_T))
p.append(seta(160, 136, 160, 250, OXID, "m1", esp=6))
p.append(caixa(0, 256, 320, 110, OXID, OXID_T))
p.append("</svg>")
rs += [rot(10, 38, "pouco medo", w=300, tam=26, cor=OXID, peso=700, alinha="center"),
       rot(10, 78, "enfrentamento", w=300, tam=24, cor=TINTA, alinha="center"),
       rot(10, 290, "recuperação", w=300, tam=30, cor=OXID, peso=700, alinha="center", serif=True),
       rot(0, 420, "O ciclo não começa na dor. Começa na leitura da dor.", w=560, tam=30, cor=TINTA, peso=700, serif=True, lh=1.25)]
S.append({"id": "ciclo", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O modelo de medo e evitação", "titulo": "A dor lida como ameaça fecha um círculo",
          "fonte": "Modelo de medo e evitação, Pain 2000 · proposto para a cronificação em uma minoria com dor lombar aguda"})

# 6. três formas de catastrofizar
p = [svg_abre(1664, 540, "Três lentes: ruminação, magnificação e desamparo, cada uma com a frase da judoca e a resposta da equipe")]
lentes = [("t:refresh", "Ruminação", "“eu passo o dia pensando no joelho”", "estrutura: plano diário e metas curtas de processo", AZUL, AZUL_T),
          ("t:zoom-question", "Magnificação", "“essa pontada quer dizer que o enxerto soltou”", "informação com dado: o esperado e o sinal de alarme de verdade", GLIC, GLIC_T),
          ("t:mood-empty", "Desamparo", "“não depende de mim”", "devolver controle: tarefas dela, progresso registrado", FOSF, FOSF_T)]
rs = []
for i, (ic, t, fr, resp, c, ct) in enumerate(lentes):
    x = i * 564
    p.append(caixa(x, 0, 536, 540, c, ct, esp=4, rx=22))
    p.append(f'<circle cx="{x+268}" cy="100" r="74" fill="{CARTAO}" stroke="{c}" stroke-width="4"/>')
    p.append(icone(ic, x + 218, 50, 100, c))
    p.append(f'<line x1="{x+40}" y1="360" x2="{x+496}" y2="360" stroke="{c}" stroke-width="2" stroke-dasharray="8 8"/>')
    rs.append(rot(x + 20, 190, t, w=496, tam=36, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x + 30, 256, fr, w=476, tam=26, cor=TINTA, alinha="center", lh=1.3))
    rs.append(rot(x + 30, 384, resp, w=476, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.3))
p.append("</svg>")
S.append({"id": "lentes", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As três formas de catastrofizar", "titulo": "Cada forma pede uma resposta diferente",
          "fonte": "Escala de catastrofização da dor, 1995: 13 itens de 0 a 4, três dimensões"})

# 7. as curvas do medo
p = [svg_abre(1664, 520, "Esquema: a capacidade física sobe ao longo dos meses; o medo que protege desce acompanhando; o medo que persiste fica alto; faixa no quarto mês")]
x0, x1, y0, y1 = 100, 1300, 440, 40
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{MUDO}" stroke-width="3"/>')
mx = lambda m: x0 + (x1 - x0) * m / 8
p.append(f'<rect x="{mx(3.7):.0f}" y="{y1}" width="{mx(4.3)-mx(3.7):.0f}" height="{y0-y1}" fill="{GLIC_T}"/>')
cap = " ".join(f"{mx(m/10):.0f},{y0 - 300/(1+math.exp(-(m/10-3.2)*1.3)):.0f}" for m in range(0, 81))
prot = " ".join(f"{mx(m/10):.0f},{y0 - 60 - 290*math.exp(-(m/10)/2.2):.0f}" for m in range(0, 81))
pers = " ".join(f"{mx(m/10):.0f},{y0 - 360 + 12*math.sin(m/10):.0f}" for m in range(0, 81))
p.append(f'<polyline points="{cap}" fill="none" stroke="{OXID}" stroke-width="7"/>')
p.append(f'<polyline points="{prot}" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append(f'<polyline points="{pers}" fill="none" stroke="{FOSF}" stroke-width="6" stroke-dasharray="16 10"/>')
p.append("</svg>")
rs = [rot(1320, 40, "medo que persiste", w=344, tam=28, cor=FOSF, peso=700),
      rot(1320, 90, "descolado da capacidade: atrapalha", w=344, tam=24, cor=TINTA, lh=1.3),
      rot(1320, 170, "capacidade física", w=344, tam=28, cor=OXID, peso=700),
      rot(1320, 360, "medo que protege", w=344, tam=28, cor=AZUL, peso=700),
      rot(1320, 410, "desce com a capacidade", w=344, tam=24, cor=TINTA),
      rot(mx(3.2), 450, "4º mês: o parceiro pega a perna", w=mx(4.8) - mx(3.2), tam=24, cor=GLIC, peso=700, alinha="center"),
      rot(x0, 480, "lesão", w=120, tam=24, cor=MUDO),
      rot(x1 - 140, 480, "8 meses", w=140, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "curvas", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarto mês: o medo de nova lesão", "titulo": "O medo protege no começo e atrapalha quando fica",
          "fonte": "Esquema, sem valores medidos · depois da reconstrução do cruzado, cerca de 55% voltam ao esporte competitivo"})

# 8. as frases
p = [svg_abre(1664, 540, "Duas colunas de balões de fala: à esquerda, o que piora; à direita, o que ajuda")]
piora = ["“não é nada, logo você volta”", "“você tem que ser forte”", "“para de pensar nisso”", "“o exame está normal, pode ir”"]
ajuda = ["“vai levar cerca de tanto tempo; esta é a fase de agora”", "“o que você está sentindo é esperado”",
         "“isso depende de você esta semana”", "“o joelho passou; a confiança ainda não, e isso tem tratamento”"]
rs = [rot(0, 0, "Piora", w=780, tam=34, cor=FOSF, peso=700, serif=True), rot(860, 0, "Ajuda", w=804, tam=34, cor=OXID, peso=700, serif=True)]
for i, t in enumerate(piora):
    y = 60 + i * 120
    p.append(f'<path d="M0 {y} h720 a16 16 0 0 1 16 16 v70 a16 16 0 0 1 -16 16 h-600 l-30 22 v-22 h-74 a16 16 0 0 1 -16 -16 v-70 a16 16 0 0 1 16 -16 Z" fill="{FOSF_T}"/>')
    p.append(icone("t:x", 20, y + 26, 48, FOSF))
    rs.append(rot(90, y + 30, t, w=620, tam=28, cor=TINTA, peso=600))
for i, t in enumerate(ajuda):
    y = 60 + i * 120
    p.append(f'<path d="M860 {y} h788 a16 16 0 0 1 16 16 v70 a16 16 0 0 1 -16 16 h-74 v22 l-30 -22 h-684 a16 16 0 0 1 -16 -16 v-70 a16 16 0 0 1 16 -16 Z" fill="{OXID_T}"/>')
    p.append(icone("t:check", 880, y + 26, 48, OXID))
    rs.append(rot(950, y + 18, t, w=690, tam=26, cor=TINTA, peso=600, lh=1.25))
p.append("</svg>")
S.append({"id": "frases", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que se diz", "titulo": "A conversa depois da lesão já é tratamento",
          "fonte": "Nomear o medo o tira do campo do caráter e o coloca no campo do tratamento"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Psicologia da lesão", "titulo": "“Ela pode lutar na próxima?”",
          "regras": ["A leitura da lesão decide a emoção e o comportamento",
                     "Manter no grupo, com um papel; rastrear humor na lesão",
                     "O medo que protege desce; o que fica se trata"],
          "cards": [{"ic": "t:users", "t": "Quem treina e reabilita", "x": "Transforma cada sessão em progresso visível; ouve a frase e reconhece a catastrofização."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Explica a lesão com prazos honestos e rastreia o humor nos momentos de risco."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Entra quando o medo não cede, o humor cai ou a identidade está em jogo."}]})

spec = {"arquivo": "aulas/MOD10/10-06-psicologia-da-lesao-do-impacto-ao-medo-de-nova-lesao.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Psicologia da lesão", "subtitulo": "Do impacto ao medo de nova lesão",
        "nota_capa": "Uma judoca, um randori, e a linha da lesão que a ressonância não mostra.",
        "secoes": {"estacoes": ["O impacto e a leitura.", "capa"], "sentidos": ["Humor, identidade e grupo.", "sentidos"],
                   "ciclo": ["Dor, catastrofização e medo.", "ciclo"], "frases": ["O que se diz.", "frases"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-06.json"), "w"), ensure_ascii=False, indent=1)
print("10-06.json:", len(S), "slides")
