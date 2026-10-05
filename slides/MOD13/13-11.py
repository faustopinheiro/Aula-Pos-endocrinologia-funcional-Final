"""Spec do deck 13.11. Gera 13-11.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o box
p = [svg_abre(1664, 440, "Praticante de treino funcional na casa dos trinta. A semana em sete dias, todos com treino, e dois treinos em três deles. Ombro com dor há dois meses. Caixa de comprimidos: anti-inflamatório todo dia, para treinar, e pré-treino da internet. A companheira: não faltou nem no aniversário do filho. Perfil típico")]
rs = []
for j, d in enumerate(["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]):
    x = j * 132
    p.append(f'<rect x="{x}" y="40" width="118" height="110" rx="10" fill="{CARTAO}" stroke="{GRADE}" stroke-width="2"/>')
    p.append(f'<rect x="{x + 12}" y="{90 if j in (1, 3, 5) else 70}" width="94" height="{24 if j in (1, 3, 5) else 64}" rx="6" fill="{FOSF}"/>')
    if j in (1, 3, 5):
        p.append(f'<rect x="{x + 12}" y="120" width="94" height="24" rx="6" fill="{FOSF}"/>')
    rs.append(rot(x, 4, d, w=118, tam=22, cor=MUDO, peso=700, alinha="center"))
rs.append(rot(0, 158, "todo dia; dois treinos em três dias", w=910, tam=22, cor=FOSF, peso=700))
p.append(menino(110, 430, 220, TINTA))
p.append(f'<circle cx="137" cy="268" r="26" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(icone("t:barbell", 30, 196, 54, MUDO))
rs.append(rot(190, 236, "ombro: dor há dois meses", w=180, tam=22, cor=FOSF, peso=700, lh=1.2))
p.append(caixa(400, 210, 510, 230, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:pill", 424, 236, 56, GLIC))
p.append(icone("t:bolt", 424, 336, 56, GLIC))
rs += [rot(500, 236, "anti-inflamatório, todo dia, para treinar", w=390, tam=24, cor=TINTA, peso=700, lh=1.2),
       rot(500, 346, "pré-treino comprado na internet", w=390, tam=24, cor=TINTA, peso=700, lh=1.2)]
p.append(caixa(990, 40, 674, 260, AZUL, AZUL_T, esp=3, rx=24))
p.append(f'<path d="M 1060 300 L 1040 350 L 1110 300 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
p.append(f'<rect x="1058" y="294" width="56" height="10" fill="{AZUL_T}"/>')
rs += [rot(1020, 76, "“Não faltou ao treino nem no aniversário do filho.”", w=614, tam=32, cor=TINTA, peso=700, serif=True, lh=1.25),
       rot(1020, 224, "a companheira", w=614, tam=22, cor=AZUL, peso=700),
       rot(1130, 360, "Ele ri: “é disciplina”.", w=534, tam=28, cor=FOSF, peso=700, serif=True),
       rot(1130, 410, "perfil típico", w=534, tam=20, cor=MUDO)]
diagrama(S, "box", 440, p, rs, eyebrow="Treino funcional, sete dias por semana", titulo="Ele veio pelo ombro, e a consulta mostrou o resto")

# 2. as três saídas
p = [svg_abre(1664, 440, "Três saídas. A: elogiar a disciplina e tratar o ombro. B: dizer que é vício e mandar parar. C: separar duas perguntas, para que serve o treino e o que ele toma. Pergunta: o que decide o caminho?")]
rs = []
for j, (l, t, c, f) in enumerate([("A", "elogiar a disciplina e tratar o ombro", GLIC, GLIC_T),
                                   ("B", "dizer que é vício e mandar parar", FOSF, FOSF_T),
                                   ("C", "separar duas perguntas: para que serve o treino e o que ele toma", OXID, OXID_T)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 320, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 268}" cy="80" r="50" fill="{c}"/>')
    rs += [rot(x + 218, 52, l, w=100, tam=48, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(x + 28, 160, t, w=480, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Antes de escolher: o que separa dedicação de dependência", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saidas", 440, p, rs, eyebrow="A encruzilhada", titulo="Três jeitos de responder à mesma consulta")

# 3. dedicação e dependência
p = [svg_abre(1664, 450, "O mesmo calendário cheio vale para as duas colunas. Cinco perguntas. Quando não dá para treinar: dedicação frustra e reorganiza; dependência, ansiedade e culpa tomam o dia. Conflito com o resto da vida: negocia; o treino vence sempre. Treina com lesão: ajusta; mantém apesar do dano. Motivação: vai em direção a algo; foge de algo. Flexibilidade: troca a sessão; não consegue trocar")]
rs = []
X1, X2, W = 520, 1100, 564
p.append(caixa(X1, 0, W - 16, 450, OXID, OXID_T, esp=3, rx=18))
p.append(caixa(X2, 0, W, 450, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:calendar", 0, 0, 44, MUDO))
rs += [rot(56, 8, "o mesmo calendário cheio", w=440, tam=22, cor=MUDO, peso=700),
       rot(X1, 14, "Dedicação", w=W - 16, tam=30, cor=OXID, peso=700, serif=True, alinha="center"),
       rot(X2, 14, "Dependência", w=W, tam=30, cor=FOSF, peso=700, serif=True, alinha="center")]
for j, (q, a, b) in enumerate([("quando não dá para treinar", "frustra e reorganiza", "ansiedade e culpa tomam o dia"),
                               ("conflito com o resto da vida", "negocia", "o treino vence sempre"),
                               ("treina com lesão", "ajusta", "mantém apesar do dano"),
                               ("para onde aponta a motivação", "vai em direção a algo", "foge de algo"),
                               ("flexibilidade", "troca a sessão", "não consegue trocar")]):
    y = 76 + j * 74
    p.append(f'<line x1="0" y1="{y - 6}" x2="1664" y2="{y - 6}" stroke="{GRADE}" stroke-width="2"/>')
    rs += [rot(0, y + 10, q, w=500, tam=24, cor=TINTA, peso=700),
           rot(X1 + 20, y + 10, a, w=W - 56, tam=24, cor=OXID, peso=700, alinha="center"),
           rot(X2 + 20, y + 10, b, w=W - 40, tam=24, cor=FOSF, peso=700, alinha="center")]
diagrama(S, "funcao", 450, p, rs, eyebrow="Dedicação e dependência", titulo="O volume não separa os dois: a função do treino separa")

# 4. o questionário
p = [svg_abre(1664, 460, "Questionário de seis frases, cada uma com nota de 1 a 5: o treino é o mais importante da vida; brigas por causa do treino; treino para mudar o humor; a quantidade aumentou com o tempo; perder um treino irrita; tento reduzir e volto ao mesmo. Soma de 6 a 30; de 24 a 30, em risco. Rastreia, não diagnostica. Não é diagnóstico formal")]
rs = []
for j, t in enumerate(["o treino é o mais importante da vida", "brigas por causa do treino", "treino para mudar o humor",
                       "a quantidade aumentou com o tempo", "perder um treino irrita", "tento reduzir e volto ao mesmo"]):
    y = 10 + j * 72
    rs.append(rot(0, y + 6, t, w=520, tam=24, cor=TINTA, peso=700))
    for k in range(5):
        cx = 570 + k * 52
        p.append(f'<circle cx="{cx}" cy="{y + 22}" r="18" fill="{AZUL if k <= 3 - (j % 3) else CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
rs.append(rot(546, 440 - 14, "notas de 1 a 5, ilustrativas", w=300, tam=20, cor=MUDO))
X0, X9, Y = 900, 1640, 120
def px(v):
    return X0 + (v - 6) / 24 * (X9 - X0)
p.append(f'<rect x="{px(6):.0f}" y="{Y}" width="{px(24) - px(6):.0f}" height="44" rx="8" fill="{GRADE}"/>')
p.append(f'<rect x="{px(24):.0f}" y="{Y}" width="{px(30) - px(24):.0f}" height="44" rx="8" fill="{FOSF}"/>')
rs += [rot(px(6) - 30, Y + 54, "6", w=60, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(px(24) - 30, Y + 54, "24", w=60, tam=24, cor=FOSF, peso=700, alinha="center"),
       rot(px(30) - 30, Y + 54, "30", w=60, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(px(24) - 40, Y - 40, "em risco", w=200, tam=22, cor=FOSF, peso=700),
       rot(X0, 20, "a soma", w=600, tam=22, cor=MUDO, peso=700)]
p.append(caixa(X0, 250, X9 - X0 + 24, 190, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(X0 + 24, 272, "Rastreia, não diagnostica.", w=700, tam=32, cor=FOSF, peso=700, serif=True),
       rot(X0 + 24, 336, "Não é diagnóstico formal. O número abre a conversa; a entrevista decide.", w=700, tam=22, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "questionario", 460, p, rs, eyebrow="O questionário de seis frases", titulo="Seis frases rastreiam o risco, e quem decide é a entrevista",
         fonte="Addict Res Theory 2004")

# 5. o iceberg
p = [svg_abre(1664, 440, "Iceberg. Na ponta: treina demais. Debaixo da água: come pouco, peso e balança, imagem corporal, humor. Razão de chances 3,71, intervalo de 2,00 a 6,89, para dependência de exercício com e sem sinais de transtorno alimentar. Nove estudos, 2.140 participantes. Pergunte pela comida, pela balança e pelo corpo")]
rs = []
p.append(f'<rect x="0" y="120" width="700" height="320" fill="{AZUL_T}"/>')
p.append(f'<line x1="0" y1="120" x2="700" y2="120" stroke="{AZUL}" stroke-width="4"/>')
p.append(f'<polygon points="290,30 360,10 420,120 250,120" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4" stroke-linejoin="round"/>')
p.append(f'<polygon points="250,120 420,120 600,300 520,430 160,430 70,280" fill="{PAPEL}" stroke="{TINTA}" stroke-width="4" stroke-linejoin="round" opacity="0.9"/>')
rs.append(rot(430, 40, "treina demais", w=270, tam=26, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["come pouco", "peso e balança", "imagem corporal", "humor"]):
    rs.append(rot(160, 160 + j * 64, t, w=380, tam=26, cor=TINTA, peso=700, alinha="center"))
X0, X9, Y = 800, 1620, 150
def px(v):
    return X0 + v / 8 * (X9 - X0)
p.append(f'<line x1="{X0}" y1="{Y + 70}" x2="{X9}" y2="{Y + 70}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{px(1):.0f}" y1="{Y - 30}" x2="{px(1):.0f}" y2="{Y + 70}" stroke="{MUDO}" stroke-width="3" stroke-dasharray="8 6"/>')
p.append(f'<line x1="{px(2.00):.0f}" y1="{Y + 20}" x2="{px(6.89):.0f}" y2="{Y + 20}" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<circle cx="{px(3.71):.0f}" cy="{Y + 20}" r="18" fill="{FOSF}"/>')
rs += [rot(X0, 10, "razão de chances de dependência de exercício, com e sem sinais de transtorno alimentar", w=820, tam=22, cor=MUDO, peso=700, lh=1.25),
       rot(px(3.71) - 80, Y - 50, "3,71", w=160, tam=34, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(px(2.00) - 60, Y + 80, "2,00", w=120, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(px(6.89) - 60, Y + 80, "6,89", w=120, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(px(1) - 20, Y - 40, "1 = sem diferença", w=220, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(X0, Y + 130, "metanálise · 9 estudos · 2.140 participantes", w=820, tam=22, cor=MUDO, peso=700)]
p.append(caixa(X0, 340, 864, 100, OXID, OXID_T, esp=3, rx=16))
rs.append(rot(X0 + 24, 368, "Pergunte pela comida, pela balança e pelo corpo.", w=816, tam=28, cor=OXID, peso=700, serif=True))
diagrama(S, "iceberg", 440, p, rs, eyebrow="Dependência primária e secundária", titulo="Quando há dependência, o transtorno alimentar costuma estar embaixo",
         fonte="Eat Weight Disord 2020")

# 6. as saídas A e B
p = [svg_abre(1664, 440, "Saída A, elogiar e tratar o ombro: o ombro volta, o comprimido continua, o padrão ganha um aval. Saída B, é vício, pare: rótulo para um hobby sério, ele treina escondido, não volta à consulta. As duas respondem a uma pergunta que ninguém fez")]
rs = []
for j, (l, t, c, f, itens) in enumerate([("A", "elogiar e tratar o ombro", GLIC, GLIC_T, ["o ombro volta quando o treino volta", "o comprimido continua", "o padrão sai com um aval: disciplina"]),
                                          ("B", "“é vício, pare”", FOSF, FOSF_T, ["rótulo para um hobby sério", "a ordem que ele não consegue cumprir", "treina escondido e não volta"])]):
    x = j * 846
    p.append(caixa(x, 0, 818, 330, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 64}" cy="64" r="40" fill="{c}"/>')
    rs += [rot(x + 24, 40, l, w=80, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(x + 124, 42, t, w=670, tam=30, cor=TINTA, peso=700, serif=True)]
    for k, it in enumerate(itens):
        y = 140 + k * 62
        p.append(icone("t:x", x + 28, y, 40, c))
        rs.append(rot(x + 84, y + 4, it, w=710, tam=26, cor=TINTA, peso=700))
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "As duas respondem antes de perguntar.", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ab", 440, p, rs, eyebrow="As saídas A e B", titulo="Elogiar e proibir erram pelo mesmo motivo")

# 7. a largada
p = [svg_abre(1664, 440, "Maratona e meia maratona de Bonn, 2010. 3.913 corredores responderam. 49% tomaram analgésico antes da largada, a maioria para prevenir dor. Eventos adversos cerca de cinco vezes mais frequentes em quem tomou, e mais com a dose. Rim, sódio e estômago: a conversa sobre analgesia")]
rs = []
for k in range(20):
    x, y = (k % 10) * 84, (k // 10) * 130 + 60
    c = FOSF if k % 2 == 0 else MUDO
    p.append(corredor(x, y, 90, c))
    if c == FOSF:
        p.append(f'<circle cx="{x + 76}" cy="{y + 18}" r="10" fill="{GLIC}"/>')
rs += [rot(0, 4, "a cada dois corredores, um tomou", w=840, tam=22, cor=MUDO, peso=700),
       rot(0, 340, "3.913 corredores responderam depois da prova", w=840, tam=24, cor=TINTA, peso=700),
       rot(0, 386, "ponto amarelo: comprimido · esquema", w=840, tam=20, cor=MUDO)]
p.append(caixa(900, 0, 764, 200, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(924, 20, "49%", w=220, tam=72, cor=FOSF, peso=700, serif=True),
       rot(1150, 30, "tomaram analgésico antes da largada, a maioria para prevenir dor", w=490, tam=24, cor=TINTA, peso=700, lh=1.25)]
p.append(caixa(900, 220, 764, 120, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(924, 244, "eventos adversos cerca de 5× mais frequentes, e mais com a dose", w=716, tam=24, cor=TINTA, peso=700, lh=1.25))
p.append(icone("t:arrow-right", 900, 370, 44, OXID))
rs.append(rot(956, 376, "rim, sódio, estômago: a conversa sobre analgesia", w=708, tam=22, cor=OXID, peso=700))
diagrama(S, "largada", 440, p, rs, eyebrow="O comprimido antes do treino", titulo="Metade dos corredores tomou analgésico antes de sentir dor",
         fonte="BMJ Open 2013")

# 8. a entrevista pelo dia
p = [svg_abre(1664, 440, "Linha do dia: ao acordar, antes do treino, durante, depois, à noite, cada ponto com um espaço vazio. Três portas: de vez em quando, já usou e parou, alguém do treino te deu. Três cuidados: diga por que pergunta, peça a foto do rótulo, rosto neutro e nada corrigido no meio da lista"), defs(TINTA)]
rs = []
p.append(f'<line x1="40" y1="80" x2="1040" y2="80" stroke="{TINTA}" stroke-width="4"/>')
for j, (ic, t) in enumerate([("t:alarm", "ao acordar"), ("t:barbell", "antes do treino"), ("t:droplet", "durante"), ("t:coffee", "depois"), ("t:moon", "à noite")]):
    cx = 80 + j * 236
    p.append(f'<circle cx="{cx}" cy="80" r="40" fill="{AZUL}"/>')
    p.append(icone(ic, cx - 22, 58, 44, PAPEL))
    p.append(f'<rect x="{cx - 80}" y="170" width="160" height="56" rx="10" fill="none" stroke="{AZUL}" stroke-width="3"{TRACO}/>')
    rs.append(rot(cx - 110, 128, t, w=220, tam=22, cor=AZUL, peso=700, alinha="center"))
p.append(caixa(1160, 0, 504, 240, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(1184, 16, "Depois, três portas", w=456, tam=26, cor=GLIC, peso=700, serif=True))
for j, t in enumerate(["o que toma de vez em quando", "o que já usou e parou", "o que alguém do treino te deu"]):
    y = 72 + j * 54
    p.append(icone("t:door", 1184, y, 40, GLIC))
    rs.append(rot(1236, y + 6, t, w=410, tam=22, cor=TINTA, peso=700))
for j, (ic, t) in enumerate([("t:message-circle", "diga por que está perguntando"), ("t:camera-selfie", "peça a foto do rótulo"), ("t:mood-neutral", "rosto neutro: nada corrigido no meio")]):
    x = j * 564
    p.append(caixa(x, 290, 536, 150, OXID, OXID_T, esp=3, rx=16))
    p.append(icone(ic, x + 24, 330, 56, OXID))
    rs.append(rot(x + 96, 326, t, w=420, tam=24, cor=TINTA, peso=700, lh=1.25))
diagrama(S, "dia", 440, p, rs, eyebrow="O que ele toma", titulo="Pergunte pelo dia, não pela lista")

# 9. a saída C
p = [svg_abre(1664, 440, "Saída C: duas perguntas levam a três ramos. Seguir com ajuste: dedicação sem prejuízo; carga do ombro, analgésico fora da rotina, um dia livre combinado. Investigar a secundária: comida, balança, corpo, humor; roteiro da alimentação desordenada. Encaminhar: sofrimento sem treino, prejuízo que não para, hormônio na lista; fluxo de encaminhamento. O treino fica no plano; muda a função"), defs(TINTA)]
rs = []
p.append(caixa(0, 100, 360, 200, TINTA, CARTAO, esp=3, rx=18))
rs += [rot(24, 126, "Para que serve o treino?", w=312, tam=26, cor=TINTA, peso=700, serif=True, lh=1.2),
       rot(24, 210, "O que ele toma?", w=312, tam=26, cor=TINTA, peso=700, serif=True)]
for j, (t, q, a, c, f) in enumerate([("Seguir com ajuste", "dedicação, sem prejuízo", "carga do ombro, analgésico fora da rotina, dia livre combinado", OXID, OXID_T),
                                     ("Investigar a secundária", "comida, balança, corpo, humor", "o roteiro da alimentação desordenada", GLIC, GLIC_T),
                                     ("Encaminhar", "sofrimento, prejuízo que não para, hormônio", "o fluxo de encaminhamento", FOSF, FOSF_T)]):
    y = j * 128
    p.append(seta(360, 200, 444, y + 56, TINTA, "m0", esp=3))
    p.append(caixa(460, y, 1204, 112, c, f, esp=3, rx=16))
    rs += [rot(484, y + 16, t, w=360, tam=26, cor=c, peso=700, serif=True),
           rot(484, y + 60, q, w=360, tam=20, cor=MUDO, peso=700, lh=1.2),
           rot(870, y + 24, a, w=770, tam=24, cor=TINTA, peso=700, lh=1.25)]
rs.append(rot(0, 400, "Nos três ramos, o treino fica no plano; muda a função.", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"))
diagrama(S, "saida_c", 440, p, rs, eyebrow="A saída C", titulo="As duas perguntas levam a três caminhos, e nenhum tira o treino")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "Da planilha da elite ao treino que não pode faltar",
          "regras": ["Decisão: a medicina sobe a escada com pergunta, filtra o rastreio, dá o risco verdadeiro e separa dedicação de dependência; quem treina adapta o plano à semana real",
                     "Contribuição: o praticante que registra, o grupo do fim de semana, a organização da prova, o corredor que reanima, a família que percebe",
                     "Reconhecimento: a planilha da elite, quem só joga, o exame para tranquilizar, a semana com três mudanças, o comprimido para treinar"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Exame com pergunta, risco em prova, socorro, dor que persiste e dependência."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Plano que cabe na semana, força em volta do jogo, rampa e progressão pela sessão."},
                    {"ic": "t:users", "t": "Todos", "x": "Próximo módulo: integração, gestão e projeto aplicado."}]})

salvar("13-11.json", {"arquivo": "aulas/MOD13/13-11-dependencia-de-exercicio-e-automedicacao.md",
                      "titulo": "Dependência de exercício e automedicação", "subtitulo": "Três saídas para quem não consegue parar",
                      "nota_capa": "Entra por um praticante de treino funcional que treina todo dia, com dor. Fecha o módulo.",
                      "secoes": {"box": ["A decisão.", "capa"], "funcao": ["Dedicação e dependência.", "funcao"],
                                 "ab": ["As saídas e o que ele toma.", "ab"], "saida_c": ["A saída C.", "saida_c"],
                                 "fecho": ["O fecho do módulo.", "fecho"]},
                      "slides": S})
