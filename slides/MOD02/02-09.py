"""Spec do deck 2.9. Gera 02-09.json ao lado deste arquivo."""
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

# 1. a pergunta
S.append({"id": "pergunta", "tipo": "frase", "fundo": "tinta", "eyebrow": "A pergunta que chega pronta",
          "frase": "“Se eu fizer musculação, vai atrapalhar a minha corrida?”",
          "apoio": "E a versão espelhada: “se eu correr, vou perder músculo?” Quase todo mundo que você atende faz, ou deveria fazer, as duas coisas."})

# 2. Hickson
sem = [x / 2 for x in range(0, 21)]
forca = lambda w: 46 * (w / 10) ** 0.9
so_f = [(w, forca(w)) for w in sem]
def conc(w):
    if w <= 7: return forca(w)
    if w <= 8: return forca(7) + 1.5 * (w - 7)
    return forca(7) + 1.5 - 5 * (w - 8)
se = [(w, conc(w)) for w in sem]
so_e = [(w, 2.5 * (w / 10)) for w in sem]
svg, rs = linhas(1664, 400, "Esquema das dez semanas: o grupo só de força ganha força o tempo todo; o grupo que somou força e endurance acompanha até a sétima semana, estabiliza e perde força nas duas últimas; o grupo só de endurance quase não ganha força",
    [{"nome": "", "cor": FOSF, "pts": so_f}, {"nome": "", "cor": AZUL, "pts": se, "tracejado": True}, {"nome": "", "cor": OXID, "pts": so_e}],
    0, 10, 0, 50, [(0, "semana 0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")], [], margem=(40, 20, 60, 330))
rs += [rot(1350, 10, "só força", w=300, tam=30, cor=FOSF, peso=700),
       rot(1350, 110, "força + endurance", w=300, tam=30, cor=AZUL, peso=700),
       rot(1350, 300, "só endurance", w=300, tam=30, cor=OXID, peso=700)]
S.append({"id": "hickson", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "1980: dez semanas, três grupos, força de perna", "titulo": "O achado que criou o medo",
          "destaque": "O VO₂máx subiu igual nos dois grupos de endurance. E repara no volume: o grupo concorrente fazia seis dias de endurance mais cinco de força.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos · Hickson, European Journal of Applied Physiology 1980"})

# 3. duas camadas
p = [svg_abre(1664, 400, "Camada molecular: tensão mecânica manda construir, a AMPK manda economizar. Camada prática: o glicogênio que estava cheio às sete da manhã está baixo às sete da noite, e a sessão de força sai pior"),
     "<defs>" + seta_marker("a1", FOSF) + seta_marker("a2", OXID) + "</defs>",
     caixa(0, 70, 300, 110, FOSF, FOSF_T), seta(310, 125, 440, 125, FOSF, "a1"),
     f'<rect x="460" y="70" width="300" height="110" rx="14" fill="{FOSF}"/>',
     caixa(0, 240, 300, 110, OXID, OXID_T), seta(310, 295, 440, 295, OXID, "a2"),
     f'<rect x="460" y="240" width="300" height="110" rx="14" fill="{OXID}"/>',
     f'<line x1="850" y1="0" x2="850" y2="400" stroke="{GRADE}" stroke-width="3"/>']
for x, nivel in [(960, 0.9), (1240, 0.3)]:
    p.append(f'<rect x="{x}" y="{70 + 260*(1-nivel):.0f}" width="120" height="{260*nivel:.0f}" rx="6" fill="{GLIC}"/>')
    p.append(f'<rect x="{x}" y="70" width="120" height="260" rx="10" fill="none" stroke="{TINTA}" stroke-width="4"/>')
p.append(seta(1095, 200, 1225, 200, TINTA, "a3", esp=4))
p.insert(1, "<defs>" + seta_marker("a3", TINTA) + "</defs>")
p.append("</svg>")
rs = [rot(0, 0, "Camada molecular", w=760, tam=30, cor=TINTA, peso=700),
      rot(10, 88, "Tensão mecânica", w=280, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(470, 104, "“construa”", w=280, tam=34, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(10, 258, "Queda de energia: AMPK", w=280, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(470, 274, "“economize”", w=280, tam=34, cor=CLARO, peso=700, alinha="center", serif=True),
      rot(900, 0, "Camada prática", w=760, tam=30, cor=TINTA, peso=700),
      rot(900, 340, "7h, antes dos 12 km", w=240, tam=24, cor=MUDO, alinha="center"),
      rot(1180, 340, "19h, na academia", w=240, tam=24, cor=MUDO, alinha="center"),
      rot(1380, 150, "glicogênio baixo, fadiga, sessão de força pior", w=284, tam=26, cor=TINTA, peso=600)]
S.append({"id": "camadas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por que atrapalharia", "titulo": "Duas camadas de explicação",
          "destaque": "A leitura “a AMPK desliga a construção” envelheceu: a sinalização depende de tempo, dose e comida. Não é interruptor.",
          "destaque_cor": "tinta", "fonte": "Coffey e Hawley, Journal of Physiology 2017 · tanques ilustrativos"})

# 4. fadiga, não sinalização
S.append({"id": "fadiga", "tipo": "frase", "fundo": "verm", "eyebrow": "A distinção que decide a conduta",
          "frase": "A maior parte da interferência no atleta real é fadiga, não sinalização.",
          "apoio": "E fadiga tem solução de agenda. Sinalização, muito menos."})

# 5. Wilson 2012
p = [svg_abre(1664, 330, "Tamanho de efeito para ganho de potência: só força 0,91; treino concorrente 0,55; só endurance 0,11"),
     f'<line x1="420" y1="0" x2="420" y2="320" stroke="{MUDO}" stroke-width="2"/>']
esc = 1250
barras = [("Só força", 0.91, FOSF), ("Concorrente", 0.55, AZUL), ("Só endurance", 0.11, OXID)]
for i, (t, v, cor) in enumerate(barras):
    p.append(f'<rect x="422" y="{20 + i*105}" width="{v*esc:.0f}" height="80" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = []
for i, (t, v, cor) in enumerate(barras):
    rs.append(rot(0, 38 + i * 105, t, w=390, tam=30, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(422 + v * esc + 20, 34 + i * 105, f"{v:.2f}".replace(".", ","), w=200, tam=40, cor=TINTA, peso=700, serif=True))
S.append({"id": "wilson", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "2012: 21 estudos, ganho de potência", "titulo": "O concorrente ficou no meio do caminho",
          "destaque": "O que mais pesou foi o endurance escolhido: modalidade, frequência e duração. Correr junto reduziu hipertrofia e força. Pedalar, não.",
          "destaque_cor": "ambar", "fonte": "Wilson e colaboradores, Journal of Strength and Conditioning Research 2012 · tamanho de efeito"})

# 6. Schumann 2022
p = [svg_abre(1664, 360, "Quatro desfechos: hipertrofia preservada, força máxima preservada, força explosiva atenuada sobretudo na mesma sessão, capacidade aeróbica preservada"),
     "<defs>" + seta_marker("b1", FOSF) + "</defs>"]
tiles = [("Hipertrofia", "preservada", OXID, OXID_T, False), ("Força máxima", "preservada", OXID, OXID_T, False),
         ("Força explosiva", "atenuada, sobretudo na mesma sessão", FOSF, FOSF_T, True), ("Capacidade aeróbica", "preservada", OXID, OXID_T, False)]
rs = []
for i, (t, s_, cor, fundo, cai) in enumerate(tiles):
    x = i * 424
    p.append(caixa(x, 0, 392, 350, cor, fundo, esp=5 if cai else 3))
    cx = x + 196
    if cai:
        p.append(f'<line x1="{cx}" y1="100" x2="{cx}" y2="190" stroke="{FOSF}" stroke-width="12" marker-end="url(#b1)"/>')
    else:
        p.append(f'<path d="M{cx-60} 130 h120 M{cx-60} 165 h120" stroke="{OXID}" stroke-width="12" stroke-linecap="round"/>')
    rs.append(rot(x + 16, 26, t, w=360, tam=30, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x + 16, 250, s_, w=360, tam=28, cor=cor, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "schumann", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "2022: a evidência se corrigindo", "titulo": "A interferência é assimétrica",
          "destaque": "“Vou perder músculo se correr?” Não. “Vou perder explosão?” Pode ser, dependendo de como você organiza.",
          "destaque_cor": "tinta", "fonte": "Schumann e colaboradores, Sports Medicine 2022 · 43 estudos"})

# 7. Petré 2021
p = [svg_abre(1664, 420, "A interferência na força de perna apareceu só em treinados em força, e só quando força e endurance ficavam a menos de 20 minutos uma da outra; com mais de 2 horas, não apareceu")]
for i, (cor, op) in enumerate([(MUDO, 0.45), (MUDO, 0.45), (FOSF, 1)]):
    cx = 90 + i * 240
    p.append(f'<circle cx="{cx}" cy="60" r="40" fill="{cor}" fill-opacity="{op}"/>')
    p.append(f'<rect x="{cx-55}" y="110" width="110" height="150" rx="40" fill="{cor}" fill-opacity="{op}"/>')
p.append(f'<line x1="740" y1="0" x2="740" y2="420" stroke="{GRADE}" stroke-width="3"/>')
for j, (gap, cor) in enumerate([(30, FOSF), (330, OXID)]):
    y = 90 + j * 170
    p.append(f'<rect x="800" y="{y}" width="220" height="70" rx="8" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<rect x="{1020+gap}" y="{y}" width="220" height="70" rx="8" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(0, 280, "destreinado", w=180, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(215, 280, "moderadamente treinado", w=230, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(465, 280, "treinado em força", w=210, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(0, 370, "sem interferência", w=410, tam=26, cor=MUDO, alinha="center"),
      rot(440, 370, "com interferência", w=260, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(800, 0, "E mesmo nos treinados:", w=860, tam=30, cor=TINTA, peso=700),
      rot(800, 106, "força", w=220, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(1050, 106, "endurance", w=220, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(1300, 96, "menos de 20 min: aparece", w=364, tam=26, cor=FOSF, peso=700),
      rot(800, 276, "força", w=220, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(1350, 276, "endurance", w=220, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(1040, 196, "mais de 2 horas: não aparece", w=560, tam=26, cor=OXID, peso=700, alinha="center")]
S.append({"id": "treinados", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Para quem ela aparece: força de perna", "titulo": "A interferência mora num lugar específico",
          "fonte": "Petré e colaboradores, Sports Medicine 2021 · força dinâmica máxima de membros inferiores"})

# 8. modalidade
p = [svg_abre(1664, 380, "Corrida: impactos repetidos e fase excêntrica, mais dano muscular. Bicicleta: movimento circular, concêntrico, sem impacto")]
pts, x = [], 40
while x < 700:
    pts += [f"{x},300", f"{x+30},300", f"{x+50},120", f"{x+70},300"]
    x += 110
p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{FOSF}" stroke-width="6" stroke-linejoin="round"/>')
p.append(f'<line x1="20" y1="300" x2="720" y2="300" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<line x1="840" y1="0" x2="840" y2="380" stroke="{GRADE}" stroke-width="3"/>')
p.append(f'<circle cx="1110" cy="200" r="110" fill="none" stroke="{OXID}" stroke-width="6"/>')
p.append(f'<circle cx="1110" cy="200" r="16" fill="{OXID}"/>')
p.append(f'<line x1="1110" y1="200" x2="1188" y2="122" stroke="{OXID}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<line x1="1110" y1="200" x2="1032" y2="278" stroke="{OXID}" stroke-width="8" stroke-linecap="round"/>')
p.append("</svg>")
rs = [rot(0, 0, "Corrida", w=720, tam=32, cor=FOSF, peso=700),
      rot(0, 320, "impacto e fase excêntrica: mais dano muscular", w=740, tam=26, cor=TINTA),
      rot(900, 0, "Bicicleta", w=720, tam=32, cor=OXID, peso=700),
      rot(1260, 140, "concêntrica, sem impacto: menor custo mecânico", w=400, tam=26, cor=TINTA)]
S.append({"id": "modalidade", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A modalidade importa", "titulo": "Correr custa mais ao músculo que pedalar",
          "destaque": "Prioridade em força: o aeróbico mais barato é a bicicleta. Se a corrida é o objetivo, não há troca a fazer, e a solução vem da semana.",
          "destaque_cor": "petr", "fonte": "Wilson 2012 · Lundberg e colaboradores, Sports Medicine 2022: efeito na fibra maior com corrida, evidência preliminar"})

# 9. nota de rodapé
S.append({"id": "rodape", "tipo": "frase", "fundo": "petr", "eyebrow": "O atleta real deste curso",
          "frase": "Para quem quer ser saudável e funcional, a interferência é nota de rodapé.",
          "apoio": "Quem corre 30 km por semana e faz duas sessões de força não está no cenário relevante. O medo da interferência afasta gente do treino de força, que é o que mais falta."})

# 10. três saídas
p = [svg_abre(1664, 420, "Três saídas a partir da mesma semana: A, mesma sessão; B, dias diferentes; C, blocos com ênfase rotativa"),
     f'<circle cx="90" cy="210" r="70" fill="{TINTA}"/>']
cores = [GLIC, AZUL, OXID]
for i, cor in enumerate(cores):
    y = 10 + i * 140
    p.append(f'<path d="M160 210 C 330 210, 330 {y+60}, 470 {y+60}" fill="none" stroke="{cor}" stroke-width="6"/>')
    p.append(caixa(480, y, 1184, 120, cor, CARTAO))
    p.append(f'<rect x="480" y="{y}" width="16" height="120" rx="6" fill="{cor}"/>')
p.append("</svg>")
cards = [("A · Mesma sessão", "cabe em 3 dias por semana", "maior risco para a explosão"),
         ("B · Dias diferentes", "cada sessão acontece descansada", "pede 4 a 5 dias"),
         ("C · Blocos", "cada capacidade tem a sua vez", "o erro: zerar a outra")]
rs = [rot(20, 178, "a semana", w=140, tam=24, cor=CLARO, peso=700, alinha="center")]
for i, (t, v, c) in enumerate(cards):
    y = 10 + i * 140
    rs += [rot(520, y + 38, t, w=400, tam=32, cor=TINTA, peso=700),
           rot(930, y + 22, "ganha: " + v, w=720, tam=26, cor=TINTA),
           rot(930, y + 64, "custa: " + c, w=720, tam=26, cor=FOSF, peso=600)]
S.append({"id": "saidas", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A decisão é de organização", "titulo": "Três saídas, todas defensáveis"})

# 11. ordem (Eddens)
p = [svg_abre(1664, 340, "Na mesma sessão, força antes do aeróbico rendeu cerca de 7% mais ganho de força dinâmica de perna do que a ordem inversa; hipertrofia e VO2máx não mudaram com a ordem")]
for j, ordem_ in enumerate([(FOSF, FOSF_T, AZUL, AZUL_T), (AZUL, AZUL_T, FOSF, FOSF_T)]):
    y = 20 + j * 140
    c1, f1, c2, f2 = ordem_
    p.append(f'<rect x="0" y="{y}" width="300" height="100" rx="10" fill="{f1}" stroke="{c1}" stroke-width="4"/>')
    p.append(f'<rect x="310" y="{y}" width="300" height="100" rx="10" fill="{f2}" stroke="{c2}" stroke-width="4"/>')
p.append("</svg>")
rs = [rot(0, 50, "1º força", w=300, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(310, 50, "2º aeróbico", w=300, tam=30, cor=AZUL, peso=700, alinha="center"),
      rot(0, 190, "1º aeróbico", w=300, tam=30, cor=AZUL, peso=700, alinha="center"),
      rot(310, 190, "2º força", w=300, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(660, 36, "cerca de 7% mais ganho de força dinâmica de perna", w=1000, tam=32, cor=FOSF, peso=700),
      rot(660, 176, "menos ganho de força de perna", w=1000, tam=32, cor=TINTA, peso=600),
      rot(0, 290, "Hipertrofia e VO₂máx: iguais nas duas ordens.", w=1664, tam=28, cor=OXID, peso=700)]
S.append({"id": "ordem", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída A, primeira regra", "titulo": "Primeiro o que é prioridade",
          "destaque": "Se a prioridade é força, ela vem antes. Se é corrida, inverte. Quase sempre quem decide a ordem é o horário da academia.",
          "destaque_cor": "ambar", "fonte": "Eddens, van Someren e Howatson, Sports Medicine 2018 · 10 estudos, mesma sessão"})

# 12. intervalo (Robineau)
x0, x1, hmax = 300, 1300, 27
fx = lambda h: x0 + h / hmax * (x1 - x0)
p = [svg_abre(1664, 380, "Força sempre antes; aeróbico logo depois, 6 horas depois ou 24 horas depois. O grupo sem intervalo ganhou menos força máxima no supino e no agachamento")]
for j, gap in enumerate([0, 6, 24]):
    y = 20 + j * 100
    p.append(f'<line x1="{x0}" y1="{y+35}" x2="{x1}" y2="{y+35}" stroke="{GRADE}" stroke-width="3"/>')
    p.append(f'<rect x="{fx(0):.0f}" y="{y}" width="{fx(1.5)-fx(0):.0f}" height="70" rx="6" fill="{FOSF}"/>')
    p.append(f'<rect x="{fx(1.5+gap):.0f}" y="{y}" width="{fx(1.5)-fx(0):.0f}" height="70" rx="6" fill="{AZUL}"/>')
for h in [0, 6, 12, 18, 24]:
    p.append(f'<line x1="{fx(h):.0f}" y1="310" x2="{fx(h):.0f}" y2="322" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<line x1="{x0}" y1="310" x2="{x1}" y2="310" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(0, 36, "sem intervalo", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 136, "6 horas", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 236, "24 horas", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(1340, 22, "menos força máxima", w=324, tam=28, cor=FOSF, peso=700),
      rot(1340, 136, "ganho preservado", w=324, tam=28, cor=OXID, peso=700),
      rot(1340, 236, "ganho preservado", w=324, tam=28, cor=OXID, peso=700)]
for h in [0, 6, 12, 18, 24]:
    rs.append(rot(fx(h) - 60, 328, f"{h} h", w=120, tam=24, cor=MUDO, alinha="center"))
S.append({"id": "intervalo", "tipo": "diagrama", "h": 370, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída A, segunda regra", "titulo": "Se der para separar no mesmo dia, separa",
          "destaque": "Seis horas é a referência prática. Colado, o lado que a pessoa mais queria melhorar recebe a sessão pior.",
          "destaque_cor": "tinta", "fonte": "Robineau e colaboradores, Journal of Strength and Conditioning Research 2016 · rúgbi amador, 7 semanas, força sempre antes · vermelho força, azul aeróbico"})

# 13. calendário
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
cw, gx, lx = 196, 12, 220
cx = lambda i: lx + i * (cw + gx)
p = [svg_abre(1664, 420, "Duas semanas. Na primeira, perna pesada na sexta à noite e 20 quilômetros no sábado às sete da manhã: colisão. Na segunda, a perna foi para terça e o longo continua no sábado")]
semanas = [{"sex": ("perna pesada", "19h", FOSF), "sáb": ("longo 20 km", "7h", AZUL)},
           {"ter": ("perna pesada", "19h", FOSF), "sáb": ("longo 20 km", "7h", AZUL)}]
rs = [rot(cx(i), 0, d, w=cw, tam=26, cor=MUDO, peso=600, alinha="center") for i, d in enumerate(dias)]
for j, semana in enumerate(semanas):
    y = 50 + j * 190
    for i, d in enumerate(dias):
        if d in semana:
            t, h, cor = semana[d]
            p.append(f'<rect x="{cx(i)}" y="{y}" width="{cw}" height="130" rx="12" fill="{cor}"/>')
            rs.append(rot(cx(i) + 8, y + 20, t, w=cw - 16, tam=26, cor=CLARO, peso=700, alinha="center"))
            rs.append(rot(cx(i) + 8, y + 84, h, w=cw - 16, tam=24, cor=CLARO, alinha="center"))
        else:
            p.append(f'<rect x="{cx(i)}" y="{y}" width="{cw}" height="130" rx="12" fill="{CLARO}" stroke="{BORDA}" stroke-width="2"/>')
p.append(f'<path d="M{cx(4)+20} 196 C {cx(4)+90} 236, {cx(5)+100} 236, {cx(5)+170} 196" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M{cx(1)+cw/2} 386 L{cx(1)+cw/2} 400 L{cx(5)+cw/2} 400 L{cx(5)+cw/2} 386" fill="none" stroke="{OXID}" stroke-width="4"/>')
p.append("</svg>")
rs += [rot(0, 90, "antes", w=200, tam=30, cor=FOSF, peso=700),
       rot(0, 280, "depois", w=200, tam=30, cor=OXID, peso=700),
       rot(cx(5) + cw / 2 + 16, 392, "4 dias entre as duas", w=400, tam=24, cor=OXID, peso=700),
       rot(cx(2), 200, "colisão: 12 horas entre as duas", w=cx(4) + 20 - cx(2), tam=26, cor=FOSF, peso=700, alinha="right")]
S.append({"id": "calendario", "tipo": "diagrama", "h": 424, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída B, dias diferentes", "titulo": "Nada errado nos exercícios. Tudo errado no calendário",
          "destaque": "Mover a perna para o dia mais distante do longo costuma resolver a queixa inteira, sem tirar nada de ninguém. O custo: 4 a 5 dias por semana.",
          "destaque_cor": "petr", "fonte": "Exemplo ilustrativo"})

# 14. blocos
p = [svg_abre(1664, 420, "Três blocos de 8 a 12 semanas: ênfase em força com corrida em manutenção, ênfase em corrida com força em manutenção; no bloco final antes da prova, o erro comum é zerar a força")]
blocos = [("Ênfase em força", 1.0, 0.35, False), ("Ênfase em corrida", 0.35, 1.0, False), ("Antes da prova: o erro", 0.0, 1.0, True)]
rs = []
for i, (t, f, c, erro) in enumerate(blocos):
    x = i * 560
    p.append(f'<rect x="{x}" y="60" width="530" height="300" rx="14" fill="{FOSF_T if erro else CLARO}" stroke="{FOSF if erro else BORDA}" stroke-width="{4 if erro else 2}"/>')
    base = 320
    if f > 0:
        p.append(f'<rect x="{x+110}" y="{base - 220*f:.0f}" width="130" height="{220*f:.0f}" rx="4" fill="{FOSF}"/>')
    else:
        p.append(f'<rect x="{x+110}" y="{base-220*0.35:.0f}" width="130" height="{220*0.35:.0f}" rx="4" fill="none" stroke="{FOSF}" stroke-width="4" stroke-dasharray="12 10"/>')
    p.append(f'<rect x="{x+290}" y="{base - 220*c:.0f}" width="130" height="{220*c:.0f}" rx="4" fill="{AZUL}"/>')
    p.append(f'<line x1="{x+60}" y1="{base}" x2="{x+470}" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
    rs.append(rot(x, 0, t, w=530, tam=30, cor=FOSF if erro else TINTA, peso=700, alinha="center"))
    rs.append(rot(x + 70, 326, "força", w=210, tam=24, cor=FOSF, peso=700, alinha="center"))
    rs.append(rot(x + 250, 326, "corrida", w=210, tam=24, cor=AZUL, peso=700, alinha="center"))
    rs.append(rot(x, 376, "8 a 12 semanas", w=530, tam=24, cor=MUDO, alinha="center"))
rs.append(rot(1120 + 70, 180, "zerada", w=210, tam=26, cor=FOSF, peso=700, alinha="center"))
S.append({"id": "blocos", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída C, ênfase rotativa", "titulo": "Uma desenvolve, a outra se mantém",
          "destaque": "O erro mais comum do corredor amador: zerar a força nas doze semanas finais, quando o volume de corrida está maior. Chega à prova mais fraco.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

# 15. manutenção
S.append({"id": "manutencao", "tipo": "numeros", "eyebrow": "Quanto custa manter", "titulo": "Manutenção custa pouco, com uma condição",
          "numeros": [{"n": "1×/sem", "x": "e 1 série por exercício mantiveram força e tamanho por até 32 semanas em mais jovens", "cor": "tinta"},
                      {"n": "2×/sem", "x": "e 2 a 3 séries podem ser necessárias para manter o tamanho do músculo em mais velhos", "cor": "ambar"},
                      {"n": "carga", "x": "é a variável que não pode cair: corta frequência e volume, não o peso da barra", "cor": "verm"}],
          "destaque": "Manutenção não é abandono. E vale nos dois sentidos: quem zera o aeróbico num bloco de força reconstrói do zero depois.",
          "fonte": "Spiering e colaboradores, Journal of Strength and Conditioning Research 2021"})

# 16. para quem importa
S.append({"id": "quem", "tipo": "duas", "eyebrow": "Para quem essa conversa é séria", "titulo": "Onde importa, onde é nota de rodapé",
          "esq": {"t": "Importa", "cor": "verm",
                  "itens": ["Levantador, velocista, saltador, lutador em fase específica", "Fase de competição de esporte de força", "Quem está com a conta apertada: aí é falta de recuperação"]},
          "dir": {"t": "Nota de rodapé", "cor": "petr",
                  "itens": ["Corredor de rua com duas sessões de força", "Quem treina por saúde", "O master: nele, o que custa força é o tempo", "Coletivo amador: força na semana, longe do jogo"]},
          "destaque": "O inimigo do master não é o aeróbico que ele gosta de fazer. É a sessão de força que nunca entra na agenda.",
          "destaque_cor": "ambar"})

# 17. OMS
S.append({"id": "oms", "tipo": "numeros", "eyebrow": "O argumento de saúde pública", "titulo": "Quem segue a OMS faz treino concorrente",
          "numeros": [{"n": "150 a 300", "x": "minutos por semana de atividade aeróbica moderada, para adultos", "cor": "tinta"},
                      {"n": "2 ou mais", "x": "dias por semana de fortalecimento muscular", "cor": "verm"}],
          "destaque": "E está fazendo certo.", "destaque_cor": "petr",
          "fonte": "Bull e colaboradores, British Journal of Sports Medicine 2020 · diretrizes da OMS"})

# 18. critério
p = [svg_abre(1664, 400, "No centro, a pergunta: o que é prioridade nesta fase? Dela saem quatro decisões: horário, manutenção, modalidade e comida")]
p.append(f'<ellipse cx="832" cy="200" rx="260" ry="120" fill="{TINTA}"/>')
quad = [(0, 0), (1144, 0), (0, 250), (1144, 250)]
for (x, y) in quad:
    p.append(caixa(x, y, 520, 150, OXID, CARTAO, esp=3))
    ax = x + 520 if x == 0 else x
    ay = y + 75
    bx = 600 if x == 0 else 1064
    by = 150 if y == 0 else 250
    p.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{OXID}" stroke-width="4"/>')
p.append("</svg>")
itens = [("Horário", "a prioridade vai primeiro, descansada"), ("Manutenção", "a outra em dose mínima, carga mantida"),
         ("Modalidade", "pelo custo mecânico, quando dá"), ("Comida", "glicogênio sustenta as duas")]
rs = [rot(612, 140, "O que é prioridade nesta fase?", w=440, tam=34, cor=CLARO, peso=700, alinha="center", serif=True)]
for (x, y), (t, s_) in zip(quad, itens):
    rs += [rot(x + 28, y + 22, t, w=470, tam=30, cor=TINTA, peso=700), rot(x + 28, y + 70, s_, w=470, tam=26, cor=APOIO2)]
S.append({"id": "criterio", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O critério", "titulo": "Nunca é “força ou aeróbico”",
          "destaque": "Três sinais juntos apontam interferência: a queixa começou com a segunda capacidade, o treino que piorou vem logo depois do outro, e o volume total não mudou. Aí, mova uma sessão.",
          "destaque_cor": "verm"})

# 19. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Duas regras",
          "regras": ["Primeiro o que é prioridade, no melhor horário", "Manutenção não é abandono: a carga fica"],
          "cards": [{"t": "Preparador e educador físico", "x": "Montam a semana e decidem a ordem, o intervalo e os blocos."},
                    {"t": "As outras profissões", "x": "Olham o calendário e enxergam a colisão por trás de “meu rendimento caiu” ou “meu tendão dói”."}],
          "quem": "Três dias por semana? Sessão combinada, a prioridade primeiro. A que se cumpre vence quase sempre."})

# deck enxuto: blocos vizinhos da aula fundidos; fica um visual por bloco
MANTER = ['hickson', 'camadas', 'schumann', 'treinados', 'saidas', 'ordem', 'calendario', 'blocos', 'quem', 'criterio', 'fecho']
S = [s for s in S if s["id"] in MANTER]

spec = {"arquivo": "aulas/MOD02/02-09-treino-concorrente-e-o-efeito-interferencia.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "O calendário, não a molécula", "subtitulo": "Treino concorrente e o efeito interferência",
        "nota_capa": "Entra pela pergunta que chega pronta.",
        "secoes": {"origem": ["De onde vem o medo: Hickson e as duas camadas.", "capa"],
                   "evidencia": ["O que a evidência diz hoje, e para quem.", "schumann"],
                   "saidas": ["Três saídas de organização.", "saidas"],
                   "criterio": ["Para quem importa e o critério.", "quem"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-09.json"), "w"), ensure_ascii=False, indent=1)
print("02-09.json:", len(S), "slides")
