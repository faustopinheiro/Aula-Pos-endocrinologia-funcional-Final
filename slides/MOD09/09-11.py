"""Spec do deck 9.11. Gera 09-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "bilhete", "tipo": "frase", "fundo": "tinta", "eyebrow": "Segundo caso do módulo",
          "frase": "“Liberada para treinar com o grupo.”",
          "apoio": "Jogadora de basquete amador, na casa dos trinta anos, técnica de enfermagem em plantões de 12 por 36. Três semanas afastada por entorse de tornozelo. Liberada para qual treino? Em qual semana? Fazendo o quê?"})

# três degraus
p = [svg_abre(1664, 330, "Três degraus do retorno: participar, esporte, desempenho, com a reintegração entre o primeiro e o segundo"),
     "<defs>" + seta_marker("dg", FOSF) + "</defs>"]
for i, c in enumerate([OXID, GLIC, TINTA]):
    x = 140 + i * 480
    h = 90 + i * 80
    p.append(f'<rect x="{x}" y="{290 - h}" width="400" height="{h}" rx="8" fill="{c}"/>')
p.append(f'<path d="M 420 190 Q 560 60 700 120" fill="none" stroke="{FOSF}" stroke-width="5" marker-end="url(#dg)"/>')
p.append("</svg>")
rs = [rot(140, 230, "voltar a participar", w=400, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(620, 150, "voltar ao esporte", w=400, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(1100, 70, "voltar ao desempenho", w=400, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(360, 20, "reintegração", w=300, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(140, 294, "ela está aqui", w=400, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "degraus", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde ela está", "titulo": "A ponte entre participar e voltar ao esporte",
          "destaque": "O bilhete diz que o tecido está pronto para treinar. Não diz que ela está pronta para o jogo de sábado.",
          "destaque_cor": "tinta", "fonte": "Consenso de Berna, Br J Sports Med 2016 (módulo de reabilitação)"})

S.append({"id": "distancia", "tipo": "duas", "eyebrow": "Por que não basta entrar e fazer tudo", "titulo": "Dois ambientes diferentes",
          "esq": {"t": "O que a reabilitação treinou", "cor": "petr",
                  "itens": ["exercício previsível", "o ritmo dela, com intervalo", "ninguém do outro lado"]},
          "dir": {"t": "O que o treino coletivo exige", "cor": "verm",
                  "itens": ["reagir à bola e à adversária", "aterrissar com contato", "saltos seguidos, no ritmo do grupo"]},
          "destaque": "A força do tornozelo pode estar recuperada e ela ainda não ter visto nada disso.",
          "destaque_cor": "tinta"})

# contínuo controle-caos
marcas = ["exercício planejado", "reação simples", "oposição com regras", "jogo"]
p = [svg_abre(1664, 260, "Barra do controle ao caos com quatro marcas: exercício planejado, reação simples, oposição com regras, jogo"),
     '<defs><linearGradient id="cc" x1="0" x2="1" y1="0" y2="0">'
     f'<stop offset="0" stop-color="{OXID}"/><stop offset="0.55" stop-color="{GLIC}"/><stop offset="1" stop-color="{FOSF}"/></linearGradient></defs>',
     '<rect x="120" y="100" width="1420" height="40" rx="20" fill="url(#cc)"/>']
for i in range(4):
    x = 180 + i * 433
    p.append(f'<circle cx="{x}" cy="120" r="22" fill="#F7F6F2" stroke="{TINTA}" stroke-width="4"/>')
p.append("</svg>")
rs = [rot(120, 40, "controle", w=300, tam=26, cor=OXID, peso=700),
      rot(1240, 40, "caos", w=300, tam=26, cor=FOSF, peso=700, alinha="right")]
for i, t in enumerate(marcas):
    x = 180 + i * 433
    rs.append(rot(x - 150, 160, t, w=300, tam=22, cor=TINTA, alinha="center"))
S.append({"id": "caos", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O contínuo do controle ao caos", "titulo": "Acrescentar perceber e reagir, junto com a carga",
          "destaque": "Modelo de prática construído no futebol profissional inglês, não um ensaio clínico. Organiza a pergunta: onde ela está, e qual é o próximo passo.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2019"})

S.append({"id": "etapas", "tipo": "tabela", "eyebrow": "O plano dela", "titulo": "Quatro etapas dentro dos treinos do grupo",
          "cab": ["Etapa", "Faz com o grupo", "Fica de fora"],
          "larguras": [14, 46, 40],
          "linhas": [["1", "aquecimento e técnica sem oposição", "coletivo com oposição"],
                     ["2", "oposição controlada: 2 contra 2, 3 contra 3", "coletivo livre"],
                     ["3", "treino completo, com coletivo", "jogo de sábado"],
                     ["4", "jogo com minutos combinados", "nada"]],
          "destaque": "Para avançar: tornozelo sem piora na manhã seguinte, sem inchaço, nota de esforço perto do planejado. Não atingiu, repete a etapa.",
          "destaque_cor": "tinta", "fonte": "Exemplo de prática corrente, sem validação"})

# semana: trabalho + treino
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
plantao = [1, 0, 1, 0, 1, 0, 0]
treino = [0, 1, 0, 1, 0, 1, 0]
p = [svg_abre(1664, 320, "Semana com plantões de doze horas em cinza e treinos em cor, em dias alternados")]
base = 260
for i in range(7):
    x = 150 + i * 200
    y = base
    if plantao[i]:
        p.append(f'<rect x="{x}" y="{y - 150}" width="120" height="150" rx="6" fill="{GRADE}"/>')
        y -= 150
    if treino[i]:
        p.append(f'<rect x="{x}" y="{y - 100}" width="120" height="100" rx="6" fill="{GLIC if i < 5 else FOSF}"/>')
p.append(f'<line x1="100" y1="{base}" x2="1560" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(150 + i * 200, base + 10, d, w=120, tam=22, cor=MUDO, alinha="center") for i, d in enumerate(dias)]
rs += [rot(150 + i * 200, base - 90, "plantão", w=120, tam=20, cor=TINTA, alinha="center") for i in range(7) if plantao[i]]
rs += [rot(150 + i * 200, base - 60, "treino" if i < 5 else "jogo", w=120, tam=20, cor="#F7F6F2", peso=700, alinha="center") for i in range(7) if treino[i]]
rs.append(rot(100, 0, "cinza: trabalho · cor: basquete", w=500, tam=20, cor=MUDO))
S.append({"id": "plantao", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A carga que não aparece no treino", "titulo": "A semana dela não é só basquete",
          "destaque": "Carga inclui calendário, viagens e carga psicológica. No amador, o trabalho é muitas vezes a maior parte da semana.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · consenso do COI, Br J Sports Med 2016"})

S.append({"id": "encaixar", "tipo": "duas", "eyebrow": "Encaixar na semana dela", "titulo": "Não só qual etapa: em qual dia",
          "esq": {"t": "Depois de uma folga", "cor": "petr",
                  "itens": ["a sessão que avança de etapa", "o coletivo, quando chegar a hora"]},
          "dir": {"t": "Depois do plantão noturno", "cor": "ambar",
                  "itens": ["fica na etapa anterior", "ou só a parte técnica"]},
          "destaque": "Ela está no terceiro momento de risco do módulo de lesões: a volta depois de uma pausa. Reposicionar rende mais do que reduzir.",
          "destaque_cor": "tinta"})

S.append({"id": "etapa", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Liberada não quer dizer pronta para tudo. Quer dizer pronta para a próxima etapa.",
          "apoio": "O bilhete da fisioterapia é o começo de um plano, não o fim de um processo."})

S.append({"id": "medir", "tipo": "cards", "por_linha": 3, "eyebrow": "Como acompanhar", "titulo": "Três medidas, sem laboratório",
          "cards": [{"t": "Nota da sessão", "x": "contra o planejado; cinco que volta oito é o grupo exigindo mais", "cor": "petr"},
                    {"t": "Tornozelo na manhã seguinte", "x": "dor de 0 a 10 e se há inchaço: a resposta do tecido", "cor": "ambar"},
                    {"t": "Um salto por semana", "x": "numa perna só, dos dois lados, do mesmo jeito: para ver a linha", "cor": "tinta"}],
          "destaque": "Retoma a aula de carga interna e a de testes físicos.", "destaque_cor": "tinta"})

S.append({"id": "alerta", "tipo": "cards", "por_linha": 2, "eyebrow": "Como reconhecer que não está funcionando", "titulo": "Quatro sinais",
          "cards": [{"t": "Dor que piora", "x": "de uma etapa para outra, ou que não volta ao nível de antes em 24 horas", "cor": "verm"},
                    {"t": "Nota acima do planejado", "x": "em sessões seguidas", "cor": "ambar"},
                    {"t": "Nova entorse ou falseio", "x": "o tornozelo cede", "cor": "verm"},
                    {"t": "Evita o gesto", "x": "não sobe para o rebote, freia nas mudanças de direção, mesmo sem dor", "cor": "ambar"}],
          "destaque": "Voltar uma etapa, não voltar ao zero. E conversar com a fisioterapia.",
          "destaque_cor": "tinta"})

S.append({"id": "papeis", "tipo": "cards", "por_linha": 2, "eyebrow": "Uma folha só, compartilhada", "titulo": "Quem faz o quê",
          "cards": [{"t": "Fisioterapia", "x": "critério do tecido e o que ainda está proibido", "cor": "petr"},
                    {"t": "Preparação física", "x": "a dose dentro do treino do grupo: qual etapa, em qual dia", "cor": "petr"},
                    {"t": "Técnico", "x": "sabe a etapa e os minutos combinados, não o prontuário", "cor": "ambar"},
                    {"t": "Atleta", "x": "conta a escala, a noite mal dormida e o tornozelo da manhã", "cor": "tinta"}]})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Reintegração ao treinamento coletivo", "titulo": "O jogo de sábado tem data prevista, não data marcada",
          "regras": ["Quatro etapas dentro dos treinos do grupo",
                     "Avanço de etapa sempre depois de uma folga",
                     "Três medidas e uma regra para os sinais de alerta"],
          "cards": [{"t": "Preparação física", "x": "Dosa a volta dentro do grupo."},
                    {"t": "Fisioterapia", "x": "Mantém o critério do tecido."},
                    {"t": "Atleta", "x": "Traz a escala de plantões."}],
          "quem": "Próxima aula: sono e recuperação como variáveis de treino, e o fecho do módulo."})

spec = {"arquivo": "aulas/MOD09/09-11-reintegracao-ao-treinamento-coletivo.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Reintegração ao treinamento coletivo", "subtitulo": "Da alta da reabilitação ao jogo",
        "nota_capa": "Entra pelo bilhete da fisioterapia de uma jogadora de basquete amador.",
        "secoes": {"bilhete": ["O caso e onde ela está.", "capa"],
                   "distancia": ["A distância entre reabilitação e grupo, e o plano.", "distancia"],
                   "plantao": ["A carga do trabalho e a semana dela.", "plantao"],
                   "medir": ["Medir, reconhecer e dividir o trabalho.", "medir"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-11.json"), "w"), ensure_ascii=False, indent=1)
print("09-11.json:", len(S), "slides")
