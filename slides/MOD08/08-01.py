"""Spec do deck 8.1. Gera 08-01.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "tatame", "tipo": "frase", "fundo": "tinta", "eyebrow": "Seis semanas de dor no ombro",
          "frase": "“O que eu tenho?” tem dono. A reabilitação precisa de outra pergunta.",
          "apoio": "O que essa pessoa não consegue fazer hoje, por que não consegue, e por onde eu começo? O laudo não responde isso."})

S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "Antes do primeiro exercício", "titulo": "Cinco perguntas, nesta ordem",
          "itens": [{"t": "É de reabilitação?", "x": "ou algo precisa ir para outro lugar antes", "cor": "verm"},
                    {"t": "Quão irritável está?", "x": "decide quanto eu posso testar hoje", "cor": "ambar"},
                    {"t": "O que não consegue fazer?", "x": "nas palavras da pessoa", "cor": "petr"},
                    {"t": "O que explica a limitação?", "x": "hipóteses, cada uma com um teste que pode derrubá-la", "cor": "petr"},
                    {"t": "O que vou medir de novo?", "x": "para saber se o plano funciona", "cor": "tinta"}],
          "gap_itens": 16})

S.append({"id": "bandeiras", "tipo": "cards", "por_linha": 4, "eyebrow": "Primeira pergunta", "titulo": "Parar e encaminhar antes de qualquer exercício",
          "cards": [{"t": "Trauma", "x": "deformidade ou perda súbita de função", "cor": "verm"},
                    {"t": "Dor noturna", "x": "sem posição de alívio, com febre, perda de peso ou câncer prévio", "cor": "verm"},
                    {"t": "Neurológico", "x": "formigamento ou fraqueza piorando", "cor": "verm"},
                    {"t": "Articulação quente", "x": "inchada, sem trauma", "cor": "verm"}],
          "destaque": "Nenhum é diagnóstico; todos mudam o caminho. E a crença de que o ombro está “estragado” também é achado de avaliação.",
          "destaque_cor": "tinta"})

S.append({"id": "sinss", "tipo": "cards", "por_linha": 5, "eyebrow": "Segunda pergunta", "titulo": "Gravidade, irritabilidade, natureza, estágio, estabilidade",
          "cards": [{"t": "Gravidade", "x": "quanto a dor limita", "cor": "petr"},
                    {"t": "Irritabilidade", "x": "quanto tempo leva para acalmar", "cor": "verm"},
                    {"t": "Natureza", "x": "o tipo de problema, e as bandeiras", "cor": "petr"},
                    {"t": "Estágio", "x": "agudo, subagudo, persistente", "cor": "petr"},
                    {"t": "Estabilidade", "x": "melhorando, piorando ou parado", "cor": "petr"}],
          "destaque": "Acalma em minutos: dá para testar até onde dói. Fica acesa por horas: exame curto hoje, o resto na próxima sessão.",
          "destaque_cor": "tinta", "fonte": "J Man Manip Ther 2021"})

S.append({"id": "cif", "tipo": "duas", "eyebrow": "Terceira pergunta", "titulo": "O laudo mora num nível; o motivo da consulta, em outro",
          "esq": {"t": "Os três níveis da CIF", "cor": "tinta",
                  "itens": ["estrutura e função: tendão, amplitude, força", "atividade: raspagem, empurrar, dormir de lado", "participação: treinar com a turma, competir"]},
          "dir": {"t": "Escala do próprio paciente", "cor": "petr",
                  "itens": ["guarda fechada: 3 de 10", "dormir sobre o lado direito: 4", "flexão de braço: 5"]},
          "destaque": "Três a cinco atividades escolhidas pela pessoa, nota de 0 a 10: a meta do tratamento e a primeira medida que se repete.",
          "destaque_cor": "tinta", "fonte": "OMS 2001 · Physiother Can 1995"})

S.append({"id": "hipoteses", "tipo": "tabela", "eyebrow": "Quarta pergunta", "titulo": "Cada hipótese com o teste que pode derrubá-la",
          "cab": ["Hipótese", "O teste"],
          "larguras": [34, 66],
          "linhas": [["Força insuficiente", "os dois lados; dinamômetro de mão ou repetições até a falha técnica"],
                     ["Amplitude limitada", "goniômetro, fita ou inclinômetro do celular, sempre igual"],
                     ["Controle ruim", "a própria tarefa, filmada de frente e de lado"],
                     ["Pouca tolerância a volume", "quantas repetições e séries antes de a dor subir"],
                     ["Medo, crença, expectativa", "“O que você acha que está acontecendo?”"]],
          "destaque": "Se nenhum resultado possível muda o que você faz, não faça o teste.",
          "destaque_cor": "verm"})

S.append({"id": "laudo", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O laudo diz o que está alterado. A avaliação diz o que dá para mudar.",
          "apoio": "As duas são verdadeiras ao mesmo tempo. Só a segunda produz um plano."})

p = [svg_abre(1664, 260, "Régua com uma faixa central de erro da medida; uma mudança pequena cai dentro da faixa e não conta, uma maior cai fora e conta")]
p.append(f'<line x1="80" y1="150" x2="1580" y2="150" stroke="{MUDO}" stroke-width="4"/>')
p.append(f'<rect x="620" y="110" width="420" height="80" rx="10" fill="{PAUSA}" fill-opacity="0.6"/>')
p.append(f'<line x1="830" y1="95" x2="830" y2="205" stroke="{TINTA}" stroke-width="4"/>')
p.append(seta_marker("sa", AZUL).replace("<marker", "<defs><marker").replace("</marker>", "</marker></defs>"))
p.append(seta_marker("sb", OXID).replace("<marker", "<defs><marker").replace("</marker>", "</marker></defs>"))
p.append(f'<line x1="830" y1="150" x2="960" y2="150" stroke="{AZUL}" stroke-width="8" marker-end="url(#sa)"/>')
p.append(f'<line x1="830" y1="230" x2="1300" y2="230" stroke="{OXID}" stroke-width="8" marker-end="url(#sb)"/>')
p.append("</svg>")
rs = [rot(632, 200, "erro da medida", w=190, tam=22, cor=MUDO, peso=700),
      rot(680, 50, "medida anterior", w=300, tam=22, cor=TINTA, peso=700, alinha="center"),
      rot(90, 110, "dentro da faixa: é ruído", w=480, tam=24, cor=AZUL, peso=700),
      rot(1320, 212, "fora da faixa: é mudança", w=340, tam=24, cor=OXID, peso=700)]
S.append({"id": "medir", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quinta pergunta", "titulo": "Duas ou três medidas, repetidas toda semana",
          "destaque": "Escala do paciente, um teste de força e a tarefa que reproduz a dor. Protocolo escrito: posição, comando, tentativas, horário.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Sports Med 2000"})

S.append({"id": "vieses", "tipo": "cards", "por_linha": 4, "eyebrow": "Nenhum é falta de conhecimento", "titulo": "Quatro erros de raciocínio",
          "cards": [{"t": "Ancorar no laudo", "x": "o resto da avaliação vira confirmação", "cor": "ambar"},
                    {"t": "Fechar cedo", "x": "a hipótese pronta em três minutos", "cor": "ambar"},
                    {"t": "Só o que confirma", "x": "esquece o teste que poderia derrubar", "cor": "ambar"},
                    {"t": "Tratar o achado", "x": "e não a queixa da pessoa", "cor": "verm"}],
          "destaque": "Triagem de movimento não prevê quem vai se lesionar. Serve para descrever, orientar e acompanhar.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2016"})

p = [svg_abre(1664, 300, "Ciclo de quatro etapas: hipótese, intervenção, reavaliação e ajuste, voltando à hipótese")]
p.append("<defs>" + seta_marker("ciclo", MUDO) + "</defs>")
xs = [200, 620, 1040, 1460]
for x, c in zip(xs, [TINTA, OXID, AZUL, GLIC]):
    p.append(f'<circle cx="{x}" cy="120" r="22" fill="{c}"/>')
for a, b in zip(xs, xs[1:]):
    p.append(f'<line x1="{a+40}" y1="120" x2="{b-48}" y2="120" stroke="{MUDO}" stroke-width="4" marker-end="url(#ciclo)"/>')
p.append(f'<path d="M1460,152 L1460,230 Q1460,250 1440,250 L220,250 Q200,250 200,230 L200,160" fill="none" stroke="{MUDO}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ciclo)"/>')
p.append("</svg>")
rs = [rot(50, 40, "hipótese", w=300, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(470, 40, "intervenção", w=300, tam=26, cor=OXID, peso=700, alinha="center"),
      rot(890, 40, "reavaliação", w=300, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(1310, 40, "ajuste do plano", w=300, tam=26, cor=GLIC, peso=700, alinha="center"),
      rot(530, 262, "confirma ou derruba a hipótese, e o ciclo recomeça", w=600, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "ciclo", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A avaliação não acaba na primeira consulta", "titulo": "Cada sessão começa com “como ficou?”",
          "destaque": "Sem o ciclo, o protocolo roda oito semanas e ninguém percebe que parou de funcionar na terceira.",
          "destaque_cor": "tinta"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem faz o quê", "titulo": "Quatro fontes de informação",
          "cab": ["Quem", "O que traz"],
          "larguras": [30, 70],
          "linhas": [["Médico", "diagnóstico, bandeiras, decisão sobre imagem"],
                     ["Fisioterapia", "irritabilidade, função, hipóteses, medidas repetidas e o plano"],
                     ["Preparação física", "como treinava antes: a carga da semana típica, o alvo do retorno"],
                     ["O próprio atleta", "as metas; e se está melhorando, antes do teste"]],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Avaliação funcional em reabilitação", "titulo": "Cinco perguntas antes do primeiro exercício",
          "regras": ["É de reabilitação, e quão irritável está?",
                     "O que não consegue fazer, e o que explica?",
                     "O que vou medir de novo?"],
          "cards": [{"t": "Médico", "x": "Diagnóstico, bandeiras e imagem."},
                    {"t": "Fisioterapia", "x": "Hipóteses, medidas e o plano."},
                    {"t": "Preparação e atleta", "x": "A carga de antes e as metas."}],
          "quem": "Próxima aula: as fases da reabilitação e os critérios de passagem."})

spec = {"arquivo": "aulas/MOD08/08-01-avaliacao-funcional-e-raciocinio-clinico.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Avaliação funcional em reabilitação", "subtitulo": "Cinco perguntas antes do primeiro exercício",
        "nota_capa": "Entra por um praticante de jiu-jitsu com o envelope da ressonância.",
        "secoes": {"tatame": ["A pergunta que falta e o roteiro.", "capa"],
                   "sinss": ["Irritabilidade, função e hipóteses.", "sinss"],
                   "medir": ["Medir de novo, erros e o ciclo.", "medir"],
                   "fecho": ["Quem faz o quê e o fecho.", "quem"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-01.json"), "w"), ensure_ascii=False, indent=1)
print("08-01.json:", len(S), "slides")
