"""Spec do deck 11.8. Gera 11-08.json ao lado deste arquivo."""
from _base import *

S = []

# 1. o alerta e o teste
p = [svg_abre(1664, 470, "A tela de um celular com uma notificação: fase de risco para o joelho, evite saltos e mudanças de direção. Ao lado, a súmula de basquete com os minutos de uma atleta riscados e reduzidos. Embaixo, uma fila de atletas diante de uma plataforma de salto: só quem falhar no teste faz prevenção")]
p.append(f'<rect x="0" y="0" width="420" height="470" rx="40" fill="{TINTA}"/>')
p.append(f'<rect x="20" y="40" width="380" height="390" rx="20" fill="{PAPEL}"/>')
p.append(f'<rect x="40" y="80" width="340" height="190" rx="16" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
p.append(icone("t:alert-triangle", 60, 100, 48, FOSF))
rs = [rot(120, 106, "fase de risco para o joelho", w=250, tam=24, cor=FOSF, peso=700, lh=1.2),
      rot(60, 180, "evite saltos e mudanças de direção", w=300, tam=22, cor=TINTA, lh=1.25)]
p.append(caixa(480, 0, 540, 470, TINTA, CARTAO, esp=2, rx=16))
rs.append(rot(504, 20, "Súmula · sábado", w=500, tam=28, cor=TINTA, peso=700, serif=True))
for j, (n, mins, risc) in enumerate([("armadora", "32 → 14", True), ("ala", "28", False), ("pivô", "30", False)]):
    y = 100 + j * 90
    rs += [rot(504, y, n, w=220, tam=26, cor=TINTA, peso=600), rot(760, y, mins + " min", w=240, tam=26, cor=FOSF if risc else TINTA, peso=700, alinha="right")]
p.append(f'<line x1="500" y1="380" x2="1000" y2="380" stroke="{BORDA}" stroke-width="2"/>')
rs.append(rot(504, 400, "minutos cortados pelo aviso", w=500, tam=22, cor=FOSF, peso=700))
p.append(caixa(1080, 0, 584, 470, AZUL, AZUL_T, esp=3, rx=16))
p.append(f'<rect x="1140" y="300" width="200" height="40" rx="6" fill="{AZUL}"/>')
for i in range(4):
    p.append(icone("t:user", 1390 + (i % 2) * 120, 150 + (i // 2) * 110, 70, AZUL if i else FOSF))
p.append(icone("t:user", 1200, 200, 90, AZUL))
rs += [rot(1104, 20, "Teste de salto na pré-temporada", w=540, tam=26, cor=AZUL, peso=700, lh=1.2),
       rot(1104, 380, "só quem falhar faz prevenção", w=540, tam=26, cor=TINTA, peso=700, alinha="center")]
diagrama(S, "alerta", 470, p, rs, eyebrow="Uma equipe de basquete feminino", titulo="Duas decisões que parecem cuidado, e erram")

# 2. o risco por esporte
p = [svg_abre(1664, 420, "Três barras horizontais com a razão de incidência entre mulheres e homens. Esportes de contato: 3,0 vezes. Esportes com aterrissagem de alto impacto e rotação: 5,5 vezes. Esportes de colisão: 1,1 vez, sem diferença significativa")]
X = lambda v: 520 + v / 6 * 1080
rs = []
p.append(f'<line x1="{X(1):.0f}" y1="0" x2="{X(1):.0f}" y2="350" stroke="{TINTA}" stroke-width="3"{TRACO}/>')
rs.append(rot(X(1) - 120, 360, "1× = igual", w=240, tam=22, cor=MUDO, alinha="center"))
for j, (t, v, c, nota) in enumerate([("Contato", 3.0, FOSF, "3,0×"), ("Aterrissagem com rotação", 5.51, FOSF, "5,5×"), ("Colisão", 1.14, CINZA, "1,1× · sem diferença")]):
    y = 20 + j * 110
    rs.append(rot(0, y + 14, t, w=490, tam=28, cor=TINTA, peso=700, alinha="right"))
    p.append(f'<rect x="{X(0):.0f}" y="{y}" width="{X(v) - X(0):.0f}" height="70" rx="10" fill="{c}"/>')
    rs.append(rot(X(v) + 16, y + 16, nota, w=420, tam=32, cor=FOSF if c != CINZA else MUDO, peso=700, serif=True))
diagrama(S, "esportes", 420, p, rs, eyebrow="Metanálise de 2019, por categoria de esporte", titulo="A mulher rompe mais, e quanto mais depende do esporte",
         fonte="Razão de incidência mulher para homem; J Athl Train 2019")

# 3. três colunas
p = [svg_abre(1664, 470, "Três colunas. Não se mexe: lesão prévia, sexo, anatomia óssea, história familiar. Se mexe: força, controle na desaceleração, aterrissagem, fadiga e carga, exposição a jogo. Não sustenta o peso: ângulo Q isolado, core fraco como causa universal, fase do ciclo como critério de decisão")]
rs = []
cols = [("Não se mexe", ["lesão prévia, o maior", "sexo", "anatomia óssea", "história familiar"], MUDO, PAPEL),
        ("Se mexe", ["força de coxa e quadril", "controle na desaceleração", "aterrissagem", "fadiga e carga", "exposição a jogo"], OXID, OXID_T),
        ("Não sustenta o peso", ["ângulo Q isolado", "core fraco para tudo", "fase do ciclo para decidir"], FOSF, FOSF_T)]
for k, (t, itens, c, f) in enumerate(cols):
    x = k * 564
    p.append(caixa(x, 0, 536, 470, c, f, esp=4 if k == 1 else 2, rx=18))
    rs.append(rot(x + 24, 20, t, w=488, tam=32, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 36, 100 + j * 70, "· " + it, w=480, tam=27, cor=TINTA, peso=600))
diagrama(S, "colunas", 470, p, rs, eyebrow="Organizar antes de opinar", titulo="Quase nada do que se mexe é o sexo")

# 4. a cadeia do ciclo
p = [svg_abre(1664, 420, "Uma cadeia de quatro elos. Receptores de estrogênio no ligamento, colágeno influenciado pelo estradiol e frouxidão maior perto da ovulação, sólidos. Um elo pontilhado e quebrado: mais ruptura numa fase. Força da evidência: baixa"), defs(TINTA)]
rs = []
elos = [("receptores de estrogênio no ligamento", True), ("colágeno influenciado pelo estradiol", True), ("frouxidão maior perto da ovulação", True), ("mais ruptura numa fase?", False)]
for j, (t, solido) in enumerate(elos):
    x = j * 424
    c = OXID if solido else FOSF
    p.append(f'<rect x="{x}" y="40" width="360" height="220" rx="110" fill="{OXID_T if solido else CARTAO}" stroke="{c}" stroke-width="6"{"" if solido else TRACO}/>')
    rs.append(rot(x + 40, 110, t, w=280, tam=28, cor=c, peso=700, alinha="center", lh=1.2))
    if j < 3:
        p.append(seta(x + 366, 150, x + 418, 150, TINTA, "m0", 5) if j < 2 else f'<path d="M {x + 366} 150 l 18 -14 l 6 28 l 20 -14" stroke="{FOSF}" stroke-width="5" fill="none"/>')
p.append(caixa(0, 310, 1664, 110, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(24, 334, "Força da evidência sobre a ruptura: baixa · fase por contagem de dias · lesão rara", w=1616, tam=28, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "ciclo", 420, p, rs, eyebrow="O ciclo e o ligamento", titulo="Plausível no ligamento, insuficiente na ruptura",
         fonte="Revisão sistemática, Orthop J Sports Med 2017")

# 5. o custo de agir antes do dado
p = [svg_abre(1664, 440, "Três cartões riscados, cada um com o custo ao lado. Tirar de jogo pela fase: perda de oportunidade, rótulo de fragilidade. Prevenção concentrada em dias de risco: o efeito vem do acúmulo. Pílula para proteger o joelho: decisão de outra natureza, evidência baixa")]
rs = []
for j, (t, custo) in enumerate([("tirar de jogo pela fase", "minutos, oportunidade, rótulo de fragilidade"), ("prevenção só nos dias de risco", "o efeito vem do acúmulo, não da janela"), ("pílula para proteger o joelho", "outra decisão; evidência baixa demais")]):
    y = j * 150
    p.append(caixa(0, y, 640, 120, FOSF, FOSF_T, esp=3, rx=14))
    rs.append(rot(20, y + 38, t, w=600, tam=30, cor=FOSF, peso=700, alinha="center"))
    p.append(f'<line x1="30" y1="{y + 100}" x2="610" y2="{y + 20}" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<line x1="660" y1="{y + 60}" x2="720" y2="{y + 60}" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(740, y + 40, custo, w=920, tam=30, cor=TINTA, peso=600))
diagrama(S, "custo", 440, p, rs, eyebrow="Por que agir antes do dado não é neutro", titulo="Levar a fisiologia a sério não é agir antes do dado")

# 6. o teste de salto
p = [svg_abre(1664, 460, "Uma plataforma de salto com uma atleta aterrissando. Os números do estudo: 710 jogadoras de elite, 42 rupturas sem contato. Uma balança desequilibrada entre acertos e erros: teste de rastreio ruim. Nota: na análise corrigida, nenhum fator do salto se associou à lesão"), defs(TINTA)]
p.append(f'<rect x="60" y="300" width="300" height="50" rx="6" fill="{AZUL}"/>')
p.append(icone("t:user", 130, 80, 160, AZUL))
p.append(seta(380, 120, 380, 280, TINTA, "m0", 4))
rs = []
for j, (n, t) in enumerate([("710", "jogadoras de elite"), ("42", "rupturas sem contato")]):
    y = j * 130
    rs += [rot(460, y + 10, n, w=260, tam=80, cor=AZUL, peso=700, serif=True), rot(740, y + 40, t, w=360, tam=28, cor=TINTA, peso=600)]
p.append(f'<line x1="1180" y1="140" x2="1600" y2="200" stroke="{TINTA}" stroke-width="6"/>')
p.append(f'<path d="M 1390 170 l -30 120 l 60 0 z" fill="{TINTA}"/>')
p.append(f'<circle cx="1220" cy="112" r="34" fill="{OXID}"/><circle cx="1560" cy="228" r="34" fill="{FOSF}"/>')
rs += [rot(1160, 40, "acertos", w=120, tam=22, cor=OXID, peso=700, alinha="center"), rot(1500, 268, "erros", w=120, tam=22, cor=FOSF, peso=700, alinha="center"),
       rot(1100, 310, "teste de rastreio ruim", w=520, tam=32, cor=TINTA, peso=700, alinha="center", serif=True)]
p.append(caixa(0, 380, 1664, 80, GLIC, GLIC_T, esp=2, rx=14))
rs.append(rot(20, 400, "Correção de 2017: na análise corrigida, nem o joelho para dentro se associou à lesão", w=1624, tam=26, cor=TINTA, peso=600, alinha="center"))
diagrama(S, "rastreio", 460, p, rs, eyebrow="Coorte de 2016, futebol e handebol", titulo="O teste de salto não separa quem vai romper",
         fonte="Am J Sports Med 2016; correção 2017")

# 7. o time inteiro
p = [svg_abre(1664, 440, "Um time inteiro em aquecimento estruturado. Dois números: metade das rupturas, em todos os atletas; dois terços das rupturas sem contato, nas mulheres. Embaixo: o programa é o aquecimento, o ano inteiro")]
rs = []
for i in range(10):
    p.append(icone("t:run", 20 + (i % 5) * 120, 30 + (i // 5) * 130, 90, OXID))
for j, (n, t) in enumerate([("½", "das rupturas, em todos os atletas"), ("⅔", "das rupturas sem contato, nas mulheres")]):
    y = j * 150
    p.append(caixa(700, y, 964, 130, OXID, OXID_T, esp=3, rx=16))
    rs += [rot(724, y + 14, n, w=150, tam=80, cor=OXID, peso=700, serif=True, alinha="center"), rot(900, y + 44, t, w=740, tam=30, cor=TINTA, peso=700)]
p.append(caixa(0, 330, 1664, 110, TINTA, TINTA, esp=0, rx=16))
rs.append(rot(20, 362, "O programa é o aquecimento: todas, a temporada inteira, e permanente para quem já rompeu", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "time", 440, p, rs, eyebrow="Metanálise de metanálises, 2018", titulo="Treinar o time inteiro corta metade das rupturas",
         fonte="J Orthop Res 2018")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Risco de LCA em mulheres", "titulo": "Nenhum teste dispensa ninguém do programa",
          "regras": ["Ninguém sai de jogo pela fase do ciclo; ninguém troca de método para proteger o joelho",
                     "Não se rastreia para selecionar: nenhum teste separa quem vai romper",
                     "Programa para o time inteiro, o ano inteiro; permanente para quem já rompeu"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina e prepara", "x": "Transforma o aquecimento no programa e corrige a técnica na execução."},
                    {"ic": "h:doctor-female", "t": "Fisioterapia", "x": "Conduz o retorno de quem rompeu e mantém o programa depois da alta."},
                    {"ic": "h:doctor", "t": "Medicina", "x": "Responde sobre ciclo e contracepção com o que o dado autoriza."}]})

salvar("11-08.json", {"arquivo": "aulas/MOD11/11-08-risco-de-lca-em-mulheres.md",
                      "titulo": "Risco de LCA em mulheres", "subtitulo": "O que pesa, o que é folclore e o que funciona",
                      "nota_capa": "Entra por um aviso no celular e por um teste de salto numa equipe de basquete.",
                      "secoes": {"alerta": ["O erro.", "capa"], "esportes": ["O risco.", "esportes"],
                                 "ciclo": ["O ciclo.", "ciclo"], "rastreio": ["O teste e o programa.", "rastreio"]},
                      "slides": S})
