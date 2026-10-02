"""Spec do deck 12.10. Gera 12-10.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a dançarina e o ciclo
p = [svg_abre(1664, 450, "Dançarina de salão na casa dos oitenta. Linha do tempo de um ano: duas quedas em casa, a segunda com o punho imobilizado. Depois, o ciclo: medo de cair, sai menos e para de dançar, fica mais fraca, cai de novo"), defs(FOSF)]
rs = []
p.append(icone("h:woman", 20, 20, 280, AZUL))
rs.append(rot(0, 320, "na casa dos oitenta · baile duas vezes por semana", w=360, tam=24, cor=AZUL, peso=700, lh=1.25))
p.append(f'<line x1="400" y1="80" x2="860" y2="80" stroke="{TINTA}" stroke-width="3"/>')
for k, (x, t) in enumerate([(520, "queda em casa"), (760, "queda: punho imobilizado")]):
    p.append(f'<circle cx="{x}" cy="80" r="16" fill="{FOSF}"/>')
    rs.append(rot(x - 110, 110, t, w=220, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
rs.append(rot(400, 30, "último ano", w=460, tam=22, cor=MUDO, peso=600))
for t, (x, y) in [("medo de cair", (1260, 50)), ("sai menos, para de dançar", (1500, 210)), ("fica mais fraca", (1260, 370)), ("cai de novo", (1020, 210))]:
    p.append(caixa(x - 140, y - 38, 280, 76, FOSF, FOSF_T, esp=3, rx=38))
    rs.append(rot(x - 130, y - 26 if len(t) > 18 else y - 14, t, w=260, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.15))
for x1, y1, x2, y2 in [(1400, 70, 1470, 166), (1470, 254, 1400, 340), (1120, 350, 1050, 254), (1050, 166, 1120, 70)]:
    p.append(seta(x1, y1, x2, y2, FOSF, "m0", 4))
p.append(seta(880, 80, 1110, 56, FOSF, "m0", 4))
diagrama(S, "danca", 450, p, rs, eyebrow="Uma dançarina de salão na casa dos oitenta", titulo="O medo de cair acelera o que pretende evitar")

# 2. o fenótipo
p = [svg_abre(1664, 440, "Cinco critérios do fenótipo de fragilidade: perda de peso sem querer no último ano, cansaço relatado, preensão fraca, marcha lenta, pouca atividade física. Régua: 0, não frágil; 1 a 2, pré-frágil; 3 ou mais, frágil. Cerca de 7% de frágeis num estudo de 2001 com mais de 5.300 pessoas acima dos 65")]
rs = []
for k, (ic, t) in enumerate([("t:salad", "perda de peso sem querer"), ("t:zoom-question", "cansaço relatado"), ("t:bolt", "preensão fraca"),
                             ("t:run", "marcha lenta"), ("t:calendar", "pouca atividade física")]):
    x = k * 336
    p.append(caixa(x, 0, 316, 200, AZUL, AZUL_T, esp=3, rx=16))
    p.append(icone(ic, x + 118, 20, 80, AZUL))
    rs.append(rot(x + 16, 120, t, w=284, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2))
for k, (t, s_, c, f, w) in enumerate([("0", "não frágil", OXID, OXID_T, 380), ("1 a 2", "pré-frágil", GLIC, GLIC_T, 480), ("3 ou mais", "frágil", FOSF, FOSF_T, 380)]):
    x = [0, 400, 900][k]
    p.append(caixa(x, 240, w, 100, c, f, esp=3, rx=16))
    rs.append(rot(x + 16, 266, f"{t}: {s_}", w=w - 32, tam=28, cor=c, peso=700, alinha="center", serif=True))
p.append(caixa(1300, 240, 364, 200, TINTA, TINTA, esp=0, rx=16))
rs += [rot(1316, 256, "≈ 7%", w=332, tam=56, cor=PAPEL, peso=700, alinha="center", serif=True),
       rot(1316, 350, "frágeis entre mais de 5.300 pessoas acima dos 65", w=332, tam=22, cor=PAPEL, peso=600, alinha="center", lh=1.2)]
rs.append(rot(400, 360, "a janela: ainda há reserva", w=480, tam=22, cor=GLIC, peso=700, alinha="center"))
diagrama(S, "fenotipo", 440, p, rs, eyebrow="O fenótipo de fragilidade, estudo de 2001", titulo="Fragilidade é um estado medido, não uma idade",
         fonte="J Gerontol A Biol Sci Med Sci 2001")

# 3. a queda
p = [svg_abre(1664, 440, "Três silhuetas de idosos, uma com um raio de queda: cerca de 1 em cada 3 idosos na comunidade cai a cada ano, na estimativa mais citada. Depois da queda: fratura, medo, menos atividade, perda de independência"), defs(FOSF)]
rs = []
for k in range(3):
    p.append(icone("t:user", 40 + k * 200, 40, 180, FOSF if k == 1 else GRADE))
p.append(f'<path d="M 440 60 L 410 110 L 440 110 L 410 160" stroke="{FOSF}" stroke-width="8" fill="none" stroke-linejoin="round"/>')
rs += [rot(0, 260, "≈ 1 em 3", w=620, tam=56, cor=FOSF, peso=700, alinha="center", serif=True),
       rot(0, 350, "idosos na comunidade caem a cada ano (estimativa mais citada)", w=620, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.25)]
for k, t in enumerate(["fratura", "medo de cair", "menos atividade", "perda de independência"]):
    y = k * 110
    p.append(caixa(820, y, 500, 90, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(840, y + 28, t, w=460, tam=28, cor=TINTA, peso=700, alinha="center"))
    if k < 3:
        p.append(seta(1070, y + 92, 1070, y + 108, FOSF, "m0", 4))
p.append(seta(680, 200, 810, 45, FOSF, "m0", 4))
p.append(caixa(1360, 0, 304, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1376, 24, "O que se treina: a capacidade de se recuperar de um desequilíbrio.", w=272, tam=26, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "queda", 440, p, rs, eyebrow="A queda como evento", titulo="A queda transforma fragilidade em dependência")

# 4. triagem
p = [svg_abre(1664, 440, "Triagem das diretrizes mundiais de 2022. Etapa 1: caiu no último ano? tem medo de cair ou se sente instável? Etapa 2, se caiu: lesão, duas ou mais quedas, fragilidade, ficou no chão sem conseguir levantar, suspeita de desmaio. Saída: avaliação multifatorial com remédios, visão, pés e calçado, pressão ao levantar, cognição, casa"), defs(TINTA)]
rs = []
p.append(caixa(0, 0, 420, 300, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(24, 20, "Em todo contato", w=372, tam=28, cor=AZUL, peso=700, serif=True),
       rot(24, 90, "caiu no último ano?", w=372, tam=26, cor=TINTA, peso=700),
       rot(24, 170, "tem medo de cair ou se sente instável?", w=372, tam=26, cor=TINTA, peso=700, lh=1.25)]
p.append(seta(430, 150, 480, 150, TINTA, "m0", 4))
p.append(caixa(490, 0, 560, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(514, 20, "Se caiu: risco alto se houve", w=512, tam=26, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["lesão", "duas ou mais quedas no ano", "fragilidade", "ficou no chão sem conseguir levantar", "suspeita de desmaio"]):
    rs.append(rot(514, 84 + j * 70, "· " + t, w=512, tam=24, cor=TINTA, peso=700, lh=1.2))
p.append(seta(1060, 220, 1110, 220, TINTA, "m0", 4))
p.append(caixa(1120, 0, 544, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1144, 20, "Avaliação multifatorial", w=496, tam=26, cor=OXID, peso=700, serif=True))
rs.append(rot(1144, 84, "remédios · visão · pés e calçado · pressão ao levantar · cognição · casa", w=496, tam=26, cor=TINTA, peso=700, lh=1.5))
rs.append(rot(1144, 330, "a dançarina: duas quedas e uma lesão", w=496, tam=22, cor=OXID, peso=700, lh=1.2))
diagrama(S, "triagem", 440, p, rs, eyebrow="Diretrizes mundiais de prevenção de quedas, 2022", titulo="Perguntar sobre quedas, e saber o que fazer com a resposta",
         fonte="Age Ageing 2022")

# 5. testes
p = [svg_abre(1664, 440, "Três testes com cronômetro. Levantar, andar três metros, virar e voltar a sentar: 12 segundos ou mais, risco. Quatro posições de equilíbrio, dez segundos cada, a terceira com um pé à frente do outro. Velocidade de marcha abaixo de 0,8 m/s: mais quedas"), defs(TINTA)]
rs = []
p.append(caixa(0, 0, 540, 440, GLIC, GLIC_T, esp=3, rx=18))
p += [f'<rect x="40" y="150" width="70" height="80" rx="8" fill="{TINTA}"/>', f'<line x1="130" y1="250" x2="470" y2="250" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>',
      seta(140, 200, 450, 200, TINTA, "m0", 4), f'<circle cx="480" cy="200" r="14" fill="none" stroke="{TINTA}" stroke-width="4"/>']
rs += [rot(24, 20, "Levantar e andar", w=492, tam=28, cor=GLIC, peso=700, serif=True),
       rot(24, 70, "levanta, anda 3 m, vira, volta, senta", w=492, tam=22, cor=TINTA, peso=600),
       rot(24, 290, "≥ 12 s: risco", w=492, tam=40, cor=TINTA, peso=700, serif=True)]
p.append(caixa(562, 0, 540, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(586, 20, "Equilíbrio em 4 posições", w=492, tam=28, cor=AZUL, peso=700, serif=True),
       rot(586, 70, "10 segundos cada", w=492, tam=22, cor=TINTA, peso=600)]
for k, pes in enumerate([[(0, 0), (40, 0)], [(0, 0), (24, -30)], [(0, 0), (0, -64)], [(0, 0)]]):
    x0, y0 = 620 + k * 120, 250
    for dx, dy in pes:
        p.append(f'<rect x="{x0 + dx}" y="{y0 + dy}" width="28" height="60" rx="14" fill="{AZUL if k != 2 else FOSF}"/>')
rs.append(rot(586, 330, "não sustenta a 3ª: risco", w=492, tam=30, cor=FOSF, peso=700, serif=True))
p.append(caixa(1124, 0, 540, 440, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1148, 20, "Velocidade de marcha", w=492, tam=28, cor=OXID, peso=700, serif=True),
       rot(1148, 150, "< 0,8 m/s", w=492, tam=56, cor=TINTA, peso=700, serif=True),
       rot(1148, 290, "associada a mais quedas", w=492, tam=26, cor=TINTA, peso=600)]
diagrama(S, "testes", 440, p, rs, eyebrow="Capacidade funcional com um cronômetro", titulo="Três testes dão o ponto de partida, com data")

# 6. o número
p = [svg_abre(1664, 440, "Revisão sistemática de 2019 com 108 ensaios randomizados. Redução da taxa de quedas: exercício em geral, 23%, certeza alta; equilíbrio e funcionais, 24%, certeza alta; vários tipos combinados, 34%, certeza moderada")]
rs = []
base, esc = 380, 8
for k, (v, t, cert, c) in enumerate([(23, "exercício em geral", "certeza alta", OXID), (24, "equilíbrio e funcionais", "certeza alta", OXID), (34, "vários tipos combinados", "certeza moderada", AZUL)]):
    x = 80 + k * 380
    p.append(f'<rect x="{x}" y="{base - v * esc}" width="240" height="{v * esc}" rx="10" fill="{c}"/>')
    rs += [rot(x - 30, base - v * esc - 70, f"−{v}%", w=300, tam=48, cor=c, peso=700, alinha="center", serif=True),
           rot(x - 40, base + 8, t, w=320, tam=24, cor=TINTA, peso=700, alinha="center"),
           rot(x, base - v * esc + 16, cert, w=240, tam=20, cor=PAPEL, peso=700, alinha="center")]
p.append(f'<line x1="40" y1="{base}" x2="1200" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(caixa(1260, 0, 404, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(1280, 24, "Vale para quem vive na comunidade. Em instituições e logo após a alta, o exercício não mostrou efeito sozinho (revisão de 2017).", w=364, tam=24, cor=TINTA, peso=700, lh=1.35))
diagrama(S, "numero", 440, p, rs, eyebrow="Revisão sistemática de 2019, 108 ensaios randomizados", titulo="O exercício reduz as quedas em cerca de um quarto",
         fonte="Cochrane Database Syst Rev 2019; Br J Sports Med 2017")

# 7. o que faz diferença
p = [svg_abre(1664, 440, "O que torna o exercício eficaz: equilíbrio que desafia (base menor, centro de massa em movimento, menos apoio das mãos); dose de mais de 3 horas por semana, 3 ou mais dias; combinação de equilíbrio, funcionais e força. Desafio e dose juntos: 39% menos quedas na revisão de 2017")]
rs = []
for k, (t, itens, c, f) in enumerate([("Equilíbrio que desafia", ["base de apoio menor", "centro de massa em movimento", "menos apoio das mãos"], OXID, OXID_T),
                                      ("Dose", ["mais de 3 horas por semana", "3 ou mais dias"], AZUL, AZUL_T),
                                      ("Combinação", ["equilíbrio", "exercícios funcionais", "força e potência"], GLIC, GLIC_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 330, c, f, esp=3, rx=18))
    rs.append(rot(x + 20, 20, t, w=360, tam=28, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 20, 90 + j * 76, "· " + it, w=360, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(caixa(1260, 0, 404, 330, TINTA, TINTA, esp=0, rx=18))
rs += [rot(1276, 40, "−39%", w=372, tam=64, cor=PAPEL, peso=700, alinha="center", serif=True),
       rot(1276, 160, "quando desafio e dose se somam", w=372, tam=24, cor=PAPEL, peso=700, alinha="center", lh=1.25)]
p.append(caixa(0, 360, 1664, 80, GRADE, CARTAO, esp=2, rx=14))
rs.append(rot(20, 382, "Caminhar faz bem ao coração, mas desafia pouco o equilíbrio", w=1624, tam=24, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "desafio", 440, p, rs, eyebrow="Que exercício faz a diferença", titulo="Equilíbrio só treina quando desafia",
         fonte="Br J Sports Med 2017; Age Ageing 2022")

# 8. o plano
p = [svg_abre(1664, 440, "O plano da dançarina em quatro blocos: avaliação multifatorial antes e junto; equilíbrio que desafia e força, 3 vezes por semana; aprender a levantar do chão; voltar ao baile como meta"), defs(OXID)]
rs = []
for k, (ic, t, c, f) in enumerate([("h:doctor", "avaliação multifatorial, antes e junto", AZUL, AZUL_T), ("t:stopwatch", "equilíbrio que desafia e força, 3 vezes por semana", OXID, OXID_T),
                                   ("t:user", "aprender a levantar do chão", GLIC, GLIC_T), ("h:woman", "voltar ao baile como meta", FOSF, FOSF_T)]):
    x = k * 420
    p.append(caixa(x, 0, 380, 380, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 130, 40, 120, c))
    rs.append(rot(x + 20, 210, t, w=340, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.25))
    if k < 3:
        p.append(seta(x + 384, 190, x + 416, 190, OXID, "m0", 4))
rs.append(rot(0, 400, "o medo a tirou do salão; o plano a devolve a ele", w=1664, tam=24, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "plano", 440, p, rs, eyebrow="O plano da dançarina", titulo="A meta é devolvê-la ao baile, não substituí-lo")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fragilidade, risco de queda e capacidade funcional", "titulo": "Equilíbrio que desafia, força e a pergunta sobre quedas",
          "regras": ["Exercício reduz quedas em cerca de um quarto; combinado, em cerca de um terço",
                     "Equilíbrio só treina quando desafia, e a dose passa de 3 horas por semana",
                     "Lesão, duas quedas, chão ou desmaio: avaliação multifatorial além do exercício"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Pergunta sobre quedas em todo contato e conduz a avaliação multifatorial, a começar pelos remédios."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Monta equilíbrio que desafia, força e o treino de levantar do chão, três vezes por semana."},
                    {"ic": "t:users", "t": "A família", "x": "Tira o medo do centro e ajuda a pessoa a voltar ao que fazia."}]})

salvar("12-10.json", {"arquivo": "aulas/MOD12/12-10-fragilidade-risco-de-queda-e-capacidade-funcional.md",
                      "titulo": "Fragilidade, risco de queda e capacidade funcional", "subtitulo": "O exercício reduz as quedas em cerca de um quarto",
                      "nota_capa": "Entra por uma dançarina de salão na casa dos oitenta que parou de dançar depois de duas quedas.",
                      "secoes": {"danca": ["O caso e a fragilidade.", "capa"], "triagem": ["Reconhecer o risco.", "triagem"],
                                 "numero": ["O número.", "numero"], "plano": ["O plano.", "plano"]},
                      "slides": S})
