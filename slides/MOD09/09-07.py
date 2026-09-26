"""Spec do deck 9.7. Gera 09-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

S.append({"id": "coletes", "tipo": "frase", "fundo": "tinta", "eyebrow": "Seis coletes emprestados",
          "frase": "Uma pilha de relatórios e nenhuma conclusão.",
          "apoio": "Um time amador passa a usar GPS nos treinos de terça e quinta. Distância, velocidade máxima, sprints, acelerações. O mesmo vale para quem atende o indivíduo: todo relógio esportivo já é um GPS."})

S.append({"id": "externa", "tipo": "duas", "eyebrow": "Erro um", "titulo": "Tratar o que foi feito como se fosse o que custou",
          "esq": {"t": "Carga externa", "cor": "tinta",
                  "itens": ["distância, velocidade, acelerações", "igual para qualquer pessoa", "é o que o GPS mede"]},
          "dir": {"t": "Carga interna", "cor": "petr",
                  "itens": ["o custo daquilo para aquela pessoa", "muda com sono, turno, calor, cansaço", "não está no relatório"]},
          "destaque": "Complementares. A informação útil vem da relação entre as duas.",
          "destaque_cor": "tinta", "fonte": "Consenso de monitoramento de carga, Int J Sports Physiol Perform 2017"})

# mesma distância, custos diferentes
p = [svg_abre(1664, 300, "Dois jogadores com a mesma distância e percepções de esforço diferentes, nove e cinco")]
for i, (nota, c) in enumerate([(9, FOSF), (5, OXID)]):
    y = 40 + i * 130
    p.append(f'<rect x="300" y="{y}" width="700" height="60" rx="6" fill="{GRADE}"/>')
    p.append(f'<rect x="1100" y="{y}" width="{nota * 50}" height="60" rx="6" fill="{c}"/>')
p.append("</svg>")
rs = [rot(40, 55, "Jogador A", w=240, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(40, 185, "Jogador B", w=240, tam=26, cor=TINTA, peso=700, alinha="right"),
      rot(300, 55, "mesma distância no jogo", w=700, tam=24, cor=TINTA, alinha="center"),
      rot(300, 185, "mesma distância no jogo", w=700, tam=24, cor=TINTA, alinha="center"),
      rot(1100, 10, "percepção de esforço", w=500, tam=22, cor=MUDO),
      rot(1100 + 9 * 50 + 16, 52, "9", w=80, tam=34, cor=FOSF, peso=700),
      rot(1100 + 5 * 50 + 16, 182, "5", w=80, tam=34, cor=OXID, peso=700)]
S.append({"id": "razao", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A correção do erro um", "titulo": "O mesmo trabalho, custos diferentes",
          "destaque": "Quando o mesmo trabalho passa a custar mais, algo mudou na pessoa, e costuma aparecer antes de o desempenho cair.",
          "destaque_cor": "tinta", "fonte": "Esquema, sem valores medidos"})

S.append({"id": "amostragem", "tipo": "duas", "eyebrow": "Erro dois", "titulo": "Comparar números de aparelhos diferentes",
          "esq": {"t": "O motivo técnico", "cor": "tinta",
                  "itens": ["cada aparelho registra a posição algumas vezes por segundo", "quem registra pouco corta os cantos", "subestima o que é curto e intenso"]},
          "dir": {"t": "O que o estudo mostrou", "cor": "petr",
                  "itens": ["5 contra 10 registros por segundo, contra um laser", "os de 10: mais válidos e confiáveis", "sobretudo em aceleração e desaceleração"]},
          "destaque": "Trocou de fornecedor ou de relógio: a série começa de novo.",
          "destaque_cor": "tinta", "fonte": "J Sports Sci 2012"})

S.append({"id": "limiar", "tipo": "cards", "por_linha": 2, "eyebrow": "Erro três", "titulo": "Comparar números sem olhar o limiar",
          "cards": [{"t": "Cada fabricante, um limiar", "x": "“alta intensidade” começa onde o aparelho, ou o usuário, definiu", "cor": "ambar"},
                    {"t": "Absoluto ou relativo", "x": "o mesmo limiar fixo é máximo para um e trote para outro", "cor": "ambar"}],
          "destaque": "Sem o limiar escrito, o número não se compara com nada.",
          "destaque_cor": "verm", "fonte": "Revisão sistemática, Sports Med 2013"})

S.append({"id": "campo", "tipo": "frase", "fundo": "tinta", "eyebrow": "A ideia da aula",
          "frase": "O GPS mede muito bem o que está dentro do campo de visão dele. Quem decide para onde apontar é você.",
          "apoio": "Os dois próximos erros são sobre o que fica fora desse campo."})

S.append({"id": "acelerometro", "tipo": "duas", "eyebrow": "Erro quatro", "titulo": "Ler o acelerômetro como carga no tecido",
          "esq": {"t": "O que ele mede", "cor": "petr",
                  "itens": ["soma de acelerações em três eixos", "saltos, impactos, mudanças de direção", "diz mais que a distância para goleiro e futsal"]},
          "dir": {"t": "O que ele não mede", "cor": "verm",
                  "itens": ["a força que atravessa o tendão", "a carga na articulação", "carga mecânica e fisiológica seguem caminhos diferentes"]},
          "destaque": "É volume de movimento, não estresse de tecido.",
          "destaque_cor": "tinta", "fonte": "Revisão, Sports Med 2017"})

S.append({"id": "fora", "tipo": "cards", "por_linha": 3, "eyebrow": "Erro cinco", "titulo": "Medir só o que o colete vê",
          "cards": [{"t": "Terça e quinta", "x": "com colete; medido muito bem", "cor": "petr"},
                    {"t": "O trabalho em turno", "x": "esforço alto em treino que o grupo achava moderado", "cor": "ambar"},
                    {"t": "O sábado", "x": "metade do elenco jogava outra partida, sem ninguém contar", "cor": "verm"}],
          "destaque": "A correção foi uma pergunta na segunda-feira: “jogou no fim de semana? quantos minutos?”",
          "destaque_cor": "tinta"})

S.append({"id": "vale", "tipo": "duas", "eyebrow": "Onde vale o que custa", "titulo": "O retorno de lesão, e a pergunta antes de comprar",
          "esq": {"t": "Onde o GPS paga", "cor": "petr",
                  "itens": ["retorno de lesão muscular", "que fração da própria velocidade máxima", "em que volume, com progressão documentada"]},
          "dir": {"t": "Antes de comprar coletes", "cor": "ambar",
                  "itens": ["que decisão isso vai mudar?", "o mesmo dinheiro compra saúde em outro lugar?"]},
          "destaque_cor": "tinta", "destaque": "Conversa com a exposição à velocidade máxima da aula de velocidade."})

S.append({"id": "pulso", "tipo": "cards", "por_linha": 2, "eyebrow": "O GPS que o paciente já tem", "titulo": "De graça, no pulso",
          "cards": [{"t": "O uso mais valioso", "x": "classificar a semana em fácil, moderado e forte, e ver a distribuição", "cor": "petr"},
                    {"t": "O cuidado", "x": "celular erra mais; prédios e trilha fechada também. Serve para tendência, não para comparar tiros", "cor": "ambar"}],
          "destaque": "É o diagnóstico da zona cinzenta, visto pelo relógio.",
          "destaque_cor": "tinta"})

S.append({"id": "correcoes", "tipo": "tabela", "eyebrow": "Os cinco erros", "titulo": "E a correção de cada um",
          "cab": ["Erro", "Correção"],
          "larguras": [44, 56],
          "linhas": [["Carga externa tomada como carga", "percepção de esforço ao lado de cada linha"],
                     ["Aparelhos diferentes comparados", "série nova a cada troca"],
                     ["Limiar esquecido", "limiar escrito em todo relatório"],
                     ["Acelerômetro lido como estresse de tecido", "tratá-lo como volume de movimento"],
                     ["Só o que o colete vê", "perguntar pelo que aconteceu fora dele"]]})

S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Carga externa", "titulo": "O GPS mede o que está no campo de visão dele",
          "regras": ["A informação boa está na relação com o custo",
                     "Aparelhos e limiares diferentes não se comparam",
                     "Boa parte da carga acontece fora do colete"],
          "cards": [{"t": "Preparação física", "x": "Lê o relatório com o limiar e a nota ao lado."},
                    {"t": "Fisioterapia", "x": "Usa a velocidade máxima no retorno de lesão."},
                    {"t": "Atleta", "x": "Conta o jogo de sábado e o turno de trabalho."}],
          "quem": "Próxima aula: carga interna, percepção de esforço, frequência cardíaca e questionários."})

spec = {"arquivo": "aulas/MOD09/09-07-carga-externa-gps-e-metricas-de-campo.md",
        "modulo": "Preparação Física, Treinamento e Gestão de Carga", "tema": "tinta",
        "titulo": "Carga externa: GPS e métricas de campo", "subtitulo": "Cinco erros ao ler o relatório",
        "nota_capa": "Entra por um time amador com coletes emprestados.",
        "secoes": {"coletes": ["A cena e o primeiro erro.", "capa"],
                   "amostragem": ["Aparelhos e limiares.", "amostragem"],
                   "acelerometro": ["Acelerômetro e o que fica fora.", "acelerometro"],
                   "vale": ["Onde vale, o relógio e as correções.", "vale"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "09-07.json"), "w"), ensure_ascii=False, indent=1)
print("09-07.json:", len(S), "slides")
