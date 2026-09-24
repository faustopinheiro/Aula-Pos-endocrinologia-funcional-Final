"""Spec do deck 2.2. Gera 02-02.json ao lado deste arquivo."""
import json, math, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T = "#F3E1DE", "#DDEFEC", "#F4EAD6"

def pcr(t):
    """Curva ilustrativa de recarga depois de 30 s máximos, passando pelos pontos
    medidos por Bogdanis 1995: ~20% no fim do tiro, 65% em 90 s, 85,5% em 360 s."""
    return 20 + 34.5 * (1 - math.exp(-t / 31)) + 40.2 * (1 - math.exp(-t / 245))

# 1. a cena: duas sessões, a mesma pergunta
p = [svg_abre(1664, 400, "Duas linhas do tempo: seis tiros de 50 metros de natação e cinco séries de três repetições de levantamento, com um ponto de interrogação em cada pausa")]
rs = [rot(0, 0, "Nadador · 6 × 50 m livre", w=800, tam=30, cor=TINTA, peso=700),
      rot(0, 200, "Levantador · 5 × 3 repetições pesadas", w=900, tam=30, cor=TINTA, peso=700)]
for y, n, larg, pausa in [(56, 6, 110, 160), (256, 5, 70, 250)]:
    x = 0
    for i in range(n):
        p.append(f'<rect x="{x}" y="{y}" width="{larg}" height="84" rx="6" fill="{FOSF}"/>')
        x += larg
        if i < n - 1:
            p.append(f'<rect x="{x+10}" y="{y}" width="{pausa-20}" height="84" rx="6" fill="none" stroke="{MUDO}" stroke-width="3" stroke-dasharray="10 8"/>')
            rs.append(rot(x + 10, y + 14, "?", w=pausa - 20, tam=44, cor=MUDO, peso=700, alinha="center", serif=True))
            x += pausa
p.append("</svg>")
S.append({"id": "cena", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Dois esportes, a mesma decisão", "titulo": "A decisão mais importante está no espaço em branco",
          "destaque": "O mesmo sistema paga os dois esforços: o fosfagênico. E o que a pausa devolve define o que a sessão treina."})

# 2. a curva da recarga
pts = [(t, pcr(t)) for t in range(0, 361, 6)]
svg, rs = linhas(1664, 440, "Fosfocreatina depois de um tiro máximo de 30 segundos: parte de 20% do repouso, chega a 65% com um minuto e meio e a 85% com seis minutos",
    [{"nome": "", "cor": OXID, "pts": pts, "marcas": [(0, 20), (90, 65), (360, 85.5)]}],
    0, 360, 0, 100, [(0, "fim do tiro"), (90, "1,5 min"), (180, "3 min"), (270, "4,5 min"), (360, "6 min")], [0, 50, 100],
    margem=(90, 30, 60, 90))
rs += [rot(140, 330, "20%: quase o tanque inteiro gasto", w=500, tam=26, cor=TINTA, peso=600),
       rot(460, 150, "65% em 1,5 min", w=400, tam=34, cor=TINTA, peso=700, serif=True),
       rot(460, 196, "a fase rápida devolve quase metade", w=520, tam=26),
       rot(1180, 140, "85% em 6 min", w=400, tam=34, cor=TINTA, peso=700, serif=True),
       rot(1180, 186, "a fase lenta, só mais 20 pontos", w=420, tam=26)]
S.append({"id": "curva", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "Fosfocreatina, em % do repouso", "titulo": "A recarga tem duas velocidades",
          "destaque": "A potência do tiro seguinte acompanha de perto a fosfocreatina que voltou.",
          "fonte": "Bogdanis e colaboradores, Journal of Physiology 1995 · curva ilustrativa entre os pontos medidos"})

# 3. a oclusão
def faixa_oclusao(fx, fy):
    return (f'<rect x="{fx(0):.1f}" y="{fy(100):.1f}" width="{fx(150)-fx(0):.1f}" height="{fy(0)-fy(100):.1f}" fill="{FOSF_T}"/>'
            f'<line x1="{fx(150):.1f}" y1="{fy(100):.1f}" x2="{fx(150):.1f}" y2="{fy(0):.1f}" stroke="{FOSF}" stroke-width="3" stroke-dasharray="8 8"/>')
normal = [(t, pcr(t)) for t in range(0, 361, 6)]
ocl = [(0, 20), (150, 20)] + [(t, pcr(t - 150)) for t in range(156, 361, 6)]
svg, rs = linhas(1664, 440, "Com a circulação livre, a fosfocreatina sobe logo depois do esforço; com a circulação bloqueada, a linha fica parada em 20% e só começa a subir quando o manguito é solto",
    [{"nome": "", "cor": MUDO, "pts": normal, "tracejado": True, "esp": 4},
     {"nome": "", "cor": FOSF, "pts": ocl, "marcas": [(150, 20)]}],
    0, 360, 0, 100, [(0, "fim do esforço"), (150, "solta o manguito"), (360, "6 min")], [0, 50, 100],
    margem=(90, 30, 60, 30), extra=faixa_oclusao)
rs += [rot(110, 50, "Manguito inflado: sem fluxo", w=460, tam=28, cor=FOSF, peso=700),
       rot(110, 236, "não volta nada", w=460, tam=30, cor=TINTA, peso=700),
       rot(760, 40, "circulação livre", w=360, tam=26, cor=MUDO, peso=600),
       rot(1060, 250, "o sangue entra, a recarga começa", w=520, tam=28, cor=TINTA, peso=600)]
S.append({"id": "oclusao", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "O experimento que fecha o argumento", "titulo": "Sem fluxo, a fosfocreatina não volta",
          "destaque": "O tiro é fosfagênico. A pausa é oxidativa.", "destaque_cor": "verm",
          "fonte": "Esquema do achado de Harris, Hultman e colaboradores, Pflügers Archiv 1976"})

# 4. a encruzilhada
p = [svg_abre(1664, 440, "Bifurcação com três saídas: pausa de 30 a 60 segundos, de 2 a 3 minutos e de 4 a 5 minutos"),
     "<defs>" + seta_marker("e1", GLIC) + seta_marker("e2", TINTA) + seta_marker("e3", FOSF) + "</defs>",
     f'<circle cx="150" cy="220" r="26" fill="{TINTA}"/>']
for y, cor, m in [(70, GLIC, "e1"), (220, TINTA, "e2"), (370, FOSF, "e3")]:
    p.append(f'<path d="M176 220 C420 220 420 {y} 690 {y}" fill="none" stroke="{cor}" stroke-width="7" marker-end="url(#{m})"/>')
    p.append(f'<rect x="710" y="{y-58}" width="954" height="116" rx="14" fill="#FDFCF9" stroke="{cor}" stroke-width="4"/>')
p.append("</svg>")
rs = [rot(0, 270, "sessão de tiros curtos e máximos", w=300, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(740, 40, "30 a 60 s", w=300, tam=44, cor=TINTA, peso=700, serif=True),
      rot(1060, 48, "“no jogo ninguém dá cinco minutos”", w=580, tam=28),
      rot(740, 190, "2 a 3 min", w=300, tam=44, cor=TINTA, peso=700, serif=True),
      rot(1060, 198, "o meio-termo honesto", w=580, tam=28),
      rot(740, 340, "4 a 5 min", w=300, tam=44, cor=TINTA, peso=700, serif=True),
      rot(1060, 348, "cada tiro máximo de verdade", w=580, tam=28)]
S.append({"id": "saidas", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A encruzilhada", "titulo": "Quanto de pausa? Três saídas defensáveis",
          "destaque": "O problema de quase toda prescrição não é escolher mal. É escolher sem saber aonde a escolha vai dar."})

# 5. pausa curta: quem paga a conta a cada tiro
p = [svg_abre(1664, 440, "Esquema de seis tiros com pausa de um minuto: a parte paga pelo fosfagênico encolhe e a parte glicolítica cresce do primeiro ao sexto tiro")]
fos = [88, 66, 52, 42, 36, 32]
base, alt, larg, passo, x0 = 350, 280, 150, 210, 220
rs = []
for i, f in enumerate(fos):
    x = x0 + i * passo
    hf = alt * f / 100
    p.append(f'<rect x="{x}" y="{base-alt}" width="{larg}" height="{alt-hf-2:.1f}" rx="4" fill="{GLIC}"/>')
    p.append(f'<rect x="{x}" y="{base-hf:.1f}" width="{larg}" height="{hf:.1f}" rx="4" fill="{FOSF}"/>')
    rs.append(rot(x, base + 14, f"tiro {i+1}", w=larg, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append(f'<rect x="0" y="84" width="28" height="28" rx="4" fill="{GLIC}"/><rect x="0" y="250" width="28" height="28" rx="4" fill="{FOSF}"/>')
p.append(f'<line x1="{x0+3*passo-30}" y1="16" x2="{x0+3*passo-30}" y2="{base}" stroke="{TINTA}" stroke-width="2" stroke-dasharray="8 8"/></svg>')
rs += [rot(40, 80, "glicolítico", w=170, tam=26, cor=TINTA, peso=600),
       rot(40, 246, "fosfagênico", w=170, tam=26, cor=TINTA, peso=600),
       rot(x0 + 3 * passo - 20, 16, "a partir daqui, a conta é outra", w=520, tam=26, cor=TINTA, peso=600),
       rot(0, 400, "esquema, sem escala medida", w=400, tam=24, cor=MUDO)]
S.append({"id": "curta", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída curta · 30 a 60 s", "titulo": "Isso não é treino de velocidade",
          "destaque": "É treino de tolerância vestido de velocidade. O atleta fica ótimo em correr cansado. E não fica mais rápido.",
          "destaque_cor": "verm"})

# 6. as três sessões no relógio
p = [svg_abre(1664, 400, "Seis tiros com pausa de 1 minuto duram cerca de 6 minutos; com pausa de 2 minutos e meio, cerca de 13 minutos e meio; com pausa de 5 minutos, cerca de 26 minutos")]
esc, x0 = 0.8, 250
rs = []
for k, (pausa, nome, total, cor) in enumerate([(60, "1 min", "≈ 6 min", GLIC), (150, "2,5 min", "≈ 13,5 min", TINTA), (300, "5 min", "≈ 26 min", FOSF)]):
    y = 20 + k * 116
    x = x0
    for i in range(6):
        p.append(f'<rect x="{x:.1f}" y="{y}" width="16" height="72" rx="4" fill="{FOSF}"/>')
        x += 16
        if i < 5:
            p.append(f'<rect x="{x+2:.1f}" y="{y+24}" width="{pausa*esc-4:.1f}" height="24" rx="4" fill="{PAUSA}"/>')
            x += pausa * esc
    rs.append(rot(0, y + 14, nome, w=220, tam=40, cor=TINTA, peso=700, serif=True, alinha="right"))
    rs.append(rot(x + 24, y + 16, total, w=240, tam=34, cor=cor, peso=700))
p.append(f'<rect x="{x0}" y="372" width="16" height="28" rx="4" fill="{FOSF}"/><rect x="{x0+280}" y="380" width="40" height="14" rx="4" fill="{PAUSA}"/></svg>')
rs += [rot(x0 + 28, 366, "tiro", w=200, tam=24, cor=MUDO), rot(x0 + 332, 366, "pausa · tudo em escala de tempo", w=600, tam=24, cor=MUDO)]
S.append({"id": "relogio", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Saída média e saída longa", "titulo": "Seis tiros, três tamanhos de sessão",
          "destaque": "A pausa média não erra e não otimiza. A longa protege a qualidade, e é a mais defendida nos livros e a menos praticada no campo."})

# 7. o critério: o objeto do treino
p = [svg_abre(1664, 440, "Três objetos de treino ao longo de quatro semanas: qualidade com pausa de 4 minutos fixa; capacidade de repetir com pausa caindo de 3 para 1 minuto e meio; tolerância com pausa de 45 segundos desde o início")]
rs = []
x0, colw, esc = 420, 230, 52
for c in range(4):
    rs.append(rot(x0 + c * colw, 0, f"semana {c+1}", w=colw - 20, tam=24, cor=MUDO, alinha="left"))
linhas_ = [("Qualidade do esforço isolado", [4, 4, 4, 4], FOSF, "pausa é conteúdo"),
           ("Capacidade de repetir", [3, 2.5, 2, 1.5], AZUL, "a pausa encurta"),
           ("Tolerância", [0.75, 0.75, 0.75, 0.75], GLIC, "chama pelo nome")]
fmt = lambda v: {0.75: "45 s", 1.5: "1,5 min", 2.5: "2,5 min"}.get(v, f"{v:g} min")
for r, (nome, vals, cor, efeito) in enumerate(linhas_):
    y = 60 + r * 130
    rs.append(rot(0, y + 4, nome, w=390, tam=28, cor=TINTA, peso=700, alinha="right"))
    for c, v in enumerate(vals):
        p.append(f'<rect x="{x0 + c*colw}" y="{y}" width="{v*esc:.1f}" height="44" rx="4" fill="{cor}"/>')
        rs.append(rot(x0 + c * colw, y + 50, fmt(v), w=colw - 20, tam=24, cor=APOIO2))
    rs.append(rot(x0 + 4 * colw + 10, y + 4, efeito, w=1664 - x0 - 4 * colw - 10, tam=28, cor=cor, peso=700))
p.append("</svg>")
S.append({"id": "criterio", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O critério", "titulo": "Quem decide a pausa é o objeto do treino",
          "destaque": "Se o objeto é tolerância, a pausa curta é o instrumento certo. Só que aí se escreve “tolerância” na planilha, e não “velocidade”."})

# 8. o decremento
tempos = [4.10, 4.15, 4.22, 4.28, 4.35, 4.41]
p = [svg_abre(1664, 460, "Seis tiros de 4,10 a 4,41 segundos; as barras mostram quanto cada tiro ficou acima do melhor, de 0 a 0,31 segundo; a conta dá decremento de 3,7%")]
rs, esc = [], 1300
for i, t in enumerate(tempos):
    y = 10 + i * 72
    rs.append(rot(0, y + 4, f"Tiro {i+1}", w=120, tam=26, cor=TINTA, peso=600))
    rs.append(rot(120, y + 4, f"{t:.2f}".replace(".", ",") + " s", w=120, tam=26, cor=TINTA, alinha="right"))
    ex = t - min(tempos)
    if ex > 0:
        p.append(f'<rect x="270" y="{y+6}" width="{ex*esc:.1f}" height="40" rx="4" fill="{FOSF}"/>')
p.append(f'<line x1="268" y1="0" x2="268" y2="440" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 8"/>')
p.append(f'<rect x="840" y="0" width="824" height="440" rx="16" fill="#FDFCF9" stroke="#DDD8CC" stroke-width="2"/></svg>')
rs += [rot(284, 12, "o melhor", w=200, tam=24, cor=MUDO),
       rot(880, 30, "Soma real dos seis", w=460, tam=26), rot(1340, 22, "25,51 s", w=300, tam=38, cor=TINTA, peso=700, serif=True, alinha="right"),
       rot(880, 120, "Se todos fossem o melhor<br>6 × 4,10", w=460, tam=26), rot(1340, 128, "24,60 s", w=300, tam=38, cor=TINTA, peso=700, serif=True, alinha="right"),
       rot(880, 246, "(25,51 ÷ 24,60 − 1) × 100", w=740, tam=30, cor=TINTA),
       rot(880, 310, "Decremento", w=400, tam=30, cor=TINTA, peso=700),
       rot(1300, 290, "3,7%", w=340, tam=72, cor=FOSF, peso=700, serif=True, alinha="right")]
S.append({"id": "decremento", "tipo": "diagrama", "h": 460, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um marcador que cabe numa planilha", "titulo": "Quanto a sessão caiu em relação ao melhor tiro",
          "fonte": "Sessão de exemplo · a conta com todos os tiros é mais estável que primeiro contra último (Glaister e colaboradores, 2008)"})

# 9. ler contra a intenção
p = [svg_abre(1664, 480, "Matriz: quis qualidade e decremento baixo, sessão prescrita; quis qualidade e decremento alto, pausa curta ou volume demais; quis tolerância e decremento alto, era isso; quis tolerância e decremento quase zero, sessão confortável")]
x0, y0, cw, ch = 380, 60, 630, 180
quad = [(0, 0, OXID_T, OXID, "✓  A sessão foi a que você prescreveu"),
        (1, 0, FOSF_T, FOSF, "✗  Pausa curta ou volume demais: virou outra coisa"),
        (0, 1, FOSF_T, FOSF, "✗  Sessão confortável: não treinou o que você quis"),
        (1, 1, OXID_T, OXID, "✓  Era isso mesmo: foi aonde você queria levar")]
rs = [rot(x0, 4, "Decremento baixo", w=cw, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(x0 + cw + 24, 4, "Decremento alto", w=cw, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(0, y0 + 70, "Queria qualidade", w=350, tam=30, cor=TINTA, peso=700, alinha="right"),
      rot(0, y0 + ch + 24 + 70, "Queria tolerância", w=350, tam=30, cor=TINTA, peso=700, alinha="right")]
for c, r, fundo, borda, t in quad:
    x, y = x0 + c * (cw + 24), y0 + r * (ch + 24)
    p.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="14" fill="{fundo}" stroke="{borda}" stroke-width="3"/>')
    rs.append(rot(x + 36, y + 48, t, w=cw - 72, tam=30, cor=TINTA, peso=600))
p.append("</svg>")
S.append({"id": "matriz", "tipo": "diagrama", "h": 450, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O decremento só fala contra a intenção", "titulo": "Compare o atleta com ele mesmo",
          "destaque": "O decremento não é nota do atleta. É a prova de que a sessão que aconteceu foi a que você prescreveu."})

# 10. agenda apertada
p = [svg_abre(1664, 400, "Duas sessões de 12 minutos: quatro tiros com pausa de 4 minutos, todos fosfagênicos; sete tiros com pausa de 2 minutos, os últimos já glicolíticos")]
esc, x0 = 1.8, 300
rs = []
for k, (n, pausa, y) in enumerate([(4, 240, 30), (7, 120, 190)]):
    for i in range(n):
        x = x0 + i * pausa * esc
        cor = FOSF if (k == 0 or i < 3) else GLIC
        p.append(f'<rect x="{x:.1f}" y="{y}" width="18" height="96" rx="4" fill="{cor}"/>')
        if i < n - 1:
            p.append(f'<rect x="{x+21:.1f}" y="{y+34}" width="{pausa*esc-24:.1f}" height="28" rx="4" fill="{PAUSA}"/>')
p.append(f'<line x1="{x0}" y1="350" x2="{x0 + 720*esc + 18:.0f}" y2="350" stroke="{MUDO}" stroke-width="2"/></svg>')
rs += [rot(0, 26, "4 tiros<br>pausa de 4 min", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
       rot(0, 186, "7 tiros<br>pausa de 2 min", w=270, tam=28, cor=TINTA, peso=700, alinha="right"),
       rot(x0 + 30, 132, "treina velocidade", w=400, tam=26, cor=FOSF, peso=700),
       rot(x0 + 3*120*esc + 30, 292, "os últimos já são outra conta", w=500, tam=26, cor=GLIC, peso=700),
       rot(x0, 360, "mesmos 12 minutos no relógio", w=800, tam=24, cor=MUDO)]
S.append({"id": "agenda", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quando a agenda aperta", "titulo": "Corte tiros, não a pausa",
          "destaque": "Volume é a variável barata de cortar. Pausa é a cara.", "destaque_cor": "ambar"})

# 11. o que o VO2máx prevê
random.seed(119)
pts, alvo = [], 0.44
for _ in range(44):
    z1, z2 = random.gauss(0, 1), random.gauss(0, 1)
    pts.append((z1, alvo * z1 + math.sqrt(1 - alvo ** 2) * z2))
mx = sum(a for a, _ in pts) / len(pts); my = sum(b for _, b in pts) / len(pts)
sx = math.sqrt(sum((a - mx) ** 2 for a, _ in pts) / len(pts)); sy = math.sqrt(sum((b - my) ** 2 for _, b in pts) / len(pts))
r_obs = sum((a - mx) * (b - my) for a, b in pts) / len(pts) / sx / sy
W, H, ml, mt, pw, ph = 900, 440, 60, 50, 820, 330
fx = lambda z: ml + (z + 2.6) / 5.2 * pw
fy = lambda z: mt + ph - (z + 2.6) / 5.2 * ph
p = [svg_abre(1664, 440, f"Nuvem de pontos ilustrativa com correlação de cerca de 0,44 entre VO2máx e desempenho em tiros repetidos; ao lado, 45 estudos, 1.488 pessoas, o VO2máx explica cerca de um quinto da diferença"),
     f'<line x1="{ml}" y1="{mt+ph}" x2="{ml+pw}" y2="{mt+ph}" stroke="{MUDO}" stroke-width="2"/>',
     f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt+ph}" stroke="{MUDO}" stroke-width="2"/>']
b = r_obs * sy / sx
p.append(f'<line x1="{fx(-2.4):.1f}" y1="{fy(my + b*(-2.4-mx)):.1f}" x2="{fx(2.4):.1f}" y2="{fy(my + b*(2.4-mx)):.1f}" stroke="{TINTA}" stroke-width="3" stroke-dasharray="10 8"/>')
for a, c in pts:
    a, c = max(-2.5, min(2.5, a)), max(-2.5, min(2.5, c))
    p.append(f'<circle cx="{fx(a):.1f}" cy="{fy(c):.1f}" r="10" fill="{OXID}" fill-opacity="0.8" stroke="#F7F6F2" stroke-width="2"/>')
p.append(f'<line x1="980" y1="0" x2="980" y2="440" stroke="{GRADE}" stroke-width="2"/></svg>')
rs = [rot(ml, mt + ph + 14, "VO₂máx →", w=pw, tam=24, cor=MUDO, alinha="right"),
      rot(ml + 16, 0, "desempenho em tiros repetidos ↑", w=500, tam=24, cor=MUDO),
      rot(1030, 0, "r ≈ 0,44", w=620, tam=72, cor=TINTA, peso=700, serif=True),
      rot(1030, 104, "45 estudos · 1.488 pessoas", w=620, tam=28, cor=TINTA, peso=600),
      rot(1030, 170, "O VO₂máx explica cerca de um quinto da diferença. Os outros quatro quintos estão em outro lugar.", w=620, tam=28),
      rot(1030, 310, "A relação fica mais forte com tiros abaixo de 40 metros: quanto mais curto o tiro, mais a conta é pausa.", w=620, tam=26, cor=OXID, peso=600)]
S.append({"id": "vo2", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Uma frase que ficou fácil demais", "titulo": "Melhorar o VO₂máx não garante repetir tiros",
          "fonte": f"Ulupınar e colaboradores, Strength and Conditioning Journal 2023 · Sanders e colaboradores, 2017 · nuvem ilustrativa (r = " + f"{r_obs:.2f}".replace(".", ",") + ")"})

# 12. teto não é velocidade
rap = [(t, 100 * (1 - math.exp(-t / 18))) for t in range(0, 181, 3)]
len_ = [(t, 100 * (1 - math.exp(-t / 45))) for t in range(0, 181, 3)]
def area(fx, fy):
    ida = " ".join(f"{fx(t):.1f},{fy(v):.1f}" for t, v in rap if t <= 60)
    volta = " ".join(f"{fx(t):.1f},{fy(v):.1f}" for t, v in reversed(len_) if t <= 60)
    return (f'<polygon points="{ida} {volta}" fill="{OXID}" fill-opacity="0.18"/>'
            f'<rect x="996" y="256" width="28" height="28" rx="4" fill="{OXID}" fill-opacity="0.18" stroke="{OXID}" stroke-width="2"/>'
            f'<rect x="992" y="156" width="36" height="6" rx="3" fill="{OXID}"/><rect x="992" y="212" width="36" height="6" rx="3" fill="{AZUL}"/>')
svg, rs = linhas(1664, 440, "Duas curvas de consumo de oxigênio que chegam ao mesmo teto: uma sobe rápido e a outra devagar; no primeiro minuto de pausa, a diferença entre elas é a diferença na recarga",
    [{"nome": "", "cor": TINTA, "pts": [(0, 100), (180, 100)], "tracejado": True, "esp": 3},
     {"nome": "", "cor": OXID, "pts": rap}, {"nome": "", "cor": AZUL, "pts": len_}],
    0, 180, 0, 110, [(0, "0"), (60, "1 min"), (120, "2 min"), (180, "3 min")], [],
    margem=(40, 20, 60, 20), destaques=[{"x": 60}], extra=area)
rs += [rot(1100, 20, "o mesmo teto (VO₂máx)", w=500, tam=26, cor=TINTA, peso=600),
       rot(1040, 142, "subida rápida", w=400, tam=26, cor=TINTA, peso=600),
       rot(1040, 198, "subida lenta", w=400, tam=26, cor=TINTA, peso=600),
       rot(1040, 254, "a diferença na recarga, no primeiro minuto", w=600, tam=26, cor=TINTA, peso=600)]
S.append({"id": "cinetica", "tipo": "diagrama", "h": 440, "svg": svg, "rotulos": rs,
          "eyebrow": "Consumo de oxigênio no músculo durante a pausa", "titulo": "Teto alto não é subida rápida",
          "destaque": "Numa pausa curta, decide a velocidade com que a mitocôndria entra em regime. Melhora com mitocôndria e capilar no músculo que se usa.",
          "fonte": "Esquema ilustrativo, sem valores medidos"})

# 13. fecho
S.append({"id": "fecho", "tipo": "fecho", "titulo": "Três perguntas antes de escrever qualquer pausa",
          "regras": ["Qual é o objeto do treino hoje?", "A pausa protege esse objeto?", "O decremento confirma a sessão?"],
          "cards": [{"t": "Preparador e treinador", "x": "Prescrevem a pausa e leem o decremento de cada sessão."},
                    {"t": "Médico e fisioterapeuta", "x": "Lesão que se repete no fim da sessão? Pedem a planilha de intervalos. Para entender, não para mudar."}],
          "quem": "Pausa é conteúdo."})

spec = {"arquivo": "aulas/MOD02/02-02-sistema-fosfagenico-e-a-decisao-do-intervalo.md", "modulo": "Fisiologia do Exercício Aplicada",
        "titulo": "Pausa é conteúdo", "subtitulo": "O sistema fosfagênico e a decisão do intervalo",
        "nota_capa": "Entra pela cena do nadador e do levantador.",
        "secoes": {"recarga": ["A curva da recarga e o experimento da oclusão.", "capa"],
                   "decisao": ["As três saídas e o critério do objeto do treino.", "saidas"],
                   "leitura": ["Decremento, agenda apertada e o que o VO₂máx prevê.", "decremento"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "02-02.json"), "w"), ensure_ascii=False, indent=1)
print("02-02.json:", len(S), "slides · r nuvem =", round(r_obs, 2))
