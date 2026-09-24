"""Spec do deck 3.2. Gera 03-02.json ao lado deste arquivo."""
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

# 1. o vilão
S.append({"id": "vilao", "tipo": "frase", "fundo": "tinta", "eyebrow": "O hormônio mais caluniado",
          "frase": "Se o cortisol é o problema, baixar o cortisol é a solução.",
          "apoio": "Engorda, destrói músculo, causa barriga, derruba a imunidade, acaba com o sono. Essa conduta parece prudente e está errada. Sem cortisol, não se vive: insuficiência adrenal não tratada é fatal."})

# 2. origem da calúnia
p = [svg_abre(1664, 360, "Síndrome de Cushing e corticoide em dose farmacológica, com concentração alta sustentada por meses, levam por extrapolação indevida ao praticante que treina e dorme mal"),
     "<defs>" + seta_marker("b1", MUDO) + "</defs>",
     caixa(0, 20, 620, 140, FOSF, FOSF_T, esp=3), caixa(0, 200, 620, 140, FOSF, FOSF_T, esp=3),
     caixa(1044, 110, 620, 140, OXID, OXID_T, esp=3),
     f'<path d="M640 90 C 820 90, 860 180, 1030 180" fill="none" stroke="{MUDO}" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#b1)"/>',
     f'<path d="M640 270 C 820 270, 860 180, 1030 180" fill="none" stroke="{MUDO}" stroke-width="5" stroke-dasharray="14 10"/>',
     f'<line x1="810" y1="130" x2="880" y2="230" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>',
     f'<line x1="880" y1="130" x2="810" y2="230" stroke="{FOSF}" stroke-width="8" stroke-linecap="round"/>',
     "</svg>"]
rs = [rot(30, 44, "Síndrome de Cushing", w=560, tam=32, cor=FOSF, peso=700),
      rot(30, 96, "concentração alta, sustentada, por meses", w=560, tam=26, cor=TINTA),
      rot(30, 224, "Corticoide em dose farmacológica", w=560, tam=32, cor=FOSF, peso=700),
      rot(30, 276, "concentração alta, sustentada, por meses", w=560, tam=26, cor=TINTA),
      rot(1074, 134, "Quem treina e dorme mal", w=560, tam=32, cor=OXID, peso=700),
      rot(1074, 186, "variação fisiológica, que sobe e volta", w=560, tam=26, cor=TINTA),
      rot(640, 300, "extrapolar de dano para vida normal", w=400, tam=24, cor=FOSF, peso=600, alinha="center")]
S.append({"id": "origem", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "De onde vem a fama", "titulo": "Dois contextos de dano, emprestados à vida normal",
          "destaque": "Custo nas duas direções: medo de treinar forte, e um mercado para baixar o que está funcionando.",
          "destaque_cor": "verm"})

# 3. funções
S.append({"id": "funcao", "tipo": "cards", "eyebrow": "Para que ele existe", "titulo": "Deixar energia disponível agora",
          "cards": [{"t": "Glicose", "x": "mais glicose disponível no sangue", "cor": "ambar"},
                    {"t": "Substrato", "x": "gordura e aminoácido mobilizados do tecido", "cor": "ambar"},
                    {"t": "Inflamação", "x": "contida, para não consumir recursos demais", "cor": "petr"},
                    {"t": "Tônus vascular", "x": "a pressão não cai quando você precisa correr", "cor": "tinta"}],
          "destaque": "Catabólico porque músculo é reserva, e em emergência reserva vira combustível. Acionado o dia inteiro: mais sinal catabólico e menos permissão para reparar.",
          "destaque_cor": "verm"})

# 4. ritmo
def curva(m, extras=()):
    h = m / 60
    base = 6 + 14 * math.exp(-((h - 1.5) / 3.2) ** 2) + 6 * math.exp(-((h - 0.6) / 0.5) ** 2) - 3 * (h / 24)
    for c, a in extras:
        base += a * math.exp(-((h - c) / 0.7) ** 2)
    return base
ok = [(m, curva(m, [(3, 7), (11, 8)])) for m in range(0, 24 * 60 + 1, 10)]
ruim = [(m, curva(m, [(3, 7), (7, 7), (11, 8), (14, 8)]) + (5 if m > 13 * 60 else 5 * max(0, (m - 8 * 60) / 300) if m > 8 * 60 else 0)) for m in range(0, 24 * 60 + 1, 10)]
svg, rs = linhas(1664, 400, "Curva de 24 horas do cortisol, do despertar à noite. Com o ritmo preservado, os picos de treino sobem e voltam e a noite tem vale. Com estímulos empilhados, o cortisol não volta ao basal e a noite fica sem vale",
                 [{"nome": "", "cor": OXID, "pts": ok}, {"nome": "", "cor": FOSF, "pts": ruim, "tracejado": True}],
                 0, 1440, 0, 34, [(0, "despertar"), (360, "+6 h"), (720, "+12 h"), (1080, "+18 h"), (1440, "+24 h")], [],
                 margem=(20, 20, 60, 20))
rs += [rot(120, 0, "resposta ao despertar", w=400, tam=26, cor=TINTA, peso=600),
       rot(1180, 200, "ritmo preservado: a noite tem vale", w=480, tam=26, cor=OXID, peso=700),
       rot(1080, 60, "estímulos empilhados: não volta", w=560, tam=26, cor=FOSF, peso=700)]
S.append({"id": "ritmo", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "A leitura certa", "titulo": "Alto quando deve, baixo quando deve",
          "destaque": "O problema não é a amplitude. É não voltar ao basal entre um estímulo e o seguinte.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos"})

# 5. Hill 2008
vals = [("Repouso", -6.6, MUDO), ("40% do VO₂máx", 5.7, OXID), ("60%", 39.9, GLIC), ("80%", 83.1, FOSF)]
p = [svg_abre(1664, 400, "Variação do cortisol em 30 minutos: repouso menos 6,6%, 40% do VO2máx mais 5,7%, 60% mais 39,9%, 80% mais 83,1%")]
Y0, ESC = 300, 3.0
p.append(f'<line x1="0" y1="{Y0}" x2="1664" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
rs = []
for i, (nome, v, cor) in enumerate(vals):
    x = 120 + i * 400
    h = v * ESC
    y = Y0 - h if v > 0 else Y0
    p.append(f'<rect x="{x}" y="{y:.0f}" width="200" height="{abs(h):.0f}" rx="4" fill="{cor}"/>')
    sinal = "+" if v > 0 else "−"
    txt = f"{sinal}{abs(v):.1f}%".replace(".", ",")
    if v > 0:
        rs.append(rot(x - 50, Y0 - h - 50, txt, w=300, tam=38, cor=TINTA, peso=700, alinha="center", serif=True))
    else:
        rs.append(rot(x - 60, Y0 - 56, txt, w=320, tam=38, cor=TINTA, peso=700, alinha="center", serif=True))
    rs.append(rot(x - 80, 356, nome, w=360, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append("</svg>")
S.append({"id": "limiar", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Hill e colaboradores, 2008", "titulo": "Exercício acima de um certo ponto sobe cortisol",
          "destaque": "Corrigido para a redução do volume plasmático e o ritmo do dia, o esforço leve baixou o cortisol.",
          "destaque_cor": "petr", "fonte": "Journal of Endocrinological Investigation 2008 · 12 homens moderadamente treinados, 30 min, dias separados · variação sem correção"})

# 6. três cuidados
S.append({"id": "cuidados", "tipo": "lista", "eyebrow": "Como usar o dado sem exagerar", "titulo": "O que importa é a volta, não o pico",
          "itens": [{"t": "Subir no exercício é a resposta certa", "x": "treino que não sobe cortisol não é objetivo de saúde", "cor": "petr"},
                    {"t": "Sessenta por cento é princípio, não régua", "x": "doze homens, num desenho controlado", "cor": "ambar"},
                    {"t": "Volta ao basal antes do próximo estímulo?", "x": "a intervenção: parte do volume abaixo do limiar. Não tira nada da pessoa", "cor": "verm"}],
          "destaque": "Jejum soma. Pico da manhã, jejum e sessão dura na mesma janela, em quem já acorda acionado, é débito empilhado.",
          "destaque_cor": "ambar"})

# 7. curva de quatro pontos
p = [svg_abre(1664, 300, "Régua de reprodutibilidade de um dia para o outro, de 0 a 0,75 conforme a parte da curva: a resposta ao despertar fica na ponta de baixo; a área sob a curva, na de cima")]
p.append(f'<rect x="0" y="120" width="1664" height="40" rx="20" fill="{CLARO}" stroke="{BORDA}" stroke-width="2"/>')
p.append(f'<rect x="0" y="120" width="{1664*0.75:.0f}" height="40" rx="20" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(0, 60, "0", w=100, tam=28, cor=TINTA, peso=700),
      rot(1664 * 0.75 - 100, 60, "0,75", w=200, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(1564, 60, "1", w=100, tam=28, cor=MUDO, alinha="right"),
      rot(0, 190, "na ponta de baixo: a resposta ao despertar", w=620, tam=26, cor=FOSF, peso=700),
      rot(1664 * 0.75 - 640, 190, "na de cima: a área sob a curva, para estudos grandes", w=640, tam=26, cor=OXID, peso=700, alinha="right"),
      rot(0, 0, "Reprodutibilidade de um dia para o outro", w=1000, tam=28, cor=TINTA, peso=700)]
S.append({"id": "curva4", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A curva de quatro pontos", "titulo": "A foto de um dia, não o padrão",
          "destaque": "Para suspeita de excesso, as diretrizes usam outros testes: cortisol livre na urina de 24 horas, cortisol salivar no fim da noite ou supressão com 1 mg de dexametasona.",
          "destaque_cor": "tinta", "fonte": "Norton e colaboradores, Comprehensive Psychoneuroendocrinology 2023 · Nieman e colaboradores, Endocrine Society 2008"})

# 8. quando investigar
S.append({"id": "investigar", "tipo": "duas", "eyebrow": "Quando investigar de verdade", "titulo": "Os dois extremos que existem",
          "esq": {"t": "Excesso", "cor": "ambar",
                  "itens": ["fraqueza proximal: levantar da cadeira sem os braços", "estrias violáceas largas",
                            "hipertensão de difícil controle, glicose fora de proporção", "pele frágil, fratura sem trauma"]},
          "dir": {"t": "Insuficiência: urgência", "cor": "verm",
                  "itens": ["pressão baixa, fraqueza progressiva", "escurecimento de pele e mucosas",
                            "vontade intensa de sal, náusea", "perda de peso sem intenção, sódio baixo"]},
          "destaque": "Cansaço e gordura abdominal, sozinhos, não abrem investigação. E são os dois que trazem a pessoa pedindo o exame.",
          "destaque_cor": "tinta"})

# 9. fadiga adrenal
S.append({"id": "fadiga", "tipo": "numeros", "eyebrow": "Cadegiani e Kater, 2016", "titulo": "“Fadiga adrenal” não existe; os sintomas, sim",
          "numeros": [{"n": "3.470", "x": "artigos triados na revisão sistemática", "cor": "tinta"},
                      {"n": "58", "x": "estudos analisados de perto, sem base para a entidade", "cor": "verm"}],
          "destaque": "O rótulo fecha a investigação cedo: sono curto, apneia, pouca energia disponível, ferro, tireoide, medicamento, depressão. Custa os meses em que o diagnóstico certo não foi procurado.",
          "destaque_cor": "verm", "fonte": "BMC Endocrine Disorders 2016"})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que fazer no lugar", "titulo": "Quantas vezes o eixo é acionado, e ele volta?",
          "regras": ["Sessões acima do limiar por semana, horário delas, despertares noturnos",
                     "Distribuir as duras, tirar uma da manhã, volume abaixo do limiar, comer antes",
                     "Em 6 a 8 semanas: sono, despertares, esforço na mesma sessão, disposição de 0 a 10"],
          "cards": [{"t": "Médico", "x": "Investiga excesso e insuficiência."},
                    {"t": "Educador físico e preparador", "x": "Reorganizam a semana, com o nutricionista no jejum."}],
          "quem": "Não prescreva nada para baixar cortisol num eixo que responde certo a um contexto que ninguém mudou."})

spec = {"arquivo": "aulas/MOD03/03-02-hpa-e-cortisol-no-exercicio.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Eixo hipotálamo-hipófise-adrenal e exercício", "subtitulo": "Cortisol, avaliação e equívocos frequentes",
        "nota_capa": "Entra direto no vilão.",
        "secoes": {"erro": ["O erro e de onde ele vem.", "capa"],
                   "fisiologia": ["Função, ritmo e a resposta ao exercício.", "funcao"],
                   "exames": ["A curva de quatro pontos e quando investigar.", "curva4"],
                   "lugar": ["Fadiga adrenal e o que fazer no lugar.", "fadiga"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-02.json"), "w"), ensure_ascii=False, indent=1)
print("03-02.json:", len(S), "slides")
