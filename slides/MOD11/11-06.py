"""Spec do deck 11.6. Gera 11-06.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a temporada
p = [svg_abre(1664, 460, "Duas linhas ao longo de doze semanas de temporada. Uma sobe até mais 8,2 por cento: ciclo preservado. Outra desce até menos 9,8 por cento: ovário suprimido. Eixo vertical: variação da velocidade nos 400 metros")]
x0, x1, y0 = 160, 1180, 230
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="20" x2="{x0}" y2="440" stroke="{GRADE}" stroke-width="2"/>')
rs = [rot(0, y0 - 16, "0%", w=140, tam=24, cor=MUDO, alinha="right"), rot(0, 30, "mais rápida", w=140, tam=22, cor=MUDO, alinha="right", lh=1.2),
      rot(0, 390, "mais lenta", w=140, tam=22, cor=MUDO, alinha="right", lh=1.2),
      rot(x0, y0 + 190, "semana 0", w=200, tam=22, cor=MUDO), rot(x1 - 200, y0 + 190, "semana 12", w=200, tam=22, cor=MUDO, alinha="right")]
k = 160 / 9.8
p.append(f'<path d="M {x0} {y0} C 500 {y0} 800 {y0 - 8.2 * k:.0f} {x1} {y0 - 8.2 * k:.0f}" stroke="{OXID}" stroke-width="7" fill="none"/>')
p.append(f'<path d="M {x0} {y0} C 500 {y0} 800 {y0 + 9.8 * k:.0f} {x1} {y0 + 9.8 * k:.0f}" stroke="{FOSF}" stroke-width="7" fill="none"/>')
p.append(f'<circle cx="{x1}" cy="{y0 - 8.2 * k:.0f}" r="12" fill="{OXID}"/><circle cx="{x1}" cy="{y0 + 9.8 * k:.0f}" r="12" fill="{FOSF}"/>')
rs += [rot(1210, y0 - 8.2 * k - 46, "+8,2%", w=440, tam=48, cor=OXID, peso=700, serif=True), rot(1210, y0 - 8.2 * k + 10, "ciclo preservado", w=440, tam=26, cor=TINTA, peso=600),
       rot(1210, y0 + 9.8 * k - 46, "−9,8%", w=440, tam=48, cor=FOSF, peso=700, serif=True), rot(1210, y0 + 9.8 * k + 10, "ovário suprimido", w=440, tam=26, cor=TINTA, peso=600)]
diagrama(S, "temporada", 460, p, rs, eyebrow="Uma ciclista parada no rolo; uma temporada de natação", titulo="Mesmo treino, direções opostas: a supressão aparece na planilha",
         fonte="Velocidade nos 400 m livres, 12 semanas; Med Sci Sports Exerc 2014")

# 2. a amostra
p = [svg_abre(1664, 440, "Dez figuras de nadadoras adolescentes separadas em dois grupos pelo estradiol e pela progesterona. Embaixo do grupo suprimido, quatro setas para baixo no fim da temporada: ingestão, disponibilidade energética, T3, IGF-1. Etiqueta: observacional, dez atletas"), defs(FOSF)]
rs = []
for g, (t, c, f) in enumerate([("ciclo preservado", OXID, OXID_T), ("ovário suprimido", FOSF, FOSF_T)]):
    x = g * 520
    p.append(caixa(x, 0, 480, 200, c, f, esp=3, rx=16))
    rs.append(rot(x + 20, 16, t, w=440, tam=28, cor=c, peso=700, serif=True))
    for i in range(5):
        p.append(icone("h:people" if False else "t:user", x + 30 + i * 88, 80, 70, c))
rs.append(rot(0, 220, "separadas por estradiol e progesterona dosados na temporada", w=1000, tam=24, cor=MUDO))
for j, t in enumerate(["ingestão", "disponibilidade energética", "T3", "IGF-1"]):
    x = 520 + (j % 2) * 260
    y = 280 + (j // 2) * 74
    p.append(seta(x + 20, y, x + 20, y + 50, FOSF, "m0", 5))
    rs.append(rot(x + 44, y + 8, t, w=220, tam=24, cor=TINTA, peso=600, lh=1.15))
rs.append(rot(0, 300, "no fim da temporada, no grupo suprimido:", w=500, tam=26, cor=FOSF, peso=700, lh=1.25))
p.append(caixa(1100, 60, 564, 300, TINTA, PAPEL, esp=2, rx=18))
rs += [rot(1124, 90, "observacional", w=520, tam=34, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(1124, 160, "dez atletas, de 15 a 17 anos", w=520, tam=26, cor=TINTA, alinha="center"),
       rot(1124, 230, "não sorteadas para comer menos", w=520, tam=26, cor=MUDO, alinha="center")]
diagrama(S, "amostra", 440, p, rs, eyebrow="Em quem foi medido", titulo="Dez atletas; no grupo suprimido, um corpo poupando energia")

# 3. mil atletas
p = [svg_abre(1664, 440, "Uma grade de mil pontos, parte deles destacada como sinais de baixa disponibilidade. Ao lado, o número 2,1 vezes: chance de relatar resposta ao treino reduzida. Embaixo: transversal, autorrelatado")]
dots = {GLIC: [], CINZA: []}
for i in range(1000):
    r_, c_ = divmod(i, 40)
    dots[GLIC if (i * 37) % 100 < 40 else CINZA].append(f"M{10 + c_ * 22} {10 + r_ * 16}h0")
for cor, d in dots.items():
    p.append(f'<path d="{"".join(d)}" stroke="{cor}" stroke-width="12" stroke-linecap="round"/>')
rs = [rot(0, 410, "esquema: a proporção destacada é ilustrativa", w=880, tam=22, cor=MUDO)]
p.append(caixa(960, 20, 704, 380, GLIC, GLIC_T, esp=3, rx=18))
rs += [rot(984, 50, "2,1×", w=656, tam=120, cor=GLIC, peso=700, serif=True, alinha="center"),
       rot(984, 210, "chance de relatar resposta ao treino reduzida", w=656, tam=30, cor=TINTA, peso=700, alinha="center", lh=1.25),
       rot(984, 330, "transversal · autorrelatado", w=656, tam=24, cor=MUDO, alinha="center")]
diagrama(S, "mil", 440, p, rs, eyebrow="Levantamento de 2019, 1.000 atletas mulheres", titulo="A mesma direção numa amostra cem vezes maior",
         fonte="Br J Sports Med 2019")

# 4. as janelas
p = [svg_abre(1664, 470, "Cinco janelas, uma por profissional, cada uma com o que se vê dali. Treinador: platô com treino cumprido, recuperação lenta, sessões perdidas por doença. Preparação física: potência e força paradas. Fisioterapia: dor óssea localizada, lesões que se repetem. Nutrição: refeição pulada perto do treino, cardápio encolhendo. Vestiário e viagem: frio constante, comer separado, irritabilidade")]
jan = [("t:stopwatch", "Treinador", ["platô com treino cumprido", "recuperação lenta", "sessões perdidas por doença"]),
       ("t:bolt", "Preparação", ["potência parada", "força parada"]),
       ("h:doctor", "Fisioterapia", ["dor óssea localizada", "lesões que se repetem"]),
       ("t:salad", "Nutrição", ["refeição pulada perto do treino", "cardápio encolhendo"]),
       ("t:users", "Vestiário", ["frio constante", "come separado", "irritabilidade"])]
rs = []
for j, (ic, t, itens) in enumerate(jan):
    x = j * 338
    p.append(caixa(x, 0, 310, 380, AZUL, CARTAO, esp=3, rx=16))
    p.append(f'<rect x="{x}" y="0" width="310" height="96" rx="16" fill="{AZUL_T}"/>')
    p.append(icone(ic, x + 18, 22, 52, AZUL))
    rs.append(rot(x + 82, 30, t, w=220, tam=26, cor=AZUL, peso=700))
    for i, it in enumerate(itens):
        rs.append(rot(x + 20, 120 + i * 84, it, w=276, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(caixa(0, 404, 1664, 66, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 420, "Nenhum sinal sozinho diz deficiência energética: o que pesa é a soma", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "janelas", 470, p, rs, eyebrow="O que se vê sem exame", titulo="Os sinais estão espalhados por várias janelas, e só a soma pesa")

# 5. o questionário
p = [svg_abre(1664, 460, "O questionário em três blocos com cortes parciais: lesões, 2 ou mais; sintomas gastrointestinais, 2 ou mais; função menstrual, 4 ou mais. Total: 25 itens, corte 8 ou mais. Sensibilidade 78 por cento, especificidade 90 por cento. Sob contracepção hormonal, o bloco menstrual perde valor")]
rs = []
blocos = [("Lesões", "≥2", OXID), ("Gastrointestinal", "≥2", GLIC), ("Função menstrual", "≥4", FOSF)]
for j, (t, c_, c) in enumerate(blocos):
    x = j * 330
    p.append(caixa(x, 0, 300, 230, c, CARTAO, esp=4, rx=16))
    rs += [rot(x + 16, 24, t, w=268, tam=28, cor=c, peso=700, alinha="center", lh=1.2), rot(x + 16, 120, c_, w=268, tam=60, cor=TINTA, peso=700, serif=True, alinha="center")]
p.append(f'<rect x="660" y="236" width="300" height="70" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
rs.append(rot(670, 244, "sob contracepção hormonal, perde valor", w=280, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
p.append(caixa(0, 330, 960, 130, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(24, 360, "25 itens · total ≥8 · rastreio, não diagnóstico", w=912, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True))
for j, (n, t) in enumerate([("78%", "das que tinham o problema"), ("90%", "das que não tinham")]):
    y = j * 160
    rs += [rot(1040, y + 10, n, w=260, tam=72, cor=AZUL, peso=700, serif=True), rot(1300, y + 36, t, w=360, tam=26, cor=TINTA, peso=600, lh=1.2)]
p.append(caixa(1020, 330, 644, 130, MUDO, PAPEL, esp=2, rx=16))
rs.append(rot(1044, 350, "validado em 45 atletas de endurance; outros esportes, menos estudado", w=600, tam=24, cor=TINTA, lh=1.3))
diagrama(S, "questionario", 460, p, rs, eyebrow="Questionário de 2014, feito para mulheres que treinam", titulo="Vinte e cinco perguntas que qualquer profissional pode aplicar",
         fonte="Br J Sports Med 2014")

# 6. a conversa
p = [svg_abre(1664, 440, "Duas colunas de frases. Abre a conversa: rendimento que caiu com treino mantido, recuperação, ciclo, energia para treinar. Fecha a conversa: peso, corpo, você está muito magra, você está comendo pouco, elogio à forma. Embaixo: em particular, pelo funcional")]
rs = []
for k, (t, itens, c, f, ic) in enumerate([("Abre a conversa", ["o rendimento parou com tudo cumprido", "como está a recuperação?", "como está o seu ciclo?", "tem energia para treinar?"], OXID, OXID_T, "t:check"),
                                          ("Fecha a conversa", ["peso, forma, corpo", "“você está muito magra”", "“você está comendo pouco”", "elogio à forma"], FOSF, FOSF_T, "t:x")]):
    x = k * 864
    p.append(caixa(x, 0, 800, 340, c, f, esp=3, rx=18))
    rs.append(rot(x + 28, 20, t, w=740, tam=32, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 40, 96 + j * 60, "· " + it, w=740, tam=27, cor=TINTA, peso=600))
p.append(caixa(0, 370, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 386, "Em particular, pelo funcional, sem falar do corpo", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "conversa", 440, p, rs, eyebrow="Como se puxa o assunto", titulo="O rendimento abre a conversa; o corpo a fecha")

# 7. o encaminhamento
p = [svg_abre(1664, 480, "Um cartão de encaminhamento com seis linhas: modalidade e volume semanal; o que mudou em doze meses; ciclo e método contraceptivo; dor óssea ou lesões de repetição; tendência do rendimento; pontuação do questionário. Ao lado, um encaminhamento vazio: avaliar atleta, cansada, riscado")]
p.append(caixa(0, 0, 1060, 480, TINTA, CARTAO, esp=2, rx=16))
rs = [rot(30, 20, "Encaminhamento", w=600, tam=30, cor=TINTA, peso=700, serif=True), rot(640, 26, "para: medicina do esporte", w=390, tam=22, cor=MUDO, alinha="right")]
linhas = ["modalidade e volume semanal, contando tudo", "o que mudou em doze meses: treino e prato", "ciclo: intervalo e método contraceptivo",
          "dor óssea e lesões de repetição", "tendência do rendimento, com números", "questionário: pontuação"]
for j, t in enumerate(linhas):
    y = 90 + j * 64
    p.append(f'<circle cx="52" cy="{y + 18}" r="16" fill="{OXID}"/>')
    rs += [rot(36, y + 4, str(j + 1), w=32, tam=22, cor=PAPEL, peso=700, alinha="center"), rot(86, y, t, w=950, tam=26, cor=TINTA, peso=600)]
p.append(caixa(1120, 100, 544, 200, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1144, 150, "“avaliar atleta, cansada”", w=496, tam=30, cor=TINTA, alinha="center", serif=True))
p.append(f'<line x1="1150" y1="250" x2="1634" y2="150" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(1120, 320, "a consulta começa do zero", w=544, tam=26, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "encaminhamento", 480, p, rs, eyebrow="O que mais ajuda quem recebe", titulo="Seis linhas fazem a consulta começar pelo meio")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Reconhecer a deficiência energética fora do consultório médico", "titulo": "Antes de acrescentar volume, pergunte",
          "regras": ["Platô com treino mantido: pergunte por energia e ciclo antes de subir o volume",
                     "Os sinais estão em várias janelas; junte as janelas",
                     "O questionário rastreia: positivo encaminha, negativo com sinais não encerra"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Nota o rendimento, pergunta e encaminha com as seis linhas."},
                    {"ic": "t:salad", "t": "Nutrição e reabilitação", "x": "Somam o prato e o tecido, e podem aplicar o questionário."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Recebe o encaminhamento e investiga."}]})

salvar("11-06.json", {"arquivo": "aulas/MOD11/11-06-reconhecer-a-deficiencia-energetica-fora-do-consultorio-medico.md",
                      "titulo": "Reconhecer a deficiência energética fora do consultório médico", "subtitulo": "O que se vê do treino, do prato e do vestiário",
                      "nota_capa": "Entra por uma ciclista parada no rolo e por um número de rendimento.",
                      "secoes": {"temporada": ["O número.", "capa"], "janelas": ["O que cada um vê.", "janelas"],
                                 "conversa": ["Falar e encaminhar.", "conversa"]},
                      "slides": S})
