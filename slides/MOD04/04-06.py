"""Spec do deck 4.6. Gera 04-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

# 1. o erro
S.append({"id": "erro", "tipo": "frase", "fundo": "tinta", "eyebrow": "O erro desta aula",
          "frase": "Cortar gordura é comer melhor?",
          "apoio": "A gordura foi reabilitada no discurso. No prato, continua sendo o primeiro macronutriente cortado por quem decide se cuidar. E ela tem um piso."})

# 2. as três rotas
S.append({"id": "rotas", "tipo": "cards", "por_linha": 3, "eyebrow": "Três rotas até o piso", "titulo": "Não é um perfil de paciente. É uma cultura",
          "cards": [{"t": "Estética", "x": "meses com ~15% da energia em gordura para “secar”; libido, humor, sono e testosterona caem", "cor": "ambar"},
                    {"t": "Pureza alimentar", "x": "“comida limpa”, sem óleo nem castanha; sem dieta, mas sem densidade; o ciclo fica irregular", "cor": "ambar"},
                    {"t": "Orientação incompleta", "x": "“reduza a gordura”: sai azeite, castanha e ovo; fica o biscoito recheado", "cor": "verm"}],
          "destaque": "Uma das três rotas saiu de dentro de um consultório.", "destaque_cor": "tinta"})

# 3. funções
S.append({"id": "funcoes", "tipo": "lista", "eyebrow": "O que só a gordura faz", "titulo": "Cinco funções que não têm substituto",
          "itens": [{"t": "Ácidos graxos essenciais", "x": "linoleico e alfa-linolênico; não existe carboidrato essencial", "cor": "petr"},
                    {"t": "Vitaminas A, D, E e K", "x": "a salada sem azeite entrega menos", "cor": "petr"},
                    {"t": "Membranas e combustível", "x": "o substrato dominante no esforço leve e longo", "cor": "petr"},
                    {"t": "Colesterol e esteroides", "x": "a relação existe, mas não é uma torneira", "cor": "ambar"},
                    {"t": "Saciedade e adesão", "x": "dieta pobre em gordura é mais difícil de manter", "cor": "tinta"}],
          "gap_itens": 14})

# 4. o piso
p = [svg_abre(1664, 280, "Régua da energia vinda de gordura, de 0 a 50%: abaixo de 20%, zona a evitar; de 20 a 35%, faixa recomendada; acima de 35%, o carboidrato começa a ser espremido")]
fx = lambda v: v / 50 * 1664
faixas = [(0, 20, FOSF_T, FOSF, "abaixo do piso"), (20, 35, OXID_T, OXID, "20 a 35%"), (35, 50, GLIC_T, GLIC, "espreme o carboidrato")]
rs = []
for a, b, f, c, t in faixas:
    p.append(f'<rect x="{fx(a):.0f}" y="40" width="{fx(b)-fx(a):.0f}" height="110" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(fx(a) + 20, 76, t, w=fx(b) - fx(a) - 40, tam=30, cor=c, peso=700, alinha="center"))
for v in [0, 20, 35, 50]:
    rs.append(rot(fx(v) - 60 if v else 0, 166, f"{v}%", w=120, tam=26, cor=TINTA, peso=600, alinha="center" if v else "left"))
p.append("</svg>")
rs.append(rot(0, 222, "gordura: 9 kcal por grama · carboidrato e proteína: 4", w=1664, tam=26, cor=MUDO, alinha="center"))
S.append({"id": "piso", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Posicionamento conjunto de 2016", "titulo": "O piso de vinte por cento",
          "destaque": "Abaixo de 20%: essenciais comprometidos, vitaminas lipossolúveis em queda e a energia difícil de fechar. Rota direta para o déficit.",
          "destaque_cor": "verm", "fonte": "Percentual da energia total · ACSM, Academia de Nutrição e Dietética e Dietistas do Canadá, 2016"})

# 5. Whittaker e Wu
S.append({"id": "hormonio", "tipo": "duas", "eyebrow": "O erro espelhado · Whittaker e Wu, 2021", "titulo": "Gordura como nutriente dos hormônios?",
          "esq": {"t": "O que a meta-análise mostrou", "cor": "petr",
                  "itens": ["206 homens, estudos de intervenção", "baixa gordura: testosterona total e livre mais baixas",
                            "efeito pequeno a moderado; LH e SHBG iguais"]},
          "dir": {"t": "As ressalvas", "cor": "ambar",
                  "itens": ["estudos pequenos e antigos", "fibra, tipo de gordura e calorias mudando junto",
                            "errata publicada depois"]},
          "destaque": "Não se sustenta: mais gordura elevando testosterona acima do normal, gordura saturada “anabólica”, dieta como reposição hormonal.",
          "destaque_cor": "verm", "fonte": "Journal of Steroid Biochemistry and Molecular Biology 2021"})

# 6. a ordem de investigação
p = [svg_abre(1664, 400, "Ordem de investigação do homem ativo com testosterona baixa: disponibilidade energética, sono, carga e recuperação, gordura e o piso, causas clínicas")]
degraus = [("1 · disponibilidade energética", OXID, OXID_T), ("2 · sono", OXID, OXID_T), ("3 · carga e recuperação", OXID, OXID_T),
           ("4 · gordura e o piso de 20%", GLIC, GLIC_T), ("5 · causas clínicas", AZUL, AZUL_T)]
rs = []
for i, (t, c, f) in enumerate(degraus):
    y = 10 + i * 78
    x = i * 110
    p.append(f'<rect x="{x}" y="{y}" width="{1664 - x}" height="64" rx="8" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x + 24, y + 14, t, w=1000, tam=30, cor=TINTA, peso=700))
p.append("</svg>")
rs.append(rot(1100, 24, "resolve a maioria", w=540, tam=26, cor=OXID, peso=700, alinha="right"))
rs.append(rot(1100, 258, "encontra pouco", w=540, tam=26, cor=GLIC, peso=700, alinha="right"))
S.append({"id": "ordem", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Hackney, 2020", "titulo": "Energia total antes de macronutriente",
          "destaque": "Na mulher, ainda mais claro: a função reprodutiva acompanha a disponibilidade energética, não a composição da dieta.",
          "destaque_cor": "petr", "fonte": "Frontiers in Endocrinology 2020 · Loucks e Thuma 2003"})

# 7. densidade
S.append({"id": "densidade", "tipo": "numeros", "eyebrow": "A virada prática", "titulo": "Gordura como ferramenta de densidade",
          "numeros": [{"n": "≈ 120", "x": "kcal numa colher de sopa de azeite", "cor": "petr"},
                      {"n": "≈ 200", "x": "kcal num punhado de castanhas", "cor": "petr"},
                      {"n": "≈ 200", "x": "kcal em duas colheres de pasta de amendoim", "cor": "petr"}],
          "destaque": "Para quem não consegue comer volume, a comida não precisa ser maior. Precisa valer mais. Não é efeito endócrino: é densidade.",
          "destaque_cor": "tinta"})

# 8. a frase
S.append({"id": "frase", "tipo": "duas", "eyebrow": "A correção: número, momento, qualidade e a frase", "titulo": "Orientação incompleta produz o oposto",
          "esq": {"t": "“Reduza a gordura”", "cor": "verm",
                  "itens": ["sai o que parece gorduroso: azeite, castanha, ovo", "fica o que não parece: biscoito, pão doce",
                            "o colesterol quase não muda"]},
          "dir": {"t": "A frase completa", "cor": "petr",
                  "itens": ["reduza a gordura dos industrializados", "mantenha azeite, castanha, ovo e peixe",
                            "não fique abaixo do piso"]},
          "destaque": "Momento: menos gordura perto do treino, não fora do dia. Saturada: o alvo não é zero. Trans industrial: eliminar. Ômega-3: peixe duas vezes por semana antes do suplemento.",
          "destaque_cor": "tinta"})

# 9. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "As três rotas fechadas", "titulo": "Ninguém tinha sido informado do piso",
          "regras": ["Estética: a gordura foi o meio, não o mecanismo; energia, sono e carga primeiro",
                     "Pureza: densidade sem aumentar o prato; rigidez e culpa pedem outra conversa",
                     "Orientação: “você fez exatamente o que foi pedido; a orientação estava incompleta”"],
          "cards": [{"t": "Nutricionista", "x": "Macronutrientes e plano alimentar."},
                    {"t": "Médico", "x": "Testosterona, ciclo, perfil lipídico e medicação."},
                    {"t": "Educador físico e psicólogo", "x": "Carga e volume; restrição com cara de regra moral."}],
          "quem": "A pergunta de todos: você cortou alguma gordura? Qual, e por quê?"})

spec = {"arquivo": "aulas/MOD04/04-06-lipidios-e-o-papel-real-da-gordura.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Lipídios na nutrição esportiva", "subtitulo": "Funções, ingestão mínima e interpretações equivocadas",
        "nota_capa": "Entra pelo erro: cortar gordura é comer melhor.",
        "secoes": {"erro": ["O erro e as três rotas.", "capa"],
                   "piso": ["O que só a gordura faz, e o piso.", "funcoes"],
                   "hormonio": ["O erro espelhado e a correção.", "hormonio"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-06.json"), "w"), ensure_ascii=False, indent=1)
print("04-06.json:", len(S), "slides")
