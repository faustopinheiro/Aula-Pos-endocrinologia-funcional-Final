"""Spec do deck 2.8. Gera 02-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def laudo(p, rs, x0, marcas=False):
    p.append(caixa(x0, 0, 760, 440, BORDA, CARTAO, 2, 10))
    p.append(f'<rect x="{x0+40}" y="200" width="680" height="3" fill="{GRADE}"/>')
    for k in range(4):
        p.append(f'<rect x="{x0+40}" y="{300 + k*30}" width="{680 - k*60}" height="12" rx="4" fill="{GRADE}"/>')
    rs += [rot(x0 + 40, 24, "VO₂máx", w=300, tam=28, cor=MUDO, peso=600),
           rot(x0 + 40, 60, "48,2", w=400, tam=96, cor=TINTA, peso=700, serif=True),
           rot(x0 + 40, 216, "limiar 1 · limiar 2", w=500, tam=24, cor=MUDO),
           rot(x0 + 40, 256, "zonas do programa", w=500, tam=24, cor=MUDO)]

# 1. o laudo na mesa
p, rs = [svg_abre(1664, 440, "Um laudo de ergoespirometria com o VO2máx enorme no topo e, bem menores, as duas linhas de limiar e a tabela de zonas do programa")], []
laudo(p, rs, 0)
p.append("</svg>")
rs += [rot(860, 40, "“E aí, tá bom?”", w=800, tam=56, cor=TINTA, peso=700, serif=True),
       rot(860, 160, "O número grande chama o olho.", w=800, tam=30, cor=TINTA),
       rot(860, 220, "As duas linhas pequenas decidem.", w=800, tam=30, cor=FOSF, peso=700),
       rot(860, 320, "Laudo ilustrativo", w=800, tam=24, cor=MUDO)]
S.append({"id": "laudo", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A cena", "titulo": "Um laudo de ergoespirometria na sua mesa"})

# 2. duas quebras
xs = [x for x in range(0, 101, 2)]
lac = [(x, 1.0 + (0 if x < 45 else 0.03 * (x - 45)) + (0 if x < 72 else 0.004 * (x - 72) ** 2.1)) for x in xs]
def faixas(fx, fy):
    return (f'<rect x="{fx(0):.1f}" y="{fy(0.2):.1f}" width="{fx(45)-fx(0):.1f}" height="{fy(0)-fy(0.2):.1f}" fill="{OXID}"/>'
            f'<rect x="{fx(45):.1f}" y="{fy(0.2):.1f}" width="{fx(72)-fx(45):.1f}" height="{fy(0)-fy(0.2):.1f}" fill="{GLIC}"/>'
            f'<rect x="{fx(72):.1f}" y="{fy(0.2):.1f}" width="{fx(100)-fx(72):.1f}" height="{fy(0)-fy(0.2):.1f}" fill="{FOSF}"/>')
svg, rs = linhas(1664, 420, "Lactato no sangue durante um teste progressivo: quase parado até o primeiro limiar, subindo devagar até o segundo e disparando depois; embaixo, as três faixas moderado, pesado e severo",
    [{"nome": "", "cor": TINTA, "pts": lac, "esp": 5}], 0, 100, 0, 7, [(0, "leve"), (100, "máximo")], [], margem=(40, 20, 60, 30),
    destaques=[{"x": 45, "t": "1º limiar", "w": 220}, {"x": 72, "t": "2º limiar", "w": 220}], extra=faixas)
rs += [rot(120, 250, "moderado", w=400, tam=26, cor=OXID, peso=700), rot(840, 250, "pesado", w=300, tam=26, cor=GLIC, peso=700),
       rot(1290, 250, "severo", w=300, tam=26, cor=FOSF, peso=700), rot(60, 40, "lactato no sangue", w=400, tam=24, cor=MUDO)]
S.append({"id": "quebras", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "O que o teste mede", "titulo": "Duas quebras, três domínios",
          "fonte": "Esquema, sem valores medidos"})

# 3. sustentabilidade
p, rs = [svg_abre(1664, 360, "Em carga constante: no domínio moderado o lactato fica parado perto do repouso; no pesado sobe e estabiliza; no severo sobe sem parar até a exaustão")], []
for i, (nome, cor, f, dur) in enumerate([("Moderado", OXID, lambda t: 1.0 + 0.3 * (1 - math.exp(-t / 3)), "horas"),
                                        ("Pesado", GLIC, lambda t: 1.0 + 2.2 * (1 - math.exp(-t / 5)), "estabiliza"),
                                        ("Severo", FOSF, lambda t: 1.0 + 0.35 * t, "minutos")]):
    x0, w, y0, h = i * 572, 520, 60, 220
    p.append(f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
    pts = " ".join(f"{x0 + t/20*w:.1f},{y0 + h - min(f(t), 8)/8*h:.1f}" for t in [k / 2 for k in range(0, 41)] if f(t) <= 8.2)
    p.append(f'<polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="6"/>')
    rs += [rot(x0, 0, nome, w=w, tam=32, cor=cor, peso=700), rot(x0, y0 + h + 12, "tempo em carga constante →", w=w, tam=24, cor=MUDO, alinha="right"),
           rot(x0 + 20, y0 + 20, dur, w=300, tam=28, cor=TINTA, peso=700, serif=True)]
p.append("</svg>")
S.append({"id": "sustenta", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Três comportamentos, não três dificuldades", "titulo": "O limiar descreve sustentabilidade",
          "fonte": "Esquema, sem valores medidos"})

# 4. os dois limiares
S.append({"id": "limiares", "tipo": "cards", "por_linha": 2, "eyebrow": "Os dois pontos e o que cada um decide", "titulo": "Primeiro e segundo limiar",
          "cards": [{"t": "Primeiro limiar", "x": "A intensidade mais alta ainda confortável por muito tempo. É o teto do treino de verdade leve, e quase ninguém sabe onde fica o seu.", "cor": "petr"},
                    {"t": "Segundo limiar", "x": "Acima dele o lactato para de estabilizar. A intensidade mais alta em estado estável: algo entre 30 e 60 minutos.", "cor": "verm"}],
          "destaque": "Métodos diferentes marcam pontos próximos, não idênticos. Vale uma estimativa razoável, sempre pelo mesmo método, acompanhada no tempo."})

# 5. anaeróbico
p, rs = [svg_abre(1664, 400, "A palavra anaeróbico riscada e três suposições derrubadas: o músculo sem oxigênio, o lactato por falta de oxigênio e uma linha única")], []
p.append(f'<line x1="40" y1="120" x2="660" y2="40" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
for i, (t, s) in enumerate([("O músculo fica sem oxigênio", "Não fica. Continua recebendo e usando."),
                            ("O lactato aparece por falta de oxigênio", "Muda o equilíbrio entre produzir e remover."),
                            ("Existe uma linha única", "Existem várias definições, próximas e não idênticas.")]):
    y = 20 + i * 125
    p.append(caixa(760, y, 904, 105, FOSF, FOSF_T, 3))
    rs += [rot(790, y + 12, t, w=850, tam=28, cor=TINTA, peso=700), rot(790, y + 56, s, w=850, tam=24)]
p.append("</svg>")
rs += [rot(0, 30, "anaeróbico", w=700, tam=96, cor=MUDO, peso=700, serif=True, alinha="center"),
       rot(0, 220, "Este curso usa: primeiro e segundo limiar.", w=700, tam=30, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "nome", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Mais de cinquenta anos de controvérsia", "titulo": "Nome errado produz conduta errada",
          "fonte": "Poole, Rossiter, Brooks e Gladden, Journal of Physiology 2021"})

# 6. a cadeia
p, rs = [svg_abre(1664, 300, "A cadeia de entrega de oxigênio: pulmão, coração, sangue, vaso e mitocôndria; o coração é o elo que limita em pessoa saudável"),
         "<defs>" + seta_marker("c1", MUDO) + "</defs>"], []
elos = [("Pulmão", "capta"), ("Coração", "bombeia"), ("Sangue", "carrega"), ("Vaso", "distribui"), ("Mitocôndria", "consome")]
for i, (t, s) in enumerate(elos):
    x = i * 336
    lim = t == "Coração"
    p.append(caixa(x, 60, 290, 150, FOSF if lim else MUDO, FOSF_T if lim else CARTAO, 6 if lim else 3))
    rs += [rot(x, 90, t, w=290, tam=32, cor=TINTA, peso=700, alinha="center"), rot(x, 140, s, w=290, tam=26, alinha="center")]
    if i < 4:
        p.append(f'<path d="M{x+294} 135 L{x+330} 135" stroke="{MUDO}" stroke-width="4" marker-end="url(#c1)"/>')
p.append("</svg>")
rs.append(rot(336, 230, "o elo que limita, em saudável ao nível do mar", w=290, tam=24, cor=FOSF, peso=700, alinha="center"))
S.append({"id": "cadeia", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número grande do laudo", "titulo": "O VO₂máx depende da cadeia inteira",
          "destaque": "Taxa máxima de captar, transportar e usar oxigênio. Em quem é saudável, limita a entrega: débito cardíaco, com o volume de ejeção na frente."})

# 7. HERITAGE
S.append({"id": "heritage", "tipo": "numeros", "eyebrow": "HERITAGE: sedentários treinados do mesmo jeito", "titulo": "Grandes e pequenos respondedores existem",
          "numeros": [{"n": "481", "x": "sedentários de 98 famílias", "cor": "tinta"},
                      {"n": "20 sem", "x": "do mesmo treino aeróbico", "cor": "ambar"},
                      {"n": "47%", "x": "da variação na resposta do VO₂máx atribuída à família", "cor": "verm"}],
          "destaque": "Não é falta de esforço. Diga isso ao paciente. E lembre: o VO₂máx melhora mais em quem está longe do próprio teto, e é o que menos se move em quem treina há anos.",
          "fonte": "Bouchard e colaboradores, Journal of Applied Physiology 1999"})

# 8. denominador
p, rs = [svg_abre(1664, 360, "Os mesmos 3 litros por minuto de oxigênio dão 37,5 mililitros por quilo por minuto com 80 quilos e 41,7 com 72 quilos"),
         f'<line x1="440" y1="0" x2="440" y2="300" stroke="{MUDO}" stroke-width="2"/>'], []
esc = 26
for i, (v, cor, nome) in enumerate([(37.5, AZUL, "3,0 L/min ÷ 80 kg"), (41.7, OXID, "3,0 L/min ÷ 72 kg")]):
    p.append(f'<rect x="442" y="{30 + i*130}" width="{v*esc:.0f}" height="90" rx="4" fill="{cor}"/>')
    rs += [rot(0, 56 + i * 130, nome, w=410, tam=30, cor=TINTA, peso=700, alinha="right"),
           rot(442 + v * esc - 320, 52 + i * 130, f"{v:.1f}".replace(".", ",") + " mL/kg/min", w=300, tam=32, cor=CLARO, peso=700, alinha="right", serif=True)]
p.append("</svg>")
rs.append(rot(442, 300, "o coração e o músculo são os mesmos nas duas barras", w=1100, tam=26, cor=FOSF, peso=700))
S.append({"id": "denominador", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A armadilha da unidade", "titulo": "Emagreceu, o número subiu, o motor é o mesmo",
          "destaque": "Perder massa magra em restrição sobe o número e piora o resto. E saúde é outra conversa: no sedentário de cinquenta anos, aumentar o motor é o objetivo.",
          "destaque_cor": "ambar"})

# 9. três fatores
p, rs = [svg_abre(1664, 320, "Desempenho é o produto de três fatores: VO2máx, o tamanho do motor; limiar, quanto dele dá para usar; economia, quanto custa cada quilômetro")], []
fat = [("VO₂máx", "o tamanho do motor", AZUL), ("Limiar", "quanto do motor dá para usar", GLIC), ("Economia", "quanto custa cada quilômetro", OXID)]
for i, (t, s, cor) in enumerate(fat):
    x = i * 470
    p.append(f'<rect x="{x}" y="40" width="400" height="200" rx="16" fill="{cor}"/>')
    rs += [rot(x, 80, t, w=400, tam=44, cor=CLARO, peso=700, alinha="center", serif=True), rot(x + 20, 150, s, w=360, tam=26, cor=CLARO, alinha="center")]
    if i < 2:
        rs.append(rot(x + 400, 100, "×", w=70, tam=56, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
rs += [rot(1400, 100, "=", w=60, tam=56, cor=TINTA, peso=700, alinha="center"),
       rot(1460, 96, "desempenho", w=204, tam=32, cor=TINTA, peso=700, serif=True),
       rot(940, 260, "a que o laudo não traz em destaque", w=400, tam=24, cor=OXID, peso=700, alinha="center")]
S.append({"id": "fatores", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Mesmo VO₂máx, 40 e 46 minutos nos 10 km", "titulo": "Três fatores, não um",
          "fonte": "Joyner e Coyle, Journal of Physiology 2008"})

# 10. economia
p, rs = [svg_abre(1664, 400, "Dois corredores na mesma velocidade: um consome menos oxigênio que o outro; o que determina a economia: técnica, tendão, distribuição de massa, anos de prática e treino de força")], []
for i, (v, cor, nome) in enumerate([(100, FOSF, "Corredor A"), (88, OXID, "Corredor B")]):
    p.append(f'<rect x="240" y="{40 + i*120}" width="{v*5}" height="80" rx="4" fill="{cor}"/>')
    rs.append(rot(0, 62 + i * 120, nome, w=220, tam=28, cor=TINTA, peso=700, alinha="right"))
rs += [rot(240, 280, "oxigênio gasto na mesma velocidade · ilustrativo", w=560, tam=24, cor=MUDO)]
for i, (t, cor) in enumerate([("Técnica e cadência", MUDO), ("Rigidez do tendão", MUDO), ("Distribuição de massa", MUDO), ("Anos de prática", MUDO), ("Treino de força", FOSF)]):
    y = 10 + i * 76
    p.append(caixa(900, y, 764, 62, cor, FOSF_T if cor == FOSF else CARTAO, 3 if cor == FOSF else 2))
    rs.append(rot(930, y + 14, t, w=700, tam=28, cor=TINTA, peso=700))
p.append("</svg>")
S.append({"id": "economia", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A variável que o laudo não traz", "titulo": "Economia: quanto custa a mesma velocidade",
          "destaque": "Força de 8 a 12 semanas melhorou a economia de corredores de alto nível de forma clara. Sem precisar mexer no VO₂máx.", "destaque_cor": "verm",
          "fonte": "Balsalobre-Fernández e colaboradores, Journal of Strength and Conditioning Research 2016"})

# 11. caso ilustrativo
tempo = [(m, 47 if m < 36 else 47 - 2.3 * (1 - math.exp(-(m - 36) / 3))) for m in range(0, 45)]
vo2 = [(m, 47.5) for m in range(0, 45)]
def troca(fx, fy):
    return f'<rect x="{fx(36):.1f}" y="{fy(48.5):.1f}" width="{fx(44)-fx(36):.1f}" height="{fy(43.5)-fy(48.5):.1f}" fill="{OXID}" fill-opacity="0.12"/>'
svg, rs = linhas(1664, 380, "Caso ilustrativo: um corredor parado em 47 minutos nos 10 km por três anos troca um tiro por duas sessões de força; o tempo cai para menos de 45 minutos e o VO2máx estimado fica igual",
    [{"nome": "", "cor": TINTA, "pts": tempo, "esp": 5}], 0, 44, 43.5, 48.5, [(0, "3 anos atrás"), (36, "troca"), (44, "8 meses depois")],
    [44, 45, 46, 47, 48], yfmt=lambda v: f"{v:g} min", margem=(120, 20, 60, 30), extra=troca)
rs += [rot(200, 30, "tempo nos 10 km: parado em 47 minutos", w=700, tam=26, cor=TINTA, peso=700),
       rot(1160, 250, "menos de 45 min", w=380, tam=30, cor=OXID, peso=700, serif=True),
       rot(1140, 30, "1 tiro → 2 sessões de força", w=500, tam=24, cor=OXID, peso=700)]
S.append({"id": "caso", "tipo": "diagrama", "h": 380, "svg": svg, "rotulos": rs,
          "eyebrow": "Um caso ilustrativo, para fixar", "titulo": "O motor é o mesmo. Mudou o gasto.",
          "destaque": "O VO₂máx estimado ficou praticamente igual. Economia é a variável que envelhece melhor. E não refaça a técnica de quem está bem: cadência é a alavanca segura.",
          "fonte": "Caso ilustrativo, sem dados reais"})

# 12. sete passos
p, rs = [svg_abre(1664, 440, "O laudo com sete marcações na ordem de leitura; o VO2máx do topo é só o passo dois")], []
laudo(p, rs, 0)
marks = [(640, 30, "1"), (560, 100, "2"), (560, 216, "3"), (560, 256, "4"), (700, 300, "5"), (700, 360, "6"), (700, 400, "7")]
for x, y, n in marks:
    p.append(f'<circle cx="{x}" cy="{y+16}" r="22" fill="{FOSF}"/>')
    rs.append(rot(x - 22, y + 1, n, w=44, tam=26, cor=CLARO, peso=700, alinha="center"))
p.append("</svg>")
passos = ["O teste foi máximo?", "O valor, nas duas formas", "Onde estão os dois limiares", "As zonas do programa", "Resposta e recuperação da FC", "Eficiência ventilatória", "Por que o teste terminou"]
for i, t in enumerate(passos):
    rs.append(rot(860, 10 + i * 60, f"{i+1}. {t}", w=800, tam=30, cor=FOSF if i == 1 else TINTA, peso=700))
S.append({"id": "sete", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O roteiro de leitura", "titulo": "Sete passos, e o número grande é o segundo"})

# 13. o teste foi máximo
S.append({"id": "maximo", "tipo": "cards", "por_linha": 5, "eyebrow": "Passo um", "titulo": "O teste foi máximo?",
          "cards": [{"t": "RER > 1,10", "x": "razão de troca respiratória", "cor": "verm"}, {"t": "FC ± 10", "x": "da máxima prevista", "cor": "petr"},
                    {"t": "Esforço no topo", "x": "da escala percebida", "cor": "petr"}, {"t": "Lactato > 8", "x": "mmol/L", "cor": "petr"},
                    {"t": "Platô", "x": "do VO₂ com a carga subindo", "cor": "petr"}],
          "destaque": "Não há consenso sobre quantos critérios bastam, e o platô raramente aparece. Se o laudo não traz a RER atingida, peça. Sem esforço máximo, é VO₂ de pico.",
          "destaque_cor": "verm", "fonte": "Howley, Bassett e Welch, Medicine & Science in Sports & Exercise 1995"})

# 14. passos dois e três
p, rs = [svg_abre(1664, 400, "Passo dois: o valor em litros por minuto e em mililitros por quilo; passo três: os dois limiares traduzidos em watts, ritmo e frequência cardíaca")], []
p += [caixa(0, 0, 560, 380, BORDA, CARTAO, 2), caixa(620, 0, 1044, 380, OXID, OXID_T, 3)]
for k in range(3):
    p.append(f'<line x1="640" y1="{120 + k*80}" x2="1644" y2="{120 + k*80}" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs += [rot(30, 24, "2 · O valor", w=500, tam=30, cor=TINTA, peso=700),
       rot(30, 90, "3,6 L/min", w=500, tam=48, cor=TINTA, peso=700, serif=True), rot(30, 156, "absoluto: muda pouco com o peso", w=500, tam=24),
       rot(30, 220, "48,2 mL/kg/min", w=500, tam=48, cor=TINTA, peso=700, serif=True), rot(30, 286, "relativo: compara com referência", w=500, tam=24),
       rot(650, 24, "3 · Os limiares na moeda que prescreve", w=980, tam=30, cor=TINTA, peso=700),
       rot(900, 80, "carga", w=220, tam=24, cor=MUDO, alinha="center"), rot(1130, 80, "ritmo", w=220, tam=24, cor=MUDO, alinha="center"), rot(1360, 80, "FC", w=260, tam=24, cor=MUDO, alinha="center"),
       rot(650, 142, "1º limiar", w=240, tam=28, cor=OXID, peso=700), rot(900, 142, "180 W", w=220, tam=28, cor=TINTA, alinha="center"),
       rot(1130, 142, "5:40 /km", w=220, tam=28, cor=TINTA, alinha="center"), rot(1360, 142, "142 bpm", w=260, tam=28, cor=TINTA, alinha="center"),
       rot(650, 222, "2º limiar", w=240, tam=28, cor=FOSF, peso=700), rot(900, 222, "250 W", w=220, tam=28, cor=TINTA, alinha="center"),
       rot(1130, 222, "4:45 /km", w=220, tam=28, cor=TINTA, alinha="center"), rot(1360, 222, "166 bpm", w=260, tam=28, cor=TINTA, alinha="center"),
       rot(650, 310, "valores de exemplo", w=980, tam=24, cor=MUDO)]
S.append({"id": "moeda", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passos dois e três", "titulo": "Ninguém treina em percentual de VO₂máx",
          "destaque": "Se o laudo dá os limiares só em percentual, ele é bonito e inútil para a segunda-feira.", "destaque_cor": "ambar"})

# 15. as zonas do programa
p, rs = [svg_abre(1664, 400, "À esquerda, a tabela de zonas do programa por percentual da frequência máxima, riscada; à direita, as zonas refeitas a partir dos dois limiares do próprio teste")], []
p += [caixa(0, 0, 780, 380, BORDA, CARTAO, 2), caixa(884, 0, 780, 380, OXID, OXID_T, 3)]
for i, (a, b) in enumerate([("Z1", "50–60% FCmáx"), ("Z2", "60–70% FCmáx"), ("Z3", "70–80% FCmáx"), ("Z4", "80–90% FCmáx"), ("Z5", "90–100% FCmáx")]):
    rs += [rot(40, 80 + i * 56, a, w=100, tam=26, cor=MUDO, peso=700), rot(160, 80 + i * 56, b, w=500, tam=26, cor=MUDO)]
p.append(f'<line x1="30" y1="360" x2="750" y2="60" stroke="{FOSF}" stroke-width="8" stroke-linecap="round" opacity="0.7"/>')
for i, (a, b, cor) in enumerate([("Abaixo do 1º limiar", "até 142 bpm", OXID), ("Entre os limiares", "142 a 166 bpm", GLIC), ("Acima do 2º limiar", "acima de 166 bpm", FOSF)]):
    y = 90 + i * 90
    p.append(f'<rect x="914" y="{y}" width="14" height="60" rx="4" fill="{cor}"/>')
    rs += [rot(950, y, a, w=400, tam=28, cor=TINTA, peso=700), rot(950, y + 34, b, w=400, tam=24)]
p.append("</svg>")
rs += [rot(40, 20, "Do programa: fórmula de população", w=720, tam=28, cor=MUDO, peso=700),
       rot(914, 20, "Refeitas pelos limiares do teste", w=720, tam=28, cor=OXID, peso=700)]
S.append({"id": "zonas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo quatro", "titulo": "Não desperdice o exame",
          "destaque": "Se as zonas do laudo não estiverem ancoradas nos limiares, refaça a partir dos limiares.", "destaque_cor": "verm",
          "fonte": "Valores de exemplo"})

# 16. passos cinco a sete
S.append({"id": "ultimos", "tipo": "lista", "eyebrow": "Os três últimos passos", "titulo": "O que está no traçado, e não no resumo",
          "itens": [{"m": "5", "t": "Resposta e recuperação da frequência", "x": "Como subiu, o pico, quanto caiu no primeiro minuto. Recuperação lenta merece atenção."},
                    {"m": "6", "t": "Eficiência ventilatória", "x": "Valores altos têm valor prognóstico, sobretudo em doença do coração. Não é para prescrever: é para encaminhar.", "cor": "ambar"},
                    {"m": "7", "t": "Por que o teste terminou", "x": "Motivo, sintomas, eletrocardiograma, pressão. Inclusive a diastólica que sobe.", "cor": "verm"}],
          "destaque": "Clínica é médica. Limiares e zonas são do educador físico e do fisiologista. A pior leitura é a que olha só o número do topo.",
          "fonte": "Guazzi e colaboradores, Circulation 2016"})

# 17. sem laboratório
S.append({"id": "campo", "tipo": "duas", "eyebrow": "A maioria nunca vai fazer o exame", "titulo": "Achar os limiares sem laboratório",
          "esq": {"t": "1º limiar: teste do falar", "cor": "petr",
                  "itens": ["Fala uma frase inteira, com conforto: abaixo", "A fala quebra em pedaços: cruzando", "O critério para levar para todo treino leve"]},
          "dir": {"t": "2º limiar: contrarrelógio de 30 min", "cor": "verm",
                  "itens": ["Velocidade ou potência média: perto do 2º limiar", "FC média dos últimos 20 minutos: a FC de limiar", "Próximo do laboratório em corredores e triatletas"]},
          "fonte": "Reed e Pipe, Current Opinion in Cardiology 2014 · McGehee e colaboradores, Journal of Strength and Conditioning Research 2005"})

# 18. por que não % FC máxima
p, rs = [svg_abre(1664, 400, "Duas pessoas com a mesma idade e a mesma frequência máxima: numa o segundo limiar cai em 80% da máxima, na outra em 90%; a mesma zona de 85% cai em domínios diferentes")], []
for i, (lim, nome) in enumerate([(80, "Pessoa A"), (90, "Pessoa B")]):
    y = 40 + i * 150
    x0, W = 260, 1300
    p.append(f'<rect x="{x0}" y="{y}" width="{W*(lim-50)/50:.0f}" height="90" fill="{GLIC}" fill-opacity="0.85"/>')
    p.append(f'<rect x="{x0 + W*(lim-50)/50:.0f}" y="{y}" width="{W*(100-lim)/50:.0f}" height="90" fill="{FOSF}" fill-opacity="0.9"/>')
    rs.append(rot(0, y + 26, nome, w=230, tam=30, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(x0 + W - 260, y + 28, f"2º limiar em {lim}%", w=250, tam=24, cor=CLARO, peso=700, alinha="right"))
xz = 260 + 1300 * (85 - 50) / 50
p.append(f'<line x1="{xz:.0f}" y1="20" x2="{xz:.0f}" y2="300" stroke="{TINTA}" stroke-width="4" stroke-dasharray="12 8"/></svg>')
rs += [rot(xz - 200, 310, "a mesma “zona 85%” da planilha", w=400, tam=24, cor=TINTA, peso=700, alinha="center"),
       rot(260, 340, "50% da FC máxima", w=300, tam=24, cor=MUDO), rot(1260, 340, "100%", w=300, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "percentual", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que eu não recomendo", "titulo": "Mesmo número na planilha, domínios diferentes",
          "destaque": "Duzentos e oito menos 0,7 vezes a idade é melhor que 220 menos a idade, e ainda é população. E em tiro curto, a FC chega atrasada: use velocidade, potência ou esforço percebido.",
          "fonte": "Esquema · Tanaka, Monahan e Seals, Journal of the American College of Cardiology 2001"})

# 19. três zonas, três alavancas
p, rs = [svg_abre(1664, 400, "Três zonas com o que cada uma dá, e para quem treina há anos três alavancas em ordem de retorno: economia maior, limiar médio, VO2máx menor")], []
for i, (t, s, cor) in enumerate([("Abaixo do 1º", "volume que permite frequência", OXID), ("Entre os dois", "útil e caro: onde o atleta real mora", GLIC), ("Acima do 2º", "curto, potente, pede recuperação", FOSF)]):
    y = 10 + i * 128
    p.append(f'<rect x="0" y="{y}" width="760" height="110" rx="12" fill="{cor}"/>')
    rs += [rot(30, y + 14, t, w=700, tam=32, cor=CLARO, peso=700), rot(30, y + 60, s, w=700, tam=26, cor=CLARO)]
for i, (t, v, cor) in enumerate([("Economia", 1.0, OXID), ("Limiar", 0.66, GLIC), ("VO₂máx", 0.36, AZUL)]):
    y = 40 + i * 120
    p.append(f'<rect x="1080" y="{y}" width="{580*v:.0f}" height="80" rx="8" fill="{cor}"/>')
    rs.append(rot(860, y + 22, f"{i+1}. {t}", w=210, tam=28, cor=TINTA, peso=700, alinha="right"))
p.append("</svg>")
rs.append(rot(860, 0, "Quem treina há anos: ordem de retorno", w=800, tam=26, cor=TINTA, peso=700))
S.append({"id": "alavancas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que se decide com tudo isso", "titulo": "Três zonas, e onde mexer",
          "destaque": "O amador acrescenta tiros e deixa força e distribuição intocadas. A alavanca certa é a mais eficaz que a conta de energia, sono e recuperação suporta.",
          "destaque_cor": "ambar"})

# 20. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Dois lembretes",
          "regras": ["Os limiares se movem com o treino: reteste não é burocracia", "O cronômetro é mais honesto que o algoritmo"],
          "cards": [{"t": "Educador físico", "x": "Acha o limiar em campo e prescreve a intensidade a partir dele."},
                    {"t": "As outras profissões", "x": "Leem a planilha e reconhecem quando a intensidade explica o platô, a fadiga ou a lesão que se repete."}],
          "quem": "A pior leitura do laudo é a que olha só o número grande do topo."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['quebras', 'sustenta', 'cadeia', 'denominador', 'caso', 'sete', 'moeda', 'campo', 'percentual', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-08-limiares-vo2max-e-leitura-da-ergoespirometria.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Limiares e VO₂máx", "subtitulo": "Interpretação da ergoespirometria",
        "nota_capa": "Entra pela cena do laudo.",
        "secoes": {"limiares": ["Duas quebras, três domínios e o nome errado.", "capa"],
                   "vo2": ["O VO₂máx, a genética, o denominador e a economia.", "cadeia"],
                   "roteiro": ["Os sete passos de leitura do laudo.", "sete"],
                   "campo": ["Sem laboratório, e onde mexer.", "campo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-08.json"), "w"), ensure_ascii=False, indent=1)
print("02-08.json:", len(S), "slides")
