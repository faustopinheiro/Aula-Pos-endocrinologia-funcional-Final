"""Spec do deck 6.2. Gera 06-02.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a frase
S.append({"id": "pergunta", "tipo": "frase", "fundo": "tinta", "eyebrow": "A frase que organiza a aula",
          "frase": "Exame não responde se a pessoa está bem. Responde a uma pergunta, e mal às outras.",
          "apoio": "O eletrocardiograma foi desenhado para achar o que mata o jovem. O adulto de meia-idade morre de coronária, que um eletrocardiograma normal não exclui."})

# 2. três pedidos
S.append({"id": "pedidos", "tipo": "cards", "por_linha": 3, "eyebrow": "Três pedidos típicos", "titulo": "A mesma coisa, necessidades diferentes",
          "cards": [{"t": "O clube", "x": "“exame do coração para liberar” o jogador da base", "cor": "petr"},
                    {"t": "O check-up completo", "x": "mulher de meia-idade, vai começar a correr, “está tudo normal”", "cor": "ambar"},
                    {"t": "O preparador", "x": "quer exigir eletrocardiograma de todos os alunos", "cor": "verm"}],
          "destaque": "A decisão não é pedir ou não pedir. É que pergunta estou fazendo, e que ferramenta responde.",
          "destaque_cor": "tinta"})

# 3. as curvas
p = [svg_abre(1664, 340, "Esquema de duas curvas ao longo da idade: causas estruturais e genéticas caem, doença coronariana sobe, cruzando perto dos 35 anos")]
p.append(f'<line x1="60" y1="290" x2="1640" y2="290" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M60,130 C400,135 600,225 800,250 C1100,282 1400,286 1640,288" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M60,285 C400,282 600,262 800,235 C1100,190 1400,140 1640,120" fill="none" stroke="{AZUL}" stroke-width="6"/>')
xc = 60 + (35 - 10) / 60 * 1580
p.append(f'<line x1="{xc:.0f}" y1="30" x2="{xc:.0f}" y2="290" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 8"/>')
p.append("</svg>")
rs = [rot(80, 20, "estrutural e genética", w=600, tam=30, cor=FOSF, peso=700),
      rot(80, 64, "cardiomiopatias, canalopatias, coronária anômala, miocardite", w=900, tam=24, cor=TINTA),
      rot(1060, 40, "doença coronariana", w=560, tam=30, cor=AZUL, peso=700, alinha="right"),
      rot(xc - 100, 300, "perto dos 35 anos", w=200, tam=24, cor=MUDO, peso=600, alinha="center")]
for idade in (10, 30, 50, 70):
    xi = 60 + (idade - 10) / 60 * 1580
    if idade != 30:
        rs.append(rot(min(max(xi - 50, 0), 1564), 300, f"{idade} anos", w=100, tam=24, cor=MUDO, alinha="center"))
S.append({"id": "idade", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A primeira variável", "titulo": "A idade muda a doença que se procura",
          "destaque": "As duas doenças pedem ferramentas diferentes, e é aí que nasce quase todo erro de pedido.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# 4. o que o ECG vê
S.append({"id": "ecg", "tipo": "duas", "eyebrow": "O eletrocardiograma de repouso", "titulo": "Doença elétrica e estrutural, não coronária",
          "esq": {"t": "Vê bem", "cor": "petr",
                  "itens": ["padrão de cardiomiopatia hipertrófica", "sinais de cardiomiopatia arritmogênica", "pré-excitação", "QT longo, Brugada", "bloqueios e sobrecargas"]},
          "dir": {"t": "Não vê", "cor": "verm",
                  "itens": ["coronária obstruída em quem não tem sintoma", "mostra cicatriz de infarto silencioso", "normal não tranquiliza sobre a coronária"]},
          "destaque": "Depois dos quarenta, a ferramenta que importa é a avaliação de risco cardiovascular. Check-up completo é conceito de marketing.",
          "destaque_cor": "verm"})

# 5. Corrado
S.append({"id": "corrado", "tipo": "numeros", "eyebrow": "Corrado e colaboradores, 2006", "titulo": "O argumento do Vêneto",
          "numeros": [{"n": "3,6", "x": "mortes súbitas cardiovasculares por 100 mil atletas-ano, antes do rastreio", "cor": "verm"},
                      {"n": "0,4", "x": "no período tardio do rastreio com eletrocardiograma", "cor": "petr"},
                      {"n": "−89%", "x": "queda concentrada nas mortes por cardiomiopatia", "cor": "tinta"}],
          "destaque": "Observacional, de uma região, 1979 a 2004. É o dado que sustenta a posição europeia, e o debate sobre generalizá-lo continua.",
          "destaque_cor": "ambar", "fonte": "Atletas de 12 a 35 anos · JAMA 2006"})

# 6. posições
S.append({"id": "posicoes", "tipo": "tabela", "eyebrow": "Os mesmos dados, decisões diferentes", "titulo": "Onde o Brasil está",
          "cab": ["Posição", "Eletrocardiograma no jovem competitivo", "O argumento"],
          "larguras": [20, 38, 42],
          "linhas": [["Europeia", "rastreio de todos", "a experiência italiana"],
                     ["Americana", "história e exame físico de 14 itens; sem rastreio universal", "custo, estrutura, falso-positivo"],
                     ["Brasileira, 2019", "classe I, nível A, no profissional e no amador", "ergometria antes de alta intensidade com força menor; eco confirmatório"]],
          "destaque": "Quando o clube ou a federação pede eletrocardiograma, não é excesso. Está na diretriz.",
          "destaque_cor": "petr", "fonte": "SBC e SBMEE, Arquivos Brasileiros de Cardiologia 2019"})

# 7. leitura
S.append({"id": "leitura", "tipo": "duas", "eyebrow": "Drezner e colaboradores, 2017", "titulo": "Pedir é fácil; ler é o que decide",
          "esq": {"t": "Adaptação: isolada, não investiga", "cor": "petr",
                  "itens": ["bradicardia sinusal", "arritmia sinusal respiratória", "bloqueio AV de primeiro grau", "repolarização precoce", "voltagem isolada de hipertrofia"]},
          "dir": {"t": "Sempre investiga", "cor": "verm",
                  "itens": ["inversão de onda T em certas derivações", "depressão de ST", "onda Q patológica", "pré-excitação; QT muito longo ou curto", "arritmia ventricular"]},
          "destaque": "O laudo automático do aparelho não usa critério de atleta. Exame sem leitura treinada produz mais dano que benefício.",
          "destaque_cor": "tinta", "fonte": "Critérios internacionais · British Journal of Sports Medicine 2017"})

# 8. ferramentas do adulto
S.append({"id": "adulto", "tipo": "lista", "eyebrow": "O adulto de meia-idade", "titulo": "Quatro ferramentas, em ordem",
          "itens": [{"t": "Cálculo de risco cardiovascular", "x": "idade, sexo, pressão, colesterol, diabetes, tabagismo; custa zero", "cor": "petr"},
                    {"t": "Teste ergométrico", "x": "com sintoma, doença conhecida, alto risco e esforço vigoroso; e para prescrever", "cor": "petr"},
                    {"t": "Escore de cálcio", "x": "reclassifica o risco intermediário; conversa com a cardiologia", "cor": "ambar"},
                    {"t": "Ecocardiograma", "x": "por indicação: sopro, eletro alterado, sintoma, história familiar", "cor": "ambar"}],
          "destaque": "Ergometria em quem é de baixo risco e sem sintoma: falso-positivo alto, valor preditivo baixo, e uma cascata.",
          "destaque_cor": "verm", "gap_itens": 18})

# 9. o que não pedir
S.append({"id": "naopedir", "tipo": "cards", "por_linha": 4, "eyebrow": "A metade esquecida", "titulo": "O que não pedir",
          "cards": [{"t": "Eco de rotina", "x": "sem sintoma e sem indicação", "cor": "verm"},
                    {"t": "Ergometria anual", "x": "em baixo risco", "cor": "verm"},
                    {"t": "Painel gigante", "x": "em quem não tem pergunta", "cor": "verm"},
                    {"t": "Check-up completo", "x": "caro, tranquilizador, sem resposta", "cor": "verm"}],
          "destaque_cor": "tinta"})

# 10. perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "A decisão consolidada", "titulo": "Por perfil típico",
          "cab": ["Perfil", "O que pedir"],
          "larguras": [28, 72],
          "linhas": [["Jovem federado", "história e exame físico estruturados; eletrocardiograma lido com critério de atleta"],
                     ["Jovem recreacional", "anamnese no centro; eletrocardiograma razoável e amparado"],
                     ["Adulto iniciante sem sintoma", "risco calculado, pressão, colesterol, glicemia; ergometria se alto risco ou vigoroso"],
                     ["Adulto com doença conhecida", "avaliação funcional para prescrever, não para liberar"]],
          "destaque": "Sintoma no esforço, história familiar de morte súbita ou achado no exame físico transformam a triagem em investigação.",
          "destaque_cor": "verm"})

# 11. três respostas
S.append({"id": "respostas", "tipo": "tabela", "eyebrow": "Os três pedidos do começo", "titulo": "Três respostas",
          "cab": ["Pedido", "Resposta"],
          "larguras": [24, 76],
          "linhas": [["O clube", "legítimo; anamnese de verdade, história familiar perguntada, eletro lido com critério de atleta"],
                     ["O check-up completo", "desmontar o “completo”; calcular o risco; progressão; sintoma no esforço, para"],
                     ["O preparador", "exame sem leitura transfere risco; questionário, perguntas, encaminhamento e desfibrilador"]],
          "destaque": "Um plano de emergência ensaiado salva mais que uma gaveta de eletrocardiogramas que ninguém olhou.",
          "destaque_cor": "petr"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Que pergunta, que ferramenta", "titulo": "A idade muda a doença; a pergunta escolhe o exame",
          "regras": ["Abaixo dos 35, estrutural e elétrica; acima, coronariana",
                     "No Brasil, eletrocardiograma no atleta, inclusive amador, lido com critério de atleta",
                     "No adulto, decide o risco calculado, não a bateria de exames"],
          "cards": [{"t": "Médico", "x": "Pede, interpreta e decide."},
                    {"t": "Educador físico e preparador", "x": "Progride a carga; usa o teste ergométrico quando existe."},
                    {"t": "Todos", "x": "Perguntam o sintoma e a história familiar, e encaminham."}],
          "quem": "Exame normal não autoriza pular a progressão."})

spec = {"arquivo": "aulas/MOD06/06-02-triagem-cardiologica-o-que-rastrear-e-em-quem.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Triagem cardiológica", "subtitulo": "O que rastrear, em quem e com qual exame",
        "nota_capa": "Entra pela pergunta que o exame responde.",
        "secoes": {"pergunta": ["A pergunta, a idade e o eletrocardiograma.", "capa"],
                   "corrado": ["O jovem: o debate e a leitura.", "corrado"],
                   "adulto": ["O adulto e a decisão por perfil.", "adulto"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-02.json"), "w"), ensure_ascii=False, indent=1)
print("06-02.json:", len(S), "slides")
