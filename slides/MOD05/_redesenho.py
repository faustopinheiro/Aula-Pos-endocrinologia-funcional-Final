"""Desenhos que substituem os slides de texto do Módulo 5 (cartões, colunas, listas, tabelas e números).
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


# ---------------------------------------------------------------- 5.1

def pote(p, x, y, w, h, cor, fundo=CARTAO):
    """Um pote de suplemento: tampa e corpo."""
    p.append(f'<rect x="{x + w * 0.12:.0f}" y="{y}" width="{w * 0.76:.0f}" height="{h * 0.16:.0f}" rx="8" fill="{cor}"/>')
    p.append(f'<rect x="{x}" y="{y + h * 0.16 + 4:.0f}" width="{w}" height="{h * 0.84 - 4:.0f}" rx="22" fill="{fundo}" stroke="{cor}" stroke-width="4"/>')


def pedidos_51():
    """5.1: três potes, três pedidos, a mesma pergunta."""
    p = [svg_abre(1664, 400, "Três potes, cada um com um pedido. O pré-treino de catorze ingredientes, com blend proprietário e sem dose por item. O colágeno, pedido por uma mulher que treina força duas vezes por semana e tem dor no joelho. A creatina, para um adolescente do futebol que o técnico achou fraco para a idade")]
    itens = [("O pré-treino", "catorze ingredientes, “blend proprietário”, sem dose por item", FOSF, FOSF_T),
             ("O colágeno", "mulher que treina força duas vezes por semana, com dor no joelho", GLIC, GLIC_T),
             ("A creatina", "adolescente de futebol; o técnico disse que ele está fraco para a idade", OXID, OXID_T)]
    rs = []
    for k, (t, d, cor, fundo) in enumerate(itens):
        x = k * 568
        pote(p, x + 20, 0, 220, 340, cor, fundo)
        rs.append(rot(x + 20, 130, t, w=220, tam=27, cor=cor, peso=700, alinha="center", serif=True, lh=1.15))
        p.append(icone("t:question-mark", x + 98, 220, 64, cor))
        rs.append(rot(x + 262, 90, d, w=262, tam=23, cor=TINTA, lh=1.3))
    return slide("pedidos", 400, p, rs,
                 eyebrow="Três pedidos típicos", titulo="A mesma pergunta, três vezes",
                 destaque="A resposta certa para as três não é “funciona” nem “não funciona”.", destaque_cor="tinta")


def passo1():
    """5.1: um funil de três perguntas antes do pote."""
    p = [svg_abre(1664, 400, "Um funil de três perguntas antes de chegar ao pote. Primeira: qual é o objetivo, em desfecho, como sprint repetido, prova longa, massa ou recuperação entre jogos; suplemento não tem efeito genérico. Segunda: a base está feita, com energia, sono, treino e proteína distribuída; sem base, o retorno é indistinguível de zero. Terceira: existe um motivo para não ser comida? Se não existe obstáculo, a resposta já é não")]
    qs = [("Qual é o objetivo, em desfecho?", "sprint repetido, prova longa, massa, recuperação entre jogos: suplemento não tem efeito genérico", OXID, OXID_T),
          ("A base está feita?", "energia, sono, treino, proteína distribuída: sem base, o retorno é indistinguível de zero", GLIC, GLIC_T),
          ("Existe um motivo para não ser comida?", "se não existe obstáculo, a resposta já é não", FOSF, FOSF_T)]
    rs = []
    for k, (t, d, cor, fundo) in enumerate(qs):
        y = k * 130
        w0, w1 = 1300 - k * 260, 1300 - (k + 1) * 260
        x0 = (1300 - w0) / 2
        x1 = (1300 - w1) / 2
        p.append(f'<path d="M {x0:.0f} {y} H {x0 + w0:.0f} L {x1 + w1:.0f} {y + 116} H {x1:.0f} Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs += [rot(x0 + 60, y + 14, t, w=w0 - 120, tam=26, cor=cor, peso=700, alinha="center", serif=True),
               rot(x0 + 90, y + 54, d, w=w0 - 180, tam=20, cor=TINTA, alinha="center", lh=1.25)]
    pote(p, 1420, 150, 180, 230, MUDO, PAPEL)
    rs.append(rot(1440, 250, "o pote, por último", w=140, tam=21, cor=MUDO, peso=700, alinha="center", lh=1.2))
    p.append(f'<path d="M 1060 300 C 1200 340, 1320 320, 1410 290" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
    return slide("passo1", 400, p, rs,
                 eyebrow="Passo um · a pergunta antes do produto", titulo="Três perguntas antes do pote")


def comida():
    """5.1: comida primeiro, e os seis motivos que abrem espaço ao suplemento."""
    p = [svg_abre(1664, 400, "À esquerda, o prato: comida primeiro. À direita, os seis motivos que abrem espaço ao suplemento, em dois grupos. Pelo nutriente: difícil de obter na dieta em quantidade suficiente, está num alimento que a pessoa não come, ou tem teor variável quando a dose precisa ser previsível. Pela situação: deficiência que pede dose concentrada, perto do exercício quando comer é inviável, e preocupação real com a higiene do alimento disponível"), defs(MUDO)]
    p.append(f'<circle cx="190" cy="190" r="170" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    p.append(icone("t:salad", 140, 80, 100, OXID))
    rs = [rot(40, 200, "Comida primeiro", w=300, tam=30, cor=OXID, peso=700, alinha="center", serif=True)]
    p.append(seta(380, 190, 470, 190, MUDO, "m0", esp=4))
    rs.append(rot(380, 214, "nem sempre só comida, quando", w=120, tam=18, cor=MUDO, lh=1.2))
    grupos = [(520, "Pelo nutriente", OXID, [("Difícil de obter", "na dieta, em quantidade suficiente"), ("Alimento que não come", "o nutriente está onde a pessoa não vai"), ("Teor variável", "e a dose precisa ser previsível")]),
              (1100, "Pela situação", GLIC, [("Deficiência", "pede dose concentrada para corrigir"), ("Perto do exercício", "comer é inviável: gel e bebida são suplemento"), ("Higiene", "preocupação real com o alimento disponível")])]
    for x, t, cor, itens in grupos:
        rs.append(rot(x, 0, t, w=540, tam=24, cor=cor, peso=700, serif=True))
        for k, (a, b) in enumerate(itens):
            y = 46 + k * 118
            p.append(caixa(x, y, 544, 104, cor, CARTAO, esp=2, rx=14))
            rs += [rot(x + 20, y + 14, a, w=500, tam=24, cor=cor, peso=700), rot(x + 20, y + 52, b, w=510, tam=20, cor=TINTA, lh=1.2)]
    return slide("comida", 400, p, rs,
                 eyebrow="Uma revisão de 2022", titulo="Comida primeiro, mas nem sempre só comida",
                 fonte="Close e colaboradores · International Journal of Sport Nutrition and Exercise Metabolism 2022")


def abcd():
    """5.1: as quatro letras como degraus de evidência."""
    p = [svg_abre(1664, 400, "As quatro letras do quadro do Instituto Australiano do Esporte. A: evidência forte, no protocolo e na situação certos; alimentos esportivos, ferro, vitamina D e cálcio na deficiência, creatina, cafeína, beta-alanina, bicarbonato, nitrato e glicerol. B: evidência emergente; colágeno, curcumina, alguns polifenóis. C: sem benefício comprovado; o grupo maior, e a maior parte do que se vende. D: proibido ou com alto risco de conter; estimulantes, pró-hormônios e moduladores seletivos do receptor de androgênio")]
    linhas = [("A", "evidência forte, no protocolo e na situação certos", "alimentos esportivos; ferro, vitamina D e cálcio na deficiência; creatina, cafeína, beta-alanina, bicarbonato, nitrato, glicerol", OXID, OXID_T),
              ("B", "evidência emergente", "colágeno, curcumina, alguns polifenóis", GLIC, GLIC_T),
              ("C", "sem benefício comprovado", "o grupo maior, e a maior parte do que se vende", MUDO, PAPEL),
              ("D", "proibido ou com alto risco de conter", "estimulantes, pró-hormônios, moduladores seletivos do receptor de androgênio", FOSF, FOSF_T)]
    rs = []
    for k, (l, s_, ex, cor, fundo) in enumerate(linhas):
        y = k * 100
        p.append(caixa(0, y, 1664, 88, cor, fundo, esp=2, rx=14))
        p.append(f'<circle cx="50" cy="{y + 44}" r="32" fill="{cor}"/>')
        rs += [rot(18, y + 20, l, w=64, tam=34, cor=PAPEL, peso=700, alinha="center", serif=True),
               rot(110, y + 28, s_, w=520, tam=23, cor=cor if cor != MUDO else TINTA, peso=700, lh=1.2),
               rot(660, y + (16 if len(ex) > 90 else 30), ex, w=980, tam=21, cor=TINTA, lh=1.3)]
    return slide("abcd", 400, p, rs,
                 eyebrow="Passo dois · Instituto Australiano do Esporte", titulo="O eixo da evidência, em quatro letras",
                 destaque="O quadro classifica ingredientes, não marcas. Essa distinção já é meio caminho.",
                 destaque_cor="petr", fonte="AIS Sports Supplement Framework")


def perguntas():
    """5.1: o selo A no centro e as quatro perguntas que ele não responde."""
    p = [svg_abre(1664, 400, "No centro, o selo do grupo A. Em volta, quatro perguntas que a letra não responde. Em quem? A maioria dos estudos é em homens jovens treinados. Qual desfecho? Desempenho, ou marcador de laboratório. De que tamanho? Pequeno: decide pódio, some no amador. Comparado com o quê? Com placebo, e com dormir, comer e treinar")]
    cx, cy = 832, 200
    qs = [(0, 0, "h:man", "Em quem?", "a maioria dos estudos: homens jovens treinados", OXID),
          (1064, 0, "t:target", "Qual desfecho?", "desempenho, ou marcador de laboratório", OXID),
          (0, 220, "t:ruler-measure", "De que tamanho?", "pequeno: decide pódio, some no amador", GLIC),
          (1064, 220, "t:arrows-exchange", "Comparado com o quê?", "com placebo, e com dormir, comer e treinar", FOSF)]
    rs = []
    for x, y, ic, t, d, cor in qs:
        ax = x + 600 if x == 0 else x
        p.append(f'<line x1="{ax}" y1="{y + 90}" x2="{cx + (-90 if x == 0 else 90)}" y2="{cy + (-40 if y == 0 else 40)}" stroke="{BORDA}" stroke-width="3"/>')
        p.append(caixa(x, y, 600, 180, cor, CARTAO, esp=3, rx=16))
        p.append(icone(ic, x + 24, y + 24, 48, cor))
        rs += [rot(x + 90, y + 30, t, w=490, tam=28, cor=cor, peso=700, serif=True), rot(x + 24, y + 96, d, w=550, tam=22, cor=TINTA, lh=1.3)]
    p.append(f'<circle cx="{cx}" cy="{cy}" r="110" fill="{OXID}"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="94" fill="none" stroke="{PAPEL}" stroke-width="3"/>')
    rs += [rot(cx - 80, cy - 70, "A", w=160, tam=96, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(cx - 80, cy + 44, "grupo", w=160, tam=22, cor=PAPEL, alinha="center")]
    return slide("perguntas", 400, p, rs,
                 eyebrow="Dentro do grupo A · o consenso do COI, 2018", titulo="A letra não basta",
                 destaque="Consenso do Comitê Olímpico: a nutrição dá uma contribuição pequena, mas potencialmente valiosa, ao desempenho; os suplementos, uma contribuição menor dentro dela.",
                 destaque_cor="tinta", fonte="Maughan e colaboradores · British Journal of Sports Medicine 2018")


def riscos():
    """5.1: quatro riscos que convergem para o mesmo não."""
    p = [svg_abre(1664, 400, "Quatro riscos lado a lado, cada um com uma seta para a mesma barra: basta um para pesar contra. Contaminação: o rótulo e o pote podem não coincidir, e a responsabilidade é do atleta. Risco clínico: interação, doença de base, gestação, idade; avaliação médica. Custo: dinheiro que não foi para comida, academia ou consulta. Deslocamento: o que o pote tira do lugar, como sono, café da manhã e carga"), defs(MUDO)]
    rr = [("t:alert-triangle", "Contaminação", "o rótulo e o pote podem não coincidir; a responsabilidade é do atleta", FOSF, FOSF_T),
          ("t:stethoscope", "Risco clínico", "interação, doença de base, gestação, idade; avaliação médica", GLIC, GLIC_T),
          ("h:money-bag", "Custo", "dinheiro que não foi para comida, academia ou consulta", GLIC, GLIC_T),
          ("t:arrows-exchange", "Deslocamento", "o que o pote tira do lugar: sono, café da manhã, carga", TINTA, CARTAO)]
    rs = []
    W = 386
    for k, (ic, t, d, cor, fundo) in enumerate(rr):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 250, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, x + 20, 20, 44, cor))
        rs += [rot(x + 76, 28, t, w=W - 90, tam=26, cor=cor, peso=700, serif=True), rot(x + 20, 96, d, w=W - 40, tam=21, cor=TINTA, lh=1.3)]
        p.append(seta(x + W / 2, 256, 832 + (x + W / 2 - 832) * 0.3, 314, MUDO, "m0", esp=3))
    p.append(caixa(432, 320, 800, 70, FOSF, FOSF, esp=0, rx=35))
    rs.append(rot(432, 338, "basta um para pesar contra", w=800, tam=26, cor=PAPEL, peso=700, alinha="center"))
    return slide("riscos", 400, p, rs,
                 eyebrow="Passo três · o eixo do risco", titulo="Quatro riscos, e basta um",
                 destaque="O suplemento raramente faz mal. Ele frequentemente faz com que outra coisa não seja feita, e essa outra coisa costuma ser a que funcionava.",
                 destaque_cor="verm")


def rotulo():
    """5.1: o enquadramento brasileiro e um rótulo com os cinco sinais de alerta."""
    p = [svg_abre(1664, 400, "À esquerda, o enquadramento brasileiro do suplemento: suplementa, não substitui; é para indivíduos saudáveis, não tratamento; é alimento e não prova eficácia antes da venda; segue listas positivas de constituintes e de alegações. À direita, um pote com o rótulo e cinco sinais de alerta apontados: blend proprietário sem dose por item, lista muito longa, dose abaixo da estudada, alegação que não é o desfecho estudado, e estudo único, pequeno e do fabricante")]
    p.append(caixa(0, 0, 640, 400, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 18, "O enquadramento brasileiro", w=600, tam=27, cor=OXID, peso=700, serif=True)]
    for k, t in enumerate(["suplementa, não substitui", "para indivíduos saudáveis, não tratamento", "é alimento: não prova eficácia antes da venda", "listas positivas de constituintes e de alegações"]):
        y = 84 + k * 76
        p.append(f'<circle cx="38" cy="{y + 14}" r="8" fill="{OXID}"/>')
        rs.append(rot(58, y, t, w=560, tam=22, cor=TINTA, lh=1.25))
    pote(p, 720, 30, 260, 360, MUDO, CARTAO)
    p.append(f'<rect x="740" y="140" width="220" height="200" rx="8" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    for k in range(7):
        p.append(f'<line x1="760" y1="{170 + k * 24}" x2="{940 - (k % 3) * 30}" y2="{170 + k * 24}" stroke="{CINZA}" stroke-width="6" stroke-linecap="round"/>')
    alertas = ["blend proprietário, sem dose por item", "lista muito longa", "dose abaixo da estudada", "alegação que não é o desfecho estudado", "estudo único, pequeno e do fabricante"]
    rs.append(rot(1060, 0, "Cinco sinais de alerta", w=600, tam=27, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(alertas):
        y = 70 + k * 66
        p.append(f'<line x1="960" y1="{180 + k * 24}" x2="1056" y2="{y + 18}" stroke="{FOSF}" stroke-width="2"/>')
        p.append(f'<circle cx="1076" cy="{y + 18}" r="16" fill="{FOSF}"/>')
        rs += [rot(1060, y + 6, str(k + 1), w=32, tam=19, cor=PAPEL, peso=700, alinha="center"), rot(1106, y + 4, t, w=556, tam=22, cor=TINTA)]
    return slide("rotulo", 400, p, rs,
                 eyebrow="Passo quatro · RDC 243 e IN 28, de 2018", titulo="O rótulo e a alegação",
                 destaque="Promessa de cura, emagrecimento garantido ou “aumenta a testosterona” fora da lista: o rótulo está irregular.",
                 destaque_cor="ambar", fonte="Agência Nacional de Vigilância Sanitária")


def decidir():
    """5.1: o pedido se abre em três saídas, e o talvez vira uma folha de teste."""
    p = [svg_abre(1664, 400, "O pedido se abre em três saídas. Não: isso não responde; o que responde é isto. Sim, com protocolo: grupo A, dose, momento, risco avaliado. Talvez: então é teste, não adoção. O talvez leva a uma folha de teste com quatro linhas: o quê, uma coisa por vez; para qual desfecho medido; por quanto tempo; e o critério de reversão, escrito antes"), defs(MUDO, GLIC)]
    p.append(caixa(0, 150, 200, 90, TINTA, TINTA, esp=0, rx=45))
    rs = [rot(0, 178, "o pedido", w=200, tam=26, cor=PAPEL, peso=700, alinha="center")]
    saidas = [(20, "Não", "“isso não responde; o que responde é isto”", FOSF, FOSF_T),
              (150, "Sim, com protocolo", "grupo A, dose, momento, risco avaliado", OXID, OXID_T),
              (280, "Talvez", "então é teste, não adoção", GLIC, GLIC_T)]
    for y, t, d, cor, fundo in saidas:
        p.append(seta(206, 195, 296, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(306, y, 560, 104, cor, fundo, esp=3, rx=14))
        rs += [rot(330, y + 12, t, w=520, tam=25, cor=cor, peso=700, serif=True), rot(330, y + 56, d, w=520, tam=21, cor=TINTA)]
    p.append(seta(872, 332, 950, 332, GLIC, "m1", esp=4))
    p.append(f'<path d="M 960 0 h 650 l 54 54 v 346 h -704 z" fill="{CARTAO}" stroke="{GLIC}" stroke-width="3"/>')
    p.append(f'<path d="M 1610 0 v 54 h 54" fill="none" stroke="{GLIC}" stroke-width="3"/>')
    rs.append(rot(990, 18, "A folha do teste", w=600, tam=28, cor=GLIC, peso=700, serif=True))
    for k, (a, b) in enumerate([("o quê", "uma coisa por vez"), ("desfecho", "qual, e medido como"), ("tempo", "por quanto tempo"), ("reversão", "critério escrito antes")]):
        y = 84 + k * 76
        p.append(f'<line x1="990" y1="{y + 60}" x2="1634" y2="{y + 60}" stroke="{BORDA}" stroke-width="2"/>')
        rs += [rot(990, y + 14, a, w=200, tam=23, cor=GLIC, peso=700), rot(1200, y + 14, b, w=430, tam=22, cor=TINTA)]
    return slide("decidir", 400, p, rs,
                 eyebrow="Passo cinco · decidir", titulo="Três saídas, e o teste com data",
                 destaque="O placebo é real, custa todo mês e ensina a atribuir o resultado ao pote. Quem atribui o progresso ao pote para de treinar quando o pote acaba.",
                 destaque_cor="tinta")


def respostas():
    """5.1: os três potes de novo, cada um com o passo que decide e a resposta."""
    p = [svg_abre(1664, 300, "Os três potes do começo, cada um com o passo que decide e a resposta. Pré-treino: decide o passo quatro, o rótulo; sem dose por item, não há o que avaliar, e o problema é a jornada, não a química. Colágeno: decide o passo um, o objetivo; é grupo B, e para a dor no joelho o que tem evidência é exercício. Creatina: decide o passo um, a base; fraco para a idade não é diagnóstico, e vêm antes comida, sono, maturação e treino orientado")]
    itens = [("O pré-treino", "passo quatro: o rótulo", "sem dose por item, não há o que avaliar; o problema é a jornada, não a química", FOSF, FOSF_T),
             ("O colágeno", "passo um: o objetivo", "grupo B; para a dor no joelho, o que tem evidência é exercício", GLIC, GLIC_T),
             ("A creatina", "passo um: a base", "“fraco para a idade” não é diagnóstico: comida, sono, maturação, treino orientado", OXID, OXID_T)]
    rs = []
    for k, (t, ps, r, cor, fundo) in enumerate(itens):
        x = k * 568
        pote(p, x, 0, 170, 290, cor, fundo)
        rs.append(rot(x, 120, t, w=170, tam=22, cor=cor, peso=700, alinha="center", serif=True, lh=1.15))
        p.append(caixa(x + 190, 40, 340, 60, cor, cor, esp=0, rx=30))
        rs.append(rot(x + 190, 56, ps, w=340, tam=21, cor=PAPEL, peso=700, alinha="center"))
        rs.append(rot(x + 190, 124, r, w=340, tam=22, cor=TINTA, lh=1.3))
    return slide("respostas", 300, p, rs,
                 eyebrow="Os três pedidos, com os cinco passos", titulo="O passo que decide cada um",
                 destaque="A creatina tem a maior evidência do campo, e, ainda assim, a resposta não sai do eixo da evidência.",
                 destaque_cor="petr")

# ---------------------------------------------------------------- 5.2

def confusao():
    """5.2: os mitos em cima, e embaixo a régua da magnitude que explica quase todos."""
    p = [svg_abre(1664, 380, "Em cima, seis confusões sobre creatina: rim, cabelo, ciclar, cãibra, quase anabolizante, criança não pode. Embaixo, uma régua de tamanho de efeito, em esquema, de zero até o efeito de um anabolizante. A creatina fica perto do começo: um efeito pequeno e real. Quem espera o efeito de um anabolizante olha para a ponta direita; quem descarta o efeito por ser pequeno olha para o zero"), defs(FOSF, GLIC)]
    rs = []
    for k, t in enumerate(["rim", "cabelo", "ciclar", "cãibra", "“quase anabolizante”", "“criança não pode”"]):
        w = 200 if k < 4 else 340
        x = [0, 230, 460, 690, 920, 1290][k]
        p.append(caixa(x, 0, w, 64, MUDO, CARTAO, esp=2, rx=32))
        rs.append(rot(x, 18, t, w=w, tam=23, cor=TINTA, alinha="center"))
    Y = 270
    p.append(f'<line x1="40" y1="{Y}" x2="1620" y2="{Y}" stroke="{MUDO}" stroke-width="4"/>')
    for x, t in [(40, "zero"), (1620, "anabolizante")]:
        p.append(f'<line x1="{x}" y1="{Y - 14}" x2="{x}" y2="{Y + 14}" stroke="{MUDO}" stroke-width="4"/>')
        rs.append(rot(x - 110, Y + 24, t, w=220, tam=21, cor=MUDO, alinha="center"))
    p.append(f'<circle cx="300" cy="{Y}" r="18" fill="{OXID}"/>')
    rs += [rot(160, Y + 30, "a creatina: pequeno e real", w=360, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(640, Y + 60, "esquema, sem valores medidos", w=400, tam=18, cor=MUDO, alinha="center")]
    p.append(f'<path d="M 520 150 C 360 150, 120 170, 64 {Y - 26}" fill="none" stroke="{GLIC}" stroke-width="3" marker-end="url(#m1)"/>')
    p.append(f'<path d="M 1140 150 C 1320 150, 1560 170, 1606 {Y - 26}" fill="none" stroke="{FOSF}" stroke-width="3" marker-end="url(#m0)"/>')
    rs += [rot(530, 132, "quem descarta por ser pequeno", w=380, tam=21, cor=GLIC, peso=700),
           rot(720, 186, "quem espera o efeito de um anabolizante", w=410, tam=21, cor=FOSF, peso=700, alinha="right")]
    return slide("confusao", 380, p, rs,
                 eyebrow="O suplemento mais estudado", titulo="Muita evidência, muita confusão.",
                 destaque="Quase toda confusão sobre creatina é de magnitude.", destaque_cor="tinta")


def peso():
    """5.2: a balança sobe na primeira semana, e o aviso precisa vir antes."""
    p = [svg_abre(1664, 400, "À esquerda, a balança das primeiras semanas: 1 a 2 quilos a mais, em boa parte água dentro da célula, desenhada como gotas dentro de uma célula. No meio, dois caminhos: quem foi avisado antes segue; quem não foi lê o peso como gordura e para. À direita, a categoria de peso: aí o ganho é um efeito colateral real, para conversar com técnico e nutricionista"), defs(OXID, FOSF)]
    p.append(caixa(0, 0, 560, 400, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:scale", 24, 24, 56, GLIC))
    rs = [rot(96, 30, "1 a 2 kg", w=440, tam=48, cor=GLIC, peso=700, serif=True),
          rot(40, 110, "a mais, em boa parte água dentro da célula", w=480, tam=22, cor=TINTA, lh=1.25)]
    p.append(f'<ellipse cx="280" cy="270" rx="200" ry="95" fill="{CARTAO}" stroke="{GLIC}" stroke-width="3"/>')
    for k in range(7):
        p.append(icone("t:droplet", 126 + k * 44, 246 + (k % 2) * 18, 32, AZUL))
    p.append(caixa(620, 40, 460, 130, OXID, OXID_T, esp=3, rx=14))
    rs += [rot(644, 56, "avisado antes", w=420, tam=26, cor=OXID, peso=700, serif=True), rot(644, 100, "lê o peso como esperado e segue", w=420, tam=21, cor=TINTA, lh=1.25)]
    p.append(caixa(620, 230, 460, 130, FOSF, FOSF_T, esp=3, rx=14))
    rs += [rot(644, 246, "não avisado", w=420, tam=26, cor=FOSF, peso=700, serif=True), rot(644, 290, "lê como gordura e para", w=420, tam=21, cor=TINTA, lh=1.25)]
    p.append(seta(566, 170, 612, 110, OXID, "m0", esp=4))
    p.append(seta(566, 230, 612, 290, FOSF, "m1", esp=4))
    p.append(caixa(1140, 0, 524, 400, TINTA, CARTAO, esp=3, rx=16))
    p.append(icone("t:weight", 1164, 24, 48, TINTA))
    rs += [rot(1226, 30, "Categoria de peso", w=420, tam=26, cor=TINTA, peso=700, serif=True),
           rot(1164, 110, "o ganho é um efeito colateral real", w=470, tam=23, cor=TINTA, lh=1.3),
           rot(1164, 220, "conversa com técnico e nutricionista antes de começar", w=470, tam=22, cor=MUDO, lh=1.3)]
    return slide("peso", 400, p, rs,
                 eyebrow="As primeiras semanas", titulo="O que se vê em uma semana é peso",
                 destaque="O peso, sozinho, nunca é o desfecho do teste: ele sobe em quase todo mundo, responda a pessoa ou não.",
                 destaque_cor="tinta")


def responde():
    """5.2: dois tanques, o cheio e o baixo, e o espaço até o teto."""
    p = [svg_abre(1664, 400, "Dois tanques de creatina no músculo, com a mesma tampa. O tanque de quem come carne e peixe todo dia começa mais cheio, em cerca de 130 milimoles por quilo, e tem pouco espaço até o teto; entre esses estão os chamados não respondedores, 20 a 30% em estudos pequenos. O tanque do vegetariano começa em cerca de 117, mais baixo: teve maior aumento de estoque e de massa magra, e maior ganho de trabalho total. Alturas em esquema")]
    rs = []
    TETO, B, K = 60, 380, 2.2
    lados = [(0, 130, "Tanque cheio", "come carne e peixe todo dia", ["pouco espaço até o teto", "“não respondedor”: 20 a 30%, em estudos pequenos"], MUDO, CINZA),
             (864, 117, "Tanque baixo", "vegetariano", ["maior aumento de estoque e de massa magra", "maior ganho de trabalho total"], OXID, OXID_T)]
    for x, v, t, d, itens, cor, fundo in lados:
        p.append(f'<rect x="{x}" y="{TETO - 20}" width="220" height="20" rx="6" fill="{TINTA}"/>')
        p.append(f'<rect x="{x}" y="{TETO}" width="220" height="{B - TETO}" rx="10" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
        h = (v - 40) * K
        p.append(f'<rect x="{x + 4}" y="{B - h:.0f}" width="212" height="{h - 4:.0f}" rx="8" fill="{fundo}"/>')
        rs.append(rot(x, B - h + 10, f"≈ {v}", w=220, tam=30, cor=cor if cor != MUDO else TINTA, peso=700, alinha="center", serif=True))
        rs.append(rot(x, B - h + 50, "mmol/kg", w=220, tam=18, cor=MUDO, alinha="center"))
        p.append(f'<path d="M {x + 236} {TETO + 4} v {B - h - TETO - 8:.0f}" stroke="{cor}" stroke-width="3" fill="none"/>')
        rs += [rot(x + 260, 30, t, w=520, tam=30, cor=cor if cor != MUDO else TINTA, peso=700, serif=True),
               rot(x + 260, 76, d, w=520, tam=23, cor=TINTA, peso=600)]
        for k, it in enumerate(itens):
            rs.append(rot(x + 260, 150 + k * 80, it, w=520, tam=22, cor=TINTA, lh=1.25))
    rs.append(rot(0, 0, "alturas: esquema", w=220, tam=17, cor=MUDO, alinha="center"))
    return slide("responde", 400, p, rs,
                 eyebrow="Um estudo de 2003", titulo="Quem chega com o tanque baixo responde mais",
                 destaque="A primeira pergunta é dietética: quanta carne e peixe essa pessoa come? E a resposta se mede no treino: 4 a 8 semanas, um desfecho escolhido antes.",
                 destaque_cor="ambar", fonte="Burke e colaboradores · Medicine and Science in Sports and Exercise 2003 · Syrotuik e Bell 2004")


def rim():
    """5.2: o que o ensaio mostrou, e o caminho da creatina até o exame que engana."""
    p = [svg_abre(1664, 400, "À esquerda, o que o ensaio mostrou: treinados em força, com dieta rica em proteína, 12 semanas, randomizado e com placebo; a filtração medida não mudou, e proteinúria e albuminúria ficaram iguais. À direita, a armadilha, como um caminho: a creatina vira creatinina, a creatinina no sangue sobe um pouco, e a filtração estimada pela fórmula cai. É substrato a mais, não filtração a menos"), defs(MUDO)]
    p.append(caixa(0, 0, 640, 400, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "O que o ensaio mostrou", w=600, tam=27, cor=OXID, peso=700, serif=True)]
    for k, (ic, t) in enumerate([("t:barbell", "treinados em força, dieta rica em proteína"), ("t:calendar", "12 semanas, randomizado, com placebo"), ("t:check", "filtração medida sem alteração"), ("t:check", "proteinúria e albuminúria iguais")]):
        y = 82 + k * 76
        p.append(icone(ic, 24, y, 38, OXID))
        rs.append(rot(76, y + 4, t, w=550, tam=22, cor=TINTA))
    passos = [("creatina", "vira creatinina", MUDO), ("creatinina no sangue", "um pouco mais alta", GLIC), ("filtração estimada", "mais baixa na fórmula", FOSF)]
    rs.append(rot(700, 0, "A armadilha", w=600, tam=27, cor=FOSF, peso=700, serif=True))
    for k, (t, d, cor) in enumerate(passos):
        x = 700 + k * 330
        p.append(caixa(x, 60, 290, 140, cor, CARTAO, esp=3, rx=14))
        rs += [rot(x + 16, 80, t, w=258, tam=23, cor=cor if cor != MUDO else TINTA, peso=700, alinha="center", lh=1.15), rot(x + 16, 146, d, w=258, tam=20, cor=TINTA, alinha="center")]
        if k < 2:
            p.append(seta(x + 294, 130, x + 326, 130, MUDO, "m0", esp=3))
    p.append(caixa(700, 250, 950, 110, TINTA, TINTA, esp=0, rx=16))
    rs.append(rot(700, 286, "substrato a mais, não filtração a menos", w=950, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("rim", 400, p, rs,
                 eyebrow="Mito um · um ensaio de 2013", titulo="O rim, e a armadilha do exame",
                 destaque="Quem usa avisa antes de coletar. Quem tem doença renal ou risco relevante é outra conversa, médica e individual.",
                 destaque_cor="tinta", fonte="Lugaresi, Gualano e colaboradores · Journal of the International Society of Sports Nutrition 2013")


def mitos():
    """5.2: quatro mitos, cada um com o selo do que a evidência diz."""
    p = [svg_abre(1664, 400, "Quatro quadros, cada um com um mito e o selo do que a evidência diz. Cabelo: 20 jogadores, o estudo mediu hormônio e não cabelo, e não foi replicado. Cãibra e calor: sem mais cãibra numa temporada no calor, num estudo observacional, e sem prejuízo térmico. Esteroide: não é hormônio, não age no receptor androgênico e não é proibida. Ciclar: ao parar, o estoque volta ao basal; ciclar é manter o tanque pela metade")]
    W = 386
    quadros = [("Cabelo", "sem replicação", "20 jogadores; mediu hormônio, não cabelo (2009)", GLIC, GLIC_T),
               ("Cãibra e calor", "sem sinal", "sem mais cãibra no calor (2003, observacional); sem prejuízo térmico (2009)", OXID, OXID_T),
               ("Esteroide", "não é", "não é hormônio, não age no receptor androgênico, não é proibida", OXID, OXID_T),
               ("Ciclar", "tanque pela metade", "ao parar, o estoque volta ao basal", OXID, OXID_T)]
    rs = []
    for k, (t, selo, d, cor, fundo) in enumerate(quadros):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 400, cor, CARTAO, esp=3, rx=16))
        rs.append(rot(x + 20, 20, "mito", w=W - 40, tam=19, cor=MUDO, peso=700))
        rs.append(rot(x + 20, 50, t, w=W - 40, tam=30, cor=TINTA, peso=700, serif=True))
        p.append(caixa(x + 20, 112, W - 40, 64, cor, fundo, esp=3, rx=32))
        rs.append(rot(x + 20, 130, selo, w=W - 40, tam=24, cor=cor, peso=700, alinha="center"))
        rs.append(rot(x + 20, 210, d, w=W - 40, tam=21, cor=TINTA, lh=1.35))
    return slide("mitos", 400, p, rs,
                 eyebrow="Mitos dois a cinco", titulo="Cada mito com o número que merece",
                 destaque="Quem tem calvície familiar pode não usar, sabendo que a escolha é de precaução, não de evidência.",
                 destaque_cor="tinta", fonte="van der Merwe e colaboradores 2009 · Greenwood e colaboradores 2003 · Lopez e colaboradores 2009")


def populacoes():
    """5.2: quatro populações, o que a evidência mostra e onde a conta muda."""
    p = [svg_abre(1664, 400, "Quatro populações. Mulheres: efeito compatível com o dos homens, com menos estudos; dose igual, e interesse na menopausa. Idosos: 22 ensaios e 721 pessoas, com 1,4 quilo a mais de massa magra quando há treino de força; só com carga. Adolescentes: sem sinal de dano nas doses usuais; decisão médica, depois da base. Vegetarianos: tanque mais baixo, resposta maior; atenção à cápsula de gelatina")]
    linhas = [("h:woman", "Mulheres", "efeito compatível com o dos homens; menos estudos (2021)", "dose igual; interesse na menopausa", OXID),
              ("h:old-man", "Idosos", "22 ensaios, 721 pessoas: +1,4 kg de massa magra com treino de força (2017)", "só com carga; sem ela, não vale", OXID),
              ("h:boy-1015y", "Adolescentes", "sem sinal de dano nas doses usuais (2021)", "decisão médica, depois da base", FOSF),
              ("t:plant", "Vegetarianos", "tanque mais baixo, resposta maior", "atenção à cápsula de gelatina", GLIC)]
    rs = [rot(320, 0, "O que a evidência mostra", w=700, tam=19, cor=MUDO, peso=700), rot(1120, 0, "Na conduta", w=500, tam=19, cor=MUDO, peso=700)]
    for k, (ic, t, ev, cond, cor) in enumerate(linhas):
        y = 36 + k * 92
        p.append(f'<line x1="0" y1="{y + 84}" x2="1664" y2="{y + 84}" stroke="{BORDA}" stroke-width="2"/>')
        p.append(icone(ic, 0, y + 14, 50, cor))
        rs += [rot(66, y + 24, t, w=240, tam=25, cor=TINTA, peso=700, serif=True),
               rot(320, y + 12, ev, w=760, tam=21, cor=TINTA, lh=1.3)]
        p.append(caixa(1110, y + 10, 554, 62, cor, CARTAO, esp=2, rx=31))
        rs.append(rot(1110, y + 28, cond, w=554, tam=21, cor=cor, peso=700, alinha="center"))
    return slide("populacoes", 400, p, rs,
                 eyebrow="Em quem foi estudado", titulo="Onde a conta muda",
                 destaque="O adolescente “fraco para a idade” tem quatro explicações antes do pote: comida, sono, maturação e treino orientado. E o pote ensina que força se compra.",
                 destaque_cor="verm", fonte="Smith-Ryan e colaboradores 2021 · Chilibeck e colaboradores 2017 · Jagim e Kerksick 2021")


def alem():
    """5.2: a reabilitação depois do gesso e o sinal modesto na cognição."""
    p = [svg_abre(1664, 400, "À esquerda, a reabilitação: 22 voluntários com duas semanas de gesso. Durante o gesso, a creatina não protegeu o músculo parado; na reabilitação, quem tomava recuperou mais. O ponto prático é estar tomando quando a carga voltar. À direita, a cognição: 6 ensaios e 281 pessoas saudáveis, com efeito na memória de curto prazo, maior em idosos; um sinal real e modesto, e mecanismo não é indicação")]
    p.append(caixa(0, 0, 900, 400, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "Reabilitação", w=500, tam=28, cor=OXID, peso=700, serif=True),
          rot(300, 22, "22 voluntários", w=580, tam=21, cor=MUDO, alinha="right")]
    fases = [(24, 400, "2 semanas de gesso", "não protegeu o músculo parado", MUDO, PAPEL), (444, 432, "reabilitação", "recuperou mais", OXID, CARTAO)]
    for x, w, t, d, cor, fundo in fases:
        p.append(caixa(x, 80, w, 170, cor, fundo, esp=3, rx=12))
        rs += [rot(x + 18, 98, t, w=w - 36, tam=24, cor=cor if cor != MUDO else TINTA, peso=700), rot(x + 18, 150, d, w=w - 36, tam=22, cor=TINTA, lh=1.25)]
    p.append(icone("t:lock", 360, 196, 40, MUDO))
    p.append(icone("t:trending-up", 812, 196, 44, OXID))
    rs.append(rot(24, 290, "estar tomando quando a carga voltar", w=850, tam=24, cor=OXID, peso=700))
    p.append(caixa(940, 0, 724, 400, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:brain", 964, 18, 44, GLIC))
    rs += [rot(1020, 22, "Cognição", w=600, tam=28, cor=GLIC, peso=700, serif=True),
           rot(964, 90, "6 ensaios, 281 pessoas saudáveis", w=680, tam=23, cor=TINTA, peso=600),
           rot(964, 140, "memória de curto prazo, mais em idosos", w=680, tam=22, cor=TINTA),
           rot(964, 200, "sinal real e modesto", w=680, tam=24, cor=GLIC, peso=700)]
    p.append(caixa(964, 270, 676, 90, FOSF, CARTAO, esp=2, rx=14))
    rs.append(rot(964, 298, "mecanismo não é indicação", w=676, tam=24, cor=FOSF, peso=700, alinha="center"))
    return slide("alem", 400, p, rs,
                 eyebrow="Um experimento de 2001 · uma meta-análise de 2018", titulo="Além do desempenho, com sobriedade",
                 destaque="Entre “tem mecanismo e estudos em andamento” e “está indicado” mora boa parte do marketing de suplemento.",
                 destaque_cor="tinta", fonte="Hespel e colaboradores · Journal of Physiology 2001 · Avgerinos e colaboradores · Experimental Gerontology 2018")


def protocolo():
    """5.2: a receita da creatina em seis campos."""
    p = [svg_abre(1664, 400, "Seis campos de uma receita. Forma: monoidratada, a dos estudos e a mais barata. Dose: 3 a 5 gramas por dia; carga de cerca de 20 gramas por 5 a 6 dias só se houver pressa, em quatro tomadas. Horário: o que a pessoa lembrar; adesão vale mais que horário. Com líquido, e numa refeição se incomodar; desconforto quase sempre é dose alta de uma vez. Dias sem treino: toma igual, a linha mais esquecida. Por quanto tempo: enquanto houver objetivo, com pote simples, de um ingrediente")]
    campos = [("t:pill", "Forma", "monoidratada", "a dos estudos e a mais barata; as outras não mostraram superioridade", OXID),
              ("t:scale", "Dose", "3 a 5 g por dia", "carga de ~20 g por 5 a 6 dias só se houver pressa, em quatro tomadas", OXID),
              ("t:clock", "Horário", "o que a pessoa lembrar", "adesão vale mais que horário", OXID),
              ("t:droplet", "Como", "com líquido; numa refeição se incomodar", "desconforto quase sempre é dose alta de uma vez", GLIC),
              ("t:calendar", "Dias sem treino", "toma igual", "a linha mais esquecida", GLIC),
              ("t:repeat", "Por quanto tempo", "enquanto houver objetivo", "pote simples, um ingrediente, controle verificável", TINTA)]
    rs = []
    for k, (ic, rot_, v, d, cor) in enumerate(campos):
        x, y = (k % 3) * 568, (k // 3) * 208
        p.append(caixa(x, y, 528, 190, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, x + 20, y + 20, 40, cor))
        rs += [rot(x + 72, y + 26, rot_, w=440, tam=20, cor=MUDO, peso=700),
               rot(x + 20, y + 72, v, w=490, tam=25, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 20, y + 128, d, w=490, tam=19, cor=TINTA, lh=1.25)]
    return slide("protocolo", 400, p, rs,
                 eyebrow="O protocolo prático", titulo="Seis linhas")


# ---------------------------------------------------------------- 5.3

def pergunta_53():
    """5.3: as quatro perguntas que sobram quando a resposta é funciona, e os três perfis."""
    p = [svg_abre(1664, 300, "À esquerda, as quatro perguntas que sobram quando a resposta é funciona: quanto, quando, para quem, e trocando o quê. À direita, três perfis típicos: quem treina às nove da noite e só sobrou a cafeína do pote; a jogadora de vôlei com jogo às nove e meia; e o ciclista hipertenso com quatro cafés, pré-treino e gel, que nunca somou nada")]
    rs = []
    for k, t in enumerate(["Quanto?", "Quando?", "Para quem?", "Trocando o quê?"]):
        x, y = (k % 2) * 380, (k // 2) * 154
        p.append(caixa(x, y, 350, 140, OXID if k < 3 else FOSF, OXID_T if k < 3 else FOSF_T, esp=3, rx=16))
        rs.append(rot(x, y + 48, t, w=350, tam=34, cor=OXID if k < 3 else FOSF, peso=700, alinha="center", serif=True))
    perfis = [("t:moon", "treina às 21h", "só sobrou a cafeína do pote"), ("t:ball-volleyball", "vôlei às 21h30", "jogo decisivo à noite"), ("t:bike", "ciclista hipertenso", "quatro cafés, pré-treino e gel, nunca somados")]
    for k, (ic, t, d) in enumerate(perfis):
        y = k * 104
        p.append(caixa(820, y, 844, 92, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 844, y + 20, 52, TINTA))
        rs += [rot(916, y + 12, t, w=720, tam=26, cor=TINTA, peso=700, serif=True), rot(916, y + 52, d, w=720, tam=21, cor=MUDO)]
    return slide("pergunta", 300, p, rs,
                 eyebrow="Três perfis típicos", titulo="Funciona. Então a pergunta é outra.")


def mecanismo():
    """5.3: a cafeína ocupa o receptor e o sinal de cansaço não chega."""
    p = [svg_abre(1664, 400, "À esquerda, o que a evidência sustenta: 21 meta-análises reunidas, com efeito em resistência aeróbica e muscular, força e potência; efeito pequeno, que decide pódio e some no amador. À direita, o mecanismo: a cafeína ocupa o receptor de adenosina, e a adenosina, que sinaliza cansaço, fica de fora. Não queima gordura de forma relevante; adia a percepção de que a energia acaba")]
    p.append(caixa(0, 0, 700, 400, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "O que a evidência sustenta", w=650, tam=27, cor=OXID, peso=700, serif=True),
          rot(24, 70, "21", w=200, tam=64, cor=OXID, peso=700, serif=True), rot(130, 92, "meta-análises reunidas", w=540, tam=23, cor=TINTA)]
    for k, t in enumerate(["resistência aeróbica e muscular", "força e potência"]):
        p.append(icone("t:check", 24, 170 + k * 56, 36, OXID))
        rs.append(rot(72, 174 + k * 56, t, w=600, tam=22, cor=TINTA))
    rs.append(rot(24, 300, "efeito pequeno: decide pódio, some no amador", w=650, tam=22, cor=GLIC, peso=700))
    cx = 900
    p.append(f'<path d="M {cx - 90} 160 v 140 h 180 v -140 h -50 v 90 h -80 v -90 z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
    rs.append(rot(cx - 150, 316, "receptor de adenosina", w=300, tam=20, cor=AZUL, peso=700, alinha="center"))
    p.append(f'<rect x="{cx - 36}" y="168" width="72" height="80" rx="10" fill="{GLIC}"/>')
    rs.append(rot(cx - 100, 130, "cafeína", w=200, tam=22, cor=GLIC, peso=700, alinha="center"))
    p.append(f'<circle cx="{cx + 190}" cy="110" r="44" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3" stroke-dasharray="8 6"/>')
    rs.append(rot(cx + 100, 162, "adenosina: o sinal de cansaço fica de fora", w=180, tam=19, cor=MUDO, alinha="center", lh=1.2))
    rs += [rot(1260, 60, "não queima gordura de forma relevante", w=400, tam=22, cor=TINTA, lh=1.25),
           rot(1260, 200, "adia a percepção de que a energia acaba", w=400, tam=24, cor=GLIC, peso=700, lh=1.25)]
    return slide("mecanismo", 400, p, rs,
                 eyebrow="Uma revisão de 2020 · um posicionamento de 2021", titulo="Ela não cria energia",
                 destaque="O que o amador sente não é velocidade: é que o treino pareceu mais fácil. E a conta do cansaço continua existindo.",
                 destaque_cor="tinta", fonte="Grgic e colaboradores · British Journal of Sports Medicine 2020 · Guest e colaboradores · Journal of the International Society of Sports Nutrition 2021")


def fonte_53():
    """5.3: cinco fontes de cafeína e o quanto cada uma deixa a dose previsível."""
    p = [svg_abre(1664, 400, "Cinco fontes de cafeína, com um medidor de quanto a dose é previsível. Cápsula de cafeína anidra: sim, é o que os estudos usam. Gel e bebida esportiva: sim, no rótulo, práticos durante o esforço. Goma de mascar: sim, com absorção mais rápida. Café coado: não, varia com pó, grão, moagem e tempo. Energético: em parte, vem com açúcar e outros componentes")]
    linhas = [("t:pill", "Cápsula de cafeína anidra", 3, "sim", "é o que os estudos usam"),
              ("t:bolt", "Gel e bebida esportiva", 3, "sim, no rótulo", "práticos durante o esforço"),
              ("t:candy", "Goma de mascar", 3, "sim", "absorção mais rápida"),
              ("t:coffee", "Café coado", 0, "não", "varia com pó, grão, moagem e tempo"),
              ("t:battery-4", "Energético", 2, "em parte", "vem com açúcar e outros componentes")]
    rs = [rot(560, 0, "dose previsível?", w=300, tam=19, cor=MUDO, peso=700)]
    for k, (ic, t, n, v, obs) in enumerate(linhas):
        y = 36 + k * 72
        cor = OXID if n == 3 else (GLIC if n else FOSF)
        p.append(f'<line x1="0" y1="{y + 64}" x2="1664" y2="{y + 64}" stroke="{BORDA}" stroke-width="2"/>')
        p.append(icone(ic, 0, y + 12, 40, TINTA))
        rs.append(rot(56, y + 18, t, w=480, tam=23, cor=TINTA, peso=700))
        for j in range(3):
            p.append(f'<rect x="{560 + j * 46}" y="{y + 18}" width="38" height="26" rx="6" fill="{cor if j < n else CINZA}"/>')
        rs += [rot(710, y + 18, v, w=200, tam=21, cor=cor, peso=700), rot(930, y + 18, obs, w=730, tam=21, cor=TINTA)]
    return slide("fonte", 400, p, rs,
                 eyebrow="A fonte, e a soma", titulo="A dose só existe se a fonte for previsível",
                 destaque="Quatro cafés, um pré-treino e um gel não são três decisões. São uma dose só. Somar em voz alta é o primeiro trabalho da consulta.",
                 destaque_cor="ambar")


def sono():
    """5.3: três horários de dose antes de deitar, e mesmo o mais distante custou sono."""
    p = [svg_abre(1664, 400, "Uma linha do tempo até a hora de deitar, com três horários de 400 miligramas de cafeína: na hora de deitar, 3 horas antes e 6 horas antes. Uma curva de queda em esquema parte da dose de 6 horas antes e ainda está longe de zero quando a pessoa deita. Mesmo nesse horário, o sono total medido caiu mais de uma hora. A meia-vida fica em torno de 5 horas, com faixa larga")]
    import math
    X0, X1, B, T = 60, 1180, 330, 60
    X = lambda h: X0 + (h + 6) / 9 * (X1 - X0)
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X1}" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    rs = []
    for h, t in [(-6, "6 h antes"), (-3, "3 h antes"), (0, "deitar")]:
        p.append(f'<line x1="{X(h):.0f}" y1="{B}" x2="{X(h):.0f}" y2="{B + 12}" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(h) - 80, B + 16, t, w=160, tam=20, cor=TINTA if h else AZUL, peso=700, alinha="center"))
        p.append(f'<circle cx="{X(h):.0f}" cy="{T + 10}" r="12" fill="{GLIC if h == -6 else CINZA}"/>')
    rs.append(rot(X0 - 40, T - 50, "400 mg, três horários testados", w=500, tam=20, cor=MUDO))
    pts = [(X(-6 + i * 0.25), B - (B - T - 30) * math.exp(-math.log(2) * i * 0.25 / 5)) for i in range(37)]
    p.append(f'<polyline points="{" ".join(f"{a:.0f},{b:.0f}" for a, b in pts)}" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    p.append(f'<rect x="{X(0):.0f}" y="{T}" width="{X(3) - X(0):.0f}" height="{B - T}" fill="{AZUL_T}"/>')
    p.append(icone("t:moon", X(1.5) - 28, B - 120, 56, AZUL))
    rs += [rot(X(0), T + 10, "sono", w=X(3) - X(0), tam=22, cor=AZUL, peso=700, alinha="center"),
           rot(X(-5.6), B - 90, "a cafeína ainda está lá ao deitar", w=420, tam=21, cor=GLIC, peso=700),
           rot(X0, B + 50, "curva: esquema com meia-vida de cerca de 5 h", w=600, tam=18, cor=MUDO)]
    p.append(caixa(1260, 40, 404, 290, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(1260, 70, "> 1 h", w=404, tam=64, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(1284, 170, "a menos de sono total medido, mesmo com a dose 6 h antes", w=356, tam=22, cor=TINTA, alinha="center", lh=1.3)]
    return slide("sono", 400, p, rs,
                 eyebrow="Um experimento de 2013", titulo="O custo está na meia-vida",
                 destaque="Meia-vida em torno de 5 horas, com faixa larga: mais longa com anticoncepcional oral e na gestação, mais curta em fumantes.",
                 destaque_cor="petr", fonte="Drake e colaboradores · Journal of Clinical Sleep Medicine 2013")


def genetica():
    """5.3: barras de mudança no tempo por genótipo, a partir do zero."""
    p = [svg_abre(1664, 360, "Barras de mudança no tempo de 10 quilômetros de bicicleta, a partir do zero. Genótipo AA com 2 miligramas por quilo: 4,8% mais rápido. Genótipo AA com 4 miligramas por quilo: 6,8% mais rápido. Genótipo CC com 4 miligramas por quilo: 13,7% mais lento")]
    Z, K = 620, 40
    barras = [("AA, 2 mg/kg", -4.8, OXID), ("AA, 4 mg/kg", -6.8, OXID), ("CC, 4 mg/kg", 13.7, FOSF)]
    rs = []
    for k, (t, v, cor) in enumerate(barras):
        y = 50 + k * 96
        x0 = Z + min(0, v) * K
        p.append(f'<rect x="{x0:.0f}" y="{y}" width="{abs(v) * K:.0f}" height="60" rx="6" fill="{cor}"/>')
        rs.append(rot(0, y + 16, t, w=320, tam=25, cor=TINTA, peso=700))
        lab = f"{v:+.1f}%".replace(".", ",").replace("-", "−")
        if v < 0:
            rs.append(rot(x0 - 150, y + 14, lab, w=140, tam=26, cor=cor, peso=700, alinha="right"))
        else:
            rs.append(rot(Z + v * K + 14, y + 14, lab, w=160, tam=26, cor=cor, peso=700))
    p.append(f'<line x1="{Z}" y1="30" x2="{Z}" y2="340" stroke="{TINTA}" stroke-width="3"/>')
    rs += [rot(Z - 400, 0, "← mais rápido", w=380, tam=20, cor=OXID, peso=700, alinha="right"),
           rot(Z + 20, 0, "mais lento →", w=380, tam=20, cor=FOSF, peso=700)]
    return slide("genetica", 360, p, rs,
                 eyebrow="Um estudo de 2018 · 101 atletas, 10 km de bicicleta", titulo="Genética: achado real, sem teste de balcão",
                 destaque="Outros estudos não replicaram de forma consistente. E a conduta seria a mesma: testar a dose em treino. O teste barato já existe, e se chama treino.",
                 destaque_cor="tinta", fonte="Guest e colaboradores · Medicine and Science in Sports and Exercise 2018")


def habito():
    """5.3: três níveis de hábito, o mesmo ganho, e quem passa mal."""
    p = [svg_abre(1664, 400, "À esquerda, 40 ciclistas em três níveis de consumo habitual, cerca de 60, 140 e 350 miligramas por dia, em barras. Todos tomaram 6 miligramas por quilo antes do contrarrelógio, e o ganho foi o mesmo nos três grupos, desenhado como três setas iguais. A semana de abstinência não se justifica. À direita, quem passa mal: ansiedade, tremor, palpitação, náusea, urgência intestinal, dor de cabeça e insônia; para essa pessoa, não usar"), defs(OXID)]
    rs = [rot(0, 0, "40 ciclistas, consumo habitual por dia", w=900, tam=22, cor=MUDO, peso=700)]
    B = 300
    for k, v in enumerate([60, 140, 350]):
        x = 40 + k * 300
        h = v * 0.6
        p.append(f'<rect x="{x}" y="{B - h:.0f}" width="140" height="{h:.0f}" rx="6" fill="{GLIC}"/>')
        rs.append(rot(x - 30, B + 10, f"≈ {v} mg", w=200, tam=22, cor=GLIC, peso=700, alinha="center"))
        p.append(seta(x + 200, B - 20, x + 200, 70, OXID, "m0", esp=6))
    p.append(f'<line x1="20" y1="{B}" x2="900" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(0, 350, "6 mg/kg antes do contrarrelógio: o mesmo ganho nos três", w=900, tam=22, cor=OXID, peso=700)]
    p.append(caixa(980, 0, 684, 400, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(1004, 18, "Quem passa mal", w=640, tam=28, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["ansiedade, tremor, palpitação", "náusea, urgência intestinal", "dor de cabeça, insônia"]):
        p.append(f'<circle cx="1018" cy="{100 + k * 62}" r="8" fill="{FOSF}"/>')
        rs.append(rot(1038, 86 + k * 62, t, w=600, tam=23, cor=TINTA))
    p.append(caixa(1004, 300, 636, 76, FOSF, FOSF, esp=0, rx=38))
    rs.append(rot(1004, 320, "para essa pessoa: não usar", w=636, tam=25, cor=PAPEL, peso=700, alinha="center"))
    return slide("habito", 400, p, rs,
                 eyebrow="Um estudo de 2017", titulo="Hábito não apaga o efeito",
                 destaque="A semana de abstinência não se justifica. A cafeína do dia de prova é sempre a dose testada em treino.",
                 destaque_cor="ambar", fonte="Gonçalves, Gualano e colaboradores · Journal of Applied Physiology 2017")


def limites():
    """5.3: a dose de desempenho no centro e as seis fronteiras onde a decisão muda de natureza."""
    p = [svg_abre(1664, 400, "No centro, a decisão de desempenho. Em volta, seis fronteiras onde ela deixa de ser de desempenho. Pó a granel: dose em miligramas, venda em gramas, com mortes documentadas por erro de colher. Gestação: teto em torno de 200 miligramas por dia, meia-vida maior, decisão médica. Crianças e adolescentes: sem indicação ergogênica, energético desaconselhado. Coração: hipertensão não controlada, arritmia, palpitação, doença conhecida. Soma de estimulantes: pré-treino, café, energético e termogênico, a dose que ninguém pretendeu. Antidoping: não é proibida, está em monitoramento, e há regras de federação")]
    cx, cy = 832, 200
    nos = [(0, 0, "t:alert-triangle", "Pó a granel", "dose em miligramas, venda em gramas; mortes documentadas por erro de colher", FOSF, FOSF_T),
           (0, 140, "h:woman", "Gestação", "teto em torno de 200 mg/dia; meia-vida maior; decisão médica", GLIC, GLIC_T),
           (0, 280, "h:child-program", "Crianças e adolescentes", "sem indicação ergogênica; energético desaconselhado", GLIC, GLIC_T),
           (1044, 0, "t:heartbeat", "Coração", "hipertensão não controlada, arritmia, palpitação, doença conhecida", FOSF, FOSF_T),
           (1044, 140, "t:bolt", "Soma de estimulantes", "pré-treino, café, energético, termogênico: a dose que ninguém pretendeu", FOSF, FOSF_T),
           (1044, 280, "t:shield", "Antidoping", "não é proibida; está em monitoramento; há regras de federação", TINTA, CARTAO)]
    rs = []
    for x, y, ic, t, d, cor, fundo in nos:
        ax = x + 620 if x == 0 else x
        p.append(f'<line x1="{ax}" y1="{y + 60}" x2="{cx + (-80 if x == 0 else 80)}" y2="{cy + (y + 60 - cy) * 0.4:.0f}" stroke="{BORDA}" stroke-width="3"/>')
        p.append(caixa(x, y, 620, 120, cor, fundo, esp=3, rx=14))
        p.append(icone(ic, x + 18, y + 16, 38, cor))
        rs += [rot(x + 68, y + 20, t, w=530, tam=24, cor=cor, peso=700, serif=True), rot(x + 20, y + 62, d, w=580, tam=19, cor=TINTA, lh=1.25)]
    p.append(f'<circle cx="{cx}" cy="{cy}" r="90" fill="{OXID}"/>')
    rs.append(rot(cx - 80, cy - 26, "decisão de desempenho", w=160, tam=21, cor=PAPEL, peso=700, alinha="center", lh=1.2))
    return slide("limites", 400, p, rs,
                 eyebrow="Onde a decisão deixa de ser de desempenho", titulo="Os limites")


def decisoes_53():
    """5.3: cada perfil, o que decide e a decisão."""
    p = [svg_abre(1664, 380, "Três perfis, cada um ligado ao que decide e à decisão. Quem treina às 21 horas: o sono é a causa da falta de disposição; não usar como pré-treino, e cuidar de jantar, horário e sono. A jogadora de vôlei às 21h30: decide se o jogo é decisivo ou de calendário; dose baixa só no decisivo, ciente da noite pior. O ciclista hipertenso: decide a soma do dia; somar em voz alta, cortar o pré-treino e tratar a pressão com o médico"), defs(MUDO)]
    linhas = [("t:moon", "Treina às 21h", "o sono é a causa da falta de disposição", "não usar como pré-treino; jantar, horário e sono", FOSF),
              ("t:ball-volleyball", "Vôlei às 21h30", "jogo decisivo ou de calendário", "dose baixa só no decisivo, ciente da noite pior", GLIC),
              ("t:bike", "Ciclista hipertenso", "a soma do dia", "somar em voz alta; cortar o pré-treino; pressão com o médico", OXID)]
    rs = [rot(440, 0, "O que decide", w=400, tam=19, cor=MUDO, peso=700), rot(1000, 0, "Decisão", w=400, tam=19, cor=MUDO, peso=700)]
    for k, (ic, t, dec, d, cor) in enumerate(linhas):
        y = 36 + k * 118
        p.append(caixa(0, y, 400, 100, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 20, y + 26, 48, TINTA))
        rs.append(rot(84, y + 34, t, w=300, tam=24, cor=TINTA, peso=700, serif=True))
        p.append(seta(406, y + 50, 432, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(440, y, 500, 100, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(460, y + 22, dec, w=460, tam=22, cor=TINTA, lh=1.3))
        p.append(seta(946, y + 50, 992, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(1000, y, 664, 100, cor, OXID_T if cor == OXID else (GLIC_T if cor == GLIC else FOSF_T), esp=3, rx=14))
        rs.append(rot(1020, y + 22, d, w=624, tam=22, cor=cor, peso=700, lh=1.3))
    return slide("decisoes", 380, p, rs,
                 eyebrow="As três decisões", titulo="O que decide cada perfil",
                 destaque="A cafeína não é o problema principal do ciclista, mas é a parte que ele controla e que ninguém tinha contado.",
                 destaque_cor="petr")



# ---------------------------------------------------------------- 5.4

import math

def regua_duracao(p, rs, X0, X1, y, janela=True):
    """Régua logarítmica de duração do esforço, de 5 segundos a 3 horas; devolve X(segundos)."""
    X = lambda t: X0 + (math.log10(t) - math.log10(5)) / (math.log10(10800) - math.log10(5)) * (X1 - X0)
    if janela:
        p.append(f'<rect x="{X(30):.0f}" y="{y - 46}" width="{X(600) - X(30):.0f}" height="92" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{MUDO}" stroke-width="3"/>')
    for t, lab in [(10, "10 s"), (30, "30 s"), (60, "1 min"), (600, "10 min"), (3600, "1 h"), (10800, "3 h")]:
        p.append(f'<line x1="{X(t):.0f}" y1="{y - 8}" x2="{X(t):.0f}" y2="{y + 8}" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(t) - 50, y + 54, lab, w=100, tam=18, cor=MUDO, alinha="center"))
    return X


def formigamento():
    """5.4: a frase do paciente e os dois erros de número dentro dela."""
    p = [svg_abre(1664, 360, "Um balão com a frase de quem parou no terceiro dia: não senti nada, só um formigamento. Embaixo, os dois erros de número. Primeiro: esperava efeito no dia, e a beta-alanina funciona por acúmulo, em semanas. Segundo: leu o formigamento como falha, quando é parestesia esperada, resolvida pela dose"), defs(MUDO)]
    p.append(f'<path d="M 0 30 a 30 30 0 0 1 30 -30 h 1000 a 30 30 0 0 1 30 30 v 70 a 30 30 0 0 1 -30 30 h -880 l -50 40 l 10 -40 h -80 a 30 30 0 0 1 -30 -30 z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    rs = [rot(30, 36, "“Não senti nada, só um formigamento.”", w=1000, tam=32, cor=TINTA, peso=700, serif=True),
          rot(1100, 40, "parou no terceiro dia", w=560, tam=26, cor=FOSF, peso=700)]
    erros = [(0, "esperava efeito no dia", "funciona por acúmulo, em semanas"), (852, "leu o formigamento como falha", "é parestesia esperada, resolvida pela dose")]
    for x, a, b in erros:
        p.append(caixa(x, 200, 812, 150, FOSF, FOSF_T, esp=3, rx=14))
        p.append(icone("t:x", x + 20, 222, 36, FOSF))
        rs.append(rot(x + 70, 224, a, w=720, tam=24, cor=FOSF, peso=700))
        p.append(seta(x + 40, 272, x + 40, 316, MUDO, "m0", esp=3))
        rs.append(rot(x + 70, 296, b, w=720, tam=24, cor=OXID, peso=700))
    return slide("formigamento", 360, p, rs,
                 eyebrow="Perfil típico", titulo="Parou no terceiro dia, por dois erros de número")


def acumulo():
    """5.4: a carnosina sobe em semanas, com os dois pontos medidos."""
    p = [svg_abre(1664, 400, "Um gráfico de carnosina muscular ao longo de 10 semanas. Dois pontos medidos: mais 59% em 4 semanas e mais 80% em 10 semanas, ligados por linha. Marcados no eixo, 3 dias e 15 dias, perto do começo. À direita, o trabalho total no teste de bicicleta: mais 13% em 4 semanas")]
    X0, X1, B, T = 120, 1040, 330, 30
    X = lambda w: X0 + w / 10 * (X1 - X0)
    Y = lambda v: B - v / 100 * (B - T)
    rs = [rot(0, T - 10, "carnosina muscular", w=110, tam=18, cor=MUDO, lh=1.2)]
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X1}" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="{X0}" y1="{T}" x2="{X0}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<polyline points="{X(0):.0f},{Y(0):.0f} {X(4):.0f},{Y(59):.0f} {X(10):.0f},{Y(80):.0f}" fill="none" stroke="{OXID}" stroke-width="4"/>')
    for w, v, cor in [(4, 59, GLIC), (10, 80, OXID)]:
        p.append(f'<circle cx="{X(w):.0f}" cy="{Y(v):.0f}" r="12" fill="{cor}"/>')
        rs.append(rot(X(w) - 120, Y(v) - 52, f"+{v}%", w=240, tam=34, cor=cor, peso=700, alinha="center", serif=True))
    for w in [0, 4, 10]:
        rs.append(rot(X(w) - 70, B + 12, f"{w} semanas" if w else "início", w=140, tam=19, cor=MUDO, alinha="center"))
    for d, t in [(3, "3 dias"), (15, "15 dias")]:
        x = X(d / 7)
        p.append(f'<line x1="{x:.0f}" y1="{B - 60}" x2="{x:.0f}" y2="{B}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
        rs.append(rot(x - 60, B - 92, t, w=120, tam=19, cor=FOSF, peso=700, alinha="center"))
    rs.append(rot(X0, B + 44, "pontos medidos; a linha só os liga", w=600, tam=17, cor=MUDO))
    p.append(caixa(1140, 40, 524, 290, TINTA, CARTAO, esp=3, rx=16))
    p.append(icone("t:bike", 1164, 64, 52, TINTA))
    rs += [rot(1140, 140, "+13%", w=524, tam=64, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(1164, 236, "trabalho total no teste de bicicleta, em 4 semanas", w=476, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    return slide("acumulo", 400, p, rs,
                 eyebrow="Um experimento de 2007", titulo="Quatro semanas é o começo, não o fim",
                 destaque="Quem toma quinze dias e para não chegou à metade do caminho. Quem toma três dias não testou nada.",
                 destaque_cor="verm", fonte="Hill e colaboradores · 13 homens, biópsia muscular · Amino Acids 2007")


def tamanho():
    """5.4: o mesmo efeito pequeno em dois lugares, e onde os estudos medem."""
    p = [svg_abre(1664, 400, "À esquerda, o mesmo efeito pequeno em dois lugares: num 800 metros, decide a prova; num treino de academia, não se percebe. À direita, o desenho dos estudos, em esquema: muitos ganhos em testes de capacidade, como tempo sustentado e trabalho total, e menos em provas cronometradas reais")]
    lugares = [(0, "t:trophy", "num 800 m", "decide a prova", OXID, OXID_T), (0, "t:barbell", "num treino de academia", "não se percebe", MUDO, PAPEL)]
    rs = [rot(0, 0, "O mesmo efeito, pequeno", w=760, tam=26, cor=TINTA, peso=700, serif=True)]
    for k, (_, ic, t, d, cor, fundo) in enumerate(lugares):
        y = 60 + k * 170
        p.append(caixa(0, y, 760, 150, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, 30, y + 40, 64, cor))
        rs += [rot(120, y + 34, t, w=620, tam=26, cor=TINTA, peso=700), rot(120, y + 82, d, w=620, tam=28, cor=cor if cor != MUDO else TINTA, peso=700, serif=True)]
    rs.append(rot(860, 0, "Onde os estudos medem", w=780, tam=26, cor=TINTA, peso=700, serif=True))
    for k, (t, d, frac, cor) in enumerate([("testes de capacidade", "tempo sustentado, trabalho total", 0.85, GLIC), ("provas cronometradas reais", "menos ganhos", 0.35, MUDO)]):
        y = 90 + k * 140
        rs += [rot(860, y, t, w=780, tam=24, cor=TINTA, peso=700), rot(860, y + 34, d, w=780, tam=20, cor=MUDO)]
        p.append(f'<rect x="860" y="{y + 70}" width="780" height="34" rx="8" fill="{CINZA}"/>')
        p.append(f'<rect x="860" y="{y + 70}" width="{780 * frac:.0f}" height="34" rx="8" fill="{cor}"/>')
    rs.append(rot(860, 380, "barras: esquema", w=300, tam=17, cor=MUDO))
    return slide("tamanho", 400, p, rs,
                 eyebrow="A magnitude, sem propaganda", titulo="Real, e menor do que o rótulo sugere",
                 destaque="Efeito medido com precisão em laboratório não é garantia do mesmo efeito na rua.",
                 destaque_cor="tinta")


def protocolo_54():
    """5.4: o dia com doses divididas e as semanas até o estoque subir."""
    p = [svg_abre(1664, 400, "À esquerda, um dia com três tomadas de cerca de 1,6 grama, de manhã, à tarde e à noite: 4 a 6 gramas por dia, todos os dias. À direita, uma régua de semanas: a partir de 4 semanas há efeito, e o estoque continua subindo por 10 semanas ou mais")]
    p.append(caixa(0, 0, 720, 400, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 18, "Um dia", w=600, tam=27, cor=OXID, peso=700, serif=True)]
    p.append(f'<line x1="60" y1="170" x2="660" y2="170" stroke="{MUDO}" stroke-width="3"/>')
    for k, (h, t) in enumerate([(8, "manhã"), (14, "tarde"), (20, "noite")]):
        x = 60 + (h - 6) / 16 * 600
        p.append(icone("t:pill", x - 24, 100, 48, OXID))
        p.append(f'<circle cx="{x:.0f}" cy="170" r="9" fill="{OXID}"/>')
        rs += [rot(x - 80, 186, t, w=160, tam=19, cor=MUDO, alinha="center"), rot(x - 80, 64, "≈ 1,6 g", w=160, tam=20, cor=OXID, peso=700, alinha="center")]
    rs += [rot(24, 250, "4 a 6 g por dia", w=670, tam=40, cor=OXID, peso=700, serif=True), rot(24, 320, "todos os dias, dividida ao longo do dia", w=670, tam=22, cor=TINTA)]
    X0, X1 = 800, 1620
    X = lambda w: X0 + w / 12 * (X1 - X0)
    rs.append(rot(X0, 0, "As semanas", w=600, tam=27, cor=GLIC, peso=700, serif=True))
    p.append(f'<rect x="{X(4):.0f}" y="120" width="{X(12) - X(4):.0f}" height="80" rx="10" fill="{GLIC_T}"/>')
    p.append(f'<line x1="{X0}" y1="200" x2="{X1}" y2="200" stroke="{MUDO}" stroke-width="3"/>')
    for w in [0, 4, 8, 12]:
        p.append(f'<line x1="{X(w):.0f}" y1="192" x2="{X(w):.0f}" y2="208" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(w) - 50, 214, f"{w} sem", w=100, tam=18, cor=MUDO, alinha="center"))
    rs += [rot(X(4) + 14, 132, "≥ 4 semanas: efeito", w=500, tam=23, cor=GLIC, peso=700),
           rot(X0, 280, "o estoque sobe por 10 semanas ou mais", w=820, tam=23, cor=TINTA)]
    return slide("protocolo", 400, p, rs,
                 eyebrow="O posicionamento de 2015", titulo="O protocolo",
                 destaque="Quem vai competir começa pelo menos um mês antes, idealmente dois ou três.",
                 destaque_cor="petr", fonte="Trexler e colaboradores · Journal of the International Society of Sports Nutrition 2015")


def notas_54():
    """5.4: a parestesia e sua solução, e três notas de uso."""
    p = [svg_abre(1664, 400, "À esquerda, a parestesia: formigamento no rosto, pescoço e orelhas, curto, o único efeito adverso relatado; a solução é dividir a dose ou usar liberação prolongada. À direita, três notas: o total acumulado importa mais que o dia; quando para, cai devagar, e alguns dias esquecidos não apagam nada; e é uso diário, em qualquer horário, não um pré-treino, embora seja vendida dentro de um"), defs(OXID)]
    p.append(caixa(0, 0, 760, 400, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("h:head", 30, 70, 130, GLIC))
    rs = [rot(24, 18, "Parestesia", w=600, tam=28, cor=GLIC, peso=700, serif=True),
          rot(190, 80, "rosto, pescoço, orelhas; curta; o único efeito adverso relatado", w=540, tam=22, cor=TINTA, lh=1.3)]
    p.append(seta(380, 190, 380, 250, OXID, "m0", esp=4))
    p.append(caixa(24, 262, 712, 110, OXID, CARTAO, esp=3, rx=14))
    rs.append(rot(48, 282, "dividir a dose, ou liberação prolongada", w=670, tam=25, cor=OXID, peso=700, lh=1.25))
    notas = [("t:chart-line", "O total acumulado importa mais que o dia", "a carga ao longo das semanas enche o estoque", OXID),
             ("t:trending-down", "Quando para, cai devagar", "alguns dias esquecidos não apagam nada", OXID),
             ("t:calendar", "Uso diário, qualquer horário", "não é pré-treino, embora seja vendida dentro de um", TINTA)]
    for k, (ic, t, d, cor) in enumerate(notas):
        y = k * 136
        p.append(caixa(820, y, 844, 124, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 844, y + 22, 40, cor))
        rs += [rot(900, y + 22, t, w=740, tam=24, cor=cor, peso=700), rot(900, y + 66, d, w=740, tam=21, cor=TINTA)]
    return slide("notas", 400, p, rs,
                 eyebrow="Parestesia e três notas", titulo="O formigamento se resolve com dose")


def onde():
    """5.4: a janela de duração, com o que fica dentro e o que fica fora."""
    p = [svg_abre(1664, 400, "Uma régua de duração do esforço, de segundos a horas, com a janela de 30 segundos a 10 minutos destacada. Dentro dela: 400 e 800 metros, 200 metros de natação, remo de 2.000 metros, perseguição e lutas; intermitentes, com evidência mais heterogênea. Fora, à esquerda: salto, uma repetição máxima e tiro curto. Fora, à direita: meia maratona e maratona. Embaixo, mais três notas: vegetarianos têm menos carnosina e mais espaço; não serve a quem quer sentir algo hoje; e não substitui condicionamento")]
    rs = []
    X = regua_duracao(p, rs, 40, 1620, 170)
    rs.append(rot(X(30), 70, "a janela: 30 s a 10 min", w=X(600) - X(30), tam=21, cor=OXID, peso=700, alinha="center"))
    dentro = [(55, "400 m"), (110, "800 m"), (130, "200 m nado"), (240, "lutas"), (270, "perseguição"), (400, "remo 2.000 m")]
    for k, (t, lab) in enumerate(dentro):
        p.append(f'<circle cx="{X(t):.0f}" cy="170" r="9" fill="{OXID}"/>')
        rs.append(rot(X(t) - 70, 136 if k % 2 == 0 else 186, lab, w=140, tam=17, cor=OXID, peso=700, alinha="center"))
    for t, lab in [(8, "salto, 1RM, tiro curto"), (5400, "meia maratona"), (10000, "maratona")]:
        p.append(f'<circle cx="{X(t):.0f}" cy="170" r="9" fill="{FOSF}"/>')
    rs += [rot(X(8) - 30, 100, "salto, 1RM, tiro curto", w=200, tam=18, cor=FOSF, peso=700, lh=1.2),
           rot(X(5400) - 200, 100, "meia e maratona", w=260, tam=18, cor=FOSF, peso=700, alinha="right")]
    notas = [("t:plant", "vegetarianos: menos carnosina, mais espaço", OXID), ("t:clock", "não serve a quem quer sentir algo hoje", FOSF), ("t:run", "não substitui condicionamento", FOSF)]
    for k, (ic, t, cor) in enumerate(notas):
        x = k * 568
        p.append(caixa(x, 290, 528, 100, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 20, 318, 40, cor))
        rs.append(rot(x + 74, 310, t, w=440, tam=21, cor=TINTA, lh=1.25))
    return slide("onde", 400, p, rs,
                 eyebrow="É só aplicar a janela", titulo="Onde vale, e onde não vale",
                 destaque="A capacidade de tamponamento se treina. A beta-alanina se soma a esse treino; não o substitui.",
                 destaque_cor="tinta")


def perfis_54():
    """5.4: os três perfis colocados na régua de duração."""
    p = [svg_abre(1664, 400, "A mesma régua de duração, com três perfis. A nadadora de 200 metros, com esforço de 2 a 3 minutos, cai no meio da janela: 4 a 6 gramas por dia, divididos, começando dois meses antes. O futsal, de tiros repetidos, está em parte: é defensável, com expectativa calibrada. O maratonista, com esforço de horas, fica fora: funciona, mas não para o que você faz")]
    rs = []
    X = regua_duracao(p, rs, 40, 1620, 150)
    perfis = [(150, "t:swimming", "Nadadora, 200 m", "no meio", "4 a 6 g/dia, divididos, dois meses antes", OXID),
              (None, "t:ball-football", "Futsal", "em parte", "defensável, com expectativa calibrada", GLIC),
              (10000, "t:run", "Maratonista", "fora", "“funciona, mas não para o que você faz”", FOSF)]
    for k, (t, ic, nome, onde_, cond, cor) in enumerate(perfis):
        x = k * 568
        if t:
            p.append(f'<circle cx="{X(t):.0f}" cy="150" r="14" fill="{cor}"/>')
            rs.append(rot(min(X(t) - 120, 1664 - 240), 56, nome, w=240, tam=19, cor=cor, peso=700, alinha="center"))
        else:
            for tt in [6, 8, 12]:
                p.append(f'<circle cx="{X(tt):.0f}" cy="150" r="9" fill="{cor}"/>')
            rs.append(rot(X(8) - 100, 92, "tiros repetidos", w=200, tam=19, cor=cor, peso=700, alinha="center"))
        p.append(caixa(x, 250, 528, 140, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, x + 20, 270, 40, cor))
        rs += [rot(x + 74, 274, f"{nome}: {onde_}", w=440, tam=22, cor=cor, peso=700), rot(x + 20, 322, cond, w=490, tam=20, cor=TINTA, lh=1.25)]
    return slide("perfis", 400, p, rs,
                 eyebrow="Três perfis típicos", titulo="Quem está na janela",
                 destaque="O dinheiro do maratonista rende mais em carboidrato durante a prova.", destaque_cor="ambar")


# ---------------------------------------------------------------- 5.5

def esqueleto():
    """5.5: onde cada recurso se perde, e os três perfis."""
    p = [svg_abre(1664, 360, "Dois quadros. No nitrato, o problema está na boca: as bactérias da boca fazem parte do mecanismo, e o antisséptico as elimina. No bicarbonato, o problema está no intestino: a dose é grande e o desconforto decide a prova. Embaixo, três perfis típicos: o ciclista do contrarrelógio, a judoca de lutas curtas, e a corredora que tomou uma colher de bicarbonato na manhã da prova")]
    rs = []
    for k, (t, onde_, d, ic, cor, fundo) in enumerate([("Nitrato", "na boca", "as bactérias da boca fazem parte do mecanismo", "t:message-circle", OXID, OXID_T),
                                                       ("Bicarbonato", "no intestino", "a dose é grande; o desconforto decide a prova", "t:mood-sick", GLIC, GLIC_T)]):
        x = k * 852
        p.append(caixa(x, 0, 812, 200, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, x + 30, 30, 64, cor))
        rs += [rot(x + 120, 30, t, w=660, tam=24, cor=TINTA, peso=700), rot(x + 120, 66, f"o problema está {onde_}", w=660, tam=32, cor=cor, peso=700, serif=True),
               rot(x + 30, 140, d, w=760, tam=21, cor=TINTA)]
    for k, (ic, t) in enumerate([("t:bike", "ciclista do contrarrelógio"), ("t:karate", "judoca de lutas curtas"), ("t:run", "corredora: colher de bicarbonato na manhã da prova")]):
        x = k * 568
        p.append(caixa(x, 240, 528, 110, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 20, 274, 40, TINTA))
        rs.append(rot(x + 74, 268, t, w=440, tam=21, cor=TINTA, lh=1.25))
    return slide("esqueleto", 360, p, rs,
                 eyebrow="Dois recursos de grupo A", titulo="No nitrato, o problema está na boca. No bicarbonato, no intestino.",
                 destaque="Baratos, com evidência decente, quase sempre usados errado. Nada disso se estreia no dia.", destaque_cor="tinta")


def inversao():
    """5.5: o ganho do nitrato cai à medida que o nível de treino sobe."""
    p = [svg_abre(1664, 400, "Uma régua de nível de treino, do amador ao atleta de elite de resistência, com barras de ganho do nitrato que diminuem para a direita, em esquema. Rende mais no menos treinado, no esforço submáximo prolongado, no intermitente de alta intensidade, e há uma linha de pesquisa em pessoas mais velhas. Rende menos no atleta de elite de resistência, com eficiência já alta e pouco espaço para melhorar")]
    rs = []
    B = 220
    for k in range(6):
        h = 170 - k * 26
        x = 40 + k * 140
        p.append(f'<rect x="{x}" y="{B - h}" width="100" height="{h}" rx="6" fill="{OXID if k < 3 else GLIC}"/>')
    p.append(f'<line x1="20" y1="{B}" x2="880" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    rs += [rot(20, B + 12, "amador", w=200, tam=21, cor=OXID, peso=700), rot(660, B + 12, "elite de resistência", w=220, tam=21, cor=GLIC, peso=700, alinha="right"),
           rot(20, B + 50, "ganho do nitrato · barras: esquema", w=600, tam=17, cor=MUDO)]
    for k, (t, itens, cor, fundo) in enumerate([("Rende mais", ["menos treinado, amador", "esforço submáximo prolongado", "intermitente de alta intensidade", "linha de pesquisa em pessoas mais velhas"], OXID, OXID_T),
                                                ("Rende menos", ["atleta de elite de resistência", "eficiência já alta", "pouco espaço para melhorar"], GLIC, GLIC_T)]):
        y = k * 210
        hh = 196 if k == 0 else 190
        p.append(caixa(940, y, 724, hh, cor, fundo, esp=3, rx=14))
        rs.append(rot(964, y + 12, t, w=680, tam=25, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            rs.append(rot(964 + (j % 2) * 340, y + 56 + (j // 2) * 64, it, w=330, tam=20, cor=TINTA, lh=1.2))
    return slide("inversao", 400, p, rs,
                 eyebrow="Uma revisão de 2014", titulo="A inversão: rende mais em quem é menos treinado",
                 destaque="Quase todo ergogênico rende mais no alto nível. O nitrato tende a render mais no público deste curso.",
                 destaque_cor="tinta", fonte="Jones · Sports Medicine 2014")


def nitrato():
    """5.5: a dose, as horas até o pico e os dias antes."""
    p = [svg_abre(1664, 400, "Uma linha do tempo do dia de prova. O shot com 5 a 9 milimoles de nitrato, cerca de 300 a 560 miligramas, é tomado 2 a 3 horas antes; o nitrito no sangue sobe devagar, em esquema, e chega perto do pico na largada. Quinze minutos antes não dá tempo. Acima, uma fileira de dias: mais de 3 dias de uso antes da competição parecem ajudar")]
    X0, X1, B = 60, 1180, 320
    X = lambda h: X0 + (h + 3.5) / 4.5 * (X1 - X0)
    rs = []
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X1}" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    for h, t in [(-3, "3 h antes"), (-2, "2 h antes"), (-1, "1 h antes"), (0, "largada")]:
        p.append(f'<line x1="{X(h):.0f}" y1="{B - 8}" x2="{X(h):.0f}" y2="{B + 8}" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(h) - 60, B + 14, t, w=120, tam=18, cor=MUDO, alinha="center"))
    p.append(f'<rect x="{X(-3):.0f}" y="{B - 40}" width="{X(-2) - X(-3):.0f}" height="40" rx="6" fill="{OXID}"/>')
    rs.append(rot(X(-3) - 20, B - 74, "o shot", w=X(-2) - X(-3) + 40, tam=20, cor=OXID, peso=700, alinha="center"))
    pts = [(X(-2.5 + i * 0.1), B - 200 * (1 - math.exp(-i * 0.1 / 0.9))) for i in range(26)]
    p.append(f'<polyline points="{" ".join(f"{a:.0f},{b:.0f}" for a, b in pts)}" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    rs += [rot(X(-1.6), B - 236, "nitrito no sangue: sobe devagar", w=420, tam=20, cor=GLIC, peso=700),
           rot(X0, B + 50, "curva: esquema", w=300, tam=17, cor=MUDO)]
    p.append(f'<line x1="{X(-0.25):.0f}" y1="{B - 120}" x2="{X(-0.25):.0f}" y2="{B}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    rs.append(rot(X(-0.25) - 230, B - 150, "15 min antes: não dá tempo", w=220, tam=18, cor=FOSF, peso=700, alinha="right"))
    for k in range(4):
        p.append(f'<rect x="{X0 + k * 50}" y="0" width="40" height="40" rx="6" fill="{TINTA if k < 3 else OXID}"/>')
    rs.append(rot(X0 + 220, 8, "> 3 dias de uso antes da competição parecem ajudar", w=700, tam=20, cor=TINTA))
    p.append(caixa(1260, 40, 404, 290, OXID, OXID_T, esp=3, rx=16))
    rs += [rot(1260, 76, "5 a 9 mmol", w=404, tam=44, cor=OXID, peso=700, alinha="center", serif=True),
           rot(1284, 150, "de nitrato, cerca de 300 a 560 mg", w=356, tam=22, cor=TINTA, alinha="center", lh=1.3),
           rot(1284, 230, "shot concentrado com dose no rótulo", w=356, tam=20, cor=MUDO, alinha="center", lh=1.3)]
    return slide("nitrato", 400, p, rs,
                 eyebrow="O protocolo do nitrato · consenso do COI, 2018", titulo="Duas a três horas, não quinze minutos",
                 destaque="Shot concentrado com dose no rótulo para o dia de prova. Folhas verde-escuras e beterraba no prato para o resto: comida primeiro continua valendo.",
                 destaque_cor="petr", fonte="Maughan e colaboradores · British Journal of Sports Medicine 2018")


def erros_55():
    """5.5: os cinco erros, cada um no ponto do caminho em que acontece."""
    p = [svg_abre(1664, 400, "Cinco erros do nitrato, cada um num ponto do caminho. Na boca: enxaguante, bala ou chiclete antisséptico; suspender nos dias de uso. No copo: suco caseiro como se fosse dose, quando o teor varia com solo, variedade e preparo. No relógio: tomar quinze minutos antes, sem tempo. Na urina: susto com urina ou fezes avermelhadas; é beterraba, e vale avisar antes. No intestino: volume concentrado perto do esforço; ensaiar")]
    itens = [("t:message-circle", "Enxaguante, bala ou chiclete antisséptico", "suspender nos dias de uso", FOSF),
             ("t:droplet", "Suco caseiro como se fosse dose", "o teor varia com solo, variedade e preparo", GLIC),
             ("t:clock", "Tomar quinze minutos antes", "não dá tempo", GLIC),
             ("t:alert-triangle", "Susto com urina ou fezes avermelhadas", "é beterraba; avisar antes", TINTA),
             ("t:mood-sick", "Esquecer o intestino", "volume concentrado perto do esforço: ensaiar", TINTA)]
    W = 300
    rs = []
    p.append(f'<line x1="40" y1="60" x2="1624" y2="60" stroke="{BORDA}" stroke-width="6" stroke-linecap="round"/>')
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * (W + 41)
        p.append(f'<circle cx="{x + W / 2:.0f}" cy="60" r="40" fill="{CARTAO}" stroke="{cor}" stroke-width="4"/>')
        p.append(icone(ic, x + W / 2 - 22, 38, 44, cor))
        p.append(caixa(x, 130, W, 260, cor, CARTAO, esp=2, rx=14))
        rs += [rot(x + 16, 148, t, w=W - 32, tam=22, cor=cor, peso=700, lh=1.2), rot(x + 16, 270, d, w=W - 32, tam=20, cor=TINTA, lh=1.3)]
    return slide("erros", 400, p, rs,
                 eyebrow="Os cinco erros do nitrato", titulo="Onde o protocolo se perde")


def bicarbonato():
    """5.5: a dose por quilo, a colher que ela vira e a janela de horário."""
    p = [svg_abre(1664, 400, "Três partes. A dose: uma régua de 0,2 a 0,5 grama por quilo, com o trecho de 0,2 a 0,3 marcado como o que se tolera melhor. A conta: para 70 quilos, com 0,2 a 0,3 grama por quilo, 14 a 21 gramas, muito pó. O horário: de 60 a 180 minutos antes, individualizado em treino")]
    rs = [rot(0, 0, "A dose", w=500, tam=26, cor=OXID, peso=700, serif=True)]
    X0, X1 = 20, 600
    X = lambda v: X0 + (v - 0.1) / 0.5 * (X1 - X0)
    p.append(f'<rect x="{X(0.2):.0f}" y="80" width="{X(0.5) - X(0.2):.0f}" height="60" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<rect x="{X(0.2):.0f}" y="80" width="{X(0.3) - X(0.2):.0f}" height="60" rx="8" fill="{OXID}"/>')
    p.append(f'<line x1="{X0}" y1="160" x2="{X1}" y2="160" stroke="{MUDO}" stroke-width="3"/>')
    for v in [0.2, 0.3, 0.4, 0.5]:
        rs.append(rot(X(v) - 40, 168, f"{v:g}".replace(".", ","), w=80, tam=19, cor=MUDO, alinha="center"))
    rs += [rot(X0, 208, "g/kg; o trecho escuro se tolera melhor", w=600, tam=20, cor=TINTA)]
    p.append(caixa(660, 0, 420, 400, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:scale", 684, 24, 48, GLIC))
    rs += [rot(746, 30, "A conta, para 70 kg", w=320, tam=24, cor=GLIC, peso=700, serif=True),
           rot(660, 120, "14 a 21 g", w=420, tam=54, cor=GLIC, peso=700, alinha="center", serif=True),
           rot(684, 220, "com 0,2 a 0,3 g/kg: muito pó", w=372, tam=22, cor=TINTA, alinha="center", lh=1.3)]
    X2, X3 = 1160, 1640
    T = lambda m: X2 + (200 - m) / 200 * (X3 - X2)
    rs.append(rot(X2, 0, "O horário", w=480, tam=26, cor=TINTA, peso=700, serif=True))
    p.append(f'<rect x="{T(180):.0f}" y="80" width="{T(60) - T(180):.0f}" height="60" rx="8" fill="{CINZA}"/>')
    p.append(f'<line x1="{X2}" y1="160" x2="{X3}" y2="160" stroke="{MUDO}" stroke-width="3"/>')
    for m in [180, 120, 60, 0]:
        rs.append(rot(T(m) - 50, 168, f"{m} min" if m else "largada", w=100, tam=18, cor=MUDO, alinha="center"))
    rs.append(rot(X2, 208, "60 a 180 min antes, individualizado em treino", w=480, tam=20, cor=TINTA, lh=1.25))
    return slide("bicarbonato", 400, p, rs,
                 eyebrow="O protocolo do bicarbonato", titulo="Muito pó, e o tempo varia de pessoa para pessoa",
                 destaque="Uso repetido ao longo de semanas, junto ao treino, é linha de pesquisa, não conduta fechada.", destaque_cor="tinta")


def intestino_55():
    """5.5: cinco ajustes que levam ao teste duplo, e a porta de saída."""
    p = [svg_abre(1664, 400, "Quatro ajustes que reduzem o desconforto: dose menor, de 0,2 ou 0,3 grama por quilo; mais cedo, perto de 180 minutos antes; com refeição rica em carboidrato; cápsula com revestimento entérico quando disponível, e dividir a dose também ajuda. Eles levam ao quinto passo: testar duas vezes em treino, na mesma hora e com a mesma refeição. Quem não tolerou não usa"), defs(MUDO, FOSF)]
    ajustes = [("t:scale", "Dose menor", "0,2 ou 0,3 g/kg"), ("t:clock", "Mais cedo", "perto de 180 min antes"), ("t:salad", "Com refeição", "rica em carboidrato"), ("t:pill", "Cápsula entérica", "quando houver; dividir também ajuda")]
    rs = []
    for k, (ic, t, d) in enumerate(ajustes):
        y = k * 100
        p.append(caixa(0, y, 640, 88, OXID, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 20, y + 22, 44, OXID))
        rs += [rot(84, y + 14, t, w=540, tam=24, cor=OXID, peso=700), rot(84, y + 50, d, w=540, tam=20, cor=TINTA)]
        p.append(seta(648, y + 44, 760, 200, MUDO, "m0", esp=3))
    p.append(caixa(770, 120, 460, 160, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:repeat", 794, 144, 44, GLIC))
    rs += [rot(852, 146, "Testar duas vezes em treino", w=360, tam=24, cor=GLIC, peso=700, lh=1.15),
           rot(794, 214, "mesma hora, mesma refeição", w=420, tam=21, cor=TINTA)]
    p.append(seta(1236, 200, 1290, 200, FOSF, "m1", esp=4))
    p.append(caixa(1300, 120, 364, 160, FOSF, FOSF, esp=0, rx=16))
    rs.append(rot(1300, 160, "não tolerou: não usa", w=364, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.2))
    return slide("intestino", 400, p, rs,
                 eyebrow="O intestino decide", titulo="O que separa o protocolo da prova perdida")


def limites_55():
    """5.5: seis fronteiras clínicas em volta de “é só bicarbonato de cozinha”."""
    p = [svg_abre(1664, 400, "No centro, a frase: é só bicarbonato de cozinha. Em volta, seis limites clínicos. Sódio: a dose traz muito sódio. Hipertensão e coração: hipertensão, insuficiência cardíaca. Rim: doença renal. Medicação que mexe com eletrólitos ou equilíbrio ácido-básico. Alcalose: risco em dose alta. Nitrato: medicação para disfunção erétil, nitrato cardiológico e anti-hipertensivo")]
    cx, cy = 832, 200
    nos = [(0, 0, "t:scale", "Sódio", "a dose traz muito sódio", GLIC, GLIC_T),
           (0, 140, "t:heartbeat", "Hipertensão e coração", "hipertensão, insuficiência cardíaca", FOSF, FOSF_T),
           (0, 280, "t:droplet", "Rim", "doença renal", FOSF, FOSF_T),
           (1044, 0, "t:pill", "Medicação", "que mexe com eletrólitos ou equilíbrio ácido-básico", GLIC, GLIC_T),
           (1044, 140, "t:alert-triangle", "Alcalose", "risco em dose alta", FOSF, FOSF_T),
           (1044, 280, "t:heart", "Nitrato", "medicação para disfunção erétil, nitrato cardiológico, anti-hipertensivo", TINTA, CARTAO)]
    rs = []
    for x, y, ic, t, d, cor, fundo in nos:
        ax = x + 620 if x == 0 else x
        p.append(f'<line x1="{ax}" y1="{y + 60}" x2="{cx + (-80 if x == 0 else 80)}" y2="{cy + (y + 60 - cy) * 0.4:.0f}" stroke="{BORDA}" stroke-width="3"/>')
        p.append(caixa(x, y, 620, 120, cor, fundo, esp=3, rx=14))
        p.append(icone(ic, x + 18, y + 16, 38, cor))
        rs += [rot(x + 68, y + 20, t, w=530, tam=24, cor=cor, peso=700, serif=True), rot(x + 20, y + 62, d, w=580, tam=19, cor=TINTA, lh=1.25)]
    p.append(f'<circle cx="{cx}" cy="{cy}" r="96" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    rs.append(rot(cx - 84, cy - 40, "“é só bicarbonato de cozinha”", w=168, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.25))
    return slide("limites", 400, p, rs,
                 eyebrow="Os limites clínicos", titulo="“É só bicarbonato de cozinha”",
                 fonte="Doença crônica: decisão médica")


def perfis_55():
    """5.5: três perfis, a duração do esforço e o que cabe em cada um."""
    p = [svg_abre(1664, 360, "Três perfis, cada um com a duração do esforço e o que cabe. O ciclista do contrarrelógio de 20 minutos: nitrato, em shot, 2 a 3 horas antes, alguns dias antes, sem enxaguante. A judoca de várias lutas de 4 a 5 minutos: beta-alanina como base, bicarbonato testado, nunca com corte de peso. A corredora de 5 quilômetros, de 20 a 30 minutos: fora da janela do bicarbonato; nitrato é mais defensável"), defs(MUDO)]
    linhas = [("t:bike", "Ciclista, contrarrelógio", "20 min", "nitrato: shot, 2 a 3 h antes, alguns dias antes, sem enxaguante", OXID),
              ("t:karate", "Judoca, várias lutas", "4 a 5 min", "beta-alanina como base; bicarbonato testado; nunca com corte de peso", GLIC),
              ("t:run", "Corredora, 5 km", "20 a 30 min", "fora da janela do bicarbonato; nitrato é mais defensável", OXID)]
    rs = []
    for k, (ic, t, dur, d, cor) in enumerate(linhas):
        y = k * 120
        p.append(caixa(0, y, 460, 104, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 20, y + 28, 48, TINTA))
        rs.append(rot(84, y + 36, t, w=360, tam=23, cor=TINTA, peso=700, serif=True))
        p.append(caixa(490, y + 22, 200, 60, MUDO, PAPEL, esp=2, rx=30))
        p.append(icone("t:stopwatch", 504, y + 36, 32, MUDO))
        rs.append(rot(540, y + 40, dur, w=140, tam=21, cor=TINTA, peso=700, alinha="center"))
        p.append(seta(696, y + 52, 734, y + 52, MUDO, "m0", esp=3))
        p.append(caixa(744, y, 920, 104, cor, CARTAO, esp=3, rx=14))
        rs.append(rot(768, y + 22, d, w=876, tam=22, cor=cor, peso=700, lh=1.3))
    return slide("perfis", 360, p, rs,
                 eyebrow="Três perfis típicos", titulo="Quanto dura o esforço, e o que cabe",
                 destaque="“O que você usou não tem indicação para a sua prova, e o jeito como você usou não funcionaria nem na prova certa.”",
                 destaque_cor="ambar")


# ---------------------------------------------------------------- 5.6

def categoria():
    """5.6: o pote é comida em pó, e os dois enganos em volta dele."""
    p = [svg_abre(1664, 360, "No centro, um pote igual a um copo de leite: proteína em pó é comida em pó, não ergogênico. À esquerda, o primeiro engano: esperar do pó um efeito que ele não tem; custa dinheiro. À direita, o engano oposto: recusar o pó justo onde ele resolveria; custa músculo")]
    rs = []
    pote(p, 650, 30, 170, 260, OXID, OXID_T)
    rs.append(rot(650, 140, "pó", w=170, tam=28, cor=OXID, peso=700, alinha="center", serif=True))
    rs.append(rot(830, 120, "=", w=60, tam=56, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<path d="M 910 80 L 930 290 L 1010 290 L 1030 80 Z" fill="{CARTAO}" stroke="{AZUL}" stroke-width="4"/>')
    p.append(f'<path d="M 916 140 L 930 290 L 1010 290 L 1024 140 Z" fill="{AZUL_T}"/>')
    rs += [rot(860, 300, "comida", w=220, tam=24, cor=AZUL, peso=700, alinha="center")]
    for x, t, d, cus, ic, cor, fundo in [(0, "Espera um efeito que o pó não tem", "trata o pote como ergogênico", "custa dinheiro", "h:money-bag", GLIC, GLIC_T),
                                         (1104, "Recusa justo onde resolveria", "“é para ficar grande”", "custa músculo", "t:barbell", FOSF, FOSF_T)]:
        p.append(caixa(x, 20, 560, 300, cor, fundo, esp=3, rx=16))
        rs += [rot(x + 24, 40, t, w=510, tam=26, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 24, 130, d, w=510, tam=22, cor=TINTA)]
        p.append(icone(ic, x + 24, 220, 52, cor))
        rs.append(rot(x + 92, 230, cus, w=440, tam=30, cor=cor, peso=700))
    return slide("categoria", 360, p, rs,
                 eyebrow="O erro é de categoria", titulo="Proteína em pó não é ergogênico. É comida em pó.")


def perfis_56():
    """5.6: três perfis numa régua de proteína do dia."""
    p = [svg_abre(1664, 400, "Uma régua de proteína do dia, de 0 a 2,5 gramas por quilo, com a linha de cerca de 1,6 acima da qual não há ganho adicional de massa. Quem comprou whey já come perto de 2 gramas por quilo, acima da linha, porque todo mundo toma. Quem recusa whey come perto de 0,8, quase tudo no jantar, porque acha que é para ficar grande. O terceiro toma BCAA durante o treino longo de corrida, para proteger o músculo: a questão dele não está nessa régua")]
    X0, X1, Y = 40, 1620, 170
    X = lambda v: X0 + v / 2.5 * (X1 - X0)
    rs = []
    p.append(f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="{MUDO}" stroke-width="4"/>')
    for v in [0, 0.5, 1, 1.5, 2, 2.5]:
        p.append(f'<line x1="{X(v):.0f}" y1="{Y - 8}" x2="{X(v):.0f}" y2="{Y + 8}" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(X(v) - 40, Y + 14, f"{v:g}".replace(".", ","), w=80, tam=18, cor=MUDO, alinha="center"))
    rs.append(rot(X0, Y + 44, "g de proteína por kg por dia", w=500, tam=18, cor=MUDO))
    p.append(f'<line x1="{X(1.6):.0f}" y1="{Y - 120}" x2="{X(1.6):.0f}" y2="{Y + 10}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs.append(rot(X(1.6) - 100, Y - 150, "≈ 1,6: teto do ganho", w=200, tam=19, cor=TINTA, peso=700, alinha="center"))
    for v, t, cor in [(2.0, "comprou whey", FOSF), (0.8, "recusa whey", GLIC)]:
        p.append(f'<circle cx="{X(v):.0f}" cy="{Y}" r="16" fill="{cor}"/>')
        rs.append(rot(X(v) - 110, Y - 60, t, w=220, tam=21, cor=cor, peso=700, alinha="center"))
    cards = [(0, "Comprou whey", "já come perto de 2 g/kg por dia; “todo mundo toma”", FOSF), (568, "Recusa whey", "come perto de 0,8 g/kg, quase tudo no jantar; “é para ficar grande”", GLIC), (1136, "Toma BCAA", "durante o treino longo de corrida, “para proteger o músculo”", OXID)]
    for x, t, d, cor in cards:
        p.append(caixa(x, 260, 528, 130, cor, CARTAO, esp=3, rx=14))
        rs += [rot(x + 20, 274, t, w=490, tam=23, cor=cor, peso=700, serif=True), rot(x + 20, 312, d, w=490, tam=19, cor=TINTA, lh=1.25)]
    return slide("perfis", 400, p, rs,
                 eyebrow="Três perfis típicos", titulo="O pote na pessoa errada",
                 destaque="Em dois deles a conduta envolve algum pó. Só que não o que compraram.", destaque_cor="tinta")


def morton_56():
    """5.6: os dois ganhos médios e a curva com teto."""
    p = [svg_abre(1664, 400, "À esquerda, os dois ganhos médios: mais 0,30 quilo de massa livre de gordura e mais 2,49 quilos no teste de uma repetição máxima. À direita, uma curva em esquema: o ganho de massa sobe com a proteína total do dia até cerca de 1,6 grama por quilo e, acima disso, fica plano")]
    rs = []
    for k, (n, d, ic, cor, fundo) in enumerate([("+0,30 kg", "de massa livre de gordura, em média", "t:weight", OXID, OXID_T), ("+2,49 kg", "no teste de uma repetição máxima, em média", "t:barbell", GLIC, GLIC_T)]):
        x = k * 400
        p.append(caixa(x, 0, 370, 400, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, x + 24, 24, 48, cor))
        rs += [rot(x, 120, n, w=370, tam=48, cor=cor, peso=700, alinha="center", serif=True), rot(x + 24, 220, d, w=322, tam=22, cor=TINTA, alinha="center", lh=1.3)]
    X0, X1, B, T = 900, 1640, 330, 40
    X = lambda v: X0 + v / 2.5 * (X1 - X0)
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X1}" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="{X0}" y1="{T}" x2="{X0}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    pts = [(X(v / 10), B - (B - T - 60) * min(1, (v / 10) / 1.6) ** 0.7) for v in range(0, 26)]
    p.append(f'<polyline points="{" ".join(f"{a:.0f},{b:.0f}" for a, b in pts)}" fill="none" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<line x1="{X(1.6):.0f}" y1="{T}" x2="{X(1.6):.0f}" y2="{B}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs += [rot(X(1.6) - 100, B + 12, "≈ 1,6 g/kg", w=200, tam=20, cor=TINTA, peso=700, alinha="center"),
           rot(X(1.6) + 14, T + 6, "acima disso, sem ganho adicional de massa", w=250, tam=19, cor=TINTA, lh=1.25),
           rot(X0 - 80, T - 30, "ganho de massa", w=200, tam=18, cor=MUDO),
           rot(X0, B + 44, "proteína total do dia · curva: esquema", w=700, tam=17, cor=MUDO)]
    return slide("morton", 400, p, rs,
                 eyebrow="Uma meta-análise de 2018", titulo="Real, pequeno, e com teto",
                 destaque="O efeito não é do pó. É da proteína que faltava.", destaque_cor="verm",
                 fonte="Morton e colaboradores · 49 estudos, 1.863 pessoas em treino de força · British Journal of Sports Medicine 2018")


def obstaculos():
    """5.6: seis obstáculos levando ao pote, da pessoa e da rotina."""
    p = [svg_abre(1664, 400, "Seis obstáculos que justificam o pote, com setas para ele no centro. Da pessoa: apetite baixo, porque líquido passa onde sólido não passa; mastigação, como prótese mal adaptada, uma questão de viabilidade; e dieta vegetal, que o pó ajuda a fechar com menos volume. Da rotina: logística, porque cria uma refeição que não existiria; volume de treino, com necessidade alta e pouco tempo entre sessões; e custo por grama, em que o pó perde para ovo e leite e ganha de corte nobre"), defs(MUDO)]
    esq = [("t:mood-empty", "Apetite baixo", "líquido passa onde sólido não passa", OXID), ("t:mood-confuzed", "Mastigação", "prótese mal adaptada: viabilidade", OXID), ("t:plant", "Dieta vegetal", "fecha a conta com menos volume", GLIC)]
    dir_ = [("t:clock", "Logística", "cria uma refeição que não existiria", OXID), ("t:barbell", "Volume de treino", "necessidade alta, pouco tempo entre sessões", GLIC), ("h:money-bag", "Custo por grama", "perde para ovo e leite; ganha de corte nobre", GLIC)]
    rs = [rot(0, 0, "Da pessoa", w=600, tam=22, cor=MUDO, peso=700), rot(1064, 0, "Da rotina", w=600, tam=22, cor=MUDO, peso=700)]
    for lado, itens in [(0, esq), (1064, dir_)]:
        for k, (ic, t, d, cor) in enumerate(itens):
            y = 40 + k * 120
            p.append(caixa(lado, y, 600, 104, cor, CARTAO, esp=2, rx=14))
            p.append(icone(ic, lado + 18, y + 28, 44, cor))
            rs += [rot(lado + 80, y + 16, t, w=500, tam=23, cor=cor, peso=700), rot(lado + 80, y + 56, d, w=500, tam=19, cor=TINTA)]
            if lado == 0:
                p.append(seta(606, y + 52, 724, 210, MUDO, "m0", esp=3))
            else:
                p.append(seta(1058, y + 52, 940, 210, MUDO, "m0", esp=3))
    pote(p, 742, 80, 180, 260, OXID, OXID_T)
    rs.append(rot(742, 190, "o pote", w=180, tam=24, cor=OXID, peso=700, alinha="center", serif=True))
    return slide("obstaculos", 400, p, rs,
                 eyebrow="Que obstáculo ele remove?", titulo="Seis razões legítimas",
                 destaque="Entra quando há obstáculo, sai quando o obstáculo some. Sem obstáculo, só substitui: e comida traz colina, cálcio, ferro heme, B12, fibra.",
                 destaque_cor="tinta")


def tipos():
    """5.6: cinco potes, o que é cada tipo e para quem."""
    p = [svg_abre(1664, 400, "Cinco potes. Concentrado: teor variável, perto de 80% no pote comum; para a maioria. Isolado: acima de 90%, com menos lactose e gordura; para intolerância à lactose. Hidrolisado: parcialmente quebrado, mais caro e mais amargo; sem vantagem clínica demonstrada. Caseína: digestão lenta; para a refeição antes de dormir. Vegetais: soja completa, ervilha e arroz que se complementam; para o vegano, em mistura bem formulada")]
    tt = [("Concentrado", "teor variável; no pote comum, perto de 80%", "a maioria", OXID),
          ("Isolado", "acima de 90%; menos lactose e gordura", "intolerância à lactose", OXID),
          ("Hidrolisado", "parcialmente quebrado; mais caro, mais amargo", "sem vantagem clínica demonstrada", FOSF),
          ("Caseína", "digestão lenta", "refeição antes de dormir", AZUL),
          ("Vegetais", "soja completa; ervilha e arroz se complementam", "vegano, em mistura bem formulada", GLIC)]
    W = 300
    rs = []
    for k, (t, d, q, cor) in enumerate(tt):
        x = k * (W + 41)
        pote(p, x + 60, 0, 180, 150, cor, CARTAO)
        rs.append(rot(x + 60, 66, t, w=180, tam=20, cor=cor, peso=700, alinha="center", serif=True))
        rs.append(rot(x, 170, d, w=W, tam=20, cor=TINTA, alinha="center", lh=1.3))
        p.append(caixa(x, 300, W, 90, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(x + 10, 316, q, w=W - 20, tam=20, cor=cor, peso=700, alinha="center", lh=1.25))
    return slide("tipos", 400, p, rs,
                 eyebrow="Diferença real e diferença de rótulo", titulo="Os tipos",
                 destaque="Sabor muda a adesão, não a proteína. Pote simples, um ingrediente, dose declarada.", destaque_cor="petr")


def jackman():
    """5.6: o BCAA estimula, mas metade do que a mesma quantidade em whey faz."""
    p = [svg_abre(1664, 360, "Barras de síntese de proteína miofibrilar depois do treino de força. Placebo de mesma energia como linha de base. 5,6 gramas de BCAA: mais 22%. Uma dose de whey com a mesma quantidade de BCAA: cerca do dobro dessa resposta, segundo a comparação feita pelos autores com um estudo anterior. Alturas em esquema")]
    B, K = 310, 5.5
    barras = [("placebo", 0, "base", MUDO), ("5,6 g de BCAA", 22, "+22%", GLIC), ("whey com os mesmos BCAA", 44, "≈ 2×", OXID)]
    rs = []
    for k, (t, v, lab, cor) in enumerate(barras):
        x = 60 + k * 340
        h = max(v * K, 8)
        p.append(f'<rect x="{x}" y="{B - h}" width="220" height="{h}" rx="8" fill="{cor}"/>')
        rs += [rot(x - 30, B - h - 50, lab, w=280, tam=32, cor=cor, peso=700, alinha="center", serif=True), rot(x - 40, B + 10, t, w=300, tam=20, cor=TINTA, alinha="center", lh=1.2)]
    p.append(f'<line x1="30" y1="{B}" x2="1080" y2="{B}" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(0, 0, "síntese de proteína miofibrilar depois do treino de força · alturas: esquema", w=420, tam=18, cor=MUDO, lh=1.2))
    p.append(caixa(1160, 40, 504, 270, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(1160, 80, "≈ ½", w=504, tam=72, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(1184, 190, "da resposta a uma dose de whey com a mesma quantidade de BCAA", w=456, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    return slide("jackman", 360, p, rs,
                 eyebrow="Um experimento de 2017", titulo="Não é zero. É metade.",
                 destaque="A porção de whey que já tem esses BCAA traz os outros seis essenciais. No treino longo, o que poupa o corpo é carboidrato.",
                 destaque_cor="ambar", fonte="Jackman e colaboradores · comparação com whey feita pelos autores, com estudo anterior · Frontiers in Physiology 2017")


def prateleira():
    """5.6: cinco potes numa prateleira, cada um com seu veredito."""
    p = [svg_abre(1664, 400, "Uma prateleira com cinco potes, cada um com um veredito. EAA: o mais defensável, para apetite baixo, idoso e quem não tolera volume; ainda perde para comida. Leucina isolada: é o gatilho, e gatilho sem matéria-prima não constrói. Glutamina: sem sustentação em pessoa saudável e bem alimentada. HMB: resultados variam muito entre grupos, sem caso para quem já come proteína. Pote com tudo dentro: sem dose por item; se a creatina é indicada, compre creatina")]
    potes = [("EAA", "mais defensável", "apetite baixo, idoso, quem não tolera volume; ainda perde para comida", GLIC, GLIC_T),
             ("Leucina", "só o gatilho", "gatilho sem matéria-prima não constrói", FOSF, FOSF_T),
             ("Glutamina", "sem sustentação", "em pessoa saudável e bem alimentada", FOSF, FOSF_T),
             ("HMB", "resultado variável", "sem caso para quem já come proteína", FOSF, FOSF_T),
             ("Tudo dentro", "sem dose por item", "se a creatina é indicada, compre creatina", FOSF, FOSF_T)]
    W = 300
    rs = []
    p.append(f'<rect x="0" y="170" width="1664" height="16" rx="4" fill="{MUDO}"/>')
    for k, (t, v, d, cor, fundo) in enumerate(potes):
        x = k * (W + 41)
        pote(p, x + 70, 0, 160, 168, MUDO, CARTAO)
        rs.append(rot(x + 70, 80, t, w=160, tam=21, cor=TINTA, peso=700, alinha="center", serif=True))
        p.append(caixa(x, 206, W, 56, cor, fundo, esp=2, rx=28))
        rs += [rot(x, 220, v, w=W, tam=20, cor=cor, peso=700, alinha="center"), rot(x + 6, 280, d, w=W - 12, tam=19, cor=TINTA, alinha="center", lh=1.3)]
    return slide("prateleira", 400, p, rs,
                 eyebrow="O resto da prateleira", titulo="Um veredito por pote")


def colageno():
    """5.6: o desenho do estudo da gelatina e a leitura do achado."""
    p = [svg_abre(1664, 400, "À esquerda, o estudo em linha do tempo: 8 homens, cruzado e duplo-cego; 5 ou 15 gramas de gelatina com vitamina C, uma hora antes de 6 minutos de pular corda. Com 15 gramas, o marcador de síntese de colágeno quase dobrou. À direita, a leitura: é marcador, não desfecho; depende de dose, vitamina C e carga no tendão; sem exercício, é só proteína; e é proteína incompleta, que não conta como proteína do dia"), defs(MUDO)]
    passos = [("t:droplet", "5 ou 15 g de gelatina", "com vitamina C"), ("t:clock", "1 hora", "depois"), ("t:stretching", "6 min", "de pular corda")]
    rs = [rot(0, 0, "8 homens, cruzado, duplo-cego", w=900, tam=22, cor=MUDO, peso=700)]
    for k, (ic, t, d) in enumerate(passos):
        x = k * 300
        p.append(caixa(x, 40, 260, 150, OXID, OXID_T, esp=2, rx=14))
        p.append(icone(ic, x + 20, 60, 40, OXID))
        rs += [rot(x + 20, 110, t, w=230, tam=22, cor=OXID, peso=700), rot(x + 20, 146, d, w=230, tam=19, cor=TINTA)]
        if k < 2:
            p.append(seta(x + 264, 115, x + 296, 115, MUDO, "m0", esp=3))
    B = 380
    for k, (t, h, cor) in enumerate([("5 g", 70, CINZA), ("15 g", 130, OXID)]):
        x = 60 + k * 200
        p.append(f'<rect x="{x}" y="{B - h}" width="140" height="{h}" rx="6" fill="{cor}"/>')
        rs.append(rot(x, B - h - 30, t, w=140, tam=20, cor=TINTA, peso=700, alinha="center"))
    rs += [rot(460, 260, "com 15 g, o marcador de síntese quase dobrou", w=420, tam=22, cor=OXID, peso=700, lh=1.25),
           rot(460, 340, "alturas: esquema", w=300, tam=17, cor=MUDO)]
    p.append(caixa(960, 0, 704, 400, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(984, 18, "A leitura", w=660, tam=28, cor=GLIC, peso=700, serif=True))
    for k, t in enumerate(["marcador, não desfecho", "depende de dose, vitamina C e carga no tendão", "sem exercício, é só proteína", "incompleta: não conta como proteína do dia"]):
        y = 82 + k * 76
        p.append(f'<circle cx="998" cy="{y + 14}" r="8" fill="{GLIC}"/>')
        rs.append(rot(1018, y, t, w=630, tam=22, cor=TINTA, lh=1.25))
    return slide("colageno", 400, p, rs,
                 eyebrow="Um experimento de 2017", titulo="Colágeno: grupo B, e por quê",
                 destaque="Tendinopatia e a carga que a trata ficam no módulo de fisioterapia esportiva e reabilitação.",
                 destaque_cor="tinta", fonte="Shaw e colaboradores · American Journal of Clinical Nutrition 2017")


def condutas():
    """5.6: os três do começo, o problema real e a conduta."""
    p = [svg_abre(1664, 380, "Os três perfis do começo, cada um com o problema real e a conduta. Quem comprou whey: nenhum problema, está acima do teto; o pote não acrescenta, e como conveniência tudo bem. Quem recusa whey: total baixo e distribuição torta; comida no café da manhã e, se não couber, um shake. Quem toma BCAA: falta carboidrato no treino longo; carboidrato durante, e proteína nas refeições"), defs(MUDO)]
    linhas = [("Comprou whey", "nenhum: acima do teto", "o pote não acrescenta; como conveniência, tudo bem", MUDO, PAPEL),
              ("Recusa whey", "total baixo, distribuição torta", "comida no café da manhã; se não couber, um shake", OXID, OXID_T),
              ("Toma BCAA", "falta carboidrato no treino longo", "carboidrato durante; proteína nas refeições", GLIC, GLIC_T)]
    rs = [rot(440, 0, "Problema real", w=400, tam=19, cor=MUDO, peso=700), rot(1000, 0, "Conduta", w=400, tam=19, cor=MUDO, peso=700)]
    for k, (t, pr, c, cor, fundo) in enumerate(linhas):
        y = 36 + k * 118
        pote(p, 0, y, 70, 100, TINTA, CARTAO)
        rs.append(rot(90, y + 34, t, w=320, tam=24, cor=TINTA, peso=700, serif=True))
        p.append(caixa(440, y, 500, 100, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(460, y + 34, pr, w=460, tam=22, cor=TINTA))
        p.append(seta(946, y + 50, 992, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(1000, y, 664, 100, cor, fundo, esp=3, rx=14))
        rs.append(rot(1020, y + 22, c, w=624, tam=22, cor=cor if cor != MUDO else TINTA, peso=700, lh=1.3))
    return slide("condutas", 380, p, rs,
                 eyebrow="Os três do começo", titulo="O problema real e a conduta",
                 destaque="Quem mais se beneficiaria é quem acha que o produto não é para ela. Não é para ficar grande: é músculo e função.",
                 destaque_cor="petr")





# ---------------------------------------------------------------- aplicação

LICOES = {"05-01": [pedidos_51, passo1, comida, abcd, perguntas, riscos, rotulo, decidir, respostas],
          "05-02": [confusao, peso, responde, rim, mitos, populacoes, alem, protocolo],
          "05-03": [pergunta_53, mecanismo, fonte_53, sono, genetica, habito, limites, decisoes_53],
          "05-04": [formigamento, acumulo, tamanho, protocolo_54, notas_54, onde, perfis_54],
          "05-05": [esqueleto, inversao, nitrato, erros_55, bicarbonato, intestino_55, limites_55, perfis_55],
          "05-06": [categoria, perfis_56, morton_56, obstaculos, tipos, jackman, prateleira, colageno, condutas]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
