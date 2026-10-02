"""Spec do deck 12.2. Gera 12-02.json ao lado deste arquivo."""
from _base import *

S = []
A = lambda a, x0=80, w=900: x0 + (a - 8) / 10 * w
vel = lambda a: 5.5 - 0.15 * (a - 8) + 6.5 * math.exp(-((a - 13.6) / 1.1) ** 2) if a < 15.5 else max(0.0, 5.5 - 0.15 * (a - 8) + 6.5 * math.exp(-((a - 13.6) / 1.1) ** 2) - (a - 15.5) * 2.2)


def curva_vel(x0, y0, w, h, cor, esp=6):
    pts = []
    for i in range(0, 101):
        a = 8 + i / 10
        v = vel(a)
        pts.append(f"{x0 + (a - 8) / 10 * w:.0f} {y0 - v / 12 * h:.0f}")
    return f'<path d="M {" L ".join(pts)}" stroke="{cor}" stroke-width="{esp}" fill="none"/>'


# 1. a planilha
p = [svg_abre(1664, 450, "Uma planilha de clube com a altura de um jogador medida no início de cada temporada. Ao lado, o dado em gráfico: doze centímetros em um ano, oito nos últimos seis meses. Embaixo, três queixas: dor abaixo da patela, ficou desajeitado, o rendimento caiu")]
p.append(caixa(0, 0, 560, 330, TINTA, CARTAO, esp=2, rx=14))
rs = [rot(24, 18, "Altura · início de temporada", w=520, tam=26, cor=TINTA, peso=700, serif=True)]
for j, (d, h) in enumerate([("jan · ano 1", "1,56 m"), ("jul · ano 1", "1,60 m"), ("jan · ano 2", "1,68 m")]):
    y = 90 + j * 70
    p.append(f'<line x1="24" y1="{y + 50}" x2="536" y2="{y + 50}" stroke="{BORDA}" stroke-width="2"/>')
    rs += [rot(24, y + 8, d, w=260, tam=26, cor=MUDO), rot(300, y + 8, h, w=230, tam=28, cor=TINTA, peso=700, alinha="right")]
rs.append(rot(24, 290, "guardada numa pasta", w=520, tam=22, cor=FOSF, peso=700))
X0, Y0 = 640, 330
p.append(f'<line x1="{X0}" y1="{Y0}" x2="1180" y2="{Y0}" stroke="{TINTA}" stroke-width="3"/>')
pts = [(0, 1.56), (6, 1.60), (12, 1.68)]
P = lambda m, h: (X0 + 40 + m / 12 * 460, Y0 - (h - 1.50) / 0.20 * 280)
d = " L ".join(f"{P(m, h)[0]:.0f} {P(m, h)[1]:.0f}" for m, h in pts)
p.append(f'<path d="M {d}" stroke="{GLIC}" stroke-width="7" fill="none"/>')
for m, h in pts:
    x, y = P(m, h)
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="12" fill="{GLIC}"/>')
rs += [rot(1200, 40, "+12 cm em um ano", w=464, tam=40, cor=GLIC, peso=700, serif=True), rot(1200, 110, "+8 cm nos últimos seis meses", w=464, tam=28, cor=TINTA, peso=700),
       rot(1200, 170, "três pares de tênis no ano", w=464, tam=24, cor=MUDO)]
for j, t in enumerate(["dor abaixo da patela", "ficou desajeitado", "o rendimento caiu"]):
    x = j * 560
    p.append(caixa(x, 370, 520, 80, FOSF, FOSF_T, esp=2, rx=40))
    rs.append(rot(x + 20, 392, "“" + t + "”", w=480, tam=26, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "planilha", 450, p, rs, eyebrow="Um jogador de basquete de base, treze anos", titulo="O dado que explicava tudo estava numa pasta do clube")

# 2. as duas curvas
p = [svg_abre(1664, 420, "Duas curvas. À esquerda, a altura ao longo da idade, uma subida em S. À direita, a velocidade de crescimento, estável na infância, subindo até um pico e caindo até zero. Esquema")]
rs = [rot(0, 0, "Altura", w=700, tam=28, cor=TINTA, peso=700, serif=True), rot(880, 0, "Velocidade de crescimento", w=780, tam=28, cor=TINTA, peso=700, serif=True)]
alt = []
h = 0
for i in range(0, 101):
    a = 8 + i / 10
    h += vel(a) / 10
    alt.append((a, h))
hmax = alt[-1][1]
d = " L ".join(f"{40 + (a - 8) / 10 * 700:.0f} {360 - hh / hmax * 280:.0f}" for a, hh in alt)
p.append(f'<path d="M {d}" stroke="{AZUL}" stroke-width="7" fill="none"/>')
p.append(f'<line x1="40" y1="360" x2="760" y2="360" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="900" y1="360" x2="1640" y2="360" stroke="{TINTA}" stroke-width="3"/>')
p.append(curva_vel(900, 360, 720, 300, OXID, 7))
xp = 900 + 5.6 / 10 * 720
p.append(f'<line x1="{xp:.0f}" y1="60" x2="{xp:.0f}" y2="360" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
rs += [rot(xp + 40, 90, "pico de velocidade de crescimento", w=360, tam=24, cor=FOSF, peso=700, lh=1.2),
       rot(40, 372, "infância", w=200, tam=22, cor=MUDO), rot(900, 372, "infância", w=200, tam=22, cor=MUDO), rot(1440, 372, "esquema", w=200, tam=22, cor=MUDO, alinha="right")]
diagrama(S, "curva", 420, p, rs, eyebrow="O evento que organiza a vulnerabilidade", titulo="O que importa não é a altura, é a velocidade")

# 3. três coisas em volta do pico
p = [svg_abre(1664, 470, "Três quadros. Segmentos crescem fora de sincronia: coordenação cai por um tempo. O osso cresce antes do músculo e do tendão: tração nas apófises. No pico, 90 por cento da estatura adulta e 57 por cento do mineral ósseo: o mineral chega meses depois")]
rs = []
quadros = [("Fora de sincronia", "pernas e pés crescem antes do tronco: a coordenação cai por um tempo", GLIC, GLIC_T),
           ("Osso antes do tendão", "o tendão fica curto e puxa a inserção: apofisite", FOSF, FOSF_T),
           ("Mineral atrasado", "o osso está longo e ainda pouco mineralizado", AZUL, AZUL_T)]
for j, (t, x_, c, f) in enumerate(quadros):
    x = j * 564
    p.append(caixa(x, 0, 536, 470, c, f, esp=3, rx=18))
    rs += [rot(x + 24, 18, t, w=488, tam=30, cor=c, peso=700, serif=True), rot(x + 24, 340, x_, w=488, tam=24, cor=TINTA, peso=600, lh=1.3)]
# quadro 1: figura de proporções desiguais
p.append(f'<circle cx="268" cy="110" r="24" fill="{GLIC}"/><rect x="243" y="140" width="50" height="70" rx="10" fill="{GLIC}"/>')
p.append(f'<rect x="248" y="210" width="16" height="100" rx="6" fill="{GLIC}"/><rect x="272" y="210" width="16" height="100" rx="6" fill="{GLIC}"/>')
p.append(f'<rect x="228" y="306" width="40" height="14" rx="6" fill="{GLIC}"/><rect x="268" y="306" width="40" height="14" rx="6" fill="{GLIC}"/>')
# quadro 2: osso e tendão
p.append(f'<rect x="760" y="90" width="44" height="220" rx="20" fill="{CARTAO}" stroke="{TINTA}" stroke-width="5"/>')
p.append(f'<path d="M 860 80 C 840 140 840 220 806 290" stroke="{FOSF}" stroke-width="10" fill="none"/>')
p.append(f'<circle cx="806" cy="290" r="16" fill="{FOSF}"/>')
rs.append(rot(880, 200, "tração", w=160, tam=24, cor=FOSF, peso=700))
# quadro 3: barras
for k, (v, t) in enumerate([(90, "estatura"), (57, "mineral ósseo")]):
    x = 1180 + k * 200
    p.append(f'<rect x="{x}" y="{300 - v * 2:.0f}" width="120" height="{v * 2:.0f}" rx="8" fill="{AZUL}"/>')
    rs += [rot(x - 20, 300 - v * 2 - 46, f"{v}%", w=160, tam=34, cor=AZUL, peso=700, serif=True, alinha="center"), rot(x - 30, 304, t, w=180, tam=22, cor=TINTA, alinha="center")]
diagrama(S, "tres", 470, p, rs, eyebrow="Em volta do pico", titulo="O estirão é a janela de maior vulnerabilidade da base",
         fonte="Estatura e mineral no pico: estudo longitudinal, J Bone Miner Res 1999")

# 4. medir
p = [svg_abre(1664, 440, "Passo um, medir. Uma parede com marcas de altura a cada três meses, um banco para a altura sentada e uma balança. Regras: sem sapato; calcanhares juntos; olhar na horizontal; mesmo horário, de preferência de manhã; mesmo avaliador; duas ou três medidas e a média")]
p.append(f'<rect x="40" y="20" width="300" height="400" fill="{PAPEL}" stroke="{BORDA}" stroke-width="3"/>')
rs = []
for j, (y, t) in enumerate([(300, "jan"), (270, "abr"), (225, "jul"), (190, "out")]):
    p.append(f'<line x1="60" y1="{y}" x2="200" y2="{y}" stroke="{GLIC}" stroke-width="5"/>')
    rs.append(rot(210, y - 16, t, w=100, tam=22, cor=GLIC, peso=700))
p.append(f'<rect x="420" y="260" width="200" height="160" rx="10" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
rs.append(rot(400, 220, "altura sentada", w=240, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(f'<rect x="680" y="370" width="180" height="50" rx="10" fill="{TINTA}"/>')
rs.append(rot(660, 320, "peso", w=220, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(940, 0, 724, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(964, 20, "A cada três meses, sempre igual", w=680, tam=28, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["sem sapato, calcanhares juntos", "olhar na horizontal", "mesmo horário, de preferência de manhã", "mesmo avaliador e equipamento", "duas ou três medidas, e a média"]):
    rs.append(rot(964, 96 + j * 66, "· " + t, w=680, tam=26, cor=TINTA, peso=600))
diagrama(S, "medir", 440, p, rs, eyebrow="Passo um", titulo="Medir pouco, sempre do mesmo jeito")

# 5. calcular
p = [svg_abre(1664, 420, "Passo dois, calcular. Estatura de hoje menos a de três meses atrás, dividida pelo intervalo em anos. Exemplo: 2 centímetros em 3 meses dão 8 centímetros por ano. Uma pequena curva de velocidade com três pontos: acelerando, no máximo, desacelerando")]
p.append(caixa(0, 0, 800, 420, TINTA, CARTAO, esp=2, rx=18))
rs = [rot(30, 30, "estatura de hoje − de 3 meses atrás", w=740, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(30, 90, "÷ intervalo em anos", w=740, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(30, 210, "2 cm ÷ 0,25 ano", w=740, tam=44, cor=GLIC, peso=700, serif=True, alinha="center"),
      rot(30, 290, "= 8 cm por ano", w=740, tam=56, cor=GLIC, peso=700, serif=True, alinha="center")]
p.append(f'<line x1="120" y1="170" x2="680" y2="170" stroke="{BORDA}" stroke-width="3"/>')
p.append(curva_vel(880, 380, 760, 300, OXID, 6))
for a, t, c in ((12.6, "acelerando", GLIC), (13.6, "no máximo", FOSF), (14.8, "desacelerando", AZUL)):
    x = 880 + (a - 8) / 10 * 760
    y = 380 - vel(a) / 12 * 300
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" fill="{c}" stroke="{CARTAO}" stroke-width="3"/>')
rs += [rot(1020, 120, "acelerando", w=220, tam=24, cor=GLIC, peso=700, alinha="right"),
       rot(1260, 20, "no máximo", w=220, tam=24, cor=FOSF, peso=700, alinha="center"),
       rot(1400, 150, "desacelerando", w=240, tam=24, cor=AZUL, peso=700)]
diagrama(S, "calcular", 420, p, rs, eyebrow="Passo dois", titulo="A velocidade mostra o pico acontecendo")

# 6. ler a fase
p = [svg_abre(1664, 460, "Passo três, ler. Três faixas sobre a curva de velocidade. Acelerando: rever impacto, volume de salto e progressão; conversar. No máximo: reduzir progressão, monitorar dor, qualidade antes de volume. Desacelerando: tolerância voltando; a força pode progredir mais")]
x0, w = 40, 1580
fases = [(8, 12.3, "Acelerando", ["rever impacto e salto", "conversar antes da dor"], GLIC, GLIC_T),
         (12.3, 14.9, "No máximo", ["reduzir progressão", "monitorar a dor", "qualidade antes de volume"], FOSF, FOSF_T),
         (14.9, 18, "Desacelerando", ["tolerância voltando", "a força pode progredir"], AZUL, AZUL_T)]
rs = []
for a0, a1, t, itens, c, f in fases:
    xa, xb = x0 + (a0 - 8) / 10 * w, x0 + (a1 - 8) / 10 * w
    p.append(f'<rect x="{xa + 4:.0f}" y="0" width="{xb - xa - 8:.0f}" height="460" rx="14" fill="{f}"/>')
    rs.append(rot(xa + 20, 16, t, w=xb - xa - 40, tam=30, cor=c, peso=700, serif=True))
    for i, it in enumerate(itens):
        rs.append(rot(xa + 20, 280 + i * 50, "· " + it, w=xb - xa - 40, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(curva_vel(x0, 250, w, 180, TINTA, 6))
diagrama(S, "ler", 460, p, rs, eyebrow="Passo três", titulo="Cada fase do estirão pede um ajuste diferente de carga",
         destaque="Na mesma turma, a carga não deveria ser igual para todos.", destaque_cor="tinta")

# 7. o alerta
p = [svg_abre(1664, 420, "Passo quatro. Uma curva de crescimento caindo de canal, atravessando as faixas de percentil para baixo. Etiqueta: desaceleração inesperada ou queda de canal, avaliação médica, não ajuste de treino. Causas possíveis: energia que falta, doença")]
for k, off in enumerate((0, 50, 100, 150)):
    p.append(f'<path d="M 40 {340 - off} C 300 {300 - off} 600 {200 - off} 900 {170 - off}" stroke="{BORDA}" stroke-width="3" fill="none"/>')
p.append(f'<path d="M 40 240 C 300 200 420 150 520 140 C 640 130 760 170 900 230" stroke="{FOSF}" stroke-width="7" fill="none"/>')
p.append(icone("t:alert-triangle", 640, 60, 60, FOSF))
rs = [rot(0, 380, "faixas de percentil · esquema", w=900, tam=22, cor=MUDO)]
p.append(caixa(980, 0, 684, 220, FOSF, FOSF_T, esp=4, rx=16))
rs.append(rot(1004, 30, "desaceleração inesperada ou queda de canal", w=636, tam=30, cor=FOSF, peso=700, serif=True, lh=1.2, alinha="center"))
rs.append(rot(1004, 140, "avaliação médica, não ajuste de treino", w=636, tam=26, cor=TINTA, peso=700, alinha="center"))
for j, t in enumerate(["energia que falta", "doença"]):
    x = 980 + j * 352
    p.append(caixa(x, 260, 332, 100, MUDO, CARTAO, esp=2, rx=14))
    rs.append(rot(x + 16, 292, t, w=300, tam=26, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "alerta", 420, p, rs, eyebrow="Passo quatro", titulo="Quando a curva cai de canal, o problema não é do treino")

# 8. a conversa
p = [svg_abre(1664, 420, "Três balões de conversa. Para o atleta: o seu corpo cresceu oito centímetros em seis meses; a coordenação volta. Para a família: é passageiro e esperado. Para o treinador: é a fase de maior risco de lesão da carreira dele")]
rs = []
for j, (quem, t, c, f) in enumerate([("Para o atleta", "“seu corpo cresceu oito centímetros em seis meses; a coordenação volta”", GLIC, GLIC_T),
                                      ("Para a família", "“é passageiro e esperado”", AZUL, AZUL_T),
                                      ("Para o treinador", "“é a fase de maior risco de lesão da carreira dele”", FOSF, FOSF_T)]):
    x = j * 564
    p.append(caixa(x, 60, 536, 280, c, f, esp=3, rx=40))
    p.append(f'<path d="M {x + 80} 340 l 20 50 l 40 -50 z" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs += [rot(x, 0, quem, w=536, tam=28, cor=c, peso=700, alinha="center"), rot(x + 30, 130, t, w=476, tam=28, cor=TINTA, peso=600, serif=True, alinha="center", lh=1.3)]
diagrama(S, "conversa", 420, p, rs, eyebrow="O procedimento termina numa conversa", titulo="Explicar o estirão muda o que cada um faz com ele",
         destaque="Reduzir salto e impacto por um tempo, mantendo técnica e grupo, é proteger o investimento.", destaque_cor="tinta")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Pico de velocidade de crescimento e vulnerabilidade", "titulo": "Uma fita métrica vê a janela antes da lesão",
          "regras": ["Os meses do estirão são a janela de maior vulnerabilidade da base",
                     "Altura a cada três meses, transformada em velocidade, mostra a fase",
                     "Curva que cai de canal vai para o médico, não para a planilha de treino"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Mede, calcula a velocidade e ajusta impacto e progressão."},
                    {"ic": "h:doctor-female", "t": "Fisioterapia", "x": "Acompanha a dor nas inserções e conduz o fortalecimento."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Avalia a curva que cai e o crescimento que para."}]})

salvar("12-02.json", {"arquivo": "aulas/MOD12/12-02-pico-de-velocidade-de-crescimento-e-vulnerabilidade.md",
                      "titulo": "Pico de velocidade de crescimento e vulnerabilidade", "subtitulo": "Medir, calcular, ler e alertar",
                      "nota_capa": "Entra por um jogador de basquete que cresceu doze centímetros em um ano.",
                      "secoes": {"planilha": ["O dado esquecido.", "capa"], "curva": ["O que acontece no pico.", "curva"],
                                 "medir": ["Os quatro passos.", "medir"], "conversa": ["A conversa.", "conversa"]},
                      "slides": S})
