"""Spec do deck 9.3. Gera 09-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "ficha", "tipo": "frase", "fundo": "tinta", "eyebrow": "Na academia",
          "frase": "“Quantas séries e quantas repetições?” depende de para quê.",
          "apoio": "O jovem que quer massa, a corredora, o jogador de basquete que quer saltar, a senhora de setenta anos e o paciente com diabetes fazem a mesma pergunta. “Três séries de dez” é resposta pior do que parece."})

S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "O roteiro", "titulo": "Cinco passos, nesta ordem",
          "itens": [{"t": "Objetivo", "x": "força máxima, hipertrofia, potência, saúde e função, ou outro esporte", "cor": "tinta"},
                    {"t": "Carga", "x": "a variável que mais separa força de hipertrofia", "cor": "verm"},
                    {"t": "Volume e frequência", "x": "quantas séries por músculo, distribuídas como", "cor": "ambar"},
                    {"t": "Esforço e intervalo", "x": "quanto perto da falha; quanto descanso entre séries", "cor": "petr"},
                    {"t": "Progressão e registro", "x": "sem ficha, não existe progressão", "cor": "tinta"}],
          "gap_itens": 10})

S.append({"id": "objetivo", "tipo": "tabela", "eyebrow": "Passo um", "titulo": "Cada objetivo tem uma variável que manda",
          "cab": ["Objetivo", "O que mais pesa"],
          "larguras": [30, 70],
          "linhas": [["Força máxima", "carga pesada, no próprio exercício que se quer melhorar"],
                     ["Hipertrofia", "volume e esforço perto da falha; a carga pode variar"],
                     ["Potência", "velocidade de execução, sobre uma base de força"],
                     ["Saúde e função", "regularidade, com exercícios que conversam com a vida real"],
                     ["Outro esporte", "o que o esporte exige e falta, sem roubar o treino principal"]],
          "destaque": "Nomear o objetivo com a pessoa evita o programa de fisiculturista para quem queria correr melhor.",
          "destaque_cor": "tinta"})

S.append({"id": "carga", "tipo": "duas", "eyebrow": "Passo dois · carga", "titulo": "Hipertrofia em toda a faixa; força com carga pesada",
          "esq": {"t": "Hipertrofia", "cor": "petr",
                  "itens": ["ganhos semelhantes com carga baixa e alta", "desde que as séries sejam levadas ao esforço alto", "saída para quem não tolera carga pesada"]},
          "dir": {"t": "Força máxima", "cor": "verm",
                  "itens": ["carga pesada ganhou", "quem quer ficar forte num levantamento", "precisa treinar pesado nele em algum momento"]},
          "destaque": "Carga baixa: até 60% do máximo. Carga alta: acima disso. Séries até a falha, pelo menos seis semanas.",
          "destaque_cor": "tinta", "fonte": "Metanálise, J Strength Cond Res 2017"})

S.append({"id": "crescer", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Para crescer, quase qualquer carga serve se o esforço for alto. Para ficar forte, precisa de carga pesada.",
          "apoio": "As duas metades resolvem boa parte das discussões de academia, e boa parte das prescrições para quem tem limitação."})

# barras reais de volume
vals = [(5.4, "menos de 5"), (6.6, "5 a 9"), (9.8, "10 ou mais")]
p = [svg_abre(1664, 360, "Ganho de massa muscular por faixa de séries semanais: 5,4, 6,6 e 9,8 por cento")]
base, esc = 300, 24
for i, (v, _) in enumerate(vals):
    x = 260 + i * 440
    p.append(f'<rect x="{x}" y="{base - v * esc}" width="220" height="{v * esc}" rx="4" fill="{[GRADE, GLIC, OXID][i]}"/>')
p.append(f'<line x1="180" y1="{base}" x2="1480" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = []
for i, (v, t) in enumerate(vals):
    x = 260 + i * 440
    rs.append(rot(x, base - v * esc - 48, f"{str(v).replace('.', ',')}%", w=220, tam=36, cor=TINTA, peso=700, alinha="center"))
    rs.append(rot(x - 40, base + 14, f"{t} séries por semana", w=300, tam=22, cor=MUDO, alinha="center"))
S.append({"id": "volume", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo três · volume", "titulo": "O volume é um dial, não um interruptor",
          "destaque": "Cerca de 0,37% a mais por série semanal adicionada. O teto da relação ficou em aberto.",
          "destaque_cor": "tinta", "fonte": "Ganho médio de massa muscular · 15 estudos, J Sports Sci 2017"})

S.append({"id": "frequencia", "tipo": "duas", "eyebrow": "Passo três · frequência", "titulo": "Com o mesmo volume, a frequência não muda a hipertrofia",
          "esq": {"t": "O que a metanálise encontrou", "cor": "tinta",
                  "itens": ["só estudos com volume semanal igual", "uma ou três vezes por semana: resultado semelhante", "a vantagem antiga vinha do volume maior"]},
          "dir": {"t": "Para que serve, então", "cor": "petr",
                  "itens": ["logística: distribuir o volume", "sessões que a pessoa faz bem", "três dias: corpo inteiro; cinco: dividir"]},
          "destaque": "A frequência distribui o volume; não o substitui.", "destaque_cor": "tinta", "fonte": "Metanálise, J Sports Sci 2019"})

S.append({"id": "esforco", "tipo": "cards", "por_linha": 2, "eyebrow": "Passo quatro", "titulo": "Esforço e intervalo",
          "cards": [{"t": "Perto da falha", "x": "hipertrofia aumenta quanto mais perto da falha; para força, relação desprezível", "cor": "verm"},
                    {"t": "Intervalo entre séries", "x": "pequeno benefício acima de 60 segundos; sem diferença apreciável acima de 90", "cor": "ambar"}],
          "destaque": "Esforço se mede em repetições de reserva: quantas ainda sobrariam. Para força máxima, intervalos mais longos.",
          "destaque_cor": "tinta", "fonte": "Metarregressões, Sports Med 2024 · metanálise, Front Sports Act Living 2024"})

S.append({"id": "ajustes", "tipo": "duas", "eyebrow": "Dois objetivos com ajustes próprios", "titulo": "Potência e o idoso",
          "esq": {"t": "Potência", "cor": "ambar",
                  "itens": ["quem é mais forte produz mais potência", "a base de força vem antes", "depois, cargas leves a moderadas na maior velocidade"]},
          "dir": {"t": "Idoso", "cor": "petr",
                  "itens": ["duas a três sessões por semana", "duas a três séries; no início, série única basta", "incluir potência, com segurança"]},
          "destaque": "O jogador que só salta e nunca fica mais forte bate num teto.",
          "destaque_cor": "tinta", "fonte": "Revisão de potência, Sports Med 2011 · posicionamento para idosos, J Strength Cond Res 2019"})

S.append({"id": "servico", "tipo": "duas", "eyebrow": "Força a serviço de outro objetivo", "titulo": "A corredora e o treino mínimo",
          "esq": {"t": "Atleta de resistência", "cor": "petr",
                  "itens": ["força pesada ou explosiva melhora a economia", "poucas séries, poucos exercícios", "longe dos treinos de qualidade"]},
          "dir": {"t": "Quem tem pouco tempo", "cor": "ambar",
                  "itens": ["exercícios multiarticulares", "membros inferiores, empurrar e puxar", "duas vezes por semana cabe na vida"]},
          "destaque": "O treino mínimo que acontece vence o completo que nunca acontece.",
          "destaque_cor": "tinta", "fonte": "Revisão, Scand J Med Sci Sports 2014 · revisão, Sports Med 2021"})

S.append({"id": "registro", "tipo": "tabela", "eyebrow": "Passo cinco", "titulo": "A ficha que transforma progressão em número",
          "cab": ["Coluna", "Para que serve"],
          "larguras": [26, 74],
          "linhas": [["Data", "mostra a frequência real e as semanas sem treino"],
                     ["Exercício", "o mesmo por semanas, para a carga poder subir"],
                     ["Carga", "a variável que se quer ver progredir"],
                     ["Repetições", "o que foi feito, não o que estava previsto"],
                     ["Reserva", "quantas repetições ainda sobrariam; decide a próxima carga"]],
          "destaque": "Terminou com mais reserva que o combinado: a carga sobe. Com menos: a carga fica.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Força por objetivo", "titulo": "Cinco pessoas, cinco programas, nenhum “três de dez” por padrão",
          "regras": ["Objetivo primeiro; carga pesada para força",
                     "Volume como dial; frequência como logística",
                     "Perto da falha para crescer; ficha para progredir"],
          "cards": [{"t": "Preparação física", "x": "Escolhe carga, volume e esforço por objetivo."},
                    {"t": "Médico e fisioterapia", "x": "Dizem o que a articulação e o tecido toleram."},
                    {"t": "Atleta", "x": "Anota a carga e a reserva de cada série."}],
          "quem": "Próxima aula: velocidade, aceleração e mudança de direção."})

spec = {"arquivo": "aulas/MOD09/09-03-treino-de-forca-por-objetivo.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Treino de força por objetivo", "subtitulo": "Carga, volume, esforço e intervalo para cada meta",
        "nota_capa": "Entra pela pergunta mais comum da academia.",
        "secoes": {"ficha": ["A pergunta, o roteiro e o objetivo.", "capa"],
                   "carga": ["Carga e volume.", "carga"],
                   "esforco": ["Esforço, intervalo e objetivos especiais.", "esforco"],
                   "registro": ["Registro e fecho.", "registro"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-03.json"), "w"), ensure_ascii=False, indent=1)
print("09-03.json:", len(S), "slides")
