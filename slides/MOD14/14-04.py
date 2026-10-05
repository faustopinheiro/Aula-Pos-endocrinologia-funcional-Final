"""Spec do deck 14.4. Gera 14-04.json ao lado deste arquivo."""
from _base import *

S = []

def barco(x, y, w, cor):
    """Barco de remo individual visto de lado, com a remadora e os remos."""
    return (f'<path d="M {x} {y} Q {x + w / 2} {y + 40} {x + w} {y} Z" fill="{cor}"/>'
            f'<circle cx="{x + w * 0.5:.0f}" cy="{y - 70}" r="18" fill="{TINTA}"/>'
            f'<path d="M {x + w * 0.5:.0f} {y - 52} L {x + w * 0.46:.0f} {y - 4}" stroke="{TINTA}" stroke-width="16" stroke-linecap="round"/>'
            f'<line x1="{x + w * 0.2:.0f}" y1="{y + 30}" x2="{x + w * 0.62:.0f}" y2="{y - 40}" stroke="{MUDO}" stroke-width="6"/>')

# 1. o barco
p = [svg_abre(1664, 440, "Remadora de seleção no barco individual, com a costela marcada: fratura por estresse de costela. Marcas: categoria peso leve; treina duas vezes por dia; ciclo irregular há um ano, que só apareceu quando perguntado. Seletiva em oito semanas. Perfil típico")]
rs = []
p.append(f'<rect x="0" y="300" width="760" height="140" fill="{AZUL_T}"/>')
p.append(barco(80, 300, 600, AZUL))
p.append(f'<circle cx="378" cy="236" r="22" fill="none" stroke="{FOSF}" stroke-width="6"/>')
rs += [rot(420, 160, "fratura por estresse de costela", w=320, tam=24, cor=FOSF, peso=700, lh=1.2),
       rot(0, 400, "perfil típico", w=300, tam=20, cor=MUDO)]
for j, (t, c) in enumerate([("categoria peso leve", AZUL), ("treina duas vezes por dia", TINTA), ("ciclo irregular há um ano: só apareceu quando perguntado", FOSF)]):
    y = j * 100
    p.append(caixa(820, y, 520, 80, c, CARTAO, esp=3, rx=14))
    rs.append(rot(844, y + 14, t, w=472, tam=22, cor=c, peso=700, lh=1.2))
p.append(caixa(1380, 0, 284, 280, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:calendar", 1490, 24, 64, GLIC))
rs += [rot(1400, 100, "8", w=244, tam=72, cor=GLIC, peso=700, serif=True, alinha="center"),
       rot(1400, 200, "semanas até a seletiva", w=244, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.2)]
rs.append(rot(820, 330, "Seis áreas, seis critérios de retorno.", w=844, tam=30, cor=TINTA, peso=700, serif=True))
diagrama(S, "barco", 440, p, rs, eyebrow="Remo peso leve, uma remadora na casa dos vinte", titulo="Uma costela quebrada, uma seletiva em oito semanas e um ciclo que ninguém perguntou")

# 2. as três saídas
p = [svg_abre(1664, 440, "Três saídas. A: volta quando a costela consolidar. B: só volta quando tudo normalizar, inclusive o ciclo. C: volta em degraus, com a energia como condição de cada degrau, num acordo escrito. Pergunta: o que decide o caminho?")]
rs = []
for j, (l, t, c, f) in enumerate([("A", "volta quando a costela consolidar", GLIC, GLIC_T),
                                   ("B", "só volta quando tudo normalizar, inclusive o ciclo", FOSF, FOSF_T),
                                   ("C", "volta em degraus, com a energia como condição de cada degrau, num acordo escrito", OXID, OXID_T)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 320, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 268}" cy="80" r="50" fill="{c}"/>')
    rs += [rot(x + 218, 52, l, w=100, tam=48, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(x + 28, 160, t, w=480, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Antes de escolher: o que cada área está olhando", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saidas", 440, p, rs, eyebrow="A encruzilhada", titulo="Três jeitos de decidir a mesma volta ao barco")

# 3. seis critérios
p = [svg_abre(1664, 460, "Seis critérios de retorno em volta da remadora. Medicina: dor e consolidação. Fisioterapia: remar sem dor no ergômetro. Nutrição: disponibilidade de energia adequada. Ginecologia e endocrinologia: o ciclo. Técnico: a seletiva e o limite de peso. A atleta: a vaga. Velocidades diferentes: semanas para a costela, muitos meses para o ciclo")]
rs = []
for j, (q, c_, c) in enumerate([("Medicina", "dor e consolidação", AZUL), ("Fisioterapia", "remar sem dor no ergômetro", OXID),
                                ("Nutrição", "disponibilidade de energia adequada", GLIC), ("Ginecologia e endocrinologia", "o ciclo", FOSF),
                                ("Técnico", "a seletiva e o limite de peso", MUDO), ("A atleta", "a vaga", TINTA)]):
    x, y = (j % 3) * 560, (j // 3) * 150
    p.append(caixa(x, y, 530, 130, c, CARTAO, esp=3, rx=16))
    rs += [rot(x + 24, y + 14, q, w=482, tam=24, cor=c, peso=700, serif=True), rot(x + 24, y + 62, c_, w=482, tam=24, cor=TINTA, peso=700)]
X0, X1, Y = 200, 1500, 380
p.append(f'<line x1="{X0}" y1="{Y}" x2="{X1}" y2="{Y}" stroke="{TINTA}" stroke-width="3"/>')
for x, t, c in [(420, "costela: semanas", AZUL), (900, "seletiva: 8 semanas", MUDO), (1440, "ciclo: muitos meses", FOSF)]:
    p.append(f'<circle cx="{x}" cy="{Y}" r="14" fill="{c}"/>')
    rs.append(rot(x - 150, Y + 22, t, w=300, tam=22, cor=c, peso=700, alinha="center"))
rs.append(rot(0, Y - 14, "tempo", w=180, tam=20, cor=MUDO, peso=700, alinha="right"))
diagrama(S, "criterios", 460, p, rs, eyebrow="Seis critérios", titulo="Cada área tem um critério legítimo, e eles andam em velocidades diferentes")

# 4. o semáforo
p = [svg_abre(1664, 440, "Semáforo de quatro cores da ferramenta clínica do COI de 2023. Verde: participação plena. Amarelo: segue, com monitoramento. Laranja: intervenção médica intensiva e monitoramento. Vermelho: considerar afastar de treino e competição. Fratura por estresse com ciclo irregular: já não é verde; a cor final é da medicina, com os outros indicadores")]
rs = []
for j, (t, x_, c) in enumerate([("verde", "participação plena", OXID), ("amarelo", "segue, com monitoramento", GLIC),
                                ("laranja", "intervenção médica intensiva e monitoramento", "#D9772B"), ("vermelho", "considerar afastar de treino e competição", FOSF)]):
    y = j * 108
    p.append(f'<circle cx="50" cy="{y + 46}" r="40" fill="{c}"/>')
    rs += [rot(110, y + 14, t, w=200, tam=26, cor=c if c != GLIC else TINTA, peso=700, serif=True),
           rot(110, y + 52, x_, w=760, tam=24, cor=TINTA, peso=700)]
p.append(caixa(960, 0, 704, 440, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(984, 24, "Fratura por estresse + ciclo irregular", w=656, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2),
       rot(984, 120, "já não está no verde", w=656, tam=26, cor=TINTA, peso=700),
       rot(984, 190, "a cor final depende dos outros indicadores, e quem define é a medicina", w=656, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(984, 320, "o retorno vira pergunta sobre a atleta inteira, e não sobre o osso", w=656, tam=26, cor=FOSF, peso=700, serif=True, lh=1.25)]
diagrama(S, "semaforo", 440, p, rs, eyebrow="A ferramenta que organiza a conversa", titulo="O semáforo de 2023 classifica o risco da atleta, e não só o osso",
         fonte="Br J Sports Med 2023")

# 5. saída A
p = [svg_abre(1664, 420, "Saída A: a costela consolidada, com visto. Continua igual: o déficit de energia, o ciclo, o limite de peso. Uma seta para um segundo osso: a próxima fratura, em outro lugar. Trata o osso, não a causa"), defs(FOSF)]
rs = []
p.append(caixa(0, 40, 420, 260, OXID, OXID_T, esp=3, rx=18))
p.append(f'<path d="M 60 170 Q 210 90 360 170" stroke="{TINTA}" stroke-width="18" fill="none" stroke-linecap="round"/>')
p.append(f'<circle cx="340" cy="90" r="26" fill="{OXID}"/>')
p.append(f'<path d="M 328 90 L 337 100 L 354 80" stroke="{PAPEL}" stroke-width="5" fill="none"/>')
rs.append(rot(20, 220, "costela consolidada", w=380, tam=26, cor=OXID, peso=700, serif=True, alinha="center"))
for j, t in enumerate(["o déficit de energia", "o ciclo irregular", "o limite de peso"]):
    y = 40 + j * 90
    p.append(caixa(480, y, 460, 70, MUDO, CARTAO, esp=2, rx=12))
    rs.append(rot(500, y + 18, t, w=420, tam=24, cor=TINTA, peso=700))
rs.append(rot(480, 0, "continua igual", w=460, tam=22, cor=MUDO, peso=700))
p.append(seta(960, 170, 1080, 170, FOSF, "m0", esp=6))
p.append(caixa(1100, 40, 564, 260, FOSF, FOSF_T, esp=3, rx=18))
p.append(f'<path d="M 1180 200 L 1600 200" stroke="{TINTA}" stroke-width="22" stroke-linecap="round"/>')
p.append(f'<path d="M 1380 180 L 1395 200 L 1382 220" stroke="{FOSF}" stroke-width="6" fill="none"/>')
rs += [rot(1120, 70, "a próxima fratura, em outro osso", w=524, tam=26, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(0, 350, "Liberar pela consolidação responde à pergunta mais fácil do caso.", w=1664, tam=28, cor=TINTA, peso=700, serif=True, alinha="center")]
diagrama(S, "saida_a", 420, p, rs, eyebrow="Saída A · volta quando a costela consolidar", titulo="A saída A trata o osso e devolve a atleta à causa")

# 6. saída B
p = [svg_abre(1664, 420, "Saída B: esperar o ciclo voltar, o que pode levar muitos meses. Consequências: perde a seletiva e talvez a carreira; esconde sintomas na próxima vez; o afastamento total pesa no humor. Protege no papel. O semáforo prevê afastamento no vermelho")]
rs = []
p.append(caixa(0, 0, 440, 320, FOSF, FOSF_T, esp=3, rx=18))
p.append(f'<circle cx="220" cy="130" r="80" fill="{CARTAO}" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M 220 130 L 220 75 M 220 130 L 260 150" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>')
rs.append(rot(20, 230, "esperar o ciclo voltar: pode levar muitos meses", w=400, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2))
for j, t in enumerate(["perde a seletiva, e talvez a carreira", "aprende a esconder o próximo sintoma", "o afastamento total pesa no humor e no vínculo"]):
    x = 500 + j * 392
    p.append(caixa(x, 0, 370, 320, MUDO, CARTAO, esp=2, rx=16))
    p.append(icone("t:x", x + 24, 24, 44, FOSF))
    rs.append(rot(x + 24, 100, t, w=322, tam=26, cor=TINTA, peso=700, lh=1.3))
rs.append(rot(0, 360, "Protege no papel. O semáforo prevê afastamento no vermelho, não como regra para todos.", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"))
diagrama(S, "saida_b", 420, p, rs, eyebrow="Saída B · só volta quando tudo normalizar", titulo="Esperar tudo normalizar ensina a atleta a esconder o próximo sintoma")

# 7. saída C
p = [svg_abre(1664, 460, "Saída C, uma escada: ergômetro leve sem dor; barco em volume baixo; volume e intensidade sobem; decisão sobre a seletiva na data marcada. Em cada degrau, as mesmas três condições: sem dor na costela, plano alimentar cumprido, peso estável sem queda. Acordo escrito")]
rs = []
for j, t in enumerate(["ergômetro leve, sem dor", "barco, volume baixo", "volume e intensidade sobem", "decisão sobre a seletiva, na data"]):
    x, y = j * 270, 300 - j * 80
    p.append(caixa(x, y, 250, 460 - y, OXID, OXID_T if j < 3 else GLIC_T, esp=3, rx=14))
    rs.append(rot(x + 16, y + 16, t, w=218, tam=22, cor=TINTA, peso=700, lh=1.2))
p.append(caixa(1120, 0, 544, 300, OXID, CARTAO, esp=3, rx=18))
rs.append(rot(1144, 20, "Em cada degrau, as mesmas condições", w=496, tam=26, cor=OXID, peso=700, serif=True, lh=1.2))
for j, t in enumerate(["sem dor na costela", "plano alimentar cumprido", "peso estável, sem queda"]):
    p.append(f'<circle cx="1160" cy="{140 + j * 52}" r="12" fill="{OXID}"/>')
    rs.append(rot(1184, 126 + j * 52, t, w=456, tam=24, cor=TINTA, peso=700))
p.append(caixa(1120, 330, 544, 130, TINTA, TINTA, esp=0, rx=18))
p.append(icone("t:pencil", 1144, 362, 56, PAPEL))
rs += [rot(1216, 350, "acordo escrito, apresentado pelo médico da equipe", w=424, tam=24, cor=PAPEL, peso=700, lh=1.25),
       rot(0, 120, "uma condição falha: o degrau não sobe", w=700, tam=24, cor=FOSF, peso=700)]
diagrama(S, "saida_c", 460, p, rs, eyebrow="Saída C · em degraus, com acordo escrito", titulo="Cada degrau sobe com as mesmas três condições, e não só com a costela",
         fonte="Br J Sports Med 2014")

# 8. a pergunta difícil
p = [svg_abre(1664, 420, "A pergunta difícil: a categoria peso leve ainda serve para ela? Três vozes: a atleta, é a minha categoria; a nutrição, o peso que o corpo sustenta com energia adequada; a psicologia, o que essa categoria significa para ela. Decisão dela, com informação e com tempo")]
rs = []
p.append(caixa(0, 0, 1664, 120, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(24, 30, "“A categoria peso leve ainda serve para ela?”", w=1616, tam=36, cor=FOSF, peso=700, serif=True, alinha="center"))
for j, (q, t, c, ic) in enumerate([("a atleta", "“é a minha categoria”", TINTA, "t:user"), ("a nutrição", "o peso que o corpo sustenta com energia adequada", OXID, "t:apple"),
                                   ("a psicologia", "o que essa categoria significa para ela, e o que ela custa", GLIC, "t:brain")]):
    x = j * 564
    p.append(caixa(x, 150, 536, 190, c, CARTAO, esp=3, rx=16))
    p.append(icone(ic, x + 24, 170, 44, c))
    rs += [rot(x + 84, 178, q, w=428, tam=24, cor=c, peso=700, serif=True), rot(x + 24, 236, t, w=488, tam=24, cor=TINTA, peso=700, lh=1.25)]
rs.append(rot(0, 372, "Decisão dela, com informação e com tempo; o acordo pode marcar a data da conversa.", w=1664, tam=26, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "categoria", 420, p, rs, eyebrow="A pergunta difícil", titulo="A categoria é decisão da atleta, com informação e com tempo")

# 9. quem coordena
p = [svg_abre(1664, 420, "Quem coordena conforme a cor. Verde e amarelo: quem treina coordena o dia a dia, com a medicina monitorando. Laranja e vermelho: a medicina coordena; o técnico participa do plano e não decide sozinho. O acordo é assinado por médico, atleta, técnico e nutrição")]
rs = []
for j, (cores, t, x_, c) in enumerate([((OXID, GLIC), "verde e amarelo", "quem treina coordena o dia a dia, com a medicina monitorando", OXID),
                                       (("#D9772B", FOSF), "laranja e vermelho", "a medicina coordena; o técnico participa do plano, e não decide sozinho", FOSF)]):
    x = j * 846
    p.append(caixa(x, 0, 818, 260, c, CARTAO, esp=3, rx=18))
    for k, cc in enumerate(cores):
        p.append(f'<circle cx="{x + 50 + k * 70}" cy="60" r="28" fill="{cc}"/>')
    rs += [rot(x + 200, 40, t, w=590, tam=28, cor=TINTA, peso=700, serif=True), rot(x + 24, 120, x_, w=770, tam=26, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(0, 300, 1664, 120, TINTA, TINTA, esp=0, rx=18))
p.append(icone("t:pencil", 24, 332, 56, PAPEL))
rs.append(rot(100, 326, "o acordo é assinado por médico, atleta, técnico e nutrição; tira do técnico a posição de quem diz não", w=1540, tam=24, cor=PAPEL, peso=700, lh=1.3))
diagrama(S, "coordena", 420, p, rs, eyebrow="Quem coordena", titulo="A cor do semáforo define quem coordena o retorno")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Caso integrado: fratura por estresse", "titulo": "Voltar a atleta inteira, e não só o osso",
          "regras": ["A pergunta do retorno é sobre o risco da atleta, não sobre o osso",
                     "Degraus com as mesmas condições: sem dor, plano alimentar, peso estável",
                     "Tudo num acordo escrito, que a atleta assina sabendo as regras"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Define a cor, coordena no laranja e no vermelho e apresenta o acordo."},
                    {"ic": "t:users", "t": "Nutrição, fisioterapia e quem treina", "x": "Conduzem os degraus e checam as condições."},
                    {"ic": "t:user", "t": "A atleta", "x": "Participa da decisão sobre a categoria, com tempo e informação."}]})

salvar("14-04.json", {"arquivo": "aulas/MOD14/14-04-caso-integrado-atleta-mulher-com-fratura-por-estresse.md",
                      "titulo": "Caso integrado 4: atleta mulher com fratura por estresse", "subtitulo": "Três saídas para a volta ao barco",
                      "nota_capa": "Entra por uma remadora peso leve com fratura de costela e uma seletiva em oito semanas.",
                      "secoes": {"barco": ["A decisão.", "capa"], "criterios": ["Os critérios e a ferramenta.", "criterios"],
                                 "saida_a": ["As três saídas.", "saida_a"], "categoria": ["A categoria e a coordenação.", "categoria"]},
                      "slides": S})
