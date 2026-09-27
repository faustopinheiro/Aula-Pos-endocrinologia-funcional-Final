"""Spec do deck 10.10. Gera 10-10.json ao lado deste arquivo."""
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

# 1. a pirâmide
p = [svg_abre(1664, 520, "Pirâmide de quatro camadas: na base larga a violência psicológica; acima a física, a sexual e a negligência; uma seta sai da base para cima: o núcleo das outras"), defs(FOSF)]
camadas = [("negligência", GLIC_T, GLIC), ("sexual", FOSF_T, FOSF), ("física", AZUL_T, AZUL), ("psicológica", FOSF, FOSF)]
rs = []
for i, (t, c, cb) in enumerate(camadas):
    y = 20 + i * 120
    topo = 60 + i * 150
    base = 60 + (i + 1) * 150
    cx = 480
    p.append(f'<path d="M{cx - topo} {y} H{cx + topo} L{cx + base} {y + 110} H{cx - base} Z" fill="{c}" stroke="{cb}" stroke-width="3"/>')
    rs.append(rot(cx - 200, y + 38, t, w=400, tam=30 if i < 3 else 36, cor=PAPEL if i == 3 else TINTA, peso=700, alinha="center", serif=True))
p.append(f'<path d="M1000 480 C 1080 380, 1080 160, 1000 60" fill="none" stroke="{FOSF}" stroke-width="6" marker-end="url(#m0)"/>')
p.append("</svg>")
rs += [rot(1110, 220, "o núcleo das outras", w=554, tam=36, cor=FOSF, peso=700, serif=True),
       rot(1110, 290, "humilhação · desprezo · gritos · bode expiatório · rejeição · isolamento · ameaça", w=554, tam=26, cor=TINTA, lh=1.4),
       rot(1110, 40, "em todos os esportes e em todos os níveis", w=554, tam=26, cor=TINTA, peso=700)]
S.append({"id": "piramide", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Uma atleta adolescente no atletismo de base", "titulo": "A violência psicológica é o núcleo das outras",
          "fonte": "Consenso do Comitê Olímpico Internacional, 2016 · atualizado em 2024: a proteção é responsabilidade de todos"})

# 2. a prevalência
p = [svg_abre(1664, 500, "Barras de violência na infância dentro do esporte: psicológica 38%, física 11%, sexual 14%; em cada barra a parte grave: 9%, 8% e 6%; ao lado, os grupos que relataram mais")]
base, esc = 420, 9
dados = [("psicológica", 38, 9), ("física", 11, 8), ("sexual", 14, 6)]
rs = []
for i, (t, v, g) in enumerate(dados):
    x = 80 + i * 260
    p.append(f'<rect x="{x}" y="{base - v*esc}" width="200" height="{v*esc}" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
    p.append(f'<rect x="{x}" y="{base - g*esc}" width="200" height="{g*esc}" rx="10" fill="{FOSF}"/>')
    rs.append(rot(x, base - v * esc - 62, f"{v}%", w=200, tam=48, cor=FOSF, peso=700, alinha="center", serif=True))
    rs.append(rot(x, base + 12, t, w=200, tam=26, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x, base - g * esc + 8 if g * esc > 50 else base - g * esc - 34, f"grave {g}%", w=200, tam=22, cor=PAPEL if g * esc > 50 else FOSF, peso=700, alinha="center"))
p.append(f'<line x1="40" y1="{base}" x2="860" y2="{base}" stroke="{MUDO}" stroke-width="2"/>')
grupos = [("h:people", "minorias étnicas"), ("t:heart", "pessoas LGB"), ("h:wheelchair", "pessoas com deficiência"), ("t:medal", "nível internacional")]
for j, (ic, t) in enumerate(grupos):
    y = 60 + j * 95
    p.append(icone(ic, 1000, y, 64, AZUL))
    rs.append(rot(1090, y + 16, t, w=560, tam=28, cor=TINTA, peso=600))
p.append("</svg>")
rs.append(rot(1000, 0, "Relataram mais:", w=600, tam=30, cor=AZUL, peso=700, serif=True))
S.append({"id": "prevalencia", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quanto", "titulo": "Não é raro, e é mais comum onde há mais poder e menos voz",
          "fonte": "Holanda e Bélgica, 2016: mais de 4.000 adultos que praticaram esporte organizado antes dos 18 anos"})

# 3. os sinais
p = [svg_abre(1664, 560, "Duas colunas de sinais: na atleta e no ambiente; entre elas, uma escada leve com a legenda parece cuidado")]
atleta = [("t:door-exit", "evita um treino, um horário ou uma pessoa"), ("t:mood-empty", "muda de comportamento, se isola"),
          ("t:trending-down", "cai de rendimento sem motivo claro"), ("t:first-aid-kit", "queixas físicas sem explicação"),
          ("t:alert-triangle", "medo de ficar sozinha com alguém")]
ambiente = [("t:star", "atenção especial a uma atleta só"), ("t:gift", "presentes"), ("t:device-mobile", "mensagens privadas e segredos"),
            ("t:car", "caronas; afastar do grupo e da família"), ("t:stairs", "testes pequenos de limite, que crescem")]
rs = [rot(0, 0, "Na atleta", w=700, tam=32, cor=AZUL, peso=700, serif=True),
      rot(964, 0, "No ambiente", w=700, tam=32, cor=FOSF, peso=700, serif=True)]
for j, ((ic1, t1), (ic2, t2)) in enumerate(zip(atleta, ambiente)):
    y = 70 + j * 96
    p.append(f'<rect x="0" y="{y}" width="700" height="80" rx="12" fill="{AZUL_T}"/>')
    p.append(f'<rect x="964" y="{y}" width="700" height="80" rx="12" fill="{FOSF_T}"/>')
    p.append(icone(ic1, 16, y + 12, 56, AZUL))
    p.append(icone(ic2, 980, y + 12, 56, FOSF))
    rs.append(rot(90, y + 24, t1, w=600, tam=26, cor=TINTA, peso=600))
    rs.append(rot(1054, y + 24, t2, w=600, tam=26, cor=TINTA, peso=600))
for k in range(5):
    y = 480 - k * 90
    p.append(f'<line x1="760" y1="{y}" x2="904" y2="{y}" stroke="{GLIC}" stroke-width="5"/>')
p.append(f'<line x1="760" y1="60" x2="760" y2="500" stroke="{GLIC}" stroke-width="5"/><line x1="904" y1="60" x2="904" y2="500" stroke="{GLIC}" stroke-width="5"/>')
p.append("</svg>")
rs.append(rot(700, 510, "parece cuidado", w=264, tam=26, cor=GLIC, peso=700, alinha="center", serif=True))
S.append({"id": "sinais", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeira decisão: reconhecer", "titulo": "O aliciamento parece cuidado até deixar de parecer",
          "fonte": "Nenhum sinal prova nada · a pergunta útil: essa relação acontece de forma visível, dentro das regras?"})

# 4. ouvir
p = [svg_abre(1664, 540, "Dois balões: o que fazer quando alguém conta, e o que não fazer, riscado; embaixo, a frase que não promete segredo")]
p.append(f'<path d="M0 20 h760 a20 20 0 0 1 20 20 v320 a20 20 0 0 1 -20 20 h-620 l-50 50 v-50 h-90 a20 20 0 0 1 -20 -20 v-320 a20 20 0 0 1 20 -20 Z" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
p.append(f'<path d="M884 20 h760 a20 20 0 0 1 20 20 v320 a20 20 0 0 1 -20 20 h-90 v50 l-50 -50 h-620 a20 20 0 0 1 -20 -20 v-320 a20 20 0 0 1 20 -20 Z" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>')
fazer = ["ouvir", "acreditar", "agradecer", "“não é culpa sua”", "explicar o que vai acontecer", "registrar as palavras dela"]
nao = ["investigar", "perguntar detalhes", "confrontar o suspeito", "prometer segredo", "duvidar em voz alta"]
rs = [rot(40, 40, "Fazer", w=700, tam=32, cor=OXID, peso=700, serif=True), rot(924, 40, "Não fazer", w=700, tam=32, cor=FOSF, peso=700, serif=True)]
for j, t in enumerate(fazer):
    x, y = 40 + (j % 2) * 360, 110 + (j // 2) * 76
    p.append(icone("t:check", x, y, 40, OXID))
    rs.append(rot(x + 50, y + 6, t, w=300, tam=26, cor=TINTA, peso=600))
for j, t in enumerate(nao):
    x, y = 924 + (j % 2) * 360, 110 + (j // 2) * 76
    p.append(icone("t:x", x, y, 40, FOSF))
    rs.append(rot(x + 50, y + 6, t, w=300, tam=26, cor=TINTA, peso=600))
p.append(f'<rect x="0" y="440" width="1664" height="96" rx="14" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
p.append("</svg>")
rs.append(rot(30, 456, "“O que você me contou é sério, e eu não posso guardar só comigo. Vou avisar quem pode te proteger, e vou te contar cada passo.”", w=1604, tam=26, cor=TINTA, peso=700, alinha="center", serif=True, lh=1.3))
S.append({"id": "ouvir", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Segunda decisão: quando alguém conta", "titulo": "Quem ouve não investiga, e não promete segredo",
          "fonte": "Registrar com as palavras dela, entre aspas, com data e hora, sem interpretação"})

# 5. o fluxo de comunicação
p = [svg_abre(1664, 540, "Fluxo: da suspeita saem três caminhos, Conselho Tutelar, Disque 100 e polícia; ao lado, a pessoa responsável pela proteção no clube; embaixo, os artigos do estatuto"), defs(TINTA)]
p.append(caixa(0, 150, 320, 150, FOSF, FOSF_T, esp=5))
p.append(icone("t:eye", 30, 180, 80, FOSF))
canais = [("h:justice", "Conselho Tutelar", "obrigatório para criança e adolescente", OXID, 10),
          ("t:phone-call", "Disque 100", "gratuito · 24 horas · pode ser anônimo", AZUL, 160),
          ("t:alert-triangle", "Polícia, 190", "se houver perigo imediato", FOSF, 310)]
rs = [rot(120, 190, "suspeita", w=190, tam=32, cor=FOSF, peso=700, serif=True), rot(120, 240, "já basta", w=190, tam=26, cor=TINTA, peso=700)]
for ic, t, x_, c, y in canais:
    p.append(seta(330, 225, 540, y + 60, TINTA, "m0", esp=4))
    p.append(caixa(560, y, 620, 120, c, CARTAO, esp=4))
    p.append(icone(ic, 580, y + 25, 70, c))
    rs.append(rot(670, y + 18, t, w=490, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(670, y + 66, x_, w=490, tam=24, cor=TINTA))
p.append(caixa(1240, 100, 424, 220, GLIC, GLIC_T, esp=3))
p.append(icone("t:shield", 1270, 130, 70, GLIC))
p.append(f'<rect x="0" y="460" width="1664" height="76" rx="12" fill="{TINTA}"/>')
p.append("</svg>")
rs += [rot(1350, 140, "Proteção no clube", w=300, tam=28, cor=GLIC, peso=700, serif=True),
       rot(1270, 220, "acionada também, nunca no lugar dos canais oficiais", w=370, tam=24, cor=TINTA, lh=1.3),
       rot(20, 478, "ECA · art. 13: comunicação obrigatória · art. 70-B: dever de quem cuida por profissão · art. 245: multa por omissão", w=1624, tam=24, cor=PAPEL, peso=700, alinha="center")]
S.append({"id": "fluxo", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceira decisão: comunicar", "titulo": "Com criança e adolescente, a suspeita já obriga",
          "fonte": "Com adultos, a decisão de denunciar é da pessoa; a equipe acolhe, informa os caminhos e apoia, salvo risco à vida"})

# 6. a linha
p = [svg_abre(1664, 500, "Escala de práticas de treino, do aceitável ao abusivo: correção firme, grito ocasional, humilhação em público, pesagem na frente do grupo, exercício como punição, exclusão como castigo; a linha entre as duas partes marcada")]
praticas = [("correção firme", OXID, OXID_T), ("cobrança de desempenho", OXID, OXID_T), ("humilhação em público", FOSF, FOSF_T),
            ("pesagem na frente do grupo, comentário sobre o corpo", FOSF, FOSF_T), ("exercício como punição", FOSF, FOSF_T), ("exclusão e silêncio como castigo", FOSF, FOSF_T)]
rs = []
for i, (t, c, ct) in enumerate(praticas):
    x = i * 278
    p.append(f'<rect x="{x}" y="120" width="258" height="220" rx="16" fill="{ct}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x + 14, 170, t, w=230, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.3))
p.append(f'<line x1="546" y1="60" x2="546" y2="400" stroke="{TINTA}" stroke-width="6" stroke-dasharray="16 10"/>')
p.append(f'<rect x="0" y="380" width="530" height="12" rx="6" fill="{OXID}"/><rect x="560" y="380" width="1104" height="12" rx="6" fill="{FOSF}"/>')
p.append("</svg>")
rs += [rot(0, 60, "exigência", w=530, tam=30, cor=OXID, peso=700, alinha="center", serif=True),
       rot(560, 60, "desprezo pela pessoa", w=1104, tam=30, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(360, 420, "a cultura costuma esconder esta linha", w=380, tam=24, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "linha", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A violência que parece método", "titulo": "Exigir não é humilhar",
          "fonte": "Comentário sobre corpo e pesagem pública: a alimentação desordenada está no módulo de nutrição"})

# 7. a planta do clube
p = [svg_abre(1664, 560, "Planta de um clube com as regras desenhadas nos lugares: celular, sala de atendimento, vestiário, carro e viagem, entrada, mural do canal de denúncia")]
p.append(f'<rect x="0" y="0" width="1664" height="560" rx="18" fill="{CARTAO}" stroke="{TINTA}" stroke-width="5"/>')
salas = [(0, 0, 560, 280, "t:device-mobile", "Comunicação", "grupos com os responsáveis; sem mensagem privada com menor", AZUL),
         (560, 0, 560, 280, "t:door", "Atendimento", "porta aberta ou segundo adulto", OXID),
         (1120, 0, 544, 280, "t:users", "Vestiário e viagem", "regra de dois adultos; nenhuma carona a sós", GLIC),
         (0, 280, 560, 280, "t:clipboard-check", "Entrada", "triagem de quem trabalha com crianças; formação da equipe", AZUL),
         (560, 280, 560, 280, "t:speakerphone", "Canal de denúncia", "que não passe pela pessoa denunciada", FOSF),
         (1120, 280, 544, 280, "t:shield", "Responsável pela proteção", "alguém com esse nome e esse papel", OXID)]
rs = []
for x, y, w, h, ic, t, x_, c in salas:
    p.append(f'<rect x="{x + 12}" y="{y + 12}" width="{w - 24}" height="{h - 24}" rx="12" fill="none" stroke="{GRADE}" stroke-width="3"/>')
    p.append(icone(ic, x + 36, y + 40, 70, c))
    rs.append(rot(x + 126, y + 50, t, w=w - 160, tam=30, cor=c, peso=700, serif=True, lh=1.15))
    rs.append(rot(x + 36, y + 140, x_, w=w - 72, tam=24, cor=TINTA, lh=1.35))
p.append("</svg>")
S.append({"id": "planta", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarta decisão: prevenir", "titulo": "Proteger é desenho de ambiente, não confiança pessoal",
          "fonte": "As regras protegem as crianças e os adultos honestos · consenso de 2024: esporte centrado no atleta"})

# 8. a sala de atendimento
p = [svg_abre(1664, 500, "Sala de atendimento vista de cima: porta entreaberta, cadeira para o acompanhante, maca e um cartaz; três etiquetas: acompanhante, explicação e consentimento, limites nas redes")]
p.append(f'<rect x="0" y="0" width="760" height="500" rx="10" fill="{PAPEL}" stroke="{TINTA}" stroke-width="8"/>')
p.append(f'<rect x="280" y="-6" width="160" height="16" fill="{PAPEL}"/>')
p.append(f'<path d="M280 4 L360 90" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<rect x="80" y="160" width="360" height="140" rx="16" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
p.append(f'<rect x="540" y="320" width="120" height="120" rx="20" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append(f'<rect x="560" y="60" width="160" height="110" rx="8" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
etiquetas = [("t:users", "Acompanhante", "responsável presente, ou porta aberta e alguém da equipe perto", OXID),
             ("t:message-circle", "Explicar e perguntar", "“posso explicar antes de tocar?”", GLIC),
             ("t:device-mobile", "Limites nas redes", "não seguir menores em perfis pessoais; só o canal oficial", AZUL)]
rs = [rot(80, 210, "maca", w=360, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(500, 448, "acompanhante", w=200, tam=22, cor=OXID, peso=700, alinha="center"),
      rot(370, 40, "porta entreaberta", w=180, tam=22, cor=TINTA, peso=700),
      rot(560, 90, "“posso explicar antes?”", w=160, tam=20, cor=GLIC, peso=700, alinha="center", lh=1.2)]
for j, (ic, t, x_, c) in enumerate(etiquetas):
    y = 10 + j * 165
    p.append(icone(ic, 840, y + 20, 70, c))
    rs.append(rot(940, y + 18, t, w=720, tam=30, cor=c, peso=700, serif=True))
    rs.append(rot(940, y + 66, x_, w=720, tam=24, cor=TINTA, lh=1.3))
p.append("</svg>")
S.append({"id": "sala", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Uma decisão de cada um", "titulo": "O próprio consultório também é ambiente",
          "fonte": "Conforme as normas de cada profissão · nenhuma dessas práticas supõe má intenção de ninguém"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Ambiente seguro", "titulo": "A proteção não pode depender da boa índole de ninguém",
          "regras": ["Reconhecer: o aliciamento parece cuidado",
                     "Ouvir sem investigar e sem prometer segredo",
                     "Comunicar: com criança e adolescente, a suspeita já obriga"],
          "cards": [{"ic": "t:users", "t": "Toda a equipe", "x": "Reconhece, ouve, registra e comunica ao Conselho Tutelar."},
                    {"ic": "t:shield", "t": "O clube", "x": "Desenha o ambiente: regras, triagem, canal e responsável."},
                    {"ic": "h:psychology", "t": "Psicologia e rede de proteção", "x": "Acolhem a vítima e conduzem o que vem depois."}]})

spec = {"arquivo": "aulas/MOD10/10-10-ambiente-seguro-assedio-abuso-e-protecao.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Ambiente seguro", "subtitulo": "Assédio, abuso e proteção no esporte",
        "nota_capa": "Uma atleta que passou a pedir horário em que o treinador não estivesse.",
        "secoes": {"piramide": ["O que é e quanto.", "capa"], "sinais": ["Reconhecer e ouvir.", "sinais"],
                   "fluxo": ["Comunicar.", "fluxo"], "planta": ["Prevenir.", "planta"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-10.json"), "w"), ensure_ascii=False, indent=1)
print("10-10.json:", len(S), "slides")
