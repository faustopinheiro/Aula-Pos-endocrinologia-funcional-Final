"""Spec do deck 12.6. Gera 12-06.json ao lado deste arquivo."""
from _base import *

S = []


def xis(cx, cy, r, cor):
    """Círculo com um X: marca de afirmação errada."""
    d = r * 0.45
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{cor}"/>'
            f'<path d="M {cx - d} {cy - d} L {cx + d} {cy + d} M {cx + d} {cy - d} L {cx - d} {cy + d}" stroke="{PAPEL}" stroke-width="6" stroke-linecap="round"/>')


def ondas(x, y, w, cor, n=3):
    return "".join(f'<path d="M {x} {y + k * 26} ' + " ".join(f"q 30 -16 60 0 t 60 0" for _ in range(w // 120)) + f'" stroke="{cor}" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(n))


# 1. o mito
p = [svg_abre(1664, 440, "Nadadora de 12 anos na borda da piscina. Quatro frases marcadas como erradas: musculação atrofia o crescimento; peso fecha a placa de crescimento; criança só pode fazer o peso do corpo; antes da puberdade não adianta, não tem hormônio")]
rs = []
p.append(icone("h:woman", 60, 20, 280, AZUL))
p.append(ondas(20, 312, 480, AZUL))
rs.append(rot(0, 400, "12 anos · seis treinos na piscina", w=520, tam=24, cor=AZUL, peso=700, alinha="center"))
for j, t in enumerate(["“musculação atrofia o crescimento”", "“peso fecha a placa de crescimento”", "“criança só pode fazer o peso do corpo”", "“antes da puberdade não adianta”"]):
    y = j * 112
    p.append(caixa(640, y, 1024, 92, FOSF, FOSF_T, esp=2, rx=16))
    p.append(xis(690, y + 46, 26, FOSF))
    rs.append(rot(740, y + 26, t, w=900, tam=28, cor=TINTA, peso=700, serif=True))
diagrama(S, "mito", 440, p, rs, eyebrow="Uma nadadora de 12 anos fica fora da sessão de força", titulo="Quatro frases sobre força na criança, e as quatro erradas")

# 2. as raízes
p = [svg_abre(1664, 440, "Três raízes do mito. Trabalho infantil pesado, com desnutrição: não é treino supervisionado. Relatos de lesão com carga máxima sem supervisão: risco de fazer errado. Pouco hormônio, logo sem ganho: confunde força com tamanho"), defs(OXID)]
rs = []
p.append(caixa(632, 0, 400, 80, TINTA, TINTA, esp=0, rx=40))
rs.append(rot(652, 20, "o mito", w=360, tam=30, cor=PAPEL, peso=700, alinha="center", serif=True))
for k, (raiz, corr) in enumerate([("trabalho infantil pesado, com desnutrição", "não é treino supervisionado"),
                                  ("lesão com carga máxima, sem supervisão", "é o risco de fazer errado"),
                                  ("pouco hormônio, logo sem ganho", "confunde força com tamanho")]):
    x = k * 564
    p.append(f'<path d="M 832 80 C 832 120 {x + 268} 110 {x + 268} 150" stroke="{GLIC}" stroke-width="6" fill="none"/>')
    p.append(caixa(x, 150, 536, 140, GLIC, GLIC_T, esp=3, rx=16))
    rs.append(rot(x + 20, 176, raiz, w=496, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.25))
    p.append(seta(x + 268, 296, x + 268, 336, OXID, "m0", 4))
    p.append(caixa(x, 344, 536, 96, OXID, OXID_T, esp=3, rx=16))
    rs.append(rot(x + 20, 374, corr, w=496, tam=26, cor=OXID, peso=700, alinha="center"))
diagrama(S, "raiz", 440, p, rs, eyebrow="De onde veio", titulo="O mito tem três raízes, e cada uma tem resposta")

# 3. os dados de lesão
p = [svg_abre(1664, 440, "Levantamento escolar britânico de 1994: 1.634 alunos, 168.551 horas de treino, 3 lesões, a menor taxa entre os esportes escolares levantados. Estudo de 2009 em prontos-socorros: nos mais jovens, a maior parte das lesões foi acidente com mãos e pés ao soltar ou manusear o peso, evitável com supervisão"), defs(FOSF)]
rs = []
p.append(caixa(0, 0, 800, 330, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(24, 18, "Escolas britânicas, 1994", w=752, tam=28, cor=OXID, peso=700, serif=True))
for j, (n, t) in enumerate([("1.634", "alunos"), ("168.551", "horas"), ("3", "lesões")]):
    x = 24 + j * 254
    rs += [rot(x, 90, n, w=240, tam=48, cor=TINTA, peso=700, alinha="center", serif=True), rot(x, 160, t, w=240, tam=24, cor=MUDO, peso=600, alinha="center")]
rs.append(rot(24, 236, "taxa menor que a de todos os esportes escolares do levantamento", w=752, tam=24, cor=OXID, peso=700, alinha="center", lh=1.25))
p.append(caixa(864, 0, 800, 330, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(888, 18, "Prontos-socorros, 2009", w=752, tam=28, cor=FOSF, peso=700, serif=True))
p += [f'<rect x="930" y="150" width="300" height="12" rx="6" fill="{TINTA}"/>',
      f'<rect x="930" y="112" width="26" height="88" rx="6" fill="{TINTA}"/>', f'<rect x="1204" y="112" width="26" height="88" rx="6" fill="{TINTA}"/>',
      seta(1080, 210, 1080, 270, FOSF, "m0", 5),
      f'<rect x="1000" y="276" width="160" height="16" rx="8" fill="{FOSF}"/>']
rs += [rot(1270, 92, "nos mais jovens: acidente com mãos e pés ao soltar ou manusear o peso", w=370, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1270, 236, "evitável com supervisão", w=370, tam=24, cor=FOSF, peso=700)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "O risco está no ambiente sem supervisão, não no músculo nem na placa de crescimento", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "lesao", 440, p, rs, eyebrow="O que os dados de lesão mostram", titulo="Com instrução, o treino de força lesiona pouco",
         fonte="J Strength Cond Res 1994; J Strength Cond Res 2009")

# 4. o consenso
p = [svg_abre(1664, 440, "Documento de consenso internacional de 2014 com selos de várias entidades. Quatro afirmações: seguro e eficaz se bem desenhado e supervisionado; sem evidência de prejuízo ao crescimento; benefício além da força; o critério é a maturidade para seguir instruções, não a idade")]
rs = []
p += [f'<rect x="40" y="0" width="300" height="400" rx="12" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>']
for j in range(6):
    p.append(f'<rect x="80" y="{110 + j * 34}" width="{220 - (j % 3) * 40}" height="12" rx="6" fill="{GRADE}"/>')
for k, c in enumerate([OXID, AZUL, GLIC]):
    p.append(f'<circle cx="{110 + k * 80}" cy="350" r="30" fill="{c}"/>')
rs.append(rot(60, 24, "Consenso internacional, 2014", w=260, tam=24, cor=TINTA, peso=700, alinha="center", serif=True, lh=1.2))
for j, (t, c) in enumerate([("seguro e eficaz, se bem desenhado e supervisionado", OXID), ("sem evidência de prejuízo ao crescimento ou à estatura final", OXID),
                            ("benefício além da força: motor, ósseo, composição corporal, menos lesão", AZUL), ("o critério é a maturidade para seguir instruções, não a idade", GLIC)]):
    y = j * 112
    p.append(caixa(420, y, 1244, 96, c, CARTAO, esp=3, rx=16))
    p.append(icone("t:check", 444, y + 28, 40, c))
    rs.append(rot(500, y + 30, t, w=1140, tam=26, cor=TINTA, peso=700))
diagrama(S, "consenso", 440, p, rs, eyebrow="O que o consenso estabelece", titulo="Seguro, eficaz e sem prejuízo ao crescimento",
         fonte="Br J Sports Med 2014; J Strength Cond Res 2009")

# 5. ganho neural
p = [svg_abre(1664, 440, "Esquema ao longo da adolescência. Força subindo desde cedo; tamanho do músculo quase parado até o pico de crescimento e subindo depois. Antes do pico: ganho neural; depois: a hipertrofia entra. Massa óssea subindo até o início da vida adulta")]
rs = []
x0, x1, base = 80, 1100, 400
p.append(f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
p.append(f'<line x1="{x0}" y1="20" x2="{x0}" y2="{base}" stroke="{TINTA}" stroke-width="3"/>')
pico = 620
p.append(f'<line x1="{pico}" y1="20" x2="{pico}" y2="{base}" stroke="{MUDO}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(f'<path d="M {x0} 340 C 300 300 480 250 {pico} 210 S 950 80 {x1} 50" stroke="{OXID}" stroke-width="7" fill="none"/>')
p.append(f'<path d="M {x0} 370 C 300 368 480 362 {pico} 350 S 950 200 {x1} 150" stroke="{GLIC}" stroke-width="7" fill="none"/>')
p.append(f'<path d="M {x0} 380 C 400 330 700 200 900 130 S 1050 110 {x1} 110" stroke="{AZUL}" stroke-width="5" fill="none" stroke-dasharray="14 8"/>')
rs += [rot(pico - 160, 0, "pico de crescimento", w=320, tam=22, cor=MUDO, peso=600, alinha="center"),
       rot(200, 244, "força", w=200, tam=26, cor=OXID, peso=700),
       rot(700, 368, "tamanho do músculo", w=300, tam=24, cor=GLIC, peso=700),
       rot(860, 196, "massa óssea", w=200, tam=24, cor=AZUL, peso=700),
       rot(x0 + 10, 410, "idade", w=200, tam=22, cor=MUDO),
       rot(x0 + 10, 30, "esquema", w=200, tam=22, cor=MUDO)]
p.append(caixa(1260, 0, 404, 190, OXID, OXID_T, esp=3, rx=16))
rs.append(rot(1280, 20, "Antes do pico: ganho neural. Mais forte sem ficar maior.", w=364, tam=26, cor=TINTA, peso=700, lh=1.3))
p.append(caixa(1260, 220, 404, 190, GLIC, GLIC_T, esp=3, rx=16))
rs.append(rot(1280, 240, "Depois do pico: a hipertrofia entra e a carga pode subir mais.", w=364, tam=26, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "neural", 440, p, rs, eyebrow="Como a criança ganha força", titulo="Antes da puberdade, a força cresce sem o músculo crescer")

# 6. o custo do erro
p = [svg_abre(1664, 440, "Balança com dois pratos. Sem treino de força: mais volume na água, a mesma braçada repetida, osso sem impacto. Com treino de força: padrões básicos, carga no osso, ombro e tronco mais fortes. A balança pesa para o segundo")]
rs = []
p += [f'<path d="M 832 90 L 800 400 L 864 400 Z" fill="{TINTA}"/>',
      f'<line x1="300" y1="40" x2="1364" y2="140" stroke="{TINTA}" stroke-width="10" stroke-linecap="round"/>',
      f'<line x1="300" y1="40" x2="300" y2="90" stroke="{TINTA}" stroke-width="4"/>',
      f'<line x1="1364" y1="140" x2="1364" y2="190" stroke="{TINTA}" stroke-width="4"/>']
for k, (t, itens, c, f, y) in enumerate([("Sem treino de força", ["mais volume na água", "a mesma braçada, milhares de vezes", "osso quase sem impacto"], FOSF, FOSF_T, 90),
                                         ("Com treino de força", ["agachar, empurrar, puxar, aterrissar", "carga no osso em construção", "ombro e tronco mais fortes"], OXID, OXID_T, 190)]):
    x = 60 if k == 0 else 1124
    p.append(caixa(x, y, 480, 250, c, f, esp=3, rx=18))
    rs.append(rot(x + 20, y + 16, t, w=440, tam=28, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 20, y + 80 + j * 52, "· " + it, w=440, tam=24, cor=TINTA, peso=600))
diagrama(S, "custo", 440, p, rs, eyebrow="O custo do erro, na natação", titulo="Quem fica sem força fica com mais repetição e menos osso")

# 7. a prescrição
p = [svg_abre(1664, 440, "Ficha de sessão infantil: 2 a 3 vezes por semana em dias não seguidos; 20 a 40 minutos; 1 a 3 séries de 6 a 15 repetições; progressão de 5% a 10% depois da técnica. Seis padrões: agachar, dobrar o quadril, empurrar, puxar, carregar, tronco. Técnica antes de carga"), defs(OXID)]
rs = []
for j, (a, b) in enumerate([("frequência", "2 a 3 por semana, dias não seguidos"), ("duração", "20 a 40 minutos"),
                            ("séries", "1 a 3 de 6 a 15 repetições"), ("progressão", "5% a 10%, quando a técnica está estável")]):
    y = j * 80
    p.append(caixa(0, y, 900, 68, GRADE, CARTAO, esp=2, rx=12))
    rs += [rot(20, y + 18, a, w=200, tam=24, cor=MUDO, peso=700), rot(230, y + 18, b, w=650, tam=26, cor=TINTA, peso=700)]
for j, t in enumerate(["agachar", "dobrar o quadril", "empurrar", "puxar", "carregar", "tronco"]):
    x, y = 980 + (j % 2) * 342, (j // 2) * 80
    p.append(caixa(x, y, 322, 64, AZUL, AZUL_T, esp=2, rx=32))
    rs.append(rot(x + 10, y + 16, t, w=302, tam=26, cor=AZUL, peso=700, alinha="center"))
p.append(caixa(0, 350, 400, 90, OXID, OXID, esp=0, rx=18))
rs.append(rot(20, 374, "técnica", w=360, tam=30, cor=PAPEL, peso=700, alinha="center"))
p.append(seta(410, 395, 500, 395, OXID, "m0", 6))
p.append(caixa(510, 350, 400, 90, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(530, 374, "carga", w=360, tam=30, cor=OXID, peso=700, alinha="center"))
p.append(caixa(980, 270, 684, 170, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(1000, 290, "Supervisão qualificada, maturação de cada um e formato de jogo: adesão é o que dá resultado.", w=644, tam=24, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "prescricao", 440, p, rs, eyebrow="Como prescrever", titulo="Poucos padrões, técnica primeiro e carga depois",
         fonte="J Strength Cond Res 2009; Br J Sports Med 2014")

# 8. o que evitar
p = [svg_abre(1664, 440, "Quatro coisas a evitar: teste de carga máxima sem técnica; falha como rotina; programa de adulto em miniatura; força somada a um volume já excessivo. A frase para a família: a recomendação mudou")]
rs = []
for k, t in enumerate(["teste de carga máxima sem técnica", "treinar até a falha como rotina", "programa de adulto em miniatura", "força somada a um volume já excessivo"]):
    x = k * 420
    p.append(caixa(x, 0, 400, 230, FOSF, FOSF_T, esp=3, rx=18))
    p.append(icone("t:alert-triangle", x + 160, 24, 80, FOSF))
    rs.append(rot(x + 20, 124, t, w=360, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.25))
p.append(caixa(0, 270, 1664, 170, OXID, OXID_T, esp=3, rx=18))
p.append(icone("t:users", 30, 310, 90, OXID))
rs += [rot(150, 290, "Para a família", w=1480, tam=26, cor=OXID, peso=700),
       rot(150, 336, "“Essa recomendação era comum há alguns anos. A informação mudou, e hoje pediatria e medicina do esporte endossam o treino de força supervisionado.”", w=1480, tam=26, cor=TINTA, serif=True, lh=1.3)]
diagrama(S, "evitar", 440, p, rs, eyebrow="O que evitar", titulo="A força entra dentro da carga total, não por cima dela")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Treinamento de força no jovem", "titulo": "Força supervisionada é parte do esporte da criança",
          "regras": ["Bem desenhado e supervisionado, é seguro e não prejudica o crescimento",
                     "Antes da puberdade, o ganho é neural: mais forte sem ficar maior",
                     "Sem treino de força, sobra mais repetição do mesmo gesto e menos osso"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina", "x": "Ensina técnica antes de carga, supervisiona e encaixa a força no volume total."},
                    {"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Desfazem o mito com a família e liberam sem exigir idade mínima."},
                    {"ic": "t:users", "t": "A família", "x": "Entende que força é parte do esporte, não um risco a mais."}]})

salvar("12-06.json", {"arquivo": "aulas/MOD12/12-06-treinamento-de-forca-no-jovem.md",
                      "titulo": "Treinamento de força no jovem", "subtitulo": "O mito que atrasou a força na criança",
                      "nota_capa": "Entra por uma nadadora de doze anos que ficou fora da sessão de força do clube.",
                      "secoes": {"mito": ["O erro e suas raízes.", "capa"], "lesao": ["O que os dados mostram.", "lesao"],
                                 "custo": ["O custo do erro.", "custo"], "prescricao": ["Como prescrever.", "prescricao"]},
                      "slides": S})
