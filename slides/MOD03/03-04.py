"""Spec do deck 3.4. Gera 03-04.json ao lado deste arquivo."""
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

# 1. o pedido
S.append({"id": "pedido", "tipo": "duas", "eyebrow": "280 ng/dL e um pedido pronto", "titulo": "Um quadro que aponta para vinte coisas",
          "esq": {"t": "Os sintomas atribuídos à testosterona", "cor": "verm",
                  "itens": ["cansaço", "libido baixa", "dificuldade de ganhar massa", "humor ruim"]},
          "dir": {"t": "O que também produz esse quadro", "cor": "tinta",
                  "itens": ["sono curto, apneia", "déficit de energia", "excesso de treino", "depressão"]},
          "destaque": "“Minha testosterona está em 280, já pesquisei, está abaixo do normal, eu quero começar reposição.”",
          "destaque_cor": "ambar"})

# 2. duas verdades
S.append({"id": "verdades", "tipo": "duas", "eyebrow": "Duas coisas verdadeiras ao mesmo tempo", "titulo": "Doença real, e o eixo mais fácil de desligar",
          "esq": {"t": "Hipogonadismo existe", "cor": "verm",
                  "itens": ["Klinefelter, quimio ou radioterapia pélvica, trauma ou torção", "tumor de hipófise, prolactina alta, hemocromatose",
                            "opioide crônico, corticoide em dose alta", "anabolizante com eixo que não recuperou"]},
          "dir": {"t": "Suprimido por contexto", "cor": "petr",
                  "itens": ["reprodução é a função mais adiável", "quando falta caixa, é o primeiro corte",
                            "sono, energia, treino, vida", "dos cinco eixos, o mais fácil de desligar"]},
          "destaque": "A pergunta não é “quanto está”. É: o eixo está doente, ou está fazendo o que deveria diante da conta desse homem?",
          "destaque_cor": "tinta"})

# 3. eixo e par
p = [svg_abre(1664, 440, "O gerador de pulsos no hipotálamo, com neurônios de kisspeptina sensíveis a leptina, insulina e substrato, comanda a hipófise, que libera LH e FSH, que comandam o testículo; a testosterona volta ao topo"),
     "<defs>" + seta_marker("t1", TINTA) + seta_marker("t2", FOSF) + seta_marker("t3", GLIC) + "</defs>"]
for nome, y, cor in (("gerador de pulsos", 20, AZUL), ("hipófise: LH e FSH", 170, AZUL), ("testículo", 320, OXID)):
    p.append(caixa(300, y, 460, 96, cor, CARTAO, esp=4))
for y in (116, 266):
    p.append(seta(530, y + 4, 530, y + 46, TINTA, "t1", esp=5))
for k in range(3):
    p.append(seta(40, 30 + k * 34, 290, 68, GLIC, "t3", esp=3))
p.append(f'<path d="M760 368 C 900 368, 900 68, 772 68" fill="none" stroke="{FOSF}" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#t2)"/>')
p.append(f'<line x1="990" y1="0" x2="990" y2="440" stroke="{GRADE}" stroke-width="3"/>')
p.append(caixa(1040, 60, 624, 150, FOSF, FOSF_T, esp=3))
p.append(caixa(1040, 250, 624, 150, OXID, OXID_T, esp=3))
p.append("</svg>")
rs = [rot(300, 50, "gerador de pulsos", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(300, 200, "hipófise: LH e FSH", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(300, 350, "testículo", w=460, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 130, "kisspeptina: leptina, insulina, substrato", w=280, tam=24, cor=GLIC, peso=700),
      rot(890, 200, "testosterona avisa o topo", w=100, tam=24, cor=FOSF, peso=600),
      rot(1070, 80, "Testosterona baixa, LH alto", w=580, tam=30, cor=FOSF, peso=700),
      rot(1070, 130, "o comando foi dado e o testículo não cumpriu: primário", w=580, tam=26, cor=TINTA),
      rot(1070, 270, "Testosterona baixa, LH baixo ou normal", w=580, tam=30, cor=OXID, peso=700),
      rot(1070, 320, "o centro não pediu: no praticante, o mais comum", w=580, tam=26, cor=TINTA)]
S.append({"id": "eixo", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um sensor de energia acoplado à ignição", "titulo": "O cortisol é o hormônio do agora; a testosterona, do depois"})

# 4. medir direito
pts = [(h, 100 - 30 * (1 - math.cos(math.pi * (h - 7) / 24)) / 2 if h >= 7 else 100) for h in [x / 2 for x in range(14, 47)]]
def marca(fx, fy):
    return (f'<circle cx="{fx(16.5):.0f}" cy="{fy(100 - 30 * (1 - math.cos(math.pi * 9.5 / 24)) / 2):.0f}" r="14" fill="{FOSF}" stroke="#F7F6F2" stroke-width="3"/>'
            f'<circle cx="{fx(8):.0f}" cy="{fy(100 - 30 * (1 - math.cos(math.pi / 24)) / 2):.0f}" r="14" fill="{OXID}" stroke="#F7F6F2" stroke-width="3"/>')
svg, rs = linhas(1000, 380, "Testosterona ao longo do dia: mais alta às 7 ou 8 horas e mais baixa no fim da tarde; uma coleta às 16h30 cai no vale",
                 [{"nome": "", "cor": AZUL, "pts": pts}], 7, 23, 60, 105, [(7, "7 h"), (11, "11 h"), (15, "15 h"), (19, "19 h"), (23, "23 h")], [],
                 margem=(20, 30, 60, 20), extra=marca)
rs += [rot(120, 0, "coleta às 8 h, em jejum", w=400, tam=26, cor=OXID, peso=700),
       rot(520, 200, "coleta às 16h30: o vale", w=380, tam=26, cor=FOSF, peso=700)]
p = [svg.replace("</svg>", "")]
conds = ["manhã cedo", "em jejum", "sem doença aguda", "longe de treino extenuante"]
for i, c in enumerate(conds):
    p.append(f'<rect x="1080" y="{10 + i*80}" width="584" height="64" rx="32" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
    rs.append(rot(1080, 10 + i * 80 + 17, c, w=584, tam=28, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
svg4 = "".join(p).replace('width="1000" height="380" viewBox="0 0 1000 380"', 'width="1664" height="380" viewBox="0 0 1664 380"')
S.append({"id": "medir", "tipo": "diagrama", "h": 380, "svg": svg4, "rotulos": rs,
          "eyebrow": "A causa mais comum é logística", "titulo": "Medir direito, e repetir",
          "destaque": "Um valor baixo isolado não faz diagnóstico: segunda dosagem matinal, em jejum, em outro dia. Repetir custa uma coleta. Errar custa um eixo.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · Bhasin e colaboradores, Endocrine Society 2018"})

# 5. frações e SHBG
p = [svg_abre(1664, 400, "Testosterona total dividida em ligada à SHBG, ligada à albumina e livre, de 1 a 2%. Dois perfis: obesidade com SHBG baixa e total baixa; atleta magro em restrição com SHBG alta que esconde a supressão")]
fr = [(58, AZUL, "ligada à SHBG: guardada"), (40, GLIC, "ligada à albumina: solta fácil"), (2, FOSF, "")]
x = 0
rs = []
for v, cor, nome in fr:
    w = 1664 * v / 100
    p.append(f'<rect x="{x:.0f}" y="40" width="{max(w-2, 6):.0f}" height="80" rx="4" fill="{cor}"/>')
    if nome:
        rs.append(rot(x, 62, nome, w=w, tam=28, cor="#F7F6F2", peso=700, alinha="center"))
    x += w
rs.append(rot(1300, 0, "livre: 1 a 2%", w=364, tam=28, cor=FOSF, peso=700, alinha="right"))
p.append(caixa(0, 170, 810, 220, GLIC, GLIC_T, esp=3))
p.append(caixa(854, 170, 810, 220, AZUL, AZUL_T, esp=3))
p.append("</svg>")
rs += [rot(30, 190, "Obesidade e resistência à insulina", w=760, tam=30, cor=TINTA, peso=700),
       rot(30, 240, "SHBG baixa, total baixa: a livre está bem menos comprometida do que o número assusta", w=750, tam=26, cor=TINTA),
       rot(884, 190, "Atleta magro em restrição", w=760, tam=30, cor=TINTA, peso=700),
       rot(884, 240, "SHBG alta: a total fica confortável e pode esconder uma supressão real", w=750, tam=26, cor=TINTA)]
S.append({"id": "fracoes", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A total engana nos dois sentidos", "titulo": "Quem decide é a SHBG",
          "destaque": "Peça SHBG junto e use a livre calculada. Imunoensaio direto de testosterona livre não sustenta decisão.",
          "destaque_cor": "petr", "fonte": "Proporções aproximadas · Bhasin e colaboradores, Endocrine Society 2018"})

# 6. estradiol
S.append({"id": "estradiol", "tipo": "cards", "eyebrow": "Finkelstein e colaboradores, 2013", "titulo": "O estradiol no homem não é impureza",
          "cards": [{"t": "Acompanhou a testosterona", "x": "massa magra, área muscular da coxa, força no leg press", "cor": "petr"},
                    {"t": "Acompanhou o estradiol", "x": "acúmulo de gordura, sobretudo", "cor": "ambar"},
                    {"t": "Dependeu dos dois", "x": "libido e ereção", "cor": "verm"}],
          "destaque": "Bloquear aromatase para “otimizar” custa gordura, osso e função sexual: o que o paciente foi buscar.",
          "destaque_cor": "verm", "fonte": "New England Journal of Medicine 2013 · homens de 20 a 50 anos, produção própria suprimida, testosterona em doses graduadas, com e sem inibidor de aromatase"})

# 7. pico agudo
p = [svg_abre(1664, 360, "Régua de 0 a 48 horas: o pico hormonal depois da sessão volta ao basal em cerca de uma hora; a síntese de proteína muscular segue elevada por 24 a 48 horas")]
X0, W = 320, 1320
esc = lambda h: X0 + h / 48 * W
for h in (0, 12, 24, 36, 48):
    p.append(f'<line x1="{esc(h):.0f}" y1="20" x2="{esc(h):.0f}" y2="250" stroke="{GRADE}" stroke-width="2"/>')
p.append(f'<rect x="{esc(0):.0f}" y="50" width="{esc(1)-esc(0):.0f}" height="60" rx="6" fill="{FOSF}"/>')
p.append(f'<rect x="{esc(0):.0f}" y="160" width="{esc(48)-esc(0):.0f}" height="60" rx="30" fill="{OXID}"/>')
p.append("</svg>")
rs = [rot(0, 64, "pico hormonal agudo", w=300, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 174, "síntese de proteína", w=300, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(esc(1) + 20, 64, "cerca de uma hora", w=400, tam=28, cor=FOSF, peso=700),
      rot(esc(12), 174, "24 a 48 horas", w=400, tam=28, cor="#F7F6F2", peso=700)]
rs += [rot(esc(h) - 60, 262, f"{h} h", w=120, tam=24, cor=MUDO, alinha="center") for h in (0, 12, 24, 36, 48)]
rs.append(rot(0, 316, "56 homens, 12 semanas: o tamanho do pico não previu quem ganhou mais massa ou força", w=1664, tam=28, cor=TINTA, peso=600))
S.append({"id": "pico", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O mito mais difundido do assunto", "titulo": "Um sinal de minutos não explica um processo de dois dias",
          "destaque": "Ambiente hormonal crônico importa muito. O pico agudo da sessão é outra coisa.",
          "destaque_cor": "petr", "fonte": "Esquema de tempo · West e Phillips, European Journal of Applied Physiology 2012 · West e colaboradores, Journal of Applied Physiology 2010"})

# 8. saída A
S.append({"id": "saidaA", "tipo": "lista", "eyebrow": "Saída A", "titulo": "Repor agora, quando a leitura está errada",
          "itens": [{"t": "O LH cai e o testículo para", "x": "parado por meses a anos, nem sempre volta ao que era", "cor": "verm"},
                    {"t": "A produção de espermatozoide fica comprometida", "x": "e ninguém perguntou se ele ainda quer ter filho", "cor": "verm"},
                    {"t": "O contexto continua rodando embaixo", "x": "o número normaliza e a causa fica", "cor": "tinta"}],
          "destaque": "O argumento é honesto: ele tem sintoma e a reposição funciona. O custo aparece quando o número era contexto.",
          "destaque_cor": "ambar"})

# 9. saída B
p = [svg_abre(1664, 380, "À esquerda, uma semana dormindo cinco horas reduziu a testosterona diurna em 10 a 15% em homens de 24 anos. À direita, caso ilustrativo: 280 ng/dL, quatro meses corrigindo sono, déficit e treino, 510 ng/dL sem reposição")]
p.append(f'<line x1="600" y1="0" x2="600" y2="380" stroke="{GRADE}" stroke-width="3"/>')
Y0, ESCV = 300, 0.45
for x, v, cor in ((720, 280, FOSF), (1440, 510, OXID)):
    p.append(f'<rect x="{x}" y="{Y0 - v*ESCV:.0f}" width="180" height="{v*ESCV:.0f}" rx="4" fill="{cor}"/>')
p.append(f'<line x1="660" y1="{Y0}" x2="1664" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
p.append(f'<defs>{seta_marker("b9", MUDO)}</defs>')
p.append(seta(930, 200, 1410, 200, MUDO, "b9", esp=4))
p.append("</svg>")
rs = [rot(0, 20, "10 a 15%", w=560, tam=96, cor=FOSF, peso=700, serif=True),
      rot(0, 150, "menos testosterona diurna depois de uma semana dormindo cinco horas", w=560, tam=28, cor=TINTA),
      rot(0, 260, "dez homens, 24 anos: o equivalente a envelhecer 10 a 15 anos", w=560, tam=26, cor=MUDO),
      rot(690, Y0 - 280 * ESCV - 50, "280", w=240, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1410, Y0 - 510 * ESCV - 50, "510", w=240, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(930, 110, "quatro meses: déficit moderado, 4 treinos, acordar 6h30", w=480, tam=24, cor=TINTA, alinha="center"),
      rot(690, 316, "LH baixo-normal", w=240, tam=24, cor=MUDO, alinha="center"),
      rot(1410, 316, "sem reposição", w=240, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "saidaB", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída B: corrigir a conta e reavaliar", "titulo": "Aquele número não era um achado; era um resultado",
          "fonte": "Leproult e Van Cauter, JAMA 2011 · à direita, caso ilustrativo, em ng/dL"})

# 10. saída C
S.append({"id": "saidaC", "tipo": "duas", "eyebrow": "Saída C", "titulo": "Investigar a causa verdadeira",
          "esq": {"t": "Obrigatória quando", "cor": "verm",
                  "itens": ["LH alto com testosterona baixa", "alteração visual, dor de cabeça, galactorreia",
                            "trauma, quimio ou radioterapia, caxumba", "testículos pequenos, ginecomastia, anabolizante"]},
          "dir": {"t": "Quando é pulada", "cor": "tinta",
                  "itens": ["anos de “estilo de vida” em quem tinha Klinefelter", "prolactinoma, tumor de hipófise",
                            "erro mais raro, e mais grave"]},
          "destaque": "Nem todo mundo responde à correção da conta. O que se defende não é nunca repor: é nunca repor sem ter montado a conta antes.",
          "destaque_cor": "petr"})

# 11. seis perguntas
S.append({"id": "criterio", "tipo": "duas", "eyebrow": "O que torna a decisão defensável", "titulo": "Seis perguntas",
          "esq": {"t": "Antes de dosar", "cor": "petr",
                  "itens": ["Como está a conta: sono, energia, treino, vida?", "Déficit ou perda de peso rápida?",
                            "Usa ou já usou algo hormonal, pelo nome, sem julgamento?"]},
          "dir": {"t": "Antes de repor: decisão médica", "cor": "verm",
                  "itens": ["A conta foi corrigida e mantida por tempo suficiente?", "Sintoma consistente, e não só número?",
                            "Ele sabe da supressão e do impacto na fertilidade?"]},
          "destaque": "Relação testosterona-cortisol: reconheça quando aparecer, não use para decidir. Para carga, carga interna, sono, peso e relato.",
          "destaque_cor": "ambar", "fonte": "Urhausen, Gabriel e Kindermann, Sports Medicine 1995"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quem faz o quê", "titulo": "O que aconteceu nos últimos seis meses, antes da dose",
          "regras": ["Pedir, interpretar e repor é ato médico",
                     "Reconhecer o padrão é de todo mundo, e se faz sem exame"],
          "cards": [{"t": "Quem atende toda semana", "x": "Vê primeiro: peso que caiu, volume sem comida, sono curto, rendimento, irritação, libido."},
                    {"t": "O encaminhamento", "x": "“Perdeu 11 kg em 5 meses, 6 sessões, dorme 5h30, rendimento e libido em queda há 3 meses.”"}],
          "quem": "Reposição, eixo pós-anabolizante e moduladores seletivos exigem formação clínica que um módulo não entrega."})

spec = {"arquivo": "aulas/MOD03/03-04-testosterona-no-praticante.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Testosterona no praticante de exercício", "subtitulo": "Avaliação laboratorial e decisão terapêutica",
        "nota_capa": "Entra direto no pedido do homem de 41 anos.",
        "secoes": {"pedido": ["O pedido, as duas verdades e o eixo.", "capa"],
                   "medida": ["Medir direito, frações e estradiol.", "medir"],
                   "mito": ["O pico agudo não constrói músculo.", "pico"],
                   "decisao": ["As três saídas e as seis perguntas.", "saidaA"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-04.json"), "w"), ensure_ascii=False, indent=1)
print("03-04.json:", len(S), "slides")
