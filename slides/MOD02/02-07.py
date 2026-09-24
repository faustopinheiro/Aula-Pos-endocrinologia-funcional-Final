"""Spec do deck 2.7. Gera 02-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. trinta e cinco dias
p = [svg_abre(1664, 380, "Depois de 35 dias de treino de força pesado: força máxima mais 39%, ativação elétrica do músculo mais 35%, área do quadríceps mais 3,5 a 5% aos 20 dias"),
     f'<line x1="520" y1="0" x2="520" y2="340" stroke="{MUDO}" stroke-width="2"/>']
esc = 26
for i, (v, cor) in enumerate([(38.9, FOSF), (34.8, AZUL), (5.2, OXID)]):
    p.append(f'<rect x="522" y="{20 + i*110}" width="{v*esc:.0f}" height="80" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(0, 36, "Força máxima", w=490, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 146, "Ativação elétrica do músculo", w=490, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 256, "Área do quadríceps (aos 20 dias)", w=490, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(522 + 38.9 * esc - 220, 36, "+39%", w=200, tam=38, cor=CLARO, peso=700, alinha="right", serif=True),
      rot(522 + 34.8 * esc - 220, 146, "+35%", w=200, tam=38, cor=CLARO, peso=700, alinha="right", serif=True),
      rot(522 + 5.2 * esc + 20, 256, "+3,5 a 5%", w=300, tam=38, cor=TINTA, peso=700, serif=True)]
S.append({"id": "numero", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "35 dias de treino pesado, jovens destreinados", "titulo": "A força subiu muito mais que o músculo",
          "destaque": "A força veio, em boa parte, do sistema nervoso.", "destaque_cor": "tinta",
          "fonte": "Seynnes, de Boer e Narici, Journal of Applied Physiology 2007"})

# 2. força x tamanho
fo = [(w, 100 * (1 - math.exp(-w / 5))) for w in [x / 4 for x in range(0, 49)]]
ta = [(w, 100 * (max(0, w - 1) / 11) ** 1.6 * 0.55) for w in [x / 4 for x in range(0, 49)]]
def entre(fx, fy):
    a = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in fo)
    b = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in reversed(ta))
    return f'<polygon points="{a} {b}" fill="{AZUL}" fill-opacity="0.15"/>'
svg, rs = linhas(1664, 400, "Ao longo de doze semanas a força sobe desde a primeira semana e o tamanho do músculo sobe mais devagar; a distância entre as duas no começo é o ganho neural",
    [{"nome": "", "cor": FOSF, "pts": fo}, {"nome": "", "cor": OXID, "pts": ta}], 0, 12, 0, 110,
    [(0, "semana 0"), (4, "4"), (8, "8"), (12, "12")], [], margem=(40, 20, 60, 30), extra=entre)
rs += [rot(900, 10, "força", w=300, tam=30, cor=FOSF, peso=700),
       rot(1300, 300, "tamanho do músculo", w=340, tam=30, cor=OXID, peso=700, alinha="right"),
       rot(300, 150, "ganho neural", w=300, tam=30, cor=AZUL, peso=700, serif=True)]
S.append({"id": "desenho", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "O desenho clássico", "titulo": "No começo, a distância entre as curvas é nervo",
          "fonte": "Esquema · Folland e Williams, Sports Medicine 2007"})

# 3. cinco mudanças
S.append({"id": "cinco", "tipo": "lista", "eyebrow": "O que muda no sistema nervoso", "titulo": "Cinco mudanças no comando", "gap_itens": 18,
          "itens": [{"t": "Mais unidades motoras recrutadas", "x": "inclusive as mais difíceis de chamar"},
                    {"t": "Disparo mais rápido", "x": "impulsos chegando com mais frequência"},
                    {"t": "Menos freio do antagonista", "x": "o músculo oposto para de segurar o movimento"},
                    {"t": "Coordenação entre músculos", "x": "os que ajudam entram na hora certa"},
                    {"t": "Aprendizado da tarefa", "x": "simplesmente saber fazer o movimento"}]})

# 4. duas consequências
S.append({"id": "especifico", "tipo": "cards", "por_linha": 2, "eyebrow": "Duas consequências que quase ninguém explica",
          "titulo": "O ganho do nervo tem endereço",
          "cards": [{"t": "O ganho é específico", "x": "Melhora naquele padrão, naquela amplitude, naquela velocidade. Para levantar do chão aos setenta, o exercício precisa parecer com levantar do chão.", "cor": "petr"},
                    {"t": "Trocou de aparelho e a carga caiu", "x": "Não é perda de força. É o comando sendo reaprendido num padrão novo. Explicar isso evita abandono.", "cor": "ambar"}]})

# 5. educação cruzada
p = [svg_abre(1664, 400, "Duas pernas: a treinada ganha força; a outra, sem carga nenhuma, ganha perto de 12% de força também"),
     f'<line x1="640" y1="360" x2="1640" y2="360" stroke="{MUDO}" stroke-width="2"/>',
     f'<rect x="760" y="{360-300}" width="260" height="300" rx="4" fill="{FOSF}"/>',
     f'<rect x="1260" y="{360-60}" width="260" height="60" rx="4" fill="{AZUL}"/>']
# duas pernas estilizadas
for x, cor, op in [(150, FOSF, 1), (380, AZUL, 0.55)]:
    p.append(f'<rect x="{x}" y="30" width="110" height="170" rx="50" fill="{cor}" fill-opacity="{op}"/>')
    p.append(f'<rect x="{x+10}" y="200" width="90" height="150" rx="40" fill="{cor}" fill-opacity="{op}"/>')
p.append('</svg>')
rs = [rot(80, 358, "treinada", w=250, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(310, 358, "sem carga", w=250, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(760, 10, "ganho grande", w=260, tam=28, cor=FOSF, peso=700, alinha="center"),
      rot(1260, 250, "~12%", w=260, tam=40, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1180, 60, "a perna que não treinou", w=420, tam=28, cor=AZUL, peso=700, alinha="center")]
S.append({"id": "cruzada", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A prova de que o começo é nervoso", "titulo": "Educação cruzada",
          "destaque": "Membro imobilizado por fratura ou cirurgia: treinar o lado saudável atenua a perda do lado parado. Barato e pouco usado.",
          "destaque_cor": "ambar", "fonte": "Manca e colaboradores, European Journal of Applied Physiology 2017 · meta-análise · barra da perna treinada ilustrativa"})

# 6. unidade motora
p = [svg_abre(1664, 400, "Uma unidade motora pequena, com um motoneurônio e cerca de dez fibras, como nos músculos do olho; e uma grande, com um motoneurônio e mais de mil fibras, como no gastrocnêmio")]
def um(x0, n, raio, cor, larg):
    s = [f'<circle cx="{x0}" cy="100" r="{raio}" fill="{cor}"/>']
    alvo = []
    cols = max(1, int(larg // 22))
    for k in range(n):
        fx = x0 - larg / 2 + (k % cols) * 22 + 11
        fy = 250 + (k // cols) * 22
        alvo.append((fx, fy))
        s.append(f'<rect x="{fx-8:.0f}" y="{fy-8:.0f}" width="16" height="16" rx="3" fill="{cor}" fill-opacity="0.7"/>')
    s.append(f'<path d="M{x0} {100+raio} L{x0} 220" stroke="{cor}" stroke-width="5"/>')
    for fx, fy in alvo[::max(1, n // 12)]:
        s.append(f'<path d="M{x0} 220 L{fx:.0f} {fy-8:.0f}" stroke="{cor}" stroke-width="2" opacity="0.6"/>')
    return s
p += um(300, 10, 22, OXID, 240)
p += um(1150, 140, 46, FOSF, 900)
p.append("</svg>")
rs = [rot(80, 0, "Músculo do olho", w=440, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(80, 300, "~10 fibras por unidade: precisão", w=440, tam=26, cor=OXID, peso=700, alinha="center"),
      rot(700, 0, "Gastrocnêmio", w=900, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(700, 350, "> 1.000 fibras por unidade: força (desenho reduzido)", w=900, tam=24, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "unidade", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A unidade de conta do sistema", "titulo": "Um motoneurônio e todas as fibras que ele comanda",
          "destaque": "Quando ele dispara, todas as fibras dele contraem. Não existe contrair metade de uma unidade motora."})

# 7. princípio do tamanho
xs = list(range(0, 101, 2))
camadas = [(0, OXID, "pequenas: lentas, resistentes"), (35, AZUL, "médias"), (65, FOSF, "grandes: rápidas, fortes")]
def rampa(fx, fy):
    s = []
    for i, (lim, cor, _) in enumerate(camadas):
        ini = lim
        topo = [(x, min(100, sum(max(0, min(x, 100) - l) for l, _, _ in camadas[:i+1]) * 100 / 170)) for x in xs]
        base = [(x, min(100, sum(max(0, min(x, 100) - l) for l, _, _ in camadas[:i]) * 100 / 170)) for x in xs]
        a = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in topo)
        b = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in reversed(base))
        s.append(f'<polygon points="{a} {b}" fill="{cor}" fill-opacity="0.85"/>')
    return "".join(s)
svg, rs = linhas(1664, 400, "Conforme a força pedida sobe, entram primeiro as unidades pequenas, depois as médias e só no alto as grandes",
    [], 0, 100, 0, 100, [(0, "força pedida: pouca"), (100, "máxima")], [], margem=(40, 20, 60, 30), extra=rampa,
    destaques=[{"x": 35}, {"x": 65}])
rs += [rot(1150, 270, "pequenas: lentas, resistentes", w=440, tam=26, cor=CLARO, peso=700),
       rot(720, 40, "médias", w=300, tam=26, cor=AZUL, peso=700),
       rot(1110, 40, "grandes: rápidas, fortes", w=320, tam=26, cor=FOSF, peso=700)]
S.append({"id": "tamanho", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "Henneman, 1965", "titulo": "O princípio do tamanho: não dá para furar a fila",
          "fonte": "Esquema do recrutamento ordenado · Henneman, Somjen e Carpenter, Journal of Neurophysiology 1965"})

# 8. três portas
p = [svg_abre(1664, 420, "Três portas levam às unidades de limiar alto: carga alta, velocidade alta e perto da falha; a série confortável para longe delas"),
     "<defs>" + seta_marker("p1", FOSF) + seta_marker("p2", MUDO) + "</defs>",
     f'<rect x="1204" y="80" width="460" height="260" rx="20" fill="{FOSF}"/>']
for i, nome in enumerate(["Carga alta", "Velocidade alta", "Perto da falha"]):
    y = 20 + i * 130
    p.append(caixa(440, y, 420, 100, FOSF, FOSF_T))
    p.append(f'<path d="M864 {y+50} C1000 {y+50} 1060 210 1194 210" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#p1)"/>')
p.append(caixa(0, 150, 340, 120, MUDO, CARTAO, 3))
p.append(f'<path d="M344 210 L420 210" stroke="{MUDO}" stroke-width="5" stroke-dasharray="10 8"/>')
p.append(f'<line x1="395" y1="180" x2="425" y2="240" stroke="{FOSF}" stroke-width="6"/><line x1="425" y1="180" x2="395" y2="240" stroke="{FOSF}" stroke-width="6"/></svg>')
rs = [rot(440, 46, "Carga alta", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(440, 176, "Velocidade alta", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(440, 306, "Perto da falha", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(1204, 150, "Unidades de<br>limiar alto", w=460, tam=38, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(1204, 270, "potência, prevenção de queda", w=460, tam=24, cor=CLARO, alinha="center"),
      rot(0, 166, "15 repetições confortáveis, devagar, longe do limite", w=340, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "portas", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A consequência prática", "titulo": "Não existe treinar fibra rápida sem esforço alto",
          "destaque": "A série confortável não é inútil. Ela só não chega lá.", "destaque_cor": "verm"})

# 9. recrutamento x frequência
def painel(x0, lim, titulo, p, rs):
    w, h, y0 = 760, 260, 60
    p.append(f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<rect x="{x0}" y="{y0}" width="{w*lim/100:.0f}" height="{h}" fill="{AZUL}" fill-opacity="0.18"/>')
    p.append(f'<rect x="{x0 + w*lim/100:.0f}" y="{y0}" width="{w*(1-lim/100):.0f}" height="{h}" fill="{FOSF}" fill-opacity="0.18"/>')
    p.append(f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0}" stroke="{TINTA}" stroke-width="5"/>')
    rs += [rot(x0, 0, titulo, w=w, tam=30, cor=TINTA, peso=700),
           rot(x0 + 10, y0 + 10, "recruta", w=w * lim / 100 - 20, tam=24, cor=AZUL, peso=700),
           rot(x0 + w * lim / 100 + 10, y0 + h - 44, "acelera o disparo" if lim < 60 else "acelera", w=w * (1 - lim / 100) - 20, tam=24, cor=FOSF, peso=700),
           rot(x0, y0 + h + 10, "força pedida →", w=w, tam=24, cor=MUDO, alinha="right")]
p, rs = [svg_abre(1664, 360, "No músculo pequeno o recrutamento termina cedo e a força sobe pelo disparo mais rápido; no grande o recrutamento continua até intensidades altas")], []
painel(0, 40, "Músculo pequeno", p, rs)
painel(904, 80, "Músculo grande", p, rs)
p.append("</svg>")
S.append({"id": "disparo", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A divisão de trabalho", "titulo": "Recrutar ou disparar mais rápido",
          "destaque": "“Tenho força mas não tenho explosão” quase sempre é frequência de disparo e velocidade de recrutamento. Não é tamanho de músculo.",
          "fonte": "Esquema, sem valores medidos"})

# 10. o contínuo
p = [svg_abre(1664, 340, "Um contínuo de tipos de fibra: tipo I, híbrida I e IIa, IIa, híbrida IIa e IIx, IIx")]
seg = [("I", OXID), ("I/IIa", None), ("IIa", AZUL), ("IIa/IIx", None), ("IIx", FOSF)]
w = 1664 / 5
for i, (nome, cor) in enumerate(seg):
    x = i * w
    if cor:
        p.append(f'<rect x="{x+4:.0f}" y="40" width="{w-8:.0f}" height="120" rx="12" fill="{cor}"/>')
    else:
        c1, c2 = seg[i - 1][1], seg[i + 1][1]
        p.append(f'<defs><linearGradient id="g{i}" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>')
        p.append(f'<rect x="{x+4:.0f}" y="40" width="{w-8:.0f}" height="120" rx="12" fill="url(#g{i})"/>')
p.append("</svg>")
rs = []
for i, (nome, cor) in enumerate(seg):
    rs.append(rot(i * w, 78, nome, w=w, tam=40, cor=CLARO, peso=700, alinha="center", serif=True))
rs += [rot(0, 190, "lenta, muita mitocôndria, resiste à fadiga", w=w * 1.2, tam=24, cor=TINTA, alinha="left"),
       rot(2 * w - 60, 190, "rápida e oxidativa: a mais adaptável", w=w + 120, tam=24, cor=TINTA, alinha="center"),
       rot(4 * w - 0.2 * w, 190, "a mais rápida, cansa logo", w=w * 1.2, tam=24, cor=TINTA, alinha="right"),
       rot(0, 270, "As híbridas são comuns. E a proporção varia muito de uma pessoa para outra.", w=1664, tam=30, cor=TINTA, peso=700, serif=True, alinha="center")]
S.append({"id": "continuo", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Tipos de fibra, sem a nitidez do manual", "titulo": "Um contínuo, não três gavetas"})

# 11. a IIx encolhe
p = [svg_abre(1664, 400, "Fração de miosina IIx no vasto lateral: 9,3% antes, 2,0% depois de três meses de treino pesado e 17,2% depois de três meses parado"),
     f'<line x1="200" y1="340" x2="1300" y2="340" stroke="{MUDO}" stroke-width="2"/>']
esc = 15
for i, (v, cor) in enumerate([(9.3, MUDO), (2.0, AZUL), (17.2, FOSF)]):
    x = 280 + i * 340
    p.append(f'<rect x="{x}" y="{340 - v*esc:.0f}" width="200" height="{v*esc:.0f}" rx="4" fill="{cor}"/>')
p.append(f'<line x1="200" y1="{340-9.3*esc:.0f}" x2="1300" y2="{340-9.3*esc:.0f}" stroke="{TINTA}" stroke-width="2" stroke-dasharray="8 8"/></svg>')
rs = []
for i, (v, nome) in enumerate([(9.3, "antes"), (2.0, "3 meses de treino pesado"), (17.2, "3 meses parado")]):
    x = 280 + i * 340
    rs += [rot(x, 340 - v * esc - 48, f"{v:.1f}%".replace(".", ","), w=200, tam=34, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(x - 60, 352, nome, w=320, tam=24, cor=TINTA, peso=600, alinha="center")]
rs += [rot(1340, 60, "Passou do ponto de partida.", w=324, tam=30, cor=FOSF, peso=700),
       rot(1340, 160, "A fibra mais rápida é, em boa medida, a do músculo que não recebe demanda.", w=324, tam=24)]
S.append({"id": "iix", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A correção mais contraintuitiva", "titulo": "A IIx encolhe com treino e volta a mais quando para",
          "fonte": "Andersen e Aagaard, Muscle & Nerve 2000 · homens sedentários, vasto lateral"})

# 12. converter fibras
S.append({"id": "converter", "tipo": "frase", "fundo": "tinta", "eyebrow": "A quarta correção",
          "frase": "“Vou converter minhas fibras” precisa ser aposentada.",
          "apoio": "A mudança bem demonstrada acontece dentro do espectro rápido. Entre lenta e rápida, os dados não convergem. O que o treino muda de forma confiável é o tamanho e a qualidade das fibras, e o comando que as usa."})

# 13. hipertrofia
p = [svg_abre(1664, 420, "A fibra sob tensão mecânica: sensores na membrana disparam a construção de proteína; células satélite se fundem e doam núcleos; o saldo de proteína fica positivo por até 48 horas depois da sessão"),
     "<defs>" + seta_marker("h1", TINTA) + "</defs>",
     f'<rect x="0" y="120" width="760" height="160" rx="80" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>',
     f'<path d="M-2 200 L60 200 M700 200 L762 200" stroke="{TINTA}" stroke-width="8"/>']
for k in range(5):
    p.append(f'<ellipse cx="{160 + k*110}" cy="200" rx="26" ry="16" fill="{FOSF}" opacity="0.7"/>')
for k, x in enumerate([230, 520]):
    p.append(f'<circle cx="{x}" cy="{70}" r="22" fill="{OXID}"/><path d="M{x} 94 L{x} 118" stroke="{OXID}" stroke-width="4" marker-end="url(#h1)"/>')
fx0, fy0, fw, fh = 900, 60, 760, 280
curva = [(t, 0 if t < 0 else 100 * (t / 12) * math.exp(1 - t / 12)) for t in range(-6, 61)]
pts = " ".join(f"{fx0 + (t+6)/66*fw:.1f},{fy0 + fh - max(v,0)/110*fh:.1f}" for t, v in curva)
p += [f'<line x1="{fx0}" y1="{fy0+fh}" x2="{fx0+fw}" y2="{fy0+fh}" stroke="{MUDO}" stroke-width="2"/>',
      f'<polyline points="{pts}" fill="none" stroke="{OXID}" stroke-width="6"/>', "</svg>"]
rs = [rot(0, 300, "tensão mecânica → construção de proteína", w=760, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(270, 20, "células satélite doam núcleos", w=420, tam=24, cor=OXID, peso=700),
      rot(fx0, 0, "Saldo de proteína depois da sessão", w=fw, tam=28, cor=TINTA, peso=700),
      rot(fx0, fy0 + fh + 10, "sessão · 24 h · 48 h", w=fw, tam=24, cor=MUDO, alinha="right"),
      rot(fx0 + 430, 230, "positivo por até 48 h", w=400, tam=26, cor=OXID, peso=700)]
S.append({"id": "hipertrofia", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Depois das primeiras semanas", "titulo": "A hipertrofia assume o protagonismo",
          "fonte": "Esquema · Phillips e colaboradores, American Journal of Physiology 1997 · destreinados"})

# 14. duas correções
S.append({"id": "correcoes", "tipo": "duas", "eyebrow": "Duas correções de academia", "titulo": "Dor não mede estímulo. Sem recurso, não há construção.",
          "esq": {"t": "Dano não é requisito", "cor": "ambar",
                  "itens": ["A dor de um a dois dias é microlesão e inflamação", "Dá para crescer com pouca dor", "Dá para doer muito e não crescer nada"]},
          "dir": {"t": "Hipertrofia exige matéria-prima", "cor": "verm",
                  "itens": ["Construir proteína pede aminoácido e energia", "Em déficit importante, o corpo não constrói", "Treinar pesado e comer pouco gasta o estímulo"]},
          "destaque": "Estímulo sem recurso não gera adaptação. Gera custo.", "destaque_cor": "verm"})

# 15. cada tecido no seu relógio
p = [svg_abre(1664, 400, "Quatro linhas do tempo: o nervo adapta em dias a semanas, o músculo em semanas a meses, tendão e osso em meses; uma faixa marca a janela em que a força já subiu e a estrutura ainda não")]
def tx(sem):
    return 300 + math.log10(1 + sem * 3) / math.log10(1 + 40 * 3) * 1350
p.append(f'<rect x="{tx(1):.0f}" y="0" width="{tx(10)-tx(1):.0f}" height="330" fill="{FOSF_T}"/>')
rs = []
for i, (nome, ini, fim, cor) in enumerate([("Nervo", 0.2, 3, AZUL), ("Músculo", 2, 16, FOSF), ("Tendão", 8, 40, GLIC), ("Osso", 10, 40, MUDO)]):
    y = 20 + i * 76
    p.append(f'<rect x="{tx(0):.0f}" y="{y}" width="{tx(40)-tx(0):.0f}" height="50" rx="8" fill="{PAUSA}" fill-opacity="0.35"/>')
    p.append(f'<rect x="{tx(ini):.0f}" y="{y}" width="{tx(fim)-tx(ini):.0f}" height="50" rx="8" fill="{cor}" fill-opacity="0.9"/>')
    rs.append(rot(0, y + 8, nome, w=280, tam=30, cor=TINTA, peso=700, alinha="right"))
p.append(f'<line x1="300" y1="330" x2="1650" y2="330" stroke="{MUDO}" stroke-width="2"/></svg>')
for s_, t in [(0.3, "dias"), (4, "1 mês"), (16, "4 meses"), (40, "9 meses")]:
    rs.append(rot(tx(s_) - 80, 340, t, w=160, tam=24, cor=MUDO, alinha="center"))
rs.append(rot(tx(1.2), 0 + 330 - 40, "força pronta, estrutura atrasada", w=520, tam=24, cor=FOSF, peso=700))
S.append({"id": "relogios", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A aula de fisiologia vira prevenção de lesão", "titulo": "Cada tecido no seu relógio",
          "destaque": "É a janela da lesão do iniciante empolgado e da recidiva no retorno: consegue fazer antes de o tecido aguentar.",
          "destaque_cor": "verm", "fonte": "Esquema de ordem temporal, escala logarítmica"})

# 16. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Três coisas que ficam",
          "regras": ["Os primeiros ganhos de força são do nervo, e são específicos", "Fibra rápida só com carga alta, velocidade alta ou perto da falha",
                     "Progressão gradual é respeito ao tecido mais lento: a lentidão do tendão é agenda"],
          "cards": [{"t": "Preparador e educador físico", "x": "Prescrevem o treino de força."},
                    {"t": "Fisioterapia", "x": "Progride carga em tecido lesionado."}],
          "quem": "O osso gosta de impacto e de carga. Nadador e ciclista não recebem isso do próprio esporte."})

spec = {"arquivo": "aulas/MOD02/02-07-fisiologia-neuromuscular-unidade-motora-e-fibras.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Trinta e cinco dias", "subtitulo": "Fisiologia neuromuscular, unidade motora e fibras",
        "nota_capa": "Entra pelo número.",
        "secoes": {"nervo": ["A força que vem do nervo.", "capa"],
                   "unidade": ["A unidade motora e o princípio do tamanho.", "unidade"],
                   "fibras": ["Tipos de fibra e o que o treino muda.", "continuo"],
                   "estrutura": ["Hipertrofia e o relógio de cada tecido.", "hipertrofia"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-07.json"), "w"), ensure_ascii=False, indent=1)
print("02-07.json:", len(S), "slides")
