"""Spec do deck 4.9. Gera 04-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o risco e as três decisões
p = [svg_abre(1664, 260, "Três decisões em sequência: medir, com o quê, para chegar aonde; antes delas, a pergunta: o que a pessoa quer saber"),
     "<defs>" + seta_marker("d1", MUDO) + "</defs>"]
rs = [rot(0, 0, "antes: o que a pessoa quer saber?", w=1664, tam=30, cor=GLIC, peso=700, alinha="center")]
for i, t in enumerate(["medir?", "com o quê?", "para chegar aonde?"]):
    x = i * 580
    p.append(caixa(x, 80, 500, 150, OXID, OXID_T, esp=3))
    rs.append(rot(x, 100, f"decisão {i+1}", w=500, tam=28, cor=OXID, peso=700, alinha="center"))
    rs.append(rot(x, 150, t, w=500, tam=38, cor=TINTA, peso=700, alinha="center"))
    if i < 2:
        p.append(f'<line x1="{x+506}" y1="155" x2="{x+572}" y2="155" stroke="{MUDO}" stroke-width="4" marker-end="url(#d1)"/>')
p.append("</svg>")
S.append({"id": "decisoes", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A única medida do módulo que pode machucar", "titulo": "O número muda comportamento antes de mudar conduta",
          "destaque": "Quem pede a bioimpedância quase sempre pergunta outra coisa: estou perdendo músculo? Está funcionando? Eu estou bem? Força, desempenho e uma conversa respondem melhor.",
          "destaque_cor": "verm"})

# 2. decisão um
S.append({"id": "medir", "tipo": "duas", "eyebrow": "Decisão um", "titulo": "Só meça se houver uma decisão dependendo do número",
          "esq": {"t": "Medir tem indicação", "cor": "petr",
                  "itens": ["categoria de peso", "restrição com risco de perder massa magra", "recomposição em treino de força", "doença: sarcopenia, obesidade em tratamento"]},
          "dir": {"t": "Não medir de rotina", "cor": "verm",
                  "itens": ["transtorno alimentar, atual ou passado", "relação alterada com corpo e comida", "adolescente", "baixa disponibilidade energética"]},
          "destaque": "Resultado alto e resultado baixo levam à mesma conduta? Não meça. As colunas se cruzam? A da direita vence.",
          "destaque_cor": "tinta"})

# 3. métodos
S.append({"id": "metodos", "tipo": "tabela", "eyebrow": "Decisão dois · Ackland, 2012 · Nana, 2015", "titulo": "Todo método tem erro. Qual você aceita?",
          "cab": ["Método", "O que domina o erro", "Para que serve"],
          "larguras": [24, 36, 40],
          "linhas": [["Bioimpedância", "a água do corpo", "só com padronização rigorosa"],
                     ["Dobras cutâneas", "quem mede", "acompanhar a mesma pessoa, avaliador treinado"],
                     ["DXA", "protocolo e aparelho", "massa magra por região"],
                     ["Cintura", "quase nada, se padronizada", "risco cardiometabólico"],
                     ["Índice de massa corporal", "não separa músculo de gordura", "população, não indivíduo"]],
          "destaque": "A massa livre de gordura da conta de disponibilidade energética vem de um destes métodos, e carrega o erro dele.",
          "destaque_cor": "petr", "fonte": "Sports Medicine 2012 · International Journal of Sport Nutrition and Exercise Metabolism 2015"})

# 4. percentual como razão
p = [svg_abre(1664, 340, "Três colunas empilhadas de massa magra e gordura: partida, 70 kg e 20%; cenário um, mais 2 kg de massa magra, 72 kg e 19,4%; cenário dois, menos 1 kg de gordura e menos 4 kg de massa magra, 65 kg e 20%")]
esc = 3.0
base = 300
rs = []
cen = [("partida", 56, 14, "20%", TINTA), ("+2 kg magra", 58, 14, "19,4%", OXID), ("−4 magra, −1 gordura", 52, 13, "20,0%", FOSF)]
for i, (t, mm, g, pc, c) in enumerate(cen):
    x = 180 + i * 520
    hm, hg = mm * esc * 1.0, g * esc * 1.0
    p.append(f'<rect x="{x}" y="{base-hm:.0f}" width="220" height="{hm:.0f}" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>')
    p.append(f'<rect x="{x}" y="{base-hm-hg-4:.0f}" width="220" height="{hg:.0f}" fill="{GLIC_T}" stroke="{GLIC}" stroke-width="3"/>')
    rs.append(rot(x - 60, base - hm - hg - 64, pc, w=340, tam=40, cor=c, peso=700, alinha="center"))
    rs.append(rot(x - 60, base - hm / 2 - 16, f"{mm} kg", w=340, tam=26, cor=AZUL, peso=600, alinha="center"))
    rs.append(rot(x + 230, base - hm - hg / 2 - 18, f"{g}", w=120, tam=26, cor=GLIC, peso=600))
    rs.append(rot(x - 100, base + 8, t, w=420, tam=26, cor=TINTA, peso=700, alinha="center"))
p.append("</svg>")
rs += [rot(1480, 40, "gordura", w=184, tam=24, cor=GLIC, peso=700, alinha="right"),
       rot(1480, 76, "massa magra", w=184, tam=24, cor=AZUL, peso=700, alinha="right")]
S.append({"id": "razao", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que acompanhar", "titulo": "O percentual é uma razão",
          "destaque": "Somatório de dobras em milímetros; DXA em quilos. O medido engana menos que o calculado: 68 mm é dado, 18,2% é equação.",
          "destaque_cor": "petr", "fonte": "Conta ilustrativa"})

# 5. padronização
S.append({"id": "padrao", "tipo": "duas", "eyebrow": "Se for medir, medir direito", "titulo": "Uma série, não números soltos",
          "esq": {"t": "Padronizar e anotar", "cor": "petr",
                  "itens": ["mesmo horário, de manhã; mesmo jejum", "hidratação habitual; nada depois de treino ou sauna",
                            "sem treino intenso no dia anterior", "mesma fase do ciclo; mesmo avaliador e aparelho"]},
          "dir": {"t": "Ler a mudança", "cor": "ambar",
                  "itens": ["não mais que a cada doze semanas", "diferença real: maior que o erro do método",
                            "um ponto a menos num método que erra vários: variação"]},
          "destaque": "Medir todo mês produz custo, ilusão de precisão e ansiedade. Nenhuma das três é conduta.",
          "destaque_cor": "tinta"})

# 6. a meta errada
xs = [i / 10 for i in range(0, 101)]
svg, rs = linhas(1664, 300, "Curva em U de desempenho e saúde em função da gordura corporal: faixa larga no meio, as duas pontas com prejuízo; a meta errada mora na ponta da esquerda",
                 [{"nome": "", "cor": OXID, "pts": [(x, 90 - 70 * ((x - 5) / 5) ** 2) for x in xs]}],
                 0, 10, 0, 100, [(0.5, "gordura de menos"), (5, "faixa larga"), (9.5, "gordura demais")], [], margem=(40, 20, 60, 30),
                 extra=lambda fx, fy: f'<rect x="{fx(0):.0f}" y="{fy(100):.0f}" width="{fx(2)-fx(0):.0f}" height="{fy(0)-fy(100):.0f}" fill="{FOSF_T}"/>')
rs += [rot(70, 30, "a meta errada mora aqui", w=420, tam=28, cor=FOSF, peso=700)]
S.append({"id": "meta", "tipo": "diagrama", "h": 300, "svg": svg, "rotulos": rs,
          "eyebrow": "Decisão três", "titulo": "A meta errada quase sempre olha para baixo",
          "destaque": "Três portas: a foto (números de poucos dias), a crença (menos gordura, sempre mais desempenho) e o método (meta construída sobre ruído).",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

# 7. Garthe
S.append({"id": "ritmo", "tipo": "numeros", "eyebrow": "Garthe e colaboradores, 2011", "titulo": "Mais devagar preservou o que importava",
          "numeros": [{"n": "+2,1%", "x": "massa magra a 0,7% do peso por semana", "cor": "petr"},
                      {"n": "≈ 0", "x": "massa magra a 1,4% por semana", "cor": "verm"},
                      {"n": "≈ 500 g", "x": "por semana, a 0,7%, em 70 kg", "cor": "tinta"}],
          "destaque": "Meta numérica pede faixa, prazo, ritmo e freios: desempenho que cai, ciclo que some, fratura por estresse, humor e sono piores, comida ocupando o dia.",
          "destaque_cor": "ambar", "fonte": "24 atletas de elite, 4 sessões de força por semana · International Journal of Sport Nutrition and Exercise Metabolism 2011"})

# 8. devolver o número
S.append({"id": "devolver", "tipo": "cards", "por_linha": 4, "eyebrow": "Como devolver o número", "titulo": "Quatro regras de linguagem",
          "cards": [{"t": "Sem adjetivo", "x": "não é alto, ruim ou ótimo: é número com contexto e margem", "cor": "petr"},
                    {"t": "Sem elogio automático", "x": "a redução pode ter vindo de restrição", "cor": "verm"},
                    {"t": "O erro em voz alta", "x": "“uma diferença pequena pode ser só variação”", "cor": "ambar"},
                    {"t": "Ancorar no que importa", "x": "força, desempenho, sintoma, ciclo", "cor": "tinta"}],
          "destaque": "“Eu tenho o número e posso te mostrar. Mas ele não responde à sua pergunta. O que responde é isto aqui.” E a mesma frase em todas as salas.",
          "destaque_cor": "petr"})

# 9. três perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "Três perfis típicos", "titulo": "A mesma pergunta, três respostas",
          "cab": ["Perfil", "Medir?", "Com o quê", "A meta"],
          "larguras": [28, 16, 26, 30],
          "linhas": [["Lutadora: 62 kg, −4 kg em 6 semanas", "sim, após triagem", "dobras ou DXA, em mm e kg", "≈ 1,1%/semana: rever o prazo"],
                     ["Em medicação para obesidade, força caindo", "sim", "DXA e teste de função", "gordura, preservando músculo"],
                     ["Rapaz com o papel da academia, restrição e culpa", "não", "", "regularidade e relação com a comida"]],
          "destaque": "Desidratar para a pesagem não é composição corporal: é água, com risco real. Ninguém da equipe ensina.",
          "destaque_cor": "verm"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "A regra para todos", "titulo": "Medir quando houver decisão",
          "regras": ["Só meça quando o resultado mudar a conduta",
                     "Acompanhe o medido, com protocolo, a cada doze semanas no máximo",
                     "Devolva sem adjetivo, e desconfie da meta que só olha para baixo"],
          "cards": [{"t": "Nutricionista", "x": "Meta e plano alimentar."},
                    {"t": "Educador físico", "x": "A carga que decide o que se perde."},
                    {"t": "Médico", "x": "Medicação, sarcopenia, critério de interrupção."}],
          "quem": "Quando o número dispara restrição, o psicólogo entra junto com o médico."})

spec = {"arquivo": "aulas/MOD04/04-09-composicao-corporal-metodos-metas-e-risco.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Composição corporal no praticante de exercício", "subtitulo": "Indicação, métodos e definição de metas",
        "nota_capa": "Entra pelo risco e pelas três decisões.",
        "secoes": {"decisoes": ["O risco e a decisão de medir.", "capa"],
                   "metodos": ["Com o quê, e o que acompanhar.", "metodos"],
                   "meta": ["A meta, a linguagem e os três perfis.", "meta"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-09.json"), "w"), ensure_ascii=False, indent=1)
print("04-09.json:", len(S), "slides")
