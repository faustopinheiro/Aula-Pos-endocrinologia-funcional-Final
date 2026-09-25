"""Spec do deck 7.2. Gera 07-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "cena", "tipo": "frase", "fundo": "tinta", "eyebrow": "A situação mais comum",
          "frase": "Não é que os dados de lesão sejam ruins. É que eles não existem.",
          "apoio": "A literatura de vigilância nasceu no clube profissional. Esta aula entrega um sistema que funciona com a equipe e o tempo que você tem."})

S.append({"id": "perguntas", "tipo": "cards", "por_linha": 3, "eyebrow": "O que o registro precisa responder", "titulo": "Três perguntas, e só três",
          "cards": [{"t": "Quantos agora?", "x": "quantas pessoas do grupo estão com problema nesta semana", "cor": "petr"},
                    {"t": "O quê, onde, quando?", "x": "tipo, região do corpo e momento da temporada", "cor": "ambar"},
                    {"t": "Funcionou?", "x": "o que eu mudei reduziu o problema", "cor": "tinta"}],
          "destaque": "Se o registro responde as três, está bom. Se não responde, não adianta ter vinte colunas.",
          "destaque_cor": "tinta"})

S.append({"id": "definicao", "tipo": "lista", "eyebrow": "Passo um · antes de coletar", "titulo": "A definição escrita numa folha",
          "itens": [{"t": "Lesão", "x": "consenso com restrição para o recreativo; perda de tempo mais sobrecarga no clube", "cor": "petr"},
                    {"t": "Problema de saúde", "x": "inclui doença: infecção respiratória também tira do treino", "cor": "ambar"},
                    {"t": "Recorrência", "x": "a mesma lesão, no mesmo lugar, depois de retorno completo", "cor": "verm"},
                    {"t": "Acesso", "x": "quem vê o quê", "cor": "tinta"}],
          "gap_itens": 22, "destaque": "Assinada por quem coordena, e não muda sem avisar.", "destaque_cor": "tinta",
          "fonte": "Consenso do COI, Br J Sports Med 2020"})

S.append({"id": "exposicao", "tipo": "tabela", "eyebrow": "Passo dois · a metade que todo mundo esquece", "titulo": "Exposição: consistente, não sofisticada",
          "cab": ["Contexto", "Unidade de exposição", "Onde já está"],
          "larguras": [26, 40, 34],
          "linhas": [["Assessoria de corrida", "quilômetros ou minutos por semana", "a planilha do aluno"],
                     ["Academia", "sessões feitas", "a catraca"],
                     ["Clube", "horas de treino e minutos de jogo, separados", "a lista de presença"],
                     ["Escola ou projeto", "sessões oferecidas vezes presença", "a chamada"]],
          "destaque": "Quem estava lesionado e não treinou não entra na exposição daquela semana.",
          "destaque_cor": "verm"})

S.append({"id": "ferramentas", "tipo": "duas", "eyebrow": "Passo três · duas ferramentas", "titulo": "Mais que isso ninguém sustenta",
          "esq": {"t": "Questionário semanal de Oslo", "cor": "petr",
                  "itens": ["quatro perguntas, por mensagem", "mesmo dia, para todo mundo", "esteja bem ou não", "trinta segundos"]},
          "dir": {"t": "Ficha de lesão, oito campos", "cor": "ambar",
                  "itens": ["início, região e lado, tipo", "súbito ou gradual; o que fazia", "se já teve antes", "dias restrito e data do retorno"]},
          "destaque": "Sem data de retorno não há gravidade. E se a ficha exigir computador, não vai ser preenchida.",
          "destaque_cor": "tinta", "fonte": "Questionários do OSTRC, Br J Sports Med 2020"})

S.append({"id": "indicadores", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo quatro · indicadores", "titulo": "Não são dez. São três",
          "cards": [{"t": "Proporção semanal", "x": "gente com problema na semana; o número de toda segunda-feira", "cor": "petr"},
                    {"t": "Incidência", "x": "lesões novas por mil horas ou mil sessões", "cor": "ambar"},
                    {"t": "Carga de lesão", "x": "frequência vezes gravidade: dias perdidos por mil horas", "cor": "verm"}],
          "destaque": "Bahr, Clarsen e Ekstrand, 2018: olhar a carga, e não só a incidência.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2018"})

S.append({"id": "carga", "tipo": "numeros", "eyebrow": "Mesma incidência, outra realidade", "titulo": "Duas equipes, dez lesões cada",
          "numeros": [{"n": "30 dias", "x": "dez entorses leves de tornozelo, três dias cada", "cor": "petr"},
                      {"n": "250 dias", "x": "dez lesões de posterior de coxa, vinte e cinco dias cada", "cor": "verm"}],
          "destaque": "Quem olha incidência cuida do que é frequente. Quem olha carga cuida do que custa caro, e é isso que decide temporada.",
          "destaque_cor": "tinta", "fonte": "Exemplo de conta"})

p = [svg_abre(1664, 300, "Esquema: a taxa de resposta ao questionário começa alta e cai ao longo das semanas quando ninguém cuida da adesão")]
p.append(f'<line x1="120" y1="250" x2="1600" y2="250" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="120" y1="30" x2="120" y2="250" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M120,60 C400,70 600,110 800,150 C1000,190 1300,215 1600,225" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M120,60 C500,65 1000,70 1600,72" fill="none" stroke="{AZUL}" stroke-width="6" stroke-dasharray="14 10"/>')
p.append("</svg>")
rs = [rot(1180, 20, "com responsável, dia fixo e devolutiva", w=480, tam=24, cor=AZUL, peso=700),
      rot(1180, 160, "sem ninguém cuidando", w=420, tam=24, cor=FOSF, peso=700),
      rot(0, 20, "resposta", w=110, tam=22, cor=MUDO),
      rot(120, 262, "semanas", w=600, tam=22, cor=MUDO)]
S.append({"id": "adesao", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo cinco · onde o sistema morre", "titulo": "Não morre na planilha. Morre na adesão",
          "destaque": "Uma pessoa com nome, dia e horário fixos, link curto no aplicativo de mensagem, cobrança leve no dia seguinte.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "devolutiva", "tipo": "lista", "eyebrow": "A parte mais ignorada", "titulo": "Devolutiva: uma página por mês",
          "itens": [{"t": "Proporção do mês", "x": "quantos tiveram algum problema", "cor": "petr"},
                    {"t": "Três regiões", "x": "as mais frequentes no período", "cor": "ambar"},
                    {"t": "Dias perdidos", "x": "o que custou caro", "cor": "verm"},
                    {"t": "O que muda", "x": "uma frase sobre o planejamento", "cor": "tinta"}],
          "gap_itens": 22, "destaque": "Quem responde toda semana e nunca vê nada voltar, para de responder.", "destaque_cor": "verm"})

S.append({"id": "lgpd", "tipo": "lista", "eyebrow": "Passo seis · dado de saúde é dado sensível", "titulo": "O cuidado que protege todo mundo",
          "itens": [{"t": "Consentimento", "x": "o que se coleta, para quê, quem vê; menor assina o responsável", "cor": "petr"},
                    {"t": "Acesso por função", "x": "treinador vê a condição de treino, não o diagnóstico", "cor": "ambar"},
                    {"t": "Nada em grupo de mensagem", "x": "circula liberado, com restrição ou fora", "cor": "verm"},
                    {"t": "Relatório agregado", "x": "sem nome", "cor": "petr"},
                    {"t": "Prazo e dono", "x": "onde fica, por quanto tempo, e quando o atleta sai", "cor": "tinta"}],
          "gap_itens": 18, "fonte": "Lei 13.709/2018, art. 5º, II"})

S.append({"id": "painel", "tipo": "duas", "eyebrow": "Para montar nesta semana", "titulo": "O painel mínimo e os quatro erros",
          "esq": {"t": "Painel de uma página", "cor": "petr",
                  "itens": ["proporção semanal: o pulso", "regiões mais atingidas", "dias perdidos por mil horas", "recorrências: o espelho do retorno"]},
          "dir": {"t": "Erros que estragam o registro", "cor": "verm",
                  "itens": ["registrar só quem procurou atendimento", "lesão sem exposição", "mudar a definição no meio", "coletar sem devolver"]},
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Seis passos", "titulo": "Um registro que dura é um registro que alguém cuida",
          "regras": ["Definição escrita antes de coletar",
                     "Exposição medida, lesão com data de retorno",
                     "Devolutiva todo mês, dado protegido sempre"],
          "cards": [{"t": "Coordenação, médico e fisioterapeuta", "x": "Definem a pergunta; quem atendeu preenche a ficha."},
                    {"t": "Preparação física", "x": "Manda o questionário e mantém a adesão."},
                    {"t": "Comissão e instituição", "x": "Leem o painel todo mês; guardam o dado."}],
          "quem": "Próxima aula: por que a lesão acontece, e por que caçar uma causa única não funciona."})

spec = {"arquivo": "aulas/MOD07/07-02-vigilancia-e-registro-padronizado.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Vigilância de lesão no mundo real", "subtitulo": "Seis passos para um registro que dura",
        "nota_capa": "Entra pela ausência de dados, sem culpar ninguém.",
        "secoes": {"cena": ["Perguntas, definição e exposição.", "capa"],
                   "ferramentas": ["Ferramentas, indicadores e carga.", "ferramentas"],
                   "adesao": ["Adesão, devolutiva, LGPD e painel.", "adesao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-02.json"), "w"), ensure_ascii=False, indent=1)
print("07-02.json:", len(S), "slides")
