"""Spec do deck 11.4. Gera 11-04.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a ficha e o mostrador apagado
p = [svg_abre(1664, 480, "Uma ficha de anamnese com o campo medicações em uso preenchido com nenhuma, e ao lado o implante no braço, a cartela de pílula e o DIU. À direita, um painel de mostradores clínicos com o mostrador do sangramento apagado. Embaixo: perto de metade das atletas de elite usa contracepção hormonal")]
p.append(caixa(0, 0, 600, 360, TINTA, CARTAO, esp=2, rx=16))
rs = [rot(30, 24, "Ficha de anamnese", w=540, tam=28, cor=TINTA, peso=700, serif=True),
      rot(30, 100, "Medicações em uso:", w=540, tam=26, cor=MUDO),
      rot(30, 150, "nenhuma", w=540, tam=44, cor=FOSF, peso=700, serif=True)]
p.append(f'<line x1="30" y1="230" x2="570" y2="230" stroke="{BORDA}" stroke-width="2"/>')
p.append(f'<rect x="60" y="260" width="140" height="22" rx="11" fill="{GLIC}"/>')
p.append(f'<rect x="250" y="250" width="120" height="80" rx="10" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
for i in range(6):
    p.append(f'<circle cx="{270 + (i % 3) * 40}" cy="{272 + (i // 3) * 36}" r="10" fill="{AZUL}"/>')
p.append(f'<path d="M 470 250 L 470 330 M 440 255 Q 470 240 500 255" stroke="{OXID}" stroke-width="6" fill="none"/>')
rs += [rot(40, 300, "implante", w=180, tam=20, cor=GLIC, alinha="center"), rot(230, 336, "pílula", w=160, tam=20, cor=AZUL, alinha="center"), rot(410, 336, "DIU", w=120, tam=20, cor=OXID, alinha="center")]
mostr = [("energia", OXID), ("peso", OXID), ("sono", OXID), ("osso", OXID), ("humor", OXID), ("sangramento", CINZA)]
for j, (t, c) in enumerate(mostr):
    x, y = 700 + (j % 3) * 330, (j // 3) * 180
    p.append(f'<circle cx="{x + 80}" cy="{y + 80}" r="70" fill="{CARTAO}" stroke="{c}" stroke-width="6"/>')
    if c != CINZA:
        p.append(f'<line x1="{x + 80}" y1="{y + 80}" x2="{x + 120}" y2="{y + 40}" stroke="{c}" stroke-width="6" stroke-linecap="round"/>')
    else:
        p.append(f'<line x1="{x + 30}" y1="{y + 30}" x2="{x + 130}" y2="{y + 130}" stroke="{FOSF}" stroke-width="6"/>')
    rs.append(rot(x + 160, y + 64, t, w=160, tam=24, cor=TINTA if c != CINZA else FOSF, peso=700))
p.append(caixa(0, 390, 1664, 90, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 412, "Perto de metade das atletas de elite usa; sete em cada dez já usaram · e o sangramento sai do painel", w=1624, tam=27, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ficha", 480, p, rs, eyebrow="Uma lutadora de jiu-jitsu, categoria de peso", titulo="Sob contracepção hormonal, o sangramento deixa de ser sinal vital",
         fonte="Levantamento com 430 atletas de elite, Int J Sports Physiol Perform 2018")

# 2. os dois grupos
p = [svg_abre(1664, 470, "Dois blocos. Substitui o eixo: pílula, anel e adesivo combinados, injetável trimestral, com o pulso do hormônio luteinizante apagado e o sangramento de retirada. Convive com o eixo: DIU hormonal, DIU de cobre, barreira, com o pulso ainda batendo. No meio, a pílula só de progestagênio: depende da molécula")]
rs = []
for k, (t, itens, c, f, bate) in enumerate([("Substitui o eixo", ["pílula, anel, adesivo combinados", "injetável trimestral", "sem ovulação; a pausa dá sangramento de retirada"], FOSF, FOSF_T, False),
                                             ("Convive com o eixo", ["DIU hormonal", "DIU de cobre, barreira", "muitas continuam ovulando"], OXID, OXID_T, True)]):
    x = 0 if k == 0 else 1004
    p.append(caixa(x, 0, 660, 470, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 20, t, w=600, tam=34, cor=c, peso=700, serif=True))
    path = f"M {x + 40} 150"
    for i in range(6):
        xx = x + 40 + i * 96
        path += f" L {xx + 40} 150 L {xx + 48} {90 if bate else 146} L {xx + 56} 150 L {xx + 96} 150"
    p.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="5"{"" if bate else TRACO}/>')
    rs.append(rot(x + 40, 170, "pulso de LH batendo" if bate else "pulso de LH calado", w=580, tam=22, cor=c, peso=700))
    for j, it in enumerate(itens):
        rs.append(rot(x + 40, 240 + j * 70, "· " + it, w=600, tam=26, cor=TINTA, peso=600 if j < 2 else 400, lh=1.25))
p.append(caixa(700, 120, 264, 230, GLIC, GLIC_T, esp=3, rx=16))
rs += [rot(712, 140, "Pílula só de progestagênio", w=240, tam=24, cor=GLIC, peso=700, alinha="center", lh=1.2),
       rot(712, 230, "depende da molécula: leia a caixa", w=240, tam=22, cor=TINTA, alinha="center", lh=1.25)]
diagrama(S, "grupos", 470, p, rs, eyebrow="A farmacologia mínima", titulo="Dois grupos: o que cala o eixo e o que convive com ele")

# 3. sangramento parecido, situações opostas
p = [svg_abre(1664, 470, "Dois calendários. No primeiro, uma usuária de pílula combinada sangrando todo mês na pausa, pontual, e embaixo o eixo desligado. No segundo, uma usuária de DIU hormonal sem sangrar há meses, e embaixo o eixo funcionando. Uma faixa entre os dois: o sangramento parecido esconde situações opostas")]
rs = []
for k, (t, sangra, eixo, c) in enumerate([("Pílula combinada", True, "eixo desligado", FOSF), ("DIU hormonal", False, "eixo funcionando", OXID)]):
    x = k * 860
    p.append(caixa(x, 0, 804, 470, c, CARTAO, esp=3, rx=18))
    rs.append(rot(x + 24, 20, t, w=740, tam=32, cor=TINTA, peso=700, serif=True))
    for m in range(3):
        for d in range(28):
            cor = FOSF if (sangra and d >= 24) else BORDA
            p.append(f'<rect x="{x + 30 + d * 26}" y="{90 + m * 56}" width="22" height="44" rx="4" fill="{cor}"/>')
    rs.append(rot(x + 30, 262, "sangra todo mês, na pausa" if sangra else "não sangra há meses", w=740, tam=26, cor=TINTA, peso=600))
    p.append(f'<rect x="{x + 24}" y="320" width="756" height="120" rx="14" fill="{FOSF_T if not k else OXID_T}"/>')
    path = f"M {x + 40} 400"
    for i in range(7):
        xx = x + 40 + i * 100
        path += f" L {xx + 40} 400 L {xx + 48} {358 if k else 396} L {xx + 56} 400 L {xx + 100} 400"
    p.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="5"/>')
    rs.append(rot(x + 520, 326, eixo, w=250, tam=26, cor=c, peso=700, alinha="right"))
diagrama(S, "opostas", 470, p, rs, eyebrow="O que o sangramento passa a esconder", titulo="O sangramento parecido esconde situações opostas",
         destaque="O sangramento de retirada vem pontual com o eixo íntegro ou desligado: é efeito do remédio, não relatório do ovário.", destaque_cor="tinta")

# 4. a pergunta do desempenho
p = [svg_abre(1664, 440, "À esquerda, um gráfico de efeito em esquema com o ponto um pouco à esquerda do zero e o intervalo atravessando o zero: pílula e desempenho, trivial, evidência baixa a muito baixa, só via oral. À direita, a balança da decisão contraceptiva com os pesos que importam: gravidez não planejada, cólica, sangramento intenso, endometriose")]
cx = 420
p.append(f'<line x1="{cx}" y1="20" x2="{cx}" y2="240" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{cx - 260}" y1="130" x2="{cx + 150}" y2="130" stroke="{GLIC}" stroke-width="6" stroke-linecap="round"/>')
p.append(f'<rect x="{cx - 70}" y="112" width="36" height="36" fill="{GLIC}"/>')
rs = [rot(cx - 90, 246, "zero", w=180, tam=22, cor=MUDO, alinha="center"),
      rot(0, 300, "pílula e desempenho: trivial, evidência baixa a muito baixa", w=820, tam=27, cor=GLIC, peso=700, lh=1.25),
      rot(0, 380, "e só via oral: não vale para implante, injetável ou DIU", w=820, tam=24, cor=TINTA)]
p.append(caixa(900, 0, 764, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(924, 20, "O que pesa na decisão dela", w=720, tam=30, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["evitar gravidez não planejada", "cólica e sangramento intenso", "endometriose, acne", "efeito colateral que tira treino"]):
    y = 90 + j * 82
    p.append(f'<rect x="924" y="{y}" width="{620 - j * 60}" height="62" rx="10" fill="{OXID}" opacity="{0.95 - j * 0.15:.2f}"/>')
    rs.append(rot(944, y + 15, t, w=600, tam=25, cor=PAPEL, peso=700))
rs.append(rot(924, 404, "decidida por ela, com a ginecologia", w=720, tam=22, cor=TINTA, peso=600))
diagrama(S, "desempenho", 440, p, rs, eyebrow="A pergunta que vai chegar", titulo="Um efeito trivial não tira nem coloca método em ninguém",
         fonte="Metanálise de 2020 sobre pílula e desempenho · intervalo em esquema")

# 5. a encruzilhada
p = [svg_abre(1664, 480, "Uma encruzilhada com três saídas a partir de: atleta usando método hormonal, com algo que preocupa. Saída 1, manter e trocar os mostradores, em verde. Saída 2, reavaliar o método com a ginecologia, em verde. Saída 3, pílula para trazer a menstruação de volta ou proteger o osso, em vermelho, terminando num alarme apagado"), defs(OXID, FOSF)]
p.append(caixa(0, 160, 400, 160, TINTA, TINTA, esp=0, rx=18))
rs = [rot(20, 182, "Usa método hormonal, e algo preocupa", w=360, tam=28, cor=PAPEL, peso=700, serif=True, lh=1.25)]
saidas = [("Manter e trocar os mostradores", "energia, peso, fratura, humor, desempenho, densitometria", OXID, OXID_T, "m0", "t:gauge"),
          ("Reavaliar o método com a ginecologia", "efeito colateral que tira treino; osso em risco", OXID, OXID_T, "m0", "h:doctor"),
          ("Pílula para trazer a menstruação ou proteger o osso", "parece cuidado; apaga o alarme", FOSF, FOSF_T, "m1", "t:volume-off")]
for j, (t, x_, c, f, mk, ic) in enumerate(saidas):
    y = j * 165
    p.append(seta(404, 240, 560, y + 70, c, mk, esp=5))
    p.append(caixa(580, y, 1084, 150, c, f, esp=3, rx=16))
    p.append(icone(ic, 604, y + 40, 64, c))
    rs += [rot(690, y + 20, t, w=950, tam=28, cor=c, peso=700, serif=True), rot(690, y + 86, x_, w=950, tam=24, cor=TINTA)]
diagrama(S, "encruzilhada", 480, p, rs, eyebrow="A decisão", titulo="Três saídas aparecem na prática; uma delas só parece cuidado")

# 6. por que a pílula não trata
p = [svg_abre(1664, 480, "Três barras de mudança da densidade óssea em doze meses num ensaio com 121 atletas de 14 a 25 anos que não menstruavam ou menstruavam pouco: adesivo de estradiol subindo, pílula combinada sem ganho comparável, sem hormônio. Ao lado, o fígado como um filtro que a pílula atravessa e o adesivo não: o IGF-1 cai")]
base = 300
p.append(f'<line x1="0" y1="{base}" x2="820" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
rs = []
for j, (t, h, c) in enumerate([("adesivo de estradiol", 170, OXID), ("pílula combinada", 40, GLIC), ("sem hormônio", 25, MUDO)]):
    x = 40 + j * 270
    p.append(f'<rect x="{x}" y="{base - h}" width="200" height="{h}" rx="8" fill="{c}"/>')
    rs.append(rot(x - 20, base + 14, t, w=240, tam=24, cor=c, peso=700, alinha="center", lh=1.15))
rs += [rot(0, 0, "Densidade óssea em 12 meses", w=820, tam=28, cor=TINTA, peso=700, serif=True),
       rot(0, 400, "121 atletas de 14 a 25 anos · barras em esquema, só a direção do resultado", w=820, tam=22, cor=MUDO)]
p.append(caixa(900, 0, 764, 480, GLIC, GLIC_T, esp=3, rx=18))
p.append(f'<path d="M 960 200 C 960 120, 1180 90, 1300 130 C 1360 150, 1360 230, 1280 250 C 1160 280, 960 280, 960 200 Z" fill="{FOSF}" opacity="0.75"/>')
p.append(f'<path d="M 1400 120 L 1400 260" stroke="{GLIC}" stroke-width="6"/>')
rs += [rot(924, 20, "A via oral passa pelo fígado", w=720, tam=30, cor=GLIC, peso=700, serif=True),
       rot(1040, 168, "fígado", w=200, tam=26, cor=PAPEL, peso=700, alinha="center"),
       rot(1420, 160, "IGF-1 cai", w=230, tam=28, cor=FOSF, peso=700),
       rot(924, 310, "o adesivo não passa por ali · e nenhum dos dois substitui corrigir a energia", w=720, tam=25, cor=TINTA, lh=1.3)]
diagrama(S, "osso", 480, p, rs, eyebrow="Por que a pílula não trata", titulo="“Ela toma pílula, então o osso está coberto” é uma frase falsa",
         fonte="Ensaio randomizado, Br J Sports Med 2019 · diretriz de amenorreia hipotalâmica funcional, 2017")

# 7. o injetável e o osso
p = [svg_abre(1664, 440, "Uma linha de densidade óssea ao longo dos anos de uso do injetável trimestral, descendo durante o uso e subindo em parte depois da suspensão. Um selo de advertência de bula. Ao lado, um perfil de risco aceso: esporte de peso ou corrida longa, fratura prévia, energia duvidosa")]
x0, x1 = 40, 900
pts = [(0, 200), (1, 230), (2, 255), (3, 270), (3.5, 270), (4.5, 240), (5.5, 225)]
X = lambda a: x0 + a / 5.5 * (x1 - x0)
p.append(f'<rect x="{X(0):.0f}" y="40" width="{X(3.5) - X(0):.0f}" height="300" fill="{FOSF_T}"/>')
p.append(f'<polyline points="{" ".join(f"{X(a):.0f},{y}" for a, y in pts)}" fill="none" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<line x1="{x0}" y1="340" x2="{x1}" y2="340" stroke="{TINTA}" stroke-width="2"/>')
rs = [rot(X(0) + 10, 50, "durante o uso", w=300, tam=24, cor=FOSF, peso=700), rot(X(3.6), 50, "depois de suspender", w=320, tam=24, cor=OXID, peso=700),
      rot(x0, 350, "densidade óssea ao longo dos anos · esquema", w=860, tam=22, cor=MUDO)]
p.append(f'<g transform="rotate(-10 580 160)"><rect x="470" y="110" width="220" height="90" rx="12" fill="none" stroke="{FOSF}" stroke-width="6"/></g>')
rs.append(rot(470, 136, "advertência em bula", w=220, tam=22, cor=FOSF, peso=700, alinha="center"))
p.append(caixa(980, 0, 684, 440, FOSF, CARTAO, esp=3, rx=18))
rs.append(rot(1004, 20, "Quando a conversa precisa acontecer", w=640, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2))
for j, (ic, t) in enumerate([("t:barbell", "esporte de peso ou corrida longa"), ("t:alert-triangle", "fratura por estresse prévia"), ("t:salad", "energia duvidosa")]):
    y = 130 + j * 90
    p.append(icone(ic, 1004, y, 52, FOSF))
    rs.append(rot(1076, y + 10, t, w=570, tam=26, cor=TINTA, peso=600))
rs.append(rot(1004, 400, "levar o caso a quem prescreve; não trocar por conta própria", w=640, tam=22, cor=TINTA))
diagrama(S, "injetavel", 440, p, rs, eyebrow="O injetável trimestral", titulo="Um método que pesa sobre o osso de quem já tem o osso em risco",
         fonte="Coorte de adolescentes, Fertil Steril 2008")

# 8. as condutas
p = [svg_abre(1664, 480, "Uma ficha de prontuário com o método registrado como medicação: nome, via, início, e uma linha destacada: como eram os ciclos antes? Ao lado, dois exames com setas: proteína carreadora subindo e testosterona caindo, efeito do remédio, não hipogonadismo")]
p.append(caixa(0, 0, 860, 480, TINTA, CARTAO, esp=2, rx=16))
rs = [rot(30, 24, "Medicações em uso", w=800, tam=30, cor=TINTA, peso=700, serif=True)]
for j, (k, v) in enumerate([("método", "implante de progestagênio"), ("via", "subdérmica"), ("desde", "três anos")]):
    y = 100 + j * 70
    rs += [rot(30, y, k, w=200, tam=26, cor=MUDO), rot(240, y, v, w=600, tam=26, cor=TINTA, peso=600)]
p.append(f'<rect x="20" y="320" width="820" height="130" rx="14" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
rs += [rot(44, 336, "Como eram os ciclos antes do método?", w=780, tam=30, cor=GLIC, peso=700, serif=True),
       rot(44, 396, "a pergunta mais rentável desta aula", w=780, tam=24, cor=TINTA)]
p.append(caixa(920, 0, 744, 300, AZUL, AZUL_T, esp=3, rx=16))
rs.append(rot(944, 20, "Sob pílula combinada", w=700, tam=28, cor=AZUL, peso=700, serif=True))
for j, (t, up) in enumerate([("proteína carreadora", True), ("testosterona total e livre", False)]):
    y = 100 + j * 80
    p.append(icone("t:trending-up" if up else "t:trending-down", 944, y, 52, AZUL))
    rs.append(rot(1012, y + 10, t, w=620, tam=27, cor=TINTA, peso=600))
rs.append(rot(944, 250, "efeito do remédio, não hipogonadismo", w=700, tam=24, cor=AZUL, peso=700))
p.append(caixa(920, 330, 744, 150, MUDO, PAPEL, esp=2, rx=16))
rs.append(rot(944, 352, "Platô? Antes de culpar o método: carga, energia, sono e ferro", w=700, tam=26, cor=TINTA, peso=600, lh=1.3))
diagrama(S, "condutas", 480, p, rs, eyebrow="O que cabe em qualquer profissão", titulo="Registrar como remédio, e perguntar pelo que veio antes")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Contracepção hormonal no esporte", "titulo": "O método não causou; apagou o sinal que teria avisado antes",
          "regras": ["Registrar o método como medicação, e perguntar pelos ciclos de antes",
                     "Sob método hormonal, trocar o sangramento por outros mostradores",
                     "Pílula não trata deficiência energética nem protege o osso"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Pergunta pelo método e não comemora a falta de sangramento."},
                    {"ic": "t:salad", "t": "Nutrição", "x": "Faz a conta da energia que o sangramento não mostra mais."},
                    {"ic": "h:doctor", "t": "Ginecologia e medicina", "x": "Decidem sobre o método e investigam o eixo e o osso."}]})

salvar("11-04.json", {"arquivo": "aulas/MOD11/11-04-contracepcao-hormonal-no-esporte.md",
                      "titulo": "Contracepção hormonal no esporte", "subtitulo": "Quando o sinal vital sai do painel",
                      "nota_capa": "Entra por uma lutadora que escreveu nenhuma no campo de medicações.",
                      "secoes": {"ficha": ["O sinal que sai.", "capa"], "grupos": ["O que cada método faz.", "grupos"],
                                 "encruzilhada": ["A decisão.", "encruzilhada"], "condutas": ["As condutas.", "condutas"]},
                      "slides": S})
