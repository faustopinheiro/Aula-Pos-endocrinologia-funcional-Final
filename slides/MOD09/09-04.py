"""Spec do deck 9.4. Gera 09-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "lance", "tipo": "frase", "fundo": "tinta", "eyebrow": "Antes do gol",
          "frase": "Dois ou três segundos que raramente aparecem no treino da semana.",
          "apoio": "Antes do chute, quase sempre alguém correu, e quase sempre em linha reta. A semana costuma estar cheia de corrida contínua, circuitos e força. Muito pouco de correr o mais rápido possível."})

S.append({"id": "gols", "tipo": "numeros", "eyebrow": "O primeiro número", "titulo": "A ação mais frequente antes do gol",
          "numeros": [{"n": "360", "x": "gols da primeira divisão alemã analisados em vídeo", "cor": "tinta"},
                      {"n": "45%", "x": "com sprint em linha reta do jogador que marcou", "cor": "verm"}],
          "destaque": "Em 83% dos gols, quem marcou ou quem passou fez pelo menos uma ação de potência antes do lance.",
          "destaque_cor": "tinta", "fonte": "J Sports Sci 2012"})

# barras reais das ações do jogador que marcou
acoes = [(45, "sprint em linha reta", FOSF), (16, "salto", GLIC), (6, "rotação", OXID), (6, "sprint com mudança de direção", AZUL)]
p = [svg_abre(1664, 340, "Ações do jogador que marcou: sprint em linha reta 45%, salto 16%, rotação 6%, sprint com mudança de direção 6%")]
for i, (v, t, c) in enumerate(acoes):
    y = 20 + i * 80
    p.append(f'<rect x="520" y="{y}" width="{v * 22}" height="52" rx="4" fill="{c}"/>')
p.append("</svg>")
rs = []
for i, (v, t, c) in enumerate(acoes):
    y = 20 + i * 80
    rs.append(rot(40, y + 12, t, w=460, tam=24, cor=TINTA, alinha="right"))
    rs.append(rot(520 + v * 22 + 16, y + 8, f"{v}%", w=120, tam=30, cor=TINTA, peso=700))
S.append({"id": "acoes", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As ações do jogador que marcou", "titulo": "A linha reta decide mais gols; a mudança de direção enche o jogo",
          "destaque": "O estudo olha gols, não o jogo inteiro. No jogo, mudanças de direção e desacelerações são muito frequentes.",
          "destaque_cor": "tinta", "fonte": "Porcentagem dos 360 gols · J Sports Sci 2012"})

S.append({"id": "tres", "tipo": "cards", "por_linha": 3, "eyebrow": "Três qualidades, não uma", "titulo": "Cada uma se treina e se mede de um jeito",
          "cards": [{"t": "Aceleração", "x": "ganhar velocidade nos primeiros metros; empurrar o chão para trás com força", "cor": "verm"},
                    {"t": "Velocidade máxima", "x": "o pico, depois da aceleração; força rápida num contato curto", "cor": "ambar"},
                    {"t": "Mudança de direção", "x": "frear, mudar e sair; força excêntrica, técnica e decisão", "cor": "petr"}],
          "destaque": "Uma pessoa pode ser boa numa e ruim em outra.",
          "destaque_cor": "tinta"})

S.append({"id": "agilidade", "tipo": "duas", "eyebrow": "Uma definição que muda o treino", "titulo": "Agilidade exige estímulo",
          "esq": {"t": "Mudança de direção pré-planejada", "cor": "tinta",
                  "itens": ["circuito de cones", "o atleta sabe o caminho", "treina a parte física"]},
          "dir": {"t": "Agilidade", "cor": "petr",
                  "itens": ["movimento rápido do corpo inteiro", "mudança de velocidade ou direção", "em resposta a um estímulo: adversário, bola, sinal"]},
          "destaque": "Só cones deixa de fora a percepção e a decisão, a parte que o jogo cobra.",
          "destaque_cor": "tinta", "fonte": "Revisão, J Sports Sci 2006"})

S.append({"id": "descansado", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Velocidade se treina com velocidade. Correr rápido e cansado é treinar outra coisa.",
          "apoio": "O esforço máximo e curto depende de um sistema que precisa de minutos para se recompor. Sprint com ele vazio sai mais lento, e vira resistência à velocidade."})

S.append({"id": "treno", "tipo": "numeros", "eyebrow": "A aceleração", "titulo": "A força aplicada no chão responde ao treino",
          "numeros": [{"n": "80%", "x": "da massa corporal no trenó; 16 sessões de 10 sprints de 20 m", "cor": "tinta"},
                      {"n": "0,80 × 0,20", "x": "tamanho de efeito na força horizontal máxima: trenó contra sem carga", "cor": "verm"}],
          "destaque": "Melhora moderada nos primeiros 5 metros. Estudo pequeno, 16 jogadores amadores: sprint resistido e sem carga são estímulos diferentes.",
          "destaque_cor": "tinta", "fonte": "Int J Sports Physiol Perform 2017"})

# déficit de mudança de direção
p = [svg_abre(1664, 300, "Dois atletas com o mesmo tempo total no teste de mudança de direção e proporções diferentes de velocidade linear e custo da mudança")]
for i, (lin, cus) in enumerate([(1000, 320), (760, 560)]):
    y = 40 + i * 130
    p.append(f'<rect x="300" y="{y}" width="{lin}" height="70" rx="6" fill="{OXID}" fill-opacity="0.8"/>')
    p.append(f'<rect x="{300 + lin}" y="{y}" width="{cus}" height="70" rx="6" fill="{FOSF}" fill-opacity="0.85"/>')
p.append("</svg>")
rs = [rot(20, 60, "Atleta A", w=260, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(20, 190, "Atleta B", w=260, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(300, 62, "velocidade em linha reta", w=1000, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(1300, 62, "custo", w=320, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(300, 192, "velocidade em linha reta", w=760, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(1060, 192, "custo da mudança", w=560, tam=24, cor="#F7F6F2", peso=700, alinha="center"),
      rot(300, 262, "mesmo tempo total no teste", w=1320, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "deficit", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que o teste esconde", "titulo": "Déficit de mudança de direção",
          "destaque": "Tempo com mudança menos tempo do sprint reto na mesma distância: o custo da mudança, separado da velocidade.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · revisão, Strength Cond J 2018"})

S.append({"id": "dose", "tipo": "cards", "por_linha": 2, "eyebrow": "Como dosar", "titulo": "Quatro regras para o sprint ser treino de velocidade",
          "cards": [{"t": "Esforço máximo", "x": "a oitenta por cento é outro treino", "cor": "verm"},
                    {"t": "Recuperação completa", "x": "se o tempo começa a cair, a série acabou", "cor": "ambar"},
                    {"t": "Poucas repetições", "x": "a qualidade some antes do cansaço aparecer", "cor": "petr"},
                    {"t": "Início da sessão", "x": "depois do aquecimento, não no fim de um treino longo", "cor": "tinta"}]})

S.append({"id": "protege", "tipo": "duas", "eyebrow": "Velocidade também protege", "titulo": "Exposição regular à velocidade máxima",
          "esq": {"t": "O achado", "cor": "petr",
                  "itens": ["mais exposição a esforços em velocidade máxima", "menor risco de lesão", "estudo observacional, futebol gaélico"]},
          "dir": {"t": "A lógica", "cor": "ambar",
                  "itens": ["o posterior da coxa que nunca vai à velocidade máxima no treino", "encontra essa velocidade pela primeira vez no jogo", "treinar velocidade prepara o tecido para ela"]},
          "destaque_cor": "tinta", "destaque": "Exposição regular, não ocasional.", "fonte": "J Sci Med Sport 2017"})

S.append({"id": "resumo", "tipo": "tabela", "eyebrow": "O resumo operacional", "titulo": "Treinar e medir cada qualidade",
          "cab": ["Qualidade", "Como treinar", "Como medir"],
          "larguras": [24, 44, 32],
          "linhas": [["Aceleração", "sprints curtos com e sem resistência; força para empurrar o chão", "tempo nos primeiros 10 m"],
                     ["Velocidade máxima", "sprints com aceleração suficiente; recuperação completa", "trecho lançado ou velocidade máxima registrada"],
                     ["Mudança de direção e agilidade", "desaceleração, técnica e exercícios com estímulo", "déficit de mudança de direção; teste com estímulo"]]})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Velocidade, aceleração e mudança de direção", "titulo": "Velocidade se treina com velocidade, descansado",
          "regras": ["Três qualidades: aceleração, velocidade máxima, mudança de direção",
                     "Agilidade exige estímulo",
                     "Separar o custo da mudança da velocidade em linha reta"],
          "cards": [{"t": "Preparação física", "x": "Põe o sprint no começo e na semana."},
                    {"t": "Técnico", "x": "Cria os exercícios com estímulo e decisão."},
                    {"t": "Fisioterapia", "x": "Prepara o tecido para a velocidade máxima."}],
          "quem": "Próxima aula: treino aeróbio contínuo e intervalado."})

spec = {"arquivo": "aulas/MOD09/09-04-velocidade-aceleracao-e-mudanca-de-direcao.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Velocidade, aceleração e mudança de direção", "subtitulo": "O que os números dizem sobre treinar o que decide o jogo",
        "nota_capa": "Entra pelo sprint em linha reta antes do gol.",
        "secoes": {"lance": ["O lance e os números dos gols.", "capa"],
                   "tres": ["Três qualidades e a agilidade.", "tres"],
                   "treno": ["Aceleração e o teste de mudança de direção.", "treno"],
                   "dose": ["Dose, proteção e resumo.", "dose"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-04.json"), "w"), ensure_ascii=False, indent=1)
print("09-04.json:", len(S), "slides")
