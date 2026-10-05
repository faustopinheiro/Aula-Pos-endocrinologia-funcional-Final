"""Spec do deck 13.6. Gera 13-06.json ao lado deste arquivo."""
import random
from _base import *

S = []

# 1. a largada
p = [svg_abre(1664, 440, "Largada de corrida de rua vista de cima, uma multidão de pontos. Um ponto destacado: um homem na casa dos quarenta com o número da primeira maratona. Recorte de notícia: corredor morre na maratona da cidade. A conta: cerca de 1 parada a cada 100 mil maratonistas")]
rs = []
rnd = random.Random(13)
p.append(f'<rect x="0" y="0" width="900" height="440" rx="18" fill="{CARTAO}" stroke="{GRADE}" stroke-width="2"/>')
pts = "".join(f'<circle cx="{rnd.randint(30, 870)}" cy="{rnd.randint(30, 410)}" r="7" fill="{GRADE}"/>' for _ in range(420))
p.append(pts)
p.append(f'<circle cx="450" cy="220" r="20" fill="{AZUL}" stroke="{PAPEL}" stroke-width="5"/>')
p.append(f'<rect x="490" y="196" width="230" height="52" rx="10" fill="{AZUL}"/>')
rs.append(rot(490, 206, "a primeira maratona", w=230, tam=20, cor=PAPEL, peso=700, alinha="center"))
p.append(caixa(960, 0, 704, 150, MUDO, CARTAO, esp=2, rx=12))
rs += [rot(984, 16, "notícia do ano passado", w=656, tam=20, cor=MUDO, peso=700),
       rot(984, 56, "“Corredor morre na maratona da cidade”", w=656, tam=28, cor=TINTA, peso=700, serif=True, lh=1.2)]
p.append(caixa(960, 190, 704, 250, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(984, 210, "cerca de 1 em 100 mil", w=656, tam=48, cor=FOSF, peso=700, serif=True),
       rot(984, 300, "maratonistas tem uma parada cardíaca na prova", w=656, tam=26, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "largada", 440, p, rs, eyebrow="Corrida de rua, a primeira maratona", titulo="Na maratona, cerca de uma parada a cada cem mil corredores",
         fonte="JAMA 2025")

# 2. a primeira década
p = [svg_abre(1664, 440, "Primeiro registro norte-americano, 2000 a 2010: 10,9 milhões de corredores, 59 paradas cardíacas, 0,54 por 100 mil, 71% fatais. Idade média de 42 anos; 51 dos 59 eram homens")]
rs = []
for k, (n, t, c, f) in enumerate([("10,9 milhões", "corredores, 2000 a 2010", AZUL, AZUL_T), ("59", "paradas cardíacas", GLIC, GLIC_T),
                                  ("0,54", "por 100 mil corredores", GLIC, GLIC_T), ("71%", "das paradas foram fatais", FOSF, FOSF_T)]):
    x = k * 420
    p.append(caixa(x, 0, 400, 200, c, f, esp=3, rx=18))
    rs += [rot(x + 16, 24, n, w=368, tam=52, cor=c, peso=700, alinha="center", serif=True),
           rot(x + 16, 120, t, w=368, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2)]
for j in range(59):
    x = 20 + (j % 30) * 50
    y = 260 + (j // 30) * 60
    c = AZUL if j < 51 else GLIC
    p.append(icone("t:user", x, y, 40, c))
rs += [rot(0, 392, "51 homens", w=500, tam=24, cor=AZUL, peso=700),
       rot(560, 392, "8 mulheres", w=300, tam=24, cor=GLIC, peso=700),
       rot(1060, 392, "idade média: 42 anos", w=604, tam=26, cor=TINTA, peso=700, alinha="right", serif=True)]
diagrama(S, "registro", 440, p, rs, eyebrow="A primeira década medida, registro de 2012", titulo="Sete em cada dez paradas foram fatais",
         fonte="N Engl J Med 2012")

# 3. a distância
p = [svg_abre(1664, 440, "Paradas por 100 mil corredores. 2000 a 2010: maratona 1,01, meia maratona 0,27. 2010 a 2023: maratona 1,04, meia 0,47. Nos homens da maratona da primeira década, de 0,71 para 2,03 entre a primeira e a segunda metade"), defs(FOSF)]
rs = []
B, K = 380, 260
p.append(f'<line x1="0" y1="{B}" x2="1000" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for g, (per, vals) in enumerate([("2000 a 2010", (1.01, 0.27)), ("2010 a 2023", (1.04, 0.47))]):
    x0 = 40 + g * 500
    for j, (v, c, t) in enumerate(zip(vals, (FOSF, AZUL), ("maratona", "meia"))):
        x = x0 + j * 200
        h = v * K
        p.append(f'<rect x="{x}" y="{B - h:.0f}" width="160" height="{h:.0f}" rx="10" fill="{c}"/>')
        rs.append(rot(x, B - h - 44, f"{v:.2f}".replace(".", ","), w=160, tam=30, cor=c, peso=700, alinha="center", serif=True))
        rs.append(rot(x, B + 8, t, w=160, tam=20, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x0, 0, per, w=360, tam=24, cor=MUDO, peso=700, alinha="center"))
p.append(caixa(1080, 40, 584, 340, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1104, 60, "homens na maratona, 2000 a 2010", w=536, tam=22, cor=FOSF, peso=700),
       rot(1104, 110, "0,71", w=200, tam=44, cor=MUDO, peso=700, serif=True),
       rot(1400, 110, "2,03", w=240, tam=44, cor=FOSF, peso=700, serif=True),
       rot(1104, 180, "primeira metade → segunda metade", w=536, tam=22, cor=TINTA, peso=700),
       rot(1104, 260, "o registro descreveu o aumento, sem testar a causa", w=536, tam=22, cor=MUDO, peso=700, lh=1.25)]
p.append(seta(1240, 136, 1380, 136, FOSF, "m0", 4))
diagrama(S, "distancia", 440, p, rs, eyebrow="Paradas por 100 mil corredores", titulo="A maratona tem de duas a quatro vezes o risco da meia",
         fonte="N Engl J Med 2012 · JAMA 2025")

# 4. a causa
p = [svg_abre(1664, 440, "Duas causas. Miocardiopatia hipertrófica: estrutural, mais no jovem. Doença coronariana: placa, no adulto de meia-idade. Eixo de idade com o cruzamento perto dos 35 anos. No registro mais recente, entre os casos com causa definida, a coronária foi a mais comum")]
rs = []
p.append(caixa(0, 0, 780, 220, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:heart", 24, 30, 90, AZUL))
rs += [rot(140, 30, "Miocardiopatia hipertrófica", w=620, tam=30, cor=AZUL, peso=700, serif=True),
       rot(140, 90, "doença do músculo do coração, estrutural; pesa mais abaixo dos 35", w=620, tam=24, cor=TINTA, peso=600, lh=1.25)]
p.append(caixa(884, 0, 780, 220, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:heartbeat", 908, 30, 90, FOSF))
rs += [rot(1024, 30, "Doença coronariana", w=620, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1024, 90, "placa silenciosa; domina acima dos 35, e foi a mais comum no registro recente", w=620, tam=24, cor=TINTA, peso=600, lh=1.25)]
p.append(f'<line x1="0" y1="330" x2="1664" y2="330" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 0 260 C 500 270 700 320 1664 325" stroke="{AZUL}" stroke-width="5" fill="none"/>')
p.append(f'<path d="M 0 325 C 600 320 800 280 1664 250" stroke="{FOSF}" stroke-width="5" fill="none"/>')
p.append(f'<line x1="760" y1="250" x2="760" y2="340" stroke="{MUDO}" stroke-width="3" stroke-dasharray="6 6"/>')
rs += [rot(700, 346, "≈ 35 anos", w=120, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(0, 380, "A prova não cria a doença: é o dia em que a placa encontra o esforço mais longo do ano.", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(1300, 346, "idade", w=364, tam=20, cor=MUDO, alinha="right"), rot(0, 230, "esquema", w=200, tam=20, cor=MUDO)]
diagrama(S, "causa", 440, p, rs, eyebrow="Quem para, e por quê", titulo="A prova revela a doença que estava escondida")

# 5. a sobrevida
p = [svg_abre(1664, 440, "Duas décadas. 2000 a 2009: 29% sobreviveram, 0,39 morte por 100 mil. 2010 a 2023: 29,3 milhões de concluintes, 176 paradas, 0,60 por 100 mil, 66% sobreviveram, 0,20 morte por 100 mil. A incidência não mudou; a morte caiu pela metade"), defs(OXID)]
rs = []
for k, (per, sob, mort, c, f) in enumerate([("2000 a 2009", 29, "0,39", MUDO, CARTAO), ("2010 a 2023", 66, "0,20", OXID, OXID_T)]):
    x = k * 860
    p.append(caixa(x, 0, 804, 330, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 18, per, w=756, tam=28, cor=c, peso=700, serif=True))
    for j in range(10):
        cor = c if j < round(sob / 10) else GRADE
        p.append(icone("t:user", x + 24 + j * 76, 80, 64, cor))
    rs += [rot(x + 24, 164, f"{sob}% sobreviveram", w=756, tam=36, cor=c, peso=700, serif=True),
           rot(x + 24, 240, f"morte: {mort} por 100 mil corredores", w=756, tam=24, cor=TINTA, peso=700)]
p.append(seta(810, 160, 852, 160, OXID, "m0", 4))
rs += [rot(0, 350, "incidência: 0,54 → 0,60 por 100 mil · 176 paradas em 29,3 milhões de concluintes", w=1664, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(0, 392, "A incidência não mudou. A morte caiu pela metade.", w=1664, tam=30, cor=OXID, peso=700, serif=True, alinha="center")]
diagrama(S, "sobrevida", 440, p, rs, eyebrow="O registro atualizado em 2025", titulo="A chance de sobreviver mais que dobrou",
         fonte="N Engl J Med 2012 · JAMA 2025")

# 6. o que mudou
p = [svg_abre(1664, 420, "Os dois fatores ligados à sobrevida no primeiro registro: ressuscitação começada por quem estava perto, e causa diferente de miocardiopatia hipertrófica. No registro recente: reanimação em praticamente todos e desfibrilador usado em quase todos. O que mudou foi a resposta, não o rastreio")]
rs = []
p.append(caixa(0, 0, 780, 280, GRADE, CARTAO, esp=2, rx=18))
rs.append(rot(24, 18, "Registro de 2012: o que se associou à sobrevida", w=732, tam=24, cor=MUDO, peso=700))
for j, (ic, t) in enumerate([("t:users", "reanimação começada por quem estava perto"), ("t:heart", "causa diferente de miocardiopatia hipertrófica")]):
    p.append(icone(ic, 24, 80 + j * 90, 56, AZUL))
    rs.append(rot(100, 84 + j * 90, t, w=656, tam=26, cor=TINTA, peso=700, lh=1.2))
p.append(caixa(884, 0, 780, 280, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(908, 18, "Registro de 2025: a resposta nas provas", w=732, tam=24, cor=OXID, peso=700))
for j, (ic, t) in enumerate([("t:users", "reanimação em praticamente todos"), ("t:bolt", "desfibrilador usado em quase todos")]):
    p.append(icone(ic, 908, 80 + j * 90, 56, OXID))
    rs.append(rot(984, 84 + j * 90, t, w=656, tam=26, cor=TINTA, peso=700, lh=1.2))
p.append(f'<rect x="0" y="310" width="1664" height="100" rx="16" fill="{OXID}"/>')
rs.append(rot(0, 336, "O que mudou foi a resposta, não o rastreio.", w=1664, tam=34, cor=PAPEL, peso=700, serif=True, alinha="center"))
diagrama(S, "resposta", 420, p, rs, eyebrow="Por que a morte caiu", titulo="Reanimação e desfibrilador, não exame em todos os inscritos")

# 7. o triatlo
p = [svg_abre(1664, 440, "Duas faixas: natação com 13 mortes, outras etapas com uma. Cerca de 959 mil participantes de 2006 a 2008, 14 mortes, 1,5 por 100 mil, 80% homens, 28 a 65 anos. Registro com outra metodologia; comparação com a corrida é aproximada")]
rs = []
for j, (t, n, c, f) in enumerate([("natação", 13, AZUL, AZUL_T), ("outras etapas", 1, GLIC, GLIC_T)]):
    y = j * 110
    p.append(caixa(0, y, 980, 90, c, f, esp=3, rx=14))
    rs.append(rot(20, y + 28, t, w=220, tam=26, cor=c, peso=700, serif=True))
    for k in range(n):
        p.append(f'<line x1="{250 + k * 46}" y1="{y + 20}" x2="{250 + k * 46}" y2="{y + 70}" stroke="{FOSF}" stroke-width="10" stroke-linecap="round"/>')
    if n:
        rs.append(rot(250 + n * 46 + 4, y + 28, str(n), w=80, tam=28, cor=FOSF, peso=700, serif=True))
rs.append(rot(0, 240, "registro com outra metodologia: a comparação com a corrida é aproximada", w=980, tam=22, cor=MUDO, peso=700))
p.append(caixa(1040, 0, 624, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1064, 20, "1,5 por 100 mil", w=576, tam=48, cor=AZUL, peso=700, serif=True),
       rot(1064, 110, "14 mortes em cerca de 959 mil participantes, 2006 a 2008", w=576, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1064, 220, "80% homens · 28 a 65 anos", w=576, tam=24, cor=TINTA, peso=700),
       rot(1064, 300, "na água, quem perde a consciência afunda e não é visto a tempo", w=576, tam=24, cor=AZUL, peso=700, lh=1.25)]
diagrama(S, "triatlo", 440, p, rs, eyebrow="O triatlo, levantamento de 2010", titulo="No triatlo, quase todas as mortes foram na natação",
         fonte="JAMA 2010")

# 8. o que dizer
p = [svg_abre(1664, 440, "Duas colunas. Para o corredor: risco absoluto pequeno; sintoma no treino não vai para a prova; febre ou infecção recente, não larga; aprender reanimação. Para quem organiza: o tempo até a reanimação e até o desfibrilador")]
rs = []
p.append(caixa(0, 0, 900, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(corredor(24, 20, 90, AZUL))
rs.append(rot(130, 40, "Para o corredor", w=740, tam=32, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["risco pequeno: largar, não desistir", "treinar para a distância", "sintoma no treino vai para a consulta, não para a prova",
                       "febre ou infecção recente: não larga", "aprender reanimação"]):
    p.append(icone("t:check", 24, 130 + j * 60, 32, AZUL))
    rs.append(rot(70, 130 + j * 60, t, w=810, tam=24, cor=TINTA, peso=700))
p.append(caixa(960, 0, 704, 440, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:stopwatch", 984, 24, 72, OXID))
rs += [rot(1070, 40, "Para quem organiza", w=570, tam=32, cor=OXID, peso=700, serif=True),
       rot(984, 140, "o número que importa", w=656, tam=26, cor=TINTA, peso=700),
       rot(984, 200, "tempo até a reanimação e até o desfibrilador", w=656, tam=34, cor=OXID, peso=700, serif=True, lh=1.2),
       rot(984, 350, "não quantos inscritos fizeram exame", w=656, tam=24, cor=MUDO, peso=700)]
diagrama(S, "corredor", 440, p, rs, eyebrow="O que dizer ao homem da primeira maratona", titulo="Pode largar; e quem organiza mede o tempo até o socorro")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Eventos de massa: corrida de rua", "titulo": "O risco é pequeno, e o que o reduz é a resposta",
          "regras": ["Cerca de uma parada a cada cem mil maratonistas, mais em homens de meia-idade",
                     "A incidência não mudou; a morte caiu pela metade com reanimação e desfibrilador",
                     "No triatlo, o ponto crítico é a natação"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Dá o número verdadeiro e investiga o sintoma do treino antes da largada."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Prepara para a distância e não deixa largar quem está doente."},
                    {"ic": "t:user", "t": "O corredor", "x": "Aprende reanimação: na prova, quem salva é quem está ao lado."}]})

salvar("13-06.json", {"arquivo": "aulas/MOD13/13-06-eventos-de-massa-risco-cardiovascular-em-corrida-de-rua.md",
                      "titulo": "Eventos de massa: risco cardiovascular em corrida de rua", "subtitulo": "O que os registros de provas mostram",
                      "nota_capa": "Entra por um homem na casa dos quarenta inscrito na primeira maratona.",
                      "secoes": {"largada": ["A pergunta.", "capa"], "registro": ["Os registros.", "registro"],
                                 "triatlo": ["O triatlo e a conduta.", "triatlo"]},
                      "slides": S})
