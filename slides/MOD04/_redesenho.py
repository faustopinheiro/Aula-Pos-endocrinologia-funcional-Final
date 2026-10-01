"""Desenhos que substituem os slides de texto do Módulo 4 (cartões, colunas, listas, tabelas e números).
Cada função devolve o dicionário do slide, com o mesmo id do slide que substitui."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

TRACO = ' stroke-dasharray="10 8"'
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL, BORDA = "#FDFCF9", "#F7F6F2", "#DDD8CC"
CINZA = "#C9CFD4"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"
def slide(id_, h, p, rs, **k):
    p.append("</svg>")
    d = {"id": id_, "tipo": "diagrama", "h": h, "svg": "".join(p), "rotulos": rs}
    d.update(k)
    return d


# ---------------------------------------------------------------- 4.1

def equacao():
    """4.1: a equação da disponibilidade energética montada em blocos."""
    p = [svg_abre(1664, 400, "A equação em blocos: ingestão, menos o gasto do exercício, dá o que sobra para o corpo funcionar; o que sobra, dividido pela massa livre de gordura, dá a disponibilidade energética em quilocalorias por quilo por dia"), defs(TINTA)]
    blocos = [(0, "t:salad", "Ingestão", "o que entra", AZUL, AZUL_T),
              (420, "t:run", "Gasto do exercício", "o que o treino cobra", GLIC, GLIC_T),
              (840, "t:battery-4", "O que sobra", "para o corpo funcionar", OXID, OXID_T)]
    rs = []
    for x, ic, t, d, cor, fundo in blocos:
        p.append(caixa(x, 40, 340, 190, cor, fundo, esp=3, rx=18))
        p.append(icone(ic, x + 140, 60, 60, cor))
        rs += [rot(x, 132, t, w=340, tam=28, cor=cor, peso=700, alinha="center", serif=True),
               rot(x, 176, d, w=340, tam=22, cor=TINTA, alinha="center")]
    rs += [rot(340, 104, "−", w=80, tam=60, cor=TINTA, peso=700, alinha="center"),
           rot(760, 104, "=", w=80, tam=60, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="1240" y1="135" x2="1300" y2="135" stroke="{TINTA}" stroke-width="4"/>')
    rs.append(rot(1180, 104, "÷", w=180, tam=60, cor=TINTA, peso=700, alinha="center"))
    p.append(caixa(1324, 40, 340, 190, MUDO, PAPEL, esp=3, rx=18))
    p.append(icone("t:barbell", 1464, 60, 60, MUDO))
    rs += [rot(1324, 132, "Massa livre de gordura", w=340, tam=26, cor=TINTA, peso=700, alinha="center", serif=True, lh=1.1),
           rot(1324, 196, "em kg", w=340, tam=22, cor=MUDO, alinha="center")]
    p.append(caixa(432, 290, 800, 100, TINTA, TINTA, esp=0, rx=18))
    rs.append(rot(432, 318, "kcal por kg de massa livre de gordura por dia", w=800, tam=28, cor=PAPEL, peso=700, alinha="center"))
    p.append(seta(832, 236, 832, 282, TINTA, "m0", esp=4))
    return slide("equacao", 400, p, rs,
                 eyebrow="O número que o curso inteiro citou", titulo="O que sobra para o corpo funcionar",
                 destaque="Disponibilidade energética baixa não é comer pouco. É comer pouco para o que se gasta.",
                 destaque_cor="verm")


def conta_41():
    """4.1: três mil calorias que viram menos de trinta, em cascata."""
    p = [svg_abre(1664, 420, "Uma cascata: 3.100 quilocalorias ingeridas, menos 1.100 do exercício, sobram 2.000. Divididas por 69 quilos de massa livre de gordura, de um homem de 78 quilos com 12% de gordura, dão cerca de 29 quilocalorias por quilo, abaixo da linha de 30")]
    Y0, K = 380, 0.1
    barras = [(40, 3100, 0, "3.100 ingeridas", AZUL), (300, 1100, 2000, "− 1.100 do exercício", GLIC), (560, 2000, 0, "2.000 que sobram", OXID)]
    rs = []
    for x, v, base, t, cor in barras:
        p.append(f'<rect x="{x}" y="{Y0 - (base + v) * K:.0f}" width="200" height="{v * K:.0f}" rx="6" fill="{cor}"/>')
        rs.append(rot(x - 20, Y0 + 6, t, w=240, tam=22, cor=cor, peso=700, alinha="center"))
    p.append(f'<line x1="240" y1="{Y0 - 3100 * K:.0f}" x2="300" y2="{Y0 - 3100 * K:.0f}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    p.append(f'<line x1="500" y1="{Y0 - 2000 * K:.0f}" x2="560" y2="{Y0 - 2000 * K:.0f}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    p.append(f'<line x1="20" y1="{Y0}" x2="780" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(830, 150, "÷ 69 kg", w=220, tam=40, cor=TINTA, peso=700, serif=True))
    rs.append(rot(830, 206, "de massa livre de gordura: 78 kg com 12% de gordura", w=260, tam=20, cor=MUDO, lh=1.2))
    # régua
    X0, X1 = 1120, 1640
    X = lambda v: X0 + (v - 15) / 35 * (X1 - X0)
    p.append(f'<rect x="{X(15):.0f}" y="230" width="{X(30) - X(15):.0f}" height="40" fill="{FOSF_T}"/>')
    p.append(f'<rect x="{X(30):.0f}" y="230" width="{X(45) - X(30):.0f}" height="40" fill="{GLIC_T}"/>')
    p.append(f'<rect x="{X(45):.0f}" y="230" width="{X(50) - X(45):.0f}" height="40" fill="{OXID_T}"/>')
    p.append(f'<line x1="{X(30):.0f}" y1="210" x2="{X(30):.0f}" y2="290" stroke="{FOSF}" stroke-width="4"/>')
    p.append(f'<path d="M {X(29):.0f} 222 l -14 -26 l 28 0 z" fill="{FOSF}"/>')
    rs += [rot(X(29) - 100, 100, "≈ 29", w=200, tam=56, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(X(30) - 40, 294, "30", w=80, tam=22, cor=FOSF, peso=700, alinha="center"),
           rot(X0, 330, "kcal por kg de massa livre de gordura por dia", w=X1 - X0, tam=20, cor=MUDO, alinha="center")]
    return slide("conta", 420, p, rs,
                 eyebrow="Uma conta que desmonta a intuição", titulo="Três mil calorias, e abaixo de trinta",
                 destaque="Ninguém que come três mil calorias se vê como alguém que come pouco. É esse perfil que chega para discutir testosterona.",
                 destaque_cor="tinta")


def revisao():
    """4.1: de linha a faixa de risco nas mulheres; o que mexe primeiro nos homens."""
    import math
    p = [svg_abre(1664, 380, "À esquerda, mulheres: a chance de alteração menstrual sobe abaixo de 30, mas a curva não começa em zero acima de 30 e não chega a cem abaixo; há alteração dos dois lados. À direita, homens, seis voluntários, 15 contra 40 quilocalorias por quilo por quatro dias: a leptina caiu 53 a 56%, a insulina 34 a 38%, e T3, testosterona e IGF-1 ainda não se moveram")]
    p.append(caixa(0, 0, 800, 380, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 14, "Mulheres: uma faixa de risco", w=760, tam=26, cor=OXID, peso=700, serif=True)]
    X0, X1, Yb, Yt = 70, 760, 270, 80
    p.append(f'<line x1="{X0}" y1="{Yb}" x2="{X1}" y2="{Yb}" stroke="{MUDO}" stroke-width="2"/><line x1="{X0}" y1="{Yt}" x2="{X0}" y2="{Yb}" stroke="{MUDO}" stroke-width="2"/>')
    pts = [(v, 0.15 + 0.6 / (1 + math.exp((v - 28) / 3.5))) for v in range(15, 51)]
    d = "M" + " L".join(f"{X0 + (v - 15) / 35 * (X1 - X0):.0f} {Yb - r * (Yb - Yt):.0f}" for v, r in pts)
    p.append(f'<path d="{d}" fill="none" stroke="{OXID}" stroke-width="6"/>')
    x30 = X0 + 15 / 35 * (X1 - X0)
    p.append(f'<line x1="{x30:.0f}" y1="{Yt}" x2="{x30:.0f}" y2="{Yb}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    rs += [rot(x30 - 40, Yb + 6, "30", w=80, tam=20, cor=FOSF, peso=700, alinha="center"),
           rot(X0, Yb + 30, "disponibilidade energética", w=X1 - X0, tam=20, cor=MUDO, alinha="center"),
           rot(x30 + 16, 120, "acima de 30 também há alteração", w=330, tam=20, cor=TINTA, lh=1.2),
           rot(24, 334, "uma linha libera; um risco não libera", w=760, tam=22, cor=OXID, peso=700)]
    p.append(caixa(864, 0, 800, 380, GLIC, GLIC_T, esp=3, rx=16))
    rs += [rot(888, 14, "Homens: quatro dias a 15 contra 40", w=760, tam=26, cor=GLIC, peso=700, serif=True),
           rot(888, 52, "seis voluntários", w=760, tam=20, cor=MUDO)]
    Z = 1180
    p.append(f'<line x1="{Z}" y1="90" x2="{Z}" y2="360" stroke="{TINTA}" stroke-width="2"/>')
    itens = [("leptina", 53, 56, FOSF), ("insulina", 34, 38, FOSF), ("T3", 0, 0, MUDO), ("testosterona", 0, 0, MUDO), ("IGF-1", 0, 0, MUDO)]
    for k, (t, a, b, cor) in enumerate(itens):
        y = 94 + k * 54
        rs.append(rot(832, y + 8, t, w=150, tam=20, cor=TINTA, peso=600, alinha="right"))
        if b:
            p.append(f'<rect x="{Z - b * 3.4:.0f}" y="{y}" width="{b * 3.4:.0f}" height="40" rx="4" fill="{cor}" fill-opacity="0.35"/>')
            p.append(f'<rect x="{Z - a * 3.4:.0f}" y="{y}" width="{a * 3.4:.0f}" height="40" rx="4" fill="{cor}"/>')
            rs.append(rot(Z + 14, y + 6, f"−{a} a −{b}%", w=300, tam=22, cor=cor, peso=700))
        else:
            p.append(f'<circle cx="{Z}" cy="{y + 20}" r="9" fill="{MUDO}"/>')
            rs.append(rot(Z + 14, y + 6, "ainda parado", w=300, tam=22, cor=MUDO))
    return slide("revisao", 380, p, rs,
                 eyebrow="Vinte anos depois", titulo="De linha a faixa de risco",
                 destaque="Consenso do COI, 2023: um contínuo, do adaptável ao problemático. Quanto, por quanto tempo, e com que consequência?",
                 destaque_cor="tinta", fonte="Curva: esquema · Salamunes e colaboradores, Applied Physiology, Nutrition, and Metabolism 2024 · Koehler e colaboradores, Journal of Sports Sciences 2016")


def medida():
    """4.1: a mesma equação, com o erro pendurado em cada termo."""
    p = [svg_abre(1664, 420, "A equação de novo, ingestão menos gasto do exercício dividido pela massa livre de gordura, e embaixo de cada termo o seu erro: a ingestão é subestimada por esquecimento, porção mal estimada e o que se come em pé; o gasto do exercício é mal medido e quase ninguém desconta o repouso; a massa magra muda com o método; e a variação de um dia para o outro é grande"), defs(GLIC)]
    termos = [(0, "Ingestão", AZUL, "t:trending-down", "subestimada", "esquecimento, porção mal estimada, o que se come em pé"),
              (450, "Gasto do exercício", GLIC, "t:question-mark", "mal medido", "e quase ninguém desconta o que se gastaria em repouso"),
              (900, "Massa livre de gordura", MUDO, "t:arrows-exchange", "muda com o método", "o denominador também tem erro")]
    rs = []
    for x, t, cor, ic, e, d in termos:
        p.append(caixa(x, 0, 380, 90, cor, CARTAO, esp=3, rx=14))
        rs.append(rot(x, 26, t, w=380, tam=26, cor=cor, peso=700, alinha="center"))
        p.append(seta(x + 190, 96, x + 190, 140, GLIC, "m0", esp=3))
        p.append(caixa(x, 150, 380, 170, GLIC, GLIC_T, esp=2, rx=14))
        p.append(icone(ic, x + 20, 170, 44, GLIC))
        rs += [rot(x + 76, 176, e, w=290, tam=24, cor=GLIC, peso=700), rot(x + 20, 232, d, w=340, tam=21, cor=TINTA, lh=1.25)]
    rs += [rot(380, 26, "−", w=70, tam=40, cor=TINTA, peso=700, alinha="center"), rot(830, 26, "÷", w=70, tam=40, cor=TINTA, peso=700, alinha="center")]
    # variação diária
    p.append(caixa(1350, 0, 314, 320, GLIC, GLIC_T, esp=2, rx=14))
    rs.append(rot(1366, 14, "Variação diária grande", w=290, tam=24, cor=GLIC, peso=700, lh=1.15))
    import math
    pts = [(1380 + k * 36, 200 - 60 * math.sin(k * 1.7)) for k in range(8)]
    p.append(f'<path d="M' + " L".join(f"{x} {y:.0f}" for x, y in pts) + f'" fill="none" stroke="{GLIC}" stroke-width="4"/>')
    rs.append(rot(1366, 266, "um dia não representa a semana", w=290, tam=20, cor=TINTA, lh=1.2))
    p.append(caixa(0, 350, 1664, 70, OXID, OXID_T, esp=2, rx=14))
    rs.append(rot(0, 368, "o número não é diagnóstico: é ordem de grandeza", w=1664, tam=26, cor=OXID, peso=700, alinha="center"))
    return slide("medida", 420, p, rs,
                 eyebrow="Uma revisão de 2018", titulo="A equação é frágil",
                 destaque="E faz o paciente ver a própria conta.", destaque_cor="petr",
                 fonte="Burke e colaboradores, International Journal of Sport Nutrition and Exercise Metabolism 2018")


def alarme():
    """4.1: o alarme que apita todo mês, e o silêncio do lado masculino."""
    import math
    p = [svg_abre(1664, 420, "À esquerda, a mulher: o ciclo como um sinal vital que apita todo mês, desenhado como um anel de 28 dias com um sino; a alteração vai da fase lútea curta à amenorreia, e foi onde a literatura nasceu, porque era visível. À direita, o homem: um sino riscado, sem alarme equivalente; os sinais são desempenho, fadiga, libido, infecções e uma testosterona que cai com LH baixo")]
    p.append(caixa(0, 0, 800, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 14, "Mulher: um alarme que apita todo mês", w=760, tam=26, cor=OXID, peso=700, serif=True)]
    cx, cy, r = 190, 240, 120
    for k in range(28):
        a = -math.pi / 2 + k * 2 * math.pi / 28
        p.append(f'<circle cx="{cx + r * math.cos(a):.0f}" cy="{cy + r * math.sin(a):.0f}" r="10" fill="{OXID}"/>')
    p.append(icone("t:alarm", cx - 36, cy - 36, 72, OXID))
    itens = ["o ciclo, um sinal vital", "da fase lútea curta à amenorreia", "foi onde a literatura nasceu, porque era visível"]
    for k, t in enumerate(itens):
        rs.append(rot(350, 120 + k * 90, t, w=420, tam=23, cor=TINTA, lh=1.25))
    p.append(caixa(864, 0, 800, 420, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(888, 14, "Homem: nenhum alarme equivalente", w=760, tam=26, cor=GLIC, peso=700, serif=True))
    p.append(f'<circle cx="1054" cy="240" r="110" fill="{CARTAO}" stroke="{CINZA}" stroke-width="4"/>')
    p.append(icone("t:volume-off", 1018, 204, 72, MUDO))
    sinais = [("t:trending-down", "desempenho"), ("t:battery-1", "fadiga"), ("t:heart-broken", "libido"), ("t:mood-sick", "infecções"), ("t:droplet", "testosterona baixa, LH baixo")]
    for k, (ic, t) in enumerate(sinais):
        y = 90 + k * 64
        p.append(icone(ic, 1210, y, 40, GLIC))
        rs.append(rot(1262, y + 6, t, w=390, tam=22, cor=TINTA))
    return slide("alarme", 420, p, rs,
                 eyebrow="Uma revisão de 2021", titulo="Mesma fisiologia, alarmes diferentes",
                 destaque="Homem jovem e ativo com testosterona baixa: calcule a disponibilidade antes de discutir reposição. E balança parada pode ser economia.",
                 destaque_cor="verm", fonte="Areta, Taylor e Koehler, European Journal of Applied Physiology 2021 · consenso do COI 2023")


def portas_41():
    """4.1: cinco portas para a mesma conta, só a primeira acesa."""
    p = [svg_abre(1664, 420, "Cinco portas lado a lado por onde a conta estoura. A primeira, acesa, é a única que costuma ser procurada: restrição por desempenho ou estética. As outras quatro: emagrecer com orientação legítima, com dieta e treino somados, e com remédio comer vira tarefa; o gasto subiu e o prato não; insuficiente sem intenção, por tempo, dinheiro, logística ou crescimento; e desorganização, quando o total até fecha mas a comida nunca está na hora certa")]
    portas = [("Restrição por desempenho ou estética", "categoria de peso, esporte estético", FOSF, True),
              ("Emagrecer com orientação legítima", "com remédio, comer vira tarefa", GLIC, False),
              ("O gasto subiu e o prato não", "ninguém restringiu nada", GLIC, False),
              ("Insuficiente sem intenção", "tempo, dinheiro, logística, crescimento", GLIC, False),
              ("Desorganização", "o total fecha; a hora, nunca", GLIC, False)]
    rs = []
    W = 300
    for k, (t, d, cor, acesa) in enumerate(portas):
        x = k * (W + 41)
        p.append(f'<rect x="{x + 50}" y="0" width="200" height="230" rx="8" fill="{FOSF_T if acesa else PAPEL}" stroke="{cor}" stroke-width="{5 if acesa else 3}"/>')
        p.append(f'<circle cx="{x + 226}" cy="125" r="9" fill="{cor}"/>')
        rs.append(rot(x + 50, 70, str(k + 1), w=200, tam=64, cor=cor, peso=700, alinha="center", serif=True))
        rs += [rot(x, 246, t, w=W, tam=23, cor=cor if acesa else TINTA, peso=700, alinha="center", lh=1.2),
               rot(x, 330, d, w=W, tam=20, cor=MUDO, alinha="center", lh=1.2)]
    rs.append(rot(0, 390, "só a primeira é procurada", w=W, tam=20, cor=FOSF, peso=700, alinha="center"))
    return slide("portas", 420, p, rs,
                 eyebrow="Por onde a conta estoura", titulo="Cinco portas, e só uma é procurada",
                 destaque="Identificar a porta é metade da conduta.", destaque_cor="tinta")


def controversia():
    """4.1: a zona de acordo no centro, e o que está em disputa em volta."""
    p = [svg_abre(1664, 420, "No centro, a zona de acordo: os efeitos endócrinos e metabólicos são reais; existe na prática e é modificável. Num anel tracejado em volta, o que está em disputa: o rótulo de síndrome e o diagnóstico por lista de sintomas. À esquerda, a crítica: a causa é quase impossível de medir fora do laboratório; sintomas genéricos com causas múltiplas, a carga alostática")]
    cx, cy = 1140, 210
    p.append(f'<circle cx="{cx}" cy="{cy}" r="205" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3" stroke-dasharray="14 10"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="130" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    rs = [rot(cx - 120, cy - 96, "A zona de acordo", w=240, tam=24, cor=OXID, peso=700, alinha="center", serif=True),
          rot(cx - 120, cy - 50, "efeitos endócrinos e metabólicos reais", w=240, tam=20, cor=TINTA, alinha="center", lh=1.2),
          rot(cx - 120, cy + 20, "existe na prática e é modificável", w=240, tam=20, cor=TINTA, alinha="center", lh=1.2),
          rot(cx + 150, 20, "em disputa:", w=200, tam=20, cor=GLIC, peso=700),
          rot(cx + 210, 56, "o rótulo de síndrome", w=230, tam=20, cor=GLIC, peso=700, lh=1.2),
          rot(cx + 210, 330, "o diagnóstico por lista", w=230, tam=20, cor=GLIC, peso=700, lh=1.2)]
    p.append(caixa(0, 0, 640, 420, GLIC, CARTAO, esp=3, rx=16))
    rs.append(rot(24, 16, "A crítica", w=600, tam=28, cor=GLIC, peso=700, serif=True))
    crit = [("t:zoom-question", "a causa é quase impossível de medir fora do laboratório"),
            ("t:list-check", "o diagnóstico vira lista de sintomas"),
            ("t:puzzle", "sintomas genéricos, causas múltiplas: carga alostática")]
    for k, (ic, t) in enumerate(crit):
        y = 90 + k * 106
        p.append(icone(ic, 24, y, 48, GLIC))
        rs.append(rot(92, y, t, w=520, tam=23, cor=TINTA, lh=1.25))
    return slide("controversia", 420, p, rs,
                 eyebrow="Uma crítica de 2024", titulo="A síndrome existe?",
                 destaque="Contribuinte principal e modificável, não explicação única. Encontrou? Corrija, e não pare a investigação.",
                 destaque_cor="tinta", fonte="Jeukendrup, Areta e colaboradores, Sports Medicine 2024; resposta dos autores do consenso e réplica em 2025")

# ---------------------------------------------------------------- 4.2

def regua_ea(p, rs, X0, X1, y, vmin=15, vmax=50, rotulo=True):
    """Régua de disponibilidade energética com as três faixas; devolve a função de posição."""
    X = lambda v: X0 + (v - vmin) / (vmax - vmin) * (X1 - X0)
    p.append(f'<rect x="{X(vmin):.0f}" y="{y}" width="{X(30) - X(vmin):.0f}" height="36" fill="{FOSF_T}"/>')
    p.append(f'<rect x="{X(30):.0f}" y="{y}" width="{X(45) - X(30):.0f}" height="36" fill="{GLIC_T}"/>')
    p.append(f'<rect x="{X(45):.0f}" y="{y}" width="{X(vmax) - X(45):.0f}" height="36" fill="{OXID_T}"/>')
    for v in (30, 45):
        p.append(f'<line x1="{X(v):.0f}" y1="{y - 6}" x2="{X(v):.0f}" y2="{y + 42}" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(X(v) - 40, y + 46, str(v), w=80, tam=20, cor=MUDO, alinha="center"))
    if rotulo:
        rs.append(rot(X0, y + 76, "kcal por kg de massa livre de gordura por dia", w=X1 - X0, tam=20, cor=MUDO, alinha="center"))
    return X


def conta_42():
    """4.2: a conta da triatleta montada passo a passo até cair na zona sem alarme."""
    p = [svg_abre(1664, 400, "A conta de uma triatleta amadora em blocos: 2.400 quilocalorias por dia no registro de sete dias, menos 700 do exercício, 90 minutos seis dias por semana, dividido por 45 quilos de massa livre de gordura, de 58 quilos com 22% de gordura. O resultado, cerca de 38, cai na faixa entre 30 e 45")]
    blocos = [(0, "2.400", "kcal por dia no registro de sete dias", AZUL), (440, "− 700", "kcal do exercício: 90 min, seis dias por semana", GLIC),
              (880, "÷ 45 kg", "de massa livre de gordura: 58 kg com 22% de gordura", MUDO)]
    rs = []
    for x, n, d, cor in blocos:
        p.append(caixa(x, 0, 400, 180, cor, CARTAO, esp=3, rx=16))
        rs += [rot(x, 20, n, w=400, tam=52, cor=cor, peso=700, alinha="center", serif=True),
               rot(x + 24, 100, d, w=352, tam=21, cor=TINTA, alinha="center", lh=1.25)]
    p.append(caixa(1320, 0, 344, 180, GLIC, GLIC, esp=0, rx=16))
    rs += [rot(1320, 20, "≈ 38", w=344, tam=60, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1320, 110, "resultado", w=344, tam=22, cor=PAPEL, alinha="center")]
    X = regua_ea(p, rs, 200, 1464, 260)
    p.append(f'<path d="M {X(38):.0f} 254 l -16 -30 l 32 0 z" fill="{GLIC}"/>')
    rs.append(rot(X(38) - 60, 196, "38", w=120, tam=26, cor=GLIC, peso=700, alinha="center"))
    return slide("conta", 400, p, rs,
                 eyebrow="Caso ilustrativo", titulo="“Eu como muito bem”",
                 destaque="Triatleta amadora, trinta e poucos anos, encaminhada depois da terceira lesão em um ano.",
                 destaque_cor="petr")


def ingestao():
    """4.2: o registro de sete dias e a direção do erro."""
    p = [svg_abre(1664, 420, "À esquerda, uma tira de sete dias de registro alimentar com o fim de semana destacado, ou recordatórios de 24 horas repetidos com foto das refeições. À direita, duas barras: o que foi comido de verdade e o que foi registrado, menor, porque o erro tem direção, para baixo; e numa terceira barra, de quem se preocupa com o corpo, a diferença é ainda maior")]
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    rs = [rot(0, 0, "Registro de 3 a 7 dias, com um dia de fim de semana", w=820, tam=24, cor=OXID, peso=700)]
    for k, d in enumerate(dias):
        x = k * 112
        fds = k >= 5
        p.append(f'<rect x="{x}" y="50" width="100" height="130" rx="10" fill="{OXID_T if fds else CARTAO}" stroke="{OXID}" stroke-width="{4 if fds else 2}"/>')
        p.append(icone("t:notebook", x + 30, 70, 40, OXID))
        rs.append(rot(x, 128, d, w=100, tam=22, cor=OXID if fds else TINTA, peso=700 if fds else 400, alinha="center"))
    rs.append(rot(0, 210, "ou recordatórios de 24 horas repetidos, em dias diferentes, com foto das refeições", w=780, tam=22, cor=TINTA, lh=1.25))
    p.append(icone("t:camera-selfie", 0, 290, 56, OXID))
    rs.append(rot(70, 300, "a foto pega o azeite, a porção e o que se come em pé", w=700, tam=22, cor=MUDO, lh=1.2))
    # direção do erro
    X0, B = 900, 400
    barras = [("comido de verdade", 300, AZUL), ("registrado", 230, GLIC), ("registrado, quem se preocupa com o corpo", 170, FOSF)]
    for k, (t, h, cor) in enumerate(barras):
        x = X0 + k * 250
        p.append(f'<rect x="{x}" y="{B - h}" width="170" height="{h}" rx="6" fill="{cor}"/>')
        rs.append(rot(x + 8, B - h + 14, t, w=154, tam=20, cor=PAPEL, peso=700, alinha="center", lh=1.15))
    p.append(f'<line x1="{X0 - 20}" y1="{B}" x2="1664" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="{X0}" y1="{B - 300}" x2="1660" y2="{B - 300}" stroke="{AZUL}" stroke-width="2"{TRACO}/>')
    rs.append(rot(X0 - 20, 0, "O erro tem direção: para baixo, e não é aleatório", w=784, tam=24, cor=FOSF, peso=700))
    return slide("ingestao", 420, p, rs,
                 eyebrow="Passo um", titulo="A ingestão", fonte="Barras: esquema, sem valores medidos")


def gasto():
    """4.2: o gasto do exercício com o repouso descontado, e os instrumentos."""
    p = [svg_abre(1664, 420, "À esquerda, a conta certa do gasto do exercício: MET menos um, vezes o peso, vezes as horas. Uma barra de gasto total da sessão tem embaixo uma fatia, o repouso que já seria gasto, que sai da conta; em 90 minutos por dia, perto de 100 quilocalorias de diferença. À direita, os instrumentos: relógios e aplicativos tendem a superestimar; a exceção é o medidor de potência no ciclismo, em que os quilojoules de trabalho aproximam as quilocalorias gastas")]
    p.append(caixa(0, 0, 900, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "A conta certa", w=850, tam=28, cor=OXID, peso=700, serif=True),
          rot(24, 70, "(MET − 1) × peso × horas", w=850, tam=40, cor=TINTA, peso=700, serif=True)]
    p.append(f'<rect x="60" y="150" width="200" height="200" rx="6" fill="{GLIC}"/>')
    p.append(f'<rect x="60" y="300" width="200" height="50" rx="6" fill="{CINZA}" stroke="{FOSF}" stroke-width="3" stroke-dasharray="8 6"/>')
    rs += [rot(60, 200, "gasto da sessão", w=200, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.15),
           rot(60, 312, "repouso", w=200, tam=20, cor=TINTA, alinha="center"),
           rot(290, 290, "o “menos um”: o repouso que já seria gasto sai da conta", w=580, tam=22, cor=TINTA, lh=1.25),
           rot(290, 170, "em 90 minutos por dia, perto de 100 kcal de diferença", w=580, tam=24, cor=OXID, peso=700, lh=1.25)]
    p.append(caixa(964, 0, 700, 200, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:device-watch", 988, 40, 64, GLIC))
    p.append(icone("t:trending-up", 1070, 52, 44, FOSF))
    rs += [rot(1140, 30, "Relógios e aplicativos", w=500, tam=26, cor=GLIC, peso=700, serif=True),
           rot(1140, 76, "tendem a superestimar", w=500, tam=22, cor=TINTA)]
    p.append(caixa(964, 220, 700, 200, OXID, CARTAO, esp=3, rx=16))
    p.append(icone("t:bike", 988, 262, 64, OXID))
    rs += [rot(1080, 246, "A exceção: medidor de potência", w=560, tam=26, cor=OXID, peso=700, serif=True),
           rot(1080, 292, "kJ de trabalho ≈ kcal gastas", w=560, tam=28, cor=TINTA, peso=700),
           rot(1080, 340, "eficiência do pedal de 20 a 25%, e 1 kcal ≈ 4 kJ", w=560, tam=20, cor=MUDO)]
    return slide("gasto", 420, p, rs, eyebrow="Passo dois", titulo="O gasto do exercício, descontado o repouso")


def massa():
    """4.2: três métodos, três números para a mesma pessoa."""
    p = [svg_abre(1664, 400, "Uma mesma pessoa medida por três métodos, bioimpedância, dobras cutâneas e densitometria, com três barras de massa livre de gordura de alturas diferentes. Ao lado, a regra: sempre o mesmo método; sem nenhum, estime um percentual razoável e assuma que o erro existe")]
    p.append(icone("t:user", 0, 120, 180, TINTA))
    rs = [rot(0, 320, "a mesma pessoa", w=180, tam=22, cor=TINTA, alinha="center")]
    met = [("bioimpedância", 230, AZUL, "t:bolt"), ("dobras cutâneas", 270, GLIC, "t:ruler-measure"), ("densitometria", 250, OXID, "t:scale")]
    for k, (t, h, cor, ic) in enumerate(met):
        x = 280 + k * 230
        p.append(f'<rect x="{x}" y="{340 - h}" width="160" height="{h}" rx="6" fill="{cor}"/>')
        p.append(icone(ic, x + 56, 340 - h + 20, 48, PAPEL))
        rs.append(rot(x - 30, 350, t, w=220, tam=22, cor=cor, peso=700, alinha="center"))
    p.append(f'<line x1="260" y1="340" x2="980" y2="340" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(280, 20, "massa livre de gordura estimada", w=700, tam=20, cor=MUDO))
    p.append(caixa(1060, 40, 604, 300, OXID, OXID_T, esp=3, rx=18))
    rs += [rot(1084, 70, "Sempre o mesmo método", w=560, tam=34, cor=OXID, peso=700, serif=True),
           rot(1084, 150, "sem nenhum: estime um percentual razoável e assuma que o erro existe", w=560, tam=24, cor=TINTA, lh=1.3)]
    return slide("massa", 400, p, rs,
                 eyebrow="Passo três · o denominador", titulo="Três métodos, três números para a mesma pessoa",
                 fonte="Barras: esquema, sem valores medidos")


def erro():
    """4.2: os quatro cenários da mesma mulher, marcados na régua."""
    p = [svg_abre(1664, 400, "Uma régua de disponibilidade energética de 15 a 50, com as faixas abaixo de 30, de 30 a 45 e acima de 45. Quatro pontos para a mesma mulher: conta revisada, cerca de 38; registro 20% abaixo e relógio 30% acima, cerca de 22; método que marca 28% de gordura, cerca de 41; método que marca 18% de gordura, cerca de 36")]
    rs = []
    X = regua_ea(p, rs, 500, 1640, 320)
    cen = [("Conta revisada", "2.400 − 700 ÷ 45 kg", 38, TINTA),
           ("Registro −20%, relógio +30%", "1.920 − 910 ÷ 45 kg", 22, FOSF),
           ("Método marca 28% de gordura", "2.400 − 700 ÷ 42 kg", 41, GLIC),
           ("Método marca 18% de gordura", "2.400 − 700 ÷ 47,5 kg", 36, GLIC)]
    for k, (t, d, v, cor) in enumerate(cen):
        y = k * 72
        rs += [rot(0, y + 2, t, w=470, tam=22, cor=cor, peso=700), rot(0, y + 32, d, w=470, tam=18, cor=MUDO)]
        p.append(f'<line x1="480" y1="{y + 24}" x2="{X(v):.0f}" y2="{y + 24}" stroke="{CINZA}" stroke-width="2"{TRACO}/>')
        p.append(f'<line x1="{X(v):.0f}" y1="{y + 24}" x2="{X(v):.0f}" y2="314" stroke="{cor}" stroke-width="2"/>')
        p.append(f'<circle cx="{X(v):.0f}" cy="{y + 24}" r="14" fill="{cor}" stroke="{CARTAO}" stroke-width="3"/>')
        rs.append(rot(X(v) + 20, y + 8, f"≈ {v}", w=100, tam=24, cor=cor, peso=700))
    return slide("erro", 400, p, rs,
                 eyebrow="Passo quatro · propagar o erro", titulo="A mesma mulher, números diferentes",
                 destaque="Número muito baixo pode ser artefato. Número na casa dos 40 não tranquiliza quem tem três lesões. A conta gera hipótese.",
                 destaque_cor="verm", fonte="Suposições de erro para o cálculo; direção do erro conforme Burke e colaboradores, 2018")


def semconta():
    """4.2: a pergunta que dispensa calculadora, e o questionário que rastreia."""
    p = [svg_abre(1664, 420, "À esquerda, a pergunta que dispensa calculadora: o treino subiu e o prato não mudou? Se sim, a conta está negativa até prova em contrário. À direita, o questionário LEAF-Q, 25 itens sobre lesão, intestino e função reprodutiva, com corte em 8: sensibilidade de 78% e especificidade de 90%; para homens, o LEAM-Q, em validação"), defs(TINTA)]
    p.append(caixa(0, 0, 760, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "Sem calculadora", w=720, tam=28, cor=OXID, peso=700, serif=True)]
    p.append(icone("t:barbell", 60, 100, 70, GLIC))
    p.append(icone("t:trending-up", 140, 110, 50, GLIC))
    p.append(icone("t:salad", 330, 100, 70, AZUL))
    p.append(icone("t:arrows-exchange", 410, 110, 50, AZUL))
    rs += [rot(30, 180, "o treino subiu", w=220, tam=22, cor=GLIC, peso=700, alinha="center"),
           rot(300, 180, "o prato não mudou", w=220, tam=22, cor=AZUL, peso=700, alinha="center")]
    p.append(seta(380, 230, 380, 270, TINTA, "m0", esp=4))
    p.append(caixa(40, 280, 680, 110, FOSF, FOSF_T, esp=3, rx=14))
    rs.append(rot(60, 300, "a conta está negativa até prova em contrário", w=640, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.2))
    p.append(caixa(824, 0, 840, 420, GLIC, CARTAO, esp=3, rx=16))
    rs += [rot(848, 16, "LEAF-Q", w=400, tam=30, cor=GLIC, peso=700, serif=True),
           rot(848, 62, "25 itens: lesão, intestino, função reprodutiva · corte em 8", w=790, tam=21, cor=TINTA)]
    for k, (t, v, cor) in enumerate([("sensibilidade", 78, OXID), ("especificidade", 90, AZUL)]):
        y = 130 + k * 90
        rs.append(rot(848, y + 8, t, w=210, tam=22, cor=TINTA, peso=600))
        p.append(f'<rect x="1070" y="{y}" width="460" height="44" rx="8" fill="{CINZA}"/>')
        p.append(f'<rect x="1070" y="{y}" width="{460 * v / 100:.0f}" height="44" rx="8" fill="{cor}"/>')
        rs.append(rot(1540, y + 6, f"{v}%", w=110, tam=28, cor=cor, peso=700))
    rs += [rot(848, 320, "homens: LEAM-Q, em validação", w=790, tam=22, cor=MUDO),
           rot(848, 360, "rastreia; falso positivo é esperado", w=790, tam=22, cor=GLIC, peso=700)]
    return slide("semconta", 420, p, rs,
                 eyebrow="Passo cinco · quando a conta não sai", titulo="Os caminhos mais baratos",
                 destaque="Os itens se confundem com treino pesado: o questionário rastreia, não diagnostica.",
                 destaque_cor="tinta", fonte="Melin e colaboradores, British Journal of Sports Medicine 2014 · 84 atletas")


def lanche():
    """4.2: a distância de 38 a 45 virando um lanche de verdade."""
    p = [svg_abre(1664, 400, "Na régua de disponibilidade, uma seta vai de 38 a 45: sete pontos. Sete pontos vezes 45 quilos de massa livre de gordura dão cerca de 315 quilocalorias por dia, desenhadas como um lanche de verdade perto do treino"), defs(OXID)]
    rs = []
    X = regua_ea(p, rs, 0, 900, 140)
    p.append(f'<path d="M {X(38):.0f} 110 C {X(40):.0f} 60, {X(43):.0f} 60, {X(45):.0f} 106" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m0)"/>')
    rs += [rot(X(38) - 100, 70, "38", w=80, tam=26, cor=GLIC, peso=700, alinha="center"),
           rot(X(41.5) - 120, 20, "+ 7 pontos", w=240, tam=26, cor=OXID, peso=700, alinha="center")]
    rs += [rot(0, 280, "7 × 45 kg de massa livre de gordura", w=900, tam=30, cor=TINTA, peso=700, serif=True, alinha="center")]
    p.append(caixa(980, 20, 684, 360, OXID, OXID_T, esp=3, rx=20))
    p.append(icone("t:salad", 1040, 70, 120, OXID))
    p.append(icone("t:apple", 1180, 90, 80, OXID))
    p.append(icone("t:cookie", 1280, 90, 80, OXID))
    rs += [rot(1000, 210, "≈ 315 kcal por dia", w=644, tam=44, cor=OXID, peso=700, alinha="center", serif=True),
           rot(1000, 290, "um lanche real, perto do treino", w=644, tam=24, cor=TINTA, alinha="center")]
    return slide("lanche", 400, p, rs,
                 eyebrow="Passo seis · o que fazer com o número", titulo="Acrescentar comida, não tirar treino",
                 destaque="“O treino não é demais; a comida é pouca para o treino que você faz.” O mesmo desequilíbrio, dito pelo lado que preserva a identidade.",
                 destaque_cor="tinta")

# ---------------------------------------------------------------- aplicação

LICOES = {"04-01": [equacao, conta_41, revisao, medida, alarme, portas_41, controversia],
          "04-02": [conta_42, ingestao, gasto, massa, erro, semconta, lanche]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
