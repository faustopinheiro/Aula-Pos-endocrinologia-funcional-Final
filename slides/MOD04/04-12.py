"""Spec do deck 4.12. Gera 04-12.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. disciplina ou sintoma
S.append({"id": "disciplina", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ambiguidade que o esporte cria",
          "frase": "Disciplina ou sintoma?",
          "apoio": "Pesar toda a comida, controlar com rigidez, treinar doente, buscar o menor percentual possível, resistir à fome. Fora do esporte, alerta. Dentro, elogio. As ferramentas das onze aulas são as mesmas; muda a relação da pessoa com elas."})

# 2. três números
S.append({"id": "fatos", "tipo": "numeros", "eyebrow": "Sundgot-Borgen e Torstveit, 2004 · Arcelus, 2011", "titulo": "Mais comum no esporte, e grave",
          "numeros": [{"n": "13,5%", "x": "dos atletas de elite com transtorno alimentar, contra 4,6% na população geral", "cor": "verm"},
                      {"n": "20% e 8%", "x": "nas atletas mulheres e nos atletas homens", "cor": "ambar"},
                      {"n": "5,9 ×", "x": "mortalidade na anorexia nervosa; uma em cada cinco mortes por suicídio", "cor": "tinta"}],
          "destaque": "A concentração foi maior nos esportes em que o peso ou a magreza pesam no resultado.",
          "destaque_cor": "petr", "fonte": "Clinical Journal of Sport Medicine 2004 · Archives of General Psychiatry 2011"})

# 3. o espectro e os quatro passos
p = [svg_abre(1664, 330, "Espectro contínuo da alimentação organizada à alimentação desordenada e ao transtorno alimentar; embaixo, quatro passos: reconhecer, perguntar, abordar, encaminhar"),
     "<defs>" + seta_marker("e1", MUDO) + '<linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="' + OXID_T + '"/><stop offset="0.5" stop-color="' + GLIC_T + '"/><stop offset="1" stop-color="' + FOSF_T + '"/></linearGradient></defs>',
     f'<rect x="0" y="20" width="1664" height="90" rx="10" fill="url(#g1)" stroke="{BORDA}" stroke-width="2"/>']
rs = [rot(20, 48, "alimentação organizada", w=500, tam=28, cor=OXID, peso=700),
      rot(582, 48, "alimentação desordenada", w=500, tam=28, cor=GLIC, peso=700, alinha="center"),
      rot(1144, 48, "transtorno alimentar", w=500, tam=28, cor=FOSF, peso=700, alinha="right")]
for i, t in enumerate(["reconhecer", "perguntar", "abordar", "encaminhar"]):
    x = i * 420
    p.append(caixa(x, 180, 360, 110, AZUL, AZUL_T, esp=3))
    rs.append(rot(x, 200, f"{i+1}", w=360, tam=28, cor=AZUL, peso=700, alinha="center"))
    rs.append(rot(x, 238, t, w=360, tam=30, cor=TINTA, peso=700, alinha="center"))
    if i < 3:
        p.append(f'<line x1="{x+366}" y1="235" x2="{x+410}" y2="235" stroke="{MUDO}" stroke-width="4" marker-end="url(#e1)"/>')
p.append("</svg>")
S.append({"id": "espectro", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um espectro, sem fronteira nítida", "titulo": "Sofrimento e prejuízo importam mais que o critério",
          "destaque": "Tratar não é um dos passos: é trabalho de equipe especializada. Reconhecer é de todos, e o esporte vê a pessoa, o corpo e, às vezes, o prato.",
          "destaque_cor": "tinta"})

# 4. reconhecer
S.append({"id": "reconhecer", "tipo": "cards", "por_linha": 4, "eyebrow": "Passo um · reconhecer", "titulo": "Muito disso é observável",
          "cards": [{"t": "O que se vê", "x": "perda ou oscilação de peso, roupa larga no calor, frio constante, fratura por estresse repetida", "cor": "petr"},
                    {"t": "O que se observa", "x": "evitar comer com o grupo, banheiro após refeições, rituais, excluir grupos, treinar doente", "cor": "ambar"},
                    {"t": "O que se ouve", "x": "“fui bem”, “estraguei tudo”, comida limpa e suja, merecer, compensar", "cor": "verm"},
                    {"t": "O que o exame mostra", "x": "bradicardia com sintomas, hipotensão, eletrólitos, ciclo ausente, osso baixo", "cor": "tinta"}],
          "destaque": "O vocabulário moral sobre comida é o sinal mais barato e mais subestimado.",
          "destaque_cor": "verm"})

# 5. duas observações
S.append({"id": "observacoes", "tipo": "duas", "eyebrow": "Dois erros comuns", "titulo": "O homem musculoso e a energia que falta",
          "esq": {"t": "No homem, outra apresentação", "cor": "ambar",
                  "itens": ["o corpo parece pequeno: dismorfia muscular", "espelho, dieta ritualizada, treino acima de tudo",
                            "anabolizante com frequência importante", "chega por lesão, dor ou platô"]},
          "dir": {"t": "Baixa disponibilidade não é transtorno", "cor": "petr",
                  "itens": ["pode ser não intencional: tempo, apetite, informação", "ou intencional e ligada a um transtorno",
                            "mesma fisiologia, condutas opostas"]},
          "destaque": "O ambiente elogia a dismorfia muscular, e o corpo não denuncia. O passo dois é o que separa as duas colunas da direita.",
          "destaque_cor": "tinta"})

# 6. perguntar
S.append({"id": "perguntar", "tipo": "duas", "eyebrow": "Passo dois · Morgan, Reid e Lacey, 1999 · Martinsen, 2014", "titulo": "Por que você come pouco?",
          "esq": {"t": "Logística", "cor": "petr",
                  "itens": ["não dá tempo, sem fome de manhã, não sei o que comer", "nutrição e organização do dia", "aumentar a ingestão resolve"]},
          "dir": {"t": "Outra coisa", "cor": "verm",
                  "itens": ["medo de engordar, culpa, regras, compensação", "“coma mais” pode aumentar a angústia", "cuidar da relação com a comida"]},
          "destaque": "SCOFF: cinco perguntas, dois “sim” pedem avaliação. BEDA-Q: feito para atletas. Rastreio não é diagnóstico, e falha no homem com dismorfia: quanto tempo por dia você pensa no seu corpo?",
          "destaque_cor": "ambar", "fonte": "BMJ 1999 · Medicine and Science in Sports and Exercise 2014"})

# 7. abordar
S.append({"id": "abordar", "tipo": "duas", "eyebrow": "Passo três · abordar", "titulo": "A lista do que não fazer pesa tanto quanto a outra",
          "esq": {"t": "Fazer", "cor": "petr",
                  "itens": ["em particular, com tempo", "começar pelo funcional: frio, cargas que caíram", "nomear a preocupação, não o diagnóstico", "manter o vínculo, mesmo com recusa"]},
          "dir": {"t": "Não fazer", "cor": "verm",
                  "itens": ["comentar o corpo, nem para elogiar", "pesar em público; medir sem indicação", "prescrever restrição; comida como prêmio", "prometer sigilo absoluto a menor em risco"]},
          "destaque": "A pressão também está na regra da modalidade. Uma conversa com técnicos e pais alcança mais atletas do que um ano de consultório.",
          "destaque_cor": "tinta"})

# 8. encaminhar
S.append({"id": "encaminhar", "tipo": "duas", "eyebrow": "Passo quatro · encaminhar", "titulo": "Duas portas",
          "esq": {"t": "Agora", "cor": "verm",
                  "itens": ["desmaio ou quase desmaio", "bradicardia com sintomas, hipotensão ao levantar", "vômitos frequentes, perda de peso rápida, confusão", "qualquer sinal de risco de suicídio"]},
          "dir": {"t": "Com calma", "cor": "petr",
                  "itens": ["psicólogo e médico com experiência em transtorno alimentar", "nutricionista da mesma rede", "ajudar a marcar: um nome num papel não acontece", "menor de idade: a família entra"]},
          "destaque": "Na porta de agora, interromper a atividade e levar ao médico hoje, não na semana que vem.",
          "destaque_cor": "verm"})

# 9. caso ilustrativo
S.append({"id": "caso", "tipo": "lista", "eyebrow": "Caso ilustrativo", "titulo": "A apresentação que mais escapa",
          "itens": [{"t": "Primeira consulta", "x": "24 anos, musculação há sete anos, dor no ombro há cinco meses, nenhum treino perdido", "cor": "tinta"},
                    {"t": "Ao longo das semanas", "x": "exercício adaptado, nunca reduzido; o casamento do primo perdido; as mesmas refeições; fotos diárias; ainda se achava pequeno", "cor": "ambar"},
                    {"t": "A pergunta direta, sem julgamento", "x": "terceiro ciclo de anabolizante do ano, orientado na academia", "cor": "verm"},
                    {"t": "A conduta, lenta", "x": "vínculo; conversa funcional sobre o casamento; psicólogo e médico; treino redesenhado mantendo a frequência", "cor": "petr"}],
          "gap_itens": 18})

# 10. decisão e contribuição
S.append({"id": "niveis", "tipo": "tabela", "eyebrow": "O módulo nos três níveis", "titulo": "Decisão e contribuição",
          "cab": ["Quem", "Decide", "Contribui com"],
          "larguras": [26, 36, 38],
          "linhas": [["Nutricionista", "plano, quantidades, periodização, estratégia de prova", "o que a pessoa excluiu, e por quê"],
                     ["Médico", "exame, reposição, medicação, afastamento", "a ferritina baixa que volta como pergunta"],
                     ["Educador e preparador físico", "a carga que decide o que se perde", "a taxa de suor; a carga que caiu com a dieta"],
                     ["Fisioterapeuta", "tecido e fratura em recuperação", "a segunda fratura leva a pergunta sobre energia"],
                     ["Psicólogo", "alimentação desordenada, com o médico", "a restrição de origem comportamental"]],
          "destaque": "O treinador que organiza o kit da viagem garante que o plano chegue ao ônibus.",
          "destaque_cor": "tinta"})

# 11. reconhecimento
S.append({"id": "todos", "tipo": "cards", "por_linha": 3, "eyebrow": "O terceiro nível é de todos", "titulo": "Reconhecer exige ter aprendido o sinal",
          "cards": [{"t": "O que se ouve", "x": "vocabulário moral; exclusão sem razão clínica; parar de comer com o grupo", "cor": "tinta"},
                    {"t": "O que o corpo mostra", "x": "frio constante; ciclo que espaçou; fratura que se repete", "cor": "tinta"},
                    {"t": "O que o treino mostra", "x": "rendimento que cai com o treino mantido", "cor": "tinta"},
                    {"t": "O que a prova mostra", "x": "peso que sobe na prova longa; cãibra atribuída ao sal", "cor": "ambar"},
                    {"t": "O que o espelho esconde", "x": "o atleta muito musculoso que se acha pequeno", "cor": "ambar"},
                    {"t": "A porta de agora", "x": "desmaio, instabilidade, vômitos frequentes, risco de suicídio", "cor": "verm"}]})

# 12. fecho do módulo
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que atravessou as doze aulas", "titulo": "Uma pergunta antes de um número",
          "regras": ["Quase todo problema começa por falta: de energia, de variedade, de organização ou de informação certa",
                     "A mesma ferramenta, na pessoa errada, vira sintoma",
                     "Quem pergunta por que antes de calcular quanto erra menos"],
          "cards": [{"t": "Decisão", "x": "De quem tem a profissão para ela."},
                    {"t": "Contribuição", "x": "A informação que passa de uma profissão para outra."},
                    {"t": "Reconhecimento", "x": "De todos."}],
          "quem": "No próximo módulo, suplementos e ergogênicos: evidência, marketing, risco e antidoping."})

spec = {"arquivo": "aulas/MOD04/04-12-alimentacao-desordenada-sinais-rastreio-e-encaminhamento.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Alimentação desordenada no esporte", "subtitulo": "Sinais, rastreio e encaminhamento",
        "nota_capa": "Entra por disciplina ou sintoma. Fecha o módulo.",
        "secoes": {"disciplina": ["A ambiguidade, os números e o espectro.", "capa"],
                   "reconhecer": ["Reconhecer, perguntar, abordar e encaminhar.", "reconhecer"],
                   "caso": ["O caso ilustrativo e o módulo nos três níveis.", "caso"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-12.json"), "w"), ensure_ascii=False, indent=1)
print("04-12.json:", len(S), "slides")
