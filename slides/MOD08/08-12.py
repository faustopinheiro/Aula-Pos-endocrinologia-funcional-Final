"""Spec do deck 8.12. Gera 08-12.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "quadra", "tipo": "frase", "fundo": "tinta", "eyebrow": "Na consulta de liberação",
          "frase": "“Qual a chance de romper de novo?”",
          "apoio": "Uma jogadora de basquete adolescente, depois da reconstrução do cruzado, e a pergunta da mãe. “Fica tranquila”, “o risco é bem maior” e “seis vezes mais” são as três respostas ruins."})

S.append({"id": "dois", "tipo": "numeros", "eyebrow": "O mesmo estudo, dois números", "titulo": "Um diz quanto a mais; o outro, quanto",
          "numeros": [{"n": "quase 6×", "x": "a taxa de nova lesão do cruzado, comparada com quem nunca rompeu", "cor": "ambar"},
                      {"n": "~30 em 100", "x": "atletas operados com nova lesão do cruzado em dois anos", "cor": "tinta"}],
          "destaque": "Risco relativo não diz de onde se parte. Risco absoluto é o que a mãe perguntou.",
          "destaque_cor": "tinta", "fonte": "Coorte de Cincinnati, 78 atletas jovens · Am J Sports Med 2014"})

S.append({"id": "formatos", "tipo": "tabela", "eyebrow": "Três formas de dizer", "titulo": "Sempre o grupo de referência e o tempo",
          "cab": ["Formato", "Como soa", "O que provoca"],
          "larguras": [22, 44, 34],
          "linhas": [["Risco relativo", "“seis vezes mais”", "infla a percepção; não diz de quanto se parte"],
                     ["Porcentagem", "“trinta por cento”", "melhor, mas de quem e em quanto tempo?"],
                     ["Frequência natural", "“de cada cem jovens como você, cerca de trinta em dois anos”", "responde às duas perguntas numa frase"]],
          "destaque": "Cem pessoas como quem? Em quanto tempo?",
          "destaque_cor": "tinta", "fonte": "BMJ 2003"})

# quadro de 100 ícones, 23 destacados
p = [svg_abre(1664, 400, "Quadro de cem ícones de pessoas, vinte e três destacados")]
x0, y0, dx, dy = 140, 10, 40, 38
for i in range(100):
    r, c = divmod(i, 10)
    cx, cy = x0 + c * dx, y0 + r * dy
    cor = FOSF if i < 23 else GRADE
    p.append(f'<circle cx="{cx}" cy="{cy + 8}" r="7" fill="{cor}"/>')
    p.append(f'<rect x="{cx - 10}" y="{cy + 17}" width="20" height="17" rx="7" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(640, 50, "23", w=200, tam=96, cor=FOSF, peso=700),
      rot(840, 85, "com nova lesão do cruzado", w=600, tam=30, cor=TINTA),
      rot(640, 190, "77", w=200, tam=96, cor=MUDO, peso=700),
      rot(840, 225, "sem nova lesão", w=600, tam=30, cor=TINTA),
      rot(640, 350, "de cada 100 atletas com menos de 25 anos que voltaram ao esporte", w=900, tam=22, cor=MUDO)]
S.append({"id": "icones", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número desenhado", "titulo": "Quase um em cada quatro",
          "destaque": "A família vê as duas partes ao mesmo tempo: o risco é real, e a maioria não teve nova lesão.",
          "destaque_cor": "tinta", "fonte": "Metanálise, Am J Sports Med 2016 · 15% no total, 23% nos mais jovens que voltaram"})

S.append({"id": "lado", "tipo": "numeros", "eyebrow": "O risco que ninguém menciona", "titulo": "A maior parte foi no outro joelho",
          "numeros": [{"n": "~20 em 100", "x": "romperam o cruzado do joelho do outro lado", "cor": "verm"},
                      {"n": "~9 em 100", "x": "romperam o enxerto", "cor": "ambar"}],
          "destaque": "“O enxerto aguenta?” é a pergunta pela metade. A prevenção depois da alta é para os dois joelhos.",
          "destaque_cor": "verm", "fonte": "Coorte de Cincinnati · Am J Sports Med 2014"})

S.append({"id": "posterior", "tipo": "numeros", "eyebrow": "E não é só o mesmo ligamento", "titulo": "Lesão prévia do cruzado e posterior da coxa",
          "numeros": [{"n": "2,25", "x": "risco relativo de lesão do posterior da coxa em quem já teve lesão do cruzado", "cor": "ambar"},
                      {"n": "3", "x": "estudos reunidos nessa análise", "cor": "tinta"}],
          "destaque": "Relativo, sem conversão para cada cem. Entra como motivo para a equipe manter força e carga, não como número para a família.",
          "destaque_cor": "tinta", "fonte": "Revisão sistemática, Br J Sports Med 2017"})

S.append({"id": "sobra", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O risco que sobra não é falha do tratamento. É o que o melhor tratamento não tira, e precisa ser dito.",
          "apoio": "Quem ouve o número antes pode decidir. Quem não ouve ouve a lesão depois como traição."})

# duas curvas: adesão cai no retorno, exposição sobe
p = [svg_abre(1664, 380, "Duas curvas: a adesão ao programa cai no dia do retorno enquanto a exposição sobe"), "<defs>", seta_marker("sx", MUDO), "</defs>"]
p.append(f'<line x1="80" y1="330" x2="1560" y2="330" stroke="{MUDO}" stroke-width="3" marker-end="url(#sx)"/>')
p.append(f'<line x1="820" y1="40" x2="820" y2="330" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<path d="M 100 90 C 400 80, 700 85, 800 100 C 880 115, 900 260, 1000 280 C 1150 300, 1350 300, 1540 305" fill="none" stroke="{OXID}" stroke-width="6"/>')
p.append(f'<path d="M 100 300 C 400 300, 650 290, 780 270 C 860 250, 880 110, 980 95 C 1150 80, 1350 80, 1540 80" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(110, 40, "adesão ao programa", w=320, tam=24, cor=OXID, peso=700),
      rot(1180, 40, "exposição ao risco", w=320, tam=24, cor=FOSF, peso=700),
      rot(720, 342, "dia do retorno", w=200, tam=22, cor=TINTA, peso=700, alinha="center"),
      rot(100, 340, "reabilitação", w=300, tam=20, cor=MUDO),
      rot(1260, 340, "temporada", w=300, tam=20, cor=MUDO, alinha="right")]
S.append({"id": "curvas", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Onde o número costuma subir", "titulo": "As duas curvas se cruzam no pior lugar",
          "destaque": "Programa dentro do aquecimento, no mínimo que ela vai fazer, reteste marcado antes da alta, e “até o fim da temporada”.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "publicos", "tipo": "tabela", "eyebrow": "Três públicos", "titulo": "O mesmo risco, três conversas",
          "cab": ["Quem", "Precisa ouvir"],
          "larguras": [22, 78],
          "linhas": [["Atleta", "o número, o que ela faz para baixá-lo e os sinais que a fazem parar"],
                     ["Técnico", "as condições práticas: tempo de jogo, restrições, prazo, quem avisa se mudar"],
                     ["Família", "o número, o que foi decidido e por quê, e fazer parte da decisão"]],
          "destaque": "Nas três: pedir que a pessoa explique de volta com as palavras dela. Se a mãe repete “seis vezes”, a conversa não terminou.",
          "destaque_cor": "tinta", "fonte": "Teach-back, revisão sistemática, PLoS One 2020"})

S.append({"id": "lei", "tipo": "duas", "eyebrow": "Quem pode saber o quê", "titulo": "Dado de saúde é dado sensível",
          "esq": {"t": "O que a lei diz", "cor": "tinta",
                  "itens": ["dado de saúde é dado pessoal sensível", "tratamento com regras próprias", "criança: consentimento específico de pelo menos um dos pais"]},
          "dir": {"t": "O que muda na prática", "cor": "petr",
                  "itens": ["técnico e clube recebem as condições, não o prontuário", "o que for além disso sai com autorização", "o registro, com o número dito, fica com a equipe de saúde"]},
          "destaque": "O sigilo profissional já pedia esse cuidado antes da lei.",
          "destaque_cor": "tinta", "fonte": "LGPD, Lei 13.709/2018 · art. 5º, II; art. 11; art. 14, § 1º"})

S.append({"id": "resposta", "tipo": "lista", "eyebrow": "A resposta para a mãe", "titulo": "Quatro frases e uma pergunta de volta",
          "itens": [{"t": "O número", "x": "de cada cem jovens que voltam a um esporte como o basquete, cerca de vinte a trinta têm nova lesão em dois anos, muitas vezes no outro joelho", "cor": "verm"},
                    {"t": "A outra parte", "x": "setenta a oitenta não têm", "cor": "petr"},
                    {"t": "O que ela fez", "x": "passou nos critérios: mais perto do menor número, não em zero", "cor": "ambar"},
                    {"t": "O que baixa e o que faz parar", "x": "programa nos dois joelhos; parar se inchar ou falsear", "cor": "tinta"}],
          "gap_itens": 10,
          "destaque": "“Pode me dizer, com as suas palavras, o que vai contar em casa?” A resposta vai para o registro.",
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "A reabilitação termina num número dito em voz alta",
          "regras": ["Decisão: cada profissão no seu campo; a atleta pesa o risco; a gestão garante testes e separa quem avalia de quem tem interesse",
                     "Contribuição: o dia seguinte, o calendário honesto, a dor que ninguém viu",
                     "Reconhecimento: os sinais que qualquer um leva adiante"],
          "cards": [{"t": "Médico e fisioterapia", "x": "Liberação, riscos inaceitáveis, fases, carga e testes."},
                    {"t": "Preparação, nutrição e psicologia", "x": "Carga no campo, energia para reparar, medo de voltar."},
                    {"t": "Todos", "x": "O joelho que incha, a fase pelo calendário, o “fica tranquila”."}],
          "quem": "Próximo módulo: preparação física, treinamento e gestão de carga."})

spec = {"arquivo": "aulas/MOD08/08-12-risco-residual-e-comunicacao.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Risco residual no retorno ao esporte", "subtitulo": "Números que o atleta, o técnico e a família entendem",
        "nota_capa": "Entra pela pergunta da mãe de uma jogadora de basquete.",
        "secoes": {"quadra": ["A pergunta e os formatos do número.", "capa"],
                   "icones": ["Os números do cruzado e o que sobra.", "icones"],
                   "curvas": ["Onde o número sobe e como se conversa.", "curvas"],
                   "resposta": ["A resposta montada e o fecho do módulo.", "resposta"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-12.json"), "w"), ensure_ascii=False, indent=1)
print("08-12.json:", len(S), "slides")
