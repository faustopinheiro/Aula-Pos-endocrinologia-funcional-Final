"""Spec do deck 3.12. Gera 03-12.json ao lado deste arquivo."""
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

# 1. dois ensaios
S.append({"id": "ensaios", "tipo": "numeros", "eyebrow": "Dois ensaios, a mesma vitamina", "titulo": "Resultados opostos",
          "numeros": [{"n": "−20%", "x": "fratura por estresse: 5.201 recrutas, cálcio e vitamina D (Lappe, 2008)", "cor": "petr"},
                      {"n": "0,98", "x": "razão de risco de fratura: 25.871 adultos, vitamina D (LeBoff, 2022)", "cor": "verm"}],
          "destaque": "A diferença não está na molécula. Está em quem tomou.",
          "destaque_cor": "tinta", "fonte": "Journal of Bone and Mineral Research 2008 · New England Journal of Medicine 2022, estudo VITAL"})

# 2. quem tomou
S.append({"id": "quem", "tipo": "duas", "eyebrow": "Quem tomou", "titulo": "Boa para quem tem o problema que ela resolve",
          "esq": {"t": "Recrutas da Marinha", "cor": "petr",
                  "itens": ["mulheres jovens", "carga óssea nova e muito alta", "risco concentrado em semanas",
                            "2.000 mg de cálcio junto com 800 UI"]},
          "dir": {"t": "VITAL", "cor": "ambar",
                  "itens": ["homens de 50 e mulheres de 55 anos ou mais", "vida comum, sem carga aguda",
                            "vitamina D inicial média de 30,7 ng/mL", "2.000 UI de vitamina D, sozinha"]},
          "destaque": "No VITAL, o resultado nulo não mudou com o nível inicial de vitamina D.", "destaque_cor": "tinta"})

# 3. hierarquia
p = [svg_abre(1664, 380, "Três entradas para o osso, de tamanhos diferentes: carga mecânica, a maior; disponibilidade energética, a do meio; cálcio e vitamina D, a menor")]
ents = [("carga mecânica", "impacto e magnitude", 1.0, OXID, OXID_T),
        ("disponibilidade energética", "eixo gonadal, substrato, remodelamento", 0.66, GLIC, GLIC_T),
        ("cálcio e vitamina D", "o substrato", 0.33, AZUL, AZUL_T)]
rs = []
for i, (nome, sub, f, cor, fundo) in enumerate(ents):
    y = 10 + i * 124
    w = 1280 * f
    p.append(f'<rect x="0" y="{y}" width="{w:.0f}" height="104" rx="10" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    p.append(f'<path d="M{w+10:.0f} {y+52} L1356 {y+52}" stroke="{cor}" stroke-width="6"/><path d="M1376 {y+52} l-22 -14 v28 z" fill="{cor}"/>')
    rs.append(rot(24, y + 18, f"{i+1}. {nome}", w=max(w - 40, 380), tam=30, cor=TINTA, peso=700))
    rs.append(rot(24, y + 60, sub, w=max(w - 40, 380), tam=24, cor=APOIO2))
p.append(f'<rect x="1384" y="10" width="280" height="352" rx="20" fill="{CLARO}" stroke="{TINTA}" stroke-width="4"/>')
p.append("</svg>")
rs.append(rot(1384, 164, "osso", w=280, tam=36, cor=TINTA, peso=700, alinha="center"))
S.append({"id": "hierarquia", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Antes da decisão, a hierarquia", "titulo": "Carga, conta, substrato",
          "destaque": "Nadador e ciclista não recebem do esporte o estímulo ósseo do corredor. Para eles, força e impacto controlado cobrem uma lacuna.",
          "destaque_cor": "petr", "fonte": "Esquema de hierarquia, sem valores medidos · consenso do COI sobre REDs, British Journal of Sports Medicine 2023"})

# 4. três saídas
p = [svg_abre(1664, 400, "Três saídas: A, não dosar de rotina e garantir o essencial; B, dosar de forma dirigida; C, repor"),
     "<defs>" + seta_marker("s1", OXID) + seta_marker("s2", GLIC) + seta_marker("s3", FOSF) + "</defs>"]
p.append(caixa(0, 140, 320, 120, TINTA, CLARO, esp=3))
said = [("A · não dosar de rotina", "a maioria dos praticantes saudáveis: sol habitual e cálcio pela comida", OXID, OXID_T, "s1"),
        ("B · dosar de forma dirigida", "quem tem fator de risco: aí o exame muda conduta", GLIC, GLIC_T, "s2"),
        ("C · repor", "deficiência documentada, ou risco alto com carga óssea intensa", FOSF, FOSF_T, "s3")]
rs = [rot(0, 172, "o praticante", w=320, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 212, "depois da triagem", w=320, tam=22, cor=MUDO, alinha="center")]
for i, (t, x, cor, fundo, mid) in enumerate(said):
    y = 10 + i * 134
    p.append(seta(330, 200, 500, y + 56, cor, mid, esp=5))
    p.append(caixa(520, y, 1144, 112, cor, fundo, esp=3))
    rs.append(rot(548, y + 14, t, w=1090, tam=30, cor=cor, peso=700))
    rs.append(rot(548, y + 60, x, w=1090, tam=26, cor=TINTA))
p.append("</svg>")
S.append({"id": "saidas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A decisão", "titulo": "Três saídas",
          "destaque": "A saída A não dispensa triagem. Ela depende da triagem: sem perguntar, você perde quem tinha fator de risco.",
          "destaque_cor": "ambar"})

# 5. em quem dosar
S.append({"id": "dosar", "tipo": "cards", "por_linha": 3, "eyebrow": "Saída B · Farrokhyar e colaboradores, 2015", "titulo": "56% dos atletas com vitamina D inadequada",
          "cards": [{"t": "Ambiente e pele", "x": "inverno e primavera, latitude alta, treino em ambiente fechado, pele mais pigmentada", "cor": "ambar"},
                    {"t": "Osso e energia", "x": "fratura por estresse, baixa disponibilidade energética, transtorno alimentar, ciclo alterado", "cor": "verm"},
                    {"t": "Absorção e remédios", "x": "celíaca, doença inflamatória intestinal, bariátrica, anticonvulsivante, corticoide, dieta sem laticínios", "cor": "tinta"}],
          "destaque": "Esse é o grupo em que dosar muda conduta. Fora dele, o exame produz mais ansiedade e mais frasco do que decisão.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2015 · meta-análise"})

# 6. repor
S.append({"id": "repor", "tipo": "lista", "eyebrow": "Saída C", "titulo": "Repor, e onde isso se sustenta",
          "itens": [{"t": "Deficiência documentada", "x": "aqui a reposição tem base e muda desfecho", "cor": "petr"},
                    {"t": "Risco alto com carga óssea intensa", "x": "o cenário das recrutas, e era cálcio e vitamina D juntos", "cor": "petr"},
                    {"t": "Repor para todo mundo", "x": "o cenário do VITAL: dose generosa, nenhuma fratura a menos", "cor": "verm"},
                    {"t": "Cálcio: comida primeiro", "x": "suplemento para quem não alcança pela dieta, dose caso a caso", "cor": "ambar"}],
          "gap_itens": 22})

# 7. o critério
S.append({"id": "criterio", "tipo": "frase", "fundo": "tinta", "eyebrow": "O critério",
          "frase": "Corrigir deficiência, não perseguir número alto.",
          "apoio": "Otimizar, em busca de desempenho, imunidade ou força, não tem sustentação equivalente. Se alguém disser um número, pergunte de onde veio e que desfecho ele previu."})

# 8. segurança
S.append({"id": "seguranca", "tipo": "duas", "eyebrow": "Duas notas de segurança", "titulo": "Nem a dose alta nem o exame são neutros",
          "esq": {"t": "Vitamina D em dose alta não é inócua", "cor": "verm",
                  "itens": ["intoxicação pela subida do cálcio no sangue", "megadose", "dose de ataque repetida sem controle",
                            "aparece em quem toma por conta própria"]},
          "dir": {"t": "Densitometria tem indicação", "cor": "tinta",
                  "itens": ["fratura por estresse repetida", "baixa disponibilidade energética sustentada",
                            "amenorreia prolongada ou transtorno alimentar", "corticoide crônico"]},
          "destaque": "Dose quem tem risco, corrija quem tem deficiência, cálcio pela comida. Carga e conta energética são as intervenções principais.",
          "destaque_cor": "petr"})

# 9. módulo: decisão e contribuição
S.append({"id": "niveis", "tipo": "tabela", "eyebrow": "O módulo nos três níveis", "titulo": "Decisão e contribuição",
          "cab": ["Quem", "Decide", "Contribui com"],
          "larguras": [30, 32, 38],
          "linhas": [["Médico", "exame hormonal e reposição", "a leitura do número pela história"],
                     ["Educador e preparador físico", "estímulo e distribuição", "a queda de rendimento"],
                     ["Nutricionista", "energia, proteína, cálcio", "há quanto tempo está em déficit"],
                     ["Fisioterapeuta", "carga em tecido em recuperação", "a fratura que se repete"],
                     ["Psicólogo", "transtorno alimentar, com o médico", "a restrição de origem comportamental"]],
          "destaque": "Quem convive toda semana é quem escuta sobre substância, e pode levar isso adiante, com consentimento.",
          "destaque_cor": "tinta"})

# 10. reconhecimento
S.append({"id": "reconhecer", "tipo": "cards", "por_linha": 3, "eyebrow": "O terceiro nível é de todos", "titulo": "Reconhecer exige ter aprendido o sinal",
          "cards": [{"t": "Vários eixos", "x": "levemente deslocados na mesma direção", "cor": "tinta"},
                    {"t": "Só quando perguntados", "x": "libido e ereção matinal", "cor": "tinta"},
                    {"t": "O ciclo que espaçou", "x": "e a fratura por estresse que se repete", "cor": "tinta"},
                    {"t": "Ronco e pausas", "x": "relatados por quem dorme ao lado", "cor": "tinta"},
                    {"t": "Fadiga de meses", "x": "que não cede com menos carga", "cor": "ambar"},
                    {"t": "Fora deste módulo", "x": "perda de peso sem intenção, pele escurecendo, campo visual, ideação suicida", "cor": "verm"}]})

# 11. fecho do módulo
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que atravessou as doze aulas", "titulo": "O que separa as duas leituras é a história",
          "regras": ["O mesmo número admite duas leituras: disfunção, ou eixo respondendo ao contexto",
                     "Cortisol de quem treinou de manhã, T3 de quem está em déficit, testosterona de quem dorme cinco horas",
                     "A vitamina D só importa em quem tem o problema que ela resolve"],
          "cards": [{"t": "Decisão", "x": "De quem tem a profissão para ela."},
                    {"t": "Contribuição", "x": "A informação que passa de uma profissão para outra."},
                    {"t": "Reconhecimento", "x": "De todos."}],
          "quem": "No próximo módulo, a nutrição esportiva abre pela disponibilidade energética."})

spec = {"arquivo": "aulas/MOD03/03-12-vitamina-d-calcio-e-saude-ossea.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Saúde óssea no praticante de exercício", "subtitulo": "Vitamina D, cálcio e decisão de suplementar",
        "nota_capa": "Entra pelos dois ensaios opostos. Fecha o módulo.",
        "secoes": {"ensaios": ["Dois ensaios e a hierarquia do osso.", "capa"],
                   "decisao": ["As três saídas e o critério.", "saidas"],
                   "modulo": ["O módulo nos três níveis.", "niveis"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-12.json"), "w"), ensure_ascii=False, indent=1)
print("03-12.json:", len(S), "slides")
