"""Spec do deck 10.7. Gera 10-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"

# 1. o funil do retorno
p = [svg_abre(1664, 500, "Funil a partir de cem operados do cruzado: 81 voltam a algum esporte, 65 ao nível de antes, 55 ao competitivo; ao lado, um enxerto firme")]
niveis = [(100, "operados", "#C9CFD4"), (81, "algum esporte", AZUL_T), (65, "nível de antes", AZUL), (55, "competitivo", FOSF)]
rs = []
esc = 9
for i, (v, t, c) in enumerate(niveis):
    y = 20 + i * 118
    w = v * esc
    x = 500 - w / 2
    p.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="96" rx="12" fill="{c}"/>')
    rs.append(rot(x + 16, y + 20, f"{v}", w=160, tam=44, cor=PAPEL if i >= 2 else TINTA, peso=700, serif=True))
    rs.append(rot(960, y + 30, t, w=300, tam=28, cor=TINTA, peso=600))
p.append(f'<line x1="950" y1="20" x2="950" y2="480" stroke="{GRADE}" stroke-width="2"/>')
p.append(icone("t:shield-check", 1330, 60, 260, OXID))
p.append("</svg>")
rs.append(rot(1280, 350, "o joelho não é o gargalo", w=380, tam=32, cor=OXID, peso=700, alinha="center", serif=True))
S.append({"id": "funil", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um armador de handebol, dez meses depois", "titulo": "O enxerto aguenta; quase metade não volta a competir",
          "fonte": "Metanálise de 2014, retorno depois da reconstrução do cruzado · porcentagens arredondadas"})

# 2. preditores precoces
p = [svg_abre(1664, 500, "Linha do tempo: antes da cirurgia, quatro meses, doze meses; quatro sinais medidos cedo levam ao retorno ou não ao nível de antes"), defs(TINTA)]
p.append(f'<rect x="60" y="60" width="760" height="360" rx="18" fill="{AZUL_T}"/>')
p.append(f'<line x1="60" y1="440" x2="1600" y2="440" stroke="{TINTA}" stroke-width="5"/>')
for x in [160, 720, 1500]:
    p.append(f'<circle cx="{x}" cy="440" r="16" fill="{TINTA}"/>')
sinais = [("t:gauge", "prontidão para o retorno"), ("t:alert-triangle", "medo de nova lesão"), ("t:target", "sensação de que depende de si"), ("t:calendar", "estimativa de meses até voltar")]
rs = []
for i, (ic, t) in enumerate(sinais):
    y = 80 + i * 84
    p.append(icone(ic, 100, y, 56, AZUL))
    rs.append(rot(180, y + 10, t, w=600, tam=28, cor=TINTA, peso=600))
p.append(f'<path d="M830 240 C 1050 240, 1200 240, 1380 240" fill="none" stroke="{TINTA}" stroke-width="5" marker-end="url(#m0)"/>')
p.append(caixa(1390, 150, 270, 180, OXID, OXID_T))
p.append("</svg>")
rs += [rot(60, 460, "antes da cirurgia", w=200, tam=24, cor=TINTA, alinha="center"),
       rot(620, 460, "4 meses", w=200, tam=24, cor=TINTA, alinha="center"),
       rot(1400, 460, "12 meses", w=200, tam=24, cor=TINTA, alinha="center"),
       rot(1400, 180, "voltou ao nível de antes?", w=250, tam=28, cor=OXID, peso=700, alinha="center", lh=1.25),
       rot(860, 180, "cada um contribui de forma independente", w=500, tam=24, cor=MUDO)]
S.append({"id": "preditores", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Medível antes", "titulo": "A prontidão se mede cedo, e prevê o retorno",
          "fonte": "Estudo australiano, Am J Sports Med 2013 · medida no quarto mês, ainda há tempo de tratar"})

# 3. a escala do cruzado
p = [svg_abre(1664, 520, "Mostrador de 0 a 100 com três faixas de uso; barra com a composição da escala: 5 itens de emoção, 5 de confiança, 2 de avaliação de risco; curva de reaplicação")]
cx, cy, r = 360, 330, 300
faixas = [(0, 40, FOSF_T, "alvo de tratamento"), (40, 70, GLIC_T, "retorno gradual acompanhado"), (70, 100, OXID_T, "critério cumprido")]
for a, b, c, t in faixas:
    a0, a1 = math.pi * (1 - a / 100), math.pi * (1 - b / 100)
    p.append(f'<path d="M{cx} {cy} L{cx + r*math.cos(a0):.0f} {cy - r*math.sin(a0):.0f} A{r} {r} 0 0 1 {cx + r*math.cos(a1):.0f} {cy - r*math.sin(a1):.0f} Z" fill="{c}" stroke="{PAPEL}" stroke-width="4"/>')
aa = math.pi * (1 - 52 / 100)
p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 250*math.cos(aa):.0f}" y2="{cy - 250*math.sin(aa):.0f}" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="{TINTA}"/>')
comp = [(5, "emoções", FOSF), (5, "confiança", AZUL), (2, "risco", GLIC)]
x = 780
rs = []
for n, t, c in comp:
    w = n * 70
    p.append(f'<rect x="{x}" y="60" width="{w}" height="80" fill="{c}"/>')
    rs.append(rot(x, 76, f"{n} · {t}", w=w, tam=26 if n > 2 else 22, cor=PAPEL, peso=700, alinha="center"))
    x += w
pts = [(0, 34), (1, 38), (2, 45), (3, 52), (4, 60), (5, 67), (6, 72)]
p.append(f'<line x1="800" y1="480" x2="1640" y2="480" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<polyline points="{" ".join(f"{820 + k*130},{480 - v*3.4:.0f}" for k, v in pts)}" fill="none" stroke="{OXID}" stroke-width="6"/>')
for k, v in pts:
    p.append(f'<circle cx="{820 + k*130}" cy="{480 - v*3.4:.0f}" r="10" fill="{OXID}"/>')
p.append("</svg>")
rs += [rot(20, 350, "0", w=60, tam=24, cor=MUDO), rot(640, 350, "100", w=80, tam=24, cor=MUDO),
       rot(40, 390, "faixas de uso, não pontos de corte", w=640, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(10, 170, "alvo de tratamento", w=200, tam=22, cor=FOSF, peso=700, lh=1.2),
       rot(250, 0, "retorno gradual acompanhado", w=240, tam=22, cor=GLIC, peso=700, alinha="center", lh=1.2),
       rot(540, 170, "critério cumprido", w=180, tam=22, cor=OXID, peso=700, alinha="right", lh=1.2),
       rot(780, 12, "12 itens, escore de 0 a 100 · versão curta de 6 itens", w=860, tam=26, cor=TINTA, peso=600),
       rot(780, 170, "Reaplique: a curva vale mais que o número", w=860, tam=28, cor=OXID, peso=700, serif=True)]
S.append({"id": "escala", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A escala do cruzado", "titulo": "Doze perguntas, três domínios, nenhum número mágico",
          "fonte": "Escala de 2008, versão curta de 2018, ambas com versão brasileira · curva ilustrativa, sem valores medidos"})

# 4. fora do joelho
p = [svg_abre(1664, 480, "Três cartões para qualquer lesão: prontidão geral com seis itens; medo do movimento com dezessete itens; três perguntas em voz alta, com a terceira destacada")]
cards = [("t:gauge", "Prontidão geral", "6 itens de confiança · baixa depois da lesão, sobe antes do treino e antes da competição", AZUL, AZUL_T, 2009),
         ("t:run", "Medo do movimento", "17 itens, de 17 a 68 · dor musculoesquelética, inclusive lombar · versão brasileira", GLIC, GLIC_T, 1990)]
rs = []
for i, (ic, t, x_, c, ct, ano) in enumerate(cards):
    x = i * 420
    p.append(caixa(x, 0, 396, 480, c, ct, esp=3, rx=20))
    p.append(icone(ic, x + 30, 30, 80, c))
    rs.append(rot(x + 130, 40, t, w=250, tam=30, cor=c, peso=700, serif=True, lh=1.15))
    rs.append(rot(x + 30, 140, str(ano), w=200, tam=44, cor=c, peso=700, serif=True))
    rs.append(rot(x + 30, 220, x_, w=340, tam=24, cor=TINTA, lh=1.4))
p.append(caixa(840, 0, 824, 480, OXID, CARTAO, esp=4, rx=20))
p.append(icone("t:message-circle", 870, 30, 70, OXID))
perg = ["“De zero a dez, quanta confiança você tem de que aguenta um jogo inteiro?”",
        "“O que aconteceria se entrasse numa disputa de bola hoje?”",
        "“Tem algum movimento que você evita sem precisar?”"]
for j, t in enumerate(perg):
    y = 130 + j * 110
    if j == 2:
        p.append(f'<rect x="860" y="{y - 14}" width="784" height="100" rx="14" fill="{OXID_T}"/>')
    rs.append(rot(880, y, t, w=750, tam=28 if j == 2 else 26, cor=OXID if j == 2 else TINTA, peso=700 if j == 2 else 400, lh=1.3))
rs.append(rot(960, 44, "Três perguntas em voz alta", w=660, tam=30, cor=OXID, peso=700, serif=True))
rs.append(rot(880, 440, "a evitação é visível para quem pergunta e invisível para quem a pratica", w=760, tam=22, cor=MUDO))
p.append("</svg>")
S.append({"id": "fora", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quando não é joelho", "titulo": "Fora do joelho, três perguntas já abrem o caso"})

# 5. a matriz
p = [svg_abre(1664, 560, "Matriz dois por dois: capacidade física no eixo horizontal, prontidão psicológica no vertical; quatro quadrantes nomeados; o armador no quadrante de capacidade alta e prontidão baixa")]
X0, Y0, W, H = 160, 20, 1180, 460
quad = [(0, 0, "Capacidade baixa, prontidão alta", "o mais perigoso: sem freio interno", FOSF, FOSF_T),
        (1, 0, "Capacidade alta, prontidão alta", "libere", OXID, OXID_T),
        (0, 1, "Capacidade baixa, prontidão baixa", "trate os dois: melhoram juntos", AZUL, AZUL_T),
        (1, 1, "Capacidade alta, prontidão baixa", "o mais mal manejado", GLIC, GLIC_T)]
rs = []
for cx_, cy_, t, x_, c, ct in quad:
    x, y = X0 + cx_ * W / 2, Y0 + cy_ * H / 2
    p.append(f'<rect x="{x + 6:.0f}" y="{y + 6:.0f}" width="{W/2 - 12:.0f}" height="{H/2 - 12:.0f}" rx="16" fill="{ct}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x + 30, y + 30, t, w=W / 2 - 60, tam=28, cor=c, peso=700, serif=True))
    rs.append(rot(x + 30, y + 80, x_, w=W / 2 - 60, tam=26, cor=TINTA, peso=600))
p.append(icone("h:running", X0 + W * 0.78, Y0 + H * 0.66, 90, GLIC))
p.append(f'<line x1="{X0}" y1="{Y0 + H + 20}" x2="{X0 + W}" y2="{Y0 + H + 20}" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="{X0 - 20}" y1="{Y0}" x2="{X0 - 20}" y2="{Y0 + H}" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs += [rot(X0, Y0 + H + 34, "capacidade física →", w=W, tam=24, cor=MUDO, alinha="center"),
       rot(0, Y0 + H / 2 - 40, "prontidão psicológica ↑", w=120, tam=24, cor=MUDO, alinha="center", lh=1.2),
       rot(1380, 60, "Os dois quadrantes desalinhados são os que mais aparecem, e os que uma avaliação só física não distingue.", w=284, tam=26, cor=TINTA, peso=600, lh=1.35),
       rot(1380, 330, "o armador", w=284, tam=28, cor=GLIC, peso=700, serif=True)]
S.append({"id": "matriz", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dois números, uma decisão", "titulo": "Corpo e confiança nem sempre estão no mesmo lugar"})

# 6. condutas opostas
p = [svg_abre(1664, 520, "Duas colunas de conduta: capacidade alta e prontidão baixa (nomear, expor em degraus, registrar) e capacidade baixa e prontidão alta (números mostrados, retorno negociado, freio de fora)")]
cols = [("Capacidade alta, prontidão baixa", GLIC, GLIC_T, [("t:message-circle", "nomear: “o joelho passou; a confiança ainda não, e tem tratamento”"),
                                                          ("t:stairs", "exposição em degraus"), ("t:notebook", "registro do que deu certo")]),
        ("Capacidade baixa, prontidão alta", FOSF, FOSF_T, [("t:chart-bar", "os números dos testes, em voz alta e por escrito"),
                                                          ("t:adjustments-horizontal", "retorno negociado: tempo, posição, saída ao primeiro sinal"),
                                                          ("t:barbell", "força seguindo durante a temporada")])]
rs = []
for i, (t, c, ct, itens) in enumerate(cols):
    x = i * 844
    p.append(caixa(x, 0, 820, 520, c, ct, esp=4, rx=22))
    rs.append(rot(x + 30, 24, t, w=760, tam=32, cor=c, peso=700, serif=True))
    for j, (ic, it) in enumerate(itens):
        y = 110 + j * 130
        p.append(f'<rect x="{x + 24}" y="{y}" width="772" height="110" rx="14" fill="{CARTAO}"/>')
        p.append(icone(ic, x + 44, y + 23, 64, c))
        rs.append(rot(x + 130, y + 22, it, w=650, tam=26, cor=TINTA, peso=600, lh=1.3))
p.append("</svg>")
rs.append(rot(874, 488, "no atleta mais velho: calibração desatualizada, não teimosia", w=760, tam=22, cor=FOSF, peso=700))
S.append({"id": "condutas", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os dois quadrantes desalinhados", "titulo": "Quando não há freio interno, o freio vem de fora"})

# 7. a escada da previsibilidade
p = [svg_abre(1664, 540, "Escada de cinco degraus de exposição, com a previsibilidade diminuindo a cada degrau; lacuna vermelha entre o terceiro degrau e o jogo")]
degs = [("sozinho, devagar", "salto de arremesso sem bola"), ("velocidade normal", "em velocidade de jogo"),
        ("com carga ou salto", "com bola, salto máximo"), ("com outra pessoa, combinado", "bloqueio combinado"),
        ("imprevisível", "bloqueio real, em fadiga")]
rs = []
for i, (t, hb) in enumerate(degs):
    x, h = i * 300, 130 + i * 75
    c = AZUL if i < 3 else OXID
    p.append(f'<rect x="{x}" y="{500 - h}" width="290" height="{h}" rx="10" fill="{AZUL_T if i < 3 else OXID_T}" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(x + 14, 500 - h + 14, f"{i+1} · {t}", w=262, tam=26, cor=c, peso=700, lh=1.2))
    rs.append(rot(x + 14, 500 - h + (80 if len(t) > 16 else 50), hb, w=262, tam=22, cor=TINTA, lh=1.25))
p.append(f'<path d="M880 215 Q 900 40 1190 30" fill="none" stroke="{FOSF}" stroke-width="5" stroke-dasharray="14 10"/>')
p.append(f'<polygon points="0,510 1500,510 1500,530 0,538" fill="{GRADE}"/>')
p.append("</svg>")
rs += [rot(1210, 0, "o salto que quase todo programa dá: do 3 para o jogo", w=454, tam=24, cor=FOSF, peso=700),
       rot(0, 0, "previsibilidade diminui a cada degrau →", w=700, tam=26, cor=MUDO, peso=600)]
S.append({"id": "escada", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A exposição em degraus", "titulo": "O que se progride é a previsibilidade, não o peso",
          "fonte": "Os degraus 4 e 5 são conduzidos em campo pela preparação física e pelo treinador, com a fisioterapia por perto"})

# 8. o caderno
p = [svg_abre(1664, 500, "Caderno aberto: à esquerda, a lista do que doeu, riscada; à direita, a lista do que ele conseguiu fazer, com vistos; ao lado, a memória do medo guardando um episódio ruim e esquecendo onze bons")]
p.append(f'<rect x="0" y="0" width="1000" height="500" rx="16" fill="{CARTAO}" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<line x1="500" y1="20" x2="500" y2="480" stroke="{TINTA}" stroke-width="3"/>')
rs = [rot(30, 24, "o que doeu", w=440, tam=28, cor=MUDO, peso=700, serif=True),
      rot(530, 24, "o que eu consegui", w=440, tam=28, cor=OXID, peso=700, serif=True)]
doeu = ["pontada no aquecimento", "rigidez de manhã", "desconforto no salto"]
fiz = ["arremesso em suspensão, 20 vezes", "bloqueio combinado, 3 séries", "jogo reduzido, 10 minutos"]
for j, (d, f) in enumerate(zip(doeu, fiz)):
    y = 110 + j * 110
    rs.append(rot(30, y, d, w=440, tam=26, cor=MUDO))
    p.append(f'<line x1="30" y1="{y + 18}" x2="{30 + len(d) * 14}" y2="{y + 18}" stroke="{MUDO}" stroke-width="3"/>')
    p.append(icone("t:check", 530, y - 4, 44, OXID))
    rs.append(rot(590, y, f, w=390, tam=26, cor=TINTA, peso=600))
for k in range(12):
    x = 1080 + (k % 6) * 94
    y = 120 if k < 6 else 230
    c = FOSF if k == 4 else "#D9DDE0"
    p.append(f'<rect x="{x}" y="{y}" width="76" height="76" rx="12" fill="{c}"/>')
p.append("</svg>")
rs += [rot(1080, 20, "A memória do medo", w=560, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1080, 330, "guarda o único episódio ruim e esquece as onze sessões em que nada aconteceu", w=560, tam=24, cor=TINTA, lh=1.35)]
S.append({"id": "caderno", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O registro e o encaminhamento", "titulo": "O caderno do que deu certo corrige a memória do medo",
          "destaque": "“Não tem nada, pode ir” não trata medo. Encaminhamento é parte do plano esportivo, não consolo.", "destaque_cor": "verm"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Prontidão psicológica para o retorno", "titulo": "Os testes diziam pronto; ele não arremessava",
          "regras": ["Medir a prontidão cedo, e reaplicar",
                     "Cruzar corpo e confiança na matriz",
                     "Subir os degraus da previsibilidade até o jogo"],
          "cards": [{"ic": "t:users", "t": "Quem reabilita e prepara", "x": "Mede, conduz os degraus e não salta do terceiro para o jogo."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Junta as duas dimensões na decisão de retorno."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Trata o medo que não cede à exposição."}]})

spec = {"arquivo": "aulas/MOD10/10-07-prontidao-psicologica-para-o-retorno.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Prontidão psicológica para o retorno", "subtitulo": "Medir, cruzar com o corpo, tratar o medo",
        "nota_capa": "Entra por um armador de handebol que passou em todos os testes.",
        "secoes": {"funil": ["O tamanho do problema.", "capa"], "escala": ["Como medir.", "escala"],
                   "matriz": ["Corpo e confiança.", "matriz"], "escada": ["Como tratar o medo.", "escada"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-07.json"), "w"), ensure_ascii=False, indent=1)
print("10-07.json:", len(S), "slides")
