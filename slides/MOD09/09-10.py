"""Spec do deck 9.10. Gera 09-10.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "planilha", "tipo": "frase", "fundo": "tinta", "eyebrow": "Pré-temporada no tênis",
          "frase": "Onze testes, cento e trinta e dois números, nenhum treino mudou.",
          "apoio": "Doze atletas, uma manhã de sábado. Três meses depois, ninguém tinha aberto a planilha de novo. Faltou um procedimento: perguntar, escolher, aplicar, interpretar e repetir."})

S.append({"id": "pergunta", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo um", "titulo": "A pergunta vem antes do teste",
          "cards": [{"t": "Prescrever", "x": "a referência de onde saem zonas e séries", "cor": "petr"},
                    {"t": "Medir mudança", "x": "refazer do mesmo jeito e ver se o programa funciona", "cor": "petr"},
                    {"t": "Diagnosticar o método", "x": "quatro meses de treino e o teste parado é informação", "cor": "ambar"}],
          "destaque": "Que decisão este número vai mudar? Teste que não muda nenhuma decisão sai da lista.",
          "destaque_cor": "tinta"})

S.append({"id": "propriedades", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo dois: escolher", "titulo": "Três propriedades de um bom teste",
          "cards": [{"t": "Validade", "x": "mede o que interessa para aquele esporte?", "cor": "tinta"},
                    {"t": "Confiabilidade", "x": "feito duas vezes, sem mudança real, o resultado se repete?", "cor": "petr"},
                    {"t": "Sensibilidade", "x": "enxerga uma mudança do tamanho das que importam?", "cor": "ambar"}],
          "destaque": "Contrarrelógios costumam variar menos de um dia para outro do que testes até a exaustão.",
          "destaque_cor": "tinta", "fonte": "Revisão, Sports Med 2008"})

S.append({"id": "parecido", "tipo": "tabela", "eyebrow": "Escolher", "titulo": "O teste mais parecido com o que a pessoa faz",
          "cab": ["Perfil", "Teste"],
          "larguras": [40, 60],
          "linhas": [["Corredor de rua", "contrarrelógio na distância que já corre"],
                     ["Quadra: tênis, futsal, basquete", "vaivém de 20 metros, em grupo"],
                     ["Praticante de força", "repetições até a falha técnica em carga conhecida"],
                     ["Saúde, depois dos cinquenta", "sentar e levantar em 30 segundos, preensão"]],
          "destaque": "Limiares de campo estão na aula de limiares do módulo de fisiologia. Especificidade também é aderência.",
          "destaque_cor": "tinta", "fonte": "Vaivém: Eur J Appl Physiol 1982"})

S.append({"id": "padronizar", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo três: aplicar", "titulo": "Padronizar, e por escrito",
          "cards": [{"t": "Mesmo horário e local", "x": "mesma superfície, mesmo percurso", "cor": "petr"},
                    {"t": "Mesmo aquecimento", "x": "escrito, não improvisado", "cor": "petr"},
                    {"t": "Mesmo calçado e cafeína", "x": "ou nenhuma, das duas vezes", "cor": "petr"},
                    {"t": "48 horas sem sessão pesada", "x": "prática corrente", "cor": "ambar"},
                    {"t": "Ambiente anotado", "x": "calor, umidade e vento mudam o resultado", "cor": "ambar"},
                    {"t": "Pista hoje, parque amanhã", "x": "compara dois lugares, não o atleta", "cor": "verm"}]})

# ordem da bateria
passos = ["repouso", "sem fadiga", "agilidade", "potência e força", "sprint", "resistência local", "anaeróbio", "aeróbio"]
p = [svg_abre(1664, 300, "Sequência recomendada da bateria, do menos para o mais cansativo, com o teste aeróbio por último"),
     "<defs>" + seta_marker("sq", MUDO) + "</defs>"]
w, gap = 176, 30
for i, t in enumerate(passos):
    x = 20 + i * (w + gap)
    cor = OXID if i < 3 else (GLIC if i < 6 else FOSF)
    p.append(f'<rect x="{x}" y="90" width="{w}" height="110" rx="10" fill="{cor}"/>')
    if i < len(passos) - 1:
        p.append(f'<line x1="{x + w + 3}" y1="145" x2="{x + w + gap - 5}" y2="145" stroke="{MUDO}" stroke-width="3" marker-end="url(#sq)"/>')
p.append("</svg>")
rs = []
for i, t in enumerate(passos):
    x = 20 + i * (w + gap)
    rs.append(rot(x + 6, 124, t, w=w - 12, tam=22, cor="#F7F6F2", peso=700, alinha="center"))
rs.append(rot(20, 30, "menos cansativo", w=400, tam=22, cor=MUDO))
rs.append(rot(1004, 30, "mais cansativo, de preferência em outro dia", w=640, tam=22, cor=MUDO, alinha="right"))
S.append({"id": "ordem", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A ordem da bateria", "titulo": "Cada teste não pode estragar o seguinte",
          "destaque": "No tênis, o vaivém foi o primeiro da manhã. Todos os saltos e sprints depois dele foram medidos em atletas cansados.",
          "destaque_cor": "verm", "fonte": "Sequência do manual da NSCA"})

# familiarização
p = [svg_abre(1664, 320, "Três testes do mesmo atleta: o primeiro mais baixo, o segundo e o terceiro no mesmo nível")]
base = 270
vals = [(1, 150, GRADE), (2, 200, OXID), (3, 204, OXID)]
for i, (n, h, c) in enumerate(vals):
    x = 300 + i * 400
    p.append(f'<rect x="{x}" y="{base - h}" width="200" height="{h}" rx="8" fill="{c}"/>')
p.append(f'<line x1="200" y1="{base}" x2="1500" y2="{base}" stroke="{GRADE}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(300, base + 10, "1º teste", w=200, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(700, base + 10, "2º teste", w=200, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(1100, base + 10, "3º teste", w=200, tam=24, cor=TINTA, peso=700, alinha="center"),
      rot(300, base - 150 - 40, "aprendizado", w=200, tam=22, cor=MUDO, alinha="center"),
      rot(700, base - 200 - 40, "linha de base", w=200, tam=22, cor=TINTA, peso=700, alinha="center")]
S.append({"id": "familiarizar", "tipo": "diagrama", "h": 320, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Familiarização", "titulo": "O primeiro teste é aprendizado",
          "destaque": "Quem compara o terceiro com o primeiro comemora um ganho que é, em parte, só aprendizado. Em equipe: o primeiro entra num treino comum.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "linha", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "Um teste simples, feito sempre do mesmo jeito, vale mais que um teste sofisticado feito uma vez.",
          "apoio": "O valor de uma bateria não está na primeira aplicação. Está na terceira, quando existe uma linha."})

# ruído x menor mudança
p = [svg_abre(1664, 300, "Régua com a faixa de ruído do teste em torno do resultado anterior, mais larga que a menor mudança que importa")]
cx = 700
p.append(f'<line x1="120" y1="170" x2="1540" y2="170" stroke="{GRADE}" stroke-width="4"/>')
p.append(f'<rect x="{cx - 260}" y="120" width="520" height="100" rx="10" fill="{GRADE}" opacity="0.8"/>')
p.append(f'<line x1="{cx}" y1="100" x2="{cx}" y2="222" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<rect x="{cx}" y="150" width="140" height="40" rx="6" fill="{OXID}"/>')
p.append(f'<circle cx="{cx + 380}" cy="170" r="16" fill="{FOSF}"/>')
p.append("</svg>")
rs = [rot(cx - 260, 232, "ruído do teste: erro típico", w=520, tam=22, cor=MUDO, alinha="center"),
      rot(cx - 420, 96, "resultado anterior", w=400, tam=22, cor=TINTA, peso=700, alinha="right"),
      rot(cx + 10, 80, "menor mudança que importa", w=400, tam=22, cor=OXID, peso=700),
      rot(cx + 300, 200, "fora do ruído: notícia", w=260, tam=22, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "ruido", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo quatro: interpretar", "titulo": "Erro típico e menor mudança que importa",
          "destaque": "Se o ruído é maior que a mudança que importa, o teste feito uma vez não vê a melhora. Repita a medida no dia (três saltos, a média) ou troque o teste.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · Sports Med 2000 · Sportscience 2004 (0,2 do desvio-padrão)"})

S.append({"id": "bruto", "tipo": "duas", "eyebrow": "Interpretar", "titulo": "Acompanhe o dado bruto, não a estimativa",
          "esq": {"t": "Medido", "cor": "petr",
                  "itens": ["2.600 m em março", "2.750 m em julho", "melhorou: a informação está completa"]},
          "dir": {"t": "Calculado", "cor": "verm",
                  "itens": ["consumo máximo estimado por equação", "soma o erro do teste ao da equação", "fórmulas de frequência máxima por idade"]},
          "destaque": "As zonas saem da velocidade ou da potência medida, não de um número calculado.",
          "destaque_cor": "tinta", "fonte": "Exemplo ilustrativo"})

S.append({"id": "repetir", "tipo": "duas", "eyebrow": "Passo cinco: repetir", "titulo": "Um calendário enxuto, e como saber que não funciona",
          "esq": {"t": "O calendário", "cor": "petr",
                  "itens": ["desempenho a cada 8 a 12 semanas", "submáximo mensal: 5 minutos na mesma velocidade, FC no fim", "teste máximo com triagem prévia"]},
          "dir": {"t": "Sinais de que não funciona", "cor": "verm",
                  "itens": ["nenhum treino mudou por causa dela", "números sobem e descem sem padrão", "o atleta falta no dia do teste"]},
          "destaque": "Mesma velocidade custando menos batimentos é adaptação; custando mais, fadiga, calor ou doença chegando.",
          "destaque_cor": "tinta", "fonte": "Revisão, Front Physiol 2014 · frequência como prática corrente"})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Testes físicos", "titulo": "Para o tênis: três testes, dois dias, a ordem certa",
          "regras": ["A pergunta escrita ao lado de cada teste",
                     "Primeiro ciclo como familiarização",
                     "Erro típico antes de comemorar"],
          "cards": [{"t": "Preparação física", "x": "Escolhe, padroniza e mantém a linha."},
                    {"t": "Médico", "x": "Faz a triagem antes do teste máximo."},
                    {"t": "Atleta", "x": "Chega descansado e vê a própria série."}],
          "quem": "Próxima aula: reintegração ao treinamento coletivo."})

spec = {"arquivo": "aulas/MOD09/09-10-testes-fisicos-escolher-aplicar-e-interpretar.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Testes físicos", "subtitulo": "Escolher, aplicar e interpretar, em cinco passos",
        "nota_capa": "Entra por uma pré-temporada de tênis com onze testes numa manhã.",
        "secoes": {"planilha": ["A cena e a pergunta.", "capa"],
                   "propriedades": ["Escolher o teste.", "propriedades"],
                   "padronizar": ["Aplicar: padronização, ordem e familiarização.", "padronizar"],
                   "ruido": ["Interpretar e repetir.", "ruido"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-10.json"), "w"), ensure_ascii=False, indent=1)
print("09-10.json:", len(S), "slides")
