"""Spec do deck 8.9. Gera 08-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

p = [svg_abre(1664, 220, "Uma sessão em linha do tempo: 15 minutos de aparelho, 10 de gelo e 10 de exercício no fim")]
blocos = [(0, 15, MUDO, 0.55), (15, 25, AZUL, 0.55), (25, 35, OXID, 1)]
X = lambda m: 20 + m / 35 * 1620
for a, b, c, o in blocos:
    p.append(f'<rect x="{X(a):.0f}" y="70" width="{X(b) - X(a) - 8:.0f}" height="90" rx="10" fill="{c}" fill-opacity="{o}"/>')
p.append("</svg>")
rs = [rot(X(0) + 10, 96, "15 min de aparelho", w=X(15) - X(0) - 30, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(X(15) + 10, 96, "10 min de gelo", w=X(25) - X(15) - 30, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(X(25) + 10, 96, "10 min de exercício", w=X(35) - X(25) - 30, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(X(25), 170, "o que mais muda o quadro, se sobrar tempo", w=X(35) - X(25), tam=22, cor=OXID, peso=700, alinha="center")]
S.append({"id": "sessao", "tipo": "diagrama", "h": 220, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A décima sessão de uma jogadora de beach tennis", "titulo": "Uma sessão de cabeça para baixo",
          "destaque": "O que tem mais evidência de mudar o quadro recebe menos tempo. O que tem menos abre a sessão.",
          "destaque_cor": "verm", "fonte": "Perfil típico"})

S.append({"id": "perguntas", "tipo": "cards", "por_linha": 4, "eyebrow": "Para qualquer recurso, de qualquer profissão", "titulo": "Quatro perguntas",
          "cards": [{"t": "O que muda?", "x": "dor por horas, amplitude, força, tecido", "cor": "petr"},
                    {"t": "Quando entra?", "x": "em que fase, para qual objetivo, em quem", "cor": "petr"},
                    {"t": "Quando sai?", "x": "prazo ou critério de saída", "cor": "ambar"},
                    {"t": "Como sei que não funciona?", "x": "qual medida, em quanto tempo", "cor": "verm"}],
          "destaque": "Sem resposta para as quatro, o recurso não está sendo prescrito. Está sendo repetido.",
          "destaque_cor": "tinta"})

S.append({"id": "aparelho", "tipo": "numeros", "eyebrow": "Erro um · o aparelho como tratamento", "titulo": "Eletroterapia no ombro, revisão Cochrane",
          "numeros": [{"n": "47", "x": "ensaios", "cor": "tinta"},
                      {"n": "2.388", "x": "participantes", "cor": "tinta"}],
          "destaque": "Evidência de baixa qualidade: ultrassom, laser de baixa intensidade e campo eletromagnético provavelmente sem benefício somados a outras intervenções. Corrente elétrica: incerteza.",
          "destaque_cor": "ambar", "fonte": "Cochrane 2016 · dor do ombro relacionada ao manguito"})

S.append({"id": "fita", "tipo": "duas", "eyebrow": "Erro dois · a fita como proteção", "titulo": "A bandagem elástica na revisão brasileira",
          "esq": {"t": "O que se examinou", "cor": "tinta",
                  "itens": ["ombro, joelho, lombar, pescoço, fáscia plantar", "contra fita falsa e outras intervenções"]},
          "dir": {"t": "O que se encontrou", "cor": "verm",
                  "itens": ["não foi melhor que a fita falsa", "nem que outras intervenções", "efeitos pequenos, provavelmente sem importância clínica"]},
          "destaque": "Se o atleta gosta e ela não substitui nada, o dano é pequeno. O problema é quando ela entra no lugar do exercício.",
          "destaque_cor": "tinta", "fonte": "J Physiother 2014"})

S.append({"id": "manual", "tipo": "duas", "eyebrow": "A terapia manual, com honestidade", "titulo": "Um efeito real, de curto prazo",
          "esq": {"t": "O que faz", "cor": "petr",
                  "itens": ["modula a dor pelo sistema nervoso", "melhora dor e amplitude por um tempo", "abre uma janela para o movimento"]},
          "dir": {"t": "O que não faz", "cor": "verm",
                  "itens": ["“colocar no lugar” vértebra ou articulação", "mudar a estrutura de um tendão"]},
          "destaque": "Justificar o uso por razões neurofisiológicas, não biomecânicas.",
          "destaque_cor": "tinta", "fonte": "Modelo de 2009, Man Ther"})

S.append({"id": "janela", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O recurso passivo abre uma janela. O exercício é o que passa por ela.",
          "apoio": "Duas horas de alívio valem muito se o exercício acontece nelas. Valem pouco se a pessoa volta na semana seguinte para abrir a mesma janela."})

S.append({"id": "caros", "tipo": "duas", "eyebrow": "Os recursos que custam mais", "titulo": "Nenhum deles dispensa a carga",
          "esq": {"t": "Ondas de choque e agulhamento", "cor": "ambar",
                  "itens": ["estudos em algumas condições", "qualidade de evidência variável", "adjuvante, depois de carga bem feita"]},
          "dir": {"t": "Injeções", "cor": "tinta",
                  "itens": ["decisão médica", "riscos, prazos e indicações próprias", "a aula de analgesia do módulo clínico"]},
          "destaque": "Quando o recurso alivia a dor, é a janela para carregar mais, não a licença para voltar sem ter carregado.",
          "destaque_cor": "tinta"})

S.append({"id": "contexto", "tipo": "cards", "por_linha": 4, "eyebrow": "O ritual também tem efeito", "titulo": "Fatores de contexto: placebo e nocebo",
          "cards": [{"t": "Profissional e paciente", "x": "o que cada um traz: expectativa, crença, jeito", "cor": "petr"},
                    {"t": "A relação", "x": "tempo, atenção, o mesmo profissional", "cor": "petr"},
                    {"t": "O tratamento", "x": "explicação clara, sem palavras que assustam", "cor": "ambar"},
                    {"t": "O ambiente", "x": "privado, pontual, com seguimento", "cor": "ambar"}],
          "destaque": "Usar o contexto para potencializar o que funciona; nunca para vender como tratamento o que só funciona pelo contexto.",
          "destaque_cor": "verm", "fonte": "Man Ther 2016"})

p = [svg_abre(1664, 260, "A pessoa que só melhora na maca: a dor cai na sessão e volta no dia seguinte, sessão após sessão, sem descer de patamar")]
p.append(f'<line x1="40" y1="230" x2="1620" y2="230" stroke="{MUDO}" stroke-width="3"/>')
pts = []
for i in range(8):
    x = 60 + i * 200
    pts += [(x, 70), (x + 40, 170), (x + 120, 90), (x + 200, 70)]
d = "M" + " L".join(f"{x},{y}" for x, y in pts[:-1])
p.append(f'<path d="{d}" fill="none" stroke="{FOSF}" stroke-width="5" stroke-linejoin="round"/>')
for i in range(8):
    p.append(f'<circle cx="{100 + i*200}" cy="170" r="10" fill="{OXID}"/>')
p.append("</svg>")
rs = [rot(40, 20, "dor", w=200, tam=24, cor=FOSF, peso=700),
      rot(60, 188, "alívio na sessão", w=240, tam=20, cor=OXID, peso=700),
      rot(1300, 236, "meses", w=300, tam=22, cor=MUDO, alinha="right")]
S.append({"id": "maca", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O custo do ritual", "titulo": "A pessoa que só melhora na maca",
          "destaque": "Alívio que dura horas, medidas paradas, programa sem avançar, e o tratamento dito como algo que fazem nela.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "reconhecer", "tipo": "lista", "eyebrow": "De forma objetiva", "titulo": "Três sinais de que não está funcionando",
          "itens": [{"t": "A medida combinada não mudou", "x": "em duas ou três semanas; a medida, não a sensação na sessão", "cor": "verm"},
                    {"t": "O alívio não passa do dia seguinte", "x": "sessão após sessão", "cor": "ambar"},
                    {"t": "O programa ativo está parado", "x": "o recurso ocupa o lugar da carga", "cor": "ambar"}],
          "destaque": "Qualquer um dos três: rever o plano, não aumentar as sessões com o mesmo recurso.",
          "destaque_cor": "tinta"})

S.append({"id": "quem", "tipo": "tabela", "eyebrow": "Quem faz o quê", "titulo": "Cada um com uma parte da régua",
          "cab": ["Quem", "O que faz"],
          "larguras": [26, 74],
          "linhas": [["Fisioterapia", "escolhe o recurso e escreve as quatro respostas no plano"],
                     ["Médico", "medicação e injeções; nada de sessões sem objetivo"],
                     ["Preparação física", "mantém o treino que não dói"],
                     ["Atleta", "pergunta: “o que isso muda no meu problema?”"]],
          "destaque_cor": "tinta"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Recursos terapêuticos passivos", "titulo": "Coadjuvante, não protagonista",
          "regras": ["O que muda, quando entra, quando sai, como sei que não funciona",
                     "Recurso passivo abre a janela; o exercício passa por ela",
                     "Medida parada em três semanas: rever o plano"],
          "cards": [{"t": "A sessão desvirada", "x": "Começa pelo exercício com carga que progride."},
                    {"t": "O recurso", "x": "Entra para abrir a janela, se ajudar."},
                    {"t": "O gelo", "x": "Se ela gostar, em casa."}],
          "quem": "Próxima aula: testes de retorno ao esporte, e como não ser enganado por eles."})

spec = {"arquivo": "aulas/MOD08/08-09-recursos-terapeuticos-evidencia-efeito-e-ritual.md",
        "modulo": "Fisioterapia Esportiva e Reabilitação", "tema": "tinta",
        "titulo": "Recursos terapêuticos passivos", "subtitulo": "O que cada um muda, e o que é ritual",
        "nota_capa": "Entra pela décima sessão de uma jogadora de beach tennis.",
        "secoes": {"sessao": ["A sessão de cabeça para baixo e as quatro perguntas.", "capa"],
                   "aparelho": ["Aparelho, fita e terapia manual.", "aparelho"],
                   "caros": ["Recursos caros, contexto e dependência.", "caros"],
                   "reconhecer": ["Reconhecer e o fecho.", "reconhecer"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "08-09.json"), "w"), ensure_ascii=False, indent=1)
print("08-09.json:", len(S), "slides")
