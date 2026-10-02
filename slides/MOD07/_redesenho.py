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

# ---------------------------------------------------------------- aplicação

LICOES = {"07-01": [numeros_71, usos_71, familias_71, consenso_71, denominador_71, novatos_71, vocabulario_71, oslo_71, leitura_71, rastreio_71],
          "07-02": [cena_72, perguntas_72, definicao_72, exposicao_72, ferramentas_72, indicadores_72, carga_72, devolutiva_72, lgpd_72, painel_72],
          "07-03": [cena_73, mecanismo_73, modelo_73, copo_73, padrao_73, razao_73, colunas_73]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
