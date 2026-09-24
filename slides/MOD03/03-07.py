"""Spec do deck 3.7. Gera 03-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def seta(x1, y1, x2, y2, cor, mid, esp=5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mid})"/>'

# 1. o laudo
S.append({"id": "laudo", "tipo": "duas", "eyebrow": "O eixo que mais recebe prescrição desnecessária", "titulo": "A glândula falhou, ou o organismo economizou?",
          "esq": {"t": "Primeiro erro: tratar a economia", "cor": "ambar",
                  "itens": ["T3 baixo, TSH normal, sintomas de hipotireoidismo", "hormônio prescrito, melhora no começo",
                            "a conta aparece depois, em massa magra e osso"]},
          "dir": {"t": "Segundo erro, mais grave: não tratar a doença", "cor": "verm",
                  "itens": ["hipotireoidismo é comum", "mulher acima dos 40, Hashimoto, pós-parto",
                            "depois de radioiodo ou cirurgia"]},
          "destaque": "O objetivo não é desconfiar de tireoide. É ter o discriminador.", "destaque_cor": "tinta"})

# 2. desiodases
p = [svg_abre(1664, 400, "A tireoide entrega sobretudo T4; nos tecidos, as desiodases transformam o T4 em T3 ativo ou em T3 reverso inativo"),
     "<defs>" + seta_marker("d1", OXID) + seta_marker("d2", MUDO) + seta_marker("d3", TINTA) + "</defs>"]
p.append(caixa(0, 130, 360, 140, AZUL, AZUL_T, esp=3))
p.append(seta(370, 200, 590, 200, TINTA, "d3", esp=6))
p.append(caixa(610, 100, 440, 200, GLIC, GLIC_T, esp=3))
p.append(seta(1060, 160, 1250, 90, OXID, "d1", esp=5))
p.append(seta(1060, 240, 1250, 310, MUDO, "d2", esp=5))
p.append(caixa(1270, 40, 394, 110, OXID, OXID_T, esp=3))
p.append(caixa(1270, 260, 394, 110, MUDO, CLARO, esp=3))
p.append("</svg>")
rs = [rot(0, 160, "Tireoide", w=360, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(0, 210, "entrega sobretudo T4", w=360, tam=26, cor=TINTA, alinha="center"),
      rot(370, 150, "T4", w=220, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(610, 130, "Tecidos", w=440, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(610, 180, "desiodases: ligar ou desligar", w=440, tam=26, cor=GLIC, peso=700, alinha="center"),
      rot(1270, 60, "T3 ativo", w=394, tam=30, cor=OXID, peso=700, alinha="center"),
      rot(1270, 100, "cerca de 80% feito aqui", w=394, tam=24, cor=TINTA, alinha="center"),
      rot(1270, 280, "T3 reverso", w=394, tam=30, cor=MUDO, peso=700, alinha="center"),
      rot(1270, 320, "inativo: a via de desligar", w=394, tam=24, cor=TINTA, alinha="center")]
S.append({"id": "desiodases", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo um", "titulo": "A tireoide entrega matéria-prima; o tecido decide",
          "fonte": "Bianco e Kim, Journal of Clinical Investigation 2006"})

# 3. hipófise isolada
p = [svg_abre(1664, 380, "A hipófise tem sua própria desiodase e usa o T3 que fabrica para decidir o TSH; ela não enxerga o T3 do músculo, que pode estar baixo com TSH normal")]
p.append(caixa(0, 40, 700, 300, AZUL, AZUL_T, esp=4))
p.append(f'<line x1="830" y1="20" x2="830" y2="360" stroke="{TINTA}" stroke-width="8"/>')
p.append(caixa(960, 40, 704, 300, FOSF, FOSF_T, esp=4))
p.append("</svg>")
rs = [rot(30, 70, "Hipófise", w=640, tam=34, cor=AZUL, peso=700),
      rot(30, 130, "tem a própria desiodase", w=640, tam=28, cor=TINTA),
      rot(30, 180, "usa o T3 que ela mesma faz para decidir o TSH", w=640, tam=28, cor=TINTA),
      rot(30, 270, "TSH: normal", w=640, tam=34, cor=OXID, peso=700),
      rot(990, 70, "Músculo e outros tecidos", w=640, tam=34, cor=FOSF, peso=700),
      rot(990, 130, "T3 baixo, rodando devagar", w=640, tam=28, cor=TINTA),
      rot(990, 180, "menos calor, menos sinal para mitocôndria", w=640, tam=28, cor=TINTA),
      rot(700, 360, "a hipófise não enxerga o T3 do músculo", w=260, tam=24, cor=TINTA, peso=600, alinha="center")]
S.append({"id": "hipofise", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A peça que explica a aula", "titulo": "TSH normal não prova ação normal no tecido"})

# 4. padrão T3 baixo
S.append({"id": "padrao", "tipo": "cards", "eyebrow": "Passo dois", "titulo": "O padrão de economia: síndrome do T3 baixo",
          "cards": [{"t": "T3", "x": "baixo", "cor": "verm"},
                    {"t": "T3 reverso", "x": "alto", "cor": "ambar"},
                    {"t": "T4 livre", "x": "normal ou no limite de baixo", "cor": "tinta"},
                    {"t": "TSH", "x": "normal ou um pouco reduzido", "cor": "petr"}],
          "destaque": "Déficit de energia, doença aguda, trauma, jejum prolongado: o organismo desliga a via que ativa e liga a que desativa. Não é falha, é a resposta certa.",
          "destaque_cor": "petr"})

# 5. Loucks e Spaulding
vals = [("Jejum total", -53, FOSF), ("800 kcal sem carboidrato", -47, FOSF), ("800 kcal com ≥ 50 g de carboidrato", 0, OXID)]
p = [svg_abre(1664, 330, "Spaulding 1976: T3 caiu 53% no jejum total e 47% com 800 kcal sem carboidrato; com 800 kcal e pelo menos 50 g de carboidrato não mudou")]
X0 = 760
p.append(f'<line x1="{X0}" y1="20" x2="{X0}" y2="330" stroke="{MUDO}" stroke-width="2"/>')
rs = []
for i, (nome, v, cor) in enumerate(vals):
    y = 40 + i * 100
    w = abs(v) * 10
    if v:
        p.append(f'<rect x="{X0 - w}" y="{y}" width="{w}" height="64" rx="4" fill="{cor}"/>')
    else:
        p.append(f'<rect x="{X0 - 3}" y="{y}" width="6" height="64" rx="2" fill="{cor}"/>')
    rs.append(rot(X0 + 24, y + 14, nome, w=860, tam=28, cor=TINTA, peso=600))
    rs.append(rot(X0 - (w if v else 0) - 190, y + 10, f"−{abs(v)}%".replace("−0%", "sem mudança") if v else "", w=170, tam=34, cor=TINTA, peso=700, alinha="right", serif=True))
rs.append(rot(X0 - 330, 250, "sem mudança", w=300, tam=30, cor=OXID, peso=700, alinha="right"))
p.append("</svg>")
S.append({"id": "carboidrato", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O limiar e o carboidrato", "titulo": "O T3 muda de regime quando a conta cruza uma linha",
          "destaque": "Loucks e Heath: o T3 caiu de forma abrupta abaixo de um nível de disponibilidade de energia, não aos poucos. Estudos pequenos e antigos, mas consistentes.",
          "destaque_cor": "ambar", "fonte": "Variação do T3 em pessoas com obesidade · Spaulding e colaboradores, JCEM 1976 · Loucks e Heath, American Journal of Physiology 1994"})

# 6. discriminador
S.append({"id": "discriminador", "tipo": "frase", "fundo": "petr", "eyebrow": "Passo três: o discriminador",
          "frase": "TSH alto acusa a glândula. T3 baixo com TSH normal acusa a conta.",
          "apoio": "No hipotireoidismo primário a glândula não entrega e a hipófise grita mais alto. Na economia, o ajuste acontece na ponta, e o TSH não sobe."})

# 7. o que pedir
S.append({"id": "pedir", "tipo": "duas", "eyebrow": "Na ordem certa", "titulo": "O que pedir, e o que não pedir para rastrear",
          "esq": {"t": "Pedir", "cor": "petr",
                  "itens": ["TSH e T4 livre: baratos, bastam para a triagem", "anti-TPO se houver suspeita de autoimunidade",
                            "subclínico: decisão médica caso a caso"]},
          "dir": {"t": "Não pedir para rastrear", "cor": "verm",
                  "itens": ["T3: normal no hipotireoidismo inicial, baixo na economia", "T3 reverso: sobe em quase tudo, sem corte que mude conduta"]},
          "destaque": "Tratamento: levotiroxina é o padrão, sem vantagem consistente das combinações com T3. T3 manipulado para economia soma dois erros.",
          "destaque_cor": "ambar", "fonte": "Jonklaas e colaboradores, American Thyroid Association 2014"})

# 8. caso ilustrativo
p = [svg_abre(1664, 380, "Caso ilustrativo: corredora de 31 anos com T3 baixo, TSH 1,8 e T4 livre no limite; seis meses de T3 manipulado depois, TSH suprimido, palpitação, sono pior, dois quilos a menos quase todos de massa magra e o mesmo cansaço"),
     "<defs>" + seta_marker("c1", MUDO) + "</defs>"]
p.append(caixa(0, 20, 620, 330, AZUL, AZUL_T, esp=3))
p.append(seta(640, 185, 1020, 185, MUDO, "c1", esp=5))
p.append(caixa(1044, 20, 620, 330, FOSF, FOSF_T, esp=3))
p.append("</svg>")
rs = [rot(30, 40, "Início", w=560, tam=32, cor=AZUL, peso=700),
      rot(30, 96, "31 anos, 60 km por semana<br>cansaço, frio, intestino lento<br>T3 baixo · TSH 1,8 · T4 livre no limite", w=560, tam=26, cor=TINTA, lh=1.5),
      rot(30, 260, "história alimentar: não colhida", w=560, tam=26, cor=FOSF, peso=700),
      rot(640, 120, "T3 manipulado, 6 meses", w=380, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(1074, 40, "Seis meses depois", w=560, tam=32, cor=FOSF, peso=700),
      rot(1074, 96, "TSH suprimido, palpitação<br>sono pior<br>2 kg a menos, quase todos de massa magra", w=560, tam=26, cor=TINTA, lh=1.5),
      rot(1074, 260, "o cansaço original: igual", w=560, tam=26, cor=FOSF, peso=700)]
S.append({"id": "caso", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Caso ilustrativo", "titulo": "O TSH de 1,8 era a resposta desde o primeiro dia",
          "destaque": "Os sintomas eram reais e iguais aos do hipotireoidismo, porque o mecanismo final é o mesmo. O que separa é o padrão lido em ordem, mais a história alimentar.",
          "destaque_cor": "tinta"})

# 9. procedimento
S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "O procedimento", "titulo": "Cinco passos, com a história antes do exame", "gap_itens": 20,
          "itens": [{"t": "A história", "x": "quanto come, quanto treina, se cortou carboidrato, quanto peso perdeu", "cor": "petr"},
                    {"t": "TSH e T4 livre", "x": "anti-TPO se houver suspeita de autoimunidade", "cor": "tinta"},
                    {"t": "O discriminador", "x": "TSH alto: glândula · T3 baixo com TSH normal: conta", "cor": "tinta"},
                    {"t": "Economia: restaurar energia", "x": "nutricionista, carga revista, exame repetido depois", "cor": "ambar"},
                    {"t": "Glândula: conduta médica", "x": "levotiroxina; subclínico caso a caso", "cor": "verm"}]})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Ceticismo não; ordem", "titulo": "Não deixe de investigar tireoide",
          "regras": ["Mulher acima dos 40 com fadiga e ganho de peso merece TSH",
                     "E o TSH alto merece ser levado a sério"],
          "cards": [{"t": "Médico", "x": "Pede, interpreta e trata."},
                    {"t": "Quem acompanha toda semana", "x": "Sabe do déficit, do carboidrato cortado, do volume que subiu, e há quanto tempo."}],
          "quem": "Com essa informação escrita no encaminhamento, o caminho mais fácil passa a ser o certo."})

spec = {"arquivo": "aulas/MOD03/03-07-tireoide-e-exercicio.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Função tireoidiana no praticante de exercício", "subtitulo": "Interpretação laboratorial",
        "nota_capa": "Entra direto no laudo.",
        "secoes": {"eixo": ["Os dois erros e onde a decisão acontece.", "capa"],
                   "economia": ["O padrão de economia, o limiar e o carboidrato.", "padrao"],
                   "exames": ["O discriminador e o que pedir.", "discriminador"],
                   "roteiro": ["O caso ilustrativo e o procedimento.", "caso"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-07.json"), "w"), ensure_ascii=False, indent=1)
print("03-07.json:", len(S), "slides")
