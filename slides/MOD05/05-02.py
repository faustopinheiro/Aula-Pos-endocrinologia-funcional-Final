"""Spec do deck 5.2. Gera 05-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. evidência e confusão
S.append({"id": "confusao", "tipo": "frase", "fundo": "tinta", "eyebrow": "O suplemento mais estudado",
          "frase": "Muita evidência, muita confusão.",
          "apoio": "Rim, cabelo, ciclar, cãibra, “quase anabolizante”, “criança não pode”. Quase toda confusão sobre creatina é de magnitude: há quem espere o efeito de um anabolizante, e há quem descarte um efeito real por ser pequeno."})

# 2. de onde vem, quanto cabe
p = [svg_abre(1664, 300, "Régua do estoque de creatina no músculo: cerca de 120 mmol por quilo de músculo seco no habitual, teto de saturação de 150 a 160")]
fx = lambda v: (v - 80) / 100 * 1664
p.append(f'<rect x="{fx(80):.0f}" y="120" width="{fx(120)-fx(80):.0f}" height="80" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
p.append(f'<rect x="{fx(120):.0f}" y="120" width="{fx(155)-fx(120):.0f}" height="80" fill="{OXID_T}" stroke="{OXID}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{fx(155):.0f}" y1="90" x2="{fx(155):.0f}" y2="230" stroke="{FOSF}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(fx(80) + 20, 144, "estoque habitual ≈ 120", w=700, tam=30, cor=AZUL, peso=700),
      rot(fx(120) + 10, 144, "espaço da suplementação", w=560, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(fx(155) - 220, 40, "teto ≈ 150 a 160", w=440, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(0, 244, "mmol por quilo de músculo seco · síntese ≈ 1 g/dia · carne e peixe ≈ 1 a 2 g/dia · 95% no músculo", w=1664, tam=26, cor=MUDO, alinha="center")]
S.append({"id": "tanque", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os números de base · Kreider, 2017", "titulo": "Um tanque com tampa",
          "destaque": "Quando enche, acabou: creatina a mais não sobe mais nada. E 1 a 2% do estoque vira creatinina todo dia; guarde isso para o exame de sangue.",
          "destaque_cor": "petr", "fonte": "Journal of the International Society of Sports Nutrition 2017"})

# 3. Hultman
t = [i / 2 for i in range(0, 61)]
carga = [(d, 100 + 20 * (1 - math.exp(-d / 2.2))) for d in t]
lenta = [(d, 100 + 20 * (1 - math.exp(-d / 11))) for d in t]
svg, rs = linhas(1664, 320, "Dois caminhos até o mesmo patamar de creatina muscular: 20 g por dia por 6 dias sobe rápido; 3 g por dia por 28 dias sobe devagar; ambos chegam a cerca de 20% acima do basal",
                 [{"nome": "", "cor": FOSF, "pts": carga}, {"nome": "", "cor": OXID, "pts": lenta}],
                 0, 30, 95, 125, [(0, "dia 0"), (6, "6"), (14, "14"), (28, "28")], [100, 120], margem=(90, 20, 60, 30),
                 yfmt=lambda v: "basal" if v == 100 else "+20%")
rs += [rot(110, 20, "20 g/dia por 6 dias", w=460, tam=28, cor=FOSF, peso=700),
       rot(1000, 170, "3 g/dia por 28 dias", w=460, tam=28, cor=OXID, peso=700)]
S.append({"id": "hultman", "tipo": "diagrama", "h": 320, "svg": svg, "rotulos": rs,
          "eyebrow": "Hultman e colaboradores, 1996", "titulo": "O mesmo destino, por dois caminhos",
          "destaque": "Depois, 2 g/dia mantêm. Carga só se o efeito for preciso em menos de duas semanas. E é uso contínuo: só nos dias de treino deixa o tanque pela metade.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos no traçado · 31 homens, biópsia muscular · Journal of Applied Physiology 1996"})

# 4. o que ela faz
p = [svg_abre(1664, 300, "Repetições em quatro séries: placebo 8, 8, 7, 6; creatina 8, 8, 8, 7. Esquema ilustrativo")]
rs = []
dados = [("placebo", [8, 8, 7, 6], AZUL, AZUL_T), ("creatina", [8, 8, 8, 7], OXID, OXID_T)]
for g, (nome, reps, c, f) in enumerate(dados):
    rs.append(rot(0, 40 + g * 120, nome, w=220, tam=30, cor=c, peso=700, alinha="right"))
    for i, r in enumerate(reps):
        x = 260 + i * 340
        p.append(f'<rect x="{x}" y="{24 + g*120}" width="{r*36}" height="70" rx="8" fill="{f}" stroke="{c}" stroke-width="3"/>')
        rs.append(rot(x + r * 36 + 10, 40 + g * 120, str(r), w=60, tam=30, cor=TINTA, peso=700))
for i in range(4):
    rs.append(rot(260 + i * 340, 262, f"série {i+1}", w=300, tam=24, cor=MUDO))
p.append("</svg>")
S.append({"id": "efeito", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Branch, 2003", "titulo": "A creatina não constrói músculo",
          "destaque": "Ela permite treinar um pouco mais, e é o treino que constrói. Efeito maior no esforço curto e repetido; sem treino, irrelevante.",
          "destaque_cor": "tinta", "fonte": "Esquema ilustrativo, sem valores medidos · International Journal of Sport Nutrition and Exercise Metabolism 2003"})

# 5. o peso
S.append({"id": "peso", "tipo": "numeros", "eyebrow": "As primeiras semanas", "titulo": "O que se vê em uma semana é peso",
          "numeros": [{"n": "1 a 2 kg", "x": "a mais na balança, em boa parte água dentro da célula", "cor": "ambar"},
                      {"n": "antes", "x": "é quando avisar; depois, a pessoa lê como gordura e para", "cor": "petr"},
                      {"n": "categoria", "x": "de peso: efeito colateral real, conversa com técnico e nutricionista", "cor": "verm"}],
          "destaque": "O peso, sozinho, nunca é o desfecho do teste: ele sobe em quase todo mundo, responda a pessoa ou não.",
          "destaque_cor": "tinta"})

# 6. quem responde
S.append({"id": "responde", "tipo": "duas", "eyebrow": "Burke e colaboradores, 2003", "titulo": "Quem chega com o tanque baixo responde mais",
          "esq": {"t": "Tanque cheio", "cor": "tinta",
                  "itens": ["come carne e peixe todo dia", "pouco espaço até o teto", "“não respondedor”: 20 a 30%, em estudos pequenos"]},
          "dir": {"t": "Tanque baixo", "cor": "petr",
                  "itens": ["vegetariano: 117 contra 130 mmol/kg no início", "maior aumento de estoque e de massa magra", "maior ganho de trabalho total"]},
          "destaque": "A primeira pergunta é dietética: quanta carne e peixe essa pessoa come? E a resposta se mede no treino: 4 a 8 semanas, um desfecho escolhido antes.",
          "destaque_cor": "ambar", "fonte": "Medicine and Science in Sports and Exercise 2003 · Syrotuik e Bell 2004"})

# 7. rim
S.append({"id": "rim", "tipo": "duas", "eyebrow": "Mito um · Lugaresi, Gualano e colaboradores, 2013", "titulo": "O rim, e a armadilha do exame",
          "esq": {"t": "O que o ensaio mostrou", "cor": "petr",
                  "itens": ["treinados em força, dieta rica em proteína", "12 semanas, randomizado, com placebo", "filtração medida sem alteração", "proteinúria e albuminúria iguais"]},
          "dir": {"t": "A armadilha", "cor": "verm",
                  "itens": ["creatina vira creatinina", "creatinina sérica um pouco mais alta", "filtração estimada mais baixa", "substrato a mais, não filtração a menos"]},
          "destaque": "Quem usa avisa antes de coletar. Quem tem doença renal ou risco relevante é outra conversa, médica e individual.",
          "destaque_cor": "tinta", "fonte": "Journal of the International Society of Sports Nutrition 2013"})

# 8. outros mitos
S.append({"id": "mitos", "tipo": "cards", "por_linha": 4, "eyebrow": "Mitos dois a cinco", "titulo": "Cada mito com o número que merece",
          "cards": [{"t": "Cabelo", "x": "20 jogadores, mediu hormônio, não cabelo, sem replicação (van der Merwe, 2009)", "cor": "ambar"},
                    {"t": "Cãibra e calor", "x": "sem mais cãibra em temporada no calor (Greenwood, 2003, observacional); sem prejuízo térmico (Lopez, 2009)", "cor": "petr"},
                    {"t": "Esteroide", "x": "não é hormônio, não age no receptor androgênico, não é proibida", "cor": "petr"},
                    {"t": "Ciclar", "x": "ao parar, o estoque volta ao basal; ciclar é tanque pela metade", "cor": "petr"}],
          "destaque": "Quem tem calvície familiar pode não usar, sabendo que a escolha é de precaução, não de evidência.",
          "destaque_cor": "tinta"})

# 9. populações
S.append({"id": "populacoes", "tipo": "tabela", "eyebrow": "Em quem foi estudado", "titulo": "Onde a conta muda",
          "cab": ["População", "O que a evidência mostra", "Na conduta"],
          "larguras": [18, 46, 36],
          "linhas": [["Mulheres", "efeito compatível com o dos homens; menos estudos (Smith-Ryan, 2021)", "dose igual; interesse na menopausa"],
                     ["Idosos", "22 ensaios, 721 pessoas: +1,4 kg de massa magra com treino de força (Chilibeck, 2017)", "só com carga; sem ela, não vale"],
                     ["Adolescentes", "sem sinal de dano nas doses usuais (Jagim e Kerksick, 2021)", "decisão médica, depois da base"],
                     ["Vegetarianos", "tanque mais baixo, resposta maior", "atenção à cápsula de gelatina"]],
          "destaque": "O adolescente “fraco para a idade” tem quatro explicações antes do pote: comida, sono, maturação e treino orientado. E o pote ensina que força se compra.",
          "destaque_cor": "verm"})

# 10. reabilitação e cognição
S.append({"id": "alem", "tipo": "duas", "eyebrow": "Hespel, 2001 · Avgerinos, 2018", "titulo": "Além do desempenho, com sobriedade",
          "esq": {"t": "Reabilitação", "cor": "petr",
                  "itens": ["22 voluntários, 2 semanas de gesso", "não protegeu o músculo parado", "recuperou mais na reabilitação", "estar tomando quando a carga voltar"]},
          "dir": {"t": "Cognição", "cor": "ambar",
                  "itens": ["6 ensaios, 281 pessoas saudáveis", "memória de curto prazo, mais em idosos", "sinal real e modesto", "mecanismo não é indicação"]},
          "destaque": "Entre “tem mecanismo e estudos em andamento” e “está indicado” mora boa parte do marketing de suplemento.",
          "destaque_cor": "tinta", "fonte": "Journal of Physiology 2001 · Experimental Gerontology 2018"})

# 11. protocolo
S.append({"id": "protocolo", "tipo": "lista", "eyebrow": "O protocolo prático", "titulo": "Seis linhas",
          "itens": [{"t": "Forma: monoidratada", "x": "a dos estudos e a mais barata; as outras não mostraram superioridade", "cor": "petr"},
                    {"t": "Dose: 3 a 5 g por dia", "x": "carga de ~20 g por 5 a 6 dias só se houver pressa, em quatro tomadas", "cor": "petr"},
                    {"t": "Horário: o que a pessoa lembrar", "x": "adesão vale mais que horário", "cor": "petr"},
                    {"t": "Com líquido, e numa refeição se incomodar", "x": "desconforto quase sempre é dose alta de uma vez", "cor": "ambar"},
                    {"t": "Dias sem treino: toma igual", "x": "a linha mais esquecida", "cor": "ambar"},
                    {"t": "Por quanto tempo: enquanto houver objetivo", "x": "pote simples, um ingrediente, controle verificável", "cor": "tinta"}],
          "gap_itens": 10})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Os três perfis", "titulo": "Treinar um pouco mais, todo dia",
          "regras": ["Corredor: pequeno na prova; a pergunta é se o treino de força existe",
                     "Mulher na menopausa com musculação: a indicação mais sólida, contínua, sem carga",
                     "Adolescente: ainda não é essa a pergunta; comida, sono, maturação, treino"],
          "cards": [{"t": "Nutricionista", "x": "Indica e dosa."},
                    {"t": "Médico", "x": "Rim, doença de base, adolescente."},
                    {"t": "Educador físico e preparador", "x": "O treino que dá sentido ao pote."}],
          "quem": "Registrar o uso antes de um exame de sangue é de todos."})

spec = {"arquivo": "aulas/MOD05/05-02-creatina-mecanismo-protocolo-mitos-e-populacoes.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Creatina", "subtitulo": "Fisiologia, protocolo de uso, segurança e populações específicas",
        "nota_capa": "Entra pelo contraste entre evidência e confusão.",
        "secoes": {"confusao": ["Os números de base e o protocolo.", "capa"],
                   "efeito": ["O efeito, o peso e quem responde.", "efeito"],
                   "rim": ["Mitos, populações e o protocolo prático.", "rim"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-02.json"), "w"), ensure_ascii=False, indent=1)
print("05-02.json:", len(S), "slides")
