"""Spec do deck 8.7. Gera 08-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "um3", "tipo": "frase", "fundo": "tinta", "eyebrow": "Descendo do bloqueio, no pé da adversária",
          "frase": "Um em cada três torceu de novo no ano seguinte.",
          "apoio": "Com o tratamento habitual, bem feito: gelo, faixa, alguns dias de muleta, volta sem dor em pouco mais de uma semana. O tratamento termina antes da parte que evita a próxima."})

S.append({"id": "ensaio", "tipo": "numeros", "eyebrow": "BMJ, 2009", "titulo": "Oito semanas em casa, sem supervisão",
          "numeros": [{"n": "522", "x": "atletas de 12 a 70 anos com entorse lateral recente, sorteados", "cor": "tinta"},
                      {"n": "33%", "x": "nova entorse em um ano com tratamento habitual", "cor": "verm"},
                      {"n": "22%", "x": "com o programa de equilíbrio e propriocepção em casa", "cor": "petr"}],
          "destaque": "Não foi um programa caro, conduzido todo dia por um profissional. A pessoa fez sozinha, depois de orientada.",
          "destaque_cor": "tinta", "fonte": "Ensaio holandês, BMJ 2009"})

p = [svg_abre(1664, 300, "Duas grades de cem pontos: 33 marcados com tratamento habitual e 22 marcados com o programa")]
def grade(x0, marcados, cor):
    for i in range(100):
        r, c = divmod(i, 20)
        cx, cy = x0 + c * 34, 40 + r * 44
        p.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{cor if i < marcados else GRADE}"/>')
grade(40, 33, FOSF)
grade(900, 22, OXID)
p.append("</svg>")
rs = [rot(30, 250, "tratamento habitual: 33 em 100", w=680, tam=24, cor=FOSF, peso=700),
      rot(890, 250, "com o programa: 22 em 100", w=680, tam=24, cor=OXID, peso=700)]
S.append({"id": "conta", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A conta que se leva para a conversa", "titulo": "Nove atletas fazendo, uma entorse a menos",
          "destaque": "33 − 22 = 11 em cada 100. 100 ÷ 11 ≈ 9. O programa não zera a recidiva: leva de um em três para perto de um em cinco.",
          "destaque_cor": "tinta", "fonte": "Conta feita a partir das duas proporções do ensaio"})

S.append({"id": "programa", "tipo": "cards", "por_linha": 4, "eyebrow": "Os quatro ingredientes do módulo de lesões", "titulo": "Em casa, oito semanas, depois da alta",
          "cards": [{"t": "Amplitude", "x": "a dorsiflexão, o tornozelo dobrando para a frente", "cor": "petr"},
                    {"t": "Força", "x": "panturrilha e estabilizadores do pé", "cor": "petr"},
                    {"t": "Equilíbrio", "x": "do apoio parado ao instável, olhos abertos a fechados", "cor": "ambar"},
                    {"t": "Gesto", "x": "salto, aterrissagem, mudança de direção", "cor": "verm"}],
          "destaque": "A fisioterapia ensina e entrega por escrito. Alguém pergunta toda semana se está sendo feito.",
          "destaque_cor": "tinta"})

S.append({"id": "ortese", "tipo": "numeros", "eyebrow": "O segundo número, 2014", "titulo": "Treino, órtese ou os dois",
          "numeros": [{"n": "27%", "x": "nova entorse com o treino de oito semanas", "cor": "ambar"},
                      {"n": "15%", "x": "com órtese semirrígida em todo esporte por 12 meses", "cor": "petr"},
                      {"n": "19%", "x": "com os dois, órtese por oito semanas", "cor": "petr"}],
          "destaque": "Órtese contra treino: risco relativo de 0,53. Mas gravidade, tempo perdido e custos não foram diferentes.",
          "destaque_cor": "tinta", "fonte": "384 atletas, ensaio holandês · Br J Sports Med 2014"})

S.append({"id": "juntar", "tipo": "duas", "eyebrow": "Sem briga de torcida", "titulo": "Uma protege, o outro reconstrói",
          "esq": {"t": "A órtese", "cor": "petr",
                  "itens": ["protege enquanto a capacidade não voltou", "funciona desde o primeiro dia", "depende de usar em todo treino, por meses"]},
          "dir": {"t": "O treino", "cor": "ambar",
                  "itens": ["reconstrói amplitude, força e controle", "leva semanas para fazer efeito", "depende de fazer, e muita gente para"]},
          "destaque": "Para quem já torceu, as duas se somam. A pergunta útil: qual delas essa pessoa vai de fato usar ou fazer, e por quanto tempo?",
          "destaque_cor": "tinta", "fonte": "Revisão de revisões, Br J Sports Med 2017"})

S.append({"id": "oito", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "A próxima entorse se decide nas oito semanas depois da alta.",
          "apoio": "A dor vai embora sozinha. A capacidade do tornozelo não. E é quando a dor vai embora que a pessoa para de cuidar do tornozelo."})

S.append({"id": "paass", "tipo": "cards", "por_linha": 5, "eyebrow": "Consenso internacional de 2021", "titulo": "Cinco perguntas antes de voltar",
          "cards": [{"t": "Dor", "x": "no esporte e nas últimas 24 horas", "cor": "verm"},
                    {"t": "Tornozelo", "x": "amplitude, força, resistência, potência", "cor": "petr"},
                    {"t": "Percepção", "x": "confiança, estabilidade, prontidão", "cor": "ambar"},
                    {"t": "Controle", "x": "equilíbrio parado e em movimento", "cor": "petr"},
                    {"t": "Desempenho", "x": "saltos, agilidade, um treino inteiro", "cor": "tinta"}],
          "destaque": "98% de concordância entre os participantes. A decisão depende das cinco, não da ausência de dor.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2021"})

S.append({"id": "barato", "tipo": "tabela", "eyebrow": "Sem laboratório", "titulo": "Um jeito barato de responder cada uma",
          "cab": ["Pergunta", "Como medir"],
          "larguras": [22, 78],
          "linhas": [["Dor", "nota de 0 a 10 no treino e na manhã seguinte"],
                     ["Tornozelo", "joelho à parede com fita; elevações de calcanhar numa perna, dos dois lados"],
                     ["Percepção", "“Você confia nesse tornozelo para bloquear e cair?”; questionário de instabilidade"],
                     ["Controle", "apoio numa perna, olhos abertos e fechados; alcance em várias direções"],
                     ["Desempenho", "saltos numa perna, de lado e para a frente; o treino completo, observado"]],
          "destaque": "Nenhum valor mágico: compare com o outro lado e com a própria pessoa ao longo das semanas.",
          "destaque_cor": "tinta"})

S.append({"id": "erros", "tipo": "cards", "por_linha": 3, "eyebrow": "O que os números explicam", "titulo": "Três erros de alta",
          "cards": [{"t": "Alta pela dor", "x": "o erro que produz o um em cada três", "cor": "verm"},
                    {"t": "Órtese sem treino", "x": "quando a órtese sai, o tornozelo é o mesmo de antes", "cor": "ambar"},
                    {"t": "Programa que para no jogo", "x": "quem para na segunda semana não fez o programa que funcionou", "cor": "ambar"}],
          "destaque_cor": "tinta"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem faz o quê", "titulo": "Da beira da quadra às oito semanas",
          "cab": ["Quem", "O que faz"],
          "larguras": [26, 74],
          "linhas": [["Médico", "descarta fratura e lesão associada; imagem; analgesia nos primeiros dias"],
                     ["Fisioterapia", "fase inicial; ensina e entrega o programa; aplica as cinco perguntas"],
                     ["Preparação física", "o programa dentro do aquecimento; saltos e mudança de direção"],
                     ["Treinador", "cobra a órtese indicada; não conta como recuperada quem parou o programa"],
                     ["Atleta", "sabe a conta: nove fazendo, uma entorse a menos"]],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Tornozelo depois da entorse", "titulo": "A dor não decide a alta",
          "regras": ["Um em três com o tratamento habitual; perto de um em cinco com oito semanas em casa",
                     "Órtese reduziu o número de novas entorses, não a gravidade",
                     "Retorno por cinco perguntas"],
          "cards": [{"t": "Fisioterapia", "x": "Ensina o programa e decide pelas cinco perguntas."},
                    {"t": "Preparação e treinador", "x": "Põem o programa na semana e cobram a órtese."},
                    {"t": "Atleta", "x": "Faz as oito semanas depois da alta."}],
          "quem": "Próxima aula: ombro e coluna; parar, modificar ou manter."})

spec = {"arquivo": "aulas/MOD08/08-07-reabilitacao-do-tornozelo-e-prevencao-de-recidiva.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Tornozelo depois da entorse", "subtitulo": "A recidiva em números e as cinco perguntas do retorno",
        "nota_capa": "Entra por um em cada três.",
        "secoes": {"um3": ["O número e o ensaio de 2009.", "capa"],
                   "programa": ["O programa e a órtese.", "programa"],
                   "oito": ["As oito semanas e as cinco perguntas.", "oito"],
                   "erros": ["Erros de alta e quem faz o quê.", "erros"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-07.json"), "w"), ensure_ascii=False, indent=1)
print("08-07.json:", len(S), "slides")
