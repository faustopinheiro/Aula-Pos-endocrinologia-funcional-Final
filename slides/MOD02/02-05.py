"""Spec do deck 2.5. Gera 02-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o comando vem antes
fc = [(t, 70 if t < -8 else (70 + 30 * (1 - math.exp(-(t + 8) / 3)) if t < 0 else 70 + 30 * (1 - math.exp(-8 / 3)) + 70 * (1 - math.exp(-t / 12)))) for t in range(-30, 61)]
svg, rs = linhas(1664, 420, "A frequência cardíaca começa a subir alguns segundos antes do primeiro passo e continua subindo depois que o esforço começa",
    [{"nome": "", "cor": FOSF, "pts": fc}], -30, 60, 50, 180, [(-30, "−30 s"), (0, "primeiro passo"), (30, "30 s"), (60, "60 s")],
    [60, 120, 180], yfmt=lambda v: f"{v:g} bpm", margem=(130, 20, 60, 40), destaques=[{"x": 0}])
rs += [rot(160, 150, "sobe antes: é o comando central", w=420, tam=28, cor=TINTA, peso=700),
       rot(900, 200, "depois entram os receptores do músculo", w=560, tam=26, cor=TINTA, peso=600)]
S.append({"id": "comando", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "Etapa um · a jogadora entra em quadra", "titulo": "O comando vem antes de o músculo pedir",
          "destaque": "A frequência dos primeiros trinta segundos não mede esforço. É antecipação.",
          "fonte": "Esquema, sem valores medidos"})

# 2. o débito multiplica
p = [svg_abre(1664, 360, "Débito cardíaco: 5 litros por minuto em repouso, cerca de 20 no esforço máximo de um destreinado e mais de 35 num atleta de endurance de alto nível"),
     f'<line x1="440" y1="0" x2="440" y2="330" stroke="{MUDO}" stroke-width="2"/>']
esc = 30
for i, (v, cor) in enumerate([(5, MUDO), (20, AZUL), (35, FOSF)]):
    p.append(f'<rect x="442" y="{20 + i*110}" width="{v*esc}" height="80" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(0, 36, "Repouso", w=410, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 146, "Destreinado, no máximo", w=410, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, 256, "Atleta de endurance, no máximo", w=410, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(442 + 5 * esc + 20, 36, "5 L/min", w=300, tam=34, cor=TINTA, peso=700, serif=True),
      rot(442 + 20 * esc + 20, 146, "~20 L/min", w=300, tam=34, cor=TINTA, peso=700, serif=True),
      rot(442 + 35 * esc - 290, 256, "> 35 L/min", w=270, tam=34, cor=CLARO, peso=700, serif=True, alinha="right")]
S.append({"id": "debito", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Etapa dois", "titulo": "O débito cardíaco multiplica até sete vezes",
          "fonte": "Joyner e Coyle, Journal of Physiology 2008"})

# 3. FC e volume de ejeção
def painel(x0, pts, cor, titulo, nota, rs, p):
    w, h, y0 = 760, 280, 60
    p.append(f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
    pl = " ".join(f"{x0 + x/100*w:.1f},{y0 + h - y/100*h:.1f}" for x, y in pts)
    p.append(f'<polyline points="{pl}" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round"/>')
    rs += [rot(x0, 0, titulo, w=w, tam=30, cor=TINTA, peso=700),
           rot(x0, y0 + h + 12, "leve → máximo", w=w, tam=24, cor=MUDO, alinha="right"),
           rot(x0 + 30, y0 + 20, nota, w=440, tam=26, cor=cor, peso=700)]
p = [svg_abre(1664, 380, "À esquerda, a frequência cardíaca subindo quase em linha reta com a intensidade; à direita, o volume de ejeção subindo no começo e estabilizando")]
rs = []
painel(0, [(x, 15 + 0.8 * x) for x in range(0, 101, 5)], FOSF, "Frequência cardíaca", "sobe até o fim", rs, p)
painel(904, [(x, 30 + 55 * (1 - math.exp(-x / 18))) for x in range(0, 101, 2)], AZUL, "Volume de ejeção", "sobe e estabiliza", rs, p)
p.append("</svg>")
rs[-1] = rot(904 + 330, 60 + 190, "sobe e estabiliza", w=400, tam=26, cor=AZUL, peso=700)
S.append({"id": "assimetria", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "De onde vem o aumento", "titulo": "Treinar o coração é treinar volume de ejeção",
          "destaque": "A frequência máxima quase não muda com treino. O quanto sai em cada batida muda.",
          "fonte": "Esquema, sem valores medidos"})

# 4. o sangue muda de endereço
p = [svg_abre(1664, 300, "Fatia do débito que vai para o músculo: 15 a 20% em repouso e mais de 80% no esforço máximo")]
W0, x0 = 1200, 440
for y, frac in [(20, 0.18), (170, 0.82)]:
    p.append(f'<rect x="{x0}" y="{y}" width="{W0*frac-2:.0f}" height="100" rx="4" fill="{FOSF}"/>')
    p.append(f'<rect x="{x0+W0*frac:.0f}" y="{y}" width="{W0*(1-frac):.0f}" height="100" rx="4" fill="{PAUSA}"/>')
p.append("</svg>")
rs = [rot(0, 46, "Repouso", w=410, tam=32, cor=TINTA, peso=700, alinha="right"),
      rot(0, 196, "Esforço máximo", w=410, tam=32, cor=TINTA, peso=700, alinha="right"),
      rot(x0, 44, "15–20%", w=W0 * 0.18, tam=34, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(x0 + W0 * 0.18 + 30, 48, "vísceras, cérebro, pele, coração, resto", w=700, tam=26, cor=TINTA),
      rot(x0, 194, "> 80% para o músculo", w=W0 * 0.82, tam=34, cor=CLARO, peso=700, alinha="center", serif=True)]
S.append({"id": "endereco", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Etapa três", "titulo": "O sangue muda de endereço",
          "destaque": "Vasos se abrem no músculo que trabalha e se fecham nas vísceras: rim, intestino, fígado.",
          "fonte": "Fatias aproximadas, em % do débito cardíaco"})

# 5. três territórios
p = [svg_abre(1664, 420, "O coração no centro com três saídas disputando o mesmo débito: músculo, vísceras e pele"),
     "<defs>" + seta_marker("t1", FOSF) + seta_marker("t2", GLIC) + seta_marker("t3", AZUL) + "</defs>",
     f'<path d="M180 150 C120 60 20 110 40 190 C60 270 180 330 180 360 C180 330 300 270 320 190 C340 110 240 60 180 150 Z" fill="{FOSF}"/>']
for i, (cor, m) in enumerate([(FOSF, "t1"), (GLIC, "t2"), (AZUL, "t3")]):
    y = 40 + i * 135
    p.append(f'<path d="M340 210 C520 210 520 {y+50} 690 {y+50}" fill="none" stroke="{cor}" stroke-width="8" marker-end="url(#{m})"/>')
    p.append(caixa(710, y, 954, 100, cor))
p.append("</svg>")
rs = [rot(40, 380, "um débito só", w=280, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(740, 60, "Músculo: o esforço", w=420, tam=30, cor=TINTA, peso=700),
      rot(1170, 64, "leva a maior fatia", w=470, tam=26),
      rot(740, 195, "Vísceras: o intestino", w=420, tam=30, cor=TINTA, peso=700),
      rot(1170, 186, "horas com pouco sangue: desconforto na prova longa", w=470, tam=26),
      rot(740, 330, "Pele: o calor", w=420, tam=30, cor=TINTA, peso=700),
      rot(1170, 322, "entra na disputa quando é preciso jogar calor fora", w=470, tam=26)]
S.append({"id": "territorios", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Duas consequências de toda semana", "titulo": "Três territórios disputam o mesmo débito"})

# 6. a pressão assimétrica
sis = [(x, 120 + 80 * x / 100) for x in range(0, 101, 5)]
dia = [(x, 80 - 6 * x / 100) for x in range(0, 101, 5)]
dia_ruim = [(x, 80 + 30 * (x / 100) ** 1.3) for x in range(0, 101, 5)]
svg, rs = linhas(1664, 420, "No exercício dinâmico a pressão sistólica sobe de 120 para perto de 200 e a diastólica fica perto de 80 ou cai um pouco; uma diastólica que sobe durante o teste é achado que pede atenção",
    [{"nome": "", "cor": FOSF, "pts": sis}, {"nome": "", "cor": AZUL, "pts": dia},
     {"nome": "", "cor": MUDO, "pts": dia_ruim, "tracejado": True, "esp": 4}],
    0, 100, 40, 220, [(0, "repouso"), (100, "esforço máximo")], [80, 120, 160, 200], yfmt=lambda v: f"{v:g}",
    margem=(90, 20, 60, 30))
rs += [rot(1150, 110, "sistólica sobe", w=400, tam=28, cor=FOSF, peso=700),
       rot(1100, 305, "diastólica estável ou cai", w=460, tam=28, cor=AZUL, peso=700),
       rot(1040, 170, "diastólica subindo: pede atenção médica", w=560, tam=26, cor=MUDO, peso=700)]
S.append({"id": "pressao", "tipo": "diagrama", "h": 420, "svg": svg, "rotulos": rs,
          "eyebrow": "Etapa quatro · exercício dinâmico", "titulo": "Sistólica sobe, diastólica fica",
          "fonte": "mmHg · esquema, sem valores medidos"})

# 7. a equação
p = [svg_abre(1664, 400, "Consumo de oxigênio igual a débito cardíaco vezes diferença arteriovenosa de oxigênio; o primeiro termo é circular mais e decide o teto, o segundo é extrair mais e pesa no limiar"),
     caixa(420, 150, 520, 120, FOSF, FOSF_T), caixa(1080, 150, 584, 120, OXID, OXID_T), "</svg>"]
rs = [rot(0, 172, "VO₂  =", w=390, tam=72, cor=TINTA, peso=700, serif=True, alinha="right"),
      rot(420, 180, "débito cardíaco", w=520, tam=40, cor=TINTA, peso=700, alinha="center"),
      rot(940, 172, "×", w=140, tam=72, cor=TINTA, peso=700, serif=True, alinha="center"),
      rot(1080, 164, "diferença arteriovenosa<br>de oxigênio", w=584, tam=34, cor=TINTA, peso=700, alinha="center"),
      rot(420, 20, "circular mais", w=520, tam=34, cor=FOSF, peso=700, alinha="center"),
      rot(1080, 20, "extrair mais", w=584, tam=34, cor=OXID, peso=700, alinha="center"),
      rot(420, 300, "a entrega decide o teto do VO₂máx", w=520, tam=26, alinha="center"),
      rot(1080, 300, "a periferia pesa na intensidade que se sustenta: o limiar", w=584, tam=26, alinha="center")]
S.append({"id": "equacao", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Etapa cinco", "titulo": "A conta fecha numa equação só",
          "destaque": "Em pessoa saudável, ao nível do mar, o que limita o VO₂máx é a entrega. Não é a mitocôndria esperando trabalho.",
          "destaque_cor": "tinta"})

# 8. a deriva
p = [svg_abre(1664, 380, "Três horas em ritmo constante no calor: a frequência cardíaca sobe devagar e o volume de ejeção cai")]
rs = []
def painel2(x0, pts, cor, titulo, nota):
    w, h, y0 = 760, 260, 60
    p.append(f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{MUDO}" stroke-width="2"/>')
    pl = " ".join(f"{x0 + x/180*w:.1f},{y0 + h - y/100*h:.1f}" for x, y in pts)
    p.append(f'<polyline points="{pl}" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round"/>')
    rs.extend([rot(x0, 0, titulo, w=w, tam=30, cor=TINTA, peso=700),
               rot(x0, y0 + h + 12, "0 → 3 horas, ritmo constante", w=w, tam=24, cor=MUDO, alinha="right"),
               rot(x0 + 20, y0 + h - 70, nota, w=500, tam=26, cor=cor, peso=700)])
painel2(0, [(t, 45 + 35 * (1 - math.exp(-t / 90))) for t in range(0, 181, 5)], FOSF, "Frequência cardíaca", "sobe sozinha")
painel2(904, [(t, 80 - 30 * (1 - math.exp(-t / 90))) for t in range(0, 181, 5)], AZUL, "Volume de ejeção", "cai")
p.append("</svg>")
S.append({"id": "deriva", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Etapa seis · a sessão longa, no calor", "titulo": "A zona de frequência perde validade",
          "destaque": "Quem estourou a zona na terceira hora pode não ter acelerado nada. Desidratou e esquentou.", "destaque_cor": "ambar",
          "fonte": "Esquema · Coyle e González-Alonso, Exercise and Sport Sciences Reviews 2001"})

# 9. carga alta
p = [svg_abre(1664, 420, "Pressão arterial: referência de repouso 120 por 80; média no leg press pesado 320 por 250; maior valor medido acima de 480 por 350"),
     f'<line x1="0" y1="380" x2="1664" y2="380" stroke="{MUDO}" stroke-width="2"/>']
esc = 0.72
grupos = [(120, 80, "Repouso<br>(referência)"), (320, 250, "Leg press pesado<br>média"), (480, 350, "Leg press pesado<br>maior valor")]
rs = []
for i, (s_, d_, nome) in enumerate(grupos):
    x = 140 + i * 520
    p.append(f'<rect x="{x}" y="{380 - s_*esc:.0f}" width="140" height="{s_*esc:.0f}" rx="4" fill="{FOSF}"/>')
    p.append(f'<rect x="{x+150}" y="{380 - d_*esc:.0f}" width="140" height="{d_*esc:.0f}" rx="4" fill="{AZUL}"/>')
    rs += [rot(x, 380 - s_ * esc - 44, f"{s_}", w=140, tam=32, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(x + 150, 380 - d_ * esc - 44, f"{d_}", w=140, tam=32, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(x + 300, 300, nome, w=210, tam=24, cor=TINTA, peso=600)]
p.append(f'<rect x="0" y="10" width="28" height="28" rx="4" fill="{FOSF}"/><rect x="0" y="54" width="28" height="28" rx="4" fill="{AZUL}"/></svg>')
rs += [rot(40, 6, "sistólica", w=300, tam=26, cor=TINTA, peso=600), rot(40, 50, "diastólica", w=300, tam=26, cor=TINTA, peso=600)]
S.append({"id": "cargaalta", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Troca o cenário: leg press pesado", "titulo": "Medido com cateter dentro da artéria",
          "destaque": "Picos de segundos, bem tolerados pelo corpo saudável. Não é argumento contra o treino de força.",
          "fonte": "mmHg · MacDougall e colaboradores, Journal of Applied Physiology 1985 · fisiculturistas experientes"})

# 10. quem precisa de técnica
S.append({"id": "tecnica", "tipo": "cards", "por_linha": 4,
          "eyebrow": "O que esses números decidem", "titulo": "Para quem a respiração vira conduta",
          "cards": [{"t": "Pressão descontrolada", "cor": "verm"}, {"t": "Aneurisma conhecido", "cor": "verm"},
                    {"t": "Retinopatia proliferativa", "cor": "verm"}, {"t": "Cirurgia recente", "x": "de certos territórios", "cor": "verm"}],
          "destaque": "Não prender a respiração, soltar o ar na fase de esforço, evitar a falha com carga máxima. E a pergunta que custa cinco segundos: “você prende a respiração quando levanta peso?”",
          "destaque_cor": "ambar"})

# 11. hipotensão pós-exercício
pa = [(t, 0 if t < 0 else -6 * (1 - math.exp(-t / 0.4)) * math.exp(-t / 8)) for t in [x / 4 for x in range(-4, 49)]]
def faixa0(fx, fy):
    return f'<rect x="{fx(-1):.1f}" y="{fy(1):.1f}" width="{fx(0)-fx(-1):.1f}" height="{fy(-8)-fy(1):.1f}" fill="{PAUSA}" fill-opacity="0.5"/>'
svg, rs = linhas(1664, 400, "Nas horas depois de uma sessão, a pressão fica abaixo da linha de repouso e volta devagar",
    [{"nome": "", "cor": AZUL, "pts": pa}], -1, 12, -8, 1, [(0, "fim da sessão"), (4, "4 h"), (8, "8 h"), (12, "12 h")], [0, -4, -8],
    yfmt=lambda v: f"{v:+g}".replace("+0", "0"), margem=(90, 20, 60, 520), extra=faixa0)
svg = svg.replace("</svg>", f'<line x1="1180" y1="0" x2="1180" y2="400" stroke="{GRADE}" stroke-width="2"/></svg>')
rs += [rot(1220, 20, "−6/−4", w=440, tam=64, cor=AZUL, peso=700, serif=True),
       rot(1220, 104, "mmHg, em média, depois de uma sessão aeróbica", w=440, tam=26),
       rot(1220, 200, "−3/−3", w=440, tam=64, cor=AZUL, peso=700, serif=True),
       rot(1220, 284, "depois de uma sessão de força", w=440, tam=26),
       rot(1220, 336, "queda maior em quem tem pressão alta", w=440, tam=24, cor=TINTA, peso=600)]
S.append({"id": "hipotensao", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "O efeito agudo mais útil da aula", "titulo": "Depois da sessão, a pressão fica mais baixa por horas",
          "fonte": "Carpio-Rivera e colaboradores, Arquivos Brasileiros de Cardiologia 2016 · 65 estudos · curva ilustrativa"})

# 12. frequência ganha de heroísmo
p = [svg_abre(1664, 360, "Uma semana em faixa de horas: cinco sessões moderadas cobrem boa parte dos dias com pressão mais baixa; duas sessões muito longas cobrem só dois dias")]
x0, W = 300, 1340
for k, (dias, y) in enumerate([([0, 1, 2, 3, 4], 60), ([1, 5], 210)]):
    p.append(f'<rect x="{x0}" y="{y}" width="{W}" height="70" rx="6" fill="{PAUSA}" fill-opacity="0.45"/>')
    for d in dias:
        xs = x0 + (d + 7 / 24) * W / 7
        p.append(f'<rect x="{xs:.0f}" y="{y}" width="{W/7*0.5:.0f}" height="70" rx="4" fill="{AZUL}"/>')
        p.append(f'<rect x="{xs:.0f}" y="{y}" width="10" height="70" rx="2" fill="{TINTA}"/>')
for d in range(8):
    p.append(f'<line x1="{x0 + d*W/7:.0f}" y1="40" x2="{x0 + d*W/7:.0f}" y2="300" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(0, 68, "5 sessões<br>moderadas", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 218, "2 sessões<br>heroicas", w=270, tam=28, cor=TINTA, peso=700, alinha="right")]
for d, nome in enumerate(["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]):
    rs.append(rot(x0 + d * W / 7, 0, nome, w=W / 7, tam=24, cor=MUDO, alinha="center"))
rs.append(rot(x0, 310, "azul: horas com a pressão mais baixa depois de cada sessão · esquema", w=W, tam=24, cor=MUDO))
S.append({"id": "semana", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Se o efeito dura horas, e não dias", "titulo": "Frequência ganha de heroísmo",
          "destaque": "O controle da pressão depende da frequência das sessões, não da intensidade delas."})

# 13. a ordem das adaptações
p = [svg_abre(1664, 400, "Linha do tempo de dois anos: o volume plasmático começa em dias, a frequência de repouso cai em semanas, o coração remodela em meses a anos e a massa de hemoglobina aumenta por último")]
def tx(meses):
    return 380 + math.log10(1 + meses * 4) / math.log10(1 + 24 * 4) * 1270
faixas = [("Volume de plasma", 0.1, OXID), ("Frequência de repouso cai", 1, AZUL), ("Coração remodela", 4, GLIC), ("Massa de hemoglobina", 10, FOSF)]
rs = []
for i, (nome, ini, cor) in enumerate(faixas):
    y = 20 + i * 80
    p.append(f'<rect x="{tx(ini):.0f}" y="{y}" width="{tx(24)-tx(ini):.0f}" height="56" rx="8" fill="{cor}" fill-opacity="0.85"/>')
    rs.append(rot(0, y + 10, nome, w=360, tam=28, cor=TINTA, peso=700, alinha="right"))
p.append(f'<line x1="380" y1="345" x2="1650" y2="345" stroke="{MUDO}" stroke-width="2"/>')
for m, t in [(0.1, "dias"), (1, "1 mês"), (4, "4 meses"), (12, "1 ano"), (24, "2 anos")]:
    p.append(f'<line x1="{tx(m):.0f}" y1="345" x2="{tx(m):.0f}" y2="355" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(tx(m) - 80, 360, t, w=160, tam=24, cor=MUDO, alinha="center"))
p.append("</svg>")
S.append({"id": "ordem", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Do agudo para o crônico", "titulo": "Líquido, ritmo, estrutura, transporte",
          "destaque": "Quem promete adaptação cardiovascular em quatro semanas está prometendo a parte líquida. Real, boa, e a primeira a ir embora.",
          "fonte": "Esquema de ordem temporal, escala logarítmica"})

# 14. dois corações
p = [svg_abre(1664, 380, "Dois corações em corte: o de endurance com cavidade maior e parede proporcional; o de força com parede mais espessa e cavidade pouco alterada")]
for cx, (rx, ry, esp), cor in [(420, (190, 150, 34), OXID), (1244, (170, 135, 62), FOSF)]:
    p.append(f'<ellipse cx="{cx}" cy="190" rx="{rx}" ry="{ry}" fill="{cor}"/>')
    p.append(f'<ellipse cx="{cx}" cy="190" rx="{rx-esp}" ry="{ry-esp}" fill="{CLARO}"/>')
p.append("</svg>")
rs = [rot(0, 0, "Endurance: sobrecarga de volume", w=840, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(824, 0, "Força: sobrecarga de pressão", w=840, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(270, 170, "cavidade maior", w=300, tam=28, cor=OXID, peso=700, alinha="center"),
      rot(1094, 170, "parede mais<br>espessa", w=300, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(0, 350, "Na vida real quase ninguém faz só um dos dois: o que se vê é mistura.", w=1664, tam=26, cor=MUDO, alinha="center")]
S.append({"id": "coracoes", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Meses a anos", "titulo": "O coração remodela conforme a carga que recebeu",
          "fonte": "Esquema, sem escala"})

# 15. pseudoanemia
p = [svg_abre(1664, 460, "Dois tubos de sangue: depois do treino o plasma aumenta bastante e as hemácias um pouco; a concentração de hemoglobina cai")]
for i, (plasma, hem) in enumerate([(160, 140), (240, 150)]):
    x = 260 + i * 460
    top = 400 - plasma - hem
    p.append(f'<rect x="{x}" y="{top}" width="160" height="{plasma+hem}" rx="20" fill="none" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="{x+6}" y="{top+6}" width="148" height="{plasma-6}" rx="14" fill="{GLIC_T}"/>')
    p.append(f'<rect x="{x+6}" y="{400-hem}" width="148" height="{hem-6}" rx="14" fill="{FOSF}"/>')
p.append(f'<line x1="1180" y1="0" x2="1180" y2="460" stroke="{GRADE}" stroke-width="2"/></svg>')
rs = [rot(200, 412, "Antes", w=280, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(620, 412, "Depois de semanas de treino", w=360, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(430, 150, "plasma", w=200, tam=26, cor=GLIC, peso=700),
      rot(430, 320, "hemácias", w=200, tam=26, cor=FOSF, peso=700),
      rot(1220, 40, "Mais hemoglobina total, diluída em mais plasma.", w=440, tam=30, cor=TINTA, peso=700),
      rot(1220, 180, "O laudo mostra a concentração. A concentração cai.", w=440, tam=26),
      rot(1220, 290, "Diluição, não carência.", w=440, tam=30, cor=FOSF, peso=700, serif=True)]
S.append({"id": "pseudoanemia", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A adaptação que engana o laboratório", "titulo": "Pseudoanemia do atleta",
          "fonte": "Esquema · Mairbäurl, Frontiers in Physiology 2013"})

# 16. procedimento de leitura
S.append({"id": "leitura", "tipo": "lista", "eyebrow": "Hemoglobina baixa: o procedimento", "titulo": "Ler sem errar nos dois sentidos",
          "itens": [{"t": "Olhar a companhia, não o número sozinho", "x": "Índices, ferritina com proteína C reativa, volume de treino."},
                    {"t": "Registrar a condição de coleta", "x": "Hora, tempo desde a última sessão, hidratação, fase do ciclo. Férias e carga alta dão números diferentes."},
                    {"t": "Lembrar dos três cenários", "x": "Diluição. Falta de ferro. E as duas juntas, que é comum.", "cor": "verm"}],
          "destaque": "Tratar tudo com ferro e chamar tudo de pseudoanemia é o mesmo erro com o sinal trocado. Interpretar e repor é conduta médica."})

# 17. a ficha
p = [svg_abre(1664, 420, "Uma ficha com três instrumentos e datas: frequência de repouso, frequência em carga submáxima padronizada e recuperação da frequência no primeiro minuto"),
     caixa(0, 0, 1664, 420, BORDA, CARTAO, 2, 16)]
for i in range(4):
    p.append(f'<line x1="0" y1="{80 + i*85}" x2="1664" y2="{80 + i*85}" stroke="{GRADE}" stroke-width="2"/>')
for x in (620, 880, 1140, 1400):
    p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="335" stroke="{GRADE}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(30, 24, "Instrumento", w=560, tam=26, cor=MUDO, peso=700)]
for j, d in enumerate(["data", "data", "data", "data"]):
    rs.append(rot(620 + j * 260, 24, d, w=260, tam=24, cor=MUDO, alinha="center"))
for i, (t, s) in enumerate([("FC de repouso", "mesma condição, mesmo horário"), ("FC em carga padronizada", "mesma carga, mesma duração"), ("Recuperação no 1º minuto", "depois do esforço padronizado")]):
    rs += [rot(30, 92 + i * 85, t, w=560, tam=28, cor=TINTA, peso=700), rot(30, 128 + i * 85, s, w=560, tam=24)]
rs.append(rot(30, 356, "Fora do laboratório não se acompanha volume de ejeção, débito nem volume de plasma.", w=1600, tam=26, cor=FOSF, peso=600))
S.append({"id": "ficha", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que usar na segunda-feira", "titulo": "Tendência, nunca ponto isolado",
          "fonte": "Buchheit, Frontiers in Physiology 2014"})

# 18. master
sed = [(a, 42 - 0.40 * (a - 20)) for a in range(20, 81, 2)]
tre = [(a, 58 - 0.45 * (a - 20)) for a in range(20, 81, 2)]
svg, rs = linhas(1664, 400, "A capacidade aeróbica cai com a idade no sedentário e no treinado; a curva do treinado fica bem acima, e o treinado de 60 anos aparece acima do sedentário de 40",
    [{"nome": "", "cor": OXID, "pts": tre, "marcas": [(60, 58 - 0.45 * 40)]}, {"nome": "", "cor": MUDO, "pts": sed, "marcas": [(40, 42 - 0.40 * 20)]}],
    20, 80, 0, 65, [(20, "20 anos"), (40, "40"), (60, "60"), (80, "80")], [], margem=(40, 20, 60, 40))
rs += [rot(1400, 100, "treinado", w=260, tam=30, cor=OXID, peso=700),
       rot(1400, 250, "sedentário", w=300, tam=30, cor=MUDO, peso=700),
       rot(960, 70, "treinado de 60 acima do sedentário de 40", w=560, tam=26, cor=TINTA, peso=700)]
S.append({"id": "master", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "Expectativa com o atleta master", "titulo": "O treino não impede a queda. Desloca a curva.",
          "destaque": "O objetivo não é o número de vinte anos atrás. É ficar o mais alto possível na curva que a idade permite.",
          "fonte": "Esquema, sem valores medidos"})

# 19. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "O que interrompe e encaminha",
          "regras": ["Desmaio ou quase desmaio durante o esforço", "Dor no peito ao esforço", "Falta de ar desproporcional ao treino",
                     "Palpitação com sensação de desmaio", "Morte súbita precoce na família"],
          "cards": [{"t": "Encaminhar direito", "x": "Com prazo dito e orientação para o intervalo."},
                    {"t": "A frase mais perigosa", "x": "“É coração de atleta”, dita por quem não avaliou."}],
          "quem": "Fisiologia e doença se sobrepõem. Quem decide é a avaliação."})

spec = {"arquivo": "aulas/MOD02/02-05-respostas-cardiovasculares-agudas-e-cronicas.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "O coração em ordem", "subtitulo": "Respostas cardiovasculares agudas e crônicas",
        "nota_capa": "Entra pela jogadora de handebol.",
        "secoes": {"agudo": ["A resposta aguda em seis etapas.", "capa"],
                   "forca": ["Carga alta e a hipotensão depois do exercício.", "cargaalta"],
                   "cronico": ["A ordem das adaptações e a hemoglobina que engana.", "ordem"],
                   "segunda": ["O que medir, o master e o que encaminha.", "ficha"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-05.json"), "w"), ensure_ascii=False, indent=1)
print("02-05.json:", len(S), "slides")
