"""Spec do deck 9.2. Gera 09-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "pedidos", "tipo": "frase", "fundo": "tinta", "eyebrow": "Três pedidos na mesma semana",
          "frase": "Os três pedem “uma periodização”. Precisam de coisas diferentes.",
          "apoio": "Uma nadadora master com um único campeonato em outubro. Um time de vôlei que joga todo sábado por oito meses. Um representante comercial que corre e passa metade da semana na estrada."})

# três mini-gráficos esquemáticos
p = [svg_abre(1664, 330, "Três esquemas: linear, ondulatório e em blocos")]
def moldura(x0):
    p.append(f'<line x1="{x0}" y1="280" x2="{x0 + 460}" y2="280" stroke="{GRADE}" stroke-width="3"/>')
# linear
x0 = 40; moldura(x0)
p.append(f'<path d="M {x0} 80 L {x0 + 460} 250" stroke="{OXID}" stroke-width="6" fill="none"/>')
p.append(f'<path d="M {x0} 250 L {x0 + 460} 80" stroke="{FOSF}" stroke-width="6" fill="none"/>')
# ondulatório
x0 = 600; moldura(x0)
pts = " ".join(f"{x0 + i * 46},{[120, 230, 170][i % 3]}" for i in range(11))
p.append(f'<polyline points="{pts}" stroke="{FOSF}" stroke-width="6" fill="none"/>')
# blocos
x0 = 1160; moldura(x0)
for i, (c, h) in enumerate([(OXID, 150), (GLIC, 180), (FOSF, 210)]):
    p.append(f'<rect x="{x0 + i * 155}" y="{280 - h}" width="145" height="{h}" rx="6" fill="{c}" fill-opacity="0.3"/>')
    p.append(f'<rect x="{x0 + i * 155}" y="{280 - h}" width="145" height="7" rx="3" fill="{c}"/>')
p.append("</svg>")
rs = [rot(40, 10, "Linear", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(600, 10, "Ondulatório", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(1160, 10, "Em blocos", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(40, 48, "volume", w=150, tam=20, cor=OXID, peso=700),
      rot(330, 48, "intensidade", w=170, tam=20, cor=FOSF, peso=700, alinha="right"),
      rot(40, 292, "semanas até o alvo", w=460, tam=20, cor=MUDO, alinha="center"),
      rot(600, 292, "variação dentro da semana", w=460, tam=20, cor=MUDO, alinha="center"),
      rot(1160, 292, "uma capacidade por bloco", w=460, tam=20, cor=MUDO, alinha="center")]
S.append({"id": "modelos", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Os três modelos", "titulo": "Uma frase para cada um",
          "destaque": "Em blocos: a sequência aposta que o ganho de um bloco ainda esteja presente quando o seguinte começa.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · revisão de blocos, Sports Med 2010"})

S.append({"id": "funciona", "tipo": "numeros", "eyebrow": "Periodizar funciona?", "titulo": "Funciona, por pouco",
          "numeros": [{"n": "18", "x": "estudos comparando força periodizada e não periodizada", "cor": "tinta"},
                      {"n": "0,43 → 0,23", "x": "tamanho de efeito, antes e depois do ajuste para viés de publicação", "cor": "ambar"}],
          "destaque": "Ondulatório um pouco à frente. Ganhos maiores em quem não era treinado: no começo, quase qualquer progressão funciona.",
          "destaque_cor": "tinta", "fonte": "Metanálise, Sports Med 2017"})

S.append({"id": "igualado", "tipo": "tabela", "eyebrow": "Com o volume igualado", "titulo": "Força responde ao modelo; hipertrofia, ao volume",
          "cab": ["Comparação", "Força", "Hipertrofia"],
          "larguras": [40, 30, 30],
          "linhas": [["Periodizado × não periodizado", "periodizado maior", "igual"],
                     ["Ondulatório × linear", "ondulatório maior, sobretudo em treinados", "igual"]],
          "destaque": "Para massa muscular, o modelo importa pouco. O que importa é o volume.",
          "destaque_cor": "tinta", "fonte": "Metanálise, Sports Med 2022"})

S.append({"id": "acontece", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O melhor modelo é o que acontece.",
          "apoio": "Boa parte dos modelos vem da tradição, e a diferença entre eles é pequena. Menor que a diferença entre fazer e não fazer as sessões."})

S.append({"id": "picos", "tipo": "duas", "eyebrow": "Pergunta um", "titulo": "Quantos momentos de pico existem?",
          "esq": {"t": "Um pico", "cor": "petr",
                  "itens": ["a nadadora e o campeonato de outubro", "sequência linear ou em blocos", "termina com polimento antes da prova"]},
          "dir": {"t": "Um pico por semana", "cor": "ambar",
                  "itens": ["o vôlei e seus sábados", "ondulatório dentro da semana", "manutenção de força ao longo da temporada"]},
          "destaque": "Com trinta e poucos picos, não existe caminhar para um momento.",
          "destaque_cor": "tinta"})

S.append({"id": "sessoes", "tipo": "cards", "por_linha": 3, "eyebrow": "Pergunta dois", "titulo": "Quantas sessões acontecem de verdade?",
          "cards": [{"t": "A literatura clássica", "x": "atletas com dez a catorze sessões por semana", "cor": "tinta"},
                    {"t": "O representante", "x": "quatro sessões; duas nas semanas de viagem", "cor": "ambar"},
                    {"t": "A unidade muda", "x": "sai o macrociclo, entra a semana que se repete por três a seis semanas", "cor": "petr"}],
          "destaque": "Cada sessão precisa se justificar numa frase. Sem a frase, é enfeite.",
          "destaque_cor": "tinta"})

S.append({"id": "objetivo", "tipo": "tabela", "eyebrow": "Pergunta três", "titulo": "Qual o objetivo, e há quanto tempo treina?",
          "cab": ["Quem", "O que decide"],
          "larguras": [34, 66],
          "linhas": [["Iniciante", "qualquer progressão bem feita; aprender e aparecer"],
                     ["Treinado buscando força", "variar a intensidade ao longo da semana"],
                     ["Hipertrofia", "o volume; o modelo fica em segundo plano"],
                     ["Endurance", "a distribuição de intensidade na semana"]]})

S.append({"id": "minima", "tipo": "duas", "eyebrow": "O detalhe que salva o plano", "titulo": "Semana cheia e semana mínima, escritas desde o primeiro dia",
          "esq": {"t": "Semana cheia", "cor": "petr",
                  "itens": ["as quatro sessões", "progressão pequena", "revisão a cada três a seis semanas"]},
          "dir": {"t": "Semana mínima", "cor": "ambar",
                  "itens": ["duas sessões", "começa pelo mais difícil de recuperar: a força", "não conta como falha, não exige recomeço"]},
          "destaque": "Sem versão mínima, a semana ruim tem zero sessões: “não deu para fazer direito” vira “não deu para fazer”.",
          "destaque_cor": "tinta"})

S.append({"id": "aplicado", "tipo": "tabela", "eyebrow": "As três perguntas aplicadas", "titulo": "Três pedidos, três escolhas",
          "cab": ["Pedido", "Picos · sessões · objetivo", "Escolha"],
          "larguras": [22, 36, 42],
          "linhas": [["Nadadora master", "um · quatro a cinco · desempenho", "linear ou blocos até outubro, polimento no fim"],
                     ["Time de vôlei", "um por semana · muitas · jogo de sábado", "ondulatório, sessão pesada longe do jogo, manutenção"],
                     ["Representante", "a prova · quatro que viram duas · meia maratona", "semana que se repete, cheia e mínima"]]})

S.append({"id": "sinais", "tipo": "cards", "por_linha": 3, "eyebrow": "Quando não está funcionando", "titulo": "Três sinais, em qualquer modelo",
          "cards": [{"t": "As sessões não acontecem", "x": "o plano pede mais do que a vida comporta", "cor": "verm"},
                    {"t": "A carga não sobe", "x": "falta sobrecarga, não falta modelo", "cor": "ambar"},
                    {"t": "O dia seguinte piora", "x": "sono, dor, rendimento: a carga passou da recuperação", "cor": "verm"}],
          "destaque": "O terceiro sinal é o assunto das aulas de monitoramento deste módulo.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Modelos de periodização", "titulo": "Nenhum vencedor absoluto; três perguntas para escolher",
          "regras": ["Quantos picos existem?",
                     "Quantas sessões acontecem de verdade?",
                     "Qual o objetivo, e há quanto tempo treina?"],
          "cards": [{"t": "Preparação física", "x": "Escolhe o modelo e escreve as duas semanas."},
                    {"t": "Técnico", "x": "Diz onde estão os picos e o que o jogo exige."},
                    {"t": "Atleta", "x": "Diz quantas sessões a vida comporta."}],
          "quem": "Próxima aula: treino de força por objetivo."})

spec = {"arquivo": "aulas/MOD09/09-02-modelos-de-periodizacao.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Modelos de periodização", "subtitulo": "Linear, ondulatório e em blocos, e como escolher",
        "nota_capa": "Entra por três pedidos diferentes chegando na mesma semana.",
        "secoes": {"pedidos": ["Os pedidos e os três modelos.", "capa"],
                   "funciona": ["O que as metanálises mostram.", "funciona"],
                   "picos": ["As três perguntas.", "picos"],
                   "aplicado": ["A escolha e os sinais de alerta.", "aplicado"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-02.json"), "w"), ensure_ascii=False, indent=1)
print("09-02.json:", len(S), "slides")
