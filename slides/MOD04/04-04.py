"""Spec do deck 4.4. Gera 04-04.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a decisão
S.append({"id": "decisao", "tipo": "frase", "fundo": "tinta", "eyebrow": "Periodizar ou não, e em que nível",
          "frase": "A ferramenta certa, no paciente errado, na ordem errada.",
          "apoio": "A periodização nutricional é legítima e nasceu no esporte de elite. A pergunta é quanto dela sobrevive quando o paciente trabalha nove horas por dia."})

# 2. as duas famílias
S.append({"id": "familias", "tipo": "duas", "eyebrow": "Jeukendrup, 2017 · Impey, 2018", "titulo": "Um princípio de planejamento, duas famílias",
          "esq": {"t": "A refeição: alta disponibilidade", "cor": "petr",
                  "itens": ["combustível para o trabalho exigido", "a dose acompanha a sessão que vem",
                            "consensual, baixo risco, quase todo o ganho"]},
          "dir": {"t": "A sobremesa: baixa disponibilidade", "cor": "ambar",
                  "itens": ["treinar em jejum", "dois treinos sem repor entre eles",
                            "a sessão da noite e dormir sem carboidrato"]},
          "destaque": "Periodizar é ajustar a nutrição ao objetivo de cada sessão e de cada fase. Nesse sentido amplo, quase todo mundo deveria periodizar alguma coisa.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2017 e 2018"})

# 3. Marquet
p = [svg_abre(1664, 300, "Melhora no tempo de 10 km após três semanas: controle cerca de 0,1%, sleep low 2,9%, com a mesma quantidade diária de carboidrato")]
x0, esc = 360, 300
barras = [("controle", 0.1, "≈ 0,1%", MUDO), ("dormir com pouco", 2.9, "2,9% mais rápido", OXID)]
rs = []
for i, (n, v, t, c) in enumerate(barras):
    y = 40 + i * 130
    p.append(f'<rect x="{x0}" y="{y}" width="{max(v*esc, 6):.0f}" height="80" rx="4" fill="{c}"/>')
    rs.append(rot(0, y + 22, n, w=340, tam=30, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(x0 + max(v * esc, 6) + 20, y + 22, t, w=400, tam=30, cor=c if c != MUDO else TINTA, peso=700))
p.append(f'<line x1="{x0}" y1="20" x2="{x0}" y2="290" stroke="{TINTA}" stroke-width="3"/>')
p.append("</svg>")
S.append({"id": "marquet", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O lado a favor · Marquet e colaboradores, 2016", "titulo": "Mesmo total, outro horário",
          "destaque": "21 triatletas, três semanas, 6 g/kg/dia nos dois grupos. Não houve restrição do total: foi redistribuição.",
          "destaque_cor": "petr", "fonte": "Melhora no tempo de 10 km · Medicine and Science in Sports and Exercise 2016"})

# 4. Gejl e Nybo
p = [svg_abre(1664, 260, "Meta-análise de nove estudos: diferença média padronizada de 0,17, com intervalo de confiança de −0,15 a 0,49, cruzando o zero")]
fx = lambda v: 832 + v * 1200
p.append(f'<line x1="{fx(0):.0f}" y1="20" x2="{fx(0):.0f}" y2="200" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<line x1="{fx(-0.15):.0f}" y1="110" x2="{fx(0.49):.0f}" y2="110" stroke="{GLIC}" stroke-width="8" stroke-linecap="round"/>')
p.append(f'<rect x="{fx(0.17)-22:.0f}" y="88" width="44" height="44" fill="{GLIC}"/>')
p.append(f'<line x1="{fx(-0.6):.0f}" y1="200" x2="{fx(0.6):.0f}" y2="200" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(fx(0.17) - 150, 36, "0,17", w=300, tam=36, cor=GLIC, peso=700, alinha="center"),
      rot(fx(-0.15) - 150, 140, "−0,15", w=300, tam=26, cor=GLIC, alinha="center"),
      rot(fx(0.49) - 150, 140, "0,49", w=300, tam=26, cor=GLIC, alinha="center"),
      rot(fx(-0.6), 214, "favorece o controle", w=500, tam=24, cor=MUDO),
      rot(fx(0.6) - 500, 214, "favorece a restrição", w=500, tam=24, cor=MUDO, alinha="right"),
      rot(fx(0) - 60, 214, "0", w=120, tam=24, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "gejl", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O outro lado · Gejl e Nybo, 2021", "titulo": "Sinalização não é desfecho",
          "destaque": "E os custos: sessão intensa pior, mais esforço percebido, imunidade, deriva para o déficit, adesão difícil.",
          "destaque_cor": "verm", "fonte": "Diferença média padronizada no desempenho, 9 estudos · Journal of the International Society of Sports Nutrition 2021"})

# 5. cinco limites
S.append({"id": "limites", "tipo": "lista", "eyebrow": "Por que antes da hora", "titulo": "Cinco limites estruturais no amador",
          "itens": [{"t": "Margem de erro", "x": "o elite erra e alguém corrige; o amador descobre três meses depois", "cor": "tinta"},
                    {"t": "O denominador do ganho", "x": "1 a 3% sobre base otimizada, contra buracos grandes no básico", "cor": "verm"},
                    {"t": "Orçamento de atenção", "x": "a complexidade não soma; desloca", "cor": "tinta"},
                    {"t": "Deriva para o déficit", "x": "treinar com pouco vira comer pouco", "cor": "ambar"},
                    {"t": "O objetivo é outro", "x": "pico numa data contra treinar bem o ano inteiro", "cor": "tinta"}],
          "gap_itens": 14})

# 6. triagem
S.append({"id": "triagem", "tipo": "cards", "por_linha": 2, "eyebrow": "A regra de triagem", "titulo": "Quatro coisas estáveis por três meses",
          "cards": [{"t": "Energia total adequada", "x": "fora da zona cinza", "cor": "petr"},
                    {"t": "Proteína distribuída", "x": "e não concentrada no jantar", "cor": "petr"},
                    {"t": "Carboidrato alinhado à sessão", "x": "mais no dia intenso, menos no leve", "cor": "petr"},
                    {"t": "Sono", "x": "a variável que ninguém periodiza", "cor": "petr"}],
          "destaque": "Quem não cumpre as quatro não precisa de periodização. Precisa das quatro.",
          "destaque_cor": "tinta"})

# 7. escada
p = [svg_abre(1664, 400, "Escada de três níveis: um, para todos; dois, para quem compete; três, para quem tem base e suporte")]
niveis = [("1 · para todos", "mais carboidrato nos dias de sessão longa ou intensa", OXID, OXID_T),
          ("2 · para quem compete", "treinar o intestino, ensaiar a prova, carregar antes de eventos longos", GLIC, GLIC_T),
          ("3 · base, objetivo e suporte", "baixa disponibilidade só em sessões leves", FOSF, FOSF_T)]
rs = []
for i, (t, x_, c, f) in enumerate(niveis):
    w = 1664 - i * 300
    y = 280 - i * 130
    p.append(f'<rect x="0" y="{y}" width="{w}" height="110" rx="10" fill="{f}" stroke="{c}" stroke-width="3"/>')
    rs.append(rot(24, y + 12, t, w=w - 48, tam=30, cor=c, peso=700))
    rs.append(rot(24, y + 58, x_, w=w - 48, tam=26, cor=TINTA))
p.append("</svg>")
S.append({"id": "escada", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "As saídas são níveis", "titulo": "Base larga, topo estreito",
          "destaque": "“Eu como igual todo dia?” Não. E dizer isso já é periodizar. No amador, ensaiar a comida da prova rende mais que treinar com pouco.",
          "destaque_cor": "petr", "fonte": "Esquema de níveis · Stellingwerff, Morton e Burke, 2019"})

# 8. nunca
S.append({"id": "nunca", "tipo": "frase", "fundo": "tinta", "eyebrow": "A lista do nunca",
          "frase": "Restrição deliberada aqui é risco sem contrapartida.",
          "apoio": "Adolescente em crescimento · história de transtorno alimentar ou relação difícil com a comida · disponibilidade energética já baixa · gestante · doença crônica descompensada."})

# 9. perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "O critério aplicado", "titulo": "Três perfis típicos, três condutas",
          "cab": ["Perfil", "O que falta", "Conduta"],
          "larguras": [30, 34, 36],
          "linhas": [["Amador que dorme com pouco", "as quatro condições", "suspender e fazer o básico"],
                     ["Quatro estratégias juntas", "atenção para o básico", "manter uma, largar três"],
                     ["Base sólida, prova marcada", "nada", "nível dois, sem treinar com pouco"]],
          "destaque": "Ele fazia a parte difícil e pulava a parte fácil. E os atletas dos estudos não trabalham nove horas por dia.",
          "destaque_cor": "ambar"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "A regra operacional do módulo", "titulo": "Uma mudança por vez",
          "regras": ["Com prazo definido e registro",
                     "Com critério de reversão escrito antes de começar",
                     "Nível três só depois das quatro condições, e nunca nas sessões de qualidade"],
          "cards": [{"t": "Nutricionista", "x": "O desenho da estratégia periodizada."},
                    {"t": "Preparador físico", "x": "Se a base de treino é estável."},
                    {"t": "Médico", "x": "Se há contraindicação clínica."}],
          "quem": "Qualquer um pode perguntar se as quatro coisas estão de pé, antes da sobremesa."})

spec = {"arquivo": "aulas/MOD04/04-04-periodizacao-de-carboidrato.md",
        "modulo": "Nutrição Esportiva", "tema": "petroleo",
        "titulo": "Periodização de carboidrato", "subtitulo": "Disponibilidade manipulada e critérios de indicação",
        "nota_capa": "Entra pela decisão: periodizar, e em que nível.",
        "secoes": {"conceito": ["O conceito e as duas famílias.", "capa"],
                   "evidencia": ["Os dois lados da evidência e os limites no amador.", "marquet"],
                   "saidas": ["Triagem, níveis e perfis.", "triagem"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "04-04.json"), "w"), ensure_ascii=False, indent=1)
print("04-04.json:", len(S), "slides")
