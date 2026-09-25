"""Spec do deck 8.5. Gera 08-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "caso", "tipo": "frase", "fundo": "tinta", "eyebrow": "Caso ilustrativo · jogadora de handebol, na casa dos vinte",
          "frase": "“Quando eu volto?” A resposta é um plano, não uma data.",
          "apoio": "Aterrissagem depois do arremesso, joelho para dentro, estalo, inchaço em horas. Ruptura do cruzado anterior; reconstrução decidida com o cirurgião. O objeto da aula é o percurso, não o desfecho."})

S.append({"id": "expectativa", "tipo": "numeros", "eyebrow": "A conversa do primeiro mês", "titulo": "Voltar ao nível de antes não é automático",
          "numeros": [{"n": "81%", "x": "voltam a algum esporte", "cor": "petr"},
                      {"n": "65%", "x": "ao nível de antes da lesão", "cor": "ambar"},
                      {"n": "55%", "x": "ao esporte competitivo", "cor": "verm"}],
          "destaque": "Com os números de Delaware e Oslo do módulo de lesões: nove meses é o horizonte, e o critério decide se nove meses bastam.",
          "destaque_cor": "tinta", "fonte": "Metanálise, Br J Sports Med 2014"})

p = [svg_abre(1664, 260, "Linha do tempo de zero a nove meses ou mais, com cinco fases e quatro portas entre elas")]
M = lambda m: 40 + m / 10 * 1580
fases = [(0, 1.3, FOSF), (1.3, 3, GLIC), (3, 5.5, OXID), (5.5, 8.5, AZUL), (8.5, 10, TINTA)]
for a, b, c in fases:
    p.append(f'<rect x="{M(a):.0f}" y="90" width="{M(b) - M(a) - 6:.0f}" height="70" rx="8" fill="{c}" fill-opacity="0.8"/>')
for a, b, c in fases[1:]:
    p.append(f'<rect x="{M(a) - 8:.0f}" y="70" width="10" height="110" rx="3" fill="{TINTA}"/>')
for m in range(0, 11):
    p.append(f'<line x1="{M(m):.0f}" y1="190" x2="{M(m):.0f}" y2="200" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
nomes = ["proteger", "movimento e quadríceps", "força", "potência, corrida, campo", "voltar"]
rs = [rot(M(a) + 8, 20, n, w=M(b) - M(a) - 14, tam=22, cor=c, peso=700) for (a, b, c), n in zip(fases, nomes)] + \
     [rot(M(m) - 40, 206, f"{m}", w=80, tam=20, cor=MUDO, alinha="center") for m in (0, 3, 6, 9)] + \
     [rot(M(9.5) - 90, 206, "meses", w=180, tam=20, cor=MUDO, alinha="center")]
S.append({"id": "mapa", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mapa do percurso", "titulo": "Cinco fases com o tempo do cruzado",
          "destaque": "O enxerto marca o piso; o critério abre cada porta. E o caminho não é reto: o plano já prevê as semanas ruins.",
          "destaque_cor": "tinta", "fonte": "Esquema; faixas aproximadas, as portas abrem por critério"})

S.append({"id": "antes", "tipo": "numeros", "eyebrow": "Quando há tempo antes da cirurgia", "titulo": "A reabilitação começa antes dela",
          "numeros": [{"n": "72%", "x": "voltaram ao esporte de antes, com reabilitação estendida antes da cirurgia", "cor": "petr"},
                      {"n": "63%", "x": "sem ela; dois anos depois", "cor": "ambar"}],
          "destaque": "Joelho calmo, extensão completa, quadríceps ativo. Comparação entre coortes, não ensaio sorteado; a direção é consistente.",
          "destaque_cor": "tinta", "fonte": "192 contra 1.995 pacientes · Am J Sports Med 2016"})

S.append({"id": "semanas", "tipo": "cards", "por_linha": 3, "eyebrow": "Primeiras semanas depois da cirurgia", "titulo": "Três prioridades, nesta ordem",
          "cards": [{"t": "Extensão completa", "x": "perdida agora, é difícil de recuperar e muda a marcha por meses", "cor": "verm"},
                    {"t": "Derrame sob controle", "x": "o joelho cheio desliga o quadríceps; medido toda sessão", "cor": "ambar"},
                    {"t": "Quadríceps ligado", "x": "contração voluntária e perna estendida sem o joelho dobrar", "cor": "petr"}],
          "destaque": "A porta: extensão completa, derrame mínimo e estável, marcha sem muletas e sem mancar. Não é “semana seis”.",
          "destaque_cor": "tinta"})

S.append({"id": "forca", "tipo": "duas", "eyebrow": "A fase mais longa: o quadríceps é o eixo", "titulo": "Duas discussões antigas",
          "esq": {"t": "Cadeira extensora pode?", "cor": "petr",
                  "itens": ["cadeia aberta e fechada: sem diferença na frouxidão do joelho", "entra, com amplitude e carga combinadas"]},
          "dir": {"t": "Eletroestimulação ajuda?", "cor": "petr",
                  "itens": ["somada à fisioterapia, aumenta a força do quadríceps", "soma ao treino, não o substitui"]},
          "destaque": "Força de verdade pede carga alta, por meses. Faixa elástica para sempre não reconstrói um quadríceps.",
          "destaque_cor": "tinta", "fonte": "J Orthop Sports Phys Ther 2018 · Knee Surg Sports Traumatol Arthrosc 2018"})

S.append({"id": "corrida", "tipo": "numeros", "eyebrow": "A primeira porta que a atleta sente como vitória", "titulo": "Voltar a correr: o tempo quase sempre sozinho",
          "numeros": [{"n": "12 sem", "x": "mediana de liberação da corrida em 201 estudos", "cor": "ambar"},
                      {"n": "< 1 em 5", "x": "usou algum critério além do tempo", "cor": "verm"}],
          "destaque": "A porta dela: sem derrame, amplitude completa, força do quadríceps combinada, saltitar e aterrissar sem dor e sem o joelho ir para dentro.",
          "destaque_cor": "tinta", "fonte": "Revisão de mapeamento, Br J Sports Med 2018"})

p = [svg_abre(1664, 240, "Faixa do controlado ao caótico em cinco etapas: exercício previsto, gesto sem oponente, gesto com oponente e reação, treino coletivo, jogo")]
etapas = ["exercício previsto", "gesto sem oponente", "com oponente e reação", "treino coletivo", "jogo"]
cores = [OXID, OXID, GLIC, GLIC, FOSF]
for i in range(5):
    x = 20 + i * 330
    p.append(f'<rect x="{x}" y="80" width="300" height="70" rx="10" fill="{cores[i]}" fill-opacity="{0.35 + i * 0.13:.2f}"/>')
p.append(f'<line x1="20" y1="200" x2="1620" y2="200" stroke="{MUDO}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(30 + i * 330, 96, e, w=280, tam=24, cor=TINTA, peso=700, alinha="center") for i, e in enumerate(etapas)] + \
     [rot(20, 208, "controlado", w=300, tam=22, cor=MUDO), rot(1320, 208, "caótico", w=300, tam=22, cor=MUDO, alinha="right")]
S.append({"id": "campo", "tipo": "diagrama", "h": 240, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A fase que mais decide e a que mais se encurta", "titulo": "Do controlado ao caótico",
          "destaque": "Potência, qualidade de movimento, fadiga e o gesto do esporte. A lesão foi numa aterrissagem depois do arremesso: o retorno passa por esse gesto, cansada, muitas vezes.",
          "destaque_cor": "tinta", "fonte": "Sports Med 2019"})

S.append({"id": "relogios", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia do caso",
          "frase": "O relógio do enxerto e o relógio do quadríceps não andam juntos.",
          "apoio": "Pronta no sexto mês com o quadríceps fraco; quadríceps excelente no sétimo com o enxerto no meio do caminho. A decisão é tempo e critério."})

S.append({"id": "ultima", "tipo": "cards", "por_linha": 3, "eyebrow": "Perto do nono mês", "titulo": "A última porta tem três partes",
          "cards": [{"t": "Testes de retorno", "x": "força, saltos e a armadilha do índice de simetria", "cor": "petr"},
                    {"t": "Prontidão psicológica", "x": "o medo de nova lesão não aparece no dinamômetro", "cor": "ambar"},
                    {"t": "Decisão compartilhada", "x": "avaliar o risco é uma coisa; aceitá-lo é outra", "cor": "tinta"}],
          "destaque": "Cada parte ganha uma aula adiante. A porta está no plano desde o primeiro dia; ninguém é surpreendido no oitavo mês.",
          "destaque_cor": "tinta"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Nove meses, muitas mãos", "titulo": "Quem faz o quê",
          "cab": ["Quem", "O que faz no percurso"],
          "larguras": [28, 72],
          "linhas": [["Cirurgião", "técnica, enxerto, restrições iniciais, portas em que o tecido é o limite"],
                     ["Fisioterapia", "conduz do começo ao fim; mede derrame, amplitude e força; escreve as portas"],
                     ["Preparação física", "corrida, fase de campo, gesto e condicionamento"],
                     ["Psicologia e nutrição", "o medo perto do retorno; a matéria-prima de meses de força"],
                     ["Treinador, atleta, família", "a porta de cada mês; a expectativa honesta desde o começo"]],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Caso ilustrativo · o plano", "titulo": "Cada passo tem uma porta, um responsável e um motivo",
          "regras": ["Expectativa honesta no primeiro mês",
                     "Extensão, derrame e quadríceps; depois meses de força",
                     "Corrida e campo por critério; a última porta no plano desde o início"],
          "cards": [{"t": "Cirurgião e fisioterapia", "x": "O tecido e as portas."},
                    {"t": "Preparação física", "x": "A corrida, o campo e o gesto."},
                    {"t": "Psicologia, nutrição, família", "x": "O medo, a matéria-prima, a paciência."}],
          "quem": "Próxima aula: posterior da coxa e virilha."})

spec = {"arquivo": "aulas/MOD08/08-05-reabilitacao-do-lca.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Reabilitação do cruzado anterior", "subtitulo": "Nove meses de portas num caso ilustrativo",
        "nota_capa": "Caso ilustrativo: jogadora de handebol na casa dos vinte anos.",
        "secoes": {"caso": ["O caso, a expectativa e o mapa.", "capa"],
                   "antes": ["Antes da cirurgia e as primeiras semanas.", "antes"],
                   "forca": ["Força, corrida e campo.", "forca"],
                   "relogios": ["Os dois relógios, a última porta e quem faz o quê.", "relogios"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-05.json"), "w"), ensure_ascii=False, indent=1)
print("08-05.json:", len(S), "slides")
