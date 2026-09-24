"""Spec do deck 3.3. Gera 03-03.json ao lado deste arquivo."""
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

# 1. doze vezes
p = [svg_abre(1664, 400, "Noradrenalina plasmática de 219 para 2.738 pg/mL e adrenalina de 49 para 555 pg/mL, do repouso para 8 minutos a 90% do VO2máx")]
ESC = 0.36
linhas_ = [("Noradrenalina", 219, 2738, FOSF, 20), ("Adrenalina", 49, 555, AZUL, 220)]
rs = []
for nome, rep, esf, cor, y in linhas_:
    p.append(f'<rect x="360" y="{y}" width="{max(rep*ESC, 6):.0f}" height="60" rx="4" fill="{MUDO}"/>')
    p.append(f'<rect x="360" y="{y+76}" width="{esf*ESC:.0f}" height="60" rx="4" fill="{cor}"/>')
    rs += [rot(0, y + 50, nome, w=250, tam=30, cor=TINTA, peso=700, alinha="right"),
           rot(260, y + 14, "repouso", w=90, tam=24, cor=MUDO, alinha="right"),
           rot(260, y + 90, "90%", w=90, tam=24, cor=MUDO, alinha="right"),
           rot(360 + max(rep * ESC, 6) + 16, y + 10, f"{rep} pg/mL", w=260, tam=28, cor=TINTA, peso=600),
           rot(360 + esf * ESC + 16, y + 82, f"{esf:,} pg/mL".replace(",", "."), w=280, tam=32, cor=TINTA, peso=700, serif=True)]
p.append("</svg>")
S.append({"id": "doze", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Oito minutos a 90% do VO₂máx", "titulo": "Doze vezes, em minutos",
          "destaque": "A subida significativa só apareceu a 90%. Em intensidade baixa e moderada, o sistema mexe pouco; acima de um certo ponto, dispara.",
          "destaque_cor": "verm", "fonte": "Sothmann, Gustafson e Chandler, Journal of Applied Physiology 1987 · sete homens treinados, 30, 60 e 90% do VO₂máx"})

# 2. hormônio e neurotransmissor
S.append({"id": "origem", "tipo": "duas", "eyebrow": "De onde vem cada uma", "titulo": "Um hormônio e um neurotransmissor que vazou",
          "esq": {"t": "Adrenalina", "cor": "petr",
                  "itens": ["produzida na medula da adrenal", "cai na circulação e age longe", "é a peça endócrina do sistema"]},
          "dir": {"t": "Noradrenalina", "cor": "verm",
                  "itens": ["liberada nas terminações simpáticas, dentro dos tecidos", "no plasma, o excedente que escapou das sinapses",
                            "marca quanto o simpático está acionado"]},
          "destaque": "Noradrenalina plasmática não é um comando que desce. É o eco de uma atividade local, espalhada pelo corpo.",
          "destaque_cor": "tinta"})

# 3. o que fazem
S.append({"id": "efeitos", "tipo": "cards", "por_linha": 3, "eyebrow": "Muita coisa ao mesmo tempo", "titulo": "Liga em segundos, desliga em minutos",
          "cards": [{"t": "Coração", "x": "mais frequência e mais força", "cor": "verm"},
                    {"t": "Vaso", "x": "fecha víscera e pele, abre o músculo que trabalha", "cor": "verm"},
                    {"t": "Brônquio", "x": "dilata: o mesmo receptor da medicação de asma", "cor": "tinta"},
                    {"t": "Fígado", "x": "quebra glicogênio, solta glicose", "cor": "ambar"},
                    {"t": "Tecido adiposo", "x": "libera gordura", "cor": "ambar"},
                    {"t": "Músculo", "x": "acelera a glicólise, com oxigênio sobrando", "cor": "petr"}],
          "destaque": "Parte do lactato do esforço intenso depende da adrenalina, não da falta de oxigênio.",
          "destaque_cor": "petr", "fonte": "Hargreaves e Spriet, Nature Metabolism 2020"})

# 4. treinado
p = [svg_abre(1664, 380, "Na mesma carga absoluta, o treinado libera menos catecolamina que o destreinado; no esforço máximo, libera mais adrenalina")]
grupos = [("Mesma carga absoluta", [(OXID, 90, "treinado"), (MUDO, 170, "destreinado")]),
          ("Esforço máximo", [(OXID, 250, "treinado"), (MUDO, 180, "destreinado")])]
rs = []
for g, (titulo_g, barras) in enumerate(grupos):
    x0 = g * 860
    p.append(f'<line x1="{x0}" y1="320" x2="{x0+780}" y2="320" stroke="{MUDO}" stroke-width="2"/>')
    for b, (cor, h, nome) in enumerate(barras):
        x = x0 + 120 + b * 300
        p.append(f'<rect x="{x}" y="{320-h}" width="200" height="{h}" rx="4" fill="{cor}"/>')
        rs.append(rot(x - 50, 330, nome, w=300, tam=26, cor=TINTA, peso=600, alinha="center"))
    rs.append(rot(x0, 0, titulo_g, w=780, tam=30, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "treinado", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A medula adrenal esportiva", "titulo": "Mais econômico no submáximo, mais capaz no máximo",
          "fonte": "Esquema, sem valores medidos · Kjær, European Journal of Applied Physiology 1998 · Zouhal e colaboradores, Sports Medicine 2008"})

# 5. relógio no dia da prova
t = list(range(0, 31))
treino = [(m, 70 + 85 * (1 - math.exp(-m / 3)) if m > 5 else 70) for m in t]
prova = [(m, 95 + 72 * (1 - math.exp(-(m) / 3)) if m > 5 else 95) for m in t]
svg, rs = linhas(1000, 400, "Frequência cardíaca na mesma carga: no dia da competição a curva começa mais alta antes do esforço e fica acima da curva do treino",
                 [{"nome": "", "cor": OXID, "pts": treino}, {"nome": "", "cor": FOSF, "pts": prova}],
                 0, 30, 50, 180, [(0, "antes"), (5, "início"), (30, "mesma carga")], [],
                 margem=(20, 20, 60, 20))
rs += [rot(560, 8, "dia da prova", w=300, tam=28, cor=FOSF, peso=700),
       rot(560, 98, "treino", w=300, tam=28, cor=OXID, peso=700),
       rot(10, 160, "já alta antes da luta", w=160, tam=24, cor=FOSF, peso=600)]
p = [svg.replace("</svg>", "")]
for i, (tt, cor) in enumerate([("calor", GLIC), ("desidratação", GLIC), ("cafeína e pré-treino", GLIC)]):
    p.append(f'<rect x="1080" y="{40 + i*110}" width="584" height="84" rx="42" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
    rs.append(rot(1080, 40 + i * 110 + 26, tt, w=584, tam=28, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
svg5 = "".join(p).replace('width="1000" height="400" viewBox="0 0 1000 400"', 'width="1664" height="400" viewBox="0 0 1664 400"')
S.append({"id": "relogio", "tipo": "diagrama", "h": 400, "svg": svg5, "rotulos": rs,
          "eyebrow": "A judoca antes da primeira luta", "titulo": "A zona do treino não serve na prova",
          "destaque": "Em alta ativação simpática, prescreva por percepção de esforço. O relógio mede a intensidade somada à emoção.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos · Buchheit, Frontiers in Physiology 2014"})

# 6. betabloqueador e estimulantes
S.append({"id": "beta", "tipo": "duas", "eyebrow": "A situação espelhada", "titulo": "Quando o relógio subestima o esforço",
          "esq": {"t": "Betabloqueador", "cor": "petr",
                  "itens": ["a frequência não sobe como a de outra pessoa", "o pico fica achatado",
                            "percentual da máxima prevista subestima o esforço", "percepção de esforço vira o instrumento principal"]},
          "dir": {"t": "Estimulantes", "cor": "verm",
                  "itens": ["cafeína em dose alta, termogênico, pré-treino adrenérgico", "somam num sistema que o exercício já aciona",
                            "saudável, dose habitual: costuma ser tolerado", "arritmia, hipertensão mal controlada, doença cardíaca: cuidado"]},
          "destaque": "No betabloqueado, a percepção de esforço deixa de ser alternativa: é o instrumento, para prescrever e para interpretar um teste.",
          "destaque_cor": "petr"})

# 7. o que não explica
S.append({"id": "limites", "tipo": "duas", "eyebrow": "Onde a conversa escorrega", "titulo": "O que esse sistema explica, e o que não explica",
          "esq": {"t": "Explica", "cor": "petr",
                  "itens": ["a subida rápida da frequência cardíaca, até antes do esforço", "a redistribuição de fluxo",
                            "glicose e gordura disponíveis, parte do lactato", "a diferença entre treino e prova"]},
          "dir": {"t": "Não explica", "cor": "verm",
                  "itens": ["cansaço de meses: sobe em segundos, cai em minutos", "não é exame de painel de atleta",
                            "metanefrinas: só na suspeita de feocromocitoma", "não é o que se trata: trata-se o contexto"]},
          "fonte": "Lenders e colaboradores, Endocrine Society 2014"})

# 8. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Um sistema de agora", "titulo": "Doze vezes em minutos, e de volta em minutos",
          "regras": ["No dia da prova, no calor e no betabloqueado, o relógio mede outra coisa",
                     "Prescreva pela percepção de esforço"],
          "cards": [{"t": "Médico", "x": "Betabloqueador, suspeita de feocromocitoma, estimulante em quem tem doença cardíaca."},
                    {"t": "Educador físico e preparador", "x": "Prescrevem por percepção de esforço e ensinam o atleta a usá-la."}],
          "quem": "Cansaço de seis meses não é adrenalina alta o tempo todo."})

spec = {"arquivo": "aulas/MOD03/03-03-catecolaminas-e-a-resposta-aguda.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Catecolaminas no exercício", "subtitulo": "Resposta simpatoadrenal aguda e adaptações ao treino",
        "nota_capa": "Entra pelo número.",
        "secoes": {"numero": ["O número e de onde vem cada catecolamina.", "capa"],
                   "efeitos": ["O que fazem e o que o treino muda.", "efeitos"],
                   "relogio": ["O relógio no dia da prova e no betabloqueado.", "relogio"],
                   "limites": ["O que o sistema não explica.", "limites"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-03.json"), "w"), ensure_ascii=False, indent=1)
print("03-03.json:", len(S), "slides")
