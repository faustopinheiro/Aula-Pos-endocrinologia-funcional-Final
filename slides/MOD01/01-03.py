"""Spec do deck 1.3 (refeito no modelo dos desenhos). Gera 01-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

TRACO = ' stroke-dasharray="10 8"'

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
CINZA = "#C9CFD4"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"
def carimbo(x, y, w, h, t, cor, rs, ang=-8, tam=34):
    rs.append(rot(x, y + h / 2 - tam * 0.62, t, w=w, tam=tam, cor=cor, peso=700, alinha="center", serif=True))
    return f'<g transform="rotate({ang} {x + w / 2} {y + h / 2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{cor}" stroke-width="6"/></g>'

# 1. as duas receitas incompletas
p = [svg_abre(1664, 470, "Duas receitas lado a lado, uma diz tome um remédio para pressão e a outra diz faça exercício; as duas com os campos em branco e o carimbo incompleta")]
rs = []
campos = ["qual?", "quanto?", "quantas vezes?", "até quando?", "quando volta?"]
for k, (x, frase) in enumerate([(0, "“Tome um remédio para pressão.”"), (872, "“Faça exercício.”")]):
    p.append(caixa(x, 0, 792, 470, CINZA, CARTAO, esp=3, rx=16))
    p.append(f'<rect x="{x}" y="0" width="792" height="16" rx="8" fill="{AZUL}"/>')
    p.append(icone("h:medical-records", x + 30, 40, 60, AZUL))
    rs.append(rot(x + 110, 52, frase, w=660, tam=34, cor=TINTA, peso=700, serif=True))
    for j, c in enumerate(campos):
        y = 150 + j * 60
        rs.append(rot(x + 40, y, c, w=240, tam=24, cor=MUDO, peso=600))
        p.append(f'<line x1="{x + 260}" y1="{y + 32}" x2="{x + 480}" y2="{y + 32}" stroke="{CINZA}" stroke-width="3"{TRACO}/>')
    p.append(carimbo(x + 510, 250, 250, 90, "incompleta", FOSF, rs))
p.append("</svg>")
S.append({"id": "receita", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Para começar", "titulo": "A receita que ninguém escreveria",
          "destaque": "Conselho não obriga ninguém a nada: nem o paciente a fazer, nem o profissional a acompanhar.", "destaque_cor": "verm"})

# 2. a curva de risco
p = [svg_abre(1664, 520, "Curva do risco de morrer que despenca nos primeiros minutos diários de atividade e achata depois; uma faixa marca 30 a 40 minutos por dia; o primeiro trecho em vermelho, sair do zero")]
p.append(f'<rect x="560" y="20" width="150" height="420" fill="{OXID}" opacity="0.15"/>')
p.append(f'<path d="M100 40 C 200 270, 360 350, 620 380 C 900 405, 1200 412, 1560 418" fill="none" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<path d="M100 40 C 130 120, 170 190, 230 250" fill="none" stroke="{FOSF}" stroke-width="14" stroke-linecap="round"/>')
p.append(f'<line x1="80" y1="442" x2="1580" y2="442" stroke="{MUDO}" stroke-width="3"/><line x1="82" y1="10" x2="82" y2="442" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<circle cx="100" cy="40" r="14" fill="{FOSF}"/>')
p.append(icone("t:user", 1000, 170, 70, AZUL))
p.append(icone("t:bed", 1080, 170, 70, AZUL))
rs = [rot(260, 110, "sair do zero: a maior queda do risco", w=420, tam=28, cor=FOSF, peso=700, lh=1.2, serif=True),
      rot(540, 40, "30 a 40 min/dia", w=190, tam=24, cor=OXID, peso=700, alinha="center", lh=1.1),
      rot(900, 330, "de muito para muitíssimo: ganho pequeno", w=600, tam=24, cor=MUDO, peso=600, alinha="center"),
      rot(1170, 150, "mais de 44 mil adultos: 30 a 40 minutos por dia de atividade moderada a vigorosa diminuíram bastante o risco de muitas horas sentado", w=494, tam=22, cor=AZUL, peso=600, lh=1.3),
      rot(80, 456, "minutos por dia de atividade moderada a vigorosa, medidos com acelerômetro", w=1500, tam=22, cor=MUDO, alinha="center"),
      rot(96, -6, "risco de morrer", w=300, tam=22, cor=MUDO)]
p.append("</svg>")
S.append({"id": "curva", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A forma da curva", "titulo": "O maior ganho está em sair do zero",
          "fonte": "Ekelund e colaboradores, BMJ 2019 e Br J Sports Med 2020 · esquema, sem valores medidos"})

# 3. 26 doenças em sete grupos
grupos = [("Cabeça", 4, "depressão, ansiedade", "h:mental-health"),
          ("Cérebro", 3, "demência, Parkinson, esclerose múltipla", "t:brain"),
          ("Metabolismo", 6, "obesidade, diabetes 1 e 2, colesterol, ovários policísticos", "t:droplet"),
          ("Coração", 5, "hipertensão, coronária, insuficiência cardíaca, derrame", "t:heartbeat"),
          ("Pulmão", 3, "DPOC, asma", "h:lungs"),
          ("Músculos e ossos", 4, "artrose, osteoporose, dor lombar, artrite reumatoide", "t:stretching"),
          ("Câncer", 1, "", "t:shield")]
p = [svg_abre(1664, 580, "Sete colunas de quadradinhos, uma por grupo de doenças, somando 26: cabeça 4, cérebro 3, metabolismo 6, coração 5, pulmão 3, músculos e ossos 4, câncer 1")]
rs = []
cores = [AZUL, AZUL, GLIC, FOSF, OXID, GLIC, FOSF]
for k, ((t, n, ex, ic), c) in enumerate(zip(grupos, cores)):
    x = 240 + k * 204
    for j in range(n):
        p.append(f'<rect x="{x + 30}" y="{330 - (j + 1) * 46}" width="120" height="38" rx="8" fill="{c}" opacity="0.85"/>')
    rs.append(rot(x + 30, 330 - n * 46 - 42, str(n), w=120, tam=30, cor=c, peso=700, alinha="center", serif=True))
    p.append(icone(ic, x + 64, 346, 52, c))
    rs.append(rot(x, 408, t, w=180, tam=24, cor=c, peso=700, alinha="center", lh=1.1))
    if ex:
        rs.append(rot(x, 474, ex, w=180, tam=19, cor=TINTA, alinha="center", lh=1.25))
p.append(f'<line x1="250" y1="332" x2="1660" y2="332" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs += [rot(0, 60, "26", w=220, tam=150, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(0, 260, "doenças crônicas com evidência para prescrever exercício como terapia", w=220, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.25)]
S.append({"id": "26-doencas", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Com que direito se chama de tratamento", "titulo": "Exercício tem evidência como terapia em quase toda a clínica",
          "fonte": "Pedersen e Saltin, Scand J Med Sci Sports 2015"})

# 4. o cartaz com três adesivos
p = [svg_abre(1664, 540, "Um cartaz com a frase exercício é remédio e três adesivos de atenção colados por cima: o efeito varia, não substitui por decreto, prescrever é assumir")]
p.append(f'<rect x="200" y="20" width="1264" height="500" rx="12" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(icone("t:pill", 260, 60, 110, AZUL))
rs = [rot(400, 70, "“Exercício é remédio”", w=1000, tam=72, cor=AZUL, peso=700, serif=True)]
adesivos = [(120, 230, -6, "O efeito varia", "muito, entre doenças e entre desfechos: reabilitação cardíaca não é fibrose cística", GLIC, GLIC_T),
            (620, 250, 3, "Não substitui por decreto", "ninguém tira insulina, betabloqueador ou antidepressivo porque a pessoa começou a treinar", FOSF, FOSF_T),
            (1120, 225, -3, "Prescrever é assumir", "dose, acompanhamento, efeito colateral, reavaliação", OXID, OXID_T)]
for (x, y, a, t, tx, c, ct) in adesivos:
    p.append(f'<g transform="rotate({a} {x + 210} {y + 130})"><rect x="{x}" y="{y}" width="420" height="260" rx="10" fill="{ct}" stroke="{c}" stroke-width="4"/>'
             f'<rect x="{x + 150}" y="{y - 14}" width="120" height="28" fill="{CINZA}" opacity="0.7"/></g>')
    p.append(icone("t:alert-triangle", x + 24, y + 26, 44, c))
    rs.append(rot(x + 80, y + 30, t, w=320, tam=28, cor=c, peso=700, serif=True, lh=1.1))
    rs.append(rot(x + 24, y + 100, tx, w=372, tam=22, cor=TINTA, lh=1.3))
p.append("</svg>")
S.append({"id": "slogan", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O cuidado com o slogan", "titulo": "O slogan certo precisa de três ressalvas"})

# 5. o receituário com sete campos
p = [svg_abre(1664, 600, "Um receituário com sete campos preenchidos: frequência, intensidade, tempo, tipo, volume, progressão e, destacado, quem acompanha e quando volta")]
p.append(caixa(0, 0, 1060, 600, CINZA, CARTAO, esp=3, rx=16))
p.append(f'<rect x="0" y="0" width="1060" height="16" rx="8" fill="{OXID}"/>')
campos = [("Frequência", "quantas vezes por semana"), ("Intensidade", "quão forte, e medida como"), ("Tempo", "quantos minutos por sessão"),
          ("Tipo", "o que a pessoa tolera e aceita fazer"), ("Volume", "o total da semana, com força incluída"), ("Progressão", "como aumenta, e quando"),
          ("Quem acompanha", "e quando é a reavaliação")]
rs = []
for j, (c, q) in enumerate(campos):
    y = 36 + j * 72
    ult = j == 6
    if ult:
        p.append(f'<rect x="16" y="{y - 10}" width="1028" height="72" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(40, y + 8, c, w=300, tam=28, cor=FOSF if ult else OXID, peso=700, serif=True))
    rs.append(rot(360, y + 12, q, w=660, tam=24, cor=TINTA))
    if not ult:
        p.append(f'<line x1="40" y1="{y + 60}" x2="1020" y2="{y + 60}" stroke="{GRADE}" stroke-width="2"/>')
rs.append(rot(40, 556, "os seis primeiros vêm da sigla em inglês; o sétimo quase nunca aparece escrito", w=980, tam=20, cor=MUDO))
for k, (ic, t, tx, c) in enumerate([("t:barbell", "Força", "duas vezes por semana, com carga e progressão: a parte mais esquecida", GLIC),
                                     ("t:calendar", "Progressão", "“aumente conforme se sentir bem” não é progressão: é um número com uma data", OXID),
                                     ("t:run", "Tipo", "com sobrepeso, artrose ou muito descondicionado: baixo impacto primeiro", AZUL)]):
    y = k * 204
    p.append(caixa(1110, y, 554, 188, c, CARTAO, esp=3, rx=16))
    p.append(icone(ic, 1130, y + 22, 50, c))
    rs.append(rot(1196, y + 30, t, w=440, tam=28, cor=c, peso=700, serif=True))
    rs.append(rot(1130, y + 90, tx, w=510, tam=22, cor=TINTA, lh=1.3))
p.append("</svg>")
S.append({"id": "sete-campos", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A receita completa", "titulo": "Uma prescrição de verdade tem sete campos"})

# 6. as âncoras de intensidade
p = [svg_abre(1664, 560, "Um medidor de frequência cardíaca travado por um comprimido de betabloqueador; ao lado, três âncoras: a escala de esforço de zero a dez com as faixas moderada e vigorosa, o teste da fala, e o laudo do teste de esforço feito com os remédios em uso")]
p.append(caixa(0, 0, 420, 560, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:heartbeat", 60, 90, 150, MUDO))
p.append(icone("t:pill", 200, 190, 110, FOSF))
p.append(f'<line x1="50" y1="360" x2="370" y2="80" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
rs = [rot(20, 380, "zona de frequência cardíaca com betabloqueador", w=380, tam=26, cor=FOSF, peso=700, serif=True, lh=1.2),
      rot(20, 470, "o remédio segura o coração; o número não reflete o esforço", w=380, tam=22, cor=TINTA, lh=1.3)]
# escala 0 a 10
x0, x1 = 480, 1664
p.append(f'<rect x="{x0}" y="60" width="{x1 - x0}" height="50" rx="25" fill="{GRADE}"/>')
passo = (x1 - x0) / 10
p.append(f'<rect x="{x0 + 5 * passo}" y="60" width="{2 * passo}" height="50" fill="{GLIC}"/>')
p.append(f'<rect x="{x0 + 7 * passo}" y="60" width="{2 * passo}" height="50" fill="{FOSF}"/>')
for n in range(11):
    rs.append(rot(x0 + n * passo - 20, 118, str(n), w=40, tam=20, cor=MUDO, alinha="center"))
rs += [rot(x0, 10, "Esforço de 0 a 10", w=500, tam=28, cor=TINTA, peso=700, serif=True),
       rot(x0 + 5 * passo, 70, "moderado", w=2 * passo, tam=22, cor=PAPEL, peso=700, alinha="center"),
       rot(x0 + 7 * passo, 70, "vigoroso", w=2 * passo, tam=22, cor=PAPEL, peso=700, alinha="center")]
# teste da fala
rs.append(rot(x0, 180, "Teste da fala", w=500, tam=28, cor=TINTA, peso=700, serif=True))
p.append(icone("h:walking", x0, 230, 90, GLIC))
p.append(f'<rect x="{x0 + 110}" y="236" width="380" height="80" rx="24" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
rs.append(rot(x0 + 110, 250, "conversa, com alguma dificuldade", w=380, tam=22, cor=GLIC, peso=700, alinha="center", lh=1.2))
p.append(icone("h:running", x0 + 560, 230, 90, FOSF))
p.append(f'<rect x="{x0 + 670}" y="236" width="380" height="80" rx="24" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
rs.append(rot(x0 + 670, 250, "não termina a frase inteira…", w=380, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
# teste de esforço
p.append(caixa(x0, 380, x1 - x0, 180, OXID, OXID_T, esp=3, rx=16))
p.append(icone("t:clipboard-check", x0 + 30, 420, 90, OXID))
rs += [rot(x0 + 150, 405, "Teste de esforço feito com os remédios em uso", w=1000, tam=28, cor=OXID, peso=700, serif=True),
       rot(x0 + 150, 460, "se a pessoa tem um, use os números dele: é a melhor âncora que existe para ela", w=1000, tam=24, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "intensidade", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O campo que mais gera erro", "titulo": "A intensidade se ancora no esforço, não no pulso",
          "fonte": "Faixas de esforço da diretriz da Organização Mundial da Saúde, 2020"})

# 7. três caminhos na triagem
p = [svg_abre(1664, 580, "Uma pessoa na porta de três caminhos: em cima, liberar tudo sem perguntar leva a uma aula de alta intensidade; embaixo, exigir cardiologista para caminhar esbarra num muro de três meses; no meio, três perguntas levam a começar hoje"), defs(FOSF, OXID, GLIC)]
p.append(icone("h:man", 0, 200, 150, TINTA))
p.append(f'<path d="M170 250 C 320 250, 360 70, 560 70 L 1180 70" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m0)"/>')
p.append(f'<path d="M170 290 L 1180 290" fill="none" stroke="{OXID}" stroke-width="8" marker-end="url(#m1)"/>')
p.append(f'<path d="M170 330 C 320 330, 360 490, 560 490 L 960 490" fill="none" stroke="{GLIC}" stroke-width="6"/>')
p.append(f'<rect x="970" y="430" width="36" height="120" fill="{GLIC}"/>')
p.append(icone("t:hourglass", 1030, 450, 70, GLIC))
p.append(icone("t:flame", 1210, 30, 80, FOSF))
p.append(caixa(560, 220, 400, 140, OXID, OXID_T, esp=3, rx=16))
p.append(icone("t:flag", 1210, 250, 80, OXID))
rs = [rot(560, 20, "liberar tudo sem perguntar", w=600, tam=26, cor=FOSF, peso=700),
      rot(1310, 30, "vinte anos parado, aula de alta intensidade na segunda semana", w=354, tam=22, cor=FOSF, peso=600, lh=1.25),
      rot(580, 232, "três perguntas", w=360, tam=24, cor=OXID, peso=700, alinha="center"),
      rot(580, 270, "já é ativa? tem doença ou sintoma? que intensidade pretende?", w=360, tam=20, cor=TINTA, alinha="center", lh=1.25),
      rot(1310, 250, "sem sintoma, sem doença conhecida, vai caminhar: começa hoje", w=354, tam=24, cor=OXID, peso=700, lh=1.25, serif=True),
      rot(560, 506, "exigir cardiologista para caminhar", w=400, tam=26, cor=GLIC, peso=700),
      rot(1110, 460, "três meses de espera, e a pessoa não começa nunca", w=554, tam=22, cor=GLIC, peso=600, lh=1.25)]
p.append("</svg>")
S.append({"id": "triagem", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Antes de começar", "titulo": "A triagem erra para os dois lados",
          "fonte": "Colégio Americano de Medicina do Esporte, revisão das recomendações de triagem, 2015"})

# 8. a prescrição perfeita e a feita
p = [svg_abre(1664, 580, "Duas prescrições: uma perfeita e intocada, com efeito zero; outra modesta, cheia de marcas de feito, com uma medalha; ao lado, cinco coisas que ajudam e a versão menor para a semana ruim")]
rs = []
for k, (x, tit, feito, c) in enumerate([(0, "a ideal", False, MUDO), (400, "a possível", True, OXID)]):
    p.append(caixa(x, 40, 360, 440, CINZA if not feito else OXID, CARTAO, esp=3, rx=16))
    rs.append(rot(x, 0, tit, w=360, tam=28, cor=c, peso=700, alinha="center", serif=True))
    n = 8 if not feito else 4
    for j in range(n):
        y = 70 + j * (48 if not feito else 90)
        p.append(f'<rect x="{x + 30}" y="{y}" width="34" height="34" rx="6" fill="none" stroke="{c}" stroke-width="3"/>')
        p.append(f'<line x1="{x + 84}" y1="{y + 17}" x2="{x + 330}" y2="{y + 17}" stroke="{CINZA}" stroke-width="6" stroke-linecap="round"/>')
        if feito:
            p.append(icone("t:check", x + 26, y - 6, 44, OXID))
rs.append(rot(0, 496, "efeito zero, e sensação de fracasso", w=360, tam=22, cor=MUDO, alinha="center", lh=1.25))
p.append(icone("t:medal", 690, 400, 80, GLIC))
rs.append(rot(400, 496, "vale mais do que a ideal não feita", w=360, tam=22, cor=OXID, peso=700, alinha="center", lh=1.25))
dicas = [("t:arrow-down-right", "comece abaixo do que ela acha que consegue"), ("t:repeat", "pendure na rotina que já existe"),
         ("t:eye-check", "acompanhe de perto nas primeiras semanas"), ("t:ruler-measure", "meça função, não só peso"), ("t:hand-stop", "não use medo")]
for j, (ic, t) in enumerate(dicas):
    y = 10 + j * 72
    p.append(icone(ic, 860, y, 46, FOSF if j == 4 else OXID))
    rs.append(rot(924, y + 8, t, w=740, tam=26, cor=TINTA, peso=600))
p.append(caixa(860, 390, 804, 170, GLIC, GLIC_T, esp=4, rx=18))
p.append(icone("t:battery-1", 884, 420, 60, GLIC))
rs += [rot(964, 410, "a versão menor, combinada no começo", w=680, tam=28, cor=GLIC, peso=700, serif=True),
       rot(964, 460, "sem ela, a semana ruim não vira semana pequena: vira abandono", w=680, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "adesao", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde a prescrição morre", "titulo": "O exercício feito vale mais do que o ideal não feito"})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "Você prescreveu ou aconselhou?",
          "regras": ["Tem número? Minuto, dia, série ou carga.", "Tem data de volta? Sem reavaliação, ninguém sabe se a dose estava certa.",
                     "Tem uma versão menor combinada para a semana ruim?"],
          "quem": "Falar a recomendação e explicar por que ela existe é de todos. Montar a prescrição individual, com carga e progressão, é de quem prescreve treino ou conduz a reabilitação.",
          "proxima": "150 minutos e o que ninguém lê na diretriz"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-03.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-03.json"), "w"), ensure_ascii=False, indent=1)
print("01-03.json:", len(S), "slides")
