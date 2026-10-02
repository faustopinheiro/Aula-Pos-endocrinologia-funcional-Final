"""Spec do deck 11.1. Gera 11-01.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a régua do masculino
p = [svg_abre(1664, 500, "Duas réguas de velocidade de 0 a 30 km/h. Em cima, o corte de alta velocidade do masculino em 19,8. Embaixo, a distribuição de velocidades de uma jogadora: quase toda a corrida intensa fica abaixo de 19,8 e some do relatório")]
x0, x1 = 80, 1580
X = lambda v: x0 + v / 30 * (x1 - x0)
rs = []
for k, y in enumerate([150, 420]):
    p.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{TINTA}" stroke-width="3"/>')
    for v in range(0, 31, 5):
        p.append(f'<line x1="{X(v):.0f}" y1="{y}" x2="{X(v):.0f}" y2="{y + 14}" stroke="{TINTA}" stroke-width="2"/>')
        if k == 1:
            rs.append(rot(X(v) - 40, y + 20, f"{v}", w=80, tam=22, cor=MUDO, alinha="center"))
p.append(f'<rect x="{X(19.8):.0f}" y="90" width="{X(30) - X(19.8):.0f}" height="60" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
rs.append(rot(X(19.8) + 16, 104, "alta velocidade, no relatório do masculino", w=X(30) - X(19.8) - 24, tam=24, cor=FOSF, peso=700))
pts = []
for i in range(121):
    v = i / 4
    d = 235 * math.exp(-((v - 9) / 4.6) ** 2) + 70 * math.exp(-((v - 16) / 2.6) ** 2)
    pts.append(f"{X(v):.0f},{420 - d:.0f}")
p.append(f'<polygon points="{X(0):.0f},420 ' + " ".join(pts) + f' {X(30):.0f},420" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
p.append(f'<line x1="{X(19.8):.0f}" y1="60" x2="{X(19.8):.0f}" y2="430" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
rs += [rot(X(19.8) - 60, 20, "19,8 km/h", w=200, tam=26, cor=FOSF, peso=700, alinha="center"),
       rot(X(9) - 210, 300, "a corrida intensa dela acontece aqui", w=420, tam=26, cor=OXID, peso=700, alinha="center", lh=1.2),
       rot(X(21), 330, "e quase nada passa da linha", w=440, tam=24, cor=TINTA),
       rot(x0, 474, "km/h · distribuição de velocidades em esquema, sem valores medidos", w=1400, tam=22, cor=MUDO)]
diagrama(S, "regua", 500, p, rs, eyebrow="Um time feminino que herdou tudo do masculino", titulo="O relatório dizia que elas não corriam. A régua é que não as via")

# 2. os limiares próprios
p = [svg_abre(1664, 470, "Régua de 0 a 30 km/h com os cortes do masculino em cima, 19,8 e 25,2, e os três cortes propostos em 2015 para o futebol feminino de elite embaixo: 12,5, 19,0 e 22,5. Ao lado, o limiar relativo: a fração da velocidade máxima de cada jogadora"), defs(OXID)]
x0, x1 = 60, 1100
X = lambda v: x0 + v / 30 * (x1 - x0)
rs = []
p.append(f'<line x1="{x0}" y1="200" x2="{x1}" y2="200" stroke="{TINTA}" stroke-width="4"/>')
for v in range(0, 31, 5):
    rs.append(rot(X(v) - 30, 214, f"{v}", w=60, tam=22, cor=MUDO, alinha="center"))
for v, t in [(19.8, "19,8"), (25.2, "25,2")]:
    p.append(f'<path d="M{X(v):.0f} 196 l -14 -40 l 28 0 Z" fill="{MUDO}"/>')
    rs.append(rot(X(v) - 50, 110, t, w=100, tam=26, cor=MUDO, peso=700, alinha="center"))
for v, t in [(12.5, "12,5"), (19.0, "19,0"), (22.5, "22,5")]:
    p.append(f'<path d="M{X(v):.0f} 254 l -14 40 l 28 0 Z" fill="{OXID}"/>')
    rs.append(rot(X(v) - 50, 302, t, w=100, tam=26, cor=OXID, peso=700, alinha="center"))
rs += [rot(x0, 40, "cortes do masculino", w=600, tam=24, cor=MUDO, peso=700),
       rot(x0, 360, "cortes propostos para o futebol feminino de elite", w=900, tam=24, cor=OXID, peso=700),
       rot(x0, 400, "alta · muito alta · sprint", w=900, tam=22, cor=MUDO)]
p.append(caixa(1160, 20, 504, 430, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:run", 1190, 50, 64, OXID))
rs += [rot(1270, 62, "Melhor ainda", w=370, tam=30, cor=OXID, peso=700, serif=True),
       rot(1190, 150, "o limiar relativo: uma fração da velocidade máxima de cada jogadora", w=450, tam=27, cor=TINTA, peso=600, lh=1.3),
       rot(1190, 310, "resolve o sexo e a diferença dentro do próprio elenco", w=450, tam=25, cor=OXID, lh=1.3)]
diagrama(S, "limiares", 470, p, rs, eyebrow="Medir as próprias jogadoras", titulo="Mesmo jogo, mesmo colete: muda a régua, vira a conclusão",
         fonte="Futebol feminino de elite, Int J Sports Physiol Perform 2015 · 19,8 e 25,2 são cortes de uso comum no masculino")

# 3. o pêndulo
p = [svg_abre(1664, 480, "Um pêndulo entre dois extremos. À esquerda, o descaso: a mulher tratada como homem menor e a amenorreia que passa batida. À direita, o exagero: o mês dividido em fases coloridas, cada uma com um treino vendido. No meio, parado, o ponto defensável")]
p.append(f'<line x1="832" y1="20" x2="832" y2="300" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<path d="M 832 20 L 470 250" stroke="{CINZA}" stroke-width="3"{TRACO}/>')
p.append(f'<path d="M 832 20 L 1194 250" stroke="{CINZA}" stroke-width="3"{TRACO}/>')
p.append(f'<path d="M 360 330 Q 832 470 1304 330" fill="none" stroke="{BORDA}" stroke-width="4"/>')
p.append(f'<circle cx="832" cy="330" r="46" fill="{OXID}"/>')
p.append(caixa(0, 40, 520, 400, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:eye-off", 30, 70, 64, FOSF))
p.append(caixa(1144, 40, 520, 400, GLIC, GLIC_T, esp=3, rx=18))
for j, c in enumerate([FOSF, GLIC, OXID, AZUL]):
    p.append(f'<rect x="{1180 + j * 112}" y="76" width="100" height="56" rx="10" fill="{c}" opacity="0.75"/>')
rs = [rot(110, 78, "Descaso", w=380, tam=34, cor=FOSF, peso=700, serif=True),
      rot(30, 170, "a mulher tratada como homem menor", w=460, tam=27, cor=TINTA, peso=600, lh=1.3),
      rot(30, 290, "e a amenorreia que ninguém pergunta", w=460, tam=25, cor=FOSF, lh=1.3),
      rot(1174, 160, "Exagero", w=460, tam=34, cor=GLIC, peso=700, serif=True),
      rot(1174, 220, "cada fase do mês com um treino vendido", w=460, tam=27, cor=TINTA, peso=600, lh=1.3),
      rot(1174, 330, "duas semanas sem treino forte, à toa", w=460, tam=25, cor=GLIC, lh=1.3),
      rot(582, 412, "uma variável clínica relevante, entre várias", w=500, tam=27, cor=OXID, peso=700, alinha="center", lh=1.25)]
diagrama(S, "pendulo", 480, p, rs, eyebrow="O erro de quem corrige o erro", titulo="Os dois extremos decidem pela mulher sem medir a mulher")

# 4. a puberdade e o ponto de partida
p = [svg_abre(1664, 520, "À esquerda, duas curvas de desempenho dos 6 aos 25 anos, uma por sexo: juntas até perto dos 12 e separadas depois da puberdade, estabilizando numa diferença de 8% a 12% em corrida e natação. À direita, as faixas de testosterona circulante de mulheres e homens adultos, que não se encostam. Embaixo, o mesmo programa de força: resposta relativa semelhante")]
gx0, gx1, gy0, gy1 = 70, 900, 40, 380
IX = lambda a: gx0 + (a - 6) / 19 * (gx1 - gx0)
def curva(f, cor):
    return '<polyline points="' + " ".join(f"{IX(a / 4):.0f},{gy1 - f(a / 4) * (gy1 - gy0):.0f}" for a in range(24, 101)) + f'" fill="none" stroke="{cor}" stroke-width="6"/>'
base = lambda a: min(1.0, 0.25 + 0.75 / (1 + math.exp(-(a - 13) / 1.8)))
p.append(f'<line x1="{gx0}" y1="{gy1}" x2="{gx1}" y2="{gy1}" stroke="{TINTA}" stroke-width="2"/>')
p.append(curva(lambda a: base(a) * 0.95, AZUL))
p.append(curva(lambda a: base(a) * (0.95 - 0.1 / (1 + math.exp(-(a - 13.5) / 1.2))), FOSF))
p.append(f'<line x1="{IX(12):.0f}" y1="{gy0}" x2="{IX(12):.0f}" y2="{gy1}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
rs = [rot(IX(6) - 20, gy1 + 10, "6 anos", w=120, tam=22, cor=MUDO), rot(IX(25) - 100, gy1 + 10, "25 anos", w=120, tam=22, cor=MUDO, alinha="right"),
      rot(IX(12) - 90, gy1 + 10, "puberdade", w=180, tam=22, cor=MUDO, alinha="center"),
      rot(IX(19), 0, "homens", w=200, tam=24, cor=AZUL, peso=700), rot(IX(19), 150, "mulheres", w=200, tam=24, cor=FOSF, peso=700),
      rot(IX(15), 230, "8% a 12% em corrida e natação", w=360, tam=24, cor=TINTA, peso=600)]
p.append(caixa(960, 20, 704, 360, TINTA, CARTAO, esp=2, rx=16))
TX = lambda v: 1000 + v / 30 * 620
for k, (a, b, t, c) in enumerate([(0, 1.7, "mulheres", FOSF), (7.7, 29.4, "homens", AZUL)]):
    y = 150 + k * 110
    p.append(f'<rect x="{TX(a):.0f}" y="{y}" width="{max(TX(b) - TX(a), 14):.0f}" height="44" rx="8" fill="{c}"/>')
    rs.append(rot(TX(b) + 14 if k == 0 else TX(a), y - 36, t, w=200, tam=24, cor=c, peso=700))
rs += [rot(984, 40, "Testosterona circulante, adultos", w=660, tam=26, cor=TINTA, peso=700, serif=True),
       rot(984, 330, "faixas que não se encostam · nmol/L", w=660, tam=22, cor=MUDO)]
p.append(caixa(0, 430, 1664, 90, OXID, OXID, esp=0, rx=14))
rs.append(rot(30, 452, "Mesmo programa de força: hipertrofia e força relativas semelhantes; nos braços, elas ganham mais", w=1600, tam=27, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "puberdade", 520, p, rs, eyebrow="O que de fato difere", titulo="Outro ponto de partida, a mesma resposta ao treino",
         fonte="Endocr Rev 2018 · metanálise de treino de força, J Strength Cond Res 2020 · curvas em esquema")

# 5. as diferenças que mudam conduta
p = [svg_abre(1664, 470, "Quatro quadros. Fadiga: numa contração sustentada de mesma intensidade, a força da mulher cai mais devagar, mas depende da tarefa. Ferro: perda menstrual somada ao treino. Energia, ciclo e osso: o eixo em que o déficit aparece primeiro. Joelho e assoalho pélvico: o corpo que o esporte masculino não precisou olhar")]
rs = []
quadros = [("Fadiga", "em contração sustentada, ela costuma cansar mais devagar; depende da tarefa", OXID, OXID_T),
           ("Ferro", "perda menstrual somada ao treino: pergunte pelo volume do sangramento", FOSF, FOSF_T),
           ("Energia, ciclo e osso", "onde o déficit aparece primeiro, e onde o descaso cobra mais caro", GLIC, GLIC_T),
           ("Joelho e assoalho", "mais lesão do cruzado; perda urinária que ninguém pergunta", AZUL, AZUL_T)]
for k, (t, x_, c, f) in enumerate(quadros):
    x = k * 421
    p.append(caixa(x, 0, 401, 470, c, f, esp=3, rx=16))
    rs += [rot(x + 24, 20, t, w=360, tam=28, cor=c, peso=700, serif=True, lh=1.15), rot(x + 24, 300, x_, w=356, tam=24, cor=TINTA, lh=1.3)]
for k, (cor, q) in enumerate([(AZUL, 0.45), (FOSF, 0.2)]):
    p.append(f'<polyline points="' + " ".join(f"{30 + i * 34},{110 + q * i * i * 2.2:.0f}" for i in range(11)) + f'" fill="none" stroke="{cor}" stroke-width="5"/>')
p.append(f'<path d="M 636 110 C 600 160, 600 200, 636 220 C 672 200, 672 160, 636 110 Z" fill="{FOSF}"/>')
p.append(icone("t:calendar", 520, 130, 64, FOSF))
p.append(icone("t:salad", 890, 110, 72, GLIC))
p.append(f'<rect x="1000" y="140" width="150" height="34" rx="17" fill="{GLIC}" opacity="0.6"/>')
p.append(icone("h:woman", 1350, 100, 150, AZUL))
p.append(f'<circle cx="1410" cy="200" r="16" fill="{FOSF}"/><circle cx="1428" cy="168" r="12" fill="{GLIC}"/>')
rs += [rot(24, 240, "homens · mulheres, em esquema", w=360, tam=20, cor=MUDO)]
diagrama(S, "quatro", 470, p, rs, eyebrow="Onde a diferença muda a conduta", titulo="Quatro lugares. Fora deles, o princípio geral costuma servir",
         fonte="Fadiga: revisão, Acta Physiol 2014")

# 6. o déficit de evidência
p = [svg_abre(1664, 470, "Uma grade de cem quadrados representando os participantes da pesquisa em ciência do esporte, 66 homens e 34 mulheres. Ao lado, duas barras: 31% dos estudos só com homens, 6% só com mulheres. Embaixo, a porta do laboratório marcada variável demais")]
rs = []
for i in range(100):
    c = AZUL if i < 66 else FOSF
    p.append(f'<rect x="{(i % 10) * 44}" y="{(i // 10) * 44}" width="38" height="38" rx="6" fill="{c}" opacity="0.85"/>')
rs += [rot(460, 40, "66% homens", w=300, tam=30, cor=AZUL, peso=700), rot(460, 330, "34% mulheres", w=300, tam=30, cor=FOSF, peso=700),
       rot(0, 448, "participantes de 5.261 artigos, 2014 a 2020", w=760, tam=20, cor=MUDO)]
for k, (v, t, c) in enumerate([(31, "dos estudos só com homens", AZUL), (6, "só com mulheres", FOSF)]):
    y = 40 + k * 130
    p.append(f'<rect x="820" y="{y + 50}" width="{v * 24}" height="50" rx="8" fill="{c}"/>')
    rs += [rot(820, y, f"{v}%", w=200, tam=40, cor=c, peso=700, serif=True), rot(960, y + 6, t, w=680, tam=26, cor=TINTA, peso=600)]
p.append(caixa(820, 320, 844, 150, TINTA, CARTAO, esp=2, rx=16))
p.append(icone("t:door", 846, 350, 80, MUDO))
rs += [rot(946, 340, "Excluir quem tem ciclo saía mais barato", w=700, tam=28, cor=TINTA, peso=700, serif=True),
       rot(946, 394, "fase, ovulação, contracepção: tudo encarece", w=700, tam=24, cor=MUDO)]
diagrama(S, "deficit", 470, p, rs, eyebrow="Por que se sabe menos sobre elas", titulo="A literatura ficou limpa, e fala pouco de quem mais procura atendimento",
         fonte="Levantamento de 2021 em seis revistas da área · guia de padrões para estudos com mulheres, Sports Med 2021")

# 7. os dois baldes
p = [svg_abre(1664, 480, "Dois baldes. Extrapolar é razoável: força e progressão de carga, sono, princípios de periodização, mecânica da reabilitação. Extrapolar é arriscado: limiares de energia, osso, gestação e pós-parto, assoalho pélvico, cruzado, calor e hidratação, eixo reprodutivo. Entre eles, a pergunta: o desfecho depende de hormônio sexual?")]
rs = []
for k, (t, itens, c, f) in enumerate([("Extrapolar é razoável", ["força e progressão de carga", "sono e desempenho", "princípios de periodização", "mecânica da reabilitação"], OXID, OXID_T),
                                      ("Extrapolar é arriscado", ["limiares de energia e osso", "gestação e pós-parto", "assoalho pélvico", "cruzado, calor e hidratação"], FOSF, FOSF_T)]):
    x = 0 if k == 0 else 1004
    p.append(f'<path d="M {x} 80 L {x + 660} 80 L {x + 600} 480 L {x + 60} 480 Z" fill="{f}" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(x, 20, t, w=660, tam=32, cor=c, peso=700, serif=True, alinha="center"))
    for j, it in enumerate(itens):
        rs.append(rot(x + 80, 130 + j * 82, it, w=500, tam=27, cor=TINTA, peso=600, alinha="center"))
p.append(f'<circle cx="832" cy="260" r="120" fill="{TINTA}"/>')
rs.append(rot(722, 196, "o desfecho depende de hormônio sexual?", w=220, tam=24, cor=PAPEL, peso=700, alinha="center", lh=1.2))
diagrama(S, "baldes", 480, p, rs, eyebrow="Decidir com a lacuna", titulo="Uma pergunta diz em que balde a sua dúvida cai",
         destaque="No cruzado, a lógica se inverte: os programas de prevenção foram testados sobretudo em mulheres.", destaque_cor="tinta")

# 8. a ficha de leitura
p = [svg_abre(1664, 480, "Uma ficha de leitura com cinco perguntas e caixas de marcar: havia mulheres, e quantas? o estado hormonal foi caracterizado? a contracepção foi incluída, excluída ou misturada? o desfecho depende de hormônio? a conclusão passou da amostra? Ao lado, um carimbo: extrapolação declarada")]
p.append(caixa(0, 0, 1080, 480, TINTA, CARTAO, esp=2, rx=16))
rs = []
for j, t in enumerate(["Havia mulheres na amostra, e quantas?", "O estado hormonal foi caracterizado, ou só o sexo?", "Contracepção: incluída, excluída ou misturada?",
                       "O desfecho depende de hormônio sexual?", "A conclusão passou da amostra?"]):
    y = 34 + j * 88
    p.append(f'<rect x="34" y="{y}" width="48" height="48" rx="8" fill="{PAPEL}" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(110, y + 6, t, w=940, tam=29, cor=TINTA, peso=600))
p.append(f'<g transform="rotate(-8 1380 220)"><rect x="1150" y="120" width="460" height="200" rx="20" fill="none" stroke="{OXID}" stroke-width="8"/></g>')
rs += [rot(1150, 180, "extrapolação declarada", w=460, tam=36, cor=OXID, peso=700, alinha="center", serif=True, lh=1.2),
       rot(1130, 380, "a extrapolação não é proibida; ela é dita, e acompanhada de perto", w=520, tam=25, cor=TINTA, lh=1.3)]
diagrama(S, "ficha", 480, p, rs, eyebrow="Antes de levar um estudo para ela", titulo="Cinco perguntas, e uma regra para o que sobrar de dúvida")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fisiologia da mulher e o déficit de evidência", "titulo": "Antes do número, pergunte em quem ele foi medido",
          "regras": ["Trocar a régua antes de concluir que ela rende menos",
                     "Desconfiar da extrapolação quando o desfecho depende de hormônio",
                     "Extrapolar dizendo que está extrapolando, e acompanhar"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem prepara e reabilita", "x": "Confere o limiar e a régua antes de ler qualquer relatório."},
                    {"ic": "t:book", "t": "Quem pesquisa e divulga", "x": "Caracteriza o estado hormonal e não estica a conclusão."},
                    {"ic": "t:users", "t": "Toda a equipe", "x": "Pergunta pelo ciclo: o descaso começa na pergunta que ninguém faz."}]})

salvar("11-01.json", {"arquivo": "aulas/MOD11/11-01-fisiologia-da-mulher-e-o-deficit-historico-de-evidencia.md",
                      "titulo": "Fisiologia da mulher e o déficit histórico de evidência", "subtitulo": "O que difere, o que não difere, e como saber",
                      "nota_capa": "Entra por um time feminino que herdou o relatório do masculino.",
                      "secoes": {"regua": ["O erro que parece padronização.", "capa"], "puberdade": ["O que de fato difere.", "puberdade"],
                                 "deficit": ["De onde vem a lacuna.", "deficit"], "baldes": ["Como decidir com ela.", "baldes"]},
                      "slides": S})
