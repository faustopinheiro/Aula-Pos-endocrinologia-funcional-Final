"""Desenhos que substituem os slides de texto do Módulo 3 (cartões, colunas, listas, tabelas e números).
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


# ---------------------------------------------------------------- 3.1

def laudos():
    """3.1: quatro laudos com o valor fora da faixa, e quem está por trás de cada um."""
    p = [svg_abre(1664, 430, "Quatro laudos, cada um com o valor fora da faixa de referência: testosterona baixa num homem de quarenta e poucos anos que treina força cinco vezes por semana, TSH alterado numa corredora em restrição, cortisol fora da faixa num plantonista e IGF-1 baixo num nadador master. Embaixo de cada laudo, a pessoa e o contexto")]
    itens = [("Testosterona", "baixa", 0.12, "t:barbell", "quarenta e poucos anos, força cinco vezes por semana", FOSF),
             ("TSH", "alterado", 0.9, "t:run", "corredora em restrição há meses", GLIC),
             ("Cortisol", "fora da faixa", 0.94, "t:moon", "plantonista", OXID),
             ("IGF-1", "baixo", 0.1, "t:swimming", "nadador master que quer recuperar melhor", AZUL)]
    rs = []
    for i, (h, est, pos, ic, ctx, cor) in enumerate(itens):
        x = i * 424
        p.append(caixa(x, 0, 392, 214, BORDA, CARTAO, esp=2, rx=10))
        p.append(f'<rect x="{x}" y="0" width="392" height="10" rx="4" fill="{cor}"/>')
        # faixa de referência e o valor
        p.append(f'<rect x="{x+40}" y="132" width="312" height="18" rx="9" fill="{CINZA}"/>')
        p.append(f'<rect x="{x+118}" y="132" width="156" height="18" rx="0" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        cx = x + 40 + pos * 312
        p.append(f'<circle cx="{cx:.0f}" cy="141" r="15" fill="{FOSF}" stroke="{CARTAO}" stroke-width="3"/>')
        rs += [rot(x + 24, 28, h, w=344, tam=32, cor=TINTA, peso=700, serif=True),
               rot(x + 24, 72, est, w=344, tam=24, cor=FOSF, peso=700),
               rot(x + 118, 162, "faixa", w=156, tam=20, cor=OXID, alinha="center")]
        # a pessoa
        p.append(f'<line x1="{x+196}" y1="222" x2="{x+196}" y2="252" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
        p.append(f'<circle cx="{x+196}" cy="300" r="44" fill="{PAPEL}" stroke="{cor}" stroke-width="3"/>')
        p.append(icone(ic, x + 170, 274, 52, cor))
        rs.append(rot(x + 10, 356, ctx, w=372, tam=22, cor=TINTA, alinha="center", lh=1.25))
    return slide("laudos", 430, p, rs,
                 eyebrow="Quatro exames", titulo="O mesmo número, duas leituras opostas",
                 destaque="Disfunção do eixo, ou eixo funcionando certo diante do contexto que a pessoa criou?",
                 destaque_cor="verm")


def pares():
    """3.1: o par de cada eixo, como uma linha de comando que sobe e desce."""
    p = [svg_abre(1664, 440, "Quatro eixos em linhas. Em cada um, o sinal de cima comanda o hormônio final: LH e FSH comandam a testosterona; LH e FSH, com o ciclo, comandam o estradiol; TSH comanda o T4 livre; ACTH comanda o cortisol, com horário. À direita, o sinal que aponta para a própria glândula: LH alto, FSH alto, TSH alto, ACTH alto"), defs(TINTA, FOSF)]
    linhas_ = [("Gonadal masculino", "LH e FSH", "Testosterona total", "LH alto"),
               ("Gonadal feminino", "LH, FSH e o ciclo", "Estradiol", "FSH alto"),
               ("Tireoidiano", "TSH", "T4 livre", "TSH alto"),
               ("Adrenal", "ACTH", "Cortisol, com horário", "ACTH alto")]
    rs = [rot(360, 0, "sinal de cima", w=340, tam=22, cor=AZUL, peso=700, alinha="center"),
          rot(800, 0, "hormônio final", w=380, tam=22, cor=OXID, peso=700, alinha="center"),
          rot(1270, 0, "aponta para a glândula quando", w=394, tam=22, cor=FOSF, peso=700, alinha="center")]
    for i, (eixo, sinal, final, alto) in enumerate(linhas_):
        y = 44 + i * 100
        p.append(f'<rect x="0" y="{y}" width="1664" height="84" rx="12" fill="{PAPEL if i % 2 == 0 else CARTAO}"/>')
        p.append(caixa(360, y + 10, 340, 64, AZUL, AZUL_T, esp=3, rx=32))
        p.append(seta(708, y + 42, 790, y + 42, TINTA, "m0", esp=4))
        p.append(caixa(800, y + 10, 380, 64, OXID, OXID_T, esp=3, rx=32))
        p.append(f'<line x1="1196" y1="{y+42}" x2="1262" y2="{y+42}" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
        p.append(icone("t:arrow-up-right", 1300, y + 18, 48, FOSF))
        rs += [rot(20, y + 26, eixo, w=330, tam=26, cor=TINTA, peso=700),
               rot(360, y + 26, sinal, w=340, tam=24, cor=AZUL, peso=600, alinha="center"),
               rot(800, y + 26, final, w=380, tam=24, cor=OXID, peso=600, alinha="center"),
               rot(1360, y + 26, alto, w=300, tam=26, cor=FOSF, peso=700)]
    return slide("pares", 440, p, rs,
                 eyebrow="O que pedir", titulo="O par em cada eixo",
                 destaque="Se o TSH não está alto, a fadiga não é hipotireoidismo primário. O TSH rastreia bem, e não fecha a história em quem está em restrição.",
                 destaque_cor="ambar")


def anamnese():
    """3.1: a bifurcação entre supressão funcional e causa central, decidida pela história."""
    p = [svg_abre(1664, 420, "No centro, o achado: hormônio final baixo com sinal de cima baixo ou normal. Dele saem dois caminhos. À esquerda, supressão funcional: restrição energética e perda de peso, sono curto crônico, volume alto com pouca comida, doença recente ou estresse prolongado. À direita, central verdadeiro: cefaleia e alteração visual, outros eixos alterados fora de proporção, trauma ou cirurgia na cabeça, hormônio exógeno"), defs(OXID, FOSF)]
    p.append(caixa(482, 0, 700, 64, TINTA, PAPEL, esp=3, rx=16))
    rs = [rot(492, 14, "Final baixo, sinal de cima baixo ou normal", w=680, tam=26, cor=TINTA, peso=700, alinha="center", serif=True),
          rot(612, 84, "a pergunta vai para a história", w=440, tam=22, cor=MUDO, alinha="center")]
    p.append(f'<path d="M 600 64 C 600 120, 420 100, 420 150" fill="none" stroke="{OXID}" stroke-width="5" marker-end="url(#m0)"/>')
    p.append(f'<path d="M 1064 64 C 1064 120, 1244 100, 1244 150" fill="none" stroke="{FOSF}" stroke-width="5" marker-end="url(#m1)"/>')
    lados = [(0, "Supressão funcional", OXID, OXID_T,
              [("t:salad", "restrição energética, perda de peso"), ("t:zzz", "sono curto crônico"),
               ("t:barbell", "volume alto com pouca comida"), ("t:mood-sick", "doença recente, estresse prolongado")]),
             (852, "Central verdadeiro", FOSF, FOSF_T,
              [("t:eye", "cefaleia, alteração visual"), ("t:adjustments-horizontal", "outros eixos alterados fora de proporção"),
               ("t:first-aid-kit", "trauma ou cirurgia na cabeça"), ("t:pill", "hormônio exógeno, declarado ou não")])]
    for x0, tit, cor, fundo, itens in lados:
        p.append(caixa(x0, 164, 812, 256, cor, fundo, esp=3, rx=16))
        rs.append(rot(x0 + 24, 176, tit, w=760, tam=28, cor=cor, peso=700, serif=True))
        for k, (ic, t) in enumerate(itens):
            cx, cy = x0 + 24 + (k % 2) * 396, 228 + (k // 2) * 94
            p.append(f'<circle cx="{cx+30}" cy="{cy+30}" r="30" fill="{CARTAO}" stroke="{cor}" stroke-width="2"/>')
            p.append(icone(ic, cx + 12, cy + 12, 36, cor))
            rs.append(rot(cx + 72, cy + 2, t, w=310, tam=22, cor=TINTA, lh=1.25))
    return slide("anamnese", 470, p, rs,
                 eyebrow="Passo dois", titulo="Quem separa central de funcional é a anamnese",
                 destaque="Abaixo de 30 kcal por kg de massa magra por dia, em cinco dias, os pulsos de LH ficaram 10 a 32% menos frequentes. O hipotálamo lê a escassez rápido.",
                 destaque_cor="ambar", fonte="Loucks e Thuma, Journal of Clinical Endocrinology and Metabolism 2003 · 29 mulheres jovens com ciclo regular")


def ficha():
    """3.1: a ficha de coleta como um formulário de seis campos."""
    p = [svg_abre(1664, 460, "Uma ficha de coleta com seis campos para preencher: horário, horas desde o último treino, quão duro foi esse treino, fase do ciclo quando for o caso, tempo de jejum e o que comeu na véspera, e o que mudou em três meses. Ao lado, duas fotos da mesma pessoa com luz diferente")]
    p.append(caixa(0, 0, 1120, 460, TINTA, CARTAO, esp=2, rx=14))
    p.append(f'<rect x="0" y="0" width="1120" height="64" rx="14" fill="{TINTA}"/><rect x="0" y="40" width="1120" height="24" fill="{TINTA}"/>')
    rs = [rot(28, 14, "Ficha de coleta", w=600, tam=28, cor=PAPEL, peso=700, serif=True)]
    campos = [("t:clock", "Horário", "testosterona das 15 h não é a das 7 h"),
              ("t:hourglass", "Horas desde o último treino", "a manhã seguinte à sessão pesada não é base"),
              ("t:gauge", "Quão duro foi esse treino", "quem sabe é o preparador físico"),
              ("t:calendar", "Fase do ciclo", "quando for o caso"),
              ("t:coffee", "Tempo de jejum", "e o que comeu na véspera"),
              ("t:refresh", "O que mudou em três meses", "peso, sono, carga, trabalho, doença")]
    for k, (ic, t, x) in enumerate(campos):
        cx, cy = 28 + (k % 2) * 546, 90 + (k // 2) * 122
        p.append(f'<rect x="{cx}" y="{cy+6}" width="34" height="34" rx="6" fill="{CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
        p.append(icone(ic, cx + 48, cy + 2, 42, AZUL))
        p.append(f'<line x1="{cx+104}" y1="{cy+96}" x2="{cx+516}" y2="{cy+96}" stroke="{CINZA}" stroke-width="2"/>')
        rs += [rot(cx + 104, cy, t, w=412, tam=24, cor=TINTA, peso=700),
               rot(cx + 104, cy + 36, x, w=412, tam=20, cor=MUDO, lh=1.2)]
    # duas fotos com luz diferente
    for j, (fundo, t) in enumerate([("#F4EAD6", "coleta às 7 h, descansado"), ("#C9CFD4", "coleta às 15 h, depois do treino")]):
        x = 1180 + j * 250
        p.append(f'<rect x="{x}" y="60" width="220" height="260" rx="10" fill="{fundo}" stroke="{MUDO}" stroke-width="2"/>')
        p.append(icone("t:user", x + 50, 110, 120, TINTA))
        rs.append(rot(x, 332, t, w=220, tam=20, cor=TINTA, alinha="center", lh=1.2))
    rs.append(rot(1180, 400, "mesma pessoa, fotos diferentes", w=470, tam=22, cor=FOSF, peso=700, alinha="center"))
    return slide("ficha", 460, p, rs,
                 eyebrow="Passo três", titulo="Registre a condição de coleta",
                 destaque="Sem a ficha, você compara duas fotos tiradas com luz diferente e atribui a diferença à pessoa.",
                 destaque_cor="tinta")


def cinco():
    """3.1: um centro que decide e cinco sistemas que executam na mesma direção."""
    p = [svg_abre(1664, 460, "O hipotálamo no centro, com cinco linhas saindo para cinco sistemas: cortisol, mobilização; gonadal, investimento, o primeiro a ser cortado; tireoidiano, velocidade, com oitenta por cento do T3 nascendo nos tecidos; GH e IGF-1, reparo acoplado ao sono profundo; sinais periféricos, informação, insulina, leptina e grelina. A periferia informa, o hipotálamo decide, os outros executam"), defs(MUDO)]
    cx, cy = 832, 250
    sist = [("Cortisol", "mobilização: energia agora", FOSF, "t:bolt"),
            ("Gonadal", "investimento: o primeiro a ser cortado", GLIC, "t:seedling"),
            ("Tireoidiano", "velocidade: 80% do T3 nasce nos tecidos", OXID, "t:gauge"),
            ("GH e IGF-1", "reparo, acoplado ao sono profundo", AZUL, "t:tools"),
            ("Sinais periféricos", "informação: insulina, leptina, grelina", TINTA, "t:messages")]
    pos = [(0, 0), (1144, 0), (0, 320), (1144, 320), (572, 380)]
    rs = []
    for (x, y), (t, d, cor, ic) in zip(pos, sist):
        w = 520
        bx, by = x + w / 2, y + 40
        p.append(f'<line x1="{cx}" y1="{cy}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{CINZA}" stroke-width="4"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="96" fill="{TINTA}"/>')
    rs += [rot(cx - 90, cy - 38, "Hipotálamo", w=180, tam=26, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(cx - 90, cy + 4, "decide uma vez", w=180, tam=20, cor=PAPEL, alinha="center")]
    for (x, y), (t, d, cor, ic) in zip(pos, sist):
        w, h = 520, 80
        p.append(caixa(x, y, w, h, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, x + w - 62, y + 16, 46, cor))
        rs += [rot(x + 20, y + 6, t, w=w - 90, tam=26, cor=cor, peso=700),
               rot(x + 20, y + 42, d, w=w - 90, tam=20, cor=TINTA)]
    rs += [rot(0, 422, "um eixo sozinho alterado: desconfie de doença", w=560, tam=22, cor=FOSF, peso=700),
           rot(1104, 422, "vários na mesma direção: desconfie de contexto", w=560, tam=22, cor=OXID, peso=700, alinha="right")]
    return slide("cinco", 460, p, rs,
                 eyebrow="Passo quatro", titulo="Um eixo sozinho, ou vários na mesma direção?",
                 destaque="Não são cinco decisões independentes. É uma decisão executada em cinco lugares.",
                 destaque_cor="petr", fonte="Bianco e Kim, Journal of Clinical Investigation 2006")


# ---------------------------------------------------------------- 3.2

def vilao():
    """3.2: as cinco acusações e o raciocínio que parece prudente."""
    p = [svg_abre(1664, 440, "À esquerda, o cortisol no centro com cinco acusações ligadas a ele: engorda, destrói músculo, causa barriga, derruba a imunidade, acaba com o sono. À direita, o raciocínio em três passos: o cortisol é o problema, então baixar o cortisol, então a solução; o último passo está riscado, porque sem cortisol não se vive"), defs(TINTA)]
    cx, cy = 360, 220
    acus = ["engorda", "destrói músculo", "causa barriga", "derruba a imunidade", "acaba com o sono"]
    pos = [(0, 0), (500, 20), (0, 360), (470, 380), (-10, 180)]
    pos = [(10, 10), (470, 30), (10, 374), (450, 374), (0, 192)]
    rs = []
    for (x, y), t in zip(pos, acus):
        w = 240 if len(t) < 16 else 270
        p.append(f'<line x1="{cx}" y1="{cy}" x2="{x + w/2:.0f}" y2="{y + 28}" stroke="{CINZA}" stroke-width="3"{TRACO}/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="{FOSF}"/>')
    rs.append(rot(cx - 90, cy - 18, "Cortisol", w=180, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
    for (x, y), t in zip(pos, acus):
        w = 240 if len(t) < 16 else 270
        p.append(caixa(x, y, w, 56, FOSF, FOSF_T, esp=2, rx=28))
        rs.append(rot(x, y + 13, t, w=w, tam=22, cor=FOSF, peso=700, alinha="center"))
    passos = [("o cortisol é o problema", TINTA, False), ("então baixar o cortisol", TINTA, False), ("é a solução", FOSF, True)]
    for k, (t, cor, risca) in enumerate(passos):
        y = 20 + k * 140
        p.append(caixa(900, y, 520, 90, cor, CARTAO, esp=3, rx=14))
        rs.append(rot(900, y + 26, t, w=520, tam=28, cor=cor, peso=700, alinha="center", serif=True))
        if k < 2:
            p.append(seta(1160, y + 94, 1160, y + 132, TINTA, "m0", esp=4))
        if risca:
            p.append(f'<line x1="920" y1="{y+80}" x2="1400" y2="{y+10}" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
    rs.append(rot(1440, 300, "parece prudente e está errado", w=224, tam=24, cor=FOSF, peso=700, lh=1.25))
    rs.append(rot(900, 408, "Sem cortisol, não se vive.", w=764, tam=26, cor=TINTA, peso=700))
    return slide("vilao", 440, p, rs,
                 eyebrow="O hormônio mais caluniado", titulo="Baixar o cortisol parece prudente e está errado",
                 destaque="Insuficiência adrenal não tratada é fatal. O problema nunca foi o hormônio existir.",
                 destaque_cor="verm")


def funcao():
    """3.2: o que o cortisol faz, em quatro saídas, e por que ele é catabólico."""
    p = [svg_abre(1664, 430, "Um estímulo aciona o cortisol, que tem quatro saídas: mais glicose disponível no sangue; gordura e aminoácido mobilizados do tecido; inflamação contida, para não consumir recursos demais; tônus vascular, para a pressão não cair quando é preciso correr. Embaixo, o músculo como reserva que vira combustível na emergência"), defs(TINTA, GLIC)]
    p.append(caixa(0, 150, 260, 110, TINTA, PAPEL, esp=3, rx=16))
    rs = [rot(0, 170, "estímulo", w=260, tam=28, cor=TINTA, peso=700, alinha="center", serif=True),
          rot(0, 210, "treino, susto, jejum", w=260, tam=20, cor=MUDO, alinha="center")]
    p.append(seta(268, 205, 350, 205, TINTA, "m0", esp=5))
    p.append(f'<circle cx="460" cy="205" r="100" fill="{FOSF}"/>')
    rs += [rot(370, 170, "Cortisol", w=180, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(370, 212, "energia agora", w=180, tam=20, cor=PAPEL, alinha="center")]
    saidas = [("t:droplet", "Glicose", "mais glicose disponível no sangue", GLIC),
              ("t:arrows-exchange", "Substrato", "gordura e aminoácido mobilizados do tecido", GLIC),
              ("t:flame", "Inflamação", "contida, para não consumir recursos demais", OXID),
              ("t:gauge", "Tônus vascular", "a pressão não cai quando você precisa correr", AZUL)]
    for k, (ic, t, x, cor) in enumerate(saidas):
        y = k * 100
        p.append(f'<path d="M 560 205 C 640 205, 640 {y+40}, 720 {y+40}" fill="none" stroke="{cor}" stroke-width="4"/>')
        p.append(caixa(730, y, 934, 80, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, 750, y + 16, 48, cor))
        rs += [rot(820, y + 8, t, w=820, tam=26, cor=cor, peso=700),
               rot(820, y + 44, x, w=820, tam=22, cor=TINTA)]
    p.append(f'<rect x="0" y="330" width="560" height="100" rx="14" fill="{GLIC_T}"/>')
    p.append(icone("t:barbell", 20, 350, 60, GLIC))
    p.append(seta(96, 380, 150, 380, GLIC, "m1", esp=4))
    p.append(icone("t:flame", 160, 350, 60, GLIC))
    rs.append(rot(240, 344, "músculo é reserva: na emergência, reserva vira combustível", w=310, tam=21, cor=TINTA, lh=1.25))
    return slide("funcao", 430, p, rs,
                 eyebrow="Para que ele existe", titulo="Deixar energia disponível agora",
                 destaque="Acionado o dia inteiro: mais sinal catabólico e menos permissão para reparar.",
                 destaque_cor="verm")


def cuidados():
    """3.2: a volta ao basal entre estímulos, e o débito empilhado quando ela não acontece."""
    import math
    p = [svg_abre(1664, 440, "Dois dias esquemáticos de cortisol com três sessões de treino. No de cima, cada sessão sobe o cortisol e ele volta ao basal antes da próxima. No de baixo, as sessões chegam antes da volta, somadas a jejum e pico da manhã, e a curva fica empilhada num patamar alto")]
    rs = []
    def curva(y0, picos, cor, largura):
        pts = []
        for i in range(0, 1301, 10):
            v = 0
            for c, a in picos:
                if i >= c:
                    v += a * math.exp(-(i - c) / largura) * (1 - math.exp(-(i - c) / 25))
            pts.append((i + 300, y0 - v))
        d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
        p.append(f'<line x1="300" y1="{y0}" x2="1620" y2="{y0}" stroke="{CINZA}" stroke-width="2"{TRACO}/>')
        p.append(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="6" stroke-linejoin="round"/>')
        for c, a in picos:
            p.append(f'<rect x="{c + 300}" y="{y0 + 10}" width="60" height="14" rx="7" fill="{TINTA}"/>')
    curva(170, [(60, 110), (500, 110), (940, 110)], OXID, 70)
    curva(400, [(60, 90), (230, 90), (400, 90), (570, 90)], FOSF, 260)
    rs += [rot(0, 60, "Volta ao basal antes do próximo estímulo", w=280, tam=24, cor=OXID, peso=700, lh=1.25),
           rot(0, 300, "Não volta: pico da manhã, jejum e sessão dura na mesma janela", w=280, tam=22, cor=FOSF, peso=700, lh=1.25),
           rot(1310, 30, "subir no exercício é a resposta certa", w=340, tam=22, cor=TINTA, lh=1.25),
           rot(1500, 136, "basal", w=120, tam=20, cor=MUDO, alinha="right"),
           rot(1150, 250, "débito empilhado", w=460, tam=26, cor=FOSF, peso=700, alinha="right"),
           rot(300, 424 - 0, "barras escuras: sessões de treino", w=600, tam=20, cor=MUDO)]
    return slide("cuidados", 440, p, rs,
                 eyebrow="Como usar o dado sem exagerar", titulo="O que importa é a volta, não o pico",
                 destaque="A intervenção: parte do volume abaixo do limiar. Sessenta por cento é princípio, não régua: foram doze homens.",
                 destaque_cor="ambar", fonte="Esquema, sem valores medidos")


def investigar():
    """3.2: os dois extremos que existem, nas pontas de uma régua, e o meio que não abre investigação."""
    p = [svg_abre(1664, 440, "Uma régua de cortisol, de pouco a muito. Na ponta esquerda, insuficiência, uma urgência: pressão baixa e fraqueza progressiva, escurecimento de pele e mucosas, vontade intensa de sal e náusea, perda de peso sem intenção e sódio baixo. Na ponta direita, excesso: fraqueza proximal, estrias violáceas largas, hipertensão de difícil controle e glicose fora de proporção, pele frágil e fratura sem trauma. No meio, cansaço e gordura abdominal sozinhos, que não abrem investigação"), defs(MUDO)]
    p.append(f'<defs><linearGradient id="rg" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{FOSF}"/><stop offset="0.3" stop-color="{CINZA}"/><stop offset="0.7" stop-color="{CINZA}"/><stop offset="1" stop-color="{GLIC}"/></linearGradient></defs>')
    p.append(f'<rect x="0" y="0" width="1664" height="26" rx="13" fill="url(#rg)"/>')
    rs = [rot(0, 36, "pouco cortisol", w=300, tam=22, cor=FOSF, peso=700),
          rot(1364, 36, "muito cortisol", w=300, tam=22, cor=GLIC, peso=700, alinha="right")]
    lados = [(0, "Insuficiência: urgência", FOSF, FOSF_T, ["pressão baixa, fraqueza progressiva", "escurecimento de pele e mucosas", "vontade intensa de sal, náusea", "perda de peso sem intenção, sódio baixo"],
              ["t:trending-down", "t:sun", "t:salad", "t:scale"]),
             (1064, "Excesso", GLIC, GLIC_T, ["fraqueza proximal: levantar da cadeira sem os braços", "estrias violáceas largas", "hipertensão difícil, glicose fora de proporção", "pele frágil, fratura sem trauma"],
              ["t:stairs", "t:ruler-measure", "t:heartbeat", "t:bandaged" if False else "t:first-aid-kit"])]
    for x0, tit, cor, fundo, itens, ics in lados:
        p.append(caixa(x0, 80, 600, 360, cor, fundo, esp=3, rx=16))
        rs.append(rot(x0 + 24, 94, tit, w=560, tam=28, cor=cor, peso=700, serif=True))
        for k, (t, ic) in enumerate(zip(itens, ics)):
            y = 150 + k * 70
            p.append(icone(ic, x0 + 24, y + 4, 40, cor))
            rs.append(rot(x0 + 80, y, t, w=500, tam=22, cor=TINTA, lh=1.2))
    p.append(caixa(640, 170, 384, 190, MUDO, PAPEL, esp=2, rx=16))
    p.append(icone("t:battery-1", 700, 196, 56, MUDO))
    p.append(icone("t:scale", 868, 196, 56, MUDO))
    rs += [rot(660, 262, "cansaço e gordura abdominal, sozinhos", w=344, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.2),
           rot(660, 318, "não abrem investigação", w=344, tam=20, cor=MUDO, alinha="center")]
    return slide("investigar", 440, p, rs,
                 eyebrow="Quando investigar de verdade", titulo="Os dois extremos que existem",
                 destaque="E cansaço e gordura abdominal são justamente os dois que trazem a pessoa pedindo o exame.",
                 destaque_cor="tinta")


def fadiga():
    """3.2: o funil da revisão sistemática, e o que o rótulo esconde."""
    p = [svg_abre(1664, 420, "À esquerda, um funil: 3.470 artigos triados, 58 estudos analisados de perto, nenhuma base para a entidade fadiga adrenal. À direita, uma etiqueta escrita fadiga adrenal cobrindo sete causas que ficam sem ser procuradas: sono curto, apneia, pouca energia disponível, ferro, tireoide, medicamento e depressão")]
    funil = [(0, 700, "3.470", "artigos triados", TINTA), (110, 520, "58", "estudos analisados de perto", AZUL), (220, 340, "0", "base para a entidade", FOSF)]
    rs = []
    for y, w, n, t, cor in funil:
        x = (700 - w) / 2
        p.append(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="96" rx="12" fill="{cor}"/>')
        rs += [rot(x + 16, y + 14, n, w=160 if w > 300 else 90, tam=44, cor=PAPEL, peso=700, serif=True),
               rot(x + (180 if w > 300 else 90), y + 30, t, w=w - (200 if w > 300 else 100), tam=22 if w > 300 else 20, cor=PAPEL, peso=600, lh=1.15)]
    rs.append(rot(0, 340, "revisão sistemática, 2016", w=700, tam=22, cor=MUDO, alinha="center"))
    causas = ["sono curto", "apneia", "pouca energia disponível", "ferro", "tireoide", "medicamento", "depressão"]
    for k, c in enumerate(causas):
        x, y = 860 + (k % 2) * 400, 124 + (k // 2) * 72
        p.append(caixa(x, y, 370, 60, OXID, OXID_T, esp=2, rx=12))
        rs.append(rot(x, y + 14, c, w=370, tam=24, cor=OXID, peso=700, alinha="center"))
    p.append(f'<g transform="rotate(-4 1250 44)"><rect x="960" y="6" width="560" height="84" rx="12" fill="{GLIC}" stroke="{TINTA}" stroke-width="2"/></g>')
    rs.append(rot(960, 26, "“fadiga adrenal”", w=560, tam=34, cor=TINTA, peso=700, alinha="center", serif=True))
    rs.append(rot(1270, 350, "o que o rótulo deixa de procurar", w=370, tam=22, cor=OXID, peso=700, lh=1.2))
    return slide("fadiga", 420, p, rs,
                 eyebrow="Uma revisão sistemática, 2016", titulo="“Fadiga adrenal” não existe; os sintomas, sim",
                 destaque="O rótulo fecha a investigação cedo. Custa os meses em que o diagnóstico certo não foi procurado.",
                 destaque_cor="verm", fonte="Cadegiani e Kater, BMC Endocrine Disorders 2016")


# ---------------------------------------------------------------- aplicação

LICOES = {"03-01": [laudos, pares, anamnese, ficha, cinco],
          "03-02": [vilao, funcao, cuidados, investigar, fadiga]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
