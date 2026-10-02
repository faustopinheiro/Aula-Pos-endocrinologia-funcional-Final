"""Spec do deck 12.5. Gera 12-05.json ao lado deste arquivo."""
from _base import *

S = []
OSSO = "#D9D4C7"


def corpo(cor):
    """Silhueta de frente, 300 x 440, canto superior esquerdo em (120, 0)."""
    return "".join([
        f'<circle cx="270" cy="32" r="30" fill="{cor}"/>',
        f'<rect x="220" y="70" width="100" height="150" rx="22" fill="{cor}"/>',
        f'<path d="M 214 84 L 176 230" stroke="{cor}" stroke-width="26" stroke-linecap="round"/>',
        f'<path d="M 326 84 L 364 230" stroke="{cor}" stroke-width="26" stroke-linecap="round"/>',
        f'<rect x="218" y="206" width="104" height="48" rx="16" fill="{cor}"/>',
        f'<rect x="226" y="240" width="38" height="186" rx="16" fill="{cor}"/>',
        f'<rect x="276" y="240" width="38" height="186" rx="16" fill="{cor}"/>',
        f'<rect x="206" y="414" width="58" height="22" rx="10" fill="{cor}"/>',
        f'<rect x="276" y="414" width="58" height="22" rx="10" fill="{cor}"/>'])


def ponto(x, y, cor):
    return f'<circle cx="{x}" cy="{y}" r="13" fill="{cor}" stroke="{PAPEL}" stroke-width="4"/>'


# 1. o ombro do ponteiro
p = [svg_abre(1664, 440, "Ponteiro de vôlei de 13 anos no momento da cortada, ombro direito marcado. Linha do tempo de cinco meses de dor, com dois tratamentos de tendinite do manguito, cada um com melhora parcial e volta da dor ao voltar ao treino"), defs(TINTA)]
rs = []
p += [f'<circle cx="200" cy="70" r="34" fill="{AZUL}"/>', f'<rect x="160" y="112" width="80" height="150" rx="22" fill="{AZUL}"/>',
      f'<path d="M 232 124 L 300 30" stroke="{AZUL}" stroke-width="24" stroke-linecap="round"/>',
      f'<path d="M 168 128 L 120 220" stroke="{AZUL}" stroke-width="24" stroke-linecap="round"/>',
      f'<rect x="166" y="250" width="30" height="120" rx="14" fill="{AZUL}"/>', f'<rect x="204" y="250" width="30" height="120" rx="14" fill="{AZUL}"/>',
      f'<circle cx="320" cy="10" r="24" fill="{GLIC}"/>',
      f'<circle cx="234" cy="124" r="30" fill="none" stroke="{FOSF}" stroke-width="6"/>']
rs.append(rot(40, 400, "13 anos · ponteiro", w=330, tam=26, cor=AZUL, peso=700, alinha="center"))
p.append(f'<rect x="440" y="40" width="1224" height="20" rx="10" fill="{FOSF_T}"/>')
for m in range(6):
    p.append(f'<line x1="{440 + m * 244.8:.0f}" y1="30" x2="{440 + m * 244.8:.0f}" y2="70" stroke="{FOSF}" stroke-width="3"/>')
rs.append(rot(440, 80, "cinco meses de dor no ombro direito", w=1224, tam=24, cor=FOSF, peso=700, alinha="center"))
for k in range(2):
    x = 480 + k * 600
    p.append(caixa(x, 140, 540, 110, TINTA, CARTAO, esp=2, rx=14))
    rs += [rot(x + 20, 156, f"tratamento {k + 1}", w=500, tam=22, cor=MUDO, peso=600),
           rot(x + 20, 192, "“tendinite do manguito”", w=500, tam=28, cor=TINTA, peso=700, serif=True)]
    p.append(seta(x + 270, 256, x + 270, 300, TINTA, "m0", 3))
    rs.append(rot(x, 310, "melhora em parte, volta a doer", w=540, tam=24, cor=FOSF, peso=700, alinha="center"))
p.append(caixa(480, 370, 1140, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(500, 388, "Manguito rotador é diagnóstico de adulto", w=1100, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "ombro", 440, p, rs, eyebrow="Um ponteiro de vôlei de 13 anos", titulo="Dois tratamentos para um diagnóstico de adulto")

# 2. as duas estruturas
p = [svg_abre(1664, 440, "Osso longo de criança com a fise, placa de crescimento, atravessando a extremidade, e uma apófise na inserção de um tendão. Ao lado, o mesmo trauma: no adulto cede o ligamento ou o tendão; na criança, a fise ou a apófise")]
rs = []
p += [f'<path d="M 120 40 Q 220 -10 320 40 L 320 110 L 120 110 Z" fill="{OSSO}"/>',
      f'<rect x="120" y="110" width="200" height="26" fill="{GLIC}"/>',
      f'<path d="M 120 136 L 320 136 L 290 200 L 290 440 L 150 440 L 150 200 Z" fill="{OSSO}"/>',
      f'<circle cx="300" cy="210" r="26" fill="{OXID}"/>',
      f'<path d="M 320 214 C 400 222 460 262 520 330" stroke="{OXID}" stroke-width="16" fill="none" stroke-linecap="round"/>']
rs += [rot(340, 96, "fise: o osso cresce aqui", w=300, tam=24, cor=GLIC, peso=700),
       rot(340, 140, "apófise: onde o tendão se prende", w=320, tam=24, cor=OXID, peso=700, lh=1.2),
       rot(120, 400, "esquema", w=160, tam=22, cor=MUDO)]
for k, (t, l1, l2, c, f) in enumerate([("Adulto", "trauma em valgo: rompe o ligamento", "tração repetida: tendão", TINTA, CARTAO),
                                       ("Criança", "trauma em valgo: lesa a fise", "tração repetida: apófise", FOSF, FOSF_T)]):
    y = k * 230
    p.append(caixa(700, y, 964, 210, c, f, esp=3, rx=18))
    rs += [rot(724, y + 18, t, w=916, tam=30, cor=c, peso=700, serif=True),
           rot(724, y + 80, l1, w=916, tam=28, cor=TINTA, peso=600), rot(724, y + 136, l2, w=916, tam=28, cor=TINTA, peso=600)]
diagrama(S, "elo", 440, p, rs, eyebrow="O que o adulto não tem", titulo="Na criança, o elo mais fraco é a cartilagem de crescimento")

# 3. passo 1
p = [svg_abre(1664, 440, "Passo 1, filtro: isto é do esporte? Seis sinais que tiram o caso do esporte: dor noturna que acorda, febre, perda de peso ou mal-estar, dor sem relação com a atividade, deformidade, incapacidade de usar o membro. Saída: avaliação médica urgente"), defs(FOSF, OXID)]
rs = []
p.append('<path d="M 0 0 L 360 0 L 230 170 L 230 300 L 130 340 L 130 170 Z" fill="' + FOSF_T + '" stroke="' + FOSF + '" stroke-width="4"/>')
rs.append(rot(20, 40, "isto é do esporte?", w=320, tam=30, cor=FOSF, peso=700, alinha="center", serif=True))
for i, t in enumerate(["dor noturna que acorda", "febre", "perda de peso, mal-estar", "dor sem relação com o treino", "deformidade", "não consegue usar o membro"]):
    x, y = 410 + (i % 2) * 412, (i // 2) * 96
    p.append(caixa(x, y, 400, 80, FOSF, CARTAO, esp=3, rx=40))
    rs.append(rot(x + 12, y + 22, t, w=376, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(seta(1226, 136, 1292, 136, FOSF, "m0", 5))
p.append(caixa(1300, 60, 364, 150, FOSF, FOSF, esp=0, rx=18))
rs.append(rot(1316, 92, "avaliação médica urgente", w=332, tam=28, cor=PAPEL, peso=700, alinha="center", lh=1.2))
p.append(caixa(420, 330, 1244, 110, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(444, 350, "Sem nenhum deles, padrão mecânico: piora com a carga, melhora com a pausa. Daí em diante, raciocínio esportivo.", w=1196, tam=26, cor=TINTA, peso=600, lh=1.3))
p.append(seta(180, 350, 400, 386, OXID, "m1", 4))
diagrama(S, "alarmes", 440, p, rs, eyebrow="Passo 1", titulo="Primeiro, tirar o que não é do esporte")

# 4. passo 2: endereços
p = [svg_abre(1664, 450, "Passo 2: silhueta de adolescente com endereços em três cores. Apófises: tuberosidade da tíbia, polo inferior da patela, calcâneo, crista ilíaca, tuberosidade isquiática, epicôndilo medial. Fises por estresse: rádio distal, úmero proximal. Osso: tíbia, metatarsos, colo do fêmur, vértebra lombar"), corpo(GRADE)]
rs = []
for x, y in [(245, 330), (295, 300), (245, 432), (222, 212), (300, 252), (190, 160)]:
    p.append(ponto(x, y, OXID))
for x, y in [(364, 222), (322, 88)]:
    p.append(ponto(x, y, GLIC))
for x, y in [(295, 380), (320, 432), (250, 248), (270, 196)]:
    p.append(ponto(x, y, FOSF))
for k, (t, itens, c) in enumerate([("Apófises", ["tuberosidade da tíbia", "polo inferior da patela", "calcâneo", "crista ilíaca", "tuberosidade isquiática", "epicôndilo medial"], OXID),
                                   ("Fises por estresse", ["rádio distal (apoio nas mãos)", "úmero proximal (arremesso, saque)"], GLIC),
                                   ("Osso", ["tíbia, metatarsos", "colo do fêmur: alto risco", "vértebra lombar"], FOSF)]):
    x = 500 + [0, 400, 400][k]
    y0 = [0, 0, 200][k]
    p.append(f'<circle cx="{x + 12}" cy="{y0 + 22}" r="12" fill="{c}"/>')
    rs.append(rot(x + 34, y0 + 4, t, w=360, tam=28, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 34, y0 + 56 + j * 44, it, w=360 if k == 0 else 730, tam=24, cor=TINTA, peso=600))
diagrama(S, "endereco", 450, p, rs, eyebrow="Passo 2", titulo="Palpar o endereço: no jovem, o lugar exato decide")

# 5. passo 3: trauma
p = [svg_abre(1664, 450, "Passo 3, trauma agudo: cinco desenhos de traço de fratura através da fise, tipos I a V. Tipos I e V: radiografia pode vir normal. Tipo II: o mais comum. Conduta: parar, imobilizar, avaliar no mesmo dia; não fazer teste de estresse vigoroso")]
rs = []
tracos = ["M 10 70 L 190 70",
          "M 10 70 L 120 70 L 170 150",
          "M 10 70 L 110 70 L 110 0",
          "M 110 0 L 110 150",
          ""]
for k, d in enumerate(tracos):
    x = k * 300
    p += [f'<g transform="translate({x},20)">',
          f'<path d="M 10 60 L 10 20 Q 100 -14 190 20 L 190 60 Z" fill="{OSSO}"/>',
          f'<rect x="10" y="{60 if k < 4 else 64}" width="180" height="{20 if k < 4 else 10}" fill="{GLIC}"/>',
          f'<path d="M 10 80 L 190 80 L 170 170 L 30 170 Z" fill="{OSSO}"/>']
    if d:
        p.append(f'<path d="{d}" stroke="{FOSF}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        p.append(f'<path d="M 60 -4 L 60 40 M 140 -4 L 140 40" stroke="{FOSF}" stroke-width="6" stroke-linecap="round"/>')
    p.append('</g>')
    rs.append(rot(x, 200, ["I", "II", "III", "IV", "V"][k], w=200, tam=30, cor=TINTA, peso=700, alinha="center", serif=True))
rs += [rot(0, 244, "radiografia pode vir normal", w=200, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2),
       rot(300, 244, "o mais comum", w=200, tam=22, cor=TINTA, peso=700, alinha="center"),
       rot(1200, 244, "radiografia pode vir normal", w=200, tam=22, cor=FOSF, peso=700, alinha="center", lh=1.2)]
for j, t in enumerate(["parar", "imobilizar", "avaliar no mesmo dia"]):
    x = j * 330
    p.append(caixa(x, 340, 310, 80, OXID, OXID_T, esp=3, rx=40))
    rs.append(rot(x + 10, 362, t, w=290, tam=26, cor=OXID, peso=700, alinha="center"))
p.append(caixa(1020, 340, 644, 80, FOSF, FOSF_T, esp=3, rx=40))
rs.append(rot(1040, 362, "não: teste de estresse vigoroso", w=604, tam=26, cor=FOSF, peso=700, alinha="center"))
diagrama(S, "trauma", 450, p, rs, eyebrow="Passo 3, se houve trauma", titulo="Depois de trauma, pensar em fise antes de entorse",
         fonte="J Bone Joint Surg Am 1963")

# 6. passo 4: imagem
p = [svg_abre(1664, 440, "Passo 4: duas radiografias esquemáticas de ombro. Lado sem dor: fise do úmero fina e regular. Lado da dor: fise alargada e irregular. Compare com o outro lado; ressonância se a suspeita persiste; na apofisite, diagnóstico clínico; radiografia normal com clínica sugestiva não libera")]
rs = []
for k, (t, larga) in enumerate([("lado sem dor", False), ("lado da dor", True)]):
    x = k * 420
    p.append(f'<rect x="{x}" y="0" width="390" height="380" rx="16" fill="{TINTA}"/>')
    p.append(f'<circle cx="{x + 200}" cy="110" r="90" fill="{OSSO}"/>')
    p.append(f'<rect x="{x + 140}" y="150" width="120" height="230" fill="{OSSO}"/>')
    if larga:
        p.append(f'<path d="M {x + 104} 140 L {x + 140} 128 L {x + 170} 150 L {x + 200} 130 L {x + 232} 152 L {x + 262} 132 L {x + 298} 146 L {x + 298} 170 L {x + 262} 158 L {x + 232} 178 L {x + 200} 156 L {x + 170} 176 L {x + 140} 154 L {x + 104} 166 Z" fill="{TINTA}"/>')
    else:
        p.append(f'<path d="M {x + 108} 146 Q {x + 200} 128 {x + 292} 146" stroke="{TINTA}" stroke-width="6" fill="none"/>')
    rs.append(rot(x, 392, t, w=390, tam=26, cor=FOSF if larga else TINTA, peso=700, alinha="center"))
rs.append(rot(0, 330, "esquema", w=380, tam=22, cor=PAPEL, alinha="right"))
for j, (t, c, f) in enumerate([("Compare com o lado que não dói", OXID, OXID_T), ("Ressonância se a suspeita persiste", AZUL, AZUL_T),
                               ("Apofisite: diagnóstico clínico", GLIC, GLIC_T), ("Radiografia normal com clínica sugestiva não libera", FOSF, FOSF_T)]):
    y = j * 112
    p.append(caixa(900, y, 764, 96, c, f, esp=3, rx=16))
    rs.append(rot(924, y + 30, t, w=716, tam=26, cor=c if j != 2 else TINTA, peso=700, lh=1.2))
diagrama(S, "imagem", 440, p, rs, eyebrow="Passo 4", titulo="Na imagem, a diferença entre os dois lados é o achado")

# 7. a lombar
p = [svg_abre(1664, 440, "Coluna lombar de perfil com a parte posterior de L5 destacada. Estudo de 1995 com dor lombar: lesão por estresse dessa região em 47% dos jovens atletas e em 5% dos adultos. Padrão: dor que piora na extensão, muitas vezes de um lado, arrastada; o teste de extensão em uma perna não decide")]
rs = []
for i in range(5):
    y = i * 80
    p.append(f'<rect x="40" y="{y}" width="150" height="62" rx="10" fill="{OSSO}"/>')
    p.append(f'<path d="M 190 {y + 20} L 250 {y + 30} L 290 {y + 10} L 300 {y + 50} L 250 {y + 52} L 190 {y + 44} Z" fill="{OSSO}"/>')
    rs.append(rot(70, y + 14, f"L{i + 1}", w=90, tam=24, cor=TINTA, peso=700, alinha="center"))
p.append(f'<circle cx="228" cy="{4 * 80 + 40}" r="22" fill="none" stroke="{FOSF}" stroke-width="6"/>')
for k, (t, v, c) in enumerate([("jovens atletas", 47, FOSF), ("adultos", 5, MUDO)]):
    x = 420 + k * 220
    p.append(f'<rect x="{x}" y="{400 - v * 7}" width="150" height="{v * 7}" rx="8" fill="{c}"/>')
    rs += [rot(x - 25, 404, t, w=200, tam=22, cor=TINTA, peso=700, alinha="center"),
           rot(x - 25, 400 - v * 7 - 44, f"{v}%", w=200, tam=32, cor=c, peso=700, alinha="center", serif=True)]
p.append(caixa(900, 0, 764, 440, AZUL, AZUL_T, esp=3, rx=18))
rs.append(rot(924, 18, "O padrão que pede investigação", w=716, tam=28, cor=AZUL, peso=700, serif=True))
for j, t in enumerate(["piora na extensão", "muitas vezes de um lado", "arrastada por semanas", "esporte de extensão repetida"]):
    rs.append(rot(924, 86 + j * 52, "· " + t, w=716, tam=26, cor=TINTA, peso=600))
rs.append(rot(924, 316, "O teste de extensão numa perna só não confirma nem afasta.", w=716, tam=24, cor=FOSF, peso=700, lh=1.3))
diagrama(S, "lombar", 440, p, rs, eyebrow="Dor lombar com espondilólise, estudo de 1995", titulo="No jovem que estende a coluna, a dor lombar tem causa",
         fonte="Arch Pediatr Adolesc Med 1995; Br J Sports Med 2006")

# 8. a conduta
p = [svg_abre(1664, 440, "Conduta em cinco blocos: tira o gesto, não o esporte; conta o gesto; corrige o que é corrigível; explica o prazo; acompanha o crescimento. Nota: na apofisite do calcâneo, nove artigos numa revisão de 2013")]
rs = []
for k, (ic, t, x_t, c, f) in enumerate([("t:run", "Tira o gesto", "não o esporte", OXID, OXID_T), ("t:stopwatch", "Conta o gesto", "por sessão e por semana", GLIC, GLIC_T),
                                         ("t:check", "Corrige", "tornozelo, calçado, força, técnica", AZUL, AZUL_T), ("t:calendar", "Explica o prazo", "até a apófise se fundir", TINTA, CARTAO),
                                         ("t:zoom-question", "Acompanha", "comprimento e desvio, meses depois", FOSF, FOSF_T)]):
    x = k * 336
    p.append(caixa(x, 0, 316, 300, c, f, esp=3, rx=18))
    p.append(icone(ic, x + 118, 24, 80, c))
    rs += [rot(x + 14, 124, t, w=288, tam=28, cor=c, peso=700, alinha="center"), rot(x + 14, 180, x_t, w=288, tam=24, cor=TINTA, peso=600, alinha="center", lh=1.25)]
p.append(caixa(0, 330, 1664, 110, MUDO, CARTAO, esp=2, rx=16))
rs.append(rot(24, 350, "Evidência pequena: na apofisite do calcâneo, nove artigos numa revisão de 2013. Anti-inflamatório contínuo esconde o sinal; infiltração não tem lugar.", w=1616, tam=24, cor=TINTA, peso=600, lh=1.3))
diagrama(S, "conduta", 440, p, rs, eyebrow="A conduta, para fise e apófise", titulo="Tira o gesto, mantém o atleta no grupo e conta",
         fonte="J Foot Ankle Res 2013")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Lesões do esqueleto imaturo", "titulo": "Dor localizada em quem cresce e treina tem endereço",
          "regras": ["Na criança, o elo mais fraco é a cartilagem de crescimento; “dor do crescimento” não fecha diagnóstico",
                     "Tirar o que não é do esporte, palpar o endereço, pensar em fise após trauma, comparar os lados",
                     "A conduta tira o gesto, não o esporte, e conta o gesto"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina", "x": "Conta os gestos de risco, legitima a queixa de dor e mantém o atleta no grupo."},
                    {"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Palpam o endereço, pedem a imagem certa e escrevem a hipótese."},
                    {"ic": "t:users", "t": "A família", "x": "Sabe o prazo e sabe que dor que acorda à noite é urgente."}]})

salvar("12-05.json", {"arquivo": "aulas/MOD12/12-05-lesoes-do-esqueleto-imaturo.md",
                      "titulo": "Lesões do esqueleto imaturo", "subtitulo": "Quatro passos para a dor localizada no jovem atleta",
                      "nota_capa": "Entra por um ponteiro de vôlei de treze anos tratado duas vezes por tendinite do manguito.",
                      "secoes": {"ombro": ["O caso e as estruturas.", "capa"], "alarmes": ["Os quatro passos.", "alarmes"],
                                 "lombar": ["A lombar.", "lombar"], "conduta": ["A conduta.", "conduta"]},
                      "slides": S})
