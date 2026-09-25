"""Spec do deck 6.1. Gera 06-01.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o caso
S.append({"id": "caso", "tipo": "frase", "fundo": "tinta", "eyebrow": "Caso ilustrativo",
          "frase": "Na matrícula, ele marcou “não” para problema de saúde. Porque não sabia que tinha.",
          "apoio": "Vinte anos parado, aula de alta intensidade na segunda semana, aperto no peito na terceira série. Depois: pressão alta sem tratamento, colesterol nunca dosado, trinta anos de cigarro, pai morto de infarto aos 52. Ninguém tinha perguntado."})

# 2. as duas frases
S.append({"id": "paradoxo", "tipo": "duas", "eyebrow": "Franklin e colaboradores, 2020", "titulo": "As duas frases são verdade",
          "esq": {"t": "No esforço", "cor": "verm",
                  "itens": ["o risco de morte súbita e infarto sobe", "de forma transitória", "mais em quem é menos ativo"]},
          "dir": {"t": "Na vida", "cor": "petr",
                  "itens": ["o risco absoluto é pequeno", "a atividade habitual reduz eventos", "o saldo favorece a proteção"]},
          "destaque": "A avaliação não serve para assustar nem para impedir. Serve para achar quem precisa de uma entrada diferente.",
          "destaque_cor": "tinta", "fonte": "Associação Americana do Coração · Circulation 2020"})

# 3. três perguntas
S.append({"id": "modelo", "tipo": "lista", "eyebrow": "Riebe e colaboradores, 2015", "titulo": "Etapa um: três perguntas, não a idade",
          "itens": [{"t": "Já pratica exercício regular?", "x": "planejado, ao menos moderado, 30 min, 3 vezes por semana, nos últimos 3 meses", "cor": "petr"},
                    {"t": "Tem doença ou sintoma?", "x": "cardiovascular, metabólica ou renal conhecida; ou sinais e sintomas sugestivos", "cor": "verm"},
                    {"t": "Que intensidade pretende?", "x": "leve, moderada ou vigorosa", "cor": "ambar"}],
          "destaque": "O modelo anterior mandava gente demais ao médico. O rastreio cauteloso demais tira mais gente do exercício do que salva de evento.",
          "destaque_cor": "tinta", "gap_itens": 22, "fonte": "Colégio Americano de Medicina do Esporte · Medicine & Science in Sports & Exercise 2015"})

# 4. as saídas
S.append({"id": "saidas", "tipo": "tabela", "eyebrow": "As saídas do modelo", "titulo": "Quem precisa de liberação médica",
          "cab": ["", "Sem doença, sem sintoma", "Doença conhecida, sem sintoma", "Sinal ou sintoma"],
          "larguras": [16, 28, 30, 26],
          "linhas": [["Não pratica", "não precisa; leve a moderado, progride", "recomendada antes de começar", "recomendada antes de começar"],
                     ["Já pratica", "não precisa; segue e progride", "moderado sem; vigoroso com liberação", "para e avalia"]],
          "destaque": "Perguntar sobre doença e sintoma é de todos. Investigar o que a pergunta achar é do médico. PAR-Q+: melhor que o formulário de uma linha.",
          "destaque_cor": "petr"})

# 5. A e B
p = [svg_abre(1664, 300, "Duas perguntas, é seguro e por que não adapta, e a ordem da entrevista do neutro para o íntimo"),
     "<defs>" + seta_marker("o1", MUDO) + "</defs>"]
rs = []
p.append(caixa(0, 0, 800, 110, FOSF, FOSF_T, esp=3))
p.append(caixa(864, 0, 800, 110, AZUL, AZUL_T, esp=3))
rs += [rot(24, 20, "A: é seguro?", w=752, tam=34, cor=FOSF, peso=700),
       rot(24, 66, "rastreio de risco: esta aula e a próxima", w=752, tam=26, cor=TINTA),
       rot(888, 20, "B: por que não adapta?", w=752, tam=34, cor=AZUL, peso=700),
       rot(888, 66, "sono, energia, carga, medicação, substância", w=752, tam=26, cor=TINTA)]
ordem = ["treino", "sono", "energia e comida", "trabalho e vida", "saúde e substâncias"]
for i, t in enumerate(ordem):
    x = i * 338
    fundo = FOSF_T if i == 4 else CARTAO
    cor = FOSF if i == 4 else TINTA
    p.append(caixa(x, 180, 300, 90, cor, fundo, esp=2, rx=10))
    rs.append(rot(x + 10, 206, t, w=280, tam=28, cor=cor, peso=600, alinha="center"))
    if i < 4:
        p.append(f'<line x1="{x+304}" y1="225" x2="{x+334}" y2="225" stroke="{MUDO}" stroke-width="4" marker-end="url(#o1)"/>')
p.append("</svg>")
rs.append(rot(0, 140, "a ordem: do neutro para o íntimo", w=800, tam=24, cor=MUDO, peso=600))
S.append({"id": "anamnese", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Etapa dois: a anamnese dirigida", "titulo": "Duas perguntas, uma entrevista com ordem",
          "destaque": "Quem abre perguntando o que a pessoa toma não tem anamnese; tem um formulário preenchido.",
          "destaque_cor": "tinta"})

# 6. três perguntas de fechamento
S.append({"id": "fechamento", "tipo": "cards", "por_linha": 3, "eyebrow": "Rendem mais do que parecem", "titulo": "Três perguntas que quase ninguém faz",
          "cards": [{"t": "“O que mudou nos últimos seis meses?”", "x": "trabalho, sono, peso, medicação, vida", "cor": "petr"},
                    {"t": "“Já parou alguma atividade por causa de um sintoma?”", "x": "acha quem se adaptou ao próprio limite", "cor": "ambar"},
                    {"t": "“Toma alguma coisa por conta própria?”", "x": "estimulante, pré-treino, emagrecedor, anabolizante", "cor": "verm"}],
          "destaque": "Na primeira consulta, o que decide segurança: sintoma, doença, história familiar, medicação e substância. O resto melhora com vínculo.",
          "destaque_cor": "tinta"})

# 7. sintomas
S.append({"id": "sintomas", "tipo": "lista", "eyebrow": "Etapa três: para as seis profissões", "titulo": "Os sinais que interrompem tudo",
          "itens": [{"t": "Desconforto no peito no esforço", "x": "aperto, peso, queimação; quem nega “dor” descreve outra coisa", "cor": "verm"},
                    {"t": "Síncope durante o esforço", "x": "bandeira vermelha máxima: não treina até ser avaliado", "cor": "verm"},
                    {"t": "Falta de ar desproporcional", "x": "ou em repouso, ou ao deitar", "cor": "ambar"},
                    {"t": "Palpitação com tontura, falta de ar ou desmaio", "x": "isolada é comum; com sintoma, não", "cor": "ambar"},
                    {"t": "Queda de tolerância sem explicação", "x": "acima dos 40, coronária se disfarça de “fora de forma”", "cor": "ambar"},
                    {"t": "Inchaço, falta de ar ao deitar, acordar sem ar", "x": "o conjunto da insuficiência cardíaca", "cor": "ambar"}],
          "gap_itens": 10})

# 8. história
S.append({"id": "historia", "tipo": "cards", "por_linha": 3, "eyebrow": "O que precisa estar na ficha", "titulo": "História familiar, fatores de risco, substâncias",
          "cards": [{"t": "História familiar", "x": "morte súbita, cardiopatia hereditária; coronária precoce: antes dos 55 no homem, antes dos 65 na mulher, em parente de primeiro grau", "cor": "verm"},
                    {"t": "Fatores de risco", "x": "pressão alta, diabetes, colesterol, tabagismo, obesidade abdominal, doença renal", "cor": "ambar"},
                    {"t": "Medicações e substâncias", "x": "inclusive as de conta própria", "cor": "petr"}],
          "destaque": "“Não sei” é resposta clínica: não é “não”, é motivo para medir a pressão ali mesmo.",
          "destaque_cor": "tinta"})

# 9. perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "Etapa quatro: perfis típicos", "titulo": "O que fazer com o que se achou",
          "cab": ["Perfil", "O que decide", "Entrada"],
          "larguras": [26, 38, 36],
          "linhas": [["Jovem sem sintoma", "sem história familiar", "leve a moderado sem liberação; progressão"],
                     ["Meia-idade voltando", "fatores de risco, sintoma, intensidade", "conta do risco pelo médico; entrada gradual"],
                     ["Doença crônica compensada", "quem prescreve e como monitora", "exercício é tratamento, com critério"],
                     ["Atleta federado", "exigência da federação ou do evento", "outro sistema, outra lógica"]],
          "destaque": "Doença cardiovascular estabelecida não é, em geral, contraindicação ao exercício. É indicação de exercício prescrito com critério.",
          "destaque_cor": "petr"})

# 10. três saídas
S.append({"id": "tres_saidas", "tipo": "cards", "por_linha": 3, "eyebrow": "Quase nunca é tudo ou nada", "titulo": "Três saídas",
          "cards": [{"t": "Libera com progressão", "x": "a maioria", "cor": "petr"},
                    {"t": "Libera com restrição enquanto investiga", "x": "a mais subutilizada: caminhar enquanto espera o cardiologista", "cor": "ambar"},
                    {"t": "Suspende até avaliar", "x": "sintoma de alerta e instabilidade", "cor": "verm"}],
          "destaque_cor": "tinta"})

# 11. registro
S.append({"id": "registro", "tipo": "duas", "eyebrow": "O registro", "titulo": "O que não está escrito não aconteceu",
          "esq": {"t": "Em uma página", "cor": "petr",
                  "itens": ["as três perguntas do modelo", "sintomas, com o que foi negado", "história familiar, com idade e evento", "fatores de risco, medicações, substâncias", "conduta, data e orientação dada"]},
          "dir": {"t": "Dois erros", "cor": "verm",
                  "itens": ["“sem alterações” sem dizer o que se perguntou", "não registrar a recusa, nem a orientação"]},
          "destaque": "O formulário de matrícula de uma linha é documento de defesa, não instrumento clínico. Trocá-lo custa cinco minutos por aluno.",
          "destaque_cor": "tinta"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Três perguntas teriam bastado", "titulo": "A avaliação serve para permitir com segurança",
          "regras": ["O critério não é a idade: o que faz, tem, sente e pretende fazer",
                     "Síncope durante o esforço interrompe tudo até ser avaliada",
                     "Escreva o que perguntou, o que foi negado e o que orientou"],
          "cards": [{"t": "Médico", "x": "Libera, investiga, diagnostica, trata."},
                    {"t": "Educador físico e preparador", "x": "Progride a carga; reconhece o sintoma no treino."},
                    {"t": "Fisioterapeuta e nutricionista", "x": "Fazem as mesmas perguntas, com frequência."}],
          "quem": "Perguntar é da sua profissão, qualquer que seja ela."})

spec = {"arquivo": "aulas/MOD06/06-01-avaliacao-pre-participacao-estrutura-e-anamnese.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Avaliação pré-participação", "subtitulo": "Estrutura, anamnese dirigida e decisão",
        "nota_capa": "Entra pelo caso ilustrativo.",
        "secoes": {"caso": ["O caso, o paradoxo e o modelo.", "capa"],
                   "anamnese": ["A anamnese e os sinais.", "anamnese"],
                   "perfis": ["O que fazer, e o registro.", "perfis"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-01.json"), "w"), ensure_ascii=False, indent=1)
print("06-01.json:", len(S), "slides")
