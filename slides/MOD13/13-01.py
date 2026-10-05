"""Spec do deck 13.1. Gera 13-01.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o corredor e a planilha da elite
p = [svg_abre(1664, 440, "Corredor na casa dos quarenta com a planilha impressa: a mesma metodologia da elite. Seis horas por semana, três meses sem melhorar, dor na canela. Exames todos normais")]
rs = []
p.append(corredor(0, 30, 330, AZUL))
p.append(f'<circle cx="{0 + 55 * 3.3:.0f}" cy="{30 + 88 * 3.3:.0f}" r="26" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(caixa(380, 0, 520, 240, TINTA, CARTAO, esp=3, rx=12))
for j in range(5):
    p.append(f'<rect x="410" y="{90 + j * 28}" width="{440 - (j % 3) * 70}" height="12" rx="6" fill="{GRADE}"/>')
rs.append(rot(400, 20, "“a mesma metodologia da elite”", w=480, tam=26, cor=TINTA, peso=700, serif=True))
for j, (t, c) in enumerate([("seis horas por semana", AZUL), ("três meses sem melhorar", GLIC), ("dor na canela", FOSF)]):
    p.append(caixa(380, 270 + j * 58, 520, 48, c, PAPEL, esp=2, rx=24))
    rs.append(rot(400, 280 + j * 58, t, w=480, tam=24, cor=c, peso=700, alinha="center"))
p.append(caixa(960, 0, 704, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(984, 20, "Os exames que ele trouxe", w=656, tam=28, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["hemograma", "tireoide", "vitamina D", "testosterona"]):
    p.append(icone("t:check", 984, 96 + j * 70, 36, OXID))
    rs.append(rot(1034, 96 + j * 70, f"{t}: normal", w=600, tam=26, cor=TINTA, peso=600))
rs.append(rot(984, 380, "o que faltava não estava no exame", w=656, tam=24, cor=OXID, peso=700))
diagrama(S, "corredor", 440, p, rs, eyebrow="Um corredor na casa dos quarenta", titulo="A planilha da elite em escala menor não funcionou")

# 2. transpor x adaptar
p = [svg_abre(1664, 440, "Duas setas saindo do plano da elite. Transpor: o mesmo plano, encolhido. Adaptar: um plano redesenhado em volta de outra vida, com sono, trabalho e família no desenho"), defs(FOSF, OXID)]
rs = []
p.append(caixa(0, 120, 380, 200, TINTA, CARTAO, esp=3, rx=16))
for j in range(4):
    p.append(f'<rect x="30" y="{180 + j * 30}" width="{320 - j * 30}" height="14" rx="7" fill="{GRADE}"/>')
rs.append(rot(20, 136, "plano da elite", w=340, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
p.append(seta(400, 170, 620, 90, FOSF, "m0", 5))
p.append(seta(400, 270, 620, 350, OXID, "m1", 5))
p.append(caixa(640, 20, 340, 150, FOSF, FOSF_T, esp=3, rx=16))
for j in range(4):
    p.append(f'<rect x="665" y="{70 + j * 22}" width="{200 - j * 20}" height="10" rx="5" fill="{FOSF}"/>')
rs += [rot(1000, 40, "Transpor", w=300, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1000, 90, "o mesmo plano, encolhido: menos quilômetro, mesma lógica", w=664, tam=24, cor=TINTA, peso=600, lh=1.25)]
p.append(caixa(640, 260, 340, 170, OXID, OXID_T, esp=3, rx=16))
for j, (t, c) in enumerate([("sono", AZUL), ("trabalho", GLIC), ("família", FOSF)]):
    p.append(f'<rect x="{660 + j * 104}" y="300" width="96" height="40" rx="20" fill="{c}"/>')
    rs.append(rot(660 + j * 104, 308, t, w=96, tam=20, cor=PAPEL, peso=700, alinha="center"))
p.append(f'<rect x="665" y="370" width="290" height="14" rx="7" fill="{OXID}"/>')
rs += [rot(1000, 280, "Adaptar", w=300, tam=30, cor=OXID, peso=700, serif=True),
       rot(1000, 330, "o plano redesenhado em volta da vida real: o que falta é margem, não quilômetro", w=664, tam=24, cor=TINTA, peso=600, lh=1.25)]
diagrama(S, "transpor", 440, p, rs, eyebrow="Transpor não é adaptar", titulo="O amador é outro organismo, não a elite encolhida")

# 3. o funil de quem é estudado
p = [svg_abre(1664, 440, "Funil. Na boca larga, quem é estudado: atletas, jovens, homens, disponíveis às seis da manhã por doze semanas. Na ponta estreita, quem é atendido: quarenta, cinquenta, sessenta anos, com trabalho, filhos e remédios")]
rs = []
p.append(f'<path d="M 0 20 L 1000 20 L 640 300 L 640 420 L 360 420 L 360 300 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
rs += [rot(40, 32, "Quem é estudado", w=920, tam=30, cor=AZUL, peso=700, alinha="center", serif=True),
       rot(150, 84, "atletas · jovens · homens · disponíveis às seis da manhã por doze semanas", w=700, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.3),
       rot(370, 330, "coletável", w=260, tam=26, cor=AZUL, peso=700, alinha="center")]
p.append(caixa(1080, 120, 584, 300, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:users", 1104, 140, 80, FOSF))
rs += [rot(1200, 150, "Quem é atendido", w=440, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1104, 240, "quarenta, cinquenta, sessenta anos · trabalho · filhos · remédios", w=536, tam=26, cor=TINTA, peso=700, lh=1.3),
       rot(1104, 350, "a faixa que mais procura é a menos estudada", w=536, tam=22, cor=FOSF, peso=700)]
p.insert(1, defs(FOSF))
p.append(seta(1010, 260, 1070, 260, FOSF, "m0", 5))
diagrama(S, "funil", 440, p, rs, eyebrow="De onde vem o descompasso", titulo="A elite é estudada porque é coletável")

# 4. a mesma sessão, três corpos
p = [svg_abre(1664, 440, "A mesma sessão para três pessoas. Iniciante: overdose. Praticante regular: a dose depende da semana. Atleta: subdose. Lesão é carga sobre capacidade, não carga sozinha"), defs(TINTA)]
rs = []
p.append(caixa(632, 0, 400, 90, TINTA, TINTA, esp=0, rx=45))
rs.append(rot(652, 26, "a mesma sessão", w=360, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
for k, (t, dose, c, f, frac) in enumerate([("iniciante", "overdose", FOSF, FOSF_T, 1.0), ("praticante regular", "depende da semana", GLIC, GLIC_T, 0.75), ("atleta", "subdose", OXID, OXID_T, 0.35)]):
    x = k * 564
    p.append(seta(832, 96, x + 268, 150, TINTA, "m0", 3))
    p.append(caixa(x, 160, 536, 200, c, f, esp=3, rx=18))
    p.append(f'<rect x="{x + 30}" y="270" width="476" height="30" rx="15" fill="{PAPEL}" stroke="{c}" stroke-width="2"/>')
    p.append(f'<rect x="{x + 30}" y="270" width="{476 * frac:.0f}" height="30" rx="15" fill="{c}"/>')
    rs += [rot(x + 24, 180, t, w=488, tam=28, cor=c, peso=700, alinha="center", serif=True), rot(x + 24, 222, dose, w=488, tam=26, cor=TINTA, peso=700, alinha="center")]
rs.append(rot(24, 312, "barra: fração da capacidade · esquema", w=488, tam=20, cor=MUDO, alinha="center"))
p.append(caixa(0, 380, 1664, 60, OXID, OXID, esp=0, rx=14))
rs.append(rot(20, 394, "Lesão é carga sobre capacidade, não carga sozinha", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "tres", 440, p, rs, eyebrow="Uma sessão, três corpos", titulo="A mesma sessão é excesso num corpo e pouco em outro")

# 5. quatro perfis
p = [svg_abre(1664, 440, "Quatro perfis de praticante amador: o iniciante ou quem recomeça, risco progressão rápida, alavanca rampa; o praticante de saúde, risco desistência, alavanca adesão; o amador competitivo, risco treino alto com vida cheia, alavanca recuperação; o de fim de semana, risco salto de carga, alavanca distribuir")]
rs = []
for k, (ic, t, risco, alav, c, f) in enumerate([("t:user", "Iniciante ou quem recomeça", "progressão rápida sobre tecido sem histórico", "a rampa", AZUL, AZUL_T),
                                                ("t:salad", "Praticante de saúde", "desistir", "a adesão", OXID, OXID_T),
                                                ("t:stopwatch", "Amador competitivo", "treino alto somado à vida cheia", "a recuperação", GLIC, GLIC_T),
                                                ("t:calendar", "O de fim de semana", "o salto de carga do sábado", "distribuir parte da carga", FOSF, FOSF_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 440, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 150, 20, 100, c))
    rs += [rot(x + 20, 136, t, w=360, tam=26, cor=c, peso=700, alinha="center", serif=True, lh=1.15),
           rot(x + 20, 214, "risco: " + risco, w=360, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.25),
           rot(x + 20, 340, "alavanca: " + alav, w=360, tam=24, cor=c, peso=700, alinha="center", lh=1.25)]
diagrama(S, "perfis", 440, p, rs, eyebrow="Quatro perfis dentro do amador", titulo="Cada perfil tem um risco e uma alavanca")

# 6. motivos
p = [svg_abre(1664, 440, "Escala de motivação de maratonistas de 1993: nove motivos em quatro grupos. Saúde física: saúde geral, peso. Social: pertencimento, reconhecimento. Conquista: competição, meta pessoal. Psicológico: enfrentar o estresse, autoestima, sentido de vida")]
rs = []
for k, (t, itens, c, f) in enumerate([("Saúde física", ["saúde geral", "peso"], OXID, OXID_T), ("Social", ["pertencimento", "reconhecimento"], AZUL, AZUL_T),
                                      ("Conquista", ["competição", "meta pessoal"], GLIC, GLIC_T), ("Psicológico", ["enfrentar o estresse", "autoestima", "sentido de vida"], FOSF, FOSF_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 300, c, f, esp=3, rx=18))
    rs.append(rot(x + 20, 20, t, w=360, tam=30, cor=c, peso=700, alinha="center", serif=True))
    for j, it in enumerate(itens):
        p.append(caixa(x + 30, 90 + j * 66, 340, 52, c, PAPEL, esp=2, rx=26))
        rs.append(rot(x + 40, 102 + j * 66, it, w=320, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(0, 330, 1664, 110, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(24, 352, "O plano precisa servir ao motivo: para quem corre pelo grupo, tirar o treino do sábado é tirar o motivo", w=1616, tam=26, cor=PAPEL, peso=700, alinha="center", lh=1.3))
diagrama(S, "motivos", 440, p, rs, eyebrow="Escala de motivação de maratonistas, 1993", titulo="Nove motivos para correr, em quatro famílias",
         fonte="Res Q Exerc Sport 1993")

# 7. a semana real
p = [svg_abre(1664, 440, "A semana do corredor em duas camadas: em cima, o treino prescrito, seis horas; embaixo, acordar às cinco para correr, deitar à meia-noite, duas horas de deslocamento, a filha pequena. Régua de sono: cinco horas por noite há dois anos")]
rs = []
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
for i, d in enumerate(dias):
    x = 160 + i * 214
    rs.append(rot(x, 0, d, w=196, tam=22, cor=MUDO, peso=700, alinha="center"))
    if i in (0, 2, 4, 5):
        p.append(f'<rect x="{x}" y="40" width="196" height="60" rx="10" fill="{OXID}"/>')
    for j, (c, h) in enumerate([(AZUL, 50), (GLIC, 40), (FOSF, 30)]):
        p.append(f'<rect x="{x}" y="{140 + j * 60}" width="196" height="{h}" rx="8" fill="{c}" opacity="0.85"/>')
rs += [rot(0, 54, "treino", w=150, tam=24, cor=OXID, peso=700), rot(0, 150, "acordar às 5", w=150, tam=22, cor=AZUL, peso=700),
       rot(0, 206, "trânsito", w=150, tam=22, cor=GLIC, peso=700), rot(0, 262, "a filha", w=150, tam=22, cor=FOSF, peso=700)]
p.append(f'<rect x="160" y="350" width="1494" height="30" rx="15" fill="{GRADE}"/>')
p.append(f'<rect x="160" y="350" width="{1494 * 5 / 8:.0f}" height="30" rx="15" fill="{FOSF}"/>')
rs += [rot(0, 352, "sono", w=150, tam=22, cor=FOSF, peso=700), rot(160, 392, "≈ 5 horas por noite, há dois anos", w=1494, tam=24, cor=FOSF, peso=700)]
diagrama(S, "semana", 440, p, rs, eyebrow="O que o plano não via", titulo="No amador, o resto da semana compete com a recuperação")

# 8. cinco perguntas
p = [svg_abre(1664, 440, "Cinco perguntas, custo zero: que horas deita e levanta; turno, escala e deslocamento; refeições em dia de treino; já fez dieta restritiva, perdeu muito peso ou parou de menstruar; quantas infecções nos últimos doze meses. Registro diário: hora de deitar, nota ao acordar, esforço percebido")]
rs = []
for j, t in enumerate(["que horas deita e que horas levanta", "turno, escala, plantão e deslocamento", "refeições em dia de treino, antes e depois",
                       "dieta restritiva, perda grande de peso ou menstruação que parou", "infecções nos últimos doze meses"]):
    y = j * 86
    p.append(f'<circle cx="32" cy="{y + 32}" r="28" fill="{OXID}"/>')
    rs += [rot(12, y + 14, str(j + 1), w=40, tam=26, cor=PAPEL, peso=700, alinha="center"), rot(80, y + 14, t, w=980, tam=28, cor=TINTA, peso=700, serif=True)]
p.append(caixa(1140, 0, 524, 440, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(1164, 20, "Registro diário", w=476, tam=28, cor=GLIC, peso=700, serif=True))
for j, t in enumerate(["hora de deitar", "nota de 0 a 10 ao acordar", "esforço percebido no fim do treino"]):
    rs.append(rot(1164, 96 + j * 64, "· " + t, w=476, tam=24, cor=TINTA, peso=700))
rs.append(rot(1164, 330, "custo zero; o padrão aparece em poucas semanas", w=476, tam=24, cor=GLIC, peso=700, lh=1.25))
diagrama(S, "perguntas", 440, p, rs, eyebrow="Antes de olhar exame", titulo="Cinco perguntas mudam mais conduta que um painel caro")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quem é o praticante amador", "titulo": "Adaptar o plano à vida, e não encolher o da elite",
          "regras": ["O amador não é a elite em escala menor: transpor não é adaptar",
                     "Lesão é carga sobre capacidade: a mesma sessão é excesso num corpo e pouco em outro",
                     "O plano serve ao motivo e cabe na semana real, não na ideal"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina", "x": "Pergunta pelo motivo e pela semana antes de montar a planilha."},
                    {"ic": "h:doctor", "t": "Medicina e nutrição", "x": "Fazem as cinco perguntas e olham a vida antes do exame."},
                    {"ic": "t:user", "t": "O praticante", "x": "Registra sono, como acordou e o esforço, para o padrão aparecer."}]})

salvar("13-01.json", {"arquivo": "aulas/MOD13/13-01-quem-e-o-praticante-amador.md",
                      "titulo": "Quem é o praticante amador", "subtitulo": "Perfis, motivos e a semana real",
                      "nota_capa": "Entra por um corredor na casa dos quarenta que segue a planilha da elite em escala menor.",
                      "secoes": {"corredor": ["O erro.", "capa"], "funil": ["Por que o erro acontece.", "funil"],
                                 "perfis": ["Perfis e motivos.", "perfis"], "semana": ["A semana real.", "semana"]},
                      "slides": S})
