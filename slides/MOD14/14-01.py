"""Spec do deck 14.1. Gera 14-01.json ao lado deste arquivo."""
from _base import *

S = []

# 1. a linha do tempo
p = [svg_abre(1664, 440, "Linha do tempo de doze meses, meses ilustrativos. Mês 1: dor abaixo da patela na pré-temporada. Mês 3: jogos duas vezes por semana, anti-inflamatório e gelo. Mês 5: afastada três semanas. Mês 6: volta. Mês 7: convocada para a seleção. Mês 8: volta pior, afastada de novo. Seis profissões, cada uma com um visto: cada área fez a sua parte")]
rs = []
for j, ic in enumerate(["h:doctor", "t:first-aid-kit", "t:barbell", "t:clipboard-list", "t:flag", "t:user"]):
    x = j * 96
    p.append(icone(ic, x, 0, 56, TINTA))
    p.append(f'<circle cx="{x + 56}" cy="56" r="14" fill="{OXID}"/>')
    p.append(f'<path d="M {x + 49} 56 L {x + 54} 62 L {x + 64} 50" stroke="{PAPEL}" stroke-width="4" fill="none"/>')
rs.append(rot(600, 14, "cada área fez a sua parte", w=600, tam=28, cor=OXID, peso=700, serif=True))
p.append(icone("t:ball-volleyball", 1580, 0, 72, AZUL))
Y = 260
tl, xs = linha_do_tempo(60, 1600, Y, 12, TINTA)
p.append(tl)
p.append(f'<line x1="{xs[7]:.0f}" y1="{Y}" x2="{xs[11]:.0f}" y2="{Y}" stroke="{PAPEL}" stroke-width="6"/>')
p.append(f'<line x1="{xs[7]:.0f}" y1="{Y}" x2="{xs[11]:.0f}" y2="{Y}" stroke="{MUDO}" stroke-width="4"{TRACO}/>')
for m, t, c, cima in [(1, "dor abaixo da patela", AZUL, True), (3, "jogos 2× por semana: anti-inflamatório e gelo", AZUL, False),
                      (5, "afastada três semanas", FOSF, True), (6, "volta", AZUL, False),
                      (7, "convocada para a seleção", AZUL, True), (8, "volta pior: afastada de novo", FOSF, False)]:
    x = xs[m - 1]
    p.append(f'<circle cx="{x:.0f}" cy="{Y}" r="16" fill="{c}"/>')
    w = 160 if m == 6 else 250
    rs.append(rot(max(0, x - w / 2), Y - 110 if cima else Y + 34, t, w=w, tam=22, cor=c, peso=700, alinha="center", lh=1.2))
rs += [rot(0, Y + 150, "mês 1", w=120, tam=20, cor=MUDO, peso=700),
       rot(xs[11] - 100, Y + 34, "mês 12", w=120, tam=20, cor=MUDO, peso=700, alinha="right"),
       rot(xs[9] - 120, Y - 70, "o resto, no fim da conversa", w=300, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(1100, Y + 150, "meses ilustrativos", w=500, tam=20, cor=MUDO, alinha="right")]
diagrama(S, "linha", 440, p, rs, eyebrow="Vôlei profissional, uma oposta na casa dos vinte", titulo="Cada área fez a sua parte, e a dor voltou duas vezes")

# 2. o tamanho do problema
p = [svg_abre(1664, 420, "Dor atual no tendão patelar em atletas de elite, estudo norueguês de 2005 com 613 atletas de nove modalidades: vôlei 44,6%; basquete 31,9%; média geral 14,2%; ciclismo e orientação, nenhum caso. A meta realista: a dor não decide quem joga")]
rs = []
X0, K = 330, 16
for j, (t, v, c) in enumerate([("vôlei", 44.6, FOSF), ("basquete", 31.9, GLIC), ("média das nove", 14.2, MUDO), ("ciclismo e orientação", 0, AZUL)]):
    y = 20 + j * 96
    rs.append(rot(0, y + 18, t, w=310, tam=26, cor=TINTA, peso=700, alinha="right"))
    if v:
        p.append(f'<rect x="{X0}" y="{y}" width="{v * K:.0f}" height="70" rx="10" fill="{c}"/>')
    rs.append(rot(X0 + v * K + 16, y + 12, f"{v:.1f}%".replace(".", ",") if v else "nenhum caso", w=220, tam=32, cor=c, peso=700, serif=True))
rs.append(rot(0, 396 - 6, "613 atletas de elite, nove modalidades, 2005", w=1000, tam=20, cor=MUDO, peso=700))
p.append(caixa(1180, 20, 484, 360, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1204, 44, "A meta realista", w=436, tam=28, cor=OXID, peso=700, serif=True),
       rot(1204, 110, "não é uma temporada sem dor", w=436, tam=26, cor=TINTA, peso=700, lh=1.25),
       rot(1204, 220, "é uma temporada em que a dor não decide quem joga", w=436, tam=28, cor=OXID, peso=700, serif=True, lh=1.25)]
diagrama(S, "tamanho", 420, p, rs, eyebrow="O tamanho do problema", titulo="No vôlei de elite, quase metade tem o tendão patelar doendo agora",
         fonte="Am J Sports Med 2005")

# 3. a reunião que não aconteceu
p = [svg_abre(1664, 460, "Mesa com seis cadeiras. Medicina: tendinopatia, sem ruptura. Fisioterapia: melhora na clínica com carga pesada e lenta. Preparação física: saltos no treino de força. Técnico: saltos no treino de quadra, sem contagem. Seleção: outra equipe, outro plano. A atleta: não conta a dor para não perder a vaga. No centro, um joelho em seis pedaços")]
rs = []
CX, CY, R = 832, 230, 120
cores = [AZUL, OXID, GLIC, FOSF, MUDO, TINTA]
for k in range(6):
    a0, a1 = math.radians(k * 60 - 90 + 3), math.radians(k * 60 - 30 - 3)
    x0, y0, x1, y1 = CX + R * math.cos(a0), CY + R * math.sin(a0), CX + R * math.cos(a1), CY + R * math.sin(a1)
    p.append(f'<path d="M {CX} {CY} L {x0:.0f} {y0:.0f} A {R} {R} 0 0 1 {x1:.0f} {y1:.0f} Z" fill="{cores[k]}" opacity="0.85"/>')
rs.append(rot(CX - 160, CY + R + 20, "o mesmo joelho", w=320, tam=24, cor=TINTA, peso=700, serif=True, alinha="center"))
for j, (t, x_, c) in enumerate([("Medicina", "tendinopatia, sem ruptura", AZUL), ("Fisioterapia", "melhora na clínica com carga pesada e lenta", OXID),
                                ("Preparação física", "saltos no treino de força", GLIC), ("Técnico", "saltos de quadra: ninguém contava", FOSF),
                                ("Seleção", "outra equipe, outro plano", MUDO), ("A atleta", "não conta a dor, para não perder a vaga", TINTA)]):
    x = 0 if j < 3 else 1104
    y = (j % 3) * 156
    p.append(caixa(x, y, 560, 136, c, CARTAO, esp=3, rx=16))
    rs += [rot(x + 24, y + 14, t, w=512, tam=26, cor=c, peso=700, serif=True),
           rot(x + 24, y + 60, x_, w=512, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "mesa", 460, p, rs, eyebrow="A reunião que não aconteceu", titulo="Seis pessoas viam pedaços diferentes do mesmo joelho")

# 4. as passagens
p = [svg_abre(1664, 440, "Três passagens como pontes quebradas. Da clínica para a quadra: a carga controlada na clínica, solta no treino. Do clube para a seleção: o plano não viajou. Da atleta para a equipe: a dor escondida. Nos momentos em que a dor voltou, havia uma passagem sem dono")]
rs = []
for j, (t, x_) in enumerate([("da clínica para a quadra", "carga controlada na clínica, solta no treino"),
                             ("do clube para a seleção", "o plano ficou no clube"),
                             ("da atleta para a equipe", "a dor existia e não era dita")]):
    x = j * 564
    p.append(f'<rect x="{x + 20}" y="80" width="90" height="170" rx="8" fill="{MUDO}"/>')
    p.append(f'<rect x="{x + 426}" y="80" width="90" height="170" rx="8" fill="{MUDO}"/>')
    p.append(f'<path d="M {x + 20} 80 L {x + 230} 80 L {x + 246} 110 L {x + 20} 110 Z" fill="{TINTA}"/>')
    p.append(f'<path d="M {x + 290} 80 L {x + 516} 80 L {x + 516} 110 L {x + 306} 110 Z" fill="{TINTA}"/>')
    p.append(f'<path d="M {x + 252} 120 L {x + 262} 160 M {x + 280} 124 L {x + 272} 170" stroke="{FOSF}" stroke-width="5"/>')
    rs += [rot(x, 10, t, w=536, tam=26, cor=FOSF, peso=700, serif=True, alinha="center"),
           rot(x + 20, 270, x_, w=496, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.25)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Nos momentos em que a dor voltou, havia uma passagem sem dono.", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "passagens", 440, p, rs, eyebrow="Onde o caso quebrou", titulo="A dor voltou nas passagens entre as áreas")

# 5. contar saltos
p = [svg_abre(1664, 470, "Carga semanal de saltos no eixo horizontal e probabilidade de queixa no joelho no vertical: curva quase plana, faixa larga de incerteza. 65 jogadores, 102 temporadas de jogador, vôlei masculino de elite, coorte de 2024. Contar saltos é útil para conversar e não basta como regra sozinho")]
rs = []
X0, X1, Y0, Y1 = 60, 960, 380, 40
p.append(f'<line x1="{X0}" y1="{Y0}" x2="{X1}" y2="{Y0}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M {X0} 150 C 300 120 600 110 {X1} 140 L {X1} 320 C 600 300 300 290 {X0} 330 Z" fill="{AZUL_T}"/>')
p.append(f'<path d="M {X0} 240 C 300 215 600 205 {X1} 230" stroke="{AZUL}" stroke-width="6" fill="none"/>')
rs += [rot(X0, Y0 + 10, "saltos por semana", w=X1 - X0, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(X0 + 16, Y1 - 30, "chance de queixa no joelho", w=500, tam=22, cor=MUDO, peso=700),
       rot(X0 + 300, 160, "faixa de incerteza larga", w=360, tam=22, cor=AZUL, peso=700, alinha="center"),
       rot(X0, 436, "esquema da forma do resultado, sem os valores", w=X1 - X0, tam=20, cor=MUDO)]
p.append(caixa(1040, 0, 624, 100, MUDO, CARTAO, esp=2, rx=14))
rs.append(rot(1064, 16, "65 jogadores · 102 temporadas · vôlei masculino de elite", w=576, tam=22, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(1040, 130, 624, 130, OXID, OXID_T, esp=3, rx=16))
rs.append(rot(1064, 152, "Contar saltos: útil para a conversa entre as áreas", w=576, tam=26, cor=OXID, peso=700, lh=1.25))
p.append(caixa(1040, 290, 624, 150, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1064, 312, "Teto de saltos sozinho: não é a regra do dia; a régua é o próprio tendão", w=576, tam=24, cor=FOSF, peso=700, lh=1.25))
diagrama(S, "saltos", 470, p, rs, eyebrow="A tentação de resolver com um número", titulo="O estudo não achou relação clara entre saltos por semana e dor no joelho",
         fonte="Scand J Med Sci Sports 2024")

# 6. os três degraus
p = [svg_abre(1664, 440, "Três degraus em sequência. Um, como está o tecido: medicina e fisioterapia. Dois, o que a semana vai pedir: preparação física e técnico. Três, quanto risco aceitar: atleta, técnico e clube. A ordem das perguntas define quem fala primeiro; quando o calendário fala primeiro, a avaliação vira justificativa"), defs(TINTA)]
rs = []
for j, (n, q, quem, c, f) in enumerate([("1", "Como está o tecido?", "medicina e fisioterapia", AZUL, AZUL_T),
                                        ("2", "O que a semana vai pedir?", "preparação física e técnico", GLIC, GLIC_T),
                                        ("3", "Quanto risco aceitar?", "atleta, técnico e clube", FOSF, FOSF_T)]):
    x, y = j * 560, 160 - j * 80
    p.append(caixa(x, y, 500, 340 - y, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 50}" cy="{y + 50}" r="30" fill="{c}"/>')
    rs += [rot(x + 30, y + 30, n, w=40, tam=32, cor=PAPEL, peso=700, serif=True, alinha="center"),
           rot(x + 96, y + 30, q, w=380, tam=26, cor=c, peso=700, serif=True, lh=1.2),
           rot(x + 24, y + 120, quem, w=452, tam=24, cor=TINTA, peso=700, lh=1.25)]
    if j < 2:
        p.append(seta(x + 504, y + 50, x + 552, y - 30, TINTA, "m0", esp=3))
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Quando o calendário fala primeiro, a avaliação vira justificativa.", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ordem", 440, p, rs, eyebrow="Quem decide o quê, e em que ordem", titulo="A ordem das perguntas define quem fala primeiro")

# 7. o plano em uma folha
p = [svg_abre(1664, 460, "Plano da oposta em seis linhas: régua diária de dor no agachamento numa perna só, de 0 a 10, toda manhã; carga do tendão três vezes por semana com a fisioterapia; saltos de quadra por fase da semana, técnico e preparação física; regra de ajuste, se a régua sobe dois pontos o treino seguinte perde os saltos; o plano viaja para a seleção; uma coordenadora responde pelo plano. Valores ilustrativos")]
rs = []
p.append(caixa(0, 0, 1664, 460, TINTA, CARTAO, esp=3, rx=18))
rs.append(rot(32, 18, "Plano da oposta", w=600, tam=30, cor=TINTA, peso=700, serif=True))
rs.append(rot(1100, 26, "valores ilustrativos", w=532, tam=20, cor=MUDO, alinha="right"))
for j, (t, dono, ic, c) in enumerate([("régua diária: dor no agachamento numa perna só, 0 a 10, toda manhã", "a atleta", "t:user", TINTA),
                                      ("carga do tendão: três vezes por semana", "fisioterapia", "t:first-aid-kit", OXID),
                                      ("saltos de quadra distribuídos pela semana", "técnico e preparação física", "t:clipboard-list", GLIC),
                                      ("regra de ajuste: régua sobe 2 pontos, o treino seguinte perde os saltos", "quem estiver no treino", "t:adjustments-horizontal", FOSF),
                                      ("o plano viaja junto para a seleção", "coordenadora", "t:plane", AZUL),
                                      ("uma pessoa responde pelo plano e convoca a próxima conversa", "coordenadora", "t:users", AZUL)]):
    y = 76 + j * 62
    p.append(f'<line x1="32" y1="{y - 6}" x2="1632" y2="{y - 6}" stroke="{GRADE}" stroke-width="2"/>')
    p.append(icone(ic, 32, y + 4, 40, c))
    rs += [rot(88, y + 8, t, w=1060, tam=24, cor=TINTA, peso=700),
           rot(1170, y + 8, dono, w=460, tam=22, cor=c, peso=700, alinha="right")]
diagrama(S, "plano", 460, p, rs, eyebrow="O plano em uma folha", titulo="Cada linha do plano tem um dono, e a dor vira dado")

# 8. as sete frentes
p = [svg_abre(1664, 440, "Sete setas apontando para o mesmo joelho: avaliação biomecânica, neurodinâmica, estabilidade do tronco, excêntrico, corrida progressiva, injeção, alongamento e relaxamento. Embaixo: qual delas funcionou? Relato de caso de 2014, futebol profissional, cinco lesões do posterior da coxa"), defs(TINTA)]
rs = []
CX, CY = 470, 220
p.append(f'<circle cx="{CX}" cy="{CY}" r="70" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>')
p.append(icone("t:question-mark", CX - 36, CY - 36, 72, FOSF))
for k, t in enumerate(["avaliação biomecânica", "neurodinâmica", "estabilidade do tronco", "excêntrico", "corrida progressiva", "injeção", "alongamento e relaxamento"]):
    a = math.radians(-90 + k * 360 / 7)
    x1, y1 = CX + 340 * math.cos(a), CY + 190 * math.sin(a)
    p.append(seta(CX + 230 * math.cos(a), CY + 130 * math.sin(a), CX + 84 * math.cos(a), CY + 84 * math.sin(a), TINTA, "m0", esp=3))
    rs.append(rot(x1 - 130, y1 - 16, t, w=260, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(1000, 0, 664, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1024, 24, "Cinco lesões do posterior da coxa, sete frentes ao mesmo tempo", w=616, tam=26, cor=AZUL, peso=700, serif=True, lh=1.25),
       rot(1024, 150, "ele voltou e não se lesionou de novo", w=616, tam=24, cor=TINTA, peso=700),
       rot(1024, 220, "os autores: impossível dizer qual frente funcionou", w=616, tam=24, cor=FOSF, peso=700, lh=1.25),
       rot(1024, 330, "Integrar é mudar poucas coisas, com dono e data.", w=616, tam=26, cor=AZUL, peso=700, serif=True, lh=1.25)]
diagrama(S, "sete", 440, p, rs, eyebrow="O risco de mudar tudo de uma vez", titulo="Sete frentes ao mesmo tempo funcionaram, e ninguém soube qual",
         fonte="Br J Sports Med 2014")

# 9. o resto da linha do tempo
p = [svg_abre(1664, 440, "Linha do tempo do mês 1 ao 12, meses ilustrativos. A partir do mês 8, a régua diária oscila entre 2 e 5. Mês 10: a régua subiu, dois treinos sem saltos. Mês 11: a seleção recebeu o plano. Do mês 9 ao 12, nenhum afastamento. Mês 12: jogou a fase final. Um caso não prova o método; mostra a integração")]
rs = []
Y = 340
tl, xs = linha_do_tempo(60, 1600, Y, 12, TINTA)
p.append(tl)
for m in (5, 8):
    p.append(f'<circle cx="{xs[m - 1]:.0f}" cy="{Y}" r="14" fill="{MUDO}"/>')
def yr(v):
    return 300 - (v - 0) * 40
pts = [(8, 4), (8.5, 3), (9, 5), (9.5, 3), (10, 5), (10.3, 4), (10.7, 2.5), (11, 3), (11.5, 4), (12, 2.5)]
d = " L ".join(f"{xs[0] + (m - 1) * (xs[1] - xs[0]):.0f} {yr(v):.0f}" for m, v in pts)
p.append(f'<path d="M {d}" stroke="{AZUL}" stroke-width="5" fill="none" stroke-linejoin="round"/>')
p.append(f'<rect x="{xs[8]:.0f}" y="{Y + 30}" width="{xs[11] - xs[8]:.0f}" height="40" rx="10" fill="{OXID}"/>')
p.append(icone("t:ball-volleyball", xs[11] - 26, 20, 52, FOSF))
rs += [rot(xs[8], Y + 36, "nenhum afastamento", w=xs[11] - xs[8], tam=22, cor=PAPEL, peso=700, alinha="center"),
       rot(xs[7] - 330, 60, "régua diária: oscila entre 2 e 5", w=320, tam=22, cor=AZUL, peso=700, alinha="right"),
       rot(xs[9] - 150, 30, "mês 10: régua subiu; dois treinos sem saltos", w=300, tam=20, cor=FOSF, peso=700, alinha="center", lh=1.2),
       rot(xs[11] - 260, 84, "jogou a fase final", w=230, tam=22, cor=FOSF, peso=700, alinha="right"),
       rot(xs[10] - 140, 236, "mês 11: o plano foi junto para a seleção", w=280, tam=20, cor=AZUL, peso=700, alinha="center", lh=1.2),
       rot(xs[4] - 100, Y + 24, "afastamentos", w=200, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(0, 160, "um caso não prova o método; mostra a integração", w=700, tam=24, cor=TINTA, peso=700, serif=True),
       rot(0, 210, "meses e valores ilustrativos", w=700, tam=20, cor=MUDO)]
diagrama(S, "resto", 440, p, rs, eyebrow="O resto da linha do tempo", titulo="A dor continuou oscilando, e ela não parou mais")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Caso integrado: lesão recorrente", "titulo": "Dar dono às passagens, não só ao tecido",
          "regras": ["Na lesão que volta, procure a passagem sem dono antes do tecido",
                     "Tecido, depois a semana, depois o risco aceito, nessa ordem",
                     "Integrar é mudar poucas coisas, com dono e data"],
          "cards": [{"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Respondem pelo estado do tecido e pela régua diária."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Distribui os saltos e aplica a regra de ajuste combinada."},
                    {"ic": "t:user", "t": "A atleta", "x": "Anota a dor toda manhã: é a régua que faz o plano funcionar."}]})

salvar("14-01.json", {"arquivo": "aulas/MOD14/14-01-caso-integrado-atleta-profissional-com-lesao-recorrente.md",
                      "titulo": "Caso integrado 1: atleta profissional com lesão recorrente", "subtitulo": "A dor que volta nas passagens",
                      "nota_capa": "Entra por uma oposta de vôlei profissional com o tendão patelar doendo há doze meses.",
                      "secoes": {"linha": ["O caso.", "capa"], "mesa": ["A leitura de cada área.", "mesa"],
                                 "ordem": ["A conduta integrada.", "ordem"], "resto": ["O resto da linha do tempo.", "resto"]},
                      "slides": S})
