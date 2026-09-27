"""Spec do deck 10.11. Gera 10-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

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

# 1. a curva de janeiro
meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
p = [svg_abre(1664, 480, "Esquema: a frequência de uma academia ao longo do ano, alta em janeiro e descendo mês a mês; em cima, a frase ele não tem motivação, riscada")]
x0, dx, y0 = 80, 120, 400
pts = [(x0 + i * dx, y0 - 300 * math.exp(-i / 3.2) - 40) for i in range(12)]
p.append(f'<path d="M{pts[0][0]} {y0} ' + " ".join(f"L{x:.0f} {y:.0f}" for x, y in pts) + f' L{pts[-1][0]} {y0} Z" fill="{AZUL_T}"/>')
p.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in pts)}" fill="none" stroke="{AZUL}" stroke-width="7"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x0 + 11*dx}" y2="{y0}" stroke="{MUDO}" stroke-width="3"/>')
p.append(icone("t:barbell", 1460, 40, 140, CINZA))
p.append(f'<line x1="760" y1="130" x2="1400" y2="70" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
p.append("</svg>")
rs = [rot(x0 + i * dx - 40, y0 + 12, m, w=80, tam=22, cor=MUDO, alinha="center") for i, m in enumerate(meses)]
rs += [rot(760, 70, "“esse aí não tem motivação”", w=640, tam=34, cor=TINTA, peso=700, alinha="center", serif=True),
       rot(760, 170, "permanência: o desfecho que sustenta todos os outros", w=700, tam=28, cor=AZUL, peso=700, alinha="center")]
S.append({"id": "janeiro", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um aluno novo, em janeiro", "titulo": "Ninguém não tem motivação",
          "fonte": "Esquema, sem valores medidos · as pessoas têm motivações, e muitas vezes elas não combinam com o que foi prescrito"})

# 2. o banquinho
p = [svg_abre(1664, 520, "Banquinho de três pernas com a palavra comportamento no assento: capacidade, oportunidade e motivação; uma perna mais curta faz o banquinho tombar")]
p.append(f'<g transform="rotate(8 420 260)">')
p.append(f'<rect x="170" y="80" width="500" height="70" rx="30" fill="{TINTA}"/>')
p.append(f'<rect x="210" y="150" width="40" height="300" rx="10" fill="{AZUL}"/>')
p.append(f'<rect x="400" y="150" width="40" height="190" rx="10" fill="{GLIC}"/>')
p.append(f'<rect x="590" y="150" width="40" height="300" rx="10" fill="{OXID}"/>')
p.append("</g>")
p.append(f'<line x1="80" y1="480" x2="780" y2="480" stroke="{MUDO}" stroke-width="3"/>')
pernas = [("t:tools", "Capacidade", "sabe e consegue fazer? fica perdido na academia cheia?", AZUL, AZUL_T),
          ("t:calendar", "Oportunidade", "a planilha pede quatro dias; a agenda tem dois, com filho e turnos", GLIC, GLIC_T),
          ("t:target", "Motivação", "quer, mas quer o quê? e quanto?", OXID, OXID_T)]
rs = [rot(200, 98, "comportamento", w=440, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True)]
for i, (ic, t, x_, c, ct) in enumerate(pernas):
    y = 10 + i * 170
    p.append(caixa(900, y, 764, 150, c, ct, esp=3))
    p.append(icone(ic, 920, y + 40, 70, c))
    rs.append(rot(1010, y + 20, t, w=640, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(1010, y + 70, x_, w=640, tam=24, cor=TINTA, lh=1.3))
p.append("</svg>")
S.append({"id": "banquinho", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeiro passo: descobrir o que falta", "titulo": "Se uma perna falta, não adianta alongar as outras",
          "fonte": "Modelo de 2011, a partir de 19 modelos de mudança de comportamento · “falta de motivação” costuma ser uma perna de oportunidade"})

# 3. o cabo de guerra
p = [svg_abre(1664, 480, "Cabo de guerra: de um lado o profissional puxando para mudança, do outro o aluno puxando para não mudar; embaixo, 48 ensaios e razão de chances de 1,55")]
p.append(f'<line x1="200" y1="200" x2="1464" y2="200" stroke="#9C8E74" stroke-width="14" stroke-linecap="round"/>')
p.append(f'<line x1="832" y1="150" x2="832" y2="250" stroke="{FOSF}" stroke-width="6"/>')
p.append(icone("h:doctor", 60, 110, 180, AZUL))
p.append(icone("h:person", 1424, 110, 180, GLIC))
p.append(f'<path d="M420 140 L320 140" stroke="{AZUL}" stroke-width="6" marker-end="url(#m0)"/>')
p.append(f'<path d="M1244 140 L1344 140" stroke="{GLIC}" stroke-width="6" marker-end="url(#m1)"/>')
p.insert(1, defs(AZUL, GLIC))
p.append(caixa(420, 330, 824, 130, OXID, OXID_T, esp=3))
p.append("</svg>")
rs = [rot(0, 20, "“você precisa…” “o ideal é…” “já expliquei…”", w=520, tam=24, cor=AZUL, peso=600, alinha="center", lh=1.3),
      rot(1144, 20, "“mas eu não tenho tempo…” “já tentei…”", w=520, tam=24, cor=GLIC, peso=600, alinha="center", lh=1.3),
      rot(560, 250, "quanto mais você puxa, mais ele puxa de volta", w=544, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.25),
      rot(440, 346, "1,55", w=200, tam=56, cor=OXID, peso=700, alinha="center", serif=True),
      rot(650, 350, "razão de chances · 48 ensaios · 9.618 participantes · vantagem significativa e modesta", w=580, tam=24, cor=TINTA, lh=1.35)]
S.append({"id": "cabo", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Segundo passo: parar de argumentar", "titulo": "Quem argumenta mais perde o cabo de guerra",
          "fonte": "Entrevista motivacional em contextos de cuidado em saúde, metanálise de 2013 · a ambivalência não é resistência"})

# 4. a régua do por que não três
p = [svg_abre(1664, 520, "Régua de 0 a 10 com o marcador no 6; a pergunta por que não 10 riscada; a pergunta por que não 3 gera as razões do próprio aluno; ao lado, quatro ferramentas"), defs(OXID, FOSF)]
X0, W = 60, 1000
p.append(f'<rect x="{X0}" y="200" width="{W}" height="60" rx="12" fill="#E6E3DA"/>')
for k in range(11):
    x = X0 + k * W / 10
    p.append(f'<line x1="{x:.0f}" y1="200" x2="{x:.0f}" y2="{230 if k % 5 else 260}" stroke="{MUDO}" stroke-width="3"/>')
xm = X0 + 6 * W / 10
p.append(f'<polygon points="{xm-24},170 {xm+24},170 {xm},205" fill="{TINTA}"/>')
p.append(f'<path d="M{xm} 150 Q {X0 + 8.5*W/10} 80 {X0 + W - 10} 150" fill="none" stroke="{FOSF}" stroke-width="5" stroke-dasharray="12 8" marker-end="url(#m1)"/>')
p.append(f'<path d="M{xm} 280 Q {X0 + 4.5*W/10} 360 {X0 + 3*W/10 + 10} 280" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m0)"/>')
rs = [rot(X0 + k * W / 10 - 20, 268 if k % 5 else 272, str(k), w=40, tam=22, cor=MUDO, alinha="center") for k in (0, 3, 6, 10)]
rs += [rot(X0 + 6.5 * W / 10, 40, "“por que não 10?” → motivos para não mudar", w=460, tam=24, cor=FOSF, peso=600),
       rot(X0 + 2 * W / 10, 380, "“por que 6, e não 3?”", w=520, tam=30, cor=OXID, peso=700, serif=True),
       rot(X0, 430, "“quero correr com meu filho sem ficar sem ar” · “meu pai teve infarto com a minha idade”", w=W, tam=24, cor=TINTA, lh=1.35)]
ferr = [("t:question-mark", "perguntas abertas"), ("t:thumb-up", "reconhecimento"), ("t:refresh", "reflexão"), ("t:list-check", "resumo")]
for j, (ic, t) in enumerate(ferr):
    y = 20 + j * 120
    p.append(f'<rect x="1160" y="{y}" width="504" height="100" rx="14" fill="{AZUL_T}"/>')
    p.append(icone(ic, 1180, y + 20, 60, AZUL))
    rs.append(rot(1260, y + 32, t, w=390, tam=28, cor=TINTA, peso=700))
p.append("</svg>")
S.append({"id": "regua", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceiro passo: as razões são dela", "titulo": "Pergunte por que não é três",
          "fonte": "Argumento próprio convence; argumento alheio, não · anote as frases dele: vão servir no dia em que ele quiser parar"})

# 5. o plano se-então
p = [svg_abre(1664, 500, "Dois cartões: vou treinar mais, riscado; e o plano se-então ancorado na escola do filho; embaixo, 94 testes e d = 0,65")]
p.append(caixa(0, 20, 560, 200, CINZA, "#EEEBE3", esp=3))
p.append(f'<line x1="30" y1="200" x2="530" y2="40" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
p.append(caixa(640, 0, 1024, 260, OXID, OXID_T, esp=5))
p.append(icone("t:school", 670, 30, 70, OXID))
p.append(icone("t:barbell", 670, 150, 70, OXID))
p.append(f'<rect x="0" y="300" width="1664" height="190" rx="16" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(30, 90, "“vou treinar mais”", w=500, tam=36, cor=MUDO, peso=700, alinha="center", serif=True),
      rot(760, 36, "SE deixar meu filho na escola, na terça e na quinta,", w=880, tam=30, cor=TINTA, peso=700, lh=1.25),
      rot(760, 156, "ENTÃO vou direto para a academia e faço o treino A", w=880, tam=30, cor=OXID, peso=700, lh=1.25),
      rot(40, 320, "0,65", w=260, tam=72, cor=OXID, peso=700, serif=True),
      rot(300, 330, "efeito de tamanho médio a grande · 94 testes, mais de 8.000 participantes · ajuda a começar, protege das distrações, facilita trocar o que não funciona", w=1330, tam=24, cor=TINTA, lh=1.35),
      rot(300, 420, "“Qual a menor coisa que você tem certeza de que consegue manter? Logo depois de quê?”", w=1330, tam=26, cor=OXID, peso=700, serif=True)]
S.append({"id": "plano", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarto passo: o plano é dela", "titulo": "Um plano se-então vale mais que uma intenção",
          "fonte": "Metanálise de 2006 de planos se-então · a planilha de quatro dias virou dois treinos ancorados e um curto em casa"})

# 6. a curva do hábito
p = [svg_abre(1664, 500, "Curva de automaticidade de um hábito ao longo dos dias, subindo e se achatando; mediana de 66 dias; faixa de 18 a 254 dias; uma falta quase não mexe na linha")]
x0, x1, y0 = 80, 1200, 400
sx = (x1 - x0) / 260
curva = []
for d in range(0, 261, 2):
    v = 1 - math.exp(-d / 28)
    if 40 <= d <= 44:
        v -= 0.03
    curva.append((x0 + d * sx, y0 - 320 * v))
p.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in curva)}" fill="none" stroke="{OXID}" stroke-width="7"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="60" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<rect x="{x0 + 18*sx:.0f}" y="440" width="{(254-18)*sx:.0f}" height="26" rx="13" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
p.append(f'<line x1="{x0 + 66*sx:.0f}" y1="60" x2="{x0 + 66*sx:.0f}" y2="470" stroke="{TINTA}" stroke-width="4" stroke-dasharray="10 8"/>')
p.append(f'<circle cx="{x0 + 42*sx:.0f}" cy="{y0 - 320*(1-math.exp(-42/28)) + 10:.0f}" r="14" fill="{FOSF}"/>')
p.append("</svg>")
rs = [rot(x0 + 66 * sx + 12, 150, "66 dias: mediana", w=300, tam=28, cor=TINTA, peso=700),
      rot(x0 + 66 * sx + 12, 190, "de cerca de metade dos participantes", w=300, tam=22, cor=MUDO, lh=1.3),
      rot(x0 + 20, 170, "uma falta", w=200, tam=24, cor=FOSF, peso=700),
      rot(x0 + 254 * sx - 280, 400, "de 18 a 254 dias", w=280, tam=24, cor=GLIC, peso=700, alinha="right"),
      rot(x0 + 10, 60, "automaticidade", w=300, tam=22, cor=MUDO),
      rot(1240, 120, "“Vai ter semana em que você não vem. Está previsto. O que conta é voltar na seguinte.”", w=424, tam=28, cor=OXID, peso=700, serif=True, lh=1.3),
      rot(1240, 360, "96 pessoas, 84 dias, um comportamento de saúde por dia", w=424, tam=22, cor=MUDO, lh=1.3)]
S.append({"id": "habito", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quanto tempo leva", "titulo": "O hábito leva semanas a meses, e uma falta não o derruba",
          "fonte": "Estudo de 2010 sobre formação de hábito · os dois primeiros meses são para instalar o hábito, não para a adaptação máxima"})

# 7. as palavras
p = [svg_abre(1664, 500, "Duas colunas de palavras: à esquerda o vocabulário de dívida, riscado; à direita o vocabulário de capacidade")]
divida = ["compensar", "queimar o que comeu", "merecer a sobremesa", "pagar pelo fim de semana", "recomeçar do zero"]
capac = ["construir", "conseguir", "voltar", "o que você já faz", "o que você vai usar"]
p.append(f'<rect x="0" y="70" width="780" height="420" rx="18" fill="{FOSF_T}"/>')
p.append(f'<rect x="884" y="70" width="780" height="420" rx="18" fill="{OXID_T}"/>')
rs = [rot(0, 0, "Dívida e punição", w=780, tam=34, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(884, 0, "Capacidade", w=780, tam=34, cor=OXID, peso=700, alinha="center", serif=True)]
for j, (a, b) in enumerate(zip(divida, capac)):
    y = 100 + j * 76
    rs.append(rot(40, y, a, w=700, tam=32, cor=TINTA, peso=600, alinha="center"))
    p.append(f'<line x1="{390 - len(a)*8.5:.0f}" y1="{y + 22}" x2="{390 + len(a)*8.5:.0f}" y2="{y + 22}" stroke="{FOSF}" stroke-width="4"/>')
    rs.append(rot(924, y, b, w=700, tam=32, cor=OXID, peso=700, alinha="center"))
p.append(seta(800, 280, 864, 280, TINTA, "m0", esp=6))
p.insert(1, defs(TINTA))
p.append("</svg>")
S.append({"id": "palavras", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A linguagem", "titulo": "Ninguém sustenta penitência por vinte anos",
          "destaque": "Na recaída: “você não perdeu tudo; voltar agora é mais fácil do que foi começar”.", "destaque_cor": "tinta"})

# 8. os cinco passos
p = [svg_abre(1664, 500, "A consulta de adesão em cinco estações: descobrir o que falta, parar de argumentar, ouvir as razões dela, o plano se-então, prever a falta e marcar o retorno; um relógio de dez minutos"), defs(TINTA)]
passos = [("t:zoom-question", "descobrir o que falta", "capacidade, oportunidade ou motivação", AZUL, AZUL_T),
          ("t:hand-stop", "parar de argumentar", "ambivalência é normal", GLIC, GLIC_T),
          ("t:ear", "ouvir as razões dela", "“por que não 3?”", OXID, OXID_T),
          ("t:checklist", "o plano se-então", "pequeno, ancorado, escolhido por ela", AZUL, AZUL_T),
          ("t:calendar", "prever a falta e marcar o retorno", "uma mensagem na terceira semana", FOSF, FOSF_T)]
rs = []
for i, (ic, t, x_, c, ct) in enumerate(passos):
    x = i * 334
    p.append(f'<circle cx="{x + 150}" cy="120" r="90" fill="{ct}" stroke="{c}" stroke-width="5"/>')
    p.append(icone(ic, x + 105, 75, 90, c))
    if i < 4:
        p.append(seta(x + 250, 120, x + 380, 120, TINTA, "m0", esp=4))
    rs.append(rot(x, 230, f"{i+1} · {t}", w=300, tam=26, cor=c, peso=700, alinha="center", lh=1.2))
    rs.append(rot(x + 10, 310, x_, w=280, tam=22, cor=TINTA, alinha="center", lh=1.3))
p.append(icone("t:clock", 760, 400, 70, MUDO))
p.append("</svg>")
rs.append(rot(850, 418, "cerca de dez minutos, em qualquer profissão", w=600, tam=26, cor=MUDO, peso=700))
S.append({"id": "passos", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O procedimento inteiro", "titulo": "A conversa de adesão em cinco passos",
          "fonte": "Respeita a autonomia: se a pessoa decide não mudar agora, a conversa terminou bem, e a porta fica aberta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "Da motivação à conversa que a sustenta",
          "regras": ["Decisão: psicologia e psiquiatria tratam; o médico investiga, rastreia e libera; reabilitação, preparação e nutrição no seu campo",
                     "Contribuição: o alívio quando o treino cai, a mudança de comportamento, o que acontece em casa",
                     "Reconhecimento: o silêncio depois do treino, a frase dita como piada, a atleta que evita alguém, o ex-atleta que sumiu"],
          "cards": [{"ic": "h:psychology", "t": "Psicologia e psiquiatria", "x": "Diagnóstico, psicoterapia, psicofármaco, plano de segurança."},
                    {"ic": "h:doctor", "t": "Médico e equipe de saúde", "x": "Causas clínicas, rastreio, emergência, retorno, Conselho Tutelar."},
                    {"ic": "t:users", "t": "Todos", "x": "Próximo módulo: a atleta mulher, do déficit de evidência ao ciclo e à energia."}]})

spec = {"arquivo": "aulas/MOD10/10-11-comunicacao-adesao-e-mudanca-de-comportamento.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Comunicação, adesão e mudança de comportamento", "subtitulo": "A conversa que faz a pessoa voltar",
        "nota_capa": "Entra por um aluno de academia em janeiro. Fecha o módulo.",
        "secoes": {"janeiro": ["O que falta.", "capa"], "cabo": ["A conversa.", "cabo"],
                   "plano": ["O plano e o hábito.", "plano"], "passos": ["Os cinco passos e o fecho do módulo.", "passos"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-11.json"), "w"), ensure_ascii=False, indent=1)
print("10-11.json:", len(S), "slides")
