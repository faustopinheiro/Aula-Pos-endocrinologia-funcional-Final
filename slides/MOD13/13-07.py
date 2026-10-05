"""Spec do deck 13.7. Gera 13-07.json ao lado deste arquivo."""
from _base import *

S = []


def mapa_prova(p, ox, oy, k=1.0):
    """Desenha o mapa esquemático da prova: represa com boias, transição, circuito e chegada."""
    def P(x, y):
        return f"{ox + x * k:.0f} {oy + y * k:.0f}"
    p.append(f'<ellipse cx="{ox + 220 * k:.0f}" cy="{oy + 200 * k:.0f}" rx="{200 * k:.0f}" ry="{170 * k:.0f}" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    for bx, by in ((120, 120), (320, 120), (320, 280), (120, 280)):
        p.append(f'<circle cx="{ox + bx * k:.0f}" cy="{oy + by * k:.0f}" r="{10 * k:.0f}" fill="{GLIC}"/>')
    p.append(f'<path d="M {P(420, 200)} L {P(520, 200)}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="{ox + 520 * k:.0f}" y="{oy + 170 * k:.0f}" width="{60 * k:.0f}" height="{60 * k:.0f}" rx="8" fill="{MUDO}"/>')
    p.append(f'<path d="M {P(580, 200)} C {P(700, 40)} {P(900, 40)} {P(940, 200)} C {P(900, 360)} {P(700, 360)} {P(600, 230)}" stroke="{TINTA}" stroke-width="4" fill="none" stroke-dasharray="14 8"/>')
    p.append(f'<path d="M {P(580, 210)} L {P(1000, 380)}" stroke="{OXID}" stroke-width="4" fill="none"/>')
    p.append(f'<rect x="{ox + 990 * k:.0f}" y="{oy + 360 * k:.0f}" width="{12 * k:.0f}" height="{50 * k:.0f}" fill="{FOSF}"/>')
    p.append(f'<rect x="{ox + 1002 * k:.0f}" y="{oy + 360 * k:.0f}" width="{40 * k:.0f}" height="{26 * k:.0f}" fill="{FOSF}"/>')


# 1. a pergunta do organizador
p = [svg_abre(1664, 440, "Mapa de um triatlo curto numa represa: boias da natação, transição, circuito de bicicleta, corrida e chegada. Prancheta com a pergunta do organizador: quantas ambulâncias eu preciso? Ao lado, a pergunta reescrita: quanto tempo do colapso ao socorro, em cada ponto?")]
rs = []
mapa_prova(p, 0, 10, 0.95)
rs += [rot(100, 6, "natação", w=220, tam=20, cor=AZUL, peso=700, alinha="center"),
       rot(700, 0, "bicicleta", w=200, tam=20, cor=TINTA, peso=700, alinha="center"),
       rot(820, 400, "chegada", w=200, tam=20, cor=FOSF, peso=700)]
p.append(caixa(1100, 0, 564, 180, MUDO, CARTAO, esp=2, rx=14))
rs += [rot(1124, 16, "a pergunta do organizador", w=516, tam=20, cor=MUDO, peso=700),
       rot(1124, 60, "“Quantas ambulâncias eu preciso?”", w=516, tam=28, cor=MUDO, peso=700, serif=True, lh=1.2)]
p.append(caixa(1100, 220, 564, 220, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1124, 236, "a pergunta que decide", w=516, tam=20, cor=OXID, peso=700),
       rot(1124, 280, "“Quanto tempo do colapso ao socorro, em cada ponto?”", w=516, tam=30, cor=TINTA, peso=700, serif=True, lh=1.25)]
diagrama(S, "lago", 440, p, rs, eyebrow="Triatlo curto numa represa, mil inscritos", titulo="A pergunta certa não é quantas ambulâncias")

# 2. o mapa de risco
p = [svg_abre(1664, 440, "Mapa da prova com três zonas. Natação: a largada e os primeiros minutos. Percurso: longe de tudo. Chegada: onde a maioria dos atendimentos acontece. Três camadas de risco: calor e horário, distância, perfil dos inscritos")]
rs = []
mapa_prova(p, 0, 10, 0.95)
for cx, cy, r, c in ((209, 200, 195, AZUL), (760, 190, 170, MUDO), (990, 350, 52, FOSF)):
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="10 8"/>')
rs += [rot(10, 412, "natação: largada e primeiros minutos", w=420, tam=20, cor=AZUL, peso=700),
       rot(940, 40, "percurso: longe de tudo", w=150, tam=20, cor=TINTA, peso=700, lh=1.2),
       rot(560, 412, "chegada: a maior parte dos atendimentos", w=500, tam=20, cor=FOSF, peso=700, alinha="right")]
p.append(caixa(1100, 0, 564, 440, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(1124, 20, "Três camadas sobre o mapa", w=516, tam=28, cor=GLIC, peso=700, serif=True))
for j, (ic, t) in enumerate([("t:sun", "calor e horário da largada"), ("t:route", "distância de cada etapa"), ("t:users", "perfil: amadores de 40 e 50, primeira prova")]):
    p.append(icone(ic, 1124, 100 + j * 100, 48, GLIC))
    rs.append(rot(1190, 104 + j * 100, t, w=450, tam=24, cor=TINTA, peso=700, lh=1.2))
diagrama(S, "mapa", 440, p, rs, eyebrow="Passo 1", titulo="Desenhar o risco no mapa antes de montar a equipe")

# 3. a água
p = [svg_abre(1664, 440, "A natação vista de cima. Largada em ondas. Caiaques e pranchas ao longo do percurso, cada um com um observador. Sinal combinado: braço levantado, preciso de ajuda. Na saída da água, contagem de quem entrou e de quem saiu")]
rs = []
p.append(f'<rect x="0" y="0" width="1100" height="440" rx="18" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
for w_, x0 in enumerate((60, 200, 340)):
    for j in range(5):
        p.append(f'<circle cx="{x0 + (j % 2) * 30}" cy="{90 + j * 60}" r="10" fill="{TINTA}"/>')
    rs.append(rot(x0 - 40, 400, f"onda {w_ + 1}", w=110, tam=20, cor=AZUL, peso=700, alinha="center"))
for kx, ky in ((560, 80), (800, 200), (560, 330), (960, 360)):
    p.append(f'<ellipse cx="{kx}" cy="{ky}" rx="60" ry="16" fill="{GLIC}"/>')
    p.append(f'<circle cx="{kx}" cy="{ky - 18}" r="12" fill="{GLIC}"/>')
p.append(f'<circle cx="760" cy="80" r="12" fill="{TINTA}"/>')
p.append(f'<line x1="760" y1="70" x2="760" y2="20" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
rs += [rot(800, 20, "braço levantado: “preciso de ajuda”", w=280, tam=20, cor=FOSF, peso=700, lh=1.2),
       rot(480, 120, "caiaque com observador", w=200, tam=20, cor=GLIC, peso=700, alinha="center", lh=1.2)]
p.append(caixa(1160, 0, 504, 440, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1184, 20, "Na saída da água", w=456, tam=28, cor=OXID, peso=700, serif=True),
       rot(1184, 90, "entraram: 1.000", w=456, tam=30, cor=TINTA, peso=700),
       rot(1184, 150, "saíram: 999", w=456, tam=30, cor=FOSF, peso=700),
       rot(1184, 240, "a única forma de saber que alguém não saiu é saber quantos entraram", w=456, tam=24, cor=OXID, peso=700, lh=1.3),
       rot(1184, 390, "números ilustrativos", w=456, tam=20, cor=MUDO)]
diagrama(S, "agua", 440, p, rs, eyebrow="Passo 2", titulo="Na água, ver quem afunda e contar quem sai")

# 4. o desfibrilador
p = [svg_abre(1664, 440, "O percurso com círculos de alcance em volta de cada desfibrilador, cobrindo todo o trajeto; dois na chegada; equipes móveis de bicicleta com desfibrilador. Cronômetro: 3 a 5 minutos do colapso ao primeiro choque")]
rs = []
mapa_prova(p, 0, 10, 0.95)
for cx, cy in ((209, 200), (560, 200), (850, 100), (850, 300), (980, 350)):
    p.append(f'<circle cx="{cx}" cy="{cy}" r="88" fill="{OXID}" fill-opacity="0.12" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<rect x="{cx - 16}" y="{cy - 16}" width="32" height="32" rx="6" fill="{OXID}"/>')
p.append(icone("t:bike", 680, 210, 56, OXID))
rs.append(rot(600, 270, "equipe móvel", w=200, tam=20, cor=OXID, peso=700, alinha="center"))
p.append(caixa(1100, 0, 564, 440, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:stopwatch", 1124, 24, 80, OXID))
rs += [rot(1220, 40, "3 a 5 minutos", w=420, tam=40, cor=OXID, peso=700, serif=True),
       rot(1124, 130, "do colapso ao primeiro choque", w=516, tam=26, cor=TINTA, peso=700),
       rot(1124, 210, "onde o círculo não cobre, falta um aparelho", w=516, tam=26, cor=OXID, peso=700, lh=1.25),
       rot(1124, 320, "e todos da equipe, até o posto de água, sabem comprimir", w=516, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "dea", 440, p, rs, eyebrow="Passo 3", titulo="Desfibrilador a poucos minutos de qualquer ponto")

# 5. a triagem pela linha de chegada
p = [svg_abre(1664, 460, "A linha de chegada como divisor. Depois da linha: corredor consciente que não consegue ficar de pé, hipotensão postural: deitar, pernas para cima, líquido pela boca. Antes da linha, ou com alteração do estado mental: parada, golpe de calor, hiponatremia")]
rs = []
p.append(f'<rect x="800" y="0" width="64" height="460" fill="{TINTA}"/>')
for j in range(10):
    for i in range(2):
        if (i + j) % 2 == 0:
            p.append(f'<rect x="{800 + i * 32}" y="{j * 46}" width="32" height="46" fill="{PAPEL}"/>')
rs += [rot(0, 0, "ANTES da linha, ou com alteração mental", w=760, tam=24, cor=FOSF, peso=700),
       rot(904, 0, "DEPOIS da linha, consciente", w=760, tam=24, cor=OXID, peso=700)]
for j, (t, x_) in enumerate([("parada cardíaca", "reanimação e choque"), ("golpe de calor", "temperatura retal e imersão: resfriar primeiro"),
                             ("hiponatremia", "medir o sódio: o próximo passo")]):
    y = 60 + j * 132
    p.append(caixa(0, y, 760, 116, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(24, y + 14, t, w=712, tam=28, cor=FOSF, peso=700, serif=True), rot(24, y + 60, x_, w=712, tam=24, cor=TINTA, peso=600)]
p.append(caixa(904, 60, 760, 380, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:bed", 1180, 190, 150, OXID))
rs += [rot(928, 80, "hipotensão postural", w=712, tam=32, cor=OXID, peso=700, serif=True),
       rot(928, 136, "a causa mais comum de colapso, e benigna", w=712, tam=24, cor=TINTA, peso=700),
       rot(928, 360, "deitar · pernas para cima · líquido pela boca", w=712, tam=24, cor=OXID, peso=700)]
diagrama(S, "colapso", 460, p, rs, eyebrow="Passo 4: a triagem de quem cai", titulo="Quem cai antes da linha é grave até prova em contrário",
         fonte="Br J Sports Med 2011")

# 6. o sódio
p = [svg_abre(1664, 440, "Um aparelho portátil de sódio. Proibido: soro na veia antes de medir. Sinais: confusão, dor de cabeça, vômito, ganho de peso durante a prova. Conduta: sódio baixo com sintoma neurológico, 100 mL de salina a 3%, repetível. Prevenção: beber pela sede")]
rs = []
p.append(f'<rect x="40" y="20" width="220" height="320" rx="24" fill="{AZUL}"/>')
p.append(f'<rect x="70" y="60" width="160" height="110" rx="10" fill="{PAPEL}"/>')
rs.append(rot(70, 86, "Na 128", w=160, tam=34, cor=FOSF, peso=700, alinha="center", serif=True))
for j in range(3):
    p.append(f'<circle cx="{100 + j * 50}" cy="240" r="16" fill="{AZUL_T}"/>')
rs.append(rot(0, 360, "valor ilustrativo", w=300, tam=20, cor=MUDO, alinha="center"))
p.append(caixa(320, 0, 600, 200, FOSF, FOSF_T, esp=3, rx=18))
p.append(f'<circle cx="370" cy="54" r="26" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<line x1="352" y1="36" x2="388" y2="72" stroke="{FOSF}" stroke-width="6"/>')
rs += [rot(410, 36, "soro na veia antes de medir", w=490, tam=26, cor=FOSF, peso=700, serif=True),
       rot(344, 100, "parece desidratação; o soro piora", w=556, tam=24, cor=TINTA, peso=700)]
p.append(caixa(320, 230, 600, 210, GRADE, CARTAO, esp=2, rx=18))
rs.append(rot(344, 248, "Sinais", w=556, tam=26, cor=TINTA, peso=700, serif=True))
for j, t in enumerate(["confusão, dor de cabeça", "náusea, vômito", "ganho de peso na prova"]):
    rs.append(rot(344, 300 + j * 44, t, w=556, tam=24, cor=TINTA, peso=600))
p.append(caixa(980, 0, 684, 300, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1004, 20, "Sódio baixo com sintoma neurológico", w=636, tam=26, cor=OXID, peso=700, serif=True, lh=1.2),
       rot(1004, 110, "salina a 3%, bolus de 100 mL", w=636, tam=34, cor=TINTA, peso=700, serif=True),
       rot(1004, 180, "repetido até os sintomas melhorarem, e transferência", w=636, tam=24, cor=TINTA, peso=700, lh=1.25)]
p.append(f'<rect x="980" y="330" width="684" height="110" rx="18" fill="{AZUL}"/>')
rs.append(rot(1004, 364, "Prevenção: beber pela sede.", w=636, tam=30, cor=PAPEL, peso=700, serif=True, alinha="center"))
diagrama(S, "sodio", 440, p, rs, eyebrow="Passo 5", titulo="Medir o sódio antes de dar soro",
         fonte="Clin J Sport Med 2015")

# 7. a tenda
p = [svg_abre(1664, 440, "Planta da tenda médica com quatro estações: maca com pernas elevadas; imersão com banheira, água e gelo e termômetro retal; sódio com aparelho portátil e salina a 3%; parada com desfibrilador e via de saída livre. Um rádio no centro, ligado aos pontos do percurso")]
rs = []
p.append(f'<path d="M 40 60 L 832 0 L 1624 60 L 1624 440 L 40 440 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
est = [("t:bed", "macas com pernas elevadas", "a maioria: hipotensão postural", AZUL, AZUL_T),
       ("t:temperature", "imersão", "banheira, água e gelo, termômetro retal", GLIC, GLIC_T),
       ("t:droplet", "sódio", "aparelho portátil e salina a 3%", OXID, OXID_T),
       ("t:heartbeat", "parada", "desfibrilador e via de saída livre", FOSF, FOSF_T)]
for j, (ic, t, x_, c, f) in enumerate(est):
    x = 80 + j * 390
    p.append(caixa(x, 90, 360, 250, c, f, esp=3, rx=16))
    p.append(icone(ic, x + 20, 110, 56, c))
    rs += [rot(x + 90, 118, t, w=250, tam=26, cor=c, peso=700, serif=True, lh=1.15),
           rot(x + 20, 200, x_, w=320, tam=22, cor=TINTA, peso=700, lh=1.25)]
p.append(icone("t:phone-call", 790, 360, 56, TINTA))
rs.append(rot(860, 372, "rádio ligado a todos os pontos do percurso", w=700, tam=22, cor=TINTA, peso=700))
diagrama(S, "tenda", 440, p, rs, eyebrow="A tenda médica", titulo="A tenda tem quatro estações, não só macas")

# 8. antes e depois
p = [svg_abre(1664, 440, "Ficha de atendimento com cinco campos: hora, ponto do percurso, queixa, conduta, destino. Briefing da véspera em três itens: calor previsto, beber pela sede, sinais para parar. Seta circular: a ficha desta edição desenha o mapa da próxima"), defs(MUDO)]
rs = []
p.append(caixa(0, 0, 520, 440, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:microphone", 24, 24, 56, GLIC))
rs.append(rot(96, 34, "Antes: o briefing", w=400, tam=28, cor=GLIC, peso=700, serif=True))
for j, t in enumerate(["calor previsto", "beber pela sede", "sinais que fazem parar", "o braço levantado na água"]):
    rs.append(rot(24, 120 + j * 70, f"· {t}", w=472, tam=26, cor=TINTA, peso=700))
p.append(caixa(580, 0, 680, 440, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(604, 20, "Depois: a ficha de cada atendimento", w=632, tam=28, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["hora", "ponto do percurso", "queixa", "conduta", "destino"]):
    y = 90 + j * 66
    p.append(f'<rect x="604" y="{y}" width="632" height="52" rx="8" fill="{PAPEL}" stroke="{GRADE}" stroke-width="2"/>')
    rs.append(rot(624, y + 12, t, w=600, tam=24, cor=TINTA, peso=700))
p.append(f'<path d="M 1482 150 A 90 90 0 1 1 1392 240" stroke="{MUDO}" stroke-width="6" fill="none" marker-end="url(#m0)"/>')
rs += [rot(1300, 0, "a ficha desta edição desenha o mapa da próxima", w=364, tam=26, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.25),
       rot(1300, 400, "revisão no mesmo dia", w=364, tam=22, cor=MUDO, peso=700, alinha="center")]
diagrama(S, "ficha", 440, p, rs, eyebrow="Passo 6: antes da largada e depois da chegada", titulo="Cada atendimento vira uma linha para a próxima edição")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Organização da resposta de emergência em prova", "titulo": "Medir o tempo até o socorro em cada ponto",
          "regras": ["Não é quantas ambulâncias: é quanto tempo até o socorro",
                     "Antes da linha, ou confuso, é grave até prova em contrário",
                     "Na prova longa, sódio medido antes de soro"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Desenha o mapa, monta a tenda em quatro estações e conduz a revisão."},
                    {"ic": "t:stopwatch", "t": "Organização e treino", "x": "Garantem observadores na água, largada em ondas e briefing."},
                    {"ic": "t:user", "t": "O atleta", "x": "Bebe pela sede, conhece o sinal na água e para diante de sintoma."}]})

salvar("13-07.json", {"arquivo": "aulas/MOD13/13-07-organizacao-da-resposta-de-emergencia-em-prova.md",
                      "titulo": "Organização da resposta de emergência em prova", "subtitulo": "Seis passos, da represa à linha de chegada",
                      "nota_capa": "Entra pelo organizador de um triatlo curto que pergunta quantas ambulâncias precisa.",
                      "secoes": {"lago": ["A pergunta.", "capa"], "mapa": ["Antes e durante.", "mapa"],
                                 "colapso": ["A chegada e a tenda.", "colapso"]},
                      "slides": S})
