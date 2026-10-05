"""Spec do deck 14.6. Gera 14-06.json ao lado deste arquivo."""
from _base import *

S = []

SEIS = ["a pergunta", "o que se sabia, com números", "as opções consideradas", "o que foi decidido, e por quem",
        "o que foi dito e combinado com a atleta", "quando e como reavaliar"]

def ficha(x, y, w, h, cor, fundo=CARTAO):
    return (caixa(x, y, w, h, cor, fundo, esp=3, rx=10)
            + f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="10" fill="{cor}"/>'
            + f'<rect x="{x}" y="{y + 30}" width="{w}" height="10" fill="{cor}"/>')

# 1. a linha
p = [svg_abre(1664, 420, "Ficha de prontuário com uma única linha: liberada, sem queixas. Linha do tempo: mês 0, liberada; mês 6, nova entorse no mesmo tornozelo. A diretoria pergunta: quem liberou, e por quê? Perfil típico")]
rs = []
p.append(ficha(0, 0, 560, 300, MUDO))
rs += [rot(20, 6, "prontuário", w=520, tam=22, cor=PAPEL, peso=700),
       rot(30, 120, "“Liberada. Sem queixas.”", w=500, tam=34, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(0, 330, "perfil típico", w=560, tam=20, cor=MUDO)]
Y = 150
p.append(f'<line x1="660" y1="{Y}" x2="1000" y2="{Y}" stroke="{TINTA}" stroke-width="4"/>')
for x, t, c in [(660, "mês 0: liberada", OXID), (1000, "mês 6: nova entorse, mesmo tornozelo", FOSF)]:
    p.append(f'<circle cx="{x}" cy="{Y}" r="22" fill="{c}"/>')
    rs.append(rot(x - 110, Y + 34, t, w=220, tam=22, cor=c, peso=700, alinha="center", lh=1.2))
p.append(caixa(1180, 20, 484, 280, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1204, 44, "a diretoria do clube", w=436, tam=22, cor=MUDO, peso=700),
       rot(1204, 100, "“Quem liberou, e por quê?”", w=436, tam=34, cor=FOSF, peso=700, serif=True, lh=1.2),
       rot(640, 330, "O que não está escrito, seis meses depois, não aconteceu.", w=1024, tam=26, cor=TINTA, peso=700, serif=True)]
diagrama(S, "linha", 420, p, rs, eyebrow="Handebol, uma armadora depois de uma entorse", titulo="Uma linha no prontuário, e seis meses depois ninguém sabe por quê")

# 2. resultado e decisão
p = [svg_abre(1664, 420, "Duas fichas lado a lado. O resultado: liberada. A decisão: a pergunta, o que se sabia, as opções, quem decidiu, o que foi combinado, quando reavaliar. O erro: registrar o resultado e não a decisão")]
rs = []
p.append(ficha(0, 0, 560, 420, MUDO))
rs += [rot(20, 6, "o resultado", w=520, tam=22, cor=PAPEL, peso=700),
       rot(30, 190, "liberada", w=500, tam=44, cor=TINTA, peso=700, serif=True, alinha="center")]
p.append(ficha(640, 0, 1024, 420, OXID))
rs.append(rot(660, 6, "a decisão", w=984, tam=22, cor=PAPEL, peso=700))
for j, t in enumerate(SEIS):
    y = 64 + j * 58
    p.append(f'<circle cx="684" cy="{y + 18}" r="16" fill="{OXID}"/>')
    rs += [rot(670, y + 4, str(j + 1), w=28, tam=20, cor=PAPEL, peso=700, alinha="center"), rot(716, y + 2, t, w=920, tam=24, cor=TINTA, peso=700)]
diagrama(S, "decisao", 420, p, rs, eyebrow="O erro", titulo="O erro é registrar o resultado e não a decisão")

# 3. viés de resultado
p = [svg_abre(1664, 420, "A mesma decisão desenhada duas vezes, com dois desfechos, bom e ruim, e a nota dada à qualidade da decisão: alta e baixa. Estudo de 1988: a mesma decisão julgada pelo desfecho, mesmo por quem dizia que o desfecho não deveria importar"), defs(TINTA)]
rs = []
for j, (desf, nota, c, h) in enumerate([("desfecho bom", "decisão julgada boa", OXID, 260), ("desfecho ruim", "decisão julgada ruim", FOSF, 110)]):
    y = j * 210
    p.append(caixa(0, y, 300, 180, AZUL, AZUL_T, esp=3, rx=16))
    rs.append(rot(20, y + 60, "a mesma decisão", w=260, tam=26, cor=AZUL, peso=700, serif=True, alinha="center"))
    p.append(seta(310, y + 90, 400, y + 90, TINTA, "m0", esp=4))
    p.append(f'<circle cx="470" cy="{y + 90}" r="56" fill="{c}"/>')
    rs.append(rot(410, y + 160, desf, w=120, tam=20, cor=c, peso=700, alinha="center"))
    p.append(seta(540, y + 90, 620, y + 90, TINTA, "m0", esp=4))
    p.append(f'<rect x="640" y="{y + 90 - 30}" width="{h * 2}" height="60" rx="10" fill="{c}"/>')
    rs.append(rot(660, y + 76, nota, w=480, tam=24, cor=PAPEL if h > 150 else TINTA, peso=700) if h > 150 else rot(880, y + 76, nota, w=400, tam=24, cor=c, peso=700))
p.append(caixa(1240, 0, 424, 420, FOSF, FOSF_T, esp=3, rx=18))
rs += [rot(1264, 24, "Viés de resultado", w=376, tam=30, cor=FOSF, peso=700, serif=True),
       rot(1264, 100, "estudo de 1988, com decisões médicas entre os exemplos", w=376, tam=22, cor=TINTA, peso=700, lh=1.25),
       rot(1264, 220, "acontece mesmo com quem diz que o desfecho não deveria importar", w=376, tam=24, cor=FOSF, peso=700, lh=1.25)]
diagrama(S, "vies", 420, p, rs, eyebrow="Por que isso pesa", titulo="Sem registro da decisão, só resta julgá-la pelo desfecho",
         fonte="J Pers Soc Psychol 1988")

# 4. por que o erro acontece
p = [svg_abre(1664, 360, "Quatro motivos do erro: falta de tempo; registro visto como burocracia de defesa; cada profissão no seu sistema; o que não deu problema não precisa ser escrito")]
rs = []
for j, (ic, t, x_) in enumerate([("t:clock", "falta de tempo", "o registro é o último passo e o primeiro cortado"),
                                 ("t:shield", "burocracia de defesa", "feito para se proteger, e por isso mínimo"),
                                 ("t:users", "cada profissão no seu sistema", "prontuário, outro prontuário, planilha"),
                                 ("t:check", "“não deu problema”", "ninguém sabe, na hora, o que vai dar")]):
    x = j * 420
    p.append(caixa(x, 0, 396, 360, GLIC, CARTAO, esp=3, rx=18))
    p.append(icone(ic, x + 24, 24, 56, GLIC))
    rs += [rot(x + 24, 110, t, w=348, tam=26, cor=TINTA, peso=700, serif=True, lh=1.2), rot(x + 24, 220, x_, w=348, tam=22, cor=MUDO, peso=700, lh=1.3)]
diagrama(S, "motivos", 360, p, rs, eyebrow="Por que o erro acontece", titulo="Quatro motivos fazem o registro encolher até virar carimbo")

# 5. a ficha de decisão
p = [svg_abre(1664, 440, "A ficha de decisão em seis linhas: a pergunta; o que se sabia, com números; as opções consideradas; o que foi decidido e por quem; o que foi dito e combinado com a atleta; quando e como reavaliar. Seis linhas, dois minutos")]
rs = []
p.append(ficha(0, 0, 1100, 440, OXID))
rs.append(rot(20, 6, "ficha de decisão", w=1060, tam=22, cor=PAPEL, peso=700))
for j, t in enumerate(SEIS):
    y = 64 + j * 62
    p.append(f'<line x1="24" y1="{y + 50}" x2="1076" y2="{y + 50}" stroke="{GRADE}" stroke-width="2"/>')
    rs += [rot(24, y + 6, f"{j + 1}.", w=40, tam=26, cor=OXID, peso=700, serif=True), rot(72, y + 8, t, w=1000, tam=26, cor=TINTA, peso=700)]
p.append(caixa(1160, 0, 504, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:clock", 1184, 24, 56, AZUL))
rs += [rot(1256, 34, "dois minutos", w=384, tam=30, cor=AZUL, peso=700, serif=True),
       rot(1184, 130, "já apareceu no curso", w=456, tam=22, cor=MUDO, peso=700),
       rot(1184, 180, "a ficha de seis campos da decisão de retorno", w=456, tam=24, cor=TINTA, peso=700, lh=1.25),
       rot(1184, 270, "o registro de cinco linhas da comunicação com pais e treinadores", w=456, tam=24, cor=TINTA, peso=700, lh=1.25)]
diagrama(S, "ficha", 440, p, rs, eyebrow="A correção", titulo="Seis linhas guardam a decisão, e não só o carimbo")

# 6. rastreabilidade
p = [svg_abre(1664, 360, "A cadeia da rastreabilidade em quatro elos: data e autor de cada registro; a versão do protocolo usada; o que mudou, e quando; um lugar só, que a equipe acessa. Rastreável: outra pessoa refaz o caminho")]
rs = []
for j, (ic, t) in enumerate([("t:calendar", "data e autor de cada registro"), ("t:writing", "a versão do protocolo usada"),
                             ("t:arrows-exchange", "o que mudou, e quando"), ("t:users", "um lugar só, que a equipe acessa")]):
    x = j * 420
    p.append(f'<ellipse cx="{x + 190}" cy="130" rx="180" ry="110" fill="{CARTAO}" stroke="{AZUL}" stroke-width="6"/>')
    p.append(icone(ic, x + 162, 50, 56, AZUL))
    rs.append(rot(x + 40, 120, t, w=300, tam=24, cor=TINTA, peso=700, alinha="center", lh=1.2))
rs.append(rot(0, 290, "Rastreável: outra pessoa, meses depois, refaz o caminho da decisão em cinco minutos.", w=1664, tam=28, cor=AZUL, peso=700, serif=True, alinha="center"))
diagrama(S, "rastreio", 360, p, rs, eyebrow="O que torna o registro rastreável", titulo="Quatro elos permitem refazer o caminho de uma decisão")

# 7. o que a lei pede
p = [svg_abre(1664, 400, "Prontuário com cadeado e calendário: guarda mínima de 20 anos a partir do último registro, papel ou digital, lei de 2018. Três notas: o prontuário é do paciente; cada conselho profissional tem regras próprias; planilha do clube não substitui prontuário")]
rs = []
p.append(ficha(0, 0, 520, 400, TINTA))
p.append(icone("t:lock", 210, 70, 100, TINTA))
rs += [rot(20, 6, "prontuário", w=480, tam=22, cor=PAPEL, peso=700),
       rot(20, 190, "20 anos", w=480, tam=56, cor=TINTA, peso=700, serif=True, alinha="center"),
       rot(20, 280, "de guarda mínima, a partir do último registro, papel ou digital", w=480, tam=22, cor=TINTA, peso=700, alinha="center", lh=1.25),
       rot(20, 360, "lei brasileira de 2018", w=480, tam=20, cor=MUDO, alinha="center")]
for j, (t, c) in enumerate([("o prontuário é do paciente, que tem direito de acesso", AZUL), ("cada conselho profissional tem regras próprias de registro", GLIC),
                            ("a planilha do clube não substitui o prontuário de quem atendeu", FOSF)]):
    y = j * 136
    p.append(caixa(600, y, 1064, 116, c, CARTAO, esp=3, rx=16))
    rs.append(rot(624, y + 34, t, w=1016, tam=26, cor=TINTA, peso=700))
diagrama(S, "lei", 400, p, rs, eyebrow="O que a lei pede", titulo="O prontuário fica pelo menos vinte anos, e é do paciente",
         fonte="Lei nº 13.787/2018")

# 8. o registro reescrito
p = [svg_abre(1664, 440, "O registro da armadora reescrito. Antes: liberada, sem queixas. Depois, seis linhas: pergunta, volta ao jogo; salto unipodal 92% do outro lado, equilíbrio sem falha, sem dor; opções, liberar, liberar com restrição, esperar duas semanas; liberada com tornozeleira nos primeiros jogos, decisão da médica com a fisioterapeuta; dito, o risco de nova entorse existe e cai com o programa mantido; reavaliar em quatro semanas. Valores ilustrativos"), defs(TINTA)]
rs = []
p.append(ficha(0, 60, 360, 220, MUDO))
rs += [rot(20, 66, "antes", w=320, tam=22, cor=PAPEL, peso=700),
       rot(20, 160, "“Liberada. Sem queixas.”", w=320, tam=26, cor=TINTA, peso=700, serif=True, alinha="center", lh=1.2)]
p.append(seta(380, 170, 440, 170, TINTA, "m0", esp=4))
p.append(ficha(460, 0, 1204, 440, OXID))
rs.append(rot(480, 6, "depois · valores ilustrativos", w=1164, tam=22, cor=PAPEL, peso=700))
for j, t in enumerate(["pergunta: volta ao jogo", "salto numa perna só: 92% do outro lado; equilíbrio sem falha; sem dor",
                       "opções: liberar, liberar com restrição, esperar duas semanas", "liberada com tornozeleira nos primeiros jogos: médica, com a fisioterapeuta",
                       "dito: o risco de nova entorse existe, e cai com o programa mantido", "reavaliar em quatro semanas"]):
    y = 60 + j * 62
    rs += [rot(484, y + 6, f"{j + 1}.", w=36, tam=24, cor=OXID, peso=700, serif=True), rot(528, y + 8, t, w=1116, tam=24, cor=TINTA, peso=700)]
diagrama(S, "reescrito", 440, p, rs, eyebrow="O mesmo registro, reescrito", titulo="Com seis linhas, a recidiva vira um risco medido, dito e aceito")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Documentação e rastreabilidade", "titulo": "Guardar a decisão, e não só o carimbo",
          "regras": ["Registre a decisão: pergunta, dados, opções, quem, o que foi dito, quando rever",
                     "Sem registro, a decisão é julgada pelo desfecho",
                     "Data, autor, versão e o que mudou, num lugar comum"],
          "cards": [{"ic": "t:writing", "t": "Quem decide", "x": "Escreve as seis linhas no mesmo dia."},
                    {"ic": "t:users", "t": "Cada profissão", "x": "Registra no seu prontuário e alimenta o lugar comum da equipe."},
                    {"ic": "t:clipboard-list", "t": "Quem coordena", "x": "Garante que o lugar comum exista e seja usado."}]})

salvar("14-06.json", {"arquivo": "aulas/MOD14/14-06-documentacao-de-decisao-e-rastreabilidade.md",
                      "titulo": "Documentação de decisão e rastreabilidade", "subtitulo": "Seis linhas contra o viés de resultado",
                      "nota_capa": "Entra por uma armadora de handebol liberada com uma linha no prontuário.",
                      "secoes": {"linha": ["O erro.", "capa"], "vies": ["Por que acontece.", "vies"],
                                 "ficha": ["A correção.", "ficha"], "reescrito": ["O registro reescrito.", "reescrito"]},
                      "slides": S})
