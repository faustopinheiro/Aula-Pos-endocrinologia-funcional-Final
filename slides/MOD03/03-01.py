"""Spec do deck 3.1. Gera 03-01.json ao lado deste arquivo."""
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

# 1. quatro laudos
S.append({"id": "laudos", "tipo": "cards", "eyebrow": "Quatro exames", "titulo": "O mesmo número, duas leituras opostas",
          "cards": [{"t": "Testosterona baixa", "x": "42 anos, musculação cinco vezes por semana", "cor": "verm"},
                    {"t": "TSH alterado", "x": "corredora em restrição há meses", "cor": "ambar"},
                    {"t": "Cortisol fora da faixa", "x": "plantonista", "cor": "petr"},
                    {"t": "IGF-1 baixo", "x": "nadador master que quer recuperar melhor", "cor": "tinta"}],
          "destaque": "Disfunção do eixo, ou eixo funcionando certo diante do contexto que a pessoa criou?",
          "destaque_cor": "verm"})

# 2. três andares
p = [svg_abre(1664, 470, "Entradas de energia, sono, emoção, temperatura, infecção e luz chegam ao hipotálamo, que comanda a hipófise, que comanda a glândula, que age no tecido; o hormônio final volta ao topo como feedback negativo"),
     "<defs>" + seta_marker("a1", TINTA) + seta_marker("a2", FOSF) + seta_marker("a3", MUDO) + "</defs>"]
andares = [("Hipotálamo", 20, AZUL), ("Hipófise", 140, AZUL), ("Glândula periférica", 260, OXID), ("Tecido", 380, GLIC)]
for nome, y, cor in andares:
    p.append(caixa(560, y, 520, 76, cor, CARTAO, esp=4))
for y in (96, 216, 336):
    p.append(seta(820, y + 4, 820, y + 36, TINTA, "a1", esp=5))
for k in range(6):
    yy = 8 + k * 16
    p.append(seta(420, 58 + (k - 2.5) * 22, 548, 58, MUDO, "a3", esp=3))
p.append(f'<path d="M1080 298 C 1300 298, 1300 58, 1092 58" fill="none" stroke="{FOSF}" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#a2)"/>')
p.append("</svg>")
rs = [rot(560, 38, "Hipotálamo", w=520, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(560, 158, "Hipófise", w=520, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(560, 278, "Glândula periférica", w=520, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(560, 398, "Tecido", w=520, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 0, "energia · sono · emoção", w=400, tam=26, cor=TINTA, alinha="right"),
      rot(0, 40, "temperatura · infecção · luz", w=400, tam=26, cor=TINTA, alinha="right"),
      rot(0, 80, "e o treino, como mais uma", w=400, tam=26, cor=MUDO, alinha="right"),
      rot(1300, 150, "feedback negativo: o hormônio final avisa o começo da linha", w=360, tam=26, cor=FOSF, peso=600)]
S.append({"id": "andares", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A arquitetura", "titulo": "Três andares e uma alça",
          "destaque": "Três andares permitem integração: o hipotálamo soma tudo o que recebe e decide uma vez.",
          "destaque_cor": "petr"})

# 3. o par
p = [svg_abre(1664, 400, "Três colunas com o hormônio final baixo. Primário: sinal da hipófise alto. Central: sinal baixo. Funcional: sinal baixo ou normal")]
cols = [("Primário", FOSF, 250), ("Central", AZUL, 60), ("Funcional", OXID, 110)]
rs = []
for i, (nome, cor, sinal) in enumerate(cols):
    x0 = i * 570
    p.append(f'<rect x="{x0}" y="0" width="520" height="400" rx="18" fill="{CLARO}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<line x1="{x0+60}" y1="330" x2="{x0+460}" y2="330" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<rect x="{x0+100}" y="{330-sinal}" width="120" height="{sinal}" rx="4" fill="{cor}"/>')
    p.append(f'<rect x="{x0+300}" y="{330-60}" width="120" height="60" rx="4" fill="{MUDO}"/>')
    rs += [rot(x0, 16, nome, w=520, tam=32, cor=cor, peso=700, alinha="center"),
           rot(x0 + 60, 340, "sinal de cima", w=200, tam=24, cor=TINTA, alinha="center"),
           rot(x0 + 260, 340, "hormônio final", w=200, tam=24, cor=TINTA, alinha="center")]
p.append("</svg>")
S.append({"id": "par", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo um", "titulo": "Dose o par, não o hormônio",
          "destaque": "Final baixo com sinal alto: o comando foi dado e não foi cumprido. Final baixo com sinal baixo ou normal: por que o centro decidiu não pedir?",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# 4. qual é o par
S.append({"id": "pares", "tipo": "tabela", "eyebrow": "O que pedir", "titulo": "O par em cada eixo",
          "cab": ["Eixo", "Hormônio final", "Sinal de cima", "Aponta para a glândula quando"],
          "larguras": [22, 22, 26, 30],
          "linhas": [["Gonadal masculino", "Testosterona total", "LH e FSH", "LH alto"],
                     ["Gonadal feminino", "Estradiol", "LH e FSH, e como está o ciclo", "FSH alto"],
                     ["Tireoidiano", "T4 livre", "TSH", "TSH alto"],
                     ["Adrenal", "Cortisol, com horário", "ACTH", "ACTH alto"]],
          "destaque": "Se o TSH não está alto, a fadiga não é hipotireoidismo primário. O TSH rastreia bem, e não fecha a história em quem está em restrição.",
          "destaque_cor": "ambar"})

# 5. pulsos
pts = []
for m in range(0, 1441, 4):
    v = 8
    for c, amp in ((60, 70), (180, 70), (300, 70), (420, 70), (650, 28), (950, 28), (1250, 28)):
        v += amp * math.exp(-((m - c) / 18) ** 2)
    pts.append((m, v))
def marca_igf(fx, fy):
    return (f'<line x1="{fx(0):.0f}" y1="{fy(30):.0f}" x2="{fx(1440):.0f}" y2="{fy(30):.0f}" stroke="{OXID}" stroke-width="6"/>'
            f'<line x1="1180" y1="22" x2="1240" y2="22" stroke="{OXID}" stroke-width="6"/>'
            f'<circle cx="{fx(300):.0f}" cy="{fy(78):.0f}" r="14" fill="{FOSF}" stroke="#F7F6F2" stroke-width="3"/>'
            f'<circle cx="{fx(800):.0f}" cy="{fy(8):.0f}" r="14" fill="{FOSF}" stroke="#F7F6F2" stroke-width="3"/>')
svg, rs = linhas(1664, 400, "Liberação de GH em pulsos ao longo de 24 horas, maiores durante o sono; uma coleta num pico e outra num vale dão valores muito diferentes; o IGF-1 corre como uma linha estável que integra a média",
                 [{"nome": "", "cor": AZUL, "pts": pts, "esp": 5}], 0, 1440, 0, 90, [], [],
                 margem=(20, 60, 70, 20), extra=marca_igf)
rs += [rot(20, 0, "noite: pulsos maiores, no sono profundo", w=640, tam=26, cor=AZUL, peso=700),
       rot(1256, 4, "IGF-1: a média de dias", w=400, tam=26, cor=OXID, peso=700),
       rot(380, 44, "coleta no pico", w=260, tam=26, cor=FOSF, peso=700),
       rot(790, 340, "coleta no vale", w=260, tam=26, cor=FOSF, peso=700, alinha="center"),
       rot(1200, 340, "24 horas", w=440, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "pulsos", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "A exceção, e o corolário", "titulo": "Um resultado isolado é uma amostra de uma onda",
          "destaque": "Valor limítrofe pede repetição, não conduta.", "destaque_cor": "verm",
          "fonte": "Esquema, sem valores medidos"})

# 6. central x funcional
S.append({"id": "anamnese", "tipo": "duas", "eyebrow": "Passo dois", "titulo": "Quem separa central de funcional é a anamnese",
          "esq": {"t": "Supressão funcional", "cor": "petr",
                  "itens": ["restrição energética sustentada, perda de peso", "sono curto crônico",
                            "volume alto com pouca comida", "doença recente, estresse prolongado"]},
          "dir": {"t": "Central verdadeiro", "cor": "verm",
                  "itens": ["cefaleia, alteração visual", "outros eixos alterados fora de proporção",
                            "trauma ou cirurgia na cabeça", "hormônio exógeno, declarado ou não"]},
          "destaque": "Abaixo de 30 kcal por kg de massa magra por dia, em cinco dias, os pulsos de LH ficaram 10 a 32% menos frequentes. O hipotálamo lê a escassez rápido.",
          "destaque_cor": "ambar", "fonte": "Loucks e Thuma, Journal of Clinical Endocrinology and Metabolism 2003 · 29 mulheres jovens com ciclo regular"})

# 7. relógios
esc = ["minutos", "horas", "dias", "semanas", "meses"]
p = [svg_abre(1664, 400, "Régua de tempo de minutos a meses: o cortisol responde em minutos e volta em horas; o comando central de LH muda em dias; testosterona, estradiol e tireoide mudam de patamar em semanas a meses")]
X0, PASSO = 470, 290
for i, t_ in enumerate(esc):
    x = X0 + i * PASSO
    p.append(f'<line x1="{x}" y1="40" x2="{x}" y2="330" stroke="{GRADE}" stroke-width="2"/>')
barras = [("Cortisol", 0, 1.1, FOSF, 60), ("Comando central (pulsos de LH)", 1.7, 2.4, AZUL, 150),
          ("Testosterona, estradiol, tireoide", 2.8, 4.0, OXID, 240)]
rs = [rot(X0 + i * PASSO - 100, 350, t_, w=200, tam=26, cor=MUDO, alinha="center") for i, t_ in enumerate(esc)]
for nome, a, b, cor, y in barras:
    p.append(f'<rect x="{X0 + a*PASSO:.0f}" y="{y}" width="{(b-a)*PASSO:.0f}" height="56" rx="28" fill="{cor}"/>')
    rs.append(rot(0, y + 12, nome, w=440, tam=26, cor=TINTA, peso=600, alinha="right"))
p.append("</svg>")
S.append({"id": "relogios", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O relógio de cada andar", "titulo": "O cortisol conta sobre hoje; a testosterona, sobre os últimos meses",
          "destaque": "Exame normal não prova que está tudo bem. E a clínica às vezes chega antes do laboratório.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos"})

# 8. ficha de coleta
S.append({"id": "ficha", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo três", "titulo": "Registre a condição de coleta",
          "cards": [{"t": "Horário", "x": "testosterona das 15 h não é a das 7 h"},
                    {"t": "Horas desde o último treino", "x": "a manhã seguinte à sessão pesada não é base"},
                    {"t": "Quão duro foi esse treino", "x": "quem sabe é o preparador físico"},
                    {"t": "Fase do ciclo", "x": "quando for o caso"},
                    {"t": "Tempo de jejum", "x": "e o que comeu na véspera"},
                    {"t": "O que mudou em três meses", "x": "peso, sono, carga, trabalho, doença"}],
          "destaque": "Sem a ficha, você compara duas fotos tiradas com luz diferente e atribui a diferença à pessoa.",
          "destaque_cor": "tinta"})

# 9. cinco sistemas
S.append({"id": "cinco", "tipo": "cards", "eyebrow": "Passo quatro", "titulo": "Um eixo sozinho, ou vários na mesma direção?",
          "cards": [{"t": "Cortisol", "x": "mobilização: energia agora", "cor": "verm"},
                    {"t": "Gonadal", "x": "investimento: o primeiro a ser cortado", "cor": "ambar"},
                    {"t": "Tireoidiano", "x": "velocidade: 80% do T3 nasce nos tecidos", "cor": "petr"},
                    {"t": "GH e IGF-1", "x": "reparo, acoplado ao sono profundo", "cor": "tinta"},
                    {"t": "Sinais periféricos", "x": "informação: insulina, leptina, grelina", "cor": "tinta"}],
          "destaque": "Um eixo alterado sozinho: desconfie de doença. Vários levemente deslocados na mesma direção: desconfie de contexto. É uma decisão executada em cinco lugares.",
          "destaque_cor": "petr", "fonte": "Bianco e Kim, Journal of Clinical Investigation 2006"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O procedimento", "titulo": "Procure o hábito antes do hormônio",
          "regras": ["Dose o par", "Separe central de funcional pela anamnese",
                     "Registre a condição de coleta", "Um eixo ou vários?"],
          "cards": [{"t": "Médico", "x": "Solicita e interpreta o exame hormonal e decide sobre reposição."},
                    {"t": "O resto da equipe", "x": "Entrega a virada percebida semana a semana: esforço, ciclo, recuperação."}],
          "quem": "Hipotireoidismo, hipogonadismo, insuficiência adrenal e tumor de hipófise existem. A defesa é de ordem, não de negação."})

spec = {"arquivo": "aulas/MOD03/03-01-arquitetura-dos-eixos-neuroendocrinos.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Organização dos eixos neuroendócrinos", "subtitulo": "Princípios de leitura do perfil hormonal",
        "nota_capa": "Entra pelos quatro exames.",
        "secoes": {"arquitetura": ["Os quatro laudos e os três andares.", "capa"],
                   "par": ["Passo um: o par, e a pulsatilidade.", "par"],
                   "contexto": ["Passo dois e três: anamnese, relógios e condição de coleta.", "anamnese"],
                   "mapa": ["Passo quatro e o fecho.", "cinco"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-01.json"), "w"), ensure_ascii=False, indent=1)
print("03-01.json:", len(S), "slides")
