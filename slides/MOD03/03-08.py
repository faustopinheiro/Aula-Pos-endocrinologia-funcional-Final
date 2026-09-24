"""Spec do deck 3.8. Gera 03-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def seta(x1, y1, x2, y2, cor, mid, esp=5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mid})"/>'

# 1. régua do espectro
p = [svg_abre(1664, 330, "Espectro em três faixas: overreaching funcional, com volta em dias; não funcional, em semanas a meses; síndrome do overtraining, em vários meses a anos")]
faixas = [("Overreaching funcional", "dias, raramente semanas", OXID, OXID_T), ("Overreaching não funcional", "semanas, às vezes meses", GLIC, GLIC_T),
          ("Síndrome do overtraining", "vários meses a anos", FOSF, FOSF_T)]
rs = []
for i, (nome, tempo, cor, fundo) in enumerate(faixas):
    x = i * 560
    p.append(f'<rect x="{x}" y="60" width="544" height="120" rx="10" fill="{fundo}" stroke="{cor}" stroke-width="4"/>')
    rs.append(rot(x, 80, nome, w=544, tam=30, cor=cor, peso=700, alinha="center"))
    rs.append(rot(x, 200, "volta em", w=544, tam=24, cor=MUDO, alinha="center"))
    rs.append(rot(x, 236, tempo, w=544, tam=32, cor=TINTA, peso=700, alinha="center", serif=True))
p.append(f'<line x1="0" y1="42" x2="1664" y2="42" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs.append(rot(0, 0, "mais grave →", w=1664, tam=24, cor=MUDO, alinha="right"))
S.append({"id": "espectro", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "“Eu estou em overtraining”", "titulo": "A diferença não é o sintoma; é o tempo de volta",
          "destaque": "A síndrome é diagnóstico de exclusão.", "destaque_cor": "verm",
          "fonte": "Meeusen e colaboradores, consenso ECSS e ACSM, Medicine and Science in Sports and Exercise 2013"})

# 2. diagnóstico retrospectivo
S.append({"id": "retro", "tipo": "frase", "fundo": "tinta", "eyebrow": "A coisa mais importante da aula",
          "frase": "O diagnóstico é retrospectivo.",
          "apoio": "Na consulta há uma pessoa cansada, com desempenho caindo. Não há como saber, naquele dia, se ela volta em dez dias ou em dez meses. A boa notícia: a primeira conduta é parecida nos três."})

# 3. funcional x real
t = list(range(0, 43))
def curva(m, real):
    if m < 7: return 100
    if m < 21: return 100 - 8 * (1 - math.exp(-(m - 7) / 4))
    if not real:
        return 92 + 13 * (1 - math.exp(-(m - 21) / 4))
    return 92 - 5 * (1 - math.exp(-(m - 21) / 6))
svg, rs = linhas(1664, 380, "Duas curvas de desempenho: no atleta com margem, a queda da sobrecarga é seguida de descarga e o desempenho sobe acima da base; no atleta sem margem, a semana seguinte é igual e o desempenho não volta",
                 [{"nome": "", "cor": OXID, "pts": [(m, curva(m, False)) for m in t]}, {"nome": "", "cor": FOSF, "pts": [(m, curva(m, True)) for m in t], "tracejado": True}],
                 0, 42, 80, 110, [(0, "base"), (7, "sobrecarga"), (21, "descarga?"), (42, "6 semanas")], [],
                 margem=(20, 30, 60, 20))
rs += [rot(1180, 16, "com margem: supercompensa", w=480, tam=28, cor=OXID, peso=700),
       rot(1180, 272, "sem margem: não volta", w=480, tam=28, cor=FOSF, peso=700)]
S.append({"id": "funcional", "tipo": "diagrama", "h": 380, "svg": svg, "rotulos": rs,
          "eyebrow": "Overreaching funcional", "titulo": "Ferramenta de atleta com margem",
          "destaque": "Planejado, curto e seguido de descarga real. Em quem trabalha doze horas e dorme cinco, é um empréstimo que não tem como pagar.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos"})

# 4. critério do consenso
S.append({"id": "criterio", "tipo": "cards", "por_linha": 3, "eyebrow": "O que existe como critério", "titulo": "Cada palavra carrega trabalho",
          "cards": [{"t": "Queda de desempenho", "x": "pressupõe um “antes” medido", "cor": "tinta"},
                    {"t": "Inexplicada", "x": "obriga o diferencial", "cor": "verm"},
                    {"t": "Apesar de repouso adequado", "x": "carga bem reduzida por semanas", "cor": "tinta"},
                    {"t": "Com sintomas", "x": "fadiga, sono, humor, apetite, infecções", "cor": "tinta"},
                    {"t": "Outras causas afastadas", "x": "diagnóstico de exclusão", "cor": "verm"},
                    {"t": "Nenhum exame", "x": "nenhum hormônio, nenhuma razão entre marcadores", "cor": "ambar"}],
          "fonte": "Meeusen e colaboradores, consenso ECSS e ACSM 2013"})

# 5. por que não existe o exame
S.append({"id": "exame", "tipo": "duas", "eyebrow": "Urhausen e Kindermann, 2002", "titulo": "“Que ferramentas diagnósticas nós temos?”",
          "esq": {"t": "A resposta", "cor": "verm",
                  "itens": ["muitas publicações sobre o tema", "poucos instrumentos válidos", "mais de vinte anos depois, mudou pouco"]},
          "dir": {"t": "O porquê", "cor": "tinta",
                  "itens": ["validar exige medir antes do quadro", "o padrão-ouro é retrospectivo",
                            "dois testes com 4 horas: protocolo de pesquisa hormonal"]},
          "destaque": "Painel que “diagnostica overtraining” vende o que não existe. Relação testosterona-cortisol: reconhecer, não decidir.",
          "destaque_cor": "ambar", "fonte": "Sports Medicine 2002 · Meeusen e colaboradores 2013"})

# 6. instrumentos
S.append({"id": "instrumentos", "tipo": "cards", "eyebrow": "O que funciona", "titulo": "Três instrumentos, nenhum de sangue",
          "cards": [{"t": "Teste padronizado repetido", "x": "mesmo percurso ou carga, mesma condição; a sessão de sábado depois da de sexta", "cor": "petr"},
                    {"t": "Esforço para carga fixa", "x": "mesma carga, percepção subindo por semanas", "cor": "petr"},
                    {"t": "Humor e recuperação", "x": "questionários validados: mais fadiga, menos vigor", "cor": "petr"}],
          "destaque": "E o que vale mais que os três: o histórico de carga escrito. Às vezes a carga não mudou. Mudou a vida.",
          "destaque_cor": "tinta"})

# 7. Saw 2016
S.append({"id": "subjetivo", "tipo": "duas", "eyebrow": "Saw, Main e Gastin, 2016", "titulo": "A pergunta bem feita supera o exame",
          "esq": {"t": "Medidas subjetivas", "cor": "petr",
                  "itens": ["bem-estar, sono percebido", "dor muscular, estresse, humor", "responderam à carga de forma mais sensível e consistente"]},
          "dir": {"t": "Objetivas habituais", "cor": "tinta",
                  "itens": ["frequência cardíaca de repouso", "marcadores de sangue", "responderam menos"]},
          "destaque": "O problema não é que falte instrumento. É que o instrumento que funciona não parece instrumento.",
          "destaque_cor": "petr", "fonte": "British Journal of Sports Medicine 2016 · revisão sistemática de estudos com as duas medidas em paralelo"})

# 8. escada
degraus = ["esforço sobe", "sono muda", "humor e vigor caem", "motivação cai",
           "dores difusas", "mais infecções", "desempenho cai"]
p = [svg_abre(1664, 470, "Escada de sete degraus: do sinal mais precoce, o esforço para carga conhecida, até o mais tardio, a queda de desempenho")]
rs = []
for i, d in enumerate(degraus):
    x = i * 230
    y = 400 - (i + 1) * 54
    cor = FOSF if i == 6 else (OXID if i == 0 else AZUL)
    fundo = FOSF_T if i == 6 else (OXID_T if i == 0 else AZUL_T)
    p.append(f'<rect x="{x}" y="{y}" width="220" height="{400 - y}" rx="8" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
    rs.append(rot(x + 8, y + 10, d, w=204, tam=24, cor=TINTA, peso=600, lh=1.2))
p.append(f'<path d="M0 430 H{6*230-10}" stroke="{OXID}" stroke-width="4"/>')
p.append("</svg>")
rs.append(rot(0, 438, "seis degraus que se colhem com perguntas", w=1380, tam=26, cor=OXID, peso=700, alinha="center"))
rs.append(rot(1380, 438, "tardio", w=220, tam=26, cor=FOSF, peso=700, alinha="center"))
S.append({"id": "escada", "tipo": "diagrama", "h": 480, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que muda antes", "titulo": "Quando o desempenho cai, você já está atrasado",
          "fonte": "Ordem aproximada da prática, não sequência medida em estudo · os seis primeiros são inespecíficos: não dispensam o diferencial"})

# 9. saídas A e B
S.append({"id": "saidas", "tipo": "duas", "eyebrow": "A encruzilhada", "titulo": "Manter a carga, ou reduzir e reavaliar",
          "esq": {"t": "A: manter, como se fosse funcional", "cor": "verm",
                  "itens": ["só com sobrecarga planejada e curta", "e descarga real que a vida permite cumprir",
                            "faltou uma: está fora"]},
          "dir": {"t": "B: o teste de descarga", "cor": "petr",
                  "itens": ["carga bem reduzida, não zerada", "frequência e alguma intensidade curta mantidas",
                            "2 a 3 semanas, marcadores anotados antes"]},
          "destaque": "Avise que os primeiros dias vão ser ruins. Sem aviso, a pessoa abandona no terceiro dia achando que precisava treinar mais.",
          "destaque_cor": "ambar"})

# 10. saída C e critério
S.append({"id": "criterioC", "tipo": "duas", "eyebrow": "Saída C e o critério", "titulo": "B e C em paralelo; A precisa ser justificada",
          "esq": {"t": "C: investigar antes de mexer", "cor": "verm",
                  "itens": ["perda de peso sem intenção, febre, suor noturno", "gânglios, falta de ar desproporcional, dor no peito",
                            "palpitação com sensação de desmaio, ideação suicida", "fadiga de meses sem mudança de carga"]},
          "dir": {"t": "Reavaliar em 4 a 6 semanas", "cor": "petr",
                  "itens": ["esforço na mesma sessão", "qualidade do sono", "vigor e motivação numa escala simples", "teste padronizado, com data"]},
          "destaque": "A primeira conduta é a mesma nos três estados, e reduzir carga não atrapalha investigação nenhuma.",
          "destaque_cor": "petr"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Cinco eixos na mesma direção", "titulo": "Uma decisão executada em cinco lugares",
          "regras": ["Cortisol sem voltar ao basal · gonadal suprimido · T3 baixo com TSH normal",
                     "IGF-1 baixo · sinais periféricos avisando escassez",
                     "A carga estava alta demais para o que essa pessoa podia sustentar naquele período"],
          "cards": [{"t": "Médico", "x": "Investiga causas; as bandeiras da saída C são o gatilho."},
                    {"t": "Preparador e educador físico", "x": "Ajustam a carga e montam a descarga: primeira linha."},
                    {"t": "Todo mundo", "x": "Reconhece os seis primeiros degraus da escada."}],
          "quem": "Entre o primeiro degrau e o sétimo está a janela em que isso ainda é barato de resolver."})

spec = {"arquivo": "aulas/MOD03/03-08-excesso-de-treinamento.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Excesso de treinamento", "subtitulo": "Overreaching funcional, não funcional e síndrome do overtraining",
        "nota_capa": "Entra pela frase “eu estou em overtraining”.",
        "secoes": {"espectro": ["O vocabulário e o diagnóstico retrospectivo.", "capa"],
                   "criterio": ["O que existe como critério, e o que não existe.", "criterio"],
                   "instrumentos": ["Os instrumentos que funcionam e a escada.", "instrumentos"],
                   "decisao": ["As três saídas e o fecho do módulo.", "saidas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-08.json"), "w"), ensure_ascii=False, indent=1)
print("03-08.json:", len(S), "slides")
