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

# ---------------------------------------------------------------- aplicação

LICOES = {"09-01": [percurso_91, roteiro_91, especificidade_91, dose_91, variacao_91, reversibilidade_91, teoria_91, perguntas_91, ciclista_91]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
