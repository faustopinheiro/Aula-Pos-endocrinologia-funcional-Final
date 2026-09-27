"""Spec do deck 10.5. Gera 10-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL = "#FDFCF9", "#F7F6F2"
LARANJA = "#C2571A"
def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'
def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'
def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"

# 1. três círculos
p = [svg_abre(1664, 540, "Três círculos concêntricos: de todos, da sua profissão e o que não é seu; uma seta sai do círculo de dentro para fora com a palavra encaminhar"), defs(OXID)]
cx, cy = 700, 280
p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="690" ry="255" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
p.append(f'<ellipse cx="{cx}" cy="{cy+35}" rx="450" ry="175" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(f'<ellipse cx="{cx}" cy="{cy+70}" rx="240" ry="100" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>')
p.append(icone("t:lock", cx - 30, cy + 15, 60, FOSF))
p.append(icone("t:briefcase", cx - 390, cy + 20, 60, AZUL))
p.append(icone("t:users", cx - 640, cy - 30, 70, OXID))
p.append(f'<path d="M{cx+230} {cy+50} C {cx+450} {cy+10}, {cx+620} {cy-40}, {cx+760} {cy-60}" fill="none" stroke="{OXID}" stroke-width="6" marker-end="url(#m0)"/>')
p.append("</svg>")
rs = [rot(cx - 520, 56, "De todos: reconhecer · perguntar · acolher · encaminhar · acompanhar", w=1040, tam=26, cor=OXID, peso=700, alinha="center"),
      rot(cx - 250, 160, "Da sua profissão", w=500, tam=28, cor=AZUL, peso=700, alinha="center"),
      rot(cx - 220, cy + 90, "Não é seu: diagnosticar · prescrever · psicoterapia · internação", w=440, tam=24, cor=FOSF, peso=700, alinha="center", lh=1.3),
      rot(1420, cy - 150, "encaminhar é ato clínico", w=244, tam=30, cor=OXID, peso=700, serif=True, lh=1.2)]
S.append({"id": "circulos", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mapa antes do procedimento", "titulo": "Ninguém precisa saber conduzir para saber reconhecer",
          "fonte": "“Às vezes eu penso que seria mais fácil não acordar”: a frase dita no alongamento"})

# 2. sinais
p = [svg_abre(1664, 560, "Painel de sinais de alerta com a tentativa prévia maior; embaixo, uma faixa de terreno com o contexto que aumenta a vulnerabilidade")]
sinais = [("t:message-circle", "falas sobre morte, mesmo como piada"), ("t:cloud-rain", "desesperança"),
          ("t:note", "despedidas e pendências resolvidas"), ("t:user", "isolamento crescente"),
          ("t:glass-full", "mais álcool ou outras substâncias"), ("t:alert-triangle", "comportamento de risco novo")]
rs = []
for i, (ic, t) in enumerate(sinais):
    x, y = (i % 3) * 360, (i // 3) * 170
    p.append(caixa(x, y, 340, 150, GLIC, GLIC_T, esp=3))
    p.append(icone(ic, x + 20, y + 20, 56, GLIC))
    rs.append(rot(x + 20, y + 84, t, w=300, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(caixa(1100, 0, 564, 320, FOSF, FOSF_T, esp=6))
p.append(icone("h:warning", 1130, 30, 110, FOSF))
p.append(f'<path d="M0 420 Q 200 380 420 410 T 840 400 T 1260 410 T 1664 395 V560 H0 Z" fill="#E6E0D2"/>')
p.append("</svg>")
rs += [rot(1260, 50, "tentativa prévia", w=380, tam=40, cor=FOSF, peso=700, serif=True),
       rot(1130, 170, "o fator de risco mais importante na população geral", w=500, tam=28, cor=TINTA, peso=600, lh=1.3),
       rot(0, 360, "O terreno", w=400, tam=26, cor=MUDO, peso=700),
       rot(40, 460, "perda recente · lesão grave com afastamento longo · fim de carreira · humilhação pública · dívida · acesso a meios", w=1584, tam=26, cor=TINTA, peso=600, alinha="center")]
S.append({"id": "sinais", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo zero: reconhecer", "titulo": "A tentativa prévia é o sinal que mais pesa",
          "fonte": "Organização Mundial da Saúde · nenhum sinal é diagnóstico; todos são motivo para perguntar"})

# 3. a pergunta
p = [svg_abre(1664, 460, "Dois balões: o silêncio com um cadeado e a pergunta direta em letra grande; entre eles, treze estudos e nenhum aumento de ideação")]
p.append(f'<path d="M0 40 H420 a20 20 0 0 1 20 20 V300 a20 20 0 0 1 -20 20 H160 L110 380 L110 320 H20 a20 20 0 0 1 -20 -20 Z" fill="#E6E3DA"/>')
p.append(icone("t:lock", 150, 110, 140, "#9AA0A6"))
p.append(f'<path d="M720 20 H1644 a20 20 0 0 1 20 20 V320 a20 20 0 0 1 -20 20 H1500 L1540 410 L1420 340 H740 a20 20 0 0 1 -20 -20 V40 a20 20 0 0 1 20 -20 Z" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>')
p.append("</svg>")
rs = [rot(0, 400, "o silêncio: é ele que produz dano", w=440, tam=26, cor=MUDO, peso=600, alinha="center"),
      rot(470, 110, "13", w=220, tam=96, cor=OXID, peso=700, alinha="center", serif=True),
      rot(470, 240, "estudos, nenhum com aumento de ideação depois da pergunta", w=220, tam=22, cor=TINTA, alinha="center", lh=1.25),
      rot(780, 80, "“Você tem tido pensamentos de tirar a própria vida?”", w=820, tam=52, cor=TINTA, peso=700, serif=True, lh=1.2),
      rot(780, 262, "sem eufemismo · com calma · olhando para a pessoa", w=820, tam=26, cor=OXID, peso=700)]
S.append({"id": "pergunta", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A pergunta que destrava", "titulo": "Perguntar não planta a ideia",
          "fonte": "Revisão de 13 estudos, adultos e adolescentes, comunidade e grupos de risco · Psychol Med 2014"})

# 4. o roteiro
p = [svg_abre(1664, 520, "Caminho de quatro passos: fique, pergunte mais, acione conforme a gravidade, envolva alguém"), defs(TINTA)]
passos = [("h:person", "Fique", "não deixe a pessoa sozinha; atrase o próximo treino se precisar", AZUL, AZUL_T),
          ("t:message-circle", "Pergunte mais", "como faria? tem acesso? hoje, nos próximos dias? já tentou?", GLIC, GLIC_T),
          ("t:phone-call", "Acione", "conforme a gravidade: o próximo slide", FOSF, FOSF_T),
          ("t:friends", "Envolva alguém", "“quem você prefere que eu chame?”", OXID, OXID_T)]
rs = []
for i, (ic, t, x_, c, ct) in enumerate(passos):
    x = i * 424
    p.append(f'<circle cx="{x+100}" cy="90" r="80" fill="{ct}" stroke="{c}" stroke-width="5"/>')
    p.append(icone(ic, x + 55, 45, 90, c))
    if i < 3:
        p.append(seta(x + 190, 90, x + 410, 90, TINTA, "m0", esp=4))
    p.append(caixa(x, 200, 396, 300, c, CARTAO, esp=3))
    rs.append(rot(x + 24, 220, f"{i+1} · {t}", w=350, tam=34, cor=c, peso=700, serif=True))
    rs.append(rot(x + 24, 290, x_, w=350, tam=26, cor=TINTA, lh=1.35))
p.append("</svg>")
S.append({"id": "roteiro", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quando a resposta é sim", "titulo": "Quatro passos, na mesma ordem, sem improviso",
          "destaque": "Não fazer: prometer sigilo antes de ouvir, minimizar, discutir razões para viver, deixar ir sozinha sem plano.", "destaque_cor": "verm"})

# 5. três degraus
p = [svg_abre(1664, 560, "Rampa de três degraus: ideação sem plano, risco presente sem iminência e risco iminente; por baixo, uma faixa contínua com o 188")]
deg = [("Ideação sem plano", "encaminhar · contato próximo · não deixar solto", GLIC, GLIC_T, 300),
       ("Risco presente, sem iminência", "prioridade no mesmo dia ou nos próximos · rede de apoio · menos acesso a meios · retorno marcado", LARANJA, "#F6E0D2", 170),
       ("Risco iminente: plano, meio, intenção", "emergência · ninguém sozinho · SAMU 192 · alguém de confiança", FOSF, FOSF_T, 40)]
rs = []
for i, (t, x_, c, ct, y) in enumerate(deg):
    x = i * 555
    p.append(f'<rect x="{x}" y="{y}" width="540" height="{440-y}" rx="10" fill="{ct}" stroke="{c}" stroke-width="4"/>')
    rs.append(rot(x + 24, y + 20, t, w=500, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(x + 24, y + 70, x_, w=490, tam=24, cor=TINTA, lh=1.35))
p.append(f'<rect x="0" y="460" width="1664" height="90" rx="12" fill="{OXID}"/>')
p.append(icone("t:phone-call", 30, 475, 60, PAPEL))
p.append("</svg>")
rs.append(rot(110, 484, "Em qualquer degrau: 188, Centro de Valorização da Vida · 24 horas · sem custo · sigilo", w=1520, tam=30, cor=PAPEL, peso=700))
S.append({"id": "degraus", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo três: acionar", "titulo": "A gravidade decide quem você aciona",
          "fonte": "Rede pública: atenção básica, centros de atenção psicossocial e urgência e emergência são portas de entrada"})

# 6. o cano
p = [svg_abre(1664, 540, "Um cano da indicação até a primeira consulta, com cinco vazamentos e um remendo em cada um")]
p.append(f'<rect x="120" y="190" width="1420" height="70" rx="35" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="5"/>')
p.append(icone("t:note", 10, 170, 100, AZUL))
p.append(icone("h:psychology", 1554, 170, 100, OXID))
vaz = [("“procure um psicólogo”", "nome, não categoria"), ("“vou ver”", "ajudar a marcar ali"),
       ("“não sei como é”", "explicar o que acontece"), ("“vou ter que parar de treinar?”", "antecipar a objeção"),
       ("ninguém perguntou de novo", "marcar um retorno seu")]
rs = []
for i, (q, r) in enumerate(vaz):
    x = 250 + i * 290
    p.append(f'<path d="M{x} 262 q -14 30 0 44 q 14 -14 0 -44 Z" fill="{AZUL}"/>')
    p.append(icone("t:droplet", x - 16, 320, 32, AZUL))
    p.append(f'<rect x="{x-60}" y="180" width="120" height="90" rx="10" fill="{OXID}" opacity="0.18"/>')
    rs.append(rot(x - 135, 60 + (i % 2) * 50, q, w=270, tam=24, cor=MUDO, alinha="center", lh=1.2))
    rs.append(rot(x - 135, 380, r, w=270, tam=26, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append("</svg>")
rs += [rot(0, 280, "indicação", w=140, tam=24, cor=AZUL, peso=700, alinha="center"),
       rot(1524, 280, "primeira consulta", w=140, tam=24, cor=OXID, peso=700, alinha="center"),
       rot(0, 480, "E o encaminhamento escrito com as cinco linhas do módulo de fundamentos.", w=1664, tam=26, cor=TINTA, peso=600, alinha="center")]
S.append({"id": "cano", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O encaminhamento de rotina", "titulo": "O encaminhamento se perde no caminho",
          "fonte": "Estudos de encaminhamento da atenção primária para saúde mental: comparecimento muito variável"})

# 7. seguimento
p = [svg_abre(1664, 540, "Barras de comportamento suicida em seis meses: 5,29% no cuidado habitual e 3,03% com plano de segurança e telefonemas; linha do tempo dos telefonemas; seis passos do plano")]
base, esc = 470, 60
for i, (v, c) in enumerate([(5.29, "#B9BEC3"), (3.03, OXID)]):
    x = 60 + i * 260
    p.append(f'<rect x="{x}" y="{base - v*esc:.0f}" width="200" height="{v*esc:.0f}" rx="8" fill="{c}"/>')
p.append(f'<line x1="20" y1="{base}" x2="560" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<line x1="680" y1="60" x2="1060" y2="60" stroke="{TINTA}" stroke-width="4"/>')
for k, x in enumerate([680, 760, 880, 980, 1060]):
    p.append(f'<circle cx="{x}" cy="60" r="{14 if k else 18}" fill="{TINTA if k == 0 else OXID}"/>')
p.append(caixa(1120, 0, 544, 520, OXID, OXID_T, esp=3))
rs = [rot(60, base - 5.29 * esc - 56, "5,29%", w=200, tam=40, cor=MUDO, peso=700, alinha="center", serif=True),
      rot(320, base - 3.03 * esc - 56, "3,03%", w=200, tam=40, cor=OXID, peso=700, alinha="center", serif=True),
      rot(40, base + 12, "cuidado habitual", w=240, tam=24, cor=TINTA, peso=600, alinha="center"),
      rot(300, base + 12, "plano + telefonemas", w=240, tam=24, cor=OXID, peso=700, alinha="center"),
      rot(630, 0, "alta", w=100, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(700, 90, "até 72 h", w=120, tam=24, cor=OXID, peso=700, alinha="center"),
      rot(840, 90, "depois, semanal", w=260, tam=24, cor=OXID, alinha="center"),
      rot(650, 200, "≈ 45% menos", w=440, tam=56, cor=OXID, peso=700, serif=True),
      rot(650, 290, "comportamento suicida em seis meses, 1.640 pacientes", w=440, tam=24, cor=TINTA, lh=1.3),
      rot(1150, 24, "O plano de segurança", w=500, tam=30, cor=OXID, peso=700, serif=True)]
for j, t in enumerate(["sinais de alerta da própria pessoa", "o que ela faz sozinha", "pessoas e lugares que distraem",
                       "a quem pedir ajuda", "profissionais e serviços, um a qualquer hora", "ambiente mais seguro, menos acesso a meios"]):
    rs.append(rot(1150, 90 + j * 70, f"{j+1}. {t}", w=490, tam=24, cor=TINTA, lh=1.25))
p.append("</svg>")
S.append({"id": "seguimento", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que o retorno marcado faz", "titulo": "O telefonema depois faz parte do cuidado",
          "fonte": "Serviços de emergência de hospitais de veteranos, EUA · JAMA Psychiatry 2018 · quem monta o plano é o profissional de saúde mental"})

# 8. o cartão
p = [svg_abre(1664, 540, "Um cartão em quatro blocos: emergência, a sua rede, a rede pública e as perguntas; ao lado, uma porta entreaberta com um calendário para a recusa")]
p.append(f'<rect x="0" y="0" width="1100" height="540" rx="28" fill="{CARTAO}" stroke="{TINTA}" stroke-width="5"/>')
p.append(f'<line x1="550" y1="30" x2="550" y2="510" stroke="{GRADE}" stroke-width="3"/>')
p.append(f'<line x1="30" y1="270" x2="1070" y2="270" stroke="{GRADE}" stroke-width="3"/>')
blocos = [("t:phone-call", "Emergência", "192 · 188 · pronto-socorro de referência", FOSF),
          ("t:users", "A sua rede", "psicologia com quem já conversou · psiquiatria · transtorno alimentar", AZUL),
          ("t:building-hospital", "Rede pública", "unidade básica de referência · centro de atenção psicossocial", OXID),
          ("t:message-circle", "As perguntas", "ainda gosta de treinar? · tem se irritado mais? · o que mudou? · e a direta", GLIC)]
rs = []
for i, (ic, t, x_, c) in enumerate(blocos):
    x, y = 40 + (i % 2) * 550, 30 + (i // 2) * 270
    p.append(icone(ic, x, y + 10, 64, c))
    rs.append(rot(x + 80, y + 18, t, w=400, tam=32, cor=c, peso=700, serif=True))
    rs.append(rot(x, y + 96, x_, w=470, tam=24, cor=TINTA, lh=1.35))
p.append(icone("t:door", 1230, 40, 200, MUDO))
p.append(icone("t:calendar", 1450, 150, 110, OXID))
p.append("</svg>")
rs += [rot(1160, 290, "A recusa não fecha nada", w=504, tam=30, cor=TINTA, peso=700, serif=True),
       rot(1160, 350, "“Eu vou perguntar de novo daqui a um tempo, porque me importo com isso.”", w=480, tam=26, cor=OXID, peso=600, lh=1.35)]
S.append({"id": "cartao", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Pronto antes de precisar", "titulo": "Monte o cartão hoje",
          "fonte": "E para quem cuida: não ser o único apoio de ninguém, ter com quem discutir casos, deixar claro o canal de urgência"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fluxo de encaminhamento", "titulo": "Da frase solta à consulta marcada",
          "regras": ["Reconhecer, perguntar de forma direta, ficar",
                     "A gravidade decide quem você aciona; o 188 vale em qualquer degrau",
                     "Nome, marcação e retorno: o encaminhamento que chega"],
          "cards": [{"ic": "t:users", "t": "Quem treina e reabilita", "x": "Reconhece, pergunta, fica e encaminha com nome e telefone."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Avalia o risco clínico e aciona a emergência quando é emergência."},
                    {"ic": "h:psychology", "t": "Psicologia e psiquiatria", "x": "Avaliam, tratam e montam o plano de segurança."}]})

spec = {"arquivo": "aulas/MOD10/10-05-fluxo-de-encaminhamento.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Fluxo de encaminhamento", "subtitulo": "Da frase solta à consulta marcada",
        "nota_capa": "Entra por uma corredora de rua que brinca com não acordar.",
        "secoes": {"circulos": ["Reconhecer e perguntar.", "capa"], "roteiro": ["O roteiro de crise.", "roteiro"],
                   "cano": ["O encaminhamento de rotina.", "cano"], "cartao": ["Pronto antes de precisar.", "cartao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-05.json"), "w"), ensure_ascii=False, indent=1)
print("10-05.json:", len(S), "slides")
