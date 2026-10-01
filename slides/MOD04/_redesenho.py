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

# ---------------------------------------------------------------- 4.3

def identidade():
    """4.3: dois eixos para decidir a dose: a identidade, riscada, e a demanda."""
    p = [svg_abre(1664, 400, "Dois caminhos para a dose de carboidrato. Em cima, riscado: a identidade, eu sou corredor, que leva à pergunta a favor ou contra. Embaixo, a demanda: quanto tempo, que intensidade e quando é a próxima sessão, que leva à dose"), defs(MUDO, OXID)]
    rs = []
    linhas_ = [(20, "t:id", "“Eu sou corredor”", "a favor ou contra?", FOSF, True),
               (220, "t:calendar", "quanto tempo · que intensidade · quando é a próxima sessão", "a dose da sessão", OXID, False)]
    for y, ic, t, res, cor, risca in linhas_:
        p.append(caixa(0, y, 980, 150, cor, FOSF_T if risca else OXID_T, esp=3, rx=18))
        p.append(icone(ic, 30, y + 40, 70, cor))
        rs.append(rot(130, y + 30 if risca else y + 26, t, w=820, tam=32 if risca else 28, cor=cor, peso=700, serif=True, lh=1.2))
        p.append(seta(990, y + 75, 1130, y + 75, cor if not risca else MUDO, "m1" if not risca else "m0", esp=5))
        p.append(caixa(1140, y, 524, 150, cor, CARTAO, esp=3, rx=18))
        rs.append(rot(1140, y + 52, res, w=524, tam=30, cor=cor, peso=700, alinha="center", serif=True))
        if risca:
            p.append(f'<line x1="20" y1="{y + 140}" x2="960" y2="{y + 10}" stroke="{FOSF}" stroke-width="6" stroke-linecap="round" opacity="0.7"/>')
    return slide("identidade", 400, p, rs,
                 eyebrow="O erro é de eixo", titulo="A dose foi prescrita pela identidade, e não pela demanda",
                 destaque="O carboidrato é o único macronutriente com opinião moral, e a pergunta clínica vira “a favor ou contra?”.",
                 destaque_cor="tinta")


def demais():
    """4.3: oito gramas por quilo contra quatro horas de treino por semana."""
    p = [svg_abre(1664, 420, "À esquerda, a conta: 78 quilos vezes 8 gramas por quilo dão 624 gramas de carboidrato por dia, cerca de 2.500 quilocalorias só de carboidrato. À direita, a semana de treino: sete barras de cerca de 34 minutos, quatro horas por semana, ao lado das barras tracejadas, bem mais altas, da semana de quem treina em alto volume, a quem essa dose se destina")]
    blocos = [(0, "78 kg × 8 g/kg", AZUL), (0, "= 624 g por dia", GLIC), (0, "≈ 2.500 kcal só de carboidrato", GLIC)]
    rs = []
    for k, (x, t, cor) in enumerate(blocos):
        y = 20 + k * 120
        p.append(caixa(0, y, 640, 100, cor, CARTAO if k == 0 else GLIC_T, esp=3, rx=16))
        rs.append(rot(0, y + 26, t, w=640, tam=36, cor=cor, peso=700, alinha="center", serif=True))
    rs.append(rot(0, 384, "antes de proteína e gordura", w=640, tam=22, cor=MUDO, alinha="center"))
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    B = 360
    for k, d in enumerate(dias):
        x = 760 + k * 128
        p.append(f'<rect x="{x}" y="{B - 260}" width="80" height="260" rx="6" fill="none" stroke="{CINZA}" stroke-width="2" stroke-dasharray="8 6"/>')
        p.append(f'<rect x="{x}" y="{B - 34 * 1.6:.0f}" width="80" height="{34 * 1.6:.0f}" rx="6" fill="{TINTA}"/>')
        rs.append(rot(x - 10, B + 8, d, w=100, tam=20, cor=MUDO, alinha="center"))
    rs += [rot(760, 0, "≈ 4 h por semana: menos de 40 minutos por dia", w=900, tam=26, cor=TINTA, peso=700),
           rot(760, 40, "tracejado: a semana de quem treina em alto volume", w=900, tam=20, cor=MUDO)]
    return slide("demais", 420, p, rs,
                 eyebrow="Primeiro erro · demais para a demanda", titulo="Oito gramas por quilo, quatro horas por semana",
                 destaque="Não há mistério metabólico. É a dieta de quem treina em alto volume, com quatro horas por semana.",
                 destaque_cor="tinta", fonte="Barras tracejadas: esquema")


def marchadores():
    """4.3: o que o cetogênico fez nos marchadores: mais gordura queimada, pior economia, sem ganho."""
    p = [svg_abre(1664, 420, "Três painéis esquemáticos dos marchadores de elite. A oxidação de gordura subiu muito no grupo cetogênico. A economia piorou: mais oxigênio para a mesma velocidade. E o ganho do bloco de treino, que veio nos grupos com carboidrato, não veio no cetogênico. O resultado se repetiu em 2020, com mais atletas e incluindo mulheres")]
    W = 520
    paineis = [("A oxidação de gordura subiu", OXID, [("carbo", 0.25, CINZA), ("cetogênico", 0.95, OXID)], "a adaptação é real e mensurável"),
               ("A economia piorou", FOSF, [("carbo", 0.5, CINZA), ("cetogênico", 0.75, FOSF)], "mais oxigênio para a mesma velocidade"),
               ("O ganho do treino não veio", FOSF, [("carbo alto", 0.7, AZUL), ("periodizado", 0.75, AZUL), ("cetogênico", 0.04, FOSF)], "os outros grupos melhoraram")]
    rs = []
    for j, (t, cor, barras, d) in enumerate(paineis):
        x0 = j * (W + 52)
        p.append(caixa(x0, 0, W, 420, cor, CARTAO, esp=3, rx=16))
        rs += [rot(x0 + 20, 14, t, w=W - 40, tam=26, cor=cor, peso=700, serif=True),
               rot(x0 + 20, 370, d, w=W - 40, tam=20, cor=TINTA)]
        bw = 110 if len(barras) == 3 else 150
        for k, (n, v, c) in enumerate(barras):
            x = x0 + 40 + k * (bw + 40)
            h = v * 230
            p.append(f'<rect x="{x}" y="{300 - h:.0f}" width="{bw}" height="{max(h, 4):.0f}" rx="6" fill="{c}"/>')
            rs.append(rot(x - 20, 310, n, w=bw + 40, tam=18, cor=MUDO, alinha="center"))
        p.append(f'<line x1="{x0 + 20}" y1="300" x2="{x0 + W - 20}" y2="300" stroke="{MUDO}" stroke-width="2"/>')
    return slide("marchadores", 420, p, rs,
                 eyebrow="Segundo erro · de menos para a intensidade", titulo="Os marchadores de elite",
                 destaque="Gordura custa mais oxigênio por ATP. No leve, quase não importa. Na intensidade alta, importa muito. E o resultado se repetiu em 2020, com mais atletas e incluindo mulheres.",
                 destaque_cor="tinta", fonte="Barras: esquema, sem valores medidos · Burke e colaboradores, Journal of Physiology 2017 · PLoS One 2020")


def paraquem():
    """4.3: a régua de intensidade com quem pode e quem provavelmente não, e o teste de seis semanas."""
    p = [svg_abre(1664, 420, "Uma régua de intensidade do treino, do leve ao intenso. No lado leve, sem prejuízo relevante para baixo carboidrato: treino predominantemente leve, preferência forte sem competir, razão clínica. No lado intenso, provavelmente não: quem compete, alta intensidade frequente, esporte intermitente, glicolítico por natureza. Embaixo, um teste de seis semanas com carboidrato só em torno das sessões intensas e o desempenho registrado")]
    p.append(f'<defs><linearGradient id="gi" x1="0" x2="1"><stop offset="0" stop-color="{OXID}"/><stop offset="1" stop-color="{FOSF}"/></linearGradient></defs>')
    p.append(f'<rect x="0" y="0" width="1664" height="22" rx="11" fill="url(#gi)"/>')
    rs = [rot(0, 30, "treino leve", w=300, tam=20, cor=OXID, peso=700), rot(1364, 30, "treino intenso", w=300, tam=20, cor=FOSF, peso=700, alinha="right")]
    lados = [(0, "Sem prejuízo relevante", OXID, OXID_T, ["treino predominantemente leve", "preferência forte, sem competir", "razão clínica"]),
             (864, "Provavelmente não", FOSF, FOSF_T, ["quem compete", "alta intensidade frequente", "esporte intermitente, glicolítico por natureza"])]
    for x, t, cor, fundo, itens in lados:
        p.append(caixa(x, 70, 800, 200, cor, fundo, esp=3, rx=16))
        rs.append(rot(x + 24, 82, t, w=760, tam=26, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            rs.append(rot(x + 24, 130 + k * 42, "· " + it, w=760, tam=22, cor=TINTA))
    rs.append(rot(0, 290, "Teste de seis semanas, com desempenho registrado", w=1100, tam=24, cor=TINTA, peso=700))
    for k in range(6):
        x = k * 278
        p.append(caixa(x, 330, 258, 90, MUDO, PAPEL, esp=2, rx=12))
        rs.append(rot(x + 14, 342, f"semana {k + 1}", w=230, tam=20, cor=MUDO))
        for j, intensa in enumerate([True, False, False, True, False]):
            p.append(f'<rect x="{x + 14 + j * 46}" y="376" width="36" height="30" rx="4" fill="{GLIC if intensa else CINZA}"/>')
    rs.append(rot(1180, 290, "carboidrato só nas sessões intensas", w=484, tam=20, cor=GLIC, peso=700, alinha="right"))
    return slide("paraquem", 420, p, rs,
                 eyebrow="Baixo carboidrato", titulo="Para quem, e como conversar",
                 destaque="A decisão sai com os números da pessoa. E cortar carboidrato costuma cortar o total.",
                 destaque_cor="ambar")


def comida():
    """4.3: a prateleira de comida de verdade, e o gel ao lado com o preço de várias bananas."""
    p = [svg_abre(1664, 420, "À esquerda, uma prateleira de comida de verdade para o carboidrato durante o treino: banana média, cerca de 25 gramas; pão francês com geleia, mais de 30 gramas; tapioca com mel; bolacha de água e sal; doce de banana; rapadura; tâmaras; água de coco. À direita, o gel: compacto, não amassa, rótulo com a quantidade; conveniência, não requisito fisiológico; e custa muitas vezes uma banana")]
    p.append(caixa(0, 0, 1040, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 14, "Comida de verdade", w=990, tam=28, cor=OXID, peso=700, serif=True)]
    itens = [("banana média", "≈ 25 g"), ("pão francês com geleia", "> 30 g"), ("tapioca com mel", ""), ("bolacha de água e sal", ""),
             ("doce de banana", ""), ("rapadura", ""), ("tâmaras", ""), ("água de coco", "")]
    for k, (t, g) in enumerate(itens):
        x, y = 24 + (k % 4) * 250, 80 + (k // 4) * 160
        p.append(caixa(x, y, 230, 140, OXID, CARTAO, esp=2, rx=14))
        rs.append(rot(x + 10, y + 20, t, w=210, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.2))
        if g:
            rs.append(rot(x + 10, y + 90, g, w=210, tam=28, cor=OXID, peso=700, alinha="center", serif=True))
    rs.append(rot(24, 392, "carboidrato por porção, quando medido", w=990, tam=18, cor=MUDO))
    p.append(caixa(1100, 0, 564, 420, GLIC, GLIC_T, esp=3, rx=16))
    rs += [rot(1124, 14, "O gel", w=520, tam=28, cor=GLIC, peso=700, serif=True),
           rot(1124, 64, "compacto, não amassa, rótulo com a quantidade", w=520, tam=21, cor=TINTA, lh=1.2),
           rot(1124, 128, "conveniência, não requisito fisiológico", w=520, tam=21, cor=GLIC, peso=700, lh=1.2)]
    p.append(f'<rect x="1130" y="230" width="90" height="140" rx="14" fill="{GLIC}"/>')
    rs.append(rot(1240, 240, "=", w=40, tam=40, cor=TINTA, peso=700))
    for k in range(5):
        p.append(f'<path d="M {1300 + k * 70} 300 q 30 -60 60 -40 q -20 10 -50 60 z" fill="#E2BE55" stroke="{GLIC}" stroke-width="2"/>')
    rs.append(rot(1290, 330, "custa muitas vezes uma banana", w=360, tam=20, cor=TINTA, alinha="center"))
    return slide("comida", 420, p, rs,
                 eyebrow="Uma pós feita para o Brasil", titulo="Nada disso exige gel",
                 destaque="Para quem pedala quatro horas toda semana, o custo decide se a estratégia é seguida. Estratégia abandonada tem eficácia zero.",
                 destaque_cor="tinta")


# ---------------------------------------------------------------- 4.4

def decisao():
    """4.4: a ferramenta certa, o paciente errado, a ordem errada."""
    p = [svg_abre(1664, 400, "Três verificações lado a lado. A ferramenta: certa, a periodização nutricional é legítima e nasceu no esporte de elite. O paciente: errado, ele trabalha nove horas por dia. A ordem: errada, o refinamento veio antes do básico")]
    cols = [("t:tools", "A ferramenta", "certa", "legítima, nasceu no esporte de elite", OXID, "t:check"),
            ("t:briefcase", "O paciente", "errado", "trabalha nove horas por dia", FOSF, "t:x"),
            ("t:stairs", "A ordem", "errada", "o refinamento veio antes do básico", FOSF, "t:x")]
    rs = []
    for k, (ic, t, v, d, cor, marca) in enumerate(cols):
        x = k * 570
        p.append(caixa(x, 0, 524, 400, cor, OXID_T if cor == OXID else FOSF_T, esp=3, rx=18))
        p.append(icone(ic, x + 30, 30, 70, cor))
        p.append(f'<circle cx="{x + 460}" cy="66" r="40" fill="{cor}"/>')
        p.append(icone(marca, x + 436, 42, 48, PAPEL))
        rs += [rot(x + 30, 130, t, w=470, tam=30, cor=TINTA, peso=700, serif=True),
               rot(x + 30, 180, v, w=470, tam=44, cor=cor, peso=700, serif=True),
               rot(x + 30, 260, d, w=470, tam=24, cor=TINTA, lh=1.3)]
    return slide("decisao", 400, p, rs,
                 eyebrow="Periodizar ou não, e em que nível", titulo="A ferramenta certa, no paciente errado, na ordem errada",
                 destaque="A pergunta é quanto da periodização sobrevive quando o paciente trabalha nove horas por dia.",
                 destaque_cor="tinta")


def familias():
    """4.4: a refeição grande e a sobremesa pequena da periodização."""
    p = [svg_abre(1664, 420, "À esquerda, um prato grande: a refeição, alta disponibilidade de carboidrato, combustível para o trabalho exigido, com a dose acompanhando a sessão que vem; consensual, baixo risco, quase todo o ganho. À direita, uma tigela pequena: a sobremesa, baixa disponibilidade, treinar em jejum, dois treinos sem repor entre eles, a sessão da noite e dormir sem carboidrato")]
    p.append(f'<circle cx="300" cy="210" r="200" fill="{OXID_T}" stroke="{OXID}" stroke-width="6"/>')
    p.append(f'<circle cx="300" cy="210" r="150" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
    rs = [rot(160, 120, "A refeição", w=280, tam=34, cor=OXID, peso=700, alinha="center", serif=True),
          rot(160, 176, "alta disponibilidade", w=280, tam=22, cor=TINTA, alinha="center"),
          rot(160, 220, "quase todo o ganho", w=280, tam=22, cor=OXID, peso=700, alinha="center")]
    itens = ["combustível para o trabalho exigido", "a dose acompanha a sessão que vem", "consensual, baixo risco"]
    for k, t in enumerate(itens):
        rs.append(rot(540, 60 + k * 70, "· " + t, w=480, tam=23, cor=TINTA))
    p.append(f'<path d="M 1180 200 q 140 160 280 0 z" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="5"/>')
    p.append(f'<line x1="1160" y1="200" x2="1480" y2="200" stroke="{GLIC}" stroke-width="5"/>')
    rs += [rot(1160, 110, "A sobremesa", w=320, tam=30, cor=GLIC, peso=700, alinha="center", serif=True),
           rot(1160, 150, "baixa disponibilidade", w=320, tam=20, cor=TINTA, alinha="center")]
    sob = ["treinar em jejum", "dois treinos sem repor entre eles", "a sessão da noite e dormir sem carboidrato"]
    for k, t in enumerate(sob):
        rs.append(rot(1120, 300 + k * 38, "· " + t, w=540, tam=21, cor=TINTA))
    return slide("familias", 420, p, rs,
                 eyebrow="Duas revisões de 2017 e 2018", titulo="Um princípio de planejamento, duas famílias",
                 destaque="Periodizar é ajustar a nutrição ao objetivo de cada sessão e de cada fase. Nesse sentido amplo, quase todo mundo deveria periodizar alguma coisa.",
                 destaque_cor="tinta", fonte="Jeukendrup, Sports Medicine 2017 · Impey e colaboradores, Sports Medicine 2018")


def limites():
    """4.4: cinco barreiras numa pista antes da periodização."""
    p = [svg_abre(1664, 420, "Uma pista com cinco barreiras antes da periodização no amador: margem de erro, o elite erra e alguém corrige, o amador descobre três meses depois; o denominador do ganho, 1 a 3% sobre base otimizada contra buracos grandes no básico; orçamento de atenção, a complexidade não soma, desloca; deriva para o déficit, treinar com pouco vira comer pouco; o objetivo é outro, pico numa data contra treinar bem o ano inteiro"), defs(TINTA)]
    p.append(f'<line x1="0" y1="190" x2="1600" y2="190" stroke="{MUDO}" stroke-width="3"/>')
    p.append(seta(1560, 190, 1650, 190, TINTA, "m0", esp=4))
    bar = [("Margem de erro", "o elite erra e alguém corrige; o amador descobre três meses depois", TINTA),
           ("O denominador do ganho", "1 a 3% sobre base otimizada, contra buracos grandes no básico", FOSF),
           ("Orçamento de atenção", "a complexidade não soma; desloca", TINTA),
           ("Deriva para o déficit", "treinar com pouco vira comer pouco", GLIC),
           ("O objetivo é outro", "pico numa data contra treinar bem o ano inteiro", TINTA)]
    rs = []
    for k, (t, d, cor) in enumerate(bar):
        x = 20 + k * 320
        p.append(f'<rect x="{x + 100}" y="110" width="12" height="80" fill="{cor}"/><rect x="{x + 180}" y="110" width="12" height="80" fill="{cor}"/>')
        p.append(f'<rect x="{x + 90}" y="104" width="112" height="18" rx="4" fill="{cor}"/>')
        rs += [rot(x + 146 - 40, 40, str(k + 1), w=80, tam=40, cor=cor, peso=700, alinha="center", serif=True),
               rot(x, 210, t, w=300, tam=24, cor=cor, peso=700, alinha="center", lh=1.15),
               rot(x, 280, d, w=300, tam=20, cor=TINTA, alinha="center", lh=1.25)]
    return slide("limites", 420, p, rs, eyebrow="Por que antes da hora", titulo="Cinco limites estruturais no amador")


def triagem():
    """4.4: quatro colunas que seguram o telhado da periodização."""
    p = [svg_abre(1664, 420, "Um frontão sustentado por quatro colunas. As colunas: energia total adequada, fora da zona cinza; proteína distribuída, e não concentrada no jantar; carboidrato alinhado à sessão, mais no dia intenso e menos no leve; sono, a variável que ninguém periodiza. O telhado, só depois que as quatro estão estáveis por três meses: a periodização")]
    p.append(f'<path d="M 232 110 L 832 10 L 1432 110 Z" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
    rs = [rot(532, 60, "periodização, só depois", w=600, tam=26, cor=GLIC, peso=700, alinha="center", serif=True)]
    cols = [("t:battery-4", "Energia total adequada", "fora da zona cinza"), ("t:barbell", "Proteína distribuída", "e não concentrada no jantar"),
            ("t:calendar", "Carboidrato alinhado à sessão", "mais no dia intenso, menos no leve"), ("t:moon", "Sono", "a variável que ninguém periodiza")]
    for k, (ic, t, d) in enumerate(cols):
        x = 232 + k * 310
        p.append(f'<rect x="{x}" y="120" width="270" height="250" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
        p.append(icone(ic, x + 105, 140, 60, OXID))
        rs += [rot(x + 10, 214, t, w=250, tam=23, cor=OXID, peso=700, alinha="center", lh=1.15),
               rot(x + 10, 290, d, w=250, tam=19, cor=TINTA, alinha="center", lh=1.2)]
    p.append(f'<rect x="212" y="370" width="1240" height="30" fill="{CINZA}"/>')
    rs.append(rot(212, 372, "estáveis por três meses", w=1240, tam=20, cor=TINTA, peso=700, alinha="center"))
    return slide("triagem", 420, p, rs,
                 eyebrow="A regra de triagem", titulo="Quatro coisas estáveis por três meses",
                 destaque="Quem não cumpre as quatro não precisa de periodização. Precisa das quatro.", destaque_cor="tinta")


def nunca():
    """4.4: cinco placas de pare para a restrição deliberada."""
    p = [svg_abre(1664, 400, "Cinco placas de pare, uma para cada grupo em que restrição deliberada de carboidrato é risco sem contrapartida: adolescente em crescimento; história de transtorno alimentar ou relação difícil com a comida; disponibilidade energética já baixa; gestante; doença crônica descompensada")]
    grupos = [("t:seedling", "Adolescente em crescimento"), ("t:mood-sad", "Transtorno alimentar ou relação difícil com a comida"),
              ("t:battery-1", "Disponibilidade energética já baixa"), ("t:baby-carriage", "Gestante"), ("t:heartbeat", "Doença crônica descompensada")]
    rs = []
    for k, (ic, t) in enumerate(grupos):
        x = k * 336
        cx = x + 150
        pts = " ".join(f"{cx + 110 * __import__('math').cos(__import__('math').pi / 8 + j * __import__('math').pi / 4):.0f},{120 + 110 * __import__('math').sin(__import__('math').pi / 8 + j * __import__('math').pi / 4):.0f}" for j in range(8))
        p.append(f'<polygon points="{pts}" fill="{FOSF}" stroke="{CARTAO}" stroke-width="6"/>')
        p.append(icone(ic, cx - 36, 84, 72, PAPEL))
        rs.append(rot(x, 250, t, w=300, tam=23, cor=TINTA, peso=700, alinha="center", lh=1.25))
    return slide("nunca", 400, p, rs,
                 eyebrow="A lista do nunca", titulo="Restrição deliberada aqui é risco sem contrapartida")


def perfis():
    """4.4: três perfis em linha, do que falta à conduta."""
    p = [svg_abre(1664, 400, "Três linhas, cada uma com o perfil, o que falta e a conduta. O amador que dorme pouco: faltam as quatro condições; suspender e fazer o básico. Quem faz quatro estratégias juntas: falta atenção para o básico; manter uma e largar três. Base sólida e prova marcada: não falta nada; nível dois, sem treinar com pouco"), defs(MUDO)]
    linhas_ = [("t:moon", "Amador que dorme pouco", "as quatro condições", "suspender e fazer o básico", FOSF),
               ("t:list-check", "Quatro estratégias juntas", "atenção para o básico", "manter uma, largar três", GLIC),
               ("t:flag", "Base sólida, prova marcada", "nada", "nível dois, sem treinar com pouco", OXID)]
    rs = [rot(0, 0, "Perfil", w=520, tam=22, cor=MUDO, peso=700), rot(600, 0, "O que falta", w=460, tam=22, cor=MUDO, peso=700),
          rot(1140, 0, "Conduta", w=524, tam=22, cor=MUDO, peso=700)]
    for k, (ic, t, f, c, cor) in enumerate(linhas_):
        y = 44 + k * 118
        p.append(caixa(0, y, 520, 100, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, 20, y + 26, 48, cor))
        rs.append(rot(84, y + 30, t, w=420, tam=24, cor=TINTA, peso=700))
        p.append(seta(526, y + 50, 594, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(600, y, 460, 100, cor, PAPEL, esp=2, rx=14))
        rs.append(rot(600, y + 32, f, w=460, tam=24, cor=cor, peso=700, alinha="center"))
        p.append(seta(1066, y + 50, 1134, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(1140, y, 524, 100, cor, cor, esp=0, rx=14))
        rs.append(rot(1140, y + 32, c, w=524, tam=24, cor=PAPEL, peso=700, alinha="center"))
    return slide("perfis", 400, p, rs,
                 eyebrow="O critério aplicado", titulo="Três perfis típicos, três condutas",
                 destaque="Ele fazia a parte difícil e pulava a parte fácil. E os atletas dos estudos não trabalham nove horas por dia.",
                 destaque_cor="ambar")



# ---------------------------------------------------------------- 4.5

def tres():
    """4.5: os três números de proteína numa régua de gramas por quilo."""
    p = [svg_abre(1664, 380, "Uma régua de proteína em gramas por quilo por dia, de zero a três. Em 0,8, o piso populacional contra deficiência, que não é meta para quem treina. Em 1,6, o platô do ganho de massa livre de gordura com treino de força. Em 2,2, o limite superior do intervalo desse platô; a faixa entre 1,6 e 2,2 está sombreada")]
    X0, X1, Y = 40, 1624, 200
    X = lambda v: X0 + v / 3 * (X1 - X0)
    p.append(f'<rect x="{X(1.6):.0f}" y="{Y - 30}" width="{X(2.2) - X(1.6):.0f}" height="60" fill="{OXID_T}"/>')
    p.append(f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="{MUDO}" stroke-width="4"/>')
    rs = []
    for v in (0, 1, 2, 3):
        p.append(f'<line x1="{X(v):.0f}" y1="{Y - 8}" x2="{X(v):.0f}" y2="{Y + 8}" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(v) - 30, Y + 44, str(v), w=60, tam=20, cor=MUDO, alinha="center"))
    marcos = [(0.8, "0,8", "piso populacional contra deficiência", "não é meta para quem treina", TINTA, -1),
              (1.6, "1,6", "platô do ganho de massa livre de gordura", "com treino de força", OXID, 1),
              (2.2, "2,2", "limite superior do intervalo", "desse platô", GLIC, -1)]
    for v, n, t, d, cor, lado in marcos:
        p.append(f'<circle cx="{X(v):.0f}" cy="{Y}" r="16" fill="{cor}" stroke="{CARTAO}" stroke-width="3"/>')
        y = 10 if lado < 0 else 260
        p.append(f'<line x1="{X(v):.0f}" y1="{Y - 18 if lado < 0 else Y + 18}" x2="{X(v):.0f}" y2="{y + 100 if lado < 0 else y}" stroke="{cor}" stroke-width="2"/>')
        rs += [rot(X(v) - 230, y, n, w=460, tam=40, cor=cor, peso=700, alinha="center", serif=True),
               rot(X(v) - 230, y + 50 if lado < 0 else y + 50, t, w=460, tam=21, cor=TINTA, alinha="center")]
        if lado < 0:
            rs.append(rot(X(v) - 230, y + 76, d, w=460, tam=19, cor=MUDO, alinha="center"))
        else:
            rs.append(rot(X(v) - 230, y + 78, d, w=460, tam=19, cor=MUDO, alinha="center"))
    rs.append(rot(X1 - 420, Y + 70, "g por kg por dia", w=420, tam=20, cor=MUDO, alinha="right"))
    return slide("tres", 380, p, rs,
                 eyebrow="Três números que todo mundo mistura", titulo="Gramas por quilo por dia",
                 destaque="“A recomendação oficial é 0,8, o resto é exagero”: o número certo para a pergunta errada.",
                 destaque_cor="tinta")


def teto():
    """4.5: 25 contra 100 gramas: a resposta maior e mais longa, e a conduta."""
    import math
    p = [svg_abre(1664, 400, "À esquerda, curvas esquemáticas de síntese de proteína muscular depois de treino de corpo inteiro: com 25 gramas, a resposta sobe e volta; com 100 gramas, a resposta é maior e mais longa, e passou de 12 horas. À direita, a conduta: refeição grande não é desperdício; 0,25 grama por quilo ou 20 a 40 gramas a cada 3 a 4 horas; a janela pós-treino é larga, salvo quem treina em jejum")]
    X0, X1, Yb = 60, 900, 320
    p.append(f'<line x1="{X0}" y1="{Yb}" x2="{X1}" y2="{Yb}" stroke="{MUDO}" stroke-width="2"/><line x1="{X0}" y1="40" x2="{X0}" y2="{Yb}" stroke="{MUDO}" stroke-width="2"/>')
    def curva(amp, larg, cor, esp):
        pts = [(h, amp * (1 - math.exp(-h / 1.2)) * math.exp(-h / larg)) for h in [x / 4 for x in range(0, 57)]]
        d = "M" + " L".join(f"{X0 + h / 14 * (X1 - X0):.0f} {Yb - v:.0f}" for h, v in pts)
        p.append(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{esp}"/>')
    curva(260, 3.5, MUDO, 5)
    curva(380, 9, OXID, 7)
    x12 = X0 + 12 / 14 * (X1 - X0)
    p.append(f'<line x1="{x12:.0f}" y1="60" x2="{x12:.0f}" y2="{Yb}" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
    rs = [rot(x12 - 60, Yb + 8, "12 h", w=120, tam=20, cor=TINTA, peso=700, alinha="center"),
          rot(X0, Yb + 40, "horas depois do treino", w=X1 - X0, tam=20, cor=MUDO, alinha="center"),
          rot(330, 70, "100 g: maior e mais longa", w=360, tam=22, cor=OXID, peso=700),
          rot(160, 210, "25 g", w=120, tam=22, cor=MUDO, peso=700)]
    p.append(caixa(980, 0, 684, 400, OXID, OXID_T, esp=3, rx=16))
    rs.append(rot(1004, 16, "A conduta", w=640, tam=28, cor=OXID, peso=700, serif=True))
    cond = [("t:check", "refeição grande não é desperdício"), ("t:clock", "0,25 g/kg ou 20 a 40 g a cada 3 a 4 h"),
            ("t:door", "a janela pós-treino é larga, salvo quem treina em jejum")]
    for k, (ic, t) in enumerate(cond):
        y = 84 + k * 100
        p.append(icone(ic, 1004, y, 44, OXID))
        rs.append(rot(1064, y + 4, t, w=580, tam=23, cor=TINTA, lh=1.25))
    return slide("teto", 400, p, rs,
                 eyebrow="Um experimento de 2023", titulo="O mito do teto de 30 gramas",
                 destaque="O problema não é o jantar com 60 g. É o café da manhã com 8.", destaque_cor="verm",
                 fonte="Curvas: esquema · Trommelen e colaboradores, Cell Reports Medicine 2023 · Jäger e colaboradores 2017")


def qualidade():
    """4.5: digestibilidade, aminoácidos que se completam e o gatilho da leucina."""
    p = [svg_abre(1664, 400, "Três painéis sobre a qualidade da proteína. Digestibilidade: quanto do ingerido é absorvido, menor na fonte vegetal. Aminoácidos essenciais: a lisina limita nos cereais e a metionina nas leguminosas, e o arroz com feijão se completa como duas peças. Leucina: o gatilho da síntese, de 700 a 3.000 miligramas por dose")]
    W = 520
    rs = []
    tits = [("Digestibilidade", "quanto do ingerido é absorvido", TINTA), ("Aminoácidos essenciais", "um completa o que falta no outro", TINTA), ("Leucina", "o gatilho da síntese", GLIC)]
    for j, (t, d, cor) in enumerate(tits):
        x = j * (W + 52)
        p.append(caixa(x, 0, W, 400, cor, CARTAO, esp=3, rx=16))
        rs += [rot(x + 20, 14, t, w=W - 40, tam=26, cor=cor, peso=700, serif=True), rot(x + 20, 54, d, w=W - 40, tam=20, cor=MUDO)]
    # 1
    for k, (t, v, cor) in enumerate([("animal", 0.95, AZUL), ("vegetal", 0.8, OXID)]):
        y = 130 + k * 110
        rs.append(rot(20, y + 6, t, w=120, tam=22, cor=cor, peso=700))
        p.append(f'<rect x="140" y="{y}" width="340" height="40" rx="8" fill="{CINZA}"/>')
        p.append(f'<rect x="140" y="{y}" width="{340 * v:.0f}" height="40" rx="8" fill="{cor}"/>')
    rs.append(rot(20, 350, "menor na vegetal", w=480, tam=21, cor=OXID, peso=700))
    rs.append(rot(140, 300, "barras: esquema", w=340, tam=18, cor=MUDO))
    # 2 peças
    x = W + 52
    p.append(f'<path d="M {x+60} 130 h 160 v 50 a 25 25 0 0 1 0 50 v 50 h -160 z" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
    p.append(f'<path d="M {x+240} 130 h 220 v 150 h -220 v -50 a 25 25 0 0 0 0 -50 z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
    rs += [rot(x + 60, 180, "arroz", w=160, tam=24, cor=GLIC, peso=700, alinha="center"),
           rot(x + 270, 180, "feijão", w=190, tam=24, cor=AZUL, peso=700, alinha="center"),
           rot(x + 20, 300, "cereais: falta lisina", w=480, tam=20, cor=TINTA),
           rot(x + 20, 334, "leguminosas: falta metionina", w=480, tam=20, cor=TINTA)]
    # 3 limiar de leucina
    x = 2 * (W + 52)
    p.append(f'<rect x="{x+40}" y="200" width="440" height="50" rx="10" fill="{CINZA}"/>')
    p.append(f'<rect x="{x+40 + 440 * 0.7 / 3.5:.0f}" y="200" width="{440 * 2.3 / 3.5:.0f}" height="50" fill="{GLIC}"/>')
    rs += [rot(x + 40, 140, "700 a 3.000 mg por dose", w=440, tam=26, cor=GLIC, peso=700, alinha="center"),
           rot(x + 40, 262, "0", w=60, tam=18, cor=MUDO), rot(x + 340, 262, "3.500 mg", w=120, tam=18, cor=MUDO, alinha="right"),
           rot(x + 20, 330, "abaixo do limiar, o sinal é fraco", w=480, tam=20, cor=TINTA)]
    return slide("qualidade", 400, p, rs,
                 eyebrow="Uma revisão de 2015", titulo="Qualidade: o que muda entre as fontes",
                 destaque="Vegetariano ganha músculo, com ajuste: um pouco mais por refeição, combinar fontes (arroz com feijão), soja, ovos e laticínios.",
                 destaque_cor="petr", fonte="van Vliet, Burd e van Loon, Journal of Nutrition 2015")


def whey():
    """4.5: o pó que é leite, e a pergunta que muda."""
    p = [svg_abre(1664, 400, "À esquerda, uma equação: uma medida de whey é igual a proteína do leite, conveniente e fácil de dosar, nem mágica nem obrigatória. À direita, a troca de pergunta: precisa de whey, riscada; está fechando a conta com comida, no lugar")]
    p.append(f'<path d="M 60 140 h 180 l -20 200 h -140 z" fill="{PAPEL}" stroke="{MUDO}" stroke-width="4"/>')
    p.append(f'<ellipse cx="150" cy="140" rx="90" ry="22" fill="#EFE8D8" stroke="{MUDO}" stroke-width="3"/>')
    rs = [rot(40, 360, "whey", w=220, tam=24, cor=MUDO, peso=700, alinha="center"),
          rot(270, 200, "=", w=80, tam=60, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<path d="M 400 120 h 140 l -14 220 h -112 z" fill="{CARTAO}" stroke="{AZUL}" stroke-width="4"/>')
    p.append(f'<path d="M 410 170 h 120 l -10 166 h -100 z" fill="{AZUL_T}"/>')
    rs += [rot(360, 360, "proteína do leite", w=220, tam=24, cor=AZUL, peso=700, alinha="center"),
           rot(600, 120, "conveniente, fácil de dosar", w=360, tam=24, cor=TINTA, lh=1.25),
           rot(600, 210, "não é mágica nem obrigatória", w=360, tam=24, cor=OXID, peso=700, lh=1.25)]
    p.append(caixa(1000, 30, 664, 140, MUDO, PAPEL, esp=2, rx=16))
    rs.append(rot(1000, 76, "“Precisa de whey?”", w=664, tam=34, cor=MUDO, peso=700, alinha="center", serif=True))
    p.append(f'<line x1="1030" y1="150" x2="1634" y2="50" stroke="{FOSF}" stroke-width="6" stroke-linecap="round"/>')
    p.append(caixa(1000, 220, 664, 150, OXID, OXID_T, esp=4, rx=16))
    rs.append(rot(1020, 252, "“Está fechando a conta com comida?”", w=624, tam=32, cor=OXID, peso=700, alinha="center", serif=True, lh=1.2))
    return slide("whey", 400, p, rs,
                 eyebrow="O suplemento de proteína", titulo="Whey é comida em pó")


def carga_45():
    """4.5: cada barreira do idoso ligada à comida que resolve."""
    p = [svg_abre(1664, 400, "Três barreiras do idoso, cada uma ligada ao que resolve. Apetite menor e saciedade precoce: ovos, leite, iogurte e queijo, que cabem em pouco volume. Mastigação e prótese: carne moída ou desfiada, e peixe. Custo da carne e morar sozinho: leguminosas bem cozidas, e ovos"), defs(MUDO)]
    pares = [("t:mood-empty", "apetite menor, saciedade precoce", "ovos, leite, iogurte, queijo"),
             ("t:mood-confuzed", "mastigação e prótese", "carne moída ou desfiada, peixe"),
             ("t:home", "custo da carne, morar sozinho", "leguminosas bem cozidas, ovos")]
    rs = [rot(0, 0, "Barreiras", w=700, tam=26, cor=GLIC, peso=700, serif=True), rot(964, 0, "O que resolve", w=700, tam=26, cor=OXID, peso=700, serif=True)]
    for k, (ic, b, s_) in enumerate(pares):
        y = 50 + k * 116
        p.append(caixa(0, y, 700, 96, GLIC, GLIC_T, esp=3, rx=14))
        p.append(icone(ic, 20, y + 22, 52, GLIC))
        rs.append(rot(90, y + 30, b, w=590, tam=24, cor=TINTA))
        p.append(seta(708, y + 48, 956, y + 48, MUDO, "m0", esp=4))
        p.append(caixa(964, y, 700, 96, OXID, OXID_T, esp=3, rx=14))
        rs.append(rot(990, y + 30, s_, w=650, tam=24, cor=OXID, peso=700))
    return slide("carga", 400, p, rs,
                 eyebrow="Carga primeiro, proteína junto", titulo="O problema do idoso é textura e logística",
                 destaque="Rim: com função normal, sem sinal de dano nestas faixas. Com doença renal, a decisão é médica, e quem descarta é o exame.",
                 destaque_cor="tinta")


def perfis_45():
    """4.5: três pessoas na régua de g/kg, do número de hoje ao da conduta."""
    p = [svg_abre(1664, 420, "Três linhas sobre a mesma régua de proteína, de zero a quatro gramas por quilo. A vegetariana de 58 quilos está em 1,5 com 87 gramas por dia, mas com 8 gramas no café da manhã: o problema é a distribuição, e a conduta é quatro refeições de 20 a 25 gramas, com o total um pouco maior. O idoso de 65 quilos que começou a treinar está em 0,9, com 58 gramas: total baixo, e a conduta é 26 gramas três vezes ao dia, com textura. O jovem de 80 quilos está em 3,5, com 280 gramas: total alto, e a conduta é cerca de 2 gramas por quilo, com espaço para o carboidrato"), defs(OXID)]
    X0, X1 = 520, 1100
    X = lambda v: X0 + v / 4 * (X1 - X0)
    perf = [("Vegetariana, 58 kg", "87 g/dia; 8 g no café", 1.5, 1.6, "distribuição", "4 × 20 a 25 g, total um pouco maior", GLIC),
            ("Idoso, 65 kg, começou a treinar", "58 g/dia", 0.9, 1.2, "total baixo", "26 g × 3, com textura", FOSF),
            ("Jovem, 80 kg", "280 g/dia", 3.5, 2.0, "total alto", "≈ 2 g/kg e espaço ao carboidrato", AZUL)]
    rs = [rot(X0, 0, "g por kg por dia", w=X1 - X0, tam=20, cor=MUDO, alinha="center")]
    for v in range(5):
        rs.append(rot(X(v) - 20, 392, str(v), w=40, tam=18, cor=MUDO, alinha="center"))
        p.append(f'<line x1="{X(v):.0f}" y1="40" x2="{X(v):.0f}" y2="384" stroke="{GRADE}" stroke-width="1"/>')
    p.append(f'<rect x="{X(1.6):.0f}" y="40" width="{X(2.2) - X(1.6):.0f}" height="344" fill="{OXID_T}"/>')
    for k, (t, d, hoje, alvo, prob, cond, cor) in enumerate(perf):
        y = 56 + k * 112
        rs += [rot(0, y + 4, t, w=500, tam=24, cor=TINTA, peso=700), rot(0, y + 40, d, w=500, tam=20, cor=MUDO)]
        p.append(f'<line x1="{X0}" y1="{y + 34}" x2="{X1}" y2="{y + 34}" stroke="{CINZA}" stroke-width="3"/>')
        if abs(hoje - alvo) > 0.15:
            p.append(f'<path d="M {X(hoje):.0f} {y + 34} L {X(alvo) + (10 if alvo < hoje else -10):.0f} {y + 34}" stroke="{OXID}" stroke-width="4" marker-end="url(#m0)"/>')
        p.append(f'<circle cx="{X(hoje):.0f}" cy="{y + 34}" r="15" fill="{cor}" stroke="{CARTAO}" stroke-width="3"/>')
        rs.append(rot(X(hoje) - 50, y - 4, f"{hoje:.1f}".replace(".", ","), w=100, tam=20, cor=cor, peso=700, alinha="center"))
        p.append(caixa(1150, y, 514, 88, cor, CARTAO, esp=3, rx=12))
        rs += [rot(1170, y + 8, prob, w=480, tam=22, cor=cor, peso=700), rot(1170, y + 44, cond, w=480, tam=20, cor=TINTA)]
    return slide("perfis", 420, p, rs,
                 eyebrow="As três perguntas aplicadas", titulo="O mesmo número, três condutas",
                 destaque="No primeiro, o total estava certo e a distribuição errada. No segundo, o total baixo. No terceiro, alto demais para o objetivo.",
                 destaque_cor="petr")


# ---------------------------------------------------------------- 4.6

def erro_46():
    """4.6: reabilitada no discurso, cortada no prato."""
    p = [svg_abre(1664, 400, "À esquerda, um balão de fala com azeite, castanha e ovo aprovados: a gordura foi reabilitada no discurso. À direita, um prato em que a fatia de gordura está tracejada e recortada: no prato, ela continua sendo o primeiro macronutriente cortado por quem decide se cuidar. Embaixo, a lembrança de que ela tem um piso")]
    p.append(f'<path d="M 40 20 h 640 a 30 30 0 0 1 30 30 v 200 a 30 30 0 0 1 -30 30 h -480 l -60 50 l 10 -50 h -110 a 30 30 0 0 1 -30 -30 v -200 a 30 30 0 0 1 30 -30 z" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    rs = [rot(40, 40, "No discurso: reabilitada", w=670, tam=30, cor=OXID, peso=700, alinha="center", serif=True)]
    for k, t in enumerate(["azeite", "castanha", "ovo"]):
        x = 90 + k * 200
        p.append(icone("t:thumb-up", x + 40, 110, 56, OXID))
        rs.append(rot(x, 180, t, w=140, tam=24, cor=TINTA, alinha="center"))
    import math
    cx, cy, r = 1200, 205, 140
    P = lambda a, dx=0, dy=0: f"{cx + dx + r * math.cos(math.radians(a)):.0f} {cy + dy + r * math.sin(math.radians(a)):.0f}"
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 28}" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<path d="M {cx} {cy} L {P(-30)} A {r} {r} 0 1 1 {P(-90)} Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    p.append(f'<path d="M {cx + 40} {cy - 30} L {P(-90, 40, -30)} A {r} {r} 0 0 1 {P(-30, 40, -30)} Z" fill="none" stroke="{GLIC}" stroke-width="4" stroke-dasharray="12 8"/>')
    rs += [rot(cx + 180, 20, "gordura, recortada", w=200, tam=24, cor=GLIC, peso=700, lh=1.2),
           rot(cx - 120, cy + 30, "no prato: o primeiro corte", w=240, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2)]
    return slide("erro", 400, p, rs,
                 eyebrow="O erro desta aula", titulo="Cortar gordura é comer melhor?",
                 destaque="E ela tem um piso.", destaque_cor="verm")


def rotas():
    """4.6: três rotas que chegam ao mesmo piso, uma delas saindo do consultório."""
    p = [svg_abre(1664, 420, "Três rotas que descem até o mesmo lugar, abaixo do piso de gordura. Estética: meses com cerca de 15% da energia em gordura para secar, e libido, humor, sono e testosterona caem. Pureza alimentar: comida limpa, sem óleo nem castanha, sem dieta mas sem densidade, e o ciclo fica irregular. Orientação incompleta: reduza a gordura, sai azeite, castanha e ovo e fica o biscoito recheado; esta saiu de dentro de um consultório"), defs(GLIC, FOSF)]
    rotas_ = [(0, "t:barbell", "Estética", "meses com ~15% da energia em gordura para “secar”; libido, humor, sono e testosterona caem", GLIC, "m0"),
              (572, "t:salad", "Pureza alimentar", "“comida limpa”, sem óleo nem castanha; sem dieta, mas sem densidade; o ciclo fica irregular", GLIC, "m0"),
              (1144, "t:stethoscope", "Orientação incompleta", "“reduza a gordura”: sai azeite, castanha e ovo; fica o biscoito recheado", FOSF, "m1")]
    rs = []
    for x, ic, t, d, cor, mk in rotas_:
        p.append(caixa(x, 0, 520, 230, cor, CARTAO, esp=3, rx=16))
        p.append(icone(ic, x + 20, 20, 50, cor))
        rs += [rot(x + 84, 28, t, w=420, tam=26, cor=cor, peso=700, serif=True), rot(x + 20, 90, d, w=480, tam=21, cor=TINTA, lh=1.25)]
        p.append(f'<path d="M {x + 260} 236 C {x + 260} 300, 832 280, 832 320" fill="none" stroke="{cor}" stroke-width="4" marker-end="url(#{mk})"/>')
    p.append(caixa(482, 330, 700, 80, FOSF, FOSF_T, esp=3, rx=14))
    rs += [rot(482, 352, "abaixo do piso", w=700, tam=30, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(1190, 360, "esta saiu de um consultório", w=470, tam=20, cor=FOSF, peso=700)]
    return slide("rotas", 420, p, rs,
                 eyebrow="Três rotas até o piso", titulo="Não é um perfil de paciente. É uma cultura",
                 destaque="Uma das três rotas saiu de dentro de um consultório.", destaque_cor="tinta")


def funcoes():
    """4.6: cinco funções da gordura em cinco colunas, sem substituto."""
    p = [svg_abre(1664, 420, "Cinco colunas, cinco funções que só a gordura faz: ácidos graxos essenciais, linoleico e alfa-linolênico, e não existe carboidrato essencial; vitaminas A, D, E e K, porque a salada sem azeite entrega menos; membranas e combustível, o substrato dominante no esforço leve e longo; colesterol e esteroides, uma relação que existe mas não é uma torneira; saciedade e adesão, porque dieta pobre em gordura é mais difícil de manter")]
    fun = [("t:key", "Ácidos graxos essenciais", "linoleico e alfa-linolênico; não existe carboidrato essencial", OXID),
           ("t:salad", "Vitaminas A, D, E e K", "a salada sem azeite entrega menos", OXID),
           ("t:battery-4", "Membranas e combustível", "o substrato dominante no esforço leve e longo", OXID),
           ("t:adjustments-horizontal", "Colesterol e esteroides", "a relação existe, mas não é uma torneira", GLIC),
           ("t:mood-smile", "Saciedade e adesão", "dieta pobre em gordura é mais difícil de manter", TINTA)]
    rs = []
    W = 304
    for k, (ic, t, d, cor) in enumerate(fun):
        x = k * (W + 36)
        p.append(caixa(x, 0, W, 420, cor, OXID_T if cor == OXID else (GLIC_T if cor == GLIC else PAPEL), esp=3, rx=16))
        p.append(f'<circle cx="{x + W / 2:.0f}" cy="80" r="50" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        p.append(icone(ic, x + W / 2 - 30, 50, 60, cor))
        rs += [rot(x + 14, 150, t, w=W - 28, tam=24, cor=cor, peso=700, alinha="center", lh=1.15),
               rot(x + 14, 240, d, w=W - 28, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    return slide("funcoes", 420, p, rs, eyebrow="O que só a gordura faz", titulo="Cinco funções que não têm substituto")


def hormonio():
    """4.6: o que a meta-análise mostrou, em pontos de efeito, e as ressalvas."""
    p = [svg_abre(1664, 420, "À esquerda, pontos esquemáticos de efeito da dieta baixa em gordura em 206 homens: testosterona total e livre mais baixas, efeito pequeno a moderado; LH e SHBG sem diferença, sobre a linha do zero. À direita, as ressalvas: estudos pequenos e antigos; fibra, tipo de gordura e calorias mudando junto; errata publicada depois")]
    p.append(caixa(0, 0, 900, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 14, "O que a meta-análise mostrou", w=850, tam=26, cor=OXID, peso=700, serif=True),
          rot(24, 52, "206 homens, estudos de intervenção, dieta baixa em gordura", w=850, tam=20, cor=MUDO)]
    Z = 640
    p.append(f'<line x1="{Z}" y1="100" x2="{Z}" y2="360" stroke="{TINTA}" stroke-width="2"/>')
    efe = [("testosterona total", -0.45, FOSF), ("testosterona livre", -0.55, FOSF), ("LH", 0, MUDO), ("SHBG", 0, MUDO)]
    for k, (t, e, cor) in enumerate(efe):
        y = 120 + k * 60
        rs.append(rot(24, y - 4, t, w=330, tam=22, cor=TINTA, peso=600, alinha="right"))
        x = Z + e * 400
        p.append(f'<line x1="{x - 60:.0f}" y1="{y + 10}" x2="{x + 60:.0f}" y2="{y + 10}" stroke="{cor}" stroke-width="4"/>')
        p.append(f'<rect x="{x - 12:.0f}" y="{y - 2}" width="24" height="24" fill="{cor}"/>')
    rs += [rot(Z - 380, 370, "mais baixa", w=300, tam=20, cor=FOSF, alinha="center"),
           rot(Z - 60, 370, "sem diferença", w=200, tam=20, cor=MUDO, alinha="center"),
           rot(Z + 90, 160, "efeito pequeno a moderado", w=220, tam=20, cor=FOSF, peso=700, lh=1.2)]
    p.append(caixa(964, 0, 700, 420, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(988, 14, "As ressalvas", w=650, tam=26, cor=GLIC, peso=700, serif=True))
    res = [("t:hourglass", "estudos pequenos e antigos"), ("t:arrows-exchange", "fibra, tipo de gordura e calorias mudando junto"), ("t:pencil", "errata publicada depois")]
    for k, (ic, t) in enumerate(res):
        y = 90 + k * 100
        p.append(icone(ic, 988, y, 44, GLIC))
        rs.append(rot(1048, y + 4, t, w=590, tam=23, cor=TINTA, lh=1.25))
    return slide("hormonio", 420, p, rs,
                 eyebrow="O erro espelhado · uma meta-análise de 2021", titulo="Gordura como nutriente dos hormônios?",
                 destaque="Não se sustenta: mais gordura elevando testosterona acima do normal, gordura saturada “anabólica”, dieta como reposição hormonal.",
                 destaque_cor="verm", fonte="Pontos: esquema · Whittaker e Wu, Journal of Steroid Biochemistry and Molecular Biology 2021")


def densidade():
    """4.6: três porções pequenas que valem muito, em barras de energia."""
    p = [svg_abre(1664, 400, "Três porções pequenas e a energia de cada uma em barras: uma colher de sopa de azeite, cerca de 120 quilocalorias; um punhado de castanhas, cerca de 200; duas colheres de pasta de amendoim, cerca de 200. Para quem não consegue comer volume, a comida não precisa ser maior: precisa valer mais")]
    itens = [("uma colher de sopa de azeite", 120, "t:droplet"), ("um punhado de castanhas", 200, "t:seedling"), ("duas colheres de pasta de amendoim", 200, "t:cookie")]
    rs = []
    for k, (t, v, ic) in enumerate(itens):
        y = 20 + k * 120
        p.append(f'<circle cx="60" cy="{y + 46}" r="44" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
        p.append(icone(ic, 34, y + 20, 52, OXID))
        rs.append(rot(130, y + 30, t, w=440, tam=24, cor=TINTA, peso=600))
        p.append(f'<rect x="600" y="{y + 16}" width="{v * 4.2:.0f}" height="60" rx="8" fill="{OXID}"/>')
        rs.append(rot(600 + v * 4.2 + 20, y + 26, f"≈ {v} kcal", w=240, tam=34, cor=OXID, peso=700, serif=True))
    p.append(f'<line x1="600" y1="10" x2="600" y2="380" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(600, 380 - 0, "", w=10, tam=18)); rs.pop()
    return slide("densidade", 400, p, rs,
                 eyebrow="A virada prática", titulo="Gordura como ferramenta de densidade",
                 destaque="Para quem não consegue comer volume, a comida não precisa ser maior. Precisa valer mais. Não é efeito endócrino: é densidade.",
                 destaque_cor="tinta")


def frase_46():
    """4.6: a frase incompleta e o que ela tira do prato, contra a frase completa."""
    p = [svg_abre(1664, 400, "À esquerda, a frase incompleta, reduza a gordura: saem azeite, castanha e ovo, riscados, e ficam biscoito e pão doce; o colesterol quase não muda. À direita, a frase completa: reduza a gordura dos industrializados, mantenha azeite, castanha, ovo e peixe, e não fique abaixo do piso")]
    p.append(caixa(0, 0, 800, 400, FOSF, FOSF_T, esp=3, rx=16))
    rs = [rot(24, 14, "“Reduza a gordura”", w=760, tam=30, cor=FOSF, peso=700, serif=True)]
    rs.append(rot(24, 74, "sai o que parece gorduroso", w=360, tam=20, cor=MUDO))
    for k, t in enumerate(["azeite", "castanha", "ovo"]):
        y = 110 + k * 60
        rs.append(rot(24, y, t, w=300, tam=24, cor=TINTA))
        p.append(f'<line x1="20" y1="{y + 16}" x2="{30 + len(t) * 14}" y2="{y + 16}" stroke="{FOSF}" stroke-width="4"/>')
    rs.append(rot(420, 74, "fica o que não parece", w=360, tam=20, cor=MUDO))
    for k, t in enumerate(["biscoito recheado", "pão doce"]):
        rs.append(rot(420, 110 + k * 60, t, w=360, tam=24, cor=FOSF, peso=700))
    rs.append(rot(24, 320, "e o colesterol quase não muda", w=760, tam=24, cor=FOSF, peso=700))
    p.append(caixa(864, 0, 800, 400, OXID, OXID_T, esp=3, rx=16))
    rs.append(rot(888, 14, "A frase completa", w=760, tam=30, cor=OXID, peso=700, serif=True))
    comp = [("t:x", "reduza a gordura dos industrializados", FOSF), ("t:check", "mantenha azeite, castanha, ovo e peixe", OXID), ("t:stairs", "não fique abaixo do piso", OXID)]
    for k, (ic, t, cor) in enumerate(comp):
        y = 90 + k * 96
        p.append(icone(ic, 888, y, 44, cor))
        rs.append(rot(948, y + 6, t, w=690, tam=25, cor=TINTA, peso=600))
    return slide("frase", 400, p, rs,
                 eyebrow="A correção: número, momento, qualidade e a frase", titulo="Orientação incompleta produz o oposto",
                 destaque="Momento: menos gordura perto do treino, não fora do dia. Saturada: o alvo não é zero. Trans industrial: eliminar. Ômega-3: peixe duas vezes por semana antes do suplemento.",
                 destaque_cor="tinta")



# ---------------------------------------------------------------- 4.7

def pedidos():
    """4.7: o adulto que pede o painel e a adolescente que ninguém pensou em examinar."""
    p = [svg_abre(1664, 400, "Dois pedidos lado a lado. À esquerda, o adulto que quer dosar trinta micronutrientes, toma multivitamínico por conta própria e come bem, sem excluir nada: risco de deficiência baixo. À direita, a adolescente cansada, que nada dois períodos por dia, está em crescimento, não come carne vermelha e evita leite: risco alto")]
    lados = [(0, "h:man", "O adulto do painel", GLIC, GLIC_T,
              [("t:clipboard-list", "quer dosar trinta micronutrientes"), ("t:pill", "multivitamínico por conta própria"), ("t:salad", "come bem, não exclui nada")], 0.15, "baixo", OXID),
             (864, "h:girl-1015y", "A adolescente cansada", FOSF, FOSF_T,
              [("t:swimming", "nada dois períodos por dia, em crescimento"), ("t:x", "não come carne vermelha"), ("t:x", "evita leite “porque incha”")], 0.85, "alto", FOSF)]
    rs = []
    for x, ic, t, cor, fundo, itens, frac, nivel, cr in lados:
        p.append(caixa(x, 0, 800, 400, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, x + 24, 18, 52, cor))
        rs.append(rot(x + 90, 26, t, w=680, tam=30, cor=cor, peso=700, serif=True))
        for k, (ii, tt) in enumerate(itens):
            y = 100 + k * 62
            p.append(icone(ii, x + 30, y, 38, cor if ii == "t:x" else MUDO))
            rs.append(rot(x + 84, y + 4, tt, w=690, tam=24, cor=TINTA))
        p.append(f'<rect x="{x + 30}" y="350" width="740" height="18" rx="9" fill="{CINZA}"/>')
        p.append(f'<rect x="{x + 30}" y="350" width="{740 * frac:.0f}" height="18" rx="9" fill="{cr}"/>')
        rs.append(rot(x + 30, 306, f"risco de deficiência: {nivel}", w=740, tam=22, cor=cr, peso=700))
    return slide("pedidos", 400, p, rs,
                 eyebrow="Dois pedidos típicos", titulo="Um painel sem risco, um risco sem painel",
                 destaque="O posicionamento de 2016: o risco está em quem restringe energia, perde peso de forma agressiva ou exclui grupos de alimentos.",
                 destaque_cor="petr", fonte="Thomas, Erdman e Burke · Medicine and Science in Sports and Exercise 2016")


def quem():
    """4.7: matriz de grupos por nutriente, com as linhas que a adolescente cruza."""
    grupos = [("Mulher que menstrua", "●    ", True), ("Adolescente em crescimento", "●●   ", True),
              ("Atleta de resistência", "●    ", True), ("Restrição de energia ou corte", "●●●  ", False),
              ("Exclusão de grupos (vegano)", "●●●●●", True), ("Doador de sangue frequente", "●    ", False)]
    nutr = [("Ferro", FOSF), ("Cálcio", AZUL), ("Vit. D", GLIC), ("B12", OXID), ("Iodo", TINTA)]
    p = [svg_abre(1664, 400, "Uma matriz: seis grupos nas linhas e cinco nutrientes nas colunas. Ferro aparece em todos os grupos. Cálcio no adolescente, na restrição de energia e na exclusão de grupos. Vitamina D na restrição e na exclusão. B12 e iodo só na exclusão de grupos, como o vegano. Na última coluna, as quatro linhas que a adolescente cansada cruza: mulher que menstrua, adolescente em crescimento, atleta de resistência e exclusão de grupos")]
    rs = []
    X = lambda j: 690 + j * 140
    for j, (n, cor) in enumerate(nutr):
        rs.append(rot(X(j) - 70, 4, n, w=140, tam=24, cor=cor, peso=700, alinha="center"))
    rs.append(rot(1400, 4, "a adolescente", w=264, tam=24, cor=FOSF, peso=700, alinha="center"))
    for i, (g, marc, ela) in enumerate(grupos):
        y = 80 + i * 54
        if i % 2 == 0:
            p.append(f'<rect x="0" y="{y - 26}" width="1664" height="54" rx="8" fill="{PAPEL}"/>')
        rs.append(rot(10, y - 14, g, w=600, tam=24, cor=TINTA))
        for j, c in enumerate(marc):
            if c == "●":
                p.append(f'<circle cx="{X(j)}" cy="{y}" r="15" fill="{nutr[j][1]}"/>')
            else:
                p.append(f'<circle cx="{X(j)}" cy="{y}" r="5" fill="{CINZA}"/>')
        if ela:
            p.append(icone("t:check", 1508, y - 20, 40, FOSF))
    p.append(f'<line x1="1390" y1="0" x2="1390" y2="400" stroke="{BORDA}" stroke-width="3"/>')
    return slide("quem", 400, p, rs,
                 eyebrow="Passo um · quem é", titulo="Onde as deficiências se concentram",
                 destaque="A adolescente cruza quase todas as linhas. O adulto do painel não cruza nenhuma.",
                 destaque_cor="petr", fonte="Pontos de atenção principais por grupo, conforme a aula")


def vegano():
    """4.7: o que muda na lista de quem não come nada de origem animal."""
    p = [svg_abre(1664, 400, "Três blocos. B12: não há fonte vegetal confiável, e o suplemento é parte da dieta. Seis pontos de atenção: ferro, zinco, cálcio, iodo, vitamina D e ômega-3 de cadeia longa. O iodo no Brasil: o sal comum é iodado, alguns sais gourmet não são, então vale ler o rótulo")]
    p.append(caixa(0, 0, 440, 400, FOSF, FOSF_T, esp=3, rx=16))
    p.append(icone("t:pill", 170, 40, 100, FOSF))
    rs = [rot(0, 160, "B12", w=440, tam=56, cor=FOSF, peso=700, alinha="center", serif=True),
          rot(30, 250, "não há fonte vegetal confiável: suplementar é parte da dieta", w=380, tam=24, cor=TINTA, alinha="center", lh=1.3)]
    p.append(caixa(480, 0, 640, 400, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(504, 18, "Pontos de atenção", w=600, tam=30, cor=GLIC, peso=700, serif=True))
    for k, t in enumerate(["ferro", "zinco", "cálcio", "iodo", "vitamina D", "ômega-3 de cadeia longa"]):
        y = 84 + k * 50
        p.append(f'<circle cx="524" cy="{y + 14}" r="8" fill="{GLIC}"/>')
        rs.append(rot(548, y, t, w=560, tam=25, cor=TINTA))
    p.append(caixa(1160, 0, 504, 400, TINTA, CARTAO, esp=3, rx=16))
    rs.append(rot(1184, 18, "A nota brasileira do iodo", w=460, tam=28, cor=TINTA, peso=700, serif=True))
    for k, (t, ok, cor) in enumerate([("sal comum", "iodado", OXID), ("alguns sais “gourmet”", "nem sempre", FOSF)]):
        y = 90 + k * 110
        p.append(icone("t:check" if k == 0 else "t:x", 1184, y + 8, 44, cor))
        rs += [rot(1244, y, t, w=400, tam=25, cor=TINTA, peso=600), rot(1244, y + 38, ok, w=400, tam=23, cor=cor, peso=700)]
    p.append(icone("t:zoom-question", 1184, 318, 44, TINTA))
    rs.append(rot(1244, 326, "leia o rótulo", w=400, tam=25, cor=TINTA, peso=700))
    return slide("vegano", 400, p, rs,
                 eyebrow="Uma revisão de 2017", titulo="O vegano muda a lista",
                 destaque="Uma dieta vegana bem planejada atende a maior parte dos atletas, com manejo de alimentos e suplementação adequada.",
                 destaque_cor="petr", fonte="Rogerson · Journal of the International Society of Sports Nutrition 2017")


def come():
    """4.7: quatro perguntas em sequência, e a primeira pode encerrar a conversa."""
    p = [svg_abre(1664, 400, "Quatro perguntas em sequência. Primeira: come energia suficiente? Se não, esse é o problema principal, e a conversa muda. Segunda: o que foi excluído, e por quê? Ética é uma coisa, medo é outra conversa. Terceira: de onde vem o ferro, heme ou não heme, e o que vem junto. Quarta: de onde vem o cálcio, e qual é a rota de quem cortou laticínio"), defs(MUDO, FOSF)]
    qs = [("Come energia suficiente?", FOSF, FOSF_T), ("O que foi excluído, e por quê?", GLIC, GLIC_T),
          ("De onde vem o ferro?", OXID, OXID_T), ("De onde vem o cálcio?", OXID, OXID_T)]
    sub = ["", "ética é uma coisa; medo é outra conversa", "heme ou não heme, e o que vem junto", "e qual é a rota de quem cortou laticínio"]
    rs = []
    for k, (t, cor, fundo) in enumerate(qs):
        x = k * 428
        p.append(caixa(x, 0, 380, 256, cor, fundo, esp=3, rx=16))
        p.append(f'<circle cx="{x + 44}" cy="44" r="24" fill="{cor}"/>')
        rs += [rot(x + 20, 30, str(k + 1), w=48, tam=26, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 24, 86, t, w=340, tam=28, cor=cor, peso=700, serif=True, lh=1.15)]
        if sub[k]:
            rs.append(rot(x + 24, 180, sub[k], w=340, tam=21, cor=TINTA, lh=1.25))
        if k < 3:
            p.append(seta(x + 384, 115, x + 422, 115, MUDO, "m0", esp=4))
    p.append(seta(190, 262, 190, 304, FOSF, "m1", esp=4))
    rs.append(rot(214, 270, "não", w=80, tam=22, cor=FOSF, peso=700))
    p.append(caixa(0, 310, 760, 70, FOSF, FOSF, esp=0, rx=14))
    rs.append(rot(24, 330, "esse é o problema principal", w=720, tam=27, cor=PAPEL, peso=700))
    return slide("come", 380, p, rs,
                 eyebrow="Passo dois · o que come", titulo="Quatro perguntas sobre o padrão")


def prato():
    """4.7: ferro e cálcio no prato, com o que ajuda e o que atrapalha."""
    p = [svg_abre(1664, 400, "À esquerda, o ferro: o heme das carnes é bem absorvido, o não heme de feijão, folhas e fortificados bem menos; vitamina C junto aumenta, café, chá e cálcio junto reduzem, e convém afastar uma hora. Barras em esquema. À direita, o cálcio: cerca de 1.000 miligramas por dia no adulto, mais no adolescente; um copo de leite ou iogurte dá perto de 300, então três copos chegam perto da meta; sem laticínio, bebida fortificada, tofu, sardinha e folhas"), defs(OXID, FOSF)]
    p.append(caixa(0, 0, 800, 400, FOSF, CARTAO, esp=3, rx=16))
    rs = [rot(24, 16, "Ferro", w=400, tam=32, cor=FOSF, peso=700, serif=True),
          rot(560, 24, "absorção: esquema", w=220, tam=18, cor=MUDO, alinha="right")]
    for k, (t, d, frac) in enumerate([("heme", "carnes", 0.8), ("não heme", "feijão, folhas, fortificados", 0.3)]):
        y = 90 + k * 84
        rs += [rot(24, y, t, w=170, tam=25, cor=TINTA, peso=700), rot(24, y + 34, d, w=300, tam=19, cor=MUDO)]
        p.append(f'<rect x="330" y="{y}" width="440" height="30" rx="6" fill="{CINZA}"/>')
        p.append(f'<rect x="330" y="{y}" width="{440 * frac:.0f}" height="30" rx="6" fill="{FOSF}"/>')
    p.append(f'<line x1="24" y1="270" x2="776" y2="270" stroke="{BORDA}" stroke-width="2"/>')
    p.append(icone("t:trending-up", 24, 290, 40, OXID))
    rs.append(rot(78, 296, "vitamina C junto aumenta", w=700, tam=24, cor=TINTA))
    p.append(icone("t:coffee", 24, 344, 40, FOSF))
    rs.append(rot(78, 340, "café, chá e cálcio junto reduzem: afastar uma hora", w=700, tam=24, cor=TINTA, lh=1.2))
    p.append(caixa(864, 0, 800, 400, AZUL, CARTAO, esp=3, rx=16))
    rs += [rot(888, 16, "Cálcio", w=400, tam=32, cor=AZUL, peso=700, serif=True),
           rot(888, 76, "cerca de 1.000 mg por dia no adulto; mais no adolescente", w=760, tam=22, cor=TINTA)]
    K = 0.7
    for k in range(3):
        p.append(f'<rect x="{888 + k * 300 * K + 3:.0f}" y="130" width="{300 * K - 6:.0f}" height="56" rx="8" fill="{AZUL}"/>')
        rs.append(rot(888 + k * 300 * K, 144, "copo ≈ 300", w=300 * K, tam=20, cor=PAPEL, peso=700, alinha="center"))
    p.append(f'<rect x="{888 + 900 * K + 3:.0f}" y="130" width="{100 * K - 6:.0f}" height="56" rx="8" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="2"/>')
    p.append(f'<line x1="{888 + 1000 * K:.0f}" y1="116" x2="{888 + 1000 * K:.0f}" y2="200" stroke="{TINTA}" stroke-width="3"/>')
    rs += [rot(888 + 1000 * K - 40, 204, "1.000 mg", w=120, tam=20, cor=TINTA, peso=700),
           rot(888, 204, "leite ou iogurte", w=400, tam=20, cor=MUDO)]
    p.append(f'<line x1="888" y1="262" x2="1640" y2="262" stroke="{BORDA}" stroke-width="2"/>')
    rs += [rot(888, 280, "Sem laticínio", w=760, tam=24, cor=AZUL, peso=700),
           rot(888, 320, "bebida fortificada, tofu, sardinha, folhas", w=760, tam=24, cor=TINTA)]
    return slide("prato", 400, p, rs,
                 eyebrow="Onde a comida mais resolve", titulo="Ferro e cálcio no prato",
                 destaque="Multivitamínico comum: não corrige ferro, não repõe vitamina D baixa, tem pouco cálcio. Resposta genérica para uma pergunta específica.",
                 destaque_cor="ambar")


def sente():
    """4.7: os sintomas vagos espalham para muitas causas; poucas pistas apontam."""
    p = [svg_abre(1664, 400, "À esquerda, cansaço, queda de desempenho e infecções se espalham para quatro causas possíveis: sono ruim, treino excessivo, déficit de energia e deficiência de um nutriente. À direita, as pistas que apontam: para ferro, fluxo intenso, falta de ar desproporcional, palidez e vontade de mastigar gelo; para B12, formigamento, memória e humor, em vegano sem suplemento ou com remédios que reduzem a absorção; para cálcio e vitamina D, fratura por estresse repetida, e antes disso a pergunta sobre energia"), defs(MUDO)]
    p.append(caixa(0, 110, 260, 180, MUDO, PAPEL, esp=3, rx=14))
    rs = [rot(0, 136 + k * 40, t, w=260, tam=22, cor=TINTA, peso=700, alinha="center") for k, t in enumerate(["cansaço", "queda de desempenho", "infecções"])]
    causas = ["sono ruim", "treino excessivo", "déficit de energia", "deficiência"]
    for k, c in enumerate(causas):
        y = 20 + k * 96
        p.append(seta(266, 200, 330, y + 30, MUDO, "m0", esp=3))
        p.append(caixa(340, y, 220, 60, MUDO, CARTAO, esp=2, rx=10))
        rs.append(rot(340, y + 16, c, w=220, tam=21, cor=TINTA, alinha="center"))
    pistas = [("Ferro", FOSF, FOSF_T, "fluxo intenso, falta de ar desproporcional, palidez, vontade de mastigar gelo"),
              ("B12", GLIC, GLIC_T, "formigamento, memória e humor, em vegano sem suplemento ou com remédios que reduzem a absorção"),
              ("Cálcio e vitamina D", AZUL, AZUL_T, "fratura por estresse repetida; e antes: falta energia?")]
    rs.append(rot(620, 0, "As pistas que apontam", w=1000, tam=24, cor=MUDO, peso=700))
    for k, (t, cor, fundo, x) in enumerate(pistas):
        y = 44 + k * 120
        p.append(caixa(620, y, 1044, 104, cor, fundo, esp=3, rx=14))
        rs += [rot(644, y + 14, t, w=1000, tam=25, cor=cor, peso=700, serif=True),
               rot(644, y + 52, x, w=1000, tam=21, cor=TINTA, lh=1.25)]
    return slide("sente", 400, p, rs,
                 eyebrow="Passo três · o que sente", titulo="O sintoma não aponta o nutriente",
                 destaque="Cansaço, queda de desempenho e infecções são os mesmos de sono ruim, treino excessivo e déficit. O passo três decide a urgência, não o diagnóstico.",
                 destaque_cor="petr")


def turbina():
    """4.7: o tanque baixo enche até a linha; o tanque cheio não passa dela."""
    p = [svg_abre(1664, 380, "Dois tanques com a mesma linha de suficiência. No primeiro, o nível está baixo, e uma seta mostra que a deficiência se corrige até a linha. No segundo, o nível já está na linha, e a seta para cima está riscada: suficiência não se turbina. À direita, o que fica fora do procedimento: exame de cabelo, teste intracelular em pacote, painel sem pergunta clínica e soro de vitaminas na veia sem deficiência"), defs(OXID, FOSF)]
    rs = []
    for k, (nivel, t, cor) in enumerate([(0.3, "deficiência: se corrige", OXID), (0.65, "suficiência: não se turbina", FOSF)]):
        x = 40 + k * 380
        p.append(f'<rect x="{x}" y="40" width="200" height="260" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
        p.append(f'<rect x="{x + 4}" y="{296 - 252 * nivel:.0f}" width="192" height="{252 * nivel:.0f}" rx="10" fill="{AZUL_T}"/>')
        ylin = 296 - 252 * 0.65
        p.append(f'<line x1="{x - 16}" y1="{ylin:.0f}" x2="{x + 216}" y2="{ylin:.0f}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
        if k == 0:
            p.append(seta(x + 100, 260, x + 100, ylin + 14, OXID, "m0", esp=6))
        else:
            p.append(seta(x + 100, ylin - 10, x + 100, 60, FOSF, "m1", esp=6))
            p.append(f'<line x1="{x + 66}" y1="62" x2="{x + 134}" y2="104" stroke="{FOSF}" stroke-width="6"/>')
        rs.append(rot(x - 60, 320, t, w=320, tam=24, cor=cor, peso=700, alinha="center", lh=1.2))
    rs.append(rot(260, 108, "linha de suficiência", w=140, tam=18, cor=MUDO, alinha="center", lh=1.2))
    p.append(caixa(860, 0, 804, 380, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(884, 18, "Fora do procedimento", w=760, tam=30, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["exame de cabelo", "teste “intracelular” em pacote", "painel sem pergunta clínica", "soro de vitaminas na veia sem deficiência"]):
        y = 90 + k * 68
        p.append(icone("t:x", 884, y, 40, FOSF))
        rs.append(rot(940, y + 4, t, w=700, tam=25, cor=TINTA))
    return slide("turbina", 380, p, rs,
                 eyebrow="O que o procedimento não inclui", titulo="Deficiência se corrige. Suficiência não se turbina.",
                 destaque="Magnésio e zinco se perdem no suor, mas deficiência clínica em quem come bem é incomum.",
                 destaque_cor="tinta")


# ---------------------------------------------------------------- 4.8

def numero():
    """4.8: a maratonista que bebeu em todos os postos e a metade da regra que faltou."""
    p = [svg_abre(1664, 400, "Uma prova desenhada como uma estrada: largada, oito postos de água, todos usados, e a chegada depois de mais de cinco horas, confusa e mais pesada do que largou. Embaixo, as duas metades da regra: não perder mais de 2 por cento, que ela cumpriu, e não ganhar, a metade que teria protegido")]
    p.append(f'<line x1="60" y1="110" x2="1300" y2="110" stroke="{MUDO}" stroke-width="6" stroke-linecap="round"/>')
    p.append(icone("t:flag", 30, 30, 56, TINTA))
    rs = [rot(0, 136, "largada", w=120, tam=22, cor=TINTA, alinha="center")]
    for k in range(8):
        x = 190 + k * 130
        p.append(f'<circle cx="{x}" cy="110" r="26" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
        p.append(icone("t:droplet", x - 16, 94, 32, AZUL))
    rs.append(rot(190, 150, "bebe em todos os postos", w=930, tam=22, cor=AZUL, peso=700, alinha="center"))
    p.append(icone("t:clock", 1150, 20, 40, MUDO))
    rs.append(rot(1196, 28, "mais de 5 h", w=160, tam=22, cor=MUDO))
    p.append(caixa(1330, 40, 334, 150, FOSF, FOSF_T, esp=3, rx=14))
    p.append(icone("t:scale", 1350, 60, 48, FOSF))
    rs.append(rot(1410, 58, "chega confusa e mais pesada", w=240, tam=23, cor=FOSF, peso=700, lh=1.2))
    rs.append(rot(1350, 134, "primeira maratona", w=300, tam=20, cor=TINTA))
    metades = [(0, "t:check", "Não perder mais de 2%", "ela cumpriu", OXID, OXID_T),
               (864, "t:x", "E não ganhar", "a metade que teria protegido", FOSF, FOSF_T)]
    for x, ic, t, d, cor, fundo in metades:
        p.append(caixa(x, 240, 800, 150, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, x + 30, 270, 56, cor))
        rs += [rot(x + 110, 264, t, w=660, tam=32, cor=cor, peso=700, serif=True),
               rot(x + 110, 322, d, w=660, tam=24, cor=TINTA)]
    return slide("numero", 400, p, rs,
                 eyebrow="O posicionamento de 2007", titulo="Não perder mais de 2%. E não ganhar.",
                 destaque="Fez o que mandaram. A segunda metade da regra teria protegido.",
                 destaque_cor="verm", fonte="Sawka e colaboradores · Medicine and Science in Sports and Exercise 2007")


def variacao():
    """4.8: a faixa de suor entre pessoas e a conta da corredora lenta."""
    p = [svg_abre(1664, 400, "À esquerda, uma régua de taxa de suor de 0 a 2,5 litros por hora, com a faixa relatada em atletas de 0,5 a 2, um fator de quatro. Marcados nela: 0,6 litro por hora, o que a corredora perde, e 0,8, o que ela bebe. À direita, duas barras em 5 horas e 40: cerca de 3,4 litros perdidos e cerca de 4,5 bebidos, um quilo a mais na chegada. Conta ilustrativa")]
    X0, X1 = 20, 860
    X = lambda v: X0 + v / 2.5 * (X1 - X0)
    rs = []
    p.append(f'<rect x="{X(0.5):.0f}" y="120" width="{X(2) - X(0.5):.0f}" height="60" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<line x1="{X0}" y1="180" x2="{X1}" y2="180" stroke="{MUDO}" stroke-width="3"/>')
    for v in [0, 0.5, 1, 1.5, 2, 2.5]:
        p.append(f'<line x1="{X(v):.0f}" y1="180" x2="{X(v):.0f}" y2="192" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(v) - 40, 198, f"{v:g}".replace(".", ","), w=80, tam=20, cor=MUDO, alinha="center"))
    rs += [rot(X0, 236, "litros de suor por hora", w=840, tam=20, cor=MUDO, alinha="center"),
           rot(X(0.5), 128, "faixa relatada em atletas: fator de quatro", w=X(2) - X(0.5), tam=22, cor=OXID, peso=700, alinha="center")]
    for v, t, cor, y in [(0.6, "perde 0,6", GLIC, 290), (0.8, "bebe 0,8", FOSF, 340)]:
        p.append(f'<line x1="{X(v):.0f}" y1="182" x2="{X(v):.0f}" y2="{y + 10}" stroke="{cor}" stroke-width="3"/>')
        p.append(f'<circle cx="{X(v):.0f}" cy="180" r="10" fill="{cor}"/>')
        rs.append(rot(X(v) + 12, y - 4, t, w=200, tam=22, cor=cor, peso=700))
    B, K = 380, 70
    for k, (v, t, cor) in enumerate([(3.4, "≈ 3,4 L perdidos", GLIC), (4.5, "≈ 4,5 L bebidos", FOSF)]):
        x = 1040 + k * 260
        p.append(f'<rect x="{x}" y="{B - v * K:.0f}" width="180" height="{v * K:.0f}" rx="8" fill="{cor}"/>')
        rs.append(rot(x - 30, B - v * K - 36, t, w=240, tam=22, cor=cor, peso=700, alinha="center"))
    p.append(f'<line x1="1000" y1="{B}" x2="1520" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="1220" y1="{B - 3.4 * K:.0f}" x2="1300" y2="{B - 3.4 * K:.0f}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    p.append(f'<path d="M 1500 {B - 4.5 * K:.0f} h 20 v {1.1 * K:.0f} h -20" fill="none" stroke="{FOSF}" stroke-width="3"/>')
    rs += [rot(1530, B - 4.2 * K, "+ 1 kg na chegada", w=134, tam=22, cor=FOSF, peso=700, lh=1.2),
           rot(1040, 0, "em 5 h 40", w=440, tam=22, cor=TINTA, peso=700, alinha="center")]
    return slide("variacao", 400, p, rs,
                 eyebrow="Uma revisão de 2017", titulo="Um fator de quatro entre pessoas",
                 destaque="Conta ilustrativa, não dado medido. Sua pouco, corre devagar, passa muito tempo na prova: a regra de quem sua muito vira excesso.",
                 destaque_cor="tinta", fonte="Baker · Sports Medicine 2017")


def regras():
    """4.8: três regras de uso da taxa de suor, cada uma num quadro."""
    p = [svg_abre(1664, 380, "Três quadros. Primeiro: a taxa vale para aquela condição; verão e inverno dão números diferentes, então se mede no longão, no jogo, na prova. Segundo: não é para repor cem por cento durante; o alvo é limitar a perda, não zerar, e a sede guia. Barras em esquema. Terceiro: até uma hora em clima ameno, a sede resolve; a conta é para sessão longa, calor, sintoma ou problema prévio")]
    rs = []
    W = 528
    cores = [(AZUL, AZUL_T), (GLIC, GLIC_T), (OXID, OXID_T)]
    tits = ["A taxa vale para aquela condição", "Não é repor cem por cento durante", "Até uma hora, clima ameno: a sede resolve"]
    for k in range(3):
        x = k * (W + 40)
        cor, fundo = cores[k]
        p.append(caixa(x, 0, W, 380, cor, fundo, esp=3, rx=16))
        rs.append(rot(x + 24, 18, tits[k], w=W - 48, tam=27, cor=cor, peso=700, serif=True, lh=1.15))
    # 1: verão e inverno
    p.append(icone("t:sun", 60, 120, 70, GLIC))
    p.append(icone("t:cloud-rain", 300, 120, 70, AZUL))
    rs += [rot(170, 130, "≠", w=100, tam=56, cor=TINTA, peso=700, alinha="center"),
           rot(24, 210, "verão e inverno dão números diferentes", w=W - 48, tam=22, cor=TINTA, alinha="center"),
           rot(24, 290, "medir no longão, no jogo, na prova", w=W - 48, tam=23, cor=AZUL, peso=700, alinha="center")]
    # 2: limitar a perda
    x = W + 40
    for j, (t, frac, cor) in enumerate([("perda", 1.0, MUDO), ("reposição durante", 0.6, GLIC)]):
        y = 130 + j * 76
        rs.append(rot(x + 24, y - 30, t, w=300, tam=20, cor=MUDO))
        p.append(f'<rect x="{x + 24}" y="{y}" width="{(W - 48) * frac:.0f}" height="32" rx="6" fill="{cor}"/>')
    rs += [rot(x + 24, 260, "barras: esquema", w=300, tam=18, cor=MUDO),
           rot(x + 24, 296, "limitar a perda, não zerar; a sede guia", w=W - 48, tam=23, cor=GLIC, peso=700, lh=1.2)]
    # 3: quando a conta entra
    x = 2 * (W + 40)
    for j, (ic, t) in enumerate([("t:clock", "sessão longa"), ("t:temperature", "calor"), ("t:mood-sick", "sintoma"), ("t:alert-triangle", "problema prévio")]):
        y = 140 + j * 56
        p.append(icone(ic, x + 24, y, 36, OXID))
        rs.append(rot(x + 74, y + 4, t, w=300, tam=23, cor=TINTA))
    rs.append(rot(x + 24, 104, "a conta é para:", w=300, tam=21, cor=MUDO))
    return slide("regras", 380, p, rs,
                 eyebrow="Três regras de uso", titulo="O número vale para uma condição")


def depois():
    """4.8: a conta da reidratação no jogo da noite, e quando ela importa."""
    p = [svg_abre(1664, 400, "À esquerda, a conta: perdeu 1,1 quilo no treino, multiplica por 1,25 a 1,5, e bebe 1,4 a 1,7 litro até o jogo da noite, com sódio da bebida ou da comida. À direita, quando a conta importa: outra sessão no mesmo dia ou cedo no dia seguinte, e perda grande. Com uma sessão por dia e jantar normal, a comida e a sede resolvem"), defs(MUDO)]
    passos = [("t:scale", "perdeu", "1,1 kg", GLIC), (None, "vezes", "1,25 a 1,5", TINTA), ("t:droplet", "até o jogo", "1,4 a 1,7 L", AZUL)]
    rs = []
    for k, (ic, t, n, cor) in enumerate(passos):
        x = k * 290
        p.append(caixa(x, 20, 230, 200, cor, CARTAO, esp=3, rx=16))
        if ic:
            p.append(icone(ic, x + 91, 36, 48, cor))
        rs += [rot(x, 96, t, w=230, tam=21, cor=MUDO, alinha="center"),
               rot(x, 134, n, w=230, tam=34, cor=cor, peso=700, alinha="center", serif=True)]
        if k < 2:
            p.append(seta(x + 236, 120, x + 284, 120, MUDO, "m0", esp=4))
    p.append(caixa(0, 260, 810, 120, AZUL, AZUL_T, esp=3, rx=16))
    rs += [rot(24, 278, "com sódio, da bebida ou da comida", w=760, tam=26, cor=AZUL, peso=700),
           rot(24, 326, "volume de 1,25 a 1,5 L por quilo perdido, nas horas seguintes", w=760, tam=21, cor=TINTA)]
    p.append(caixa(880, 20, 784, 220, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(904, 36, "Quando importa", w=740, tam=28, cor=GLIC, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:repeat", "outra sessão no mesmo dia ou cedo no dia seguinte"), ("t:weight", "perda grande")]):
        y = 96 + j * 66
        p.append(icone(ic, 904, y, 40, GLIC))
        rs.append(rot(960, y + 6, t, w=690, tam=23, cor=TINTA))
    p.append(caixa(880, 260, 784, 120, MUDO, PAPEL, esp=3, rx=16))
    p.append(icone("t:salad", 904, 290, 48, MUDO))
    rs.append(rot(970, 282, "uma sessão por dia e jantar normal: a comida e a sede resolvem", w=670, tam=23, cor=TINTA, lh=1.25))
    return slide("depois", 400, p, rs,
                 eyebrow="Depois · Shirreffs e colaboradores, 1996", titulo="Volume maior que a perda, com sódio",
                 destaque="Volume sem sódio escoa pela urina. Sódio sem volume não basta. O balanço fecha na interação dos dois.",
                 destaque_cor="tinta", fonte="Medicine and Science in Sports and Exercise 1996")


def bebidas():
    """4.8: a água como régua; três bebidas acima dela, nove no mesmo nível."""
    p = [svg_abre(1664, 400, "A água como linha de referência. Acima dela, as três bebidas que retiveram mais volume: leite integral, leite desnatado e solução de reidratação oral. Na linha, as nove que ficaram iguais à água no volume testado: café, chá quente, chá gelado, refrigerante comum, refrigerante sem açúcar, água com gás, isotônico, suco de laranja e cerveja comum"), defs(OXID)]
    rs = []
    acima = ["leite integral", "leite desnatado", "solução de reidratação oral"]
    for k, t in enumerate(acima):
        x = 120 + k * 480
        p.append(caixa(x, 10, 420, 70, OXID, OXID, esp=0, rx=35))
        rs.append(rot(x, 30, t, w=420, tam=25, cor=PAPEL, peso=700, alinha="center"))
        p.append(seta(x + 210, 160, x + 210, 92, OXID, "m0", esp=4))
    rs.append(rot(1540, 22, "retiveram mais", w=124, tam=21, cor=OXID, peso=700, lh=1.2))
    p.append(f'<line x1="0" y1="170" x2="1664" y2="170" stroke="{AZUL}" stroke-width="5"{TRACO}/>')
    p.append(icone("t:droplet", 0, 120, 40, AZUL))
    rs.append(rot(48, 128, "água", w=200, tam=24, cor=AZUL, peso=700))
    iguais = ["café", "chá quente", "chá gelado", "refrigerante comum", "refrigerante sem açúcar", "água com gás", "isotônico", "suco de laranja", "cerveja comum"]
    for k, t in enumerate(iguais):
        x, y = 120 + (k % 3) * 480, 200 + (k // 3) * 66
        p.append(caixa(x, y, 420, 54, TINTA, CARTAO, esp=2, rx=27))
        rs.append(rot(x, y + 13, t, w=420, tam=23, cor=TINTA, alinha="center"))
    rs.append(rot(1540, 234, "iguais à água, no volume testado", w=124, tam=21, cor=TINTA, peso=700, lh=1.2))
    return slide("bebidas", 400, p, rs,
                 eyebrow="Maughan e colaboradores, 2016", titulo="Treze bebidas, e a água como régua",
                 destaque="O café de todo dia não desidrata. O leite é uma bebida de recuperação subestimada. A cerveja: o problema não é a água, é o sono e a recuperação.",
                 destaque_cor="ambar", fonte="Um litro de cada, em pessoas hidratadas · American Journal of Clinical Nutrition 2016")


def sodio():
    """4.8: a faixa do sódio no suor contra a faixa da bebida, e quem precisa repor durante."""
    p = [svg_abre(1664, 400, "Uma régua de sódio de 0 a 100 milimoles por litro. O suor varia de 10 a 90 entre pessoas. A bebida esportiva fica entre 20 e 50, o que dá 0,5 a pouco mais de 1 grama de sódio por litro. À direita, quem precisa repor durante: acima de duas horas, calor e umidade, suador salgado, duas sessões no dia. Embaixo, a água de coco: potássio alto, sódio baixo e variável, não repõe o suador salgado")]
    X0, X1 = 20, 1000
    X = lambda v: X0 + v / 100 * (X1 - X0)
    rs = [rot(X0, 0, "sódio, em mmol/L", w=400, tam=20, cor=MUDO)]
    for v, w_, t, cor, fundo, y in [(10, 80, "no suor: 10 a 90", GLIC, GLIC_T, 40), (20, 30, "na bebida: 20 a 50", OXID, OXID_T, 120)]:
        p.append(f'<rect x="{X(v):.0f}" y="{y}" width="{X(v + w_) - X(v):.0f}" height="56" rx="8" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(X(v) + 14, y + 14, t, w=400, tam=23, cor=cor, peso=700))
    p.append(f'<line x1="{X0}" y1="200" x2="{X1}" y2="200" stroke="{MUDO}" stroke-width="3"/>')
    for v in range(0, 101, 20):
        p.append(f'<line x1="{X(v):.0f}" y1="200" x2="{X(v):.0f}" y2="212" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(v) - 40, 216, str(v), w=80, tam=19, cor=MUDO, alinha="center"))
    rs.append(rot(X(50) + 14, 134, "0,5 a pouco mais de 1 g de sódio por litro", w=420, tam=20, cor=TINTA))
    p.append(caixa(0, 280, 1000, 110, FOSF, FOSF_T, esp=3, rx=14))
    rs += [rot(24, 296, "Água de coco", w=300, tam=25, cor=FOSF, peso=700, serif=True),
           rot(24, 336, "potássio alto, sódio baixo e variável: não repõe o suador salgado", w=960, tam=22, cor=TINTA)]
    p.append(caixa(1060, 0, 604, 390, AZUL, AZUL_T, esp=3, rx=16))
    rs.append(rot(1084, 18, "Quem precisa durante", w=560, tam=28, cor=AZUL, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:clock", "acima de duas horas"), ("t:sun", "calor e umidade"), ("t:droplet", "suador salgado"), ("t:repeat", "duas sessões no dia")]):
        y = 90 + j * 72
        p.append(icone(ic, 1084, y, 42, AZUL))
        rs.append(rot(1144, y + 6, t, w=500, tam=24, cor=TINTA))
    return slide("sodio", 400, p, rs,
                 eyebrow="Sódio · uma revisão de 2017", titulo="De 10 a 90 mmol/L no suor",
                 destaque="Sal em cápsula não protege de quem bebe demais. A hiponatremia do exercício é, quase sempre, excesso de água.",
                 destaque_cor="tinta", fonte="Baker 2017 · Hew-Butler e colaboradores 2015 · faixa da bebida: posicionamento de 2007")



# ---------------------------------------------------------------- aplicação

LICOES = {"04-01": [equacao, conta_41, revisao, medida, alarme, portas_41, controversia],
          "04-02": [conta_42, ingestao, gasto, massa, erro, semconta, lanche],
          "04-03": [identidade, demais, marchadores, paraquem, comida],
          "04-04": [decisao, familias, limites, triagem, nunca, perfis],
          "04-05": [tres, teto, qualidade, whey, carga_45, perfis_45],
          "04-06": [erro_46, rotas, funcoes, hormonio, densidade, frase_46],
          "04-07": [pedidos, quem, vegano, come, prato, sente, turbina],
          "04-08": [numero, variacao, regras, depois, bebidas, sodio]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
