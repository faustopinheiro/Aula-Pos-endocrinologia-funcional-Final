"""Spec do deck 6.3. Gera 06-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. frase
S.append({"id": "laudos", "tipo": "frase", "fundo": "tinta", "eyebrow": "A zona cinzenta",
          "frase": "Três laudos assustadores. Nenhum deles é, sozinho, um diagnóstico.",
          "apoio": "Os três descrevem um coração que treinou muito, e descrevem também, com as mesmas palavras, doenças que matam jovens em campo. Esta aula não ensina a liberar nem a afastar: ensina a não entrar em pânico e a não banalizar."})

# 2. perfis
S.append({"id": "perfis", "tipo": "cards", "por_linha": 3, "eyebrow": "Três perfis típicos", "titulo": "O que os laudos dizem",
          "cards": [{"t": "O zagueiro", "x": "“hipertrofia ventricular esquerda”, parede de 13 mm", "cor": "ambar"},
                    {"t": "A triatleta", "x": "cavidade de 59 mm, “avaliar cardiomiopatia dilatada”; sem sintoma", "cor": "petr"},
                    {"t": "O adolescente do basquete", "x": "negro; onda T invertida de V1 a V4, “considerar cardiopatia”", "cor": "verm"}],
          "destaque_cor": "tinta"})

# 3. o que o treino faz
S.append({"id": "remodelamento", "tipo": "duas", "eyebrow": "O que o treino faz", "titulo": "Coração de atleta é um conjunto, não um número",
          "esq": {"t": "Coração de atleta", "cor": "petr",
                  "itens": ["cavidade maior", "parede no limite ou um pouco acima", "frequência baixa, 40 a 50 bpm", "função normal ou melhor", "capacidade funcional alta"]},
          "dir": {"t": "O que separar", "cor": "verm",
                  "itens": ["cardiomiopatia hipertrófica", "cardiomiopatia dilatada", "cardiomiopatia arritmogênica"]},
          "destaque": "Em fase inicial, as três doenças produzem os números que o treino produz. O exame não separa; o raciocínio separa.",
          "destaque_cor": "tinta"})

# 4. régua
p = [svg_abre(1664, 260, "Régua de espessura de parede de 8 a 20 milímetros com faixas: até 12 esperado, 13 a 16 zona cinzenta, acima de 16 investigar")]
fx = lambda mm: 20 + (mm - 8) / 12 * 1620
p.append(f'<rect x="{fx(8):.0f}" y="60" width="{fx(12.5)-fx(8):.0f}" height="100" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append(f'<rect x="{fx(12.5):.0f}" y="60" width="{fx(16.5)-fx(12.5):.0f}" height="100" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
p.append(f'<rect x="{fx(16.5):.0f}" y="60" width="{fx(20)-fx(16.5):.0f}" height="100" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(fx(8), 90, "esperado", w=fx(12.5) - fx(8), tam=32, cor=OXID, peso=700, alinha="center"),
      rot(fx(12.5), 90, "zona cinzenta", w=fx(16.5) - fx(12.5), tam=32, cor=GLIC, peso=700, alinha="center"),
      rot(fx(16.5), 90, "provavelmente não é treino", w=fx(20) - fx(16.5), tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(fx(12.5) - 100, 16, "13: olhe com atenção", w=400, tam=24, cor=TINTA, peso=600),
      rot(fx(16.5) - 100, 16, "16: o teto do treino", w=400, tam=24, cor=TINTA, peso=600)]
for mm in (8, 10, 12, 14, 16, 18, 20):
    rs.append(rot(min(max(fx(mm) - 50, 0), 1564), 176, f"{mm} mm", w=100, tam=24, cor=MUDO, alinha="center"))
S.append({"id": "parede", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Pelliccia e colaboradores, 1991", "titulo": "Espessura da parede em 947 atletas de elite",
          "destaque": "Parede de 13 mm ou mais foi incomum, quase só no remo e na canoagem, e com cavidade aumentada. Acima de 16 com cavidade não dilatada: hipertrófica até prova em contrário.",
          "destaque_cor": "tinta", "fonte": "New England Journal of Medicine 1991"})

# 5. cavidade
S.append({"id": "cavidade", "tipo": "numeros", "eyebrow": "Pelliccia e colaboradores, 1999", "titulo": "A cavidade que assusta o laudo",
          "numeros": [{"n": "1.309", "x": "atletas de elite, 38 esportes", "cor": "tinta"},
                      {"n": "≈ 15%", "x": "com cavidade em faixa compatível com cardiomiopatia dilatada", "cor": "ambar"},
                      {"n": "43 a 70 mm", "x": "variação nos homens; 38 a 66 mm nas mulheres", "cor": "petr"}],
          "destaque": "A dobradiça: na ausência de disfunção sistólica, é provavelmente adaptação. E 52% de fração de ejeção num triatleta não é 52% num sedentário.",
          "destaque_cor": "petr", "fonte": "Superfície corporal e endurance como determinantes · Annals of Internal Medicine 1999"})

# 6. normal para quem
S.append({"id": "quem", "tipo": "tabela", "eyebrow": "O erro mais evitável", "titulo": "Normal para quem?",
          "cab": ["Variável", "O dado", "A consequência"],
          "larguras": [18, 44, 38],
          "linhas": [["Sexo", "600 mulheres de elite: parede de 6 a 12 mm, nenhuma acima", "acima de 12 na mulher: investigar"],
                     ["Ancestralidade", "negros 11,3 × brancos 10,0 mm; > 12 mm em 18% × 4%", "régua de branco gera falso-positivo no negro"],
                     ["Idade", "720 adolescentes de elite: limites menores", "o teto de 16 do adulto não vale"],
                     ["Tamanho e esporte", "indexar; remo e ciclismo nos extremos", "zagueiro não é remador olímpico"]],
          "destaque": "A régua não pode ser afrouxada no atleta negro, porque a hipertrófica pesa nas mortes súbitas. Precisa ser a régua certa.",
          "destaque_cor": "verm", "fonte": "Pelliccia 1996 · Basavarajaiah 2008 · Sharma 2002"})

# 7. discriminadores
S.append({"id": "discriminadores", "tipo": "duas", "eyebrow": "Por que o cardiologista pede o que pede", "titulo": "Os discriminadores",
          "esq": {"t": "Aponta para atleta", "cor": "petr",
                  "itens": ["parede e cavidade crescem juntas", "hipertrofia simétrica", "relaxamento normal ou melhor", "VO2 > 50 ou > 120% do previsto", "sem realce tardio"]},
          "dir": {"t": "Aponta para doença", "cor": "verm",
                  "itens": ["parede espessa, cavidade pequena", "hipertrofia assimétrica, septal", "disfunção diastólica", "capacidade baixa", "fibrose na ressonância; história familiar"]},
          "destaque": "“Mas o eco dele está normal” não encerra a conversa quando há sintoma ou história familiar.",
          "destaque_cor": "tinta", "fonte": "Ergoespirometria: Sharma e colaboradores, JACC 2000"})

# 8. destreino
S.append({"id": "destreino", "tipo": "numeros", "eyebrow": "Pelliccia e colaboradores, 2002", "titulo": "O teste que não é exame: parar de treinar",
          "numeros": [{"n": "−15%", "x": "espessura da parede; voltou ao normal em todos", "cor": "petr"},
                      {"n": "−7%", "x": "cavidade", "cor": "tinta"},
                      {"n": "22%", "x": "mantiveram cavidade de 60 mm ou mais", "cor": "ambar"}],
          "destaque": "40 atletas, 1 a 13 anos sem treinar. Na clínica, 8 a 12 semanas e regressão parcial: a última carta, porque custa uma temporada.",
          "destaque_cor": "ambar", "fonte": "Circulation 2002"})

# 9. onda T
S.append({"id": "ondat", "tipo": "duas", "eyebrow": "Sheikh e colaboradores, 2018", "titulo": "A localização da onda T muda tudo",
          "esq": {"t": "Variante descrita", "cor": "petr",
                  "itens": ["anterior, V1 a V4", "em atleta negro", "com elevação do ponto J", "e ST abaulado, “em domo”"]},
          "dir": {"t": "Investiga sempre", "cor": "verm",
                  "itens": ["inferior e lateral", "em qualquer atleta", "associação real com cardiomiopatia"]},
          "destaque": "100 atletas com T invertida e eco normal: cardiomiopatia em 21% (30% nos brancos, 12% nos negros). Investigação negativa não é alta; é seguimento.",
          "destaque_cor": "verm", "fonte": "Circulation 2018"})

# 10. aritmética
S.append({"id": "aritmetica", "tipo": "numeros", "eyebrow": "Basavarajaiah e colaboradores, 2008", "titulo": "Por que o falso-positivo é a regra",
          "numeros": [{"n": "3.500", "x": "atletas de elite sem sintoma", "cor": "tinta"},
                      {"n": "53", "x": "com parede de 13 a 16 mm (1,5%)", "cor": "ambar"},
                      {"n": "3", "x": "compatíveis com cardiomiopatia hipertrófica (0,08%)", "cor": "verm"}],
          "destaque": "Achado não é afastamento automático. Mas o falso-negativo mata: síncope no esforço, sintoma no esforço e história familiar passam por cima de qualquer número.",
          "destaque_cor": "verm", "fonte": "JACC 2008"})

# 11. três laudos
S.append({"id": "condutas", "tipo": "tabela", "eyebrow": "Os três laudos do começo", "titulo": "O que a aula permite dizer",
          "cab": ["Perfil", "Onde está", "Conduta"],
          "larguras": [22, 30, 48],
          "linhas": [["Zagueiro, 13 mm", "entrada da zona cinzenta", "avaliação cardiológica completa; nem proibir nem “relaxa”"],
                     ["Triatleta, 59 mm", "comum em endurance", "com função normal e sem sintoma: provável adaptação, com seguimento"],
                     ["Adolescente, T anterior", "variante descrita", "eco e seguimento; investiga se sintoma, família ou T inferolateral"]],
          "destaque": "O cansaço da triatleta continua precisando de explicação: carga, sono, ferro, alimentação.",
          "destaque_cor": "petr"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Cinco regras da zona cinzenta", "titulo": "Antes de “é normal?”, pergunte “normal para quem?”",
          "regras": ["Número isolado não diagnostica; quem é a pessoa muda o número",
                     "Função e sintoma pesam mais que milímetro",
                     "Achado não é afastamento nem alta: é investigação e seguimento"],
          "cards": [{"t": "Médico", "x": "Decide elegibilidade; na zona cinzenta, cardiologista com experiência em atleta."},
                    {"t": "Educador físico e preparador", "x": "Carga durante a investigação, com o médico."},
                    {"t": "Todos", "x": "Nem banalizar nem dramatizar; uma voz alinhada com clube e família."}],
          "quem": "Decidir inclui marcar o retorno."})

spec = {"arquivo": "aulas/MOD06/06-03-coracao-de-atleta-versus-cardiopatia.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Coração de atleta versus cardiopatia", "subtitulo": "Os números da zona cinzenta",
        "nota_capa": "Entra pelos três laudos.",
        "secoes": {"laudos": ["Os laudos e o que o treino faz.", "capa"],
                   "parede": ["Parede, cavidade e para quem.", "parede"],
                   "discriminadores": ["Discriminadores, destreino e onda T.", "discriminadores"],
                   "aritmetica": ["A aritmética e os três laudos.", "aritmetica"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-03.json"), "w"), ensure_ascii=False, indent=1)
print("06-03.json:", len(S), "slides")
