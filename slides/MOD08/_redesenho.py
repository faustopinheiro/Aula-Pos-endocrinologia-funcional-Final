"""Desenhos que substituem os slides de texto do Módulo 8 (cartões, colunas, listas, tabelas e números).
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


# ---------------------------------------------------------------- 8.1

def tatame_81():
    """8.1: duas perguntas, cada uma com seu dono; o laudo responde só a primeira."""
    p = [svg_abre(1664, 360, "Duas perguntas lado a lado. À esquerda, o que eu tenho? Ela tem dono: o diagnóstico, que diz o que é e o que não pode ser. À direita, a pergunta da reabilitação: o que essa pessoa não consegue fazer hoje, por que não consegue, e por onde eu começo? No meio, o envelope do laudo, que responde só a primeira"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 620, 360, AZUL, AZUL_T, esp=2, rx=16))
    p.append(icone("t:message-circle", 24, 24, 48, AZUL))
    rs += [rot(88, 30, "“O que eu tenho?”", w=510, tam=30, cor=AZUL, peso=700, serif=True),
           rot(24, 120, "tem dono: o diagnóstico", w=570, tam=24, cor=TINTA, peso=700),
           rot(24, 170, "o que é, e o que não pode ser", w=570, tam=22, cor=TINTA)]
    p.append(caixa(660, 110, 344, 140, TINTA, CARTAO, esp=2, rx=12))
    p.append(icone("t:clipboard-list", 682, 140, 48, TINTA))
    rs += [rot(744, 138, "o laudo", w=240, tam=24, cor=TINTA, peso=700), rot(744, 178, "responde só a primeira", w=250, tam=19, cor=MUDO, lh=1.2)]
    p.append(seta(656, 180, 626, 180, MUDO, "m0", esp=3))
    p.append(caixa(1044, 0, 620, 360, OXID, OXID, esp=0, rx=16))
    rs.append(rot(1068, 26, "A pergunta da reabilitação", w=570, tam=26, cor=PAPEL, peso=700, serif=True))
    for k, t in enumerate(["o que não consegue fazer hoje?", "por que não consegue?", "por onde eu começo?"]):
        y = 100 + k * 80
        p.append(f'<rect x="1068" y="{y}" width="572" height="64" rx="32" fill="{CARTAO}"/>')
        rs.append(rot(1068, y + 18, t, w=572, tam=23, cor=TINTA, peso=700, alinha="center"))
    return slide("tatame", 360, p, rs, eyebrow="Seis semanas de dor no ombro", titulo="“O que eu tenho?” tem dono. A reabilitação precisa de outra pergunta.")


def roteiro_81():
    """8.1: cinco perguntas em fila, na ordem; o exercício aparece só no fim, como consequência."""
    p = [svg_abre(1664, 400, "Cinco perguntas em fila, nesta ordem. É de reabilitação, ou algo precisa ir para outro lugar antes? Quão irritável está: decide quanto posso testar hoje. O que não consegue fazer, nas palavras da pessoa. O que explica a limitação: hipóteses, cada uma com um teste que pode derrubá-la. O que vou medir de novo, para saber se o plano funciona. Só no fim, como consequência, o exercício"), defs(MUDO)]
    rs = []
    qs = [("É de reabilitação?", "ou algo precisa ir para outro lugar antes", FOSF), ("Quão irritável está?", "decide quanto eu posso testar hoje", GLIC),
          ("O que não consegue fazer?", "nas palavras da pessoa", OXID), ("O que explica a limitação?", "hipóteses, cada uma com um teste que pode derrubá-la", OXID),
          ("O que vou medir de novo?", "para saber se o plano funciona", TINTA)]
    for k, (t, d, cor) in enumerate(qs):
        x = k * 337
        p.append(caixa(x, 0, 312, 290, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 42}" cy="42" r="24" fill="{cor}"/>')
        rs += [rot(x + 18, 28, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 20, 86, t, w=274, tam=24, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 20, 180, d, w=274, tam=20, cor=TINTA, lh=1.3)]
        if k < 4:
            p.append(seta(x + 314, 145, x + 334, 145, MUDO, "m0", esp=2))
    p.append(seta(832, 296, 832, 318, MUDO, "m0", esp=3))
    p.append(caixa(532, 322, 600, 72, TINTA, TINTA, esp=0, rx=36))
    p.append(icone("t:barbell", 560, 340, 36, PAPEL))
    rs.append(rot(610, 344, "o exercício: consequência", w=500, tam=24, cor=PAPEL, peso=700))
    return slide("roteiro", 400, p, rs, eyebrow="Antes do primeiro exercício", titulo="Cinco perguntas, nesta ordem")


def bandeiras_81():
    """8.1: quatro sinais vermelhos que param tudo e levam a encaminhar."""
    p = [svg_abre(1664, 360, "Quatro sinais que fazem parar e encaminhar antes de qualquer exercício. Trauma: deformidade ou perda súbita de função. Dor noturna: sem posição de alívio, com febre, perda de peso ou câncer prévio. Neurológico: formigamento ou fraqueza piorando. Articulação quente: inchada, sem trauma. Embaixo: parar e encaminhar no mesmo dia"), defs(FOSF)]
    rs = []
    itens = [("t:alert-triangle", "Trauma", "deformidade ou perda súbita de função"), ("t:moon", "Dor noturna", "sem posição de alívio, com febre, perda de peso ou câncer prévio"),
             ("t:wave-sine", "Neurológico", "formigamento ou fraqueza piorando"), ("t:temperature", "Articulação quente", "inchada, sem trauma")]
    for k, (ic, t, d) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 0, 392, 250, FOSF, FOSF_T, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 48, FOSF))
        rs += [rot(x + 84, 30, t, w=290, tam=25, cor=FOSF, peso=700, serif=True), rot(x + 22, 100, d, w=350, tam=21, cor=TINTA, lh=1.3)]
        p.append(seta(x + 196, 254, x + 196, 284, FOSF, "m0", esp=3))
    p.append(caixa(0, 290, 1664, 70, FOSF, FOSF, esp=0, rx=35))
    p.append(icone("t:hand-stop", 24, 304, 40, PAPEL))
    rs.append(rot(80, 308, "parar e encaminhar ao médico, no mesmo dia, antes de qualquer exercício", w=1560, tam=23, cor=PAPEL, peso=700))
    return slide("bandeiras", 360, p, rs, eyebrow="Primeira pergunta", titulo="Parar e encaminhar antes de qualquer exercício",
                 destaque="Nenhum é diagnóstico; todos mudam o caminho. E a crença de que o ombro está “estragado” também é achado de avaliação.", destaque_cor="tinta")


def sinss_81():
    """8.1: as cinco letras, com a irritabilidade em destaque e a régua de tempo que decide o exame do dia."""
    p = [svg_abre(1664, 400, "Cinco colunas: gravidade, quanto a dor limita; irritabilidade, quanto tempo leva para acalmar, em destaque; natureza, o tipo de problema e as bandeiras; estágio, agudo, subagudo, persistente; estabilidade, melhorando, piorando ou parado. Embaixo, a régua da irritabilidade: acalma em minutos, dá para testar até onde dói; fica acesa por horas, exame curto hoje e o resto na próxima sessão")]
    rs = []
    cols = [("Gravidade", "quanto a dor limita"), ("Irritabilidade", "quanto tempo leva para acalmar"), ("Natureza", "o tipo de problema, e as bandeiras"),
            ("Estágio", "agudo, subagudo, persistente"), ("Estabilidade", "melhorando, piorando ou parado")]
    for k, (t, d) in enumerate(cols):
        x = k * 337
        dest = k == 1
        cor = FOSF if dest else OXID
        p.append(caixa(x, 0, 312, 200, cor, FOSF_T if dest else CARTAO, esp=4 if dest else 2, rx=16))
        rs += [rot(x + 16, 22, t, w=280, tam=25, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 16, 84, d, w=280, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    p.append(f'<line x1="505" y1="204" x2="505" y2="236" stroke="{FOSF}" stroke-width="3"/>')
    for k, (t, d, cor, fundo, ic) in enumerate([("acalma em minutos", "dá para testar até onde dói", OXID, OXID_T, "t:stopwatch"),
                                                 ("fica acesa por horas", "exame curto hoje, o resto na próxima sessão", FOSF, FOSF_T, "t:hourglass")]):
        x = k * 852
        p.append(caixa(x, 240, 812, 160, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 290, 52, cor))
        rs += [rot(x + 96, 262, t, w=690, tam=26, cor=cor, peso=700, serif=True), rot(x + 96, 312, d, w=690, tam=22, cor=TINTA, lh=1.3)]
    return slide("sinss", 400, p, rs, eyebrow="Segunda pergunta", titulo="Gravidade, irritabilidade, natureza, estágio, estabilidade", fonte="J Man Manip Ther 2021")


def cif_81():
    """8.1: os três níveis da CIF, com o laudo embaixo e o motivo da consulta em cima, e a ficha da escala do próprio paciente."""
    p = [svg_abre(1664, 360, "À esquerda, os três níveis da CIF em degraus. Embaixo, estrutura e função: tendão, amplitude, força; é onde mora o laudo. No meio, atividade: raspagem, empurrar, dormir de lado. Em cima, participação: treinar com a turma, competir; é onde mora o motivo da consulta. À direita, a ficha da escala do próprio paciente, com notas de 0 a 10: guarda fechada, 3; dormir sobre o lado direito, 4; flexão de braço, 5")]
    rs = []
    niveis = [("participação", "treinar com a turma, competir", OXID, 0, "o motivo da consulta"), ("atividade", "raspagem, empurrar, dormir de lado", GLIC, 1, ""),
              ("estrutura e função", "tendão, amplitude, força", AZUL, 2, "o laudo")]
    for t, d, cor, k, tag in niveis:
        x, y, w = 120 - k * 60, k * 122, 640 + k * 120
        p.append(caixa(x, y, w, 104, cor, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, y + 14, t, w=w - 40, tam=24, cor=cor, peso=700, serif=True), rot(x + 20, y + 56, d, w=w - 40, tam=20, cor=TINTA)]
        if tag:
            rs.append(rot(x + w - 290, y + 16, tag, w=270, tam=18, cor=cor, peso=700, alinha="right"))
    X = 940
    p.append(caixa(X, 0, 724, 360, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 18, "Escala do próprio paciente", w=680, tam=25, cor=TINTA, peso=700, serif=True))
    for k, (t, v) in enumerate([("guarda fechada", 3), ("dormir sobre o lado direito", 4), ("flexão de braço", 5)]):
        y = 80 + k * 90
        rs += [rot(X + 24, y, t, w=520, tam=21, cor=TINTA, peso=700), rot(X + 560, y - 4, f"{v} / 10", w=140, tam=26, cor=OXID, peso=700, alinha="right", serif=True)]
        p.append(f'<rect x="{X + 24}" y="{y + 38}" width="660" height="22" rx="11" fill="{PAPEL}" stroke="{BORDA}" stroke-width="1"/>')
        p.append(f'<rect x="{X + 24}" y="{y + 38}" width="{66 * v}" height="22" rx="11" fill="{OXID}"/>')
    return slide("cif", 360, p, rs, eyebrow="Terceira pergunta", titulo="O laudo mora num nível; o motivo da consulta, em outro",
                 destaque="Três a cinco atividades escolhidas pela pessoa, nota de 0 a 10: a meta do tratamento e a primeira medida que se repete.", destaque_cor="tinta",
                 fonte="OMS 2001 · Physiother Can 1995")


def hipoteses_81():
    """8.1: cinco hipóteses, cada uma ligada ao teste que pode derrubá-la."""
    p = [svg_abre(1664, 420, "Cinco hipóteses, cada uma ligada por uma seta ao teste que pode derrubá-la. Força insuficiente: os dois lados, dinamômetro de mão ou repetições até a falha técnica. Amplitude limitada: goniômetro, fita ou inclinômetro do celular, sempre igual. Controle ruim: a própria tarefa, filmada de frente e de lado. Pouca tolerância a volume: quantas repetições e séries antes de a dor subir. Medo, crença, expectativa: perguntar o que você acha que está acontecendo"), defs(MUDO)]
    rs = []
    itens = [("t:barbell", "Força insuficiente", "os dois lados; dinamômetro de mão ou repetições até a falha técnica"),
             ("t:ruler-measure", "Amplitude limitada", "goniômetro, fita ou inclinômetro do celular, sempre igual"),
             ("t:camera-selfie", "Controle ruim", "a própria tarefa, filmada de frente e de lado"),
             ("t:repeat", "Pouca tolerância a volume", "quantas repetições e séries antes de a dor subir"),
             ("t:message-circle", "Medo, crença, expectativa", "“O que você acha que está acontecendo?”")]
    for k, (ic, h, t) in enumerate(itens):
        y = k * 84
        p.append(caixa(0, y, 520, 72, GLIC, GLIC_T, esp=2, rx=14))
        p.append(icone(ic, 18, y + 16, 40, GLIC))
        rs.append(rot(72, y + 22, h, w=440, tam=22, cor=TINTA, peso=700))
        p.append(seta(524, y + 36, 592, y + 36, MUDO, "m0", esp=3))
        p.append(caixa(600, y, 1064, 72, OXID, CARTAO, esp=2, rx=14))
        rs.append(rot(624, y + 22, t, w=1020, tam=21, cor=TINTA))
    return slide("hipoteses", 420, p, rs, eyebrow="Quarta pergunta", titulo="Cada hipótese com o teste que pode derrubá-la",
                 destaque="Se nenhum resultado possível muda o que você faz, não faça o teste.", destaque_cor="verm")


def laudo_81():
    """8.1: o que o laudo diz e o que a avaliação diz, no mesmo ombro; só a segunda vira plano."""
    p = [svg_abre(1664, 360, "O mesmo ombro, duas leituras. O laudo diz o que está alterado: um tendão espessado, que não vai sumir em doze semanas. A avaliação diz o que dá para mudar: a rotação externa daquele lado tem bem menos força que a do outro, a amplitude está boa, a dor aparece com volume, não com posição. As duas são verdadeiras; só a segunda produz um plano"), defs(OXID)]
    rs = []
    p.append(caixa(0, 0, 640, 360, AZUL, AZUL_T, esp=2, rx=16))
    p.append(icone("t:clipboard-list", 24, 22, 48, AZUL))
    rs += [rot(88, 30, "O laudo: o que está alterado", w=530, tam=25, cor=AZUL, peso=700, serif=True),
           rot(24, 120, "tendão espessado", w=590, tam=24, cor=TINTA, peso=700), rot(24, 166, "não vai sumir em doze semanas", w=590, tam=22, cor=TINTA),
           rot(24, 290, "verdadeiro", w=590, tam=21, cor=AZUL, peso=700)]
    p.append(caixa(680, 0, 640, 360, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:stethoscope", 704, 22, 48, OXID))
    rs.append(rot(768, 30, "A avaliação: o que dá para mudar", w=530, tam=25, cor=OXID, peso=700, serif=True))
    for k, t in enumerate(["rotação externa bem mais fraca desse lado", "amplitude boa", "a dor vem com volume, não com posição"]):
        y = 104 + k * 60
        p.append(icone("t:check", 704, y, 34, OXID))
        rs.append(rot(750, y + 4, t, w=550, tam=21, cor=TINTA, peso=700 if k == 0 else 400))
    rs.append(rot(704, 290, "verdadeiro também", w=590, tam=21, cor=OXID, peso=700))
    p.append(seta(1324, 180, 1374, 180, OXID, "m0", esp=4))
    p.append(caixa(1384, 80, 280, 200, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1394, 110, "só esta", w=260, tam=22, cor=PAPEL, alinha="center"), rot(1394, 150, "produz um plano", w=260, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.2)]
    return slide("laudo", 360, p, rs, eyebrow="A ideia da aula", titulo="O laudo diz o que está alterado. A avaliação diz o que dá para mudar.")


def vieses_81():
    """8.1: quatro erros de raciocínio, cada um com um ícone."""
    p = [svg_abre(1664, 340, "Quatro erros de raciocínio, nenhum por falta de conhecimento. Ancorar no laudo: o resto da avaliação vira confirmação. Fechar cedo: a hipótese pronta em três minutos. Só o que confirma: esquece o teste que poderia derrubar. Tratar o achado, e não a queixa da pessoa")]
    rs = []
    itens = [("t:anchor", "Ancorar no laudo", "o resto da avaliação vira confirmação", GLIC), ("t:lock", "Fechar cedo", "a hipótese pronta em três minutos", GLIC),
             ("t:filter", "Só o que confirma", "esquece o teste que poderia derrubar", GLIC), ("t:target", "Tratar o achado", "e não a queixa da pessoa", FOSF)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 424
        p.append(caixa(x, 0, 392, 340, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 196}" cy="80" r="52" fill="{GLIC_T if cor == GLIC else FOSF_T}"/>')
        p.append(icone(ic, x + 166, 50, 60, cor))
        rs += [rot(x + 20, 156, t, w=352, tam=26, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 20, 212, d, w=352, tam=22, cor=TINTA, alinha="center", lh=1.3)]
    return slide("vieses", 340, p, rs, eyebrow="Nenhum é falta de conhecimento", titulo="Quatro erros de raciocínio",
                 destaque="Triagem de movimento não prevê quem vai se lesionar. Serve para descrever, orientar e acompanhar.", destaque_cor="tinta", fonte="Br J Sports Med 2016")


def quem_81():
    """8.1: quatro fontes de informação convergindo para o plano."""
    p = [svg_abre(1664, 400, "Quatro fontes de informação convergindo para o plano de reabilitação. Médico: diagnóstico, bandeiras, decisão sobre imagem. Fisioterapia: irritabilidade, função, hipóteses, medidas repetidas e o plano. Preparação física: como treinava antes, a carga da semana típica, o alvo do retorno. O próprio atleta: as metas, e se está melhorando, antes do teste"), defs(MUDO)]
    rs = []
    fontes = [("t:stethoscope", "Médico", "diagnóstico, bandeiras, decisão sobre imagem", AZUL, 0, 0), ("t:clipboard-check", "Fisioterapia", "irritabilidade, função, hipóteses, medidas repetidas e o plano", OXID, 0, 210),
              ("t:barbell", "Preparação física", "como treinava antes: a carga da semana típica, o alvo do retorno", GLIC, 1104, 0), ("h:running", "O próprio atleta", "as metas; e se está melhorando, antes do teste", TINTA, 1104, 210)]
    for ic, t, d, cor, x, y in fontes:
        p.append(caixa(x, y, 560, 190, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, x + 22, y + 22, 46, cor))
        rs += [rot(x + 82, y + 30, t, w=460, tam=25, cor=cor, peso=700, serif=True), rot(x + 22, y + 96, d, w=516, tam=21, cor=TINTA, lh=1.3)]
        p.append(seta(x + 564 if x == 0 else x - 4, y + 95, 640 if x == 0 else 1024, 200, MUDO, "m0", esp=3))
    p.append(caixa(648, 130, 368, 140, TINTA, TINTA, esp=0, rx=70))
    rs.append(rot(648, 180, "o plano", w=368, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("quem", 400, p, rs, eyebrow="Quem faz o quê", titulo="Quatro fontes de informação")

# ---------------------------------------------------------------- aplicação

LICOES = {"08-01": [tatame_81, roteiro_81, bandeiras_81, sinss_81, cif_81, hipoteses_81, laudo_81, vieses_81, quem_81]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
