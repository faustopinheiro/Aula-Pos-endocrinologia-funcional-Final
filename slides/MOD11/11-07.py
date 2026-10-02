"""Spec do deck 11.7. Gera 11-07.json ao lado deste arquivo."""
from _base import *

S = []
X = lambda m: 60 + m / 30 * 1540


def raio(x, y, c):
    return f'<path d="M {x - 10} {y - 30} L {x + 8} {y - 6} L {x - 6} {y + 2} L {x + 10} {y + 30}" stroke="{c}" stroke-width="6" fill="none" stroke-linejoin="round"/>'


# 1. a linha do tempo
p = [svg_abre(1664, 470, "Linha do tempo de trinta meses ilustrativos. Mês zero: primeira fratura. Mês nove: segunda fratura. Entre os dois: voltou a jogar. Depois do mês nove: energia, investigação, carga. Mês dezesseis: ciclo volta. Mês trinta: densitometria de controle. Uma linha pontilhada do começo até o mês dezesseis: sem menstruar")]
p.append(f'<line x1="40" y1="200" x2="1624" y2="200" stroke="{TINTA}" stroke-width="4"/>')
rs = []
for m in (0, 9, 16, 30):
    p.append(f'<line x1="{X(m):.0f}" y1="190" x2="{X(m):.0f}" y2="210" stroke="{TINTA}" stroke-width="4"/>')
    rs.append(rot(X(m) - 60, 214, f"mês {m}", w=120, tam=22, cor=MUDO, alinha="center"))
p.append(f'<rect x="{X(0) + 20:.0f}" y="110" width="{X(9) - X(0) - 40:.0f}" height="50" rx="10" fill="{CINZA}" opacity="0.5"/>')
rs.append(rot(X(0) + 20, 120, "voltou a jogar", w=X(9) - X(0) - 40, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append(f'<rect x="{X(9) + 20:.0f}" y="110" width="{X(30) - X(9) - 40:.0f}" height="50" rx="10" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
rs.append(rot(X(9) + 20, 120, "energia, investigação, carga", w=X(30) - X(9) - 40, tam=26, cor=OXID, peso=700, alinha="center"))
for m, t in ((0, "primeira fratura"), (9, "segunda fratura")):
    p.append(raio(X(m), 50, FOSF))
    rs.append(rot(X(m) + 24, 30, t, w=300, tam=26, cor=FOSF, peso=700))
p.append(f'<circle cx="{X(16):.0f}" cy="300" r="16" fill="{FOSF}"/>')
rs += [rot(X(16) - 150, 330, "ciclo volta", w=300, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(X(30) - 330, 300, "densitometria de controle", w=330, tam=26, cor=TINTA, peso=700, alinha="right")]
p.append(f'<line x1="{X(0):.0f}" y1="410" x2="{X(16):.0f}" y2="410" stroke="{FOSF}" stroke-width="6"{TRACO}/>')
rs.append(rot(X(0), 424, "sem menstruar", w=600, tam=26, cor=FOSF, peso=700))
diagrama(S, "linha", 470, p, rs, eyebrow="Uma jogadora de vôlei, no começo dos vinte", titulo="A primeira fratura consolidou; o que a causou continuou",
         fonte="Meses ilustrativos")

# 2. a régua da atleta
p = [svg_abre(1664, 440, "Régua de Z-score de menos 3 a mais 2. Faixa de menos 2 a mais 2: laudo, dentro do esperado. Faixa acima de zero: esperado para quem salta. Linha em menos 1: abaixo disso, baixa para atleta de impacto. Coluna lombar em menos 1,4; colo do fêmur em mais 0,3")]
Z = lambda z: 80 + (z + 3) / 5 * 1500
rs = []
p.append(f'<rect x="{Z(-2):.0f}" y="40" width="{Z(2) - Z(-2):.0f}" height="60" rx="12" fill="{CINZA}" opacity="0.45"/>')
rs.append(rot(Z(-2), 54, "laudo: dentro do esperado para a idade", w=Z(2) - Z(-2), tam=26, cor=TINTA, peso=600, alinha="center"))
p.append(f'<rect x="{Z(0):.0f}" y="120" width="{Z(2) - Z(0):.0f}" height="60" rx="12" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
rs.append(rot(Z(0), 134, "esperado para quem salta", w=Z(2) - Z(0), tam=26, cor=OXID, peso=700, alinha="center"))
p.append(f'<line x1="{Z(-3):.0f}" y1="260" x2="{Z(2):.0f}" y2="260" stroke="{TINTA}" stroke-width="4"/>')
for z in range(-3, 3):
    p.append(f'<line x1="{Z(z):.0f}" y1="250" x2="{Z(z):.0f}" y2="270" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(Z(z) - 40, 280, f"{z:+d}".replace("+0", "0").replace("-", "−"), w=80, tam=24, cor=MUDO, alinha="center"))
p.append(f'<line x1="{Z(-1):.0f}" y1="110" x2="{Z(-1):.0f}" y2="250" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
rs.append(rot(Z(-1) - 420, 130, "abaixo de −1: baixa para atleta de impacto", w=400, tam=24, cor=FOSF, peso=700, alinha="right", lh=1.2))
for z, t, c in ((-1.4, "coluna −1,4", FOSF), (0.3, "fêmur +0,3", OXID)):
    p.append(f'<circle cx="{Z(z):.0f}" cy="260" r="14" fill="{c}" stroke="{CARTAO}" stroke-width="3"/>')
    rs.append(rot(Z(z) - 130, 340, t, w=260, tam=30, cor=c, peso=700, alinha="center", serif=True))
diagrama(S, "regua", 440, p, rs, eyebrow="O laudo do mês zero", titulo="Para quem salta, um Z-score de −1,4 não é normal",
         fonte="Coalizão da tríade, Br J Sports Med 2014")

# 3. trabecular e cortical
p = [svg_abre(1664, 440, "Lado a lado, uma vértebra em corte com a malha trabecular rarefeita e o colo do fêmur com casca cortical grossa e setas de impacto chegando de baixo. Trabecular: troca rápida, depende de estrogênio. Cortical: protegido pelo impacto. Esquema"), defs(OXID)]
rs = []
p.append(caixa(0, 0, 800, 440, FOSF, FOSF_T, esp=3, rx=18))
p.append(f'<rect x="200" y="60" width="400" height="240" rx="40" fill="{CARTAO}" stroke="{TINTA}" stroke-width="6"/>')
for i in range(9):
    for j in range(5):
        if (i * 3 + j * 5) % 4:
            p.append(f'<line x1="{230 + i * 42}" y1="{90 + j * 44}" x2="{250 + i * 42}" y2="{120 + j * 44}" stroke="{FOSF}" stroke-width="4"/>')
rs += [rot(24, 320, "Vértebra: trabecular", w=752, tam=30, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(24, 372, "troca rápida; perde primeiro sem estrogênio", w=752, tam=26, cor=TINTA, alinha="center")]
p.append(caixa(864, 0, 800, 440, OXID, OXID_T, esp=3, rx=18))
p.append(f'<path d="M 1000 260 Q 1100 240 1180 150 Q 1230 90 1320 80 Q 1400 80 1400 150 Q 1390 210 1300 200 Q 1240 200 1210 250 Q 1180 300 1180 300 L 1060 300 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="14"/>')
for k in range(3):
    p.append(seta(1080 + k * 40, 300, 1080 + k * 40, 236, OXID, "m0", 5))
rs += [rot(888, 320, "Colo do fêmur: mais cortical", w=752, tam=30, cor=OXID, peso=700, serif=True, alinha="center"),
       rot(888, 372, "o impacto segura a densidade", w=752, tam=26, cor=TINTA, alinha="center")]
rs.append(rot(1520, 20, "esquema", w=130, tam=22, cor=MUDO, alinha="right"))
diagrama(S, "sitios", 440, p, rs, eyebrow="Por que os dois sítios discordam", titulo="A coluna perde primeiro; o impacto protege o fêmur",
         destaque="Densitometria em atleta com disfunção menstrual: coluna e fêmur. O fêmur bom não tranquiliza sobre a coluna.", destaque_cor="tinta")

# 4. o mês nove
p = [svg_abre(1664, 470, "A tíbia com duas marcas de fratura, uma consolidada e outra nova. O que foi feito: imobilização, retorno progressivo, liberação. O que não foi feito: pergunta sobre o ciclo, conta da energia, investigação da amenorreia, leitura do laudo com a régua da atleta")]
p.append(f'<path d="M 150 20 Q 130 240 150 450 L 230 450 Q 250 240 230 20 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="5"/>')
p.append(f'<line x1="140" y1="150" x2="200" y2="140" stroke="{CINZA}" stroke-width="8"/>')
p.append(raio(200, 330, FOSF))
rs = [rot(250, 126, "mês 0: consolidou", w=240, tam=24, cor=MUDO, peso=600), rot(250, 316, "mês 9: nova fratura", w=240, tam=24, cor=FOSF, peso=700)]
for k, (t, itens, c, f) in enumerate([("Foi feito", ["proteção da fratura", "retorno progressivo", "liberação"], OXID, OXID_T),
                                      ("Não foi feito", ["perguntar pelo ciclo", "fazer a conta da energia", "investigar a amenorreia", "ler o laudo com a régua da atleta"], FOSF, FOSF_T)]):
    x = 520 + k * 580
    p.append(caixa(x, 0, 544, 470, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 20, t, w=500, tam=32, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 34, 100 + j * 80, "· " + it, w=490, tam=27, cor=TINTA, peso=600, lh=1.2))
diagrama(S, "mesnove", 470, p, rs, eyebrow="Entre o mês zero e o mês nove", titulo="Cada um tratou bem a sua parte; ninguém juntou as partes")

# 5. a escada de risco
p = [svg_abre(1664, 460, "Degraus que sobem. Um fator de risco: de 15 a 20 por cento com lesão óssea. Fatores combinados: de 30 a 50 por cento. Duas combinações: densidade baixa para atleta mais 12 horas ou mais por semana, 29,7 por cento; 12 horas ou mais mais esporte de magreza mais restrição alimentar, 46,2 por cento")]
rs = []
degraus = [("um fator", "15 a 20%", 120, GLIC), ("combinados", "30 a 50%", 260, FOSF)]
for j, (t, v, h, c) in enumerate(degraus):
    x = j * 400
    p.append(f'<rect x="{x}" y="{460 - h - 60}" width="380" height="{h}" rx="10" fill="{c}"/>')
    rs += [rot(x, 460 - h - 40, v, w=380, tam=44, cor=PAPEL, peso=700, serif=True, alinha="center"),
           rot(x, 420, t, w=380, tam=26, cor=TINTA, peso=700, alinha="center")]
for j, (v, t) in enumerate([("29,7%", "densidade baixa para atleta + 12 h ou mais por semana"), ("46,2%", "12 h ou mais + esporte de magreza + restrição alimentar")]):
    y = j * 210
    p.append(caixa(880, y, 784, 190, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(904, y + 24, v, w=240, tam=60, cor=FOSF, peso=700, serif=True), rot(1150, y + 40, t, w=490, tam=26, cor=TINTA, peso=600, lh=1.3)]
diagrama(S, "escada", 460, p, rs, eyebrow="Estudo prospectivo de 2014, cerca de 260 meninas e mulheres ativas", titulo="Fatores de risco somam: de um em cinco a quase metade",
         fonte="Proporção com lesão óssea por estresse no seguimento; Am J Sports Med 2014")

# 6. a pirâmide de tratamento
p = [svg_abre(1664, 460, "Pirâmide de tratamento. Base: energia, carga e comportamento. Meio: estradiol transdérmico com progesterona cíclica, se o ciclo não volta e a densidade é baixa. Ao lado, riscados: pílula combinada e bisfosfonato")]
rs = []
p.append(f'<path d="M 40 440 L 1000 440 L 860 260 L 180 260 Z" fill="{OXID}"/>')
rs += [rot(180, 316, "energia, carga e comportamento", w=680, tam=34, cor=PAPEL, peso=700, alinha="center", serif=True), rot(180, 372, "o tratamento da causa", w=680, tam=24, cor=PAPEL, alinha="center")]
p.append(f'<path d="M 200 240 L 840 240 L 700 60 L 340 60 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
rs += [rot(300, 90, "estradiol transdérmico + progesterona cíclica", w=440, tam=26, cor=AZUL, peso=700, alinha="center", lh=1.2),
       rot(260, 180, "se o ciclo não volta e a densidade segue baixa", w=520, tam=22, cor=TINTA, alinha="center")]
for j, t in enumerate(["pílula combinada", "bisfosfonato"]):
    y = 80 + j * 180
    p.append(caixa(1100, y, 564, 120, FOSF, FOSF_T, esp=3, rx=14))
    rs.append(rot(1120, y + 38, t, w=524, tam=32, cor=FOSF, peso=700, alinha="center"))
    p.append(f'<line x1="1130" y1="{y + 100}" x2="1634" y2="{y + 20}" stroke="{FOSF}" stroke-width="6"/>')
diagrama(S, "piramide", 460, p, rs, eyebrow="A partir do mês nove", titulo="A causa na base; o hormônio só se faltar",
         fonte="Diretriz da sociedade de endocrinologia, J Clin Endocrinol Metab 2017")

# 7. a janela de construção
p = [svg_abre(1664, 440, "Curva de massa óssea ao longo da vida, subindo na adolescência, pico perto do fim da segunda década, descendo devagar depois. Janela de construção sombreada. Dois pontos: dois anos sem menstruar aos 19 e aos 35, com setas de tamanhos diferentes. Esquema")]
A = lambda a: 60 + a / 60 * 1540
p.append(f'<rect x="{A(10):.0f}" y="10" width="{A(20) - A(10):.0f}" height="360" fill="{GLIC_T}"/>')
rs = [rot(A(10), 20, "janela de construção", w=A(20) - A(10), tam=24, cor=GLIC, peso=700, alinha="center", lh=1.2)]
curva = "M " + " L ".join(f"{A(a):.0f} {370 - (300 * (1 - math.exp(-((a / 11) ** 2.4))) - max(0, a - 30) * 2.2):.0f}" for a in range(0, 61, 2))
p.append(f'<path d="{curva}" stroke="{TINTA}" stroke-width="6" fill="none"/>')
p.append(f'<line x1="{A(0):.0f}" y1="370" x2="{A(60):.0f}" y2="370" stroke="{GRADE}" stroke-width="3"/>')
for a in (0, 10, 20, 30, 40, 50, 60):
    rs.append(rot(A(a) - 40, 380, f"{a}", w=80, tam=22, cor=MUDO, alinha="center"))
yv = lambda a: 370 - (300 * (1 - math.exp(-((a / 11) ** 2.4))) - max(0, a - 30) * 2.2)
for a, t, d in ((19, "aos 19: deixa de construir", 110), (35, "aos 35: perde a partir do pico", 50)):
    p.append(f'<circle cx="{A(a):.0f}" cy="{yv(a):.0f}" r="14" fill="{FOSF}"/>')
    p.append(f'<line x1="{A(a):.0f}" y1="{yv(a) + 18:.0f}" x2="{A(a):.0f}" y2="{yv(a) + 18 + d:.0f}" stroke="{FOSF}" stroke-width="8"/>')
    rs.append(rot(A(a) + 24, yv(a) + 30, t, w=420, tam=26, cor=FOSF, peso=700))
rs += [rot(A(60) - 200, 410, "idade, anos", w=200, tam=22, cor=MUDO, alinha="right"), rot(A(60) - 200, 20, "esquema", w=200, tam=22, cor=MUDO, alinha="right")]
diagrama(S, "janela", 440, p, rs, eyebrow="Dá para recuperar tudo?", titulo="Dois anos sem menstruar não custam o mesmo aos 19 e aos 35")

# 8. o desfecho
p = [svg_abre(1664, 440, "A linha do tempo completa a partir do mês nove. Mês dezesseis: ciclo volta, irregular. Mês vinte: ciclos de 30 a 35 dias. Mês trinta: coluna lombar menos 1,1, melhor, ainda abaixo do esperado para quem salta. Faixa contínua desde o mês nove: sem nova fratura")]
p.append(f'<line x1="40" y1="160" x2="1624" y2="160" stroke="{TINTA}" stroke-width="4"/>')
rs = []
marcos = [(9, "mês 9", "mudança de rumo", OXID), (16, "mês 16", "ciclo volta, irregular", FOSF), (20, "mês 20", "ciclos de 30 a 35 dias", FOSF), (30, "mês 30", "coluna −1,1", AZUL)]
for m, a, t, c in marcos:
    x = 60 + (m - 9) / 21 * 1500
    p.append(f'<circle cx="{x:.0f}" cy="160" r="16" fill="{c}" stroke="{CARTAO}" stroke-width="4"/>')
    al = "left" if m == 9 else ("right" if m == 30 else "center")
    lx = x - 20 if al == "left" else (x - 320 if al == "right" else x - 170)
    rs += [rot(lx, 40, a, w=340, tam=30, cor=c, peso=700, serif=True, alinha=al), rot(lx, 90, t, w=340, tam=26, cor=TINTA, peso=600, alinha=al)]
rs.append(rot(1224, 200, "melhor, ainda abaixo do esperado para quem salta", w=400, tam=22, cor=AZUL, alinha="right", lh=1.2))
p.append(f'<rect x="60" y="300" width="1564" height="64" rx="32" fill="{OXID}"/>')
rs.append(rot(60, 314, "sem nova fratura desde o mês 9", w=1564, tam=30, cor=PAPEL, peso=700, alinha="center"))
rs.append(rot(60, 392, "meses e valores ilustrativos", w=800, tam=22, cor=MUDO))
diagrama(S, "desfecho", 440, p, rs, eyebrow="O desfecho, sem enfeite", titulo="O ciclo voltou em meses; o osso melhorou, mas não normalizou",
         destaque="As duas fraturas tinham a mesma causa, e só a segunda foi tratada pela causa.", destaque_cor="tinta")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Saúde óssea, disfunção menstrual e fratura por estresse", "titulo": "Trate a fratura e a causa no mesmo dia",
          "regras": ["Fratura por estresse na atleta abre a pergunta pelo ciclo e pela energia no mesmo dia",
                     "Densitometria com a régua da atleta: Z-score, coluna e fêmur; abaixo de −1 com impacto já é baixo",
                     "Energia, carga e comportamento primeiro; estradiol transdérmico só se faltar; nem pílula, nem bisfosfonato"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Ajusta o impacto e não libera sem saber se a causa foi tratada."},
                    {"ic": "t:salad", "t": "Nutrição", "x": "Conduz a energia, que é o tratamento principal."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Faz o funil, lê a densitometria com a régua certa e decide sobre hormônio."}]})

salvar("11-07.json", {"arquivo": "aulas/MOD11/11-07-saude-ossea-disfuncao-menstrual-e-fratura-por-estresse.md",
                      "titulo": "Saúde óssea, disfunção menstrual e fratura por estresse", "subtitulo": "Trinta meses de uma jogadora de vôlei",
                      "nota_capa": "Entra por uma fratura que consolidou e por uma causa que continuou.",
                      "secoes": {"linha": ["O caso.", "capa"], "regua": ["O osso da atleta.", "regua"],
                                 "mesnove": ["A segunda fratura.", "mesnove"], "piramide": ["O tratamento e o desfecho.", "piramide"]},
                      "slides": S})
