"""Spec do deck 4.7. Gera 04-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. dois pedidos
S.append({"id": "pedidos", "tipo": "duas", "eyebrow": "Dois pedidos típicos", "titulo": "Um painel sem risco, um risco sem painel",
          "esq": {"t": "O adulto do painel", "cor": "ambar",
                  "itens": ["quer dosar trinta micronutrientes", "multivitamínico por conta própria", "come bem, não exclui nada"]},
          "dir": {"t": "A adolescente cansada", "cor": "verm",
                  "itens": ["nada dois períodos por dia, em crescimento", "não come carne vermelha", "evita leite “porque incha”"]},
          "destaque": "Thomas, Erdman e Burke, 2016: o risco está em quem restringe energia, perde peso de forma agressiva ou exclui grupos de alimentos.",
          "destaque_cor": "petr", "fonte": "Medicine and Science in Sports and Exercise 2016"})

# 2. o procedimento
p = [svg_abre(1664, 220, "Procedimento em quatro passos: quem é, o que come, o que sente, para onde vai"),
     "<defs>" + seta_marker("q1", MUDO) + "</defs>"]
passos = ["quem é", "o que come", "o que sente", "para onde vai"]
rs = []
for i, t in enumerate(passos):
    x = i * 420
    p.append(caixa(x, 40, 360, 140, OXID, OXID_T, esp=3))
    rs.append(rot(x, 64, f"{i+1}", w=360, tam=36, cor=OXID, peso=700, alinha="center"))
    rs.append(rot(x, 116, t, w=360, tam=32, cor=TINTA, peso=700, alinha="center"))
    if i < 3:
        p.append(f'<line x1="{x+366}" y1="110" x2="{x+410}" y2="110" stroke="{MUDO}" stroke-width="4" marker-end="url(#q1)"/>')
p.append("</svg>")
S.append({"id": "passos", "tipo": "diagrama", "h": 220, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O procedimento", "titulo": "Não começa pelo exame",
          "destaque": "Fronteiras: vitamina D e osso tiveram aula própria; anemia e ferro, com diagnóstico e tratamento, ficam para o módulo de medicina esportiva clínica. Aqui: quem está em risco, e o que a comida resolve.",
          "destaque_cor": "tinta"})

# 3. matriz
S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Passo um · quem é", "titulo": "Onde as deficiências se concentram",
          "cab": ["Grupo", "Ferro", "Cálcio", "Vit. D", "B12", "Iodo"],
          "larguras": [40, 12, 12, 12, 12, 12],
          "linhas": [["Mulher que menstrua", "●", "", "", "", ""],
                     ["Adolescente em crescimento", "●", "●", "", "", ""],
                     ["Atleta de resistência", "●", "", "", "", ""],
                     ["Restrição de energia ou corte", "●", "●", "●", "", ""],
                     ["Exclusão de grupos (vegano)", "●", "●", "●", "●", "●"],
                     ["Doador de sangue frequente", "●", "", "", "", ""]],
          "destaque": "A adolescente cruza quase todas as linhas. O adulto do painel não cruza nenhuma.",
          "destaque_cor": "petr", "fonte": "Pontos de atenção principais por grupo, conforme a aula"})

# 4. hepcidina
t = [i / 4 for i in range(0, 49)]
svg, rs = linhas(1664, 320, "Hepcidina subindo depois de uma sessão intensa, com pico por volta de três a seis horas, período em que a absorção de ferro diminui",
                 [{"nome": "", "cor": FOSF, "pts": [(h, 20 + 80 * math.exp(-((h - 4.5) / 2.6) ** 2)) for h in t]}],
                 0, 12, 0, 110, [(0, "fim da sessão"), (3, "3 h"), (6, "6 h"), (12, "12 h")], [], margem=(40, 20, 60, 30),
                 extra=lambda fx, fy: f'<rect x="{fx(3):.0f}" y="{fy(110):.0f}" width="{fx(6)-fx(3):.0f}" height="{fy(0)-fy(110):.0f}" fill="{FOSF_T}"/>')
rs += [rot(780, 40, "hepcidina", w=300, tam=30, cor=FOSF, peso=700),
       rot(1000, 110, "absorção de ferro menor enquanto ela está alta", w=620, tam=26, cor=TINTA, peso=600)]
S.append({"id": "hepcidina", "tipo": "diagrama", "h": 320, "svg": svg, "rotulos": rs,
          "eyebrow": "Sim e colaboradores, 2019", "titulo": "Por que o exercício pesa no ferro",
          "destaque": "Dois treinos duros por dia: muitas horas com a porta de absorção meio fechada. A refeição mais rica em ferro rende mais longe desse pico.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · European Journal of Applied Physiology 2019"})

# 5. vegano e iodo
S.append({"id": "vegano", "tipo": "cards", "por_linha": 3, "eyebrow": "Rogerson, 2017", "titulo": "O vegano muda a lista",
          "cards": [{"t": "B12", "x": "não há fonte vegetal confiável: suplementar é parte da dieta", "cor": "verm"},
                    {"t": "Pontos de atenção", "x": "ferro, zinco, cálcio, iodo, vitamina D e ômega-3 de cadeia longa", "cor": "ambar"},
                    {"t": "A nota brasileira do iodo", "x": "o sal comum é iodado; alguns sais “gourmet” não; leia o rótulo", "cor": "tinta"}],
          "destaque": "Uma dieta vegana bem planejada atende a maior parte dos atletas, com manejo de alimentos e suplementação adequada.",
          "destaque_cor": "petr", "fonte": "Journal of the International Society of Sports Nutrition 2017"})

# 6. passo dois
S.append({"id": "come", "tipo": "lista", "eyebrow": "Passo dois · o que come", "titulo": "Quatro perguntas sobre o padrão",
          "itens": [{"t": "Come energia suficiente?", "x": "se não, esse é o problema principal", "cor": "verm"},
                    {"t": "O que foi excluído, e por quê?", "x": "ética é uma coisa; medo é outra conversa", "cor": "ambar"},
                    {"t": "De onde vem o ferro?", "x": "heme ou não heme, e o que vem junto", "cor": "petr"},
                    {"t": "De onde vem o cálcio?", "x": "e qual é a rota de quem cortou laticínio", "cor": "petr"}],
          "gap_itens": 22})

# 7. ferro e cálcio no prato
S.append({"id": "prato", "tipo": "duas", "eyebrow": "Onde a comida mais resolve", "titulo": "Ferro e cálcio no prato",
          "esq": {"t": "Ferro", "cor": "verm",
                  "itens": ["heme (carnes): bem absorvido", "não heme (feijão, folhas, fortificados): bem menos",
                            "vitamina C junto aumenta", "café, chá e cálcio junto reduzem: afastar uma hora"]},
          "dir": {"t": "Cálcio", "cor": "petr",
                  "itens": ["cerca de 1.000 mg/dia no adulto; mais no adolescente", "copo de leite ou iogurte: perto de 300 mg",
                            "sem laticínio: bebida fortificada, tofu, sardinha, folhas"]},
          "destaque": "Multivitamínico comum: não corrige ferro, não repõe vitamina D baixa, tem pouco cálcio. Resposta genérica para uma pergunta específica.",
          "destaque_cor": "ambar"})

# 8. passo três
S.append({"id": "sente", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo três · o que sente", "titulo": "O sintoma não aponta o nutriente",
          "cards": [{"t": "Ferro", "x": "fluxo intenso, falta de ar desproporcional, palidez, vontade de mastigar gelo", "cor": "verm"},
                    {"t": "B12", "x": "formigamento, memória e humor, em vegano sem suplemento ou com remédios que reduzem a absorção", "cor": "ambar"},
                    {"t": "Cálcio e vitamina D", "x": "fratura por estresse repetida; e antes: falta energia?", "cor": "tinta"}],
          "destaque": "Cansaço, queda de desempenho e infecções são os mesmos de sono ruim, treino excessivo e déficit. O passo três decide a urgência, não o diagnóstico.",
          "destaque_cor": "petr"})

# 9. o que não entra
S.append({"id": "turbina", "tipo": "frase", "fundo": "tinta", "eyebrow": "O que o procedimento não inclui",
          "frase": "Deficiência se corrige. Suficiência não se turbina.",
          "apoio": "Exame de cabelo, teste “intracelular” em pacote, painel sem pergunta clínica, soro de vitaminas na veia sem deficiência. Magnésio e zinco se perdem no suor, mas deficiência clínica em quem come bem é incomum."})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Passo quatro · para onde vai", "titulo": "Quem é, o que come, o que sente, para onde vai",
          "regras": ["Risco pelo padrão, sem sinal: ajustar a comida",
                     "Risco com sinal, ou sinal forte: avaliação médica; ferro por conta própria, nunca",
                     "A adolescente vai pelas duas saídas; o adulto do painel, por uma conversa"],
          "cards": [{"t": "Nutricionista", "x": "Alimentação e fontes."},
                    {"t": "Médico", "x": "Exame, diagnóstico e reposição."},
                    {"t": "Educador e preparador físico", "x": "A queda de rendimento, vista primeiro."}],
          "quem": "Exclusão com medo ou culpa: o psicólogo entra com o médico."})

spec = {"arquivo": "aulas/MOD04/04-07-micronutrientes-e-deficiencias-prevalentes.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Micronutrientes no praticante de exercício", "subtitulo": "Grupos de risco e avaliação dirigida",
        "nota_capa": "Entra pelos dois pedidos: o painel e a adolescente.",
        "secoes": {"quem": ["Os dois pedidos e quem está em risco.", "capa"],
                   "come": ["O que come: ferro e cálcio no prato.", "come"],
                   "sente": ["O que sente e para onde vai.", "sente"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-07.json"), "w"), ensure_ascii=False, indent=1)
print("04-07.json:", len(S), "slides")
