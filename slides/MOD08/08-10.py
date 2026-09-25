"""Spec do deck 8.10. Gera 08-10.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "simetria", "tipo": "frase", "fundo": "tinta", "eyebrow": "Um armador de basquete, oito meses depois do cruzado",
          "frase": "Noventa e cinco por cento de simetria. E se a outra perna também perdeu força?",
          "apoio": "O índice compara uma perna com a outra. 95% de uma perna enfraquecida pode ser bem menos do que ele tinha antes da lesão."})

S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "O roteiro da bateria", "titulo": "Cinco passos",
          "itens": [{"t": "O que medir", "x": "força, salto, movimento, gesto do esporte, cabeça", "cor": "petr"},
                    {"t": "Contra o quê comparar", "x": "a outra perna, a capacidade de antes, valores de referência", "cor": "ambar"},
                    {"t": "Como o esporte cobra", "x": "cansado, reagindo, mudando de direção", "cor": "petr"},
                    {"t": "A cabeça", "x": "confiança e medo de nova lesão", "cor": "ambar"},
                    {"t": "A leitura", "x": "o que a bateria prevê e o que não prevê", "cor": "tinta"}],
          "gap_itens": 8})

S.append({"id": "medir", "tipo": "tabela", "eyebrow": "Passo um", "titulo": "O que medir, com e sem laboratório",
          "cab": ["Domínio", "Como"],
          "larguras": [24, 76],
          "linhas": [["Força", "isocinético; ou dinamômetro de mão com faixa, ou repetições com carga padronizada"],
                     ["Salto", "quatro saltos numa perna: simples, triplo, cruzado, seis metros cronometrados"],
                     ["Movimento", "aterrissagem filmada de frente: joelho para dentro, tronco que desaba"],
                     ["Gesto", "no basquete: parada brusca, corte, salto para o rebote"],
                     ["Cabeça", "o passo quatro"]],
          "destaque": "A distância do salto pode ser boa com uma aterrissagem ruim.",
          "destaque_cor": "tinta", "fonte": "Saltos: Am J Sports Med 1991"})

S.append({"id": "epic", "tipo": "numeros", "eyebrow": "Passo dois · 70 pacientes, seis meses depois", "titulo": "Contra o quê comparar muda o resultado",
          "numeros": [{"n": "57%", "x": "passaram no índice de simetria de 90% em todos os testes", "cor": "ambar"},
                      {"n": "29%", "x": "passaram na comparação com a capacidade de antes da lesão", "cor": "verm"},
                      {"n": "34%", "x": "passaram no primeiro e não no segundo", "cor": "verm"}],
          "destaque": "A comparação com a capacidade de antes foi bem mais sensível para identificar quem teria a segunda lesão do cruzado.",
          "destaque_cor": "tinta", "fonte": "Coorte de Delaware · J Orthop Sports Phys Ther 2017"})

p = [svg_abre(1664, 300, "Esquema: a perna boa antes da cirurgia é alta; depois de meses, a perna boa cai e a operada sobe, e as duas se encontram num ponto simétrico mais baixo que o de antes")]
p.append(f'<line x1="60" y1="270" x2="1600" y2="270" stroke="{MUDO}" stroke-width="3"/>')
barras = [(160, 230, MUDO, "perna boa, antes"), (660, 175, OXID, "perna boa, depois"), (960, 165, AZUL, "perna operada, depois")]
for x, h, c, _ in barras:
    p.append(f'<rect x="{x}" y="{270 - h}" width="200" height="{h}" rx="8" fill="{c}" fill-opacity="0.85"/>')
p.append(f'<line x1="120" y1="40" x2="1500" y2="40" stroke="{TINTA}" stroke-width="3" stroke-dasharray="12 8"/>')
p.append(f'<line x1="620" y1="95" x2="1500" y2="95" stroke="{FOSF}" stroke-width="3" stroke-dasharray="6 6"/>')
p.append("</svg>")
rs = [rot(120, 276, "perna boa, antes", w=280, tam=22, cor=MUDO, peso=700, alinha="center"),
      rot(620, 276, "perna boa, depois", w=280, tam=22, cor=OXID, peso=700, alinha="center"),
      rot(920, 276, "operada, depois", w=280, tam=22, cor=AZUL, peso=700, alinha="center"),
      rot(1220, 6, "onde ele precisa estar", w=380, tam=22, cor=TINTA, peso=700),
      rot(1220, 100, "simétrico, e mais baixo", w=380, tam=22, cor=FOSF, peso=700)]
S.append({"id": "engana", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Por que o índice engana", "titulo": "As duas pernas se encontram embaixo",
          "destaque": "Medir as duas pernas cedo, antes da cirurgia quando der. E olhar o valor absoluto, não só a porcentagem.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "distancia", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Simetria mede a distância entre as pernas, não a distância até o esporte.",
          "apoio": "Continua útil: uma perna muito mais fraca é problema, sempre. Mas simetria boa não diz, sozinha, que o atleta está pronto."})

S.append({"id": "esporte", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo três", "titulo": "Testar como o esporte cobra",
          "cards": [{"t": "Cansado", "x": "saltos e aterrissagem depois de um bloco de esforço", "cor": "ambar"},
                    {"t": "Reagindo", "x": "a direção só aparece depois de um sinal", "cor": "ambar"},
                    {"t": "No treino", "x": "o gesto do esporte filmado, não só o teste isolado", "cor": "petr"}],
          "destaque": "A faixa do controlado ao caótico da aula do cruzado, usada como teste.",
          "destaque_cor": "tinta"})

S.append({"id": "cabeca", "tipo": "duas", "eyebrow": "Passo quatro", "titulo": "Medir a cabeça",
          "esq": {"t": "O questionário australiano, 2008", "cor": "petr",
                  "itens": ["confiança no joelho", "emoções", "avaliação de risco"]},
          "dir": {"t": "Para que serve", "cor": "ambar",
                  "itens": ["achar testes físicos bons com a cabeça longe", "quem volta protegendo o joelho joga diferente", "abrir a conversa da decisão"]},
          "destaque": "O medo de nova lesão é uma das razões mais citadas para não voltar, e não aparece no dinamômetro.",
          "destaque_cor": "tinta", "fonte": "Phys Ther Sport 2008"})

S.append({"id": "preve", "tipo": "numeros", "eyebrow": "Passo cinco · o que a bateria prevê", "titulo": "Ajuda muito, não prevê o indivíduo",
          "numeros": [{"n": "158", "x": "atletas profissionais homens que voltaram ao nível de antes", "cor": "tinta"},
                      {"n": "4×", "x": "mais ruptura do enxerto sem cumprir seis critérios de alta", "cor": "verm"}],
          "destaque": "Metanálise de 2019: passar nos testes, menos ruptura do enxerto; a proteção não apareceu para o outro joelho. A bateria alimenta a decisão, não a substitui.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2016 · Sports Med 2019"})

S.append({"id": "consultorio", "tipo": "cards", "por_linha": 5, "eyebrow": "Sem laboratório", "titulo": "Uma bateria de consultório",
          "cards": [{"t": "Força", "x": "dinamômetro de mão ou repetições", "cor": "petr"},
                    {"t": "Saltos", "x": "fita métrica e cronômetro", "cor": "petr"},
                    {"t": "Aterrissagem", "x": "celular, sempre no mesmo ângulo", "cor": "ambar"},
                    {"t": "Reação", "x": "alguém aponta a direção", "cor": "ambar"},
                    {"t": "Prontidão", "x": "o questionário", "cor": "tinta"}],
          "destaque": "Medir cedo, padronizar tudo e registrar valores absolutos, não só a porcentagem.",
          "destaque_cor": "tinta"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem faz o quê", "titulo": "Cada domínio tem dono",
          "cab": ["Quem", "Na bateria"],
          "larguras": [26, 74],
          "linhas": [["Fisioterapia", "testes clínicos e de força; guarda os valores de antes"],
                     ["Preparação física", "saltos, velocidade, fadiga; a referência do esporte e do atleta"],
                     ["Psicologia", "prontidão e medo; sem psicólogo, o questionário e a conversa"],
                     ["Médico", "junta com o tempo biológico do tecido, que o teste não mede"]],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Testes de retorno", "titulo": "Informação para a decisão, não a decisão",
          "regras": ["Vários domínios, não um",
                     "Comparar com a capacidade de antes, não só com a outra perna",
                     "Cansado, reagindo, e com a cabeça medida"],
          "cards": [{"t": "Fisioterapia", "x": "Força e testes clínicos."},
                    {"t": "Preparação física", "x": "Saltos, velocidade e fadiga."},
                    {"t": "Psicologia e médico", "x": "A cabeça e o tempo do tecido."}],
          "quem": "Próxima aula: a decisão de retorno, compartilhada."})

spec = {"arquivo": "aulas/MOD08/08-10-testes-de-retorno-ao-esporte.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Testes de retorno ao esporte", "subtitulo": "O que medir, contra o quê, e como não ser enganado",
        "nota_capa": "Entra por um armador com 95% de simetria.",
        "secoes": {"simetria": ["O número que tranquiliza e o roteiro.", "capa"],
                   "epic": ["Contra o quê comparar.", "epic"],
                   "esporte": ["Como o esporte cobra e a cabeça.", "esporte"],
                   "preve": ["O que prevê, o consultório e quem faz.", "preve"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-10.json"), "w"), ensure_ascii=False, indent=1)
print("08-10.json:", len(S), "slides")
