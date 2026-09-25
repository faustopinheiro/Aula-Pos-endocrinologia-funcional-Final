"""Spec do deck 4.2. Gera 04-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a conta
S.append({"id": "conta", "tipo": "numeros", "eyebrow": "Caso ilustrativo", "titulo": "“Eu como muito bem”",
          "numeros": [{"n": "2.400", "x": "kcal por dia no registro de sete dias", "cor": "tinta"},
                      {"n": "− 700", "x": "kcal do exercício: 90 minutos, seis dias por semana", "cor": "ambar"},
                      {"n": "÷ 45", "x": "kg de massa livre de gordura: 58 kg com 22% de gordura", "cor": "tinta"}],
          "destaque": "Resultado: cerca de 38. Triatleta amadora, 31 anos, encaminhada depois da terceira lesão em um ano.",
          "destaque_cor": "petr"})

# 2. zona cinza
p = [svg_abre(1664, 260, "Régua de disponibilidade energética de 0 a 60: abaixo de 30, zona de efeitos endócrinos; de 30 a 45, zona cinza; acima de 45, equilíbrio; o ponto 38 cai na zona cinza")]
x0, W = 0, 1664
fx = lambda v: x0 + v / 60 * W
faixas = [(0, 30, FOSF_T, FOSF), (30, 45, "#E4E1D9", MUDO), (45, 60, OXID_T, OXID)]
for a, b, f, c in faixas:
    p.append(f'<rect x="{fx(a):.0f}" y="60" width="{fx(b)-fx(a):.0f}" height="90" fill="{f}" stroke="{c}" stroke-width="2"/>')
p.append(f'<circle cx="{fx(38):.0f}" cy="105" r="22" fill="{TINTA}"/>')
p.append("</svg>")
rs = [rot(fx(0) + 20, 88, "abaixo de 30", w=600, tam=28, cor=FOSF, peso=700),
      rot(fx(30), 10, "zona cinza", w=fx(45) - fx(30), tam=28, cor=MUDO, peso=700, alinha="center"),
      rot(fx(45) + 20, 88, "perto de 45", w=360, tam=28, cor=OXID, peso=700),
      rot(fx(38) - 60, 168, "38", w=120, tam=40, cor=TINTA, peso=700, alinha="center"),
      rot(fx(30) - 60, 168, "30", w=120, tam=26, cor=MUDO, alinha="center"),
      rot(fx(45) - 60, 168, "45", w=120, tam=26, cor=MUDO, alinha="center")]
S.append({"id": "zona", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Entre 30 e 45", "titulo": "A zona que não dispara alarme",
          "destaque": "Sem amenorreia franca, sem magreza chamativa, sem transtorno evidente. Três lesões em um ano.",
          "destaque_cor": "verm", "fonte": "Faixas como ordem de grandeza, em kcal por kg de massa livre de gordura por dia"})

# 3. ingestão
S.append({"id": "ingestao", "tipo": "lista", "eyebrow": "Passo um", "titulo": "A ingestão",
          "itens": [{"t": "Registro de 3 a 7 dias", "x": "com pelo menos um dia de fim de semana", "cor": "petr"},
                    {"t": "Ou recordatórios de 24 h repetidos", "x": "em dias diferentes, com foto das refeições", "cor": "petr"},
                    {"t": "O erro tem direção: para baixo", "x": "esquecimento, porção, o azeite, o que se come em pé", "cor": "ambar"},
                    {"t": "E não é aleatório", "x": "quem se preocupa com o corpo subnotifica mais", "cor": "verm"}],
          "gap_itens": 22})

# 4. gasto
S.append({"id": "gasto", "tipo": "duas", "eyebrow": "Passo dois", "titulo": "O gasto do exercício, descontado o repouso",
          "esq": {"t": "A conta certa", "cor": "petr",
                  "itens": ["(MET − 1) × peso × horas", "o “menos um” é o repouso que já seria gasto",
                            "em 90 minutos por dia, perto de 100 kcal de diferença"]},
          "dir": {"t": "Os instrumentos", "cor": "ambar",
                  "itens": ["relógios e aplicativos tendem a superestimar", "exceção: medidor de potência no ciclismo",
                            "kJ de trabalho ≈ kcal gastas"]},
          "destaque": "Eficiência do pedal de 20 a 25% e 1 kcal ≈ 4 kJ: por isso os quilojoules do medidor aproximam as quilocalorias.",
          "destaque_cor": "tinta"})

# 5. massa magra
S.append({"id": "massa", "tipo": "frase", "fundo": "petr", "eyebrow": "Passo três · o denominador",
          "frase": "Sempre o mesmo método.",
          "apoio": "Bioimpedância, dobras e densitometria dão números diferentes para a mesma pessoa. Sem nenhum, estime um percentual razoável e assuma que o erro existe."})

# 6. sensibilidade
S.append({"id": "erro", "tipo": "tabela", "eyebrow": "Passo quatro · propagar o erro", "titulo": "A mesma mulher, números diferentes",
          "cab": ["Cenário", "Ingestão", "Exercício", "Massa magra", "Resultado"],
          "larguras": [34, 16, 16, 18, 16],
          "linhas": [["Conta revisada", "2.400", "700", "45 kg", "≈ 38"],
                     ["Registro −20%, relógio +30%", "1.920", "910", "45 kg", "≈ 22"],
                     ["Método marca 28% de gordura", "2.400", "700", "≈ 42 kg", "≈ 41"],
                     ["Método marca 18% de gordura", "2.400", "700", "≈ 47,5 kg", "≈ 36"]],
          "destaque": "Número muito baixo pode ser artefato. Número na casa dos 40 não tranquiliza quem tem três lesões. A conta gera hipótese.",
          "destaque_cor": "verm", "fonte": "Suposições de erro para o cálculo; direção do erro conforme Burke e colaboradores, 2018"})

# 7. quando não dá para calcular
S.append({"id": "semconta", "tipo": "duas", "eyebrow": "Passo cinco · quando a conta não sai", "titulo": "Os caminhos mais baratos",
          "esq": {"t": "As cinco perguntas", "cor": "petr",
                  "itens": ["o treino subiu e o prato não mudou?", "então a conta está negativa até prova em contrário",
                            "sem calculadora"]},
          "dir": {"t": "LEAF-Q · Melin, 2014", "cor": "ambar",
                  "itens": ["25 itens: lesão, intestino, função reprodutiva", "corte em 8; sensibilidade 78%, especificidade 90%",
                            "homens: LEAM-Q, em validação"]},
          "destaque": "Questionário rastreia. Itens se confundem com treino pesado, e falso positivo é esperado.",
          "destaque_cor": "tinta", "fonte": "British Journal of Sports Medicine 2014 · 84 atletas"})

# 8. razão do metabolismo e CAT2
p = [svg_abre(1664, 360, "Na mesma amostra de 49 atletas, a proporção classificada como suprimida variou de 35% a 94% conforme a equação; abaixo, a ferramenta do COI em quatro cores")]
fx = lambda v: v / 100 * 1664
p.append(f'<rect x="0" y="40" width="1664" height="56" rx="8" fill="{CLARO}" stroke="{BORDA}" stroke-width="2"/>')
p.append(f'<rect x="{fx(35):.0f}" y="40" width="{fx(94)-fx(35):.0f}" height="56" rx="8" fill="{GLIC}"/>')
cores = [("verde", OXID, OXID_T), ("amarelo", GLIC, GLIC_T), ("laranja", "#C0632A", "#F6E2D3"), ("vermelho", FOSF, FOSF_T)]
rs = [rot(fx(35) + 16, 50, "35%", w=200, tam=30, cor="#FFFFFF", peso=700, alinha="left"),
      rot(fx(94) - 236, 50, "94%", w=200, tam=30, cor="#FFFFFF", peso=700, alinha="right"),
      rot(0, 108, "“suprimidos” na mesma amostra, conforme a equação escolhida", w=1664, tam=26, cor=TINTA, peso=600, alinha="center")]
for i, (n, c, f) in enumerate(cores):
    x = i * 416
    p.append(f'<rect x="{x + 8}" y="220" width="400" height="110" rx="12" fill="{f}" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(x + 8, 256, n, w=400, tam=32, cor=c if n != "amarelo" else "#8A5F12", peso=700, alinha="center"))
rs.append(rot(0, 172, "Ferramenta do COI, 2023: rastreio, estratificação e diagnóstico médico", w=1664, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
S.append({"id": "caros", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os caminhos mais caros", "titulo": "Razão do metabolismo de repouso e ferramenta do COI",
          "destaque": "Abaixo de 0,90 sugere supressão, mas depende da equação e, em 2025, não se associou à disponibilidade calculada.",
          "destaque_cor": "ambar", "fonte": "Applied Physiology, Nutrition, and Metabolism 2025, 49 atletas · British Journal of Sports Medicine 2023, REDs CAT2"})

# 9. o lanche
S.append({"id": "lanche", "tipo": "numeros", "eyebrow": "Passo seis · o que fazer com o número", "titulo": "Acrescentar comida, não tirar treino",
          "numeros": [{"n": "38 → 45", "x": "sete pontos de disponibilidade", "cor": "tinta"},
                      {"n": "× 45 kg", "x": "de massa livre de gordura", "cor": "tinta"},
                      {"n": "≈ 315", "x": "kcal por dia: um lanche real, perto do treino", "cor": "petr"}],
          "destaque": "“O treino não é demais; a comida é pouca para o treino que você faz.” O mesmo desequilíbrio, dito pelo lado que preserva a identidade.",
          "destaque_cor": "tinta"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Duas regras de segurança", "titulo": "A conta é instrumento, não sentença",
          "regras": ["Suspeita de transtorno alimentar: a conta é para você, não para ela",
                     "Monitorar o desfecho, não o número: ciclo, lesão, desempenho, sono",
                     "Número baixo sozinho pode ser artefato; número confortável não tranquiliza"],
          "cards": [{"t": "Nutricionista", "x": "A ingestão detalhada e o plano."},
                    {"t": "Educador e preparador físico", "x": "O gasto real do que a pessoa faz."},
                    {"t": "Médico", "x": "O diagnóstico quando há deficiência clínica."}],
          "quem": "Encaminhar com a ordem de grandeza já calculada encurta o trabalho de todos."})

spec = {"arquivo": "aulas/MOD04/04-02-como-calcular-disponibilidade-energetica.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Estimativa da disponibilidade energética", "subtitulo": "Métodos, erros de medida e alternativas clínicas",
        "nota_capa": "Entra pelo caso ilustrativo e pela conta.",
        "secoes": {"caso": ["A conta e a zona cinza.", "capa"],
                   "oficina": ["As três variáveis e o erro propagado.", "ingestao"],
                   "alternativas": ["Quando não dá para calcular, e o que fazer.", "semconta"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-02.json"), "w"), ensure_ascii=False, indent=1)
print("04-02.json:", len(S), "slides")
