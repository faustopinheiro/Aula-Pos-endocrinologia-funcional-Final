"""Spec do deck 5.4. Gera 05-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a expectativa errada
S.append({"id": "formigamento", "tipo": "frase", "fundo": "tinta", "eyebrow": "Perfil típico",
          "frase": "“Não senti nada, só um formigamento.”",
          "apoio": "Parou no terceiro dia. Dois erros de número: esperava efeito no dia, e a beta-alanina funciona por acúmulo, em semanas; e leu o formigamento como falha, quando é parestesia esperada, resolvida pela dose."})

# 2. carnosina
p = [svg_abre(1664, 300, "Beta-alanina e histidina formam carnosina dentro do músculo; a histidina sobra e a beta-alanina é o passo limitante"),
     "<defs>" + seta_marker("c1", MUDO) + "</defs>"]
rs = []
p.append(caixa(0, 40, 420, 110, FOSF, FOSF_T, esp=3))
rs += [rot(0, 60, "beta-alanina", w=420, tam=34, cor=FOSF, peso=700, alinha="center"),
       rot(0, 104, "escassa: passo limitante", w=420, tam=26, cor=TINTA, alinha="center")]
p.append(caixa(0, 180, 420, 110, OXID, OXID_T, esp=3))
rs += [rot(0, 200, "histidina", w=420, tam=34, cor=OXID, peso=700, alinha="center"),
       rot(0, 244, "sobra no músculo", w=420, tam=26, cor=TINTA, alinha="center")]
p.append(f'<line x1="440" y1="95" x2="720" y2="160" stroke="{MUDO}" stroke-width="4" marker-end="url(#c1)"/>')
p.append(f'<line x1="440" y1="235" x2="720" y2="180" stroke="{MUDO}" stroke-width="4" marker-end="url(#c1)"/>')
p.append(caixa(740, 100, 420, 130, AZUL, AZUL_T, esp=4))
rs += [rot(740, 124, "carnosina", w=420, tam=38, cor=AZUL, peso=700, alinha="center"),
       rot(740, 176, "tampão dentro da fibra", w=420, tam=26, cor=TINTA, alinha="center")]
p.append("</svg>")
rs += [rot(1200, 60, "Carnosina ingerida é quebrada antes de chegar ao músculo: por isso se suplementa beta-alanina.", w=464, tam=26, cor=TINTA),
       rot(1200, 190, "Tamponamento é a explicação mais citada, não necessariamente a completa.", w=464, tam=26, cor=MUDO)]
S.append({"id": "carnosina", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mecanismo", "titulo": "Matéria-prima, não efeito direto",
          "destaque": "O que sustenta o uso não é o mecanismo. É o desfecho replicado.",
          "destaque_cor": "tinta"})

# 3. Hill
S.append({"id": "acumulo", "tipo": "numeros", "eyebrow": "Hill e colaboradores, 2007", "titulo": "Quatro semanas é o começo, não o fim",
          "numeros": [{"n": "+59%", "x": "carnosina muscular em 4 semanas", "cor": "ambar"},
                      {"n": "+80%", "x": "carnosina muscular em 10 semanas", "cor": "petr"},
                      {"n": "+13%", "x": "trabalho total no teste de bicicleta, em 4 semanas", "cor": "tinta"}],
          "destaque": "Quem toma quinze dias e para não chegou à metade do caminho. Quem toma três dias não testou nada.",
          "destaque_cor": "verm", "fonte": "13 homens, biópsia muscular · Amino Acids 2007"})

# 4. a janela
p = [svg_abre(1664, 260, "Régua da duração do esforço, de zero a vinte minutos: a janela da beta-alanina vai de trinta segundos a dez minutos")]
fx = lambda m: 20 + (m ** 0.5) / (20 ** 0.5) * 1620
p.append(f'<rect x="{fx(0):.0f}" y="60" width="{fx(0.5)-fx(0):.0f}" height="90" fill="{CLARO}" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<rect x="{fx(0.5):.0f}" y="60" width="{fx(10)-fx(0.5):.0f}" height="90" fill="{OXID_T}" stroke="{OXID}" stroke-width="4"/>')
p.append(f'<rect x="{fx(10):.0f}" y="60" width="{fx(20)-fx(10):.0f}" height="90" fill="{CLARO}" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(fx(0.5) + 20, 90, "janela da beta-alanina", w=fx(10) - fx(0.5) - 40, tam=32, cor=OXID, peso=700, alinha="center"),
      rot(fx(0) - 10, 16, "fosfocreatina", w=300, tam=24, cor=MUDO, peso=600),
      rot(fx(10) + 10, 16, "oxidativo", w=300, tam=24, cor=MUDO, peso=600)]
for m, t in [(0.5, "30 s"), (2, "2 min"), (5, "5 min"), (10, "10 min"), (20, "20 min")]:
    rs.append(rot(min(fx(m) - 70, 1664 - 140), 162, t, w=140, tam=26, cor=TINTA, peso=700, alinha="right" if m == 20 else "center"))
S.append({"id": "janela", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saunders e colaboradores, 2017", "titulo": "De trinta segundos a dez minutos",
          "destaque": "40 estudos, 65 protocolos, 1.461 pessoas. Abaixo de 30 s domina a fosfocreatina (creatina); acima de 10 min, o esforço oxidativo. No meio, o território glicolítico intenso.",
          "destaque_cor": "petr", "fonte": "Escala da régua comprimida · British Journal of Sports Medicine 2017"})

# 5. magnitude
S.append({"id": "tamanho", "tipo": "duas", "eyebrow": "A magnitude, sem propaganda", "titulo": "Real, e menor do que o rótulo sugere",
          "esq": {"t": "O tamanho", "cor": "petr",
                  "itens": ["pequeno, como todo o grupo A", "num 800 m, decide a prova", "num treino de academia, não se percebe"]},
          "dir": {"t": "O desenho dos estudos", "cor": "ambar",
                  "itens": ["muitos ganhos em testes de capacidade", "tempo sustentado, trabalho total", "menos em provas cronometradas reais"]},
          "destaque": "Efeito medido com precisão em laboratório não é garantia do mesmo efeito na rua.",
          "destaque_cor": "tinta"})

# 6. protocolo
S.append({"id": "protocolo", "tipo": "numeros", "eyebrow": "Trexler e colaboradores, 2015", "titulo": "O protocolo",
          "numeros": [{"n": "4 a 6 g", "x": "por dia, todos os dias", "cor": "petr"},
                      {"n": "≥ 4 sem", "x": "para efeito; o estoque sobe por 10 semanas ou mais", "cor": "ambar"},
                      {"n": "≈ 1,6 g", "x": "por tomada, dividida ao longo do dia", "cor": "tinta"}],
          "destaque": "Quem vai competir começa pelo menos um mês antes, idealmente dois ou três.",
          "destaque_cor": "petr", "fonte": "Journal of the International Society of Sports Nutrition 2015"})

# 7. parestesia e notas
S.append({"id": "notas", "tipo": "lista", "eyebrow": "Parestesia e três notas", "titulo": "O formigamento se resolve com dose",
          "itens": [{"t": "Parestesia", "x": "rosto, pescoço, orelhas; curta; único efeito adverso relatado; dividir a dose ou liberação prolongada", "cor": "ambar"},
                    {"t": "O total acumulado importa mais que o dia", "x": "a carga ao longo das semanas enche o estoque", "cor": "petr"},
                    {"t": "Quando para, cai devagar", "x": "alguns dias esquecidos não apagam nada", "cor": "petr"},
                    {"t": "Uso diário, qualquer horário", "x": "não é pré-treino, embora seja vendida dentro de um", "cor": "tinta"}],
          "gap_itens": 18})

# 8. onde vale
S.append({"id": "onde", "tipo": "duas", "eyebrow": "É só aplicar a janela", "titulo": "Onde vale, e onde não vale",
          "esq": {"t": "Vale", "cor": "petr",
                  "itens": ["400 e 800 m; 200 m de natação", "remo de 2.000 m; perseguição", "lutas; intermitentes (evidência mais heterogênea)", "vegetarianos: menos carnosina, mais espaço"]},
          "dir": {"t": "Não vale", "cor": "verm",
                  "itens": ["salto, uma repetição máxima, tiro curto", "meia maratona e maratona", "quem quer sentir algo hoje", "como substituto de condicionamento"]},
          "destaque": "A capacidade de tamponamento se treina. A beta-alanina se soma a esse treino; não o substitui.",
          "destaque_cor": "tinta"})

# 9. três perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "Três perfis típicos", "titulo": "Quem está na janela",
          "cab": ["Perfil", "Esforço", "Na janela?", "Conduta"],
          "larguras": [22, 22, 16, 40],
          "linhas": [["Nadadora, 200 m", "2 a 3 min", "no meio", "4 a 6 g/dia, divididos, dois meses antes"],
                     ["Futsal", "tiros repetidos", "em parte", "defensável, com expectativa calibrada"],
                     ["Maratonista", "horas", "fora", "“funciona, mas não para o que você faz”"]],
          "destaque": "O dinheiro do maratonista rende mais em carboidrato durante a prova.",
          "destaque_cor": "ambar"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Os quatro números", "titulo": "Quanto tempo dura o esforço?",
          "regras": ["Janela de 30 segundos a 10 minutos",
                     "4 a 6 g por dia, divididos, por pelo menos 4 semanas",
                     "Efeito pequeno, real, mais visível no laboratório do que na rua"],
          "cards": [{"t": "Nutricionista", "x": "Indica e dosa."},
                    {"t": "Educador físico e preparador", "x": "O treino na faixa em que ela age."},
                    {"t": "Médico", "x": "Sintoma atípico; gestante, criança, adolescente."}],
          "quem": "A pergunta da duração do esforço é de todos."})

spec = {"arquivo": "aulas/MOD05/05-04-beta-alanina-e-capacidade-de-tamponamento.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Beta-alanina", "subtitulo": "Carnosina muscular, janela de efeito e protocolo de uso",
        "nota_capa": "Entra pela expectativa errada.",
        "secoes": {"formigamento": ["O mecanismo e o acúmulo.", "capa"],
                   "janela": ["A janela e o tamanho.", "janela"],
                   "protocolo": ["Protocolo, onde vale e três perfis.", "protocolo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-04.json"), "w"), ensure_ascii=False, indent=1)
print("05-04.json:", len(S), "slides")
