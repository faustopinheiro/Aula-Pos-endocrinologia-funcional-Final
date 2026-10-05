"""Spec do deck 13.3. Gera 13-03.json ao lado deste arquivo."""
from _base import *

S = []
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def semana(x0, y0, wd, h, blocos, rs, p, rotulo_dia=True):
    """Desenha sete colunas; blocos = {dia: (texto, cor)}; dia sem bloco fica tracejado."""
    for j, d in enumerate(DIAS):
        x = x0 + j * (wd + 10)
        if rotulo_dia:
            rs.append(rot(x, y0 - 36, d, w=wd, tam=22, cor=MUDO, peso=700, alinha="center"))
        if d in blocos:
            t, c = blocos[d]
            p.append(f'<rect x="{x}" y="{y0}" width="{wd}" height="{h}" rx="12" fill="{c}"/>')
            rs.append(rot(x + 6, y0 + 16, t, w=wd - 12, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.2))
        else:
            p.append(f'<rect x="{x}" y="{y0}" width="{wd}" height="{h}" rx="12" fill="none" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')


# 1. a ciclista
p = [svg_abre(1664, 440, "Uma semana de ciclista: sábado e domingo com quatro horas de pedal cada; de segunda a sexta, nada. Balão de fala: isso conta, ou estou fazendo mal ao corpo?")]
rs = []
p.append(icone("t:bike", 0, 40, 260, AZUL))
semana(320, 220, 180, 200, {"sáb": ("quatro horas", AZUL), "dom": ("quatro horas", AZUL)}, rs, p)
p.append(caixa(320, 0, 900, 130, GLIC, GLIC_T, esp=3, rx=24))
p.append(f'<path d="M 520 130 L 500 168 L 570 130" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
rs.append(rot(350, 30, "“Isso conta, ou estou fazendo mal ao corpo?”", w=840, tam=30, cor=TINTA, peso=700, serif=True))
p.append(caixa(1260, 0, 404, 130, GRADE, CARTAO, esp=2, rx=16))
rs += [rot(1280, 18, "duas perguntas:", w=364, tam=22, cor=MUDO, peso=700),
       rot(1280, 56, "viver mais · se machucar", w=364, tam=26, cor=TINTA, peso=700, serif=True)]
rs.append(rot(0, 320, "uma ciclista na casa dos cinquenta", w=280, tam=22, cor=AZUL, peso=700, lh=1.25))
diagrama(S, "ciclista", 440, p, rs, eyebrow="Ciclismo de fim de semana", titulo="Oito horas em dois dias: conta, ou faz mal?")

# 2. o estudo de 2017
p = [svg_abre(1664, 440, "Risco de morte por qualquer causa contra inativos, que valem 1,0. Pouco ativo em uma ou duas sessões: 0,66. Concentrado em uma ou duas sessões: 0,70. Regularmente ativo: 0,65. Ficha: 63.591 adultos acima dos 40, Inglaterra e Escócia, 1994 a 2012; concentrados, 3,7% da amostra")]
rs = []
B, H = 400, 340
p.append(f'<line x1="0" y1="{B}" x2="1000" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="0" y1="{B - H}" x2="1000" y2="{B - H}" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 6"/>')
rs.append(rot(0, B - H - 34, "inativo = 1,0", w=300, tam=22, cor=MUDO, peso=700))
for j, (t, v, c) in enumerate([("inativo", 1.0, GRADE), ("pouco ativo, uma ou duas sessões", 0.66, MUDO),
                               ("concentrado, uma ou duas sessões", 0.70, FOSF), ("regularmente ativo", 0.65, AZUL)]):
    x = 30 + j * 245
    h = H * v
    p.append(f'<rect x="{x}" y="{B - h:.0f}" width="180" height="{h:.0f}" rx="10" fill="{c}"/>')
    rs.append(rot(x, B - h + 14, f"{v:.2f}".replace(".", ","), w=180, tam=30, cor=PAPEL if c != GRADE else TINTA, peso=700, alinha="center", serif=True))
    rs.append(rot(x - 20, B + 12, t, w=220, tam=20, cor=TINTA, peso=600, alinha="center", lh=1.2))
p.append(caixa(1080, 20, 584, 380, GRADE, CARTAO, esp=2, rx=18))
rs += [rot(1104, 40, "63.591 adultos", w=536, tam=36, cor=TINTA, peso=700, serif=True),
       rot(1104, 100, "acima dos 40 anos · Inglaterra e Escócia · 1994 a 2012 · atividade relatada", w=536, tam=24, cor=TINTA, peso=600, lh=1.3),
       rot(1104, 240, "concentrados: 3,7% da amostra", w=536, tam=26, cor=FOSF, peso=700),
       rot(1104, 300, "o maior ganho está em sair do zero", w=536, tam=24, cor=AZUL, peso=700, lh=1.25)]
diagrama(S, "coorte", 440, p, rs, eyebrow="Morte por qualquer causa, estudo de 2017", titulo="Concentrar reduziu a mortalidade quase tanto quanto espalhar",
         fonte="JAMA Intern Med 2017")


# 3. os intervalos
def xr(v):
    """Posição de uma razão de risco entre 0,4 e 1,2."""
    return 60 + (v - 0.4) / 0.8 * 1000


p = [svg_abre(1664, 440, "Padrão concentrado contra inativos, com intervalos de confiança. Qualquer causa: 0,70, de 0,60 a 0,82. Cardiovascular: 0,60, de 0,45 a 0,82. Câncer: 0,82, de 0,63 a 1,06, cruzando o 1. O intervalo que cruza o 1 não exclui o efeito nulo")]
rs = []
p.append(f'<line x1="{xr(1.0):.0f}" y1="0" x2="{xr(1.0):.0f}" y2="340" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{xr(0.4):.0f}" y1="340" x2="{xr(1.2):.0f}" y2="340" stroke="{TINTA}" stroke-width="3"/>')
for v in (0.4, 0.6, 0.8, 1.0, 1.2):
    p.append(f'<line x1="{xr(v):.0f}" y1="332" x2="{xr(v):.0f}" y2="348" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(xr(v) - 40, 356, f"{v:.1f}".replace(".", ","), w=80, tam=20, cor=MUDO, alinha="center"))
rs.append(rot(xr(1.0) + 12, 0, "sem efeito", w=200, tam=20, cor=MUDO, peso=700))
for j, (t, v, a, b, c) in enumerate([("qualquer causa", 0.70, 0.60, 0.82, AZUL), ("cardiovascular", 0.60, 0.45, 0.82, OXID), ("câncer", 0.82, 0.63, 1.06, FOSF)]):
    y = 70 + j * 90
    p.append(f'<line x1="{xr(a):.0f}" y1="{y}" x2="{xr(b):.0f}" y2="{y}" stroke="{c}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<circle cx="{xr(v):.0f}" cy="{y}" r="16" fill="{c}"/>')
    rs.append(rot(xr(0.4), y - 46, t, w=260, tam=22, cor=c, peso=700))
    rs.append(rot(xr(b) + 20, y - 14, f"{v:.2f} ({a:.2f} a {b:.2f})".replace(".", ","), w=300, tam=22, cor=TINTA, peso=700))
p.append(caixa(1180, 0, 484, 400, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1204, 24, "O intervalo que cruza o 1 não exclui o efeito nulo.", w=436, tam=28, cor=FOSF, peso=700, serif=True, lh=1.25),
       rot(1204, 200, "concentrados: pouco mais de 2 mil adultos, por isso os intervalos largos", w=436, tam=24, cor=TINTA, peso=600, lh=1.3)]
diagrama(S, "intervalos", 440, p, rs, eyebrow="O padrão concentrado, por causa de morte", titulo="O benefício cardiovascular é firme; o de câncer não exclui o nulo",
         fonte="JAMA Intern Med 2017")

# 4. o acelerômetro
p = [svg_abre(1664, 440, "Acelerômetro de pulso, uma semana, 89.573 pessoas. Mais da metade dos ativos acumula a maior parte da atividade em um ou dois dias. Os dois padrões ativos, contra inativos: fibrilação atrial cerca de 0,8; infarto 0,69; insuficiência cardíaca 0,63; AVC 0,81")]
rs = []
p.append(caixa(0, 0, 560, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:device-watch", 30, 30, 120, AZUL))
rs += [rot(170, 40, "89.573 pessoas", w=370, tam=32, cor=AZUL, peso=700, serif=True),
       rot(170, 92, "uma semana de acelerômetro no pulso", w=370, tam=22, cor=TINTA, peso=600, lh=1.25),
       rot(30, 210, "mais da metade dos ativos", w=500, tam=34, cor=TINTA, peso=700, serif=True, lh=1.2),
       rot(30, 300, "acumula a maior parte da atividade em um ou dois dias", w=500, tam=24, cor=AZUL, peso=700, lh=1.3)]
XA = 900
def xa(v):
    return XA + (v - 0.5) / 0.6 * 700
p.append(f'<line x1="{xa(1.0):.0f}" y1="10" x2="{xa(1.0):.0f}" y2="360" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{xa(0.5):.0f}" y1="360" x2="{xa(1.1):.0f}" y2="360" stroke="{TINTA}" stroke-width="3"/>')
for v in (0.5, 0.7, 0.9, 1.1):
    rs.append(rot(xa(v) - 40, 372, f"{v:.1f}".replace(".", ","), w=80, tam=20, cor=MUDO, alinha="center"))
for j, (t, v) in enumerate([("fibrilação atrial", 0.80), ("infarto", 0.69), ("insuficiência cardíaca", 0.63), ("AVC", 0.81)]):
    y = 60 + j * 80
    p.append(f'<line x1="{xa(v):.0f}" y1="{y}" x2="{xa(1.0):.0f}" y2="{y}" stroke="{GRADE}" stroke-width="4"/>')
    p.append(f'<circle cx="{xa(v):.0f}" cy="{y}" r="16" fill="{OXID}"/>')
    rs.append(rot(600, y - 14, t, w=250, tam=22, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(xa(1.0) + 16, y - 14, f"{v:.2f}".replace(".", ","), w=100, tam=22, cor=OXID, peso=700))
rs.append(rot(600, 400, "os dois padrões ativos, contra inativos, quase iguais", w=1064, tam=22, cor=OXID, peso=700, alinha="center"))
diagrama(S, "relogio", 440, p, rs, eyebrow="Medido em vez de perguntado, estudo de 2023", titulo="Medido, o padrão concentrado é o jeito mais comum de ser ativo",
         fonte="JAMA 2023")

# 5. a comparação direta
p = [svg_abre(1664, 440, "Uma balança equilibrada: o mesmo volume em um ou dois dias contra o mesmo volume em três dias ou mais. Concentrado contra regular, morte por qualquer causa: 1,08, de 0,97 a 1,20, cruzando o 1. Ficha: 350.978 adultos, Estados Unidos, seguimento mediano de 10,4 anos")]
rs = []
p.append(f'<line x1="500" y1="40" x2="500" y2="250" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<path d="M 440 260 L 560 260 L 500 220 Z" fill="{TINTA}"/>')
p.append(f'<line x1="140" y1="70" x2="860" y2="70" stroke="{TINTA}" stroke-width="6"/>')
for x, t, c, f in ((140, "o mesmo volume em um ou dois dias", FOSF, FOSF_T), (860, "o mesmo volume em três dias ou mais", AZUL, AZUL_T)):
    p.append(f'<line x1="{x}" y1="70" x2="{x}" y2="120" stroke="{TINTA}" stroke-width="3"/>')
    p.append(caixa(x - 140, 120, 280, 110, c, f, esp=3, rx=16))
    rs.append(rot(x - 124, 140, t, w=248, tam=22, cor=c, peso=700, alinha="center", lh=1.25))
def xb(v):
    return 100 + (v - 0.8) / 0.5 * 800
p.append(f'<line x1="{xb(0.8):.0f}" y1="380" x2="{xb(1.3):.0f}" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{xb(1.0):.0f}" y1="290" x2="{xb(1.0):.0f}" y2="380" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 6"/>')
p.append(f'<line x1="{xb(0.97):.0f}" y1="330" x2="{xb(1.20):.0f}" y2="330" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<circle cx="{xb(1.08):.0f}" cy="330" r="16" fill="{FOSF}"/>')
for v in (0.8, 1.0, 1.2):
    rs.append(rot(xb(v) - 40, 392, f"{v:.1f}".replace(".", ","), w=80, tam=20, cor=MUDO, alinha="center"))
rs.append(rot(xb(1.20) + 20, 314, "1,08 (0,97 a 1,20)", w=260, tam=22, cor=TINTA, peso=700))
p.append(caixa(1100, 0, 564, 440, GRADE, CARTAO, esp=2, rx=18))
rs += [rot(1124, 24, "350.978 adultos", w=516, tam=36, cor=TINTA, peso=700, serif=True),
       rot(1124, 86, "Estados Unidos · seguimento mediano de 10,4 anos", w=516, tam=24, cor=TINTA, peso=600, lh=1.3),
       rot(1124, 200, "qualquer causa, cardiovascular e câncer: intervalos cruzando o 1", w=516, tam=24, cor=FOSF, peso=700, lh=1.3),
       rot(1124, 320, "o que pesa é o total", w=516, tam=30, cor=TINTA, peso=700, serif=True)]
diagrama(S, "balanca", 440, p, rs, eyebrow="Concentrado contra regular, estudo de 2022", titulo="Com o mesmo volume, distribuir não mudou a mortalidade",
         fonte="JAMA Intern Med 2022")

# 6. os limites
p = [svg_abre(1664, 400, "Três estudos com seus limites: relato, não medida; uma semana de acelerômetro; observacional. Embaixo, uma faixa: nenhum dos três mediu lesão")]
rs = []
for k, (ano, lim, x_) in enumerate([("2017", "relato, não medida", "o que a pessoa diz fazer"),
                                    ("2023", "uma semana de acelerômetro", "a semana medida pode não ser a típica"),
                                    ("os três", "observacionais", "quem mantém o padrão é diferente em outras coisas")]):
    x = k * 564
    p.append(caixa(x, 0, 536, 250, GRADE, CARTAO, esp=2, rx=18))
    rs += [rot(x + 24, 20, ano, w=488, tam=26, cor=MUDO, peso=700),
           rot(x + 24, 70, lim, w=488, tam=30, cor=TINTA, peso=700, serif=True, lh=1.2),
           rot(x + 24, 170, x_, w=488, tam=22, cor=TINTA, peso=600, lh=1.25)]
p.append(f'<rect x="0" y="290" width="1664" height="100" rx="16" fill="{FOSF}"/>')
rs.append(rot(0, 318, "Nenhum dos três mediu lesão.", w=1664, tam=34, cor=PAPEL, peso=700, serif=True, alinha="center"))
diagrama(S, "limites", 400, p, rs, eyebrow="O que esses números não dizem", titulo="Os estudos respondem a viver mais, não a se machucar")

# 7. o salto
p = [svg_abre(1664, 450, "Esquema da carga na semana: zero de segunda a sexta, duas barras altas no sábado e no domingo. Uma linha tracejada baixa, a capacidade construída na semana. A diferença entre a barra do sábado e a linha é o salto. Ao lado: o esforço vigoroso eleva o risco cardíaco por algumas horas, mais em quem é pouco ativo"), defs(FOSF)]
rs = []
BB = 380
p.append(f'<line x1="0" y1="{BB}" x2="960" y2="{BB}" stroke="{TINTA}" stroke-width="3"/>')
for j, d in enumerate(DIAS):
    x = 20 + j * 134
    rs.append(rot(x, BB + 12, d, w=110, tam=22, cor=MUDO, peso=700, alinha="center"))
    if d in ("sáb", "dom"):
        p.append(f'<rect x="{x}" y="60" width="110" height="{BB - 60}" rx="10" fill="{AZUL}"/>')
    else:
        p.append(f'<rect x="{x}" y="{BB - 8}" width="110" height="8" rx="4" fill="{GRADE}"/>')
p.append(f'<line x1="0" y1="290" x2="960" y2="290" stroke="{OXID}" stroke-width="4" stroke-dasharray="12 8"/>')
rs.append(rot(20, 244, "capacidade construída na semana", w=560, tam=22, cor=OXID, peso=700))
xs = 20 + 5 * 134
p.append(seta(xs - 30, 290, xs - 30, 66, FOSF, "m0", 4))
rs.append(rot(xs - 250, 110, "o salto", w=200, tam=30, cor=FOSF, peso=700, alinha="right", serif=True))
rs.append(rot(20, 10, "esquema, sem valores medidos", w=400, tam=20, cor=MUDO))
p.append(caixa(1040, 0, 624, 450, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:heart", 1064, 24, 70, FOSF))
p.append(icone("t:bolt", 1124, 44, 46, FOSF))
rs += [rot(1190, 30, "o mesmo salto no coração", w=450, tam=26, cor=FOSF, peso=700, serif=True, lh=1.2),
       rot(1064, 140, "o esforço vigoroso eleva o risco por algumas horas", w=576, tam=26, cor=TINTA, peso=700, lh=1.25),
       rot(1064, 240, "mais em quem é pouco ativo", w=576, tam=26, cor=FOSF, peso=700),
       rot(1064, 320, "risco absoluto baixo; a atividade habitual o reduz", w=576, tam=22, cor=TINTA, peso=600, lh=1.3)]
diagrama(S, "salto", 450, p, rs, eyebrow="Onde mora o risco do padrão concentrado", titulo="O risco está no salto, não no total de horas")

# 8. a semana nova
p = [svg_abre(1664, 460, "A semana nova da ciclista: sábado e domingo de pedal com o grupo; terça, força por 25 minutos; quinta, pedal leve ou caminhada por 30 minutos. Lembrete: o efeito agudo sobre glicose dura de um a dois dias, e para glicose e pressão a distribuição pesa. Faixa: manter o sábado, acrescentar o que falta para tolerá-lo")]
rs = []
semana(0, 36, 216, 190, {"ter": ("força, 25 min", OXID), "qui": ("pedal leve ou caminhada, 30 min", OXID),
                         "sáb": ("pedal com o grupo", AZUL), "dom": ("pedal com o grupo", AZUL)}, rs, p)
p.append(caixa(0, 270, 760, 170, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:droplet", 24, 300, 56, GLIC))
rs += [rot(100, 290, "glicose e pressão", w=640, tam=26, cor=GLIC, peso=700, serif=True),
       rot(100, 340, "o efeito agudo dura de um a dois dias: aqui, a distribuição pesa", w=640, tam=22, cor=TINTA, peso=600, lh=1.3)]
p.append(f'<rect x="800" y="270" width="864" height="170" rx="18" fill="{OXID}"/>')
rs.append(rot(830, 310, "Manter o sábado, acrescentar o que falta para tolerá-lo.", w=804, tam=30, cor=PAPEL, peso=700, serif=True, lh=1.3))
diagrama(S, "semana", 460, p, rs, eyebrow="O que se prescreve", titulo="O fim de semana conta; o meio da semana protege")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Atividade concentrada em poucos dias", "titulo": "Para viver mais, o total pesa; para não se machucar, o salto",
          "regras": ["Para mortalidade, concentrar funcionou quase como espalhar",
                     "Os estudos não mediram lesão: o risco está no salto",
                     "Para glicose e pressão, a distribuição pesa"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Diz que o fim de semana conta e pergunta por sintomas no esforço."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Mantém o sábado e põe duas sessões curtas no meio da semana."},
                    {"ic": "t:user", "t": "O praticante", "x": "Protege o grupo do fim de semana e cumpre as duas sessões curtas."}]})

salvar("13-03.json", {"arquivo": "aulas/MOD13/13-03-atividade-concentrada-em-poucos-dias.md",
                      "titulo": "Atividade concentrada em poucos dias", "subtitulo": "O que o fim de semana faz pela mortalidade e pela lesão",
                      "nota_capa": "Entra por uma ciclista na casa dos cinquenta que pedala só no sábado e no domingo.",
                      "secoes": {"ciclista": ["A pergunta.", "capa"], "coorte": ["Os três estudos.", "coorte"],
                                 "salto": ["A lesão e a conduta.", "salto"]},
                      "slides": S})
