"""Spec do deck 9.9. Gera 09-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "reuniao", "tipo": "frase", "fundo": "tinta", "eyebrow": "Segunda-feira, reunião técnica",
          "frase": "“Razão aguda e crônica, 1,6. Zona de perigo.”",
          "apoio": "Um clube de rúgbi amador comprou um software de monitoramento. O técnico quer tirar o jogador do jogo de sábado; ele diz que está ótimo. Ninguém na sala sabe de onde vem o número."})

S.append({"id": "origem", "tipo": "numeros", "eyebrow": "De onde veio", "titulo": "Começou no críquete",
          "numeros": [{"n": "28", "x": "arremessadores rápidos de elite", "cor": "tinta"},
                      {"n": "43", "x": "temporadas individuais", "cor": "petr"},
                      {"n": "6 anos", "x": "de acompanhamento", "cor": "ambar"}],
          "destaque": "A semana atual comparada com a média das últimas quatro. Picos de carga aguda se associaram a mais lesão nas semanas seguintes.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2014"})

# curva em U esquemática
p = [svg_abre(1664, 380, "Curva em U esquemática do risco de lesão pela razão, com faixa ideal entre 0,8 e 1,3 e zona de risco a partir de 1,5")]
x0, x1, y0 = 120, 1560, 300
def X(r): return x0 + (r - 0.4) / (2.0 - 0.4) * (x1 - x0)
p.append(f'<rect x="{X(0.8):.0f}" y="40" width="{X(1.3) - X(0.8):.0f}" height="{y0 - 40}" fill="{OXID}" opacity="0.18"/>')
p.append(f'<rect x="{X(1.5):.0f}" y="40" width="{X(2.0) - X(1.5):.0f}" height="{y0 - 40}" fill="{FOSF}" opacity="0.18"/>')
pts = []
for i in range(81):
    r = 0.4 + i * 0.02
    risco = 0.35 + 1.6 * (r - 1.05) ** 2 if r < 1.05 else 0.35 + 1.7 * (r - 1.05) ** 2
    pts.append(f"{X(r):.1f},{y0 - min(risco, 1.9) * 110:.1f}")
p.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(X(0.8), y0 + 10, "faixa ideal", w=X(1.3) - X(0.8), tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(X(0.8), y0 + 38, "0,8 a 1,3", w=X(1.3) - X(0.8), tam=22, cor=MUDO, alinha="center"),
      rot(X(1.5), y0 + 10, "zona de risco", w=X(2.0) - X(1.5), tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(X(1.5), y0 + 38, "a partir de 1,5", w=X(2.0) - X(1.5), tam=22, cor=MUDO, alinha="center"),
      rot(x0, y0 + 10, "razão aguda e crônica", w=340, tam=22, cor=MUDO),
      rot(x0 - 110, 40, "risco", w=100, tam=22, cor=MUDO, alinha="right")]
S.append({"id": "promessa", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A promessa", "titulo": "Uma faixa verde e uma zona vermelha",
          "destaque": "Nos dados dos arremessadores, risco duas a quatro vezes maior na zona vermelha. E uma ideia que continua valendo: carga crônica construída aos poucos protege.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Br J Sports Med 2016"})

S.append({"id": "convenceu", "tipo": "cards", "por_linha": 2, "eyebrow": "Por que se espalhou", "titulo": "Quatro motivos compreensíveis",
          "cards": [{"t": "Simples", "x": "uma divisão", "cor": "petr"},
                    {"t": "Colorido", "x": "verde, amarelo, vermelho", "cor": "petr"},
                    {"t": "Cabe em software", "x": "virou gráfico em aplicativo de clube e de relógio", "cor": "ambar"},
                    {"t": "Ideia de fundo sensata", "x": "não dar saltos de carga sobre uma base baixa", "cor": "tinta"}],
          "destaque": "Uma ideia sensata embalada numa conta que não aguenta o peso colocado nela.",
          "destaque_cor": "verm"})

S.append({"id": "causa", "tipo": "duas", "eyebrow": "Erro um", "titulo": "Tratar associação como causa",
          "esq": {"t": "O que os estudos mostram", "cor": "petr",
                  "itens": ["dados observacionais", "picos de carga andam junto com lesão", "em grupos específicos"]},
          "dir": {"t": "O que não mostram", "cor": "verm",
                  "itens": ["que mexer na razão reduz lesão", "nenhum estudo estimou o efeito causal", "base para usar em gestão de carga"]},
          "destaque": "Tirar o jogador pelo vermelho é tratar uma associação de outro esporte como mecanismo.",
          "destaque_cor": "tinta", "fonte": "Int J Sports Physiol Perform 2020"})

# acoplamento: aguda dentro da crônica
p = [svg_abre(1664, 320, "A semana aguda desenhada dentro do bloco das quatro semanas crônicas")]
for i in range(4):
    x = 360 + i * 200
    p.append(f'<rect x="{x}" y="90" width="184" height="120" rx="8" fill="{FOSF if i == 3 else GRADE}"/>')
p.append(f'<rect x="344" y="70" width="816" height="160" rx="14" fill="none" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append("</svg>")
rs = [rot(360 + 3 * 200, 136, "semana atual", w=184, tam=22, cor="#F7F6F2", peso=700, alinha="center"),
      rot(344, 24, "carga crônica: média das quatro semanas", w=816, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(344, 246, "o numerador está dentro do denominador", w=816, tam=24, cor=MUDO, alinha="center"),
      rot(1220, 120, "aguda ÷ crônica", w=380, tam=28, cor=TINTA, peso=700)]
S.append({"id": "acoplamento", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro dois", "titulo": "Ignorar o acoplamento matemático",
          "destaque": "Correlação espúria entre aguda e crônica, produzida pela própria conta. Parte do padrão do gráfico vem daí.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2019"})

S.append({"id": "janelas", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro três", "titulo": "Confiar em janelas e cortes que ninguém justificou",
          "cards": [{"t": "7 e 28 dias", "x": "janelas sem fundamento declarado", "cor": "ambar"},
                    {"t": "0,8 · 1,3 · 1,5", "x": "cortes que mudam de estudo para estudo", "cor": "ambar"},
                    {"t": "Médias com peso no tempo", "x": "melhora técnica, mas continua sendo uma razão com cortes", "cor": "petr"}],
          "destaque": "1,49 é verde, 1,51 é vermelho. Cortar um número contínuo em cores joga informação fora.",
          "destaque_cor": "verm", "fonte": "Int J Sports Physiol Perform 2020 · Br J Sports Med 2017"})

S.append({"id": "aleatorio", "tipo": "duas", "eyebrow": "Erro quatro", "titulo": "Acreditar que a carga crônica faz o trabalho",
          "esq": {"t": "Crônica verdadeira", "cor": "tinta",
                  "itens": ["aguda ÷ média real", "associada à lesão"]},
          "dir": {"t": "Crônica sorteada", "cor": "ambar",
                  "itens": ["aguda ÷ valores inventados", "associação parecida com a original"]},
          "destaque": "Se trocar o denominador por qualquer número não muda o resultado, a razão não mede o que prometia.",
          "destaque_cor": "verm", "fonte": "Sports Med 2021"})

S.append({"id": "fragil", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "A ideia por trás estava certa. A conta estava frágil.",
          "apoio": "Construir a carga aos poucos, evitar saltos, cuidar da volta após pausa: tudo continua valendo. O que caiu foi a razão colorida decidindo quem joga."})

S.append({"id": "transplante", "tipo": "duas", "eyebrow": "Erro cinco", "titulo": "Transplantar a elite e deixar o número decidir",
          "esq": {"t": "Dados de origem", "cor": "tinta",
                  "itens": ["atletas profissionais", "monitoramento diário", "rotina estável"]},
          "dir": {"t": "O amador", "cor": "petr",
                  "itens": ["trabalho, sono ruim, semana que quebra", "dados incompletos", "uma medida simples diz mais"]},
          "destaque": "874 corredores iniciantes: aumentos acima de 30% em duas semanas se associaram a alguns tipos de lesão. Também é associação, mas o corredor entende.",
          "destaque_cor": "tinta", "fonte": "J Orthop Sports Phys Ther 2014"})

S.append({"id": "fica", "tipo": "tabela", "eyebrow": "O que fica", "titulo": "Descrever sem colorir, decidir com contexto",
          "cab": ["Semana", "Carga", "Média anterior", "Mudança"],
          "larguras": [22, 22, 30, 26],
          "linhas": [["1", "1.800", "sem base", "sem base"],
                     ["2", "1.900", "1.800", "+6%"],
                     ["3", "2.000", "1.850", "+8%"],
                     ["4", "2.700", "1.900", "+42%"]],
          "destaque": "Vigiar três momentos: salto de volume, acúmulo sem descanso, volta depois de pausa. E perguntar por sono, dor e nota de esforço.",
          "destaque_cor": "tinta", "fonte": "Exemplo ilustrativo, sem dados reais"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Índices de carga aguda e crônica", "titulo": "O vermelho na tela é motivo para três perguntas",
          "regras": ["De onde veio o salto?",
                     "Como ele dorme e o que sente?",
                     "Como foram as semanas anteriores?"],
          "cards": [{"t": "Preparação física", "x": "Descreve a mudança em porcentagem, sem cor."},
                    {"t": "Comissão técnica", "x": "Decide com contexto, não com a zona."},
                    {"t": "Atleta", "x": "Conta sono, dor e o que fez fora do clube."}],
          "quem": "Próxima aula: testes físicos, escolher, aplicar e interpretar."})

spec = {"arquivo": "aulas/MOD09/09-09-indices-de-carga-aguda-e-cronica.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Índices de carga aguda e crônica", "subtitulo": "Uso, limitação e crítica em cinco erros",
        "nota_capa": "Entra por uma reunião de clube de rúgbi com um jogador em vermelho.",
        "secoes": {"reuniao": ["A cena, a origem e a promessa.", "capa"],
                   "causa": ["Os três primeiros erros.", "causa"],
                   "aleatorio": ["O quarto erro e a ideia central.", "aleatorio"],
                   "transplante": ["O quinto erro e o que fica.", "transplante"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-09.json"), "w"), ensure_ascii=False, indent=1)
print("09-09.json:", len(S), "slides")
