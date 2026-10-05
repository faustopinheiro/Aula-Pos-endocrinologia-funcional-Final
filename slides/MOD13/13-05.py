"""Spec do deck 13.5. Gera 13-05.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a mesa com três números
p = [svg_abre(1664, 460, "Uma mulher na casa dos sessenta com um tapete de pilates. Na mesa: relógio com recuperação 38, sensor de glicose com picos depois da banana, laudo genético com perfil desfavorável para força. Riscados: banana antes da caminhada; pilates nos dias de nota baixa")]
rs = []
p.append(icone("h:old-woman", 0, 20, 240, AZUL))
p.append(f'<rect x="20" y="290" width="200" height="44" rx="22" fill="{OXID}"/>')
rs.append(rot(0, 350, "caminha 5× e faz pilates 2× por semana", w=260, tam=20, cor=AZUL, peso=700, lh=1.25))
cards = [("t:device-watch", "relógio", "recuperação: 38", GLIC, GLIC_T),
         ("t:droplet", "sensor de glicose", "picos depois da banana", FOSF, FOSF_T),
         ("t:clipboard-list", "laudo genético", "desfavorável para força", AZUL, AZUL_T)]
for k, (ic, t, x_, c, f) in enumerate(cards):
    x = 300 + k * 460
    p.append(caixa(x, 0, 440, 250, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 72, c))
    rs += [rot(x + 110, 30, t, w=310, tam=26, cor=c, peso=700, serif=True),
           rot(x + 24, 130, f"“{x_}”", w=392, tam=26, cor=TINTA, peso=700, lh=1.25)]
for j, t in enumerate(["banana antes da caminhada", "pilates nos dias de nota baixa"]):
    x = 300 + j * 690
    p.append(caixa(x, 300, 660, 100, GRADE, CARTAO, esp=2, rx=16))
    rs.append(rot(x + 20, 330, t, w=620, tam=28, cor=MUDO, peso=700, alinha="center"))
    p.append(f'<line x1="{x + 40}" y1="350" x2="{x + 620}" y2="350" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(300, 414, "o que os três números tiraram dela", w=1364, tam=22, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "mesa", 460, p, rs, eyebrow="Caminhada e pilates", titulo="Três números sem doença tiraram duas coisas que faziam bem")

# 2. rastreio x medicalização
p = [svg_abre(1664, 440, "Duas colunas. Rastreio: pergunta definida, teste validado, ação conhecida, benefício demonstrado em desfecho. Medicalização: número sem pergunta, referência que ninguém conhece, correção inventada, pessoa saudável que se vê como paciente")]
rs = []
for k, (tit, itens, c, f) in enumerate([("Rastreio", ["uma pergunta definida", "um teste validado para ela", "uma ação conhecida", "benefício demonstrado em desfecho"], OXID, OXID_T),
                                        ("Medicalização", ["um número sem pergunta", "uma referência que ninguém conhece", "uma correção inventada", "uma pessoa saudável que se vê como paciente"], FOSF, FOSF_T)]):
    x = k * 852
    p.append(caixa(x, 0, 812, 440, c, f, esp=3, rx=18))
    rs.append(rot(x + 28, 22, tit, w=756, tam=34, cor=c, peso=700, serif=True))
    for j, t in enumerate(itens):
        y = 110 + j * 80
        p.append(f'<circle cx="{x + 46}" cy="{y + 16}" r="18" fill="{c}"/>')
        rs.append(rot(x + 28, y + 2, str(j + 1), w=36, tam=20, cor=PAPEL, peso=700, alinha="center"))
        rs.append(rot(x + 84, y, t, w=700, tam=26, cor=TINTA, peso=600))
diagrama(S, "diferenca", 440, p, rs, eyebrow="A diferença", titulo="Rastreio responde a uma pergunta; medicalização cria uma")

# 3. o rótulo
p = [svg_abre(1664, 440, "Faltas ao trabalho depois do rastreio de pressão numa indústria. Trabalhadores que receberam o rótulo de hipertensos: aumento de 80%, cerca de 5 dias por ano. Média da empresa: aumento de 9%. Um crachá com a etiqueta hipertenso. O aumento se associou a ficar sabendo, com ou sem tratamento")]
rs = []
B = 400
p.append(f'<line x1="0" y1="{B}" x2="760" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for j, (t, v, c) in enumerate([("rotulados como hipertensos", 80, FOSF), ("média da empresa", 9, MUDO)]):
    x = 60 + j * 360
    h = v * 4
    p.append(f'<rect x="{x}" y="{B - h}" width="240" height="{h}" rx="10" fill="{c}"/>')
    rs.append(rot(x, B - h - 50, f"+{v}%", w=240, tam=36, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x - 20, B + 10, t, w=280, tam=20, cor=TINTA, peso=700, alinha="center"))
rs.append(rot(60, B - 260, "≈ 5 dias a mais por ano", w=240, tam=20, cor=PAPEL, peso=700, alinha="center"))
p.append(f'<rect x="900" y="20" width="300" height="200" rx="16" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<rect x="1020" y="0" width="60" height="30" rx="8" fill="{TINTA}"/>')
p.append(icone("t:user", 930, 60, 90, MUDO))
p.append(f'<rect x="1040" y="90" width="140" height="48" rx="10" fill="{FOSF}"/>')
rs.append(rot(1040, 100, "hipertenso", w=140, tam=22, cor=PAPEL, peso=700, alinha="center"))
rs += [rot(900, 260, "associado a ficar sabendo, com ou sem tratamento", w=764, tam=26, cor=TINTA, peso=700, lh=1.25),
       rot(900, 360, "O rótulo muda o comportamento antes de a doença mudar.", w=764, tam=26, cor=FOSF, peso=700, serif=True, lh=1.25)]
diagrama(S, "rotulo", 440, p, rs, eyebrow="O rótulo pesa por si, estudo de 1978", titulo="Saber-se doente aumentou as faltas em 80%",
         fonte="N Engl J Med 1978")

# 4. a glicose de quem não tem diabetes
def yg(v):
    return 380 - (v - 60) * 3.2


p = [svg_abre(1664, 450, "Curva ilustrativa de glicose de um dia numa pessoa sem diabetes, com picos depois das refeições e a faixa de 70 a 140 mg/dL. 96% do tempo na faixa; cerca de 30 minutos por dia acima de 140; média perto de 99, e de 104 acima dos 60 anos. 153 pessoas sem diabetes, sensor cego, até 10 dias")]
rs = []
p.append(f'<rect x="60" y="{yg(140):.0f}" width="960" height="{yg(70) - yg(140):.0f}" fill="{OXID_T}"/>')
p.append(f'<line x1="60" y1="{yg(140):.0f}" x2="1020" y2="{yg(140):.0f}" stroke="{OXID}" stroke-width="2" stroke-dasharray="8 6"/>')
pts = [(0, 92), (6, 90), (7, 96), (7.5, 132), (8, 146), (9, 112), (10, 98), (12, 94), (12.5, 128), (13, 138), (14, 110), (15, 96), (19, 94), (19.5, 124), (20, 134), (21, 106), (22, 96), (24, 92)]
d = "M " + " L ".join(f"{60 + h * 40:.0f} {yg(v):.0f}" for h, v in pts)
p.append(f'<path d="{d}" stroke="{AZUL}" stroke-width="5" fill="none" stroke-linejoin="round"/>')
p.append(f'<line x1="60" y1="390" x2="1020" y2="390" stroke="{TINTA}" stroke-width="3"/>')
for h in (0, 6, 12, 18, 24):
    rs.append(rot(60 + h * 40 - 40, 400, f"{h}h", w=80, tam=20, cor=MUDO, alinha="center"))
for h in (7, 12.5, 19.5):
    p.append(icone("t:apple", 60 + h * 40 - 16, 20, 32, GLIC))
rs += [rot(0, yg(140) - 14, "140", w=52, tam=20, cor=OXID, peso=700, alinha="right"),
       rot(0, yg(70) - 14, "70", w=52, tam=20, cor=OXID, peso=700, alinha="right"),
       rot(80, yg(78), "faixa de 70 a 140 mg/dL", w=300, tam=20, cor=OXID, peso=700),
       rot(560, 60, "curva ilustrativa", w=300, tam=20, cor=MUDO)]
p.append(caixa(1080, 0, 584, 450, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1104, 20, "96% do tempo na faixa", w=536, tam=30, cor=AZUL, peso=700, serif=True),
       rot(1104, 90, "cerca de 30 minutos por dia acima de 140", w=536, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1104, 180, "média perto de 99, e de 104 acima dos 60 anos", w=536, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1104, 290, "153 pessoas sem diabetes · sensor cego · até 10 dias", w=536, tam=22, cor=MUDO, peso=700, lh=1.3),
       rot(1104, 380, "subir e voltar é fisiologia", w=536, tam=26, cor=AZUL, peso=700, serif=True)]
diagrama(S, "glicose", 450, p, rs, eyebrow="O pico da banana, estudo de 2019", titulo="Na pessoa sem diabetes, o pico depois de comer é fisiologia",
         fonte="J Clin Endocrinol Metab 2019")

# 5. o laudo genético
p = [svg_abre(1664, 440, "Um laudo genético com três genes e selos coloridos, riscado em diagonal. Ao lado, o consenso de 2015: os testes genéticos não têm papel na identificação de talento nem na prescrição individual de treino. Embaixo: força é o treino que mais protege acima dos sessenta")]
rs = []
p.append(f'<rect x="0" y="0" width="560" height="380" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
rs.append(rot(24, 20, "Laudo genético esportivo", w=512, tam=26, cor=TINTA, peso=700, serif=True))
for j, (g, c) in enumerate([("gene A", OXID), ("gene B", GLIC), ("gene C", FOSF)]):
    y = 90 + j * 80
    rs.append(rot(24, y + 10, g, w=200, tam=24, cor=TINTA, peso=600))
    p.append(f'<rect x="300" y="{y}" width="220" height="50" rx="25" fill="{c}"/>')
p.append(f'<line x1="10" y1="370" x2="550" y2="10" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
p.append(caixa(620, 0, 1044, 250, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(648, 20, "Consenso de 2015", w=988, tam=26, cor=AZUL, peso=700),
       rot(648, 70, "“Os testes genéticos não têm papel na identificação de talento nem na prescrição individual de treino.”", w=988, tam=30, cor=TINTA, peso=700, serif=True, lh=1.3)]
p.append(caixa(620, 280, 1044, 100, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:barbell", 644, 302, 56, OXID))
rs.append(rot(720, 304, "acima dos sessenta, força protege osso, músculo e queda", w=920, tam=26, cor=OXID, peso=700, lh=1.2))
rs.append(rot(0, 400, "mesmo problema de um gene específico na conversa sobre cafeína", w=1664, tam=20, cor=MUDO, peso=600))
diagrama(S, "genes", 440, p, rs, eyebrow="O laudo genético de farmácia", titulo="Para prescrever treino, o teste de balcão não tem papel",
         fonte="Br J Sports Med 2015")

# 6. o aviso que tem caminho
p = [svg_abre(1664, 440, "Relógio com aviso de pulso irregular. 419.297 participantes; 0,52% receberam o aviso; dos que usaram o adesivo de eletro depois, 34% tinham fibrilação atrial; quando o aviso coincidia com o adesivo, 84% eram fibrilação. Ao lado, a nota de recuperação, sem caminho validado: ortossonia"), defs(OXID)]
rs = []
p.append(icone("t:device-watch", 0, 40, 180, OXID))
rs.append(rot(0, 240, "“pulso irregular”", w=200, tam=24, cor=OXID, peso=700, alinha="center", serif=True))
etapas = [("419.297", "usuários de relógio"), ("0,52%", "receberam o aviso"), ("34%", "fibrilação no adesivo depois"), ("84%", "quando aviso e adesivo coincidiam")]
for j, (n, t) in enumerate(etapas):
    x = 240 + j * 210
    p.append(caixa(x, 30, 190, 210, OXID, OXID_T if j < 3 else OXID, esp=3, rx=16))
    cor = PAPEL if j == 3 else OXID
    rs += [rot(x + 8, 50, n, w=174, tam=30, cor=cor, peso=700, alinha="center", serif=True),
           rot(x + 8, 110, t, w=174, tam=20, cor=PAPEL if j == 3 else TINTA, peso=700, alinha="center", lh=1.25)]
    if j:
        p.append(seta(x - 18, 135, x - 4, 135, OXID, "m0", 3))
rs.append(rot(240, 270, "um sinal com caminho: eletro e avaliação do risco de AVC", w=820, tam=24, cor=OXID, peso=700))
p.append(caixa(1140, 0, 524, 440, GRADE, CARTAO, esp=2, rx=18))
rs += [rot(1164, 24, "“recuperação: 38”", w=476, tam=30, cor=MUDO, peso=700, serif=True),
       rot(1164, 110, "?", w=476, tam=80, cor=MUDO, peso=700, alinha="center", serif=True),
       rot(1164, 240, "sem referência validada para faltar ao pilates", w=476, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1164, 340, "o padrão tem nome: ortossonia", w=476, tam=24, cor=MUDO, peso=700)]
diagrama(S, "aviso", 440, p, rs, eyebrow="Nem todo número de relógio é ruído, estudo de 2019", titulo="O aviso de pulso irregular tem caminho; a nota da manhã não",
         fonte="N Engl J Med 2019")

# 7. o filtro
p = [svg_abre(1664, 440, "Um filtro de quatro camadas por onde passam os números trazidos de casa: tem referência na pessoa saudável; existe uma ação validada; a ação melhora um desfecho que importa; o que essa medida está tirando da pessoa. Poucos números passam")]
rs = []
for j in range(14):
    p.append(f'<circle cx="{120 + j * 60}" cy="20" r="10" fill="{MUDO}"/>')
for j, (t, c, f) in enumerate([("tem referência medida na pessoa saudável?", AZUL, AZUL_T), ("existe uma ação validada para ele?", AZUL, AZUL_T),
                               ("a ação melhora um desfecho que importa?", AZUL, AZUL_T), ("o que essa medida está tirando da pessoa?", FOSF, FOSF_T)]):
    y = 50 + j * 80
    inset = j * 45
    p.append(f'<path d="M {inset} {y} L {1000 - inset} {y} L {1000 - inset - 45} {y + 70} L {inset + 45} {y + 70} Z" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(inset + 50, y + 22, f"{j + 1} · {t}", w=900 - 2 * inset, tam=22, cor=c, peso=700, alinha="center"))
for j in range(2):
    p.append(f'<circle cx="{470 + j * 60}" cy="400" r="10" fill="{OXID}"/>')
p.append(caixa(1080, 40, 584, 360, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1104, 64, "A quarta pergunta", w=536, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1104, 130, "comida · treino · sono · tranquilidade", w=536, tam=26, cor=TINTA, peso=700, lh=1.3),
       rot(1104, 260, "nela: a banana e o pilates", w=536, tam=28, cor=FOSF, peso=700, serif=True)]
diagrama(S, "filtro", 440, p, rs, eyebrow="Para qualquer número que chega de casa", titulo="Quatro perguntas antes de corrigir um número")

# 8. o que foi feito
p = [svg_abre(1664, 460, "A semana dela de volta: cinco caminhadas, dois pilates e duas sessões curtas de força. Banana antes da caminhada. Laudo genético na gaveta. Relógio mantido para passos e para o aviso de pulso. Rastreio por diretriz: pressão, colesterol, glicose, densitometria na idade indicada, rastreios de câncer recomendados")]
rs = []
for j, (ic, n, t, c) in enumerate([("t:walk", "5×", "caminhada", AZUL), ("t:yoga", "2×", "pilates, com qualquer nota", OXID), ("t:barbell", "2×", "força, curta", GLIC)]):
    y = j * 100
    p.append(caixa(0, y, 1000, 84, c, PAPEL, esp=2, rx=14))
    p.append(icone(ic, 20, y + 14, 56, c))
    rs += [rot(96, y + 18, n, w=100, tam=34, cor=c, peso=700, serif=True), rot(200, y + 24, t, w=780, tam=26, cor=TINTA, peso=700)]
for j, (ic, t) in enumerate([("t:apple", "banana antes da caminhada"), ("t:clipboard-list", "laudo na gaveta"), ("t:device-watch", "relógio: passos e aviso de pulso")]):
    x = j * 340
    p.append(caixa(x, 320, 320, 130, GRADE, CARTAO, esp=2, rx=14))
    p.append(icone(ic, x + 20, 344, 40, MUDO))
    rs.append(rot(x + 70, 340, t, w=232, tam=22, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(1060, 0, 604, 450, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1084, 20, "O rastreio que a idade pede", w=556, tam=28, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["pressão", "colesterol", "glicose", "densitometria na idade indicada", "rastreios de câncer recomendados"]):
    p.append(icone("t:check", 1084, 92 + j * 66, 32, OXID))
    rs.append(rot(1128, 92 + j * 66, t, w=512, tam=24, cor=TINTA, peso=600))
diagrama(S, "conduta", 460, p, rs, eyebrow="O que foi feito", titulo="A banana e o pilates de volta, e o rastreio onde ele tem pergunta")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Rastreio versus medicalização", "titulo": "Cuidado onde há pergunta, e só lá",
          "regras": ["Sem pergunta, teste, ação e benefício, o número é medicalização",
                     "O rótulo muda o comportamento antes de a doença mudar",
                     "Pergunte o que cada número está tirando da pessoa"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Mantém o rastreio da idade e passa os números de casa pelo filtro."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Não troca o plano por nota de aplicativo nem por laudo genético."},
                    {"ic": "t:user", "t": "A praticante", "x": "Usa o aparelho no que ele tem de útil e treina sem pedir licença ao número."}]})

salvar("13-05.json", {"arquivo": "aulas/MOD13/13-05-rastreio-versus-medicalizacao.md",
                      "titulo": "Rastreio versus medicalização", "subtitulo": "Quando o número feito em casa vira problema",
                      "nota_capa": "Entra por uma mulher na casa dos sessenta que caminha, faz pilates e trouxe três números.",
                      "secoes": {"mesa": ["O erro.", "capa"], "rotulo": ["Os três números.", "rotulo"],
                                 "filtro": ["O filtro e a conduta.", "filtro"]},
                      "slides": S})
