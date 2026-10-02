"""Spec do deck 12.3. Gera 12-03.json ao lado deste arquivo."""
from _base import *

S = []


def calendario(x, y, cores, w=60, h=40, gap=8):
    """Doze meses em linha, cada um com a cor da atividade."""
    return "".join(f'<rect x="{x + i * (w + gap)}" y="{y}" width="{w}" height="{h}" rx="6" fill="{c}"/>' for i, c in enumerate(cores))


MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

# 1. a proposta
p = [svg_abre(1664, 450, "Uma criança de nove anos com raquete de tênis e, ao lado, chuteira e touca de natação. A proposta do clube: programa de alto rendimento, treino todos os dias, o ano inteiro, dedicação exclusiva. Três caminhos saindo da mesa: A, B, C"), defs(TINTA)]
p.append(icone("t:user", 60, 60, 220, GLIC))
rs = [rot(0, 300, "nove anos", w=340, tam=28, cor=GLIC, peso=700, alinha="center")]
for j, t in enumerate(["tênis desde os seis", "natação", "futebol com os amigos"]):
    p.append(caixa(360, 40 + j * 100, 360, 76, OXID if j else GLIC, CARTAO, esp=2, rx=38))
    rs.append(rot(380, 60 + j * 100, t, w=320, tam=26, cor=TINTA, peso=600, alinha="center"))
p.append(caixa(800, 0, 864, 260, FOSF, FOSF_T, esp=3, rx=16))
rs += [rot(824, 20, "Programa de alto rendimento", w=816, tam=32, cor=FOSF, peso=700, serif=True),
       rot(824, 90, "· treino todos os dias, o ano inteiro", w=816, tam=26, cor=TINTA, peso=600),
       rot(824, 140, "· dedicação exclusiva: largar natação e futebol", w=816, tam=26, cor=TINTA, peso=600),
       rot(824, 196, "“quem quer chegar longe começa cedo e só faz isso”", w=816, tam=24, cor=MUDO, serif=True)]
for j, l in enumerate("ABC"):
    x = 900 + j * 260
    p.append(seta(1230, 270, x + 60, 360, TINTA, "m0", 4))
    p.append(f'<circle cx="{x + 60}" cy="400" r="40" fill="{TINTA}"/>')
    rs.append(rot(x + 20, 378, l, w=80, tam=36, cor=PAPEL, peso=700, alinha="center", serif=True))
diagrama(S, "proposta", 450, p, rs, eyebrow="Uma criança de nove anos no tênis", titulo="O clube oferece especialização; a família pede a sua opinião")

# 2. as três saídas
p = [svg_abre(1664, 440, "Encruzilhada com três saídas. A: especializar agora, num esporte que não exige. B: diversificar e especializar depois, na adolescência. C: esporte que exige início cedo, especializar com limites. Pergunta: o que decide o caminho?")]
rs = []
for j, (l, t, c, f) in enumerate([("A", "especializar agora, num esporte que não exige", FOSF, FOSF_T),
                                   ("B", "diversificar e especializar depois, na adolescência", OXID, OXID_T),
                                   ("C", "esporte que exige começar cedo: especializar, com limites", AZUL, AZUL_T)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 320, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 268}" cy="80" r="50" fill="{c}"/>')
    rs += [rot(x + 218, 52, l, w=100, tam=48, cor=PAPEL, peso=700, alinha="center", serif=True), rot(x + 28, 160, t, w=480, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "O que separa as saídas: lesão, abandono e a promessa de chegar mais longe", w=1624, tam=28, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saidas", 440, p, rs, eyebrow="A encruzilhada", titulo="Três saídas, e o tipo de esporte decide qual é possível")

# 3. a evidência sobre lesão
p = [svg_abre(1664, 440, "Duas balanças. Horas por semana de esporte organizado contra idade em anos: quando as horas pesam mais, mais lesão por sobrecarga. Esporte organizado contra brincadeira livre: limite de 2 para 1")]
rs = []
for k, (a, b, regra) in enumerate([("horas por semana", "idade em anos", "horas acima da idade: mais lesão"), ("esporte organizado", "brincadeira livre", "acima de 2 para 1: mais lesão")]):
    x0 = k * 860
    cx = x0 + 400
    p.append(f'<line x1="{cx - 300}" y1="130" x2="{cx + 300}" y2="200" stroke="{TINTA}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<path d="M {cx} 166 l -40 140 l 80 0 z" fill="{TINTA}"/>')
    p.append(f'<rect x="{cx - 360}" y="140" width="120" height="70" rx="10" fill="{FOSF}"/>')
    p.append(f'<rect x="{cx + 250}" y="130" width="100" height="40" rx="10" fill="{OXID}"/>')
    rs += [rot(cx - 400, 60, a, w=280, tam=26, cor=FOSF, peso=700, alinha="center"), rot(cx + 180, 60, b, w=280, tam=26, cor=OXID, peso=700, alinha="center"),
           rot(x0, 340, regra, w=800, tam=28, cor=TINTA, peso=700, alinha="center")]
rs.append(rot(0, 400, "caso e controle: associação, não prova de causa", w=1664, tam=22, cor=MUDO, alinha="center"))
diagrama(S, "lesao", 440, p, rs, eyebrow="Estudo de caso e controle de 2015, 7 a 18 anos", titulo="Mais horas que a idade, e pouca brincadeira, mais lesão",
         fonte="Am J Sports Med 2015")

# 4. a promessa
p = [svg_abre(1664, 440, "Pirâmide invertida: muitas crianças especializadas cedo na base larga, pouquíssimas no topo. Ao lado, atletas de alto nível com várias modalidades na infância e especialização mais tarde. Etiqueta: sem vantagem consistente para chegar ao topo, na maioria dos esportes")]
rs = []
for i in range(6):
    n = 12 - i * 2
    y = 360 - i * 60
    for k in range(n):
        p.append(f'<circle cx="{400 - n * 26 + k * 52:.0f}" cy="{y}" r="18" fill="{FOSF if i < 5 else OXID}"/>')
rs.append(rot(80, 396, "muitos começam cedo e só fazem isso", w=640, tam=24, cor=FOSF, peso=700, alinha="center"))
p.append(caixa(860, 0, 804, 320, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(884, 20, "Atletas de alto nível, na infância", w=760, tam=28, cor=OXID, peso=700, serif=True))
for j, (c, t) in enumerate([(GLIC, "futebol"), (AZUL, "natação"), (OXID, "atletismo"), (FOSF, "brincadeira")]):
    p.append(f'<rect x="{900 + j * 180}" y="100" width="160" height="60" rx="30" fill="{c}"/>')
    rs.append(rot(900 + j * 180, 114, t, w=160, tam=22, cor=PAPEL, peso=700, alinha="center"))
rs.append(rot(884, 200, "várias modalidades, especialização mais tarde", w=760, tam=26, cor=TINTA, peso=600))
p.append(caixa(860, 340, 804, 100, FOSF, FOSF_T, esp=3, rx=14))
rs.append(rot(880, 364, "Especializar cedo: sem vantagem consistente para chegar ao topo", w=764, tam=26, cor=FOSF, peso=700, alinha="center", lh=1.2))
diagrama(S, "promessa", 440, p, rs, eyebrow="E a promessa?", titulo="Especializar cedo não aumenta a chance de chegar ao topo",
         fonte="Revisão, Sports Health 2015; consenso, Orthop J Sports Med 2016")

# 5. saída A
p = [svg_abre(1664, 420, "Saída A riscada. Um calendário de doze meses todo da mesma cor. Consequências: mais lesão por sobrecarga, mais abandono, sem ganho demonstrado de alto rendimento")]
p.append(calendario(40, 40, [FOSF] * 12, w=110, h=70, gap=12))
rs = [rot(40 + i * 122, 120, m, w=110, tam=22, cor=MUDO, alinha="center") for i, m in enumerate(MESES)]
rs.append(rot(40, 160, "só tênis, todos os dias, o ano inteiro", w=1460, tam=26, cor=FOSF, peso=700))
for j, t in enumerate(["mais lesão por sobrecarga", "mais esgotamento e abandono", "sem ganho demonstrado de alto rendimento"]):
    x = j * 564
    p.append(caixa(x, 240, 536, 140, FOSF, FOSF_T, esp=3, rx=14))
    rs.append(rot(x + 20, 280, t, w=496, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.25))
diagrama(S, "saida_a", 420, p, rs, eyebrow="Saída A, até o fim", titulo="Troca risco real por uma vantagem que não se confirma")

# 6. saída B
p = [svg_abre(1664, 470, "Saída B. Um calendário de doze meses com cores variadas: tênis, natação, futebol, brincadeira. Regras: horas por semana até a idade; organizado no máximo o dobro da brincadeira; um a dois dias sem esporte organizado por semana; alguns meses fora da modalidade principal; especializar depois")]
cores = [GLIC, GLIC, AZUL, GLIC, GLIC, OXID, AZUL, GLIC, GLIC, OXID, GLIC, AZUL]
p.append(calendario(40, 30, cores, w=110, h=70, gap=12))
rs = [rot(40 + i * 122, 110, m, w=110, tam=22, cor=MUDO, alinha="center") for i, m in enumerate(MESES)]
for j, (c, t) in enumerate([(GLIC, "tênis"), (AZUL, "natação"), (OXID, "futebol e brincadeira")]):
    p.append(f'<rect x="{40 + j * 300}" y="150" width="30" height="30" rx="6" fill="{c}"/>')
    rs.append(rot(80 + j * 300, 150, t, w=260, tam=24, cor=TINTA, peso=600))
regras = ["horas por semana até a idade", "organizado até o dobro da brincadeira livre", "1 a 2 dias por semana sem esporte organizado", "alguns meses por ano fora da modalidade", "especializar na adolescência"]
for j, t in enumerate(regras):
    x, y = (j % 2) * 840, 220 + (j // 2) * 84
    p.append(caixa(x, y, 820, 70, OXID, OXID_T, esp=2, rx=12))
    rs.append(rot(x + 20, y + 18, f"{j + 1} · {t}", w=780, tam=26, cor=TINTA, peso=700))
diagrama(S, "saida_b", 470, p, rs, eyebrow="Saída B, a recomendada para a maioria", titulo="Diversificar agora constrói a base do sonho",
         fonte="Mais de oito meses por ano numa modalidade só: mais lesão (consenso de 2016)")

# 7. saída C
p = [svg_abre(1664, 440, "Saída C. Uma ginasta de dez anos com vinte horas semanais. Limites que entram mesmo quando a especialização é necessária: um dia por semana sem treino; pausas no ano; treino de força estruturado; ajuste no movimento que dói; acompanhamento do crescimento; dor lombar em extensão pede investigação")]
p.append(caixa(0, 0, 560, 440, AZUL, AZUL_T, esp=3, rx=18))
p.append(icone("t:user", 180, 40, 200, AZUL))
rs = [rot(20, 260, "ginasta, dez anos", w=520, tam=30, cor=AZUL, peso=700, alinha="center", serif=True),
      rot(20, 320, "20 horas por semana, o ano inteiro", w=520, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(20, 370, "dor lombar na extensão", w=520, tam=26, cor=FOSF, peso=700, alinha="center")]
limites = ["1 dia por semana sem treino", "pausas no meio do ano", "força estruturada", "carga ajustada no movimento que dói", "crescimento acompanhado", "dor lombar em extensão: investigar"]
for j, t in enumerate(limites):
    x, y = 620 + (j % 2) * 524, (j // 2) * 150
    p.append(caixa(x, y, 504, 130, AZUL if j < 5 else FOSF, CARTAO, esp=3, rx=14))
    rs.append(rot(x + 20, y + 36, t, w=464, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.25))
diagrama(S, "saida_c", 440, p, rs, eyebrow="Saída C, quando o esporte exige começar cedo", titulo="Quando especializar é inevitável, a decisão vira limites")

# 8. a conversa
p = [svg_abre(1664, 440, "Mesa de conversa com a família. Frases que funcionam: se o objetivo é ela jogar bem aos dezoito, isso joga a favor; atleta lesionado não treina e não é visto; na intertemporada, natação em vez de parada. Riscadas: vocês estão prejudicando sua filha; quase ninguém se profissionaliza; ignorar o custo da família")]
rs = []
for k, (t, itens, c, f) in enumerate([("Funciona", ["“se o objetivo é jogar bem aos dezoito, isso joga a favor”", "“atleta lesionado não treina e não é visto”", "“na intertemporada, natação em vez de parada”"], OXID, OXID_T),
                                      ("Não funciona", ["“vocês estão prejudicando sua filha”", "“quase ninguém se profissionaliza”", "ignorar o custo que a família já teve"], FOSF, FOSF_T)]):
    x = k * 864
    p.append(caixa(x, 0, 800, 340, c, f, esp=3, rx=18))
    rs.append(rot(x + 24, 18, t, w=760, tam=30, cor=c, peso=700, serif=True))
    for j, it in enumerate(itens):
        rs.append(rot(x + 32, 96 + j * 80, it, w=740, tam=25, cor=TINTA, peso=600, lh=1.25))
p.append(caixa(0, 370, 1664, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 388, "A decisão é da família: informar, recomendar, registrar e continuar acompanhando", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "conversa", 440, p, rs, eyebrow="O critério da decisão", titulo="A recomendação parte do objetivo da própria família")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Especialização precoce", "titulo": "Na infância, base larga; na adolescência, foco",
          "regras": ["Na maioria dos esportes, diversificar na infância e especializar na adolescência",
                     "Horas até a idade, organizado até o dobro da brincadeira, dias e meses fora",
                     "Nos esportes que exigem começar cedo, a decisão vira limites e acompanhamento"],
          "cards": [{"ic": "t:stopwatch", "t": "Quem treina", "x": "Conta as horas, monta a variedade e protege os dias e meses fora."},
                    {"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Investigam a dor por sobrecarga e acompanham o crescimento."},
                    {"ic": "t:users", "t": "Todos", "x": "Conversam com a família a partir do objetivo dela."}]})

salvar("12-03.json", {"arquivo": "aulas/MOD12/12-03-especializacao-precoce.md",
                      "titulo": "Especialização precoce", "subtitulo": "Especializar cedo ou diversificar",
                      "nota_capa": "Entra por uma criança de nove anos chamada ao programa de alto rendimento do clube de tênis.",
                      "secoes": {"proposta": ["A encruzilhada.", "capa"], "lesao": ["A evidência.", "lesao"],
                                 "saida_a": ["As três saídas.", "saida_a"], "conversa": ["A conversa.", "conversa"]},
                      "slides": S})
