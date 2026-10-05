"""Spec do deck 14.8. Gera 14-08.json ao lado deste arquivo."""
from _base import *

S = []

RASC = [("“Melhorar a saúde das atletas do clube.”", "grande demais"),
        ("“Implantar um programa de prevenção de lesão.”", "isso é solução"),
        ("“Reduzir as lesões do time.”", "de quanto para quanto?")]

# 1. os três rascunhos
p = [svg_abre(1664, 420, "Três rascunhos de projeto riscados, de uma fisioterapeuta numa escolinha de futebol feminino sub-15: melhorar a saúde das atletas do clube; implantar um programa de prevenção de lesão; reduzir as lesões do time. Carimbos do orientador: grande demais; isso é solução; reduzir de quanto para quanto?")]
rs = []
for j, (t, c_) in enumerate(RASC):
    y = j * 140
    p.append(caixa(0, y, 1060, 116, MUDO, CARTAO, esp=2, rx=12))
    rs.append(rot(24, y + 34, t, w=1012, tam=30, cor=TINTA, peso=700, serif=True))
    p.append(f'<line x1="24" y1="{y + 58}" x2="1036" y2="{y + 58}" stroke="{FOSF}" stroke-width="5"/>')
    p.append(f'<rect x="1120" y="{y + 18}" width="440" height="80" rx="12" fill="none" stroke="{FOSF}" stroke-width="5" transform="rotate(-3 1340 {y + 58})"/>')
    rs.append(rot(1130, y + 40, c_, w=420, tam=28, cor=FOSF, peso=700, serif=True, alinha="center"))
diagrama(S, "rascunhos", 420, p, rs, eyebrow="Futebol feminino sub-15, uma fisioterapeuta começa o projeto", titulo="Três rascunhos, três devoluções, o mesmo erro")

# 2. as três armadilhas
p = [svg_abre(1664, 400, "Três armadilhas. Grande demais: não cabe em meses, nem num lugar. Solução disfarçada de problema: começa pelo que eu quero fazer. Sem medida de hoje: não dá para saber se melhorou. O erro: começar pelo tema, e não pelo problema")]
rs = []
for j, (t, x_, c) in enumerate([("grande demais", "não cabe nos meses do curso, nem num lugar só", GLIC),
                                ("solução disfarçada de problema", "começa pelo que eu quero fazer, e não pelo que acontece", FOSF),
                                ("sem medida de hoje", "não dá para saber, no fim, se alguma coisa mudou", AZUL)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 300, c, CARTAO, esp=3, rx=18))
    p.append(f'<circle cx="{x + 60}" cy="60" r="30" fill="{c}"/>')
    rs += [rot(x + 40, 40, str(j + 1), w=40, tam=32, cor=PAPEL, peso=700, serif=True, alinha="center"),
           rot(x + 110, 38, t, w=400, tam=28, cor=c, peso=700, serif=True, lh=1.2),
           rot(x + 24, 160, x_, w=488, tam=26, cor=TINTA, peso=700, lh=1.3)]
p.append(caixa(0, 330, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 348, "O erro: começar pelo tema, e não pelo problema.", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "armadilhas", 400, p, rs, eyebrow="O erro", titulo="O erro aparece em três formas")

# 3. as duas portas
p = [svg_abre(1664, 400, "Uma pessoa diante de duas portas. Uma porta larga e iluminada: o que eu sei fazer e quero fazer. Uma porta estreita: o que acontece aqui, hoje, e com que frequência. Por que o erro acontece")]
rs = []
p.append(f'<rect x="80" y="40" width="460" height="320" rx="16" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="5"/>')
p.append(f'<circle cx="500" cy="210" r="12" fill="{GLIC}"/>')
p.append(f'<rect x="1120" y="40" width="200" height="320" rx="12" fill="{OXID_T}" stroke="{OXID}" stroke-width="5"/>')
p.append(f'<circle cx="1290" cy="210" r="10" fill="{OXID}"/>')
p.append(menino(830, 380, 240, TINTA))
rs += [rot(100, 120, "o que eu sei fazer e quero fazer", w=420, tam=30, cor=GLIC, peso=700, serif=True, alinha="center", lh=1.25),
       rot(1340, 120, "o que acontece aqui, hoje, e com que frequência", w=324, tam=28, cor=OXID, peso=700, serif=True, lh=1.25),
       rot(560, 30, "a solução que eu trouxe pode não ser a resposta do meu lugar", w=540, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.25)]
diagrama(S, "portas", 400, p, rs, eyebrow="Por que o erro acontece", titulo="A gente chega ao projeto com a solução na cabeça")

# 4. a frase do problema
p = [svg_abre(1664, 440, "A frase do problema em cinco peças: onde; com quem; o que acontece hoje, com número; o que deveria acontecer; por que importa. Exemplo: escolinha de futebol feminino sub-15; vinte e poucas atletas; aquecimento completo em 1 de cada 4 sessões nas últimas 4 semanas; em todas as sessões; o programa só protege quem faz. Valores ilustrativos")]
rs = []
for j, (t, ex, c) in enumerate([("onde", "escolinha de futebol feminino sub-15", AZUL), ("com quem", "as vinte e poucas atletas", OXID),
                                ("hoje, com número", "aquecimento completo em 1 de cada 4 sessões, 4 semanas", FOSF),
                                ("o que deveria acontecer", "em todas as sessões", GLIC), ("por que importa", "o programa só protege quem faz", TINTA)]):
    x = j * 334
    p.append(f'<rect x="{x}" y="0" width="318" height="90" rx="12" fill="{c}"/>')
    rs.append(rot(x + 10, 26, t, w=298, tam=24, cor=PAPEL, peso=700, alinha="center"))
    p.append(caixa(x, 110, 318, 200, c, CARTAO, esp=3, rx=12))
    rs.append(rot(x + 16, 140, ex, w=286, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.3))
rs += [rot(0, 340, "lugar · pessoas · situação de hoje com número · situação desejada · motivo", w=1664, tam=26, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(0, 400, "valores ilustrativos", w=1664, tam=20, cor=MUDO, alinha="center")]
diagrama(S, "frase", 440, p, rs, eyebrow="A correção", titulo="O problema cabe numa frase com cinco peças")

# 5. as três perguntas
p = [svg_abre(1664, 420, "Modelo de melhoria, três perguntas: o que estamos tentando alcançar, a meta; como saberemos que uma mudança é uma melhora, o indicador; que mudança podemos fazer que leve a uma melhora, a ideia a testar. Primeiro o problema e a meta, depois a ideia"), defs(TINTA)]
rs = []
for j, (q, a, x_, c) in enumerate([("O que estamos tentando alcançar?", "a meta", "aquecimento completo em todas as sessões até o fim do semestre", AZUL),
                                   ("Como saberemos que uma mudança é uma melhora?", "o indicador", "proporção de sessões com aquecimento completo, por semana", OXID),
                                   ("Que mudança podemos fazer que leve a uma melhora?", "a ideia a testar", "a capitã conduz; o aquecimento vira parte do treino", GLIC)]):
    y = j * 140
    p.append(caixa(0, y, 760, 120, c, CARTAO, esp=3, rx=14))
    rs.append(rot(24, y + 28, q, w=712, tam=26, cor=c, peso=700, serif=True, lh=1.2))
    p.append(seta(770, y + 60, 830, y + 60, TINTA, "m0", esp=4))
    p.append(f'<rect x="850" y="{y}" width="220" height="120" rx="14" fill="{c}"/>')
    rs += [rot(860, y + 42, a, w=200, tam=24, cor=PAPEL, peso=700, alinha="center"),
           rot(1100, y + 22, x_, w=564, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "perguntas", 420, p, rs, eyebrow="Modelo de melhoria", titulo="Três perguntas transformam a frase em projeto, nessa ordem",
         fonte="The Improvement Guide, 2009")

# 6. o funil
p = [svg_abre(1664, 480, "Funil do tema ao problema: saúde das atletas; lesão no futebol feminino de base; prevenção de lesão na escolinha; aquecimento completo em 1 de cada 4 sessões, na sub-15, nas últimas 4 semanas. Do tema ao problema que cabe")]
rs = []
for j, (t, w, c) in enumerate([("saúde das atletas", 1500, MUDO), ("lesão no futebol feminino de base", 1180, AZUL),
                               ("prevenção de lesão na escolinha", 860, OXID), ("aquecimento completo em 1 de cada 4 sessões, na sub-15, em 4 semanas", 900, FOSF)]):
    y = j * 108
    x = (1664 - w) / 2
    p.append(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="{92 if j < 3 else 110}" rx="14" fill="{c}" opacity="{0.25 if j < 3 else 1}"/>')
    rs.append(rot(x + 20, y + 26 if j < 3 else y + 16, t, w=w - 40, tam=28 if j < 3 else 26, cor=TINTA if j < 3 else PAPEL, peso=700, alinha="center", serif=j == 3, lh=1.2))
rs.append(rot(0, 446, "nada se perdeu: o tema continua sendo a saúde das atletas", w=1664, tam=24, cor=MUDO, peso=700, alinha="center"))
diagrama(S, "funil", 480, p, rs, eyebrow="Do tema ao problema que cabe", titulo="O funil leva do tema a um problema com lugar, número e tamanho")

# 7. o teste do problema
p = [svg_abre(1664, 420, "Cinco perguntas de teste, cada uma com uma caixa de marcar: acontece no meu lugar de trabalho? Acontece com frequência? Consigo medir como está hoje em quatro semanas? Cabe nos meses do curso? Alguém além de mim se importa com isso? Cinco sim, e o problema serve")]
rs = []
for j, t in enumerate(["acontece no meu lugar de trabalho?", "acontece com frequência, ou foi um caso marcante?", "consigo medir como está hoje em quatro semanas?",
                       "cabe nos meses do curso?", "alguém além de mim se importa com isso?"]):
    y = j * 80
    p.append(f'<rect x="0" y="{y}" width="56" height="56" rx="10" fill="{CARTAO}" stroke="{OXID}" stroke-width="4"/>')
    p.append(f'<path d="M 12 {y + 28} L 24 {y + 42} L 46 {y + 14}" stroke="{OXID}" stroke-width="6" fill="none"/>')
    rs.append(rot(80, y + 10, t, w=1000, tam=28, cor=FOSF if j == 4 else TINTA, peso=700))
p.append(caixa(1160, 0, 504, 400, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1184, 30, "cinco sim: o problema serve", w=456, tam=30, cor=OXID, peso=700, serif=True, lh=1.2),
       rot(1184, 140, "um não: de volta ao funil", w=456, tam=26, cor=TINTA, peso=700),
       rot(1184, 230, "a última pergunta decide se o projeto sobrevive ao fim do curso", w=456, tam=24, cor=FOSF, peso=700, lh=1.3)]
diagrama(S, "teste", 420, p, rs, eyebrow="O teste do problema", titulo="Cinco perguntas dizem se o problema serve")

# 8. o rascunho reescrito
p = [svg_abre(1664, 420, "Os três rascunhos riscados à esquerda. À direita, a frase final: na escolinha de futebol feminino sub-15, o aquecimento neuromuscular completo aconteceu em 1 de cada 4 sessões nas últimas 4 semanas; a meta é todas as sessões até o fim do semestre, porque o programa só protege quem faz. Valores ilustrativos"), defs(TINTA)]
rs = []
for j, (t, _) in enumerate(RASC):
    y = 40 + j * 110
    p.append(caixa(0, y, 460, 86, MUDO, CARTAO, esp=2, rx=10))
    rs.append(rot(16, y + 18, t, w=428, tam=20, cor=MUDO, peso=700, serif=True, lh=1.2))
    p.append(f'<line x1="16" y1="{y + 43}" x2="444" y2="{y + 43}" stroke="{FOSF}" stroke-width="4"/>')
p.append(seta(480, 200, 560, 200, TINTA, "m0", esp=5))
p.append(caixa(580, 0, 1084, 420, OXID, OXID_T, esp=4, rx=18))
rs += [rot(610, 30, "“Na escolinha de futebol feminino sub-15, o aquecimento neuromuscular completo aconteceu em 1 de cada 4 sessões nas últimas 4 semanas; a meta é todas as sessões até o fim do semestre, porque o programa só protege quem faz.”", w=1024, tam=30, cor=TINTA, peso=700, serif=True, lh=1.35),
       rot(610, 380, "valores ilustrativos · a solução fica em aberto, para ser testada", w=1024, tam=20, cor=MUDO, peso=700)]
diagrama(S, "reescrito", 420, p, rs, eyebrow="O rascunho reescrito", titulo="Os três rascunhos viram uma frase pequena de propósito")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Projeto aplicado: o problema", "titulo": "Começar pelo que acontece, e não pelo que eu quero fazer",
          "regras": ["Comece pelo problema do seu lugar, não pela solução que trouxe",
                     "Uma frase: onde, com quem, hoje com número, meta, motivo",
                     "Cinco perguntas de teste, inclusive quem mais se importa"],
          "cards": [{"ic": "t:user", "t": "O aluno", "x": "Observa o lugar e mede a situação de hoje antes de escolher a ideia."},
                    {"ic": "t:book", "t": "O orientador", "x": "Devolve o rascunho até a frase ter as cinco peças."},
                    {"ic": "t:users", "t": "As pessoas do lugar", "x": "Dizem se o problema é delas também."}]})

salvar("14-08.json", {"arquivo": "aulas/MOD14/14-08-projeto-aplicado-como-definir-o-problema.md",
                      "titulo": "Projeto aplicado: como definir o problema", "subtitulo": "Do tema ao problema que cabe",
                      "nota_capa": "Entra por três rascunhos de uma fisioterapeuta numa escolinha de futebol feminino.",
                      "secoes": {"rascunhos": ["O erro.", "capa"], "portas": ["Por que acontece.", "portas"],
                                 "frase": ["A correção.", "frase"], "reescrito": ["O rascunho reescrito.", "reescrito"]},
                      "slides": S})
