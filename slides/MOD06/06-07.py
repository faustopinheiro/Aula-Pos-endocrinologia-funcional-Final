"""Spec do deck 6.7. Gera 06-07.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []

# 1. três perfis
S.append({"id": "perfis", "tipo": "frase", "fundo": "tinta", "eyebrow": "Três pessoas com bombinha na mão",
          "frase": "Em nenhuma delas a queixa decide. O número decide.",
          "apoio": "O adolescente afastado da educação física desde a infância. A nadadora que tosse depois de todo treino. O corredor com a bombinha de um amigo antes da prova fria."})

# 2. três números
S.append({"id": "numeros", "tipo": "numeros", "eyebrow": "Os números que atravessam a aula", "titulo": "Diagnóstico, uso e limite",
          "numeros": [{"n": "10%", "x": "queda do VEF1 que define o diagnóstico", "cor": "tinta"},
                      {"n": "15 min", "x": "entre o broncodilatador e o esforço", "cor": "petr"},
                      {"n": "1.600 µg", "x": "teto diário do salbutamol inalado", "cor": "verm"}],
          "destaque": "O rótulo errado afasta gente do esporte; a falta de rótulo deixa gente tossindo por anos. Os dois se resolvem com medida.",
          "destaque_cor": "tinta"})

# 3. mecanismo
S.append({"id": "mecanismo", "tipo": "duas", "eyebrow": "O que é", "titulo": "Com asma ou sem asma de base",
          "esq": {"t": "A definição", "cor": "petr",
                  "itens": ["estreitamento transitório das vias aéreas", "durante ou logo depois do esforço", "acontece em quem tem asma", "e em quem não tem"]},
          "dir": {"t": "O mecanismo", "cor": "ambar",
                  "itens": ["ventilação alta e prolongada", "epitélio perde água e calor", "mastócitos liberam mediadores", "o músculo liso contrai"]},
          "destaque": "Ar frio e seco piora, ar morno e úmido melhora. O risco cresce com o volume de ar que passa.",
          "destaque_cor": "tinta"})

# 4. curva esquemática
p = [svg_abre(1664, 340, "Esquema de uma curva de VEF1 depois do esforço: cai abaixo da linha de queda de 10% e depois volta ao basal")]
p.append(f'<line x1="60" y1="300" x2="1640" y2="300" stroke="{MUDO}" stroke-width="3"/>')
p.append(f'<line x1="60" y1="70" x2="1640" y2="70" stroke="{MUDO}" stroke-width="2" stroke-dasharray="4 8"/>')
p.append(f'<line x1="60" y1="150" x2="1640" y2="150" stroke="{FOSF}" stroke-width="3" stroke-dasharray="12 10"/>')
p.append(f'<path d="M60,70 C260,72 380,120 520,210 C640,265 760,262 900,215 C1100,140 1300,85 1640,72" fill="none" stroke="{AZUL}" stroke-width="6"/>')
p.append("</svg>")
rs = [rot(1240, 22, "basal", w=380, tam=24, cor=MUDO, peso=600, alinha="right"),
      rot(1240, 104, "queda de 10%", w=380, tam=26, cor=FOSF, peso=700, alinha="right"),
      rot(560, 272, "VEF1 depois do esforço", w=420, tam=26, cor=AZUL, peso=700, alinha="center"),
      rot(60, 306, "fim do esforço", w=300, tam=24, cor=MUDO),
      rot(1340, 306, "minutos depois", w=300, tam=24, cor=MUDO, alinha="right")]
S.append({"id": "criterio", "tipo": "diagrama", "h": 340, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "O número do diagnóstico", "titulo": "Queda de pelo menos 10% do VEF1",
          "destaque": "Espirometria de repouso normal não exclui nada. Se a suspeita é de esforço, o teste inclui o esforço, ou um substituto como hiperventilação eucápnica ou manitol.",
          "destaque_cor": "verm", "fonte": "Esquema, sem valores medidos · critério da diretriz ATS 2013"})

# 5. prevalência
S.append({"id": "prevalencia", "tipo": "numeros", "eyebrow": "Quem tem mais", "titulo": "Em atletas, de 30 a 70%",
          "numeros": [{"n": "inverno", "x": "ar frio e seco", "cor": "petr"},
                      {"n": "endurance", "x": "muito ar, por muito tempo", "cor": "ambar"},
                      {"n": "piscina", "x": "coberta, com subprodutos de cloro", "cor": "tinta"}],
          "destaque": "Tosse depois do treino não é normal do esporte. E prevalência alta não autoriza tratar sem medir: o grupo sintomático tem muita gente com outra coisa.",
          "destaque_cor": "verm", "fonte": "Varia com modalidade e critério diagnóstico"})

# 6. diferenciais
S.append({"id": "diferenciais", "tipo": "tabela", "eyebrow": "Antes de tratar", "titulo": "O que imita broncoespasmo",
          "cab": ["Diferencial", "A pista"],
          "larguras": [38, 62],
          "linhas": [["Descondicionamento", "falta de ar proporcional ao esforço; o tratamento é treinar"],
                     ["Rinite com respiração oral", "ar que chega sem aquecer nem umidificar"],
                     ["Refluxo", "tosse e aperto em posição e horário específicos"],
                     ["Padrão disfuncional, ansiedade", "falta de ar real, pulmão normal"],
                     ["Deficiência de ferro", "exame respiratório normal"],
                     ["Causa cardíaca", "exame respiratório normal"]],
          "destaque": "O círculo cruel: o rótulo afasta, o afastamento descondiciona, o descondicionamento confirma o rótulo.",
          "destaque_cor": "ambar"})

# 7. laringe
S.append({"id": "laringe", "tipo": "duas", "eyebrow": "O diferencial que mais engana", "titulo": "Obstrução laríngea induzida pelo exercício",
          "esq": {"t": "Broncoespasmo", "cor": "petr",
                  "itens": ["chiado na expiração", "aperto no peito", "piora depois do esforço", "responde ao broncodilatador"]},
          "dir": {"t": "Obstrução laríngea", "cor": "verm",
                  "itens": ["ruído na inspiração, o estridor", "garganta fechando", "no pico; some em 1 a 2 minutos parado", "não responde ao broncodilatador"]},
          "destaque": "Tratamento de fonoaudiologia e padrão respiratório. Não melhora com a bombinha: pense nela antes de subir a dose.",
          "destaque_cor": "tinta"})

# 8. camadas
S.append({"id": "camadas", "tipo": "lista", "eyebrow": "O tratamento, pela diretriz de 2013", "titulo": "Em camadas",
          "itens": [{"t": "Beta-2 de curta ação, 15 minutos antes", "x": "uso intermitente; diário gera tolerância e é sinal", "cor": "petr"},
                    {"t": "Corticoide inalatório de manutenção", "x": "broncoespasmo frequente na asma é asma mal controlada", "cor": "verm"},
                    {"t": "Alternativas e comorbidades", "x": "antileucotrieno, anti-histamínico na alergia, tratar a rinite", "cor": "ambar"},
                    {"t": "Aquecimento", "x": "de graça, e é prescrição de treino", "cor": "petr"}],
          "gap_itens": 22})

# 9. aquecimento
S.append({"id": "aquecimento", "tipo": "numeros", "eyebrow": "A camada de graça", "titulo": "O período refratário",
          "numeros": [{"n": "10 a 15 min", "x": "de aquecimento moderado a vigoroso", "cor": "petr"},
                      {"n": "~2 h", "x": "de broncoespasmo atenuado depois dele", "cor": "ambar"},
                      {"n": "intervalado", "x": "ou combinado: a recomendação para todos", "cor": "tinta"}],
          "destaque": "Frio: bandana ou máscara. Poluição e pólen: mudar o horário. Piscina coberta: ventilação e qualidade da água fazem parte do problema.",
          "destaque_cor": "tinta", "fonte": "Diretriz da Sociedade Torácica Americana, 2013"})

# 10. doses
S.append({"id": "doses", "tipo": "tabela", "eyebrow": "Onde o atleta perde carreira por desatenção", "titulo": "Os limites dos inalados permitidos",
          "cab": ["Substância", "Em 24 horas", "Por intervalo"],
          "larguras": [30, 30, 40],
          "linhas": [["Salbutamol", "1.600 µg", "até 600 µg em 8 h"],
                     ["Formoterol", "54 µg", "até 36 µg em 12 h"],
                     ["Salmeterol", "200 µg", "até 100 µg em 8 h (novo em 2026)"],
                     ["Vilanterol", "25 µg", ""]],
          "destaque": "Oral, injetável ou acima do limite: só com autorização de uso terapêutico. Confira a lista vigente a cada temporada.",
          "destaque_cor": "verm", "fonte": "Lista de substâncias proibidas da WADA, 2026, seção S3"})

# 11. urina
S.append({"id": "urina", "tipo": "numeros", "eyebrow": "A segunda camada do antidoping", "titulo": "Dose certa não garante urina limpa",
          "numeros": [{"n": "1.000", "x": "ng/mL de salbutamol na urina: incompatível com uso terapêutico", "cor": "verm"},
                      {"n": "40", "x": "ng/mL de formoterol na urina", "cor": "verm"},
                      {"n": "10%", "x": "o teste documentado que a autorização exige", "cor": "tinta"}],
          "destaque": "Sem diagnóstico objetivo, não há autorização. Registre princípio ativo, dose e horário, e nunca use a bombinha de outra pessoa.",
          "destaque_cor": "tinta", "fonte": "WADA 2026"})

# 12. fecho
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Os três perfis, respondidos", "titulo": "Medir antes de tratar, e continuar treinando",
          "regras": ["Queda de 10% do VEF1 com esforço: sem ela, é suspeita",
                     "Bombinha todo dia é sinal de asma mal controlada",
                     "Sem teste documentado, sem autorização de uso terapêutico"],
          "cards": [{"t": "Médico", "x": "Mede, prescreve, ajusta controle, conduz a autorização."},
                    {"t": "Preparação física", "x": "Aquecimento com período refratário, carga, horário e ambiente."},
                    {"t": "Comissão inteira", "x": "Pergunta sobre tosse e chiado, registra o que é inalado."}],
          "quem": "Cochrane: treinar melhora o condicionamento, é bem tolerado, sem relato de piora. O afastamento nunca foi neutro."})

spec = {"arquivo": "aulas/MOD06/06-07-asma-e-broncoespasmo-induzido-por-exercicio.md",
        "modulo": "Medicina Esportiva Clínica", "tema": "tinta",
        "titulo": "Broncoespasmo induzido pelo exercício", "subtitulo": "Os números do diagnóstico, do tratamento e do antidoping",
        "nota_capa": "Entra pelos três perfis com bombinha na mão.",
        "secoes": {"perfis": ["Os perfis, os números e o diagnóstico.", "capa"],
                   "prevalencia": ["Quem tem, e o que imita.", "prevalencia"],
                   "camadas": ["Tratamento e aquecimento.", "camadas"],
                   "doses": ["Antidoping e fecho.", "doses"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "06-07.json"), "w"), ensure_ascii=False, indent=1)
print("06-07.json:", len(S), "slides")
