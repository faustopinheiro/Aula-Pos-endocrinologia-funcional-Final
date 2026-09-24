"""Spec do deck 3.6. Gera 03-06.json ao lado deste arquivo."""
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

# 1. hipnograma e pulso
p = [svg_abre(1664, 440, "Hipnograma de uma noite: o primeiro bloco de sono de ondas lentas logo depois de adormecer coincide com o maior pulso de GH; os pulsos seguintes são menores")]
X0, W = 40, 1600
fx = lambda h: X0 + h / 8 * W
# estágios: 0 vigília,1 REM,2 N1,3 N2,4 N3 (y maior = mais profundo)
estagios = [(0, 0), (0.2, 2), (0.35, 3), (0.5, 4), (1.3, 3), (1.5, 1), (1.7, 3), (2.0, 4), (2.5, 3), (3.0, 1), (3.3, 3),
            (4.2, 1), (4.6, 3), (5.4, 1), (5.9, 3), (6.7, 1), (7.3, 3), (7.8, 0), (8, 0)]
ys = {0: 215, 1: 240, 2: 262, 3: 288, 4: 330}
d = f"M{fx(0):.0f} {ys[0]}"
for i in range(1, len(estagios)):
    h, e = estagios[i]
    d += f" H{fx(h):.0f} V{ys[e]}"
p.append(f'<path d="{d}" fill="none" stroke="{TINTA}" stroke-width="4"/>')
p.append(f'<rect x="{fx(0.5):.0f}" y="318" width="{fx(1.3)-fx(0.5):.0f}" height="24" fill="{AZUL}" opacity="0.35"/>')
gh = []
for k in range(0, 161):
    h = k / 20
    v = 8 + 150 * math.exp(-((h - 0.9) / 0.35) ** 2) + 35 * math.exp(-((h - 2.2) / 0.3) ** 2) + 20 * math.exp(-((h - 4.5) / 0.3) ** 2) + 15 * math.exp(-((h - 6.5) / 0.3) ** 2)
    gh.append(f"{fx(h):.0f},{190 - v:.0f}")
p.append(f'<polyline points="{" ".join(gh)}" fill="none" stroke="{FOSF}" stroke-width="6" stroke-linejoin="round"/>')
p.append(f'<line x1="{X0}" y1="400" x2="{X0+W}" y2="400" stroke="{MUDO}" stroke-width="2"/>')
p.append("</svg>")
rs = [rot(fx(1.1), 16, "o maior pulso de GH do dia", w=460, tam=28, cor=FOSF, peso=700),
      rot(fx(0.5), 350, "ondas lentas", w=260, tam=26, cor=AZUL, peso=700),
      rot(fx(5.2), 120, "GH", w=100, tam=28, cor=FOSF, peso=700),
      rot(fx(8) - 300, 345, "fases do sono", w=300, tam=26, cor=TINTA, peso=600, alinha="right"),
      rot(X0, 406, "adormecer", w=300, tam=24, cor=MUDO),
      rot(X0 + W - 300, 406, "+8 horas", w=300, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "sono", "tipo": "diagrama", "h": 440, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Primeira e segunda afirmações", "titulo": "Ondas lentas, não REM; o adormecer, não o relógio",
          "destaque": "Quem protege o pulso é a primeira metade da noite. E as ondas lentas caem cedo, entre 25 e 45 anos, com o GH junto.",
          "destaque_cor": "petr", "fonte": "Esquema, sem valores medidos · Van Cauter, Leproult e Plat, JAMA 2000 · 149 homens de 16 a 83 anos"})

# 2. enquadramento
S.append({"id": "enquadre", "tipo": "duas", "eyebrow": "O enquadramento", "titulo": "Uma doença rara e uma queda universal",
          "esq": {"t": "Deficiência do adulto: existe, e é rara", "cor": "verm",
                  "itens": ["lesão ou tumor de hipófise", "sequela de radioterapia, trauma craniano",
                            "critério diagnóstico, tratamento que ajuda muito"]},
          "dir": {"t": "Queda com a idade: universal", "cor": "ambar",
                  "itens": ["a partir da terceira década, em todo mundo", "fisiológica, e vendida como doença",
                            "antienvelhecimento, GH injetável, secretagogos, peptídeos"]},
          "destaque": "Dois comandos opostos no hipotálamo, um que estimula e a somatostatina, que freia. A hipófise libera em pulsos; o fígado responde com IGF-1.",
          "destaque_cor": "tinta"})

# 3. dosar GH
S.append({"id": "dosar", "tipo": "cards", "eyebrow": "Terceira e quarta afirmações", "titulo": "GH isolado no sangue é quase inútil",
          "cards": [{"t": "Dosagem isolada de GH", "x": "no vale de um pulso, indetectável numa pessoa normal", "cor": "verm"},
                    {"t": "IGF-1", "x": "o integrador de dias: é o que se olha", "cor": "petr"},
                    {"t": "Teste de estímulo", "x": "o que faz o diagnóstico no adulto, com endocrinologista", "cor": "petr"},
                    {"t": "IGFBP-3", "x": "sem papel no diagnóstico de rotina do adulto", "cor": "ambar"}],
          "destaque": "E a mulher em idade reprodutiva secreta mais GH por dia do que o homem.", "destaque_cor": "tinta",
          "fonte": "Ho e colaboradores, Journal of Clinical Endocrinology and Metabolism 1987"})

# 4. restrição: GH sobe, IGF-1 cai
p = [svg_abre(1664, 380, "Em restrição energética o GH sobe e o IGF-1 cai: o fígado deixa de responder ao GH"),
     "<defs>" + seta_marker("g1", MUDO) + "</defs>"]
p.append(f'<line x1="0" y1="300" x2="1664" y2="300" stroke="{MUDO}" stroke-width="2"/>')
for x, h0, h1, cor in ((120, 120, 230, AZUL), (1240, 200, 90, FOSF)):
    p.append(f'<rect x="{x}" y="{300-h0}" width="130" height="{h0}" rx="4" fill="{MUDO}" opacity="0.5"/>')
    p.append(f'<rect x="{x+160}" y="{300-h1}" width="130" height="{h1}" rx="4" fill="{cor}"/>')
p.append(caixa(620, 90, 424, 160, GLIC, GLIC_T, esp=3))
p.append(seta(440, 170, 600, 170, MUDO, "g1", esp=5))
p.append(f'<line x1="1060" y1="170" x2="1200" y2="170" stroke="{MUDO}" stroke-width="5" stroke-dasharray="12 10"/>')
p.append(f'<line x1="1115" y1="140" x2="1145" y2="200" stroke="{FOSF}" stroke-width="7" stroke-linecap="round"/>')
p.append("</svg>")
rs = [rot(120, 316, "GH", w=290, tam=30, cor=AZUL, peso=700, alinha="center"),
      rot(1240, 316, "IGF-1", w=290, tam=30, cor=FOSF, peso=700, alinha="center"),
      rot(100, 20, "antes · em restrição", w=330, tam=24, cor=MUDO, alinha="center"),
      rot(1220, 20, "antes · em restrição", w=330, tam=24, cor=MUDO, alinha="center"),
      rot(620, 120, "fígado", w=424, tam=32, cor=TINTA, peso=700, alinha="center"),
      rot(620, 170, "resistência ao GH", w=424, tam=28, cor=GLIC, peso=700, alinha="center")]
S.append({"id": "restricao", "tipo": "diagrama", "h": 380, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quinta afirmação", "titulo": "IGF-1 baixo em restrição é a assinatura do déficit",
          "destaque": "O comando é dado com força e o fígado não responde. Olhar só o GH ou só o IGF-1 leva a duas leituras erradas.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · Areta, Taylor e Koehler, European Journal of Applied Physiology 2021"})

# 5. jejum e dois IGF-1
S.append({"id": "jejum", "tipo": "duas", "eyebrow": "Sexta afirmação", "titulo": "“Jejum sobe o GH, logo é anabólico”",
          "esq": {"t": "No jejum", "cor": "ambar",
                  "itens": ["o GH sobe: é verdade e se mede", "o IGF-1 cai: a mesma resistência do fígado",
                            "a frase de venda está pela metade"]},
          "dir": {"t": "Dois IGF-1", "cor": "petr",
                  "itens": ["o que circula, vindo do fígado", "o que a fibra fabrica sob tensão mecânica",
                            "para hipertrofia, pesa mais o local"]},
          "destaque": "Subir um fator de crescimento no sangue não reproduz o que a tensão produz dentro da fibra. O frasco não substitui a série.",
          "destaque_cor": "petr"})

# 6. mitocôndria
p = [svg_abre(1664, 360, "Demanda energética da célula, AMPK, cálcio e sinal redox convergem no PGC-1 alfa, que dispara a biogênese mitocondrial; GH e IGF-1 ficam fora desse circuito, ligados a crescimento e reparo"),
     "<defs>" + seta_marker("m1", OXID) + "</defs>"]
for i, t_ in enumerate(("AMPK", "cálcio", "sinal redox")):
    p.append(caixa(0, 20 + i * 110, 300, 80, OXID, OXID_T, esp=3))
    p.append(seta(310, 60 + i * 110, 560, 170, OXID, "m1", esp=4))
p.append(caixa(580, 120, 320, 100, OXID, CARTAO, esp=5))
p.append(seta(910, 170, 1010, 170, OXID, "m1", esp=5))
p.append(caixa(1030, 120, 300, 100, OXID, OXID_T, esp=3))
p.append(f'<rect x="1380" y="80" width="284" height="180" rx="14" fill="{CLARO}" stroke="{MUDO}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append("</svg>")
rs = [rot(0, 44, "AMPK", w=300, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(0, 154, "cálcio", w=300, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(0, 264, "sinal redox", w=300, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(580, 152, "PGC-1α", w=320, tam=34, cor=OXID, peso=700, alinha="center"),
      rot(1030, 140, "mais mitocôndria", w=300, tam=28, cor=TINTA, peso=700, alinha="center"),
      rot(1380, 110, "GH e IGF-1", w=284, tam=28, cor=MUDO, peso=700, alinha="center"),
      rot(1380, 160, "crescimento e reparo: outro circuito", w=284, tam=24, cor=MUDO, alinha="center")]
S.append({"id": "mitocondria", "tipo": "diagrama", "h": 360, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Sétima afirmação", "titulo": "GH não é o motor da mitocôndria",
          "destaque": "Quem dispara a biogênese é a demanda da própria célula. Vender GH para isso é vender um frasco no lugar de uma sessão.",
          "destaque_cor": "tinta"})

# 7. Liu e Meinhardt
p = [svg_abre(1664, 400, "Meinhardt 2010: capacidade de sprint mais 3,9% com GH e mais 8,3% com GH e testosterona; força, potência e capacidade aeróbica sem mudança; efeito perdido seis semanas depois de parar")]
p.append(f'<line x1="700" y1="0" x2="700" y2="400" stroke="{GRADE}" stroke-width="3"/>')
Y0, ESC = 260, 18
for x, v, cor in ((820, 3.9, AZUL), (1120, 8.3, FOSF)):
    p.append(f'<rect x="{x}" y="{Y0 - v*ESC:.0f}" width="200" height="{v*ESC:.0f}" rx="4" fill="{cor}"/>')
p.append(f'<line x1="760" y1="{Y0}" x2="1664" y2="{Y0}" stroke="{MUDO}" stroke-width="2"/>')
p.append(caixa(1380, 60, 284, 200, MUDO, CLARO, esp=2))
p.append("</svg>")
rs = [rot(0, 0, "Liu e colaboradores, 2008", w=660, tam=30, cor=TINTA, peso=700),
      rot(0, 50, "303 pessoas saudáveis que receberam GH", w=660, tam=26, cor=TINTA),
      rot(0, 120, "massa magra: sobe", w=660, tam=30, cor=OXID, peso=700),
      rot(0, 170, "força e capacidade de exercício: não", w=660, tam=30, cor=FOSF, peso=700),
      rot(0, 230, "mais inchaço e mais fadiga relatada", w=660, tam=26, cor=MUDO),
      rot(760, 0, "Meinhardt e colaboradores, 2010 · sprint", w=900, tam=30, cor=TINTA, peso=700),
      rot(790, Y0 - 3.9 * ESC - 50, "+3,9%", w=260, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(1090, Y0 - 8.3 * ESC - 50, "+8,3%", w=260, tam=38, cor=TINTA, peso=700, alinha="center", serif=True),
      rot(790, Y0 + 12, "GH", w=260, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(1090, Y0 + 12, "GH e testosterona", w=260, tam=26, cor=TINTA, peso=600, alinha="center"),
      rot(1390, 80, "força, potência, capacidade aeróbica: sem mudança", w=264, tam=24, cor=TINTA, lh=1.3),
      rot(760, 330, "seis semanas depois de parar, o efeito sumiu", w=900, tam=26, cor=MUDO)]
S.append({"id": "desfecho", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Quando alguém mediu desfecho", "titulo": "Um desfecho estreito, modesto e reversível",
          "destaque": "A massa magra que sobe é, em boa parte, água fora das células. O espelho muda; a fibra, bem menos.",
          "destaque_cor": "ambar", "fonte": "Annals of Internal Medicine 2008 e 2010 · 96 atletas recreativos, 8 semanas, com placebo"})

# 8. secretagogo
S.append({"id": "secretagogo", "tipo": "duas", "eyebrow": "Nass e colaboradores, 2008", "titulo": "O biomarcador se move, a função não acompanha",
          "esq": {"t": "O que subiu", "cor": "petr",
                  "itens": ["GH e IGF-1, até a faixa do adulto jovem", "massa livre de gordura"]},
          "dir": {"t": "O que não mudou, e o que piorou", "cor": "verm",
                  "itens": ["força e função: iguais", "glicemia de jejum: subiu", "sensibilidade à insulina: caiu", "cortisol: subiu"]},
          "destaque": "GH e secretagogos estão na lista proibida do controle antidopagem. Muita gente compra sem saber.",
          "destaque_cor": "verm", "fonte": "Annals of Internal Medicine 2008 · 65 adultos saudáveis de 60 a 81 anos, dois anos, secretagogo oral contra placebo"})

# 9. apneia
S.append({"id": "apneia", "tipo": "duas", "eyebrow": "O IGF-1 baixo que vai aparecer", "titulo": "“Você ronca?”",
          "esq": {"t": "O quadro", "cor": "tinta",
                  "itens": ["homem de 50 e poucos anos, treina há anos", "não ganha mais massa, acorda arrebentado",
                            "IGF-1 abaixo da faixa, pedido de GH pronto"]},
          "dir": {"t": "A apneia se reconhece de graça", "cor": "verm",
                  "itens": ["ronco alto, pausas que alguém viu", "sonolência de dia, ganho de peso",
                            "pressão difícil de controlar, álcool à noite"]},
          "destaque": "Acima de 45 anos, com IGF-1 baixo, fadiga e dificuldade de ganhar massa, a apneia entra no diferencial antes da deficiência de GH.",
          "destaque_cor": "petr"})

# 10. condutas
S.append({"id": "condutas", "tipo": "lista", "eyebrow": "O que sobra de prático", "titulo": "Três condutas, em ordem",
          "itens": [{"t": "Proteger a primeira metade da noite", "x": "álcool, sessão dura perto de deitar, apneia, continuidade do sono", "cor": "petr"},
                    {"t": "Alimentar o eixo", "x": "energia disponível e proteína suficiente", "cor": "ambar"},
                    {"t": "Carregar o músculo", "x": "a série é o estímulo; não há substituto sistêmico", "cor": "verm"}],
          "destaque": "A primeira é a única intervenção com mecanismo direto sobre este eixo ao alcance de todo mundo, e é gratuita.",
          "destaque_cor": "tinta"})

# 11. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "As sete correções", "titulo": "Neste eixo, a pergunta é quase sempre sobre o sono",
          "regras": ["Ondas lentas, não REM · o adormecer, não o relógio · GH isolado é quase inútil",
                     "A mulher secreta mais · IGF-1 baixo em restrição é déficit",
                     "Jejum sobe o GH e derruba o IGF-1 · GH não é o motor da mitocôndria"],
          "cards": [{"t": "Médico especialista", "x": "Diagnostica deficiência com teste de estímulo, não com dosagem basal."},
                    {"t": "Toda a equipe", "x": "Reconhece o exame baixo que é consequência, e faz a pergunta que revela a causa."}],
          "quem": "GH, secretagogos e peptídeos para desempenho, estética ou longevidade não são terreno de prescrição de nenhuma profissão desta turma."})

spec = {"arquivo": "aulas/MOD03/03-06-eixo-gh-igf1.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Eixo somatotrófico e exercício", "subtitulo": "GH, IGF-1 e equívocos de interpretação",
        "nota_capa": "Entra direto no primeiro erro.",
        "secoes": {"sono": ["O pulso, o sono e o enquadramento.", "capa"],
                   "exame": ["Dosar GH, IGF-1 em restrição, jejum e mitocôndria.", "dosar"],
                   "desfecho": ["O que os ensaios mediram.", "desfecho"],
                   "conduta": ["O IGF-1 baixo na mesa e as três condutas.", "apneia"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-06.json"), "w"), ensure_ascii=False, indent=1)
print("03-06.json:", len(S), "slides")
