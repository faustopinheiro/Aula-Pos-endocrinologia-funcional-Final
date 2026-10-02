"""Spec do deck 11.9. Gera 11-09.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o ruído
p = [svg_abre(1664, 420, "Uma praticante de treinamento funcional, grávida, na porta do box. Em volta, quatro balões que se contradizem: pode caminhar; só com liberação por escrito; é perigoso levantar peso; não levante o braço acima da cabeça. Embaixo, quatro semanas riscadas: sem treino")]
p.append(icone("h:woman", 712, 60, 240, GLIC))
rs = []
baloes = [(0, 0, "“pode caminhar”"), (1124, 0, "“só com liberação por escrito”"), (0, 180, "“é perigoso levantar peso”"), (1124, 180, "“não levante o braço acima da cabeça”")]
for x, y, t in baloes:
    p.append(caixa(x, y, 540, 140, MUDO, CARTAO, esp=2, rx=40))
    rs.append(rot(x + 30, y + 40, t, w=480, tam=28, cor=TINTA, peso=600, alinha="center", serif=True, lh=1.2))
for i in range(4):
    x = 560 + i * 140
    p.append(f'<rect x="{x}" y="356" width="110" height="56" rx="8" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    p.append(f'<line x1="{x + 10}" y1="402" x2="{x + 100}" y2="366" stroke="{FOSF}" stroke-width="4"/>')
rs.append(rot(1140, 368, "quatro semanas sem treino", w=520, tam=26, cor=FOSF, peso=700))
diagrama(S, "ruido", 420, p, rs, eyebrow="Catorze semanas de gestação", titulo="Na gestação sem complicação, ficar parada não é a opção segura",
         destaque="Seguir a recomendação: cerca de 40% menos diabetes gestacional, hipertensão e pré-eclâmpsia; ao menos 25% menos depressão.", destaque_cor="tinta",
         fonte="Diretriz canadense, Br J Sports Med 2018")

# 2. a pergunta específica
p = [svg_abre(1664, 470, "Passo um. Dois balões: vago, pode treinar?; específico, agachamento com carga moderada e corrida em ritmo de conversa, três vezes por semana, trinta minutos, está liberado? Embaixo, não liberado diferente de contraindicado. Ao lado, contraindicações decididas pela obstetrícia")]
rs = []
p.append(caixa(0, 0, 360, 130, FOSF, FOSF_T, esp=3, rx=40))
rs.append(rot(20, 40, "“pode treinar?”", w=320, tam=30, cor=FOSF, peso=700, alinha="center", serif=True))
p.append(caixa(400, 0, 600, 200, OXID, OXID_T, esp=3, rx=40))
rs.append(rot(430, 26, "“agachamento moderado e corrida em ritmo de conversa, 3 vezes por semana, 30 minutos: liberado?”", w=540, tam=26, cor=OXID, peso=700, alinha="center", lh=1.3))
for k, t in enumerate(["não liberado", "contraindicado"]):
    x = k * 560
    p.append(caixa(x, 280, 440, 110, TINTA, CARTAO, esp=2, rx=14))
    rs.append(rot(x + 20, 312, t, w=400, tam=32, cor=TINTA, peso=700, alinha="center", serif=True))
p.append(f'<line x1="470" y1="322" x2="530" y2="322" stroke="{FOSF}" stroke-width="6"/><line x1="470" y1="346" x2="530" y2="346" stroke="{FOSF}" stroke-width="6"/><line x1="490" y1="370" x2="512" y2="300" stroke="{FOSF}" stroke-width="5"/>')
rs.append(rot(0, 410, "a maioria das “não liberadas” nunca teve a pergunta feita", w=1000, tam=24, cor=MUDO))
p.append(caixa(1060, 0, 604, 470, MUDO, PAPEL, esp=2, rx=16))
rs.append(rot(1084, 18, "Contraindicações: decide a obstetrícia", w=560, tam=26, cor=TINTA, peso=700, lh=1.2))
for j, t in enumerate(["membranas rotas, trabalho de parto prematuro", "sangramento persistente sem explicação", "placenta prévia após 28 semanas", "pré-eclâmpsia, colo incompetente", "restrição de crescimento fetal", "doenças descontroladas"]):
    rs.append(rot(1084, 100 + j * 60, "· " + t, w=560, tam=22, cor=TINTA, peso=600))
diagrama(S, "pergunta", 470, p, rs, eyebrow="Passo um", titulo="Pergunte à obstetrícia de forma específica")

# 3. a dose
p = [svg_abre(1664, 440, "Passo dois, a dose em quatro blocos: 150 minutos por semana; 3 dias ou mais; aeróbico e força; assoalho pélvico todo dia. Já treinava: continua, com ajustes. Sedentária: pode começar, com progressão")]
rs = []
for j, (n, t, ic) in enumerate([("150", "minutos por semana, moderado", "t:stopwatch"), ("3+", "dias por semana", "t:calendar"), ("2", "aeróbico e força, juntos", "t:bolt"), ("1×", "assoalho pélvico, todo dia", "t:check")]):
    x = j * 420
    p.append(caixa(x, 0, 390, 260, OXID, OXID_T, esp=3, rx=18))
    rs += [rot(x + 20, 30, n, w=350, tam=80, cor=OXID, peso=700, serif=True, alinha="center"), rot(x + 20, 160, t, w=350, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.25)]
for k, (t, c) in enumerate([("já treinava: continua, com ajustes", AZUL), ("sedentária: pode começar, com progressão", GLIC)]):
    x = k * 840
    p.append(caixa(x, 300, 824, 90, c, CARTAO, esp=3, rx=14))
    rs.append(rot(x + 20, 326, t, w=784, tam=28, cor=c, peso=700, alinha="center"))
rs.append(rot(0, 404, "elite com volume e intensidade muito altos: menos dados, conversa obrigatória com a obstetrícia", w=1664, tam=22, cor=MUDO, alinha="center"))
diagrama(S, "dose", 440, p, rs, eyebrow="Passo dois", titulo="A dose: 150 minutos, força incluída, assoalho pélvico todo dia",
         fonte="Diretriz canadense, Br J Sports Med 2018")

# 4. os ajustes
p = [svg_abre(1664, 470, "Passo três. Quatro pares, mudança e ajuste. Frequência de repouso sobe: teste da fala. Centro de massa muda: cuidado com queda, não com força. Tontura deitada de costas: mudar de posição. Calor e glicemia: ambiente ventilado, comer antes. Fica a força; saem contato, queda, mergulho autônomo e Valsalva sustentada"), defs(TINTA)]
rs = []
pares = [("frequência de repouso sobe", "guiar pelo teste da fala"), ("centro de massa muda", "evitar queda, não força"),
         ("tontura deitada de costas", "mudar de posição"), ("calor e glicemia oscilam", "ventilação e comer antes")]
for j, (a, b) in enumerate(pares):
    x, y = (j % 2) * 840, (j // 2) * 160
    p.append(caixa(x, y, 360, 130, GLIC, GLIC_T, esp=2, rx=14))
    rs.append(rot(x + 16, y + 30, a, w=328, tam=26, cor=GLIC, peso=700, alinha="center", lh=1.2))
    p.append(seta(x + 370, y + 65, x + 430, y + 65, TINTA, "m0", 4))
    p.append(caixa(x + 440, y, 380, 130, OXID, OXID_T, esp=2, rx=14))
    rs.append(rot(x + 456, y + 30, b, w=348, tam=26, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append(caixa(0, 340, 800, 130, OXID, CARTAO, esp=3, rx=14))
rs += [rot(24, 356, "Fica", w=760, tam=28, cor=OXID, peso=700, serif=True), rot(24, 404, "treino de força, carga adequada, progressão", w=760, tam=26, cor=TINTA, peso=600)]
p.append(caixa(864, 340, 800, 130, FOSF, CARTAO, esp=3, rx=14))
rs += [rot(888, 356, "Sai", w=760, tam=28, cor=FOSF, peso=700, serif=True), rot(888, 404, "contato, queda, mergulho autônomo, Valsalva sustentada", w=760, tam=26, cor=TINTA, peso=600)]
diagrama(S, "ajustes", 470, p, rs, eyebrow="Passo três", titulo="O corpo mudou: muda o guia, não a força")

# 5. sinais para parar
p = [svg_abre(1664, 440, "Passo quatro. Painel de sinais para parar: sangramento vaginal; perda de líquido; dor abdominal persistente; contrações regulares e dolorosas; falta de ar antes do esforço; tontura ou desmaio; dor de cabeça; dor no peito; fraqueza com perda de equilíbrio; dor ou inchaço na panturrilha. Parar e procurar a obstetrícia")]
rs = []
sinais = ["sangramento vaginal", "perda de líquido", "dor abdominal persistente", "contrações regulares e dolorosas", "falta de ar antes do esforço",
          "tontura ou desmaio", "dor de cabeça", "dor no peito", "fraqueza com perda de equilíbrio", "dor ou inchaço na panturrilha"]
for j, t in enumerate(sinais):
    x, y = (j % 2) * 840, (j // 2) * 68
    p.append(f'<rect x="{x}" y="{y}" width="820" height="56" rx="10" fill="{FOSF_T}"/>')
    p.append(icone("t:alert-triangle", x + 12, y + 8, 40, FOSF))
    rs.append(rot(x + 66, y + 13, t, w=740, tam=26, cor=TINTA, peso=600))
p.append(caixa(0, 360, 1664, 80, FOSF, FOSF, esp=0, rx=14))
rs.append(rot(20, 382, "Qualquer um: parar e procurar a obstetrícia, sem esperar a próxima consulta", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "parar", 440, p, rs, eyebrow="Passo quatro", titulo="Dez sinais que qualquer um na sala precisa saber de cor")

# 6. o pós-parto
p = [svg_abre(1664, 470, "Passo cinco. Linha do tempo do pós-parto. Semana zero: respiração, assoalho pélvico, caminhada curta. Semanas duas a seis: caminhada progressiva, carga leve. Semana seis: revisão, começa a progressão, bandeira de largada. Semana doze: impacto e corrida, por critério. Critérios: sem perda urinária, sem peso ou pressão vaginal, sem dor, testes de impacto tolerados. Cesárea: mais tempo para carga no abdome. Esquema")]
W = lambda s: {0: 40, 2: 330, 6: 640, 12: 1010, 14: 1100}[s]
p.append(f'<line x1="{W(0):.0f}" y1="200" x2="{W(14):.0f}" y2="200" stroke="{TINTA}" stroke-width="4"/>')
rs = []
fases = [(0, 2, "respiração, assoalho, caminhada curta", GLIC_T), (2, 6, "caminhada progressiva, carga leve", GLIC_T), (6, 12, "força progressiva, assoalho avaliado", OXID_T)]
for a, b, t, f in fases:
    p.append(f'<rect x="{W(a) + 4:.0f}" y="230" width="{W(b) - W(a) - 8:.0f}" height="120" rx="12" fill="{f}"/>')
    rs.append(rot(W(a) + 12, 248, t, w=W(b) - W(a) - 24, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.25))
for s, t, c in ((0, "parto", TINTA), (6, "revisão: largada", OXID), (12, "impacto, por critério", FOSF)):
    p.append(f'<circle cx="{W(s):.0f}" cy="200" r="14" fill="{c}"/>')
    rs.append(rot(W(s) - 20 if s == 0 else W(s) - 140, 130, t, w=280, tam=24, cor=c, peso=700, alinha="left" if s == 0 else "center"))
    rs.append(rot(W(s) - 60, 360, f"semana {s}", w=120, tam=22, cor=MUDO, alinha="center"))
p.append(caixa(1180, 0, 484, 400, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1204, 20, "Critérios para o impacto", w=440, tam=28, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["sem perda urinária no esforço", "sem peso ou pressão vaginal", "sem dor", "testes de impacto e força tolerados"]):
    rs.append(rot(1204, 90 + j * 70, "· " + t, w=440, tam=24, cor=TINTA, peso=600, lh=1.2))
rs += [rot(0, 420, "cesárea: mais tempo antes de carga no abdome · esquema", w=1100, tam=22, cor=MUDO),
       rot(1180, 420, "não antes de três meses", w=484, tam=24, cor=FOSF, peso=700, alinha="center")]
diagrama(S, "posparto", 470, p, rs, eyebrow="Passo cinco", titulo="Seis semanas é largada; o impacto vem por critério",
         fonte="Orientação britânica de retorno à corrida no pós-parto, 2019")

# 7. o assoalho pélvico
p = [svg_abre(1664, 460, "Passo seis. Três perguntas: perde urina quando tosse, espirra, salta ou corre? Sente peso, pressão ou uma bola na vagina? Sente dor na relação? Seta para fisioterapia pélvica. Duas armadilhas: faça Kegel não é prescrição; assoalho tenso, contrair mais piora"), defs(OXID)]
rs = []
for j, t in enumerate(["Perde urina quando tosse, espirra, salta ou corre?", "Sente peso, pressão ou uma bola na vagina?", "Sente dor na relação?"]):
    y = j * 100
    p.append(caixa(0, y, 1000, 84, AZUL, AZUL_T, esp=3, rx=14))
    rs.append(rot(24, y + 22, t, w=952, tam=28, cor=AZUL, peso=700, serif=True))
p.append(seta(1010, 140, 1110, 140, OXID, "m0", 6))
p.append(caixa(1120, 60, 544, 160, OXID, OXID_T, esp=4, rx=16))
rs += [rot(1140, 84, "qualquer sim", w=504, tam=26, cor=TINTA, alinha="center"), rot(1140, 132, "fisioterapia pélvica", w=504, tam=34, cor=OXID, peso=700, serif=True, alinha="center")]
for k, t in enumerate(["“faça Kegel” não é prescrição: muitas contraem o músculo errado", "assoalho tenso, com dor: contrair mais piora"]):
    x = k * 840
    p.append(caixa(x, 330, 824, 130, FOSF, FOSF_T, esp=2, rx=14))
    p.append(icone("t:alert-triangle", x + 20, 362, 52, FOSF))
    rs.append(rot(x + 90, 352, t, w=710, tam=26, cor=TINTA, peso=600, lh=1.3))
diagrama(S, "assoalho", 460, p, rs, eyebrow="Passo seis", titulo="Três perguntas, a toda mulher que treina")

# 8. lactação e energia
p = [svg_abre(1664, 450, "Balança de energia da puérpera. De um lado, o prato. Do outro, treino, amamentação e sono fragmentado. Ao lado, um calendário sem menstruação: esperado durante a amamentação. Faixa: o vértice do ciclo não serve aqui; os outros dois servem")]
p.append(f'<line x1="100" y1="120" x2="900" y2="200" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<path d="M 500 160 l -50 200 l 100 0 z" fill="{TINTA}"/>')
p.append(f'<ellipse cx="180" cy="110" rx="110" ry="26" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
rs = [rot(80, 30, "o prato", w=200, tam=28, cor=GLIC, peso=700, alinha="center")]
for j, t in enumerate(["treino", "amamentação", "sono picado"]):
    p.append(f'<rect x="{660 + j * 80}" y="{150 - j * 0}" width="70" height="{50 + j * 10}" rx="8" fill="{FOSF}" transform="translate(0,{j * 8})"/>')
rs.append(rot(600, 240, "treino · amamentação · sono fragmentado", w=420, tam=24, cor=FOSF, peso=700, alinha="center", lh=1.2))
p.append(caixa(1100, 0, 564, 300, AZUL, CARTAO, esp=3, rx=16))
for i in range(3):
    for j in range(7):
        p.append(f'<rect x="{1130 + j * 72}" y="{40 + i * 60}" width="60" height="48" rx="6" fill="{BORDA}"/>')
rs.append(rot(1124, 232, "sem menstruar: esperado durante a amamentação", w=516, tam=24, cor=AZUL, peso=700, alinha="center", lh=1.2))
p.append(caixa(0, 340, 1664, 110, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(20, 370, "O vértice do ciclo fica apagado por um motivo normal: osso, lesões e rendimento pesam mais", w=1624, tam=27, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "lactacao", 450, p, rs, eyebrow="Amamentação, energia e sono", titulo="No pós-parto, a deficiência energética perde o alarme habitual")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Exercício na gestação e no pós-parto", "titulo": "Parar não é neutro; voltar tem critério",
          "regras": ["Gestação sem complicação: pergunta específica à obstetrícia e a dose prescrita",
                     "Seis semanas é largada: impacto não antes de três meses, e só por critério",
                     "Assoalho pélvico: três perguntas a toda mulher que treina; qualquer sim encaminha"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Ajusta o treino, sabe os sinais para parar e leva a pergunta específica."},
                    {"ic": "h:doctor-female", "t": "Fisioterapia pélvica", "x": "Avalia e trata o assoalho e define o critério para o impacto."},
                    {"ic": "h:doctor", "t": "Obstetrícia", "x": "Decide as contraindicações e acompanha a gestação."}]})

salvar("11-09.json", {"arquivo": "aulas/MOD11/11-09-exercicio-na-gestacao-e-no-pos-parto.md",
                      "titulo": "Exercício na gestação e no pós-parto", "subtitulo": "Um roteiro em seis passos",
                      "nota_capa": "Entra por uma praticante parada na porta do box por excesso de frases.",
                      "secoes": {"ruido": ["O ruído.", "capa"], "pergunta": ["A gestação.", "pergunta"],
                                 "posparto": ["O pós-parto.", "posparto"]},
                      "slides": S})
