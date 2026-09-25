"""Spec do deck 5.7. Gera 05-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a regra
S.append({"id": "regra", "tipo": "frase", "fundo": "tinta", "eyebrow": "Suplementos de uso clínico",
          "frase": "Corrigir deficiência melhora. Turbinar suficiência, não.",
          "apoio": "Os ergogênicos acrescentam algo sobre uma base normal. Ferro, vitamina D e ômega-3 funcionam quando há falta. Sem saber se falta, não existe decisão possível."})

# 2. a curva
p = [svg_abre(1664, 360, "Esquema de uma curva de benefício pela quantidade: sobe na falta, vira platô na suficiência e desce abaixo de zero no excesso")]
p.append(f'<rect x="60" y="20" width="500" height="320" fill="{OXID_T}" opacity="0.6"/>')
p.append(f'<rect x="1120" y="20" width="484" height="320" fill="{FOSF_T}" opacity="0.6"/>')
p.append(f'<line x1="60" y1="240" x2="1604" y2="240" stroke="{MUDO}" stroke-width="2" stroke-dasharray="10 8"/>')
p.append(f'<path d="M60,236 C300,228 400,80 620,80 L1100,80 C1300,80 1420,200 1600,330" fill="none" stroke="{TINTA}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(60, 30, "falta: corrigir ajuda", w=500, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(620, 30, "suficiência: platô", w=480, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(1120, 30, "excesso: dano", w=484, tam=28, cor=FOSF, peso=700, alinha="center"),
      rot(620, 110, "mais produto, nenhum benefício a mais", w=480, tam=24, cor=MUDO, alinha="center"),
      rot(70, 256, "sem efeito", w=200, tam=22, cor=MUDO),
      rot(1180, 280, "ferro e vitamina D", w=260, tam=22, cor=FOSF, peso=600)]
S.append({"id": "curva", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A forma da curva", "titulo": "Onde a pessoa está?",
          "destaque": "A pergunta não é “isso é bom?”. É “onde essa pessoa está na curva?”. Para ferro e vitamina D, só um exame responde.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# 3. perfis
S.append({"id": "perfis", "tipo": "cards", "por_linha": 3, "eyebrow": "Três perfis típicos", "titulo": "Uma precisa, um se arrisca, um não move nada",
          "cards": [{"t": "A corredora", "x": "cansada há três meses; ferritina 18, hemoglobina normal", "cor": "petr"},
                    {"t": "O homem da megadose", "x": "50 mil unidades de vitamina D por semana, há oito meses; nunca dosou cálcio", "cor": "verm"},
                    {"t": "O jogador", "x": "uma cápsula de ômega-3 por dia “para inflamação”", "cor": "ambar"}],
          "destaque_cor": "tinta"})

# 4. três perguntas
S.append({"id": "perguntas", "tipo": "lista", "eyebrow": "A decisão", "titulo": "Três perguntas, para qualquer suplemento de uso clínico",
          "itens": [{"t": "Existe falta, demonstrada?", "x": "ferro e vitamina D: exame com indicação · ômega-3: ingestão habitual de peixe", "cor": "petr"},
                    {"t": "Existe risco no excesso?", "x": "ferro: sério · vitamina D: em dose alta sem controle · ômega-3: menor; anticoagulante", "cor": "verm"},
                    {"t": "Existe dose, prazo e reavaliação?", "x": "repor sem data de reavaliação cria uso permanente por inércia", "cor": "ambar"}],
          "gap_itens": 24})

# 5. ferro: quem e o número
S.append({"id": "ferro", "tipo": "numeros", "eyebrow": "Sim e colaboradores, 2019", "titulo": "Ferro: quem testar e o que o número diz",
          "numeros": [{"n": "< 35 µg/L", "x": "ferritina do primeiro estágio de deficiência em atletas, com hemoglobina ainda normal", "cor": "petr"},
                      {"n": "3 a 6 h", "x": "pico da hepcidina depois do exercício: a absorção intestinal se fecha", "cor": "ambar"},
                      {"n": "↑", "x": "ferritina sobe na inflamação: pode estar falsamente confortável", "cor": "verm"}],
          "destaque": "Grupo de risco somado a sintoma abre exame. Nenhum dos dois, sozinho, costuma abrir.",
          "destaque_cor": "tinta", "fonte": "European Journal of Applied Physiology 2019"})

# 6. Stoffel
S.append({"id": "stoffel", "tipo": "numeros", "eyebrow": "Stoffel e colaboradores, 2017", "titulo": "Ferro: dias alternados, dose única",
          "numeros": [{"n": "16,3%", "x": "absorção fracionada acumulada em dias consecutivos", "cor": "tinta"},
                      {"n": "21,8%", "x": "em dias alternados; ferro total de 131 para 175 mg", "cor": "petr"},
                      {"n": "= ", "x": "dividir a dose do dia: sem ganho de absorção, mais hepcidina", "cor": "verm"}],
          "destaque": "Dose única, pela manhã, em dias alternados, longe da sessão intensa. Vitamina C junto; café, chá, leite e cálcio longe.",
          "destaque_cor": "petr", "fonte": "Mulheres com estoque baixo, dois ensaios · Lancet Haematology 2017"})

# 7. por que não repor sem diagnóstico
S.append({"id": "pista", "tipo": "duas", "eyebrow": "Ferro só com diagnóstico", "titulo": "Por que não repor às cegas",
          "esq": {"t": "Ferro em excesso", "cor": "verm",
                  "itens": ["acumula; sem via eficiente de excreção", "hemocromatose hereditária não é raríssima", "polivitamínico com ferro também conta"]},
          "dir": {"t": "Repor apaga a pista", "cor": "ambar",
                  "itens": ["ferritina baixa é achado, não diagnóstico", "fluxo menstrual, dieta, doença celíaca", "perda digestiva: obrigatório investigar"]},
          "destaque": "Diagnóstico, prescrição e reavaliação são do médico. Reconhecer risco e sintoma e encaminhar cedo é de todos.",
          "destaque_cor": "tinta"})

# 8. vitamina D
S.append({"id": "vitd", "tipo": "duas", "eyebrow": "Vitamina D: só a decisão", "titulo": "Corrigir não é otimizar",
          "esq": {"t": "Corrigir", "cor": "petr",
                  "itens": ["testar quem tem motivo: pouco sol, treino coberto, pele escura", "idade, obesidade, má absorção, fratura por estresse", "em deficiente, repor melhora desfecho ósseo", "com refeição que tenha gordura"]},
          "dir": {"t": "Otimizar", "cor": "verm",
                  "itens": ["em suficiente, sem ganho de desempenho demonstrado", "alvo alto “para performance”: qual desfecho previu?", "megadose sem controle: hipercalcemia", "não dá sintoma cedo"]},
          "destaque": "Na megadose, a conduta é avaliação médica com cálcio e vitamina D, e a suspensão decidida com o resultado na mão.",
          "destaque_cor": "verm"})

# 9. ômega-3: a conta da cápsula
p = [svg_abre(1664, 300, "Barras comparando a dose de muitos ensaios em esporte, dois a três gramas de EPA mais DHA por dia, com os cerca de trezentos miligramas de uma cápsula comum")]
esc = 1180 / 3000
p.append(f'<rect x="420" y="40" width="{2000*esc:.0f}" height="80" rx="6" fill="{OXID}"/>')
p.append(f'<rect x="{420+2000*esc:.0f}" y="40" width="{1000*esc:.0f}" height="80" rx="6" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append(f'<rect x="420" y="180" width="{300*esc:.0f}" height="80" rx="6" fill="{FOSF}"/>')
p.append("</svg>")
rs = [rot(0, 58, "muitos ensaios em esporte", w=400, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(0, 198, "1 cápsula de 1.000 mg de óleo", w=400, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(440, 62, "2 a 3 g de EPA + DHA por dia", w=760, tam=28, cor="#FFFFFF", peso=700),
      rot(420 + 300 * esc + 20, 202, "≈ 300 mg de EPA + DHA: seis ou sete cápsulas para chegar a 2 g", w=1100, tam=26, cor=FOSF, peso=700)]
S.append({"id": "omega", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Ômega-3: a decisão é pela ingestão", "titulo": "Leia a linha de EPA e DHA, não o peso da cápsula",
          "destaque": "Quase nunca come peixe? Há espaço. Efeito claro em marcador de inflamação e dano; inconsistente no desempenho. Incorporação leva semanas.",
          "destaque_cor": "petr", "fonte": "A cápsula é exemplo de rótulo comum, não número de estudo"})

# 10. Paulsen
S.append({"id": "paulsen", "tipo": "numeros", "eyebrow": "Paulsen e colaboradores, 2014", "titulo": "Apagar o sinal que adapta",
          "numeros": [{"n": "54", "x": "jovens, duplo-cego, 11 semanas de treino aeróbio, sobretudo corrida", "cor": "tinta"},
                      {"n": "1.000 mg", "x": "de vitamina C, com 235 mg de vitamina E, por dia: doses de prateleira", "cor": "ambar"},
                      {"n": "↓", "x": "aumento das proteínas mitocondriais embotado no grupo suplementado", "cor": "verm"}],
          "destaque": "Achado de vitamina C e E, não do ômega-3. Mas a postura vale: onde a inflamação faz parte do sinal, “reduzir inflamação” não é automaticamente bom.",
          "destaque_cor": "tinta", "fonte": "Journal of Physiology 2014"})

# 11. aplicado
S.append({"id": "aplicado", "tipo": "tabela", "eyebrow": "As três perguntas, aplicadas", "titulo": "Três posições na curva",
          "cab": ["Perfil", "Falta?", "Risco?", "Conduta"],
          "larguras": [18, 16, 18, 48],
          "linhas": [["Corredora", "provável", "repor às cegas", "médico investiga o porquê; dose única matinal, dias alternados; reavaliação"],
                     ["Megadose de D", "não é a questão", "hipercalcemia", "médico, cálcio e vitamina D; suspensão orientada"],
                     ["Jogador", "talvez", "baixo", "peixe duas vezes por semana; se usar, a dose dos estudos"]],
          "destaque": "A dor depois do jogo tem candidatos melhores: volume de jogo acima do treinado, sono e recuperação.",
          "destaque_cor": "ambar"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Nos ergogênicos: vale a pena? Aqui: falta?", "titulo": "Você toma alguma vitamina ou suplemento por conta própria?",
          "regras": ["Corrigir deficiência melhora; turbinar suficiência, não",
                     "Ferro e vitamina D: exame antes do produto, e reavaliação marcada",
                     "Ômega-3: ingestão habitual primeiro; dose lida no rótulo"],
          "cards": [{"t": "Médico", "x": "Exame, diagnóstico, prescrição, causa, suspensão."},
                    {"t": "Nutricionista", "x": "Comida que previne e sustenta a correção."},
                    {"t": "Educador físico e preparador", "x": "Veem o sinal primeiro; levam o dado adiante."}],
          "quem": "A pergunta de primeira consulta é de todas as profissões."})

spec = {"arquivo": "aulas/MOD05/05-07-ferro-vitamina-d-e-omega-3-no-praticante.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Ferro, vitamina D e ômega-3", "subtitulo": "Suplementos de uso clínico, diagnóstico antes do produto",
        "nota_capa": "Entra pela forma da curva.",
        "secoes": {"regra": ["A regra, a curva e as três perguntas.", "capa"],
                   "ferro": ["Ferro: quem testar, como repor, por que não às cegas.", "ferro"],
                   "vitd": ["Vitamina D, ômega-3 e o alerta dos antioxidantes.", "vitd"],
                   "aplicado": ["As três perguntas aplicadas.", "aplicado"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-07.json"), "w"), ensure_ascii=False, indent=1)
print("05-07.json:", len(S), "slides")
