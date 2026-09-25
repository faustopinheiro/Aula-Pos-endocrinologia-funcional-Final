"""Spec do deck 5.9. Gera 05-09.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a inversão
S.append({"id": "inversao", "tipo": "frase", "fundo": "tinta", "eyebrow": "O que não está escrito no rótulo",
          "frase": "Uma promessa falsa custa dinheiro. Uma substância não declarada pode custar uma carreira.",
          "apoio": "E, às vezes, a saúde. A aula anterior leu o rótulo; esta trata do que está no pote sem estar no rótulo."})

# 2. três posições
S.append({"id": "situacoes", "tipo": "cards", "por_linha": 3, "eyebrow": "Três situações típicas", "titulo": "Depois, durante e antes",
          "cards": [{"t": "Depois", "x": "a atleta testou positivo; “comprei em loja, com nota fiscal”", "cor": "verm"},
                    {"t": "Durante", "x": "o jogador toma fórmula manipulada, “feita sob medida”", "cor": "ambar"},
                    {"t": "Antes", "x": "a nutricionista precisa escolher a marca para três atletas testados", "cor": "petr"}],
          "destaque": "Esta aula é o procedimento do antes, porque é o único que funciona.",
          "destaque_cor": "tinta"})

# 3. Geyer
S.append({"id": "geyer", "tipo": "numeros", "eyebrow": "Geyer e colaboradores, 2004", "titulo": "634 suplementos não hormonais",
          "numeros": [{"n": "14,8%", "x": "com esteroide anabolizante não declarado, sobretudo pró-hormônio", "cor": "verm"},
                      {"n": "21,1%", "x": "nos produtos de empresas que também vendiam pró-hormônio", "cor": "ambar"},
                      {"n": "9,6%", "x": "nos de empresas que não vendiam", "cor": "petr"}],
          "destaque": "A companhia que o produto mantém importa, e é uma das poucas coisas que dá para checar de fora.",
          "destaque_cor": "tinta", "fonte": "13 países, 215 fornecedores · International Journal of Sports Medicine 2004"})

# 4. depois e no Brasil
S.append({"id": "brasil", "tipo": "duas", "eyebrow": "Martínez-Sanz, 2017 · Torres, 2024", "titulo": "Depois de Geyer, e aqui",
          "esq": {"t": "A revisão", "cor": "ambar",
                  "itens": ["contaminação por substância proibida entre 12% e 58%", "faixa larga: estudos heterogêneos", "até o limite inferior é alto demais para ignorar"]},
          "dir": {"t": "O laboratório brasileiro, 2017 a 2022", "cor": "verm",
                  "itens": ["diuréticos: os adulterantes mais comuns", "estimulantes: mais nos industrializados", "anabolizantes: mais nos manipulados"]},
          "destaque": "Guarde a última linha: ela contradiz a intuição do jogador.",
          "destaque_cor": "verm", "fonte": "Nutrients 2017 · Drug Testing and Analysis 2024"})

# 5. quatro rotas
S.append({"id": "rotas", "tipo": "lista", "eyebrow": "Por que acontece", "titulo": "Quatro rotas",
          "itens": [{"t": "Contaminação cruzada", "x": "mesma linha de produção; a quantidade não precisa ter efeito, só ser detectável", "cor": "ambar"},
                    {"t": "Adulteração deliberada", "x": "remédio posto para o produto “funcionar”, sem declarar", "cor": "verm"},
                    {"t": "Matéria-prima", "x": "insumo a granel, importado, que o fabricante final não testa", "cor": "ambar"},
                    {"t": "Enquadramento regulatório", "x": "suplemento é alimento: não há teste de rotina de cada lote para o esporte", "cor": "tinta"}],
          "destaque": "Não existe suplemento com risco zero. Existe risco menor e risco maior.",
          "destaque_cor": "verm", "gap_itens": 18})

# 6. responsabilidade
S.append({"id": "responsabilidade", "tipo": "duas", "eyebrow": "Responsabilidade estrita", "titulo": "Nota fiscal não protege",
          "esq": {"t": "O atleta", "cor": "verm",
                  "itens": ["responde pelo que está no corpo, sem prova de intenção", "rótulo e boa-fé não protegem sozinhos", "reduzir a sanção exige demonstrar a origem", "pote, lote, compra e análise do produto"]},
          "dir": {"t": "Quem indicou", "cor": "ambar",
                  "itens": ["responde pela indicação", "o código prevê consequência para o pessoal de apoio", "fora do esporte, o risco é à saúde", "estimulante com arritmia; diurético com anti-hipertensivo"]},
          "destaque": "Se você não sabe checar o produto, não indique o produto.",
          "destaque_cor": "tinta"})

# 7. seis passos
p = [svg_abre(1664, 260, "Seis passos em sequência: precisa mesmo, categoria de risco, fabricante, lote certificado, registro e guarda, revisão a cada compra"),
     "<defs>" + seta_marker("q1", MUDO) + "</defs>"]
rs = []
passos = [("1", "precisa mesmo?"), ("2", "a categoria é de risco?"), ("3", "quem fabrica?"),
          ("4", "o lote é certificado?"), ("5", "registrou e guardou?"), ("6", "revisou nesta compra?")]
for i, (n, t) in enumerate(passos):
    x = i * 282
    cor = OXID if i == 0 else (AZUL if i == 3 else TINTA)
    fundo = OXID_T if i == 0 else (AZUL_T if i == 3 else CARTAO)
    p.append(caixa(x, 40, 240, 180, cor, fundo, esp=4 if i in (0, 3) else 2))
    rs.append(rot(x, 58, n, w=240, tam=48, cor=cor, peso=700, alinha="center"))
    rs.append(rot(x + 14, 128, t, w=212, tam=26, cor=TINTA, peso=600, alinha="center"))
    if i < 5:
        p.append(f'<line x1="{x+246}" y1="130" x2="{x+276}" y2="130" stroke="{MUDO}" stroke-width="4" marker-end="url(#q1)"/>')
p.append("</svg>")
S.append({"id": "passos", "tipo": "diagrama", "h": 260, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O procedimento", "titulo": "Seis perguntas, na ordem",
          "destaque": "O produto que não é usado tem risco zero. Num atleta testado, reduzir o número de produtos é a principal medida de segurança.",
          "destaque_cor": "petr"})

# 8. categoria e fabricante
S.append({"id": "categoria", "tipo": "tabela", "eyebrow": "Passos dois e três", "titulo": "Categoria e fabricante",
          "cab": ["", "Risco menor", "Risco maior"],
          "larguras": [18, 41, 41],
          "linhas": [["Categoria", "um ingrediente: creatina, proteína, carboidrato, eletrólito", "pré-treino, termogênico, “hormonal”, emagrecedor, fórmula complexa"],
                     ["Fabricante", "planta própria, boas práticas, rastreabilidade", "também vende apelo hormonal ou pró-hormônio"],
                     ["Compra", "canal com fabricante identificável", "marketplace, importação por conta própria"]],
          "destaque": "É a lista da primeira aula do módulo, agora lida como mapa de risco.",
          "destaque_cor": "ambar"})

# 9. lote
S.append({"id": "lote", "tipo": "duas", "eyebrow": "Passos quatro, cinco e seis", "titulo": "A certificação é do lote, não da marca",
          "esq": {"t": "O que ela faz", "cor": "petr",
                  "itens": ["terceiro independente analisa o lote", "procura substâncias proibidas no esporte", "confere-se pelo número do lote na embalagem", "é a melhor ferramenta que existe"]},
          "dir": {"t": "O que ela não faz", "cor": "verm",
                  "itens": ["não zera o risco: amostra e painel", "não vale para o lote seguinte", "não substitui registro e guarda", "não acompanha troca de fórmula"]},
          "destaque": "Anotar marca, lote e validade, fotografar o rótulo e guardar a embalagem custa dois minutos. Revisar a cada compra, não a cada temporada.",
          "destaque_cor": "tinta"})

# 10. cenário brasileiro
S.append({"id": "cenario", "tipo": "tabela", "eyebrow": "O cenário brasileiro", "titulo": "Três origens, três condutas",
          "cab": ["Origem", "O que se sabe", "Atleta testado"],
          "larguras": [20, 46, 34],
          "linhas": [["Industrializado", "estimulantes mais frequentes; certificação rara e cara", "lista mínima; lote certificado quando houver"],
                     ["Manipulado", "anabolizantes mais frequentes; lote único, sem certificação", "não"],
                     ["Importado por conta própria", "sem registro, sem fabricante, sem origem demonstrável", "não"]],
          "destaque": "Regular perante a Anvisa não é o mesmo que seguro para quem é testado. São duas perguntas diferentes.",
          "destaque_cor": "verm"})

# 11. três condutas
S.append({"id": "condutas", "tipo": "tabela", "eyebrow": "As três situações", "titulo": "Três condutas",
          "cab": ["Situação", "Conduta"],
          "larguras": [22, 78],
          "linhas": [["Depois", "reunir embalagem, lote, nota e histórico; listar tudo o que usou; apoio jurídico e via formal"],
                     ["Durante", "o que há na fórmula, quem prescreveu, por quê; se testado, não; se hormonal, outra conversa"],
                     ["Antes", "lista mínima; um ingrediente; fabricante identificável; lote certificado; planilha da equipe"]],
          "destaque": "“Nenhum produto é risco zero. O que a gente pode fazer é escolher o risco menor e documentar tudo.”",
          "destaque_cor": "petr"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O procedimento do antes", "titulo": "Quem não sabe checar o produto não indica o produto",
          "regras": ["Precisa mesmo? A categoria é de risco? Quem fabrica?",
                     "O lote é certificado? Registrou e guardou?",
                     "Revisou nesta compra?"],
          "cards": [{"t": "Nutricionista", "x": "Escolhe e indica; no atleta testado, decisão de equipe com registro."},
                    {"t": "Médico", "x": "Sintoma, interação, suspeita de substância não declarada."},
                    {"t": "Preparador, técnico, fisioterapeuta", "x": "Levam a informação e o pote; nunca endossam."}],
          "quem": "A regra vale para todos, sem exceção."})

spec = {"arquivo": "aulas/MOD05/05-09-contaminacao-de-suplementos-e-certificacao-de-lote.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Contaminação de suplementos", "subtitulo": "Rotas, responsabilidade e certificação de lote",
        "nota_capa": "Entra pela inversão do problema.",
        "secoes": {"inversao": ["O problema, em números e rotas.", "capa"],
                   "responsabilidade": ["Responsabilidade e o procedimento.", "responsabilidade"],
                   "cenario": ["O Brasil e as três condutas.", "cenario"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-09.json"), "w"), ensure_ascii=False, indent=1)
print("05-09.json:", len(S), "slides")
