"""Spec do deck 8.11. Gera 08-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "tatame", "tipo": "frase", "fundo": "tinta", "eyebrow": "No tatame",
          "frase": "O joelho é o mesmo. A decisão de voltar pode ser diferente.",
          "apoio": "Uma judoca no fim da reabilitação do colateral medial. Numa situação, um torneio de pré-temporada sem nada em jogo; na outra, a seletiva da equipe nacional em doze dias."})

S.append({"id": "variam", "tipo": "duas", "eyebrow": "O problema reconhecido", "titulo": "Mesma condição, mesma circunstância, decisões diferentes",
          "esq": {"t": "O que existia", "cor": "tinta",
                  "itens": ["listas de fatores que entram na decisão", "nenhum critério quantitativo", "nenhuma ordem nem peso para os fatores"]},
          "dir": {"t": "O que o modelo propôs", "cor": "petr",
                  "itens": ["três passos, na ordem em que o clínico pensa", "depois, separar quanto risco existe de quanto risco se aceita"]},
          "destaque": "É essa separação que resolve a judoca.",
          "destaque_cor": "tinta", "fonte": "Clin J Sport Med 2010 · Br J Sports Med 2015"})

S.append({"id": "passos", "tipo": "cards", "por_linha": 3, "eyebrow": "Os três passos", "titulo": "Dois descrevem o risco; o terceiro, o contexto",
          "cards": [{"t": "1 · Estado de saúde", "x": "tecido, função, dor, testes: tudo o que o módulo construiu", "cor": "petr"},
                    {"t": "2 · Risco da participação", "x": "esporte, posição, proteção; no judô, entradas de perna e quedas em valgo", "cor": "petr"},
                    {"t": "3 · Modificadores", "x": "momento da temporada, pressão interna e externa, analgesia, conflito de interesse, medo de responsabilização", "cor": "ambar"}],
          "destaque": "Joelheira, restrição de técnica e tempo de luta menor mudam o passo dois.",
          "destaque_cor": "tinta"})

# diagrama: mesma barra de risco, duas linhas de tolerância
p = [svg_abre(1664, 400, "Barra de risco estimado igual nas duas situações; linha de tolerância mais baixa no torneio e mais alta na seletiva")]
base = 340
for i, (cx, tol, cor, nome) in enumerate([(420, 250, FOSF, "torneio"), (1180, 130, OXID, "seletiva")]):
    p.append(f'<line x1="{cx-240}" y1="{base}" x2="{cx+240}" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
    p.append(f'<rect x="{cx-70}" y="190" width="140" height="{base-190}" rx="6" fill="{GLIC}" fill-opacity="0.85"/>')
    p.append(f'<line x1="{cx-220}" y1="{tol}" x2="{cx+220}" y2="{tol}" stroke="{cor}" stroke-width="5" stroke-dasharray="14 10"/>')
p.append("</svg>")
rs = [rot(180, 20, "Torneio de pré-temporada", w=480, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(940, 20, "Seletiva em doze dias", w=480, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(190, 212, "tolerância baixa", w=150, tam=18, cor=FOSF, peso=700),
      rot(1210, 85, "tolerância mais alta", w=220, tam=20, cor=OXID, peso=700),
      rot(1400, 255, "risco estimado: o mesmo", w=240, tam=20, cor=MUDO),
      rot(200, 350, "risco acima da linha: não vale", w=440, tam=20, cor=MUDO, alinha="center"),
      rot(960, 350, "risco abaixo da linha: aceitável, se informada", w=440, tam=20, cor=MUDO, alinha="center")]
S.append({"id": "starrt", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Avaliar e tolerar", "titulo": "A barra não muda; a linha muda",
          "destaque": "A decisão mudou pelo contexto, não porque o joelho melhorou numa semana.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · StARRT, Br J Sports Med 2015"})

S.append({"id": "aceitar", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Avaliar o risco é uma coisa. Aceitar o risco é outra. E quem aceita é quem corre.",
          "apoio": "A equipe de saúde é a melhor fonte para avaliar o risco. Não é, sozinha, a dona da tolerância a ele."})

S.append({"id": "saidas", "tipo": "cards", "por_linha": 3, "eyebrow": "As três saídas", "titulo": "Liberar com restrição é a mais útil e a mais esquecida",
          "cards": [{"t": "Liberar", "x": "risco abaixo da tolerância; volta sem restrição, com monitoramento", "cor": "petr"},
                    {"t": "Liberar com restrição", "x": "menos tempo de luta, sem certas técnicas, com proteção, ou só treino", "cor": "ambar"},
                    {"t": "Ainda não", "x": "risco acima da tolerância, por mais que a data aperte", "cor": "verm"}],
          "destaque": "Há riscos inaceitáveis por si: tecido que pode falhar de forma grave, sinal neurológico, sequela permanente. A tolerância de ninguém muda essa resposta.",
          "destaque_cor": "verm"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem responde por quê", "titulo": "Decidido com a atleta, não sobre ela",
          "cab": ["Quem", "Responde por"],
          "larguras": [30, 70],
          "linhas": [["Equipe de saúde", "estimar o risco: tecido, função, prontidão"],
                     ["Médico", "liberação médica; dizer quando o risco é inaceitável por si"],
                     ["Atleta", "pesar o risco contra o que está em jogo e decidir dentro do aceitável"],
                     ["Técnico e clube", "trazer o contexto esportivo, sem decidir pela saúde"],
                     ["Família", "entra na decisão quando a atleta é menor de idade"]],
          "destaque": "Decisão compartilhada, na direção do consenso de Berna.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2017 · Consenso de Berna, 2016"})

S.append({"id": "conversa", "tipo": "lista", "eyebrow": "Decidir junto, na prática", "titulo": "Três conversas, alguns minutos a mais",
          "itens": [{"t": "Escolha", "x": "“Há mais de um caminho razoável, e a sua opinião conta.”", "cor": "petr"},
                    {"t": "Opções", "x": "cada saída, com o que traz de bom e de risco, em números que a pessoa entenda", "cor": "ambar"},
                    {"t": "Decisão", "x": "“Para você, o que pesa mais: a seletiva deste ano ou chegar inteira ao próximo ciclo?”", "cor": "tinta"}],
          "gap_itens": 16,
          "destaque": "Os números da conversa das opções são o assunto da próxima aula.",
          "destaque_cor": "tinta", "fonte": "Modelo de decisão compartilhada, J Gen Intern Med 2012"})

S.append({"id": "conflitos", "tipo": "cards", "por_linha": 2, "eyebrow": "O que distorce a decisão", "titulo": "Nomear os conflitos antes que eles decidam",
          "cards": [{"t": "Quem paga quem decide", "x": "o dever com a saúde da atleta não fica abaixo do interesse do clube", "cor": "verm"},
                    {"t": "A dor escondida", "x": "quem quer voltar minimiza; testes e observação não dependem só do relato", "cor": "ambar"},
                    {"t": "A analgesia que mascara", "x": "muda a informação, não o risco", "cor": "verm"},
                    {"t": "A pressão do calendário", "x": "empurra a linha de tolerância sem ninguém dizer em voz alta", "cor": "ambar"}],
          "destaque": "Proteções: separar quem avalia de quem tem interesse, registrar o raciocínio, pedir segunda opinião.",
          "destaque_cor": "tinta"})

S.append({"id": "semclube", "tipo": "tabela", "eyebrow": "Fora do clube", "titulo": "Os mesmos passos, outra equipe",
          "cab": ["Passo", "No consultório"],
          "larguras": [30, 70],
          "linhas": [["Estado de saúde", "avaliação e testes de consultório"],
                     ["Risco da participação", "corrida de rua, campeonato de fim de semana, treino de academia"],
                     ["Modificadores", "a prova já paga, a viagem marcada, o trabalho que não pode parar"]],
          "destaque": "Equipe menor não diminui a decisão compartilhada. Aumenta a responsabilidade de explicar bem.",
          "destaque_cor": "tinta"})

S.append({"id": "registro", "tipo": "cards", "por_linha": 3, "eyebrow": "O registro", "titulo": "Seis campos bastam",
          "cards": [{"t": "Estado de saúde", "x": "com os testes", "cor": "petr"},
                    {"t": "Risco da participação", "x": "no esporte e na posição", "cor": "petr"},
                    {"t": "Modificadores", "x": "os que foram considerados", "cor": "ambar"},
                    {"t": "Saída escolhida", "x": "liberar, com restrição, ainda não", "cor": "tinta"},
                    {"t": "Condições", "x": "restrições, prazo e sinais para parar", "cor": "verm"},
                    {"t": "Data de revisão", "x": "a próxima conversa já marcada", "cor": "tinta"}],
          "destaque": "Protege a atleta, mostra o raciocínio da equipe e organiza a próxima conversa.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Decisão de retorno", "titulo": "Avaliar o risco não é o mesmo que aceitá-lo",
          "regras": ["Três passos: estado, risco da participação, modificadores",
                     "Três saídas: liberar, com restrição, ainda não",
                     "Quem corre o risco participa da decisão"],
          "cards": [{"t": "Médico", "x": "Liberação e riscos inaceitáveis por si."},
                    {"t": "Equipe de saúde", "x": "Estima o risco e registra o raciocínio."},
                    {"t": "Atleta", "x": "Pesa o que está em jogo, informada."}],
          "quem": "Próxima aula, a última do módulo: risco residual e comunicação."})

spec = {"arquivo": "aulas/MOD08/08-11-decisao-de-retorno-compartilhada.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Decisão de retorno ao esporte", "subtitulo": "Avaliar o risco, aceitar o risco e decidir junto",
        "nota_capa": "Entra por uma judoca com o mesmo joelho diante de duas competições.",
        "secoes": {"tatame": ["A cena e o modelo em três passos.", "capa"],
                   "starrt": ["Avaliar e tolerar; as três saídas.", "starrt"],
                   "quem": ["Quem decide e como se conversa.", "quem"],
                   "conflitos": ["Conflitos, fora do clube, registro e fecho.", "conflitos"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-11.json"), "w"), ensure_ascii=False, indent=1)
print("08-11.json:", len(S), "slides")
