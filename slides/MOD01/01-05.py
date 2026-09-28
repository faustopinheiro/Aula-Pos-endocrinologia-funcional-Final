"""Spec do deck 1.5 (refeito no modelo dos desenhos). Gera 01-05.json ao lado deste arquivo."""
import json, math, os, random, sys
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
def no(p, x, y, r, cor, cheio=True):
    p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{cor if cheio else CARTAO}" stroke="{cor}" stroke-width="3"/>')

# 1. quatro portas
p = [svg_abre(1664, 540, "Quatro portas: a do treinador, a da fisioterapia, a da balança e a do consultório médico; um atleta entra por cada uma das três primeiras, e a porta do médico fica vazia")]
portas = [("a do treinador", "h:running", "fratura por estresse começando", "“ficou mais lento: falta de foco”", FOSF),
          ("a da fisioterapia", "h:girl-1015y", "transtorno alimentar começando", "a terceira lesão do ano", GLIC),
          ("a da balança", "t:karate", "desidratação", "a véspera da pesagem", FOSF),
          ("a do médico", None, "", "quase ninguém entra primeiro por aqui", MUDO)]
rs = []
for k, (porta, ic, cond, pista, c) in enumerate(portas):
    x = k * 420
    vazia = ic is None
    p.append(f'<rect x="{x + 110}" y="110" width="200" height="330" rx="10" fill="{CARTAO if vazia else AZUL_T}" stroke="{MUDO if vazia else AZUL}" stroke-width="4"/>')
    p.append(f'<circle cx="{x + 280}" cy="290" r="9" fill="{MUDO if vazia else AZUL}"/>')
    if not vazia:
        p.append(icone(ic, x + 10, 280, 130, c))
        rs.append(rot(x, 0, cond, w=400, tam=26, cor=c, peso=700, alinha="center", serif=True, lh=1.15))
    rs.append(rot(x + 110, 450, porta, w=200, tam=24, cor=TINTA if not vazia else MUDO, peso=700, alinha="center"))
    rs.append(rot(x + 20, 490, pista, w=380, tam=22, cor=MUDO if vazia else TINTA, alinha="center", lh=1.25))
p.append(icone("t:stethoscope", 1260 + 150, 200, 80, CINZA))
p.append("</svg>")
S.append({"id": "portas", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Para começar", "titulo": "O atleta entra pela porta de quem ele vê mais",
          "destaque": "O que acontece com a informação depois que ela entra é o assunto de hoje."})

# 2. quatro formatos como redes
p = [svg_abre(1664, 560, "Quatro redes: o departamento completo com muitos nós num organograma; a equipe pequena com quatro nós todos ligados; a rede informal com três nós soltos e só uma linha pontilhada; o profissional sozinho com setas pontilhadas para contatos")]
rs = []
tit = [("Departamento completo", "clube, seleção, centro de treinamento", OXID), ("Equipe pequena", "academia, assessoria, box, clínica: 3 a 6 pessoas", OXID),
       ("Rede informal", "o arranjo mais comum do país", GLIC), ("Sozinho", "consultório ou personal, com uma agenda para encaminhar", AZUL)]
for k, (t, x_, c) in enumerate(tit):
    x = k * 420
    p.append(caixa(x, 0, 400, 400, c, [OXID_T, OXID_T, GLIC_T, AZUL_T][k], esp=3, rx=18))
    rs.append(rot(x + 10, 420, t, w=380, tam=28, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x + 10, 462, x_, w=380, tam=22, cor=TINTA, alinha="center", lh=1.25))
# departamento: organograma
c = OXID
p.append(f'<line x1="200" y1="80" x2="200" y2="140" stroke="{c}" stroke-width="3"/><line x1="80" y1="140" x2="320" y2="140" stroke="{c}" stroke-width="3"/>')
for xx in (80, 200, 320):
    p.append(f'<line x1="{xx}" y1="140" x2="{xx}" y2="200" stroke="{c}" stroke-width="3"/>')
    for yy in (220, 290):
        p.append(f'<line x1="{xx}" y1="200" x2="{xx}" y2="{yy}" stroke="{c}" stroke-width="3"/>')
no(p, 200, 70, 24, c)
for xx in (80, 200, 320):
    for yy in (210, 280, 340):
        no(p, xx, yy, 20, c)
# equipe pequena
pts = [(630, 110), (770, 110), (630, 290), (770, 290), (700, 200)]
for a in range(5):
    for b in range(a + 1, 5):
        p.append(f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" x2="{pts[b][0]}" y2="{pts[b][1]}" stroke="{OXID}" stroke-width="3"/>')
for (x, y) in pts:
    no(p, x, y, 26, OXID)
# rede informal
pts = [(960, 110), (1180, 150), (1030, 310)]
p.append(f'<line x1="960" y1="110" x2="1180" y2="150" stroke="{GLIC}" stroke-width="3"{TRACO}/>')
for (x, y) in pts:
    no(p, x, y, 30, GLIC)
p.append(icone("t:messages", 1040, 150, 46, GLIC))
no(p, 1110, 230, 18, TINTA)
rs.append(rot(1120, 260, "o atleta", w=120, tam=20, cor=TINTA, peso=600))
# sozinho
no(p, 1460, 200, 34, AZUL)
for (x, y) in [(1330, 80), (1600, 90), (1330, 330), (1600, 320)]:
    p.append(f'<line x1="1460" y1="200" x2="{x}" y2="{y}" stroke="{AZUL}" stroke-width="3"{TRACO}/>')
    no(p, x, y, 16, AZUL, cheio=False)
p.append("</svg>")
S.append({"id": "formatos", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeiro erro: achar que equipe é um lugar", "titulo": "Equipe é um conjunto de funções, em quatro formatos",
          "destaque": "As mesmas funções precisam acontecer nos quatro. O que muda é quem faz e com que recurso."})

# 3. oito funções: sete em volta, coordenação no meio
p = [svg_abre(1664, 600, "Sete funções em volta de um círculo e, no centro, em vermelho, a coordenação, ligada a todas")]
cx, cy = 832, 290
func = [("Triagem", "quem pode fazer o quê antes de começar", "t:filter"),
        ("Prescrição do treino", "define a carga e responde quando muda", "t:barbell"),
        ("Monitoramento", "coleta, registra e olha o dado", "t:chart-line"),
        ("Diagnóstico e conduta", "sintoma, doença, remédio, exame", "t:stethoscope"),
        ("Reabilitação e retorno", "do tecido lesionado à função", "h:crutches"),
        ("Nutrição e energia", "a conta de energia e o resto", "t:salad"),
        ("Saúde mental", "acolher, rastrear, adesão", "t:brain")]
rs = []
pos = []
for k in range(7):
    a = math.radians(-90 + k * 360 / 7)
    pos.append((cx + 640 * math.cos(a), cy + 235 * math.sin(a)))
for (x, y) in pos:
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{FOSF}" stroke-width="3" opacity="0.6"/>')
for (t, tx, ic), (x, y) in zip(func, pos):
    bx, by = x - 190, y - 52
    p.append(caixa(bx, by, 380, 104, OXID, OXID_T, esp=3, rx=16))
    p.append(icone(ic, bx + 16, by + 22, 56, OXID))
    rs.append(rot(bx + 84, by + 14, t, w=286, tam=24, cor=OXID, peso=700, serif=True, lh=1.1))
    rs.append(rot(bx + 84, by + 56, tx, w=286, tam=19, cor=TINTA, lh=1.2))
p.append(f'<circle cx="{cx}" cy="{cy}" r="110" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="6"/>')
p.append(icone("t:route", cx - 32, cy - 80, 64, FOSF))
rs += [rot(cx - 100, cy - 6, "Coordenação", w=200, tam=28, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(cx - 100, cy + 32, "quase sempre vaga", w=200, tam=20, cor=FOSF, peso=600, alinha="center")]
p.append("</svg>")
S.append({"id": "oito-funcoes", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Função, não profissão", "titulo": "Oito funções, e a que ninguém reivindica fica no meio"})

# 4. a folha com nomes
p = [svg_abre(1664, 520, "Uma folha com as oito funções em coluna e um nome ao lado de cada uma; três linhas ficam sem nome, em vermelho: triagem, monitoramento que alguém olha e coordenação")]
p.append(caixa(0, 0, 1000, 520, CINZA, CARTAO, esp=3, rx=14))
linhas = [("Triagem", None), ("Prescrição do treino", "treinador"), ("Monitoramento que alguém olha", None), ("Diagnóstico e conduta", "médica"),
          ("Reabilitação e retorno", "fisioterapeuta"), ("Nutrição e energia", "nutricionista"), ("Saúde mental", "psicóloga"), ("Coordenação", None)]
rs = []
for j, (f, nome) in enumerate(linhas):
    y = 22 + j * 62
    vaga = nome is None
    if vaga:
        p.append(f'<rect x="12" y="{y - 8}" width="976" height="56" rx="8" fill="{FOSF_T}"/>')
    rs.append(rot(40, y + 6, f, w=520, tam=26, cor=FOSF if vaga else TINTA, peso=700 if vaga else 500, serif=vaga))
    p.append(f'<line x1="600" y1="{y + 40}" x2="960" y2="{y + 40}" stroke="{FOSF if vaga else CINZA}" stroke-width="3"{TRACO if vaga else ""}/>')
    if not vaga:
        rs.append(rot(610, y + 4, nome, w=340, tam=28, cor=AZUL, peso=600, serif=True))
    else:
        rs.append(rot(610, y + 6, "?", w=340, tam=28, cor=FOSF, peso=700, alinha="center"))
p.append(caixa(1060, 0, 604, 240, OXID, OXID_T, esp=3, rx=18))
p.append(icone("h:person", 1090, 40, 90, OXID))
for k, t in enumerate(["triagem", "prescrição", "monitoramento"]):
    p.append(f'<rect x="{1200 + (k % 2) * 220}" y="{50 + (k // 2) * 60}" width="200" height="46" rx="23" fill="{CARTAO}" stroke="{OXID}" stroke-width="2"/>')
    rs.append(rot(1200 + (k % 2) * 220, 60 + (k // 2) * 60, t, w=200, tam=20, cor=OXID, peso=700, alinha="center"))
rs += [rot(1090, 170, "acumular funções numa equipe pequena: normal, e funciona", w=544, tam=22, cor=TINTA, lh=1.3)]
p.append(caixa(1060, 260, 604, 260, FOSF, FOSF_T, esp=4, rx=18))
rs += [rot(1090, 280, "A que falha é a vaga que ninguém sabe que está vaga", w=544, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2),
       rot(1090, 390, "quase sempre as mesmas três: triagem, monitoramento que alguém de fato olha, e coordenação", w=544, tam=22, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "funcao-vaga", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Segundo erro: achar que o problema é acumular", "titulo": "Escreva um nome ao lado de cada função",
          "destaque": "Fazer uma função não é ter competência exclusiva sobre ela. Aqui o ponto é garantir que a função exista."})

# 5. a informação que para
p = [svg_abre(1664, 440, "Quatro profissionais, cada um guardando o que viu no próprio caderno, aplicativo ou cabeça; nenhuma linha liga os quatro; uma seta longa leva ao quinto, meses depois, com a fratura"), defs(FOSF)]
silos = [("h:exercise-weights", "treinador", "ficou mais lento", "t:notebook"), ("h:crutches", "fisioterapeuta", "lesão que volta", "t:device-mobile"),
         ("t:salad", "nutricionista", "come pouco", "t:clipboard-list"), ("t:ear", "psicóloga", "ansiosa com o peso", "t:brain")]
rs = []
for k, (ic, prof, viu, onde) in enumerate(silos):
    x = k * 300
    p.append(caixa(x, 110, 270, 250, GLIC, GLIC_T, esp=3, rx=18))
    p.append(icone(ic, x + 95, 130, 80, GLIC))
    rs.append(rot(x, 220, prof, w=270, tam=22, cor=GLIC, peso=700, alinha="center"))
    p.append(f'<rect x="{x + 30}" y="260" width="210" height="80" rx="12" fill="{CARTAO}" stroke="{GLIC}" stroke-width="2"/>')
    p.append(icone(onde, x + 40, 278, 40, MUDO))
    rs.append(rot(x + 88, 278, viu, w=150, tam=20, cor=TINTA, peso=600, lh=1.2))
p.append(seta(1200, 235, 1400, 235, FOSF, "m0", esp=5))
p.append(caixa(1420, 110, 244, 250, FOSF, FOSF_T, esp=4, rx=18))
p.append(icone("h:stethoscope", 1500, 130, 80, FOSF))
rs += [rot(1420, 220, "o quinto, meses depois", w=244, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2),
       rot(1420, 280, "fratura", w=244, tam=30, cor=FOSF, peso=700, alinha="center", serif=True)]
motivos = [("t:eye-off", "não sabe que aquilo é importante"), ("t:zoom-question", "sabe, e não sabe para quem mandar"), ("t:home", "não existe um lugar onde a informação more")]
for k, (ic, t) in enumerate(motivos):
    x = k * 560
    p.append(icone(ic, x, 20, 56, FOSF))
    rs.append(rot(x + 70, 22, t, w=470, tam=24, cor=TINTA, peso=700, lh=1.2))
rs.append(rot(0, 384, "O dado existe. O conjunto não existe.", w=1664, tam=30, cor=TINTA, peso=700, alinha="center", serif=True))
p.append("</svg>")
S.append({"id": "informacao", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceiro erro: achar que a informação circula sozinha", "titulo": "A informação para em quem viu primeiro",
          "destaque": "Não é falta de competência. É falta de caminho para a informação.", "destaque_cor": "verm"})

# 6. a folha das três perguntas
p = [svg_abre(1664, 600, "Uma folha com três perguntas: onde a informação mora, com o conteúdo mínimo; quem chama a conversa quando as informações não batem; e quem assina cada tipo de decisão")]
p.append(caixa(0, 0, 1664, 600, CINZA, CARTAO, esp=3, rx=16))
blocos = [("t:home", "Onde a informação mora?", "um lugar só, que todos acessam; o suporte não importa",
           ["histórico de lesão", "carga da semana", "o que mudou", "o que cada um viu"], OXID),
          ("t:phone-call", "Quem chama a conversa quando as informações não batem?", "discordar é o sistema funcionando; o problema é virar a decisão de quem insiste mais",
           [], GLIC),
          ("t:writing", "Quem assina, por tipo de decisão?", "algumas são compartilhadas de propósito",
           ["alta clínica", "mudança de carga", "volta ao jogo", "ajuste de remédio"], AZUL)]
rs = []
for j, (ic, q, tx, chips, c) in enumerate(blocos):
    y = 30 + j * 190
    p.append(icone(ic, 40, y + 10, 70, c))
    rs.append(rot(140, y, q, w=1480, tam=32, cor=c, peso=700, serif=True))
    rs.append(rot(140, y + 52, tx, w=1480, tam=22, cor=TINTA))
    xc = 140
    for t in chips:
        w = 30 + len(t) * 13
        p.append(f'<rect x="{xc}" y="{y + 96}" width="{w}" height="44" rx="22" fill="{CARTAO}" stroke="{c}" stroke-width="2"/>')
        rs.append(rot(xc, y + 105, t, w=w, tam=20, cor=c, peso=700, alinha="center"))
        xc += w + 16
    if j < 2:
        p.append(f'<line x1="40" y1="{y + 170}" x2="1624" y2="{y + 170}" stroke="{GRADE}" stroke-width="2"/>')
# quem chama: dois balões que discordam
p.append(f'<rect x="140" y="{30 + 190 + 96}" width="300" height="44" rx="22" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
p.append(f'<rect x="470" y="{30 + 190 + 96}" width="300" height="44" rx="22" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="2"/>')
rs += [rot(140, 30 + 190 + 105, "treinador: “pode jogar”", w=300, tam=20, cor=GLIC, peso=700, alinha="center"),
       rot(470, 30 + 190 + 105, "fisioterapeuta: “não pode”", w=300, tam=20, cor=GLIC, peso=700, alinha="center")]
p.append("</svg>")
S.append({"id": "tres-perguntas", "tipo": "diagrama", "h": 600, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A estrutura mínima", "titulo": "A estrutura mínima cabe numa folha com três perguntas"})

# 7. de quem é a decisão
p = [svg_abre(1664, 560, "À esquerda, a pergunta de quem é esse paciente riscada, com duas profissões puxando o atleta; à direita, três nuvens de pontos, uma por profissão, que se sobrepõem quase por inteiro: a discordância dentro de cada profissão é maior que entre elas")]
p.append(caixa(0, 0, 640, 560, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("h:person", 270, 200, 100, TINTA))
p.append(icone("h:doctor", 40, 200, 100, FOSF))
p.append(icone("h:health-worker", 500, 200, 100, FOSF))
p.append(f'<line x1="140" y1="250" x2="270" y2="250" stroke="{FOSF}" stroke-width="5"/><line x1="370" y1="250" x2="500" y2="250" stroke="{FOSF}" stroke-width="5"/>')
rs = [rot(20, 30, "“De quem é esse paciente?”", w=600, tam=32, cor=FOSF, peso=700, serif=True, alinha="center"),
      rot(20, 340, "produz disputa de território", w=600, tam=24, cor=TINTA, peso=600, alinha="center"),
      rot(20, 420, "“De quem é esta decisão?”", w=600, tam=32, cor=OXID, peso=700, serif=True, alinha="center"),
      rot(20, 470, "cada tipo tem um responsável; algumas são compartilhadas", w=600, tam=22, cor=TINTA, alinha="center", lh=1.3)]
p.append(f'<line x1="40" y1="60" x2="600" y2="88" stroke="{FOSF}" stroke-width="5"/>')
random.seed(7)
grupos = [("médicos do esporte", AZUL, 960), ("fisioterapeutas", OXID, 1030), ("treinadores", GLIC, 1110)]
p.append(f'<line x1="720" y1="440" x2="1640" y2="440" stroke="{MUDO}" stroke-width="3"/>')
for (t, c, mx) in grupos:
    for _ in range(26):
        x = mx + random.gauss(0, 150)
        y = 120 + random.random() * 290
        x = max(740, min(1620, x))
        p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="{c}" opacity="0.75" stroke="{PAPEL}" stroke-width="2"/>')
for k, (t, c, mx) in enumerate(grupos):
    p.append(f'<circle cx="{760 + k * 300}" cy="30" r="10" fill="{c}"/>')
    rs.append(rot(778 + k * 300, 18, t, w=270, tam=22, cor=c, peso=700))
rs += [rot(720, 452, "critério para decidir a volta ao esporte", w=920, tam=22, cor=MUDO, alinha="center"),
       rot(720, 490, "dentro de cada profissão, a discordância foi em geral maior que entre profissões", w=920, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append("</svg>")
S.append({"id": "de-quem", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarto erro: a pergunta mal feita", "titulo": "O conflito é de critério, e não de corporação",
          "fonte": "Shrier, Safai e Charland, British Journal of Sports Medicine 2014 · nuvem de pontos: esquema, sem valores medidos"})

S.append({"id": "fecho", "tipo": "fecho", "titulo": "O que falha e o que compensa, formato por formato",
          "regras": ["Departamento completo: escrever quem assina quando técnica e competição discordam.",
                     "Equipe pequena: triagem e registro. A folha das três perguntas resolve quase tudo.",
                     "Rede informal: um lugar comum de registro e quem chama a conversa, combinados antes.",
                     "Sozinho: perguntar o que os outros estão vendo. “O que seu treinador falou do seu desempenho?”"],
          "quem": "Equipe não é quantidade de gente. É saber quais funções precisam existir, quem cumpre cada uma e onde a informação mora.",
          "proxima": "O que é seu, o que é do colega e o que é de todos"})

base = json.load(open(os.path.join(os.path.dirname(__file__), "01-05.json")))
spec = {k: v for k, v in base.items() if k != "slides"}
spec["slides"] = S
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "01-05.json"), "w"), ensure_ascii=False, indent=1)
print("01-05.json:", len(S), "slides")
