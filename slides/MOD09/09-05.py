"""Spec do deck 9.5. Gera 09-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "planilha", "tipo": "frase", "fundo": "tinta", "eyebrow": "O caso",
          "frase": "“Cansada, mas nunca morta. Não consigo conversar direito, mas também não estou no limite.”",
          "apoio": "Uma corredora na faixa dos quarenta anos, seis anos de corrida, quatro treinos por semana quase no mesmo ritmo, três deles com o grupo do bairro. Há dois anos, o tempo nos dez quilômetros não sai do lugar."})

# três faixas e a semana empilhada no meio
p = [svg_abre(1664, 300, "Três faixas de intensidade com a semana da corredora quase toda na faixa do meio")]
faixas = [(40, OXID), (590, GLIC), (1140, FOSF)]
for x, c in faixas:
    p.append(f'<rect x="{x}" y="60" width="500" height="200" rx="12" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-width="3"/>')
for i in range(4):
    p.append(f'<rect x="{620 + i * 112}" y="150" width="90" height="90" rx="10" fill="{GLIC}"/>')
p.append("</svg>")
rs = [rot(40, 76, "Fácil", w=500, tam=30, cor=OXID, peso=700, alinha="center"),
      rot(40, 120, "frases inteiras", w=500, tam=22, cor=MUDO, alinha="center"),
      rot(590, 76, "Moderado", w=500, tam=30, cor=GLIC, peso=700, alinha="center"),
      rot(590, 120, "“confortavelmente desconfortável”", w=500, tam=22, cor=MUDO, alinha="center"),
      rot(1140, 76, "Forte", w=500, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(1140, 120, "palavras soltas", w=500, tam=22, cor=MUDO, alinha="center"),
      rot(590, 268, "os quatro treinos da semana dela", w=500, tam=22, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "faixas", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um vocabulário comum", "titulo": "Três faixas, e a semana dela empilhada no meio",
          "destaque": "Fácil “não parece treino”. Forte dói. Sobra o meio.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "tipos", "tipo": "duas", "eyebrow": "Contínuo e intervalado", "titulo": "Dois jeitos de organizar o esforço",
          "esq": {"t": "Contínuo", "cor": "petr",
                  "itens": ["esforço sustentado, sem pausas", "fácil e longo, ou moderado e mais curto", "intensidade estável"]},
          "dir": {"t": "Intervalado", "cor": "verm",
                  "itens": ["trechos acima do sustentável, com pausas", "acumula mais tempo em intensidade alta", "variáveis: intensidade e duração do trecho e da pausa, repetições, modo"]},
          "destaque": "Mudar qualquer variável do intervalado muda o estímulo.",
          "destaque_cor": "tinta", "fonte": "Revisão, Sports Med 2013"})

S.append({"id": "ambos", "tipo": "duas", "eyebrow": "Contínuo ou intervalado?", "titulo": "Os dois funcionam; o intervalado entrega mais por minuto",
          "esq": {"t": "O que a metanálise encontrou", "cor": "tinta",
                  "itens": ["adultos saudáveis, 18 a 45 anos", "grandes melhoras no consumo máximo de oxigênio com os dois", "melhora maior com o intervalado"]},
          "dir": {"t": "A leitura correta", "cor": "petr",
                  "itens": ["não é “intervalado sempre”", "o intervalado dá mais estímulo cardiorrespiratório em menos tempo", "o contínuo fácil entrega outra coisa"]},
          "destaque_cor": "tinta", "destaque": "O que o contínuo fácil entrega é o próximo slide.", "fonte": "Metanálise, Sports Med 2015"})

S.append({"id": "elite", "tipo": "numeros", "eyebrow": "O que fazem os melhores", "titulo": "A maior parte do tempo no fácil",
          "numeros": [{"n": "10 a 13", "x": "sessões por semana em atletas de endurance de alto nível", "cor": "tinta"},
                      {"n": "~80%", "x": "das sessões em intensidade baixa", "cor": "petr"}],
          "destaque": "Intensificar o treino de quem já é bem treinado não trouxe evidência convincente de ganho no longo prazo. O fácil constrói capilares e mitocôndrias com pouca fadiga.",
          "destaque_cor": "tinta", "fonte": "Int J Sports Physiol Perform 2010"})

S.append({"id": "ensaio", "tipo": "numeros", "eyebrow": "O ensaio mais citado", "titulo": "Polarizado à frente, com cuidado na leitura",
          "numeros": [{"n": "48", "x": "atletas bem treinados, nove semanas, quatro modelos", "cor": "tinta"},
                      {"n": "+11,7%", "x": "consumo de pico no polarizado; limiar e alto volume sem melhora significativa", "cor": "petr"}],
          "destaque": "Metanálise de 2019: polarizado cerca de 40 segundos melhor no contrarrelógio de 10 km; no ciclismo, menos claro. Para a amadora, transfere-se a direção, não o número.",
          "destaque_cor": "ambar", "fonte": "Front Physiol 2014 · J Strength Cond Res 2019"})

S.append({"id": "paga", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O treino fácil não é o treino que sobra. É o treino que paga o treino difícil.",
          "apoio": "Sem ele, a sessão forte não sai com qualidade, e vira mais uma sessão na faixa do meio."})

S.append({"id": "cinzenta", "tipo": "cards", "por_linha": 3, "eyebrow": "O diagnóstico do caso", "titulo": "A zona cinzenta: fadiga que atrapalha, estímulo que não basta",
          "cards": [{"t": "Fácil “não parece treino”", "x": "então ela nunca corre devagar", "cor": "ambar"},
                    {"t": "Forte dói", "x": "então ela nunca corre forte de verdade", "cor": "ambar"},
                    {"t": "O grupo escolhe", "x": "três vezes por semana, o pelotão dita o ritmo", "cor": "verm"}],
          "destaque": "A pergunta que confirma custa zero: quanto você consegue conversar enquanto corre?",
          "destaque_cor": "tinta"})

S.append({"id": "conta", "tipo": "numeros", "eyebrow": "A aritmética do volume baixo", "titulo": "Sessões de qualidade em número, não em porcentagem",
          "numeros": [{"n": "20% de 12", "x": "cerca de 2,4 sessões duras por semana", "cor": "tinta"},
                      {"n": "20% de 4", "x": "0,8: menos de uma sessão dura", "cor": "verm"}],
          "destaque": "De três a cinco sessões aeróbias: uma a duas de qualidade, o resto fácil de verdade. Com quatro, uma forte e três fáceis: 75% fácil.",
          "destaque_cor": "tinta"})

S.append({"id": "plano", "tipo": "tabela", "eyebrow": "O plano", "titulo": "A semana da corredora, reorganizada",
          "cab": ["Sessão", "Antes", "Depois"],
          "larguras": [22, 34, 44],
          "linhas": [["Qualidade", "nenhuma forte de verdade", "intervalado: por exemplo, 4 a 6 blocos de 3 a 4 min fortes, pausas de trote"],
                     ["Longa", "sozinha, no ritmo do meio", "sozinha, mais devagar"],
                     ["Fáceis", "três com o grupo, no ritmo do meio", "duas: uma no pelotão mais lento, uma sozinha, em frases inteiras"],
                     ["Força", "nenhuma", "duas sessões curtas por semana"]],
          "destaque": "O formato do intervalado é exemplo de prática corrente. Começa pelo número menor de blocos.",
          "destaque_cor": "tinta"})

S.append({"id": "acompanhar", "tipo": "cards", "por_linha": 3, "eyebrow": "Como acompanhar, sem laboratório", "titulo": "Três perguntas",
          "cards": [{"t": "Dias fáceis", "x": "ela conversa em frases inteiras? Se não, está rápido", "cor": "petr"},
                    {"t": "Intervalado", "x": "os blocos saem parecidos do primeiro ao último?", "cor": "verm"},
                    {"t": "A semana", "x": "sono, dor e vontade de treinar no dia seguinte", "cor": "ambar"}],
          "destaque": "O caso não tem desfecho aqui. Fica o raciocínio: achar a zona cinzenta, separar os extremos, dosar a qualidade em número.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Treino aeróbio", "titulo": "Separar os extremos, e contar as sessões de qualidade",
          "regras": ["Contínuo e intervalado funcionam; o intervalado rende mais por minuto",
                     "O fácil paga o difícil",
                     "Quem treina pouco: uma a duas sessões de qualidade"],
          "cards": [{"t": "Preparação física", "x": "Separa o fácil do forte e dosa a qualidade."},
                    {"t": "Médico", "x": "Libera a intensidade alta em quem tem risco."},
                    {"t": "Atleta", "x": "Aceita correr devagar, e sozinha se preciso."}],
          "quem": "Próxima aula: prescrição por zonas e por percepção de esforço."})

spec = {"arquivo": "aulas/MOD09/09-05-treino-aerobio-continuo-e-intervalado.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Treino aeróbio contínuo e intervalado", "subtitulo": "Distribuição de intensidade para quem treina pouco",
        "nota_capa": "Entra pelo caso de uma corredora que parou de melhorar.",
        "secoes": {"planilha": ["O caso e as três faixas.", "capa"],
                   "tipos": ["Contínuo, intervalado e a evidência.", "tipos"],
                   "cinzenta": ["O diagnóstico e a aritmética.", "cinzenta"],
                   "plano": ["O plano e o acompanhamento.", "plano"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-05.json"), "w"), ensure_ascii=False, indent=1)
print("09-05.json:", len(S), "slides")
