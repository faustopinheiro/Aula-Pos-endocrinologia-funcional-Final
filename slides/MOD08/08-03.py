"""Spec do deck 8.3. Gera 08-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "bomba", "tipo": "frase", "fundo": "tinta", "eyebrow": "O carbono-14 dos testes nucleares como data de fabricação",
          "frase": "O miolo do tendão de Aquiles adulto tem o colágeno da adolescência.",
          "apoio": "28 tendões de pessoas nascidas entre 1945 e 1983: o carbono do miolo correspondia aos primeiros 17 anos de vida. No músculo das mesmas pessoas, renovação contínua."})

S.append({"id": "desmontar", "tipo": "duas", "eyebrow": "Antes que o número vire mito", "titulo": "O tendão muda devagar, e de outro jeito",
          "esq": {"t": "O que significa", "cor": "tinta",
                  "itens": ["o núcleo de colágeno não é trocado", "explica a cicatrização ruim", "explica tendinopatia de meses"]},
          "dir": {"t": "O que não significa", "cor": "petr",
                  "itens": ["que o tendão não responde a treino", "a resposta muda o material e a periferia", "a dose e a paciência são outras"]},
          "destaque_cor": "tinta", "fonte": "FASEB J 2013"})

p = [svg_abre(1664, 260, "Três etapas da mecanotransdução: a carga deforma a célula, a célula avisa as vizinhas, as células produzem proteína")]
p.append("<defs>" + seta_marker("mt", MUDO) + "</defs>")
for i, c in enumerate([AZUL, GLIC, OXID]):
    x = 150 + i * 560
    p.append(f'<ellipse cx="{x + 120}" cy="120" rx="{120 if i else 150}" ry="{70 if i else 50}" fill="{c}" fill-opacity="0.18" stroke="{c}" stroke-width="4"/>')
p.append(f'<line x1="10" y1="120" x2="100" y2="120" stroke="{AZUL}" stroke-width="5" marker-end="url(#mt)"/>')
p.append(f'<line x1="530" y1="120" x2="420" y2="120" stroke="{AZUL}" stroke-width="5" marker-end="url(#mt)"/>')
for dx in (-60, 0, 60):
    p.append(f'<circle cx="{830 + dx}" cy="120" r="14" fill="{GLIC}"/>')
for dx in (-80, -30, 20, 70):
    p.append(f'<rect x="{1390 + dx}" y="100" width="36" height="40" rx="6" fill="{OXID}"/>')
p.append(f'<line x1="560" y1="120" x2="660" y2="120" stroke="{MUDO}" stroke-width="3" stroke-dasharray="8 6"/>')
p.append(f'<line x1="1000" y1="120" x2="1220" y2="120" stroke="{MUDO}" stroke-width="3" marker-end="url(#mt)"/>')
p.append("</svg>")
rs = [rot(100, 200, "1 · acoplamento: a carga deforma a célula", w=440, tam=24, cor=AZUL, peso=700, alinha="center"),
      rot(610, 200, "2 · a célula avisa as vizinhas", w=440, tam=24, cor=GLIC, peso=700, alinha="center"),
      rot(1170, 200, "3 · resposta: fabricar proteína na direção da carga", w=470, tam=24, cor=OXID, peso=700, alinha="center")]
S.append({"id": "passos", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Mecanoterapia", "titulo": "Como a carga vira reparo, em três passos",
          "destaque": "Sem carga, não há sinal. O exercício de reabilitação é o sinal que manda o tecido se refazer.",
          "destaque_cor": "tinta", "fonte": "Esquema · Br J Sports Med 2009"})

S.append({"id": "musculo", "tipo": "numeros", "eyebrow": "O relógio do músculo", "titulo": "Uma sessão de força, quase dois dias de sinal",
          "numeros": [{"n": "+112%", "x": "síntese de proteína 3 horas depois", "cor": "petr"},
                      {"n": "+65%", "x": "24 horas depois", "cor": "petr"},
                      {"n": "+34%", "x": "48 horas depois", "cor": "petr"}],
          "destaque": "A degradação também sobe. Em jejum, o balanço seguiu negativo, só menos que em repouso: o sinal vem da carga, a matéria-prima vem da comida.",
          "destaque_cor": "ambar", "fonte": "8 destreinados, 8 × 8 a 80% de 1RM · Am J Physiol 1997"})

p = [svg_abre(1664, 300, "Esquema: depois da carga, a degradação de colágeno do tendão sobe e cai antes; a síntese sobe depois, com pico perto de 24 horas, e segue elevada por cerca de três dias")]
p.append(f'<line x1="80" y1="260" x2="1600" y2="260" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="80" y1="30" x2="80" y2="260" stroke="{MUDO}" stroke-width="3"/>')
X = lambda h: 80 + h / 84 * 1500
p.append(f'<path d="M{X(0)},250 C{X(4)},120 {X(8)},70 {X(14)},90 C{X(22)},120 {X(30)},230 {X(48)},250 L{X(84)},250" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M{X(0)},250 C{X(10)},200 {X(18)},60 {X(24)},55 C{X(36)},60 {X(60)},140 {X(78)},245" fill="none" stroke="{OXID}" stroke-width="6"/>')
for h in (24, 48, 72):
    p.append(f'<line x1="{X(h)}" y1="255" x2="{X(h)}" y2="265" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(X(10) - 80, 30, "degradação: pico mais cedo", w=320, tam=24, cor=FOSF, peso=700),
      rot(X(30), 12, "síntese: pico perto de 24 h, elevada por cerca de 3 dias", w=780, tam=24, cor=OXID, peso=700),
      rot(X(24) - 60, 270, "24 h", w=120, tam=22, cor=MUDO, alinha="center"),
      rot(X(48) - 60, 270, "48 h", w=120, tam=22, cor=MUDO, alinha="center"),
      rot(X(72) - 60, 270, "72 h", w=120, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "tendao", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O relógio do tendão", "titulo": "Primeiro degrada, depois constrói",
          "destaque": "Carga pesada de novo antes de o saldo virar, semana após semana, e o tendão vive na fase de perda.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Nat Rev Rheumatol 2010"})

S.append({"id": "magnitude", "tipo": "numeros", "eyebrow": "O que faz o tendão se adaptar", "titulo": "Magnitude e tempo",
          "numeros": [{"n": "0,90", "x": "efeito na rigidez com mais de 70% da contração máxima", "cor": "petr"},
                      {"n": "0,04", "x": "efeito com intensidade menor", "cor": "verm"},
                      {"n": "> 12 sem", "x": "intervenções mais longas funcionaram melhor", "cor": "tinta"}],
          "destaque": "O tipo de contração pesou menos que a intensidade. Na fase de construção: carga alta, lenta e controlada, por meses.",
          "destaque_cor": "tinta", "fonte": "Metanálise em tendões saudáveis · Sports Med Open 2015"})

p = [svg_abre(1664, 280, "A mesma carga diária de 360 ciclos aplicada num bloco só e dividida em quatro e em seis blocos com pausas")]
linhas_ = [(1, 360), (4, 90), (6, 60)]
for j, (n, c) in enumerate(linhas_):
    y = 30 + j * 85
    larg = 1100 / n - (24 if n > 1 else 0)
    for k in range(n):
        p.append(f'<rect x="{400 + k * (1100 / n)}" y="{y}" width="{larg:.0f}" height="46" rx="6" fill="{[MUDO, OXID, OXID][j]}" fill-opacity="{0.45 if j == 0 else 0.8}"/>')
p.append("</svg>")
rs = [rot(0, 38, "1 bloco de 360", w=380, tam=24, cor=MUDO, peso=700),
      rot(0, 123, "4 blocos de 90, com pausa", w=380, tam=24, cor=OXID, peso=700),
      rot(0, 208, "6 blocos de 60, com pausa", w=380, tam=24, cor=OXID, peso=700)]
S.append({"id": "osso", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O relógio do osso", "titulo": "A mesma carga rende mais quando é dividida",
          "destaque": "O osso satura com repetição e recupera a sensibilidade com pausa. Na prática: poucos saltos, em blocos curtos, distribuídos.",
          "destaque_cor": "tinta", "fonte": "Em ratos: blocos divididos com mais formação óssea · J Bone Miner Res 2000"})

S.append({"id": "desuso", "tipo": "numeros", "eyebrow": "O custo de tirar o sinal", "titulo": "Perna engessada em homens jovens e saudáveis",
          "numeros": [{"n": "−3,5%", "x": "área do quadríceps em 5 dias", "cor": "verm"},
                      {"n": "−9%", "x": "força em 5 dias", "cor": "verm"},
                      {"n": "−23%", "x": "força em 14 dias", "cor": "verm"}],
          "destaque": "Proteger o tecido lesionado nos primeiros dias é necessário. Imobilizar o resto do corpo junto não é.",
          "destaque_cor": "tinta", "fonte": "Acta Physiol 2014"})

S.append({"id": "repouso", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Repouso não é neutro. O tecido lê a ausência de carga como uma ordem.",
          "apoio": "Proteger é tirar a carga que machuca. Não é tirar toda a carga."})

S.append({"id": "relogios", "tipo": "tabela", "eyebrow": "Quatro relógios, lado a lado", "titulo": "O prazo é do tecido, não da dor",
          "cab": ["Tecido", "Como responde"],
          "larguras": [24, 76],
          "linhas": [["Músculo", "horas; síntese elevada por 1 a 2 dias; ganhos em semanas"],
                     ["Tendão", "colágeno em dias, saldo depois; miolo não se renova; rigidez em mais de 12 semanas"],
                     ["Osso", "carga dinâmica; satura com repetição; volta com pausa; meses"],
                     ["Ligamento e enxerto", "lentos como o tendão; a biologia marca o piso de tempo"]],
          "destaque": "Duas lesões com a mesma dor podem ter prazos muito diferentes.",
          "destaque_cor": "tinta"})

S.append({"id": "pratica", "tipo": "cards", "por_linha": 5, "eyebrow": "Na segunda-feira", "titulo": "Cinco traduções para a prescrição",
          "cards": [{"t": "Carga é sinal", "x": "sem progressão, é espera", "cor": "petr"},
                    {"t": "Magnitude", "x": "principalmente no tendão", "cor": "petr"},
                    {"t": "Espaçamento", "x": "tendão alterna; osso pausa", "cor": "ambar"},
                    {"t": "Tempo", "x": "semanas no músculo, meses no tendão", "cor": "ambar"},
                    {"t": "Dor não mede", "x": "informa tolerância, não adaptação", "cor": "verm"}],
          "destaque": "Avisar no começo que o tendão leva meses evita o abandono no segundo mês.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Mecanotransdução", "titulo": "Sem carga, não há sinal; sem sinal, não há reparo",
          "regras": ["Cada tecido tem o seu relógio",
                     "Magnitude, espaçamento e tempo, por tecido",
                     "Repouso não é neutro"],
          "cards": [{"t": "Quem prescreve repouso", "x": "Diz por quanto tempo e para qual tecido."},
                    {"t": "Fisioterapia e preparação", "x": "Dosam a carga pelo relógio do tecido."},
                    {"t": "Nutrição", "x": "Garante a matéria-prima do reparo."}],
          "quem": "Próxima aula: progressão de carga em tecido em cicatrização."})

spec = {"arquivo": "aulas/MOD08/08-03-mecanotransducao.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Mecanotransdução", "subtitulo": "Como a carga vira reparo, em números",
        "nota_capa": "Entra pelo carbono-14 dos testes nucleares no tendão de Aquiles.",
        "secoes": {"bomba": ["O tendão que não se renova e o mecanismo.", "capa"],
                   "musculo": ["Os relógios do músculo, do tendão e do osso.", "musculo"],
                   "desuso": ["O custo do repouso.", "desuso"],
                   "relogios": ["Os quatro relógios e a prática.", "relogios"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-03.json"), "w"), ensure_ascii=False, indent=1)
print("08-03.json:", len(S), "slides")
