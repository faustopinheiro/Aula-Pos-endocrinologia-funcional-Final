"""Spec do deck 9.8. Gera 09-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "propostas", "tipo": "frase", "fundo": "tinta", "eyebrow": "Três propostas, um orçamento",
          "frase": "Cintas cardíacas, um aplicativo de variabilidade, ou uma folha com quatro perguntas?",
          "apoio": "O técnico de uma equipe universitária de handebol precisa escolher como monitorar a carga das dezoito atletas. A resposta não é o mais sofisticado. É o que muda uma decisão."})

S.append({"id": "quatro", "tipo": "cards", "por_linha": 2, "eyebrow": "A carga vista de dentro", "titulo": "Quatro ferramentas, cada uma com um ponto cego",
          "cards": [{"t": "Percepção de esforço da sessão", "x": "nota de 0 a 10 vezes os minutos", "cor": "petr"},
                    {"t": "Frequência cardíaca", "x": "durante o treino", "cor": "ambar"},
                    {"t": "Variabilidade da frequência cardíaca", "x": "em repouso, de manhã", "cor": "tinta"},
                    {"t": "Questionários curtos", "x": "sono, dor, cansaço, estresse, humor", "cor": "verm"}]})

S.append({"id": "conta", "tipo": "numeros", "eyebrow": "A mais barata", "titulo": "Percepção de esforço da sessão",
          "numeros": [{"n": "70 × 7 = 490", "x": "minutos vezes a nota: unidades de carga", "cor": "tinta"},
                      {"n": "40 × 4 = 160", "x": "sessões diferentes no mesmo denominador", "cor": "petr"}],
          "destaque": "Validada contra um padrão de frequência cardíaca em exercício contínuo, intervalado e basquete. A mesma pergunta soma quadra, musculação e jogo.",
          "destaque_cor": "tinta", "fonte": "J Strength Cond Res 2001 · revisão, Front Neurosci 2017"})

S.append({"id": "condicoes", "tipo": "cards", "por_linha": 2, "eyebrow": "Sem isso, vira ruído", "titulo": "Quatro condições para a nota valer",
          "cards": [{"t": "Escala com âncoras", "x": "de 0 a 10, as mesmas palavras, ensinadas uma vez com calma", "cor": "petr"},
                    {"t": "Cerca de 30 minutos depois", "x": "no fim do treino, a nota reflete só o último tiro", "cor": "ambar"},
                    {"t": "Sem plateia", "x": "em voz alta no grupo mede hierarquia; por mensagem, individual", "cor": "ambar"},
                    {"t": "Nunca para punir", "x": "nota alta que vira sermão deixa de ser honesta", "cor": "verm"}]})

# planejado x relatado
sess = [("seg", 5, 5), ("ter", 5, 8), ("qua", 3, 3), ("qui", 5, 8), ("sex", 5, 8)]
p = [svg_abre(1664, 320, "Carga planejada e relatada por sessão; três sessões planejadas como 5 voltaram como 8")]
base = 280
for i, (d, pl, rl) in enumerate(sess):
    x = 120 + i * 300
    p.append(f'<rect x="{x}" y="{base - pl * 28}" width="90" height="{pl * 28}" rx="4" fill="{GRADE}"/>')
    p.append(f'<rect x="{x + 100}" y="{base - rl * 28}" width="90" height="{rl * 28}" rx="4" fill="{FOSF if rl > pl else OXID}"/>')
p.append(f'<line x1="80" y1="{base}" x2="1600" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = []
for i, (d, pl, rl) in enumerate(sess):
    x = 120 + i * 300
    rs.append(rot(x, base + 10, d, w=190, tam=22, cor=MUDO, alinha="center"))
    rs.append(rot(x, base - pl * 28 - 34, str(pl), w=90, tam=24, cor=MUDO, peso=700, alinha="center"))
    rs.append(rot(x + 100, base - rl * 28 - 34, str(rl), w=90, tam=24, cor=TINTA, peso=700, alinha="center"))
rs.append(rot(80, 10, "cinza: planejado · cor: relatado", w=420, tam=20, cor=MUDO))
S.append({"id": "planejado", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O uso mais valioso", "titulo": "Planejado contra o que aconteceu",
          "destaque": "Um cinco que virou oito uma vez é ruído. Três vezes na semana é a conversa: sono, comida, prova, dor.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "fc", "tipo": "duas", "eyebrow": "Frequência cardíaca", "titulo": "Boa no contínuo, fraca no resto",
          "esq": {"t": "Funciona", "cor": "petr",
                  "itens": ["esforço aeróbio contínuo", "complemento objetivo à nota", "de graça para quem já usa relógio"]},
          "dir": {"t": "Falha", "cor": "verm",
                  "itens": ["atrasa nos esforços curtos", "responde mal ao treino de força", "subestima sprints, saltos e contato"]},
          "destaque": "Para uma equipe de handebol: um aparelho por atleta, bateria, dados e alguém para olhar. Caro para o que entrega.",
          "destaque_cor": "tinta"})

S.append({"id": "vfc", "tipo": "duas", "eyebrow": "Variabilidade da frequência cardíaca", "titulo": "Exigente, e com um efeito colateral",
          "esq": {"t": "Como usar bem", "cor": "petr",
                  "itens": ["mesma hora, mesma posição, ao acordar", "média de vários dias, não o número do dia", "a pessoa comparada com ela mesma"]},
          "dir": {"t": "O risco", "cor": "ambar",
                  "itens": ["decidir o dia pelo número da manhã", "ansiedade com o próprio dado", "descrito no sono como ortossonia"]},
          "destaque": "Número que gera ansiedade custa caro.",
          "destaque_cor": "tinta", "fonte": "Revisão, Sports Med 2013 · J Clin Sleep Med 2017"})

S.append({"id": "questionario", "tipo": "tabela", "eyebrow": "Questionários curtos", "titulo": "Trinta segundos de manhã",
          "cab": ["Pergunta", "Escala"],
          "larguras": [60, 40],
          "linhas": [["Como você dormiu?", "1 a 5"],
                     ["Dor muscular", "1 a 5"],
                     ["Cansaço", "1 a 5"],
                     ["Estresse", "1 a 5"],
                     ["Algum problema de saúde esta semana?", "semanal"]],
          "destaque": "Medidas relatadas pela atleta respondem à carga de forma sensível. O risco: perguntas demais, todo dia, sem retorno.",
          "destaque_cor": "tinta", "fonte": "Revisão sistemática, Br J Sports Med 2016 · formato de prática corrente"})

S.append({"id": "terceira", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O melhor instrumento é o que muda uma decisão, e que a atleta ainda responde na terceira semana.",
          "apoio": "Precisão que ninguém usa vale menos que uma pergunta simples que chega todo dia e que alguém lê."})

S.append({"id": "cenarios", "tipo": "tabela", "eyebrow": "Como escolher", "titulo": "Instrumento por cenário",
          "cab": ["Cenário", "Principal", "Complemento"],
          "larguras": [34, 32, 34],
          "linhas": [["Coletivo com pouco dinheiro", "nota da sessão", "quatro perguntas de bem-estar"],
                     ["Endurance com relógio", "nota da sessão e FC", "variabilidade, se tolerar, em média"],
                     ["Praticante de força", "nota da sessão", "registro de cargas"],
                     ["Ansioso com números", "nota da sessão", "uma conversa por semana"]]})

S.append({"id": "regras", "tipo": "cards", "por_linha": 2, "eyebrow": "Para qualquer instrumento", "titulo": "Quatro regras de uso",
          "cards": [{"t": "Contra ela mesma", "x": "há quem dê notas altas e quem dê baixas", "cor": "petr"},
                    {"t": "Tendência, não o dia", "x": "um ponto isolado é ruído", "cor": "petr"},
                    {"t": "Regra antes do dado", "x": "“se três sessões voltarem acima do planejado, reduzimos e conversamos”", "cor": "ambar"},
                    {"t": "Retorno a quem responde", "x": "quem nunca vê o uso da nota para de responder", "cor": "verm"}]})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Carga interna", "titulo": "Para o handebol: a folha, com uma regra de decisão",
          "regras": ["A nota da sessão é a mais barata e atravessa modalidades",
                     "FC no contínuo; variabilidade em média, se tolerar",
                     "Questionários curtos, com retorno"],
          "cards": [{"t": "Preparação física", "x": "Coleta, compara com o planejado e decide."},
                    {"t": "Médico e psicologia", "x": "Entram quando a nota sobe sem motivo de treino."},
                    {"t": "Atleta", "x": "Responde sozinha, meia hora depois."}],
          "quem": "Próxima aula: índices de carga aguda e crônica, uso, limitação e crítica."})

spec = {"arquivo": "aulas/MOD09/09-08-carga-interna-pse-fc-e-questionarios.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Carga interna", "subtitulo": "Percepção de esforço, frequência cardíaca, variabilidade e questionários, e como escolher",
        "nota_capa": "Entra por um técnico de handebol com três propostas e um orçamento.",
        "secoes": {"propostas": ["A pergunta e as quatro ferramentas.", "capa"],
                   "conta": ["A percepção de esforço da sessão.", "conta"],
                   "fc": ["Frequência cardíaca, variabilidade e questionários.", "fc"],
                   "cenarios": ["Como escolher e como usar.", "cenarios"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-08.json"), "w"), ensure_ascii=False, indent=1)
print("09-08.json:", len(S), "slides")
