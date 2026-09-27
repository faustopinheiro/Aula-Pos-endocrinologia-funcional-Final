"""Spec do deck 10.4. Gera 10-04.json ao lado deste arquivo."""
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

# 1. a ponte
p = [svg_abre(1664, 460, "Uma ponte: de um lado a pessoa sem queixa, no meio o questionário que só sinaliza, do outro lado a avaliação clínica onde está o diagnóstico")]
p.append(f'<rect x="0" y="300" width="360" height="160" rx="12" fill="{AZUL_T}"/>')
p.append(f'<rect x="1304" y="300" width="360" height="160" rx="12" fill="{OXID_T}"/>')
p.append(f'<path d="M340 300 Q 832 40 1324 300" fill="none" stroke="{TINTA}" stroke-width="8"/>')
for k in range(1, 10):
    x = 340 + k * 98.4
    t = (x - 340) / 984
    y = (1 - t) ** 2 * 300 + 2 * (1 - t) * t * 40 + t ** 2 * 300
    p.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x:.0f}" y2="300" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="340" y1="300" x2="1324" y2="300" stroke="{TINTA}" stroke-width="6"/>')
p.append(icone("h:person", 110, 150, 140, AZUL))
p.append(icone("t:play-volleyball", 20, 30, 100, "#C9CFD4"))
p.append(f'<circle cx="832" cy="200" r="86" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="5"/>')
p.append(icone("t:clipboard-list", 772, 140, 120, GLIC))
p.append(icone("h:psychology", 1414, 150, 140, OXID))
p.append("</svg>")
rs = [rot(0, 330, "pessoa sem queixa", w=360, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(632, 310, "13 pontos", w=400, tam=44, cor=GLIC, peso=700, alinha="center", serif=True),
      rot(582, 370, "sinaliza probabilidade e abre uma conversa", w=500, tam=26, cor=TINTA, alinha="center"),
      rot(1304, 330, "avaliação clínica", w=360, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(1304, 380, "aqui está o diagnóstico", w=360, tam=24, cor=OXID, peso=600, alinha="center")]
S.append({"id": "ponte", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Rastreio não é diagnóstico", "titulo": "O questionário abre a conversa, não fecha o diagnóstico",
          "destaque": "O que um positivo autoriza: “vale conversar com alguém especializado, e eu posso te ajudar a encontrar”.", "destaque_cor": "tinta"})

# 2. a porta e o caminho
p = [svg_abre(1664, 540, "Uma porta aberta com uma pessoa na soleira; atrás, três caminhos já desenhados: profissional de referência, rede pública e emergência. Embaixo, a pergunta se o resultado muda a conduta"), defs(OXID, FOSF)]
p.append(f'<rect x="60" y="20" width="300" height="420" rx="8" fill="{PAPEL}" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<path d="M60 20 L 200 70 L 200 470 L 60 440 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(f'<rect x="40" y="440" width="340" height="16" rx="4" fill="{TINTA}"/>')
p.append(icone("h:person", 220, 250, 180, TINTA))
cam = [("h:psychology", "profissional de referência", "com quem você já conversou", OXID, 60),
       ("t:building-hospital", "rede pública", "unidade básica → centro de atenção psicossocial", OXID, 210),
       ("t:phone-call", "emergência", "o número à mão, para o caso de risco", FOSF, 360)]
rs = []
for ic, t, x, c, y in cam:
    p.append(seta(410, 250, 610, y + 50, c, "m0" if c == OXID else "m1", esp=4))
    p.append(caixa(630, y, 1034, 110, c, OXID_T if c == OXID else FOSF_T, esp=3))
    p.append(icone(ic, 650, y + 15, 80, c))
    rs.append(rot(750, y + 16, t, w=880, tam=30, cor=TINTA, peso=700))
    rs.append(rot(750, y + 60, x, w=880, tam=24, cor=TINTA))
p.append(icone("t:scale", 630, 478, 56, GLIC))
p.append("</svg>")
rs.append(rot(700, 488, "E o resultado muda o que eu vou fazer? Se não muda, não aplique.", w=960, tam=28, cor=GLIC, peso=700))
rs.append(rot(0, 470, "a soleira", w=420, tam=24, cor=MUDO, alinha="center"))
S.append({"id": "porta", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeira decisão: vale rastrear?", "titulo": "Antes do questionário vem o caminho",
          "fonte": "O fluxo de encaminhamento completo é a próxima aula"})

# 3. cinco filtros e três lentes
p = [svg_abre(1664, 560, "Cinco filtros antes de adotar um instrumento; embaixo, três tipos: rastreio pergunta se vale olhar melhor, gravidade pergunta quanto, monitoramento pergunta se está mudando"), defs(MUDO)]
filtros = ["validado no Brasil?", "que pergunta responde?", "quanto tempo custa?", "corte feito em quem?", "o que muda se der positivo?"]
rs = []
for i, t in enumerate(filtros):
    x = i * 336
    p.append(f'<rect x="{x}" y="0" width="316" height="96" rx="48" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    p.append(f'<circle cx="{x+48}" cy="48" r="30" fill="{AZUL}"/>')
    rs.append(rot(x + 18, 30, str(i + 1), w=60, tam=30, cor=PAPEL, peso=700, alinha="center"))
    rs.append(rot(x + 90, 18, t, w=216, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(seta(832, 110, 832, 170, MUDO, "m0", esp=4))
lentes = [("t:zoom-question", "Rastreio", "“vale olhar melhor?”", "t:photo", "fotografia", GLIC, GLIC_T),
          ("t:gauge", "Gravidade", "“quanto?”", "t:photo", "fotografia", FOSF, FOSF_T),
          ("t:chart-line", "Monitoramento", "“está mudando?”", "t:movie", "filme: só vale repetido", OXID, OXID_T)]
for i, (ic, t, perg, ic2, modo, c, ct) in enumerate(lentes):
    x = i * 564
    p.append(caixa(x, 190, 536, 360, c, ct, esp=4, rx=20))
    p.append(icone(ic, x + 30, 220, 100, c))
    p.append(icone(ic2, x + 40, 440, 70, c))
    rs.append(rot(x + 150, 230, t, w=370, tam=38, cor=c, peso=700, serif=True))
    rs.append(rot(x + 150, 300, perg, w=370, tam=30, cor=TINTA, peso=600))
    rs.append(rot(x + 130, 458, modo, w=390, tam=26, cor=TINTA))
p.append("</svg>")
S.append({"id": "lentes", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Segunda decisão: qual instrumento", "titulo": "Cada instrumento responde a uma pergunta só",
          "fonte": "Entre dois que respondem a mesma pergunta, o mais curto: é o que chega respondido até o fim"})

# 4. as duas réguas
px = 1080 / 27
X0 = 560
p = [svg_abre(1664, 540, "Filtro de duas perguntas; régua de depressão de 0 a 27 com marcas em 5, 10, 15 e 20; régua de ansiedade de 0 a 21 com marcas em 5, 10 e 15; corte de 10 destacado nas duas"), defs(TINTA)]
p.append(f'<path d="M0 60 H400 L270 250 H130 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(seta(200, 256, 200, 330, TINTA, "m0"))
p.append(f'<rect x="40" y="340" width="320" height="90" rx="45" fill="{AZUL}"/>')
faixas = [(0, 5, "#E6E3DA"), (5, 10, GLIC_T), (10, 15, "#E9C88A"), (15, 20, "#E3A89F"), (20, 27, FOSF)]
rs = [rot(0, 0, "Filtro", w=400, tam=30, cor=AZUL, peso=700, alinha="center", serif=True),
      rot(20, 90, "humor deprimido", w=360, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(20, 136, "perda de interesse", w=360, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(40, 362, "3 ou mais → aplicar completo", w=320, tam=24, cor=PAPEL, peso=700, alinha="center"),
      rot(0, 450, "sens. 83% · espec. 92%", w=400, tam=24, cor=MUDO, alinha="center")]
for k, (y, maxv, marcas, nome, se) in enumerate([(90, 27, [5, 10, 15, 20], "Depressão · 9 itens · 0 a 27", "corte 10: sens. 88% · espec. 88%"),
                                                  (330, 21, [5, 10, 15], "Ansiedade · 7 itens · 0 a 21", "corte 10: sens. 89% · espec. 82%")]):
    for a, b, c in faixas:
        if a >= maxv:
            continue
        b = min(b, maxv)
        p.append(f'<rect x="{X0 + a*px:.0f}" y="{y}" width="{(b-a)*px:.0f}" height="70" fill="{c}"/>')
    p.append(f'<rect x="{X0}" y="{y}" width="{maxv*px:.0f}" height="70" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    for m in [0] + marcas + [maxv]:
        p.append(f'<line x1="{X0 + m*px:.0f}" y1="{y+70}" x2="{X0 + m*px:.0f}" y2="{y+86}" stroke="{TINTA}" stroke-width="3"/>')
    p.append(f'<line x1="{X0 + 10*px:.0f}" y1="{y-16}" x2="{X0 + 10*px:.0f}" y2="{y+86}" stroke="{TINTA}" stroke-width="6"/>')
    rs.append(rot(X0, y - 58, nome, w=520, tam=30, cor=TINTA, peso=700))
    for m in [0] + marcas + [maxv]:
        rs.append(rot(X0 + m * px - 30, y + 92, str(m), w=60, tam=26 if m == 10 else 24, cor=TINTA if m == 10 else MUDO, peso=700 if m == 10 else 400, alinha="center"))
    rs.append(rot(X0 + 1080 - 560, y - 56, se, w=560, tam=26, cor=TINTA, peso=600, alinha="right"))
p.append("</svg>")
S.append({"id": "reguas", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os dois instrumentos gerais", "titulo": "Duas perguntas filtram, nove medem",
          "fonte": "Estudos originais em atenção primária, 2001, 2003 e 2006 · Pelotas, 447 adultos: corte acima de 9, sens. 77,5% · espec. 86,7%"})

# 5. os itens do central
itens = [("sono", 3, "c"), ("energia", 3, "c"), ("apetite", 3, "c"), ("concentração", 3, "c"), ("lentidão ou agitação", 1, "c"),
         ("humor deprimido", 0, "h"), ("perda de interesse", 0, "h"), ("autoimagem", 0, "h")]
p = [svg_abre(1664, 540, "Os nove itens do central: sono, energia, apetite e concentração com três pontos, lentidão com um, humor, interesse e autoimagem com zero; o total 13 em cinza; o item sobre pensamentos de morte separado numa moldura vermelha")]
L, BW, RH = 400, 190, 50
rs = []
for i, (t, v, g) in enumerate(itens):
    y = i * RH
    c = GLIC if g == "c" else AZUL
    p.append(f'<rect x="{L}" y="{y+8}" width="{3*BW}" height="34" rx="6" fill="#EEEBE3"/>')
    if v:
        p.append(f'<rect x="{L}" y="{y+8}" width="{v*BW}" height="34" rx="6" fill="{c}"/>')
    else:
        p.append(f'<circle cx="{L+12}" cy="{y+25}" r="9" fill="{c}"/>')
    rs.append(rot(0, y + 10, t, w=380, tam=26, cor=TINTA, peso=600, alinha="right"))
p.append(f'<rect x="{L-420}" y="{8*RH+26}" width="{3*BW+440}" height="64" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="5"/>')
p.append(f'<circle cx="{L+12}" cy="{8*RH+58}" r="9" fill="{FOSF}"/>')
p.append(f'<path d="M1000 10 h20 v230 h-20" fill="none" stroke="{GLIC}" stroke-width="4"/>')
p.append(f'<path d="M1000 260 h20 v130 h-20" fill="none" stroke="{AZUL}" stroke-width="4"/>')
p.append("</svg>")
rs += [rot(0, 8 * RH + 42, "pensamentos de morte", w=380, tam=26, cor=FOSF, peso=700, alinha="right"),
       rot(1040, 70, "itens que um bloco pesado de treino também produz", w=600, tam=28, cor=GLIC, peso=700),
       rot(1040, 290, "o núcleo do humor", w=600, tam=28, cor=AZUL, peso=700),
       rot(1040, 8 * RH + 36, "lido antes do total, sempre", w=600, tam=28, cor=FOSF, peso=700),
       rot(1340, 150, "13", w=280, tam=96, cor="#B9BEC3", peso=700, alinha="center", serif=True),
       rot(1340, 270, "o total, por último", w=280, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "itens", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceira decisão: como ler", "titulo": "Leia os itens antes do total",
          "fonte": "Perfil ilustrativo, sem valores medidos · o inverso também acontece: quem aprendeu a suportar pontua baixo estando mal"})

# 6. a escada olímpica
p = [svg_abre(1664, 560, "Escada de três degraus: triagem de dez perguntas com corte 17; seis instrumentos específicos; avaliação clínica. Ao lado, o entorno do atleta com a ferramenta de reconhecimento")]
p.append(f'<path d="M0 560 V400 H540 V260 H1100 V120 H1664 V560 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
p.append(f'<rect x="0" y="400" width="540" height="160" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
p.append(f'<rect x="1100" y="120" width="564" height="440" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
esp6 = [("t:mood-nervous", "ansiedade"), ("t:mood-sad", "depressão"), ("t:zzz", "sono"),
        ("t:glass-full", "álcool"), ("t:pill", "substâncias"), ("t:salad", "alimentação")]
rs = []
for i, (ic, t) in enumerate(esp6):
    x = 560 + (i % 3) * 176
    y = 290 + (i // 3) * 130
    p.append(icone(ic, x + 58, y, 60, AZUL))
    rs.append(rot(x, y + 66, t, w=176, tam=24, cor=TINTA, peso=600, alinha="center"))
p.append(icone("h:doctor", 1150, 170, 120, OXID))
p.append(icone("t:users", 40, 60, 110, MUDO))
p.append(icone("t:eye", 170, 80, 70, MUDO))
p.append("</svg>")
rs += [rot(20, 420, "1 · Triagem", w=500, tam=34, cor=GLIC, peso=700, serif=True),
       rot(20, 470, "10 perguntas, de 10 a 50 pontos · 17 ou mais: risco aumentado", w=500, tam=24, cor=TINTA, lh=1.3),
       rot(560, 200, "2 · Seis instrumentos específicos", w=520, tam=32, cor=AZUL, peso=700, serif=True),
       rot(1290, 180, "3 · Avaliação clínica", w=360, tam=34, cor=OXID, peso=700, serif=True),
       rot(1130, 310, "médico do esporte ou profissional de saúde mental; aqui, e só aqui, o diagnóstico", w=500, tam=26, cor=TINTA, lh=1.35),
       rot(260, 70, "Reconhecimento", w=260, tam=28, cor=TINTA, peso=700),
       rot(260, 112, "para o atleta e o entorno: colegas, família, treinador", w=280, tam=24, cor=MUDO, lh=1.3)]
S.append({"id": "escada", "tipo": "diagrama", "h": 560, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A ferramenta do esporte", "titulo": "A ferramenta olímpica sobe em degraus e termina num clínico",
          "fonte": "Comitê Olímpico Internacional, 2021 · atletas de elite a partir de 16 anos · triagem com três domínios: autorregulação, desempenho, enfrentamento externo"})

# 7. cem positivos
p = [svg_abre(1664, 520, "Duas grades de cem positivos. Com 5% de prevalência, 28 são verdadeiros e 72 falsos. Com 30% de prevalência, 76 são verdadeiros e 24 falsos")]
rs = []
for k, (x0, verd, prev, cont, c, ct) in enumerate([(0, 28, "prevalência 5%", "44 reais em 158 positivos", GLIC, GLIC_T),
                                                    (850, 76, "prevalência 30%", "264 reais em 348 positivos", OXID, OXID_T)]):
    for i in range(100):
        col, lin = i % 10, i // 10
        p.append(f'<rect x="{x0 + col*42}" y="{60 + lin*42}" width="36" height="36" rx="6" fill="{c if i < verd else ct}"/>')
    rs.append(rot(x0, 0, prev, w=412, tam=30, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x0 + 440, 120, str(verd), w=360, tam=120, cor=c, peso=700, serif=True))
    rs.append(rot(x0 + 440, 280, "de cada 100 positivos são reais", w=340, tam=28, cor=TINTA, peso=600, lh=1.3))
    rs.append(rot(x0 + 440, 380, cont, w=340, tam=24, cor=MUDO, lh=1.3))
p.append("</svg>")
S.append({"id": "positivos", "tipo": "diagrama", "h": 520, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O valor de um positivo", "titulo": "O mesmo escore vale mais onde o risco é maior",
          "fonte": "Esquema, sem valores medidos · conta ilustrativa com sensibilidade e especificidade de 88% do estudo original e prevalências hipotéticas"})

# 8. a temporada
p = [svg_abre(1664, 540, "A temporada de um atleta numa linha do tempo: aplicação na entrada, nos momentos de risco e a cada três a seis meses; embaixo, a frase de abertura em três partes")]
Y = 170
p.append(f'<line x1="40" y1="{Y}" x2="1624" y2="{Y}" stroke="{TINTA}" stroke-width="5"/>')
p.append(f'<circle cx="70" cy="{Y}" r="30" fill="{OXID}"/>')
for x in [560, 1100, 1600]:
    p.append(f'<circle cx="{x}" cy="{Y}" r="12" fill="{AZUL}"/>')
riscos = [("h:bandaged", "lesão", 230), ("t:hourglass", "afastamento", 460), ("t:door-exit", "corte ou transição", 730),
          ("t:trending-down", "queda sem explicação", 1030), ("t:message-circle", "alguém avisa", 1340)]
rs = [rot(0, Y + 44, "entrada", w=140, tam=26, cor=OXID, peso=700, alinha="center"),
      rot(360, Y + 30, "a cada 3 a 6 meses, em quem você acompanha", w=900, tam=24, cor=AZUL, peso=600, alinha="center")]
for ic, t, x in riscos:
    p.append(f'<line x1="{x}" y1="{Y-60}" x2="{x}" y2="{Y}" stroke="{FOSF}" stroke-width="4"/>')
    p.append(f'<circle cx="{x}" cy="{Y}" r="16" fill="{FOSF}"/>')
    p.append(icone(ic, x - 36, 20, 72, FOSF))
    rs.append(rot(x + 42, 30, t, w=180, tam=24, cor=TINTA, peso=600))
p.append(f'<path d="M40 290 H1624 V470 H300 L240 520 L240 470 H40 Z" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
for i, (t, c) in enumerate([("“faço com todo mundo”", AZUL), ("“afeta o treino”", OXID), ("“não é para te tirar de nada”", GLIC)]):
    x = 70 + i * 520
    p.append(f'<rect x="{x}" y="320" width="490" height="120" rx="14" fill="{[AZUL_T, OXID_T, GLIC_T][i]}"/>')
    rs.append(rot(x, 340, t, w=490, tam=30, cor=c, peso=700, alinha="center", serif=True))
    rs.append(rot(x, 392, ["tira a sensação de ter sido escolhido", "entra pela porta que interessa", "desarma o medo de perder a vaga"][i], w=490, tam=24, cor=TINTA, alinha="center"))
p.append("</svg>")
S.append({"id": "temporada", "tipo": "diagrama", "h": 540, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quarta decisão: quando e como", "titulo": "O momento e a frase decidem a resposta",
          "destaque": "Regra de equipe: o resultado individual não vai para o técnico. Combine antes, e cumpra.", "destaque_cor": "verm"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Rastreio e instrumentos validados", "titulo": "“Ele está deprimido?” ainda não tem resposta",
          "regras": ["Antes do questionário, o caminho",
                     "Os itens antes do total, e o último item antes de todos",
                     "O positivo vale o risco de quem você rastreia"],
          "cards": [{"ic": "t:users", "t": "Quem treina e reabilita", "x": "Reconhece, apresenta o instrumento do jeito certo, encaminha."},
                    {"ic": "h:doctor", "t": "Médico", "x": "Aplica, lê item a item, conduz o que é clínico."},
                    {"ic": "h:psychology", "t": "Psicologia e psiquiatria", "x": "Fazem a avaliação que fecha o diagnóstico."}]})

spec = {"arquivo": "aulas/MOD10/10-04-rastreio-e-instrumentos-validados.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Rastreio e instrumentos validados", "subtitulo": "Quatro decisões antes do número",
        "nota_capa": "Entra por um central de vôlei com treze pontos na pré-temporada.",
        "secoes": {"ponte": ["Se vale rastrear.", "capa"], "lentes": ["Qual instrumento.", "lentes"],
                   "itens": ["Como ler o resultado.", "itens"], "temporada": ["Quando e como aplicar.", "temporada"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-04.json"), "w"), ensure_ascii=False, indent=1)
print("10-04.json:", len(S), "slides")
