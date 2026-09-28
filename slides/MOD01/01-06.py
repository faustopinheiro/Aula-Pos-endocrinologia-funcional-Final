"""Spec do deck 1.6 (refeito no modelo dos desenhos). Gera 01-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

TRACO = ' stroke-dasharray="10 8"'

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
CINZA = "#C9CFD4"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"
def balao(x, y, w, h, cor, fundo, rabo="esq"):
    bx = x + 40 if rabo == "esq" else x + w - 70
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="{fundo}" stroke="{cor}" stroke-width="3"/>'
            f'<path d="M{bx} {y + h - 2} L{bx + 6} {y + h + 30} L{bx + 36} {y + h - 2}" fill="{fundo}" stroke="{cor}" stroke-width="3" stroke-linejoin="round"/>'
            f'<line x1="{bx + 2}" y1="{y + h - 1.5}" x2="{bx + 34}" y2="{y + h - 1.5}" stroke="{fundo}" stroke-width="5"/>')

# 1. quatro cenas de fronteira
p = [svg_abre(1664, 530, "Quatro balões de fala, cada um com a pergunta difícil de uma cena: o painel hormonal para a nutricionista, a creatina para o educador físico, o jogo de domingo para o fisioterapeuta, a planilha de treino montada pelo médico; no centro, a frase isso não é da minha área, riscada")]
cenas = [(0, 0, "h:health-worker", "A nutricionista", "“O que você acha desses resultados?”", "painel hormonal em cima da mesa", "t:clipboard-list"),
         (904, 0, "h:gym", "O educador físico", "“Professor, eu tomo creatina? E aquele pré-treino?”", "", "t:pill"),
         (0, 220, "h:crutches", "O fisioterapeuta", "“Ele pode jogar no domingo?”", "o técnico, no fim da reabilitação", "t:phone-call"),
         (904, 220, "h:doctor", "O médico", "monta a planilha de treino na consulta", "porque também corre há oito anos", "t:notebook")]
rs = []
for (x, y, ic, quem, fala, contexto, ic2) in cenas:
    p.append(icone(ic, x + 10, y + 10, 90, GLIC))
    rs.append(rot(x - 10, y + 106, quem, w=130, tam=20, cor=GLIC, peso=700, alinha="center", lh=1.1))
    p.append(balao(x + 130, y, 630, 150, GLIC, GLIC_T))
    p.append(icone(ic2, x + 154, y + 24, 48, GLIC))
    rs.append(rot(x + 216, y + 22, fala, w=530, tam=28, cor=TINTA, peso=600, serif=True, lh=1.2))
    if contexto:
        rs.append(rot(x + 216, y + 106, contexto, w=530, tam=20, cor=MUDO))
p.append(f'<rect x="582" y="430" width="500" height="90" rx="45" fill="{PAPEL}" stroke="{FOSF}" stroke-width="4"/>')
p.append(f'<line x1="600" y1="506" x2="1064" y2="444" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(582, 456, "“isso não é da minha área”", w=500, tam=28, cor=FOSF, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "cenas", "tipo": "diagrama", "h": 530, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Esta semana", "titulo": "Nas quatro cenas, “não é da minha área” é uma conduta ruim"})

# 2. a balança invasão × omissão
p = [svg_abre(1664, 580, "Uma balança torta: no prato mais leve, a invasão; no prato mais pesado, a omissão, com três exemplos de quem viu e não falou")]
ang = 8
p.append(f'<polygon points="832,220 790,340 874,340" fill="{TINTA}"/>')
p.append(f'<g transform="rotate({ang} 832 220)"><line x1="252" y1="220" x2="1412" y2="220" stroke="{TINTA}" stroke-width="10" stroke-linecap="round"/></g>')
yl = 220 - 580 * math.sin(math.radians(ang))
yr = 220 + 580 * math.sin(math.radians(ang))
p.append(f'<line x1="252" y1="130" x2="252" y2="{yl:.0f}" stroke="{TINTA}" stroke-width="3"/><line x1="1412" y1="{yr:.0f}" x2="1412" y2="{yr + 20:.0f}" stroke="{TINTA}" stroke-width="3"/>')
p.append(caixa(20, 0, 464, 130, GLIC, GLIC_T, esp=3, rx=16))
p.append(caixa(1044, yr + 20, 620, 220, FOSF, FOSF_T, esp=4, rx=16))
rs = [rot(40, 12, "Invasão", w=424, tam=32, cor=GLIC, peso=700, serif=True),
      rot(40, 58, "fazer o que não é seu; todo conselho fiscaliza, todo mundo tem medo", w=424, tam=22, cor=TINTA, lh=1.3),
      rot(1064, yr + 34, "Omissão", w=580, tam=32, cor=FOSF, peso=700, serif=True),
      rot(1064, yr + 80, "não fazer o que é seu; ninguém fiscaliza, e prejudica mais gente", w=580, tam=22, cor=TINTA, lh=1.3)]
exemplos = ["a menstruação ausente que ninguém comentou", "o suplemento estranho que ninguém perguntou", "a decisão devolvida ao técnico sem nada escrito"]
for k, t in enumerate(exemplos):
    x = 1064 + k * 200
    rs.append(rot(x, yr + 146, t, w=186, tam=18, cor=FOSF, peso=600, lh=1.2))
rs.append(rot(0, 420, "o medo mal calibrado paralisa também o que é seu: você para de perguntar, de anotar e de escrever", w=900, tam=24, cor=TINTA, peso=600, lh=1.3))
p.append("</svg>")
S.append({"id": "dois-erros", "tipo": "diagrama", "h": 580, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dois erros opostos", "titulo": "A omissão pesa mais que a invasão, e quase ninguém fala dela"})

# 3. as três camadas em Venn
p = [svg_abre(1664, 600, "Três círculos que se sobrepõem: o que a lei permite, o que eu sei fazer, o que este caso precisa agora; a interseção dos três em destaque")]
circ = [(640, 220, OXID, "O que a lei permite"), (900, 220, AZUL, "O que eu sei fazer"), (770, 400, GLIC, "O que este caso precisa agora")]
for (x, y, c, t) in circ:
    p.append(f'<circle cx="{x}" cy="{y}" r="190" fill="{c}" opacity="0.18" stroke="{c}" stroke-width="4"/>')
p.append(f'<circle cx="770" cy="290" r="40" fill="{FOSF}"/>')
p.append(icone("t:check", 750, 270, 40, PAPEL))
rs = [rot(470, 130, "O que a lei permite", w=220, tam=28, cor=OXID, peso=700, serif=True, lh=1.15),
      rot(870, 130, "O que eu sei fazer", w=200, tam=28, cor=AZUL, peso=700, serif=True, alinha="right", lh=1.15),
      rot(620, 490, "O que este caso precisa agora", w=300, tam=26, cor=GLIC, peso=700, serif=True, alinha="center", lh=1.15)]
notas = [(0, 30, "Lei", "a fonte é o conselho da sua profissão, na resolução em vigor; resolução muda", OXID),
         (1250, 30, "Preparo", "autorizado não é preparado; este curso aumenta esta camada, não a primeira", AZUL),
         (1250, 360, "Caso", "a resposta pode ser não em qualquer uma das três", GLIC)]
for (x, y, t, tx, c) in notas:
    p.append(caixa(x, y, 400 if x == 0 else 414, 180, c, CARTAO, esp=3, rx=16))
    rs.append(rot(x + 20, y + 16, t, w=360, tam=26, cor=c, peso=700, serif=True))
    rs.append(rot(x + 20, y + 60, tx, w=370, tam=21, cor=TINTA, lh=1.3))
p.append(caixa(0, 360, 400, 200, FOSF, FOSF_T, esp=3, rx=16))
rs += [rot(20, 376, "A pergunta vira", w=360, tam=26, cor=FOSF, peso=700, serif=True),
       rot(20, 420, "é meu, eu sei fazer, e é disso que essa pessoa precisa agora?", w=370, tam=22, cor=TINTA, peso=600, lh=1.3)]
p.append("</svg>")
S.append({"id": "tres-camadas", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Para decidir se é seu", "titulo": "Decidir se é seu passa por três camadas, não por uma"})

# 4. os três níveis em faixas
p = [svg_abre(1664, 520, "Três faixas horizontais: decisão, contribuição e reconhecimento, cada uma com o que o profissional faz; embaixo, uma quarta faixa pontilhada e riscada: não é comigo")]
niveis = [("Decisão", "você conhece a fundo e responde pela conduta, dentro do que a lei permite", "é a sua assinatura", "t:writing", OXID, OXID_T),
          ("Contribuição", "você entende o raciocínio e influencia a decisão do colega com argumento técnico", "você não assina, e sua opinião pesa", "t:messages", GLIC, GLIC_T),
          ("Reconhecimento", "você identifica o sinal que não é seu e encaminha bem feito, em tempo útil", "reconhecer exige saber o que procurar", "t:eye-check", FOSF, FOSF_T)]
rs = []
for k, (t, tx, marca, ic, c, ct) in enumerate(niveis):
    y = k * 136
    p.append(caixa(0, y, 1664, 120, c, ct, esp=3, rx=16))
    p.append(icone(ic, 30, y + 24, 72, c))
    rs.append(rot(130, y + 16, t, w=360, tam=36, cor=c, peso=700, serif=True))
    rs.append(rot(130, y + 68, marca, w=380, tam=20, cor=c, peso=600))
    rs.append(rot(540, y + 24, tx, w=1110, tam=26, cor=TINTA, lh=1.3))
p.append(f'<rect x="0" y="424" width="1664" height="96" rx="16" fill="none" stroke="{MUDO}" stroke-width="3"{TRACO}/>')
p.append(f'<line x1="20" y1="508" x2="1644" y2="436" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(0, 450, "“não é comigo”: essa posição não existe neste curso", w=1664, tam=30, cor=MUDO, peso=700, alinha="center", serif=True))
p.append("</svg>")
S.append({"id": "tres-niveis", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O modelo do curso", "titulo": "Três níveis de responsabilidade, e nenhum é “não é comigo”"})

# 5. a matriz do exemplo
p = [svg_abre(1664, 600, "Matriz com as profissões nas linhas e os três níveis nas colunas, para a falta de energia no atleta: nutrição e medicina em decisão, preparação física e fisioterapia em contribuição, psicologia entre decisão e contribuição, e todas em reconhecimento")]
cols = [("Decisão", OXID), ("Contribuição", GLIC), ("Reconhecimento", FOSF)]
linhas = [("Nutrição", 0, "cálculo, conduta alimentar, reconstrução da energia"), ("Medicina", 0, "menstruação ausente, osso, outras causas"),
          ("Preparação física", 1, "ajusta a carga; não trata como periodização"), ("Fisioterapia", 1, "a lesão repetida pode ser consequência"),
          ("Psicologia", 9, "decisão se há transtorno alimentar")]
x0, cw = 330, 250
rs = []
for j, (t, c) in enumerate(cols):
    rs.append(rot(x0 + j * cw, 0, t, w=cw, tam=24, cor=c, peso=700, alinha="center", serif=True))
for i, (prof, niv, nota) in enumerate(linhas):
    y = 60 + i * 86
    p.append(f'<rect x="0" y="{y}" width="1664" height="76" rx="10" fill="{CARTAO if i % 2 == 0 else PAPEL}"/>')
    rs.append(rot(20, y + 22, prof, w=300, tam=26, cor=TINTA, peso=700))
    rs.append(rot(x0 + 3 * cw + 30, y + 22, nota, w=1664 - (x0 + 3 * cw + 50), tam=22, cor=TINTA))
    for j, (t, c) in enumerate(cols):
        cx = x0 + j * cw + cw / 2
        cheio = (niv == j) or (niv == 9 and j in (0, 1)) or j == 2
        meia = niv == 9 and j in (0, 1)
        if cheio:
            p.append(f'<circle cx="{cx}" cy="{y + 38}" r="22" fill="{c}" opacity="{0.55 if meia else 1}"/>')
        else:
            p.append(f'<circle cx="{cx}" cy="{y + 38}" r="8" fill="{CINZA}"/>')
y = 60 + 5 * 86
p.append(f'<rect x="0" y="{y}" width="1664" height="76" rx="10" fill="{FOSF_T}"/>')
rs += [rot(20, y + 22, "Todas", w=300, tam=26, cor=FOSF, peso=700), rot(x0 + 3 * cw + 30, y + 22, "sempre", w=400, tam=24, cor=FOSF, peso=700)]
p.append(f'<rect x="{x0 + 2 * cw + 30}" y="{y + 18}" width="{cw - 60}" height="40" rx="20" fill="{FOSF}"/>')
p.append("</svg>")
S.append({"id": "exemplo", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um exemplo", "titulo": "Na falta de energia, cada profissão ocupa um nível diferente"})

# 6. quem enxerga primeiro
p = [svg_abre(1664, 460, "Linha do tempo: na primeira semana, o profissional em reconhecimento vê o sinal; quatro meses depois, o profissional em decisão vê a pessoa; uma seta liga os dois: quem vê primeiro decide se o outro vai ver"), defs(FOSF, OXID)]
p.append(f'<line x1="40" y1="240" x2="1620" y2="240" stroke="{MUDO}" stroke-width="4"/>')
for k, t in enumerate(["semana 1", "mês 1", "mês 2", "mês 3", "mês 4"]):
    x = 120 + k * 360
    p.append(f'<line x1="{x}" y1="228" x2="{x}" y2="252" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<circle cx="120" cy="240" r="22" fill="{FOSF}"/><circle cx="1560" cy="240" r="22" fill="{OXID}"/>')
p.append(icone("t:eye-check", 80, 136, 80, FOSF))
p.append(icone("t:writing", 1520, 130, 80, OXID))
p.append(f'<path d="M140 272 C 500 410, 1180 410, 1540 272" fill="none" stroke="{FOSF}" stroke-width="5"{TRACO} marker-end="url(#m0)"/>')
rs = [rot(0, 50, "quem está em reconhecimento", w=500, tam=22, cor=FOSF, peso=700),
      rot(1164, 50, "quem está em decisão", w=500, tam=22, cor=OXID, peso=700, alinha="right"),
      rot(0, 86, "vê primeiro", w=500, tam=20, cor=MUDO),
      rot(1164, 86, "vê a pessoa daqui a quatro meses", w=500, tam=20, cor=MUDO, alinha="right"),
      rot(432, 400, "o encaminhamento bem feito, ou o silêncio", w=800, tam=24, cor=FOSF, peso=700, alinha="center")]
for k, t in enumerate(["semana 1", "mês 1", "mês 2", "mês 3", "mês 4"]):
    if 0 < k < 4:
        rs.append(rot(120 + k * 360 - 60, 256, t, w=120, tam=18, cor=MUDO, alinha="center"))
p.append("</svg>")
S.append({"id": "quem-enxerga", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os níveis não são ranking", "titulo": "Quem decide não é quem enxerga primeiro",
          "destaque": "E quem enxerga primeiro decide se o outro vai enxergar.", "destaque_cor": "verm"})

# 7. as quatro omissões em miniatura
p = [svg_abre(1664, 470, "Quatro desenhos: uma pergunta riscada, não perguntar; um envelope vazio com favor avaliar; duas linhas paralelas que nunca se encontram, encaminhar e sumir; quatro pessoas em roda apontando uma para a outra, achar que alguém está cuidando"), defs(FOSF)]
rs = []
tit = [("Não perguntar", "“sono é do médico”: perguntar é de todo mundo"), ("Encaminhar sem informação", "transfere o paciente, não o conhecimento"),
       ("Encaminhar e sumir", "duas condutas paralelas que nunca conversam"), ("Achar que alguém está cuidando", "todos veem, cada um acha que o outro resolve")]
for k, (t, tx) in enumerate(tit):
    x = k * 420
    p.append(caixa(x, 0, 396, 470, FOSF, FOSF_T, esp=3, rx=18))
    rs.append(rot(x + 20, 300, t, w=356, tam=28, cor=FOSF, peso=700, serif=True, lh=1.15))
    rs.append(rot(x + 20, 385, tx, w=356, tam=22, cor=TINTA, lh=1.3))
# 1: pergunta riscada
p.append(icone("t:message-circle", 108, 60, 180, FOSF))
rs.append(rot(128, 118, "?", w=140, tam=64, cor=FOSF, peso=700, alinha="center", serif=True))
p.append(f'<line x1="90" y1="270" x2="310" y2="50" stroke="{FOSF}" stroke-width="8"/>')
# 2: envelope vazio
x = 420
p.append(f'<rect x="{x + 70}" y="90" width="256" height="170" rx="10" fill="{CARTAO}" stroke="{FOSF}" stroke-width="4"/>')
p.append(f'<path d="M{x + 70} 90 L{x + 198} 190 L{x + 326} 90" fill="none" stroke="{FOSF}" stroke-width="4"/>')
rs.append(rot(x + 70, 210, "“favor avaliar”", w=256, tam=24, cor=FOSF, peso=700, alinha="center", serif=True))
# 3: paralelas
x = 840
p.append(seta(x + 50, 130, x + 340, 130, FOSF, "m0", esp=6))
p.append(seta(x + 50, 220, x + 340, 220, FOSF, "m0", esp=6))
rs += [rot(x + 40, 84, "conduta 1", w=200, tam=20, cor=MUDO), rot(x + 40, 234, "conduta 2", w=200, tam=20, cor=MUDO)]
# 4: roda apontando
x = 1260
cx, cy = x + 198, 170
for k in range(4):
    a = math.radians(k * 90 - 45)
    px, py = cx + 90 * math.cos(a), cy + 90 * math.sin(a)
    p.append(icone("h:person", px - 30, py - 30, 60, FOSF))
    a2 = math.radians((k + 1) * 90 - 45)
    qx, qy = cx + 90 * math.cos(a2), cy + 90 * math.sin(a2)
    mx, my = (px + qx) / 2, (py + qy) / 2
    p.append(seta(px + (qx - px) * 0.3, py + (qy - py) * 0.3, px + (qx - px) * 0.6, py + (qy - py) * 0.6, FOSF, "m0", esp=3))
p.append("</svg>")
S.append({"id": "omissoes", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A omissão por dentro", "titulo": "A omissão tem quatro formas, e todas têm a mesma raiz",
          "destaque": "Quem está em reconhecimento não fica em silêncio. Fica por escrito."})

# 8. o caso em linha do tempo
p = [svg_abre(1664, 560, "Linha do tempo do caso: o antidepressivo em uso estável, o treino começando; a conversa com o personal; o remédio caindo até zero em seis semanas; três semanas de insônia, irritação e volta dos pensamentos ruins; quatro meses de recuperação, com o treino interrompido")]
X = lambda s: 60 + s * 26   # semanas
p.append(f'<line x1="40" y1="470" x2="1640" y2="470" stroke="{MUDO}" stroke-width="3"/>')
# faixa do remédio
p.append(f'<path d="M{X(0)} 150 L{X(22)} 150 L{X(28)} 330 L{X(36)} 330 L{X(40)} 150 L{X(60)} 150" fill="none" stroke="{AZUL}" stroke-width="8" stroke-linejoin="round"/>')
# faixa do treino
p.append(f'<path d="M{X(0)} 300 L{X(36)} 300" fill="none" stroke="{OXID}" stroke-width="8"/>')
p.append(f'<path d="M{X(36)} 300 L{X(56)} 300" fill="none" stroke="{OXID}" stroke-width="8"{TRACO} opacity="0.5"/>')
p.append(f'<rect x="{X(30)}" y="40" width="{X(33) - X(30)}" height="420" fill="{FOSF}" opacity="0.18"/>')
p.append(f'<rect x="{X(36)}" y="40" width="{X(56) - X(36)}" height="420" fill="{OXID}" opacity="0.08"/>')
p.append(icone("t:messages", X(20) - 26, 360, 52, GLIC))
rs = [rot(X(0), 110, "antidepressivo, psiquiatra e psicoterapia", w=520, tam=22, cor=AZUL, peso=700),
      rot(X(0), 262, "musculação com personal, três vezes por semana", w=700, tam=22, cor=OXID, peso=700),
      rot(X(12), 420, "“o exercício é o melhor antidepressivo; vai diminuindo”", w=560, tam=22, cor=GLIC, peso=700, alinha="center"),
      rot(X(8), 180, "diminui por conta própria: zero em seis semanas", w=X(22) - X(8) - 10, tam=20, cor=AZUL, peso=600, lh=1.2, alinha="right"),
      rot(X(30) - 20, 50, "insônia, irritação, pensamentos ruins", w=180, tam=20, cor=FOSF, peso=700, lh=1.2),
      rot(X(38), 60, "quatro meses de recuperação, com o remédio reintroduzido pelo psiquiatra", w=480, tam=22, cor=TINTA, peso=600, lh=1.25),
      rot(X(40), 320, "e parou de treinar", w=400, tam=24, cor=OXID, peso=700, serif=True),
      rot(40, 482, "semanas", w=1600, tam=20, cor=MUDO, alinha="center")]
p.append("</svg>")
S.append({"id": "caso", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um caso desconfortável", "titulo": "Uma opinião bem-intencionada tirou o remédio e depois o treino",
          "fonte": "Esquema, sem valores medidos"})

# 9. o bilhete que nunca foi escrito
p = [svg_abre(1664, 560, "À esquerda, o personal que vê o paciente três vezes por semana; à direita, o psiquiatra; no meio, um bilhete de cinco linhas que o paciente levaria; embaixo, riscado, o caminho que aconteceu: a opinião direto ao paciente"), defs(OXID, FOSF)]
p.append(icone("h:gym", 20, 120, 150, OXID))
p.append(icone("h:doctor", 1490, 120, 150, AZUL))
rs = [rot(0, 280, "o personal: vê três vezes por semana", w=200, tam=20, cor=OXID, peso=700, alinha="center", lh=1.2),
      rot(1464, 280, "o psiquiatra: conduz o tratamento", w=200, tam=20, cor=AZUL, peso=700, alinha="center", lh=1.2)]
p.append(f'<g transform="rotate(-1.5 832 200)"><rect x="330" y="0" width="1004" height="380" rx="8" fill="{CARTAO}" stroke="{OXID}" stroke-width="3"/><rect x="330" y="0" width="12" height="380" fill="{OXID}"/></g>')
p.append(seta(190, 200, 318, 200, OXID, "m0", esp=5))
p.append(seta(1346, 200, 1474, 200, OXID, "m0", esp=5))
bil = ["Ao psiquiatra do paciente.", "Ele treina comigo três vezes por semana há seis meses, quase sem faltas.",
       "Relata mais disposição e sono melhor nas últimas semanas.", "Me contou que usa antidepressivo e pensa em reduzir por conta própria.",
       "Achei importante você saber. O que devo observar daqui para frente?"]
rs.append(rot(370, 20, "o bilhete que nunca foi escrito", w=920, tam=20, cor=OXID, peso=700))
for k, t in enumerate(bil):
    rs.append(rot(370, 64 + k * 60, t, w=940, tam=26, cor=TINTA, serif=True, lh=1.2))
p.append(f'<path d="M190 470 L 1100 470" fill="none" stroke="{FOSF}" stroke-width="4"{TRACO}/>')
p.append(f'<line x1="600" y1="500" x2="720" y2="440" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(190, 490, "o que aconteceu: a opinião direto ao paciente, sem passar por quem conduz", w=1000, tam=22, cor=FOSF, peso=600))
p.append("</svg>")
S.append({"id": "bilhete", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que teria sido excelente", "titulo": "A informação estava certa, e o caminho, errado",
          "destaque": "O erro não foi de conhecimento, foi de lugar. A invasão quase nunca tem cara de invasão."})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "Três verbos e um limite",
          "regras": ["Ler não é prescrever.", "Reconhecer não é diagnosticar.", "Encaminhar não é opinar sobre a conduta do colega.",
                     "Limite duro: ninguém mexe em tratamento conduzido por outro profissional."],
          "quem": "Discordância no time: se há risco para o paciente, fale com o colega, com clareza e sem plateia. Se é diferença de escola ou de estilo, segure.",
          "proxima": "O encaminhamento que o colega usa"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-06.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-06.json"), "w"), ensure_ascii=False, indent=1)
print("01-06.json:", len(S), "slides")
