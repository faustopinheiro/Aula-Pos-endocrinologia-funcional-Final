"""Spec do deck 14.5. Gera 14-05.json ao lado deste arquivo."""
from _base import *

S = []

def bola_rugbi(cx, cy, r, cor):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * 0.62:.0f}" fill="{cor}"/>'
            f'<line x1="{cx - r * 0.45:.0f}" y1="{cy}" x2="{cx + r * 0.45:.0f}" y2="{cy}" stroke="{PAPEL}" stroke-width="4"/>'
            + "".join(f'<line x1="{cx + k}" y1="{cy - 8}" x2="{cx + k}" y2="{cy + 8}" stroke="{PAPEL}" stroke-width="3"/>' for k in (-18, -6, 6, 18)))

# 1. o campo
p = [svg_abre(1664, 420, "Clube de rúgbi amador, três pancadas na cabeça na mesma temporada. Primeira: voltou ao jogo no mesmo dia. Segunda: pronto-socorro, tomografia, liberado sem orientação. Terceira: uma semana parado, voltou ao contato sem avaliação. Três pessoas, três condutas, nenhum protocolo. Perfil típico")]
rs = []
p.append(bola_rugbi(120, 120, 90, GLIC))
rs.append(rot(0, 230, "perfil típico", w=240, tam=20, cor=MUDO, alinha="center"))
for j, (t, x_, c) in enumerate([("1ª pancada", "voltou ao jogo no mesmo dia", FOSF),
                                ("2ª pancada", "pronto-socorro, tomografia, liberado sem orientação de retorno", GLIC),
                                ("3ª pancada", "uma semana parado, voltou ao contato sem avaliação", AZUL)]):
    x = 300 + j * 460
    p.append(caixa(x, 0, 430, 260, c, CARTAO, esp=3, rx=18))
    p.append(f'<circle cx="{x + 50}" cy="50" r="26" fill="{c}"/>')
    rs += [rot(x + 90, 34, t, w=320, tam=26, cor=c, peso=700, serif=True), rot(x + 24, 110, x_, w=382, tam=24, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(300, 300, 1364, 100, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(320, 330, "Três pessoas, três condutas, nenhum protocolo.", w=1324, tam=30, cor=PAPEL, peso=700, serif=True, alinha="center"))
diagrama(S, "campo", 420, p, rs, eyebrow="Rúgbi amador, uma temporada", titulo="Três pancadas na cabeça, três condutas diferentes")

# 2. diretriz e protocolo
p = [svg_abre(1664, 420, "Duas colunas. Diretriz: escrita por especialistas, para todos os lugares, longa, com níveis de evidência. Protocolo: escrito para este lugar, com estas pessoas, cabe numa página, diz quem faz o quê. Uma seta da diretriz para o protocolo: adaptar, não copiar"), defs(TINTA)]
rs = []
p.append(caixa(0, 0, 640, 420, MUDO, CARTAO, esp=3, rx=18))
for k in range(9):
    p.append(f'<rect x="40" y="{110 + k * 30}" width="{480 + (k % 3) * 30}" height="14" rx="5" fill="{GRADE}"/>')
rs += [rot(24, 20, "Diretriz", w=592, tam=32, cor=MUDO, peso=700, serif=True),
       rot(24, 66, "para todos os lugares, longa, com níveis de evidência", w=592, tam=22, cor=TINTA, peso=700)]
p.append(seta(660, 210, 1000, 210, TINTA, "m0", esp=5))
rs.append(rot(660, 160, "adaptar, não copiar", w=340, tam=26, cor=FOSF, peso=700, serif=True, alinha="center"))
p.append(caixa(1024, 0, 640, 420, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1048, 20, "Protocolo", w=592, tam=32, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["para este lugar", "com estas pessoas", "cabe numa página", "diz quem faz o quê, quando, com qual critério"]):
    rs.append(rot(1048, 100 + j * 72, "· " + t, w=592, tam=26, cor=TINTA, peso=700))
diagrama(S, "diretriz", 420, p, rs, eyebrow="O que é um protocolo", titulo="O protocolo é a diretriz traduzida para um lugar e suas pessoas")

# 3. passo 1: escolher o problema
p = [svg_abre(1664, 440, "Três critérios para escolher o problema: se repete; custa caro quando dá errado; cada um faz de um jeito. Vários problemas como pontos; a concussão no ponto em que os três se cruzam")]
rs = []
for (cx, cy, c, t) in [(360, 170, AZUL, "se repete"), (560, 170, GLIC, "custa caro quando dá errado"), (460, 320, FOSF, "cada um faz de um jeito")]:
    p.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="{c}" opacity="0.18" stroke="{c}" stroke-width="4"/>')
rs += [rot(140, 0, "se repete", w=300, tam=24, cor=AZUL, peso=700, alinha="center"),
       rot(500, 0, "custa caro quando dá errado", w=340, tam=24, cor=GLIC, peso=700, alinha="center"),
       rot(300, 400, "cada um faz de um jeito", w=320, tam=24, cor=FOSF, peso=700, alinha="center")]
p.append(f'<circle cx="460" cy="220" r="22" fill="{TINTA}"/>')
rs.append(rot(380, 250, "concussão", w=160, tam=24, cor=TINTA, peso=700, serif=True, alinha="center"))
for (x, y) in [(260, 120), (640, 110), (520, 380), (320, 330), (700, 230)]:
    p.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{MUDO}"/>')
p.append(caixa(940, 40, 724, 360, TINTA, CARTAO, esp=3, rx=18))
rs += [rot(964, 64, "Passo 1 · escolher o problema", w=676, tam=28, cor=TINTA, peso=700, serif=True),
       rot(964, 140, "um departamento com cinquenta protocolos não segue nenhum", w=676, tam=24, cor=FOSF, peso=700, lh=1.25),
       rot(964, 250, "a concussão do clube cumpre os três: toda temporada, erro grave, três condutas", w=676, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "problema", 440, p, rs, eyebrow="Passo 1", titulo="Protocolo é para o problema que se repete, custa caro e varia")

# 4. passo 2: o filtro da diretriz
p = [svg_abre(1664, 420, "Uma diretriz passando por um filtro de seis domínios: propósito e alcance; quem participou; rigor do desenvolvimento; clareza; aplicabilidade; independência editorial. 23 itens em 6 domínios, instrumento de 2010. A pergunta: esta diretriz merece virar o nosso protocolo?"), defs(TINTA)]
rs = []
p.append(f'<path d="M 0 40 L 560 40 L 380 260 L 380 380 L 180 380 L 180 260 Z" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="4"/>')
rs += [rot(60, 90, "23 itens", w=440, tam=44, cor=AZUL, peso=700, serif=True, alinha="center"),
       rot(60, 160, "em 6 domínios", w=440, tam=28, cor=AZUL, peso=700, alinha="center"),
       rot(130, 388, "instrumento de 2010", w=300, tam=20, cor=MUDO, peso=700, alinha="center")]
for j, t in enumerate(["propósito e alcance", "quem participou", "rigor do desenvolvimento", "clareza", "aplicabilidade", "independência editorial"]):
    x, y = 640 + (j % 2) * 360, (j // 2) * 92
    p.append(caixa(x, y, 330, 72, AZUL, CARTAO, esp=2, rx=12))
    rs.append(rot(x + 16, y + 20, t, w=298, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(640, 300, 1024, 120, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(664, 320, "Esta diretriz merece virar o nosso protocolo? Para concussão: o consenso de 2022 passa com folga.", w=976, tam=24, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "filtro", 420, p, rs, eyebrow="Passo 2 · escolher a diretriz de partida", titulo="Seis perguntas decidem se a diretriz merece virar protocolo",
         fonte="CMAJ 2010")

# 5. passo 2: adaptar ao lugar
p = [svg_abre(1664, 420, "A diretriz, longa, e as perguntas de adaptação ao clube: quem está presente no treino? Tem médico no jogo? Qual o pronto-socorro mais perto? Quem pode retirar um jogador? Quem libera o contato? Traduzir para este lugar")]
rs = []
for j, (ic, t) in enumerate([("t:users", "quem está presente no treino de terça?"), ("h:doctor", "tem médico no jogo de sábado?"),
                             ("t:route", "qual o pronto-socorro mais perto, e a quantos minutos?"), ("t:flag", "quem tem autoridade para retirar um jogador?"),
                             ("t:check", "quem libera a volta ao contato?")]):
    y = j * 80
    p.append(caixa(0, y, 1060, 64, GLIC, CARTAO, esp=2, rx=12))
    p.append(icone(ic, 16, y + 12, 40, GLIC))
    rs.append(rot(76, y + 16, t, w=960, tam=26, cor=TINTA, peso=700))
p.append(caixa(1120, 0, 544, 420, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1144, 24, "As respostas mudam o protocolo", w=496, tam=28, cor=OXID, peso=700, serif=True, lh=1.2),
       rot(1144, 140, "sem médico no treino, “retirar e avaliar” precisa dizer quem retira, como, e para onde o jogador vai depois", w=496, tam=24, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "adaptar", 420, p, rs, eyebrow="Passo 2 · adaptar ao lugar", titulo="A diretriz pressupõe recursos que o clube talvez não tenha")

# 6. passo 3: a página
p = [svg_abre(1664, 460, "O protocolo em uma página, sete partes: para que serve; a quem se aplica; gatilho, qualquer sinal de concussão; quem faz o quê, em ordem; o que fazer quando a pessoa responsável não está; o que se registra; versão, data e próxima revisão. Verbos no imperativo: retire, não volte no mesmo dia, encaminhe, registre")]
rs = []
p.append(caixa(0, 0, 900, 460, TINTA, CARTAO, esp=3, rx=14))
for j, t in enumerate(["para que serve", "a quem se aplica", "gatilho: qualquer sinal de concussão", "quem faz o quê, em ordem",
                       "quando a pessoa responsável não está", "o que se registra", "versão, data e próxima revisão"]):
    y = 20 + j * 62
    p.append(f'<circle cx="44" cy="{y + 22}" r="18" fill="{FOSF if j == 4 else TINTA}"/>')
    rs += [rot(29, y + 8, str(j + 1), w=30, tam=20, cor=PAPEL, peso=700, alinha="center"),
           rot(80, y + 8, t, w=800, tam=24, cor=FOSF if j == 4 else TINTA, peso=700)]
p.append(caixa(960, 0, 704, 200, OXID, OXID_T, esp=3, rx=18))
rs += [rot(984, 20, "Verbo no imperativo", w=656, tam=26, cor=OXID, peso=700, serif=True),
       rot(984, 80, "retire · não volte no mesmo dia · encaminhe · registre", w=656, tam=24, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(960, 230, 704, 230, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(984, 250, "“Avaliar se necessário” não é instrução.", w=656, tam=24, cor=FOSF, peso=700, serif=True, lh=1.25),
       rot(984, 330, "“Qualquer sinal da lista: fora do jogo, sem volta no mesmo dia” é.", w=656, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "pagina", 460, p, rs, eyebrow="Passo 3 · escrever em uma página", titulo="Sete partes numa página, e nenhuma frase que dependa de interpretação")

# 7. passo 4: simular
p = [svg_abre(1664, 420, "Simulação de mesa com quem vai usar o protocolo: treinador, capitão, fisioterapeuta, um pai. Cenário lido em voz alta: terça, oito da noite, sem fisioterapeuta, um jogador fica tonto depois de um choque. Marcas vermelhas onde o grupo travou")]
rs = []
CX, CY = 360, 220
p.append(f'<ellipse cx="{CX}" cy="{CY}" rx="260" ry="130" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="4"/>')
p.append(f'<rect x="{CX - 70}" y="{CY - 80}" width="140" height="160" rx="8" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
for k in range(5):
    p.append(f'<rect x="{CX - 50}" y="{CY - 60 + k * 26}" width="100" height="10" rx="4" fill="{FOSF if k in (1, 3) else GRADE}"/>')
for k, t in enumerate(["treinador", "capitão", "fisioterapeuta", "um pai"]):
    a = math.radians(-150 + k * 100)
    x, y = CX + 360 * math.cos(a), CY + 190 * math.sin(a)
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22" fill="{TINTA}"/>')
    rs.append(rot(x - 100, y + 26, t, w=200, tam=22, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(800, 0, 864, 160, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(824, 24, "“Terça, oito da noite, sem fisioterapeuta, um jogador fica tonto depois de um choque.”", w=816, tam=26, cor=AZUL, peso=700, serif=True, lh=1.3))
p.append(caixa(800, 190, 864, 230, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(824, 210, "Onde o grupo trava, o protocolo está errado", w=816, tam=26, cor=FOSF, peso=700, serif=True),
       rot(824, 270, "ninguém sabe onde está o cartão de reconhecimento · ninguém sabe quem avisa a família", w=816, tam=24, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "simular", 420, p, rs, eyebrow="Passo 4 · simular antes de valer", titulo="Onde a simulação trava, o protocolo está errado")

# 8. passo 5: versão e revisão
p = [svg_abre(1664, 400, "Linha do tempo de um ano: aprovado, versão 1, assinado por quem responde; cada uso registrado; revisão anual com três perguntas, quantos casos, quantos seguiram o fluxo, onde travou. Seta de volta: versão 2"), defs(TINTA)]
rs = []
Y = 160
p.append(f'<line x1="60" y1="{Y}" x2="1500" y2="{Y}" stroke="{TINTA}" stroke-width="4"/>')
for x, t, c in [(60, "aprovado e assinado: versão 1", OXID), (780, "cada uso registrado", AZUL), (1500, "revisão anual", GLIC)]:
    p.append(f'<circle cx="{x}" cy="{Y}" r="26" fill="{c}"/>')
    rs.append(rot(max(0, x - 180), Y - 90, t, w=360, tam=24, cor=c, peso=700, alinha="center"))
for k in range(8):
    p.append(f'<rect x="{360 + k * 90}" y="{Y - 14}" width="12" height="28" rx="3" fill="{AZUL}"/>')
p.append(f'<path d="M 1500 200 Q 1500 360 780 360 Q 60 360 60 200" stroke="{GLIC}" stroke-width="4" fill="none" stroke-dasharray="12 8" marker-end="url(#m0)"/>')
rs.append(rot(580, 312, "versão 2", w=400, tam=26, cor=GLIC, peso=700, serif=True, alinha="center"))
for j, t in enumerate(["na revisão: quantos casos?", "quantos seguiram o fluxo?", "onde travou?"]):
    rs.append(rot(540, 200 + j * 36, t, w=480, tam=22, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "versao", 400, p, rs, eyebrow="Passo 5 · aprovar, registrar e revisar", titulo="O próprio uso do protocolo escreve a versão seguinte")

# 9. o protocolo de gaveta
p = [svg_abre(1664, 400, "Uma gaveta entreaberta com um protocolo de vinte páginas coberto de poeira. Três sinais do protocolo de gaveta: ninguém sabe onde está; longo demais para usar na hora; nunca foi revisado")]
rs = []
p.append(f'<rect x="40" y="120" width="460" height="240" rx="12" fill="{MUDO}"/>')
p.append(f'<rect x="80" y="60" width="380" height="120" rx="10" fill="{GRADE}" stroke="{TINTA}" stroke-width="3"/>')
for k in range(4):
    p.append(f'<rect x="{110 + k * 8}" y="{70 - k * 6}" width="300" height="100" rx="6" fill="{CARTAO}" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<rect x="230" y="220" width="80" height="16" rx="8" fill="{TINTA}"/>')
rs.append(rot(140, 100, "20 páginas", w=260, tam=24, cor=MUDO, peso=700, alinha="center"))
for j, t in enumerate(["ninguém sabe onde está na hora", "longo demais para ler na beira do campo", "nunca foi revisado: ninguém confia que vale"]):
    x = 580 + j * 362
    p.append(caixa(x, 40, 340, 220, FOSF, FOSF_T, esp=3, rx=16))
    p.append(icone("t:x", x + 20, 60, 40, FOSF))
    rs.append(rot(x + 20, 120, t, w=300, tam=24, cor=TINTA, peso=700, lh=1.3))
rs.append(rot(580, 300, "Os cinco passos foram desenhados contra esses três sinais.", w=1084, tam=26, cor=TINTA, peso=700, serif=True))
diagrama(S, "gaveta", 400, p, rs, eyebrow="O erro mais comum", titulo="O protocolo que ninguém usa é pior do que nenhum")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Como escrever um protocolo", "titulo": "Uma página que funciona sem você na beira do campo",
          "regras": ["Protocolo é para o problema que se repete, custa caro e varia",
                     "Diretriz que passa no filtro, traduzida para o lugar",
                     "Uma página, imperativo, simulada e revisada com o uso"],
          "cards": [{"ic": "t:writing", "t": "Quem coordena", "x": "Escolhe o problema, escreve com a equipe e assina a versão."},
                    {"ic": "t:users", "t": "Cada profissional", "x": "Diz, na simulação, onde o fluxo trava na prática dele."},
                    {"ic": "t:flag", "t": "Quem está no campo", "x": "Sabe onde a página está e o que ela manda fazer."}]})

salvar("14-05.json", {"arquivo": "aulas/MOD14/14-05-como-escrever-um-protocolo-de-departamento.md",
                      "titulo": "Como escrever um protocolo de departamento", "subtitulo": "Cinco passos, uma página",
                      "nota_capa": "Entra por um clube de rúgbi amador com três condutas diferentes para a mesma pancada.",
                      "secoes": {"campo": ["O problema.", "capa"], "problema": ["Escolher e adaptar.", "problema"],
                                 "pagina": ["Escrever e testar.", "pagina"], "gaveta": ["O erro mais comum.", "gaveta"]},
                      "slides": S})
