"""Spec do deck 11.5. Gera 11-05.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a ficha de três caixas
p = [svg_abre(1664, 460, "Uma ficha de avaliação com três caixas de seleção, transtorno alimentar, amenorreia e osteoporose, nenhuma marcada. Ao lado de amenorreia, escrito à mão: ciclos de 45 a 60 dias. Embaixo, um carimbo: não fecha tríade. À direita, uma pista de corrida e o volume que quase dobrou em um ano")]
p.append(caixa(0, 0, 820, 460, TINTA, CARTAO, esp=2, rx=16))
rs = [rot(30, 24, "Ficha de avaliação", w=760, tam=30, cor=TINTA, peso=700, serif=True)]
for j, t in enumerate(["transtorno alimentar", "amenorreia", "osteoporose"]):
    y = 100 + j * 80
    p.append(f'<rect x="40" y="{y}" width="46" height="46" rx="8" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(110, y + 6, t, w=330, tam=30, cor=TINTA, peso=600))
rs.append(rot(420, 188, "ciclos de 45 a 60 dias", w=380, tam=28, cor=GLIC, peso=700, serif=True))
p.append(f'<path d="M 410 210 Q 380 205 370 200" stroke="{GLIC}" stroke-width="3" fill="none"/>')
p.append(f'<rect x="200" y="350" width="420" height="80" rx="10" fill="none" stroke="{FOSF}" stroke-width="5"/>')
rs.append(rot(200, 368, "não fecha tríade", w=420, tam=36, cor=FOSF, peso=700, alinha="center", serif=True))
for k in range(4):
    p.append(f'<rect x="{900 + k * 34}" y="{40 + k * 34}" width="{700 - k * 68}" height="{300 - k * 68}" rx="{150 - k * 34}" fill="none" stroke="{GLIC if k == 0 else BORDA}" stroke-width="{8 if k == 0 else 4}"/>')
p.append(icone("t:run", 1180, 150, 90, GLIC))
rs += [rot(880, 370, "volume semanal quase dobrou em um ano", w=760, tam=28, cor=TINTA, peso=600, alinha="center"),
       rot(880, 414, "primeira maratona", w=760, tam=24, cor=MUDO, alinha="center")]
diagrama(S, "caixas", 460, p, rs, eyebrow="Uma corredora de rua, na casa dos trinta", titulo="Esperar as três caixas marcadas deixa a maioria de fora")

# 2. a linha do tempo
p = [svg_abre(1664, 470, "Linha do tempo de 1992 a 2023. 1992: três doenças. 1997: primeiro posicionamento do colégio americano. 2007: três espectros, energia como motor. 2014: consenso da coalizão da tríade e REDs do Comitê Olímpico. 2021: tríade masculina. 2023: REDs revisado. Embaixo, uma faixa que vai de diagnóstico tardio a reconhecimento precoce"), defs(TINTA)]
X = lambda a: 70 + (a - 1992) / 31 * 1520
p.append(f'<line x1="40" y1="200" x2="1624" y2="200" stroke="{TINTA}" stroke-width="4"/>')
rs = []
marcos = [(1992, "1992", "três doenças", FOSF, True, "left"), (1997, "1997", "primeiro posicionamento", FOSF, False, "left"),
          (2007, "2007", "três espectros; energia como motor", OXID, True, "center"), (2014, "2014", "coalizão da tríade e REDs do Comitê Olímpico", AZUL, False, "center"),
          (2021, "2021", "tríade masculina", OXID, True, "right"), (2023, "2023", "REDs revisado", AZUL, False, "right")]
for a, ano, t, c, cima, al in marcos:
    x = X(a)
    p.append(f'<circle cx="{x:.0f}" cy="200" r="16" fill="{c}" stroke="{CARTAO}" stroke-width="4"/>')
    lx = x - 20 if al == "left" else (x - 170 if al == "center" else x - 300)
    if cima:
        rs += [rot(lx, 30, ano, w=340 if al != "right" else 320, tam=34, cor=c, peso=700, serif=True, alinha=al),
               rot(lx, 80, t, w=340 if al != "right" else 320, tam=24, cor=TINTA, alinha=al, lh=1.25)]
    else:
        rs += [rot(lx, 232, ano, w=340 if al != "right" else 320, tam=34, cor=c, peso=700, serif=True, alinha=al),
               rot(lx, 282, t, w=340 if al != "right" else 320, tam=24, cor=TINTA, alinha=al, lh=1.25)]
p.append('<defs><linearGradient id="gt" x1="0" x2="1"><stop offset="0" stop-color="#A8322A"/><stop offset="1" stop-color="#008A7E"/></linearGradient></defs>')
p.append('<rect x="40" y="390" width="1584" height="64" rx="32" fill="url(#gt)"/>')
rs += [rot(70, 404, "diagnóstico tardio", w=600, tam=28, cor=PAPEL, peso=700),
       rot(994, 404, "reconhecimento precoce", w=600, tam=28, cor=PAPEL, peso=700, alinha="right")]
diagrama(S, "linha", 470, p, rs, eyebrow="Trinta anos de revisões", titulo="Cada revisão empurrou o diagnóstico para mais cedo")

# 3. as três réguas
p = [svg_abre(1664, 490, "Três réguas empilhadas. Energia: da baixa disponibilidade, com ou sem transtorno alimentar, à disponibilidade ótima. Ciclo: da amenorreia hipotalâmica funcional, passando por disfunção subclínica e oligomenorreia, à eumenorreia. Osso: da osteoporose, passando pela densidade baixa, à saúde óssea ótima. Uma seta sai do cursor da energia e empurra os outros dois. Esquema"), defs(TINTA)]
p.append('<defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="#A8322A"/><stop offset="0.5" stop-color="#B07A1C"/><stop offset="1" stop-color="#008A7E"/></linearGradient></defs>')
rs = []
reguas = [("Energia", "baixa, com ou sem transtorno alimentar", "", "ótima", 0.38),
          ("Ciclo", "amenorreia hipotalâmica", "subclínica · oligomenorreia", "eumenorreia", 0.5),
          ("Osso", "osteoporose", "densidade baixa", "saúde óssea ótima", 0.72)]
for j, (t, esq, meio, dir_, pos) in enumerate(reguas):
    y = 30 + j * 160
    rs.append(rot(0, y + 2, t, w=200, tam=36, cor=TINTA, peso=700, serif=True))
    p.append(f'<rect x="280" y="{y}" width="1380" height="40" rx="20" fill="url(#gr)"/>')
    cx = 280 + pos * 1380
    p.append(f'<path d="M {cx:.0f} {y - 4} l -18 -28 l 36 0 z" fill="{TINTA}"/>')
    rs += [rot(280, y + 52, esq, w=520, tam=24, cor=FOSF, peso=700),
           rot(1260, y + 52, dir_, w=400, tam=24, cor=OXID, peso=700, alinha="right")]
    if meio:
        rs.append(rot(770, y + 52, meio, w=420, tam=24, cor=GLIC, peso=700, alinha="center"))
p.append(seta(230, 76, 230, 178, TINTA, "m0", 5))
p.append(seta(230, 236, 230, 338, TINTA, "m0", 5).replace("/>", f'{TRACO}/>'))
rs.append(rot(0, 452, "esquema", w=260, tam=22, cor=MUDO))
diagrama(S, "espectros", 490, p, rs, eyebrow="O modelo de 2007", titulo="Cada componente é uma régua; a energia empurra as outras")

# 4. a prevalência
p = [svg_abre(1664, 420, "Três barras de faixa sobre um eixo de 0 a 60 por cento. Um componente: de 16 a 60 por cento. Dois componentes: de 2,7 a 27 por cento. Os três: de 0 a 15,9 por cento")]
X = lambda v: 400 + v / 60 * 1200
rs = []
for v in (0, 20, 40, 60):
    p.append(f'<line x1="{X(v):.0f}" y1="10" x2="{X(v):.0f}" y2="330" stroke="{GRADE}" stroke-width="2"/>')
    rs.append(rot(X(v) - 60, 344, f"{v}%", w=120, tam=24, cor=MUDO, alinha="center"))
barras = [("Um componente", 16, 60, "16 a 60%", OXID), ("Dois componentes", 2.7, 27, "2,7 a 27%", GLIC), ("Os três", 0, 15.9, "0 a 15,9%", FOSF)]
for j, (t, a, b, txt, c) in enumerate(barras):
    y = 30 + j * 104
    rs.append(rot(0, y + 10, t, w=370, tam=30, cor=TINTA, peso=700, alinha="right"))
    p.append(f'<rect x="{X(a):.0f}" y="{y}" width="{X(b) - X(a):.0f}" height="60" rx="12" fill="{c}"/>')
    if b < 40:
        rs.append(rot(X(b) + 16, y + 12, txt, w=300, tam=30, cor=c, peso=700, serif=True))
    else:
        rs.append(rot(X(a) + 20, y + 12, txt, w=400, tam=30, cor=PAPEL, peso=700, serif=True))
rs.append(rot(400, 384, "faixas largas: populações, esportes e cortes diferentes", w=1200, tam=22, cor=MUDO, alinha="center"))
diagrama(S, "prevalencia", 420, p, rs, eyebrow="Revisão sistemática de 2013, 65 estudos", titulo="A tríade completa é a forma rara; um componente só é a comum",
         fonte="Med Sci Sports Exerc 2013")

# 5. a regra: um vértice aceso
p = [svg_abre(1664, 470, "Um triângulo com três vértices: energia, ciclo e osso. O vértice do ciclo aceso; dele saem setas pontilhadas para os outros dois, com pontos de interrogação. À direita, quatro círculos menores apagados: ferro, imunidade, humor, desempenho, o resto do corpo"), defs(FOSF)]
V = {"energia": (450, 80), "ciclo": (160, 380), "osso": (740, 380)}
p.append(f'<path d="M 450 80 L 160 380 L 740 380 Z" fill="none" stroke="{BORDA}" stroke-width="4"/>')
rs = []
for k, (x, y) in V.items():
    aceso = k == "ciclo"
    p.append(f'<circle cx="{x}" cy="{y}" r="72" fill="{FOSF if aceso else CARTAO}" stroke="{FOSF if aceso else MUDO}" stroke-width="4"{"" if aceso else TRACO}/>')
    rs.append(rot(x - 90, y - 18, k, w=180, tam=30, cor=PAPEL if aceso else TINTA, peso=700, alinha="center"))
p.append(seta(210, 312, 380, 140, FOSF, "m0", 5).replace("/>", f'{TRACO}/>'))
p.append(seta(240, 380, 650, 380, FOSF, "m0", 5).replace("/>", f'{TRACO}/>'))
rs += [rot(200, 200, "?", w=60, tam=44, cor=FOSF, peso=700), rot(420, 400, "?", w=60, tam=44, cor=FOSF, peso=700)]
p.append(caixa(940, 20, 724, 430, MUDO, PAPEL, esp=2, rx=18))
rs.append(rot(964, 40, "O resto do corpo", w=680, tam=30, cor=TINTA, peso=700, serif=True))
for j, t in enumerate(["ferro", "imunidade", "humor", "desempenho"]):
    x, y = 1010 + (j % 2) * 330, 130 + (j // 2) * 150
    p.append(f'<circle cx="{x + 50}" cy="{y + 50}" r="50" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
    rs.append(rot(x + 112, y + 34, t, w=200, tam=28, cor=TINTA, peso=600))
rs.append(rot(964, 404, "pesam mais sob contracepção hormonal", w=680, tam=22, cor=MUDO))
diagrama(S, "regra", 470, p, rs, eyebrow="O que entra no lugar da ficha", titulo="Um componente aceso obriga a procurar os outros dois",
         destaque="A regra já estava no posicionamento de 2007: quem chega com um componente é avaliada para os outros.", destaque_cor="tinta")

# 6. a disputa de 2014
p = [svg_abre(1664, 470, "Duas colunas de 2014. Comitê Olímpico: muitos sistemas, homens incluídos, o nome tríade deixa gente de fora. Coalizão da tríade: o modelo de 2007 já punha a energia como motor, elos novos sem evidência causal, nome novo confunde. Embaixo, a faixa de acordo: a energia que falta é o motor")]
rs = []
for k, (t, itens, c, f) in enumerate([("Comitê Olímpico, 2014", ["muitos sistemas, não três", "homens também", "o nome tríade deixa gente de fora"], AZUL, AZUL_T),
                                      ("Coalizão da tríade, 2014", ["2007 já punha a energia como motor", "elos novos sem evidência causal", "nome novo confunde quem atende"], GLIC, GLIC_T)]):
    x = k * 864
    p.append(caixa(x, 0, 800, 330, c, f, esp=3, rx=18))
    rs.append(rot(x + 28, 22, t, w=740, tam=32, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 40, 104 + j * 70, "· " + it, w=740, tam=27, cor=TINTA, peso=600))
p.append(caixa(0, 370, 1664, 100, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(20, 396, "Onde concordam: a energia que falta é o motor", w=1624, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True))
diagrama(S, "disputa", 470, p, rs, eyebrow="A troca de nome não foi pacífica", titulo="A briga de 2014 era sobre o mapa e o nome, não sobre a causa")

# 7. as estradas convergem
p = [svg_abre(1664, 470, "Duas estradas que saem de pontos diferentes em 2014 e se encontram. Na estrada da tríade, a placa de 2021: tríade masculina. Na estrada do REDs, a placa de 2023: muitos sistemas, gravidade em faixas. No encontro, uma placa única: energia no centro, homens incluídos, reconhecer cedo")]
for y0, c in ((70, GLIC), (400, AZUL)):
    d = f"M 0 {y0} C 500 {y0} 760 235 1200 235"
    p.append(f'<path d="{d}" stroke="{c}" stroke-opacity="0.25" stroke-width="54" fill="none"/>')
    p.append(f'<path d="{d}" stroke="{c}" stroke-width="4" fill="none"{TRACO}/>')
rs = [rot(10, 6, "tríade, 2014", w=300, tam=24, cor=GLIC, peso=700), rot(10, 440, "REDs, 2014", w=300, tam=24, cor=AZUL, peso=700)]
p.append(caixa(380, 110, 420, 96, GLIC, GLIC_T, esp=3, rx=12))
rs += [rot(396, 118, "2021 · tríade masculina", w=390, tam=24, cor=GLIC, peso=700), rot(396, 156, "energia, hipogonadismo, osso", w=390, tam=22, cor=TINTA)]
p.append(caixa(380, 268, 420, 96, AZUL, AZUL_T, esp=3, rx=12))
rs += [rot(396, 276, "2023 · REDs revisado", w=390, tam=24, cor=AZUL, peso=700), rot(396, 314, "muitos sistemas, gravidade em faixas", w=390, tam=22, cor=TINTA)]
p.append(caixa(1200, 80, 464, 310, TINTA, CARTAO, esp=4, rx=18))
for j, t in enumerate(["energia no centro", "homens incluídos", "reconhecer cedo"]):
    p.append(icone("t:flame" if j == 0 else ("t:users" if j == 1 else "t:zoom-question"), 1224, 110 + j * 92, 44, OXID))
    rs.append(rot(1284, 112 + j * 92, t, w=360, tam=28, cor=TINTA, peso=700))
diagrama(S, "convergencia", 470, p, rs, eyebrow="O que veio depois", titulo="As duas estradas convergiram, e a conduta é a mesma nas duas",
         destaque="Use o nome que quem vai ler o relatório entende. O motor não muda.", destaque_cor="tinta")

# 8. o funil de exclusão
p = [svg_abre(1664, 500, "Um funil com cinco filtros, cada um com o exame ao lado. Gravidez, beta-hCG. Prolactina alta, prolactina. Tireoide, TSH e T4 livre. Ovário que falhou, FSH alto. Excesso de andrógeno e ovário policístico, clínica, testosterona e hormônio antimülleriano. No fundo, o que sobra: amenorreia hipotalâmica funcional, com LH e estradiol baixos e FSH sem subir")]
filtros = [("gravidez", "beta-hCG, sempre primeiro"), ("prolactina alta", "prolactina"), ("tireoide", "TSH e T4 livre"),
           ("ovário que falhou", "FSH alto"), ("andrógeno · ovário policístico", "clínica, testosterona, antimülleriano")]
rs = []
for j, (t, ex) in enumerate(filtros):
    y = j * 70
    w = 860 - j * 90
    x = 460 - w / 2
    p.append(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="58" rx="10" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    rs.append(rot(x, y + 12, t, w=w, tam=26, cor=AZUL, peso=700, alinha="center"))
    p.append(f'<line x1="{x + w + 10:.0f}" y1="{y + 29}" x2="930" y2="{y + 29}" stroke="{BORDA}" stroke-width="2"/>')
    rs.append(rot(950, y + 12, ex, w=714, tam=26, cor=TINTA, peso=600))
p.append(caixa(150, 370, 620, 130, FOSF, FOSF_T, esp=4, rx=16))
rs += [rot(160, 384, "amenorreia hipotalâmica funcional", w=600, tam=28, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(160, 436, "LH e estradiol baixos · FSH sem subir", w=600, tam=24, cor=TINTA, alinha="center")]
p.append(caixa(950, 390, 714, 90, GLIC, GLIC_T, esp=3, rx=14))
p.append(icone("t:alert-triangle", 970, 410, 48, GLIC))
rs.append(rot(1036, 416, "duas causas podem coexistir", w=610, tam=28, cor=GLIC, peso=700))
diagrama(S, "exclusao", 500, p, rs, eyebrow="O que só o médico faz", titulo="A amenorreia só vira energética depois de excluir o resto",
         fonte="Diretriz da sociedade de endocrinologia, J Clin Endocrinol Metab 2017")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "REDs: da tríade ao modelo multissistêmico", "titulo": "Quem espera as três caixas chega depois",
          "regras": ["Um componente aceso: procure os outros dois e o resto do corpo",
                     "Amenorreia é diagnóstico de exclusão: gravidez, prolactina, tireoide e ovário primeiro",
                     "Tríade ou REDs, o motor é a energia: devolver energia, não apagar o sinal"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Reconhece o vértice aceso e encaminha."},
                    {"ic": "t:salad", "t": "Nutrição", "x": "Avalia a energia e conduz a correção, a intervenção principal."},
                    {"ic": "h:doctor", "t": "Medicina e ginecologia", "x": "Fazem o funil de exclusão, pedem densitometria e decidem a liberação."}]})

salvar("11-05.json", {"arquivo": "aulas/MOD11/11-05-reds-da-triade-ao-modelo-multissistemico.md",
                      "titulo": "REDs: da tríade ao modelo multissistêmico", "subtitulo": "Por que a ficha de três caixas está errada",
                      "nota_capa": "Entra por uma corredora de rua cujos ciclos espaçaram no ano da primeira maratona.",
                      "secoes": {"caixas": ["O erro.", "capa"], "linha": ["De onde ele vem.", "linha"],
                                 "disputa": ["Os dois vocabulários.", "disputa"], "exclusao": ["O funil.", "exclusao"]},
                      "slides": S})
