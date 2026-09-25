"""Spec do deck 7.11. Gera 07-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "dedo", "tipo": "frase", "fundo": "tinta", "eyebrow": "O gesto que muda a conversa",
          "frase": "A dor apontada com a ponta de um dedo.",
          "apoio": "Num ponto do osso, depois de aumento de carga, piorando conforme a corrida avança. Começa pequena, dá para correr com ela, até o dia em que não dá mais."})

S.append({"id": "balanca", "tipo": "duas", "eyebrow": "A fisiologia em trinta segundos", "titulo": "Dano mais rápido que reparo",
          "esq": {"t": "A carga subiu demais", "cor": "ambar",
                  "itens": ["aumento de volume", "mudança de superfície", "volta de férias num esporte de impacto"]},
          "dir": {"t": "O reparo caiu", "cor": "verm",
                  "itens": ["energia disponível baixa", "hormônios, vitamina D, cálcio", "sono curto"]},
          "destaque": "Tirar o impacto e esperar resolve o episódio e deixa a causa de pé.",
          "destaque_cor": "tinta"})

S.append({"id": "reconhecer", "tipo": "lista", "eyebrow": "Sem exame", "titulo": "O padrão que qualquer um da equipe reconhece",
          "itens": [{"t": "Localizada", "x": "apontada com o dedo", "cor": "verm"},
                    {"t": "Depois de mudança de carga", "x": "nas últimas semanas", "cor": "ambar"},
                    {"t": "Piora com a atividade", "x": "não melhora com o aquecimento; segue depois de parar", "cor": "verm"},
                    {"t": "Progride", "x": "até doer andando ou em repouso", "cor": "verm"}],
          "gap_itens": 22, "destaque": "Dor à percussão do osso ou ao saltitar num pé só, num ponto: encaminhar.",
          "destaque_cor": "verm"})

S.append({"id": "diferencial", "tipo": "duas", "eyebrow": "O que parece e é mais brando", "titulo": "Lesão óssea ou estresse tibial medial",
          "esq": {"t": "Lesão óssea por estresse", "cor": "verm",
                  "itens": ["um ponto", "piora com a atividade", "progride ao longo dos dias"]},
          "dir": {"t": "Estresse tibial medial", "cor": "ambar",
                  "itens": ["vários centímetros na borda interna", "aparece no começo, melhora aquecido", "manejo parecido, prazo menor"]},
          "destaque": "A avaliação médica decide. O que não pode é tratar dor localizada e progressiva como dor muscular.",
          "destaque_cor": "tinta"})

S.append({"id": "risco", "tipo": "duas", "eyebrow": "A divisão que decide a urgência", "titulo": "Sítios de alto e de baixo risco",
          "esq": {"t": "Alto risco", "cor": "verm",
                  "itens": ["colo do fêmur, lado da tensão", "borda anterior da tíbia", "maléolo medial", "navicular; base do quinto metatarso"]},
          "dir": {"t": "Baixo risco", "cor": "petr",
                  "itens": ["face posteromedial da tíbia", "fíbula", "maior parte dos metatarsos", "pega cedo: caminho tranquilo"]},
          "destaque": "Tensão e irrigação pobre consolidam pior e podem evoluir para fratura completa.",
          "destaque_cor": "tinta", "fonte": "Warden e colegas, J Orthop Sports Phys Ther 2014"})

S.append({"id": "naoespera", "tipo": "frase", "fundo": "tinta", "eyebrow": "Encaminhamento imediato",
          "frase": "Virilha no corredor, meio do pé, frente da canela: não esperam duas semanas.",
          "apoio": "A diferença entre um desfecho tranquilo e meses fora, muitas vezes, é o tempo que alguém levou para levar a queixa a sério."})

S.append({"id": "energia", "tipo": "numeros", "eyebrow": "A raiz energética · atletas de elite de fundo e meio-fundo", "titulo": "Quando o corpo economiza, o osso paga",
          "numeros": [{"n": "37%", "x": "das mulheres com amenorreia", "cor": "ambar"},
                      {"n": "40%", "x": "dos homens com testosterona baixa", "cor": "ambar"},
                      {"n": "× 4,5", "x": "a taxa de lesão nesses grupos", "cor": "verm"}],
          "destaque": "Baixa disponibilidade de energia é difícil de medir, mas as consequências pesam nas lesões ósseas.",
          "destaque_cor": "verm", "fonte": "Int J Sport Nutr Exerc Metab 2018"})

S.append({"id": "detalhes", "tipo": "cards", "por_linha": 2, "eyebrow": "Dois detalhes desses números", "titulo": "Não é só elite, e não é só mulher",
          "cards": [{"t": "Inclui homens", "x": "o problema ficou conhecido no esporte feminino e deixou de ser procurado no homem", "cor": "ambar"},
                    {"t": "Não é só elite", "x": "dieta da moda, jejum com treino e “emagrecer é sempre bom” no praticante comum", "cor": "verm"}],
          "destaque": "Deficiência relativa de energia no esporte: consenso do COI de 2023, tratado no módulo de nutrição.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2023"})

S.append({"id": "perguntas", "tipo": "cards", "por_linha": 4, "eyebrow": "Sempre, e nenhuma é sobre osso", "titulo": "Quatro perguntas obrigatórias",
          "cards": [{"t": "Alimentação", "x": "e perda de peso recente", "cor": "ambar"},
                    {"t": "Ciclo menstrual", "x": "ausência ou irregularidade é sinal", "cor": "verm"},
                    {"t": "Fraturas antes", "x": "outras lesões por estresse", "cor": "ambar"},
                    {"t": "Sono", "x": "quanto e como", "cor": "petr"}],
          "destaque": "É a diferença entre tratar o episódio e resolver o problema.", "destaque_cor": "tinta"})

S.append({"id": "volta", "tipo": "lista", "eyebrow": "Prazo e volta", "titulo": "Faixas, não datas",
          "itens": [{"t": "Baixo risco, pego cedo", "x": "semanas até a volta progressiva ao impacto", "cor": "petr"},
                    {"t": "Fratura estabelecida", "x": "mais tempo", "cor": "ambar"},
                    {"t": "Alto risco", "x": "muito mais; às vezes imobilização ou cirurgia", "cor": "verm"},
                    {"t": "Durante o afastamento", "x": "bicicleta, piscina, remo, força: preserva capacidade e cabeça", "cor": "tinta"}],
          "gap_itens": 22})

S.append({"id": "recidiva", "tipo": "frase", "fundo": "tinta", "eyebrow": "A parte que evita a recidiva",
          "frase": "Sem corrigir a causa energética, o retorno é frágil.",
          "apoio": "Quem repete costuma ter voltado com a mesma alimentação, a mesma ausência de ciclo e a mesma progressão que produziram a primeira."})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Lesão óssea por estresse", "titulo": "Quase nunca é só osso",
          "regras": ["Dor apontada com o dedo: lesão óssea até prova em contrário",
                     "Sítio de alto risco não espera",
                     "Pergunte por energia, ciclo, fraturas e sono"],
          "cards": [{"t": "Médico e fisioterapia", "x": "Risco do sítio, imagem, afastamento e retorno."},
                    {"t": "Nutrição e preparação", "x": "Energia suficiente; condicionamento por outras vias."},
                    {"t": "Quem está mais perto", "x": "Reconhece o gesto do dedo e encaminha."}],
          "quem": "Próxima aula: imagem no esporte e o achado incidental."})

spec = {"arquivo": "aulas/MOD07/07-11-lesao-ossea-de-estresse-e-sua-raiz-energetica.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Lesão óssea por estresse", "subtitulo": "Sítio de risco, reconhecimento e a raiz energética",
        "nota_capa": "Entra pelo gesto do dedo.",
        "secoes": {"dedo": ["Fisiologia e reconhecimento.", "capa"],
                   "risco": ["Sítios de alto e baixo risco.", "risco"],
                   "energia": ["A raiz energética, o prazo e a recidiva.", "energia"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-11.json"), "w"), ensure_ascii=False, indent=1)
print("07-11.json:", len(S), "slides")
