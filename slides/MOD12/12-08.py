"""Spec do deck 12.8. Gera 12-08.json ao lado deste arquivo."""
from _base import *

S = []


def bicicleta(x, y, s, cor):
    """Bicicleta de perfil com ciclista sentada, num retângulo de largura s (altura ~0,7 s)."""
    k = s / 100
    def P(a, b):
        return f"{x + a * k:.0f} {y + b * k:.0f}"
    r = 17 * k
    w = max(4, 3.5 * k)
    return (f'<circle cx="{x + 20 * k:.0f}" cy="{y + 52 * k:.0f}" r="{r:.0f}" fill="none" stroke="{TINTA}" stroke-width="{w:.0f}"/>'
            f'<circle cx="{x + 80 * k:.0f}" cy="{y + 52 * k:.0f}" r="{r:.0f}" fill="none" stroke="{TINTA}" stroke-width="{w:.0f}"/>'
            f'<path d="M {P(20, 52)} L {P(42, 30)} L {P(68, 30)} L {P(80, 52)} M {P(42, 30)} L {P(50, 52)} L {P(68, 30)} M {P(20, 52)} L {P(50, 52)} M {P(40, 24)} L {P(46, 24)} M {P(68, 30)} L {P(66, 20)} L {P(72, 18)}" '
            f'stroke="{TINTA}" stroke-width="{w:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{x + 56 * k:.0f}" cy="{y - 6 * k:.0f}" r="{7 * k:.0f}" fill="{cor}"/>'
            f'<path d="M {P(43, 22)} L {P(54, 2)} L {P(70, 18)} M {P(43, 22)} L {P(56, 34)} L {P(50, 50)}" stroke="{cor}" stroke-width="{7 * k:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


# 1. a ciclista
p = [svg_abre(1664, 440, "Ciclista na casa dos setenta. Pedala três vezes por semana, pressão alta controlada, osteopenia. A ficha da academia: elástico leve, 3 × 15, sem carga: estímulo pequeno demais")]
rs = []
p.append(bicicleta(20, 100, 440, AZUL))
p.append(caixa(560, 0, 480, 300, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(584, 20, "Na casa dos setenta", w=432, tam=28, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["pedala 3 vezes por semana", "pressão alta controlada", "osteopenia na densitometria"]):
    rs.append(rot(584, 90 + j * 60, "· " + t, w=432, tam=26, cor=TINTA, peso=600))
p.append(caixa(1100, 0, 564, 300, FOSF, CARTAO, esp=3, rx=18))
rs.append(rot(1124, 20, "A ficha da academia", w=516, tam=28, cor=FOSF, peso=700, serif=True))
for j, t in enumerate(["elástico leve", "3 × 15", "sem carga"]):
    rs.append(rot(1124, 90 + j * 60, t, w=516, tam=30, cor=TINTA, peso=700))
p.append(caixa(560, 340, 1104, 100, FOSF, FOSF, esp=0, rx=16))
rs.append(rot(580, 368, "A intenção é proteger; o estímulo é pequeno demais para mudar alguma coisa", w=1064, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ciclista", 440, p, rs, eyebrow="Uma ciclista na casa dos setenta começa força", titulo="Proteger com carga baixa demais não protege")

# 2. triagem
p = [svg_abre(1664, 440, "Passo 1, triagem em três perguntas: já é ativa? tem doença cardiovascular, metabólica ou renal conhecida, ou sintomas? que intensidade quer? Saídas: sintoma, para e avalia; doença conhecida, começa leve a moderado e avalia antes do vigoroso; ativa sem doença nem sintoma, segue e começa"), defs(TINTA)]
rs = []
for k, t in enumerate(["Já é ativa?", "Doença cardiovascular, metabólica ou renal conhecida, ou sintomas?", "Que intensidade quer?"]):
    x = k * 564
    p.append(caixa(x, 0, 520, 120, TINTA, CARTAO, esp=3, rx=16))
    rs.append(rot(x + 20, 24 if k != 1 else 14, t, w=480, tam=26 if k != 1 else 24, cor=TINTA, peso=700, alinha="center", lh=1.2))
    if k < 2:
        p.append(seta(x + 524, 60, x + 560, 60, TINTA, "m0", 4))
for k, (t, c, f) in enumerate([("sintoma: para e avalia", FOSF, FOSF_T), ("doença conhecida: começa leve a moderado; avalia antes do vigoroso", GLIC, GLIC_T),
                               ("ativa, sem doença nem sintoma: segue e começa", OXID, OXID_T)]):
    x = k * 564
    p.append(caixa(x, 160, 520, 150, c, f, esp=3, rx=16))
    rs.append(rot(x + 20, 186, t, w=480, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.25))
p.append(caixa(1128, 318, 520, 40, OXID, OXID, esp=0, rx=20))
rs.append(rot(1128, 322, "a ciclista está aqui", w=520, tam=22, cor=PAPEL, peso=700, alinha="center"))
p.append(caixa(0, 380, 1100, 60, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 394, "A triagem acha quem precisa de avaliação; não pode virar barreira", w=1060, tam=24, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "triagem", 440, p, rs, eyebrow="Passo 1", titulo="Três perguntas decidem quem começa já",
         fonte="Med Sci Sports Exerc 2015")

# 3. ponto de partida
p = [svg_abre(1664, 440, "Passo 2: quatro medidas com data: preensão palmar, sentar e levantar cinco vezes, velocidade de marcha e carga em dois ou três exercícios. Régua de esforço: terminar a série com 2 a 3 repetições sobrando")]
rs = []
for k, (ic, t) in enumerate([("t:bolt", "preensão palmar"), ("t:stopwatch", "sentar e levantar 5 vezes"), ("t:run", "velocidade de marcha"), ("t:calendar", "carga em 2 ou 3 exercícios")]):
    x = k * 420
    p.append(caixa(x, 0, 400, 180, AZUL, AZUL_T, esp=3, rx=16))
    p.append(icone(ic, x + 24, 24, 64, AZUL))
    rs.append(rot(x + 104, 30, t, w=280, tam=24, cor=TINTA, peso=700, lh=1.2))
rs.append(rot(0, 196, "com data, para comparar depois", w=1664, tam=22, cor=MUDO, peso=600, alinha="center"))
for i in range(12):
    sobra = i >= 9
    p.append(f'<rect x="{i * 112}" y="270" width="100" height="70" rx="10" fill="{GRADE if sobra else OXID}" stroke="{OXID}" stroke-width="3"/>')
rs += [rot(0, 352, "repetições feitas", w=1000, tam=24, cor=OXID, peso=700, alinha="center"),
       rot(1008, 352, "2 a 3 sobrando", w=320, tam=24, cor=MUDO, peso=700, alinha="center")]
p.append(caixa(1360, 250, 304, 190, OXID, OXID_T, esp=3, rx=16))
rs.append(rot(1376, 266, "sem teste de carga máxima para quem começa", w=272, tam=24, cor=TINTA, peso=700, lh=1.25))
diagrama(S, "partida", 440, p, rs, eyebrow="Passo 2", titulo="Medir o começo e achar a carga pelo esforço")

# 4. gestos da vida
p = [svg_abre(1664, 440, "Passo 3, seis gestos da vida e o exercício de cada um: sentar e levantar, agachamento; pegar do chão, dobrar o quadril; empurrar, supino ou flexão; puxar, remada; carregar sacolas, caminhada com peso; subir degrau, subida no banco"), defs(OXID)]
rs = []
for i, (g, e) in enumerate([("sentar e levantar", "agachamento"), ("pegar do chão", "dobrar o quadril"), ("empurrar", "supino ou flexão"),
                            ("puxar", "remada"), ("carregar sacolas", "caminhada com peso"), ("subir degrau", "subida no banco")]):
    x, y = (i % 3) * 564, (i // 3) * 230
    p.append(caixa(x, y, 240, 200, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(x + 16, y + 70, g, w=208, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.2))
    p.append(seta(x + 250, y + 100, x + 290, y + 100, OXID, "m0", 4))
    p.append(caixa(x + 296, y, 240, 200, OXID, OXID_T, esp=3, rx=16))
    rs.append(rot(x + 312, y + 70, e, w=208, tam=26, cor=OXID, peso=700, alinha="center", lh=1.2))
diagrama(S, "gestos", 440, p, rs, eyebrow="Passo 3", titulo="O exercício precisa parecer com o gesto da vida")

# 5. a dose
p = [svg_abre(1664, 440, "Passo 4, a dose. Semana com força em segunda, quarta e sexta e pedal em terça, quinta e sábado. Régua de intensidade com a seta em moderada a pesada. OMS 2020: força em 2 ou mais dias; idosos, equilíbrio e força em 3 ou mais dias. Ensaio de 2018: 5 × 5 acima de 85%, supervisionado")]
rs = []
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
for i, d in enumerate(dias):
    x = i * 140
    tipo = {0: "força", 2: "força", 4: "força", 1: "pedal", 3: "pedal", 5: "pedal"}.get(i, "")
    c, f = (OXID, OXID_T) if tipo == "força" else ((AZUL, AZUL_T) if tipo else (GRADE, CARTAO))
    p.append(caixa(x, 0, 124, 150, c, f, esp=3, rx=14))
    rs += [rot(x, 14, d, w=124, tam=24, cor=TINTA, peso=700, alinha="center")]
    if tipo:
        rs.append(rot(x, 80, tipo, w=124, tam=22, cor=c, peso=700, alinha="center"))
p.append(f'<rect x="0" y="220" width="960" height="30" rx="15" fill="{GRADE}"/>')
p.append(f'<rect x="480" y="220" width="400" height="30" rx="15" fill="{OXID}"/>')
rs += [rot(0, 262, "leve", w=200, tam=22, cor=MUDO, peso=600), rot(380, 262, "moderada", w=200, tam=22, cor=TINTA, peso=700, alinha="center"),
       rot(760, 262, "pesada", w=200, tam=22, cor=TINTA, peso=700, alinha="right"),
       rot(0, 320, "2 a 3 sessões · 6 a 8 exercícios · 2 a 3 séries · 2 a 3 repetições sobrando", w=960, tam=24, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(1040, 0, 624, 200, AZUL, AZUL_T, esp=3, rx=16))
rs += [rot(1064, 18, "OMS, 2020", w=576, tam=26, cor=AZUL, peso=700, serif=True),
       rot(1064, 70, "força em 2 ou mais dias; idosos: equilíbrio e força em 3 ou mais dias", w=576, tam=24, cor=TINTA, peso=600, lh=1.3)]
p.append(caixa(1040, 230, 624, 210, FOSF, FOSF_T, esp=3, rx=16))
rs += [rot(1064, 248, "Sem teto por idade", w=576, tam=26, cor=FOSF, peso=700, serif=True),
       rot(1064, 300, "ensaio de 2018: 5 × 5 acima de 85% da carga máxima, supervisionado", w=576, tam=24, cor=TINTA, peso=600, lh=1.3)]
diagrama(S, "dose", 440, p, rs, eyebrow="Passo 4", titulo="Duas a três vezes por semana, com carga de verdade",
         fonte="Br J Sports Med 2020; J Bone Miner Res 2018")

# 6. potência
p = [svg_abre(1664, 440, "Passo 5, potência: no agachamento, subir rápido com intenção e descer controlado. Ao lado, esquema: potência caindo mais depressa que força com a idade"), defs(FOSF, AZUL)]
rs = []
p += [f'<circle cx="200" cy="40" r="30" fill="{TINTA}"/>', f'<rect x="170" y="76" width="60" height="120" rx="20" fill="{TINTA}"/>',
      f'<path d="M 182 196 L 150 270 L 186 340 M 218 196 L 250 270 L 214 340" stroke="{TINTA}" stroke-width="26" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
      f'<rect x="80" y="360" width="240" height="20" rx="10" fill="{GRADE}"/>']
p.append(seta(370, 100, 370, 300, AZUL, "m1", 7))
p.append(seta(470, 300, 470, 100, FOSF, "m0", 7))
rs += [rot(300, 320, "descer controlado", w=150, tam=24, cor=AZUL, peso=700, alinha="center", lh=1.2),
       rot(420, 30, "subir rápido, com intenção", w=200, tam=24, cor=FOSF, peso=700, alinha="center", lh=1.2)]
x0, base = 760, 380
p.append(f'<line x1="{x0}" y1="{base}" x2="1300" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="40" x2="{x0}" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M {x0} 80 C 950 90 1100 140 1300 220" stroke="{OXID}" stroke-width="6" fill="none"/>')
p.append(f'<path d="M {x0} 80 C 900 110 1050 230 1300 320" stroke="{FOSF}" stroke-width="6" fill="none"/>')
rs += [rot(1110, 120, "força", w=200, tam=24, cor=OXID, peso=700), rot(980, 270, "potência", w=200, tam=24, cor=FOSF, peso=700),
       rot(x0 + 10, base + 10, "idade · esquema", w=400, tam=22, cor=MUDO)]
p.append(caixa(1360, 0, 304, 440, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1376, 24, "É a potência que segura o tropeço e levanta da cadeira sem apoio.", w=272, tam=26, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "potencia", 440, p, rs, eyebrow="Passo 5", titulo="Subir rápido treina a qualidade que cai primeiro")

# 7. progressão
p = [svg_abre(1664, 440, "Passo 6, dupla progressão numa planilha ilustrativa: semanas 1 a 6, repetições subindo de 8 a 12 com a mesma carga; ao chegar a 12 com 2 a 3 sobrando, a carga sobe e as repetições voltam a 8. Reavaliar as medidas em 8 a 12 semanas")]
rs = []
plano = [(10, 8), (10, 10), (10, 12), (12, 8), (12, 10), (12, 12)]
rs += [rot(0, 70, "carga (kg)", w=180, tam=24, cor=TINTA, peso=700), rot(0, 170, "repetições", w=180, tam=24, cor=TINTA, peso=700)]
for i, (cg, rp) in enumerate(plano):
    x = 200 + i * 170
    sobe = i == 3
    rs.append(rot(x, 10, f"sem {i + 1}", w=150, tam=22, cor=MUDO, peso=600, alinha="center"))
    p.append(caixa(x, 50, 150, 70, OXID if sobe else GRADE, OXID_T if sobe else CARTAO, esp=3, rx=12))
    p.append(caixa(x, 150, 150, 70, GLIC, GLIC_T if rp == 12 else CARTAO, esp=3, rx=12))
    rs.append(rot(x, 172, str(rp), w=150, tam=26, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x, 72, f"{cg} ↑" if sobe else str(cg), w=150, tam=26, cor=OXID if sobe else TINTA, peso=700, alinha="center"))
rs.append(rot(200, 236, "números ilustrativos", w=400, tam=20, cor=MUDO))
p.append(caixa(0, 290, 1220, 150, GLIC, GLIC_T, esp=3, rx=16))
rs.append(rot(24, 310, "Chegou ao topo da faixa com 2 a 3 sobrando: a carga sobe e as repetições voltam ao começo. Tudo anotado.", w=1172, tam=26, cor=TINTA, peso=700, lh=1.3))
p.append(caixa(1280, 50, 384, 390, AZUL, AZUL_T, esp=3, rx=16))
p.append(icone("t:calendar", 1420, 80, 100, AZUL))
rs += [rot(1300, 200, "8 a 12 semanas", w=344, tam=30, cor=AZUL, peso=700, alinha="center", serif=True),
       rot(1300, 260, "repetir as medidas do passo 2 e mostrar o resultado", w=344, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.3)]
diagrama(S, "progressao", 440, p, rs, eyebrow="Passo 6", titulo="Sem registro não há progressão, só repetição")

# 8. ajustes
p = [svg_abre(1664, 440, "Quatro situações. Artrose de joelho: força é tratamento; ajustar amplitude e carga pela dor. Pressão alta: não prender a respiração; expirar no esforço. Osteoporose: carga supervisionada, coluna neutra. Volta de internação: começar mais baixo, progredir mais rápido")]
rs = []
for k, (t, x_t, c, f) in enumerate([("Artrose de joelho", "força é tratamento; amplitude e carga ajustadas pela dor do dia seguinte", OXID, OXID_T),
                                    ("Pressão alta", "não prender a respiração; expirar na fase de força", AZUL, AZUL_T),
                                    ("Osteoporose", "carga é o estímulo do osso: supervisão e coluna neutra", GLIC, GLIC_T),
                                    ("Volta de internação", "começar mais baixo e progredir mais rápido", FOSF, FOSF_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 340, c, f, esp=3, rx=18))
    rs += [rot(x + 20, 24, t, w=360, tam=28, cor=c, peso=700, serif=True, lh=1.15), rot(x + 20, 120, x_t, w=360, tam=24, cor=TINTA, peso=600, lh=1.3)]
p.append(caixa(0, 370, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 388, "Sintoma novo em qualquer situação: volta ao passo 1", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ajustes", 440, p, rs, eyebrow="Quando há dor ou doença", titulo="Os mesmos seis passos, com ajustes de cada condição")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Prescrição de força no idoso", "titulo": "Carga de verdade, subida rápida e progressão anotada",
          "regras": ["A triagem acha quem precisa de avaliação e não pode virar barreira",
                     "A carga certa deixa 2 a 3 repetições sobrando; não há teto por idade",
                     "Sem potência e sem registro, o treino vira exercício que não muda nada"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Faz a triagem pelas três perguntas e libera sem atrasar quem pode começar."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Escolhe gestos da vida, dosa pelo esforço, ensina a subir rápido e registra."},
                    {"ic": "h:doctor-female", "t": "Fisioterapia", "x": "Ajusta o caminho na dor, na artrose e na volta de internação."}]})

salvar("12-08.json", {"arquivo": "aulas/MOD12/12-08-prescricao-de-forca-no-idoso.md",
                      "titulo": "Prescrição de força no idoso", "subtitulo": "Seis passos, do primeiro dia à progressão",
                      "nota_capa": "Entra por uma ciclista na casa dos setenta que recebeu uma ficha de carga baixa demais.",
                      "secoes": {"ciclista": ["O caso.", "capa"], "triagem": ["Os seis passos.", "triagem"],
                                 "ajustes": ["Dor ou doença.", "ajustes"]},
                      "slides": S})
