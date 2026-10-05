"""Spec do deck 13.8. Gera 13-08.json ao lado deste arquivo."""
from _base import *

S = []


def faixa(p, rs, y, ponto=None, seta_para=None):
    """A faixa de 0 a 100% de lesão com as duas pontas marcadas."""
    x0, x1 = 60, 1600
    p.append(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="40" rx="20" fill="{GRADE}"/>')
    p.append(f'<rect x="{x0 + (x1 - x0) * 0.032:.0f}" y="{y}" width="{(x1 - x0) * (0.849 - 0.032):.0f}" height="40" rx="20" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="2"/>')
    for v, t, c in ((0.032, "cross country, 3,2%", AZUL), (0.849, "novatos, 84,9%", FOSF)):
        x = x0 + (x1 - x0) * v
        p.append(f'<circle cx="{x:.0f}" cy="{y + 20}" r="22" fill="{c}"/>')
        rs.append(rot(x - 160, y + 52, t, w=320, tam=22, cor=c, peso=700, alinha="center"))
    for v in (0, 0.5, 1):
        rs.append(rot(x0 + (x1 - x0) * v - 40, y - 34, f"{int(v * 100)}%", w=80, tam=20, cor=MUDO, alinha="center"))


# 1. a turma
p = [svg_abre(1664, 440, "Quarenta silhuetas de corredores numa praça, com a faixa: do zero aos cinco quilômetros, dez semanas. O treinador da assessoria com uma prancheta: quantos vão se machucar?")]
rs = []
p.append(f'<rect x="0" y="0" width="1664" height="70" rx="12" fill="{AZUL}"/>')
rs.append(rot(0, 18, "do zero aos cinco quilômetros · dez semanas", w=1664, tam=28, cor=PAPEL, peso=700, alinha="center", serif=True))
for j in range(40):
    x = 10 + (j % 20) * 52
    y = 110 + (j // 20) * 150
    p.append(corredor(x, y, 110, AZUL if j % 3 else GLIC))
p.append(caixa(1180, 110, 484, 300, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:clipboard-list", 1204, 134, 64, FOSF))
rs += [rot(1280, 140, "o treinador", w=360, tam=24, cor=FOSF, peso=700),
       rot(1204, 230, "“Quantos vão se machucar?”", w=436, tam=34, cor=TINTA, peso=700, serif=True, lh=1.2)]
diagrama(S, "turma", 440, p, rs, eyebrow="Uma turma de iniciantes numa assessoria", titulo="Quarenta novatos, e uma pergunta justa")

# 2. a faixa
p = [svg_abre(1664, 400, "Faixa de 0 a 100% de lesão com perda de tempo em corredores: cross country 3,2%, novatos 84,9%. Revisão de 2015, 86 artigos. A proporção muda com a definição e com a duração do seguimento")]
rs = []
faixa(p, rs, 60)
for j, (ic, t) in enumerate([("t:book", "86 artigos"), ("t:ruler-measure", "muda com a definição de lesão"), ("t:calendar", "muda com o tempo de seguimento")]):
    x = j * 564
    p.append(caixa(x, 220, 536, 120, GRADE, CARTAO, esp=2, rx=16))
    p.append(icone(ic, x + 24, 252, 56, MUDO))
    rs.append(rot(x + 100, 260, t, w=420, tam=26, cor=TINTA, peso=700, lh=1.2))
rs.append(rot(0, 360, "A corrida não tem um risco; tem uma faixa.", w=1664, tam=28, cor=FOSF, peso=700, serif=True, alinha="center"))
diagrama(S, "faixa", 400, p, rs, eyebrow="Lesão com perda de tempo, revisão de 2015", titulo="Na mesma modalidade, de três a oitenta e cinco por cento",
         fonte="Sports Med 2015")

# 3. o novato
p = [svg_abre(1664, 440, "Duas pessoas correndo a mesma hora: o novato com barra alta de lesão por hora, o recreativo experiente com menos da metade. Embaixo do novato: tecido sem histórico de carga, volume subindo. Curva em U: distância semanal e lesão com perda de tempo")]
rs = []
B = 380
p.append(f'<line x1="0" y1="{B}" x2="900" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for j, (t, h, c) in enumerate([("novato", 250, FOSF), ("recreativo experiente", 110, AZUL)]):
    x = 60 + j * 420
    p.append(f'<rect x="{x}" y="{B - h}" width="260" height="{h}" rx="12" fill="{c}"/>')
    p.append(corredor(x + 80, B - h - 110, 100, c))
    rs.append(rot(x - 20, B + 10, t, w=300, tam=22, cor=c, peso=700, alinha="center"))
rs += [rot(60, B - 180, "tecido sem histórico de carga · volume subindo", w=260, tam=20, cor=PAPEL, peso=700, alinha="center", lh=1.25),
       rot(480, B - 90, "menos da metade, por hora", w=260, tam=20, cor=PAPEL, peso=700, alinha="center", lh=1.2),
       rot(420, 0, "esquema; números na conversa sobre definição de lesão", w=480, tam=20, cor=MUDO)]
p.append(caixa(980, 0, 684, 440, GLIC, GLIC_T, esp=3, rx=18))
p.append(f'<path d="M 1040 120 C 1140 330 1460 330 1600 120" stroke="{GLIC}" stroke-width="6" fill="none"/>')
p.append(f'<line x1="1030" y1="340" x2="1620" y2="340" stroke="{TINTA}" stroke-width="2"/>')
rs += [rot(1004, 20, "padrão em U", w=636, tam=28, cor=GLIC, peso=700, serif=True),
       rot(1004, 70, "lesão com perda de tempo", w=636, tam=20, cor=TINTA, peso=700),
       rot(1004, 352, "muito pouco ← distância semanal → muito", w=636, tam=20, cor=MUDO, peso=700, alinha="center"),
       rot(1004, 392, "o iniciante sai do zero: está numa ponta", w=636, tam=22, cor=GLIC, peso=700, alinha="center")]
diagrama(S, "novato", 440, p, rs, eyebrow="Quem está na ponta alta", titulo="Por hora, o novato se machuca mais que o dobro do experiente",
         fonte="Sports Med 2015")

# 4. onde
p = [svg_abre(1664, 440, "Silhueta de corredor com joelho, tornozelo e perna marcados. Cinco diagnósticos mais frequentes: tendinopatia do Aquiles 10,3%, síndrome do estresse tibial medial 9,4%, dor patelofemoral 6,3%, fascite plantar 6,1%, entorse de tornozelo 5,8%. Revisão de 2021, estudos prospectivos")]
rs = []
p.append(corredor(0, 20, 400, AZUL_T))
for cx, cy, t in ((210, 300, "joelho"), (180, 390, "tornozelo"), (230, 345, "perna")):
    p.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="{FOSF}"/>')
rs += [rot(280, 280, "joelho, perna e tornozelo: as regiões com mais lesão", w=300, tam=22, cor=FOSF, peso=700, lh=1.25)]
diag = [("tendinopatia do Aquiles", 10.3), ("síndrome do estresse tibial medial", 9.4), ("dor patelofemoral", 6.3), ("fascite plantar", 6.1), ("entorse de tornozelo", 5.8)]
for j, (t, v) in enumerate(diag):
    y = 10 + j * 78
    c = GLIC if "entorse" in t else AZUL
    p.append(f'<rect x="1060" y="{y}" width="{v * 52:.0f}" height="50" rx="8" fill="{c}"/>')
    rs += [rot(620, y + 12, t, w=420, tam=22, cor=TINTA, peso=700, alinha="right"),
           rot(1070 + v * 52, y + 12, f"{v:.1f}%".replace(".", ","), w=100, tam=22, cor=c, peso=700)]
rs.append(rot(620, 404, "em azul, sobrecarga; a entorse é a exceção traumática", w=1044, tam=22, cor=MUDO, peso=700, alinha="right"))
diagrama(S, "onde", 440, p, rs, eyebrow="Onde a lesão aparece, revisão de 2021", titulo="Quase toda lesão do corredor é de sobrecarga",
         fonte="J Sport Health Sci 2021")

# 5. o joelho
p = [svg_abre(1664, 420, "Prevalência de artrose de quadril e joelho: sedentários 10,2%, corredores recreacionais 3,5%, corredores competitivos de elite 13,3%. Metanálise de 2017, estudos observacionais")]
rs = []
B, K = 360, 22
p.append(f'<line x1="0" y1="{B}" x2="1000" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for j, (t, v, c) in enumerate([("sedentários", 10.2, MUDO), ("corredores recreacionais", 3.5, OXID), ("competitivos de elite", 13.3, FOSF)]):
    x = 60 + j * 320
    h = v * K
    p.append(f'<rect x="{x}" y="{B - h:.0f}" width="220" height="{h:.0f}" rx="10" fill="{c}"/>')
    rs += [rot(x, B - h - 48, f"{v:.1f}%".replace(".", ","), w=220, tam=34, cor=c, peso=700, alinha="center", serif=True),
           rot(x - 30, B + 10, t, w=280, tam=22, cor=TINTA, peso=700, alinha="center")]
p.append(caixa(1080, 0, 584, 420, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1104, 24, "“Corrida destrói o joelho”?", w=536, tam=30, cor=OXID, peso=700, serif=True),
       rot(1104, 110, "o dado não sustenta para a corrida recreacional", w=536, tam=26, cor=TINTA, peso=700, lh=1.25),
       rot(1104, 230, "estudos observacionais: quem segue correndo pode ter a articulação mais tolerante", w=536, tam=22, cor=MUDO, peso=700, lh=1.3),
       rot(1104, 340, "até 15 anos, e possivelmente mais", w=536, tam=24, cor=OXID, peso=700)]
diagrama(S, "joelho", 420, p, rs, eyebrow="Artrose de quadril e joelho, metanálise de 2017", titulo="O corredor recreacional tem menos artrose que o sedentário",
         fonte="J Orthop Sports Phys Ther 2017")

# 6. o que prediz
p = [svg_abre(1664, 440, "Duas colunas. Prediz: lesão prévia, ser novato, mudança brusca de volume. Vendido como preditor, sem sustentação: tipo de pisada; coorte de 927 novatos com o mesmo tênis neutro, 252 lesionados, sem diferença entre os tipos de pé")]
rs = []
p.append(caixa(0, 0, 780, 440, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:check", 24, 24, 48, OXID))
rs.append(rot(90, 28, "Prediz", w=660, tam=32, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["lesão prévia: o fator mais consistente", "ser novato", "mudança brusca de volume"]):
    rs.append(rot(24, 120 + j * 90, t, w=732, tam=28, cor=TINTA, peso=700))
p.append(caixa(884, 0, 780, 440, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:x", 908, 24, 48, FOSF))
rs.append(rot(974, 28, "Vendido como preditor", w=660, tam=32, cor=FOSF, peso=700, serif=True))
rs.append(rot(908, 110, "tipo de pisada", w=732, tam=30, cor=TINTA, peso=700))
for j, (n, t) in enumerate([("927", "novatos, mesmo tênis neutro"), ("252", "lesionados em um ano"), ("0", "diferença entre os tipos de pé")]):
    y = 180 + j * 80
    rs += [rot(908, y, n, w=140, tam=36, cor=FOSF, peso=700, serif=True), rot(1060, y + 8, t, w=580, tam=24, cor=TINTA, peso=700)]
diagrama(S, "preditores", 440, p, rs, eyebrow="O que prediz a lesão, e o que não", titulo="No primeiro dia, pergunte a lesão prévia, não a pisada",
         fonte="Br J Sports Med 2014")

# 7. a balança
p = [svg_abre(1664, 440, "Duas curvas de sobrevida ao longo de 15 anos: corredores acima, não corredores abaixo. 30% menos mortalidade por qualquer causa, 45% menos cardiovascular. A partir de 5 a 10 minutos por dia, em ritmo lento. 55.137 adultos, seguimento médio de 15 anos")]
rs = []
p.append(f'<line x1="60" y1="380" x2="900" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="40" x2="60" y2="380" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M 60 60 C 400 80 700 120 900 150" stroke="{OXID}" stroke-width="6" fill="none"/>')
p.append(f'<path d="M 60 60 C 400 110 700 190 900 250" stroke="{MUDO}" stroke-width="6" fill="none"/>')
rs += [rot(620, 80, "corredores", w=260, tam=22, cor=OXID, peso=700, alinha="right"),
       rot(620, 260, "não corredores", w=260, tam=22, cor=MUDO, peso=700, alinha="right"),
       rot(60, 392, "15 anos", w=840, tam=20, cor=MUDO, alinha="right"),
       rot(80, 320, "esquema", w=200, tam=20, cor=MUDO)]
p.append(caixa(980, 0, 684, 440, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1004, 20, "−30%", w=300, tam=56, cor=OXID, peso=700, serif=True),
       rot(1304, 40, "mortalidade por qualquer causa", w=340, tam=22, cor=TINTA, peso=700, lh=1.2),
       rot(1004, 120, "−45%", w=300, tam=56, cor=OXID, peso=700, serif=True),
       rot(1304, 140, "mortalidade cardiovascular", w=340, tam=22, cor=TINTA, peso=700, lh=1.2),
       rot(1004, 240, "a partir de 5 a 10 minutos por dia, em ritmo lento", w=636, tam=26, cor=OXID, peso=700, lh=1.25),
       rot(1004, 360, "55.137 adultos · estudo observacional", w=636, tam=22, cor=MUDO, peso=700)]
diagrama(S, "balanca", 440, p, rs, eyebrow="O outro prato da balança, estudo de 2014", titulo="Correr pouco já reduz a mortalidade",
         fonte="J Am Coll Cardiol 2014")

# 8. a resposta ao treinador
p = [svg_abre(1664, 440, "Ficha da turma de quarenta iniciantes com quatro campos: definição de lesão combinada, lesão prévia no primeiro dia, registro semanal de dor e de sessões perdidas, rampa de volume. Resposta ao treinador: esperar algumas lesões, contar do mesmo jeito, reduzir pela rampa")]
rs = []
p.append(caixa(0, 0, 1000, 440, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(24, 20, "Ficha da turma", w=952, tam=30, cor=AZUL, peso=700, serif=True))
for j, (ic, t) in enumerate([("t:ruler-measure", "definição de lesão combinada: perder ou reduzir uma sessão"), ("t:zoom-question", "lesão prévia, perguntada no primeiro dia"),
                             ("t:calendar", "registro semanal: dor de 0 a 10 e sessões perdidas"), ("t:stairs", "rampa de volume")]):
    y = 90 + j * 86
    p.append(icone(ic, 24, y, 48, AZUL))
    rs.append(rot(90, y + 6, t, w=890, tam=26, cor=TINTA, peso=700))
p.append(caixa(1060, 0, 604, 440, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1084, 20, "A resposta honesta", w=556, tam=28, cor=FOSF, peso=700, serif=True),
       rot(1084, 90, "algumas pessoas vão se machucar", w=556, tam=28, cor=TINTA, peso=700, lh=1.2),
       rot(1084, 220, "o trabalho é que sejam poucas, leves e percebidas cedo", w=556, tam=28, cor=FOSF, peso=700, serif=True, lh=1.25)]
diagrama(S, "resposta", 440, p, rs, eyebrow="A resposta ao treinador", titulo="Contar do mesmo jeito, perguntar a lesão prévia e subir em rampa")

# 9. mover o ponto
p = [svg_abre(1664, 400, "A faixa de 3% a 85% com uma seta empurrando o ponto da turma da ponta alta para o meio. Três alavancas: rampa, força, dor percebida cedo"), defs(OXID)]
rs = []
faixa(p, rs, 60)
p.append(f'<circle cx="1250" cy="80" r="16" fill="{TINTA}"/>')
p.append(seta(1230, 150, 880, 150, OXID, "m0", 6))
rs.append(rot(1190, 160, "a turma", w=120, tam=20, cor=TINTA, peso=700, alinha="center"))
for j, (ic, t, x_) in enumerate([("t:stairs", "rampa", "segura o volume abaixo do que o tecido tolera"),
                                 ("t:barbell", "força", "aumenta o que o tecido tolera"),
                                 ("t:alert-triangle", "dor percebida cedo", "uma semana de ajuste em vez de semanas parado")]):
    x = j * 564
    p.append(caixa(x, 220, 536, 170, OXID, OXID_T, esp=3, rx=16))
    p.append(icone(ic, x + 20, 240, 48, OXID))
    rs += [rot(x + 84, 246, t, w=430, tam=28, cor=OXID, peso=700, serif=True), rot(x + 20, 310, x_, w=496, tam=22, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "mover", 400, p, rs, eyebrow="Dez semanas para mover um ponto", titulo="Três alavancas tiram a turma da ponta alta")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Epidemiologia de lesão no corredor recreacional", "titulo": "A corrida tem uma faixa de risco, e o treino escolhe o ponto",
          "regras": ["De três a oitenta e cinco por cento: o novato está na ponta alta",
                     "Lesão de sobrecarga; a lesão prévia prediz, a pisada não",
                     "Menos artrose que o sedentário, e menos mortalidade já em doses pequenas"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Pergunta a lesão prévia, avalia a dor que persiste e desmonta o mito do joelho."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Combina a definição de lesão, registra toda semana e monta a rampa."},
                    {"ic": "t:user", "t": "O corredor", "x": "Relata a dor cedo, em vez de esperar que ela passe correndo."}]})

salvar("13-08.json", {"arquivo": "aulas/MOD13/13-08-epidemiologia-de-lesao-no-corredor-recreacional.md",
                      "titulo": "Epidemiologia de lesão no corredor recreacional", "subtitulo": "Quantos se machucam, onde, e por quê",
                      "nota_capa": "Entra por uma turma de quarenta iniciantes numa assessoria de corrida.",
                      "secoes": {"turma": ["A pergunta.", "capa"], "faixa": ["Os números.", "faixa"],
                                 "resposta": ["A resposta ao treinador.", "resposta"]},
                      "slides": S})
