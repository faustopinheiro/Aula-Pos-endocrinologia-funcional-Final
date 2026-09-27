"""Spec do deck 10.8. Gera 10-08.json ao lado deste arquivo."""
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

# 1. os dois círculos
p = [svg_abre(1664, 500, "Dois círculos quase sobrepostos, excesso de treinamento e esgotamento, com a interseção maior que as partes; embaixo, a receita de duas semanas de descanso riscada")]
p.append(f'<circle cx="520" cy="230" r="220" fill="{AZUL}" fill-opacity="0.18" stroke="{AZUL}" stroke-width="5"/>')
p.append(f'<circle cx="800" cy="230" r="220" fill="{FOSF}" fill-opacity="0.14" stroke="{FOSF}" stroke-width="5"/>')
p.append(f'<rect x="1160" y="130" width="480" height="200" rx="16" fill="{CARTAO}" stroke="{MUDO}" stroke-width="3"/>')
p.append(icone("t:bed", 1190, 170, 90, MUDO))
p.append(f'<line x1="1170" y1="320" x2="1630" y2="140" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>')
p.append("</svg>")
rs = [rot(320, 200, "excesso de treinamento", w=220, tam=24, cor=AZUL, peso=700, alinha="center", lh=1.2),
      rot(830, 210, "esgotamento", w=170, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(590, 90, "exaustão · desempenho em queda · humor pior · sono ruim · vontade de parar", w=140, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.45),
      rot(1300, 180, "“duas semanas de descanso completo”", w=320, tam=26, cor=TINTA, peso=600, lh=1.3),
      rot(1160, 360, "voltou descansado, e sem vontade", w=480, tam=28, cor=FOSF, peso=700, alinha="center", serif=True)]
S.append({"id": "venn", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um triatleta amador, terceiro ironman em três anos", "titulo": "Descanso não trata o que não é cansaço",
          "fonte": "O excesso de treinamento está no módulo de endocrinologia"})

# 2. três pilares
p = [svg_abre(1664, 520, "Três pilares sustentando o esgotamento esportivo: exaustão física e emocional, realização reduzida e desvalorização do esporte, o terceiro em destaque")]
p.append(f'<rect x="80" y="20" width="1504" height="80" rx="10" fill="{TINTA}"/>')
pil = [("t:battery-1", "Exaustão física e emocional", "o descanso não repõe · é a que engana", AZUL, AZUL_T),
       ("t:trending-down", "Realização reduzida", "cai a percepção, com ou sem queda real", GLIC, GLIC_T),
       ("t:mood-empty", "Desvalorização do esporte", "indiferença ao que importava · é a que separa", FOSF, FOSF_T)]
rs = [rot(80, 42, "esgotamento esportivo", w=1504, tam=32, cor=PAPEL, peso=700, alinha="center", serif=True)]
for i, (ic, t, x_, c, ct) in enumerate(pil):
    x = 140 + i * 490
    p.append(f'<rect x="{x}" y="110" width="400" height="{360 if i < 2 else 380}" rx="8" fill="{ct}" stroke="{c}" stroke-width="{4 if i < 2 else 8}"/>')
    p.append(icone(ic, x + 150, 140, 100, c))
    rs.append(rot(x + 20, 270, t, w=360, tam=30, cor=c, peso=700, alinha="center", serif=True, lh=1.2))
    rs.append(rot(x + 30, 370, x_, w=340, tam=24, cor=TINTA, alinha="center", lh=1.3))
p.append(f'<rect x="80" y="490" width="1504" height="20" rx="4" fill="{GRADE}"/>')
p.append("</svg>")
S.append({"id": "pilares", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As três dimensões", "titulo": "Três dimensões, e a terceira é a que separa",
          "fonte": "Questionário de esgotamento em atletas, 2001: 15 itens, 5 por dimensão · no trabalho, a OMS descreve três dimensões parecidas"})

# 3. quer e não consegue / consegue e não quer
p = [svg_abre(1664, 480, "À esquerda, atleta atrás de uma porta trancada olhando o treino: quer e não consegue; à direita, atleta com a porta aberta de costas para o treino: consegue e não quer")]
for i in range(2):
    x = i * 850
    p.append(caixa(x, 0, 814, 380, AZUL if i == 0 else FOSF, AZUL_T if i == 0 else FOSF_T, esp=4, rx=22))
    p.append(f'<rect x="{x + 330}" y="60" width="150" height="260" rx="6" fill="{CARTAO}" stroke="{TINTA}" stroke-width="5"/>')
    p.append(icone("t:lock" if i == 0 else "t:lock-open", x + 370, 150, 70, TINTA))
    p.append(icone("t:bike", x + 560, 130, 150, MUDO))
    p.append(icone("h:person", x + 120 if i == 0 else x + 110, 120, 170, AZUL if i == 0 else FOSF))
p.append("</svg>")
rs = [rot(20, 320, "quer treinar e não consegue", w=774, tam=34, cor=AZUL, peso=700, alinha="center", serif=True),
      rot(870, 320, "consegue treinar e não quer", w=774, tam=34, cor=FOSF, peso=700, alinha="center", serif=True),
      rot(0, 410, "“O que você sente quando um treino é cancelado: alívio ou frustração?”", w=1664, tam=32, cor=TINTA, peso=700, alinha="center", serif=True)]
S.append({"id": "porta", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A frase que resolve a maior parte", "titulo": "Um quer e não consegue; o outro consegue e não quer",
          "fonte": "Os dois podem coexistir · a desvalorização nem sempre é dita"})

# 4. a tabela dos discriminadores
p = [svg_abre(1664, 560, "Tabela com cinco discriminadores entre excesso de treinamento e esgotamento, com a resposta ao repouso destacada, e a pergunta das duas semanas")]
linhas = [("resposta ao repouso", "melhora, devagar", "alivia a exaustão, não devolve a vontade"),
          ("atitude com o esporte", "preservada: quer voltar", "negativa, indiferente, ambivalente"),
          ("percepção de realização", "frustração com a queda", "insuficiência que antecede a queda"),
          ("curso no tempo", "ponto de virada identificável", "devagar, ao longo de temporadas"),
          ("peso do contexto", "a carga é central", "o contexto pesa muito")]
p.append(f'<rect x="420" y="0" width="600" height="60" rx="10" fill="{AZUL}"/>')
p.append(f'<rect x="1040" y="0" width="624" height="60" rx="10" fill="{FOSF}"/>')
rs = [rot(420, 14, "excesso de treinamento", w=600, tam=28, cor=PAPEL, peso=700, alinha="center"),
      rot(1040, 14, "esgotamento", w=624, tam=28, cor=PAPEL, peso=700, alinha="center")]
for j, (a, b, c) in enumerate(linhas):
    y = 76 + j * 78
    if j == 0:
        p.append(f'<rect x="0" y="{y - 4}" width="1664" height="74" rx="10" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
    else:
        p.append(f'<line x1="0" y1="{y - 6}" x2="1664" y2="{y - 6}" stroke="{GRADE}" stroke-width="2"/>')
    rs.append(rot(10, y + 14, a, w=400, tam=26, cor=TINTA, peso=700))
    rs.append(rot(430, y + 14, b, w=580, tam=26, cor=AZUL))
    rs.append(rot(1050, y + 14, c, w=604, tam=26, cor=FOSF))
p.append(f'<rect x="0" y="480" width="1664" height="80" rx="12" fill="{CARTAO}" stroke="{TINTA}" stroke-width="2"/>')
p.append("</svg>")
rs += [rot(20, 500, "Duas semanas sem treino?", w=380, tam=26, cor=TINTA, peso=700, serif=True),
       rot(430, 500, "“vou perder tudo”", w=580, tam=26, cor=AZUL, peso=700),
       rot(1050, 500, "“ia ser ótimo”", w=604, tam=26, cor=FOSF, peso=700)]
S.append({"id": "tabela", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os discriminadores", "titulo": "O repouso alivia a exaustão e não devolve a vontade"})

# 5. restrito ou espalhado
p = [svg_abre(1664, 540, "À esquerda, só o círculo do esporte apagado em volta da pessoa: esgotamento; à direita, todos os círculos apagados: depressão; embaixo, quatro causas clínicas para excluir")]
areas = ["trabalho", "relações", "lazer", "autocuidado", "esporte"]
rs = []
for k, (cx, todos, t, c) in enumerate([(400, False, "esgotamento: restrito ao esporte", OXID), (1260, True, "depressão: espalhada pela vida", FOSF)]):
    p.append(icone("h:person", cx - 55, 150, 110, TINTA))
    for i, a in enumerate(areas):
        ang = math.radians(-90 + i * 72)
        x, y = cx + 260 * math.cos(ang), 205 + 155 * math.sin(ang)
        apagado = todos or a == "esporte"
        p.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="84" ry="52" fill="{"#E6E3DA" if apagado else OXID_T}" stroke="{CINZA if apagado else OXID}" stroke-width="4"/>')
        rs.append(rot(x - 80, y - 14, a, w=160, tam=22, cor=MUDO if apagado else TINTA, peso=700, alinha="center"))
    rs.append(rot(cx - 330, 385, t, w=660, tam=28, cor=c, peso=700, alinha="center", serif=True))
p.append(f'<line x1="832" y1="10" x2="832" y2="420" stroke="{GRADE}" stroke-width="2"/>')
p.append(f'<rect x="0" y="450" width="1664" height="84" rx="12" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
p.append("</svg>")
rs.append(rot(20, 474, "Excluir antes: anemia e ferro · tireoide · apneia do sono · baixa disponibilidade de energia", w=1624, tam=28, cor=TINTA, peso=700, alinha="center"))
S.append({"id": "circulos", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os dois diferenciais", "titulo": "Restrito ao esporte favorece esgotamento; espalhado, depressão",
          "fonte": "Causas clínicas nos módulos de medicina esportiva clínica, endocrinologia e nutrição"})

# 6. a árvore e as raízes
p = [svg_abre(1664, 560, "Árvore murcha com raízes: à esquerda as do alto rendimento, à direita as do amador; no tronco, relação com o treino")]
p.append(f'<ellipse cx="832" cy="90" rx="220" ry="90" fill="#D8D3C4"/>')
p.append(f'<path d="M800 170 L790 300 H874 L864 170 Z" fill="#9C8E74"/>')
p.append(f'<line x1="0" y1="300" x2="1664" y2="300" stroke="#9C8E74" stroke-width="4"/>')
elite = ["pressão externa", "falta de autonomia", "monotonia", "especialização precoce", "identidade só de atleta", "perfeccionismo"]
amador = ["obrigação autoimposta", "treino como tarefa", "comparação permanente", "culpa"]
rs = []
for i, t in enumerate(elite):
    y = 330 + i * 38
    x = 120 + (i % 2) * 40
    p.append(f'<path d="M812 300 C 760 {y}, 600 {y}, {x + 300} {y + 12}" fill="none" stroke="{AZUL}" stroke-width="4"/>')
    rs.append(rot(x, y - 4, t, w=300, tam=24, cor=AZUL, peso=600, alinha="right"))
for i, t in enumerate(amador):
    y = 340 + i * 52
    p.append(f'<path d="M852 300 C 900 {y}, 1060 {y}, {1150} {y + 12}" fill="none" stroke="{FOSF}" stroke-width="5"/>')
    rs.append(rot(1170, y - 4, t, w=440, tam=26, cor=FOSF, peso=700))
p.append("</svg>")
rs += [rot(640, 60, "esgotamento", w=384, tam=30, cor=TINTA, peso=700, alinha="center", serif=True),
       rot(900, 200, "relação com o treino", w=320, tam=28, cor=TINTA, peso=700, serif=True),
       rot(0, 250, "alto rendimento", w=400, tam=26, cor=AZUL, peso=700, serif=True),
       rot(1170, 250, "amador", w=400, tam=26, cor=FOSF, peso=700, serif=True)]
S.append({"id": "arvore", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "De onde vem", "titulo": "No amador, a raiz é a relação com o treino, não a carga",
          "fonte": "O aplicativo que cobra, a sequência que não pode quebrar, a meta anual que virou dívida"})

# 7. a régua e o esgotamento
p = [svg_abre(1664, 500, "Régua da motivação, da falta de motivação à intrínseca; acima, o esgotamento alto sobre a falta de motivação, baixo sobre a autônoma e a intrínseca, sem inclinação sobre a controlada")]
segs = [("falta de motivação", FOSF), ("controlada", GLIC), ("autônoma", AZUL), ("intrínseca", OXID)]
for i, (t, c) in enumerate(segs):
    p.append(f'<rect x="{i * 416}" y="380" width="404" height="90" rx="10" fill="{c}"/>')
p.append(f'<path d="M20 90 C 200 90, 330 120, 404 150" fill="none" stroke="{FOSF}" stroke-width="8"/>')
p.append(f'<path d="M416 200 H 820" fill="none" stroke="{GLIC}" stroke-width="8" stroke-dasharray="18 12"/>')
p.append(f'<path d="M832 230 C 1000 270, 1200 300, 1644 320" fill="none" stroke="{OXID}" stroke-width="8"/>')
p.append(f'<line x1="0" y1="350" x2="1664" y2="350" stroke="{GRADE}" stroke-width="2"/>')
rs = [rot(i * 416, 408, t, w=404, tam=28, cor=PAPEL, peso=700, alinha="center") for i, (t, c) in enumerate(segs)]
p.append("</svg>")
rs += [rot(20, 20, "mais esgotamento", w=400, tam=28, cor=FOSF, peso=700, serif=True),
       rot(430, 220, "pouca ou nenhuma associação", w=380, tam=24, cor=GLIC, peso=700, alinha="center"),
       rot(1200, 230, "menos esgotamento", w=440, tam=28, cor=OXID, peso=700, alinha="right", serif=True),
       rot(840, 60, "necessidades atendidas: autonomia, competência, vínculo", w=800, tam=26, cor=TINTA, peso=600, alinha="right")]
S.append({"id": "regua", "tipo": "diagrama", "h": 500, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A régua da primeira aula, de novo", "titulo": "Quanto mais a razão vem de dentro, menos esgota",
          "fonte": "Esquema, sem valores medidos · metanálise de 2013 em atletas · teoria da autodeterminação de Deci e Ryan"})

# 8. o painel de alavancas
p = [svg_abre(1664, 540, "Painel com quatro alavancas, autonomia, variedade, sentido e vínculo; uma alavanca menor travada, volume; embaixo, três botões riscados")]
alav = [("t:adjustments-horizontal", "Autonomia", "escolher dias e exercícios", AZUL),
        ("t:refresh", "Variedade", "outra modalidade, lugar, grupo", GLIC),
        ("t:compass", "Sentido", "“por que você começou? ainda é verdade?”", OXID),
        ("t:users-group", "Vínculo", "treinar com gente", FOSF)]
rs = []
for i, (ic, t, x_, c) in enumerate(alav):
    x = i * 330
    p.append(f'<rect x="{x + 130}" y="40" width="30" height="260" rx="15" fill="#E6E3DA"/>')
    p.append(f'<rect x="{x + 100}" y="60" width="90" height="56" rx="14" fill="{c}"/>')
    p.append(icone(ic, x + 115, 310, 60, c))
    rs.append(rot(x + 10, 380, t, w=270, tam=30, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x + 10, 426, x_, w=270, tam=22, cor=TINTA, alinha="center", lh=1.25))
p.append(f'<rect x="1360" y="20" width="304" height="300" rx="16" fill="#EEEBE3" stroke="{CINZA}" stroke-width="3"/>')
p.append(f'<rect x="1497" y="60" width="30" height="200" rx="15" fill="{CINZA}"/>')
p.append(f'<rect x="1472" y="190" width="80" height="44" rx="12" fill="{MUDO}"/>')
p.append(icone("t:lock", 1400, 60, 56, MUDO))
p.append("</svg>")
rs += [rot(1370, 270, "volume: ajuda a exaustão, não trata o resto", w=284, tam=22, cor=MUDO, peso=700, alinha="center", lh=1.25),
       rot(1360, 380, "Não funciona:", w=304, tam=26, cor=FOSF, peso=700, serif=True),
       rot(1360, 424, "mais cobrança · apelo à disciplina · meta nova e ambiciosa", w=304, tam=22, cor=FOSF, lh=1.3)]
S.append({"id": "painel", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A conduta", "titulo": "Quatro alavancas, e o volume não é uma delas",
          "destaque": "Nomear primeiro. E, se nada basta, a pausa deliberada: data marcada, sem culpa, outra atividade no lugar.", "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Esgotamento e sobrecarga crônica", "titulo": "O erro não foi o descanso",
          "regras": ["Quer e não consegue, ou consegue e não quer",
                     "Diferencial com depressão e com as causas clínicas",
                     "Autonomia, variedade, sentido e vínculo"],
          "cards": [{"ic": "t:users", "t": "Quem conduz o treino", "x": "Devolve escolha, varia o formato e traz o grupo de volta."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Faz os diferenciais antes de fechar a hipótese."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Entra quando há sofrimento maior ou a identidade está em jogo."}]})

spec = {"arquivo": "aulas/MOD10/10-08-esgotamento-e-sobrecarga-cronica.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Esgotamento e sobrecarga crônica", "subtitulo": "Quando o descanso não devolve a vontade",
        "nota_capa": "Entra por um triatleta que voltou das férias descansado, e sem vontade.",
        "secoes": {"venn": ["O erro e as três dimensões.", "capa"], "porta": ["Os discriminadores.", "porta"],
                   "arvore": ["De onde vem.", "arvore"], "painel": ["O que trata.", "painel"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-08.json"), "w"), ensure_ascii=False, indent=1)
print("10-08.json:", len(S), "slides")
