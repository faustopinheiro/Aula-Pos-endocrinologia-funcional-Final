"""Spec do deck 3.10. Gera 03-10.json ao lado deste arquivo."""
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

# 1. enquadramento: o músculo que recebe e o músculo que fala
p = [svg_abre(1664, 420, "À esquerda, testosterona, cortisol, T3 e insulina chegam ao músculo; à direita, o mesmo músculo manda sinais para fígado, tecido adiposo, osso, cérebro, pâncreas e sistema imune"),
     "<defs>" + seta_marker("e1", MUDO) + seta_marker("e2", OXID) + "</defs>"]
rs = []
hs = ["testosterona", "cortisol", "T3", "insulina"]
for i, h in enumerate(hs):
    y = 40 + i * 95
    p.append(seta(250, y + 20, 430, 210, MUDO, "e1", esp=4))
    rs.append(rot(0, y, h, w=240, tam=26, cor=APOIO2, alinha="right"))
p.append(caixa(450, 150, 260, 120, MUDO, CLARO, esp=3))
rs.append(rot(450, 190, "músculo", w=260, tam=30, cor=TINTA, peso=700, alinha="center"))
p.append(f'<line x1="832" y1="10" x2="832" y2="410" stroke="{GRADE}" stroke-width="3" stroke-dasharray="10 8"/>')
p.append(caixa(960, 150, 260, 120, OXID, OXID_T, esp=4))
rs.append(rot(960, 190, "músculo", w=260, tam=30, cor=TINTA, peso=700, alinha="center"))
orgs = ["fígado", "tecido adiposo", "osso", "cérebro", "pâncreas", "sistema imune"]
for i, o in enumerate(orgs):
    y = 20 + i * 70
    p.append(seta(1230, 210, 1370, y + 18, OXID, "e2", esp=4))
    rs.append(rot(1390, y, o, w=274, tam=26, cor=TINTA, peso=600))
p.append("</svg>")
rs += [rot(0, 0, "", w=10)]
S.append({"id": "enquadramento", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs[:-1],
          "eyebrow": "O erro de enquadramento", "titulo": "O músculo recebe ordens. E também fala",
          "destaque": "A figura clássica não está errada. Está pela metade: falta a seta que sai.",
          "destaque_cor": "petr", "fonte": "Pedersen e Febbraio, Physiological Reviews 2008"})

# 2. a escala: IL-6 contra noradrenalina
p = [svg_abre(1664, 300, "Aumento sobre o repouso: noradrenalina perto de 12 vezes no esforço intenso; interleucina-6 até 100 vezes no exercício prolongado")]
x0, esc = 360, 12.8
barras = [("noradrenalina", 12, "≈ 12×", AZUL, "esforço intenso"), ("interleucina-6", 100, "até 100×", OXID, "exercício prolongado")]
rs = []
for i, (nome, v, txt, cor, sub) in enumerate(barras):
    y = 40 + i * 130
    p.append(f'<rect x="{x0}" y="{y}" width="{v*esc:.0f}" height="80" rx="4" fill="{cor}"/>')
    rs.append(rot(0, y + 8, nome, w=340, tam=30, cor=TINTA, peso=700, alinha="right"))
    rs.append(rot(0, y + 46, sub, w=340, tam=22, cor=MUDO, alinha="right"))
    if v * esc > 400:
        rs.append(rot(x0 + v * esc - 300, y + 20, txt, w=280, tam=32, cor="#FFFFFF", peso=700, alinha="right"))
    else:
        rs.append(rot(x0 + v * esc + 20, y + 20, txt, w=200, tam=32, cor=TINTA, peso=700))
p.append(f'<line x1="{x0}" y1="20" x2="{x0}" y2="290" stroke="{TINTA}" stroke-width="3"/>')
p.append("</svg>")
S.append({"id": "escala", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número que chamou a atenção", "titulo": "Uma citocina subindo cem vezes",
          "destaque": "A leitura óbvia: exercício lesa o músculo, e a inflamação sobe. É razoável. E está errada.",
          "destaque_cor": "verm", "fonte": "Aumento sobre o repouso · noradrenalina: aula das catecolaminas · IL-6: Pedersen e Febbraio 2008"})

# 3. dois problemas
S.append({"id": "trabalho", "tipo": "duas", "eyebrow": "O que desmontou a leitura", "titulo": "Sinal de trabalho, não de lesão",
          "esq": {"t": "Se fosse lesão", "cor": "ambar",
                  "itens": ["o TNF sobe antes e puxa a IL-6", "a IL-6 acompanha o dano",
                            "o excêntrico, que lesa mais, daria mais IL-6"]},
          "dir": {"t": "O que se mediu", "cor": "petr",
                  "itens": ["sem TNF na frente", "sai do próprio músculo em contração",
                            "acompanha duração, intensidade e massa envolvida", "sobe mais com o glicogênio baixo"]},
          "destaque": "Steensberg, 2001: na mesma pessoa, a perna com pouco glicogênio liberou mais IL-6. Um sinal de escassez local.",
          "destaque_cor": "tinta", "fonte": "Steensberg e colaboradores, Journal of Physiology 2001 · 7 homens, 5 horas de extensão de joelho"})

# 4. o paradoxo
p = [svg_abre(1664, 400, "A IL-6 que sai do músculo segue dois caminhos: para fígado e tecido adiposo, liberando glicose e gordura; para o sistema imune, subindo IL-1ra e IL-10 e bloqueando a subida do TNF"),
     "<defs>" + seta_marker("p1", GLIC) + seta_marker("p2", OXID) + "</defs>"]
p.append(caixa(0, 130, 380, 140, OXID, OXID_T, esp=4))
p.append(seta(390, 170, 700, 80, GLIC, "p1", esp=5))
p.append(seta(390, 230, 700, 320, OXID, "p2", esp=5))
p.append(caixa(720, 10, 944, 150, GLIC, GLIC_T, esp=3))
p.append(caixa(720, 240, 944, 150, OXID, CARTAO, esp=3))
p.append("</svg>")
rs = [rot(0, 160, "IL-6", w=380, tam=36, cor=TINTA, peso=700, alinha="center"),
      rot(0, 212, "do músculo em contração", w=380, tam=24, cor=TINTA, alinha="center"),
      rot(750, 30, "Metabólico: fígado e tecido adiposo", w=880, tam=28, cor=GLIC, peso=700),
      rot(750, 80, "mais glicose liberada pelo fígado, mais gordura mobilizada", w=880, tam=26, cor=TINTA),
      rot(750, 260, "Imune: o contexto muda o efeito", w=880, tam=28, cor=OXID, peso=700),
      rot(750, 310, "IL-1ra e IL-10 sobem · a subida do TNF some", w=880, tam=26, cor=TINTA)]
S.append({"id": "paradoxo", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Starkie e colaboradores, 2003", "titulo": "Pró-inflamatória no livro, anti-inflamatória no músculo",
          "destaque": "Endotoxina sozinha dobrou ou triplicou o TNF. Com três horas de pedalada, ou com IL-6 infundida, a subida não veio.",
          "destaque_cor": "petr", "fonte": "FASEB Journal 2003 · 8 homens saudáveis"})

# 5. o catálogo com régua
S.append({"id": "catalogo", "tipo": "cards", "por_linha": 3, "eyebrow": "Centenas de candidatas", "titulo": "Separar o estabelecido da promessa",
          "cards": [{"t": "Mais firme em humanos", "x": "IL-6 · o treino de força reduz a miostatina: parte do efeito é soltar um freio", "cor": "petr"},
                    {"t": "Em construção", "x": "IL-15, decorina, apelina, SPARC, catepsina B, BDNF", "cor": "ambar"},
                    {"t": "Controversa", "x": "irisina: um estudo de caso de como ler literatura", "cor": "verm"}],
          "destaque": "BDNF: no remo de quatro horas, o cérebro respondia por 70 a 80% do que circulava. “O músculo manda BDNF ao cérebro” é mais simples que o dado.",
          "destaque_cor": "tinta", "fonte": "Rasmussen e colaboradores, Experimental Physiology 2009"})

# 6. irisina
p = [svg_abre(1664, 400, "Linha do tempo da irisina: 2012, descrita em camundongos; 2015, anticorpos dos kits reagem com outras proteínas; 2015, espectrometria de massas encontra irisina em concentração baixa, maior em treinados")]
p.append(f'<line x1="40" y1="60" x2="1624" y2="60" stroke="{MUDO}" stroke-width="4"/>')
pts = [(40, "2012 · Boström", "FNDC5 vira irisina e “escurece” a gordura branca, em camundongos", GLIC, GLIC_T),
       (585, "2015 · Albrecht", "anticorpos dos kits comerciais reagem com outras proteínas do soro", FOSF, FOSF_T),
       (1130, "2015 · Jedrychowski", "espectrometria de massas, sem anticorpo: a molécula existe", OXID, OXID_T)]
rs = []
for x, t, d, cor, fundo in pts:
    p.append(f'<circle cx="{x + 20}" cy="60" r="16" fill="{cor}"/>')
    p.append(caixa(x, 110, 500, 270, cor, fundo, esp=3))
    rs.append(rot(x + 24, 130, t, w=452, tam=30, cor=cor, peso=700))
    rs.append(rot(x + 24, 190, d, w=452, tam=26, cor=TINTA))
p.append("</svg>")
rs.append(rot(1154, 300, "≈ 3,6 ng/mL sedentários · ≈ 4,3 ng/mL treinados", w=452, tam=24, cor=OXID, peso=700))
S.append({"id": "irisina", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Um estudo de caso de ceticismo", "titulo": "Irisina: exercício em forma de molécula?",
          "destaque": "Existe, circula e muda com o treino. Em disputa: o tamanho da resposta em humanos. Com mercado do outro lado, confira o método de medida.",
          "destaque_cor": "verm", "fonte": "Nature 2012 · Scientific Reports 2015 · Cell Metabolism 2015"})

# 7. para quem o músculo fala + exercinas
S.append({"id": "mapa", "tipo": "cards", "por_linha": 3, "eyebrow": "Para quem o músculo fala", "titulo": "A contração é, ela mesma, um evento endócrino",
          "cards": [{"t": "Fígado", "x": "glicose e gordura hepática, mesmo sem perda de peso", "cor": "tinta"},
                    {"t": "Tecido adiposo", "x": "quebra de gordura, comportamento do adipócito", "cor": "tinta"},
                    {"t": "Osso", "x": "sinal além da carga; sarcopenia e osteoporose juntas", "cor": "tinta"},
                    {"t": "Cérebro", "x": "catepsina B: memória em camundongos; em humanos, correlação", "cor": "ambar"},
                    {"t": "Sistema imune", "x": "tônus inflamatório mais baixo", "cor": "tinta"},
                    {"t": "Pâncreas", "x": "sinais que modulam a célula beta", "cor": "tinta"}],
          "destaque": "Exercina: sinal liberado com o exercício por músculo, coração, fígado ou tecido adiposo. Proteínas, vesículas, microRNAs e metabólitos como o lactato.",
          "destaque_cor": "petr", "fonte": "Moon e colaboradores, Cell Metabolism 2016 · Chow e colaboradores, Nature Reviews Endocrinology 2022"})

# 8. o que muda
S.append({"id": "conduta", "tipo": "lista", "eyebrow": "O que muda na segunda-feira", "titulo": "A balança não mede o que o músculo manda",
          "itens": [{"t": "O benefício não é só gasto calórico", "x": "boa parte acontece em tecido que não se contraiu", "cor": "petr"},
                    {"t": "Quem treina e não emagrece está mudando outra coisa", "x": "a resposta deixa de ser consolo e vira mecanismo", "cor": "petr"},
                    {"t": "Perder músculo é perder um órgão que sinaliza", "x": "o peso novo da sarcopenia e do destreino", "cor": "ambar"},
                    {"t": "Parar não é neutro", "x": "é tirar um recado que o corpo estava recebendo", "cor": "verm"}],
          "gap_itens": 22})

# 9. o que não autoriza
S.append({"id": "frasco", "tipo": "frase", "fundo": "tinta", "eyebrow": "O que o conceito não autoriza",
          "frase": "O que eleva miocina é músculo se contraindo.",
          "apoio": "São dezenas de sinais juntos, em pulsos. Boa parte da ação é local, como a do IGF-1. E o estímulo é a contração: não existe versão dela em frasco."})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "A régua honesta", "titulo": "A molécula é gratuita",
          "regras": ["Sólido: o músculo libera sinais ao se contrair, e há efeito a distância",
                     "Em construção: benefício clínico específico atribuído a molécula específica",
                     "Promessa comercial: qualquer efeito sem a contração"],
          "cards": [{"t": "Educador físico", "x": "Quanta massa entra e por quanto tempo."},
                    {"t": "Nutricionista", "x": "O combustível em que a contração acontece."},
                    {"t": "Fisioterapia e psicologia", "x": "Contração possível na lesão, e a adesão."}],
          "quem": "O médico reconhece o que não melhora sem contração, e para de procurar frasco."})

spec = {"arquivo": "aulas/MOD03/03-10-musculo-como-orgao-endocrino.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "O músculo como órgão endócrino", "subtitulo": "Miocinas, exercinas e os limites da evidência",
        "nota_capa": "Entra pelo erro de enquadramento.",
        "secoes": {"erro": ["O músculo que fala e a IL-6 lida errado.", "enquadramento"],
                   "catalogo": ["O catálogo e a irisina.", "catalogo"],
                   "conduta": ["O que muda e o que não autoriza.", "conduta"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-10.json"), "w"), ensure_ascii=False, indent=1)
print("03-10.json:", len(S), "slides")
