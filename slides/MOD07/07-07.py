"""Spec do deck 7.7. Gera 07-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "palavra", "tipo": "frase", "fundo": "tinta", "eyebrow": "A palavra que carrega o erro",
          "frase": "Tendinite.",
          "apoio": "Se é inflamação, o tratamento parece óbvio: anti-inflamatório, gelo e repouso. Quem tem dor no Aquiles há oito meses já fez os três, e continua com dor."})

S.append({"id": "nome", "tipo": "duas", "eyebrow": "Consenso de terminologia, 2019", "titulo": "O nome muda o tratamento",
          "esq": {"t": "Tendinite", "cor": "verm",
                  "itens": ["sugere inflamação", "empurra para anti-inflamatório", "gelo e repouso"]},
          "dir": {"t": "Tendinopatia", "cor": "petr",
                  "itens": ["dor persistente associada à carga", "aponta para a forma de carregar", "carga bem administrada"]},
          "destaque": "Não é preciosismo de vocabulário: o nome antigo empurra para o tratamento errado.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2020"})

p = [svg_abre(1664, 260, "Três estados do tendão em sequência: reativo, desarranjo e degenerativo, com ida e volta entre os dois primeiros")]
for x, c in [(120, OXID), (660, GLIC), (1200, FOSF)]:
    p.append(f'<rect x="{x}" y="70" width="340" height="90" rx="45" fill="{c}" fill-opacity="0.2" stroke="{c}" stroke-width="5"/>')
p.append(f'<path d="M470,100 L640,100" stroke="{MUDO}" stroke-width="5" marker-end="none"/>')
p.append(f'<path d="M628,88 L648,100 L628,112 Z" fill="{MUDO}"/>')
p.append(f'<path d="M650,132 L480,132" stroke="{MUDO}" stroke-width="5"/>')
p.append(f'<path d="M492,120 L472,132 L492,144 Z" fill="{MUDO}"/>')
p.append(f'<path d="M1010,115 L1180,115" stroke="{MUDO}" stroke-width="5"/>')
p.append(f'<path d="M1168,103 L1188,115 L1168,127 Z" fill="{MUDO}"/>')
p.append("</svg>")
rs = [rot(120, 96, "reativo", w=340, tam=30, cor=OXID, peso=700, alinha="center"),
      rot(660, 96, "desarranjo", w=340, tam=30, cor=GLIC, peso=700, alinha="center"),
      rot(1200, 96, "degenerativo", w=340, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(120, 180, "sobrecarga aguda; engrossa, dói, reversível", w=340, tam=22, cor=MUDO, alinha="center"),
      rot(660, 180, "a reação não resolveu; estrutura se desorganiza", w=340, tam=22, cor=MUDO, alinha="center"),
      rot(1200, 180, "áreas que não voltam; às vezes vasos novos", w=340, tam=22, cor=MUDO, alinha="center")]
S.append({"id": "continuo", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro um · achar que é uma coisa só", "titulo": "O contínuo de Cook e Purdam, 2009",
          "destaque": "Os estados iniciais são reversíveis: uma dor de três semanas tem caminho mais curto que a de três anos.",
          "destaque_cor": "tinta", "fonte": "Br J Sports Med 2009"})

S.append({"id": "rosca", "tipo": "frase", "fundo": "tinta", "eyebrow": "A revisão do modelo, 2016",
          "frase": "Trate a rosca, não o buraco.",
          "apoio": "Mesmo o tendão com área degenerada tem muito tecido funcional em volta, e ele pode ganhar capacidade. Essa frase muda a conversa com quem chegou assustado com o laudo."})

S.append({"id": "imagem", "tipo": "duas", "eyebrow": "Erro dois · achar que a dor mede o estrago", "titulo": "Estrutura e dor andam menos juntas do que parece",
          "esq": {"t": "Imagem alterada", "cor": "ambar",
                  "itens": ["comum em quem não sente dor", "aumenta o risco de dor futura", "não diz quanto dói hoje"]},
          "dir": {"t": "Dor", "cor": "verm",
                  "itens": ["pode vir com imagem pouco alterada", "acompanha a carga recente", "e quanto essa carga mudou"]},
          "destaque_cor": "tinta", "fonte": "Metanálise de ultrassom, Br J Sports Med 2016"})

S.append({"id": "exames", "tipo": "cards", "por_linha": 3, "eyebrow": "O que isso muda sobre imagem", "titulo": "Três consequências práticas",
          "cards": [{"t": "Não é rotina", "x": "dúvida diagnóstica, ruptura, caso que não evolui", "cor": "petr"},
                    {"t": "Não serve de controle", "x": "a estrutura muda devagar e frustra quem melhora", "cor": "ambar"},
                    {"t": "Melhora se mede na função", "x": "e na dor durante a carga, não em milímetros", "cor": "tinta"}],
          "destaque": "O laudo que assusta faz a pessoa se mover com medo, e o medo é parte do problema.",
          "destaque_cor": "verm"})

p = [svg_abre(1664, 300, "Esquema: a cada ciclo de parar e voltar, a capacidade do tendão desce um degrau, enquanto a demanda do treino continua igual")]
p.append(f'<line x1="60" y1="80" x2="1600" y2="80" stroke="{FOSF}" stroke-width="5" stroke-dasharray="16 10"/>')
p.append(f'<path d="M60,100 L400,100 L400,150 L760,150 L760,200 L1120,200 L1120,250 L1600,250" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(1200, 30, "demanda do treino", w=400, tam=24, cor=FOSF, peso=700, alinha="right"),
      rot(80, 112, "para, melhora", w=320, tam=22, cor=AZUL, peso=700),
      rot(420, 162, "volta, piora, para", w=320, tam=22, cor=AZUL, peso=700),
      rot(780, 212, "volta, piora, para", w=320, tam=22, cor=AZUL, peso=700),
      rot(1200, 262, "capacidade do tendão", w=400, tam=24, cor=AZUL, peso=700, alinha="right")]
S.append({"id": "repouso", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro três · achar que repouso resolve", "titulo": "Repouso alivia, e por isso engana",
          "destaque": "O tendão não precisa de ausência de carga. Precisa da carga certa, na dose certa, pelo tempo certo.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "mudou", "tipo": "cards", "por_linha": 4, "eyebrow": "A pergunta que abre o caso", "titulo": "O que mudou nas semanas antes da dor?",
          "cards": [{"t": "Volume", "x": "mais quilômetros ou mais sessões", "cor": "ambar"},
                    {"t": "Tipo", "x": "ladeira, escada, pliometria", "cor": "ambar"},
                    {"t": "Retomada", "x": "voltou das férias no ritmo de antes", "cor": "verm"},
                    {"t": "Contexto", "x": "superfície nova, duas sessões no dia", "cor": "petr"}],
          "destaque": "A dor apareceu depois de uma mudança. É a mudança que se ajusta, não a existência de carga.",
          "destaque_cor": "tinta"})

S.append({"id": "compressao", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro quatro · mandar alongar", "titulo": "Onde o tendão é comprimido contra o osso",
          "cards": [{"t": "Aquiles na inserção", "x": "contra o calcanhar, com o tornozelo em flexão máxima", "cor": "verm"},
                    {"t": "Isquiotibiais proximais", "x": "contra o ísquio, com o quadril muito fletido", "cor": "verm"},
                    {"t": "Glúteos", "x": "na lateral do quadril, com a perna cruzada para dentro", "cor": "verm"}],
          "destaque": "Tração somada a compressão irrita o tecido. O alongamento sustentado faz isso várias vezes por dia.",
          "destaque_cor": "tinta", "fonte": "Cook e Purdam, Br J Sports Med 2012"})

S.append({"id": "conduta", "tipo": "duas", "eyebrow": "Reconhecer e aliviar", "titulo": "Sem exame, na conversa e no movimento",
          "esq": {"t": "Como reconhecer", "cor": "ambar",
                  "itens": ["piora na flexão profunda", "subir escada, banco baixo", "cruzar as pernas", "dormir de lado, perna de cima caída"]},
          "dir": {"t": "O que fazer", "cor": "petr",
                  "itens": ["reduzir posições de compressão", "ajustar como senta e dorme", "força em amplitude que não comprime", "extremos só depois"]},
          "destaque": "Mobilidade continua importando. Evita-se o alongamento sustentado, em compressão, num tendão irritado.",
          "destaque_cor": "tinta"})

p = [svg_abre(1664, 300, "Esquema: com infiltração, a dor cai rápido e depois volta; com exercício, cai devagar e fica baixa")]
p.append(f'<line x1="80" y1="270" x2="1600" y2="270" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="80" y1="30" x2="80" y2="270" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<path d="M80,50 C160,230 260,240 420,230 C700,200 900,110 1600,120" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(f'<path d="M80,50 C400,120 700,200 1000,230 C1200,245 1400,250 1600,250" fill="none" stroke="{OXID}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(1180, 60, "infiltração: alívio rápido, e volta", w=460, tam=24, cor=FOSF, peso=700),
      rot(1180, 204, "exercício: devagar, e fica", w=460, tam=24, cor=OXID, peso=700),
      rot(80, 276, "meses", w=300, tam=22, cor=MUDO)]
S.append({"id": "infiltracao", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Erro cinco · infiltração como primeira linha", "titulo": "Alivia rápido, cobra depois",
          "destaque": "Se usar, é para permitir fazer o trabalho, não para substituir o trabalho.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · revisão sistemática, Lancet 2010"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Cinco erros", "titulo": "Tendão responde à carga",
          "regras": ["Tendinopatia, contínuo, e a rosca em volta do buraco",
                     "A dor acompanha a carga recente, não o laudo",
                     "Pergunte o que mudou; tire a compressão"],
          "cards": [{"t": "Médico", "x": "Diagnostica e decide medicação ou infiltração."},
                    {"t": "Fisioterapia e preparação", "x": "Dosam o exercício e ajustam o treino."},
                    {"t": "Todos", "x": "Explicam que dor de tendão não é destruição."}],
          "quem": "Próxima aula: como se dosa carga num tendão que dói."})

spec = {"arquivo": "aulas/MOD07/07-07-tendinopatia-o-continuum-e-o-que-a-dor-significa.md",
        "modulo": "Lesões: Mecanismos, Epidemiologia e Prevenção", "tema": "tinta",
        "titulo": "Tendinopatia", "subtitulo": "Cinco erros sobre o contínuo e o significado da dor",
        "nota_capa": "Entra pela palavra errada.",
        "secoes": {"palavra": ["O nome e o contínuo.", "capa"],
                   "imagem": ["Imagem, dor e repouso.", "imagem"],
                   "compressao": ["Compressão e infiltração.", "compressao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "07-07.json"), "w"), ensure_ascii=False, indent=1)
print("07-07.json:", len(S), "slides")
