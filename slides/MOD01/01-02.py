"""Spec do deck 1.2 (refeito no modelo dos desenhos). Gera 01-02.json ao lado deste arquivo."""
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
def balao(x, y, w, h, cor, fundo, rabo="esq"):
    """Balão de conversa com o rabinho embaixo, à esquerda ou à direita."""
    bx = x + 40 if rabo == "esq" else x + w - 70
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="{fundo}" stroke="{cor}" stroke-width="3"/>'
            f'<path d="M{bx} {y + h - 2} L{bx + 6} {y + h + 30} L{bx + 36} {y + h - 2}" fill="{fundo}" stroke="{cor}" stroke-width="3" stroke-linejoin="round"/>'
            f'<line x1="{bx + 2}" y1="{y + h - 1.5}" x2="{bx + 34}" y2="{y + h - 1.5}" stroke="{fundo}" stroke-width="5"/>')

# 1. três mensagens e o que cada uma custa
p = [svg_abre(1664, 500, "Três balões de mensagem com os pedidos da semana; cada um aponta para o que custa ao corpo: a canela, seis quilos em três semanas, sete dias sem pausa"), defs(FOSF)]
msgs = [("h:running", "“A maratona é daqui a cinco semanas, a canela está doendo, mas eu não vou desistir. Me ajuda a chegar lá.”", "t:bolt", "a canela"),
        ("t:scale", "“Preciso bater o peso da categoria. Faltam seis quilos e a pesagem é em três semanas.”", "t:hourglass", "6 kg em 3 semanas"),
        ("t:calendar", "“Quando eu não treino eu fico péssima. Me passa um treino para os sete dias.”", "t:battery-1", "nenhum dia de pausa")]
rs = [rot(1180, 0, "o que custa ao corpo", w=484, tam=24, cor=FOSF, peso=700, alinha="center")]
for i, (ic, t, ic2, custo) in enumerate(msgs):
    y = 40 + i * 150
    p.append(icone(ic, 0, y + 20, 90, AZUL))
    p.append(balao(120, y, 900, 110, AZUL, AZUL_T))
    rs.append(rot(150, y + 16, t, w=840, tam=26, cor=TINTA, peso=500, lh=1.3))
    p.append(seta(1040, y + 55, 1150, y + 55, FOSF, "m0", esp=4))
    p.append(caixa(1180, y + 10, 484, 90, FOSF, FOSF_T, esp=3, rx=45))
    p.append(icone(ic2, 1210, y + 30, 50, FOSF))
    rs.append(rot(1280, y + 38, custo, w=370, tam=28, cor=FOSF, peso=700, serif=True))
p.append("</svg>")
S.append({"id": "mensagens", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Três mensagens da semana", "titulo": "Nenhum desses pedidos é irracional",
          "destaque": "Objetivos legítimos de adultos, e cada um custa alguma coisa ao corpo. O conflito aqui é de valores, não técnico."})

# 2. a curva do benefício e o guerreiro de fim de semana
p = [svg_abre(1664, 470, "Curva do benefício do exercício, subindo rápido no começo e achatando depois, com a área de acordo pintada; ao lado, duas semanas, uma com treino espalhado e outra concentrada no fim de semana, com redução de mortalidade parecida")]
curva = "M80 400 C 170 180, 330 110, 620 85 C 820 70, 1000 62, 1080 60"
p.append(f'<path d="{curva} L1080 400 Z" fill="{OXID}" opacity="0.14"/>')
p.append(f'<path d="{curva}" fill="none" stroke="{OXID}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<path d="M80 400 C 120 300, 160 236, 210 195" fill="none" stroke="{FOSF}" stroke-width="14" stroke-linecap="round"/>')
p.append(f'<line x1="60" y1="402" x2="1100" y2="402" stroke="{MUDO}" stroke-width="3"/><line x1="62" y1="30" x2="62" y2="402" stroke="{MUDO}" stroke-width="3"/>')
rs = [rot(230, 230, "sair do zero: o maior ganho por minuto", w=380, tam=26, cor=FOSF, peso=700, lh=1.2),
      rot(640, 110, "mais volume: continua subindo, mais devagar", w=440, tam=24, cor=OXID, peso=600, lh=1.2),
      rot(420, 300, "zona de acordo", w=400, tam=36, cor=OXID, peso=700, alinha="center", serif=True),
      rot(60, 412, "quanto se treina", w=1040, tam=22, cor=MUDO, alinha="center"),
      rot(0, -8, "benefício", w=200, tam=22, cor=MUDO)]
# duas semanas
dias = "STQQSSD"
for r_, (nome, cheios, cor) in enumerate([("espalhado na semana", {0, 2, 4}, OXID), ("guerreiro de fim de semana", {5, 6}, GLIC)]):
    y = 90 + r_ * 170
    rs.append(rot(1200, y - 44, nome, w=464, tam=24, cor=cor, peso=700))
    for d in range(7):
        x = 1200 + d * 64
        p.append(f'<rect x="{x}" y="{y}" width="52" height="52" rx="8" fill="{cor if d in cheios else CARTAO}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(x, y + 60, dias[d], w=52, tam=18, cor=MUDO, alinha="center"))
p.append("</svg>")
rs.append(rot(1180, 380, "redução de mortalidade parecida", w=484, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
S.append({"id": "acordo", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A boa notícia", "titulo": "Na maior parte do caminho, treinar mais é ter mais saúde",
          "fonte": "Curva: esquema, sem valores medidos · semanas: O'Donovan e colaboradores, JAMA Intern Med 2017",
          "destaque": "A primeira decisão: o que essa pessoa quer constrói margem ou gasta margem?"})

# 3. o sermão para quem está em acordo
p = [svg_abre(1664, 500, "À esquerda, a curva do benefício com um corredor na parte que ainda sobe; à direita, um profissional falando cortisol, excesso e overtraining; embaixo, o trabalho de facilitar em quatro partes"), defs(FOSF)]
mini = "M40 330 C 110 170, 220 110, 420 92 C 540 84, 620 80, 680 78"
p.append(f'<path d="{mini} L680 330 Z" fill="{OXID}" opacity="0.12"/>')
p.append(f'<path d="{mini}" fill="none" stroke="{OXID}" stroke-width="7" stroke-linecap="round"/>')
p.append(f'<line x1="30" y1="332" x2="700" y2="332" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<circle cx="190" cy="148" r="18" fill="{OXID}" stroke="{PAPEL}" stroke-width="4"/>')
p.append(icone("h:running", 150, 30, 80, OXID))
p.append(icone("h:doctor", 1470, 150, 170, FOSF))
for k, t in enumerate(["“cuidado com o cortisol”", "“isso é excesso”", "“você está em overtraining”"]):
    y = 20 + k * 100
    p.append(balao(860, y, 520, 76, FOSF, FOSF_T, rabo="dir"))
p.append(seta(840, 160, 740, 160, FOSF, "m0", esp=4))
rs = [rot(240, 170, "30 km por semana, dorme bem, feliz com o treino", w=440, tam=24, cor=OXID, peso=700, lh=1.25),
      rot(40, 345, "ainda na parte da curva que sobe", w=660, tam=22, cor=MUDO, alinha="center")]
for k, t in enumerate(["“cuidado com o cortisol”", "“isso é excesso”", "“você está em overtraining”"]):
    rs.append(rot(860, 20 + k * 100 + 20, t, w=520, tam=26, cor=FOSF, peso=700, alinha="center"))
p.append(caixa(0, 390, 1664, 110, OXID, OXID_T, esp=3, rx=20))
rs.append(rot(30, 414, "o trabalho aqui: facilitar", w=400, tam=30, cor=OXID, peso=700, serif=True, lh=1.2))
for k, (ic, t) in enumerate([("t:road-sign", "tirar pedra do caminho"), ("t:adjustments-horizontal", "ajustar"), ("t:checklist", "organizar"), ("t:shield-check", "proteger o que funciona")]):
    x = 440 + k * 305
    p.append(icone(ic, x, 417, 56, OXID))
    rs.append(rot(x + 66, 425, t, w=230, tam=22, cor=TINTA, peso=600, lh=1.2))
p.append("</svg>")
S.append({"id": "erro-sermao", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O erro que ninguém nomeia", "titulo": "Tratar acordo como se fosse conflito",
          "destaque": "O conflito é a exceção que pede método, não a regra que pede sermão."})

# 4. os cinco lugares em volta da pessoa
p = [svg_abre(1664, 480, "Uma pessoa no centro e cinco lugares em volta, ligados a ela: energia, peso e estética, competir machucado, volume e calendário, identidade")]
cx, cy = 832, 240
lugares = [("Energia", "comer menos e treinar igual ou mais", "t:flame", FOSF, FOSF_T),
           ("Peso e estética", "está no regulamento: reduzir dano, não condenar", "t:scale", GLIC, GLIC_T),
           ("Competir machucado", "a volta decidida pelo calendário, não pelo tecido", "h:bandaged", FOSF, FOSF_T),
           ("Volume e calendário", "o corpo paga por acúmulo, não por sessão", "t:calendar", GLIC, GLIC_T),
           ("Identidade", "treinar é quem a pessoa é", "t:id", OXID, OXID_T)]
pos = []
for k in range(5):
    a = math.radians(-90 + k * 72)
    pos.append((cx + 600 * math.cos(a), cy + 180 * math.sin(a)))
for (x, y) in pos:
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{CINZA}" stroke-width="4"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="90" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
p.append(icone("h:person", cx - 55, cy - 58, 110, TINTA))
rs = []
for (t, x_, ic, c, ct), (x, y) in zip(lugares, pos):
    bx, by = x - 215, y - 58
    p.append(caixa(bx, by, 430, 118, c, ct, esp=3 if t != "Identidade" else 5, rx=18))
    p.append(icone(ic, bx + 20, by + 16, 52, c))
    rs.append(rot(bx + 86, by + 14, t, w=330, tam=28, cor=c, peso=700, serif=True))
    rs.append(rot(bx + 86, by + 54, x_, w=330, tam=21, cor=TINTA, lh=1.25))
p.append("</svg>")
S.append({"id": "cinco-lugares", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde o conflito aparece", "titulo": "O conflito aparece sempre nos mesmos cinco lugares",
          "destaque": "Antes de retirar, redistribua. Retirar é a conduta mais cara que existe.", "destaque_cor": "petr"})

# 5. o conflito com atraso
p = [svg_abre(1664, 540, "Linha do tempo: nas primeiras semanas a linha do retorno sobe, mais leve, rende mais, elogio; o custo acumulado cresce devagar, e meses depois aparece em fratura, menstruação que sumiu, cansaço e humor")]
p.append(f'<rect x="60" y="20" width="560" height="400" rx="16" fill="{OXID_T}"/>')
p.append(f'<rect x="1000" y="20" width="664" height="400" rx="16" fill="{FOSF_T}"/>')
p.append(f'<line x1="60" y1="420" x2="1640" y2="420" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M80 330 C 250 250, 420 160, 600 120 C 780 90, 880 150, 1000 260 C 1150 380, 1300 400, 1620 400" fill="none" stroke="{OXID}" stroke-width="7" stroke-linecap="round"/>')
p.append(f'<path d="M80 395 C 400 390, 700 370, 900 320 C 1100 260, 1300 150, 1620 60" fill="none" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"{TRACO}/>')
p.append(icone("t:hourglass", 770, 160, 70, TINTA))
for k, (ic, t) in enumerate([("t:trending-down", "mais leve"), ("t:trending-up", "às vezes rende mais"), ("t:thumb-up", "recebe elogio")]):
    p.append(icone(ic, 90, 50 + k * 60, 40, OXID))
for k, (ic, t) in enumerate([("t:bolt", "fratura por estresse"), ("t:calendar", "menstruação que sumiu"), ("t:battery-1", "cansaço que não passa"), ("t:mood-sad", "humor, sono, imunidade")]):
    p.append(icone(ic, 1320, 170 + k * 56, 40, FOSF))
p.append("</svg>")
rs = [rot(140, 56, "mais leve", w=300, tam=24, cor=OXID, peso=700), rot(140, 116, "às vezes rende mais", w=300, tam=24, cor=OXID, peso=700),
      rot(140, 176, "recebe elogio", w=300, tam=24, cor=OXID, peso=700),
      rot(700, 238, "atraso", w=210, tam=30, cor=TINTA, peso=700, alinha="center", serif=True)]
for k, t in enumerate(["fratura por estresse", "menstruação que sumiu", "cansaço que não passa", "humor, sono, imunidade"]):
    rs.append(rot(1372, 176 + k * 56, t, w=280, tam=24, cor=FOSF, peso=700))
rs += [rot(330, 290, "o que a pessoa sente", w=240, tam=22, cor=OXID, peso=700, alinha="center"),
       rot(1030, 40, "o custo que acumula", w=260, tam=22, cor=FOSF, peso=700),
       rot(60, 432, "primeiras semanas", w=560, tam=22, cor=MUDO, alinha="center"),
       rot(1000, 432, "meses depois", w=664, tam=22, cor=MUDO, alinha="center"),
       rot(0, 480, "Osso, hormônio, metabolismo, sangue, crescimento, cabeça, coração, intestino, imunidade, e o desempenho junto", w=1664, tam=24, cor=TINTA, peso=600, alinha="center")]
S.append({"id": "atraso", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O conflito mais traiçoeiro", "titulo": "A falta de energia funciona antes de cobrar",
          "fonte": "Consenso do Comitê Olímpico Internacional sobre deficiência de energia no esporte, 2023 · esquema, sem valores medidos"})

# 6. uma pergunta por lugar
p = [svg_abre(1664, 560, "Cinco balões de pergunta, um para cada lugar do conflito, com o ícone do lugar embaixo; no da energia, três sinais juntos")]
perg = [("Energia", "t:flame", FOSF, FOSF_T, "“Está tentando perder peso agora?” “O que comeu ontem?”"),
        ("Peso da categoria", "t:scale", GLIC, GLIC_T, "“Quando é a pesagem, e quanto falta?”"),
        ("Competir machucado", "h:bandaged", FOSF, FOSF_T, "“O que acontece se você não jogar?”"),
        ("Volume", "t:calendar", GLIC, GLIC_T, "“Quanto tempo leva para voltar de uma semana pesada?”"),
        ("Identidade", "t:id", OXID, OXID_T, "“Como você se sente num dia sem treino?”")]
rs = []
for k, (t, ic, c, ct, q) in enumerate(perg):
    x = k * 336
    p.append(balao(x, 0, 316, 250, c, ct))
    rs.append(rot(x + 20, 30, q, w=276, tam=26, cor=TINTA, peso=600, lh=1.3, serif=True))
    p.append(icone(ic, x + 20, 300, 64, c))
    rs.append(rot(x + 96, 312, t, w=220, tam=24, cor=c, peso=700, lh=1.2))
# energia: três sinais juntos
p.append(caixa(0, 400, 820, 160, FOSF, CARTAO, esp=3, rx=16))
for k, (ic, t) in enumerate([("t:trending-down", "desempenho caiu com o treino mantido"), ("t:hourglass", "recuperação mais lenta"), ("t:eye-off", "algo sumiu: ciclo, libido, sono, disposição")]):
    x = 20 + k * 270
    p.append(icone(ic, x, 470, 44, FOSF))
    rs.append(rot(x + 52, 470, t, w=200, tam=20, cor=TINTA, peso=600, lh=1.2))
rs.append(rot(20, 414, "na energia, três sinais juntos, e não o peso", w=780, tam=24, cor=FOSF, peso=700))
# peso: prazo
p.append(caixa(860, 400, 804, 160, GLIC, CARTAO, esp=3, rx=16))
rs.append(rot(880, 414, "no peso, o sinal é o calendário", w=760, tam=24, cor=GLIC, peso=700))
p.append(f'<rect x="880" y="470" width="480" height="30" rx="15" fill="{GLIC}" opacity="0.35"/><rect x="880" y="515" width="70" height="30" rx="15" fill="{FOSF}"/>')
rs += [rot(1380, 472, "5% em 4 semanas", w=270, tam=22, cor=TINTA, peso=600), rot(970, 517, "5% em 4 dias: outra conversa", w=500, tam=22, cor=FOSF, peso=700)]
p.append("</svg>")
S.append({"id": "sinais", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Como perceber, sem pedir exame", "titulo": "Cada lugar se revela com uma pergunta de conversa"})

# 7. quem vê primeiro
p = [svg_abre(1664, 580, "Linha do tempo de quem vê cada sinal: quem prescreve o treino, quem reabilita, quem pergunta de comida, quem escuta, e o médico por último; embaixo, sinais que circulam na equipe e sinais que param em quem viu"), defs(TINTA, OXID)]
p.append(seta(40, 250, 1620, 250, TINTA, "m0", esp=4))
quem = [("h:exercise-weights", "queda de desempenho", "quem prescreve o treino", OXID),
        ("h:crutches", "lesão que se repete", "quem reabilita", OXID),
        ("t:salad", "o que sumiu do prato", "quem pergunta de comida", OXID),
        ("t:ear", "desânimo no dia sem treino", "quem escuta", OXID),
        ("h:stethoscope", "exame alterado, ciclo ausente, fratura", "o médico, por último", FOSF)]
rs = [rot(1530, 200, "tempo", w=100, tam=20, cor=MUDO, alinha="right")]
for k, (ic, sinal, prof, c) in enumerate(quem):
    x = 60 + k * 300 + (80 if k == 4 else 0)
    p.append(f'<circle cx="{x + 90}" cy="250" r="14" fill="{c}"/>')
    p.append(icone(ic, x + 45, 140, 90, c))
    rs.append(rot(x, 20, sinal, w=250, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.2))
    rs.append(rot(x - 10, 278, prof, w=220, tam=22, cor=c, peso=700, alinha="center", lh=1.2))
# duas equipes
for j, (tit, circula, c) in enumerate([("sinais que circulam: equipe", True, OXID), ("sinais que param em quem viu: cinco atendimentos", False, FOSF)]):
    x0 = j * 852
    p.append(caixa(x0, 370, 812, 210, c, OXID_T if circula else FOSF_T, esp=3, rx=18))
    rs.append(rot(x0 + 20, 386, tit, w=772, tam=24, cor=c, peso=700))
    pts = [(x0 + 150 + i * 130, 500) for i in range(5)]
    if circula:
        for a in range(5):
            for b in range(a + 1, 5):
                (x1, y1), (x2, y2) = pts[a], pts[b]
                p.append(f'<path d="M{x1} {y1} Q {(x1 + x2) / 2} {y1 - 30 - (b - a) * 12} {x2} {y2}" fill="none" stroke="{OXID}" stroke-width="2.5" opacity="0.7"/>')
    for (x, y) in pts:
        p.append(f'<circle cx="{x}" cy="{y}" r="22" fill="{c}"/>')
        if not circula:
            p.append(f'<circle cx="{x}" cy="{y}" r="36" fill="none" stroke="{c}" stroke-width="2.5"{TRACO}/>')
p.append("</svg>")
S.append({"id": "quem-ve", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quem vê primeiro", "titulo": "Ninguém vê os cinco sinais sozinho"})

# 8. a postura em três degraus
p = [svg_abre(1664, 600, "Três degraus subindo: o objetivo é dela; o custo é dito em quatro partes, com a maioria dos casos parada ali; e o limite estreito, em vermelho, de dano previsível e grave")]
degraus = [(0, 420, 520, "O objetivo é dela", OXID, OXID_T), (560, 260, 520, "O custo é dito, sem chantagem", GLIC, GLIC_T), (1120, 100, 544, "Existe um ponto em que você não acompanha", FOSF, FOSF_T)]
rs = []
for (x, y, w, t, c, ct) in degraus:
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{600 - y}" rx="12" fill="{ct}" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(x + 24, y + 20, t, w=w - 48, tam=30, cor=c, peso=700, serif=True, lh=1.15))
rs.append(rot(24, 500, "adulto informado escolhe o próprio risco", w=470, tam=22, cor=TINTA, lh=1.3))
for k, t in enumerate(["o quê", "em quanto tempo", "com que chance", "o que dá para fazer"]):
    x, y = 590 + (k % 2) * 240, 350 + (k // 2) * 64
    p.append(caixa(x, y, 220, 50, GLIC, CARTAO, esp=2, rx=25))
    rs.append(rot(x, y + 12, t, w=220, tam=20, cor=TINTA, peso=700, alinha="center"))
for k in range(14):
    p.append(f'<circle cx="{600 + (k % 7) * 64}" cy="{505 + (k // 7) * 40}" r="12" fill="{GLIC}" opacity="0.8"/>')
p.append(f'<circle cx="1180" cy="520" r="12" fill="{FOSF}"/>')
p.append(icone("t:filter", 1150, 200, 90, FOSF))
p.append(f'<circle cx="20" cy="40" r="12" fill="{GLIC}"/>')
rs += [rot(46, 26, "cada ponto: uma pessoa que chega em conflito", w=600, tam=22, cor=TINTA, peso=600),
       rot(1250, 210, "dano previsível e grave", w=400, tam=24, cor=FOSF, peso=700),
       rot(1250, 246, "um filtro estreito de propósito", w=400, tam=22, cor=TINTA),
       rot(1150, 330, "diz que não faz, diz por quê e continua disponível", w=490, tam=22, cor=TINTA, lh=1.3),
       rot(1210, 506, "quase ninguém chega aqui", w=440, tam=20, cor=FOSF, peso=600)]
p.append("</svg>")
S.append({"id": "postura", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A segunda decisão", "titulo": "Quase tudo que chega fica no segundo degrau"})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "Constrói margem ou gasta margem?",
          "regras": ["O acordo entre objetivo e saúde é a regra. O conflito é a exceção que pede método.",
                     "Quando há conflito, ele está num de cinco lugares: energia, peso e estética, competir machucado, volume e calendário, identidade.",
                     "A postura: o objetivo é da pessoa, o custo é dito com prazo e chance, e existe um limite estreito."],
          "quem": "Todas as profissões reconhecem os cinco lugares. Cada uma vê um primeiro, e é isso que faz a equipe valer mais do que a soma.",
          "proxima": "Exercício é dose: da conversa à prescrição"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-02.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-02.json"), "w"), ensure_ascii=False, indent=1)
print("01-02.json:", len(S), "slides")
