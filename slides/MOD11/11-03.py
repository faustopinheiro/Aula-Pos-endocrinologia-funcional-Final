"""Spec do deck 11.3. Gera 11-03.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o calendário da nadadora
p = [svg_abre(1664, 470, "Um calendário de doze meses de natação, com os treinos marcados em azul. Em cada mês, dois ou três dias seguidos em branco, sempre no começo do sangramento. Ao lado, a conta: dois dias e meio por mês são trinta dias por ano, um mês de treino perdido")]
rs = []
for m in range(12):
    x, y = (m % 6) * 172, (m // 6) * 230
    p.append(caixa(x, y, 156, 210, MUDO, CARTAO, esp=2, rx=10))
    falta = {(m * 3) % 20 + 2, (m * 3) % 20 + 3} | ({(m * 3) % 20 + 4} if m % 2 else set())
    for d in range(28):
        c = PAPEL if d in falta else AZUL
        p.append(f'<rect x="{x + 10 + (d % 7) * 20}" y="{y + 50 + (d // 7) * 38}" width="16" height="30" rx="3" fill="{c}" stroke="{AZUL}" stroke-width="1.5"/>')
    rs.append(rot(x, y + 10, ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"][m], w=156, tam=22, cor=MUDO, peso=700, alinha="center"))
p.append(caixa(1080, 0, 584, 470, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1110, 30, "2,5 dias por mês × 12", w=530, tam=30, cor=TINTA, peso=700),
       rot(1110, 100, "30 dias", w=530, tam=80, cor=FOSF, peso=700, serif=True),
       rot(1110, 220, "um mês inteiro de treino por ano, há quase vinte anos", w=530, tam=26, cor=TINTA, lh=1.3),
       rot(1110, 350, "“É assim, todo mundo tem.”", w=530, tam=30, cor=FOSF, peso=700, serif=True)]
diagrama(S, "calendario", 470, p, rs, eyebrow="Uma nadadora e os dias em branco", titulo="O hormônio pesa pouco; o sintoma tira um mês por ano")

# 2. a balança
p = [svg_abre(1664, 470, "Uma balança. No prato leve, o efeito da fase, um peso pequeno. No prato pesado, os sintomas empilhados com as frequências de um levantamento de 2021: humor ou ansiedade 91%, cansaço 86%, cólica 84%, dor nas mamas 83%. Embaixo: quanto mais sintomas, mais treino perdido ou alterado")]
p.append(f'<polygon points="832,440 792,470 872,470" fill="{TINTA}"/>')
p.append(f'<line x1="832" y1="440" x2="832" y2="150" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<line x1="320" y1="90" x2="1344" y2="210" stroke="{TINTA}" stroke-width="8"/>')
rs = []
p.append(f'<line x1="320" y1="90" x2="320" y2="130" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 180 130 L 460 130 L 420 170 L 220 170 Z" fill="{CINZA}"/>')
p.append(f'<rect x="290" y="100" width="60" height="30" rx="6" fill="{MUDO}"/>')
rs.append(rot(150, 186, "efeito da fase: trivial", w=340, tam=26, cor=MUDO, peso=700, alinha="center"))
p.append(f'<line x1="1344" y1="210" x2="1344" y2="420" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 1104 420 L 1584 420 L 1544 466 L 1144 466 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
for j, (t, v) in enumerate([("humor ou ansiedade", 91), ("cansaço", 86), ("cólica", 84), ("dor nas mamas", 83)]):
    y = 372 - j * 48
    p.append(f'<rect x="1164" y="{y}" width="360" height="42" rx="8" fill="{FOSF}" opacity="1"/>')
    rs.append(rot(1176, y + 7, f"{t} · {v}%", w=340, tam=23, cor=PAPEL, peso=700))
rs += [rot(0, 390, "mais sintomas: mais treino perdido ou alterado, mais competição e trabalho perdidos", w=720, tam=24, cor=TINTA, peso=600, lh=1.3),
       rot(0, 290, "e a crença sobre a fase pode pesar mais que a fase", w=640, tam=24, cor=GLIC, peso=700, lh=1.3)]
diagrama(S, "balanca", 470, p, rs, eyebrow="O que pesa de verdade", titulo="O que tira a mulher do treino está neste prato",
         fonte="Levantamento com 6.812 mulheres que treinam, Br J Sports Med 2021")

# 3. o sangramento que ninguém mede
p = [svg_abre(1664, 470, "Uma gota grande com quatro perguntas de rastreio: troca em menos de duas horas, coágulos grandes, vazamento à noite ou dupla proteção, mais de sete dias. Uma seta leva da gota a um tubo de exame: ferritina. Ao lado, o número: 37% das atletas de elite relataram sangramento intenso"), defs(FOSF)]
p.append(f'<path d="M 360 0 C 300 120, 60 230, 60 330 A 300 140 0 0 0 660 330 C 660 230, 420 120, 360 0 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="5"/>')
rs = []
for j, t in enumerate(["troca em menos de 2 horas?", "coágulos grandes?", "vaza à noite, ou usa dois métodos?", "dura mais de 7 dias?"]):
    rs.append(rot(110, 180 + j * 62, t, w=500, tam=27, cor=TINTA, peso=600, alinha="center"))
p.append(seta(690, 320, 820, 320, FOSF, "m0", esp=5))
p.append(f'<rect x="840" y="200" width="70" height="240" rx="35" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<rect x="846" y="320" width="58" height="114" rx="29" fill="{FOSF}"/>')
rs += [rot(930, 300, "ferritina", w=260, tam=34, cor=FOSF, peso=700, serif=True)]
p.append(caixa(1220, 0, 444, 470, FOSF, CARTAO, esp=3, rx=18))
rs += [rot(1244, 30, "37%", w=400, tam=96, cor=FOSF, peso=700, serif=True),
       rot(1244, 170, "das atletas de elite relataram sangramento intenso", w=400, tam=27, cor=TINTA, peso=600, lh=1.3),
       rot(1244, 300, "um terço já tinha tido anemia; poucas procuraram atendimento", w=400, tam=24, cor=MUDO, lh=1.3)]
diagrama(S, "sangramento", 470, p, rs, eyebrow="O sintoma mais subestimado", titulo="Ninguém mede em mililitro: pergunte pelo efeito, e peça a ferritina",
         fonte="Atletas e corredoras da maratona de Londres, 2016")

# 4. seis perguntas, dois minutos
p = [svg_abre(1664, 480, "Uma ficha de anamnese com seis perguntas numeradas e um relógio marcando dois minutos: primeira menstruação; regularidade, e como ela sabe; meses sem menstruar; contracepção, qual e desde quando; sintomas que atrapalham o treino; gestações e planos")]
rs = []
perg = [("t:calendar", "Com que idade veio a primeira menstruação?"), ("t:repeat", "Os ciclos são regulares? E como você sabe?"),
        ("t:alert-triangle", "Já ficou meses sem menstruar? Quantos, quando?"), ("t:pill", "Usa contracepção? Qual, por qual via, desde quando?"),
        ("t:mood-sad", "Algum sintoma atrapalha o treino? Já tratou?"), ("h:woman", "Já engravidou? Tem planos?")]
for j, (ic, t) in enumerate(perg):
    x, y = (j % 2) * 640, (j // 2) * 160
    p.append(caixa(x, y, 620, 140, TINTA, CARTAO, esp=2, rx=14))
    p.append(icone(ic, x + 24, y + 38, 60, FOSF if j == 2 else TINTA))
    rs.append(rot(x + 104, y + 30, t, w=490, tam=28, cor=TINTA, peso=600, lh=1.3))
p.append(f'<circle cx="1470" cy="200" r="150" fill="{OXID_T}" stroke="{OXID}" stroke-width="6"/>')
p.append(f'<path d="M1470 200 L1470 80 A120 120 0 0 1 1574 140 Z" fill="{OXID}"/>')
rs += [rot(1320, 380, "dois minutos", w=300, tam=36, cor=OXID, peso=700, serif=True, alinha="center"),
       rot(1300, 430, "quase nunca alguém perguntou antes", w=340, tam=22, cor=MUDO, alinha="center")]
diagrama(S, "perguntas", 480, p, rs, eyebrow="Primeiro passo: perguntar", titulo="Seis perguntas que cabem em qualquer avaliação")

# 5. o registro de três ciclos
p = [svg_abre(1664, 470, "Uma planilha de três ciclos, cada um em linha, com dias numerados. Duas faixas acendem nos três ciclos: os dois primeiros dias de sangramento e os três dias antes dele, com sintoma e esforço altos. Ao lado, o que não precisa de rotina: temperatura basal, teste de ovulação, aplicativo com previsão")]
rs = []
for c in range(3):
    y = 40 + c * 120
    rs.append(rot(0, y + 18, f"ciclo {c + 1}", w=120, tam=24, cor=TINTA, peso=700))
    n = [29, 31, 28][c]
    for d in range(n):
        x = 130 + d * 30
        cor = FOSF if d < 2 else (GLIC if d >= n - 3 else BORDA)
        p.append(f'<rect x="{x}" y="{y}" width="26" height="70" rx="4" fill="{cor}"/>')
rs += [rot(130, 0, "sangramento: sintoma e esforço altos", w=420, tam=22, cor=FOSF, peso=700),
       rot(600, 400, "os três dias antes: esforço alto e sono ruim, nos três ciclos", w=640, tam=22, cor=GLIC, peso=700, alinha="right")]
p.append(caixa(1100, 0, 564, 380, MUDO, PAPEL, esp=2, rx=16))
rs.append(rot(1124, 20, "O que não precisa de rotina", w=520, tam=27, cor=MUDO, peso=700, serif=True))
for j, t in enumerate(["temperatura basal", "teste de ovulação", "aplicativo com previsão"]):
    p.append(icone("t:x", 1124, 96 + j * 80, 40, MUDO))
    rs.append(rot(1180, 100 + j * 80, t, w=460, tam=26, cor=MUDO))
rs.append(rot(1124, 340, "três colunas bastam", w=520, tam=24, cor=OXID, peso=700))
diagrama(S, "registro", 470, p, rs, eyebrow="Segundo passo: registrar por três ciclos", titulo="Três colunas mostram se o padrão é dela, ou se não existe",
         fonte="Colunas: primeiro dia do sangramento · nota de sintoma de 0 a 10 · esforço nas sessões habituais")

# 6. os seis alertas
p = [svg_abre(1664, 500, "Um painel de seis sinais de alerta, cada um com um ícone, três em vermelho: amenorreia de três meses ou mais em quem menstruava; sem menarca aos 15 anos; intervalos acima de 35 dias de forma persistente; mudança de padrão em quem era regular; sangramento intenso; dor que limita. Embaixo: rastrear é de todos, investigar é médico")]
rs = []
al = [("Amenorreia de 3 meses ou mais", "em quem já menstruava: nunca é adaptação ao treino", True),
      ("Sem menarca aos 15 anos", "ou 3 anos depois do início das mamas", True),
      ("Intervalos acima de 35 dias", "de forma persistente", False),
      ("Mudança de padrão", "de 28 para 45 dias: o que mais mudou?", False),
      ("Sangramento intenso", "e a ferritina", False),
      ("Dor que limita", "a endometriose ainda leva anos para ser vista", True)]
for j, (t, x_, forte) in enumerate(al):
    x, y = (j % 3) * 560, (j // 3) * 190
    c = FOSF if forte else GLIC
    p.append(caixa(x, y, 536, 170, c, FOSF_T if forte else GLIC_T, esp=3, rx=14))
    p.append(icone("t:alert-triangle", x + 20, y + 22, 48, c))
    rs += [rot(x + 84, y + 24, t, w=430, tam=26, cor=c, peso=700, lh=1.2), rot(x + 24, y + 100, x_, w=490, tam=22, cor=TINTA, lh=1.25)]
p.append(caixa(0, 400, 1664, 100, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 418, "Amenorreia, lesão óssea e perda de peso juntas: prioridade sobre todos · rastrear é de todos; investigar é médico", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center", lh=1.25))
diagrama(S, "alertas", 500, p, rs, eyebrow="Terceiro passo: o que muda de mãos", titulo="Seis sinais em que o caso sai do treino e vai para quem investiga")

# 7. tratar devolve dias
p = [svg_abre(1664, 470, "Dois caminhos saindo da mesma cólica. Em cima, reorganizar o treino em volta do sintoma: o calendário fica cheio de buracos. Embaixo, tratar o sintoma: encaminhamento, tratamento, e o calendário volta a ficar cheio. A frase: se a cólica tira você do treino, o problema a resolver é a cólica"), defs(FOSF, OXID)]
p.append(f'<circle cx="120" cy="235" r="100" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="5"/>')
rs = [rot(40, 214, "a mesma cólica", w=160, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.15)]
p.append(seta(230, 190, 380, 100, FOSF, "m0", esp=5))
p.append(seta(230, 280, 380, 370, OXID, "m1", esp=5))
for k, (t, c, f, buraco) in enumerate([("reorganizar o treino em volta dela", FOSF, FOSF_T, True), ("tratar, e depois ajustar o fino", OXID, OXID_T, False)]):
    y = k * 250
    p.append(caixa(400, y, 1264, 220, c, f, esp=3, rx=16))
    rs.append(rot(424, y + 20, t, w=800, tam=30, cor=c, peso=700, serif=True))
    for d in range(28):
        vazio = buraco and (d % 7 in (0, 1, 6))
        p.append(f'<rect x="{430 + d * 42}" y="{y + 100}" width="34" height="80" rx="5" fill="{PAPEL if vazio else c}" stroke="{c}" stroke-width="2"/>')
p.append(caixa(1250, 10, 400, 70, TINTA, TINTA, esp=0, rx=12))
rs.append(rot(1250, 26, "o calendário esvazia", w=400, tam=24, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "tratar", 470, p, rs, eyebrow="A decisão que mais devolve dias", titulo="Se a cólica tira você do treino, o problema a resolver é a cólica",
         destaque="Primeiro tratar, depois ajustar. Na nadadora: ginecologia, ferro, e só então o ajuste de três dias pelo registro dela.", destaque_cor="tinta")

# 8. como falar, e o dia da prova
p = [svg_abre(1664, 460, "Dois balões de fala. O riscado: nessas duas semanas o seu corpo não responde. O marcado: em média o efeito é pequeno; vamos anotar três ciclos e descobrir se você sente, e ajustar pelos seus dados. Embaixo, uma prova no calendário caindo no primeiro dia do sangramento: manejar o sintoma, não o calendário")]
rs = []
for k, (t, c, f, ok) in enumerate([("“Nessas duas semanas o seu corpo não responde.”", FOSF, FOSF_T, False),
                                   ("“Em média, o efeito é pequeno. Vamos anotar três ciclos e descobrir se você sente. Se sentir, a gente ajusta pelos seus dados.”", OXID, OXID_T, True)]):
    x = 0 if k == 0 else 600
    w = 560 if k == 0 else 1064
    p.append(f'<rect x="{x}" y="0" width="{w}" height="250" rx="40" fill="{f}" stroke="{c}" stroke-width="4"/>')
    p.append(f'<path d="M {x + 80} 250 l 0 50 l 60 -50 Z" fill="{f}" stroke="{c}" stroke-width="4"/>')
    p.append(icone("t:check" if ok else "t:x", x + w - 90, 20, 60, c))
    rs.append(rot(x + 36, 50, t, w=w - 150, tam=30 if ok else 32, cor=TINTA, peso=600, serif=True, lh=1.3))
p.append(caixa(0, 330, 1664, 130, TINTA, CARTAO, esp=2, rx=16))
p.append(icone("t:trophy", 30, 360, 70, GLIC))
rs += [rot(130, 352, "A prova cai no primeiro dia do sangramento?", w=1500, tam=28, cor=TINTA, peso=700, serif=True),
       rot(130, 400, "manejar o sintoma, não o calendário; deslocar o sangramento com hormônio é decisão médica", w=1500, tam=24, cor=MUDO)]
diagrama(S, "falar", 460, p, rs, eyebrow="Quarto passo: como falar", titulo="A frase errada instala um limite que a evidência não sustenta")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Sintomas menstruais", "titulo": "Perguntar, registrar, separar o alerta, tratar antes de ajustar",
          "regras": ["Seis perguntas e três ciclos de registro",
                     "Amenorreia de três meses nunca é adaptação ao treino",
                     "Tratar o sintoma antes de reorganizar o treino"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Pergunta, registra e ajusta o dia pelo sintoma do dia."},
                    {"ic": "t:salad", "t": "Nutrição", "x": "Pergunta pelo sangramento quando vê cansaço e ferritina baixa."},
                    {"ic": "h:doctor", "t": "Médico e ginecologia", "x": "Investigam amenorreia, dor e sangramento, e tratam."}]})

salvar("11-03.json", {"arquivo": "aulas/MOD11/11-03-sintomas-menstruais-o-que-de-fato-limita.md",
                      "titulo": "Sintomas menstruais: o que de fato limita", "subtitulo": "O roteiro para enxergar, registrar e tratar",
                      "nota_capa": "Entra por uma nadadora que perdia um mês de treino por ano.",
                      "secoes": {"calendario": ["O que pesa.", "capa"], "perguntas": ["Perguntar e registrar.", "perguntas"],
                                 "alertas": ["O que muda de mãos.", "alertas"], "tratar": ["Tratar e falar.", "tratar"]},
                      "slides": S})
