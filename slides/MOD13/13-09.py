"""Spec do deck 13.9. Gera 13-09.json ao lado deste arquivo."""
from _base import *

S = []

# 1. na porta da academia
p = [svg_abre(1664, 440, "Uma mulher na casa dos quarenta na porta de uma academia, sem entrar. Três balões: musculação machuca a coluna; o vizinho rompeu o joelho no futebol; a amiga se machucou no funcional. Na mão, a pergunta: qual esporte machuca menos? Ao lado, uma piscina: vou fazer só natação")]
rs = []
p.append(f'<rect x="0" y="40" width="300" height="400" rx="10" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
p.append(icone("t:barbell", 90, 120, 120, MUDO))
rs.append(rot(0, 0, "academia", w=300, tam=22, cor=MUDO, peso=700, alinha="center"))
p.append(icone("h:woman", 330, 160, 260, AZUL))
for j, (t, x, y) in enumerate([("“musculação machuca a coluna”", 620, 0), ("“o vizinho rompeu o joelho no futebol”", 620, 120), ("“a amiga se machucou no funcional”", 620, 240)]):
    p.append(caixa(x, y, 560, 96, MUDO, PAPEL, esp=2, rx=40))
    rs.append(rot(x + 20, y + 30, t, w=520, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(620, 360, 560, 80, FOSF, FOSF_T, esp=3, rx=14))
rs.append(rot(640, 382, "“Qual esporte machuca menos?”", w=520, tam=26, cor=FOSF, peso=700, serif=True, alinha="center"))
p.append(f'<rect x="1240" y="200" width="424" height="200" rx="14" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
for j in range(3):
    p.append(f'<path d="M 1260 {260 + j * 40} q 30 -14 60 0 t 60 0 t 60 0 t 60 0 t 60 0 t 60 0" stroke="{AZUL}" stroke-width="3" fill="none"/>')
rs.append(rot(1240, 130, "“vou fazer só natação”", w=424, tam=26, cor=AZUL, peso=700, serif=True, alinha="center"))
diagrama(S, "porta", 440, p, rs, eyebrow="Musculação, depois de seis anos parada", titulo="Ela quer saber qual esporte machuca menos")

# 2. as armadilhas
p = [svg_abre(1664, 420, "Três armadilhas: taxas de estudos diferentes não se comparam; frequência não é gravidade; a variação dentro de uma modalidade é maior que entre modalidades. Em destaque, o comparador esquecido: não fazer nada")]
rs = []
for k, (n, t, ic) in enumerate([("1", "taxas de estudos diferentes não se comparam", "t:ruler-measure"),
                                ("2", "frequência não é gravidade", "t:scale"),
                                ("3", "a variação dentro de uma modalidade é maior que entre elas", "t:arrows-exchange")]):
    x = k * 420
    p.append(caixa(x, 0, 400, 280, FOSF, FOSF_T, esp=3, rx=18))
    p.append(f'<circle cx="{x + 50}" cy="50" r="28" fill="{FOSF}"/>')
    rs.append(rot(x + 22, 34, n, w=56, tam=26, cor=PAPEL, peso=700, alinha="center"))
    p.append(icone(ic, x + 300, 24, 60, FOSF))
    rs.append(rot(x + 24, 110, t, w=352, tam=26, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(1270, 0, 394, 420, AZUL, AZUL, esp=3, rx=18))
p.append(icone("t:bed", 1300, 30, 80, PAPEL))
rs += [rot(1294, 130, "O comparador esquecido", w=346, tam=26, cor=PAPEL, peso=700, serif=True),
       rot(1294, 200, "seis anos parada não é um estado neutro", w=346, tam=26, cor=PAPEL, peso=700, lh=1.25),
       rot(1294, 330, "é o risco de não fazer nada", w=346, tam=24, cor=PAPEL, peso=600, lh=1.25)]
rs.append(rot(0, 320, "Responder com um ranking endossa as três.", w=1240, tam=30, cor=FOSF, peso=700, serif=True, alinha="center"))
diagrama(S, "armadilhas", 420, p, rs, eyebrow="O erro: responder a pergunta como ela veio", titulo="Um ranking de modalidades esconde três armadilhas")

# 3. os pesos
p = [svg_abre(1664, 460, "Lesões por mil horas: maioria dos esportes com pesos cerca de 2 a 4; fisiculturismo 0,24 a 1; strongman 4,5 a 6,1. Separado, futebol profissional em jogo: 36, medido em estudos diferentes, ordem de grandeza. Revisão de 2017")]
rs = []
B, K = 400, 9
p.append(f'<line x1="0" y1="{B}" x2="1100" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
barras = [("fisiculturismo", 0.24, 1, OXID), ("maioria com pesos", 2, 4, AZUL), ("strongman", 4.5, 6.1, GLIC)]
for j, (t, a, b, c) in enumerate(barras):
    x = 40 + j * 200
    p.append(f'<rect x="{x}" y="{B - b * K:.0f}" width="150" height="{b * K:.0f}" rx="8" fill="{c}" fill-opacity="0.35"/>')
    p.append(f'<rect x="{x}" y="{B - a * K:.0f}" width="150" height="{a * K:.0f}" rx="8" fill="{c}"/>')
    rs += [rot(x - 20, B - b * K - 40, f"{a:g} a {b:g}".replace(".", ","), w=190, tam=24, cor=c, peso=700, alinha="center"),
           rot(x - 30, B + 10, t, w=210, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.2)]
p.append(f'<line x1="680" y1="40" x2="680" y2="{B}" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 6"/>')
p.append(f'<rect x="760" y="{B - 36 * K}" width="180" height="{36 * K}" rx="8" fill="{FOSF}"/>')
rs += [rot(740, B - 36 * K - 40, "36", w=220, tam=30, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(720, B + 10, "futebol profissional, em jogo", w=260, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.2),
       rot(0, 0, "lesões por mil horas", w=600, tam=22, cor=MUDO, peso=700)]
p.append(caixa(1160, 0, 504, 460, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1184, 24, "Por hora de prática, treinar força está entre o que menos machuca.", w=456, tam=28, cor=OXID, peso=700, serif=True, lh=1.25),
       rot(1184, 240, "estudos diferentes: a comparação é de ordem de grandeza", w=456, tam=22, cor=MUDO, peso=700, lh=1.3),
       rot(1184, 350, "locais mais comuns: ombro, lombar, joelho", w=456, tam=22, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "pesos", 460, p, rs, eyebrow="Esportes com pesos, revisão de 2017", titulo="A musculação não está entre o que mais machuca",
         fonte="Sports Med 2017 · Br J Sports Med 2020")

# 4. os vieses
p = [svg_abre(1664, 420, "Duas cenas. A lesão tem cena: uma barra caindo na academia, com pessoas olhando. A lesão não tem cena: seis meses de corrida com uma dor surgindo devagar. Embaixo, o consultório: quem se machucou aparece; as horas sem lesão, não")]
rs = []
p.append(caixa(0, 0, 800, 280, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:barbell", 40, 70, 120, FOSF))
for j in range(4):
    p.append(icone("t:user", 220 + j * 70, 160, 56, MUDO))
p.append(icone("t:alert-triangle", 200, 40, 56, FOSF))
rs += [rot(520, 30, "a lesão tem cena", w=260, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2),
       rot(520, 140, "barra, testemunha, e a história é contada", w=260, tam=22, cor=TINTA, peso=700, lh=1.25)]
p.append(caixa(864, 0, 800, 280, AZUL, AZUL_T, esp=3, rx=18))
p.append(f'<line x1="900" y1="220" x2="1360" y2="220" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 900 215 C 1100 214 1250 200 1360 110" stroke="{AZUL}" stroke-width="6" fill="none"/>')
rs += [rot(900, 232, "seis meses de corrida", w=460, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(1380, 30, "a lesão não tem cena", w=260, tam=28, cor=AZUL, peso=700, serif=True, lh=1.2),
       rot(1380, 140, "a dor chega devagar, sem testemunha", w=260, tam=22, cor=TINTA, peso=700, lh=1.25)]
p.append(caixa(0, 310, 1664, 100, GRADE, CARTAO, esp=2, rx=16))
p.append(icone("h:stethoscope", 24, 326, 64, MUDO))
rs.append(rot(110, 336, "No consultório, quem se machucou aparece. As milhões de horas sem lesão, não.", w=1530, tam=26, cor=TINTA, peso=700))
diagrama(S, "vies", 420, p, rs, eyebrow="Por que o senso comum erra", titulo="O viés da cena e o viés do consultório")

# 5. o funcional
p = [svg_abre(1664, 440, "Sala de treinamento funcional com dois grupos: num, um treinador acompanhando a execução; no outro, ninguém. 386 praticantes, cerca de 20% com lesão; ombro, lombar e joelho os locais mais comuns; envolvimento do treinador associado a menos lesão. Estudo transversal")]
rs = []
p.append(caixa(0, 0, 520, 300, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:stopwatch", 24, 24, 56, OXID))
for j in range(3):
    p.append(icone("t:user", 120 + j * 110, 130, 90, OXID))
rs += [rot(96, 30, "com treinador", w=400, tam=28, cor=OXID, peso=700, serif=True),
       rot(24, 240, "menos lesão", w=472, tam=26, cor=OXID, peso=700, alinha="center")]
p.append(caixa(560, 0, 520, 300, FOSF, FOSF_T, esp=3, rx=18))
for j in range(3):
    p.append(icone("t:user", 680 + j * 110, 130, 90, FOSF))
rs += [rot(584, 30, "sem ninguém olhando", w=472, tam=28, cor=FOSF, peso=700, serif=True),
       rot(584, 240, "mais lesão", w=472, tam=26, cor=FOSF, peso=700, alinha="center")]
rs.append(rot(0, 330, "associação, não prova de causa: estudo transversal por questionário", w=1080, tam=22, cor=MUDO, peso=700, alinha="center"))
p.append(caixa(1140, 0, 524, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1164, 20, "386 praticantes", w=476, tam=32, cor=AZUL, peso=700, serif=True),
       rot(1164, 84, "cerca de 1 em cada 5 com lesão", w=476, tam=26, cor=TINTA, peso=700, lh=1.2),
       rot(1164, 180, "ombro, lombar, joelho", w=476, tam=26, cor=TINTA, peso=700),
       rot(1164, 240, "ombro na ginástica; lombar nos levantamentos", w=476, tam=22, cor=MUDO, peso=700, lh=1.3)]
diagrama(S, "funcional", 440, p, rs, eyebrow="Treinamento funcional de alta intensidade, levantamento de 2014", titulo="Com o treinador por perto, menos lesão",
         fonte="Orthop J Sports Med 2014")

# 6. o coletivo e a raquete
p = [svg_abre(1664, 440, "A semana do coletivo amador: seis dias vazios e um bloco de jogo. Ao lado, quadra de raquete com a entrada típica: acima dos 40, vindo do sedentarismo, direto para o torneio. Mecanismo: desaceleração e mudança de direção, joelho e tornozelo")]
rs = []
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
for j, d in enumerate(DIAS):
    x = j * 110
    rs.append(rot(x, 0, d, w=100, tam=20, cor=MUDO, peso=700, alinha="center"))
    if d == "sáb":
        p.append(f'<rect x="{x}" y="36" width="100" height="160" rx="10" fill="{FOSF}"/>')
    else:
        p.append(f'<rect x="{x}" y="36" width="100" height="160" rx="10" fill="none" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
rs += [rot(550, 100, "jogo", w=100, tam=22, cor=PAPEL, peso=700, alinha="center"),
       rot(0, 214, "só a parte de maior risco, nenhuma hora que constrói capacidade", w=770, tam=22, cor=FOSF, peso=700, lh=1.25)]
p.append(caixa(820, 0, 844, 260, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:ball-tennis", 844, 24, 72, GLIC))
rs += [rot(940, 30, "A entrada na raquete", w=700, tam=28, cor=GLIC, peso=700, serif=True),
       rot(844, 120, "acima dos 40 · vindo do sedentarismo · direto para o torneio", w=796, tam=26, cor=TINTA, peso=700, lh=1.25)]
p.append(caixa(0, 300, 1664, 140, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:arrows-exchange", 24, 330, 72, AZUL))
rs += [rot(120, 320, "Mecanismo: desaceleração e mudança de direção", w=1520, tam=28, cor=AZUL, peso=700, serif=True),
       rot(120, 372, "joelho e tornozelo · o que previne: força, aterrissagem, equilíbrio e mudança de direção treinada", w=1520, tam=22, cor=TINTA, peso=700)]
diagrama(S, "coletivo", 440, p, rs, eyebrow="O coletivo e a raquete", titulo="No coletivo amador, a pessoa só faz a parte perigosa")

# 7. a tabela por mecanismo
p = [svg_abre(1664, 460, "Quatro perfis por mecanismo. Impacto repetido: sobrecarga; rampa e força. Contato e mudança de direção: trauma; programa neuromuscular e treino antes do jogo. Carga externa com técnica: técnica e salto de carga; supervisão e progressão registrada. Sem impacto: ombro, ajuste, queda; técnica, ajuste da bicicleta, rota")]
rs = []
perfis = [("t:run", "Impacto repetido", "corrida, caminhada longa", "sobrecarga", "rampa e força", AZUL, AZUL_T),
          ("t:ball-football", "Contato e corte", "futebol, quadra, raquete", "trauma", "neuromuscular e treino antes do jogo", FOSF, FOSF_T),
          ("t:barbell", "Carga com técnica", "musculação, funcional", "técnica e salto de carga", "supervisão e progressão registrada", OXID, OXID_T),
          ("t:swimming", "Sem impacto", "natação, ciclismo", "ombro, ajuste, queda", "técnica, ajuste da bicicleta, rota", GLIC, GLIC_T)]
for k, (ic, t, ex, mec, prev, c, f) in enumerate(perfis):
    x = k * 420
    p.append(caixa(x, 0, 400, 380, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 56, c))
    rs += [rot(x + 96, 30, t, w=290, tam=26, cor=c, peso=700, serif=True, lh=1.15),
           rot(x + 24, 100, ex, w=352, tam=20, cor=MUDO, peso=700),
           rot(x + 24, 150, f"mecanismo: {mec}", w=352, tam=24, cor=TINTA, peso=700, lh=1.25),
           rot(x + 24, 260, f"previne: {prev}", w=352, tam=24, cor=c, peso=700, lh=1.25)]
rs.append(rot(0, 404, "A modalidade define o tipo de lesão; o comportamento define a quantidade.", w=1664, tam=28, cor=TINTA, peso=700, serif=True, alinha="center"))
diagrama(S, "perfis", 460, p, rs, eyebrow="No lugar do ranking", titulo="Uma tabela por mecanismo, não uma lista de esportes")

# 8. a resposta para ela
p = [svg_abre(1664, 440, "A semana dela: duas sessões de força supervisionadas e, nos outros dias, natação com uma rampa de doze semanas escrita. Frase em destaque: o mais perigoso não é o exercício; é a pressa")]
rs = []
plano = {"seg": ("força", OXID), "ter": ("natação", AZUL), "qui": ("força", OXID), "sáb": ("natação", AZUL)}
for j, d in enumerate(DIAS):
    x = j * 236
    rs.append(rot(x, 0, d, w=220, tam=22, cor=MUDO, peso=700, alinha="center"))
    if d in plano:
        t, c = plano[d]
        p.append(f'<rect x="{x}" y="36" width="220" height="140" rx="12" fill="{c}"/>')
        rs.append(rot(x, 88, t, w=220, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
    else:
        p.append(f'<rect x="{x}" y="36" width="220" height="140" rx="12" fill="none" stroke="{GRADE}" stroke-width="3" stroke-dasharray="8 6"/>')
rs += [rot(0, 190, "força: supervisionada no começo", w=700, tam=22, cor=OXID, peso=700),
       rot(720, 190, "natação: rampa de doze semanas, escrita", w=940, tam=22, cor=AZUL, peso=700)]
p.append(f'<rect x="0" y="260" width="1664" height="170" rx="18" fill="{FOSF}"/>')
rs.append(rot(40, 300, "“O mais perigoso do que você vai fazer não é o exercício. É a pressa.”", w=1584, tam=36, cor=PAPEL, peso=700, serif=True, alinha="center", lh=1.25))
diagrama(S, "resposta", 440, p, rs, eyebrow="A resposta para ela", titulo="Não um esporte: uma forma de começar")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Lesões em academia, funcional e coletivo amador", "titulo": "Não ranquear modalidades; ajustar o comportamento",
          "regras": ["Taxas não se comparam e frequência não é gravidade",
                     "Por hora, força está entre o que menos machuca; supervisão ajuda",
                     "A modalidade define o tipo de lesão; o comportamento, a quantidade"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Responde ao medo com dado e não proíbe modalidade por fama."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Supervisiona a técnica e registra a progressão."},
                    {"ic": "t:user", "t": "O praticante", "x": "Escolhe o que vai manter e começa sem pressa."}]})

salvar("13-09.json", {"arquivo": "aulas/MOD13/13-09-lesoes-em-academia-funcional-e-coletivo-amador.md",
                      "titulo": "Lesões em academia, funcional e coletivo amador", "subtitulo": "Por que não existe o esporte que não machuca",
                      "nota_capa": "Entra por uma mulher na casa dos quarenta que tem medo de começar a musculação.",
                      "secoes": {"porta": ["O erro.", "capa"], "pesos": ["Os números.", "pesos"],
                                 "perfis": ["A tabela e a resposta.", "perfis"]},
                      "slides": S})
