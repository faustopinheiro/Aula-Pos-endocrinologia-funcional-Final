"""Spec do deck 13.4. Gera 13-04.json ao lado deste arquivo."""
from _base import *

S = []


def raquete(x, y, s, cor):
    """Raquete de padel de frente: cabeça arredondada com furos e cabo, num retângulo s x 1,6s."""
    k = s / 100
    furos = "".join(f'<circle cx="{x + (32 + c * 18) * k:.0f}" cy="{y + (30 + r * 18) * k:.0f}" r="{4 * k:.0f}" fill="{PAPEL}"/>'
                    for r in range(4) for c in range(3))
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{100 * k:.0f}" height="{110 * k:.0f}" rx="{48 * k:.0f}" fill="{cor}"/>' + furos +
            f'<rect x="{x + 40 * k:.0f}" y="{y + 104 * k:.0f}" width="{20 * k:.0f}" height="{56 * k:.0f}" rx="{8 * k:.0f}" fill="{cor}"/>')


# 1. o pedido
p = [svg_abre(1664, 470, "Raquete de padel e bola sobre um pedido de exames com cinco linhas marcadas: eletrocardiograma, teste ergométrico, ecocardiograma, escore de cálcio, exames de sangue completos. Perfil: casa dos cinquenta, parado há dez anos, pressão tratada, ex-fumante, sem sintomas. Três saídas: libera com rampa, investiga antes do vigoroso, não libera até avaliar")]
rs = []
p.append(raquete(10, 20, 170, AZUL))
p.append(f'<circle cx="200" cy="250" r="26" fill="{GLIC}"/>')
p.append(caixa(260, 0, 520, 300, TINTA, CARTAO, esp=3, rx=14))
rs.append(rot(284, 16, "Pedido de exames", w=472, tam=26, cor=TINTA, peso=700, serif=True))
for j, t in enumerate(["eletrocardiograma", "teste ergométrico", "ecocardiograma", "escore de cálcio", "exames de sangue completos"]):
    y = 70 + j * 44
    p.append(f'<rect x="284" y="{y + 4}" width="24" height="24" rx="4" fill="none" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<path d="M 288 {y + 16} L 295 {y + 23} L 306 {y + 8}" stroke="{FOSF}" stroke-width="4" fill="none"/>')
    rs.append(rot(322, y, t, w=440, tam=22, cor=TINTA, peso=600))
p.append(caixa(820, 0, 844, 300, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(844, 18, "O perfil", w=796, tam=28, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["casa dos cinquenta, parado há dez anos", "pressão tratada com um remédio", "parou de fumar há cinco anos", "nenhum sintoma"]):
    rs.append(rot(844, 80 + j * 52, t, w=796, tam=24, cor=TINTA, peso=600))
for k, (t, c, f) in enumerate([("libera com rampa", OXID, OXID_T), ("investiga antes do vigoroso", GLIC, GLIC_T), ("não libera até avaliar", FOSF, FOSF_T)]):
    x = k * 564
    p.append(caixa(x, 340, 536, 110, c, f, esp=3, rx=16))
    rs.append(rot(x + 20, 372, t, w=496, tam=26, cor=c, peso=700, alinha="center", serif=True))
diagrama(S, "padel", 470, p, rs, eyebrow="Padel, um homem na casa dos cinquenta", titulo="Antes de começar, ele pediu todos os exames")

# 2. o tamanho do risco
p = [svg_abre(1664, 450, "Esquema fora de escala do risco ao longo de um dia: baixo no repouso, um pico durante o esforço vigoroso e nos 30 minutos seguintes. Risco relativo de 16,9 vezes. Risco absoluto de uma morte súbita a cada 1,51 milhão de episódios de esforço. 21.481 médicos homens, 12 anos de seguimento. Menor em quem se exercitava com frequência, sem desaparecer")]
rs = []
p.append(f'<line x1="0" y1="360" x2="860" y2="360" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<rect x="360" y="40" width="200" height="320" fill="{FOSF_T}"/>')
p.append(f'<path d="M 0 330 L 360 330 L 380 70 L 460 70 L 560 300 L 600 330 L 860 330" stroke="{FOSF}" stroke-width="6" fill="none" stroke-linejoin="round"/>')
rs += [rot(0, 372, "repouso", w=300, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(350, 372, "esforço e 30 minutos", w=220, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(600, 372, "repouso", w=260, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(0, 0, "esquema fora de escala", w=400, tam=20, cor=MUDO)]
p.append(caixa(920, 0, 360, 220, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(940, 20, "16,9×", w=320, tam=64, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(940, 120, "risco relativo no esforço vigoroso", w=320, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.25)]
p.append(caixa(1304, 0, 360, 220, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1324, 20, "1 em 1,51 milhão", w=320, tam=36, cor=AZUL, peso=700, serif=True, alinha="center", lh=1.15),
       rot(1324, 120, "episódios de esforço: o risco absoluto", w=320, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.25)]
p.append(caixa(920, 250, 744, 200, GRADE, CARTAO, esp=2, rx=18))
p.append(icone("t:trending-down", 944, 280, 56, OXID))
rs += [rot(1016, 276, "menor em quem se exercitava com frequência, sem desaparecer", w=624, tam=24, cor=OXID, peso=700, lh=1.25),
       rot(944, 380, "21.481 médicos homens · 12 anos", w=696, tam=22, cor=MUDO, peso=700)]
diagrama(S, "risco", 450, p, rs, eyebrow="O tamanho do risco que ele quer descartar", titulo="Na hora, o risco sobe dezessete vezes, e continua raríssimo",
         fonte="N Engl J Med 2000")

# 3. a escada
p = [svg_abre(1664, 470, "Escada de quatro degraus. Degrau 1, perguntas: sintoma no esforço, doença conhecida, intensidade pretendida. Degrau 2, exame e risco calculado. Degrau 3, teste ergométrico. Degrau 4, além: escore de cálcio, ecocardiograma. Só se sobe com uma pergunta que o degrau de baixo não respondeu. O pedido dele começa no degrau 4"), defs(MUDO)]
rs = []
for k, (t, x_, c, f) in enumerate([("1 · perguntas", "sintoma no esforço · doença conhecida · intensidade pretendida", OXID, OXID_T),
                                   ("2 · exame e risco", "pressão · colesterol · glicose · risco em dez anos", OXID, OXID_T),
                                   ("3 · teste ergométrico", "", GLIC, GLIC_T),
                                   ("4 · além", "escore de cálcio · ecocardiograma", FOSF, FOSF_T)]):
    x = k * 416
    top = 320 - k * 90
    p.append(f'<rect x="{x}" y="{top}" width="400" height="{470 - top}" rx="14" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x + 16, top + 14, t, w=368, tam=26, cor=c, peso=700, serif=True))
    if x_:
        rs.append(rot(x + 16, top + 60, x_, w=368, tam=20, cor=TINTA, peso=600, lh=1.3))
    if k:
        p.append(seta(x - 60, top + 120, x - 10, top + 40, MUDO, "m0", 3))
rs.append(rot(0, 40, "Só se sobe com uma pergunta que o degrau de baixo não respondeu.", w=1100, tam=28, cor=TINTA, peso=700, serif=True, lh=1.25))
p.append(seta(1460, 16, 1460, 40, FOSF, "m0", 3))
rs.append(rot(1180, 0, "o pedido dele começa aqui", w=260, tam=20, cor=FOSF, peso=700, alinha="right"))
diagrama(S, "escada", 470, p, rs, eyebrow="A avaliação do amador é uma escada", titulo="Cada exame precisa de uma pergunta nova")

# 4. o eletro como rastreio
p = [svg_abre(1664, 460, "Recomendação de 2018 da força-tarefa de prevenção dos Estados Unidos. Sem sintoma e risco baixo: não rastrear com eletro de repouso nem de esforço, grau D. Sem sintoma e risco intermediário ou alto: evidência insuficiente, I. 16 estudos, 77.140 participantes. Cascata: achado inespecífico, novo exame, procedimento, complicação"), defs(FOSF)]
rs = []
p.append(caixa(0, 0, 1080, 120, FOSF, FOSF_T, esp=3, rx=16))
p.append(f'<rect x="20" y="20" width="80" height="80" rx="12" fill="{FOSF}"/>')
rs += [rot(20, 36, "D", w=80, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True),
       rot(124, 20, "sem sintoma e risco baixo", w=936, tam=26, cor=FOSF, peso=700, serif=True),
       rot(124, 64, "não rastrear com eletro de repouso nem de esforço", w=936, tam=24, cor=TINTA, peso=600)]
p.append(caixa(0, 140, 1080, 120, GLIC, GLIC_T, esp=3, rx=16))
p.append(f'<rect x="20" y="160" width="80" height="80" rx="12" fill="{GLIC}"/>')
rs += [rot(20, 176, "I", w=80, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True),
       rot(124, 160, "sem sintoma, risco intermediário ou alto", w=936, tam=26, cor=GLIC, peso=700, serif=True),
       rot(124, 204, "evidência insuficiente para pesar benefício e dano", w=936, tam=24, cor=TINTA, peso=600)]
p.append(caixa(1120, 0, 544, 260, GRADE, CARTAO, esp=2, rx=16))
rs += [rot(1144, 24, "16 estudos", w=496, tam=36, cor=TINTA, peso=700, serif=True),
       rot(1144, 80, "77.140 participantes", w=496, tam=26, cor=TINTA, peso=700),
       rot(1144, 140, "o resultado quase nunca muda a categoria de risco", w=496, tam=22, cor=MUDO, peso=700, lh=1.3)]
for j, t in enumerate(["achado inespecífico", "novo exame", "procedimento", "complicação"]):
    x = j * 424
    p.append(caixa(x, 320, 360, 100, FOSF, PAPEL, esp=2, rx=14))
    rs.append(rot(x + 12, 352, t, w=336, tam=24, cor=FOSF, peso=700, alinha="center"))
    if j:
        p.append(seta(x - 60, 370, x - 8, 370, FOSF, "m0", 4))
rs.append(rot(0, 428, "a cascata da conversa sobre rastreio laboratorial", w=1664, tam=20, cor=MUDO, peso=600, alinha="center"))
diagrama(S, "eletro", 460, p, rs, eyebrow="O eletro como rastreio, força-tarefa de 2018", titulo="Sem sintoma e com risco baixo, o eletro de rastreio não muda o desfecho",
         fonte="JAMA 2018")

# 5. a decisão para ele
p = [svg_abre(1664, 470, "A escada com as respostas dele. Degrau 1: sem sintoma, sem doença cardiovascular conhecida, quer jogar em intensidade vigorosa. Degrau 2: pressão controlada, colesterol e glicose, risco calculado. Bifurcação: risco baixo, libera com rampa; risco alto ou sintoma, teste ergométrico antes do jogo competitivo. Ecocardiograma e escore de cálcio sem pergunta não entram"), defs(OXID, FOSF)]
rs = []
for k, (t, itens) in enumerate([("Degrau 1", ["sem sintoma", "sem doença cardiovascular conhecida", "quer jogar em intensidade vigorosa"]),
                                ("Degrau 2", ["pressão controlada", "colesterol e glicose", "risco calculado em dez anos"])]):
    x = k * 440
    p.append(caixa(x, 0, 410, 300, OXID, OXID_T, esp=3, rx=18))
    rs.append(rot(x + 20, 18, t, w=370, tam=28, cor=OXID, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 20, 80 + j * 64, it, w=370, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(seta(880, 110, 960, 60, OXID, "m0", 5))
p.append(seta(880, 190, 960, 240, FOSF, "m1", 5))
p.append(caixa(980, 0, 684, 130, OXID, OXID, esp=3, rx=18))
rs += [rot(1004, 16, "risco baixo", w=636, tam=24, cor=PAPEL, peso=700),
       rot(1004, 56, "libera com rampa", w=636, tam=36, cor=PAPEL, peso=700, serif=True)]
p.append(caixa(980, 170, 684, 130, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1004, 186, "risco alto ou sintoma", w=636, tam=24, cor=FOSF, peso=700),
       rot(1004, 226, "teste ergométrico antes do competitivo", w=636, tam=28, cor=TINTA, peso=700, serif=True)]
p.append(caixa(0, 340, 1664, 110, GRADE, CARTAO, esp=2, rx=18))
rs.append(rot(24, 376, "Ecocardiograma e escore de cálcio sem uma pergunta específica não entram.", w=1616, tam=26, cor=MUDO, peso=700, alinha="center"))
diagrama(S, "decisao", 470, p, rs, eyebrow="A escada com as respostas dele", titulo="Para ele, a decisão para no segundo degrau")

# 6. o que tira da quadra
p = [svg_abre(1664, 450, "Silhueta de jogador com quatro regiões numeradas em ordem de frequência: cotovelo, joelho, ombro, lombar. Tendão e músculo são os tipos mais relatados. Revisão de 2023: 8 estudos, 2.022 participantes, idade média de 31 a 57 anos; 3 lesões por mil horas de treino e 8 por mil jogos")]
rs = []
p.append(menino(200, 440, 420, AZUL_T))
p.append(f'<rect x="250" y="160" width="26" height="150" rx="10" fill="{AZUL_T}" transform="rotate(-30 263 160)"/>')
for n, (cx, cy) in enumerate([(300, 260), (225, 340), (240, 150), (200, 250)], 1):
    p.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="{FOSF}"/>')
    rs.append(rot(cx - 22, cy - 14, str(n), w=44, tam=22, cor=PAPEL, peso=700, alinha="center"))
for n, t in enumerate(["cotovelo", "joelho", "ombro", "lombar"], 1):
    y = 30 + (n - 1) * 70
    p.append(f'<circle cx="500" cy="{y + 18}" r="22" fill="{FOSF}"/>')
    rs.append(rot(478, y + 4, str(n), w=44, tam=22, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(540, y, t, w=360, tam=30, cor=TINTA, peso=700, serif=True))
rs.append(rot(478, 320, "tendão e músculo: os tipos mais relatados", w=500, tam=24, cor=FOSF, peso=700, lh=1.25))
p.append(caixa(1040, 0, 624, 450, GRADE, CARTAO, esp=2, rx=18))
rs += [rot(1064, 24, "Revisão de 2023", w=576, tam=30, cor=TINTA, peso=700, serif=True),
       rot(1064, 84, "8 estudos · 2.022 jogadores · idade média de 31 a 57 anos", w=576, tam=24, cor=TINTA, peso=600, lh=1.3),
       rot(1064, 200, "3 lesões por mil horas de treino", w=576, tam=26, cor=AZUL, peso=700),
       rot(1064, 250, "8 por mil jogos", w=576, tam=26, cor=AZUL, peso=700),
       rot(1064, 330, "estudos pequenos e diferentes entre si, sem metanálise", w=576, tam=22, cor=MUDO, peso=700, lh=1.3)]
diagrama(S, "quadra", 450, p, rs, eyebrow="O que de fato tira o amador da quadra", titulo="No padel amador, o problema mais comum é tendão e músculo",
         fonte="BMJ Open Sport Exerc Med 2023")

# 7. a rampa
p = [svg_abre(1664, 440, "Esquema da rampa em doze semanas. Semanas 1 a 4: duas vezes por semana, aula e jogos curtos. Semanas 5 a 8: duas a três vezes, jogos inteiros. Semanas 9 a 12: três vezes, competitivo. Contínuos: força duas vezes por semana com antebraço, ombro e panturrilha; aquecimento de dez minutos antes de cada jogo")]
rs = []
for k, (sem, t, h, c) in enumerate([("semanas 1 a 4", "2× por semana · aula e jogos curtos", 120, AZUL_T),
                                    ("semanas 5 a 8", "2 a 3× · jogos inteiros", 190, AZUL_T),
                                    ("semanas 9 a 12", "3× · competitivo", 260, AZUL)]):
    x = k * 560
    p.append(f'<rect x="{x}" y="{270 - h}" width="540" height="{h}" rx="14" fill="{c}" stroke="{AZUL}" stroke-width="3"/>')
    cor_t = PAPEL if c == AZUL else AZUL
    rs += [rot(x + 20, 270 - h + 14, sem, w=500, tam=24, cor=cor_t, peso=700),
           rot(x + 20, 270 - h + 52, t, w=500, tam=24, cor=PAPEL if c == AZUL else TINTA, peso=700, serif=True, lh=1.2)]
for j, (t, c, f) in enumerate([("força 2× por semana: antebraço, ombro, panturrilha", OXID, OXID_T), ("aquecimento de dez minutos antes de cada jogo", GLIC, GLIC_T)]):
    y = 300 + j * 70
    p.append(caixa(0, y, 1664, 56, c, f, esp=2, rx=12))
    rs.append(rot(20, y + 12, t, w=1624, tam=24, cor=c, peso=700))
rs.append(rot(0, 0, "esquema", w=300, tam=20, cor=MUDO))
diagrama(S, "rampa", 440, p, rs, eyebrow="O que protege no primeiro ano", titulo="A rampa protege mais que o exame que ele queria")

# 8. os sinais
p = [svg_abre(1664, 450, "Quatro sinais: desconforto no peito no esforço, falta de ar desproporcional, batedeira ou palpitação diferente, desmaio ou quase desmaio. Parar e procurar avaliação antes do próximo jogo. Ao lado, um desfibrilador na parede de um clube: o clube tem um, e alguém sabe usar?")]
rs = []
for j, t in enumerate(["desconforto no peito no esforço", "falta de ar desproporcional", "batedeira ou palpitação diferente", "desmaio ou quase desmaio"]):
    x, y = (j % 2) * 530, (j // 2) * 150
    p.append(caixa(x, y, 510, 130, FOSF, FOSF_T, esp=3, rx=16))
    p.append(icone("t:alert-triangle", x + 20, y + 37, 56, FOSF))
    rs.append(rot(x + 92, y + 30, t, w=398, tam=26, cor=TINTA, peso=700, lh=1.2))
p.append(f'<rect x="0" y="330" width="1040" height="110" rx="16" fill="{FOSF}"/>')
rs.append(rot(20, 366, "Parar e procurar avaliação antes do próximo jogo.", w=1000, tam=28, cor=PAPEL, peso=700, serif=True, alinha="center"))
p.append(f'<rect x="1100" y="0" width="564" height="440" rx="18" fill="{CARTAO}" stroke="{GRADE}" stroke-width="2"/>')
p.append(f'<rect x="1270" y="40" width="220" height="200" rx="18" fill="{OXID}"/>')
p.append(icone("t:heart", 1330, 70, 100, PAPEL))
p.append(icone("t:bolt", 1358, 98, 44, PAPEL))
rs += [rot(1124, 270, "o clube tem um, e alguém sabe usar?", w=516, tam=28, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.25),
       rot(1124, 370, "a resposta de emergência tem conversa própria", w=516, tam=22, cor=MUDO, peso=700, alinha="center")]
diagrama(S, "sinais", 450, p, rs, eyebrow="O que ele leva para casa", titulo="Os quatro sinais valem mais que o laudo")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Avaliação pré-participação no amador", "titulo": "Subir a escada só com pergunta",
          "regras": ["Cada exame precisa de uma pergunta nova",
                     "Sem sintoma e com risco baixo, o eletro de rastreio não muda o desfecho",
                     "A rampa e os sinais protegem mais que o exame para tranquilizar"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Sobe a escada só com pergunta, calcula o risco e ensina os sinais."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Monta a rampa de doze semanas e a força de antebraço, ombro e panturrilha."},
                    {"ic": "t:user", "t": "O praticante", "x": "Respeita a rampa e para diante de qualquer sinal."}]})

salvar("13-04.json", {"arquivo": "aulas/MOD13/13-04-avaliacao-pre-participacao-no-amador.md",
                      "titulo": "Avaliação pré-participação no amador", "subtitulo": "Até onde ir com exames antes de começar",
                      "nota_capa": "Entra por um homem na casa dos cinquenta que quer todos os exames antes do padel.",
                      "secoes": {"padel": ["O pedido.", "capa"], "escada": ["A escada.", "escada"],
                                 "quadra": ["O que protege de fato.", "quadra"]},
                      "slides": S})
