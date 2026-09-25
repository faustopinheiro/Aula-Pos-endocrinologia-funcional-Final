"""Spec do deck 8.8. Gera 08-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "paro", "tipo": "frase", "fundo": "tinta", "eyebrow": "Na borda da piscina e no chão da academia",
          "frase": "“Eu paro?” Uma decisão com três saídas, não com duas.",
          "apoio": "Uma nadadora adolescente com dor no ombro no meio da temporada; um levantador com dor lombar desde o terra de segunda-feira. “Para tudo” e “continua, é normal” são as duas respostas ruins."})

p = [svg_abre(1664, 280, "Três portas: parar, estreita; modificar, a mais larga; manter")]
portas = [(80, 260, FOSF), (520, 620, GLIC), (1320, 300, OXID)]
for x, w, c in portas:
    p.append(f'<rect x="{x}" y="40" width="{w}" height="200" rx="14" fill="{c}" fill-opacity="0.18" stroke="{c}" stroke-width="5"/>')
p.append("</svg>")
rs = [rot(80, 110, "parar", w=260, tam=34, cor=FOSF, peso=700, alinha="center"),
      rot(520, 110, "modificar", w=620, tam=40, cor=GLIC, peso=700, alinha="center"),
      rot(1320, 110, "manter", w=300, tam=34, cor=OXID, peso=700, alinha="center"),
      rot(80, 250, "sinal de alerta ou piora apesar de tudo", w=420, tam=20, cor=MUDO),
      rot(520, 250, "mudar o que provoca; a maior parte dos casos", w=620, tam=20, cor=MUDO, alinha="center"),
      rot(1320, 250, "dor baixa, estável, sem piora no dia seguinte", w=330, tam=20, cor=MUDO)]
S.append({"id": "portas", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As três saídas", "titulo": "A porta do meio é a mais larga",
          "destaque": "A decisão é revista toda semana, pela leitura de 24 horas.",
          "destaque_cor": "tinta", "fonte": "Esquema"})

S.append({"id": "alerta", "tipo": "duas", "eyebrow": "Quando parar e avaliar", "titulo": "Os sinais que tiram a decisão da piscina e da academia",
          "esq": {"t": "Ombro", "cor": "verm",
                  "itens": ["perda súbita de força depois de trauma", "sensação de que saiu do lugar", "formigamento ou fraqueza descendo para a mão"]},
          "dir": {"t": "Coluna", "cor": "verm",
                  "itens": ["fraqueza ou dormência progredindo na perna", "alteração urinária ou dormência na sela: emergência", "dor noturna com febre, perda de peso, câncer prévio"]},
          "destaque": "E o adolescente com dor lombar que piora ao estender a coluna: lesão por estresse do arco vertebral entra na lista, avaliação médica antes do programa.",
          "destaque_cor": "verm"})

S.append({"id": "natacao", "tipo": "numeros", "eyebrow": "O ombro da nadadora", "titulo": "Começa numa temporada, não numa braçada",
          "numeros": [{"n": "12", "x": "estudos reunidos em 2020", "cor": "tinta"},
                      {"n": "1.460", "x": "nadadores de competição, da base aos masters", "cor": "tinta"}],
          "destaque": "Os adolescentes tiveram mais dor no ombro, e nesse grupo o volume de treino se associou à dor. Monitorar o ano inteiro; evitar aumentos grandes e repentinos.",
          "destaque_cor": "ambar", "fonte": "Revisão sistemática, J Athl Train 2020"})

S.append({"id": "mod_ombro", "tipo": "tabela", "eyebrow": "Modificar o ombro", "titulo": "Várias alavancas, a atleta na água",
          "cab": ["Alavanca", "O que muda"],
          "larguras": [26, 74],
          "linhas": [["Volume", "menos quilômetros por um período, sem zerar"],
                     ["Intensidade e estilo", "tirar as séries mais fortes e o estilo que mais provoca"],
                     ["Material", "o palmar grande costuma ser o primeiro a sair"],
                     ["Pernada", "mais pernas mantém o condicionamento com menos ombro"],
                     ["Em paralelo", "fortalecimento progressivo do manguito e da escápula"]],
          "destaque": "A modificação tira o pico; o fortalecimento aumenta a capacidade.",
          "destaque_cor": "tinta"})

S.append({"id": "cirurgia", "tipo": "cards", "por_linha": 3, "eyebrow": "E quando alguém propõe cirurgia", "titulo": "Um ensaio com artroscopia sem descompressão",
          "cards": [{"t": "Descompressão", "x": "melhorou um pouco mais que nada, sem diferença clinicamente importante", "cor": "ambar"},
                    {"t": "Artroscopia sem retirar nada", "x": "o mesmo resultado da descompressão", "cor": "ambar"},
                    {"t": "Nenhum tratamento", "x": "um pouco atrás dos dois grupos operados", "cor": "tinta"}],
          "destaque": "Adultos com dor subacromial, não nadadores de competição; a decisão é do cirurgião com o paciente. Mas a carga bem conduzida segue como primeira linha.",
          "destaque_cor": "tinta", "fonte": "32 hospitais britânicos · Lancet 2018"})

S.append({"id": "meio", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Parar tudo raramente é a resposta. Manter tudo também não.",
          "apoio": "Modificar o suficiente para a dor baixar, e pouco o bastante para o atleta seguir treinando, condicionado e confiante."})

S.append({"id": "flexao", "tipo": "duas", "eyebrow": "A coluna do levantador · o medo", "titulo": "“Você curvou a coluna e se machucou”",
          "esq": {"t": "O que a revisão de 2020 buscou", "cor": "tinta",
                  "itens": ["mais flexão lombar ao levantar", "é fator de risco para a dor começar ou persistir?", "diferencia quem tem de quem não tem dor?"]},
          "dir": {"t": "O que encontrou", "cor": "petr",
                  "itens": ["não, nas duas perguntas", "evidência de baixa qualidade", "técnica segue importando para o desempenho"]},
          "destaque": "A explicação não tem o peso que costuma ter, e alimenta um medo de mexer a coluna que atrapalha a recuperação.",
          "destaque_cor": "tinta", "fonte": "J Orthop Sports Phys Ther 2020"})

S.append({"id": "risco", "tipo": "numeros", "eyebrow": "O risco em perspectiva", "titulo": "O medo costuma ser maior que o risco",
          "numeros": [{"n": "1 a 4,4", "x": "lesões por mil horas de treino no levantamento básico", "cor": "petr"},
                      {"n": "> 3 anos", "x": "é quanto duram mil horas para quem levanta seis horas por semana", "cor": "tinta"}],
          "destaque": "Risco parecido com outros esportes de força sem contato, e baixo perto dos de contato.",
          "destaque_cor": "tinta", "fonte": "Revisão sistemática, Br J Sports Med 2017 · conta feita em aula"})

S.append({"id": "mod_coluna", "tipo": "tabela", "eyebrow": "Modificar a coluna", "titulo": "Sem sinal de alerta, ele continua sendo um levantador",
          "cab": ["Alavanca", "O que muda"],
          "larguras": [22, 78],
          "linhas": [["Carga", "menos carga no exercício que provoca, sem tirá-lo; sobe pela resposta do dia seguinte"],
                     ["Amplitude", "puxar de blocos ou suportes e ir descendo"],
                     ["Variação", "barra hexagonal no lugar do terra; agachamento com a barra na frente"],
                     ["Volume", "menos séries pesadas na semana"],
                     ["O resto", "membros superiores, cardio, o que não dói"]],
          "destaque": "Série do Lancet de 2018: educação, retomar as atividades e exercício como primeira linha; sem imagem de rotina.",
          "destaque_cor": "tinta", "fonte": "Lancet 2018"})

S.append({"id": "custo", "tipo": "tabela", "eyebrow": "O custo de escolher errado", "titulo": "Cada erro tem o seu preço",
          "cab": ["Escolha errada", "O preço"],
          "larguras": [36, 64],
          "linhas": [["Parar quando dava para modificar", "força, condicionamento, medo; na adolescente, a temporada"],
                     ["Manter quando precisava modificar", "dor crônica, volume subindo, compensação"],
                     ["Modificar quando precisava parar", "ruptura, lesão do arco vertebral, sinal neurológico"]],
          "destaque": "Por isso a primeira pergunta é sempre a dos sinais de alerta.",
          "destaque_cor": "verm"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Ombro e coluna", "titulo": "A maior parte da solução está na planilha",
          "regras": ["Primeiro, os sinais de alerta",
                     "Depois, modificar o que provoca e manter o que não dói",
                     "Rever toda semana pelo dia seguinte"],
          "cards": [{"t": "Médico", "x": "Sinais de alerta e decisão sobre imagem."},
                    {"t": "Fisioterapia", "x": "Fortalecimento e escolha das modificações."},
                    {"t": "Treinador e preparador", "x": "Mexem no volume, na carga e no material."}],
          "quem": "Próxima aula: recursos terapêuticos; o que muda e o que é ritual."})

spec = {"arquivo": "aulas/MOD08/08-08-membro-superior-e-coluna.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Ombro e coluna", "subtitulo": "Parar, modificar ou manter",
        "nota_capa": "Entra por uma nadadora e um levantador fazendo a mesma pergunta.",
        "secoes": {"paro": ["A pergunta, as três saídas e os alertas.", "capa"],
                   "natacao": ["O ombro da nadadora.", "natacao"],
                   "flexao": ["A coluna do levantador.", "flexao"],
                   "custo": ["O custo de errar e o fecho.", "custo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-08.json"), "w"), ensure_ascii=False, indent=1)
print("08-08.json:", len(S), "slides")
