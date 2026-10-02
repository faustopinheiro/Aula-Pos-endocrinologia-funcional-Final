"""Desenhos que substituem os slides de texto do Módulo 7 (cartões, colunas, listas, tabelas e números).
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


# ---------------------------------------------------------------- 7.1

def numeros_71():
    """7.1: duas barras na mesma escala de 0 a 100%: 19,4% e 79,3%, as duas chamadas de lesão."""
    p = [svg_abre(1664, 360, "Duas barras na mesma escala de zero a cem por cento, da mesma revisão de 2007 sobre corredores de longa distância. No estudo que achou menos lesão, 19,4%. No que achou mais, 79,3%. As duas barras se chamam lesão. Quatro vezes de diferença, no mesmo esporte"), defs(MUDO)]
    rs = []
    X0, E = 300, 12
    for k, (v, txt, cor) in enumerate([(19.4, "o estudo que achou menos", OXID), (79.3, "o estudo que achou mais", FOSF)]):
        y = 20 + k * 130
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E:.0f}" height="96" rx="8" fill="{cor}"/>')
        rs += [rot(0, y + 32, txt, w=280, tam=20, cor=TINTA, peso=700, alinha="right"),
               rot(X0 + 20, y + 30, "lesão", w=160, tam=24, cor=PAPEL, peso=700),
               rot(X0 + v * E + 20, y + 18, f"{v:.1f}%".replace(".", ","), w=260, tam=48, cor=cor, peso=700, serif=True)]
    for t in range(0, 101, 25):
        x = X0 + t * E
        p.append(f'<line x1="{x}" y1="260" x2="{x}" y2="272" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(x - 40, 280, f"{t}%", w=80, tam=18, cor=MUDO, alinha="center"))
    p.append(f'<line x1="{X0}" y1="260" x2="{X0 + 100 * E}" y2="260" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(X0, 318, "mesma revisão (2007), mesmo esporte: corredores de longa distância", w=1200, tam=20, cor=MUDO))
    return slide("numeros", 360, p, rs, eyebrow="Mesma revisão, mesmo esporte", titulo="Lesão em corredores: de 19,4% a 79,3%",
                 destaque="Os estudos mediram coisas diferentes e chamaram todas de lesão. O número não descreve só a realidade: descreve a definição.", destaque_cor="tinta")


def usos_71():
    """7.1: o número de lesão no centro, abrindo em quatro usos práticos."""
    p = [svg_abre(1664, 400, "O número de lesão, à esquerda, abre em quatro usos práticos: implantar prevenção, vale a pena no meu clube ou assessoria; responder ao aluno que pergunta se corrida destrói o joelho; comparar modalidades, em que esporte colocar o filho; saber se funcionou, o que eu mudei reduziu lesão"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 120, 340, 160, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(20, 150, "o número", w=300, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(20, 200, "de lesão", w=300, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True)]
    itens = [("t:shield-check", "Implantar prevenção", "vale a pena no meu clube ou assessoria?", OXID),
             ("t:message-circle", "Responder ao aluno", "“corrida destrói o joelho?”", GLIC),
             ("t:arrows-exchange", "Comparar modalidades", "em que esporte colocar o filho?", GLIC),
             ("t:chart-line", "Saber se funcionou", "o que eu mudei reduziu lesão?", OXID)]
    for k, (ic, t, d, cor) in enumerate(itens):
        y = k * 102
        p.append(seta(344, 200, 472, y + 44, MUDO, "m0", esp=3))
        p.append(caixa(480, y, 1184, 88, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 500, y + 20, 48, cor))
        rs += [rot(570, y + 28, t, w=420, tam=26, cor=cor, peso=700, serif=True), rot(1000, y + 30, d, w=640, tam=23, cor=TINTA)]
    return slide("usos", 400, p, rs, eyebrow="Por que começar por aqui", titulo="Você vai usar esses números a vida inteira",
                 destaque="As ferramentas nasceram no esporte profissional. Em quem treina sozinho, erram sempre para o mesmo lado: não enxergam a sobrecarga.",
                 destaque_cor="tinta", fonte="Revisão sistemática, Br J Sports Med 2007")


def familias_71():
    """7.1: três lentes, cada uma com o que enxerga e o que deixa passar."""
    p = [svg_abre(1664, 400, "Três famílias de definição, como três lentes. Perda de tempo: enxerga o agudo e permite comparar clubes; deixa passar a sobrecarga de quem segue treinando. Atenção médica: enxerga o que chega ao serviço; deixa passar quem não tem acesso, e acaba medindo a fila. Autorrelato: enxerga o que as outras perdem; separa mal o desconforto passageiro")]
    rs = []
    itens = [("t:stopwatch", "Perda de tempo", "o agudo; compara clubes", "a sobrecarga de quem segue treinando", OXID, OXID_T),
             ("t:stethoscope", "Atenção médica", "o que chega ao serviço", "quem não tem acesso: mede a fila", AZUL, AZUL_T),
             ("t:message-circle", "Autorrelato", "o que as outras perdem", "separa mal o desconforto passageiro", GLIC, GLIC_T)]
    for k, (ic, t, v, n, cor, fundo) in enumerate(itens):
        x = k * 564
        p.append(caixa(x, 0, 536, 400, cor, CARTAO, esp=2, rx=16))
        p.append(f'<rect x="{x}" y="0" width="536" height="96" rx="16" fill="{fundo}"/>')
        p.append(icone(ic, x + 24, 24, 48, cor))
        rs.append(rot(x + 90, 30, t, w=420, tam=28, cor=cor, peso=700, serif=True))
        p.append(icone("t:eye", x + 24, 124, 36, OXID))
        rs += [rot(x + 72, 126, "enxerga", w=400, tam=19, cor=OXID, peso=700), rot(x + 24, 172, v, w=490, tam=23, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 24}" y1="244" x2="{x + 512}" y2="244" stroke="{BORDA}" stroke-width="2"/>')
        p.append(icone("t:eye-off", x + 24, 264, 36, FOSF))
        rs += [rot(x + 72, 266, "deixa passar", w=400, tam=19, cor=FOSF, peso=700), rot(x + 24, 312, n, w=490, tam=23, cor=TINTA, lh=1.3)]
    return slide("familias", 400, p, rs, eyebrow="As três famílias de definição", titulo="Cada uma enxerga uma coisa",
                 destaque="A tendinopatia que dói há oito meses não afasta ninguém do treino. Só estraga a qualidade dele.", destaque_cor="verm",
                 fonte="Consenso do futebol, Br J Sports Med 2006")


def consenso_71():
    """7.1: a definição de consenso como fluxo: dor relacionada à corrida, restrição por 7 dias ou 3 sessões, ou consulta."""
    p = [svg_abre(1664, 400, "A definição brasileira como fluxo. Dor musculoesquelética em membros inferiores, relacionada à corrida. Ela vira lesão por um de dois caminhos: restringe ou interrompe a corrida, em distância, velocidade, duração ou treino, sem precisar parar, por pelo menos sete dias ou três sessões seguidas, o que separa o desconforto passageiro do problema; ou leva o corredor a consultar um profissional de saúde"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 100, 400, 200, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("h:running", 20, 120, 60, TINTA))
    rs += [rot(94, 126, "Dor musculoesquelética", w=290, tam=23, cor=TINTA, peso=700, lh=1.2),
           rot(20, 200, "em membros inferiores, relacionada à corrida", w=360, tam=21, cor=TINTA, lh=1.3)]
    p.append(seta(404, 170, 486, 90, MUDO, "m0", esp=3))
    p.append(seta(404, 230, 486, 310, MUDO, "m0", esp=3))
    p.append(caixa(494, 0, 680, 220, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(518, 18, "Restringe ou interrompe a corrida", w=630, tam=25, cor=OXID, peso=700, serif=True),
           rot(518, 62, "distância, velocidade, duração ou treino: não precisa parar", w=630, tam=21, cor=TINTA, lh=1.3)]
    p.append(caixa(518, 138, 330, 60, GLIC, GLIC, esp=0, rx=30))
    p.append(icone("t:calendar", 536, 150, 36, PAPEL))
    rs += [rot(580, 154, "≥ 7 dias ou 3 sessões", w=260, tam=22, cor=PAPEL, peso=700),
           rot(866, 144, "separa o desconforto passageiro do problema", w=290, tam=19, cor=TINTA, lh=1.25)]
    rs.append(rot(800, 236, "ou", w=80, tam=24, cor=MUDO, peso=700, alinha="center"))
    p.append(caixa(494, 280, 680, 120, AZUL, AZUL_T, esp=2, rx=16))
    p.append(icone("t:stethoscope", 518, 314, 52, AZUL))
    rs += [rot(588, 304, "Leva a consultar", w=560, tam=25, cor=AZUL, peso=700, serif=True),
           rot(588, 346, "um profissional de saúde", w=560, tam=21, cor=TINTA)]
    p.append(seta(1178, 110, 1256, 180, MUDO, "m0", esp=3))
    p.append(seta(1178, 340, 1256, 230, MUDO, "m0", esp=3))
    p.append(caixa(1264, 120, 400, 160, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1280, 150, "lesão", w=368, tam=34, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1280, 204, "relacionada à corrida", w=368, tam=22, cor=PAPEL, alinha="center")]
    return slide("consenso", 400, p, rs, eyebrow="A definição brasileira para corredor recreativo", titulo="Yamato, Saragiotto e Lopes, 2015",
                 fonte="Delphi modificado, limiar de consenso de 75%, J Orthop Sports Phys Ther 2015")


def denominador_71():
    """7.1: a mesma contagem de lesões dividida por quatro denominadores, cada um com quando usar e cuidado."""
    p = [svg_abre(1664, 420, "As mesmas lesões no numerador, quatro denominadores possíveis. Por mil horas: o melhor, porque corrige pela exposição; exige medir o volume. Por mil sessões: onde a sessão é a unidade; sessões têm durações diferentes. Por cem atletas por ano, o percentual anual: fácil de comunicar e o mais enganoso, porque ignora quanto cada um treinou. Por mil exposições: esporte coletivo; separar treino de jogo")]
    rs = []
    rs += [rot(0, 0, "lesões divididas por", w=320, tam=19, cor=MUDO, peso=700, alinha="center"),
           rot(400, 0, "quando usar", w=400, tam=19, cor=OXID, peso=700), rot(1060, 0, "cuidado", w=400, tam=19, cor=FOSF, peso=700)]
    itens = [("mil horas", "o melhor: corrige pela exposição", "exige medir o volume", OXID, "o melhor"),
             ("mil sessões", "onde a sessão é a unidade", "sessões de durações diferentes", TINTA, ""),
             ("cem atletas por ano", "comunicação", "ignora quanto cada um treinou", FOSF, "o mais enganoso"),
             ("mil exposições", "esporte coletivo", "separar treino de jogo", TINTA, "")]
    for k, (den, q, c, cor, tag) in enumerate(itens):
        y = 40 + k * 96
        p.append(caixa(0, y, 1664, 84, cor if tag else BORDA, CARTAO, esp=3 if tag else 2, rx=14))
        rs.append(rot(0, y + 8, "lesões", w=320, tam=19, cor=MUDO, alinha="center"))
        p.append(f'<line x1="70" y1="{y + 38}" x2="250" y2="{y + 38}" stroke="{TINTA}" stroke-width="2"/>')
        rs.append(rot(0, y + 46, den, w=320, tam=22, cor=cor, peso=700, alinha="center"))
        p.append(icone("t:check", 350, y + 24, 36, OXID))
        rs.append(rot(400, y + 28, q, w=560, tam=22, cor=TINTA))
        p.append(icone("t:alert-triangle", 1010, y + 24, 36, FOSF))
        rs.append(rot(1060, y + 28, c, w=420, tam=22, cor=TINTA))
        if tag:
            rs.append(rot(1480, y + 30, tag, w=170, tam=18, cor=cor, peso=700, alinha="right"))
    return slide("denominador", 420, p, rs, eyebrow="Setenta e nove por cento de quê?", titulo="O denominador muda tudo")


def novatos_71():
    """7.1: duas barras por mil horas: novatos 17,8, experientes 7,7."""
    p = [svg_abre(1664, 360, "Duas barras na mesma unidade, lesões por mil horas de corrida. Corredores novatos: 17,8. Recreativos experientes: 7,7. Mais que o dobro, 2,3 vezes, no mesmo esporte: a diferença está em quem é a pessoa"), defs(MUDO)]
    rs = []
    X0, E = 340, 60
    for k, (v, t, ic, cor) in enumerate([(17.8, "novatos", "h:running", FOSF), (7.7, "recreativos experientes", "h:running", OXID)]):
        y = 10 + k * 110
        p.append(icone(ic, 0, y + 10, 64, cor))
        rs.append(rot(76, y + 28, t, w=250, tam=23, cor=TINTA, peso=700))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E:.0f}" height="88" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + v * E + 18, y + 14, f"{v:.1f}".replace(".", ","), w=200, tam=48, cor=cor, peso=700, serif=True))
    p.append(f'<line x1="{X0}" y1="226" x2="{X0 + 18 * E}" y2="226" stroke="{MUDO}" stroke-width="2"/>')
    for t in range(0, 19, 5):
        x = X0 + t * E
        p.append(f'<line x1="{x}" y1="226" x2="{x}" y2="238" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(x - 30, 244, str(t), w=60, tam=18, cor=MUDO, alinha="center"))
    rs.append(rot(X0, 274, "lesões por mil horas de corrida", w=600, tam=19, cor=MUDO))
    p.append(caixa(1200, 270, 464, 84, TINTA, TINTA, esp=0, rx=14))
    rs += [rot(1216, 280, "× 2,3", w=150, tam=38, cor=PAPEL, peso=700, serif=True),
           rot(1360, 284, "a diferença está em quem é a pessoa", w=290, tam=20, cor=PAPEL, lh=1.25)]
    return slide("novatos", 360, p, rs, eyebrow="A demonstração mais clara", titulo="Mesmo esporte, mesma unidade, mais que o dobro",
                 destaque="Percentual anual não compara grupos que treinam volumes diferentes. Para risco por hora, divida pela exposição.", destaque_cor="tinta",
                 fonte="Metanálise, Sports Med 2015")


def vocabulario_71():
    """7.1: três quadros: uma foto do grupo agora, casos novos ao longo do tempo, e casos novos por hora de exposição."""
    p = [svg_abre(1664, 400, "Três perguntas, três desenhos. Prevalência: uma foto do grupo agora, quantos têm o problema neste momento. Incidência: uma linha do tempo, quantos passaram a ter ao longo de um período. Taxa de incidência: casos novos divididos por horas, sessões ou jogos de exposição"), defs(MUDO)]
    rs = []
    cards = [("Prevalência", "quantos têm o problema agora", OXID), ("Incidência", "quantos passaram a ter, num período", GLIC),
             ("Taxa de incidência", "por hora, sessão ou jogo de exposição", TINTA)]
    for k, (t, d, cor) in enumerate(cards):
        x = k * 564
        p.append(caixa(x, 0, 536, 400, cor, CARTAO, esp=2, rx=16))
        rs += [rot(x + 24, 22, t, w=490, tam=28, cor=cor, peso=700, serif=True), rot(x + 24, 318, d, w=490, tam=23, cor=TINTA, lh=1.3)]
    # prevalência: um instante
    verm = {2, 8, 11}
    for i in range(18):
        cx, cy = 70 + (i % 6) * 80, 100 + (i // 6) * 56
        p.append(f'<circle cx="{cx}" cy="{cy}" r="20" fill="{FOSF if i in verm else CINZA}"/>')
    rs.append(rot(24, 262, "uma foto, um instante", w=490, tam=19, cor=MUDO))
    # incidência: período
    x = 564
    p.append(seta(x + 40, 230, x + 500, 230, MUDO, "m0", esp=3))
    for j, (px, novo) in enumerate([(80, False), (150, True), (220, False), (290, True), (360, False), (430, True)]):
        p.append(f'<circle cx="{x + px}" cy="{150}" r="20" fill="{FOSF if novo else CINZA}"/>')
        if novo:
            p.append(f'<line x1="{x + px}" y1="176" x2="{x + px}" y2="222" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
    rs += [rot(x + 30, 244, "início", w=120, tam=19, cor=MUDO), rot(x + 400, 244, "fim", w=100, tam=19, cor=MUDO, alinha="right"),
           rot(x + 24, 92, "casos novos no período", w=490, tam=19, cor=FOSF, peso=700)]
    # taxa
    x = 1128
    rs.append(rot(x + 24, 100, "casos novos", w=490, tam=26, cor=FOSF, peso=700, alinha="center"))
    p.append(f'<line x1="{x + 80}" y1="148" x2="{x + 456}" y2="148" stroke="{TINTA}" stroke-width="3"/>')
    p.append(icone("t:stopwatch", x + 110, 170, 44, TINTA))
    rs.append(rot(x + 164, 176, "horas · sessões · jogos", w=300, tam=22, cor=TINTA, peso=700))
    return slide("vocabulario", 400, p, rs, eyebrow="O vocabulário usado errado", titulo="Três perguntas diferentes",
                 destaque="Trocar uma pela outra é o erro de leitura mais comum da área.", destaque_cor="verm")


def oslo_71():
    """7.1: as quatro perguntas num celular, toda semana, para todo mundo; sai a proporção com algum problema."""
    p = [svg_abre(1664, 420, "À esquerda, um celular com as quatro perguntas de Oslo: participação, teve dificuldade de participar do treino; volume, reduziu volume ou duração; desempenho, o desempenho foi afetado; sintoma, em que grau sentiu. Uma seta diz toda semana, para todo mundo. À direita, o que sai: a proporção do grupo com algum problema em cada semana, em esquema, e não uma contagem de eventos"), defs(MUDO)]
    rs = []
    p.append(f'<rect x="0" y="0" width="620" height="420" rx="40" fill="{TINTA}"/>')
    p.append(f'<rect x="20" y="40" width="580" height="360" rx="20" fill="{CARTAO}"/>')
    p.append(f'<rect x="250" y="16" width="120" height="10" rx="5" fill="{MUDO}"/>')
    itens = [("Participação", "teve dificuldade de participar do treino?", OXID), ("Volume", "reduziu volume ou duração?", OXID),
             ("Desempenho", "o desempenho foi afetado?", GLIC), ("Sintoma", "em que grau sentiu?", FOSF)]
    for k, (t, d, cor) in enumerate(itens):
        y = 56 + k * 86
        p.append(f'<rect x="36" y="{y}" width="548" height="76" rx="12" fill="{PAPEL}" stroke="{cor}" stroke-width="2"/>')
        p.append(f'<circle cx="68" cy="{y + 38}" r="18" fill="{cor}"/>')
        rs += [rot(50, y + 24, str(k + 1), w=36, tam=20, cor=PAPEL, peso=700, alinha="center"),
               rot(100, y + 10, t, w=470, tam=22, cor=cor, peso=700), rot(100, y + 42, d, w=470, tam=19, cor=TINTA)]
    p.append(seta(640, 210, 790, 210, MUDO, "m0", esp=4))
    p.append(icone("t:calendar", 680, 130, 44, TINTA))
    rs += [rot(630, 236, "toda semana, todo mundo", w=170, tam=19, cor=TINTA, peso=700, alinha="center", lh=1.25)]
    X0, B = 830, 330
    vals = [22, 30, 26, 38, 34, 28, 40, 32]
    for k, v in enumerate(vals):
        x = X0 + 20 + k * 100
        h = v * 5.5
        p.append(f'<rect x="{x}" y="{B - h:.0f}" width="72" height="{h:.0f}" rx="4" fill="{GLIC}"/>')
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X0 + 834}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(X0, 0, "% do grupo com algum problema na semana", w=834, tam=22, cor=GLIC, peso=700),
           rot(X0, 36, "proporção, não contagem de eventos · esquema", w=834, tam=19, cor=MUDO),
           rot(X0, 344, "semana a semana", w=834, tam=18, cor=MUDO, alinha="right")]
    return slide("oslo", 420, p, rs, eyebrow="A solução: medir todo mundo, toda semana", titulo="As quatro perguntas de Oslo")


def leitura_71():
    """7.1: sete perguntas em ladrilhos; o oitavo, só então, o número."""
    p = [svg_abre(1664, 420, "Sete perguntas para qualquer estudo, em ladrilhos, e só no oitavo o número. Qual a definição? Resolve o 19 contra o 79. Qual o denominador? Percentual anual esconde o volume. Coleta semanal ou lembrança de um ano? A memória de dor é seletiva. Quem é a população? Novato e experiente não se comparam. Exposição medida ou estimada? As pessoas superestimam o treino. Quem abandonou? Quem some muitas vezes se lesionou. A conclusão cabe no desenho? Estar junto não é causar. Depois disso, o número")]
    rs = []
    itens = [("t:id", "Qual a definição?", "resolve o 19 contra o 79"), ("t:stopwatch", "Qual o denominador?", "percentual anual esconde o volume"),
             ("t:calendar", "Coleta semanal ou lembrança de um ano?", "a memória de dor é seletiva"), ("t:users", "Quem é a população?", "novato e experiente não se comparam"),
             ("t:ruler-measure", "Exposição medida ou estimada?", "as pessoas superestimam o treino"), ("t:door-exit", "Quem abandonou?", "quem some muitas vezes se lesionou"),
             ("t:zoom-question", "A conclusão cabe no desenho?", "estar junto não é causar")]
    for k, (ic, t, d) in enumerate(itens):
        col, lin = k % 2, k // 2
        x, y = col * 840, lin * 106
        p.append(caixa(x, y, 824, 94, OXID if k < 2 else BORDA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 20, y + 23, 46, OXID))
        rs += [rot(x + 86, y + 14, t, w=720, tam=23, cor=TINTA, peso=700), rot(x + 86, y + 52, d, w=720, tam=20, cor=MUDO)]
    p.append(caixa(840, 318, 824, 94, TINTA, TINTA, esp=0, rx=14))
    p.append(icone("t:check", 860, 341, 46, PAPEL))
    rs.append(rot(926, 344, "Depois disso, o número", w=720, tam=26, cor=PAPEL, peso=700, serif=True))
    return slide("leitura", 420, p, rs, eyebrow="Antes de acreditar no número", titulo="Sete perguntas para qualquer estudo")


def rastreio_71():
    """7.1: três degraus subindo; nenhum teste chegou ao terceiro."""
    p = [svg_abre(1664, 400, "Três degraus subindo. Primeiro: associação no tempo, o achado prevê lesão futura em coorte. Segundo: separação real, ponto de corte que funciona em mais de uma população. Terceiro, vazio, com um ponto de interrogação: benefício de intervir só nos marcados, melhor que intervir em todos, ninguém mostrou. Nenhum teste de rastreio de lesão esportiva subiu os três")]
    rs = []
    degs = [("Associação no tempo", "o achado prevê lesão futura em coorte", OXID, OXID_T, 230),
            ("Separação real", "ponto de corte que funciona em mais de uma população", GLIC, GLIC_T, 120),
            ("Benefício de intervir só nos marcados", "melhor que intervir em todos: ninguém mostrou", FOSF, CARTAO, 10)]
    for k, (t, d, cor, fundo, y) in enumerate(degs):
        x = k * 470
        if k < 2:
            p.append(f'<rect x="{x}" y="{y}" width="450" height="{400 - y}" rx="14" fill="{fundo}" stroke="{cor}" stroke-width="2"/>')
        else:
            p.append(f'<rect x="{x}" y="{y}" width="450" height="{400 - y}" rx="14" fill="{fundo}" stroke="{cor}" stroke-width="3"{TRACO}/>')
            rs.append(rot(x, 230, "?", w=450, tam=110, cor=FOSF, peso=700, alinha="center", serif=True))
        p.append(f'<circle cx="{x + 42}" cy="{y + 40}" r="24" fill="{cor}"/>')
        rs += [rot(x + 18, y + 26, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 80, y + 20, t, w=350, tam=24, cor=cor, peso=700, serif=True, lh=1.2),
               rot(x + 24, y + (100 if k == 2 else 82), d, w=400, tam=21, cor=TINTA, lh=1.3)]
    p.append(caixa(1420, 10, 244, 390, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:x", 1512, 40, 60, PAPEL))
    rs.append(rot(1436, 130, "nenhum teste de rastreio de lesão esportiva subiu os três", w=212, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.3))
    return slide("rastreio", 400, p, rs, eyebrow="Fator de risco não é teste de rastreio", titulo="Os três degraus que nenhum teste subiu",
                 fonte="Revisão, Br J Sports Med 2016")

# ---------------------------------------------------------------- 7.2

def cena_72():
    """7.2: uma planilha vazia de um lado; do outro, impressões soltas no lugar do dado."""
    p = [svg_abre(1664, 380, "À esquerda, uma planilha de lesões com as colunas prontas e todas as linhas vazias. À direita, o que ocupa o lugar do dado: impressões soltas. Está aparecendo muita canelite. O problema é o piso da quadra. Teve um ano pior. Ninguém sabe dizer se melhorou ou piorou")]
    rs = []
    p.append(caixa(0, 0, 760, 380, TINTA, CARTAO, esp=2, rx=14))
    cols = ["semana", "nome", "região", "dias"]
    for k, c in enumerate(cols):
        x = k * 190
        p.append(f'<rect x="{x + 2}" y="2" width="{186 if k < 3 else 186}" height="54" fill="{AZUL_T}"/>')
        rs.append(rot(x + 16, 16, c, w=160, tam=21, cor=AZUL, peso=700))
        if k:
            p.append(f'<line x1="{x}" y1="2" x2="{x}" y2="378" stroke="{BORDA}" stroke-width="2"/>')
    for j in range(1, 7):
        y = 56 + j * 52
        p.append(f'<line x1="2" y1="{y}" x2="758" y2="{y}" stroke="{BORDA}" stroke-width="2"/>')
    rs.append(rot(0, 210, "vazia", w=760, tam=40, cor=MUDO, peso=700, alinha="center", serif=True))
    falas = ["“Está aparecendo muita canelite.”", "“O problema é o piso da quadra.”", "“Teve um ano pior.”"]
    for k, t in enumerate(falas):
        y = k * 100
        p.append(caixa(840, y, 620, 80, GLIC, GLIC_T, esp=2, rx=40))
        p.append(icone("t:message-circle", 864, y + 18, 44, GLIC))
        rs.append(rot(924, y + 24, t, w=520, tam=23, cor=TINTA, peso=700))
    p.append(icone("t:zoom-question", 840, 312, 52, FOSF))
    rs.append(rot(908, 318, "melhorou ou piorou? ninguém sabe", w=740, tam=24, cor=FOSF, peso=700))
    return slide("cena", 380, p, rs, eyebrow="A situação mais comum", titulo="Não é que os dados de lesão sejam ruins. É que eles não existem.",
                 destaque="A literatura de vigilância nasceu no clube profissional. Esta aula entrega um sistema que funciona com a equipe e o tempo que você tem.", destaque_cor="tinta")


def perguntas_72():
    """7.2: três perguntas; embaixo, o registro que responde as três contra as vinte colunas que não respondem."""
    p = [svg_abre(1664, 400, "Três perguntas que o registro precisa responder. Quantos agora: quantas pessoas do grupo estão com problema nesta semana. O quê, onde, quando: tipo, região do corpo e momento da temporada. Funcionou: o que eu mudei reduziu o problema. Embaixo, dois registros: um que responde as três, e está bom; outro com vinte colunas que não respondem nenhuma, e não adianta")]
    rs = []
    qs = [("t:users", "Quantos agora?", "quantas pessoas do grupo estão com problema nesta semana", OXID),
          ("t:map", "O quê, onde, quando?", "tipo, região do corpo e momento da temporada", GLIC),
          ("t:chart-line", "Funcionou?", "o que eu mudei reduziu o problema", TINTA)]
    for k, (ic, t, d, cor) in enumerate(qs):
        x = k * 564
        p.append(caixa(x, 0, 536, 220, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 52, cor))
        rs += [rot(x + 92, 34, t, w=420, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 110, d, w=490, tam=23, cor=TINTA, lh=1.3)]
    p.append(caixa(0, 250, 816, 150, OXID, OXID_T, esp=2, rx=16))
    for k in range(3):
        p.append(f'<rect x="{30 + k * 90}" y="290" width="76" height="70" rx="8" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
        p.append(icone("t:check", 30 + k * 90 + 20, 307, 36, OXID))
    rs += [rot(320, 286, "responde as três", w=470, tam=26, cor=OXID, peso=700, serif=True), rot(320, 330, "está bom", w=470, tam=23, cor=TINTA)]
    p.append(caixa(848, 250, 816, 150, FOSF, CARTAO, esp=2, rx=16))
    for j in range(4):
        for i in range(10):
            p.append(f'<rect x="{876 + i * 26}" y="{276 + j * 26}" width="20" height="20" rx="3" fill="{CINZA}"/>')
    p.append(f'<line x1="870" y1="270" x2="1136" y2="380" stroke="{FOSF}" stroke-width="5"/>')
    rs += [rot(1168, 286, "vinte colunas que não respondem", w=480, tam=26, cor=FOSF, peso=700, serif=True, lh=1.15), rot(1168, 356, "não adianta", w=480, tam=23, cor=TINTA)]
    return slide("perguntas", 400, p, rs, eyebrow="O que o registro precisa responder", titulo="Três perguntas, e só três")


def definicao_72():
    """7.2: uma folha com quatro definições e a assinatura de quem coordena."""
    p = [svg_abre(1664, 420, "Uma folha de papel com quatro definições escritas. Lesão: o consenso com restrição para o recreativo; perda de tempo mais sobrecarga no clube. Problema de saúde: inclui doença, porque infecção respiratória também tira do treino. Recorrência: a mesma lesão, no mesmo lugar, depois de retorno completo. Acesso: quem vê o quê. No pé da folha, a assinatura de quem coordena: não muda sem avisar")]
    rs = []
    X, W = 200, 1264
    p.append(f'<path d="M {X} 0 H {X + W - 50} L {X + W} 50 V 420 H {X} Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
    p.append(f'<path d="M {X + W - 50} 0 V 50 H {X + W}" fill="{PAPEL}" stroke="{TINTA}" stroke-width="2"/>')
    itens = [("t:first-aid-kit", "Lesão", "consenso com restrição para o recreativo; perda de tempo mais sobrecarga no clube", OXID),
             ("t:mood-sick", "Problema de saúde", "inclui doença: infecção respiratória também tira do treino", GLIC),
             ("t:refresh", "Recorrência", "a mesma lesão, no mesmo lugar, depois de retorno completo", FOSF),
             ("t:lock", "Acesso", "quem vê o quê", TINTA)]
    for k, (ic, t, d, cor) in enumerate(itens):
        y = 30 + k * 76
        p.append(icone(ic, X + 36, y + 10, 44, cor))
        rs += [rot(X + 100, y + 14, t, w=280, tam=24, cor=cor, peso=700, serif=True), rot(X + 390, y + 16, d, w=820, tam=21, cor=TINTA, lh=1.25)]
        if k < 3:
            p.append(f'<line x1="{X + 36}" y1="{y + 68}" x2="{X + W - 36}" y2="{y + 68}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<path d="M {X + 760} 384 c 30 -40 50 10 80 -20 s 50 20 90 -10 s 40 10 70 -5" fill="none" stroke="{AZUL}" stroke-width="3"/>')
    p.append(f'<line x1="{X + 740}" y1="392" x2="{X + W - 60}" y2="392" stroke="{TINTA}" stroke-width="2"/>')
    p.append(icone("t:writing", X + 36, 350, 44, TINTA))
    rs.append(rot(X + 100, 356, "assinada por quem coordena, e não muda sem avisar", w=620, tam=21, cor=TINTA, peso=700))
    return slide("definicao", 420, p, rs, eyebrow="Passo um · antes de coletar", titulo="A definição escrita numa folha",
                 fonte="Consenso do COI, Br J Sports Med 2020")


def exposicao_72():
    """7.2: quatro contextos, cada um com sua unidade de exposição e o lugar onde ela já está anotada."""
    p = [svg_abre(1664, 420, "Quatro contextos, cada um com a unidade de exposição e o lugar onde o dado já existe. Assessoria de corrida: quilômetros ou minutos por semana, na planilha do aluno. Academia: sessões feitas, na catraca. Clube: horas de treino e minutos de jogo, separados, na lista de presença. Escola ou projeto: sessões oferecidas vezes presença, na chamada"), defs(MUDO)]
    rs = [rot(0, 0, "contexto", w=400, tam=19, cor=MUDO, peso=700), rot(470, 0, "unidade de exposição", w=600, tam=19, cor=OXID, peso=700),
          rot(1190, 0, "onde já está", w=400, tam=19, cor=GLIC, peso=700)]
    itens = [("t:run", "Assessoria de corrida", "km ou minutos por semana", "t:clipboard-list", "a planilha do aluno"),
             ("t:barbell", "Academia", "sessões feitas", "t:door", "a catraca"),
             ("t:soccer-field", "Clube", "horas de treino e minutos de jogo, separados", "t:checklist", "a lista de presença"),
             ("t:school", "Escola ou projeto", "sessões oferecidas × presença", "t:notebook", "a chamada")]
    for k, (ic, ctx, un, ic2, onde) in enumerate(itens):
        y = 40 + k * 96
        p.append(caixa(0, y, 420, 84, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 20, y + 20, 44, TINTA))
        rs.append(rot(80, y + 28, ctx, w=330, tam=22, cor=TINTA, peso=700))
        p.append(seta(424, y + 42, 462, y + 42, MUDO, "m0", esp=3))
        p.append(caixa(470, y, 680, 84, OXID, OXID_T, esp=2, rx=14))
        rs.append(rot(492, y + (28 if len(un) < 40 else 16), un, w=640, tam=22, cor=TINTA, peso=700, lh=1.2))
        p.append(caixa(1190, y, 474, 84, GLIC, CARTAO, esp=2, rx=14))
        p.append(icone(ic2, 1210, y + 20, 44, GLIC))
        rs.append(rot(1270, y + 28, onde, w=380, tam=22, cor=TINTA))
    return slide("exposicao", 420, p, rs, eyebrow="Passo dois · a metade que todo mundo esquece", titulo="Exposição: consistente, não sofisticada",
                 destaque="Quem estava lesionado e não treinou não entra na exposição daquela semana.", destaque_cor="verm")


def ferramentas_72():
    """7.2: o celular com o questionário semanal e a ficha de lesão com oito campos."""
    p = [svg_abre(1664, 420, "Duas ferramentas. À esquerda, um celular com a mensagem semanal de Oslo: quatro perguntas, no mesmo dia, para todo mundo, esteja bem ou não, em trinta segundos. À direita, a ficha de lesão com oito campos: início; região e lado; tipo; súbito ou gradual; o que fazia; se já teve antes; dias restrito; data do retorno, destacada porque sem ela não há gravidade")]
    rs = []
    p.append(f'<rect x="0" y="0" width="560" height="420" rx="40" fill="{TINTA}"/>')
    p.append(f'<rect x="20" y="40" width="520" height="360" rx="20" fill="{CARTAO}"/>')
    p.append(f'<rect x="220" y="16" width="120" height="10" rx="5" fill="{MUDO}"/>')
    rs.append(rot(40, 56, "Questionário semanal de Oslo", w=480, tam=22, cor=OXID, peso=700, serif=True))
    bal = ["quatro perguntas, por mensagem", "mesmo dia, para todo mundo", "esteja bem ou não"]
    for k, t in enumerate(bal):
        y = 104 + k * 70
        p.append(f'<rect x="40" y="{y}" width="430" height="56" rx="18" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        rs.append(rot(60, y + 15, t, w=400, tam=20, cor=TINTA))
    p.append(icone("t:stopwatch", 330, 330, 44, OXID))
    rs.append(rot(384, 338, "30 s", w=140, tam=26, cor=OXID, peso=700))
    X = 620
    p.append(caixa(X, 0, 1044, 420, GLIC, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 18, "Ficha de lesão, oito campos", w=900, tam=24, cor=GLIC, peso=700, serif=True))
    campos = ["início", "região e lado", "tipo", "súbito ou gradual", "o que fazia", "se já teve antes", "dias restrito", "data do retorno"]
    for k, c in enumerate(campos):
        col, lin = k % 2, k // 2
        x, y = X + 24 + col * 506, 74 + lin * 84
        dest = k == 7
        rs.append(rot(x, y, c, w=460, tam=20, cor=FOSF if dest else TINTA, peso=700))
        p.append(f'<rect x="{x}" y="{y + 32}" width="470" height="40" rx="6" fill="{FOSF_T if dest else PAPEL}" stroke="{FOSF if dest else BORDA}" stroke-width="2"/>')
    return slide("ferramentas", 420, p, rs, eyebrow="Passo três · duas ferramentas", titulo="Mais que isso ninguém sustenta",
                 destaque="Sem data de retorno não há gravidade. E se a ficha exigir computador, não vai ser preenchida.", destaque_cor="tinta",
                 fonte="Questionários do OSTRC, Br J Sports Med 2020")


def indicadores_72():
    """7.2: três indicadores, cada um escrito como conta."""
    p = [svg_abre(1664, 380, "Três indicadores, cada um escrito como conta. Proporção semanal: gente com algum problema na semana, dividida pelo grupo; o número de toda segunda-feira. Incidência: lesões novas divididas por mil horas ou mil sessões. Carga de lesão: frequência vezes gravidade, na prática dias perdidos por mil horas")]
    rs = []
    itens = [("Proporção semanal", "com algum problema", "o grupo na semana", "o número de toda segunda-feira", OXID, OXID_T),
             ("Incidência", "lesões novas", "mil horas ou mil sessões", "compara períodos, categorias e a literatura", GLIC, GLIC_T),
             ("Carga de lesão", "dias perdidos", "mil horas", "frequência × gravidade", FOSF, FOSF_T)]
    for k, (t, num, den, d, cor, fundo) in enumerate(itens):
        x = k * 564
        p.append(caixa(x, 0, 536, 380, cor, CARTAO, esp=2 if k < 2 else 4, rx=16))
        p.append(f'<rect x="{x}" y="0" width="536" height="84" rx="16" fill="{fundo}"/>')
        rs.append(rot(x + 24, 24, t, w=490, tam=28, cor=cor, peso=700, serif=True))
        rs.append(rot(x + 24, 120, num, w=490, tam=26, cor=TINTA, peso=700, alinha="center"))
        p.append(f'<line x1="{x + 80}" y1="168" x2="{x + 456}" y2="168" stroke="{cor}" stroke-width="3"/>')
        rs += [rot(x + 24, 180, den, w=490, tam=24, cor=TINTA, peso=700, alinha="center"),
               rot(x + 24, 280, d, w=490, tam=22, cor=cor if k == 2 else TINTA, peso=700 if k == 2 else 400, alinha="center", lh=1.3)]
    return slide("indicadores", 380, p, rs, eyebrow="Passo quatro · indicadores", titulo="Não são dez. São três",
                 destaque="Bahr e colegas, 2018: olhar a carga, e não só a incidência.", destaque_cor="tinta", fonte="Bahr, Clarsen e Ekstrand, Br J Sports Med 2018")


def carga_72():
    """7.2: duas equipes com dez lesões cada; os blocos de dias perdidos mostram 30 contra 250."""
    p = [svg_abre(1664, 340, "Duas equipes, dez lesões cada, desenhadas como dez blocos de dias perdidos na mesma escala. Equipe A: dez entorses leves de tornozelo, três dias cada, somam 30 dias. Equipe B: dez lesões de posterior de coxa, vinte e cinco dias cada, somam 250 dias. Mesma incidência, outra realidade. Exemplo de conta")]
    rs = []
    X0, E = 0, 4.6
    for k, (dias, t, tot, cor) in enumerate([(3, "dez entorses leves de tornozelo, 3 dias cada", "30 dias", OXID),
                                              (25, "dez lesões de posterior de coxa, 25 dias cada", "250 dias", FOSF)]):
        y = k * 150
        rs.append(rot(0, y, t, w=1100, tam=22, cor=TINTA, peso=700))
        for i in range(10):
            x = X0 + i * dias * E
            p.append(f'<rect x="{x:.0f}" y="{y + 40}" width="{dias * E - 2:.0f}" height="70" rx="4" fill="{cor}"/>')
        rs.append(rot(X0 + 10 * dias * E + 24, y + 46, tot, w=300, tam=44, cor=cor, peso=700, serif=True))
    p.append(f'<line x1="0" y1="300" x2="{250 * E:.0f}" y2="300" stroke="{MUDO}" stroke-width="2"/>')
    for t in range(0, 251, 50):
        p.append(f'<line x1="{t * E:.0f}" y1="300" x2="{t * E:.0f}" y2="310" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(0, 314, "dias perdidos · cada bloco é uma lesão · exemplo de conta", w=1200, tam=18, cor=MUDO))
    p.append(caixa(1424, 40, 240, 220, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1434, 70, "10 = 10", w=220, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1434, 140, "mesma incidência, outra realidade", w=220, tam=21, cor=PAPEL, alinha="center", lh=1.3)]
    return slide("carga", 340, p, rs, eyebrow="Mesma incidência, outra realidade", titulo="Duas equipes, dez lesões cada",
                 destaque="Quem olha incidência cuida do que é frequente. Quem olha carga cuida do que custa caro, e é isso que decide temporada.",
                 destaque_cor="tinta", fonte="Exemplo de conta")


def devolutiva_72():
    """7.2: a página do mês com quatro blocos, voltando para quem respondeu."""
    p = [svg_abre(1664, 400, "Uma página por mês, com quatro blocos: a proporção do mês, quantos tiveram algum problema; as três regiões mais frequentes no período; os dias perdidos, o que custou caro; e uma frase sobre o que muda no planejamento. Uma seta leva a página de volta ao grupo que respondeu toda semana"), defs(OXID)]
    rs = []
    X, W = 0, 1060
    p.append(caixa(X, 0, W, 400, TINTA, CARTAO, esp=2, rx=14))
    rs.append(rot(X + 24, 16, "Devolutiva do mês", w=600, tam=22, cor=TINTA, peso=700, serif=True))
    itens = [("t:users", "Proporção do mês", "quantos tiveram algum problema", OXID), ("t:target", "Três regiões", "as mais frequentes no período", GLIC),
             ("t:hourglass", "Dias perdidos", "o que custou caro", FOSF), ("t:writing", "O que muda", "uma frase sobre o planejamento", TINTA)]
    for k, (ic, t, d, cor) in enumerate(itens):
        col, lin = k % 2, k // 2
        x, y = X + 24 + col * 512, 64 + lin * 166
        p.append(caixa(x, y, 492, 150, cor, PAPEL, esp=2, rx=12))
        p.append(icone(ic, x + 18, y + 18, 44, cor))
        rs += [rot(x + 76, y + 24, t, w=400, tam=24, cor=cor, peso=700), rot(x + 18, y + 86, d, w=456, tam=21, cor=TINTA, lh=1.3)]
    p.append(f'<path d="M {W + 10} 200 C {W + 120} 200, {W + 140} 200, {W + 230} 200" fill="none" stroke="{OXID}" stroke-width="4" marker-end="url(#m0)"/>')
    p.append(caixa(1310, 60, 354, 280, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:users-group", 1447, 90, 80, OXID))
    rs.append(rot(1326, 200, "volta para quem respondeu toda semana", w=322, tam=22, cor=OXID, peso=700, alinha="center", lh=1.3))
    return slide("devolutiva", 400, p, rs, eyebrow="A parte mais ignorada", titulo="Devolutiva: uma página por mês",
                 destaque="Quem responde toda semana e nunca vê nada voltar, para de responder.", destaque_cor="verm")


def lgpd_72():
    """7.2: o dado sensível no centro, com cadeado, e os cinco cuidados em volta."""
    p = [svg_abre(1664, 420, "O dado de saúde no centro, com um cadeado: dado pessoal sensível. Em volta, cinco cuidados. Consentimento: o que se coleta, para quê, quem vê; menor assina o responsável. Acesso por função: o treinador vê a condição de treino, não o diagnóstico. Nada em grupo de mensagem: o que circula é liberado, com restrição ou fora. Relatório agregado, sem nome. Prazo e dono: onde fica, por quanto tempo, e o que acontece quando o atleta sai")]
    rs = []
    p.append(caixa(612, 0, 440, 190, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:lock", 798, 20, 68, PAPEL))
    rs.append(rot(628, 104, "dado de saúde é dado pessoal sensível", w=408, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.3))
    itens = [((0, 0), "Consentimento", "o que se coleta, para quê, quem vê; menor assina o responsável", OXID, "t:writing"),
             ((0, 220), "Acesso por função", "treinador vê a condição de treino, não o diagnóstico", GLIC, "t:key"),
             ((1104, 0), "Nada em grupo de mensagem", "", FOSF, "t:message-off"),
             ((1104, 220), "Relatório agregado", "sem nome", OXID, "t:users-group"),
             ((612, 220), "Prazo e dono", "onde fica, por quanto tempo, e quando o atleta sai", TINTA, "t:calendar")]
    for (x, y), t, d, cor, ic in itens:
        w = 440 if x == 612 else 560
        p.append(caixa(x, y, w, 200, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 20, y + 20, 44, cor))
        rs.append(rot(x + 78, y + 26, t, w=w - 96, tam=23, cor=cor, peso=700, lh=1.15))
        if d:
            rs.append(rot(x + 20, y + 96, d, w=w - 40, tam=21, cor=TINTA, lh=1.3))
    for k, (t, cor) in enumerate([("liberado", OXID), ("com restrição", GLIC), ("fora", FOSF)]):
        x = 1124 + k * 176
        p.append(f'<rect x="{x}" y="110" width="164" height="50" rx="25" fill="{cor}"/>')
        rs.append(rot(x, 122, t, w=164, tam=19, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(1124, 168, "o que circula", w=520, tam=17, cor=MUDO))
    return slide("lgpd", 420, p, rs, eyebrow="Passo seis · dado de saúde é dado sensível", titulo="O cuidado que protege todo mundo",
                 fonte="Lei 13.709/2018, art. 5º, II")


def painel_72():
    """7.2: o painel de uma página com quatro blocos desenhados, ao lado dos quatro erros riscados."""
    p = [svg_abre(1664, 420, "À esquerda, o painel de uma página com quatro blocos: a proporção semanal, uma linha que é o pulso do grupo; as regiões mais atingidas, em ordem; os dias perdidos por mil horas; as recorrências, espelho do retorno. À direita, os quatro erros que estragam o registro, riscados: registrar só quem procurou atendimento; lesão sem exposição; mudar a definição no meio; coletar sem devolver")]
    rs = []
    p.append(caixa(0, 0, 900, 420, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "Painel de uma página", w=600, tam=24, cor=OXID, peso=700, serif=True))
    blocos = [("proporção semanal: o pulso", (24, 64)), ("regiões mais atingidas", (462, 64)),
              ("dias perdidos por mil horas", (24, 244)), ("recorrências: o espelho do retorno", (462, 244))]
    for t, (x, y) in blocos:
        p.append(f'<rect x="{x}" y="{y}" width="414" height="164" rx="10" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
        rs.append(rot(x + 16, y + 12, t, w=390, tam=19, cor=TINTA, peso=700))
    # pulso
    p.append(f'<polyline points="44,190 100,170 156,180 212,140 268,160 324,130 400,150" fill="none" stroke="{OXID}" stroke-width="3"/>')
    # regiões em ordem
    for k, w in enumerate([300, 220, 150]):
        p.append(f'<rect x="482" y="{110 + k * 34}" width="{w}" height="24" rx="4" fill="{GLIC}"/>')
    # dias perdidos
    for k, h in enumerate([50, 80, 40, 100, 60]):
        p.append(f'<rect x="{60 + k * 70}" y="{392 - h}" width="44" height="{h}" rx="4" fill="{FOSF}"/>')
    # recorrências
    p.append(icone("t:refresh", 640, 300, 64, AZUL))
    rs.append(rot(24, 384, "esquema", w=850, tam=16, cor=MUDO, alinha="right"))
    X = 960
    p.append(caixa(X, 0, 704, 420, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 16, "Erros que estragam o registro", w=660, tam=24, cor=FOSF, peso=700, serif=True))
    erros = ["registrar só quem procurou atendimento", "lesão sem exposição", "mudar a definição no meio", "coletar sem devolver"]
    for k, t in enumerate(erros):
        y = 76 + k * 84
        p.append(icone("t:x", X + 24, y, 40, FOSF))
        rs.append(rot(X + 80, y + 6, t, w=600, tam=22, cor=TINTA))
    return slide("painel", 420, p, rs, eyebrow="Para montar nesta semana", titulo="O painel mínimo e os quatro erros")

# ---------------------------------------------------------------- 7.3

def cena_73():
    """7.3: centenas de sprints sem problema na semana, dezenas na partida, e só o último marcado."""
    p = [svg_abre(1664, 340, "Uma linha do tempo de sprints, em esquema. Centenas de traços cinzas na semana anterior, sem problema. Dezenas na partida, também cinzas. Só o último traço é vermelho: o sprint em que a lesão apareceu. A diferença entre ele e os outros não está no sprint")]
    rs = []
    import random
    r = random.Random(7)
    for i in range(110):
        x = 10 + i * 8.6 + r.uniform(-2, 2)
        p.append(f'<line x1="{x:.0f}" y1="120" x2="{x:.0f}" y2="{120 - r.uniform(40, 90):.0f}" stroke="{CINZA}" stroke-width="3"/>')
    for i in range(34):
        x = 1010 + i * 13 + r.uniform(-2, 2)
        p.append(f'<line x1="{x:.0f}" y1="120" x2="{x:.0f}" y2="{120 - r.uniform(40, 90):.0f}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="1500" y1="120" x2="1500" y2="20" stroke="{FOSF}" stroke-width="8"/>')
    p.append(f'<line x1="0" y1="122" x2="1560" y2="122" stroke="{TINTA}" stroke-width="2"/>')
    p.append(f'<line x1="990" y1="20" x2="990" y2="140" stroke="{BORDA}" stroke-width="2"{TRACO}/>')
    p.append(icone("h:running", 1530, 30, 80, FOSF))
    rs += [rot(10, 140, "centenas na semana anterior, sem problema", w=960, tam=22, cor=MUDO, peso=700),
           rot(1010, 140, "dezenas na partida", w=460, tam=22, cor=TINTA, peso=700),
           rot(1380, 140, "este", w=240, tam=24, cor=FOSF, peso=700, alinha="right"),
           rot(10, 300, "cada traço é um sprint · esquema", w=900, tam=18, cor=MUDO)]
    p.append(caixa(0, 200, 1664, 80, FOSF, FOSF_T, esp=0, rx=14))
    rs.append(rot(24, 222, "A diferença entre aquele sprint e os outros não está no sprint.", w=1610, tam=26, cor=FOSF, peso=700, serif=True))
    return slide("cena", 340, p, rs, eyebrow="A pergunta de sempre", titulo="“Foi no sprint, então foi o sprint.”")


def mecanismo_73():
    """7.3: o mecanismo é um instante; a causa está nas semanas anteriores."""
    p = [svg_abre(1664, 400, "Dois quadros. Mecanismo: um instante, o que acontecia quando o tecido falhou: sprint, mudança de direção, contato, aterrissagem; diz onde e como a carga chega. Causa: uma fileira de semanas antes do dia, por que o tecido não aguentou, naquele dia, o que aguentava antes; está nas semanas anteriores")]
    rs = []
    p.append(caixa(0, 0, 800, 400, OXID, CARTAO, esp=2, rx=16))
    p.append(icone("t:bolt", 24, 22, 52, OXID))
    rs += [rot(92, 30, "Mecanismo", w=600, tam=30, cor=OXID, peso=700, serif=True),
           rot(24, 96, "o que acontecia quando o tecido falhou", w=750, tam=23, cor=TINTA, peso=700)]
    for k, (ic, t) in enumerate([("t:run", "sprint"), ("t:arrows-exchange", "mudança de direção"), ("t:users", "contato"), ("t:arrow-down-right", "aterrissagem")]):
        x, y = 24 + (k % 2) * 380, 150 + (k // 2) * 76
        p.append(f'<rect x="{x}" y="{y}" width="360" height="62" rx="31" fill="{OXID_T}"/>')
        p.append(icone(ic, x + 16, y + 13, 36, OXID))
        rs.append(rot(x + 62, y + 18, t, w=290, tam=21, cor=TINTA, peso=700))
    rs.append(rot(24, 330, "diz onde e como a carga chega", w=750, tam=22, cor=OXID))
    X = 864
    p.append(caixa(X, 0, 800, 400, FOSF, CARTAO, esp=2, rx=16))
    p.append(icone("t:calendar", X + 24, 22, 52, FOSF))
    rs += [rot(X + 92, 30, "Causa", w=600, tam=30, cor=FOSF, peso=700, serif=True),
           rot(X + 24, 96, "por que o tecido não aguentou, naquele dia, o que aguentava antes", w=750, tam=23, cor=TINTA, peso=700, lh=1.25)]
    for k in range(6):
        x = X + 24 + k * 108
        p.append(f'<rect x="{x}" y="196" width="96" height="70" rx="8" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
        rs.append(rot(x, 218, f"sem {k + 1}", w=96, tam=18, cor=FOSF, alinha="center"))
    p.append(f'<rect x="{X + 24 + 6 * 108}" y="186" width="80" height="90" rx="8" fill="{FOSF}"/>')
    p.append(icone("t:bolt", X + 24 + 6 * 108 + 22, 213, 36, PAPEL))
    rs.append(rot(X + 24, 330, "está nas semanas anteriores", w=750, tam=22, cor=FOSF))
    return slide("mecanismo", 400, p, rs, eyebrow="Erro um", titulo="Confundir mecanismo com causa",
                 destaque="Quem responde só o mecanismo proíbe o mecanismo, e o atleta volta menos preparado para ele.", destaque_cor="verm",
                 fonte="Revisão sobre mecanismos de lesão, Br J Sports Med 2005")


def modelo_73():
    """7.3: internos tornam o atleta predisposto, externos o tornam suscetível, o evento fecha em lesão."""
    p = [svg_abre(1664, 380, "O modelo em três blocos. Fatores internos, como idade, sexo, composição, força, controle motor e histórico, deixam o atleta predisposto. Fatores externos, como carga, calendário, superfície, equipamento e clima, deixam o atleta predisposto também suscetível. O evento desencadeante, o mecanismo, fecha a cadeia em lesão"), defs(MUDO)]
    rs = []
    fat = [("Fatores internos", "idade, sexo, composição, força, controle motor, histórico", OXID, OXID_T, 0, 520),
           ("Fatores externos", "carga, calendário, superfície, equipamento, clima", GLIC, GLIC_T, 572, 520),
           ("Evento desencadeante", "o mecanismo do erro um", FOSF, FOSF_T, 1144, 520)]
    est = ["atleta predisposto", "atleta suscetível", "lesão"]
    for k, (t, d, cor, fundo, x, w) in enumerate(fat):
        p.append(caixa(x, 0, w, 190, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 20, t, w=w - 48, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 72, d, w=w - 48, tam=22, cor=TINTA, lh=1.3)]
        p.append(seta(x + w / 2, 194, x + w / 2, 262, MUDO, "m0", esp=3))
        fundo2, cor2 = (TINTA, PAPEL) if k == 2 else (CARTAO, cor)
        p.append(caixa(x + 60, 270, w - 120, 100, cor if k < 2 else TINTA, fundo2, esp=2, rx=50))
        rs.append(rot(x + 60, 300, est[k], w=w - 120, tam=26, cor=cor2, peso=700, alinha="center", serif=True))
        if k < 2:
            p.append(seta(x + w - 58, 320, x + 572 + 56, 320, MUDO, "m0", esp=3))
    return slide("modelo", 380, p, rs, eyebrow="Erro dois · achar que existe um fator", titulo="O modelo multifatorial de Meeuwisse, 1994",
                 destaque="Encurtamento, desequilíbrio, pisada, piso, alongamento: nenhum deles, sozinho, produz lesão.", destaque_cor="tinta",
                 fonte="Clin J Sport Med 1994")


def copo_73():
    """7.3: dois copos do mesmo tamanho e a mesma gota; num sobra espaço, no outro transborda."""
    p = [svg_abre(1664, 400, "Dois copos do mesmo tamanho, que é dado pelos fatores internos. Os fatores externos enchem cada copo ao longo das semanas. Sobre os dois cai a mesma gota, o mecanismo. No primeiro momento da temporada sobra espaço e nada acontece; no segundo, o copo está quase cheio e a mesma gota transborda. Não existe exercício perigoso em si: existe exercício mal dosado para aquele copo, naquele dia")]
    rs = []
    def copo(x0, nivel, cor_liq):
        w, top, base = 300, 90, 380
        p.append(f'<path d="M {x0 + 30} {base} L {x0 + w - 30} {base} L {x0 + w} {top} L {x0} {top} Z" fill="{CARTAO}"/>')
        y = base - (base - top) * nivel
        fr = (y - top) / (base - top)
        xl, xr = x0 + 30 * fr, x0 + w - 30 * fr
        p.append(f'<path d="M {x0 + 30} {base} L {x0 + w - 30} {base} L {xr:.0f} {y:.0f} L {xl:.0f} {y:.0f} Z" fill="{cor_liq}" opacity="0.85"/>')
        p.append(f'<path d="M {x0} {top} L {x0 + 30} {base} L {x0 + w - 30} {base} L {x0 + w} {top}" fill="none" stroke="{TINTA}" stroke-width="4"/>')
        cx = x0 + w / 2
        p.append(f'<path d="M {cx} 0 C {cx + 4} 14, {cx + 16} 26, {cx + 16} 38 A 16 16 0 0 1 {cx - 16} 38 C {cx - 16} 26, {cx - 4} 14, {cx} 0 Z" fill="{FOSF}"/>')
    copo(0, 0.5, GLIC)
    copo(420, 0.97, GLIC)
    p.append(f'<path d="M 720 92 q 14 30 6 80" fill="none" stroke="{GLIC}" stroke-width="6" stroke-linecap="round"/>')
    rs += [rot(0, 170, "sobra espaço", w=300, tam=22, cor=TINTA, peso=700, alinha="center"),
           rot(420, 180, "transborda", w=300, tam=22, cor=PAPEL, peso=700, alinha="center")]
    leg = [("o tamanho do copo", "fatores internos", TINTA), ("o que enche, semana a semana", "fatores externos", GLIC), ("a última gota", "o mecanismo", FOSF)]
    for k, (t, d, cor) in enumerate(leg):
        y = 10 + k * 130
        p.append(caixa(860, y, 804, 110, cor, CARTAO, esp=2, rx=14))
        rs += [rot(884, y + 18, t, w=760, tam=25, cor=cor, peso=700, serif=True), rot(884, y + 62, d, w=760, tam=22, cor=TINTA)]
    return slide("copo", 400, p, rs, eyebrow="A imagem para explicar ao atleta", titulo="Todo mundo discute a gota. Quase ninguém discute quem encheu o copo.",
                 destaque="Não existe exercício perigoso em si: existe exercício mal dosado para aquele copo, naquele dia.", destaque_cor="tinta")


def padrao_73():
    """7.3: um fator isolado, riscado; ao lado, cinco fatores ligados em rede formando um padrão."""
    p = [svg_abre(1664, 400, "À esquerda, um fator isolado: força de quadril baixa. Sozinha, não prediz lesão, e nenhum teste de rastreio passou. À direita, uma rede: força baixa, joelho para dentro na aterrissagem, calendário congestionado, pouco sono e lesão no mesmo membro no ano anterior, todos ligados entre si. Não são cinco fatores somados: são um padrão, e padrão se reconhece")]
    rs = []
    p.append(caixa(0, 0, 520, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 20, "Fator isolado", w=470, tam=27, cor=FOSF, peso=700, serif=True))
    p.append(f'<circle cx="260" cy="170" r="60" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(icone("t:barbell", 230, 140, 60, FOSF))
    rs += [rot(24, 244, "força de quadril baixa", w=470, tam=23, cor=TINTA, peso=700, alinha="center"),
           rot(24, 286, "sozinha, não prediz lesão", w=470, tam=21, cor=TINTA, alinha="center"),
           rot(24, 330, "nenhum teste de rastreio passou (Bahr, 2016)", w=470, tam=20, cor=FOSF, alinha="center")]
    X = 580
    p.append(caixa(X, 0, 1084, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 20, "Padrão", w=400, tam=27, cor=OXID, peso=700, serif=True))
    nos = [(1122, 90, "t:arrow-down-right"), (1436, 176, "t:calendar"), (1316, 316, "t:moon"), (928, 316, "t:refresh"), (808, 176, "t:barbell")]
    for i in range(5):
        a, b = nos[i], nos[(i + 1) % 5]
        p.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{OXID}" stroke-width="2" opacity="0.5"/>')
        p.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="1122" y2="215" stroke="{OXID}" stroke-width="2" opacity="0.5"/>')
    p.append(f'<circle cx="1122" cy="215" r="52" fill="{TINTA}"/>')
    for cx, cy, ic in nos:
        p.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{OXID}"/>')
        p.append(icone(ic, cx - 18, cy - 18, 36, PAPEL))
    rs += [rot(1070, 202, "padrão", w=104, tam=20, cor=PAPEL, peso=700, alinha="center"),
           rot(1166, 76, "joelho para dentro", w=300, tam=20, cor=TINTA, peso=700),
           rot(1478, 152, "calendário congestionado", w=180, tam=20, cor=TINTA, peso=700, lh=1.15),
           rot(1360, 304, "pouco sono", w=200, tam=20, cor=TINTA, peso=700),
           rot(600, 292, "lesão no mesmo membro no ano anterior", w=286, tam=20, cor=TINTA, peso=700, alinha="right", lh=1.15),
           rot(600, 164, "força baixa", w=166, tam=20, cor=TINTA, peso=700, alinha="right")]
    return slide("padrao", 400, p, rs, eyebrow="Erro quatro · caçar o preditor", titulo="De fator de risco a reconhecimento de padrão",
                 destaque="Bittencourt e o grupo da UFMG, 2016: a lesão emerge de uma rede de determinantes que interagem.", destaque_cor="petr",
                 fonte="Br J Sports Med 2016 (rastreio; sistemas complexos)")


def razao_73():
    """7.3: o painel com zona vermelha, riscado, e os três problemas da conta."""
    p = [svg_abre(1664, 400, "À esquerda, em esquema, o painel de software com uma faixa considerada segura e uma zona de perigo em vermelho, riscado. À direita, os três problemas da razão entre carga aguda e crônica. Estatística: a própria razão distorce a leitura. Pontos de corte: variam de estudo para estudo, sem justificativa. Uso para decidir treino: sem evidência de que reduza lesão")]
    rs = []
    p.append(caixa(0, 0, 640, 400, TINTA, CARTAO, esp=2, rx=16))
    p.append(f'<rect x="40" y="60" width="560" height="80" fill="{FOSF_T}"/>')
    p.append(f'<rect x="40" y="170" width="560" height="90" fill="{OXID_T}"/>')
    p.append(f'<polyline points="50,250 120,230 190,240 260,200 330,190 400,150 470,110 540,130 590,90" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    rs += [rot(220, 70, "zona de perigo", w=200, tam=19, cor=FOSF, peso=700, alinha="center"), rot(50, 176, "faixa “segura”", w=230, tam=19, cor=OXID, peso=700),
           rot(40, 340, "esquema", w=560, tam=17, cor=MUDO, alinha="right")]
    p.append(f'<line x1="30" y1="30" x2="610" y2="320" stroke="{FOSF}" stroke-width="7"/>')
    p.append(f'<line x1="610" y1="30" x2="30" y2="320" stroke="{FOSF}" stroke-width="7"/>')
    itens = [("t:chart-bar", "Estatística", "a própria razão distorce a leitura", FOSF), ("t:adjustments-horizontal", "Pontos de corte", "variam de estudo para estudo, sem justificativa", GLIC),
             ("t:x", "Uso para decidir treino", "sem evidência de que reduza lesão", FOSF)]
    for k, (ic, t, d, cor) in enumerate(itens):
        y = k * 136
        p.append(caixa(700, y, 964, 124, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 724, y + 38, 48, cor))
        rs += [rot(796, y + 22, t, w=840, tam=25, cor=cor, peso=700, serif=True), rot(796, y + 68, d, w=840, tam=22, cor=TINTA)]
    return slide("razao", 400, p, rs, eyebrow="Razão entre carga aguda e crônica", titulo="A ideia estava certa, a conta estava frágil",
                 destaque="Não entregue a decisão a um número em vermelho, nem diga ao atleta que ele está numa zona de perigo.", destaque_cor="tinta",
                 fonte="Crítica metodológica, Int J Sports Physiol Perform 2020")


def colunas_73():
    """7.3: três colunas; sobre a do meio, uma pilha de recibos."""
    p = [svg_abre(1664, 420, "Três colunas. Não modificáveis: idade, sexo, estrutura, histórico; servem para calibrar expectativa. Vendidos como modificáveis: pisada, palmilha de loja, alongamento para prevenir; sobre esta coluna, uma pilha de recibos, sem retorno demonstrado. Modificáveis com retorno: carga, força, sono, energia, reabilitação completa; é onde investir")]
    rs = []
    cols = [("Não modificáveis", "idade, sexo, estrutura, histórico", "calibrar expectativa", MUDO, PAPEL, "t:lock"),
            ("Vendidos como modificáveis", "pisada, palmilha de loja, alongamento para prevenir", "sem retorno demonstrado", FOSF, FOSF_T, "t:x"),
            ("Modificáveis com retorno", "carga, força, sono, energia, reabilitação completa", "onde investir", OXID, OXID_T, "t:trending-up")]
    for k, (t, e, s, cor, fundo, ic) in enumerate(cols):
        x = k * 564
        p.append(caixa(x, 0, 536, 420, cor, CARTAO, esp=2 if k < 2 else 4, rx=16))
        rs += [rot(x + 24, 22, t, w=490, tam=27, cor=cor if k else TINTA, peso=700, serif=True), rot(x + 24, 80, e, w=490, tam=23, cor=TINTA, lh=1.3)]
        p.append(f'<rect x="{x + 24}" y="330" width="488" height="66" rx="33" fill="{fundo}"/>')
        p.append(icone(ic, x + 44, 345, 36, cor))
        rs.append(rot(x + 92, 350, s, w=410, tam=22, cor=cor if k else TINTA, peso=700))
    for j in range(5):
        x, y = 564 + 150 + j * 10, 160 + j * 22
        ang = (-6, 4, -3, 7, -2)[j]
        p.append(f'<g transform="rotate({ang} {x + 110} {y + 40})"><rect x="{x}" y="{y}" width="220" height="80" rx="4" fill="{CARTAO}" stroke="{FOSF}" stroke-width="2"/>'
                 f'<line x1="{x + 16}" y1="{y + 24}" x2="{x + 150}" y2="{y + 24}" stroke="{BORDA}" stroke-width="3"/>'
                 f'<line x1="{x + 16}" y1="{y + 44}" x2="{x + 190}" y2="{y + 44}" stroke="{BORDA}" stroke-width="3"/>'
                 f'<line x1="{x + 120}" y1="{y + 64}" x2="{x + 200}" y2="{y + 64}" stroke="{FOSF}" stroke-width="3"/></g>')
    return slide("colunas", 420, p, rs, eyebrow="A pasta com recibos", titulo="Três colunas em vez de duas",
                 destaque="Das coisas que você fez nesses meses, quantas mexeram na terceira coluna?", destaque_cor="verm",
                 fonte="Coorte de pronação e metanálise de prevenção, Br J Sports Med 2014")

# ---------------------------------------------------------------- 7.4

def palavra_74():
    """7.4: uma faixa que vai da sobrecarga de poucos dias à ruptura do tendão de meses, e os quatro passos."""
    p = [svg_abre(1664, 360, "Uma faixa contínua sob a frase teve uma lesão muscular. Numa ponta, a sobrecarga que passa em poucos dias; na outra, a ruptura que envolve o tendão e leva meses. Embaixo, os quatro passos: o que falha, a avaliação, a imagem e a classificação"), defs(MUDO),
         f'<defs><linearGradient id="g74" x1="0" x2="1"><stop offset="0" stop-color="{OXID}"/><stop offset="0.5" stop-color="{GLIC}"/><stop offset="1" stop-color="{FOSF}"/></linearGradient></defs>']
    rs = []
    p.append('<rect x="0" y="60" width="1664" height="44" rx="22" fill="url(#g74)"/>')
    rs += [rot(0, 0, "sobrecarga que passa em poucos dias", w=700, tam=24, cor=OXID, peso=700),
           rot(964, 0, "ruptura que envolve o tendão e leva meses", w=700, tam=24, cor=FOSF, peso=700, alinha="right"),
           rot(0, 120, "tudo isso cabe na mesma frase", w=1664, tam=22, cor=MUDO, alinha="center")]
    passos = [("t:bolt", "o que falha"), ("t:stethoscope", "a avaliação"), ("t:eye", "a imagem"), ("t:list-check", "a classificação")]
    for k, (ic, t) in enumerate(passos):
        x = k * 424
        p.append(caixa(x, 200, 392, 120, TINTA, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 46}" cy="260" r="26" fill="{TINTA}"/>')
        p.append(icone(ic, x + 300, 236, 48, TINTA))
        rs += [rot(x + 20, 246, str(k + 1), w=52, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(x + 88, 244, t, w=210, tam=24, cor=TINTA, peso=700)]
        if k < 3:
            p.append(seta(x + 394, 260, x + 420, 260, MUDO, "m0", esp=3))
    return slide("palavra", 360, p, rs, eyebrow="Uma palavra que esconde tudo", titulo="“Teve uma lesão muscular.”")


def tamanho_74():
    """7.4: duas barras, 12% na primeira temporada e 24% na mais recente, com a linha dos 19% no conjunto."""
    p = [svg_abre(1664, 360, "Proporção de lesões de posterior de coxa no futebol de elite europeu. Uma barra de 12% na primeira temporada e outra de 24% na mais recente, o dobro. Uma linha tracejada marca 19%, a proporção no conjunto das vinte e uma temporadas"), defs(FOSF)]
    rs = []
    B, E = 320, 11
    for x, v, t, cor in [(200, 12, "primeira temporada", OXID), (900, 24, "temporada mais recente", FOSF)]:
        p.append(f'<rect x="{x}" y="{B - v * E}" width="260" height="{v * E}" rx="6" fill="{cor}"/>')
        rs += [rot(x, B - v * E - 60, f"{v}%", w=260, tam=48, cor=cor, peso=700, alinha="center", serif=True),
               rot(x - 40, B + 10, t, w=340, tam=21, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="120" y1="{B - 19 * E}" x2="1280" y2="{B - 19 * E}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs.append(rot(1300, B - 19 * E - 34, "19%", w=360, tam=40, cor=TINTA, peso=700, serif=True))
    rs.append(rot(1300, B - 19 * E + 18, "no conjunto das 21 temporadas", w=360, tam=21, cor=TINTA))
    p.append(f'<path d="M 470 {B - 12 * E - 20} C 650 {B - 12 * E - 60}, 760 {B - 24 * E + 40}, 880 {B - 24 * E + 20}" fill="none" stroke="{FOSF}" stroke-width="3" marker-end="url(#m0)"/>')
    p.append(f'<line x1="120" y1="{B}" x2="1280" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    return slide("tamanho", 360, p, rs, eyebrow="O tamanho do problema", titulo="Posterior de coxa no futebol de elite europeu",
                 destaque="Quase uma em cada quatro lesões, num único grupo muscular, e crescendo.", destaque_cor="verm",
                 fonte="Estudo de lesões dos clubes de elite da UEFA, Br J Sports Med 2023")


def mecanismos_74():
    """7.4: dois cenários, cada um com o músculo puxado nas duas pontas enquanto contrai."""
    p = [svg_abre(1664, 420, "Dois cenários de alongamento sob tensão, cada um com um músculo desenhado sendo puxado nas duas pontas enquanto contrai. Corrida em alta velocidade: no fim do balanço da perna, os isquiotibiais freiam enquanto alongam; pega a cabeça longa do bíceps femoral; a mais comum no jogador e no velocista. Alongamento extremo: chute alto, abertura, carrinho, dança; dor mais alta, perto do quadril; pouca perda de função no primeiro dia; recuperação mais longa"), defs(OXID, FOSF)]
    rs = []
    cen = [("h:running", "Corrida em alta velocidade", ["fim do balanço da perna", "isquiotibiais freiam enquanto alongam", "cabeça longa do bíceps femoral", "a mais comum no jogador e no velocista"], OXID, "m0"),
           ("t:stretching", "Alongamento extremo", ["chute alto, abertura, carrinho, dança", "dor mais alta, perto do quadril", "pouca perda de função no primeiro dia", "recuperação mais longa"], FOSF, "m1")]
    for k, (ic, t, itens, cor, mk) in enumerate(cen):
        x = k * 842
        p.append(caixa(x, 0, 822, 420, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 20, 60, cor))
        rs.append(rot(x + 100, 34, t, w=700, tam=28, cor=cor, peso=700, serif=True))
        cx = x + 411
        p.append(f'<ellipse cx="{cx}" cy="130" rx="150" ry="26" fill="{FOSF_T if k else OXID_T}" stroke="{cor}" stroke-width="3"/>')
        p.append(seta(cx - 160, 130, cx - 280, 130, cor, mk, esp=4))
        p.append(seta(cx + 160, 130, cx + 280, 130, cor, mk, esp=4))
        rs.append(rot(cx - 150, 118, "alonga sob tensão", w=300, tam=18, cor=cor, peso=700, alinha="center"))
        for j, it in enumerate(itens):
            y = 190 + j * 56
            p.append(f'<circle cx="{x + 36}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(x + 56, y, it, w=740, tam=23, cor=TINTA))
    return slide("mecanismos", 420, p, rs, eyebrow="Passo um · o que falha", titulo="Dois cenários de alongamento sob tensão",
                 destaque="A segunda engana: o susto é pequeno e o prazo é grande.", destaque_cor="verm", fonte="Dois estudos suecos, Am J Sports Med 2007")


def historia_74():
    """7.4: quatro perguntas em fila; a última, a que mais se esquece, em destaque."""
    p = [svg_abre(1664, 340, "Quatro perguntas da história, em fila. O que fazia: sprint, chute, abertura, desaceleração. O que sentiu: estalo, pontada, ou algo que apertou aos poucos. Continuou: conseguiu seguir no treino, conseguiu andar. Já teve antes: no mesmo lugar, e quando; esta última está em destaque, porque é a que mais se esquece"), defs(MUDO)]
    rs = []
    qs = [("t:run", "O que fazia", "sprint, chute, abertura, desaceleração", OXID), ("t:bolt", "O que sentiu", "estalo, pontada, ou algo que apertou aos poucos", GLIC),
          ("t:walk", "Continuou?", "conseguiu seguir no treino, conseguiu andar", GLIC), ("t:refresh", "Já teve antes?", "no mesmo lugar, e quando", FOSF)]
    for k, (ic, t, d, cor) in enumerate(qs):
        x = k * 424
        ult = k == 3
        p.append(caixa(x, 0, 392, 340, cor, FOSF_T if ult else CARTAO, esp=4 if ult else 2, rx=16))
        p.append(f'<circle cx="{x + 44}" cy="44" r="24" fill="{cor}"/>')
        p.append(icone(ic, x + 320, 22, 48, cor))
        rs += [rot(x + 20, 30, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 24, 100, t, w=350, tam=28, cor=cor, peso=700, serif=True), rot(x + 24, 160, d, w=350, tam=23, cor=TINTA, lh=1.3)]
        if k < 3:
            p.append(seta(x + 394, 170, x + 420, 170, MUDO, "m0", esp=3))
    rs.append(rot(1296, 290, "a que mais se esquece", w=360, tam=20, cor=FOSF, peso=700))
    return slide("historia", 340, p, rs, eyebrow="Passo dois · as primeiras horas", titulo="A história vale mais do que parece",
                 destaque="A última pergunta é a que mais se esquece, e é a que mais muda o plano.", destaque_cor="tinta")


def exame_74():
    """7.4: o que a maca mostra, e os sinais de alarme que mudam a urgência."""
    p = [svg_abre(1664, 400, "À esquerda, o exame em quatro itens: onde dói e em que extensão; amplitude perdida, lado a lado; dor ao contrair, com e sem resistência; falha palpável. À direita, em vermelho, os sinais que mudam a urgência: não consegue andar; hematoma extenso em poucas horas; dor muito alta, perto do osso da bacia; no adolescente, pensar em arrancamento")]
    rs = []
    itens = [("t:target", "onde dói e em que extensão"), ("t:ruler-measure", "amplitude perdida, lado a lado"), ("t:barbell", "dor ao contrair, com e sem resistência"), ("t:hand-stop", "falha palpável")]
    p.append(caixa(0, 0, 800, 400, OXID, CARTAO, esp=2, rx=16))
    p.append(icone("t:stethoscope", 24, 20, 48, OXID))
    rs.append(rot(88, 28, "O exame", w=600, tam=28, cor=OXID, peso=700, serif=True))
    for k, (ic, t) in enumerate(itens):
        y = 96 + k * 76
        p.append(f'<rect x="24" y="{y}" width="752" height="64" rx="12" fill="{OXID_T}"/>')
        p.append(icone(ic, 40, y + 14, 36, OXID))
        rs.append(rot(92, y + 18, t, w=670, tam=22, cor=TINTA))
    sinais = [("t:walk", "não consegue andar"), ("t:droplet", "hematoma extenso em poucas horas"), ("t:bolt", "dor muito alta, perto do osso da bacia"), ("h:boy-1015y", "no adolescente: pensar em arrancamento")]
    p.append(caixa(864, 0, 800, 400, FOSF, FOSF_T, esp=4, rx=16))
    p.append(icone("t:alert-triangle", 888, 20, 48, FOSF))
    rs.append(rot(952, 28, "Sinais que mudam a urgência", w=680, tam=28, cor=FOSF, peso=700, serif=True))
    for k, (ic, t) in enumerate(sinais):
        y = 96 + k * 76
        p.append(f'<rect x="888" y="{y}" width="752" height="64" rx="12" fill="{CARTAO}"/>')
        p.append(icone(ic, 904, y + 14, 36, FOSF))
        rs.append(rot(956, y + 18, t, w=670, tam=22, cor=TINTA, peso=700))
    return slide("exame", 400, p, rs, eyebrow="Passo dois · o exame", titulo="O que a maca mostra e o que muda a urgência",
                 destaque="Com história e exame, quem examina já separa o leve do sério e decide se precisa de imagem.", destaque_cor="tinta")


def imagem_74():
    """7.4: uma pergunta antes da ressonância; de um lado quando ajuda, do outro quando não ajuda."""
    p = [svg_abre(1664, 400, "No alto, a pergunta que vem antes da ressonância: o laudo muda a decisão? Se sim, ela ajuda: dúvida de gravidade ou de arrancamento; prazo apertado e tendão interno em jogo; evolução que não bate com o esperado. Se não, não ajuda: pedida por reflexo, no dia seguinte; desconforto leve, já melhorando; plano que não muda com o laudo"), defs(OXID, FOSF)]
    rs = []
    p.append(caixa(532, 0, 600, 90, TINTA, TINTA, esp=0, rx=45))
    p.append(icone("t:zoom-question", 560, 21, 48, PAPEL))
    rs.append(rot(620, 28, "o laudo muda a decisão?", w=490, tam=27, cor=PAPEL, peso=700, serif=True))
    p.append(seta(600, 92, 420, 140, OXID, "m0", esp=3))
    p.append(seta(1064, 92, 1244, 140, FOSF, "m1", esp=3))
    for k, (t, itens, cor, fundo, ic) in enumerate([("sim: ajuda", ["dúvida de gravidade ou de arrancamento", "prazo apertado e tendão interno em jogo", "evolução que não bate com o esperado"], OXID, OXID_T, "t:check"),
                                                    ("não: não ajuda", ["pedida por reflexo, no dia seguinte", "desconforto leve, já melhorando", "plano que não muda com o laudo"], FOSF, FOSF_T, "t:x")]):
        x = k * 864
        p.append(caixa(x, 150, 800, 250, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, 166, t, w=740, tam=26, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            y = 218 + j * 58
            p.append(icone(ic, x + 24, y, 34, cor))
            rs.append(rot(x + 72, y + 4, it, w=700, tam=22, cor=TINTA))
    return slide("imagem", 400, p, rs, eyebrow="Passo três · imagem com pergunta", titulo="Quando a ressonância muda a decisão",
                 destaque="Em 180 atletas, a ressonância não acrescentou valor à história e ao exame para prever o retorno.", destaque_cor="tinta",
                 fonte="Coorte norueguesa, Br J Sports Med 2015")


def advertencias_74():
    """7.4: uma linha do tempo com os dois erros de momento e, ao lado, o achado que sobra em quem já voltou."""
    p = [svg_abre(1664, 360, "Uma linha do tempo desde a lesão, em esquema. No começo, cedo demais: a imagem pode subestimar a lesão. No fim, tarde demais: pode mostrar cicatriz antiga e confundir. O momento importa. Ao lado, o terceiro alerta: o achado sem sintoma, o edema que persiste em quem já voltou a treinar bem"), defs(MUDO)]
    rs = []
    p.append(seta(0, 250, 1000, 250, MUDO, "m0", esp=3))
    rs.append(rot(0, 266, "tempo desde a lesão · esquema", w=990, tam=18, cor=MUDO, alinha="right"))
    for x, w, t, d in [(0, 360, "Cedo demais", "pode subestimar a lesão"), (620, 360, "Tarde demais", "pode mostrar cicatriz antiga e confundir")]:
        p.append(caixa(x, 0, w, 220, GLIC, GLIC_T, esp=2, rx=16))
        p.append(icone("t:clock", x + 24, 22, 44, GLIC))
        rs += [rot(x + 82, 28, t, w=w - 100, tam=26, cor=GLIC, peso=700, serif=True), rot(x + 24, 96, d, w=w - 48, tam=23, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + w / 2}" y1="220" x2="{x + w / 2}" y2="244" stroke="{GLIC}" stroke-width="3"/>')
    rs.append(rot(370, 96, "o momento importa", w=240, tam=20, cor=MUDO, peso=700, alinha="center", lh=1.2))
    p.append(caixa(1064, 0, 600, 360, FOSF, FOSF_T, esp=4, rx=16))
    p.append(icone("t:run", 1088, 22, 48, OXID))
    p.append(icone("t:eye", 1150, 22, 48, FOSF))
    rs += [rot(1088, 96, "Achado sem sintoma", w=550, tam=27, cor=FOSF, peso=700, serif=True),
           rot(1088, 150, "o edema persiste em quem já voltou a treinar bem", w=550, tam=23, cor=TINTA, lh=1.3)]
    return slide("advertencias", 360, p, rs, eyebrow="Imagem de músculo", titulo="Três advertências que evitam erro caro",
                 destaque="A imagem, sozinha, não decide quando a pessoa volta.", destaque_cor="verm")


def munique_74():
    """7.4: dois mundos separados pela ruptura de fibra, cada um com dois tipos."""
    p = [svg_abre(1664, 420, "Dois mundos, separados pela ruptura de fibra. Funcional, sem ruptura: a sobrecarga por fadiga e a dor muscular tardia, que costumam resolver rápido; e o neuromuscular, que inclui a dor que vem da coluna lombar e é tratado como ruptura por engano. Estrutural, com ruptura: a parcial, ruptura de fibra pequena a moderada, com prazo pelo exame; e a completa, ruptura total e arrancamento do tendão, que pede avaliação cirúrgica")]
    rs = []
    mundos = [("Funcional", "sem ruptura de fibra", OXID, OXID_T, [("sem ruptura", "sobrecarga por fadiga, dor muscular tardia", "costuma resolver rápido"),
                                                                  ("neuromuscular", "inclui a dor que vem da coluna lombar", "tratada como ruptura por engano")]),
              ("Estrutural", "com ruptura de fibra", FOSF, FOSF_T, [("parcial", "ruptura de fibra, pequena a moderada", "prazo pelo exame"),
                                                                   ("completa", "ruptura total e arrancamento do tendão", "avaliação cirúrgica")])]
    for k, (t, d, cor, fundo, tipos) in enumerate(mundos):
        x = k * 852
        p.append(caixa(x, 0, 812, 420, cor, CARTAO, esp=2, rx=16))
        p.append(f'<rect x="{x}" y="0" width="812" height="80" rx="16" fill="{fundo}"/>')
        rs += [rot(x + 24, 20, t, w=300, tam=30, cor=cor, peso=700, serif=True), rot(x + 260, 28, d, w=520, tam=22, cor=TINTA, peso=700)]
        for j, (n, e, c) in enumerate(tipos):
            y = 100 + j * 160
            p.append(f'<rect x="{x + 24}" y="{y}" width="764" height="144" rx="12" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
            rs += [rot(x + 44, y + 16, n, w=400, tam=24, cor=cor, peso=700), rot(x + 44, y + 54, e, w=720, tam=22, cor=TINTA),
                   rot(x + 44, y + 98, "→ " + c, w=720, tam=21, cor=cor if (k, j) != (0, 0) else TINTA, peso=700)]
    p.append(f'<line x1="832" y1="0" x2="832" y2="420" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    return slide("munique", 420, p, rs, eyebrow="Passo quatro · classificar", titulo="Consenso de Munique, 2013", fonte="Br J Sports Med 2013")


def britanica_74():
    """7.4: o grau pelo tamanho numa escada de 0 a 4 e a letra pelo lugar num corte do músculo com o tendão por dentro."""
    p = [svg_abre(1664, 400, "À esquerda, o grau pelo tamanho, numa escada de zero a quatro. À direita, um músculo desenhado com o tendão correndo por dentro, como espinha de peixe, e as três letras pelo lugar. Letra a: periferia, perto da fáscia. Letra b: no músculo ou na junção com o tendão. Letra c: estende-se para dentro do tendão, em destaque")]
    rs = [rot(0, 0, "o grau: tamanho", w=480, tam=24, cor=TINTA, peso=700, serif=True)]
    for g in range(5):
        h = 50 + g * 55
        x = g * 92
        p.append(f'<rect x="{x}" y="{340 - h}" width="76" height="{h}" rx="6" fill="{TINTA}" opacity="{0.35 + g * 0.16:.2f}"/>')
        rs.append(rot(x, 352, str(g), w=76, tam=24, cor=TINTA, peso=700, alinha="center"))
    X = 560
    rs.append(rot(X, 0, "a letra: lugar", w=500, tam=24, cor=TINTA, peso=700, serif=True))
    p.append(f'<ellipse cx="{X + 300}" cy="200" rx="290" ry="110" fill="{GLIC_T}" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<line x1="{X + 40}" y1="200" x2="{X + 560}" y2="200" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
    for i in range(9):
        xx = X + 90 + i * 50
        p.append(f'<line x1="{xx}" y1="200" x2="{xx - 40}" y2="130" stroke="{GLIC}" stroke-width="2"/>')
        p.append(f'<line x1="{xx}" y1="200" x2="{xx - 40}" y2="270" stroke="{GLIC}" stroke-width="2"/>')
    for t, cx, cy, cor in [("a", X + 300, 92, OXID), ("b", X + 180, 152, GLIC), ("c", X + 420, 200, FOSF)]:
        p.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="{cor}" stroke="{PAPEL}" stroke-width="3"/>')
        rs.append(rot(cx - 24, cy - 15, t, w=48, tam=24, cor=PAPEL, peso=700, alinha="center"))
    letras = [("a", "periferia, perto da fáscia", OXID), ("b", "no músculo ou na junção com o tendão", GLIC), ("c", "estende-se para dentro do tendão", FOSF)]
    for k, (t, d, cor) in enumerate(letras):
        y = 30 + k * 124
        p.append(caixa(1220, y, 444, 110, cor, FOSF_T if t == "c" else CARTAO, esp=4 if t == "c" else 2, rx=14))
        rs += [rot(1240, y + 14, f"Letra {t}", w=400, tam=24, cor=cor, peso=700, serif=True), rot(1240, y + 54, d, w=410, tam=20, cor=TINTA, lh=1.25)]
    return slide("britanica", 400, p, rs, eyebrow="Classificação britânica, 2014", titulo="Grau de 0 a 4 pelo tamanho, letra pelo lugar",
                 destaque="No atletismo de elite, a letra c demorou mais para voltar ao treino completo e repetiu mais.", destaque_cor="verm",
                 fonte="Br J Sports Med 2014 e 2016")


def conduta_74():
    """7.4: três faixas do primeiro dia à volta; no meio, a lesão periférica avança rápido e a do tendão devagar."""
    p = [svg_abre(1664, 380, "Três etapas do primeiro dia à volta ao esporte. Proteger sem imobilizar: repouso relativo, dor controlada, movimento no que não dói. Carga cedo, progressão por critério: a lesão periférica avança rápido, a do tendão interno devagar. O gesto volta antes da alta: sprint na reabilitação, não no jogo"), defs(MUDO, OXID, FOSF)]
    rs = []
    et = [("Proteger sem imobilizar", "repouso relativo, dor controlada, movimento no que não dói", OXID, OXID_T, 0, 460),
          ("Carga cedo, progressão por critério", "", GLIC, GLIC_T, 500, 660),
          ("O gesto volta antes da alta", "sprint na reabilitação, não no jogo", FOSF, FOSF_T, 1200, 464)]
    for k, (t, d, cor, fundo, x, w) in enumerate(et):
        p.append(caixa(x, 0, w, 300, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, 20, t, w=w - 48, tam=26, cor=cor, peso=700, serif=True, lh=1.2))
        if d:
            rs.append(rot(x + 24, 130, d, w=w - 48, tam=23, cor=TINTA, lh=1.3))
        if k < 2:
            p.append(seta(x + w + 4, 150, x + w + 34, 150, MUDO, "m0", esp=3))
    p.append(seta(524, 150, 1120, 150, OXID, "m1", esp=6))
    p.append(seta(524, 240, 800, 240, FOSF, "m2", esp=6))
    rs += [rot(524, 106, "periférica: avança rápido", w=600, tam=21, cor=OXID, peso=700),
           rot(524, 196, "tendão interno: devagar", w=600, tam=21, cor=FOSF, peso=700)]
    p.append(seta(0, 350, 1650, 350, MUDO, "m0", esp=2))
    rs += [rot(0, 316, "primeiro dia", w=300, tam=18, cor=MUDO), rot(1364, 316, "volta ao esporte", w=286, tam=18, cor=MUDO, alinha="right")]
    return slide("conduta", 380, p, rs, eyebrow="O que a classificação muda", titulo="Ritmo por critério, não por calendário",
                 destaque="Quando o calendário pula a última etapa, o jogo faz a exposição, em velocidade máxima e com adversário.", destaque_cor="verm")

# ---------------------------------------------------------------- 7.5

def celular_75():
    """7.5: o celular com quatro mensagens perguntando o prazo, e o destino do número que você der."""
    p = [svg_abre(1664, 400, "Um celular com quatro mensagens chegando dez minutos depois da lesão. O diretor: quanto tempo ele fica fora? O empresário: pega a convocação? A imprensa: pega o clássico? O atleta: perco o campeonato? Ao lado, o destino do número que você der: repetido, publicado e cobrado"), defs(MUDO)]
    rs = []
    p.append(f'<rect x="0" y="0" width="700" height="400" rx="40" fill="{TINTA}"/>')
    p.append(f'<rect x="20" y="40" width="660" height="340" rx="20" fill="{CARTAO}"/>')
    p.append(f'<rect x="290" y="16" width="120" height="10" rx="5" fill="{MUDO}"/>')
    msgs = [("t:briefcase", "diretor", "Quanto tempo ele fica fora?"), ("t:id", "empresário", "Pega a convocação?"),
            ("t:speakerphone", "imprensa", "Pega o clássico?"), ("h:running", "atleta", "Perco o campeonato?")]
    for k, (ic, q, t) in enumerate(msgs):
        y = 56 + k * 80
        p.append(f'<rect x="40" y="{y}" width="620" height="66" rx="22" fill="{AZUL_T if k < 3 else GLIC_T}"/>')
        p.append(icone(ic, 56, y + 15, 36, AZUL if k < 3 else GLIC))
        rs += [rot(104, y + 8, q, w=200, tam=17, cor=MUDO, peso=700), rot(104, y + 32, t, w=540, tam=22, cor=TINTA, peso=700)]
    p.append(seta(720, 200, 830, 200, MUDO, "m0", esp=4))
    p.append(caixa(850, 120, 300, 160, TINTA, TINTA, esp=0, rx=16))
    rs.append(rot(860, 160, "o número que você der", w=280, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.2))
    for k, t in enumerate(["repetido", "publicado", "cobrado"]):
        y = 50 + k * 110
        p.append(seta(1154, 200, 1240, y + 40, MUDO, "m0", esp=3))
        p.append(caixa(1250, y, 414, 80, FOSF, FOSF_T, esp=2, rx=40))
        rs.append(rot(1250, y + 22, t, w=414, tam=26, cor=FOSF, peso=700, alinha="center"))
    return slide("celular", 400, p, rs, eyebrow="Dez minutos depois da lesão", titulo="“Quanto tempo ele fica fora?”")


def medianas_75():
    """7.5: barras de mediana de afastamento por categoria da classificação de Munique."""
    p = [svg_abre(1664, 400, "Barras horizontais com a mediana de dias de afastamento, futebol de elite, lesões da coxa. Desordem funcional, sem ruptura: de 5 a 8 dias. Ruptura parcial pequena: 13 dias. Ruptura parcial moderada: 32 dias. Subtotal, completa ou arrancamento: 60 dias")]
    rs = []
    X0, E = 470, 17
    itens = [("desordem funcional, sem ruptura", 5, 8, "5 a 8 d", OXID), ("ruptura parcial pequena", 0, 13, "13 d", GLIC),
             ("ruptura parcial moderada", 0, 32, "32 d", GLIC), ("subtotal, completa ou arrancamento", 0, 60, "60 d", FOSF)]
    for k, (t, a, b, n, cor) in enumerate(itens):
        y = k * 86
        rs.append(rot(0, y + 22, t, w=440, tam=22, cor=TINTA, peso=700, alinha="right"))
        if a:
            p.append(f'<rect x="{X0}" y="{y + 10}" width="{b * E}" height="60" rx="6" fill="{cor}" opacity="0.35"/>')
            p.append(f'<rect x="{X0 + a * E}" y="{y + 10}" width="{(b - a) * E}" height="60" rx="6" fill="{cor}"/>')
        else:
            p.append(f'<rect x="{X0}" y="{y + 10}" width="{b * E}" height="60" rx="6" fill="{cor}"/>')
        rs.append(rot(X0 + b * E + 16, y + 14, n, w=200, tam=36, cor=cor, peso=700, serif=True))
    p.append(f'<line x1="{X0}" y1="350" x2="{X0 + 60 * E}" y2="350" stroke="{MUDO}" stroke-width="2"/>')
    for t in range(0, 61, 10):
        p.append(f'<line x1="{X0 + t * E}" y1="350" x2="{X0 + t * E}" y2="360" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(X0 + t * E - 30, 366, str(t), w=60, tam=17, cor=MUDO, alinha="center"))
    rs.append(rot(0, 366, "mediana, dias de afastamento", w=440, tam=17, cor=MUDO, alinha="right"))
    return slide("medianas", 400, p, rs, eyebrow="Validação de Munique, futebol de elite", titulo="Medianas de afastamento na lesão da coxa",
                 destaque="Quanto mais estrutura rompida, mais tempo. Tendão interno envolvido também alonga o retorno.", destaque_cor="tinta",
                 fonte="Br J Sports Med 2013 · letra c: Br J Sports Med 2016")


def variacao_75():
    """7.5: uma régua de dias com a média de 73 e a faixa de um desvio padrão, de 13 a 133 dias."""
    p = [svg_abre(1664, 340, "Uma régua de dias. A média de afastamento da lesão de grau 3 do posterior de coxa, 73 dias, marcada no meio. Em volta, a faixa de um desvio padrão, mais ou menos 60 dias, que vai de 13 a 133 dias: de poucas semanas a meses, dentro da mesma nota no laudo")]
    rs = []
    X0, E = 80, 10.4
    p.append(f'<rect x="{X0 + 13 * E:.0f}" y="80" width="{120 * E:.0f}" height="90" rx="12" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<line x1="{X0 + 73 * E:.0f}" y1="50" x2="{X0 + 73 * E:.0f}" y2="200" stroke="{TINTA}" stroke-width="6"/>')
    rs += [rot(X0 + 73 * E - 200, 0, "73 dias: média", w=400, tam=34, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(X0 + 13 * E + 16, 108, "poucas semanas", w=300, tam=21, cor=FOSF, peso=700),
           rot(X0 + 133 * E - 316, 108, "meses", w=300, tam=21, cor=FOSF, peso=700, alinha="right")]
    p.append(f'<line x1="{X0}" y1="240" x2="{X0 + 140 * E:.0f}" y2="240" stroke="{MUDO}" stroke-width="2"/>')
    for t in range(0, 141, 20):
        p.append(f'<line x1="{X0 + t * E:.0f}" y1="240" x2="{X0 + t * E:.0f}" y2="252" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(X0 + t * E - 30, 258, str(t), w=60, tam=18, cor=MUDO, alinha="center"))
    rs += [rot(X0, 292, "dias de afastamento", w=600, tam=18, cor=MUDO),
           rot(X0 + 13 * E, 292, "± 60 dias: desvio padrão, quase do tamanho da média", w=120 * E, tam=21, cor=FOSF, peso=700, alinha="center")]
    return slide("variacao", 340, p, rs, eyebrow="Por que se trabalha com faixa", titulo="Grau 3 na ressonância, posterior de coxa",
                 destaque="Mesma nota no laudo, pessoas e reabilitações diferentes: desfechos diferentes.", destaque_cor="verm",
                 fonte="Equipes profissionais europeias, Br J Sports Med 2012")


def advertencias_75():
    """7.5: três cartões, cada um com um pequeno desenho: o profissional e o amador, a faixa larga, duas semanas boas contra seis ruins."""
    p = [svg_abre(1664, 400, "Três advertências. Os números vêm do profissional, com fisioterapia todo dia; para o amador sem estrutura, some tempo. A variação é grande: dentro de cada faixa, desfechos muito diferentes. A reabilitação decide: duas semanas boas, desenhadas como dois blocos cheios, valem mais que seis semanas ruins, desenhadas como seis blocos vazios")]
    rs = []
    cards = [("Vêm do profissional", "fisioterapia todo dia; no amador sem estrutura, some tempo", GLIC),
             ("Variação grande", "dentro de cada faixa, desfechos muito diferentes", GLIC),
             ("A reabilitação decide", "duas semanas boas valem mais que seis ruins", FOSF)]
    for k, (t, d, cor) in enumerate(cards):
        x = k * 564
        p.append(caixa(x, 0, 536, 400, cor, CARTAO, esp=2 if k < 2 else 4, rx=16))
        rs += [rot(x + 24, 22, t, w=490, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 290, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    p.append(icone("t:building-hospital", 40, 100, 80, OXID))
    p.append(icone("h:person", 300, 100, 80, MUDO))
    rs += [rot(20, 196, "profissional", w=160, tam=19, cor=OXID, peso=700, alinha="center"), rot(260, 196, "amador sozinho", w=200, tam=19, cor=MUDO, peso=700, alinha="center"),
           rot(400, 120, "+", w=100, tam=48, cor=GLIC, peso=700, alinha="center")]
    x = 564
    p.append(f'<rect x="{x + 40}" y="140" width="456" height="50" rx="25" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
    for px in (70, 130, 220, 300, 390, 450):
        p.append(f'<circle cx="{x + px}" cy="165" r="10" fill="{GLIC}"/>')
    rs.append(rot(x + 40, 206, "mesma categoria, retornos espalhados", w=456, tam=18, cor=MUDO, alinha="center"))
    x = 1128
    for i in range(2):
        p.append(f'<rect x="{x + 40 + i * 64}" y="110" width="54" height="54" rx="6" fill="{OXID}"/>')
    for i in range(6):
        p.append(f'<rect x="{x + 40 + i * 64}" y="190" width="54" height="54" rx="6" fill="{CARTAO}" stroke="{CINZA}" stroke-width="3"/>')
    rs += [rot(x + 180, 122, "boas", w=200, tam=20, cor=OXID, peso=700), rot(x + 40, 252, "ruins", w=200, tam=18, cor=MUDO, peso=700)]
    return slide("advertencias", 400, p, rs, eyebrow="Valem mais que os números", titulo="Três advertências")


def laudo_75():
    """7.5: dois laudos, cada um levando a um erro: parado demais ou de volta cedo demais."""
    p = [svg_abre(1664, 400, "Dois laudos e os dois lados do erro. O laudo que assustou, grau 2 com edema extenso: a pessoa fica parada além do necessário e perde capacidade à toa. O laudo que tranquilizou, lesão pequena: volta com o exame ainda ruim, e vem a recidiva"), defs(GLIC, FOSF)]
    rs = []
    for k, (t, q, a, b, cor, fundo, mk) in enumerate([("O laudo assustou", "“grau 2 com edema extenso”", "fica parado além do necessário", "perde capacidade à toa", GLIC, GLIC_T, "m0"),
                                                       ("O laudo tranquilizou", "“lesão pequena”", "volta com o exame ainda ruim", "recidiva", FOSF, FOSF_T, "m1")]):
        x = k * 852
        rs.append(rot(x, 0, t, w=800, tam=28, cor=cor, peso=700, serif=True))
        p.append(f'<path d="M {x} 56 H {x + 760} L {x + 812} 100 V 170 H {x} Z" fill="{CARTAO}" stroke="{cor}" stroke-width="2"/>')
        p.append(icone("t:clipboard-list", x + 20, 86, 48, cor))
        rs.append(rot(x + 84, 96, q, w=700, tam=25, cor=TINTA, peso=700))
        p.append(seta(x + 200, 174, x + 200, 220, cor, mk, esp=3))
        p.append(caixa(x, 226, 380, 120, cor, fundo, esp=2, rx=14))
        rs.append(rot(x + 20, 258, a, w=340, tam=23, cor=TINTA, peso=700, lh=1.25))
        p.append(seta(x + 384, 286, x + 424, 286, cor, mk, esp=3))
        p.append(caixa(x + 432, 226, 380, 120, cor, cor, esp=0, rx=14))
        rs.append(rot(x + 452, 258, b, w=340, tam=24, cor=PAPEL, peso=700, lh=1.25))
    p.append(f'<line x1="832" y1="0" x2="832" y2="360" stroke="{BORDA}" stroke-width="2"{TRACO}/>')
    return slide("laudo", 400, p, rs, eyebrow="Quando o laudo vira calendário", titulo="O erro vai para os dois lados",
                 destaque="Critério é o que a pessoa consegue fazer, com qualidade, sem dor e sem apreensão. O laudo entra na conversa, não a resolve.",
                 destaque_cor="tinta", fonte="Ressonância sem valor adicional para prever retorno, Br J Sports Med 2015")


def movem_75():
    """7.5: o prazo no centro, empurrado para um lado pelo que alonga e para o outro pelo que encurta."""
    p = [svg_abre(1664, 420, "O prazo no centro, com duas setas. Para a direita, o que alonga: tendão interno envolvido; lesão prévia no mesmo músculo; lesão alta, por alongamento extremo; calendário apertado, sem estrutura. Para a esquerda, o que encurta: carga cedo, dentro do tolerado; progressão por critério, registrada; reexposição planejada ao gesto; atleta que não precisa esconder dor"), defs(OXID, FOSF)]
    rs = []
    p.append(caixa(632, 0, 400, 70, TINTA, TINTA, esp=0, rx=35))
    rs.append(rot(632, 18, "o prazo", w=400, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    p.append(seta(626, 35, 420, 35, OXID, "m0", esp=5))
    p.append(seta(1038, 35, 1244, 35, FOSF, "m1", esp=5))
    cols = [("Encurta", ["carga cedo, dentro do tolerado", "progressão por critério, registrada", "reexposição planejada ao gesto", "atleta que não precisa esconder dor"], OXID, OXID_T, 0),
            ("Alonga", ["tendão interno envolvido", "lesão prévia no mesmo músculo", "lesão alta, por alongamento extremo", "calendário apertado, sem estrutura"], FOSF, FOSF_T, 864)]
    for t, itens, cor, fundo, x in cols:
        rs.append(rot(x if x == 0 else x + 400, 14, t, w=400, tam=28, cor=cor, peso=700, serif=True, alinha="left" if x == 0 else "right"))
        for j, it in enumerate(itens):
            y = 100 + j * 80
            p.append(caixa(x, y, 800, 68, cor, fundo, esp=2, rx=12))
            rs.append(rot(x + 24, y + 20, it, w=750, tam=23, cor=TINTA, peso=700 if j == 3 else 400))
    return slide("movem", 420, p, rs, eyebrow="O que move o prazo", titulo="Para cima e para baixo",
                 destaque="Quem tem medo de perder a vaga esconde dor, e dor escondida vira recidiva.", destaque_cor="verm")


def andar_75():
    """7.5: dois grupos pelo tempo até andar sem dor; quem levou mais de um dia teve cerca de quatro vezes a chance de ficar mais de três semanas fora."""
    p = [svg_abre(1664, 340, "Dois grupos pela resposta a uma pergunta: quanto tempo levou para andar sem dor? Até um dia: a chance de ficar mais de três semanas fora serve de referência, uma barra curta. Mais de um dia: chance cerca de quatro vezes maior, uma barra quatro vezes mais longa")]
    rs = []
    X0, E = 560, 250
    for k, (t, v, n, cor) in enumerate([("andou sem dor em até 1 dia", 1, "referência", OXID), ("levou mais de 1 dia", 4, "≈ × 4", FOSF)]):
        y = 20 + k * 130
        p.append(icone("t:walk", 0, y + 14, 60, cor))
        rs.append(rot(80, y + 28, t, w=460, tam=24, cor=TINTA, peso=700))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E}" height="90" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + v * E + 20 if v == 1 else X0 + 20, y + (28 if v == 1 else 18), n, w=300, tam=26 if v == 1 else 44, cor=cor if v == 1 else PAPEL, peso=700, serif=v != 1))
    rs.append(rot(X0, 290, "chance de ficar mais de três semanas fora de competição", w=1000, tam=21, cor=MUDO, peso=700))
    return slide("andar", 340, p, rs, eyebrow="Uma pergunta barata", titulo="Quanto tempo levou para andar sem dor?",
                 destaque="A história, bem perguntada, carrega boa parte do prognóstico.", destaque_cor="tinta", fonte="Futebol australiano de elite, Br J Sports Med 2010")


def naodizer_75():
    """7.5: um balão com uma data riscada, e o que ela vira depois de dita."""
    p = [svg_abre(1664, 360, "Um balão de fala com uma data no calendário, riscada: uma data seca, no primeiro dia. Ela vira manchete, expectativa e cobrança. E, a partir dela, todo mundo trabalha para cumprir a data, não os critérios"), defs(MUDO)]
    rs = []
    p.append(f'<path d="M 20 20 H 520 Q 540 20 540 40 V 220 Q 540 240 520 240 H 160 L 90 300 L 110 240 H 40 Q 20 240 20 220 V 40 Q 20 20 40 20 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    p.append(icone("t:calendar", 200, 50, 140, TINTA))
    p.append(f'<line x1="140" y1="40" x2="420" y2="220" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
    for k, t in enumerate(["manchete", "expectativa", "cobrança"]):
        x = 640 + k * 290
        p.append(caixa(x, 40, 260, 76, GLIC, GLIC_T, esp=2, rx=38))
        rs.append(rot(x, 60, t, w=260, tam=24, cor=GLIC, peso=700, alinha="center"))
        p.append(seta(x + 130, 120, 1150, 196, MUDO, "m0", esp=2))
    p.append(caixa(640, 210, 1024, 130, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(664, 228, "todo mundo trabalha para cumprir a data,", w=980, tam=26, cor=TINTA, peso=700, serif=True),
           rot(664, 278, "não os critérios", w=980, tam=26, cor=FOSF, peso=700, serif=True)]
    return slide("naodizer", 360, p, rs, eyebrow="O que não dizer", titulo="Uma data seca, no primeiro dia.")


def dizer_75():
    """7.5: três partes da resposta, cada uma com um pequeno desenho: a faixa, os critérios, a data de reavaliação."""
    p = [svg_abre(1664, 380, "Três partes da resposta, numeradas. A faixa: lesões deste tipo costumam levar de tanto a tanto, desenhada como uma faixa larga. Os critérios: resposta à carga, força em amplitude, tolerância à velocidade. Quando volta a falar: reavalio na sexta e atualizo a previsão"), defs(MUDO)]
    rs = []
    partes = [("A faixa", "“lesões deste tipo costumam levar de tanto a tanto”", OXID, OXID_T), ("Os critérios", "", GLIC, GLIC_T), ("Quando volta a falar", "“reavalio na sexta e atualizo a previsão”", TINTA, AZUL_T)]
    for k, (t, d, cor, fundo) in enumerate(partes):
        x = k * 564
        p.append(caixa(x, 0, 536, 380, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 46}" cy="46" r="24" fill="{cor}"/>')
        rs += [rot(x + 22, 32, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(x + 86, 30, t, w=430, tam=27, cor=cor, peso=700, serif=True)]
        if d:
            rs.append(rot(x + 24, 260, d, w=490, tam=22, cor=TINTA, lh=1.3))
        if k < 2:
            p.append(seta(x + 538, 190, x + 560, 190, MUDO, "m0", esp=3))
    p.append(f'<rect x="40" y="130" width="456" height="70" rx="35" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    rs += [rot(56, 152, "de", w=80, tam=20, cor=OXID, peso=700), rot(400, 152, "a", w=80, tam=20, cor=OXID, peso=700, alinha="right")]
    for j, (ic, c) in enumerate([("t:barbell", "resposta à carga"), ("t:ruler-measure", "força em amplitude"), ("t:run", "tolerância à velocidade")]):
        y = 100 + j * 86
        p.append(f'<rect x="588" y="{y}" width="488" height="70" rx="35" fill="{GLIC_T}"/>')
        p.append(icone(c and ic, 606, y + 17, 36, GLIC))
        rs.append(rot(656, y + 22, c, w=400, tam=22, cor=TINTA, peso=700))
    p.append(icone("t:calendar", 1340, 110, 96, TINTA))
    return slide("dizer", 380, p, rs, eyebrow="O que dizer", titulo="Três partes, sempre",
                 destaque="“Não vou te liberar pelo calendário. Vou te liberar pelo que você conseguir fazer, e te mostrar o que falta.”", destaque_cor="tinta")

# ---------------------------------------------------------------- 7.6

def cena_76():
    """7.6: a sequência automática, da mão na coxa ao jogo, e as três coisas que mudaram."""
    p = [svg_abre(1664, 360, "A sequência que acontece no automático, em fila: a mão na coxa, gelo, anti-inflamatório, repouso, ressonância e a pergunta quanto tempo, até o jogo. Embaixo, as três coisas que mudaram e ainda não chegaram à beira do campo: o que fazer nas primeiras horas, o que não usar, e como se atravessa da reabilitação ao jogo"), defs(MUDO)]
    rs = []
    seq = [("h:running", "a mão na coxa", FOSF), ("t:droplet", "gelo", AZUL), ("t:pill", "anti-inflamatório", AZUL), ("t:bed", "repouso", AZUL), ("t:eye", "ressonância", AZUL), ("t:message-circle", "“quanto tempo?”", GLIC)]
    for k, (ic, t, cor) in enumerate(seq):
        x = k * 278
        p.append(caixa(x, 0, 250, 130, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 101, 16, 48, cor))
        rs.append(rot(x + 8, 76, t, w=234, tam=21, cor=TINTA, peso=700, alinha="center"))
        if k < 5:
            p.append(seta(x + 252, 65, x + 274, 65, MUDO, "m0", esp=3))
    rs.append(rot(278, 148, "no automático", w=1110, tam=19, cor=MUDO, alinha="center"))
    p.append(f'<path d="M 290 140 H 1390" fill="none" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    for k, t in enumerate(["o que fazer nas primeiras horas", "o que não usar", "a travessia da reabilitação ao jogo"]):
        x = k * 564
        p.append(caixa(x, 220, 536, 120, OXID, OXID_T, esp=2, rx=16))
        p.append(icone("t:refresh", x + 24, 256, 44, OXID))
        rs.append(rot(x + 84, 262, t, w=430, tam=23, cor=TINTA, peso=700, lh=1.2))
    rs.append(rot(0, 184, "o que mudou e ainda não chegou à beira do campo", w=1664, tam=20, cor=OXID, peso=700))
    return slide("cena", 360, p, rs, eyebrow="No terceiro passo", titulo="Não caiu, ninguém encostou. Só parou.")


def custo_76():
    """7.6: 34 jogadores em pontos, a perda estimada e os dois fatores associados."""
    p = [svg_abre(1664, 360, "Um clube de elite brasileiro, uma temporada. Trinta e quatro pontos, um por jogador acompanhado, só lesão de posterior de coxa. Ao lado, a perda potencial estimada, cerca de 43 milhões de dólares, quase toda pelo desempenho da equipe, não pelos salários. E os dois fatores associados: lesão prévia e déficit dos flexores do joelho")]
    rs = []
    p.append(caixa(0, 0, 520, 360, TINTA, CARTAO, esp=2, rx=16))
    for i in range(34):
        cx, cy = 50 + (i % 9) * 52, 50 + (i // 9) * 52
        p.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="{TINTA}"/>')
    rs += [rot(24, 236, "34", w=200, tam=54, cor=TINTA, peso=700, serif=True), rot(24, 306, "jogadores, só posterior de coxa", w=470, tam=21, cor=TINTA)]
    p.append(caixa(560, 0, 540, 360, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(584, 40, "US$ 43 mi", w=500, tam=64, cor=FOSF, peso=700, serif=True),
           rot(584, 140, "perda potencial estimada", w=500, tam=24, cor=TINTA, peso=700),
           rot(584, 190, "quase toda pelo desempenho da equipe, não pelos salários", w=490, tam=22, cor=TINTA, lh=1.3)]
    p.append(caixa(1140, 0, 524, 360, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(1164, 22, "2 fatores associados, os dois trabalháveis", w=480, tam=23, cor=OXID, peso=700, lh=1.2))
    for k, (ic, t) in enumerate([("t:refresh", "lesão prévia"), ("t:barbell", "déficit dos flexores do joelho")]):
        y = 120 + k * 110
        p.append(f'<rect x="1164" y="{y}" width="476" height="90" rx="45" fill="{OXID_T}"/>')
        p.append(icone(ic, 1186, y + 23, 44, OXID))
        rs.append(rot(1244, y + 18, t, w=380, tam=23, cor=TINTA, peso=700, lh=1.2))
    return slide("custo", 360, p, rs, eyebrow="Um clube de elite brasileiro, uma temporada", titulo="Por que uma aula inteira sobre isso",
                 destaque="Estudo piloto, um clube, conta estimada. Mas a ordem de grandeza diz alguma coisa.", destaque_cor="tinta", fonte="Front Sports Act Living 2024")


def graus_76():
    """7.6: três feixes de fibras: poucas rompidas, parte rompida, todas rompidas com afundamento."""
    p = [svg_abre(1664, 400, "Três graus da beira do campo, cada um com um feixe de fibras desenhado. Grau 1: poucas fibras rompidas; dor localizada, força e amplitude quase preservadas. Grau 2: parte das fibras rompida; não continua, força cai, roxo dias depois. Grau 3: todas rompidas, com afundamento; ruptura completa ou arrancamento, afundamento palpável")]
    rs = []
    graus = [("Grau 1", "poucas fibras, dor localizada, força e amplitude quase preservadas", OXID, {3}),
             ("Grau 2", "ruptura parcial, não continua, força cai, roxo dias depois", GLIC, {1, 2, 3, 4}),
             ("Grau 3", "ruptura completa ou arrancamento, afundamento palpável", FOSF, set(range(7)))]
    for k, (t, d, cor, rompe) in enumerate(graus):
        x = k * 564
        p.append(caixa(x, 0, 536, 400, cor, CARTAO, esp=2 if k < 2 else 4, rx=16))
        rs.append(rot(x + 24, 20, t, w=490, tam=30, cor=cor, peso=700, serif=True))
        for j in range(7):
            y = 90 + j * 22
            if j in rompe:
                gap = 40 if k == 2 else 26
                p.append(f'<line x1="{x + 40}" y1="{y}" x2="{x + 268 - gap}" y2="{y}" stroke="{cor}" stroke-width="8" stroke-linecap="round"/>')
                p.append(f'<line x1="{x + 268 + gap}" y1="{y}" x2="{x + 496}" y2="{y}" stroke="{cor}" stroke-width="8" stroke-linecap="round"/>')
            else:
                p.append(f'<line x1="{x + 40}" y1="{y}" x2="{x + 496}" y2="{y}" stroke="{CINZA}" stroke-width="8" stroke-linecap="round"/>')
        rs.append(rot(x + 24, 260, d, w=490, tam=23, cor=TINTA, lh=1.3))
    return slide("graus", 400, p, rs, eyebrow="Passo um · acertar o nome", titulo="Os três graus da beira do campo",
                 destaque="Estalo forte, dor para sentar e hematoma descendo pela coxa: arrancamento alto, avaliação ortopédica em dias.", destaque_cor="verm")


def imitacoes_76():
    """7.6: o estiramento tem hora marcada; quatro imitações em volta."""
    p = [svg_abre(1664, 400, "No alto, o estiramento: tem hora marcada, a pessoa diz o segundo em que doeu. Embaixo, quatro imitações para descartar antes de tratar. Dor tardia: horas depois, difusa, dos dois lados, sem momento exato. Contusão: pancada; não massagear forte nem aquecer no início. Câimbra: trava e solta, sem dor localizada depois. Dor da coluna: sem momento claro, piora sentado com perna e pescoço")]
    rs = []
    p.append(caixa(0, 0, 1664, 90, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:stopwatch", 24, 21, 48, PAPEL))
    rs.append(rot(92, 28, "Estiramento: hora marcada. A pessoa diz o segundo em que doeu.", w=1540, tam=26, cor=PAPEL, peso=700, serif=True))
    itens = [("t:clock", "Dor tardia", "horas depois, difusa, dos dois lados, sem momento exato", OXID),
             ("t:hand-stop", "Contusão", "pancada; não massagear forte nem aquecer no início", GLIC),
             ("t:bolt", "Câimbra", "trava e solta, sem dor localizada depois", OXID),
             ("h:pain-managment", "Dor da coluna", "sem momento claro, piora sentado com perna e pescoço", FOSF)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 120, 392, 280, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 142, 48, cor))
        rs += [rot(x + 86, 152, t, w=290, tam=26, cor=cor, peso=700, serif=True), rot(x + 24, 220, d, w=350, tam=22, cor=TINTA, lh=1.3)]
    return slide("imitacoes", 400, p, rs, eyebrow="O que parece estiramento e não é", titulo="Descarte antes de tratar")


def peace_76():
    """7.6: a palavra PEACE na vertical, letra por letra."""
    p = [svg_abre(1664, 420, "A sigla PEACE na vertical, letra por letra, para os primeiros dias. P, proteger: poupar de um a três dias; não é imobilizar. E, elevar: acima do coração quando der; custo zero. A, evitar anti-inflamatório: a inflamação é o começo do conserto. C, comprimir: faixa ou malha contra inchaço e hematoma. E, educar: a letra mais importante e a que menos se faz")]
    rs = []
    itens = [("P", "Proteger", "poupar de um a três dias; não é imobilizar", OXID), ("E", "Elevar", "acima do coração quando der; custo zero", OXID),
             ("A", "Evitar anti-inflamatório", "a inflamação é o começo do conserto", FOSF), ("C", "Comprimir", "faixa ou malha contra inchaço e hematoma", OXID),
             ("E", "Educar", "a letra mais importante e a que menos se faz", TINTA)]
    for k, (L, t, d, cor) in enumerate(itens):
        y = k * 84
        p.append(f'<rect x="0" y="{y}" width="76" height="76" rx="12" fill="{cor}"/>')
        rs.append(rot(0, y + 12, L, w=76, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True))
        ult = k == 4
        p.append(caixa(92, y, 1572, 76, cor, AZUL_T if ult else CARTAO, esp=3 if ult else 2, rx=12))
        rs += [rot(116, y + 22, t, w=420, tam=25, cor=cor, peso=700, serif=True), rot(560, y + 24, d, w=1080, tam=23, cor=TINTA, peso=700 if ult else 400)]
    return slide("peace", 420, p, rs, eyebrow="Os primeiros dias", titulo="PEACE", fonte="Br J Sports Med 2020")


def love_76():
    """7.6: a palavra LOVE na vertical e, ao lado, a escada de carga."""
    p = [svg_abre(1664, 400, "A sigla LOVE na vertical, para depois dos primeiros dias. L, carga: isométrico, depois movimento, depois carga crescente. O, otimismo: como a equipe fala da lesão faz parte do tratamento. V, vascularização: aeróbico sem dor, desde cedo, bicicleta, piscina. E, exercício: força, amplitude e controle até o gesto do esporte. Ao lado, uma escada de carga: isométrico, movimento, carga crescente, gesto do esporte")]
    rs = []
    itens = [("L", "Carga", "isométrico, depois movimento, depois carga crescente", OXID), ("O", "Otimismo", "como a equipe fala da lesão faz parte do tratamento", GLIC),
             ("V", "Vascularização", "aeróbico sem dor, desde cedo: bicicleta, piscina", OXID), ("E", "Exercício", "força, amplitude e controle até o gesto do esporte", TINTA)]
    for k, (L, t, d, cor) in enumerate(itens):
        y = k * 100
        p.append(f'<rect x="0" y="{y}" width="86" height="88" rx="12" fill="{cor}"/>')
        rs.append(rot(0, y + 16, L, w=86, tam=44, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(caixa(100, y, 960, 88, cor, CARTAO, esp=2, rx=12))
        rs += [rot(124, y + 12, t, w=400, tam=25, cor=cor, peso=700, serif=True), rot(124, y + 50, d, w=920, tam=21, cor=TINTA)]
    deg = ["isométrico", "movimento", "carga crescente", "gesto do esporte"]
    for k, t in enumerate(deg):
        x, h = 1120 + k * 136, 90 + k * 90
        p.append(f'<rect x="{x}" y="{400 - h}" width="128" height="{h}" rx="8" fill="{OXID}" opacity="{0.45 + k * 0.18:.2f}"/>')
        rs.append(rot(x + 4, 400 - h + 12, t, w=120, tam=18, cor=PAPEL, peso=700, alinha="center", lh=1.15))
    return slide("love", 400, p, rs, eyebrow="Depois dos primeiros dias", titulo="LOVE",
                 destaque="Poucos dias de proteção inteligente, depois carga progressiva. Nenhuma letra é repouso absoluto.", destaque_cor="tinta")


def aine_76():
    """7.6: a cadeia do reparo com o comprimido no meio dela, e o que fazer no lugar."""
    p = [svg_abre(1664, 400, "À esquerda, a cadeia do reparo: a inflamação inicial, as primeiras células limpam o tecido, as seguintes sinalizam a reconstrução, o reparo. O anti-inflamatório aparece cortando a cadeia. Embaixo, a mesma via participa da resposta ao treino; doses altas por semanas: menor ganho de massa em jovens. À direita, o que fazer: analgésico para a dor, por decisão médica; curso curto só em situação específica; nunca o comprimido do vestiário"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 1000, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "Por quê", w=400, tam=27, cor=FOSF, peso=700, serif=True))
    cad = ["inflamação inicial", "limpa o tecido", "sinaliza a reconstrução", "reparo"]
    for k, t in enumerate(cad):
        x = 24 + k * 240
        p.append(caixa(x, 80, 210, 90, OXID if k == 3 else GLIC, OXID_T if k == 3 else GLIC_T, esp=2, rx=14))
        rs.append(rot(x + 10, 102, t, w=190, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.2))
        if k < 3:
            p.append(seta(x + 212, 125, x + 236, 125, MUDO, "m0", esp=3))
    p.append(f'<line x1="250" y1="110" x2="250" y2="186" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<circle cx="250" cy="214" r="30" fill="{FOSF}"/>')
    p.append(icone("t:pill", 234, 198, 32, PAPEL))
    rs.append(rot(294, 200, "o anti-inflamatório corta a cadeia", w=560, tam=21, cor=FOSF, peso=700))
    rs += [rot(24, 270, "a mesma via participa da resposta ao treino", w=950, tam=22, cor=TINTA),
           rot(24, 320, "doses altas por semanas: menor ganho de massa em jovens", w=950, tam=22, cor=TINTA, peso=700)]
    p.append(caixa(1040, 0, 624, 400, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(1064, 18, "O que fazer", w=560, tam=27, cor=OXID, peso=700, serif=True))
    for k, (ic, t, cor) in enumerate([("t:check", "analgésico para a dor, por decisão médica", OXID), ("t:check", "curso curto só em situação específica", OXID), ("t:x", "nunca o comprimido do vestiário", FOSF)]):
        y = 90 + k * 100
        p.append(icone(ic, 1064, y + 4, 40, cor))
        rs.append(rot(1118, y, t, w=520, tam=23, cor=TINTA, peso=700 if k == 2 else 400, lh=1.25))
    return slide("aine", 400, p, rs, eyebrow="Passo três · anti-inflamatório", titulo="Não entra de forma automática", fonte="Revisão, Scand J Med Sci Sports 2018")


def gelo_76():
    """7.6: um cubo de gelo com três etiquetas: alivia, reparo contraditório, sem prova em gente."""
    p = [svg_abre(1664, 380, "Um cubo de gelo com três etiquetas. Alivia a dor, por pouco tempo, e isso é real. Reparo: contraditório; em ratos, menos inflamação sem mudar a regeneração, e outros estudos sugerem atraso. Em gente: sem prova clara de que acelere a volta")]
    rs = []
    p.append(f'<rect x="60" y="80" width="240" height="240" rx="36" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
    p.append(f'<path d="M 100 130 q 30 -20 70 0" fill="none" stroke="{CARTAO}" stroke-width="10" stroke-linecap="round"/>')
    rs.append(rot(60, 336, "o gelo", w=240, tam=22, cor=AZUL, peso=700, alinha="center"))
    tags = [("Alivia a dor", "por pouco tempo, e isso é real", OXID, OXID_T), ("Reparo: contraditório", "em ratos, menos inflamação sem mudar a regeneração; outros sugerem atraso", GLIC, GLIC_T),
            ("Em gente", "sem prova clara de que acelere a volta", FOSF, FOSF_T)]
    for k, (t, d, cor, fundo) in enumerate(tags):
        y = k * 128
        p.append(f'<line x1="304" y1="200" x2="420" y2="{y + 56}" stroke="{cor}" stroke-width="3"/>')
        p.append(f'<circle cx="304" cy="200" r="7" fill="{TINTA}"/>')
        p.append(caixa(420, y, 1244, 112, cor, fundo, esp=2, rx=14))
        rs += [rot(444, y + 16, t, w=1190, tam=25, cor=cor, peso=700, serif=True), rot(444, y + 60, d, w=1190, tam=22, cor=TINTA)]
    return slide("gelo", 380, p, rs, eyebrow="E o gelo", titulo="Conforto, não tratamento",
                 destaque="Se alivia, pode usar nos primeiros dias. Não é obrigatório e não é o centro da conversa.", destaque_cor="tinta",
                 fonte="Estudo brasileiro em ratos, Sci Rep 2016")


def curcuma_76():
    """7.6: o que a metanálise mostra, e uma faixa da dor tardia à ruptura com os estudos todos num lado só."""
    p = [svg_abre(1664, 400, "À esquerda, o que mostra: 14 ensaios e 349 pessoas; menos dor e marcadores de dano, mais amplitude depois do exercício. À direita, o que não mostra, numa faixa que vai da dor tardia à ruptura: todos os estudos estão do lado da dor tardia; do lado da ruptura, nenhum; sem prova de retorno mais rápido; anti-inflamatório brando, nunca testado aqui")]
    rs = []
    p.append(caixa(0, 0, 640, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "O que mostra", w=590, tam=27, cor=OXID, peso=700, serif=True))
    rs += [rot(24, 72, "14", w=200, tam=64, cor=OXID, peso=700, serif=True), rot(24, 160, "ensaios", w=200, tam=21, cor=TINTA),
           rot(260, 72, "349", w=300, tam=64, cor=OXID, peso=700, serif=True), rot(260, 160, "pessoas", w=300, tam=21, cor=TINTA),
           rot(24, 230, "menos dor e marcadores de dano", w=590, tam=23, cor=TINTA, peso=700),
           rot(24, 280, "mais amplitude depois do exercício", w=590, tam=23, cor=TINTA, peso=700)]
    X = 680
    p.append(caixa(X, 0, 984, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 18, "O que não mostra", w=900, tam=27, cor=FOSF, peso=700, serif=True))
    p.append(f'<rect x="{X + 40}" y="110" width="904" height="56" rx="28" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<rect x="{X + 40}" y="110" width="300" height="56" rx="28" fill="{OXID}"/>')
    rs += [rot(X + 40, 124, "dor tardia", w=300, tam=22, cor=PAPEL, peso=700, alinha="center"),
           rot(X + 644, 124, "ruptura", w=300, tam=22, cor=FOSF, peso=700, alinha="center"),
           rot(X + 40, 176, "os estudos estão aqui", w=300, tam=18, cor=OXID, peso=700, alinha="center"),
           rot(X + 644, 176, "nenhum estudo aqui", w=300, tam=18, cor=FOSF, peso=700, alinha="center")]
    for k, t in enumerate(["sem prova de retorno mais rápido", "anti-inflamatório brando, nunca testado aqui"]):
        y = 250 + k * 64
        p.append(icone("t:x", X + 40, y, 36, FOSF))
        rs.append(rot(X + 90, y + 4, t, w=850, tam=23, cor=TINTA))
    return slide("curcuma", 400, p, rs, eyebrow="Passo quatro · a cúrcuma", titulo="Resposta com as duas mãos",
                 destaque="Coadjuvante para o conforto, com procedência e conversa com o médico. Não substitui carga.", destaque_cor="tinta",
                 fonte="Metanálise, PLoS One 2024")


def reabilitacao_76():
    """7.6: duas barras de retorno, 28 contra 51 dias, e a escada do retorno em três degraus."""
    p = [svg_abre(1664, 380, "Duas barras de retorno médio, em 75 jogadores. Com o protocolo em alongamento: 28 dias. Com a reabilitação convencional: 51 dias. Embaixo, o retorno como caminho em três degraus: voltar a participar, voltar ao esporte, voltar a render")]
    rs = []
    X0, E = 380, 19
    for k, (v, t, cor) in enumerate([(28, "protocolo em alongamento", OXID), (51, "reabilitação convencional", FOSF)]):
        y = k * 96
        rs.append(rot(0, y + 26, t, w=350, tam=22, cor=TINTA, peso=700, alinha="right"))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E}" height="80" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + v * E + 18, y + 12, f"{v} dias", w=260, tam=42, cor=cor, peso=700, serif=True))
    rs.append(rot(X0, 184, "retorno médio", w=600, tam=18, cor=MUDO))
    for k, t in enumerate(["voltar a participar", "voltar ao esporte", "voltar a render"]):
        x, h = 380 + k * 420, 60 + k * 40
        p.append(f'<rect x="{x}" y="{380 - h}" width="400" height="{h}" rx="8" fill="{TINTA}" opacity="{0.55 + k * 0.2:.2f}"/>')
        rs.append(rot(x, 380 - h + h / 2 - 14, t, w=400, tam=22, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(0, 316, "o retorno é um caminho", w=350, tam=22, cor=TINTA, peso=700, alinha="right"))
    return slide("reabilitacao", 380, p, rs, eyebrow="Passo cinco · a travessia até o jogo", titulo="Exercício em alongamento, 75 jogadores",
                 destaque="Desconforto tolerável: mesmo prazo, mais força e fibras mais preservadas. Quem lesionou correndo corre rápido na reabilitação antes do jogo.",
                 destaque_cor="tinta", fonte="Br J Sports Med 2013 · J Orthop Sports Phys Ther 2020 · consenso de Berna 2016")

# ---------------------------------------------------------------- aplicação

LICOES = {"07-01": [numeros_71, usos_71, familias_71, consenso_71, denominador_71, novatos_71, vocabulario_71, oslo_71, leitura_71, rastreio_71],
          "07-02": [cena_72, perguntas_72, definicao_72, exposicao_72, ferramentas_72, indicadores_72, carga_72, devolutiva_72, lgpd_72, painel_72],
          "07-03": [cena_73, mecanismo_73, modelo_73, copo_73, padrao_73, razao_73, colunas_73],
          "07-04": [palavra_74, tamanho_74, mecanismos_74, historia_74, exame_74, imagem_74, advertencias_74, munique_74, britanica_74, conduta_74],
          "07-05": [celular_75, medianas_75, variacao_75, advertencias_75, laudo_75, movem_75, andar_75, naodizer_75, dizer_75],
          "07-06": [cena_76, custo_76, graus_76, imitacoes_76, peace_76, love_76, aine_76, gelo_76, curcuma_76, reabilitacao_76]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
