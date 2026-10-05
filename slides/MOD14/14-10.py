"""Spec do deck 14.10. Gera 14-10.json ao lado deste arquivo."""
from _base import *

S = []

# 1. dez minutos, quatro olhares
p = [svg_abre(1664, 440, "Um cronômetro marcando 10:00. Uma mesa com quatro pessoas de profissões diferentes: medicina, fisioterapia, educação física e nutrição. Do outro lado, a fisioterapeuta da escolinha, com uma folha na mão. Dez minutos, quatro olhares")]
rs = []
p.append(f'<circle cx="200" cy="210" r="160" fill="{CARTAO}" stroke="{FOSF}" stroke-width="8"/>')
p.append(f'<rect x="180" y="26" width="40" height="30" rx="6" fill="{FOSF}"/>')
rs.append(rot(60, 170, "10:00", w=280, tam=64, cor=FOSF, peso=700, serif=True, alinha="center"))
for j, (t, c) in enumerate([("medicina", AZUL), ("fisioterapia", OXID), ("educação física", GLIC), ("nutrição", FOSF)]):
    x = 560 + j * 190
    p.append(menino(x, 270, 190, c))
    rs.append(rot(x - 90, 320, t, w=180, tam=22, cor=c, peso=700, alinha="center"))
p.append(f'<rect x="460" y="262" width="760" height="34" rx="8" fill="{TINTA}"/>')
p.append(menino(1460, 400, 260, TINTA))
p.append(f'<rect x="1490" y="250" width="60" height="78" rx="4" fill="{PAPEL}" stroke="{TINTA}" stroke-width="3"/>')
rs += [rot(1330, 20, "a fisioterapeuta da escolinha", w=334, tam=24, cor=TINTA, peso=700, alinha="center"),
       rot(460, 390, "dez minutos, quatro olhares", w=760, tam=28, cor=TINTA, peso=700, serif=True, alinha="center")]
diagrama(S, "relogio", 440, p, rs, eyebrow="O projeto aplicado diante da banca", titulo="Dez minutos para uma banca de quatro profissões")

# 2. o roteiro
p = [svg_abre(1664, 420, "Barra de tempo de dez minutos em sete blocos: o problema numa frase, 1 min; a linha de base e a definição, 1,5 min; a mudança e os ciclos, 2 min; o gráfico e as regras, 2 min; os três indicadores e os limites, 1,5 min; o que fica no lugar, 1 min; folga, 1 min. Sugestão de tempo; siga a regra da sua banca")]
rs = []
x = 0
U = 166.4
for t, m, c in [("o problema, numa frase", 1, AZUL), ("a linha de base e a definição", 1.5, OXID), ("a mudança e os ciclos", 2, GLIC),
                ("o gráfico e as regras", 2, FOSF), ("os três indicadores e os limites", 1.5, AZUL), ("o que fica no lugar", 1, OXID), ("folga", 1, MUDO)]:
    w = m * U
    p.append(f'<rect x="{x + 3:.0f}" y="40" width="{w - 6:.0f}" height="110" rx="12" fill="{c}" opacity="{0.45 if c == MUDO else 1}"/>')
    rs += [rot(x + 6, 76, f"{m:g} min".replace(".", ","), w=w - 12, tam=28, cor=PAPEL, peso=700, serif=True, alinha="center"),
           rot(x + 6, 176, t, w=w - 12, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.25)]
    x += w
rs += [rot(0, 300, "a ordem segue as três perguntas do modelo de melhoria: meta, medida, mudança", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(0, 370, "sugestão de tempo · siga a regra da sua banca", w=1664, tam=20, cor=MUDO, alinha="center")]
diagrama(S, "roteiro", 420, p, rs, eyebrow="Passo 1", titulo="O roteiro dá a cada bloco um tempo e uma ordem")

# 3. a banca
p = [svg_abre(1664, 420, "Os quatro membros da banca, cada um com uma pergunta. Medicina: é seguro, e para quem não é? Fisioterapia: a dose e a execução estão certas? Educação física: isso cabe no treino? Nutrição: o que mais muda na rotina dessas atletas? Cada profissão escuta uma coisa")]
rs = []
for j, (t, q, ic, c) in enumerate([("medicina", "é seguro, e para quem não é?", "h:doctor", AZUL),
                                   ("fisioterapia", "a dose e a execução estão certas?", "t:first-aid-kit", OXID),
                                   ("educação física", "isso cabe no treino, ou rouba tempo da bola?", "t:stopwatch", GLIC),
                                   ("nutrição", "o que mais muda na rotina dessas atletas?", "t:apple", FOSF)]):
    x = j * 424
    p.append(caixa(x, 0, 392, 200, c, CARTAO, esp=3, rx=18))
    p.append(f'<path d="M {x + 60} 200 L {x + 90} 236 L {x + 120} 200" fill="{CARTAO}" stroke="{c}" stroke-width="3"/>')
    p.append(f'<rect x="{x + 62}" y="194" width="56" height="8" fill="{CARTAO}"/>')
    rs.append(rot(x + 22, 40, q, w=348, tam=26, cor=TINTA, peso=700, serif=True, lh=1.3))
    p.append(icone(ic, x + 60, 260, 60, c))
    rs.append(rot(x + 136, 274, t, w=250, tam=26, cor=c, peso=700))
p.append(caixa(0, 350, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 368, "uma frase de resposta para cada pergunta, escrita antes da defesa", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "banca", 420, p, rs, eyebrow="Passo 2", titulo="Cada profissão da banca escuta o projeto com uma pergunta")

# 4. o ciclo que falhou
BASE = [25, 25, 0, 50, 25, 25]
DEPOIS = [25, 50, 50, 75, 50, 75, 75, 100, 75, 75, 100, 75]
pts = BASE + DEPOIS
x0, x1, y0, y1 = 80, 1060, 30, 360
dx = (x1 - x0 - 40) / 17
xs = [x0 + 20 + i * dx for i in range(18)]
Y = lambda v: y1 - v / 100 * (y1 - y0)
p = [svg_abre(1664, 420, "O gráfico de sequência da escolinha, com as semanas do primeiro ciclo marcadas: a capitã conduzia, mas não se espalhou. Ao lado, um cartão: o que não funcionou e o que aprendemos. O ciclo que falhou entra na defesa. Valores ilustrativos")]
p.append(f'<rect x="{(xs[5] + xs[6]) / 2:.0f}" y="{y0}" width="{dx * 2:.0f}" height="{y1 - y0}" fill="{GLIC_T}"/>')
p += [f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{GRADE}" stroke-width="3"/>',
      f'<line x1="{x0}" y1="{Y(25):.0f}" x2="{x1}" y2="{Y(25):.0f}" stroke="{AZUL}" stroke-width="3" stroke-dasharray="12 8"/>']
p.append('<path d="' + " ".join(f'{"M" if i == 0 else "L"} {xs[i]:.0f} {Y(v):.0f}' for i, v in enumerate(pts)) + f'" stroke="{TINTA}" stroke-width="3" fill="none"/>')
for i, v in enumerate(pts):
    p.append(f'<circle cx="{xs[i]:.0f}" cy="{Y(v):.0f}" r="9" fill="{MUDO if i < 6 else OXID}" stroke="{PAPEL}" stroke-width="3"/>')
rs = [rot(xs[6] - 40, 372, "ciclo 1", w=200, tam=22, cor=GLIC, peso=700),
      rot(x0, 380, "valores ilustrativos", w=300, tam=20, cor=MUDO)]
p.append(caixa(1120, 0, 544, 420, GLIC, GLIC_T, esp=3, rx=18))
rs += [rot(1150, 30, "o que não funcionou", w=484, tam=30, cor=GLIC, peso=700, serif=True),
       rot(1150, 90, "a capitã conduzia na sessão dela, e a prática não se espalhou", w=484, tam=24, cor=TINTA, peso=700, lh=1.3),
       rot(1150, 210, "o que aprendemos", w=484, tam=30, cor=OXID, peso=700, serif=True),
       rot(1150, 270, "o aquecimento precisava estar dentro do treino, com bola, em todas as sessões", w=484, tam=24, cor=TINTA, peso=700, lh=1.3)]
diagrama(S, "falhou", 420, p, rs, eyebrow="Passo 3", titulo="O ciclo que falhou explica o que deu certo, e entra na defesa")

# 5. os limites em três frases
p = [svg_abre(1664, 400, "Três frases numa ficha. O que mostramos: o aquecimento completo passou a ser feito, com deslocamento acima da mediana. O que não podemos dizer: se houve menos lesões; o grupo e o tempo não permitem. O que faríamos a seguir: manter a contagem por um ano e comparar com outra categoria")]
rs = []
for j, (k, v, c) in enumerate([("o que mostramos", "o aquecimento completo passou a ser feito, com deslocamento acima da mediana", OXID),
                               ("o que não podemos dizer", "se houve menos lesões: o grupo e o tempo não permitem", FOSF),
                               ("o que faríamos a seguir", "manter a contagem por um ano e comparar com outra categoria do clube", AZUL)]):
    y = j * 116
    p.append(caixa(0, y, 1664, 100, c, CARTAO, esp=3, rx=14))
    p.append(f'<rect x="0" y="{y}" width="380" height="100" rx="14" fill="{c}"/>')
    rs += [rot(20, y + 32, k, w=340, tam=26, cor=PAPEL, peso=700),
           rot(410, y + 32, v, w=1230, tam=26, cor=TINTA, peso=700)]
rs.append(rot(0, 366, "quem diz o limite primeiro controla a conversa · valores do exemplo, ilustrativos", w=1664, tam=22, cor=MUDO, peso=700, alinha="center"))
diagrama(S, "limites", 400, p, rs, eyebrow="Passo 4", titulo="Os limites cabem em três frases, ditas antes da banca perguntar")

# 6. o que fica no lugar
p = [svg_abre(1664, 420, "A escolinha um ano depois. Uma cadeira vazia: a aluna já saiu. Três coisas ficaram: o dono da medida, a auxiliar técnica; a ficha, na pasta da categoria; a mudança, escrita no protocolo do clube, com responsável e data de revisão. O projeto fica quando tem dono, ficha e papel")]
rs = []
p.append(f'<path d="M 130 110 L 130 330 M 130 230 L 300 230 L 300 330" stroke="{MUDO}" stroke-width="10" fill="none" stroke-linecap="round"/>')
p.append(f'<rect x="110" y="214" width="200" height="22" rx="6" fill="{MUDO}"/>')
rs.append(rot(40, 360, "a aluna já saiu", w=340, tam=26, cor=MUDO, peso=700, serif=True, alinha="center"))
for j, (t, x_, ic, c) in enumerate([("dono", "a auxiliar técnica, que já contava", "t:user", OXID),
                                    ("ficha", "na pasta da categoria, e não no computador da aluna", "t:clipboard-list", AZUL),
                                    ("papel", "no protocolo do clube, com responsável e data de revisão", "t:writing", GLIC)]):
    x = 440 + j * 412
    p.append(caixa(x, 0, 388, 320, c, CARTAO, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 56, c))
    rs += [rot(x + 96, 36, t, w=270, tam=32, cor=c, peso=700, serif=True),
           rot(x + 24, 120, x_, w=340, tam=26, cor=TINTA, peso=700, lh=1.3)]
rs.append(rot(440, 360, "o projeto fica quando tem dono, ficha e papel", w=1224, tam=26, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "fica", 420, p, rs, eyebrow="Passo 5", titulo="A banca quer saber o que acontece depois que você sai")

# 7. o ensaio
p = [svg_abre(1664, 420, "A fisioterapeuta falando em pé, um cronômetro na mesa e duas pessoas assistindo: uma técnica do clube e um colega de outra profissão. Três cartões com perguntas difíceis na parede. Ensaiar em voz alta, cronometrado, para quem não é da sua área")]
rs = []
p.append(menino(160, 400, 280, OXID))
p.append(f'<rect x="300" y="300" width="300" height="20" rx="6" fill="{TINTA}"/>')
p.append(icone("t:stopwatch", 410, 236, 60, FOSF))
p.append(menino(720, 400, 190, MUDO))
p.append(menino(880, 400, 190, AZUL))
rs += [rot(640, 150, "técnica", w=160, tam=22, cor=MUDO, peso=700, alinha="center"),
       rot(800, 150, "outra profissão", w=160, tam=22, cor=AZUL, peso=700, alinha="center", lh=1.2)]
for j in range(3):
    x = 1040 + j * 210
    p.append(f'<rect x="{x}" y="20" width="180" height="120" rx="10" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3" transform="rotate({(-3, 2, -2)[j]} {x + 90} 80)"/>')
    rs.append(rot(x, 50, "?", w=180, tam=44, cor=FOSF, peso=700, serif=True, alinha="center"))
rs += [rot(1040, 170, "três perguntas difíceis, três respostas curtas", w=600, tam=24, cor=TINTA, peso=700),
       rot(1040, 250, "em voz alta, com cronômetro, pelo menos duas vezes", w=600, tam=24, cor=TINTA, peso=700),
       rot(1040, 330, "slide que precisa ser lido: carregado demais", w=600, tam=22, cor=FOSF, peso=700)]
diagrama(S, "ensaio", 420, p, rs, eyebrow="Passo 6", titulo="O ensaio é o lugar barato para descobrir o que não se entende")

# 8. o kit
p = [svg_abre(1664, 440, "Uma caixa de ferramentas aberta com oito instrumentos: ficha de anamnese; painel de carga; critérios de passagem e de retorno; plano de emergência do local; auditoria de suplemento; fluxo de encaminhamento; registro de decisão; acordo de informação. Na tampa: o projeto aplicado, a frase do problema e o gráfico de sequência")]
rs = []
p.append(caixa(0, 0, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 18, "na tampa: o projeto aplicado, a frase do problema e o gráfico de sequência", w=1624, tam=26, cor=PAPEL, peso=700, serif=True, alinha="center"))
KIT = [("ficha de anamnese", "avaliação pré-participação", "t:clipboard-list", AZUL),
       ("painel de carga", "carga interna e externa", "t:adjustments-horizontal", OXID),
       ("critérios de passagem e de retorno", "reabilitação", "t:route", GLIC),
       ("plano de emergência do local", "cadeia de sobrevivência", "t:first-aid-kit", FOSF),
       ("auditoria de suplemento", "evidência e lote", "t:pill", AZUL),
       ("fluxo de encaminhamento", "saúde mental", "t:arrows-exchange", OXID),
       ("registro de decisão", "seis linhas", "t:writing", GLIC),
       ("acordo de informação", "ética e sigilo", "t:lock", FOSF)]
for k, (t, o, ic, c) in enumerate(KIT):
    x = (k % 4) * 424
    y = 96 + (k // 4) * 176
    p.append(caixa(x, y, 392, 156, c, CARTAO, esp=3, rx=14))
    p.append(icone(ic, x + 20, y + 20, 48, c))
    rs.append(rot(x + 84, y + 22, t, w=290, tam=24, cor=TINTA, peso=700, lh=1.2))
    rs.append(rot(x + 84, y + 108, o, w=290, tam=20, cor=c, peso=700))
diagrama(S, "kit", 440, p, rs, eyebrow="O que o curso deixa", titulo="O curso deixa oito instrumentos e um método para melhorá-los")

# 9. o caminho do curso
MODS = ["fundamentos", "fisiologia", "hormônios", "nutrição", "suplementos", "clínica", "lesões",
        "reabilitação", "treino e carga", "saúde mental", "a atleta mulher", "adolescente e idoso", "o amador", "integração"]
p = [svg_abre(1664, 440, "Um caminho com catorze marcos, um por módulo: fundamentos e trabalho multiprofissional; fisiologia; hormônios; nutrição; suplementos; clínica; lesões; reabilitação; treino e carga; saúde mental; a atleta mulher; adolescente e idoso; o amador; integração. O caminho termina numa porta: segunda-feira, no seu lugar")]
rs = []
XS = [300 + i * 210 for i in range(7)]
pos = [(XS[i], 120) for i in range(7)] + [(XS[6 - i], 300) for i in range(7)]
p.append(f'<path d="M {XS[0]} 120 L {XS[6]} 120 A 90 90 0 0 1 {XS[6]} 300 L 170 300" stroke="{GRADE}" stroke-width="14" fill="none" stroke-linecap="round"/>')
for i, (x, y) in enumerate(pos):
    c = OXID if i == 13 else (AZUL if i < 10 else GLIC)
    p.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{c}" stroke="{PAPEL}" stroke-width="4"/>')
    ty = 40 if y == 120 else 330
    rs.append(rot(x - 100, ty, f"{i + 1} · {MODS[i]}", w=200, tam=22, cor=TINTA if i < 13 else OXID, peso=700, alinha="center", lh=1.2))
p.append(f'<rect x="40" y="220" width="110" height="170" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>')
p.append(f'<circle cx="130" cy="310" r="8" fill="{OXID}"/>')
rs.append(rot(0, 140, "segunda-feira, no seu lugar", w=200, tam=22, cor=OXID, peso=700, serif=True, alinha="center", lh=1.2))
diagrama(S, "curso", 440, p, rs, eyebrow="O caminho do curso", titulo="Ninguém cuida de um atleta sozinho, do primeiro módulo ao último")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo e do curso · três níveis", "titulo": "Da parte que cada um sabe ao cuidado que a equipe sustenta",
          "regras": ["Decisão: um dono por passagem, protocolo fora da gaveta, registro com o que se sabia, sigilo em duas camadas, problema antes da solução",
                     "Contribuição: o atleta que assina o acordo, quem conta no treino, a família, a capitã, a diretoria que guarda o protocolo",
                     "Reconhecimento: a passagem sem dono, o corte de peso, a menstruação que parou, o “liberada, sem queixas”, dois números como prova"],
          "cards": [{"ic": "h:doctor", "t": "Quem decide", "x": "Explica, registra e repete a decisão, com a equipe."},
                    {"ic": "t:users", "t": "Quem contribui", "x": "Atleta, técnico, auxiliar, família e diretoria."},
                    {"ic": "t:flag", "t": "Próximo passo", "x": "A banca, e depois a segunda-feira no seu lugar."}]})

salvar("14-10.json", {"arquivo": "aulas/MOD14/14-10-projeto-aplicado-estrutura-da-defesa.md",
                      "titulo": "Projeto aplicado: estrutura da defesa", "subtitulo": "Seis passos para a banca, e o que o curso deixa",
                      "nota_capa": "Entra por um cronômetro de dez minutos. Fecha o módulo e o curso.",
                      "secoes": {"relogio": ["A defesa em seis passos.", "capa"], "limites": ["Limites e continuidade.", "limites"],
                                 "kit": ["O que o curso deixa.", "kit"], "fecho": ["O fecho do módulo e do curso.", "fecho"]},
                      "slides": S})
