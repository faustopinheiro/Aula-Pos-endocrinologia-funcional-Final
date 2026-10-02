"""Spec do deck 11.10. Gera 11-10.json ao lado deste arquivo. Fecha o módulo."""
from _base import *

S = []

# 1. o número
p = [svg_abre(1664, 450, "Duas barras sobre uma linha de zero. Treino de alta intensidade supervisionado: mais 2,9 por cento na densidade da coluna lombar. Programa leve em casa: menos 1,2 por cento. Receita: duas sessões por semana, trinta minutos, cinco séries de cinco repetições acima de 85 por cento da carga máxima, mais impacto")]
y0 = 230
k = 50
p.append(f'<line x1="40" y1="{y0}" x2="900" y2="{y0}" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<rect x="140" y="{y0 - 2.9 * k:.0f}" width="260" height="{2.9 * k:.0f}" rx="8" fill="{OXID}"/>')
p.append(f'<rect x="540" y="{y0}" width="260" height="{1.2 * k:.0f}" rx="8" fill="{FOSF}"/>')
rs = [rot(140, y0 - 2.9 * k - 70, "+2,9%", w=260, tam=56, cor=OXID, peso=700, serif=True, alinha="center"),
      rot(540, y0 + 1.2 * k + 10, "−1,2%", w=260, tam=56, cor=FOSF, peso=700, serif=True, alinha="center"),
      rot(100, y0 + 30, "carga alta, supervisionada", w=340, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2),
      rot(500, y0 - 70, "programa leve em casa", w=340, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(40, 410, "densidade da coluna lombar em oito meses", w=860, tam=22, cor=MUDO, alinha="center")]
p.append(caixa(980, 0, 684, 450, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1004, 22, "A receita", w=636, tam=32, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["2 sessões por semana", "30 minutos cada", "5 séries de 5, acima de 85% da carga máxima", "agachamento, terra, desenvolvimento", "mais impacto"]):
    rs.append(rot(1004, 96 + j * 66, "· " + t, w=636, tam=26, cor=TINTA, peso=600))
diagrama(S, "numero", 450, p, rs, eyebrow="Uma jogadora de beach tennis, na casa dos cinquenta", titulo="O osso baixo respondeu à carga pesada, não à leve",
         fonte="Ensaio randomizado, J Bone Miner Res 2018")

# 2. em quem
p = [svg_abre(1664, 420, "O cartão do ensaio: 101 mulheres acima de 58 anos com massa óssea baixa; adesão de 92 por cento; nenhuma fratura vertebral nova ou piorada; um evento adverso. Ressalvas: supervisionado; progressão conduzida; fratura vertebral prévia muda a indicação")]
rs = []
for j, (n, t) in enumerate([("101", "mulheres, acima de 58 anos, osso baixo"), ("92%", "de adesão no grupo da carga alta"), ("0", "fratura vertebral nova ou piorada"), ("1", "evento adverso, leve")]):
    x, y = (j % 2) * 520, (j // 2) * 210
    p.append(caixa(x, y, 490, 190, AZUL, AZUL_T, esp=3, rx=16))
    rs += [rot(x + 20, y + 16, n, w=450, tam=64, cor=AZUL, peso=700, serif=True), rot(x + 20, y + 110, t, w=450, tam=24, cor=TINTA, peso=600, lh=1.2)]
p.append(caixa(1080, 0, 584, 400, GLIC, GLIC_T, esp=3, rx=16))
rs.append(rot(1104, 20, "Vai junto com o número", w=540, tam=28, cor=GLIC, peso=700, serif=True))
for j, t in enumerate(["supervisionado", "técnica ensinada, progressão conduzida", "fratura vertebral prévia muda a indicação"]):
    rs.append(rot(1104, 100 + j * 90, "· " + t, w=540, tam=26, cor=TINTA, peso=600, lh=1.25))
diagrama(S, "quem", 420, p, rs, eyebrow="Em quem foi medido", titulo="Seguro e bem aceito, desde que supervisionado")

# 3. os estágios
p = [svg_abre(1664, 470, "Linha dos estágios: ciclos regulares; transição inicial, ciclos variando sete dias ou mais; transição tardia, intervalos de sessenta dias ou mais; menopausa, uma data, depois de doze meses sem menstruar; pós-menopausa. Avisos: FSH oscila; antes dos 45 precoce, antes dos 40 insuficiência ovariana; enquanto há ciclo, há chance de gravidez")]
rs = []
faixas = [("ciclos regulares", OXID_T, OXID), ("transição inicial: variação de 7 dias ou mais", GLIC_T, GLIC), ("transição tardia: intervalos de 60 dias ou mais", GLIC_T, GLIC), ("pós-menopausa", AZUL_T, AZUL)]
xs = [0, 360, 760, 1220, 1664]
for j, (t, f, c) in enumerate(faixas):
    x0, x1 = xs[j], xs[j + 1]
    p.append(f'<rect x="{x0 + 4}" y="20" width="{x1 - x0 - 8}" height="140" rx="14" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(x0 + 16, 50, t, w=x1 - x0 - 32, tam=26, cor=c, peso=700, alinha="center", lh=1.25))
p.append(f'<line x1="1220" y1="0" x2="1220" y2="200" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<circle cx="1220" cy="200" r="14" fill="{FOSF}"/>')
rs.append(rot(980, 220, "menopausa: uma data, reconhecida após 12 meses sem menstruar", w=480, tam=24, cor=FOSF, peso=700, alinha="center", lh=1.2))
for j, t in enumerate(["FSH oscila na transição: o diagnóstico é pela história", "antes dos 45: precoce · antes dos 40: insuficiência ovariana", "enquanto há ciclo, há chance de gravidez"]):
    x = j * 560
    p.append(caixa(x, 320, 524, 150, MUDO, CARTAO, esp=2, rx=14))
    rs.append(rot(x + 20, 350, t, w=484, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.3))
diagrama(S, "estagios", 470, p, rs, eyebrow="Os nomes", titulo="Menopausa é uma data; a transição é o que vem antes",
         fonte="Estadiamento revisto, Fertil Steril 2012")

# 4. os pesos
p = [svg_abre(1664, 470, "Sete domínios com pesos. Grandes: fogachos e sono; osso. Médios: massa magra e força; síndrome geniturinária; humor e memória; gordura abdominal. Pequeno, com interrogação: tendão")]
rs = []
dom = [("fogachos e sono", 3, FOSF), ("osso", 3, FOSF), ("massa magra e força", 2, GLIC), ("síndrome geniturinária", 2, GLIC),
       ("humor e memória", 2, GLIC), ("gordura abdominal", 2, GLIC), ("tendão: dados limitados", 1, MUDO)]
for j, (t, w_, c) in enumerate(dom):
    col, row = j // 4, j % 4
    x, y = col * 840, row * 116
    rs.append(rot(x, y + 26, t, w=420, tam=28, cor=TINTA, peso=700, alinha="right"))
    for i in range(w_):
        p.append(f'<rect x="{x + 450 + i * 100}" y="{y + 16}" width="86" height="64" rx="10" fill="{c}"/>')
    if w_ == 1:
        rs.append(rot(x + 560, y + 26, "?", w=60, tam=36, cor=MUDO, peso=700))
diagrama(S, "pesos", 470, p, rs, eyebrow="O que muda, e com que peso", titulo="O sono e o osso pesam mais; o tendão ainda é pergunta")

# 5. a atribuição
p = [svg_abre(1664, 420, "Uma queixa, a força caiu e o ritmo piorou, decomposta numa barra empilhada: desuso, sono fragmentado, falta de estrogênio, idade. Esquema; as fatias variam de mulher para mulher. A pergunta: existe outra explicação mais tratável? Trate essa primeiro")]
rs = [rot(0, 0, "“a força caiu e o ritmo piorou”", w=1000, tam=32, cor=TINTA, peso=700, serif=True)]
partes = [("desuso", 0.40, OXID), ("sono fragmentado", 0.25, AZUL), ("falta de estrogênio", 0.22, FOSF), ("idade", 0.13, MUDO)]
x = 0
for t, f, c in partes:
    w_ = f * 1000
    p.append(f'<rect x="{x:.0f}" y="80" width="{w_ - 6:.0f}" height="120" rx="10" fill="{c}"/>')
    rs.append(rot(x + 8, 116, t, w=w_ - 22, tam=24, cor=PAPEL, peso=700, alinha="center", lh=1.15))
    x += w_
rs.append(rot(0, 220, "esquema: as fatias variam de mulher para mulher", w=1000, tam=22, cor=MUDO))
p.append(caixa(1080, 40, 584, 300, TINTA, TINTA, esp=0, rx=18))
rs.append(rot(1110, 80, "Existe outra explicação, provável e mais tratável? Trate essa primeiro.", w=524, tam=32, cor=PAPEL, peso=700, serif=True, lh=1.3))
rs.append(rot(0, 300, "várias costumam coexistir: todas entram no plano, a ordem é que muda", w=1000, tam=26, cor=TINTA, peso=600, lh=1.3))
diagrama(S, "atribuicao", 420, p, rs, eyebrow="A ferramenta clínica", titulo="Antes de dizer “é a menopausa”, divida a queixa")

# 6. os pilares
p = [svg_abre(1664, 440, "Quatro pilares sob uma barra: força pesada supervisionada, impacto progressivo, proteína distribuída, aeróbico. Ao lado, riscado: exercício para tratar fogacho, evidência insuficiente")]
p.append(f'<rect x="0" y="20" width="1100" height="50" rx="10" fill="{TINTA}"/>')
rs = []
for j, (t, ic) in enumerate([("força pesada, supervisionada", "t:bolt"), ("impacto progressivo", "t:run"), ("proteína distribuída", "t:salad"), ("aeróbico", "t:stopwatch")]):
    x = 30 + j * 270
    p.append(f'<rect x="{x}" y="70" width="230" height="280" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    p.append(icone(ic, x + 75, 110, 80, OXID))
    rs.append(rot(x + 10, 220, t, w=210, tam=26, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append(f'<rect x="0" y="350" width="1100" height="30" rx="6" fill="{CINZA}"/>')
p.append(caixa(1160, 60, 504, 220, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1180, 100, "exercício para tratar fogacho", w=464, tam=30, cor=FOSF, peso=700, alinha="center", lh=1.2))
p.append(f'<line x1="1190" y1="250" x2="1634" y2="90" stroke="{FOSF}" stroke-width="6"/>')
rs.append(rot(1160, 300, "evidência insuficiente (revisão de 2014)", w=504, tam=24, cor=TINTA, peso=600, alinha="center"))
diagrama(S, "pilares", 440, p, rs, eyebrow="O que o treino faz", titulo="Pelo osso, pela força, pelo sono e pelo coração; não pelo fogacho")

# 7. a janela da terapia hormonal
p = [svg_abre(1664, 420, "Régua de idade com a janela antes dos 60 anos ou até 10 anos da menopausa: benefício maior que risco para fogachos incômodos e prevenção de perda óssea. Cartão: estrogênio vaginal em dose baixa para síndrome geniturinária. Selo: decisão médica, compartilhada")]
A = lambda a: 40 + (a - 40) / 35 * 1040
p.append(f'<line x1="{A(40):.0f}" y1="200" x2="{A(75):.0f}" y2="200" stroke="{TINTA}" stroke-width="4"/>')
rs = []
for a in (40, 50, 60, 70):
    p.append(f'<line x1="{A(a):.0f}" y1="190" x2="{A(a):.0f}" y2="210" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(A(a) - 40, 220, f"{a}", w=80, tam=24, cor=MUDO, alinha="center"))
p.append(f'<rect x="{A(48):.0f}" y="60" width="{A(60) - A(48):.0f}" height="120" rx="14" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
rs.append(rot(A(48) + 10, 78, "benefício maior que risco", w=A(60) - A(48) - 20, tam=24, cor=OXID, peso=700, alinha="center", lh=1.2))
p.append(f'<rect x="{A(60):.0f}" y="60" width="{A(75) - A(60):.0f}" height="120" rx="14" fill="{PAPEL}" stroke="{MUDO}" stroke-width="2"{TRACO}/>')
rs.append(rot(A(60) + 10, 92, "menos favorável", w=A(75) - A(60) - 20, tam=24, cor=MUDO, peso=700, alinha="center"))
rs.append(rot(40, 270, "antes dos 60 anos ou até 10 anos da menopausa · fogachos incômodos e prevenção de perda óssea", w=1040, tam=24, cor=TINTA, peso=600, lh=1.3))
p.append(caixa(1140, 0, 524, 200, AZUL, AZUL_T, esp=3, rx=16))
rs.append(rot(1160, 40, "estrogênio vaginal em dose baixa: síndrome geniturinária", w=484, tam=26, cor=AZUL, peso=700, alinha="center", lh=1.3))
p.append(caixa(1140, 240, 524, 120, TINTA, TINTA, esp=0, rx=60))
rs.append(rot(1160, 280, "decisão médica, compartilhada", w=484, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "janela", 420, p, rs, eyebrow="Posicionamento de 2022", titulo="Terapia hormonal: eficaz, com janela definida",
         fonte="Sociedade norte-americana de menopausa, Menopause 2022")

# 8. o mercado
p = [svg_abre(1664, 440, "Uma mesa com potes, uma ampola e um implante, com etiquetas riscadas: hormônio para desempenho; testosterona para força ou composição corporal; implante manipulado em dose acima da fisiológica; bioidêntico como argumento. Aviso: atleta federada, verificar regras antidoping")]
rs = []
for j, t in enumerate(["hormônio para desempenho", "testosterona para força ou composição corporal", "implante manipulado acima da dose fisiológica", "“bioidêntico” como argumento"]):
    x, y = (j % 2) * 840, (j // 2) * 160
    p.append(caixa(x, y, 820, 130, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(x + 30, y + 44, t, w=760, tam=30, cor=FOSF, peso=700, alinha="center"))
    p.append(f'<line x1="{x + 40}" y1="{y + 110}" x2="{x + 780}" y2="{y + 20}" stroke="{FOSF}" stroke-width="5"/>')
p.append(caixa(0, 340, 1664, 100, GLIC, GLIC_T, esp=3, rx=16))
p.append(icone("t:alert-triangle", 30, 364, 52, GLIC))
rs.append(rot(100, 370, "Atleta federada: terapia hormonal e testosterona têm implicações antidoping", w=1540, tam=28, cor=TINTA, peso=700))
diagrama(S, "mercado", 440, p, rs, eyebrow="O que não é indicação", titulo="O que a mesa vende não trata o que ela tem")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "Do déficit de evidência à mulher que treina depois dos cinquenta",
          "regras": ["Decisão: a medicina e a ginecologia investigam e decidem sobre hormônio; a nutrição corrige a energia; preparação e fisioterapia conduzem carga, prevenção e retorno",
                     "Contribuição: o ciclo registrado, o rendimento que parou, o prato contado, a lesão que se repete, o encaminhamento em seis linhas",
                     "Reconhecimento: o ciclo que espaçou, a fratura que volta, o platô com treino mantido, a perda urinária, a gestante parada, a carga leve para osso fraco"],
          "cards": [{"ic": "h:doctor-female", "t": "Medicina e ginecologia", "x": "Funil de exclusão, densitometria, contracepção, terapia hormonal, liberação."},
                    {"ic": "t:salad", "t": "Nutrição, preparação e fisioterapia", "x": "Energia, programa de prevenção, gestação, assoalho pélvico, carga."},
                    {"ic": "t:users", "t": "Todos", "x": "Próximo módulo: o atleta adolescente e o atleta idoso, a começar pelo crescimento."}]})

salvar("11-10.json", {"arquivo": "aulas/MOD11/11-10-transicao-da-menopausa.md",
                      "titulo": "Transição da menopausa", "subtitulo": "Mais carga, melhor atribuição, menos mercado",
                      "nota_capa": "Entra por uma jogadora de beach tennis com osteopenia. Fecha o módulo.",
                      "secoes": {"numero": ["O número.", "capa"], "estagios": ["O que muda.", "estagios"],
                                 "pilares": ["O treino e o hormônio.", "pilares"], "mercado": ["O mercado e o fecho do módulo.", "mercado"]},
                      "slides": S})
