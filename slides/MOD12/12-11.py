"""Spec do deck 12.11. Gera 12-11.json ao lado deste arquivo."""
from _base import *

S = []


def balao(x, y, w, h, t, cor, fundo, rs, tam=22):
    """Balão de fala com rabicho para baixo; o texto entra em rs."""
    out = caixa(x, y, w, h, cor, fundo, esp=3, rx=18)
    out += f'<path d="M {x + 40} {y + h - 2} l 0 26 l 30 -26 z" fill="{fundo}" stroke="{cor}" stroke-width="3" stroke-linejoin="round"/>'
    out += f'<rect x="{x + 38}" y="{y + h - 6}" width="36" height="6" fill="{fundo}"/>'
    rs.append(rot(x + 16, y + 14, t, w=w - 32, tam=tam, cor=TINTA, peso=700, lh=1.25))
    return out


# 1. a pista
p = [svg_abre(1664, 450, "Saltadora de 14 anos na pista, com a tuberosidade da tíbia marcada. Em volta, o pai: ela não pode perder a temporada, tem a bolsa; o treinador: o regional é daqui a três semanas; a atleta: eu quero competir. Calendário com a prova em três semanas")]
rs = []
p.append(icone("h:woman", 690, 150, 280, AZUL))
p.append(f'<circle cx="812" cy="390" r="20" fill="none" stroke="{FOSF}" stroke-width="6"/>')
p.append(balao(0, 20, 480, 120, "Pai: “ela não pode perder a temporada, tem a bolsa”", GLIC, GLIC_T, rs))
p.append(balao(1184, 20, 480, 120, "Treinador: “o regional é daqui a três semanas”", OXID, OXID_T, rs))
p.append(balao(560, 0, 520, 90, "Ela: “eu quero competir”", AZUL, AZUL_T, rs, tam=24))
p.append(caixa(0, 250, 480, 190, TINTA, CARTAO, esp=2, rx=16))
for i in range(21):
    x, y = 24 + (i % 7) * 64, 300 + (i // 7) * 44
    p.append(f'<rect x="{x}" y="{y}" width="52" height="34" rx="6" fill="{FOSF if i == 20 else GRADE}"/>')
rs.append(rot(24, 262, "prova em três semanas", w=432, tam=22, cor=FOSF, peso=700))
p.append(caixa(1184, 250, 480, 190, FOSF, FOSF_T, esp=3, rx=16))
rs.append(rot(1204, 270, "apofisite da tuberosidade da tíbia, sem sinal de alarme", w=440, tam=24, cor=TINTA, peso=700, lh=1.3))
diagrama(S, "pista", 450, p, rs, eyebrow="Uma saltadora de 14 anos e os adultos em volta", titulo="No atleta de base, quem decide não é o paciente")

# 2. as três saídas
p = [svg_abre(1664, 440, "Três saídas. A: laudo de afastamento entregue ao treinador. B: conversas separadas, uma versão para cada adulto. C: conversa conjunta, com ela no centro, e plano escrito de carga. Pergunta: o que decide o caminho?")]
rs = []
for j, (l, t, c, f) in enumerate([("A", "laudo de afastamento entregue ao treinador", FOSF, FOSF_T),
                                   ("B", "conversas separadas: uma versão para cada adulto", GLIC, GLIC_T),
                                   ("C", "conversa conjunta, com ela no centro, e plano escrito", OXID, OXID_T)]):
    x = j * 564
    p.append(caixa(x, 0, 536, 320, c, f, esp=3, rx=18))
    p.append(f'<circle cx="{x + 268}" cy="80" r="50" fill="{c}"/>')
    rs += [rot(x + 218, 52, l, w=100, tam=48, cor=PAPEL, peso=700, alinha="center", serif=True), rot(x + 28, 160, t, w=480, tam=28, cor=TINTA, peso=700, alinha="center", lh=1.3)]
p.append(caixa(0, 360, 1664, 80, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(20, 382, "Antes de escolher: as duas relações que cercam a atleta, a família e o treinador", w=1624, tam=26, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saidas", 440, p, rs, eyebrow="A encruzilhada", titulo="Três jeitos de conduzir a mesma conversa")

# 3. a família
p = [svg_abre(1664, 440, "Espectro de famílias: ausente ou sobrecarregada, equilibrada, superenvolvida. Três regras: fale com ela, não sobre ela; pergunte: e você, o que você quer?; dê à família uma tarefa")]
rs = []
p.append(f'<rect x="0" y="40" width="1664" height="20" rx="10" fill="{GRADE}"/>')
for k, (t, x, c) in enumerate([("ausente ou sobrecarregada", 140, AZUL), ("equilibrada", 832, OXID), ("superenvolvida", 1524, GLIC)]):
    p.append(f'<circle cx="{x}" cy="50" r="26" fill="{c}"/>')
    rs.append(rot(x - 200, 90, t, w=400, tam=24, cor=c, peso=700, alinha="center"))
for k, (ic, t) in enumerate([("t:users", "fale com ela, não sobre ela"), ("t:zoom-question", "“e você, o que você quer?”"), ("t:check", "dê à família uma tarefa: sono, refeição, avisar a dor")]):
    x = k * 564
    p.append(caixa(x, 160, 536, 180, OXID, OXID_T, esp=3, rx=16))
    p.append(icone(ic, x + 24, 200, 72, OXID))
    rs.append(rot(x + 116, 196, t, w=396, tam=26, cor=TINTA, peso=700, lh=1.25))
p.append(caixa(0, 364, 1664, 76, GLIC, GLIC_T, esp=2, rx=14))
rs.append(rot(20, 384, "Para muitas famílias, o esporte é via real de bolsa: mostre que a recomendação serve a esse objetivo", w=1624, tam=24, cor=TINTA, peso=700, alinha="center"))
diagrama(S, "familia", 440, p, rs, eyebrow="A família", titulo="Família sem tarefa cobra; com tarefa, ajuda")

# 4. o treinador
p = [svg_abre(1664, 440, "O treinador e quatro pressões: avaliado por resultado em prazo curto; um grupo, não um indivíduo; pouca formação em crescimento; cultura de suportar. O que funciona: informação, não julgamento; a língua da disponibilidade; solução pronta; para a equipe inteira; crédito devolvido")]
rs = []
p.append(caixa(0, 0, 640, 440, GLIC, GLIC_T, esp=3, rx=18))
rs.append(rot(24, 20, "O que pesa sobre ele", w=592, tam=28, cor=GLIC, peso=700, serif=True))
for j, t in enumerate(["avaliado por resultado, em prazo curto", "um grupo, não um indivíduo", "pouca formação em crescimento", "cultura de suportar a dor"]):
    rs.append(rot(24, 96 + j * 80, "· " + t, w=592, tam=26, cor=TINTA, peso=600))
p.append(caixa(700, 0, 964, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(724, 20, "O que funciona", w=916, tam=28, cor=OXID, peso=700, serif=True))
for j, t in enumerate(["informação, não julgamento", "a língua dele: atleta lesionada não compete", "a solução pronta, não a restrição", "o que serve à equipe inteira", "o crédito devolvido quando dá certo"]):
    p.append(icone("t:check", 724, 96 + j * 66, 36, OXID))
    rs.append(rot(774, 98 + j * 66, t, w=866, tam=26, cor=TINTA, peso=700))
diagrama(S, "treinador", 440, p, rs, eyebrow="O treinador", titulo="Tratado como adversário, ele vence todas as negociações")

# 5. saída A
p = [svg_abre(1664, 440, "Saída A: o laudo de afastamento. Protege no papel; consequências: o treinador se sente excluído, a atleta treina escondida, a família procura outra opinião. Lugar certo: risco real, último recurso"), defs(FOSF)]
rs = []
p.append(caixa(0, 20, 340, 400, TINTA, CARTAO, esp=3, rx=12))
for j in range(7):
    p.append(f'<rect x="40" y="{90 + j * 40}" width="{260 - (j % 3) * 50}" height="12" rx="6" fill="{GRADE}"/>')
rs.append(rot(20, 34, "laudo: afastar", w=300, tam=26, cor=FOSF, peso=700, alinha="center", serif=True))
for j, t in enumerate(["o treinador se sente excluído", "a atleta treina escondida ou esconde a dor", "a família procura outra opinião"]):
    y = j * 120
    p.append(seta(350, 220, 420, y + 50, FOSF, "m0", 4))
    p.append(caixa(430, y, 760, 100, FOSF, FOSF_T, esp=3, rx=16))
    rs.append(rot(454, y + 32, t, w=712, tam=26, cor=TINTA, peso=700))
p.append(caixa(1240, 0, 424, 440, OXID, OXID_T, esp=3, rx=18))
rs += [rot(1264, 24, "Lugar certo", w=376, tam=28, cor=OXID, peso=700, serif=True),
       rot(1264, 90, "risco real e conversas que falharam: o registro por escrito protege a adolescente", w=376, tam=24, cor=TINTA, peso=600, lh=1.3),
       rot(1264, 330, "último recurso, não o primeiro", w=376, tam=26, cor=OXID, peso=700, lh=1.2)]
diagrama(S, "saida_a", 440, p, rs, eyebrow="Saída A, o laudo de afastamento", titulo="O laudo protege no papel e perde a aliança")

# 6. saída B
p = [svg_abre(1664, 440, "Saída B: três conversas separadas. O pai ouve pode competir se doer pouco; o treinador ouve tirar todos os saltos; a atleta ouve quase nada. As versões se encontram no treino e se contradizem"), defs(FOSF)]
rs = []
for k, (t, fala, c, f) in enumerate([("o pai ouve", "“pode competir se doer pouco”", GLIC, GLIC_T), ("o treinador ouve", "“tirar todos os saltos”", OXID, OXID_T), ("ela ouve", "quase nada", AZUL, AZUL_T)]):
    x = k * 564
    p.append(caixa(x, 0, 536, 200, c, f, esp=3, rx=18))
    rs += [rot(x + 24, 20, t, w=488, tam=26, cor=c, peso=700, serif=True), rot(x + 24, 90, fala, w=488, tam=28, cor=TINTA, peso=700, serif=True, lh=1.25)]
    p.append(seta(x + 268, 210, 832, 290, FOSF, "m0", 4))
p.append(caixa(432, 300, 800, 140, FOSF, FOSF_T, esp=3, rx=18))
rs.append(rot(456, 324, "no treino seguinte, as três versões se encontram e se contradizem", w=752, tam=26, cor=TINTA, peso=700, alinha="center", lh=1.3))
diagrama(S, "saida_b", 440, p, rs, eyebrow="Saída B, as conversas separadas", titulo="Cada adulto cumpre um plano que não existe")

# 7. saída C
p = [svg_abre(1664, 440, "Saída C: uma mesa com a atleta no centro, pai, treinador e profissional. O plano escrito em quatro linhas: mantém técnica, corrida de aproximação, força de tronco e membros superiores; sai o volume de saltos, contado; a prova decidida por critério de dor, não por data; quem faz o quê")]
rs = []
p.append(f'<ellipse cx="300" cy="230" rx="240" ry="120" fill="{CARTAO}" stroke="{TINTA}" stroke-width="3"/>')
for (x, y, c, t) in [(300, 80, AZUL, "ela"), (60, 230, GLIC, "pai"), (540, 230, OXID, "técnico"), (300, 380, TINTA, "saúde")]:
    p.append(f'<circle cx="{x}" cy="{y}" r="44" fill="{c}"/>')
    rs.append(rot(x - 80, y - 14, t, w=160, tam=22, cor=PAPEL, peso=700, alinha="center"))
p.append(caixa(640, 0, 1024, 340, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(664, 18, "O plano escrito", w=976, tam=28, cor=OXID, peso=700, serif=True))
for j, (a, b) in enumerate([("mantém", "técnica, corrida de aproximação, força de tronco e braços"), ("sai", "o volume de saltos, contado"),
                            ("a prova", "decidida por critério de dor, não por data"), ("quem faz o quê", "treinador conta, pai cuida do sono, reavaliação em 2 semanas")]):
    rs += [rot(664, 80 + j * 62, a, w=210, tam=24, cor=OXID, peso=700), rot(880, 80 + j * 62, b, w=760, tam=24, cor=TINTA, peso=600)]
p.append(caixa(640, 370, 1024, 70, TINTA, TINTA, esp=0, rx=14))
rs.append(rot(660, 388, "Sem risco imediato: todos os adultos do mesmo lado, e ela dentro da decisão", w=984, tam=24, cor=PAPEL, peso=700, alinha="center"))
diagrama(S, "saida_c", 440, p, rs, eyebrow="Saída C, a conversa conjunta", titulo="A prova vira consequência de um critério, não de uma briga",
         fonte="Consenso do COI sobre desenvolvimento do jovem atleta, Br J Sports Med 2015")

# 8. o cuidador
p = [svg_abre(1664, 440, "Na outra ponta da vida: a dançarina na casa dos oitenta e a filha, que quer que ela pare de dançar para não cair. As mesmas regras: fale com ela, não sobre ela; a decisão é dela; dê à cuidadora uma tarefa: a casa segura, ir junto ao baile. O risco explicado com número: exercício reduz quedas")]
rs = []
p.append(icone("h:woman", 30, 60, 240, FOSF))
p.append(icone("h:woman", 270, 100, 200, GLIC))
rs += [rot(0, 330, "a dançarina", w=300, tam=24, cor=FOSF, peso=700, alinha="center"), rot(250, 330, "a filha", w=240, tam=24, cor=GLIC, peso=700, alinha="center")]
p.append(balao(260, 0, 420, 90, "“melhor parar, para não cair”", GLIC, GLIC_T, rs))
for j, (t, c, f) in enumerate([("fale com ela, não sobre ela", OXID, OXID_T), ("a decisão é dela: autonomia também é saúde", OXID, OXID_T),
                               ("tarefa da cuidadora: a casa segura, ir junto ao baile", OXID, OXID_T), ("o risco com número: o exercício certo reduz quedas", AZUL, AZUL_T)]):
    y = j * 112
    p.append(caixa(760, y, 904, 96, c, f, esp=3, rx=16))
    rs.append(rot(784, y + 30, t, w=856, tam=26, cor=TINTA, peso=700))
diagrama(S, "cuidador", 440, p, rs, eyebrow="Na outra ponta da vida", titulo="A cuidadora sem tarefa proíbe; com tarefa, ajuda")

# 9. o registro
p = [svg_abre(1664, 440, "Ficha de registro em cinco linhas: o que foi avaliado; o que foi recomendado; o que foi combinado e com quem; o critério de reavaliação; o que não foi acatado. Com vários adultos envolvidos, o registro é a memória do que foi combinado")]
rs = []
p.append(caixa(0, 0, 1100, 440, TINTA, CARTAO, esp=3, rx=16))
for j, t in enumerate(["o que foi avaliado", "o que foi recomendado", "o que foi combinado, e com quem", "o critério de reavaliação", "o que não foi acatado"]):
    y = 30 + j * 80
    p.append(f'<circle cx="60" cy="{y + 26}" r="22" fill="{OXID}"/>')
    rs += [rot(40, y + 12, str(j + 1), w=40, tam=24, cor=PAPEL, peso=700, alinha="center"), rot(100, y + 10, t, w=960, tam=30, cor=TINTA, peso=700, serif=True)]
    p.append(f'<line x1="100" y1="{y + 64}" x2="1060" y2="{y + 64}" stroke="{GRADE}" stroke-width="2"/>')
p.append(caixa(1160, 0, 504, 440, OXID, OXID_T, esp=3, rx=18))
rs.append(rot(1184, 40, "Com vários adultos envolvidos, o registro é a memória do que foi combinado.", w=456, tam=30, cor=TINTA, peso=700, serif=True, lh=1.3))
diagrama(S, "registro", 440, p, rs, eyebrow="O registro, nas duas pontas", titulo="Cinco linhas para retomar a conversa onde parou")

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Fecho do módulo · três níveis", "titulo": "Dos três meninos na peneira à dançarina de volta ao salão",
          "regras": ["Decisão: a medicina estima maturação, diagnostica, faz triagem e investiga; quem treina e a fisioterapia decidem caminho, força e plano",
                     "Contribuição: a curva de altura da família, os saltos contados, o trimestre no clube, a cuidadora que acompanha",
                     "Reconhecimento: os 12 cm num ano, a “dor do crescimento”, o dispensado de dezembro, a força caindo, o medo de cair"],
          "cards": [{"ic": "h:doctor", "t": "Medicina e fisioterapia", "x": "Maturação, esqueleto imaturo, triagem, quedas e investigação no máster."},
                    {"ic": "t:stopwatch", "t": "Quem treina", "x": "Gestos contados, força do jovem ao idoso, equilíbrio, plano que envelhece."},
                    {"ic": "t:users", "t": "Todos", "x": "Próximo módulo: o atleta amador e o praticante recreacional."}]})

salvar("12-11.json", {"arquivo": "aulas/MOD12/12-11-comunicacao-com-pais-treinadores-e-cuidadores.md",
                      "titulo": "Comunicação com pais, treinadores e cuidadores", "subtitulo": "Três saídas para a mesma conversa",
                      "nota_capa": "Entra por uma saltadora de catorze anos e os adultos em volta. Fecha o módulo.",
                      "secoes": {"pista": ["A decisão.", "capa"], "familia": ["Família e treinador.", "familia"],
                                 "saida_a": ["As três saídas.", "saida_a"], "cuidador": ["O cuidador e o registro.", "cuidador"],
                                 "fecho": ["O fecho do módulo.", "fecho"]},
                      "slides": S})
