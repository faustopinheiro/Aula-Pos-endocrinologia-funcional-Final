"""Spec do deck 3.9. Gera 03-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. Breen
S.append({"id": "breen", "tipo": "numeros", "eyebrow": "Breen e colaboradores, 2013", "titulo": "Catorze dias andando menos",
          "numeros": [{"n": "−76%", "x": "passos por dia, para cerca de 1.400", "cor": "tinta"},
                      {"n": "−43%", "x": "sensibilidade à insulina depois da refeição", "cor": "verm"},
                      {"n": "−26%", "x": "síntese de proteína muscular depois da refeição", "cor": "verm"}],
          "destaque": "Resistência anabólica instalada em duas semanas, e massa magra da perna menor. Em idosos saudáveis, sem cama e sem doença.",
          "destaque_cor": "verm", "fonte": "Journal of Clinical Endocrinology and Metabolism 2013"})

# 2. McGlory
p = [svg_abre(1664, 360, "Linha do tempo: uma semana habitual, catorze dias com menos de mil passos, catorze dias de volta; o controle da glicose e a síntese de proteína pioram e não voltam ao ponto de partida"),]
fases = [("7 dias habituais", 0, 300, OXID_T, OXID), ("14 dias com < 1.000 passos", 320, 640, FOSF_T, FOSF), ("14 dias de volta", 980, 684, AZUL_T, AZUL)]
rs = []
for nome, x, w, fundo, cor in fases:
    p.append(f'<rect x="{x}" y="20" width="{w}" height="60" rx="8" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    rs.append(rot(x, 34, nome, w=w, tam=26, cor=TINTA, peso=700, alinha="center"))
pts = [(0, 240), (300, 240), (960, 150), (1664, 185)]
p.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in [(0, 150), (300, 150), (960, 280), (1664, 250)])}" fill="none" stroke="{FOSF}" stroke-width="6" stroke-linejoin="round"/>')
p.append(f'<line x1="0" y1="150" x2="1664" y2="150" stroke="{MUDO}" stroke-width="2" stroke-dasharray="10 8"/>')
p.append("</svg>")
rs += [rot(20, 104, "ponto de partida", w=300, tam=24, cor=MUDO),
       rot(1180, 280, "não voltou", w=480, tam=30, cor=FOSF, peso=700, alinha="right"),
       rot(560, 300, "controle da glicose e síntese de proteína", w=600, tam=26, cor=FOSF, peso=600)]
S.append({"id": "mcglory", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "McGlory e colaboradores, 2018", "titulo": "Duas semanas para perder; duas de volta não bastaram",
          "destaque": "As adaptações se perdem mais rápido do que se constroem, e a volta não é o espelho da ida.",
          "destaque_cor": "tinta", "fonte": "Esquema da linha do tempo, sem valores medidos · 22 adultos com sobrepeso e pré-diabetes, 69 anos · Journals of Gerontology 2018"})

# 3. Walker, a concessão
S.append({"id": "walker", "tipo": "duas", "eyebrow": "A concessão que o tema pede", "titulo": "O estrago depende de quanto cai, e de quem cai",
          "esq": {"t": "Walker e colaboradores, 2024", "cor": "petr",
                  "itens": ["66 idosos, quase 8 em 10 mulheres, sorteados", "menos de 2.000 passos por 2 semanas",
                            "massa magra da perna e função: sem mudança"]},
          "dir": {"t": "O que diferencia os estudos", "cor": "ambar",
                  "itens": ["mil passos não é o mesmo que dois mil", "pré-diabetes não é o mesmo que metabolismo bom",
                            "o dado mais consistente: o metabólico, no mais vulnerável"]},
          "destaque": "E é esse grupo que a gente mais encontra depois de internação e cirurgia.", "destaque_cor": "tinta",
          "fonte": "European Journal of Applied Physiology 2024 · ensaio randomizado"})

# 4. ordem de perda
etapas = [("volume plasmático", "dias", FOSF, FOSF_T, 1), ("enzimas e glicogênio", "semanas", GLIC, GLIC_T, 2),
          ("VO₂máx", "primeiras semanas", GLIC, GLIC_T, 3), ("coração", "meses", AZUL, AZUL_T, 4), ("força", "a mais resistente", OXID, OXID_T, 5)]
p = [svg_abre(1664, 380, "Ordem da perda, da mais rápida à mais lenta: volume plasmático em dias; enzimas, mitocôndria e glicogênio em semanas; VO2máx nas primeiras semanas; coração em meses; força, a mais resistente")]
rs = []
for i, (nome, tempo, cor, fundo, k) in enumerate(etapas):
    x = i * 334
    p.append(f'<rect x="{x}" y="40" width="310" height="200" rx="12" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    rs.append(rot(x + 12, 70, nome, w=286, tam=28, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x + 12, 170, tempo, w=286, tam=26, cor=cor, peso=700, alinha="center"))
p.append(f'<line x1="0" y1="290" x2="1640" y2="290" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M1640 290 l-20 -12 v24 z" fill="{MUDO}"/>')
p.append("</svg>")
rs.append(rot(0, 306, "perde primeiro · volta primeiro", w=800, tam=26, cor=FOSF, peso=700))
rs.append(rot(864, 306, "perde por último · volta por último", w=780, tam=26, cor=OXID, peso=700, alinha="right"))
S.append({"id": "ordem", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Mujika e Padilla, 2000", "titulo": "O que se perde primeiro volta mais rápido",
          "destaque": "A primeira semana de volta pesa por causa da parte hidráulica, que é a mais barata de recuperar.",
          "destaque_cor": "petr", "fonte": "Esquema de ordem, sem valores medidos · Sports Medicine 2000, partes I e II"})

# 5. memória muscular
t = list(range(0, 13))
svg, rs = linhas(1664, 360, "Duas trajetórias de reconquista de massa e força: quem já treinou volta mais rápido do que quem nunca treinou",
                 [{"nome": "", "cor": OXID, "pts": [(m, 100 * (1 - math.exp(-m / 2.5))) for m in t]},
                  {"nome": "", "cor": MUDO, "pts": [(m, 100 * (1 - math.exp(-m / 6))) for m in t], "tracejado": True}],
                 0, 12, 0, 105, [(0, "retomada"), (12, "semanas")], [], margem=(20, 20, 60, 20))
rs += [rot(300, 20, "já treinou antes", w=400, tam=28, cor=OXID, peso=700),
       rot(1000, 200, "nunca treinou", w=400, tam=28, cor=MUDO, peso=700)]
S.append({"id": "memoria", "tipo": "diagrama", "h": 360, "svg": svg, "rotulos": rs,
          "eyebrow": "Memória muscular", "titulo": "Quem já construiu reconstrói mais rápido",
          "destaque": "O mecanismo, núcleos retidos na fibra, segue em debate em humanos. O fenômeno é consistente o bastante para ser dito ao paciente.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos"})

# 6. duas conversas
S.append({"id": "conversas", "tipo": "duas", "eyebrow": "Duas conversas opostas", "titulo": "Duas semanas não estragam; três meses custam",
          "esq": {"t": "Acalmar quem para pouco", "cor": "petr",
                  "itens": ["custa volume plasmático e um pouco de enzima", "a aptidão mal se move",
                            "o medo faz gente treinar doente e voltar cedo"]},
          "dir": {"t": "Não banalizar quem para muito", "cor": "verm",
                  "itens": ["tempo parado mais tempo de voltar", "pós-internação: volta para trás do ponto de partida",
                            "a redução silenciosa também é destreino"]}})

# 7. manutenção
S.append({"id": "manter", "tipo": "lista", "eyebrow": "O oposto do repouso por precaução", "titulo": "Manter alguma coisa vale muito mais que nada",
          "itens": [{"t": "Dose de manutenção", "x": "1 a 2 sessões de força por semana, carga perto da habitual", "cor": "petr"},
                    {"t": "Na lesão, o que o quadro permitir", "x": "pedalar, nadar, poupar só o que precisa", "cor": "petr"},
                    {"t": "Treinar o lado saudável", "x": "educação cruzada atenua a perda do lado imobilizado", "cor": "ambar"}],
          "destaque": "Quem mantém alguma coisa não está treinando pouco. Está encurtando muito o retorno.",
          "destaque_cor": "tinta"})

# 8. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que os números decidem", "titulo": "Afastamento não é binário",
          "regras": ["Duas semanas não vão te estragar; três meses vão custar: vamos manter alguma coisa",
                     "A primeira semana de volta é ruim, e é a parte barata",
                     "No idoso e no pós-operatório, o relógio corre mais rápido"],
          "cards": [{"t": "Preparador e educador físico", "x": "Dose de manutenção e retorno progressivo."},
                    {"t": "Fisioterapia", "x": "O mesmo em tecido lesionado."},
                    {"t": "Médico", "x": "A liberação clínica quando há condição médica."}],
          "quem": "Enxergar o afastamento antes que vire hábito é de toda a equipe."})

spec = {"arquivo": "aulas/MOD03/03-09-destreino-e-reversao-das-adaptacoes.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Destreino", "subtitulo": "Cronologia da perda e da recuperação das adaptações",
        "nota_capa": "Entra pelo número: catorze dias.",
        "secoes": {"numero": ["Os três estudos de redução de passos.", "capa"],
                   "ordem": ["A ordem da perda e a memória muscular.", "ordem"],
                   "conduta": ["As duas conversas e a manutenção.", "conversas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-09.json"), "w"), ensure_ascii=False, indent=1)
print("03-09.json:", len(S), "slides")
