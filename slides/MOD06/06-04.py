"""Spec do deck 6.4. Gera 06-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

# 1. duas frases
S.append({"id": "frases", "tipo": "frase", "fundo": "tinta", "eyebrow": "Depois de todo caso",
          "frase": "“Foi azar, não dava para fazer nada.” “Com certeza não fizeram os exames direito.”",
          "apoio": "As duas estão erradas, em direções opostas. A primeira leva ao conformismo; a segunda, à ilusão de que exigir exame basta. Cinco erros, e o quinto é o que mais mata."})

# 2. dois desfechos
S.append({"id": "desfechos", "tipo": "duas", "eyebrow": "Dois colapsos em campo", "titulo": "A diferença esteve nos minutos seguintes",
          "esq": {"t": "2004, Brasil", "cor": "verm",
                  "itens": ["jogador profissional", "avaliado e acompanhado", "caiu em campo", "morreu"]},
          "dir": {"t": "2021, Eurocopa", "cor": "petr",
                  "itens": ["jogador profissional", "compressão em segundos", "desfibrilado no gramado", "sobreviveu e voltou a jogar"]},
          "destaque": "A diferença entre os desfechos não foi o exame de admissão.",
          "destaque_cor": "tinta"})

# 3. frequência
S.append({"id": "frequencia", "tipo": "numeros", "eyebrow": "Erro um: a frequência", "titulo": "Raro, e concentrado",
          "numeros": [{"n": "1 : 53.703", "x": "atletas universitários por ano, no geral", "cor": "tinta"},
                      {"n": "1 : 5.200", "x": "no basquete masculino da primeira divisão", "cor": "verm"},
                      {"n": "6,8", "x": "por 100 mil jovens do futebol inglês", "cor": "ambar"}],
          "destaque": "Raro não é improvável numa vida institucional. Evento raro, fatal e com resposta conhecida é exatamente o evento para o qual se prepara.",
          "destaque_cor": "petr", "fonte": "Harmon, Circulation 2015 · Malhotra, NEJM 2018"})

# 4. causa
S.append({"id": "causa", "tipo": "duas", "eyebrow": "Erro dois: a causa", "titulo": "Dois bons estudos, dois quadros",
          "esq": {"t": "Registro de Maron, 2009", "cor": "ambar",
                  "itens": ["1.866 mortes, 1980 a 2006", "hipertrófica: cerca de 36%", "anomalia coronariana: cerca de 17%", "montado em boa parte a partir de notícias"]},
          "dir": {"t": "Autópsias de Harmon, 2014", "cor": "petr",
                  "itens": ["cada caso julgado por painel", "autópsia negativa: cerca de 31%", "coração estruturalmente normal", "hipertrófica apareceu pouco"]},
          "destaque": "Parte relevante das mortes é doença elétrica. Isso valoriza o eletrocardiograma, limita a imagem e explica por que nenhum exame zera o risco.",
          "destaque_cor": "tinta"})

# 5. quem morre
S.append({"id": "quem", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro três: quem morre", "titulo": "Não só o jovem de elite",
          "cards": [{"t": "Acima dos 35", "x": "a causa dominante é coronariana", "cor": "verm"},
                    {"t": "O destreinado que volta forte", "x": "parado anos, direto para o vigoroso", "cor": "verm"},
                    {"t": "Commotio cordis", "x": "impacto no peito, coração normal; nenhum exame prevê", "cor": "ambar"},
                    {"t": "Calor", "x": "colapso por hipertermia, não cardíaco", "cor": "ambar"},
                    {"t": "Miocardite", "x": "depois de infecção", "cor": "ambar"},
                    {"t": "O amador de fim de semana", "x": "o mais numeroso e o menos coberto", "cor": "petr"}],
          "destaque_cor": "tinta"})

# 6. Malhotra
S.append({"id": "rastreio", "tipo": "numeros", "eyebrow": "Erro quatro: o que o rastreio faz", "titulo": "Rastreio não é vacina",
          "numeros": [{"n": "11.168", "x": "adolescentes com eletro e eco", "cor": "tinta"},
                      {"n": "42", "x": "com doença associada a morte súbita (0,38%): o rastreio funcionou", "cor": "petr"},
                      {"n": "6 de 8", "x": "mortes cardíacas no seguimento com rastreio normal", "cor": "verm"}],
          "destaque": "Reduz, não elimina. Fotografa um momento, e doença genética se expressa com o tempo.",
          "destaque_cor": "verm", "fonte": "Malhotra e colaboradores · New England Journal of Medicine 2018"})

# 7. três consequências
S.append({"id": "consequencias", "tipo": "lista", "eyebrow": "O núcleo da aula", "titulo": "Três consequências",
          "itens": [{"t": "Rastreio exige seguimento", "x": "exame de entrada arquivado numa pasta é quase decorativo", "cor": "petr"},
                    {"t": "Sintoma novo vale mais que exame antigo", "x": "“mas ele fez todos os exames” é a frase mais perigosa da aula", "cor": "verm"},
                    {"t": "A preparação para o evento não é opcional", "x": "não é pessimismo; é a conclusão lógica do dado", "cor": "ambar"}],
          "gap_itens": 26})

# 8. reconhecer
S.append({"id": "reconhecer", "tipo": "duas", "eyebrow": "Erro cinco: o da hora", "titulo": "Caiu sem contato e não responde: é parada",
          "esq": {"t": "O que engana", "cor": "ambar",
                  "itens": ["abalos que parecem convulsão", "respiração agônica, o gasping", "“está respirando, então não é parada”"]},
          "dir": {"t": "A regra", "cor": "verm",
                  "itens": ["parada até prova em contrário", "movimento convulsivo não exclui", "gasping não exclui", "começa compressão, busca o desfibrilador"]},
          "destaque": "Cada minuto de atraso custa sobrevida. Todo o departamento precisa saber a regra de cor.",
          "destaque_cor": "tinta"})

# 9. 89%
S.append({"id": "desfibrilador", "tipo": "cards", "por_linha": 3, "eyebrow": "O número que nenhum exame alcança", "titulo": "89% de sobrevida com o desfibrilador do local usado",
          "cards": [{"t": "Reconhecer rápido", "x": "caiu sem contato e não responde", "cor": "verm"},
                    {"t": "Comprimir cedo", "x": "quem estiver mais perto", "cor": "ambar"},
                    {"t": "Desfibrilar cedo", "x": "aparelho acessível, em minutos", "cor": "petr"}],
          "destaque": "A pergunta certa para clube, escola e prova: “o que vocês fazem quando alguém cai?”. Se é difícil nos clubes profissionais de São Paulo, imagine na várzea.",
          "destaque_cor": "tinta", "fonte": "Registro americano de ensino médio, BJSM 2013 · Revista Brasileira de Medicina do Esporte 2011"})

# 10. cinco correções
S.append({"id": "correcoes", "tipo": "tabela", "eyebrow": "As cinco frases erradas", "titulo": "O que as substitui",
          "cab": ["Frase errada", "O que substitui"],
          "larguras": [36, 64],
          "linhas": [["“É raríssimo.”", "raro, concentrado, e com resposta conhecida: prepare-se"],
                     ["“É sempre hipertrófica.”", "parte relevante é doença elétrica em coração normal"],
                     ["“É coisa de jovem de elite.”", "acima dos 35 é coronária; o amador é o menos coberto"],
                     ["“Com exame não teria acontecido.”", "6 de 8 tinham rastreio normal; seguimento e sintoma"],
                     ["“Deve ser convulsão.”", "caiu e não responde: compressão e desfibrilador"]],
          "destaque_cor": "tinta"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "A parte que mais muda o desfecho não é médica", "titulo": "Os minutos seguintes à queda",
          "regras": ["Rastreio reduz, não elimina; exige seguimento",
                     "Sintoma novo passa por cima de exame antigo",
                     "Caiu sem contato e não responde: compressão e desfibrilador"],
          "cards": [{"t": "Médico", "x": "Pede, interpreta, decide elegibilidade."},
                    {"t": "Quem estiver mais perto", "x": "Reconhece e começa a compressão. Nenhuma profissão é dona dela."},
                    {"t": "A gestão", "x": "Desfibrilador acessível, plano escrito, ensaio periódico."}],
          "quem": "Levar sintoma a sério é de todo mundo."})

spec = {"arquivo": "aulas/MOD06/06-04-morte-subita-no-esporte.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Morte súbita no esporte", "subtitulo": "Frequência, causas e o que muda o desfecho",
        "nota_capa": "Entra pelas duas frases erradas.",
        "secoes": {"frases": ["As frases, os desfechos, frequência e causa.", "capa"],
                   "quem": ["Quem morre e o que o rastreio faz.", "quem"],
                   "reconhecer": ["O erro da hora e as correções.", "reconhecer"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-04.json"), "w"), ensure_ascii=False, indent=1)
print("06-04.json:", len(S), "slides")
