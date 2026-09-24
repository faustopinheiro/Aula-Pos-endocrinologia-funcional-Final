"""Spec do deck 3.5. Gera 03-05.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. dois erros
S.append({"id": "portas", "tipo": "numeros", "eyebrow": "Dois erros simétricos", "titulo": "Tratado sem ter, ou tem e nunca foi tratado",
          "numeros": [{"n": "1 em 650", "x": "nascimentos masculinos com síndrome de Klinefelter", "cor": "tinta"},
                      {"n": "3 em 4", "x": "dos afetados nunca diagnosticados", "cor": "verm"}],
          "destaque": "E eles passam pelo consultório por infertilidade, ginecomastia, dificuldade de ganhar massa: as queixas que chegam à nossa área.",
          "destaque_cor": "ambar", "fonte": "Bojesen, Juul e Gravholt, Journal of Clinical Endocrinology and Metabolism 2003 · registro nacional da Dinamarca"})

# 2. três caixas
p = [svg_abre(1664, 430, "Três caixas: primário, com LH e FSH altos; central orgânico e funcional, com LH e FSH baixos ou normais, o mesmo laboratório com causas diferentes")]
cols = [("Primário", FOSF, FOSF_T, "LH e FSH altos"), ("Central orgânico", AZUL, AZUL_T, "LH e FSH baixos ou normais"),
        ("Funcional", OXID, OXID_T, "LH e FSH baixos ou normais")]
causas = [["Klinefelter", "criptorquidia", "trauma, torção, orquite", "quimio, radioterapia"],
          ["tumor de hipófise", "prolactina alta", "hemocromatose", "Kallmann, trauma craniano"],
          ["pouca energia, sono curto", "obesidade", "treino sem recuperação", "remédios, anabolizante"]]
rs = []
for i, (nome, cor, fundo, lh) in enumerate(cols):
    x = i * 570
    p.append(caixa(x, 0, 524, 340, cor, fundo, esp=3))
    rs.append(rot(x + 24, 18, nome, w=480, tam=32, cor=cor, peso=700))
    rs.append(rot(x + 24, 66, lh, w=480, tam=26, cor=TINTA, peso=600))
    rs.append(rot(x + 24, 124, "<br>".join(causas[i]), w=480, tam=26, cor=TINTA, lh=1.45))
p.append(f'<path d="M594 360 V390 H1640 V360" fill="none" stroke="{TINTA}" stroke-width="4"/>')
p.append("</svg>")
rs.append(rot(594, 396, "mesmo exame: quem separa é a história e o exame físico", w=1046, tam=28, cor=TINTA, peso=700, alinha="center"))
S.append({"id": "caixas", "tipo": "diagrama", "h": 430, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Passo um", "titulo": "Classificar em três caixas"})

# 3. auditar
S.append({"id": "auditar", "tipo": "cards", "por_linha": 3, "eyebrow": "Passo dois", "titulo": "Auditar como o número foi produzido",
          "cards": [{"t": "Horário", "x": "coleta de tarde é coleta no vale", "cor": "verm"},
                    {"t": "Alimento", "x": "depois de comer, o valor cai por horas", "cor": "verm"},
                    {"t": "Doença aguda", "x": "o exame descreve a virose, não o eixo", "cor": "verm"},
                    {"t": "Treino recente", "x": "a manhã seguinte à sessão pesada não é base", "cor": "ambar"},
                    {"t": "SHBG não pedida", "x": "atleta magro e homem com obesidade erram em sentidos opostos", "cor": "ambar"},
                    {"t": "Troca de método", "x": "laboratórios diferentes, “queda” que é de método", "cor": "ambar"}],
          "destaque": "Qualquer uma comprometida: repita, não trate.", "destaque_cor": "tinta"})

# 4. remédios e obesidade
S.append({"id": "acionaveis", "tipo": "duas", "eyebrow": "As mais acionáveis", "titulo": "Remédios e obesidade",
          "esq": {"t": "Remédios que suprimem o eixo", "cor": "verm",
                  "itens": ["opioide, inclusive o crônico para dor", "corticoide em dose alta ou prolongada",
                            "antipsicóticos e alguns antieméticos: prolactina", "gabapentinoides, antiandrogênicos"]},
          "dir": {"t": "Obesidade, por duas vias", "cor": "ambar",
                  "itens": ["SHBG baixa derruba a total", "mais aromatização no tecido adiposo, mais freio no eixo",
                            "a causa reversível mais comum no homem adulto", "perder peso sobe a testosterona"]},
          "destaque": "Perda de peso é intervenção de primeira linha sobre o próprio eixo: sem ampola, sem supressão, sem impacto na fertilidade.",
          "destaque_cor": "petr", "fonte": "Corona e colaboradores, European Journal of Endocrinology 2013 · Bhasin e colaboradores, Endocrine Society 2018"})

# 5. as que escondem
S.append({"id": "escondem", "tipo": "lista", "eyebrow": "Passo três", "titulo": "As armadilhas que escondem o hipogonádico",
          "itens": [{"t": "“É normal nessa idade”", "x": "a queda com a idade é lenta e modesta", "cor": "verm"},
                    {"t": "Total normal com SHBG alta", "x": "o magro de endurance passa, com fração disponível ruim", "cor": "ambar"},
                    {"t": "Prolactina não pedida", "x": "em todo padrão central; ferro quando a história sugerir", "cor": "petr"}]})

# 6. exame físico
S.append({"id": "exame", "tipo": "cards", "eyebrow": "A armadilha que mais falta", "titulo": "O exame físico que decide",
          "cards": [{"t": "Volume testicular", "x": "pequenos e firmes: primário · pequenos e moles: supressão central longa", "cor": "verm"},
                    {"t": "Mama", "x": "glândula à palpação, não gordura", "cor": "ambar"},
                    {"t": "Pelos e puberdade", "x": "antes ou depois da puberdade", "cor": "tinta"},
                    {"t": "Campo visual", "x": "30 segundos: compressão do quiasma", "cor": "petr"},
                    {"t": "Olfato", "x": "Kallmann: “sente cheiro normalmente?”", "cor": "petr"}]})

# 7. anabolizante: funil
p = [svg_abre(1664, 400, "Funil: 168 casos de hipogonadismo ligado a anabolizante, 38 com desfecho completamente conhecido, 4 com reversão completa do eixo, 2 deles com medicamento")]
etapas = [(168, "casos claramente ligados a anabolizante", MUDO), (38, "com desfecho completamente conhecido", AZUL), (4, "com reversão completa do eixo", FOSF)]
rs = []
for i, (n, txt, cor) in enumerate(etapas):
    y = 20 + i * 120
    w = max(880 * n / 168, 40)
    p.append(f'<rect x="300" y="{y}" width="{w:.0f}" height="90" rx="6" fill="{cor}"/>')
    rs.append(rot(0, y + 18, str(n), w=270, tam=56, cor=TINTA, peso=700, alinha="right", serif=True))
    rs.append(rot(300 + w + 24, y + 28, txt, w=1664 - 324 - w, tam=28, cor=TINTA, peso=600))
p.append("</svg>")
rs.append(rot(300, 370, "dois dos quatro, com ajuda de medicamento", w=1300, tam=26, cor=MUDO))
S.append({"id": "anabolizante", "tipo": "diagrama", "h": 400, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Vilar Neto e colaboradores, 2021", "titulo": "Mais do que se promete, e nem sempre volta",
          "destaque": "Viés: relato publicado favorece o caso que deu errado. Mas ninguém consegue prometer quanto tempo, nem se.",
          "destaque_cor": "ambar", "fonte": "Andrologia 2021 · Solanki e colaboradores, Endocrine Connections 2023"})

# 8. o que dizer
S.append({"id": "dizer", "tipo": "lista", "eyebrow": "Sem moralismo", "titulo": "Três coisas ditas com clareza",
          "itens": [{"t": "“Ciclo” sugere um retorno que não é garantido", "cor": "verm"},
                    {"t": "Terapia pós-ciclo não é botão de reset", "x": "é conduta médica, com indicação, e não garante retorno", "cor": "verm"},
                    {"t": "Fertilidade se discute antes", "x": "não depois de três anos de uso", "cor": "petr"}],
          "destaque": "Testosterona baixa, LH baixo, testículos pequenos e moles: pergunte pelo nome da substância, por quanto tempo, há quanto tempo parou.",
          "destaque_cor": "tinta"})

# 9. roteiro
S.append({"id": "roteiro", "tipo": "lista", "eyebrow": "O procedimento", "titulo": "Cinco passos, cada um com sua saída", "gap_itens": 20,
          "itens": [{"t": "Auditar o número", "x": "algo comprometido: repetir", "cor": "tinta"},
                    {"t": "Dosar o par e classificar", "x": "LH alto: testículo · baixo ou normal: acima", "cor": "tinta"},
                    {"t": "Central: orgânico ou funcional?", "x": "história, exame físico, prolactina, ferro quando couber", "cor": "petr"},
                    {"t": "Corrigir o que é corrigível e reavaliar", "x": "3 a 4 meses, coleta padronizada", "cor": "petr"},
                    {"t": "Investigar com imagem e encaminhar", "x": "central sem contexto, prolactina alta, visão, dor de cabeça nova", "cor": "verm"}]})

# 10. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Quem faz o quê", "titulo": "Tratar a causa, e não o número",
          "regras": ["Idade não é diagnóstico", "Classificar, investigar e tratar é ato médico"],
          "cards": [{"t": "O padrão clínico", "x": "Quem atende toda semana vê rendimento, humor e massa caindo apesar do treino."},
                    {"t": "A substância", "x": "Contada ao educador físico, chega ao médico com o consentimento do paciente."}],
          "quem": "Não é delação. É a diferença entre tratar a causa e tratar o número."})

spec = {"arquivo": "aulas/MOD03/03-05-hipogonadismo-diferencial-e-armadilhas.md",
        "modulo": "Fisiologia Hormonal e Endocrinologia do Exercício", "tema": "bordo",
        "titulo": "Hipogonadismo masculino", "subtitulo": "Diagnóstico diferencial e armadilhas de interpretação",
        "nota_capa": "Entra pelos dois erros simétricos.",
        "secoes": {"classificar": ["Os dois erros e as três caixas.", "capa"],
                   "armadilhas": ["O que fabrica e o que esconde o diagnóstico.", "auditar"],
                   "anabolizante": ["Anabolizante, sem moralismo.", "anabolizante"],
                   "roteiro": ["O procedimento e o fecho.", "roteiro"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "03-05.json"), "w"), ensure_ascii=False, indent=1)
print("03-05.json:", len(S), "slides")
