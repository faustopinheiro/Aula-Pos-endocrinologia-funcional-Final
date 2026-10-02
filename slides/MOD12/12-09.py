"""Spec do deck 12.9. Gera 12-09.json ao lado deste arquivo."""
from _base import *

S = []

X0, X1 = 60, 1600


def mx(m):
    """Posição horizontal do mês m (0 a 24) na linha do tempo."""
    return X0 + (X1 - X0) * m / 24


def eixo_meses(y, marcas=(0, 6, 12, 18, 24)):
    out = [f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{TINTA}" stroke-width="3"/>']
    for m in marcas:
        out.append(f'<line x1="{mx(m):.0f}" y1="{y - 8}" x2="{mx(m):.0f}" y2="{y + 8}" stroke="{TINTA}" stroke-width="3"/>')
    return "".join(out)


CURVA1 = [(0, 300), (3, 230), (6, 190), (9, 200), (10, 210), (13, 280), (16, 330)]
CURVA2 = [(16, 330), (18, 290), (20, 230), (22, 190), (24, 170)]


def caminho(pts, base=0):
    return "M " + " L ".join(f"{mx(m):.0f} {y + base}" for m, y in pts)


# 1. a linha do tempo
p = [svg_abre(1664, 450, "Linha do tempo de 24 meses ilustrativos. Mês 0: volta ao triatlo com o plano dos 25. Mês 6: melhor prova da volta. Mês 10: desempenho começa a cair. Mês 11: remédio novo para a pressão. Mês 13: dor no tendão de Aquiles. Mês 16: é a idade. Embaixo: quatro sessões duras por semana, nenhuma de força")]
rs = []
p.append(eixo_meses(380))
p.append(f'<rect x="{mx(16):.0f}" y="40" width="{mx(24) - mx(16):.0f}" height="300" rx="12" fill="{CARTAO}" stroke="{GRADE}" stroke-width="2" stroke-dasharray="8 6"/>')
p.append(f'<path d="{caminho(CURVA1)}" stroke="{AZUL}" stroke-width="7" fill="none" stroke-linejoin="round"/>')
eventos = [(0, "volta, com o plano dos 25", TINTA, 300), (6, "melhor prova", OXID, 190), (11, "remédio novo para a pressão", GLIC, 230),
           (13, "dor no Aquiles", FOSF, 280), (16, "“é a idade”", FOSF, 330)]
for m, t, c, y in eventos:
    p.append(f'<circle cx="{mx(m):.0f}" cy="{y}" r="14" fill="{c}"/>')
rs += [rot(mx(0) - 20, 320, "volta, com o plano dos 25", w=260, tam=22, cor=TINTA, peso=700, lh=1.2),
       rot(mx(6) - 100, 112, "melhor prova da volta", w=220, tam=22, cor=OXID, peso=700, alinha="center", lh=1.2),
       rot(mx(11) - 150, 140, "remédio novo para a pressão", w=240, tam=22, cor=GLIC, peso=700, alinha="center", lh=1.2),
       rot(mx(13) + 20, 240, "dor no Aquiles", w=200, tam=22, cor=FOSF, peso=700),
       rot(mx(16) + 24, 316, "“é a idade”", w=220, tam=26, cor=FOSF, peso=700, serif=True)]
for m in (0, 6, 12, 18, 24):
    rs.append(rot(mx(m) - 50, 396, f"mês {m}", w=100, tam=20, cor=MUDO, alinha="center"))
rs.append(rot(mx(16) + 260, 60, "o resto da linha, no fim da conversa", w=260, tam=22, cor=MUDO, peso=600, alinha="center", lh=1.25))
rs.append(rot(X0, 0, "desempenho · meses ilustrativos", w=600, tam=22, cor=MUDO))
diagrama(S, "linha", 450, p, rs, eyebrow="Um triatleta na casa dos quarenta volta a competir", titulo="Dois anos de um atleta que ouviu “é a idade”")

# 2. a curva da idade
p = [svg_abre(1664, 440, "Curva dos recordes mundiais máster por idade: quase reta e suave até perto dos 80 anos, depois dobrando para baixo. Ao lado, a curva do triatleta caindo em seis meses. Três cautelas: é o teto, não a média; menos competidores nas faixas mais velhas; é um mosaico, não uma pessoa")]
rs = []
p.append(f'<line x1="60" y1="380" x2="900" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="20" x2="60" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 80 70 L 640 170 C 720 190 780 260 860 360" stroke="{AZUL}" stroke-width="7" fill="none"/>')
rs += [rot(70, 392, "35", w=60, tam=22, cor=MUDO, alinha="center"), rot(610, 392, "≈ 80", w=80, tam=22, cor=MUDO, alinha="center"),
       rot(760, 392, "idade", w=140, tam=22, cor=MUDO, alinha="right"),
       rot(120, 230, "recordes máster: inclinação suave até perto dos 80", w=420, tam=24, cor=AZUL, peso=700, lh=1.25)]
p.append(caixa(960, 0, 300, 200, FOSF, FOSF_T, esp=3, rx=16))
p.append(f'<path d="M 990 70 L 1080 46 L 1230 110" stroke="{FOSF}" stroke-width="6" fill="none"/>')
rs.append(rot(980, 136, "o triatleta: queda em seis meses", w=260, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
for j, t in enumerate(["é o teto, não a média", "menos competidores nas faixas mais velhas", "um mosaico, não uma pessoa"]):
    y = 230 + j * 72
    p.append(caixa(960, y, 704, 60, GRADE, CARTAO, esp=2, rx=12))
    rs.append(rot(980, y + 16, t, w=664, tam=24, cor=TINTA, peso=600))
rs.append(rot(1300, 40, "Idade não muda de um semestre para o outro.", w=364, tam=26, cor=TINTA, peso=700, serif=True, lh=1.3))
diagrama(S, "curva", 440, p, rs, eyebrow="Análise de 2017 dos recordes mundiais máster", titulo="A idade é uma inclinação suave, não uma queda",
         fonte="J Physiol 2017")

# 3. o que muda
p = [svg_abre(1664, 440, "Três determinantes do desempenho de resistência: consumo máximo de oxigênio cai, por frequência cardíaca máxima e volume sistólico; limiar como fração do máximo preservado em quem treina; economia preservada. No máster pesam também: potência cai mais rápido e recuperação mais lenta"), defs(FOSF, OXID)]
rs = []
for k, (t, s_, c, f, desce) in enumerate([("consumo máximo de oxigênio", "frequência cardíaca máxima e volume sistólico caem", FOSF, FOSF_T, True),
                                          ("limiar como fração do máximo", "preservado ou maior em quem treina", OXID, OXID_T, False),
                                          ("economia de movimento", "preservada", OXID, OXID_T, False)]):
    x = k * 360
    p.append(caixa(x, 0, 340, 300, c, f, esp=3, rx=18))
    p.append(seta(x + 120, 40, x + 220, 120, c, "m0", 8) if desce else seta(x + 110, 80, x + 230, 80, c, "m1", 8))
    rs += [rot(x + 20, 150, t, w=300, tam=26, cor=c, peso=700, alinha="center", lh=1.2), rot(x + 20, 226, s_, w=300, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.25)]
p.append(caixa(1110, 0, 554, 300, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1134, 20, "E no máster pesam ainda", w=506, tam=26, cor=AZUL, peso=700, serif=True),
       rot(1134, 90, "· a potência cai mais depressa que a força", w=506, tam=24, cor=TINTA, peso=600, lh=1.25),
       rot(1134, 170, "· a recuperação do mesmo estímulo demora mais", w=506, tam=24, cor=TINTA, peso=600, lh=1.25)]
p.append(caixa(0, 330, 1664, 110, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 350, "Desempenho de resistência: mantido até ≈ 35 anos, queda modesta até 50 a 60, mais íngreme depois", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center", lh=1.3))
diagrama(S, "determinantes", 440, p, rs, eyebrow="Revisão de 2008 sobre atletas máster de resistência", titulo="O máximo cai; limiar e economia se preservam",
         fonte="J Physiol 2008")

# 4. as três perguntas
p = [svg_abre(1664, 440, "Três perguntas: mudou em meses ou em anos? O treino mudou, ainda treina força? Há uma explicação médica que ninguém procurou? Ao lado da primeira, a curva do triatleta: meses")]
rs = []
for k, (n, t, c, f) in enumerate([("1", "Mudou em meses ou em anos?", FOSF, FOSF_T), ("2", "O treino mudou? Ainda treina força?", GLIC, GLIC_T),
                                  ("3", "Há uma explicação médica que ninguém procurou?", AZUL, AZUL_T)]):
    x = k * 564
    p.append(caixa(x, 0, 536, 300, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 70}" cy="70" r="44" fill="{c}"/>')
    rs += [rot(x + 30, 46, n, w=80, tam=40, cor=PAPEL, peso=700, alinha="center", serif=True), rot(x + 24, 140, t, w=488, tam=30, cor=TINTA, peso=700, serif=True, lh=1.2)]
for k, t in enumerate(["meses: não é a idade", "nunca voltou à força; quatro sessões duras", "a seguir"]):
    x = k * 564
    p.append(caixa(x, 330, 536, 110, TINTA, CARTAO, esp=2, rx=14))
    rs.append(rot(x + 20, 362, "no triatleta: " + t, w=496, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.2))
diagrama(S, "perguntas", 440, p, rs, eyebrow="Antes de dizer “é a idade”", titulo="Três perguntas tiram a idade do papel principal")

# 5. os disfarces
p = [svg_abre(1664, 440, "Seis diagnósticos que se disfarçam de idade: deficiência de ferro, tireoide, apneia do sono, remédio novo, energia insuficiente, depressão. Acesos no caso: ferritina baixa com hemoglobina normal e betabloqueador há cinco meses. No homem acima dos quarenta, ferritina baixa pede investigação da causa")]
rs = []
itens = [("deficiência de ferro", "ferritina baixa, hemoglobina normal", True), ("tireoide", "", False), ("apneia do sono", "", False),
         ("remédio novo", "betabloqueador há cinco meses", True), ("energia insuficiente", "", False), ("depressão", "", False)]
for i, (t, achado, aceso) in enumerate(itens):
    x, y = (i % 3) * 564, (i // 3) * 170
    c, f = (FOSF, FOSF_T) if aceso else (GRADE, CARTAO)
    p.append(caixa(x, y, 536, 150, c, f, esp=4 if aceso else 2, rx=16))
    rs.append(rot(x + 24, y + 22, t, w=488, tam=28, cor=FOSF if aceso else TINTA, peso=700, serif=True))
    if achado:
        rs.append(rot(x + 24, y + 84, achado, w=488, tam=24, cor=TINTA, peso=700))
p.append(caixa(0, 350, 1664, 90, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 374, "No homem acima dos quarenta, ferritina baixa pede a investigação da causa, incluindo o tubo digestivo", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "disfarces", 440, p, rs, eyebrow="O que a investigação achou", titulo="Seis diagnósticos se disfarçam de idade")

# 6. a balança
p = [svg_abre(1664, 440, "Balança de treino: estímulo contra recuperação disponível. Aos 25, equilibrada. Aos quarenta e poucos, o mesmo estímulo e menos recuperação: a balança tomba. A semana dele: quatro sessões duras, dias fáceis em ritmo moderado, nenhuma força")]
rs = []
for k, (idade, inc, rec) in enumerate([("aos 25", 0, 130), ("aos quarenta e poucos", 28, 80)]):
    cx = 270 + k * 520
    p.append(f'<path d="M {cx} 120 L {cx - 30} 300 L {cx + 30} 300 Z" fill="{TINTA}"/>')
    p.append(f'<line x1="{cx - 170}" y1="{120 + inc}" x2="{cx + 170}" y2="{120 - inc}" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<rect x="{cx - 220}" y="{120 + inc - 110}" width="100" height="100" rx="10" fill="{FOSF}"/>')
    p.append(f'<rect x="{cx + 120}" y="{120 - inc - rec * 0.8:.0f}" width="100" height="{rec * 0.8:.0f}" rx="10" fill="{OXID}"/>')
    rs.append(rot(cx - 200, 320, idade, w=400, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
rs += [rot(40, 380, "estímulo", w=240, tam=22, cor=FOSF, peso=700, alinha="center"), rot(330, 380, "recuperação disponível", w=300, tam=22, cor=OXID, peso=700, alinha="center")]
p.append(caixa(1080, 0, 584, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(1104, 20, "A semana dele", w=536, tam=28, cor=FOSF, peso=700, serif=True))
for j, (t, c) in enumerate([("4 sessões duras", FOSF), ("dias fáceis em ritmo moderado", GLIC), ("nenhuma força", MUDO)]):
    y = 100 + j * 100
    p.append(f'<rect x="1104" y="{y}" width="40" height="40" rx="8" fill="{c}"/>')
    rs.append(rot(1160, y + 4, t, w=480, tam=26, cor=TINTA, peso=700))
diagrama(S, "balanca", 440, p, rs, eyebrow="O treino também se disfarçava de idade", titulo="O plano não envelheceu junto com ele")

# 7. a semana nova
p = [svg_abre(1664, 440, "A semana nova: duas sessões duras separadas por 48 a 72 horas; dias fáceis de verdade; dois blocos de força; um dia livre; descarga quando os sinais aparecem. Estudo de 2013 com corredores máster de maratona: força máxima melhorou a economia de corrida em cerca de 6%, grupo de seis pessoas")]
rs = []
dias = [("seg", "dura", FOSF, FOSF_T), ("ter", "fácil + força", OXID, OXID_T), ("qua", "fácil", AZUL, AZUL_T), ("qui", "dura", FOSF, FOSF_T),
        ("sex", "fácil + força", OXID, OXID_T), ("sáb", "fácil longo", AZUL, AZUL_T), ("dom", "livre", GRADE, CARTAO)]
for i, (d, t, c, f) in enumerate(dias):
    x = i * 150
    p.append(caixa(x, 0, 136, 220, c, f, esp=3, rx=14))
    rs += [rot(x, 20, d, w=136, tam=26, cor=TINTA, peso=700, alinha="center"), rot(x + 8, 100, t, w=120, tam=22, cor=c if c != GRADE else MUDO, peso=700, alinha="center", lh=1.2)]
rs.append(rot(0, 240, "duas sessões duras, separadas por 48 a 72 horas · descarga quando os sinais aparecem", w=1040, tam=24, cor=TINTA, peso=700, lh=1.3))
p.append(caixa(1100, 0, 564, 440, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1124, 20, "Estudo de 2013", w=516, tam=28, cor=OXID, peso=700, serif=True),
       rot(1124, 80, "corredores máster de maratona; grupo de força máxima", w=516, tam=24, cor=TINTA, peso=600, lh=1.25),
       rot(1124, 190, "+6%", w=516, tam=72, cor=OXID, peso=700, serif=True),
       rot(1124, 290, "na economia de corrida no ritmo de maratona", w=516, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1124, 380, "estudo pequeno: seis pessoas no grupo", w=516, tam=22, cor=MUDO, peso=600)]
diagrama(S, "semana", 440, p, rs, eyebrow="A semana nova", titulo="Menos sessões duras, dias fáceis de verdade e força",
         fonte="J Strength Cond Res 2013")

# 8. o resto da linha do tempo
p = [svg_abre(1664, 450, "Linha do tempo completa, mês 0 a 24. A partir do mês 16: ferro e causa investigados, remédio trocado por quem prescreveu, semana nova com força. A curva sobe de novo e passa o ponto do mês 10, sem chegar à linha tracejada dos 25 anos")]
rs = []
p.append(eixo_meses(380))
p.append(f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{MUDO}" stroke-width="3" stroke-dasharray="12 8"/>')
p.append(f'<path d="{caminho(CURVA1)}" stroke="{GRADE}" stroke-width="7" fill="none" stroke-linejoin="round"/>')
p.append(f'<path d="{caminho(CURVA2)}" stroke="{OXID}" stroke-width="8" fill="none" stroke-linejoin="round"/>')
p.append(f'<line x1="{mx(6):.0f}" y1="190" x2="{X1}" y2="190" stroke="{AZUL}" stroke-width="2" stroke-dasharray="6 6"/>')
for k, (t, c) in enumerate([("ferro e causa investigados", GLIC), ("remédio trocado por quem prescreveu", AZUL), ("semana nova, com força", OXID)]):
    p.append(f'<circle cx="{mx(12):.0f}" cy="{224 + k * 40}" r="10" fill="{c}"/>')
    rs.append(rot(mx(12) + 20, 210 + k * 40, t, w=420, tam=22, cor=TINTA, peso=700))
rs += [rot(X0, 70, "aos 25: não volta", w=400, tam=22, cor=MUDO, peso=600), rot(X1 - 500, 70, "mês 24: melhor que na volta", w=500, tam=22, cor=OXID, peso=700, alinha="right"),
       rot(mx(6) - 110, 140, "melhor prova da volta", w=220, tam=20, cor=AZUL, alinha="center")]
for m in (0, 6, 12, 18, 24):
    rs.append(rot(mx(m) - 50, 396, f"mês {m}", w=100, tam=20, cor=MUDO, alinha="center"))
diagrama(S, "desfecho", 450, p, rs, eyebrow="O resto da linha do tempo", titulo="A idade é a menor parte, e a única que não se trata")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O atleta máster", "titulo": "Investigar antes de explicar, e fazer o plano envelhecer",
          "regras": ["A idade é uma inclinação suave: queda em meses quase nunca é idade",
                     "Antes de “é a idade”: meses ou anos, o treino mudou, que explicação ninguém procurou",
                     "Menos sessões duras, dias fáceis de verdade e força duas vezes por semana"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Investiga antes de explicar: ferro e causa, tireoide, sono, remédios, energia e humor."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Ajusta a densidade de sessões duras, protege os dias fáceis e põe a força na semana."},
                    {"ic": "t:calendar", "t": "O atleta", "x": "Registra o que mudou e quando: a pergunta dos meses ou anos depende disso."}]})

salvar("12-09.json", {"arquivo": "aulas/MOD12/12-09-o-atleta-master.md",
                      "titulo": "O atleta máster", "subtitulo": "Dois anos de um triatleta que ouviu “é a idade”",
                      "nota_capa": "Acompanha, por vinte e quatro meses ilustrativos, um triatleta na casa dos quarenta.",
                      "secoes": {"linha": ["O caso.", "capa"], "curva": ["O que a idade explica.", "curva"],
                                 "perguntas": ["A investigação.", "perguntas"], "balanca": ["O treino.", "balanca"],
                                 "desfecho": ["O resto da linha.", "desfecho"]},
                      "slides": S})
