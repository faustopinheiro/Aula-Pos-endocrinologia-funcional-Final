"""Spec do deck 5.6. Gera 05-06.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o erro de categoria
S.append({"id": "categoria", "tipo": "frase", "fundo": "tinta", "eyebrow": "O erro é de categoria",
          "frase": "Proteína em pó não é ergogênico. É comida em pó.",
          "apoio": "Dois enganos opostos na mesma sala de espera: quem espera do pó um efeito que ele não tem, e quem o recusa justo onde ele resolveria. Um custa dinheiro; o outro custa músculo."})

# 2. três perfis
S.append({"id": "perfis", "tipo": "cards", "por_linha": 3, "eyebrow": "Três perfis típicos", "titulo": "O pote na pessoa errada",
          "cards": [{"t": "Comprou whey", "x": "já come perto de 2 g/kg por dia; “todo mundo toma”", "cor": "verm"},
                    {"t": "Recusa whey", "x": "come perto de 0,8 g/kg, quase tudo no jantar; “é para ficar grande”", "cor": "ambar"},
                    {"t": "Toma BCAA", "x": "durante o treino longo de corrida, “para proteger o músculo”", "cor": "petr"}],
          "destaque": "Em dois deles a conduta envolve algum pó. Só que não o que compraram.",
          "destaque_cor": "tinta"})

# 3. Morton
S.append({"id": "morton", "tipo": "numeros", "eyebrow": "Morton e colaboradores, 2018", "titulo": "Real, pequeno, e com teto",
          "numeros": [{"n": "+0,30 kg", "x": "de massa livre de gordura, em média", "cor": "petr"},
                      {"n": "+2,49 kg", "x": "no teste de uma repetição máxima, em média", "cor": "ambar"},
                      {"n": "≈ 1,6 g/kg", "x": "de proteína total por dia: acima disso, sem ganho adicional de massa", "cor": "tinta"}],
          "destaque": "O efeito não é do pó. É da proteína que faltava.",
          "destaque_cor": "verm", "fonte": "49 estudos, 1.863 pessoas em treino de força · British Journal of Sports Medicine 2018"})

# 4. obstáculos
S.append({"id": "obstaculos", "tipo": "cards", "por_linha": 3, "eyebrow": "Que obstáculo ele remove?", "titulo": "Seis razões legítimas",
          "cards": [{"t": "Apetite baixo", "x": "líquido passa onde sólido não passa", "cor": "petr"},
                    {"t": "Logística", "x": "cria uma refeição que não existiria", "cor": "petr"},
                    {"t": "Mastigação", "x": "prótese mal adaptada: viabilidade, não conveniência", "cor": "petr"},
                    {"t": "Custo por grama", "x": "perde para ovo e leite; ganha de corte nobre", "cor": "ambar"},
                    {"t": "Dieta vegetal", "x": "fecha a conta com menos volume", "cor": "ambar"},
                    {"t": "Volume de treino", "x": "necessidade alta, pouco tempo entre sessões", "cor": "ambar"}],
          "destaque": "Entra quando há obstáculo, sai quando o obstáculo some. Sem obstáculo, só substitui: e comida traz colina, cálcio, ferro heme, B12, fibra.",
          "destaque_cor": "tinta"})

# 5. tipos
S.append({"id": "tipos", "tipo": "tabela", "eyebrow": "Diferença real e diferença de rótulo", "titulo": "Os tipos",
          "cab": ["Tipo", "O que é", "Para quem"],
          "larguras": [20, 42, 38],
          "linhas": [["Concentrado", "teor variável; no pote comum, perto de 80%", "a maioria"],
                     ["Isolado", "acima de 90%; menos lactose e gordura", "intolerância à lactose"],
                     ["Hidrolisado", "parcialmente quebrado; mais caro, mais amargo", "sem vantagem clínica demonstrada"],
                     ["Caseína", "digestão lenta", "refeição antes de dormir"],
                     ["Vegetais", "soja completa; ervilha e arroz se complementam", "vegano, em mistura bem formulada"]],
          "destaque": "Sabor muda a adesão, não a proteína. Pote simples, um ingrediente, dose declarada.",
          "destaque_cor": "petr"})

# 6. amino spiking
p = [svg_abre(1664, 330, "Esquema da análise: o método mede nitrogênio e multiplica por 6,25; glicina e taurina adicionadas entram na conta como se fossem proteína"),
     "<defs>" + seta_marker("s1", MUDO) + seta_marker("s2", FOSF) + "</defs>"]
rs = []
cx = [(0, "pó no laboratório"), (440, "mede nitrogênio"), (880, "× 6,25"), (1320, "“proteína” no rótulo")]
for i, (x, t) in enumerate(cx):
    cor = AZUL if i < 3 else TINTA
    p.append(caixa(x, 40, 344, 110, cor, AZUL_T if i < 3 else CLARO, esp=3))
    rs.append(rot(x, 76, t, w=344, tam=30, cor=cor, peso=700, alinha="center"))
    if i < 3:
        p.append(f'<line x1="{x+352}" y1="95" x2="{x+430}" y2="95" stroke="{MUDO}" stroke-width="4" marker-end="url(#s1)"/>')
p.append(caixa(440, 220, 344, 100, FOSF, FOSF_T, esp=3))
rs.append(rot(440, 246, "glicina, taurina", w=344, tam=30, cor=FOSF, peso=700, alinha="center"))
p.append(f'<line x1="612" y1="214" x2="612" y2="160" stroke="{FOSF}" stroke-width="4" marker-end="url(#s2)"/>')
p.append("</svg>")
rs.append(rot(830, 236, "têm nitrogênio, entram na conta, não são proteína completa", w=834, tam=26, cor=TINTA))
S.append({"id": "spiking", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Amino spiking", "titulo": "O laudo mede nitrogênio, não proteína",
          "destaque": "O teste que separa mede aminoácido por aminoácido. Defesa do consumidor: controle de qualidade verificável e lote testado.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos"})

# 7. Wolfe
p = [svg_abre(1664, 330, "Nove blocos de aminoácidos essenciais; três são os BCAA fornecidos pelo suplemento; os outros seis só podem vir da quebra de proteína do próprio músculo"),
     "<defs>" + seta_marker("w1", FOSF) + "</defs>"]
rs = []
nomes = ["leucina", "isoleucina", "valina", "histidina", "lisina", "metionina", "fenilalanina", "treonina", "triptofano"]
for i, n in enumerate(nomes):
    x = 32 + i * 180
    bcaa = i < 3
    p.append(caixa(x, 20, 164, 90, AZUL if bcaa else MUDO, AZUL_T if bcaa else CLARO, esp=4 if bcaa else 2, rx=10))
    rs.append(rot(x, 50, n, w=164, tam=22, cor=AZUL if bcaa else TINTA, peso=700 if bcaa else 500, alinha="center"))
    if not bcaa:
        p.append(f'<line x1="{x+82}" y1="218" x2="{x+82}" y2="122" stroke="{FOSF}" stroke-width="3" marker-end="url(#w1)"/>')
p.append(caixa(572, 226, 1044, 90, FOSF, FOSF_T, esp=3))
p.append(f'<line x1="32" y1="140" x2="536" y2="140" stroke="{AZUL}" stroke-width="3"/>')
p.append("</svg>")
rs += [rot(572, 250, "quebra de proteína do próprio músculo", w=1044, tam=30, cor=FOSF, peso=700, alinha="center"),
       rot(32, 156, "o que o pote de BCAA entrega", w=504, tam=24, cor=AZUL, peso=600, alinha="center")]
S.append({"id": "wolfe", "tipo": "diagrama", "h": 330, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Wolfe, 2017", "titulo": "Três de nove",
          "destaque": "Para fazer proteína nova, o músculo precisa dos nove essenciais. O teto dos BCAA sozinhos é aritmética, não falta de estudo.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# 8. Jackman
S.append({"id": "jackman", "tipo": "numeros", "eyebrow": "Jackman e colaboradores, 2017", "titulo": "Não é zero. É metade.",
          "numeros": [{"n": "5,6 g", "x": "de BCAA depois do treino de força", "cor": "tinta"},
                      {"n": "+22%", "x": "síntese de proteína miofibrilar contra placebo de mesma energia", "cor": "petr"},
                      {"n": "≈ ½", "x": "da resposta a uma dose de whey com a mesma quantidade de BCAA", "cor": "verm"}],
          "destaque": "A porção de whey que já tem esses BCAA traz os outros seis essenciais. No treino longo, o que poupa o corpo é carboidrato.",
          "destaque_cor": "ambar", "fonte": "Comparação com whey feita pelos autores, com estudo anterior · Frontiers in Physiology 2017"})

# 9. resto da prateleira
S.append({"id": "prateleira", "tipo": "lista", "eyebrow": "O resto da prateleira", "titulo": "Um veredito por pote",
          "itens": [{"t": "EAA", "x": "mais defensável: apetite baixo, idoso, quem não tolera volume; ainda perde para comida", "cor": "ambar"},
                    {"t": "Leucina isolada", "x": "é o gatilho; gatilho sem matéria-prima não constrói", "cor": "verm"},
                    {"t": "Glutamina", "x": "sem sustentação em pessoa saudável e bem alimentada", "cor": "verm"},
                    {"t": "HMB", "x": "resultados variam muito entre grupos; sem caso para quem já come proteína", "cor": "verm"},
                    {"t": "Pote com tudo dentro", "x": "sem dose por item; se a creatina é indicada, compre creatina", "cor": "verm"}],
          "gap_itens": 16})

# 10. colágeno
S.append({"id": "colageno", "tipo": "duas", "eyebrow": "Shaw e colaboradores, 2017", "titulo": "Colágeno: grupo B, e por quê",
          "esq": {"t": "O estudo", "cor": "petr",
                  "itens": ["8 homens, cruzado, duplo-cego", "5 ou 15 g de gelatina com vitamina C", "1 hora antes de 6 min de pular corda", "com 15 g, o marcador de síntese quase dobrou"]},
          "dir": {"t": "A leitura", "cor": "ambar",
                  "itens": ["marcador, não desfecho", "depende de dose, vitamina C e carga no tendão", "sem exercício, é só proteína", "incompleta: não conta como proteína do dia"]},
          "destaque": "Tendinopatia e a carga que a trata ficam no módulo de fisioterapia esportiva e reabilitação.",
          "destaque_cor": "tinta", "fonte": "American Journal of Clinical Nutrition 2017"})

# 11. condutas
S.append({"id": "condutas", "tipo": "tabela", "eyebrow": "Os três do começo", "titulo": "O problema real e a conduta",
          "cab": ["Perfil", "Problema real", "Conduta"],
          "larguras": [22, 34, 44],
          "linhas": [["Comprou whey", "nenhum: acima do teto", "o pote não acrescenta; como conveniência, tudo bem"],
                     ["Recusa whey", "total baixo, distribuição torta", "comida no café da manhã; se não couber, um shake"],
                     ["Toma BCAA", "falta carboidrato no treino longo", "carboidrato durante; proteína nas refeições"]],
          "destaque": "Quem mais se beneficiaria é quem acha que o produto não é para ela. Não é para ficar grande: é músculo e função.",
          "destaque_cor": "petr"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Três regras", "titulo": "Quanta proteína você come, e em quantas refeições?",
          "regras": ["Comida em pó: entra com obstáculo, sai quando ele some",
                     "Concentrado para a maioria; isolado para lactose",
                     "BCAA, leucina e glutamina não se sustentam; colágeno depende de carga"],
          "cards": [{"t": "Nutricionista", "x": "Necessidade, fonte e indicação do pó."},
                    {"t": "Médico", "x": "Rim, fígado, medicação: quem descarta é o exame."},
                    {"t": "Educador físico e preparador", "x": "Veem a pergunta primeiro."}],
          "quem": "A melhor resposta ao pedido de pote é uma pergunta."})

spec = {"arquivo": "aulas/MOD05/05-06-proteina-em-po-e-aminoacidos.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Proteína em pó e aminoácidos", "subtitulo": "Tipos, indicação e o limite dos aminoácidos isolados",
        "nota_capa": "Entra pelo erro de categoria.",
        "secoes": {"categoria": ["O erro, o efeito e os obstáculos.", "capa"],
                   "tipos": ["Tipos, fraude e aminoácidos isolados.", "tipos"],
                   "prateleira": ["O resto da prateleira e as condutas.", "prateleira"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-06.json"), "w"), ensure_ascii=False, indent=1)
print("05-06.json:", len(S), "slides")
