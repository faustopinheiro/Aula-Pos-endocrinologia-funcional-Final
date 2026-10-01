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



# ---------------------------------------------------------------- aplicação

LICOES = {"05-01": [pedidos_51, passo1, comida, abcd, perguntas, riscos, rotulo, decidir, respostas],
          "05-02": [confusao, peso, responde, rim, mitos, populacoes, alem, protocolo],
          "05-03": [pergunta_53, mecanismo, fonte_53, sono, genetica, habito, limites, decisoes_53]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
