"""Spec do deck 14.3. Gera 14-03.json ao lado deste arquivo."""
from _base import *

S = []

ATEND = [("pronto-socorro", "tontura na pesagem: soro e alta", FOSF),
         ("nutricionista", "plano para manter a categoria", OXID),
         ("fisioterapeuta", "dor lombar: exercícios", AZUL),
         ("psicóloga", "ansiedade antes das lutas: respiração", GLIC),
         ("escola", "notas caindo: reforço", MUDO)]

# 1. o tatame
p = [svg_abre(1664, 440, "Judoca de treze anos na balança da pesagem. Cinco atendimentos em quatro meses, todos com visto: pronto-socorro, tontura na pesagem, hidratação na veia e alta; nutricionista, plano para manter a categoria; fisioterapeuta, dor lombar; psicóloga, ansiedade antes das lutas; escola, notas caindo. A pergunta que ninguém escreveu: por que um menino de treze anos corta peso quatro vezes por ano? Perfil típico")]
rs = []
p.append(menino(150, 300, 220, TINTA))
p.append(f'<rect x="60" y="300" width="180" height="40" rx="8" fill="{MUDO}"/>')
p.append(f'<rect x="120" y="310" width="60" height="20" rx="4" fill="{PAPEL}"/>')
rs += [rot(0, 350, "13 anos · perfil típico", w=300, tam=20, cor=MUDO, peso=700, alinha="center")]
for j, (q, c_, c) in enumerate(ATEND):
    y = j * 72
    p.append(caixa(340, y, 640, 60, c, CARTAO, esp=3, rx=12))
    p.append(f'<circle cx="368" cy="{y + 30}" r="14" fill="{OXID}"/>')
    p.append(f'<path d="M 361 {y + 30} L 366 {y + 36} L 376 {y + 24}" stroke="{PAPEL}" stroke-width="4" fill="none"/>')
    rs += [rot(396, y + 16, q, w=200, tam=22, cor=c, peso=700), rot(600, y + 16, c_, w=370, tam=20, cor=TINTA, peso=700)]
p.append(caixa(1040, 40, 624, 300, FOSF, FOSF_T, esp=4, rx=20))
rs += [rot(1064, 60, "A pergunta que ninguém escreveu", w=576, tam=22, cor=MUDO, peso=700),
       rot(1064, 110, "“Por que um menino de treze anos corta peso quatro vezes por ano?”", w=576, tam=32, cor=FOSF, peso=700, serif=True, lh=1.25),
       rot(1040, 380, "cinco atendimentos em quatro meses", w=624, tam=22, cor=TINTA, peso=700, alinha="center")]
diagrama(S, "tatame", 440, p, rs, eyebrow="Judô competitivo, um menino de treze anos", titulo="Cinco atendimentos certos, e ninguém perguntou pelo peso")

# 2. o erro
p = [svg_abre(1664, 400, "Cinco caixas com visto e a conduta de cada atendimento; embaixo, a soma das cinco: um ponto de interrogação. Cinco condutas certas não somam um plano")]
rs = []
for j, (q, c_, c) in enumerate(ATEND):
    x = j * 336
    p.append(caixa(x, 0, 312, 150, c, CARTAO, esp=3, rx=14))
    p.append(f'<circle cx="{x + 36}" cy="36" r="18" fill="{OXID}"/>')
    p.append(f'<path d="M {x + 27} 36 L {x + 34} 44 L {x + 46} 28" stroke="{PAPEL}" stroke-width="4" fill="none"/>')
    rs += [rot(x + 64, 22, q, w=236, tam=22, cor=c, peso=700), rot(x + 20, 70, c_, w=272, tam=20, cor=TINTA, peso=700, lh=1.2)]
    p.append(f'<line x1="{x + 156}" y1="150" x2="832" y2="230" stroke="{GRADE}" stroke-width="3"/>')
p.append(f'<circle cx="832" cy="290" r="60" fill="{FOSF}"/>')
rs += [rot(782, 252, "?", w=100, tam=64, cor=PAPEL, peso=700, serif=True, alinha="center"),
       rot(0, 362, "Cinco condutas certas não somam um plano.", w=1664, tam=30, cor=FOSF, peso=700, serif=True, alinha="center")]
diagrama(S, "erro", 400, p, rs, eyebrow="O erro", titulo="Cada profissional teve razão sozinho")

# 3. o padrão no judô brasileiro
p = [svg_abre(1664, 440, "822 judocas brasileiros: 86% já perderam peso rápido para competir. Idade média em que começaram: 12,6 anos. Métodos relatados: pular refeições, restringir líquido, treinar com roupa plástica. Levantamento de 2010")]
rs = []
for k in range(100):
    cx, cy = 20 + (k % 20) * 34, 30 + (k // 20) * 34
    p.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{FOSF if k < 86 else GRADE}"/>')
rs += [rot(0, 200, "86%", w=200, tam=64, cor=FOSF, peso=700, serif=True),
       rot(200, 216, "já perderam peso rápido para competir", w=480, tam=24, cor=TINTA, peso=700, lh=1.2),
       rot(0, 300, "822 judocas competitivos · cada ponto, 1% · levantamento brasileiro de 2010", w=700, tam=20, cor=MUDO, peso=700, lh=1.2)]
X0, X1, Y = 800, 1640, 120
def px(v):
    return X0 + (v - 8) / 12 * (X1 - X0)
p.append(f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="{TINTA}" stroke-width="4"/>')
for v in (8, 10, 12, 14, 16, 18, 20):
    p.append(f'<line x1="{px(v):.0f}" y1="{Y - 10}" x2="{px(v):.0f}" y2="{Y + 10}" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(px(v) - 30, Y + 18, str(v), w=60, tam=20, cor=MUDO, peso=700, alinha="center"))
p.append(f'<circle cx="{px(12.6):.0f}" cy="{Y}" r="18" fill="{FOSF}"/>')
rs += [rot(px(12.6) - 150, Y - 96, "12,6 anos: início médio do corte", w=300, tam=24, cor=FOSF, peso=700, alinha="center"),
       rot(X1 - 200, Y + 50, "idade em anos", w=200, tam=20, cor=MUDO, alinha="right")]
p.append(caixa(X0, 230, X1 - X0 + 24, 210, MUDO, CARTAO, esp=2, rx=16))
rs.append(rot(X0 + 24, 250, "Métodos relatados", w=780, tam=24, cor=TINTA, peso=700, serif=True))
for j, t in enumerate(["pular refeições", "restringir líquido", "treinar com roupa plástica"]):
    rs.append(rot(X0 + 24 + j * 280, 320, t, w=260, tam=24, cor=FOSF, peso=700, lh=1.2))
diagrama(S, "padrao", 440, p, rs, eyebrow="O tamanho do padrão", titulo="No judô brasileiro, o corte de peso começa por volta dos doze anos",
         fonte="Med Sci Sports Exerc 2010")

# 4. a árvore
p = [svg_abre(1664, 460, "Árvore. Nos galhos, cinco sintomas: tontura, peso, dor lombar, ansiedade, notas, cada um com o profissional que o tratou. No tronco, a raiz comum: competir o ano inteiro; categoria abaixo do peso de crescimento; ninguém responde pelo conjunto")]
rs = []
p.append(f'<path d="M 790 460 L 790 230 M 874 460 L 874 230" stroke="{TINTA}" stroke-width="10"/>')
p.append(f'<rect x="790" y="230" width="84" height="230" fill="{MUDO}"/>')
for j, (q, c_, c) in enumerate(ATEND):
    x = 40 + j * 330
    p.append(f'<line x1="832" y1="230" x2="{x + 130}" y2="130" stroke="{TINTA}" stroke-width="6"/>')
    p.append(f'<circle cx="{x + 130}" cy="100" r="32" fill="{c}"/>')
    rs += [rot(x, 0, ["tontura", "peso", "dor lombar", "ansiedade", "notas"][j], w=260, tam=22, cor=c, peso=700, alinha="center"),
           rot(x, 30, q, w=260, tam=20, cor=MUDO, peso=700, alinha="center")]
for j, t in enumerate(["competir o ano inteiro", "categoria abaixo do peso de crescimento", "ninguém responde pelo conjunto"]):
    y = 270 + j * 62
    rs.append(rot(900, y, t, w=700, tam=26, cor=FOSF if j == 2 else TINTA, peso=700, serif=True))
rs += [rot(400, 300, "a raiz", w=360, tam=28, cor=FOSF, peso=700, serif=True, alinha="right"),
       rot(400, 344, "não é queixa de ninguém", w=360, tam=22, cor=MUDO, peso=700, alinha="right")]
diagrama(S, "arvore", 460, p, rs, eyebrow="Por que o erro acontece", titulo="Cada um tratou o galho que viu, e a raiz não era queixa de ninguém")

# 5. quando a conduta certa alimenta a raiz
p = [svg_abre(1664, 450, "Três condutas certas que viraram parte do problema. Hidratação na veia e alta: a pesagem seguinte é igual. Plano para manter a categoria: um adolescente em crescimento segurando o peso. Técnicas de respiração: a ansiedade tem data marcada, a pesagem. Cada uma volta para a raiz")]
rs = []
for j, (t, x_, c) in enumerate([("hidratação na veia e alta", "a alta devolveu o menino à mesma pesagem, sem aviso a ninguém", FOSF),
                                ("plano para manter a categoria", "manter a categoria no pico de crescimento é brigar com o crescimento", OXID),
                                ("técnicas de respiração", "a ansiedade tem data marcada: a véspera da pesagem", GLIC)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 300, c, CARTAO, esp=3, rx=18))
    rs += [rot(x + 24, 24, t, w=488, tam=26, cor=c, peso=700, serif=True, lh=1.2),
           rot(x + 24, 120, x_, w=488, tam=24, cor=TINTA, peso=700, lh=1.3)]
    p.append(f'<path d="M {x + 268} 300 Q {x + 268} 370 832 390" stroke="{c}" stroke-width="4" fill="none"{TRACO}/>')
p.append(f'<circle cx="832" cy="392" r="20" fill="{MUDO}"/>')
rs.append(rot(632, 418, "de volta à raiz", w=400, tam=24, cor=MUDO, peso=700, alinha="center"))
diagrama(S, "alimenta", 450, p, rs, eyebrow="Quando a conduta certa alimenta a raiz", titulo="Sem a raiz, a conduta certa passa a sustentar o problema")

# 6. a correção
p = [svg_abre(1664, 460, "Um plano em cinco linhas: uma pessoa coordena; a categoria é decidida em conjunto com a família, olhando o crescimento; calendário com meses fora da competição; linhas que não se cruzam no adolescente: restringir líquido, roupa plástica, sauna, laxante, diurético; a escola entra na conversa")]
rs = []
p.append(caixa(0, 0, 1664, 460, TINTA, CARTAO, esp=3, rx=18))
rs.append(rot(32, 18, "Um plano, não cinco", w=800, tam=30, cor=TINTA, peso=700, serif=True))
for j, (ic, t, c) in enumerate([("t:users", "uma pessoa coordena, de qualquer profissão", AZUL),
                                ("t:scale", "a categoria é decidida em conjunto, com a família, olhando o crescimento", OXID),
                                ("t:calendar", "calendário com meses fora da competição", GLIC),
                                ("t:x", "não entram no plano: restringir líquido, roupa plástica, sauna, laxante, diurético", FOSF),
                                ("t:book", "a escola entra na conversa: as notas são o sinal mais precoce", MUDO)]):
    y = 84 + j * 72
    p.append(f'<line x1="32" y1="{y - 8}" x2="1632" y2="{y - 8}" stroke="{GRADE}" stroke-width="2"/>')
    p.append(icone(ic, 32, y + 4, 44, c))
    rs.append(rot(96, y + 10, t, w=1520, tam=26, cor=TINTA if j != 3 else FOSF, peso=700))
diagrama(S, "correcao", 460, p, rs, eyebrow="A correção", titulo="Os cinco atendimentos viram um plano com cinco linhas")

# 7. a reunião
p = [svg_abre(1664, 440, "Reunião de trinta minutos com o atleta no centro; em volta, pais, técnico, nutricionista, psicóloga e quem coordena. Na mesa, o resumo combinado e a assinatura: o que pode ser compartilhado, com consentimento dos pais e do atleta. Quem percebe o padrão convoca")]
rs = []
CX, CY = 480, 220
p.append(f'<ellipse cx="{CX}" cy="{CY}" rx="260" ry="120" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
p.append(menino(CX, CY + 40, 120, FOSF))
rs.append(rot(CX - 100, CY + 50, "o atleta", w=200, tam=22, cor=FOSF, peso=700, alinha="center"))
for k, t in enumerate(["pais", "técnico", "nutricionista", "psicóloga", "coordenação"]):
    a = math.radians(-160 + k * 70)
    x, y = CX + 360 * math.cos(a), CY + 190 * math.sin(a)
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="24" fill="{TINTA}"/>')
    rs.append(rot(x - 100, y + 28, t, w=200, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(1000, 0, 664, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:clock", 1024, 24, 52, AZUL))
rs += [rot(1092, 34, "trinta minutos", w=548, tam=28, cor=AZUL, peso=700, serif=True),
       rot(1024, 110, "quem percebe o padrão convoca", w=616, tam=26, cor=TINTA, peso=700),
       rot(1024, 200, "o que pode ser compartilhado, e com quem, fica escrito", w=616, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1024, 300, "menor de idade: consentimento dos pais, com o adolescente participando", w=616, tam=24, cor=FOSF, peso=700, lh=1.25)]
diagrama(S, "reuniao", 440, p, rs, eyebrow="Quem convoca", titulo="Quem percebe o padrão primeiro convoca a reunião")

# 8. o nome certo
p = [svg_abre(1664, 420, "Antes: cinco fichas separadas, cada uma com uma queixa resolvida. Depois: uma ficha com o problema no topo, corte de peso repetido em adolescente no pico de crescimento, e cinco contribuições embaixo. A pergunta muda de como bater o peso para se ele deve bater esse peso"), defs(TINTA)]
rs = []
rs.append(rot(0, 0, "Antes", w=600, tam=28, cor=MUDO, peso=700, serif=True))
for j, (q, c_, c) in enumerate(ATEND):
    x, y = (j % 3) * 200, 60 + (j // 3) * 170
    p.append(caixa(x, y, 180, 150, GRADE, CARTAO, esp=2, rx=10))
    rs.append(rot(x + 12, y + 16, q, w=156, tam=20, cor=c, peso=700, lh=1.15))
    rs.append(rot(x + 12, y + 100, "resolvido", w=156, tam=20, cor=MUDO, peso=700))
p.append(seta(640, 200, 740, 200, TINTA, "m0", esp=4))
rs.append(rot(780, 0, "Depois", w=600, tam=28, cor=AZUL, peso=700, serif=True))
p.append(caixa(780, 60, 884, 360, AZUL, CARTAO, esp=3, rx=16))
p.append(f'<rect x="780" y="60" width="884" height="110" rx="16" fill="{AZUL_T}"/>')
rs += [rot(804, 80, "problema: corte de peso repetido em adolescente no pico de crescimento", w=836, tam=26, cor=AZUL, peso=700, serif=True, lh=1.25),
       rot(804, 200, "pronto-socorro · nutrição · fisioterapia · psicologia · escola", w=836, tam=22, cor=TINTA, peso=700),
       rot(804, 280, "não mais “como bater o peso”, e sim “ele deve bater esse peso?”", w=836, tam=26, cor=FOSF, peso=700, serif=True, lh=1.25)]
diagrama(S, "nome", 420, p, rs, eyebrow="O nome certo do problema", titulo="Com o nome certo, a pergunta deixa de ser como bater o peso")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Caso integrado: especialização precoce", "titulo": "Procurar a raiz que não é queixa de ninguém",
          "regras": ["Vários atendimentos em poucos meses: procure a raiz comum",
                     "No pico de crescimento, segurar a categoria é brigar com o crescimento",
                     "Quem percebe o padrão convoca, com o atleta no centro"],
          "cards": [{"ic": "h:doctor", "t": "Medicina e nutrição", "x": "Escrevem o problema com o nome certo e discutem a categoria com o crescimento."},
                    {"ic": "t:users", "t": "Técnico e família", "x": "Decidem calendário e categoria junto com a equipe, e não depois dela."},
                    {"ic": "t:user", "t": "O atleta", "x": "Participa da decisão, porque a balança é dele."}]})

salvar("14-03.json", {"arquivo": "aulas/MOD14/14-03-caso-integrado-adolescente-em-especializacao-precoce.md",
                      "titulo": "Caso integrado 3: adolescente em especialização precoce", "subtitulo": "Cinco condutas certas não somam um plano",
                      "nota_capa": "Entra por um judoca de treze anos que passou por cinco atendimentos em quatro meses.",
                      "secoes": {"tatame": ["O erro.", "capa"], "padrao": ["Por que acontece.", "padrao"],
                                 "correcao": ["A correção.", "correcao"]},
                      "slides": S})
