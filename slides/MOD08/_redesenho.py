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

# ---------------------------------------------------------------- 8.2

def folha_82():
    """8.2: a folha de oito semanas e, na semana cinco, as duas corredoras possíveis."""
    p = [svg_abre(1664, 380, "À esquerda, a folha de protocolo: semanas um e dois, proteção; três e quatro, fortalecimento; cinco, trote; seis, corrida contínua; oito, liberada. A semana cinco está marcada. À direita, as duas corredoras possíveis nessa semana: uma pronta desde a semana três, que perdeu duas semanas; outra que não faz vinte elevações de calcanhar numa perna só, e o trote vira recidiva"), defs(MUDO)]
    rs = []
    p.append(f'<path d="M 0 0 H 520 L 580 60 V 380 H 0 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
    linhas = [("sem 1 e 2", "proteção"), ("sem 3 e 4", "fortalecimento"), ("sem 5", "trote"), ("sem 6", "corrida contínua"), ("sem 8", "liberada")]
    for k, (a, b) in enumerate(linhas):
        y = 30 + k * 68
        if k == 2:
            p.append(f'<rect x="12" y="{y - 10}" width="530" height="56" rx="8" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
        rs += [rot(28, y + 4, a, w=170, tam=21, cor=MUDO, peso=700), rot(200, y + 4, b, w=330, tam=22, cor=TINTA, peso=700 if k == 2 else 400)]
    p.append(seta(584, 167, 680, 90, MUDO, "m0", esp=3))
    p.append(seta(584, 167, 680, 280, MUDO, "m0", esp=3))
    for k, (t, d, cor, fundo, ic) in enumerate([("pronta desde a semana três", "perdeu duas semanas", GLIC, GLIC_T, "t:hourglass"),
                                                 ("não faz 20 elevações de calcanhar numa perna só", "o trote da semana cinco vira a recidiva da seis", FOSF, FOSF_T, "t:alert-triangle")]):
        y = k * 200
        p.append(caixa(690, y, 974, 180, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 714, y + 24, 48, cor))
        rs += [rot(778, y + 26, t, w=860, tam=25, cor=cor, peso=700, serif=True, lh=1.15), rot(778, y + 110, d, w=860, tam=22, cor=TINTA)]
    return slide("folha", 380, p, rs, eyebrow="Semana um, semana dois, semana oito", titulo="A folha sabe que dia é. Não sabe como está a panturrilha.",
                 destaque="Troca-se a folha de semanas por uma sequência de portas.", destaque_cor="tinta")


def piso_82():
    """8.2: uma porta com duas trancas, o tempo biológico e o critério funcional; abre só com as duas."""
    p = [svg_abre(1664, 400, "Uma porta com duas trancas. A de baixo é o tempo biológico, o piso: enxerto, osso e tendão não se apressam, e abaixo dele nenhum teste autoriza carga alta; o erro é dizer que já passaram seis semanas, então pode. A de cima é o critério funcional, a porta: o que a pessoa consegue fazer, com qualidade, sem dor que dure até o dia seguinte; o erro é um teste ótimo antes do tempo biológico. A porta só abre com as duas")]
    rs = []
    p.append(f'<rect x="672" y="20" width="320" height="380" rx="10" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="700" y="48" width="264" height="352" rx="6" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    for y, cor, ic in [(110, OXID, "t:lock"), (270, GLIC, "t:lock")]:
        p.append(f'<circle cx="832" cy="{y + 30}" r="40" fill="{cor}"/>')
        p.append(icone(ic, 808, y + 6, 48, PAPEL))
    rs += [rot(672, 196, "abre só com as duas", w=320, tam=20, cor=TINTA, peso=700, alinha="center")]
    for k, (t, sub, itens, err, cor, fundo, x, y) in enumerate([
            ("Critério funcional", "a porta", ["o que a pessoa consegue fazer, com qualidade", "sem dor que dure até o dia seguinte"], "erro: teste ótimo antes do tempo biológico", OXID, OXID_T, 1040, 0),
            ("Tempo biológico", "o piso", ["enxerto, osso, tendão não se apressam", "abaixo do piso, nenhum teste autoriza carga alta"], "erro: “já passaram seis semanas, então pode”", GLIC, GLIC_T, 0, 160)]):
        p.append(caixa(x, y, 624, 240, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, y + 16, t, w=380, tam=26, cor=cor, peso=700, serif=True), rot(x + 420, y + 22, sub, w=180, tam=20, cor=cor, peso=700, alinha="right")]
        for j, it in enumerate(itens):
            rs.append(rot(x + 24, y + 70 + j * 40, "· " + it, w=580, tam=20, cor=TINTA))
        rs.append(rot(x + 24, y + 170, err, w=580, tam=20, cor=FOSF, peso=700, lh=1.2))
        p.append(f'<line x1="{x + 624 if x == 0 else x}" y1="{y + 120}" x2="{792 if x == 0 else 872}" y2="{300 if x == 0 else 140}" stroke="{cor}" stroke-width="3"/>')
    return slide("piso", 400, p, rs, eyebrow="Tempo e critério não são rivais", titulo="O tempo é o piso; o critério é a porta",
                 destaque="Faltou um dos dois, a porta fica fechada.", destaque_cor="verm")


def resposta_82():
    """8.2: uma linha de 24 horas, da sessão até a manhã seguinte, com as quatro perguntas na ponta."""
    p = [svg_abre(1664, 380, "Uma linha de vinte e quatro horas, da sessão de hoje até a manhã seguinte. É na manhã seguinte que se lê a resposta, em quatro perguntas. Dor: voltou ao nível de antes até a manhã seguinte? Rigidez: a da manhã está igual ou pior? Inchaço: apareceu onde não havia? Função: consegue fazer o que fazia ontem?"), defs(MUDO)]
    rs = []
    p.append(seta(60, 60, 1600, 60, MUDO, "m0", esp=3))
    p.append(f'<circle cx="80" cy="60" r="22" fill="{TINTA}"/>')
    p.append(f'<circle cx="1560" cy="60" r="22" fill="{OXID}"/>')
    rs += [rot(0, 96, "a sessão de hoje", w=300, tam=20, cor=TINTA, peso=700), rot(1364, 96, "a manhã seguinte", w=300, tam=20, cor=OXID, peso=700, alinha="right"),
           rot(400, 20, "24 horas", w=860, tam=22, cor=MUDO, peso=700, alinha="center")]
    qs = [("t:bolt", "Dor", "voltou ao nível de antes até a manhã seguinte?"), ("t:adjustments-horizontal", "Rigidez", "a da manhã está igual ou pior?"),
          ("t:droplet", "Inchaço", "apareceu onde não havia?"), ("t:walk", "Função", "consegue fazer o que fazia ontem?")]
    for k, (ic, t, d) in enumerate(qs):
        x = k * 424
        p.append(caixa(x, 150, 392, 230, OXID, OXID_T, esp=2, rx=16))
        p.append(icone(ic, x + 22, 172, 44, OXID))
        rs += [rot(x + 80, 180, t, w=290, tam=26, cor=OXID, peso=700, serif=True), rot(x + 22, 248, d, w=350, tam=22, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 196}" y1="146" x2="1560" y2="84" stroke="{OXID}" stroke-width="1.5" opacity="0.5"/>')
    return slide("resposta", 380, p, rs, eyebrow="O sinal que decide todas as portas", titulo="A resposta de 24 horas",
                 destaque="Uma resposta pior e a carga de ontem passou do ponto, mesmo com a sessão sem dor. A própria pessoa aprende a ler e manda por mensagem.",
                 destaque_cor="tinta", fonte="Mesma lógica da régua de dor · Am J Sports Med 2007")


def saidas_82():
    """8.2: uma porta com três setas: avançar, segurar, recuar."""
    p = [svg_abre(1664, 400, "Uma porta no centro e três setas saindo dela. Para a frente, avançar: critérios cumpridos, piso passado, resposta boa por algumas sessões seguidas. Em volta da própria fase, segurar: parte cumprida, ou resposta que oscila; mais carga dentro da mesma fase. Para trás, recuar: resposta pior de forma clara, inchaço novo, função caindo; um degrau, por poucos dias"), defs(OXID, GLIC, FOSF)]
    rs = []
    p.append(f'<rect x="700" y="40" width="264" height="320" rx="10" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<circle cx="930" cy="210" r="10" fill="{TINTA}"/>')
    rs.append(rot(700, 180, "a porta", w=264, tam=24, cor=TINTA, peso=700, alinha="center", serif=True))
    p.append(seta(970, 120, 1110, 80, OXID, "m0", esp=5))
    p.append(seta(694, 300, 560, 340, FOSF, "m2", esp=5))
    cards = [("Avançar", "critérios cumpridos, piso passado, resposta boa por algumas sessões seguidas", OXID, OXID_T, 1120, 0),
             ("Segurar", "parte cumprida, ou resposta que oscila: mais carga dentro da mesma fase", GLIC, GLIC_T, 1120, 210),
             ("Recuar", "resposta pior de forma clara, inchaço novo, função caindo: um degrau, por poucos dias", FOSF, FOSF_T, 0, 190)]
    for t, d, cor, fundo, x, y in cards:
        p.append(caixa(x, y, 544, 190, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, y + 18, t, w=496, tam=28, cor=cor, peso=700, serif=True), rot(x + 24, y + 70, d, w=496, tam=21, cor=TINTA, lh=1.3)]
    p.append(seta(970, 300, 1110, 300, GLIC, "m1", esp=5))
    return slide("saidas", 400, p, rs, eyebrow="Em cada porta", titulo="Três saídas defensáveis",
                 destaque="A decisão vale até a próxima avaliação. Quem recuou na quarta pode avançar na segunda.", destaque_cor="tinta")


def portas_82():
    """8.2: quatro portas em escada, cada uma com o critério que pede."""
    p = [svg_abre(1664, 420, "Quatro portas em escada, cada uma com o critério funcional. Proteção para movimento: dor em repouso controlada, inchaço estável, dia a dia sem piora no dia seguinte. Movimento para força: amplitude perto do lado bom, marcha sem mancar, contração sem inibição. Força para potência: força perto do outro lado nos testes combinados, aguentando volume. Potência para retorno: saltos, acelerações e mudanças de direção na intensidade do esporte, sem apreensão")]
    rs = []
    portas = [("proteção → movimento", "dor em repouso controlada, inchaço estável, dia a dia sem piora no dia seguinte", OXID),
              ("movimento → força", "amplitude perto do lado bom, marcha sem mancar, contração sem inibição", OXID),
              ("força → potência", "força perto do outro lado nos testes combinados, aguentando volume", GLIC),
              ("potência → retorno", "saltos, acelerações e mudanças de direção na intensidade do esporte, sem apreensão", FOSF)]
    for k, (t, d, cor) in enumerate(portas):
        x, y = k * 424, 180 - k * 60
        p.append(caixa(x, y, 392, 420 - y, cor, CARTAO, esp=2, rx=16))
        p.append(f'<rect x="{x + 22}" y="{y + 20}" width="40" height="56" rx="4" fill="{cor}"/>')
        p.append(f'<circle cx="{x + 54}" cy="{y + 50}" r="4" fill="{PAPEL}"/>')
        rs += [rot(x + 76, y + 30, t, w=300, tam=22, cor=cor, peso=700, lh=1.15), rot(x + 22, y + 100, d, w=350, tam=21, cor=TINTA, lh=1.3)]
    return slide("portas", 420, p, rs, eyebrow="Vale para quase qualquer lesão", titulo="O que cada porta pede",
                 destaque="Os números mudam por tecido e por esporte. A lógica da tabela não muda.", destaque_cor="tinta")


def custo_82():
    """8.2: uma balança com o critério como apoio: de um lado o custo de avançar cedo, do outro o de segurar demais."""
    p = [svg_abre(1664, 340, "Uma balança equilibrada sobre o critério. Num prato, avançar cedo demais, que custa uma recidiva, muitas vezes mais longa que a primeira lesão. No outro, segurar tempo demais, que custa uma temporada, a paciência de quem volta por conta própria sem critério, e o destreino do resto do corpo")]
    rs = []
    cx = 832
    p.append(f'<path d="M {cx - 50} 300 L {cx} 150 L {cx + 50} 300 Z" fill="{TINTA}"/>')
    rs.append(rot(cx - 100, 306, "o critério", w=200, tam=22, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="{cx - 420}" y1="150" x2="{cx + 420}" y2="150" stroke="{TINTA}" stroke-width="7" stroke-linecap="round"/>')
    for sx, cor in [(cx - 420, FOSF), (cx + 420, GLIC)]:
        p.append(f'<line x1="{sx}" y1="150" x2="{sx - 80}" y2="210" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<line x1="{sx}" y1="150" x2="{sx + 80}" y2="210" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<path d="M {sx - 110} 210 H {sx + 110} Q {sx} 270 {sx - 110} 210 Z" fill="{cor}"/>')
    for k, (t, itens, cor, x) in enumerate([("Avançar cedo demais", ["recidiva, muitas vezes mais longa que a primeira"], FOSF, 0),
                                            ("Segurar tempo demais", ["uma temporada", "a paciência: volta por conta própria", "destreino do resto do corpo"], GLIC, 1124)]):
        p.append(caixa(x, 0, 540, 140, cor, FOSF_T if cor == FOSF else GLIC_T, esp=2, rx=14))
        rs.append(rot(x + 20, 12, t, w=500, tam=24, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            rs.append(rot(x + 20, 48 + j * 30, "· " + it, w=500, tam=20, cor=TINTA))
    return slide("custo", 340, p, rs, eyebrow="Os dois erros têm custo", titulo="Avançar cedo demais custa uma recidiva. Segurar tempo demais custa uma temporada.",
                 destaque="O critério existe para que a decisão não dependa do medo de quem decide.", destaque_cor="tinta")


def naoabre_82():
    """8.2: três frases em balões, cada uma riscada como chave da porta."""
    p = [svg_abre(1664, 340, "Três frases que abrem porta com frequência, e não deveriam, cada uma num balão riscado. Estou ótima: a dor some antes de a capacidade voltar. Semana seis: o protocolo diz o piso, quando diz alguma coisa. Precisamos dela no sábado: entra na aceitação de risco, não na avaliação do tecido")]
    rs = []
    itens = [("“Estou ótima.”", "a dor some antes de a capacidade voltar"), ("“Semana seis.”", "o protocolo diz o piso, quando diz alguma coisa"),
             ("“Precisamos dela no sábado.”", "entra na aceitação de risco, não na avaliação do tecido")]
    for k, (t, d) in enumerate(itens):
        x = k * 564
        p.append(f'<path d="M {x + 20} 0 H {x + 516} Q {x + 536} 0 {x + 536} 20 V 120 Q {x + 536} 140 {x + 516} 140 H {x + 120} L {x + 70} 180 L {x + 80} 140 H {x + 20} Q {x} 140 {x} 120 V 20 Q {x} 0 {x + 20} 0 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
        rs.append(rot(x + 24, 46, t, w=440, tam=26, cor=TINTA, peso=700, serif=True))
        p.append(icone("t:x", x + 478, 18, 40, FOSF))
        p.append(icone("t:key", x + 24, 200, 40, MUDO))
        rs.append(rot(x + 76, 206, d, w=440, tam=21, cor=TINTA, lh=1.3))
    return slide("naoabre", 340, p, rs, eyebrow="Abrem porta com frequência", titulo="Três coisas que não deveriam abrir",
                 destaque="Misturar pressão com avaliação é o jeito mais comum de liberar quem não passou na porta.", destaque_cor="tinta")


def degraus_82():
    """8.2: três degraus depois da última porta, cada um com o exemplo da corredora."""
    p = [svg_abre(1664, 360, "Depois da última porta, três degraus. Participar: treina de forma modificada ou restrita; corre com o grupo, sem os tiros. Voltar ao esporte: compete, ainda sem o nível de antes; prova curta sem objetivo de tempo. Voltar ao desempenho: no nível de antes ou acima; o ritmo que tinha")]
    rs = []
    p.append(f'<rect x="0" y="80" width="120" height="280" rx="8" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
    rs.append(rot(0, 200, "última porta", w=120, tam=17, cor=TINTA, peso=700, alinha="center", lh=1.2))
    degs = [("Participar", "treina modificado ou restrito", "corre com o grupo, sem os tiros", GLIC), ("Voltar ao esporte", "compete, sem o nível de antes", "prova curta sem objetivo de tempo", OXID),
            ("Voltar ao desempenho", "no nível de antes ou acima", "o ritmo que tinha", TINTA)]
    for k, (t, d, ex, cor) in enumerate(degs):
        x, y = 160 + k * 504, 200 - k * 100
        p.append(caixa(x, y, 484, 360 - y, cor, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, y + 16, t, w=440, tam=25, cor=cor, peso=700, serif=True), rot(x + 20, y + 60, d, w=440, tam=20, cor=TINTA),
               rot(x + 20, y + 96, ex, w=440, tam=19, cor=MUDO, peso=700)]
    return slide("degraus", 360, p, rs, eyebrow="A última fase não é um dia", titulo="Três degraus depois da última porta",
                 destaque="É aqui que a reabilitação sai da sala e a preparação física passa a conduzir junto.", destaque_cor="tinta", fonte="Consenso de Berna, Br J Sports Med 2016")


def quem_82():
    """8.2: as fases em colunas e faixas de quem conduz, com o treinador avisado em todas."""
    p = [svg_abre(1664, 380, "As cinco fases em colunas e, em faixas, quem conduz e decide. Fisioterapia nas três primeiras, com o médico quando o tecido é de risco. Fisioterapia e preparação física juntas em potência e gesto. Decisão compartilhada, com o atleta, no retorno. E uma faixa atravessando todas: alguém avisa o treinador em que porta o atleta está")]
    rs = []
    fases = ["proteção", "movimento", "força", "potência e gesto", "retorno"]
    X0, W = 260, 280
    for k, f in enumerate(fases):
        rs.append(rot(X0 + k * W, 0, f, w=W - 10, tam=20, cor=TINTA, peso=700, alinha="center"))
        p.append(f'<line x1="{X0 + k * W}" y1="34" x2="{X0 + k * W}" y2="380" stroke="{BORDA}" stroke-width="2"/>')
    faixas = [("fisioterapia", 0, 3, OXID, 50), ("médico, se tecido de risco", 0, 3, AZUL, 118), ("fisioterapia + preparação física", 3, 4, GLIC, 186),
              ("decisão compartilhada, com o atleta", 4, 5, TINTA, 254)]
    for t, a, b, cor, y in faixas:
        dashed = "médico" in t
        p.append(f'<rect x="{X0 + a * W + 6}" y="{y}" width="{(b - a) * W - 12}" height="56" rx="28" fill="{cor if not dashed else AZUL_T}" stroke="{cor}" stroke-width="2"{TRACO if dashed else ""}/>')
        rs.append(rot(X0 + a * W + 16, y + 15, t, w=(b - a) * W - 32, tam=19, cor=PAPEL if not dashed else AZUL, peso=700, alinha="center", lh=1.1))
    rs += [rot(0, 64, "conduz e decide", w=240, tam=19, cor=MUDO, peso=700, alinha="right")]
    p.append(f'<rect x="{X0 + 6}" y="322" width="{5 * W - 12}" height="52" rx="26" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    p.append(icone("t:speakerphone", X0 + 20, 330, 36, FOSF))
    rs += [rot(X0 + 70, 334, "alguém avisa o treinador em que porta o atleta está", w=1300, tam=21, cor=FOSF, peso=700), rot(0, 334, "em todas", w=240, tam=19, cor=FOSF, peso=700, alinha="right")]
    return slide("quem", 380, p, rs, eyebrow="Quem abre cada porta", titulo="Condução e decisão, fase a fase",
                 destaque="A informação que mais falta: o técnico põe o atleta na finalização porque “ele já está treinando”.", destaque_cor="verm")


def ficha_82():
    """8.2: a ficha de uma página desenhada, e o que ela resolve."""
    p = [svg_abre(1664, 400, "Uma ficha de uma página desenhada: a fase atual, marcada numa régua de cinco fases; os critérios da próxima porta, dois cumpridos e um pendente; e a resposta de 24 horas das últimas sessões, em pontos. Ao lado, o que ela resolve: a pessoa conquista, não conta dias; a equipe fala a mesma língua; avançar deixa de ser opinião do dia")]
    rs = []
    p.append(f'<path d="M 0 0 H 900 L 960 60 V 400 H 0 Z" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(24, 16, "fase atual", w=300, tam=19, cor=MUDO, peso=700))
    for k in range(5):
        p.append(f'<rect x="{24 + k * 176}" y="48" width="164" height="36" rx="18" fill="{OXID if k < 3 else PAPEL}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(24 + 2 * 176, 54, "força", w=164, tam=18, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(24, 108, "critérios da próxima porta", w=500, tam=19, cor=MUDO, peso=700))
    for j, (t, ok) in enumerate([("força perto do outro lado", True), ("aguenta volume", True), ("tarefa mais exigente sem piora no dia seguinte", False)]):
        y = 144 + j * 50
        p.append(icone("t:check" if ok else "t:hourglass", 24, y, 34, OXID if ok else GLIC))
        rs.append(rot(70, y + 4, t, w=820, tam=21, cor=TINTA, peso=700 if not ok else 400))
    rs.append(rot(24, 306, "resposta de 24 h, últimas sessões", w=600, tam=19, cor=MUDO, peso=700))
    for j, c in enumerate([OXID, OXID, GLIC, OXID, OXID]):
        p.append(f'<circle cx="{44 + j * 56}" cy="360" r="18" fill="{c}"/>')
    X = 1020
    p.append(caixa(X, 0, 644, 400, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(X + 24, 18, "O que ela resolve", w=600, tam=26, cor=TINTA, peso=700, serif=True))
    for j, t in enumerate(["a pessoa conquista, não conta dias", "a equipe fala a mesma língua", "avançar deixa de ser opinião do dia"]):
        y = 96 + j * 96
        p.append(f'<circle cx="{X + 44}" cy="{y + 18}" r="20" fill="{OXID}"/>')
        rs += [rot(X + 24, y + 5, str(j + 1), w=40, tam=20, cor=PAPEL, peso=700, alinha="center"), rot(X + 80, y + 4, t, w=540, tam=23, cor=TINTA, peso=700)]
    return slide("ficha", 400, p, rs, eyebrow="O que substitui a folha de semanas", titulo="Uma ficha de uma página",
                 destaque="O prazo existe, como faixa: “depende de você passar nas portas, não do calendário”.", destaque_cor="tinta")

# ---------------------------------------------------------------- 8.3

def bomba_83():
    """8.3: a curva de carbono-14 na atmosfera, em esquema, e o que ela revelou no tendão e no músculo."""
    p = [svg_abre(1664, 380, "À esquerda, em esquema, a concentração de carbono-14 na atmosfera: sobe de repente com os testes nucleares, até a proibição em 1963, e cai devagar depois. Funciona como data de fabricação de cada tecido. À direita, o resultado em 28 tendões de Aquiles de pessoas nascidas entre 1945 e 1983: o carbono do miolo do tendão correspondia aos primeiros 17 anos de vida; no músculo das mesmas pessoas, a renovação era contínua")]
    rs = []
    p.append(caixa(0, 0, 820, 380, TINTA, CARTAO, esp=2, rx=16))
    X0, B = 60, 300
    p.append(f'<line x1="{X0}" y1="{B}" x2="790" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {X0} {B - 10} L 250 {B - 14} C 290 {B - 20}, 310 70, 350 66 C 420 70, 520 170, 780 {B - 40}" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    p.append(f'<line x1="350" y1="56" x2="350" y2="{B}" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
    for x, t in [(X0, "1950"), (350, "1963"), (560, "1980"), (760, "2000")]:
        rs.append(rot(x - 40, B + 8, t, w=80, tam=18, cor=MUDO, alinha="center"))
    rs += [rot(362, 46, "proibição dos testes", w=260, tam=18, cor=TINTA, peso=700),
           rot(24, 16, "carbono-14 na atmosfera · esquema", w=600, tam=19, cor=GLIC, peso=700),
           rot(24, 344, "a data de fabricação de cada tecido", w=760, tam=19, cor=MUDO)]
    for k, (ic, t, d, cor, fundo) in enumerate([("t:hourglass", "Miolo do tendão de Aquiles", "carbono dos primeiros 17 anos de vida", FOSF, FOSF_T),
                                                 ("t:refresh", "Músculo, mesmas pessoas", "renovação contínua", OXID, OXID_T)]):
        y = k * 150
        p.append(caixa(860, y, 804, 136, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 884, y + 24, 44, cor))
        rs += [rot(944, y + 26, t, w=700, tam=25, cor=cor, peso=700, serif=True), rot(944, y + 76, d, w=700, tam=22, cor=TINTA)]
    rs.append(rot(860, 318, "28 tendões, pessoas nascidas entre 1945 e 1983", w=804, tam=21, cor=TINTA, peso=700))
    return slide("bomba", 380, p, rs, eyebrow="O carbono-14 dos testes nucleares como data de fabricação", titulo="O miolo do tendão de Aquiles adulto tem o colágeno da adolescência.",
                 fonte="FASEB J 2013")


def desmontar_83():
    """8.3: o corte do tendão com o miolo fixo e a resposta acontecendo no material e na periferia."""
    p = [svg_abre(1664, 360, "Um corte de tendão. O miolo, em cinza, não é trocado: isso explica a cicatrização ruim e a tendinopatia de meses. Em volta, setas de resposta: o tendão responde a treino, mudando o material, como as fibras se ligam, e a periferia e a matriz ao redor. A dose e a paciência são outras")]
    rs = []
    cx, cy = 400, 180
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="300" ry="160" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="150" ry="80" fill="{CINZA}"/>')
    rs += [rot(cx - 140, cy - 30, "miolo", w=280, tam=24, cor=TINTA, peso=700, alinha="center"), rot(cx - 140, cy + 4, "não é trocado", w=280, tam=19, cor=TINTA, alinha="center")]
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        x1, y1 = cx + 190 * math.cos(a), cy + 105 * math.sin(a)
        x2, y2 = cx + 270 * math.cos(a), cy + 145 * math.sin(a)
        p.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{OXID}" stroke-width="4" stroke-linecap="round"/>')
    for k, (t, itens, cor) in enumerate([("O que significa", ["o núcleo de colágeno não é trocado", "explica a cicatrização ruim", "explica tendinopatia de meses"], TINTA),
                                         ("O que não significa", ["que o tendão não responde a treino", "a resposta muda o material e a periferia", "a dose e a paciência são outras"], OXID)]):
        y = k * 186
        p.append(caixa(760, y, 904, 174, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(784, y + 14, t, w=860, tam=24, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            rs.append(rot(784, y + 56 + j * 36, "· " + it, w=860, tam=21, cor=TINTA))
    return slide("desmontar", 360, p, rs, eyebrow="Antes que o número vire mito", titulo="O tendão muda devagar, e de outro jeito", fonte="FASEB J 2013")


def musculo_83():
    """8.3: barras da síntese de proteína muscular acima do repouso em 3, 24 e 48 horas."""
    p = [svg_abre(1664, 340, "Barras da síntese de proteína muscular acima do repouso depois de uma sessão de força, em oito pessoas destreinadas. Três horas depois: mais 112%. Vinte e quatro horas: mais 65%. Quarenta e oito horas: mais 34%. Uma sessão, quase dois dias de sinal")]
    rs = []
    B, E = 280, 2.0
    for k, (t, v) in enumerate([("3 h", 112), ("24 h", 65), ("48 h", 34)]):
        x = 120 + k * 380
        p.append(f'<rect x="{x}" y="{B - v * E:.0f}" width="260" height="{v * E:.0f}" rx="6" fill="{OXID}" opacity="{1 - k * 0.2:.1f}"/>')
        rs += [rot(x, B - v * E - 50, f"+{v}%", w=260, tam=40, cor=OXID, peso=700, alinha="center", serif=True), rot(x, B + 10, t, w=260, tam=22, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="80" y1="{B}" x2="1240" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(80, 318, "síntese de proteína acima do repouso · depois de uma sessão", w=1100, tam=17, cor=MUDO))
    p.append(caixa(1300, 40, 364, 220, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(1316, 70, "uma sessão,", w=332, tam=24, cor=PAPEL, alinha="center"), rot(1316, 110, "quase dois dias de sinal", w=332, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.2)]
    return slide("musculo", 340, p, rs, eyebrow="O relógio do músculo", titulo="Uma sessão de força, quase dois dias de sinal",
                 destaque="A degradação também sobe. Em jejum, o balanço seguiu negativo, só menos que em repouso: o sinal vem da carga, a matéria-prima vem da comida.",
                 destaque_cor="ambar", fonte="8 destreinados, 8 × 8 a 80% de 1RM · Am J Physiol 1997")


def magnitude_83():
    """8.3: duas barras de tamanho de efeito na rigidez do tendão, alta e baixa intensidade, e a régua de semanas."""
    p = [svg_abre(1664, 340, "Duas barras do tamanho de efeito na rigidez do tendão. Com contrações acima de 70% da contração máxima: 0,90, efeito grande. Com intensidade menor: 0,04, praticamente nada. Ao lado, uma régua de semanas: intervenções com mais de 12 semanas funcionaram melhor")]
    rs = []
    X0, E = 380, 900
    for k, (t, v, cor) in enumerate([("acima de 70% da contração máxima", 0.90, OXID), ("intensidade menor", 0.04, FOSF)]):
        y = 20 + k * 120
        rs.append(rot(0, y + 22, t, w=350, tam=21, cor=TINTA, peso=700, alinha="right", lh=1.2))
        p.append(f'<rect x="{X0}" y="{y}" width="{max(v * E, 6):.0f}" height="90" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + max(v * E, 6) + 18, y + 18, f"{v:.2f}".replace(".", ","), w=200, tam=44, cor=cor, peso=700, serif=True))
    rs.append(rot(X0, 236, "tamanho de efeito na rigidez do tendão", w=800, tam=18, cor=MUDO))
    p.append(caixa(0, 270, 1664, 70, TINTA, PAPEL, esp=2, rx=35))
    for w in range(1, 15):
        x = 40 + w * 90
        p.append(f'<rect x="{x}" y="288" width="70" height="34" rx="6" fill="{OXID if w > 12 else CINZA}"/>')
    rs.append(rot(1400, 292, "mais de 12 semanas", w=250, tam=21, cor=OXID, peso=700))
    return slide("magnitude", 340, p, rs, eyebrow="O que faz o tendão se adaptar", titulo="Magnitude e tempo",
                 destaque="O tipo de contração pesou menos que a intensidade. Na fase de construção: carga alta, lenta e controlada, por meses.", destaque_cor="tinta",
                 fonte="Metanálise em tendões saudáveis · Sports Med Open 2015")


def desuso_83():
    """8.3: barras de perda com a perna engessada: área e força em 5 dias, força em 14 dias."""
    p = [svg_abre(1664, 340, "Barras de perda com a perna engessada, em homens jovens e saudáveis, numa linha de dias. Em 5 dias: área do quadríceps menos 3,5% e força menos 9%. Em 14 dias: força menos 23%")]
    rs = []
    T, E = 40, 8
    bars = [("área do quadríceps", "5 dias", 3.5, GLIC, 200), ("força", "5 dias", 9, FOSF, 560), ("força", "14 dias", 23, FOSF, 920)]
    p.append(f'<line x1="120" y1="{T}" x2="1300" y2="{T}" stroke="{MUDO}" stroke-width="2"/>')
    for t, d, v, cor, x in bars:
        p.append(f'<rect x="{x}" y="{T}" width="240" height="{v * E:.0f}" rx="6" fill="{cor}"/>')
        rs += [rot(x, T + v * E + 10, f"−{str(v).replace('.', ',')}%", w=240, tam=38, cor=cor, peso=700, alinha="center", serif=True),
               rot(x, 0, f"{t} · {d}", w=240, tam=18, cor=TINTA, peso=700, alinha="center")]
    p.append(icone("t:lock", 1360, 60, 80, MUDO))
    rs += [rot(1330, 160, "perna engessada", w=300, tam=22, cor=TINTA, peso=700, alinha="center"), rot(1330, 196, "homens jovens e saudáveis", w=300, tam=19, cor=MUDO, alinha="center")]
    return slide("desuso", 340, p, rs, eyebrow="O custo de tirar o sinal", titulo="Perna engessada em homens jovens e saudáveis",
                 destaque="Proteger o tecido lesionado nos primeiros dias é necessário. Imobilizar o resto do corpo junto não é.", destaque_cor="tinta", fonte="Acta Physiol 2014")


def repouso_83():
    """8.3: proteger tira a carga que machuca; repouso total é lido como ordem de perder."""
    p = [svg_abre(1664, 340, "Dois caminhos. Proteger: tirar a carga que machuca, e manter o resto. Repouso total: o tecido lê a ausência de carga como uma ordem, e obedece: menos proteína, menos matriz, menos força")]
    rs = []
    p.append(caixa(0, 0, 700, 340, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:shield-check", 24, 24, 56, OXID))
    rs += [rot(96, 34, "Proteger", w=580, tam=30, cor=OXID, peso=700, serif=True), rot(24, 120, "tirar a carga que machuca", w=650, tam=26, cor=TINTA, peso=700),
           rot(24, 170, "e manter o resto", w=650, tam=24, cor=TINTA)]
    p.append(caixa(760, 0, 904, 340, FOSF, FOSF_T, esp=2, rx=16))
    p.append(icone("t:bed", 784, 24, 56, FOSF))
    rs += [rot(856, 34, "Repouso total", w=780, tam=30, cor=FOSF, peso=700, serif=True), rot(784, 110, "o tecido lê como ordem, e obedece:", w=850, tam=23, cor=TINTA, peso=700)]
    for j, t in enumerate(["menos proteína", "menos matriz", "menos força"]):
        x = 784 + j * 290
        p.append(f'<rect x="{x}" y="180" width="270" height="70" rx="35" fill="{CARTAO}" stroke="{FOSF}" stroke-width="2"/>')
        p.append(icone("t:trending-down", x + 18, 197, 36, FOSF))
        rs.append(rot(x + 60, 200, t, w=200, tam=21, cor=FOSF, peso=700))
    return slide("repouso", 340, p, rs, eyebrow="A ideia da aula", titulo="Repouso não é neutro. O tecido lê a ausência de carga como uma ordem.")


def relogios_83():
    """8.3: quatro faixas numa régua de tempo, das horas aos meses, uma por tecido."""
    p = [svg_abre(1664, 400, "Quatro faixas numa régua de tempo que vai de horas a meses, uma por tecido, em esquema. Músculo: responde em horas, síntese elevada por 1 a 2 dias, ganhos em semanas. Tendão: colágeno em dias, saldo depois, miolo não se renova, rigidez em mais de 12 semanas. Osso: carga dinâmica, satura com repetição, volta com pausa, meses. Ligamento e enxerto: lentos como o tendão; a biologia marca o piso de tempo")]
    rs = []
    X0, W = 300, 340
    for k, t in enumerate(["horas", "dias", "semanas", "meses"]):
        rs.append(rot(X0 + k * W, 0, t, w=W, tam=21, cor=TINTA, peso=700, alinha="center"))
        p.append(f'<line x1="{X0 + k * W}" y1="32" x2="{X0 + k * W}" y2="400" stroke="{BORDA}" stroke-width="2"/>')
    faixas = [("Músculo", 0.1, 2.6, "horas; síntese 1 a 2 dias; ganhos em semanas", OXID), ("Tendão", 1.0, 4.0, "colágeno em dias; miolo não se renova; rigidez > 12 sem", GLIC),
              ("Osso", 2.3, 4.0, "carga dinâmica; satura; volta com pausa; meses", AZUL), ("Ligamento e enxerto", 2.4, 4.0, "lentos como o tendão; a biologia marca o piso", FOSF)]
    for k, (t, a, b, d, cor) in enumerate(faixas):
        y = 50 + k * 88
        rs.append(rot(0, y + 18, t, w=280, tam=22, cor=cor, peso=700, alinha="right"))
        p.append(f'<rect x="{X0 + a * W:.0f}" y="{y}" width="{(b - a) * W:.0f}" height="72" rx="36" fill="{cor}"/>')
        rs.append(rot(X0 + a * W + 20, y + 22, d, w=(b - a) * W - 40, tam=19, cor=PAPEL, peso=700))
    return slide("relogios", 400, p, rs, eyebrow="Quatro relógios, lado a lado", titulo="O prazo é do tecido, não da dor",
                 destaque="Duas lesões com a mesma dor podem ter prazos muito diferentes.", destaque_cor="tinta")


def pratica_83():
    """8.3: cinco traduções para a prescrição, cada uma com um ícone."""
    p = [svg_abre(1664, 340, "Cinco traduções para a prescrição. Carga é sinal: sem progressão, é espera. Magnitude: principalmente no tendão. Espaçamento: tendão alterna, osso pausa. Tempo: semanas no músculo, meses no tendão. Dor não mede: informa tolerância, não adaptação")]
    rs = []
    itens = [("t:bolt", "Carga é sinal", "sem progressão, é espera", OXID), ("t:barbell", "Magnitude", "principalmente no tendão", OXID),
             ("t:calendar", "Espaçamento", "tendão alterna; osso pausa", GLIC), ("t:hourglass", "Tempo", "semanas no músculo, meses no tendão", GLIC),
             ("t:gauge", "Dor não mede", "informa tolerância, não adaptação", FOSF)]
    for k, (ic, t, d, cor) in enumerate(itens):
        x = k * 337
        p.append(caixa(x, 0, 312, 340, cor, CARTAO, esp=2, rx=16))
        p.append(f'<circle cx="{x + 156}" cy="80" r="50" fill="{OXID_T if cor == OXID else GLIC_T if cor == GLIC else FOSF_T}"/>')
        p.append(icone(ic, x + 128, 52, 56, cor))
        rs += [rot(x + 14, 156, t, w=284, tam=25, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 14, 210, d, w=284, tam=21, cor=TINTA, alinha="center", lh=1.3)]
    return slide("pratica", 340, p, rs, eyebrow="Na segunda-feira", titulo="Cinco traduções para a prescrição",
                 destaque="Avisar no começo que o tendão leva meses evita o abandono no segundo mês.", destaque_cor="tinta")

# ---------------------------------------------------------------- 8.4

def planilha_84():
    """8.4: sete semanas de volume, cada uma dez por cento maior, e a dor subindo junto, em esquema."""
    p = [svg_abre(1664, 360, "Em esquema, a planilha de um corredor voltando de tendinopatia de Aquiles: sete barras de volume semanal, cada uma dez por cento maior que a anterior, e uma linha de dor que sobe junto. Ao lado, as duas coisas que a regra não diz: sobre o que se calculam os dez por cento, e o que mais mudou naquela semana")]
    rs = []
    B, X0 = 300, 40
    pts = []
    for k in range(7):
        v = 1.1 ** k
        h = 90 * v
        x = X0 + k * 130
        p.append(f'<rect x="{x}" y="{B - h:.0f}" width="96" height="{h:.0f}" rx="6" fill="{AZUL}" opacity="0.85"/>')
        rs.append(rot(x - 10, B + 10, f"sem {k + 1}", w=116, tam=18, cor=MUDO, alinha="center"))
        pts.append((x + 48, B - 110 - k * 20 - (k * k) * 1.2))
    p.append(f'<line x1="{X0 - 10}" y1="{B}" x2="{X0 + 900}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{FOSF}" stroke-width="4"/>')
    for x, y in pts:
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="{FOSF}" stroke="{CARTAO}" stroke-width="2"/>')
    rs += [rot(X0, 0, "volume semanal +10% · esquema", w=500, tam=19, cor=AZUL, peso=700),
           rot(pts[-1][0] + 18, pts[-1][1] - 14, "dor", w=100, tam=22, cor=FOSF, peso=700)]
    p.append(caixa(1000, 0, 664, 360, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:question-mark", 1024, 22, 44, TINTA))
    rs.append(rot(1080, 28, "O que a regra não diz", w=560, tam=26, cor=TINTA, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:anchor", "sobre o que se calculam os dez por cento"), ("t:arrows-exchange", "o que mais mudou naquela semana")]):
        y = 110 + j * 120
        p.append(icone(ic, 1024, y, 44, GLIC))
        rs.append(rot(1084, y + 4, t, w=556, tam=23, cor=TINTA, lh=1.25))
    return slide("planilha", 360, p, rs, eyebrow="A conduta que parece prudente", titulo="Dez por cento por semana, religiosamente, há sete semanas. E piorando.",
                 fonte="Um corredor voltando de tendinopatia de Aquiles")


def regra_84():
    """8.4: o ensaio de 2008 com proporções iguais de lesão, e a coorte de 2014 com saltos acima de 30%."""
    p = [svg_abre(1664, 340, "Dois estudos. À esquerda, um ensaio de 2008 com 486 corredores iniciantes sorteados: lesionados com a regra dos dez por cento, 21%; sem a regra, 20%. À direita, uma coorte de 2014 com 874 iniciantes acompanhados por GPS: quem aumentou a distância mais de 30% em duas semanas teve mais lesão relacionada à distância que quem aumentou menos de 10%")]
    rs = []
    p.append(caixa(0, 0, 800, 340, GLIC, CARTAO, esp=2, rx=16))
    rs += [rot(24, 16, "Ensaio de 2008 · 486 iniciantes sorteados", w=760, tam=22, cor=GLIC, peso=700),
           rot(24, 290, "lesionados", w=760, tam=19, cor=MUDO)]
    B = 270
    for k, (t, v) in enumerate([("com a regra dos 10%", 21), ("sem a regra", 20)]):
        x = 60 + k * 360
        h = v * 7
        p.append(f'<rect x="{x}" y="{B - h}" width="300" height="{h}" rx="6" fill="{GLIC}" opacity="{1 - k * 0.3:.1f}"/>')
        rs += [rot(x, B - h - 54, f"{v}%", w=300, tam=40, cor=GLIC, peso=700, alinha="center", serif=True),
               rot(x, B - h + 18, t, w=300, tam=20, cor=PAPEL, peso=700, alinha="center")]
    p.append(caixa(864, 0, 800, 340, FOSF, CARTAO, esp=2, rx=16))
    rs += [rot(888, 16, "Coorte de 2014 · 874 iniciantes com GPS", w=760, tam=22, cor=FOSF, peso=700),
           rot(888, 290, "aumento de distância em duas semanas", w=760, tam=19, cor=MUDO)]
    p.append(f'<line x1="920" y1="270" x2="1220" y2="230" stroke="{OXID}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<line x1="1300" y1="270" x2="1600" y2="90" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
    p.append(icone("t:alert-triangle", 1540, 120, 48, FOSF))
    rs += [rot(920, 170, "menos de 10%", w=300, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(1300, 80, "mais de 30%", w=220, tam=24, cor=FOSF, peso=700),
           rot(1300, 118, "mais lesão por distância", w=230, tam=19, cor=TINTA, lh=1.2)]
    return slide("regra", 340, p, rs, eyebrow="O que a evidência diz da regra", titulo="Saltos grandes preocupam; a regra sozinha não protegeu",
                 destaque="Boa heurística de conversa, não lei. E dá para errar respeitando-a à risca.", destaque_cor="tinta",
                 fonte="Am J Sports Med 2008 · J Orthop Sports Phys Ther 2014")


def variavel_84():
    """8.4: escada de quatro degraus, do menos arriscado ao mais, com a leitura de 24 a 48 horas entre eles."""
    p = [svg_abre(1664, 400, "Uma escada de quatro degraus, do menos arriscado para o mais: frequência, mais sessões na semana; volume, mais em cada sessão; densidade, menos pausa; intensidade, ritmo, ladeira e carga, por último. Entre um degrau e outro, um relógio: a leitura de 24 a 48 horas. É regra prática, não achado de ensaio")]
    rs = []
    degraus = [("Frequência", "mais sessões na semana", OXID, OXID_T), ("Volume", "mais em cada sessão", OXID, OXID_T),
               ("Densidade", "menos pausa", GLIC, GLIC_T), ("Intensidade", "ritmo, ladeira, carga: por último", FOSF, FOSF_T)]
    W, H, B = 360, 72, 330
    for k, (t, d, cor, fundo) in enumerate(degraus):
        x, y = k * (W + 70), B - (k + 1) * H
        p.append(f'<rect x="{x}" y="{y}" width="{W}" height="{B - y}" rx="10" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
        rs += [rot(x + 18, y + 8, t, w=W - 36, tam=26, cor=cor, peso=700, serif=True), rot(x + 18, y + 44, d, w=W - 36, tam=19, cor=TINTA, lh=1.2)]
        if k < 3:
            p.append(icone("t:clock", x + W + 13, y - 58, 44, TINTA))
    p.append(icone("t:clock", 0, 20, 40, TINTA))
    rs.append(rot(52, 26, "entre um degrau e outro, leia o dia seguinte: 24 a 48 h", w=800, tam=21, cor=TINTA, peso=700))
    p.append(f'<line x1="0" y1="354" x2="1600" y2="354" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<path d="M 1600 344 L 1630 354 L 1600 364 Z" fill="{MUDO}"/>')
    rs += [rot(0, 368, "do menos arriscado para o mais", w=600, tam=20, cor=MUDO, peso=700),
           rot(1000, 368, "regra prática, não achado de ensaio", w=600, tam=20, cor=MUDO, alinha="right")]
    return slide("variavel", 400, p, rs, eyebrow="Erro dois · volume e ladeira na mesma semana", titulo="Uma variável por vez, nesta ordem")


def degrau_84():
    """8.4: os quatro elementos de um degrau, com o critério de regressão destacado."""
    p = [svg_abre(1664, 380, "Quatro caixas em sequência, os elementos de um degrau. Estímulo: elevação de calcanhar numa perna só, 3 séries, 2 repetições antes da falha. Dose: quantas vezes por semana, com que carga. Critério de saída: o que precisa acontecer para subir, por exemplo as repetições combinadas nos dois lados sem dor no dia seguinte. Critério de regressão, destacado: o que faz voltar um degrau, por exemplo dor no dia seguinte bem acima do habitual ou inchaço que voltou. É o mais importante e o menos escrito")]
    rs = []
    cards = [("t:target", "Estímulo", "elevação de calcanhar numa perna só, 3 séries, 2 repetições antes da falha", OXID, OXID_T),
             ("t:calendar", "Dose", "quantas vezes por semana, com que carga", OXID, OXID_T),
             ("t:trending-up", "Critério de saída", "o que precisa acontecer para subir: as repetições combinadas, sem dor no dia seguinte", GLIC, GLIC_T),
             ("t:arrow-down-right", "Critério de regressão", "o que faz voltar um degrau: dor no dia seguinte bem acima do habitual, ou inchaço de volta", FOSF, FOSF_T)]
    W = 386
    for k, (ic, t, d, cor, fundo) in enumerate(cards):
        x = k * (W + 40)
        ultimo = k == 3
        p.append(caixa(x, 40 if not ultimo else 0, W, 300 if not ultimo else 380, cor, fundo, esp=6 if ultimo else 2, rx=16))
        y0 = 64 if not ultimo else 24
        p.append(icone(ic, x + 20, y0, 44, cor))
        rs += [rot(x + 76, y0 + 6, t, w=W - 92, tam=24, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 20, y0 + 70, d, w=W - 40, tam=20, cor=TINTA, lh=1.3)]
        if k < 3:
            p.append(f'<path d="M {x + W + 10} 180 L {x + W + 30} 190 L {x + W + 10} 200 Z" fill="{MUDO}"/>')
    rs.append(rot(3 * (W + 40) + 20, 300, "o mais importante e o menos escrito", w=W - 40, tam=20, cor=FOSF, peso=700, lh=1.2))
    return slide("degrau", 380, p, rs, eyebrow="Erro três · o protocolo sem “desde que”", titulo="Os quatro elementos de um degrau")


def degrauabaixo_84():
    """8.4: na escada, uma piora é descer um degrau; sem plano, vira queda até o chão."""
    p = [svg_abre(1664, 360, "Duas escadas. À esquerda, com regressão escrita antes: a piora desce um degrau, por poucos dias, e a subida recomeça dali. À direita, sem plano: a piora vira queda da escada inteira, até o chão, e a subida recomeça do zero")]
    rs = []

    def escada(x0, cor):
        d = f"M {x0} 320"
        for k in range(5):
            d += f" L {x0 + k * 110} {320 - (k + 1) * 56} L {x0 + (k + 1) * 110} {320 - (k + 1) * 56}"
        d += f" L {x0 + 550} 320 Z"
        p.append(f'<path d="{d}" fill="{CINZA}" opacity="0.5" stroke="{cor}" stroke-width="3"/>')
    escada(40, OXID)
    p.append(f'<circle cx="{40 + 3 * 110 + 55}" cy="{320 - 4 * 56 - 22}" r="14" fill="{MUDO}" opacity="0.5"/>')
    p.append(f'<circle cx="{40 + 2 * 110 + 55}" cy="{320 - 3 * 56 - 22}" r="16" fill="{OXID}"/>')
    p.append(f'<path d="M {40 + 3 * 110 + 40} {320 - 4 * 56 - 40} Q {40 + 3 * 110} {320 - 4 * 56 - 70} {40 + 2 * 110 + 70} {320 - 3 * 56 - 44}" fill="none" stroke="{OXID}" stroke-width="4"/>')
    rs += [rot(620, 70, "Degrau para baixo", w=380, tam=28, cor=OXID, peso=700, serif=True),
           rot(620, 116, "regressão escrita antes", w=380, tam=21, cor=TINTA),
           rot(620, 150, "volta um passo por poucos dias", w=380, tam=21, cor=TINTA),
           rot(620, 184, "e sobe de novo dali", w=380, tam=21, cor=TINTA)]
    escada(1060, FOSF)
    p.append(f'<circle cx="{1060 + 4 * 110 + 55}" cy="{320 - 5 * 56 - 22}" r="14" fill="{MUDO}" opacity="0.5"/>')
    p.append(f'<circle cx="1640" cy="304" r="16" fill="{FOSF}"/>')
    p.append(f'<path d="M {1060 + 4 * 110 + 40} {320 - 5 * 56 - 30} C 1640 10, 1650 150, 1640 288" fill="none" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
    rs += [rot(1060, 0, "Queda da escada", w=330, tam=28, cor=FOSF, peso=700, serif=True),
           rot(1060, 40, "sem plano: para tudo", w=330, tam=21, cor=TINTA),
           rot(1060, 74, "e recomeça do zero", w=330, tam=21, cor=TINTA)]
    return slide("degrauabaixo", 360, p, rs, eyebrow="A ideia da aula", titulo="Uma piora é um degrau para baixo, não uma queda da escada.",
                 destaque="A piora vai acontecer; no tendão, quase sempre. A diferença está em a pessoa saber, antes, o que fazer quando ela chegar.", destaque_cor="tinta")


def registro_84():
    """8.4: uma página de caderno com as cinco colunas e a linha da ladeira marcada."""
    p = [svg_abre(1664, 360, "Uma página de caderno com cinco colunas: data, o que fez, carga ou volume, dor durante de 0 a 10, dor em 24 horas de 0 a 10. Três linhas ilustrativas: segunda, trote e caminhada, 20 minutos, dor 2 e 2; quarta, trote e caminhada, 25 minutos, dor 2 e 3; sexta, trote com ladeira, 25 minutos, dor 3 e 6. A linha de sexta está marcada: a ladeira entrou e a dor do dia seguinte subiu")]
    rs = []
    p.append(caixa(0, 0, 1300, 360, BORDA, CARTAO, esp=2, rx=16))
    p.append(f'<line x1="60" y1="0" x2="60" y2="360" stroke="{FOSF}" stroke-width="2" opacity="0.5"/>')
    cab = ["Data", "O que fez", "Carga ou volume", "Dor durante (0–10)", "Dor em 24 h (0–10)"]
    larg = [140, 340, 240, 260, 260]
    linhas = [["seg", "trote e caminhada", "20 min", "2", "2"], ["qua", "trote e caminhada", "25 min", "2", "3"], ["sex", "trote com ladeira", "25 min", "3", "6"]]
    xs = [70]
    for w in larg[:-1]:
        xs.append(xs[-1] + w)
    for x, w, t in zip(xs, larg, cab):
        rs.append(rot(x + 10, 30, t, w=w - 20, tam=20, cor=TINTA, peso=700, lh=1.15))
    for k in range(4):
        y = 100 + k * 80
        p.append(f'<line x1="20" y1="{y}" x2="1280" y2="{y}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<rect x="66" y="262" width="1220" height="76" rx="8" fill="{FOSF_T}"/>')
    for i, l in enumerate(linhas):
        y = 124 + i * 80
        for j, (x, w, t) in enumerate(zip(xs, larg, l)):
            forte = i == 2 and j in (1, 4)
            rs.append(rot(x + 10, y, t, w=w - 20, tam=24 if not forte else 26, cor=FOSF if forte else TINTA, peso=700 if forte else 400,
                          alinha="center" if j >= 3 else "left", serif=j >= 3))
    p.append(icone("t:notebook", 1340, 40, 64, TINTA))
    rs.append(rot(1340, 130, "na sexta entrou a ladeira, e a dor do dia seguinte subiu", w=324, tam=21, cor=FOSF, peso=700, lh=1.3))
    return slide("registro", 360, p, rs, eyebrow="A ferramenta que corrige os cinco", titulo="O registro de cinco colunas",
                 destaque="Sem registro, a consulta traz memória, puxada pelo último dia ruim. Com registro, a pessoa costuma achar o padrão antes de você.",
                 destaque_cor="tinta", fonte="Linhas ilustrativas")


def principios_84():
    """8.4: três cartões com mini desenhos: base larga, semana de pico, e a carga que vem de fora do treino."""
    p = [svg_abre(1664, 360, "Três cartões, cada um com um pequeno esquema. A base protege: uma faixa larga de carga crônica bem construída, que tolera mais. O pico importa: barras semanais com uma semana que dobrou, que pesa mais que a média do mês. Carga não é só treino: ao lado do treino entram sono, trabalho, estresse e doença")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("A base protege", "carga crônica bem construída tolera mais", OXID, OXID_T),
                                            ("O pico importa", "a semana em que dobrou pesa mais que a média do mês", GLIC, GLIC_T),
                                            ("Carga não é só treino", "sono, trabalho, estresse e doença entram na conta", TINTA, PAPEL)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 360, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 18, t, w=W - 48, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 270, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    # base
    p.append(f'<rect x="40" y="190" width="448" height="56" rx="8" fill="{OXID}"/>')
    for j, h in enumerate([30, 40, 34, 44, 38, 46]):
        p.append(f'<rect x="{60 + j * 72}" y="{186 - h}" width="48" height="{h}" rx="4" fill="{OXID}" opacity="0.5"/>')
    # pico
    x0 = W + 40
    for j, h in enumerate([50, 56, 52, 112, 54]):
        p.append(f'<rect x="{x0 + 50 + j * 88}" y="{246 - h}" width="60" height="{h}" rx="4" fill="{GLIC}" opacity="{1 if j == 3 else 0.45}"/>')
    p.append(f'<line x1="{x0 + 40}" y1="{246 - 65}" x2="{x0 + 490}" y2="{246 - 65}" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
    p.append(f'<line x1="{x0 + 40}" y1="246" x2="{x0 + 490}" y2="246" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(x0 + 30, 74, "média do mês", w=200, tam=17, cor=TINTA))
    # fora do treino
    x0 = 2 * (W + 40)
    for j, (ic, cor) in enumerate([("t:barbell", OXID), ("t:moon", AZUL), ("t:clipboard-list", MUDO), ("t:bolt", GLIC), ("t:mood-sick", FOSF)]):
        p.append(icone(ic, x0 + 30 + j * 96, 130, 56, cor))
    return slide("principios", 360, p, rs, eyebrow="O que sobrevive à crítica dos índices de carga", titulo="Três princípios para a reabilitação",
                 destaque="O índice agudo e crônico não serve como número de decisão; o módulo de preparação física volta a ele.", destaque_cor="tinta",
                 fonte="Br J Sports Med 2016 · consenso do COI 2016")


def cinco_84():
    """8.4: cinco linhas de erro para correção, apoiadas numa faixa do registro."""
    p = [svg_abre(1664, 470, "Cinco linhas, cada uma com um erro à esquerda e o que fazer no lugar à direita. Âncora errada: progredir sobre o que tolerou nas últimas duas semanas. Duas variáveis juntas: uma por vez, frequência, volume, densidade, intensidade. Degrau sem condição: estímulo, dose, critério de saída e de regressão. Parar tudo quando piora: regressão escrita antes, um degrau para baixo. Alta administrativa: sessões espaçadas, programa escrito, revisão marcada. Por baixo das cinco linhas, uma faixa: o registro")]
    rs = []
    mk = defs(OXID)
    p.append(mk)
    linhas = [("t:anchor", "Âncora errada", "progredir sobre o que tolerou nas últimas duas semanas"),
              ("t:arrows-exchange", "Duas variáveis juntas", "uma por vez: frequência, volume, densidade, intensidade"),
              ("t:stairs", "Degrau sem condição", "estímulo, dose, critério de saída e de regressão"),
              ("t:hand-stop", "Parar tudo quando piora", "regressão escrita antes: um degrau para baixo"),
              ("t:door-exit", "Alta administrativa", "sessões espaçadas, programa escrito, revisão marcada")]
    for k, (ic, e, c) in enumerate(linhas):
        y = k * 76
        p.append(caixa(0, y, 560, 64, FOSF, FOSF_T, esp=2, rx=12))
        p.append(icone(ic, 16, y + 12, 40, FOSF))
        rs.append(rot(70, y + 16, e, w=480, tam=23, cor=FOSF, peso=700))
        p.append(seta(574, y + 32, 636, y + 32, OXID, "m0", esp=3))
        p.append(caixa(650, y, 1014, 64, OXID, OXID_T, esp=2, rx=12))
        rs.append(rot(674, y + 17, c, w=970, tam=22, cor=TINTA))
    p.append(caixa(0, 394, 1664, 76, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:notebook", 24, 408, 48, PAPEL))
    rs.append(rot(90, 414, "Por baixo dos cinco, o registro", w=1500, tam=28, cor=PAPEL, peso=700, serif=True))
    return slide("cinco", 470, p, rs, eyebrow="Juntando", titulo="Cinco erros e o que fazer no lugar")

# ---------------------------------------------------------------- 8.5

def caso_85():
    """8.5: a sequência da lesão da jogadora e, ao lado, nove meses de plano no lugar de uma data."""
    p = [svg_abre(1664, 360, "À esquerda, a sequência da lesão de uma jogadora de handebol na casa dos vinte anos: aterrissagem depois do arremesso, joelho para dentro, estalo, inchaço em horas; ruptura do cruzado anterior e reconstrução decidida com o cirurgião. À direita, a pergunta quando eu volto, respondida com nove meses de plano em vez de uma data. O objeto é o percurso, não o desfecho"), defs(MUDO)]
    rs = []
    passos = [("h:running", "aterrissagem depois do arremesso"), ("t:arrow-down-right", "joelho para dentro"), ("t:bolt", "estalo"), ("t:droplet", "inchaço em horas")]
    for k, (ic, t) in enumerate(passos):
        y = k * 76
        p.append(caixa(0, y, 560, 64, FOSF, FOSF_T, esp=2, rx=12))
        p.append(icone(ic, 14, y + 10, 44, FOSF))
        rs.append(rot(72, y + 18, t, w=470, tam=22, cor=TINTA, peso=700))
    p.append(caixa(0, 304, 560, 56, TINTA, TINTA, esp=0, rx=12))
    rs.append(rot(20, 318, "ruptura do cruzado · reconstrução", w=520, tam=21, cor=PAPEL, peso=700))
    p.append(seta(580, 180, 650, 180, MUDO, "m0", esp=3))
    p.append(caixa(670, 0, 994, 360, OXID, CARTAO, esp=2, rx=16))
    p.append(icone("t:message-circle", 694, 22, 48, TINTA))
    rs.append(rot(756, 26, "“Quando eu volto?”", w=600, tam=28, cor=TINTA, peso=700, serif=True))
    for m in range(9):
        x = 700 + m * 104
        p.append(f'<rect x="{x}" y="120" width="92" height="110" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        p.append(f'<circle cx="{x + 46}" cy="200" r="7" fill="{OXID}"/>')
        rs.append(rot(x, 134, f"{m + 1}º", w=92, tam=22, cor=OXID, peso=700, alinha="center"))
    rs += [rot(700, 250, "um plano: fases, portas, responsáveis", w=940, tam=22, cor=TINTA, peso=700),
           rot(700, 296, "o objeto é o percurso, não o desfecho", w=940, tam=21, cor=MUDO)]
    return slide("caso", 360, p, rs, eyebrow="Caso ilustrativo · jogadora de handebol, na casa dos vinte", titulo="“Quando eu volto?” A resposta é um plano, não uma data.")


def expectativa_85():
    """8.5: três barras que encolhem, de algum esporte a esporte competitivo, sobre cem atletas."""
    p = [svg_abre(1664, 300, "Três barras horizontais sobre uma escala de cem por cento: 81% voltam a algum esporte, 65% ao nível de antes da lesão, 55% ao esporte competitivo")]
    rs = []
    X0, E = 420, 12
    for k, (v, t, cor) in enumerate([(81, "voltam a algum esporte", OXID), (65, "ao nível de antes da lesão", GLIC), (55, "ao esporte competitivo", FOSF)]):
        y = k * 96
        p.append(f'<rect x="{X0}" y="{y}" width="{100 * E}" height="76" rx="8" fill="{CINZA}" opacity="0.45"/>')
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E}" height="76" rx="8" fill="{cor}"/>')
        rs += [rot(0, y + 22, t, w=390, tam=23, cor=TINTA, peso=700, alinha="right"),
               rot(X0 + v * E - 170, y + 14, f"{v}%", w=150, tam=40, cor=PAPEL, peso=700, alinha="right", serif=True)]
    rs.append(rot(X0, 290 - 4, "100%", w=1200, tam=17, cor=MUDO, alinha="right"))
    return slide("expectativa", 300, p, rs, eyebrow="A conversa do primeiro mês", titulo="Voltar ao nível de antes não é automático",
                 destaque="Com os números de Delaware e Oslo do módulo de lesões: nove meses é o horizonte, e o critério decide se nove meses bastam.", destaque_cor="tinta",
                 fonte="Metanálise, Br J Sports Med 2014")


def antes_85():
    """8.5: duas barras de retorno, com e sem reabilitação antes da cirurgia, e os três alvos da chegada à cirurgia."""
    p = [svg_abre(1664, 380, "Duas barras de retorno ao esporte de antes, dois anos depois da cirurgia: 72% com reabilitação estendida antes da cirurgia, 63% sem ela. É comparação entre coortes, não ensaio sorteado. À direita, os três alvos para chegar à cirurgia: joelho calmo, extensão completa, quadríceps ativo")]
    rs = []
    B, E = 310, 3.0
    for k, (v, t, cor) in enumerate([(72, "com reabilitação antes", OXID), (63, "sem ela", GLIC)]):
        x = 40 + k * 340
        p.append(f'<rect x="{x}" y="{B - v * E:.0f}" width="280" height="{v * E:.0f}" rx="8" fill="{cor}"/>')
        rs += [rot(x, B - v * E - 56, f"{v}%", w=280, tam=44, cor=cor, peso=700, alinha="center", serif=True),
               rot(x, B + 10, t, w=280, tam=20, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="20" y1="{B}" x2="700" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(20, 0, "voltaram ao esporte de antes, dois anos depois", w=680, tam=19, cor=MUDO, peso=700))
    rs.append(rot(20, 352, "comparação entre coortes, não ensaio sorteado", w=680, tam=18, cor=MUDO))
    p.append(caixa(780, 0, 884, 380, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(808, 20, "Chegar à cirurgia com", w=820, tam=26, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:temperature", "joelho calmo, sem derrame importante"), ("t:ruler-measure", "extensão completa"), ("t:bolt", "quadríceps contraindo bem")]):
        y = 96 + j * 84
        p.append(icone(ic, 808, y, 48, OXID))
        rs.append(rot(874, y + 10, t, w=760, tam=24, cor=TINTA, peso=700))
    return slide("antes", 380, p, rs, eyebrow="Quando há tempo antes da cirurgia", titulo="A reabilitação começa antes dela",
                 fonte="192 contra 1.995 pacientes · Am J Sports Med 2016")


def semanas_85():
    """8.5: três prioridades numeradas e, embaixo, a porta da fase no lugar da semana seis."""
    p = [svg_abre(1664, 400, "Três prioridades numeradas, nesta ordem. Um: extensão completa; perdida agora, é difícil de recuperar e muda a marcha por meses. Dois: derrame sob controle; o joelho cheio desliga o quadríceps, medido toda sessão. Três: quadríceps ligado; contração voluntária e perna estendida sem o joelho dobrar. Embaixo, a porta da fase: extensão completa, derrame mínimo e estável, marcha sem muletas e sem mancar. Não é semana seis"), defs(MUDO)]
    rs = []
    W = 520
    cards = [("Extensão completa", "perdida agora, é difícil de recuperar e muda a marcha por meses", FOSF, FOSF_T, "t:ruler-measure"),
             ("Derrame sob controle", "o joelho cheio desliga o quadríceps; medido toda sessão", GLIC, GLIC_T, "t:droplet"),
             ("Quadríceps ligado", "contração voluntária e perna estendida sem o joelho dobrar", OXID, OXID_T, "t:bolt")]
    for k, (t, d, cor, fundo, ic) in enumerate(cards):
        x = k * (W + 52)
        p.append(caixa(x, 0, W, 230, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="{x + 44}" cy="46" r="26" fill="{cor}"/>')
        rs.append(rot(x + 18, 30, str(k + 1), w=52, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(icone(ic, x + W - 64, 22, 44, cor))
        rs += [rot(x + 84, 30, t, w=W - 160, tam=25, cor=cor, peso=700, serif=True), rot(x + 24, 100, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
        if k < 2:
            p.append(seta(x + W + 6, 115, x + W + 46, 115, MUDO, "m0", esp=3))
    p.append(caixa(0, 260, 1664, 140, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:door", 24, 282, 48, PAPEL))
    rs += [rot(88, 288, "A porta da fase", w=500, tam=26, cor=PAPEL, peso=700, serif=True),
           rot(88, 334, "extensão completa · derrame mínimo e estável · marcha sem muletas e sem mancar", w=1240, tam=22, cor=PAPEL)]
    p.append(icone("t:calendar", 1360, 290, 56, MUDO))
    p.append(f'<line x1="1350" y1="352" x2="1426" y2="280" stroke="{FOSF}" stroke-width="5"/>')
    rs.append(rot(1440, 300, "não é “semana seis”", w=210, tam=22, cor=PAPEL, peso=700, lh=1.2))
    return slide("semanas", 400, p, rs, eyebrow="Primeiras semanas depois da cirurgia", titulo="Três prioridades, nesta ordem")


def forca_85():
    """8.5: cadeia aberta igual a fechada na frouxidão; eletroestimulação somada ao treino."""
    p = [svg_abre(1664, 340, "Dois painéis. À esquerda, cadeira extensora pode? Cadeia aberta e cadeia fechada, com um sinal de igual: sem diferença na frouxidão do joelho; entra, com amplitude e carga combinadas. À direita, eletroestimulação ajuda? Uma barra de força do quadríceps com a fisioterapia, e um pedaço a mais somado pela eletroestimulação: soma ao treino, não o substitui")]
    rs = []
    p.append(caixa(0, 0, 800, 340, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "Cadeira extensora pode?", w=760, tam=27, cor=OXID, peso=700, serif=True))
    for k, (t, d) in enumerate([("cadeia aberta", "cadeira extensora, pé livre"), ("cadeia fechada", "agachamento, pé apoiado")]):
        x = 30 + k * 420
        p.append(caixa(x, 80, 320, 120, OXID, OXID_T, esp=2, rx=14))
        rs += [rot(x + 16, 100, t, w=288, tam=24, cor=OXID, peso=700, alinha="center"), rot(x + 16, 140, d, w=288, tam=19, cor=TINTA, alinha="center")]
    rs.append(rot(350, 112, "=", w=100, tam=52, cor=TINTA, peso=700, alinha="center", serif=True))
    rs += [rot(30, 222, "sem diferença na frouxidão do joelho", w=740, tam=23, cor=TINTA, peso=700),
           rot(30, 268, "entra, com amplitude e carga combinadas", w=740, tam=21, cor=MUDO)]
    p.append(caixa(864, 0, 800, 340, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(888, 18, "Eletroestimulação ajuda?", w=760, tam=27, cor=OXID, peso=700, serif=True))
    p.append(f'<rect x="900" y="100" width="480" height="80" rx="8" fill="{OXID}"/>')
    p.append(f'<rect x="1384" y="100" width="150" height="80" rx="8" fill="{GLIC}"/>')
    rs += [rot(900, 122, "fisioterapia e treino", w=480, tam=22, cor=PAPEL, peso=700, alinha="center"),
           rot(1384, 114, "+ eletro", w=150, tam=22, cor=PAPEL, peso=700, alinha="center"),
           rot(900, 194, "força do quadríceps · esquema", w=640, tam=18, cor=MUDO),
           rot(900, 238, "soma ao treino, não o substitui", w=740, tam=23, cor=TINTA, peso=700)]
    return slide("forca", 340, p, rs, eyebrow="A fase mais longa: o quadríceps é o eixo", titulo="Duas discussões antigas",
                 destaque="Força de verdade pede carga alta, por meses. Faixa elástica para sempre não reconstrói um quadríceps.", destaque_cor="tinta",
                 fonte="J Orthop Sports Phys Ther 2018 · Knee Surg Sports Traumatol Arthrosc 2018")


def corrida_85():
    """8.5: o relógio de doze semanas e menos de um em cinco estudos com critério; ao lado, a porta da jogadora."""
    p = [svg_abre(1664, 380, "À esquerda, um relógio: mediana de 12 semanas para liberar a corrida em 201 estudos. Embaixo, cinco casas, com menos de uma preenchida: menos de 1 em 5 usou algum critério além do tempo. À direita, a porta da jogadora: sem derrame, amplitude completa, força do quadríceps combinada com o outro lado, saltitar e aterrissar sem dor e sem o joelho ir para dentro")]
    rs = []
    p.append(caixa(0, 0, 760, 380, GLIC, CARTAO, esp=2, rx=16))
    p.append(icone("t:clock", 30, 30, 96, GLIC))
    rs += [rot(150, 30, "12 semanas", w=580, tam=48, cor=GLIC, peso=700, serif=True),
           rot(150, 96, "mediana de liberação da corrida em 201 estudos", w=580, tam=20, cor=TINTA, lh=1.25)]
    for c in range(5):
        x = 30 + c * 140
        p.append(f'<rect x="{x}" y="200" width="124" height="70" rx="10" fill="{CINZA}" opacity="0.5"/>')
    p.append(f'<rect x="30" y="200" width="100" height="70" rx="10" fill="{FOSF}"/>')
    rs += [rot(30, 286, "menos de 1 em 5 usou algum critério além do tempo", w=700, tam=21, cor=FOSF, peso=700, lh=1.25)]
    p.append(caixa(820, 0, 844, 380, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:door", 846, 22, 48, OXID))
    rs.append(rot(908, 28, "A porta dela", w=700, tam=28, cor=OXID, peso=700, serif=True))
    for j, t in enumerate(["sem derrame", "amplitude completa", "força do quadríceps combinada com o outro lado", "saltitar e aterrissar sem dor e sem o joelho ir para dentro"]):
        y = 98 + j * 68
        p.append(icone("t:check", 846, y, 36, OXID))
        rs.append(rot(896, y + 4, t, w=740, tam=22, cor=TINTA, peso=700 if j < 2 else 400, lh=1.2))
    return slide("corrida", 380, p, rs, eyebrow="A primeira porta que a atleta sente como vitória", titulo="Voltar a correr: o tempo quase sempre sozinho",
                 fonte="Revisão de mapeamento, Br J Sports Med 2018")


def relogios_85():
    """8.5: duas trilhas de nove meses, a do enxerto lenta e regular, a do quadríceps imprevisível, em esquema."""
    p = [svg_abre(1664, 380, "Em esquema, duas trilhas de zero a nove meses. O enxerto amadurece devagar e de forma regular: é ele que marca o horizonte de nove meses. O quadríceps sobe e empaca de forma imprevisível. No sexto mês a atleta pode se sentir pronta com o quadríceps fraco; no sétimo, ter um quadríceps excelente com o enxerto no meio do caminho. A decisão é tempo e critério")]
    rs = []
    X0, W, B = 300, 1300, 320
    for m in range(10):
        x = X0 + m * W / 9
        p.append(f'<line x1="{x:.0f}" y1="20" x2="{x:.0f}" y2="{B}" stroke="{BORDA}" stroke-width="2"/>')
        if m % 3 == 0:
            rs.append(rot(x - 50, B + 8, f"{m} meses" if m else "0", w=100, tam=18, cor=MUDO, alinha="center"))
    p.append(f'<line x1="{X0}" y1="{B}" x2="{X0 + W}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {X0} 290 C {X0 + 500} 280, {X0 + 900} 200, {X0 + W} 60" fill="none" stroke="{AZUL}" stroke-width="6"/>')
    p.append(f'<path d="M {X0} 300 L {X0 + 150} 260 L {X0 + 260} 270 L {X0 + 420} 190 L {X0 + 560} 200 L {X0 + 700} 150 L {X0 + 870} 90 L {X0 + 1000} 100 L {X0 + W} 70" fill="none" stroke="{GLIC}" stroke-width="6" stroke-linejoin="round"/>')
    rs += [rot(0, 216, "enxerto", w=280, tam=26, cor=AZUL, peso=700, alinha="right", serif=True), rot(0, 250, "devagar e regular", w=280, tam=19, cor=TINTA, alinha="right"),
           rot(0, 120, "quadríceps", w=280, tam=26, cor=GLIC, peso=700, alinha="right", serif=True), rot(0, 154, "sobe e empaca", w=280, tam=19, cor=TINTA, alinha="right")]
    rs.append(rot(X0, 0, "esquema", w=200, tam=17, cor=MUDO))
    p.append(icone("t:door", X0 + W - 16, 2, 40, TINTA))
    rs.append(rot(X0 + W - 260, 350, "a decisão: tempo e critério", w=300, tam=21, cor=TINTA, peso=700, alinha="right"))
    return slide("relogios", 380, p, rs, eyebrow="A ideia do caso", titulo="O relógio do enxerto e o relógio do quadríceps não andam juntos.",
                 destaque="Pronta no sexto mês com o quadríceps fraco; quadríceps excelente no sétimo com o enxerto no meio do caminho.", destaque_cor="tinta")


def ultima_85():
    """8.5: a porta do nono mês com três placas, ligada ao primeiro dia por uma linha do tempo."""
    p = [svg_abre(1664, 380, "Uma linha do tempo do primeiro dia até perto do nono mês, onde está a última porta, com três placas. Testes de retorno: força, saltos e a armadilha do índice de simetria. Prontidão psicológica: o medo de nova lesão não aparece no dinamômetro. Decisão compartilhada: avaliar o risco é uma coisa; aceitá-lo é outra. A porta está no plano desde o primeiro dia, e cada parte ganha uma conversa adiante")]
    rs = []
    W = 520
    for k, (ic, t, d, cor, fundo) in enumerate([("t:ruler-measure", "Testes de retorno", "força, saltos e a armadilha do índice de simetria", OXID, OXID_T),
                                                ("t:zoom-question", "Prontidão psicológica", "o medo de nova lesão não aparece no dinamômetro", GLIC, GLIC_T),
                                                ("t:users-group", "Decisão compartilhada", "avaliar o risco é uma coisa; aceitá-lo é outra", TINTA, PAPEL)]):
        x = k * (W + 52)
        p.append(caixa(x, 0, W, 230, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 48, cor))
        rs += [rot(x + 88, 32, t, w=W - 110, tam=25, cor=cor, peso=700, serif=True), rot(x + 24, 100, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    B = 300
    p.append(f'<line x1="20" y1="{B}" x2="1560" y2="{B}" stroke="{MUDO}" stroke-width="4"/>')
    p.append(f'<circle cx="20" cy="{B}" r="12" fill="{OXID}"/>')
    p.append(f'<rect x="1560" y="{B - 46}" width="64" height="92" rx="8" fill="{TINTA}"/>')
    rs += [rot(0, B + 24, "primeiro dia: a porta já está no plano", w=700, tam=21, cor=OXID, peso=700),
           rot(1000, B + 54, "perto do nono mês", w=620, tam=21, cor=TINTA, peso=700, alinha="right"),
           rot(560, B - 44, "ninguém é surpreendido no oitavo mês", w=600, tam=19, cor=MUDO, alinha="center")]
    return slide("ultima", 380, p, rs, eyebrow="Perto do nono mês", titulo="A última porta tem três partes",
                 destaque="Cada parte ganha uma conversa própria adiante.", destaque_cor="tinta")


def quem_85():
    """8.5: cinco faixas de responsáveis ao longo dos nove meses, em esquema."""
    p = [svg_abre(1664, 420, "Em esquema, cinco faixas ao longo dos nove meses. Cirurgião: técnica, enxerto e restrições iniciais, forte no começo, depois nas portas em que o tecido é o limite. Fisioterapia: do começo ao fim, mede derrame, amplitude e força e escreve as portas. Preparação física: da corrida em diante, fase de campo, gesto e condicionamento. Psicologia e nutrição: a matéria-prima de meses de força o tempo todo, e o medo perto do retorno. Treinador, atleta e família: a expectativa honesta desde o começo e a porta de cada mês")]
    rs = []
    X0, W = 430, 1234
    def mx(m):
        return X0 + m * W / 9.5
    for m in range(0, 10, 3):
        p.append(f'<line x1="{mx(m):.0f}" y1="0" x2="{mx(m):.0f}" y2="380" stroke="{BORDA}" stroke-width="2"/>')
        rs.append(rot(mx(m) - 50, 388, f"{m} meses" if m else "cirurgia", w=100, tam=18, cor=MUDO, alinha="center"))
    faixas = [("Cirurgião", [(-0.4, 1.5, .3), (3, 3.4, .3), (6, 6.4, .3), (8.7, 9.2, .3)], "técnica, enxerto, restrições; portas do tecido", AZUL, -0.4, TINTA),
              ("Fisioterapia", [(-0.4, 9.4, 1)], "conduz do começo ao fim; mede e escreve as portas", OXID, -0.4, PAPEL),
              ("Preparação física", [(3, 9.4, 1)], "corrida, fase de campo, gesto e condicionamento", GLIC, 3, PAPEL),
              ("Psicologia e nutrição", [(-0.4, 9.4, .3), (7, 9.4, .8)], "matéria-prima de meses; o medo perto do retorno", FOSF, -0.4, TINTA),
              ("Treinador, atleta, família", [(-0.4, 9.4, .3)], "expectativa honesta desde o começo; a porta de cada mês", TINTA, -0.4, TINTA)]
    for k, (t, segs, d, cor, x0, ct) in enumerate(faixas):
        y = 6 + k * 76
        rs.append(rot(0, y + 18, t, w=360, tam=21, cor=cor, peso=700, alinha="right", lh=1.15))
        for a, b, op in segs:
            p.append(f'<rect x="{mx(a):.0f}" y="{y}" width="{mx(b) - mx(a):.0f}" height="60" rx="10" fill="{cor}" opacity="{op}"/>')
        rs.append(rot(mx(x0) + 16, y + 18, d, w=mx(9.4) - mx(x0) - 32, tam=19, cor=ct, peso=700))
    rs.append(rot(0, 388, "esquema", w=300, tam=17, cor=MUDO, alinha="right"))
    return slide("quem", 420, p, rs, eyebrow="Nove meses, muitas mãos", titulo="Quem faz o quê")

# ---------------------------------------------------------------- 8.6

def macas_86():
    """8.6: as duas macas lado a lado, o meia que quer jogar e o lateral que vai e volta."""
    p = [svg_abre(1664, 360, "Duas macas lado a lado. Na primeira, um meia sem dor há uma semana depois de lesão de posterior de coxa num sprint, querendo jogar domingo. Na segunda, um lateral com dor na virilha há dois meses, num ciclo: treina, dói, para, melhora, volta. A maior parte dos dados é do futebol, e isso limita")]
    rs = []
    p.append(caixa(0, 0, 800, 300, AZUL, CARTAO, esp=2, rx=16))
    p.append(icone("h:running", 24, 24, 64, AZUL))
    rs += [rot(104, 30, "Primeira maca · o meia", w=670, tam=27, cor=AZUL, peso=700, serif=True),
           rot(104, 74, "posterior de coxa, num sprint", w=670, tam=21, cor=TINTA)]
    p.append(f'<rect x="24" y="150" width="520" height="110" rx="12" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(icone("t:check", 44, 180, 48, OXID))
    rs.append(rot(108, 178, "sem dor há uma semana", w=420, tam=24, cor=OXID, peso=700))
    p.append(icone("t:calendar", 580, 150, 56, FOSF))
    rs.append(rot(560, 214, "quer jogar domingo", w=220, tam=21, cor=FOSF, peso=700, alinha="center"))
    p.append(caixa(864, 0, 800, 300, GLIC, CARTAO, esp=2, rx=16))
    p.append(icone("h:pain-managment", 888, 24, 64, GLIC))
    rs += [rot(968, 30, "Segunda maca · o lateral", w=670, tam=27, cor=GLIC, peso=700, serif=True),
           rot(968, 74, "dor na virilha há dois meses", w=670, tam=21, cor=TINTA)]
    cx, cy, r = 1264, 205, 70
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GLIC}" stroke-width="4"{TRACO}/>')
    p.append(icone("t:refresh", cx - 24, cy - 24, 48, GLIC))
    for t, x, y, al in [("treina, dói", cx - 330, cy - 50, "right"), ("para", cx - 330, cy + 20, "right"), ("melhora", cx + 90, cy - 50, "left"), ("volta, dói de novo", cx + 90, cy + 20, "left")]:
        rs.append(rot(x, y, t, w=240, tam=21, cor=TINTA, peso=700, alinha=al))
    rs.append(rot(0, 322, "a maior parte dos dados é do futebol, e isso limita", w=1664, tam=20, cor=MUDO, alinha="center"))
    return slide("macas", 360, p, rs, eyebrow="Duas macas no departamento médico de um clube de futebol",
                 titulo="Parar de tratar quando a dor some, ou tratar sem saber o que se está tratando.")


def roteiro_86():
    """8.6: dois roteiros de três passos numerados, posterior da coxa e virilha."""
    p = [svg_abre(1664, 340, "Dois roteiros de três passos. Posterior da coxa, fase final: um, o que já está resolvido; dois, expor à velocidade antes do jogo; três, critérios de retorno. Virilha: um, dar nome, porque pubalgia não é diagnóstico; dois, medir; três, tratar com carga"), defs(MUDO)]
    rs = []
    for k, (t, itens, cor, fundo, ic) in enumerate([("Posterior da coxa, fase final", ["o que já está resolvido", "expor à velocidade antes do jogo", "critérios de retorno"], AZUL, AZUL_T, "h:running"),
                                                    ("Virilha", ["dar nome: “pubalgia” não é diagnóstico", "medir", "tratar com carga"], GLIC, GLIC_T, "t:target")]):
        y = k * 180
        p.append(icone(ic, 0, y + 10, 48, cor))
        rs.append(rot(60, y + 16, t, w=700, tam=26, cor=cor, peso=700, serif=True))
        for j, it in enumerate(itens):
            x = j * 560
            p.append(caixa(x, y + 70, 500, 90, cor, fundo, esp=2, rx=14))
            p.append(f'<circle cx="{x + 42}" cy="{y + 115}" r="22" fill="{cor}"/>')
            rs += [rot(x + 20, y + 102, str(j + 1), w=44, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True),
                   rot(x + 80, y + 100 if len(it) < 34 else y + 90, it, w=400, tam=22, cor=TINTA, peso=700, lh=1.2)]
            if j < 2:
                p.append(seta(x + 508, y + 115, x + 552, y + 115, MUDO, "m0", esp=3))
    return slide("roteiro", 340, p, rs, eyebrow="O roteiro", titulo="Dois roteiros, três passos cada")


def resolvido_86():
    """8.6: duas caixas marcadas como feitas e a terceira em aberto, tracejada."""
    p = [svg_abre(1664, 300, "Três caixas. Duas marcadas como feitas: exercício em alongamento, o músculo trabalhando alongado encurta o retorno; desconforto tolerável, não atrasa a liberação e preserva força e comprimento de fibra. A terceira, tracejada, em aberto: do exercício na maca ao sprint do jogo, e os critérios da volta")]
    rs = []
    W = 520
    for k, (t, d, feito) in enumerate([("Exercício em alongamento", "o músculo trabalhando alongado encurta o retorno", True),
                                       ("Desconforto tolerável", "não atrasa a liberação; preserva força e comprimento de fibra", True),
                                       ("Em aberto", "do exercício na maca ao sprint do jogo, e os critérios da volta", False)]):
        x = k * (W + 52)
        cor = OXID if feito else GLIC
        if feito:
            p.append(caixa(x, 0, W, 300, cor, OXID_T, esp=2, rx=16))
            p.append(f'<circle cx="{x + W - 52}" cy="52" r="30" fill="{OXID}"/>')
            p.append(icone("t:check", x + W - 72, 32, 40, PAPEL))
        else:
            p.append(f'<rect x="{x + 2}" y="2" width="{W - 4}" height="296" rx="16" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"{TRACO}/>')
            p.append(icone("t:question-mark", x + W - 72, 32, 40, GLIC))
        rs += [rot(x + 24, 30, t, w=W - 120, tam=26, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 24, 130, d, w=W - 48, tam=22, cor=TINTA, lh=1.3)]
    rs += [rot(24, 254, "feito no módulo de lesões", w=W - 48, tam=18, cor=MUDO), rot(2 * (W + 52) + 24, 254, "o assunto desta conversa", w=W - 48, tam=18, cor=GLIC, peso=700)]
    return slide("resolvido", 300, p, rs, eyebrow="Posterior da coxa · passo um", titulo="O que o módulo de lesões já resolveu",
                 fonte="Ensaio australiano, J Orthop Sports Phys Ther 2020")


def criterios_86():
    """8.6: três critérios de dor e função marcados, e a ressonância riscada."""
    p = [svg_abre(1664, 300, "Quatro cartões de critério de retorno. Marcados: sem dor à palpação do músculo; sem dor nos testes de força e flexibilidade; sem dor durante e depois do desempenho funcional, corrida e gesto incluídos. Riscado: a ressonância, porque a imagem inicial não prediz a nova lesão")]
    rs = []
    W = 386
    for k, (ic, t, d, fora) in enumerate([("t:hand-stop", "Palpação", "sem dor ao apertar o músculo", False), ("t:barbell", "Força e flexibilidade", "sem dor nos testes", False),
                                          ("t:run", "Desempenho funcional", "sem dor durante e depois, corrida e gesto incluídos", False),
                                          ("t:eye-off", "Ressonância", "fora: a imagem inicial não prediz a nova lesão", True)]):
        x = k * (W + 40)
        cor, fundo = (FOSF, FOSF_T) if fora else (OXID, OXID_T)
        p.append(caixa(x, 0, W, 300, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 52, cor))
        p.append(icone("t:x" if fora else "t:check", x + W - 64, 28, 40, cor))
        rs += [rot(x + 24, 100, t, w=W - 48, tam=25, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 24, 176, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    return slide("criterios", 300, p, rs, eyebrow="Posterior da coxa · passo três", titulo="58 especialistas, 28 centros da FIFA",
                 destaque="Sem consenso sobre força excêntrica como critério obrigatório. Decisão compartilhada, com o jogador.", destaque_cor="tinta",
                 fonte="Consenso Delphi, Br J Sports Med 2017")


def sprint_86():
    """8.6: sem dor é a primeira porta; as três perguntas da segunda-feira vêm antes do jogo."""
    p = [svg_abre(1664, 340, "À esquerda, sem dor há uma semana: necessário, não suficiente. Uma seta leva a três perguntas da equipe na segunda-feira: quantas vezes ele já correu perto da velocidade máxima, em quantas sessões, e como estava o músculo no dia seguinte. Só depois, o jogo"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 40, 380, 260, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:check", 24, 64, 48, OXID))
    rs += [rot(24, 130, "sem dor há uma semana", w=332, tam=25, cor=OXID, peso=700, serif=True, lh=1.15),
           rot(24, 210, "necessário, não suficiente", w=332, tam=21, cor=TINTA, peso=700)]
    p.append(seta(392, 170, 450, 170, MUDO, "m0", esp=3))
    for j, (ic, t) in enumerate([("t:stopwatch", "quantas vezes já correu perto do máximo?"), ("t:calendar", "em quantas sessões?"), ("t:clock", "como estava o músculo no dia seguinte?")]):
        y = j * 116
        p.append(caixa(464, y, 860, 100, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 488, y + 26, 48, TINTA))
        rs.append(rot(556, y + 34, t, w=750, tam=23, cor=TINTA, peso=700))
    p.append(seta(1336, 170, 1394, 170, MUDO, "m0", esp=3))
    p.append(caixa(1408, 90, 256, 160, MUDO, PAPEL, esp=2, rx=16))
    p.append(icone("t:soccer-field", 1504, 110, 64, MUDO))
    rs.append(rot(1408, 190, "só depois, o jogo", w=256, tam=21, cor=MUDO, peso=700, alinha="center"))
    return slide("sprint", 340, p, rs, eyebrow="A regra da primeira maca", titulo="O primeiro sprint máximo não pode ser no jogo.")


def doha_86():
    """8.6: a árvore de Doha em três grupos e, embaixo, o nome que aponta o tratamento contra o que não aponta nada."""
    p = [svg_abre(1664, 420, "Uma árvore. No topo, dor na virilha do atleta, nomeada pela história e pelo exame. Três ramos: entidades clínicas, com dor relacionada ao adutor, ao iliopsoas, à região inguinal e ao púbis; dor relacionada ao quadril, em que a articulação é a fonte; outras causas, inclusive o que não é musculoesquelético. Embaixo, pubalgia não aponta nada; dor relacionada ao adutor aponta o tratamento"), defs(MUDO)]
    rs = []
    p.append(caixa(532, 0, 600, 64, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(532, 16, "dor na virilha · história e exame", w=600, tam=23, cor=PAPEL, peso=700, alinha="center"))
    ramos = [(0, 760, "Entidades clínicas", OXID, OXID_T), (800, 420, "Relacionada ao quadril", AZUL, AZUL_T), (1260, 404, "Outras causas", MUDO, PAPEL)]
    for x, w, t, cor, fundo in ramos:
        p.append(f'<path d="M 832 64 L 832 84 L {x + w / 2:.0f} 84 L {x + w / 2:.0f} 104" fill="none" stroke="{MUDO}" stroke-width="3"/>')
        p.append(caixa(x, 110, w, 170, cor, fundo, esp=2, rx=14))
        rs.append(rot(x + 20, 126, t, w=w - 40, tam=24, cor=cor, peso=700, serif=True))
    for j, t in enumerate(["adutor", "iliopsoas", "inguinal", "púbis"]):
        x = 20 + j * 182
        p.append(f'<rect x="{x}" y="186" width="166" height="60" rx="30" fill="{CARTAO}" stroke="{OXID}" stroke-width="{4 if j == 0 else 2}"/>')
        rs.append(rot(x, 202, t, w=166, tam=21, cor=OXID, peso=700, alinha="center"))
    rs += [rot(820, 180, "a articulação do quadril é a fonte", w=380, tam=21, cor=TINTA, lh=1.25),
           rot(1280, 180, "inclusive o que não é musculoesquelético", w=364, tam=21, cor=TINTA, lh=1.25)]
    p.append(caixa(0, 310, 800, 110, FOSF, FOSF_T, esp=2, rx=14))
    p.append(icone("t:x", 24, 340, 48, FOSF))
    rs += [rot(90, 330, "“Pubalgia”", w=680, tam=25, cor=FOSF, peso=700, serif=True), rot(90, 370, "não aponta nada", w=680, tam=21, cor=TINTA)]
    p.append(caixa(864, 310, 800, 110, OXID, OXID_T, esp=2, rx=14))
    p.append(icone("t:target", 888, 340, 48, OXID))
    rs += [rot(954, 330, "“Dor relacionada ao adutor”", w=690, tam=25, cor=OXID, peso=700, serif=True), rot(954, 370, "aponta o tratamento: a musculatura adutora e a carga", w=690, tam=21, cor=TINTA)]
    return slide("doha", 420, p, rs, eyebrow="Virilha · passo um", titulo="Dar nome: a classificação de Doha",
                 fonte="24 especialistas de 14 países · Br J Sports Med 2015")


def medir_86():
    """8.6: o aperto de adução entre os joelhos e o questionário de seis domínios."""
    p = [svg_abre(1664, 360, "Dois instrumentos. À esquerda, o aperto de adução: dois joelhos apertando um dinamômetro ou um esfigmomanômetro dobrado, para medir força e dor no esforço, sempre na mesma posição. À direita, o questionário de quadril e virilha: 37 perguntas em seis domínios, dor, sintomas, atividades do dia a dia, função no esporte, participação e qualidade de vida; a perspectiva do atleta")]
    rs = []
    p.append(caixa(0, 0, 800, 360, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "Aperto de adução", w=760, tam=27, cor=OXID, peso=700, serif=True))
    p.append(f'<ellipse cx="190" cy="170" rx="90" ry="62" fill="{CINZA}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<ellipse cx="510" cy="170" rx="90" ry="62" fill="{CINZA}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<rect x="290" y="135" width="120" height="70" rx="14" fill="{OXID}"/>')
    p.append(f'<path d="M 70 170 L 96 170 M 84 158 L 98 170 L 84 182" stroke="{OXID}" stroke-width="5" fill="none"/>')
    p.append(f'<path d="M 630 170 L 604 170 M 616 158 L 602 170 L 616 182" stroke="{OXID}" stroke-width="5" fill="none"/>')
    rs += [rot(290, 156, "força", w=120, tam=21, cor=PAPEL, peso=700, alinha="center"),
           rot(24, 256, "dinamômetro ou esfigmomanômetro dobrado", w=760, tam=21, cor=TINTA, peso=700),
           rot(24, 292, "força e dor no esforço · sempre na mesma posição", w=760, tam=21, cor=TINTA)]
    p.append(caixa(864, 0, 800, 360, GLIC, CARTAO, esp=2, rx=16))
    p.append(icone("t:clipboard-list", 888, 18, 40, GLIC))
    rs.append(rot(940, 18, "Questionário de quadril e virilha", w=700, tam=27, cor=GLIC, peso=700, serif=True))
    rs.append(rot(888, 72, "37 perguntas, seis domínios", w=740, tam=21, cor=TINTA, peso=700))
    for j, t in enumerate(["dor", "sintomas", "dia a dia", "esporte", "participação", "qualidade de vida"]):
        x = 888 + (j % 3) * 250
        y = 120 + (j // 3) * 84
        p.append(f'<rect x="{x}" y="{y}" width="230" height="68" rx="10" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
        rs.append(rot(x, y + 20, t, w=230, tam=21, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(888, 304, "a perspectiva do atleta", w=740, tam=21, cor=GLIC, peso=700))
    return slide("medir", 360, p, rs, eyebrow="Virilha · passo dois", titulo="Medir, porque a sensação engana",
                 destaque="“Está melhorando?” deixa de depender de como foi o último treino.", destaque_cor="tinta", fonte="Copenhague, Br J Sports Med 2011")


def holmich_86():
    """8.6: 23 figuras de volta sem dor com treino ativo, 4 com fisioterapia passiva."""
    p = [svg_abre(1664, 320, "Duas fileiras de figuras. Com treino ativo de força e coordenação da pelve: 23 atletas de volta ao esporte sem dor na virilha. Com fisioterapia sem treino ativo, com recursos passivos: 4")]
    rs = []
    for k, (n, t, cor) in enumerate([(23, "treino ativo de força e coordenação da pelve", OXID), (4, "fisioterapia sem treino ativo, recursos passivos", FOSF)]):
        y = k * 160
        rs += [rot(0, y + 10, str(n), w=160, tam=72, cor=cor, peso=700, serif=True, alinha="center"), rot(190, y + 108, t, w=1400, tam=21, cor=TINTA, peso=700)]
        for i in range(n):
            x = 190 + (i % 23) * 64
            p.append(icone("h:person", x, y + 8, 56, cor))
    return slide("holmich", 320, p, rs, eyebrow="Virilha · passo três", titulo="Tratar com carga: o ensaio de 1999",
                 destaque="Dor relacionada ao adutor de longa duração: o que muda o desfecho é a carga, não o recurso passivo.", destaque_cor="tinta",
                 fonte="Ensaio dinamarquês sorteado, Lancet 1999")


def manter_86():
    """8.6: o calendário da dose, três vezes na pré-temporada e uma na temporada, e as duas barras de prevalência."""
    p = [svg_abre(1664, 360, "À esquerda, o calendário da dose: um exercício de adutores, três vezes por semana na pré-temporada e uma vez por semana na temporada. À direita, em 35 equipes semiprofissionais sorteadas, a prevalência de problemas na virilha: 13,5% com o programa, 21,3% sem. Risco de relatar problema na virilha 41% menor")]
    rs = []
    p.append(caixa(0, 0, 760, 360, OXID, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 18, "Um exercício de adutores", w=720, tam=26, cor=OXID, peso=700, serif=True))
    for j, (t, n, sem) in enumerate([("pré-temporada", 3, 4), ("temporada", 1, 6)]):
        y = 90 + j * 130
        rs.append(rot(24, y, f"{t} · {n}× por semana", w=720, tam=21, cor=TINTA, peso=700))
        for s in range(sem):
            for d in range(7):
                x = 24 + s * 118 + d * 15
                marca = (n == 3 and d in (0, 2, 4)) or (n == 1 and d == 2)
                p.append(f'<rect x="{x}" y="{y + 38}" width="12" height="44" rx="3" fill="{OXID if marca else CINZA}" opacity="{1 if marca else 0.5}"/>')
    rs.append(rot(24, 320, "a dose que sobrevive ao calendário", w=720, tam=20, cor=MUDO))
    B, E = 280, 9
    for k, (v, t, cor) in enumerate([(13.5, "com o programa", OXID), (21.3, "sem", GLIC)]):
        x = 860 + k * 260
        p.append(f'<rect x="{x}" y="{B - v * E:.0f}" width="200" height="{v * E:.0f}" rx="8" fill="{cor}"/>')
        rs += [rot(x - 20, B - v * E - 52, f"{v:.1f}%".replace(".", ","), w=240, tam=38, cor=cor, peso=700, alinha="center", serif=True),
               rot(x - 20, B + 10, t, w=240, tam=20, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="840" y1="{B}" x2="1360" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(840, 320, "prevalência de problemas na virilha · 35 equipes", w=560, tam=18, cor=MUDO))
    p.append(caixa(1400, 60, 264, 200, OXID, OXID, esp=0, rx=16))
    rs += [rot(1400, 90, "−41%", w=264, tam=52, cor=PAPEL, peso=700, alinha="center", serif=True), rot(1416, 170, "risco de relatar problema na virilha", w=232, tam=19, cor=PAPEL, alinha="center", lh=1.2)]
    return slide("manter", 360, p, rs, eyebrow="Depois que ele voltar", titulo="Um exercício de adutores, uma vez por semana",
                 fonte="Futebol masculino norueguês, 35 equipes semiprofissionais sorteadas · Br J Sports Med 2019")


def armadilhas_86():
    """8.6: quatro armadilhas, cada uma com o desenho do erro."""
    p = [svg_abre(1664, 320, "Quatro armadilhas. Pubalgia: tratar sem saber a fonte. Repouso e volta igual: a dor some e volta junto com a carga. Passivo antes da carga: recurso ou injeção como tratamento principal. Esquecer a manutenção: a recidiva mora na volta sem exercícios")]
    rs = []
    W = 386
    for k, (ic, t, d, cor, fundo) in enumerate([("t:question-mark", "“Pubalgia”", "tratar sem saber a fonte", GLIC, GLIC_T),
                                                ("t:repeat", "Repouso e volta igual", "a dor some e volta junto com a carga", GLIC, GLIC_T),
                                                ("t:pill", "Passivo antes da carga", "recurso ou injeção como tratamento principal", FOSF, FOSF_T),
                                                ("t:door-exit", "Esquecer a manutenção", "a recidiva mora na volta sem exercícios", FOSF, FOSF_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 320, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="{x + 60}" cy="70" r="40" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        p.append(icone(ic, x + 36, 46, 48, cor))
        p.append(icone("t:alert-triangle", x + W - 64, 30, 40, cor))
        rs += [rot(x + 24, 134, t, w=W - 48, tam=25, cor=cor, peso=700, serif=True, lh=1.15),
               rot(x + 24, 210, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    return slide("armadilhas", 320, p, rs, eyebrow="Juntando as duas macas", titulo="Quatro armadilhas")

# ---------------------------------------------------------------- 8.7

def um3_87():
    """8.7: a linha do tratamento habitual que termina cedo, e três figuras com uma torcendo de novo."""
    p = [svg_abre(1664, 340, "Uma linha do tempo do tratamento habitual, bem feito: entorse descendo do bloqueio, gelo, faixa e alguns dias de muleta, volta sem dor em pouco mais de uma semana. Ali o tratamento termina. No ano seguinte, de cada três atletas, uma torce de novo"), defs(MUDO)]
    rs = []
    etapas = [("t:alert-triangle", "entorse", FOSF), ("t:first-aid-kit", "gelo, faixa, muleta", AZUL), ("t:walk", "sem dor em pouco mais de uma semana", OXID)]
    for k, (ic, t, cor) in enumerate(etapas):
        x = k * 300
        p.append(f'<circle cx="{x + 60}" cy="80" r="56" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        p.append(icone(ic, x + 34, 54, 52, cor))
        rs.append(rot(x - 20, 152, t, w=200, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.2))
        if k < 2:
            p.append(seta(x + 124, 80, x + 232, 80, MUDO, "m0", esp=3))
    p.append(f'<line x1="810" y1="0" x2="810" y2="300" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs.append(rot(830, 0, "o tratamento termina aqui", w=320, tam=21, cor=TINTA, peso=700))
    p.append(caixa(850, 70, 814, 270, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(874, 88, "no ano seguinte", w=780, tam=22, cor=FOSF, peso=700))
    for j in range(3):
        p.append(icone("h:person", 900 + j * 130, 140, 110, FOSF if j == 0 else MUDO))
    rs.append(rot(1330, 160, "uma em cada três torce de novo", w=320, tam=26, cor=FOSF, peso=700, serif=True, lh=1.2))
    return slide("um3", 340, p, rs, eyebrow="Descendo do bloqueio, no pé da adversária", titulo="Um em cada três torceu de novo no ano seguinte.",
                 fonte="Tratamento habitual, bem feito · BMJ 2009")


def ensaio_87():
    """8.7: 522 atletas sorteados em dois braços, com as barras de nova entorse em um ano."""
    p = [svg_abre(1664, 340, "522 atletas de 12 a 70 anos com entorse lateral recente, sorteados em dois braços. Tratamento habitual: 33% de nova entorse em um ano. Tratamento habitual mais oito semanas de programa de equilíbrio e propriocepção em casa, sem supervisão: 22%"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 90, 340, 160, TINTA, TINTA, esp=0, rx=16))
    rs += [rot(0, 108, "522", w=340, tam=52, cor=PAPEL, peso=700, alinha="center", serif=True), rot(16, 186, "atletas de 12 a 70 anos, entorse lateral recente", w=308, tam=18, cor=PAPEL, alinha="center", lh=1.2)]
    p.append(seta(350, 170, 420, 80, MUDO, "m0", esp=3))
    p.append(seta(350, 170, 420, 260, MUDO, "m0", esp=3))
    X0, E = 860, 22
    for k, (t, v, cor, ic) in enumerate([("tratamento habitual", 33, FOSF, "t:first-aid-kit"), ("+ 8 semanas em casa, sem supervisão", 22, OXID, "t:notebook")]):
        y = 20 + k * 180
        p.append(icone(ic, 432, y + 22, 48, cor))
        rs.append(rot(492, y + 24, t, w=350, tam=21, cor=TINTA, peso=700, lh=1.2))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E}" height="100" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + v * E + 20, y + 26, f"{v}%", w=200, tam=48, cor=cor, peso=700, serif=True))
    rs.append(rot(X0, 310, "nova entorse em um ano", w=600, tam=18, cor=MUDO))
    return slide("ensaio", 340, p, rs, eyebrow="BMJ, 2009", titulo="Oito semanas em casa, sem supervisão",
                 destaque="Não foi um programa caro, conduzido todo dia por um profissional. A pessoa fez sozinha, depois de orientada.", destaque_cor="tinta",
                 fonte="Ensaio holandês, BMJ 2009")


def programa_87():
    """8.7: os quatro ingredientes e, embaixo, oito semanas em casa com a pergunta de toda semana."""
    p = [svg_abre(1664, 400, "Quatro ingredientes: amplitude, a dorsiflexão; força, panturrilha e estabilizadores do pé; equilíbrio, do apoio parado ao instável, olhos abertos a fechados; gesto, salto, aterrissagem e mudança de direção. Embaixo, uma faixa de oito semanas em casa depois da alta. A fisioterapia ensina e entrega por escrito; alguém pergunta toda semana se está sendo feito")]
    rs = []
    W = 386
    for k, (ic, t, d, cor, fundo) in enumerate([("t:ruler-measure", "Amplitude", "a dorsiflexão, o tornozelo dobrando para a frente", OXID, OXID_T),
                                                ("t:barbell", "Força", "panturrilha e estabilizadores do pé", OXID, OXID_T),
                                                ("t:yoga", "Equilíbrio", "do apoio parado ao instável, olhos abertos a fechados", GLIC, GLIC_T),
                                                ("t:ball-volleyball", "Gesto", "salto, aterrissagem, mudança de direção", FOSF, FOSF_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 220, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 44, cor))
        rs += [rot(x + 80, 30, t, w=W - 100, tam=26, cor=cor, peso=700, serif=True), rot(x + 22, 96, d, w=W - 44, tam=21, cor=TINTA, lh=1.3)]
    rs.append(rot(0, 248, "em casa, oito semanas, depois da alta", w=800, tam=22, cor=TINTA, peso=700))
    for s in range(8):
        x = s * 140
        p.append(f'<rect x="{x}" y="290" width="124" height="60" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        p.append(icone("t:check", x + 44, 300, 36, OXID))
    p.append(caixa(1140, 250, 524, 150, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:message-circle", 1162, 272, 44, PAPEL))
    rs += [rot(1220, 274, "alguém pergunta toda semana se está sendo feito", w=420, tam=21, cor=PAPEL, peso=700, lh=1.25),
           rot(0, 366, "a fisioterapia ensina e entrega por escrito", w=1100, tam=20, cor=MUDO)]
    return slide("programa", 400, p, rs, eyebrow="Os quatro ingredientes do módulo de lesões", titulo="Em casa, oito semanas, depois da alta")


def ortese_87():
    """8.7: três barras de nova entorse, treino, órtese e os dois, e o que não mudou entre os grupos."""
    p = [svg_abre(1664, 340, "Três barras de nova entorse em um ano, em 384 atletas: 27% com o treino de oito semanas; 15% com órtese semirrígida em todo esporte por 12 meses; 19% com os dois, órtese por oito semanas. Órtese contra treino: risco relativo de 0,53. Ao lado, o que não foi diferente entre os grupos: gravidade, tempo perdido e custos")]
    rs = []
    B, E = 270, 7
    for k, (v, t, cor) in enumerate([(27, "treino, 8 semanas", GLIC), (15, "órtese, 12 meses", OXID), (19, "os dois", OXID)]):
        x = 20 + k * 280
        p.append(f'<rect x="{x}" y="{B - v * E}" width="220" height="{v * E}" rx="8" fill="{cor}" opacity="{0.7 if k == 2 else 1}"/>')
        rs += [rot(x, B - v * E - 54, f"{v}%", w=220, tam=40, cor=cor, peso=700, alinha="center", serif=True), rot(x - 20, B + 10, t, w=260, tam=20, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="0" y1="{B}" x2="840" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(0, 310, "nova entorse em um ano · órtese contra treino: risco relativo 0,53", w=860, tam=19, cor=MUDO, peso=700))
    p.append(caixa(920, 0, 744, 340, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(944, 20, "Não foram diferentes", w=700, tam=27, cor=TINTA, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:gauge", "gravidade das novas entorses"), ("t:hourglass", "tempo perdido"), ("t:scale", "custos")]):
        y = 90 + j * 76
        p.append(icone(ic, 944, y, 44, MUDO))
        rs.append(rot(1004, y + 8, t, w=620, tam=23, cor=TINTA, peso=700))
    rs.append(rot(944, 304, "a órtese reduziu quantas, não o tamanho", w=700, tam=19, cor=MUDO))
    return slide("ortese", 340, p, rs, eyebrow="O segundo número, 2014", titulo="Treino, órtese ou os dois",
                 fonte="384 atletas, ensaio holandês · Br J Sports Med 2014")


def juntar_87():
    """8.7: duas linhas do tempo, a proteção da órtese desde o primeiro dia e a capacidade do treino subindo em semanas."""
    p = [svg_abre(1664, 360, "Duas linhas do tempo, em esquema. A órtese: proteção desde o primeiro dia, enquanto a capacidade não voltou; depende de usar em todo treino, por meses. O treino: reconstrói amplitude, força e controle, subindo ao longo de semanas; depende de fazer, e muita gente para. Um sinal de mais entre as duas: para quem já torceu, se somam")]
    rs = []
    for k, (t, cor, fundo, ic, itens) in enumerate([("A órtese protege", OXID, OXID_T, "t:shield", ["funciona desde o primeiro dia", "depende de usar em todo treino, por meses"]),
                                                    ("O treino reconstrói", GLIC, GLIC_T, "t:barbell", ["amplitude, força e controle, em semanas", "depende de fazer, e muita gente para"])]):
        x = k * 884
        p.append(caixa(x, 0, 780, 360, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 22, 44, cor))
        rs.append(rot(x + 82, 28, t, w=680, tam=27, cor=cor, peso=700, serif=True))
        p.append(f'<line x1="{x + 40}" y1="210" x2="{x + 740}" y2="210" stroke="{MUDO}" stroke-width="2"/>')
        if k == 0:
            p.append(f'<path d="M {x + 40} 210 L {x + 40} 110 L {x + 740} 110 L {x + 740} 210 Z" fill="{OXID}" opacity="0.35"/>')
        else:
            p.append(f'<path d="M {x + 40} 205 C {x + 300} 200, {x + 450} 120, {x + 740} 104" fill="none" stroke="{GLIC}" stroke-width="6"/>')
        rs.append(rot(x + 40, 218, "tempo · esquema", w=700, tam=16, cor=MUDO, alinha="right"))
        for j, it in enumerate(itens):
            rs.append(rot(x + 40, 260 + j * 40, "· " + it, w=720, tam=21, cor=TINTA, peso=700 if j == 0 else 400))
    p.append(f'<circle cx="832" cy="180" r="34" fill="{TINTA}"/>')
    rs.append(rot(798, 152, "+", w=68, tam=44, cor=PAPEL, peso=700, alinha="center"))
    return slide("juntar", 360, p, rs, eyebrow="Sem briga de torcida", titulo="Uma protege, o outro reconstrói",
                 destaque="Para quem já torceu, as duas se somam. A pergunta útil: qual delas essa pessoa vai de fato usar ou fazer, e por quanto tempo?", destaque_cor="tinta",
                 fonte="Revisão de revisões, Br J Sports Med 2017")


def oito_87():
    """8.7: a dor cai sozinha até a alta; a capacidade só sobe se as oito semanas acontecerem, em esquema."""
    p = [svg_abre(1664, 360, "Em esquema, depois da entorse: a dor cai sozinha e zera perto da alta. A capacidade do tornozelo fica baixa e só sobe na faixa das oito semanas depois da alta, se o programa for feito; sem ele, continua baixa. É quando a dor vai embora que a pessoa para de cuidar do tornozelo")]
    rs = []
    X0, B, A = 120, 300, 520
    p.append(f'<rect x="{A}" y="20" width="700" height="{B - 20}" fill="{OXID_T}"/>')
    p.append(f'<line x1="{X0}" y1="{B}" x2="1640" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="{A}" y1="10" x2="{A}" y2="{B}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    p.append(f'<path d="M {X0} 40 C {X0 + 200} 60, {A - 160} 270, {A} 296 L 1640 296" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<path d="M {X0} 250 C {X0 + 200} 240, {A - 100} 220, {A} 220 C {A + 300} 210, {A + 500} 100, 1220 80 L 1640 76" fill="none" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<path d="M {A} 220 L 1640 222" fill="none" stroke="{MUDO}" stroke-width="4"{TRACO}/>')
    rs += [rot(X0, 0, "dor", w=200, tam=22, cor=FOSF, peso=700), rot(A - 250, 60, "a dor vai embora sozinha", w=240, tam=19, cor=FOSF, alinha="right"),
           rot(A + 14, 0, "alta", w=200, tam=22, cor=TINTA, peso=700), rot(A + 160, 30, "oito semanas depois da alta", w=420, tam=22, cor=OXID, peso=700),
           rot(1260, 34, "com o programa", w=380, tam=21, cor=OXID, peso=700), rot(1260, 180, "sem ele, a capacidade não volta", w=380, tam=21, cor=MUDO, peso=700),
           rot(0, 236, "capacidade", w=110, tam=19, cor=OXID, peso=700, alinha="right"), rot(X0, 312, "entorse", w=200, tam=18, cor=MUDO),
           rot(1440, 312, "esquema", w=200, tam=17, cor=MUDO, alinha="right")]
    return slide("oito", 360, p, rs, eyebrow="A ideia da aula", titulo="A próxima entorse se decide nas oito semanas depois da alta.",
                 destaque="É quando a dor vai embora que a pessoa para de cuidar do tornozelo.", destaque_cor="tinta")


def paass_87():
    """8.7: cinco fechaduras numa porta de retorno, uma por domínio do consenso."""
    p = [svg_abre(1664, 320, "Cinco cartões, como cinco fechaduras de uma porta de retorno. Dor: no esporte e nas últimas 24 horas. Tornozelo: amplitude, força, resistência, potência. Percepção: confiança, estabilidade, prontidão. Controle: equilíbrio parado e em movimento. Desempenho: saltos, agilidade, um treino inteiro. A porta só abre com as cinco")]
    rs = []
    W = 304
    for k, (ic, t, d, cor, fundo) in enumerate([("t:gauge", "Dor", "no esporte e nas últimas 24 horas", FOSF, FOSF_T),
                                                ("t:ruler-measure", "Tornozelo", "amplitude, força, resistência, potência", OXID, OXID_T),
                                                ("t:message-circle", "Percepção", "confiança, estabilidade, prontidão", GLIC, GLIC_T),
                                                ("t:yoga", "Controle", "equilíbrio parado e em movimento", OXID, OXID_T),
                                                ("t:run", "Desempenho", "saltos, agilidade, um treino inteiro", TINTA, PAPEL)]):
        x = k * (W + 36)
        p.append(caixa(x, 0, W, 240, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 22, 22, 48, cor))
        p.append(icone("t:lock", x + W - 58, 26, 36, MUDO))
        rs += [rot(x + 22, 92, t, w=W - 44, tam=26, cor=cor, peso=700, serif=True), rot(x + 22, 140, d, w=W - 44, tam=20, cor=TINTA, lh=1.3)]
    p.append(f'<path d="M 152 252 L 152 272 L 1512 272 L 1512 252" fill="none" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="832" y1="272" x2="832" y2="286" stroke="{MUDO}" stroke-width="3"/>')
    rs.append(rot(432, 290, "a porta só abre com as cinco, não com a ausência de dor", w=800, tam=21, cor=TINTA, peso=700, alinha="center"))
    return slide("paass", 320, p, rs, eyebrow="Consenso internacional de 2021", titulo="Cinco perguntas antes de voltar",
                 destaque="98% de concordância entre os participantes.", destaque_cor="tinta", fonte="Br J Sports Med 2021")


def barato_87():
    """8.7: cinco linhas, cada pergunta com o jeito barato de medir."""
    p = [svg_abre(1664, 420, "Cinco linhas, cada pergunta com um jeito barato de responder. Dor: nota de 0 a 10 no treino e na manhã seguinte. Tornozelo: joelho à parede com fita; elevações de calcanhar numa perna, dos dois lados. Percepção: você confia nesse tornozelo para bloquear e cair?, e um questionário de instabilidade. Controle: apoio numa perna, olhos abertos e fechados; alcance em várias direções. Desempenho: saltos numa perna, de lado e para a frente; o treino completo, observado. Embaixo: compare com o outro lado e com a própria pessoa ao longo das semanas"), defs(MUDO)]
    rs = []
    linhas = [("t:gauge", "Dor", "nota de 0 a 10 no treino e na manhã seguinte", FOSF, FOSF_T),
              ("t:ruler-measure", "Tornozelo", "joelho à parede com fita; elevações de calcanhar numa perna, dos dois lados", OXID, OXID_T),
              ("t:message-circle", "Percepção", "“Você confia nesse tornozelo para bloquear e cair?”; questionário de instabilidade", GLIC, GLIC_T),
              ("t:yoga", "Controle", "apoio numa perna, olhos abertos e fechados; alcance em várias direções", OXID, OXID_T),
              ("t:run", "Desempenho", "saltos numa perna, de lado e para a frente; o treino completo, observado", TINTA, PAPEL)]
    for k, (ic, t, d, cor, fundo) in enumerate(linhas):
        y = k * 70
        p.append(caixa(0, y, 330, 58, cor, fundo, esp=2, rx=12))
        p.append(icone(ic, 14, y + 10, 38, cor))
        rs.append(rot(64, y + 15, t, w=250, tam=23, cor=cor, peso=700))
        p.append(seta(340, y + 29, 392, y + 29, MUDO, "m0", esp=3))
        p.append(caixa(404, y, 1260, 58, BORDA, CARTAO, esp=2, rx=12))
        rs.append(rot(426, y + 16, d, w=1220, tam=21, cor=TINTA))
    p.append(caixa(0, 362, 1664, 58, TINTA, TINTA, esp=0, rx=12))
    p.append(icone("t:arrows-exchange", 18, 371, 40, PAPEL))
    rs.append(rot(72, 376, "nenhum valor mágico: compare com o outro lado e com a própria pessoa ao longo das semanas", w=1570, tam=22, cor=PAPEL, peso=700))
    return slide("barato", 420, p, rs, eyebrow="Sem laboratório", titulo="Um jeito barato de responder cada uma")


def erros_87():
    """8.7: três erros de alta, cada um com o seu pequeno desenho."""
    p = [svg_abre(1664, 340, "Três cartões de erro de alta, cada um com um pequeno desenho. Alta pela dor: três figuras, uma torcendo de novo; é o erro que produz o um em cada três. Órtese sem treino: a órtese sai e o tornozelo é o mesmo de antes. Programa que para no jogo: oito semanas previstas, só duas feitas; quem para na segunda semana não fez o programa que funcionou")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("Alta pela dor", "o erro que produz o um em cada três", FOSF, FOSF_T),
                                            ("Órtese sem treino", "quando a órtese sai, o tornozelo é o mesmo de antes", GLIC, GLIC_T),
                                            ("Programa que para no jogo", "quem para na segunda semana não fez o programa que funcionou", GLIC, GLIC_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 340, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 20, t, w=W - 48, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 250, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    for j in range(3):
        p.append(icone("h:person", 60 + j * 140, 90, 120, FOSF if j == 0 else MUDO))
    x = W + 40
    p.append(icone("t:shield", x + 60, 100, 100, MUDO))
    p.append(f'<line x1="{x + 50}" y1="200" x2="{x + 170}" y2="100" stroke="{FOSF}" stroke-width="5"/>')
    p.append(icone("t:arrows-exchange", x + 210, 126, 48, MUDO))
    p.append(icone("t:alert-triangle", x + 310, 100, 100, GLIC))
    x = 2 * (W + 40)
    for s in range(8):
        p.append(f'<rect x="{x + 24 + s * 60}" y="120" width="50" height="80" rx="8" fill="{GLIC if s < 2 else CINZA}" opacity="{1 if s < 2 else 0.5}"/>')
    rs.append(rot(x + 24, 80, "8 semanas previstas, 2 feitas", w=W - 48, tam=19, cor=MUDO, peso=700))
    return slide("erros", 340, p, rs, eyebrow="O que os números explicam", titulo="Três erros de alta")


def quem_87():
    """8.7: cinco faixas de responsáveis da beira da quadra às oito semanas, em esquema."""
    p = [svg_abre(1664, 420, "Em esquema, cinco faixas da entorse às oito semanas depois da alta. Médico: nos primeiros dias, descarta fratura e lesão associada, decide imagem, analgesia. Fisioterapia: fase inicial, ensina e entrega o programa, aplica as cinco perguntas. Preparação física: o programa dentro do aquecimento, saltos e mudança de direção. Treinador: cobra a órtese indicada e não conta como recuperada quem parou o programa. Atleta: sabe a conta, nove fazendo, uma entorse a menos")]
    rs = []
    X0, W = 330, 1334
    def mx(s):
        return X0 + (s + 1) * W / 11
    for s, t in [(-1, "entorse"), (1.5, "alta"), (9.5, "8 semanas depois")]:
        p.append(f'<line x1="{mx(s):.0f}" y1="0" x2="{mx(s):.0f}" y2="380" stroke="{BORDA}" stroke-width="2"/>')
        rs.append(rot(min(mx(s) - 90, 1484), 388, t, w=180, tam=18, cor=MUDO, alinha="center" if s < 9 else "right"))
    faixas = [("Médico", [(-1, 0.4, 1)], "primeiros dias: descarta fratura e lesão associada; imagem; analgesia", AZUL, 0.4, TINTA),
              ("Fisioterapia", [(-1, 1.5, .55), (1.5, 9.5, .3), (8.8, 9.5, .55)], "fase inicial; ensina e entrega o programa; as cinco perguntas", OXID, -1, TINTA),
              ("Preparação física", [(1.5, 9.5, 1)], "o programa no aquecimento; saltos e mudança de direção", GLIC, 1.5, PAPEL),
              ("Treinador", [(-1, 9.5, .3)], "cobra a órtese indicada; não conta como recuperada quem parou o programa", TINTA, -1, TINTA),
              ("Atleta", [(-1, 9.5, .3)], "sabe a conta: nove fazendo, uma entorse a menos", FOSF, -1, TINTA)]
    for k, (t, segs, d, cor, x0, ct) in enumerate(faixas):
        y = 6 + k * 76
        rs.append(rot(0, y + 18, t, w=300, tam=22, cor=cor, peso=700, alinha="right"))
        for a, b, op in segs:
            p.append(f'<rect x="{mx(a):.0f}" y="{y}" width="{mx(b) - mx(a):.0f}" height="60" rx="10" fill="{cor}" opacity="{op}"/>')
        rs.append(rot(mx(x0) + 14, y + 18, d, w=mx(9.5) - mx(x0) - 32, tam=19, cor=ct, peso=700))
    rs.append(rot(0, 388, "esquema", w=200, tam=17, cor=MUDO, alinha="right"))
    return slide("quem", 420, p, rs, eyebrow="Quem faz o quê", titulo="Da beira da quadra às oito semanas")

# ---------------------------------------------------------------- 8.8

def paro_88():
    """8.8: a nadadora e o levantador perguntam se param; as duas respostas ruins riscadas."""
    p = [svg_abre(1664, 340, "À esquerda, dois atletas fazem a mesma pergunta, eu paro?: uma nadadora adolescente com dor no ombro no meio da temporada, e um levantador com dor lombar desde o terra de segunda-feira. À direita, as duas respostas ruins, riscadas: para tudo até passar, que tira o atleta do esporte por semanas; e continua, é normal, que mantém a carga que produziu a dor")]
    rs = []
    for k, (ic, t, d, cor) in enumerate([("t:swimming", "Nadadora adolescente", "dor no ombro no meio da temporada", AZUL), ("t:barbell", "Levantador", "dor lombar desde o terra de segunda", GLIC)]):
        y = k * 180
        p.append(caixa(0, y, 640, 160, cor, CARTAO, esp=2, rx=16))
        p.append(icone(ic, 24, y + 24, 64, cor))
        rs += [rot(108, y + 26, t, w=510, tam=25, cor=cor, peso=700, serif=True), rot(108, y + 70, d, w=510, tam=21, cor=TINTA)]
    p.append(f'<path d="M 660 80 C 720 80, 720 170, 760 170 C 720 170, 720 260, 660 260" fill="none" stroke="{MUDO}" stroke-width="3"/>')
    p.append(caixa(780, 120, 240, 100, TINTA, TINTA, esp=0, rx=50))
    rs.append(rot(780, 148, "“Eu paro?”", w=240, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    for k, (t, d) in enumerate([("“Para tudo até passar”", "tira do esporte por semanas"), ("“Continua, é normal”", "mantém a carga que produziu a dor")]):
        y = k * 180
        p.append(caixa(1060, y, 604, 160, FOSF, FOSF_T, esp=2, rx=16))
        p.append(icone("t:x", 1084, y + 24, 48, FOSF))
        rs += [rot(1146, y + 28, t, w=500, tam=25, cor=FOSF, peso=700, serif=True), rot(1084, y + 90, d, w=560, tam=21, cor=TINTA)]
    return slide("paro", 340, p, rs, eyebrow="Na borda da piscina e no chão da academia", titulo="“Eu paro?” Uma decisão com três saídas, não com duas.")


def alerta_88():
    """8.8: os sinais de alerta do ombro e da coluna, e a faixa do adolescente que piora em extensão."""
    p = [svg_abre(1664, 420, "Dois painéis vermelhos de sinais de alerta. Ombro: perda súbita de força depois de trauma; sensação de que saiu do lugar; formigamento ou fraqueza descendo para a mão. Coluna: fraqueza ou dormência progredindo na perna; alteração urinária ou dormência na sela, que é emergência; dor noturna com febre, perda de peso ou câncer prévio. Embaixo, uma faixa: o adolescente com dor lombar que piora ao estender a coluna; lesão por estresse do arco vertebral entra na lista, avaliação médica antes do programa")]
    rs = []
    for k, (t, itens) in enumerate([("Ombro", [("t:trending-down", "perda súbita de força depois de trauma"), ("t:arrows-exchange", "sensação de que saiu do lugar"), ("t:bolt", "formigamento ou fraqueza descendo para a mão")]),
                                    ("Coluna", [("t:walk", "fraqueza ou dormência progredindo na perna"), ("t:alert-triangle", "alteração urinária ou dormência na sela: emergência"), ("t:moon", "dor noturna com febre, perda de peso, câncer prévio")])]):
        x = k * 844
        p.append(caixa(x, 0, 820, 280, FOSF, FOSF_T, esp=2, rx=16))
        rs.append(rot(x + 24, 18, t, w=760, tam=27, cor=FOSF, peso=700, serif=True))
        for j, (ic, it) in enumerate(itens):
            y = 78 + j * 66
            p.append(icone(ic, x + 24, y, 40, FOSF))
            rs.append(rot(x + 80, y + 6, it, w=720, tam=22, cor=TINTA, peso=700 if "emergência" in it else 400))
    p.append(caixa(0, 304, 1664, 116, FOSF, FOSF, esp=0, rx=16))
    p.append(icone("t:stretching", 24, 334, 56, PAPEL))
    rs += [rot(100, 322, "Adolescente com dor lombar que piora ao estender a coluna", w=1540, tam=24, cor=PAPEL, peso=700, serif=True),
           rot(100, 364, "lesão por estresse do arco vertebral entra na lista: avaliação médica antes do programa", w=1540, tam=21, cor=PAPEL)]
    return slide("alerta", 420, p, rs, eyebrow="Quando parar e avaliar", titulo="Os sinais que tiram a decisão da piscina e da academia")


def natacao_88():
    """8.8: a faixa etária dos nadadores com o grupo adolescente marcado, e uma temporada com um salto de volume."""
    p = [svg_abre(1664, 360, "À esquerda, 12 estudos com 1.460 nadadores de competição, das categorias de base aos masters, numa faixa de idade; os adolescentes estão marcados: mais dor no ombro, e nesse grupo o volume de treino se associou à dor. À direita, em esquema, uma temporada de quilômetros por semana com um salto grande e repentino, marcado: é ali que a dor costuma começar. Monitorar o ano inteiro")]
    rs = []
    p.append(caixa(0, 0, 760, 360, TINTA, CARTAO, esp=2, rx=16))
    rs += [rot(24, 18, "12 estudos · 1.460 nadadores", w=720, tam=26, cor=TINTA, peso=700, serif=True),
           rot(24, 60, "de competição, da base aos masters", w=720, tam=20, cor=MUDO)]
    for j, t in enumerate(["base", "adolescentes", "adultos", "masters"]):
        x = 24 + j * 180
        ado = j == 1
        p.append(f'<rect x="{x}" y="120" width="168" height="90" rx="10" fill="{GLIC if ado else CINZA}" opacity="{1 if ado else 0.5}"/>')
        p.append(icone("t:swimming", x + 62, 132, 44, PAPEL if ado else MUDO))
        rs.append(rot(x, 180, t, w=168, tam=19, cor=PAPEL if ado else TINTA, peso=700, alinha="center"))
    rs += [rot(24, 236, "adolescentes: mais dor no ombro", w=720, tam=22, cor=GLIC, peso=700),
           rot(24, 276, "e, nesse grupo, o volume se associou à dor", w=720, tam=21, cor=TINTA)]
    p.append(caixa(820, 0, 844, 360, GLIC, CARTAO, esp=2, rx=16))
    rs.append(rot(844, 18, "km por semana numa temporada · esquema", w=800, tam=20, cor=GLIC, peso=700))
    B = 280
    vals = [40, 42, 44, 45, 46, 48, 74, 76, 78, 60, 58, 60]
    for i, v in enumerate(vals):
        x = 860 + i * 64
        p.append(f'<rect x="{x}" y="{B - v * 2.6:.0f}" width="48" height="{v * 2.6:.0f}" rx="4" fill="{FOSF if i == 6 else GLIC}" opacity="{1 if i == 6 else 0.55}"/>')
    p.append(f'<line x1="844" y1="{B}" x2="1640" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(icone("t:alert-triangle", 1240, 54, 40, FOSF))
    rs += [rot(1288, 60, "salto grande e repentino", w=340, tam=20, cor=FOSF, peso=700),
           rot(844, 300, "monitorar o ano inteiro; evitar aumentos grandes e repentinos", w=800, tam=20, cor=TINTA, peso=700, lh=1.2)]
    return slide("natacao", 360, p, rs, eyebrow="O ombro da nadadora", titulo="Começa numa temporada, não numa braçada",
                 fonte="Revisão sistemática, J Athl Train 2020")


def _alavancas(p, rs, linhas, y0=0, alt=66, xb=420):
    """Linhas de alavanca: nome, controle deslizante com a posição antes e depois, e o que muda."""
    for k, (t, antes, depois, d, cor) in enumerate(linhas):
        y = y0 + k * alt
        rs.append(rot(0, y + 12, t, w=280, tam=22, cor=cor, peso=700, alinha="right", lh=1.1))
        p.append(f'<rect x="300" y="{y + 22}" width="{xb - 300 + 0}" height="10" rx="5" fill="{CINZA}"/>')
        xa, xd = 300 + antes * (xb - 300), 300 + depois * (xb - 300)
        if antes is not None and antes != depois:
            p.append(f'<circle cx="{xa:.0f}" cy="{y + 27}" r="10" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"/>')
        p.append(f'<circle cx="{xd:.0f}" cy="{y + 27}" r="13" fill="{cor}"/>')
        rs.append(rot(xb + 40, y + 12, d, w=1664 - xb - 40, tam=21, cor=TINTA))


def mod_ombro_88():
    """8.8: cinco alavancas como controles deslizantes, cada uma na posição nova, e a atleta na água."""
    p = [svg_abre(1664, 360, "Cinco alavancas desenhadas como controles deslizantes, com a posição de antes em cinza e a nova em cor. Volume: menos quilômetros por um período, sem zerar. Intensidade e estilo: tirar as séries mais fortes e o estilo que mais provoca. Material: o palmar grande costuma ser o primeiro a sair. Pernada: sobe, mantém o condicionamento com menos ombro. Em paralelo: fortalecimento progressivo do manguito e da escápula, subindo")]
    rs = []
    _alavancas(p, rs, [("Volume", 0.9, 0.55, "menos quilômetros por um período, sem zerar", AZUL),
                       ("Intensidade e estilo", 0.85, 0.5, "tirar as séries mais fortes e o estilo que mais provoca", AZUL),
                       ("Material", 0.9, 0.1, "o palmar grande costuma ser o primeiro a sair", AZUL),
                       ("Pernada", 0.4, 0.85, "mais pernas mantém o condicionamento com menos ombro", OXID),
                       ("Em paralelo", 0.3, 0.8, "fortalecimento progressivo do manguito e da escápula", OXID)], xb=620)
    rs.append(rot(300, 340, "antes ○ · ● agora", w=320, tam=17, cor=MUDO, alinha="center"))
    return slide("mod_ombro", 360, p, rs, eyebrow="Modificar o ombro", titulo="Várias alavancas, a atleta na água",
                 destaque="A modificação tira o pico; o fortalecimento aumenta a capacidade.", destaque_cor="tinta")


def cirurgia_88():
    """8.8: três grupos do ensaio em esquema, os dois operados iguais e o sem tratamento um pouco atrás."""
    p = [svg_abre(1664, 320, "Em esquema, sem valores, três barras de melhora. Descompressão e artroscopia sem retirar nada: iguais entre si, com um sinal de igual. Nenhum tratamento: um pouco atrás dos dois grupos operados, sem diferença clinicamente importante")]
    rs = []
    B = 250
    grupos = [("t:first-aid-kit", "Descompressão", "melhorou um pouco mais que nada", 170, GLIC),
              ("t:eye", "Artroscopia sem retirar nada", "o mesmo resultado da descompressão", 172, GLIC),
              ("t:clock", "Nenhum tratamento", "um pouco atrás dos operados", 140, MUDO)]
    for k, (ic, t, d, h, cor) in enumerate(grupos):
        x = k * 560
        p.append(f'<rect x="{x + 40}" y="{B - h}" width="220" height="{h}" rx="8" fill="{cor}"/>')
        p.append(icone(ic, x + 126, B - h + 20, 48, PAPEL))
        rs += [rot(x + 280, B - h, t, w=260, tam=23, cor=cor if cor != MUDO else TINTA, peso=700, serif=True, lh=1.15),
               rot(x + 280, B - h + 70, d, w=260, tam=19, cor=TINTA, lh=1.25)]
    rs.append(rot(500, 40, "=", w=80, tam=48, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="0" y1="{B}" x2="1664" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(0, 266, "melhora da dor e da função · esquema, sem valores · diferença sem importância clínica", w=1664, tam=19, cor=MUDO))
    return slide("cirurgia", 320, p, rs, eyebrow="E quando alguém propõe cirurgia", titulo="Um ensaio com artroscopia sem descompressão",
                 destaque="Adultos com dor subacromial, não nadadores de competição; a decisão é do cirurgião com o paciente. Mas a carga bem conduzida segue como primeira linha.",
                 destaque_cor="tinta", fonte="32 hospitais britânicos · Lancet 2018")


def meio_88():
    """8.8: um mostrador de três faixas com o ponteiro no meio, a faixa de modificar."""
    import math
    p = [svg_abre(1664, 400, "Um mostrador em arco com três faixas: parar, estreita, à esquerda; modificar, a mais larga, no meio; manter, à direita. O ponteiro aponta para o meio. Modificar o suficiente para a dor baixar, e pouco o bastante para o atleta seguir treinando, condicionado e confiante")]
    rs = []
    cx, cy, R = 832, 380, 290
    def arco(a0, a1, cor):
        x0, y0 = cx - R * math.cos(math.radians(a0)), cy - R * math.sin(math.radians(a0))
        x1, y1 = cx - R * math.cos(math.radians(a1)), cy - R * math.sin(math.radians(a1))
        return f'<path d="M {x0:.0f} {y0:.0f} A {R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="{cor}" stroke-width="56"/>'
    p += [arco(2, 34, FOSF), arco(38, 142, GLIC), arco(146, 178, OXID)]
    a = math.radians(90)
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 220}" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="{TINTA}"/>')
    rs += [rot(240, 346, "parar", w=200, tam=26, cor=FOSF, peso=700, alinha="right", serif=True),
           rot(cx - 150, 0, "modificar", w=300, tam=30, cor=GLIC, peso=700, alinha="center", serif=True),
           rot(1224, 346, "manter", w=200, tam=26, cor=OXID, peso=700, serif=True),
           rot(0, 160, "o suficiente para a dor baixar", w=440, tam=22, cor=TINTA, peso=700, alinha="right", lh=1.25),
           rot(1224, 160, "pouco o bastante para seguir treinando, condicionado e confiante", w=440, tam=22, cor=TINTA, peso=700, lh=1.25)]
    return slide("meio", 400, p, rs, eyebrow="A ideia da aula", titulo="Parar tudo raramente é a resposta. Manter tudo também não.")


def flexao_88():
    """8.8: as duas perguntas da revisão de 2020, cada uma com um não, e as ressalvas."""
    p = [svg_abre(1664, 340, "Duas perguntas que a revisão de 2020 fez sobre mais flexão lombar ao levantar. É fator de risco para a dor começar ou persistir? Não. Diferencia quem tem de quem não tem dor? Não. Ao lado, as ressalvas: evidência de baixa qualidade; a técnica segue importando para o desempenho"), defs(MUDO)]
    rs = []
    rs.append(rot(0, 0, "mais flexão lombar ao levantar…", w=1000, tam=23, cor=TINTA, peso=700, serif=True))
    for k, t in enumerate(["é fator de risco para a dor começar ou persistir?", "diferencia quem tem de quem não tem dor?"]):
        y = 56 + k * 140
        p.append(caixa(0, y, 820, 116, TINTA, CARTAO, esp=2, rx=14))
        p.append(icone("t:question-mark", 22, y + 34, 48, TINTA))
        rs.append(rot(90, y + 22, t, w=700, tam=23, cor=TINTA, peso=700, lh=1.25))
        p.append(seta(832, y + 58, 900, y + 58, MUDO, "m0", esp=3))
        p.append(f'<circle cx="980" cy="{y + 58}" r="56" fill="{OXID}"/>')
        rs.append(rot(924, y + 38, "não", w=112, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True))
    p.append(caixa(1100, 56, 564, 256, MUDO, PAPEL, esp=2, rx=16))
    for j, (ic, t) in enumerate([("t:filter", "evidência de baixa qualidade"), ("t:target", "a técnica segue importando para o desempenho")]):
        y = 84 + j * 110
        p.append(icone(ic, 1124, y, 44, MUDO))
        rs.append(rot(1184, y + 4, t, w=460, tam=22, cor=TINTA, lh=1.25))
    return slide("flexao", 340, p, rs, eyebrow="A coluna do levantador · o medo", titulo="“Você curvou a coluna e se machucou”",
                 destaque="A explicação não tem o peso que costuma ter, e alimenta um medo de mexer a coluna que atrapalha a recuperação.", destaque_cor="tinta",
                 fonte="J Orthop Sports Phys Ther 2020")


def risco_88():
    """8.8: mil horas de treino como mais de três anos de calendário, com uma a quatro lesões espalhadas."""
    p = [svg_abre(1664, 340, "Mil horas de treino desenhadas como calendário: para quem levanta seis horas por semana, mais de três anos, em faixas de um ano. Nessas mil horas, entre 1 e 4,4 lesões no levantamento básico, marcadas como pontos. Embaixo, uma régua: risco parecido com outros esportes de força sem contato, e baixo perto dos de contato")]
    rs = []
    rs.append(rot(0, 0, "mil horas de treino, a seis horas por semana", w=1100, tam=22, cor=TINTA, peso=700))
    semanas = 1000 / 6
    for ano in range(4):
        y = 46 + ano * 50
        n = 52 if ano < 3 else int(semanas - 156) + 1
        rs.append(rot(0, y + 6, f"{ano + 1}º ano", w=100, tam=19, cor=MUDO, peso=700, alinha="right"))
        for s in range(n):
            p.append(f'<rect x="{120 + s * 22}" y="{y}" width="18" height="36" rx="3" fill="{OXID}" opacity="0.35"/>')
    for s, ano in [(14, 0), (40, 1), (20, 2), (8, 3)]:
        p.append(f'<circle cx="{129 + s * 22}" cy="{64 + ano * 50}" r="12" fill="{FOSF}"/>')
    p.append(caixa(1300, 46, 364, 186, OXID, OXID, esp=0, rx=16))
    rs += [rot(1300, 70, "1 a 4,4", w=364, tam=46, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1316, 140, "lesões em mil horas no levantamento básico", w=332, tam=20, cor=PAPEL, alinha="center", lh=1.2)]
    p.append(f'<rect x="120" y="270" width="1544" height="20" rx="10" fill="{CINZA}" opacity="0.5"/>')
    p.append(f'<rect x="120" y="270" width="540" height="20" rx="10" fill="{OXID}"/>')
    p.append(f'<rect x="1220" y="270" width="444" height="20" rx="10" fill="{FOSF}" opacity="0.7"/>')
    rs += [rot(120, 300, "força sem contato: parecido", w=700, tam=19, cor=OXID, peso=700),
           rot(1064, 300, "esportes de contato: mais alto", w=600, tam=19, cor=FOSF, peso=700, alinha="right")]
    return slide("risco", 340, p, rs, eyebrow="O risco em perspectiva", titulo="O medo costuma ser maior que o risco",
                 fonte="Revisão sistemática, Br J Sports Med 2017 · a conta dos três anos é nossa")


def mod_coluna_88():
    """8.8: cinco alavancas do levantador e a faixa da primeira linha da série de 2018."""
    p = [svg_abre(1664, 420, "Cinco alavancas desenhadas como controles deslizantes. Carga: menos carga no exercício que provoca, sem tirá-lo, subindo pela resposta do dia seguinte. Amplitude: puxar de blocos ou suportes e ir descendo. Variação: barra hexagonal no lugar do terra, agachamento com a barra na frente. Volume: menos séries pesadas na semana. O resto: membros superiores, cardio, o que não dói, mantido. Embaixo, a primeira linha da série de 2018: educação, retomar as atividades, exercício; sem imagem de rotina")]
    rs = []
    _alavancas(p, rs, [("Carga", 0.9, 0.55, "menos carga no exercício que provoca, sem tirá-lo; sobe pela resposta do dia seguinte", GLIC),
                       ("Amplitude", 0.9, 0.5, "puxar de blocos ou suportes e ir descendo", GLIC),
                       ("Variação", 0.9, 0.6, "barra hexagonal no lugar do terra; agachamento com a barra na frente", GLIC),
                       ("Volume", 0.85, 0.55, "menos séries pesadas na semana", GLIC),
                       ("O resto", 0.8, 0.8, "membros superiores, cardio, o que não dói: mantido", OXID)], xb=560)
    p.append(caixa(0, 340, 1664, 80, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(24, 364, "Primeira linha: educação · retomar as atividades · exercício · sem imagem de rotina", w=1616, tam=22, cor=PAPEL, peso=700))
    return slide("mod_coluna", 420, p, rs, eyebrow="Modificar a coluna", titulo="Sem sinal de alerta, ele continua sendo um levantador",
                 fonte="Série sobre dor lombar, Lancet 2018")


def custo_88():
    """8.8: três desvios entre as portas, cada um com o seu preço."""
    p = [svg_abre(1664, 360, "Três linhas, cada uma com a porta escolhida e a porta certa. Parar quando dava para modificar: força, condicionamento, medo; na adolescente, a temporada. Manter quando precisava modificar: dor crônica, volume subindo, compensação. Modificar quando precisava parar: ruptura, lesão do arco vertebral, sinal neurológico"), defs(MUDO)]
    rs = []
    cores = {"parar": FOSF, "modificar": GLIC, "manter": OXID}
    for k, (esc, certa, preco) in enumerate([("parar", "modificar", "força, condicionamento, medo; na adolescente, a temporada"),
                                             ("manter", "modificar", "dor crônica, volume subindo, compensação"),
                                             ("modificar", "parar", "ruptura, lesão do arco vertebral, sinal neurológico")]):
        y = k * 120
        p.append(caixa(0, y, 230, 96, cores[esc], CARTAO, esp=4, rx=14))
        rs.append(rot(0, y + 30, esc, w=230, tam=26, cor=cores[esc], peso=700, alinha="center", serif=True))
        rs.append(rot(244, y + 8, "quando precisava", w=200, tam=17, cor=MUDO, alinha="center"))
        p.append(seta(250, y + 56, 430, y + 56, MUDO, "m0", esp=3))
        p.append(f'<rect x="{444}" y="{y + 2}" width="226" height="92" rx="14" fill="{CARTAO}" stroke="{cores[certa]}" stroke-width="3"{TRACO}/>')
        rs.append(rot(444, y + 30, certa, w=226, tam=26, cor=cores[certa], peso=700, alinha="center", serif=True))
        p.append(caixa(710, y, 954, 96, FOSF, FOSF_T, esp=2, rx=14))
        p.append(icone("t:scale", 730, y + 26, 44, FOSF))
        rs.append(rot(790, y + 32, preco, w=850, tam=22, cor=TINTA, peso=700))
    return slide("custo", 360, p, rs, eyebrow="O custo de escolher errado", titulo="Cada erro tem o seu preço",
                 destaque="Por isso a primeira pergunta é sempre a dos sinais de alerta.", destaque_cor="verm")

# ---------------------------------------------------------------- 8.9

def perguntas_89():
    """8.9: as quatro perguntas presas a uma barra de uso do recurso: entrada, efeito, checagem e saída."""
    p = [svg_abre(1664, 340, "Uma barra que representa o uso de um recurso ao longo do tempo, com as quatro perguntas presas a ela. No começo: quando entra? Em que fase, para qual objetivo, em quem. Sobre a barra: o que muda? Dor por horas, amplitude, força, tecido. No meio, um ponto de checagem: como sei que não funciona? Qual medida, em quanto tempo. No fim: quando sai? Prazo ou critério de saída")]
    rs = []
    p.append(f'<rect x="180" y="150" width="1300" height="56" rx="28" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    rs.append(rot(180, 164, "o recurso em uso", w=1300, tam=21, cor=OXID, peso=700, alinha="center"))
    p.append(f'<line x1="180" y1="120" x2="180" y2="236" stroke="{OXID}" stroke-width="5"/>')
    p.append(f'<line x1="1480" y1="120" x2="1480" y2="236" stroke="{GLIC}" stroke-width="5"/>')
    p.append(f'<path d="M 200 130 Q 200 110 230 110 L 1430 110 Q 1460 110 1460 130" fill="none" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<circle cx="980" cy="178" r="34" fill="{FOSF}"/>')
    p.append(icone("t:gauge", 960, 158, 40, PAPEL))
    rs += [rot(0, 250, "Quando entra?", w=360, tam=24, cor=OXID, peso=700, alinha="center", serif=True), rot(0, 290, "fase, objetivo, em quem", w=360, tam=20, cor=TINTA, alinha="center"),
           rot(530, 20, "O que muda?", w=600, tam=24, cor=OXID, peso=700, alinha="center", serif=True), rot(430, 60, "dor por horas, amplitude, força, tecido", w=800, tam=20, cor=TINTA, alinha="center"),
           rot(800, 250, "Como sei que não funciona?", w=360, tam=24, cor=FOSF, peso=700, alinha="center", serif=True, lh=1.1), rot(800, 316, "qual medida, em quanto tempo", w=360, tam=20, cor=TINTA, alinha="center"),
           rot(1304, 250, "Quando sai?", w=360, tam=24, cor=GLIC, peso=700, alinha="center", serif=True), rot(1304, 290, "prazo ou critério", w=360, tam=20, cor=TINTA, alinha="center")]
    return slide("perguntas", 340, p, rs, eyebrow="Para qualquer recurso, de qualquer profissão", titulo="Quatro perguntas",
                 destaque="Sem resposta para as quatro, o recurso não está sendo prescrito. Está sendo repetido.", destaque_cor="tinta")


def aparelho_89():
    """8.9: 47 quadrados de ensaio e o veredito para cada aparelho somado a outras intervenções."""
    p = [svg_abre(1664, 340, "À esquerda, 47 quadrados, um por ensaio, com 2.388 participantes, sobre eletroterapia na dor do ombro relacionada ao manguito. À direita, o veredito para cada aparelho somado a outras intervenções, com evidência de baixa qualidade. Ultrassom, laser de baixa intensidade e campo eletromagnético: provavelmente sem benefício. Corrente elétrica para analgesia: incerteza")]
    rs = []
    for i in range(47):
        x, y = (i % 8) * 64, (i // 8) * 46
        p.append(f'<rect x="{x}" y="{y}" width="54" height="36" rx="6" fill="{TINTA}" opacity="0.75"/>')
    rs += [rot(0, 284, "47 ensaios · 2.388 participantes", w=520, tam=22, cor=TINTA, peso=700),
           rot(0, 314, "evidência de baixa qualidade", w=520, tam=19, cor=MUDO)]
    for j, (t, v, ic, cor) in enumerate([("Ultrassom terapêutico", "provavelmente sem benefício somado", "t:x", GLIC), ("Laser de baixa intensidade", "provavelmente sem benefício somado", "t:x", GLIC),
                                         ("Campo eletromagnético pulsado", "provavelmente sem benefício somado", "t:x", GLIC), ("Corrente elétrica para analgesia", "incerteza grande demais", "t:question-mark", MUDO)]):
        y = j * 86
        p.append(caixa(600, y, 1064, 74, cor, CARTAO, esp=2, rx=12))
        p.append(icone(ic, 620, y + 17, 40, cor))
        rs += [rot(676, y + 22, t, w=480, tam=22, cor=TINTA, peso=700), rot(1160, y + 24, v, w=480, tam=20, cor=cor, peso=700, alinha="right")]
    return slide("aparelho", 340, p, rs, eyebrow="Erro um · o aparelho como tratamento", titulo="Eletroterapia no ombro, revisão Cochrane",
                 fonte="Cochrane 2016 · dor do ombro relacionada ao manguito")


def fita_89():
    """8.9: as cinco regiões examinadas e as duas comparações em que a fita não ganhou."""
    p = [svg_abre(1664, 320, "No alto, as cinco regiões examinadas: ombro, joelho, lombar, pescoço, fáscia plantar. Embaixo, duas comparações. Fita elástica contra fita falsa: não foi melhor, com um sinal de igual. Fita elástica contra outras intervenções: não foi melhor. Efeitos pequenos, provavelmente sem importância clínica")]
    rs = []
    for j, t in enumerate(["ombro", "joelho", "lombar", "pescoço", "fáscia plantar"]):
        x = j * 336
        p.append(f'<rect x="{x}" y="0" width="316" height="56" rx="28" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
        rs.append(rot(x, 14, t, w=316, tam=21, cor=TINTA, peso=700, alinha="center"))
    for k, (b, t) in enumerate([("fita falsa", "não foi melhor"), ("outras intervenções", "não foi melhor")]):
        x = k * 844
        p.append(caixa(x, 90, 820, 150, FOSF, FOSF_T, esp=2, rx=16))
        p.append(f'<rect x="{x + 24}" y="130" width="200" height="70" rx="10" fill="{GLIC}"/>')
        rs += [rot(x + 24, 150, "fita elástica", w=200, tam=20, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 230, 140, "=", w=60, tam=40, cor=TINTA, peso=700, alinha="center"),
               rot(x + 300, 132, b, w=260, tam=23, cor=TINTA, peso=700, lh=1.15), rot(x + 560, 140, t, w=240, tam=22, cor=FOSF, peso=700, alinha="right")]
    rs.append(rot(0, 264, "efeitos pequenos, provavelmente sem importância clínica", w=1664, tam=22, cor=TINTA, peso=700, alinha="center"))
    return slide("fita", 320, p, rs, eyebrow="Erro dois · a fita como proteção", titulo="A bandagem elástica na revisão brasileira",
                 destaque="Se o atleta gosta e ela não substitui nada, o dano é pequeno. O problema é quando ela entra no lugar do exercício.", destaque_cor="tinta",
                 fonte="J Physiother 2014")


def manual_89():
    """8.9: a mão sobre o ombro dispara uma resposta do sistema nervoso que abre uma janela curta; o que não faz, riscado."""
    p = [svg_abre(1664, 340, "Uma mão sobre o ombro dispara um estímulo que sobe ao sistema nervoso, periférico e central, e volta como modulação da dor: melhora de dor e amplitude por um tempo, uma janela para o movimento. Ao lado, riscado, o que não faz: colocar no lugar vértebra ou articulação; mudar a estrutura de um tendão"), defs(OXID)]
    rs = []
    p.append(f'<circle cx="90" cy="170" r="80" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    p.append(icone("t:hand-stop", 50, 130, 80, OXID))
    rs.append(rot(0, 264, "estímulo mecânico", w=180, tam=19, cor=TINTA, peso=700, alinha="center"))
    p.append(seta(180, 140, 330, 80, OXID, "m0", esp=4))
    p.append(caixa(340, 20, 340, 120, OXID, OXID, esp=0, rx=16))
    rs.append(rot(340, 42, "sistema nervoso periférico e central", w=340, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.2))
    p.append(seta(510, 150, 510, 196, OXID, "m0", esp=4))
    p.append(caixa(240, 206, 540, 120, OXID, OXID_T, esp=2, rx=16))
    rs += [rot(260, 222, "modula a dor", w=500, tam=24, cor=OXID, peso=700, alinha="center", serif=True),
           rot(260, 262, "dor e amplitude melhores por um tempo: uma janela para o movimento", w=500, tam=19, cor=TINTA, alinha="center", lh=1.2)]
    p.append(caixa(860, 0, 804, 340, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(884, 20, "O que não faz", w=760, tam=27, cor=FOSF, peso=700, serif=True))
    for j, t in enumerate(["“colocar no lugar” vértebra ou articulação", "mudar a estrutura de um tendão"]):
        y = 100 + j * 110
        p.append(icone("t:x", 884, y, 48, FOSF))
        rs.append(rot(950, y + 8, t, w=690, tam=23, cor=TINTA, peso=700, lh=1.2))
    return slide("manual", 340, p, rs, eyebrow="A terapia manual, com honestidade", titulo="Um efeito real, de curto prazo",
                 destaque="Justificar o uso por razões neurofisiológicas, não biomecânicas.", destaque_cor="tinta", fonte="Modelo de 2009, Man Ther")


def janela_89():
    """8.9: duas semanas de dor com janelas de alívio; numa, o exercício passa pela janela; na outra, a janela abre e fecha vazia."""
    p = [svg_abre(1664, 380, "Em esquema, duas faixas de dor ao longo de semanas. Na de cima, cada sessão abre uma janela de alívio de algumas horas e o exercício acontece dentro dela; a dor de base vai descendo. Na de baixo, a janela abre e fecha vazia, e a pessoa volta na semana seguinte para abrir a mesma janela; a dor de base não muda")]
    rs = []
    for k, (t, cor, desce) in enumerate([("exercício dentro da janela", OXID, True), ("janela vazia: volta para abrir a mesma", FOSF, False)]):
        y0 = k * 190
        rs.append(rot(0, y0 + 4, t, w=900, tam=22, cor=cor, peso=700))
        pts = []
        for s in range(4):
            x = 120 + s * 380
            base = y0 + 70 + (s * 22 if desce else 0)
            pts += [f"{x},{base}", f"{x + 10},{base + 70}", f"{x + 90},{base + 70}", f"{x + 110},{base}", f"{x + 380},{base}"]
            p.append(f'<rect x="{x + 10}" y="{y0 + 40}" width="80" height="130" fill="{cor}" opacity="0.12"/>')
            if desce:
                p.append(f'<rect x="{x + 22}" y="{base + 40}" width="56" height="26" rx="5" fill="{OXID}"/>')
        p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{cor}" stroke-width="4" stroke-linejoin="round"/>')
        rs.append(rot(0, y0 + 60, "dor", w=100, tam=18, cor=MUDO, alinha="right"))
    rs += [rot(1300, 4, "a base desce", w=360, tam=20, cor=OXID, peso=700, alinha="right"), rot(1300, 194, "a base não muda", w=360, tam=20, cor=FOSF, peso=700, alinha="right"),
           rot(120, 352, "■ exercício  ·  faixa clara: a janela de alívio, algumas horas  ·  esquema", w=1400, tam=18, cor=MUDO)]
    return slide("janela", 380, p, rs, eyebrow="A ideia da aula", titulo="O recurso passivo abre uma janela. O exercício é o que passa por ela.")


def caros_89():
    """8.9: a ordem dos adjuvantes caros, depois da carga, e as injeções como decisão médica à parte."""
    p = [svg_abre(1664, 320, "À esquerda, uma sequência: primeiro, um programa de carga bem feito, pelo tempo que o tecido pede; se não bastou, ondas de choque ou agulhamento como adjuvante, com estudos em algumas condições e evidência de qualidade variável. À direita, as injeções: decisão médica, com riscos, prazos e indicações próprias, tratadas na aula de analgesia do módulo clínico"), defs(MUDO)]
    rs = []
    p.append(caixa(0, 0, 440, 230, OXID, OXID, esp=0, rx=16))
    p.append(icone("t:barbell", 24, 24, 48, PAPEL))
    rs += [rot(24, 90, "1 · carga bem feita", w=400, tam=25, cor=PAPEL, peso=700, serif=True), rot(24, 136, "pelo tempo que o tecido pede", w=400, tam=21, cor=PAPEL)]
    p.append(seta(452, 115, 520, 115, MUDO, "m0", esp=3))
    rs.append(rot(446, 132, "não bastou?", w=80, tam=17, cor=MUDO, alinha="center", lh=1.1))
    p.append(caixa(532, 0, 440, 230, GLIC, GLIC_T, esp=2, rx=16))
    p.append(icone("t:bolt", 556, 24, 48, GLIC))
    rs += [rot(556, 90, "2 · ondas de choque, agulhamento", w=400, tam=24, cor=GLIC, peso=700, serif=True, lh=1.15),
           rot(556, 160, "adjuvante; estudos em algumas condições; qualidade variável", w=400, tam=19, cor=TINTA, lh=1.25)]
    p.append(caixa(1060, 0, 604, 230, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:stethoscope", 1084, 24, 48, TINTA))
    rs += [rot(1146, 30, "Injeções", w=480, tam=27, cor=TINTA, peso=700, serif=True),
           rot(1084, 96, "decisão médica, com riscos, prazos e indicações próprias", w=560, tam=21, cor=TINTA, lh=1.25),
           rot(1084, 166, "a aula de analgesia do módulo clínico", w=560, tam=19, cor=MUDO)]
    rs.append(rot(0, 268, "nenhum deles dispensa a carga", w=1664, tam=24, cor=TINTA, peso=700, alinha="center", serif=True))
    return slide("caros", 320, p, rs, eyebrow="Os recursos que custam mais", titulo="Nenhum deles dispensa a carga",
                 destaque="Quando o recurso alivia a dor, é a janela para carregar mais, não a licença para voltar sem ter carregado.", destaque_cor="tinta")


def contexto_89():
    """8.9: quatro fatores de contexto em volta da intervenção, com as setas de placebo e nocebo."""
    p = [svg_abre(1664, 380, "No centro, a intervenção: efeito específico mais efeito de contexto, somados. Em volta, quatro fatores: profissional e paciente, o que cada um traz, expectativa, crença, jeito; a relação, tempo, atenção, o mesmo profissional; o tratamento, explicação clara, sem palavras que assustam; o ambiente, privado, pontual, com seguimento. À direita, os dois sentidos: placebo, com explicação clara e atenção, ajuda; nocebo, com pressa e frases como sua coluna está desgastada, atrapalha")]
    rs = []
    p.append(caixa(380, 130, 420, 120, TINTA, TINTA, esp=0, rx=60))
    rs += [rot(380, 150, "a intervenção", w=420, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True), rot(380, 192, "efeito específico + contexto", w=420, tam=19, cor=PAPEL, alinha="center")]
    fat = [(0, 0, "Profissional e paciente", "expectativa, crença, jeito", OXID, OXID_T), (720, 0, "A relação", "tempo, atenção, o mesmo profissional", OXID, OXID_T),
           (0, 270, "O tratamento", "explicação clara, sem palavras que assustam", GLIC, GLIC_T), (720, 270, "O ambiente", "privado, pontual, com seguimento", GLIC, GLIC_T)]
    for x, y, t, d, cor, fundo in fat:
        p.append(caixa(x, y, 460, 110, cor, fundo, esp=2, rx=14))
        rs += [rot(x + 20, y + 14, t, w=420, tam=22, cor=cor, peso=700, serif=True), rot(x + 20, y + 54, d, w=420, tam=19, cor=TINTA, lh=1.2)]
        p.append(f'<line x1="{x + 230}" y1="{y + 110 if y == 0 else y}" x2="{590}" y2="{130 if y == 0 else 250}" stroke="{MUDO}" stroke-width="2"/>')
    for k, (t, d, cor, fundo, ic) in enumerate([("Placebo", "explicação clara, tempo, atenção: ajuda", OXID, OXID_T, "t:trending-up"),
                                                ("Nocebo", "pressa, “sua coluna está desgastada”: atrapalha", FOSF, FOSF_T, "t:trending-down")]):
        y = k * 196
        p.append(caixa(1260, y, 404, 184, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, 1284, y + 20, 44, cor))
        rs += [rot(1340, y + 26, t, w=300, tam=25, cor=cor, peso=700, serif=True), rot(1284, y + 84, d, w=356, tam=20, cor=TINTA, lh=1.25)]
    return slide("contexto", 380, p, rs, eyebrow="O ritual também tem efeito", titulo="Fatores de contexto: placebo e nocebo",
                 destaque="Usar o contexto para potencializar o que funciona; nunca para vender como tratamento o que só funciona pelo contexto.", destaque_cor="verm",
                 fonte="Man Ther 2016")


def reconhecer_89():
    """8.9: três sinais com o seu mini gráfico: medida parada, alívio que não passa do dia seguinte, programa travado."""
    p = [svg_abre(1664, 340, "Três cartões, cada um com um pequeno gráfico em esquema. A medida combinada não mudou em duas ou três semanas: uma linha reta. O alívio não passa do dia seguinte, sessão após sessão: um serrote que sempre volta ao mesmo nível. O programa ativo está parado: degraus que pararam de subir, o recurso ocupando o lugar da carga")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("A medida combinada não mudou", "em duas ou três semanas; a medida, não a sensação na sessão", FOSF, FOSF_T),
                                            ("O alívio não passa do dia seguinte", "sessão após sessão", GLIC, GLIC_T),
                                            ("O programa ativo está parado", "o recurso ocupa o lugar da carga", GLIC, GLIC_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 340, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 20, t, w=W - 48, tam=24, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 24, 256, d, w=W - 48, tam=20, cor=TINTA, lh=1.25)]
        p.append(f'<line x1="{x + 40}" y1="230" x2="{x + W - 40}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<polyline points="60,170 180,168 300,171 420,169 488,170" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    for s in range(4):
        p.append(f'<circle cx="{60 + s * 140}" cy="170" r="8" fill="{FOSF}"/>')
    x0 = W + 40
    pts = []
    for s in range(4):
        x = x0 + 50 + s * 112
        pts += [f"{x},120", f"{x + 10},200", f"{x + 40},200", f"{x + 80},120"]
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GLIC}" stroke-width="4" stroke-linejoin="round"/>')
    x0 = 2 * (W + 40)
    p.append(f'<polyline points="{x0 + 50},210 {x0 + 140},210 {x0 + 140},180 {x0 + 230},180 {x0 + 230},150 {x0 + 488},150" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    p.append(icone("t:hand-stop", x0 + 400, 100, 40, GLIC))
    return slide("reconhecer", 340, p, rs, eyebrow="De forma objetiva", titulo="Três sinais de que não está funcionando",
                 destaque="Qualquer um dos três: rever o plano, não aumentar as sessões com o mesmo recurso.", destaque_cor="tinta")


def quem_89():
    """8.9: quatro cartões de papel, cada um com o seu pedaço da régua."""
    p = [svg_abre(1664, 300, "Quatro cartões, cada um com uma parte da régua. Fisioterapia: escolhe o recurso e escreve as quatro respostas no plano. Médico: medicação e injeções; nada de sessões sem objetivo. Preparação física: mantém o treino que não dói. Atleta: pergunta, o que isso muda no meu problema?")]
    rs = []
    W = 386
    for k, (ic, t, d, cor, fundo) in enumerate([("t:writing", "Fisioterapia", "escolhe o recurso e escreve as quatro respostas no plano", OXID, OXID_T),
                                                ("t:stethoscope", "Médico", "medicação e injeções; nada de sessões sem objetivo", AZUL, AZUL_T),
                                                ("t:barbell", "Preparação física", "mantém o treino que não dói", GLIC, GLIC_T),
                                                ("t:message-circle", "Atleta", "pergunta: “o que isso muda no meu problema?”", TINTA, PAPEL)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 300, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 24, 52, cor))
        rs += [rot(x + 24, 100, t, w=W - 48, tam=26, cor=cor, peso=700, serif=True), rot(x + 24, 150, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    return slide("quem", 300, p, rs, eyebrow="Quem faz o quê", titulo="Cada um com uma parte da régua")

# ---------------------------------------------------------------- aplicação

LICOES = {"08-01": [tatame_81, roteiro_81, bandeiras_81, sinss_81, cif_81, hipoteses_81, laudo_81, vieses_81, quem_81],
          "08-02": [folha_82, piso_82, resposta_82, saidas_82, portas_82, custo_82, naoabre_82, degraus_82, quem_82, ficha_82],
          "08-03": [bomba_83, desmontar_83, musculo_83, magnitude_83, desuso_83, repouso_83, relogios_83, pratica_83],
          "08-04": [planilha_84, regra_84, variavel_84, degrau_84, degrauabaixo_84, registro_84, principios_84, cinco_84],
          "08-05": [caso_85, expectativa_85, antes_85, semanas_85, forca_85, corrida_85, relogios_85, ultima_85, quem_85],
          "08-06": [macas_86, roteiro_86, resolvido_86, criterios_86, sprint_86, doha_86, medir_86, holmich_86, manter_86, armadilhas_86],
          "08-07": [um3_87, ensaio_87, programa_87, ortese_87, juntar_87, oito_87, paass_87, barato_87, erros_87, quem_87],
          "08-08": [paro_88, alerta_88, natacao_88, mod_ombro_88, cirurgia_88, meio_88, flexao_88, risco_88, mod_coluna_88, custo_88],
          "08-09": [perguntas_89, aparelho_89, fita_89, manual_89, janela_89, caros_89, contexto_89, reconhecer_89, quem_89]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
