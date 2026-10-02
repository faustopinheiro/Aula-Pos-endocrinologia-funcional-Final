"""Spec do deck 12.1. Gera 12-01.json ao lado deste arquivo."""
from _base import *

S = []


def menino(x, base, alt, cor):
    """Silhueta simples de pé: cabeça e corpo, alt em px."""
    r = alt * 0.09
    return (f'<circle cx="{x}" cy="{base - alt + r:.0f}" r="{r:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.12:.0f}" y="{base - alt + 2 * r + 6:.0f}" width="{alt * 0.24:.0f}" height="{alt * 0.45:.0f}" rx="{alt * 0.05:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.1:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>'
            f'<rect x="{x + alt * 0.02:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>')


# 1. os três meninos
p = [svg_abre(1664, 460, "Três meninos de treze anos numa peneira de futebol: 1,45 m, 1,72 m e um no meio. Etiqueta: sub-13, nascidos no mesmo ano. Ao lado, a prancheta do avaliador com altura, velocidade e força")]
base = 400
for x, alt, c in ((140, 230, GLIC), (340, 345, OXID), (560, 290, AZUL)):
    p.append(menino(x, base, alt, c))
p.append(f'<line x1="40" y1="{base}" x2="700" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
rs = [rot(40, 414, "1,45 m", w=200, tam=24, cor=GLIC, peso=700, alinha="center"),
      rot(240, 414, "1,72 m", w=200, tam=24, cor=OXID, peso=700, alinha="center"),
      rot(460, 414, "1,59 m", w=200, tam=24, cor=AZUL, peso=700, alinha="center")]
p.append(caixa(760, 0, 300, 70, TINTA, TINTA, esp=0, rx=35))
rs.append(rot(760, 18, "sub-13 · mesmo ano", w=300, tam=26, cor=PAPEL, peso=700, alinha="center"))
p.append(caixa(1120, 0, 544, 460, TINTA, CARTAO, esp=2, rx=16))
rs.append(rot(1144, 20, "Prancheta do avaliador", w=500, tam=28, cor=TINTA, peso=700, serif=True))
for j, t in enumerate(["altura", "velocidade", "força", "ganha a dividida"]):
    y = 100 + j * 80
    p.append(f'<line x1="1144" y1="{y + 50}" x2="1640" y2="{y + 50}" stroke="{BORDA}" stroke-width="2"/>')
    rs.append(rot(1144, y + 6, t, w=300, tam=26, cor=TINTA, peso=600))
rs.append(rot(1144, 420, "nenhuma linha para maturação", w=500, tam=24, cor=FOSF, peso=700))
diagrama(S, "tres", 460, p, rs, eyebrow="Uma peneira de futebol, categoria sub-13", titulo="Mesma idade no documento, corpos com anos de distância")

# 2. ritmos de maturação
p = [svg_abre(1664, 440, "Régua de idade biológica sob os três meninos: o primeiro bem atrás, o segundo bem à frente, com uma chave de vários anos. Embaixo, duas faixas do pico de crescimento: meninas por volta dos doze, meninos por volta dos catorze, cerca de dois anos de diferença. Esquema"), defs(TINTA)]
X = lambda a: 120 + (a - 9) / 9 * 1420
p.append(f'<line x1="{X(9):.0f}" y1="110" x2="{X(18):.0f}" y2="110" stroke="{TINTA}" stroke-width="4"/>')
rs = [rot(0, 40, "idade biológica", w=600, tam=26, cor=MUDO, peso=700)]
for a in range(9, 19):
    p.append(f'<line x1="{X(a):.0f}" y1="100" x2="{X(a):.0f}" y2="120" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(X(a) - 30, 128, str(a), w=60, tam=22, cor=MUDO, alinha="center"))
for a, c, t in ((11.4, GLIC, "1,45 m"), (13, AZUL, "1,59 m"), (14.8, OXID, "1,72 m")):
    p.append(f'<circle cx="{X(a):.0f}" cy="110" r="18" fill="{c}" stroke="{CARTAO}" stroke-width="4"/>')
    rs.append(rot(X(a) - 80, 40, t, w=160, tam=24, cor=c, peso=700, alinha="center"))
p.append(f'<path d="M {X(11.4):.0f} 176 q 0 20 20 20 L {X(14.8) - 20:.0f} 196 q 20 0 20 -20" stroke="{FOSF}" stroke-width="4" fill="none"/>')
rs.append(rot(X(13) - 150, 206, "todos com 13 anos no documento", w=300, tam=24, cor=FOSF, peso=700, alinha="center"))
for j, (t, a0, a1, c, f) in enumerate([("meninas: pico por volta dos 12", 11, 13, FOSF, FOSF_T), ("meninos: pico por volta dos 14", 13, 15, AZUL, AZUL_T)]):
    y = 280 + j * 74
    p.append(f'<rect x="{X(a0):.0f}" y="{y}" width="{X(a1) - X(a0):.0f}" height="58" rx="12" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(X(a1) + 20, y + 14, t, w=520, tam=26, cor=c, peso=700))
rs.append(rot(0, 300, "esquema", w=200, tam=22, cor=MUDO))
diagrama(S, "faixa", 440, p, rs, eyebrow="Ritmos de maturação", titulo="Na puberdade, o calendário deixa de descrever o corpo")

# 3. métodos
p = [svg_abre(1664, 470, "Quatro métodos de estimar maturação: idade óssea, referência, consultório; estágios puberais, consultório com privacidade; equação do tempo até o pico, campo, erro de cerca de meio ano; percentual da estatura adulta prevista, campo, com altura dos pais. Um quinto, mais simples: altura a cada três meses")]
rs = []
mets = [("Idade óssea", "radiografia de mão e punho", "referência · consultório", AZUL, AZUL_T, "h:doctor"),
        ("Estágios puberais", "exame físico", "consultório · privacidade", AZUL, AZUL_T, "h:doctor"),
        ("Tempo até o pico", "estatura, altura sentada, perna, peso", "campo · erro de ~meio ano", OXID, OXID_T, "t:stopwatch"),
        ("% da estatura adulta", "medidas e altura dos pais", "campo", OXID, OXID_T, "t:users")]
for j, (t, a, b, c, f, ic) in enumerate(mets):
    x = j * 420
    p.append(caixa(x, 0, 396, 300, c, f, esp=3, rx=16))
    p.append(icone(ic, x + 20, 20, 52, c))
    rs += [rot(x + 84, 30, t, w=296, tam=27, cor=c, peso=700, lh=1.15), rot(x + 20, 120, a, w=356, tam=24, cor=TINTA, lh=1.3),
           rot(x + 20, 230, b, w=356, tam=24, cor=c, peso=700, lh=1.2)]
p.append(caixa(0, 340, 1664, 130, GLIC, GLIC_T, esp=3, rx=16))
p.append(f'<rect x="40" y="360" width="16" height="90" fill="{GLIC}"/>')
for i in range(6):
    p.append(f'<line x1="56" y1="{368 + i * 15}" x2="{80 if i % 2 else 70}" y2="{368 + i * 15}" stroke="{GLIC}" stroke-width="3"/>')
rs.append(rot(120, 380, "O mais simples: altura a cada três meses, sempre do mesmo jeito", w=1500, tam=30, cor=TINTA, peso=700, serif=True))
diagrama(S, "metodos", 470, p, rs, eyebrow="Como se estima a idade biológica", titulo="Uma estimativa imperfeita vale mais que a data de nascimento",
         fonte="Equação de tempo até o pico: Med Sci Sports Exerc 2002")

# 4. as curvas de desempenho
p = [svg_abre(1664, 440, "Duas curvas de desempenho dos doze aos vinte anos. A de quem amadureceu cedo começa alta e se achata; a de quem amadureceu tarde começa baixa, sobe e cruza a primeira perto dos dezessete. Faixa sobre os treze e catorze: onde acontecem as seleções. Esquema")]
A = lambda a: 120 + (a - 12) / 8 * 1100
p.append(f'<rect x="{A(13):.0f}" y="10" width="{A(15) - A(13):.0f}" height="340" fill="{FOSF_T}"/>')
rs = [rot(A(13), 20, "onde acontecem as seleções", w=A(15) - A(13), tam=24, cor=FOSF, peso=700, alinha="center", lh=1.2)]
p.append(f'<line x1="{A(12):.0f}" y1="350" x2="{A(20):.0f}" y2="350" stroke="{TINTA}" stroke-width="3"/>')
for a in range(12, 21, 2):
    rs.append(rot(A(a) - 40, 360, f"{a} anos", w=80, tam=22, cor=MUDO, alinha="center"))
p.append(f'<path d="M {A(12):.0f} 170 C {A(14):.0f} 110 {A(16):.0f} 100 {A(20):.0f} 96" stroke="{OXID}" stroke-width="7" fill="none"/>')
p.append(f'<path d="M {A(12):.0f} 300 C {A(15):.0f} 290 {A(16.5):.0f} 120 {A(20):.0f} 60" stroke="{GLIC}" stroke-width="7" fill="none"/>')
rs += [rot(A(20) + 20, 80, "amadureceu cedo", w=420, tam=26, cor=OXID, peso=700), rot(A(20) + 20, 30, "amadureceu tarde", w=420, tam=26, cor=GLIC, peso=700),
       rot(0, 40, "desempenho", w=110, tam=22, cor=MUDO, lh=1.2), rot(0, 400, "esquema", w=200, tam=22, cor=MUDO)]
diagrama(S, "curvas", 440, p, rs, eyebrow="Desempenho na base", titulo="A vantagem de quem amadurece cedo é real e temporária",
         fonte="Revisão sobre maturação de jovens atletas, Br J Sports Med 2015")

# 5. o inverso
p = [svg_abre(1664, 420, "Uma balança: de um lado, uma ginasta pequena e leve, favorecida por amadurecer tarde; do outro, um jogador grande, favorecido por amadurecer cedo. Embaixo: o esporte decide quem leva vantagem e quem sofre pressão")]
p.append(f'<line x1="320" y1="220" x2="1340" y2="220" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<path d="M 830 220 l -60 160 l 120 0 z" fill="{TINTA}"/>')
p.append(menino(420, 210, 150, GLIC))
p.append(menino(1240, 210, 200, AZUL))
rs = [rot(0, 60, "ginástica, provas de fundo", w=360, tam=26, cor=GLIC, peso=700, alinha="right"),
      rot(0, 110, "favorece quem amadurece tarde", w=360, tam=24, cor=TINTA, alinha="right", lh=1.2),
      rot(1300, 60, "força, potência, tamanho", w=364, tam=26, cor=AZUL, peso=700),
      rot(1300, 110, "favorece quem amadurece cedo", w=364, tam=24, cor=TINTA, lh=1.2),
      rot(0, 390, "Em cada lado, quem tem o ritmo contrário sofre a pressão", w=1664, tam=28, cor=FOSF, peso=700, alinha="center")]
diagrama(S, "inverso", 420, p, rs, eyebrow="Nem todo esporte premia o mesmo", titulo="Ritmo de maturação não é mérito nem defeito")

# 6. agrupar por maturação
p = [svg_abre(1664, 440, "Dois campos. No primeiro, times montados por ano de nascimento, com tamanhos muito diferentes. No segundo, times montados por maturação, com tamanhos parecidos e idades misturadas. Faixa: complementa a categoria por idade, não a substitui")]
rs = []
for k, (t, alts, c) in enumerate([("por ano de nascimento", [120, 200, 150, 230, 130], MUDO), ("por maturação", [170, 180, 175, 165, 185], OXID)]):
    x0 = k * 860
    p.append(caixa(x0, 0, 804, 330, c, OXID_T if k else PAPEL, esp=3, rx=18))
    rs.append(rot(x0 + 24, 18, t, w=760, tam=28, cor=c, peso=700, serif=True))
    for i, a in enumerate(alts):
        p.append(menino(x0 + 110 + i * 150, 310, a, AZUL if i % 2 else GLIC))
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Complementa a categoria por idade; não a substitui", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "grupos", 440, p, rs, eyebrow="Uma resposta em teste", titulo="Agrupar por maturação muda o que o avaliador enxerga")

# 7. a ficha refeita
p = [svg_abre(1664, 460, "Ficha de avaliação refeita, com duas colunas novas: estimativa de maturação e desempenho ajustado. Um carimbo riscado: cortado aos 13. No lugar dele: reavaliar em 6 meses")]
p.append(caixa(0, 0, 1060, 460, TINTA, CARTAO, esp=2, rx=16))
cols = ["atleta", "altura", "velocidade", "maturação", "leitura"]
rs = []
for i, c in enumerate(cols):
    rs.append(rot(30 + i * 205, 24, c, w=200, tam=24, cor=OXID if i >= 3 else TINTA, peso=700))
linhas = [("A", "1,45", "média", "tardia", "promissor"), ("B", "1,72", "alta", "precoce", "vantagem de corpo"), ("C", "1,59", "média", "na média", "acompanhar")]
for j, row in enumerate(linhas):
    y = 90 + j * 90
    p.append(f'<line x1="20" y1="{y + 66}" x2="1040" y2="{y + 66}" stroke="{BORDA}" stroke-width="2"/>')
    for i, v in enumerate(row):
        rs.append(rot(30 + i * 205, y + 14, v, w=200, tam=24, cor=OXID if i >= 3 else TINTA, peso=600, lh=1.2))
p.append(f'<rect x="30" y="384" width="1000" height="56" rx="10" fill="{OXID_T}"/>')
rs.append(rot(40, 396, "colunas novas: maturação estimada e leitura do desempenho contra ela", w=980, tam=22, cor=OXID, peso=700, alinha="center"))
p.append(caixa(1120, 40, 544, 140, FOSF, FOSF_T, esp=4, rx=14))
rs.append(rot(1140, 82, "cortado aos 13", w=504, tam=36, cor=FOSF, peso=700, serif=True, alinha="center"))
p.append(f'<line x1="1150" y1="160" x2="1634" y2="60" stroke="{FOSF}" stroke-width="6"/>')
p.append(caixa(1120, 260, 544, 140, OXID, OXID_T, esp=4, rx=14))
rs.append(rot(1140, 302, "reavaliar em 6 meses", w=504, tam=34, cor=OXID, peso=700, serif=True, alinha="center"))
diagrama(S, "ficha", 460, p, rs, eyebrow="O que fazer no lugar", titulo="A ficha ganha a maturação, e o corte vira reavaliação")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Crescimento e maturação", "titulo": "Na base, o corpo não segue o calendário",
          "regras": ["Idade no documento não é idade biológica: na puberdade, anos separam atletas do mesmo ano",
                     "Desempenho na base se lê junto com a maturação",
                     "Corte definitivo nessa idade se evita: reavaliar custa pouco"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e avalia", "x": "Estima a maturação em campo e lê o desempenho contra ela."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Avalia maturação no consultório quando há dúvida clínica."},
                    {"ic": "t:users", "t": "Todos", "x": "Explicam ao adolescente e à família que ritmo não é talento nem defeito."}]})

salvar("12-01.json", {"arquivo": "aulas/MOD12/12-01-crescimento-e-maturacao.md",
                      "titulo": "Crescimento e maturação", "subtitulo": "Idade no documento não é idade do corpo",
                      "nota_capa": "Entra por três meninos de treze anos numa peneira de futebol. Abre o módulo.",
                      "secoes": {"tres": ["O erro.", "capa"], "metodos": ["Como estimar.", "metodos"],
                                 "curvas": ["O que muda na seleção.", "curvas"], "ficha": ["A ficha refeita.", "ficha"]},
                      "slides": S})
