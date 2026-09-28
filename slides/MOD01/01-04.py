"""Spec do deck 1.4 (refeito no modelo dos desenhos). Gera 01-04.json ao lado deste arquivo."""
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

# 1. o 150 riscado três vezes
p = [svg_abre(1664, 520, "O número 150 enorme com três riscos vermelhos; cada risco leva a um desenho: a faixa de 150 a 300, o círculo pela metade sem a força, e a escada que começa no zero")]
rs = [rot(0, 20, "150", w=560, tam=230, cor=TINTA, peso=700, serif=True, alinha="center"),
      rot(0, 300, "minutos por semana", w=560, tam=32, cor=MUDO, peso=600, alinha="center")]
for k, (y, a) in enumerate([(90, -8), (160, 4), (230, -3)]):
    p.append(f'<line x1="40" y1="{y + 20}" x2="520" y2="{y - 20 if a < 0 else y + 50}" stroke="{FOSF}" stroke-width="12" stroke-linecap="round" opacity="0.9"/>')
x0 = 640
for k in range(3):
    p.append(caixa(x0, k * 176, 1024, 160, [GLIC, FOSF, OXID][k], [GLIC_T, FOSF_T, OXID_T][k], esp=3, rx=16))
# faixa
p.append(f'<rect x="{x0 + 40}" y="96" width="540" height="36" rx="18" fill="{GLIC}" opacity="0.3"/><rect x="{x0 + 40}" y="96" width="30" height="36" rx="10" fill="{GLIC}"/>')
rs += [rot(x0 + 30, 20, "É o começo de uma faixa", w=560, tam=30, cor=GLIC, peso=700, serif=True),
       rot(x0 + 20, 58, "150", w=80, tam=22, cor=GLIC, peso=700), rot(x0 + 530, 58, "300", w=80, tam=22, cor=GLIC, peso=700),
       rot(x0 + 620, 40, "dito sozinho, o mínimo vira meta; passar dos 300 traz benefício adicional", w=380, tam=22, cor=TINTA, lh=1.3)]
# metade
cx, cy = x0 + 110, 176 + 80
p.append(f'<path d="M{cx} {cy - 56} A 56 56 0 0 0 {cx} {cy + 56} Z" fill="{FOSF}"/>')
p.append(f'<path d="M{cx} {cy - 56} A 56 56 0 0 1 {cx} {cy + 56} Z" fill="none" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
rs += [rot(x0 + 200, 196, "É só a metade aeróbia", w=780, tam=30, cor=FOSF, peso=700, serif=True),
       rot(x0 + 200, 244, "a força em dois dias ou mais está na mesma recomendação", w=780, tam=22, cor=TINTA, lh=1.3)]
# escada do zero
for k in range(4):
    p.append(f'<rect x="{x0 + 40 + k * 44}" y="{352 + 130 - (k + 1) * 28}" width="40" height="{(k + 1) * 28}" fill="{OXID if k == 0 else CINZA}"/>')
rs += [rot(x0 + 250, 372, "Para quem está parado, assusta", w=740, tam=30, cor=OXID, peso=700, serif=True),
       rot(x0 + 250, 420, "entrega a distância, e não o primeiro degrau, que é o que vale mais", w=740, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "cento-e-cinquenta", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número mais repetido da saúde pública", "titulo": "O 150 é o número menos útil do documento",
          "destaque": "“Fazer alguma atividade é melhor do que não fazer nenhuma.” Está escrito no documento."})

# 2. as seis linhas numa régua de idade
p = [svg_abre(1664, 600, "Uma régua de idade com três faixas: criança e adolescente de 5 a 17 anos, adulto de 18 a 64, idoso de 65 ou mais, cada uma com a sua recomendação; embaixo, gestante e pós-parto, doença crônica e deficiência ligadas ao adulto: a mesma meta, adaptada"), defs(OXID)]
faixas = [(0, 420, "5 a 17 anos", "Criança e adolescente", "média de 60 min por dia de moderada a vigorosa · músculo e osso 3 dias por semana", AZUL, AZUL_T, "h:child-program"),
          (440, 600, "18 a 64 anos", "Adulto", "150 a 300 min moderada ou 75 a 150 vigorosa · força 2 dias ou mais · passar da faixa traz benefício", OXID, OXID_T, "h:person"),
          (1060, 604, "65 anos ou mais", "Idoso", "tudo do adulto · mais equilíbrio e força 3 dias ou mais: mais exigente, não menos", GLIC, GLIC_T, "h:elderly")]
rs = []
for (x, w, idade, t, rec, c, ct, ic) in faixas:
    p.append(f'<rect x="{x}" y="0" width="{w}" height="40" rx="8" fill="{c}"/>')
    rs.append(rot(x, 6, idade, w=w, tam=22, cor=PAPEL, peso=700, alinha="center"))
    p.append(caixa(x, 56, w, 240, c, ct, esp=3, rx=16))
    p.append(icone(ic, x + 20, 76, 70, c))
    rs.append(rot(x + 104, 90, t, w=w - 120, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(x + 20, 170, rec, w=w - 40, tam=22, cor=TINTA, lh=1.3))
extras = [(0, "Gestante e pós-parto", "atividade regular durante e depois: linha nova em 2020", "h:woman"),
          (560, "Doença crônica", "a mesma recomendação do adulto, com as adaptações necessárias", "h:heartbeat"),
          (1120, "Deficiência", "a mesma recomendação, quando possível, adaptada", "h:wheelchair")]
for (x, t, tx, ic) in extras:
    p.append(f'<path d="M740 300 C 740 350, {x + 272} 330, {x + 272} 380" fill="none" stroke="{OXID}" stroke-width="3"{TRACO} marker-end="url(#m0)"/>')
    p.append(caixa(x, 400, 544, 200, OXID, CARTAO, esp=3, rx=16))
    p.append(icone(ic, x + 20, 420, 60, OXID))
    rs.append(rot(x + 96, 432, t, w=430, tam=28, cor=OXID, peso=700, serif=True))
    rs.append(rot(x + 20, 500, tx, w=504, tam=22, cor=TINTA, lh=1.3))
p.append(f'<rect x="560" y="322" width="360" height="40" rx="20" fill="{PAPEL}" stroke="{OXID}" stroke-width="2"/>')
rs.append(rot(560, 330, "mesma meta, caminho adaptado", w=360, tam=20, cor=OXID, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "seis-linhas", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Organização Mundial da Saúde, 2020", "titulo": "O documento inteiro cabe em seis linhas"})

# 3. sentado: sem número mágico
p = [svg_abre(1664, 480, "Uma régua de horas sentado sem nenhuma linha de corte, só um ponto de interrogação riscado; embaixo, uma seta de trocas: sentado, em pé, andando, treinando, e cada troca conta"), defs(OXID)]
p.append(f'<rect x="200" y="60" width="1400" height="50" rx="25" fill="url(#gr)"/>')
p.insert(1, f'<defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="{OXID}" stop-opacity="0.25"/><stop offset="1" stop-color="{FOSF}" stop-opacity="0.55"/></linearGradient></defs>')
p.append(icone("t:home", 60, 40, 90, MUDO))
p.append(f'<line x1="1000" y1="20" x2="1000" y2="150" stroke="{TINTA}" stroke-width="4"{TRACO}/>')
p.append(f'<circle cx="1000" cy="85" r="34" fill="{PAPEL}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="970" y1="115" x2="1030" y2="55" stroke="{FOSF}" stroke-width="6"/>')
rs = [rot(200, 124, "horas sentado por dia", w=700, tam=22, cor=MUDO, alinha="center"),
      rot(986, 64, "?", w=28, tam=34, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1060, 160, "nenhum limite definido: a evidência não permitiu fixar um número", w=560, tam=22, cor=FOSF, peso=700, lh=1.3)]
trocas = [("t:user", "sentado"), ("h:person", "em pé"), ("h:walking", "andando"), ("h:running", "treinando")]
for k, (ic, t) in enumerate(trocas):
    x = 120 + k * 400
    p.append(icone(ic, x, 280, 100, [MUDO, OXID, OXID, OXID][k]))
    rs.append(rot(x - 50, 390, t, w=200, tam=24, cor=TINTA, peso=700, alinha="center"))
    if k < 3:
        p.append(seta(x + 130, 330, x + 360, 330, OXID, "m0", esp=5))
        rs.append(rot(x + 150, 290, "conta", w=190, tam=22, cor=OXID, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "sentado", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Atravessando as seis linhas", "titulo": "Menos tempo sentado, e não existe número mágico de horas",
          "destaque": "Quem te der um número exato de horas sentado está inventando o número. O que existe é a direção."})

# 4. três mudanças
p = [svg_abre(1664, 560, "Três painéis: o bloco de dez minutos riscado e trocado por pedaços pequenos que somam; 150 minutos cumpridos ao lado de dez horas sentado que continuam pesando; o documento com três populações novas acrescentadas")]
rs = []
for i, (t, c, ct) in enumerate([("Acabou o bloco de 10 minutos", OXID, OXID_T), ("Sentado virou recomendação própria", GLIC, GLIC_T), ("Novas populações por escrito", AZUL, AZUL_T)]):
    x = i * 564
    p.append(caixa(x, 0, 536, 560, c, ct, esp=3, rx=18))
    rs.append(rot(x + 24, 24, t, w=488, tam=30, cor=c, peso=700, serif=True, lh=1.15))
# painel 1
p.append(f'<rect x="40" y="130" width="300" height="70" rx="10" fill="none" stroke="{MUDO}" stroke-width="4"{TRACO}/>')
p.append(f'<line x1="30" y1="215" x2="350" y2="115" stroke="{FOSF}" stroke-width="7"/>')
rs.append(rot(40, 148, "só blocos de 10 min", w=300, tam=22, cor=MUDO, alinha="center"))
xs = 40
for k, (t, w) in enumerate([("escada", 100), ("6 min", 100), ("6 min", 100), ("6 min", 100)]):
    p.append(f'<rect x="{xs}" y="260" width="{w}" height="64" rx="10" fill="{OXID}"/>')
    rs.append(rot(xs, 278, t, w=w, tam=20, cor=PAPEL, peso=700, alinha="center"))
    xs += w + 12
rs += [rot(24, 350, "qualquer duração conta", w=488, tam=26, cor=OXID, peso=700),
       rot(24, 400, "para quem diz “não tenho meia hora”, é a diferença entre começar e não começar", w=488, tam=22, cor=TINTA, lh=1.3)]
# painel 2
x = 564
p.append(f'<rect x="{x + 40}" y="140" width="90" height="220" rx="8" fill="{OXID}"/>')
p.append(icone("t:check", x + 60, 90, 50, OXID))
p.append(f'<rect x="{x + 200}" y="140" width="280" height="220" rx="8" fill="{FOSF}" opacity="0.8"/>')
rs += [rot(x + 10, 370, "150 min por semana", w=150, tam=20, cor=OXID, peso=700, alinha="center", lh=1.2),
       rot(x + 200, 226, "10 h sentado por dia", w=280, tam=26, cor=PAPEL, peso=700, alinha="center"),
       rot(x + 200, 370, "continuam pesando", w=280, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(x + 24, 450, "uma coisa não resolve a outra", w=488, tam=26, cor=GLIC, peso=700)]
# painel 3
x = 1128
p.append(f'<rect x="{x + 40}" y="120" width="200" height="260" rx="8" fill="{CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
for k in range(5):
    p.append(f'<line x1="{x + 64}" y1="{160 + k * 40}" x2="{x + 216}" y2="{160 + k * 40}" stroke="{CINZA}" stroke-width="5" stroke-linecap="round"/>')
for k, ic in enumerate(["h:woman", "h:heartbeat", "h:wheelchair"]):
    p.append(f'<circle cx="{x + 330}" cy="{150 + k * 100}" r="40" fill="{CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
    p.append(icone(ic, x + 302, 122 + k * 100, 56, AZUL))
    rs.append(rot(x + 380, 136 + k * 100, ["gestação", "doença crônica", "deficiência"][k], w=150, tam=20, cor=AZUL, peso=700, lh=1.1))
rs += [rot(x + 24, 410, "vale para o meu paciente com doença? Vale, está escrito", w=488, tam=24, cor=AZUL, peso=700, lh=1.25),
       rot(x + 24, 480, "muda o caminho, não o destino", w=488, tam=22, cor=TINTA)]
p.append("</svg>")
S.append({"id": "mudou", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Em relação à versão anterior", "titulo": "Três mudanças de 2020 ainda estão mal incorporadas"})

# 5. o piso e as construções
p = [svg_abre(1664, 520, "À esquerda, uma multidão de milhões de pessoas vira uma laje: a diretriz é o piso; em cima da laje, três construções diferentes, uma por pessoa, com o joelho, o turno e a agenda de cada uma")]
for k in range(40):
    p.append(icone("h:person", 10 + (k % 8) * 48, 20 + (k // 8) * 56, 44, CINZA))
p.append(f'<rect x="0" y="400" width="1664" height="60" rx="8" fill="{OXID}"/>')
rs = [rot(0, 310, "milhões de pessoas, evidência em boa parte observacional", w=400, tam=22, cor=MUDO, lh=1.3),
      rot(20, 414, "a diretriz: o piso, o vocabulário, a legitimidade", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True),
      rot(0, 474, "a partir dele você prescreve; ele não é a prescrição", w=1664, tam=24, cor=OXID, peso=700, alinha="center")]
predios = [(560, [(120, GLIC), (60, AZUL), (90, GLIC)], "o joelho", "h:bandaged"),
           (900, [(80, AZUL), (140, GLIC), (60, AZUL)], "o turno de trabalho", "t:clock"),
           (1240, [(60, GLIC), (70, AZUL), (80, GLIC), (60, AZUL)], "a agenda", "t:calendar")]
for (x, blocos, t, ic) in predios:
    y = 400
    for (h, c) in blocos:
        p.append(f'<rect x="{x}" y="{y - h}" width="260" height="{h - 4}" rx="6" fill="{c}" opacity="0.8"/>')
        y -= h
    p.append(icone(ic, x + 100, y - 70, 60, TINTA))
    rs.append(rot(x - 20, y - 110, t, w=300, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "piso", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um cuidado de leitura", "titulo": "A diretriz é o piso, e cada prescrição é uma construção"})

# 6. quatro conversas numa régua de minutos
p = [svg_abre(1664, 560, "Uma régua de minutos por semana de zero a mais de 300 com a faixa de 150 a 300 pintada; quatro pessoas marcadas: uma no zero, uma além dos 300, uma que faz só o aeróbio e uma com doença crônica, cada uma com a frase que funciona")]
x0, x1 = 60, 1600
def xm(m): return x0 + (x1 - x0) * m / 420
p.append(f'<line x1="{x0}" y1="240" x2="{x1}" y2="240" stroke="{MUDO}" stroke-width="4"/>')
p.append(f'<rect x="{xm(150)}" y="216" width="{xm(300) - xm(150)}" height="48" rx="8" fill="{OXID}" opacity="0.25"/>')
rs = [rot(xm(150), 184, "a faixa: 150 a 300", w=xm(300) - xm(150), tam=22, cor=OXID, peso=700, alinha="center")]
for m in (0, 150, 300):
    rs.append(rot(xm(m) - 40, 276, str(m), w=80, tam=22, cor=MUDO, peso=600, alinha="center"))
rs.append(rot(x1 - 300, 276, "minutos por semana", w=300, tam=20, cor=MUDO, alinha="right"))
for (m, ic, c) in [(0, "t:user", GLIC), (380, "h:running", AZUL)]:
    p.append(f'<circle cx="{xm(m)}" cy="240" r="16" fill="{c}"/>')
    p.append(icone(ic, xm(m) - 36, 136, 72, c))
rs += [rot(xm(0) + 60, 40, "Com quem está em zero", w=520, tam=30, cor=GLIC, peso=700, serif=True),
       rot(xm(0) + 60, 86, "fale o degrau, não o número: “dez minutos, cinco dias, depois do almoço”", w=520, tam=22, lh=1.3, cor=TINTA),
       rot(xm(380) - 620, 40, "Com quem treina muito", w=560, tam=30, cor=AZUL, peso=700, serif=True, alinha="right"),
       rot(xm(380) - 620, 86, "mostre a faixa inteira: acima de 300 ainda há benefício; o limite vem da recuperação dela", w=560, tam=22, lh=1.3, cor=TINTA, alinha="right")]
for k, (t, tx, ic, c, ct) in enumerate([("Com quem esquece a força", "está no documento, com a mesma autoridade: não é preferência sua", "t:barbell", FOSF, FOSF_T),
                                        ("Com quem ouviu “pegue leve”", "doença crônica: a meta é a mesma, está escrito; muda o caminho", "h:heartbeat", OXID, OXID_T)]):
    x = 120 + k * 760
    p.append(caixa(x, 340, 700, 200, c, ct, esp=3, rx=18))
    p.append(icone(ic, x + 24, 370, 70, c))
    rs.append(rot(x + 114, 376, t, w=560, tam=28, cor=c, peso=700, serif=True))
    rs.append(rot(x + 114, 430, tx, w=560, tam=24, cor=TINTA, lh=1.3))
p.append(f'<path d="M{xm(225)} 300 L{xm(225)} 336" stroke="{OXID}" stroke-width="3"{TRACO}/>')
p.append("</svg>")
S.append({"id": "conversas", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Na segunda-feira", "titulo": "A diretriz vira quatro conversas diferentes"})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "A diretriz tira o “não sei quanto” da conversa",
          "regras": ["É uma faixa, tem força e começa em sair do zero.", "Idoso tem recomendação mais exigente; doença crônica tem a mesma meta.",
                     "Diretriz é piso: a prescrição individual dá o resto."],
          "quem": "“A recomendação é de 150 a 300 minutos e inclui força” é de todos. “Faça três séries de dez com essa carga” é de quem prescreve treino ou conduz a reabilitação.",
          "proxima": "Quem cuida de quem: as funções de uma equipe"})

F = S[-1]
F["cards"] = [{"ic": "t:writing", "t": "Quem faz o quê", "x": F.pop("quem")}, {"ic": "t:arrow-right", "t": "Próxima conversa", "x": F["proxima"][0].upper() + F["proxima"][1:] + "."}]

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-04.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-04.json"), "w"), ensure_ascii=False, indent=1)
print("01-04.json:", len(S), "slides")
