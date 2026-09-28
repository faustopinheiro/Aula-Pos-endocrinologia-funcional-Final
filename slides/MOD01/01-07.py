"""Spec do deck 1.7 (refeito no modelo dos desenhos). Gera 01-07.json ao lado deste arquivo."""
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

# 1. o bilhete de uma linha
p = [svg_abre(1664, 560, "Um papel de encaminhamento com uma linha só, favor avaliar, queixa de fadiga, e muito espaço em branco; ao lado, a cabeça de quem escreveu, cheia do que sabia e não escreveu; do outro lado, o colega que começa do zero"), defs(MUDO)]
p.append(caixa(0, 0, 620, 560, CINZA, CARTAO, esp=3, rx=12))
p.append(f'<rect x="0" y="0" width="620" height="16" rx="8" fill="{AZUL}"/>')
for k in range(9):
    p.append(f'<line x1="40" y1="{200 + k * 38}" x2="580" y2="{200 + k * 38}" stroke="{GRADE}" stroke-width="2"/>')
rs = [rot(40, 50, "Encaminhamento", w=540, tam=22, cor=MUDO, peso=700),
      rot(40, 100, "“Favor avaliar. Queixa de fadiga.”", w=560, tam=36, cor=TINTA, peso=700, serif=True)]
p.append(f'<circle cx="930" cy="250" r="190" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
p.append(icone("h:head", 850, 150, 160, GLIC))
ficou = [("há oito meses", 760, 90), ("o que já tentei", 960, 70), ("a menstruação que sumiu", 700, 390), ("minha hipótese", 990, 400)]
for (t, x, y) in ficou:
    w = 30 + len(t) * 12
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="22" fill="{CARTAO}" stroke="{GLIC}" stroke-width="2"/>')
    rs.append(rot(x, y + 10, t, w=w, tam=20, cor=GLIC, peso=700, alinha="center"))
rs.append(rot(740, 470, "o que ficou na sua cabeça, e não no papel", w=380, tam=22, cor=GLIC, peso=700, alinha="center", lh=1.25))
p.append(seta(1140, 250, 1270, 250, MUDO, "m0", esp=4))
p.append(caixa(1290, 60, 374, 380, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("h:doctor-female", 1420, 90, 110, AZUL))
p.append(icone("t:clock", 1330, 250, 56, AZUL))
rs += [rot(1400, 256, "começa do zero", w=250, tam=28, cor=AZUL, peso=700, serif=True),
       rot(1310, 330, "quarenta minutos para descobrir de novo o que você já sabia, e às vezes não descobre", w=334, tam=21, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "bilhete", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O encaminhamento mais comum do país", "titulo": "Esse bilhete transfere o paciente, e não o que você sabe"})

# 2. as cinco linhas
p = [svg_abre(1664, 580, "Cinco linhas numeradas, cada uma com uma pergunta: o que eu observei, com dado; há quanto tempo; o que eu já tentei; minha hipótese, escrita como hipótese; o que eu quero saber de volta; uma seta volta da quinta linha para o começo"), defs(OXID)]
linhas = [("t:ruler-measure", "O que eu observei, com dado", "não “parece cansado”: o que dá para medir ou contar", OXID),
          ("t:hourglass", "Há quanto tempo", "muda a hipótese, a urgência e a conduta", OXID),
          ("t:checklist", "O que eu já tentei, e o que aconteceu", "evita que o colega repita o que falhou", OXID),
          ("t:bulb", "Minha hipótese, escrita como hipótese", "é o que separa contribuir de invadir", GLIC),
          ("t:refresh", "O que eu quero saber de volta", "abre o caminho de volta", AZUL)]
rs = []
for k, (ic, t, tx, c) in enumerate(linhas):
    y = k * 116
    p.append(caixa(120, y, 1400, 100, c, [OXID_T, OXID_T, OXID_T, GLIC_T, AZUL_T][k], esp=3, rx=16))
    p.append(f'<circle cx="50" cy="{y + 50}" r="40" fill="{c}"/>')
    rs.append(rot(10, y + 26, str(k + 1), w=80, tam=36, cor=PAPEL, peso=700, alinha="center", serif=True))
    p.append(icone(ic, 150, y + 22, 56, c))
    rs.append(rot(230, y + 14, t, w=900, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(230, y + 58, tx, w=1200, tam=22, cor=TINTA))
p.append(f'<path d="M1520 514 C 1640 514, 1640 50, 1540 50" fill="none" stroke="{AZUL}" stroke-width="4"{TRACO} marker-end="url(#m0)"/>')
p.append("</svg>")
S.append({"id": "cinco-linhas", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O instrumento", "titulo": "Um encaminhamento que funciona tem sempre cinco linhas"})

# 3. o exemplo com as linhas marcadas pela função
p = [svg_abre(1664, 530, "O encaminhamento de uma nutricionista, frase por frase, cada uma marcada pela cor da linha que cumpre: dado, tempo, o que já tentou, hipótese e pedido de retorno; a frase da menstruação ausente destacada como o que só ela tinha")]
frases = [("Paciente em acompanhamento nutricional há quatro meses.", "tempo", OXID),
          ("Refere cansaço progressivo há oito meses e queda de rendimento.", "dado e tempo", OXID),
          ("Relata que a menstruação não vem há cinco meses, o que ainda não foi investigado.", "dado", FOSF),
          ("A ingestão estimada está bem abaixo do gasto, com cinco sessões de treino por semana.", "dado", OXID),
          ("Comecei a reconstrução da energia há seis semanas, com melhora parcial da disposição.", "já tentei", OXID),
          ("Encaminho para avaliação médica, com hipótese de baixa disponibilidade de energia.", "hipótese", GLIC),
          ("Gostaria de saber a conduta, para ajustar a minha.", "de volta", AZUL)]
p.append(caixa(0, 0, 1664, 530, CINZA, CARTAO, esp=3, rx=14))
rs = []
for k, (t, lab, c) in enumerate(frases):
    y = 20 + k * 72
    if c == FOSF:
        p.append(f'<rect x="12" y="{y - 6}" width="1640" height="68" rx="10" fill="{FOSF_T}"/>')
    p.append(f'<rect x="30" y="{y}" width="10" height="60" rx="5" fill="{c}"/>')
    rs.append(rot(64, y + 12, t, w=1260, tam=26, cor=TINTA, serif=True, lh=1.2))
    p.append(f'<rect x="1380" y="{y + 10}" width="250" height="40" rx="20" fill="{CARTAO}" stroke="{c}" stroke-width="2"/>')
    rs.append(rot(1380, y + 18, lab, w=250, tam=20, cor=c, peso=700, alinha="center"))
rs.append(rot(1100, 20 + 2 * 72 + 44, "o que só ela tinha", w=260, tam=18, cor=FOSF, peso=700, alinha="right"))
p.append("</svg>")
S.append({"id": "exemplo", "tipo": "diagrama", "h": 530, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Escrito por uma nutricionista", "titulo": "Sete linhas que entregam o que só ela tinha",
          "destaque": "Quem pergunta o que aconteceu com o paciente vira o profissional para quem os outros encaminham."})

# 4. seis palavras que explodem em sentidos
p = [svg_abre(1664, 500, "Seis palavras, cada uma no centro de um grupo de setas para sentidos diferentes: carga, liberado, repouso, moderado, dieta e alta"), defs(GLIC)]
palavras = [("Carga", ["da sessão", "do tecido", "de tudo que gasta adaptação"]),
            ("Liberado", ["para parte do treino?", "para o coletivo?", "para jogo?"]),
            ("Repouso", ["absoluto?", "relativo?", "parar o que dói?"]),
            ("Moderado", ["esforço percebido?", "frequência cardíaca?", "teste da fala?"]),
            ("Dieta", ["padrão alimentar", "restrição"]),
            ("Alta", ["da reabilitação", "para competir"])]
rs = []
for k, (w_, sentidos) in enumerate(palavras):
    cx0, cy0 = (k % 3) * 560, (k // 3) * 250
    p.append(f'<rect x="{cx0}" y="{cy0 + 90}" width="200" height="70" rx="35" fill="{FOSF if w_ == "Liberado" else TINTA}"/>')
    rs.append(rot(cx0, cy0 + 106, w_, w=200, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
    n = len(sentidos)
    for j, t in enumerate(sentidos):
        ty = cy0 + 30 + j * (190 / max(n - 1, 1)) if n > 1 else cy0 + 125
        if n == 2:
            ty = cy0 + 60 + j * 110
        p.append(f'<path d="M{cx0 + 200} {cy0 + 125} C {cx0 + 240} {cy0 + 125}, {cx0 + 240} {ty + 20}, {cx0 + 268} {ty + 20}" fill="none" stroke="{GLIC}" stroke-width="3" marker-end="url(#m0)"/>')
        rs.append(rot(cx0 + 280, ty + 6, t, w=250, tam=21, cor=TINTA, peso=600, lh=1.15))
p.append("</svg>")
S.append({"id": "palavras", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A mesma palavra, sentidos diferentes", "titulo": "Seis palavras que cada profissão entende de um jeito",
          "destaque": "Acrescente o complemento: “liberado para treino técnico sem sprint, por duas semanas”."})

# 5. o registro com quatro campos
p = [svg_abre(1664, 560, "Uma ficha de registro compartilhado com quatro campos preenchidos: o que mudou, a carga da semana, o que cada um viu com data e nome, e o que está pendente e com quem")]
p.append(caixa(0, 0, 1664, 560, CINZA, CARTAO, esp=3, rx=16))
p.append(f'<rect x="0" y="0" width="1664" height="70" rx="16" fill="{OXID}"/><rect x="0" y="40" width="1664" height="30" fill="{OXID}"/>')
rs = [rot(30, 18, "Registro compartilhado · um lugar só", w=1000, tam=26, cor=PAPEL, peso=700)]
campos = [("t:arrows-exchange", "O que mudou", "só a diferença desde o último registro: é o campo que mais economiza o tempo de quem lê", OXID, None),
          ("t:barbell", "A carga da semana", "com o complemento: para quê, quanto e por quanto tempo", OXID, None),
          ("t:eye-check", "O que cada um viu", "com data e com o nome de quem viu: a informação ganha dono", OXID, None),
          ("t:hourglass", "O que está pendente, e com quem", "impede que todo mundo ache que alguém está resolvendo", GLIC, GLIC_T)]
for k, (ic, t, tx, c, ct) in enumerate(campos):
    y = 90 + k * 116
    if ct:
        p.append(f'<rect x="12" y="{y - 6}" width="1640" height="108" rx="10" fill="{ct}"/>')
    p.append(icone(ic, 40, y + 18, 60, c))
    rs.append(rot(130, y + 10, t, w=520, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(660, y + 16, tx, w=960, tam=24, cor=TINTA, lh=1.3))
    if k < 3:
        p.append(f'<line x1="30" y1="{y + 106}" x2="1634" y2="{y + 106}" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
S.append({"id": "registro", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde a informação mora", "titulo": "O registro compartilhado precisa de quatro campos"})

# 6. o que nunca entra
p = [svg_abre(1664, 482, "Quatro cartões com cadeado: conteúdo da psicoterapia, dado sensível sem necessidade, julgamento sobre o paciente e crítica a colega; em cada um, o que foi riscado e o que entra no lugar"), defs(OXID)]
itens = [("Conteúdo da psicoterapia", "a conversa da sessão", "risco, prontidão, se a carga precisa mudar"),
         ("Dado sensível sem necessidade", "tudo o que se sabe", "só o que quem lê precisa para agir, com consentimento"),
         ("Julgamento", "“pouco aderente”", "“fez 2 das 4 sessões nas últimas 3 semanas”"),
         ("Crítica a colega", "a discordância", "a decisão; a discordância se resolve na conversa")]
rs = []
for k, (t, sai, entra) in enumerate(itens):
    x, y = (k % 2) * 842, (k // 2) * 250
    p.append(caixa(x, y, 822, 232, FOSF, FOSF_T, esp=3, rx=18))
    p.append(icone("t:lock", x + 24, y + 22, 52, FOSF))
    rs.append(rot(x + 92, y + 28, t, w=700, tam=30, cor=FOSF, peso=700, serif=True))
    rs.append(rot(x + 30, y + 110, sai, w=320, tam=24, cor=MUDO, peso=600, lh=1.25))
    p.append(f'<line x1="{x + 30}" y1="{y + 125}" x2="{x + 20 + min(320, 30 + len(sai) * 12)}" y2="{y + 125}" stroke="{FOSF}" stroke-width="4"/>')
    p.append(seta(x + 360, y + 125, x + 420, y + 125, OXID, "m0", esp=4))
    p.append(f'<rect x="{x + 440}" y="{y + 80}" width="360" height="136" rx="14" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(x + 456, y + 92, "entra:", w=330, tam=18, cor=OXID, peso=700))
    rs.append(rot(x + 456, y + 120, entra, w=330, tam=22, cor=TINTA, peso=600, lh=1.3))
p.append("</svg>")
S.append({"id": "nunca-entra", "tipo": "diagrama", "h": 482, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Ética e lei", "titulo": "Quatro coisas nunca entram num registro compartilhado",
          "destaque": "Antes de escrever: quem vai ler isso precisa disso para agir?"})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "Para fazer ainda esta semana",
          "regras": ["Adote as cinco linhas em todo encaminhamento que sair de você.", "Acrescente o complemento a liberado, carga, repouso, alta e moderado.",
                     "Pergunte de volta: “como ficou aquele paciente que eu te mandei?”"],
          "quem": "Sem equipe montada? Três nomes na agenda: um médico, um nutricionista e um profissional de educação física ou fisioterapeuta. Três pessoas para quem você escreve e de quem recebe retorno.",
          "proxima": "Como não ser enganado por um estudo"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-07.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-07.json"), "w"), ensure_ascii=False, indent=1)
print("01-07.json:", len(S), "slides")
