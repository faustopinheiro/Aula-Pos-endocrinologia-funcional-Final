"""Spec do deck 7.8. Gera 07-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "caso", "tipo": "frase", "fundo": "tinta", "eyebrow": "Caso ilustrativo",
          "frase": "Homem na casa dos quarenta, corredor há anos. Entraram ladeira e tiro.",
          "apoio": "O volume quase não mudou; o estímulo mudou todo. Semanas depois, dor no Aquiles: pior no começo da corrida e na primeira pisada da manhã seguinte."})

S.append({"id": "tentativas", "tipo": "lista", "eyebrow": "O ciclo de sempre", "titulo": "“Já tentei de tudo e nada funciona”",
          "itens": [{"t": "Parou duas semanas", "x": "melhorou, voltou no mesmo ritmo, piorou", "cor": "verm"},
                    {"t": "Anti-inflamatório", "x": "melhorou, voltou, piorou", "cor": "verm"},
                    {"t": "Alongamento diário", "x": "piorou", "cor": "verm"},
                    {"t": "Palmilha e dois tênis", "x": "nada mudou", "cor": "ambar"}],
          "gap_itens": 22, "destaque": "Faltou a única coisa com boa evidência: carga bem dosada, por tempo suficiente.",
          "destaque_cor": "tinta"})

S.append({"id": "perguntas", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo um · entender a carga", "titulo": "Três perguntas antes de prescrever",
          "cards": [{"t": "O que mudou?", "x": "volume, ladeira, tiro, salto, pausa, piso, calçado, horário", "cor": "ambar"},
                    {"t": "Há compressão?", "x": "piora em alongamento máximo, escada, agachamento fundo", "cor": "verm"},
                    {"t": "E a manhã seguinte?", "x": "rigidez e primeira pisada: o termômetro do dia anterior", "cor": "petr"}],
          "destaque": "No caso ilustrativo, a resposta era evidente: entraram os estímulos que mais pedem do tendão como mola.",
          "destaque_cor": "tinta"})

S.append({"id": "ajuste", "tipo": "duas", "eyebrow": "Passo dois · ajustar sem zerar", "titulo": "Tirar os picos, manter o resto",
          "esq": {"t": "Sai por algumas semanas", "cor": "verm",
                  "itens": ["tiro, ladeira, salto", "mudança brusca de ritmo", "posições de compressão", "a sessão longa que é o dobro"]},
          "dir": {"t": "Fica", "cor": "petr",
                  "itens": ["corrida confortável em piso plano", "volume dentro da régua de dor", "a força, que é o tratamento"]},
          "destaque": "Quem chegou esperando ouvir “pare de correr” e ouve “corra de outro jeito” adere muito mais.",
          "destaque_cor": "tinta"})

S.append({"id": "regua", "tipo": "lista", "eyebrow": "Passo três · a régua da dor", "titulo": "Até cerca de 5 em 10, com três condições",
          "itens": [{"t": "Volta ao basal na manhã seguinte", "x": "a primeira pisada é o termômetro", "cor": "petr"},
                    {"t": "Não sobe de semana para semana", "x": "a tendência importa mais que o dia", "cor": "ambar"},
                    {"t": "A função não piora", "x": "continua conseguindo fazer o que fazia", "cor": "tinta"}],
          "gap_itens": 26, "destaque": "Em 38 pacientes, continuar correndo e saltando com a régua deu o mesmo resultado que o repouso ativo.",
          "destaque_cor": "petr", "fonte": "Silbernagel e colegas, Am J Sports Med 2007"})

S.append({"id": "pesada", "tipo": "tabela", "eyebrow": "Passo quatro · fase dois, carga pesada e lenta", "titulo": "A dose do ensaio dinamarquês, no Aquiles",
          "cab": ["Semanas", "Repetições máximas", "Séries"],
          "larguras": [30, 40, 30],
          "linhas": [["1", "15", "3"],
                     ["2 e 3", "12", "3"],
                     ["4 e 5", "10", "4"],
                     ["6 a 8", "8", "4"],
                     ["9 a 12", "6", "4"]],
          "destaque": "Três vezes por semana, 3 s para subir e 3 s para descer. Antes, se a dor estiver irritada, isometria: 5 × 45 s.",
          "destaque_cor": "tinta", "fonte": "Am J Sports Med 2015 · isometria: Br J Sports Med 2015"})

S.append({"id": "comparacao", "tipo": "numeros", "eyebrow": "Carga pesada e lenta contra excêntrico, 58 pessoas", "titulo": "Os dois funcionam; um se cumpre melhor",
          "numeros": [{"n": "100%", "x": "satisfeitos em 12 semanas, carga pesada e lenta", "cor": "petr"},
                      {"n": "80%", "x": "satisfeitos em 12 semanas, excêntrico", "cor": "ambar"},
                      {"n": "92%", "x": "adesão com carga pesada e lenta, contra 78%", "cor": "tinta"}],
          "destaque": "A diferença de satisfação sumiu em um ano. Carga suficiente, consistente, por tempo suficiente, importa mais que a escola.",
          "destaque_cor": "tinta", "fonte": "Am J Sports Med 2015"})

p = [svg_abre(1664, 280, "Quatro degraus subindo: isometria, carga pesada e lenta, mola e esporte")]
for i, c in enumerate([AZUL, OXID, GLIC, FOSF]):
    x, y = 60 + i * 400, 220 - i * 50
    p.append(f'<rect x="{x}" y="{y}" width="380" height="{280 - y}" rx="8" fill="{c}" fill-opacity="0.18" stroke="{c}" stroke-width="4"/>')
p.append("</svg>")
rs = [rot(60, 180, "1 · isometria", w=380, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(460, 130, "2 · pesada e lenta", w=380, tam=26, cor=OXID, peso=700, alinha="center"),
      rot(860, 80, "3 · mola: salto", w=380, tam=26, cor=GLIC, peso=700, alinha="center"),
      rot(1260, 30, "4 · esporte", w=380, tam=26, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "fases", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As fases que costumam ser puladas", "titulo": "Progride quem passa no critério",
          "destaque": "A fase da mola é a mais pulada e é a que prepara para o esporte. Critério: manhã seguinte estável, força subindo, novo estímulo tolerado.",
          "destaque_cor": "tinta"})

p = [svg_abre(1664, 300, "Esquema de doze semanas em que a dor oscila, com semanas boas e ruins, mas desce na tendência")]
p.append(f'<line x1="80" y1="270" x2="1600" y2="270" stroke="{MUDO}" stroke-width="3"/>')
pts = [(80, 60), (206, 90), (332, 70), (458, 120), (584, 105), (710, 150), (836, 130), (962, 180), (1088, 165), (1214, 205), (1340, 190), (1466, 225), (1592, 215)]
p.append('<polyline points="' + " ".join(f"{x},{y}" for x, y in pts) + f'" fill="none" stroke="{FOSF}" stroke-width="5"/>')
p.append(f'<line x1="80" y1="70" x2="1592" y2="222" stroke="{AZUL}" stroke-width="4" stroke-dasharray="16 10"/>')
p.append("</svg>")
rs = [rot(1180, 20, "dor da manhã seguinte", w=420, tam=24, cor=FOSF, peso=700, alinha="right"),
      rot(1180, 236, "a tendência", w=420, tam=24, cor=AZUL, peso=700, alinha="right"),
      rot(80, 276, "12 semanas", w=300, tam=22, cor=MUDO)]
S.append({"id": "prazo", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo cinco · combinar o prazo", "titulo": "Doze semanas, com oscilação",
          "destaque": "Meça algo e mostre, reavalie a cada duas ou três semanas, avise que vai oscilar. Semana ruim não é estaca zero.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "falhas", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo seis · por que falha", "titulo": "Quase nunca é o tratamento",
          "cards": [{"t": "Dose baixa", "x": "se conversa tranquilo na série, não está pesado", "cor": "verm"},
                    {"t": "Tempo curto", "x": "quatro semanas é amostra grátis", "cor": "verm"},
                    {"t": "Causa intacta", "x": "a ladeira continua igual", "cor": "ambar"},
                    {"t": "Sem fase de mola", "x": "alta, tiro no fim de semana, dor de volta", "cor": "ambar"},
                    {"t": "Imagem como régua", "x": "compare função, não estrutura", "cor": "petr"},
                    {"t": "Bem feito e não melhora", "x": "rever o diagnóstico com o médico", "cor": "tinta"}]})

S.append({"id": "plano", "tipo": "tabela", "eyebrow": "De volta ao caso ilustrativo", "titulo": "O plano, não o desfecho",
          "cab": ["Fase", "O que entra", "Para avançar"],
          "larguras": [22, 44, 34],
          "linhas": [["Primeiras semanas", "corrida leve em plano; sem ladeira, tiro e alongamento sustentado; isometria se irritado", "manhã seguinte estável"],
                     ["Força", "carga pesada e lenta, 3 × por semana, registrada", "força subindo, régua mantida"],
                     ["Mola", "salto em volume baixo", "régua mantida"],
                     ["Esporte", "tiro 1 × por semana, depois ladeira", "uma novidade de cada vez"]],
          "destaque": "Depois da alta, força duas vezes por semana como hábito: é o que mais protege contra a recaída.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Seis passos", "titulo": "Carga bem dosada, por tempo suficiente",
          "regras": ["Entender a carga que causou; ajustar sem zerar",
                     "Régua da manhã seguinte; fases até a mola e o esporte",
                     "Prazo dito em voz alta no primeiro dia"],
          "cards": [{"t": "Médico", "x": "Diagnostica e descarta o que imita tendinopatia."},
                    {"t": "Fisioterapia", "x": "Prescreve, progride e reavalia o exercício."},
                    {"t": "Preparação física", "x": "Ajusta o treino e mantém a força como hábito."}],
          "quem": "Próxima aula: o joelho, dois problemas debaixo da mesma queixa."})

spec = {"arquivo": "aulas/MOD07/07-08-tendinopatia-manejo-de-carga-como-tratamento.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Tendinopatia do Aquiles", "subtitulo": "Manejo de carga como tratamento, em seis passos",
        "nota_capa": "Caso ilustrativo: homem na casa dos quarenta.",
        "secoes": {"caso": ["O caso e as três perguntas.", "capa"],
                   "ajuste": ["Ajuste, régua de dor e dose.", "ajuste"],
                   "fases": ["Fases, prazo, falhas e o plano.", "fases"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-08.json"), "w"), ensure_ascii=False, indent=1)
print("07-08.json:", len(S), "slides")
