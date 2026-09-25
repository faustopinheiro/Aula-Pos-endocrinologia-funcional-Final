"""Spec do deck 4.5. Gera 04-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

# 1. três números
S.append({"id": "tres", "tipo": "numeros", "eyebrow": "Três números que todo mundo mistura", "titulo": "Gramas por quilo por dia",
          "numeros": [{"n": "0,8", "x": "piso populacional contra deficiência, não meta para quem treina", "cor": "tinta"},
                      {"n": "1,6", "x": "platô do ganho de massa livre de gordura com treino de força", "cor": "petr"},
                      {"n": "2,2", "x": "limite superior do intervalo desse platô", "cor": "ambar"}],
          "destaque": "“A recomendação oficial é 0,8, o resto é exagero”: o número certo para a pergunta errada.",
          "destaque_cor": "tinta"})

# 2. o platô
xs = [i / 10 for i in range(4, 31)]
svg, rs = linhas(1664, 340, "Ganho de massa livre de gordura subindo com a proteína diária e achatando perto de 1,6 g/kg, com a faixa até 2,2 como incerteza",
                 [{"nome": "", "cor": OXID, "pts": [(x, 100 * (1 - math.exp(-(x - 0.4) / 0.45))) for x in xs]}],
                 0.4, 3.0, 0, 105, [(0.8, "0,8"), (1.6, "1,6"), (2.2, "2,2"), (3.0, "3,0 g/kg/dia")], [], margem=(40, 20, 60, 30),
                 destaques=[{"x": 1.6}],
                 extra=lambda fx, fy: f'<rect x="{fx(1.6):.0f}" y="{fy(105):.0f}" width="{fx(2.2)-fx(1.6):.0f}" height="{fy(0)-fy(105):.0f}" fill="{GLIC_T}"/>')
rs += [rot(1050, 60, "platô", w=300, tam=30, cor=OXID, peso=700),
       rot(120, 220, "ganho de massa livre de gordura", w=500, tam=26, cor=OXID, peso=600)]
S.append({"id": "plato", "tipo": "diagrama", "h": 340, "svg": svg, "rotulos": rs,
          "eyebrow": "Morton e colaboradores, 2018", "titulo": "Onde mais proteína para de ajudar",
          "destaque": "49 estudos, 1.863 pessoas treinando força: +0,30 kg de massa livre de gordura. Efeito maior em treinados, menor com a idade. Em déficit, a necessidade sobe.",
          "destaque_cor": "petr", "fonte": "Esquema da curva, sem valores medidos, com os pontos do estudo · British Journal of Sports Medicine 2018 · Jäger 2017: 1,4 a 2,0 g/kg"})

# 3. Areta
p = [svg_abre(1664, 330, "Mesmos 80 g de whey em 12 horas, divididos em 8 doses de 10 g, 4 de 20 g ou 2 de 40 g; o padrão de 4 doses de 20 g teve a maior síntese miofibrilar")]
padroes = [("8 × 10 g", 8, 10, MUDO), ("4 × 20 g", 4, 20, OXID), ("2 × 40 g", 2, 40, MUDO)]
x0, W = 280, 1340
rs = []
for i, (n, k, g, c) in enumerate(padroes):
    y = 50 + i * 100
    p.append(f'<line x1="{x0}" y1="{y}" x2="{x0+W}" y2="{y}" stroke="{GRADE}" stroke-width="3"/>')
    for j in range(k):
        cx = x0 + (j + 0.5) * W / k
        r = 6 + g * 0.8
        p.append(f'<circle cx="{cx:.0f}" cy="{y}" r="{r:.0f}" fill="{c}"/>')
    rs.append(rot(0, y - 20, n, w=260, tam=30, cor=c if c == OXID else TINTA, peso=700, alinha="right"))
p.append("</svg>")
rs.append(rot(x0, 300, "doze horas depois de uma sessão de força", w=W, tam=24, cor=MUDO, alinha="center"))
S.append({"id": "areta", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Areta e colaboradores, 2013", "titulo": "Mesmo total, três distribuições",
          "destaque": "4 × 20 g teve a maior síntese miofibrilar. Limite: síntese aguda em 12 h, whey, 24 homens jovens. Sinal sobre padrão, não prova de hipertrofia.",
          "destaque_cor": "ambar", "fonte": "Journal of Physiology 2013"})

# 4. Trommelen
S.append({"id": "teto", "tipo": "duas", "eyebrow": "Trommelen e colaboradores, 2023", "titulo": "O mito do teto de 30 gramas",
          "esq": {"t": "O dado", "cor": "petr",
                  "itens": ["25 g contra 100 g depois de treino de corpo inteiro", "100 g: resposta maior e mais longa",
                            "passou de 12 horas"]},
          "dir": {"t": "A conduta", "cor": "ambar",
                  "itens": ["refeição grande não é desperdício", "0,25 g/kg ou 20 a 40 g a cada 3 a 4 h",
                            "a janela pós-treino é larga, salvo quem treina em jejum"]},
          "destaque": "O problema não é o jantar com 60 g. É o café da manhã com 8.", "destaque_cor": "verm",
          "fonte": "Cell Reports Medicine 2023 · Jäger 2017"})

# 5. qualidade
S.append({"id": "qualidade", "tipo": "cards", "por_linha": 3, "eyebrow": "van Vliet, Burd e van Loon, 2015", "titulo": "Qualidade: o que muda entre as fontes",
          "cards": [{"t": "Digestibilidade", "x": "quanto do ingerido é absorvido; menor na vegetal", "cor": "tinta"},
                    {"t": "Aminoácidos essenciais", "x": "lisina limita nos cereais, metionina nas leguminosas", "cor": "tinta"},
                    {"t": "Leucina", "x": "o gatilho da síntese: 700 a 3.000 mg por dose", "cor": "ambar"}],
          "destaque": "Vegetariano ganha músculo, com ajuste: um pouco mais por refeição, combinar fontes (arroz com feijão), soja, ovos e laticínios.",
          "destaque_cor": "petr", "fonte": "Journal of Nutrition 2015"})

# 6. whey
S.append({"id": "whey", "tipo": "frase", "fundo": "petr", "eyebrow": "O suplemento de proteína",
          "frase": "Whey é comida em pó.",
          "apoio": "Proteína do leite, conveniente, fácil de dosar. Não é mágica nem obrigatória. A pergunta não é “precisa de whey?”. É “está fechando a conta com comida?”."})

# 7. idoso
xs = [i / 100 for i in range(0, 61)]
svg, rs = linhas(1664, 340, "Síntese miofibrilar por dose de proteína por refeição: o jovem chega ao platô perto de 0,24 g/kg; o idoso só perto de 0,40 g/kg",
                 [{"nome": "", "cor": OXID, "pts": [(x, 100 * min(1, x / 0.24) ** 0.7) for x in xs]},
                  {"nome": "", "cor": GLIC, "pts": [(x, 80 * min(1, x / 0.40) ** 0.9) for x in xs]}],
                 0, 0.6, 0, 110, [(0, "0"), (0.24, "0,24"), (0.40, "0,40"), (0.6, "0,6 g/kg")], [], margem=(40, 20, 60, 30),
                 destaques=[{"x": 0.24}, {"x": 0.40}])
rs += [rot(1320, 50, "jovem", w=200, tam=30, cor=OXID, peso=700),
       rot(1160, 110, "idoso", w=200, tam=30, cor=GLIC, peso=700)]
S.append({"id": "idoso", "tipo": "diagrama", "h": 340, "svg": svg, "rotulos": rs,
          "eyebrow": "Moore e colaboradores, 2015", "titulo": "A mesma refeição rende menos no idoso",
          "destaque": "PROT-AGE: ≥ 1,0 a 1,2 g/kg/dia; ≥ 1,2 para quem se exercita; 1,2 a 1,5 com doença. Para 65 kg, 26 g por refeição.",
          "destaque_cor": "ambar", "fonte": "Esquema das curvas, com os pontos de platô do estudo · Journals of Gerontology 2015 · Bauer 2013"})

# 8. carga e barreiras
S.append({"id": "carga", "tipo": "duas", "eyebrow": "Carga primeiro, proteína junto", "titulo": "O problema do idoso é textura e logística",
          "esq": {"t": "Barreiras", "cor": "ambar",
                  "itens": ["apetite menor, saciedade precoce", "mastigação e prótese", "custo da carne, morar sozinho"]},
          "dir": {"t": "O que resolve", "cor": "petr",
                  "itens": ["ovos, leite, iogurte, queijo", "carne moída ou desfiada, peixe", "leguminosas bem cozidas"]},
          "destaque": "Rim: com função normal, sem sinal de dano nestas faixas. Com doença renal, a decisão é médica, e quem descarta é o exame.",
          "destaque_cor": "tinta"})

# 9. perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "As três perguntas aplicadas", "titulo": "O mesmo número, três condutas",
          "cab": ["Perfil", "A conta", "O problema", "Conduta"],
          "larguras": [24, 26, 22, 28],
          "linhas": [["Vegetariana, 58 kg", "87 g/dia, 1,5 g/kg; 8 g no café", "distribuição", "4 × 20 a 25 g, total um pouco maior"],
                     ["Idoso, 65 kg, começou a treinar", "58 g/dia, 0,9 g/kg", "total baixo", "26 g × 3, com textura"],
                     ["Jovem, 80 kg", "280 g/dia, 3,5 g/kg", "total alto", "≈ 2 g/kg e espaço ao carboidrato"]],
          "destaque": "No primeiro, o total estava certo e a distribuição errada. No segundo, o total baixo. No terceiro, alto demais para o objetivo.",
          "destaque_cor": "petr"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Três perguntas, nessa ordem", "titulo": "Quanto, como distribuir, de que fonte",
          "regras": ["Quanto: 1,6 cobre a maioria; até 2,2 como margem; mais em déficit",
                     "Como: 3 a 4 refeições com proteína decente; o café da manhã primeiro",
                     "De que fonte: ajuste na vegetal; no idoso, 0,4 g/kg por refeição, com carga"],
          "cards": [{"t": "Nutricionista", "x": "Plano, fontes e quantidades."},
                    {"t": "Médico", "x": "Rim, exames e medicação."},
                    {"t": "Educador físico", "x": "A carga que dá motivo ao músculo."}],
          "quem": "Total, distribuição e fonte: três perguntas que qualquer profissional sabe fazer."})

spec = {"arquivo": "aulas/MOD04/04-05-proteina-dose-distribuicao-e-qualidade.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Proteína no praticante de exercício", "subtitulo": "Dose diária, distribuição e qualidade",
        "nota_capa": "Entra pelos três números que todo mundo mistura.",
        "secoes": {"quanto": ["Quanto: 0,8, 1,6 e 2,2.", "capa"],
                   "distribuicao": ["Como distribuir, e de que fonte.", "areta"],
                   "idoso": ["O idoso e os três perfis.", "idoso"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-05.json"), "w"), ensure_ascii=False, indent=1)
print("04-05.json:", len(S), "slides")
