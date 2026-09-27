"""Spec do deck 10.1. Gera 10-01.json ao lado deste arquivo."""
import json, os

S = []
S.append({"id": "grupo", "tipo": "pergunta", "fundo": "tinta", "eyebrow": "Mensagem no grupo do ciclismo",
          "pergunta": "“Ele não tem motivação.” Isso explica alguma coisa?",
          "apoio": "Pedalava quatro vezes por semana e sumiu dos treinos de sábado.", "ic": "h:bike"})
S.append({"id": "qualidade", "tipo": "espectro", "eyebrow": "Erro um", "titulo": "Motivação não é quanto. É de que tipo",
          "extremos": ["controlada", "autônoma"], "inverter": True,
          "marcas": [{"ic": "t:lock", "t": "Obrigação", "cor": "verm"}, {"ic": "t:mood-sad", "t": "Culpa", "cor": "verm"},
                     {"ic": "t:scale", "t": "Valor", "cor": "ambar"}, {"ic": "t:user", "t": "Identidade", "cor": "petr"},
                     {"ic": "t:mood-happy", "t": "Prazer", "cor": "petr"}],
          "destaque": "66 estudos: quanto mais autônoma, mais exercício, e mais tempo.", "destaque_cor": "petr",
          "fonte": "Teoria da autodeterminação (Deci e Ryan) · revisão sistemática, Int J Behav Nutr Phys Act 2012"})
S.append({"id": "necessidades", "tipo": "icones", "eyebrow": "Três necessidades", "titulo": "Qual delas deixou de ser atendida?",
          "itens": [{"ic": "h:award-trophy", "t": "Competência", "x": "sentir que melhora", "cor": "ambar"},
                    {"ic": "t:compass", "t": "Autonomia", "x": "a escolha também é dele", "cor": "petr"},
                    {"ic": "t:friends", "t": "Vínculo", "x": "pertencer ao grupo", "cor": "verm"}]})
S.append({"id": "controle", "tipo": "versus", "eyebrow": "Erro dois", "titulo": "Controlar para motivar",
          "esq": {"ic": "t:lock", "t": "Controlar", "itens": ["cobrança em público", "planilha fechada"], "cor": "verm"},
          "dir": {"ic": "t:compass", "t": "Apoiar a autonomia", "itens": ["escolha dentro de limites", "explicar o porquê"], "cor": "petr"},
          "fonte": "Modelo da relação técnico e atleta, J Sports Sci 2003"})
S.append({"id": "autoeficacia", "tipo": "painel", "lado": "esq", "cor": "petr", "ic": "t:target-arrow", "grande": "r = 0,38",
          "tam_grande": 88, "ic_tam": 360, "eyebrow": "Erro três", "titulo": "Autoeficácia é sobre esta tarefa, hoje",
          "itens": [{"ic": "t:x", "t": "“Você é fera”", "cor": "verm"},
                    {"ic": "t:check", "t": "“Você já subiu serra parecida neste ritmo”"},
                    {"ic": "t:chart-line", "t": "45 estudos no esporte: correlação média de 0,38 com desempenho"}],
          "fonte": "Bandura, 1977 · metanálise, Res Q Exerc Sport 2000"})
S.append({"id": "fontes", "tipo": "matriz", "eyebrow": "As quatro fontes", "titulo": "Da mais forte à mais fraca",
          "quadrantes": [{"ic": "h:award-trophy", "t": "1 · Ter conseguido antes", "x": "experiência de domínio", "cor": "petr"},
                         {"ic": "t:eye", "t": "2 · Ver alguém parecido", "x": "experiência vicária", "cor": "petr"},
                         {"ic": "t:message-circle", "t": "3 · Ouvir que consegue", "x": "persuasão verbal", "cor": "ambar"},
                         {"ic": "t:heartbeat", "t": "4 · Ler o próprio corpo", "x": "coração acelerado: pronto ou perdido?", "cor": "ambar"}]})
S.append({"id": "ambiente", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Motivação não se injeta. Ela cresce no ambiente de todo dia.",
          "apoio": "A planilha que oferece escolha, o treino que mostra progresso, o grupo onde há lugar.", "ic": "t:seedling"})
S.append({"id": "processo", "tipo": "fluxo", "eyebrow": "Erro quatro", "titulo": "“Engole o choro” chega tarde demais",
          "passos": [{"ic": "t:map", "t": "Situação", "x": "escolher, modificar", "cor": "petr"},
                     {"ic": "t:eye", "t": "Atenção", "x": "para onde olhar", "cor": "petr"},
                     {"ic": "t:bulb", "t": "Interpretação", "x": "reavaliar o sentido", "cor": "petr"},
                     {"ic": "t:hand-stop", "t": "Resposta", "x": "suprimir o que já sente", "cor": "verm"}],
          "fonte": "Modelo de processo da regulação emocional (James Gross, 1998)"})
S.append({"id": "custo", "tipo": "painel", "lado": "dir", "cor": "ambar", "ic": "t:bulb", "ic_tam": 400,
          "eyebrow": "O custo de suprimir", "titulo": "Reavaliar ajuda mais que esconder",
          "itens": [{"ic": "t:mood-happy", "t": "Reavaliar: mais emoção positiva e mais bem-estar", "cor": "petr"},
                    {"ic": "t:mood-sad", "t": "Suprimir: mais emoção negativa, apesar de mostrar menos", "cor": "verm"},
                    {"ic": "t:message-circle", "t": "“O que esse nervosismo está te dizendo?”", "cor": "ambar"}],
          "fonte": "Cinco estudos com estudantes, J Pers Soc Psychol 2003"})
S.append({"id": "ciclo", "tipo": "ciclo", "eyebrow": "Erro cinco", "titulo": "Motivação é assunto de todo dia",
          "nos": [{"ic": "t:users", "t": "Quem conduz o treino", "x": "escolha, estrutura, envolvimento", "cor": "tinta"},
                  {"ic": "t:puzzle", "t": "Necessidades atendidas", "cor": "petr"},
                  {"ic": "t:compass", "t": "Motivação autônoma", "cor": "petr"},
                  {"ic": "t:trending-up", "t": "Persistência e bem-estar", "cor": "ambar"}],
          "centro": "o ciclo também roda ao contrário", "fonte": "J Sports Sci 2003"})
S.append({"id": "segunda", "tipo": "checklist", "eyebrow": "Na segunda-feira", "titulo": "Quatro gestos",
          "itens": [{"ic": "t:compass", "t": "Uma escolha real", "x": "em toda prescrição", "cor": "petr"},
                    {"ic": "t:chart-line", "t": "Um progresso visível", "x": "carga anotada, teste repetido", "cor": "ambar"},
                    {"ic": "t:friends", "t": "Com quem ele treina?", "x": "pertencer também sustenta", "cor": "verm"},
                    {"ic": "t:message-circle", "t": "Nomear a emoção", "x": "em vez de mandar esconder", "cor": "tinta"}]})
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Motivação, autoeficácia e regulação emocional", "titulo": "“Sentimos sua falta no sábado. O que mudou?”",
          "regras": ["Motivação tem tipo, e o tipo muda com o ambiente",
                     "Autoeficácia se constrói com sucesso em tarefas calibradas",
                     "Reavaliar a emoção ajuda mais que suprimir"],
          "cards": [{"ic": "t:users", "t": "Quem conduz o treino", "x": "Mexe nas três necessidades todo dia."},
                    {"ic": "h:doctor", "t": "Médico e fisioterapia", "x": "Escolha, progresso visível e vínculo em cada consulta."},
                    {"ic": "h:psychology", "t": "Psicologia do esporte", "x": "Quando a emoção atrapalha o desempenho ou a vida."}]})

spec = {"arquivo": "aulas/MOD10/10-01-motivacao-autoeficacia-e-regulacao-emocional.md",
        "modulo": "Psicologia do Esporte e Saúde Mental", "tema": "anil",
        "titulo": "Motivação, autoeficácia e regulação emocional", "subtitulo": "Cinco erros de quem tenta motivar",
        "nota_capa": "Entra pela mensagem do treinador no grupo do ciclismo.",
        "secoes": {"grupo": ["A cena e o primeiro erro.", "capa"], "controle": ["Controle e autoeficácia.", "controle"],
                   "processo": ["Regulação emocional.", "processo"], "ciclo": ["O ciclo e o que muda.", "ciclo"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "10-01.json"), "w"), ensure_ascii=False, indent=1)
print("10-01.json:", len(S), "slides")
