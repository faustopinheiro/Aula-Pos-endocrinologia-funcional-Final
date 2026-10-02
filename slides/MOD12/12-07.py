"""Spec do deck 12.7. Gera 12-07.json ao lado deste arquivo."""
from _base import *

S = []


def corredor(x, y, s, cor):
    """Corredor em passada, de perfil, num quadrado de lado s com canto em (x, y)."""
    k = s / 100
    def P(a, b):
        return f"{x + a * k:.0f} {y + b * k:.0f}"
    w = max(4, 9 * k)
    return (f'<circle cx="{x + 58 * k:.0f}" cy="{y + 12 * k:.0f}" r="{10 * k:.0f}" fill="{cor}"/>'
            f'<path d="M {P(55, 24)} L {P(45, 55)} M {P(45, 55)} L {P(62, 75)} L {P(55, 98)} M {P(45, 55)} L {P(30, 72)} L {P(14, 70)} '
            f'M {P(52, 32)} L {P(70, 44)} L {P(80, 34)} M {P(52, 32)} L {P(36, 42)} L {P(30, 56)}" '
            f'stroke="{cor}" stroke-width="{w:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


# 1. o corredor
p = [svg_abre(1664, 440, "Corredor na casa dos sessenta ao lado de uma balança de bioimpedância com massa muscular normal. Duas fichas de preensão palmar com dois anos de distância, 46 kg e 40 kg, ambas acima da linha de 27 kg. Números ilustrativos")]
rs = []
p.append(corredor(0, 20, 300, AZUL))
p.append(caixa(340, 140, 300, 220, TINTA, CARTAO, esp=3, rx=24))
p.append(f'<rect x="400" y="170" width="180" height="60" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="2"/>')
rs += [rot(400, 186, "normal", w=180, tam=24, cor=OXID, peso=700, alinha="center"),
       rot(350, 250, "massa muscular na bioimpedância", w=280, tam=22, cor=TINTA, peso=600, alinha="center", lh=1.2),
       rot(0, 360, "na casa dos sessenta · 40 km por semana", w=640, tam=24, cor=AZUL, peso=700)]
base, esc = 400, 7
for k, (v, t) in enumerate([(46, "há dois anos"), (40, "agora")]):
    x = 800 + k * 300
    p.append(f'<rect x="{x}" y="{base - v * esc}" width="180" height="{v * esc}" rx="8" fill="{GLIC if k else AZUL}"/>')
    rs += [rot(x - 40, base - v * esc - 50, f"{v} kg", w=260, tam=32, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(x - 40, base + 6, t, w=260, tam=22, cor=MUDO, peso=600, alinha="center")]
p.append(f'<line x1="740" y1="{base - 27 * esc}" x2="1440" y2="{base - 27 * esc}" stroke="{FOSF}" stroke-width="4" stroke-dasharray="12 8"/>')
p.append(f'<line x1="740" y1="{base}" x2="1440" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
rs += [rot(1460, base - 27 * esc - 16, "corte: 27 kg", w=204, tam=24, cor=FOSF, peso=700),
       rot(1460, 0, "preensão palmar", w=204, tam=24, cor=TINTA, peso=700, lh=1.2),
       rot(1460, 380, "números ilustrativos", w=204, tam=20, cor=MUDO)]
diagrama(S, "corredor", 440, p, rs, eyebrow="Um corredor na casa dos sessenta", titulo="A balança diz normal, e a força está caindo")

# 2. a definição
p = [svg_abre(1664, 440, "Três degraus do consenso europeu revisado de 2019: força baixa levanta a suspeita; massa ou qualidade baixa confirma; desempenho físico ruim indica gravidade. A balança de bioimpedância não diagnostica")]
rs = []
for k, (t, s_, c, f) in enumerate([("força baixa", "suspeita", FOSF, FOSF_T), ("massa ou qualidade baixa", "confirma", GLIC, GLIC_T), ("desempenho ruim", "gravidade", AZUL, AZUL_T)]):
    x, y = k * 340, 280 - k * 130
    p.append(caixa(x, y, 330, 440 - y, c, f, esp=3, rx=14))
    rs += [rot(x + 16, y + 16, t, w=298, tam=26, cor=TINTA, peso=700, lh=1.2), rot(x + 16, y + 80 if k else y + 60, s_, w=298, tam=30, cor=c, peso=700, serif=True)]
p.append(caixa(1140, 40, 524, 230, TINTA, CARTAO, esp=3, rx=24))
p.append(f'<rect x="1290" y="80" width="220" height="70" rx="8" fill="{GRADE}"/>')
p.append(f'<rect x="1220" y="190" width="80" height="40" rx="8" fill="{GRADE}"/><rect x="1500" y="190" width="80" height="40" rx="8" fill="{GRADE}"/>')
p.append(f'<line x1="1180" y1="250" x2="1624" y2="60" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
rs += [rot(1140, 300, "bioimpedância da academia: não diagnostica", w=524, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.25)]
diagrama(S, "definicao", 440, p, rs, eyebrow="Consenso europeu revisado, 2019", titulo="A suspeita começa pela força, não pela massa",
         fonte="Age Ageing 2019")

# 3. como medir
p = [svg_abre(1664, 440, "Quatro instrumentos com pontos de corte. Questionário de cinco itens: rastreio. Dinamômetro: preensão abaixo de 27 kg em homens e 16 kg em mulheres. Cadeira com cronômetro: cinco levantadas em mais de 15 segundos. Marcha a 0,8 metro por segundo ou menos")]
rs = []
for k, (ic, t, v, s_, c, f) in enumerate([("t:zoom-question", "Rastrear", "5 itens", "questionário", TINTA, CARTAO),
                                           ("t:bolt", "Força", "< 27 kg · < 16 kg", "preensão, homens · mulheres", FOSF, FOSF_T),
                                           ("t:stopwatch", "Força, sem dinamômetro", "> 15 s", "5 levantadas da cadeira", GLIC, GLIC_T),
                                           ("t:run", "Gravidade", "≤ 0,8 m/s", "velocidade de marcha", AZUL, AZUL_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 440, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 150, 30, 100, c))
    rs += [rot(x + 20, 160, t, w=360, tam=26, cor=c, peso=700, alinha="center"),
           rot(x + 20, 230, v, w=360, tam=36, cor=TINTA, peso=700, alinha="center", serif=True),
           rot(x + 20, 320, s_, w=360, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.25)]
diagrama(S, "medir", 440, p, rs, eyebrow="Como medir", titulo="Um dinamômetro e um cronômetro bastam para começar",
         fonte="Age Ageing 2019")

# 4. três vezes
p = [svg_abre(1664, 440, "Estudo de 2006 com 1.880 pessoas na casa dos setenta, três anos. Perda anual de massa magra da perna, cerca de 1%; perda anual de força da perna, cerca de 3%. Três vezes. Ganhar massa não impediu a perda de força")]
rs = []
base, esc = 380, 90
for k, (v, t, c) in enumerate([(1, "massa magra da perna", AZUL), (3, "força da perna", FOSF)]):
    x = 80 + k * 360
    p.append(f'<rect x="{x}" y="{base - v * esc}" width="220" height="{v * esc}" rx="10" fill="{c}"/>')
    rs += [rot(x - 40, base - v * esc - 56, f"≈ {v}% ao ano", w=300, tam=30, cor=c, peso=700, alinha="center", serif=True),
           rot(x - 40, base + 10, t, w=300, tam=24, cor=TINTA, peso=700, alinha="center")]
p.append(f'<line x1="40" y1="{base}" x2="760" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
rs.append(rot(820, 0, "3×", w=300, tam=120, cor=FOSF, peso=700, serif=True))
rs.append(rot(820, 160, "cerca de 3% de força contra 1% de massa por ano", w=844, tam=32, cor=TINTA, peso=700, serif=True, lh=1.2))
p.append(caixa(820, 290, 844, 150, OXID, OXID_T, esp=3, rx=16))
rs.append(rot(844, 310, "Quem ganhou massa no período não manteve a força por isso. A potência cai mais depressa ainda.", w=796, tam=26, cor=TINTA, peso=600, lh=1.3))
diagrama(S, "tres", 440, p, rs, eyebrow="Estudo de 2006, 1.880 pessoas na casa dos setenta, três anos", titulo="A força cai três vezes mais rápido que a massa",
         fonte="J Gerontol A Biol Sci Med Sci 2006")

# 5. a tendência
p = [svg_abre(1664, 440, "Duas réguas. Em cima, os pontos de corte feitos para o idoso frágil, com o corredor muito acima. Embaixo, a curva do corredor em dois anos: 46 caindo para 40 kg, menos 13%, contra cerca de 6% esperado. No ativo, o valor está na tendência"), defs(FOSF)]
rs = []
p.append(f'<rect x="0" y="40" width="1100" height="24" rx="12" fill="{GRADE}"/>')
p.append(f'<rect x="0" y="40" width="{27 * 18}" height="24" rx="12" fill="{FOSF_T}"/>')
p.append(f'<line x1="{27 * 18}" y1="20" x2="{27 * 18}" y2="84" stroke="{FOSF}" stroke-width="5"/>')
for v in (40, 46):
    p.append(f'<circle cx="{v * 18}" cy="52" r="16" fill="{AZUL if v == 46 else GLIC}"/>')
rs += [rot(0, 96, "corte para o idoso frágil: 27 kg", w=700, tam=24, cor=FOSF, peso=700),
       rot(600, 96, "o corredor: 40 e 46 kg, muito acima", w=500, tam=24, cor=AZUL, peso=700, alinha="right")]
pts = [(140, 230), (440, 270), (740, 320)]
p.append(f'<path d="M 140 230 L 440 270 L 740 320" stroke="{FOSF}" stroke-width="6" fill="none"/>')
p.append(f'<path d="M 140 230 L 740 258" stroke="{MUDO}" stroke-width="4" stroke-dasharray="10 8" fill="none"/>')
for x, y in pts:
    p.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{FOSF}"/>')
p.append(f'<line x1="80" y1="380" x2="800" y2="380" stroke="{TINTA}" stroke-width="3"/>')
rs += [rot(60, 186, "46 kg", w=160, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(680, 330, "40 kg", w=160, tam=26, cor=TINTA, peso=700, alinha="center"),
       rot(780, 236, "esperado: ≈ −6%", w=260, tam=22, cor=MUDO, peso=600),
       rot(80, 392, "dois anos", w=720, tam=22, cor=MUDO, alinha="center")]
p.append(caixa(1140, 150, 524, 290, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1164, 170, "−13%", w=476, tam=56, cor=FOSF, peso=700, serif=True),
       rot(1164, 260, "No ativo, o valor está na tendência: medir com data a cada 6 a 12 meses e olhar a inclinação.", w=476, tam=24, cor=TINTA, peso=600, lh=1.3)]
diagrama(S, "tendencia", 440, p, rs, eyebrow="No atleta que envelhece", titulo="No ativo, a queda importa mais que o ponto de corte")

# 6. resistência anabólica
p = [svg_abre(1664, 440, "Curvas de síntese de proteína muscular em resposta à dose: a do jovem e a do mais velho, deslocada para a direita, que ainda sobe com doses maiores. Inatividade empurra mais para a direita; treino de força puxa de volta"), defs(FOSF, OXID)]
rs = []
x0, base = 60, 400
p.append(f'<line x1="{x0}" y1="{base}" x2="1000" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="20" x2="{x0}" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M {x0} 380 C 200 200 300 100 420 90 L 1000 86" stroke="{OXID}" stroke-width="7" fill="none"/>')
p.append(f'<path d="M {x0} 390 C 360 340 520 170 700 120 L 1000 110" stroke="{GLIC}" stroke-width="7" fill="none"/>')
rs += [rot(250, 44, "jovem", w=200, tam=26, cor=OXID, peso=700), rot(720, 150, "mais velho", w=240, tam=26, cor=GLIC, peso=700),
       rot(x0 + 10, 408, "dose de proteína por refeição", w=600, tam=22, cor=MUDO),
       rot(x0 + 16, 10, "resposta", w=200, tam=22, cor=MUDO), rot(780, 360, "esquema", w=200, tam=22, cor=MUDO, alinha="right")]
p.append(caixa(1080, 0, 584, 200, FOSF, FOSF_T, esp=3, rx=16))
p.append(seta(1110, 60, 1200, 60, FOSF, "m0", 5))
rs.append(rot(1216, 24, "inatividade empurra a curva mais para a direita", w=430, tam=26, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(1080, 240, 584, 200, OXID, OXID_T, esp=3, rx=16))
p.append(seta(1200, 300, 1110, 300, OXID, "m1", 5))
rs.append(rot(1216, 264, "treino de força puxa de volta: a comida volta a funcionar", w=430, tam=26, cor=TINTA, peso=700, lh=1.25))
diagrama(S, "resistencia", 440, p, rs, eyebrow="Resistência anabólica", titulo="A curva se desloca com a idade, mas não desaparece")

# 7. noventa anos
p = [svg_abre(1664, 440, "Ensaio de 1990: dez moradores de instituição de longa permanência, média de 90 anos, até 96, oito semanas de treino de força com carga alta. Ganhos: força +174%, área muscular da coxa +9%, velocidade de marcha em linha +48%")]
rs = []
p.append(caixa(0, 0, 480, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(24, 24, "Ensaio de 1990", w=432, tam=28, cor=AZUL, peso=700, serif=True),
       rot(24, 96, "10 moradores de instituição", w=432, tam=26, cor=TINTA, peso=600),
       rot(24, 150, "média de 90 anos, até 96", w=432, tam=26, cor=TINTA, peso=600),
       rot(24, 204, "8 semanas de força com carga alta", w=432, tam=26, cor=TINTA, peso=600, lh=1.25),
       rot(24, 330, "pequeno, sem grupo controle: vale a direção", w=432, tam=22, cor=MUDO, peso=600, lh=1.25)]
base = 380
for k, (v, t, c) in enumerate([(174, "força", FOSF), (9, "área muscular da coxa", GLIC), (48, "marcha em linha", OXID)]):
    x = 600 + k * 360
    h = v * 1.6
    p.append(f'<rect x="{x}" y="{base - h:.0f}" width="220" height="{h:.0f}" rx="10" fill="{c}"/>')
    rs += [rot(x - 40, base - h - 56, f"+{v}%", w=300, tam=36, cor=c, peso=700, alinha="center", serif=True),
           rot(x - 40, base + 10, t, w=300, tam=24, cor=TINTA, peso=700, alinha="center")]
p.append(f'<line x1="560" y1="{base}" x2="1664" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
diagrama(S, "noventa", 440, p, rs, eyebrow="O segundo número", titulo="Aos noventa anos, o músculo ainda responde à carga",
         fonte="JAMA 1990")

# 8. o que o corredor precisa
p = [svg_abre(1664, 440, "O corredor. O que a corrida mantém: coração, capacidade aeróbia, peso. O que não mantém: força, potência, massa da perna, levantar do chão. Embaixo: exercício é a atividade; treino é a atividade com sobrecarga que progride")]
rs = []
p.append(corredor(700, 20, 260, AZUL))
for k, (t, itens, c, f) in enumerate([("A corrida mantém", ["coração", "capacidade aeróbia", "peso e humor"], OXID, OXID_T),
                                      ("A corrida não mantém", ["força", "potência", "levantar do chão"], FOSF, FOSF_T)]):
    x = 0 if k == 0 else 1064
    p.append(caixa(x, 0, 600, 280, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 20, t, w=552, tam=28, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 24, 90 + j * 56, "· " + it, w=552, tam=26, cor=TINTA, peso=600))
for k, (t, x_t, c) in enumerate([("exercício", "a atividade", MUDO), ("treino", "a atividade com sobrecarga que progride", OXID)]):
    x = k * 832
    p.append(caixa(x, 310, 812, 130, c, CARTAO, esp=3, rx=16))
    rs += [rot(x + 24, 330, t, w=764, tam=32, cor=c, peso=700, serif=True), rot(x + 24, 384, x_t, w=764, tam=24, cor=TINTA, peso=600)]
diagrama(S, "corrida", 440, p, rs, eyebrow="De volta ao corredor", titulo="Correr não substitui força: falta o que progride")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Sarcopenia e exercício como contramedida", "titulo": "Força medida com data e carga que progride",
          "regras": ["A força cai cerca de três vezes mais rápido que a massa",
                     "No atleta ativo, vale a tendência da força, não o ponto de corte do idoso frágil",
                     "O músculo responde a carga em qualquer idade; trava sem progressão"],
          "cards": [{"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Medem preensão, sentar e levantar e marcha, com data, e olham a inclinação."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Acrescenta força e potência ao que o esporte não entrega, com progressão registrada."},
                    {"ic": "t:salad", "t": "Nutrição", "x": "Ajusta a proteína por refeição ao músculo que envelhece."}]})

salvar("12-07.json", {"arquivo": "aulas/MOD12/12-07-sarcopenia-e-exercicio-como-contramedida.md",
                      "titulo": "Sarcopenia e exercício como contramedida", "subtitulo": "A força cai três vezes mais rápido que a massa",
                      "nota_capa": "Entra por um corredor na casa dos sessenta com a balança normal e a força caindo.",
                      "secoes": {"corredor": ["O caso e a definição.", "capa"], "tres": ["O número.", "tres"],
                                 "resistencia": ["Por que rende menos.", "resistencia"], "noventa": ["A contramedida.", "noventa"]},
                      "slides": S})
