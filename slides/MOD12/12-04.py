"""Spec do deck 12.4. Gera 12-04.json ao lado deste arquivo."""
from _base import *

S = []


def menino(x, base, alt, cor):
    """Silhueta simples de pé: cabeça e corpo, alt em px."""
    r = alt * 0.09
    return (f'<circle cx="{x}" cy="{base - alt + r:.0f}" r="{r:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.12:.0f}" y="{base - alt + 2 * r + 6:.0f}" width="{alt * 0.24:.0f}" height="{alt * 0.45:.0f}" rx="{alt * 0.05:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.1:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>'
            f'<rect x="{x + alt * 0.02:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>')


def camisa(x, y, s, cor):
    """Camisa de jogo vista de frente, num quadrado de lado s."""
    k = s / 100
    pts = [(30, 0), (70, 0), (100, 20), (88, 42), (78, 36), (78, 100), (22, 100), (22, 36), (12, 42), (0, 20)]
    d = " ".join(f"{x + a * k:.0f},{y + b * k:.0f}" for a, b in pts)
    return f'<polygon points="{d}" fill="{cor}"/>'


TRI = [GLIC, OXID, AZUL, FOSF]

# 1. a lista da seleção
MESES = ["jan", "jan", "jan", "fev", "fev", "mar", "mar", "abr", "abr", "mai", "jun", "jun", "ago", "set", "out", "dez"]
TRIM = [0] * 7 + [1] * 5 + [2] * 2 + [3] * 2
p = [svg_abre(1664, 450, "Lista de uma seleção regional sub-14 de handebol com dezesseis atletas e o mês de nascimento de cada um. Agrupados por trimestre: 7, 5, 2 e 2. Números ilustrativos")]
rs = []
for i, (m, t) in enumerate(zip(MESES, TRIM)):
    x, y = (i % 4) * 184, (i // 4) * 100
    p.append(camisa(x, y, 86, TRI[t]))
    rs.append(rot(x + 92, y + 22, m, w=86, tam=28, cor=TINTA, peso=700))
for k, (n, rot_t) in enumerate(zip([7, 5, 2, 2], ["jan–mar", "abr–jun", "jul–set", "out–dez"])):
    x = 900 + k * 190
    for j in range(n):
        p.append(f'<circle cx="{x + 60}" cy="{360 - j * 44}" r="18" fill="{TRI[k]}"/>')
    rs.append(rot(x - 20, 396, f"{rot_t}: {n}", w=160, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(f'<line x1="880" y1="{360 - 3 * 44 - 22}" x2="1664" y2="{360 - 3 * 44 - 22}" stroke="{MUDO}" stroke-width="3" stroke-dasharray="10 8"/>')
rs.append(rot(1104, 110, "se o mês não importasse: 4 por trimestre", w=560, tam=22, cor=MUDO, alinha="right"))
rs.append(rot(0, 410, "números ilustrativos", w=720, tam=22, cor=MUDO))
diagrama(S, "elenco", 450, p, rs, eyebrow="Uma seleção regional sub-14 de handebol", titulo="Os melhores da seleção nasceram no começo do ano")

# 2. a conta
p = [svg_abre(1664, 460, "Calendário de um ano com dois meninos nas pontas, um nascido em 1º de janeiro e outro em 31 de dezembro, na mesma categoria. Entre eles, 364 dias. Embaixo, a diferença como fração da vida: 12% aos 8 anos, 10% aos 10 e 7% aos 14"), defs(TINTA)]
rs = []
p.append(f'<rect x="200" y="150" width="1264" height="20" rx="10" fill="{GRADE}"/>')
for i in range(13):
    p.append(f'<line x1="{200 + i * 105.3:.0f}" y1="140" x2="{200 + i * 105.3:.0f}" y2="180" stroke="{MUDO}" stroke-width="2"/>')
p.append(menino(110, 190, 190, GLIC))
p.append(menino(1554, 190, 160, AZUL))
rs += [rot(0, 200, "1º de janeiro", w=220, tam=24, cor=GLIC, peso=700, alinha="center"),
       rot(1444, 200, "31 de dezembro", w=220, tam=24, cor=AZUL, peso=700, alinha="center")]
p.append(seta(260, 100, 1404, 100, TINTA, "m0", 4))
p.append(seta(1404, 100, 260, 100, TINTA, "m0", 4))
rs.append(rot(632, 40, "364 dias: quase um ano", w=400, tam=32, cor=TINTA, peso=700, alinha="center", serif=True))
for j, (idade, pct) in enumerate([("aos 8 anos", 12), ("aos 10 anos", 10), ("aos 14 anos", 7)]):
    y = 270 + j * 64
    rs.append(rot(0, y + 6, idade, w=260, tam=26, cor=TINTA, peso=700, alinha="right"))
    p.append(f'<rect x="290" y="{y}" width="{pct * 90}" height="44" rx="8" fill="{FOSF}"/>')
    rs.append(rot(290 + pct * 90 + 20, y + 4, f"{pct}% da vida", w=260, tam=28, cor=FOSF, peso=700))
diagrama(S, "conta", 460, p, rs, eyebrow="O número", titulo="Na mesma categoria cabe quase um ano de diferença")

# 3. o esperado e o observado
p = [svg_abre(1664, 440, "Quatro colunas de trimestres. Linha tracejada em 25%: o esperado, se o mês não importasse. Colunas decrescentes do primeiro ao quarto trimestre: o padrão observado, esquema. Ficha da meta-análise de 2009: 38 estudos, 253 amostras, 14 esportes, 16 países, 1984 a 2007. Efeito maior aos 15 a 18 anos, no nível representativo e nos esportes populares")]
rs = []
base = 380
for k, h in enumerate([36, 28, 20, 16]):
    x = 80 + k * 170
    p.append(f'<rect x="{x}" y="{base - h * 9}" width="120" height="{h * 9}" rx="6" fill="{TRI[k]}"/>')
    rs.append(rot(x, base + 14, f"{k + 1}º tri", w=120, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(f'<line x1="40" y1="{base}" x2="760" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="40" y1="{base - 25 * 9}" x2="760" y2="{base - 25 * 9}" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
rs += [rot(440, base - 25 * 9 - 44, "esperado: 25% cada", w=320, tam=22, cor=TINTA, peso=600, alinha="right"),
       rot(40, 0, "esquema", w=200, tam=22, cor=MUDO)]
p.append(caixa(860, 0, 804, 190, AZUL, AZUL_T, esp=3, rx=16))
rs += [rot(884, 18, "Primeira meta-análise, 2009", w=760, tam=30, cor=AZUL, peso=700, serif=True),
       rot(884, 76, "38 estudos, de 1984 a 2007", w=760, tam=26, cor=TINTA, peso=600),
       rot(884, 124, "253 amostras · 14 esportes · 16 países", w=760, tam=26, cor=TINTA, peso=600)]
p.append(caixa(860, 214, 804, 226, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(884, 230, "Efeito pequeno em média, maior em:", w=760, tam=26, cor=FOSF, peso=700))
for j, t in enumerate(["adolescentes de 15 a 18 anos", "seleções regionais e nacionais", "esportes populares"]):
    p.append(f'<circle cx="900" cy="{298 + j * 48}" r="8" fill="{FOSF}"/>')
    rs.append(rot(924, 282 + j * 48, t, w=720, tam=26, cor=TINTA, peso=600))
diagrama(S, "esperado", 440, p, rs, eyebrow="O esperado e o observado", titulo="Em vez de um quarto por trimestre, uma escada",
         fonte="Sports Med 2009; J Sports Sci 2005")

# 4. o ciclo
p = [svg_abre(1664, 440, "Ciclo de quatro elos: mais velho e mais desenvolvido, parece melhor na peneira, é selecionado, mais treino, mais jogo e técnico melhor; e volta ao começo, agora de fato melhor. Fora do ciclo, quem nasceu no fim do ano: menos jogo, técnico menos experiente, parte desiste"), defs(OXID, FOSF)]
rs = []
nos = [(330, 0, "mais velho e mais desenvolvido"), (680, 172, "parece melhor na peneira"), (330, 344, "é selecionado"), (0, 172, "mais treino, mais jogo, técnico melhor")]
for x, y, t in nos:
    p.append(caixa(x, y, 400, 96, OXID, OXID_T, esp=3, rx=18))
    rs.append(rot(x + 16, y + 16, t, w=368, tam=25, cor=TINTA, peso=700, alinha="center", lh=1.2))
for x1, y1, x2, y2 in [(740, 60, 870, 160), (870, 280, 740, 380), (320, 380, 190, 280), (190, 160, 320, 60)]:
    p.append(seta(x1, y1, x2, y2, OXID, "m0", 5))
rs.append(rot(410, 170, "anos depois, de fato melhor", w=240, tam=24, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append(seta(1090, 220, 1170, 220, FOSF, "m1", 5))
p.append(caixa(1190, 0, 474, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(1214, 20, "Quem nasceu no fim do ano", w=426, tam=28, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["menos jogo", "técnico menos experiente", "parte desiste"]):
    rs.append(rot(1214, 100 + j * 56, "· " + t, w=426, tam=26, cor=TINTA, peso=600))
rs.append(rot(1214, 300, "cada peneira escolhe entre quem passou na anterior", w=426, tam=24, cor=MUDO, serif=True, lh=1.3))
diagrama(S, "ciclo", 440, p, rs, eyebrow="Por que o efeito cresce com a idade", titulo="A seleção transforma vantagem de idade em preparo")

# 5. idade relativa e maturação
p = [svg_abre(1664, 440, "Grade dois por dois. Colunas: nasceu cedo no ano e nasceu tarde no ano. Linhas: amadurece cedo e amadurece tarde. Nasceu cedo e amadurece cedo: duas vantagens. Nasceu tarde e amadurece tarde: dupla desvantagem")]
rs = []
x0 = 300
for k, t in enumerate(["nasceu cedo no ano", "nasceu tarde no ano"]):
    rs.append(rot(x0 + k * 580, 0, t, w=560, tam=28, cor=TINTA, peso=700, alinha="center"))
for j, t in enumerate(["amadurece cedo", "amadurece tarde"]):
    rs.append(rot(0, 110 + j * 180, t, w=270, tam=28, cor=TINTA, peso=700, alinha="right"))
celulas = [("duas vantagens juntas", OXID, OXID_T), ("a maturação compensa o calendário", GLIC, GLIC_T),
           ("o calendário compensa a maturação", GLIC, GLIC_T), ("dupla desvantagem", FOSF, FOSF_T)]
for i, (t, c, f) in enumerate(celulas):
    x, y = x0 + (i % 2) * 580, 56 + (i // 2) * 180
    p.append(caixa(x, y, 560, 164, c, f, esp=4 if i in (0, 3) else 2, rx=18))
    rs.append(rot(x + 24, y + 54, t, w=512, tam=30 if i in (0, 3) else 26, cor=c if i in (0, 3) else TINTA, peso=700, alinha="center"))
rs.append(rot(1480, 290, "o mais novo da turma e atrás no relógio do corpo", w=184, tam=22, cor=FOSF, peso=600, lh=1.25))
diagrama(S, "soma", 440, p, rs, eyebrow="Calendário e biologia", titulo="Idade relativa e maturação se somam")

# 6. quem paga a conta
p = [svg_abre(1664, 450, "Perfil típico: adolescente de 14 anos, nascido em dezembro, dispensado por porte físico. Consequências: abandona o esporte, conclui que não é bom, compensa treinando com dor e procurando atalho. No consultório: ele não está crescendo; a avaliação mostra estatura e velocidade normais, antes do pico: nada a tratar, algo a explicar"), defs(TINTA)]
rs = []
p.append(menino(150, 300, 260, AZUL))
p.append(caixa(0, 320, 300, 130, AZUL, AZUL_T, esp=3, rx=16))
rs += [rot(16, 334, "14 anos · dezembro", w=268, tam=24, cor=AZUL, peso=700, alinha="center"),
       rot(16, 380, "dispensado “por porte físico”", w=268, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.2)]
for j, t in enumerate(["abandona o esporte", "conclui que não é bom", "compensa: treina com dor, procura atalho"]):
    y = 10 + j * 100
    p.append(seta(320, 200, 400, y + 40, TINTA, "m0", 3))
    p.append(caixa(410, y, 560, 80, FOSF, FOSF_T, esp=2, rx=14))
    rs.append(rot(430, y + 22, t, w=520, tam=25, cor=TINTA, peso=700))
p.append(seta(320, 360, 400, 360, TINTA, "m0", 3))
p.append(caixa(410, 310, 560, 80, AZUL, AZUL_T, esp=3, rx=14))
rs.append(rot(430, 332, "no consultório: “ele não está crescendo”", w=520, tam=25, cor=AZUL, peso=700))
p.append(caixa(1030, 0, 634, 450, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1054, 20, "O que a avaliação costuma mostrar", w=586, tam=28, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["estatura dentro da faixa", "velocidade de crescimento normal", "ainda antes do pico", "nascido perto do fim do ano"]):
    p.append(icone("t:check", 1054, 92 + j * 60, 32, OXID))
    rs.append(rot(1100, 92 + j * 60, t, w=540, tam=25, cor=TINTA, peso=600))
p.append(caixa(1054, 352, 586, 76, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(1066, 372, "nada a tratar; algo a explicar", w=562, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "custo", 450, p, rs, eyebrow="Quem paga a conta", titulo="O dispensado por porte físico quase sempre é normal")

# 7. a virada no rúgbi
p = [svg_abre(1664, 440, "Dois painéis, esquema. Na entrada da via de formação do rúgbi, nascidos no início do ano são muitos e os do fim do ano poucos. Entre os que entraram, a chance de chegar ao profissional é maior para os nascidos no fim do ano. Hipótese do azarão: discutida, não demonstrada; a virada fala dos que sobreviveram ao filtro")]
rs = []
for k, (titulo_p, alturas) in enumerate([("Na entrada", (230, 90)), ("Entre os que entraram: chegar ao profissional", (110, 200))]):
    x0 = k * 860
    rs.append(rot(x0, 0, titulo_p, w=780, tam=28, cor=TINTA, peso=700, serif=True))
    for j, (h, c, t) in enumerate(zip(alturas, (GLIC, AZUL), ("início do ano", "fim do ano"))):
        x = x0 + 120 + j * 300
        p.append(f'<rect x="{x}" y="{310 - h}" width="180" height="{h}" rx="8" fill="{c}"/>')
        rs.append(rot(x - 30, 322, t, w=240, tam=24, cor=c, peso=700, alinha="center"))
    p.append(f'<line x1="{x0 + 60}" y1="310" x2="{x0 + 720}" y2="310" stroke="{TINTA}" stroke-width="3"/>')
rs.append(rot(1500, 0, "esquema", w=164, tam=22, cor=MUDO, alinha="right"))
p.append(caixa(0, 372, 1664, 68, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 390, "Hipótese do azarão: discutida, não demonstrada. A virada fala de quem passou pelo filtro.", w=1624, tam=24, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "inversao", 440, p, rs, eyebrow="Rúgbi inglês, estudos de 2014 e 2021", titulo="Entre os que entram, o mais novo chega mais longe",
         fonte="J Sports Sci 2014; Front Sports Act Living 2021")

# 8. o que reduz o viés
p = [svg_abre(1664, 450, "Experimento com olheiros em três grupos: sem informação de idade, viés; com a data de nascimento, viés; com camisas numeradas pela idade relativa, de 1 o mais velho a 16 o mais novo, sem viés. Outras medidas: adiar a seleção definitiva, rodar a data de corte, acompanhar a distribuição por trimestre, agrupar por maturação")]
rs = []
for j, (t, res, c, f) in enumerate([("sem informação de idade", "viés", FOSF, FOSF_T), ("com a data de nascimento", "viés", FOSF, FOSF_T),
                                     ("camisa numerada pela idade", "sem viés", OXID, OXID_T)]):
    y = j * 150
    p.append(caixa(0, y, 960, 130, c, f, esp=3, rx=16))
    p.append(icone("h:people", 20, y + 25, 80, c))
    rs.append(rot(120, y + 44, t, w=420, tam=26, cor=TINTA, peso=700))
    rs.append(rot(800, y + 40, res, w=140, tam=32, cor=c, peso=700, alinha="center", serif=True))
for k, n in enumerate([1, 6, 11, 16]):
    x = 540 + k * 60
    p.append(camisa(x, 326, 56, OXID))
    rs.append(rot(x + 4, 338, str(n), w=48, tam=20, cor=PAPEL, peso=700, alinha="center"))
p.append(caixa(1020, 0, 644, 450, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(1044, 20, "Outras medidas", w=596, tam=30, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["adiar a seleção definitiva", "rodar a data de corte", "acompanhar a distribuição por trimestre", "agrupar por maturação"]):
    p.append(f'<circle cx="1058" cy="{112 + j * 82}" r="9" fill="{AZUL}"/>')
    rs.append(rot(1082, 94 + j * 82, t, w=560, tam=26, cor=TINTA, peso=600, lh=1.2))
diagrama(S, "medidas", 450, p, rs, eyebrow="Experimento de 2017 com olheiros de futebol", titulo="A idade precisa estar à vista na hora de avaliar",
         fonte="J Sports Sci 2017")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Efeito da idade relativa", "titulo": "Na base, avaliar sempre com o calendário à vista",
          "regras": ["Na mesma categoria cabe quase um ano; aos oito anos, doze por cento da vida",
                     "A seleção transforma vantagem de idade em preparo, e o efeito cresce com a idade",
                     "Saber do viés não basta: a idade relativa precisa estar visível na avaliação"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e seleciona", "x": "Põe a idade relativa à vista e adia a seleção definitiva."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Avalia o crescimento antes de qualquer conversa sobre hormônio e diz o que é normal."},
                    {"ic": "t:calendar", "t": "O clube", "x": "Acompanha a distribuição por trimestre em cada categoria."}]})

salvar("12-04.json", {"arquivo": "aulas/MOD12/12-04-efeito-da-idade-relativa.md",
                      "titulo": "Efeito da idade relativa", "subtitulo": "Quase um ano dentro da mesma categoria",
                      "nota_capa": "Entra pela lista de uma seleção regional sub-14 de handebol e o mês em que cada atleta nasceu.",
                      "secoes": {"elenco": ["O número.", "capa"], "ciclo": ["O mecanismo.", "ciclo"],
                                 "custo": ["O custo e a virada.", "custo"], "medidas": ["O que reduz o viés.", "medidas"]},
                      "slides": S})
