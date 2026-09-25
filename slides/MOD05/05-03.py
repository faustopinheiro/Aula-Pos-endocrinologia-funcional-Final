"""Spec do deck 5.3. Gera 05-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a pergunta
S.append({"id": "pergunta", "tipo": "frase", "fundo": "tinta", "eyebrow": "Três perfis típicos",
          "frase": "Funciona. Então a pergunta é outra.",
          "apoio": "Quem treina às nove da noite e só sobrou a cafeína do pote. A jogadora de vôlei com jogo às nove e meia. O ciclista hipertenso com quatro cafés, pré-treino e gel, que nunca somou nada. Quanto, quando, para quem, e trocando o quê."})

# 2. evidência e mecanismo
S.append({"id": "mecanismo", "tipo": "duas", "eyebrow": "Grgic e colaboradores, 2020 · Guest e colaboradores, 2021", "titulo": "Ela não cria energia",
          "esq": {"t": "O que a evidência sustenta", "cor": "petr",
                  "itens": ["21 meta-análises reunidas", "resistência aeróbica e muscular", "força e potência", "efeito pequeno: decide pódio, some no amador"]},
          "dir": {"t": "O mecanismo certo", "cor": "ambar",
                  "itens": ["bloqueia o receptor de adenosina", "a adenosina sinaliza cansaço", "não queima gordura de forma relevante", "adia a percepção de que a energia acaba"]},
          "destaque": "O que o amador sente não é velocidade: é que o treino pareceu mais fácil. E a conta do cansaço continua existindo.",
          "destaque_cor": "tinta", "fonte": "British Journal of Sports Medicine 2020 · Journal of the International Society of Sports Nutrition 2021"})

# 3. dose
p = [svg_abre(1664, 280, "Régua de dose de cafeína em mg por kg: de 1 a 3, começar aqui; de 3 a 6, a faixa dos estudos; 9 ou mais, mais efeito adverso sem mais efeito")]
fx = lambda v: v / 10 * 1664
faixas = [(0.5, 3, OXID_T, OXID, "começar aqui"), (3, 6, AZUL_T, AZUL, "a faixa dos estudos"), (6, 9, CLARO, MUDO, ""), (9, 10, FOSF_T, FOSF, "")]
rs = []
for a, b, f, c, t in faixas:
    p.append(f'<rect x="{fx(a):.0f}" y="40" width="{fx(b)-fx(a):.0f}" height="100" fill="{f}" stroke="{c}" stroke-width="3"/>')
    if t:
        rs.append(rot(fx(a) + 10, 76, t, w=fx(b) - fx(a) - 20, tam=28, cor=c, peso=700, alinha="center"))
for v in [1, 3, 6, 9]:
    rs.append(rot(fx(v) - 60, 150, f"{v}", w=120, tam=28, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
rs += [rot(fx(9) - 720, 196, "9 mg/kg: muito efeito adverso, sem necessidade", w=720, tam=26, cor=FOSF, peso=700, alinha="right"),
       rot(0, 196, "mg/kg, cerca de 60 min antes", w=600, tam=26, cor=MUDO)]
S.append({"id": "dose", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A dose · posicionamento de 2021", "titulo": "Mais não é melhor",
          "destaque": "Para 70 kg, 3 a 6 mg/kg são 210 a 420 mg. A dose mínima eficaz pode ser tão baixa quanto 2 mg/kg. E a cafeína aumenta a ansiedade de quem já chega nervoso.",
          "destaque_cor": "petr", "fonte": "Journal of the International Society of Sports Nutrition 2021"})

# 4. fonte e soma
S.append({"id": "fonte", "tipo": "tabela", "eyebrow": "A fonte, e a soma", "titulo": "A dose só existe se a fonte for previsível",
          "cab": ["Fonte", "Dose previsível?", "Observação"],
          "larguras": [28, 18, 54],
          "linhas": [["Cápsula de cafeína anidra", "sim", "é o que os estudos usam"],
                     ["Gel e bebida esportiva", "sim, no rótulo", "práticos durante o esforço"],
                     ["Goma de mascar", "sim", "absorção mais rápida"],
                     ["Café coado", "não", "varia com pó, grão, moagem e tempo"],
                     ["Energético", "em parte", "vem com açúcar e outros componentes"]],
          "destaque": "Quatro cafés, um pré-treino e um gel não são três decisões. São uma dose só. Somar em voz alta é o primeiro trabalho da consulta.",
          "destaque_cor": "ambar"})

# 5. Drake
S.append({"id": "sono", "tipo": "numeros", "eyebrow": "Drake e colaboradores, 2013", "titulo": "O custo está na meia-vida",
          "numeros": [{"n": "400 mg", "x": "de cafeína, em três horários", "cor": "tinta"},
                      {"n": "6 h", "x": "antes de deitar, o horário mais distante testado", "cor": "ambar"},
                      {"n": "> 1 h", "x": "a menos de sono total medido, mesmo assim", "cor": "verm"}],
          "destaque": "Meia-vida em torno de 5 horas, com faixa larga: mais longa com anticoncepcional oral e na gestação, mais curta em fumantes.",
          "destaque_cor": "petr", "fonte": "Journal of Clinical Sleep Medicine 2013"})

# 6. de trás para a frente
p = [svg_abre(1664, 260, "Linha do tempo da noite: cafeína às 20h30, jogo às 21h30, deitar à 0h30; a faixa de seis horas antes de deitar cobre tudo"),
     "<defs>" + seta_marker("n1", MUDO) + "</defs>"]
fx = lambda h: 80 + (h - 17) / 8.5 * 1500
p.append(f'<rect x="{fx(18.5):.0f}" y="60" width="{fx(24.5)-fx(18.5):.0f}" height="80" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
p.append(f'<line x1="{fx(17):.0f}" y1="100" x2="{fx(25.4):.0f}" y2="100" stroke="{MUDO}" stroke-width="4" marker-end="url(#n1)"/>')
rs = [rot(fx(18.5) + 10, 66, "6 horas antes de deitar", w=500, tam=26, cor=FOSF, peso=700)]
for h, t, c, yy in [(20.5, "cafeína 20h30", GLIC, 150), (21.5, "jogo 21h30", AZUL, 196), (24.5, "deitar 0h30", TINTA, 150)]:
    p.append(f'<circle cx="{fx(h):.0f}" cy="100" r="16" fill="{c}"/>')
    rs.append(rot(fx(h) - 150, yy, t, w=300, tam=28, cor=c, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "tras", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A jogadora de vôlei", "titulo": "Contar a partir da hora de dormir",
          "destaque": "Três saídas: usar com dose baixa, ciente do custo; não usar e proteger o sono; usar só nos jogos que importam. Para o amador, a terceira quase sempre ganha.",
          "destaque_cor": "tinta"})

# 7. genética
S.append({"id": "genetica", "tipo": "numeros", "eyebrow": "Guest e colaboradores, 2018 · 101 atletas, 10 km de bicicleta", "titulo": "Genética: achado real, sem teste de balcão",
          "numeros": [{"n": "−4,8%", "x": "tempo no genótipo AA, com 2 mg/kg", "cor": "petr"},
                      {"n": "−6,8%", "x": "tempo no genótipo AA, com 4 mg/kg", "cor": "petr"},
                      {"n": "+13,7%", "x": "tempo no genótipo CC, com 4 mg/kg", "cor": "verm"}],
          "destaque": "Outros estudos não replicaram de forma consistente. E a conduta seria a mesma: testar a dose em treino. O teste barato já existe, e se chama treino.",
          "destaque_cor": "tinta", "fonte": "Medicine and Science in Sports and Exercise 2018"})

# 8. hábito e intolerância
S.append({"id": "habito", "tipo": "duas", "eyebrow": "Gonçalves, Gualano e colaboradores, 2017", "titulo": "Hábito não apaga o efeito",
          "esq": {"t": "40 ciclistas, três tercis de consumo", "cor": "petr",
                  "itens": ["≈ 60, 140 e 350 mg por dia", "todos com 6 mg/kg antes do contrarrelógio", "mesmo ganho nos três grupos", "a semana de abstinência não se justifica"]},
          "dir": {"t": "Quem passa mal", "cor": "verm",
                  "itens": ["ansiedade, tremor, palpitação", "náusea, urgência intestinal", "dor de cabeça, insônia", "para essa pessoa: não usar"]},
          "destaque": "A cafeína do dia de prova é sempre a dose testada em treino.",
          "destaque_cor": "ambar", "fonte": "Journal of Applied Physiology 2017"})

# 9. limites
S.append({"id": "limites", "tipo": "cards", "por_linha": 3, "eyebrow": "Onde a decisão deixa de ser de desempenho", "titulo": "Os limites",
          "cards": [{"t": "Pó a granel", "x": "dose em miligramas, venda em gramas; mortes documentadas por erro de colher", "cor": "verm"},
                    {"t": "Gestação", "x": "teto em torno de 200 mg/dia; meia-vida maior; decisão médica", "cor": "ambar"},
                    {"t": "Crianças e adolescentes", "x": "sem indicação ergogênica; energético desaconselhado", "cor": "ambar"},
                    {"t": "Coração", "x": "hipertensão não controlada, arritmia, palpitação, doença conhecida", "cor": "verm"},
                    {"t": "Soma de estimulantes", "x": "pré-treino, café, energético, termogênico: a dose que ninguém pretendeu", "cor": "verm"},
                    {"t": "Antidoping", "x": "não é proibida; está em monitoramento; há regras de federação", "cor": "tinta"}]})

# 10. três perfis
S.append({"id": "decisoes", "tipo": "tabela", "eyebrow": "As três decisões", "titulo": "O que decide cada perfil",
          "cab": ["Perfil", "O que decide", "Decisão"],
          "larguras": [24, 30, 46],
          "linhas": [["Treina às 21h", "o sono é a causa da falta de disposição", "não usar como pré-treino; jantar, horário e sono"],
                     ["Vôlei às 21h30", "jogo decisivo ou de calendário", "dose baixa só no decisivo, ciente da noite pior"],
                     ["Ciclista hipertenso", "a soma do dia", "somar em voz alta; cortar o pré-treino; pressão com o médico"]],
          "destaque": "A cafeína não é o problema principal do ciclista, mas é a parte que ele controla e que ninguém tinha contado.",
          "destaque_cor": "petr"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "A decisão, em cinco linhas", "titulo": "Quanta cafeína, somando tudo?",
          "regras": ["3 a 6 mg/kg, 60 min antes; doses menores funcionam e custam menos",
                     "Fonte previsível, não xícara; some o dia inteiro",
                     "Conte a partir da hora de dormir; teste em treino; não é para todo mundo"],
          "cards": [{"t": "Nutricionista", "x": "Dose e momento."},
                    {"t": "Médico", "x": "Pressão, arritmia, gestação, ansiedade, interação."},
                    {"t": "Educador físico e preparador", "x": "Veem o efeito e o efeito adverso no treino."}],
          "quem": "A pergunta que quase ninguém faz é de todos."})

spec = {"arquivo": "aulas/MOD05/05-03-cafeina-dose-momento-genetica-e-efeito-real.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Cafeína no exercício", "subtitulo": "Dose, momento de uso e variabilidade individual",
        "nota_capa": "Entra pela decisão, não pela eficácia.",
        "secoes": {"pergunta": ["Os perfis, a evidência e a dose.", "capa"],
                   "sono": ["O momento e o sono.", "sono"],
                   "genetica": ["Variação individual, limites e decisões.", "genetica"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-03.json"), "w"), ensure_ascii=False, indent=1)
print("05-03.json:", len(S), "slides")
