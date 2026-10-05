"""Spec do deck 14.7. Gera 14-07.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o departamento médico
p = [svg_abre(1664, 420, "Departamento médico de um clube de futebol. Jogador na casa dos vinte em tratamento para depressão há dois meses, com remédio. Na porta, o diretor de futebol: o que ele tem? Por que está rendendo menos? No celular de alguém, um grupo de mensagens com a planilha de sono e frequência cardíaca do elenco. Perfil típico")]
rs = []
p.append(caixa(0, 0, 640, 420, AZUL, AZUL_T, esp=3, rx=18))
p.append(menino(160, 360, 260, TINTA))
p.append(icone("t:pill", 260, 200, 64, AZUL))
rs += [rot(340, 200, "tratamento para depressão, há dois meses", w=280, tam=24, cor=AZUL, peso=700, lh=1.25),
       rot(24, 24, "departamento médico", w=592, tam=24, cor=AZUL, peso=700, serif=True),
       rot(340, 330, "perfil típico", w=280, tam=20, cor=MUDO)]
p.append(icone("t:door", 700, 40, 90, MUDO))
p.append(caixa(820, 0, 844, 190, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(844, 20, "o diretor de futebol", w=796, tam=22, cor=MUDO, peso=700),
       rot(844, 64, "“O que ele tem? Por que está rendendo menos?”", w=796, tam=32, cor=FOSF, peso=700, serif=True, lh=1.25)]
p.append(caixa(820, 230, 844, 190, GLIC, GLIC_T, esp=3, rx=18))
p.append(icone("t:device-mobile", 844, 260, 64, GLIC))
rs.append(rot(924, 262, "a planilha de sono e frequência cardíaca do elenco, num grupo de mensagens da comissão", w=716, tam=24, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "sala", 420, p, rs, eyebrow="Futebol profissional, um jogador na casa dos vinte", titulo="Quem paga é o clube; quem é paciente é o jogador")

# 2. as três saídas
p = [svg_abre(1664, 440, "Três saídas. A: contar ao clube o diagnóstico, quem paga tem direito de saber. B: não contar nada a ninguém, é sigilo. C: separar o que a equipe precisa para trabalhar do diagnóstico, e só contar o diagnóstico com consentimento escrito. Pergunta: o que decide o caminho?")]
rs = []
for j, (l, t, c, f) in enumerate([("A", "contar ao clube o diagnóstico: quem paga tem direito de saber", FOSF, FOSF_T),
                                   ("B", "não contar nada a ninguém: é sigilo", GLIC, GLIC_T),
                                   ("C", "separar o que a equipe precisa do diagnóstico; o diagnóstico, só com consentimento escrito", OXID, OXID_T)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 320, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 268}" cy="80" r="50" fill="{c}"/>')
    rs += [rot(x + 218, 52, l, w=100, tam=48, cor=PAPEL, peso=700, alinha="center", serif=True),
           rot(x + 28, 160, t, w=480, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Antes de escolher: o que torna a decisão difícil, e o que as regras dizem", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saidas", 440, p, rs, eyebrow="A encruzilhada", titulo="Três jeitos de responder ao diretor que bate à porta")

# 3. a dupla lealdade
p = [svg_abre(1664, 420, "O profissional de saúde no centro, puxado por duas cordas. De um lado, o clube: contrata, paga, quer resultado. Do outro, o atleta: é o paciente, confia, tem direito ao sigilo. Dupla lealdade. Outros exemplos do mesmo conflito: o patrocinador do suplemento, a federação, a família do atleta menor")]
rs = []
p.append(f'<path d="M 340 170 Q 580 140 760 170" stroke="{GLIC}" stroke-width="10" fill="none"/>')
p.append(f'<path d="M 900 170 Q 1080 140 1320 170" stroke="{AZUL}" stroke-width="10" fill="none"/>')
p.append(menino(830, 300, 220, TINTA))
p.append(caixa(0, 60, 340, 220, GLIC, GLIC_T, esp=3, rx=18))
rs += [rot(20, 80, "o clube", w=300, tam=30, cor=GLIC, peso=700, serif=True, alinha="center"),
       rot(20, 140, "contrata, paga, quer resultado", w=300, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.25)]
p.append(caixa(1324, 60, 340, 220, AZUL, AZUL_T, esp=3, rx=18))
rs += [rot(1344, 80, "o atleta", w=300, tam=30, cor=AZUL, peso=700, serif=True, alinha="center"),
       rot(1344, 140, "é o paciente, confia, tem direito ao sigilo", w=300, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.25),
       rot(630, 310, "dupla lealdade", w=400, tam=32, cor=FOSF, peso=700, serif=True, alinha="center"),
       rot(0, 370, "o mesmo conflito: o patrocinador do suplemento · a federação · a família do atleta menor", w=1664, tam=24, cor=MUDO, peso=700, alinha="center")]
diagrama(S, "lealdade", 420, p, rs, eyebrow="O que torna a decisão difícil", titulo="O profissional contratado pelo clube atende o atleta")

# 4. as regras
p = [svg_abre(1664, 420, "Duas regras. Código de Ética Médica, artigo 73: vedado revelar fato conhecido no exercício da profissão, salvo por motivo justo, dever legal ou consentimento por escrito do paciente. Lei de proteção de dados, artigo 11: dado de saúde é sensível; consentimento específico e destacado, para finalidades específicas. Cada profissão tem o seu código, com regras de sigilo")]
rs = []
p.append(caixa(0, 0, 800, 330, AZUL, CARTAO, esp=3, rx=18))
rs += [rot(24, 20, "Código de Ética Médica · art. 73", w=752, tam=26, cor=AZUL, peso=700, serif=True),
       rot(24, 80, "vedado revelar o que soube no exercício da profissão, salvo:", w=752, tam=24, cor=TINTA, peso=700, lh=1.25)]
for j, t in enumerate(["motivo justo", "dever legal", "consentimento por escrito do paciente"]):
    p.append(f'<circle cx="44" cy="{178 + j * 50}" r="10" fill="{AZUL}"/>')
    rs.append(rot(66, 164 + j * 50, t, w=700, tam=24, cor=TINTA, peso=700))
p.append(caixa(864, 0, 800, 330, OXID, CARTAO, esp=3, rx=18))
rs += [rot(888, 20, "Lei de proteção de dados · art. 11", w=752, tam=26, cor=OXID, peso=700, serif=True),
       rot(888, 80, "dado de saúde é dado sensível", w=752, tam=24, cor=TINTA, peso=700),
       rot(888, 140, "consentimento específico e destacado, para finalidades específicas", w=752, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(888, 240, "consentimento genérico no contrato não cobre tudo", w=752, tam=24, cor=FOSF, peso=700, lh=1.25),
       rot(0, 370, "“O clube paga” não está entre as exceções. E cada profissão tem o seu código, com regras de sigilo.", w=1664, tam=24, cor=TINTA, peso=700, serif=True, alinha="center")]
diagrama(S, "regras", 420, p, rs, eyebrow="O que as regras dizem", titulo="Quem paga não está entre as exceções do sigilo",
         fonte="Res. CFM 2.217/2018 · Lei 13.709/2018")

# 5. saída A
p = [svg_abre(1664, 400, "Saída A: o diagnóstico sai da sala e se espalha: diretor, técnico, grupo de mensagens, imprensa. Consequências: quebra de sigilo; o jogador para de contar; o próximo atleta não procura o departamento. O sigilo protege o próximo atendimento"), defs(FOSF)]
rs = []
p.append(caixa(0, 120, 220, 160, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(10, 176, "diagnóstico", w=200, tam=24, cor=FOSF, peso=700, serif=True, alinha="center"))
for j, (t, ic) in enumerate([("diretor", "t:user"), ("técnico", "t:clipboard-list"), ("grupo de mensagens", "t:messages"), ("imprensa", "t:microphone")]):
    x = 300 + j * 210
    p.append(seta(x - 70, 200, x - 10, 200, FOSF, "m0", esp=4))
    p.append(icone(ic, x + 40, 150, 72, FOSF))
    rs.append(rot(x - 10, 240, t, w=180, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.2))
p.append(caixa(1180, 0, 484, 400, FOSF, FOSF_T, esp=3, rx=18))
for j, t in enumerate(["quebra de sigilo, sem exceção que a justifique", "o jogador para de contar ao departamento", "o próximo atleta não procura o departamento"]):
    p.append(icone("t:x", 1204, 30 + j * 110, 40, FOSF))
    rs.append(rot(1256, 30 + j * 110, t, w=388, tam=24, cor=TINTA, peso=700, lh=1.25))
rs.append(rot(0, 340, "O sigilo protege o próximo atendimento.", w=1140, tam=28, cor=FOSF, peso=700, serif=True))
diagrama(S, "saida_a", 400, p, rs, eyebrow="Saída A · contar ao clube", titulo="Contar ao clube ensina o atleta a não contar mais")

# 6. saída B
p = [svg_abre(1664, 400, "Saída B: uma parede entre o departamento médico e a comissão técnica. Do lado da comissão, o técnico planeja carga cheia e jogo no sábado. Consequências: a equipe trabalha às cegas; o atleta pode ser sobrecarregado; o departamento vira ilha. Sigilo não é silêncio")]
rs = []
p.append(caixa(0, 40, 440, 280, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(20, 60, "departamento médico", w=400, tam=26, cor=AZUL, peso=700, serif=True, alinha="center"))
p.append(f'<rect x="470" y="0" width="60" height="320" fill="{MUDO}"/>')
for k in range(6):
    p.append(f'<line x1="470" y1="{k * 60}" x2="530" y2="{k * 60}" stroke="{PAPEL}" stroke-width="3"/>')
p.append(caixa(560, 40, 440, 280, GLIC, GLIC_T, esp=3, rx=18))
rs += [rot(580, 60, "comissão técnica", w=400, tam=26, cor=GLIC, peso=700, serif=True, alinha="center"),
       rot(580, 150, "“carga cheia, jogo no sábado”", w=400, tam=26, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.25)]
p.append(caixa(1060, 0, 604, 400, MUDO, CARTAO, esp=3, rx=18))
for j, t in enumerate(["a equipe trabalha às cegas", "o atleta pode ser sobrecarregado quando precisa de ajuste", "o departamento vira ilha"]):
    p.append(icone("t:x", 1084, 30 + j * 110, 40, FOSF))
    rs.append(rot(1136, 30 + j * 110, t, w=508, tam=24, cor=TINTA, peso=700, lh=1.25))
rs.append(rot(0, 346, "Sigilo não é silêncio.", w=1000, tam=30, cor=FOSF, peso=700, serif=True, alinha="center"))
diagrama(S, "saida_b", 400, p, rs, eyebrow="Saída B · não contar nada", titulo="Não contar nada deixa a equipe trabalhando às cegas")

# 7. saída C: duas camadas
p = [svg_abre(1664, 460, "Saída C, duas camadas. Em cima, o que a equipe precisa: disponível para treino com ajuste de carga; pode jogar no sábado até 60 minutos; reavaliação em duas semanas. Embaixo, trancado: o diagnóstico e o tratamento, só com consentimento escrito, específico, para uma finalidade. Antes de falar com a equipe, combine com o atleta o que vai ser dito. Valores ilustrativos")]
rs = []
p.append(caixa(0, 0, 1100, 200, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(24, 16, "o que a equipe precisa para trabalhar", w=1052, tam=26, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["disponível para treino, com ajuste de carga", "pode jogar no sábado, até 60 minutos", "reavaliação em duas semanas"]):
    rs.append(rot(24 + j * 360, 90, t, w=340, tam=24, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(0, 230, 1100, 200, TINTA, TINTA, esp=0, rx=18))
p.append(icone("t:lock", 24, 260, 64, PAPEL))
rs += [rot(110, 256, "o diagnóstico e o tratamento", w=966, tam=28, cor=PAPEL, peso=700, serif=True),
       rot(110, 320, "só com consentimento escrito, específico, para uma finalidade: por exemplo, o psicólogo do clube no cuidado", w=966, tam=22, cor=PAPEL, peso=700, lh=1.3),
       rot(0, 438, "valores ilustrativos", w=400, tam=20, cor=MUDO)]
p.append(caixa(1160, 0, 504, 430, FOSF, FOSF_T, esp=3, rx=18))
p.append(icone("t:messages", 1184, 24, 56, FOSF))
rs += [rot(1184, 100, "Regra de ordem", w=456, tam=28, cor=FOSF, peso=700, serif=True),
       rot(1184, 160, "antes de falar com a equipe, combine com o atleta o que vai ser dito, e com que palavras", w=456, tam=24, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "camadas", 460, p, rs, eyebrow="Saída C · duas camadas", titulo="A equipe recebe disponibilidade e prazo; o diagnóstico fica trancado")

# 8. o acordo de informação
p = [svg_abre(1664, 420, "Acordo de informação assinado no início do vínculo, com quatro linhas: o que a equipe recebe, disponibilidade, restrições, prazo; o que só sai com autorização específica, diagnóstico, tratamento, saúde mental; quem vê os dados de monitoramento e para quê; atleta menor, os pais assinam e o atleta participa. Combinar antes do problema")]
rs = []
p.append(caixa(0, 0, 1100, 420, AZUL, CARTAO, esp=3, rx=14))
rs.append(rot(24, 18, "Acordo de informação · assinado no início do vínculo", w=1052, tam=26, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["o que a equipe recebe sempre: disponibilidade, restrições, prazo", "o que só sai com autorização específica: diagnóstico, tratamento, saúde mental",
                       "quem vê os dados de monitoramento, e para quê", "atleta menor de idade: os pais assinam, e o atleta participa"]):
    y = 90 + j * 76
    p.append(f'<line x1="24" y1="{y - 10}" x2="1076" y2="{y - 10}" stroke="{GRADE}" stroke-width="2"/>')
    rs += [rot(24, y, f"{j + 1}.", w=40, tam=26, cor=AZUL, peso=700, serif=True), rot(72, y + 2, t, w=1004, tam=24, cor=TINTA, peso=700, lh=1.25)]
p.append(f'<path d="M 760 400 q 30 -40 60 0 t 60 0 t 60 0" stroke="{AZUL}" stroke-width="4" fill="none"/>')
p.append(caixa(1160, 0, 504, 420, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1184, 24, "Combinar antes do problema", w=456, tam=28, cor=OXID, peso=700, serif=True, lh=1.2),
       rot(1184, 150, "o diretor recebe a camada de cima e sabe de antemão que a de baixo não é dele", w=456, tam=24, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "acordo", 420, p, rs, eyebrow="Combinar antes do problema", titulo="Um acordo assinado no início evita a discussão na porta")

# 9. onde o dado vaza
p = [svg_abre(1664, 420, "Três vazamentos e o que fazer. Grupo de mensagens com a planilha do elenco: acesso por função, em lugar controlado. Imprensa e redes sociais: nada de diagnóstico sem autorização; o clube fala de disponibilidade. Conversa de corredor: o caso se discute na sala, com quem cuida. Motivo justo existe: risco grave para o atleta ou para outros, como na rampa de risco de suicídio")]
rs = []
for j, (ic, t, x_) in enumerate([("t:messages", "grupo de mensagens", "acesso por função, em lugar controlado"),
                                 ("t:microphone", "imprensa e redes", "o clube fala de disponibilidade; diagnóstico, só com autorização"),
                                 ("t:users", "conversa de corredor", "o caso se discute na sala, com quem cuida")]):
    x = j * 564
    p.append(caixa(x, 0, 536, 280, GLIC, CARTAO, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 56, GLIC))
    rs += [rot(x + 96, 34, t, w=416, tam=26, cor=GLIC, peso=700, serif=True), rot(x + 24, 120, x_, w=488, tam=24, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(0, 310, 1664, 110, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(24, 330, "Motivo justo existe: risco grave para o atleta ou para outros, como na rampa de risco de suicídio. Exceção pensada e registrada, não atalho.", w=1616, tam=24, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "vazamento", 420, p, rs, eyebrow="Onde o dado vaza", titulo="O dado de saúde vaza por três caminhos conhecidos")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Ética, sigilo e proteção de dados", "titulo": "Sigilo não é silêncio, e quem paga não é exceção",
          "regras": ["Exceções: motivo justo, dever legal ou consentimento escrito específico",
                     "Equipe recebe disponibilidade, restrições e prazo; o diagnóstico fica",
                     "Acordo de informação no início, e acesso aos dados por função"],
          "cards": [{"ic": "h:doctor", "t": "Profissionais de saúde", "x": "Guardam o diagnóstico pelo seu código e passam à equipe a camada de cima."},
                    {"ic": "t:clipboard-list", "t": "Quem treina e quem dirige", "x": "Trabalham com disponibilidade e restrições, sem pedir o resto."},
                    {"ic": "t:user", "t": "O atleta", "x": "Decide, por escrito, o que mais sai da sala."}]})

salvar("14-07.json", {"arquivo": "aulas/MOD14/14-07-etica-sigilo-e-protecao-de-dados.md",
                      "titulo": "Ética, sigilo e proteção de dados", "subtitulo": "Três saídas para o diretor que bate à porta",
                      "nota_capa": "Entra por um jogador em tratamento para depressão e um diretor que quer saber o que ele tem.",
                      "secoes": {"sala": ["A decisão.", "capa"], "lealdade": ["O conflito e as regras.", "lealdade"],
                                 "saida_a": ["As três saídas.", "saida_a"], "acordo": ["Combinar antes.", "acordo"]},
                      "slides": S})
