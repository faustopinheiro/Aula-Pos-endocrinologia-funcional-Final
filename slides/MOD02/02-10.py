"""Spec do deck 2.10. Gera 02-10.json ao lado deste arquivo."""
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

# 1. dois endereços
p = [svg_abre(1664, 420, "O caminho do comando, do córtex à fibra muscular, cortado na junção neuromuscular: antes dela, fadiga central; depois dela, fadiga periférica"),
     "<defs>" + seta_marker("c1", TINTA) + "</defs>",
     f'<rect x="0" y="60" width="930" height="300" rx="18" fill="{AZUL_T}"/>',
     f'<rect x="950" y="60" width="714" height="300" rx="18" fill="{FOSF_T}"/>',
     f'<circle cx="150" cy="210" r="80" fill="{AZUL}"/>',
     f'<path d="M230 210 C 380 210, 420 210, 560 210 L 890 210" fill="none" stroke="{TINTA}" stroke-width="8"/>',
     f'<circle cx="905" cy="210" r="18" fill="{TINTA}"/>',
     f'<line x1="940" y1="30" x2="940" y2="390" stroke="{TINTA}" stroke-width="4" stroke-dasharray="14 10"/>',
     f'<rect x="1000" y="150" width="600" height="120" rx="60" fill="{FOSF}"/>']
p.append(f'<path d="' + " ".join(f"M{x} 160 v100" for x in range(1060, 1560, 40)) + f'" stroke="{FOSF_T}" stroke-width="6" stroke-opacity="0.6"/>')
p.append("</svg>")
rs = [rot(20, 0, "Fadiga central", w=900, tam=32, cor=AZUL, peso=700),
      rot(960, 0, "Fadiga periférica", w=700, tam=32, cor=FOSF, peso=700),
      rot(90, 190, "córtex", w=120, tam=26, cor=CLARO, peso=700, alinha="center"),
      rot(300, 150, "comando descendo pelo nervo", w=520, tam=26, cor=TINTA, alinha="center"),
      rot(740, 240, "junção", w=180, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(20, 300, "o músculo poderia, e o comando não vem", w=900, tam=28, cor=AZUL, peso=600),
      rot(1000, 90, "fibra", w=600, tam=26, cor=TINTA, peso=700, alinha="center"),
      rot(970, 300, "o comando chega, e o músculo não consegue", w=690, tam=28, cor=FOSF, peso=600)]
S.append({"id": "enderecos", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Terceiro set: “cansei”", "titulo": "Fadiga tem dois endereços",
          "destaque": "Fadiga é a queda induzida pelo exercício na capacidade de produzir força. Não é a sensação de cansaço: é a queda medida.",
          "destaque_cor": "tinta"})

# 2. duas faces
t = [x for x in range(0, 61, 2)]
des = [(m, 100 - 10 * (m / 60) ** 1.2) for m in t]
per = [(m, 100 - (10 * (m / 60) ** 1.2 if m <= 30 else 10 * (m / 60) ** 1.2 + 1.1 * (m - 30))) for m in t]
def faixa(fx, fy):
    return f'<rect x="{fx(30):.0f}" y="{fy(100):.0f}" width="{fx(60)-fx(30):.0f}" height="{fy(60)-fy(100):.0f}" fill="{GLIC_T}"/>'
svg, rs = linhas(1664, 400, "Ao longo da sessão, o desempenho medido e a disposição percebida caem juntos no começo; depois a percepção piora muito mais do que a medida",
    [{"nome": "", "cor": FOSF, "pts": des}, {"nome": "", "cor": AZUL, "pts": per, "tracejado": True}],
    0, 60, 60, 102, [(0, "início"), (30, "meio"), (60, "fim da sessão")], [], margem=(40, 20, 60, 360), extra=faixa)
rs += [rot(1320, 40, "desempenho medido", w=340, tam=30, cor=FOSF, peso=700),
       rot(1320, 290, "disposição percebida", w=340, tam=30, cor=AZUL, peso=700),
       rot(760, 20, "aqui elas se descolam", w=400, tam=28, cor=GLIC, peso=700)]
S.append({"id": "faces", "tipo": "diagrama", "h": 400, "svg": svg, "rotulos": rs,
          "eyebrow": "A segunda distinção", "titulo": "A queda medida e a queda sentida",
          "destaque": "Dá para cair na medida sem reclamar, e para sentir um esforço enorme com queda pequena.",
          "destaque_cor": "ambar", "fonte": "Esquema, sem valores medidos · Enoka e Duchateau 2016 · Behrens e colaboradores, Sports Medicine 2023"})

# 3. interpolação do abalo
p = [svg_abre(1664, 440, "Contração voluntária máxima com estímulo no nervo: antes do exercício o estímulo não acrescenta força; depois, aparece um degrau extra e o platô é mais baixo. O abalo do músculo relaxado também fica menor depois"),
     f'<line x1="0" y1="250" x2="1664" y2="250" stroke="{MUDO}" stroke-width="2"/>',
     f'<line x1="0" y1="420" x2="1664" y2="420" stroke="{MUDO}" stroke-width="2"/>',
     f'<line x1="832" y1="0" x2="832" y2="440" stroke="{GRADE}" stroke-width="3"/>']
def contracao(x0, topo, degrau, cor):
    return (f'<path d="M{x0} 250 C {x0+60} 250, {x0+80} {topo}, {x0+140} {topo} L {x0+300} {topo} '
            f'L {x0+310} {topo-degrau} L {x0+330} {topo-degrau} L {x0+340} {topo} L {x0+500} {topo} '
            f'C {x0+560} {topo}, {x0+580} 250, {x0+640} 250" fill="none" stroke="{cor}" stroke-width="6" stroke-linejoin="round"/>')
def abalo(x0, alt, cor):
    return f'<path d="M{x0} 420 C {x0+40} 420, {x0+50} {420-alt}, {x0+80} {420-alt} C {x0+120} {420-alt}, {x0+140} 420, {x0+220} 420" fill="none" stroke="{cor}" stroke-width="6"/>'
p += [contracao(80, 70, 4, OXID), contracao(930, 120, 40, AZUL), abalo(300, 110, OXID), abalo(1150, 60, FOSF)]
p.append("</svg>")
rs = [rot(0, 0, "Antes do exercício", w=800, tam=30, cor=TINTA, peso=700),
      rot(850, 0, "Depois do exercício", w=800, tam=30, cor=TINTA, peso=700),
      rot(160, 110, "estímulo no nervo: nada a mais", w=480, tam=26, cor=OXID, peso=600, alinha="center"),
      rot(1290, 50, "degrau extra: comando que faltava", w=370, tam=26, cor=AZUL, peso=700),
      rot(0, 330, "músculo relaxado:", w=280, tam=26, cor=MUDO),
      rot(540, 330, "abalo cheio", w=280, tam=26, cor=OXID, peso=600),
      rot(1390, 350, "abalo menor: periférica", w=270, tam=26, cor=FOSF, peso=700)]
S.append({"id": "interpolacao", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O método de laboratório", "titulo": "Interpolação do abalo",
          "fonte": "Esquema, sem valores medidos · Gandevia, Physiological Reviews 2001"})

# 4. campo
p = [svg_abre(1664, 400, "Quatro medidas de campo: salto vertical, velocidade da barra em carga conhecida e decremento nos tiros medem o desempenho; a percepção de esforço mede o lado percebido")]
cores = [FOSF, FOSF, FOSF, AZUL]
for i in range(4):
    x = i * 424
    p.append(caixa(x, 80, 392, 300, cores[i], FOSF_T if i < 3 else AZUL_T, esp=3))
# brackets
p.append(f'<path d="M10 60 V40 H1250 V60" fill="none" stroke="{FOSF}" stroke-width="4"/>')
p.append(f'<path d="M1282 60 V40 H1654 V60" fill="none" stroke="{AZUL}" stroke-width="4"/>')
# glifos
p.append(f'<path d="M110 300 Q 196 120 282 300" fill="none" stroke="{FOSF}" stroke-width="8" stroke-dasharray="14 10"/>')
p.append(f'<rect x="470" y="226" width="300" height="12" rx="6" fill="{TINTA}"/><rect x="490" y="196" width="24" height="72" rx="4" fill="{FOSF}"/><rect x="726" y="196" width="24" height="72" rx="4" fill="{FOSF}"/>')
for j, hgt in enumerate([120, 112, 100, 86, 72]):
    p.append(f'<rect x="{900 + j*56}" y="{300-hgt}" width="40" height="{hgt}" rx="4" fill="{FOSF}"/>')
p.append(f'<rect x="1320" y="236" width="316" height="28" rx="14" fill="{CLARO}" stroke="{AZUL}" stroke-width="3"/><rect x="1320" y="236" width="220" height="28" rx="14" fill="{AZUL}"/>')
p.append("</svg>")
rs = [rot(10, 0, "desempenho", w=1240, tam=26, cor=FOSF, peso=700, alinha="center"),
      rot(1282, 0, "percebida", w=372, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(0, 100, "Salto vertical", w=392, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(424, 100, "Velocidade da barra", w=392, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(848, 100, "Decremento", w=392, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(1272, 100, "Percepção de esforço", w=392, tam=30, cor=TINTA, peso=700, alinha="center"),
      rot(0, 320, "a média dos saltos, não o melhor", w=392, tam=24, cor=TINTA, alinha="center"),
      rot(424, 320, "mesma carga, barra mais lenta", w=392, tam=24, cor=TINTA, alinha="center"),
      rot(848, 320, "nos tiros repetidos", w=392, tam=24, cor=TINTA, alinha="center"),
      rot(1272, 320, "a única que não custa nada", w=392, tam=24, cor=TINTA, alinha="center")]
S.append({"id": "campo", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Na beira da quadra", "titulo": "Quatro medidas, dois eixos",
          "destaque": "Medida e percepção caem juntas: quadro coerente. A percepção dispara e a medida quase não cai: olhe o lado central, e o que aconteceu fora do treino.",
          "destaque_cor": "petr", "fonte": "Claudino e colaboradores, Journal of Science and Medicine in Sport 2017 · 151 estudos"})

# 5. dentro da fibra
p = [svg_abre(1664, 470, "Dentro da fibra: o fosfato inorgânico sobe de cerca de 5 para perto de 30 milimolares, o retículo libera menos cálcio, o glicogênio perto do retículo se esvazia primeiro e o potássio sai pela membrana"),
     "<defs>" + seta_marker("d1", GLIC) + seta_marker("d2", AZUL) + "</defs>",
     f'<rect x="0" y="40" width="1100" height="380" rx="40" fill="{FOSF_T}" stroke="{FOSF}" stroke-width="4"/>',
     f'<path d="' + " ".join(f"M{x} 150 v160" for x in range(80, 1040, 60)) + f'" stroke="{FOSF}" stroke-width="10" stroke-opacity="0.35"/>',
     f'<rect x="40" y="110" width="1020" height="24" rx="12" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>',
     f'<rect x="40" y="326" width="1020" height="24" rx="12" fill="{AZUL_T}" stroke="{AZUL}" stroke-width="3"/>']
gpath = []
for k, x in enumerate(range(90, 1040, 80)):
    gpath.append(f"M{x} 96 a10 10 0 1 0 0.1 0")
p.append(f'<path d="{" ".join(gpath)}" fill="none" stroke="{GLIC}" stroke-width="4"/>')
p.append(f'<path d="{" ".join(f"M{x} 372 a10 10 0 1 0 0.1 0" for x in range(90, 1040, 80))}" fill="{GLIC}"/>')
p.append(seta(560, 350, 560, 290, AZUL, "d2", esp=4))
p.append(seta(1100, 230, 1180, 230, GLIC, "d1", esp=6))
p.append(f'<rect x="1230" y="60" width="80" height="360" rx="8" fill="{CLARO}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<rect x="1230" y="{420-360*30/34:.0f}" width="80" height="{360*30/34:.0f}" rx="8" fill="{FOSF}"/>')
p.append(f'<line x1="1220" y1="{420-360*5/34:.0f}" x2="1320" y2="{420-360*5/34:.0f}" stroke="{TINTA}" stroke-width="4" stroke-dasharray="8 6"/>')
p.append("</svg>")
rs = [rot(40, 0, "retículo sarcoplasmático: menos cálcio liberado", w=1000, tam=26, cor=AZUL, peso=700),
      rot(40, 60, "glicogênio perto do retículo: vazio", w=700, tam=24, cor=GLIC, peso=700),
      rot(40, 430, "glicogênio longe do retículo: ainda cheio", w=700, tam=24, cor=GLIC, peso=700),
      rot(590, 290, "cálcio", w=200, tam=26, cor=AZUL, peso=700),
      rot(1110, 180, "K⁺", w=100, tam=30, cor=GLIC, peso=700),
      rot(1330, 60, "fosfato inorgânico", w=330, tam=28, cor=FOSF, peso=700),
      rot(1330, 110, "~30 mM no esforço intenso", w=330, tam=26, cor=TINTA),
      rot(1330, 350, "~5 mM em repouso", w=330, tam=26, cor=TINTA)]
S.append({"id": "fibra", "tipo": "diagrama", "h": 470, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Fadiga periférica", "titulo": "Onde a conta é paga dentro da fibra",
          "destaque": "Assinatura: não responde a incentivo, tem curso de tempo próprio, desconforto local intenso.",
          "destaque_cor": "verm", "fonte": "Allen, Lamb e Westerblad, Physiological Reviews 2008 · Ørtenblad, Westerblad e Nielsen, Journal of Physiology 2013 · desenho esquemático"})

# 6. freio central, Amann
p = [svg_abre(1664, 420, "O músculo avisa o sistema nervoso por fibras finas e o comando desce reduzido. Com esse aviso bloqueado, o tempo até a exaustão caiu de 8,7 para 6,8 minutos e a fadiga periférica se instalou 67% mais rápido"),
     "<defs>" + seta_marker("e1", AZUL) + seta_marker("e2", TINTA) + "</defs>",
     f'<circle cx="220" cy="80" r="70" fill="{AZUL}"/>',
     f'<rect x="120" y="300" width="200" height="100" rx="40" fill="{FOSF}"/>',
     f'<path d="M300 300 C 380 220, 380 150, 290 110" fill="none" stroke="{AZUL}" stroke-width="4" marker-end="url(#e1)"/>',
     f'<path d="M175 152 C 135 200, 140 250, 180 292" fill="none" stroke="{TINTA}" stroke-width="14" marker-end="url(#e2)"/>',
     f'<line x1="620" y1="0" x2="620" y2="420" stroke="{GRADE}" stroke-width="3"/>',
     f'<line x1="900" y1="60" x2="900" y2="345" stroke="{MUDO}" stroke-width="2"/>']
esc = 70
for i, (v, cor) in enumerate([(8.7, OXID), (6.8, FOSF)]):
    p.append(f'<rect x="902" y="{90 + i*140}" width="{v*esc:.0f}" height="90" rx="4" fill="{cor}"/>')
p.append("</svg>")
rs = [rot(160, 60, "cérebro", w=120, tam=24, cor=CLARO, peso=700, alinha="center"),
      rot(120, 334, "músculo", w=200, tam=26, cor=CLARO, peso=700, alinha="center"),
      rot(390, 180, "o aviso sobe", w=220, tam=26, cor=AZUL, peso=700),
      rot(0, 200, "comando", w=130, tam=24, cor=TINTA, peso=700),
      rot(660, 116, "aviso preservado", w=230, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(660, 256, "aviso bloqueado", w=230, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(902 + 8.7 * esc + 20, 110, "8,7 min", w=200, tam=38, cor=TINTA, peso=700, serif=True),
      rot(902 + 6.8 * esc + 20, 250, "6,8 min", w=200, tam=38, cor=TINTA, peso=700, serif=True),
      rot(660, 20, "Tempo até a exaustão, ciclistas", w=1000, tam=28, cor=TINTA, peso=700),
      rot(660, 370, "e fadiga periférica 67% mais rápida", w=1000, tam=28, cor=FOSF, peso=700)]
S.append({"id": "freio", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Fadiga central", "titulo": "Sem o freio, o atleta foi menos longe",
          "destaque": "A fadiga central não é fraqueza: é proteção com custo. O freio é fisiologia, não caráter.",
          "destaque_cor": "petr", "fonte": "Amann e colaboradores, Journal of Physiology 2011 · bloqueio intratecal contra placebo"})

# 7. fadiga mental, Marcora
p = [svg_abre(1664, 360, "Depois de 90 minutos de documentário, 754 segundos até a exaustão; depois de 90 minutos de tarefa mental exigente, 640 segundos. Frequência cardíaca, lactato e consumo de oxigênio iguais nas duas condições"),
     f'<line x1="460" y1="0" x2="460" y2="250" stroke="{MUDO}" stroke-width="2"/>']
esc = 1.25
for i, (v, cor) in enumerate([(754, OXID), (640, AZUL)]):
    p.append(f'<rect x="462" y="{20 + i*115}" width="{v*esc:.0f}" height="90" rx="4" fill="{cor}"/>')
for i, t_ in enumerate(["frequência cardíaca", "lactato", "consumo de oxigênio"]):
    p.append(f'<rect x="{462 + i*400}" y="280" width="380" height="70" rx="35" fill="{OXID_T}" stroke="{OXID}" stroke-width="3"/>')
p.append("</svg>")
rs = [rot(0, 36, "90 min de documentário", w=430, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(0, 151, "90 min de tarefa mental", w=430, tam=28, cor=TINTA, peso=700, alinha="right"),
      rot(462 + 754 * esc + 20, 30, "754 s", w=200, tam=40, cor=TINTA, peso=700, serif=True),
      rot(462 + 640 * esc + 20, 145, "640 s", w=200, tam=40, cor=TINTA, peso=700, serif=True),
      rot(0, 296, "iguais nas duas:", w=430, tam=28, cor=OXID, peso=700, alinha="right")]
for i, t_ in enumerate(["frequência cardíaca", "lactato", "consumo de oxigênio"]):
    rs.append(rot(462 + i * 400, 297, t_, w=380, tam=26, cor=TINTA, peso=600, alinha="center"))
S.append({"id": "mental", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O que acontece fora do treino entra na conta", "titulo": "O corpo igual, a conta subjetiva não",
          "destaque": "Honestidade: análises que corrigem viés de publicação sugerem que o efeito existe, mas é menor do que os primeiros estudos fizeram parecer.",
          "destaque_cor": "ambar", "fonte": "Marcora, Staiano e Manning, Journal of Applied Physiology 2009 · 16 pessoas, 80% da potência de pico · Holgado e colaboradores, Sports Medicine 2023"})

# 8. roteiro
p = [svg_abre(1664, 440, "Três perguntas em ordem: a queda é objetiva ou só percebida; responde a estímulo externo; tem duração de fadiga de treino"),
     "<defs>" + seta_marker("f1", MUDO) + "</defs>"]
perg = [("1", "A queda é objetiva ou só percebida?", "só a sensação subiu: olhe fora do treino", AZUL),
        ("2", "Responde a estímulo externo?", "sim: havia reserva, lado central · não: periferia", FOSF),
        ("3", "Tem duração de fadiga de treino?", "semanas ou meses: outro assunto", GLIC)]
rs = []
for i, (n, q, r, cor) in enumerate(perg):
    y = i * 150
    p.append(f'<circle cx="50" cy="{y+60}" r="46" fill="{cor}"/>')
    p.append(caixa(120, y, 700, 120, cor, CARTAO, esp=3))
    p.append(seta(830, y + 60, 920, y + 60, MUDO, "f1", esp=4))
    p.append(f'<rect x="930" y="{y}" width="734" height="120" rx="14" fill="{CLARO}" stroke="{BORDA}" stroke-width="2"/>')
    rs += [rot(10, y + 36, n, w=80, tam=38, cor=CLARO, peso=700, alinha="center", serif=True),
           rot(150, y + 38, q, w=660, tam=30, cor=TINTA, peso=700),
           rot(960, y + 24, r, w=680, tam=28, cor=TINTA, lh=1.3)]
p.append("</svg>")
S.append({"id": "roteiro", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O roteiro para a segunda-feira", "titulo": "Três perguntas, em ordem"})

# 9. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Minutos a dias, ou semanas a meses?",
          "regras": ["Minutos a dias: fadiga de treino, resolve com recuperação",
                     "Semanas a meses: outro assunto, não atribua ao treino por reflexo"],
          "cards": [{"t": "Preparador e educador físico", "x": "Medem a fadiga neuromuscular em campo e ajustam a sessão."},
                    {"t": "Todo mundo", "x": "Reconhece quando a fadiga saiu da escala do treino. É a porta da investigação clínica."}],
          "quem": "Sono curto, apneia, pouca energia disponível, ferro, tireoide, medicamentos, infecção, depressão: todos produzem o mesmo relato."})

spec = {"arquivo": "aulas/MOD02/02-10-fadiga-central-e-fadiga-periferica.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Fadiga no exercício", "subtitulo": "Mecanismos centrais e periféricos",
        "nota_capa": "Entra pela cena do terceiro set.",
        "secoes": {"definir": ["O que é fadiga e as duas distinções.", "capa"],
                   "medir": ["Como separar central de periférico, no laboratório e no campo.", "interpolacao"],
                   "mecanismos": ["Dentro da fibra, o freio central e a vida fora do treino.", "fibra"],
                   "roteiro": ["As três perguntas e o limite da aula.", "roteiro"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-10.json"), "w"), ensure_ascii=False, indent=1)
print("02-10.json:", len(S), "slides")
