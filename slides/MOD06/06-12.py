"""Spec do deck 6.12. Gera 06-12.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

# 1. caso
S.append({"id": "caso", "tipo": "frase", "fundo": "tinta", "eyebrow": "Caso ilustrativo",
          "frase": "Ouviu que, com rim doente, não podia fazer esforço. E obedeceu.",
          "apoio": "Um homem na casa dos sessenta, com doença renal crônica moderada, diabetes e hipertensão. Anos depois, não levanta da cadeira sem apoio e dorme na sala. O rim pouco mudou."})

# 2. custo
p = [svg_abre(1664, 300, "Esquema ao longo dos anos: a função renal fica quase estável enquanto massa, força e autonomia caem muito")]
p.append(f'<line x1="60" y1="270" x2="1640" y2="270" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M60,80 C500,86 1000,96 1640,108" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append(f'<path d="M60,60 C400,90 700,160 1000,210 C1250,245 1450,255 1640,258" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(1160, 58, "função renal", w=460, tam=28, cor=AZUL, peso=700, alinha="right"),
      rot(900, 176, "massa, força e autonomia", w=720, tam=28, cor=FOSF, peso=700, alinha="right"),
      rot(80, 278, "o diagnóstico", w=300, tam=24, cor=MUDO),
      rot(1340, 278, "anos depois", w=300, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "custo", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O custo do afastamento", "titulo": "A frase protegeu o rim de um risco que não estava ali",
          "destaque": "Na doença renal crônica, a principal causa de morte é cardiovascular. A diretriz de 2024 recomenda atividade moderada, 150 minutos por semana ou o tolerado.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · KDIGO 2024, recomendação 3.2.2.1"})

# 3. inversão
S.append({"id": "inversao", "tipo": "tabela", "eyebrow": "A mesma inversão em quase toda doença crônica", "titulo": "Não é se pode treinar, é como",
          "cab": ["Condição", "O que as diretrizes dizem"],
          "larguras": [30, 70],
          "linhas": [["Doença renal crônica", "atividade moderada, 150 min por semana ou o tolerado"],
                     ["Diabetes tipo 2", "exercício é tratamento: glicemia, insulina, risco cardiovascular"],
                     ["Hipertensão", "reduz a pressão; entre as primeiras condutas"],
                     ["Asma", "melhora o condicionamento, bem tolerado"],
                     ["Câncer", "exercício durante e depois do tratamento"],
                     ["Cardiopatia estável", "exercício supervisionado faz parte do tratamento"]],
          "destaque": "Autonomia não é desfecho secundário: levantar da cadeira, subir escada, dormir no próprio quarto.",
          "destaque_cor": "tinta"})

# 4. três perguntas
S.append({"id": "perguntas", "tipo": "lista", "eyebrow": "O que organiza qualquer caso", "titulo": "Três perguntas antes da prescrição",
          "itens": [{"t": "Existe instabilidade clínica agora?", "x": "onde moram as contraindicações reais, quase todas temporárias", "cor": "verm"},
                    {"t": "Que medicações usa, e o que fazem no esforço?", "x": "a pergunta que mais muda a prescrição", "cor": "ambar"},
                    {"t": "O que consegue fazer hoje?", "x": "não o que a diretriz recomenda: o que ela consegue", "cor": "petr"}],
          "gap_itens": 26})

# 5. contraindicações
S.append({"id": "agora", "tipo": "cards", "por_linha": 4, "eyebrow": "As contraindicações de verdade", "titulo": "Quase tudo é “agora”, não “para sempre”",
          "cards": [{"t": "Coronária instável", "x": "síndrome aguda recente, angina instável", "cor": "verm"},
                    {"t": "Coração descompensado", "x": "insuficiência cardíaca, arritmia não controlada", "cor": "verm"},
                    {"t": "Pressão muito alta", "x": "e não controlada", "cor": "verm"},
                    {"t": "Febre", "x": "infecção aguda", "cor": "ambar"},
                    {"t": "Metabólico", "x": "cetose, hipoglicemia grave recente", "cor": "ambar"},
                    {"t": "Lesão em investigação", "x": "", "cor": "ambar"},
                    {"t": "Sintoma novo no esforço", "x": "que ninguém avaliou", "cor": "verm"},
                    {"t": "A conduta", "x": "“hoje não, por isso; vamos resolver e começar”", "cor": "petr"}],
          "destaque": "O erro simétrico ao afastamento é a prescrição impossível: fracasso, culpa e abandono.",
          "destaque_cor": "tinta"})

# 6. medicações
S.append({"id": "remedios", "tipo": "tabela", "eyebrow": "O núcleo prático", "titulo": "Remédios que mudam a prescrição",
          "cab": ["Medicação", "O que exige no treino"],
          "larguras": [30, 70],
          "linhas": [["Betabloqueador", "sem alvo de FC por fórmula; percepção de esforço, fala, teste com o remédio"],
                     ["Insulina, sulfonilureia", "glicemia antes, carboidrato à mão, hipoglicemia tardia"],
                     ["Inibidor de SGLT2", "hidratação e calor; cetoacidose rara com glicemia pouco alta"],
                     ["Diurético", "volume, eletrólitos, cãibra"],
                     ["Anti-hipertensivos", "tontura ao terminar: desaquecer"],
                     ["Estatina, anticoagulante", "ouvir a dor muscular; contato e queda"]],
          "destaque": "Quem prescreve treino precisa saber o que a pessoa toma, e quem prescreve remédio precisa saber que ela treina.",
          "destaque_cor": "verm"})

# 7. diabetes
S.append({"id": "diabetes", "tipo": "numeros", "eyebrow": "Diabetes tipo 2, o mais frequente", "titulo": "O benefício tem prazo de validade",
          "numeros": [{"n": "24 a 72 h", "x": "de sensibilidade à insulina depois de uma sessão aeróbica", "cor": "petr"},
                      {"n": "2 dias", "x": "no máximo, seguidos, sem atividade aeróbica", "cor": "ambar"},
                      {"n": "+ força", "x": "o músculo é o principal destino da glicose", "cor": "tinta"}],
          "destaque": "Cuidados: hipoglicemia com insulina e sulfonilureia, inspeção dos pés, neuropatia autonômica, retinopatia. Glicemia alta com cetose: dia de resolver o controle.",
          "destaque_cor": "verm", "fonte": "Associação Americana de Diabetes, Diabetes Care 2016"})

# 8. outras
S.append({"id": "outras", "tipo": "cards", "por_linha": 2, "eyebrow": "As outras condições", "titulo": "Ajustar, não parar",
          "cards": [{"t": "Hipertensão", "x": "aeróbio com força; pressão descontrolada adia a sessão; desaquecer", "cor": "petr"},
                    {"t": "Cardiopatia estável", "x": "a prescrição sai de um teste, compartilhada com a cardiologia", "cor": "petr"},
                    {"t": "Câncer", "x": "cerca de 30 min, 3 vezes por semana, força ao menos 2; fadiga, humor, função", "cor": "ambar"},
                    {"t": "Doença renal", "x": "força no centro; proteína, sódio, potássio e fósforo com nutrição e nefrologia", "cor": "ambar"}],
          "destaque": "Ninguém aumenta proteína por conta própria em quem tem doença renal, e isso inclui suplemento da loja.",
          "destaque_cor": "tinta", "fonte": "Mesa-redonda internacional de exercício no câncer, Med Sci Sports Exerc 2019"})

# 9. plano
S.append({"id": "plano", "tipo": "lista", "eyebrow": "O caso, conduzido pelo que a aula construiu", "titulo": "A meta não está no laudo",
          "itens": [{"t": "Avaliar", "x": "estabilidade, seis remédios revisados, função; teste de esforço com a medicação", "cor": "tinta"},
                    {"t": "Começar pelo possível", "x": "levantar da cadeira com apoio, caminhadas curtas em casa", "cor": "petr"},
                    {"t": "Progredir", "x": "força duas vezes por semana; intensidade pela percepção, não pela FC", "cor": "petr"},
                    {"t": "Combinar a equipe", "x": "nutrição, nefrologia, endocrinologia; tontura ao terminar volta ao médico", "cor": "ambar"}],
          "destaque": "A meta que importa: voltar a subir a escada e dormir no próprio quarto.",
          "destaque_cor": "tinta"})

# 10. regras
S.append({"id": "regras", "tipo": "cards", "por_linha": 3, "eyebrow": "As regras que o caso entrega", "titulo": "Afastar é uma intervenção",
          "cards": [{"t": "Afastar tem efeito adverso", "x": "e pede reavaliação", "cor": "verm"},
                    {"t": "Como, não se", "x": "contraindicações específicas e temporárias", "cor": "petr"},
                    {"t": "A medicação muda a prescrição", "x": "", "cor": "ambar"},
                    {"t": "Comece pelo que consegue", "x": "a prescrição impossível também faz mal", "cor": "petr"},
                    {"t": "Força não é opcional", "x": "é o que preserva autonomia", "cor": "petr"},
                    {"t": "O desfecho nem sempre é o exame", "x": "às vezes é a escada", "cor": "tinta"}],
          "destaque_cor": "tinta"})

# 11. decisão e contribuição
S.append({"id": "niveis", "tipo": "duas", "eyebrow": "O módulo nos três níveis", "titulo": "Decisão e contribuição",
          "esq": {"t": "Decisão", "cor": "tinta",
                  "itens": ["médico: exames, elegibilidade, remédio, retorno", "cardiologia na zona cinzenta", "preparação: carga liberada", "fisio, nutrição, psicologia no seu campo", "gestão: desfibrilador, plano, ensaio"]},
          "dir": {"t": "Contribuição", "cor": "petr",
                  "itens": ["teste do pescoço na sexta", "FC alta para a carga depois da virose", "estridor no asmático que não melhora", "incoordenação depois do choque", "a primeira compressão sem dono"]},
          "destaque": "A decisão administrativa que mais muda desfecho no módulo é da gestão.",
          "destaque_cor": "tinta"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Reconhecimento: de todos",
          "titulo": "Exame, remédio e afastamento são intervenções",
          "regras": ["Síncope no esforço, morte súbita na família, “hipertrofia” no laudo",
                     "Caiu sem contato e não responde; tosse que todo mundo tem; febre na véspera",
                     "Gelo na boca, check-up completo, comprimido no vestiário, “não pode fazer esforço”"],
          "cards": [{"t": "Decisão", "x": "Cada profissão decide no seu campo, com registro."},
                    {"t": "Contribuição", "x": "A informação que atravessa profissões."},
                    {"t": "Reconhecimento", "x": "Não exige a profissão certa. Exige ter aprendido o sinal."}],
          "quem": "Todas pedem uma pergunta clínica antes. Próximo módulo: lesões, mecanismos, epidemiologia e prevenção."})

spec = {"arquivo": "aulas/MOD06/06-12-exercicio-e-doenca-cronica.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Exercício na doença crônica", "subtitulo": "Prescrição segura e o custo do afastamento",
        "nota_capa": "Entra pelo caso ilustrativo.",
        "secoes": {"caso": ["O caso e o custo do afastamento.", "capa"],
                   "perguntas": ["As três perguntas, os remédios e as condições.", "perguntas"],
                   "plano": ["O plano do caso, as regras e o fecho do módulo.", "plano"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-12.json"), "w"), ensure_ascii=False, indent=1)
print("06-12.json:", len(S), "slides")
