"""Spec do deck 8.6. Gera 08-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "macas", "tipo": "frase", "fundo": "tinta", "eyebrow": "Duas macas no departamento médico de um clube de futebol",
          "frase": "Parar de tratar quando a dor some, ou tratar sem saber o que se está tratando.",
          "apoio": "Um meia sem dor há uma semana depois de lesão de posterior de coxa, querendo jogar domingo. Um lateral com dor na virilha há dois meses. A maior parte dos dados é do futebol, e isso limita."})

S.append({"id": "roteiro", "tipo": "duas", "eyebrow": "O roteiro", "titulo": "Dois roteiros, três passos cada",
          "esq": {"t": "Posterior da coxa, fase final", "cor": "petr",
                  "itens": ["o que já está resolvido", "expor à velocidade antes do jogo", "critérios de retorno"]},
          "dir": {"t": "Virilha", "cor": "ambar",
                  "itens": ["dar nome: “pubalgia” não é diagnóstico", "medir", "tratar com carga"]},
          "destaque_cor": "tinta"})

S.append({"id": "resolvido", "tipo": "cards", "por_linha": 3, "eyebrow": "Posterior da coxa · passo um", "titulo": "O que o módulo de lesões já resolveu",
          "cards": [{"t": "Exercício em alongamento", "x": "o músculo trabalhando alongado encurta o retorno", "cor": "petr"},
                    {"t": "Desconforto tolerável", "x": "não atrasa a liberação; preserva força e comprimento de fibra", "cor": "petr"},
                    {"t": "Em aberto", "x": "do exercício na maca ao sprint do jogo, e os critérios da volta", "cor": "ambar"}],
          "destaque_cor": "tinta", "fonte": "Ensaio australiano, J Orthop Sports Phys Ther 2020"})

p = [svg_abre(1664, 280, "Esquema: exposição semanal à corrida em alta velocidade durante a reabilitação, subindo em degraus até o nível típico de jogo antes do primeiro jogo")]
p.append(f'<line x1="60" y1="240" x2="1600" y2="240" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="60" x2="1600" y2="60" stroke="{TINTA}" stroke-width="3" stroke-dasharray="12 8"/>')
nivel = [30, 55, 85, 120, 150, 170, 180]
for i, v in enumerate(nivel):
    x = 90 + i * 190
    p.append(f'<rect x="{x}" y="{240 - v}" width="150" height="{v}" rx="6" fill="{OXID}" fill-opacity="{0.4 + i*0.08:.2f}"/>')
p.append(f'<rect x="1440" y="60" width="150" height="180" rx="6" fill="{FOSF}" fill-opacity="0.85"/>')
p.append("</svg>")
rs = [rot(60, 20, "volume típico de alta velocidade num jogo", w=600, tam=22, cor=TINTA, peso=700),
      rot(90, 246, "corridas progressivas", w=340, tam=20, cor=MUDO),
      rot(660, 246, "acelerações e perto do máximo", w=420, tam=20, cor=MUDO),
      rot(1400, 246, "primeiro jogo", w=230, tam=20, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "velocidade", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Posterior da coxa · passo dois", "titulo": "Expor à velocidade antes do jogo",
          "destaque": "Semanas com corrida de alta velocidade acima do habitual se associaram a mais lesão na semana seguinte, no futebol australiano. O pico é o risco.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Br J Sports Med 2016"})

S.append({"id": "criterios", "tipo": "cards", "por_linha": 4, "eyebrow": "Posterior da coxa · passo três", "titulo": "58 especialistas, 28 centros da FIFA",
          "cards": [{"t": "Palpação", "x": "sem dor ao apertar o músculo", "cor": "petr"},
                    {"t": "Força e flexibilidade", "x": "sem dor nos testes", "cor": "petr"},
                    {"t": "Desempenho funcional", "x": "sem dor durante e depois, corrida e gesto incluídos", "cor": "petr"},
                    {"t": "Ressonância", "x": "fora: a imagem inicial não prediz a nova lesão", "cor": "verm"}],
          "destaque": "Sem consenso sobre força excêntrica como critério obrigatório. Decisão compartilhada, com o jogador.",
          "destaque_cor": "tinta", "fonte": "Consenso Delphi, Br J Sports Med 2017"})

S.append({"id": "sprint", "tipo": "frase", "fundo": "tinta", "eyebrow": "A regra da primeira maca",
          "frase": "O primeiro sprint máximo não pode ser no jogo.",
          "apoio": "Sem dor há uma semana é necessário, não suficiente. Quantas vezes ele já correu perto do máximo, em quantas sessões, e como estava no dia seguinte?"})

S.append({"id": "doha", "tipo": "tabela", "eyebrow": "Virilha · passo um", "titulo": "Dar nome: a classificação de Doha",
          "cab": ["Grupo", "O que inclui"],
          "larguras": [34, 66],
          "linhas": [["Entidades clínicas", "dor relacionada ao adutor, ao iliopsoas, à região inguinal, ao púbis"],
                     ["Relacionada ao quadril", "a articulação do quadril é a fonte"],
                     ["Outras causas", "inclusive o que não é musculoesquelético"]],
          "destaque": "Pela história e pelo exame. “Dor relacionada ao adutor” aponta o tratamento; “pubalgia” não aponta nada.",
          "destaque_cor": "tinta", "fonte": "24 especialistas de 14 países · Br J Sports Med 2015"})

S.append({"id": "medir", "tipo": "duas", "eyebrow": "Virilha · passo dois", "titulo": "Medir, porque a sensação engana",
          "esq": {"t": "Aperto de adução", "cor": "petr",
                  "itens": ["dinamômetro ou esfigmomanômetro dobrado", "força e dor no esforço", "sempre na mesma posição"]},
          "dir": {"t": "Questionário de quadril e virilha", "cor": "ambar",
                  "itens": ["37 perguntas, seis domínios", "dor, sintomas, função no esporte, participação", "a perspectiva do atleta"]},
          "destaque": "“Está melhorando?” deixa de depender de como foi o último treino.",
          "destaque_cor": "tinta", "fonte": "Copenhague, Br J Sports Med 2011"})

S.append({"id": "holmich", "tipo": "numeros", "eyebrow": "Virilha · passo três", "titulo": "Tratar com carga: o ensaio de 1999",
          "numeros": [{"n": "23", "x": "atletas de volta ao esporte sem dor, com treino ativo de força e coordenação da pelve", "cor": "petr"},
                      {"n": "4", "x": "com fisioterapia sem treino ativo, com recursos passivos", "cor": "verm"}],
          "destaque": "Dor relacionada ao adutor de longa duração: o que muda o desfecho é a carga, não o recurso passivo.",
          "destaque_cor": "tinta", "fonte": "Ensaio dinamarquês sorteado, Lancet 1999"})

S.append({"id": "manter", "tipo": "numeros", "eyebrow": "Depois que ele voltar", "titulo": "Um exercício de adutores, uma vez por semana",
          "numeros": [{"n": "35", "x": "equipes semiprofissionais sorteadas", "cor": "tinta"},
                      {"n": "13,5%", "x": "prevalência de problemas na virilha com o programa, contra 21,3% sem", "cor": "petr"},
                      {"n": "−41%", "x": "risco de relatar problema na virilha", "cor": "petr"}],
          "destaque": "Três vezes por semana na pré-temporada, uma vez por semana na temporada: dose que sobrevive ao calendário.",
          "destaque_cor": "tinta", "fonte": "Futebol masculino norueguês · Br J Sports Med 2019"})

S.append({"id": "armadilhas", "tipo": "cards", "por_linha": 4, "eyebrow": "Juntando as duas macas", "titulo": "Quatro armadilhas",
          "cards": [{"t": "“Pubalgia”", "x": "tratar sem saber a fonte", "cor": "ambar"},
                    {"t": "Repouso e volta igual", "x": "a dor some e volta junto com a carga", "cor": "ambar"},
                    {"t": "Passivo antes da carga", "x": "recurso ou injeção como tratamento principal", "cor": "verm"},
                    {"t": "Esquecer a manutenção", "x": "a recidiva mora na volta sem exercícios", "cor": "verm"}],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Posterior da coxa e virilha", "titulo": "A última fase é a que evita a próxima lesão",
          "regras": ["Posterior: velocidade em degraus e critérios de dor e função, sem ressonância",
                     "Virilha: nome pela classificação de Doha, medida e carga ativa",
                     "Os dois: manutenção na temporada"],
          "cards": [{"t": "Médico", "x": "Dá o nome e descarta outras causas."},
                    {"t": "Fisioterapia", "x": "Conduz a carga e mede."},
                    {"t": "Preparação física", "x": "Constrói a velocidade e mantém o programa."}],
          "quem": "Próxima aula: o tornozelo, a região mais lesionada e a que mais recidiva."})

spec = {"arquivo": "aulas/MOD08/08-06-reabilitacao-de-isquiotibiais-e-regiao-inguinal.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Posterior da coxa e virilha", "subtitulo": "O roteiro da fase final e da dor que não passa",
        "nota_capa": "Entra por duas macas num departamento médico de futebol.",
        "secoes": {"macas": ["As duas macas e o roteiro.", "capa"],
                   "resolvido": ["Posterior da coxa na fase final.", "resolvido"],
                   "doha": ["Virilha: nome, medida, carga e manutenção.", "doha"],
                   "armadilhas": ["Armadilhas e fecho.", "armadilhas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-06.json"), "w"), ensure_ascii=False, indent=1)
print("08-06.json:", len(S), "slides")
