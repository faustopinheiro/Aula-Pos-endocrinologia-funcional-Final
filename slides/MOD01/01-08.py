"""Spec do deck 1.8 (refeito no modelo dos desenhos). Gera 01-08.json ao lado deste arquivo."""
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

# 1. a cadeia que faz todo sentido
p = [svg_abre(1664, 470, "Quatro elos em sequência: o exercício produz radicais livres, radicais livres causam dano, antioxidante neutraliza radical livre, logo antioxidante ajuda a recuperar; o último elo com um X vermelho"), defs(OXID, FOSF)]
elos = [("O exercício produz radicais livres", OXID, OXID_T), ("Radicais livres causam dano nas células", OXID, OXID_T),
        ("Antioxidante neutraliza radical livre", OXID, OXID_T), ("Logo, antioxidante depois do treino ajuda a recuperar e a render", FOSF, FOSF_T)]
rs = []
for k, (t, c, ct) in enumerate(elos):
    x = k * 420
    p.append(caixa(x, 170, 380, 190, c, ct, esp=4 if k == 3 else 3, rx=20))
    p.append(f'<circle cx="{x + 40}" cy="170" r="30" fill="{c}"/>')
    rs.append(rot(x + 10, 152, str(k + 1) if k < 3 else "?", w=60, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
    rs.append(rot(x + 24, 210, t, w=332, tam=26, cor=TINTA, peso=600, serif=True, lh=1.25))
    if k < 3:
        p.append(seta(x + 384, 265, x + 414, 265, c if k < 2 else FOSF, "m0" if k < 2 else "m1", esp=4))
p.append(f'<line x1="1280" y1="180" x2="1650" y2="350" stroke="{FOSF}" stroke-width="6" opacity="0.35"/><line x1="1650" y1="180" x2="1280" y2="350" stroke="{FOSF}" stroke-width="6" opacity="0.35"/>')
p.append(icone("t:pill", 20, 10, 80, GLIC)); p.append(icone("t:pill", 100, 30, 64, GLIC)); p.append(icone("t:glass-full", 180, 14, 80, AZUL))
rs += [rot(290, 40, "vitamina C e vitamina E todo dia, depois do treino", w=900, tam=26, cor=TINTA, peso=600),
       rot(0, 400, "cada passo é verdade, e a conclusão parece inevitável", w=1664, tam=28, cor=OXID, peso=700, alinha="center", serif=True)]
p.append("</svg>")
S.append({"id": "faz-sentido", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Para começar", "titulo": "Faz todo sentido, e está errado",
          "destaque": "Cinco histórias, cinco jeitos de gente boa e bem informada ser enganada. Sem pirâmide, sem fórmula."})

# 2. o antioxidante: marcador × desempenho
p = [svg_abre(1664, 480, "Dois painéis de barras: à esquerda, os marcadores de adaptação dentro do músculo sobem só no grupo placebo; à direita, o VO2máx ao fim do treino fica igual nos dois grupos")]
p.append(caixa(0, 0, 1664, 80, CINZA, CARTAO, esp=2, rx=14))
rs = [rot(24, 22, "54 jovens · 11 semanas de treino aeróbio · vitamina C 1.000 mg e E 235 mg por dia × placebo · biópsia do músculo antes e depois", w=1616, tam=24, cor=TINTA, peso=600)]
for j, (tit, x0, alturas, c) in enumerate([("Marcadores de adaptação no músculo", 0, [(80, 80, 210), (80, 80, 82)], OXID),
                                           ("VO₂máx", 880, [(0, 0, 200), (0, 0, 200)], AZUL)]):
    p.append(caixa(x0, 100, 784, 380, c, [OXID_T, AZUL_T][j], esp=3, rx=18))
    rs.append(rot(x0 + 24, 114, tit, w=740, tam=28, cor=c, peso=700, serif=True))
    base = 400
    for g, (nome, cor_g) in enumerate([("placebo", OXID), ("vitaminas C e E", FOSF)]):
        pre, _, pos = alturas[g]
        gx = x0 + 120 + g * 330
        if pre:
            p.append(f'<rect x="{gx}" y="{base - pre}" width="100" height="{pre}" rx="6" fill="{CINZA}"/>')
            rs.append(rot(gx, base + 6, "antes", w=100, tam=18, cor=MUDO, alinha="center"))
        p.append(f'<rect x="{gx + (110 if pre else 55)}" y="{base - pos}" width="100" height="{pos}" rx="6" fill="{cor_g}"/>')
        rs.append(rot(gx + (110 if pre else 55), base + 6, "depois", w=100, tam=18, cor=MUDO, alinha="center"))
        rs.append(rot(gx - 20, base + 34, nome, w=250, tam=22, cor=cor_g, peso=700, alinha="center"))
    p.append(f'<line x1="{x0 + 40}" y1="{base}" x2="{x0 + 744}" y2="{base}" stroke="{MUDO}" stroke-width="3"/>')
rs += [rot(540, 160, "só o placebo sobe", w=300, tam=22, cor=OXID, peso=700), rot(1320, 160, "igual nos dois grupos", w=320, tam=22, cor=AZUL, peso=700)]
p.append("</svg>")
S.append({"id": "antioxidante", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeiro erro: confiar numa cadeia lógica perfeita", "titulo": "O antioxidante apagou o sinal, e o desempenho não mudou",
          "fonte": "Paulsen e colaboradores, Journal of Physiology 2014 · barras: esquema, sem valores medidos",
          "destaque": "Mecanismo explica como poderia acontecer. Não diz se acontece."})

# 3. o betacaroteno
p = [svg_abre(1664, 560, "Em cima, o prato de vegetais com uma seta verde para menos câncer de pulmão, e entre eles uma nuvem de diferenças escondidas; embaixo, a cápsula de betacaroteno com uma seta vermelha para mais câncer de pulmão no ensaio sorteado"), defs(OXID, FOSF)]
p.append(caixa(0, 0, 1664, 250, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:salad", 40, 60, 120, OXID))
p.append(seta(190, 120, 1260, 120, OXID, "m0", esp=5))
rs = [rot(40, 190, "quem come mais vegetal", w=240, tam=22, cor=OXID, peso=700, alinha="center"),
      rot(1290, 80, "menos câncer de pulmão", w=360, tam=30, cor=OXID, peso=700, serif=True, lh=1.15),
      rot(1290, 170, "a associação era real", w=360, tam=22, cor=TINTA)]
nuvem = ["fuma menos", "bebe menos", "se exercita mais", "mais estudo", "mais renda", "mais acesso a médico"]
for k, t in enumerate(nuvem):
    x = 330 + (k % 3) * 300
    y = 36 + (k // 3) * 110
    p.append(f'<rect x="{x}" y="{y}" width="270" height="48" rx="24" fill="{PAPEL}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
    rs.append(rot(x, y + 11, t, w=270, tam=22, cor=MUDO, peso=600, alinha="center"))
p.append(caixa(0, 290, 1664, 270, FOSF, FOSF_T, esp=4, rx=18))
p.append(icone("t:pill", 40, 340, 120, FOSF))
p.append(seta(190, 400, 1260, 400, FOSF, "m1", esp=5))
rs += [rot(20, 470, "betacaroteno em cápsula", w=280, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(330, 330, "quase 30 mil fumantes sorteados, na Finlândia", w=900, tam=24, cor=TINTA, peso=600),
       rot(330, 430, "um segundo ensaio, nos Estados Unidos, parou antes do fim pelo mesmo sinal", w=900, tam=22, cor=TINTA),
       rot(1290, 330, "18% mais câncer de pulmão", w=360, tam=30, cor=FOSF, peso=700, serif=True, lh=1.15),
       rot(1290, 430, "o dedo que apontava foi colocado numa cápsula", w=360, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "betacaroteno", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Segundo erro: achar que andar junto é causar", "titulo": "Com o betacaroteno, a associação era real e a causa, não",
          "fonte": "ATBC, New England Journal of Medicine 1994 · a mesma história com a reposição hormonal, Women's Health Initiative, JAMA 2002"})

# 4. o usuário saudável
p = [svg_abre(1664, 450, "Duas pessoas lado a lado: uma cercada de suplemento, sono em dia, comida organizada, check-up e treino regular; a outra sem nada disso; entre elas, a pergunta: você está comparando o suplemento ou as pessoas; embaixo, o alongamento levando o crédito do aquecimento e da progressão")]
p.append(icone("h:person", 190, 40, 160, OXID))
p.append(icone("h:person", 1310, 40, 160, MUDO))
volta = [("t:pill", -140, 0), ("t:moon", -150, 100), ("t:salad", 190, 0), ("t:stethoscope", 200, 100), ("t:barbell", 30, -60)]
for (ic, dx, dy) in volta:
    p.append(icone(ic, 220 + dx, 70 + dy, 56, OXID))
rs = [rot(60, 236, "usa suplemento por conta própria", w=440, tam=22, cor=OXID, peso=700, alinha="center"),
      rot(1180, 236, "não usa", w=440, tam=22, cor=MUDO, peso=700, alinha="center"),
      rot(560, 70, "Você está comparando o suplemento, ou as pessoas?", w=560, tam=34, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.2),
      rot(560, 190, "sortear quem usa é o jeito de desligar esse efeito", w=560, tam=22, cor=OXID, peso=600, alinha="center")]
p.append(caixa(0, 270, 1664, 180, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:stretching", 40, 300, 90, GLIC))
p.append(icone("t:medal", 150, 310, 60, GLIC))
for k, t in enumerate(["chega mais cedo", "aquece direito", "tem orientação", "cuida da progressão"]):
    x = 560 + k * 270
    p.append(f'<rect x="{x}" y="300" width="250" height="48" rx="24" fill="{CARTAO}" stroke="{GLIC}" stroke-width="2"/>')
    rs.append(rot(x, 311, t, w=250, tam=20, cor=GLIC, peso=700, alinha="center"))
rs += [rot(240, 300, "alongar antes levou o crédito", w=300, tam=24, cor=GLIC, peso=700, serif=True, lh=1.15),
       rot(560, 378, "nos ensaios que sortearam as pessoas, o alongamento sozinho não mostrou efeito preventivo", w=1070, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "usuario-saudavel", "tipo": "diagrama", "h": 450, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O nome que explica metade dos milagres", "titulo": "O efeito do usuário saudável explica metade dos milagres",
          "fonte": "Lauersen e colaboradores, British Journal of Sports Medicine 2014",
          "destaque": "A primeira pergunta: essas pessoas eram iguais antes de começar?"})

# 5. em quem foi medido
p = [svg_abre(1664, 540, "À esquerda, uma barra com os estudos de ciência do esporte: 31% só com homens, 6% só com mulheres, o resto misto, e mulheres em cerca de um terço dos participantes; à direita, o participante padrão, homem jovem universitário treinado, e a paciente real, mulher de 50 e poucos anos, hipertensa, com dois empregos; entre eles, o filtro dos critérios de exclusão")]
rs = [rot(0, 0, "Mais de 5 mil estudos, mais de 12 milhões de participantes", w=760, tam=26, cor=TINTA, peso=700, serif=True, lh=1.2)]
x0, w0 = 0, 760
partes = [(31, FOSF, "31% só homens"), (63, CINZA, "mistos"), (6, GLIC, "6% só mulheres")]
xx = x0
for (pct, c, t) in partes:
    w = w0 * pct / 100
    p.append(f'<rect x="{xx}" y="100" width="{w - 3}" height="80" fill="{c}"/>')
    xx += w
rs += [rot(0, 190, "31% só homens", w=300, tam=22, cor=FOSF, peso=700), rot(300, 190, "mistos", w=300, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(560, 190, "6% só mulheres", w=200, tam=22, cor=GLIC, peso=700, alinha="right")]
for k in range(3):
    p.append(icone("h:woman" if k == 0 else "h:man", k * 110, 260, 90, GLIC if k == 0 else CINZA))
rs += [rot(340, 270, "mulheres: cerca de um terço dos participantes", w=420, tam=24, cor=GLIC, peso=700, lh=1.25),
       rot(0, 400, "e a idade: boa parte da fisiologia do exercício foi medida entre 18 e 30 anos, porque o laboratório fica dentro da universidade", w=760, tam=22, cor=TINTA, lh=1.3)]
# participante x paciente com filtro
p.append(caixa(860, 0, 380, 420, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("h:man", 970, 30, 160, AZUL))
for k, t in enumerate(["homem", "jovem", "universitário", "treinado"]):
    rs.append(rot(880, 210 + k * 40, t, w=340, tam=24, cor=AZUL, peso=700, alinha="center"))
rs.append(rot(880, 370, "o participante padrão", w=340, tam=24, cor=AZUL, peso=700, serif=True, alinha="center"))
p.append(caixa(1284, 0, 380, 420, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("h:woman", 1394, 30, 160, FOSF))
for k, t in enumerate(["mulher", "50 e poucos anos", "hipertensa", "dois empregos"]):
    rs.append(rot(1304, 210 + k * 40, t, w=340, tam=24, cor=FOSF, peso=700, alinha="center"))
rs.append(rot(1304, 370, "a paciente real", w=340, tam=24, cor=FOSF, peso=700, serif=True, alinha="center"))
p.append(caixa(860, 440, 804, 100, TINTA, CARTAO, esp=2, rx=16))
p.append(icone("t:filter", 880, 462, 56, TINTA))
rs.append(rot(950, 456, "critérios de exclusão: sem doença do coração, sem remédio contínuo, sem lesão, sem cigarro; tiram do estudo quem você atende", w=700, tam=21, cor=TINTA, lh=1.3))
p.append("</svg>")
S.append({"id": "em-quem", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceiro erro: não perguntar em quem foi medido", "titulo": "O participante padrão não é o seu paciente",
          "fonte": "Cowley e colaboradores, Women in Sport and Physical Activity Journal 2021"})

# 6. o placar de outro jogo
p = [svg_abre(1664, 560, "A tela de um celular com um medidor e a agulha na faixa vermelha; ao lado, a frase da paciente; embaixo, a linha dela mesma subindo nos últimos meses")]
p.append(f'<rect x="40" y="0" width="340" height="560" rx="40" fill="{TINTA}"/><rect x="60" y="40" width="300" height="480" rx="20" fill="{CARTAO}"/>')
cx, cy, r = 210, 260, 110
def arco(a0, a1, c):
    x0_, y0_ = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1_, y1_ = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    return f'<path d="M{x0_:.1f} {y0_:.1f} A {r} {r} 0 0 1 {x1_:.1f} {y1_:.1f}" fill="none" stroke="{c}" stroke-width="28"/>'
p.append(arco(180, 120, FOSF)); p.append(arco(118, 60, GLIC)); p.append(arco(58, 0, OXID))
a = math.radians(160)
p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 90 * math.cos(a):.0f}" y2="{cy - 90 * math.sin(a):.0f}" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="10" fill="{TINTA}"/>')
rs = [rot(60, 80, "capacidade cardiorrespiratória", w=300, tam=20, cor=MUDO, alinha="center", lh=1.2),
      rot(60, 300, "faixa vermelha", w=300, tam=26, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(80, 360, "tabela construída com outra população", w=260, tam=18, cor=MUDO, alinha="center", lh=1.2),
      rot(460, 10, "“Eu tô ganhando o jogo. Só me mostraram o placar de outro jogo.”", w=1204, tam=44, cor=TINTA, peso=700, serif=True, lh=1.2),
      rot(460, 150, "50 e poucos anos, catorze meses depois de sair do sedentarismo, os primeiros 5 km da vida", w=1204, tam=24, cor=MUDO, peso=600)]
pts = [(480, 520), (620, 500), (760, 470), (900, 450), (1040, 410), (1180, 380), (1320, 330), (1460, 290), (1600, 250)]
p.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{OXID}" stroke-width="7" stroke-linejoin="round"/>')
for (x, y) in pts:
    p.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{OXID}" stroke="{PAPEL}" stroke-width="3"/>')
p.append(f'<line x1="460" y1="540" x2="1640" y2="540" stroke="{MUDO}" stroke-width="3"/>')
rs += [rot(460, 230, "A comparação que importa: ela mesma, três meses atrás", w=1000, tam=28, cor=OXID, peso=700, serif=True)]
p.append("</svg>")
S.append({"id": "placar", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Toda faixa de referência veio de algum grupo", "titulo": "A faixa do aplicativo foi medida em outro jogo",
          "fonte": "Linha: esquema, sem valores medidos"})

# 7. quem pagou
p = [svg_abre(1664, 580, "À esquerda, um documento carimbado 1965 com trechos grifados; à direita, dois grupos de revisões sobre bebida açucarada: sem conflito, quase todas encontram associação; com conflito, quase todas dizem que a evidência é insuficiente; embaixo, os cinco lugares onde o conflito age antes do dado")]
p.append(f'<g transform="rotate(-2 280 200)"><rect x="40" y="10" width="480" height="340" rx="8" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"/></g>')
for k in range(7):
    w = [380, 340, 400, 300, 360, 390, 250][k]
    c = GLIC if k in (1, 4) else CINZA
    p.append(f'<rect x="80" y="{70 + k * 38}" width="{w}" height="{20 if c == CINZA else 26}" rx="4" fill="{c}" opacity="{0.9 if c == GLIC else 0.7}"/>')
p.append(f'<g transform="rotate(-12 420 300)"><rect x="330" y="270" width="190" height="70" rx="8" fill="none" stroke="{FOSF}" stroke-width="5"/></g>')
rs = [rot(330, 283, "1965", w=190, tam=34, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(40, 370, "gordura como vilã, açúcar minimizado, financiamento não declarado", w=480, tam=22, cor=TINTA, lh=1.3)]
for j, (t, cor_maior, lab_maior, cor_menor) in enumerate([("revisões sem conflito", OXID, "há associação", GLIC), ("revisões com conflito", GLIC, "evidência insuficiente", OXID)]):
    y = 20 + j * 180
    rs.append(rot(620, y, t, w=400, tam=26, cor=TINTA, peso=700, serif=True))
    for k in range(6):
        c = cor_maior if k < 5 else cor_menor
        p.append(f'<rect x="{620 + k * 90}" y="{y + 50}" width="70" height="90" rx="6" fill="{c}" opacity="0.85"/>')
    rs.append(rot(1180, y + 70, lab_maior, w=484, tam=28, cor=cor_maior, peso=700, serif=True))
etapas = ["a pergunta", "o comparador", "o desfecho do resumo", "o estudo que não sai", "a redação"]
for k, t in enumerate(etapas):
    x = 620 + k * 212
    p.append(f'<rect x="{x}" y="400" width="196" height="60" rx="30" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    rs.append(rot(x, 410, t, w=196, tam=19, cor=FOSF, peso=700, alinha="center", lh=1.1))
rs += [rot(620, 370, "onde o conflito age, antes do dado:", w=1000, tam=22, cor=TINTA, peso=600),
       rot(620, 490, "sinal prático: existe estudo grande e independente? Muitos pequenos, todos positivos e nenhum grande: desconfie", w=1044, tam=22, cor=TINTA, peso=600, lh=1.3)]
p.append("</svg>")
S.append({"id": "quem-pagou", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarto erro: não perguntar quem pagou", "titulo": "Ninguém mentiu, e o enquadramento mudou a conclusão",
          "fonte": "Kearns e colaboradores, JAMA Internal Medicine 2016 · Bes-Rastrollo e colaboradores, PLoS Medicine 2013 · blocos: esquema"})

# 8. o espelho
p = [svg_abre(1664, 464, "Um espelho oval; dentro dele, uma prateleira de consultório com produtos à venda e um vídeo antigo com muitas visualizações; ao lado, os dois conflitos: o de quem vende o que prescreve e o do que já se disse em público")]
p.append(f'<ellipse cx="400" cy="235" rx="290" ry="225" fill="{AZUL_T}" stroke="{TINTA}" stroke-width="10"/>')
p.append(f'<line x1="200" y1="190" x2="600" y2="190" stroke="{GLIC}" stroke-width="8"/>')
for k in range(5):
    p.append(f'<rect x="{220 + k * 76}" y="{110 + (k % 2) * 16}" width="56" height="{80 - (k % 2) * 16}" rx="8" fill="{GLIC}" opacity="0.8"/>')
p.append(f'<rect x="250" y="230" width="300" height="150" rx="14" fill="{TINTA}"/>')
p.append(icone("t:player-play", 360, 265, 80, PAPEL))
rs = [rot(250, 390, "vídeo antigo, milhares de visualizações", w=300, tam=18, cor=TINTA, peso=600, alinha="center", lh=1.2)]
for k, (t, tx, c, ct, ic) in enumerate([("Quem vende o que prescreve", "prateleira, linha própria, laboratório de que é sócio, curso do protocolo: não é antiético por si, mas é conflito; diga antes, em uma frase", GLIC, GLIC_T, "h:money-bag"),
                                        ("O que você já disse em público", "o conflito sem dinheiro, e o mais difícil: mudar de ideia custa identidade", FOSF, FOSF_T, "h:megaphone")]):
    y = k * 240
    p.append(caixa(780, y, 884, 224, c, ct, esp=3, rx=18))
    p.append(icone(ic, 810, y + 30, 80, c))
    rs.append(rot(914, y + 26, t, w=720, tam=32, cor=c, peso=700, serif=True))
    rs.append(rot(914, y + 82, tx, w=720, tam=24, cor=TINTA, lh=1.35))
p.append("</svg>")
S.append({"id": "sobre-nos", "tipo": "diagrama", "h": 464, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mesmo olhar, virado para nós", "titulo": "Conflito de interesse também é nosso",
          "destaque": "As pessoas confiam mais em quem muda de ideia explicando o motivo. O que destrói autoridade é defender o indefensável porque já falou."})

# 9. a curva da dor que melhora sozinha
p = [svg_abre(1664, 480, "Curva da dor de um paciente ao longo do tempo: sobe até um pico no dia da consulta e desce depois, com três faixas que explicam a descida: história natural, regressão à média e expectativa; alguns pontos saem do gráfico: quem não melhorou parou de vir")]
p.append(f'<line x1="80" y1="440" x2="1600" y2="440" stroke="{MUDO}" stroke-width="3"/><line x1="82" y1="30" x2="82" y2="440" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M100 360 C 300 340, 420 240, 560 90 C 700 240, 900 340, 1580 385" fill="none" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<line x1="560" y1="70" x2="560" y2="440" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
faixas = [("história natural", "a maior parte das dores melhora sozinha", GLIC), ("regressão à média", "depois do pior momento, vem um melhor", AZUL), ("expectativa", "quem investiu relata melhora, e ela é real", OXID)]
rs = [rot(96, 20, "dor", w=200, tam=22, cor=MUDO), rot(1400, 450, "tempo", w=200, tam=22, cor=MUDO, alinha="right"),
      rot(340, 40, "o dia da consulta: o pior momento", w=210, tam=20, cor=TINTA, peso=700, alinha="right", lh=1.2)]
for k, (t, tx, c) in enumerate(faixas):
    y = 40 + k * 88
    p.append(f'<rect x="960" y="{y}" width="12" height="76" rx="6" fill="{c}"/>')
    rs.append(rot(990, y + 2, t, w=440, tam=28, cor=c, peso=700, serif=True))
    rs.append(rot(990, y + 42, tx, w=440, tam=21, cor=TINTA))
for (x, y) in [(1500, 200), (1550, 150), (1600, 100)]:
    p.append(f'<circle cx="{x}" cy="{y}" r="12" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
p.append(f'<path d="M1460 250 L 1630 60" fill="none" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
rs += [rot(1440, 270, "quem não melhorou parou de vir, e não entra na conta", w=224, tam=21, cor=MUDO, peso=600, lh=1.25)]
p.append("</svg>")
S.append({"id": "experiencia", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quinto erro: a própria experiência como prova", "titulo": "Três forças melhoram o paciente sem você ter feito nada",
          "fonte": "Esquema, sem valores medidos",
          "destaque": "Experiência cria hipótese. Não prova."})

# 10. cinco perguntas e a balança da assimetria
p = [svg_abre(1664, 480, "À esquerda, cinco perguntas numa coluna: quem foram, comparado com o quê, desfecho ou marcador, por quanto tempo, qual o tamanho do efeito; à direita, uma balança: barato e seguro pede pouca prova, caro, invasivo ou por anos pede ensaio sorteado")]
perg = [("t:users", "Quem foram?"), ("t:arrows-exchange", "Comparado com o quê?"), ("t:target", "É desfecho ou marcador?"), ("t:hourglass", "Por quanto tempo?"), ("t:ruler-measure", "Qual o tamanho do efeito?")]
rs = []
for k, (ic, t) in enumerate(perg):
    y = k * 98
    p.append(caixa(0, y, 640, 84, OXID, OXID_T, esp=3, rx=16))
    p.append(icone(ic, 24, y + 14, 56, OXID))
    rs.append(rot(100, y + 22, t, w=520, tam=30, cor=OXID, peso=700, serif=True))
ang = 9
cx, cy = 1180, 290
p.append(f'<polygon points="{cx},{cy} {cx - 44},{cy + 130} {cx + 44},{cy + 130}" fill="{TINTA}"/>')
p.append(f'<g transform="rotate({ang} {cx} {cy})"><line x1="{cx - 400}" y1="{cy}" x2="{cx + 400}" y2="{cy}" stroke="{TINTA}" stroke-width="10" stroke-linecap="round"/></g>')
yl = cy - 400 * math.sin(math.radians(ang))
yr = cy + 400 * math.sin(math.radians(ang))
p.append(caixa(700, yl - 210, 360, 190, OXID, CARTAO, esp=3, rx=16))
p.append(caixa(1300, yr - 262, 364, 210, FOSF, FOSF_T, esp=4, rx=16))
rs += [rot(720, yl - 196, "Barato, seguro e plausível", w=320, tam=26, cor=OXID, peso=700, serif=True, lh=1.15),
       rot(720, yl - 120, "dormir mais, comer melhor, distribuir a carga: dá para agir com estudo de observação", w=320, tam=20, cor=TINTA, lh=1.3),
       rot(1320, yr - 248, "Caro, invasivo, arriscado ou por anos", w=324, tam=26, cor=FOSF, peso=700, serif=True, lh=1.15),
       rot(1320, yr - 162, "hormônio, remédio, dose alta: exija ensaio sorteado; o custo de errar é o do betacaroteno", w=324, tam=20, cor=TINTA, lh=1.3),
       rot(800, 440, "o custo de errar decide quanta prova é preciso", w=760, tam=24, cor=TINTA, peso=700, alinha="center", serif=True)]
p.append("</svg>")
S.append({"id": "cinco-perguntas", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Três minutos, antes de ler a conclusão", "titulo": "Cinco perguntas antes da conclusão, e uma regra de peso",
          "destaque": "Na fala: “foi visto em”, e diga em quem. “Hoje não há base para esperar isso.” E marque quando for observação sua."})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "A abertura, nos três níveis",
          "regras": ["Decisão: prescrição individual é da educação física (e da fisioterapia na reabilitação); plano alimentar, da nutrição; diagnóstico, remédio e liberação, da medicina; psicoterapia, da psicologia.",
                     "Contribuição: o sinal que cada um vê primeiro, as cinco linhas do encaminhamento, a carga com complemento e a pergunta de volta.",
                     "Reconhecimento: objetivo que gasta margem, “150 minutos” para quem está em zero, conselho de tirar remédio vindo de quem não prescreveu, estudo só de marcador, produto sem estudo independente."],
          "quem": "Antes de acreditar, pergunte: em quem, comparado com o quê, e quem pagou.",
          "proxima": "o corpo, começando pela energia"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-08.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-08.json"), "w"), ensure_ascii=False, indent=1)
print("01-08.json:", len(S), "slides")
