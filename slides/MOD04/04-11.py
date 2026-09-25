"""Spec do deck 4.11. Gera 04-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def piramide(desc, marcas=None):
    """Pirâmide de quatro andares, base embaixo. marcas: {andar: texto à direita}."""
    p = [svg_abre(1664, 380, desc)]
    rs = []
    andares = [("total do dia", OXID, OXID_T), ("distribuição", OXID, OXID_T), ("perto do treino", GLIC, GLIC_T), ("minutos", MUDO, CLARO)]
    for i, (t, c, f) in enumerate(andares):
        w = 1000 - i * 220
        x = (1000 - w) / 2
        y = 290 - i * 90
        p.append(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="80" rx="6" fill="{f}" stroke="{c}" stroke-width="3"/>')
        rs.append(rot(x, y + 20, t, w=w, tam=30, cor=TINTA, peso=700, alinha="center"))
        if marcas and i in marcas:
            rs.append(rot(1060, y + 20, marcas[i], w=604, tam=26, cor=c if c != MUDO else TINTA, peso=600))
    p.append("</svg>")
    return "".join(p), rs

# 1. a pergunta
S.append({"id": "pergunta", "tipo": "frase", "fundo": "tinta", "eyebrow": "A restrição real",
          "frase": "Quando a agenda não deixa fazer tudo, o que priorizar?",
          "apoio": "Na literatura, horário, viagem e recuperação são variáveis de otimização. No consultório, são a restrição principal: o paciente treina no único horário que sobra."})

# 2. a pirâmide
svg, rs = piramide("Pirâmide de quatro andares: total do dia na base, distribuição, perto do treino, minutos no topo",
                   {0: "a maior parte do resultado", 1: "sem buracos longos", 2: "a refeição antes e a depois", 3: "existe, é o menor, e é o mais falado"})
S.append({"id": "piramide", "tipo": "diagrama", "h": 380, "svg": svg, "rotulos": rs,
          "eyebrow": "A resposta", "titulo": "Quatro andares, de baixo para cima",
          "destaque": "Agenda difícil: energia na base e no segundo andar. O topo pode ficar imperfeito. Imperfeito e feito é melhor do que perfeito e impossível.",
          "destaque_cor": "petr"})

# 3. decisão um
S.append({"id": "posjogo", "tipo": "duas", "eyebrow": "Decisão um · o pós-jogo", "titulo": "Quando é o próximo esforço?",
          "esq": {"t": "Em menos de oito horas", "cor": "ambar",
                  "itens": ["dois jogos no dia, torneio, etapas", "a reposição rápida importa", "carboidrato logo, com alguma proteína"]},
          "dir": {"t": "Amanhã ou depois", "cor": "petr",
                  "itens": ["as próximas 24 horas resolvem", "o jantar e o café seguinte decidem", "o shake não é errado; só não decide"]},
          "destaque": "Carboidrato, líquido e sódio, proteína e sono: arroz, feijão, carne, salada e um copo de leite já são uma refeição de recuperação.",
          "destaque_cor": "tinta"})

# 4. a cerveja
S.append({"id": "alcool", "tipo": "numeros", "eyebrow": "Parr e colaboradores, 2014", "titulo": "A cerveja, com a dose na mesa",
          "numeros": [{"n": "1,5 g/kg", "x": "de álcool: cerca de 12 doses, uma noite de bebedeira", "cor": "tinta"},
                      {"n": "−24%", "x": "síntese de proteína muscular, álcool com proteína", "cor": "ambar"},
                      {"n": "−37%", "x": "álcool com carboidrato, sem proteína", "cor": "verm"}],
          "destaque": "O efeito é de dose, e o estudo mostrou o extremo. A conduta não moraliza, ordena: comer antes do copo, água entre as doses, nada na véspera do que importa.",
          "destaque_cor": "petr", "fonte": "Oito homens ativos, treino de força e bicicleta · PLoS One 2014"})

# 5. treino às cinco
S.append({"id": "cinco", "tipo": "duas", "eyebrow": "Decisão dois · Aird, Davies e Carson, 2018", "titulo": "Treino às cinco da manhã",
          "esq": {"t": "Jejum aceitável", "cor": "petr",
                  "itens": ["sessão curta, leve a moderada", "em quem tolera", "nunca em baixa disponibilidade energética"]},
          "dir": {"t": "Mini-refeição antes", "cor": "ambar",
                  "itens": ["sessão longa, intensa ou força pesada", "20 a 40 g de carboidrato, 15 a 30 min antes", "banana, pão com geleia, suco, tapioca fina"]},
          "destaque": "O problema de quem treina às cinco é o depois: sete horas sem proteína até o almoço. A refeição que decide cabe na mochila.",
          "destaque_cor": "verm", "fonte": "46 estudos: comer antes melhorou o aeróbico prolongado, não o curto · Scandinavian Journal of Medicine and Science in Sports 2018"})

# 6. treino às dez da noite: cafeína
h = [i / 4 for i in range(0, 41)]
svg, rs = linhas(1664, 280, "Decaimento da cafeína tomada às 21h30 com meia-vida de cerca de cinco horas: metade às 2h30 e um quarto às 7h30",
                 [{"nome": "", "cor": GLIC, "pts": [(t, 100 * 0.5 ** (t / 5)) for t in h]}],
                 0, 10, 0, 110, [(0, "21h30"), (5, "2h30"), (10, "7h30")], [0, 50, 100], margem=(90, 20, 60, 30),
                 destaques=[{"x": 5}])
rs += [rot(900, 40, "ainda perto da metade no meio da noite", w=700, tam=28, cor=GLIC, peso=700)]
S.append({"id": "noite", "tipo": "diagrama", "h": 280, "svg": svg, "rotulos": rs,
          "eyebrow": "Treino às dez da noite · Snijders e colaboradores, 2015", "titulo": "O jantar é a refeição antes do sono",
          "destaque": "Jantar modesto, com proteína e carboidrato, pouca gordura e fibra. Caseína antes de dormir somou massa e força em 12 semanas, com mais proteína no total. Cafeína à noite: uma sessão melhor, uma noite pior.",
          "destaque_cor": "petr", "fonte": "Esquema calculado com meia-vida de cerca de 5 h, sem valores medidos; a variação entre pessoas é grande · Journal of Nutrition 2015"})

# 7. regra do buraco
p = [svg_abre(1664, 300, "Três dias de treino em horários diferentes, das 5h às 24h, com as refeições marcadas; qualquer intervalo acordado acima de quatro a cinco horas sem comer aparece em vermelho")]
fx = lambda hh: 200 + (hh - 5) / 19 * 1440
rs = []
dias = [("treino 5h", 5, [(4.7, "p"), (7, "r"), (12.5, "r"), (16, "r"), (20, "r")]),
        ("treino 12h30", 12.5, [(7, "r"), (10, "r"), (13.8, "r"), (17, "r"), (20.5, "r")]),
        ("treino 22h", 22, [(7, "r"), (12.5, "r"), (17.5, "r"), (23.2, "r")])]
for i, (t, tr, refs) in enumerate(dias):
    y = 40 + i * 90
    rs.append(rot(0, y - 4, t, w=190, tam=26, cor=TINTA, peso=700))
    p.append(f'<line x1="{fx(5):.0f}" y1="{y+14}" x2="{fx(24):.0f}" y2="{y+14}" stroke="{GRADE}" stroke-width="3"/>')
    p.append(f'<rect x="{fx(tr):.0f}" y="{y}" width="{fx(tr+1)-fx(tr):.0f}" height="28" rx="4" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="2"/>')
    ts = sorted(r[0] for r in refs)
    for a, b in zip(ts, ts[1:]):
        if b - a > 5:
            p.append(f'<line x1="{fx(a):.0f}" y1="{y+14}" x2="{fx(b):.0f}" y2="{y+14}" stroke="{FOSF}" stroke-width="6"/>')
    for r, _ in refs:
        p.append(f'<circle cx="{fx(r):.0f}" cy="{y+14}" r="11" fill="{OXID}"/>')
for hh in [5, 9, 13, 17, 21, 24]:
    rs.append(rot(fx(hh) - 50, 262, f"{hh}h", w=100, tam=24, cor=MUDO, alinha="center"))
p.append("</svg>")
S.append({"id": "buraco", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A regra do buraco", "titulo": "Nunca mais de quatro a cinco horas acordado sem comer",
          "destaque": "Treino no almoço: lanche no meio da manhã e almoço logo depois do treino, não às três da tarde. A regra corrige o déficit por desorganização, o mais comum de quem trabalha e treina.",
          "destaque_cor": "ambar", "fonte": "Esquema de dias típicos: bolinha verde, refeição; faixa azul, treino; traço vermelho, intervalo longo"})

# 8. viagem
S.append({"id": "viagem", "tipo": "cards", "por_linha": 3, "eyebrow": "Decisão três · a viagem", "titulo": "Levar o que precisa, não depender do que encontrar",
          "cards": [{"t": "O kit sem geladeira", "x": "banana, pão, pasta de amendoim, bolacha, castanhas, leite em caixinha, bebida com carboidrato", "cor": "petr"},
                    {"t": "Nada de novo na véspera", "x": "o restaurante com arroz, massa e frango é o certo; a comida típica fica para depois", "cor": "ambar"},
                    {"t": "Ferva, cozinhe, descasque, ou deixe", "x": "a diarreia do viajante perde a competição antes de ela começar", "cor": "verm"}],
          "destaque": "O café do hotel segue a regra do dia de prova. E o pós-jogo em viagem é no ônibus: é quando o kit mais importa.",
          "destaque_cor": "tinta"})

# 9. três perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "Três perfis típicos", "titulo": "Uma decisão para cada",
          "cab": ["Perfil", "A decisão", "Andar"],
          "larguras": [30, 48, 22],
          "linhas": [["Jogador de domingo, churrasco sem jantar", "prato antes do copo, água entre as cervejas, jantar leve; nenhum suplemento", "base e distribuição"],
                     ["Treina às 22h, cafeína às 21h30", "sem cafeína à noite, jantar como refeição pré-sono, lanche no fim da tarde", "distribuição e perto do treino"],
                     ["Equipe jovem, 8 horas de ônibus", "kit em horários fixos, jantar combinado, café cedo com o de casa", "logística para existir um total"]],
          "destaque": "Ninguém precisou do topo da pirâmide. E ninguém mudou a agenda: mudou o que acontece em volta dela.",
          "destaque_cor": "petr"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quem faz o quê", "titulo": "Os minutos ficam para quem resolveu o resto",
          "regras": ["Pós-jogo: a pergunta é quando vem o próximo esforço",
                     "Horário quebrado: o dia montado de trás para a frente, sem buracos",
                     "Viagem: levar o que precisa, e nada de novo na véspera"],
          "cards": [{"t": "Nutricionista", "x": "O plano da semana, do pós-jogo e da viagem."},
                    {"t": "Treinador e comissão", "x": "A logística que leva o plano ao ônibus."},
                    {"t": "Médico", "x": "Sono, estimulantes e álcool que preocupa."}],
          "quem": "Se o álcool virou padrão, o psicólogo entra junto."})

spec = {"arquivo": "aulas/MOD04/04-11-nutricao-em-viagem-e-recuperacao-pos-jogo.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Nutrição na rotina real", "subtitulo": "Recuperação pós-esforço, horários irregulares e viagem",
        "nota_capa": "Entra pela restrição real e pela pirâmide.",
        "secoes": {"pergunta": ["A pergunta e a pirâmide.", "capa"],
                   "posjogo": ["O pós-jogo e a cerveja.", "posjogo"],
                   "cinco": ["Horário quebrado, viagem e os três perfis.", "cinco"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-11.json"), "w"), ensure_ascii=False, indent=1)
print("04-11.json:", len(S), "slides")
