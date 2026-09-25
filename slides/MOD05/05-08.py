"""Spec do deck 5.8. Gera 05-08.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o erro de leitura
S.append({"id": "aparencia", "tipo": "frase", "fundo": "tinta", "eyebrow": "O erro é de leitura",
          "frase": "A promessa moderna não mente de forma grosseira. Ela se parece com ciência.",
          "apoio": "Vem com estudo, referência, mecanismo e gráfico. O erro não é do paciente: é confundir a aparência de ciência com ciência, e o profissional também comete."})

# 2. três situações
S.append({"id": "situacoes", "tipo": "cards", "por_linha": 3, "eyebrow": "Três situações típicas", "titulo": "Resposta para hoje",
          "cards": [{"t": "O estimulante de testosterona", "x": "dez ingredientes, um estudo citado no rótulo; “posso tomar junto?”", "cor": "ambar"},
                    {"t": "O termogênico", "x": "indicado por uma amiga; começou a ter palpitação", "cor": "verm"},
                    {"t": "O estudo do laboratório", "x": "a colega fisioterapeuta pergunta sobre um produto de recuperação", "cor": "petr"}],
          "destaque": "“Não tem evidência” não é resposta suficiente para nenhum dos três.",
          "destaque_cor": "tinta"})

# 3. a escada
p = [svg_abre(1664, 400, "Escada de seis degraus de evidência; a promessa sai do primeiro degrau e salta direto para a conclusão"),
     "<defs>" + seta_marker("p1", FOSF) + "</defs>"]
rs = []
degraus = ["mecanismo plausível", "estudo em célula", "estudo em animal", "marcador em humano", "ensaio pequeno sem controle", "ensaio controlado com desfecho"]
for i, t in enumerate(degraus):
    x, y = 20 + i * 232, 310 - i * 40
    forte = i == 5
    p.append(caixa(x, y, 220, 84, OXID if forte else MUDO, OXID_T if forte else CLARO, esp=4 if forte else 2, rx=8))
    rs.append(rot(x + 8, y + 12, t, w=204, tam=22, cor=OXID if forte else TINTA, peso=700 if forte else 500, alinha="center"))
p.append(caixa(1440, 100, 204, 84, FOSF, FOSF_T, esp=4, rx=8))
p.append(f'<path d="M130,304 C380,-20 1100,-20 1432,130" fill="none" stroke="{FOSF}" stroke-width="4" stroke-dasharray="14 10" marker-end="url(#p1)"/>')
p.append("</svg>")
rs += [rot(1440, 124, "“funciona”", w=204, tam=30, cor=FOSF, peso=700, alinha="center"),
       rot(1084, 4, "a promessa salta os degraus do meio", w=560, tam=26, cor=FOSF, peso=700, alinha="right")]
S.append({"id": "escada", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O movimento central", "titulo": "Em que degrau está a afirmação?",
          "destaque": "Desmontar é devolver os degraus que a promessa pulou. Não é desconfiar de tudo.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

# 4. seis peças
S.append({"id": "pecas", "tipo": "lista", "eyebrow": "A anatomia da promessa", "titulo": "Seis peças, quase sempre nesta ordem",
          "itens": [{"t": "Mecanismo plausível", "x": "a frase costuma ser verdadeira; plausibilidade não é efeito", "cor": "petr"},
                    {"t": "Um estudo que existe", "x": "a pergunta muda de “tem estudo?” para “que estudo?”", "cor": "petr"},
                    {"t": "Desfecho substituto", "x": "mediu marcador; o anúncio vende desempenho", "cor": "ambar"},
                    {"t": "Dose e população extrapoladas", "x": "dose maior que a do pote; gente que não é o seu paciente", "cor": "ambar"},
                    {"t": "Prova social", "x": "depoimento, antes e depois, atleta conhecido", "cor": "verm"},
                    {"t": "Autoridade e urgência", "x": "“patenteado”, “últimas unidades”: a peça que impede de pensar", "cor": "verm"}],
          "gap_itens": 12})

# 5. fraquezas
S.append({"id": "fraquezas", "tipo": "duas", "eyebrow": "Quando existe um estudo", "titulo": "Cinco fraquezas, três expressões vazias",
          "esq": {"t": "O estudo citado", "cor": "ambar",
                  "itens": ["amostra pequena: gera hipótese, não conduta", "sem placebo ou sem cegamento", "marcador no lugar de desfecho", "único estudo do fabricante, sem replicação", "resumo de congresso que nunca virou artigo"]},
          "dir": {"t": "O rótulo", "cor": "verm",
                  "itens": ["“clinicamente testado”: não diz o resultado", "“fórmula patenteada”: propriedade, não eficácia", "“natural”: digitálico também é"]},
          "destaque": "Patrocínio não invalida um estudo; a pesquisa da creatina também tem indústria. O problema é a fonte única.",
          "destaque_cor": "tinta"})

# 6. Clemesha
S.append({"id": "clemesha", "tipo": "numeros", "eyebrow": "Clemesha e colaboradores, 2020", "titulo": "Cinquenta estimulantes de testosterona",
          "numeros": [{"n": "90%", "x": "dos produtos prometem aumentar a testosterona", "cor": "verm"},
                      {"n": "8,3", "x": "ingredientes por produto, em média; 109 ingredientes diferentes", "cor": "ambar"},
                      {"n": "27 de 109", "x": "ingredientes com algum estudo mostrando aumento; 11 mostrando queda; 67 sem estudo", "cor": "petr"}],
          "destaque": "Vários produtos traziam zinco, vitamina B3 ou magnésio acima do limite superior tolerável.",
          "destaque_cor": "tinta", "fonte": "World Journal of Men’s Health 2020"})

# 7. categorias
S.append({"id": "categorias", "tipo": "tabela", "eyebrow": "O que mais chega ao consultório", "titulo": "Quatro prateleiras",
          "cab": ["Categoria", "O que se sabe", "O que dizer"],
          "larguras": [22, 40, 38],
          "linhas": [["Testosterona", "tribulus: sem mudança hormonal em ensaio controlado", "o sintoma é que se investiga"],
                     ["Termogênico", "o que age costuma ser cafeína, somada a outros estimulantes", "palpitação, insônia, pressão alta"],
                     ["Detox", "sem mecanismo; efeito diurético ou laxativo", "fígado e rim fazem o trabalho"],
                     ["Recuperação e articulação", "grupo B: colágeno, curcumina, cereja azeda", "“ainda não se sabe o suficiente”"]],
          "destaque": "Nem tudo na prateleira é igual. Tratar tudo como charlatanismo é tão impreciso quanto tratar tudo como promissor.",
          "destaque_cor": "petr", "fonte": "Tribulus: Neychev e Mitev, Journal of Ethnopharmacology 2005"})

# 8. quatro passos
S.append({"id": "passos", "tipo": "lista", "eyebrow": "Como dizer", "titulo": "Quem só diz não perde o paciente para quem diz sim",
          "itens": [{"t": "Validar a pergunta, não o produto", "x": "“isso é um problema real, e a gente vai resolver”", "cor": "petr"},
                    {"t": "Ensinar o critério", "x": "“vinte pessoas, mediu um marcador, dose maior que a do pote”", "cor": "petr"},
                    {"t": "Oferecer o que responde", "x": "cansaço: sono, energia total, ferro, carga de treino", "cor": "ambar"},
                    {"t": "Negociar, quando couber", "x": "“mantenha, e em oito semanas a gente olha o que mudou”", "cor": "ambar"}],
          "gap_itens": 22})

# 9. negocia ou não
S.append({"id": "negocia", "tipo": "duas", "eyebrow": "Escolha as batalhas", "titulo": "Quando negociar, e quando não",
          "esq": {"t": "Negocia", "cor": "petr",
                  "itens": ["produto inócuo", "barato", "pessoa decidida", "e o que muda o caso está sendo feito"]},
          "dir": {"t": "Não negocia", "cor": "verm",
                  "itens": ["estimulante com doença cardiovascular ou sintoma", "origem duvidosa, ou algo que pareça hormônio", "custo alto para quem não tem sobrando", "substitui um tratamento que funciona"]},
          "destaque": "Aí a resposta é não, firme, com o motivo dito em voz alta.",
          "destaque_cor": "verm"})

# 10. cartão de bolso
S.append({"id": "alertas", "tipo": "cards", "por_linha": 3, "eyebrow": "Três ou mais, e a conversa muda de tom", "titulo": "O cartão de bolso",
          "cards": [{"t": "Promete tudo", "x": "emagrece, dá energia, melhora o sono", "cor": "ambar"},
                    {"t": "Dose escondida", "x": "fórmula patenteada, sem dose por item", "cor": "ambar"},
                    {"t": "Lista longa", "x": "muitos ingredientes ativos", "cor": "ambar"},
                    {"t": "Degrau baixo", "x": "célula, animal ou marcador", "cor": "ambar"},
                    {"t": "Fonte única", "x": "só o fabricante, sem replicação", "cor": "ambar"},
                    {"t": "Dose que não bate", "x": "o pote e o estudo não conversam", "cor": "ambar"},
                    {"t": "Depoimento", "x": "antes e depois no lugar da técnica", "cor": "ambar"},
                    {"t": "Urgência", "x": "escassez, prazo, marketing de rede", "cor": "ambar"},
                    {"t": "Efeito de remédio", "x": "sinal de substância não declarada", "cor": "verm"}]})

# 11. as três respostas
S.append({"id": "respostas", "tipo": "tabela", "eyebrow": "As três situações do começo", "titulo": "Três respostas",
          "cab": ["Situação", "Resposta"],
          "larguras": [26, 74],
          "linhas": [["Estimulante de testosterona", "valida o sintoma, ensina o critério, investiga sono, energia e carga; pote só se não houver estimulante"],
                     ["Termogênico com palpitação", "sem negociação: suspende, avaliação médica, o pote vai junto à consulta"],
                     ["Estudo do laboratório", "o método, não o veredito: quantos, placebo, desfecho, dose, quem financiou, quem replicou"]],
          "destaque": "Grupo B é “pode ser, ainda não se sabe”, que é diferente de “não funciona”. E a clínica vai vender o produto?",
          "destaque_cor": "ambar"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Um procedimento, não desconfiança", "titulo": "Seis peças, cinco fraquezas, nove alertas, quatro passos",
          "regras": ["Devolver os degraus que a promessa pulou",
                     "Ensinar o critério vale mais que dar o veredito",
                     "Negociar o inócuo; nunca o risco, o custo alto ou a troca de tratamento"],
          "cards": [{"t": "Nutricionista", "x": "Avalia e indica suplemento."},
                    {"t": "Médico", "x": "Interação, sintoma e risco."},
                    {"t": "Educador físico e preparador", "x": "Ouvem a promessa primeiro, no vestiário."}],
          "quem": "Desmontar uma promessa é de todos."})

spec = {"arquivo": "aulas/MOD05/05-08-suplementos-sem-evidencia-como-desmontar-uma-promessa.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Suplementos sem evidência", "subtitulo": "Anatomia de uma promessa comercial e como respondê-la",
        "nota_capa": "Entra pelo erro de leitura.",
        "secoes": {"aparencia": ["O erro, a escada e as seis peças.", "capa"],
                   "fraquezas": ["O estudo citado e as prateleiras.", "fraquezas"],
                   "passos": ["Como dizer, o cartão e as três respostas.", "passos"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-08.json"), "w"), ensure_ascii=False, indent=1)
print("05-08.json:", len(S), "slides")
