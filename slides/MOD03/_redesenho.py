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


# ---------------------------------------------------------------- 3.5

def portas():
    """3.5: duas portas com o mesmo exame, e o tamanho do segundo erro em Klinefelter."""
    p = [svg_abre(1664, 400, "À esquerda, duas portas lado a lado com o mesmo exame pendurado: numa, tratado sem ter; na outra, tem e nunca foi tratado. À direita, uma grade de 650 pontos com um só destacado: cerca de 1 em 650 nascimentos masculinos com síndrome de Klinefelter. Embaixo, quatro pessoas, três apagadas: 3 em cada 4 nunca diagnosticados")]
    p.append(f'<defs><pattern id="gp" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="4" fill="{CINZA}"/></pattern></defs>')
    rs = []
    for j, (t, cor) in enumerate([("tratado sem ter", GLIC), ("tem e nunca foi tratado", FOSF)]):
        x = j * 330
        p.append(f'<rect x="{x+20}" y="30" width="260" height="360" rx="8" fill="{CARTAO}" stroke="{cor}" stroke-width="5"/>')
        p.append(f'<rect x="{x+44}" y="54" width="212" height="140" rx="6" fill="none" stroke="{cor}" stroke-width="2"/>')
        p.append(f'<rect x="{x+44}" y="214" width="212" height="150" rx="6" fill="none" stroke="{cor}" stroke-width="2"/>')
        p.append(f'<circle cx="{x+246}" cy="214" r="10" fill="{cor}"/>')
        p.append(f'<rect x="{x+80}" y="84" width="140" height="84" rx="6" fill="{PAPEL}" stroke="{TINTA}" stroke-width="2"/>')
        p.append(f'<line x1="{x+150}" y1="30" x2="{x+150}" y2="84" stroke="{TINTA}" stroke-width="2"/>')
        rs += [rot(x + 80, 100, "o mesmo exame", w=140, tam=20, cor=TINTA, alinha="center", lh=1.15),
               rot(x + 30, 236, t, w=240, tam=24, cor=cor, peso=700, alinha="center", serif=True, lh=1.2)]
    # grade de 650
    gx, gy = 760, 40
    p.append(f'<rect x="{gx}" y="{gy}" width="{26*14}" height="{25*14}" fill="url(#gp)"/>')
    p.append(f'<circle cx="{gx + 17*14 + 7}" cy="{gy + 11*14 + 7}" r="7" fill="{FOSF}"/>')
    rs += [rot(gx, 0, "1 em 650", w=364, tam=32, cor=FOSF, peso=700, serif=True, alinha="center"),
           rot(gx, 394 - 0, "", w=10, tam=20)]
    rs.pop()
    rs.append(rot(1150, 40, "nascimentos masculinos com síndrome de Klinefelter", w=500, tam=24, cor=TINTA, lh=1.25))
    for k in range(4):
        x = 1160 + k * 120
        cor = FOSF if k == 0 else CINZA
        p.append(icone("t:user", x, 150, 96, cor))
    rs += [rot(1150, 256, "3 em 4", w=500, tam=36, cor=FOSF, peso=700, serif=True),
           rot(1150, 306, "dos afetados nunca diagnosticados", w=500, tam=24, cor=TINTA)]
    return slide("portas", 400, p, rs,
                 eyebrow="Dois erros simétricos", titulo="Tratado sem ter, ou tem e nunca foi tratado",
                 destaque="E eles passam pelo consultório por infertilidade, ginecomastia, dificuldade de ganhar massa: as queixas que chegam à nossa área.",
                 destaque_cor="ambar", fonte="Bojesen, Juul e Gravholt, Journal of Clinical Endocrinology and Metabolism 2003 · registro nacional da Dinamarca")


def auditar():
    """3.5: o número no centro e as seis perguntas de auditoria em volta."""
    p = [svg_abre(1664, 440, "No centro, um laudo com a testosterona baixa sob uma lupa. Em volta, seis perguntas sobre como o número foi produzido: horário, a coleta de tarde é coleta no vale; alimento, depois de comer o valor cai por horas; doença aguda, o exame descreve a virose; treino recente, a manhã seguinte à sessão pesada não é base; SHBG não pedida; troca de método de laboratório. Qualquer uma comprometida: repita, não trate")]
    cx, cy = 832, 200
    itens = [("t:clock", "Horário", "coleta de tarde é coleta no vale", FOSF),
             ("t:salad", "Alimento", "depois de comer, o valor cai por horas", FOSF),
             ("t:mood-sick", "Doença aguda", "o exame descreve a virose, não o eixo", FOSF),
             ("t:barbell", "Treino recente", "a manhã seguinte à sessão pesada não é base", GLIC),
             ("t:scale", "SHBG não pedida", "atleta magro e obeso erram em sentidos opostos", GLIC),
             ("t:arrows-exchange", "Troca de método", "laboratórios diferentes, “queda” de método", GLIC)]
    pos = [(0, 0), (0, 140), (0, 280), (1124, 0), (1124, 140), (1124, 280)]
    rs = []
    for (x, y) in pos:
        ex = x + 540 if x == 0 else x
        p.append(f'<line x1="{cx}" y1="{cy}" x2="{ex}" y2="{y+55}" stroke="{CINZA}" stroke-width="3"/>')
    p.append(caixa(cx - 150, cy - 130, 300, 230, TINTA, CARTAO, esp=2, rx=10))
    p.append(f'<rect x="{cx-150}" y="{cy-130}" width="300" height="12" rx="4" fill="{TINTA}"/>')
    rs += [rot(cx - 130, cy - 100, "Testosterona total", w=260, tam=22, cor=TINTA, peso=700, alinha="center"),
           rot(cx - 130, cy - 60, "baixa", w=260, tam=36, cor=FOSF, peso=700, alinha="center", serif=True)]
    p.append(f'<circle cx="{cx+40}" cy="{cy+40}" r="42" fill="none" stroke="{AZUL}" stroke-width="7"/>')
    p.append(f'<line x1="{cx+70}" y1="{cy+70}" x2="{cx+110}" y2="{cy+110}" stroke="{AZUL}" stroke-width="10" stroke-linecap="round"/>')
    for (x, y), (ic, t, d, cor) in zip(pos, itens):
        p.append(caixa(x, y, 540, 110, cor, CARTAO, esp=3, rx=14))
        p.append(icone(ic, x + 18, y + 28, 52, cor))
        rs += [rot(x + 86, y + 12, t, w=440, tam=26, cor=cor, peso=700),
               rot(x + 86, y + 52, d, w=440, tam=21, cor=TINTA, lh=1.2)]
    rs.append(rot(cx - 250, 400, "Qualquer uma comprometida: repita, não trate.", w=500, tam=24, cor=TINTA, peso=700, alinha="center"))
    return slide("auditar", 440, p, rs,
                 eyebrow="Passo dois", titulo="Auditar como o número foi produzido")


def acionaveis():
    """3.5: remédios que freiam o eixo, e as duas vias da obesidade."""
    p = [svg_abre(1664, 420, "À esquerda, remédios que suprimem o eixo: opioide, inclusive o crônico para dor; corticoide em dose alta ou prolongada; antipsicóticos e alguns antieméticos, pela prolactina; gabapentinoides e antiandrogênicos. À direita, a obesidade age por duas vias: a SHBG baixa derruba a testosterona total, e a aromatização no tecido adiposo gera estradiol, que freia o eixo. Perder peso sobe a testosterona"), defs(GLIC, OXID)]
    p.append(caixa(0, 0, 700, 420, FOSF, FOSF_T, esp=3, rx=16))
    rs = [rot(24, 16, "Remédios que suprimem o eixo", w=650, tam=28, cor=FOSF, peso=700, serif=True)]
    rem = ["opioide, inclusive o crônico para dor", "corticoide em dose alta ou prolongada", "antipsicóticos e alguns antieméticos: prolactina", "gabapentinoides, antiandrogênicos"]
    for k, t in enumerate(rem):
        y = 80 + k * 82
        p.append(icone("t:pill", 24, y + 4, 44, FOSF))
        rs.append(rot(86, y + 6, t, w=590, tam=24, cor=TINTA, lh=1.2))
    # obesidade
    rs.append(rot(780, 0, "Obesidade, por duas vias", w=884, tam=28, cor=GLIC, peso=700, serif=True))
    p.append(f'<circle cx="880" cy="200" r="90" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
    p.append(icone("t:scale", 846, 150, 68, GLIC))
    rs.append(rot(800, 226, "tecido adiposo", w=160, tam=20, cor=GLIC, peso=700, alinha="center"))
    vias = [(60, "SHBG baixa", "derruba a total"), (240, "mais aromatização", "estradiol, mais freio no eixo")]
    for y, t, d in vias:
        p.append(seta(972, 200, 1054, y + 44, GLIC, "m0", esp=4))
        p.append(caixa(1064, y, 600, 96, GLIC, CARTAO, esp=3, rx=14))
        rs += [rot(1086, y + 12, t, w=560, tam=26, cor=GLIC, peso=700), rot(1086, y + 52, d, w=560, tam=22, cor=TINTA)]
    p.append(caixa(780, 360, 884, 60, OXID, OXID_T, esp=3, rx=30))
    p.append(icone("t:trending-up", 800, 368, 44, OXID))
    rs.append(rot(860, 374, "perder peso sobe a testosterona: a causa reversível mais comum", w=790, tam=22, cor=OXID, peso=700))
    return slide("acionaveis", 420, p, rs,
                 eyebrow="As mais acionáveis", titulo="Remédios e obesidade",
                 destaque="Perda de peso é intervenção de primeira linha sobre o próprio eixo: sem ampola, sem supressão, sem impacto na fertilidade.",
                 destaque_cor="petr", fonte="Corona e colaboradores, European Journal of Endocrinology 2013 · Bhasin e colaboradores, Endocrine Society 2018")


def escondem():
    """3.5: três armadilhas, cada uma com o desenho do que ela esconde."""
    p = [svg_abre(1664, 460, "Três painéis. Primeiro, é normal nessa idade: a queda da testosterona com a idade é lenta e modesta, uma linha quase plana. Segundo, total normal com SHBG alta: no magro de endurance a barra da total está dentro da faixa, e a da fração disponível está baixa. Terceiro, prolactina não pedida: um pedido de exame com a prolactina sem marcar; ela entra em todo padrão central, e o ferro quando a história sugerir")]
    rs = []
    W = 528
    for j, (t, cor) in enumerate([("“É normal nessa idade”", FOSF), ("Total normal com SHBG alta", GLIC), ("Prolactina não pedida", OXID)]):
        x = j * (W + 40)
        p.append(caixa(x, 0, W, 460, cor, CARTAO, esp=3, rx=16))
        rs.append(rot(x + 24, 18, t, w=W - 48, tam=26, cor=cor, peso=700, serif=True))
    # painel 1: queda lenta
    x = 0
    p.append(f'<line x1="{x+60}" y1="330" x2="{x+480}" y2="330" stroke="{MUDO}" stroke-width="2"/><line x1="{x+60}" y1="100" x2="{x+60}" y2="330" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="M {x+60} 150 L {x+480} 196" stroke="{MUDO}" stroke-width="6" fill="none"/>')
    p.append(f'<path d="M {x+60} 150 L {x+200} 150 L {x+230} 300 L {x+480} 300" stroke="{FOSF}" stroke-width="6" fill="none" stroke-dasharray="14 8"/>')
    rs += [rot(x + 60, 340, "idade", w=420, tam=20, cor=MUDO, alinha="center"),
           rot(x + 250, 104, "queda com a idade: lenta e modesta", w=260, tam=20, cor=MUDO, lh=1.2),
           rot(x + 250, 250, "queda franca: não é a idade", w=260, tam=20, cor=FOSF, peso=700, lh=1.2),
           rot(x + 24, 390, "a idade não explica um valor muito baixo", w=W - 48, tam=22, cor=TINTA, lh=1.25)]
    # painel 2: total e disponível
    x = W + 40
    p.append(f'<rect x="{x+60}" y="150" width="400" height="44" rx="4" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<rect x="{x+60}" y="150" width="300" height="44" rx="4" fill="{AZUL}"/>')
    p.append(f'<rect x="{x+60}" y="250" width="400" height="44" rx="4" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    p.append(f'<rect x="{x+60}" y="250" width="70" height="44" rx="4" fill="{GLIC}"/>')
    for y1 in (144, 244):
        p.append(f'<line x1="{x+160}" y1="{y1}" x2="{x+160}" y2="{y1+56}" stroke="{OXID}" stroke-width="3"{TRACO}/>')
    rs += [rot(x + 60, 110, "testosterona total", w=400, tam=22, cor=AZUL, peso=700),
           rot(x + 60, 210, "fração disponível", w=400, tam=22, cor=GLIC, peso=700),
           rot(x + 170, 310, "limite da faixa", w=280, tam=20, cor=OXID),
           rot(x + 24, 390, "o magro de endurance passa, com fração disponível ruim", w=W - 48, tam=22, cor=TINTA, lh=1.25)]
    # painel 3: pedido de exame
    x = 2 * (W + 40)
    p.append(f'<rect x="{x+80}" y="90" width="370" height="260" rx="10" fill="{PAPEL}" stroke="{MUDO}" stroke-width="2"/>')
    campos = [("Testosterona total", True), ("LH e FSH", True), ("SHBG", True), ("Prolactina", False)]
    for k, (c, ok) in enumerate(campos):
        y = 116 + k * 56
        p.append(f'<rect x="{x+104}" y="{y}" width="32" height="32" rx="6" fill="{CARTAO}" stroke="{OXID if ok else FOSF}" stroke-width="3"/>')
        if ok:
            p.append(icone("t:check", x + 106, y + 2, 28, OXID))
        rs.append(rot(x + 150, y + 2, c, w=280, tam=22, cor=TINTA if ok else FOSF, peso=400 if ok else 700))
    rs.append(rot(x + 24, 390, "em todo padrão central; ferro quando a história sugerir", w=W - 48, tam=22, cor=TINTA, lh=1.25))
    return slide("escondem", 460, p, rs,
                 eyebrow="Passo três", titulo="As armadilhas que escondem o hipogonádico",
                 fonte="Esquemas, sem valores medidos")


def exame():
    """3.5: uma figura humana com os cinco pontos do exame físico que decide."""
    p = [svg_abre(1664, 460, "Uma figura humana esquemática com cinco pontos de exame: olfato, perguntar se sente cheiro normalmente, pela síndrome de Kallmann; campo visual, trinta segundos, por compressão do quiasma; mama, glândula à palpação e não gordura; pelos e puberdade, antes ou depois da puberdade; volume testicular, pequenos e firmes no primário, pequenos e moles na supressão central longa")]
    cx = 832
    # figura
    p.append(f'<circle cx="{cx}" cy="70" r="58" fill="{PAPEL}" stroke="{TINTA}" stroke-width="4"/>')
    p.append(f'<path d="M {cx-120} 460 L {cx-120} 200 Q {cx-120} 140 {cx-60} 140 L {cx+60} 140 Q {cx+120} 140 {cx+120} 200 L {cx+120} 460" fill="{PAPEL}" stroke="{TINTA}" stroke-width="4"/>')
    pontos = [("Olfato", "Kallmann: “sente cheiro normalmente?”", OXID, cx, 84, 0, 20),
              ("Campo visual", "30 segundos: compressão do quiasma", OXID, cx + 20, 58, 1, 20),
              ("Mama", "glândula à palpação, não gordura", GLIC, cx - 50, 220, 0, 160),
              ("Pelos e puberdade", "antes ou depois da puberdade", TINTA, cx + 50, 300, 1, 180),
              ("Volume testicular", "pequenos e firmes: primário · pequenos e moles: supressão central longa", FOSF, cx, 430, 0, 320)]
    rs = []
    for t, d, cor, px, py, lado, by in pontos:
        p.append(f'<circle cx="{px}" cy="{py}" r="14" fill="{cor}" stroke="{CARTAO}" stroke-width="3"/>')
        if lado == 0:
            bx = 0
            p.append(f'<line x1="{px}" y1="{py}" x2="{bx+560}" y2="{by+40}" stroke="{cor}" stroke-width="2"/>')
            p.append(caixa(bx, by, 560, 110 if len(d) > 40 else 90, cor, CARTAO, esp=3, rx=14))
        else:
            bx = 1104
            p.append(f'<line x1="{px}" y1="{py}" x2="{bx}" y2="{by+40}" stroke="{cor}" stroke-width="2"/>')
            p.append(caixa(bx, by, 560, 90, cor, CARTAO, esp=3, rx=14))
        rs += [rot(bx + 20, by + 10, t, w=520, tam=26, cor=cor, peso=700),
               rot(bx + 20, by + 48, d, w=520, tam=21, cor=TINTA, lh=1.2)]
    return slide("exame", 460, p, rs,
                 eyebrow="A armadilha que mais falta", titulo="O exame físico que decide")


def dizer():
    """3.5: três frases ditas ao paciente, e as três perguntas que abrem a conversa."""
    p = [svg_abre(1664, 440, "Três balões de fala, ditos com clareza e sem moralismo: ciclo sugere um retorno que não é garantido; terapia pós-ciclo não é botão de reset, é conduta médica com indicação e não garante retorno; fertilidade se discute antes, não depois de três anos de uso. À direita, as três perguntas: o nome da substância, por quanto tempo, há quanto tempo parou")]
    frases = [("“Ciclo” sugere um retorno que não é garantido", "", FOSF),
              ("Terapia pós-ciclo não é botão de reset", "é conduta médica, com indicação, e não garante retorno", FOSF),
              ("Fertilidade se discute antes", "não depois de três anos de uso", OXID)]
    rs = []
    for k, (t, d, cor) in enumerate(frases):
        y = k * 148
        p.append(f'<path d="M 90 {y+10} L 1000 {y+10} Q 1020 {y+10} 1020 {y+30} L 1020 {y+104} Q 1020 {y+124} 1000 {y+124} L 150 {y+124} L 110 {y+144} L 118 {y+124} L 90 {y+124} Q 70 {y+124} 70 {y+104} L 70 {y+30} Q 70 {y+10} 90 {y+10} Z" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        rs.append(rot(100, y + (34 if not d else 22), t, w=890, tam=28, cor=cor, peso=700, serif=True))
        if d:
            rs.append(rot(100, y + 68, d, w=890, tam=22, cor=TINTA))
        p.append(icone("t:message-circle", 0, y + 40, 52, cor))
    p.append(caixa(1100, 0, 564, 440, TINTA, PAPEL, esp=2, rx=16))
    rs.append(rot(1124, 18, "Pergunte, pelo nome", w=520, tam=28, cor=TINTA, peso=700, serif=True))
    qs = [("t:pill", "qual substância"), ("t:hourglass", "por quanto tempo"), ("t:calendar", "há quanto tempo parou")]
    for k, (ic, t) in enumerate(qs):
        y = 90 + k * 110
        p.append(f'<circle cx="1160" cy="{y+36}" r="36" fill="{CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
        p.append(icone(ic, 1136, y + 12, 48, AZUL))
        rs.append(rot(1214, y + 20, t, w=430, tam=26, cor=TINTA, peso=600))
    return slide("dizer", 440, p, rs,
                 eyebrow="Sem moralismo", titulo="Três coisas ditas com clareza",
                 destaque="Testosterona baixa, LH baixo, testículos pequenos e moles: é aqui que a pergunta entra.",
                 destaque_cor="tinta")


def roteiro():
    """3.5: cinco passos em linha, cada um com a sua saída embaixo."""
    p = [svg_abre(1664, 380, "Cinco passos em sequência, cada um com a sua saída embaixo. Um, auditar o número: algo comprometido, repetir. Dois, dosar o par e classificar: LH alto aponta o testículo, baixo ou normal aponta para cima. Três, central orgânico ou funcional: história, exame físico, prolactina, ferro quando couber. Quatro, corrigir o que é corrigível e reavaliar em três a quatro meses, com coleta padronizada. Cinco, investigar com imagem e encaminhar: central sem contexto, prolactina alta, visão, dor de cabeça nova"), defs(TINTA, MUDO)]
    passos = [("Auditar o número", "algo comprometido: repetir", TINTA),
              ("Dosar o par e classificar", "LH alto: testículo · baixo ou normal: acima", TINTA),
              ("Central: orgânico ou funcional?", "história, exame físico, prolactina, ferro quando couber", OXID),
              ("Corrigir o corrigível e reavaliar", "3 a 4 meses, coleta padronizada", OXID),
              ("Imagem e encaminhar", "central sem contexto, prolactina alta, visão, dor de cabeça nova", FOSF)]
    rs = []
    W, G = 300, 41
    for k, (t, d, cor) in enumerate(passos):
        x = k * (W + G)
        p.append(f'<rect x="{x}" y="0" width="{W}" height="150" rx="16" fill="{cor}"/>')
        rs += [rot(x, 14, str(k + 1), w=W, tam=36, cor=PAPEL, peso=700, alinha="center", serif=True),
               rot(x + 16, 66, t, w=W - 32, tam=24, cor=PAPEL, peso=700, alinha="center", lh=1.2)]
        if k < 4:
            p.append(seta(x + W + 4, 75, x + W + G - 4, 75, TINTA, "m0", esp=4))
        p.append(seta(x + W / 2, 156, x + W / 2, 222, MUDO, "m1", esp=3))
        p.append(caixa(x, 230, W, 150, cor, CARTAO, esp=2, rx=14))
        rs.append(rot(x + 16, 246, d, w=W - 32, tam=24, cor=TINTA, lh=1.3))
    return slide("roteiro", 380, p, rs,
                 eyebrow="O procedimento", titulo="Cinco passos, cada um com sua saída")


# ---------------------------------------------------------------- 3.6

def enquadre():
    """3.6: o comando duplo do eixo, e a diferença entre a doença rara e a queda universal."""
    import math
    p = [svg_abre(1664, 440, "À esquerda, o eixo: no hipotálamo, um comando que estimula e a somatostatina, que freia; a hipófise libera GH em pulsos; o fígado responde com IGF-1. À direita, em cima, a deficiência do adulto, rara: lesão ou tumor de hipófise, sequela de radioterapia, trauma craniano; tem critério diagnóstico e tratamento que ajuda muito. Embaixo, a queda com a idade, universal: uma curva que desce devagar a partir da terceira década em todo mundo, fisiológica, e vendida como doença"), defs(OXID, FOSF, TINTA)]
    # eixo
    p.append(caixa(0, 0, 440, 90, AZUL, AZUL_T, esp=3, rx=14))
    rs = [rot(0, 12, "Hipotálamo", w=440, tam=26, cor=AZUL, peso=700, alinha="center"),
          rot(0, 48, "um comando estimula, a somatostatina freia", w=440, tam=20, cor=TINTA, alinha="center")]
    p.append(seta(170, 96, 170, 150, OXID, "m0", esp=5))
    p.append(seta(270, 96, 270, 150, FOSF, "m1", esp=5))
    rs += [rot(60, 104, "+", w=100, tam=30, cor=OXID, peso=700, alinha="right"), rot(284, 104, "−", w=100, tam=30, cor=FOSF, peso=700)]
    p.append(caixa(0, 160, 440, 90, AZUL, CARTAO, esp=3, rx=14))
    pulsos = "M 250 230 " + " ".join(f"L {250 + i * 6} {230 - (40 if i % 6 == 2 else 0)}" for i in range(28))
    p.append(f'<path d="{pulsos}" fill="none" stroke="{AZUL}" stroke-width="3"/>')
    rs.append(rot(20, 176, "Hipófise: GH em pulsos", w=220, tam=22, cor=AZUL, peso=700, lh=1.2))
    p.append(seta(220, 256, 220, 310, TINTA, "m2", esp=5))
    p.append(caixa(0, 320, 440, 90, OXID, OXID_T, esp=3, rx=14))
    rs.append(rot(0, 346, "Fígado: IGF-1", w=440, tam=26, cor=OXID, peso=700, alinha="center"))
    # doença rara
    p.append(caixa(540, 0, 1124, 190, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(564, 14, "Deficiência do adulto: existe, e é rara", w=1080, tam=28, cor=FOSF, peso=700, serif=True),
           rot(564, 66, "lesão ou tumor de hipófise · sequela de radioterapia · trauma craniano", w=1080, tam=24, cor=TINTA),
           rot(564, 118, "critério diagnóstico, tratamento que ajuda muito", w=1080, tam=24, cor=FOSF, peso=600)]
    # queda universal
    p.append(caixa(540, 220, 1124, 220, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(564, 232, "Queda com a idade: universal", w=620, tam=28, cor=GLIC, peso=700, serif=True))
    pts = [(20 + a, 1 - 0.55 * (1 - math.exp(-a / 30))) for a in range(0, 61, 2)]
    d = "M" + " L".join(f"{580 + (x - 20) * 9:.0f} {420 - y * 120:.0f}" for x, y in pts)
    p.append(f'<path d="{d}" fill="none" stroke="{GLIC}" stroke-width="6"/>')
    rs += [rot(580, 408, "20", w=60, tam=20, cor=MUDO), rot(580 + 60 * 9 - 40, 408, "80 anos", w=100, tam=20, cor=MUDO),
           rot(1200, 280, "a partir da terceira década, em todo mundo", w=440, tam=22, cor=TINTA, lh=1.25),
           rot(1200, 350, "fisiológica, e vendida como doença", w=440, tam=22, cor=GLIC, peso=700, lh=1.25)]
    return slide("enquadre", 440, p, rs,
                 eyebrow="O enquadramento", titulo="Uma doença rara e uma queda universal",
                 destaque="Antienvelhecimento, GH injetável, secretagogos, peptídeos: é a queda universal que se vende como doença.",
                 destaque_cor="ambar", fonte="Curva: esquema, sem valores medidos")


def dosar():
    """3.6: a coleta que cai no vale, o IGF-1 que integra, e o que faz o diagnóstico."""
    import math
    p = [svg_abre(1664, 420, "À esquerda, o GH ao longo de um dia em pulsos, com uma coleta isolada caindo num vale, indetectável numa pessoa normal, e o IGF-1 correndo estável como o integrador de dias. À direita, o teste de estímulo, que faz o diagnóstico no adulto com endocrinologista, e o IGFBP-3, sem papel no diagnóstico de rotina do adulto")]
    X0, X1, Y0 = 20, 980, 330
    pts = []
    for m in range(0, 1441, 6):
        v = 4
        for c, amp in ((90, 180), (220, 150), (340, 170), (620, 60), (900, 70), (1200, 60)):
            v += amp * math.exp(-((m - c) / 22) ** 2)
        pts.append((X0 + m / 1440 * (X1 - X0), Y0 - v))
    d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    p.append(f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="{d}" fill="none" stroke="{AZUL}" stroke-width="4"/>')
    p.append(f'<line x1="{X0}" y1="250" x2="{X1}" y2="250" stroke="{OXID}" stroke-width="7"/>')
    xv = X0 + 760 / 1440 * (X1 - X0)
    p.append(f'<line x1="{xv:.0f}" y1="140" x2="{xv:.0f}" y2="{Y0-6}" stroke="{FOSF}" stroke-width="3"{TRACO}/>')
    p.append(f'<circle cx="{xv:.0f}" cy="{Y0-4}" r="13" fill="{FOSF}" stroke="{CARTAO}" stroke-width="3"/>')
    rs = [rot(X0, 0, "GH em pulsos", w=300, tam=24, cor=AZUL, peso=700),
          rot(xv - 30, 96, "coleta isolada: no vale, indetectável", w=330, tam=22, cor=FOSF, peso=700, lh=1.2),
          rot(X0 + 700, 208, "IGF-1: o integrador de dias", w=300, tam=22, cor=OXID, peso=700, alinha="right"),
          rot(X0, Y0 + 10, "24 horas", w=X1 - X0, tam=20, cor=MUDO, alinha="right")]
    cards = [(0, "t:stethoscope", "Teste de estímulo", "o que faz o diagnóstico no adulto, com endocrinologista", OXID, OXID_T),
             (200, "t:x", "IGFBP-3", "sem papel no diagnóstico de rotina do adulto", GLIC, GLIC_T)]
    for y, ic, t, d_, cor, fundo in cards:
        p.append(caixa(1060, y, 604, 170, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, 1082, y + 20, 52, cor))
        rs += [rot(1150, y + 24, t, w=500, tam=28, cor=cor, peso=700, serif=True),
               rot(1082, y + 88, d_, w=560, tam=22, cor=TINTA, lh=1.25)]
    return slide("dosar", 420, p, rs,
                 eyebrow="Terceira e quarta afirmações", titulo="GH isolado no sangue é quase inútil",
                 destaque="E a mulher em idade reprodutiva secreta mais GH por dia do que o homem.",
                 destaque_cor="tinta", fonte="Curva: esquema, sem valores medidos · Ho e colaboradores, Journal of Clinical Endocrinology and Metabolism 1987")


def jejum():
    """3.6: no jejum o GH sobe e o IGF-1 cai; e os dois IGF-1, o que circula e o que a fibra fabrica."""
    p = [svg_abre(1664, 430, "À esquerda, no jejum: a seta do GH sobe, a do IGF-1 cai, porque o fígado fica resistente ao GH. A frase de venda está pela metade. À direita, dois IGF-1: um vem do fígado e circula no sangue; o outro é fabricado dentro da fibra muscular sob tensão mecânica. Para hipertrofia, pesa mais o local"), defs(TINTA)]
    p.append(caixa(0, 0, 700, 430, GLIC, GLIC_T, esp=3, rx=16))
    rs = [rot(24, 16, "No jejum", w=650, tam=28, cor=GLIC, peso=700, serif=True)]
    barras = [(80, "GH", 260, AZUL, "sobe: é verdade e se mede", "t:trending-up"), (380, "IGF-1", 80, FOSF, "cai: o fígado fica resistente", "t:trending-down")]
    for x, t, h, cor, d, ic in barras:
        p.append(f'<rect x="{x}" y="{340 - 110}" width="120" height="110" rx="6" fill="{CINZA}"/>')
        p.append(f'<rect x="{x + 130}" y="{340 - h}" width="120" height="{h}" rx="6" fill="{cor}"/>')
        p.append(icone(ic, x + 150, 340 - h - 60, 50, cor))
        rs += [rot(x, 350, "antes", w=120, tam=20, cor=MUDO, alinha="center"), rot(x + 130, 350, "jejum", w=120, tam=20, cor=cor, peso=700, alinha="center"),
               rot(x, 60, t, w=250, tam=30, cor=cor, peso=700, serif=True),
               rot(x, 386, d, w=300, tam=20, cor=TINTA, lh=1.15)]
    # dois IGF-1
    rs.append(rot(780, 0, "Dois IGF-1", w=884, tam=28, cor=OXID, peso=700, serif=True))
    p.append(caixa(780, 60, 380, 130, MUDO, CARTAO, esp=2, rx=14))
    rs += [rot(800, 72, "do fígado", w=340, tam=24, cor=MUDO, peso=700), rot(800, 110, "circula no sangue", w=340, tam=22, cor=TINTA)]
    p.append(f'<rect x="1200" y="100" width="460" height="40" rx="20" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    for k in range(6):
        p.append(f'<circle cx="{1230 + k * 76}" cy="120" r="8" fill="{MUDO}"/>')
    p.append(seta(1162, 125, 1196, 120, MUDO, "m0", esp=3))
    # fibra
    p.append(f'<rect x="780" y="240" width="880" height="110" rx="55" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
    for k in range(9):
        p.append(f'<line x1="{840 + k * 90}" y1="262" x2="{840 + k * 90}" y2="328" stroke="{OXID}" stroke-width="3"/>')
    for k in range(5):
        p.append(f'<circle cx="{890 + k * 170}" cy="295" r="16" fill="{OXID}"/>')
    p.append(seta(740, 295, 772, 295, TINTA, "m0", esp=5))
    rs += [rot(780, 204, "o que a fibra fabrica sob tensão mecânica", w=880, tam=24, cor=OXID, peso=700),
           rot(780, 370, "para hipertrofia, pesa mais o local", w=880, tam=26, cor=OXID, peso=700)]
    return slide("jejum", 430, p, rs,
                 eyebrow="Sexta afirmação", titulo="“Jejum sobe o GH, logo é anabólico”",
                 destaque="Subir um fator de crescimento no sangue não reproduz o que a tensão produz dentro da fibra. O frasco não substitui a série.",
                 destaque_cor="petr", fonte="Barras: esquema, sem valores medidos")


def secretagogo():
    """3.6: o placar de dois anos de secretagogo: o que subiu, o que não mudou, o que piorou."""
    p = [svg_abre(1664, 420, "Um placar com seis linhas, depois de dois anos de secretagogo oral contra placebo em adultos de 60 a 81 anos. Subiram, em verde: GH e IGF-1, até a faixa do adulto jovem, e a massa livre de gordura. Não mudaram: força e função. Pioraram, em vermelho: a glicemia de jejum subiu, a sensibilidade à insulina caiu e o cortisol subiu")]
    linhas_ = [("GH e IGF-1", "até a faixa do adulto jovem", "t:trending-up", OXID, "subiu"),
               ("Massa livre de gordura", "", "t:trending-up", OXID, "subiu"),
               ("Força e função", "", "t:arrows-exchange", MUDO, "igual"),
               ("Glicemia de jejum", "", "t:trending-up", FOSF, "subiu"),
               ("Sensibilidade à insulina", "", "t:trending-down", FOSF, "caiu"),
               ("Cortisol", "", "t:trending-up", FOSF, "subiu")]
    blocos = [(0, "O que subiu", OXID, OXID_T, linhas_[:2]), (560, "O que não mudou", MUDO, PAPEL, linhas_[2:3]), (1120, "O que piorou", FOSF, FOSF_T, linhas_[3:])]
    rs = []
    for x, tit, cor, fundo, itens in blocos:
        p.append(caixa(x, 0, 544, 420, cor, fundo, esp=3, rx=16))
        rs.append(rot(x + 24, 16, tit, w=500, tam=28, cor=cor, peso=700, serif=True))
        for k, (t, d, ic, c, v) in enumerate(itens):
            y = 80 + k * 110
            p.append(f'<circle cx="{x+56}" cy="{y+36}" r="32" fill="{CARTAO}" stroke="{c}" stroke-width="3"/>')
            p.append(icone(ic, x + 34, y + 14, 44, c))
            rs.append(rot(x + 104, y + 8, t, w=420, tam=26, cor=TINTA, peso=700, lh=1.2))
            rs.append(rot(x + 104, y + 44, d if d else v, w=420, tam=22, cor=c, peso=600))
    return slide("secretagogo", 420, p, rs,
                 eyebrow="Dois anos de secretagogo oral, 2008", titulo="O biomarcador se move, a função não acompanha",
                 destaque="GH e secretagogos estão na lista proibida do controle antidopagem. Muita gente compra sem saber.",
                 destaque_cor="verm", fonte="Nass e colaboradores, Annals of Internal Medicine 2008 · 65 adultos saudáveis de 60 a 81 anos, secretagogo oral contra placebo")


def apneia():
    """3.6: a respiração da noite com pausas, e o quadro que ela imita."""
    import math
    p = [svg_abre(1664, 430, "Em cima, a respiração ao longo da noite em onda, com pausas planas marcadas: o ronco e as pausas que alguém viu. Embaixo, à esquerda, o quadro: homem de cinquenta e poucos anos, treina há anos, não ganha mais massa, acorda arrebentado, IGF-1 abaixo da faixa e pedido de GH pronto. À direita, os sinais que reconhecem a apneia de graça: ronco alto e pausas, sonolência de dia e ganho de peso, pressão difícil de controlar e álcool à noite")]
    pts = []
    for i in range(0, 1665, 4):
        pausa = any(a <= i <= a + 110 for a in (300, 760, 1200))
        v = 0 if pausa else 40 * math.sin(i / 22)
        pts.append((i, 80 - v))
    d = "M" + " L".join(f"{x} {y:.0f}" for x, y in pts)
    p.append(f'<path d="{d}" fill="none" stroke="{AZUL}" stroke-width="4"/>')
    for a in (300, 760, 1200):
        p.append(f'<rect x="{a}" y="30" width="110" height="100" rx="8" fill="{FOSF}" fill-opacity="0.12" stroke="{FOSF}" stroke-width="2"{TRACO}/>')
    rs = [rot(0, 136, "a respiração durante a noite; as pausas são a apneia", w=1000, tam=22, cor=MUDO),
          rot(1200, 136, "pausa", w=110, tam=20, cor=FOSF, peso=700, alinha="center")]
    p.append(caixa(0, 190, 780, 240, TINTA, PAPEL, esp=2, rx=16))
    rs += [rot(24, 204, "O quadro", w=730, tam=28, cor=TINTA, peso=700, serif=True),
           rot(24, 256, "homem de cinquenta e poucos anos, treina há anos", w=730, tam=22, cor=TINTA),
           rot(24, 302, "não ganha mais massa, acorda arrebentado", w=730, tam=22, cor=TINTA),
           rot(24, 348, "IGF-1 abaixo da faixa, pedido de GH pronto", w=730, tam=22, cor=FOSF, peso=700)]
    p.append(caixa(860, 190, 804, 240, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(884, 204, "A apneia se reconhece de graça", w=760, tam=28, cor=FOSF, peso=700, serif=True))
    sinais = [("t:volume", "ronco alto, pausas que alguém viu"), ("t:zzz", "sonolência de dia, ganho de peso"), ("t:heartbeat", "pressão difícil de controlar, álcool à noite")]
    for k, (ic, t) in enumerate(sinais):
        y = 256 + k * 50
        p.append(icone(ic, 884, y - 2, 36, FOSF))
        rs.append(rot(934, y, t, w=710, tam=22, cor=TINTA))
    return slide("apneia", 430, p, rs,
                 eyebrow="O IGF-1 baixo que vai aparecer", titulo="“Você ronca?”",
                 destaque="Acima de 45 anos, com IGF-1 baixo, fadiga e dificuldade de ganhar massa, a apneia entra no diferencial antes da deficiência de GH.",
                 destaque_cor="petr")


def condutas():
    """3.6: as três condutas em ordem, com o hipnograma da primeira metade da noite."""
    p = [svg_abre(1664, 420, "Três condutas em ordem. Um, proteger a primeira metade da noite: um hipnograma mostra o sono de ondas lentas concentrado nas primeiras horas, e o que o ameaça é álcool, sessão dura perto de deitar, apneia e sono picado. Dois, alimentar o eixo: energia disponível e proteína suficiente. Três, carregar o músculo: a série é o estímulo, não há substituto sistêmico"), defs(TINTA)]
    p.append(caixa(0, 0, 900, 420, OXID, OXID_T, esp=3, rx=16))
    rs = [rot(24, 16, "1 · Proteger a primeira metade da noite", w=850, tam=28, cor=OXID, peso=700, serif=True)]
    # hipnograma: profundidade por hora
    fases = [(0, 1), (0.3, 3), (0.8, 2), (1.1, 3), (1.7, 1), (2.0, 2), (2.3, 3), (2.7, 1), (3.1, 0), (3.3, 1), (4.0, 2), (4.4, 1), (4.9, 0), (5.1, 1), (6.0, 2), (6.3, 1), (6.8, 0), (7.0, 1), (8, 1)]
    X = lambda h: 120 + h * 95
    Y = lambda n: 110 + n * 50
    d = "M" + " ".join(f"{X(h):.0f} {Y(n)} L {X(fases[i+1][0]) if i + 1 < len(fases) else X(8):.0f} {Y(n)} L" for i, (h, n) in enumerate(fases)).rstrip(" L")
    p.append(f'<rect x="{X(0)}" y="{Y(2.5):.0f}" width="{X(4) - X(0)}" height="{Y(3.4) - Y(2.5):.0f}" fill="{OXID}" fill-opacity="0.18"/>')
    p.append(f'<path d="{d}" fill="none" stroke="{TINTA}" stroke-width="4"/>')
    for n, t in [(0, "REM"), (1, "leve"), (2, "médio"), (3, "profundo")]:
        rs.append(rot(10, Y(n) - 12, t, w=100, tam=20, cor=MUDO, alinha="right"))
    rs += [rot(X(0), 282, "primeira metade: o sono profundo, e o pulso maior de GH", w=370, tam=20, cor=OXID, peso=700, lh=1.2),
           rot(X(4) + 10, 282, "ameaças: álcool, sessão dura perto de deitar, apneia, sono picado", w=370, tam=20, cor=FOSF, peso=700, lh=1.2)]
    rs.append(rot(24, 360, "a única intervenção com mecanismo direto sobre este eixo, e gratuita", w=850, tam=22, cor=TINTA, lh=1.25))
    passos = [(0, "2 · Alimentar o eixo", "energia disponível e proteína suficiente", "t:salad", GLIC, GLIC_T),
              (220, "3 · Carregar o músculo", "a série é o estímulo; não há substituto sistêmico", "t:barbell", FOSF, FOSF_T)]
    for y, t, d_, ic, cor, fundo in passos:
        p.append(caixa(960, y, 704, 200, cor, fundo, esp=3, rx=16))
        p.append(icone(ic, 984, y + 70, 64, cor))
        rs += [rot(1068, y + 40, t, w=580, tam=28, cor=cor, peso=700, serif=True),
               rot(1068, y + 92, d_, w=580, tam=22, cor=TINTA, lh=1.25)]
    return slide("condutas", 420, p, rs,
                 eyebrow="O que sobra de prático", titulo="Três condutas, em ordem",
                 fonte="Hipnograma: esquema, sem valores medidos")


# ---------------------------------------------------------------- 3.7

def laudo():
    """3.7: os dois erros, um em linha do tempo, o outro em quem tem mais risco."""
    p = [svg_abre(1664, 420, "À esquerda, o primeiro erro, tratar a economia: T3 baixo com TSH normal e sintomas; hormônio prescrito; melhora no começo; a conta aparece depois, em massa magra e osso. À direita, o segundo erro, mais grave, não tratar a doença: hipotireoidismo é comum, sobretudo em mulher acima dos 40, em Hashimoto, no pós-parto e depois de radioiodo ou cirurgia"), defs(GLIC)]
    p.append(caixa(0, 0, 800, 420, GLIC, GLIC_T, esp=3, rx=16))
    rs = [rot(24, 16, "Primeiro erro: tratar a economia", w=750, tam=28, cor=GLIC, peso=700, serif=True)]
    passos = [("T3 baixo, TSH normal, sintomas", "t:clipboard-list"), ("hormônio prescrito", "t:pill"), ("melhora no começo", "t:trending-up"), ("a conta aparece depois: massa magra e osso", "t:alert-triangle")]
    for k, (t, ic) in enumerate(passos):
        y = 76 + k * 84
        p.append(f'<circle cx="60" cy="{y+30}" r="30" fill="{CARTAO}" stroke="{GLIC}" stroke-width="3"/>')
        p.append(icone(ic, 40, y + 10, 40, FOSF if k == 3 else GLIC))
        if k < 3:
            p.append(f'<line x1="60" y1="{y+62}" x2="60" y2="{y+82}" stroke="{GLIC}" stroke-width="3"/>')
        rs.append(rot(110, y + 16, t, w=660, tam=24, cor=FOSF if k == 3 else TINTA, peso=700 if k == 3 else 400))
    p.append(caixa(864, 0, 800, 420, FOSF, FOSF_T, esp=3, rx=16))
    rs += [rot(888, 16, "Segundo erro, mais grave: não tratar a doença", w=750, tam=28, cor=FOSF, peso=700, serif=True, lh=1.15),
           rot(888, 100, "hipotireoidismo é comum, sobretudo em:", w=750, tam=24, cor=TINTA)]
    grupos = [("h:woman", "mulher acima dos 40"), ("t:shield", "Hashimoto"), ("t:baby-carriage", "pós-parto"), ("t:first-aid-kit", "depois de radioiodo ou cirurgia")]
    for k, (ic, t) in enumerate(grupos):
        x, y = 888 + (k % 2) * 380, 160 + (k // 2) * 130
        p.append(f'<circle cx="{x+40}" cy="{y+40}" r="40" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"/>')
        p.append(icone(ic, x + 12, y + 12, 56, FOSF))
        rs.append(rot(x + 94, y + 14, t, w=270, tam=22, cor=TINTA, peso=600, lh=1.2))
    return slide("laudo", 420, p, rs,
                 eyebrow="O eixo que mais recebe prescrição desnecessária", titulo="A glândula falhou, ou o organismo economizou?",
                 destaque="O objetivo não é desconfiar de tireoide. É ter o discriminador.", destaque_cor="tinta")


def padrao():
    """3.7: o painel do T3 baixo, e as duas vias que o organismo troca."""
    p = [svg_abre(1664, 400, "À esquerda, um painel com quatro exames e a posição de cada um na faixa: T3 baixo; T3 reverso alto; T4 livre normal ou no limite de baixo; TSH normal ou um pouco reduzido. À direita, o T4 chega ao tecido e tem duas saídas: a via que ativa, que gera T3, fica fechada; a via que desativa, que gera T3 reverso, fica aberta"), defs(MUDO, GLIC)]
    exames = [("T3", "baixo", 0.08, FOSF), ("T3 reverso", "alto", 0.92, GLIC), ("T4 livre", "normal ou no limite de baixo", 0.34, TINTA), ("TSH", "normal ou um pouco reduzido", 0.4, OXID)]
    rs = []
    for k, (t, d, pos, cor) in enumerate(exames):
        y = k * 100
        rs += [rot(0, y + 10, t, w=200, tam=28, cor=cor, peso=700, serif=True), rot(0, y + 50, d, w=260, tam=20, cor=TINTA, lh=1.15)]
        p.append(f'<rect x="280" y="{y+30}" width="520" height="20" rx="10" fill="{CINZA}"/>')
        p.append(f'<rect x="400" y="{y+30}" width="280" height="20" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
        p.append(f'<circle cx="{280 + pos * 520:.0f}" cy="{y+40}" r="16" fill="{cor}" stroke="{CARTAO}" stroke-width="3"/>')
    rs.append(rot(400, 380, "faixa de referência", w=280, tam=20, cor=OXID, alinha="center"))
    # vias
    p.append(f'<circle cx="1000" cy="200" r="70" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
    rs.append(rot(930, 184, "T4", w=140, tam=30, cor=AZUL, peso=700, alinha="center", serif=True))
    p.append(f'<path d="M 1070 170 C 1150 120, 1200 90, 1290 90" fill="none" stroke="{CINZA}" stroke-width="6" stroke-dasharray="4 10"/>')
    p.append(f'<line x1="1160" y1="80" x2="1200" y2="140" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
    p.append(f'<path d="M 1070 230 C 1150 280, 1200 310, 1280 310" fill="none" stroke="{GLIC}" stroke-width="6" marker-end="url(#m1)"/>')
    p.append(caixa(1300, 50, 364, 80, MUDO, CARTAO, esp=2, rx=14))
    p.append(caixa(1300, 270, 364, 80, GLIC, GLIC_T, esp=3, rx=14))
    rs += [rot(1300, 60, "T3: a via que ativa", w=364, tam=24, cor=MUDO, peso=700, alinha="center"),
           rot(1300, 94, "fechada", w=364, tam=20, cor=FOSF, peso=700, alinha="center"),
           rot(1300, 280, "T3 reverso: a que desativa", w=364, tam=24, cor=GLIC, peso=700, alinha="center"),
           rot(1300, 314, "aberta", w=364, tam=20, cor=GLIC, peso=700, alinha="center")]
    return slide("padrao", 400, p, rs,
                 eyebrow="Passo dois", titulo="O padrão de economia: síndrome do T3 baixo",
                 destaque="Déficit de energia, doença aguda, trauma, jejum prolongado: o organismo desliga a via que ativa e liga a que desativa. Não é falha, é a resposta certa.",
                 destaque_cor="petr", fonte="Esquema, sem valores medidos")


def discriminador():
    """3.7: duas linhas de comando, uma com a hipófise gritando e outra com o ajuste na ponta."""
    p = [svg_abre(1664, 420, "Duas linhas de comando. Em cima, hipotireoidismo primário: a glândula não entrega, a hipófise grita mais alto, TSH alto. Embaixo, economia: a glândula entrega, a hipófise fala no tom de sempre, TSH normal, e o ajuste acontece na ponta, no tecido, com T3 baixo"), defs(FOSF, OXID, MUDO)]
    faixas = [(0, "Hipotireoidismo primário", FOSF, FOSF_T, "TSH alto", "acusa a glândula", True),
              (220, "Economia", OXID, OXID_T, "TSH normal, T3 baixo", "acusa a conta", False)]
    rs = []
    for y, t, cor, fundo, res, acusa, grito in faixas:
        p.append(f'<rect x="0" y="{y}" width="1664" height="200" rx="18" fill="{fundo}"/>')
        rs.append(rot(24, y + 12, t, w=600, tam=28, cor=cor, peso=700, serif=True))
        # hipófise
        p.append(f'<circle cx="160" cy="{y+120}" r="50" fill="{CARTAO}" stroke="{AZUL}" stroke-width="3"/>')
        rs.append(rot(90, y + 176, "hipófise", w=140, tam=20, cor=AZUL, alinha="center"))
        p.append(icone("t:speakerphone" if grito else "t:message-circle", 130 if grito else 136, y + 90, 60 if grito else 48, FOSF if grito else AZUL))
        p.append(seta(216, y + 120, 380 if grito else 360, y + 120, cor, "m0" if grito else "m1", esp=10 if grito else 4))
        # glândula
        tr = TRACO if grito else ""
        p.append(f'<path d="M 420 {y+80} q 50 -30 90 0 q 40 -30 90 0 q 20 40 -40 90 q -50 10 -100 0 q -60 -50 -40 -90 z" fill="{CARTAO}" stroke="{cor}" stroke-width="4"{tr}/>')
        rs.append(rot(420, y + 176, "tireoide: " + ("não entrega" if grito else "entrega"), w=200, tam=20, cor=cor, peso=700, alinha="center"))
        p.append(seta(640, y + 120, 840, y + 120, MUDO, "m2", esp=3 if grito else 5))
        # tecido
        p.append(caixa(860, y + 70, 220, 100, cor if not grito else MUDO, CARTAO, esp=3 if not grito else 2, rx=14))
        rs.append(rot(860, y + 104, "tecido" + ("" if grito else ": ajuste na ponta"), w=220, tam=20, cor=OXID if not grito else MUDO, peso=700, alinha="center", lh=1.15))
        p.append(caixa(1160, y + 60, 480, 120, cor, CARTAO, esp=4, rx=16))
        rs += [rot(1160, y + 76, res, w=480, tam=30, cor=cor, peso=700, alinha="center", serif=True),
               rot(1160, y + 126, acusa, w=480, tam=24, cor=TINTA, alinha="center")]
    return slide("discriminador", 420, p, rs,
                 eyebrow="Passo três: o discriminador", titulo="TSH alto acusa a glândula. T3 baixo com TSH normal acusa a conta.",
                 destaque="Na economia, o ajuste acontece na ponta, e o TSH não sobe.", destaque_cor="petr")


def pedir():
    """3.7: o pedido de exame com o que marcar e o que deixar de fora, e o tratamento padrão."""
    p = [svg_abre(1664, 420, "Um pedido de exame. Marcados: TSH e T4 livre, baratos e suficientes para a triagem. Condicional: anti-TPO, se houver suspeita de autoimunidade. Riscados para rastrear: T3, normal no hipotireoidismo inicial e baixo na economia; T3 reverso, sobe em quase tudo, sem corte que mude conduta. À direita, o tratamento: levotiroxina é o padrão; T3 manipulado para economia soma dois erros")]
    p.append(caixa(0, 0, 1000, 420, MUDO, PAPEL, esp=2, rx=14))
    p.append(f'<rect x="0" y="0" width="1000" height="60" rx="14" fill="{TINTA}"/><rect x="0" y="36" width="1000" height="24" fill="{TINTA}"/>')
    rs = [rot(24, 12, "Pedido para rastrear tireoide", w=900, tam=26, cor=PAPEL, peso=700, serif=True)]
    itens = [("TSH e T4 livre", "baratos, bastam para a triagem", "ok"), ("anti-TPO", "se houver suspeita de autoimunidade", "cond"),
             ("T3", "normal no hipotireoidismo inicial, baixo na economia", "nao"), ("T3 reverso", "sobe em quase tudo, sem corte que mude conduta", "nao")]
    for k, (t, d, st) in enumerate(itens):
        y = 80 + k * 74
        cor = {"ok": OXID, "cond": GLIC, "nao": FOSF}[st]
        p.append(f'<rect x="28" y="{y+6}" width="40" height="40" rx="8" fill="{CARTAO}" stroke="{cor}" stroke-width="3"/>')
        if st == "ok":
            p.append(icone("t:check", 30, y + 8, 36, OXID))
        elif st == "cond":
            p.append(icone("t:question-mark", 32, y + 10, 32, GLIC))
        else:
            p.append(icone("t:x", 32, y + 10, 32, FOSF))
        rs += [rot(92, y, t, w=260, tam=26, cor=cor, peso=700), rot(360, y + 4, d, w=610, tam=22, cor=TINTA, lh=1.2)]
        if st == "nao":
            p.append(f'<line x1="88" y1="{y+17}" x2="{96 + len(t) * 14.5:.0f}" y2="{y+17}" stroke="{FOSF}" stroke-width="3"/>')
    rs.append(rot(92, 380, "subclínico: decisão médica, caso a caso", w=880, tam=22, cor=MUDO))
    p.append(caixa(1064, 0, 600, 200, OXID, OXID_T, esp=3, rx=16))
    p.append(icone("t:pill", 1088, 24, 52, OXID))
    rs += [rot(1156, 28, "Levotiroxina é o padrão", w=490, tam=28, cor=OXID, peso=700, serif=True, lh=1.15),
           rot(1088, 104, "sem vantagem consistente das combinações com T3", w=550, tam=22, cor=TINTA, lh=1.25)]
    p.append(caixa(1064, 220, 600, 200, FOSF, FOSF_T, esp=3, rx=16))
    p.append(icone("t:alert-triangle", 1088, 244, 52, FOSF))
    rs += [rot(1156, 248, "T3 manipulado para economia", w=490, tam=28, cor=FOSF, peso=700, serif=True, lh=1.15),
           rot(1088, 324, "soma dois erros: trata o que não é doença, com o que não é padrão", w=550, tam=22, cor=TINTA, lh=1.25)]
    return slide("pedir", 420, p, rs,
                 eyebrow="Na ordem certa", titulo="O que pedir, e o que não pedir para rastrear",
                 fonte="Jonklaas e colaboradores, American Thyroid Association 2014")


def roteiro_tireoide():
    """3.7: cinco passos, com a bifurcação entre conta e glândula no terceiro."""
    p = [svg_abre(1664, 420, "Um fluxo. Um, a história: quanto come, quanto treina, se cortou carboidrato, quanto peso perdeu. Dois, TSH e T4 livre, e anti-TPO se houver suspeita de autoimunidade. Três, o discriminador. Dele saem dois caminhos: TSH alto aponta a glândula e leva ao passo cinco, conduta médica, levotiroxina, subclínico caso a caso; T3 baixo com TSH normal aponta a conta e leva ao passo quatro, restaurar energia, com nutricionista, carga revista e exame repetido depois"), defs(TINTA, GLIC, FOSF)]
    passos = [("1", "A história", "quanto come, quanto treina, se cortou carboidrato, quanto peso perdeu", OXID),
              ("2", "TSH e T4 livre", "anti-TPO se houver suspeita de autoimunidade", TINTA),
              ("3", "O discriminador", "TSH alto ou T3 baixo com TSH normal?", TINTA)]
    rs = []
    for k, (n, t, d, cor) in enumerate(passos):
        x = k * 360
        p.append(caixa(x, 110, 320, 200, cor, CARTAO, esp=3, rx=16))
        p.append(f'<circle cx="{x+40}" cy="150" r="24" fill="{cor}"/>')
        rs += [rot(x + 16, 136, n, w=48, tam=26, cor=PAPEL, peso=700, alinha="center"),
               rot(x + 76, 132, t, w=230, tam=26, cor=cor, peso=700, lh=1.1),
               rot(x + 20, 196, d, w=280, tam=21, cor=TINTA, lh=1.25)]
        if k < 2:
            p.append(seta(x + 324, 210, x + 356, 210, TINTA, "m0", esp=4))
    p.append(f'<path d="M 1044 180 C 1100 180, 1100 90, 1150 90" fill="none" stroke="{GLIC}" stroke-width="5" marker-end="url(#m1)"/>')
    p.append(f'<path d="M 1044 240 C 1100 240, 1100 330, 1150 330" fill="none" stroke="{FOSF}" stroke-width="5" marker-end="url(#m2)"/>')
    rs += [rot(1040, 60, "conta", w=100, tam=20, cor=GLIC, peso=700), rot(1030, 356, "glândula", w=120, tam=20, cor=FOSF, peso=700)]
    saidas = [(0, "4", "Economia: restaurar energia", "nutricionista, carga revista, exame repetido depois", GLIC, GLIC_T),
              (240, "5", "Glândula: conduta médica", "levotiroxina; subclínico caso a caso", FOSF, FOSF_T)]
    for y, n, t, d, cor, fundo in saidas:
        p.append(caixa(1164, y, 500, 180, cor, fundo, esp=3, rx=16))
        p.append(f'<circle cx="1204" cy="{y+40}" r="24" fill="{cor}"/>')
        rs += [rot(1180, y + 26, n, w=48, tam=26, cor=PAPEL, peso=700, alinha="center"),
               rot(1240, y + 22, t, w=410, tam=24, cor=cor, peso=700, lh=1.15),
               rot(1188, y + 96, d, w=460, tam=21, cor=TINTA, lh=1.25)]
    return slide("roteiro", 420, p, rs,
                 eyebrow="O procedimento", titulo="Cinco passos, com a história antes do exame")


# ---------------------------------------------------------------- 3.8

def retro():
    """3.8: o mesmo dia de consulta e três futuros que só se conhecem olhando para trás."""
    p = [svg_abre(1664, 430, "Um ponto marca o dia da consulta: pessoa cansada, desempenho caindo. Dele saem três curvas de volta ao normal: uma em cerca de dez dias, outra em semanas, outra em dez meses. Até o dia da consulta, as três são iguais; depois, uma área cinzenta com um ponto de interrogação: naquele dia não há como saber qual delas é. A primeira conduta é parecida nas três")]
    X0, X1, Yb, Yc = 60, 1640, 70, 330
    p.append(f'<line x1="{X0}" y1="{Yb}" x2="{X1}" y2="{Yb}" stroke="{CINZA}" stroke-width="2"{TRACO}/>')
    p.append(f'<path d="M {X0} {Yb} C {X0+120} {Yb}, {X0+200} {Yc}, 360 {Yc}" fill="none" stroke="{TINTA}" stroke-width="6"/>')
    p.append(f'<circle cx="360" cy="{Yc}" r="16" fill="{TINTA}"/>')
    p.append(f'<rect x="376" y="20" width="{X1 - 376}" height="340" fill="{MUDO}" fill-opacity="0.07"/>')
    futuros = [(460, OXID, "cerca de dez dias"), (820, GLIC, "semanas"), (1560, FOSF, "dez meses")]
    rs = [rot(200, 360, "hoje, na consulta: cansaço, desempenho caindo", w=480, tam=22, cor=TINTA, peso=700, lh=1.2),
          rot(X0, Yb - 40, "o desempenho de antes", w=400, tam=20, cor=MUDO)]
    for xv, cor, t in futuros:
        p.append(f'<path d="M 360 {Yc} C {360 + (xv-360)*0.5} {Yc}, {360 + (xv-360)*0.6} {Yb}, {xv} {Yb}" fill="none" stroke="{cor}" stroke-width="5"/>')
        p.append(f'<circle cx="{xv}" cy="{Yb}" r="10" fill="{cor}"/>')
        rs.append(rot(xv - 140, Yb - 44, t, w=280, tam=22, cor=cor, peso=700, alinha="center"))
    p.append(icone("t:question-mark", 1100, 150, 110, MUDO))
    rs.append(rot(900, 280, "só se sabe olhando para trás", w=560, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
    return slide("retro", 430, p, rs,
                 eyebrow="A coisa mais importante da aula", titulo="O diagnóstico é retrospectivo",
                 destaque="A boa notícia: a primeira conduta é parecida nos três.", destaque_cor="petr",
                 fonte="Esquema, sem valores medidos")


def criterio_ot():
    """3.8: a definição sublinhada palavra por palavra, e o exame que não entra nela."""
    p = [svg_abre(1664, 420, "A definição escrita em uma linha, com cada trecho sublinhado e uma nota embaixo: queda de desempenho, pressupõe um antes medido; inexplicada, obriga o diferencial; apesar de repouso adequado, carga bem reduzida por semanas; com sintomas, fadiga, sono, humor, apetite, infecções; outras causas afastadas, diagnóstico de exclusão. À parte, riscado: nenhum exame, nenhum hormônio, nenhuma razão entre marcadores")]
    trechos = [("Queda de desempenho", "pressupõe um “antes” medido", TINTA, 0, 10, 400),
               ("inexplicada,", "obriga o diferencial", FOSF, 440, 10, 260),
               ("apesar de repouso adequado,", "carga bem reduzida por semanas", TINTA, 740, 10, 520),
               ("com sintomas,", "fadiga, sono, humor, apetite, infecções", TINTA, 0, 230, 330),
               ("outras causas afastadas", "diagnóstico de exclusão", FOSF, 370, 230, 440)]
    rs = []
    for t, d, cor, x, y, w in trechos:
        rs.append(rot(x, y, t, w=w, tam=32, cor=cor, peso=700, serif=True))
        p.append(f'<line x1="{x}" y1="{y+52}" x2="{x+w-20}" y2="{y+52}" stroke="{cor}" stroke-width="5"/>')
        p.append(f'<line x1="{x+20}" y1="{y+56}" x2="{x+20}" y2="{y+86}" stroke="{cor}" stroke-width="2"/>')
        rs.append(rot(x + 30, y + 78, d, w=w - 30, tam=24, cor=TINTA, lh=1.2))
    p.append(caixa(1100, 220, 564, 170, GLIC, GLIC_T, esp=3, rx=16))
    p.append(icone("t:droplet", 1124, 250, 56, GLIC))
    p.append(f'<line x1="1120" y1="310" x2="1190" y2="246" stroke="{FOSF}" stroke-width="6"/>')
    rs += [rot(1200, 242, "Nenhum exame", w=440, tam=28, cor=GLIC, peso=700, serif=True),
           rot(1200, 290, "nenhum hormônio, nenhuma razão entre marcadores", w=440, tam=22, cor=TINTA, lh=1.25)]
    return slide("criterio", 420, p, rs,
                 eyebrow="O que existe como critério", titulo="Cada palavra carrega trabalho",
                 fonte="Meeusen e colaboradores, consenso ECSS e ACSM 2013")


def exame_ot():
    """3.8: muitas publicações e poucos instrumentos, e por que validar é tão difícil."""
    p = [svg_abre(1664, 420, "À esquerda, uma pilha alta de publicações sobre o tema ao lado de uma pilha baixa de instrumentos válidos; mais de vinte anos depois, mudou pouco. À direita, a linha do tempo de por que validar é difícil: seria preciso medir antes do quadro, mas ninguém sabe quem vai entrar nele; o quadro aparece; o padrão-ouro só confirma olhando para trás. Embaixo, dois testes separados por quatro horas: protocolo de pesquisa hormonal, não de consultório"), defs(MUDO)]
    for k in range(12):
        p.append(f'<rect x="{40 + (k % 2) * 6}" y="{330 - k * 26}" width="200" height="22" rx="3" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="2"/>')
    for k in range(2):
        p.append(f'<rect x="320" y="{330 - k * 26}" width="200" height="22" rx="3" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
    rs = [rot(20, 364, "publicações sobre o tema", w=240, tam=22, cor=AZUL, peso=700, alinha="center", lh=1.2),
          rot(300, 364, "instrumentos válidos", w=240, tam=22, cor=OXID, peso=700, alinha="center", lh=1.2),
          rot(300, 200, "mais de vinte anos depois, mudou pouco", w=280, tam=22, cor=TINTA, lh=1.25)]
    # linha do tempo
    X0 = 700
    p.append(f'<line x1="{X0}" y1="120" x2="1640" y2="120" stroke="{MUDO}" stroke-width="3" marker-end="url(#m0)"/>')
    marcos = [(X0 + 60, "medir antes do quadro", "ninguém sabe quem vai entrar nele", True),
              (X0 + 420, "o quadro aparece", "", False),
              (X0 + 760, "o padrão-ouro confirma", "olhando para trás", False)]
    for x, t, d, falta in marcos:
        if falta:
            p.append(f'<circle cx="{x}" cy="120" r="18" fill="{CARTAO}" stroke="{FOSF}" stroke-width="4" stroke-dasharray="6 5"/>')
        else:
            p.append(f'<circle cx="{x}" cy="120" r="18" fill="{TINTA}"/>')
        rs.append(rot(x - 140, 20, t, w=280, tam=22, cor=FOSF if falta else TINTA, peso=700, alinha="center", lh=1.15))
        if d:
            rs.append(rot(x - 140, 150, d, w=280, tam=20, cor=TINTA, alinha="center", lh=1.2))
    p.append(caixa(X0, 250, 964, 150, TINTA, PAPEL, esp=2, rx=16))
    p.append(icone("t:clock", X0 + 24, 290, 60, TINTA))
    rs += [rot(X0 + 104, 268, "dois testes com 4 horas de intervalo", w=830, tam=26, cor=TINTA, peso=700),
           rot(X0 + 104, 318, "protocolo de pesquisa hormonal, não de consultório", w=830, tam=22, cor=MUDO)]
    return slide("exame", 420, p, rs,
                 eyebrow="Uma revisão de 2002", titulo="“Que ferramentas diagnósticas nós temos?”",
                 destaque="Painel que “diagnostica overtraining” vende o que não existe. Relação testosterona-cortisol: reconhecer, não decidir.",
                 destaque_cor="ambar", fonte="Urhausen e Kindermann, Sports Medicine 2002 · Meeusen e colaboradores 2013")


def instrumentos():
    """3.8: três instrumentos sem sangue, cada um com o seu desenho, e o histórico de carga acima deles."""
    p = [svg_abre(1664, 440, "Três instrumentos, nenhum de sangue. Teste padronizado repetido: o mesmo percurso, com o tempo anotado em datas. Esforço para carga fixa: a mesma carga com a percepção de esforço subindo semana a semana. Humor e recuperação: questionário validado com mais fadiga e menos vigor. Em cima dos três, o histórico de carga escrito, que vale mais: às vezes a carga não mudou, mudou a vida")]
    p.append(caixa(0, 0, 1664, 110, TINTA, PAPEL, esp=3, rx=16))
    p.append(icone("t:notebook", 24, 24, 62, TINTA))
    rs = [rot(110, 16, "O histórico de carga escrito vale mais que os três", w=1520, tam=28, cor=TINTA, peso=700, serif=True),
          rot(110, 62, "às vezes a carga não mudou; mudou a vida", w=1520, tam=22, cor=MUDO)]
    W = 528
    tits = [("Teste padronizado repetido", "mesmo percurso ou carga, mesma condição"),
            ("Esforço para carga fixa", "mesma carga, percepção subindo por semanas"),
            ("Humor e recuperação", "questionários validados: mais fadiga, menos vigor")]
    for j, (t, d) in enumerate(tits):
        x = j * (W + 40)
        p.append(caixa(x, 140, W, 300, OXID, CARTAO, esp=3, rx=16))
        rs += [rot(x + 24, 154, t, w=W - 48, tam=26, cor=OXID, peso=700, serif=True),
               rot(x + 24, 196, d, w=W - 48, tam=20, cor=TINTA, lh=1.2)]
    # 1: tempos em datas
    x = 0
    for k, v in enumerate([0, 4, 10, 18]):
        p.append(f'<rect x="{x + 60 + k * 110}" y="{400 - 80 - v}" width="70" height="{80 + v}" rx="4" fill="{AZUL}"/>')
        rs.append(rot(x + 40 + k * 110, 404, f"sem {1 + k * 2}", w=110, tam=18, cor=MUDO, alinha="center"))
    rs.append(rot(x + 30, 250, "tempo no mesmo percurso, subindo", w=460, tam=20, cor=AZUL, peso=700))
    # 2: percepção subindo
    x = W + 40
    pts = [(0, 30), (1, 34), (2, 46), (3, 62), (4, 80)]
    d = "M" + " L".join(f"{x + 60 + a * 100} {390 - b * 1.6:.0f}" for a, b in pts)
    p.append(f'<line x1="{x+60}" y1="390" x2="{x+480}" y2="390" stroke="{MUDO}" stroke-width="2"/>')
    p.append(f'<path d="{d}" fill="none" stroke="{FOSF}" stroke-width="6" stroke-linejoin="round"/>')
    rs += [rot(x + 60, 400, "semanas, carga fixa", w=420, tam=18, cor=MUDO, alinha="center"),
           rot(x + 30, 250, "percepção de esforço, subindo", w=460, tam=20, cor=FOSF, peso=700)]
    # 3: questionário
    x = 2 * (W + 40)
    for k, (t, v, cor) in enumerate([("fadiga", 0.85, FOSF), ("vigor", 0.25, OXID), ("sono", 0.4, AZUL)]):
        y = 270 + k * 50
        rs.append(rot(x + 30, y - 4, t, w=100, tam=20, cor=TINTA))
        p.append(f'<rect x="{x+140}" y="{y}" width="340" height="18" rx="9" fill="{CINZA}"/>')
        p.append(f'<rect x="{x+140}" y="{y}" width="{340 * v:.0f}" height="18" rx="9" fill="{cor}"/>')
    return slide("instrumentos", 440, p, rs,
                 eyebrow="O que funciona", titulo="Três instrumentos, nenhum de sangue",
                 fonte="Esquemas, sem valores medidos")


def subjetivo():
    """3.8: a mesma carga, e quem acusou primeiro: as medidas subjetivas ou as objetivas."""
    p = [svg_abre(1664, 420, "No alto, um aumento de carga. Embaixo, duas colunas de medidas acompanhando essa carga. Medidas subjetivas: bem-estar, sono percebido, dor muscular, estresse e humor, com os indicadores acesos, porque responderam à carga de forma mais sensível e consistente. Objetivas habituais: frequência cardíaca de repouso e marcadores de sangue, com os indicadores mais apagados, porque responderam menos"), defs(TINTA)]
    p.append(f'<path d="M 0 90 L 500 90 L 560 20 L 1664 20 L 1664 90 Z" fill="{GLIC_T}"/>')
    p.append(f'<path d="M 0 90 L 500 90 L 560 20 L 1664 20" fill="none" stroke="{GLIC}" stroke-width="5"/>')
    rs = [rot(20, 40, "a carga aumenta", w=400, tam=22, cor=GLIC, peso=700)]
    cols = [(0, "Medidas subjetivas", OXID, OXID_T, [("t:mood-smile", "bem-estar"), ("t:bed", "sono percebido"), ("t:barbell", "dor muscular"), ("t:brain", "estresse"), ("t:mood-neutral", "humor")], 5,
             "responderam à carga de forma mais sensível e consistente"),
            (872, "Objetivas habituais", MUDO, PAPEL, [("t:heartbeat", "frequência cardíaca de repouso"), ("t:droplet", "marcadores de sangue")], 2, "responderam menos")]
    for x, t, cor, fundo, itens, acesos, nota in cols:
        p.append(caixa(x, 120, 792, 300, cor, fundo, esp=3, rx=16))
        rs.append(rot(x + 24, 132, t, w=740, tam=28, cor=cor, peso=700, serif=True))
        for k, (ic, it) in enumerate(itens):
            cx = x + 24 + (k % 3) * 250
            cy = 186 + (k // 3) * 80
            p.append(icone(ic, cx, cy, 40, cor))
            rs.append(rot(cx + 50, cy + 6, it, w=190, tam=21, cor=TINTA, lh=1.15))
        for k in range(5):
            on = (k < 4) if cor == OXID else (k < 1)
            p.append(f'<rect x="{x + 24 + k * 44}" y="360" width="36" height="36" rx="6" fill="{cor if on else CINZA}"/>')
        rs.append(rot(x + 260, 356, nota, w=510, tam=22, cor=cor if cor == OXID else TINTA, peso=700, lh=1.2))
    return slide("subjetivo", 420, p, rs,
                 eyebrow="Uma revisão sistemática, 2016", titulo="A pergunta bem feita supera o exame",
                 destaque="O problema não é que falte instrumento. É que o instrumento que funciona não parece instrumento.",
                 destaque_cor="petr", fonte="Saw, Main e Gastin, British Journal of Sports Medicine 2016 · indicadores: esquema, sem valores medidos")


def saidas_ot():
    """3.8: manter só sob condição, ou o teste de descarga desenhado em barras de carga."""
    p = [svg_abre(1664, 420, "À esquerda, a saída A, manter a carga como se fosse funcional: só com sobrecarga planejada e curta, e descarga real que a vida permite cumprir; faltou uma, está fora. À direita, a saída B, o teste de descarga: barras de carga semanal com três semanas bem reduzidas mas não zeradas, frequência e alguma intensidade curta mantidas, e os marcadores anotados antes de começar"), defs(TINTA)]
    p.append(caixa(0, 0, 600, 420, FOSF, FOSF_T, esp=3, rx=16))
    rs = [rot(24, 16, "A: manter, como se fosse funcional", w=560, tam=26, cor=FOSF, peso=700, serif=True, lh=1.15)]
    cond = ["sobrecarga planejada e curta", "descarga real que a vida permite cumprir"]
    for k, t in enumerate(cond):
        y = 110 + k * 90
        p.append(f'<rect x="24" y="{y}" width="40" height="40" rx="8" fill="{CARTAO}" stroke="{FOSF}" stroke-width="3"/>')
        rs.append(rot(80, y + 4, t, w=500, tam=24, cor=TINTA, lh=1.2))
    rs += [rot(24, 70, "só com as duas:", w=560, tam=22, cor=MUDO),
           rot(24, 300, "faltou uma: está fora", w=560, tam=28, cor=FOSF, peso=700, serif=True)]
    # B
    x0 = 660
    rs.append(rot(x0, 0, "B: o teste de descarga", w=1004, tam=28, cor=OXID, peso=700, serif=True))
    cargas = [100, 105, 110, 108, 45, 45, 45, None]
    for k, c in enumerate(cargas):
        x = x0 + 40 + k * 120
        if c is None:
            p.append(f'<rect x="{x}" y="120" width="80" height="210" rx="6" fill="none" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 6"/>')
            rs.append(rot(x - 20, 180, "reavaliar", w=120, tam=20, cor=MUDO, alinha="center"))
        else:
            h = c * 1.9
            p.append(f'<rect x="{x}" y="{330 - h:.0f}" width="80" height="{h:.0f}" rx="6" fill="{GLIC if k < 4 else OXID}"/>')
        rs.append(rot(x - 20, 338, f"sem {k + 1}", w=120, tam=18, cor=MUDO, alinha="center"))
    p.append(f'<line x1="{x0 + 520}" y1="60" x2="{x0 + 520}" y2="330" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
    p.append(icone("t:notebook", x0 + 490, 60, 44, TINTA))
    rs += [rot(x0 + 540, 60, "marcadores anotados antes", w=400, tam=22, cor=TINTA, peso=700),
           rot(x0 + 540, 96, "2 a 3 semanas: bem reduzida, não zerada", w=440, tam=20, cor=OXID, peso=700, lh=1.2),
           rot(x0, 376, "frequência e alguma intensidade curta mantidas", w=1004, tam=22, cor=TINTA)]
    return slide("saidas", 420, p, rs,
                 eyebrow="A encruzilhada", titulo="Manter a carga, ou reduzir e reavaliar",
                 destaque="Avise que os primeiros dias vão ser ruins. Sem aviso, a pessoa abandona no terceiro dia achando que precisava treinar mais.",
                 destaque_cor="ambar", fonte="Barras: esquema, sem valores medidos")


def criterioC():
    """3.8: as bandeiras que mandam investigar antes, e o que reavaliar em quatro a seis semanas."""
    p = [svg_abre(1664, 420, "À esquerda, a saída C, investigar antes de mexer, com quatro bandeiras: perda de peso sem intenção, febre, suor noturno; gânglios, falta de ar desproporcional, dor no peito; palpitação com sensação de desmaio, ideação suicida; fadiga de meses sem mudança de carga. À direita, uma régua de seis semanas com a reavaliação marcada entre a quarta e a sexta: esforço na mesma sessão, qualidade do sono, vigor e motivação numa escala simples, teste padronizado com data")]
    p.append(caixa(0, 0, 800, 420, FOSF, FOSF_T, esp=3, rx=16))
    rs = [rot(24, 16, "C: investigar antes de mexer", w=750, tam=28, cor=FOSF, peso=700, serif=True)]
    band = [("t:scale", "perda de peso sem intenção, febre, suor noturno"), ("t:heartbeat", "gânglios, falta de ar desproporcional, dor no peito"),
            ("t:alert-triangle", "palpitação com sensação de desmaio, ideação suicida"), ("t:calendar", "fadiga de meses sem mudança de carga")]
    for k, (ic, t) in enumerate(band):
        y = 76 + k * 84
        p.append(icone("t:flag", 24, y + 4, 40, FOSF))
        p.append(icone(ic, 72, y + 4, 40, FOSF))
        rs.append(rot(128, y + 4, t, w=650, tam=23, cor=TINTA, lh=1.2))
    X0, X1 = 900, 1640
    rs.append(rot(864, 0, "Reavaliar em 4 a 6 semanas", w=800, tam=28, cor=OXID, peso=700, serif=True))
    p.append(f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{MUDO}" stroke-width="3"/>')
    for k in range(7):
        x = X0 + k * (X1 - X0) / 6
        p.append(f'<line x1="{x:.0f}" y1="100" x2="{x:.0f}" y2="120" stroke="{MUDO}" stroke-width="3"/>')
        rs.append(rot(x - 30, 124, str(k), w=60, tam=20, cor=MUDO, alinha="center"))
    xa, xb = X0 + 4 * (X1 - X0) / 6, X1
    p.append(f'<rect x="{xa:.0f}" y="90" width="{xb - xa:.0f}" height="40" rx="10" fill="{OXID}" fill-opacity="0.25"/>')
    rs.append(rot(X0, 60, "semanas", w=200, tam=20, cor=MUDO))
    marc = ["esforço na mesma sessão", "qualidade do sono", "vigor e motivação numa escala simples", "teste padronizado, com data"]
    for k, t in enumerate(marc):
        y = 180 + k * 60
        p.append(f'<rect x="{X0 - 36}" y="{y+2}" width="32" height="32" rx="6" fill="{CARTAO}" stroke="{OXID}" stroke-width="3"/>')
        p.append(icone("t:check", X0 - 34, y + 4, 28, OXID))
        rs.append(rot(X0 + 10, y + 2, t, w=740, tam=23, cor=TINTA))
    return slide("criterioC", 420, p, rs,
                 eyebrow="Saída C e o critério", titulo="B e C em paralelo; A precisa ser justificada",
                 destaque="A primeira conduta é a mesma nos três estados, e reduzir carga não atrapalha investigação nenhuma.",
                 destaque_cor="petr")


# ---------------------------------------------------------------- aplicação

LICOES = {"03-01": [laudos, pares, anamnese, ficha, cinco],
          "03-02": [vilao, funcao, cuidados, investigar, fadiga],
          "03-03": [origem, efeitos, beta, limites],
          "03-04": [pedido, verdades, estradiol, saidaA, saidaC, criterio],
          "03-05": [portas, auditar, acionaveis, escondem, exame, dizer, roteiro],
          "03-06": [enquadre, dosar, jejum, secretagogo, apneia, condutas],
          "03-07": [laudo, padrao, discriminador, pedir, roteiro_tireoide],
          "03-08": [retro, criterio_ot, exame_ot, instrumentos, subjetivo, saidas_ot, criterioC]}

def aplicar(S, licao):
    """Troca, em S, cada slide de texto da aula pelo desenho de mesmo id."""
    novos = {d["id"]: d for d in (f() for f in LICOES.get(licao, []))}
    ids = {s["id"] for s in S}
    falta = set(novos) - ids
    assert not falta, f"{licao}: desenho sem slide correspondente: {falta}"
    return [novos.get(s["id"], s) for s in S]
