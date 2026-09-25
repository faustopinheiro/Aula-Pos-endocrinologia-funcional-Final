"""Spec do deck 7.3. Gera 07-03.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "cena", "tipo": "frase", "fundo": "tinta", "eyebrow": "A pergunta de sempre",
          "frase": "Foi no sprint, então foi o sprint.",
          "apoio": "Ele fez dezenas de sprints naquela partida e centenas na semana anterior. A diferença entre aquele sprint e os outros não está no sprint."})

S.append({"id": "mecanismo", "tipo": "duas", "eyebrow": "Erro um", "titulo": "Confundir mecanismo com causa",
          "esq": {"t": "Mecanismo", "cor": "petr",
                  "itens": ["o que acontecia quando o tecido falhou", "sprint, mudança de direção, contato, aterrissagem", "diz onde e como a carga chega"]},
          "dir": {"t": "Causa", "cor": "verm",
                  "itens": ["por que o tecido não aguentou, naquele dia", "o que aguentava antes", "está nas semanas anteriores"]},
          "destaque": "Quem responde só o mecanismo proíbe o mecanismo, e o atleta volta menos preparado para ele.",
          "destaque_cor": "verm", "fonte": "Revisão sobre mecanismos de lesão, Br J Sports Med 2005"})

p = [svg_abre(1664, 300, "Linha do tempo de seis semanas terminando no dia da lesão, com quatro marcas antes: doença, jogos seguidos, salto de volume e lesão antiga")]
p.append(f'<line x1="40" y1="170" x2="1560" y2="170" stroke="{MUDO}" stroke-width="4"/>')
for i in range(7):
    x = 40 + i * 250
    p.append(f'<line x1="{x}" y1="160" x2="{x}" y2="180" stroke="{MUDO}" stroke-width="3"/>')
for x, c in [(260, GLIC), (620, AZUL), (1000, FOSF)]:
    p.append(f'<circle cx="{x}" cy="170" r="16" fill="{c}"/>')
p.append(f'<circle cx="1560" cy="170" r="26" fill="{FOSF}"/>')
p.append(f'<rect x="0" y="120" width="30" height="100" fill="{TINTA}" rx="6"/>')
p.append("</svg>")
rs = [rot(0, 234, "lesão antiga, tratada até a dor sumir", w=420, tam=22, cor=TINTA, peso=700),
      rot(170, 60, "retorno de doença sem reconstruir carga", w=380, tam=22, cor=GLIC, peso=700),
      rot(520, 234, "jogos seguidos, pouco intervalo", w=380, tam=22, cor=AZUL, peso=700),
      rot(880, 60, "corrida em alta velocidade muito acima do habitual", w=440, tam=22, cor=FOSF, peso=700),
      rot(1380, 234, "o dia do sprint", w=280, tam=24, cor=FOSF, peso=700)]
S.append({"id": "semanas", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que costuma aparecer quando se olha para trás", "titulo": "A lesão conta as últimas semanas",
          "destaque": "Pergunte o que aconteceu nas últimas quatro semanas antes de perguntar o que aconteceu no dia.",
          "destaque_cor": "tinta", "fonte": "Perfil típico, sem valores medidos"})

S.append({"id": "modelo", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro dois · achar que existe um fator", "titulo": "O modelo multifatorial de Meeuwisse, 1994",
          "cards": [{"t": "Fatores internos", "x": "idade, sexo, composição, força, controle motor, histórico: predisposição", "cor": "petr"},
                    {"t": "Fatores externos", "x": "carga, calendário, superfície, equipamento, clima: suscetibilidade", "cor": "ambar"},
                    {"t": "Evento desencadeante", "x": "o mecanismo do erro um", "cor": "verm"}],
          "destaque": "Encurtamento, desequilíbrio, pisada, piso, alongamento: nenhum deles, sozinho, produz lesão.",
          "destaque_cor": "tinta", "fonte": "Clin J Sport Med 1994"})

S.append({"id": "copo", "tipo": "frase", "fundo": "tinta", "eyebrow": "A imagem para explicar ao atleta",
          "frase": "Todo mundo discute a gota. Quase ninguém discute quem encheu o copo.",
          "apoio": "Internos definem o tamanho do copo, externos enchem, o mecanismo é a última gota. Não existe exercício perigoso em si: existe exercício mal dosado para aquele copo, naquele dia."})

cx, cy, r = 832, 150, 110
p = [svg_abre(1664, 300, "Ciclo em que cada exposição leva a adaptação, má adaptação, lesão com recuperação completa ou lesão com recuperação incompleta, e volta ao atleta")]
p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MUDO}" stroke-width="5" stroke-dasharray="18 12"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="{TINTA}"/>')
for (x2, y2, c) in [(460, 60, OXID), (1204, 60, FOSF), (460, 240, GLIC), (1204, 240, AZUL)]:
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="5"/>')
    p.append(f'<circle cx="{x2}" cy="{y2}" r="14" fill="{c}"/>')
p.append("</svg>")
rs = [rot(772, 132, "atleta", w=120, tam=24, cor="#FFFFFF", peso=700, alinha="center"),
      rot(40, 44, "adaptação: o copo aumenta", w=400, tam=24, cor=OXID, peso=700, alinha="right"),
      rot(1224, 44, "má adaptação: o copo diminui", w=420, tam=24, cor=FOSF, peso=700),
      rot(40, 224, "lesão, recuperação completa", w=400, tam=24, cor=GLIC, peso=700, alinha="right"),
      rot(1224, 224, "lesão, recuperação pela metade", w=420, tam=24, cor=AZUL, peso=700)]
S.append({"id": "circulo", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro três · tratar como conta que se faz uma vez", "titulo": "Cada exposição modifica o atleta",
          "destaque": "Risco não é número fixo. Avaliação anual é foto de um filme; medida repetida descreve o filme.",
          "destaque_cor": "tinta", "fonte": "Modelo dinâmico e recursivo, Clin J Sport Med 2007"})

S.append({"id": "padrao", "tipo": "duas", "eyebrow": "Erro quatro · caçar o preditor", "titulo": "De fator de risco a reconhecimento de padrão",
          "esq": {"t": "Fator isolado", "cor": "verm",
                  "itens": ["força de quadril baixa", "sozinha, não prediz lesão", "nenhum teste de rastreio passou (Bahr, 2016)"]},
          "dir": {"t": "Padrão", "cor": "petr",
                  "itens": ["força baixa e joelho para dentro", "calendário congestionado, pouco sono", "lesão no mesmo membro no ano anterior"]},
          "destaque": "Bittencourt e o grupo da UFMG, 2016: a lesão emerge de uma rede de determinantes que interagem.",
          "destaque_cor": "petr", "fonte": "Br J Sports Med 2016 (rastreio; sistemas complexos)"})

p = [svg_abre(1664, 300, "Esquema de volume semanal subindo em degraus suaves, com um degrau muito alto destacado")]
p.append(f'<line x1="40" y1="270" x2="1620" y2="270" stroke="{MUDO}" stroke-width="3"/>')
alt = [60, 72, 84, 96, 108, 190, 120, 132]
for i, a in enumerate(alt):
    c = FOSF if a == 190 else AZUL
    p.append(f'<rect x="{80 + i * 190}" y="{270 - a}" width="140" height="{a}" rx="6" fill="{c}"/>')
p.append("</svg>")
rs = [rot(880, 30, "o salto", w=300, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(80, 30, "progressão em degraus", w=600, tam=24, cor=AZUL, peso=700)]
S.append({"id": "carga", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Carga: o que se sabe", "titulo": "A variável que você mais controla",
          "destaque": "Mudança brusca preocupa mais que valor alto. Vigie salto de volume, acúmulo sem descanso e retomada depois de pausa.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "razao", "tipo": "lista", "eyebrow": "Razão entre carga aguda e crônica", "titulo": "A ideia estava certa, a conta estava frágil",
          "itens": [{"t": "Estatística", "x": "a própria razão distorce a leitura", "cor": "verm"},
                    {"t": "Pontos de corte", "x": "variam de estudo para estudo, sem justificativa", "cor": "ambar"},
                    {"t": "Uso para decidir treino", "x": "sem evidência de que reduza lesão", "cor": "verm"}],
          "gap_itens": 26, "destaque": "Não entregue a decisão a um número em vermelho, nem diga ao atleta que ele está numa zona de perigo.",
          "destaque_cor": "tinta", "fonte": "Crítica metodológica, Int J Sports Physiol Perform 2020"})

S.append({"id": "colunas", "tipo": "tabela", "eyebrow": "A pasta com recibos", "titulo": "Três colunas em vez de duas",
          "cab": ["Coluna", "O que entra", "Para que serve"],
          "larguras": [30, 42, 28],
          "linhas": [["Não modificáveis", "idade, sexo, estrutura, histórico", "calibrar expectativa"],
                     ["Vendidos como modificáveis", "pisada, palmilha de loja, alongamento para prevenir", "sem retorno demonstrado"],
                     ["Modificáveis com retorno", "carga, força, sono, energia, reabilitação completa", "onde investir"]],
          "destaque": "Das coisas que você fez nesses meses, quantas mexeram na terceira coluna?",
          "destaque_cor": "verm", "fonte": "Coorte de pronação e metanálise de prevenção, Br J Sports Med 2014"})

p = [svg_abre(1664, 300, "Esquema: depois de uma lesão, o risco de quem reabilitou por completo volta ao patamar; o de quem parou cedo fica acima")]
p.append(f'<line x1="60" y1="270" x2="1600" y2="270" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="200" x2="400" y2="200" stroke="{MUDO}" stroke-width="5"/>')
p.append(f'<path d="M400,200 L400,50 C600,60 800,190 1100,198 L1600,200" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append(f'<path d="M400,50 C600,55 800,110 1100,118 L1600,120" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(80, 150, "antes da lesão", w=300, tam=22, cor=MUDO),
      rot(1180, 76, "parou quando a dor sumiu", w=440, tam=22, cor=FOSF, peso=700),
      rot(1180, 214, "capacidade devolvida", w=440, tam=22, cor=AZUL, peso=700)]
S.append({"id": "previa", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O fator mais consistente", "titulo": "Lesão prévia é trabalho a fazer, não carimbo",
          "destaque": "O fator não diz “este atleta é frágil”. Diz “voltou com um copo menor, e ninguém devolveu o tamanho”.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · coorte do futebol de elite, Br J Sports Med 2006"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quatro erros", "titulo": "A causa está nas semanas, não no segundo",
          "regras": ["Pergunte pelas últimas quatro semanas, não só pelo dia",
                     "Gaste energia e dinheiro na terceira coluna",
                     "Trate o histórico como trabalho, não como carimbo"],
          "cards": [{"t": "Médico e fisioterapeuta", "x": "Diagnosticam e conduzem o tratamento."},
                    {"t": "Educação física e preparação", "x": "Dosam e progridem a carga; leem o registro."},
                    {"t": "Nutrição e psicologia", "x": "Sono, alimentação e energia disponível."}],
          "quem": "Próxima aula: lesão muscular, o que acontece dentro do músculo quando ele falha."})

spec = {"arquivo": "aulas/MOD07/07-03-modelo-etiologico-por-que-a-lesao-acontece.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Etiologia da lesão esportiva", "subtitulo": "Quatro erros ao explicar por que alguém se machucou",
        "nota_capa": "Entra pela cena do sprint.",
        "secoes": {"cena": ["Mecanismo, causa e as semanas anteriores.", "capa"],
                   "modelo": ["O modelo multifatorial, o copo e o círculo.", "modelo"],
                   "padrao": ["Padrão, carga, razão aguda e crônica.", "padrao"],
                   "colunas": ["As três colunas e a lesão prévia.", "colunas"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-03.json"), "w"), ensure_ascii=False, indent=1)
print("07-03.json:", len(S), "slides")
