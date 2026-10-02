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

# ---------------------------------------------------------------- 7.7

def palavra_77():
    """7.7: o sufixo -ite levando aos três tratamentos automáticos e à dor que continua."""
    p = [svg_abre(1664, 340, "A palavra tendinite numa receita, com o sufixo ite marcado: quer dizer inflamação. Dele saem, no automático, três tratamentos: anti-inflamatório, gelo e repouso. Ao fim da fila, quem tem dor no Aquiles há oito meses: já fez os três, e continua com dor"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 40, 420, 260, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:clipboard-list", 24, 60, 44, TINTA))
    rs += [rot(24, 130, "tendin", w=220, tam=48, cor=TINTA, peso=700, serif=True, alinha="right"),
           rot(246, 130, "ite", w=150, tam=48, cor=FOSF, peso=700, serif=True),
           rot(24, 230, "“ite” = inflamação", w=372, tam=22, cor=FOSF, peso=700, alinha="center")]
    p.append(f'<line x1="250" y1="196" x2="330" y2="196" stroke="{FOSF}" stroke-width="4"/>')
    p.append(seta(424, 170, 480, 170, MUDO, "m0", esp=3))
    for k, (ic, t) in enumerate([("t:pill", "anti-inflamatório"), ("t:droplet", "gelo"), ("t:bed", "repouso")]):
        y = k * 116
        p.append(caixa(490, y, 460, 100, AZUL, AZUL_T, esp=2, rx=50))
        p.append(icone(ic, 520, y + 28, 44, AZUL))
        rs.append(rot(584, y + 34, t, w=340, tam=24, cor=TINTA, peso=700))
        p.append(seta(954, y + 50, 1050, 170, MUDO, "m0", esp=2))
    p.append(caixa(1060, 60, 604, 220, FOSF, FOSF_T, esp=4, rx=16))
    p.append(icone("t:calendar", 1084, 84, 48, FOSF))
    rs += [rot(1146, 92, "oito meses depois", w=500, tam=26, cor=FOSF, peso=700, serif=True),
           rot(1084, 160, "já fez os três, e continua com dor", w=560, tam=25, cor=TINTA, peso=700, lh=1.25)]
    return slide("palavra", 340, p, rs, eyebrow="A palavra que carrega o erro", titulo="Tendinite.")


def nome_77():
    """7.7: cada nome levando ao seu tratamento."""
    p = [svg_abre(1664, 360, "Dois nomes, cada um levando ao seu tratamento. Tendinite, riscada: sugere inflamação e empurra para anti-inflamatório, gelo e repouso. Tendinopatia: dor persistente associada à carga, aponta para a forma de carregar, e leva a carga bem administrada"), defs(FOSF, OXID)]
    rs = []
    rows = [("Tendinite", "sugere inflamação", ["anti-inflamatório", "gelo", "repouso"], FOSF, FOSF_T, "m0"),
            ("Tendinopatia", "dor persistente associada à carga", ["carga bem administrada"], OXID, OXID_T, "m1")]
    for k, (n, d, trat, cor, fundo, mk) in enumerate(rows):
        y = k * 190
        p.append(caixa(0, y, 560, 160, cor, CARTAO, esp=2 if k == 0 else 4, rx=16))
        rs += [rot(24, y + 22, n, w=510, tam=34, cor=cor, peso=700, serif=True), rot(24, y + 90, d, w=510, tam=23, cor=TINTA)]
        if k == 0:
            p.append(f'<line x1="24" y1="{y + 44}" x2="260" y2="{y + 44}" stroke="{FOSF}" stroke-width="4"/>')
        p.append(seta(566, y + 80, 640, y + 80, cor, mk, esp=4))
        if len(trat) == 3:
            for j, t in enumerate(trat):
                x = 652 + j * 340
                p.append(caixa(x, y + 30, 320, 100, cor, fundo, esp=2, rx=50))
                rs.append(rot(x, y + 64, t, w=320, tam=24, cor=TINTA, peso=700, alinha="center"))
        else:
            p.append(caixa(652, y + 30, 1012, 100, cor, cor, esp=0, rx=50))
            rs.append(rot(652, y + 62, trat[0] + ": a forma de carregar", w=1012, tam=27, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("nome", 360, p, rs, eyebrow="Consenso de terminologia, 2019", titulo="O nome muda o tratamento",
                 destaque="Não é preciosismo de vocabulário: o nome antigo empurra para o tratamento errado.", destaque_cor="tinta", fonte="Br J Sports Med 2020")


def rosca_77():
    """7.7: o corte do tendão como uma rosca: muito tecido funcional em volta de um centro alterado."""
    p = [svg_abre(1664, 380, "O corte de um tendão desenhado como uma rosca. No centro, uma pequena área degenerada, o buraco. Em volta, muito tecido funcional, a rosca, que pode ganhar capacidade. Não é preciso consertar o buraco para a pessoa voltar a correr: é preciso aumentar a capacidade do que está bom"), defs(OXID, FOSF)]
    rs = []
    cx, cy = 300, 190
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="280" ry="180" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>')
    import math
    for i in range(70):
        a = i * 2.39996
        r = 0.35 + 0.6 * ((i * 37) % 70) / 70
        x, y = cx + 250 * r * math.cos(a), cy + 160 * r * math.sin(a)
        if ((x - cx) / 110) ** 2 + ((y - cy) / 70) ** 2 > 1.2:
            p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="{OXID}" opacity="0.55"/>')
    p.append(f'<path d="M {cx - 90} {cy} C {cx - 90} {cy - 60}, {cx + 20} {cy - 70}, {cx + 80} {cy - 30} S {cx + 60} {cy + 60}, {cx} {cy + 55} S {cx - 90} {cy + 50}, {cx - 90} {cy} Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(cx - 80, cy - 14, "o buraco", w=160, tam=22, cor=FOSF, peso=700, alinha="center"))
    p.append(seta(560, 90, 700, 70, OXID, "m0", esp=3))
    p.append(seta(390, 220, 700, 270, FOSF, "m1", esp=3))
    p.append(caixa(710, 0, 954, 150, OXID, CARTAO, esp=4, rx=16))
    rs += [rot(734, 20, "A rosca: trate aqui", w=900, tam=28, cor=OXID, peso=700, serif=True),
           rot(734, 72, "muito tecido funcional em volta, que pode ganhar capacidade", w=900, tam=23, cor=TINTA, lh=1.3)]
    p.append(caixa(710, 200, 954, 150, FOSF, CARTAO, esp=2, rx=16))
    rs += [rot(734, 220, "O buraco: não precisa consertar", w=900, tam=28, cor=FOSF, peso=700, serif=True),
           rot(734, 272, "a área degenerada pode ficar; a pessoa volta a correr assim mesmo", w=900, tam=23, cor=TINTA, lh=1.3)]
    return slide("rosca", 380, p, rs, eyebrow="A revisão do modelo, 2016", titulo="Trate a rosca, não o buraco.",
                 destaque="Essa frase muda a conversa com quem chegou assustado com o laudo.", destaque_cor="tinta")


def imagem_77():
    """7.7: duas imagens de tendão; a mais alterada não dói, a menos alterada dói."""
    p = [svg_abre(1664, 400, "Duas imagens de ultrassom de tendão, em esquema. A da esquerda tem alteração evidente e não dói. A da direita tem alteração pequena e dói. Ao lado, o que cada coisa diz. Imagem alterada: comum em quem não sente dor; aumenta o risco de dor futura; não diz quanto dói hoje. Dor: pode vir com imagem pouco alterada; acompanha a carga recente, e quanto essa carga mudou")]
    rs = []
    for k, (t, cor, mancha) in enumerate([("não dói", OXID, 70), ("dói", FOSF, 18)]):
        x = k * 380
        p.append(f'<rect x="{x}" y="0" width="350" height="300" rx="12" fill="#2B3640"/>')
        for j in range(9):
            y = 60 + j * 22
            p.append(f'<path d="M {x + 20} {y} Q {x + 175} {y + (6 if j % 2 else -6)} {x + 330} {y}" fill="none" stroke="{CINZA}" stroke-width="3"/>')
        p.append(f'<ellipse cx="{x + 175}" cy="150" rx="{mancha * 1.6:.0f}" ry="{mancha * 0.7:.0f}" fill="#0B1015"/>')
        p.append(caixa(x + 60, 320, 230, 70, cor, cor, esp=0, rx=35))
        rs.append(rot(x + 60, 340, t, w=230, tam=26, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(0, 8, "esquema", w=730, tam=16, cor=PAPEL, alinha="right"))
    cols = [("Imagem alterada", ["comum em quem não sente dor", "aumenta o risco de dor futura", "não diz quanto dói hoje"], GLIC, 0),
            ("Dor", ["pode vir com imagem pouco alterada", "acompanha a carga recente", "e quanto essa carga mudou"], FOSF, 205)]
    for t, itens, cor, y in cols:
        p.append(caixa(800, y, 864, 195, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(824, y + 14, t, w=800, tam=25, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            p.append(f'<circle cx="836" cy="{y + 74 + j * 40}" r="6" fill="{cor}"/>')
            rs.append(rot(854, y + 61 + j * 40, it, w=790, tam=21, cor=TINTA))
    return slide("imagem", 400, p, rs, eyebrow="Erro dois · achar que a dor mede o estrago", titulo="Estrutura e dor andam menos juntas do que parece",
                 fonte="Metanálise de ultrassom, Br J Sports Med 2016")


def exames_77():
    """7.7: três consequências, cada uma com um pequeno desenho."""
    p = [svg_abre(1664, 380, "Três consequências práticas sobre imagem. Não é rotina: só para dúvida diagnóstica, ruptura ou caso que não evolui. Não serve de controle: a pessoa melhora e a imagem continua igual, o que frustra quem melhora. A melhora se mede na função e na dor durante a carga, não em milímetros")]
    rs = []
    cards = [("Não é rotina", "dúvida diagnóstica, ruptura, caso que não evolui", OXID), ("Não serve de controle", "a estrutura muda devagar e frustra quem melhora", GLIC),
             ("Melhora se mede na função", "e na dor durante a carga, não em milímetros", TINTA)]
    for k, (t, d, cor) in enumerate(cards):
        x = k * 564
        p.append(caixa(x, 0, 536, 380, cor, CARTAO, esp=2, rx=16))
        rs += [rot(x + 24, 20, t, w=490, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 280, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    for j, (ic, t) in enumerate([("t:zoom-question", "dúvida"), ("t:alert-triangle", "ruptura"), ("t:hourglass", "não evolui")]):
        x = 40 + j * 160
        p.append(f'<circle cx="{x + 50}" cy="150" r="46" fill="{OXID_T}"/>')
        p.append(icone(ic, x + 26, 126, 48, OXID))
        rs.append(rot(x, 206, t, w=100, tam=18, cor=OXID, peso=700, alinha="center"))
    x = 564
    for j, (t, c) in enumerate([("mês 1", FOSF), ("mês 4", OXID)]):
        xx = x + 50 + j * 240
        p.append(f'<rect x="{xx}" y="90" width="190" height="130" rx="8" fill="{TINTA}"/>')
        p.append(f'<ellipse cx="{xx + 95}" cy="155" rx="50" ry="22" fill="{MUDO}"/>')
        rs.append(rot(xx, 228, t + (": dói" if j == 0 else ": bem"), w=190, tam=19, cor=c, peso=700, alinha="center"))
    rs.append(rot(x + 240, 140, "=", w=60, tam=40, cor=GLIC, peso=700, alinha="center"))
    x = 1128
    for j, h in enumerate([40, 70, 100, 130]):
        p.append(f'<rect x="{x + 50 + j * 60}" y="{230 - h}" width="44" height="{h}" rx="4" fill="{OXID}"/>')
    p.append(icone("t:ruler-measure", x + 330, 120, 60, MUDO))
    p.append(f'<line x1="{x + 320}" y1="110" x2="{x + 400}" y2="190" stroke="{FOSF}" stroke-width="5"/>')
    rs.append(rot(x + 30, 238, "função", w=260, tam=19, cor=OXID, peso=700, alinha="center"))
    return slide("exames", 380, p, rs, eyebrow="O que isso muda sobre imagem", titulo="Três consequências práticas",
                 destaque="O laudo que assusta faz a pessoa se mover com medo, e o medo é parte do problema.", destaque_cor="verm")


def mudou_77():
    """7.7: as semanas antes da dor numa linha, com a mudança marcada antes do início da dor."""
    p = [svg_abre(1664, 400, "Quatro mudanças comuns nas semanas antes da dor: volume, mais quilômetros ou mais sessões; tipo, ladeira, escada, pliometria; retomada, voltou das férias no ritmo de antes; contexto, superfície nova, duas sessões no dia. Embaixo, uma linha das semanas: primeiro a mudança, depois a dor"), defs(MUDO)]
    rs = []
    cards = [("t:trending-up", "Volume", "mais quilômetros ou mais sessões", GLIC), ("t:stairs", "Tipo", "ladeira, escada, pliometria", GLIC),
             ("t:plane", "Retomada", "voltou das férias no ritmo de antes", FOSF), ("t:map", "Contexto", "superfície nova, duas sessões no dia", OXID)]
    for k, (ic, t, d, cor) in enumerate(cards):
        x = k * 424
        p.append(caixa(x, 0, 392, 210, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 46, cor))
        rs += [rot(x + 82, 30, t, w=290, tam=27, cor=cor, peso=700, serif=True), rot(x + 22, 100, d, w=350, tam=22, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 196}" y1="214" x2="700" y2="290" stroke="{cor}" stroke-width="2" opacity="0.6"/>')
    p.append(seta(0, 320, 1650, 320, MUDO, "m0", esp=3))
    for i in range(8):
        x = 60 + i * 190
        p.append(f'<line x1="{x}" y1="310" x2="{x}" y2="330" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<circle cx="700" cy="320" r="20" fill="{GLIC}"/>')
    p.append(f'<circle cx="1280" cy="320" r="20" fill="{FOSF}"/>')
    rs += [rot(560, 350, "a mudança", w=280, tam=22, cor=GLIC, peso=700, alinha="center"),
           rot(1140, 350, "a dor começa", w=280, tam=22, cor=FOSF, peso=700, alinha="center"),
           rot(0, 350, "semanas", w=300, tam=18, cor=MUDO)]
    return slide("mudou", 400, p, rs, eyebrow="A pergunta que abre o caso", titulo="O que mudou nas semanas antes da dor?",
                 destaque="A dor apareceu depois de uma mudança. É a mudança que se ajusta, não a existência de carga.", destaque_cor="tinta")


def compressao_77():
    """7.7: três desenhos do tendão dobrando sobre o osso, com o ponto de compressão marcado."""
    p = [svg_abre(1664, 400, "Três lugares onde o tendão, em amplitude máxima, é comprimido contra o osso, cada um desenhado como um tendão dobrando sobre um osso, com o ponto de compressão marcado. Aquiles na inserção: contra o calcanhar, com o tornozelo em flexão máxima. Isquiotibiais proximais: contra o ísquio, com o quadril muito fletido. Glúteos: na lateral do quadril, com a perna cruzada para dentro")]
    rs = []
    sitios = [("Aquiles na inserção", "contra o calcanhar, com o tornozelo em flexão máxima"), ("Isquiotibiais proximais", "contra o ísquio, com o quadril muito fletido"),
              ("Glúteos", "na lateral do quadril, com a perna cruzada para dentro")]
    for k, (t, d) in enumerate(sitios):
        x = k * 564
        p.append(caixa(x, 0, 536, 400, FOSF, CARTAO, esp=2, rx=16))
        rs += [rot(x + 24, 20, t, w=490, tam=26, cor=FOSF, peso=700, serif=True), rot(x + 24, 290, d, w=490, tam=22, cor=TINTA, lh=1.3)]
        cx, cy = x + 268, 180
        p.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="{PAPEL}" stroke="{MUDO}" stroke-width="4"/>')
        rs.append(rot(cx - 50, cy - 12, "osso", w=100, tam=18, cor=MUDO, peso=700, alinha="center"))
        p.append(f'<path d="M {cx - 190} {cy - 80} Q {cx - 70} {cy - 72} {cx} {cy - 62} Q {cx + 66} {cy - 54} {cx + 70} {cy} L {cx + 74} {cy + 90}" fill="none" stroke="{GLIC}" stroke-width="14" stroke-linecap="round"/>')
        p.append(f'<circle cx="{cx + 46}" cy="{cy - 44}" r="18" fill="{FOSF}" opacity="0.85"/>')
        p.append(f'<line x1="{cx - 200}" y1="{cy - 80}" x2="{cx - 240}" y2="{cy - 82}" stroke="{GLIC}" stroke-width="3"/>')
    rs.append(rot(24, 256, "tendão: tração + compressão", w=300, tam=18, cor=GLIC, peso=700))
    return slide("compressao", 400, p, rs, eyebrow="Erro quatro · mandar alongar", titulo="Onde o tendão é comprimido contra o osso",
                 destaque="Tração somada a compressão irrita o tecido. O alongamento sustentado faz isso várias vezes por dia.", destaque_cor="tinta",
                 fonte="Cook e Purdam, Br J Sports Med 2012")


def conduta_77():
    """7.7: as posições que denunciam compressão e o que fazer com elas."""
    p = [svg_abre(1664, 400, "À esquerda, como reconhecer sem exame, em quatro posições que pioram a dor: flexão profunda; subir escada e banco baixo; cruzar as pernas; dormir de lado com a perna de cima caída. À direita, o que fazer: reduzir posições de compressão; ajustar como senta e dorme; força em amplitude que não comprime; extremos só depois"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 780, 400, GLIC, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "Como reconhecer", w=700, tam=27, cor=GLIC, peso=700, serif=True))
    for k, (ic, t) in enumerate([("t:stretching", "piora na flexão profunda"), ("t:stairs", "subir escada, banco baixo"), ("h:person", "cruzar as pernas"), ("t:bed", "dormir de lado, perna de cima caída")]):
        col, lin = k % 2, k // 2
        x, y = 24 + col * 374, 80 + lin * 156
        p.append(f'<rect x="{x}" y="{y}" width="354" height="140" rx="12" fill="{GLIC_T}"/>')
        p.append(icone(ic, x + 18, y + 18, 48, GLIC))
        rs.append(rot(x + 18, y + 78, t, w=320, tam=21, cor=TINTA, peso=700, lh=1.2))
    p.append(seta(786, 200, 840, 200, MUDO, "m0", esp=4))
    p.append(caixa(848, 0, 816, 400, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(872, 18, "O que fazer", w=700, tam=27, cor=OXID, peso=700, serif=True))
    for k, t in enumerate(["reduzir posições de compressão", "ajustar como senta e dorme", "força em amplitude que não comprime", "extremos só depois"]):
        y = 84 + k * 78
        p.append(f'<circle cx="896" cy="{y + 26}" r="20" fill="{OXID}"/>')
        rs += [rot(876, y + 13, str(k + 1), w=40, tam=20, cor=PAPEL, peso=700, alinha="center"), rot(932, y + 12, t, w=700, tam=23, cor=TINTA, peso=700 if k == 0 else 400)]
    return slide("conduta", 400, p, rs, eyebrow="Reconhecer e aliviar", titulo="Sem exame, na conversa e no movimento",
                 destaque="Mobilidade continua importando. Evita-se o alongamento sustentado, em compressão, num tendão irritado.", destaque_cor="tinta")

# ---------------------------------------------------------------- 7.8

def caso_78():
    """7.8: a semana antes e depois do grupo novo, com o mesmo volume e outro estímulo, e o desenho da dor no Aquiles."""
    p = [svg_abre(1664, 380, "Caso ilustrativo. Um homem na casa dos quarenta, corredor há anos, três vezes por semana. Antes: três corridas parecidas. Depois do grupo novo: uma corrida, uma ladeira e um tiro, com o volume quase igual e o estímulo todo diferente. À direita, em esquema, a dor no Aquiles: forte nos primeiros minutos de corrida, melhora no meio, volta forte na primeira pisada da manhã seguinte")]
    rs = []
    p.append(caixa(0, 0, 900, 380, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("h:man", 24, 18, 56, TINTA))
    rs.append(rot(92, 30, "casa dos quarenta, corre há anos, três vezes por semana", w=790, tam=22, cor=TINTA, peso=700))
    semanas = [("antes", [("t:run", "corrida", OXID)] * 3), ("depois", [("t:run", "corrida", OXID), ("t:trending-up", "ladeira", FOSF), ("t:bolt", "tiro", FOSF)])]
    for k, (t, ses) in enumerate(semanas):
        y = 100 + k * 120
        rs.append(rot(24, y + 34, t, w=110, tam=22, cor=MUDO, peso=700))
        for j, (ic, n, cor) in enumerate(ses):
            x = 140 + j * 248
            p.append(f'<rect x="{x}" y="{y}" width="232" height="100" rx="12" fill="{cor}" opacity="{1 if cor == FOSF else 0.85}"/>')
            p.append(icone(ic, x + 18, y + 28, 44, PAPEL))
            rs.append(rot(x + 72, y + 36, n, w=150, tam=22, cor=PAPEL, peso=700))
    rs.append(rot(140, 338, "volume quase igual · o estímulo mudou todo", w=740, tam=21, cor=FOSF, peso=700))
    X = 960
    p.append(caixa(X, 0, 704, 380, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 18, "semanas depois: dor no Aquiles", w=660, tam=23, cor=FOSF, peso=700))
    p.append(f'<polyline points="{X + 50},110 {X + 130},130 {X + 220},230 {X + 330},240 {X + 420},210 {X + 520},120 {X + 640},90" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<line x1="{X + 40}" y1="270" x2="{X + 670}" y2="270" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(X + 30, 284, "começo da corrida", w=200, tam=18, cor=TINTA, peso=700, lh=1.2),
           rot(X + 220, 284, "meio", w=150, tam=18, cor=TINTA, peso=700, alinha="center"),
           rot(X + 470, 284, "primeira pisada da manhã seguinte", w=210, tam=18, cor=TINTA, peso=700, alinha="right", lh=1.2),
           rot(X + 24, 60, "dor · esquema", w=300, tam=17, cor=MUDO)]
    return slide("caso", 380, p, rs, eyebrow="Caso ilustrativo", titulo="Homem na casa dos quarenta, corredor há anos. Entraram ladeira e tiro.")


def tentativas_78():
    """7.8: quatro tentativas, cada uma com o caminho que fez até piorar ou não mudar nada."""
    p = [svg_abre(1664, 380, "Quatro tentativas, cada uma com o caminho que fez. Parou duas semanas: melhorou, voltou no mesmo ritmo, piorou. Anti-inflamatório: melhorou, voltou, piorou. Alongamento diário: piorou. Palmilha e dois tênis: nada mudou"), defs(MUDO)]
    rs = []
    linhas = [("t:bed", "Parou duas semanas", ["melhorou", "voltou no mesmo ritmo", "piorou"]), ("t:pill", "Anti-inflamatório", ["melhorou", "voltou", "piorou"]),
              ("t:stretching", "Alongamento diário", ["piorou"]), ("t:shirt-sport", "Palmilha e dois tênis", ["nada mudou"])]
    for k, (ic, t, passos) in enumerate(linhas):
        y = k * 96
        p.append(caixa(0, y, 460, 82, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 20, y + 19, 44, TINTA))
        rs.append(rot(80, y + 26, t, w=370, tam=23, cor=TINTA, peso=700))
        x = 500
        for j, ps in enumerate(passos):
            ult = j == len(passos) - 1
            cor = FOSF if ps == "piorou" else (GLIC if ps == "nada mudou" else OXID if ps == "melhorou" else MUDO)
            w = 340 if len(ps) > 12 else 220
            p.append(seta(x - 34, y + 41, x - 6, y + 41, MUDO, "m0", esp=2))
            p.append(caixa(x, y + 10, w, 62, cor, cor if ult else CARTAO, esp=2, rx=31))
            rs.append(rot(x, y + 27, ps, w=w, tam=21, cor=PAPEL if ult else cor, peso=700, alinha="center"))
            x += w + 44
    return slide("tentativas", 380, p, rs, eyebrow="O ciclo de sempre", titulo="“Já tentei de tudo e nada funciona”",
                 destaque="Faltou a única coisa com boa evidência: carga bem dosada, por tempo suficiente.", destaque_cor="tinta")


def perguntas_78():
    """7.8: três perguntas, cada uma com seu pequeno desenho."""
    p = [svg_abre(1664, 380, "Três perguntas antes de prescrever. O que mudou: volume, ladeira, tiro, salto, pausa, piso, calçado, horário, em etiquetas. Há compressão: piora em alongamento máximo, escada, agachamento fundo. E a manhã seguinte: rigidez e primeira pisada, o termômetro do dia anterior")]
    rs = []
    cards = [("O que mudou?", GLIC), ("Há compressão?", FOSF), ("E a manhã seguinte?", OXID)]
    for k, (t, cor) in enumerate(cards):
        x = k * 564
        p.append(caixa(x, 0, 536, 380, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 46}" cy="44" r="24" fill="{cor}"/>')
        rs += [rot(x + 22, 30, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(x + 86, 28, t, w=430, tam=27, cor=cor, peso=700, serif=True)]
    tags = ["volume", "ladeira", "tiro", "salto", "pausa", "piso", "calçado", "horário"]
    for j, t in enumerate(tags):
        col, lin = j % 2, j // 2
        x, y = 24 + col * 250, 100 + lin * 66
        p.append(f'<rect x="{x}" y="{y}" width="236" height="52" rx="26" fill="{GLIC_T}" stroke="{GLIC if t in ("ladeira", "tiro") else GLIC_T}" stroke-width="3"/>')
        rs.append(rot(x, y + 13, t, w=236, tam=20, cor=TINTA, peso=700, alinha="center"))
    for j, (ic, t) in enumerate([("t:stretching", "alongamento máximo"), ("t:stairs", "escada"), ("t:barbell", "agachamento fundo")]):
        y = 104 + j * 86
        p.append(f'<rect x="588" y="{y}" width="488" height="72" rx="14" fill="{FOSF_T}"/>')
        p.append(icone(ic, 604, y + 16, 40, FOSF))
        rs.append(rot(660, y + 22, "piora em " + t, w=400, tam=21, cor=TINTA, peso=700))
    p.append(icone("t:temperature", 1170, 100, 110, OXID))
    p.append(icone("t:sun", 1300, 110, 70, GLIC))
    rs += [rot(1300, 186, "primeira pisada", w=200, tam=19, cor=TINTA, peso=700),
           rot(1152, 250, "rigidez e primeira pisada: o termômetro do dia anterior", w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("perguntas", 380, p, rs, eyebrow="Passo um · entender a carga", titulo="Três perguntas antes de prescrever",
                 destaque="No caso ilustrativo, a resposta era evidente: entraram os estímulos que mais pedem do tendão como mola.", destaque_cor="tinta")


def ajuste_78():
    """7.8: a semana com picos e a mesma semana ajustada, sem os picos, com a força."""
    p = [svg_abre(1664, 420, "Duas semanas desenhadas em barras, em esquema. Na primeira, com os picos que saem por algumas semanas: tiro, ladeira, salto, mudança brusca de ritmo, posições de compressão e a sessão longa que é o dobro. Na segunda, ajustada: fica a corrida confortável em piso plano, o volume dentro da régua de dor e a força, que é o tratamento")]
    rs = []
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    antes = [(3, OXID, ""), (6, FOSF, "tiro"), (3, OXID, ""), (6, FOSF, "ladeira"), (0, OXID, ""), (9, FOSF, "longo dobrado"), (0, OXID, "")]
    depois = [(3, OXID, ""), (0, OXID, ""), (3, OXID, ""), (3, OXID, ""), (0, OXID, ""), (4, OXID, ""), (0, OXID, "")]
    forca = {1, 4}
    for k, (t, cor, dados, itens) in enumerate([("Sai por algumas semanas", FOSF, antes, ["tiro, ladeira, salto", "mudança brusca de ritmo", "posições de compressão", "a sessão longa que é o dobro"]),
                                                 ("Fica", OXID, depois, ["corrida confortável em piso plano", "volume dentro da régua de dor", "a força, que é o tratamento"])]):
        x = k * 852
        p.append(caixa(x, 0, 812, 420, cor, CARTAO, esp=2, rx=16))
        rs.append(rot(x + 24, 16, t, w=760, tam=26, cor=cor, peso=700, serif=True))
        B = 210
        for d, (v, c, lab) in enumerate(dados):
            bx = x + 40 + d * 104
            if v:
                p.append(f'<rect x="{bx}" y="{B - v * 13}" width="76" height="{v * 13}" rx="4" fill="{c}"/>')
            if k == 1 and d in forca:
                p.append(f'<rect x="{bx}" y="{B - 52}" width="76" height="52" rx="4" fill="{GLIC}"/>')
                p.append(icone("t:barbell", bx + 20, B - 44, 36, PAPEL))
            if lab:
                rs.append(rot(bx - 20, B - v * 13 - 28, lab, w=116, tam=16, cor=FOSF, peso=700, alinha="center"))
        p.append(f'<line x1="{x + 30}" y1="{B}" x2="{x + 780}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(x + 40, B + 6, "seg a dom", w=720, tam=16, cor=MUDO))
        for j, it in enumerate(itens):
            y = 262 + j * 38
            p.append(f'<circle cx="{x + 36}" cy="{y + 12}" r="6" fill="{cor}"/>')
            rs.append(rot(x + 54, y, it, w=740, tam=20, cor=TINTA, peso=700 if (k == 1 and j == 2) else 400))
    rs.append(rot(852, 392, "esquema", w=790, tam=15, cor=MUDO, alinha="right"))
    return slide("ajuste", 420, p, rs, eyebrow="Passo dois · ajustar sem zerar", titulo="Tirar os picos, manter o resto",
                 destaque="Quem chegou esperando ouvir “pare de correr” e ouve “corra de outro jeito” adere muito mais.", destaque_cor="tinta")


def regua_78():
    """7.8: a régua de dor de 0 a 10 com a faixa até 5, e as três condições."""
    p = [svg_abre(1664, 380, "Uma régua de dor de zero a dez. A faixa até cerca de cinco está liberada, com três condições: a dor volta ao basal na manhã seguinte, e a primeira pisada é o termômetro; não sobe de semana para semana, porque a tendência importa mais que o dia; e a função não piora, a pessoa continua conseguindo fazer o que fazia")]
    rs = []
    X0, E = 40, 150
    p.append(f'<rect x="{X0}" y="20" width="{5 * E}" height="70" rx="8" fill="{OXID}"/>')
    p.append(f'<rect x="{X0 + 5 * E}" y="20" width="{5 * E}" height="70" rx="8" fill="{FOSF}"/>')
    for i in range(1, 10):
        p.append(f'<line x1="{X0 + i * E}" y1="76" x2="{X0 + i * E}" y2="90" stroke="{PAPEL}" stroke-width="2"/>')
    for i in range(11):
        rs.append(rot(X0 + i * E - 30, 98, str(i), w=60, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="{X0 + 5 * E}" y1="6" x2="{X0 + 5 * E}" y2="104" stroke="{TINTA}" stroke-width="5"/>')
    rs += [rot(X0, 34, "pode treinar com dor até cerca de 5", w=5 * E, tam=22, cor=PAPEL, peso=700, alinha="center"),
           rot(X0 + 5 * E, 34, "acima: ajustar", w=5 * E, tam=22, cor=PAPEL, peso=700, alinha="center")]
    conds = [("t:sun", "Volta ao basal na manhã seguinte", "a primeira pisada é o termômetro", OXID),
             ("t:chart-line", "Não sobe de semana para semana", "a tendência importa mais que o dia", GLIC),
             ("t:run", "A função não piora", "continua conseguindo fazer o que fazia", TINTA)]
    for k, (ic, t, d, cor) in enumerate(conds):
        x = k * 564
        p.append(caixa(x, 150, 536, 230, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 172, 44, cor))
        rs += [rot(x + 84, 176, t, w=430, tam=23, cor=cor, peso=700, lh=1.2), rot(x + 24, 280, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("regua", 380, p, rs, eyebrow="Passo três · a régua da dor", titulo="Até cerca de 5 em 10, com três condições",
                 destaque="Em 38 pacientes, continuar correndo e saltando com a régua deu o mesmo resultado que o repouso ativo.", destaque_cor="petr",
                 fonte="Silbernagel e colegas, Am J Sports Med 2007")


def pesada_78():
    """7.8: degraus de carga ao longo de 12 semanas: as repetições máximas caem de 15 a 6 e a carga sobe."""
    p = [svg_abre(1664, 380, "Doze semanas em degraus, cada degrau com a largura das semanas que dura. Semana 1: 15 repetições máximas, 3 séries. Semanas 2 e 3: 12, 3 séries. Semanas 4 e 5: 10, 4 séries. Semanas 6 a 8: 8, 4 séries. Semanas 9 a 12: 6, 4 séries. A carga sobe a cada degrau, porque as repetições máximas caem")]
    rs = []
    X0, W = 40, 118
    fases = [(1, 15, 3, "1"), (2, 12, 3, "2 e 3"), (2, 10, 4, "4 e 5"), (3, 8, 4, "6 a 8"), (4, 6, 4, "9 a 12")]
    x = X0
    for k, (sem, rm, ser, lab) in enumerate(fases):
        h = 90 + k * 50
        w = sem * W
        p.append(f'<rect x="{x}" y="{320 - h}" width="{w - 6}" height="{h}" rx="8" fill="{OXID}" opacity="{0.45 + k * 0.13:.2f}"/>')
        rs += [rot(x, 320 - h + 14, f"{rm} RM", w=w - 6, tam=30 if sem > 1 else 24, cor=PAPEL, peso=700, alinha="center", serif=True),
               rot(x, 320 - h + 58, f"{ser} séries", w=w - 6, tam=18, cor=PAPEL, alinha="center"),
               rot(x, 330, "sem " + lab, w=w - 6, tam=18, cor=TINTA, peso=700, alinha="center")]
        x += w
    rs.append(rot(X0, 0, "a carga sobe a cada degrau: as repetições máximas caem", w=760, tam=21, cor=OXID, peso=700))
    return slide("pesada", 380, p, rs, eyebrow="Passo quatro · fase dois, carga pesada e lenta", titulo="A dose do ensaio dinamarquês, no Aquiles",
                 destaque="Três vezes por semana, 3 s para subir e 3 s para descer. Antes, se a dor estiver irritada, isometria: 5 × 45 s.", destaque_cor="tinta",
                 fonte="Am J Sports Med 2015 · isometria: Br J Sports Med 2015")


def comparacao_78():
    """7.8: barras lado a lado: satisfação em 12 semanas e adesão, carga pesada e lenta contra excêntrico."""
    p = [svg_abre(1664, 360, "Barras lado a lado, em 58 pessoas. Satisfeitos em 12 semanas: 100% com carga pesada e lenta, 80% com excêntrico. Adesão: 92% com carga pesada e lenta, 78% com excêntrico")]
    rs = []
    B, E = 290, 2.4
    grupos = [("satisfeitos em 12 semanas", [(100, OXID), (80, GLIC)]), ("adesão", [(92, OXID), (78, GLIC)])]
    for g, (t, barras) in enumerate(grupos):
        gx = 60 + g * 620
        for j, (v, cor) in enumerate(barras):
            x = gx + j * 230
            p.append(f'<rect x="{x}" y="{B - v * E:.0f}" width="200" height="{v * E:.0f}" rx="6" fill="{cor}"/>')
            rs.append(rot(x, B - v * E - 46, f"{v}%", w=200, tam=36, cor=cor, peso=700, alinha="center", serif=True))
        rs.append(rot(gx, B + 12, t, w=430, tam=22, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="40" y1="{B}" x2="1180" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    for k, (t, cor) in enumerate([("carga pesada e lenta", OXID), ("excêntrico", GLIC)]):
        y = 60 + k * 70
        p.append(f'<rect x="1280" y="{y}" width="40" height="40" rx="6" fill="{cor}"/>')
        rs.append(rot(1336, y + 6, t, w=320, tam=23, cor=TINTA, peso=700))
    return slide("comparacao", 360, p, rs, eyebrow="Carga pesada e lenta contra excêntrico, 58 pessoas", titulo="Os dois funcionam; um se cumpre melhor",
                 destaque="A diferença de satisfação sumiu em um ano. Carga suficiente, consistente, por tempo suficiente, importa mais que a escola.",
                 destaque_cor="tinta", fonte="Am J Sports Med 2015")


def falhas_78():
    """7.8: seis motivos de falha, cada um com um ícone."""
    p = [svg_abre(1664, 400, "Seis motivos pelos quais o tratamento parece falhar, em ladrilhos. Dose baixa: se conversa tranquilo na série, não está pesado. Tempo curto: quatro semanas é amostra grátis. Causa intacta: a ladeira continua igual. Sem fase de mola: alta, tiro no fim de semana, dor de volta. Imagem como régua: compare função, não estrutura. Bem feito e não melhora: rever o diagnóstico com o médico")]
    rs = []
    itens = [("t:barbell", "Dose baixa", "se conversa tranquilo na série, não está pesado", FOSF), ("t:hourglass", "Tempo curto", "quatro semanas é amostra grátis", FOSF),
             ("t:trending-up", "Causa intacta", "a ladeira continua igual", GLIC), ("t:bolt", "Sem fase de mola", "alta, tiro no fim de semana, dor de volta", GLIC),
             ("t:ruler-measure", "Imagem como régua", "compare função, não estrutura", OXID), ("t:stethoscope", "Bem feito e não melhora", "rever o diagnóstico com o médico", TINTA)]
    for k, (ic, t, d, cor) in enumerate(itens):
        col, lin = k % 3, k // 3
        x, y = col * 564, lin * 206
        p.append(caixa(x, y, 536, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, y + 22, 48, cor))
        rs += [rot(x + 86, y + 30, t, w=430, tam=25, cor=cor, peso=700, serif=True), rot(x + 24, y + 98, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("falhas", 400, p, rs, eyebrow="Passo seis · por que falha", titulo="Quase nunca é o tratamento")


def plano_78():
    """7.8: quatro fases do plano do caso, com o portão que cada uma precisa passar."""
    p = [svg_abre(1664, 420, "O plano do caso em quatro fases, cada uma com o portão para avançar. Primeiras semanas: corrida leve em plano; sem ladeira, tiro e alongamento sustentado; isometria se irritado. Portão: manhã seguinte estável. Força: carga pesada e lenta, três vezes por semana, registrada. Portão: força subindo, régua mantida. Mola: salto em volume baixo. Portão: régua mantida. Esporte: tiro uma vez por semana, depois ladeira. Portão: uma novidade de cada vez"), defs(MUDO)]
    rs = []
    fases = [("Primeiras semanas", "corrida leve em plano; sem ladeira, tiro e alongamento sustentado; isometria se irritado", "manhã seguinte estável", OXID),
             ("Força", "carga pesada e lenta, 3 × por semana, registrada", "força subindo, régua mantida", OXID),
             ("Mola", "salto em volume baixo", "régua mantida", GLIC),
             ("Esporte", "tiro 1 × por semana, depois ladeira", "uma novidade de cada vez", FOSF)]
    for k, (t, e, g, cor) in enumerate(fases):
        x = k * 424
        p.append(caixa(x, 0, 392, 300, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 44}" cy="44" r="24" fill="{cor}"/>')
        rs += [rot(x + 20, 30, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(x + 82, 28, t, w=300, tam=24, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 22, 100, e, w=350, tam=21, cor=TINTA, lh=1.3)]
        p.append(caixa(x, 320, 392, 100, cor, cor, esp=0, rx=16))
        p.append(icone("t:lock-open", x + 18, 346, 40, PAPEL))
        rs.append(rot(x + 68, 340, g, w=310, tam=20, cor=PAPEL, peso=700, lh=1.25))
        if k < 3:
            p.append(seta(x + 394, 370, x + 420, 370, MUDO, "m0", esp=3))
    return slide("plano", 420, p, rs, eyebrow="De volta ao caso ilustrativo", titulo="O plano, não o desfecho",
                 destaque="Depois da alta, força duas vezes por semana como hábito: é o que mais protege contra a recaída.", destaque_cor="tinta")

# ---------------------------------------------------------------- 7.9

def sala_79():
    """7.9: três perfis típicos na sala de espera, cada um com sua decisão."""
    p = [svg_abre(1664, 360, "Três perfis típicos na sala de espera, cada um com uma decisão. A corredora com dor na frente do joelho há meses, que nunca inchou, travou ou falseou. O jogador que torceu sem contato, ouviu um estalo e viu o joelho inchar em horas. O atleta com alguns meses de pós-operatório do cruzado, sem dor, com pressa de voltar")]
    rs = []
    perfis = [("h:woman", "Dor na frente do joelho", "há meses; nunca inchou, travou ou falseou", "decisão um", OXID),
              ("h:man", "Inchou em poucas horas", "torceu sem contato, estalo, o joelho saiu e voltou", "decisão dois", FOSF),
              ("h:running", "Pós-operatório com pressa", "alguns meses de cruzado, sem dor, quer jogar agora", "decisão três", GLIC)]
    for k, (ic, t, d, dec, cor) in enumerate(perfis):
        x = k * 564
        p.append(caixa(x, 0, 536, 360, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 268}" cy="86" r="62" fill="{OXID_T if cor == OXID else FOSF_T if cor == FOSF else GLIC_T}"/>')
        p.append(icone(ic, x + 228, 46, 80, cor))
        rs += [rot(x + 24, 168, t, w=490, tam=26, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 24, 216, d, w=490, tam=22, cor=TINTA, alinha="center", lh=1.3)]
        p.append(f'<rect x="{x + 168}" y="296" width="200" height="44" rx="22" fill="{cor}"/>')
        rs.append(rot(x + 168, 306, dec, w=200, tam=19, cor=PAPEL, peso=700, alinha="center"))
    return slide("sala", 360, p, rs, eyebrow="Três perfis típicos na sala de espera", titulo="Dor na frente do joelho, joelho que inchou em horas, pós-operatório com pressa.",
                 destaque="Três decisões diferentes, com urgências diferentes. O que cada profissional precisa reconhecer, encaminhar e parar de fazer.", destaque_cor="tinta")


def femoropatelar_79():
    """7.9: o joelho com a dor difusa em volta da patela, as situações que pioram e os três sinais que ela não tem."""
    p = [svg_abre(1664, 400, "À esquerda, o joelho de frente com a dor desenhada como um halo difuso em volta da patela, apontada com a mão inteira. Piora em flexão sob carga: escada, agachar, cinema; mais depois da atividade que durante. À direita, o que ela não tem: inchaço, travamento, falseio. Se tem, é a decisão dois")]
    rs = []
    p.append(caixa(0, 0, 1000, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "O padrão", w=400, tam=27, cor=OXID, peso=700, serif=True))
    p.append(f'<path d="M 140 70 C 120 160, 120 240, 140 380 M 340 70 C 360 160, 360 240, 340 380" fill="none" stroke="{MUDO}" stroke-width="4"/>')
    p.append(f'<ellipse cx="240" cy="220" rx="110" ry="120" fill="{FOSF}" opacity="0.18"/>')
    p.append(f'<ellipse cx="240" cy="220" rx="70" ry="80" fill="{FOSF}" opacity="0.22"/>')
    p.append(f'<ellipse cx="240" cy="220" rx="44" ry="54" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    p.append(icone("t:hand-stop", 330, 110, 56, FOSF))
    rs += [rot(296, 172, "aponta com a mão inteira", w=150, tam=18, cor=FOSF, peso=700, lh=1.2)]
    for k, (ic, t) in enumerate([("t:stairs", "escada"), ("t:barbell", "agachar"), ("t:movie", "cinema")]):
        y = 80 + k * 76
        p.append(f'<rect x="460" y="{y}" width="500" height="62" rx="31" fill="{OXID_T}"/>')
        p.append(icone(ic, 478, y + 13, 36, OXID))
        rs.append(rot(528, y + 18, t, w=420, tam=22, cor=TINTA, peso=700))
    rs += [rot(460, 50, "piora em flexão sob carga", w=500, tam=20, cor=OXID, peso=700),
           rot(460, 318, "mais depois da atividade que durante", w=520, tam=21, cor=TINTA, lh=1.25)]
    p.append(caixa(1040, 0, 624, 400, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(1064, 16, "O que ela não tem", w=560, tam=27, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["inchaço", "travamento", "falseio"]):
        y = 80 + k * 76
        p.append(icone("t:x", 1064, y + 10, 40, FOSF))
        rs.append(rot(1120, y + 14, t, w=500, tam=24, cor=TINTA, peso=700))
    p.append(caixa(1064, 316, 576, 64, FOSF, FOSF, esp=0, rx=32))
    rs.append(rot(1064, 334, "se tem: é a decisão dois", w=576, tam=22, cor=PAPEL, peso=700, alinha="center"))
    return slide("femoropatelar", 400, p, rs, eyebrow="Decisão um · dor na frente do joelho", titulo="Reconhecer a dor femoropatelar sem exame",
                 destaque="É a queixa de joelho mais comum em quem corre, agacha, e no adolescente que cresce rápido.", destaque_cor="tinta")


def mensagens_79():
    """7.9: duas falas de primeiro contato, em balões."""
    p = [svg_abre(1664, 340, "Dois balões de fala para o primeiro contato. Não é desgaste: não é artrose, e o joelho não está acabando; o medo quase sempre vem de laudo mal explicado. Parar e esperar não resolve: uma parte importante continua com dor anos depois; é um dos quadros que mais cronificam")]
    rs = []
    for k, (ic, t, d, cor, fundo) in enumerate([("t:shield-check", "“Não é desgaste.”", "não é artrose, e o joelho não está acabando; o medo quase sempre vem de laudo mal explicado", OXID, OXID_T),
                                                 ("t:hourglass", "“Parar e esperar não resolve.”", "uma parte importante continua com dor anos depois; é um dos quadros que mais cronificam", FOSF, FOSF_T)]):
        x = k * 852
        p.append(f'<path d="M {x + 20} 0 H {x + 792} Q {x + 812} 0 {x + 812} 20 V 260 Q {x + 812} 280 {x + 792} 280 H {x + 180} L {x + 110} 336 L {x + 120} 280 H {x + 20} Q {x} 280 {x} 260 V 20 Q {x} 0 {x + 20} 0 Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        p.append(icone(ic, x + 28, 28, 52, cor))
        rs += [rot(x + 96, 34, t, w=690, tam=30, cor=cor, peso=700, serif=True), rot(x + 28, 120, d, w=760, tam=24, cor=TINTA, lh=1.35)]
    return slide("mensagens", 340, p, rs, eyebrow="No primeiro contato", titulo="Duas mensagens que mudam o tratamento",
                 fonte="Consenso de dor femoropatelar, Br J Sports Med 2016")


def fazer_79():
    """7.9: o tratamento em tamanho de evidência: exercício grande, complementos médios, o resto apagado."""
    p = [svg_abre(1664, 400, "O tratamento desenhado pelo tamanho da evidência. Uma caixa grande: exercício de quadril e joelho, quadríceps e glúteos, carga que progride, por meses. Duas caixas médias de complemento: ajuste de treino, porque quase sempre houve mudança de carga antes da dor; palmilha pré-fabricada, apoiada para alívio no curto prazo. Duas caixas pequenas e apagadas: bandagem patelar, com incerteza; mobilização isolada e eletroterapia, não recomendadas")]
    rs = []
    p.append(caixa(0, 0, 760, 400, OXID, OXID, esp=0, rx=18))
    p.append(icone("t:barbell", 32, 32, 80, PAPEL))
    rs += [rot(32, 140, "Exercício de quadril e joelho", w=700, tam=36, cor=PAPEL, peso=700, serif=True, lh=1.15),
           rot(32, 250, "quadríceps e glúteos, carga que progride, por meses", w=690, tam=25, cor=PAPEL, lh=1.3)]
    for k, (t, d, cor, fundo) in enumerate([("Ajuste de treino", "quase sempre houve mudança de carga antes da dor", OXID, OXID_T),
                                            ("Palmilha pré-fabricada", "apoiada para alívio no curto prazo, como complemento", GLIC, GLIC_T)]):
        y = k * 140
        p.append(caixa(800, y, 864, 124, cor, fundo, esp=2, rx=16))
        rs += [rot(824, y + 16, t, w=820, tam=26, cor=cor, peso=700, serif=True), rot(824, y + 62, d, w=820, tam=22, cor=TINTA)]
    for k, (t, d) in enumerate([("Bandagem patelar", "incerteza"), ("Mobilização isolada, eletroterapia", "não recomendadas")]):
        x = 800 + k * 440
        p.append(caixa(x, 290, 424, 110, CINZA, PAPEL, esp=2, rx=14))
        rs += [rot(x + 20, 304, t, w=390, tam=21, cor=MUDO, peso=700, lh=1.2), rot(x + 20, 362, d, w=390, tam=20, cor=FOSF if k else MUDO, peso=700)]
    return slide("fazer", 400, p, rs, eyebrow="Consenso de tratamento, 2018", titulo="O que fazer", fonte="Br J Sports Med 2018")


def naofazer_79():
    """7.9: quatro erros de rotina, cada um riscado."""
    p = [svg_abre(1664, 360, "Quatro erros de rotina, cada um com um X. Parar e esperar: a força cai e a dor volta pior. Imagem por reflexo: raramente muda a conduta, e traz achados de quem não tem dor. Recurso passivo sozinho: ajuda a atravessar a dor, mas quem trata é o exercício. Prometer duas semanas: o quadro leva meses")]
    rs = []
    itens = [("t:bed", "Parar e esperar", "a força cai e a dor volta pior", FOSF), ("t:eye", "Imagem por reflexo", "raramente muda a conduta; achados de quem não tem dor", FOSF),
             ("t:adjustments-horizontal", "Recurso passivo sozinho", "ajuda a atravessar a dor; quem trata é o exercício", GLIC), ("t:calendar", "Prometer duas semanas", "o quadro leva meses", GLIC)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 0, 392, 360, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 52, cor))
        p.append(icone("t:x", x + 330, 24, 40, FOSF))
        rs += [rot(x + 24, 104, t, w=350, tam=26, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 24, 200, d, w=350, tam=22, cor=TINTA, lh=1.3)]
    return slide("naofazer", 360, p, rs, eyebrow="E o que parar de fazer", titulo="Quatro erros de rotina",
                 destaque="No adolescente, a mesma lógica, com o tendão abaixo da patela e a placa de crescimento em mente, e ainda mais paciência.", destaque_cor="tinta")


def inchou_79():
    """7.9: o inchaço que sobe em horas contra o que aparece no dia seguinte, e os quatro sinais."""
    p = [svg_abre(1664, 400, "À esquerda, em esquema, duas curvas de inchaço depois do trauma. Uma sobe nas primeiras horas: sangue na articulação até prova em contrário. Outra só aparece no dia seguinte: mais comum e menos grave. À direita, os quatro sinais que somados elevam a suspeita: mecanismo sem contato, na mudança de direção, desaceleração ou aterrissagem; estalo, ou sensação de que o joelho saiu do lugar e voltou; inchaço rápido, nas primeiras horas; insegurança, a sensação de que o joelho vai falhar")]
    rs = []
    p.append(caixa(0, 0, 820, 400, TINTA, CARTAO, esp=2, rx=16))
    X0, B = 50, 320
    p.append(f'<line x1="{X0}" y1="{B}" x2="790" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {X0} {B} C 120 {B - 10}, 160 110, 280 90 S 600 80, 780 84" fill="none" stroke="{FOSF}" stroke-width="6"/>')
    p.append(f'<path d="M {X0} {B} C 300 {B - 4}, 420 {B - 20}, 520 230 S 700 200, 780 196" fill="none" stroke="{MUDO}" stroke-width="4"{TRACO}/>')
    p.append(f'<line x1="200" y1="{B}" x2="200" y2="{B + 10}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="560" y1="{B}" x2="560" y2="{B + 10}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(110, B + 16, "poucas horas", w=180, tam=18, cor=TINTA, peso=700, alinha="center"),
           rot(470, B + 16, "dia seguinte", w=180, tam=18, cor=TINTA, peso=700, alinha="center"),
           rot(300, 20, "em horas: sangue na articulação até prova em contrário", w=500, tam=20, cor=FOSF, peso=700, lh=1.15),
           rot(560, 132, "no dia seguinte: mais comum, menos grave", w=230, tam=19, cor=MUDO, peso=700, lh=1.2),
           rot(24, 16, "inchaço · esquema", w=300, tam=17, cor=MUDO)]
    sinais = [("Mecanismo sem contato", "mudança de direção, desaceleração, aterrissagem", FOSF), ("Estalo", "ou o joelho saiu do lugar e voltou", FOSF),
              ("Inchaço rápido", "nas primeiras horas, não no dia seguinte", FOSF), ("Insegurança", "a sensação de que o joelho vai falhar", GLIC)]
    for k, (t, d, cor) in enumerate(sinais):
        y = k * 102
        p.append(caixa(860, y, 804, 90, cor, FOSF_T if cor == FOSF else GLIC_T, esp=2, rx=14))
        rs += [rot(884, y + 12, t, w=760, tam=23, cor=cor, peso=700), rot(884, y + 50, d, w=760, tam=20, cor=TINTA)]
    return slide("inchou", 400, p, rs, eyebrow="Decisão dois · inchou em poucas horas", titulo="Sangue na articulação até prova em contrário",
                 destaque="No esporte, a causa mais comum desse sangramento é a lesão do ligamento cruzado anterior.", destaque_cor="verm")


def gramado_79():
    """7.9: no gramado, quatro passos em fila; ao lado, três coisas riscadas."""
    p = [svg_abre(1664, 380, "No gramado, quatro passos em fila: tirar do jogo, sem negociar; deixar confortável; controlar dor e inchaço; encaminhar para avaliação médica. Ao lado, riscadas: testar o joelho com adrenalina alta; deixar voltar porque a dor passou; prometer que não foi nada"), defs(MUDO)]
    rs = []
    rs.append(rot(0, 0, "Fazer", w=400, tam=27, cor=OXID, peso=700, serif=True))
    passos = [("t:door-exit", "tirar do jogo, sem negociar"), ("t:heart-handshake", "deixar confortável"), ("t:droplet", "controlar dor e inchaço"), ("t:stethoscope", "encaminhar para avaliação médica")]
    for k, (ic, t) in enumerate(passos):
        y = 50 + k * 82
        p.append(caixa(0, y, 900, 70, OXID, OXID_T if k else OXID, esp=2, rx=14))
        p.append(icone(ic, 20, y + 15, 40, PAPEL if k == 0 else OXID))
        rs.append(rot(76, y + 20, t, w=800, tam=23, cor=PAPEL if k == 0 else TINTA, peso=700))
        if k < 3:
            p.append(seta(450, y + 70, 450, y + 82, MUDO, "m0", esp=2))
    p.append(caixa(960, 0, 704, 380, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(984, 18, "Não fazer", w=600, tam=27, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["testar o joelho com adrenalina alta", "deixar voltar porque a dor passou", "prometer que “não foi nada”"]):
        y = 90 + k * 92
        p.append(icone("t:x", 984, y, 40, FOSF))
        rs.append(rot(1040, y + 6, t, w=600, tam=23, cor=TINTA, peso=700 if k == 1 else 400))
    return slide("gramado", 380, p, rs, eyebrow="No momento", titulo="O que a comissão faz no gramado",
                 destaque="Nem todo joelho que incha assim é cruzado: menisco, cartilagem e luxação da patela também incham rápido.", destaque_cor="tinta")


def depois_79():
    """7.9: uma balança entre cirurgia e reabilitação sem cirurgia, com os pesos; ao lado, o que vale para os dois caminhos."""
    p = [svg_abre(1664, 400, "Uma balança com cirurgia num prato e reabilitação sem cirurgia no outro, e a pessoa no meio. O que pesa na decisão: esporte e nível; idade e lesões associadas; instabilidade no dia a dia; o que a pessoa quer fazer. Ao lado, o que vale para os dois caminhos: a reabilitação decide o resultado; o tempo é longo; e isso é dito no começo, não no meio")]
    rs = []
    p.append(caixa(0, 0, 1000, 400, GLIC, CARTAO, esp=2, rx=16))
    cx = 500
    p.append(f'<path d="M {cx - 40} 250 L {cx} 120 L {cx + 40} 250 Z" fill="{GLIC}"/>')
    p.append(f'<line x1="{cx - 300}" y1="120" x2="{cx + 300}" y2="120" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>')
    for sx, t in [(cx - 300, "cirurgia"), (cx + 300, "reabilitação sem cirurgia")]:
        p.append(f'<line x1="{sx}" y1="120" x2="{sx - 80}" y2="190" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<line x1="{sx}" y1="120" x2="{sx + 80}" y2="190" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<path d="M {sx - 100} 190 H {sx + 100} Q {sx} 250 {sx - 100} 190 Z" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
        rs.append(rot(sx - 140, 60, t, w=280, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.15))
    p.append(icone("h:person", cx - 30, 40, 60, TINTA))
    for k, t in enumerate(["esporte e nível", "idade e lesões associadas", "instabilidade no dia a dia", "o que a pessoa quer fazer"]):
        col, lin = k % 2, k // 2
        x, y = 24 + col * 480, 280 + lin * 56
        p.append(f'<rect x="{x}" y="{y}" width="466" height="46" rx="23" fill="{GLIC_T}"/>')
        rs.append(rot(x, y + 11, t, w=466, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(caixa(1040, 0, 624, 400, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(1064, 18, "Vale para os dois caminhos", w=580, tam=26, cor=OXID, peso=700, serif=True))
    for k, t in enumerate(["a reabilitação decide o resultado", "o tempo é longo", "dito no começo, não no meio"]):
        y = 96 + k * 96
        p.append(icone("t:check", 1064, y, 40, OXID))
        rs.append(rot(1118, y + 6, t, w=520, tam=24, cor=TINTA, peso=700 if k == 0 else 400))
    return slide("depois", 400, p, rs, eyebrow="Depois da confirmação", titulo="Nem toda lesão do cruzado vai para cirurgia",
                 destaque="A decisão é médica e compartilhada. Expectativa mal calibrada no começo vira pressa lá na frente.", destaque_cor="tinta")


def grindem_79():
    """7.9: o risco caindo mês a mês até o nono e depois plano; ao lado, 38% contra 6% de nova lesão."""
    p = [svg_abre(1664, 400, "À esquerda, em esquema, o risco de nova lesão no joelho conforme o mês da volta: cai cerca de 51% por mês de espera até o nono mês de cirurgia e, depois disso, adiar mais não reduziu. À direita, duas barras: 38% de nova lesão entre quem não passou nos critérios de retorno, e cerca de 6% entre quem passou")]
    rs = []
    p.append(caixa(0, 0, 900, 400, OXID, CARTAO, esp=2, rx=16))
    X0, B, E = 60, 320, 64
    pts = []
    for m in range(13):
        r = 0.49 ** min(m, 9)
        pts.append(f"{X0 + m * E},{B - 40 - 220 * r ** 0.45:.0f}")
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X0 + 12 * E}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="{X0 + 9 * E}" y1="60" x2="{X0 + 9 * E}" y2="{B}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    for m in (0, 3, 6, 9, 12):
        rs.append(rot(X0 + m * E - 30, B + 8, str(m), w=60, tam=18, cor=MUDO, alinha="center"))
    rs += [rot(X0, B + 40, "mês da volta depois da cirurgia · esquema", w=800, tam=17, cor=MUDO),
           rot(140, 30, "−51% de nova lesão por mês de espera", w=440, tam=24, cor=OXID, peso=700, serif=True),
           rot(X0 + 9 * E + 10, 170, "depois do nono mês: plano", w=230, tam=19, cor=TINTA, peso=700, lh=1.2)]
    X, B2, E2 = 960, 330, 6
    p.append(caixa(X, 0, 704, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 16, "nova lesão no joelho", w=660, tam=23, cor=TINTA, peso=700))
    for j, (v, t, cor) in enumerate([(38, "não passou nos critérios", FOSF), (6, "passou", OXID)]):
        x = X + 80 + j * 320
        p.append(f'<rect x="{x}" y="{B2 - v * E2}" width="220" height="{v * E2}" rx="6" fill="{cor}"/>')
        rs += [rot(x, B2 - v * E2 - 50, f"{v}%", w=220, tam=40, cor=cor, peso=700, alinha="center", serif=True),
               rot(x - 40, B2 + 10, t, w=300, tam=20, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="{X + 40}" y1="{B2}" x2="{X + 664}" y2="{B2}" stroke="{MUDO}" stroke-width="2"/>')
    return slide("grindem", 400, p, rs, eyebrow="Decisão três · coorte de Delaware e Oslo, 106 atletas", titulo="Tempo e critério, os dois",
                 destaque="Depois do nono mês, adiar mais não reduziu o risco. Voltar cedo e voltar sem critério são erros que se somam.", destaque_cor="tinta",
                 fonte="Grindem e colegas, Br J Sports Med 2016")


def regras_79():
    """7.9: três regras, cada uma com um pequeno desenho: a ampulheta, os critérios, o calendário do primeiro ao oitavo mês."""
    p = [svg_abre(1664, 380, "Três regras do retorno. Tempo é necessário, não suficiente: nove meses sem critério não libera. Critério decide: simetria de força do quadríceps, testes funcionais, o gesto do esporte. O prazo se combina no primeiro mês: aí a decisão do oitavo é só cumprir um plano"), defs(MUDO)]
    rs = []
    regras = [("Tempo é necessário, não suficiente", "nove meses sem critério não libera", GLIC), ("Critério decide", "", OXID), ("O prazo se combina no primeiro mês", "aí a decisão do oitavo é só cumprir um plano", TINTA)]
    for k, (t, d, cor) in enumerate(regras):
        x = k * 564
        p.append(caixa(x, 0, 536, 380, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 46}" cy="46" r="24" fill="{cor}"/>')
        rs += [rot(x + 22, 32, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(x + 86, 26, t, w=430, tam=24, cor=cor, peso=700, serif=True, lh=1.15)]
        if d:
            rs.append(rot(x + 24, 290, d, w=490, tam=22, cor=TINTA, lh=1.3))
    p.append(icone("t:hourglass", 70, 120, 110, GLIC))
    p.append(icone("t:x", 330, 140, 70, FOSF))
    rs.append(rot(220, 220, "9 meses sozinho", w=300, tam=20, cor=GLIC, peso=700, alinha="center"))
    for j, (ic, t) in enumerate([("t:barbell", "simetria de força do quadríceps"), ("t:checklist", "testes funcionais"), ("t:ball-football", "o gesto do esporte")]):
        y = 120 + j * 82
        p.append(f'<rect x="588" y="{y}" width="488" height="68" rx="34" fill="{OXID_T}"/>')
        p.append(icone(ic, 606, y + 16, 36, OXID))
        rs.append(rot(656, y + 21, t, w=410, tam=21, cor=TINTA, peso=700))
    p.append(caixa(1160, 130, 150, 110, TINTA, TINTA, esp=0, rx=12))
    p.append(caixa(1400, 130, 150, 110, TINTA, CARTAO, esp=2, rx=12))
    p.append(seta(1314, 185, 1394, 185, MUDO, "m0", esp=3))
    rs += [rot(1160, 158, "mês 1", w=150, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(1160, 196, "combina", w=150, tam=18, cor=PAPEL, alinha="center"),
           rot(1400, 158, "mês 8", w=150, tam=24, cor=TINTA, peso=700, alinha="center"), rot(1400, 196, "cumpre", w=150, tam=18, cor=TINTA, alinha="center")]
    return slide("regras", 380, p, rs, eyebrow="O que isso significa para a equipe", titulo="Três regras do retorno",
                 destaque="Os testes específicos ficam para o módulo de reabilitação.", destaque_cor="tinta")


def prevencao_79():
    """7.9: o aquecimento estruturado no centro, com seus quatro componentes e a condição de fazer de verdade."""
    p = [svg_abre(1664, 360, "O aquecimento estruturado no centro, em grupo e sem equipamento, com quatro componentes em volta: força, equilíbrio, aterrissagem e mudança de direção. Embaixo, a condição: várias vezes por semana, a temporada inteira. E uma etiqueta: atenção especial à atleta mulher")]
    rs = []
    p.append(caixa(560, 90, 544, 150, OXID, OXID, esp=0, rx=20))
    rs += [rot(570, 116, "Aquecimento estruturado", w=524, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(570, 170, "em grupo, sem equipamento", w=524, tam=22, cor=PAPEL, alinha="center")]
    comps = [("t:barbell", "força", 0, 0), ("t:yoga", "equilíbrio", 0, 200), ("t:arrow-down-right", "aterrissagem", 1184, 0), ("t:arrows-exchange", "mudança de direção", 1184, 200)]
    for ic, t, x, y in comps:
        p.append(caixa(x, y, 480, 130, OXID, OXID_T, esp=2, rx=16))
        p.append(icone(ic, x + 24, y + 37, 56, OXID))
        rs.append(rot(x + 100, y + 46, t, w=360, tam=26, cor=TINTA, peso=700))
        p.append(f'<line x1="{x + 480 if x == 0 else x}" y1="{y + 65}" x2="{560 if x == 0 else 1104}" y2="165" stroke="{OXID}" stroke-width="3"/>')
    p.append(caixa(560, 270, 544, 70, GLIC, GLIC_T, esp=2, rx=35))
    rs.append(rot(560, 290, "várias vezes por semana, a temporada inteira", w=544, tam=21, cor=TINTA, peso=700, alinha="center"))
    p.append(caixa(640, 0, 384, 60, FOSF, FOSF_T, esp=2, rx=30))
    p.append(icone("h:woman", 656, 10, 40, FOSF))
    rs.append(rot(704, 17, "atenção à atleta mulher", w=310, tam=20, cor=FOSF, peso=700))
    return slide("prevencao", 360, p, rs, eyebrow="A parte que evitaria boa parte disso", titulo="Aquecimento estruturado reduz lesão do cruzado, quando é feito de verdade.",
                 destaque="Os números de efeito e o problema da adesão fecham o módulo.", destaque_cor="tinta")

# ---------------------------------------------------------------- 7.10

def abertura_710():
    """7.10: duas filas, tornozelo e ombro, cada uma com a alta cedo demais e a volta do problema."""
    p = [svg_abre(1664, 360, "Duas filas com o mesmo erro. Tornozelo: torceu; anda sem dor; alta; torce de novo. Ombro: dói devagar; o repouso aliviou; alta; o volume volta e a dor volta. Nas duas, a alta está marcada cedo demais"), defs(MUDO)]
    rs = []
    filas = [("t:ball-football", "Tornozelo", ["torceu", "anda sem dor", "alta", "torce de novo"]), ("t:swimming", "Ombro", ["dói devagar", "o repouso aliviou", "alta", "volume volta, dor volta"])]
    for k, (ic, t, passos) in enumerate(filas):
        y = k * 180
        p.append(icone(ic, 0, y + 40, 56, TINTA))
        rs.append(rot(0, y + 104, t, w=160, tam=22, cor=TINTA, peso=700))
        for j, ps in enumerate(passos):
            x = 180 + j * 372
            alta = ps == "alta"
            fim = j == 3
            cor = GLIC if alta else FOSF if fim else OXID
            p.append(caixa(x, y + 20, 330, 110, cor, cor if fim else (GLIC_T if alta else CARTAO), esp=3 if alta else 2, rx=16))
            rs.append(rot(x, y + 58, ps, w=330, tam=24, cor=PAPEL if fim else TINTA, peso=700, alinha="center"))
            if alta:
                rs.append(rot(x, y + 136, "cedo demais", w=330, tam=19, cor=GLIC, peso=700, alinha="center"))
            if j < 3:
                p.append(seta(x + 334, y + 75, x + 368, y + 75, MUDO, "m0", esp=3))
    return slide("abertura", 360, p, rs, eyebrow="Duas regiões, um erro em comum", titulo="A conduta padrão termina cedo demais.")


def ottawa_710():
    """7.10: o tornozelo de lado e de dentro, com os pontos da regra de Ottawa, e os números da revisão."""
    p = [svg_abre(1664, 400, "Dois desenhos do tornozelo, por fora e por dentro, com os pontos da regra de Ottawa marcados. Por fora: borda posterior do maléolo lateral e base do quinto metatarso. Por dentro: borda posterior do maléolo medial e navicular. Embaixo, quatro pegadas: não conseguir dar quatro passos também pede imagem. À direita, a revisão: 27 estudos, 15.581 pacientes, sensibilidade combinada de 97,6% para fratura")]
    rs = []
    def pe(x, t, pts):
        p.append(caixa(x, 0, 430, 300, TINTA, CARTAO, esp=2, rx=16))
        rs.append(rot(x + 20, 14, t, w=390, tam=20, cor=TINTA, peso=700))
        p.append(f'<path d="M {x + 130} 50 L {x + 130} 190 C {x + 120} 230, {x + 70} 240, {x + 70} 262 L {x + 390} 262 C {x + 400} 240, {x + 340} 228, {x + 280} 214 C {x + 220} 200, {x + 200} 180, {x + 190} 160 L {x + 190} 50" fill="{PAPEL}" stroke="{MUDO}" stroke-width="3"/>')
        p.append(f'<circle cx="{x + 160}" cy="188" r="22" fill="{CINZA}"/>')
        for px, py, lab in pts:
            p.append(f'<circle cx="{x + px}" cy="{py}" r="14" fill="{FOSF}" stroke="{PAPEL}" stroke-width="3"/>')
    pe(0, "por fora", [(136, 176, ""), (300, 248, "")])
    pe(450, "por dentro", [(136, 176, ""), (250, 214, "")])
    rs += [rot(200, 120, "maléolo", w=200, tam=17, cor=FOSF, peso=700), rot(236, 270, "base do 5º metatarso", w=180, tam=16, cor=FOSF, peso=700, alinha="right"),
           rot(650, 120, "maléolo", w=200, tam=17, cor=FOSF, peso=700), rot(700, 270, "navicular", w=160, tam=16, cor=FOSF, peso=700, alinha="right")]
    for i in range(4):
        x = 40 + i * 90 + (i % 2) * 10
        p.append(f'<ellipse cx="{x + 20}" cy="{340 + (i % 2) * 22}" rx="14" ry="22" fill="{TINTA}" opacity="0.7"/>')
    rs.append(rot(420, 336, "não dá quatro passos: também pede imagem", w=460, tam=20, cor=TINTA, peso=700))
    nums = [("27", "estudos", TINTA), ("15.581", "pacientes", TINTA), ("97,6%", "sensibilidade combinada para fratura", OXID)]
    for k, (n, t, cor) in enumerate(nums):
        y = k * 134
        p.append(caixa(940, y, 724, 120, cor, OXID_T if cor == OXID else CARTAO, esp=2, rx=16))
        rs += [rot(964, y + 26, n, w=260, tam=48, cor=cor, peso=700, serif=True), rot(1230, y + 38, t, w=410, tam=22, cor=TINTA, lh=1.25)]
    return slide("ottawa", 400, p, rs, eyebrow="Tornozelo · passo um · precisa de radiografia?", titulo="A regra de Ottawa",
                 destaque="Pede imagem: dor óssea na borda posterior dos maléolos, na base do quinto metatarso ou no navicular, ou não conseguir dar quatro passos.",
                 destaque_cor="tinta", fonte="Revisão sistemática, BMJ 2003")


def alerta_710():
    """7.10: cinco sinais de alarme em fila."""
    p = [svg_abre(1664, 300, "Cinco sinais que pedem avaliação urgente, qualquer que seja a regra: deformidade visível; não apoia o pé no chão; dor desproporcional; formigamento ou perda de sensibilidade; pé pálido ou frio")]
    rs = []
    itens = [("t:alert-triangle", "Deformidade", "visível"), ("t:walk", "Não apoia", "o pé no chão"), ("t:bolt", "Dor", "desproporcional"),
             ("t:wave-sine", "Formigamento", "ou perda de sensibilidade"), ("t:temperature", "Pé pálido", "ou frio")]
    for k, (ic, t, d) in enumerate(itens):
        x = k * 337
        p.append(caixa(x, 0, 312, 300, FOSF, FOSF_T, esp=2, rx=16))
        p.append(f'<circle cx="{x + 156}" cy="80" r="50" fill="{FOSF}"/>')
        p.append(icone(ic, x + 128, 52, 56, PAPEL))
        rs += [rot(x + 14, 156, t, w=284, tam=26, cor=FOSF, peso=700, serif=True, alinha="center"), rot(x + 16, 204, d, w=284, tam=21, cor=TINTA, alinha="center", lh=1.25)]
    return slide("alerta", 300, p, rs, eyebrow="Qualquer que seja a regra", titulo="Sinais que pedem avaliação urgente",
                 destaque="Qualquer um desses tira a conversa da beira do campo.", destaque_cor="verm")


def semana_710():
    """7.10: a primeira semana numa linha de sete dias: proteção curta, movimento e apoio desde cedo."""
    p = [svg_abre(1664, 400, "A primeira semana numa linha de sete dias. Proteção nas primeiras 48 horas. Mobilização precoce, mover e apoiar no que a dor permite, começando cedo e crescendo ao longo da semana. Anti-inflamatório nos primeiros dias, para dor e inchaço. Embaixo, riscados: imobilizar por semanas sem indicação médica; achar que o remédio substitui reabilitação")]
    rs = []
    X0, D = 280, 196
    for d in range(8):
        p.append(f'<line x1="{X0 + d * D}" y1="0" x2="{X0 + d * D}" y2="250" stroke="{BORDA}" stroke-width="2"/>')
    for d in range(7):
        rs.append(rot(X0 + d * D, 256, f"dia {d + 1}", w=D, tam=18, cor=MUDO, alinha="center"))
    linhas = [("proteção", GLIC, GLIC_T), ("mover e apoiar", OXID, OXID_T), ("anti-inflamatório", AZUL, AZUL_T)]
    for k, (t, cor, fundo) in enumerate(linhas):
        rs.append(rot(0, 22 + k * 80, t, w=260, tam=22, cor=cor, peso=700, alinha="right"))
    p.append(f'<rect x="{X0}" y="10" width="{2 * D}" height="60" rx="10" fill="{GLIC}"/>')
    rs.append(rot(X0, 28, "primeiras 48 h", w=2 * D, tam=20, cor=PAPEL, peso=700, alinha="center"))
    p.append(f'<path d="M {X0} 150 L {X0 + 7 * D} 90 L {X0 + 7 * D} 150 Z" fill="{OXID}"/>')
    rs.append(rot(X0 + 3 * D, 120, "no que a dor permite, desde cedo", w=4 * D - 20, tam=19, cor=PAPEL, peso=700, alinha="right"))
    p.append(f'<rect x="{X0}" y="170" width="{3 * D}" height="60" rx="10" fill="{AZUL}"/>')
    rs.append(rot(X0, 188, "primeiros dias: dor e inchaço", w=3 * D, tam=19, cor=PAPEL, peso=700, alinha="center"))
    for k, t in enumerate(["imobilizar por semanas sem indicação médica", "achar que o remédio substitui reabilitação"]):
        x = k * 842
        p.append(caixa(x, 300, 822, 90, FOSF, FOSF_T, esp=2, rx=14))
        p.append(icone("t:x", x + 20, 325, 40, FOSF))
        rs.append(rot(x + 76, 330, t, w=730, tam=22, cor=TINTA, peso=700))
    return slide("semana", 400, p, rs, eyebrow="Tornozelo · passo dois · a primeira semana", titulo="Proteger pouco, mover cedo",
                 fonte="Revisão de 46 revisões sistemáticas, Br J Sports Med 2017")


def alta_710():
    """7.10: duas marcas de pronto e uma barra vazia: a reabilitação que evita a próxima torção nem começou."""
    p = [svg_abre(1664, 320, "Duas caixas marcadas: anda sem dor, e o inchaço sumiu. Ao lado, a palavra alta com um ponto de interrogação. Embaixo, uma barra vazia: a parte que evita a próxima torção nem começou")]
    rs = []
    for k, t in enumerate(["anda sem dor", "o inchaço sumiu"]):
        x = k * 420
        p.append(caixa(x, 0, 390, 110, OXID, OXID_T, esp=2, rx=16))
        p.append(icone("t:check", x + 24, 31, 48, OXID))
        rs.append(rot(x + 88, 38, t, w=290, tam=25, cor=TINTA, peso=700))
    p.append(caixa(900, 0, 340, 110, GLIC, GLIC_T, esp=3, rx=55))
    rs.append(rot(900, 24, "alta?", w=340, tam=44, cor=GLIC, peso=700, alinha="center", serif=True))
    p.append(f'<line x1="930" y1="96" x2="1210" y2="14" stroke="{FOSF}" stroke-width="6"/>')
    rs.append(rot(0, 160, "a parte que evita a próxima torção", w=1300, tam=24, cor=FOSF, peso=700))
    p.append(f'<rect x="0" y="210" width="1664" height="70" rx="35" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<rect x="6" y="216" width="40" height="58" rx="29" fill="{FOSF}"/>')
    rs.append(rot(70, 230, "nem começou", w=1560, tam=24, cor=FOSF, peso=700))
    return slide("alta", 320, p, rs, eyebrow="O erro clássico", titulo="Anda sem dor, o inchaço sumiu. Alta?")


def instabilidade_710():
    """7.10: duas fileiras de dez tornozelos: quatro marcados na estimativa baixa, sete na alta."""
    p = [svg_abre(1664, 300, "Duas fileiras de dez pessoas depois da primeira entorse. Na estimativa mais baixa, cerca de quatro em cada dez desenvolvem instabilidade crônica. Na mais alta, até sete em cada dez, conforme o critério e a população")]
    rs = []
    for k, (n, t, d, cor) in enumerate([(4, "~40%", "nas estimativas mais baixas", GLIC), (7, "até 70%", "nas mais altas, conforme critério e população", FOSF)]):
        y = k * 150
        for i in range(10):
            p.append(icone("h:person", 380 + i * 82, y + 10, 70, cor if i < n else CINZA))
        rs += [rot(0, y + 10, t, w=340, tam=46, cor=cor, peso=700, serif=True), rot(0, y + 76, d, w=340, tam=20, cor=TINTA, lh=1.25)]
    rs.append(rot(1220, 120, "cada figura: uma pessoa depois da primeira entorse", w=440, tam=19, cor=MUDO, lh=1.3))
    return slide("instabilidade", 300, p, rs, eyebrow="Tornozelo · passo três · por que reabilitar", titulo="Instabilidade crônica depois da primeira entorse",
                 destaque="Insegurança, torções repetidas e limitação por anos: uma lesão que parece banal e deixa sequela.", destaque_cor="verm",
                 fonte="Consenso do International Ankle Consortium, Br J Sports Med 2016")


def programa_710():
    """7.10: quatro ingredientes em fila; o equilíbrio aberto nas suas quatro etapas."""
    p = [svg_abre(1664, 400, "Quatro ingredientes do programa, por semanas. Amplitude, principalmente a flexão do tornozelo para a frente. Força de panturrilha e estabilizadores do pé. Equilíbrio progressivo, em quatro etapas: parado, superfície instável, olhos fechados, com perturbação. E o gesto: salto, mudança de direção, aterrissagem"), defs(MUDO)]
    rs = []
    ing = [("t:ruler-measure", "Amplitude", "principalmente a flexão do tornozelo para a frente", OXID), ("t:barbell", "Força", "panturrilha e estabilizadores do pé", OXID),
           ("t:yoga", "Equilíbrio progressivo", "", GLIC), ("t:ball-football", "O gesto", "salto, mudança de direção, aterrissagem", TINTA)]
    for k, (ic, t, d, cor) in enumerate(ing):
        x = k * 424
        p.append(caixa(x, 0, 392, 400, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 50, cor))
        rs.append(rot(x + 84, 30, t, w=300, tam=25, cor=cor, peso=700, serif=True, lh=1.15))
        if d:
            rs.append(rot(x + 22, 120, d, w=350, tam=22, cor=TINTA, lh=1.3))
        if k < 3:
            p.append(seta(x + 394, 200, x + 420, 200, MUDO, "m0", esp=3))
    for j, t in enumerate(["parado", "superfície instável", "olhos fechados", "com perturbação"]):
        y = 110 + j * 68
        p.append(f'<rect x="{848 + 22 + j * 12}" y="{y}" width="{340 - j * 12}" height="56" rx="28" fill="{GLIC}" opacity="{0.35 + j * 0.2:.2f}"/>')
        rs.append(rot(848 + 22 + j * 12, y + 15, t, w=340 - j * 12, tam=20, cor=TINTA if j < 2 else PAPEL, peso=700, alinha="center"))
    return slide("programa", 400, p, rs, eyebrow="O que reduz a recidiva", titulo="Quatro ingredientes, por semanas",
                 destaque="Em quem já torceu: órtese ou bandagem no período de risco (evidência forte) e treino neuromuscular (moderada).", destaque_cor="tinta",
                 fonte="Br J Sports Med 2017")


def ombro_710():
    """7.10: a dor que acompanha o volume, desenhada em semanas, e o que sai do padrão."""
    p = [svg_abre(1664, 400, "À esquerda, o padrão, em esquema: barras de volume semanal e uma linha de dor que sobe com o volume, cai com a redução e volta quando o volume volta. Dor lateral, acima da cabeça, que começou devagar, sem trauma, e dói ao deitar do lado. À direita, fora do padrão: trauma com perda súbita de força; não eleva o braço ou sensação de luxação; dor noturna intensa e persistente; formigamento para a mão ou dor que não muda")]
    rs = []
    p.append(caixa(0, 0, 860, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "O padrão", w=400, tam=27, cor=OXID, peso=700, serif=True))
    vol = [3, 4, 6, 7, 3, 3, 6, 7]
    dor = [1, 2, 4, 6, 3, 2, 4, 6]
    B = 230
    pts = []
    for i, (v, d) in enumerate(zip(vol, dor)):
        x = 40 + i * 98
        p.append(f'<rect x="{x}" y="{B - v * 18}" width="70" height="{v * 18}" rx="4" fill="{OXID_T}"/>')
        pts.append(f"{x + 35},{B - d * 22}")
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<line x1="30" y1="{B}" x2="830" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(560, 60, "dor", w=100, tam=19, cor=FOSF, peso=700), rot(650, 60, "volume", w=150, tam=19, cor=OXID, peso=700),
           rot(40, B + 6, "semanas · esquema", w=760, tam=16, cor=MUDO),
           rot(24, 280, "dor lateral, acima da cabeça", w=820, tam=21, cor=TINTA, peso=700),
           rot(24, 318, "começou devagar, sem trauma; dói ao deitar do lado", w=820, tam=21, cor=TINTA),
           rot(24, 356, "melhora com redução, volta com o volume", w=820, tam=21, cor=TINTA)]
    p.append(caixa(900, 0, 764, 400, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(924, 16, "Fora do padrão", w=700, tam=27, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["trauma com perda súbita de força", "não eleva o braço; sensação de luxação", "dor noturna intensa e persistente", "formigamento para a mão; dor que não muda"]):
        y = 84 + k * 76
        p.append(icone("t:alert-triangle", 924, y + 2, 38, FOSF))
        rs.append(rot(976, y + 6, t, w=670, tam=22, cor=TINTA, peso=700))
    return slide("ombro", 400, p, rs, eyebrow="Ombro · passo um · reconhecer", titulo="O padrão de quem joga acima da cabeça")


def manguito_710():
    """7.10: o nome antigo riscado, o nome novo e as três leituras."""
    p = [svg_abre(1664, 400, "No alto, a leitura antiga riscada: algo pinçando que precisa ser tirado. Ao lado, o nome novo: dor do ombro relacionada ao manguito rotador. Embaixo, três leituras. Primeira linha: exercício com progressão de carga, por meses, e ajuste do treino. Atleta jovem de arremesso ou natação: instabilidade é parte frequente do quadro. Acima dos quarenta: mais lesão estrutural; exercício segue primeira linha na maioria"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 640, 110, CINZA, PAPEL, esp=2, rx=16))
    rs.append(rot(24, 22, "“algo pinçando que precisa ser tirado”", w=600, tam=24, cor=MUDO, peso=700, lh=1.2))
    p.append(f'<line x1="20" y1="94" x2="620" y2="16" stroke="{FOSF}" stroke-width="5"/>')
    p.append(seta(646, 55, 714, 55, MUDO, "m0", esp=4))
    p.append(caixa(720, 0, 944, 110, OXID, OXID, esp=0, rx=16))
    rs.append(rot(744, 32, "dor do ombro relacionada ao manguito rotador", w=900, tam=28, cor=PAPEL, peso=700, serif=True))
    cards = [("Primeira linha", "exercício com progressão de carga, por meses, e ajuste do treino", OXID), ("Atleta jovem de arremesso ou natação", "instabilidade é parte frequente do quadro", GLIC),
             ("Acima dos quarenta", "mais lesão estrutural; exercício segue primeira linha na maioria", GLIC)]
    for k, (t, d, cor) in enumerate(cards):
        x = k * 564
        p.append(caixa(x, 140, 536, 260, cor, CARTAO, esp=2 if k else 4, rx=16))
        rs += [rot(x + 24, 160, t, w=490, tam=25, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 24, 256, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("manguito", 400, p, rs, eyebrow="O nome e a leitura que mudaram", titulo="Dor do ombro relacionada ao manguito rotador",
                 fonte="Lewis e colegas, J Orthop Sports Phys Ther 2015")


def frentes_710():
    """7.10: quatro frentes; o ajuste do que produziu o quadro em destaque."""
    p = [svg_abre(1664, 400, "Quatro frentes para o ombro. Exercício progressivo: manguito e escápula, carga que sobe. Ajuste do que produziu, em destaque: sem isso a fisioterapia trata com uma mão e o treino machuca com a outra. Mobilidade e controle: escápula e coluna torácica, quando limitadas. Expectativa combinada: leva meses e oscila")]
    rs = []
    p.append(caixa(0, 0, 700, 400, FOSF, FOSF, esp=0, rx=18))
    p.append(icone("t:adjustments-horizontal", 30, 30, 70, PAPEL))
    rs += [rot(30, 130, "Ajuste do que produziu", w=640, tam=34, cor=PAPEL, peso=700, serif=True),
           rot(30, 200, "sem isso a fisioterapia trata com uma mão e o treino machuca com a outra", w=640, tam=24, cor=PAPEL, lh=1.35)]
    outros = [("t:barbell", "Exercício progressivo", "manguito e escápula, carga que sobe", OXID), ("t:stretching", "Mobilidade e controle", "escápula e coluna torácica, quando limitadas", OXID),
              ("t:calendar", "Expectativa combinada", "leva meses e oscila", TINTA)]
    for k, (ic, t, d, cor) in enumerate(outros):
        y = k * 136
        p.append(caixa(740, y, 924, 122, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, 764, y + 36, 48, cor))
        rs += [rot(830, y + 20, t, w=810, tam=25, cor=cor, peso=700, serif=True), rot(830, y + 66, d, w=810, tam=22, cor=TINTA)]
    return slide("frentes", 400, p, rs, eyebrow="Ombro · o que fazer", titulo="Quatro frentes",
                 destaque="Não fazer: repouso prolongado, infiltração como primeira linha, imagem de rotina em quadro típico.", destaque_cor="verm")


def carga_710():
    """7.10: três modalidades, cada uma com o que olhar na carga."""
    p = [svg_abre(1664, 340, "Três modalidades e o que olhar na carga de cada uma. Natação: metragem semanal, uso de palmar, distribuição entre os estilos. Arremesso: contagem de arremessos e dias de descanso. Academia: volume de empurrar acima da cabeça e proporção entre empurrar e puxar")]
    rs = []
    mods = [("t:swimming", "Natação", ["metragem semanal", "uso de palmar", "distribuição entre os estilos"]), ("t:ball-volleyball", "Arremesso", ["contagem de arremessos", "dias de descanso"]),
            ("t:barbell", "Academia", ["volume de empurrar acima da cabeça", "proporção empurrar e puxar"])]
    for k, (ic, t, itens) in enumerate(mods):
        x = k * 564
        p.append(caixa(x, 0, 536, 340, OXID, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 60}" cy="60" r="38" fill="{OXID_T}"/>')
        p.append(icone(ic, x + 36, 36, 48, OXID))
        rs.append(rot(x + 116, 42, t, w=400, tam=28, cor=OXID, peso=700, serif=True))
        for j, it in enumerate(itens):
            y = 130 + j * 66
            p.append(f'<rect x="{x + 24}" y="{y}" width="488" height="54" rx="27" fill="{OXID_T}"/>')
            rs.append(rot(x + 24, y + 14, it, w=488, tam=21, cor=TINTA, peso=700, alinha="center"))
    return slide("carga", 340, p, rs, eyebrow="O ajuste de carga", titulo="Esporte por esporte",
                 destaque="Em todos: o que mudou nas semanas antes da dor?", destaque_cor="tinta")

# ---------------------------------------------------------------- 7.11

def dedo_711():
    """7.11: a dor mostrada com a mão inteira e a dor apontada com um dedo, cada uma com seu caminho."""
    p = [svg_abre(1664, 340, "Dois gestos, dois caminhos. A dor mostrada com a mão inteira: difusa, melhora depois que aquece. A dor apontada com a ponta de um dedo: num ponto do osso, depois de aumento de carga, piora conforme a corrida avança, passa a doer até andando; é o caminho da lesão óssea por estresse")]
    rs = []
    for k, (ic, t, itens, cor, fundo) in enumerate([("t:hand-stop", "Com a mão inteira", ["difusa", "melhora depois que aquece"], OXID, OXID_T),
                                                     ("t:target", "Com a ponta de um dedo", ["num ponto do osso", "depois de aumento de carga", "piora conforme a corrida avança", "passa a doer até andando"], FOSF, FOSF_T)]):
        x = k * 852
        p.append(caixa(x, 0, 812, 340, cor, CARTAO, esp=2 if k == 0 else 4, rx=16))
        p.append(f'<circle cx="{x + 130}" cy="170" r="{100 if k == 0 else 26}" fill="{fundo}" stroke="{cor}" stroke-width="{2 if k == 0 else 4}"/>')
        if k == 1:
            p.append(f'<circle cx="{x + 130}" cy="170" r="10" fill="{FOSF}"/>')
        if k == 0:
            p.append(icone(ic, x + 100, 30, 60, cor))
        rs.append(rot(x + 270, 24, t, w=520, tam=28, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            y = 90 + j * 56
            p.append(f'<circle cx="{x + 282}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(x + 302, y, it, w=490, tam=23, cor=TINTA, peso=700 if k else 400))
    rs.append(rot(852 + 270, 300, "lesão óssea por estresse", w=520, tam=22, cor=FOSF, peso=700))
    return slide("dedo", 340, p, rs, eyebrow="O gesto que muda a conversa", titulo="A dor apontada com a ponta de um dedo.",
                 destaque="Começa pequena, dá para correr com ela, até o dia em que não dá mais.", destaque_cor="verm")


def balanca_711():
    """7.11: uma balança pendendo para o dano; de um lado a carga que subiu, do outro o reparo que caiu."""
    p = [svg_abre(1664, 400, "Uma balança entre dano e reparo, pendendo para o dano. Do lado do dano, a carga subiu demais: aumento de volume, mudança de superfície, volta de férias num esporte de impacto. Do lado do reparo, o reparo caiu: energia disponível baixa; hormônios, vitamina D, cálcio; sono curto")]
    rs = []
    cx = 832
    p.append(f'<path d="M {cx - 40} 230 L {cx} 110 L {cx + 40} 230 Z" fill="{TINTA}"/>')
    p.append(f'<line x1="{cx - 330}" y1="150" x2="{cx + 330}" y2="70" stroke="{TINTA}" stroke-width="7" stroke-linecap="round"/>')
    for sx, sy, t, cor in [(cx - 330, 150, "dano", FOSF), (cx + 330, 70, "reparo", OXID)]:
        p.append(f'<line x1="{sx}" y1="{sy}" x2="{sx - 70}" y2="{sy + 60}" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<line x1="{sx}" y1="{sy}" x2="{sx + 70}" y2="{sy + 60}" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<path d="M {sx - 90} {sy + 60} H {sx + 90} Q {sx} {sy + 140} {sx - 90} {sy + 60} Z" fill="{cor}"/>')
        rs.append(rot(sx - 90, sy + 66, t, w=180, tam=20, cor=PAPEL, peso=700, alinha="center"))
    for k, (t, itens, cor, x) in enumerate([("A carga subiu demais", ["aumento de volume", "mudança de superfície", "volta de férias num esporte de impacto"], GLIC, 0),
                                            ("O reparo caiu", ["energia disponível baixa", "hormônios, vitamina D, cálcio", "sono curto"], FOSF, 1144)]):
        p.append(caixa(x, 262, 520, 138, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(x + 20, 272, t, w=480, tam=23, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            rs.append(rot(x + 20, 308 + j * 30, "· " + it, w=480, tam=20, cor=TINTA, peso=700 if (k == 1 and j == 0) else 400))
    return slide("balanca", 400, p, rs, eyebrow="A fisiologia em trinta segundos", titulo="Dano mais rápido que reparo",
                 destaque="Tirar o impacto e esperar resolve o episódio e deixa a causa de pé.", destaque_cor="tinta")


def reconhecer_711():
    """7.11: quatro elementos do padrão e, embaixo, os dois sinais de beira de quadra que pedem encaminhamento."""
    p = [svg_abre(1664, 400, "Quatro elementos do padrão, em fila: localizada, apontada com o dedo; depois de mudança de carga nas últimas semanas; piora com a atividade, não melhora com o aquecimento e segue depois de parar; progride até doer andando ou em repouso. Embaixo, os dois sinais de beira de quadra: dor à percussão do osso, ou ao saltitar num pé só, num ponto. Encaminhar"), defs(MUDO)]
    rs = []
    els = [("t:target", "Localizada", "apontada com o dedo", FOSF), ("t:trending-up", "Depois de mudança de carga", "nas últimas semanas", GLIC),
           ("t:run", "Piora com a atividade", "não melhora com o aquecimento; segue depois de parar", FOSF), ("t:walk", "Progride", "até doer andando ou em repouso", FOSF)]
    for k, (ic, t, d, cor) in enumerate(els):
        x = k * 424
        p.append(caixa(x, 0, 392, 240, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 46, cor))
        rs += [rot(x + 82, 26, t, w=300, tam=23, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 22, 120, d, w=350, tam=21, cor=TINTA, lh=1.3)]
        if k < 3:
            p.append(seta(x + 394, 120, x + 420, 120, MUDO, "m0", esp=3))
    p.append(caixa(0, 270, 1664, 130, FOSF, FOSF_T, esp=2, rx=16))
    for k, (ic, t) in enumerate([("t:hand-stop", "dor à percussão do osso"), ("t:stairs", "dor ao saltitar num pé só, num ponto")]):
        x = 24 + k * 560
        p.append(icone(ic, x, 312, 44, FOSF))
        rs.append(rot(x + 56, 318, t, w=490, tam=23, cor=TINTA, peso=700))
    p.append(caixa(1160, 290, 480, 90, FOSF, FOSF, esp=0, rx=45))
    rs.append(rot(1160, 316, "encaminhar", w=480, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("reconhecer", 400, p, rs, eyebrow="Sem exame", titulo="O padrão que qualquer um da equipe reconhece")


def diferencial_711():
    """7.11: duas canelas: uma com um ponto, outra com uma faixa ao longo da borda interna."""
    p = [svg_abre(1664, 400, "Duas canelas desenhadas. Na lesão óssea por estresse, a dor é um ponto, piora com a atividade e progride ao longo dos dias. No estresse tibial medial, a dor ocupa vários centímetros da borda interna, aparece no começo e melhora aquecido; manejo parecido, prazo menor")]
    rs = []
    for k, (t, itens, cor, fundo) in enumerate([("Lesão óssea por estresse", ["um ponto", "piora com a atividade", "progride ao longo dos dias"], FOSF, FOSF_T),
                                                 ("Estresse tibial medial", ["vários centímetros na borda interna", "aparece no começo, melhora aquecido", "manejo parecido, prazo menor"], GLIC, GLIC_T)]):
        x = k * 852
        p.append(caixa(x, 0, 812, 400, cor, CARTAO, esp=2, rx=16))
        rs.append(rot(x + 300, 22, t, w=490, tam=27, cor=cor, peso=700, serif=True))
        p.append(f'<path d="M {x + 110} 30 C {x + 100} 150, {x + 110} 280, {x + 120} 370 L {x + 200} 370 C {x + 205} 280, {x + 215} 150, {x + 210} 30 Z" fill="{PAPEL}" stroke="{MUDO}" stroke-width="3"/>')
        if k == 0:
            p.append(f'<circle cx="{x + 150}" cy="190" r="18" fill="{FOSF}"/>')
            p.append(f'<circle cx="{x + 150}" cy="190" r="34" fill="none" stroke="{FOSF}" stroke-width="2" opacity="0.6"/>')
        else:
            p.append(f'<rect x="{x + 108}" y="150" width="26" height="170" rx="13" fill="{GLIC}" opacity="0.85"/>')
        for j, it in enumerate(itens):
            y = 110 + j * 70
            p.append(f'<circle cx="{x + 312}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(x + 332, y, it, w=460, tam=23, cor=TINTA, lh=1.25))
    return slide("diferencial", 400, p, rs, eyebrow="O que parece e é mais brando", titulo="Lesão óssea ou estresse tibial medial",
                 destaque="A avaliação médica decide. O que não pode é tratar dor localizada e progressiva como dor muscular.", destaque_cor="tinta")


def risco_711():
    """7.11: o esqueleto do membro inferior com pontos de alto risco em vermelho e de baixo risco em verde."""
    p = [svg_abre(1664, 420, "Um desenho do esqueleto do membro inferior com pontos marcados. Em vermelho, os sítios de alto risco: colo do fêmur, do lado da tensão; borda anterior da tíbia; maléolo medial; navicular; base do quinto metatarso. Em verde, os de baixo risco: face posteromedial da tíbia; fíbula; maior parte dos metatarsos. Identificada cedo, uma lesão de baixo risco costuma ter caminho tranquilo")]
    rs = []
    o = MUDO
    p.append(f'<circle cx="150" cy="40" r="26" fill="{PAPEL}" stroke="{o}" stroke-width="4"/>')
    p.append(f'<path d="M 170 52 L 210 80 L 228 200" fill="none" stroke="{o}" stroke-width="16" stroke-linecap="round"/>')
    p.append(f'<path d="M 222 220 L 226 350" fill="none" stroke="{o}" stroke-width="16" stroke-linecap="round"/>')
    p.append(f'<path d="M 256 226 L 258 348" fill="none" stroke="{o}" stroke-width="7" stroke-linecap="round"/>')
    p.append(f'<path d="M 200 372 L 230 360 L 300 372 L 400 392 L 400 404 L 190 404 Z" fill="{PAPEL}" stroke="{o}" stroke-width="3"/>')
    alto = [(186, 66), (232, 280), (214, 352), (280, 372), (360, 396)]
    baixo = [(212, 300), (258, 300), (340, 386)]
    for cx, cy in alto:
        p.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{FOSF}" stroke="{PAPEL}" stroke-width="3"/>')
    for cx, cy in baixo:
        p.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{OXID}" stroke="{PAPEL}" stroke-width="3"/>')
    for k, (t, itens, cor, fundo, x) in enumerate([("Alto risco", ["colo do fêmur, lado da tensão", "borda anterior da tíbia", "maléolo medial", "navicular; base do quinto metatarso"], FOSF, FOSF_T, 480),
                                                    ("Baixo risco", ["face posteromedial da tíbia", "fíbula", "maior parte dos metatarsos", "pega cedo: caminho tranquilo"], OXID, OXID_T, 1084)]):
        p.append(caixa(x, 0, 580, 420, cor, fundo, esp=2 if k else 4, rx=16))
        p.append(f'<circle cx="{x + 40}" cy="40" r="14" fill="{cor}"/>')
        rs.append(rot(x + 66, 22, t, w=490, tam=28, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            y = 100 + j * 76
            p.append(f'<rect x="{x + 22}" y="{y}" width="536" height="62" rx="12" fill="{CARTAO}"/>')
            rs.append(rot(x + 40, y + 17, it, w=510, tam=22, cor=TINTA, peso=700 if j < 3 or k == 0 else 400))
    return slide("risco", 420, p, rs, eyebrow="A divisão que decide a urgência", titulo="Sítios de alto e de baixo risco",
                 destaque="Tensão e irrigação pobre consolidam pior e podem evoluir para fratura completa.", destaque_cor="tinta",
                 fonte="Warden e colegas, J Orthop Sports Phys Ther 2014")


def naoespera_711():
    """7.11: três lugares marcados, cada um com um alarme: não esperam duas semanas."""
    p = [svg_abre(1664, 320, "Três lugares de dor que não esperam duas semanas para ver se melhora: a virilha ou a frente da coxa no corredor; o meio do pé; a frente da canela, apontada com o dedo. Os três são encaminhamento imediato")]
    rs = []
    for k, (ic, t) in enumerate([("h:running", "virilha ou frente da coxa, no corredor"), ("t:walk", "meio do pé"), ("t:target", "frente da canela, apontada com o dedo")]):
        x = k * 564
        p.append(caixa(x, 0, 536, 210, FOSF, FOSF_T, esp=3, rx=16))
        p.append(icone(ic, x + 24, 24, 56, FOSF))
        p.append(icone("t:alarm", x + 450, 24, 56, FOSF))
        rs.append(rot(x + 24, 110, t, w=490, tam=25, cor=TINTA, peso=700, lh=1.25))
    p.append(caixa(0, 240, 1664, 80, FOSF, FOSF, esp=0, rx=40))
    p.append(icone("t:calendar", 30, 258, 44, PAPEL))
    rs.append(rot(90, 262, "não esperam duas semanas: encaminhamento imediato", w=1540, tam=26, cor=PAPEL, peso=700, serif=True))
    return slide("naoespera", 320, p, rs, eyebrow="Encaminhamento imediato", titulo="Virilha no corredor, meio do pé, frente da canela: não esperam duas semanas.",
                 destaque="A diferença entre um desfecho tranquilo e meses fora, muitas vezes, é o tempo que alguém levou para levar a queixa a sério.", destaque_cor="tinta")


def energia_711():
    """7.11: barras de 37% e 40%, e a taxa de lesão óssea 4,5 vezes maior nesses grupos."""
    p = [svg_abre(1664, 360, "Atletas de elite de fundo e meio-fundo. Barras: 37% das mulheres com amenorreia; 40% dos homens com testosterona baixa. Nesses grupos, a taxa de lesão óssea foi cerca de 4,5 vezes maior que a dos colegas com função normal: uma barra curta de referência e outra quatro vezes e meia mais longa")]
    rs = []
    X0, E = 340, 10
    for k, (ic, v, t) in enumerate([("h:woman", 37, "mulheres com amenorreia"), ("h:man", 40, "homens com testosterona baixa")]):
        y = k * 100
        p.append(icone(ic, 0, y + 6, 64, GLIC))
        rs.append(rot(72, y + 22, t, w=260, tam=21, cor=TINTA, peso=700, lh=1.2))
        p.append(f'<rect x="{X0}" y="{y + 10}" width="{100 * E}" height="60" rx="8" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
        p.append(f'<rect x="{X0}" y="{y + 10}" width="{v * E}" height="60" rx="8" fill="{GLIC}"/>')
        rs.append(rot(X0 + 16, y + 20, f"{v}%", w=200, tam=32, cor=PAPEL, peso=700, serif=True))
    rs.append(rot(0, 214, "taxa de lesão óssea", w=330, tam=21, cor=TINTA, peso=700))
    p.append(f'<rect x="{X0}" y="250" width="{int(1.0 * 200)}" height="40" rx="6" fill="{OXID}"/>')
    p.append(f'<rect x="{X0}" y="300" width="{int(4.5 * 200)}" height="40" rx="6" fill="{FOSF}"/>')
    rs += [rot(0, 256, "função normal", w=330, tam=19, cor=OXID, peso=700), rot(0, 306, "nesses grupos", w=330, tam=19, cor=FOSF, peso=700),
           rot(X0 + 900 + 16, 296, "× 4,5", w=260, tam=40, cor=FOSF, peso=700, serif=True)]
    return slide("energia", 360, p, rs, eyebrow="A raiz energética · atletas de elite de fundo e meio-fundo", titulo="Quando o corpo economiza, o osso paga",
                 destaque="Baixa disponibilidade de energia é difícil de medir, mas as consequências pesam nas lesões ósseas.", destaque_cor="verm",
                 fonte="Int J Sport Nutr Exerc Metab 2018")


def detalhes_711():
    """7.11: dois cartões: homem e mulher lado a lado; o praticante comum com as três armadilhas."""
    p = [svg_abre(1664, 340, "Dois detalhes. Inclui homens: o problema ficou conhecido no esporte feminino e deixou de ser procurado no homem. Não é só elite: no praticante comum, dieta da moda, jejum com treino e a ideia de que emagrecer é sempre bom")]
    rs = []
    p.append(caixa(0, 0, 812, 340, GLIC, CARTAO, esp=2, rx=16))
    p.append(icone("h:woman", 30, 30, 80, MUDO))
    p.append(icone("h:man", 120, 30, 80, GLIC))
    rs += [rot(230, 44, "Inclui homens", w=560, tam=30, cor=GLIC, peso=700, serif=True),
           rot(30, 150, "o problema ficou conhecido no esporte feminino e deixou de ser procurado no homem", w=750, tam=24, cor=TINTA, lh=1.35)]
    p.append(caixa(852, 0, 812, 340, FOSF, CARTAO, esp=2, rx=16))
    p.append(icone("h:person", 882, 30, 80, FOSF))
    rs.append(rot(982, 44, "Não é só elite", w=660, tam=30, cor=FOSF, peso=700, serif=True))
    for j, t in enumerate(["dieta da moda", "jejum com treino", "“emagrecer é sempre bom”"]):
        y = 140 + j * 64
        p.append(f'<rect x="882" y="{y}" width="752" height="52" rx="26" fill="{FOSF_T}"/>')
        rs.append(rot(882, y + 13, t, w=752, tam=22, cor=TINTA, peso=700, alinha="center"))
    return slide("detalhes", 340, p, rs, eyebrow="Dois detalhes desses números", titulo="Não é só elite, e não é só mulher",
                 destaque="Deficiência relativa de energia no esporte: consenso do COI de 2023, tratado no módulo de nutrição.", destaque_cor="tinta", fonte="Br J Sports Med 2023")


def perguntas_711():
    """7.11: quatro perguntas obrigatórias, cada uma com seu ícone, nenhuma sobre osso."""
    p = [svg_abre(1664, 320, "Quatro perguntas obrigatórias, nenhuma sobre osso. Alimentação, e perda de peso recente. Ciclo menstrual: ausência ou irregularidade é sinal. Fraturas antes: outras lesões por estresse. Sono: quanto e como")]
    rs = []
    itens = [("t:salad", "Alimentação", "e perda de peso recente", GLIC), ("t:calendar", "Ciclo menstrual", "ausência ou irregularidade é sinal", FOSF),
             ("t:refresh", "Fraturas antes", "outras lesões por estresse", GLIC), ("t:moon", "Sono", "quanto e como", OXID)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 0, 392, 320, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 196}" cy="80" r="52" fill="{FOSF_T if cor == FOSF else GLIC_T if cor == GLIC else OXID_T}"/>')
        p.append(icone(ic, x + 166, 50, 60, cor))
        p.append(f'<circle cx="{x + 34}" cy="34" r="18" fill="{cor}"/>')
        rs += [rot(x + 16, 22, "?", w=36, tam=22, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 20, 156, t, w=352, tam=27, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 20, 210, d, w=352, tam=22, cor=TINTA, alinha="center", lh=1.3)]
    return slide("perguntas", 320, p, rs, eyebrow="Sempre, e nenhuma é sobre osso", titulo="Quatro perguntas obrigatórias",
                 destaque="É a diferença entre tratar o episódio e resolver o problema.", destaque_cor="tinta")


def volta_711():
    """7.11: três faixas de prazo de comprimento crescente e, embaixo, o que fazer durante o afastamento."""
    p = [svg_abre(1664, 400, "Três faixas de prazo, em esquema, sem valores: baixo risco pego cedo, semanas até a volta progressiva ao impacto, a mais curta; fratura estabelecida, mais tempo; alto risco, muito mais, às vezes com imobilização ou cirurgia, a mais longa. Embaixo, durante o afastamento: bicicleta, piscina, remo e força, que preservam capacidade e cabeça")]
    rs = []
    faixas = [("Baixo risco, pego cedo", "semanas até a volta progressiva ao impacto", 600, OXID), ("Fratura estabelecida", "mais tempo", 880, GLIC),
              ("Alto risco", "muito mais; às vezes imobilização ou cirurgia", 1220, FOSF)]
    for k, (t, d, w, cor) in enumerate(faixas):
        y = k * 76
        rs.append(rot(0, y + 18, t, w=380, tam=22, cor=cor, peso=700, alinha="right"))
        p.append(f'<rect x="400" y="{y}" width="{w}" height="62" rx="31" fill="{cor}"/>')
        rs.append(rot(424, y + 18, d, w=w - 40, tam=20, cor=PAPEL, peso=700))
    rs.append(rot(400, 230, "faixas, não datas · esquema, sem valores", w=1200, tam=17, cor=MUDO))
    p.append(caixa(0, 270, 1664, 130, TINTA, AZUL_T, esp=2, rx=16))
    rs.append(rot(24, 282, "durante o afastamento do impacto", w=600, tam=21, cor=TINTA, peso=700))
    for j, (ic, t) in enumerate([("t:bike", "bicicleta"), ("t:swimming", "piscina"), ("t:refresh", "remo"), ("t:barbell", "força")]):
        x = 24 + j * 260
        p.append(icone(ic, x, 326, 44, AZUL))
        rs.append(rot(x + 54, 334, t, w=190, tam=22, cor=TINTA, peso=700))
    rs.append(rot(1080, 318, "preserva capacidade e cabeça", w=560, tam=24, cor=AZUL, peso=700, serif=True))
    return slide("volta", 400, p, rs, eyebrow="Prazo e volta", titulo="Faixas, não datas")


def recidiva_711():
    """7.11: a primeira lesão, a volta com as mesmas três coisas, e a segunda lesão."""
    p = [svg_abre(1664, 320, "A primeira lesão, uma volta com as mesmas três coisas, e a segunda lesão. A mesma alimentação, a mesma ausência de ciclo, a mesma progressão que produziram a primeira"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 80, 300, 160, FOSF, FOSF, esp=0, rx=16))
    rs.append(rot(0, 140, "primeira lesão", w=300, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True))
    p.append(seta(304, 160, 370, 160, MUDO, "m0", esp=4))
    rs.append(rot(380, 0, "voltou com", w=900, tam=22, cor=TINTA, peso=700, alinha="center"))
    for j, t in enumerate(["a mesma alimentação", "a mesma ausência de ciclo", "a mesma progressão"]):
        y = 44 + j * 92
        p.append(caixa(380, y, 900, 78, GLIC, GLIC_T, esp=2, rx=39))
        p.append(icone("t:repeat", 404, y + 19, 40, GLIC))
        rs.append(rot(460, y + 24, t, w=800, tam=24, cor=TINTA, peso=700))
    p.append(seta(1284, 160, 1350, 160, MUDO, "m0", esp=4))
    p.append(caixa(1364, 80, 300, 160, FOSF, FOSF, esp=0, rx=16))
    rs.append(rot(1364, 140, "segunda lesão", w=300, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("recidiva", 320, p, rs, eyebrow="A parte que evita a recidiva", titulo="Sem corrigir a causa energética, o retorno é frágil.")

# ---------------------------------------------------------------- 7.12

def caso_712():
    """7.12: a corredora, o laudo com três achados e as duas perguntas."""
    p = [svg_abre(1664, 360, "Caso ilustrativo. Uma corredora na casa dos quarenta, três vezes por semana, com dor no joelho há três semanas, desde que aumentou o ritmo. Ela chega com a ressonância. O laudo: lesão horizontal do menisco medial, condropatia patelar grau dois, edema ósseo subcondral. E duas perguntas: vou ter que operar? Vou poder voltar a correr?")]
    rs = []
    p.append(caixa(0, 0, 440, 360, OXID, CARTAO, esp=2, rx=16))
    p.append(icone("h:woman", 24, 24, 72, OXID))
    rs += [rot(110, 34, "casa dos quarenta", w=310, tam=24, cor=OXID, peso=700), rot(110, 72, "corre três vezes por semana", w=310, tam=20, cor=TINTA),
           rot(24, 150, "dor no joelho há três semanas, desde que aumentou o ritmo", w=392, tam=23, cor=TINTA, peso=700, lh=1.3)]
    X = 480
    p.append(f'<path d="M {X} 0 H {X + 620} L {X + 680} 60 V 360 H {X} Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
    p.append(icone("t:clipboard-list", X + 24, 20, 44, TINTA))
    rs.append(rot(X + 80, 30, "laudo de ressonância", w=500, tam=22, cor=TINTA, peso=700))
    for j, t in enumerate(["lesão horizontal do menisco medial", "condropatia patelar grau dois", "edema ósseo subcondral"]):
        y = 104 + j * 78
        p.append(f'<rect x="{X + 24}" y="{y}" width="632" height="62" rx="10" fill="{FOSF_T}"/>')
        rs.append(rot(X + 44, y + 18, t, w=600, tam=22, cor=FOSF, peso=700))
    for k, q in enumerate(["“Vou ter que operar?”", "“Vou poder voltar a correr?”"]):
        y = 30 + k * 170
        p.append(f'<path d="M 1200 {y} H 1644 Q 1664 {y} 1664 {y + 20} V {y + 110} Q 1664 {y + 130} 1644 {y + 130} H 1230 L 1190 {y + 150} L 1206 {y + 130} H 1220 Q 1200 {y + 130} 1200 {y + 110} Z" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
        rs.append(rot(1220, y + 44, q, w=420, tam=25, cor=TINTA, peso=700, serif=True))
    return slide("caso", 360, p, rs, eyebrow="Caso ilustrativo", titulo="Corredora na casa dos quarenta, dor no joelho há três semanas, ressonância na mão.")


def mesa_712():
    """7.12: a dor pequena num canto e o laudo ocupando o centro da mesa."""
    p = [svg_abre(1664, 360, "Uma mesa vista de cima. Num canto, pequena, a dor: três semanas, começou quando o ritmo subiu, é o que ela veio resolver. No centro, grande, o laudo: três achados que ocuparam a conversa; agora o assunto é o menisco"), defs(MUDO)]
    rs = []
    p.append(f'<rect x="0" y="0" width="1664" height="360" rx="24" fill="{GLIC_T}"/>')
    p.append(caixa(40, 90, 380, 220, OXID, CARTAO, esp=2, rx=14))
    rs += [rot(60, 106, "A dor", w=340, tam=25, cor=OXID, peso=700, serif=True)]
    for j, t in enumerate(["três semanas", "começou quando o ritmo subiu", "é o que ela veio resolver"]):
        rs.append(rot(60, 156 + j * 44, "· " + t, w=350, tam=19, cor=TINTA, peso=700 if j == 2 else 400))
    p.append(seta(430, 200, 560, 200, MUDO, "m0", esp=3))
    rs.append(rot(424, 160, "saiu do centro", w=140, tam=16, cor=MUDO, alinha="center"))
    p.append(f'<path d="M 580 20 H 1560 L 1624 84 V 340 H 580 Z" fill="{CARTAO}" stroke="{FOSF}" stroke-width="4"/>')
    p.append(icone("t:clipboard-list", 610, 44, 64, FOSF))
    rs += [rot(690, 52, "O laudo", w=600, tam=34, cor=FOSF, peso=700, serif=True)]
    for j, t in enumerate(["três achados", "ocupou o centro da conversa", "agora o assunto é o menisco"]):
        rs.append(rot(610, 140 + j * 60, "· " + t, w=980, tam=27, cor=TINTA, peso=700 if j == 2 else 400))
    return slide("mesa", 360, p, rs, eyebrow="O que aconteceu naquela mesa", titulo="O papel virou o assunto",
                 destaque="O problema quase nunca é o exame. É o que a gente faz com ele.", destaque_cor="tinta")


def joelhos_712():
    """7.12: quatro barras de 0 a 100% em joelhos sem dor."""
    p = [svg_abre(1664, 380, "Barras numa escala de zero a cem por cento, em 230 joelhos de adultos sem dor e sem lesão. Alguma alteração: 97%. Alteração de cartilagem femoropatelar: 57%. Alteração de medula óssea femoropatelar: 48%. Lesão de menisco, a maioria horizontal: 30%")]
    rs = []
    X0, E = 470, 10.5
    itens = [("com alguma alteração", 97, TINTA), ("cartilagem femoropatelar", 57, GLIC), ("medula óssea femoropatelar", 48, GLIC), ("menisco, a maioria horizontal", 30, FOSF)]
    for k, (t, v, cor) in enumerate(itens):
        y = k * 82
        rs.append(rot(0, y + 20, t, w=440, tam=22, cor=TINTA, peso=700, alinha="right"))
        p.append(f'<rect x="{X0}" y="{y}" width="{100 * E:.0f}" height="66" rx="8" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E:.0f}" height="66" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + 16, y + 12, f"{v}%", w=200, tam=34, cor=PAPEL, peso=700, serif=True))
    rs.append(rot(X0, 340, "dos 230 joelhos, de 115 adultos sedentários sem queixa", w=1100, tam=19, cor=MUDO))
    return slide("joelhos", 380, p, rs, eyebrow="Erro um · achar que a imagem diagnostica", titulo="230 joelhos de adultos sem dor, sem lesão",
                 destaque="Mediana de 44 anos. Ninguém sentia dor.", destaque_cor="verm", fonte="Skeletal Radiol 2020")


def dez_712():
    """7.12: dez pessoas a partir dos quarenta; quase todas com achado, três com menisco."""
    p = [svg_abre(1664, 320, "Dez pessoas quaisquer a partir dos quarenta. Quase todas têm alguma marca de achado no laudo; três delas têm menisco. O menisco já estava lá antes da dor, e vai continuar lá depois")]
    rs = []
    for i in range(10):
        x = 20 + i * 164
        men = i in (2, 5, 8)
        p.append(icone("h:person", x, 30, 120, FOSF if men else MUDO))
        if i != 6:
            p.append(f'<circle cx="{x + 100}" cy="44" r="14" fill="{GLIC}" stroke="{PAPEL}" stroke-width="3"/>')
        if men:
            p.append(f'<rect x="{x}" y="170" width="124" height="44" rx="22" fill="{FOSF}"/>')
            rs.append(rot(x, 180, "menisco", w=124, tam=19, cor=PAPEL, peso=700, alinha="center"))
    p.append(f'<circle cx="34" cy="280" r="12" fill="{GLIC}"/>')
    rs += [rot(56, 266, "alguma coisa no laudo: quase todas", w=700, tam=22, cor=TINTA, peso=700),
           rot(820, 266, "menisco: três em dez", w=700, tam=22, cor=FOSF, peso=700)]
    return slide("dez", 320, p, rs, eyebrow="Na prática", titulo="O menisco já estava lá antes da dor, e vai continuar lá depois.",
                 destaque="Menisco pode doer, mas a presença do achado não prova que ele é a causa.", destaque_cor="verm")


def territorios_712():
    """7.12: quatro regiões, cada uma com barras do que a imagem mostra em gente sem dor."""
    p = [svg_abre(1664, 420, "O mesmo padrão no corpo inteiro, em gente sem dor, em barras de zero a cem por cento. Ombro: rotura do manguito em 34%, completa em 15%. Quadril: alguma alteração em 73%, lesão do lábio em 69%. Coluna: degeneração de disco em 37% aos 20 anos, 96% aos 80. Joelho: sinais de artrose em 4 a 14% abaixo dos 40, 19 a 43% acima")]
    rs = []
    X0, E = 330, 9.6
    regs = [("Ombro", [(0, 34, "rotura do manguito 34%"), (0, 15, "completa 15%")]),
            ("Quadril", [(0, 73, "alguma alteração 73%"), (0, 69, "lábio 69%")]),
            ("Coluna", [(0, 37, "disco aos 20 anos: 37%"), (0, 96, "aos 80: 96%")]),
            ("Joelho", [(4, 14, "artrose abaixo dos 40: 4 a 14%"), (19, 43, "acima dos 40: 19 a 43%")])]
    for k, (t, barras) in enumerate(regs):
        y = k * 104
        p.append(caixa(0, y, 300, 92, TINTA, CARTAO, esp=2, rx=14))
        rs.append(rot(0, y + 28, t, w=300, tam=27, cor=TINTA, peso=700, alinha="center", serif=True))
        for j, (a, b, lab) in enumerate(barras):
            yy = y + 4 + j * 46
            p.append(f'<rect x="{X0}" y="{yy}" width="{100 * E:.0f}" height="38" rx="6" fill="{PAPEL}" stroke="{BORDA}" stroke-width="1"/>')
            p.append(f'<rect x="{X0 + a * E:.0f}" y="{yy}" width="{(b - a) * E:.0f}" height="38" rx="6" fill="{GLIC if j == 0 else FOSF}" opacity="{1 if a == 0 else 0.85}"/>')
            rs.append(rot(X0 + max(b, 0) * E + 12 if b < 60 else X0 + 12, yy + 8, lab, w=420, tam=18, cor=TINTA if b < 60 else PAPEL, peso=700))
    return slide("territorios", 420, p, rs, eyebrow="Erro dois · achar que o joelho é exceção", titulo="O mesmo padrão no corpo inteiro, em gente sem dor",
                 destaque="Não é doença: é o tecido ao longo do tempo, como cabelo branco. Ninguém faz ressonância do cabelo.", destaque_cor="tinta",
                 fonte="J Bone Joint Surg Am 1995 · Am J Sports Med 2012 · AJNR 2015 · Br J Sports Med 2019")


def perguntas_712():
    """7.12: três perguntas em fila, como portões, antes de qualquer exame."""
    p = [svg_abre(1664, 380, "Três perguntas em fila, como portões antes de qualquer exame. O que eu estou suspeitando? Sem completar quero saber se tem, é ansiedade, não indicação. O resultado muda a conduta? Se faço o mesmo com laudo normal e alterado, não é agora. E o achado que eu não procurei? Ele vai vir; decida antes o que fazer com ele. Só depois dos três portões, o exame"), defs(MUDO)]
    rs = []
    qs = [("O que eu estou suspeitando?", "sem completar “quero saber se tem”, é ansiedade, não indicação", OXID), ("O resultado muda a conduta?", "se faço o mesmo com laudo normal e alterado, não é agora", GLIC),
          ("E o achado que eu não procurei?", "ele vai vir; decida antes o que fazer com ele", FOSF)]
    for k, (t, d, cor) in enumerate(qs):
        x = k * 440
        p.append(caixa(x, 0, 408, 380, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 46}" cy="46" r="24" fill="{cor}"/>')
        p.append(icone("t:lock-open", x + 340, 24, 44, cor))
        rs += [rot(x + 22, 32, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 24, 100, t, w=360, tam=26, cor=cor, peso=700, serif=True, lh=1.2), rot(x + 24, 230, d, w=360, tam=22, cor=TINTA, lh=1.3)]
        p.append(seta(x + 410, 190, x + 436, 190, MUDO, "m0", esp=3))
    p.append(caixa(1320, 120, 344, 140, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:eye", 1340, 166, 48, PAPEL))
    rs.append(rot(1400, 172, "aí, o exame", w=250, tam=26, cor=PAPEL, peso=700, serif=True))
    return slide("perguntas", 380, p, rs, eyebrow="Erro três · pedir sem pergunta", titulo="Três perguntas antes de qualquer exame",
                 destaque="Auditoria de um mês: anote cada exame pedido e se mudou a conduta.", destaque_cor="tinta")


def palavras_712():
    """7.12: quatro palavras do laudo pesando sobre uma pessoa pequena."""
    p = [svg_abre(1664, 360, "Quatro palavras do laudo, grandes, pesando sobre uma pessoa pequena embaixo. Degeneração, lida como fim. Rotura, lida como algo partido. Lesão, lida como dano novo. Desgaste, lido como prazo de validade")]
    rs = []
    pal = [("Degeneração", "lida como fim"), ("Rotura", "lida como algo partido"), ("Lesão", "lida como dano novo"), ("Desgaste", "lida como prazo de validade")]
    for k, (t, d) in enumerate(pal):
        x = k * 424
        p.append(caixa(x, 0, 392, 200, FOSF, FOSF_T, esp=2, rx=16))
        rs += [rot(x, 40, t, w=392, tam=36, cor=FOSF, peso=700, alinha="center", serif=True), rot(x, 120, d, w=392, tam=22, cor=TINTA, alinha="center")]
        p.append(f'<line x1="{x + 196}" y1="204" x2="832" y2="268" stroke="{FOSF}" stroke-width="2" opacity="0.5"/>')
    p.append(icone("h:person", 800, 270, 64, TINTA))
    rs.append(rot(880, 296, "quem lê com medo", w=400, tam=20, cor=MUDO, peso=700))
    return slide("palavras", 360, p, rs, eyebrow="Erro quatro · a palavra vira prognóstico", titulo="Feitas para descrever tecido, lidas com medo",
                 destaque="Tem gente que para de correr porque leu “desgaste”. Ninguém mandou parar.", destaque_cor="tinta")


def laudo_712():
    """7.12: o laudo com a frase de prevalência acrescentada, os números do ensaio e o efeito pequeno."""
    p = [svg_abre(1664, 360, "Um laudo de coluna com uma frase a mais: a prevalência do achado em gente sem dor da mesma idade. O ensaio randomizado testou isso em 250.401 adultos, em 98 clínicas de atenção primária. O efeito sobre o que veio depois foi pequeno"), defs(MUDO)]
    rs = []
    p.append(f'<path d="M 0 0 H 560 L 620 60 V 360 H 0 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
    p.append(icone("t:clipboard-list", 24, 20, 44, TINTA))
    rs.append(rot(80, 30, "laudo de coluna", w=440, tam=22, cor=TINTA, peso=700))
    for j in range(3):
        p.append(f'<rect x="24" y="{96 + j * 34}" width="{520 - j * 80}" height="14" rx="7" fill="{CINZA}"/>')
    p.append(f'<rect x="24" y="210" width="572" height="120" rx="12" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(44, 226, "+ prevalência do achado em gente sem dor da mesma idade", w=530, tam=22, cor=OXID, peso=700, lh=1.3))
    nums = [("250.401", "adultos no ensaio randomizado"), ("98", "clínicas de atenção primária")]
    for k, (n, t) in enumerate(nums):
        y = k * 110
        p.append(caixa(680, y, 560, 96, TINTA, CARTAO, esp=2, rx=14))
        rs += [rot(700, y + 20, n, w=240, tam=40, cor=TINTA, peso=700, serif=True), rot(950, y + 32, t, w=280, tam=20, cor=TINTA, lh=1.2)]
    p.append(seta(1244, 100, 1300, 100, MUDO, "m0", esp=3))
    p.append(caixa(1310, 0, 354, 206, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(1310, 30, "efeito", w=354, tam=22, cor=TINTA, alinha="center"), rot(1310, 70, "pequeno", w=354, tam=44, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(1326, 140, "sobre o que veio depois", w=322, tam=20, cor=TINTA, alinha="center")]
    return slide("laudo", 360, p, rs, eyebrow="E se o laudo fosse escrito melhor?", titulo="Prevalência dentro do laudo de coluna",
                 destaque="A frase no papel não substitui a conversa. Quem desarma o laudo é quem está na frente do paciente.", destaque_cor="tinta",
                 fonte="JAMA Netw Open 2020")


def dizer_712():
    """7.12: a segunda metade da frase, em balão, e o que ela é: informação correta."""
    p = [svg_abre(1664, 320, "Um balão de fala com a continuação da frase: o que explica a sua dor é o que mudou no treino nas últimas semanas, e é isso que a gente vai ajustar. Ao lado, uma etiqueta: não é consolo, é informação correta")]
    rs = []
    p.append(f'<path d="M 20 0 H 1100 Q 1120 0 1120 20 V 220 Q 1120 240 1100 240 H 180 L 110 300 L 120 240 H 20 Q 0 240 0 220 V 20 Q 0 0 20 0 Z" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    p.append(icone("t:message-circle", 30, 30, 52, OXID))
    rs.append(rot(100, 40, "“O que explica a sua dor é o que mudou no treino nas últimas semanas, e é isso que a gente vai ajustar.”", w=980, tam=30, cor=TINTA, peso=700, serif=True, lh=1.3))
    p.append(caixa(1180, 40, 484, 160, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1200, 70, "não é consolo:", w=444, tam=26, cor=PAPEL, alinha="center"), rot(1200, 116, "é informação correta", w=444, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True)]
    return slide("dizer", 320, p, rs, eyebrow="Como dizer", titulo="“Essas alterações são comuns na sua idade, e a maioria de quem tem não sente dor.”")


def controle_712():
    """7.12: duas curvas em esquema, tendão e músculo, com a imagem e a função descasadas, e as exceções."""
    p = [svg_abre(1664, 400, "Dois esquemas, sem valores. No tendão, a função volta e a imagem continua alterada. No músculo, a imagem melhora antes da capacidade. O retorno se decide por função. À direita, as exceções em que a imagem de controle tem lugar: lesão óssea em sítio de alto risco; suspeita de complicação; quadro que não segue o esperado")]
    rs = []
    for k, (t, fun, img, lf, li) in enumerate([("Tendão", "40,250 140,200 240,140 340,100 440,80", "40,90 140,92 240,94 340,96 440,95", "função volta", "imagem segue alterada"),
                                              ("Músculo", "40,250 140,230 240,190 340,140 440,90", "40,250 140,140 240,90 340,80 440,78", "capacidade, devagar", "imagem melhora antes")]):
        x = k * 530
        p.append(caixa(x, 0, 510, 330, FOSF, CARTAO, esp=2, rx=16))
        rs.append(rot(x + 24, 14, t, w=400, tam=26, cor=FOSF, peso=700, serif=True))
        p.append(f'<g transform="translate({x + 20},20)"><polyline points="{fun}" fill="none" stroke="{OXID}" stroke-width="5"/><polyline points="{img}" fill="none" stroke="{MUDO}" stroke-width="4"{TRACO}/>'
                 f'<line x1="30" y1="270" x2="460" y2="270" stroke="{MUDO}" stroke-width="2"/></g>')
        rs += [rot(x + 40, 296, lf, w=220, tam=18, cor=OXID, peso=700), rot(x + 260, 296, li, w=230, tam=18, cor=MUDO, peso=700, alinha="right")]
    rs.append(rot(0, 346, "o retorno se decide por função · esquema", w=1040, tam=21, cor=TINTA, peso=700))
    p.append(caixa(1100, 0, 564, 400, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(1124, 18, "Exceções", w=500, tam=27, cor=OXID, peso=700, serif=True))
    for j, t in enumerate(["lesão óssea em sítio de alto risco", "suspeita de complicação", "quadro que não segue o esperado"]):
        y = 96 + j * 96
        p.append(icone("t:check", 1124, y, 40, OXID))
        rs.append(rot(1178, y + 4, t, w=460, tam=23, cor=TINTA, peso=700, lh=1.25))
    return slide("controle", 400, p, rs, eyebrow="Erro cinco · repetir para ver se curou", titulo="A imagem de controle engana nos dois sentidos")


def pedir_712():
    """7.12: seis situações em que pedir imagem é obrigação, em ladrilhos com ícones."""
    p = [svg_abre(1664, 400, "Seis situações em que pedir imagem é obrigação. Trauma: não apoia ou dor óssea localizada, regra de Ottawa. Joelho que incha em horas depois de torção. Osso de alto risco: virilha, frente da tíbia, meio do pé. Bloqueio articular: trava e não completa o movimento. Sinais sistêmicos: dor noturna, febre, perda de peso; déficit neurológico. Tratamento bem feito falhou: a imagem entra na revisão do diagnóstico")]
    rs = []
    itens = [("t:alert-triangle", "Trauma", "não apoia ou dor óssea localizada; regra de Ottawa", FOSF), ("t:droplet", "Joelho que incha em horas", "depois de torção", FOSF),
             ("t:target", "Osso de alto risco", "virilha, frente da tíbia, meio do pé", FOSF), ("t:lock", "Bloqueio articular", "trava e não completa o movimento", GLIC),
             ("t:temperature", "Sinais sistêmicos", "dor noturna, febre, perda de peso; déficit neurológico", GLIC), ("t:zoom-question", "Tratamento bem feito falhou", "a imagem entra na revisão do diagnóstico", OXID)]
    for k, (ic, t, d, cor) in enumerate(itens):
        col, lin = k % 3, k // 3
        x, y = col * 564, lin * 206
        p.append(caixa(x, y, 536, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, y + 22, 48, cor))
        rs += [rot(x + 86, y + 30, t, w=430, tam=24, cor=cor, peso=700, serif=True), rot(x + 24, y + 98, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("pedir", 400, p, rs, eyebrow="O outro lado da balança", titulo="Quando pedir é obrigação")

# ---------------------------------------------------------------- aplicação

LICOES = {"07-01": [numeros_71, usos_71, familias_71, consenso_71, denominador_71, novatos_71, vocabulario_71, oslo_71, leitura_71, rastreio_71],
          "07-02": [cena_72, perguntas_72, definicao_72, exposicao_72, ferramentas_72, indicadores_72, carga_72, devolutiva_72, lgpd_72, painel_72],
          "07-03": [cena_73, mecanismo_73, modelo_73, copo_73, padrao_73, razao_73, colunas_73],
          "07-04": [palavra_74, tamanho_74, mecanismos_74, historia_74, exame_74, imagem_74, advertencias_74, munique_74, britanica_74, conduta_74],
          "07-05": [celular_75, medianas_75, variacao_75, advertencias_75, laudo_75, movem_75, andar_75, naodizer_75, dizer_75],
          "07-06": [cena_76, custo_76, graus_76, imitacoes_76, peace_76, love_76, aine_76, gelo_76, curcuma_76, reabilitacao_76],
          "07-07": [palavra_77, nome_77, rosca_77, imagem_77, exames_77, mudou_77, compressao_77, conduta_77],
          "07-08": [caso_78, tentativas_78, perguntas_78, ajuste_78, regua_78, pesada_78, comparacao_78, falhas_78, plano_78],
          "07-09": [sala_79, femoropatelar_79, mensagens_79, fazer_79, naofazer_79, inchou_79, gramado_79, depois_79, grindem_79, regras_79, prevencao_79],
          "07-10": [abertura_710, ottawa_710, alerta_710, semana_710, alta_710, instabilidade_710, programa_710, ombro_710, manguito_710, frentes_710, carga_710],
          "07-11": [dedo_711, balanca_711, reconhecer_711, diferencial_711, risco_711, naoespera_711, energia_711, detalhes_711, perguntas_711, volta_711, recidiva_711],
          "07-12": [caso_712, mesa_712, joelhos_712, dez_712, territorios_712, perguntas_712, palavras_712, laudo_712, dizer_712, controle_712, pedir_712]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
