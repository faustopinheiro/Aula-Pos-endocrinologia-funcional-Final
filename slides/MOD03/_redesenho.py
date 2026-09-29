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


# ---------------------------------------------------------------- 3.3

def origem():
    """3.3: adrenalina que cai no sangue e age longe; noradrenalina que age no tecido e vaza para o plasma."""
    p = [svg_abre(1664, 430, "À esquerda, a medula da adrenal lança adrenalina no sangue, e ela viaja até órgãos distantes: a peça endócrina do sistema. À direita, uma terminação simpática solta noradrenalina dentro do tecido; a maior parte age ali, e só o excedente escapa da sinapse para o vaso, onde é medido no plasma"), defs(OXID, FOSF)]
    rs = [rot(0, 0, "Adrenalina", w=780, tam=30, cor=OXID, peso=700, serif=True),
          rot(884, 0, "Noradrenalina", w=780, tam=30, cor=FOSF, peso=700, serif=True)]
    # adrenal e vaso
    p.append(f'<ellipse cx="120" cy="170" rx="100" ry="70" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<ellipse cx="120" cy="170" rx="46" ry="30" fill="{OXID}"/>')
    rs.append(rot(20, 250, "medula da adrenal", w=200, tam=22, cor=OXID, peso=700, alinha="center"))
    p.append(f'<rect x="230" y="150" width="480" height="44" rx="22" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    for k in range(8):
        p.append(f'<circle cx="{258 + k * 58}" cy="172" r="9" fill="{OXID}"/>')
    rs.append(rot(230, 110, "cai na circulação", w=480, tam=22, cor=TINTA, alinha="center"))
    for k, ic in enumerate(["t:heart", "t:droplet", "t:barbell"]):
        y = 60 + k * 90
        p.append(seta(712, 172, 744, y + 24, OXID, "m0", esp=3))
        p.append(icone(ic, 756, y, 48, OXID))
    rs.append(rot(0, 320, "age longe: é a peça endócrina do sistema", w=780, tam=24, cor=OXID, peso=700))
    rs.append(rot(0, 360, "produzida na medula da adrenal, age em órgãos distantes", w=780, tam=22, cor=TINTA))
    # terminação simpática
    X = 884
    p.append(f'<line x1="{X}" y1="120" x2="{X+300}" y2="120" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
    p.append(f'<circle cx="{X+320}" cy="120" r="36" fill="{FOSF}"/>')
    p.append(f'<rect x="{X+380}" y="60" width="200" height="130" rx="20" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
    for (dx, dy) in [(0, -24), (8, 0), (0, 24), (14, -12), (14, 12), (22, -30), (22, 30)]:
        p.append(f'<circle cx="{X+366+dx}" cy="{120+dy}" r="7" fill="{FOSF}"/>')
    rs += [rot(X, 70, "terminação simpática", w=300, tam=22, cor=FOSF, peso=700),
           rot(X + 380, 196, "tecido", w=200, tam=22, cor=GLIC, peso=700, alinha="center")]
    # vazamento para o vaso
    p.append(f'<rect x="{X+100}" y="270" width="680" height="44" rx="22" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    p.append(f'<path d="M {X+360} 160 C {X+330} 210, {X+300} 230, {X+300} 262" fill="none" stroke="{FOSF}" stroke-width="3" stroke-dasharray="6 6" marker-end="url(#m1)"/>')
    for k in range(3):
        p.append(f'<circle cx="{X+260 + k * 60}" cy="292" r="7" fill="{FOSF}"/>')
    rs += [rot(X, 214, "o excedente que escapou", w=280, tam=22, cor=FOSF, peso=700, alinha="right"),
           rot(X, 330, "no plasma, é o eco de uma atividade local, espalhada pelo corpo", w=780, tam=24, cor=FOSF, peso=700, lh=1.25),
           rot(X, 396, "marca quanto o simpático está acionado", w=780, tam=22, cor=TINTA)]
    return slide("origem", 430, p, rs,
                 eyebrow="De onde vem cada uma", titulo="Um hormônio e um neurotransmissor que vazou",
                 destaque="Noradrenalina plasmática não é um comando que desce.", destaque_cor="tinta")


def efeitos():
    """3.3: seis alvos ligados ao mesmo tempo, e o relógio de segundos e minutos."""
    p = [svg_abre(1664, 430, "No centro, as catecolaminas. Em volta, seis alvos ao mesmo tempo: coração, mais frequência e mais força; vaso, fecha víscera e pele e abre o músculo que trabalha; brônquio, dilata, o mesmo receptor da medicação de asma; fígado, quebra glicogênio e solta glicose; tecido adiposo, libera gordura; músculo, acelera a glicólise com oxigênio sobrando. Embaixo, uma régua: liga em segundos, desliga em minutos")]
    alvos = [("t:heart", "Coração", "mais frequência e mais força", FOSF),
             ("t:route", "Vaso", "fecha víscera e pele, abre o músculo que trabalha", FOSF),
             ("t:wave-sine", "Brônquio", "dilata: o receptor da medicação de asma", AZUL),
             ("t:droplet", "Fígado", "quebra glicogênio, solta glicose", GLIC),
             ("t:scale", "Tecido adiposo", "libera gordura", GLIC),
             ("t:barbell", "Músculo", "acelera a glicólise, com oxigênio sobrando", OXID)]
    cx, cy = 832, 150
    pos = [(0, 0), (0, 110), (0, 220), (1124, 0), (1124, 110), (1124, 220)]
    rs = []
    for (x, y) in pos:
        ex = x + 540 if x == 0 else x
        p.append(f'<line x1="{cx}" y1="{cy}" x2="{ex}" y2="{y+45}" stroke="{CINZA}" stroke-width="3"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="120" fill="{TINTA}"/>')
    rs += [rot(cx - 110, cy - 34, "Catecolaminas", w=220, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(cx - 110, cy + 8, "tudo ao mesmo tempo", w=220, tam=20, cor=PAPEL, alinha="center")]
    for (x, y), (ic, t, d, cor) in zip(pos, alvos):
        p.append(caixa(x, y, 540, 90, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, x + 18, y + 20, 50, cor))
        rs += [rot(x + 84, y + 8, t, w=440, tam=26, cor=cor, peso=700),
               rot(x + 84, y + 46, d, w=440, tam=20, cor=TINTA, lh=1.15)]
    # régua de tempo
    y0 = 360
    p.append(f'<line x1="0" y1="{y0}" x2="1664" y2="{y0}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<rect x="0" y="{y0-14}" width="140" height="28" rx="14" fill="{FOSF}"/>')
    p.append(f'<path d="M 140 {y0-14} L 620 {y0-4} L 620 {y0+4} L 140 {y0+14} Z" fill="{FOSF_T}"/>')
    rs += [rot(0, y0 + 24, "liga em segundos", w=300, tam=22, cor=FOSF, peso=700),
           rot(420, y0 + 24, "desliga em minutos", w=300, tam=22, cor=FOSF, peso=700),
           rot(1200, y0 + 24, "horas, dias: fora do alcance", w=464, tam=22, cor=MUDO, alinha="right")]
    return slide("efeitos", 430, p, rs,
                 eyebrow="Muita coisa ao mesmo tempo", titulo="Liga em segundos, desliga em minutos",
                 destaque="Parte do lactato do esforço intenso depende da adrenalina, não da falta de oxigênio.",
                 destaque_cor="petr", fonte="Hargreaves e Spriet, Nature Metabolism 2020")


def beta():
    """3.3: frequência cardíaca por esforço, com o betabloqueado achatado e o estimulante somando."""
    p = [svg_abre(1664, 440, "Gráfico esquemático de frequência cardíaca contra esforço. A curva de referência sobe até a máxima prevista. A do betabloqueado sobe menos e achata no pico, então o percentual da máxima prevista subestima o esforço. A de quem usa estimulante corre acima da referência, somando num sistema que o exercício já aciona")]
    X0, X1, Y0, Y1 = 90, 900, 400, 30
    p.append(f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="{MUDO}" stroke-width="3"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<line x1="{X0}" y1="70" x2="{X1}" y2="70" stroke="{CINZA}" stroke-width="2"{TRACO}/>')
    def c(pts, cor, esp, traco=""):
        d = "M" + " L".join(f"{X0 + a * (X1 - X0):.0f} {Y0 - b * (Y0 - 70):.0f}" for a, b in pts)
        p.append(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{esp}" stroke-linecap="round" stroke-linejoin="round"{traco}/>')
    c([(0, 0.25), (0.25, 0.42), (0.5, 0.62), (0.75, 0.82), (1, 1)], MUDO, 6)
    c([(0, 0.18), (0.25, 0.3), (0.5, 0.42), (0.75, 0.52), (1, 0.58)], OXID, 7)
    c([(0, 0.38), (0.25, 0.56), (0.5, 0.74), (0.75, 0.9), (0.95, 1.04)], FOSF, 7)
    rs = [rot(X0 + 10, 40, "máxima prevista", w=260, tam=20, cor=MUDO),
          rot(0, 20, "FC", w=80, tam=22, cor=MUDO, peso=700),
          rot(X0, 408, "esforço", w=X1 - X0, tam=22, cor=MUDO, alinha="center"),
          rot(X1 - 250, 250, "betabloqueado: pico achatado", w=260, tam=22, cor=OXID, peso=700, lh=1.2),
          rot(X0 + 180, 120, "com estimulante", w=260, tam=22, cor=FOSF, peso=700),
          rot(X0 + 400, 212, "referência", w=180, tam=20, cor=MUDO)]
    blocos = [(960, 0, "Betabloqueador", OXID, OXID_T, ["o percentual da máxima prevista subestima o esforço", "a percepção de esforço vira o instrumento principal"]),
              (960, 220, "Estimulantes", FOSF, FOSF_T, ["saudável, dose habitual: costuma ser tolerado", "arritmia, hipertensão mal controlada, doença cardíaca: cuidado"])]
    for x, y, t, cor, fundo, itens in blocos:
        p.append(caixa(x, y, 704, 200, cor, fundo, esp=3, rx=16))
        rs.append(rot(x + 24, y + 14, t, w=660, tam=28, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            rs.append(rot(x + 24, y + 62 + k * 66, it, w=660, tam=22, cor=TINTA, lh=1.25))
    return slide("beta", 440, p, rs,
                 eyebrow="A situação espelhada", titulo="Quando o relógio subestima o esforço",
                 destaque="No betabloqueado, a percepção de esforço deixa de ser alternativa: é o instrumento, para prescrever e para interpretar um teste.",
                 destaque_cor="petr", fonte="Curvas: esquema, sem valores medidos")


def limites():
    """3.3: o alcance do sistema numa régua de tempo: explica segundos e minutos, não explica meses."""
    p = [svg_abre(1664, 440, "Uma régua de tempo de segundos a meses. A faixa das catecolaminas cobre segundos e minutos. Embaixo dela, o que o sistema explica: a subida rápida da frequência cardíaca, até antes do esforço; a redistribuição de fluxo; glicose e gordura disponíveis e parte do lactato; a diferença entre treino e prova. Do lado das horas aos meses, o que não explica: cansaço de meses; não é exame de painel de atleta; metanefrinas só na suspeita de feocromocitoma; não é o que se trata, trata-se o contexto")]
    esc = ["segundos", "minutos", "horas", "dias", "meses"]
    rs = []
    for i, t in enumerate(esc):
        x = 80 + i * 376
        p.append(f'<line x1="{x}" y1="36" x2="{x}" y2="60" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(x - 100, 0, t, w=200, tam=22, cor=MUDO, alinha="center"))
    p.append(f'<line x1="80" y1="60" x2="1584" y2="60" stroke="{MUDO}" stroke-width="3"/>')
    p.append(f'<rect x="40" y="70" width="496" height="30" rx="15" fill="{OXID}"/>')
    rs.append(rot(40, 72, "catecolaminas", w=496, tam=20, cor=PAPEL, peso=700, alinha="center"))
    lados = [(0, 740, "Explica", OXID, OXID_T,
              ["a subida rápida da frequência cardíaca, até antes do esforço", "a redistribuição de fluxo", "glicose e gordura disponíveis, parte do lactato", "a diferença entre treino e prova"]),
             (804, 860, "Não explica", FOSF, FOSF_T,
              ["cansaço de meses: sobe em segundos, cai em minutos", "não é exame de painel de atleta", "metanefrinas: só na suspeita de feocromocitoma", "não é o que se trata: trata-se o contexto"])]
    for x, w, t, cor, fundo, itens in lados:
        p.append(caixa(x, 124, w, 316, cor, fundo, esp=3, rx=16))
        p.append(icone("t:check" if cor == OXID else "t:x", x + 20, 138, 40, cor))
        rs.append(rot(x + 70, 140, t, w=w - 90, tam=28, cor=cor, peso=700, serif=True))
        for k, it in enumerate(itens):
            rs.append(rot(x + 24, 196 + k * 60, it, w=w - 48, tam=24, cor=TINTA, lh=1.2))
    return slide("limites", 440, p, rs,
                 eyebrow="Onde a conversa escorrega", titulo="O que esse sistema explica, e o que não explica",
                 fonte="Lenders e colaboradores, Endocrine Society 2014")


# ---------------------------------------------------------------- 3.4

def pedido():
    """3.4: quatro sintomas que convergem num quadro, e o quadro que aponta para muitas causas."""
    p = [svg_abre(1664, 420, "À esquerda, os quatro sintomas atribuídos à testosterona: cansaço, libido baixa, dificuldade de ganhar massa, humor ruim. Eles convergem num quadro só. Do quadro saem muitas setas: testosterona baixa é uma delas; sono curto e apneia, déficit de energia, excesso de treino e depressão também produzem o mesmo quadro"), defs(MUDO)]
    sint = [("t:battery-1", "cansaço"), ("t:heart-broken", "libido baixa"), ("t:barbell", "dificuldade de ganhar massa"), ("t:mood-sad", "humor ruim")]
    rs = [rot(0, 0, "Os sintomas atribuídos à testosterona", w=520, tam=24, cor=FOSF, peso=700)]
    for k, (ic, t) in enumerate(sint):
        y = 50 + k * 90
        p.append(caixa(0, y, 480, 72, FOSF, FOSF_T, esp=2, rx=36))
        p.append(icone(ic, 20, y + 14, 44, FOSF))
        rs.append(rot(80, y + 20, t, w=390, tam=24, cor=TINTA))
        p.append(f'<path d="M 484 {y+36} C 560 {y+36}, 560 226, 632 226" fill="none" stroke="{CINZA}" stroke-width="4"/>')
    p.append(f'<circle cx="720" cy="226" r="90" fill="{TINTA}"/>')
    rs.append(rot(640, 206, "o quadro", w=160, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    causas = [("testosterona baixa", GLIC), ("sono curto, apneia", AZUL), ("déficit de energia", AZUL), ("excesso de treino", AZUL), ("depressão", AZUL), ("e muitas outras", MUDO)]
    rs.append(rot(1004, 0, "O que também produz esse quadro", w=660, tam=24, cor=TINTA, peso=700))
    for k, (t, cor) in enumerate(causas):
        y = 44 + k * 62
        p.append(f'<path d="M 810 226 C 900 226, 900 {y+26}, 996 {y+26}" fill="none" stroke="{cor}" stroke-width="3"/>')
        p.append(caixa(1004, y, 520, 52, cor, CARTAO, esp=2 if cor == MUDO else 3, rx=26))
        rs.append(rot(1004, y + 11, t, w=520, tam=24, cor=cor, peso=700, alinha="center"))
    return slide("pedido", 420, p, rs,
                 eyebrow="280 ng/dL e um pedido pronto", titulo="Um quadro que aponta para vinte coisas",
                 destaque="“Minha testosterona está em 280, já pesquisei, está abaixo do normal, eu quero começar reposição.”",
                 destaque_cor="ambar")


def verdades():
    """3.4: a doença que existe, e o orçamento que corta primeiro a reprodução."""
    p = [svg_abre(1664, 440, "À esquerda, o hipogonadismo que existe: Klinefelter, quimio ou radioterapia pélvica, trauma ou torção; tumor de hipófise, prolactina alta, hemocromatose; opioide crônico, corticoide em dose alta; anabolizante com eixo que não recuperou. À direita, um orçamento de energia com os gastos em ordem de prioridade: manter-se vivo, mover-se, reparar, e por último reproduzir. Quando falta caixa, o corte começa por cima, na reprodução")]
    p.append(caixa(0, 0, 780, 440, FOSF, FOSF_T, esp=3, rx=16))
    rs = [rot(24, 16, "Hipogonadismo existe", w=730, tam=30, cor=FOSF, peso=700, serif=True)]
    doencas = [("t:id", "Klinefelter, quimio ou radioterapia pélvica, trauma ou torção"),
               ("t:brain", "tumor de hipófise, prolactina alta, hemocromatose"),
               ("t:pill", "opioide crônico, corticoide em dose alta"),
               ("t:barbell", "anabolizante com eixo que não recuperou")]
    for k, (ic, t) in enumerate(doencas):
        y = 80 + k * 88
        p.append(icone(ic, 24, y + 6, 48, FOSF))
        rs.append(rot(92, y, t, w=660, tam=24, cor=TINTA, lh=1.25))
    rs.append(rot(900, 0, "Suprimido por contexto", w=764, tam=30, cor=OXID, peso=700, serif=True))
    gastos = [("reproduzir", GLIC, True), ("reparar", AZUL, False), ("mover-se", AZUL, False), ("manter-se vivo", TINTA, False)]
    for k, (t, cor, corta) in enumerate(gastos):
        y = 60 + k * 84
        if corta:
            p.append(f'<rect x="900" y="{y}" width="460" height="70" rx="12" fill="{CARTAO}" stroke="{cor}" stroke-width="4" stroke-dasharray="12 8"/>')
        else:
            p.append(f'<rect x="900" y="{y}" width="460" height="70" rx="12" fill="{cor}"/>')
        rs.append(rot(900, y + 18, t, w=460, tam=26, cor=cor if corta else PAPEL, peso=700, alinha="center"))
    p.append(f'<line x1="880" y1="146" x2="1380" y2="146" stroke="{FOSF}" stroke-width="5"/>')
    rs += [rot(1390, 60, "quando falta caixa, é o primeiro corte", w=274, tam=24, cor=FOSF, peso=700, lh=1.25),
           rot(1390, 200, "o que pesa na conta: sono, energia, treino, vida", w=274, tam=22, cor=TINTA, lh=1.25),
           rot(900, 400, "dos cinco eixos, o mais fácil de desligar", w=764, tam=24, cor=OXID, peso=700)]
    return slide("verdades", 440, p, rs,
                 eyebrow="Duas coisas verdadeiras ao mesmo tempo", titulo="Doença real, e o eixo mais fácil de desligar",
                 destaque="A pergunta não é “quanto está”. É: o eixo está doente, ou está fazendo o que deveria diante da conta desse homem?",
                 destaque_cor="tinta")


def estradiol():
    """3.4: dois círculos, testosterona e estradiol, e o que coube a cada um e aos dois."""
    p = [svg_abre(1664, 420, "Dois círculos que se sobrepõem. No da testosterona: massa magra, área muscular da coxa, força no leg press. No do estradiol: acúmulo de gordura, sobretudo. Na interseção, o que dependeu dos dois: libido e ereção")]
    p.append(f'<circle cx="692" cy="206" r="200" fill="{OXID}" fill-opacity="0.14" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<circle cx="952" cy="206" r="200" fill="{GLIC}" fill-opacity="0.14" stroke="{GLIC}" stroke-width="4"/>')
    p.append(f'<path d="M 822 54 A 200 200 0 0 1 822 358 A 200 200 0 0 1 822 54 Z" fill="{FOSF}" fill-opacity="0.22"/>')
    rs = [rot(160, 40, "Testosterona", w=300, tam=30, cor=OXID, peso=700, serif=True, alinha="right"),
          rot(1204, 40, "Estradiol", w=300, tam=30, cor=GLIC, peso=700, serif=True),
          rot(516, 150, "massa magra", w=236, tam=20, cor=TINTA, peso=600),
          rot(506, 196, "área muscular da coxa", w=246, tam=20, cor=TINTA, peso=600),
          rot(516, 242, "força no leg press", w=236, tam=20, cor=TINTA, peso=600),
          rot(924, 180, "acúmulo de gordura, sobretudo", w=200, tam=20, cor=TINTA, peso=600, lh=1.25),
          rot(752, 170, "libido e ereção", w=140, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2),
          rot(742, 234, "dependeu dos dois", w=160, tam=20, cor=FOSF, alinha="center", lh=1.15)]
    return slide("estradiol", 420, p, rs,
                 eyebrow="Um ensaio de doses graduadas, 2013", titulo="O estradiol no homem não é impureza",
                 destaque="Bloquear aromatase para “otimizar” custa gordura, osso e função sexual: o que o paciente foi buscar.",
                 destaque_cor="verm", fonte="Finkelstein e colaboradores, New England Journal of Medicine 2013 · homens de 20 a 50 anos, produção própria suprimida, doses graduadas com e sem inibidor de aromatase")


def saidaA():
    """3.4: o que acontece embaixo do número depois que a reposição começa."""
    p = [svg_abre(1664, 430, "Linha do tempo esquemática depois do início da reposição. A testosterona no sangue sobe para a faixa normal. O LH cai e o testículo para, por meses a anos. A produção de espermatozoide cai junto. Embaixo, uma faixa cinza continua igual o tempo todo: o contexto de sono, energia e treino segue rodando"), defs(TINTA)]
    X0, X1 = 260, 1640
    p.append(f'<line x1="{X0 + 180}" y1="10" x2="{X0 + 180}" y2="330" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    rs = [rot(X0 + 190, 0, "começa a reposição", w=300, tam=22, cor=TINTA, peso=700)]
    faixas = [(40, "Testosterona no sangue", OXID, [(0, 0.2), (0.14, 0.2), (0.22, 0.85), (1, 0.85)], "o número normaliza"),
              (140, "LH e testículo", FOSF, [(0, 0.7), (0.14, 0.7), (0.24, 0.08), (1, 0.08)], "parado por meses a anos, nem sempre volta ao que era"),
              (240, "Espermatozoide", FOSF, [(0, 0.7), (0.14, 0.7), (0.34, 0.1), (1, 0.1)], "e ninguém perguntou se ele ainda quer ter filho")]
    for y, t, cor, pts, nota in faixas:
        d = "M" + " L".join(f"{X0 + a * (X1 - X0):.0f} {y + 80 - b * 70:.0f}" for a, b in pts)
        p.append(f'<line x1="{X0}" y1="{y+80}" x2="{X1}" y2="{y+80}" stroke="{CINZA}" stroke-width="2"/>')
        p.append(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="6" stroke-linejoin="round"/>')
        rs += [rot(0, y + 38, t, w=240, tam=22, cor=cor, peso=700, alinha="right"),
               rot(X0 + 520, y + 48 if cor == OXID else y + 36, nota, w=X1 - X0 - 520, tam=22, cor=cor if cor != OXID else OXID, peso=600)]
    p.append(f'<rect x="{X0}" y="352" width="{X1 - X0}" height="56" rx="12" fill="{CINZA}"/>')
    rs += [rot(0, 366, "O contexto", w=240, tam=22, cor=TINTA, peso=700, alinha="right"),
           rot(X0 + 20, 364, "sono, energia, treino: continua rodando embaixo, e a causa fica", w=X1 - X0 - 40, tam=24, cor=TINTA, peso=600)]
    return slide("saidaA", 430, p, rs,
                 eyebrow="Saída A", titulo="Repor agora, quando a leitura está errada",
                 destaque="O argumento é honesto: ele tem sintoma e a reposição funciona. O custo aparece quando o número era contexto.",
                 destaque_cor="ambar", fonte="Esquema, sem valores medidos")


def saidaC():
    """3.4: as bandeiras que tornam a investigação obrigatória, e o caminho de quando ela é pulada."""
    p = [svg_abre(1664, 430, "À esquerda, quatro bandeiras que tornam a investigação obrigatória: LH alto com testosterona baixa; alteração visual, dor de cabeça, galactorreia; trauma, quimio ou radioterapia, caxumba; testículos pequenos, ginecomastia, anabolizante. À direita, o caminho de quando a investigação é pulada: anos de estilo de vida em quem tinha Klinefelter, prolactinoma ou tumor de hipófise; o erro mais raro, e mais grave"), defs(TINTA, FOSF)]
    rs = [rot(0, 0, "Obrigatória quando", w=760, tam=28, cor=FOSF, peso=700, serif=True)]
    band = ["LH alto com testosterona baixa", "alteração visual, dor de cabeça, galactorreia", "trauma, quimio ou radioterapia, caxumba", "testículos pequenos, ginecomastia, anabolizante"]
    for k, t in enumerate(band):
        y = 56 + k * 92
        p.append(caixa(0, y, 760, 76, FOSF, FOSF_T, esp=2, rx=14))
        p.append(icone("t:flag", 18, y + 14, 46, FOSF))
        rs.append(rot(84, y + 22, t, w=660, tam=24, cor=TINTA))
    rs.append(rot(860, 0, "Quando é pulada", w=804, tam=28, cor=TINTA, peso=700, serif=True))
    passos = [("t:zoom-question", "“é estilo de vida”", MUDO), ("t:calendar", "anos corrigindo sono, dieta e treino", MUDO), ("t:alert-triangle", "Klinefelter, prolactinoma, tumor de hipófise", FOSF)]
    for k, (ic, t, cor) in enumerate(passos):
        y = 56 + k * 124
        p.append(caixa(860, y, 804, 92, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, 880, y + 20, 52, cor))
        rs.append(rot(950, y + 26, t, w=700, tam=24, cor=cor if cor == FOSF else TINTA, peso=700 if cor == FOSF else 400))
        if k < 2:
            p.append(seta(1262, y + 96, 1262, y + 118, TINTA, "m0", esp=4))
    rs.append(rot(860, 404, "o erro mais raro, e mais grave", w=804, tam=24, cor=FOSF, peso=700))
    return slide("saidaC", 430, p, rs,
                 eyebrow="Saída C", titulo="Investigar a causa verdadeira",
                 destaque="Nem todo mundo responde à correção da conta. O que se defende não é nunca repor: é nunca repor sem ter montado a conta antes.",
                 destaque_cor="petr")


def criterio():
    """3.4: as seis perguntas como um caminho com dois portões."""
    p = [svg_abre(1664, 430, "Um caminho com dois portões e três perguntas em cada. Antes de dosar: como está a conta de sono, energia, treino e vida; há déficit ou perda de peso rápida; usa ou já usou algo hormonal, pelo nome, sem julgamento. Antes de repor, decisão médica: a conta foi corrigida e mantida por tempo suficiente; o sintoma é consistente, e não só número; ele sabe da supressão e do impacto na fertilidade"), defs(TINTA)]
    blocos = [(0, "Antes de dosar", OXID, OXID_T, ["Como está a conta: sono, energia, treino, vida?", "Déficit ou perda de peso rápida?", "Usa ou já usou algo hormonal? Pelo nome, sem julgamento"]),
              (872, "Antes de repor: decisão médica", FOSF, FOSF_T, ["A conta foi corrigida e mantida por tempo suficiente?", "Sintoma consistente, e não só número?", "Ele sabe da supressão e do impacto na fertilidade?"])]
    rs = []
    n = 1
    for x, t, cor, fundo, qs in blocos:
        p.append(caixa(x, 0, 792, 430, cor, fundo, esp=3, rx=18))
        rs.append(rot(x + 28, 18, t, w=740, tam=28, cor=cor, peso=700, serif=True))
        for k, q in enumerate(qs):
            y = 86 + k * 112
            p.append(f'<circle cx="{x+60}" cy="{y+40}" r="32" fill="{cor}"/>')
            rs.append(rot(x + 28, y + 24, str(n), w=64, tam=28, cor=PAPEL, peso=700, alinha="center"))
            rs.append(rot(x + 112, y + 8, q, w=650, tam=24, cor=TINTA, lh=1.3))
            n += 1
    p.append(seta(796, 215, 866, 215, TINTA, "m0", esp=6))
    return slide("criterio", 430, p, rs,
                 eyebrow="O que torna a decisão defensável", titulo="Seis perguntas",
                 destaque="Relação testosterona-cortisol: reconheça quando aparecer, não use para decidir. Para carga, carga interna, sono, peso e relato.",
                 destaque_cor="ambar", fonte="Urhausen, Gabriel e Kindermann, Sports Medicine 1995")


# ---------------------------------------------------------------- aplicação

LICOES = {"03-01": [laudos, pares, anamnese, ficha, cinco],
          "03-02": [vilao, funcao, cuidados, investigar, fadiga],
          "03-03": [origem, efeitos, beta, limites],
          "03-04": [pedido, verdades, estradiol, saidaA, saidaC, criterio]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
