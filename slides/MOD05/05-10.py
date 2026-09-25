"""Spec do deck 5.10. Gera 05-10.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. a pergunta
S.append({"id": "remedio", "tipo": "frase", "fundo": "tinta", "eyebrow": "Decisão clínica, não suplemento",
          "frase": "A pergunta “isso é proibido?” quase nunca chega sobre um pote. Chega sobre um remédio.",
          "apoio": "A lista muda todo ano. O sistema, o raciocínio e o fluxo são estáveis; os itens se conferem na fonte oficial, toda vez."})

# 2. três decisões
S.append({"id": "decisoes", "tipo": "cards", "por_linha": 3, "eyebrow": "Três decisões típicas", "titulo": "Nenhuma resposta é “não”",
          "cards": [{"t": "A nadadora master", "x": "asma, broncodilatador inalatório há anos; campeonato nacional", "cor": "petr"},
                    {"t": "O corredor", "x": "TDAH, metilfenidato do psiquiatra; prova com premiação e controle", "cor": "ambar"},
                    {"t": "A jogadora de vôlei", "x": "infiltração de corticoide indicada duas semanas antes do campeonato", "cor": "verm"}],
          "destaque": "E a quarta pessoa: o profissional que não prescreve nada e acha que isso não é com ele.",
          "destaque_cor": "tinta"})

# 3. a lista
S.append({"id": "lista", "tipo": "tabela", "eyebrow": "Agência Mundial Antidopagem · ABCD", "titulo": "Três blocos, em vigor em 1º de janeiro",
          "cab": ["Bloco", "Classes"],
          "larguras": [24, 76],
          "linhas": [["Em todos os momentos", "não aprovadas; anabolizantes; hormônios peptídicos e fatores de crescimento; beta-2 agonistas; moduladores hormonais e metabólicos; diuréticos e mascarantes; métodos de sangue, químicos e genéticos"],
                     ["Em competição", "estimulantes, narcóticos, canabinoides, glicocorticoides; das 23h59 da véspera ao fim da coleta"],
                     ["Esportes específicos", "betabloqueadores, em modalidades de precisão"]],
          "destaque": "Entra na lista quem cumpre dois de três critérios (desempenho, saúde, espírito esportivo) ou mascara. Consulte a do ano, em português, pelo princípio ativo.",
          "destaque_cor": "petr"})

# 4. violações
S.append({"id": "violacoes", "tipo": "duas", "eyebrow": "Onze violações", "titulo": "Violação não é sinônimo de exame positivo",
          "esq": {"t": "Dizem respeito ao atleta", "cor": "tinta",
                  "itens": ["presença na amostra", "uso ou tentativa", "recusar ou evitar a coleta", "falhas de localização"]},
          "dir": {"t": "Qualquer pessoa pode cometer", "cor": "verm",
                  "itens": ["adulterar o controle", "posse; tráfico", "administração a um atleta", "cumplicidade: ajudar, encobrir, incentivar", "associação proibida", "retaliar quem denuncia"]},
          "destaque": "“Eu não prescrevo, então não me envolve” está errado como fato, não como opinião.",
          "destaque_cor": "verm", "fonte": "Código Mundial Antidopagem, artigos 2.1 a 2.11"})

# 5. o fluxo
p = [svg_abre(1664, 420, "Fluxograma de prescrição em quatro perguntas: compete sob controle, princípio ativo na lista, via dose e momento permitidos, alternativa permitida; a última saída é a AUT"),
     "<defs>" + seta_marker("f1", MUDO) + seta_marker("f2", OXID) + "</defs>"]
rs = []
perg = ["compete sob controle?", "princípio ativo na lista vigente?", "via, dose e momento permitidos?", "alternativa permitida razoável?"]
for i, t in enumerate(perg):
    x = i * 346
    p.append(caixa(x, 20, 280, 124, AZUL, AZUL_T, esp=3))
    rs.append(rot(x + 14, 44, t, w=252, tam=26, cor=TINTA, peso=700, alinha="center"))
p.append(caixa(4 * 346, 20, 280, 124, FOSF, FOSF_T, esp=4))
rs.append(rot(4 * 346 + 14, 44, "AUT com antecedência", w=252, tam=28, cor=FOSF, peso=700, alinha="center"))
horiz = ["sim", "sim", "não", "não"]
for i, t in enumerate(horiz):
    x = i * 346 + 284
    p.append(f'<line x1="{x}" y1="82" x2="{x+56}" y2="82" stroke="{MUDO}" stroke-width="4" marker-end="url(#f1)"/>')
    rs.append(rot(x - 4, 40, t, w=66, tam=22, cor=MUDO, peso=700, alinha="center"))
saidas = [("não", "a pergunta vira: é seguro?", TINTA, CLARO),
          ("não", "prescreve e registra", OXID, OXID_T),
          ("sim", "segue, registra, declara", OXID, OXID_T),
          ("sim", "troca pela permitida", OXID, OXID_T)]
for i, (r, t, cor, fundo) in enumerate(saidas):
    x = i * 346
    p.append(f'<line x1="{x+140}" y1="150" x2="{x+140}" y2="266" stroke="{MUDO}" stroke-width="4" marker-end="url(#f1)"/>')
    rs.append(rot(x + 152, 190, r, w=80, tam=22, cor=MUDO, peso=700))
    p.append(caixa(x, 276, 280, 124, cor, fundo, esp=3))
    rs.append(rot(x + 14, 308, t, w=252, tam=26, cor=cor, peso=700, alinha="center"))
p.append("</svg>")
S.append({"id": "fluxo", "tipo": "diagrama", "h": 420, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "A decisão de prescrever", "titulo": "Quatro perguntas em cascata",
          "destaque": "“Não pode” não aparece em nenhuma saída do fluxo.",
          "destaque_cor": "tinta"})

# 6. cinco situações
S.append({"id": "consultorio", "tipo": "tabela", "eyebrow": "Onde a lista aparece de verdade", "titulo": "Cinco situações do consultório",
          "cab": ["Situação", "Classe e bloco", "O que decide"],
          "larguras": [18, 30, 52],
          "linhas": [["Asma", "beta-2 agonista · sempre", "substância, via, dose; salbutamol inalado até 1.600 µg/24 h e 600 µg/8 h (lista 2026)"],
                     ["Corticoide", "glicocorticoide · em competição", "injetável, oral e retal proibidos; tempo de eliminação publicado"],
                     ["Resfriado", "estimulante · em competição", "descongestionante do xarope; conferir o princípio ativo"],
                     ["TDAH", "estimulante · em competição", "não interromper: AUT"],
                     ["Corte de peso", "diurético · sempre", "mascara; também o adulterante mais comum no Brasil"]],
          "destaque": "Números da lista de 2026 são exemplo. Confira sempre a lista vigente.",
          "destaque_cor": "ambar"})

# 7. AUT
S.append({"id": "aut", "tipo": "lista", "eyebrow": "Autorização de uso terapêutico", "titulo": "Não é brecha: é o que permite tratar",
          "itens": [{"t": "Condição médica diagnosticada", "x": "que exige a substância ou o método proibido", "cor": "petr"},
                    {"t": "Sem ganho além do normal", "x": "altamente improvável que melhore além do retorno ao estado de saúde", "cor": "petr"},
                    {"t": "Sem alternativa permitida razoável", "x": "", "cor": "petr"},
                    {"t": "Não é consequência de doping prévio", "x": "quem se dopou não usa o dano como justificativa", "cor": "petr"}],
          "destaque": "Na ABCD: pedido pelo menos 30 dias antes (substância proibida em competição) e até 21 dias para decidir. A documentação aprova ou reprova.",
          "destaque_cor": "verm", "gap_itens": 16})

# 8. o controle
S.append({"id": "controle", "tipo": "duas", "eyebrow": "O controle, na prática", "titulo": "O que fazer e o que dizer no dia",
          "esq": {"t": "No dia", "cor": "petr",
                  "itens": ["notificação; observação até a coleta", "acompanhante: obrigatório para menor", "conferir dados e lacres; irregularidade no formulário", "declarar remédios e suplementos"]},
          "dir": {"t": "Depois do resultado adverso", "cor": "verm",
                  "itens": ["amostra B a pedido do atleta", "recusar a coleta equivale a positivo", "suspensão provisória, defesa, recurso", "sem culpa significativa: a documentação pesa"]},
          "destaque": "O papel da equipe não é julgar. É organizar a defesa e sustentar a pessoa.",
          "destaque_cor": "tinta"})

# 9. profissões
S.append({"id": "profissoes", "tipo": "tabela", "eyebrow": "A parte que é de todos", "titulo": "Responsabilidade de cada profissão",
          "cab": ["Profissão", "O que faz no antidoping"],
          "larguras": [26, 74],
          "linhas": [["Médico", "verifica antes de prescrever, escolhe a alternativa permitida, conduz a AUT, registra"],
                     ["Nutricionista", "as seis perguntas do suplemento; registro de marca e lote; o direito de dizer não"],
                     ["Educador físico e preparador", "encaminha em vez de opinar; reconhece o que circula no vestiário"],
                     ["Fisioterapeuta", "o que é aplicado entra na conta; administrar é violação"],
                     ["Psicólogo", "a pressão que leva ao uso; o atleta em colapso depois da violação"]],
          "destaque": "Verificar, documentar, encaminhar. Verificar custa minutos; não verificar pode custar anos.",
          "destaque_cor": "petr"})

# 10. quem nunca será testado
S.append({"id": "amador", "tipo": "duas", "eyebrow": "E quem nunca vai ser testado?", "titulo": "Muda a pergunta, não a lista",
          "esq": {"t": "A sobreposição", "cor": "ambar",
                  "itens": ["campeonatos master", "ligas amadoras federadas", "provas de rua com premiação", "universitários e categorias de base"]},
          "dir": {"t": "Fora dela", "cor": "verm",
                  "itens": ["a lista é, em boa parte, de coisas que fazem mal", "mesmo risco à saúde, sem controle médico", "“ciclo”, “protocolo”, “TRT”, “modulador”", "reconhecer o vocabulário é clínica"]},
          "destaque": "Para o amador: “isso é seguro, e por que essa pessoa está usando?”. É a pergunta da próxima aula.",
          "destaque_cor": "tinta"})

# 11. três decisões
S.append({"id": "resolucao", "tipo": "tabela", "eyebrow": "As três decisões do começo", "titulo": "Onde cada uma se resolve no fluxo",
          "cab": ["Decisão", "Pergunta do fluxo", "Conduta"],
          "larguras": [20, 26, 54],
          "linhas": [["Nadadora, asma", "via, dose e momento", "inalatório dentro do limite: segue, registra, declara; fora dele: AUT"],
                     ["Corredor, TDAH", "alternativa permitida", "AUT 30 dias antes; se não der tempo, muda a prova, não o remédio"],
                     ["Jogadora, infiltração", "via, dose e momento", "injetável: tempo de eliminação, alternativa, ou AUT; e é o melhor tratamento?"]],
          "destaque": "Depende da substância, da via, da dose e do prazo, e alguém precisa verificar e documentar.",
          "destaque_cor": "ambar"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "O que fica", "titulo": "Verificar, documentar, encaminhar",
          "regras": ["Lista anual, três blocos, conferida pelo princípio ativo",
                     "Onze violações; sete alcançam quem não é atleta",
                     "AUT: quatro critérios, 30 dias antes, até 21 para decidir"],
          "cards": [{"t": "Médico", "x": "Prescreve verificando; conduz a AUT."},
                    {"t": "Nutricionista", "x": "Suplemento checado e registrado."},
                    {"t": "Educador físico, preparador, fisioterapeuta, psicólogo", "x": "Escutam primeiro; encaminham."}],
          "quem": "Responsabilidade estrita para o atleta; profissional para quem indica."})

spec = {"arquivo": "aulas/MOD05/05-10-lista-proibida-aut-e-responsabilidade-da-equipe.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Lista proibida e autorização de uso terapêutico", "subtitulo": "Sistema, decisão clínica e responsabilidade da equipe",
        "nota_capa": "Entra pela decisão clínica.",
        "secoes": {"remedio": ["O sistema, a lista e as violações.", "capa"],
                   "fluxo": ["A decisão de prescrever, o consultório e a AUT.", "fluxo"],
                   "controle": ["O controle, as profissões e o amador.", "controle"],
                   "resolucao": ["As três decisões.", "resolucao"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-10.json"), "w"), ensure_ascii=False, indent=1)
print("05-10.json:", len(S), "slides")
