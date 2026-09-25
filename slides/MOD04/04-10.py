"""Spec do deck 4.10. Gera 04-10.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a regra
S.append({"id": "regra", "tipo": "frase", "fundo": "tinta", "eyebrow": "Perfil típico de primeira meia maratona",
          "frase": "Nada de novo no dia.",
          "apoio": "Massa com molho de creme na véspera, o gel do kit, um café mais forte para acordar. Nada era absurdo. Tudo era novo. E no quilômetro doze, a procura por um banheiro."})

# 2. cinco passos
p = [svg_abre(1664, 220, "Procedimento em cinco passos: dias antes, véspera e manhã, durante, entre esforços, o plano escrito"),
     "<defs>" + seta_marker("c1", MUDO) + "</defs>"]
rs = []
for i, t in enumerate(["dias antes", "véspera e manhã", "durante", "entre esforços", "o plano escrito"]):
    x = i * 340
    cor, f = (GLIC, GLIC_T) if i == 4 else (OXID, OXID_T)
    p.append(caixa(x, 40, 290, 140, cor, f, esp=3))
    rs.append(rot(x, 62, f"{i+1}", w=290, tam=34, cor=cor, peso=700, alinha="center"))
    rs.append(rot(x + 10, 112, t, w=270, tam=28, cor=TINTA, peso=700, alinha="center"))
    if i < 4:
        p.append(f'<line x1="{x+294}" y1="110" x2="{x+334}" y2="110" stroke="{MUDO}" stroke-width="4" marker-end="url(#c1)"/>')
p.append("</svg>")
S.append({"id": "passos", "tipo": "diagrama", "h": 220, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O procedimento", "titulo": "O roteiro do ensaio",
          "destaque": "Quantidades de carboidrato: aula de carboidrato. Hidratação e sódio: aula de hidratação. Aqui, a sequência, e o que só aparece em dia de prova: nervosismo, horário, intestino e logística.",
          "destaque_cor": "tinta"})

# 3. pergunta de corte
S.append({"id": "corte", "tipo": "duas", "eyebrow": "Passo um · Burke e colaboradores, 2011", "titulo": "A prova passa de noventa minutos contínuos?",
          "esq": {"t": "Não: 10 km, futebol, luta", "cor": "tinta",
                  "itens": ["sem sobrecarga de carboidrato", "alimentação habitual de treino", "o treino reduzido já enche o estoque"]},
          "dir": {"t": "Sim: maratona, ciclismo longo, triatlo", "cor": "petr",
                  "itens": ["10 a 12 g/kg por dia", "nas 36 a 48 horas antes", "com o treino reduzido"]},
          "destaque": "A conta, para 70 kg: 700 a 840 g de carboidrato por dia. Planejado em dois dias, não improvisado num jantar.",
          "destaque_cor": "ambar", "fonte": "Journal of Sports Sciences 2011"})

# 4. três ajustes
S.append({"id": "ajustes", "tipo": "lista", "eyebrow": "Como a sobrecarga cabe no prato", "titulo": "Três ajustes",
          "itens": [{"t": "Carboidrato de baixo volume", "x": "arroz branco, massa, pão, tapioca, batata sem casca, suco; não é o momento das fibras", "cor": "petr"},
                    {"t": "Trocar parte do prato", "x": "menos gordura e fibra para abrir espaço; não é comer mais de tudo", "cor": "ambar"},
                    {"t": "Avisar que a balança vai subir", "x": "glicogênio vem com água; quem não sabe corta a comida na véspera", "cor": "verm"}],
          "gap_itens": 26})

# 5. manhã de trás para a frente
p = [svg_abre(1664, 240, "Relógio lido de trás para a frente: acordar às 4h, comer às 4h15, sair às 5h30, chegar às 6h, largada às 7h"),
     "<defs>" + seta_marker("m1", MUDO) + "</defs>",
     f'<line x1="1620" y1="120" x2="40" y2="120" stroke="{MUDO}" stroke-width="4" marker-end="url(#m1)"/>']
rs = []
marcos = [("7h", "largada", FOSF), ("6h", "chegar", TINTA), ("5h30", "sair de casa", TINTA), ("4h15", "comer", OXID), ("4h", "acordar", TINTA)]
for i, (h, t, c) in enumerate(marcos):
    x = 1480 - i * 340
    p.append(f'<circle cx="{x+60}" cy="120" r="16" fill="{c}"/>')
    rs.append(rot(x - 90, 40, h, w=300, tam=38, cor=c, peso=700, alinha="center"))
    rs.append(rot(x - 90, 160, t, w=300, tam=28, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
S.append({"id": "manha", "tipo": "diagrama", "h": 240, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo dois · véspera e manhã", "titulo": "A conta de trás para a frente",
          "destaque": "Véspera: jantar conhecido, pouca fibra, gordura, gás e álcool. Manhã: se o nervosismo tira a fome, opção líquida, ensaiada. Cafeína: a dose do treino, nunca mais forte.",
          "destaque_cor": "petr"})

# 6. intestino
S.append({"id": "intestino", "tipo": "numeros", "eyebrow": "Passo três · De Oliveira, Burini e Jeukendrup, 2014", "titulo": "O intestino decide a prova do amador",
          "numeros": [{"n": "30 a 50%", "x": "dos atletas com queixa gastrointestinal no exercício", "cor": "verm"},
                      {"n": "3", "x": "tipos de causa: fisiológica, mecânica e nutricional", "cor": "tinta"},
                      {"n": "1", "x": "a mais acionável: o que foi comido, quando e em que concentração", "cor": "petr"}],
          "destaque": "Costa e colaboradores, 2017: a perfusão intestinal cai no esforço. Piora com intensidade, duração, calor e desidratação.",
          "destaque_cor": "ambar", "fonte": "Sports Medicine 2014 · Alimentary Pharmacology and Therapeutics 2017"})

# 7. o que resolve
S.append({"id": "resolve", "tipo": "cards", "por_linha": 4, "eyebrow": "Em ordem de retorno", "titulo": "O que resolve, e o que é proibido",
          "cards": [{"t": "1 · Antes", "x": "pouca gordura, fibra e volume", "cor": "petr"},
                    {"t": "2 · Concentração", "x": "gel com água", "cor": "petr"},
                    {"t": "3 · Treinar o intestino", "x": "semanas de longos com a estratégia da prova", "cor": "petr"},
                    {"t": "4 · Mistura de açúcares", "x": "quando a taxa for alta", "cor": "petr"}],
          "destaque": "Anti-inflamatório preventivo: não. Van Wijck, 2012: ibuprofeno antes do esforço aumentou a lesão do intestino. Sangue nas fezes, dor intensa, sintoma noturno ou perda de peso: médico, não gel.",
          "destaque_cor": "verm", "fonte": "Medicine and Science in Sports and Exercise 2012"})

# 8. entre esforços
S.append({"id": "entre", "tipo": "tabela", "eyebrow": "Passo quatro · entre um esforço e outro", "titulo": "O intervalo decide o que cabe",
          "cab": ["Intervalo", "O que comer"],
          "larguras": [30, 70],
          "linhas": [["Cerca de 4 horas", "refeição leve logo depois: sanduíche, arroz com frango, fruta"],
                     ["1 a 2 horas", "fruta, pão com mel, bebida com carboidrato, iogurte"],
                     ["Menos de 1 hora", "líquido com carboidrato e lanches pequenos"],
                     ["Intervalo do jogo", "bebida com carboidrato, gel com água, fruta fácil"],
                     ["Pesagem na véspera", "líquido com sódio, carboidrato em refeições pequenas, nada novo"]],
          "destaque": "A bolsa térmica é parte do equipamento. A lanchonete do ginásio tem salgado frito, refrigerante e fila.",
          "destaque_cor": "ambar"})

# 9. o plano de uma página
S.append({"id": "plano", "tipo": "duas", "eyebrow": "Passo cinco · o plano escrito", "titulo": "Uma página, tudo testado em treino",
          "esq": {"t": "O mesmo perfil, com plano", "cor": "petr",
                  "itens": ["dois dias de sobrecarga, menos fibra; a balança sobe", "véspera: arroz, frango, legumes cozidos",
                            "3 h antes: pão com mel e banana; o café de sempre", "gel dos treinos, com água, a partir dos 40 min"]},
          "dir": {"t": "O plano B", "cor": "ambar",
                  "itens": ["largada atrasada", "posto sem a bebida esperada", "calor acima do previsto", "estômago que não aceita"]},
          "destaque": "O gel do kit fica no kit. O que não tem a marca “testado em treino” sai do plano.",
          "destaque_cor": "tinta"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quem faz o quê", "titulo": "Nada de novo no dia",
          "regras": ["Pergunta de corte: sobrecarga só acima de noventa minutos contínuos",
                     "Manhã de trás para a frente; o intestino treinado antes da prova",
                     "Entre esforços, a logística manda; tudo cabe numa página"],
          "cards": [{"t": "Nutricionista", "x": "O plano, com quantidades."},
                    {"t": "Preparador e treinador", "x": "O ensaio nos treinos."},
                    {"t": "Médico", "x": "Sintoma que a comida não explica; anti-inflamatório."}],
          "quem": "Sem ensaio, não há plano."})

spec = {"arquivo": "aulas/MOD04/04-10-nutricao-em-dia-de-competicao.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Nutrição em dia de competição", "subtitulo": "Planejamento, tolerância gastrointestinal e logística",
        "nota_capa": "Entra pela regra: nada de novo no dia.",
        "secoes": {"regra": ["A regra e o procedimento.", "capa"],
                   "corte": ["Dias antes, véspera e manhã.", "corte"],
                   "intestino": ["Durante, entre esforços e o plano.", "intestino"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-10.json"), "w"), ensure_ascii=False, indent=1)
print("04-10.json:", len(S), "slides")
