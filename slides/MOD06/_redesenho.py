"""Desenhos que substituem os slides de texto do Módulo 6 (cartões, colunas, listas, tabelas e números).
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


# ---------------------------------------------------------------- 6.1

def caso_61():
    """6.1: a trajetória do caso, a ficha de uma linha e o que ninguém perguntou."""
    p = [svg_abre(1664, 400, "Em cima, a trajetória: vinte anos parado, aula de alta intensidade na segunda semana, aperto no peito na terceira série. Embaixo, à esquerda, a ficha de matrícula de uma linha: tem algum problema de saúde? Ele marcou não. À direita, o que a investigação achou depois: pressão alta sem tratamento, colesterol nunca dosado, trinta anos de cigarro, circunferência abdominal alta e um pai morto de infarto aos cinquenta e poucos"), defs(MUDO, FOSF)]
    rs = []
    passos = [("vinte anos parado", MUDO, PAPEL), ("alta intensidade, na segunda semana", GLIC, GLIC_T), ("aperto no peito, na terceira série", FOSF, FOSF_T)]
    for k, (t, cor, fundo) in enumerate(passos):
        x = k * 568
        p.append(caixa(x, 0, 500, 76, cor, fundo, esp=2, rx=38))
        rs.append(rot(x + 20, 22, t, w=460, tam=23, cor=cor if cor != MUDO else TINTA, peso=700, alinha="center"))
        if k < 2:
            p.append(seta(x + 508, 38, x + 558, 38, MUDO, "m0", esp=3))
    p.append(caixa(0, 130, 560, 270, TINTA, CARTAO, esp=2, rx=12))
    p.append(icone("t:clipboard-list", 24, 152, 44, TINTA))
    rs += [rot(84, 158, "Ficha de matrícula", w=440, tam=26, cor=TINTA, peso=700, serif=True),
           rot(24, 232, "Tem algum problema de saúde?", w=520, tam=24, cor=TINTA)]
    for k, t in enumerate(["sim", "não"]):
        x = 40 + k * 220
        p.append(f'<rect x="{x}" y="300" width="40" height="40" rx="6" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
        rs.append(rot(x + 54, 304, t, w=120, tam=26, cor=TINTA))
    p.append(f'<path d="M 268 318 L 282 334 L 304 302" fill="none" stroke="{FOSF}" stroke-width="5" stroke-linecap="round"/>')
    p.append(seta(580, 265, 680, 265, FOSF, "m1", esp=4))
    rs.append(rot(720, 130, "O que a investigação achou depois", w=900, tam=24, cor=FOSF, peso=700, serif=True))
    achados = ["pressão alta sem tratamento", "colesterol nunca dosado", "trinta anos de cigarro", "circunferência abdominal alta", "pai morto de infarto aos cinquenta e poucos"]
    for k, t in enumerate(achados):
        col, lin = (0, k) if k < 3 else (1, k - 3)
        x, y = 720 + col * 470, 186 + lin * 72
        p.append(f'<circle cx="{x + 10}" cy="{y + 16}" r="9" fill="{FOSF}"/>')
        rs.append(rot(x + 32, y, t, w=430, tam=23, cor=TINTA, lh=1.25))
    rs.append(rot(1190, 340, "Ninguém tinha perguntado.", w=470, tam=24, cor=FOSF, peso=700))
    return slide("caso", 400, p, rs, eyebrow="Caso ilustrativo", titulo="Marcou “não” porque não sabia que tinha")


def paradoxo_61():
    """6.1: o risco ao longo dos dias, com picos no esforço, em quem é ativo e em quem não é (esquema)."""
    p = [svg_abre(1664, 400, "Esquema, sem valores medidos. Risco ao longo das semanas em duas pessoas. Quem é pouco ativo tem a linha de base mais alta e, no esforço vigoroso raro, um pico grande. Quem é ativo tem a linha de base mais baixa e picos pequenos a cada sessão. No esforço, o risco sobe de forma transitória e mais em quem é menos ativo; na vida, o risco absoluto é pequeno e o saldo favorece a proteção")]
    rs = []
    X0, X1, Yb = 60, 1080, 360
    p.append(f'<line x1="{X0}" y1="{Yb}" x2="{X1}" y2="{Yb}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="{X0}" y1="20" x2="{X0}" y2="{Yb}" stroke="{MUDO}" stroke-width="3"/>')
    rs += [rot(0, 20, "risco", w=56, tam=20, cor=MUDO, alinha="right"),
           rot(X1 - 300, Yb + 8, "semanas", w=300, tam=20, cor=MUDO, alinha="right")]
    # pouco ativo: base alta, um pico grande
    d = f"M {X0} 210 L 640 210 L 660 60 L 690 210 L {X1} 210"
    p.append(f'<path d="{d}" fill="none" stroke="{FOSF}" stroke-width="4" stroke-linejoin="round"/>')
    # ativo: base baixa, picos pequenos em cada sessão
    pts = [f"M {X0} 310"]
    for k in range(9):
        x = X0 + 60 + k * 110
        pts.append(f"L {x} 310 L {x + 12} 270 L {x + 28} 310")
    pts.append(f"L {X1} 310")
    p.append(f'<path d="{" ".join(pts)}" fill="none" stroke="{OXID}" stroke-width="4" stroke-linejoin="round"/>')
    rs += [rot(80, 170, "pouco ativo", w=300, tam=22, cor=FOSF, peso=700),
           rot(700, 50, "esforço vigoroso raro", w=320, tam=21, cor=FOSF),
           rot(80, 322, "ativo", w=200, tam=22, cor=OXID, peso=700),
           rot(X0, Yb + 8, "esquema, sem valores medidos", w=400, tam=18, cor=MUDO)]
    for k, (t, d_, cor, fundo, y) in enumerate([("No esforço", "o risco sobe, de forma transitória, e mais em quem é menos ativo", FOSF, FOSF_T, 0),
                                                ("Na vida", "o risco absoluto é pequeno; a atividade habitual reduz eventos; o saldo favorece a proteção", OXID, OXID_T, 200)]):
        p.append(caixa(1150, y, 514, 180, cor, fundo, esp=2, rx=14))
        rs += [rot(1172, y + 18, t, w=470, tam=28, cor=cor, peso=700, serif=True),
               rot(1172, y + 66, d_, w=470, tam=22, cor=TINTA, lh=1.3)]
    return slide("paradoxo", 400, p, rs,
                 eyebrow="Associação Americana do Coração, 2020", titulo="As duas frases são verdade",
                 destaque="A avaliação não serve para assustar nem para impedir. Serve para achar quem precisa de uma entrada diferente.",
                 destaque_cor="tinta", fonte="Franklin e colaboradores · Circulation 2020")


def modelo_61():
    """6.1: a idade riscada e as três perguntas do modelo."""
    p = [svg_abre(1664, 360, "À esquerda, a idade, riscada: deixou de ser o critério. À direita, as três perguntas do modelo. Já pratica exercício regular, planejado, ao menos moderado, trinta minutos, três vezes por semana, nos últimos três meses? Tem doença cardiovascular, metabólica ou renal conhecida, ou sinais e sintomas sugestivos? Que intensidade pretende: leve, moderada ou vigorosa?"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 110, 240, 120, MUDO, PAPEL, esp=2, rx=60))
    rs += [rot(0, 140, "a idade", w=240, tam=34, cor=MUDO, peso=700, alinha="center", serif=True)]
    p.append(f'<line x1="20" y1="210" x2="220" y2="130" stroke="{FOSF}" stroke-width="6" stroke-linecap="round"/>')
    rs.append(rot(0, 250, "deixou de ser o critério", w=240, tam=20, cor=MUDO, alinha="center"))
    p.append(seta(256, 170, 316, 170, MUDO, "m0", esp=4))
    qs = [("t:run", "Já pratica exercício regular?", "planejado, ao menos moderado, 30 min, 3 vezes por semana, nos últimos 3 meses", OXID, OXID_T),
          ("t:heartbeat", "Tem doença ou sintoma?", "cardiovascular, metabólica ou renal conhecida; ou sinais e sintomas sugestivos", FOSF, FOSF_T),
          ("t:gauge", "Que intensidade pretende?", "leve, moderada ou vigorosa", GLIC, GLIC_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(qs):
        x = 336 + k * 448
        p.append(caixa(x, 0, 424, 360, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="{x + 48}" cy="48" r="28" fill="{cor}"/>')
        rs.append(rot(x + 20, 30, str(k + 1), w=56, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(icone(ic, x + 340, 22, 56, cor))
        rs += [rot(x + 24, 100, t, w=380, tam=28, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 24, 170, d, w=380, tam=22, cor=TINTA, lh=1.35)]
    return slide("modelo", 360, p, rs,
                 eyebrow="Colégio Americano de Medicina do Esporte, 2015", titulo="Etapa um: três perguntas, não a idade",
                 destaque="O modelo anterior mandava gente demais ao médico. O rastreio cauteloso demais tira mais gente do exercício do que salva de evento.",
                 destaque_cor="tinta", fonte="Riebe e colaboradores · Medicine & Science in Sports & Exercise 2015")


def saidas_61():
    """6.1: a grade de saídas do modelo, em cores."""
    p = [svg_abre(1664, 360, "Grade com as saídas do modelo. Linhas: não pratica e já pratica. Colunas: sem doença e sem sintoma, doença conhecida sem sintoma, sinal ou sintoma. Não pratica, sem doença: não precisa de liberação, começa leve a moderado e progride. Não pratica, com doença conhecida: liberação recomendada antes de começar. Não pratica, com sintoma: liberação antes de começar. Já pratica, sem doença: segue e progride. Já pratica, com doença conhecida: moderado sem liberação, vigoroso com liberação. Já pratica, com sintoma: para e avalia")]
    rs = []
    cols = ["Sem doença, sem sintoma", "Doença conhecida, sem sintoma", "Sinal ou sintoma"]
    W0, cw, gap = 250, 462, 14
    for j, t in enumerate(cols):
        x = W0 + j * (cw + gap)
        rs.append(rot(x, 6, t, w=cw, tam=24, cor=TINTA, peso=700, alinha="center"))
    linhas = [("Não pratica", [("não precisa de liberação", "começa leve a moderado e progride", OXID, OXID_T, "t:check"),
                                ("liberação recomendada", "antes de começar", GLIC, GLIC_T, "t:stethoscope"),
                                ("liberação antes de começar", "o sintoma é investigado primeiro", FOSF, FOSF_T, "t:stethoscope")]),
              ("Já pratica", [("não precisa de liberação", "segue e progride", OXID, OXID_T, "t:check"),
                               ("moderado: segue", "vigoroso: com liberação", GLIC, GLIC_T, "t:gauge"),
                               ("para e avalia", "a única saída sem negociação", FOSF, FOSF_T, "t:hand-stop")])]
    for i, (rot_l, cel) in enumerate(linhas):
        y = 52 + i * 154
        rs.append(rot(0, y + 52, rot_l, w=230, tam=28, cor=TINTA, peso=700, serif=True))
        for j, (a, b, cor, fundo, ic) in enumerate(cel):
            x = W0 + j * (cw + gap)
            p.append(caixa(x, y, cw, 140, cor, fundo, esp=2, rx=14))
            p.append(icone(ic, x + 18, y + 20, 40, cor))
            rs += [rot(x + 70, y + 22, a, w=cw - 86, tam=24, cor=cor, peso=700, lh=1.2),
                   rot(x + 70, y + 84, b, w=cw - 86, tam=21, cor=TINTA, lh=1.25)]
    return slide("saidas", 360, p, rs,
                 eyebrow="As saídas do modelo", titulo="Quem precisa de liberação médica",
                 destaque="Perguntar sobre doença e sintoma é de todos. Investigar o que a pergunta achar é do médico. PAR-Q+: melhor que o formulário de uma linha.",
                 destaque_cor="petr")


def fechamento_61():
    """6.1: três balões de fala e o que cada pergunta acha."""
    p = [svg_abre(1664, 400, "Três balões de fala com as perguntas de fechamento. O que mudou nos últimos seis meses: trabalho, sono, peso, medicação, vida. Já parou alguma atividade por causa de um sintoma: acha quem se adaptou ao próprio limite, quem não diz que sente falta de ar, diz que parou de subir escada. Toma alguma coisa por conta própria: estimulante, pré-treino, emagrecedor, anabolizante, que não são relatados espontaneamente")]
    rs = []
    qs = [("“O que mudou nos últimos seis meses?”", "trabalho, sono, peso, medicação, vida", OXID, OXID_T, "t:calendar"),
          ("“Já parou alguma atividade por causa de um sintoma?”", "acha quem se adaptou ao próprio limite: não diz que sente falta de ar, diz que parou de subir escada", GLIC, GLIC_T, "t:stairs"),
          ("“Toma alguma coisa por conta própria?”", "estimulante, pré-treino, emagrecedor, anabolizante: ninguém relata sem ser perguntado", FOSF, FOSF_T, "t:pill")]
    for k, (q, d, cor, fundo, ic) in enumerate(qs):
        x = k * 568
        p.append(f'<path d="M {x + 16} 0 H {x + 512} Q {x + 528} 0 {x + 528} 16 V 168 Q {x + 528} 184 {x + 512} 184 H {x + 120} L {x + 70} 226 L {x + 80} 184 H {x + 16} Q {x} 184 {x} 168 V 16 Q {x} 0 {x + 16} 0 Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(x + 24, 30, q, w=480, tam=27, cor=cor, peso=700, serif=True, lh=1.2))
        p.append(icone(ic, x + 24, 260, 52, cor))
        rs.append(rot(x + 92, 256, d, w=430, tam=22, cor=TINTA, lh=1.3))
    return slide("fechamento", 400, p, rs,
                 eyebrow="Rendem mais do que parecem", titulo="Três perguntas que quase ninguém faz",
                 destaque="Na primeira consulta, o que decide segurança: sintoma, doença, história familiar, medicação e substância. O resto melhora com vínculo.",
                 destaque_cor="tinta")


def sintomas_61():
    """6.1: a síncope no esforço em destaque e os outros cinco sinais."""
    p = [svg_abre(1664, 420, "À esquerda, em destaque, a síncope durante o esforço: bandeira vermelha máxima, não treina até ser avaliado. À direita, os outros sinais: desconforto no peito no esforço, falta de ar desproporcional, palpitação com tontura ou desmaio, queda de tolerância sem explicação, e o conjunto da insuficiência cardíaca. Uma nota: síncope logo depois de parar costuma ser vasovagal, mas quem conclui é quem investigou")]
    rs = []
    p.append(caixa(0, 0, 560, 420, FOSF, FOSF, esp=0, rx=18))
    p.append(icone("t:alert-triangle", 32, 32, 80, PAPEL))
    rs += [rot(32, 136, "Síncope durante o esforço", w=500, tam=40, cor=PAPEL, peso=700, serif=True, lh=1.1),
           rot(32, 250, "bandeira vermelha máxima", w=500, tam=26, cor=PAPEL, peso=700),
           rot(32, 300, "desmaiou no esforço: não treina até ser avaliado. Sem “foi só a pressão”.", w=500, tam=23, cor=PAPEL, lh=1.3)]
    itens = [("Desconforto no peito no esforço", "aperto, peso, queimação: quem nega “dor” descreve outra coisa", FOSF, FOSF_T),
             ("Falta de ar desproporcional", "ou em repouso, ou ao deitar", GLIC, GLIC_T),
             ("Palpitação com tontura ou desmaio", "isolada é comum; com sintoma, não", GLIC, GLIC_T),
             ("Queda de tolerância sem explicação", "acima dos quarenta, a coronária se disfarça de “fora de forma”", GLIC, GLIC_T),
             ("Inchaço e falta de ar ao deitar", "acordar sem ar: o conjunto da insuficiência cardíaca", GLIC, GLIC_T),
             ("Síncope logo depois de parar", "costuma ser vasovagal; quem conclui é quem investigou", MUDO, PAPEL)]
    for k, (t, d, cor, fundo) in enumerate(itens):
        col, lin = k % 2, k // 2
        x, y = 600 + col * 540, lin * 144
        p.append(caixa(x, y, 524, 130, cor, fundo, esp=2, rx=14))
        rs += [rot(x + 20, y + 14, t, w=484, tam=23, cor=cor if cor != MUDO else TINTA, peso=700, lh=1.2),
               rot(x + 20, y + (74 if len(t) < 38 else 74), d, w=484, tam=20, cor=TINTA, lh=1.25)]
    return slide("sintomas", 420, p, rs, eyebrow="Etapa três: para as seis profissões", titulo="Os sinais que interrompem tudo")


def historia_61():
    """6.1: a árvore da família, os fatores de risco e o que a pessoa toma."""
    p = [svg_abre(1664, 400, "Três blocos da ficha. História familiar, numa árvore: morte súbita ou cardiopatia hereditária em qualquer parente; coronária precoce em parente de primeiro grau, antes dos 55 no homem e antes dos 65 na mulher. Fatores de risco: pressão alta, diabetes, colesterol, tabagismo, obesidade abdominal, doença renal. Medicações e substâncias, inclusive as de conta própria")]
    rs = []
    p.append(caixa(0, 0, 640, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "História familiar", w=590, tam=28, cor=FOSF, peso=700, serif=True))
    # árvore: pai e mãe, linha até o paciente e um irmão
    for x, ic, t in [(130, "h:man", "homem: antes dos 55"), (390, "h:woman", "mulher: antes dos 65")]:
        p.append(icone(ic, x, 76, 72, FOSF))
        rs.append(rot(x - 70, 152, t, w=212, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="202" y1="112" x2="390" y2="112" stroke="{BORDA}" stroke-width="3"/>')
    p.append(f'<line x1="296" y1="112" x2="296" y2="200" stroke="{BORDA}" stroke-width="3"/>')
    p.append(f'<line x1="200" y1="200" x2="400" y2="200" stroke="{BORDA}" stroke-width="3"/>')
    for x, ic in [(170, "h:person"), (370, "h:person")]:
        p.append(f'<line x1="{x + 30}" y1="200" x2="{x + 30}" y2="212" stroke="{BORDA}" stroke-width="3"/>')
        p.append(icone(ic, x, 212, 60, TINTA if x == 170 else FOSF))
    rs += [rot(130, 276, "a pessoa", w=140, tam=20, cor=TINTA, alinha="center"),
           rot(330, 276, "irmão", w=140, tam=20, cor=TINTA, alinha="center"),
           rot(24, 318, "coronária precoce em parente de primeiro grau; morte súbita ou cardiopatia hereditária em qualquer idade", w=596, tam=19, cor=TINTA, lh=1.3)]
    p.append(caixa(680, 0, 560, 400, GLIC, CARTAO, esp=2, rx=16))
    rs.append(rot(704, 18, "Fatores de risco", w=510, tam=28, cor=GLIC, peso=700, serif=True))
    for k, t in enumerate(["pressão alta", "diabetes", "colesterol", "tabagismo", "obesidade abdominal", "doença renal"]):
        col, lin = k % 2, k // 2
        x, y = 704 + col * 262, 90 + lin * 100
        p.append(caixa(x, y, 244, 80, GLIC, GLIC_T, esp=2, rx=40))
        rs.append(rot(x + 8, y + 24, t, w=228, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.15))
    p.append(caixa(1280, 0, 384, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(1304, 18, "Medicações e substâncias", w=340, tam=28, cor=OXID, peso=700, serif=True, lh=1.15))
    p.append(icone("t:pill", 1412, 130, 120, OXID))
    rs.append(rot(1304, 280, "inclusive as de conta própria", w=340, tam=23, cor=TINTA, alinha="center", lh=1.3))
    return slide("historia", 400, p, rs,
                 eyebrow="O que precisa estar na ficha", titulo="História familiar, fatores de risco, substâncias",
                 destaque="“Não sei” é resposta clínica: não é “não”, é motivo para medir a pressão ali mesmo.",
                 destaque_cor="tinta")


def perfis_61():
    """6.1: quatro perfis, o que decide e a entrada, em linhas com setas."""
    p = [svg_abre(1664, 380, "Quatro perfis típicos, cada um com o que decide e a entrada no exercício. Jovem sem sintoma: decide a ausência de história familiar; entra leve a moderado sem liberação, com progressão. Meia-idade voltando: decidem fatores de risco, sintoma e intensidade; o médico faz a conta do risco e a entrada é gradual. Doença crônica compensada: decide quem prescreve e como monitora; exercício é tratamento, com critério. Atleta federado: decide a exigência da federação ou do evento; outro sistema, outra lógica"), defs(MUDO)]
    rs = [rot(84, 0, "Perfil", w=400, tam=22, cor=MUDO, peso=700), rot(560, 0, "O que decide", w=500, tam=22, cor=MUDO, peso=700),
          rot(1150, 0, "Entrada", w=500, tam=22, cor=MUDO, peso=700)]
    linhas = [("h:running", "Jovem sem sintoma", "sem história familiar", "leve a moderado sem liberação; progressão", OXID, OXID_T),
              ("h:man", "Meia-idade voltando", "fatores de risco, sintoma, intensidade", "conta do risco pelo médico; entrada gradual", GLIC, GLIC_T),
              ("t:heartbeat", "Doença crônica compensada", "quem prescreve e como monitora", "exercício é tratamento, com critério", AZUL, AZUL_T),
              ("t:medal", "Atleta federado", "exigência da federação ou do evento", "outro sistema, outra lógica", MUDO, PAPEL)]
    for k, (ic, a, b, c, cor, fundo) in enumerate(linhas):
        y = 40 + k * 86
        p.append(icone(ic, 10, y + 8, 56, cor))
        p.append(caixa(84, y, 420, 74, cor, fundo, esp=2, rx=37))
        rs.append(rot(100, y + 22, a, w=388, tam=24, cor=TINTA, peso=700, alinha="center"))
        p.append(seta(512, y + 37, 548, y + 37, MUDO, "m0", esp=3))
        rs.append(rot(560, y + 22, b, w=540, tam=22, cor=TINTA))
        p.append(seta(1102, y + 37, 1138, y + 37, MUDO, "m0", esp=3))
        p.append(caixa(1150, y, 514, 74, cor, CARTAO, esp=2, rx=12))
        rs.append(rot(1166, y + 22, c, w=484, tam=22, cor=cor if cor != MUDO else TINTA, peso=600, lh=1.2))
    return slide("perfis", 380, p, rs,
                 eyebrow="Etapa quatro: perfis típicos", titulo="O que fazer com o que se achou",
                 destaque="Doença cardiovascular estabelecida não é, em geral, contraindicação ao exercício. É indicação de exercício prescrito com critério.",
                 destaque_cor="petr")


def tres_saidas_61():
    """6.1: uma bifurcação em três, com a espessura do caminho dizendo quem vai por onde (esquema)."""
    p = [svg_abre(1664, 400, "Do que se achou na avaliação saem três caminhos; a espessura indica, em esquema, quantos vão por cada um. O mais largo: libera com progressão, a maioria. O do meio: libera com restrição enquanto investiga, a saída mais subutilizada, como caminhar enquanto espera o cardiologista. O mais fino: suspende até avaliar, para sintoma de alerta e instabilidade")]
    rs = []
    vias = [(60, 70, "Libera com progressão", "a maioria", OXID, OXID_T, "t:trending-up"),
            (200, 30, "Libera com restrição enquanto investiga", "a mais subutilizada: caminhar enquanto espera o cardiologista", GLIC, GLIC_T, "t:walk"),
            (340, 12, "Suspende até avaliar", "sintoma de alerta e instabilidade", FOSF, FOSF_T, "t:hand-stop")]
    for yc, esp, t, d, cor, fundo, ic in vias:
        y0 = 200 + (yc - 200) * 0.3
        p.append(f'<path d="M 280 {y0:.0f} C 480 {y0:.0f}, 560 {yc}, 760 {yc}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linecap="round" opacity="0.85"/>')
        p.append(caixa(780, yc - 58, 884, 116, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 800, yc - 30, 60, cor))
        rs += [rot(880, yc - 44, t, w=760, tam=27, cor=cor, peso=700, serif=True),
               rot(880, yc + 2, d, w=760, tam=22, cor=TINTA, lh=1.25)]
    p.append(caixa(0, 140, 300, 120, TINTA, CARTAO, esp=3, rx=60))
    rs.append(rot(10, 178, "o que se achou", w=280, tam=28, cor=TINTA, peso=700, alinha="center", serif=True))
    rs.append(rot(0, 300, "espessura em esquema", w=300, tam=18, cor=MUDO, alinha="center"))
    return slide("tres_saidas", 400, p, rs, eyebrow="Quase nunca é tudo ou nada", titulo="Três saídas")


def registro_61():
    """6.1: a página do registro e os dois erros carimbados."""
    p = [svg_abre(1664, 400, "À esquerda, uma página de registro com cinco linhas marcadas: as três perguntas do modelo; sintomas, com o que foi negado; história familiar, com idade e evento; fatores de risco, medicações e substâncias; conduta, data e orientação dada. À direita, dois erros: escrever sem alterações sem dizer o que se perguntou, e não registrar a recusa nem a orientação")]
    rs = []
    p.append(f'<path d="M 0 0 H 820 L 880 60 V 400 H 0 Z" fill="{CARTAO}" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<path d="M 820 0 V 60 H 880" fill="none" stroke="{OXID}" stroke-width="3"/>')
    rs.append(rot(28, 20, "Em uma página", w=700, tam=28, cor=OXID, peso=700, serif=True))
    itens = ["as três perguntas do modelo", "sintomas, com o que foi negado", "história familiar, com idade e evento", "fatores de risco, medicações, substâncias", "conduta, data e orientação dada"]
    for k, t in enumerate(itens):
        y = 84 + k * 62
        p.append(f'<rect x="28" y="{y}" width="34" height="34" rx="6" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        p.append(f'<path d="M 36 {y + 17} L 43 {y + 25} L 56 {y + 9}" fill="none" stroke="{OXID}" stroke-width="4" stroke-linecap="round"/>')
        rs.append(rot(80, y + 2, t, w=760, tam=24, cor=TINTA))
        p.append(f'<line x1="80" y1="{y + 44}" x2="840" y2="{y + 44}" stroke="{BORDA}" stroke-width="1"/>')
    erros = [("“Sem alterações”", "sem dizer o que se perguntou"), ("Nada sobre a recusa", "nem sobre a orientação dada")]
    rs.append(rot(960, 20, "Dois erros", w=700, tam=28, cor=FOSF, peso=700, serif=True))
    for k, (a, b) in enumerate(erros):
        y = 84 + k * 158
        p.append(caixa(960, y, 704, 136, FOSF, FOSF_T, esp=2, rx=14))
        p.append(icone("t:x", 984, y + 38, 60, FOSF))
        rs += [rot(1064, y + 22, a, w=580, tam=27, cor=FOSF, peso=700), rot(1064, y + 70, b, w=580, tam=23, cor=TINTA)]
    return slide("registro", 400, p, rs,
                 eyebrow="O registro", titulo="O que não está escrito não aconteceu",
                 destaque="O formulário de matrícula de uma linha é documento de defesa, não instrumento clínico. Trocá-lo custa cinco minutos por aluno.",
                 destaque_cor="tinta")

# ---------------------------------------------------------------- 6.2

def ecg(p, x0, y0, w, cor, n=4, amp=60, esp=4):
    """Um traçado de eletrocardiograma estilizado, com n batimentos, de x0 a x0 + w, na linha de base y0."""
    passo = w / n
    d = [f"M {x0:.0f} {y0}"]
    for k in range(n):
        x = x0 + k * passo
        u = passo / 20
        d.append(f"L {x + 3*u:.0f} {y0} Q {x + 4.5*u:.0f} {y0 - amp*0.18:.0f} {x + 6*u:.0f} {y0}"
                 f" L {x + 8*u:.0f} {y0} L {x + 8.6*u:.0f} {y0 + amp*0.15:.0f} L {x + 9.4*u:.0f} {y0 - amp:.0f}"
                 f" L {x + 10.2*u:.0f} {y0 + amp*0.3:.0f} L {x + 10.8*u:.0f} {y0} L {x + 12.5*u:.0f} {y0}"
                 f" Q {x + 14.5*u:.0f} {y0 - amp*0.32:.0f} {x + 16.5*u:.0f} {y0} L {x + 20*u:.0f} {y0}")
    p.append(f'<path d="{" ".join(d)}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linejoin="round"/>')


def pergunta_62():
    """6.2: o eletrocardiograma aponta bem para uma pergunta e mal para a outra."""
    p = [svg_abre(1664, 400, "À esquerda, um traçado de eletrocardiograma de repouso. Duas setas saem dele. Uma, firme, chega ao que mata o jovem: cardiomiopatia, canalopatia, pré-excitação; o exame foi desenhado para isso. A outra, tracejada, chega ao que mata o adulto de meia-idade: a doença coronariana, que um eletrocardiograma normal não exclui"), defs(OXID, FOSF)]
    rs = []
    p.append(caixa(0, 110, 560, 180, TINTA, CARTAO, esp=2, rx=16))
    ecg(p, 30, 220, 500, TINTA, n=3, amp=70)
    rs.append(rot(24, 124, "eletrocardiograma de repouso", w=510, tam=22, cor=MUDO, peso=700))
    p.append(f'<path d="M 570 170 C 700 120, 760 90, 880 90" fill="none" stroke="{OXID}" stroke-width="5" marker-end="url(#m0)"/>')
    p.append(f'<path d="M 570 240 C 700 290, 760 310, 880 310" fill="none" stroke="{FOSF}" stroke-width="4"{TRACO} marker-end="url(#m1)"/>')
    for y, ic, t, d, cor, fundo in [(0, "h:young-people", "O que mata o jovem", "cardiomiopatia, canalopatia, pré-excitação: o exame foi desenhado para isso", OXID, OXID_T),
                                    (220, "h:man", "O que mata o adulto de meia-idade", "doença coronariana: um eletrocardiograma normal não a exclui", FOSF, FOSF_T)]:
        p.append(caixa(900, y, 764, 180, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 924, y + 30, 72, cor))
        rs += [rot(1016, y + 24, t, w=620, tam=28, cor=cor, peso=700, serif=True),
               rot(1016, y + 76, d, w=620, tam=23, cor=TINTA, lh=1.3)]
    p.append(icone("t:check", 700, 60, 44, OXID))
    p.append(icone("t:x", 700, 300, 44, FOSF))
    return slide("pergunta", 400, p, rs, eyebrow="A frase que organiza a aula",
                 titulo="Exame responde a uma pergunta, e mal às outras")


def pedidos_62():
    """6.2: três pedidos, a mesma palavra, perguntas diferentes por trás."""
    p = [svg_abre(1664, 400, "Três pedidos típicos na mesma semana. O clube pede exame do coração para liberar o jogador da base. Uma mulher de meia-idade vai começar a correr e diz que faz check-up completo e está tudo normal. O preparador quer exigir eletrocardiograma de todos os alunos. Embaixo de cada pedido, a pergunta que precisa ser feita antes: que pergunta estou fazendo, e que ferramenta responde"), defs(MUDO)]
    rs = []
    itens = [("t:shirt-sport", "O clube", "“exame do coração para liberar” o jogador da base", OXID, OXID_T),
             ("t:checklist", "O check-up completo", "mulher de meia-idade, vai começar a correr: “está tudo normal”", GLIC, GLIC_T),
             ("t:users-group", "O preparador", "quer exigir eletrocardiograma de todos os alunos", FOSF, FOSF_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 220, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 56, cor))
        rs += [rot(x + 96, 34, t, w=410, tam=28, cor=cor, peso=700, serif=True),
               rot(x + 24, 108, d, w=480, tam=23, cor=TINTA, lh=1.3)]
        p.append(seta(x + 264, 230, x + 264, 282, MUDO, "m0", esp=3))
        p.append(caixa(x + 64, 296, 400, 100, MUDO, CARTAO, esp=2, rx=50))
        p.append(icone("t:zoom-question", x + 88, 322, 48, MUDO))
        rs.append(rot(x + 150, 314, "que pergunta? que ferramenta?", w=300, tam=22, cor=TINTA, peso=600, lh=1.2))
    return slide("pedidos", 400, p, rs, eyebrow="Três pedidos típicos", titulo="A mesma coisa, necessidades diferentes",
                 destaque="A decisão não é pedir ou não pedir. É que pergunta estou fazendo, e que ferramenta responde.", destaque_cor="tinta")


def ecg_62():
    """6.2: o traçado em cima, e o que ele vê e o que não vê."""
    p = [svg_abre(1664, 380, "Em cima, um traçado de eletrocardiograma de repouso. À esquerda, o que ele vê bem: padrão de cardiomiopatia hipertrófica, sinais de cardiomiopatia arritmogênica, pré-excitação, QT longo e Brugada, bloqueios e sobrecargas. À direita, o que não vê: coronária obstruída em quem não tem sintoma; mostra a cicatriz de um infarto silencioso, mas um traçado normal não tranquiliza sobre a coronária")]
    rs = []
    ecg(p, 0, 70, 1664, TINTA, n=8, amp=56, esp=3)
    blocos = [(0, "t:eye", "Vê bem", ["padrão de cardiomiopatia hipertrófica", "sinais de cardiomiopatia arritmogênica", "pré-excitação", "QT longo, Brugada", "bloqueios e sobrecargas"], OXID, OXID_T),
              (864, "t:eye-off", "Não vê", ["coronária obstruída em quem não tem sintoma", "mostra a cicatriz de um infarto silencioso", "normal não tranquiliza sobre a coronária"], FOSF, FOSF_T)]
    for x, ic, t, itens, cor, fundo in blocos:
        p.append(caixa(x, 110, 800, 270, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 126, 44, cor))
        rs.append(rot(x + 82, 130, t, w=680, tam=28, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            y = 190 + k * (38 if len(itens) > 3 else 56)
            p.append(f'<circle cx="{x + 34}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(x + 54, y, it, w=720, tam=23, cor=TINTA))
    return slide("ecg", 380, p, rs, eyebrow="O eletrocardiograma de repouso", titulo="Doença elétrica e estrutural, não coronária",
                 destaque="Depois dos quarenta, a ferramenta que importa é a avaliação de risco cardiovascular. Check-up completo é conceito de marketing.",
                 destaque_cor="verm")


def corrado_62():
    """6.2: as duas taxas do Vêneto em barras, na mesma escala."""
    p = [svg_abre(1664, 360, "Duas barras na mesma escala: mortes súbitas cardiovasculares por cem mil atletas por ano no Vêneto. Em 1979 e 1980, antes do rastreio, 3,6. Em 2003 e 2004, no período tardio do rastreio com eletrocardiograma, 0,4. Queda de 89 por cento, concentrada nas mortes por cardiomiopatia"), defs(MUDO)]
    rs = []
    X0, esc = 340, 220
    for k, (rot_, v, cor) in enumerate([("1979–1980, antes do rastreio", 3.6, FOSF), ("2003–2004, rastreio estabelecido", 0.4, OXID)]):
        y = 30 + k * 140
        rs.append(rot(0, y + 18, rot_, w=320, tam=23, cor=TINTA, peso=600, lh=1.2))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * esc:.0f}" height="90" rx="4" fill="{cor}"/>')
        rs.append(rot(X0 + v * esc + 20, y + 16, f"{v:.1f}".replace(".", ","), w=200, tam=48, cor=cor, peso=700, serif=True))
    p.append(f'<line x1="{X0}" y1="10" x2="{X0}" y2="280" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(X0, 296, "mortes súbitas cardiovasculares por 100 mil atletas por ano, de 12 a 35 anos", w=1000, tam=20, cor=MUDO))
    p.append(caixa(1340, 40, 324, 220, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1340, 64, "−89%", w=324, tam=72, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1360, 160, "concentrada nas mortes por cardiomiopatia", w=284, tam=22, cor=PAPEL, alinha="center", lh=1.3)]
    return slide("corrado", 360, p, rs, eyebrow="Corrado e colaboradores, 2006", titulo="O argumento do Vêneto",
                 destaque="Observacional, de uma região, 1979 a 2004. É o dado que sustenta a posição europeia, e o debate sobre generalizá-lo continua.",
                 destaque_cor="ambar", fonte="Atletas de 12 a 35 anos · JAMA 2006")


def posicoes_62():
    """6.2: as três posições como colunas, com a brasileira em destaque."""
    p = [svg_abre(1664, 380, "Três posições sobre o eletrocardiograma no jovem competitivo, a partir dos mesmos dados. Europeia: rastreio de todos, pela experiência italiana. Americana: história e exame físico de catorze itens, sem rastreio universal, por custo, estrutura e falso-positivo. Brasileira, de 2019, em destaque: eletrocardiograma classe I, nível A, no profissional e no amador; ergometria antes de alta intensidade com força menor; ecocardiograma como confirmatório")]
    rs = []
    cols = [("Europeia", "rastreio de todos", "a experiência italiana", OXID, CARTAO, "t:check", 2),
            ("Americana", "história e exame físico de 14 itens; sem rastreio universal", "custo, estrutura, falso-positivo", MUDO, CARTAO, "t:clipboard-list", 2),
            ("Brasileira, 2019", "classe I, nível A, no profissional e no amador", "ergometria antes de alta intensidade, com força menor; eco confirmatório", OXID, OXID_T, "t:flag", 5)]
    for k, (t, ecg_, arg, cor, fundo, ic, esp) in enumerate(cols):
        x = k * 560
        p.append(caixa(x, 0, 524, 380, cor, fundo, esp=esp, rx=18))
        p.append(icone(ic, x + 24, 24, 48, cor))
        rs += [rot(x + 88, 30, t, w=420, tam=30, cor=cor if cor != MUDO else TINTA, peso=700, serif=True),
               rot(x + 24, 104, "eletrocardiograma no jovem competitivo", w=480, tam=19, cor=MUDO, peso=700),
               rot(x + 24, 140, ecg_, w=476, tam=25, cor=TINTA, peso=700, lh=1.25),
               rot(x + 24, 256, "o argumento", w=480, tam=19, cor=MUDO, peso=700),
               rot(x + 24, 290, arg, w=476, tam=22, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 24}" y1="240" x2="{x + 500}" y2="240" stroke="{BORDA}" stroke-width="2"/>')
    return slide("posicoes", 380, p, rs, eyebrow="Os mesmos dados, decisões diferentes", titulo="Onde o Brasil está",
                 destaque="Quando o clube ou a federação pede eletrocardiograma, não é excesso. Está na diretriz.",
                 destaque_cor="petr", fonte="SBC e SBMEE, Arquivos Brasileiros de Cardiologia 2019")


def leitura_62():
    """6.2: a régua de leitura: o que é adaptação e o que sempre investiga."""
    p = [svg_abre(1664, 380, "Dois lados de uma régua de leitura do eletrocardiograma do atleta. À esquerda, adaptação: isolada, não investiga; bradicardia sinusal, arritmia sinusal respiratória, bloqueio atrioventricular de primeiro grau, repolarização precoce, voltagem isolada de hipertrofia. À direita, sempre investiga: inversão de onda T em certas derivações, depressão de ST, onda Q patológica, pré-excitação e QT muito longo ou curto, arritmia ventricular")]
    rs = []
    lados = [(0, "Adaptação: isolada, não investiga", ["bradicardia sinusal", "arritmia sinusal respiratória", "bloqueio AV de primeiro grau", "repolarização precoce", "voltagem isolada de hipertrofia"], OXID, OXID_T, "t:heart"),
             (864, "Sempre investiga", ["inversão de onda T em certas derivações", "depressão de ST", "onda Q patológica", "pré-excitação; QT muito longo ou curto", "arritmia ventricular"], FOSF, FOSF_T, "t:zoom-question")]
    for x, t, itens, cor, fundo, ic in lados:
        p.append(icone(ic, x, 0, 44, cor))
        rs.append(rot(x + 58, 4, t, w=740, tam=27, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            y = 64 + k * 62
            p.append(caixa(x, y, 800, 52, cor, fundo, esp=2, rx=26))
            rs.append(rot(x + 28, y + 12, it, w=750, tam=23, cor=TINTA))
    p.append(f'<line x1="832" y1="0" x2="832" y2="380" stroke="{BORDA}" stroke-width="3"{TRACO}/>')
    return slide("leitura", 380, p, rs, eyebrow="Critérios internacionais, 2017", titulo="Pedir é fácil; ler é o que decide",
                 destaque="O laudo automático do aparelho não usa critério de atleta. Exame sem leitura treinada produz mais dano que benefício.",
                 destaque_cor="tinta", fonte="Drezner e colaboradores · British Journal of Sports Medicine 2017")


def adulto_62():
    """6.2: quatro ferramentas como degraus, da que custa zero à que depende de indicação."""
    p = [svg_abre(1664, 380, "Quatro degraus, na ordem de uso no adulto de meia-idade. Primeiro, o cálculo de risco cardiovascular, com idade, sexo, pressão, colesterol, diabetes e tabagismo, que custa zero. Segundo, o teste ergométrico, com sintoma, doença conhecida, alto risco e esforço vigoroso, e para prescrever. Terceiro, o escore de cálcio, que reclassifica o risco intermediário, em conversa com a cardiologia. Quarto, o ecocardiograma, por indicação: sopro, eletro alterado, sintoma, história familiar")]
    rs = []
    degraus = [("Cálculo de risco cardiovascular", "idade, sexo, pressão, colesterol, diabetes, tabagismo: custa zero", OXID, OXID_T, "t:checklist"),
               ("Teste ergométrico", "sintoma, doença conhecida, alto risco e esforço vigoroso; e para prescrever", OXID, OXID_T, "t:run"),
               ("Escore de cálcio", "reclassifica o risco intermediário; conversa com a cardiologia", GLIC, GLIC_T, "t:target"),
               ("Ecocardiograma", "por indicação: sopro, eletro alterado, sintoma, história familiar", GLIC, GLIC_T, "t:heartbeat")]
    for k, (t, d, cor, fundo, ic) in enumerate(degraus):
        x, w = k * 416, 400
        y = 190 - k * 60
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{380 - y}" rx="10" fill="{fundo}" stroke="{cor}" stroke-width="2"/>')
        p.append(f'<circle cx="{x + 40}" cy="{y + 40}" r="24" fill="{cor}"/>')
        rs.append(rot(x + 16, y + 24, str(k + 1), w=48, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(icone(ic, x + w - 64, y + 18, 44, cor))
        rs += [rot(x + 76, y + 20, t, w=w - 150, tam=24, cor=cor, peso=700, lh=1.15),
               rot(x + 18, y + 86, d, w=w - 36, tam=20, cor=TINTA, lh=1.3)]
    rs.append(rot(0, 0, "do mais barato e mais útil ao que depende de indicação", w=800, tam=21, cor=MUDO))
    return slide("adulto", 380, p, rs, eyebrow="O adulto de meia-idade", titulo="Quatro ferramentas, em ordem",
                 destaque="Ergometria em quem é de baixo risco e sem sintoma: falso-positivo alto, valor preditivo baixo, e uma cascata.",
                 destaque_cor="verm")


def naopedir_62():
    """6.2: quatro pedidos riscados, e a cascata que eles disparam."""
    p = [svg_abre(1664, 400, "Quatro pedidos riscados: ecocardiograma de rotina sem sintoma e sem indicação; ergometria anual em quem é de baixo risco; painel gigante de exames em quem não tem pergunta; check-up completo, caro, tranquilizador e sem resposta. Embaixo, a cascata que um achado sem pergunta dispara: achado, novo exame, ansiedade, outro exame, afastamento")]
    rs = []
    itens = [("t:heartbeat", "Eco de rotina", "sem sintoma e sem indicação"), ("t:run", "Ergometria anual", "em baixo risco"),
             ("t:clipboard-list", "Painel gigante", "em quem não tem pergunta"), ("t:checklist", "Check-up completo", "caro, tranquilizador, sem resposta")]
    for k, (ic, t, d) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 0, 392, 230, FOSF, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 156, 22, 80, MUDO))
        p.append(f'<line x1="{x + 140}" y1="112" x2="{x + 252}" y2="16" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
        rs += [rot(x + 16, 124, t, w=360, tam=27, cor=FOSF, peso=700, alinha="center", serif=True),
               rot(x + 16, 168, d, w=360, tam=21, cor=TINTA, alinha="center", lh=1.25)]
    passos = ["achado sem pergunta", "novo exame", "ansiedade", "outro exame", "afastamento"]
    p.append(f'<path d="M 40 300 H 1624" stroke="{BORDA}" stroke-width="3"/>')
    for k, t in enumerate(passos):
        x = 40 + k * 396
        p.append(f'<circle cx="{x}" cy="300" r="12" fill="{FOSF if k else MUDO}"/>')
        rs.append(rot(x - 150 if 0 < k < 4 else (x - 40 if k == 0 else x - 260), 326, t, w=300, tam=22, cor=TINTA, peso=600, alinha="center" if 0 < k < 4 else ("left" if k == 0 else "right")))
    rs.append(rot(0, 256, "a cascata", w=400, tam=20, cor=MUDO, peso=700))
    return slide("naopedir", 400, p, rs, eyebrow="A metade esquecida", titulo="O que não pedir")


def perfis_62():
    """6.2: quatro perfis, cada um com o seu jogo de exames."""
    p = [svg_abre(1664, 380, "Quatro perfis, cada um com o que pedir. Jovem federado: história e exame físico estruturados, e eletrocardiograma lido com critério de atleta. Jovem recreacional: anamnese no centro; eletrocardiograma razoável e amparado. Adulto iniciante sem sintoma: risco calculado; pressão, colesterol e glicemia; ergometria só se alto risco ou esforço vigoroso. Adulto com doença conhecida: avaliação funcional para prescrever, não para liberar")]
    rs = []
    linhas = [("t:medal", "Jovem federado", [("história e exame físico estruturados", OXID), ("eletro lido com critério de atleta", OXID)]),
              ("h:running", "Jovem recreacional", [("anamnese no centro", OXID), ("eletro: razoável e amparado", MUDO)]),
              ("h:man", "Adulto iniciante sem sintoma", [("risco calculado", OXID), ("pressão, colesterol, glicemia", OXID), ("ergometria se alto risco ou vigoroso", GLIC)]),
              ("t:heartbeat", "Adulto com doença conhecida", [("avaliação funcional para prescrever, não para liberar", AZUL)])]
    for k, (ic, t, chips) in enumerate(linhas):
        y = k * 96
        p.append(icone(ic, 0, y + 14, 52, TINTA))
        rs.append(rot(68, y + 20, t, w=330, tam=24, cor=TINTA, peso=700, lh=1.15))
        x = 410
        for c, cor in chips:
            w = min(26 + len(c) * 11.4, 1664 - x)
            fundo = {OXID: OXID_T, GLIC: GLIC_T, AZUL: AZUL_T, MUDO: PAPEL}[cor]
            p.append(caixa(x, y + 12, w, 60, cor, fundo, esp=2, rx=30))
            rs.append(rot(x + 13, y + 28, c, w=w - 26, tam=21, cor=TINTA, alinha="center"))
            x += w + 14
        if k < 3:
            p.append(f'<line x1="0" y1="{y + 88}" x2="1664" y2="{y + 88}" stroke="{BORDA}" stroke-width="1"/>')
    return slide("perfis", 380, p, rs, eyebrow="A decisão consolidada", titulo="Por perfil típico",
                 destaque="Sintoma no esforço, história familiar de morte súbita ou achado no exame físico transformam a triagem em investigação.",
                 destaque_cor="verm")


def respostas_62():
    """6.2: os três pedidos do começo, agora com a resposta."""
    p = [svg_abre(1664, 400, "Os três pedidos do começo, agora com resposta. O clube: o pedido é legítimo; anamnese de verdade, história familiar perguntada e eletrocardiograma lido com critério de atleta. O check-up completo: desmontar o completo, calcular o risco, progredir, e parar se houver sintoma no esforço. O preparador: exame sem leitura transfere risco; o que funciona é questionário, as perguntas certas, encaminhamento e desfibrilador")]
    rs = []
    itens = [("t:shirt-sport", "O clube", "legítimo", ["anamnese de verdade", "história familiar perguntada", "eletro lido com critério de atleta"], OXID, OXID_T),
             ("t:checklist", "O check-up completo", "desmontar o “completo”", ["calcular o risco", "progressão", "sintoma no esforço: para"], GLIC, GLIC_T),
             ("t:users-group", "O preparador", "exame sem leitura transfere risco", ["questionário e perguntas", "encaminhamento", "desfibrilador"], FOSF, FOSF_T)]
    for k, (ic, t, veredito, passos, cor, fundo) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 400, cor, CARTAO, esp=2, rx=16))
        p.append(f'<rect x="{x}" y="0" width="528" height="140" rx="16" fill="{fundo}"/>')
        p.append(icone(ic, x + 24, 22, 48, cor))
        rs += [rot(x + 88, 28, t, w=420, tam=27, cor=cor, peso=700, serif=True),
               rot(x + 24, 88, veredito, w=480, tam=23, cor=TINTA, peso=700)]
        for j, ps in enumerate(passos):
            y = 172 + j * 72
            p.append(icone("t:check", x + 24, y, 36, cor))
            rs.append(rot(x + 74, y + 4, ps, w=430, tam=23, cor=TINTA))
    return slide("respostas", 400, p, rs, eyebrow="Os três pedidos do começo", titulo="Três respostas",
                 destaque="Um plano de emergência ensaiado salva mais que uma gaveta de eletrocardiogramas que ninguém olhou.",
                 destaque_cor="petr")

# ---------------------------------------------------------------- 6.3

def ventriculo(p, cx, cy, re, ri, cor, fundo):
    """Corte do ventrículo esquerdo em esquema: anel de parede (re) e cavidade (ri)."""
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{re}" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{ri}" fill="{CARTAO}" stroke="{cor}" stroke-width="2"/>')


def ecg_t(p, x0, y0, w, cor, n=3, tipo="domo", amp=60, esp=4):
    """Traçado com onda T invertida: 'domo' (ponto J elevado e ST abaulado) ou 'plano' (ST reto e T invertida)."""
    passo = w / n
    d = [f"M {x0:.0f} {y0}"]
    for k in range(n):
        x = x0 + k * passo
        u = passo / 20
        d.append(f"L {x + 3*u:.0f} {y0} Q {x + 4.5*u:.0f} {y0 - amp*0.18:.0f} {x + 6*u:.0f} {y0}"
                 f" L {x + 8*u:.0f} {y0} L {x + 8.6*u:.0f} {y0 + amp*0.15:.0f} L {x + 9.4*u:.0f} {y0 - amp:.0f}"
                 f" L {x + 10.2*u:.0f} {y0 + amp*0.3:.0f}")
        if tipo == "domo":
            d.append(f" L {x + 10.8*u:.0f} {y0 - amp*0.22:.0f} Q {x + 12.2*u:.0f} {y0 - amp*0.42:.0f} {x + 13.4*u:.0f} {y0 - amp*0.05:.0f}"
                     f" Q {x + 14.8*u:.0f} {y0 + amp*0.62:.0f} {x + 16.5*u:.0f} {y0} L {x + 20*u:.0f} {y0}")
        else:
            d.append(f" L {x + 10.8*u:.0f} {y0} L {x + 12.2*u:.0f} {y0}"
                     f" Q {x + 14.2*u:.0f} {y0 + amp*0.62:.0f} {x + 16.2*u:.0f} {y0} L {x + 20*u:.0f} {y0}")
    p.append(f'<path d="{" ".join(d)}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linejoin="round"/>')


def laudos_63():
    """6.3: três laudos assustadores, e a corda entre o pânico e a banalização."""
    p = [svg_abre(1664, 400, "Três laudos com frases que assustam: hipertrofia ventricular esquerda; avaliar cardiomiopatia dilatada; considerar cardiopatia. Cada um descreve um coração que treinou muito, e, com as mesmas palavras, doenças que matam jovens em campo. Embaixo, os dois erros nas pontas de uma linha: entrar em pânico e banalizar; o raciocínio fica no meio")]
    rs = []
    frases = ["“hipertrofia ventricular esquerda”", "“avaliar cardiomiopatia dilatada”", "“considerar cardiopatia”"]
    for k, f in enumerate(frases):
        x = 40 + k * 548
        p.append(f'<path d="M {x} 0 H {x + 420} L {x + 480} 50 V 230 H {x} Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<path d="M {x + 420} 0 V 50 H {x + 480}" fill="none" stroke="{TINTA}" stroke-width="2"/>')
        rs.append(rot(x + 24, 20, "Laudo", w=300, tam=20, cor=MUDO, peso=700))
        for j in range(3):
            p.append(f'<line x1="{x + 24}" y1="{70 + j * 18}" x2="{x + 380 - j * 70}" y2="{70 + j * 18}" stroke="{BORDA}" stroke-width="5" stroke-linecap="round"/>')
        rs.append(rot(x + 24, 140, f, w=430, tam=25, cor=FOSF, peso=700, serif=True, lh=1.2))
    Y = 330
    p.append(f'<line x1="200" y1="{Y}" x2="1464" y2="{Y}" stroke="{MUDO}" stroke-width="3"/>')
    for x, t, cor in [(200, "entrar em pânico", FOSF), (1464, "banalizar", GLIC)]:
        p.append(f'<circle cx="{x}" cy="{Y}" r="14" fill="{cor}"/>')
        rs.append(rot(x - 200 if x == 200 else x - 20, Y + 26, t, w=240, tam=24, cor=cor, peso=700, alinha="center" if x == 200 else "left"))
    p.append(f'<circle cx="832" cy="{Y}" r="18" fill="{OXID}"/>')
    rs.append(rot(632, Y + 28, "o raciocínio", w=400, tam=24, cor=OXID, peso=700, alinha="center"))
    return slide("laudos", 400, p, rs, eyebrow="A zona cinzenta", titulo="Três laudos assustadores, nenhum é diagnóstico sozinho")


def perfis_63():
    """6.3: os três atletas e o número de cada laudo."""
    p = [svg_abre(1664, 380, "Três perfis típicos e o número de cada laudo. O zagueiro: hipertrofia ventricular esquerda, parede de 13 milímetros. A triatleta: cavidade de 59 milímetros, avaliar cardiomiopatia dilatada, sem sintoma. O adolescente negro do basquete: onda T invertida de V1 a V4, considerar cardiopatia")]
    rs = []
    itens = [("t:ball-football", "O zagueiro", "13 mm", "de parede: “hipertrofia ventricular esquerda”", GLIC, GLIC_T),
             ("t:swimming", "A triatleta", "59 mm", "de cavidade: “avaliar cardiomiopatia dilatada”; sem sintoma", OXID, OXID_T),
             ("t:ball-basketball", "O adolescente do basquete", "T invertida", "de V1 a V4, em atleta negro: “considerar cardiopatia”", FOSF, FOSF_T)]
    for k, (ic, t, n, d, cor, fundo) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 380, cor, fundo, esp=2, rx=18))
        p.append(icone(ic, x + 24, 24, 56, cor))
        rs += [rot(x + 96, 34, t, w=410, tam=27, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 24, 120, n, w=480, tam=72, cor=TINTA, peso=700, serif=True),
               rot(x + 24, 230, d, w=480, tam=23, cor=TINTA, lh=1.3)]
        if k == 2:
            ecg_t(p, x + 24, 340, 480, FOSF, n=3, tipo="domo", amp=44, esp=3)
    return slide("perfis", 380, p, rs, eyebrow="Três perfis típicos", titulo="O que os laudos dizem")


def remodelamento_63():
    """6.3: o corte do ventrículo do atleta ao lado do da hipertrófica, e as três doenças a separar (esquema)."""
    p = [svg_abre(1664, 400, "Esquema, fora de escala. À esquerda, o corte do ventrículo do atleta: cavidade maior e parede proporcional. Ao lado, o da cardiomiopatia hipertrófica: parede muito espessa e cavidade pequena. No meio, o conjunto do coração de atleta: cavidade maior, parede no limite ou um pouco acima, frequência de 40 a 50 batimentos, função normal ou melhor, capacidade funcional alta. À direita, as três doenças a separar: hipertrófica, dilatada e arritmogênica, que em fase inicial produzem os mesmos números")]
    rs = []
    ventriculo(p, 130, 170, 120, 88, OXID, OXID_T)
    ventriculo(p, 410, 170, 120, 44, FOSF, FOSF_T)
    rs += [rot(10, 304, "atleta", w=240, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(10, 336, "cavidade maior, parede proporcional", w=240, tam=19, cor=TINTA, alinha="center", lh=1.2),
           rot(290, 304, "hipertrófica", w=240, tam=24, cor=FOSF, peso=700, alinha="center"),
           rot(290, 336, "parede espessa, cavidade pequena", w=240, tam=19, cor=TINTA, alinha="center", lh=1.2),
           rot(10, 0, "esquema, fora de escala", w=500, tam=18, cor=MUDO)]
    p.append(caixa(580, 0, 520, 400, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(604, 18, "Coração de atleta: um conjunto", w=480, tam=26, cor=OXID, peso=700, serif=True))
    for k, t in enumerate(["cavidade maior", "parede no limite ou um pouco acima", "frequência baixa, 40 a 50 bpm", "função normal ou melhor", "capacidade funcional alta"]):
        y = 84 + k * 62
        p.append(icone("t:check", 604, y, 34, OXID))
        rs.append(rot(650, y + 2, t, w=430, tam=23, cor=TINTA))
    p.append(caixa(1140, 0, 524, 400, FOSF, CARTAO, esp=2, rx=16))
    rs.append(rot(1164, 18, "O que separar", w=480, tam=26, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["cardiomiopatia hipertrófica", "cardiomiopatia dilatada", "cardiomiopatia arritmogênica"]):
        y = 84 + k * 80
        p.append(caixa(1164, y, 476, 64, FOSF, FOSF_T, esp=2, rx=32))
        rs.append(rot(1180, y + 18, t, w=444, tam=23, cor=TINTA, peso=600, alinha="center"))
    rs.append(rot(1164, 330, "em fase inicial, produzem os números que o treino produz", w=476, tam=21, cor=FOSF, lh=1.3))
    return slide("remodelamento", 400, p, rs, eyebrow="O que o treino faz", titulo="Coração de atleta é um conjunto, não um número",
                 destaque="Em fase inicial, as três doenças produzem os números que o treino produz. O exame não separa; o raciocínio separa.",
                 destaque_cor="tinta")


def cavidade_63():
    """6.3: a faixa de cavidade de homens e mulheres numa régua em milímetros, e um em cada sete."""
    p = [svg_abre(1664, 360, "Régua de diâmetro diastólico do ventrículo esquerdo, de 35 a 75 milímetros, em 1.309 atletas de elite de 38 esportes. Nas mulheres, a cavidade variou de 38 a 66; nos homens, de 43 a 70. A faixa a partir de 60 milímetros, que num sedentário seria compatível com cardiomiopatia dilatada, foi alcançada por cerca de 15 por cento, um em cada sete. À direita, sete pessoas, uma destacada")]
    rs = []
    X0, X1, m0, m1 = 180, 1100, 35, 75
    fx = lambda mm: X0 + (mm - m0) / (m1 - m0) * (X1 - X0)
    p.append(f'<rect x="{fx(60):.0f}" y="0" width="{X1 - fx(60):.0f}" height="250" fill="{FOSF_T}"/>')
    rs.append(rot(fx(60) + 12, 8, "≥ 60 mm: num sedentário, compatível com dilatada", w=X1 - fx(60) - 20, tam=19, cor=FOSF, peso=700, lh=1.2))
    for k, (t, a, b, cor) in enumerate([("mulheres", 38, 66, AZUL), ("homens", 43, 70, OXID)]):
        y = 90 + k * 80
        rs.append(rot(0, y + 2, t, w=160, tam=24, cor=cor, peso=700, alinha="right"))
        p.append(f'<line x1="{fx(a):.0f}" y1="{y + 18}" x2="{fx(b):.0f}" y2="{y + 18}" stroke="{cor}" stroke-width="16" stroke-linecap="round"/>')
        rs += [rot(fx(a) - 60, y + 36, f"{a}", w=120, tam=20, cor=cor, peso=700, alinha="center"),
               rot(fx(b) - 60, y + 36, f"{b}", w=120, tam=20, cor=cor, peso=700, alinha="center")]
    p.append(f'<line x1="{X0}" y1="250" x2="{X1}" y2="250" stroke="{MUDO}" stroke-width="3"/>')
    for mm in range(35, 80, 5):
        p.append(f'<line x1="{fx(mm):.0f}" y1="250" x2="{fx(mm):.0f}" y2="262" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(fx(mm) - 40, 268, f"{mm}", w=80, tam=19, cor=MUDO, alinha="center"))
    rs.append(rot(X0, 300, "diâmetro diastólico do ventrículo esquerdo, em mm · 1.309 atletas de elite, 38 esportes", w=1000, tam=19, cor=MUDO))
    for k in range(7):
        x = 1200 + (k % 4) * 116
        y = 30 + (k // 4) * 130
        p.append(icone("h:person", x, y, 96, FOSF if k == 0 else CINZA))
    rs += [rot(1200, 290, "≈ 15%: um em cada sete", w=464, tam=26, cor=FOSF, peso=700, serif=True)]
    return slide("cavidade", 360, p, rs, eyebrow="A cavidade de atletas de elite, 1999", titulo="A cavidade que assusta o laudo",
                 destaque="A dobradiça: na ausência de disfunção sistólica, é provavelmente adaptação. E 52% de fração de ejeção num triatleta não é 52% num sedentário.",
                 destaque_cor="petr", fonte="Pelliccia e colaboradores · Annals of Internal Medicine 1999")


def quem_63():
    """6.3: quatro réguas, uma por variável: sexo, ancestralidade, idade, tamanho e esporte."""
    p = [svg_abre(1664, 400, "Quatro cartões, cada um com uma régua de normalidade. Sexo: em 600 mulheres de elite, a parede ficou entre 6 e 12 milímetros, nenhuma acima; acima de 12 na mulher, investigar. Ancestralidade: parede acima de 12 milímetros em 18 por cento dos atletas negros e 4 por cento dos brancos; média de 11,3 contra 10,0; régua de branco gera falso-positivo no negro. Idade: em 720 adolescentes de elite, os limites são menores; o teto de 16 do adulto não vale. Tamanho e esporte: indexar; remo e ciclismo nos extremos; zagueiro não é remador olímpico")]
    rs = []
    W = 818
    # sexo
    p.append(caixa(0, 0, W, 190, AZUL, CARTAO, esp=2, rx=14))
    rs += [rot(20, 14, "Sexo", w=200, tam=26, cor=AZUL, peso=700, serif=True),
           rot(200, 18, "600 mulheres de elite", w=600, tam=21, cor=MUDO)]
    fx = lambda mm: 40 + (mm - 4) / (18 - 4) * 560
    p.append(f'<line x1="{fx(4):.0f}" y1="110" x2="{fx(18):.0f}" y2="110" stroke="{BORDA}" stroke-width="4"/>')
    p.append(f'<line x1="{fx(6):.0f}" y1="110" x2="{fx(12):.0f}" y2="110" stroke="{AZUL}" stroke-width="16" stroke-linecap="round"/>')
    p.append(f'<line x1="{fx(12):.0f}" y1="82" x2="{fx(12):.0f}" y2="138" stroke="{FOSF}" stroke-width="3"/>')
    rs += [rot(fx(6) - 40, 134, "6", w=80, tam=19, cor=AZUL, alinha="center"), rot(fx(12) - 40, 142, "12 mm", w=80, tam=19, cor=FOSF, peso=700, alinha="center"),
           rot(640, 70, "nenhuma acima de 12: acima, investigar", w=160, tam=19, cor=FOSF, lh=1.25)]
    # ancestralidade
    p.append(caixa(846, 0, W, 190, GLIC, CARTAO, esp=2, rx=14))
    rs += [rot(866, 14, "Ancestralidade", w=300, tam=26, cor=GLIC, peso=700, serif=True),
           rot(1130, 18, "parede acima de 12 mm", w=500, tam=21, cor=MUDO)]
    for k, (t, v) in enumerate([("negros", 18), ("brancos", 4)]):
        y = 70 + k * 50
        rs.append(rot(866, y + 4, t, w=110, tam=21, cor=TINTA, peso=600))
        p.append(f'<rect x="990" y="{y}" width="{v * 18}" height="34" rx="3" fill="{GLIC if k == 0 else MUDO}"/>')
        rs.append(rot(1000 + v * 18, y + 4, f"{v}%", w=80, tam=22, cor=TINTA, peso=700))
    rs.append(rot(1420, 64, "régua de branco gera falso-positivo no negro", w=230, tam=19, cor=GLIC, lh=1.25))
    rs.append(rot(866, 166, "média 11,3 × 10,0 mm", w=500, tam=18, cor=MUDO))
    # idade
    p.append(caixa(0, 210, W, 190, OXID, CARTAO, esp=2, rx=14))
    rs += [rot(20, 224, "Idade", w=200, tam=26, cor=OXID, peso=700, serif=True),
           rot(200, 228, "720 adolescentes de elite", w=600, tam=21, cor=MUDO),
           rot(20, 290, "limites fisiológicos menores que no adulto: o teto de 16 mm do adulto de elite não vale", w=560, tam=22, cor=TINTA, lh=1.3)]
    p.append(icone("h:boy-1015y", 640, 270, 100, OXID))
    # tamanho e esporte
    p.append(caixa(846, 210, W, 190, MUDO, CARTAO, esp=2, rx=14))
    rs += [rot(866, 224, "Tamanho e esporte", w=400, tam=26, cor=TINTA, peso=700, serif=True),
           rot(866, 290, "indexar pela superfície corporal; remo e ciclismo nos extremos", w=500, tam=22, cor=TINTA, lh=1.3),
           rot(866, 356, "zagueiro não é remador olímpico", w=500, tam=20, cor=MUDO)]
    p.append(icone("t:ruler-measure", 1440, 270, 90, MUDO))
    return slide("quem", 400, p, rs, eyebrow="O erro mais evitável", titulo="Normal para quem?",
                 destaque="A régua não pode ser afrouxada no atleta negro, porque a hipertrófica pesa nas mortes súbitas. Precisa ser a régua certa.",
                 destaque_cor="verm", fonte="Pelliccia 1996 · Basavarajaiah 2008 · Sharma 2002")


def discriminadores_63():
    """6.3: cinco pares, cada achado do atleta frente ao achado da doença."""
    p = [svg_abre(1664, 380, "Cinco pares de discriminadores, cada um com o que aponta para atleta à esquerda e para doença à direita. Parede e cavidade crescem juntas, contra parede espessa com cavidade pequena. Hipertrofia simétrica, contra assimétrica e septal. Relaxamento normal ou melhor, contra disfunção diastólica. Consumo de oxigênio acima de 50 ou acima de 120 por cento do previsto, contra capacidade baixa. Sem realce tardio na ressonância, contra fibrose, ou história familiar"), defs(OXID, FOSF)]
    rs = [rot(0, 0, "Aponta para atleta", w=660, tam=26, cor=OXID, peso=700, serif=True, alinha="right"),
          rot(1004, 0, "Aponta para doença", w=660, tam=26, cor=FOSF, peso=700, serif=True)]
    pares = [("parede e cavidade crescem juntas", "parede espessa, cavidade pequena", "geometria"),
             ("hipertrofia simétrica", "assimétrica, septal", "distribuição"),
             ("relaxamento normal ou melhor", "disfunção diastólica", "diástole"),
             ("VO₂ > 50 ou > 120% do previsto", "capacidade baixa", "ergoespirometria"),
             ("sem realce tardio", "fibrose na ressonância; história familiar", "ressonância e família")]
    for k, (a, b, eixo) in enumerate(pares):
        y = 52 + k * 66
        p.append(caixa(0, y, 660, 54, OXID, OXID_T, esp=2, rx=27))
        rs.append(rot(20, y + 13, a, w=620, tam=22, cor=TINTA, alinha="right"))
        p.append(caixa(1004, y, 660, 54, FOSF, FOSF_T, esp=2, rx=27))
        rs.append(rot(1024, y + 13, b, w=620, tam=22, cor=TINTA))
        p.append(seta(820, y + 27, 680, y + 27, OXID, "m0", esp=3))
        p.append(seta(844, y + 27, 984, y + 27, FOSF, "m1", esp=3))
        rs.append(rot(690, y - 2, eixo, w=284, tam=18, cor=MUDO, alinha="center"))
    return slide("discriminadores", 380, p, rs, eyebrow="Por que o cardiologista pede o que pede", titulo="Os discriminadores",
                 destaque="“Mas o eco dele está normal” não encerra a conversa quando há sintoma ou história familiar.",
                 destaque_cor="tinta", fonte="Ergoespirometria: Sharma e colaboradores, JACC 2000")


def destreino_63():
    """6.3: antes e depois de parar, em índice, e a fração que manteve a cavidade grande."""
    p = [svg_abre(1664, 360, "Antes e depois de um período longo sem treinar, em índice com o antes igual a cem, em 40 atletas da zona cinzenta. A espessura da parede caiu 15 por cento e voltou ao normal em todos. A cavidade caiu 7 por cento. Numa barra de cem por cento, 22 por cento dos atletas mantiveram cavidade de 60 milímetros ou mais")]
    rs = []
    Yb, esc = 300, 2.4
    grupos = [("Parede", -15, "voltou ao normal em todos", OXID), ("Cavidade", -7, "", AZUL)]
    for k, (t, dv, nota, cor) in enumerate(grupos):
        x = 60 + k * 420
        for j, (v, rot_) in enumerate([(100, "antes"), (100 + dv, "depois")]):
            bx = x + j * 140
            h = v * esc
            p.append(f'<rect x="{bx}" y="{Yb - h:.0f}" width="110" height="{h:.0f}" rx="4" fill="{cor if j else CINZA}"/>')
            rs.append(rot(bx - 20, Yb + 8, rot_, w=150, tam=20, cor=MUDO, alinha="center"))
        rs += [rot(x, 0, t, w=260, tam=26, cor=cor, peso=700, serif=True),
               rot(x + 140, Yb - (100 + dv) * esc - 48, f"{dv}%".replace("-", "−"), w=110, tam=30, cor=cor, peso=700, alinha="center", serif=True)]
        if nota:
            rs.append(rot(x + 270, 60, nota, w=140, tam=19, cor=OXID, lh=1.25))
    p.append(f'<line x1="40" y1="{Yb}" x2="880" y2="{Yb}" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(40, Yb + 36, "índice, antes = 100", w=400, tam=18, cor=MUDO))
    p.append(caixa(960, 60, 704, 240, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(984, 80, "Mantiveram cavidade de 60 mm ou mais", w=660, tam=24, cor=GLIC, peso=700, serif=True))
    p.append(f'<rect x="984" y="150" width="656" height="56" rx="6" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<rect x="984" y="150" width="{656 * 0.22:.0f}" height="56" rx="6" fill="{GLIC}"/>')
    rs += [rot(994, 162, "22%", w=130, tam=26, cor=PAPEL, peso=700, alinha="center"),
           rot(984, 224, "dos 40 atletas, depois de 1 a 13 anos sem treinar", w=660, tam=21, cor=TINTA)]
    return slide("destreino", 360, p, rs, eyebrow="O destreino, 2002", titulo="O teste que não é exame: parar de treinar",
                 destaque="40 atletas, 1 a 13 anos sem treinar. Na clínica, 8 a 12 semanas e regressão parcial: a última carta, porque custa uma temporada.",
                 destaque_cor="ambar", fonte="Pelliccia e colaboradores · Circulation 2002")


def ondat_63():
    """6.3: os dois traçados com onda T invertida: o padrão em domo anterior e a inversão inferolateral."""
    p = [svg_abre(1664, 380, "Dois traçados com onda T invertida. À esquerda, a variante descrita: inversão anterior, de V1 a V4, em atleta negro, precedida de elevação do ponto J e de segmento ST abaulado, em domo. À direita, a que se investiga sempre: inversão nas derivações inferiores e laterais, em qualquer atleta, com associação real com cardiomiopatia")]
    rs = []
    blocos = [(0, "Variante descrita", "domo", ["anterior, V1 a V4", "em atleta negro", "com elevação do ponto J", "e ST abaulado, “em domo”"], OXID, OXID_T),
              (864, "Investiga sempre", "plano", ["inferior e lateral", "em qualquer atleta", "associação real com cardiomiopatia"], FOSF, FOSF_T)]
    for x, t, tipo, itens, cor, fundo in blocos:
        p.append(caixa(x, 0, 800, 380, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, 18, t, w=740, tam=28, cor=cor, peso=700, serif=True))
        p.append(f'<rect x="{x + 24}" y="70" width="752" height="140" rx="8" fill="{CARTAO}"/>')
        ecg_t(p, x + 40, 160, 720, TINTA, n=3, tipo=tipo, amp=70, esp=4)
        for k, it in enumerate(itens):
            col, lin = k % 2, k // 2
            xx, y = x + 24 + col * 380, 236 + lin * 60
            p.append(f'<circle cx="{xx + 8}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(xx + 26, y, it, w=350, tam=22, cor=TINTA, lh=1.2))
    return slide("ondat", 380, p, rs, eyebrow="Onda T invertida, 2018", titulo="A localização da onda T muda tudo",
                 destaque="100 atletas com T invertida e eco normal: cardiomiopatia em 21% (30% nos brancos, 12% nos negros). Investigação negativa não é alta; é seguimento.",
                 destaque_cor="verm", fonte="Sheikh e colaboradores · Circulation 2018")


def aritmetica_63():
    """6.3: o funil de 3.500 atletas até 3 com hipertrófica (fora de escala)."""
    p = [svg_abre(1664, 360, "Funil fora de escala. De 3.500 atletas de elite sem sintoma, 53, ou 1,5 por cento, tinham parede de 13 a 16 milímetros. Desses, 3, ou 0,08 por cento do total, tinham quadro compatível com cardiomiopatia hipertrófica. A maior parte da zona cinzenta é adaptação; o falso-positivo é a regra")]
    rs = []
    niveis = [("3.500", "atletas de elite sem sintoma", 1200, TINTA, PAPEL), ("53", "com parede de 13 a 16 mm (1,5%)", 760, GLIC, GLIC_T),
              ("3", "compatíveis com hipertrófica (0,08%)", 320, FOSF, FOSF_T)]
    for k, (n, t, w, cor, fundo) in enumerate(niveis):
        y = k * 112
        x = (1200 - w) / 2
        wn = niveis[k + 1][2] if k < 2 else w * 0.7
        xn = (1200 - wn) / 2
        p.append(f'<path d="M {x:.0f} {y} H {x + w:.0f} L {xn + wn:.0f} {y + 100} H {xn:.0f} Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(x, y + 20, n, w=w, tam=48, cor=cor, peso=700, alinha="center", serif=True))
        rs.append(rot(1240, y + 30, t, w=424, tam=24, cor=TINTA, peso=600, lh=1.2))
        p.append(f'<line x1="{x + w - 30:.0f}" y1="{y + 50}" x2="1226" y2="{y + 50}" stroke="{BORDA}" stroke-width="2"{TRACO}/>')
    rs.append(rot(0, 336, "funil fora de escala", w=400, tam=18, cor=MUDO))
    return slide("aritmetica", 360, p, rs, eyebrow="Rastreio de 3.500 atletas, 2008", titulo="Por que o falso-positivo é a regra",
                 destaque="Achado não é afastamento automático. Mas o falso-negativo mata: síncope no esforço, sintoma no esforço e história familiar passam por cima de qualquer número.",
                 destaque_cor="verm", fonte="Basavarajaiah e colaboradores · JACC 2008")


def condutas_63():
    """6.3: os três laudos numa faixa que vai da adaptação à doença, com a conduta de cada um."""
    p = [svg_abre(1664, 400, "Uma faixa que vai da adaptação provável, à esquerda, à doença, à direita, passando pela zona cinzenta. A triatleta, com cavidade de 59 milímetros, fica no lado da adaptação, comum em endurance: com função normal e sem sintoma, provável adaptação, com seguimento. O adolescente com onda T anterior fica na variante descrita: ecocardiograma e seguimento, e investiga se houver sintoma, família ou T inferolateral. O zagueiro, com 13 milímetros, fica na entrada da zona cinzenta: avaliação cardiológica completa, nem proibir nem dizer que está tudo bem")]
    rs = []
    p.append(f'<defs><linearGradient id="faixa" x1="0" x2="1"><stop offset="0" stop-color="{OXID}"/><stop offset="0.5" stop-color="{GLIC}"/><stop offset="1" stop-color="{FOSF}"/></linearGradient></defs>')
    p.append(f'<rect x="0" y="40" width="1664" height="26" rx="13" fill="url(#faixa)"/>')
    rs += [rot(0, 0, "adaptação provável", w=400, tam=21, cor=OXID, peso=700), rot(632, 0, "zona cinzenta", w=400, tam=21, cor=GLIC, peso=700, alinha="center"),
           rot(1264, 0, "doença", w=400, tam=21, cor=FOSF, peso=700, alinha="right")]
    itens = [(260, "A triatleta, 59 mm", "comum em endurance", "com função normal e sem sintoma: provável adaptação, com seguimento", OXID),
             (640, "O adolescente, T anterior", "variante descrita", "eco e seguimento; investiga se sintoma, família ou T inferolateral", GLIC),
             (1000, "O zagueiro, 13 mm", "entrada da zona cinzenta", "avaliação cardiológica completa; nem proibir nem “relaxa”", GLIC)]
    for k, (cx, t, onde, cond, cor) in enumerate(itens):
        x = k * 568
        p.append(f'<circle cx="{cx}" cy="53" r="20" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
        p.append(f'<path d="M {cx} 76 C {cx} 110, {x + 264} 96, {x + 264} 120" fill="none" stroke="{TINTA}" stroke-width="2"/>')
        p.append(caixa(x, 120, 528, 280, cor, CARTAO, esp=2, rx=16))
        rs += [rot(x + 24, 138, t, w=480, tam=27, cor=TINTA, peso=700, serif=True),
               rot(x + 24, 184, onde, w=480, tam=22, cor=cor, peso=700),
               rot(x + 24, 236, cond, w=480, tam=23, cor=TINTA, lh=1.3)]
    return slide("condutas", 400, p, rs, eyebrow="Os três laudos do começo", titulo="O que a aula permite dizer",
                 destaque="O cansaço da triatleta continua precisando de explicação: carga, sono, ferro, alimentação.",
                 destaque_cor="petr")

# ---------------------------------------------------------------- 6.4

def frases_64():
    """6.4: as duas frases de depois do caso, em direções opostas, e os cinco erros."""
    p = [svg_abre(1664, 400, "Duas frases que se ouvem depois de todo caso, em direções opostas. À esquerda: foi azar, não dava para fazer nada, que leva ao conformismo. À direita: com certeza não fizeram os exames direito, que leva à ilusão de que exigir exame basta. Embaixo, cinco erros em fila; o quinto, o da hora, é o que mais mata"), defs(MUDO)]
    rs = []
    bal = [(0, "“Foi azar, não dava para fazer nada.”", "leva ao conformismo", GLIC, GLIC_T), (904, "“Com certeza não fizeram os exames direito.”", "leva à ilusão de que exigir exame basta", AZUL, AZUL_T)]
    for x, q, d, cor, fundo in bal:
        tx = x + 120 if x == 0 else x + 640
        p.append(f'<path d="M {x + 16} 0 H {x + 744} Q {x + 760} 0 {x + 760} 16 V 144 Q {x + 760} 160 {x + 744} 160 H {tx + 40} L {tx} 200 L {tx + 10} 160 H {x + 16} Q {x} 160 {x} 144 V 16 Q {x} 0 {x + 16} 0 Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(x + 28, 26, q, w=704, tam=30, cor=cor, peso=700, serif=True, lh=1.2))
        rs.append(rot(x + 28 if x == 0 else x + 28, 206, d, w=704, tam=22, cor=TINTA, alinha="left" if x == 0 else "right"))
    p.append(seta(820, 80, 790, 80, MUDO, "m0", esp=3))
    p.append(seta(844, 80, 874, 80, MUDO, "m0", esp=3))
    Y = 330
    p.append(f'<line x1="100" y1="{Y}" x2="1564" y2="{Y}" stroke="{BORDA}" stroke-width="3"/>')
    for k in range(5):
        x = 100 + k * 366
        r = 22 if k < 4 else 36
        p.append(f'<circle cx="{x}" cy="{Y}" r="{r}" fill="{MUDO if k < 4 else FOSF}"/>')
        rs.append(rot(x - 30, Y - (16 if k < 4 else 22), str(k + 1), w=60, tam=24 if k < 4 else 34, cor=PAPEL, peso=700, alinha="center", serif=True))
    rs.append(rot(1300, Y + 42, "o quinto é o que mais mata", w=364, tam=22, cor=FOSF, peso=700, alinha="right"))
    rs.append(rot(0, Y + 42, "cinco erros", w=400, tam=22, cor=MUDO, peso=700))
    return slide("frases", 400, p, rs, eyebrow="Depois de todo caso", titulo="Duas frases erradas, em direções opostas")


def desfechos_64():
    """6.4: dois colapsos em campo, em duas linhas do tempo depois da queda."""
    p = [svg_abre(1664, 380, "Duas linhas do tempo a partir da queda, sem escala de minutos. Em cima, 2004, no Brasil: um jogador profissional, avaliado e acompanhado, caiu em campo e morreu. Embaixo, 2021, na Eurocopa: um jogador profissional caiu, recebeu compressão em segundos, foi desfibrilado no gramado, sobreviveu e voltou a jogar. Os dois tinham exame de admissão; a diferença esteve nos minutos seguintes à queda")]
    rs = []
    linhas = [("2004, Brasil", [("caiu em campo", MUDO), ("morreu", FOSF)], FOSF, 40),
              ("2021, Eurocopa", [("caiu em campo", MUDO), ("compressão em segundos", OXID), ("desfibrilado no gramado", OXID), ("sobreviveu e voltou a jogar", OXID)], OXID, 220)]
    for t, marcos, cor, y in linhas:
        rs += [rot(0, y + 10, t, w=280, tam=28, cor=cor, peso=700, serif=True),
               rot(0, y + 52, "profissional, avaliado e acompanhado", w=280, tam=19, cor=MUDO, lh=1.25)]
        p.append(f'<line x1="320" y1="{y + 40}" x2="1640" y2="{y + 40}" stroke="{cor}" stroke-width="5"/>')
        n = len(marcos)
        for k, (m, c) in enumerate(marcos):
            x = 340 + k * (1280 / max(n - 1, 1)) if n > 2 else (340 if k == 0 else 1600)
            p.append(f'<circle cx="{x:.0f}" cy="{y + 40}" r="16" fill="{c}"/>')
            rs.append(rot(x - 150 if 0 < k < n - 1 else (x - 30 if k == 0 else x - 270), y + 68, m, w=300 if 0 < k < n - 1 else 300, tam=22, cor=TINTA, peso=600, alinha="center" if 0 < k < n - 1 else ("left" if k == 0 else "right")))
    rs.append(rot(320, 350, "a linha começa na queda; sem escala de minutos", w=700, tam=18, cor=MUDO))
    return slide("desfechos", 380, p, rs, eyebrow="Dois colapsos em campo", titulo="A diferença esteve nos minutos seguintes",
                 destaque="A diferença entre os desfechos não foi o exame de admissão.", destaque_cor="tinta")


def frequencia_64():
    """6.4: a taxa geral e a do basquete na mesma escala, e o número inglês ao lado."""
    p = [svg_abre(1664, 360, "À esquerda, duas barras na mesma escala, mortes súbitas cardíacas por 100 mil atletas universitários por ano: no geral, 1 em 53.703, cerca de 1,9; no basquete masculino da primeira divisão, 1 em 5.200, cerca de 19, dez vezes mais. À direita, à parte, porque a conta é outra: 6,8 por 100 mil adolescentes do futebol inglês, no seguimento depois do rastreio")]
    rs = []
    X0, esc = 330, 32
    for k, (t, frac, v, cor, ic) in enumerate([("no geral", "1 : 53.703", 1.86, MUDO, "t:school"), ("basquete masculino, primeira divisão", "1 : 5.200", 19.2, FOSF, "t:ball-basketball")]):
        y = 40 + k * 130
        p.append(icone(ic, 0, y + 14, 48, cor))
        rs.append(rot(60, y + 6, t, w=250, tam=22, cor=TINTA, peso=600, lh=1.2))
        p.append(f'<rect x="{X0}" y="{y}" width="{max(v * esc, 6):.0f}" height="80" rx="4" fill="{cor}"/>')
        rs += [rot(X0 + v * esc + 18, y + 6, frac, w=260, tam=34, cor=cor if cor != MUDO else TINTA, peso=700, serif=True),
               rot(X0 + v * esc + 18, y + 50, f"≈ {v:.1f}".replace(".", ",") + " por 100 mil por ano", w=300, tam=19, cor=MUDO)]
    p.append(f'<line x1="{X0}" y1="20" x2="{X0}" y2="300" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(X0, 310, "atletas universitários americanos, por ano", w=600, tam=19, cor=MUDO))
    rs.append(rot(X0 + 19.2 * esc - 160, 252, "dez vezes mais", w=160, tam=21, cor=FOSF, peso=700, alinha="right"))
    p.append(caixa(1290, 20, 374, 300, GLIC, GLIC_T, esp=2, rx=16))
    p.append(icone("t:ball-football", 1314, 44, 48, GLIC))
    rs += [rot(1314, 110, "6,8", w=330, tam=64, cor=GLIC, peso=700, serif=True),
           rot(1314, 196, "por 100 mil adolescentes do futebol inglês, no seguimento depois do rastreio", w=330, tam=20, cor=TINTA, lh=1.3)]
    return slide("frequencia", 360, p, rs, eyebrow="Erro um: a frequência", titulo="Raro, e concentrado",
                 destaque="Raro não é improvável numa vida institucional. Evento raro, fatal e com resposta conhecida é exatamente o evento para o qual se prepara.",
                 destaque_cor="petr", fonte="Harmon, Circulation 2015 · Malhotra, NEJM 2018")


def causa_64():
    """6.4: duas barras de 100%, uma por conjunto de dados, mostrando quadros diferentes."""
    p = [svg_abre(1664, 380, "Duas barras de cem por cento. Em cima, o registro de Maron, de 2009: 1.866 mortes de 1980 a 2006, montado em boa parte a partir de notícias; entre as causas cardiovasculares, hipertrófica cerca de 36 por cento, anomalia coronariana cerca de 17 por cento, e o restante. Embaixo, as autópsias revisadas de 2014, com cada caso julgado por um painel: o achado mais comum foi autópsia negativa, coração estruturalmente normal, em cerca de 31 por cento; a hipertrófica apareceu pouco")]
    rs = []
    X0, W = 0, 1664
    barras = [("O registro de Maron, 2009", "1.866 mortes, 1980 a 2006; montado em boa parte a partir de notícias", [(36, "hipertrófica ≈ 36%", FOSF), (17, "anomalia coronariana ≈ 17%", GLIC), (47, "outras causas", CINZA)], 0),
              ("As autópsias revisadas, 2014", "cada caso julgado por painel; a hipertrófica apareceu pouco", [(31, "autópsia negativa ≈ 31%", AZUL), (69, "outras causas, entre elas a hipertrófica", CINZA)], 200)]
    for t, sub, partes, y in barras:
        rs += [rot(0, y, t, w=800, tam=27, cor=TINTA, peso=700, serif=True), rot(820, y + 6, sub, w=844, tam=20, cor=MUDO, alinha="right")]
        x = X0
        for v, lab, cor in partes:
            w = v / 100 * W
            p.append(f'<rect x="{x:.0f}" y="{y + 50}" width="{w - 4:.0f}" height="80" rx="4" fill="{cor}"/>')
            rs.append(rot(x + 16, y + 74, lab, w=w - 30, tam=22, cor=PAPEL if cor != CINZA else TINTA, peso=700))
            x += w
    return slide("causa", 380, p, rs, eyebrow="Erro dois: a causa", titulo="Dois bons estudos, dois quadros",
                 destaque="Parte relevante das mortes é doença elétrica. Isso valoriza o eletrocardiograma, limita a imagem e explica por que nenhum exame zera o risco.",
                 destaque_cor="tinta")


def quem_64():
    """6.4: seis perfis em volta do jovem de elite, que não é o único."""
    p = [svg_abre(1664, 420, "No centro, o jovem de elite, o perfil em que todo mundo pensa. Em volta, seis perfis que também morrem: acima dos 35, em que a causa dominante é coronariana; o destreinado que volta forte, parado anos e direto para o vigoroso; a commotio cordis, impacto no peito com coração normal, que nenhum exame prevê; o colapso por calor, que não é cardíaco; a miocardite depois de infecção; e o amador de fim de semana, o mais numeroso e o menos coberto")]
    rs = []
    p.append(f'<circle cx="832" cy="210" r="110" fill="{PAPEL}" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
    p.append(icone("t:medal", 792, 130, 80, MUDO))
    rs.append(rot(732, 224, "o jovem de elite", w=200, tam=22, cor=MUDO, peso=700, alinha="center"))
    itens = [("h:man", "Acima dos 35", "a causa dominante é coronariana", FOSF), ("t:barbell", "O destreinado que volta forte", "parado anos, direto para o vigoroso", FOSF),
             ("t:target", "Commotio cordis", "impacto no peito, coração normal; nenhum exame prevê", GLIC), ("t:temperature", "Calor", "colapso por hipertermia, não cardíaco", GLIC),
             ("t:mood-sick", "Miocardite", "depois de infecção", GLIC), ("t:run", "O amador de fim de semana", "o mais numeroso e o menos coberto", OXID)]
    pos = [(0, 0), (0, 145), (0, 290), (1124, 0), (1124, 145), (1124, 290)]
    for (x, y), (ic, t, d, cor) in zip(pos, itens):
        p.append(caixa(x, y, 540, 130, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 18, y + 22, 48, cor))
        rs += [rot(x + 80, y + 16, t, w=440, tam=24, cor=cor, peso=700, lh=1.15), rot(x + 80, y + 62, d, w=440, tam=20, cor=TINTA, lh=1.25)]
        cx = x + 540 if x == 0 else x
        p.append(f'<line x1="{cx}" y1="{y + 65}" x2="{832 + (-110 if x == 0 else 110) * 0.8:.0f}" y2="{210 + (y - 145) * 0.5:.0f}" stroke="{BORDA}" stroke-width="2"/>')
    return slide("quem", 420, p, rs, eyebrow="Erro três: quem morre", titulo="Não só o jovem de elite")


def rastreio_64():
    """6.4: o que o rastreio achou e o que veio depois, em fluxo."""
    p = [svg_abre(1664, 380, "Fluxo de 11.168 adolescentes rastreados com eletrocardiograma e ecocardiograma. Para cima, 42 com doença associada a morte súbita, 0,38 por cento: o rastreio funcionou. Para a frente, no seguimento, 8 mortes cardíacas; 6 delas em quem tinha rastreio normal, desenhadas como seis corações em vermelho e dois em cinza"), defs(OXID, FOSF)]
    rs = []
    p.append(caixa(0, 120, 380, 140, TINTA, CARTAO, esp=3, rx=16))
    rs += [rot(0, 136, "11.168", w=380, tam=56, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(20, 210, "adolescentes com eletro e eco", w=340, tam=21, cor=TINTA, alinha="center")]
    p.append(f'<path d="M 380 160 C 460 160, 470 70, 560 70" fill="none" stroke="{OXID}" stroke-width="4" marker-end="url(#m0)"/>')
    p.append(f'<path d="M 380 230 C 460 230, 470 300, 560 300" fill="none" stroke="{FOSF}" stroke-width="4" marker-end="url(#m1)"/>')
    p.append(caixa(580, 0, 1084, 140, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(604, 20, "42", w=150, tam=64, cor=OXID, peso=700, serif=True),
           rot(760, 26, "com doença associada a morte súbita (0,38%)", w=880, tam=24, cor=TINTA, peso=600),
           rot(760, 70, "o rastreio funcionou", w=880, tam=22, cor=OXID, peso=700)]
    p.append(caixa(580, 220, 1084, 160, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(604, 236, "no seguimento: 8 mortes cardíacas", w=640, tam=24, cor=TINTA, peso=600),
           rot(604, 290, "6 de 8 tinham rastreio normal", w=520, tam=30, cor=FOSF, peso=700, serif=True)]
    for k in range(8):
        p.append(icone("t:heart", 1150 + (k % 4) * 120, 236 + (k // 4) * 70, 56, FOSF if k < 6 else CINZA))
    return slide("rastreio", 380, p, rs, eyebrow="Erro quatro: o que o rastreio faz", titulo="Rastreio não é vacina",
                 destaque="Reduz, não elimina. Fotografa um momento, e doença genética se expressa com o tempo.",
                 destaque_cor="verm", fonte="Malhotra e colaboradores · New England Journal of Medicine 2018")


def consequencias_64():
    """6.4: do dado às três consequências."""
    p = [svg_abre(1664, 400, "À esquerda, o dado: o rastreio reduz, não elimina. Dele saem três consequências. Rastreio exige seguimento: exame de entrada arquivado numa pasta é quase decorativo. Sintoma novo vale mais que exame antigo: mas ele fez todos os exames é a frase mais perigosa. A preparação para o evento não é opcional: não é pessimismo, é a conclusão lógica do dado"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 120, 380, 160, TINTA, TINTA, esp=0, rx=18))
    rs.append(rot(24, 150, "O rastreio reduz, não elimina", w=332, tam=30, cor=PAPEL, peso=700, serif=True, alinha="center", lh=1.2))
    itens = [("t:calendar", "Rastreio exige seguimento", "exame de entrada arquivado numa pasta é quase decorativo", OXID, OXID_T),
             ("t:alert-triangle", "Sintoma novo vale mais que exame antigo", "“mas ele fez todos os exames” é a frase mais perigosa", FOSF, FOSF_T),
             ("t:first-aid-kit", "A preparação para o evento não é opcional", "não é pessimismo; é a conclusão lógica do dado", GLIC, GLIC_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(itens):
        y = k * 140
        p.append(f'<path d="M 380 200 C 440 200, 440 {y + 60}, 500 {y + 60}" fill="none" stroke="{MUDO}" stroke-width="3" marker-end="url(#m0)"/>')
        p.append(caixa(520, y, 1144, 120, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 544, y + 32, 56, cor))
        rs += [rot(624, y + 18, t, w=1010, tam=27, cor=cor, peso=700, serif=True), rot(624, y + 66, d, w=1010, tam=22, cor=TINTA)]
    return slide("consequencias", 400, p, rs, eyebrow="O núcleo da aula", titulo="Três consequências")


def reconhecer_64():
    """6.4: a pergunta de reconhecimento e o que não a exclui."""
    p = [svg_abre(1664, 380, "Um losango de decisão: caiu sem contato e não responde? Sim leva direto à regra: é parada até prova em contrário; começa a compressão e alguém busca o desfibrilador. Embaixo, três coisas que enganam e não excluem a parada: abalos que parecem convulsão, a respiração agônica, o gasping, e a frase está respirando, então não é parada"), defs(FOSF)]
    rs = []
    p.append(f'<path d="M 280 0 L 560 130 L 280 260 L 0 130 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(90, 92, "Caiu sem contato e não responde?", w=380, tam=27, cor=FOSF, peso=700, alinha="center", serif=True, lh=1.2))
    p.append(seta(570, 130, 690, 130, FOSF, "m0", esp=5))
    rs.append(rot(580, 90, "sim", w=100, tam=22, cor=FOSF, peso=700, alinha="center"))
    p.append(caixa(710, 20, 954, 220, FOSF, FOSF, esp=0, rx=18))
    p.append(icone("t:heartbeat", 740, 50, 64, PAPEL))
    rs += [rot(824, 50, "Parada até prova em contrário", w=810, tam=32, cor=PAPEL, peso=700, serif=True),
           rot(740, 136, "começa a compressão; alguém busca o desfibrilador. Cada minuto de atraso custa sobrevida.", w=890, tam=23, cor=PAPEL, lh=1.3)]
    rs.append(rot(0, 286, "Não excluem a parada:", w=400, tam=22, cor=GLIC, peso=700))
    for k, t in enumerate(["abalos que parecem convulsão", "respiração agônica, o gasping", "“está respirando, então não é parada”"]):
        x = 300 + k * 460
        p.append(caixa(x, 276, 440, 64, GLIC, GLIC_T, esp=2, rx=32))
        rs.append(rot(x + 16, 294, t, w=408, tam=21, cor=TINTA, alinha="center"))
    return slide("reconhecer", 380, p, rs, eyebrow="Erro cinco: o da hora", titulo="Caiu sem contato e não responde: é parada",
                 destaque="Cada minuto de atraso custa sobrevida. Todo o departamento precisa saber a regra de cor.", destaque_cor="tinta")


def desfibrilador_64():
    """6.4: o 89% e a corrente de três elos."""
    p = [svg_abre(1664, 380, "À esquerda, o número: 89 por cento de sobrevida de atletas do ensino médio americano quando havia desfibrilador no local e ele foi usado. À direita, uma corrente de três elos: reconhecer rápido, caiu sem contato e não responde; comprimir cedo, quem estiver mais perto; desfibrilar cedo, aparelho acessível, em minutos")]
    rs = []
    p.append(caixa(0, 0, 460, 380, OXID, OXID, esp=0, rx=18))
    rs += [rot(0, 60, "89%", w=460, tam=120, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(30, 230, "de sobrevida com o desfibrilador do local usado", w=400, tam=24, cor=PAPEL, alinha="center", lh=1.3)]
    elos = [("t:eye", "Reconhecer rápido", "caiu sem contato e não responde", FOSF), ("t:hand-stop", "Comprimir cedo", "quem estiver mais perto", GLIC), ("t:bolt", "Desfibrilar cedo", "aparelho acessível, em minutos", OXID)]
    for k, (ic, t, d, cor) in enumerate(elos):
        x = 520 + k * 372
        p.append(f'<rect x="{x}" y="60" width="388" height="200" rx="100" fill="none" stroke="{cor}" stroke-width="14"/>')
        p.append(icone(ic, x + 164, 90, 60, cor))
        rs += [rot(x + 24, 160, t, w=340, tam=24, cor=cor, peso=700, alinha="center"),
               rot(x + 4, 290, d, w=380, tam=21, cor=TINTA, alinha="center", lh=1.25)]
    return slide("desfibrilador", 380, p, rs, eyebrow="O número que nenhum exame alcança", titulo="89% de sobrevida com o desfibrilador do local usado",
                 destaque="A pergunta certa para clube, escola e prova: “o que vocês fazem quando alguém cai?”. Se é difícil nos clubes profissionais de São Paulo, imagine na várzea.",
                 destaque_cor="tinta", fonte="Registro americano de ensino médio, BJSM 2013 · Revista Brasileira de Medicina do Esporte 2011")


def correcoes_64():
    """6.4: as cinco frases erradas riscadas, cada uma com a que a substitui."""
    p = [svg_abre(1664, 420, "Cinco frases erradas, riscadas, cada uma com a que a substitui. É raríssimo: raro, concentrado e com resposta conhecida, então prepare-se. É sempre hipertrófica: parte relevante é doença elétrica em coração normal. É coisa de jovem de elite: acima dos 35 é coronária, e o amador é o menos coberto. Com exame não teria acontecido: 6 de 8 tinham rastreio normal; seguimento e sintoma. Deve ser convulsão: caiu e não responde, compressão e desfibrilador"), defs(MUDO)]
    rs = []
    linhas = [("“É raríssimo.”", "raro, concentrado, e com resposta conhecida: prepare-se"),
              ("“É sempre hipertrófica.”", "parte relevante é doença elétrica em coração normal"),
              ("“É coisa de jovem de elite.”", "acima dos 35 é coronária; o amador é o menos coberto"),
              ("“Com exame não teria acontecido.”", "6 de 8 tinham rastreio normal; seguimento e sintoma"),
              ("“Deve ser convulsão.”", "caiu e não responde: compressão e desfibrilador")]
    for k, (a, b) in enumerate(linhas):
        y = k * 84
        p.append(caixa(0, y, 560, 70, FOSF, FOSF_T, esp=2, rx=35))
        rs.append(rot(20, y + 19, a, w=520, tam=24, cor=FOSF, peso=700, alinha="center"))
        wl = min(len(a) * 12.5, 500)
        p.append(f'<line x1="{280 - wl / 2:.0f}" y1="{y + 36}" x2="{280 + wl / 2:.0f}" y2="{y + 36}" stroke="{FOSF}" stroke-width="3"/>')
        p.append(seta(576, y + 35, 640, y + 35, MUDO, "m0", esp=3))
        p.append(caixa(660, y, 1004, 70, OXID, CARTAO, esp=2, rx=14))
        rs.append(rot(684, y + 19, b, w=960, tam=24, cor=TINTA))
    return slide("correcoes", 420, p, rs, eyebrow="As cinco frases erradas", titulo="O que as substitui")

# ---------------------------------------------------------------- 6.5

def cena_65():
    """6.5: o campo visto de cima, o menino caído e as quatro decisões tomadas antes do jogo."""
    p = [svg_abre(1664, 400, "Um campo de futebol visto de cima, num sábado de manhã. No meio do primeiro tempo, um menino cai sem que ninguém tenha encostado nele. Em volta, as quatro coisas decididas antes do jogo: quem vai primeiro, onde está o desfibrilador, quem liga, quem abre o portão")]
    rs = []
    F0, F1, Fy0, Fy1 = 0, 900, 0, 400
    p.append(f'<rect x="{F0}" y="{Fy0}" width="{F1 - F0}" height="{Fy1 - Fy0}" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<line x1="450" y1="0" x2="450" y2="400" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<circle cx="450" cy="200" r="64" fill="none" stroke="{OXID}" stroke-width="3"/>')
    for x in (0, 900):
        w = 120
        xx = x if x == 0 else x - w
        p.append(f'<rect x="{xx}" y="110" width="{w}" height="180" fill="none" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<circle cx="300" cy="240" r="34" fill="{FOSF}"/>')
    p.append(icone("h:person", 276, 216, 48, PAPEL))
    rs.append(rot(180, 286, "caiu; ninguém encostou", w=240, tam=20, cor=FOSF, peso=700, alinha="center"))
    p.append(caixa(820, 330, 70, 56, FOSF, FOSF, esp=0, rx=8))
    p.append(icone("t:bolt", 836, 340, 36, PAPEL))
    p.append(f'<path d="M 820 350 C 600 350, 420 320, 330 270" fill="none" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    rs.append(rot(560, 360, "onde está o DEA?", w=240, tam=19, cor=FOSF, peso=700))
    rs.append(rot(950, 0, "Decidido antes do jogo", w=700, tam=26, cor=TINTA, peso=700, serif=True))
    itens = [("t:run", "quem vai primeiro"), ("t:bolt", "onde está o desfibrilador"), ("t:phone-call", "quem liga"), ("t:door", "quem abre o portão")]
    for k, (ic, t) in enumerate(itens):
        y = 60 + k * 84
        p.append(caixa(950, y, 714, 70, TINTA, CARTAO, esp=2, rx=35))
        p.append(icone(ic, 974, y + 15, 40, TINTA))
        rs.append(rot(1030, y + 20, t, w=620, tam=24, cor=TINTA, peso=600))
    return slide("cena", 400, p, rs, eyebrow="Sábado de manhã, campo alugado", titulo="Um menino cai no meio do primeiro tempo")


def mapa_65():
    """6.5: os seis passos em três faixas de tempo: antes, na queda, depois."""
    p = [svg_abre(1664, 380, "Os seis passos em três faixas de tempo. Antes da queda: plano escrito e desfibrilador no lugar. Na queda: reconhecer e comprimir, chocar e voltar. Depois: transferir e registrar, e ensaiar, de novo. Metade dos passos acontece antes da queda, numa terça-feira qualquer")]
    rs = []
    faixas = [("Antes da queda", [("1", "Plano escrito"), ("2", "Desfibrilador no lugar")], OXID, OXID_T),
              ("Na queda", [("3", "Reconhecer e comprimir"), ("4", "Chocar e voltar")], FOSF, FOSF_T),
              ("Depois", [("5", "Transferir e registrar"), ("6", "Ensaiar, de novo")], GLIC, GLIC_T)]
    for k, (t, passos, cor, fundo) in enumerate(faixas):
        x = k * 560
        p.append(caixa(x, 0, 524, 380, cor, fundo, esp=2, rx=18))
        rs.append(rot(x + 24, 20, t, w=480, tam=28, cor=cor, peso=700, serif=True))
        for j, (n, ps) in enumerate(passos):
            y = 90 + j * 140
            p.append(caixa(x + 24, y, 476, 120, cor, CARTAO, esp=2, rx=14))
            p.append(f'<circle cx="{x + 80}" cy="{y + 60}" r="32" fill="{cor}"/>')
            rs += [rot(x + 50, y + 40, n, w=60, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True),
                   rot(x + 130, y + 40, ps, w=350, tam=25, cor=TINTA, peso=700)]
        if k < 2:
            p.append(f'<path d="M {x + 532} 190 l 20 0" stroke="{MUDO}" stroke-width="4"/>')
    return slide("mapa", 380, p, rs, eyebrow="O procedimento", titulo="Seis passos, metade antes da queda",
                 destaque="A parte que decide o desfecho é a parte administrativa, feita numa terça-feira qualquer. Nada aqui substitui o curso presencial de suporte básico de vida.",
                 destaque_cor="tinta")


def folha_65():
    """6.5: a folha do plano, com sete funções e o espaço do nome próprio."""
    p = [svg_abre(1664, 420, "A folha do plano escrito, com sete linhas. Cada linha tem a função, o que ela faz e um espaço para um nome próprio. Quem lidera: olha o relógio e distribui tarefas, não comprime. Quem comprime, e quem é o segundo: troca a cada dois minutos. Quem busca o desfibrilador: sai correndo sem esperar ordem. Quem liga para o 192: com endereço, referência e portão escritos na folha. Quem abre o portão e conduz a ambulância até o atleta. Quem afasta as pessoas e protege a imagem do atleta. Quem cuida do grupo: atletas e famílias que viram a queda")]
    rs = []
    p.append(caixa(0, 0, 1664, 420, OXID, CARTAO, esp=3, rx=14))
    rs += [rot(24, 14, "Plano de emergência", w=600, tam=24, cor=OXID, peso=700, serif=True),
           rot(1240, 18, "nome", w=400, tam=20, cor=MUDO, peso=700)]
    linhas = [("t:clock", "Quem lidera", "olha o relógio, distribui tarefas; não comprime"),
              ("t:hand-stop", "Quem comprime", "e quem é o segundo: troca a cada dois minutos"),
              ("t:bolt", "Quem busca o desfibrilador", "sai correndo sem esperar ordem"),
              ("t:phone-call", "Quem liga para o 192", "com endereço, referência e portão escritos na folha"),
              ("t:door", "Quem abre o portão", "e conduz a ambulância até o atleta"),
              ("t:users", "Quem afasta as pessoas", "e protege a imagem do atleta"),
              ("t:heart-handshake", "Quem cuida do grupo", "atletas e famílias que viram a queda")]
    for k, (ic, f, d) in enumerate(linhas):
        y = 58 + k * 51
        p.append(icone(ic, 24, y + 6, 32, OXID))
        rs += [rot(70, y + 8, f, w=400, tam=22, cor=TINTA, peso=700), rot(470, y + 8, d, w=740, tam=21, cor=TINTA)]
        p.append(f'<line x1="1240" y1="{y + 38}" x2="1630" y2="{y + 38}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
        if k < 6:
            p.append(f'<line x1="24" y1="{y + 48}" x2="1640" y2="{y + 48}" stroke="{BORDA}" stroke-width="1"/>')
    return slide("folha", 420, p, rs, eyebrow="Passo um: o plano escrito", titulo="Sete linhas, sete nomes próprios",
                 destaque="O teste: entregue a folha a quem não estava na reunião. Se não souber o que fazer, existe uma folha, não um plano.",
                 destaque_cor="petr")


def dea_65():
    """6.5: o relógio da queda ao choque, o aparelho e a verificação."""
    p = [svg_abre(1664, 380, "À esquerda, um relógio de dez minutos a partir da queda, com a faixa de três a cinco minutos destacada: a meta entre a queda e o primeiro choque. No meio, o desfibrilador: qualquer pessoa pode usar, e o aparelho só choca ritmo chocável. À direita, a verificação: bateria e pás dentro da validade, e a checagem registrada")]
    rs = []
    import math as _m
    cx, cy, r = 190, 190, 160
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    def pt(min_, rr):
        a = _m.radians(-90 + min_ * 36)
        return cx + rr * _m.cos(a), cy + rr * _m.sin(a)
    x3, y3 = pt(3, r - 22); x5, y5 = pt(5, r - 22)
    p.append(f'<path d="M {x3:.0f} {y3:.0f} A {r - 22} {r - 22} 0 0 1 {x5:.0f} {y5:.0f}" fill="none" stroke="{FOSF}" stroke-width="28"/>')
    for m in range(10):
        x1, y1 = pt(m, r - 6); x2, y2 = pt(m, r - 40 if m % 5 == 0 else r - 18)
        p.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{TINTA}" stroke-width="3"/>')
    xq, yq = pt(0, r - 60)
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{xq:.0f}" y2="{yq:.0f}" stroke="{TINTA}" stroke-width="5" stroke-linecap="round"/>')
    rs += [rot(cx + 12, 42, "queda", w=120, tam=18, cor=MUDO),
           rot(cx - 150, cy + 24, "3 a 5 min", w=140, tam=26, cor=FOSF, peso=700, alinha="right")]
    rs.append(rot(400, 40, "A meta", w=260, tam=28, cor=FOSF, peso=700, serif=True))
    rs.append(rot(400, 170, "da queda ao primeiro choque, contando a corrida até o aparelho", w=260, tam=21, cor=TINTA, lh=1.3))
    p.append(caixa(700, 0, 460, 380, OXID, OXID_T, esp=2, rx=18))
    p.append(caixa(860, 40, 140, 120, OXID, OXID, esp=0, rx=16))
    p.append(icone("t:bolt", 895, 65, 70, PAPEL))
    rs += [rot(724, 190, "Qualquer pessoa pode usar", w=412, tam=26, cor=OXID, peso=700, alinha="center", serif=True),
           rot(724, 240, "o aparelho só choca ritmo chocável", w=412, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    p.append(caixa(1200, 0, 464, 380, GLIC, GLIC_T, esp=2, rx=18))
    rs.append(rot(1224, 20, "Verificação", w=420, tam=26, cor=GLIC, peso=700, serif=True))
    for k, (ic, t) in enumerate([("t:battery-4", "bateria na validade"), ("t:first-aid-kit", "pás na validade"), ("t:clipboard-check", "checagem registrada")]):
        y = 90 + k * 90
        p.append(icone(ic, 1224, y, 48, GLIC))
        rs.append(rot(1290, y + 10, t, w=350, tam=23, cor=TINTA, peso=600))
    return slide("dea", 380, p, rs, eyebrow="Passo dois: o desfibrilador", titulo="O critério de posicionamento é tempo",
                 destaque="Distância se mede em segundos de corrida. DEA trancado na diretoria é DEA que não existe. A primeira vez que alguém abre a maleta não pode ser com um atleta no chão.",
                 destaque_cor="tinta", fonte="Força-tarefa americana, Prehosp Emerg Care 2007 · Lei Lucas, 13.722/2018")


def comprimir_65():
    """6.5: frequência, profundidade e troca de quem comprime, em três desenhos."""
    p = [svg_abre(1664, 380, "Três desenhos. Frequência: uma fileira de batidas, de 100 a 120 compressões por minuto. Profundidade: uma régua no tórax do adulto, com a faixa de 5 a 6 centímetros e retorno completo. Troca: duas pessoas que se revezam na compressão a cada dois minutos")]
    rs = []
    p.append(caixa(0, 0, 524, 380, FOSF, FOSF_T, esp=2, rx=18))
    rs += [rot(24, 20, "100 a 120", w=480, tam=56, cor=FOSF, peso=700, serif=True), rot(24, 100, "compressões por minuto", w=480, tam=24, cor=TINTA)]
    for k in range(8):
        x = 40 + k * 58
        h = 70
        p.append(f'<path d="M {x} 260 L {x + 10} 260 L {x + 18} {260 - h} L {x + 26} 260 L {x + 48} 260" fill="none" stroke="{FOSF}" stroke-width="4" stroke-linejoin="round"/>')
    rs.append(rot(24, 300, "no ritmo, sem pausa", w=480, tam=21, cor=MUDO))
    p.append(caixa(570, 0, 524, 380, GLIC, GLIC_T, esp=2, rx=18))
    rs += [rot(594, 20, "5 a 6 cm", w=480, tam=56, cor=GLIC, peso=700, serif=True), rot(594, 100, "de profundidade no adulto", w=480, tam=24, cor=TINTA)]
    X, Y0 = 700, 160
    p.append(f'<line x1="{X}" y1="{Y0}" x2="{X}" y2="{Y0 + 180}" stroke="{TINTA}" stroke-width="4"/>')
    for cm in range(0, 8):
        y = Y0 + cm * 25
        p.append(f'<line x1="{X}" y1="{y}" x2="{X + (24 if cm % 5 == 0 else 14)}" y2="{y}" stroke="{TINTA}" stroke-width="3"/>')
        rs.append(rot(X - 70, y - 12, f"{cm}", w=56, tam=18, cor=MUDO, alinha="right"))
    p.append(f'<rect x="{X + 30}" y="{Y0 + 125}" width="200" height="25" fill="{GLIC}"/>')
    rs += [rot(X + 240, Y0 + 122, "5 a 6 cm", w=140, tam=21, cor=GLIC, peso=700),
           rot(X + 30, Y0 + 20, "com retorno completo do tórax", w=320, tam=21, cor=TINTA, lh=1.25)]
    p.append(caixa(1140, 0, 524, 380, OXID, OXID_T, esp=2, rx=18))
    rs += [rot(1164, 20, "2 min", w=480, tam=56, cor=OXID, peso=700, serif=True), rot(1164, 100, "troca de quem comprime", w=480, tam=24, cor=TINTA)]
    p.append(icone("h:person", 1210, 180, 110, OXID))
    p.append(icone("h:person", 1470, 180, 110, MUDO))
    p.append(f'<path d="M 1340 200 C 1380 160, 1420 160, 1460 200" fill="none" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<path d="M 1460 290 C 1420 330, 1380 330, 1340 290" fill="none" stroke="{MUDO}" stroke-width="4"/>')
    return slide("comprimir", 380, p, rs, eyebrow="Passo três: reconhecer e começar", titulo="Não responde e não respira normalmente: comprime",
                 destaque="Grite e dispare duas tarefas ao mesmo tempo: “traz o DEA” e “liga 192”. Quem não é treinado em ventilação faz compressão contínua.",
                 destaque_cor="tinta", fonte="Diretriz americana de ressuscitação, Circulation 2025")


def erros_65():
    """6.5: a faixa de compressão contínua e os três buracos que os erros abrem nela (esquema)."""
    p = [svg_abre(1664, 400, "Esquema. Uma faixa de compressão contínua, da queda até a chegada do socorro. Três erros abrem buracos na faixa: procurar pulso, em que leigos e profissionais erram e cada segundo é sem compressão; esperar o médico, que pode estar no vestiário ou não existir, quando quem está ao lado deveria começar; levar o atleta para fora do campo, quando a reanimação acontece onde ele está")]
    rs = []
    Y = 60
    segs = [(0, 244), (356, 776), (888, 1308), (1420, 1664)]
    for a, b in segs:
        p.append(f'<rect x="{a}" y="{Y}" width="{b - a}" height="60" rx="6" fill="{OXID}"/>')
    rs += [rot(0, 0, "compressão contínua", w=400, tam=22, cor=OXID, peso=700), rot(1264, 0, "esquema", w=400, tam=18, cor=MUDO, alinha="right")]
    erros = [(300, "Procurar pulso", "leigos e profissionais erram; cada segundo nisso é sem compressão"),
             (832, "Esperar o médico", "pode estar no vestiário, ou não existir; quem está ao lado começa"),
             (1364, "Levar para fora do campo", "a reanimação acontece onde o atleta está")]
    for cx, t, d in erros:
        p.append(f'<rect x="{cx - 56}" y="{Y}" width="112" height="60" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
        p.append(f'<line x1="{cx}" y1="{Y + 66}" x2="{cx}" y2="170" stroke="{FOSF}" stroke-width="2"/>')
        x = cx - 235
        p.append(caixa(x, 170, 470, 230, FOSF, FOSF_T, esp=2, rx=16))
        p.append(icone("t:x", x + 20, 190, 40, FOSF))
        rs += [rot(x + 70, 194, t, w=380, tam=26, cor=FOSF, peso=700, serif=True), rot(x + 24, 260, d, w=422, tam=22, cor=TINTA, lh=1.35)]
    return slide("erros", 400, p, rs, eyebrow="Três erros que custam tempo", titulo="O que aparece em quase todo vídeo")


def chocar_65():
    """6.5: o laço choque e compressão, e seis obstáculos com a solução de cada um."""
    p = [svg_abre(1664, 400, "À esquerda, um laço: compressão, choque, e de volta à compressão na hora, sem checar pulso; quem comprime não para enquanto outro cola as pás. À direita, seis obstáculos que atrasam as pás e a solução de cada um: tórax molhado, secar rápido; muito pelo, lâmina da maleta; adesivo de medicação, retirar e limpar; dispositivo implantado, pá alguns centímetros ao lado; criança sem pá pediátrica, usar a de adulto; choque não indicado, continuar comprimindo"), defs(OXID, FOSF)]
    rs = []
    p.append(f'<path d="M 120 140 A 130 80 0 0 1 380 140" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m1)"/>')
    p.append(f'<path d="M 380 240 A 130 80 0 0 1 120 240" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m0)"/>')
    p.append(caixa(0, 150, 220, 80, OXID, OXID_T, esp=3, rx=40))
    p.append(caixa(290, 150, 220, 80, FOSF, FOSF_T, esp=3, rx=40))
    rs += [rot(0, 172, "compressão", w=220, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(290, 172, "choque", w=220, tam=24, cor=FOSF, peso=700, alinha="center"),
           rot(0, 344, "volta a comprimir na hora, sem checar pulso", w=520, tam=21, cor=OXID, peso=700, alinha="center")]
    obst = [("Tórax molhado", "secar rápido"), ("Muito pelo onde vão as pás", "lâmina da maleta"), ("Adesivo de medicação", "retirar e limpar"),
            ("Dispositivo implantado", "pá alguns centímetros ao lado"), ("Criança sem pá pediátrica", "usar a de adulto"), ("“Choque não indicado”", "continuar comprimindo")]
    for k, (a, b) in enumerate(obst):
        col, lin = k % 2, k // 2
        x, y = 580 + col * 546, lin * 136
        p.append(caixa(x, y, 530, 122, GLIC if k < 5 else OXID, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, y + 16, a, w=490, tam=23, cor=TINTA, peso=700), rot(x + 20, y + 64, "→ " + b, w=490, tam=22, cor=GLIC if k < 5 else OXID, peso=600)]
    return slide("chocar", 400, p, rs, eyebrow="Passo quatro: chocar e voltar a comprimir", titulo="O que atrasa as pás, e a solução",
                 destaque="Depois do choque, volta a comprimir na hora, sem checar pulso. Quem comprime não para enquanto outro cola as pás.",
                 destaque_cor="tinta")


def depois_65():
    """6.5: o cartão de transferência, quem fala e o registro do mesmo dia."""
    p = [svg_abre(1664, 380, "Três blocos de depois da queda. A transferência para a equipe da ambulância, numa frase com quatro campos: hora da queda, hora da primeira compressão, choques dados, estado agora. Quem fala: uma pessoa designada; família por telefone, não pelo story. O registro, no mesmo dia: horários, choques e quem fez o quê")]
    rs = []
    p.append(caixa(0, 0, 760, 380, OXID, CARTAO, esp=2, rx=16))
    p.append(icone("t:ambulance", 24, 20, 48, OXID))
    rs += [rot(88, 28, "A transferência, numa frase", w=650, tam=27, cor=OXID, peso=700, serif=True)]
    for k, t in enumerate(["hora da queda", "hora da primeira compressão", "choques dados", "estado agora"]):
        col, lin = k % 2, k // 2
        x, y = 24 + col * 362, 100 + lin * 140
        p.append(caixa(x, y, 346, 120, OXID, OXID_T, esp=2, rx=12))
        rs.append(rot(x + 16, y + 14, t, w=314, tam=22, cor=OXID, peso=700))
        p.append(f'<line x1="{x + 16}" y1="{y + 90}" x2="{x + 330}" y2="{y + 90}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    p.append(caixa(800, 0, 420, 380, GLIC, GLIC_T, esp=2, rx=16))
    p.append(icone("t:speakerphone", 824, 20, 48, GLIC))
    rs += [rot(888, 28, "Quem fala", w=310, tam=27, cor=GLIC, peso=700, serif=True),
           rot(824, 110, "uma pessoa designada", w=372, tam=24, cor=TINTA, peso=700),
           rot(824, 170, "família por telefone, não pelo story", w=372, tam=23, cor=TINTA, lh=1.3)]
    p.append(caixa(1260, 0, 404, 380, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:writing", 1284, 20, 48, TINTA))
    rs += [rot(1348, 28, "O registro", w=300, tam=27, cor=TINTA, peso=700, serif=True),
           rot(1284, 110, "no mesmo dia", w=360, tam=24, cor=TINTA, peso=700),
           rot(1284, 170, "horários, choques, quem fez o quê", w=360, tam=23, cor=TINTA, lh=1.3)]
    return slide("depois", 380, p, rs, eyebrow="Passo cinco: o que quase todo mundo esquece", titulo="Transferir, registrar, cuidar de quem ficou",
                 destaque="O grupo que viu o colega cair faz parte do atendimento. Dias depois, revisão curta: o que travou e quanto demorou cada elo.",
                 destaque_cor="petr")


def calor_65():
    """6.5: o termômetro retal, do limiar do golpe de calor à meta, e a ordem resfriar e depois transportar."""
    p = [svg_abre(1664, 380, "À esquerda, um termômetro retal. No alto, acima de 40,5 graus, com disfunção do sistema nervoso, o golpe de calor. Embaixo, a meta: abaixo de 38,9 graus. Uma seta desce de um ao outro: imersão fria, em até 30 minutos do colapso à meta. À direita, a ordem: primeiro resfriar, depois transportar; caixa d'água, banheira inflável ou tanque, com água, gelo e o corpo dentro, antes da ambulância"), defs(OXID, MUDO)]
    rs = []
    X = 120
    ft = lambda c: 330 - (c - 38) / (41.5 - 38) * 300
    p.append(f'<rect x="{X - 22}" y="20" width="44" height="320" rx="22" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    p.append(f'<rect x="{X - 12}" y="{ft(40.8):.0f}" width="24" height="{330 - ft(40.8):.0f}" rx="12" fill="{FOSF}"/>')
    for c in range(38, 42):
        p.append(f'<line x1="{X + 26}" y1="{ft(c):.0f}" x2="{X + 40}" y2="{ft(c):.0f}" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(X - 110, ft(c) - 12, f"{c} °C", w=80, tam=18, cor=MUDO, alinha="right"))
    for c, t, cor in [(40.5, "> 40,5 °C retal, com disfunção do sistema nervoso", FOSF), (38.9, "< 38,9 °C: a meta", OXID)]:
        p.append(f'<line x1="{X - 30}" y1="{ft(c):.0f}" x2="{X + 200}" y2="{ft(c):.0f}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(X + 210, ft(c) - 16, t, w=420, tam=23, cor=cor, peso=700, lh=1.2))
    p.append(seta(X + 280, ft(40.5) + 40, X + 280, ft(38.9) - 12, OXID, "m0", esp=5))
    rs.append(rot(X + 300, ft(39.7) - 8, "imersão fria: até 30 min do colapso à meta", w=330, tam=21, cor=TINTA, lh=1.25))
    for k, (n, t, d, cor, fundo, ic) in enumerate([("1", "Resfriar", "caixa d'água, banheira inflável, tanque: água, gelo, corpo dentro", OXID, OXID_T, "t:droplet"),
                                                   ("2", "Transportar", "depois de chegar à meta, não antes", MUDO, PAPEL, "t:ambulance")]):
        y = k * 196
        p.append(caixa(860, y, 804, 180, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="910" cy="{y + 50}" r="30" fill="{cor}"/>')
        p.append(icone(ic, 1580, y + 22, 56, cor))
        rs += [rot(880, y + 32, n, w=60, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True),
               rot(964, y + 28, t, w=600, tam=30, cor=cor if cor != MUDO else TINTA, peso=700, serif=True),
               rot(884, y + 96, d, w=740, tam=22, cor=TINTA, lh=1.3)]
    p.append(seta(1262, 182, 1262, 194, MUDO, "m1", esp=3))
    return slide("calor", 380, p, rs, eyebrow="A emergência não cardíaca que mais se trata errado", titulo="Golpe de calor: resfriar primeiro, transportar depois",
                 destaque="A medida retal é a única confiável em quem está se exercitando. Caixa d'água, banheira inflável, tanque: água, gelo, corpo dentro, antes da ambulância.",
                 destaque_cor="tinta", fonte="Posicionamento da NATA, J Athl Train 2015")


def outras_65():
    """6.5: seis emergências em ladrilhos, cada uma com a primeira conduta."""
    p = [svg_abre(1664, 400, "Seis emergências, cada uma com a primeira conduta. Hipoglicemia: consciente, açúcar pela boca; inconsciente, nada pela boca e 192. Anafilaxia: adrenalina intramuscular na coxa, já, com o dispositivo no local do treino. Lesão cervical: não mover, não tirar o capacete; na parada, comprimir vem antes. Engasgo: tosse eficaz, deixa tossir; se não passa ar, desobstrução. Convulsão: protege a cabeça, nada na boca; passou de cinco minutos, emergência. Fratura e luxação: imobiliza como está, não reduz em campo")]
    rs = []
    itens = [("t:candy", "Hipoglicemia", "consciente: açúcar pela boca; inconsciente: nada pela boca, 192", GLIC),
             ("h:medicines", "Anafilaxia", "adrenalina intramuscular na coxa, já; dispositivo no local do treino", FOSF),
             ("h:head", "Lesão cervical", "não mover, não tirar capacete; na parada, comprimir vem antes", FOSF),
             ("h:lungs", "Engasgo", "tosse eficaz, deixa tossir; não passa ar, desobstrução", GLIC),
             ("t:brain", "Convulsão", "protege a cabeça, nada na boca; passou de 5 min, emergência", AZUL),
             ("h:crutches", "Fratura, luxação", "imobiliza como está; não reduz em campo", MUDO)]
    for k, (ic, t, d, cor) in enumerate(itens):
        col, lin = k % 3, k // 3
        x, y = col * 560, lin * 206
        p.append(caixa(x, y, 536, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, y + 22, 56, cor))
        rs += [rot(x + 94, y + 34, t, w=420, tam=27, cor=cor if cor != MUDO else TINTA, peso=700, serif=True),
               rot(x + 24, y + 98, d, w=490, tam=22, cor=TINTA, lh=1.3)]
    return slide("outras", 400, p, rs, eyebrow="As outras emergências", titulo="Uma linha para cada")


def ensaio_65():
    """6.5: o ensaio cronometrado no gramado e as quatro perguntas de cada jogo fora."""
    p = [svg_abre(1664, 380, "À esquerda, o ensaio: quinze minutos, com cronômetro; alguém deita no gramado e a equipe executa cada linha da folha; uma vez por trimestre, e com gente nova. À direita, as quatro perguntas antes de cada jogo fora: onde está o desfibrilador daqui, qual é o endereço e o portão, tem ambulância e até que horas, e qual é o hospital de referência")]
    rs = []
    p.append(caixa(0, 0, 780, 380, OXID, OXID_T, esp=2, rx=18))
    p.append(icone("t:stopwatch", 24, 24, 120, OXID))
    rs += [rot(170, 30, "15 min", w=400, tam=64, cor=OXID, peso=700, serif=True),
           rot(170, 116, "com cronômetro", w=400, tam=24, cor=TINTA)]
    for k, t in enumerate(["alguém deita no gramado", "a equipe executa cada linha da folha", "por trimestre, e com gente nova"]):
        y = 190 + k * 60
        p.append(icone("t:check", 24, y, 36, OXID))
        rs.append(rot(74, y + 4, t, w=680, tam=24, cor=TINTA))
    p.append(caixa(820, 0, 844, 380, GLIC, CARTAO, esp=2, rx=18))
    rs.append(rot(844, 20, "Antes de cada jogo fora", w=780, tam=27, cor=GLIC, peso=700, serif=True))
    for k, (ic, t) in enumerate([("t:bolt", "onde está o DEA daqui?"), ("t:map", "qual o endereço e o portão?"), ("t:ambulance", "tem ambulância, e até que horas?"), ("t:building-hospital", "qual o hospital de referência?")]):
        y = 84 + k * 72
        p.append(caixa(844, y, 796, 60, GLIC, GLIC_T, esp=2, rx=30))
        p.append(icone(ic, 864, y + 12, 36, GLIC))
        rs.append(rot(914, y + 16, t, w=700, tam=23, cor=TINTA, peso=600))
    return slide("ensaio", 380, p, rs, eyebrow="Passo seis: ensaiar", titulo="O que transforma papel em plano",
                 destaque="O cronômetro costuma mostrar a mesma coisa: o DEA demora mais do que todo mundo achava.",
                 destaque_cor="tinta")

# ---------------------------------------------------------------- 6.6

def frase_66():
    """6.6: o exame que não decide e a decisão clínica tomada três vezes."""
    p = [svg_abre(1664, 400, "À esquerda, o exame: a tomografia costuma vir normal na concussão; ela exclui sangramento, não concussão, e não decide por você. À direita, a decisão: clínica, rápida, sob pressão, e tomada três vezes, à beira do campo, em casa e no vestiário")]
    rs = []
    p.append(caixa(0, 0, 620, 400, MUDO, PAPEL, esp=2, rx=18))
    p.append(icone("t:brain", 40, 40, 120, MUDO))
    p.append(icone("t:check", 170, 110, 56, OXID))
    rs += [rot(240, 60, "A tomografia", w=360, tam=30, cor=TINTA, peso=700, serif=True),
           rot(240, 110, "costuma vir normal", w=360, tam=24, cor=OXID, peso=700),
           rot(40, 220, "exclui sangramento, não concussão: nenhum exame decide por você", w=550, tam=24, cor=TINTA, lh=1.35)]
    p.append(caixa(680, 0, 984, 400, FOSF, CARTAO, esp=2, rx=18))
    rs += [rot(704, 24, "A decisão é clínica, rápida, sob pressão", w=930, tam=30, cor=FOSF, peso=700, serif=True),
           rot(704, 82, "e é tomada três vezes", w=930, tam=24, cor=TINTA)]
    for k, (t, ic) in enumerate([("à beira do campo", "t:soccer-field"), ("em casa", "t:home"), ("no vestiário", "t:door")]):
        x = 720 + k * 312
        p.append(f'<circle cx="{x + 130}" cy="230" r="72" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
        p.append(icone(ic, x + 100, 200, 60, FOSF))
        rs.append(rot(x, 320, t, w=260, tam=24, cor=TINTA, peso=700, alinha="center"))
        if k < 2:
            p.append(f'<line x1="{x + 206}" y1="230" x2="{x + 366}" y2="230" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    return slide("frase", 400, p, rs, eyebrow="Concussão relacionada ao esporte", titulo="A lesão em que a decisão errada custa mais do que a lesão")


def decisoes_66():
    """6.6: as três decisões numa linha do tempo: 30 segundos, 48 horas, sétimo dia."""
    p = [svg_abre(1664, 380, "Uma linha do tempo com três decisões. Aos trinta segundos, à beira do campo: o meia cambaleia e diz que está bem; dá para continuar? Às quarenta e oito horas, na casa da família: o adolescente no domingo; escola, celular, quarto escuro? No sétimo dia, no vestiário: estou zerado, posso treinar com contato?")]
    rs = []
    p.append(f'<line x1="0" y1="52" x2="1664" y2="52" stroke="{MUDO}" stroke-width="4"/>')
    itens = [("30 segundos", "À beira do campo", "o meia cambaleia e diz que está bem: dá para continuar?", FOSF, FOSF_T, "t:soccer-field"),
             ("48 horas", "Na casa da família", "o adolescente no domingo: escola, celular, quarto escuro?", GLIC, GLIC_T, "t:home"),
             ("7º dia", "No vestiário", "“estou zerado, posso treinar com contato?”", OXID, OXID_T, "t:door")]
    for k, (q, t, d, cor, fundo, ic) in enumerate(itens):
        x = k * 568
        p.append(f'<circle cx="{x + 264}" cy="52" r="14" fill="{cor}"/>')
        rs.append(rot(x, 0, q, w=528, tam=22, cor=cor, peso=700, alinha="center"))
        p.append(caixa(x, 90, 528, 290, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 114, 52, cor))
        rs += [rot(x + 92, 122, t, w=420, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 200, d, w=480, tam=24, cor=TINTA, lh=1.35)]
    return slide("decisoes", 380, p, rs, eyebrow="As três decisões da aula", titulo="Trinta segundos, quarenta e oito horas, sétimo dia",
                 destaque="O diagnóstico é médico. Reconhecer e retirar de campo não é, e é aí que o sistema mais falha.", destaque_cor="tinta")


def equivocos_66():
    """6.6: três frases riscadas e o que vale no lugar, com a perda de consciência em barra."""
    p = [svg_abre(1664, 380, "Três equívocos riscados e o que vale. Não bateu a cabeça: a força chega pelo ombro, pelo tronco, pela queda. Não desmaiou: a perda de consciência aparece em menos de dez por cento dos casos, mostrada numa barra. A tomografia deu normal: é o esperado; ela exclui sangramento, não concussão")]
    rs = []
    itens = [("“Não bateu a cabeça.”", "a força chega pelo ombro, pelo tronco, pela queda", "forca"),
             ("“Não desmaiou.”", "perda de consciência em menos de 10% dos casos", "barra"),
             ("“A tomografia deu normal.”", "é o esperado; ela exclui sangramento, não concussão", "tc")]
    for k, (a, b, viz) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 80, FOSF, FOSF_T, esp=2, rx=40))
        rs.append(rot(x + 20, 22, a, w=488, tam=25, cor=FOSF, peso=700, alinha="center"))
        wl = len(a) * 12.5
        p.append(f'<line x1="{x + 264 - wl / 2:.0f}" y1="40" x2="{x + 264 + wl / 2:.0f}" y2="40" stroke="{FOSF}" stroke-width="3"/>')
        p.append(caixa(x, 100, 528, 280, OXID, CARTAO, esp=2, rx=16))
        rs.append(rot(x + 24, 290, b, w=480, tam=23, cor=TINTA, lh=1.3))
        if viz == "forca":
            p.append(icone("h:person", x + 200, 120, 140, MUDO))
            p.append(f'<line x1="{x + 60}" y1="200" x2="{x + 220}" y2="200" stroke="{OXID}" stroke-width="6"/>')
            p.append(f'<path d="M {x + 220} 188 L {x + 240} 200 L {x + 220} 212 Z" fill="{OXID}"/>')
        elif viz == "barra":
            p.append(f'<rect x="{x + 24}" y="170" width="480" height="60" rx="6" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
            p.append(f'<rect x="{x + 24}" y="170" width="48" height="60" rx="6" fill="{OXID}"/>')
            rs += [rot(x + 84, 186, "< 10% perdem a consciência", w=400, tam=22, cor=OXID, peso=700)]
        else:
            p.append(icone("t:brain", x + 190, 120, 140, MUDO))
            p.append(icone("t:check", x + 340, 130, 50, OXID))
    return slide("equivocos", 380, p, rs, eyebrow="A definição do consenso de Amsterdã", titulo="Três equívocos que ela resolve",
                 destaque="Os sintomas podem aparecer em minutos ou horas. Quem estava bem no intervalo e piora à noite continua suspeito.",
                 destaque_cor="petr", fonte="Consenso de Amsterdã, Br J Sports Med 2023")


def sinais_66():
    """6.6: seis sinais, e qualquer um deles leva para fora de campo."""
    p = [svg_abre(1664, 400, "Seis sinais em ladrilhos, todos ligados a uma saída à direita: fora de campo. Demora para levantar sem causa aparente; incoordenação, cambaleio e passos instáveis; olhar vago, parado, desconectado; postura tônica ou abalos, com retirada imediata e avaliação urgente; confusão, não sabe o placar, repete perguntas; e o que ele relata: dor de cabeça, náusea, tontura, lentidão. Um único sinal basta"), defs(FOSF)]
    rs = []
    itens = [("t:clock", "Demora para levantar", "sem causa aparente", FOSF), ("t:walk", "Incoordenação", "cambaleio, passos instáveis", FOSF),
             ("t:eye-off", "Olhar vago", "parado, desconectado", FOSF), ("t:alert-triangle", "Postura tônica ou abalos", "retirada imediata e avaliação urgente", FOSF),
             ("t:mood-confuzed", "Confusão", "não sabe o placar, repete perguntas", GLIC), ("t:message-circle", "O que ele relata", "dor de cabeça, náusea, tontura, lentidão", GLIC)]
    for k, (ic, t, d, cor) in enumerate(itens):
        col, lin = k % 3, k // 3
        x, y = col * 410, lin * 206
        p.append(caixa(x, y, 390, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 20, y + 20, 48, cor))
        rs += [rot(x + 80, y + 26, t, w=290, tam=24, cor=cor, peso=700, lh=1.15), rot(x + 20, y + 106, d, w=350, tam=22, cor=TINTA, lh=1.3)]
    p.append(seta(1240, 200, 1300, 200, FOSF, "m0", esp=6))
    p.append(caixa(1320, 60, 344, 280, FOSF, FOSF, esp=0, rx=18))
    p.append(icone("t:door-exit", 1452, 90, 80, PAPEL))
    rs += [rot(1330, 190, "um sinal basta", w=324, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1340, 240, "sai de campo para ser avaliado", w=304, tam=22, cor=PAPEL, alinha="center", lh=1.3)]
    return slide("sinais", 400, p, rs, eyebrow="Decisão à beira do campo", titulo="Um único sinal basta")


def retira_66():
    """6.6: reconhecer, retirar, avaliar: quem faz cada parte e com que ferramenta."""
    p = [svg_abre(1664, 380, "Um fluxo em três partes. Reconhecer: qualquer pessoa, com o cartão CRT6, feito para quem não é da saúde; não diagnostica, decide quem sai para ser avaliado. Retirar: não volta no mesmo dia, em nenhuma idade. Avaliar: o médico, com o SCAT6 a partir de 13 anos e o Child SCAT6 de 8 a 12, com maior sensibilidade até 72 horas; depois de uma semana, a versão de consultório"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 620, 380, OXID, OXID_T, esp=2, rx=18))
    p.append(icone("t:users", 24, 22, 48, OXID))
    rs += [rot(88, 28, "Reconhecer: qualquer pessoa", w=520, tam=27, cor=OXID, peso=700, serif=True)]
    for k, t in enumerate(["cartão CRT6", "feito para quem não é da saúde", "não diagnostica", "decide quem sai para ser avaliado"]):
        y = 104 + k * 64
        p.append(icone("t:check", 24, y, 34, OXID))
        rs.append(rot(70, y + 2, t, w=530, tam=23, cor=TINTA))
    p.append(seta(630, 190, 690, 190, MUDO, "m0", esp=4))
    p.append(caixa(700, 90, 264, 200, FOSF, FOSF, esp=0, rx=18))
    p.append(icone("t:door-exit", 800, 108, 64, PAPEL))
    rs.append(rot(712, 186, "retira: não volta no mesmo dia", w=240, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.25))
    p.append(seta(974, 190, 1034, 190, MUDO, "m0", esp=4))
    p.append(caixa(1044, 0, 620, 380, TINTA, CARTAO, esp=2, rx=18))
    p.append(icone("t:stethoscope", 1068, 22, 48, TINTA))
    rs += [rot(1132, 28, "Avaliar: o médico", w=510, tam=27, cor=TINTA, peso=700, serif=True)]
    for k, (a, b) in enumerate([("SCAT6", "13 anos ou mais"), ("Child SCAT6", "8 a 12 anos"), ("até 72 h", "maior sensibilidade"), ("após 1 semana", "versão de consultório")]):
        y = 104 + k * 64
        rs += [rot(1068, y, a, w=220, tam=24, cor=TINTA, peso=700), rot(1300, y + 2, b, w=340, tam=23, cor=TINTA)]
    return slide("retira", 380, p, rs, eyebrow="Reconheceu, retira", titulo="Não volta no mesmo dia, em nenhuma idade",
                 destaque="Retirar não é diagnosticar. É tirar do risco quem pode estar lesionado.", destaque_cor="petr",
                 fonte="SCAT6 e CRT6, Br J Sports Med 2023")


def alarme_66():
    """6.6: três grupos de sinais de alarme convergindo para a conduta: não mover, 192, hospital."""
    p = [svg_abre(1664, 380, "Três grupos de sinais de alarme, à esquerda, convergem para a conduta, à direita: não mover, ligar 192, hospital. Consciência: perda prolongada ou nível piorando, comportamento muito alterado. Cabeça: vômitos repetidos, dor que piora, pupilas diferentes, convulsão. Neurológico e coluna: fraqueza, formigamento, fala arrastada, suspeita de lesão cervical"), defs(FOSF)]
    rs = []
    itens = [("t:eye-off", "Consciência", "perda prolongada ou nível piorando; comportamento muito alterado"),
             ("h:head", "Cabeça", "vômitos repetidos, dor que piora, pupilas diferentes, convulsão"),
             ("t:bolt", "Neurológico e coluna", "fraqueza, formigamento, fala arrastada, suspeita de lesão cervical")]
    for k, (ic, t, d) in enumerate(itens):
        y = k * 130
        p.append(caixa(0, y, 1000, 116, FOSF, FOSF_T, esp=2, rx=16))
        p.append(icone(ic, 22, y + 30, 52, FOSF))
        rs += [rot(96, y + 14, t, w=880, tam=26, cor=FOSF, peso=700, serif=True), rot(96, y + 60, d, w=880, tam=22, cor=TINTA)]
        p.append(f'<path d="M 1000 {y + 58} C 1060 {y + 58}, 1080 190, 1130 190" fill="none" stroke="{FOSF}" stroke-width="3" marker-end="url(#m0)"/>')
    p.append(caixa(1150, 40, 514, 300, FOSF, FOSF, esp=0, rx=18))
    for k, (ic, t) in enumerate([("t:hand-stop", "não mover"), ("t:phone-call", "192"), ("t:building-hospital", "hospital")]):
        y = 70 + k * 86
        p.append(icone(ic, 1190, y, 52, PAPEL))
        rs.append(rot(1262, y + 8, t, w=380, tam=32, cor=PAPEL, peso=700, serif=True))
    return slide("alarme", 380, p, rs, eyebrow="Quando a suspeita vira emergência", titulo="Não mover, 192, hospital")


def cultura_66():
    """6.6: as duas pressões que empurram para ficar em campo e a regra que empurra de volta."""
    p = [svg_abre(1664, 380, "No centro, a decisão de ficar ou sair de campo. Da esquerda, duas pressões empurram para ficar: o atleta subnotifica, por vaga, contrato ou final, e o órgão lesionado é o que se autoavalia; o técnico decide sob pressão, não por maldade, mas pela função. Da direita, a regra empurra para sair: a substituição adicional por concussão, aprovada pela IFAB em 2024 e adotada pela CBF, que não conta nas trocas normais e tira o peso do banco"), defs(GLIC, OXID)]
    rs = []
    for k, (t, d) in enumerate([("O atleta subnotifica", "vaga, contrato, final; o órgão lesionado é o que se autoavalia; “disse que está bem” não é dado clínico"),
                                ("O técnico decide sob pressão", "não é maldade, é a função; a retirada não deveria depender dele")]):
        y = k * 196
        p.append(caixa(0, y, 560, 184, GLIC, GLIC_T, esp=2, rx=16))
        rs += [rot(24, y + 18, t, w=510, tam=26, cor=GLIC, peso=700, serif=True), rot(24, y + 66, d, w=510, tam=21, cor=TINTA, lh=1.3)]
        p.append(seta(570, y + 92, 690, 190, GLIC, "m0", esp=4))
    p.append(f'<circle cx="832" cy="190" r="120" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    p.append(icone("t:soccer-field", 792, 110, 80, TINTA))
    rs.append(rot(722, 206, "fica ou sai?", w=220, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
    p.append(seta(1090, 190, 974, 190, OXID, "m1", esp=5))
    p.append(caixa(1104, 0, 560, 380, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:arrows-exchange", 1128, 22, 52, OXID))
    rs += [rot(1196, 26, "A regra tira o peso do banco", w=450, tam=26, cor=OXID, peso=700, serif=True, lh=1.15),
           rot(1128, 120, "substituição adicional por concussão", w=510, tam=24, cor=TINTA, peso=700),
           rot(1128, 190, "aprovada pela IFAB em 2024; adotada pela CBF, a primeira confederação da FIFA a implantá-la", w=510, tam=21, cor=TINTA, lh=1.3),
           rot(1128, 300, "não conta nas trocas normais", w=510, tam=22, cor=OXID, peso=700)]
    return slide("cultura", 380, p, rs, eyebrow="Por que a regra é quebrada", titulo="E o que ajuda a cumpri-la",
                 fonte="IFAB 2024 · CBF, relatório dos campeonatos brasileiros de 2024")


def repouso_66():
    """6.6: duas linhas do tempo: o repouso absoluto antigo e o repouso relativo com volta gradual."""
    p = [svg_abre(1664, 380, "Duas linhas do tempo, em esquema. Em cima, a orientação antiga: repouso absoluto até zerar os sintomas, quarto escuro, sem tela e sem escola, por dias, desenhado como uma faixa parada. Embaixo, a orientação atual: repouso relativo de 24 a 48 horas, com tela limitada e sono priorizado; depois, movimento leve abaixo do limiar de sintoma, numa linha que sobe aos poucos; uma piora breve de até dois pontos na escala de sintomas é tolerada")]
    rs = []
    X0 = 330
    rs += [rot(0, 20, "A orientação antiga", w=300, tam=26, cor=FOSF, peso=700, serif=True),
           rot(0, 64, "quarto escuro, sem tela, sem escola, por dias", w=300, tam=20, cor=TINTA, lh=1.25)]
    p.append(f'<rect x="{X0}" y="40" width="1300" height="60" rx="8" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    rs.append(rot(X0 + 24, 56, "repouso absoluto até zerar", w=900, tam=24, cor=FOSF, peso=700))
    rs += [rot(0, 190, "A orientação atual", w=300, tam=26, cor=OXID, peso=700, serif=True),
           rot(0, 234, "tela limitada, sono priorizado; álcool não", w=300, tam=20, cor=TINTA, lh=1.25)]
    p.append(f'<rect x="{X0}" y="300" width="260" height="50" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(X0 + 10, 310, "24 a 48 h relativo", w=240, tam=21, cor=OXID, peso=700, alinha="center"))
    p.append(f'<path d="M {X0 + 260} 300 C {X0 + 600} 290, {X0 + 900} 220, {X0 + 1300} 170" fill="none" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<path d="M {X0 + 260} 270 C {X0 + 600} 260, {X0 + 900} 190, {X0 + 1300} 140 L {X0 + 1300} 170 C {X0 + 900} 220, {X0 + 600} 290, {X0 + 260} 300 Z" fill="{OXID}" opacity="0.15"/>')
    rs += [rot(X0 + 620, 176, "movimento leve abaixo do limiar, subindo aos poucos", w=520, tam=21, cor=OXID, peso=700),
           rot(X0 + 820, 300, "faixa: piora breve de até 2 pontos é tolerada", w=480, tam=19, cor=MUDO),
           rot(X0, 356, "esquema", w=200, tam=18, cor=MUDO)]
    return slide("repouso", 380, p, rs, eyebrow="Decisão na casa da família", titulo="A recomendação mudou",
                 destaque="Álcool não. Analgésico só com orientação. Sinais de alarme entregues por escrito.", destaque_cor="tinta",
                 fonte="Consenso de Amsterdã 2023")


def escola_66():
    """6.6: duas trilhas em paralelo, a cognitiva e a física, com o contato no fim."""
    p = [svg_abre(1664, 400, "Duas trilhas em paralelo. Em cima, a trilha cognitiva: atividade cognitiva é carga; meia jornada, pausas, prova adiada, combinado por escrito, até a jornada inteira. Embaixo, a trilha física: movimento leve em paralelo, que sobe aos poucos; o contato fica para o fim, depois que a escola voltou inteira. No adulto, o trabalho: motorista, máquina e altura têm critério de segurança próprio"), defs(MUDO)]
    rs = []
    rs += [rot(0, 0, "Escola e trabalho", w=300, tam=26, cor=OXID, peso=700, serif=True), rot(0, 40, "atividade cognitiva é carga", w=300, tam=20, cor=TINTA)]
    for k, t in enumerate(["meia jornada, com pausas", "prova adiada, combinado por escrito", "jornada inteira"]):
        x = 320 + k * 420
        p.append(caixa(x, 0, 400, 80, OXID, OXID_T, esp=2, rx=12))
        rs.append(rot(x + 16, 24, t, w=368, tam=22, cor=TINTA, peso=600, alinha="center"))
        if k < 2:
            p.append(seta(x + 402, 40, x + 416, 40, MUDO, "m0", esp=3))
    rs += [rot(0, 150, "Movimento", w=300, tam=26, cor=GLIC, peso=700, serif=True), rot(0, 190, "leve, em paralelo", w=300, tam=20, cor=TINTA)]
    for k, t in enumerate(["leve, abaixo do limiar", "moderado", "treino sem contato"]):
        x = 320 + k * 420
        p.append(caixa(x, 150, 400, 80, GLIC, GLIC_T, esp=2, rx=12))
        rs.append(rot(x + 16, 174, t, w=368, tam=22, cor=TINTA, peso=600, alinha="center"))
        if k < 2:
            p.append(seta(x + 402, 190, x + 416, 190, MUDO, "m0", esp=3))
    p.append(f'<line x1="1500" y1="80" x2="1500" y2="260" stroke="{OXID}" stroke-width="3"{TRACO}/>')
    p.append(caixa(1440, 260, 224, 80, FOSF, FOSF, esp=0, rx=12))
    rs += [rot(1440, 284, "contato, no fim", w=224, tam=23, cor=PAPEL, peso=700, alinha="center"),
           rot(1060, 266, "só depois da escola inteira", w=370, tam=20, cor=OXID, peso=700, alinha="right")]
    p.append(caixa(0, 300, 1060, 100, MUDO, PAPEL, esp=2, rx=14))
    p.append(icone("t:briefcase", 20, 326, 48, TINTA))
    rs.append(rot(84, 318, "No adulto, o trabalho: motorista, máquina, altura têm critério de segurança próprio", w=960, tam=22, cor=TINTA, lh=1.3))
    return slide("escola", 400, p, rs, eyebrow="A ordem que quase todo mundo inverte", titulo="Escola e trabalho antes do contato")


def escada_66():
    """6.6: os seis degraus do retorno ao esporte, com a seta de recuo."""
    p = [svg_abre(1664, 400, "Uma escada de seis degraus, cada um com pelo menos 24 horas. Um: atividade limitada por sintoma. Dois: aeróbico leve, cerca de 55 por cento da frequência máxima, depois moderado. Três: exercício do esporte, individual, sem impacto na cabeça. Nos três primeiros, sintoma leve e breve é tolerado. Quatro: treino sem contato, intenso, com força, com sintomas no basal. Cinco: treino com contato, depois da liberação médica. Seis: jogo. Uma seta mostra que sintoma que volta faz retroceder um degrau"), defs(FOSF)]
    rs = []
    degraus = [("atividade limitada por sintoma", OXID), ("aeróbico leve (≈ 55% da FC máx.), depois moderado", OXID), ("exercício do esporte, individual, sem impacto na cabeça", OXID),
               ("treino sem contato, intenso, com força", GLIC), ("treino com contato", FOSF), ("jogo", FOSF)]
    for k, (t, cor) in enumerate(degraus):
        x, w = k * 277, 270
        y = 270 - k * 46
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{400 - y}" rx="8" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="4" fill="{cor}"/>')
        rs += [rot(x + 14, y + 22, str(k + 1), w=60, tam=30, cor=cor, peso=700, serif=True),
               rot(x + 14, y + 56, t, w=w - 28, tam=19, cor=TINTA, lh=1.25)]
    rs += [rot(0, 40, "cada degrau: pelo menos 24 horas", w=700, tam=22, cor=TINTA, peso=700),
           rot(0, 76, "1 a 3: sintoma leve e breve tolerado · 4: sintomas no basal · 5: liberação médica", w=780, tam=20, cor=MUDO, lh=1.3)]
    p.append(f'<path d="M 1420 34 C 1380 -6, 1290 0, 1250 76" fill="none" stroke="{FOSF}" stroke-width="4" marker-end="url(#m0)"/>')
    rs.append(rot(860, 0, "sintoma volta: desce um degrau", w=380, tam=21, cor=FOSF, peso=700, alinha="right"))
    return slide("escada", 400, p, rs, eyebrow="Decisão no vestiário", titulo="Seis degraus, pelo menos 24 horas cada",
                 destaque="Sintoma que volta faz retroceder. Assintomático em repouso não é liberado: o teste é tolerar carga.", destaque_cor="verm",
                 fonte="Estratégia de retorno ao esporte, consenso de Amsterdã 2023")


def demora_66():
    """6.6: a maioria em quatro semanas, a fração que demora mais, e as quatro frentes."""
    p = [svg_abre(1664, 380, "Uma barra de cem por cento: a maioria dos jovens e adultos se recupera em até quatro semanas; de 20 a 30 por cento seguem com sintoma por mais tempo, faixa mostrada como intervalo. À direita, as quatro frentes de tratamento de quem demora: pescoço, sistema vestibular, visão, e humor e sono")]
    rs = []
    rs.append(rot(0, 0, "Jovens e adultos com concussão", w=900, tam=22, cor=MUDO, peso=700))
    p.append(f'<rect x="0" y="50" width="900" height="80" rx="8" fill="{OXID}"/>')
    p.append(f'<rect x="630" y="50" width="270" height="80" fill="{GLIC}"/>')
    p.append(f'<rect x="630" y="50" width="90" height="80" fill="{GLIC_T}"/>')
    p.append(f'<line x1="630" y1="40" x2="630" y2="140" stroke="{GLIC}" stroke-width="3"/>')
    rs += [rot(20, 74, "a maioria: recuperada em até 4 semanas", w=600, tam=23, cor=PAPEL, peso=700),
           rot(630, 150, "20 a 30%: sintoma por mais tempo", w=270, tam=22, cor=GLIC, peso=700, alinha="right", lh=1.2),
           rot(0, 230, "esperar parado é o erro: quem demora tem frentes tratáveis", w=880, tam=23, cor=TINTA, lh=1.3)]
    for k, (ic, t) in enumerate([("t:stretching", "pescoço"), ("h:ear", "sistema vestibular"), ("t:eye", "visão"), ("t:moon", "humor e sono")]):
        col, lin = k % 2, k // 2
        x, y = 980 + col * 344, lin * 190
        p.append(caixa(x, y, 324, 174, TINTA, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 132, y + 24, 60, TINTA))
        rs.append(rot(x + 12, y + 104, t, w=300, tam=24, cor=TINTA, peso=700, alinha="center"))
    return slide("demora", 380, p, rs, eyebrow="Quando a recuperação demora", titulo="Não é frescura, e esperar parado é o erro",
                 destaque="Encefalopatia traumática crônica: preocupação legítima, associação descrita, causa e risco individual não estabelecidos. Reduzir exposição já se justifica hoje.",
                 destaque_cor="tinta", fonte="Consenso de Amsterdã 2023")


def prevencao_66():
    """6.6: as reduções com dado, em barras, e o que não tem evidência, riscado."""
    p = [svg_abre(1664, 380, "Três barras de redução de concussão, cada uma de um conjunto de estudos. Sem body checking no hóquei de crianças e adolescentes: 58 por cento menos. Com protetor bucal nos esportes de colisão: cerca de 26 por cento menos. Com aquecimento neuromuscular no rugby: até 60 por cento menos. À direita, riscados, o que não tem evidência para vender como prevenção: faixa de cabeça, suplemento neuroprotetor, imagem de rotina")]
    rs = []
    X0, esc = 420, 10
    for k, (t, v, lab, cor) in enumerate([("regra: sem body checking no hóquei jovem", 58, "58%", OXID), ("protetor bucal, esportes de colisão", 26, "≈ 26%", GLIC), ("aquecimento neuromuscular no rugby", 60, "até 60%", OXID)]):
        y = 20 + k * 110
        rs.append(rot(0, y + 12, t, w=400, tam=22, cor=TINTA, peso=600, lh=1.2))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * esc}" height="70" rx="4" fill="{cor}"/>')
        rs.append(rot(X0 + v * esc + 16, y + 16, lab, w=160, tam=30, cor=cor, peso=700, serif=True))
    p.append(f'<line x1="{X0}" y1="0" x2="{X0}" y2="340" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(X0, 346, "menos concussão, em redução relativa; estudos diferentes", w=700, tam=18, cor=MUDO))
    rs.append(rot(1210, 0, "Sem evidência como prevenção", w=454, tam=24, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["faixa de cabeça", "suplemento neuroprotetor", "imagem de rotina"]):
        y = 60 + k * 90
        p.append(caixa(1210, y, 454, 70, FOSF, FOSF_T, esp=2, rx=35))
        rs.append(rot(1230, y + 20, t, w=414, tam=23, cor=TINTA, alinha="center"))
        p.append(f'<line x1="{1437 - len(t) * 6.5:.0f}" y1="{y + 35}" x2="{1437 + len(t) * 6.5:.0f}" y2="{y + 35}" stroke="{FOSF}" stroke-width="3"/>')
    return slide("prevencao", 380, p, rs, eyebrow="Prevenção com dado", titulo="Regra primeiro, equipamento depois",
                 destaque="Custo zero: ensinar a comissão e limitar contato no treino.", destaque_cor="verm",
                 fonte="Revisão sistemática do consenso, Br J Sports Med 2023")

# ---------------------------------------------------------------- 6.7

def perfis_67():
    """6.7: três pessoas com bombinha e a régua que decide por elas."""
    p = [svg_abre(1664, 400, "Três pessoas com bombinha na mão. O adolescente afastado da educação física desde a infância. A nadadora que tosse depois de todo treino. O corredor que usa a bombinha de um amigo antes da prova fria. Embaixo, uma régua comum às três: o que decide é a queda do VEF1 medida, de pelo menos dez por cento, não a queixa")]
    rs = []
    itens = [("t:school", "O adolescente", "afastado da educação física desde a infância", OXID, OXID_T),
             ("t:swimming", "A nadadora", "tosse depois de todo treino", AZUL, AZUL_T),
             ("t:run", "O corredor", "usa a bombinha de um amigo antes da prova fria", GLIC, GLIC_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 230, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 56, cor))
        rs += [rot(x + 96, 34, t, w=410, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 110, d, w=480, tam=23, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 264}" y1="230" x2="{x + 264}" y2="280" stroke="{BORDA}" stroke-width="3"/>')
    p.append(caixa(0, 280, 1664, 120, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(30, 304, "A queixa não decide.", w=600, tam=30, cor=PAPEL, peso=700, serif=True),
           rot(30, 350, "o número decide: queda medida do VEF1", w=900, tam=22, cor=PAPEL),
           rot(1100, 296, "≥ 10%", w=520, tam=64, cor=PAPEL, peso=700, serif=True, alinha="right")]
    return slide("perfis", 400, p, rs, eyebrow="Três pessoas com bombinha na mão", titulo="Em nenhuma delas a queixa decide")


def numeros_67():
    """6.7: três números ao longo do caminho: diagnóstico, uso, limite."""
    p = [svg_abre(1664, 360, "Um caminho em três etapas, cada uma com o seu número. Diagnóstico: queda de dez por cento do VEF1. Uso: quinze minutos entre o broncodilatador e o esforço. Limite: 1.600 microgramas por dia, o teto do salbutamol inalado"), defs(MUDO)]
    rs = []
    itens = [("Diagnóstico", "10%", "queda do VEF1 que define o diagnóstico", TINTA, PAPEL, "t:chart-line"),
             ("Uso", "15 min", "entre o broncodilatador e o esforço", OXID, OXID_T, "t:clock"),
             ("Limite", "1.600 µg", "teto diário do salbutamol inalado", FOSF, FOSF_T, "t:alert-triangle")]
    for k, (etapa, n, d, cor, fundo, ic) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 500, 360, cor, fundo, esp=2, rx=18))
        p.append(icone(ic, x + 24, 24, 48, cor))
        rs += [rot(x + 88, 32, etapa, w=380, tam=26, cor=cor, peso=700, serif=True),
               rot(x + 24, 110, n, w=460, tam=72, cor=cor, peso=700, serif=True),
               rot(x + 24, 230, d, w=450, tam=24, cor=TINTA, lh=1.3)]
        if k < 2:
            p.append(seta(x + 510, 180, x + 556, 180, MUDO, "m0", esp=4))
    return slide("numeros", 360, p, rs, eyebrow="Os números que atravessam a aula", titulo="Diagnóstico, uso e limite",
                 destaque="O rótulo errado afasta gente do esporte; a falta de rótulo deixa gente tossindo por anos. Os dois se resolvem com medida.", destaque_cor="tinta")


def mecanismo_67():
    """6.7: a cadeia do ar que passa ao músculo que contrai."""
    p = [svg_abre(1664, 380, "Em cima, a definição: estreitamento transitório das vias aéreas, durante ou logo depois do esforço, em quem tem asma e em quem não tem. Embaixo, a cadeia do mecanismo em quatro elos: ventilação alta e prolongada; o epitélio perde água e calor; os mastócitos liberam mediadores; o músculo liso contrai. Ao lado, o ar: frio e seco piora, morno e úmido melhora"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 1664, 110, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(24, 16, "Estreitamento transitório das vias aéreas", w=1000, tam=28, cor=OXID, peso=700, serif=True),
           rot(24, 62, "durante ou logo depois do esforço · em quem tem asma e em quem não tem", w=1600, tam=22, cor=TINTA)]
    elos = [("t:wave-sine", "ventilação alta e prolongada"), ("t:droplet", "epitélio perde água e calor"), ("t:bolt", "mastócitos liberam mediadores"), ("h:lungs", "o músculo liso contrai")]
    for k, (ic, t) in enumerate(elos):
        x = k * 330
        p.append(caixa(x, 150, 290, 170, GLIC, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 121, 168, 48, GLIC))
        rs.append(rot(x + 16, 236, t, w=258, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.25))
        if k < 3:
            p.append(seta(x + 294, 235, x + 326, 235, MUDO, "m0", esp=3))
    p.append(caixa(1340, 150, 324, 230, TINTA, CARTAO, esp=2, rx=14))
    rs += [rot(1360, 166, "O ar", w=290, tam=26, cor=TINTA, peso=700, serif=True),
           rot(1360, 214, "frio e seco: piora", w=290, tam=22, cor=FOSF, peso=700),
           rot(1360, 256, "morno e úmido: melhora", w=290, tam=22, cor=OXID, peso=700),
           rot(1360, 300, "o risco cresce com o volume de ar", w=290, tam=20, cor=TINTA, lh=1.25)]
    return slide("mecanismo", 380, p, rs, eyebrow="O que é", titulo="Com asma ou sem asma de base")


def prevalencia_67():
    """6.7: a faixa de 30 a 70% numa régua de zero a cem, e os três ambientes que concentram."""
    p = [svg_abre(1664, 360, "Uma régua de zero a cem por cento com a faixa de 30 a 70 por cento: a prevalência de broncoespasmo induzido por exercício em atletas, que varia com a modalidade e o critério diagnóstico. Embaixo, os três ambientes que concentram casos: inverno, com ar frio e seco; endurance, com muito ar por muito tempo; piscina coberta, com subprodutos de cloro")]
    rs = []
    X0, W = 40, 1580
    fx = lambda v: X0 + v / 100 * W
    p.append(f'<line x1="{X0}" y1="80" x2="{X0 + W}" y2="80" stroke="{BORDA}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<line x1="{fx(30):.0f}" y1="80" x2="{fx(70):.0f}" y2="80" stroke="{FOSF}" stroke-width="30" stroke-linecap="round"/>')
    for v in (0, 30, 70, 100):
        rs.append(rot(fx(v) - 60, 104, f"{v}%", w=120, tam=22 if v in (30, 70) else 19, cor=FOSF if v in (30, 70) else MUDO, peso=700 if v in (30, 70) else 400, alinha="center"))
    rs.append(rot(fx(30), 22, "atletas, conforme modalidade e critério", w=fx(70) - fx(30), tam=22, cor=FOSF, peso=700, alinha="center"))
    itens = [("t:temperature", "inverno", "ar frio e seco", OXID), ("t:run", "endurance", "muito ar, por muito tempo", GLIC), ("t:swimming", "piscina", "coberta, com subprodutos de cloro", AZUL)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 170, 528, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 24, 194, 56, cor))
        rs += [rot(x + 96, 202, t, w=410, tam=32, cor=cor, peso=700, serif=True), rot(x + 24, 280, d, w=480, tam=23, cor=TINTA)]
    return slide("prevalencia", 360, p, rs, eyebrow="Quem tem mais", titulo="Em atletas, de 30 a 70%",
                 destaque="Tosse depois do treino não é normal do esporte. E prevalência alta não autoriza tratar sem medir: o grupo sintomático tem muita gente com outra coisa.",
                 destaque_cor="verm", fonte="Varia com modalidade e critério diagnóstico")


def diferenciais_67():
    """6.7: seis imitadores e o círculo que o rótulo errado fecha."""
    p = [svg_abre(1664, 400, "À esquerda, seis diagnósticos que imitam broncoespasmo, cada um com a sua pista. Descondicionamento: falta de ar proporcional ao esforço; o tratamento é treinar. Rinite com respiração oral: o ar chega sem aquecer nem umidificar. Refluxo: tosse e aperto em posição e horário específicos. Padrão disfuncional e ansiedade: falta de ar real, pulmão normal. Deficiência de ferro e causa cardíaca: exame respiratório normal. À direita, o círculo cruel: o rótulo afasta, o afastamento descondiciona, o descondicionamento confirma o rótulo"), defs(GLIC)]
    rs = []
    itens = [("Descondicionamento", "falta de ar proporcional ao esforço; o tratamento é treinar"), ("Rinite com respiração oral", "ar que chega sem aquecer nem umidificar"),
             ("Refluxo", "tosse e aperto em posição e horário específicos"), ("Padrão disfuncional, ansiedade", "falta de ar real, pulmão normal"),
             ("Deficiência de ferro", "exame respiratório normal"), ("Causa cardíaca", "exame respiratório normal")]
    for k, (t, d) in enumerate(itens):
        col, lin = k % 2, k // 2
        x, y = col * 540, lin * 136
        p.append(caixa(x, y, 520, 124, TINTA, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, y + 14, t, w=480, tam=23, cor=TINTA, peso=700), rot(x + 20, y + 56, d, w=480, tam=21, cor=TINTA, lh=1.25)]
    import math as _m
    cx, cy, r = 1400, 200, 140
    nos = ["o rótulo afasta", "o afastamento descondiciona", "o descondicionamento confirma o rótulo"]
    angs = [-90, 30, 150]
    for k, a in enumerate(angs):
        a1, a2 = _m.radians(a + 22), _m.radians(angs[(k + 1) % 3] - 22 + (360 if k == 2 else 0))
        x1, y1 = cx + r * _m.cos(a1), cy + r * _m.sin(a1)
        x2, y2 = cx + r * _m.cos(a2), cy + r * _m.sin(a2)
        p.append(f'<path d="M {x1:.0f} {y1:.0f} A {r} {r} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="{GLIC}" stroke-width="5" marker-end="url(#m0)"/>')
    for k, (t, a) in enumerate(zip(nos, angs)):
        x, y = cx + r * _m.cos(_m.radians(a)), cy + r * _m.sin(_m.radians(a))
        rs.append(rot(min(x - 120, 1664 - 240), y - 26, t, w=240, tam=20, cor=GLIC, peso=700, alinha="center", lh=1.2))
    rs.append(rot(cx - 90, cy - 18, "o círculo cruel", w=180, tam=22, cor=TINTA, peso=700, alinha="center", serif=True))
    return slide("diferenciais", 400, p, rs, eyebrow="Antes de tratar", titulo="O que imita broncoespasmo")


def laringe_67():
    """6.7: quando cada um aparece em relação ao esforço (esquema), e as pistas de cada lado."""
    p = [svg_abre(1664, 400, "Em cima, em esquema, a intensidade do sintoma ao longo do tempo, com o esforço sombreado. A obstrução laríngea aparece no pico do esforço e some em um a dois minutos parado. O broncoespasmo piora depois do esforço. Embaixo, as pistas. Broncoespasmo: chiado na expiração, aperto no peito, responde ao broncodilatador. Obstrução laríngea: ruído na inspiração, o estridor, garganta fechando, não responde ao broncodilatador")]
    rs = []
    X0, X1, Yb = 0, 1664, 170
    p.append(f'<rect x="200" y="10" width="560" height="{Yb - 10}" fill="{AZUL_T}"/>')
    rs += [rot(210, 14, "esforço", w=300, tam=20, cor=MUDO, peso=700), rot(1300, 14, "esquema", w=360, tam=18, cor=MUDO, alinha="right")]
    p.append(f'<line x1="{X0}" y1="{Yb}" x2="{X1}" y2="{Yb}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<path d="M 200 {Yb} C 500 {Yb}, 680 40, 750 40 C 790 40, 800 {Yb}, 860 {Yb}" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<path d="M 600 {Yb} C 760 {Yb}, 820 70, 1000 60 C 1200 52, 1300 120, 1640 {Yb - 6}" fill="none" stroke="{OXID}" stroke-width="5"/>')
    rs += [rot(220, 46, "obstrução laríngea: no pico", w=380, tam=20, cor=FOSF, peso=700),
           rot(870, 138, "some em 1 a 2 min parado", w=280, tam=19, cor=FOSF),
           rot(1040, 30, "broncoespasmo: piora depois", w=400, tam=20, cor=OXID, peso=700)]
    for x, t, itens, cor, fundo in [(0, "Broncoespasmo", ["chiado na expiração", "aperto no peito", "responde ao broncodilatador"], OXID, OXID_T),
                                    (848, "Obstrução laríngea", ["ruído na inspiração, o estridor", "garganta fechando", "não responde ao broncodilatador"], FOSF, FOSF_T)]:
        p.append(caixa(x, 200, 816, 200, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, 214, t, w=760, tam=26, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            y = 262 + k * 42
            p.append(f'<circle cx="{x + 32}" cy="{y + 14}" r="7" fill="{cor}"/>')
            rs.append(rot(x + 50, y, it, w=740, tam=22, cor=TINTA))
    return slide("laringe", 400, p, rs, eyebrow="O diferencial que mais engana", titulo="Obstrução laríngea induzida pelo exercício",
                 destaque="Tratamento de fonoaudiologia e padrão respiratório. Não melhora com a bombinha: pense nela antes de subir a dose.", destaque_cor="tinta")


def camadas_67():
    """6.7: o tratamento como camadas empilhadas, com o aquecimento na base."""
    p = [svg_abre(1664, 400, "Quatro camadas empilhadas. Na base, o aquecimento: de graça, e é prescrição de treino. Acima, o beta-2 de curta ação quinze minutos antes, de uso intermitente; uso diário gera tolerância e é sinal. Acima, o corticoide inalatório de manutenção: broncoespasmo frequente na asma é asma mal controlada. No topo, alternativas e comorbidades: antileucotrieno, anti-histamínico na alergia, tratar a rinite")]
    rs = []
    camadas = [("Alternativas e comorbidades", "antileucotrieno, anti-histamínico na alergia, tratar a rinite", GLIC, GLIC_T, 1100),
               ("Corticoide inalatório de manutenção", "broncoespasmo frequente na asma é asma mal controlada", FOSF, FOSF_T, 1300),
               ("Beta-2 de curta ação, 15 minutos antes", "uso intermitente; diário gera tolerância e é sinal", OXID, OXID_T, 1480),
               ("Aquecimento", "de graça, e é prescrição de treino", OXID, OXID, 1664)]
    for k, (t, d, cor, fundo, w) in enumerate(camadas):
        y = k * 100
        x = (1664 - w) / 2
        p.append(caixa(x, y, w, 88, cor, fundo, esp=2, rx=12))
        cort = PAPEL if fundo == OXID else cor
        rs += [rot(x + 24, y + 12, t, w=w * 0.45, tam=24, cor=cort, peso=700, lh=1.15),
               rot(x + w * 0.47, y + 14, d, w=w * 0.5, tam=21, cor=PAPEL if fundo == OXID else TINTA, lh=1.25)]
    return slide("camadas", 400, p, rs, eyebrow="O tratamento, pela diretriz de 2013", titulo="Em camadas")


def aquecimento_67():
    """6.7: o aquecimento e as duas horas de proteção que ele deixa."""
    p = [svg_abre(1664, 360, "Uma linha do tempo. Primeiro, dez a quinze minutos de aquecimento moderado a vigoroso, intervalado ou combinado. Depois, um período refratário de cerca de duas horas em que o broncoespasmo vem atenuado, sombreado sobre a linha. Embaixo, três ajustes de ambiente: frio, bandana ou máscara; poluição e pólen, mudar o horário; piscina coberta, ventilação e qualidade da água")]
    rs = []
    p.append(f'<line x1="0" y1="120" x2="1664" y2="120" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<rect x="0" y="70" width="300" height="100" rx="10" fill="{OXID}"/>')
    rs += [rot(10, 82, "10 a 15 min", w=280, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(10, 126, "aquecimento intervalado", w=280, tam=20, cor=PAPEL, alinha="center")]
    p.append(f'<rect x="300" y="80" width="1100" height="80" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"{TRACO}/>')
    rs += [rot(320, 100, "≈ 2 h de broncoespasmo atenuado: o período refratário", w=1060, tam=24, cor=OXID, peso=700),
           rot(0, 18, "moderado a vigoroso, intervalado ou combinado: a recomendação para todos", w=1300, tam=21, cor=TINTA)]
    for k, (ic, t, d) in enumerate([("t:temperature", "Frio", "bandana ou máscara"), ("t:clock", "Poluição e pólen", "mudar o horário"), ("t:swimming", "Piscina coberta", "ventilação e qualidade da água fazem parte do problema")]):
        x = k * 568
        p.append(caixa(x, 210, 528, 150, GLIC, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 20, 232, 44, GLIC))
        rs += [rot(x + 80, 236, t, w=430, tam=24, cor=GLIC, peso=700), rot(x + 20, 290, d, w=490, tam=21, cor=TINTA, lh=1.25)]
    return slide("aquecimento", 360, p, rs, eyebrow="A camada de graça", titulo="O período refratário",
                 fonte="Diretriz da Sociedade Torácica Americana, 2013")


def doses_67():
    """6.7: quatro cartões de limite, um por inalado permitido."""
    p = [svg_abre(1664, 360, "Quatro cartões com os limites dos inalados permitidos. Salbutamol: 1.600 microgramas em 24 horas, até 600 em 8 horas. Formoterol: 54 microgramas em 24 horas, até 36 em 12 horas. Salmeterol: 200 microgramas em 24 horas, até 100 em 8 horas, novo em 2026. Vilanterol: 25 microgramas em 24 horas")]
    rs = []
    itens = [("Salbutamol", "1.600 µg", "até 600 µg em 8 h", ""), ("Formoterol", "54 µg", "até 36 µg em 12 h", ""),
             ("Salmeterol", "200 µg", "até 100 µg em 8 h", "novo em 2026"), ("Vilanterol", "25 µg", "", "")]
    for k, (t, d24, inter, nota) in enumerate(itens):
        x = k * 421
        p.append(caixa(x, 0, 400, 360, FOSF, CARTAO, esp=2, rx=16))
        p.append(f'<rect x="{x}" y="0" width="400" height="76" rx="16" fill="{FOSF_T}"/>')
        rs += [rot(x + 24, 20, t, w=360, tam=28, cor=FOSF, peso=700, serif=True),
               rot(x + 24, 100, "em 24 horas", w=360, tam=19, cor=MUDO, peso=700),
               rot(x + 24, 128, d24, w=360, tam=56, cor=TINTA, peso=700, serif=True)]
        if inter:
            p.append(icone("t:clock", x + 24, 236, 36, FOSF))
            rs.append(rot(x + 70, 240, inter, w=310, tam=22, cor=TINTA))
        if nota:
            rs.append(rot(x + 24, 300, nota, w=360, tam=20, cor=FOSF, peso=700))
    return slide("doses", 360, p, rs, eyebrow="Onde o atleta perde carreira por desatenção", titulo="Os limites dos inalados permitidos",
                 destaque="Oral, injetável ou acima do limite: só com autorização de uso terapêutico. Confira a lista vigente a cada temporada.",
                 destaque_cor="verm", fonte="Lista de substâncias proibidas da WADA, 2026, seção S3")


def urina_67():
    """6.7: as duas camadas do antidoping, a dose e a urina, e o que a autorização exige."""
    p = [svg_abre(1664, 360, "Duas camadas em sequência. A primeira, a dose inalada dentro do limite. A segunda, a concentração na urina: acima de 1.000 nanogramas por mililitro de salbutamol, ou 40 de formoterol, o achado é incompatível com uso terapêutico. À direita, o que a autorização de uso terapêutico exige: o teste documentado com queda de dez por cento"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 40, 400, 280, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(24, 60, "Camada 1", w=350, tam=20, cor=MUDO, peso=700), rot(24, 92, "A dose inalada", w=350, tam=28, cor=OXID, peso=700, serif=True),
           rot(24, 150, "dentro do limite de 24 horas e do intervalo", w=350, tam=22, cor=TINTA, lh=1.3)]
    p.append(seta(410, 180, 466, 180, MUDO, "m0", esp=4))
    p.append(caixa(480, 0, 680, 360, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(504, 20, "Camada 2", w=350, tam=20, cor=MUDO, peso=700), rot(504, 52, "A urina", w=600, tam=28, cor=FOSF, peso=700, serif=True),
           rot(504, 100, "acima disso, incompatível com uso terapêutico", w=630, tam=21, cor=TINTA)]
    for k, (t, n) in enumerate([("salbutamol", "1.000"), ("formoterol", "40")]):
        y = 160 + k * 96
        rs += [rot(504, y + 18, t, w=220, tam=24, cor=TINTA, peso=700), rot(730, y, n, w=230, tam=52, cor=FOSF, peso=700, serif=True, alinha="right"),
               rot(970, y + 24, "ng/mL", w=160, tam=22, cor=MUDO)]
    p.append(caixa(1200, 0, 464, 360, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:clipboard-check", 1224, 24, 52, TINTA))
    rs += [rot(1290, 34, "A autorização exige", w=360, tam=24, cor=TINTA, peso=700, serif=True),
           rot(1224, 110, "10%", w=420, tam=64, cor=TINTA, peso=700, serif=True),
           rot(1224, 200, "o teste documentado, com a queda do VEF1", w=420, tam=22, cor=TINTA, lh=1.3)]
    return slide("urina", 360, p, rs, eyebrow="A segunda camada do antidoping", titulo="Dose certa não garante urina limpa",
                 destaque="Sem diagnóstico objetivo, não há autorização. Registre princípio ativo, dose e horário, e nunca use a bombinha de outra pessoa.",
                 destaque_cor="tinta", fonte="WADA 2026")

# ---------------------------------------------------------------- 6.8

def mensagens_68():
    """6.8: três mensagens no mesmo dia, como degraus de uma escada."""
    p = [svg_abre(1664, 400, "Três mensagens no mesmo dia, desenhadas como degraus. A primeira, garganta arranhando, treino hoje?, se decide à beira do treino. A segunda, a febre passou ontem, posso correr?, pede um plano de dias. A terceira, falaram em miocardite, mas estou ótimo, sai das mãos da comissão")]
    rs = []
    itens = [("“Garganta arranhando, treino hoje?”", "decide-se à beira do treino", OXID, OXID_T),
             ("“A febre passou ontem, posso correr?”", "pede um plano de dias", GLIC, GLIC_T),
             ("“Falaram em miocardite, mas estou ótimo.”", "sai das mãos da comissão", FOSF, FOSF_T)]
    for k, (q, d, cor, fundo) in enumerate(itens):
        x, y = k * 560, 250 - k * 120
        p.append(f'<path d="M {x + 16} {y} H {x + 504} Q {x + 520} {y} {x + 520} {y + 16} V {y + 104} Q {x + 520} {y + 120} {x + 504} {y + 120} H {x + 70} L {x + 30} {y + 150} L {x + 40} {y + 120} H {x + 16} Q {x} {y + 120} {x} {y + 104} V {y + 16} Q {x} {y} {x + 16} {y} Z" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(x + 22, y + 16, q, w=480, tam=25, cor=cor, peso=700, serif=True, lh=1.2))
        rs.append(rot(x + 80, y + 126 if k == 0 else y + 126, d, w=440, tam=21, cor=TINTA, peso=600))
    return slide("mensagens", 400, p, rs, eyebrow="Três mensagens no mesmo dia", titulo="Uma escada de três decisões")


def leituras_68():
    """6.8: a janela aberta riscada, e os fatores de carga que explicam quem adoece."""
    p = [svg_abre(1664, 380, "À esquerda, a leitura antiga, riscada: o esforço intenso suprime a imunidade, o atleta fica vulnerável por horas, e a solução vira suplemento. À direita, a leitura atual: a queda de linfócitos depois do esforço é redistribuição; treino regular melhora a imunidade; a doença acompanha carga mal gerida, sono, energia e viagem; e a solução é gestão"), defs(OXID)]
    rs = []
    p.append(caixa(0, 0, 640, 380, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(24, 18, "A leitura antiga: a janela aberta", w=590, tam=26, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["esforço intenso suprime a imunidade", "o atleta fica vulnerável por horas", "a solução vira suplemento"]):
        y = 100 + k * 76
        rs.append(rot(24, y, t, w=590, tam=24, cor=TINTA))
        p.append(f'<line x1="24" y1="{y + 15}" x2="{24 + len(t) * 11.5:.0f}" y2="{y + 15}" stroke="{FOSF}" stroke-width="2"/>')
    p.append(caixa(700, 0, 964, 380, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(724, 18, "A leitura atual: gestão de carga", w=900, tam=26, cor=OXID, peso=700, serif=True),
           rot(724, 72, "a queda de linfócitos é redistribuição; treino regular melhora a imunidade", w=900, tam=22, cor=TINTA, lh=1.3)]
    fat = [("t:barbell", "carga mal gerida"), ("t:moon", "sono"), ("t:salad", "energia"), ("t:plane", "viagem")]
    for k, (ic, t) in enumerate(fat):
        x = 724 + k * 166
        p.append(caixa(x, 160, 150, 120, OXID, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 51, 174, 48, OXID))
        rs.append(rot(x + 6, 232, t, w=138, tam=19, cor=TINTA, peso=600, alinha="center", lh=1.15))
    p.append(caixa(1390, 150, 250, 210, TINTA, TINTA, esp=0, rx=14))
    rs += [rot(1400, 190, "a doença acompanha", w=230, tam=20, cor=PAPEL, alinha="center"), rot(1400, 240, "a solução é gestão", w=230, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.15)]
    return slide("leituras", 380, p, rs, eyebrow="Antes das decisões", titulo="Janela aberta ou gestão de carga",
                 destaque="Quem adoece três, quatro vezes por temporada quase nunca tem problema imunológico. Tem problema de planejamento.",
                 destaque_cor="tinta", fonte="Revisão de 2018, Front Immunol · Consenso do COI, Br J Sports Med 2016")


def pescoco_68():
    """6.8: a silhueta com a linha no pescoço: acima, treino leve; abaixo, não treina."""
    p = [svg_abre(1664, 400, "No centro, uma silhueta com uma linha tracejada na altura do pescoço. Acima do pescoço e sem febre, à esquerda: coriza, espirro, nariz entupido, dor de garganta leve; treino leve a moderado, com reavaliação no dia seguinte. Abaixo do pescoço, à direita: febre, calafrio, tosse produtiva, aperto no peito, falta de ar, dor muscular difusa, vômito, diarreia; não treina")]
    rs = []
    p.append(icone("h:person", 682, 20, 300, MUDO))
    p.append(f'<line x1="560" y1="118" x2="1104" y2="118" stroke="{TINTA}" stroke-width="4"{TRACO}/>')
    rs.append(rot(712, 0, "o pescoço", w=240, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(caixa(0, 0, 540, 236, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(24, 16, "Acima do pescoço, sem febre", w=500, tam=25, cor=OXID, peso=700, serif=True),
           rot(24, 66, "coriza, espirro, nariz entupido; dor de garganta leve", w=490, tam=22, cor=TINTA, lh=1.3)]
    p.append(caixa(24, 150, 492, 70, OXID, OXID, esp=0, rx=35))
    rs.append(rot(34, 162, "treino leve a moderado; reavalia no dia seguinte", w=472, tam=20, cor=PAPEL, peso=700, alinha="center", lh=1.2))
    p.append(caixa(1124, 140, 540, 260, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(1148, 156, "Abaixo do pescoço", w=500, tam=25, cor=FOSF, peso=700, serif=True),
           rot(1148, 204, "febre, calafrio, tosse produtiva; aperto no peito, falta de ar; dor muscular difusa, vômito, diarreia", w=490, tam=21, cor=TINTA, lh=1.3)]
    p.append(caixa(1148, 320, 492, 64, FOSF, FOSF, esp=0, rx=32))
    rs.append(rot(1158, 338, "não treina", w=472, tam=24, cor=PAPEL, peso=700, alinha="center"))
    return slide("pescoco", 400, p, rs, eyebrow="A mensagem da sexta", titulo="O teste do pescoço",
                 destaque="Pragmática e útil, sem ensaio de alta qualidade por trás. Leve é leve de verdade, a decisão de sexta não vale para sábado, e um sintoma de baixo basta.",
                 destaque_cor="ambar")


def excecoes_68():
    """6.8: o teste do pescoço suspenso por três exceções."""
    p = [svg_abre(1664, 360, "À esquerda, o teste do pescoço, em cinza: não vale quando aparece uma das três exceções. À direita, as exceções que mandam parar e avaliar, onde quer que esteja o sintoma: qualquer febre, a linha vermelha da aula; sintoma cardiopulmonar, como dor no peito, palpitação, falta de ar desproporcional ou tontura no esforço; e doença transmissível na equipe, porque vestiário, ônibus e alojamento espalham, e afastar protege o grupo"), defs(FOSF)]
    rs = []
    p.append(caixa(0, 60, 400, 240, MUDO, PAPEL, esp=2, rx=16))
    p.append(icone("h:person", 140, 80, 120, MUDO))
    p.append(f'<line x1="40" y1="128" x2="360" y2="128" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
    rs += [rot(20, 216, "o teste do pescoço", w=360, tam=24, cor=TINTA, peso=700, alinha="center"),
           rot(20, 252, "não vale quando:", w=360, tam=21, cor=FOSF, peso=700, alinha="center")]
    p.append(seta(410, 180, 470, 180, FOSF, "m0", esp=4))
    itens = [("t:temperature", "Qualquer febre", "é a linha vermelha da aula", FOSF, FOSF_T),
             ("t:heartbeat", "Sintoma cardiopulmonar", "dor no peito, palpitação, falta de ar desproporcional, tontura no esforço", FOSF, FOSF_T),
             ("t:users-group", "Doença transmissível na equipe", "vestiário, ônibus e alojamento: afastar protege o grupo", GLIC, GLIC_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(itens):
        y = k * 122
        p.append(caixa(490, y, 1174, 110, cor, fundo, esp=2, rx=14))
        p.append(icone(ic, 512, y + 28, 52, cor))
        rs += [rot(588, y + 14, t, w=1050, tam=25, cor=cor, peso=700, serif=True), rot(588, y + 58, d, w=1050, tam=21, cor=TINTA)]
    return slide("excecoes", 360, p, rs, eyebrow="Quando o teste do pescoço não vale", titulo="Parar e avaliar, onde quer que esteja o sintoma")


def febre_68():
    """6.8: a febre no centro e os quatro motivos que saem dela."""
    p = [svg_abre(1664, 380, "No centro, a febre. Saem dela quatro motivos para não treinar. O coração: a miocardite está entre as causas de morte súbita em atletas jovens. O calor: a febre já desloca o termostato, e o exercício soma calor. Água e eletrólitos: febre, suor e vômito fazem o treino começar em déficit. O rendimento: força e resistência caem, e o treino prolonga a doença")]
    rs = []
    p.append(f'<circle cx="832" cy="190" r="130" fill="{FOSF}"/>')
    p.append(icone("t:temperature", 792, 90, 80, PAPEL))
    rs.append(rot(712, 186, "com febre, não se treina", w=240, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.15))
    itens = [((0, 0), "t:heart", "O coração", "miocardite está entre as causas de morte súbita em atletas jovens", FOSF),
             ((1104, 0), "t:flame", "O calor", "febre já desloca o termostato; o exercício soma calor", GLIC),
             ((0, 200), "t:droplet", "Água e eletrólitos", "febre, suor, vômito: começa o treino em déficit", GLIC),
             ((1104, 200), "t:trending-down", "O rendimento", "força e resistência caem; o treino prolonga a doença", OXID)]
    for (x, y), ic, t, d, cor in itens:
        p.append(caixa(x, y, 560, 180, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, y + 22, 48, cor))
        rs += [rot(x + 86, y + 28, t, w=450, tam=26, cor=cor, peso=700, serif=True), rot(x + 24, y + 90, d, w=510, tam=22, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 560 if x == 0 else x}" y1="{y + 90}" x2="{832 + (-120 if x == 0 else 120)}" y2="{190 + (-50 if y == 0 else 50)}" stroke="{BORDA}" stroke-width="3"/>')
    return slide("febre", 380, p, rs, eyebrow="A linha vermelha", titulo="Com febre, não se treina",
                 destaque="Um dia de treino perdido não muda uma temporada. Uma miocardite muda uma vida.", destaque_cor="tinta")


def degraus_68():
    """6.8: a porta de entrada e os quatro degraus da volta depois da doença."""
    p = [svg_abre(1664, 400, "Uma porta de entrada e quatro degraus. Antes de começar: 24 horas sem febre e sem antitérmico, sem dor difusa, comendo, bebendo e dormindo. Degrau um: atividade leve e curta, sem estímulo intenso. Degrau dois: volume habitual, intensidade reduzida. Degrau três: volta dos estímulos de intensidade. Degrau quatro: treino completo e competição. Uma regra prática: cerca de um dia de retomada para cada dia de doença sistêmica")]
    rs = []
    p.append(caixa(0, 0, 420, 400, FOSF, FOSF_T, esp=2, rx=16))
    p.append(icone("t:lock-open", 24, 22, 44, FOSF))
    rs += [rot(80, 28, "Antes de começar", w=320, tam=25, cor=FOSF, peso=700, serif=True)]
    for k, t in enumerate(["24 h sem febre e sem antitérmico", "sem dor difusa", "comendo, bebendo, dormindo"]):
        y = 100 + k * 76
        p.append(icone("t:check", 24, y, 34, FOSF))
        rs.append(rot(70, y + 2, t, w=330, tam=22, cor=TINTA, lh=1.25))
    rs.append(rot(24, 336, "≈ 1 dia de retomada por dia de doença sistêmica", w=380, tam=19, cor=FOSF, peso=700, lh=1.25))
    degraus = ["atividade leve e curta, sem estímulo intenso", "volume habitual, intensidade reduzida", "volta dos estímulos de intensidade", "treino completo e competição"]
    for k, t in enumerate(degraus):
        x, w = 460 + k * 302, 290
        y = 280 - k * 80
        cor = OXID if k < 3 else TINTA
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{400 - y}" rx="8" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="12" rx="4" fill="{cor}"/>')
        rs += [rot(x + 14, y + 20, f"Degrau {k + 1}", w=w - 28, tam=24, cor=cor, peso=700, serif=True), rot(x + 14, y + 58, t, w=w - 28, tam=20, cor=TINTA, lh=1.25)]
    return slide("degraus", 400, p, rs, eyebrow="A mensagem da corredora", titulo="Não é sim nem não: é assim",
                 destaque="Prática, não evidência forte: cerca de um dia de retomada para cada dia de doença sistêmica.", destaque_cor="ambar")


def sinais_68():
    """6.8: quatro sinais cardiopulmonares e dois de carga, com a frequência alta para a mesma carga em gráfico."""
    p = [svg_abre(1664, 380, "Seis sinais que interrompem a volta. Quatro cardiopulmonares: dor ou aperto no peito, falta de ar desproporcional, palpitação, tontura ou desmaio. Dois na mão da preparação física: frequência cardíaca alta para a mesma carga, desenhada como duas linhas, antes e depois, com a mesma carga e frequência maior; e fadiga que não cede, mesmo com dias fáceis")]
    rs = []
    for k, (ic, t) in enumerate([("t:heart-broken", "Dor ou aperto no peito"), ("h:lungs", "Falta de ar desproporcional"), ("t:heartbeat", "Palpitação"), ("t:spiral", "Tontura ou desmaio")]):
        col, lin = k % 2, k // 2
        x, y = col * 420, lin * 196
        p.append(caixa(x, y, 400, 180, FOSF, FOSF_T, esp=2, rx=16))
        p.append(icone(ic, x + 24, y + 24, 52, FOSF))
        rs.append(rot(x + 24, y + 100, t, w=352, tam=24, cor=FOSF, peso=700, lh=1.2))
    p.append(caixa(860, 0, 804, 240, GLIC, CARTAO, esp=2, rx=16))
    rs += [rot(884, 16, "FC alta para a mesma carga", w=500, tam=24, cor=GLIC, peso=700), rot(884, 54, "dado clínico na mão da preparação física", w=500, tam=20, cor=TINTA)]
    X0, Y0 = 900, 220
    p.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0 + 700}" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {X0} 200 L {X0 + 700} 120" stroke="{CINZA}" stroke-width="5" fill="none"/>')
    p.append(f'<path d="M {X0} 170 L {X0 + 700} 92" stroke="{GLIC}" stroke-width="5" fill="none"/>')
    rs += [rot(1440, 128, "antes", w=150, tam=18, cor=MUDO, alinha="right"), rot(1440, 66, "depois da infecção", w=210, tam=18, cor=GLIC, peso=700, alinha="right"),
           rot(X0, Y0 + 2, "carga →", w=300, tam=16, cor=MUDO), rot(1400, Y0 + 2, "esquema", w=200, tam=16, cor=MUDO, alinha="right")]
    p.append(caixa(860, 256, 804, 124, GLIC, CARTAO, esp=2, rx=16))
    p.append(icone("t:battery-1", 884, 290, 52, GLIC))
    rs += [rot(956, 278, "Fadiga que não cede", w=680, tam=24, cor=GLIC, peso=700), rot(956, 318, "mesmo com dias fáceis", w=680, tam=21, cor=TINTA)]
    return slide("sinais", 380, p, rs, eyebrow="A lista que precisa estar decorada", titulo="Sinais que interrompem a volta",
                 destaque="Depois de infecção, isso não é destreino. É motivo para parar e investigar o miocárdio.", destaque_cor="verm")


def medica_68():
    """6.8: três situações que saem da comissão, com o que cada uma exige."""
    p = [svg_abre(1664, 380, "Três situações que saem das mãos da comissão. Miocardite: abstenção, e retorno considerado em três a seis meses, com eletrocardiograma, Holter, teste de esforço e ressonância. Mononucleose: baço aumentado; fora do contato e do esforço vigoroso por semanas. Sintoma cardiopulmonar, como dor, falta de ar, palpitação ou síncope: não volta sem avaliação")]
    rs = []
    p.append(caixa(0, 0, 760, 380, FOSF, FOSF_T, esp=2, rx=16))
    p.append(icone("t:heart", 24, 22, 48, FOSF))
    rs += [rot(88, 28, "Miocardite", w=640, tam=28, cor=FOSF, peso=700, serif=True),
           rot(24, 96, "abstenção; retorno considerado em", w=700, tam=22, cor=TINTA),
           rot(24, 130, "3 a 6 meses", w=700, tam=48, cor=FOSF, peso=700, serif=True),
           rot(24, 214, "com os exames:", w=700, tam=20, cor=MUDO, peso=700)]
    for k, t in enumerate(["ECG", "Holter", "teste de esforço", "ressonância"]):
        x = 24 + [0, 120, 260, 480][k]
        w = [104, 124, 204, 190][k]
        p.append(caixa(x, 260, w, 56, FOSF, CARTAO, esp=2, rx=28))
        rs.append(rot(x, 275, t, w=w, tam=20, cor=TINTA, peso=600, alinha="center"))
    p.append(caixa(800, 0, 864, 180, GLIC, GLIC_T, esp=2, rx=16))
    p.append(icone("t:shield", 824, 22, 48, GLIC))
    rs += [rot(888, 28, "Mononucleose", w=740, tam=28, cor=GLIC, peso=700, serif=True),
           rot(824, 96, "baço aumentado: fora do contato e do esforço vigoroso por semanas", w=800, tam=22, cor=TINTA, lh=1.3)]
    p.append(caixa(800, 200, 864, 180, FOSF, CARTAO, esp=2, rx=16))
    p.append(icone("t:stethoscope", 824, 222, 48, FOSF))
    rs += [rot(888, 228, "Sintoma cardiopulmonar", w=740, tam=28, cor=FOSF, peso=700, serif=True),
           rot(824, 296, "dor, falta de ar, palpitação, síncope: não volta sem avaliação", w=800, tam=22, cor=TINTA, lh=1.3)]
    return slide("medica", 380, p, rs, eyebrow="A terceira mensagem", titulo="Quando o assunto sai da comissão",
                 destaque="“Estou ótimo” não é critério. Quem tem miocardite em resolução se sente bem em repouso; o risco aparece no esforço.",
                 destaque_cor="tinta", fonte="Diretrizes europeias de cardiologia do esporte, Eur Heart J 2021")


def rastreio_68():
    """6.8: cem quadrados, menos de um aceso, e o sintoma como critério."""
    p = [svg_abre(1664, 360, "À esquerda, 3.018 atletas universitários rastreados depois da infecção. No meio, uma grade de cem quadrados com menos de um aceso: menos de um por cento teve acometimento cardíaco provável ou definido. À direita, o critério para investigar: sintoma cardiopulmonar e gravidade da doença"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 60, 380, 240, TINTA, CARTAO, esp=2, rx=16))
    rs += [rot(0, 96, "3.018", w=380, tam=64, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(20, 196, "atletas universitários rastreados depois da infecção", w=340, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    X0 = 460
    for k in range(100):
        col, lin = k % 10, k // 10
        x, y = X0 + col * 34, 10 + lin * 34
        cor = FOSF if k == 0 else CINZA
        if k == 0:
            p.append(f'<rect x="{x}" y="{y}" width="14" height="28" rx="3" fill="{cor}"/>')
            p.append(f'<rect x="{x}" y="{y}" width="28" height="28" rx="3" fill="none" stroke="{FOSF}" stroke-width="2"/>')
        else:
            p.append(f'<rect x="{x}" y="{y}" width="28" height="28" rx="3" fill="{cor}"/>')
    rs.append(rot(X0 + 360, 20, "< 1%", w=300, tam=56, cor=OXID, peso=700, serif=True))
    rs.append(rot(X0 + 360, 100, "com acometimento cardíaco provável ou definido", w=330, tam=21, cor=TINTA, lh=1.3))
    rs.append(rot(X0, 346 - 4, "cada quadrado: 1% dos rastreados", w=400, tam=16, cor=MUDO))
    p.append(caixa(1220, 60, 444, 240, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(1244, 80, "O critério para investigar", w=400, tam=24, cor=FOSF, peso=700, serif=True),
           rot(1244, 140, "sintoma cardiopulmonar e gravidade da doença", w=400, tam=24, cor=TINTA, peso=600, lh=1.3)]
    return slide("rastreio", 360, p, rs, eyebrow="O dado que ensina a lógica", titulo="Escalar por sintoma, não rastrear todo mundo",
                 destaque="Rastrear todos com imagem avançada gera mais falso-positivo e afastamento desnecessário que benefício. A minoria real se acha pelo sintoma.",
                 destaque_cor="tinta", fonte="Registro americano ORCCA, Circulation 2021")


def prevencao_68():
    """6.8: as seis frentes de gestão e o risco relativo da vitamina C, com a linha do efeito nulo."""
    p = [svg_abre(1664, 380, "À esquerda, as seis frentes de prevenção em equipe: sono, energia, carga, vacina, higiene de vestiário e viagem. À direita, o risco relativo de resfriado com vitamina C numa régua de zero a um e meio, com a linha do efeito nulo em um. Na população geral, 0,97: praticamente nada. Só em estresse físico extremo, como maratona, esqui ou frio subártico, 0,48, um achado de subgrupo")]
    rs = []
    for k, (ic, t) in enumerate([("t:moon", "sono"), ("t:salad", "energia"), ("t:barbell", "carga"), ("t:shield-check", "vacina"), ("t:droplet", "higiene de vestiário"), ("t:plane", "viagem")]):
        col, lin = k % 3, k // 3
        x, y = col * 236, lin * 190
        p.append(caixa(x, y, 220, 174, OXID, OXID_T, esp=2, rx=16))
        p.append(icone(ic, x + 82, y + 22, 56, OXID))
        rs.append(rot(x + 10, y + 100, t, w=200, tam=21, cor=TINTA, peso=700, alinha="center", lh=1.2))
    X0, X1 = 1040, 1640
    fx = lambda v: X0 + v / 1.5 * (X1 - X0)
    p.append(f'<line x1="{X0}" y1="300" x2="{X1}" y2="300" stroke="{MUDO}" stroke-width="3"/>')
    for v in (0, 0.5, 1, 1.5):
        p.append(f'<line x1="{fx(v):.0f}" y1="300" x2="{fx(v):.0f}" y2="312" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(fx(v) - 40, 318, f"{v}".replace(".", ","), w=80, tam=18, cor=MUDO, alinha="center"))
    p.append(f'<line x1="{fx(1):.0f}" y1="40" x2="{fx(1):.0f}" y2="300" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
    rs.append(rot(fx(1) + 10, 30, "efeito nulo", w=200, tam=18, cor=TINTA))
    for y, v, t, cor in [(110, 0.97, "população geral: 0,97", TINTA), (220, 0.48, "estresse físico extremo: 0,48", GLIC)]:
        p.append(f'<circle cx="{fx(v):.0f}" cy="{y}" r="14" fill="{cor}"/>')
        p.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{BORDA}" stroke-width="1"/>')
        rs.append(rot(740, y - 14, t, w=290, tam=21, cor=cor, peso=700))
    rs += [rot(X0, 346, "risco relativo de resfriado com vitamina C", w=600, tam=18, cor=MUDO),
           rot(740, 246, "maratona, esqui, frio subártico", w=290, tam=18, cor=TINTA)]
    return slide("prevencao", 380, p, rs, eyebrow="Prevenção em equipe", titulo="Gestão, não farmácia",
                 destaque="Achado de subgrupo não é passe livre para vender vitamina C. A base não cabe num frasco.",
                 destaque_cor="verm", fonte="Revisão Cochrane de vitamina C e resfriado, 2013")

# ---------------------------------------------------------------- 6.9

def perfil_69():
    """6.9: a curva de quem piora há meses e os três erros empilhados por baixo dela."""
    p = [svg_abre(1664, 400, "À esquerda, em esquema, a disposição da corredora caindo ao longo dos meses, com três marcos: um painel normal, outro painel normal, ferro por conta própria, e a curva continua descendo. À direita, os três erros empilhados como blocos: o exame certo nunca foi pedido; o que foi pedido foi colhido e lido errado; o tratamento veio sem diagnóstico")]
    rs = []
    X0, X1 = 40, 860
    p.append(f'<line x1="{X0}" y1="340" x2="{X1}" y2="340" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="{X0}" y1="20" x2="{X0}" y2="340" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<path d="M {X0} 60 C 300 80, 500 160, {X1} 300" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    rs += [rot(X0 + 10, 14, "disposição", w=200, tam=19, cor=MUDO), rot(X1 - 200, 346, "meses · esquema", w=200, tam=18, cor=MUDO, alinha="right")]
    for x, y, t in [(240, 90, "painel normal"), (470, 150, "painel normal"), (690, 222, "ferro por conta própria")]:
        p.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
        rs.append(rot(x - 110, y + 22, t, w=220, tam=20, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(940, 0, "Três erros empilhados", w=720, tam=26, cor=FOSF, peso=700, serif=True))
    erros = ["o exame certo nunca foi pedido", "o que foi pedido foi colhido e lido errado", "o tratamento veio sem diagnóstico"]
    for k, t in enumerate(erros):
        y = 290 - k * 110
        p.append(caixa(940, y, 724, 100, FOSF, FOSF_T if k % 2 == 0 else CARTAO, esp=2, rx=10))
        p.append(f'<circle cx="990" cy="{y + 50}" r="26" fill="{FOSF}"/>')
        rs += [rot(964, y + 34, str(k + 1), w=52, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True), rot(1036, y + 34, t, w=610, tam=23, cor=TINTA, peso=600)]
    return slide("perfil", 400, p, rs, eyebrow="A corredora que piora há meses", titulo="Dois painéis normais, e continua piorando")


def mapa_69():
    """6.9: os cinco passos em fila, com ícone."""
    p = [svg_abre(1664, 300, "Cinco passos em fila. Um, perguntar, antes de qualquer exame. Dois, pedir e colher o exame certo na hora certa. Três, interpretar com a régua do atleta. Quatro, investigar por que o ferro caiu. Cinco, repor e reavaliar"), defs(MUDO)]
    rs = []
    passos = [("t:message-circle", "Perguntar", "antes de qualquer exame", OXID), ("t:clipboard-list", "Pedir e colher", "o exame certo, na hora certa", OXID),
              ("t:ruler-measure", "Interpretar", "com a régua do atleta", GLIC), ("t:zoom-question", "Investigar", "por que o ferro caiu", FOSF), ("t:pill", "Repor", "e reavaliar", TINTA)]
    for k, (ic, t, d, cor) in enumerate(passos):
        x = k * 340
        p.append(caixa(x, 0, 304, 300, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 48}" cy="48" r="28" fill="{cor}"/>')
        p.append(icone(ic, x + 220, 22, 56, cor))
        rs += [rot(x + 20, 30, str(k + 1), w=56, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
               rot(x + 24, 120, t, w=260, tam=28, cor=cor, peso=700, serif=True), rot(x + 24, 180, d, w=260, tam=22, cor=TINTA, lh=1.3)]
        if k < 4:
            p.append(seta(x + 308, 150, x + 334, 150, MUDO, "m0", esp=3))
    return slide("mapa", 300, p, rs, eyebrow="O procedimento", titulo="Cinco passos",
                 destaque="Das causas clínicas mais comuns de “estou sem energia”, e das mais malfeitas nos dois sentidos.", destaque_cor="tinta")


def fadiga_69():
    """6.9: a fadiga no centro e oito causas em volta, com o ferro destacado."""
    p = [svg_abre(1664, 400, "No centro, a fadiga, que é sintoma, não diagnóstico. Em volta, oito causas: carga e recuperação, a mais comum; sono curto, ruim ou apneia; energia, a baixa disponibilidade; ferro, com ou sem anemia, destacado; tireoide; depressão e ansiedade, a última hipótese, e não deveria ser; convalescença depois de infecção; e doenças da mesma idade, fora do esporte")]
    rs = []
    import math as _m
    cx, cy = 832, 200
    p.append(f'<circle cx="{cx}" cy="{cy}" r="100" fill="{TINTA}"/>')
    rs += [rot(cx - 90, cy - 30, "Fadiga", w=180, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True), rot(cx - 90, cy + 14, "é sintoma", w=180, tam=21, cor=PAPEL, alinha="center")]
    itens = [("Carga e recuperação", "a mais comum", OXID), ("Sono", "curto, ruim, apneia", OXID), ("Energia", "baixa disponibilidade", GLIC), ("Ferro", "com ou sem anemia", FOSF),
             ("Convalescença", "depois de infecção", OXID), ("Fora do esporte", "doenças da mesma idade", MUDO), ("Depressão, ansiedade", "a última hipótese, e não deveria", GLIC), ("Tireoide", "", GLIC)]
    pos = [(0, 0), (0, 104), (0, 208), (0, 312), (1264, 0), (1264, 104), (1264, 208), (1264, 312)]
    for (x, y), (t, d, cor) in zip(pos, itens):
        destaque = t == "Ferro"
        p.append(caixa(x, y, 400, 88, cor, FOSF_T if destaque else CARTAO, esp=4 if destaque else 2, rx=14))
        rs.append(rot(x + 20, y + (12 if d else 28), t, w=360, tam=23, cor=cor if cor != MUDO else TINTA, peso=700))
        if d:
            rs.append(rot(x + 20, y + 50, d, w=360, tam=19, cor=TINTA))
        x1 = x + 400 if x == 0 else x
        a = _m.atan2(y + 44 - cy, x1 - cx)
        p.append(f'<line x1="{x1}" y1="{y + 44}" x2="{cx + 100 * _m.cos(a):.0f}" y2="{cy + 100 * _m.sin(a):.0f}" stroke="{FOSF if destaque else BORDA}" stroke-width="{4 if destaque else 2}"/>')
    return slide("fadiga", 400, p, rs, eyebrow="Passo um", titulo="Fadiga é sintoma, não diagnóstico",
                 destaque="Ferritina baixa em quem dorme cinco horas por noite vai ser tratada com ferro, e a pessoa vai continuar cansada.", destaque_cor="tinta")


def perguntas_69():
    """6.9: cinco perguntas em balões e quatro sinais, com a pergunta do fluxo destacada."""
    p = [svg_abre(1664, 380, "À esquerda, cinco perguntas, com a primeira destacada: como é o fluxo menstrual? Depois: é vegetariana, come carne vermelha com que frequência? Quanto corre, em que superfície? Usa anti-inflamatório com frequência? Já teve ferro baixo, já tomou? À direita, quatro sinais: falta de ar desproporcional, queda de desempenho aeróbico, palidez com alteração de cabelo e unhas, e vontade de mastigar gelo")]
    rs = []
    qs = ["como é o fluxo menstrual?", "vegetariana? carne vermelha com que frequência?", "quanto corre, em que superfície?", "anti-inflamatório com frequência?", "já teve ferro baixo? já tomou?"]
    for k, q in enumerate(qs):
        y = k * 76
        cor, fundo = (FOSF, FOSF_T) if k == 0 else (OXID, CARTAO)
        p.append(f'<path d="M 14 {y} H 1000 Q 1014 {y} 1014 {y + 14} V {y + 50} Q 1014 {y + 64} 1000 {y + 64} H 60 L 30 {y + 74} L 36 {y + 64} H 14 Q 0 {y + 64} 0 {y + 50} V {y + 14} Q 0 {y} 14 {y} Z" fill="{fundo}" stroke="{cor}" stroke-width="{3 if k == 0 else 2}"/>')
        rs.append(rot(24, y + 17, "“" + q[0].upper() + q[1:] + "”", w=970, tam=23, cor=cor if k == 0 else TINTA, peso=700 if k == 0 else 400))
    p.append(caixa(1064, 0, 600, 380, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(1088, 18, "Sinais", w=550, tam=26, cor=GLIC, peso=700, serif=True))
    for k, (ic, t) in enumerate([("h:lungs", "falta de ar desproporcional"), ("t:trending-down", "queda de desempenho aeróbico"), ("t:eye", "palidez, cabelo, unhas"), ("t:droplet", "vontade de mastigar gelo")]):
        y = 80 + k * 72
        p.append(icone(ic, 1088, y, 40, GLIC))
        rs.append(rot(1144, y + 6, t, w=500, tam=23, cor=TINTA))
    return slide("perguntas", 380, p, rs, eyebrow="As perguntas que orientam a suspeita", titulo="O que perguntar antes de pedir",
                 destaque="A pergunta sobre o fluxo menstrual é a que mais encontra deficiência de ferro no esporte feminino, e a que menos se faz.", destaque_cor="verm")


def pedido_69():
    """6.9: os quatro exames em tubos e a janela de coleta depois do treino intenso."""
    p = [svg_abre(1664, 380, "À esquerda, quatro tubos com o que pedir: hemograma com hemoglobina, VCM e RDW; ferritina; saturação de transferrina; proteína C reativa. À direita, uma linha do tempo a partir de um treino intenso: a coleta fica na janela de 24 a 48 horas depois, fora de infecção, de manhã, sempre no mesmo esquema. Antes disso, a ferritina sobe como proteína de fase aguda e vem falsamente confortável")]
    rs = []
    tubos = [("hemograma", "Hb, VCM, RDW"), ("ferritina", ""), ("saturação de transferrina", ""), ("proteína C reativa", "")]
    for k, (t, d) in enumerate(tubos):
        x = k * 170
        p.append(f'<rect x="{x + 50}" y="0" width="70" height="30" rx="6" fill="{OXID}"/>')
        p.append(f'<path d="M {x + 50} 34 H {x + 120} V 220 Q {x + 120} 250 {x + 85} 250 Q {x + 50} 250 {x + 50} 220 Z" fill="{CARTAO}" stroke="{OXID}" stroke-width="3"/>')
        p.append(f'<path d="M {x + 53} 140 H {x + 117} V 220 Q {x + 117} 246 {x + 85} 246 Q {x + 53} 246 {x + 53} 220 Z" fill="{FOSF}" opacity="0.75"/>')
        rs.append(rot(x, 264, t, w=170, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.2))
        if d:
            rs.append(rot(x, 314, d, w=170, tam=18, cor=MUDO, alinha="center"))
    X0, X1 = 760, 1640
    fx = lambda h: X0 + h / 72 * (X1 - X0)
    p.append(f'<rect x="{fx(24):.0f}" y="40" width="{fx(48) - fx(24):.0f}" height="160" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<rect x="{fx(0):.0f}" y="40" width="{fx(24) - fx(0):.0f}" height="160" fill="{FOSF_T}"/>')
    p.append(f'<line x1="{X0}" y1="200" x2="{X1}" y2="200" stroke="{MUDO}" stroke-width="3"/>')
    for h in (0, 24, 48, 72):
        p.append(f'<line x1="{fx(h):.0f}" y1="200" x2="{fx(h):.0f}" y2="212" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(fx(h) - 40, 216, f"{h} h", w=80, tam=18, cor=MUDO, alinha="center"))
    p.append(icone("t:barbell", X0 - 24, 0, 48, TINTA))
    rs += [rot(X0 + 30, 8, "treino intenso", w=240, tam=20, cor=TINTA, peso=700),
           rot(fx(0) + 10, 90, "ferritina falsamente confortável", w=fx(24) - fx(0) - 20, tam=20, cor=FOSF, peso=700, lh=1.2),
           rot(fx(24) + 10, 70, "colher aqui", w=fx(48) - fx(24) - 20, tam=26, cor=OXID, peso=700, alinha="center", serif=True),
           rot(fx(24) + 10, 120, "24 a 48 h depois", w=fx(48) - fx(24) - 20, tam=20, cor=OXID, alinha="center")]
    for k, t in enumerate(["fora de infecção", "de manhã", "sempre no mesmo esquema"]):
        x = X0 + k * 300
        p.append(caixa(x, 270, 280, 60, OXID, CARTAO, esp=2, rx=30))
        rs.append(rot(x + 10, 289, t, w=260, tam=19, cor=TINTA, alinha="center"))
    return slide("pedido", 380, p, rs, eyebrow="Passo dois", titulo="O exame certo, na hora certa",
                 destaque="Ferritina é proteína de fase aguda: colhida depois de treino longo, vem falsamente confortável. Escreva no pedido.", destaque_cor="tinta")


def estagios_69():
    """6.9: três estágios em grade, com o que cai em cada um, e o alcance do hemograma."""
    p = [svg_abre(1664, 360, "Grade com os três estágios da deficiência de ferro e três marcadores. Depleção de estoque: ferritina baixa, saturação e hemoglobina normais. Eritropoiese deficiente em ferro: ferritina e saturação baixas, hemoglobina normal. Anemia ferropriva: os três baixos. Uma faixa mostra que o hemograma sozinho só enxerga o terceiro estágio")]
    rs = []
    cols = ["Ferritina", "Saturação", "Hemoglobina"]
    linhas = [("Depleção de estoque", [1, 0, 0]), ("Eritropoiese deficiente em ferro", [1, 1, 0]), ("Anemia ferropriva", [1, 1, 1])]
    W0, cw = 560, 300
    for j, c in enumerate(cols):
        rs.append(rot(W0 + j * cw, 0, c, w=cw, tam=24, cor=TINTA, peso=700, alinha="center"))
    for i, (t, v) in enumerate(linhas):
        y = 50 + i * 100
        rs.append(rot(0, y + 26, f"{i + 1}. {t}", w=540, tam=24, cor=TINTA, peso=700))
        p.append(f'<line x1="0" y1="{y + 90}" x2="{W0 + 3 * cw}" y2="{y + 90}" stroke="{BORDA}" stroke-width="1"/>')
        for j, b in enumerate(v):
            cx = W0 + j * cw + cw / 2
            p.append(f'<circle cx="{cx:.0f}" cy="{y + 42}" r="40" fill="{FOSF if b else OXID_T}" stroke="{FOSF if b else OXID}" stroke-width="2"/>')
            rs.append(rot(cx - 60, y + 31, "baixa" if b else "normal", w=120, tam=17, cor=PAPEL if b else OXID, peso=700, alinha="center"))
    xh = W0 + 2 * cw
    p.append(f'<rect x="{xh + 6}" y="250" width="{cw - 12}" height="88" rx="12" fill="none" stroke="{TINTA}" stroke-width="4"{TRACO}/>')
    p.append(caixa(1480, 40, 184, 300, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(1490, 80, "o hemograma sozinho só enxerga o terceiro", w=164, tam=21, cor=PAPEL, peso=700, alinha="center", lh=1.3))
    return slide("estagios", 360, p, rs, eyebrow="Passo três: interpretar", titulo="Os três estágios",
                 destaque="Os painéis da corredora não estavam errados: estavam incompletos.", destaque_cor="verm")


def armadilhas_69():
    """6.9: três armadilhas de leitura, cada uma com um pequeno desenho."""
    p = [svg_abre(1664, 380, "Três armadilhas de leitura. Ferritina com PCR alta: a inflamação empurra a ferritina para cima, e ela deixa de medir estoque; repetir ou valorizar a saturação. Pseudoanemia do atleta: o plasma expandido dilui a hemoglobina, com ferritina normal; não se trata. Ferritina muito alta, sem inflamação e sem ferro: investigar sobrecarga")]
    rs = []
    itens = [("Ferritina com PCR alta", "não mede estoque; repetir ou valorizar a saturação", GLIC, "pcr"),
             ("Pseudoanemia do atleta", "plasma expandido dilui a hemoglobina; ferritina normal; não se trata", OXID, "dilui"),
             ("Ferritina muito alta", "sem inflamação e sem ferro: investigar sobrecarga", FOSF, "alta")]
    for k, (t, d, cor, viz) in enumerate(itens):
        x = k * 568
        p.append(caixa(x, 0, 528, 380, cor, CARTAO, esp=2, rx=16))
        rs += [rot(x + 24, 18, t, w=480, tam=26, cor=cor, peso=700, serif=True), rot(x + 24, 280, d, w=480, tam=22, cor=TINTA, lh=1.3)]
        if viz == "pcr":
            p.append(f'<rect x="{x + 80}" y="{230 - 60}" width="80" height="60" fill="{OXID}"/>')
            p.append(f'<rect x="{x + 80}" y="{230 - 150}" width="80" height="90" fill="{GLIC}" opacity="0.6"/>')
            rs += [rot(x + 180, 92, "inflamação soma", w=300, tam=19, cor=GLIC, peso=700), rot(x + 180, 186, "estoque real", w=300, tam=19, cor=OXID, peso=700)]
            p.append(f'<line x1="{x + 60}" y1="230" x2="{x + 480}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
        elif viz == "dilui":
            for j, (h, rot_) in enumerate([(70, "antes"), (110, "plasma expandido")]):
                bx = x + 90 + j * 220
                p.append(f'<rect x="{bx}" y="{230 - h}" width="90" height="{h}" rx="6" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="2"/>')
                for dd in range(6):
                    p.append(f'<circle cx="{bx + 18 + (dd % 3) * 27}" cy="{230 - 14 - (dd // 3) * 24}" r="8" fill="{FOSF}"/>')
                rs.append(rot(bx - 40, 238, rot_, w=170, tam=18, cor=MUDO, alinha="center"))
        else:
            p.append(f'<line x1="{x + 60}" y1="230" x2="{x + 480}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
            p.append(f'<rect x="{x + 220}" y="80" width="90" height="150" fill="{FOSF}"/>')
            p.append(icone("t:arrow-up-right", x + 330, 80, 50, FOSF))
    return slide("armadilhas", 380, p, rs, eyebrow="As armadilhas da leitura", titulo="Errar aqui é mais comum que errar no pedido",
                 destaque="Anemia não é sinônimo de ferro: B12 e folato dão anemia com VCM alto.", destaque_cor="tinta")


def causa_69():
    """6.9: o estoque de ferro como um tanque, com o que entra e as três saídas."""
    p = [svg_abre(1664, 400, "No centro, o estoque de ferro desenhado como um tanque. À esquerda, o que entra: ingestão e dieta, com café e cálcio atrapalhando, e a doença celíaca. Embaixo, três saídas: a perda menstrual, a mais frequente no esporte feminino; o trato gastrointestinal, obrigatório investigar no homem e na mulher depois da menopausa, com o anti-inflamatório entrando aqui; e o próprio treino, com o impacto do pé, o suor e a hepcidina, que tem pico três a seis horas depois"), defs(GLIC, FOSF)]
    rs = []
    p.append(f'<path d="M 640 20 V 230 Q 640 260 670 260 H 990 Q 1020 260 1020 230 V 20" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="644" y="150" width="372" height="106" rx="8" fill="{FOSF}" opacity="0.7"/>')
    rs += [rot(640, 60, "estoque de ferro", w=380, tam=28, cor=TINTA, peso=700, alinha="center", serif=True), rot(640, 190, "baixo", w=380, tam=24, cor=PAPEL, peso=700, alinha="center")]
    p.append(caixa(0, 20, 540, 180, GLIC, GLIC_T, esp=2, rx=16))
    rs += [rot(24, 36, "O que entra", w=500, tam=26, cor=GLIC, peso=700, serif=True), rot(24, 86, "ingestão e dieta; café e cálcio atrapalham; e a doença celíaca", w=500, tam=22, cor=TINTA, lh=1.3)]
    p.append(seta(544, 110, 630, 110, GLIC, "m0", esp=5))
    saidas = [(0, "Perda menstrual", "a mais frequente no esporte feminino; tratar a perda evita a recaída"),
              (560, "Trato gastrointestinal", "obrigatório no homem e depois da menopausa; o anti-inflamatório entra aqui"),
              (1120, "O próprio treino", "impacto do pé, suor, e a hepcidina com pico 3 a 6 h depois")]
    for x, t, d in saidas:
        p.append(f'<path d="M 830 262 C 830 290, {x + 272} 270, {x + 272} 296" fill="none" stroke="{FOSF}" stroke-width="3" marker-end="url(#m1)"/>')
        p.append(caixa(x, 300, 544, 100, FOSF, FOSF_T, esp=2, rx=14))
        rs += [rot(x + 20, 310, t, w=500, tam=23, cor=FOSF, peso=700), rot(x + 20, 346, d, w=510, tam=19, cor=TINTA, lh=1.25)]
    p.append(caixa(1100, 20, 564, 180, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(1124, 40, "Investigar antes de repor: repor sem achar a saída enche um tanque furado", w=516, tam=23, cor=TINTA, peso=600, lh=1.35))
    return slide("causa", 400, p, rs, eyebrow="Passo quatro", titulo="Investigar antes de repor",
                 destaque="Na carga muito alta, parte da deficiência não se resolve com mais ferro. Resolve-se com carga e recuperação.", destaque_cor="tinta")


def repor_69():
    """6.9: a janela da hepcidina no dia de treino, a absorção em dias alternados e o prazo de reavaliação."""
    p = [svg_abre(1664, 380, "À esquerda, o dia de treino: o comprimido de manhã, fora da janela de três a seis horas depois do treino intenso, quando a hepcidina está alta. No meio, duas barras de absorção fracionada: 21,8 por cento em dias alternados contra 16,3 por cento em dias seguidos. À direita, o prazo: reavaliar em oito a doze semanas, porque o estoque leva meses")]
    rs = []
    X0, X1 = 0, 640
    fx = lambda h: X0 + (h - 6) / 18 * (X1 - X0)
    p.append(f'<rect x="{fx(17):.0f}" y="60" width="{fx(20) - fx(17):.0f}" height="180" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
    p.append(f'<line x1="{X0}" y1="240" x2="{X1}" y2="240" stroke="{MUDO}" stroke-width="3"/>')
    for h in (6, 12, 18, 24):
        rs.append(rot(fx(h) - 40, 248, f"{h} h", w=80, tam=18, cor=MUDO, alinha="center"))
    p.append(icone("t:pill", fx(7) - 20, 150, 50, OXID))
    p.append(icone("t:barbell", fx(14) - 24, 170, 48, TINTA))
    rs += [rot(fx(7) - 60, 100, "manhã", w=120, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(fx(14) - 70, 120, "treino intenso", w=140, tam=18, cor=TINTA, alinha="center"),
           rot(fx(17) + 4, 70, "hepcidina alta: 3 a 6 h depois", w=fx(20) - fx(17) + 120, tam=18, cor=FOSF, peso=700, lh=1.2),
           rot(0, 290, "o comprimido fora da janela da hepcidina", w=640, tam=21, cor=TINTA, lh=1.3)]
    Xb = 760
    rs.append(rot(Xb, 0, "absorção fracionada", w=500, tam=22, cor=MUDO, peso=700))
    for k, (t, v, cor) in enumerate([("dias alternados", 21.8, GLIC), ("dias seguidos", 16.3, CINZA)]):
        y = 60 + k * 110
        rs.append(rot(Xb, y + 20, t, w=200, tam=22, cor=TINTA, peso=600))
        p.append(f'<rect x="{Xb + 210}" y="{y}" width="{v * 10:.0f}" height="80" rx="4" fill="{cor}"/>')
        rs.append(rot(Xb + 222 + v * 10, y + 18, f"{v:.1f}%".replace(".", ","), w=140, tam=34, cor=cor if cor != CINZA else MUDO, peso=700, serif=True))
    p.append(caixa(1380, 40, 284, 260, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1380, 70, "8 a 12", w=284, tam=56, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1380, 150, "semanas", w=284, tam=24, cor=PAPEL, alinha="center"),
           rot(1400, 200, "para reavaliar; o estoque leva meses", w=244, tam=20, cor=PAPEL, alinha="center", lh=1.3)]
    return slide("repor", 380, p, rs, eyebrow="Passo cinco: repor direito", titulo="Horário, frequência, companhia, tempo",
                 destaque="Vitamina C ajuda; café, chá, cálcio e whey com leite atrapalham. E pergunte: “você está conseguindo tomar?”", destaque_cor="verm",
                 fonte="Ensaio randomizado em mulheres com estoque baixo, Lancet Haematol 2017")


def veia_69():
    """6.9: a bolsa de infusão com a linha dos 100 mL, e o que o ferro não faz."""
    p = [svg_abre(1664, 400, "No meio, uma bolsa de infusão com uma linha nos 100 mililitros: acima disso em doze horas, proibido fora do hospital. À esquerda, quando o ferro endovenoso entra: intolerância ou falha do oral, correção rápida, perdas importantes, por decisão médica, nunca por conveniência. À direita, o que o ferro não faz: trata quem tem deficiência e melhora ferritina, ferro sérico e hemoglobina, mas não é argumento para quem está normal")]
    rs = []
    p.append(caixa(0, 0, 560, 400, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(24, 18, "Endovenoso", w=500, tam=27, cor=FOSF, peso=700, serif=True))
    for k, t in enumerate(["intolerância ou falha do oral", "correção rápida, perdas importantes", "decisão médica, nunca por conveniência"]):
        y = 90 + k * 76
        p.append(f'<circle cx="34" cy="{y + 14}" r="8" fill="{FOSF}"/>')
        rs.append(rot(54, y, t, w=480, tam=23, cor=TINTA, lh=1.25))
    p.append(f'<path d="M 720 20 H 940 Q 960 20 960 40 V 260 Q 960 300 900 300 H 760 Q 700 300 700 260 V 40 Q 700 20 720 20 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="704" y="150" width="252" height="146" rx="20" fill="{GLIC}" opacity="0.55"/>')
    p.append(f'<line x1="680" y1="150" x2="980" y2="150" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
    p.append(f'<line x1="830" y1="300" x2="830" y2="326" stroke="{TINTA}" stroke-width="4"/>')
    rs += [rot(640, 104, "100 mL em 12 h", w=380, tam=26, cor=FOSF, peso=700, alinha="center", serif=True),
           rot(600, 344, "acima: proibido fora do hospital", w=460, tam=20, cor=FOSF, peso=700, alinha="center")]
    p.append(caixa(1104, 0, 560, 400, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(1128, 18, "O que o ferro faz, e não faz", w=510, tam=27, cor=OXID, peso=700, serif=True))
    for k, (t, ok) in enumerate([("trata quem tem deficiência", True), ("melhora ferritina, ferro sérico e hemoglobina", True), ("não é argumento para quem está normal", False)]):
        y = 90 + k * 90
        p.append(icone("t:check" if ok else "t:x", 1128, y, 36, OXID if ok else FOSF))
        rs.append(rot(1176, y + 2, t, w=460, tam=23, cor=TINTA, lh=1.25))
    return slide("veia", 400, p, rs, eyebrow="Ferro na veia e o que o ferro não faz", titulo="100 mL em 12 horas",
                 destaque="Infusão “de vitaminas e ferro” para dar energia é má medicina e risco antidoping.", destaque_cor="tinta",
                 fonte="WADA 2026, M2.2 · metanálise em atletas de endurance, BJSM 2015")

# ---------------------------------------------------------------- aplicação

LICOES = {"06-01": [caso_61, paradoxo_61, modelo_61, saidas_61, fechamento_61, sintomas_61, historia_61, perfis_61, tres_saidas_61, registro_61],
          "06-02": [pergunta_62, pedidos_62, ecg_62, corrado_62, posicoes_62, leitura_62, adulto_62, naopedir_62, perfis_62, respostas_62],
          "06-03": [laudos_63, perfis_63, remodelamento_63, cavidade_63, quem_63, discriminadores_63, destreino_63, ondat_63, aritmetica_63, condutas_63],
          "06-04": [frases_64, desfechos_64, frequencia_64, causa_64, quem_64, rastreio_64, consequencias_64, reconhecer_64, desfibrilador_64, correcoes_64],
          "06-05": [cena_65, mapa_65, folha_65, dea_65, comprimir_65, erros_65, chocar_65, depois_65, calor_65, outras_65, ensaio_65],
          "06-06": [frase_66, decisoes_66, equivocos_66, sinais_66, retira_66, alarme_66, cultura_66, repouso_66, escola_66, escada_66, demora_66, prevencao_66],
          "06-07": [perfis_67, numeros_67, mecanismo_67, prevalencia_67, diferenciais_67, laringe_67, camadas_67, aquecimento_67, doses_67, urina_67],
          "06-08": [mensagens_68, leituras_68, pescoco_68, excecoes_68, febre_68, degraus_68, sinais_68, medica_68, rastreio_68, prevencao_68],
          "06-09": [perfil_69, mapa_69, fadiga_69, perguntas_69, pedido_69, estagios_69, armadilhas_69, causa_69, repor_69, veia_69]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
