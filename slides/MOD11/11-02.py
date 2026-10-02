"""Spec do deck 11.2. Gera 11-02.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o aplicativo e a palavra
p = [svg_abre(1664, 480, "Um celular com um aplicativo de ciclo dividindo o mês em quatro blocos coloridos: força, leve, descanso, aeróbio. Ao lado, em letra grande, a palavra trivialmente, da conclusão de uma metanálise de 2020")]
p.append(f'<rect x="60" y="0" width="420" height="480" rx="48" fill="{TINTA}"/>')
p.append(f'<rect x="84" y="40" width="372" height="400" rx="20" fill="{PAPEL}"/>')
rs = [rot(84, 56, "seu mês", w=372, tam=24, cor=MUDO, peso=700, alinha="center")]
for j, (t, c) in enumerate([("força", FOSF), ("leve", GLIC), ("descanso", AZUL), ("aeróbio", OXID)]):
    y = 104 + j * 80
    p.append(f'<rect x="108" y="{y}" width="324" height="64" rx="12" fill="{c}"/>')
    rs.append(rot(108, y + 16, f"semana {j + 1} · {t}", w=324, tam=26, cor=PAPEL, peso=700, alinha="center"))
p.append(f'<line x1="540" y1="240" x2="640" y2="240" stroke="{BORDA}" stroke-width="4"{TRACO}/>')
rs += [rot(680, 70, "“O desempenho pode estar", w=980, tam=34, cor=TINTA, serif=True),
       rot(680, 150, "trivialmente", w=980, tam=96, cor=FOSF, peso=700, serif=True),
       rot(680, 290, "reduzido na fase folicular precoce.”", w=980, tam=34, cor=TINTA, serif=True),
       rot(680, 380, "oito meses evitando carga alta em duas semanas de cada mês", w=960, tam=26, cor=MUDO, lh=1.3)]
diagrama(S, "app", 480, p, rs, eyebrow="Uma praticante de musculação e um aplicativo", titulo="Uma palavra para desmontar: trivialmente",
         fonte="Metanálise de 2020, mulheres com ciclo regular e sem contracepção hormonal")

# 2. o eixo em pulsos
p = [svg_abre(1664, 480, "O eixo em três andares: hipotálamo, hipófise e ovário, ligados por setas, com retorno do ovário para cima. Na saída do hipotálamo, um trem de pulsos regulares. Ao lado, um prato vazio encostado nos pulsos: é aqui que a energia interfere"), defs(TINTA, MUDO)]
rs = []
for j, (t, sub, c) in enumerate([("Hipotálamo", "libera em pulsos", AZUL), ("Hipófise", "FSH e LH", OXID), ("Ovário", "estradiol e progesterona", FOSF)]):
    y = j * 170
    p.append(caixa(0, y, 460, 130, c, CARTAO, esp=4, rx=18))
    rs += [rot(24, y + 22, t, w=420, tam=34, cor=c, peso=700, serif=True), rot(24, y + 76, sub, w=420, tam=26, cor=TINTA)]
    if j < 2:
        p.append(seta(230, y + 134, 230, y + 164, TINTA, "m0", esp=4))
p.append(f'<path d="M 464 405 C 560 405, 560 65, 464 65" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO} marker-end="url(#m1)"/>')
rs.append(rot(560, 220, "o retorno regula os andares de cima", w=300, tam=22, cor=MUDO, lh=1.25))
pul = "M 880 160"
for k in range(8):
    x = 880 + k * 90
    pul += f" L {x + 30} 160 L {x + 38} 60 L {x + 46} 160 L {x + 90} 160"
p.append(f'<path d="{pul}" fill="none" stroke="{AZUL}" stroke-width="5"/>')
rs.append(rot(880, 190, "pulsos regulares: o eixo bate, não escorre", w=760, tam=26, cor=AZUL, peso=700))
p.append(caixa(880, 270, 784, 210, GLIC, GLIC_T, esp=3, rx=18))
p.append(f'<ellipse cx="990" cy="375" rx="80" ry="60" fill="{CARTAO}" stroke="{GLIC}" stroke-width="5"/>')
p.append(f'<ellipse cx="990" cy="375" rx="44" ry="32" fill="none" stroke="{GLIC}" stroke-width="3"/>')
rs += [rot(1100, 300, "É aqui que a energia interfere", w=540, tam=30, cor=GLIC, peso=700, serif=True, lh=1.2),
       rot(1100, 390, "sem energia, os pulsos rareiam e o ovário perde o comando", w=540, tam=24, cor=TINTA, lh=1.3)]
diagrama(S, "eixo", 480, p, rs, eyebrow="Onde o ciclo começa", titulo="O ciclo começa no cérebro, e bate em pulsos")

# 3. as três fases
p = [svg_abre(1664, 500, "Um ciclo de 28 dias com as curvas de estradiol e progesterona sobrepostas, em esquema. Três faixas embaixo: folicular precoce, com os dois hormônios baixos; folicular tardia, com o estradiol subindo até o pico; lútea, com a progesterona alta. Uma linha de temperatura sobe alguns décimos depois da ovulação")]
x0, x1, yb = 60, 1600, 330
DX = lambda d: x0 + (d - 1) / 27 * (x1 - x0)
def curva(f):
    return " ".join(f"{DX(d / 4):.0f},{yb - f(d / 4):.0f}" for d in range(4, 113))
estr = lambda d: 40 + 200 * math.exp(-((d - 13) / 2.2) ** 2) + 90 * math.exp(-((d - 21) / 3.5) ** 2)
prog = lambda d: 15 + 230 * math.exp(-((d - 21.5) / 3.6) ** 2)
p.append(f'<polyline points="{curva(estr)}" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<polyline points="{curva(prog)}" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append(f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="{TINTA}" stroke-width="2"/>')
p.append(f'<line x1="{DX(14):.0f}" y1="20" x2="{DX(14):.0f}" y2="{yb}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
temp = " ".join(f"{DX(d):.0f},{(40 if d > 14.5 else 62):.0f}" for d in [1, 14, 14.5, 15, 28])
p.append(f'<polyline points="{temp}" fill="none" stroke="{GLIC}" stroke-width="3"/>')
rs = [rot(DX(9.5) - 120, 60, "estradiol", w=200, tam=26, cor=FOSF, peso=700, alinha="right"),
      rot(DX(24), 70, "progesterona", w=260, tam=26, cor=AZUL, peso=700),
      rot(DX(14) + 10, 0, "ovulação", w=200, tam=22, cor=MUDO),
      rot(DX(1), 0, "temperatura: alguns décimos acima depois da ovulação", w=640, tam=22, cor=GLIC, peso=700)]
for d0, d1, t, sub, c in [(1, 6, "folicular precoce", "os dois baixos", OXID), (6, 14, "folicular tardia", "estradiol sobe ao pico", FOSF), (14, 28, "lútea", "progesterona alta", AZUL)]:
    p.append(f'<rect x="{DX(d0):.0f}" y="360" width="{DX(d1) - DX(d0) - 6:.0f}" height="140" rx="12" fill="{CARTAO}" stroke="{c}" stroke-width="3"/>')
    rs += [rot(DX(d0) + 14, 376, t, w=DX(d1) - DX(d0) - 30, tam=26, cor=c, peso=700, lh=1.15), rot(DX(d0) + 14, 446, sub, w=DX(d1) - DX(d0) - 30, tam=22, cor=TINTA, lh=1.2)]
diagrama(S, "fases", 500, p, rs, eyebrow="Três fases que interessam a quem prescreve", titulo="Dois hormônios, três ambientes, e a temperatura que sobe",
         fonte="Curvas em esquema, sem valores medidos")

# 4. a duração e o erro do calendário
p = [svg_abre(1664, 470, "Três ciclos alinhados pelo fim, de 24, 28 e 35 dias. A fase lútea tem o mesmo comprimento nos três; a folicular estica ou encolhe. A marca do dia 14 do aplicativo cai no lugar certo só no ciclo de 28 dias")]
DX = lambda d: 1600 - d * 40
rs = []
for j, n in enumerate([24, 28, 35]):
    y = 40 + j * 120
    p.append(f'<rect x="{DX(n):.0f}" y="{y}" width="{(n - 14) * 40}" height="70" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<rect x="{DX(14):.0f}" y="{y}" width="{14 * 40}" height="70" rx="10" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    xa = DX(n) + 14 * 40
    p.append(f'<path d="M{xa:.0f} {y - 6} l -12 -22 l 24 0 Z" fill="{FOSF if n != 28 else OXID}"/>')
    rs += [rot(DX(n) - 170, y + 18, f"{n} dias", w=150, tam=28, cor=TINTA, peso=700, alinha="right"),
           rot(DX(14) + 10, y + 20, "lútea, quase igual", w=540, tam=24, cor=AZUL, peso=600, alinha="center")]
rs += [rot(DX(35), 410, "o triângulo marca o dia 14 contado do sangramento: só acerta a ovulação no ciclo de 28", w=1400, tam=24, cor=FOSF, peso=700),
       rot(0, 0, "folicular: é ela que varia", w=600, tam=24, cor=FOSF, peso=700)]
diagrama(S, "duracao", 470, p, rs, eyebrow="De 21 a 35 dias", titulo="Quem estica o ciclo é a fase folicular; contar dias erra a ovulação",
         destaque="Os ciclos dela iam de 32 a 41 dias. O aplicativo contava 28.", destaque_cor="verm")

# 5. regular não é ovulatório
p = [svg_abre(1664, 420, "Em cima, um calendário com o sangramento sempre na data certa: o calendário parece normal. Embaixo, uma barra dos ciclos de mulheres que treinam, todos com intervalo de 26 a 35 dias: 50% ovulatórios, 29% com fase lútea insuficiente, 21% sem ovulação")]
rs = []
for j in range(3):
    x = j * 300
    p.append(caixa(x, 0, 270, 150, MUDO, CARTAO, esp=2, rx=12))
    for d in range(28):
        c = FOSF if d < 5 else BORDA
        p.append(f'<rect x="{x + 16 + (d % 7) * 35}" y="{16 + (d // 7) * 32}" width="28" height="24" rx="4" fill="{c}"/>')
rs.append(rot(940, 40, "O calendário parece normal", w=720, tam=32, cor=TINTA, peso=700, serif=True))
rs.append(rot(940, 96, "sangramento na data certa, ciclo após ciclo", w=720, tam=26, cor=MUDO))
xs = 0
for v, t, c in [(50.0, "50% ovulatórios", OXID), (29.2, "29% fase lútea insuficiente", GLIC), (20.8, "21% sem ovulação", FOSF)]:
    w = v / 100 * 1664
    p.append(f'<rect x="{xs:.0f}" y="210" width="{w - 4:.0f}" height="110" rx="10" fill="{c}"/>')
    rs.append(rot(xs + 16, 244, t, w=w - 30, tam=28, cor=PAPEL, peso=700, lh=1.15))
    xs += w
rs.append(rot(0, 350, "ciclos de mulheres que treinam, todos de 26 a 35 dias, com hormônios medidos todos os dias", w=1664, tam=24, cor=MUDO))
diagrama(S, "regular", 420, p, rs, eyebrow="A armadilha silenciosa", titulo="Ciclo regular não garante ovulação",
         fonte="Hum Reprod 2010 · dois a três ciclos seguidos por participante")

# 6. do receptor ao desempenho
p = [svg_abre(1664, 460, "À esquerda, um corpo com receptores de estradiol marcados em músculo, osso, tendão, vaso e cérebro. À direita, a frase treine diferente na fase folicular. Entre os dois, uma distância longa marcada do mecanismo ao desempenho, com degraus de promessa, infográfico e aplicativo, e um ponto de interrogação"), defs(MUDO)]
p.append(icone("h:woman", 40, 0, 420, MUDO))
rs = []
for t, x, y in [("cérebro", 330, 20), ("vaso", 330, 120), ("músculo", 330, 200), ("osso", 330, 290), ("tendão", 330, 380)]:
    p.append(f'<circle cx="300" cy="{y + 18}" r="12" fill="{FOSF}"/>')
    rs.append(rot(x, y, t, w=200, tam=26, cor=FOSF, peso=700))
for j, t in enumerate(["receptor", "promessa", "infográfico", "aplicativo"]):
    x = 560 + j * 200
    p.append(caixa(x, 300 - j * 70, 180, 70, GLIC, GLIC_T, esp=2, rx=10))
    rs.append(rot(x, 318 - j * 70, t, w=180, tam=24, cor=TINTA, peso=600, alinha="center"))
p.append(caixa(1380, 20, 284, 200, TINTA, TINTA, esp=0, rx=16))
rs += [rot(1400, 50, "“Treine diferente na fase folicular”", w=244, tam=28, cor=PAPEL, peso=700, serif=True, lh=1.25),
       rot(560, 400, "em nenhum degrau alguém mediu desempenho", w=820, tam=28, cor=FOSF, peso=700)]
diagrama(S, "receptor", 460, p, rs, eyebrow="O que os hormônios fazem fora do útero", titulo="Ter receptor no tendão não é treinar diferente na fase folicular")

# 7. a metanálise e o denominador
p = [svg_abre(1664, 470, "Gráfico de floresta em esquema: o efeito da fase folicular precoce um pouco à esquerda do zero, com intervalos largos. Embaixo, a qualidade dos 78 estudos: 8% alta, 24% média, 42% baixa, 26% muito baixa")]
cx = 560
p.append(f'<line x1="{cx}" y1="0" x2="{cx}" y2="250" stroke="{TINTA}" stroke-width="3"/>')
rs = [rot(cx + 14, 256, "nenhum efeito", w=200, tam=22, cor=MUDO)]
for j, (m, a) in enumerate([(-30, 140), (10, 180), (-60, 120), (-5, 200), (-20, 90)]):
    y = 30 + j * 42
    p.append(f'<line x1="{cx + m - a}" y1="{y}" x2="{cx + m + a}" y2="{y}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<rect x="{cx + m - 8}" y="{y - 8}" width="16" height="16" fill="{MUDO}"/>')
p.append(f'<path d="M {cx - 40} 236 l 24 -12 l 24 12 l -24 12 Z" fill="{FOSF}"/>')
rs.append(rot(cx - 330, 256, "folicular precoce: trivialmente abaixo", w=290, tam=22, cor=FOSF, peso=700, alinha="right", lh=1.2))
p.append(caixa(1000, 0, 664, 250, OXID, OXID_T, esp=3, rx=16))
rs += [rot(1024, 20, "78 estudos", w=620, tam=48, cor=OXID, peso=700, serif=True),
       rot(1024, 100, "1.193 participantes com ciclo regular, sem contracepção hormonal", w=620, tam=26, cor=TINTA, lh=1.3),
       rot(1024, 190, "força: nenhuma influência demonstrada (revisão de 2023)", w=620, tam=22, cor=OXID, peso=700)]
xs = 0
for v, t, c in [(8, "8% alta", OXID), (24, "24% média", AZUL), (42, "42% baixa", GLIC), (26, "26% muito baixa", FOSF)]:
    w = v / 100 * 1664
    p.append(f'<rect x="{xs:.0f}" y="320" width="{w - 4:.0f}" height="90" rx="10" fill="{c}"/>')
    rs.append(rot(xs + 6, 344, t, w=w - 12, tam=24 if v > 8 else 20, cor=PAPEL, peso=700, alinha="center"))
    xs += w
rs.append(rot(0, 428, "qualidade dos estudos · boa parte definiu a fase contando dias, sem dosar hormônio", w=1664, tam=22, cor=MUDO))
diagrama(S, "metanalise", 470, p, rs, eyebrow="O número, e o denominador", titulo="Um efeito abaixo de pequeno, medido por estudos em sua maioria fracos",
         fonte="Sports Med 2020 · revisão sobre força, Front Sports Act Living 2023 · intervalos em esquema")

# 8. média pequena, dispersão grande
p = [svg_abre(1664, 470, "Nuvem de pontos, cada ponto o efeito da fase numa mulher diferente, espalhados dos dois lados do zero; a média quase em cima do zero. Embaixo, duas setas de tempo: planejar pela fase prevista, riscada; ajustar pelo sintoma do dia, marcada"), defs(FOSF, OXID)]
cx = 832
p.append(f'<line x1="{cx}" y1="0" x2="{cx}" y2="250" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
import random
random.seed(11)
for i in range(70):
    v = random.gauss(-25, 210)
    y = 20 + random.random() * 210
    p.append(f'<circle cx="{cx + v:.0f}" cy="{y:.0f}" r="9" fill="{AZUL}" opacity="0.6"/>')
p.append(f'<line x1="{cx - 25}" y1="0" x2="{cx - 25}" y2="250" stroke="{FOSF}" stroke-width="5"/>')
rs = [rot(cx - 25 - 160, 0, "média", w=140, tam=24, cor=FOSF, peso=700, alinha="right"),
      rot(60, 100, "rende menos nesses dias", w=300, tam=24, cor=TINTA, lh=1.2), rot(1320, 100, "rende mais", w=300, tam=24, cor=TINTA, alinha="right"),
      rot(cx - 300, 256, "cada ponto, uma mulher · esquema", w=600, tam=20, cor=MUDO, alinha="center")]
for j, (t, c, mk, ok) in enumerate([("planejar pela fase prevista", FOSF, "m0", False), ("ajustar pelo sintoma do dia", OXID, "m1", True)]):
    x = j * 844
    p.append(caixa(x, 310, 820, 160, c, FOSF_T if not ok else OXID_T, esp=3, rx=16))
    p.append(seta(x + 30, 430, x + 300, 430, c, mk, esp=5) if ok else seta(x + 300, 430, x + 30, 430, c, mk, esp=5))
    p.append(icone("t:check" if ok else "t:x", x + 720, 330, 64, c))
    rs += [rot(x + 30, 330, t, w=660, tam=30, cor=c, peso=700, serif=True), rot(x + 330, 410, "reage ao que está acontecendo" if ok else "prevê, com um modelo que erra a data", w=460, tam=22, cor=TINTA)]
diagrama(S, "dispersao", 470, p, rs, eyebrow="O que a média esconde", titulo="Quando a dispersão é maior que o efeito, a média não serve para a pessoa")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Ciclo menstrual: fases e efeitos", "titulo": "O efeito é trivial; a dúvida se resolve nela, não na média",
          "regras": ["Manter o treino contínuo, sem blocos por fase prevista",
                     "Ajustar o dia pelo sintoma do dia",
                     "Perguntar pelos meses sem menstruar antes de qualquer pergunta de fase"],
          "cards": [{"ic": "t:barbell", "t": "Quem prescreve treino", "x": "Mantém o programa contínuo e ajusta pelo dia, não pelo aplicativo."},
                    {"ic": "t:clipboard-list", "t": "Quem avalia", "x": "Pergunta pelo ciclo, pela duração e pelos meses sem menstruar."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Investiga quando o calendário mostra falha do eixo."}]})

salvar("11-02.json", {"arquivo": "aulas/MOD11/11-02-ciclo-menstrual-fases-e-efeitos.md",
                      "titulo": "Ciclo menstrual: fases e efeitos", "subtitulo": "O que acontece no ciclo, e o que isso faz no desempenho",
                      "nota_capa": "Entra por uma praticante de musculação que treinava pelo aplicativo.",
                      "secoes": {"app": ["A pergunta.", "capa"], "eixo": ["O ciclo por dentro.", "eixo"],
                                 "metanalise": ["O número.", "metanalise"]},
                      "slides": S})
