"""Spec do deck 2.11. Gera 02-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def poli(pts, fx, fy, cor, esp=6, tracejado=False):
    d = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in pts)
    return (f'<polyline points="{d}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linecap="round" stroke-linejoin="round"'
            + (' stroke-dasharray="14 12"' if tracejado else "") + "/>")

# 1. a curva clássica
def sc(t):
    if t < 0: return 0
    return -35 * math.exp(-((t - 0.8) / 0.5) ** 2) + 18 * math.exp(-((t - 4.5) / 1.8) ** 2)
pts = [(t / 10, sc(t / 10)) for t in range(-10, 141)]
svg, rs = linhas(1664, 400, "A curva clássica: o desempenho cai depois do treino, volta à linha de base, sobe acima dela e depois cai de volta",
    [{"nome": "", "cor": AZUL, "pts": pts}], -1, 14, -45, 30, [(0, "treino"), (14, "dias depois")], [], margem=(40, 20, 60, 30),
    extra=lambda fx, fy: f'<line x1="{fx(-1):.0f}" y1="{fy(0):.0f}" x2="{fx(14):.0f}" y2="{fy(0):.0f}" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 8"/>')
rs += [rot(270, 290, "1. fadiga", w=260, tam=30, cor=FOSF, peso=700),
       rot(390, 170, "2. recuperação", w=300, tam=30, cor=TINTA, peso=700),
       rot(560, 14, "3. supercompensação", w=400, tam=30, cor=OXID, peso=700),
       rot(900, 170, "4. sem novo estímulo, volta", w=440, tam=30, cor=TINTA, peso=700),
       rot(1300, 100, "linha de base", w=300, tam=26, cor=MUDO, alinha="right")]
S.append({"id": "curva", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "O desenho que todo mundo já viu", "titulo": "Supercompensação: um mapa ruim",
          "destaque": "Selye descrevia uma resposta biológica ao dano. Alguém transformou isso num calendário de treino.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

# 2. polimento
p = [svg_abre(1664, 380, "Nas duas semanas antes da prova o volume cai entre 40 e 60 por cento, a intensidade se mantém e o desempenho sobe"),
     f'<line x1="0" y1="300" x2="1100" y2="300" stroke="{MUDO}" stroke-width="2"/>']
vols = [1, 1, 1, 1, 0.7, 0.5]
for i, v in enumerate(vols):
    cor = GLIC if i >= 4 else PAUSA
    p.append(f'<rect x="{20 + i*180}" y="{300 - 250*v:.0f}" width="140" height="{250*v:.0f}" rx="4" fill="{cor}"/>')
p.append(f'<rect x="{20 + 4*180 - 20}" y="10" width="{2*180}" height="330" rx="12" fill="none" stroke="{GLIC}" stroke-width="4" stroke-dasharray="12 10"/>')
for j, (t, s_, cor) in enumerate([("Volume", "cai 40 a 60%", GLIC), ("Intensidade", "mantida", TINTA), ("Frequência", "mantida", TINTA), ("Desempenho", "sobe", OXID)]):
    p.append(f'<rect x="1160" y="{10 + j*92}" width="504" height="76" rx="12" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(20 + i * 180, 312, f"sem {i+1}", w=140, tam=24, cor=MUDO, alinha="center") for i in range(6)]
rs.append(rot(20 + 4 * 180 - 20, 346, "as duas semanas finais", w=360, tam=24, cor=GLIC, peso=700, alinha="center"))
for j, (t, s_, cor) in enumerate([("Volume", "cai 40 a 60%", GLIC), ("Intensidade", "mantida", TINTA), ("Frequência", "mantida", TINTA), ("Desempenho", "sobe", OXID)]):
    rs += [rot(1184, 30 + j * 92, t, w=220, tam=28, cor=TINTA, peso=700), rot(1400, 30 + j * 92, s_, w=250, tam=28, cor=cor, peso=700, alinha="right")]
S.append({"id": "polimento", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A falha que derruba o modelo", "titulo": "Tira treino, e o desempenho sobe",
          "destaque": "Se o treino fosse uma linha só, tirar treino seria tirar linha. A curva de três fases não explica o polimento.",
          "destaque_cor": "ambar", "fonte": "Bosquet e colaboradores, Medicine & Science in Sports & Exercise 2007 · 27 estudos · barras ilustrativas"})

# 3. duas curvas depois de uma sessão
dias = [d / 2 for d in range(0, 101)]
apt = [(d, 1.0 * math.exp(-d / 40)) for d in dias]
fad = [(d, 2.0 * math.exp(-d / 7)) for d in dias]
des = [(d, a - f) for (d, a), (_, f) in zip(apt, fad)]
svg, rs = linhas(1664, 420, "Depois de uma sessão, a aptidão sobe pouco e some devagar, a fadiga sobe muito e some rápido; o desempenho é a diferença entre as duas: negativo nos primeiros dias, positivo depois",
    [{"nome": "", "cor": OXID, "pts": apt}, {"nome": "", "cor": FOSF, "pts": fad}, {"nome": "", "cor": TINTA, "pts": des, "esp": 10}],
    0, 50, -1.1, 2.1, [(0, "sessão"), (7, "1 semana"), (21, "3 semanas"), (50, "7 semanas")], [], margem=(40, 20, 60, 40),
    extra=lambda fx, fy: f'<line x1="{fx(0):.0f}" y1="{fy(0):.0f}" x2="{fx(50):.0f}" y2="{fy(0):.0f}" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 8"/>')
rs += [rot(760, 120, "aptidão: pequena e longa", w=420, tam=28, cor=OXID, peso=700),
       rot(200, 20, "fadiga: grande e curta", w=400, tam=28, cor=FOSF, peso=700),
       rot(400, 262, "desempenho: a diferença", w=420, tam=28, cor=TINTA, peso=700)]
S.append({"id": "duas", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "Banister: dois efeitos, direções opostas", "titulo": "Você nunca vê aptidão. Vê o saldo",
          "destaque": "Todo treino te dá uma moeda e te cobra uma dívida. A moeda fica no bolso por semanas. A dívida vence em dias.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos · Calvert, Banister e colaboradores, IEEE Transactions 1976"})

# 4. o polimento explicado
N = 70
carga = [1.0 if d < 56 else 0.45 for d in range(N)]
A, F, P = [], [], []
a = f = 0.0
for d in range(N):
    a = a * math.exp(-1 / 40) + carga[d]
    f = f * math.exp(-1 / 7) + 2.0 * carga[d]
    A.append((d, a)); F.append((d, f)); P.append((d, a - f))
def janela(fx, fy):
    return f'<rect x="{fx(56):.0f}" y="{fy(34):.0f}" width="{fx(69)-fx(56):.0f}" height="{fy(-2)-fy(34):.0f}" fill="{GLIC_T}"/>'
svg, rs = linhas(1664, 420, "Oito semanas de treino e depois duas de polimento: a fadiga desaba, a aptidão quase não se move, e o desempenho sobe",
    [{"nome": "", "cor": OXID, "pts": A}, {"nome": "", "cor": FOSF, "pts": F}, {"nome": "", "cor": TINTA, "pts": P, "esp": 10}],
    0, 69, -2, 34, [(0, "semana 0"), (28, "4"), (56, "8"), (69, "10")], [], margem=(40, 20, 60, 330), extra=janela)
rs += [rot(1350, 20, "aptidão", w=300, tam=28, cor=OXID, peso=700),
       rot(1350, 190, "fadiga", w=300, tam=28, cor=FOSF, peso=700),
       rot(1350, 250, "desempenho", w=300, tam=28, cor=TINTA, peso=700),
       rot(1030, 330, "polimento", w=300, tam=26, cor=GLIC, peso=700, alinha="center")]
S.append({"id": "explica", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "O que as duas curvas explicam", "titulo": "O cobrador sai da porta",
          "destaque": "Parado por doença e voltou melhor: descarregou fadiga. Férias: o VO₂máx cai um pouco, muito pelo plasma, e volta rápido.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos · Mujika e Padilla, Sports Medicine 2000"})

# 5. mal condicionado
W, H = 1664, 400
p = [svg_abre(W, H, "Duas combinações opostas: aptidão e fadiga altas, ou aptidão e fadiga baixas, produzem a mesma linha de desempenho")]
perf = lambda d: 0.9 * math.exp(-d / 40) - 1.8 * math.exp(-d / 7)
rs = []
for k, (x0, esc_a, tit, cor_t) in enumerate([(0, 1.0, "Versão A: muito ganho, muito custo", TINTA), (860, 0.55, "Versão B: pouco ganho, pouco custo", TINTA)]):
    pw, ph, top = 780, 300, 60
    fx = lambda d, x0=x0: x0 + d / 50 * pw
    fy = lambda v: top + ph - (v + 1.2) / 3.6 * ph
    ap = [(d / 2, esc_a * 2.0 * math.exp(-d / 2 / 40)) for d in range(101)]
    pf = [(d / 2, perf(d / 2)) for d in range(101)]
    fa = [(d, a_ - p_) for (d, a_), (_, p_) in zip(ap, pf)]
    p.append(f'<line x1="{x0}" y1="{fy(0):.0f}" x2="{x0+pw}" y2="{fy(0):.0f}" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 8"/>')
    p += [poli(ap, fx, fy, OXID), poli(fa, fx, fy, FOSF), poli(pf, fx, fy, TINTA, esp=10)]
    rs.append(rot(x0, 0, tit, w=780, tam=28, cor=cor_t, peso=700))
p.append("</svg>")
rs += [rot(0, 370, "verde aptidão · vermelho fadiga · preto grosso desempenho, idêntico nas duas", w=1664, tam=26, cor=MUDO)]
S.append({"id": "calculadora", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde o modelo quebra", "titulo": "Ótima metáfora, péssima calculadora",
          "destaque": "Não precisa de equação: dez dias fáceis e uma reavaliação. Melhorou, era fadiga. E avise que os três primeiros dias vão ser ruins.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Hellard e colaboradores, Journal of Sports Sciences 2006 · 9 nadadores de elite, uma temporada"})

# 6. distribuição
dias_s = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
A_ = [5, 8, 8, 5, 8, 8, 0]
B_ = [2, 10, 2, 10, 2, 12, 4]
p = [svg_abre(1664, 440, "Duas semanas com a mesma carga total. Na primeira, dias duros encostados e dias leves acima do limite do leve. Na segunda, duro depois de fácil, e o fácil abaixo do limite")]
rs = []
for j, (serie, tit, cor_t) in enumerate([(A_, "Semana A: encostada e monótona", FOSF), (B_, "Semana B: duro depois de fácil", OXID)]):
    x0 = j * 860
    base, esc = 360, 24
    p.append(f'<line x1="{x0}" y1="{base}" x2="{x0+800}" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="{x0}" y1="{base - 4*esc}" x2="{x0+800}" y2="{base - 4*esc}" stroke="{OXID}" stroke-width="3" stroke-dasharray="10 8"/>')
    for i, v in enumerate(serie):
        cor = FOSF if v >= 8 else (GLIC if v > 4 else OXID)
        if v:
            p.append(f'<rect x="{x0 + 20 + i*112}" y="{base - v*esc}" width="80" height="{v*esc}" rx="4" fill="{cor}"/>')
        rs.append(rot(x0 + 10 + i * 112, base + 8, dias_s[i], w=100, tam=24, cor=MUDO, alinha="center"))
    rs.append(rot(x0, 0, tit, w=800, tam=28, cor=cor_t, peso=700))
rs += [rot(560, 236, "teto do leve", w=240, tam=24, cor=OXID, peso=700, alinha="right"),
       rot(0, 404, "vermelho duro · âmbar “leve” que não é leve · verde leve de verdade · mesma carga total nas duas", w=1664, tam=26, cor=MUDO)]
S.append({"id": "distribuicao", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O erro que sobra no atleta real", "titulo": "Mesmo total, resultado diferente",
          "destaque": "A primeira pergunta não é “quanto você treina?”. É “como está distribuído?”.",
          "destaque_cor": "verm", "fonte": "Barras ilustrativas · monotonia e tensão: Foster, Medicine & Science in Sports & Exercise 1998"})

# 7. pirâmide
p = [svg_abre(1664, 440, "Pirâmide da recuperação: na base larga, sono, comida e distribuição da carga; no topo estreito, gelo, compressão e pistola de massagem")]
p.append(f'<polygon points="332,420 1332,420 1132,210 532,210" fill="{OXID}"/>')
p.append(f'<polygon points="542,200 1122,200 972,40 692,40" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(432, 280, "Sono · comida · distribuição da carga", w=800, tam=36, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(632, 104, "gelo · compressão · pistola", w=400, tam=24, cor=TINTA, peso=600, alinha="center"),
      rot(1260, 300, "sustenta tudo", w=400, tam=28, cor=OXID, peso=700),
      rot(1160, 100, "ajuste fino", w=400, tam=28, cor=MUDO, peso=700),
      rot(0, 300, "a base", w=300, tam=28, cor=OXID, peso=700, alinha="right"),
      rot(0, 100, "o topo", w=520, tam=28, cor=MUDO, peso=700, alinha="right")]
S.append({"id": "piramide", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A base antes de qualquer técnica", "titulo": "Casa sem telhado não se arruma pela prateleira",
          "destaque": "Quem dorme cinco horas e come mal não tem problema de distribuição. Tem problema de base.",
          "destaque_cor": "petr"})

# 8. funciona para quê
p = [svg_abre(1664, 420, "Técnicas de recuperação reduzem dor e fadiga percebida, com a massagem à frente. Mas doze semanas de força com água fria depois de cada sessão: fibra rápida mais 17% e núcleos por fibra mais 26% só no grupo de recuperação ativa"),
     f'<line x1="760" y1="0" x2="760" y2="420" stroke="{GRADE}" stroke-width="3"/>']
tecn = ["massagem", "compressão", "imersão e contraste", "recuperação ativa", "crioterapia"]
for i, t_ in enumerate(tecn):
    y = 70 + i * 66
    p.append(f'<rect x="0" y="{y}" width="700" height="54" rx="10" fill="{OXID_T if i else OXID}" stroke="{OXID}" stroke-width="2"/>')
esc = 12
for i, (t_, va, vb) in enumerate([("área da fibra rápida", 17, 0), ("núcleos por fibra", 26, 0)]):
    y = 90 + i * 150
    p.append(f'<rect x="1120" y="{y}" width="{va*esc}" height="50" rx="4" fill="{OXID}"/>')
    p.append(f'<rect x="1120" y="{y+60}" width="6" height="50" rx="2" fill="{AZUL}"/>')
p.append(f'<line x1="1120" y1="70" x2="1120" y2="380" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(0, 0, "Reduzem dor e fadiga percebida", w=740, tam=28, cor=TINTA, peso=700)]
for i, t_ in enumerate(tecn):
    rs.append(rot(20, 80 + i * 66, t_ + (": o melhor resultado" if i == 0 else ""), w=660, tam=26, cor=CLARO if i == 0 else TINTA, peso=700 if i == 0 else 400))
rs += [rot(800, 0, "Força por 12 semanas: gelo ou recuperação ativa", w=864, tam=28, cor=TINTA, peso=700),
       rot(800, 100, "área da fibra rápida", w=300, tam=26, cor=TINTA, peso=600, alinha="right"),
       rot(800, 250, "núcleos por fibra", w=300, tam=26, cor=TINTA, peso=600, alinha="right"),
       rot(1120 + 17 * esc + 16, 96, "+17% ativo", w=260, tam=28, cor=OXID, peso=700),
       rot(1140, 156, "sem aumento com gelo", w=400, tam=26, cor=AZUL, peso=700),
       rot(1120 + 26 * esc + 16, 246, "+26% ativo", w=260, tam=28, cor=OXID, peso=700),
       rot(1140, 306, "sem aumento com gelo", w=400, tam=26, cor=AZUL, peso=700)]
S.append({"id": "paraque", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A indústria da recuperação", "titulo": "Funciona, para aquilo que foi medido",
          "destaque": "Dor e marcador não são adaptação. O estresse depois do treino é parte do sinal que faz o músculo crescer.",
          "destaque_cor": "verm", "fonte": "Dupuy e colaboradores, Frontiers in Physiology 2018 · 99 estudos · Roberts e colaboradores, Journal of Physiology 2015 · 21 homens · Piñero e colaboradores 2024"})

# 9. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Render em breve, ou adaptar?",
          "regras": ["Render em breve: gelo, compressão e massagem são ferramentas legítimas",
                     "Adaptar: nada de gelo de rotina depois da sessão de força"],
          "cards": [{"t": "Preparador e educador físico", "x": "Distribuem a carga na semana: duro depois de fácil, fácil de verdade."},
                    {"t": "Todo mundo", "x": "Defende a hierarquia: sono, comida e distribuição explicam a maior parte."}],
          "quem": "“A dor muscular não é o problema que a gente está resolvendo. É efeito colateral do que a gente está construindo.”"})

spec = {"arquivo": "aulas/MOD02/02-11-recuperacao-supercompensacao-e-treino-mal-distribuido.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Recuperação e distribuição da carga", "subtitulo": "Modelos de adaptação ao treino e seus limites",
        "nota_capa": "Entra pelo desenho que todo mundo já viu.",
        "secoes": {"erro": ["A curva de supercompensação e por que ela falha.", "capa"],
                   "modelo": ["As duas curvas, o que explicam e onde quebram.", "duas"],
                   "pratica": ["Distribuição, base e a indústria da recuperação.", "distribuicao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-11.json"), "w"), ensure_ascii=False, indent=1)
print("02-11.json:", len(S), "slides")
