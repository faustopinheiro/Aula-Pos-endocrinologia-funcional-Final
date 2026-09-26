"""Spec do deck 9.6. Gera 09-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "telas", "tipo": "frase", "fundo": "tinta", "eyebrow": "Uma hora de bicicleta, três respostas",
          "frase": "O relógio diz zona quatro. O aplicativo diz zona dois. A planilha diz “ritmo de conversa”.",
          "apoio": "Um triatleta amador pergunta qual está certo. As três zonas usam âncoras diferentes: uma fórmula de idade, um teste de um ano atrás, e a fala dele, de hoje."})

S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "O roteiro", "titulo": "Quatro passos",
          "itens": [{"t": "Âncora", "x": "o ponto de referência a partir do qual as zonas são calculadas", "cor": "tinta"},
                    {"t": "Medida do dia", "x": "frequência cardíaca, ritmo, potência ou percepção de esforço", "cor": "ambar"},
                    {"t": "Zonas", "x": "poucas, e refeitas quando a âncora envelhece", "cor": "petr"},
                    {"t": "Conferência", "x": "com a fala e com o dia seguinte", "cor": "verm"}],
          "gap_itens": 16})

# mesma porcentagem, estados diferentes: três pessoas, limiares em posições diferentes
p = [svg_abre(1664, 320, "Três pessoas com limiares em posições diferentes; a mesma porcentagem do máximo cai em faixas diferentes")]
x0, W = 300, 1200
pessoas = [(0.76, 0.90), (0.55, 0.82), (0.44, 0.64)]
for i, (l1, l2) in enumerate(pessoas):
    y = 30 + i * 90
    p.append(f'<rect x="{x0}" y="{y}" width="{W * l1}" height="56" fill="{OXID}" fill-opacity="0.35"/>')
    p.append(f'<rect x="{x0 + W * l1}" y="{y}" width="{W * (l2 - l1)}" height="56" fill="{GLIC}" fill-opacity="0.4"/>')
    p.append(f'<rect x="{x0 + W * l2}" y="{y}" width="{W * (1 - l2)}" height="56" fill="{FOSF}" fill-opacity="0.4"/>')
xl = x0 + W * 0.70
p.append(f'<line x1="{xl}" y1="14" x2="{xl}" y2="300" stroke="{TINTA}" stroke-width="4" stroke-dasharray="12 8"/>')
p.append("</svg>")
rs = [rot(40, 46, "Pessoa A: fácil", w=240, tam=22, cor=OXID, peso=700, alinha="right"),
      rot(40, 136, "Pessoa B: moderado", w=240, tam=22, cor=GLIC, peso=700, alinha="right"),
      rot(40, 226, "Pessoa C: forte", w=240, tam=22, cor=FOSF, peso=700, alinha="right"),
      rot(xl + 12, 286, "a mesma % do máximo", w=300, tam=20, cor=TINTA, peso=700)]
S.append({"id": "porcentagem", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo um · a âncora", "titulo": "A mesma porcentagem do máximo, pessoas em estados diferentes",
          "destaque": "Respostas metabólicas heterogêneas na mesma % do consumo máximo. A recomendação: ancorar nas reservas ou, melhor, nos limiares.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · J Sci Med Sport 2010 · revisão, Sports Med 2013"})

S.append({"id": "ancoras", "tipo": "duas", "eyebrow": "E o máximo costuma ser estimado", "titulo": "Dois erros somados, ou uma âncora medida",
          "esq": {"t": "Máximo estimado pela idade", "cor": "verm",
                  "itens": ["erro da fórmula no indivíduo", "somado ao erro da porcentagem", "o treino fácil do triatleta vira zona quatro"]},
          "dir": {"t": "Limiar medido na pessoa", "cor": "petr",
                  "itens": ["laboratório, quando há", "teste da fala para o primeiro limiar", "esforço contínuo de 30 minutos para o segundo"]},
          "destaque_cor": "tinta", "destaque": "Os métodos de campo estão na aula de limiares do módulo de fisiologia."})

S.append({"id": "poucas", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo três · as zonas", "titulo": "Três faixas resolvem quase tudo",
          "cards": [{"t": "Fácil", "x": "abaixo do primeiro limiar", "cor": "petr"},
                    {"t": "Moderado", "x": "entre os dois limiares", "cor": "ambar"},
                    {"t": "Forte", "x": "acima do segundo limiar", "cor": "verm"}],
          "destaque": "Cinco ou sete zonas criam uma precisão que nenhum aparelho entrega. E as zonas envelhecem: refazer a âncora faz parte da prescrição.",
          "destaque_cor": "tinta"})

S.append({"id": "ancorada", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Uma zona só vale se estiver ancorada na pessoa, e não na idade dela.",
          "apoio": "O resto é conferir se a âncora continua boa, com a ferramenta que mais ajuda nisso: a percepção de esforço."})

S.append({"id": "borg", "tipo": "numeros", "eyebrow": "A percepção tem respaldo", "titulo": "Os limiares cabem na escala de Borg",
          "numeros": [{"n": "2.560", "x": "pessoas; idades, modalidades e níveis diferentes, incluindo doença coronariana", "cor": "tinta"},
                      {"n": "≈ 11 e 13,6", "x": "notas médias no primeiro limiar e no limiar anaeróbio individual, escala de 6 a 20", "cor": "petr"}],
          "destaque": "Relação independente de sexo, idade e modalidade. Recomendação: 11 a 13 para quem treina menos; 13 a 15 para esforço mais intenso, ainda aeróbio.",
          "destaque_cor": "tinta", "fonte": "Eur J Appl Physiol 2013"})

S.append({"id": "escalas", "tipo": "duas", "eyebrow": "Duas escalas, sem misturar", "titulo": "O que dá valor à nota são as âncoras",
          "esq": {"t": "De 6 a 20", "cor": "tinta",
                  "itens": ["a do estudo de 2013", "prescrever intensidade durante o esforço"]},
          "dir": {"t": "De 0 a 10", "cor": "petr",
                  "itens": ["registrar o custo da sessão inteira", "assunto da aula de carga interna"]},
          "destaque": "Mesmas palavras todas as vezes. Na primeira aplicação: “o treino mais duro que você já fez” é o máximo.",
          "destaque_cor": "tinta", "fonte": "Borg, Med Sci Sports Exerc 1982"})

S.append({"id": "medidas", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo dois · a medida do dia", "titulo": "Cada medida tem um ponto cego",
          "cards": [{"t": "Frequência cardíaca", "x": "atrasa nos tiros curtos; sobe aos poucos no esforço longo, mais no calor", "cor": "ambar"},
                    {"t": "Ritmo ou potência", "x": "responde na hora; não diz quanto custou naquele dia", "cor": "petr"},
                    {"t": "Percepção de esforço", "x": "integra sono, calor e cansaço; avisa primeiro", "cor": "verm"}]})

S.append({"id": "tabela", "tipo": "tabela", "eyebrow": "Juntando tudo", "titulo": "Três jeitos de reconhecer cada faixa",
          "cab": ["Faixa", "Fala", "Escala de 6 a 20", "Medida objetiva"],
          "larguras": [16, 24, 26, 34],
          "linhas": [["Fácil", "frases inteiras", "até perto de 11", "abaixo do 1º limiar medido"],
                     ["Moderado", "frases curtas", "em torno de 11 a 14", "entre os limiares"],
                     ["Forte", "palavras soltas", "acima de 14 a 15", "acima do 2º limiar"]],
          "destaque": "As notas são aproximações de média para começar. Na pessoa, ajustam-se em poucas semanas.",
          "destaque_cor": "tinta"})

S.append({"id": "desempate", "tipo": "tabela", "eyebrow": "Passo quatro · quando os aparelhos discordam", "titulo": "Cada medida manda num tipo de treino",
          "cab": ["Treino", "Manda", "Por quê"],
          "larguras": [26, 30, 44],
          "linhas": [["Dia fácil", "fala e percepção", "se conversa em frases inteiras, está fácil"],
                     ["Intervalado", "ritmo ou potência", "a frequência cardíaca atrasa"],
                     ["Longo e estável", "frequência cardíaca", "ancorada no limiar, atenção à subida no fim"]],
          "destaque": "A conferência final é o dia seguinte. “Fácil” que deixa cansaço pede âncora nova.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Zonas e percepção de esforço", "titulo": "Âncora na pessoa, medida certa para cada treino",
          "regras": ["Porcentagem de máximo estimado é a âncora mais fraca",
                     "Poucas zonas, refeitas quando envelhecem",
                     "Percepção de esforço integra o dia e tem respaldo"],
          "cards": [{"t": "Preparação física", "x": "Ancora as zonas e ensina a escala."},
                    {"t": "Médico", "x": "Interpreta o teste e libera a intensidade alta."},
                    {"t": "Atleta", "x": "Dá a nota com as mesmas âncoras, sempre."}],
          "quem": "Próxima aula: carga externa, GPS e métricas de campo."})

spec = {"arquivo": "aulas/MOD09/09-06-prescricao-por-zonas-e-percepcao-de-esforco.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Prescrição por zonas e percepção de esforço", "subtitulo": "Âncora, medida e conferência",
        "nota_capa": "Entra por três aparelhos que discordam sobre o mesmo treino.",
        "secoes": {"telas": ["A cena e o roteiro.", "capa"],
                   "porcentagem": ["A âncora e as zonas.", "porcentagem"],
                   "borg": ["A percepção de esforço.", "borg"],
                   "medidas": ["A medida do dia e o desempate.", "medidas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-06.json"), "w"), ensure_ascii=False, indent=1)
print("09-06.json:", len(S), "slides")
