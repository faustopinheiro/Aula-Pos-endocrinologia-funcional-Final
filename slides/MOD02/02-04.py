"""Spec do deck 2.4. Gera 02-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. três números
S.append({"id": "numeros", "tipo": "numeros", "eyebrow": "Queima de gordura no pico, em treinados",
          "titulo": "Meio grama por minuto",
          "numeros": [{"n": "0,52", "x": "grama de gordura por minuto, no pico, em homens treinados em endurance", "cor": "petr"},
                      {"n": "62%", "x": "do VO₂máx: a intensidade em que o pico acontece", "cor": "ambar"},
                      {"n": "± 0,15", "x": "de uma pessoa para outra, com o mesmo treino: quase o dobro", "cor": "verm"}],
          "fonte": "Achten e Jeukendrup, International Journal of Sports Medicine 2003 · 55 homens treinados"})

# 2. a curva
def fat(x, pico=0.52):
    larg = 24 if x < 62.5 else 15
    return pico * math.exp(-((x - 62.5) / larg) ** 2)
xs = [x / 2 for x in range(50, 181)]
def faixa(fx, fy):
    sup = " ".join(f"{fx(x):.1f},{fy(fat(x, 0.67)):.1f}" for x in xs)
    inf = " ".join(f"{fx(x):.1f},{fy(fat(x, 0.37)):.1f}" for x in reversed(xs))
    return f'<polygon points="{sup} {inf}" fill="{OXID}" fill-opacity="0.16"/>'
svg, rs = linhas(1664, 440, "Queima de gordura em gramas por minuto contra a intensidade: sobe até cerca de 0,52 grama por minuto perto de 62% do VO2máx e cai depois; uma faixa larga em volta mostra a variação de uma pessoa para outra",
    [{"nome": "", "cor": OXID, "pts": [(x, fat(x)) for x in xs], "marcas": [(62.5, 0.52)]}],
    25, 90, 0, 0.8, [(25, "25%"), (40, "40%"), (62.5, "62%"), (80, "80%"), (90, "90%")],
    [0, 0.25, 0.5, 0.75], yfmt=lambda v: f"{v:g}".replace(".", ","), margem=(90, 20, 60, 70), extra=faixa)
rs += [rot(1000, 60, "0,52 g/min no pico", w=400, tam=30, cor=TINTA, peso=700, serif=True),
       rot(1180, 110, "acima do pico, cai em gramas, não só em fração", w=420, tam=26, cor=FOSF, peso=700),
       rot(150, 40, "faixa: ± 0,15 g/min, de uma pessoa para outra", w=560, tam=24, cor=OXID, peso=600)]
S.append({"id": "curva", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "Gordura queimada, em gramas por minuto", "titulo": "O pico existe, e é de cada um",
          "fonte": "% do VO₂máx · curva ilustrativa com os valores médios de Achten e Jeukendrup 2003 · a faixa é ± 1 desvio-padrão"})

# 3. tanque e torneira: cada quadrado é uma hora no pico
p = [svg_abre(1664, 420, "Mais de duzentos quadrados, cada um uma hora queimando gordura no pico: é o tempo para esvaziar um estoque de 60 mil quilocalorias a 280 quilocalorias por hora")]
n, col, lado, passo = 214, 27, 30, 36
quad = "".join(f"M{(i % col) * passo} {(i // col) * passo}h{lado}v{lado}h-{lado}z" for i in range(1, n))
p.append(f'<path d="{quad}" fill="{OXID}" fill-opacity="0.75"/>')
p.append(f'<rect x="0" y="0" width="{lado}" height="{lado}" rx="4" fill="{FOSF}"/>')
p.append(f'<line x1="1000" y1="0" x2="1000" y2="420" stroke="{GRADE}" stroke-width="2"/></svg>')
rs = [rot(0, 310, "cada quadrado = 1 hora queimando gordura no pico", w=960, tam=26, cor=TINTA, peso=600),
      rot(0, 350, "o vermelho é a primeira hora", w=960, tam=24, cor=FOSF),
      rot(1050, 0, "~30 g/h", w=600, tam=64, cor=TINTA, peso=700, serif=True),
      rot(1050, 84, "≈ 280 kcal por hora, no melhor cenário", w=600, tam=26),
      rot(1050, 170, "> 60.000", w=600, tam=64, cor=OXID, peso=700, serif=True),
      rot(1050, 254, "kcal no tanque de gordura, mesmo em adulto magro", w=600, tam=26),
      rot(1050, 330, "Mais de 200 horas para esvaziar.", w=600, tam=30, cor=TINTA, peso=700)]
S.append({"id": "tanque", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A conta", "titulo": "Tanque imenso, torneira estreita"})

# 4. a régua da razão de troca
p = [svg_abre(1664, 420, "Razão de troca respiratória de 0,70 a 1,00: em 0,70 a energia vem toda da gordura, em 0,85 mais ou menos meio a meio, em 1,00 toda do carboidrato")]
rers = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]
rs = []
base, alt, larg, passo, x0 = 320, 270, 150, 220, 90
for i, r in enumerate(rers):
    g = (1 - r) / 0.30
    x = x0 + i * passo
    hg = alt * g
    if hg > 0:
        p.append(f'<rect x="{x}" y="{base-hg:.1f}" width="{larg}" height="{hg:.1f}" rx="4" fill="{OXID}"/>')
    if alt - hg > 0:
        p.append(f'<rect x="{x}" y="{base-alt}" width="{larg}" height="{max(alt-hg-2,0):.1f}" rx="4" fill="{GLIC}"/>')
    rs.append(rot(x - 20, base + 14, f"{r:.2f}".replace(".", ","), w=larg + 40, tam=30, cor=TINTA, peso=700, alinha="center", serif=True))
p.append(f'<rect x="{x0}" y="4" width="28" height="28" rx="4" fill="{OXID}"/><rect x="{x0+220}" y="4" width="28" height="28" rx="4" fill="{GLIC}"/></svg>')
rs += [rot(x0 + 40, 0, "gordura", w=170, tam=26, cor=TINTA, peso=600),
       rot(x0 + 260, 0, "carboidrato", w=260, tam=26, cor=TINTA, peso=600),
       rot(x0, 376, "gás carbônico solto ÷ oxigênio consumido · proporções aproximadas", w=1400, tam=24, cor=MUDO)]
S.append({"id": "regua", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Como se mede: pelo ar", "titulo": "A razão de troca respiratória diz a mistura",
          "fonte": "Proporções a partir da tabela de Péronnet e Massicotte, 1991"})

# 5. quando a régua mente
rer = [(x, 0.80 + 0.20 * (x / 70) ** 1.6 if x <= 70 else 1.0 + 0.12 * ((x - 70) / 30) ** 1.3) for x in range(0, 101, 2)]
def zona(fx, fy):
    return f'<rect x="{fx(0):.1f}" y="{fy(1.15):.1f}" width="{fx(100)-fx(0):.1f}" height="{fy(1.0)-fy(1.15):.1f}" fill="{FOSF_T}"/>'
svg, rs = linhas(1664, 400, "A razão de troca respiratória sobe com a intensidade e passa de 1,00; acima dessa linha, o gás carbônico extra vem do tamponamento e não da queima de combustível",
    [{"nome": "", "cor": TINTA, "pts": rer, "esp": 5}], 0, 100, 0.75, 1.15, [(0, "leve"), (50, "moderado"), (100, "máximo")],
    [0.8, 0.9, 1.0, 1.1], yfmt=lambda v: f"{v:.2f}".replace(".", ","), margem=(100, 20, 60, 30), extra=zona)
rs += [rot(130, 30, "acima de 1,00: CO₂ do tamponamento, não é combustível", w=900, tam=28, cor=FOSF, peso=700),
       rot(900, 250, "abaixo: vale, se a intensidade estiver estável", w=700, tam=26, cor=TINTA, peso=600)]
S.append({"id": "mente", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "Duas limitações", "titulo": "Em intensidade alta, a régua deixa de medir combustível",
          "destaque": "O mesmo CO₂ que estraga a medida de combustível é o que deixa enxergar o limiar na ergoespirometria.",
          "fonte": "Esquema, sem valores medidos"})

# 6. o caminho do ácido graxo
p = [svg_abre(1664, 440, "Cinco etapas do ácido graxo: sair do adipócito, viajar no sangue presa à albumina, atravessar a membrana da fibra, passar pela porta da carnitina e entrar na mitocôndria; o glicogênio já está dentro da fibra, a um passo da via"),
     "<defs>" + seta_marker("g1", OXID) + seta_marker("g2", GLIC) + "</defs>"]
etapas = [("1", "Sair do", "adipócito"), ("2", "Viajar presa", "à albumina"), ("3", "Atravessar", "a membrana"),
          ("4", "Porta da", "carnitina (CPT-1)"), ("5", "Entrar na", "mitocôndria")]
rs = []
w, gap = 290, 44
for i, (nn, a, b) in enumerate(etapas):
    x = i * (w + gap)
    p.append(caixa(x, 40, w, 150, OXID))
    p.append(f'<circle cx="{x+36}" cy="40" r="26" fill="{OXID}"/>')
    rs.append(rot(x + 10, 22, nn, w=52, tam=28, cor=CLARO, peso=700, alinha="center"))
    rs.append(rot(x + 10, 76, a + "<br>" + b, w=w - 20, tam=28, cor=TINTA, peso=600, alinha="center"))
    if i < 4:
        p.append(f'<path d="M{x+w+4} 115 L{x+w+gap-6} 115" stroke="{OXID}" stroke-width="5" marker-end="url(#g1)"/>')
xg = 4 * (w + gap)
p.append(caixa(xg, 300, w, 110, GLIC, GLIC_T))
p.append(f'<path d="M{xg+w/2} 296 L{xg+w/2} 200" stroke="{GLIC}" stroke-width="6" marker-end="url(#g2)"/>')
p.append("</svg>")
rs += [rot(xg, 316, "Glicogênio", w=w, tam=28, cor=TINTA, peso=700, alinha="center"),
       rot(xg, 356, "já dentro da fibra", w=w, tam=24, alinha="center"),
       rot(0, 250, "Cinco etapas, cinco gargalos possíveis. Cada uma tem a sua velocidade máxima.", w=1200, tam=30, cor=TINTA, peso=700, serif=True),
       rot(xg - 460, 330, "o carboidrato, a um passo →", w=440, tam=26, cor=GLIC, peso=700, alinha="right")]
S.append({"id": "caminho", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por que a torneira é estreita", "titulo": "O longo caminho da gordura até virar ATP"})

# 7. rendimento por litro de oxigênio
p = [svg_abre(1664, 300, "Energia por litro de oxigênio: carboidrato cerca de 5,05 quilocalorias, gordura cerca de 4,69"),
     f'<line x1="420" y1="0" x2="420" y2="240" stroke="{MUDO}" stroke-width="2"/>',
     f'<rect x="422" y="20" width="{5.05*220:.0f}" height="80" rx="4" fill="{GLIC}"/>',
     f'<rect x="422" y="140" width="{4.69*220:.0f}" height="80" rx="4" fill="{OXID}"/>', "</svg>"]
rs = [rot(0, 40, "Carboidrato", w=390, tam=32, cor=TINTA, peso=700, alinha="right"),
      rot(0, 160, "Gordura", w=390, tam=32, cor=TINTA, peso=700, alinha="right"),
      rot(422 + 5.05 * 220 - 300, 38, "~5,05 kcal/L", w=280, tam=34, cor=CLARO, peso=700, alinha="right", serif=True),
      rot(422 + 4.69 * 220 - 300, 158, "~4,69 kcal/L", w=280, tam=34, cor=CLARO, peso=700, alinha="right", serif=True),
      rot(422, 250, "quilocalorias por litro de oxigênio consumido · eixo começa no zero", w=1100, tam=24, cor=MUDO)]
S.append({"id": "litro", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O detalhe que fecha o argumento", "titulo": "Quando o oxigênio falta, o carboidrato rende mais por litro",
          "destaque": "Sete a oito por cento parece pouco. Em intensidade alta, é decisivo. A troca de combustível não é defeito: é escolha econômica correta.",
          "fonte": "Péronnet e Massicotte, Canadian Journal of Sport Sciences 1991"})

# 8. a porta da carnitina
p = [svg_abre(1664, 420, "A porta da mitocôndria depende da carnitina; com o fluxo glicolítico alto, a carnitina livre fica ocupada e o ácido graxo fica sem passagem"),
     "<defs>" + seta_marker("p1", GLIC) + seta_marker("p2", OXID) + "</defs>",
     f'<ellipse cx="1380" cy="210" rx="280" ry="180" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>',
     f'<rect x="1082" y="150" width="40" height="120" rx="8" fill="{TINTA}"/>']
for k, (x, y, livre) in enumerate([(720, 110, False), (800, 170, False), (720, 240, False), (820, 300, True)]):
    p.append(f'<circle cx="{x}" cy="{y}" r="26" fill="{GLIC if not livre else OXID}" stroke="{CLARO}" stroke-width="3"/>')
p.append(f'<path d="M20 90 Q360 70 690 110" fill="none" stroke="{GLIC}" stroke-width="10" marker-end="url(#p1)"/>')
p.append(f'<path d="M60 330 Q500 350 1060 230" fill="none" stroke="{OXID}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#p2)"/>')
p.append(f'<line x1="990" y1="200" x2="1050" y2="270" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
p.append(f'<line x1="1050" y1="200" x2="990" y2="270" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
p.append("</svg>")
rs = [rot(20, 20, "fluxo glicolítico alto", w=500, tam=28, cor=GLIC, peso=700),
      rot(560, 10, "carnitina ocupada", w=400, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(60, 360, "ácido graxo esperando na porta", w=560, tam=28, cor=OXID, peso=700),
      rot(1122, 280, "CPT-1", w=140, tam=26, cor=TINTA, peso=700),
      rot(1240, 190, "Mitocôndria", w=300, tam=32, cor=OXID, peso=700, alinha="center")]
S.append({"id": "porta", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As duas vias competem", "titulo": "O carboidrato fecha a porta do concorrente",
          "destaque": "Não existe intensidade alta tocada a gordura. Não é falta de treino. É arquitetura.", "destaque_cor": "tinta",
          "fonte": "Esquema de uma das explicações mais aceitas · Hargreaves e Spriet, Nature Metabolism 2020"})

# 9. a zona de queima na aritmética
p = [svg_abre(1664, 320, "Duas sessões: 8 quilocalorias por minuto com 60% de gordura dá 4,8 de gordura; 14 quilocalorias por minuto com 35% de gordura dá 4,9 de gordura")]
esc, x0 = 80, 460
for y, tot, g in [(20, 8, 4.8), (170, 14, 4.9)]:
    p.append(f'<rect x="{x0}" y="{y}" width="{g*esc-2:.0f}" height="100" rx="4" fill="{OXID}"/>')
    p.append(f'<rect x="{x0+g*esc:.0f}" y="{y}" width="{(tot-g)*esc:.0f}" height="100" rx="4" fill="{GLIC}"/>')
p.append("</svg>")
rs = [rot(0, 26, "Mais leve<br>8 kcal/min · 60% gordura", w=430, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(0, 176, "Mais forte<br>14 kcal/min · 35% gordura", w=430, tam=28, cor=TINTA, peso=600, alinha="right"),
      rot(x0, 46, "4,8", w=4.8 * esc, tam=44, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(x0, 196, "4,9", w=4.9 * esc, tam=44, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(x0 + 520, 280, "os números: kcal de gordura por minuto", w=600, tam=24, cor=TINTA),
      rot(x0, 280, "gordura", w=200, tam=24, cor=OXID, peso=700), rot(x0 + 220, 280, "carboidrato", w=260, tam=24, cor=GLIC, peso=700)]
S.append({"id": "zona", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A zona de queima, na aritmética", "titulo": "Proporção não é quantidade",
          "destaque": "O que decide quanto se queima é taxa vezes tempo, e nunca a fração sozinha.", "destaque_cor": "verm"})

# 10. dias e semanas
S.append({"id": "semanas", "tipo": "duas", "eyebrow": "O erro maior é conceitual", "titulo": "Composição corporal se decide em semanas",
          "esq": {"t": "Durante a sessão", "cor": "ambar",
                  "itens": ["A mistura de combustível muda com a intensidade", "Em jejum, queima-se mais gordura naquela hora", "Nada disso fica guardado como crédito"]},
          "dir": {"t": "Ao longo de dias e semanas", "cor": "petr",
                  "itens": ["O que decide é o balanço de energia", "Jejum ou alimentada, com a mesma dieta: composição parecida em quatro semanas", "A variável que importa é a intensidade que a pessoa sustenta"]},
          "destaque": "Treino longo e leve vale muito, por capilar, mitocôndria e tolerância. Só não vale pelo motivo que costuma ser vendido.",
          "fonte": "Schoenfeld e colaboradores, Journal of the International Society of Sports Nutrition 2014"})

# 11. quebrar
S.append({"id": "quebra", "tipo": "duas", "eyebrow": "O atleta que quebra", "titulo": "A cabeça foi junto, ou só a perna?",
          "esq": {"t": "Hipoglicemia", "cor": "verm",
                  "itens": ["Central: o glicogênio do fígado acabou", "Confusão, suor frio, tontura, irritação", "Melhora em minutos com carboidrato rápido", "Previne-se comendo durante a prova"]},
          "dir": {"t": "Glicogênio muscular esgotado", "cor": "ambar",
                  "itens": ["Local: o estoque da fibra acabou", "Cabeça lúcida, perna que não entrega", "Não melhora em minutos: nenhum gel enche a fibra", "Previne-se nos dias anteriores e no ritmo da primeira metade"]}})

# 12. o teto do intestino
p = [svg_abre(1664, 440, "O intestino tem uma porta para glicose e outra para frutose; nos ciclistas, a glicose sozinha chegou a 1,06 grama por minuto e glicose com frutose a 1,75"),
     "<defs>" + seta_marker("i1", GLIC) + seta_marker("i2", AZUL) + "</defs>",
     f'<rect x="0" y="180" width="660" height="60" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>',
     f'<rect x="150" y="176" width="70" height="68" rx="10" fill="{GLIC}"/>',
     f'<rect x="440" y="176" width="70" height="68" rx="10" fill="{AZUL}"/>']
for k in range(6):
    p.append(f'<circle cx="{110 + (k%3)*40}" cy="{70 + (k//3)*40}" r="14" fill="{GLIC}"/>')
for k in range(3):
    p.append(f'<circle cx="{420 + k*40}" cy="90" r="14" fill="{AZUL}"/>')
p += [f'<path d="M185 140 L185 330" stroke="{GLIC}" stroke-width="6" marker-end="url(#i1)"/>',
      f'<path d="M475 120 L475 330" stroke="{AZUL}" stroke-width="6" marker-end="url(#i2)"/>',
      f'<line x1="880" y1="380" x2="1600" y2="380" stroke="{MUDO}" stroke-width="2"/>',
      f'<rect x="940" y="{380-1.06*180:.0f}" width="220" height="{1.06*180:.0f}" rx="4" fill="{GLIC}"/>',
      f'<rect x="1260" y="{380-1.75*180:.0f}" width="220" height="{1.75*180:.0f}" rx="4" fill="{GLIC}"/>',
      "</svg>"]
rs = [rot(0, 10, "no intestino", w=400, tam=26, cor=MUDO),
      rot(0, 350, "a porta da glicose satura em ~1 g/min", w=430, tam=24, cor=GLIC, peso=700),
      rot(450, 350, "a frutose usa outra porta", w=240, tam=24, cor=AZUL, peso=700),
      rot(940, 380 - 1.06 * 180 - 50, "1,06", w=220, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1260, 380 - 1.75 * 180 - 50, "1,75", w=220, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(900, 392, "glicose", w=300, tam=24, cor=TINTA, alinha="center"),
      rot(1220, 392, "glicose + frutose", w=300, tam=24, cor=TINTA, alinha="center")]
S.append({"id": "intestino", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O outro teto não está no músculo", "titulo": "O teto do carboidrato está no intestino",
          "fonte": "g/min queimados do que foi ingerido, no pico · Jentjens e Jeukendrup, British Journal of Nutrition 2005 · a mistura foi ingerida em quantidade maior"})

# 13. o que o número decide
S.append({"id": "decide", "tipo": "numeros", "eyebrow": "O que esse número decide", "titulo": "O plano de prova, o estômago e o treino",
          "numeros": [{"n": "60 g/h", "x": "de uma fonte só: até aqui dá para queimar", "cor": "ambar"},
                      {"n": "90 g/h", "x": "de fontes combinadas, em prova de 2 h 30 ou mais", "cor": "petr"},
                      {"n": "treina-se", "x": "o intestino se adapta: ninguém testa 90 g/h no dia da prova", "cor": "verm"}],
          "destaque": "120 g/h de uma fonte só e dor de estômago não é problema de estômago. É aritmética de transportador. Quanto, de quê e quando é do nutricionista.",
          "fonte": "Jeukendrup, Sports Medicine 2014"})

# 14. a cascata da biogênese
p = [svg_abre(1664, 440, "Contração repetida gera três sinais, energia baixa pela AMPK, cálcio e sinal redox; os três convergem no PGC-1 alfa, que aciona o núcleo e o DNA da mitocôndria, e o resultado é mitocôndria nova"),
     "<defs>" + seta_marker("c1", TINTA) + "</defs>",
     f'<rect x="0" y="160" width="260" height="120" rx="14" fill="{TINTA}"/>']
for i, cor in enumerate([OXID, FOSF, AZUL]):
    y = 20 + i * 140
    p.append(caixa(360, y, 320, 120, cor))
    p.append(f'<path d="M264 220 L352 {y+60}" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>')
    p.append(f'<path d="M684 {y+60} L772 220" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>')
p += [f'<rect x="780" y="160" width="260" height="120" rx="14" fill="{GLIC}"/>',
      caixa(1130, 60, 240, 110, TINTA), caixa(1130, 270, 240, 110, TINTA),
      f'<path d="M1044 205 L1122 115" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>',
      f'<path d="M1044 235 L1122 325" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>',
      f'<ellipse cx="1560" cy="220" rx="100" ry="70" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>',
      f'<path d="M1374 115 L1462 190" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>',
      f'<path d="M1374 325 L1462 250" stroke="{TINTA}" stroke-width="4" marker-end="url(#c1)"/>', "</svg>"]
rs = [rot(0, 184, "Contração<br>repetida", w=260, tam=30, cor=CLARO, peso=700, alinha="center"),
      rot(360, 36, "Energia baixa", w=320, tam=28, cor=TINTA, peso=700, alinha="center"), rot(360, 76, "AMPK", w=320, tam=26, cor=OXID, alinha="center"),
      rot(360, 176, "Cálcio", w=320, tam=28, cor=TINTA, peso=700, alinha="center"), rot(360, 216, "a cada contração", w=320, tam=24, cor=FOSF, alinha="center"),
      rot(360, 316, "Sinal redox", w=320, tam=28, cor=TINTA, peso=700, alinha="center"), rot(360, 356, "cadeia respiratória", w=320, tam=24, cor=AZUL, alinha="center"),
      rot(780, 198, "PGC-1α", w=260, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1130, 94, "Núcleo", w=240, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(1130, 290, "DNA da<br>mitocôndria", w=240, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(1460, 186, "Mitocôndria<br>nova", w=200, tam=26, cor=OXID, peso=700, alinha="center")]
S.append({"id": "cascata", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Como o sistema melhora", "titulo": "Quem constrói mitocôndria é a contração",
          "destaque": "Não é hormônio do crescimento nem IGF-1. É um programa local, disparado pelo trabalho do músculo. E é de graça.", "destaque_cor": "verm"})

# 15. pulsos de sinal
p = [svg_abre(1664, 400, "Duas semanas: seis sessões moderadas geram seis pulsos de sinal que decaem; duas sessões muito longas geram dois pulsos grandes com dias vazios entre eles")]
def pulsos(dias, alt, y0, h):
    pts = []
    for k in range(0, 7 * 48 + 1):
        t = k / 48
        v = sum(alt * math.exp(-(t - d) / 0.5) for d in dias if t >= d)
        pts.append((t, min(v, 1.0)))
    xpx = lambda t: 260 + t / 7 * 1380
    ypx = lambda v: y0 + h - v * h
    return (f'<polygon points="{xpx(0):.1f},{y0+h} ' + " ".join(f"{xpx(t):.1f},{ypx(v):.1f}" for t, v in pts) +
            f' {xpx(7):.1f},{y0+h}" fill="{OXID}" fill-opacity="0.8"/>'
            f'<line x1="{xpx(0):.1f}" y1="{y0+h}" x2="{xpx(7):.1f}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
p.append(pulsos([0, 1, 2, 3.5, 4.5, 5.5], 0.55, 20, 130))
p.append(pulsos([1, 5], 0.95, 210, 130))
p.append("</svg>")
rs = [rot(0, 50, "6 sessões<br>moderadas", w=230, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 240, "2 sessões<br>heroicas", w=230, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(260, 356, "uma semana · cada sessão é um pulso de sinal que decai em horas a poucos dias", w=1380, tam=24, cor=MUDO)]
S.append({"id": "pulsos", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A consequência de prescrição", "titulo": "Frequência importa muito",
          "fonte": "Esquema, sem valores medidos"})

# 16. conteúdo e função
p = [svg_abre(1664, 400, "À esquerda, conteúdo mitocondrial: muitas mitocôndrias; à direita, função mitocondrial: quanto cada uma respira"),
     caixa(0, 0, 800, 330, BORDA, CARTAO, 2), caixa(864, 0, 800, 330, BORDA, CARTAO, 2)]
import random
random.seed(5)
for k in range(22):
    cx, cy = 80 + (k % 8) * 90 + random.randint(-10, 10), 110 + (k // 8) * 80 + random.randint(-8, 8)
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="34" ry="20" fill="{OXID}" fill-opacity="0.35" stroke="{OXID}" stroke-width="2"/>')
for k in range(4):
    cx, cy = 1064 + (k % 2) * 400, 130 + (k // 2) * 110
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="110" ry="44" fill="{OXID}" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<path d="M{cx-80} {cy} q15 -26 30 0 t30 0 t30 0 t30 0 t30 0" fill="none" stroke="{CLARO}" stroke-width="4"/>')
p.append("</svg>")
rs = [rot(30, 20, "Conteúdo: quantas existem", w=740, tam=30, cor=TINTA, peso=700),
      rot(894, 20, "Função: quanto cada uma respira", w=740, tam=30, cor=TINTA, peso=700),
      rot(0, 350, "As duas podem andar em direções diferentes.", w=1664, tam=30, cor=TINTA, peso=700, serif=True)]
S.append({"id": "conteudo", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Volume ou intensidade? Os dois funcionam.", "titulo": "Conteúdo não é função",
          "fonte": "Bishop e colaboradores, Physiology 2019 · controvérsia atual"})

# 17. o que derruba sem ser treino
p = [svg_abre(1664, 440, "Quatro setas descendo sobre uma mitocôndria: energia disponível baixa, sono curto, inatividade e idade; uma quinta seta tracejada: antioxidante em dose alta"),
     "<defs>" + seta_marker("d1", FOSF) + seta_marker("d2", MUDO) + "</defs>",
     f'<ellipse cx="832" cy="370" rx="360" ry="62" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>']
itens = [("Energia disponível baixa", "menos combustível e menos motor"), ("Sono curto", "a mesma sessão custa mais"),
         ("Inatividade", "desmonta em poucas semanas"), ("Idade", "muito do declínio é sofá")]
rs = [rot(632, 352, "Função oxidativa", w=400, tam=30, cor=OXID, peso=700, alinha="center")]
for i, (t, s) in enumerate(itens):
    x = 20 + i * 330
    p.append(f'<path d="M{x+150} 146 L{560 + i*90} 296" stroke="{FOSF}" stroke-width="6" marker-end="url(#d1)"/>')
    rs += [rot(x, 0, t, w=300, tam=28, cor=TINTA, peso=700, alinha="center"),
           rot(x, 76, s, w=300, tam=24, alinha="center")]
p.append(f'<path d="M1500 146 L1150 320" stroke="{MUDO}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#d2)"/></svg>')
rs += [rot(1340, 0, "Antioxidante em dose alta", w=324, tam=28, cor=TINTA, peso=700, alinha="center"),
       rot(1340, 76, "vitamina C e E atenuaram a adaptação", w=324, tam=24, alinha="center")]
S.append({"id": "derruba", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que derruba sem ser treino", "titulo": "A função oxidativa sente a vida inteira",
          "fonte": "Paulsen e colaboradores, Journal of Physiology 2014 · dieta rica em frutas e verduras é outra coisa"})

# 18. treina e não melhora
p = [svg_abre(1664, 400, "Bifurcação: treina e não melhora; ou o estímulo está errado e se resolve na planilha, ou a matéria-prima não chega e se resolve na conta de energia, sono e recuperação"),
     "<defs>" + seta_marker("b1", TINTA) + "</defs>",
     f'<rect x="0" y="140" width="420" height="120" rx="16" fill="{TINTA}"/>',
     caixa(760, 10, 904, 150, AZUL), caixa(760, 240, 904, 150, FOSF),
     f'<path d="M424 180 C600 180 600 85 752 85" fill="none" stroke="{TINTA}" stroke-width="6" marker-end="url(#b1)"/>',
     f'<path d="M424 220 C600 220 600 315 752 315" fill="none" stroke="{TINTA}" stroke-width="6" marker-end="url(#b1)"/>', "</svg>"]
rs = [rot(0, 170, "Treina e<br>não melhora", w=420, tam=34, cor=CLARO, peso=700, alinha="center"),
      rot(800, 34, "O estímulo está errado", w=840, tam=32, cor=TINTA, peso=700),
      rot(800, 88, "problema de prescrição: resolve-se na planilha", w=840, tam=26),
      rot(800, 264, "A matéria-prima não chega", w=840, tam=32, cor=TINTA, peso=700),
      rot(800, 318, "energia, sono, recuperação: nenhuma planilha resolve", w=840, tam=26)]
S.append({"id": "hipoteses", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O caso mais comum do consultório", "titulo": "Duas hipóteses, e quase todo mundo só pensa na primeira",
          "destaque": "É por isso que tanta gente treina mais e melhora menos."})

# 19. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Três tetos, três perguntas",
          "regras": ["Que adaptação eu quero produzir nesta pessoa?", "O que a conta de energia dela permite pagar?", "Em qual teto ela está batendo agora?"],
          "cards": [{"t": "Gordura", "x": "~0,5 g/min. Quem escolhe “zona” para emagrecer bate aqui."},
                    {"t": "Carboidrato", "x": "~1 g/min de uma fonte, ~1,75 combinado. Quem toma mais gel bate aqui."},
                    {"t": "Capacidade instalada", "x": "O único que se move: devagar, por volume e frequência."}],
          "quem": "O tanque é imenso. A torneira é estreita."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['curva', 'tanque', 'regua', 'litro', 'zona', 'semanas', 'intestino', 'cascata', 'derruba', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-04-metabolismo-oxidativo-e-uso-de-substratos.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Meio grama por minuto", "subtitulo": "Metabolismo oxidativo e uso de substratos",
        "nota_capa": "Entra pelo número.",
        "secoes": {"numero": ["O pico de gordura, a curva e como se mede.", "capa"],
                   "porque": ["Por que a torneira é estreita e o erro da zona de queima.", "litro"],
                   "carbo": ["O atleta que quebra e o teto do intestino.", "semanas"],
                   "melhora": ["Como a mitocôndria cresce e o que a derruba.", "cascata"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-04.json"), "w"), ensure_ascii=False, indent=1)
print("02-04.json:", len(S), "slides")
