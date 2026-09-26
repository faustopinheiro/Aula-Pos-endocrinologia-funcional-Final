"""Spec do deck 9.1. Gera 09-01.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "percurso", "tipo": "frase", "fundo": "tinta", "eyebrow": "Sessenta quilômetros, quatro vezes por semana",
          "frase": "Ele sabe os princípios de cor. Aplica ao contrário.",
          "apoio": "Um ciclista amador repete o mesmo percurso, na mesma média, há três anos. Nos outros dias, faz uma aula em que nenhum treino se repete, para o corpo “não se acostumar”."})

S.append({"id": "roteiro", "tipo": "tabela", "eyebrow": "Cinco princípios, cinco erros", "titulo": "O problema está na aplicação",
          "cab": ["Princípio", "O erro comum"],
          "larguras": [28, 72],
          "linhas": [["Especificidade", "reduzida a repetir o gesto do esporte"],
                     ["Sobrecarga", "reduzida a fazer sempre mais"],
                     ["Individualidade", "usada como desculpa: “eu não respondo a esse treino”"],
                     ["Variação", "transformada em objetivo, e não em ferramenta"],
                     ["Reversibilidade", "lembrada quando o atleta para, esquecida no planejamento"]],
          "destaque": "Quase ninguém erra por não conhecer os princípios.",
          "destaque_cor": "tinta"})

S.append({"id": "especificidade", "tipo": "duas", "eyebrow": "Erro um · especificidade", "titulo": "A resistência vale para o estímulo que a produziu",
          "esq": {"t": "O experimento clássico", "cor": "tinta",
                  "itens": ["o animal resistente ao frio", "não ficava resistente a outra agressão", "a adaptação era ao agente, não geral"]},
          "dir": {"t": "No treino", "cor": "petr",
                  "itens": ["o corpo se adapta ao estímulo, ao tecido, à velocidade e à amplitude", "o gesto é parte disso, não o todo", "o estímulo que o esporte exige e a pessoa ainda não tolera"]},
          "destaque": "O ciclista treina muito o gesto, sempre no mesmo estímulo.",
          "destaque_cor": "tinta", "fonte": "Selye, Nature 1936"})

# escada de sobrecarga x linha reta
p = [svg_abre(1664, 320, "Uma escada em que cada degrau muda uma variável, ao lado de uma linha reta sem degraus")]
base = 290
degraus = [(60, 230, OXID), (300, 180, OXID), (540, 130, GLIC), (780, 80, FOSF)]
for x, y, c in degraus:
    p.append(f'<rect x="{x}" y="{y}" width="230" height="{base - y}" rx="8" fill="{c}" fill-opacity="0.2"/>')
    p.append(f'<rect x="{x}" y="{y}" width="230" height="7" rx="3" fill="{c}"/>')
p.append(f'<line x1="1120" y1="200" x2="1600" y2="200" stroke="{MUDO}" stroke-width="7"/>')
p.append(f'<line x1="40" y1="{base}" x2="1620" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(60, 240, "base", w=230, tam=22, cor=MUDO, alinha="center"),
      rot(300, 190, "mais volume", w=230, tam=22, cor=OXID, peso=700, alinha="center"),
      rot(540, 140, "mais intensidade", w=230, tam=22, cor=GLIC, peso=700, alinha="center"),
      rot(780, 90, "mais densidade", w=230, tam=22, cor=FOSF, peso=700, alinha="center"),
      rot(1120, 130, "o mesmo estímulo há três anos", w=480, tam=24, cor=MUDO, peso=700, alinha="center"),
      rot(1120, 215, "cansa, mas não sobrecarrega", w=480, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "sobrecarga", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro dois · sobrecarga", "titulo": "Sobrecarga é estímulo acima do que já se tolera",
          "destaque": "Uma variável por vez, e a resposta do dia seguinte decide o próximo passo.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# barras reais de não respondedores
vals = [69, 40, 29, 0, 0]
p = [svg_abre(1664, 360, "Porcentagem de não respondedores por grupo: 69, 40, 29, 0 e 0 por cento")]
base, esc = 300, 3.4
for i, v in enumerate(vals):
    x = 120 + i * 300
    h = max(v * esc, 4)
    p.append(f'<rect x="{x}" y="{base - h}" width="160" height="{h}" rx="4" fill="{FOSF if v else GRADE}"/>')
p.append(f'<line x1="80" y1="{base}" x2="1600" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = []
for i, v in enumerate(vals):
    x = 120 + i * 300
    rs.append(rot(x, base - max(v * esc, 4) - 44, f"{v}%", w=160, tam=34, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x - 20, base + 14, f"{i + 1} sessão" if i == 0 else f"{i + 1} sessões", w=200, tam=22, cor=MUDO, alinha="center"))
S.append({"id": "respondedores", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro três · individualidade", "titulo": "Não responder caiu conforme a dose subiu",
          "destaque": "Seis semanas depois, com duas horas a mais por semana, todos os que não tinham respondido responderam.",
          "destaque_cor": "petr", "fonte": "78 adultos saudáveis, sessões de 60 min por semana · J Physiol 2017"})

S.append({"id": "dose", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Quase ninguém deixa de responder a tudo. Muita gente deixa de responder àquela dose.",
          "apoio": "Individualidade é ajustar dose, estímulo e tempo, e medir de novo. Antes de concluir que alguém não responde, perguntar se a dose era suficiente."})

S.append({"id": "variacao", "tipo": "duas", "eyebrow": "Erro quatro · variação", "titulo": "Se nada se repete, nada progride",
          "esq": {"t": "Pode ajudar", "cor": "petr",
                  "itens": ["variação planejada", "com motivo anatômico ou mecânico", "exercícios-base mantidos por semanas"]},
          "dir": {"t": "Pode atrapalhar", "cor": "verm",
                  "itens": ["trocar exercícios o tempo todo", "trocar por outros que dão o mesmo estímulo", "a tal “confusão muscular”"]},
          "destaque": "Não dá para saber se a carga subiu num exercício que aparece uma vez por mês.",
          "destaque_cor": "tinta", "fonte": "Revisão sistemática brasileira, 8 estudos · J Strength Cond Res 2022"})

S.append({"id": "reversibilidade", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro cinco · reversibilidade", "titulo": "Um princípio de planejamento, não de lamento",
          "cards": [{"t": "Férias e lesões", "x": "ninguém combina o mínimo que mantém alguma coisa", "cor": "ambar"},
                    {"t": "Treino concorrente", "x": "a força some no bloco de resistência, quando uma dose pequena manteria", "cor": "ambar"},
                    {"t": "O ciclista", "x": "nunca faz força fora da bicicleta e perde, ano a ano, a que tinha", "cor": "verm"}],
          "destaque": "Toda adaptação se perde quando o estímulo some. O erro é não planejar para isso.",
          "destaque_cor": "tinta"})

S.append({"id": "teoria", "tipo": "duas", "eyebrow": "Uma honestidade", "titulo": "Os princípios se sustentam; a teoria é mais fina",
          "esq": {"t": "Consistente nos estudos", "cor": "petr",
                  "itens": ["especificidade", "progressão", "recuperação e reversibilidade"]},
          "dir": {"t": "Mais fino do que se ensina", "cor": "ambar",
                  "itens": ["a base fisiológica tradicional do planejamento", "apoiada na síndrome geral de adaptação", "leitura que a pesquisa sobre estresse já abandonou"]},
          "destaque": "Planejar continua valendo. Muda a postura: menos confiança no modelo, mais no que se mede.",
          "destaque_cor": "tinta", "fonte": "“Periodization theory: confronting an inconvenient truth”, Sports Med 2018"})

S.append({"id": "perguntas", "tipo": "tabela", "eyebrow": "Princípio é pergunta", "titulo": "Cinco perguntas antes de montar a semana",
          "cab": ["Princípio", "A pergunta"],
          "larguras": [28, 72],
          "linhas": [["Especificidade", "que estímulo o esporte exige e a pessoa ainda não tolera?"],
                     ["Sobrecarga", "qual variável muda nesta semana, e só ela?"],
                     ["Individualidade", "a dose era suficiente antes de eu concluir que não funcionou?"],
                     ["Variação", "essa troca tem motivo, ou é só para não repetir?"],
                     ["Reversibilidade", "qual o mínimo que mantém o ganho quando a rotina quebrar?"]]})

S.append({"id": "ciclista", "tipo": "tabela", "eyebrow": "As perguntas aplicadas", "titulo": "A semana do ciclista, reorganizada",
          "cab": ["Antes", "Depois"],
          "larguras": [50, 50],
          "linhas": [["quatro saídas iguais, na mesma média", "uma com esforços mais intensos, uma mais longa, duas leves"],
                     ["aula que nunca se repete", "dois treinos de força com exercícios fixos por semanas"],
                     ["“não estou respondendo”", "resposta acompanhada, dose ajustada antes de concluir"],
                     ["nada combinado para as viagens", "um mínimo de manutenção acertado"]],
          "destaque": "Não é melhor por ser mais complexo. É melhor porque cada escolha responde a uma pergunta.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Princípios do treinamento", "titulo": "Princípio é pergunta, não é slogan",
          "regras": ["Especificidade é estímulo, não só gesto",
                     "Sobrecarga é uma variável por vez",
                     "Antes de “não respondedor”, conferir a dose"],
          "cards": [{"t": "Preparação física", "x": "Escolhe o estímulo e a variável da semana."},
                    {"t": "Médico e fisioterapia", "x": "Dizem o que o tecido ainda não tolera."},
                    {"t": "Atleta", "x": "Conta a resposta do dia seguinte."}],
          "quem": "Próxima aula: modelos de periodização."})

spec = {"arquivo": "aulas/MOD09/09-01-principios-do-treinamento.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Princípios do treinamento", "subtitulo": "Cinco erros na aplicação do que todos sabem de cor",
        "nota_capa": "Entra por um ciclista que repete o mesmo percurso há três anos.",
        "secoes": {"percurso": ["A cena e os cinco erros.", "capa"],
                   "respondedores": ["Individualidade e dose.", "respondedores"],
                   "variacao": ["Variação, reversibilidade e teoria.", "variacao"],
                   "perguntas": ["Os princípios como perguntas.", "perguntas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-01.json"), "w"), ensure_ascii=False, indent=1)
print("09-01.json:", len(S), "slides")
