"""Spec do deck 4.1. Gera 04-01.json ao lado deste arquivo."""
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

# 1. a equação
S.append({"id": "equacao", "tipo": "frase", "fundo": "tinta", "eyebrow": "O número que o curso inteiro citou",
          "frase": "(ingestão − gasto do exercício) ÷ massa livre de gordura",
          "apoio": "O que sobra para o corpo funcionar depois que o treino cobrou a parte dele. Disponibilidade energética baixa não é comer pouco. É comer pouco para o que se gasta."})

# 2. a conta
S.append({"id": "conta", "tipo": "numeros", "eyebrow": "Uma conta que desmonta a intuição", "titulo": "Três mil calorias, e abaixo de trinta",
          "numeros": [{"n": "69 kg", "x": "massa livre de gordura: 78 kg com 12% de gordura", "cor": "tinta"},
                      {"n": "2.000", "x": "kcal que sobram: 3.100 ingeridas menos 1.100 do exercício", "cor": "ambar"},
                      {"n": "≈ 29", "x": "kcal por kg de massa livre de gordura por dia", "cor": "verm"}],
          "destaque": "Ninguém que come três mil calorias se vê como alguém que come pouco. É esse perfil que chega para discutir testosterona.",
          "destaque_cor": "tinta"})

# 3. Loucks e Thuma
p = [svg_abre(1664, 380, "Desenho do experimento: disponibilidade de 45, 30, 20 e 10 kcal por kg de massa magra por cinco dias; a pulsatilidade do LH se altera abaixo de 30")]
rs = []
doses = [45, 30, 20, 10]
base, esc, bw = 320, 6, 260
p.append(f'<line x1="120" y1="{base - 30*esc}" x2="1664" y2="{base - 30*esc}" stroke="{TINTA}" stroke-width="3" stroke-dasharray="12 10"/>')
for i, d in enumerate(doses):
    x = 220 + i * 360
    cor, fundo = (OXID, OXID_T) if d >= 30 else (FOSF, FOSF_T)
    p.append(f'<rect x="{x}" y="{base - d*esc}" width="{bw}" height="{d*esc}" rx="6" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    rs.append(rot(x, base - d * esc + 10, str(d), w=bw, tam=34, cor=cor, peso=700, alinha="center"))
    rs.append(rot(x, base + 14, "LH preservado" if d >= 30 else "LH alterado", w=bw, tam=24, cor=cor, peso=600, alinha="center"))
p.append(f'<line x1="120" y1="{base}" x2="1664" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs.append(rot(0, base - 30 * esc - 18, "30", w=100, tam=30, cor=TINTA, peso=700, alinha="right"))
S.append({"id": "loucks", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Loucks e Thuma, 2003", "titulo": "O número tem endereço",
          "destaque": "29 mulheres jovens, sedentárias, ciclo regular, cinco dias. Desfecho: o pulso do LH. Não amenorreia, não fratura, não homens.",
          "destaque_cor": "ambar", "fonte": "Doses do desenho experimental, em kcal por kg de massa magra por dia · Journal of Clinical Endocrinology and Metabolism 2003"})

# 4. revisão
S.append({"id": "revisao", "tipo": "duas", "eyebrow": "Vinte anos depois", "titulo": "De linha a faixa de risco",
          "esq": {"t": "Mulheres · Salamunes, 2024", "cor": "petr",
                  "itens": ["abaixo de 30, a chance de alteração menstrual sobe", "mas há alteração acima e abaixo de 30",
                            "uma linha libera; um risco não libera"]},
          "dir": {"t": "Homens · Koehler, 2016", "cor": "ambar",
                  "itens": ["seis homens, 15 contra 40 kcal/kg, quatro dias", "leptina −53 a −56%, insulina −34 a −38%",
                            "T3, testosterona e IGF-1 ainda parados"]},
          "destaque": "Consenso do COI, 2023: um contínuo, do adaptável ao problemático. Quanto, por quanto tempo, e com que consequência?",
          "destaque_cor": "tinta", "fonte": "Applied Physiology, Nutrition, and Metabolism 2024 · Journal of Sports Sciences 2016"})

# 5. medida
S.append({"id": "medida", "tipo": "cards", "por_linha": 2, "eyebrow": "Burke e colaboradores, 2018", "titulo": "A equação é frágil",
          "cards": [{"t": "Ingestão subestimada", "x": "esquecimento, porção mal estimada, o que se come em pé", "cor": "ambar"},
                    {"t": "Gasto do exercício mal medido", "x": "e quase ninguém desconta o que se gastaria em repouso", "cor": "ambar"},
                    {"t": "Massa magra muda com o método", "x": "o denominador também tem erro", "cor": "ambar"},
                    {"t": "Variação diária grande", "x": "um dia não representa a semana", "cor": "ambar"}],
          "destaque": "O número não é diagnóstico. É ordem de grandeza, e faz o paciente ver a própria conta.",
          "destaque_cor": "petr"})

# 6. hora a hora
hs = list(range(0, 25))
def saldo(perfil):
    return [(h, perfil(h)) for h in hs]
dist = lambda h: 150 * math.sin((h - 3) / 24 * 2 * math.pi) - 60
desorg = lambda h: (-150 - 50 * h if h < 15 else -900 + 120 * (h - 15)) if h < 22 else -60 + 40 * (h - 22)
svg, rs = linhas(1664, 360, "Saldo energético ao longo de 24 horas em duas pessoas com o mesmo total: uma fica pouco tempo abaixo de menos 300; a outra passa horas seguidas abaixo",
                 [{"nome": "", "cor": OXID, "pts": saldo(dist)},
                  {"nome": "", "cor": FOSF, "pts": saldo(desorg)}],
                 0, 24, -1000, 400, [(0, "0 h"), (6, "6 h"), (12, "12 h"), (18, "18 h"), (24, "24 h")], [0, -300],
                 margem=(110, 20, 60, 20), yfmt=lambda v: f"{v:g}")
rs += [rot(400, 36, "come distribuído", w=380, tam=28, cor=OXID, peso=700),
       rot(130, 262, "jejum cedo, almoço tarde, jantar às 22 h", w=640, tam=26, cor=FOSF, peso=700)]
S.append({"id": "horas", "tipo": "diagrama", "h": 360, "svg": svg, "rotulos": rs,
          "eyebrow": "O segundo problema é de tempo", "titulo": "Não importa só quanto. Importa quando",
          "destaque": "Fahrenholtz, 2018: com a mesma conta de 24 h, as atletas com disfunção menstrual passavam 24% mais horas abaixo de −300 kcal.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · eixo em kcal de saldo · Scandinavian Journal of Medicine and Science in Sports 2018; Torstveit 2018, 31 homens"})

# 7. a cadeia
p = [svg_abre(1664, 400, "Déficit derruba leptina e insulina, o hipotálamo lê escassez, e os eixos respondem em relógios diferentes: dias, semanas, meses"),
     "<defs>" + seta_marker("c1", MUDO) + "</defs>"]
etapas = [("déficit", FOSF, FOSF_T), ("leptina e insulina caem", GLIC, GLIC_T), ("hipotálamo lê escassez", AZUL, AZUL_T)]
rs = []
for i, (t, cor, fundo) in enumerate(etapas):
    x = i * 300
    p.append(caixa(x, 20, 260, 110, cor, fundo, esp=3))
    rs.append(rot(x + 10, 44, t, w=240, tam=26, cor=TINTA, peso=700, alinha="center"))
    if i < 2:
        p.append(seta(x + 262, 75, x + 296, 75, MUDO, "c1", esp=4))
eixos = [("gonadal", "cortado primeiro", "semanas"), ("tireoide", "menos T3, TSH normal", "semanas"),
         ("GH e IGF-1", "GH sobe, IGF-1 cai", "semanas"), ("cortisol", "sobe", "dias a semanas"), ("osso", "perde as três entradas", "meses")]
p.append(seta(760, 132, 760, 180, MUDO, "c1", esp=4))
for i, (t, x_, tempo) in enumerate(eixos):
    x = i * 334
    p.append(caixa(x, 200, 310, 180, OXID if i < 4 else FOSF, CARTAO, esp=3))
    rs.append(rot(x + 16, 216, t, w=278, tam=28, cor=TINTA, peso=700))
    rs.append(rot(x + 16, 262, x_, w=278, tam=24, cor=APOIO2))
    rs.append(rot(x + 16, 330, tempo, w=278, tam=24, cor=OXID if i < 4 else FOSF, peso=700))
p.append("</svg>")
rs.append(rot(960, 50, "sinais periféricos: dias", w=700, tam=26, cor=MUDO, peso=600))
S.append({"id": "cadeia", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mecanismo", "titulo": "Uma cadeia, relógios diferentes",
          "destaque": "A pessoa se sente bem por semanas enquanto os eixos cedem. Quando o sintoma chega, a conta está negativa há meses.",
          "destaque_cor": "verm", "fonte": "Esquema de mecanismo, sem valores medidos"})

# 8. o alarme
S.append({"id": "alarme", "tipo": "duas", "eyebrow": "Areta, Taylor e Koehler, 2021", "titulo": "Mesma fisiologia, alarmes diferentes",
          "esq": {"t": "Mulher", "cor": "petr",
                  "itens": ["um sinal vital que apita todo mês: o ciclo", "da fase lútea curta à amenorreia",
                            "foi onde a literatura nasceu, porque era visível"]},
          "dir": {"t": "Homem", "cor": "ambar",
                  "itens": ["nenhum alarme equivalente", "desempenho, fadiga, libido, infecções",
                            "e uma testosterona que cai, com LH baixo"]},
          "destaque": "Homem jovem e ativo com testosterona baixa: calcule a disponibilidade antes de discutir reposição. E balança parada pode ser economia.",
          "destaque_cor": "verm", "fonte": "European Journal of Applied Physiology 2021 · consenso do COI 2023"})

# 9. portas
S.append({"id": "portas", "tipo": "cards", "por_linha": 3, "eyebrow": "Por onde a conta estoura", "titulo": "Cinco portas, e só uma é procurada",
          "cards": [{"t": "1 · Restrição por desempenho ou estética", "x": "categoria de peso, esporte estético: a que a gente reconhece", "cor": "verm"},
                    {"t": "2 · Emagrecer com orientação legítima", "x": "dieta e treino somados; com remédio, comer vira tarefa", "cor": "ambar"},
                    {"t": "3 · O gasto subiu e o prato não", "x": "ninguém restringiu nada: a conta do segundo slide", "cor": "ambar"},
                    {"t": "4 · Insuficiente sem intenção", "x": "tempo, dinheiro, logística, crescimento", "cor": "ambar"},
                    {"t": "5 · Desorganização", "x": "o total até fecha; a comida nunca está na hora certa", "cor": "ambar"}],
          "destaque": "Identificar a porta é metade da conduta.", "destaque_cor": "tinta"})

# 10. controvérsia
S.append({"id": "controversia", "tipo": "duas", "eyebrow": "Jeukendrup, Areta e colaboradores, 2024", "titulo": "A síndrome existe?",
          "esq": {"t": "A crítica", "cor": "ambar",
                  "itens": ["a causa é quase impossível de medir fora do laboratório", "o diagnóstico vira lista de sintomas",
                            "sintomas genéricos, causas múltiplas: carga alostática"]},
          "dir": {"t": "A zona de acordo", "cor": "petr",
                  "itens": ["os efeitos endócrinos e metabólicos são reais", "existe na prática e é modificável",
                            "a disputa é o rótulo de síndrome e o diagnóstico por lista"]},
          "destaque": "Contribuinte principal e modificável, não explicação única. Encontrou? Corrija, e não pare a investigação.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2024; resposta dos autores do consenso e réplica em 2025"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que se faz na segunda-feira", "titulo": "Quanto, por quanto tempo, e com que consequência",
          "regras": ["Perguntar: o que mudou no treino e no prato em 12 meses; peso, sono, libido e ciclo",
                     "Restaurar energia no entorno do treino; reduzir volume por um tempo se preciso",
                     "REFUEL: 20 a 40% a mais por 12 meses, duas vezes mais chance de menstruar, +2,6 kg em média"],
          "cards": [{"t": "Nutricionista", "x": "O plano alimentar."},
                    {"t": "Médico", "x": "Exames, diferencial e medicação."},
                    {"t": "Educador, preparador e psicólogo", "x": "Volume do treino e componente comportamental."}],
          "quem": "As cinco perguntas são de todo mundo."})

spec = {"arquivo": "aulas/MOD04/04-01-disponibilidade-energetica.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Disponibilidade energética", "subtitulo": "Conceito, limiares e controvérsias",
        "nota_capa": "Entra pelo número: trinta.",
        "secoes": {"numero": ["A equação e a origem do trinta.", "capa"],
                   "medida": ["Medida, tempo e mecanismo.", "medida"],
                   "pratica": ["Portas, controvérsia e conduta.", "portas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-01.json"), "w"), ensure_ascii=False, indent=1)
print("04-01.json:", len(S), "slides")
