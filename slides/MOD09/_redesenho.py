"""Desenhos que substituem os slides de texto do Módulo 9 (cartões, colunas, listas, tabelas e números).
Cada função devolve o dicionário do slide, com o mesmo id do slide que substitui."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

TRACO = ' stroke-dasharray="10 8"'
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL, BORDA = "#FDFCF9", "#F7F6F2", "#DDD8CC"
CINZA = "#C9CFD4"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"
def slide(id_, h, p, rs, **k):
    p.append("</svg>")
    d = {"id": id_, "tipo": "diagrama", "h": h, "svg": "".join(p), "rotulos": rs}
    d.update(k)
    return d


# ---------------------------------------------------------------- 9.1

def percurso_91():
    """9.1: a semana do ciclista: quatro saídas idênticas e aulas que nunca se repetem."""
    p = [svg_abre(1664, 340, "A semana de um ciclista amador em sete casas. Em quatro dias, o mesmo percurso em laço de sessenta quilômetros, na mesma média, há três anos. Em outros dois, uma aula de funcional em que nenhum treino se repete, cada um de uma cor. Embaixo: ele sabe os princípios de cor, e aplica ao contrário")]
    rs = []
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    tipo = ["bike", "func", "bike", "func", "bike", "bike", "off"]
    cores_f = [GLIC, FOSF]
    nf = 0
    for k, (d, t) in enumerate(zip(dias, tipo)):
        x = k * 236
        rs.append(rot(x, 0, d, w=216, tam=20, cor=MUDO, peso=700, alinha="center"))
        if t == "bike":
            p.append(caixa(x, 36, 216, 200, AZUL, AZUL_T, esp=2, rx=14))
            p.append(f'<ellipse cx="{x + 108}" cy="110" rx="70" ry="44" fill="none" stroke="{AZUL}" stroke-width="5"/>')
            p.append(f'<circle cx="{x + 38}" cy="110" r="9" fill="{AZUL}"/>')
            rs.append(rot(x, 170, "60 km · mesma média", w=216, tam=18, cor=AZUL, peso=700, alinha="center", lh=1.2))
        elif t == "func":
            p.append(caixa(x, 36, 216, 200, cores_f[nf], CARTAO, esp=2, rx=14))
            for j in range(6):
                cx, cy = x + 40 + (j % 3) * 68, 80 + (j // 3) * 60
                forma = [f'<rect x="{cx - 18}" y="{cy - 18}" width="36" height="36" rx="6"', f'<circle cx="{cx}" cy="{cy}" r="20"', f'<path d="M {cx} {cy - 22} L {cx + 22} {cy + 18} L {cx - 22} {cy + 18} Z"'][(j + nf) % 3]
                p.append(f'{forma} fill="{[GLIC, FOSF, OXID, AZUL][(j + nf * 2) % 4]}" opacity="0.8"/>')
            rs.append(rot(x, 190, "nunca se repete", w=216, tam=18, cor=cores_f[nf], peso=700, alinha="center"))
            nf += 1
        else:
            p.append(f'<rect x="{x}" y="36" width="216" height="200" rx="14" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(caixa(0, 262, 1664, 78, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(24, 282, "há três anos · sabe os princípios de cor, aplica ao contrário", w=1616, tam=23, cor=PAPEL, peso=700, alinha="center"))
    return slide("percurso", 340, p, rs, eyebrow="Sessenta quilômetros, quatro vezes por semana", titulo="Ele sabe os princípios de cor. Aplica ao contrário.")


def roteiro_91():
    """9.1: cinco princípios, cada um com o erro comum riscado ao lado."""
    p = [svg_abre(1664, 470, "Cinco linhas. Especificidade, reduzida a repetir o gesto do esporte. Sobrecarga, reduzida a fazer sempre mais. Individualidade, usada como desculpa: eu não respondo a esse treino. Variação, transformada em objetivo e não em ferramenta. Reversibilidade, lembrada quando o atleta para e esquecida no planejamento. Embaixo: quase ninguém erra por não conhecer os princípios; o problema está na aplicação"), defs(MUDO)]
    rs = []
    linhas = [("t:target", "Especificidade", "reduzida a repetir o gesto do esporte"), ("t:trending-up", "Sobrecarga", "reduzida a fazer sempre mais"),
              ("t:users", "Individualidade", "usada como desculpa: “eu não respondo a esse treino”"), ("t:refresh", "Variação", "transformada em objetivo, e não em ferramenta"),
              ("t:hourglass", "Reversibilidade", "lembrada quando o atleta para, esquecida no planejamento")]
    for k, (ic, t, e) in enumerate(linhas):
        y = k * 76
        p.append(caixa(0, y, 460, 64, OXID, OXID_T, esp=2, rx=12))
        p.append(icone(ic, 16, y + 12, 40, OXID))
        rs.append(rot(70, y + 16, t, w=380, tam=24, cor=OXID, peso=700, serif=True))
        p.append(seta(472, y + 32, 532, y + 32, MUDO, "m0", esp=3))
        p.append(caixa(546, y, 1118, 64, FOSF, FOSF_T, esp=2, rx=12))
        p.append(icone("t:x", 562, y + 14, 36, FOSF))
        rs.append(rot(614, y + 18, e, w=1030, tam=22, cor=TINTA))
    p.append(caixa(0, 394, 1664, 76, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(24, 414, "Quase ninguém erra por não conhecer os princípios", w=1616, tam=26, cor=PAPEL, peso=700, serif=True, alinha="center"))
    return slide("roteiro", 470, p, rs, eyebrow="Cinco princípios, cinco erros", titulo="O problema está na aplicação")


def especificidade_91():
    """9.1: a grade do experimento clássico, em esquema, e as quatro dimensões do estímulo no treino."""
    p = [svg_abre(1664, 360, "À esquerda, em esquema, uma grade do experimento clássico: três animais, cada um exposto a um agente; a resistência adquirida, marcada, aparece só no cruzamento com o próprio agente, como no animal resistente ao frio que não ficava resistente a outra agressão. À direita, no treino: o corpo se adapta ao estímulo, ao tecido, à velocidade e à amplitude; o gesto é parte disso, não o todo; o alvo é o estímulo que o esporte exige e a pessoa ainda não tolera")]
    rs = []
    p.append(caixa(0, 0, 700, 360, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "O experimento clássico · esquema", w=660, tam=22, cor=TINTA, peso=700, serif=True))
    ag = ["frio", "agente B", "agente C"]
    rs.append(rot(240, 64, "resistente a…", w=440, tam=17, cor=MUDO, alinha="center"))
    for j, a in enumerate(ag):
        rs.append(rot(240 + j * 150, 92, a, w=140, tam=18, cor=TINTA, peso=700, alinha="center"))
    for i, a in enumerate(ag):
        y = 130 + i * 70
        rs.append(rot(24, y + 18, f"exposto a {a}", w=200, tam=18, cor=TINTA, peso=700, alinha="right"))
        for j in range(3):
            x = 245 + j * 150
            ok = i == j
            p.append(f'<rect x="{x}" y="{y}" width="130" height="58" rx="10" fill="{OXID if ok else PAPEL}" stroke="{OXID if ok else BORDA}" stroke-width="2"/>')
            if ok:
                p.append(icone("t:shield-check", x + 47, y + 11, 36, PAPEL))
    p.append(caixa(760, 0, 904, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(784, 16, "No treino, o corpo se adapta a", w=860, tam=24, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:bolt", "estímulo"), ("t:barbell", "tecido"), ("t:stopwatch", "velocidade"), ("t:ruler-measure", "amplitude")]):
        x = 784 + j * 216
        p.append(f'<rect x="{x}" y="70" width="200" height="110" rx="12" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
        p.append(icone(ic, x + 78, 84, 44, OXID))
        rs.append(rot(x, 140, t, w=200, tam=21, cor=TINTA, peso=700, alinha="center"))
    rs += [rot(784, 204, "o gesto do esporte é parte disso, não o todo", w=860, tam=22, cor=TINTA),
           rot(784, 256, "o alvo: o estímulo que o esporte exige e a pessoa ainda não tolera", w=860, tam=22, cor=OXID, peso=700, lh=1.25)]
    return slide("especificidade", 360, p, rs, eyebrow="Erro um · especificidade", titulo="A resistência vale para o estímulo que a produziu",
                 destaque="O ciclista treina muito o gesto, sempre no mesmo estímulo.", destaque_cor="tinta", fonte="Selye, Nature 1936")


def dose_91():
    """9.1: antes do rótulo de não respondedor, o ciclo de ajustar a dose e medir de novo."""
    p = [svg_abre(1664, 360, "À esquerda, o rótulo não respondedor, riscado. No meio, a pergunta que vem antes: a dose era suficiente? À direita, um ciclo: ajustar a dose, o tipo de estímulo e o tempo, e medir de novo"), defs(MUDO, OXID)]
    rs = []
    p.append(caixa(0, 110, 380, 140, FOSF, FOSF_T, esp=2, rx=70))
    rs.append(rot(0, 160, "“não respondedor”", w=380, tam=27, cor=FOSF, peso=700, alinha="center", serif=True))
    p.append(f'<line x1="30" y1="230" x2="350" y2="130" stroke="{FOSF}" stroke-width="5"/>')
    p.append(seta(392, 180, 470, 180, MUDO, "m0", esp=3))
    p.append(caixa(484, 90, 420, 180, TINTA, TINTA, esp=0, rx=16))
    p.append(icone("t:question-mark", 664, 104, 48, PAPEL))
    rs.append(rot(500, 166, "a dose era suficiente?", w=388, tam=27, cor=PAPEL, peso=700, alinha="center", serif=True))
    p.append(seta(916, 180, 994, 180, MUDO, "m0", esp=3))
    cx, cy, r = 1310, 180, 150
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{OXID}" stroke-width="5"{TRACO}/>')
    for k, (ic, t, a) in enumerate([("t:barbell", "dose", -90), ("t:bolt", "estímulo", 0), ("t:clock", "tempo", 90), ("t:gauge", "medir de novo", 180)]):
        import math
        x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="{OXID}"/>')
        p.append(icone(ic, x - 18, y - 18, 36, PAPEL))
        dx = {-90: (-100, -86), 0: (40, -14), 90: (-100, 40), 180: (-100, 40)}[a]
        rs.append(rot(x + dx[0], y + dx[1], t, w=200, tam=20, cor=OXID, peso=700, alinha="center" if a in (-90, 90, 180) else "left"))
    rs.append(rot(cx - 120, cy - 16, "ajustar", w=240, tam=24, cor=TINTA, peso=700, alinha="center", serif=True))
    return slide("dose", 360, p, rs, eyebrow="A ideia da aula", titulo="Quase ninguém deixa de responder a tudo. Muita gente deixa de responder àquela dose.")


def variacao_91():
    """9.1: duas grades de seis semanas: exercícios-base mantidos, e exercícios que nunca se repetem."""
    p = [svg_abre(1664, 360, "Duas grades de seis semanas por três exercícios. À esquerda, variação planejada: os mesmos exercícios-base, A, B e C, mantidos por semanas, com uma troca com motivo na virada do bloco; a carga pode subir e ser medida. À direita, a tal confusão muscular: um exercício diferente em cada casa, nada se repete, nada progride")]
    rs = []
    for k, (t, d, cor, fundo) in enumerate([("Pode ajudar · planejada", "exercícios-base mantidos; troca com motivo", OXID, OXID_T),
                                            ("Pode atrapalhar · “confusão muscular”", "nada se repete, nada progride", FOSF, FOSF_T)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 360, cor, fundo, esp=2, rx=16))
        rs += [rot(x0 + 24, 16, t, w=780, tam=23, cor=cor, peso=700, serif=True), rot(x0 + 24, 312, d, w=780, tam=20, cor=TINTA, peso=700)]
        for s in range(6):
            rs.append(rot(x0 + 110 + s * 114, 62, f"sem {s + 1}", w=100, tam=16, cor=MUDO, alinha="center")) if k == 0 and s in (0, 5) else None
            for e in range(3):
                x, y = x0 + 110 + s * 114, 92 + e * 70
                if k == 0:
                    letra = "ABC"[e] if not (e == 2 and s >= 3) else "C′"
                    c = [OXID, AZUL, GLIC][e]
                else:
                    letra = "DEFGHIJKLMNOPQRSTU"[s * 3 + e]
                    c = [OXID, AZUL, GLIC, FOSF, MUDO][(s * 3 + e * 2) % 5]
                p.append(f'<rect x="{x}" y="{y}" width="100" height="58" rx="10" fill="{c}" opacity="0.85"/>')
                if k == 0:
                    rs.append(rot(x, y + 14, letra, w=100, tam=22, cor=PAPEL, peso=700, alinha="center")) if s == 0 or (e == 2 and s == 3) else None
    p.append(f'<line x1="{110 + 3 * 114 - 7}" y1="84" x2="{110 + 3 * 114 - 7}" y2="300" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs.append(rot(24, 120, "mesmo exercício →", w=80, tam=15, cor=MUDO, lh=1.2))
    return slide("variacao", 360, p, rs, eyebrow="Erro quatro · variação", titulo="Se nada se repete, nada progride",
                 destaque="Não dá para saber se a carga subiu num exercício que aparece uma vez por mês.", destaque_cor="tinta",
                 fonte="Revisão sistemática brasileira, 8 estudos · J Strength Cond Res 2022")


def reversibilidade_91():
    """9.1: a adaptação que sobe e cai na pausa, contra a dose de manutenção, e os três lugares do erro."""
    p = [svg_abre(1664, 380, "À esquerda, em esquema, uma linha de adaptação que sobe com o treino; na pausa, sem nada combinado, ela cai; com uma dose de manutenção, quase não cai. Toda adaptação se perde quando o estímulo some; o erro é não planejar para isso. À direita, três lugares onde o erro aparece: férias e lesões, sem o mínimo combinado; treino concorrente, a força some no bloco de resistência quando uma dose pequena manteria; o ciclista, que nunca faz força fora da bicicleta e perde, ano a ano, a que tinha")]
    rs = []
    X0, B = 40, 320
    p.append(f'<rect x="460" y="20" width="420" height="{B - 20}" fill="{PAPEL}"/>')
    rs.append(rot(460, 26, "pausa", w=420, tam=19, cor=MUDO, peso=700, alinha="center"))
    p.append(f'<line x1="{X0}" y1="{B}" x2="900" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {X0} 290 C 200 270, 330 130, 460 110" fill="none" stroke="{OXID}" stroke-width="6"/>')
    p.append(f'<path d="M 460 110 C 560 120, 700 250, 880 280" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<path d="M 460 110 C 600 116, 760 128, 880 134" fill="none" stroke="{OXID}" stroke-width="5"{TRACO}/>')
    rs += [rot(X0, 200, "treino", w=200, tam=20, cor=OXID, peso=700), rot(660, 92, "dose de manutenção", w=240, tam=19, cor=OXID, peso=700),
           rot(480, 284, "sem nada combinado", w=240, tam=19, cor=FOSF, peso=700), rot(X0, 340, "adaptação ao longo do tempo · esquema", w=600, tam=17, cor=MUDO)]
    for k, (ic, t, d, cor, fundo) in enumerate([("t:plane", "Férias e lesões", "ninguém combina o mínimo que mantém alguma coisa", GLIC, GLIC_T),
                                                ("t:arrows-exchange", "Treino concorrente", "a força some no bloco de resistência; uma dose pequena manteria", GLIC, GLIC_T),
                                                ("t:bike", "O ciclista", "nunca faz força fora da bicicleta e perde, ano a ano, a que tinha", FOSF, FOSF_T)]):
        y = k * 128
        p.append(caixa(960, y, 704, 116, cor, fundo, esp=2, rx=14))
        p.append(icone(ic, 980, y + 20, 40, cor))
        rs += [rot(1034, y + 16, t, w=610, tam=23, cor=cor, peso=700, serif=True), rot(1034, y + 54, d, w=610, tam=19, cor=TINTA, lh=1.25)]
    return slide("reversibilidade", 380, p, rs, eyebrow="Erro cinco · reversibilidade", titulo="Um princípio de planejamento, não de lamento",
                 destaque="Toda adaptação se perde quando o estímulo some. O erro é não planejar para isso.", destaque_cor="tinta")


def teoria_91():
    """9.1: três pilares firmes sobre uma base tracejada, a síndrome geral de adaptação, em esquema."""
    p = [svg_abre(1664, 360, "Em esquema, três pilares firmes: especificidade, progressão, recuperação e reversibilidade, consistentes nos estudos. Embaixo deles, uma base tracejada: a base fisiológica tradicional do planejamento, apoiada na síndrome geral de adaptação, uma leitura que a própria pesquisa sobre estresse já abandonou")]
    rs = []
    for k, t in enumerate(["especificidade", "progressão", "recuperação e reversibilidade"]):
        x = 140 + k * 480
        p.append(f'<rect x="{x}" y="20" width="400" height="200" rx="12" fill="{OXID}"/>')
        rs.append(rot(x + 20, 96, t, w=360, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True, lh=1.2))
    rs.append(rot(0, 0, "consistente nos estudos", w=130, tam=18, cor=OXID, peso=700, lh=1.2))
    p.append(f'<rect x="60" y="236" width="1544" height="110" rx="14" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"{TRACO}/>')
    rs += [rot(90, 252, "Mais fino do que se ensina: a base fisiológica tradicional do planejamento", w=1480, tam=23, cor=GLIC, peso=700, serif=True),
           rot(90, 296, "apoiada na síndrome geral de adaptação, uma leitura que a pesquisa sobre estresse já abandonou", w=1480, tam=21, cor=TINTA)]
    return slide("teoria", 360, p, rs, eyebrow="Uma honestidade", titulo="Os princípios se sustentam; a teoria é mais fina",
                 destaque="Planejar continua valendo. Muda a postura: menos confiança no modelo, mais no que se mede.", destaque_cor="tinta",
                 fonte="“Periodization theory: confronting an inconvenient truth”, Sports Med 2018")


def perguntas_91():
    """9.1: cada princípio virando uma pergunta, em balões."""
    p = [svg_abre(1664, 400, "Cinco princípios, cada um ao lado de um balão com a pergunta que ele obriga a fazer. Especificidade: que estímulo o esporte exige e a pessoa ainda não tolera? Sobrecarga: qual variável muda nesta semana, e só ela? Individualidade: a dose era suficiente antes de eu concluir que não funcionou? Variação: essa troca tem motivo, ou é só para não repetir? Reversibilidade: qual o mínimo que mantém o ganho quando a rotina quebrar?")]
    rs = []
    linhas = [("Especificidade", "que estímulo o esporte exige e a pessoa ainda não tolera?"), ("Sobrecarga", "qual variável muda nesta semana, e só ela?"),
              ("Individualidade", "a dose era suficiente antes de eu concluir que não funcionou?"), ("Variação", "essa troca tem motivo, ou é só para não repetir?"),
              ("Reversibilidade", "qual o mínimo que mantém o ganho quando a rotina quebrar?")]
    for k, (t, q) in enumerate(linhas):
        y = k * 80
        rs.append(rot(0, y + 20, t, w=300, tam=24, cor=OXID, peso=700, serif=True, alinha="right"))
        p.append(f'<path d="M 340 {y + 8} L 1650 {y + 8} Q 1664 {y + 8} 1664 {y + 22} L 1664 {y + 52} Q 1664 {y + 66} 1650 {y + 66} L 360 {y + 66} Q 346 {y + 66} 346 {y + 52} L 346 {y + 46} L 322 {y + 37} L 346 {y + 28} L 346 {y + 22} Q 346 {y + 8} 360 {y + 8} Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
        p.append(icone("t:question-mark", 362, y + 19, 36, OXID))
        rs.append(rot(410, y + 22, q, w=1230, tam=22, cor=TINTA, peso=700))
    return slide("perguntas", 400, p, rs, eyebrow="Princípio é pergunta", titulo="Cinco perguntas antes de montar a semana")


def ciclista_91():
    """9.1: a semana do ciclista antes e depois, em casas de dia, e as duas combinações que faltavam."""
    p = [svg_abre(1664, 400, "Duas semanas do ciclista em casas de dia. Antes: quatro saídas iguais, na mesma média, e aulas que nunca se repetem. Depois: uma saída com esforços mais intensos, uma mais longa, duas leves, e dois treinos de força com exercícios fixos por semanas. Embaixo, o que faltava: a resposta acompanhada, com a dose ajustada antes de concluir; e um mínimo de manutenção combinado para as viagens")]
    rs = []
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    antes = [("igual", AZUL), ("aula", GLIC), ("igual", AZUL), ("aula", GLIC), ("igual", AZUL), ("igual", AZUL), ("", None)]
    depois = [("leve", OXID), ("força", TINTA), ("intensa", FOSF), ("leve", OXID), ("força", TINTA), ("longa", AZUL), ("", None)]
    for j, d in enumerate(dias):
        rs.append(rot(220 + j * 206, 0, d, w=190, tam=19, cor=MUDO, peso=700, alinha="center"))
    for k, (t, sem) in enumerate([("Antes", antes), ("Depois", depois)]):
        y = 34 + k * 112
        rs.append(rot(0, y + 30, t, w=190, tam=26, cor=FOSF if k == 0 else OXID, peso=700, serif=True, alinha="right"))
        for j, (lab, cor) in enumerate(sem):
            x = 220 + j * 206
            if cor:
                p.append(f'<rect x="{x}" y="{y}" width="190" height="96" rx="12" fill="{cor}" opacity="{0.55 if k == 0 else 0.9}"/>')
                rs.append(rot(x, y + 34, lab, w=190, tam=21, cor=PAPEL, peso=700, alinha="center"))
            else:
                p.append(f'<rect x="{x}" y="{y}" width="190" height="96" rx="12" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    for k, (ic, t) in enumerate([("t:gauge", "resposta acompanhada; dose ajustada antes de concluir"), ("t:plane", "um mínimo de manutenção combinado para as viagens")]):
        x = k * 844
        p.append(caixa(x, 290, 820, 110, OXID, OXID_T, esp=2, rx=14))
        p.append(icone(ic, x + 24, 322, 44, OXID))
        rs.append(rot(x + 86, 326, t, w=710, tam=22, cor=TINTA, peso=700, lh=1.2))
    return slide("ciclista", 400, p, rs, eyebrow="As perguntas aplicadas", titulo="A semana do ciclista, reorganizada",
                 destaque="Não é melhor por ser mais complexo. É melhor porque cada escolha responde a uma pergunta.", destaque_cor="tinta")

# ---------------------------------------------------------------- 9.2

def pedidos_92():
    """9.2: três fichas, três calendários: um pico em outubro, um sábado atrás do outro, a semana na estrada."""
    p = [svg_abre(1664, 340, "Três fichas na mesma semana. A nadadora master: doze meses e um único campeonato, em outubro. O time de vôlei: oito meses com um jogo todo sábado. O representante comercial que corre: uma semana com três ou quatro dias na estrada e uma meia maratona como meta")]
    rs = []
    W = 528
    fichas = [("t:swimming", "Nadadora master", "um único campeonato, em outubro", AZUL, AZUL_T),
              ("t:ball-volleyball", "Time de vôlei", "um jogo todo sábado, por oito meses", GLIC, GLIC_T),
              ("t:run", "Representante que corre", "meia maratona; metade da semana na estrada", OXID, OXID_T)]
    for k, (ic, t, d, cor, fundo) in enumerate(fichas):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 340, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 22, 44, cor))
        rs += [rot(x + 82, 28, t, w=W - 100, tam=25, cor=cor, peso=700, serif=True), rot(x + 24, 270, d, w=W - 48, tam=20, cor=TINTA, lh=1.25)]
    for m in range(12):
        x = 24 + m * 40
        alvo = m == 9
        p.append(f'<rect x="{x}" y="120" width="32" height="110" rx="6" fill="{AZUL if alvo else CARTAO}" stroke="{AZUL}" stroke-width="2"/>')
    rs.append(rot(24 + 9 * 40 - 40, 90, "out", w=112, tam=18, cor=AZUL, peso=700, alinha="center"))
    x0 = W + 40
    for s in range(32):
        x, y = x0 + 30 + (s % 16) * 30, 130 + (s // 16) * 50
        p.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{GLIC}"/>')
    rs.append(rot(x0 + 24, 90, "32 sábados", w=300, tam=18, cor=GLIC, peso=700))
    x0 = 2 * (W + 40)
    for j, d in enumerate(["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]):
        x = x0 + 24 + j * 68
        estrada = j in (1, 2, 3)
        p.append(f'<rect x="{x}" y="120" width="60" height="110" rx="8" fill="{MUDO if estrada else CARTAO}" stroke="{OXID if not estrada else MUDO}" stroke-width="2" opacity="{0.6 if estrada else 1}"/>')
        if estrada:
            p.append(icone("t:map", x + 12, 158, 36, PAPEL))
    rs.append(rot(x0 + 24, 90, "dias na estrada", w=300, tam=18, cor=MUDO, peso=700))
    return slide("pedidos", 340, p, rs, eyebrow="Três pedidos na mesma semana", titulo="Os três pedem “uma periodização”. Precisam de coisas diferentes.")


def funciona_92():
    """9.2: dezoito estudos e o tamanho de efeito que encolhe com o ajuste para viés de publicação."""
    p = [svg_abre(1664, 320, "À esquerda, dezoito quadrados, um por estudo comparando força periodizada e não periodizada. À direita, duas barras do tamanho de efeito: 0,43 antes e 0,23 depois do ajuste para viés de publicação; ainda favorável, mas pequeno"), defs(MUDO)]
    rs = []
    for i in range(18):
        x, y = (i % 6) * 80, (i // 6) * 80
        p.append(f'<rect x="{x}" y="{y + 20}" width="66" height="66" rx="8" fill="{TINTA}" opacity="0.8"/>')
    rs.append(rot(0, 270, "18 estudos · força periodizada × não periodizada", w=480, tam=20, cor=TINTA, peso=700, lh=1.2))
    X0, E = 760, 1700
    for k, (v, t, cor) in enumerate([(0.43, "antes", GLIC), (0.23, "depois do ajuste para viés de publicação", OXID)]):
        y = 30 + k * 130
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E:.0f}" height="90" rx="8" fill="{cor}"/>')
        rs += [rot(X0 + v * E + 16, y + 18, f"{v:.2f}".replace(".", ","), w=180, tam=44, cor=cor, peso=700, serif=True),
               rot(560, y + 30, t, w=180, tam=19, cor=TINTA, peso=700, alinha="right", lh=1.15)]
    p.append(seta(X0 + 0.43 * E * 0.5, 124, X0 + 0.43 * E * 0.5, 156, MUDO, "m0", esp=3))
    rs.append(rot(X0, 286, "tamanho de efeito · ainda favorável, mas pequeno", w=900, tam=19, cor=MUDO))
    return slide("funciona", 320, p, rs, eyebrow="Periodizar funciona?", titulo="Funciona, por pouco",
                 destaque="Ondulatório um pouco à frente. Ganhos maiores em quem não era treinado: no começo, quase qualquer progressão funciona.", destaque_cor="tinta",
                 fonte="Metanálise, Sports Med 2017")


def igualado_92():
    """9.2: uma matriz de duas comparações por dois desfechos, com setas e sinais de igual."""
    p = [svg_abre(1664, 330, "Uma matriz com o volume igualado. Linhas: periodizado contra não periodizado; ondulatório contra linear. Colunas: força e hipertrofia. Força: periodizado maior; ondulatório maior, sobretudo em treinados. Hipertrofia: igual nas duas comparações")]
    rs = []
    rs += [rot(620, 0, "Força", w=500, tam=26, cor=OXID, peso=700, alinha="center", serif=True), rot(1164, 0, "Hipertrofia", w=500, tam=26, cor=GLIC, peso=700, alinha="center", serif=True)]
    for k, (t, f, h) in enumerate([("Periodizado × não periodizado", "periodizado maior", "igual"), ("Ondulatório × linear", "ondulatório maior, sobretudo em treinados", "igual")]):
        y = 50 + k * 140
        p.append(caixa(0, y, 590, 120, TINTA, CARTAO, esp=2, rx=14))
        rs.append(rot(24, y + 42, t, w=550, tam=24, cor=TINTA, peso=700))
        p.append(caixa(620, y, 500, 120, OXID, OXID_T, esp=2, rx=14))
        p.append(icone("t:trending-up", 640, y + 36, 48, OXID))
        rs.append(rot(706, y + 34 if k == 0 else y + 22, f, w=400, tam=22, cor=TINTA, peso=700, lh=1.25))
        p.append(caixa(1164, y, 500, 120, GLIC, GLIC_T, esp=2, rx=14))
        rs.append(rot(1164, y + 24, "=", w=160, tam=52, cor=GLIC, peso=700, alinha="center"))
        rs.append(rot(1324, y + 42, h, w=320, tam=24, cor=TINTA, peso=700))
    return slide("igualado", 330, p, rs, eyebrow="Com o volume igualado", titulo="Força responde ao modelo; hipertrofia, ao volume",
                 destaque="Para massa muscular, o modelo importa pouco. O que importa é o volume.", destaque_cor="tinta", fonte="Metanálise, Sports Med 2022")


def acontece_92():
    """9.2: dois planos, um simples cumprido em 80% e um sofisticado cumprido em 40%, em esquema."""
    p = [svg_abre(1664, 340, "Em esquema, dois planos como barras. Um plano simples, cumprido em oitenta por cento. Um plano sofisticado, mais comprido, cumprido em quarenta por cento. O simples chega mais longe. Embaixo: a diferença entre modelos é menor que a diferença entre fazer e não fazer as sessões; boa parte dos modelos vem da tradição")]
    rs = []
    X0 = 360
    for k, (t, total, feito, cor) in enumerate([("plano simples", 900, 0.8, OXID), ("plano sofisticado", 1250, 0.4, GLIC)]):
        y = 20 + k * 120
        rs.append(rot(0, y + 26, t, w=330, tam=24, cor=cor, peso=700, alinha="right", serif=True))
        p.append(f'<rect x="{X0}" y="{y}" width="{total}" height="84" rx="10" fill="{CARTAO}" stroke="{cor}" stroke-width="3"{TRACO}/>')
        p.append(f'<rect x="{X0}" y="{y}" width="{total * feito:.0f}" height="84" rx="10" fill="{cor}"/>')
        rs.append(rot(X0 + 20, y + 22, f"{int(feito * 100)}% cumprido", w=400, tam=24, cor=PAPEL, peso=700))
    p.append(f'<line x1="{X0 + 720}" y1="10" x2="{X0 + 720}" y2="240" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(X0 + 732, 116, "chega mais longe", w=300, tam=20, cor=OXID, peso=700))
    p.append(caixa(0, 262, 1664, 78, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(24, 284, "diferença entre modelos < diferença entre fazer e não fazer as sessões · esquema", w=1616, tam=21, cor=PAPEL, peso=700, alinha="center"))
    return slide("acontece", 340, p, rs, eyebrow="A ideia da aula", titulo="O melhor modelo é o que acontece.",
                 destaque="Boa parte dos modelos vem da tradição, e a diferença entre eles é pequena.", destaque_cor="tinta")


def picos_92():
    """9.2: uma curva que sobe até outubro, contra uma serra com um pico a cada sábado, em esquema."""
    p = [svg_abre(1664, 340, "Em esquema, dois painéis. Um pico: a curva da nadadora sobe até o campeonato de outubro, numa sequência linear ou em blocos, e termina com o polimento antes da prova. Um pico por semana: a linha do vôlei sobe e desce a cada sábado, com ondulatório dentro da semana e manutenção de força ao longo da temporada")]
    rs = []
    for k, (t, itens, cor, fundo) in enumerate([("Um pico", ["linear ou em blocos", "polimento antes da prova"], AZUL, AZUL_T),
                                                ("Um pico por semana", ["ondulatório dentro da semana", "manutenção de força na temporada"], GLIC, GLIC_T)]):
        x = k * 844
        p.append(caixa(x, 0, 820, 340, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, 16, t, w=780, tam=27, cor=cor, peso=700, serif=True))
        p.append(f'<line x1="{x + 40}" y1="230" x2="{x + 780}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
        for j, it in enumerate(itens):
            rs.append(rot(x + 40 + j * 380, 262, "· " + it, w=370, tam=20, cor=TINTA, lh=1.2))
    p.append(f'<path d="M 40 220 C 300 210, 560 140, 700 80 L 740 90" fill="none" stroke="{AZUL}" stroke-width="6"/>')
    p.append(f'<circle cx="720" cy="80" r="14" fill="{AZUL}"/>')
    rs.append(rot(660, 40, "outubro", w=140, tam=18, cor=AZUL, peso=700, alinha="center"))
    pts = []
    for s in range(12):
        x = 884 + s * 60
        pts += [f"{x},200", f"{x + 40},110", f"{x + 50},200"]
    p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GLIC}" stroke-width="4" stroke-linejoin="round"/>')
    rs.append(rot(884, 60, "sábado a sábado · esquema", w=600, tam=18, cor=GLIC, peso=700))
    return slide("picos", 340, p, rs, eyebrow="Pergunta um", titulo="Quantos momentos de pico existem?",
                 destaque="Com trinta e poucos picos, não existe caminhar para um momento.", destaque_cor="tinta")


def sessoes_92():
    """9.2: catorze pontos de sessão contra quatro, e a unidade de planejamento que encolhe para a semana."""
    p = [svg_abre(1664, 360, "Duas semanas lado a lado. A literatura clássica: atletas com dez a catorze sessões, catorze pontos. O representante: quatro sessões, que viram duas nas semanas de viagem. À direita, a unidade de planejamento muda: sai o macrociclo, entra a semana que se repete por três a seis semanas"), defs(MUDO)]
    rs = []
    for k, (t, n, extra, cor) in enumerate([("A literatura clássica", 14, "dez a catorze sessões por semana", TINTA), ("O representante", 4, "quatro sessões; duas nas semanas de viagem", GLIC)]):
        y = k * 180
        p.append(caixa(0, y, 860, 160, cor, CARTAO, esp=2, rx=16))
        rs += [rot(24, y + 16, t, w=500, tam=24, cor=cor, peso=700, serif=True), rot(24, y + 118, extra, w=800, tam=19, cor=TINTA)]
        for i in range(n):
            x = 30 + i * 58
            p.append(f'<circle cx="{x + 18}" cy="{y + 84}" r="20" fill="{cor}" opacity="{0.45 if (k == 1 and i >= 2) else 1}"/>')
    p.append(seta(880, 180, 940, 180, MUDO, "m0", esp=3))
    p.append(caixa(956, 0, 708, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(980, 16, "A unidade muda", w=660, tam=26, cor=OXID, peso=700, serif=True))
    p.append(f'<rect x="980" y="74" width="660" height="56" rx="10" fill="{CARTAO}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<line x1="990" y1="102" x2="1630" y2="102" stroke="{FOSF}" stroke-width="4"/>')
    rs.append(rot(980, 88, "macrociclo", w=660, tam=20, cor=MUDO, peso=700, alinha="center"))
    for s in range(6):
        x = 980 + s * 112
        p.append(f'<rect x="{x}" y="160" width="100" height="90" rx="10" fill="{OXID}" opacity="{0.6 + s * 0.07:.2f}"/>')
    rs += [rot(980, 274, "a mesma semana, de três a seis vezes", w=660, tam=20, cor=OXID, peso=700),
           rot(980, 312, "progressão pequena, revisada e ajustada", w=660, tam=20, cor=TINTA)]
    return slide("sessoes", 360, p, rs, eyebrow="Pergunta dois", titulo="Quantas sessões acontecem de verdade?",
                 destaque="Cada sessão precisa se justificar numa frase. Sem a frase, é enfeite.", destaque_cor="tinta")


def objetivo_92():
    """9.2: quatro perfis com o que decide o plano de cada um."""
    p = [svg_abre(1664, 340, "Quatro linhas, perfil e o que decide. Iniciante: qualquer progressão bem feita; aprender e aparecer. Treinado buscando força: variar a intensidade ao longo da semana. Hipertrofia: o volume; o modelo fica em segundo plano. Endurance: a distribuição de intensidade na semana"), defs(MUDO)]
    rs = []
    for k, (ic, t, d, cor, fundo) in enumerate([("t:school", "Iniciante", "qualquer progressão bem feita; aprender e aparecer", OXID, OXID_T),
                                                ("t:barbell", "Treinado buscando força", "variar a intensidade ao longo da semana", AZUL, AZUL_T),
                                                ("t:stairs", "Hipertrofia", "o volume; o modelo fica em segundo plano", GLIC, GLIC_T),
                                                ("t:run", "Endurance", "a distribuição de intensidade na semana", FOSF, FOSF_T)]):
        y = k * 86
        p.append(caixa(0, y, 520, 72, cor, fundo, esp=2, rx=12))
        p.append(icone(ic, 18, y + 15, 42, cor))
        rs.append(rot(76, y + 20, t, w=430, tam=24, cor=cor, peso=700, serif=True))
        p.append(seta(532, y + 36, 594, y + 36, MUDO, "m0", esp=3))
        p.append(caixa(608, y, 1056, 72, BORDA, CARTAO, esp=2, rx=12))
        rs.append(rot(632, y + 22, d, w=1010, tam=23, cor=TINTA, peso=700))
    return slide("objetivo", 340, p, rs, eyebrow="Pergunta três", titulo="Qual o objetivo, e há quanto tempo treina?")


def minima_92():
    """9.2: uma folha na geladeira com a semana cheia e a semana mínima, e a regra escrita embaixo."""
    p = [svg_abre(1664, 380, "Uma folha presa por um ímã, com duas colunas. Semana cheia: quatro sessões, progressão pequena, revisão a cada três a seis semanas. Semana mínima: duas sessões, começando pelo mais difícil de recuperar, a força. Embaixo, a regra escrita: semana mínima não conta como falha e não exige recomeço")]
    rs = []
    p.append(f'<rect x="0" y="10" width="1664" height="370" rx="10" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<circle cx="832" cy="14" r="16" fill="{FOSF}"/>')
    for k, (t, sess, d, cor) in enumerate([("Semana cheia", ["força", "sessão", "sessão", "sessão"], "progressão pequena · revisão a cada três a seis semanas", OXID),
                                           ("Semana mínima", ["força", "sessão"], "começa pelo mais difícil de recuperar: a força", GLIC)]):
        x = 40 + k * 812
        rs.append(rot(x, 40, t, w=760, tam=27, cor=cor, peso=700, serif=True))
        for j, s in enumerate(sess):
            p.append(f'<rect x="{x + j * 186}" y="96" width="170" height="90" rx="12" fill="{cor}" opacity="{1 if s == "força" else 0.6}"/>')
            rs.append(rot(x + j * 186, 128, s, w=170, tam=21, cor=PAPEL, peso=700, alinha="center"))
        rs.append(rot(x, 206, d, w=760, tam=20, cor=TINTA, lh=1.25))
    p.append(f'<line x1="832" y1="40" x2="832" y2="250" stroke="{BORDA}" stroke-width="2"/>')
    p.append(caixa(40, 274, 1584, 80, TINTA, TINTA, esp=0, rx=12))
    rs.append(rot(64, 296, "semana mínima não conta como falha e não exige recomeço", w=1536, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("minima", 380, p, rs, eyebrow="O detalhe que salva o plano", titulo="Semana cheia e semana mínima, escritas desde o primeiro dia",
                 destaque="Sem versão mínima, a semana ruim tem zero sessões: “não deu para fazer direito” vira “não deu para fazer”.", destaque_cor="tinta")


def aplicado_92():
    """9.2: os três pedidos passando pelas três perguntas até a escolha."""
    p = [svg_abre(1664, 380, "Três linhas, os três pedidos passando pelas três perguntas até a escolha. Nadadora master: um pico, quatro a cinco sessões, desempenho; linear ou blocos até outubro, polimento no fim. Time de vôlei: um pico por semana, muitas sessões, jogo de sábado; ondulatório, sessão pesada longe do jogo, manutenção. Representante: a prova, quatro sessões que viram duas, meia maratona; semana que se repete, cheia e mínima"), defs(MUDO)]
    rs = []
    rs += [rot(300, 0, "picos · sessões · objetivo", w=640, tam=19, cor=MUDO, peso=700, alinha="center"), rot(1010, 0, "escolha", w=654, tam=19, cor=MUDO, peso=700, alinha="center")]
    linhas = [("t:swimming", "Nadadora master", "um · 4 a 5 · desempenho", "linear ou blocos até outubro, polimento no fim", AZUL, AZUL_T),
              ("t:ball-volleyball", "Time de vôlei", "um por semana · muitas · sábado", "ondulatório, sessão pesada longe do jogo, manutenção", GLIC, GLIC_T),
              ("t:run", "Representante", "a prova · 4 que viram 2 · meia", "semana que se repete, cheia e mínima", OXID, OXID_T)]
    for k, (ic, t, perg, esc, cor, fundo) in enumerate(linhas):
        y = 40 + k * 114
        p.append(caixa(0, y, 280, 100, cor, fundo, esp=2, rx=14))
        p.append(icone(ic, 16, y + 28, 44, cor))
        rs.append(rot(70, y + 22, t, w=200, tam=21, cor=cor, peso=700, serif=True, lh=1.15))
        p.append(f'<rect x="300" y="{y + 16}" width="640" height="68" rx="34" fill="{CARTAO}" stroke="{cor}" stroke-width="2"/>')
        rs.append(rot(300, y + 36, perg, w=640, tam=21, cor=TINTA, peso=700, alinha="center"))
        p.append(seta(950, y + 50, 998, y + 50, MUDO, "m0", esp=3))
        p.append(caixa(1010, y, 654, 100, cor, cor, esp=0, rx=14))
        rs.append(rot(1030, y + 22, esc, w=614, tam=21, cor=PAPEL, peso=700, lh=1.25))
    return slide("aplicado", 380, p, rs, eyebrow="As três perguntas aplicadas", titulo="Três pedidos, três escolhas")


def sinais_92():
    """9.2: três sinais, cada um com um pequeno gráfico em esquema."""
    p = [svg_abre(1664, 340, "Três cartões, cada um com um pequeno esquema. As sessões não acontecem: casas de sessão cada vez mais vazias; o plano pede mais do que a vida comporta. A carga não sobe: uma linha reta; falta sobrecarga, não falta modelo. O dia seguinte piora: sono, dor e rendimento caindo; a carga passou da recuperação")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("As sessões não acontecem", "o plano pede mais do que a vida comporta", FOSF, FOSF_T),
                                            ("A carga não sobe", "falta sobrecarga, não falta modelo", GLIC, GLIC_T),
                                            ("O dia seguinte piora", "sono, dor, rendimento: a carga passou da recuperação", FOSF, FOSF_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 340, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 18, t, w=W - 48, tam=25, cor=cor, peso=700, serif=True), rot(x + 24, 262, d, w=W - 48, tam=20, cor=TINTA, lh=1.25)]
    for s in range(4):
        for j in range(4):
            feito = j < 4 - s
            p.append(f'<rect x="{40 + s * 120}" y="{90 + j * 38}" width="100" height="30" rx="6" fill="{FOSF if feito else CARTAO}" stroke="{FOSF}" stroke-width="2" opacity="{0.8 if feito else 1}"/>')
    x0 = W + 40
    p.append(f'<polyline points="{x0 + 40},180 {x0 + 160},178 {x0 + 280},181 {x0 + 400},179 {x0 + 488},180" fill="none" stroke="{GLIC}" stroke-width="6"/>')
    p.append(f'<line x1="{x0 + 40}" y1="230" x2="{x0 + 488}" y2="230" stroke="{MUDO}" stroke-width="2"/>')
    x0 = 2 * (W + 40)
    for j, ic in enumerate(["t:moon", "t:mood-sick", "t:trending-down"]):
        p.append(icone(ic, x0 + 60 + j * 150, 120, 72, FOSF))
    return slide("sinais", 340, p, rs, eyebrow="Quando não está funcionando", titulo="Três sinais, em qualquer modelo",
                 destaque="O terceiro sinal é o assunto das aulas de monitoramento deste módulo.", destaque_cor="tinta")

# ---------------------------------------------------------------- 9.3

def ficha_93():
    """9.3: cinco pessoas em volta da mesma ficha em branco, e o três de dez riscado."""
    p = [svg_abre(1664, 340, "No centro, uma ficha de academia em branco, com as colunas séries e repetições vazias. Em volta, cinco pessoas fazendo a mesma pergunta: o jovem que quer massa, a corredora, o jogador de basquete que quer saltar, a senhora na casa dos setenta que quer levantar da cadeira, e o paciente com diabetes. Ao lado, a resposta padrão três séries de dez, riscada")]
    rs = []
    pessoas = [("h:man", "o jovem que quer massa", AZUL), ("t:run", "a corredora", OXID), ("t:ball-basketball", "o jogador que quer saltar", GLIC),
               ("h:woman", "a senhora na casa dos setenta", FOSF), ("t:droplet", "o paciente com diabetes", TINTA)]
    for k, (ic, t, cor) in enumerate(pessoas):
        y = k * 68
        p.append(f'<circle cx="30" cy="{y + 30}" r="28" fill="{CARTAO}" stroke="{cor}" stroke-width="2"/>')
        p.append(icone(ic, 12, y + 12, 36, cor))
        rs.append(rot(72, y + 18, t, w=420, tam=21, cor=TINTA, peso=700))
    p.append(caixa(560, 0, 560, 340, TINTA, CARTAO, esp=2, rx=12))
    rs += [rot(580, 16, "ficha", w=200, tam=20, cor=MUDO, peso=700), rot(580, 60, "séries", w=250, tam=24, cor=TINTA, peso=700, alinha="center"), rot(850, 60, "repetições", w=250, tam=24, cor=TINTA, peso=700, alinha="center")]
    for j in range(5):
        y = 110 + j * 44
        p.append(f'<line x1="580" y1="{y}" x2="1100" y2="{y}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(f'<line x1="840" y1="56" x2="840" y2="320" stroke="{BORDA}" stroke-width="2"/>')
    p.append(caixa(1180, 90, 484, 160, FOSF, FOSF_T, esp=2, rx=16))
    rs += [rot(1200, 118, "“três séries de dez”", w=444, tam=28, cor=FOSF, peso=700, serif=True, alinha="center"), rot(1200, 180, "resposta pior do que parece", w=444, tam=21, cor=TINTA, alinha="center")]
    p.append(f'<line x1="1210" y1="170" x2="1630" y2="120" stroke="{FOSF}" stroke-width="4"/>')
    return slide("ficha", 340, p, rs, eyebrow="Na academia", titulo="“Quantas séries e quantas repetições?” depende de para quê.")


def roteiro_93():
    """9.3: cinco passos em fila, do objetivo ao registro."""
    p = [svg_abre(1664, 300, "Cinco passos em fila, nesta ordem. Um, objetivo: força máxima, hipertrofia, potência, saúde e função, ou outro esporte. Dois, carga: a variável que mais separa força de hipertrofia. Três, volume e frequência: quantas séries por músculo, distribuídas como. Quatro, esforço e intervalo: quanto perto da falha, quanto descanso entre séries. Cinco, progressão e registro: sem ficha, não existe progressão"), defs(MUDO)]
    rs = []
    W = 300
    for k, (ic, t, d, cor, fundo) in enumerate([("t:target", "Objetivo", "força máxima, hipertrofia, potência, saúde e função, ou outro esporte", TINTA, PAPEL),
                                                ("t:barbell", "Carga", "a variável que mais separa força de hipertrofia", FOSF, FOSF_T),
                                                ("t:calendar", "Volume e frequência", "quantas séries por músculo, distribuídas como", GLIC, GLIC_T),
                                                ("t:gauge", "Esforço e intervalo", "quanto perto da falha; quanto descanso entre séries", OXID, OXID_T),
                                                ("t:notebook", "Progressão e registro", "sem ficha, não existe progressão", TINTA, PAPEL)]):
        x = k * (W + 41)
        p.append(caixa(x, 0, W, 300, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="{x + 40}" cy="44" r="24" fill="{cor}"/>')
        rs.append(rot(x + 16, 30, str(k + 1), w=48, tam=24, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(icone(ic, x + W - 64, 22, 44, cor))
        rs += [rot(x + 20, 96, t, w=W - 40, tam=24, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 20, 170, d, w=W - 40, tam=20, cor=TINTA, lh=1.3)]
        if k < 4:
            p.append(seta(x + W + 4, 150, x + W + 36, 150, MUDO, "m0", esp=3))
    return slide("roteiro", 300, p, rs, eyebrow="O roteiro", titulo="Cinco passos, nesta ordem")


def objetivo_93():
    """9.3: cinco objetivos e a variável que manda em cada um, com a faixa do objetivo dito em voz alta."""
    p = [svg_abre(1664, 470, "Cinco linhas, objetivo e o que mais pesa. Força máxima: carga pesada, no próprio exercício que se quer melhorar. Hipertrofia: volume e esforço perto da falha; a carga pode variar. Potência: velocidade de execução, sobre uma base de força. Saúde e função: regularidade, com exercícios que conversam com a vida real. Outro esporte: o que o esporte exige e falta, sem roubar o treino principal. Embaixo: nomear o objetivo com a pessoa evita o programa de fisiculturista para quem queria correr melhor"), defs(MUDO)]
    rs = []
    for k, (ic, t, d, cor, fundo) in enumerate([("t:barbell", "Força máxima", "carga pesada, no próprio exercício que se quer melhorar", FOSF, FOSF_T),
                                                ("t:stairs", "Hipertrofia", "volume e esforço perto da falha; a carga pode variar", GLIC, GLIC_T),
                                                ("t:bolt", "Potência", "velocidade de execução, sobre uma base de força", AZUL, AZUL_T),
                                                ("t:heart-handshake", "Saúde e função", "regularidade, com exercícios que conversam com a vida real", OXID, OXID_T),
                                                ("t:run", "Outro esporte", "o que o esporte exige e falta, sem roubar o treino principal", TINTA, PAPEL)]):
        y = k * 76
        p.append(caixa(0, y, 440, 64, cor, fundo, esp=2, rx=12))
        p.append(icone(ic, 16, y + 12, 40, cor))
        rs.append(rot(70, y + 16, t, w=360, tam=24, cor=cor, peso=700, serif=True))
        p.append(seta(452, y + 32, 512, y + 32, MUDO, "m0", esp=3))
        p.append(caixa(526, y, 1138, 64, BORDA, CARTAO, esp=2, rx=12))
        rs.append(rot(548, y + 18, d, w=1100, tam=22, cor=TINTA, peso=700))
    p.append(caixa(0, 394, 1664, 76, TINTA, TINTA, esp=0, rx=14))
    p.append(icone("t:message-circle", 24, 410, 44, PAPEL))
    rs.append(rot(84, 414, "nomear o objetivo com a pessoa evita o programa de fisiculturista para quem queria correr melhor", w=1560, tam=22, cor=PAPEL, peso=700))
    return slide("objetivo", 470, p, rs, eyebrow="Passo um", titulo="Cada objetivo tem uma variável que manda")


def carga_93():
    """9.3: dois painéis de barras em esquema: hipertrofia igual nas duas cargas, força maior com carga pesada."""
    p = [svg_abre(1664, 340, "Dois painéis em esquema, sem valores. Hipertrofia: duas barras iguais, carga baixa até 60% do máximo e carga alta acima disso; ganhos semelhantes, desde que as séries sejam levadas ao esforço alto; saída para quem não tolera carga pesada. Força máxima: a barra da carga alta é maior; quem quer ficar forte num levantamento precisa treinar pesado nele em algum momento")]
    rs = []
    B = 250
    for k, (t, hs, nota, cor, fundo) in enumerate([("Hipertrofia", (150, 150), "semelhante, com esforço alto · saída para quem não tolera carga pesada", OXID, OXID_T),
                                                   ("Força máxima", (90, 170), "carga pesada ganhou · treinar pesado no próprio levantamento", FOSF, FOSF_T)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 340, cor, fundo, esp=2, rx=16))
        rs.append(rot(x0 + 24, 16, t, w=500, tam=27, cor=cor, peso=700, serif=True))
        for j, (h, lab) in enumerate(zip(hs, ["carga baixa (≤ 60%)", "carga alta"])):
            x = x0 + 80 + j * 280
            p.append(f'<rect x="{x}" y="{B - h}" width="200" height="{h}" rx="8" fill="{cor}" opacity="{0.6 if j == 0 else 1}"/>')
            rs.append(rot(x - 20, B + 8, lab, w=240, tam=18, cor=TINTA, peso=700, alinha="center"))
        p.append(f'<line x1="{x0 + 40}" y1="{B}" x2="{x0 + 620}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(x0 + 24, 290, nota, w=780, tam=19, cor=TINTA, lh=1.2))
        rs.append(rot(x0 + 640, 120, "=" if k == 0 else "↑", w=140, tam=56, cor=cor, peso=700, alinha="center"))
    rs.append(rot(1440, 16, "esquema", w=200, tam=16, cor=MUDO, alinha="right"))
    return slide("carga", 340, p, rs, eyebrow="Passo dois · carga", titulo="Hipertrofia em toda a faixa; força com carga pesada",
                 destaque="Séries até a falha, pelo menos seis semanas.", destaque_cor="tinta", fonte="Metanálise, J Strength Cond Res 2017")


def crescer_93():
    """9.3: duas metades: crescer com qualquer carga e esforço alto; ficar forte com carga pesada."""
    p = [svg_abre(1664, 320, "Duas metades. Para crescer: uma régua de carga de leve a pesada, toda ela marcada como serve, e um mostrador de esforço no alto. Para ficar forte: a mesma régua, só a ponta pesada marcada. Embaixo: as duas metades resolvem boa parte das discussões de academia e das prescrições para quem tem limitação")]
    rs = []
    for k, (t, ini, cor, fundo, extra) in enumerate([("Para crescer", 0.0, OXID, OXID_T, "quase qualquer carga, se o esforço for alto"), ("Para ficar forte", 0.7, FOSF, FOSF_T, "precisa de carga pesada")]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 240, cor, fundo, esp=2, rx=16))
        rs += [rot(x0 + 24, 18, t, w=760, tam=28, cor=cor, peso=700, serif=True), rot(x0 + 24, 190, extra, w=760, tam=22, cor=TINTA, peso=700)]
        p.append(f'<rect x="{x0 + 40}" y="110" width="560" height="34" rx="17" fill="{CINZA}" opacity="0.5"/>')
        p.append(f'<rect x="{x0 + 40 + 560 * ini:.0f}" y="110" width="{560 * (1 - ini):.0f}" height="34" rx="17" fill="{cor}"/>')
        rs += [rot(x0 + 40, 76, "leve", w=200, tam=18, cor=MUDO), rot(x0 + 400, 76, "pesada", w=200, tam=18, cor=MUDO, alinha="right")]
        p.append(icone("t:gauge" if k == 0 else "t:barbell", x0 + 660, 80, 90, cor))
    p.append(caixa(0, 260, 1664, 60, TINTA, TINTA, esp=0, rx=12))
    rs.append(rot(24, 276, "as duas metades resolvem boa parte das discussões de academia e das prescrições para quem tem limitação", w=1616, tam=20, cor=PAPEL, peso=700, alinha="center"))
    return slide("crescer", 320, p, rs, eyebrow="A ideia da aula", titulo="Para crescer, quase qualquer carga serve se o esforço for alto. Para ficar forte, precisa de carga pesada.")


def frequencia_93():
    """9.3: o mesmo volume semanal em uma, duas ou três sessões, e o mesmo ganho ao lado."""
    p = [svg_abre(1664, 340, "O mesmo volume semanal, nove séries, distribuído em uma, duas ou três sessões; ao lado de cada linha, um sinal de igual: resultado semelhante para a hipertrofia. À direita, para que serve a frequência: logística, distribuir o volume em sessões que a pessoa faz bem; com três dias, corpo inteiro; com cinco, dividir")]
    rs = []
    for k, sess in enumerate([[9], [5, 4], [3, 3, 3]]):
        y = 20 + k * 100
        rs.append(rot(0, y + 22, f"{len(sess)}× por semana", w=180, tam=20, cor=TINTA, peso=700, alinha="right"))
        x = 210
        for n in sess:
            for i in range(n):
                p.append(f'<rect x="{x + i * 34}" y="{y}" width="28" height="70" rx="5" fill="{GLIC}"/>')
            x += n * 34 + 40
        rs.append(rot(620, y + 8, "=", w=80, tam=44, cor=GLIC, peso=700, alinha="center"))
    rs.append(rot(210, 310, "mesmo volume semanal · resultado semelhante para hipertrofia", w=600, tam=18, cor=MUDO))
    p.append(caixa(760, 0, 904, 340, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(784, 18, "Para que serve, então: logística", w=860, tam=26, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:calendar", "distribuir o volume em sessões que a pessoa faz bem"), ("t:users", "três dias: corpo inteiro nos três"), ("t:list-check", "cinco dias: dá para dividir")]):
        y = 84 + j * 80
        p.append(icone(ic, 784, y, 44, OXID))
        rs.append(rot(846, y + 8, t, w=800, tam=22, cor=TINTA, peso=700 if j == 0 else 400))
    return slide("frequencia", 340, p, rs, eyebrow="Passo três · frequência", titulo="Com o mesmo volume, a frequência não muda a hipertrofia",
                 destaque="A frequência distribui o volume; não o substitui. A vantagem antiga vinha do volume maior.", destaque_cor="tinta",
                 fonte="Metanálise, J Sports Sci 2019")


def esforco_93():
    """9.3: proximidade da falha e intervalo entre séries, cada um com o seu pequeno gráfico em esquema."""
    p = [svg_abre(1664, 360, "Dois painéis em esquema. Perto da falha: conforme as repetições de reserva diminuem, a hipertrofia sobe; a linha da força fica quase plana, relação desprezível. Intervalo entre séries: o benefício para hipertrofia sobe um pouco acima de 60 segundos e achata depois de 90")]
    rs = []
    for k, (t, cor, fundo) in enumerate([("Perto da falha", FOSF, FOSF_T), ("Intervalo entre séries", GLIC, GLIC_T)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 360, cor, fundo, esp=2, rx=16))
        rs.append(rot(x0 + 24, 16, t, w=760, tam=27, cor=cor, peso=700, serif=True))
        p.append(f'<line x1="{x0 + 60}" y1="290" x2="{x0 + 780}" y2="290" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M 60 260 C 300 240, 560 160, 760 100" fill="none" stroke="{FOSF}" stroke-width="6"/>')
    p.append(f'<path d="M 60 200 L 760 190" fill="none" stroke="{AZUL}" stroke-width="5"{TRACO}/>')
    rs += [rot(560, 70, "hipertrofia", w=200, tam=20, cor=FOSF, peso=700), rot(560, 206, "força: relação desprezível", w=240, tam=18, cor=AZUL, peso=700, lh=1.15),
           rot(60, 300, "mais reserva", w=200, tam=18, cor=MUDO), rot(560, 300, "perto da falha", w=200, tam=18, cor=MUDO, alinha="right")]
    x0 = 844
    p.append(f'<path d="M {x0 + 60} 250 C {x0 + 200} 230, {x0 + 300} 150, {x0 + 420} 130 L {x0 + 780} 126" fill="none" stroke="{GLIC}" stroke-width="6"/>')
    for s, lab in [(60, "60 s"), (90, "90 s")]:
        x = x0 + 60 + s * 3.4
        p.append(f'<line x1="{x:.0f}" y1="100" x2="{x:.0f}" y2="290" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
        rs.append(rot(x - 50, 300, lab, w=100, tam=18, cor=TINTA, peso=700, alinha="center"))
    rs += [rot(x0 + 440, 80, "sem diferença apreciável acima de 90 s", w=360, tam=18, cor=GLIC, peso=700, lh=1.2), rot(x0 + 60, 326, "esquema", w=200, tam=16, cor=MUDO)]
    return slide("esforco", 360, p, rs, eyebrow="Passo quatro", titulo="Esforço e intervalo",
                 destaque="Esforço se mede em repetições de reserva: quantas ainda sobrariam. Para força máxima, intervalos mais longos.", destaque_cor="tinta",
                 fonte="Metarregressões, Sports Med 2024 · metanálise, Front Sports Act Living 2024")


def ajustes_93():
    """9.3: a pirâmide da potência sobre a base de força, e a dose para o idoso."""
    p = [svg_abre(1664, 360, "À esquerda, uma pirâmide da potência: na base, a força, porque quem é mais forte produz mais potência; acima, cargas leves a moderadas na maior velocidade; no topo, saltos e arremessos. À direita, o idoso: duas a três sessões por semana; duas a três séries, e no início uma série única basta; incluir potência, com segurança, porque é ela que tira alguém da cadeira")]
    rs = []
    camadas = [(0, 300, 760, "base: força", AZUL), (100, 210, 560, "cargas leves a moderadas na maior velocidade", GLIC), (220, 120, 320, "saltos e arremessos", FOSF)]
    for dx, y, w, t, cor in camadas:
        p.append(f'<rect x="{dx}" y="{y - 80}" width="{w}" height="80" rx="10" fill="{cor}"/>')
        rs.append(rot(dx + 10, y - 58, t, w=w - 20, tam=21, cor=PAPEL, peso=700, alinha="center", lh=1.15))
    rs.append(rot(0, 320, "quem é mais forte produz mais potência", w=760, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(caixa(840, 0, 824, 360, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("h:woman", 864, 22, 56, OXID))
    rs.append(rot(934, 30, "Idoso", w=700, tam=28, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:calendar", "duas a três sessões por semana"), ("t:list-check", "duas a três séries; no início, série única basta"), ("t:bolt", "incluir potência, com segurança: é ela que tira alguém da cadeira")]):
        y = 104 + j * 82
        p.append(icone(ic, 864, y, 44, OXID))
        rs.append(rot(926, y + 4, t, w=710, tam=22, cor=TINTA, peso=700 if j == 2 else 400, lh=1.25))
    return slide("ajustes", 360, p, rs, eyebrow="Dois objetivos com ajustes próprios", titulo="Potência e o idoso",
                 destaque="O jogador que só salta e nunca fica mais forte bate num teto.", destaque_cor="tinta",
                 fonte="Revisão de potência, Sports Med 2011 · posicionamento para idosos, J Strength Cond Res 2019")


def servico_93():
    """9.3: a semana da corredora com força longe da qualidade, e o treino mínimo de três movimentos."""
    p = [svg_abre(1664, 360, "À esquerda, a semana de uma corredora: dois treinos de qualidade e, longe deles, duas sessões curtas de força pesada ou explosiva, poucas séries e poucos exercícios; melhora a economia. À direita, o treino mínimo para quem tem pouco tempo: três movimentos multiarticulares, membros inferiores, empurrar e puxar, duas vezes por semana")]
    rs = []
    p.append(caixa(0, 0, 820, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "Atleta de resistência", w=760, tam=26, cor=OXID, peso=700, serif=True))
    sem = [("qualidade", FOSF), ("força", TINTA), ("leve", OXID), ("qualidade", FOSF), ("leve", OXID), ("força", TINTA), ("longo", AZUL)]
    for j, (t, cor) in enumerate(sem):
        x = 24 + j * 110
        p.append(f'<rect x="{x}" y="80" width="100" height="110" rx="10" fill="{cor}" opacity="{1 if t in ("força", "qualidade") else 0.55}"/>')
        rs.append(rot(x, 122, t, w=100, tam=16 if t == "qualidade" else 18, cor=PAPEL, peso=700, alinha="center"))
    rs += [rot(24, 210, "força pesada ou explosiva melhora a economia", w=780, tam=21, cor=TINTA, peso=700),
           rot(24, 250, "poucas séries, poucos exercícios, longe dos treinos de qualidade", w=780, tam=20, cor=TINTA, lh=1.25),
           rot(24, 320, "dias ilustrativos", w=400, tam=16, cor=MUDO)]
    p.append(caixa(844, 0, 820, 360, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(868, 16, "Quem tem pouco tempo", w=760, tam=26, cor=GLIC, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:stairs", "membros inferiores"), ("t:arrow-down-right", "empurrar"), ("t:arrows-exchange", "puxar")]):
        x = 868 + j * 256
        p.append(f'<rect x="{x}" y="80" width="240" height="120" rx="12" fill="{CARTAO}" stroke="{GLIC}" stroke-width="2"/>')
        p.append(icone(ic, x + 98, 96, 44, GLIC))
        rs.append(rot(x, 154, t, w=240, tam=20, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(868, 226, "multiarticulares · duas vezes por semana cabe na vida", w=780, tam=21, cor=TINTA, peso=700, lh=1.25))
    return slide("servico", 360, p, rs, eyebrow="Força a serviço de outro objetivo", titulo="A corredora e o treino mínimo",
                 destaque="O treino mínimo que acontece vence o completo que nunca acontece.", destaque_cor="tinta",
                 fonte="Revisão, Scand J Med Sci Sports 2014 · revisão, Sports Med 2021")


def registro_93():
    """9.3: a ficha de cinco colunas e a regra da reserva que decide a próxima carga."""
    p = [svg_abre(1664, 380, "Uma ficha com cinco colunas: data, exercício, carga, repetições e reserva, cada uma com a sua função: a frequência real, o mesmo exercício por semanas, a carga que se quer ver subir, o que foi feito e não o previsto, e quantas repetições ainda sobrariam. Embaixo, a regra: terminou com mais reserva que o combinado, a carga sobe; com menos, a carga fica")]
    rs = []
    cols = [("Data", "frequência real e semanas sem treino"), ("Exercício", "o mesmo por semanas"), ("Carga", "a variável que se quer ver subir"),
            ("Repetições", "o que foi feito, não o previsto"), ("Reserva", "quantas ainda sobrariam; decide a próxima carga")]
    W = 320
    for k, (t, d) in enumerate(cols):
        x = k * (W + 16)
        cor = FOSF if k == 4 else TINTA
        p.append(caixa(x, 0, W, 210, cor, CARTAO, esp=3 if k == 4 else 2, rx=12))
        p.append(f'<line x1="{x + 16}" y1="64" x2="{x + W - 16}" y2="64" stroke="{BORDA}" stroke-width="2"/>')
        rs += [rot(x + 16, 20, t, w=W - 32, tam=25, cor=cor, peso=700, serif=True, alinha="center"), rot(x + 16, 84, d, w=W - 32, tam=20, cor=TINTA, lh=1.3, alinha="center")]
    for k, (ic, t, d, cor, fundo) in enumerate([("t:trending-up", "mais reserva que o combinado", "a carga sobe", OXID, OXID_T), ("t:hand-stop", "menos reserva que o combinado", "a carga fica", GLIC, GLIC_T)]):
        x = k * 844
        p.append(caixa(x, 240, 820, 140, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 286, 48, cor))
        rs += [rot(x + 92, 266, t, w=700, tam=22, cor=TINTA, peso=700), rot(x + 92, 306, d, w=700, tam=30, cor=cor, peso=700, serif=True)]
    return slide("registro", 380, p, rs, eyebrow="Passo cinco", titulo="A ficha que transforma progressão em número")

# ---------------------------------------------------------------- aplicação

LICOES = {"09-01": [percurso_91, roteiro_91, especificidade_91, dose_91, variacao_91, reversibilidade_91, teoria_91, perguntas_91, ciclista_91],
          "09-02": [pedidos_92, funciona_92, igualado_92, acontece_92, picos_92, sessoes_92, objetivo_92, minima_92, aplicado_92, sinais_92],
          "09-03": [ficha_93, roteiro_93, objetivo_93, carga_93, crescer_93, frequencia_93, esforco_93, ajustes_93, servico_93, registro_93]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
