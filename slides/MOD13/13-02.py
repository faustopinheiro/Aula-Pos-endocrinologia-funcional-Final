"""Spec do deck 13.2. Gera 13-02.json ao lado deste arquivo."""
from _base import *

S = []
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]

# 1. a linha do tempo até a consulta
def m1(m):
    """Posição do mês m (0 a 6) na primeira parte da linha."""
    return 60 + m * 150


p = [svg_abre(1664, 440, "Linha do tempo com meses ilustrativos. Mês 0: primeira lesão de posterior de coxa no jogo de quinta. Meses 1 e 2: fisioterapia com o protocolo de clube. Mês 3: liberado. Sete semanas depois: mesmo músculo, mesmo lado. Mês 6: a consulta. Depois, o resto da linha, no fim da conversa")]
rs = []
p.append(f'<line x1="{m1(0)}" y1="380" x2="{m1(6)}" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{m1(6)}" y1="380" x2="1600" y2="380" stroke="{MUDO}" stroke-width="3" stroke-dasharray="10 8"/>')
for m in range(7):
    p.append(f'<line x1="{m1(m)}" y1="372" x2="{m1(m)}" y2="388" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(m1(m) - 50, 396, f"mês {m}", w=100, tam=20, cor=MUDO, alinha="center"))
p.append(camisa(10, 10, 110, AZUL))
p.append(icone("t:bolt", 128, 30, 64, FOSF))
p.append(f'<circle cx="{m1(0)}" cy="380" r="14" fill="{FOSF}"/>')
rs.append(rot(10, 140, "primeira lesão, no jogo de quinta", w=300, tam=22, cor=FOSF, peso=700, lh=1.2))
p.append(caixa(m1(0.4), 240, m1(2.6) - m1(0.4), 70, OXID, OXID_T, esp=2, rx=14))
rs.append(rot(m1(0.4) + 10, 248, "fisioterapia com o protocolo de clube", w=m1(2.6) - m1(0.4) - 20, tam=22, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append(f'<circle cx="{m1(3)}" cy="380" r="14" fill="{OXID}"/>')
p.append(icone("t:check", m1(3) - 26, 160, 52, OXID))
rs.append(rot(m1(3) - 70, 220, "liberado", w=140, tam=22, cor=OXID, peso=700, alinha="center"))
X2 = m1(4.6)
p.append(f'<path d="M {m1(3)} 330 L {m1(3)} 340 L {X2} 340 L {X2} 330" stroke="{MUDO}" stroke-width="3" fill="none"/>')
rs.append(rot(m1(3) + 10, 294, "sete semanas", w=X2 - m1(3) - 20, tam=20, cor=MUDO, peso=600, alinha="center"))
p.append(f'<circle cx="{X2}" cy="380" r="14" fill="{FOSF}"/>')
p.append(icone("t:bolt", X2 - 32, 60, 64, FOSF))
rs.append(rot(X2 - 110, 136, "mesmo músculo, mesmo lado", w=220, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
p.append(f'<circle cx="{m1(6)}" cy="380" r="14" fill="{AZUL}"/>')
p.append(icone("h:doctor", m1(6) - 32, 150, 64, AZUL))
rs.append(rot(m1(6) - 80, 226, "a consulta", w=160, tam=22, cor=AZUL, peso=700, alinha="center"))
p.append(f'<rect x="1030" y="30" width="610" height="300" rx="16" fill="{CARTAO}" stroke="{GRADE}" stroke-width="2" stroke-dasharray="8 6"/>')
rs.append(rot(1060, 140, "o resto da linha, no fim da conversa", w=550, tam=26, cor=MUDO, peso=600, alinha="center", serif=True))
rs.append(rot(1500, 396, "mês 24", w=100, tam=20, cor=MUDO, alinha="right"))
rs.append(rot(1060, 396, "meses ilustrativos", w=300, tam=20, cor=MUDO))
diagrama(S, "linha", 440, p, rs, eyebrow="Um jogador de society na casa dos quarenta", titulo="Duas lesões no mesmo músculo, com o protocolo certo")

# 2. as duas semanas
p = [svg_abre(1664, 470, "36 lesões por mil horas de jogo e 3,7 por mil horas de treino no futebol profissional masculino, cerca de dez vezes. A semana do profissional: cinco treinos, um jogo e uma folga. A semana do society: seis dias vazios e o jogo na quinta. Cem por cento da exposição na faixa de maior risco")]
rs = []
p.append(caixa(0, 0, 500, 120, FOSF, FOSF_T, esp=3, rx=16))
rs += [rot(20, 14, "36", w=140, tam=64, cor=FOSF, peso=700, serif=True),
       rot(170, 30, "lesões por mil horas de jogo", w=310, tam=24, cor=TINTA, peso=700, lh=1.2)]
rs.append(rot(520, 40, "cerca de dez vezes", w=240, tam=24, cor=MUDO, peso=700, alinha="center"))
p.append(caixa(780, 0, 500, 120, AZUL, AZUL_T, esp=3, rx=16))
rs += [rot(800, 14, "3,7", w=140, tam=64, cor=AZUL, peso=700, serif=True),
       rot(950, 30, "por mil horas de treino", w=310, tam=24, cor=TINTA, peso=700, lh=1.2)]
rs.append(rot(1310, 30, "futebol profissional masculino, metanálise", w=354, tam=22, cor=MUDO, peso=600, lh=1.25))
XD, WD = 300, 186
for j, d in enumerate(DIAS):
    rs.append(rot(XD + j * (WD + 8), 150, d, w=WD, tam=22, cor=MUDO, peso=700, alinha="center"))
linhas = [("o profissional", 190, ["t", "t", "t", "t", "t", "j", ""]), ("o society de quinta", 300, ["", "", "", "j", "", "", ""])]
for nome, y, sem in linhas:
    rs.append(rot(0, y + 22, nome, w=280, tam=26, cor=TINTA, peso=700, serif=True))
    for j, k in enumerate(sem):
        x = XD + j * (WD + 8)
        if k == "t":
            p.append(f'<rect x="{x}" y="{y}" width="{WD}" height="80" rx="12" fill="{AZUL}"/>')
        elif k == "j":
            p.append(f'<rect x="{x}" y="{y}" width="{WD}" height="80" rx="12" fill="{FOSF}"/>')
            rs.append(rot(x, y + 24, "jogo", w=WD, tam=24, cor=PAPEL, peso=700, alinha="center"))
        else:
            p.append(f'<rect x="{x}" y="{y}" width="{WD}" height="80" rx="12" fill="none" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
rs.append(rot(XD, 214, "treino", w=WD, tam=24, cor=PAPEL, peso=700, alinha="center"))
rs.append(rot(XD, 410, "100% da exposição na faixa de maior risco, nenhum minuto construindo capacidade", w=1364, tam=24, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "semanas", 470, p, rs, eyebrow="Dois números do futebol profissional", titulo="Quem tem clube treina muito e joga pouco; quem não tem, só joga",
         fonte="Br J Sports Med 2020")

# 3. a velocidade máxima, uma vez por semana
p = [svg_abre(1664, 450, "Esquema da velocidade máxima atingida pelo posterior da coxa em cada dia da semana: zero de segunda a quarta e de sexta a domingo; na quinta, às dez da noite, dez a quinze sprints máximos sem aquecimento. A pergunta: além da quinta, o que mais você faz? Nada")]
rs = []
p.append(f'<line x1="60" y1="380" x2="900" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="60" x2="900" y2="60" stroke="{FOSF}" stroke-width="3" stroke-dasharray="10 8"/>')
rs.append(rot(60, 22, "velocidade máxima", w=300, tam=22, cor=FOSF, peso=700))
for j, d in enumerate(DIAS):
    x = 80 + j * 118
    rs.append(rot(x, 392, d, w=100, tam=22, cor=MUDO, peso=700, alinha="center"))
    if d == "qui":
        p.append(f'<rect x="{x + 10}" y="64" width="80" height="316" rx="10" fill="{FOSF}"/>')
    else:
        p.append(f'<rect x="{x + 10}" y="372" width="80" height="8" rx="4" fill="{GRADE}"/>')
p.append(seta(560, 150, 470, 150, FOSF, "m0", 4))
rs.append(rot(580, 100, "dez a quinze sprints máximos, às dez da noite, sem aquecimento", w=320, tam=22, cor=TINTA, peso=700, lh=1.25))
rs.append(rot(580, 300, "esquema", w=320, tam=20, cor=MUDO))
p.insert(1, defs(FOSF))
p.append(caixa(980, 0, 684, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1010, 24, "“Além da quinta, o que mais você faz?”", w=624, tam=30, cor=AZUL, peso=700, serif=True, lh=1.25),
       rot(1010, 130, "Nada.", w=624, tam=48, cor=FOSF, peso=700, serif=True)]
for j, t in enumerate(["nenhuma sessão de força em doze anos", "nenhuma corrida", "nenhum sprint fora do jogo"]):
    p.append(icone("t:x", 1010, 216 + j * 52, 32, FOSF))
    rs.append(rot(1056, 216 + j * 52, t, w=580, tam=24, cor=TINTA, peso=600))
rs.append(rot(1010, 376, "não era reabilitação: era ausência de treino", w=624, tam=24, cor=AZUL, peso=700))
diagrama(S, "velocidade", 450, p, rs, eyebrow="A pergunta que ninguém tinha feito", titulo="O posterior da coxa só via velocidade máxima na quinta",
         fonte="J Sci Med Sport 2017")

# 4. o protocolo
p = [svg_abre(1664, 470, "Duas colunas. O que o protocolo pressupõe: fisioterapia supervisionada quase todo dia, microciclo ancorado no jogo, carga monitorada, alguém decide a volta. O que ele tinha: duas sessões por semana sozinho, nenhum microciclo, nenhuma medida, ele mesmo decide. Embaixo: o protocolo tratou a lesão e devolveu o jogador à condição que a produziu"), defs(MUDO, FOSF)]
rs = []
p.append(caixa(0, 0, 720, 330, AZUL, AZUL_T, esp=3, rx=18))
p.append(caixa(944, 0, 720, 330, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(24, 18, "O que o protocolo pressupõe", w=672, tam=28, cor=AZUL, peso=700, serif=True),
       rot(968, 18, "O que ele tinha", w=672, tam=28, cor=FOSF, peso=700, serif=True)]
pares = [("fisioterapia supervisionada quase todo dia", "duas sessões por semana, sozinho"),
         ("microciclo ancorado no jogo", "nenhum microciclo"),
         ("carga monitorada", "nenhuma medida"),
         ("alguém decide a volta", "ele mesmo decide")]
for j, (a, b) in enumerate(pares):
    y = 82 + j * 60
    rs += [rot(24, y, a, w=672, tam=24, cor=TINTA, peso=600), rot(968, y, b, w=672, tam=24, cor=TINTA, peso=600)]
    p.append(seta(740, y + 14, 924, y + 14, MUDO, "m0", 3))
p.append(f'<path d="M 160 400 A 40 40 0 1 1 240 400" stroke="{FOSF}" stroke-width="6" fill="none" marker-end="url(#m1)"/>')
rs.append(rot(290, 376, "O protocolo tratou a lesão e devolveu o jogador à condição que a produziu.", w=1374, tam=28, cor=TINTA, peso=700, serif=True))
diagrama(S, "protocolo", 470, p, rs, eyebrow="Por que o protocolo certo falhou", titulo="Certo para outra população, errado para esta vida")

# 5. quem decide
p = [svg_abre(1664, 470, "Em volta do clube: sono protegido, comida planejada, fisioterapia diária, carga monitorada e alguém decide por ele. Em volta da quinta: nove horas de trabalho, cerca de seis horas e meia de sono, dois filhos pequenos, come o que dá, e decide sozinho. Três consequências: não autorregula, não há descarga nem razão agudo-crônica, chega ao jogo com a carga de vida da semana")]
rs = []
for k, (tit, itens, dest, c, f) in enumerate([("Em volta do clube", ["sono protegido", "comida planejada", "fisioterapia diária", "carga monitorada"], "alguém decide por ele", AZUL, AZUL_T),
                                              ("Em volta da quinta", ["nove horas de trabalho", "seis horas e meia de sono", "dois filhos pequenos", "come o que dá"], "decide sozinho", FOSF, FOSF_T)]):
    x = k * 520
    p.append(caixa(x, 0, 490, 470, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 18, tit, w=442, tam=28, cor=c, peso=700, serif=True))
    for j, t in enumerate(itens):
        rs.append(rot(x + 24, 80 + j * 56, t, w=442, tam=24, cor=TINTA, peso=600))
    p.append(f'<rect x="{x + 20}" y="330" width="450" height="110" rx="14" fill="{c}"/>')
    rs.append(rot(x + 30, 364, dest, w=430, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
rs.append(rot(1064, 0, "Três consequências", w=600, tam=26, cor=TINTA, peso=700, serif=True))
for j, (ic, t) in enumerate([("t:friends", "não autorregula: a quinta é o único encontro com os amigos"),
                             ("t:chart-line", "sem descarga e sem razão agudo-crônica: não há denominador"),
                             ("t:zzz", "chega ao jogo com a carga de vida da semana")]):
    y = 56 + j * 140
    p.append(caixa(1064, y, 600, 124, GLIC, CARTAO, esp=2, rx=14))
    p.append(icone(ic, 1084, y + 38, 48, GLIC))
    rs.append(rot(1148, y + 18, t, w=496, tam=24, cor=TINTA, peso=600, lh=1.25))
diagrama(S, "decide", 470, p, rs, eyebrow="Quem decide, e o que pesa na decisão", titulo="No clube alguém decide por ele; na quinta, ele decide sozinho")

# 6. o perfil
p = [svg_abre(1664, 470, "Dois perfis. O profissional: vinte e poucos anos, avaliado com frequência, sem comorbidade, lesões documentadas e reabilitadas. O jogador de quinta: quarenta e poucos anos, tendão mais rígido, recuperação mais longa e menos potência, remédio que ninguém perguntou, lesões antigas nunca tratadas até o fim. Lesão prévia é o fator de risco mais consistente. No profissional europeu, o posterior de coxa chegou a um quarto das lesões")]
rs = []
p.append(caixa(0, 0, 640, 340, AZUL, AZUL_T, esp=3, rx=18))
p.append(menino(90, 300, 240, AZUL))
rs.append(rot(170, 20, "vinte e poucos anos", w=450, tam=28, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["avaliado com frequência", "sem comorbidade", "lesões documentadas e reabilitadas"]):
    rs.append(rot(170, 96 + j * 64, t, w=450, tam=24, cor=TINTA, peso=600))
p.append(caixa(680, 0, 984, 340, FOSF, FOSF_T, esp=3, rx=18))
p.append(menino(770, 300, 240, FOSF))
rs.append(rot(850, 20, "quarenta e poucos anos", w=790, tam=28, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["tendão mais rígido, que se remodela devagar", "recuperação mais longa, menos potência",
                       "um remédio para a pressão que ninguém perguntou", "três ou quatro lesões antigas nunca tratadas até o fim"]):
    rs.append(rot(850, 82 + j * 60, t, w=790, tam=24, cor=TINTA, peso=600))
rs.append(rot(0, 362, "Lesão prévia é o fator de risco mais consistente para uma nova.", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"))
p.append(f'<rect x="0" y="420" width="1100" height="40" rx="8" fill="{GRADE}"/>')
p.append(f'<rect x="0" y="420" width="{1100 * 0.24:.0f}" height="40" rx="8" fill="{FOSF}"/>')
rs.append(rot(10, 426, "24%", w=240, tam=22, cor=PAPEL, peso=700, alinha="center"))
rs.append(rot(1130, 418, "posterior de coxa nas lesões do profissional europeu", w=534, tam=22, cor=MUDO, peso=700, lh=1.2))
diagrama(S, "perfil", 470, p, rs, eyebrow="Outra população, também no corpo", titulo="Ele não é um profissional com menos tempo",
         fonte="Br J Sports Med 2023")

# 7. o que transfere
p = [svg_abre(1664, 450, "Não transfere: razão agudo-crônica e dispositivos, protocolo que pressupõe fisioterapia diária, microciclo ancorado no jogo, teste de rastreio de lesão. Transfere: força com progressão, programa neuromuscular, prazo biológico de cada tecido, exposição gradual ao gesto de risco. O inverso: preparo antes do jogo, que fora do clube é o treino que faltava")]
rs = []
for k, (tit, ic, itens, c, f) in enumerate([("Não transfere", "t:x", ["razão agudo-crônica e dispositivos", "protocolo que pressupõe fisioterapia diária", "microciclo ancorado no jogo", "teste de rastreio de lesão"], FOSF, FOSF_T),
                                            ("Transfere", "t:check", ["força com progressão de carga", "programa neuromuscular, se houver adesão", "prazo biológico de cada tecido", "exposição gradual ao gesto de risco"], OXID, OXID_T)]):
    x = k * 600
    p.append(caixa(x, 0, 570, 450, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 24, 22, 40, c))
    rs.append(rot(x + 76, 22, tit, w=470, tam=30, cor=c, peso=700, serif=True))
    for j, t in enumerate(itens):
        y = 100 + j * 86
        p.append(f'<line x1="{x + 24}" y1="{y - 14}" x2="{x + 546}" y2="{y - 14}" stroke="{GRADE}" stroke-width="2"/>')
        rs.append(rot(x + 24, y, t, w=522, tam=24, cor=TINTA, peso=600, lh=1.25))
p.append(caixa(1220, 40, 444, 370, GLIC, GLIC_T, esp=4, rx=18))
rs += [rot(1244, 66, "O inverso", w=396, tam=30, cor=GLIC, peso=700, serif=True),
       rot(1244, 130, "preparo antes do jogo", w=396, tam=30, cor=TINTA, peso=700, lh=1.2),
       rot(1244, 250, "fora do clube, prevenção é o treino que faltava", w=396, tam=24, cor=GLIC, peso=700, lh=1.3)]
diagrama(S, "transfere", 450, p, rs, eyebrow="O que se leva do clube", titulo="O conteúdo transfere; a estrutura em volta não")

# 8. a semana nova
p = [svg_abre(1664, 480, "A semana nova. Segunda e sábado: força, quarenta minutos, cadeia posterior e excêntrico. Quarta: velocidade em rampa. Quinta: aquecimento de doze minutos com a velocidade subindo, depois o jogo. Embaixo, a rampa da velocidade em dez semanas, de submáximo a perto do máximo, e a frase: a quinta não é o seu treino, é o seu jogo")]
rs = []
WD = 226
plano = {"seg": ("força", OXID), "qua": ("velocidade", AZUL), "qui": ("jogo", FOSF), "sáb": ("força", OXID)}
for j, d in enumerate(DIAS):
    x = j * (WD + 14)
    rs.append(rot(x, 0, d, w=WD, tam=22, cor=MUDO, peso=700, alinha="center"))
    if d in plano:
        t, c = plano[d]
        y0 = 40 if d != "qui" else 110
        p.append(f'<rect x="{x}" y="{y0}" width="{WD}" height="{220 - y0 + 40}" rx="14" fill="{c}"/>')
        rs.append(rot(x, y0 + 20, t, w=WD, tam=26, cor=PAPEL, peso=700, alinha="center"))
    else:
        p.append(f'<rect x="{x}" y="40" width="{WD}" height="220" rx="14" fill="none" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
for d in ("seg", "sáb"):
    x = DIAS.index(d) * (WD + 14)
    rs.append(rot(x + 12, 110, "40 min, cadeia posterior e excêntrico", w=WD - 24, tam=20, cor=PAPEL, peso=600, alinha="center", lh=1.25))
xq = 3 * (WD + 14)
p.append(f'<rect x="{xq}" y="40" width="{WD}" height="62" rx="14" fill="{GLIC}"/>')
rs.append(rot(xq, 46, "aquecimento, 12 min", w=WD, tam=20, cor=PAPEL, peso=700, alinha="center", lh=1.15))
xv = 2 * (WD + 14)
rs.append(rot(xv + 12, 110, "submáximo, subindo em rampa", w=WD - 24, tam=20, cor=PAPEL, peso=600, alinha="center", lh=1.25))
for k in range(10):
    h = 20 + k * 11
    p.append(f'<rect x="{k * 56}" y="{440 - h}" width="44" height="{h}" rx="6" fill="{AZUL}"/>')
rs += [rot(0, 290, "a rampa da velocidade, em cerca de dez semanas", w=560, tam=22, cor=AZUL, peso=700),
       rot(600, 400, "perto do máximo", w=220, tam=20, cor=MUDO, peso=600)]
p.append(caixa(880, 300, 784, 160, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(904, 322, "“A quinta não é o seu treino. É o seu jogo. E ninguém joga sem treinar.”", w=736, tam=28, cor=TINTA, peso=700, serif=True, lh=1.3))
diagrama(S, "semana", 480, p, rs, eyebrow="A semana nova", titulo="Força e velocidade em volta do jogo, e não no lugar dele")

# 9. o resto da linha
def m2(m):
    """Posição do mês m (0 a 24) na linha completa."""
    return 60 + 1540 * m / 24


p = [svg_abre(1664, 440, "Linha do tempo completa, do mês 0 ao 24, com meses ilustrativos. Duas lesões nos primeiros seis meses. A partir do mês 6: força duas vezes por semana, velocidade em rampa, aquecimento antes do jogo com dois amigos. Nenhuma nova lesão até o mês 24, jogando melhor. Um caso não prova o método; mostra a tradução")]
rs = []
p.append(f'<line x1="{m2(0)}" y1="380" x2="{m2(24)}" y2="380" stroke="{TINTA}" stroke-width="3"/>')
for m in (0, 6, 12, 18, 24):
    p.append(f'<line x1="{m2(m):.0f}" y1="372" x2="{m2(m):.0f}" y2="388" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(m2(m) - 50, 396, f"mês {m}", w=100, tam=20, cor=MUDO, alinha="center"))
for m in (0, 4.6):
    p.append(icone("t:bolt", m2(m) - 22, 316, 44, FOSF))
rs.append(rot(m2(0), 260, "duas lesões", w=260, tam=22, cor=FOSF, peso=700))
for j, (m, t, c, f) in enumerate([(6, "força duas vezes por semana", OXID, OXID_T), (7, "velocidade em rampa", AZUL, AZUL_T), (8, "aquecimento antes do jogo, com dois amigos", GLIC, GLIC_T)]):
    y = 110 + j * 66
    p.append(caixa(m2(m), y, m2(24) - m2(m), 54, c, f, esp=2, rx=12))
    rs.append(rot(m2(m) + 16, y + 12, t, w=900, tam=22, cor=c, peso=700))
p.append(f'<rect x="{m2(6):.0f}" y="320" width="{m2(24) - m2(6):.0f}" height="36" rx="8" fill="{OXID_T}"/>')
rs.append(rot(m2(6) + 16, 324, "nenhuma nova lesão", w=600, tam=22, cor=OXID, peso=700))
p.append(icone("t:star", m2(24) - 60, 20, 56, GLIC))
rs.append(rot(m2(24) - 420, 30, "jogando melhor", w=350, tam=26, cor=GLIC, peso=700, alinha="right", serif=True))
rs.append(rot(0, 20, "Um caso não prova o método; mostra a tradução.", w=900, tam=24, cor=MUDO, peso=700, serif=True))
diagrama(S, "desfecho", 440, p, rs, eyebrow="O resto da linha do tempo", titulo="O mesmo conhecimento do clube, redesenhado para uma vida sem clube")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que muda quando o esporte não paga as contas", "titulo": "Fora do clube, prevenção é o treino que faltava",
          "regras": ["Quem só joga passa toda a exposição na faixa de risco",
                     "O protocolo de clube pressupõe uma vida de clube: traduza antes de aplicar",
                     "Prevenção fora do clube não é acréscimo: é o treino que não existia"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Pergunta o que a pessoa faz além do jogo e como foi a semana."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Monta força e velocidade em volta do jogo, não no lugar dele."},
                    {"ic": "t:user", "t": "O praticante", "x": "Trata a quinta como jogo e faz o aquecimento de verdade."}]})

salvar("13-02.json", {"arquivo": "aulas/MOD13/13-02-o-que-muda-quando-o-esporte-nao-paga-as-contas.md",
                      "titulo": "O que muda quando o esporte não paga as contas", "subtitulo": "Um caso de futebol society, em dois anos",
                      "nota_capa": "Entra por um jogador de society na casa dos quarenta com duas lesões no mesmo músculo.",
                      "secoes": {"linha": ["O caso.", "capa"], "protocolo": ["Por que o protocolo falhou.", "protocolo"],
                                 "transfere": ["A tradução.", "transfere"]},
                      "slides": S})
