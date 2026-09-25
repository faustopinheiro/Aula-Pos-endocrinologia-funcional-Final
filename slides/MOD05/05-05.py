"""Spec do deck 5.5. Gera 05-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. boca e intestino
S.append({"id": "esqueleto", "tipo": "frase", "fundo": "tinta", "eyebrow": "Dois recursos de grupo A",
          "frase": "No nitrato, o problema está na boca. No bicarbonato, no intestino.",
          "apoio": "Baratos, com evidência decente, quase sempre usados errado. O ciclista do contrarrelógio, a judoca de lutas curtas e a corredora que tomou uma colher de bicarbonato na manhã da prova. Nada disso se estreia no dia."})

# 2. a via do nitrato
p = [svg_abre(1664, 260, "Via do nitrato: nitrato da comida, bactérias da língua na saliva, nitrito, óxido nítrico; o enxaguante antisséptico corta a etapa das bactérias"),
     "<defs>" + seta_marker("v1", MUDO) + "</defs>"]
rs = []
etapas = [("nitrato", "folhas e beterraba", OXID, OXID_T), ("bactérias da língua", "na saliva", GLIC, GLIC_T),
          ("nitrito", "engolido de novo", AZUL, AZUL_T), ("óxido nítrico", "custo de O₂ menor", OXID, OXID_T)]
for i, (t, s, c, f) in enumerate(etapas):
    x = i * 420
    p.append(caixa(x, 40, 360, 130, c, f, esp=3))
    rs.append(rot(x, 64, t, w=360, tam=30, cor=c, peso=700, alinha="center"))
    rs.append(rot(x, 110, s, w=360, tam=26, cor=TINTA, alinha="center"))
    if i < 3:
        p.append(f'<line x1="{x+366}" y1="105" x2="{x+410}" y2="105" stroke="{MUDO}" stroke-width="4" marker-end="url(#v1)"/>')
p.append(f'<line x1="700" y1="150" x2="770" y2="210" stroke="{FOSF}" stroke-width="8"/><line x1="770" y1="150" x2="700" y2="210" stroke="{FOSF}" stroke-width="8"/>')
p.append("</svg>")
rs.append(rot(300, 200, "enxaguante antisséptico corta aqui", w=390, tam=26, cor=FOSF, peso=700, alinha="right"))
S.append({"id": "via", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Govoni e colaboradores, 2008", "titulo": "Uma bactéria no meio do mecanismo",
          "destaque": "Sete voluntários, com e sem clorexidina: com o enxaguante, a subida do nitrito no sangue foi muito menor. Suco de beterraba com enxaguante é dinheiro fora.",
          "destaque_cor": "verm", "fonte": "Nitric Oxide 2008"})

# 3. quem responde
S.append({"id": "inversao", "tipo": "duas", "eyebrow": "Jones, 2014", "titulo": "A inversão: rende mais em quem é menos treinado",
          "esq": {"t": "Rende mais", "cor": "petr",
                  "itens": ["menos treinado, amador", "esforço submáximo prolongado", "intermitente de alta intensidade", "linha de pesquisa em pessoas mais velhas"]},
          "dir": {"t": "Rende menos", "cor": "ambar",
                  "itens": ["atleta de elite de resistência", "eficiência já alta", "pouco espaço para melhorar"]},
          "destaque": "Quase todo ergogênico rende mais no alto nível. O nitrato tende a render mais no público deste curso.",
          "destaque_cor": "tinta", "fonte": "Sports Medicine 2014"})

# 4. protocolo nitrato
S.append({"id": "nitrato", "tipo": "numeros", "eyebrow": "O protocolo do nitrato · consenso do Comitê Olímpico, 2018", "titulo": "Duas a três horas, não quinze minutos",
          "numeros": [{"n": "5 a 9 mmol", "x": "de nitrato, cerca de 300 a 560 mg", "cor": "petr"},
                      {"n": "2 a 3 h", "x": "antes: o pico de nitrito é lento", "cor": "ambar"},
                      {"n": "> 3 dias", "x": "de uso antes da competição parecem ajudar", "cor": "tinta"}],
          "destaque": "Shot concentrado com dose no rótulo para o dia de prova. Folhas verde-escuras e beterraba no prato para o resto: comida primeiro continua valendo.",
          "destaque_cor": "petr", "fonte": "British Journal of Sports Medicine 2018"})

# 5. cinco erros
S.append({"id": "erros", "tipo": "lista", "eyebrow": "Os cinco erros do nitrato", "titulo": "Onde o protocolo se perde",
          "itens": [{"t": "Enxaguante, bala ou chiclete antisséptico", "x": "suspender nos dias de uso", "cor": "verm"},
                    {"t": "Suco caseiro como se fosse dose", "x": "o teor varia com solo, variedade e preparo", "cor": "ambar"},
                    {"t": "Tomar quinze minutos antes", "x": "não dá tempo", "cor": "ambar"},
                    {"t": "Susto com urina ou fezes avermelhadas", "x": "é beterraba; avisar antes", "cor": "tinta"},
                    {"t": "Esquecer o intestino", "x": "volume concentrado perto do esforço: ensaiar", "cor": "tinta"}],
          "gap_itens": 14})

# 6. bicarbonato mecanismo
p = [svg_abre(1664, 280, "Fibra muscular e sangue: a beta-alanina age dentro da fibra, como carnosina; o bicarbonato age no sangue, aumentando a reserva alcalina que puxa o íon hidrogênio para fora"),
     "<defs>" + seta_marker("b1", FOSF) + "</defs>"]
p.append(caixa(0, 30, 700, 220, AZUL, AZUL_T, esp=3))
p.append(caixa(960, 30, 700, 220, OXID, OXID_T, esp=3))
p.append(f'<line x1="600" y1="140" x2="1060" y2="140" stroke="{FOSF}" stroke-width="6" marker-end="url(#b1)"/>')
p.append("</svg>")
rs = [rot(0, 50, "dentro da fibra", w=700, tam=30, cor=AZUL, peso=700, alinha="center"),
      rot(0, 170, "beta-alanina: carnosina", w=560, tam=28, cor=TINTA, alinha="center"),
      rot(960, 50, "no sangue", w=700, tam=30, cor=OXID, peso=700, alinha="center"),
      rot(1100, 170, "bicarbonato: reserva alcalina", w=560, tam=28, cor=TINTA, alinha="center"),
      rot(600, 90, "H⁺ sai da fibra", w=460, tam=28, cor=FOSF, peso=700, alinha="center")]
S.append({"id": "tampoes", "tipo": "diagrama", "h": 280, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O bicarbonato · Grgic e colaboradores, 2021", "titulo": "Dois tampões, dois compartimentos",
          "destaque": "Melhora em resistência muscular, em lutas (boxe, judô, caratê, taekwondo, luta olímpica) e em ciclismo, corrida e natação de alta intensidade.",
          "destaque_cor": "petr", "fonte": "Journal of the International Society of Sports Nutrition 2021"})

# 7. protocolo bicarbonato
S.append({"id": "bicarbonato", "tipo": "numeros", "eyebrow": "O protocolo do bicarbonato", "titulo": "Muito pó, e o tempo varia de pessoa para pessoa",
          "numeros": [{"n": "0,2 a 0,5", "x": "g/kg; 0,2 a 0,3 para tolerar melhor", "cor": "petr"},
                      {"n": "14 a 21 g", "x": "para 70 kg, com 0,2 a 0,3 g/kg", "cor": "ambar"},
                      {"n": "60 a 180 min", "x": "antes, individualizado em treino", "cor": "tinta"}],
          "destaque": "Uso repetido ao longo de semanas, junto ao treino, é linha de pesquisa, não conduta fechada.",
          "destaque_cor": "tinta"})

# 8. intestino
S.append({"id": "intestino", "tipo": "lista", "eyebrow": "O intestino decide", "titulo": "O que separa o protocolo da prova perdida",
          "itens": [{"t": "Dose menor", "x": "0,2 ou 0,3 g/kg", "cor": "petr"},
                    {"t": "Mais cedo", "x": "perto de 180 minutos antes", "cor": "petr"},
                    {"t": "Com refeição rica em carboidrato", "x": "reduz o desconforto", "cor": "petr"},
                    {"t": "Cápsula com revestimento entérico", "x": "quando disponível; dividir a dose também ajuda", "cor": "ambar"},
                    {"t": "Testar duas vezes em treino", "x": "mesma hora, mesma refeição; quem não tolerou não usa", "cor": "verm"}],
          "gap_itens": 14})

# 9. limites
S.append({"id": "limites", "tipo": "cards", "por_linha": 3, "eyebrow": "Os limites clínicos", "titulo": "“É só bicarbonato de cozinha”",
          "cards": [{"t": "Sódio", "x": "a dose traz muito sódio", "cor": "ambar"},
                    {"t": "Hipertensão e coração", "x": "hipertensão, insuficiência cardíaca", "cor": "verm"},
                    {"t": "Rim", "x": "doença renal", "cor": "verm"},
                    {"t": "Medicação", "x": "que mexe com eletrólitos ou equilíbrio ácido-básico", "cor": "ambar"},
                    {"t": "Alcalose", "x": "risco em dose alta", "cor": "verm"},
                    {"t": "Nitrato", "x": "medicação para disfunção erétil, nitrato cardiológico, anti-hipertensivo", "cor": "tinta"}],
          "fonte": "Doença crônica: decisão médica"})

# 10. três perfis
S.append({"id": "perfis", "tipo": "tabela", "eyebrow": "Três perfis típicos", "titulo": "Quanto dura o esforço, e o que cabe",
          "cab": ["Perfil", "Esforço", "O que cabe"],
          "larguras": [24, 20, 56],
          "linhas": [["Ciclista, contrarrelógio", "20 min", "nitrato: shot, 2 a 3 h antes, alguns dias antes, sem enxaguante"],
                     ["Judoca, várias lutas", "4 a 5 min", "beta-alanina como base; bicarbonato testado; nunca com corte de peso"],
                     ["Corredora, 5 km", "20 a 30 min", "fora da janela do bicarbonato; nitrato é mais defensável"]],
          "destaque": "“O que você usou não tem indicação para a sua prova, e o jeito como você usou não funcionaria nem na prova certa.”",
          "destaque_cor": "ambar"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O quadro-resumo", "titulo": "Isso já foi testado fora da prova?",
          "regras": ["Nitrato: 5 a 9 mmol, 2 a 3 h antes, mais de 3 dias ajudam, sem enxaguante",
                     "Bicarbonato: 0,2 a 0,5 g/kg, a menor dose, 60 a 180 min, individualizado",
                     "O intestino decide o bicarbonato; a boca decide o nitrato"],
          "cards": [{"t": "Nutricionista", "x": "Indica e dosa os dois."},
                    {"t": "Médico", "x": "Pressão, rim, coração, medicação, corte de peso."},
                    {"t": "Preparador e educador físico", "x": "O ensaio em treino."}],
          "quem": "Sem ensaio, não existe protocolo."})

spec = {"arquivo": "aulas/MOD05/05-05-nitrato-beterraba-e-bicarbonato-de-sodio.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Nitrato e bicarbonato de sódio", "subtitulo": "Mecanismos, protocolos e tolerância",
        "nota_capa": "Entra pelos dois lugares onde o protocolo falha.",
        "secoes": {"esqueleto": ["O nitrato: via, resposta e protocolo.", "capa"],
                   "tampoes": ["O bicarbonato: protocolo, intestino e limites.", "tampoes"],
                   "perfis": ["Os três perfis e o quadro.", "perfis"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-05.json"), "w"), ensure_ascii=False, indent=1)
print("05-05.json:", len(S), "slides")
