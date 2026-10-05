"""Spec do deck 13.10. Gera 13-10.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a trilha
p = [svg_abre(1664, 440, "Perfil de trilha com subidas e uma descida longa. Em cima, o plano de doze semanas com a semana sete circulada: volume sobe, primeiro treino de tiros, sessão mais longa de 9 para 14 km. Na descida, dor na tíbia no dia seguinte. Perfil típico, números ilustrativos")]
rs = []
for j in range(12):
    x = 40 + j * 86
    c = FOSF if j == 6 else GRADE
    p.append(f'<rect x="{x}" y="10" width="70" height="56" rx="8" fill="{FOSF_T if j == 6 else CARTAO}" stroke="{c}" stroke-width="{4 if j == 6 else 2}"/>')
    rs.append(rot(x, 24, str(j + 1), w=70, tam=22, cor=FOSF if j == 6 else MUDO, peso=700, alinha="center"))
p.append(f'<path d="M 0 400 L 140 300 L 260 330 L 400 200 L 520 250 L 640 150 L 1000 400" stroke="{TINTA}" stroke-width="5" fill="none" stroke-linejoin="round"/>')
p.append(f'<path d="M 640 150 L 1000 400 L 640 400 Z" fill="{FOSF_T}"/>')
p.append(icone("t:bolt", 790, 220, 60, FOSF))
rs += [rot(640, 120, "descida longa, terreno novo", w=360, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(0, 76, "perfil típico; números ilustrativos", w=600, tam=20, cor=MUDO)]
p.append(caixa(1100, 0, 564, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(1124, 20, "Semana 7, três mudanças juntas", w=516, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2))
for j, t in enumerate(["volume sobe", "primeiro treino de tiros", "sessão mais longa: 9 → 14 km"]):
    p.append(f'<circle cx="1140" cy="{148 + j * 70}" r="14" fill="{FOSF}"/>')
    rs.append(rot(1168, 134 + j * 70, t, w=480, tam=26, cor=TINTA, peso=700))
rs.append(rot(1124, 360, "“Mas eu segui o plano.”", w=516, tam=30, cor=FOSF, peso=700, serif=True))
diagrama(S, "trilha", 440, p, rs, eyebrow="Corrida de trilha, quatro horas por semana", titulo="Ela seguiu o plano, e a dor começou numa sessão")

# 2. a regra dos dez por cento
p = [svg_abre(1664, 440, "A regra não aumente mais de 10% por semana, riscada. Ensaio de 2008: 532 novatos; programa gradual de 13 semanas, 20,8% de lesão; programa padrão de 8 semanas, 20,3%. Três motivos: percentual depende da base; a semana esconde a distribuição; olha uma variável só")]
rs = []
p.append(caixa(0, 0, 600, 120, MUDO, CARTAO, esp=3, rx=16))
rs.append(rot(24, 36, "“não aumente mais de 10% por semana”", w=552, tam=28, cor=MUDO, peso=700, serif=True, alinha="center"))
p.append(f'<line x1="20" y1="60" x2="580" y2="60" stroke="{FOSF}" stroke-width="8"/>')
B = 400
p.append(f'<line x1="0" y1="{B}" x2="600" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for j, (t, v, c) in enumerate([("gradual, 13 semanas", 20.8, AZUL), ("padrão, 8 semanas", 20.3, MUDO)]):
    x = 60 + j * 280
    h = v * 9
    p.append(f'<rect x="{x}" y="{B - h:.0f}" width="200" height="{h:.0f}" rx="10" fill="{c}"/>')
    rs += [rot(x, B - h - 44, f"{v:.1f}%".replace(".", ","), w=200, tam=32, cor=c, peso=700, alinha="center", serif=True),
           rot(x - 20, B + 8, t, w=240, tam=20, cor=TINTA, peso=700, alinha="center")]
rs.append(rot(0, 128, "532 novatos sorteados · lesão em cada grupo", w=600, tam=22, cor=MUDO, peso=700))
p.append(caixa(680, 0, 984, 440, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(704, 20, "Derruba o número, não o princípio", w=936, tam=30, cor=AZUL, peso=700, serif=True))
for j, (t, x_) in enumerate([("percentual depende da base", "10% de 10 km é 1 km; de 60 km, são 6"),
                             ("a semana esconde a distribuição", "30 km em seis sessões não é 30 km em duas"),
                             ("olha uma variável só", "e a progressão tem cinco")]):
    y = 100 + j * 110
    rs += [rot(704, y, t, w=936, tam=26, cor=TINTA, peso=700), rot(704, y + 40, x_, w=936, tam=22, cor=MUDO, peso=600)]
diagrama(S, "dez", 440, p, rs, eyebrow="A regra que todo mundo ensina, ensaio de 2008", titulo="A regra dos dez por cento foi testada, e não protegeu",
         fonte="Am J Sports Med 2008")

# 3. a sessão
p = [svg_abre(1664, 440, "1.666 lesões em barra empilhada: sobrecarga aguda 28%, sobrecarga de início súbito 64%, sobrecarga gradual 8%. Curva de risco conforme a sessão passa da mais longa dos últimos 30 dias: até 10%, referência; de 10 a 30% a mais, risco 64% maior; acima, maior ainda. Coorte com relógio GPS, corredores de 87 países")]
rs = []
W = 760
segs = [("sobrecarga aguda", 0.28, GLIC), ("sobrecarga de início súbito", 0.64, FOSF), ("gradual", 0.08, AZUL)]
x = 0
for t, v, c in segs:
    w = W * v
    p.append(f'<rect x="{x:.0f}" y="60" width="{w - 4:.0f}" height="120" rx="10" fill="{c}"/>')
    rs.append(rot(x, 96, f"{int(v * 100)}%", w=w - 4, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
    x += w
rs += [rot(0, 190, "aguda", w=210, tam=20, cor=GLIC, peso=700, alinha="center"),
       rot(213, 190, "de início súbito: começou numa sessão", w=486, tam=20, cor=FOSF, peso=700, alinha="center"),
       rot(640, 220, "gradual", w=120, tam=20, cor=AZUL, peso=700, alinha="center"),
       rot(0, 10, "1.666 lesões, coorte de 2024", w=760, tam=22, cor=MUDO, peso=700),
       rot(0, 290, "o que a gente achava que era a regra é a exceção", w=760, tam=26, cor=TINTA, peso=700, serif=True, lh=1.25)]
X0, Y0 = 880, 380
p.append(f'<line x1="{X0}" y1="{Y0}" x2="1640" y2="{Y0}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{X0}" y1="60" x2="{X0}" y2="{Y0}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M {X0} 330 L 1100 330 L 1300 230 C 1420 170 1520 110 1630 70" stroke="{FOSF}" stroke-width="6" fill="none"/>')
p.append(f'<line x1="1100" y1="{Y0}" x2="1100" y2="90" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 6"/>')
rs += [rot(X0, Y0 + 10, "até 10% acima da mais longa dos últimos 30 dias", w=260, tam=20, cor=MUDO, peso=700, lh=1.2),
       rot(1300, 290, "10 a 30% acima: +64% de risco", w=300, tam=22, cor=FOSF, peso=700, lh=1.2),
       rot(1130, 110, "saltos maiores, risco maior", w=260, tam=20, cor=FOSF, peso=700, lh=1.2),
       rot(X0 + 20, 60, "risco de lesão por sobrecarga · coorte de 2025", w=700, tam=20, cor=MUDO, peso=700)]
diagrama(S, "sessao", 440, p, rs, eyebrow="A lesão que começa numa sessão", titulo="A maior parte da lesão de sobrecarga começa num dia",
         fonte="JOSPT Open 2024 · Br J Sports Med 2025")

# 4. os cinco mostradores
p = [svg_abre(1664, 440, "Cinco mostradores: volume semanal; sessão mais longa, em destaque; intensidade; contexto mecânico (superfície, descida, tênis); densidade (dias seguidos). Ao lado, duas curvas no tempo: fôlego sobe rápido, tecido sobe devagar. Esquema")]
rs = []
mostr = [("volume semanal", AZUL), ("sessão mais longa", FOSF), ("intensidade", GLIC), ("contexto: superfície, descida, tênis", OXID), ("densidade: dias seguidos", MUDO)]
for j, (t, c) in enumerate(mostr):
    x = (j % 3) * 330
    y = (j // 3) * 220
    destaque = j == 1
    p.append(f'<path d="M {x + 40} {y + 150} A 110 110 0 0 1 {x + 260} {y + 150}" stroke="{c}" stroke-width="{18 if destaque else 10}" fill="none" stroke-linecap="round"/>')
    p.append(f'<line x1="{x + 150}" y1="{y + 150}" x2="{x + 150 + (60 if destaque else 30)}" y2="{y + 70}" stroke="{TINTA}" stroke-width="5" stroke-linecap="round"/>')
    rs.append(rot(x + 10, y + 166, t, w=280, tam=22, cor=c if destaque else TINTA, peso=700, alinha="center", lh=1.2))
p.append(caixa(1040, 0, 624, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(f'<line x1="1080" y1="360" x2="1620" y2="360" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 1080 350 C 1180 180 1300 130 1620 110" stroke="{AZUL}" stroke-width="6" fill="none"/>')
p.append(f'<path d="M 1080 352 C 1300 340 1450 300 1620 220" stroke="{FOSF}" stroke-width="6" fill="none"/>')
p.append(f'<line x1="1300" y1="130" x2="1300" y2="360" stroke="{MUDO}" stroke-width="2" stroke-dasharray="6 6"/>')
rs += [rot(1064, 20, "O fôlego chega antes do tecido", w=576, tam=26, cor=AZUL, peso=700, serif=True),
       rot(1420, 80, "fôlego", w=200, tam=22, cor=AZUL, peso=700, alinha="right"),
       rot(1420, 250, "osso e tendão", w=200, tam=22, cor=FOSF, peso=700, alinha="right"),
       rot(1240, 372, "semana 7", w=120, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(1080, 400, "esquema", w=200, tam=20, cor=MUDO)]
diagrama(S, "mostradores", 440, p, rs, eyebrow="Os cinco mostradores", titulo="A progressão tem cinco mostradores, e o plano olha um")

# 5. contar tudo
p = [svg_abre(1664, 420, "A semana dela em duas camadas. Em cima, o que ela chama de treino: quatro horas de corrida. Embaixo, o que ela não conta: caminhada de 50 minutos com o cachorro todos os dias, futevôlei no sábado, oito horas em pé no trabalho. Uma lupa sobre a camada de baixo")]
rs = []
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
for j, d in enumerate(DIAS):
    x = 200 + j * 200
    rs.append(rot(x, 0, d, w=180, tam=20, cor=MUDO, peso=700, alinha="center"))
    if d in ("ter", "qui", "sáb", "dom"):
        p.append(f'<rect x="{x}" y="34" width="180" height="70" rx="10" fill="{AZUL}"/>')
    p.append(f'<rect x="{x}" y="140" width="180" height="40" rx="8" fill="{GLIC}"/>')
    if d not in ("sáb", "dom"):
        p.append(f'<rect x="{x}" y="196" width="180" height="40" rx="8" fill="{MUDO}"/>')
p.append(f'<rect x="{200 + 5 * 200}" y="196" width="180" height="40" rx="8" fill="{OXID}"/>')
rs += [rot(0, 50, "o que ela chama de treino: 4 h", w=190, tam=20, cor=AZUL, peso=700, lh=1.2),
       rot(0, 142, "cachorro, 50 min", w=190, tam=20, cor=GLIC, peso=700),
       rot(0, 198, "em pé, 8 h", w=190, tam=20, cor=MUDO, peso=700),
       rot(1200, 204, "futevôlei", w=180, tam=20, cor=PAPEL, peso=700, alinha="center")]
p.append(icone("t:zoom-question", 1500, 120, 120, FOSF))
p.append(f'<rect x="0" y="280" width="1664" height="120" rx="16" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
rs.append(rot(24, 316, "Pergunte pelo que a pessoa faz, e não pelo que ela treina.", w=1616, tam=32, cor=FOSF, peso=700, serif=True, alinha="center"))
diagrama(S, "contar", 420, p, rs, eyebrow="Passo 1", titulo="Contar tudo o que a pessoa faz, não só o treino")

# 6. as quatro regras
p = [svg_abre(1664, 440, "Quatro regras numeradas: a sessão mais longa sobe um degrau, até 10% acima da mais longa dos últimos 30 dias; uma semana de consolidação a cada três; intensidade só depois de volume estável; uma mudança por vez: volume, tiros, tênis, terreno")]
rs = []
regras = [("t:stairs", "a sessão mais longa sobe um degrau", "até 10% acima da mais longa dos últimos 30 dias"),
          ("t:repeat", "uma semana de consolidação a cada três", "mesma carga: o tecido precisa de tempo com ela"),
          ("t:bolt", "intensidade só com volume estável", "os tiros entram quando o volume parou de subir"),
          ("t:adjustments-horizontal", "uma mudança por vez", "volume, tiros, tênis ou terreno: um por semana")]
for j, (ic, t, x_) in enumerate(regras):
    x, y = (j % 2) * 842, (j // 2) * 220
    p.append(caixa(x, y, 822, 200, OXID, OXID_T, esp=3, rx=18))
    p.append(f'<circle cx="{x + 50}" cy="{y + 50}" r="28" fill="{OXID}"/>')
    rs.append(rot(x + 22, y + 34, str(j + 1), w=56, tam=26, cor=PAPEL, peso=700, alinha="center"))
    p.append(icone(ic, x + 730, y + 24, 60, OXID))
    rs += [rot(x + 100, y + 30, t, w=620, tam=28, cor=OXID, peso=700, serif=True, lh=1.2),
           rot(x + 24, y + 120, x_, w=770, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "regras", 440, p, rs, eyebrow="Passo 2", titulo="Quatro regras para reescrever qualquer plano")

# 7. pausa e terreno
p = [svg_abre(1664, 440, "Uma escada de sessões mais longas que sofre uma pausa de duas semanas por gripe. Depois da pausa, duas setas: a errada, voltando ao degrau de onde parou; a certa, voltando um degrau abaixo. Aviso: descida e terreno novo contam como degrau"), defs(FOSF, OXID)]
rs = []
for j in range(5):
    p.append(f'<rect x="{j * 120}" y="{360 - j * 50}" width="110" height="{40 + j * 50}" rx="8" fill="{AZUL}"/>')
p.append(f'<rect x="620" y="200" width="200" height="200" rx="12" fill="{CARTAO}" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
p.append(icone("t:temperature", 680, 230, 80, MUDO))
rs.append(rot(620, 340, "duas semanas paradas", w=200, tam=20, cor=MUDO, peso=700, alinha="center", lh=1.2))
p.append(f'<rect x="860" y="160" width="110" height="240" rx="8" fill="{FOSF}" fill-opacity="0.35" stroke="{FOSF}" stroke-width="3" stroke-dasharray="8 6"/>')
p.append(f'<rect x="1000" y="210" width="110" height="190" rx="8" fill="{OXID}"/>')
p.append(seta(840, 120, 900, 150, FOSF, "m0", 4))
p.append(seta(1080, 120, 1060, 200, OXID, "m1", 4))
rs += [rot(700, 70, "de onde parou: o salto", w=260, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(960, 70, "um degrau abaixo", w=200, tam=22, cor=OXID, peso=700, alinha="center")]
p.append(caixa(1180, 0, 484, 440, GLIC, GLIC_T, esp=3, rx=18))
p.append(f'<path d="M 1210 380 L 1330 220 L 1630 380" stroke="{GLIC}" stroke-width="6" fill="none"/>')
rs += [rot(1204, 24, "Terreno também é degrau", w=436, tam=28, cor=GLIC, peso=700, serif=True, lh=1.2),
       rot(1204, 110, "descida longa ou superfície nova: a distância desce na primeira vez", w=436, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "pausa", 440, p, rs, eyebrow="Passo 3: o que o aplicativo não prevê", titulo="Depois de uma pausa, um degrau abaixo")

# 8. as três perguntas
p = [svg_abre(1664, 440, "Três perguntas em balões: o que você fazia de quatro a seis semanas antes de doer; na sessão em que começou, o que foi diferente; o que mais você faz que não chama de treino. Respostas comuns da segunda: mais longa, mais rápida, descida, superfície nova, tênis novo, depois de uma pausa, acompanhando alguém mais rápido")]
rs = []
perg = [("o que você fazia de quatro a seis semanas antes de doer?", AZUL, AZUL_T),
        ("na sessão em que começou, o que foi diferente?", FOSF, FOSF_T),
        ("o que mais você faz que não chama de treino?", GLIC, GLIC_T)]
for j, (t, c, f) in enumerate(perg):
    x = j * 560
    p.append(caixa(x, 0, 536, 200, c, f, esp=3, rx=40))
    p.append(f'<path d="M {x + 100} 200 L {x + 90} 240 L {x + 150} 200" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x + 30, 50, f"{j + 1}. {t}", w=476, tam=28, cor=TINTA, peso=700, serif=True, lh=1.25))
rs.append(rot(0, 270, "respostas comuns da segunda pergunta", w=1664, tam=22, cor=FOSF, peso=700))
for j, t in enumerate(["mais longa", "mais rápida", "descida", "superfície nova", "tênis novo", "depois de uma pausa", "alguém mais rápido"]):
    x = (j % 4) * 416
    y = 320 + (j // 4) * 60
    p.append(f'<rect x="{x}" y="{y}" width="396" height="48" rx="24" fill="{PAPEL}" stroke="{FOSF}" stroke-width="2"/>')
    rs.append(rot(x, y + 12, t, w=396, tam=22, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "perguntas", 440, p, rs, eyebrow="Passo 4: quando a dor aparece", titulo="Três perguntas antes de qualquer exame")

# 9. o plano reescrito
p = [svg_abre(1664, 440, "Plano reescrito em barras da sessão mais longa por semana, subindo em degraus pequenos com uma semana plana a cada três; tiros só depois de quatro semanas de volume estável; força curta em todas as semanas. A prova marcada adiante: a prova pode esperar, a tíbia não. Esquema")]
rs = []
B = 360
vals = [6, 6.5, 7, 7, 7.5, 8, 8, 8.5, 9, 9, 10, 11, 11, 12, 13, 13]
for j, v in enumerate(vals):
    x = j * 72
    h = v * 22
    plana = j in (3, 6, 9, 12, 15)
    p.append(f'<rect x="{x}" y="{B - h:.0f}" width="60" height="{h:.0f}" rx="6" fill="{AZUL_T if plana else AZUL}"/>')
    p.append(f'<rect x="{x + 10}" y="{B + 10}" width="40" height="14" rx="7" fill="{OXID}"/>')
p.append(f'<line x1="0" y1="{B}" x2="1150" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{4 * 72 - 6}" y1="40" x2="{4 * 72 - 6}" y2="{B}" stroke="{GLIC}" stroke-width="3" stroke-dasharray="8 6"/>')
rs += [rot(4 * 72, 40, "tiros entram aqui", w=200, tam=20, cor=GLIC, peso=700),
       rot(0, 40, "sessão mais longa, por semana", w=260, tam=20, cor=AZUL, peso=700),
       rot(0, B + 30, "força curta em todas as semanas", w=600, tam=20, cor=OXID, peso=700),
       rot(620, B + 30, "barras claras: semanas de consolidação · esquema", w=530, tam=20, cor=MUDO, peso=700, alinha="right")]
p.append(caixa(1200, 0, 464, 440, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:flag", 1224, 24, 64, FOSF))
rs += [rot(1300, 36, "a prova", w=340, tam=28, cor=FOSF, peso=700, serif=True),
       rot(1224, 130, "doze semanas viram dezesseis, ou a prova do ano seguinte", w=416, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1224, 300, "A prova pode esperar; a tíbia não.", w=416, tam=28, cor=FOSF, peso=700, serif=True, lh=1.25)]
diagrama(S, "plano", 440, p, rs, eyebrow="O plano reescrito", titulo="Mais lento no papel, para chegar à prova correndo")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Progressão para quem treina quatro horas por semana", "titulo": "Proteger a sessão, não só a semana",
          "regras": ["A sessão não passa de 10% da mais longa do último mês",
                     "Cinco mostradores, e o fôlego chega antes do tecido",
                     "Uma mudança por vez; depois de pausa, um degrau abaixo"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Faz as três perguntas antes de pedir exame."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Conta tudo o que a pessoa faz e reescreve o plano com as quatro regras."},
                    {"ic": "t:user", "t": "O praticante", "x": "Registra a sessão mais longa e não muda duas coisas na mesma semana."}]})

salvar("13-10.json", {"arquivo": "aulas/MOD13/13-10-progressao-para-quem-treina-quatro-horas-por-semana.md",
                      "titulo": "Progressão para quem treina quatro horas por semana", "subtitulo": "Quatro passos para reescrever qualquer plano",
                      "nota_capa": "Entra por uma corredora de trilha que seguiu o plano e se machucou numa sessão.",
                      "secoes": {"trilha": ["O erro.", "capa"], "dez": ["O que os dados mostram.", "dez"],
                                 "contar": ["O procedimento.", "contar"]},
                      "slides": S})
