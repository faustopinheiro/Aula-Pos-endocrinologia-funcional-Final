"""Spec do deck 14.9. Gera 14-09.json ao lado deste arquivo."""
from _base import *

S = []

BASE = [25, 25, 0, 50, 25, 25]
DEPOIS = [25, 50, 50, 75, 50, 75, 75, 100, 75, 75, 100, 75]

# 1. dois números
p = [svg_abre(1664, 420, "Duas barras: antes, 25% das sessões com aquecimento completo; um mês depois, 50%. Entre elas, uma seta e a pergunta: melhorou? Valores ilustrativos"), defs(TINTA)]
rs = []
for j, (v, t, c) in enumerate([(25, "antes", MUDO), (50, "um mês depois", OXID)]):
    x = 260 + j * 820
    h = v * 6
    p.append(f'<rect x="{x}" y="{340 - h}" width="320" height="{h}" rx="10" fill="{c}"/>')
    rs += [rot(x, 340 - h - 70, f"{v}%", w=320, tam=48, cor=c, peso=700, serif=True, alinha="center"),
           rot(x, 356, t, w=320, tam=26, cor=TINTA, peso=700, alinha="center")]
p.append(f'<line x1="200" y1="340" x2="1460" y2="340" stroke="{GRADE}" stroke-width="3"/>')
p.append(seta(640, 250, 1040, 180, TINTA, "m0", esp=5))
p.append(f'<circle cx="840" cy="110" r="54" fill="{FOSF}"/>')
rs += [rot(800, 76, "?", w=80, tam=56, cor=PAPEL, peso=700, serif=True, alinha="center"),
       rot(640, 270, "melhorou?", w=400, tam=30, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(1460, 300, "sessões com aquecimento completo · valores ilustrativos", w=204, tam=20, cor=MUDO, peso=700, lh=1.25)]
diagrama(S, "numeros", 420, p, rs, eyebrow="Futebol feminino sub-15, a mudança foi feita", titulo="Dois números não dizem se a mudança foi uma melhora")

# 2. três indicadores
p = [svg_abre(1664, 400, "Três indicadores. Processo: a mudança está acontecendo? Sessões com aquecimento completo. Resultado: o atleta está melhor? Lesões por mil horas de exposição. Equilíbrio: piorou alguma outra coisa? Minutos de treino com bola; queixa do técnico e das atletas")]
rs = []
for j, (t, q, ex, ic, c) in enumerate([("processo", "a mudança está acontecendo?", "sessões com aquecimento completo", "t:check", OXID),
                                       ("resultado", "o atleta está melhor?", "lesões por mil horas de exposição", "t:first-aid-kit", AZUL),
                                       ("equilíbrio", "piorou alguma outra coisa?", "minutos de treino com bola; queixa do técnico e das atletas", "t:scale", GLIC)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 400, c, CARTAO, esp=3, rx=18))
    p.append(f'<rect x="{x}" y="0" width="536" height="96" rx="18" fill="{c}"/>')
    p.append(icone(ic, x + 30, 22, 52, PAPEL))
    rs += [rot(x + 100, 28, t, w=420, tam=32, cor=PAPEL, peso=700, serif=True),
           rot(x + 28, 130, q, w=480, tam=30, cor=c, peso=700, serif=True, lh=1.2),
           rot(x + 28, 250, ex, w=480, tam=26, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "indicadores", 400, p, rs, eyebrow="Três indicadores, três perguntas", titulo="O projeto mede o processo, o resultado e o que pode piorar")

# 3. a conta da exposição
p = [svg_abre(1664, 420, "Dois semestres: três lesões no primeiro, duas no segundo, uma queda de 33%. Cerca de 1.400 horas de exposição por semestre: 22 atletas, 4 horas por semana, 16 semanas. Uma lesão a mais ou a menos muda o número inteiro. Esquema, valores ilustrativos"), defs(TINTA)]
rs = []
for j, (t, n) in enumerate([("semestre passado", 3), ("este semestre", 2)]):
    x = 60 + j * 760
    p.append(caixa(x, 0, 560, 230, MUDO, CARTAO, esp=2, rx=16))
    rs.append(rot(x, 20, t, w=560, tam=26, cor=TINTA, peso=700, alinha="center"))
    for k in range(n):
        p.append(icone("t:first-aid-kit", x + 280 - n * 55 + k * 110 + 5, 90, 90, AZUL))
p.append(seta(640, 115, 800, 115, FOSF, "m0", esp=5))
rs += [rot(600, 40, "−33%", w=240, tam=36, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(1400, 40, "22 atletas × 4 h × 16 semanas ≈ 1.400 h", w=264, tam=24, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(0, 270, 1664, 100, FOSF, FOSF_T, esp=3, rx=14))
rs += [rot(24, 296, "Evento raro, grupo pequeno, pouco tempo: uma lesão a mais ou a menos muda o número inteiro.", w=1616, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(0, 390, "esquema · valores ilustrativos", w=1664, tam=20, cor=MUDO, alinha="center")]
diagrama(S, "exposicao", 420, p, rs, eyebrow="Por que o resultado não decide sozinho", titulo="Em meses, numa categoria, a lesão é rara demais para mostrar efeito")

# 4. a definição operacional
p = [svg_abre(1664, 420, "Ficha da definição operacional. Aquecimento completo: os cinco blocos do programa, na ordem, com pelo menos quinze minutos. Quem conta: a auxiliar técnica, numa ficha. Quando: em toda sessão. Denominador: sessões realizadas, e não as previstas. Mude a definição, e o 1 de cada 4 vira outro número. Esquema")]
rs = []
p.append(caixa(0, 0, 1060, 420, AZUL, CARTAO, esp=3, rx=18))
p.append(icone("t:clipboard-list", 24, 20, 56, AZUL))
rs.append(rot(96, 30, "definição operacional", w=900, tam=30, cor=AZUL, peso=700, serif=True))
for j, (k, v) in enumerate([("o que conta", "os cinco blocos, na ordem, com 15 minutos ou mais"), ("quem conta", "a auxiliar técnica, numa ficha"),
                            ("quando", "em toda sessão"), ("denominador", "sessões realizadas, e não as previstas")]):
    y = 110 + j * 76
    p.append(f'<line x1="24" y1="{y + 60}" x2="1036" y2="{y + 60}" stroke="{GRADE}" stroke-width="2"/>')
    rs += [rot(24, y + 12, k, w=260, tam=26, cor=AZUL, peso=700),
           rot(300, y + 12, v, w=740, tam=26, cor=TINTA, peso=700)]
p.append(caixa(1120, 0, 544, 420, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1150, 40, "mude a definição, e o “1 de cada 4” vira outro número", w=484, tam=30, cor=FOSF, peso=700, serif=True, lh=1.25),
       rot(1150, 230, "escrita antes da primeira contagem; não muda no meio do projeto", w=484, tam=24, cor=TINTA, peso=700, lh=1.3),
       rot(1150, 370, "esquema", w=484, tam=20, cor=MUDO)]
diagrama(S, "definicao", 420, p, rs, eyebrow="Antes de contar", titulo="A definição operacional diz o que conta, quem conta e sobre o quê")

# gráfico de sequência: eixo comum
def grafico(pts, n_total, x0=140, x1=1600, y0=30, y1=370, mediana=25):
    out = [f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{GRADE}" stroke-width="3"/>',
           f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{GRADE}" stroke-width="3"/>']
    dx = (x1 - x0 - 40) / (n_total - 1)
    xs = [x0 + 20 + i * dx for i in range(n_total)]
    Y = lambda v: y1 - v / 100 * (y1 - y0)
    out.append(f'<line x1="{x0}" y1="{Y(mediana):.0f}" x2="{x1}" y2="{Y(mediana):.0f}" stroke="{AZUL}" stroke-width="3" stroke-dasharray="12 8"/>')
    d = " ".join(f'{"M" if i == 0 else "L"} {xs[i]:.0f} {Y(v):.0f}' for i, v in enumerate(pts))
    out.append(f'<path d="{d}" stroke="{TINTA}" stroke-width="3" fill="none"/>')
    for i, v in enumerate(pts):
        c = MUDO if i < len(BASE) else OXID
        out.append(f'<circle cx="{xs[i]:.0f}" cy="{Y(v):.0f}" r="11" fill="{c}" stroke="{PAPEL}" stroke-width="3"/>')
    return out, xs, Y

# 5. a linha de base
g, xs, Y = grafico(BASE, 18)
p = [svg_abre(1664, 420, "Linha de base: seis pontos semanais antes da mudança, 25, 25, 0, 50, 25 e 25 por cento, com a mediana em 25%. Valores ilustrativos")] + g
rs = [rot(0, 18, "100%", w=120, tam=22, cor=MUDO, alinha="right"), rot(0, 186, "50%", w=120, tam=22, cor=MUDO, alinha="right"),
      rot(0, 356, "0%", w=120, tam=22, cor=MUDO, alinha="right"),
      rot(xs[0] - 20, 386, "seis semanas, quatro sessões por semana", w=600, tam=22, cor=MUDO, peso=700),
      rot(xs[9], 296, "mediana: 25%", w=300, tam=26, cor=AZUL, peso=700),
      rot(xs[8], 60, "zero numa semana, cinquenta em outra, e nada mudou no clube: o processo variando sozinho", w=700, tam=26, cor=TINTA, peso=700, lh=1.3),
      rot(xs[8], 180, "valores ilustrativos", w=700, tam=20, cor=MUDO)]
diagrama(S, "linhabase", 420, p, rs, eyebrow="A linha de base", titulo="Medir antes de mudar mostra quanto o processo varia sozinho")

# 6. ciclos de teste pequeno
import math
p = [svg_abre(1664, 420, "Dois ciclos de planejar, fazer, estudar e agir em sequência, subindo. Ciclo 1: a capitã conduz o aquecimento numa sessão por semana, por duas semanas. Ciclo 2: o aquecimento entra no treino, com bola, em todas as sessões. Teste pequeno antes de mudar tudo"), defs(TINTA)]
rs = []
for j, (cx, cy, c, t, tx, ty) in enumerate([(150, 270, GLIC, "ciclo 1: a capitã conduz numa sessão por semana, por duas semanas", 300, 230),
                                           (790, 170, OXID, "ciclo 2: o aquecimento entra no treino, com bola, em todas as sessões", 940, 110)]):
    r = 130
    for k, a0 in enumerate([180, 270, 0, 90]):
        a1 = a0 + 90
        x1_, y1_ = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x2_, y2_ = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        p.append(f'<path d="M {cx} {cy} L {x1_:.0f} {y1_:.0f} A {r} {r} 0 0 1 {x2_:.0f} {y2_:.0f} Z" fill="{c}" opacity="{0.55 + 0.15 * k}" stroke="{PAPEL}" stroke-width="4"/>')
    for lab, ox, oy in [("planejar", -62, -46), ("fazer", 62, -46), ("estudar", 62, 26), ("agir", -62, 26)]:
        rs.append(rot(cx + ox - 60, cy + oy, lab, w=120, tam=22, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(tx, ty, t, w=330, tam=26, cor=c, peso=700, lh=1.3))
p.append(seta(290, 170, 640, 170, TINTA, "m0", esp=4))
p.append(caixa(1300, 160, 364, 240, TINTA, TINTA, esp=0, rx=18))
rs.append(rot(1324, 190, "teste pequeno primeiro: errar numa sessão custa pouco", w=316, tam=28, cor=PAPEL, peso=700, serif=True, lh=1.3))
diagrama(S, "ciclos", 420, p, rs, eyebrow="O método", titulo="O método é o teste pequeno, em ciclos de quatro passos")

# 7. o gráfico de sequência
g, xs, Y = grafico(BASE + DEPOIS, 18)
p = [svg_abre(1664, 440, "Gráfico de sequência com dezoito semanas: seis pontos de linha de base e doze depois da mudança, 25, 50, 50, 75, 50, 75, 75, 100, 75, 75, 100 e 75 por cento. Mediana da linha de base, 25%, estendida. Ciclo 1 na semana 7, ciclo 2 na semana 9. Valores ilustrativos")] + g
for w_, t in [(6, "ciclo 1"), (8, "ciclo 2")]:
    xm = (xs[w_] + xs[w_ - 1]) / 2
    p.append(f'<line x1="{xm:.0f}" y1="20" x2="{xm:.0f}" y2="370" stroke="{GLIC}" stroke-width="3" stroke-dasharray="6 6"/>')
rs = [rot(0, 18, "100%", w=120, tam=22, cor=MUDO, alinha="right"), rot(0, 186, "50%", w=120, tam=22, cor=MUDO, alinha="right"),
      rot(0, 356, "0%", w=120, tam=22, cor=MUDO, alinha="right"),
      rot((xs[6] + xs[5]) / 2 - 116, 380, "ciclo 1", w=110, tam=22, cor=GLIC, peso=700, alinha="right"),
      rot((xs[8] + xs[7]) / 2 + 8, 380, "ciclo 2", w=110, tam=22, cor=GLIC, peso=700),
      rot(xs[0] - 20, 40, "linha de base", w=300, tam=24, cor=MUDO, peso=700),
      rot(xs[13], 296, "mediana: 25%", w=300, tam=24, cor=AZUL, peso=700),
      rot(xs[9], 380, "depois da mudança · valores ilustrativos", w=620, tam=20, cor=MUDO, peso=700),
      rot(0, 410, "semanas, na ordem do tempo", w=1664, tam=20, cor=MUDO, alinha="center")]
diagrama(S, "grafico", 440, p, rs, eyebrow="O gráfico de sequência", titulo="Um ponto por semana, na ordem, contra a mediana da linha de base")

# 8. as quatro regras
p = [svg_abre(1664, 440, "Quatro regras do gráfico de sequência. Deslocamento: seis ou mais pontos seguidos do mesmo lado da mediana; ponto sobre a mediana não conta. Tendência: cinco ou mais pontos seguidos, todos subindo ou todos descendo. Sequências: poucas ou muitas demais para o número de pontos. Ponto astronômico: um valor claramente diferente dos outros. Menos de 5% de chance de acontecer por acaso")]
rs = []
MINI = [("deslocamento", "6+ pontos seguidos de um lado da mediana", [40, 45, 70, 72, 68, 75, 71, 74], OXID),
        ("tendência", "5+ pontos seguidos subindo ou descendo", [45, 40, 30, 42, 52, 61, 70, 80], GLIC),
        ("sequências", "cruza a mediana poucas ou muitas vezes", [30, 70, 28, 72, 30, 68, 32, 70], AZUL),
        ("ponto astronômico", "um valor muito diferente dos outros", [50, 45, 55, 48, 95, 52, 47, 50], FOSF)]
for j, (t, x_, pts, c) in enumerate(MINI):
    x = j * 424
    p.append(caixa(x, 0, 392, 360, c, CARTAO, esp=3, rx=16))
    p.append(f'<line x1="{x + 24}" y1="110" x2="{x + 368}" y2="110" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
    xs_ = [x + 40 + i * 44 for i in range(8)]
    d = " ".join(f'{"M" if i == 0 else "L"} {xs_[i]} {170 - v * 1.2:.0f}' for i, v in enumerate(pts))
    p.append(f'<path d="{d}" stroke="{TINTA}" stroke-width="2" fill="none"/>')
    for i, v in enumerate(pts):
        p.append(f'<circle cx="{xs_[i]}" cy="{170 - v * 1.2:.0f}" r="8" fill="{c}"/>')
    rs += [rot(x + 20, 186, t, w=352, tam=28, cor=c, peso=700, serif=True),
           rot(x + 20, 236, x_, w=352, tam=22, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(0, 380, 1664, 60, TINTA, TINTA, esp=0, rx=12))
rs.append(rot(20, 394, "cada regra: menos de 5% de chance de aparecer só por acaso", w=1624, tam=24, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "regras", 440, p, rs, eyebrow="Ler com regra, e não com vontade", titulo="Quatro regras dizem quando o gráfico mostra uma mudança de verdade",
         fonte="Perla, Provost e Murray, BMJ Qual Saf, 2011")

# 9. os três juntos
p = [svg_abre(1664, 420, "Painel com três linhas. Processo: deslocamento acima da mediana, a mudança aconteceu. Resultado: duas lesões no semestre, relatado, sem conclusão. Equilíbrio: minutos com bola mantidos, técnico a favor. A frase do projeto: o programa passou a ser feito, sem custo para o treino. Valores ilustrativos")]
rs = []
for j, (k, v, ic, c) in enumerate([("processo", "deslocamento acima da mediana: a mudança aconteceu", "t:check", OXID),
                                   ("resultado", "duas lesões no semestre: relatado, sem conclusão", "t:first-aid-kit", AZUL),
                                   ("equilíbrio", "minutos com bola mantidos; técnico a favor", "t:scale", GLIC)]):
    y = j * 96
    p.append(caixa(0, y, 1664, 80, c, CARTAO, esp=3, rx=14))
    p.append(f'<rect x="0" y="{y}" width="260" height="80" rx="14" fill="{c}"/>')
    p.append(icone(ic, 20, y + 16, 48, PAPEL))
    rs += [rot(80, y + 22, k, w=170, tam=26, cor=PAPEL, peso=700),
           rot(290, y + 22, v, w=1350, tam=26, cor=TINTA, peso=700)]
p.append(caixa(0, 310, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs += [rot(20, 330, "“o programa passou a ser feito, sem custo para o treino”, e não “reduzimos lesões”", w=1624, tam=28, cor=PAPEL, peso=700, serif=True, alinha="center"),
       rot(0, 398, "valores ilustrativos", w=1664, tam=20, cor=MUDO, alinha="center")]
diagrama(S, "painel", 420, p, rs, eyebrow="No fim do semestre", titulo="Os três indicadores juntos dizem o que o projeto pode afirmar")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Projeto aplicado: método e indicadores", "titulo": "Medir o processo, com regra, antes de afirmar o resultado",
          "regras": ["Três indicadores: processo, resultado e equilíbrio",
                     "Definição escrita e linha de base antes de mudar",
                     "Gráfico de sequência lido com as quatro regras"],
          "cards": [{"ic": "t:user", "t": "O aluno", "x": "Define, conta e desenha o gráfico toda semana."},
                    {"ic": "t:clipboard-list", "t": "Quem conta no lugar", "x": "Usa a mesma ficha do começo ao fim."},
                    {"ic": "t:book", "t": "O orientador", "x": "Confere a definição antes da contagem e as regras antes da conclusão."}]})

salvar("14-09.json", {"arquivo": "aulas/MOD14/14-09-projeto-aplicado-metodo-e-indicadores.md",
                      "titulo": "Projeto aplicado: método e indicadores", "subtitulo": "Como saber se a mudança foi uma melhora",
                      "nota_capa": "Entra por dois números, antes e depois, que não respondem à pergunta.",
                      "secoes": {"numeros": ["Os dois números.", "capa"], "indicadores": ["Os indicadores.", "indicadores"],
                                 "linhabase": ["Linha de base e método.", "linhabase"], "grafico": ["O gráfico e as regras.", "grafico"]},
                      "slides": S})
