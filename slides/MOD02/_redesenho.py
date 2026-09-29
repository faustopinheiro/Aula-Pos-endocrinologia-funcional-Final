"""Desenhos que substituem os últimos slides de texto do Módulo 2 (cartões, colunas e números).
Cada função devolve o dicionário do slide, com o mesmo id do slide que substitui."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

TRACO = ' stroke-dasharray="10 8"'
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
CINZA = "#C9CFD4"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"


def rabdo():
    """2.3: a dor tardia que passa contra a que não passa, e os quatro sinais."""
    p = [svg_abre(1664, 480, "À esquerda, duas curvas de dor ao longo de sete dias: a dor tardia comum sobe no primeiro e no segundo dia e some até o quarto; a da rabdomiólise continua alta depois do quarto dia. À direita, os quatro sinais: dor desproporcional, inchaço importante, fraqueza marcante e urina escura, com a escala de cor da urina")]
    X = lambda d: 80 + d * 110
    Y = lambda v: 420 - v * 3.4
    p.append(f'<line x1="70" y1="420" x2="870" y2="420" stroke="{MUDO}" stroke-width="3"/><line x1="72" y1="30" x2="72" y2="420" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<rect x="{X(3)}" y="30" width="{X(4) - X(3)}" height="390" fill="{FOSF}" opacity="0.08"/>')
    comum = [(0, 5), (0.5, 40), (1, 70), (1.5, 78), (2, 70), (3, 38), (4, 12), (5, 4), (7, 2)]
    rab = [(0, 5), (0.5, 50), (1, 85), (2, 95), (3, 98), (4, 97), (5, 96), (7, 92)]
    for pts, c, esp in [(comum, MUDO, 6), (rab, FOSF, 8)]:
        d = "M" + " L".join(f"{X(a):.0f} {Y(b):.0f}" for a, b in pts)
        p.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{esp}" stroke-linejoin="round" stroke-linecap="round"/>')
    rs = [rot(84, 0, "dor", w=200, tam=22, cor=MUDO),
          rot(70, 432, "dias depois do treino", w=800, tam=22, cor=MUDO, alinha="center"),
          rot(X(3) - 40, 44, "3 a 4 dias", w=190, tam=20, cor=FOSF, peso=700, alinha="center"),
          rot(X(4) + 20, 300, "dor tardia comum: some", w=320, tam=22, cor=MUDO, peso=700),
          rot(X(4) + 20, 36, "não melhora: rabdomiólise até que se prove o contrário", w=330, tam=22, cor=FOSF, peso=700, lh=1.25)]
    sinais = [("t:bolt", "Dor desproporcional", "que não melhora em três ou quatro dias"),
              ("t:droplet", "Inchaço importante", "no músculo trabalhado"),
              ("t:battery-1", "Fraqueza marcante", "fora do esperado para o treino")]
    for k, (ic, t, x) in enumerate(sinais):
        y = k * 96
        p.append(caixa(940, y, 724, 84, FOSF, FOSF_T, esp=3, rx=14))
        p.append(icone(ic, 960, y + 17, 50, FOSF))
        rs += [rot(1030, y + 8, t, w=620, tam=26, cor=FOSF, peso=700, serif=True), rot(1030, y + 46, x, w=620, tam=21, cor=TINTA)]
    y = 292
    p.append(caixa(940, y, 724, 188, FOSF, FOSF_T, esp=3, rx=14))
    rs.append(rot(960, y + 12, "Urina escura", w=680, tam=26, cor=FOSF, peso=700, serif=True))
    cores = [("#F3E7A2", "normal"), ("#E2BE55", "concentrada"), ("#8A4B1E", "cor de chá"), ("#3A1D12", "cor de cola")]
    for k, (c, t) in enumerate(cores):
        x = 960 + k * 172
        p.append(f'<rect x="{x}" y="{y + 60}" width="150" height="64" rx="10" fill="{c}" stroke="{FOSF if k > 1 else CINZA}" stroke-width="{4 if k > 1 else 2}"/>')
        rs.append(rot(x, y + 134, t, w=150, tam=20, cor=FOSF if k > 1 else MUDO, peso=700 if k > 1 else 400, alinha="center"))
    p.append("</svg>")
    return {"id": "rabdo", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
            "eyebrow": "Bandeira vermelha", "titulo": "Dor que não melhora em quatro dias não é dor tardia",
            "fonte": "Curvas: esquema, sem valores medidos",
            "destaque": "Avaliação médica no mesmo dia. A dor tardia comum é o pano de fundo que faz a rabdomiólise passar despercebida.",
            "destaque_cor": "verm"}


def semanas():
    """2.4: a conta fecha na semana; e o atleta que quebra, cabeça ou perna."""
    p = [svg_abre(1664, 560, "À esquerda, duas faixas de quatro semanas, uma treinando em jejum e outra alimentada, com a mesma dieta e o mesmo treino; na de jejum as chamas da queima de gordura na sessão são maiores, e as duas chegam ao mesmo ponto: composição parecida. À direita, o atleta que quebra: a cabeça foi junto, hipoglicemia, ou só a perna, glicogênio muscular esgotado"), defs(OXID)]
    rs = [rot(0, 0, "Durante a sessão, e ao longo de semanas", w=900, tam=28, cor=TINTA, peso=700, serif=True)]
    for j, (t, grande, c) in enumerate([("em jejum", True, GLIC), ("alimentada", False, AZUL)]):
        y = 70 + j * 170
        rs.append(rot(0, y + 44, t, w=150, tam=24, cor=c, peso=700))
        for s in range(4):
            x = 160 + s * 150
            p.append(f'<rect x="{x}" y="{y}" width="136" height="130" rx="12" fill="{CARTAO}" stroke="{c}" stroke-width="2"/>')
            p.append(icone("t:flame", x + (34 if grande else 46), y + 20, 68 if grande else 44, GLIC if grande else CINZA))
            rs.append(rot(x, y + 100, f"semana {s + 1}", w=136, tam=18, cor=MUDO, alinha="center"))
        p.append(seta(770, y + 65, 820, 165 + 20, OXID, "m0", esp=3))
    p.append(f'<circle cx="850" cy="205" r="30" fill="{OXID}"/>')
    rs.append(rot(760, 244, "composição parecida", w=180, tam=20, cor=OXID, peso=700, alinha="center", lh=1.15))
    rs += [rot(0, 400, "na sessão, a queima de gordura em jejum é maior; em quatro semanas, com a mesma dieta, a composição foi parecida", w=900, tam=22, cor=TINTA, lh=1.3),
           rot(0, 470, "o que decide é o balanço de energia, e a intensidade que a pessoa sustenta sem se machucar e sem abandonar", w=900, tam=22, cor=OXID, peso=700, lh=1.3)]
    p.append(caixa(960, 0, 704, 560, TINTA, PAPEL, esp=2, rx=18))
    rs.append(rot(990, 20, "O atleta que quebra: a cabeça foi junto, ou só a perna?", w=650, tam=26, cor=TINTA, peso=700, serif=True, lh=1.2))
    for k, (ic, t, lista, c, ct) in enumerate([("h:head", "Hipoglicemia: central", "confusão, suor frio, tontura; melhora em minutos com carboidrato rápido; previne-se com o que se come durante a prova", FOSF, FOSF_T),
                                               ("t:run", "Glicogênio da perna: local", "cabeça lúcida, perna que não entrega; não melhora em minutos; previne-se nos dias antes e no ritmo da primeira metade", GLIC, GLIC_T)]):
        y = 120 + k * 216
        p.append(caixa(984, y, 656, 200, c, ct, esp=3, rx=14))
        p.append(icone(ic, 1004, y + 22, 64, c))
        rs += [rot(1086, y + 22, t, w=540, tam=26, cor=c, peso=700, serif=True), rot(1086, y + 66, lista, w=540, tam=21, cor=TINTA, lh=1.3)]
    p.append("</svg>")
    return {"id": "semanas", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
            "eyebrow": "O erro maior é conceitual", "titulo": "Composição corporal se decide em semanas, não na sessão",
            "fonte": "Schoenfeld e colaboradores, Journal of the International Society of Sports Nutrition 2014 · chamas: esquema"}


def dordelado():
    """2.6: quantos sentem, onde dói de verdade, e o que fazer."""
    p = [svg_abre(1664, 520, "À esquerda, dez corredores com sete destacados, os que sentiram a dor de lado no último ano, e cinco com um destacado, os que sentem numa única prova. No meio, o tronco com a região do flanco marcada: peritônio e nervos entre as costelas; a cãibra de diafragma riscada. À direita, o que ajuda antes e na hora")]
    rs = []
    for k in range(10):
        c = GLIC if k < 7 else CINZA
        p.append(icone("h:running", (k % 5) * 90, 40 + (k // 5) * 96, 80, c))
    rs.append(rot(0, 236, "perto de 70% dos corredores sentiram no último ano", w=460, tam=22, cor=GLIC, peso=700, lh=1.25))
    for k in range(5):
        p.append(icone("h:running", k * 90, 320, 80, FOSF if k == 0 else CINZA))
    rs.append(rot(0, 418, "cerca de 1 em 5 sente numa única prova", w=460, tam=22, cor=FOSF, peso=700, lh=1.25))
    p.append(icone("h:person", 560, 40, 380, CINZA))
    p.append(f'<ellipse cx="800" cy="250" rx="46" ry="60" fill="{FOSF}" opacity="0.35" stroke="{FOSF}" stroke-width="4"/>')
    p.append(f'<line x1="846" y1="230" x2="960" y2="170" stroke="{FOSF}" stroke-width="3"/><line x1="846" y1="270" x2="960" y2="320" stroke="{FOSF}" stroke-width="3"/>')
    rs += [rot(966, 150, "peritônio", w=240, tam=24, cor=FOSF, peso=700, serif=True),
           rot(966, 300, "nervos entre as costelas", w=240, tam=22, cor=FOSF, peso=700, lh=1.2),
           rot(560, 440, "cãibra de diafragma", w=380, tam=26, cor=MUDO, peso=700, alinha="center", serif=True)]
    p.append(f'<line x1="600" y1="462" x2="900" y2="462" stroke="{FOSF}" stroke-width="5"/>')
    for j, (t, itens, c, ct) in enumerate([("Antes", ["menos líquido e comida pouco antes", "postura"], GLIC, GLIC_T),
                                           ("Na hora", ["baixar o ritmo", "soltar o ar por completo", "pressionar o local"], OXID, OXID_T)]):
        y = 0 if j == 0 else 200
        h = 180 if j == 0 else 320
        p.append(caixa(1220, y, 444, h, c, ct, esp=3, rx=16))
        rs.append(rot(1244, y + 16, t, w=400, tam=28, cor=c, peso=700, serif=True))
        for i, it in enumerate(itens):
            p.append(icone("t:check", 1244, y + 70 + i * 60, 36, c))
            rs.append(rot(1292, y + 74 + i * 60, it, w=360, tam=22, cor=TINTA, peso=600))
    p.append("</svg>")
    return {"id": "dordelado", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
            "eyebrow": "A dor de lado", "titulo": "A dor de lado é muito comum, e não vem do diafragma",
            "fonte": "Morton e Callister, Sports Medicine 2015"}


def campo():
    """2.8: os dois limiares sem laboratório."""
    p = [svg_abre(1664, 500, "À esquerda, o teste do falar: um balão com a frase inteira abaixo do primeiro limiar e um balão com a frase quebrada em pedaços quando a pessoa cruza o limiar, numa seta de intensidade. À direita, o contrarrelógio de trinta minutos: a barra de tempo com os últimos vinte minutos destacados, a frequência cardíaca média desse trecho e a velocidade média do teste"), defs(TINTA)]
    p.append(caixa(0, 0, 800, 500, OXID, OXID_T, esp=3, rx=18))
    rs = [rot(24, 20, "1º limiar: o teste do falar", w=760, tam=30, cor=OXID, peso=700, serif=True)]
    p.append(f'<rect x="30" y="100" width="340" height="110" rx="26" fill="{CARTAO}" stroke="{OXID}" stroke-width="3"/>')
    rs += [rot(30, 118, "“Hoje a subida estava tranquila, deu para conversar.”", w=340, tam=21, cor=TINTA, alinha="center", lh=1.25, serif=True),
           rot(30, 220, "fala a frase inteira: abaixo", w=340, tam=22, cor=OXID, peso=700, alinha="center")]
    p.append(f'<rect x="430" y="100" width="340" height="110" rx="26" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    rs += [rot(430, 130, "“Hoje… a subida… estava…”", w=340, tam=24, cor=FOSF, alinha="center", serif=True),
           rot(430, 220, "a fala quebra: cruzando", w=340, tam=22, cor=FOSF, peso=700, alinha="center")]
    p.append(f'<defs><linearGradient id="gi" x1="0" x2="1"><stop offset="0" stop-color="{OXID}"/><stop offset="1" stop-color="{FOSF}"/></linearGradient></defs>')
    p.append(f'<rect x="40" y="300" width="720" height="26" rx="13" fill="url(#gi)"/>')
    p.append(f'<line x1="430" y1="280" x2="430" y2="346" stroke="{TINTA}" stroke-width="5"/>')
    rs += [rot(40, 340, "intensidade", w=720, tam=20, cor=MUDO, alinha="center"),
           rot(330, 250, "1º limiar", w=200, tam=22, cor=TINTA, peso=700, alinha="center"),
           rot(24, 390, "o critério para o paciente levar para todo treino leve, sem aparelho e sem conta", w=752, tam=22, cor=TINTA, peso=600, lh=1.3)]
    p.append(caixa(864, 0, 800, 500, FOSF, FOSF_T, esp=3, rx=18))
    rs.append(rot(888, 20, "2º limiar: contrarrelógio de 30 minutos", w=760, tam=30, cor=FOSF, peso=700, serif=True))
    x0, x1 = 900, 1630
    minuto = (x1 - x0) / 30
    p.append(f'<rect x="{x0}" y="130" width="{x1 - x0}" height="70" rx="10" fill="{CARTAO}" stroke="{FOSF}" stroke-width="2"/>')
    p.append(f'<rect x="{x0 + 10 * minuto}" y="130" width="{20 * minuto}" height="70" rx="10" fill="{FOSF}" opacity="0.8"/>')
    for m in (0, 10, 20, 30):
        rs.append(rot(x0 + m * minuto - 40, 210, f"{m} min", w=80, tam=20, cor=MUDO, alinha="center"))
    rs += [rot(x0 + 10 * minuto, 150, "últimos 20 minutos", w=20 * minuto, tam=24, cor=PAPEL, peso=700, alinha="center"),
           rot(x0, 80, "esforço máximo e contínuo", w=x1 - x0, tam=22, cor=TINTA, peso=600, alinha="center")]
    for k, (ic, t) in enumerate([("t:heartbeat", "FC média dos últimos 20 minutos: aproximação da FC de limiar"),
                                 ("t:gauge", "velocidade ou potência média do teste: perto do 2º limiar")]):
        y = 280 + k * 92
        p.append(icone(ic, 890, y, 52, FOSF))
        rs.append(rot(958, y + 4, t, w=680, tam=22, cor=TINTA, peso=600, lh=1.25))
    rs.append(rot(888, 460, "em corredores e triatletas, próximo da medida de laboratório", w=760, tam=20, cor=FOSF, peso=700))
    p.append("</svg>")
    return {"id": "campo", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
            "eyebrow": "A maioria nunca vai fazer o exame", "titulo": "Os dois limiares também se acham sem laboratório",
            "fonte": "Reed e Pipe, Current Opinion in Cardiology 2014 · McGehee e colaboradores, Journal of Strength and Conditioning Research 2005"}


def quem():
    """2.9: um espectro de quem sente a interferência, e a inversão com a idade."""
    p = [svg_abre(1664, 540, "Uma faixa que vai de onde a interferência importa, em vermelho, até onde ela é nota de rodapé, em verde: levantador, velocista, saltador e lutador em fase específica de um lado; corredor de rua, quem treina por saúde, o master e o coletivo amador do outro. Embaixo, a inversão com a idade: no jovem, o endurance pode custar força; no master, o que custa força é o tempo")]
    p.append(f'<defs><linearGradient id="gq" x1="0" x2="1"><stop offset="0" stop-color="{FOSF}"/><stop offset="1" stop-color="{OXID}"/></linearGradient></defs>')
    p.append(f'<rect x="0" y="170" width="1664" height="30" rx="15" fill="url(#gq)"/>')
    rs = [rot(0, 210, "importa", w=400, tam=24, cor=FOSF, peso=700), rot(1264, 210, "nota de rodapé", w=400, tam=24, cor=OXID, peso=700, alinha="right")]
    pessoas = [("t:barbell", "levantador", FOSF), ("h:running", "velocista", FOSF), ("t:karate", "lutador em fase específica", FOSF),
               ("t:trophy", "fase de competição de força", FOSF),
               ("t:ball-volleyball", "coletivo amador: força longe do jogo", GLIC),
               ("t:run", "corredor de rua com força 2 vezes", OXID), ("h:walking", "quem treina por saúde", OXID)]
    for k, (ic, t, c) in enumerate(pessoas):
        x = 40 + k * 232
        p.append(icone(ic, x + 50, 40, 90, c))
        p.append(f'<line x1="{x + 95}" y1="140" x2="{x + 95}" y2="168" stroke="{c}" stroke-width="3"/>')
        rs.append(rot(x - 10, 250, t, w=210, tam=21, cor=c, peso=700, alinha="center", lh=1.2))
    rs.append(rot(0, 330, "quem está com a conta apertada: aí não é interferência, é falta de recuperação", w=1664, tam=22, cor=TINTA, peso=600, alinha="center"))
    for j, (ic, t, x_, c, ct) in enumerate([("h:young-people", "No jovem que busca desempenho", "o endurance é o que pode custar força", FOSF, FOSF_T),
                                            ("h:elderly", "No master", "o que custa força é o tempo; o aeróbico que ele gosta não é o inimigo", OXID, OXID_T)]):
        x = j * 852
        p.append(caixa(x, 390, 812, 150, c, ct, esp=3, rx=16))
        p.append(icone(ic, x + 24, 418, 90, c))
        rs += [rot(x + 136, 410, t, w=650, tam=26, cor=c, peso=700, serif=True), rot(x + 136, 456, x_, w=650, tam=22, cor=TINTA, lh=1.3)]
    p.append("</svg>")
    return {"id": "quem", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
            "eyebrow": "Para quem essa conversa é séria", "titulo": "A interferência importa numa ponta, e é nota de rodapé na outra",
            "destaque": "O inimigo do master não é o aeróbico que ele gosta de fazer. É a sessão de força que nunca entra na agenda.",
            "destaque_cor": "ambar"}
