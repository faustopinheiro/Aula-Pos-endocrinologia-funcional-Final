"""Spec do deck 14.2. Gera 14-02.json ao lado deste arquivo."""
from _base import *

S = []

# 1. as quatro portas
p = [svg_abre(1664, 440, "Nadador amador na casa dos quarenta, tempos piores há três meses. Quatro portas, quatro respostas: treinador, descansa uma semana; nutricionista, falta carboidrato; médico, exames normais, é do treino; psicóloga, é estresse. Perfil típico")]
rs = []
p.append(f'<rect x="0" y="300" width="460" height="140" rx="12" fill="{AZUL_T}"/>')
p.append(f'<path d="M 0 330 Q 60 310 115 330 T 230 330 T 345 330 T 460 330" stroke="{AZUL}" stroke-width="4" fill="none"/>')
p.append(icone("t:swimming", 150, 120, 160, AZUL))
p.append(icone("t:stopwatch", 20, 20, 64, FOSF))
rs += [rot(100, 30, "tempos piores há três meses", w=360, tam=24, cor=FOSF, peso=700, lh=1.2),
       rot(20, 360, "cansado o dia inteiro, irritado", w=420, tam=22, cor=TINTA, peso=700),
       rot(20, 400, "perfil típico", w=420, tam=20, cor=MUDO)]
for j, (quem, fala, c) in enumerate([("treinador", "“descansa uma semana”", GLIC), ("nutricionista", "“falta carboidrato”", OXID),
                                     ("médico", "“exames normais, é do treino”", AZUL), ("psicóloga", "“é estresse”", FOSF)]):
    x = 520 + j * 290
    p.append(f'<rect x="{x}" y="40" width="260" height="380" rx="12" fill="{CARTAO}" stroke="{c}" stroke-width="4"/>')
    p.append(f'<circle cx="{x + 226}" cy="230" r="10" fill="{c}"/>')
    rs += [rot(x + 16, 64, quem, w=228, tam=26, cor=c, peso=700, serif=True, alinha="center"),
           rot(x + 16, 140, fala, w=228, tam=26, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.25)]
diagrama(S, "portas", 440, p, rs, eyebrow="Natação em águas abertas, um amador na casa dos quarenta", titulo="Quatro portas deram quatro respostas, e nenhuma investigou tudo")

# 2. o roteiro
p = [svg_abre(1664, 380, "Cinco passos numa linha, a partir da porta de entrada: a conta inteira; os sinais que pulam a fila; quatro perguntas na mesma semana; exame com pergunta; descarga com data. Qualquer porta, o mesmo roteiro"), defs(TINTA)]
rs = []
p.append(icone("t:door", 0, 120, 96, TINTA))
rs.append(rot(0, 230, "qualquer porta", w=120, tam=20, cor=MUDO, peso=700, alinha="center"))
for j, (t, c, f) in enumerate([("a conta inteira", GLIC, GLIC_T), ("os sinais que pulam a fila", FOSF, FOSF_T),
                               ("quatro perguntas na mesma semana", AZUL, AZUL_T), ("exame com pergunta", OXID, OXID_T), ("descarga com data", TINTA, CARTAO)]):
    x = 150 + j * 304
    p.append(caixa(x, 60, 280, 220, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 140}" cy="60" r="34" fill="{c}"/>')
    rs += [rot(x + 110, 38, str(j + 1), w=60, tam=36, cor=PAPEL, peso=700, serif=True, alinha="center"),
           rot(x + 20, 130, t, w=240, tam=28, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.25)]
    if j < 4:
        p.append(seta(x + 282, 170, x + 300, 170, TINTA, "m0", esp=3))
rs.append(rot(150, 320, "Quem recebe não precisa fazer os cinco. Precisa garantir que os cinco aconteçam.", w=1514, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"))
diagrama(S, "roteiro", 380, p, rs, eyebrow="O procedimento", titulo="Cinco passos fazem qualquer porta levar à mesma investigação")

# 3. passo 1: a conta inteira
p = [svg_abre(1664, 440, "A conta dos últimos três meses do nadador. Débitos: treino, o volume subiu para a travessia; trabalho, mudou de cargo; sono, cerca de seis horas; doença recente, virose há dois meses. Entrada quase vazia: descanso. A pergunta: o que mudou, e quando. Perfil típico, valores ilustrativos")]
rs = []
B = 380
p.append(f'<line x1="0" y1="{B}" x2="1100" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
for j, (ic, t, x_, h, c) in enumerate([("t:swimming", "treino", "volume subiu para a travessia", 260, AZUL),
                                       ("t:briefcase", "trabalho", "mudou de cargo", 220, GLIC),
                                       ("t:zzz", "sono", "cerca de seis horas", 180, FOSF),
                                       ("t:mood-sick", "doença recente", "virose há dois meses", 140, MUDO)]):
    x = j * 230
    p.append(f'<rect x="{x}" y="{B - h}" width="190" height="{h}" rx="10" fill="{c}"/>')
    p.append(icone(ic, x + 67, B - h + 16, 56, PAPEL))
    rs += [rot(x, B - h - 92, t, w=190, tam=24, cor=c, peso=700, alinha="center"),
           rot(x, B - h - 58, x_, w=190, tam=20, cor=TINTA, peso=700, alinha="center", lh=1.15)]
p.append(f'<rect x="940" y="{B - 30}" width="160" height="30" rx="8" fill="{OXID}"/>')
rs += [rot(900, B - 80, "descanso", w=240, tam=24, cor=OXID, peso=700, alinha="center"),
       rot(0, B + 16, "débitos dos últimos três meses · perfil típico, valores ilustrativos", w=1100, tam=20, cor=MUDO)]
p.append(caixa(1180, 0, 484, 440, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1204, 24, "O que mudou, e quando?", w=436, tam=30, cor=AZUL, peso=700, serif=True, lh=1.2),
       rot(1204, 130, "queda que começa junto com uma mudança tem um suspeito", w=436, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1204, 260, "quem treina traz a carga das últimas semanas e um teste padronizado repetido", w=436, tam=24, cor=AZUL, peso=700, lh=1.25)]
diagrama(S, "conta", 440, p, rs, eyebrow="Passo 1 · a conta inteira", titulo="Antes de qualquer exame, a conta dos últimos três meses")

# 4. passo 2: os sinais que pulam a fila
p = [svg_abre(1664, 420, "Seis sinais com atalho direto para a medicina, na mesma semana: perda de peso sem intenção; febre ou suor noturno; gânglios aumentados; falta de ar desproporcional; dor no peito ou palpitação com desmaio; ideia de se matar"), defs(FOSF)]
rs = []
for j, t in enumerate(["perda de peso sem intenção", "febre ou suor noturno", "gânglios aumentados",
                       "falta de ar desproporcional", "dor no peito ou palpitação com desmaio", "ideia de se matar"]):
    x, y = (j % 3) * 380, (j // 3) * 170
    p.append(caixa(x, y, 350, 140, FOSF, FOSF_T, esp=3, rx=16))
    p.append(icone("t:alert-triangle", x + 20, y + 20, 44, FOSF))
    rs.append(rot(x + 76, y + 24, t, w=254, tam=24, cor=TINTA, peso=700, lh=1.25))
p.append(seta(1150, 160, 1250, 160, FOSF, "m0", esp=6))
p.append(caixa(1270, 40, 394, 240, FOSF, FOSF, esp=0, rx=18))
p.append(icone("h:doctor", 1420, 60, 90, PAPEL))
rs += [rot(1290, 170, "medicina, na mesma semana", w=354, tam=28, cor=PAPEL, peso=700, serif=True, alinha="center", lh=1.2),
       rot(0, 360, "ideia de se matar: a rampa de risco da conversa sobre encaminhamento", w=1664, tam=24, cor=FOSF, peso=700),
       rot(1270, 300, "sem nenhum: o roteiro segue com calma", w=394, tam=22, cor=OXID, peso=700, alinha="center", lh=1.2)]
diagrama(S, "fila", 420, p, rs, eyebrow="Passo 2 · os sinais que pulam a fila", titulo="Seis sinais tiram o caso da fila e levam à medicina já")

# 5. passo 3: em fila e em paralelo
p = [svg_abre(1664, 440, "Duas linhas do tempo. Em fila: medicina, depois nutrição, depois psicologia, depois sono, com semanas de espera entre elas; total, meses. Em paralelo: sono pela medicina, energia pela nutrição, humor pela psicologia, remédios e infecção recente pela medicina, todas na mesma semana; total, uma a duas semanas. Esquema, tempos ilustrativos")]
rs = []
rs += [rot(0, 0, "Em fila", w=300, tam=28, cor=MUDO, peso=700, serif=True),
       rot(0, 220, "Em paralelo", w=300, tam=28, cor=AZUL, peso=700, serif=True)]
for j, t in enumerate(["medicina", "nutrição", "psicologia", "sono"]):
    x = j * 330
    p.append(f'<rect x="{x}" y="50" width="200" height="60" rx="10" fill="{GRADE}"/>')
    rs.append(rot(x, 66, t, w=200, tam=22, cor=TINTA, peso=700, alinha="center"))
    if j < 3:
        p.append(f'<line x1="{x + 210}" y1="80" x2="{x + 320}" y2="80" stroke="{MUDO}" stroke-width="4"{TRACO}/>')
rs.append(rot(1340, 66, "meses", w=300, tam=30, cor=MUDO, peso=700, serif=True))
for j, (t, q, ic, c) in enumerate([("sono", "medicina", "t:zzz", AZUL), ("energia", "nutrição", "t:apple", OXID),
                                   ("humor", "psicologia", "t:brain", GLIC), ("remédios e infecção", "medicina", "t:pill", FOSF)]):
    x = j * 330
    p.append(caixa(x, 270, 300, 130, c, CARTAO, esp=3, rx=14))
    p.append(icone(ic, x + 16, 290, 44, c))
    rs += [rot(x + 70, 290, t, w=220, tam=24, cor=c, peso=700, lh=1.15), rot(x + 70, 350, q, w=220, tam=20, cor=TINTA, peso=700)]
rs += [rot(1340, 300, "uma a duas semanas", w=324, tam=30, cor=AZUL, peso=700, serif=True, lh=1.15),
       rot(1340, 410, "esquema, tempos ilustrativos", w=324, tam=20, cor=MUDO)]
diagrama(S, "paralelo", 440, p, rs, eyebrow="Passo 3 · quatro perguntas na mesma semana", titulo="As quatro perguntas vêm juntas, e não uma área depois da outra")

# 6. a apneia
p = [svg_abre(1664, 420, "Apneia do sono moderada ou grave por grupo, coorte populacional, estimativa de 2013: homens de 30 a 49 anos, 10%; homens de 50 a 70, 17%; mulheres de 30 a 49, 3%; mulheres de 50 a 70, 9%. A pergunta: alguém já viu você parar de respirar dormindo?")]
rs = []
B, K = 340, 14
for j, (t, v, c) in enumerate([("homens, 30 a 49", 10, FOSF), ("homens, 50 a 70", 17, FOSF), ("mulheres, 30 a 49", 3, AZUL), ("mulheres, 50 a 70", 9, AZUL)]):
    x = j * 230
    p.append(f'<rect x="{x + 30}" y="{B - v * K}" width="150" height="{v * K}" rx="10" fill="{c}"/>')
    rs += [rot(x, B - v * K - 50, f"{v}%", w=210, tam=34, cor=c, peso=700, serif=True, alinha="center"),
           rot(x, B + 12, t, w=210, tam=22, cor=TINTA, peso=700, alinha="center")]
p.append(f'<line x1="0" y1="{B}" x2="920" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
rs.append(rot(0, 390, "apneia moderada ou grave · coorte populacional, 2013", w=920, tam=20, cor=MUDO, peso=700))
p.append(caixa(1000, 0, 664, 420, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:zzz", 1024, 24, 64, AZUL))
rs += [rot(1024, 110, "“Alguém já viu você parar de respirar dormindo?”", w=616, tam=32, cor=AZUL, peso=700, serif=True, lh=1.25),
       rot(1024, 270, "dez segundos de pergunta; ser atleta não protege", w=616, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1024, 350, "sim → exame do sono, não mais descanso", w=616, tam=24, cor=FOSF, peso=700)]
diagrama(S, "apneia", 420, p, rs, eyebrow="Por que a pergunta do sono não é detalhe", titulo="Um em cada dez homens dos trinta aos quarenta e poucos tem apneia relevante",
         fonte="Am J Epidemiol 2013")

# 7. passo 4: exame com pergunta
p = [svg_abre(1664, 440, "Cada pergunta ligada ao exame que ela justifica. Sono: exame do sono, se há ronco ou pausas. Energia: hemograma e ferritina, e a conta da disponibilidade de energia. Humor: instrumento de rastreio, não exame de sangue. Remédios e infecção: revisão da lista, exame dirigido pelo achado. Riscado: o painel completo, sem pergunta"), defs(TINTA)]
rs = []
for j, (q, ex, c) in enumerate([("sono", "exame do sono, se há ronco ou pausas", AZUL), ("energia", "hemograma, ferritina e a conta da disponibilidade de energia", OXID),
                                ("humor", "instrumento de rastreio e conversa, não exame de sangue", GLIC), ("remédios e infecção", "revisão da lista; exame só se houver suspeito", FOSF)]):
    y = j * 110
    p.append(caixa(0, y, 280, 90, c, CARTAO, esp=3, rx=14))
    rs.append(rot(16, y + 26, q, w=248, tam=24, cor=c, peso=700, alinha="center"))
    p.append(seta(290, y + 45, 350, y + 45, TINTA, "m0", esp=3))
    rs.append(rot(370, y + 16, ex, w=640, tam=24, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(1100, 20, 564, 300, MUDO, CARTAO, esp=3, rx=18))
for k in range(6):
    p.append(f'<rect x="1140" y="{70 + k * 44}" width="{300 + (k % 3) * 60}" height="20" rx="6" fill="{GRADE}"/>')
p.append(f'<line x1="1120" y1="40" x2="1644" y2="300" stroke="{FOSF}" stroke-width="8"/>')
rs += [rot(1124, 340, "o painel completo, sem pergunta", w=516, tam=24, cor=FOSF, peso=700, alinha="center"),
       rot(1124, 380, "foi ele que permitiu “é do treino”", w=516, tam=20, cor=MUDO, peso=700, alinha="center")]
diagrama(S, "exame", 440, p, rs, eyebrow="Passo 4 · exame com pergunta", titulo="Cada exame responde a uma das quatro perguntas, ou não entra")

# 8. passo 5: descarga com data
p = [svg_abre(1664, 440, "Curva de carga semanal que desce em degrau e fica baixa por quatro a seis semanas, com uma bandeira na data de reavaliação. Quatro réguas na data: teste padronizado, esforço percebido para a mesma carga, questionário de humor e recuperação, sono. Quem treina conduz; todos reavaliam. Esquema")]
rs = []
X0, B = 40, 380
p.append(f'<line x1="{X0}" y1="{B}" x2="1000" y2="{B}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<path d="M {X0} 140 L 300 140 L 300 260 L 760 260 L 760 200 L 860 200 L 860 150 L 1000 150" stroke="{AZUL}" stroke-width="6" fill="none"/>')
p.append(f'<rect x="300" y="262" width="460" height="{B - 262}" fill="{AZUL_T}"/>')
p.append(f'<line x1="760" y1="60" x2="760" y2="{B}" stroke="{FOSF}" stroke-width="4"/>')
p.append(icone("t:flag", 760, 40, 52, FOSF))
rs += [rot(310, 290, "quatro a seis semanas, sem sair do esporte", w=430, tam=22, cor=AZUL, peso=700, alinha="center", lh=1.2),
       rot(560, 4, "data escrita", w=190, tam=22, cor=FOSF, peso=700, alinha="right"),
       rot(X0, 100, "carga", w=200, tam=20, cor=MUDO, peso=700),
       rot(800, 100, "volta em degraus se melhorar", w=200, tam=20, cor=AZUL, peso=700, lh=1.2),
       rot(X0, B + 14, "esquema", w=300, tam=20, cor=MUDO)]
p.append(caixa(1080, 0, 584, 440, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(1104, 20, "Na data, as mesmas quatro réguas", w=536, tam=28, cor=FOSF, peso=700, serif=True, lh=1.2))
for j, t in enumerate(["teste padronizado", "esforço percebido para a mesma carga", "questionário de humor e recuperação", "sono"]):
    rs.append(rot(1104, 110 + j * 52, "· " + t, w=536, tam=22, cor=TINTA, peso=700))
rs.append(rot(1104, 336, "não melhorou: o caso sobe de camada e segue o fluxo de encaminhamento", w=536, tam=22, cor=FOSF, peso=700, lh=1.25))
diagrama(S, "descarga", 440, p, rs, eyebrow="Passo 5 · descarga com data", titulo="A descarga é conduta, com data marcada para reavaliar")

# 9. a ficha do nadador
p = [svg_abre(1664, 440, "A ficha do nadador depois da semana das quatro perguntas. Sono: ronco e pausas vistas pela esposa, exame do sono, medicina. Energia: cortou carboidrato à noite, nutrição. Humor: interesse preservado fora do treino, psicologia acompanha. Remédios: betabloqueador para pressão há quatro meses, medicina revisa. Nenhum achado explica tudo sozinho. Perfil típico")]
rs = []
for j, (ic, q, achado, dono, c) in enumerate([("t:zzz", "Sono", "ronco e pausas vistas pela esposa", "exame do sono · medicina", AZUL),
                                              ("t:apple", "Energia", "cortou o carboidrato da noite", "ajuste · nutrição", OXID),
                                              ("t:brain", "Humor", "interesse preservado fora do treino", "acompanha o cargo novo · psicologia", GLIC),
                                              ("t:pill", "Remédios", "betabloqueador para pressão há quatro meses", "revisa a escolha · medicina", FOSF)]):
    x = j * 418
    p.append(caixa(x, 0, 390, 340, c, CARTAO, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 52, c))
    rs += [rot(x + 92, 34, q, w=280, tam=28, cor=c, peso=700, serif=True),
           rot(x + 24, 110, achado, w=342, tam=24, cor=TINTA, peso=700, lh=1.25),
           rot(x + 24, 250, dono, w=342, tam=22, cor=c, peso=700, lh=1.25)]
p.append(caixa(0, 370, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs += [rot(20, 388, "Nenhum achado explica tudo sozinho, e cada um tem dono.", w=1300, tam=26, cor=PAPEL, peso=700, alinha="center"),
       rot(1340, 392, "perfil típico", w=300, tam=20, cor=PAPEL, alinha="right")]
diagrama(S, "ficha", 440, p, rs, eyebrow="O roteiro aplicado ao nadador", titulo="A semana das quatro perguntas achou o que as quatro portas não viram")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Caso integrado: fadiga no amador", "titulo": "A porta recebe; o roteiro investiga",
          "regras": ["Quem recebe garante os cinco passos, mesmo sem fazer todos",
                     "Seis sinais pulam a fila; sem eles, quatro perguntas em paralelo",
                     "O exame responde a uma pergunta, e a descarga tem data"],
          "cards": [{"ic": "h:doctor", "t": "Medicina", "x": "Triagem dos seis sinais, pergunta do sono, revisão dos remédios e o exame que responde."},
                    {"ic": "t:users", "t": "Nutrição, psicologia e quem treina", "x": "Fazem as suas perguntas na mesma semana; quem treina conduz a descarga."},
                    {"ic": "t:user", "t": "O praticante", "x": "Conta tudo, inclusive o remédio novo e o ronco."}]})

salvar("14-02.json", {"arquivo": "aulas/MOD14/14-02-caso-integrado-amador-com-fadiga-e-queda-de-rendimento.md",
                      "titulo": "Caso integrado 2: amador com fadiga e queda de rendimento", "subtitulo": "Cinco passos para qualquer porta",
                      "nota_capa": "Entra por um nadador amador que ouviu quatro respostas em quatro portas.",
                      "secoes": {"portas": ["O problema.", "capa"], "roteiro": ["O procedimento.", "roteiro"],
                                 "paralelo": ["As quatro perguntas.", "paralelo"], "ficha": ["O roteiro aplicado.", "ficha"]},
                      "slides": S})
