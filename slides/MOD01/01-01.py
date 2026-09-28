"""Spec do deck 1.1 (refeito no modelo dos desenhos). Gera 01-01.json ao lado deste arquivo."""
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

def ficha(p, rs, x, idade, linhas, cor, ct, ic):
    p.append(caixa(x, 0, 620, 590, cor, ct, esp=4, rx=20))
    p.append(icone(ic, x + 30, 30, 110, cor))
    rs.append(rot(x + 160, 50, f"{idade} anos", w=440, tam=44, cor=cor, peso=700, serif=True))
    for j, (icn, t, c) in enumerate(linhas):
        y = 180 + j * 78
        p.append(icone(icn, x + 40, y, 40, c))
        rs.append(rot(x + 100, y + 4, t, w=500, tam=26, cor=TINTA, peso=600))

# 1. as duas fichas
p = [svg_abre(1664, 600, "Duas fichas: 34 anos, exames normais, sono de cinco horas, cansaço, gripes, oito meses sem evoluir; 58 anos, hipertenso tratado, glicemia alterada, corre há doze anos, meia maratona")]
rs = []
ficha(p, rs, 0, 34, [("t:check", "todos os exames normais", OXID), ("t:moon", "dorme cinco horas", FOSF), ("t:battery-1", "acorda cansado todo dia", FOSF),
                     ("t:mood-sick", "pega toda gripe do escritório", FOSF), ("t:trending-down", "oito meses sem evoluir", FOSF)], AZUL, AZUL_T, "h:person")
ficha(p, rs, 1044, 58, [("t:heartbeat", "hipertenso, tratando", GLIC), ("t:droplet", "glicemia de jejum alterada", GLIC), ("h:running", "corre há doze anos", OXID),
                        ("t:zzz", "dorme bem e sai com os amigos", OXID), ("t:medal", "meia maratona há dois meses", OXID)], GLIC, GLIC_T, "h:old-man")
p.append(icone("t:question-mark", 752, 190, 160, TINTA))
p.append("</svg>")
rs.append(rot(640, 380, "Qual dos dois é saudável?", w=384, tam=34, cor=TINTA, peso=700, alinha="center", serif=True, lh=1.2))
S.append({"id": "pergunta", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dois pacientes", "titulo": "O exame normal não responde a pergunta"})

# 2. a régua de 1948
p = [svg_abre(1664, 400, "Régua de bem-estar de zero a completo; a faixa onde as pessoas vivem fica longe do ponto completo; a palavra completo em vermelho")]
p.append(f'<rect x="80" y="230" width="1400" height="60" rx="30" fill="#E6E3DA"/>')
p.append(f'<rect x="420" y="230" width="760" height="60" rx="30" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
p.append(f'<circle cx="1480" cy="260" r="40" fill="{FOSF}"/>')
for k, x in enumerate([500, 640, 760, 900, 1040]):
    p.append(icone("h:person", x, 150, 60, AZUL))
p.append(f'<path d="M1180 200 C 1300 120, 1400 120, 1470 200" fill="none" stroke="{FOSF}" stroke-width="4" stroke-dasharray="10 8"/>')
p.append("</svg>")
rs = [rot(0, 0, "“Saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doença.”", w=1664, tam=34, cor=TINTA, peso=600, alinha="center", serif=True, lh=1.3),
      rot(1380, 310, "completo", w=200, tam=34, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(420, 310, "onde as pessoas vivem, quase o tempo todo", w=760, tam=26, cor=AZUL, peso=600, alinha="center"),
      rot(60, 310, "zero", w=120, tam=24, cor=MUDO),
      rot(1080, 70, "ninguém fica aqui por muito tempo", w=500, tam=22, cor=FOSF, peso=600, alinha="center")]
S.append({"id": "definicao", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Organização Mundial da Saúde, 1948", "titulo": "Pela letra de 1948, quase todo mundo está doente",
          "fonte": "Um manifesto do pós-guerra que abriu a porta para a promoção de saúde, e nunca foi reescrito"})

# 3. a cascata da medicalização
p = [svg_abre(1664, 500, "Cascata: a definição declara todos doentes; envelhecer, um período difícil e a variação normal viram doença; o mercado oferece suplemento, exame e protocolo; embaixo, as duas fichas com os carimbos trocados"), defs(FOSF)]
p.append(caixa(0, 20, 360, 150, FOSF, FOSF_T, esp=4))
p.append(seta(370, 95, 450, 95, FOSF, "m0", esp=5))
viram = ["envelhecer", "um período difícil", "variação normal do corpo"]
for i, t in enumerate(viram):
    p.append(caixa(460, 10 + i * 58, 400, 50, GLIC, GLIC_T, esp=2, rx=25))
p.append(seta(870, 95, 950, 95, FOSF, "m0", esp=5))
merc = [("t:pill", "suplemento para o que não falta"), ("t:clipboard-list", "exame para quem não tem queixa"), ("t:tools", "protocolo para o que não quebrou")]
rs = [rot(20, 45, "todo mundo doente", w=320, tam=34, cor=FOSF, peso=700, alinha="center", serif=True, lh=1.15)]
for i, t in enumerate(viram):
    rs.append(rot(460, 22 + i * 58, t, w=400, tam=24, cor=TINTA, peso=600, alinha="center"))
for i, (ic, t) in enumerate(merc):
    p.append(icone(ic, 960, 8 + i * 58, 44, FOSF))
    rs.append(rot(1020, 16 + i * 58, t, w=640, tam=26, cor=TINTA, peso=600))
for k, (x, idade, carimbo, c) in enumerate([(260, "58 anos · meia maratona", "doente", FOSF), (940, "34 anos · sem fôlego para a vida", "?", AZUL)]):
    p.append(caixa(x, 250, 460, 220, CINZA, CARTAO, esp=3, rx=18))
    p.append(f'<g transform="rotate(-10 {x + 300} 380)"><rect x="{x + 200}" y="340" width="220" height="80" rx="10" fill="none" stroke="{c}" stroke-width="6"/></g>')
    rs.append(rot(x + 20, 270, idade, w=420, tam=26, cor=TINTA, peso=700, lh=1.2))
    rs.append(rot(x + 200, 352, carimbo, w=220, tam=40, cor=c, peso=700, alinha="center", serif=True))
p.append("</svg>")
S.append({"id": "medicaliza", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A consequência", "titulo": "Uma definição que declara todos doentes empurra para tratar tudo"})

# 4. a margem
p = [svg_abre(1664, 560, "Duas colunas por paciente: a demanda da vida empilhada em blocos e a capacidade como uma linha; no de 58 anos sobra margem; no de 34 a demanda encosta na capacidade")]
blocos = [("treino", AZUL), ("sono", OXID), ("trabalho", GLIC), ("doença", FOSF)]
rs = []
for k, (x, cap, dem, nome) in enumerate([(120, 450, [90, 60, 100, 60], "58 anos"), (720, 310, [100, 80, 110, 50], "34 anos")]):
    y = 510
    for (t, c), h in zip(blocos, dem):
        if h:
            p.append(f'<rect x="{x}" y="{y - h}" width="240" height="{h}" fill="{c}" opacity="0.85" stroke="{PAPEL}" stroke-width="3"/>')
            if h >= 40:
                rs.append(rot(x, y - h / 2 - 14, t, w=240, tam=22, cor=PAPEL, peso=700, alinha="center"))
            y -= h
    yc = 510 - cap
    p.append(f'<line x1="{x - 30}" y1="{yc}" x2="{x + 270}" y2="{yc}" stroke="{TINTA}" stroke-width="6"/>')
    if yc < y - 10:
        p.append(f'<rect x="{x + 290}" y="{yc}" width="26" height="{y - yc}" fill="{OXID}"/>')
        rs.append(rot(x + 330, (yc + y) / 2 - 20, "margem", w=160, tam=28, cor=OXID, peso=700, serif=True))
    else:
        rs.append(rot(x + 290, yc + 10, "sem margem", w=200, tam=28, cor=FOSF, peso=700, serif=True))
    rs.append(rot(x - 30, 520, nome, w=300, tam=26, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x - 30 if yc < y else x + 290, yc - 40, "capacidade", w=200, tam=22, cor=TINTA, peso=600))
p.append(f'<line x1="60" y1="510" x2="1160" y2="510" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs += [rot(1220, 100, "Saúde é ter margem", w=444, tam=44, cor=TINTA, peso=700, serif=True, lh=1.15),
       rot(1220, 230, "a distância entre o que a vida exige e o que a pessoa consegue pagar sem quebrar", w=444, tam=26, cor=TINTA, lh=1.35),
       rot(1220, 380, "o treino é só uma das contas", w=444, tam=26, cor=AZUL, peso=700)]
S.append({"id": "margem", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Capacidade de se adaptar e de se autogerenciar", "titulo": "Com a régua da margem, os dois pacientes trocam de lugar",
          "fonte": "Huber e colaboradores, BMJ 2011 · esquema, sem valores medidos"})

# 5. as duas críticas
p = [svg_abre(1664, 500, "Duas críticas: uma régua com a escala borrada, difícil de medir; uma pessoa carregando pesos que não escolheu: dinheiro, turno, ônibus, falta de lugar, falta de tempo")]
p.append(caixa(0, 0, 780, 500, GLIC, GLIC_T, esp=4, rx=20))
p.append(f'<rect x="80" y="220" width="620" height="60" rx="8" fill="{CARTAO}" stroke="{GLIC}" stroke-width="3"/>')
for k in range(13):
    x = 100 + k * 48
    p.append(f'<line x1="{x}" y1="220" x2="{x}" y2="{250 if k % 3 else 270}" stroke="{GLIC}" stroke-width="3" opacity="{0.9 - k*0.06:.2f}"/>')
p.append(caixa(884, 0, 780, 500, FOSF, FOSF_T, esp=4, rx=20))
p.append(icone("h:person", 920, 150, 190, FOSF))
pesos = ["dinheiro", "trabalho em turno", "duas horas de ônibus", "sem lugar seguro para caminhar", "sem tempo para cozinhar"]
rs = [rot(30, 30, "Difícil de medir", w=720, tam=36, cor=GLIC, peso=700, serif=True),
      rot(30, 100, "completo bem-estar é impossível, mas claro; capacidade de se adaptar é realista, e vaga", w=720, tam=24, cor=TINTA, lh=1.35),
      rot(30, 320, "coisa vaga é difícil de virar política pública e pesquisa", w=720, tam=24, cor=TINTA, lh=1.35),
      rot(914, 30, "“Autogerenciar” pode virar culpa", w=720, tam=36, cor=FOSF, peso=700, serif=True)]
for j, t in enumerate(pesos):
    y = 105 + j * 62
    p.append(f'<rect x="1130" y="{y}" width="500" height="50" rx="25" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<line x1="1080" y1="{y + 25}" x2="1130" y2="{y + 25}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(1130, y + 11, t, w=500, tam=22, cor=TINTA, peso=600, alinha="center"))
rs.append(rot(914, 440, "a margem depende do que a pessoa faz e de onde ela vive", w=720, tam=24, cor=FOSF, peso=700))
p.append("</svg>")
S.append({"id": "criticas", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde a definição nova é fraca", "titulo": "Duas críticas honestas, e uma delas tem razão em parte"})

# 6. o que muda na segunda-feira
p = [svg_abre(1664, 500, "Quatro painéis: o alvo passa do número do exame para a capacidade; a manutenção num período difícil é resultado; o plano que não se sustenta não adapta; a reavaliação olha o que o exame não mostra")]
paineis = [("O alvo", AZUL, AZUL_T), ("A manutenção", OXID, OXID_T), ("A adesão", GLIC, GLIC_T), ("A reavaliação", FOSF, FOSF_T)]
rs = []
for i, (t, c, ct) in enumerate(paineis):
    x = i * 420
    p.append(caixa(x, 0, 396, 500, c, ct, esp=3, rx=18))
    rs.append(rot(x + 20, 20, t, w=356, tam=32, cor=c, peso=700, serif=True))
# alvo: dois alvos
p.append(icone("t:target", 40, 110, 120, CINZA)); p.append(icone("t:target", 220, 110, 140, AZUL))
rs += [rot(10, 265, "número do exame", w=200, tam=22, cor=MUDO, alinha="center"), rot(200, 270, "capacidade de aguentar a vida", w=190, tam=22, cor=AZUL, peso=700, alinha="center", lh=1.2),
       rot(20, 380, "às vezes andam juntos; às vezes não", w=356, tam=22, cor=TINTA, lh=1.3)]
# manutenção
p.append(f'<rect x="520" y="110" width="160" height="200" fill="{FOSF}" opacity="0.12"/>')
p.append(f'<polyline points="440,300 520,240 680,240 780,170" fill="none" stroke="{OXID}" stroke-width="7"/>')
rs += [rot(520, 120, "período difícil", w=160, tam=20, cor=FOSF, peso=700, alinha="center"), rot(440, 380, "manter, aqui, é resultado", w=356, tam=24, cor=OXID, peso=700, lh=1.3)]
# adesão
for k, (h, cheia) in enumerate([(180, False), (90, True)]):
    xx = 880 + k * 150
    p.append(f'<rect x="{xx}" y="{300 - h}" width="100" height="{h}" rx="8" fill="{GLIC if cheia else "none"}" stroke="{GLIC}" stroke-width="4" {"" if cheia else TRACO}/>')
rs += [rot(860, 310, "no papel", w=140, tam=20, cor=MUDO, alinha="center"), rot(1010, 310, "sustentado", w=140, tam=20, cor=GLIC, peso=700, alinha="center"),
       rot(860, 380, "adesão é parte do resultado", w=356, tam=24, cor=GLIC, peso=700, lh=1.3)]
# reavaliação
for k, ic in enumerate(["t:barbell", "t:refresh", "t:mood-sick", "t:sun"]):
    p.append(icone(ic, 1290 + (k % 2) * 150, 100 + (k // 2) * 120, 80, FOSF))
rs += [rot(1280, 380, "quanto aguenta, quanto demora a voltar, quantas vezes adoece, como acorda", w=356, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "segunda", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por que isso muda a sua segunda-feira", "titulo": "Quatro coisas mudam no trabalho de toda semana",
          "fonte": "Coisas que quase nenhum exame mostra"})

# 7. os dois erros
p = [svg_abre(1664, 500, "Uma balança: de um lado, margem não substitui rastreio, com as doenças silenciosas; do outro, tirar o treino custa caro, com mais de setecentos mil veteranos")]
p.append(f'<polygon points="832,300 792,420 872,420" fill="{TINTA}"/>')
p.append(f'<line x1="232" y1="300" x2="1432" y2="300" stroke="{TINTA}" stroke-width="10" stroke-linecap="round"/>')
p.append(caixa(0, 40, 620, 240, AZUL, AZUL_T, esp=4, rx=18))
p.append(caixa(1044, 40, 620, 240, FOSF, FOSF_T, esp=4, rx=18))
for k, ic in enumerate(["t:heartbeat", "t:droplet", "t:scale", "t:alert-triangle"]):
    p.append(icone(ic, 40 + k * 140, 170, 60, AZUL))
p.append(icone("h:running", 1080, 150, 100, FOSF))
p.append("</svg>")
rs = [rot(30, 60, "Margem não substitui rastreio", w=560, tam=32, cor=AZUL, peso=700, serif=True),
      rot(30, 110, "pressão, colesterol, diabetes e câncer no começo não tiram ninguém do treino", w=560, tam=22, cor=TINTA, lh=1.3),
      rot(1074, 60, "Tirar o treino custa caro", w=560, tam=32, cor=FOSF, peso=700, serif=True),
      rot(1200, 140, "mais de 700 mil veteranos: estar sem condicionamento pesou mais no risco de morrer que qualquer fator de risco cardíaco avaliado", w=440, tam=22, cor=TINTA, lh=1.3),
      rot(532, 440, "o exame informa; a margem decide", w=600, tam=30, cor=TINTA, peso=700, alinha="center", serif=True)]
S.append({"id": "dois-erros", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dois jeitos de usar mal a ideia", "titulo": "Um erro para cada lado",
          "fonte": "No hipertenso, a corrida é uma das coisas que mais o protegem por causa da pressão, e não apesar dela"})

S.append({"id": "tres-perguntas", "tipo": "fecho", "titulo": "Três perguntas que custam zero",
          "regras": ["O que você consegue fazer hoje que não conseguia há um ano? Ou o contrário.",
                     "Quanto tempo você leva para se recuperar de uma semana difícil?",
                     "O que você deixou de fazer na sua vida por causa de como tem se sentido?"],
          "quem": "Avaliar margem é de todas as profissões, sem pedir exame: conversando, medindo o que você já mede e acompanhando ao longo do tempo.",
          "proxima": "Quando o objetivo e o corpo discordam"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-01.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-01.json"), "w"), ensure_ascii=False, indent=1)
print("01-01.json:", len(S), "slides")
