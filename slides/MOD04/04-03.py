"""Spec do deck 4.3. Gera 04-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

# 1. identidade
S.append({"id": "identidade", "tipo": "frase", "fundo": "tinta", "eyebrow": "O erro é de eixo",
          "frase": "A dose foi prescrita pela identidade, e não pela demanda.",
          "apoio": "“Eu sou corredor.” O carboidrato é o único macronutriente com opinião moral, e a pergunta clínica (quanto, quando, para qual sessão) vira “a favor ou contra?”."})

# 2. a conta
S.append({"id": "demais", "tipo": "numeros", "eyebrow": "Primeiro erro · demais para a demanda", "titulo": "Oito gramas por quilo, quatro horas por semana",
          "numeros": [{"n": "624 g", "x": "de carboidrato por dia: 78 kg × 8 g/kg", "cor": "ambar"},
                      {"n": "≈ 2.500", "x": "kcal só de carboidrato, antes de proteína e gordura", "cor": "ambar"},
                      {"n": "≈ 4 h", "x": "de treino por semana: menos de 40 minutos por dia", "cor": "tinta"}],
          "destaque": "Não há mistério metabólico. É a dieta de quem treina em alto volume, com quatro horas por semana.",
          "destaque_cor": "tinta"})

# 3. as faixas
p = [svg_abre(1664, 400, "Faixas de carboidrato por dia conforme horas e intensidade: leve 3 a 5 g/kg; moderado 5 a 7; resistência 6 a 10; extremo 8 a 12; a conta de 8 g/kg cai na faixa extrema, embora o treino seja da faixa leve a moderada")]
x0, W = 420, 1200
fx = lambda v: x0 + v / 12 * W
faixas = [("leve ou de habilidade", 3, 5, OXID, OXID_T), ("cerca de 1 h por dia", 5, 7, AZUL, AZUL_T),
          ("1 a 3 h por dia", 6, 10, GLIC, GLIC_T), ("4 a 5 h por dia ou mais", 8, 12, FOSF, FOSF_T)]
rs = []
for i, (n, a, b, c, f) in enumerate(faixas):
    y = 20 + i * 80
    p.append(f'<rect x="{fx(a):.0f}" y="{y}" width="{fx(b)-fx(a):.0f}" height="56" rx="8" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(0, y + 12, n, w=400, tam=26, cor=TINTA, peso=600, alinha="right"))
    rs.append(rot(fx(a) + 14, y + 12, f"{a} a {b}", w=fx(b) - fx(a) - 20, tam=26, cor=c, peso=700))
p.append(f'<line x1="{fx(8):.0f}" y1="10" x2="{fx(8):.0f}" y2="340" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{x0}" y1="340" x2="{fx(12):.0f}" y2="340" stroke="{MUDO}" stroke-width="2"/>')
for v in [0, 3, 6, 12]:
    rs.append(rot(fx(v) - 40, 350, f"{v}", w=80, tam=24, cor=MUDO, alinha="center"))
p.append("</svg>")
rs.append(rot(fx(8) + 12, 26, "a conta: 8 g/kg", w=300, tam=24, cor=TINTA, peso=700))
S.append({"id": "faixas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Thomas, Erdman e Burke, 2016", "titulo": "O eixo é hora e intensidade, não modalidade",
          "destaque": "Conte as horas reais de treino, as que aconteceram. É a pergunta mais barata da aula, e desfaz metade dos casos.",
          "destaque_cor": "petr", "fonte": "Gramas por kg por dia · posicionamento da Academia de Nutrição e Dietética, Dietistas do Canadá e ACSM"})

# 4. durante
p = [svg_abre(1664, 330, "Carboidrato durante o exercício por duração: até 30 minutos, nada; 30 a 75 minutos, bochecho ou pouco; 1 a 2 h, até 30 g/h; 2 a 3 h, até 60 g/h; acima de 2,5 h, até 90 g/h com carboidratos combinados")]
seg = [("até 30 min", "nada", CLARO, MUDO), ("30 a 75 min", "bochecho ou pouco", AZUL_T, AZUL),
       ("1 a 2 h", "até 30 g/h", OXID_T, OXID), ("2 a 3 h", "até 60 g/h", GLIC_T, GLIC), ("> 2,5 h", "até 90 g/h, combinados", FOSF_T, FOSF)]
rs = []
for i, (d, g, f, c) in enumerate(seg):
    x = i * 334
    p.append(f'<rect x="{x}" y="40" width="318" height="{80 + i*50}" rx="10" fill="{f}" stroke="{c}" stroke-width="3" transform="translate(0,{200 - i*50})"/>')
    rs.append(rot(x, 0, d, w=318, tam=28, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x + 10, 260 - i * 50, g, w=298, tam=26, cor=c if c != MUDO else TINTA, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "durante", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Jeukendrup, 2014 · o durante", "titulo": "Organizado por duração, não por esporte",
          "destaque": "Antes: 1 a 4 g/kg de 1 a 4 h antes. Depois: 1 a 1,2 g/kg/h só se a próxima sessão vem em menos de 8 h. Se é amanhã, o jantar resolve.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2014 · Medicine and Science in Sports and Exercise 2016"})

# 5. marchadores
S.append({"id": "marchadores", "tipo": "lista", "eyebrow": "Segundo erro · de menos para a intensidade", "titulo": "Os marchadores de elite",
          "itens": [{"t": "A oxidação de gordura subiu muito", "x": "a adaptação é real e mensurável", "cor": "petr"},
                    {"t": "A economia piorou", "x": "mais oxigênio para a mesma velocidade", "cor": "verm"},
                    {"t": "O ganho do bloco de treino não veio", "x": "os outros grupos melhoraram; o cetogênico, não", "cor": "verm"},
                    {"t": "E o resultado se repetiu", "x": "em 2020, com mais atletas e incluindo mulheres", "cor": "ambar"}],
          "destaque": "Gordura custa mais oxigênio por ATP. No leve, quase não importa. Na intensidade alta, importa muito.",
          "destaque_cor": "tinta", "fonte": "Burke e colaboradores, Journal of Physiology 2017 · PLoS One 2020"})

# 6. para quem
S.append({"id": "paraquem", "tipo": "duas", "eyebrow": "Baixo carboidrato", "titulo": "Para quem, e como conversar",
          "esq": {"t": "Sem prejuízo relevante", "cor": "petr",
                  "itens": ["treino predominantemente leve", "preferência forte, sem competir", "razão clínica"]},
          "dir": {"t": "Provavelmente não", "cor": "verm",
                  "itens": ["quem compete", "alta intensidade frequente", "esporte intermitente, glicolítico por natureza"]},
          "destaque": "Teste de seis semanas: carboidrato só em torno das sessões intensas, desempenho registrado, decisão com os números da pessoa. E cortar carboidrato costuma cortar o total.",
          "destaque_cor": "ambar"})

# 7. glicogênio
t = [i / 10 for i in range(0, 41)]
svg, rs = linhas(1664, 340, "Glicogênio muscular caindo ao longo de quatro horas de pedal sem comer, chegando perto do fim entre a segunda e a terceira hora",
                 [{"nome": "", "cor": GLIC, "pts": [(h, max(100 - 45 * h + 4 * h * h, 6)) for h in t]}],
                 0, 4, 0, 100, [(0, "0 h"), (1, "1 h"), (2, "2 h"), (3, "3 h"), (4, "4 h")], [], margem=(40, 20, 60, 20),
                 extra=lambda fx, fy: f'<rect x="{fx(2):.0f}" y="{fy(100):.0f}" width="{fx(3)-fx(2):.0f}" height="{fy(0)-fy(100):.0f}" fill="{FOSF_T}"/>')
rs += [rot(200, 130, "glicogênio muscular", w=400, tam=28, cor=GLIC, peso=700),
       rot(740, 40, "o sintoma tem horário marcado", w=460, tam=28, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "nada", "tipo": "diagrama", "h": 340, "svg": svg, "rotulos": rs,
          "eyebrow": "Terceiro erro · nada para a duração", "titulo": "Não é condicionamento. É aritmética",
          "destaque": "Passou de 75 minutos: comece a comer na primeira hora, por relógio e não por fome. E treine o intestino nos treinos.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos"})

# 8. comida de verdade
S.append({"id": "comida", "tipo": "duas", "eyebrow": "Uma pós feita para o Brasil", "titulo": "Nada disso exige gel",
          "esq": {"t": "Comida de verdade", "cor": "petr",
                  "itens": ["banana média: cerca de 25 g", "pão francês com geleia: mais de 30 g", "tapioca com mel, bolacha de água e sal",
                            "doce de banana, rapadura, tâmaras, água de coco"]},
          "dir": {"t": "O gel", "cor": "ambar",
                  "itens": ["compacto, não amassa, rótulo com a quantidade", "conveniência, não requisito fisiológico",
                            "custa muitas vezes uma banana"]},
          "destaque": "Para quem pedala quatro horas toda semana, o custo decide se a estratégia é seguida. Estratégia abandonada tem eficácia zero.",
          "destaque_cor": "tinta"})

# 9. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Três erros com o mesmo nutriente", "titulo": "Quanto tempo, que intensidade, quando é a próxima sessão",
          "regras": ["Demais para a demanda: conte as horas reais de treino",
                     "De menos para a intensidade: teste de seis semanas em torno das sessões intensas",
                     "Nada para a duração: comer por relógio a partir da primeira hora"],
          "cards": [{"t": "Nutricionista", "x": "Gramas por quilo e plano alimentar."},
                    {"t": "Educador e preparador físico", "x": "As horas e a intensidade reais."},
                    {"t": "Toda a equipe", "x": "O sintoma de horário marcado."}],
          "quem": "A queda em alta intensidade de quem corta carboidrato tem explicação. Não é falta de vontade."})

spec = {"arquivo": "aulas/MOD04/04-03-carboidrato-quanto-quando-e-por-que.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Carboidrato no exercício", "subtitulo": "Dose, momento e erros de prescrição",
        "nota_capa": "Entra pelo erro de eixo: identidade no lugar de demanda.",
        "secoes": {"demais": ["Demais para a demanda, e as faixas.", "capa"],
                   "quando": ["O quando, e o erro espelhado.", "durante"],
                   "duracao": ["Nada para a duração, e comida de verdade.", "nada"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-03.json"), "w"), ensure_ascii=False, indent=1)
print("04-03.json:", len(S), "slides")
