"""Spec do deck 7.6. Gera 07-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "cena", "tipo": "frase", "fundo": "tinta", "eyebrow": "No terceiro passo",
          "frase": "Não caiu, ninguém encostou. Só parou.",
          "apoio": "Gelo, anti-inflamatório, repouso, ressonância e a pergunta que não para. Esta aula é essa sequência, da mão na coxa até o jogo."})

S.append({"id": "custo", "tipo": "numeros", "eyebrow": "Um clube de elite brasileiro, uma temporada", "titulo": "Por que uma aula inteira sobre isso",
          "numeros": [{"n": "34", "x": "jogadores acompanhados, só lesão de posterior de coxa", "cor": "tinta"},
                      {"n": "US$ 43 mi", "x": "perda potencial estimada, quase toda pelo desempenho da equipe", "cor": "verm"},
                      {"n": "2", "x": "fatores associados: lesão prévia e déficit dos flexores do joelho", "cor": "petr"}],
          "destaque": "Estudo piloto, um clube, conta estimada. Mas a ordem de grandeza diz alguma coisa.",
          "destaque_cor": "tinta", "fonte": "Front Sports Act Living 2024"})

S.append({"id": "graus", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo um · acertar o nome", "titulo": "Os três graus da beira do campo",
          "cards": [{"t": "Grau 1", "x": "poucas fibras, dor localizada, força e amplitude quase preservadas", "cor": "petr"},
                    {"t": "Grau 2", "x": "ruptura parcial, não continua, força cai, roxo dias depois", "cor": "ambar"},
                    {"t": "Grau 3", "x": "ruptura completa ou arrancamento, afundamento palpável", "cor": "verm"}],
          "destaque": "Estalo forte, dor para sentar e hematoma descendo pela coxa: arrancamento alto, avaliação ortopédica em dias.",
          "destaque_cor": "verm"})

S.append({"id": "imitacoes", "tipo": "cards", "por_linha": 4, "eyebrow": "O que parece estiramento e não é", "titulo": "Descarte antes de tratar",
          "cards": [{"t": "Dor tardia", "x": "horas depois, difusa, dos dois lados, sem momento exato", "cor": "petr"},
                    {"t": "Contusão", "x": "pancada; não massagear forte nem aquecer no início", "cor": "ambar"},
                    {"t": "Câimbra", "x": "trava e solta, sem dor localizada depois", "cor": "petr"},
                    {"t": "Dor da coluna", "x": "sem momento claro, piora sentado com perna e pescoço", "cor": "verm"}],
          "destaque": "O estiramento tem hora marcada: a pessoa diz o segundo em que doeu.",
          "destaque_cor": "tinta"})

p = [svg_abre(1664, 260, "Linha do tempo das siglas: PRICE, depois POLICE em 2012, depois PEACE and LOVE em 2019")]
p.append(f'<line x1="120" y1="120" x2="1560" y2="120" stroke="{MUDO}" stroke-width="4"/>')
for x, c in [(220, MUDO), (820, AZUL), (1420, OXID)]:
    p.append(f'<circle cx="{x}" cy="120" r="22" fill="{c}"/>')
p.append("</svg>")
rs = [rot(20, 20, "PRICE", w=400, tam=40, cor=MUDO, peso=700, alinha="center"),
      rot(620, 20, "POLICE · 2012", w=400, tam=40, cor=AZUL, peso=700, alinha="center"),
      rot(1180, 20, "PEACE & LOVE · 2019", w=480, tam=40, cor=OXID, peso=700, alinha="center"),
      rot(20, 160, "proteção, repouso, gelo, compressão, elevação", w=400, tam=22, cor=MUDO, alinha="center"),
      rot(620, 160, "sai o repouso, entra a carga ideal", w=400, tam=22, cor=AZUL, alinha="center"),
      rot(1180, 160, "sai o gelo, entra evitar anti-inflamatório", w=480, tam=22, cor=OXID, alinha="center")]
S.append({"id": "siglas", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo dois · as primeiras horas", "titulo": "A história das siglas mostra o que mudou",
          "destaque": "A mudança mais importante não é uma letra que entrou. É uma que saiu.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2012 e 2020"})

S.append({"id": "peace", "tipo": "lista", "eyebrow": "Os primeiros dias", "titulo": "PEACE",
          "itens": [{"t": "Proteger", "x": "poupar de um a três dias; não é imobilizar", "cor": "petr"},
                    {"t": "Elevar", "x": "acima do coração quando der; custo zero", "cor": "petr"},
                    {"t": "Evitar anti-inflamatório", "x": "a inflamação é o começo do conserto", "cor": "verm"},
                    {"t": "Comprimir", "x": "faixa ou malha contra inchaço e hematoma", "cor": "petr"},
                    {"t": "Educar", "x": "a letra mais importante e a que menos se faz", "cor": "tinta"}],
          "gap_itens": 16, "fonte": "Br J Sports Med 2020"})

S.append({"id": "love", "tipo": "lista", "eyebrow": "Depois dos primeiros dias", "titulo": "LOVE",
          "itens": [{"t": "Carga", "x": "isométrico, depois movimento, depois carga crescente", "cor": "petr"},
                    {"t": "Otimismo", "x": "como a equipe fala da lesão faz parte do tratamento", "cor": "ambar"},
                    {"t": "Vascularização", "x": "aeróbico sem dor, desde cedo: bicicleta, piscina", "cor": "petr"},
                    {"t": "Exercício", "x": "força, amplitude e controle até o gesto do esporte", "cor": "tinta"}],
          "gap_itens": 22, "destaque": "Poucos dias de proteção inteligente, depois carga progressiva. Nenhuma letra é repouso absoluto.",
          "destaque_cor": "tinta"})

S.append({"id": "aine", "tipo": "duas", "eyebrow": "Passo três · anti-inflamatório", "titulo": "Não entra de forma automática",
          "esq": {"t": "Por quê", "cor": "verm",
                  "itens": ["a inflamação inicial é o começo do reparo", "a mesma via participa da resposta ao treino", "doses altas por semanas: menor ganho de massa em jovens"]},
          "dir": {"t": "O que fazer", "cor": "petr",
                  "itens": ["analgésico para a dor, por decisão médica", "curso curto só em situação específica", "nunca o comprimido do vestiário"]},
          "destaque_cor": "tinta", "fonte": "Revisão, Scand J Med Sci Sports 2018"})

S.append({"id": "gelo", "tipo": "cards", "por_linha": 3, "eyebrow": "E o gelo", "titulo": "Conforto, não tratamento",
          "cards": [{"t": "Alivia a dor", "x": "por pouco tempo, e isso é real", "cor": "petr"},
                    {"t": "Reparo: contraditório", "x": "em ratos, menos inflamação sem mudar a regeneração; outros sugerem atraso", "cor": "ambar"},
                    {"t": "Em gente", "x": "sem prova clara de que acelere a volta", "cor": "verm"}],
          "destaque": "Se alivia, pode usar nos primeiros dias. Não é obrigatório e não é o centro da conversa.",
          "destaque_cor": "tinta", "fonte": "Estudo brasileiro em ratos, Sci Rep 2016"})

S.append({"id": "curcuma", "tipo": "duas", "eyebrow": "Passo quatro · a cúrcuma", "titulo": "Resposta com as duas mãos",
          "esq": {"t": "O que mostra", "cor": "petr",
                  "itens": ["14 ensaios, 349 pessoas", "menos dor e marcadores de dano", "mais amplitude depois do exercício"]},
          "dir": {"t": "O que não mostra", "cor": "verm",
                  "itens": ["estudos de dor tardia, não de ruptura", "sem prova de retorno mais rápido", "anti-inflamatório brando, nunca testado aqui"]},
          "destaque": "Coadjuvante para o conforto, com procedência e conversa com o médico. Não substitui carga.",
          "destaque_cor": "tinta", "fonte": "Metanálise, PLoS One 2024"})

S.append({"id": "reabilitacao", "tipo": "numeros", "eyebrow": "Passo cinco · a travessia até o jogo", "titulo": "Exercício em alongamento, 75 jogadores",
          "numeros": [{"n": "28 dias", "x": "retorno médio com o protocolo em alongamento", "cor": "petr"},
                      {"n": "51 dias", "x": "retorno médio com a reabilitação convencional", "cor": "verm"}],
          "destaque": "Desconforto tolerável: mesmo prazo, mais força e fibras mais preservadas. Quem lesionou correndo corre rápido na reabilitação antes do jogo.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2013 · J Orthop Sports Phys Ther 2020 · consenso de Berna 2016"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Do primeiro dia ao retorno", "titulo": "Poucos dias de proteção, muita carga bem dosada",
          "regras": ["Descarte o arrancamento e as imitações",
                     "Sem anti-inflamatório de rotina; gelo é conforto",
                     "Critério em vez de calendário"],
          "cards": [{"t": "Médico", "x": "Diagnostica, gradua, decide imagem, medicação e alta."},
                    {"t": "Fisioterapia e preparação", "x": "Conduzem a carga, os degraus e a volta à corrida."},
                    {"t": "Treinador", "x": "Aceita o critério e protege o atleta da pressa."}],
          "quem": "Próxima aula: o tendão, que dói por meses e quase nunca afasta."})

spec = {"arquivo": "aulas/MOD07/07-06-estiramento-muscular-manejo-do-primeiro-dia-ao-retorno.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Manejo do estiramento muscular", "subtitulo": "Do primeiro dia ao retorno",
        "nota_capa": "Entra pela cena do terceiro passo.",
        "secoes": {"cena": ["A cena, o custo e o nome certo.", "capa"],
                   "siglas": ["As siglas, PEACE e LOVE.", "siglas"],
                   "aine": ["Anti-inflamatório, gelo e cúrcuma.", "aine"],
                   "reabilitacao": ["A travessia até o jogo.", "reabilitacao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-06.json"), "w"), ensure_ascii=False, indent=1)
print("07-06.json:", len(S), "slides")
