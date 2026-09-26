"""Spec do deck 9.12. Gera 09-12.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "raia", "tipo": "frase", "fundo": "tinta", "eyebrow": "Treino na água às 5h30",
          "frase": "Cinco horas de sono nas noites de treino.",
          "apoio": "Um perfil típico do clube de remo: deita às 23h30, acorda às 4h45. A queixa: “não estou recuperando, e o meu tempo no ergômetro piorou”. O primeiro impulso é mexer no treino."})

S.append({"id": "dose", "tipo": "numeros", "eyebrow": "O primeiro número: quanto", "titulo": "A dose de sono",
          "numeros": [{"n": "7 a 9 h", "x": "recomendação para adultos, painel de 2015", "cor": "petr"},
                      {"n": "< 7 h", "x": "sono habitual curto, frequente em atletas", "cor": "verm"},
                      {"n": "5 h", "x": "o remador, três noites por semana", "cor": "ambar"}],
          "destaque": "O consenso de 2021 não deu um número único: rastrear, educar e individualizar.",
          "destaque_cor": "tinta", "fonte": "Sleep Health 2015 · Br J Sports Med 2021"})

# hipnograma esquemático
p = [svg_abre(1664, 330, "Esquema de uma noite em ciclos: sono profundo concentrado no início, REM concentrado no fim, com a última parte cortada")]
x0, x1 = 120, 1560
ciclos = 5
w = (x1 - x0) / ciclos
for i in range(ciclos):
    x = x0 + i * w
    prof = max(0.15, 1 - i * 0.28)
    rem = 0.2 + i * 0.18
    p.append(f'<rect x="{x + 6:.0f}" y="{250 - prof * 150:.0f}" width="{w * 0.55:.0f}" height="{prof * 150:.0f}" rx="6" fill="{OXID}"/>')
    p.append(f'<rect x="{x + 6 + w * 0.58:.0f}" y="{250 - rem * 150:.0f}" width="{w * 0.36:.0f}" height="{rem * 150:.0f}" rx="6" fill="{GLIC}"/>')
cut = x0 + 3.55 * w
p.append(f'<rect x="{cut:.0f}" y="40" width="{x1 - cut:.0f}" height="215" fill="{FOSF}" opacity="0.14"/>')
p.append(f'<line x1="{cut:.0f}" y1="40" x2="{cut:.0f}" y2="255" stroke="{FOSF}" stroke-width="4" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{x0}" y1="252" x2="{x1}" y2="252" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(x0, 262, "início da noite", w=300, tam=22, cor=MUDO),
      rot(x1 - 300, 262, "fim da noite", w=300, tam=22, cor=MUDO, alinha="right"),
      rot(cut + 16, 48, "acordar às 4h45 corta esta parte", w=460, tam=22, cor=FOSF, peso=700),
      rot(x0, 0, "verde: sono profundo · âmbar: sono REM", w=700, tam=22, cor=MUDO)]
S.append({"id": "horario", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Horas, e a que horas", "titulo": "Cortar o fim da noite corta o REM",
          "destaque": "Ciclos de cerca de 90 minutos. Quem corta o fim perde a parte rica em REM; quem deita muito tarde perde a parte rica em sono profundo.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · sono profundo e GH: módulo de endocrinologia"})

S.append({"id": "sustenta", "tipo": "cards", "por_linha": 3, "eyebrow": "O que o sono muda", "titulo": "Três frentes que o curso já mostrou",
          "cards": [{"t": "Músculo e hormônios", "x": "testosterona e hormônio do crescimento: módulo de endocrinologia", "cor": "petr"},
                    {"t": "O gesto", "x": "o aprendizado motor se consolida durante o sono", "cor": "ambar"},
                    {"t": "A defesa", "x": "sono e imunidade conversam nos dois sentidos; carga e infecção: medicina esportiva clínica", "cor": "tinta"}],
          "destaque": "Esta aula acrescenta os números de desempenho e de lesão.", "destaque_cor": "tinta"})

S.append({"id": "extensao", "tipo": "numeros", "eyebrow": "O segundo número: estender o sono", "titulo": "Cerca de 111 minutos a mais por noite",
          "numeros": [{"n": "−0,7 s", "x": "sprint padronizado: de 16,2 para 15,5 segundos", "cor": "petr"},
                      {"n": "+9%", "x": "acerto nos lances livres", "cor": "petr"},
                      {"n": "+9,2%", "x": "acerto nos arremessos de três", "cor": "petr"}],
          "destaque": "Onze jogadores de basquete universitário, sem grupo controle: parte do efeito pode ser expectativa. A direção é coerente, e a intervenção não tem custo nem efeito adverso.",
          "destaque_cor": "ambar", "fonte": "Sleep 2011"})

S.append({"id": "lesao", "tipo": "numeros", "eyebrow": "O terceiro número: lesão", "titulo": "Menos de oito horas, em adolescentes",
          "numeros": [{"n": "1,7 vez", "x": "mais chance de ter tido lesão", "cor": "verm"},
                      {"n": "1,0 a 3,0", "x": "intervalo de confiança de 95%", "cor": "ambar"},
                      {"n": "112", "x": "atletas, cerca de 21 meses de registro", "cor": "tinta"}],
          "destaque": "Observacional: quem dorme pouco também treina e estuda mais. Associação não é causa, como na aula de índices de carga.",
          "destaque_cor": "tinta", "fonte": "J Pediatr Orthop 2014"})

S.append({"id": "cai", "tipo": "duas", "eyebrow": "O que cai primeiro", "titulo": "Depois de uma noite curta",
          "esq": {"t": "Pode se manter", "cor": "petr",
                  "itens": ["alguns esforços máximos", "gestos motores amplos"]},
          "dir": {"t": "Tende a cair", "cor": "verm",
                  "itens": ["desempenho específico do esporte", "decisão e respostas cognitivas", "o mesmo esforço parece mais pesado"]},
          "destaque": "O remador: ergômetro pior e nota de esforço mais alta, sem a carga ter mudado. O mesmo trabalho custando mais.",
          "destaque_cor": "tinta", "fonte": "Revisão, Sports Med 2015"})

S.append({"id": "imita", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Sono curto imita excesso de treino.",
          "apoio": "Recuperação pior, desempenho pior, esforço maior, humor pior, mais infecção. Reduzir a carga de quem dorme cinco horas ajuda um pouco, e não resolve."})

S.append({"id": "noite", "tipo": "numeros", "eyebrow": "Como se dosa: o treino decide o sono", "titulo": "Treinar à noite é uma opção",
          "numeros": [{"n": "23", "x": "estudos na metanálise: treino à noite não piorou o sono", "cor": "petr"},
                      {"n": "1 hora", "x": "a exceção: intenso terminando menos de 1 h antes de deitar", "cor": "ambar"},
                      {"n": "21h30", "x": "deitar para chegar perto de 7 h com treino às 5h30", "cor": "tinta"}],
          "destaque": "Para o remador: trocar um treino da raia por ergômetro no começo da noite. O folclore não pode tirar do amador a única janela que ele tem.",
          "destaque_cor": "tinta", "fonte": "Sports Med 2019 · o horário das 21h30 é uma conta, não recomendação de estudo"})

S.append({"id": "reconhecer", "tipo": "tabela", "eyebrow": "Como se mede e quando não é de treino", "titulo": "Seis perguntas, duas semanas de diário",
          "cab": ["Sinal", "O que fazer", "Com quem"],
          "larguras": [32, 42, 26],
          "linhas": [["Sono curto por agenda", "horário, treino e janela na cama", "preparação física"],
                     ["Insônia instalada", "terapia cognitivo-comportamental primeiro", "médico, psicologia"],
                     ["Ronco com pausas", "suspeita de apneia", "médico"],
                     ["Cafeína tardia, álcool", "cafeína: módulo de suplementos; álcool fragmenta o fim da noite", "equipe"]],
          "destaque": "Lista de higiene do sono não é tratamento de insônia. Relógio serve como tendência.",
          "destaque_cor": "tinta", "fonte": "Ann Intern Med 2016"})

S.append({"id": "plano", "tipo": "cards", "por_linha": 2, "eyebrow": "O plano, sem prometer desfecho", "titulo": "Para esse perfil de remador",
          "cards": [{"t": "7h30 na cama", "x": "nas noites antes do treino na água", "cor": "petr"},
                    {"t": "Um treino à noite", "x": "ergômetro, terminando 1 hora antes de deitar", "cor": "petr"},
                    {"t": "Duas semanas de diário", "x": "antes de mexer na planilha de treino", "cor": "ambar"},
                    {"t": "O mesmo teste", "x": "ergômetro na mesma condição, para ver a linha", "cor": "tinta"}],
          "destaque": "Sono que não melhora com agenda, ronco com pausas ou insônia: sai da preparação física e vai para quem trata.",
          "destaque_cor": "verm"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "O sono decide quanto do treino vira adaptação",
          "regras": ["Decisão: a preparação dosa e testa; o médico separa treino de doença; fisioterapia, nutrição e psicologia no seu campo",
                     "Contribuição: o calendário real, a nota honesta, o plantão e a noite mal dormida",
                     "Reconhecimento: a mesma sessão custando mais, o número decidindo sozinho, as cinco horas por trás do cansaço"],
          "cards": [{"t": "Preparação física", "x": "Princípios, periodização, força, zonas, carga, testes, volta ao grupo."},
                    {"t": "Médico, fisioterapia, nutrição, psicologia", "x": "Doença, tecido, energia, insônia e carga psicológica."},
                    {"t": "Todos", "x": "O salto, o acúmulo, a volta após pausa, o ronco com pausas."}],
          "quem": "Próximo módulo: psicologia do esporte e saúde mental."})

spec = {"arquivo": "aulas/MOD09/09-12-sono-e-recuperacao-como-variaveis-de-treino.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Sono e recuperação", "subtitulo": "O sono como variável de treino, em números",
        "nota_capa": "Entra por um clube de remo com treino às 5h30. Fecha o módulo.",
        "secoes": {"raia": ["A cena, a dose e o horário.", "capa"],
                   "sustenta": ["O que o sono muda, em números.", "sustenta"],
                   "imita": ["A ideia central, a dose e a medida.", "imita"],
                   "plano": ["O plano e o fecho do módulo.", "plano"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-12.json"), "w"), ensure_ascii=False, indent=1)
print("09-12.json:", len(S), "slides")
