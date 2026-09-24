"""Spec do deck 2.12. Gera 02-12.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def seta(x1, y1, x2, y2, cor, mid, esp=5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mid})"/>'

# 1. músculo contra pele
p = [svg_abre(1664, 400, "O débito cardíaco dividido entre músculo e pele: a 20 graus quase tudo vai para o músculo; a 33 graus com umidade alta, a pele leva uma fatia grande"),
     "<defs>" + seta_marker("g1", TINTA) + "</defs>",
     f'<path d="M150 250 C 60 180, 70 90, 150 120 C 230 90, 240 180, 150 250 Z" fill="{FOSF}"/>',
     seta(260, 170, 360, 170, TINTA, "g1", esp=5)]
for j, (musc, rot_) in enumerate([(0.85, "20 °C"), (0.62, "33 °C, úmido")]):
    y = 60 + j * 170
    wtot = 1200
    p.append(f'<rect x="440" y="{y}" width="{wtot*musc:.0f}" height="100" rx="6" fill="{OXID}"/>')
    p.append(f'<rect x="{440 + wtot*musc + 6:.0f}" y="{y}" width="{wtot*(1-musc) - 6:.0f}" height="100" rx="6" fill="{GLIC}"/>')
p.append("</svg>")
rs = [rot(80, 290, "coração", w=140, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(440, 20, "20 °C", w=400, tam=28, cor=TINTA, peso=700),
      rot(440, 190, "33 °C, umidade alta", w=600, tam=28, cor=TINTA, peso=700),
      rot(470, 92, "músculo", w=400, tam=30, cor=CLARO, peso=700),
      rot(470, 262, "músculo", w=400, tam=30, cor=CLARO, peso=700),
      rot(440 + 1200 * 0.85 + 10, 92, "pele", w=160, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(440 + 1200 * 0.62 + 10, 262, "pele: resfriar", w=440, tam=30, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "pele", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Oito da noite, 33 graus, umidade alta", "titulo": "O ambiente não é cenário. É carga",
          "destaque": "O sangue que vai para a pele é sangue que não vai para o músculo. E o suor ainda vai tirando plasma ao longo da sessão.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos"})

# 2. desvio cardiovascular
t = list(range(0, 61, 3))
fresco = [(m, 150 + 6 * m / 60) for m in t]
calor = [(m, 152 + 26 * (m / 60) ** 0.9) for m in t]
svg, rs = linhas(1664, 400, "Frequência cardíaca ao longo de uma hora no mesmo ritmo: no fresco quase plana, no calor úmido subindo sem parar",
    [{"nome": "", "cor": AZUL, "pts": fresco}, {"nome": "", "cor": FOSF, "pts": calor}], 0, 60, 140, 185,
    [(0, "0 min"), (30, "30"), (60, "60 min")], [], margem=(40, 20, 60, 330))
rs += [rot(1350, 190, "fresco", w=300, tam=30, cor=AZUL, peso=700),
       rot(1350, 20, "calor úmido", w=300, tam=30, cor=FOSF, peso=700),
       rot(40, 0, "frequência cardíaca, mesmo ritmo", w=700, tam=26, cor=MUDO)]
S.append({"id": "desvio", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "A cascata que o atleta sente", "titulo": "Mesmo ritmo, outro custo",
          "destaque": "Percepção de esforço subiu na mesma carga? Olhe o termômetro antes de concluir fadiga, má adaptação ou pouca energia.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · desvio cardiovascular: aula do coração"})

# 3. o instrumento certo
p = [svg_abre(1664, 400, "Temperatura, umidade, sol e vento se combinam num índice de estresse térmico. 30 graus com 85% de umidade é pior que 32 graus com 30%"),
     "<defs>" + seta_marker("h1", TINTA) + "</defs>"]
ent = [("temperatura", FOSF), ("umidade", AZUL), ("sol", GLIC), ("vento", OXID)]
for i, (t_, cor) in enumerate(ent):
    p.append(caixa(0, 10 + i * 96, 300, 76, cor, CARTAO, esp=3, rx=38))
    p.append(f'<path d="M300 {48 + i*96} C 380 {48 + i*96}, 380 200, 450 200" fill="none" stroke="{cor}" stroke-width="4"/>')
p.append(caixa(460, 130, 360, 140, TINTA, TINTA))
for j, (x, nivel, cor) in enumerate([(1000, 0.72, GLIC), (1340, 0.64, FOSF)]):
    p.append(f'<rect x="{x}" y="40" width="70" height="280" rx="35" fill="{CLARO}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="{x+15}" y="{40 + 280*(1-nivel):.0f}" width="40" height="{280*nivel - 15:.0f}" rx="20" fill="{cor}"/>')
    p.append(f'<circle cx="{x+35}" cy="330" r="50" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(0, 32 + i * 96, t_, w=300, tam=28, cor=TINTA, peso=700, alinha="center") for i, (t_, _) in enumerate(ent)]
rs += [rot(470, 160, "índice de bulbo úmido", w=340, tam=30, cor=CLARO, peso=700, alinha="center", serif=True),
       rot(1090, 90, "32 °C", w=220, tam=36, cor=TINTA, peso=700, serif=True),
       rot(1090, 140, "30% de umidade", w=220, tam=26, cor=TINTA),
       rot(1430, 90, "30 °C", w=220, tam=36, cor=TINTA, peso=700, serif=True),
       rot(1430, 140, "85% de umidade", w=230, tam=26, cor=TINTA),
       rot(1430, 220, "pior", w=220, tam=32, cor=FOSF, peso=700)]
S.append({"id": "indice", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A correção de instrumento", "titulo": "O termômetro sozinho não descreve o risco",
          "destaque": "É a evaporação que resfria, não o suor. Suar muito em ar saturado é perder líquido sem ganhar resfriamento.",
          "destaque_cor": "petr"})

# 4. três saídas
p = [svg_abre(1664, 440, "Três saídas: manter, modificar ou adiar. Modificar é, na maioria das vezes, a resposta certa"),
     f'<circle cx="90" cy="215" r="70" fill="{TINTA}"/>']
cores = [OXID, GLIC, FOSF]
for i, cor in enumerate(cores):
    y = 10 + i * 145
    p.append(f'<path d="M160 215 C 330 215, 330 {y+62}, 470 {y+62}" fill="none" stroke="{cor}" stroke-width="{10 if i == 1 else 6}"/>')
    p.append(caixa(480, y, 1184, 125, cor, GLIC_T if i == 1 else CARTAO, esp=6 if i == 1 else 3))
p.append("</svg>")
cards = [("Manter", "índice seguro, aclimatado, sessão curta, água à mão", "o custo aparece depois, como falso destreino"),
         ("Modificar", "horário, menos intensidade, menos duração, pausas, outro ambiente", "a resposta certa na maioria das vezes"),
         ("Adiar", "risco alto, sem aclimatação, febre recente, sono ruim", "adiar sempre impede a aclimatação")]
rs = [rot(20, 196, "33 °C", w=140, tam=28, cor=CLARO, peso=700, alinha="center")]
for i, (t_, q, c) in enumerate(cards):
    y = 10 + i * 145
    rs += [rot(510, y + 40, t_, w=260, tam=34, cor=TINTA, peso=700, serif=True),
           rot(790, y + 18, q, w=860, tam=26, cor=TINTA),
           rot(790, y + 70, c, w=860, tam=26, cor=cores[i] if i != 1 else TINTA, peso=700)]
S.append({"id": "saidas", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A encruzilhada", "titulo": "Manter, modificar, adiar",
          "destaque": "No calor, prescreva por percepção de esforço. O ritmo não sabe que está calor, e a frequência engana.",
          "destaque_cor": "ambar"})

# 5. quanto beber
p = [svg_abre(1664, 420, "Curva em U de risco: beber de menos leva à desidratação, beber muito além da sede leva à hiponatremia; a sede é o guia. Em Boston, 13% terminaram com sódio baixo, com mais chance em quem ganhou peso e em quem levou mais de 4 horas")]
pts = [(x, 330 - 0.0016 * (x - 450) ** 2) for x in range(40, 861, 20)]
p.append(f'<polyline points="{" ".join(f"{x},{y:.0f}" for x, y in pts)}" fill="none" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<line x1="40" y1="360" x2="860" y2="360" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<circle cx="450" cy="330" r="16" fill="{OXID}"/>')
p.append(f'<line x1="940" y1="0" x2="940" y2="420" stroke="{GRADE}" stroke-width="3"/>')
for j, (n, c) in enumerate([("13%", TINTA), ("4,2×", FOSF), ("7,4×", FOSF)]):
    p.append(caixa(990, 40 + j * 120, 674, 100, c, CARTAO, esp=3))
p.append("</svg>")
rs = [rot(40, 0, "risco", w=200, tam=26, cor=MUDO),
      rot(40, 372, "bebe de menos", w=300, tam=26, cor=TINTA, peso=600),
      rot(460, 372, "bebe muito além da sede", w=400, tam=26, cor=TINTA, peso=600, alinha="right"),
      rot(90, 60, "desidratação", w=260, tam=28, cor=AZUL, peso=700),
      rot(550, 60, "hiponatremia", w=260, tam=28, cor=FOSF, peso=700, alinha="right"),
      rot(300, 270, "a sede como guia", w=300, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(990, 0, "Maratona de Boston", w=674, tam=26, cor=TINTA, peso=700)]
for j, (n, x_) in enumerate([("13%", "terminaram com sódio baixo"), ("4,2×", "mais chance em quem ganhou peso na prova"), ("7,4×", "mais chance acima de 4 h que abaixo de 3h30")]):
    rs += [rot(1010, 64 + j * 120, n, w=150, tam=40, cor=FOSF if j else TINTA, peso=700, serif=True),
           rot(1170, 60 + j * 120, x_, w=480, tam=26, cor=TINTA, lh=1.3)]
S.append({"id": "beber", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A decisão dentro da decisão", "titulo": "Dois erros opostos",
          "destaque": "Sede como guia, peso como medida: pese antes e depois, com roupa seca e descontando o que bebeu.",
          "destaque_cor": "petr", "fonte": "Almond e colaboradores, New England Journal of Medicine 2005 · Hew-Butler e colaboradores, consenso de 2015 · curva esquemática"})

# 6. aclimatação
p = [svg_abre(1664, 420, "Duas semanas de exercício no calor: mais plasma, suor mais cedo e mais farto, menos sódio no suor, frequência cardíaca e temperatura menores na mesma carga")]
p.append(f'<line x1="0" y1="380" x2="1664" y2="380" stroke="{MUDO}" stroke-width="3"/>')
for d in range(15):
    x = d * 1664 / 14
    p.append(f'<line x1="{x:.0f}" y1="372" x2="{x:.0f}" y2="388" stroke="{MUDO}" stroke-width="2"/>')
adap = [("mais plasma", AZUL), ("suor mais cedo e mais farto", OXID), ("menos sódio no suor", GLIC), ("FC e temperatura menores na mesma carga", FOSF)]
for i, (t_, cor) in enumerate(adap):
    y = 20 + i * 86
    p.append(f'<rect x="{120 + i*80}" y="{y}" width="{1544 - i*80}" height="64" rx="32" fill="{cor}" fill-opacity="0.18" stroke="{cor}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(140 + i * 80, 34 + i * 86, t_, w=900, tam=28, cor=TINTA, peso=700) for i, (t_, _) in enumerate(adap)]
rs += [rot(0, 388, "dia 1", w=160, tam=24, cor=MUDO), rot(1504, 388, "dia 14", w=160, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "aclimatacao", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A boa notícia", "titulo": "O corpo se adapta ao calor, e rápido",
          "destaque": "Início do verão: 7 a 10 dias de reintrodução. Sauna depois do treino não substitui exercício no calor.",
          "destaque_cor": "ambar", "fonte": "Esquema do tempo aproximado · Racinais e colaboradores, consenso de 2015 · Périard, Racinais e Sawka 2015"})

# 7. emergência
p = [svg_abre(1664, 420, "Doença do calor por esforço: reconhecer pela alteração mental, resfriar primeiro com imersão em água fria, transportar depois. Meta: abaixo de 38,9 graus em até 30 minutos do colapso"),
     "<defs>" + seta_marker("k1", TINTA) + "</defs>"]
passos = [("1 · Reconhecer", "confusão, fala arrastada, marcha cambaleante, colapso. A pele pode estar suada.", AZUL),
          ("2 · Resfriar primeiro", "imersão em água fria; sem ela, água gelada no corpo inteiro e toalhas trocadas", FOSF),
          ("3 · Transportar depois", "emergência acionada em paralelo, não depois", TINTA)]
for i, (t_, x_, cor) in enumerate(passos):
    x = i * 570
    p.append(caixa(x, 0, 520, 260, cor, FOSF_T if i == 1 else CARTAO, esp=6 if i == 1 else 3))
    if i < 2:
        p.append(seta(x + 525, 130, x + 565, 130, TINTA, "k1", esp=5))
p.append(f'<rect x="0" y="300" width="1664" height="110" rx="14" fill="{FOSF}"/>')
p.append("</svg>")
rs = []
for i, (t_, x_, cor) in enumerate(passos):
    rs += [rot(i * 570 + 28, 24, t_, w=470, tam=32, cor=cor, peso=700),
           rot(i * 570 + 28, 90, x_, w=470, tam=26, cor=TINTA, lh=1.35)]
rs.append(rot(40, 326, "Meta: abaixo de 38,9 °C em até 30 minutos do colapso", w=1600, tam=40, cor=CLARO, peso=700, serif=True))
S.append({"id": "emergencia", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Aqui a decisão errada mata", "titulo": "Resfriar primeiro. Transportar depois",
          "fonte": "Casa e colaboradores, posicionamento da NATA, Journal of Athletic Training 2015"})

# 8. altitude
p = [svg_abre(1664, 420, "Viver a 2.500 metros e treinar a 1.250 metros melhorou os 5.000 metros ao nível do mar. O ganho de hemoglobina exige ferro. Quem viaja para uma prova em altitude ajusta o ritmo pelo esforço"),
     f'<polygon points="0,400 260,260 420,300 620,90 820,250 960,400" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>',
     f'<line x1="560" y1="150" x2="700" y2="150" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 6"/>',
     f'<line x1="200" y1="292" x2="360" y2="292" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 6"/>',
     f'<rect x="605" y="118" width="40" height="32" fill="{TINTA}"/>',
     f'<circle cx="280" cy="270" r="18" fill="{OXID}"/>',
     f'<line x1="1020" y1="0" x2="1020" y2="420" stroke="{GRADE}" stroke-width="3"/>']
for j, cor in enumerate([FOSF, GLIC]):
    p.append(caixa(1070, 20 + j * 200, 594, 170, cor, CARTAO, esp=3))
p.append("</svg>")
rs = [rot(700, 110, "viver a 2.500 m", w=300, tam=28, cor=TINTA, peso=700),
      rot(40, 200, "treinar a 1.250 m", w=300, tam=28, cor=OXID, peso=700),
      rot(1094, 40, "Ferro é pré-requisito", w=550, tam=30, cor=FOSF, peso=700),
      rot(1094, 90, "sem estoque, não há hemácia nova; ferritina antes de subir", w=550, tam=26, cor=TINTA),
      rot(1094, 240, "Prova em altitude", w=550, tam=30, cor=GLIC, peso=700),
      rot(1094, 290, "desempenho pior é esperado; ritmo pela percepção de esforço", w=550, tam=26, cor=TINTA)]
S.append({"id": "altitude", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Altitude: onde mora o mito", "titulo": "Viver alto, treinar baixo",
          "destaque": "Dor de cabeça, náusea, tontura, insônia: mal agudo das montanhas. Sintoma neurológico ou respiratório importante: subir mais é sempre errado.",
          "destaque_cor": "verm", "fonte": "Levine e Stray-Gundersen, Journal of Applied Physiology 1997 · 39 corredores · Stellingwerff e colaboradores, Sports Medicine 2019"})

# 9. poluição
x0, x1 = 420, 1600
fx = lambda h: x0 + h / 4 * (x1 - x0)
p = [svg_abre(1664, 360, "Na média urbana mundial de material particulado fino, o benefício da pedalada vence em qualquer volume. Num ar cinco vezes mais poluído, o risco só passa o benefício depois de uma hora e meia de pedalada por dia"),
     f'<rect x="{x0}" y="30" width="{x1-x0}" height="90" rx="6" fill="{OXID}"/>',
     f'<rect x="{x0}" y="170" width="{fx(1.5)-x0:.0f}" height="90" rx="6" fill="{OXID}"/>',
     f'<rect x="{fx(1.5)+4:.0f}" y="170" width="{x1-fx(1.5)-4:.0f}" height="90" rx="6" fill="{FOSF}"/>',
     f'<line x1="{x0}" y1="290" x2="{x1}" y2="290" stroke="{MUDO}" stroke-width="2"/>']
for h in range(5):
    p.append(f'<line x1="{fx(h):.0f}" y1="290" x2="{fx(h):.0f}" y2="302" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(0, 44, "média urbana mundial (22 µg/m³)", w=390, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(0, 184, "ar muito poluído (100 µg/m³)", w=390, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(x0 + 30, 58, "o benefício vence", w=600, tam=28, cor=CLARO, peso=700),
      rot(x0 + 30, 198, "benefício vence", w=300, tam=28, cor=CLARO, peso=700),
      rot(fx(1.5) + 30, 198, "a partir de 1h30 por dia, o risco passa", w=700, tam=28, cor=CLARO, peso=700)]
rs += [rot(fx(h) - 80, 308, f"{h} h", w=160, tam=24, cor=MUDO, alinha="center") for h in range(5)]
rs.append(rot(0, 308, "pedalada por dia", w=390, tam=24, cor=MUDO, alinha="right"))
S.append({"id": "poluicao", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Vale a pena correr na avenida?", "titulo": "Comparado com o quê?",
          "destaque": "Não desencoraje ninguém por causa da poluição. Melhore o balanço: fora do pico, uma quadra longe da avenida, parque quando houver.",
          "destaque_cor": "petr", "fonte": "Tainio e colaboradores, Preventive Medicine 2016 · material particulado fino, modelagem de mortalidade"})

# 10. fecho do módulo
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que fica do módulo", "titulo": "Decisão, contribuição, reconhecimento",
          "regras": ["O ambiente é carga: no calor e na altitude, ritmo pela percepção de esforço",
                     "Doença do calor: resfriar primeiro, transportar depois"],
          "cards": [{"t": "Decisão", "x": "Tem dono, e o dono muda conforme a pergunta: intensidade, laudo, reposição, carga no tecido."},
                    {"t": "Contribuição", "x": "O dado que um vê entrega ao outro a explicação que faltava."},
                    {"t": "Reconhecimento", "x": "Confusão no calor, desmaio no esforço, fadiga de meses, urina escura: é de todos."}],
          "quem": "Doze aulas depois: olhar uma planilha, um laudo, um termômetro ou um relato de cansaço e enxergar qual sistema está pagando a conta."})

spec = {"arquivo": "aulas/MOD02/02-12-calor-hidratacao-e-altitude.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Exercício em ambiente adverso", "subtitulo": "Calor, hidratação e altitude",
        "nota_capa": "Entra pela decisão das oito da noite.",
        "secoes": {"calor": ["O calor como carga e o instrumento certo.", "capa"],
                   "decidir": ["Manter, modificar ou adiar, e quanto beber.", "saidas"],
                   "adaptar": ["Aclimatação, emergência e altitude.", "aclimatacao"],
                   "fechar": ["Poluição e o fecho do módulo.", "poluicao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-12.json"), "w"), ensure_ascii=False, indent=1)
print("02-12.json:", len(S), "slides")
