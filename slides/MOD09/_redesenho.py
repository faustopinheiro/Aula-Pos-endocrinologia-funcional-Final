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

# ---------------------------------------------------------------- 9.4

def lance_94():
    """9.4: o arranque reto antes do gol e uma semana de treino quase sem velocidade máxima, em esquema."""
    p = [svg_abre(1664, 340, "À esquerda, meio campo visto de cima: o rastro de um atacante em linha reta até a pequena área, dois ou três segundos antes do chute. À direita, em esquema, a semana de treino em barras: muita corrida contínua, circuitos e força; uma fatia mínima de correr o mais rápido possível")]
    rs = []
    p.append(f'<rect x="0" y="0" width="640" height="340" rx="12" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<rect x="200" y="0" width="240" height="90" fill="none" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<rect x="270" y="0" width="100" height="36" fill="none" stroke="{OXID}" stroke-width="3"/>')
    p.append(f'<path d="M 0 340 A 120 120 0 0 1 0 340" fill="none"/>')
    p.append(f'<line x1="320" y1="300" x2="320" y2="70" stroke="{FOSF}" stroke-width="6" stroke-dasharray="14 10"/>')
    p.append(f'<circle cx="320" cy="300" r="14" fill="{FOSF}"/>')
    p.append(f'<path d="M 306 82 L 320 58 L 334 82 Z" fill="{FOSF}"/>')
    rs += [rot(350, 180, "2 a 3 segundos, em linha reta", w=260, tam=21, cor=FOSF, peso=700, lh=1.2)]
    B = 280
    barras = [("corrida contínua", 200, AZUL), ("circuitos", 160, GLIC), ("força", 140, TINTA), ("velocidade máxima", 18, FOSF)]
    for k, (t, h, cor) in enumerate(barras):
        x = 720 + k * 230
        p.append(f'<rect x="{x}" y="{B - h}" width="180" height="{h}" rx="8" fill="{cor}"/>')
        rs.append(rot(x - 20, B + 10, t, w=220, tam=19, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="700" y1="{B}" x2="1660" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(720, 0, "a semana de treino · esquema", w=600, tam=19, cor=MUDO, peso=700), rot(1410, 200, "quase nada", w=180, tam=19, cor=FOSF, peso=700, alinha="center")]
    return slide("lance", 340, p, rs, eyebrow="Antes do gol", titulo="Dois ou três segundos que raramente aparecem no treino da semana.")


def gols_94():
    """9.4: trezentos e sessenta pontos, um por gol, com 161 marcados pelo sprint reto de quem marcou."""
    p = [svg_abre(1664, 300, "Trezentos e sessenta pontos, um por gol da primeira divisão alemã analisado em vídeo. Cento e sessenta e um estão marcados: gols com sprint em linha reta do jogador que marcou, 45% do total, a ação mais frequente antes do gol")]
    rs = []
    for i in range(360):
        x, y = (i % 36) * 30, (i // 36) * 28
        p.append(f'<circle cx="{x + 12}" cy="{y + 14}" r="10" fill="{FOSF if i < 161 else CINZA}" opacity="{1 if i < 161 else 0.6}"/>')
    p.append(caixa(1124, 0, 540, 280, FOSF, FOSF, esp=0, rx=16))
    rs += [rot(1124, 24, "45%", w=540, tam=72, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(1148, 130, "161 de 360 gols com sprint em linha reta de quem marcou", w=492, tam=22, cor=PAPEL, peso=700, alinha="center", lh=1.25)]
    return slide("gols", 300, p, rs, eyebrow="O primeiro número", titulo="A ação mais frequente antes do gol",
                 destaque="Em 83% dos gols, quem marcou ou quem passou fez pelo menos uma ação de potência antes do lance.", destaque_cor="tinta",
                 fonte="J Sports Sci 2012")


def tres_94():
    """9.4: três cartões, cada um com o traçado da sua qualidade."""
    p = [svg_abre(1664, 360, "Três cartões, cada um com um pequeno traçado. Aceleração: a velocidade subindo nos primeiros metros; empurrar o chão para trás com força. Velocidade máxima: o platô depois da aceleração; força rápida num contato curto. Mudança de direção: um caminho que freia, muda e sai; força excêntrica, técnica e decisão")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("Aceleração", "ganhar velocidade nos primeiros metros; empurrar o chão para trás com força", FOSF, FOSF_T),
                                            ("Velocidade máxima", "o pico, depois da aceleração; força rápida num contato curto", GLIC, GLIC_T),
                                            ("Mudança de direção", "frear, mudar e sair; força excêntrica, técnica e decisão", OXID, OXID_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 360, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 18, t, w=W - 48, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 260, d, w=W - 48, tam=20, cor=TINTA, lh=1.3)]
        p.append(f'<line x1="{x + 40}" y1="220" x2="{x + W - 40}" y2="220" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M 40 215 C 120 120, 200 100, 300 92" fill="none" stroke="{FOSF}" stroke-width="6"/>')
    p.append(f'<path d="M 300 92 L 488 90" fill="none" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    x0 = W + 40
    p.append(f'<path d="M {x0 + 40} 215 C {x0 + 120} 130, {x0 + 200} 92, {x0 + 260} 86" fill="none" stroke="{GLIC}" stroke-width="3"{TRACO}/>')
    p.append(f'<path d="M {x0 + 260} 86 L {x0 + 488} 84" fill="none" stroke="{GLIC}" stroke-width="7"/>')
    x0 = 2 * (W + 40)
    p.append(f'<path d="M {x0 + 50} 200 L {x0 + 200} 90 L {x0 + 330} 200 L {x0 + 470} 90" fill="none" stroke="{OXID}" stroke-width="6" stroke-linejoin="round"/>')
    for cx, cy in [(200, 90), (330, 200)]:
        p.append(f'<circle cx="{x0 + cx}" cy="{cy}" r="12" fill="{OXID}"/>')
    return slide("tres", 360, p, rs, eyebrow="Três qualidades, não uma", titulo="Cada uma se treina e se mede de um jeito",
                 destaque="Uma pessoa pode ser boa numa e ruim em outra.", destaque_cor="tinta")


def agilidade_94():
    """9.4: o circuito de cones com caminho conhecido e o atleta que reage ao adversário."""
    p = [svg_abre(1664, 360, "À esquerda, mudança de direção pré-planejada: um circuito de cones em que o atleta sabe o caminho; treina a parte física. À direita, agilidade: o atleta diante de um adversário, com duas setas possíveis e uma interrogação; a mudança de velocidade ou direção acontece em resposta a um estímulo, adversário, bola ou sinal; entra a percepção e a decisão")]
    rs = []
    p.append(caixa(0, 0, 800, 360, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "Mudança de direção pré-planejada", w=760, tam=24, cor=TINTA, peso=700, serif=True))
    pts = [(80, 260), (240, 120), (400, 260), (560, 120), (720, 260)]
    p.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{TINTA}" stroke-width="4" stroke-dasharray="12 8"/>')
    for x, y in pts[1:-1]:
        p.append(f'<path d="M {x - 16} {y + 20} L {x} {y - 14} L {x + 16} {y + 20} Z" fill="{GLIC}"/>')
    rs.append(rot(24, 306, "circuito de cones · o atleta sabe o caminho · treina a parte física", w=760, tam=19, cor=TINTA))
    p.append(caixa(864, 0, 800, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(888, 16, "Agilidade", w=760, tam=24, cor=OXID, peso=700, serif=True))
    p.append(icone("h:running", 980, 150, 90, OXID))
    p.append(icone("h:man", 1380, 120, 110, FOSF))
    p.append(f'<path d="M 1090 170 Q 1200 90 1300 110" fill="none" stroke="{OXID}" stroke-width="4" stroke-dasharray="10 8"/>')
    p.append(f'<path d="M 1090 220 Q 1200 300 1300 260" fill="none" stroke="{OXID}" stroke-width="4" stroke-dasharray="10 8"/>')
    rs += [rot(1150, 166, "?", w=80, tam=44, cor=OXID, peso=700, alinha="center"),
           rot(888, 306, "em resposta a um estímulo: adversário, bola, sinal", w=760, tam=19, cor=TINTA, peso=700)]
    return slide("agilidade", 360, p, rs, eyebrow="Uma definição que muda o treino", titulo="Agilidade exige estímulo",
                 destaque="Só cones deixa de fora a percepção e a decisão, a parte que o jogo cobra.", destaque_cor="tinta", fonte="Revisão, J Sports Sci 2006")


def descansado_94():
    """9.4: sprints com recuperação completa mantêm o tempo; com pausa curta, o tempo cai, em esquema."""
    p = [svg_abre(1664, 340, "Em esquema, duas fileiras de sprints. Com recuperação completa, de minutos, cada barra de velocidade sai igual: treino de velocidade. Com pausa curta, o sistema do esforço máximo e curto não se recompõe e as barras caem uma a uma: vira resistência à velocidade, outro estímulo")]
    rs = []
    for k, (t, d, cor, alturas, gap) in enumerate([("Recuperação completa", "treino de velocidade", OXID, [150] * 6, 220),
                                                   ("Pausa curta", "vira resistência à velocidade", FOSF, [150, 132, 116, 100, 88, 78], 110)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 340, cor, CARTAO, esp=2, rx=16))
        rs += [rot(x0 + 24, 16, t, w=500, tam=25, cor=cor, peso=700, serif=True), rot(x0 + 24, 290, d, w=760, tam=21, cor=TINTA, peso=700)]
        for j, h in enumerate(alturas):
            x = x0 + 40 + j * (gap if k == 0 else 120)
            if x > x0 + 770:
                break
            p.append(f'<rect x="{x}" y="{250 - h}" width="60" height="{h}" rx="6" fill="{cor}"/>')
        rs.append(rot(x0 + 540, 16, "esquema", w=260, tam=16, cor=MUDO, alinha="right"))
    rs.append(rot(40, 64, "minutos entre os sprints", w=400, tam=17, cor=MUDO))
    return slide("descansado", 340, p, rs, eyebrow="A ideia da aula", titulo="Velocidade se treina com velocidade. Correr rápido e cansado é treinar outra coisa.")


def treno_94():
    """9.4: o trenó a 80% da massa corporal, a dose do estudo e os dois tamanhos de efeito."""
    p = [svg_abre(1664, 340, "À esquerda, um corredor puxando um trenó com carga de 80% da massa corporal: dezesseis sessões de dez sprints de vinte metros. À direita, duas barras de tamanho de efeito na força horizontal máxima: 0,80 com o trenó e 0,20 sem carga")]
    rs = []
    p.append(caixa(0, 0, 760, 340, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("h:running", 420, 60, 140, TINTA))
    p.append(f'<line x1="460" y1="150" x2="200" y2="200" stroke="{MUDO}" stroke-width="4"/>')
    p.append(f'<rect x="60" y="170" width="160" height="70" rx="8" fill="{GLIC}"/>')
    p.append(f'<line x1="40" y1="246" x2="720" y2="246" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(60, 190, "80% da massa", w=160, tam=19, cor=PAPEL, peso=700, alinha="center"),
           rot(24, 270, "16 sessões × 10 sprints de 20 m · 16 jogadores amadores", w=720, tam=20, cor=TINTA, peso=700, lh=1.25)]
    X0, E = 980, 700
    for k, (v, t, cor) in enumerate([(0.80, "trenó", FOSF), (0.20, "sem carga", MUDO)]):
        y = 30 + k * 130
        rs.append(rot(800, y + 28, t, w=160, tam=22, cor=TINTA, peso=700, alinha="right"))
        p.append(f'<rect x="{X0}" y="{y}" width="{v * E:.0f}" height="90" rx="8" fill="{cor}"/>')
        rs.append(rot(X0 + v * E + 16, y + 18, f"{v:.2f}".replace(".", ","), w=160, tam=44, cor=cor, peso=700, serif=True))
    rs.append(rot(X0, 290, "tamanho de efeito · força horizontal máxima", w=680, tam=19, cor=MUDO))
    return slide("treno", 340, p, rs, eyebrow="A aceleração", titulo="A força aplicada no chão responde ao treino",
                 destaque="Melhora moderada nos primeiros 5 metros. Estudo pequeno: sprint resistido e sem carga são estímulos diferentes.", destaque_cor="tinta",
                 fonte="Int J Sports Physiol Perform 2017")


def dose_94():
    """9.4: quatro regras, cada uma com um pequeno desenho."""
    p = [svg_abre(1664, 360, "Quatro cartões. Esforço máximo: um mostrador no topo; a oitenta por cento é outro treino. Recuperação completa: tempos iguais, até o primeiro que cai, e ali a série acaba. Poucas repetições: a qualidade some antes do cansaço aparecer. Início da sessão: o sprint logo depois do aquecimento, não no fim de um treino longo")]
    rs = []
    W = 392
    for k, (t, d, cor, fundo) in enumerate([("Esforço máximo", "a oitenta por cento é outro treino", FOSF, FOSF_T), ("Recuperação completa", "se o tempo começa a cair, a série acabou", GLIC, GLIC_T),
                                            ("Poucas repetições", "a qualidade some antes do cansaço aparecer", OXID, OXID_T), ("Início da sessão", "depois do aquecimento, não no fim de um treino longo", TINTA, PAPEL)]):
        x = k * (W + 32)
        p.append(caixa(x, 0, W, 360, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 22, 18, t, w=W - 44, tam=24, cor=cor, peso=700, serif=True), rot(x + 22, 268, d, w=W - 44, tam=20, cor=TINTA, lh=1.3)]
    p.append(icone("t:gauge", 130, 100, 130, FOSF))
    x0 = W + 32
    for j, h in enumerate([110, 110, 108, 84]):
        p.append(f'<rect x="{x0 + 40 + j * 80}" y="{220 - h}" width="56" height="{h}" rx="6" fill="{GLIC if j < 3 else FOSF}"/>')
    p.append(icone("t:hand-stop", x0 + 300, 70, 36, FOSF))
    x0 = 2 * (W + 32)
    for j in range(4):
        p.append(f'<rect x="{x0 + 40 + j * 80}" y="110" width="56" height="110" rx="6" fill="{OXID}"/>')
    x0 = 3 * (W + 32)
    p.append(f'<rect x="{x0 + 30}" y="150" width="332" height="40" rx="20" fill="{CINZA}" opacity="0.6"/>')
    p.append(f'<rect x="{x0 + 30}" y="150" width="80" height="40" rx="20" fill="{AZUL}"/>')
    p.append(f'<rect x="{x0 + 114}" y="150" width="60" height="40" rx="10" fill="{FOSF}"/>')
    rs += [rot(x0 + 22, 110, "aquecimento → sprint → resto", w=W - 44, tam=17, cor=MUDO, peso=700)]
    return slide("dose", 360, p, rs, eyebrow="Como dosar", titulo="Quatro regras para o sprint ser treino de velocidade")


def protege_94():
    """9.4: exposição regular à velocidade máxima ao longo das semanas, contra o tecido que só a encontra no jogo."""
    p = [svg_abre(1664, 360, "Em esquema, duas linhas de semanas. Na de cima, exposição regular: toques semanais na velocidade máxima. Na de baixo, exposição ocasional: a velocidade máxima aparece pela primeira vez no jogo, e é ali que o posterior da coxa a encontra. No estudo observacional do futebol gaélico, mais exposição a esforços em velocidade máxima se associou a menor risco de lesão")]
    rs = []
    for k, (t, picos, cor) in enumerate([("exposição regular", list(range(12)), OXID), ("exposição ocasional", [11], FOSF)]):
        y = 30 + k * 140
        rs.append(rot(0, y + 30, t, w=250, tam=22, cor=cor, peso=700, alinha="right", serif=True))
        p.append(f'<line x1="280" y1="{y + 100}" x2="1660" y2="{y + 100}" stroke="{MUDO}" stroke-width="2"/>')
        for s in range(12):
            x = 300 + s * 112
            h = 90 if s in picos else 30
            p.append(f'<rect x="{x}" y="{y + 100 - h}" width="70" height="{h}" rx="6" fill="{cor if s in picos else CINZA}" opacity="{1 if s in picos else 0.6}"/>')
    rs += [rot(1100, 200, "primeira vez: no jogo", w=410, tam=20, cor=FOSF, peso=700, alinha="right"),
           rot(280, 316, "semanas · altura = velocidade máxima atingida · esquema", w=1000, tam=18, cor=MUDO)]
    return slide("protege", 360, p, rs, eyebrow="Velocidade também protege", titulo="Exposição regular à velocidade máxima",
                 destaque="Estudo observacional, futebol gaélico: mais exposição, menor risco de lesão. Treinar velocidade prepara o tecido para ela.", destaque_cor="tinta",
                 fonte="J Sci Med Sport 2017")


def resumo_94():
    """9.4: três linhas, cada qualidade com como treinar e como medir."""
    p = [svg_abre(1664, 360, "Três linhas. Aceleração: sprints curtos com e sem resistência e força para empurrar o chão; mede-se pelo tempo nos primeiros 10 metros. Velocidade máxima: sprints com aceleração suficiente e recuperação completa; mede-se num trecho lançado ou pela velocidade máxima registrada. Mudança de direção e agilidade: desaceleração, técnica e exercícios com estímulo; mede-se pelo déficit de mudança de direção e por um teste com estímulo"), defs(MUDO)]
    rs = []
    rs += [rot(400, 0, "como treinar", w=700, tam=19, cor=MUDO, peso=700, alinha="center"), rot(1180, 0, "como medir", w=484, tam=19, cor=MUDO, peso=700, alinha="center")]
    for k, (t, tr, me, cor, fundo) in enumerate([("Aceleração", "sprints curtos com e sem resistência; força para empurrar o chão", "tempo nos primeiros 10 m", FOSF, FOSF_T),
                                                 ("Velocidade máxima", "sprints com aceleração suficiente; recuperação completa", "trecho lançado ou velocidade máxima registrada", GLIC, GLIC_T),
                                                 ("Mudança de direção e agilidade", "desaceleração, técnica e exercícios com estímulo", "déficit de mudança de direção; teste com estímulo", OXID, OXID_T)]):
        y = 36 + k * 108
        p.append(caixa(0, y, 370, 92, cor, fundo, esp=2, rx=14))
        rs.append(rot(20, y + 22, t, w=330, tam=23, cor=cor, peso=700, serif=True, lh=1.15))
        p.append(caixa(400, y, 700, 92, BORDA, CARTAO, esp=2, rx=14))
        rs.append(rot(420, y + 22, tr, w=660, tam=21, cor=TINTA, lh=1.25))
        p.append(seta(1110, y + 46, 1166, y + 46, MUDO, "m0", esp=3))
        p.append(caixa(1180, y, 484, 92, cor, CARTAO, esp=2, rx=14))
        p.append(icone("t:stopwatch", 1196, y + 26, 40, cor))
        rs.append(rot(1248, y + 22, me, w=400, tam=21, cor=TINTA, peso=700, lh=1.25))
    return slide("resumo", 360, p, rs, eyebrow="O resumo operacional", titulo="Treinar e medir cada qualidade")

# ---------------------------------------------------------------- 9.5

def planilha_95():
    """9.5: a planilha do relógio com quatro treinos no mesmo ritmo, e o tempo de 10 km parado há dois anos."""
    p = [svg_abre(1664, 340, "À esquerda, a planilha do relógio de uma corredora na faixa dos quarenta anos: quatro treinos na semana, todos com barras de ritmo quase iguais; três com o grupo do bairro, um sozinha no fim de semana, um pouco mais longo. À direita, em esquema, o tempo nos dez quilômetros ao longo de dois anos: uma linha reta")]
    rs = []
    p.append(caixa(0, 0, 900, 340, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "A planilha do relógio · seis anos de corrida", w=860, tam=22, cor=TINTA, peso=700, serif=True))
    for k, (d, grupo, w) in enumerate([("ter", True, 520), ("qui", True, 520), ("sáb", True, 520), ("dom", False, 620)]):
        y = 70 + k * 64
        rs.append(rot(24, y + 12, d, w=60, tam=20, cor=MUDO, peso=700))
        p.append(f'<rect x="100" y="{y}" width="{w}" height="46" rx="8" fill="{GLIC}"/>')
        p.append(icone("t:users" if grupo else "h:person", 740, y + 4, 36, TINTA))
        rs.append(rot(790, y + 12, "grupo" if grupo else "sozinha", w=100, tam=18, cor=TINTA, peso=700))
    rs.append(rot(100, 312, "o mesmo ritmo em todos · dias ilustrativos", w=700, tam=17, cor=MUDO))
    p.append(caixa(960, 0, 704, 340, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(984, 16, "Tempo nos 10 km · esquema", w=660, tam=22, cor=FOSF, peso=700, serif=True))
    p.append(f'<line x1="1000" y1="260" x2="1620" y2="260" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<polyline points="1010,160 1110,164 1210,158 1310,162 1410,159 1510,161 1610,160" fill="none" stroke="{FOSF}" stroke-width="6"/>')
    rs += [rot(1000, 270, "há dois anos", w=200, tam=18, cor=MUDO), rot(1420, 270, "hoje", w=200, tam=18, cor=MUDO, alinha="right"),
           rot(984, 90, "não sai do lugar", w=660, tam=24, cor=FOSF, peso=700)]
    return slide("planilha", 340, p, rs, eyebrow="O caso", titulo="“Cansada, mas nunca morta. Não consigo conversar direito, mas também não estou no limite.”")


def tipos_95():
    """9.5: um esforço contínuo plano e um intervalado em blocos, e as variáveis que ajustam o intervalado."""
    p = [svg_abre(1664, 360, "Em esquema, dois traçados de intensidade ao longo do tempo, com uma linha tracejada do que se sustentaria de forma contínua. Contínuo: uma linha estável, sem pausas, fácil e longa ou moderada e mais curta. Intervalado: blocos acima da linha, com pausas, acumulando mais tempo em intensidade alta. Embaixo, as variáveis do intervalado: intensidade e duração do trecho, intensidade e duração da pausa, repetições e modo")]
    rs = []
    for k, (t, cor, fundo) in enumerate([("Contínuo", OXID, OXID_T), ("Intervalado", FOSF, FOSF_T)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 230, cor, fundo, esp=2, rx=16))
        rs.append(rot(x0 + 24, 14, t, w=400, tam=26, cor=cor, peso=700, serif=True))
        p.append(f'<line x1="{x0 + 30}" y1="120" x2="{x0 + 790}" y2="120" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
        p.append(f'<line x1="{x0 + 30}" y1="200" x2="{x0 + 790}" y2="200" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<rect x="30" y="140" width="760" height="60" rx="6" fill="{OXID}" opacity="0.8"/>')
    rs += [rot(540, 80, "sustentável", w=240, tam=17, cor=TINTA, alinha="right"), rot(40, 152, "esforço estável, sem pausas", w=600, tam=20, cor=PAPEL, peso=700)]
    for j in range(5):
        x = 844 + 40 + j * 150
        p.append(f'<rect x="{x}" y="70" width="100" height="130" rx="6" fill="{FOSF}"/>')
        p.append(f'<rect x="{x + 100}" y="170" width="50" height="30" rx="4" fill="{FOSF}" opacity="0.35"/>')
    for j, t in enumerate(["intensidade do trecho", "duração do trecho", "intensidade da pausa", "duração da pausa", "repetições", "modo"]):
        x = j * 280
        p.append(f'<rect x="{x}" y="256" width="264" height="56" rx="28" fill="{CARTAO}" stroke="{FOSF}" stroke-width="2"/>')
        rs.append(rot(x, 272, t, w=264, tam=18, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(0, 326, "variáveis do intervalado · esquema", w=800, tam=17, cor=MUDO))
    return slide("tipos", 360, p, rs, eyebrow="Contínuo e intervalado", titulo="Dois jeitos de organizar o esforço",
                 destaque="Mudar qualquer variável do intervalado muda o estímulo.", destaque_cor="tinta", fonte="Revisão, Sports Med 2013")


def ambos_95():
    """9.5: duas barras grandes de ganho no consumo máximo, a do intervalado um pouco maior, em esquema."""
    p = [svg_abre(1664, 340, "Em esquema, sem valores, duas barras grandes de ganho no consumo máximo de oxigênio em adultos saudáveis de 18 a 45 anos: contínuo e intervalado; a do intervalado um pouco maior. À direita, a leitura correta: não é intervalado sempre; o intervalado dá mais estímulo cardiorrespiratório em menos tempo; o contínuo fácil entrega outra coisa")]
    rs = []
    B = 270
    for k, (t, h, cor) in enumerate([("contínuo", 190, OXID), ("intervalado", 225, FOSF)]):
        x = 60 + k * 300
        p.append(f'<rect x="{x}" y="{B - h}" width="220" height="{h}" rx="8" fill="{cor}"/>')
        rs.append(rot(x, B + 10, t, w=220, tam=21, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="30" y1="{B}" x2="620" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(30, 0, "ganho no consumo máximo · esquema", w=600, tam=18, cor=MUDO, peso=700), rot(30, 312, "adultos saudáveis, 18 a 45 anos", w=600, tam=18, cor=MUDO)]
    p.append(caixa(700, 0, 964, 340, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(724, 18, "A leitura correta", w=900, tam=26, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:x", "não é “intervalado sempre”"), ("t:clock", "o intervalado dá mais estímulo cardiorrespiratório em menos tempo"), ("t:arrows-exchange", "o contínuo fácil entrega outra coisa")]):
        y = 90 + j * 80
        p.append(icone(ic, 724, y, 44, OXID))
        rs.append(rot(786, y + 4, t, w=850, tam=22, cor=TINTA, peso=700 if j == 1 else 400, lh=1.25))
    return slide("ambos", 340, p, rs, eyebrow="Contínuo ou intervalado?", titulo="Os dois funcionam; o intervalado entrega mais por minuto",
                 destaque="O que o contínuo fácil entrega é o próximo slide.", destaque_cor="tinta", fonte="Metanálise, Sports Med 2015")


def elite_95():
    """9.5: dez casas de sessão, oito fáceis e duas duras, como a semana de um atleta de alto nível."""
    p = [svg_abre(1664, 320, "Uma semana de atleta de endurance de alto nível em casas de sessão, dez a treze por semana; aqui, dez casas: oito fáceis e duas duras, cerca de oitenta por cento em intensidade baixa. À direita, o que o fácil constrói: capilares e mitocôndrias, com pouca fadiga")]
    rs = []
    for i in range(10):
        x = (i % 5) * 150
        y = (i // 5) * 120
        dura = i in (3, 8)
        p.append(f'<rect x="{x}" y="{y}" width="130" height="100" rx="12" fill="{FOSF if dura else OXID}" opacity="{1 if dura else 0.8}"/>')
        rs.append(rot(x, y + 34, "dura" if dura else "fácil", w=130, tam=21, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(0, 256, "dez a treze sessões por semana · cerca de 80% fáceis", w=740, tam=20, cor=TINTA, peso=700))
    p.append(caixa(800, 0, 864, 300, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(824, 18, "O que o fácil constrói", w=820, tam=26, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:droplet", "capilares"), ("t:bolt", "mitocôndrias"), ("t:gauge", "com pouca fadiga: estímulo barato e acumulável")]):
        y = 84 + j * 70
        p.append(icone(ic, 824, y, 44, OXID))
        rs.append(rot(886, y + 8, t, w=760, tam=22, cor=TINTA, peso=700))
    return slide("elite", 320, p, rs, eyebrow="O que fazem os melhores", titulo="A maior parte do tempo no fácil",
                 destaque="Intensificar o treino de quem já é bem treinado não trouxe evidência convincente de ganho no longo prazo.", destaque_cor="tinta",
                 fonte="Int J Sports Physiol Perform 2010")


def ensaio_95():
    """9.5: os quatro modelos do ensaio de 2014, com o polarizado à frente e dois sem melhora significativa."""
    p = [svg_abre(1664, 320, "Quarenta e oito atletas bem treinados, nove semanas, quatro modelos: alto volume, limiar, intervalado de alta intensidade e polarizado. O polarizado teve a maior melhora no consumo de pico de oxigênio, 11,7%. Limiar e alto volume não melhoraram de forma significativa")]
    rs = []
    rs.append(rot(0, 0, "48 atletas bem treinados · 9 semanas · 4 modelos", w=1000, tam=22, cor=TINTA, peso=700, serif=True))
    B, E = 270, 15
    grupos = [("alto volume", None, "sem melhora significativa", MUDO), ("limiar", None, "sem melhora significativa", MUDO),
              ("intervalado alto", None, "não detalhado aqui", GLIC), ("polarizado", 11.7, "+11,7%", OXID)]
    for k, (t, v, lab, cor) in enumerate(grupos):
        x = 40 + k * 300
        if v:
            p.append(f'<rect x="{x}" y="{B - v * E:.0f}" width="220" height="{v * E:.0f}" rx="8" fill="{cor}"/>')
            rs.append(rot(x, B - v * E - 54, lab, w=220, tam=40, cor=cor, peso=700, alinha="center", serif=True))
        elif cor == MUDO:
            p.append(f'<rect x="{x}" y="{B - 8}" width="220" height="8" rx="4" fill="{cor}"/>')
            rs.append(rot(x, B - 70, lab, w=220, tam=18, cor=MUDO, peso=700, alinha="center", lh=1.2))
        else:
            p.append(f'<rect x="{x}" y="{B - 60}" width="220" height="60" rx="8" fill="{CARTAO}" stroke="{cor}" stroke-width="2"{TRACO}/>')
            rs.append(rot(x, B - 44, lab, w=220, tam=17, cor=MUDO, alinha="center"))
        rs.append(rot(x - 10, B + 10, t, w=240, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="20" y1="{B}" x2="1240" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(caixa(1290, 40, 374, 260, GLIC, GLIC_T, esp=2, rx=16))
    rs += [rot(1310, 60, "Para a amadora", w=334, tam=24, cor=GLIC, peso=700, serif=True), rot(1310, 110, "transfere-se a direção, não o número", w=334, tam=22, cor=TINTA, peso=700, lh=1.3)]
    return slide("ensaio", 320, p, rs, eyebrow="O ensaio mais citado", titulo="Polarizado à frente, com cuidado na leitura",
                 destaque="Metanálise de 2019: polarizado cerca de 40 segundos melhor no contrarrelógio de 10 km; no ciclismo, menos claro.", destaque_cor="ambar",
                 fonte="Front Physiol 2014 · J Strength Cond Res 2019")


def paga_95():
    """9.5: com o fácil, a sessão forte sai com qualidade; sem ele, vira mais uma sessão no meio."""
    p = [svg_abre(1664, 320, "Dois caminhos. Com o treino fácil de verdade, há recuperação e a sessão forte sai com qualidade. Sem ele, a sessão forte não sai com qualidade e vira mais uma sessão na faixa do meio"), defs(OXID, FOSF)]
    rs = []
    for k, (a, b, cor, fundo, mk, t2) in enumerate([("treino fácil de verdade", "recuperação", OXID, OXID_T, "m0", "a sessão forte sai com qualidade"),
                                                    ("sem treino fácil", "fadiga acumulada", FOSF, FOSF_T, "m1", "a forte vira mais uma sessão no meio")]):
        y = k * 170
        p.append(caixa(0, y, 420, 140, cor, fundo, esp=2, rx=16))
        rs.append(rot(20, y + 50, a, w=380, tam=25, cor=cor, peso=700, serif=True, alinha="center"))
        p.append(seta(432, y + 70, 520, y + 70, cor, mk, esp=4))
        p.append(caixa(532, y, 420, 140, cor, CARTAO, esp=2, rx=16))
        rs.append(rot(552, y + 50, b, w=380, tam=24, cor=TINTA, peso=700, alinha="center"))
        p.append(seta(964, y + 70, 1052, y + 70, cor, mk, esp=4))
        p.append(caixa(1064, y, 600, 140, cor, cor, esp=0, rx=16))
        rs.append(rot(1084, y + 50, t2, w=560, tam=24, cor=PAPEL, peso=700, alinha="center"))
    return slide("paga", 320, p, rs, eyebrow="A ideia da aula", titulo="O treino fácil não é o treino que sobra. É o treino que paga o treino difícil.")


def cinzenta_95():
    """9.5: as três faixas com a do meio em cinza, o que ela custa e as três causas no caso."""
    p = [svg_abre(1664, 380, "Três faixas de intensidade empilhadas, a do meio em cinza: a zona cinzenta, moderado o tempo todo; fadiga suficiente para atrapalhar, estímulo insuficiente para progredir. À direita, as três causas no caso: o fácil não parece treino, então ela nunca corre devagar; o forte dói, então nunca corre forte de verdade; o grupo escolhe, três vezes por semana o pelotão dita o ritmo")]
    rs = []
    for k, (t, cor, op) in enumerate([("forte", FOSF, 0.35), ("moderado · zona cinzenta", MUDO, 1), ("fácil", OXID, 0.35)]):
        y = k * 120
        p.append(f'<rect x="0" y="{y}" width="640" height="108" rx="12" fill="{cor}" opacity="{op}"/>')
        rs.append(rot(24, y + (16 if k == 1 else 36), t, w=600, tam=24, cor=PAPEL if k == 1 else TINTA, peso=700, serif=True))
    rs += [rot(24, 180, "fadiga que atrapalha, estímulo que não basta", w=600, tam=18, cor=PAPEL)]
    for j, (ic, t, d, cor, fundo) in enumerate([("t:walk", "Fácil “não parece treino”", "então ela nunca corre devagar", GLIC, GLIC_T),
                                                ("t:mood-sick", "Forte dói", "então ela nunca corre forte de verdade", GLIC, GLIC_T),
                                                ("t:users", "O grupo escolhe", "três vezes por semana, o pelotão dita o ritmo", FOSF, FOSF_T)]):
        y = j * 124
        p.append(caixa(700, y, 964, 110, cor, fundo, esp=2, rx=14))
        p.append(icone(ic, 724, y + 30, 48, cor))
        rs += [rot(794, y + 18, t, w=850, tam=24, cor=cor, peso=700, serif=True), rot(794, y + 58, d, w=850, tam=21, cor=TINTA)]
    return slide("cinzenta", 380, p, rs, eyebrow="O diagnóstico do caso", titulo="A zona cinzenta: fadiga que atrapalha, estímulo que não basta",
                 destaque="A pergunta que confirma custa zero: quanto você consegue conversar enquanto corre?", destaque_cor="tinta")


def conta_95():
    """9.5: doze casas com 2,4 marcadas e quatro casas com 0,8 marcada, e a regra em número de sessões."""
    p = [svg_abre(1664, 380, "Duas fileiras de casas de sessão. Doze sessões: vinte por cento são cerca de 2,4 sessões duras, duas casas cheias e quatro décimos de outra. Quatro sessões: vinte por cento são 0,8, menos de uma casa. Embaixo, a regra: de três a cinco sessões aeróbias, uma a duas de qualidade e o resto fácil de verdade; com quatro, uma forte e três fáceis, 75% fácil")]
    rs = []
    for k, (n, frac, t, cor) in enumerate([(12, 2.4, "20% de 12 = 2,4", TINTA), (4, 0.8, "20% de 4 = 0,8", FOSF)]):
        y = k * 120
        rs.append(rot(0, y + 26, t, w=280, tam=26, cor=cor, peso=700, serif=True, alinha="right"))
        for i in range(n):
            x = 310 + i * 110
            p.append(f'<rect x="{x}" y="{y}" width="96" height="90" rx="10" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/>')
            cheio = min(max(frac - i, 0), 1)
            if cheio > 0:
                p.append(f'<rect x="{x}" y="{y}" width="{96 * cheio:.0f}" height="90" rx="10" fill="{FOSF}"/>')
    p.append(caixa(0, 260, 1664, 120, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:calendar", 24, 296, 48, OXID))
    rs += [rot(96, 280, "três a cinco sessões aeróbias: uma a duas de qualidade, o resto fácil de verdade", w=1540, tam=23, cor=OXID, peso=700),
           rot(96, 324, "com quatro: uma forte e três fáceis = 75% fácil", w=1540, tam=22, cor=TINTA)]
    return slide("conta", 380, p, rs, eyebrow="A aritmética do volume baixo", titulo="Sessões de qualidade em número, não em porcentagem")


def plano_95():
    """9.5: a semana da corredora antes e depois, em casas de dia."""
    p = [svg_abre(1664, 380, "Duas semanas em casas de dia. Antes: três treinos com o grupo no ritmo do meio e uma longa sozinha, também no meio. Depois: uma sessão de qualidade intervalada, uma longa mais devagar, duas fáceis, uma no pelotão mais lento e uma sozinha em frases inteiras, e duas sessões curtas de força. Embaixo, um exemplo de intervalado: quatro a seis blocos de três a quatro minutos fortes, pausas de trote, começando pelo número menor")]
    rs = []
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    antes = [("", None), ("grupo · meio", MUDO), ("", None), ("grupo · meio", MUDO), ("", None), ("grupo · meio", MUDO), ("longa · meio", MUDO)]
    depois = [("força", TINTA), ("qualidade", FOSF), ("", None), ("fácil · grupo lento", OXID), ("força", TINTA), ("fácil · sozinha", OXID), ("longa · mais devagar", AZUL)]
    for j, d in enumerate(dias):
        rs.append(rot(220 + j * 206, 0, d, w=190, tam=19, cor=MUDO, peso=700, alinha="center"))
    for k, (t, sem) in enumerate([("Antes", antes), ("Depois", depois)]):
        y = 34 + k * 112
        rs.append(rot(0, y + 30, t, w=190, tam=26, cor=FOSF if k == 0 else OXID, peso=700, serif=True, alinha="right"))
        for j, (lab, cor) in enumerate(sem):
            x = 220 + j * 206
            if cor:
                p.append(f'<rect x="{x}" y="{y}" width="190" height="96" rx="12" fill="{cor}" opacity="{0.6 if k == 0 else 0.92}"/>')
                rs.append(rot(x + 8, y + 26, lab, w=174, tam=18, cor=PAPEL, peso=700, alinha="center", lh=1.15))
            else:
                p.append(f'<rect x="{x}" y="{y}" width="190" height="96" rx="12" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    p.append(caixa(0, 280, 1664, 100, FOSF, FOSF_T, esp=2, rx=14))
    for b in range(6):
        p.append(f'<rect x="{30 + b * 70}" y="{304 if b < 4 else 304}" width="50" height="52" rx="6" fill="{FOSF}" opacity="{1 if b < 4 else 0.35}"/>')
    rs.append(rot(470, 304, "exemplo de intervalado: 4 a 6 blocos de 3 a 4 min fortes, pausas de trote; começa pelo número menor", w=1170, tam=21, cor=TINTA, peso=700, lh=1.25))
    return slide("plano", 380, p, rs, eyebrow="O plano", titulo="A semana da corredora, reorganizada",
                 destaque="O formato do intervalado é exemplo de prática corrente; os dias da semana são ilustrativos.", destaque_cor="tinta")


def acompanhar_95():
    """9.5: três perguntas de acompanhamento, cada uma com o seu desenho."""
    p = [svg_abre(1664, 340, "Três cartões. Dias fáceis: ela conversa em frases inteiras? Se não, está rápido. Intervalado: os blocos saem parecidos do primeiro ao último? A semana: sono, dor e vontade de treinar no dia seguinte")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("Dias fáceis", "ela conversa em frases inteiras? Se não, está rápido", OXID, OXID_T),
                                            ("Intervalado", "os blocos saem parecidos do primeiro ao último?", FOSF, FOSF_T),
                                            ("A semana", "sono, dor e vontade de treinar no dia seguinte", GLIC, GLIC_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 340, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 18, t, w=W - 48, tam=27, cor=cor, peso=700, serif=True), rot(x + 24, 250, d, w=W - 48, tam=21, cor=TINTA, lh=1.3)]
    p.append(icone("t:message-circle", 60, 90, 70, OXID))
    p.append(icone("t:message-circle", 170, 110, 50, OXID))
    rs.append(rot(250, 120, "frases inteiras", w=260, tam=21, cor=OXID, peso=700))
    x0 = W + 40
    for j in range(5):
        p.append(f'<rect x="{x0 + 40 + j * 90}" y="100" width="66" height="110" rx="6" fill="{FOSF}" opacity="0.85"/>')
    x0 = 2 * (W + 40)
    for j, ic in enumerate(["t:moon", "t:mood-sick", "t:run"]):
        p.append(icone(ic, x0 + 60 + j * 150, 110, 70, GLIC))
    return slide("acompanhar", 340, p, rs, eyebrow="Como acompanhar, sem laboratório", titulo="Três perguntas",
                 destaque="O caso não tem desfecho aqui. Fica o raciocínio: achar a zona cinzenta, separar os extremos, dosar a qualidade em número.", destaque_cor="tinta")

# ---------------------------------------------------------------- 9.6

def telas_96():
    """9.6: três telas do mesmo treino, cada uma com a sua âncora escondida embaixo."""
    p = [svg_abre(1664, 340, "Três telas do mesmo treino de uma hora de bicicleta. O relógio diz zona quatro; sua âncora é uma fórmula de idade. O aplicativo de potência diz zona dois; sua âncora é um teste de um ano atrás. A planilha diz ritmo de conversa; sua âncora é a fala dele, de hoje")]
    rs = []
    W = 528
    for k, (ic, tela, valor, ancora, cor) in enumerate([("t:clock", "o relógio", "zona 4", "fórmula de idade", FOSF), ("t:bolt", "o aplicativo", "zona 2", "teste de um ano atrás", GLIC),
                                                        ("t:notebook", "a planilha", "“ritmo de conversa”", "a fala dele, de hoje", OXID)]):
        x = k * (W + 40)
        p.append(f'<rect x="{x}" y="0" width="{W}" height="220" rx="24" fill="{TINTA}"/>')
        p.append(f'<rect x="{x + 16}" y="16" width="{W - 32}" height="188" rx="14" fill="#1E3346"/>')
        p.append(icone(ic, x + 32, 30, 36, PAPEL))
        rs += [rot(x + 80, 36, tela, w=W - 110, tam=21, cor=PAPEL, peso=700), rot(x + 16, 98, valor, w=W - 32, tam=40 if k < 2 else 30, cor=PAPEL, peso=700, alinha="center", serif=True)]
        p.append(caixa(x, 240, W, 100, cor, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, 252, "âncora", w=W - 40, tam=17, cor=MUDO, peso=700), rot(x + 20, 282, ancora, w=W - 40, tam=23, cor=cor, peso=700)]
    return slide("telas", 340, p, rs, eyebrow="Uma hora de bicicleta, três respostas", titulo="O relógio diz zona quatro. O aplicativo diz zona dois. A planilha diz “ritmo de conversa”.")


def roteiro_96():
    """9.6: quatro passos em fila, da âncora à conferência."""
    p = [svg_abre(1664, 300, "Quatro passos em fila. Âncora: o ponto de referência a partir do qual as zonas são calculadas. Medida do dia: frequência cardíaca, ritmo, potência ou percepção de esforço. Zonas: poucas, e refeitas quando a âncora envelhece. Conferência: com a fala e com o dia seguinte"), defs(MUDO)]
    rs = []
    W = 380
    for k, (ic, t, d, cor, fundo) in enumerate([("t:anchor", "Âncora", "o ponto de referência a partir do qual as zonas são calculadas", TINTA, PAPEL),
                                                ("t:gauge", "Medida do dia", "frequência cardíaca, ritmo, potência ou percepção de esforço", GLIC, GLIC_T),
                                                ("t:chart-bar", "Zonas", "poucas, e refeitas quando a âncora envelhece", OXID, OXID_T),
                                                ("t:check", "Conferência", "com a fala e com o dia seguinte", FOSF, FOSF_T)]):
        x = k * (W + 48)
        p.append(caixa(x, 0, W, 300, cor, fundo, esp=2, rx=16))
        p.append(f'<circle cx="{x + 42}" cy="46" r="26" fill="{cor}"/>')
        rs.append(rot(x + 16, 30, str(k + 1), w=52, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True))
        p.append(icone(ic, x + W - 66, 22, 48, cor))
        rs += [rot(x + 22, 100, t, w=W - 44, tam=27, cor=cor, peso=700, serif=True), rot(x + 22, 156, d, w=W - 44, tam=21, cor=TINTA, lh=1.3)]
        if k < 3:
            p.append(seta(x + W + 6, 150, x + W + 42, 150, MUDO, "m0", esp=3))
    return slide("roteiro", 300, p, rs, eyebrow="O roteiro", titulo="Quatro passos")


def ancoras_96():
    """9.6: o máximo estimado com duas faixas de erro somadas, contra o limiar medido, estreito, em esquema."""
    p = [svg_abre(1664, 360, "Em esquema, duas âncoras. À esquerda, o máximo estimado pela idade: a faixa de erro da fórmula no indivíduo e a faixa de erro da porcentagem se somam numa faixa larga, e o treino fácil do triatleta aparece como zona quatro. À direita, o limiar medido na pessoa: uma faixa estreita, obtida no laboratório quando há, pelo teste da fala para o primeiro limiar, ou por um esforço contínuo de 30 minutos para o segundo")]
    rs = []
    p.append(caixa(0, 0, 800, 360, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(24, 16, "Máximo estimado pela idade", w=760, tam=26, cor=FOSF, peso=700, serif=True))
    for j, (t, w) in enumerate([("erro da fórmula", 300), ("erro da porcentagem", 260)]):
        y = 90 + j * 70
        p.append(f'<rect x="{400 - w // 2}" y="{y}" width="{w}" height="46" rx="23" fill="{FOSF}" opacity="0.5"/>')
        rs.append(rot(24, y + 10, t, w=220, tam=19, cor=TINTA, peso=700))
    p.append(f'<rect x="120" y="234" width="560" height="46" rx="23" fill="{FOSF}"/>')
    rs += [rot(120, 244, "dois erros somados", w=560, tam=20, cor=PAPEL, peso=700, alinha="center"),
           rot(24, 300, "o treino fácil do triatleta vira zona quatro", w=760, tam=20, cor=TINTA, peso=700)]
    p.append(caixa(864, 0, 800, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(888, 16, "Limiar medido na pessoa", w=760, tam=26, cor=OXID, peso=700, serif=True))
    p.append(f'<rect x="1220" y="90" width="90" height="46" rx="23" fill="{OXID}"/>')
    rs.append(rot(888, 100, "faixa estreita", w=320, tam=19, cor=TINTA, peso=700))
    for j, (ic, t) in enumerate([("t:building-hospital", "laboratório, quando há"), ("t:message-circle", "teste da fala: primeiro limiar"), ("t:stopwatch", "esforço contínuo de 30 min: segundo limiar")]):
        y = 168 + j * 60
        p.append(icone(ic, 888, y, 40, OXID))
        rs.append(rot(944, y + 8, t, w=700, tam=21, cor=TINTA, peso=700))
    return slide("ancoras", 360, p, rs, eyebrow="E o máximo costuma ser estimado", titulo="Dois erros somados, ou uma âncora medida",
                 destaque="Os métodos de campo estão na aula de limiares do módulo de fisiologia.", destaque_cor="tinta")


def poucas_96():
    """9.6: uma régua de intensidade com dois limiares e três faixas, e o calendário que lembra de refazer a âncora."""
    p = [svg_abre(1664, 320, "Uma régua de intensidade com duas linhas, o primeiro e o segundo limiar, e três faixas: fácil abaixo do primeiro, moderado entre os dois, forte acima do segundo. À direita, um calendário: as zonas envelhecem, e refazer a âncora faz parte da prescrição")]
    rs = []
    faixas = [(0, 420, "Fácil", "abaixo do 1º limiar", OXID), (430, 360, "Moderado", "entre os limiares", GLIC), (800, 320, "Forte", "acima do 2º limiar", FOSF)]
    for x, w, t, d, cor in faixas:
        p.append(f'<rect x="{x}" y="60" width="{w}" height="150" rx="12" fill="{cor}"/>')
        rs += [rot(x + 20, 92, t, w=w - 40, tam=30, cor=PAPEL, peso=700, serif=True), rot(x + 20, 146, d, w=w - 40, tam=21, cor=PAPEL)]
    for x, t in [(425, "1º limiar"), (795, "2º limiar")]:
        p.append(f'<line x1="{x}" y1="40" x2="{x}" y2="232" stroke="{TINTA}" stroke-width="4"/>')
        rs.append(rot(x - 80, 6, t, w=160, tam=19, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<path d="M 0 262 L 1100 262" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M 1090 254 L 1110 262 L 1090 270 Z" fill="{MUDO}"/>')
    rs.append(rot(0, 274, "intensidade", w=400, tam=18, cor=MUDO))
    p.append(caixa(1200, 30, 464, 260, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:refresh", 1224, 54, 52, TINTA))
    rs += [rot(1290, 62, "As zonas envelhecem", w=360, tam=24, cor=TINTA, peso=700, serif=True),
           rot(1224, 140, "um teste de um ano atrás descreve outra pessoa: refazer a âncora faz parte da prescrição", w=420, tam=20, cor=TINTA, lh=1.3)]
    return slide("poucas", 320, p, rs, eyebrow="Passo três · as zonas", titulo="Três faixas resolvem quase tudo",
                 destaque="Cinco ou sete zonas criam uma precisão que nenhum aparelho entrega.", destaque_cor="tinta")


def ancorada_96():
    """9.6: a âncora na idade, riscada, e a âncora na pessoa, conferida pela percepção de esforço."""
    p = [svg_abre(1664, 320, "Duas âncoras. Na idade: riscada. Na pessoa: marcada como certa, e ligada à ferramenta que confere se ela continua boa, a percepção de esforço"), defs(OXID)]
    rs = []
    p.append(caixa(0, 40, 480, 220, FOSF, FOSF_T, esp=2, rx=16))
    p.append(icone("t:anchor", 40, 100, 90, FOSF))
    rs.append(rot(150, 120, "na idade", w=300, tam=34, cor=FOSF, peso=700, serif=True))
    p.append(f'<line x1="30" y1="240" x2="450" y2="60" stroke="{FOSF}" stroke-width="6"/>')
    p.append(caixa(560, 40, 520, 220, OXID, OXID, esp=0, rx=16))
    p.append(icone("t:anchor", 600, 100, 90, PAPEL))
    rs.append(rot(710, 120, "na pessoa", w=340, tam=34, cor=PAPEL, peso=700, serif=True))
    p.append(seta(1092, 150, 1170, 150, OXID, "m0", esp=4))
    p.append(caixa(1184, 40, 480, 220, OXID, OXID_T, esp=2, rx=16))
    p.append(icone("t:gauge", 1208, 70, 60, OXID))
    rs += [rot(1280, 78, "confere", w=360, tam=26, cor=OXID, peso=700, serif=True), rot(1208, 150, "a percepção de esforço diz se a âncora continua boa", w=430, tam=21, cor=TINTA, peso=700, lh=1.3)]
    return slide("ancorada", 320, p, rs, eyebrow="A ideia da aula", titulo="Uma zona só vale se estiver ancorada na pessoa, e não na idade dela.")


def borg_96():
    """9.6: a escala de 6 a 20 com os dois limiares marcados e as duas faixas recomendadas."""
    p = [svg_abre(1664, 360, "A escala de Borg de 6 a 20 desenhada como régua horizontal. Em 2.560 pessoas de idades, modalidades e níveis diferentes, incluindo doença coronariana, o primeiro limiar de lactato ficou, em média, perto de 11, e o limiar anaeróbio individual perto de 13,6. Acima da régua, as faixas recomendadas: 11 a 13 para quem treina menos; 13 a 15 para esforço mais intenso, ainda aeróbio")]
    rs = []
    X0, E, Y = 60, 100, 200
    def px(v):
        return X0 + (v - 6) * E
    p.append(f'<line x1="{px(6)}" y1="{Y}" x2="{px(20)}" y2="{Y}" stroke="{TINTA}" stroke-width="4"/>')
    for v in range(6, 21):
        p.append(f'<line x1="{px(v)}" y1="{Y - 10}" x2="{px(v)}" y2="{Y + 10}" stroke="{TINTA}" stroke-width="2"/>')
        if v % 2 == 0 or v in (11, 13, 15):
            rs.append(rot(px(v) - 30, Y + 18, str(v), w=60, tam=19, cor=TINTA, peso=700, alinha="center"))
    for a, b, t, cor, y in [(11, 13, "11 a 13: quem treina menos", OXID, 80), (13, 15, "13 a 15: mais intenso, ainda aeróbio", GLIC, 30)]:
        p.append(f'<rect x="{px(a)}" y="{y + 36}" width="{(b - a) * E}" height="26" rx="13" fill="{cor}"/>')
        rs.append(rot(px(a), y, t, w=520, tam=19, cor=cor, peso=700) if a == 13 else rot(px(a) - 530, y + 38, t, w=520, tam=19, cor=cor, peso=700, alinha="right"))
    for v, t, cor in [(11, "1º limiar ≈ 11", OXID), (13.6, "limiar anaeróbio individual ≈ 13,6", FOSF)]:
        p.append(f'<circle cx="{px(v):.0f}" cy="{Y}" r="14" fill="{cor}"/>')
        p.append(f'<line x1="{px(v):.0f}" y1="{Y + 14}" x2="{px(v):.0f}" y2="{Y + 80}" stroke="{cor}" stroke-width="2"/>')
        rs.append(rot(px(v) - 10, Y + 84, t, w=420, tam=20, cor=cor, peso=700))
    p.append(caixa(0, 260, 380, 100, TINTA, TINTA, esp=0, rx=14))
    rs += [rot(0, 270, "2.560", w=380, tam=36, cor=PAPEL, peso=700, alinha="center", serif=True), rot(16, 318, "pessoas, incluindo doença coronariana", w=348, tam=17, cor=PAPEL, alinha="center")]
    return slide("borg", 360, p, rs, eyebrow="A percepção tem respaldo", titulo="Os limiares cabem na escala de Borg",
                 destaque="Relação independente de sexo, idade e modalidade.", destaque_cor="tinta", fonte="Eur J Appl Physiol 2013")


def escalas_96():
    """9.6: as duas réguas, de 6 a 20 e de 0 a 10, cada uma com o seu uso."""
    p = [svg_abre(1664, 300, "Duas réguas. De 6 a 20: a do estudo de 2013, para prescrever intensidade durante o esforço. De 0 a 10: para registrar o custo da sessão inteira, assunto da aula de carga interna")]
    rs = []
    for k, (a, b, t, uso, cor) in enumerate([(6, 20, "de 6 a 20", "prescrever intensidade durante o esforço", TINTA), (0, 10, "de 0 a 10", "registrar o custo da sessão inteira · carga interna", OXID)]):
        y = k * 150
        rs += [rot(0, y + 20, t, w=220, tam=28, cor=cor, peso=700, serif=True), rot(0, y + 70, uso, w=420, tam=19, cor=TINTA, lh=1.25)]
        n = b - a
        for i in range(n + 1):
            x = 460 + i * (1180 / n)
            p.append(f'<rect x="{x - 2:.0f}" y="{y + 20}" width="4" height="50" fill="{cor}"/>')
            if n <= 10 or i % 2 == 0:
                rs.append(rot(x - 25, y + 78, str(a + i), w=50, tam=17, cor=cor, peso=700, alinha="center"))
        p.append(f'<line x1="460" y1="{y + 45}" x2="1640" y2="{y + 45}" stroke="{cor}" stroke-width="3"/>')
    return slide("escalas", 300, p, rs, eyebrow="Duas escalas, sem misturar", titulo="O que dá valor à nota são as âncoras",
                 destaque="Mesmas palavras todas as vezes. Na primeira aplicação: “o treino mais duro que você já fez” é o máximo.", destaque_cor="tinta",
                 fonte="Borg, Med Sci Sports Exerc 1982")


def medidas_96():
    """9.6: três medidas do dia, cada uma com um pequeno traçado do seu ponto cego."""
    p = [svg_abre(1664, 360, "Três cartões, cada um com um pequeno traçado em esquema. Frequência cardíaca: nos tiros curtos, a curva ainda sobe quando o tiro acaba; no esforço longo, sobe aos poucos, mais no calor. Ritmo ou potência: responde na hora, em degraus retos; não diz quanto custou naquele dia. Percepção de esforço: integra sono, calor e cansaço, e avisa primeiro")]
    rs = []
    W = 528
    for k, (t, d, cor, fundo) in enumerate([("Frequência cardíaca", "atrasa nos tiros curtos; sobe aos poucos no esforço longo, mais no calor", GLIC, GLIC_T),
                                            ("Ritmo ou potência", "responde na hora; não diz quanto custou naquele dia", OXID, OXID_T),
                                            ("Percepção de esforço", "integra sono, calor e cansaço; avisa primeiro", FOSF, FOSF_T)]):
        x = k * (W + 40)
        p.append(caixa(x, 0, W, 360, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 24, 16, t, w=W - 48, tam=26, cor=cor, peso=700, serif=True), rot(x + 24, 262, d, w=W - 48, tam=20, cor=TINTA, lh=1.3)]
    p.append(f'<polyline points="40,200 100,200 100,110 180,110 180,200 260,200 260,110 340,110 340,200 420,200" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
    p.append(f'<path d="M 40 200 L 100 200 C 140 196, 170 150, 180 140 C 200 150, 240 196, 260 190 C 300 170, 330 140, 340 132 C 360 150, 400 190, 420 188" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    rs.append(rot(300, 70, "esquema", w=200, tam=16, cor=MUDO, alinha="right"))
    x0 = W + 40
    p.append(f'<polyline points="{x0 + 40},200 {x0 + 100},200 {x0 + 100},110 {x0 + 180},110 {x0 + 180},200 {x0 + 260},200 {x0 + 260},110 {x0 + 340},110 {x0 + 340},200 {x0 + 420},200" fill="none" stroke="{OXID}" stroke-width="5"/>')
    x0 = 2 * (W + 40)
    for j, ic in enumerate(["t:moon", "t:temperature", "t:hourglass"]):
        p.append(icone(ic, x0 + 50 + j * 150, 110, 64, FOSF))
    return slide("medidas", 360, p, rs, eyebrow="Passo dois · a medida do dia", titulo="Cada medida tem um ponto cego")


def tabela_96():
    """9.6: três faixas reconhecidas de três jeitos: fala, escala e medida objetiva."""
    p = [svg_abre(1664, 360, "Uma grade de três faixas por três jeitos de reconhecer. Fácil: frases inteiras; até perto de 11 na escala de 6 a 20; abaixo do primeiro limiar medido. Moderado: frases curtas; em torno de 11 a 14; entre os limiares. Forte: palavras soltas; acima de 14 a 15; acima do segundo limiar")]
    rs = []
    cab = [("t:message-circle", "Fala"), ("t:gauge", "Escala de 6 a 20"), ("t:chart-line", "Medida objetiva")]
    for j, (ic, t) in enumerate(cab):
        x = 300 + j * 456
        p.append(icone(ic, x + 10, 0, 36, TINTA))
        rs.append(rot(x + 56, 4, t, w=380, tam=22, cor=TINTA, peso=700))
    linhas = [("Fácil", ["frases inteiras", "até perto de 11", "abaixo do 1º limiar medido"], OXID, OXID_T),
              ("Moderado", ["frases curtas", "em torno de 11 a 14", "entre os limiares"], GLIC, GLIC_T),
              ("Forte", ["palavras soltas", "acima de 14 a 15", "acima do 2º limiar"], FOSF, FOSF_T)]
    for k, (t, cel, cor, fundo) in enumerate(linhas):
        y = 56 + k * 100
        p.append(caixa(0, y, 280, 86, cor, cor, esp=0, rx=14))
        rs.append(rot(0, y + 26, t, w=280, tam=27, cor=PAPEL, peso=700, alinha="center", serif=True))
        for j, c in enumerate(cel):
            x = 300 + j * 456
            p.append(caixa(x, y, 440, 86, cor, fundo, esp=2, rx=14))
            rs.append(rot(x + 20, y + 28, c, w=400, tam=22, cor=TINTA, peso=700))
    return slide("tabela", 360, p, rs, eyebrow="Juntando tudo", titulo="Três jeitos de reconhecer cada faixa",
                 destaque="As notas são aproximações de média para começar. Na pessoa, ajustam-se em poucas semanas.", destaque_cor="tinta")


def desempate_96():
    """9.6: três tipos de treino, cada um com a medida que manda e o porquê."""
    p = [svg_abre(1664, 340, "Três linhas, cada tipo de treino com a medida que manda. Dia fácil: fala e percepção, porque se conversa em frases inteiras está fácil. Intervalado: ritmo ou potência, porque a frequência cardíaca atrasa. Longo e estável: frequência cardíaca, ancorada no limiar, com atenção à subida no fim"), defs(MUDO)]
    rs = []
    rs += [rot(400, 0, "manda", w=440, tam=19, cor=MUDO, peso=700, alinha="center"), rot(920, 0, "por quê", w=744, tam=19, cor=MUDO, peso=700, alinha="center")]
    for k, (t, ic, manda, pq, cor, fundo) in enumerate([("Dia fácil", "t:message-circle", "fala e percepção", "se conversa em frases inteiras, está fácil", OXID, OXID_T),
                                                        ("Intervalado", "t:bolt", "ritmo ou potência", "a frequência cardíaca atrasa", FOSF, FOSF_T),
                                                        ("Longo e estável", "t:heart-handshake", "frequência cardíaca", "ancorada no limiar; atenção à subida no fim", GLIC, GLIC_T)]):
        y = 36 + k * 100
        p.append(caixa(0, y, 370, 86, cor, fundo, esp=2, rx=14))
        rs.append(rot(20, y + 26, t, w=330, tam=25, cor=cor, peso=700, serif=True))
        p.append(caixa(400, y, 440, 86, cor, cor, esp=0, rx=14))
        p.append(icone(ic, 420, y + 22, 42, PAPEL))
        rs.append(rot(476, y + 28, manda, w=350, tam=23, cor=PAPEL, peso=700))
        p.append(seta(850, y + 43, 906, y + 43, MUDO, "m0", esp=3))
        p.append(caixa(920, y, 744, 86, BORDA, CARTAO, esp=2, rx=14))
        rs.append(rot(944, y + 28, pq, w=700, tam=22, cor=TINTA))
    return slide("desempate", 340, p, rs, eyebrow="Passo quatro · quando os aparelhos discordam", titulo="Cada medida manda num tipo de treino",
                 destaque="A conferência final é o dia seguinte. “Fácil” que deixa cansaço pede âncora nova.", destaque_cor="tinta")

# ---------------------------------------------------------------- 9.7

def coletes_97():
    """9.7: seis coletes pendurados, uma pilha de relatórios e o espaço vazio da conclusão."""
    p = [svg_abre(1664, 340, "Seis coletes de GPS pendurados, emprestados a um time amador para os treinos de terça e quinta. Ao lado, uma pilha de relatórios: distância, velocidade máxima, sprints, acelerações. Na ponta, a caixa da conclusão, vazia. Embaixo: todo relógio esportivo já é um GPS"), defs(MUDO)]
    rs = []
    p.append(f'<line x1="0" y1="30" x2="560" y2="30" stroke="{MUDO}" stroke-width="4"/>')
    for j in range(6):
        x = 20 + j * 90
        p.append(f'<path d="M {x + 35} 30 L {x + 35} 50 M {x} 60 L {x + 20} 50 L {x + 50} 50 L {x + 70} 60 L {x + 62} 170 L {x + 8} 170 Z" fill="{GLIC}" stroke="{TINTA}" stroke-width="2"/>')
    rs.append(rot(0, 190, "seis coletes emprestados · terça e quinta", w=560, tam=20, cor=TINTA, peso=700, alinha="center"))
    for j in range(4):
        p.append(f'<rect x="{640 + j * 10}" y="{40 + j * 10}" width="400" height="200" rx="8" fill="{CARTAO}" stroke="{BORDA}" stroke-width="2"/>')
    for j, t in enumerate(["distância", "velocidade máxima", "sprints", "acelerações"]):
        rs.append(rot(696, 90 + j * 40, "· " + t, w=320, tam=20, cor=TINTA))
    p.append(seta(1080, 150, 1160, 150, MUDO, "m0", esp=3))
    p.append(f'<rect x="1176" y="60" width="488" height="180" rx="16" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    rs += [rot(1176, 100, "conclusão", w=488, tam=26, cor=FOSF, peso=700, alinha="center", serif=True), rot(1176, 150, "?", w=488, tam=48, cor=FOSF, peso=700, alinha="center")]
    p.append(caixa(0, 270, 1664, 70, TINTA, TINTA, esp=0, rx=14))
    p.append(icone("t:clock", 24, 283, 44, PAPEL))
    rs.append(rot(84, 290, "o mesmo vale para quem atende o indivíduo: todo relógio esportivo já é um GPS", w=1560, tam=22, cor=PAPEL, peso=700))
    return slide("coletes", 340, p, rs, eyebrow="Seis coletes emprestados", titulo="Uma pilha de relatórios e nenhuma conclusão.")


def externa_97():
    """9.7: os mesmos dez quilômetros no GPS de duas pessoas, e custos diferentes do lado de dentro."""
    p = [svg_abre(1664, 340, "À esquerda, carga externa: o GPS registra os mesmos 10 km para duas pessoas; é igual para qualquer um. À direita, carga interna: o custo desses 10 km muda com sono, turno, calor e cansaço; uma barra curta, outra longa; isso não está no relatório. No meio, a relação entre as duas é a informação útil")]
    rs = []
    p.append(caixa(0, 0, 720, 340, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(24, 16, "Carga externa · o que foi feito", w=680, tam=24, cor=TINTA, peso=700, serif=True))
    for k in range(2):
        y = 90 + k * 100
        p.append(icone("h:running", 30, y, 56, TINTA))
        p.append(f'<rect x="110" y="{y + 10}" width="460" height="40" rx="8" fill="{TINTA}"/>')
        rs.append(rot(590, y + 14, "10 km", w=120, tam=26, cor=TINTA, peso=700, serif=True))
    rs.append(rot(24, 300, "distância, velocidade, acelerações: é o que o GPS mede", w=680, tam=19, cor=TINTA))
    rs.append(rot(720, 140, "÷", w=224, tam=60, cor=OXID, peso=700, alinha="center"))
    rs.append(rot(720, 220, "a relação é a informação útil", w=224, tam=18, cor=OXID, peso=700, alinha="center", lh=1.2))
    p.append(caixa(944, 0, 720, 340, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(968, 16, "Carga interna · o que custou", w=680, tam=24, cor=OXID, peso=700, serif=True))
    for k, (w, d) in enumerate([(260, "dormiu bem"), (560, "cinco horas de sono, veio do turno")]):
        y = 100 + k * 100
        p.append(f'<rect x="968" y="{y}" width="{w}" height="40" rx="8" fill="{OXID if k == 0 else FOSF}"/>')
        rs.append(rot(968, y + 46, d, w=660, tam=18, cor=TINTA))
    rs.append(rot(968, 300, "sono, turno, calor, cansaço: não está no relatório", w=680, tam=19, cor=TINTA))
    return slide("externa", 340, p, rs, eyebrow="Erro um", titulo="Tratar o que foi feito como se fosse o que custou",
                 destaque="Complementares. A informação útil vem da relação entre as duas.", destaque_cor="tinta",
                 fonte="Consenso de monitoramento de carga, Int J Sports Physiol Perform 2017")


def amostragem_97():
    """9.7: o mesmo sprint com mudança de direção traçado com poucos e com muitos registros por segundo."""
    p = [svg_abre(1664, 340, "O mesmo sprint com mudança de direção, traçado duas vezes sobre a trajetória real. Com poucos registros por segundo, cinco, a linha corta os cantos e subestima o que é curto e intenso. Com dez registros por segundo, a linha acompanha a curva; no estudo contra um laser, foi mais válida e confiável, sobretudo em aceleração e desaceleração")]
    rs = []
    import math
    for k, (t, n, cor, fundo) in enumerate([("5 registros por segundo", 5, FOSF, FOSF_T), ("10 registros por segundo", 10, OXID, OXID_T)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 340, cor, fundo, esp=2, rx=16))
        rs.append(rot(x0 + 24, 16, t, w=760, tam=24, cor=cor, peso=700, serif=True))
        real = []
        for i in range(41):
            u = i / 40
            real.append((x0 + 60 + u * 700, 230 - 140 * math.sin(math.pi * u) ** 2))
        p.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in real) + f'" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
        amos = [real[int(i * 40 / n)] for i in range(n + 1)]
        p.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in amos) + f'" fill="none" stroke="{cor}" stroke-width="5"/>')
        for x, y in amos:
            p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="{cor}"/>')
        rs.append(rot(x0 + 24, 268, "corta os cantos; subestima o curto e intenso" if k == 0 else "acompanha a curva; mais válido e confiável", w=760, tam=21, cor=TINTA, peso=700))
    rs.append(rot(24, 304, "tracejado: trajetória real · esquema", w=600, tam=17, cor=MUDO))
    return slide("amostragem", 340, p, rs, eyebrow="Erro dois", titulo="Comparar números de aparelhos diferentes",
                 destaque="Trocou de fornecedor ou de relógio: a série começa de novo.", destaque_cor="tinta", fonte="J Sports Sci 2012")


def limiar_97():
    """9.7: dois relatórios com o mesmo número e limiares diferentes, e o mesmo limiar fixo em dois jogadores."""
    p = [svg_abre(1664, 340, "À esquerda, dois relatórios dizendo 800 m em alta intensidade, cada um com o limiar de velocidade escrito em letra miúda e diferente: o do fabricante A e o definido pelo usuário. À direita, o mesmo limiar fixo marcado sobre a escala de velocidade de dois jogadores: para um, é o máximo; para o outro, mais rápido, é trote")]
    rs = []
    for k, t in enumerate(["limiar do fabricante A", "limiar definido pelo usuário"]):
        x = k * 380
        p.append(caixa(x, 0, 350, 300, GLIC, CARTAO, esp=2, rx=14))
        rs += [rot(x + 20, 30, "alta intensidade", w=310, tam=18, cor=MUDO, peso=700), rot(x + 20, 70, "800 m", w=310, tam=52, cor=GLIC, peso=700, serif=True),
               rot(x + 20, 240, t, w=310, tam=15, cor=MUDO)]
    rs.append(rot(0, 310, "o mesmo número, limiares diferentes", w=730, tam=19, cor=TINTA, peso=700))
    p.append(caixa(800, 0, 864, 340, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(824, 16, "Absoluto ou relativo", w=800, tam=24, cor=GLIC, peso=700, serif=True))
    for k, (t, w, nota) in enumerate([("jogador 1", 500, "máximo"), ("jogador 2", 720, "trote")]):
        y = 100 + k * 100
        rs.append(rot(824, y + 6, t, w=140, tam=19, cor=TINTA, peso=700))
        p.append(f'<rect x="980" y="{y}" width="{w * 0.85:.0f}" height="36" rx="18" fill="{CINZA}" opacity="0.6"/>')
        p.append(f'<rect x="980" y="{y}" width="{w * 0.85:.0f}" height="36" rx="18" fill="none" stroke="{TINTA}" stroke-width="2"/>')
    p.append(f'<line x1="1405" y1="80" x2="1405" y2="260" stroke="{FOSF}" stroke-width="4"/>')
    rs += [rot(1300, 270, "limiar fixo", w=210, tam=19, cor=FOSF, peso=700, alinha="center"),
           rot(1416, 104, "= o máximo dele", w=230, tam=18, cor=FOSF, peso=700), rot(1416, 204, "= trote para ele", w=230, tam=18, cor=OXID, peso=700)]
    return slide("limiar", 340, p, rs, eyebrow="Erro três", titulo="Comparar números sem olhar o limiar",
                 destaque="Sem o limiar escrito, o número não se compara com nada.", destaque_cor="verm", fonte="Revisão sistemática, Sports Med 2013")


def campo_97():
    """9.7: o cone de visão do GPS cobrindo terça e quinta, e o que fica fora dele."""
    p = [svg_abre(1664, 320, "Um cone de visão saindo do GPS e iluminando a terça e a quinta, os treinos com colete, medidos muito bem. Fora do cone, no escuro, o trabalho em turno e o jogo de sábado. Quem decide para onde apontar é você")]
    rs = []
    p.append(f'<path d="M 120 160 L 900 20 L 900 300 Z" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<circle cx="120" cy="160" r="44" fill="{OXID}"/>')
    p.append(icone("t:target", 96, 136, 48, PAPEL))
    for j, t in enumerate(["terça", "quinta"]):
        y = 90 + j * 100
        p.append(caixa(600, y, 260, 70, OXID, OXID, esp=0, rx=12))
        rs.append(rot(600, y + 20, t, w=260, tam=24, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(260, 270, "dentro do campo de visão: medido muito bem", w=600, tam=19, cor=OXID, peso=700))
    for j, (ic, t) in enumerate([("t:building-hospital", "o trabalho em turno"), ("t:ball-football", "o jogo de sábado")]):
        y = 60 + j * 120
        p.append(caixa(1000, y, 664, 96, MUDO, PAPEL, esp=2, rx=14))
        p.append(icone(ic, 1024, y + 24, 48, MUDO))
        rs.append(rot(1094, y + 30, t, w=540, tam=24, cor=TINTA, peso=700))
    rs.append(rot(1000, 290, "fora do campo de visão", w=664, tam=19, cor=MUDO, peso=700))
    return slide("campo", 320, p, rs, eyebrow="A ideia da aula", titulo="O GPS mede muito bem o que está dentro do campo de visão dele. Quem decide para onde apontar é você.")


def acelerometro_97():
    """9.7: três eixos somados num índice de volume de movimento, e o tendão e a articulação fora do alcance."""
    p = [svg_abre(1664, 340, "À esquerda, três setas de eixos, x, y e z, somadas num índice: volume de movimento, que capta saltos, impactos e mudanças de direção e diz mais que a distância para goleiro e futsal. À direita, um tendão e uma articulação com um ponto de interrogação: a força que os atravessa não é medida; carga mecânica e fisiológica seguem caminhos diferentes"), defs(OXID)]
    rs = []
    p.append(caixa(0, 0, 820, 340, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "O que ele mede", w=760, tam=24, cor=OXID, peso=700, serif=True))
    cx, cy = 150, 180
    for (dx, dy, t) in [(110, 0, "x"), (0, -100, "z"), (-70, 70, "y")]:
        p.append(seta(cx, cy, cx + dx, cy + dy, OXID, "m0", esp=4))
        rs.append(rot(cx + dx * 1.2 - 15, cy + dy * 1.2 - 14, t, w=30, tam=20, cor=OXID, peso=700, alinha="center"))
    p.append(seta(300, 180, 380, 180, OXID, "m0", esp=4))
    p.append(caixa(392, 120, 400, 120, OXID, OXID, esp=0, rx=14))
    rs += [rot(392, 140, "índice somado", w=400, tam=22, cor=PAPEL, peso=700, alinha="center"), rot(392, 180, "volume de movimento", w=400, tam=19, cor=PAPEL, alinha="center"),
           rot(24, 280, "saltos, impactos, mudanças de direção · goleiro e futsal", w=780, tam=19, cor=TINTA, peso=700)]
    p.append(caixa(844, 0, 820, 340, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(868, 16, "O que ele não mede", w=760, tam=24, cor=FOSF, peso=700, serif=True))
    p.append(f'<path d="M 920 100 C 980 120, 1000 200, 1060 230" fill="none" stroke="{GLIC}" stroke-width="22" stroke-linecap="round"/>')
    p.append(f'<circle cx="1260" cy="160" r="60" fill="{CARTAO}" stroke="{MUDO}" stroke-width="4"/>')
    p.append(f'<circle cx="1260" cy="160" r="24" fill="{CINZA}"/>')
    rs += [rot(940, 250, "tendão", w=160, tam=19, cor=TINTA, peso=700, alinha="center"), rot(1180, 236, "articulação", w=160, tam=19, cor=TINTA, peso=700, alinha="center"),
           rot(1360, 120, "?", w=80, tam=56, cor=FOSF, peso=700, alinha="center"),
           rot(868, 286, "carga mecânica e fisiológica seguem caminhos diferentes", w=780, tam=19, cor=TINTA, peso=700)]
    return slide("acelerometro", 340, p, rs, eyebrow="Erro quatro", titulo="Ler o acelerômetro como carga no tecido",
                 destaque="É volume de movimento, não estresse de tecido.", destaque_cor="tinta", fonte="Revisão, Sports Med 2017")


def fora_97():
    """9.7: a semana do time, com o colete só na terça e na quinta, e a pergunta da segunda-feira."""
    p = [svg_abre(1664, 360, "A semana do time em casas de dia. Terça e quinta, com colete, medidas muito bem. Em dias de trabalho em turno, esforço alto em treino que o grupo achava moderado, sem colete. No sábado, metade do elenco jogava outra partida, sem ninguém contar. Na segunda-feira, um balão com a pergunta que corrigiu: jogou no fim de semana? quantos minutos?")]
    rs = []
    dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    tipo = ["pergunta", "colete", "turno", "colete", "turno", "jogo", ""]
    for j, (d, t) in enumerate(zip(dias, tipo)):
        x = j * 236
        rs.append(rot(x, 0, d, w=216, tam=20, cor=MUDO, peso=700, alinha="center"))
        if t == "colete":
            p.append(caixa(x, 36, 216, 160, OXID, OXID, esp=0, rx=14))
            rs.append(rot(x, 96, "com colete", w=216, tam=21, cor=PAPEL, peso=700, alinha="center"))
        elif t == "turno":
            p.append(f'<rect x="{x}" y="36" width="216" height="160" rx="14" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"{TRACO}/>')
            p.append(icone("t:building-hospital", x + 84, 60, 48, GLIC))
            rs.append(rot(x, 130, "turno, sem colete", w=216, tam=18, cor=GLIC, peso=700, alinha="center"))
        elif t == "jogo":
            p.append(f'<rect x="{x}" y="36" width="216" height="160" rx="14" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
            p.append(icone("t:ball-football", x + 84, 60, 48, FOSF))
            rs.append(rot(x + 8, 120, "outro jogo, ninguém contava", w=200, tam=18, cor=FOSF, peso=700, alinha="center", lh=1.15))
        elif t == "pergunta":
            p.append(caixa(x, 36, 216, 160, TINTA, TINTA, esp=0, rx=14))
            p.append(icone("t:message-circle", x + 84, 56, 48, PAPEL))
            rs.append(rot(x + 8, 116, "a pergunta", w=200, tam=19, cor=PAPEL, peso=700, alinha="center"))
        else:
            p.append(f'<rect x="{x}" y="36" width="216" height="160" rx="14" fill="{PAPEL}" stroke="{BORDA}" stroke-width="2"/>')
    rs.append(rot(1200, 204, "dias ilustrativos", w=464, tam=16, cor=MUDO, alinha="right"))
    p.append(caixa(0, 230, 1664, 130, TINTA, CARTAO, esp=2, rx=16))
    p.append(icone("t:message-circle", 24, 268, 52, TINTA))
    rs += [rot(96, 254, "A correção, na segunda-feira", w=1540, tam=22, cor=MUDO, peso=700),
           rot(96, 292, "“Jogou no fim de semana? Quantos minutos?”", w=1540, tam=30, cor=TINTA, peso=700, serif=True)]
    return slide("fora", 360, p, rs, eyebrow="Erro cinco", titulo="Medir só o que o colete vê")


def vale_97():
    """9.7: a progressão da velocidade no retorno de lesão, sessão a sessão, e a pergunta antes de comprar."""
    p = [svg_abre(1664, 340, "À esquerda, em esquema, onde o GPS paga: o retorno de lesão muscular, com barras sessão a sessão da fração da própria velocidade máxima atingida, subindo em degraus documentados até perto de cem por cento. À direita, antes de comprar coletes: que decisão isso vai mudar? O mesmo dinheiro compra saúde em outro lugar?")]
    rs = []
    p.append(caixa(0, 0, 900, 340, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "Onde o GPS paga: o retorno de lesão muscular", w=860, tam=23, cor=OXID, peso=700, serif=True))
    B = 270
    for j, v in enumerate([0.6, 0.65, 0.72, 0.78, 0.85, 0.9, 0.95]):
        x = 60 + j * 116
        p.append(f'<rect x="{x}" y="{B - v * 190:.0f}" width="84" height="{v * 190:.0f}" rx="6" fill="{OXID}" opacity="{0.55 + j * 0.06:.2f}"/>')
    p.append(f'<line x1="40" y1="{B - 190}" x2="880" y2="{B - 190}" stroke="{TINTA}" stroke-width="2"{TRACO}/>')
    rs += [rot(600, 50, "velocidade máxima dele", w=280, tam=17, cor=TINTA, alinha="right"),
           rot(40, 286, "sessões · fração da própria velocidade máxima · esquema", w=840, tam=18, cor=MUDO)]
    p.append(caixa(960, 0, 704, 340, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(984, 16, "Antes de comprar coletes", w=660, tam=24, cor=GLIC, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:question-mark", "que decisão isso vai mudar?"), ("t:scale", "o mesmo dinheiro compra saúde em outro lugar?")]):
        y = 100 + j * 100
        p.append(icone(ic, 984, y, 48, GLIC))
        rs.append(rot(1050, y + 6, t, w=590, tam=24, cor=TINTA, peso=700, lh=1.25))
    return slide("vale", 340, p, rs, eyebrow="Onde vale o que custa", titulo="O retorno de lesão, e a pergunta antes de comprar",
                 destaque="Conversa com a exposição à velocidade máxima da aula de velocidade.", destaque_cor="tinta")


def pulso_97():
    """9.7: o relógio que classifica a semana em fácil, moderado e forte, e os limites do sinal."""
    p = [svg_abre(1664, 340, "À esquerda, um relógio de pulso com a semana classificada em fácil, moderado e forte, e a distribuição em barras: o uso mais valioso, o diagnóstico da zona cinzenta visto pelo relógio. À direita, o cuidado: celular erra mais; prédios altos e trilha fechada também. Serve para tendência e volume, não para comparar tiros")]
    rs = []
    p.append(f'<rect x="40" y="20" width="260" height="300" rx="60" fill="{TINTA}"/>')
    p.append(f'<rect x="64" y="60" width="212" height="220" rx="40" fill="#1E3346"/>')
    for j, (t, h, cor) in enumerate([("F", 40, OXID), ("M", 150, MUDO), ("F", 30, FOSF)]):
        x = 90 + j * 64
        p.append(f'<rect x="{x}" y="{250 - h}" width="44" height="{h}" rx="6" fill="{cor}"/>')
    rs += [rot(340, 30, "O uso mais valioso", w=560, tam=24, cor=OXID, peso=700, serif=True),
           rot(340, 80, "classificar a semana em fácil, moderado e forte, e ver a distribuição", w=560, tam=21, cor=TINTA, lh=1.3),
           rot(340, 180, "é o diagnóstico da zona cinzenta, visto pelo relógio", w=560, tam=21, cor=OXID, peso=700, lh=1.3)]
    p.append(caixa(960, 0, 704, 340, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(984, 16, "O cuidado", w=660, tam=24, cor=GLIC, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:id", "celular erra mais que relógio dedicado"), ("t:building-hospital", "prédios altos e trilha fechada também"), ("t:chart-line", "tendência e volume, sim; comparar tiros, não")]):
        y = 84 + j * 76
        p.append(icone(ic, 984, y, 44, GLIC))
        rs.append(rot(1046, y + 8, t, w=600, tam=21, cor=TINTA, peso=700 if j == 2 else 400))
    return slide("pulso", 340, p, rs, eyebrow="O GPS que o paciente já tem", titulo="De graça, no pulso")


def correcoes_97():
    """9.7: cinco erros, cada um com a sua correção ao lado."""
    p = [svg_abre(1664, 400, "Cinco linhas, erro e correção. Carga externa tomada como carga: percepção de esforço ao lado de cada linha. Aparelhos diferentes comparados: série nova a cada troca. Limiar esquecido: limiar escrito em todo relatório. Acelerômetro lido como estresse de tecido: tratá-lo como volume de movimento. Só o que o colete vê: perguntar pelo que aconteceu fora dele"), defs(MUDO)]
    rs = []
    linhas = [("Carga externa tomada como carga", "percepção de esforço ao lado de cada linha"), ("Aparelhos diferentes comparados", "série nova a cada troca"),
              ("Limiar esquecido", "limiar escrito em todo relatório"), ("Acelerômetro lido como estresse de tecido", "tratá-lo como volume de movimento"),
              ("Só o que o colete vê", "perguntar pelo que aconteceu fora dele")]
    for k, (e, c) in enumerate(linhas):
        y = k * 80
        p.append(caixa(0, y, 720, 66, FOSF, FOSF_T, esp=2, rx=12))
        p.append(icone("t:x", 16, y + 15, 36, FOSF))
        rs.append(rot(66, y + 20, e, w=640, tam=21, cor=TINTA, peso=700))
        p.append(seta(732, y + 33, 792, y + 33, MUDO, "m0", esp=3))
        p.append(caixa(806, y, 858, 66, OXID, OXID_T, esp=2, rx=12))
        p.append(icone("t:check", 822, y + 15, 36, OXID))
        rs.append(rot(872, y + 20, c, w=770, tam=21, cor=TINTA, peso=700))
    return slide("correcoes", 400, p, rs, eyebrow="Os cinco erros", titulo="E a correção de cada um")

# ---------------------------------------------------------------- 9.8

def propostas_98():
    """9.8: dezoito atletas de handebol, três propostas na mesa e um orçamento que dá para uma."""
    p = [svg_abre(1664, 400, "No alto, dezoito atletas de uma equipe universitária de handebol. Embaixo, três propostas lado a lado: cintas de frequência cardíaca para todas; um aplicativo de variabilidade da frequência cardíaca, medido toda manhã; uma folha com quatro perguntas, respondida por mensagem depois do treino. O orçamento dá para uma. Na faixa de baixo: a resposta não é a mais sofisticada, é a que muda uma decisão")]
    rs = []
    for j in range(18):
        p.append(icone("h:woman", 120 + j * 76, 0, 52, MUDO))
    rs.append(rot(0, 64, "equipe universitária de handebol · dezoito atletas · o orçamento dá para uma", w=1664, tam=19, cor=MUDO, peso=700, alinha="center"))
    props = [("t:heartbeat", "Cintas cardíacas", "uma para cada atleta", GLIC, GLIC_T),
             ("t:device-mobile", "Aplicativo de variabilidade", "medido toda manhã", AZUL, AZUL_T),
             ("t:clipboard-list", "Folha com quatro perguntas", "por mensagem, depois do treino", OXID, OXID_T)]
    for k, (ic, t, x_, cor, fundo) in enumerate(props):
        x = k * 568
        p.append(caixa(x, 110, 528, 160, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, 140, 64, cor))
        rs += [rot(x + 104, 140, t, w=410, tam=24, cor=cor, peso=700, serif=True, lh=1.15), rot(x + 104, 210, x_, w=410, tam=20, cor=TINTA)]
    p.append(caixa(0, 300, 1664, 100, TINTA, TINTA, esp=0, rx=14))
    rs.append(rot(40, 330, "A resposta não é o mais sofisticado. É o que muda uma decisão.", w=1584, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    return slide("propostas", 400, p, rs, eyebrow="Três propostas, um orçamento", titulo="Cintas cardíacas, um aplicativo de variabilidade, ou uma folha com quatro perguntas?")


def quatro_98():
    """9.8: as quatro ferramentas da carga interna, cada uma com o que mede e o que deixa de ver."""
    p = [svg_abre(1664, 420, "Quatro cartões. Percepção de esforço da sessão: nota de 0 a 10 vezes os minutos; deixa de valer sem escala, tempo e privacidade. Frequência cardíaca durante o treino: atrasa no esforço curto e na força. Variabilidade da frequência cardíaca em repouso, de manhã: o número de um dia é ruído. Questionários curtos de sono, dor, cansaço, estresse e humor: longos demais, ninguém responde")]
    rs = []
    cards = [("t:gauge", "Percepção de esforço da sessão", "nota de 0 a 10 vezes os minutos", "sem escala, tempo e privacidade, vira ruído", OXID, OXID_T),
             ("t:heartbeat", "Frequência cardíaca", "durante o treino", "atrasa no esforço curto e na força", GLIC, GLIC_T),
             ("t:wave-sine", "Variabilidade da frequência cardíaca", "em repouso, de manhã", "o número de um dia é ruído", TINTA, CARTAO),
             ("t:clipboard-list", "Questionários curtos", "sono, dor, cansaço, estresse, humor", "longos demais, ninguém responde", FOSF, FOSF_T)]
    for k, (ic, t, x_, cego, cor, fundo) in enumerate(cards):
        x, y = (k % 2) * 844, (k // 2) * 220
        p.append(caixa(x, y, 820, 196, cor, fundo, esp=2, rx=16))
        p.append(icone(ic, x + 24, y + 24, 56, cor))
        rs += [rot(x + 100, y + 22, t, w=700, tam=24, cor=cor, peso=700, serif=True), rot(x + 100, y + 64, x_, w=700, tam=21, cor=TINTA)]
        p.append(f'<line x1="{x + 24}" y1="{y + 116}" x2="{x + 796}" y2="{y + 116}" stroke="{BORDA}" stroke-width="2"/>')
        p.append(icone("t:eye-off", x + 24, y + 132, 36, MUDO))
        rs.append(rot(x + 74, y + 138, "ponto cego: " + cego, w=730, tam=20, cor=MUDO, peso=700))
    return slide("quatro", 420, p, rs, eyebrow="A carga vista de dentro", titulo="Quatro ferramentas, cada uma com um ponto cego")


def conta_98():
    """9.8: a carga da sessão como área, minutos na base e nota na altura, e a soma de modalidades."""
    p = [svg_abre(1664, 330, "Duas áreas desenhadas em escala. Setenta minutos de base por nota sete de altura dão 490 unidades de carga. Quarenta minutos por nota quatro dão 160. À direita, quatro modalidades, musculação, quadra, piscina e jogo, respondidas com a mesma pergunta e somadas num número só da semana"), defs(MUDO)]
    rs = []
    B, kx, ky = 250, 7, 26
    for (x0, m, n, val, cor, fundo) in [(60, 70, 7, "490", TINTA, CARTAO), (640, 40, 4, "160", OXID, OXID_T)]:
        w, h = m * kx, n * ky
        p.append(f'<rect x="{x0}" y="{B - h}" width="{w}" height="{h}" rx="8" fill="{fundo}" stroke="{cor}" stroke-width="4"/>')
        rs += [rot(x0, B - h / 2 - 30, val, w=w, tam=44, cor=cor, peso=700, alinha="center", serif=True),
               rot(x0, B + 10, f"{m} minutos", w=w, tam=19, cor=TINTA, peso=700, alinha="center"),
               rot(x0 - 60, B - h / 2 - 12, f"nota {n}", w=52, tam=17, cor=TINTA, peso=700, alinha="right", lh=1.1)]
    rs.append(rot(0, 296, "altura: a nota · base: os minutos · área: unidades de carga", w=1020, tam=17, cor=MUDO))
    p.append(caixa(1080, 0, 584, 330, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(1104, 16, "A mesma pergunta em tudo", w=540, tam=23, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:barbell", "musculação"), ("t:play-basketball", "quadra"), ("t:swimming", "piscina"), ("t:trophy", "jogo")]):
        x = 1110 + j * 134
        p.append(icone(ic, x + 30, 80, 52, OXID))
        rs.append(rot(x, 140, t, w=112, tam=17, cor=TINTA, peso=700, alinha="center"))
    p.append(seta(1372, 180, 1372, 220, OXID, "m0", esp=3))
    p.append(caixa(1140, 232, 464, 70, OXID, OXID, esp=0, rx=12))
    rs.append(rot(1140, 252, "um número da semana", w=464, tam=22, cor=PAPEL, peso=700, alinha="center"))
    return slide("conta", 330, p, rs, eyebrow="A mais barata", titulo="Percepção de esforço da sessão",
                 destaque="Validada contra um padrão de frequência cardíaca em exercício contínuo, intervalado e basquete. A mesma pergunta soma quadra, musculação e jogo.", destaque_cor="tinta",
                 fonte="J Strength Cond Res 2001 · revisão, Front Neurosci 2017")


def condicoes_98():
    """9.8: a escala com âncoras, a espera depois do treino, a resposta sem plateia e o contrato de não punir."""
    p = [svg_abre(1664, 420, "Três quadros e uma faixa. A escala de 0 a 10, com as mesmas palavras em cada número, ensinadas uma vez com calma. Uma linha do tempo: o fim do treino e, cerca de trinta minutos depois, a pergunta; perguntada no fim, a nota reflete só o último tiro. Sem plateia: a nota em voz alta no grupo mede hierarquia; por mensagem, individual. Na faixa de baixo, o contrato: nunca para punir, porque nota alta que vira sermão deixa de ser honesta"), defs(GLIC)]
    rs = []
    p.append(caixa(0, 0, 528, 280, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "Escala com âncoras", w=480, tam=23, cor=OXID, peso=700, serif=True))
    for i in range(11):
        x = 44 + i * 44
        p.append(f'<rect x="{x - 16}" y="{130 - i * 6}" width="32" height="{i * 6 + 20}" rx="4" fill="{OXID}" opacity="{0.25 + i * 0.07:.2f}"/>')
    for v, x in [("0", 44), ("5", 264), ("10", 484)]:
        rs.append(rot(x - 30, 160, v, w=60, tam=19, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(24, 200, "as mesmas palavras em cada número, ensinadas uma vez com calma", w=480, tam=19, cor=TINTA, lh=1.3))
    p.append(caixa(568, 0, 528, 280, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(592, 16, "Cerca de 30 minutos depois", w=480, tam=23, cor=GLIC, peso=700, serif=True))
    p.append(f'<line x1="610" y1="120" x2="1050" y2="120" stroke="{GLIC}" stroke-width="4"/>')
    p.append(f'<circle cx="620" cy="120" r="10" fill="{GLIC}"/>')
    p.append(icone("t:message-circle", 1006, 96, 48, GLIC))
    rs += [rot(580, 140, "fim do treino", w=140, tam=17, cor=TINTA, peso=700, alinha="center"),
           rot(820, 84, "± 30 min", w=120, tam=18, cor=GLIC, peso=700, alinha="center"),
           rot(592, 200, "no fim do treino, a nota reflete só o último tiro", w=480, tam=19, cor=TINTA, lh=1.3)]
    p.append(caixa(1136, 0, 528, 280, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(1160, 16, "Sem plateia", w=480, tam=23, cor=GLIC, peso=700, serif=True))
    p.append(icone("t:users-group", 1180, 70, 64, MUDO))
    p.append(f'<line x1="1176" y1="66" x2="1248" y2="138" stroke="{FOSF}" stroke-width="5"/>')
    p.append(icone("t:message-circle", 1180, 156, 56, OXID))
    rs += [rot(1270, 84, "em voz alta, no grupo: mede hierarquia", w=370, tam=19, cor=TINTA, lh=1.25),
           rot(1270, 166, "por mensagem, individual", w=370, tam=19, cor=OXID, peso=700, lh=1.25)]
    p.append(caixa(0, 310, 1664, 110, FOSF, FOSF, esp=0, rx=14))
    p.append(icone("t:hand-stop", 28, 336, 56, PAPEL))
    rs += [rot(104, 330, "Nunca para punir", w=1520, tam=24, cor=PAPEL, peso=700, serif=True),
           rot(104, 370, "nota alta que vira sermão deixa de ser honesta", w=1520, tam=21, cor=PAPEL)]
    return slide("condicoes", 420, p, rs, eyebrow="Sem isso, vira ruído", titulo="Quatro condições para a nota valer")


def fc_98():
    """9.8: a frequência cardíaca acompanhando o esforço contínuo e atrasando nos tiros curtos e na força."""
    p = [svg_abre(1664, 380, "Dois gráficos em esquema. À esquerda, um bloco de esforço contínuo e a curva da frequência cardíaca subindo e acompanhando o bloco: funciona no esforço aeróbio contínuo, complementa a nota, de graça para quem já usa relógio. À direita, tiros curtos em picos e a curva da frequência cardíaca atrasada e achatada, sem chegar aos picos: atrasa nos esforços curtos, responde mal à força, subestima sprints, saltos e contato")]
    rs = []
    for k, (t, cor, fundo, itens) in enumerate([("Funciona", OXID, OXID_T, "esforço aeróbio contínuo · complemento objetivo à nota · de graça para quem já usa relógio"),
                                                 ("Falha", FOSF, FOSF_T, "atrasa nos esforços curtos · responde mal ao treino de força · subestima sprints, saltos e contato")]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 380, cor, fundo, esp=2, rx=16))
        rs.append(rot(x0 + 24, 16, t, w=760, tam=24, cor=cor, peso=700, serif=True))
        B = 230
        if k == 0:
            p.append(f'<rect x="{x0 + 120}" y="{B - 120}" width="560" height="120" fill="{CINZA}" opacity="0.6"/>')
            pts = []
            for i in range(61):
                u = i / 60
                xx = x0 + 60 + u * 700
                if xx < x0 + 120:
                    yy = B - 20
                elif xx > x0 + 680:
                    yy = B - 20 - 100 * (2.718 ** (-(xx - x0 - 680) / 30))
                else:
                    yy = B - 20 - 100 * (1 - 2.718 ** (-(xx - x0 - 120) / 40))
                pts.append(f"{xx:.0f},{yy:.0f}")
        else:
            for j in range(5):
                p.append(f'<rect x="{x0 + 110 + j * 130}" y="{B - 120}" width="30" height="120" fill="{CINZA}" opacity="0.6"/>')
            pts = []
            for i in range(61):
                u = i / 60
                xx = x0 + 60 + u * 700
                yy = B - 20 - 40 * (1 - 2.718 ** (-max(0, xx - x0 - 110) / 120)) - 6 * (1 + __import__("math").sin((xx - x0 - 110) / 130 * 6.283 - 1.2))
                pts.append(f"{xx:.0f},{yy:.0f}")
        p.append('<polyline points="' + " ".join(pts) + f'" fill="none" stroke="{cor}" stroke-width="5"/>')
        p.append(f'<line x1="{x0 + 50}" y1="{B}" x2="{x0 + 780}" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
        rs.append(rot(x0 + 24, 246, "cinza: esforço · linha: frequência cardíaca · esquema", w=760, tam=16, cor=MUDO))
        rs.append(rot(x0 + 24, 290, itens, w=772, tam=20, cor=TINTA, peso=700, lh=1.35))
    return slide("fc", 380, p, rs, eyebrow="Frequência cardíaca", titulo="Boa no contínuo, fraca no resto",
                 destaque="Para uma equipe de handebol: um aparelho por atleta, bateria, dados e alguém para olhar. Caro para o que entrega.", destaque_cor="tinta")


def vfc_98():
    """9.8: pontos diários serrilhados da variabilidade com a média de vários dias por cima, e o risco da ansiedade."""
    import math
    p = [svg_abre(1664, 360, "À esquerda, em esquema, pontos diários da variabilidade da frequência cardíaca muito serrilhados e, sobre eles, a média de vários dias, uma linha suave. Como usar bem: mesma hora, mesma posição, ao acordar; a média, não o número do dia; a pessoa comparada com ela mesma. À direita, o risco: decidir o dia pelo número da manhã, ansiedade com o próprio dado, padrão descrito no sono como ortossonia")]
    rs = []
    p.append(caixa(0, 0, 980, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "Como usar bem", w=900, tam=24, cor=OXID, peso=700, serif=True))
    vals = [math.sin(i * 1.9) * 0.6 + math.sin(i * 0.7 + 1) * 0.5 + math.sin(i * 0.17) * 0.4 for i in range(28)]
    pts = [(50 + i * 30, 150 - v * 50) for i, v in enumerate(vals)]
    p.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{MUDO}" stroke-width="2"/>')
    for x, y in pts:
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{MUDO}"/>')
    med = []
    for i in range(6, 28):
        med.append((50 + i * 30, 150 - sum(vals[i - 6:i + 1]) / 7 * 50))
    p.append('<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in med) + f'" fill="none" stroke="{OXID}" stroke-width="6" stroke-linecap="round"/>')
    rs += [rot(24, 226, "pontos: o número de cada manhã · linha: a média · esquema", w=930, tam=16, cor=MUDO)]
    for j, t in enumerate(["mesma hora, mesma posição, ao acordar", "a média de vários dias, não o número do dia", "a pessoa comparada com ela mesma"]):
        rs.append(rot(24 + (j % 2) * 470, 262 + (j // 2) * 40, "· " + t, w=460, tam=19, cor=TINTA, peso=700))
    p.append(caixa(1020, 0, 644, 360, GLIC, GLIC_T, esp=2, rx=16))
    rs.append(rot(1044, 16, "O risco", w=600, tam=24, cor=GLIC, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:alarm", "decidir o dia pelo número da manhã"), ("t:mood-nervous", "ansiedade com o próprio dado"), ("t:moon", "descrito no sono como ortossonia")]):
        y = 80 + j * 88
        p.append(icone(ic, 1044, y, 48, GLIC))
        rs.append(rot(1110, y + 10, t, w=530, tam=21, cor=TINTA, peso=700, lh=1.25))
    return slide("vfc", 360, p, rs, eyebrow="Variabilidade da frequência cardíaca", titulo="Exigente, e com um efeito colateral",
                 destaque="Número que gera ansiedade custa caro.", destaque_cor="tinta", fonte="Revisão, Sports Med 2013 · J Clin Sleep Med 2017")


def questionario_98():
    """9.8: a folha da manhã, quatro perguntas de 1 a 5 e uma semanal, e o caminho até ninguém responder."""
    p = [svg_abre(1664, 400, "À esquerda, a folha da manhã: como você dormiu, dor muscular, cansaço e estresse, cada uma com cinco bolinhas de 1 a 5 e uma marcada; embaixo, uma linha semanal: algum problema de saúde esta semana? No meio, um cronômetro: trinta segundos. À direita, o risco em três passos: perguntas demais, todo dia, sem retorno; na terceira semana, ninguém responde"), defs(FOSF)]
    rs = []
    p.append(caixa(0, 0, 860, 400, TINTA, CARTAO, esp=2, rx=16))
    for j, (t, m) in enumerate([("Como você dormiu?", 3), ("Dor muscular", 1), ("Cansaço", 2), ("Estresse", 3)]):
        y = 30 + j * 70
        rs.append(rot(30, y + 10, t, w=430, tam=22, cor=TINTA, peso=700))
        for i in range(5):
            cx = 520 + i * 66
            p.append(f'<circle cx="{cx}" cy="{y + 24}" r="20" fill="{OXID if i == m else PAPEL}" stroke="{OXID}" stroke-width="3"/>')
    rs.append(rot(500, 8, "1 · · · 5", w=330, tam=16, cor=MUDO, alinha="center"))
    p.append(f'<line x1="24" y1="316" x2="836" y2="316" stroke="{BORDA}" stroke-width="2"{TRACO}/>')
    rs += [rot(30, 334, "Algum problema de saúde esta semana?", w=600, tam=22, cor=TINTA, peso=700), rot(650, 334, "semanal", w=180, tam=20, cor=AZUL, peso=700, alinha="right")]
    p.append(icone("t:stopwatch", 930, 100, 96, OXID))
    rs += [rot(890, 210, "30 segundos", w=180, tam=24, cor=OXID, peso=700, alinha="center", serif=True), rot(890, 250, "de manhã", w=180, tam=19, cor=TINTA, alinha="center")]
    p.append(caixa(1120, 0, 544, 400, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(1144, 16, "O risco", w=500, tam=24, cor=FOSF, peso=700, serif=True))
    for j, t in enumerate(["perguntas demais", "todo dia", "sem retorno"]):
        y = 80 + j * 64
        p.append(caixa(1144, y, 496, 50, FOSF, CARTAO, esp=2, rx=10))
        rs.append(rot(1144, y + 12, t, w=496, tam=20, cor=TINTA, peso=700, alinha="center"))
    p.append(seta(1392, 278, 1392, 306, FOSF, "m0", esp=3))
    p.append(caixa(1144, 316, 496, 64, FOSF, FOSF, esp=0, rx=10))
    rs.append(rot(1144, 334, "na terceira semana, ninguém responde", w=496, tam=20, cor=PAPEL, peso=700, alinha="center"))
    return slide("questionario", 400, p, rs, eyebrow="Questionários curtos", titulo="Trinta segundos de manhã",
                 destaque="Medidas relatadas pela atleta respondem à carga de forma sensível. O risco: perguntas demais, todo dia, sem retorno.", destaque_cor="tinta",
                 fonte="Revisão sistemática, Br J Sports Med 2016 · formato de prática corrente")


def terceira_98():
    """9.8: três semanas de respostas, um instrumento preciso que se esvazia e uma pergunta simples que chega todo dia."""
    p = [svg_abre(1664, 330, "Três semanas, um ponto por dia, em esquema. Na primeira linha, o instrumento preciso que ninguém usa: os pontos preenchidos rareiam até sumirem na terceira semana. Na segunda linha, a pergunta simples: um ponto preenchido em todos os dias, e um olho ao lado, porque alguém lê")]
    rs = []
    for s in range(3):
        rs.append(rot(260 + s * 440, 0, f"semana {s + 1}", w=400, tam=19, cor=MUDO, peso=700, alinha="center"))
        if s:
            p.append(f'<line x1="{240 + s * 440}" y1="30" x2="{240 + s * 440}" y2="270" stroke="{BORDA}" stroke-width="2"{TRACO}/>')
    falta = {9, 11, 12, 15, 16, 17, 18, 19, 20, 13}
    for k, (t, cor, fundo) in enumerate([("preciso, e ninguém usa", MUDO, CINZA), ("simples, todo dia, e alguém lê", OXID, OXID_T)]):
        y = 60 + k * 120
        p.append(caixa(0, y, 1664, 96, cor, fundo if k else PAPEL, esp=2, rx=14))
        rs.append(rot(20, y + 22, t, w=220, tam=20, cor=TINTA if k == 0 else OXID, peso=700, lh=1.2))
        for d in range(21):
            cx = 280 + (d // 7) * 440 + (d % 7) * 56
            cheio = k == 1 or d not in falta
            p.append(f'<circle cx="{cx}" cy="{y + 48}" r="18" fill="{cor if cheio else PAPEL}" stroke="{cor}" stroke-width="3"/>')
    p.append(icone("t:eye-check", 1580, 196, 56, OXID))
    rs.append(rot(0, 300, "um ponto por dia: a resposta chegou · esquema", w=1664, tam=17, cor=MUDO, alinha="right"))
    return slide("terceira", 330, p, rs, eyebrow="A ideia da aula", titulo="O melhor instrumento é o que muda uma decisão, e que a atleta ainda responde na terceira semana.",
                 destaque="Precisão que ninguém usa vale menos que uma pergunta simples que chega todo dia e que alguém lê.", destaque_cor="tinta")


def cenarios_98():
    """9.8: quatro cenários, o instrumento principal e o complemento, com a nota da sessão em todos."""
    p = [svg_abre(1664, 420, "Quatro linhas de decisão. Coletivo com pouco dinheiro: nota da sessão, mais quatro perguntas de bem-estar. Endurance com relógio: nota da sessão e frequência cardíaca, mais variabilidade em média se tolerar. Praticante de força: nota da sessão, mais registro de cargas. Ansioso com números: nota da sessão, mais uma conversa por semana. A coluna do principal, destacada, mostra a nota da sessão em todas as linhas"), defs(MUDO)]
    rs = []
    rs += [rot(96, 0, "Cenário", w=480, tam=19, cor=MUDO, peso=700), rot(620, 0, "Principal", w=440, tam=19, cor=OXID, peso=700, alinha="center"), rot(1120, 0, "Complemento", w=544, tam=19, cor=MUDO, peso=700, alinha="center")]
    p.append(f'<rect x="608" y="30" width="464" height="390" rx="16" fill="{OXID_T}"/>')
    linhas = [("t:users-group", "Coletivo com pouco dinheiro", "nota da sessão", "quatro perguntas de bem-estar"),
              ("t:device-watch", "Endurance com relógio", "nota da sessão e FC", "variabilidade, se tolerar, em média"),
              ("t:barbell", "Praticante de força", "nota da sessão", "registro de cargas"),
              ("t:mood-nervous", "Ansioso com números", "nota da sessão", "uma conversa por semana")]
    for j, (ic, c, pr, co) in enumerate(linhas):
        y = 44 + j * 94
        p.append(icone(ic, 24, y + 14, 48, TINTA))
        rs.append(rot(96, y + 24, c, w=490, tam=22, cor=TINTA, peso=700))
        p.append(caixa(628, y + 6, 424, 70, OXID, OXID, esp=0, rx=12))
        rs.append(rot(628, y + 26, pr, w=424, tam=22, cor=PAPEL, peso=700, alinha="center"))
        p.append(seta(1060, y + 41, 1104, y + 41, MUDO, "m0", esp=3))
        p.append(caixa(1116, y + 6, 548, 70, MUDO, CARTAO, esp=2, rx=12))
        rs.append(rot(1116, y + 26, co, w=548, tam=20, cor=TINTA, alinha="center"))
    return slide("cenarios", 420, p, rs, eyebrow="Como escolher", titulo="Instrumento por cenário",
                 destaque="A nota da sessão está em todas as linhas. O complemento muda com o esporte, o dinheiro e a pessoa.", destaque_cor="petr")


def regras_98():
    """9.8: quatro regras de uso, cada uma com um desenho mínimo."""
    import math
    p = [svg_abre(1664, 440, "Quatro quadros. Contra ela mesma: duas atletas, uma que dá notas altas e outra que dá baixas, cada uma com a própria linha de base. Tendência, não o dia: pontos serrilhados com uma seta de tendência por cima. Regra antes do dado: a frase escrita antes, se três sessões voltarem acima do planejado, reduzimos e conversamos. Retorno a quem responde: um ciclo entre a atleta, a nota e o retorno; quem nunca vê o uso da nota para de responder"), defs(OXID, FOSF)]
    rs = []
    W, H = 820, 206
    for k, (t, x_, cor, fundo) in enumerate([("Contra ela mesma", "há quem dê notas altas e quem dê baixas", OXID, OXID_T),
                                             ("Tendência, não o dia", "um ponto isolado é ruído", OXID, OXID_T),
                                             ("Regra antes do dado", "", GLIC, GLIC_T),
                                             ("Retorno a quem responde", "quem nunca vê o uso da nota para de responder", FOSF, FOSF_T)]):
        x, y = (k % 2) * 844, (k // 2) * 234
        p.append(caixa(x, y, W, H, cor, fundo, esp=2, rx=16))
        rs.append(rot(x + 24, y + 16, t, w=460, tam=23, cor=cor, peso=700, serif=True))
        if x_:
            rs.append(rot(x + 24, y + 140, x_, w=420 if k != 1 else 440, tam=19, cor=TINTA, lh=1.25))
    for j, (base, cor) in enumerate([(50, OXID), (120, AZUL)]):
        yb = base + 20
        p.append(f'<line x1="500" y1="{yb}" x2="790" y2="{yb}" stroke="{cor}" stroke-width="2"{TRACO}/>')
        for i in range(7):
            p.append(f'<circle cx="{512 + i * 44}" cy="{yb + 10 * math.sin(i * 2.1 + j)}" r="7" fill="{cor}"/>')
    pts = [(1344 + i * 20, 130 - i * 3 + 26 * math.sin(i * 2.3)) for i in range(15)]
    p.append('<polyline points="' + " ".join(f"{a:.0f},{b:.0f}" for a, b in pts) + f'" fill="none" stroke="{MUDO}" stroke-width="2"/>')
    for a, b in pts:
        p.append(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="5" fill="{MUDO}"/>')
    p.append(seta(1344, 128, 1632, 78, OXID, "m0", esp=5))
    p.append(f'<rect x="24" y="300" width="772" height="116" rx="12" fill="{CARTAO}" stroke="{GLIC}" stroke-width="2"/>')
    p.append(icone("t:writing", 40, 334, 48, GLIC))
    rs.append(rot(104, 312, "“se três sessões voltarem acima do planejado, reduzimos e conversamos”", w=676, tam=21, cor=TINTA, peso=700, lh=1.3, serif=True))
    cx, cy = 1560, 340
    for a, ic in [(-90, "h:woman"), (30, "t:gauge"), (150, "t:message-circle")]:
        r = math.radians(a)
        p.append(icone(ic, cx + 62 * math.cos(r) - 20, cy + 62 * math.sin(r) - 20, 40, FOSF))
    p.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="none" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
    return slide("regras", 440, p, rs, eyebrow="Para qualquer instrumento", titulo="Quatro regras de uso")

# ---------------------------------------------------------------- 9.9

def reuniao_99():
    """9.9: a tela do software com um nome em vermelho, e três pessoas na sala sem saber de onde vem o número."""
    p = [svg_abre(1664, 380, "À esquerda, a tela de um software de monitoramento de um clube de rúgbi amador, com uma lista de jogadores e um deles em vermelho: 1,6, zona de perigo. À direita, a sala: o técnico quer tirá-lo do jogo de sábado; o jogador diz que está ótimo; o preparador físico não sabe responder. Embaixo: ninguém na sala sabe de onde vem o número")]
    rs = []
    p.append(f'<rect x="0" y="0" width="720" height="300" rx="18" fill="{TINTA}"/>')
    p.append(f'<rect x="20" y="20" width="680" height="260" rx="10" fill="#1E3346"/>')
    for j, (cor, v) in enumerate([(OXID, "0,9"), (OXID, "1,1"), (FOSF, "1,6"), (OXID, "1,0")]):
        y = 44 + j * 58
        p.append(f'<rect x="44" y="{y}" width="632" height="44" rx="8" fill="{FOSF if cor == FOSF else "#27415A"}"/>')
        p.append(f'<rect x="60" y="{y + 14}" width="{220 if j != 2 else 180}" height="16" rx="8" fill="{PAPEL}" opacity="{0.35 if cor != FOSF else 0.9}"/>')
        rs.append(rot(500, y + 8, v, w=160, tam=22, cor=PAPEL, peso=700, alinha="right"))
    rs.append(rot(300, 162, "zona de perigo", w=200, tam=18, cor=PAPEL, peso=700))
    rs.append(rot(0, 314, "clube de rúgbi amador · software comprado", w=720, tam=18, cor=MUDO, alinha="center"))
    pessoas = [("h:man", "o técnico", "“tira do jogo de sábado”", FOSF), ("h:running", "o jogador", "“estou ótimo”", OXID), ("h:person", "o preparador físico", "não sabe o que responder", MUDO)]
    for j, (ic, q, f, cor) in enumerate(pessoas):
        y = j * 100
        p.append(caixa(780, y, 884, 84, cor, CARTAO, esp=2, rx=14))
        p.append(icone(ic, 796, y + 14, 56, cor))
        rs += [rot(870, y + 12, q, w=760, tam=18, cor=MUDO, peso=700), rot(870, y + 40, f, w=760, tam=24, cor=TINTA, peso=700, serif=True)]
    p.append(caixa(780, 310, 884, 70, TINTA, TINTA, esp=0, rx=14))
    p.append(icone("t:question-mark", 800, 322, 44, PAPEL))
    rs.append(rot(860, 330, "ninguém na sala sabe de onde vem o número", w=780, tam=22, cor=PAPEL, peso=700))
    return slide("reuniao", 380, p, rs, eyebrow="Segunda-feira, reunião técnica", titulo="“Razão aguda e crônica, 1,6. Zona de perigo.”")


def origem_99():
    """9.9: os números do estudo do críquete e a conta que ele fazia, a semana atual contra a média das quatro."""
    p = [svg_abre(1664, 330, "À esquerda, três números do estudo de origem no críquete: 28 arremessadores rápidos de elite, 43 temporadas individuais, 6 anos de acompanhamento. À direita, a conta em esquema: quatro barras de semanas com a linha tracejada da média, e a semana atual bem acima dela, um pico de carga aguda; seta para lesão nas semanas seguintes"), defs(FOSF)]
    rs = []
    for j, (n, t, cor) in enumerate([("28", "arremessadores rápidos de elite", TINTA), ("43", "temporadas individuais", OXID), ("6 anos", "de acompanhamento", GLIC)]):
        y = j * 110
        rs += [rot(0, y, n, w=230, tam=64, cor=cor, peso=700, serif=True, alinha="right"), rot(256, y + 28, t, w=420, tam=22, cor=TINTA, peso=700)]
    p.append(caixa(760, 0, 904, 330, TINTA, CARTAO, esp=2, rx=16))
    B = 260
    for j, v in enumerate([110, 130, 120, 100]):
        x = 800 + j * 110
        p.append(f'<rect x="{x}" y="{B - v}" width="80" height="{v}" rx="6" fill="{CINZA}"/>')
    p.append(f'<rect x="1260" y="{B - 210}" width="80" height="210" rx="6" fill="{FOSF}"/>')
    p.append(f'<line x1="790" y1="{B - 115}" x2="1350" y2="{B - 115}" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    p.append(f'<line x1="780" y1="{B}" x2="1360" y2="{B}" stroke="{MUDO}" stroke-width="2"/>')
    rs += [rot(800, B + 10, "as últimas quatro semanas", w=410, tam=17, cor=MUDO, alinha="center"),
           rot(1230, B + 10, "semana atual", w=140, tam=17, cor=FOSF, peso=700, alinha="center"),
           rot(800, 100, "média", w=200, tam=17, cor=TINTA, peso=700)]
    p.append(seta(1370, 120, 1440, 120, FOSF, "m0", esp=4))
    rs += [rot(1450, 90, "mais lesão nas semanas seguintes", w=200, tam=21, cor=FOSF, peso=700, lh=1.25),
           rot(784, 296, "esquema", w=200, tam=16, cor=MUDO)]
    return slide("origem", 330, p, rs, eyebrow="De onde veio", titulo="Começou no críquete",
                 destaque="A semana atual comparada com a média das últimas quatro. Picos de carga aguda se associaram a mais lesão nas semanas seguintes.", destaque_cor="tinta",
                 fonte="Br J Sports Med 2014")


def convenceu_99():
    """9.9: quatro motivos, cada um com um desenho mínimo: a divisão, o semáforo, o aplicativo, a escada."""
    p = [svg_abre(1664, 300, "Quatro quadros. Simples: uma divisão, aguda sobre crônica. Colorido: um semáforo verde, amarelo e vermelho. Cabe em software: um celular com o gráfico, em aplicativo de clube e de relógio. Ideia de fundo sensata: uma escada de carga subindo aos poucos, sem saltos sobre uma base baixa")]
    rs = []
    for k, (t, x_, cor, fundo) in enumerate([("Simples", "uma divisão", OXID, OXID_T), ("Colorido", "verde, amarelo, vermelho", OXID, OXID_T),
                                              ("Cabe em software", "gráfico em aplicativo de clube e de relógio", GLIC, GLIC_T),
                                              ("Ideia de fundo sensata", "não dar saltos de carga sobre uma base baixa", TINTA, CARTAO)]):
        x = k * 420
        p.append(caixa(x, 0, 400, 300, cor, fundo, esp=2, rx=16))
        rs += [rot(x + 20, 16, t, w=360, tam=23, cor=cor, peso=700, serif=True), rot(x + 20, 224, x_, w=360, tam=19, cor=TINTA, lh=1.25)]
    rs += [rot(20, 80, "aguda", w=360, tam=26, cor=TINTA, peso=700, alinha="center", serif=True), rot(20, 150, "crônica", w=360, tam=26, cor=TINTA, peso=700, alinha="center", serif=True)]
    p.append(f'<line x1="100" y1="134" x2="300" y2="134" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<rect x="560" y="64" width="120" height="150" rx="20" fill="{TINTA}"/>')
    for j, c in enumerate([FOSF, GLIC, OXID]):
        p.append(f'<circle cx="620" cy="{94 + j * 45}" r="18" fill="{c}"/>')
    p.append(f'<rect x="980" y="60" width="100" height="160" rx="16" fill="{TINTA}"/>')
    p.append(f'<rect x="990" y="76" width="80" height="124" rx="6" fill="{PAPEL}"/>')
    for j, c in enumerate([OXID, OXID, GLIC, FOSF]):
        p.append(f'<rect x="{996 + j * 18}" y="{180 - j * 22}" width="14" height="{16 + j * 22}" rx="3" fill="{c}"/>')
    for j in range(5):
        p.append(f'<rect x="{1300 + j * 46}" y="{196 - j * 28}" width="46" height="{20 + j * 28}" fill="{TINTA}" opacity="{0.4 + j * 0.12:.2f}"/>')
    return slide("convenceu", 300, p, rs, eyebrow="Por que se espalhou", titulo="Quatro motivos compreensíveis",
                 destaque="Uma ideia sensata embalada numa conta que não aguenta o peso colocado nela.", destaque_cor="verm")


def causa_99():
    """9.9: o pico de carga andando junto com a lesão, e a seta causal que ninguém estimou."""
    p = [svg_abre(1664, 330, "À esquerda, o que os estudos mostram: dados observacionais em grupos específicos, em que o pico de carga e a lesão aparecem juntos, ligados por um traço de associação. À direita, o que não mostram: uma seta causal de mexer na razão para reduzir lesão, tracejada e com um ponto de interrogação; nenhum estudo estimou o efeito causal; sem base para usar em gestão de carga"), defs(FOSF)]
    rs = []
    p.append(caixa(0, 0, 800, 330, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "O que os estudos mostram", w=760, tam=24, cor=OXID, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:trending-up", "pico de carga"), ("t:first-aid-kit", "lesão")]):
        x = 60 + j * 440
        p.append(caixa(x, 90, 260, 110, OXID, CARTAO, esp=2, rx=14))
        p.append(icone(ic, x + 20, 118, 52, OXID))
        rs.append(rot(x + 84, 128, t, w=170, tam=22, cor=TINTA, peso=700))
    p.append(f'<line x1="330" y1="145" x2="490" y2="145" stroke="{OXID}" stroke-width="4" stroke-dasharray="4 8" stroke-linecap="round"/>')
    rs += [rot(330, 106, "andam juntos", w=160, tam=17, cor=OXID, peso=700, alinha="center"),
           rot(24, 236, "dados observacionais, em grupos específicos", w=760, tam=21, cor=TINTA, peso=700)]
    p.append(caixa(864, 0, 800, 330, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(888, 16, "O que não mostram", w=760, tam=24, cor=FOSF, peso=700, serif=True))
    p.append(caixa(904, 90, 260, 110, FOSF, CARTAO, esp=2, rx=14))
    p.append(caixa(1364, 90, 260, 110, FOSF, CARTAO, esp=2, rx=14))
    rs += [rot(904, 116, "mexer na razão", w=260, tam=22, cor=TINTA, peso=700, alinha="center"), rot(1364, 116, "reduz lesão", w=260, tam=22, cor=TINTA, peso=700, alinha="center")]
    p.append(f'<line x1="1176" y1="145" x2="1340" y2="145" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
    p.append(seta(1330, 145, 1352, 145, FOSF, "m0", esp=4))
    rs += [rot(1176, 92, "?", w=164, tam=36, cor=FOSF, peso=700, alinha="center"),
           rot(888, 226, "nenhum estudo estimou o efeito causal", w=760, tam=21, cor=TINTA, peso=700),
           rot(888, 266, "sem base para usar em gestão de carga", w=760, tam=21, cor=TINTA)]
    return slide("causa", 330, p, rs, eyebrow="Erro um", titulo="Tratar associação como causa",
                 destaque="Tirar o jogador pelo vermelho é tratar uma associação de outro esporte como mecanismo.", destaque_cor="tinta",
                 fonte="Int J Sports Physiol Perform 2020")


def janelas_99():
    """9.9: as janelas de 7 e 28 dias com interrogação, a régua contínua cortada em cores e as médias com peso no tempo."""
    p = [svg_abre(1664, 360, "No alto à esquerda, dois calendários, 7 dias e 28 dias, cada um com um ponto de interrogação: janelas sem fundamento declarado. No alto à direita, médias com peso no tempo: barras que diminuem para trás; melhora técnica, mas continua sendo uma razão com cortes. Embaixo, uma régua contínua da razão cortada em três cores, nos pontos 0,8, 1,3 e 1,5, que mudam de estudo para estudo; 1,49 e 1,51 lado a lado, um de cada lado do corte")]
    rs = []
    p.append(caixa(0, 0, 800, 170, GLIC, GLIC_T, esp=2, rx=16))
    for j, (t, n) in enumerate([("7 dias", 7), ("28 dias", 28)]):
        x = 24 + j * 300
        p.append(icone("t:calendar", x, 30, 64, GLIC))
        rs += [rot(x + 74, 34, t, w=160, tam=26, cor=GLIC, peso=700, serif=True), rot(x + 74, 70, "?", w=60, tam=28, cor=GLIC, peso=700)]
    rs.append(rot(24, 124, "janelas sem fundamento declarado", w=760, tam=20, cor=TINTA, peso=700))
    p.append(caixa(844, 0, 820, 170, OXID, OXID_T, esp=2, rx=16))
    for j in range(8):
        h = 80 * (0.75 ** j)
        p.append(f'<rect x="{1580 - j * 44}" y="{110 - h:.0f}" width="34" height="{h:.0f}" rx="4" fill="{OXID}"/>')
    rs += [rot(868, 20, "Médias com peso no tempo", w=480, tam=23, cor=OXID, peso=700, serif=True),
           rot(868, 66, "melhora técnica, mas continua sendo uma razão com cortes", w=400, tam=19, cor=TINTA, lh=1.3),
           rot(1250, 124, "o mais recente pesa mais", w=390, tam=16, cor=MUDO, alinha="right")]
    x0, x1, v0, v1 = 60, 1604, 0.5, 2.0
    X = lambda v: x0 + (v - v0) / (v1 - v0) * (x1 - x0)
    for a, b, c in [(0.5, 0.8, CINZA), (0.8, 1.3, OXID), (1.3, 1.5, GLIC), (1.5, 2.0, FOSF)]:
        p.append(f'<rect x="{X(a):.0f}" y="220" width="{X(b) - X(a):.0f}" height="40" fill="{c}"/>')
    for v in (0.8, 1.3, 1.5):
        p.append(f'<line x1="{X(v):.0f}" y1="206" x2="{X(v):.0f}" y2="274" stroke="{TINTA}" stroke-width="3"/>')
        rs.append(rot(X(v) - 40, 282, f"{v}".replace(".", ","), w=80, tam=20, cor=TINTA, peso=700, alinha="center"))
    for v, d in [(1.49, -1), (1.51, 1)]:
        p.append(f'<circle cx="{X(v):.0f}" cy="240" r="7" fill="{PAPEL}" stroke="{TINTA}" stroke-width="3"/>')
        rs.append(rot(X(v) + (8 if d > 0 else -128), 186, f"{v}".replace(".", ","), w=120, tam=18, cor=TINTA, peso=700, alinha="left" if d > 0 else "right"))
    rs.append(rot(0, 322, "uma régua contínua cortada em cores · cortes que mudam de estudo para estudo", w=1664, tam=18, cor=MUDO, alinha="center"))
    return slide("janelas", 360, p, rs, eyebrow="Erro três", titulo="Confiar em janelas e cortes que ninguém justificou",
                 destaque="1,49 fica fora da zona vermelha, 1,51 fica dentro. Cortar um número contínuo em cores joga informação fora.", destaque_cor="verm",
                 fonte="Int J Sports Physiol Perform 2020 · Br J Sports Med 2017")


def aleatorio_99():
    """9.9: a razão com a crônica verdadeira e com uma crônica sorteada, e associações parecidas com lesão."""
    p = [svg_abre(1664, 330, "Duas frações lado a lado. À esquerda, carga aguda dividida pela crônica verdadeira, a média real. À direita, carga aguda dividida por valores inventados, sorteados como num dado. Embaixo de cada uma, em esquema, uma barra de associação com lesão, de tamanho parecido nas duas")]
    rs = []
    for k, (t, den, cor, fundo, w) in enumerate([("Crônica verdadeira", "média real", TINTA, CARTAO, 520), ("Crônica sorteada", "valores inventados", GLIC, GLIC_T, 490)]):
        x0 = k * 844
        p.append(caixa(x0, 0, 820, 330, cor, fundo, esp=2, rx=16))
        rs += [rot(x0 + 24, 16, t, w=760, tam=24, cor=cor, peso=700, serif=True),
               rot(x0 + 60, 70, "aguda", w=320, tam=28, cor=TINTA, peso=700, alinha="center", serif=True),
               rot(x0 + 60, 132, den, w=320, tam=24, cor=cor, peso=700, alinha="center")]
        p.append(f'<line x1="{x0 + 90}" y1="120" x2="{x0 + 350}" y2="120" stroke="{TINTA}" stroke-width="4"/>')
        if k:
            p.append(icone("t:question-mark", x0 + 500, 70, 80, GLIC))
        else:
            p.append(icone("t:chart-bar", x0 + 500, 70, 80, TINTA))
        rs.append(rot(x0 + 24, 210, "associação com lesão", w=760, tam=19, cor=MUDO, peso=700))
        p.append(f'<rect x="{x0 + 24}" y="244" width="{w}" height="36" rx="8" fill="{FOSF}"/>')
    rs.append(rot(0, 298, "esquema", w=1640, tam=16, cor=MUDO, alinha="right"))
    return slide("aleatorio", 330, p, rs, eyebrow="Erro quatro", titulo="Acreditar que a carga crônica faz o trabalho",
                 destaque="Se trocar o denominador por qualquer número não muda o resultado, a razão não mede o que prometia.", destaque_cor="verm",
                 fonte="Sports Med 2021")


def fragil_99():
    """9.9: a ideia que continua de pé e a conta que caiu."""
    p = [svg_abre(1664, 320, "À esquerda, a ideia, que continua valendo: uma escada de carga construída aos poucos, com três marcas de certo: construir a carga aos poucos, evitar saltos, cuidar da volta após pausa. À direita, a conta, que caiu: um semáforo riscado, a razão colorida decidindo quem joga")]
    rs = []
    p.append(caixa(0, 0, 1000, 320, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(24, 16, "A ideia: continua valendo", w=960, tam=24, cor=OXID, peso=700, serif=True))
    for j in range(5):
        p.append(f'<rect x="{40 + j * 50}" y="{250 - j * 30}" width="50" height="{30 + j * 30}" fill="{OXID}" opacity="{0.4 + j * 0.12:.2f}"/>')
    for j, t in enumerate(["construir a carga aos poucos", "evitar saltos", "cuidar da volta após pausa"]):
        y = 90 + j * 70
        p.append(icone("t:check", 340, y, 40, OXID))
        rs.append(rot(396, y + 4, t, w=580, tam=24, cor=TINTA, peso=700))
    p.append(caixa(1040, 0, 624, 320, FOSF, FOSF_T, esp=2, rx=16))
    rs.append(rot(1064, 16, "A conta: caiu", w=580, tam=24, cor=FOSF, peso=700, serif=True))
    p.append(f'<rect x="1100" y="80" width="100" height="200" rx="20" fill="{TINTA}"/>')
    for j, c in enumerate([FOSF, GLIC, OXID]):
        p.append(f'<circle cx="1150" cy="{120 + j * 60}" r="22" fill="{c}" opacity="0.5"/>')
    p.append(f'<line x1="1080" y1="290" x2="1220" y2="70" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
    rs.append(rot(1250, 130, "a razão colorida decidindo quem joga", w=390, tam=24, cor=TINTA, peso=700, lh=1.3))
    return slide("fragil", 320, p, rs, eyebrow="A ideia da aula", titulo="A ideia por trás estava certa. A conta estava frágil.")


def transplante_99():
    """9.9: do monitoramento diário da elite para a semana que quebra do amador, e a mudança semanal em porcentagem."""
    p = [svg_abre(1664, 360, "À esquerda, os dados de origem: atletas profissionais, monitoramento diário, rotina estável, uma fileira de dias todos preenchidos. Uma seta riscada para o amador: trabalho, sono ruim, semana que quebra, dados incompletos, a fileira de dias com falhas. À direita, uma medida simples: barras da distância semanal de um corredor com a mudança em porcentagem escrita sobre cada uma; diz mais"), defs(FOSF)]
    rs = []
    import math
    for k, (t, itens, cor, fundo, falha) in enumerate([("Dados de origem", "atletas profissionais · monitoramento diário · rotina estável", TINTA, CARTAO, set()),
                                                        ("O amador", "trabalho, sono ruim, semana que quebra · dados incompletos", GLIC, GLIC_T, {2, 3, 7, 9, 10, 13})]):
        y0 = k * 190
        p.append(caixa(0, y0, 900, 170, cor, fundo, esp=2, rx=16))
        rs += [rot(24, y0 + 14, t, w=400, tam=23, cor=cor, peso=700, serif=True), rot(24, y0 + 120, itens, w=860, tam=19, cor=TINTA, peso=700)]
        for d in range(14):
            cx = 60 + d * 58
            p.append(f'<rect x="{cx - 20}" y="{y0 + 62}" width="40" height="40" rx="8" fill="{PAPEL if d in falha else cor}" stroke="{cor}" stroke-width="2"/>')
    p.append(caixa(940, 0, 724, 360, OXID, OXID_T, esp=2, rx=16))
    rs.append(rot(964, 14, "Para o amador, uma medida simples diz mais", w=680, tam=22, cor=OXID, peso=700, serif=True))
    B = 300
    for j, (km, pc) in enumerate([(20, ""), (22, "+10%"), (24, "+9%"), (32, "+33%")]):
        x = 1000 + j * 160
        h = km * 6
        p.append(f'<rect x="{x}" y="{B - h}" width="110" height="{h}" rx="6" fill="{FOSF if j == 3 else OXID}"/>')
        if pc:
            rs.append(rot(x - 20, B - h - 32, pc, w=150, tam=21, cor=FOSF if j == 3 else TINTA, peso=700, alinha="center"))
    rs.append(rot(964, B + 14, "distância semanal · semanas ilustrativas", w=680, tam=17, cor=MUDO))
    return slide("transplante", 360, p, rs, eyebrow="Erro cinco", titulo="Transplantar a elite e deixar o número decidir",
                 destaque="874 corredores iniciantes: aumentos acima de 30% em duas semanas se associaram a alguns tipos de lesão. Também é associação, mas o corredor entende.", destaque_cor="tinta",
                 fonte="J Orthop Sports Phys Ther 2014")


def fica_99():
    """9.9: quatro semanas descritas sem cor, com a média anterior e a mudança, e os três momentos a vigiar."""
    p = [svg_abre(1664, 360, "À esquerda, quatro semanas de carga em barras neutras, sem zona verde nem vermelha: 1.800, 1.900, 2.000 e 2.700. Sobre cada barra, a média das semanas anteriores, tracejada, e a mudança: sem base, mais 6%, mais 8%, mais 42%. Exemplo ilustrativo. À direita, três momentos a vigiar: salto de volume, acúmulo sem descanso, volta depois de pausa")]
    rs = []
    B, k = 290, 0.09
    for j, (c, m, pc) in enumerate([(1800, None, "sem base"), (1900, 1800, "+6%"), (2000, 1850, "+8%"), (2700, 1900, "+42%")]):
        x = 40 + j * 220
        p.append(f'<rect x="{x}" y="{B - c * k:.0f}" width="150" height="{c * k:.0f}" rx="6" fill="{TINTA}" opacity="{0.9 if j == 3 else 0.55}"/>')
        if m:
            p.append(f'<line x1="{x - 10}" y1="{B - m * k:.0f}" x2="{x + 160}" y2="{B - m * k:.0f}" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
        rs += [rot(x - 20, B - c * k - 34, pc, w=190, tam=22 if j == 3 else 19, cor=TINTA, peso=700, alinha="center"),
               rot(x - 20, B + 10, f"semana {j + 1} · {c:,}".replace(",", "."), w=190, tam=17, cor=TINTA, alinha="center")]
    rs.append(rot(40, 336, "tracejado: média das semanas anteriores, sem a atual", w=860, tam=16, cor=MUDO))
    p.append(caixa(960, 0, 704, 360, TINTA, CARTAO, esp=2, rx=16))
    rs.append(rot(984, 16, "Três momentos a vigiar", w=660, tam=24, cor=TINTA, peso=700, serif=True))
    for j, (ic, t) in enumerate([("t:trending-up", "salto de volume"), ("t:stairs", "acúmulo sem descanso"), ("t:refresh", "volta depois de pausa")]):
        y = 80 + j * 66
        p.append(icone(ic, 984, y, 44, TINTA))
        rs.append(rot(1046, y + 8, t, w=600, tam=22, cor=TINTA, peso=700))
    rs.append(rot(984, 290, "e perguntar por sono, dor e nota de esforço", w=660, tam=20, cor=OXID, peso=700))
    return slide("fica", 360, p, rs, eyebrow="O que fica", titulo="Descrever sem colorir, decidir com contexto",
                 fonte="Exemplo ilustrativo, sem dados reais")

# ---------------------------------------------------------------- aplicação

LICOES = {"09-01": [percurso_91, roteiro_91, especificidade_91, dose_91, variacao_91, reversibilidade_91, teoria_91, perguntas_91, ciclista_91],
          "09-02": [pedidos_92, funciona_92, igualado_92, acontece_92, picos_92, sessoes_92, objetivo_92, minima_92, aplicado_92, sinais_92],
          "09-03": [ficha_93, roteiro_93, objetivo_93, carga_93, crescer_93, frequencia_93, esforco_93, ajustes_93, servico_93, registro_93],
          "09-04": [lance_94, gols_94, tres_94, agilidade_94, descansado_94, treno_94, dose_94, protege_94, resumo_94],
          "09-05": [planilha_95, tipos_95, ambos_95, elite_95, ensaio_95, paga_95, cinzenta_95, conta_95, plano_95, acompanhar_95],
          "09-06": [telas_96, roteiro_96, ancoras_96, poucas_96, ancorada_96, borg_96, escalas_96, medidas_96, tabela_96, desempate_96],
          "09-07": [coletes_97, externa_97, amostragem_97, limiar_97, campo_97, acelerometro_97, fora_97, vale_97, pulso_97, correcoes_97],
          "09-08": [propostas_98, quatro_98, conta_98, condicoes_98, fc_98, vfc_98, questionario_98, terceira_98, cenarios_98, regras_98],
          "09-09": [reuniao_99, origem_99, convenceu_99, causa_99, janelas_99, aleatorio_99, fragil_99, transplante_99, fica_99]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
