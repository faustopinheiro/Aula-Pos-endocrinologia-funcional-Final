"""Spec do deck 3.11. Gera 03-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

def seta(x1, y1, x2, y2, cor, mid, esp=5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mid})"/>'

# 1. Mikines: 48 horas
p = [svg_abre(1664, 330, "Linha do tempo: uma sessão no dia zero; sensibilidade à insulina aumentada logo depois e ainda 48 horas depois; efeito ausente no quinto dia")]
dx = 1664 / 6
rs = []
p.append(f'<rect x="0" y="80" width="{2*dx:.0f}" height="90" rx="8" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append(f'<line x1="0" y1="220" x2="1664" y2="220" stroke="{TINTA}" stroke-width="3"/>')
for d in range(7):
    x = d * dx
    p.append(f'<line x1="{x:.0f}" y1="210" x2="{x:.0f}" y2="230" stroke="{TINTA}" stroke-width="3"/>')
    rs.append(rot(x - 60 if d else 0, 244, "sessão" if d == 0 else f"dia {d}", w=120, tam=24, cor=MUDO, alinha="center" if d else "left"))
for d, cor, fundo in [(0, OXID, OXID), (2, OXID, OXID), (5, MUDO, CLARO)]:
    p.append(f'<circle cx="{max(d*dx, 14):.0f}" cy="220" r="14" fill="{fundo}" stroke="{cor}" stroke-width="3"/>')
p.append("</svg>")
rs += [rot(24, 104, "sensibilidade à insulina aumentada", w=2 * dx - 48, tam=28, cor=TINTA, peso=700),
       rot(5 * dx - 200, 120, "dia 5: efeito ausente", w=400, tam=26, cor=MUDO, peso=700, alinha="center")]
S.append({"id": "mikines", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Mikines e colaboradores, 1988", "titulo": "Uma sessão, dois dias de insulina funcionando melhor",
          "destaque": "Medido com clamp em repouso, logo depois e 48 horas depois de uma hora de bicicleta. Com cinco dias, já tinha ido embora.",
          "destaque_cor": "petr", "fonte": "American Journal of Physiology 1988 · 7 homens destreinados, 60 min a 150 W"})

# 2. cobertura
dias = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
semanas = [("duas sessões longas", [5, 6]), ("cinco sessões moderadas", [0, 1, 3, 4, 5])]
p = [svg_abre(1664, 360, "Duas semanas: com sessões só no sábado e no domingo, quarta, quinta e sexta ficam descobertas; com cinco sessões espalhadas, a semana toda fica coberta")]
x0, cw = 420, (1664 - 420) / 7
rs = []
for j, d in enumerate(dias):
    rs.append(rot(x0 + j * cw, 0, d, w=cw, tam=24, cor=MUDO, alinha="center"))
for i, (nome, sess) in enumerate(semanas):
    y = 50 + i * 150
    cob = set()
    for s in sess:
        for k in range(3):
            cob.add((s + k) % 7)
    for j in range(7):
        x = x0 + j * cw
        c, f = (OXID, OXID_T) if j in cob else (FOSF, CLARO)
        p.append(f'<rect x="{x+3:.0f}" y="{y}" width="{cw-6:.0f}" height="100" rx="8" fill="{f}" stroke="{c}" stroke-width="{3 if j in cob else 2}"/>')
        if j in sess:
            p.append(f'<circle cx="{x+cw/2:.0f}" cy="{y+50}" r="18" fill="{OXID}"/>')
        elif j not in cob:
            rs.append(rot(x, y + 34, "descoberto", w=cw, tam=22, cor=FOSF, peso=700, alinha="center"))
    rs.append(rot(0, y + 30, nome, w=400, tam=28, cor=TINTA, peso=700, alinha="right"))
p.append("</svg>")
S.append({"id": "cobertura", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A aritmética da cobertura", "titulo": "Para a glicose, a frequência pesa mais que o heroísmo",
          "destaque": "Associação Americana de Diabetes, 2016: 150 minutos por semana, em pelo menos três dias, e no máximo dois dias seguidos sem exercício.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos · cada sessão cobre o próprio dia e os dois seguintes · Diabetes Care 2016"})

# 3. GLUT4: duas portas
p = [svg_abre(1664, 400, "Uma fibra muscular com GLUT4 guardado em vesículas; a insulina e a contração levam o GLUT4 à membrana por vias independentes; no paciente resistente, a via da insulina falha e a da contração continua aberta"),
     "<defs>" + seta_marker("g1", MUDO) + seta_marker("g2", OXID) + "</defs>"]
p.append(f'<rect x="560" y="20" width="1104" height="360" rx="40" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>')
for cx, cy in [(1180, 150), (1260, 230), (1360, 160), (1430, 260), (1300, 310)]:
    p.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="{CARTAO}" stroke="{GLIC}" stroke-width="4"/>')
p.append(caixa(0, 40, 400, 120, MUDO, CLARO, esp=3))
p.append(caixa(0, 240, 400, 120, OXID, OXID_T, esp=4))
p.append(seta(410, 100, 600, 100, MUDO, "g1", esp=5))
p.append(seta(410, 300, 600, 300, OXID, "g2", esp=6))
p.append(f'<g stroke="{FOSF}" stroke-width="10" stroke-linecap="round"><line x1="480" y1="70" x2="530" y2="130"/><line x1="530" y1="70" x2="480" y2="130"/></g>')
p.append("</svg>")
rs = [rot(0, 62, "insulina", w=400, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(0, 108, "falha na resistência", w=400, tam=24, cor=FOSF, alinha="center"),
      rot(0, 262, "contração", w=400, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(0, 308, "via independente, preservada", w=400, tam=24, cor=OXID, alinha="center"),
      rot(640, 50, "fibra muscular", w=440, tam=28, cor=FOSF, peso=700),
      rot(1120, 50, "GLUT4 guardado em vesículas", w=520, tam=26, cor=GLIC, peso=700)]
S.append({"id": "portas", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Richter e Hargreaves, 2013", "titulo": "Duas portas para a mesma glicose",
          "destaque": "Kennedy, 1999: depois de uma sessão de bicicleta, o GLUT4 na membrana subiu cerca de 70%, com e sem diabetes tipo 2.",
          "destaque_cor": "petr", "fonte": "Physiological Reviews 2013 · Diabetes 1999, 5 pessoas com diabetes tipo 2 e 5 controles"})

# 4. dois relógios e o 80%
S.append({"id": "relogios", "tipo": "numeros", "eyebrow": "Dois efeitos, dois relógios", "titulo": "Abrir as portas, e ter mais portas",
          "numeros": [{"n": "48 h", "x": "efeito agudo: abre as portas que já existem", "cor": "petr"},
                      {"n": "semanas", "x": "efeito crônico: mais GLUT4, o estímulo mais potente conhecido", "cor": "tinta"},
                      {"n": "≈ 80%", "x": "da glicose captada sob clamp vai para o músculo", "cor": "ambar"}],
          "destaque": "O tecido que mais capta glicose é o mesmo que a pessoa consegue contrair. Não por analogia. Por anatomia.",
          "destaque_cor": "tinta", "fonte": "Clamp com insulina alta; depois da refeição, o fígado divide mais a conta · DeFronzo 1981 · DeFronzo e Tripathy 2009"})

# 5. melhora sem emagrecer
S.append({"id": "balanca", "tipo": "cards", "por_linha": 2, "eyebrow": "Por que melhora sem emagrecer", "titulo": "Quatro mudanças que a balança não vê",
          "cards": [{"t": "Mais GLUT4", "x": "mais portas para a glicose", "cor": "petr"},
                    {"t": "Mais capilares por fibra", "x": "mais área de troca entre sangue e músculo", "cor": "petr"},
                    {"t": "Mais mitocôndria", "x": "muda o destino do combustível que entra", "cor": "petr"},
                    {"t": "Mais espaço para glicogênio", "x": "tanque maior e, depois da sessão, mais vazio", "cor": "ambar"}],
          "destaque": "E os sinais que o músculo manda para fígado, pâncreas e tecido adiposo. Também fora da balança.",
          "destaque_cor": "tinta"})

# 6. o que medir
S.append({"id": "medir", "tipo": "tabela", "eyebrow": "O que medir no lugar do peso", "titulo": "Barato, e conta a história certa",
          "cab": ["Medida", "Por que usar"],
          "larguras": [40, 60],
          "linhas": [["Circunferência abdominal", "muda antes do peso e conversa melhor com risco"],
                     ["Carga registrada", "a mais motivadora, e quase ninguém anota"],
                     ["Sentar e levantar em 30 s", "teste funcional repetível"],
                     ["Glicada e pressão", "desfechos de verdade, quando há indicação"],
                     ["Bioimpedância de balança doméstica", "não serve sozinha: a água fabrica resultados"]],
          "destaque": "Quem escolhe o peso como único critério abandona. Sal, ciclo, intestino, glicogênio e água mexem nele.",
          "destaque_cor": "verm"})

# 7. perder peso não é perder gordura
p = [svg_abre(1664, 330, "Duas pessoas perdem o mesmo peso em seis meses; uma perde quase só gordura, a outra perde gordura e bastante massa magra")]
rs = []
x0, W = 420, 1180
for i, (nome, g) in enumerate([("pessoa A", 0.9), ("pessoa B", 0.55)]):
    y = 40 + i * 140
    p.append(f'<rect x="{x0}" y="{y}" width="{W*g-2:.0f}" height="90" rx="4" fill="{GLIC}"/>')
    p.append(f'<rect x="{x0+W*g:.0f}" y="{y}" width="{W*(1-g):.0f}" height="90" rx="4" fill="{FOSF}"/>')
    rs.append(rot(0, y + 12, nome, w=400, tam=30, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(0, y + 52, "mesmos quilos perdidos", w=400, tam=22, cor=MUDO, alinha="right"))
    rs.append(rot(x0 + 20, y + 26, "gordura", w=300, tam=28, cor="#FFFFFF", peso=700))
    if 1 - g > 0.3:
        rs.append(rot(x0 + W * g + 20, y + 26, "massa magra", w=W * (1 - g) - 40, tam=28, cor="#FFFFFF", peso=700))
p.append("</svg>")
rs.append(rot(x0 + W - 260, 136, "massa magra", w=260, tam=22, cor=FOSF, peso=700, alinha="right"))
S.append({"id": "composicao", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Composição corporal", "titulo": "Perder peso e perder gordura não são a mesma coisa",
          "destaque": "Decidem o lado: o tamanho do déficit, o estímulo de força e a proteína. Os números podem melhorar enquanto a pessoa piora.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos"})

# 8. sabotadores
S.append({"id": "sabotadores", "tipo": "cards", "eyebrow": "O que derruba tudo por fora do treino", "titulo": "Sono, déficit e semana parada",
          "cards": [{"t": "Sono curto", "x": "Broussard, 2012: quatro noites de 4,5 h na cama pioraram a resposta à insulina no corpo e na célula de gordura", "cor": "verm"},
                    {"t": "Déficit sustentado", "x": "derruba T3 e IGF-1, suprime o eixo gonadal e impede construir músculo", "cor": "ambar"},
                    {"t": "Inatividade", "x": "catorze dias andando menos já pioram a glicose, e a volta é lenta", "cor": "tinta"}],
          "destaque": "O sono deixa de ser item de bem-estar neste módulo. É variável metabólica.",
          "destaque_cor": "tinta", "fonte": "Annals of Internal Medicine 2012 · 7 adultos jovens, cruzado e sorteado"})

# 9. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que os números decidem", "titulo": "Construir músculo que use glicose",
          "regras": ["Distribuir: no máximo dois dias seguidos sem exercício",
                     "Escolher o desfecho: cintura, carga, teste funcional e, quando indicado, glicada",
                     "Proteger a massa magra: déficit moderado, força sempre, proteína adequada"],
          "cards": [{"t": "Médico", "x": "Diagnóstico, tratamento e medicação."},
                    {"t": "Educador e preparador físico", "x": "A prescrição e a distribuição do estímulo."},
                    {"t": "Nutricionista", "x": "A ingestão que sustenta massa magra."}],
          "quem": "Perceber o sono curto, a restrição e a semana parada é de todos."})

spec = {"arquivo": "aulas/MOD03/03-11-insulina-e-composicao-corporal.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Exercício e sensibilidade à insulina", "subtitulo": "Mecanismos, prescrição e composição corporal",
        "nota_capa": "Entra pelo número: quarenta e oito horas.",
        "secoes": {"numero": ["O efeito de uma sessão e a distribuição da semana.", "capa"],
                   "mecanismo": ["As duas portas do GLUT4 e a melhora sem emagrecer.", "portas"],
                   "composicao": ["Composição corporal e o que sabota.", "composicao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-11.json"), "w"), ensure_ascii=False, indent=1)
print("03-11.json:", len(S), "slides")
