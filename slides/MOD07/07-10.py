"""Spec do deck 7.10. Gera 07-10.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "abertura", "tipo": "frase", "fundo": "tinta", "eyebrow": "Duas regiões, um erro em comum",
          "frase": "A conduta padrão termina cedo demais.",
          "apoio": "O tornozelo recebe alta quando anda sem dor; o ombro, quando o repouso aliviou. E aí o tornozelo torce de novo, e o ombro volta a doer quando o volume volta."})

S.append({"id": "ottawa", "tipo": "numeros", "eyebrow": "Tornozelo · passo um · precisa de radiografia?", "titulo": "A regra de Ottawa",
          "numeros": [{"n": "27", "x": "estudos na revisão sistemática", "cor": "tinta"},
                      {"n": "15.581", "x": "pacientes", "cor": "tinta"},
                      {"n": "97,6%", "x": "sensibilidade combinada para fratura", "cor": "petr"}],
          "destaque": "Pede imagem: dor óssea na borda posterior dos maléolos, na base do quinto metatarso ou no navicular, ou não conseguir dar quatro passos.",
          "destaque_cor": "tinta", "fonte": "Revisão sistemática, BMJ 2003"})

S.append({"id": "alerta", "tipo": "cards", "por_linha": 5, "eyebrow": "Qualquer que seja a regra", "titulo": "Sinais que pedem avaliação urgente",
          "cards": [{"t": "Deformidade", "x": "visível", "cor": "verm"},
                    {"t": "Não apoia", "x": "o pé no chão", "cor": "verm"},
                    {"t": "Dor", "x": "desproporcional", "cor": "verm"},
                    {"t": "Formigamento", "x": "ou perda de sensibilidade", "cor": "verm"},
                    {"t": "Pé pálido", "x": "ou frio", "cor": "verm"}],
          "destaque": "Qualquer um desses tira a conversa da beira do campo.", "destaque_cor": "verm"})

S.append({"id": "semana", "tipo": "duas", "eyebrow": "Tornozelo · passo dois · a primeira semana", "titulo": "Proteger pouco, mover cedo",
          "esq": {"t": "Com evidência forte", "cor": "petr",
                  "itens": ["mobilização precoce: mover e apoiar no que a dor permite", "anti-inflamatório nos primeiros dias, para dor e inchaço", "proteção nas primeiras 48 horas"]},
          "dir": {"t": "Não fazer", "cor": "verm",
                  "itens": ["imobilizar por semanas sem indicação médica", "achar que o remédio substitui reabilitação"]},
          "destaque_cor": "tinta", "fonte": "Revisão de 46 revisões sistemáticas, Br J Sports Med 2017"})

S.append({"id": "alta", "tipo": "frase", "fundo": "tinta", "eyebrow": "O erro clássico",
          "frase": "Anda sem dor, o inchaço sumiu. Alta?",
          "apoio": "A parte que evita a próxima torção nem começou."})

S.append({"id": "instabilidade", "tipo": "numeros", "eyebrow": "Tornozelo · passo três · por que reabilitar", "titulo": "Instabilidade crônica depois da primeira entorse",
          "numeros": [{"n": "~40%", "x": "nas estimativas mais baixas", "cor": "ambar"},
                      {"n": "até 70%", "x": "nas mais altas, conforme critério e população", "cor": "verm"}],
          "destaque": "Insegurança, torções repetidas e limitação por anos: uma lesão que parece banal e deixa sequela.",
          "destaque_cor": "verm", "fonte": "Consenso do International Ankle Consortium, Br J Sports Med 2016"})

S.append({"id": "programa", "tipo": "lista", "eyebrow": "O que reduz a recidiva", "titulo": "Quatro ingredientes, por semanas",
          "itens": [{"t": "Amplitude", "x": "principalmente a flexão do tornozelo para a frente", "cor": "petr"},
                    {"t": "Força", "x": "panturrilha e estabilizadores do pé", "cor": "petr"},
                    {"t": "Equilíbrio progressivo", "x": "parado, instável, olhos fechados, com perturbação", "cor": "ambar"},
                    {"t": "O gesto", "x": "salto, mudança de direção, aterrissagem", "cor": "tinta"}],
          "gap_itens": 22, "destaque": "Em quem já torceu: órtese ou bandagem no período de risco (evidência forte) e treino neuromuscular (moderada).",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2017"})

S.append({"id": "ombro", "tipo": "duas", "eyebrow": "Ombro · passo um · reconhecer", "titulo": "O padrão de quem joga acima da cabeça",
          "esq": {"t": "O padrão", "cor": "petr",
                  "itens": ["dor lateral, acima da cabeça", "começou devagar, sem trauma", "piora com volume; dói ao deitar do lado", "melhora com redução, volta com o volume"]},
          "dir": {"t": "Fora do padrão", "cor": "verm",
                  "itens": ["trauma com perda súbita de força", "não eleva o braço; sensação de luxação", "dor noturna intensa e persistente", "formigamento para a mão; dor que não muda"]},
          "destaque_cor": "tinta"})

S.append({"id": "manguito", "tipo": "cards", "por_linha": 3, "eyebrow": "O nome e a leitura que mudaram", "titulo": "Dor do ombro relacionada ao manguito rotador",
          "cards": [{"t": "Primeira linha", "x": "exercício com progressão de carga, por meses, e ajuste do treino", "cor": "petr"},
                    {"t": "Atleta jovem de arremesso ou natação", "x": "instabilidade é parte frequente do quadro", "cor": "ambar"},
                    {"t": "Acima dos quarenta", "x": "mais lesão estrutural; exercício segue primeira linha na maioria", "cor": "ambar"}],
          "destaque": "A leitura de “algo pinçando que precisa ser tirado” perdeu força.",
          "destaque_cor": "tinta", "fonte": "Lewis e colegas, J Orthop Sports Phys Ther 2015"})

S.append({"id": "frentes", "tipo": "lista", "eyebrow": "Ombro · o que fazer", "titulo": "Quatro frentes",
          "itens": [{"t": "Exercício progressivo", "x": "manguito e escápula, carga que sobe", "cor": "petr"},
                    {"t": "Ajuste do que produziu", "x": "sem isso a fisioterapia trata com uma mão e o treino machuca com a outra", "cor": "verm"},
                    {"t": "Mobilidade e controle", "x": "escápula e coluna torácica, quando limitadas", "cor": "petr"},
                    {"t": "Expectativa combinada", "x": "leva meses e oscila", "cor": "tinta"}],
          "gap_itens": 22, "destaque": "Não fazer: repouso prolongado, infiltração como primeira linha, imagem de rotina em quadro típico.",
          "destaque_cor": "verm"})

S.append({"id": "carga", "tipo": "tabela", "eyebrow": "O ajuste de carga", "titulo": "Esporte por esporte",
          "cab": ["Modalidade", "O que olhar"],
          "larguras": [30, 70],
          "linhas": [["Natação", "metragem semanal, uso de palmar, distribuição entre os estilos"],
                     ["Arremesso", "contagem de arremessos e dias de descanso"],
                     ["Academia", "volume de empurrar acima da cabeça; proporção empurrar e puxar"]],
          "destaque": "Em todos: o que mudou nas semanas antes da dor?",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Tornozelo e ombro", "titulo": "Alta por ausência de dor produz recidiva",
          "regras": ["Tornozelo: regra de imagem, mover cedo, depois equilíbrio e gesto",
                     "Órtese ou bandagem no período de risco",
                     "Ombro: exercício por meses e ajuste do volume"],
          "cards": [{"t": "Médico e fisioterapia", "x": "Imagem, encaminhamento e etapas da reabilitação."},
                    {"t": "Preparação física", "x": "Volume, arremessos, equilíbrio e aterrissagem no treino."},
                    {"t": "Quem está mais perto", "x": "Reconhece o alarme e tira o atleta."}],
          "quem": "Próxima aula: lesão óssea por estresse."})

spec = {"arquivo": "aulas/MOD07/07-10-tornozelo-e-ombro.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Entorse de tornozelo e dor no ombro", "subtitulo": "Do primeiro dia à recidiva evitada",
        "nota_capa": "Entra pelo erro em comum.",
        "secoes": {"abertura": ["Tornozelo: imagem, primeira semana e alta.", "capa"],
                   "instabilidade": ["Tornozelo: instabilidade e programa.", "instabilidade"],
                   "ombro": ["Ombro: padrão, leitura e conduta.", "ombro"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-10.json"), "w"), ensure_ascii=False, indent=1)
print("07-10.json:", len(S), "slides")
