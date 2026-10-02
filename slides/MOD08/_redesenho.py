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

# ---------------------------------------------------------------- aplicação

LICOES = {"08-01": [tatame_81, roteiro_81, bandeiras_81, sinss_81, cif_81, hipoteses_81, laudo_81, vieses_81, quem_81],
          "08-02": [folha_82, piso_82, resposta_82, saidas_82, portas_82, custo_82, naoabre_82, degraus_82, quem_82, ficha_82],
          "08-03": [bomba_83, desmontar_83, musculo_83, magnitude_83, desuso_83, repouso_83, relogios_83, pratica_83]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
