"""Spec do deck 2.6. Gera 02-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a frase
S.append({"id": "frase", "tipo": "frase", "fundo": "tinta", "eyebrow": "Na borda da piscina, no meio do circuito, no fim da subida",
          "frase": "“Meu pulmão não aguenta.”",
          "apoio": "O erro custa nos dois sentidos: trata quem não precisa e deixa de investigar quem precisa. E convence, porque a falta de ar é a sensação mais alta do corpo no esforço."})

# 2. sobra reserva
ve = [(x, 10 + 0.72 * x + 0.0025 * x * x) for x in range(0, 101, 4)]
def reserva(fx, fy):
    top = " ".join(f"{fx(x):.1f},{fy(150):.1f}" for x, _ in ve)
    bot = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in reversed(ve))
    return f'<polygon points="{top} {bot}" fill="{OXID}" fill-opacity="0.14"/>'
svg, rs = linhas(1664, 420, "Durante um teste progressivo a ventilação sobe muito, mas fica abaixo da capacidade ventilatória máxima da pessoa; a distância entre as duas é a reserva",
    [{"nome": "", "cor": TINTA, "pts": [(0, 150), (100, 150)], "tracejado": True, "esp": 3},
     {"nome": "", "cor": AZUL, "pts": ve}], 0, 100, 0, 170, [(0, "repouso"), (100, "esforço máximo")], [], margem=(40, 20, 60, 30), extra=reserva)
rs += [rot(60, 20, "capacidade ventilatória máxima da pessoa", w=700, tam=26, cor=TINTA, peso=600),
       rot(700, 140, "sobra reserva", w=400, tam=36, cor=OXID, peso=700, serif=True),
       rot(1250, 200, "ventilação no máximo", w=380, tam=26, cor=AZUL, peso=700)]
S.append({"id": "reserva", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "O fato que derruba a frase", "titulo": "Em saudável, ao nível do mar, o pulmão não limita",
          "destaque": "Exceção: parte dos atletas de endurance muito treinados, e muitas mulheres treinadas, deixam a saturação cair no máximo. Exceção de quem já está no topo.",
          "fonte": "Esquema · Dempsey e Wagner, Journal of Applied Physiology 1999"})

# 3. o único que não se adapta
p = [svg_abre(1664, 380, "Coração, volume de sangue, capilar e mitocôndria se adaptam ao treino; o pulmão praticamente não"),
     "<defs>" + seta_marker("a1", OXID) + "</defs>"]
itens = [("Coração", True), ("Volume de sangue", True), ("Capilar", True), ("Mitocôndria", True), ("Pulmão", False)]
rs = []
for i, (t, sobe) in enumerate(itens):
    x = i * 336
    cor = OXID if sobe else MUDO
    p.append(caixa(x, 150, 300, 110, cor, OXID_T if sobe else CARTAO))
    rs.append(rot(x, 184, t, w=300, tam=30, cor=TINTA, peso=700, alinha="center"))
    if sobe:
        p.append(f'<path d="M{x+150} 130 L{x+150} 30" stroke="{OXID}" stroke-width="8" marker-end="url(#a1)"/>')
    else:
        rs.append(rot(x, 60, "praticamente não muda", w=300, tam=26, cor=MUDO, peso=700, alinha="center"))
p.append("</svg>")
rs.append(rot(0, 300, "Já nasce superdimensionado para a demanda. E mesmo assim não é o gargalo.", w=1664, tam=30, cor=TINTA, peso=700, serif=True, alinha="center"))
S.append({"id": "adapta", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O segundo fato, menos conhecido", "titulo": "Tudo no transporte melhora com treino, menos o pulmão"})

# 4. comando ventilatório
p = [svg_abre(1664, 420, "A coxa produz gás carbônico e prótons; eles sobem pelo sangue até o tronco encefálico, que manda o diafragma respirar mais"),
     "<defs>" + seta_marker("c1", FOSF) + seta_marker("c2", AZUL) + "</defs>",
     caixa(0, 250, 420, 140, FOSF, FOSF_T), caixa(620, 20, 420, 140, TINTA), caixa(1244, 250, 420, 140, AZUL, AZUL_T),
     f'<path d="M300 246 C380 120 480 90 612 90" fill="none" stroke="{FOSF}" stroke-width="7" marker-end="url(#c1)"/>',
     f'<path d="M1044 90 C1180 90 1290 130 1384 242" fill="none" stroke="{AZUL}" stroke-width="7" marker-end="url(#c2)"/>', "</svg>"]
rs = [rot(0, 272, "Coxa", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(0, 318, "gás carbônico e prótons", w=420, tam=26, alinha="center"),
      rot(620, 42, "Tronco encefálico", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(620, 88, "cobra ventilação", w=420, tam=26, alinha="center"),
      rot(1244, 272, "Diafragma", w=420, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(1244, 318, "respira mais", w=420, tam=26, alinha="center"),
      rot(470, 250, "pelo sangue", w=260, tam=24, cor=FOSF, peso=600)]
S.append({"id": "comando", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Então o que é essa falta de ar", "titulo": "A química da perna chegando ao cérebro",
          "destaque": "Na imensa maioria das vezes: a demanda subiu, e o resto do sistema ainda não acompanha. Não é o pulmão. É a conta."})

# 5. três quadros
S.append({"id": "tres", "tipo": "cards", "por_linha": 3, "eyebrow": "As exceções: o motivo desta aula existir",
          "titulo": "Três quadros que se confundem",
          "cards": [{"t": "Broncoconstrição induzida pelo exercício", "x": "O brônquio se fecha por causa do esforço.", "cor": "verm"},
                    {"t": "Obstrução da laringe induzida pelo exercício", "x": "A laringe se fecha no pico do esforço.", "cor": "ambar"},
                    {"t": "Descondicionamento", "x": "Ainda a explicação mais comum.", "cor": "petr"}],
          "destaque": "Quem aprendeu que “o pulmão não limita” vira quem não investiga ninguém. É o mesmo erro com o sinal trocado.", "destaque_cor": "verm"})

# 6. broncoconstrição: o mecanismo
p = [svg_abre(1664, 400, "Muito ar passando pela via aérea por muito tempo resseca e esfria a mucosa; ar frio do inverno e cloro da piscina completam o cenário"),
     "<defs>" + seta_marker("b1", AZUL) + "</defs>",
     f'<path d="M0 120 L1000 120 M0 280 L1000 280" stroke="{FOSF}" stroke-width="14" stroke-linecap="round"/>',
     f'<rect x="0" y="127" width="1000" height="146" fill="{FOSF_T}"/>']
for k in range(6):
    y = 150 + (k % 3) * 45
    x = 40 + k * 150
    p.append(f'<path d="M{x} {y} L{x+120} {y}" stroke="{AZUL}" stroke-width="5" marker-end="url(#b1)"/>')
p += [caixa(1100, 40, 564, 140, AZUL, AZUL_T), caixa(1100, 220, 564, 140, OXID, OXID_T), "</svg>"]
rs = [rot(0, 40, "ventilação muito alta, por muito tempo", w=1000, tam=28, cor=TINTA, peso=700),
      rot(0, 300, "a mucosa resseca e esfria: o brônquio responde fechando", w=1000, tam=26, cor=FOSF, peso=600),
      rot(1130, 64, "Ar frio", w=500, tam=30, cor=TINTA, peso=700), rot(1130, 110, "esqui, patinação, corrida no inverno", w=520, tam=24),
      rot(1130, 244, "Piscina coberta", w=500, tam=30, cor=TINTA, peso=700), rot(1130, 290, "ar com cloro, em volume alto", w=520, tam=24)]
S.append({"id": "bronco", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O primeiro quadro", "titulo": "A doença crônica mais comum no atleta de elite",
          "destaque": "Endurance, inverno e água. Em algumas séries com esquiadores de cross-country e nadadores de elite, chega perto de metade dos atletas.",
          "fonte": "He e Song, The Physician and Sportsmedicine 2023"})

# 7. piora depois
sint = [(t, 0 if t < 0 else 90 * (t / 10) ** 2 * math.exp(2 * (1 - t / 10))) for t in range(-20, 41)]
def treino(fx, fy):
    return f'<rect x="{fx(-20):.1f}" y="{fy(100):.1f}" width="{fx(0)-fx(-20):.1f}" height="{fy(0)-fy(100):.1f}" fill="{PAUSA}" fill-opacity="0.45"/>'
svg, rs = linhas(1664, 400, "Linha do tempo: durante o treino e depois que ele termina; os sintomas da broncoconstrição sobem depois de parar, com pico entre 5 e 15 minutos",
    [{"nome": "", "cor": FOSF, "pts": sint}], -20, 40, 0, 100, [(-20, "treino"), (0, "para"), (5, "5 min"), (15, "15 min"), (40, "40 min")], [],
    margem=(40, 20, 60, 30), extra=treino)
rs += [rot(80, 30, "esforço", w=300, tam=28, cor=TINTA, peso=700),
       rot(1000, 40, "tosse, chiado, peito apertado no vestiário", w=600, tam=28, cor=FOSF, peso=700)]
S.append({"id": "depois", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "A assinatura da broncoconstrição", "titulo": "Piora depois que o esforço termina",
          "destaque": "O relato de sintoma é ruim para esse diagnóstico. Quem decide é o teste de broncoprovocação, não a história bem contada.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos"})

# 8. a laringe
p = [svg_abre(1664, 380, "A laringe se fecha parcialmente no pico do esforço; o ruído aparece ao puxar o ar e o atleta aponta para a garganta")]
for i, (ab, nome) in enumerate([(70, "Repouso"), (22, "Pico do esforço")]):
    cx = 300 + i * 560
    p.append(f'<ellipse cx="{cx}" cy="190" rx="160" ry="130" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="5"/>')
    p.append(f'<path d="M{cx-ab} 90 Q{cx} 190 {cx-ab} 290" fill="none" stroke="{FOSF}" stroke-width="12" stroke-linecap="round"/>')
    p.append(f'<path d="M{cx+ab} 90 Q{cx} 190 {cx+ab} 290" fill="none" stroke="{FOSF}" stroke-width="12" stroke-linecap="round"/>')
p.append(f'<line x1="1180" y1="0" x2="1180" y2="380" stroke="{GRADE}" stroke-width="2"/></svg>')
rs = [rot(140, 336, "Repouso: aberta", w=320, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(700, 336, "Pico: fechando", w=320, tam=28, cor=FOSF, peso=700, alinha="center"),
      rot(1220, 30, "5 a 8%", w=440, tam=72, cor=GLIC, peso=700, serif=True),
      rot(1220, 130, "dos adolescentes, em estudos com a população geral", w=440, tam=26),
      rot(1220, 240, "Quase ninguém conhece.", w=440, tam=30, cor=TINTA, peso=700)]
S.append({"id": "laringe", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O segundo quadro", "titulo": "O problema não está no brônquio. Está na laringe.",
          "fonte": "Esquema · Johansson e colaboradores, Thorax 2015 (5,7%) · Christensen e colaboradores, 2011 (7,5%)"})

# 9. as diferenças de graça
p = [svg_abre(1664, 380, "Comparação: a broncoconstrição piora depois de parar, o ruído é ao soltar o ar no peito e o broncodilatador costuma ajudar; a obstrução da laringe aparece no pico e melhora em minutos, o ruído é ao puxar o ar na garganta e o broncodilatador não muda nada")]
p += [caixa(400, 0, 610, 380, FOSF, FOSF_T, 3), caixa(1054, 0, 610, 380, GLIC, GLIC_T, 3)]
for y in (90, 190, 290):
    p.append(f'<line x1="0" y1="{y}" x2="1664" y2="{y}" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(400, 26, "Broncoconstrição", w=610, tam=32, cor=FOSF, peso=700, alinha="center"),
      rot(1054, 26, "Obstrução da laringe", w=610, tam=32, cor=GLIC, peso=700, alinha="center")]
linhas_t = [("Quando aparece", "Piora depois de parar", "No pico, melhora em minutos"),
            ("Onde é o barulho", "Ao soltar o ar, no peito", "Ao puxar o ar, na garganta"),
            ("Broncodilatador", "Costuma ajudar", "Não muda nada")]
for i, (a_, b_, c_) in enumerate(linhas_t):
    y = 118 + i * 100
    rs += [rot(0, y, a_, w=370, tam=30, cor=TINTA, peso=700, alinha="right"),
           rot(420, y, b_, w=570, tam=30, cor=TINTA, alinha="center"),
           rot(1074, y, c_, w=570, tam=30, cor=TINTA, alinha="center")]
S.append({"id": "diferencas", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Todas de graça, na conversa", "titulo": "Como separar os dois",
          "destaque": "“A bombinha resolveu?” A resposta costuma estar ali, de graça, na história de quem já usou."})

# 10. o tamanho do problema
S.append({"id": "tamanho", "tipo": "numeros", "eyebrow": "Obstrução da laringe · série internacional", "titulo": "Dois anos de bombinha, num quadro que ela não trata",
          "numeros": [{"n": "1.007", "x": "pacientes com obstrução da laringe", "cor": "tinta"},
                      {"n": "2 anos", "x": "de demora média até o diagnóstico", "cor": "ambar"},
                      {"n": "20%", "x": "estavam sendo tratados como asmáticos", "cor": "verm"}],
          "destaque": "Diagnóstico e tratamento são médicos. A suspeita é de todos: o técnico que nota a tosse sempre depois do treino abre a porta.",
          "fonte": "Walsted e colaboradores, ERJ Open Research 2021"})

# 11. o músculo que ventila
p = [svg_abre(1664, 390, "O coração no meio com um débito só; de um lado o diafragma trabalhando pesado, do outro a perna; quando o trabalho de respirar passa de um ponto, um reflexo fecha os vasos da perna"),
     "<defs>" + seta_marker("m1", TINTA) + seta_marker("m2", FOSF) + "</defs>",
     f'<path d="M832 150 C772 70 672 120 692 200 C712 280 832 330 832 350 C832 330 952 280 972 200 C992 120 892 70 832 150 Z" fill="{FOSF}"/>',
     caixa(0, 120, 480, 180, AZUL, AZUL_T), caixa(1184, 120, 480, 180, OXID, OXID_T),
     f'<path d="M680 240 L492 240" stroke="{TINTA}" stroke-width="6" marker-end="url(#m1)"/>',
     f'<path d="M984 240 L1172 240" stroke="{TINTA}" stroke-width="6" marker-end="url(#m1)"/>',
     f'<path d="M300 116 C500 -20 1100 -20 1330 110" fill="none" stroke="{FOSF}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#m2)"/>',
     "</svg>"]
rs = [rot(0, 150, "Diafragma", w=480, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(0, 200, "trabalho pesado de respirar", w=480, tam=26, alinha="center"),
      rot(1184, 150, "Perna", w=480, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(1184, 200, "o músculo do esforço", w=480, tam=26, alinha="center"),
      rot(532, 30, "reflexo: fecha os vasos da perna", w=600, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(632, 356, "um débito só", w=400, tam=26, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "roubo", "tipo": "diagrama", "h": 390, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A única forma legítima de a respiração limitar", "titulo": "A respiração e a perna disputam o mesmo débito",
          "destaque": "Treinar a musculatura inspiratória: um pouco, em algumas situações, e bem menos do que se anuncia. Conversa para quem já acertou o resto.",
          "destaque_cor": "ambar", "fonte": "Harms, Dempsey e colaboradores, Journal of Applied Physiology 1997"})

# 12. dor de lado
S.append({"id": "dordelado", "tipo": "numeros", "eyebrow": "A dor de lado", "titulo": "Muito comum, e não é cãibra de diafragma",
          "numeros": [{"n": "~70%", "x": "dos corredores sentiram no último ano", "cor": "ambar"},
                      {"n": "1 em 5", "x": "participantes sente numa única prova", "cor": "verm"}],
          "destaque": "Irritação do peritônio e dos nervos entre as costelas. Menos líquido e comida antes, postura, e na hora: baixar o ritmo, soltar o ar por completo, pressionar o local.",
          "fonte": "Morton e Callister, Sports Medicine 2015"})

# 13. três perguntas
p = [svg_abre(1664, 420, "Três perguntas: quando aparece, onde a pessoa aponta e o que já foi tentado; os caminhos levam a investigar via aérea, investigar laringe ou ajustar o treino"),
     "<defs>" + seta_marker("q1", TINTA) + "</defs>"]
pergs = [("Quando aparece?", "no pico e passa · ou depois e persiste"), ("Onde aponta?", "garganta · ou peito"), ("O que já tentou?", "a bombinha resolveu · ou não mudou nada")]
rs = []
for i, (t, s) in enumerate(pergs):
    y = 10 + i * 135
    p.append(f'<rect x="0" y="{y}" width="760" height="110" rx="14" fill="{TINTA}"/>')
    rs += [rot(30, y + 14, t, w=700, tam=32, cor=CLARO, peso=700), rot(30, y + 60, s, w=700, tam=26, cor="#BFD0DA")]
saidas = [("Investigar a via aérea", "tosse e chiado depois de parar", FOSF), ("Investigar a laringe", "ruído ao puxar o ar, no pico", GLIC), ("Ajustar o treino", "o sistema ainda não acompanha", OXID)]
for i, (t, s, cor) in enumerate(saidas):
    y = 10 + i * 135
    p.append(caixa(1000, y, 664, 110, cor))
    p.append(f'<path d="M770 {y+55} L990 {y+55}" stroke="{TINTA}" stroke-width="5" marker-end="url(#q1)"/>')
    rs += [rot(1030, y + 14, t, w=620, tam=30, cor=TINTA, peso=700), rot(1030, y + 60, s, w=620, tam=24)]
p.append("</svg>")
S.append({"id": "perguntas", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "No lugar de “seu pulmão não aguenta”", "titulo": "Três perguntas, nenhum equipamento",
          "destaque": "Não fecha diagnóstico, e não é para fechar. Decide se a pessoa sai com ajuste de treino ou com encaminhamento."})

# 14. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Quando a falta de ar não é normal",
          "regras": ["Desproporcional ao esforço e ao nível de treino", "Chiado, ou tosse que começa depois e persiste", "Ruído na garganta ao puxar o ar",
                     "Em repouso, ou que acorda a pessoa", "Com dor no peito, palpitação ou quase desmaio"],
          "cards": [{"t": "Ao nível do mar", "x": "Tudo isso vale ao nível do mar."},
                    {"t": "Na altitude", "x": "A pressão do oxigênio cai e a equação muda de lugar. Tem aula própria."}],
          "quem": "Não é o pulmão. É a conta. Até que a história diga o contrário."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['reserva', 'adapta', 'bronco', 'depois', 'diferencas', 'roubo', 'dordelado', 'perguntas', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-06-sistema-respiratorio-no-exercicio.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Sistema respiratório no exercício", "subtitulo": "Limites ventilatórios e diagnóstico diferencial da dispneia",
        "nota_capa": "Entra pela frase da borda da piscina.",
        "secoes": {"erro": ["A frase e os fatos que a derrubam.", "capa"],
                   "excecoes": ["Os três quadros que se confundem.", "bronco"],
                   "musculo": ["O músculo que ventila, a dor de lado e as três perguntas.", "roubo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-06.json"), "w"), ensure_ascii=False, indent=1)
print("02-06.json:", len(S), "slides")
