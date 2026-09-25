"""Spec do deck 4.8. Gera 04-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o número
S.append({"id": "numero", "tipo": "frase", "fundo": "tinta", "eyebrow": "Sawka e colaboradores, 2007",
          "frase": "Não perder mais de 2%. E não ganhar.",
          "apoio": "Perfil típico de posto médico: primeira maratona, acima de cinco horas, bebe em todos os postos, chega confusa e mais pesada do que largou. Fez o que mandaram. A segunda metade da regra teria protegido."})

# 2. a faixa e a conta
p = [svg_abre(1664, 300, "Régua do peso ao fim da sessão em relação ao início: acima de zero, bebeu mais do que perdeu; de zero a menos dois por cento, faixa-alvo; abaixo de menos dois, prejuízo começa")]
fx = lambda v: (v + 4) / 5 * 1664
faixas = [(-4, -2, GLIC_T, GLIC, "perda acima de 2%"), (-2, 0, OXID_T, OXID, "faixa-alvo"), (0, 1, FOSF_T, FOSF, "ganhou peso")]
rs = []
for a, b, f, c, t in faixas:
    p.append(f'<rect x="{fx(a):.0f}" y="30" width="{fx(b)-fx(a):.0f}" height="100" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(fx(a) + 10, 62, t, w=fx(b) - fx(a) - 20, tam=30, cor=c, peso=700, alinha="center"))
for v, t in [(-2, "−2%"), (0, "0")]:
    rs.append(rot(fx(v) - 60, 142, t, w=120, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
rs.append(rot(0, 210, "70 kg → 68,9 kg em 90 min · bebeu 0,6 L · suor 1,7 L · taxa ≈ 1,13 L/h · perda 1,6%", w=1664, tam=30, cor=TINTA, peso=700, alinha="center"))
S.append({"id": "faixa", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A faixa e a conta", "titulo": "Terminar entre zero e dois por cento abaixo",
          "destaque": "Taxa de suor = (peso antes − peso depois) + o que bebeu − a urina, dividido pelo tempo. Cada quilo perdido é, aproximadamente, um litro.",
          "destaque_cor": "petr"})

# 3. a variação e a conta da corredora
S.append({"id": "variacao", "tipo": "numeros", "eyebrow": "Baker, 2017", "titulo": "Um fator de quatro entre pessoas",
          "numeros": [{"n": "0,5 a 2", "x": "litros de suor por hora, na faixa relatada em atletas", "cor": "petr"},
                      {"n": "≈ 3,4 L", "x": "perdidos em 5 h 40 a 0,6 L/h", "cor": "ambar"},
                      {"n": "≈ 4,5 L", "x": "bebidos a 0,8 L/h: um quilo a mais na chegada", "cor": "verm"}],
          "destaque": "Conta ilustrativa, não dado medido. Sua pouco, corre devagar, passa muito tempo na prova: a regra de quem sua muito vira excesso.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2017"})

# 4. três regras
S.append({"id": "regras", "tipo": "lista", "eyebrow": "Três regras de uso", "titulo": "O número vale para uma condição",
          "itens": [{"t": "A taxa vale para aquela condição", "x": "verão e inverno dão números diferentes; medir no longão, no jogo, na prova", "cor": "petr"},
                    {"t": "Não é para repor cem por cento durante", "x": "o alvo é limitar a perda, não zerar; a sede guia", "cor": "ambar"},
                    {"t": "Até uma hora, clima ameno: a sede resolve", "x": "a conta é para sessão longa, calor, sintoma ou problema prévio", "cor": "tinta"}],
          "gap_itens": 26})

# 5. antes
p = [svg_abre(1664, 240, "Linha do tempo antes da sessão: quatro horas antes, cinco a sete mililitros por quilo; duas horas antes, se urina escura ou ausente, mais três a cinco mililitros por quilo; início da sessão"),
     "<defs>" + seta_marker("h1", MUDO) + "</defs>",
     f'<line x1="40" y1="120" x2="1600" y2="120" stroke="{MUDO}" stroke-width="4" marker-end="url(#h1)"/>']
rs = []
for x, t, d, c in [(120, "4 h antes", "5 a 7 mL/kg", OXID), (760, "2 h antes, se precisar", "+ 3 a 5 mL/kg", GLIC), (1400, "início", "", TINTA)]:
    p.append(f'<circle cx="{x+100}" cy="120" r="16" fill="{c}"/>')
    rs.append(rot(x - 100, 40, t, w=400, tam=30, cor=c, peso=700, alinha="center"))
    if d:
        rs.append(rot(x - 100, 160, d, w=400, tam=34, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "antes", "tipo": "diagrama", "h": 240, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Antes · posicionamento de 2007", "titulo": "Começar hidratado, com tempo de urinar",
          "destaque": "Para 70 kg: 350 a 500 mL quatro horas antes. Cor da urina: clara está bom, escura falta; muda com complexo B e volume recente. Sinal, não medida.",
          "destaque_cor": "petr", "fonte": "Medicine and Science in Sports and Exercise 2007"})

# 6. depois
S.append({"id": "depois", "tipo": "duas", "eyebrow": "Depois · Shirreffs e colaboradores, 1996", "titulo": "Volume maior que a perda, com sódio",
          "esq": {"t": "A regra prática", "cor": "petr",
                  "itens": ["1,25 a 1,5 L por quilo perdido, nas horas seguintes", "sódio da bebida ou da comida",
                            "perdeu 1,1 kg e joga à noite: 1,4 a 1,7 L até lá"]},
          "dir": {"t": "Quando importa", "cor": "ambar",
                  "itens": ["outra sessão no mesmo dia ou cedo no dia seguinte", "perda grande",
                            "uma sessão por dia e jantar normal: a comida e a sede resolvem"]},
          "destaque": "Volume sem sódio escoa pela urina. Sódio sem volume não basta. O balanço fecha na interação dos dois.",
          "destaque_cor": "tinta", "fonte": "Medicine and Science in Sports and Exercise 1996"})

# 7. índice de hidratação
S.append({"id": "bebidas", "tipo": "duas", "eyebrow": "Maughan e colaboradores, 2016", "titulo": "Treze bebidas contra a água",
          "esq": {"t": "Retiveram mais que a água", "cor": "petr",
                  "itens": ["leite integral", "leite desnatado", "solução de reidratação oral"]},
          "dir": {"t": "Iguais à água, no volume testado", "cor": "tinta",
                  "itens": ["café, chá quente e gelado", "refrigerante comum e sem açúcar, água com gás", "isotônico, suco de laranja, cerveja comum"]},
          "destaque": "O café de todo dia não desidrata. O leite é uma bebida de recuperação subestimada. A cerveja: o problema não é a água, é o sono e a recuperação.",
          "destaque_cor": "ambar", "fonte": "Um litro de cada, em pessoas hidratadas · American Journal of Clinical Nutrition 2016"})

# 8. sódio
S.append({"id": "sodio", "tipo": "cards", "por_linha": 3, "eyebrow": "Sódio · Baker, 2017", "titulo": "De 10 a 90 mmol/L no suor",
          "cards": [{"t": "Quem precisa durante", "x": "acima de duas horas, calor e umidade, suador salgado, duas sessões no dia", "cor": "petr"},
                    {"t": "O rótulo", "x": "na bebida, cerca de 20 a 50 mmol/L: 0,5 a pouco mais de 1 g de sódio por litro", "cor": "ambar"},
                    {"t": "Água de coco", "x": "potássio alto, sódio baixo e variável: não repõe o suador salgado", "cor": "verm"}],
          "destaque": "Sal em cápsula não protege de quem bebe demais. A hiponatremia do exercício é, quase sempre, excesso de água (Hew-Butler e colaboradores, 2015).",
          "destaque_cor": "tinta", "fonte": "Faixa do sódio na bebida: posicionamento de 2007"})

# 9. cãibra
p = [svg_abre(1664, 320, "Dois grupos de triatletas de Ironman, 43 com cãibra e 166 sem; sódio no sangue e desidratação iguais entre os grupos; ritmo mais rápido e história de cãibra previram a cãibra")]
rs = []
for i, (n, t, c, f) in enumerate([("43", "com cãibra", FOSF, FOSF_T), ("166", "sem cãibra", AZUL, AZUL_T)]):
    x = 0 if i == 0 else 1304
    p.append(caixa(x, 60, 360, 200, c, f, esp=3))
    rs.append(rot(x, 90, n, w=360, tam=64, cor=c, peso=700, alinha="center"))
    rs.append(rot(x, 190, t, w=360, tam=28, cor=TINTA, peso=600, alinha="center"))
for j, (t, c, riscado) in enumerate([("sódio no sangue: igual", MUDO, True), ("desidratação: igual", MUDO, True),
                                     ("ritmo mais rápido que o habitual", OXID, False), ("história de cãibra", OXID, False)]):
    y = 40 + j * 64
    p.append(f'<rect x="440" y="{y}" width="784" height="52" rx="8" fill="{CLARO if riscado else OXID_T}" stroke="{c}" stroke-width="2"/>')
    rs.append(rot(460, y + 10, t, w=744, tam=28, cor=c, peso=700, alinha="center"))
    if riscado:
        p.append(f'<line x1="560" y1="{y+26}" x2="1104" y2="{y+26}" stroke="{FOSF}" stroke-width="3"/>')
p.append("</svg>")
S.append({"id": "caibra", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Schwellnus, Drew e Collins, 2011", "titulo": "Cãibra não é número de hidratação",
          "destaque": "Perfil típico de quadra: futsal amador, jogo inteiro sem substituição, mais jogos que treinos, cãibra desde a adolescência. A conduta sai do copo e vai para a quadra.",
          "destaque_cor": "petr", "fonte": "210 triatletas de Ironman · British Journal of Sports Medicine 2011"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Os números da aula", "titulo": "Uma balança substitui qualquer tabela",
          "regras": ["Menos de 2% de perda, nenhum ganho; taxa de suor medida na condição que importa",
                     "5 a 7 mL/kg quatro horas antes; 1,25 a 1,5 L por kg perdido, com sódio, quando há pressa",
                     "Sódio só para quem precisa; cãibra pede condicionamento antes de sal"],
          "cards": [{"t": "Nutricionista", "x": "Plano de líquidos e de sódio."},
                    {"t": "Preparador e educador físico", "x": "A pesagem no treino; o condicionamento na cãibra."},
                    {"t": "Médico", "x": "Hiponatremia, doença do calor, atleta confuso."}],
          "quem": "Na dúvida, não se empurra líquido em quem pode estar com sódio baixo."})

spec = {"arquivo": "aulas/MOD04/04-08-hidratacao-e-reposicao-hidroeletrolitica.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Hidratação no exercício", "subtitulo": "Taxa de sudorese, reposição de sódio e prevenção da hiponatremia",
        "nota_capa": "Entra pelo número e pela metade que ninguém repete.",
        "secoes": {"numero": ["O número e a conta.", "capa"],
                   "antes": ["Antes, depois e o que se bebe.", "antes"],
                   "sodio": ["Sódio e cãibra.", "sodio"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-08.json"), "w"), ensure_ascii=False, indent=1)
print("04-08.json:", len(S), "slides")
