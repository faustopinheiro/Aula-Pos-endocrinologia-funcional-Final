"""Spec do deck 8.2. Gera 08-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "folha", "tipo": "frase", "fundo": "tinta", "eyebrow": "Semana um, semana dois, semana oito",
          "frase": "A folha sabe que dia é. Não sabe como está a panturrilha.",
          "apoio": "Na semana cinco, a corredora pode estar pronta desde a três, ou não conseguir vinte elevações de calcanhar numa perna só. Troca-se a folha de semanas por uma sequência de portas."})

p = [svg_abre(1664, 300, "Cinco fases em escada, da proteção ao retorno, com uma porta entre cada fase")]
cores = [FOSF, GLIC, OXID, AZUL, TINTA]
for i, c in enumerate(cores):
    x = 20 + i * 330; y = 230 - i * 45
    p.append(f'<rect x="{x}" y="{y}" width="290" height="{300 - y}" rx="8" fill="{c}" fill-opacity="0.16"/>')
    p.append(f'<rect x="{x}" y="{y}" width="290" height="8" rx="4" fill="{c}"/>')
    if i < 4:
        p.append(f'<rect x="{x + 300}" y="{y - 70}" width="20" height="{300 - y + 70}" rx="4" fill="{MUDO}" fill-opacity="0.55"/>')
p.append("</svg>")
nomes = ["proteger e acalmar", "movimento e ativação", "força e capacidade", "potência, velocidade e gesto", "voltar: treino, jogo, nível"]
rs = [rot(30 + i * 330, 245 - i * 45, n, w=270, tam=24, cor=[FOSF, GLIC, OXID, AZUL, TINTA][i], peso=700) for i, n in enumerate(nomes)]
S.append({"id": "escada", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os nomes mudam de livro para livro", "titulo": "Cinco fases, quatro portas",
          "destaque": "A fase de força é a mais longa e a mais negligenciada. E nenhuma porta abre pelo calendário.",
          "destaque_cor": "tinta"})

S.append({"id": "piso", "tipo": "duas", "eyebrow": "Tempo e critério não são rivais", "titulo": "O tempo é o piso; o critério é a porta",
          "esq": {"t": "Tempo biológico", "cor": "ambar",
                  "itens": ["enxerto, osso, tendão não se apressam", "abaixo do piso, nenhum teste autoriza carga alta", "erro: “já passaram seis semanas, então pode”"]},
          "dir": {"t": "Critério funcional", "cor": "petr",
                  "itens": ["o que a pessoa consegue fazer, com qualidade", "sem dor que dure até o dia seguinte", "erro: teste ótimo antes do tempo biológico"]},
          "destaque": "Faltou um dos dois, a porta fica fechada.",
          "destaque_cor": "verm"})

S.append({"id": "resposta", "tipo": "cards", "por_linha": 4, "eyebrow": "O sinal que decide todas as portas", "titulo": "A resposta de 24 horas",
          "cards": [{"t": "Dor", "x": "voltou ao nível de antes até a manhã seguinte?", "cor": "petr"},
                    {"t": "Rigidez", "x": "a da manhã está igual ou pior?", "cor": "petr"},
                    {"t": "Inchaço", "x": "apareceu onde não havia?", "cor": "petr"},
                    {"t": "Função", "x": "consegue fazer o que fazia ontem?", "cor": "petr"}],
          "destaque": "Uma resposta pior e a carga de ontem passou do ponto, mesmo com a sessão sem dor. A própria pessoa aprende a ler e manda por mensagem.",
          "destaque_cor": "tinta", "fonte": "Mesma lógica da régua de dor · Am J Sports Med 2007"})

S.append({"id": "saidas", "tipo": "cards", "por_linha": 3, "eyebrow": "Em cada porta", "titulo": "Três saídas defensáveis",
          "cards": [{"t": "Avançar", "x": "critérios cumpridos, piso passado, resposta boa por algumas sessões seguidas", "cor": "petr"},
                    {"t": "Segurar", "x": "parte cumprida, ou resposta que oscila: mais carga dentro da mesma fase", "cor": "ambar"},
                    {"t": "Recuar", "x": "resposta pior de forma clara, inchaço novo, função caindo: um degrau, por poucos dias", "cor": "verm"}],
          "destaque": "A decisão vale até a próxima avaliação. Quem recuou na quarta pode avançar na segunda.",
          "destaque_cor": "tinta"})

S.append({"id": "portas", "tipo": "tabela", "eyebrow": "Vale para quase qualquer lesão", "titulo": "O que cada porta pede",
          "cab": ["Porta", "Critério funcional"],
          "larguras": [30, 70],
          "linhas": [["Proteção → movimento", "dor em repouso controlada, inchaço estável, dia a dia sem piora no dia seguinte"],
                     ["Movimento → força", "amplitude perto do lado bom, marcha sem mancar, contração sem inibição"],
                     ["Força → potência", "força perto do outro lado nos testes combinados, aguentando volume"],
                     ["Potência → retorno", "saltos, acelerações e mudanças de direção na intensidade do esporte, sem apreensão"]],
          "destaque": "Os números mudam por tecido e por esporte. A lógica da tabela não muda.",
          "destaque_cor": "tinta"})

S.append({"id": "custo", "tipo": "frase", "fundo": "tinta", "eyebrow": "Os dois erros têm custo",
          "frase": "Avançar cedo demais custa uma recidiva. Segurar tempo demais custa uma temporada.",
          "apoio": "E custa a paciência de quem volta por conta própria, sem critério nenhum. O critério existe para que a decisão não dependa do medo de quem decide."})

S.append({"id": "naoabre", "tipo": "cards", "por_linha": 3, "eyebrow": "Abrem porta com frequência", "titulo": "Três coisas que não deveriam abrir",
          "cards": [{"t": "“Estou ótima”", "x": "a dor some antes de a capacidade voltar", "cor": "verm"},
                    {"t": "“Semana seis”", "x": "o protocolo diz o piso, quando diz alguma coisa", "cor": "verm"},
                    {"t": "“Precisamos dela no sábado”", "x": "entra na aceitação de risco, não na avaliação do tecido", "cor": "verm"}],
          "destaque": "Misturar pressão com avaliação é o jeito mais comum de liberar quem não passou na porta.",
          "destaque_cor": "tinta"})

S.append({"id": "degraus", "tipo": "lista", "eyebrow": "A última fase não é um dia", "titulo": "Três degraus depois da última porta",
          "itens": [{"t": "Participar", "x": "treina de forma modificada ou restrita: corre com o grupo, sem os tiros", "cor": "ambar"},
                    {"t": "Voltar ao esporte", "x": "compete, ainda sem o nível de antes: prova curta sem objetivo de tempo", "cor": "petr"},
                    {"t": "Voltar ao desempenho", "x": "no nível de antes ou acima: o ritmo que tinha", "cor": "tinta"}],
          "destaque": "É aqui que a reabilitação sai da sala e a preparação física passa a conduzir junto.",
          "destaque_cor": "tinta", "fonte": "Consenso de Berna, Br J Sports Med 2016"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem abre cada porta", "titulo": "Condução e decisão, fase a fase",
          "cab": ["Fases", "Quem conduz e decide"],
          "larguras": [34, 66],
          "linhas": [["Proteção, movimento, força", "fisioterapia; médico quando o tecido é de risco"],
                     ["Potência e gesto", "fisioterapia e preparação física, juntas"],
                     ["Retorno", "decisão compartilhada, com o atleta"],
                     ["Todas", "alguém avisa o treinador em que porta o atleta está"]],
          "destaque": "A informação que mais falta: o técnico põe o atleta na finalização porque “ele já está treinando”.",
          "destaque_cor": "verm"})

S.append({"id": "ficha", "tipo": "duas", "eyebrow": "O que substitui a folha de semanas", "titulo": "Uma ficha de uma página",
          "esq": {"t": "Na ficha", "cor": "petr",
                  "itens": ["a fase atual", "os critérios da próxima porta", "cumpridos e pendentes", "a resposta de 24 horas das últimas sessões"]},
          "dir": {"t": "O que ela resolve", "cor": "tinta",
                  "itens": ["a pessoa conquista, não conta dias", "a equipe fala a mesma língua", "avançar deixa de ser opinião do dia"]},
          "destaque": "O prazo existe, como faixa: “depende de você passar nas portas, não do calendário”.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fases da reabilitação", "titulo": "A reabilitação é uma sequência de portas",
          "regras": ["O tempo é o piso; o critério é a porta",
                     "A resposta de 24 horas decide o dia a dia",
                     "Em cada porta: avançar, segurar ou recuar"],
          "cards": [{"t": "Fisioterapia", "x": "Conduz e abre as primeiras portas."},
                    {"t": "Preparação física", "x": "Entra na potência e no gesto."},
                    {"t": "Toda a equipe", "x": "Sabe em que porta o atleta está."}],
          "quem": "Próxima aula: mecanotransdução, a biologia por trás de cada porta."})

spec = {"arquivo": "aulas/MOD08/08-02-fases-da-reabilitacao-e-criterios-de-passagem.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Fases da reabilitação", "subtitulo": "Avançar, segurar ou recuar em cada porta",
        "nota_capa": "Entra pela folha de oito semanas de uma corredora.",
        "secoes": {"folha": ["A folha de semanas e as cinco fases.", "capa"],
                   "resposta": ["O sinal de 24 horas e as três saídas.", "resposta"],
                   "custo": ["Os dois erros e o que não abre porta.", "custo"],
                   "degraus": ["O retorno, quem decide e a ficha.", "degraus"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-02.json"), "w"), ensure_ascii=False, indent=1)
print("08-02.json:", len(S), "slides")
