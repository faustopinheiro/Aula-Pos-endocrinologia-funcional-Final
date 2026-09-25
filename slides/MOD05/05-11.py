"""Spec do deck 5.11. Gera 05-11.json ao lado deste arquivo."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *

S = []
FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, BORDA, CLARO = "#FDFCF9", "#DDD8CC", "#F7F6F2"

def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'

# 1. o papel dobrado
S.append({"id": "papel", "tipo": "frase", "fundo": "tinta", "eyebrow": "Caso ilustrativo",
          "frase": "Na pergunta de rotina sobre remédios, ele hesitou e tirou um papel dobrado do bolso.",
          "apoio": "Veio para a avaliação pré-participação de uma prova de trilha. No papel: testosterona injetável, hormônio de crescimento, dois peptídeos, um inibidor de aromatase e um comprimido “para proteger o fígado”. Chamava aquilo de protocolo."})

# 2. o que a aula é
S.append({"id": "limites", "tipo": "duas", "eyebrow": "Antes de seguir", "titulo": "O que esta aula faz, e o que não faz",
          "esq": {"t": "Faz", "cor": "petr",
                  "itens": ["ajuda a reconhecer", "mostra o risco real", "mostra a fronteira ética e legal no Brasil", "conduz a conversa sem perder a pessoa"]},
          "dir": {"t": "Não faz", "cor": "verm",
                  "itens": ["não ensina a prescrever", "não traz protocolo nem dose", "não discute “como fazer com segurança”", "não compara esquemas"]},
          "destaque": "Hipogonadismo e deficiência de GH ficaram no módulo de fisiologia hormonal. Esta aula é sobre o que acontece fora disso.",
          "destaque_cor": "tinta"})

# 3. a lista
S.append({"id": "lista", "tipo": "tabela", "eyebrow": "O que havia no papel", "titulo": "A classificação muda tudo",
          "cab": ["Item", "O que é", "No papel dele"],
          "larguras": [24, 38, 38],
          "linhas": [["Testosterona", "medicamento; indicação: hipogonadismo diagnosticado", "sem diagnóstico; objetivo estético"],
                     ["Hormônio de crescimento", "medicamento; indicações específicas", "composição muda, força e função não acompanham"],
                     ["Inibidor de aromatase", "uso oncológico e endócrino", "sem estradiol: mais gordura, pior função sexual"],
                     ["Peptídeos", "muitos sem aprovação para uso humano", "“apenas para pesquisa”: sem controle"],
                     ["“Protetor do fígado”", "o item mais revelador", "efeito adverso previsto e administrado"]],
          "destaque": "Repor o que falta é tratamento. Elevar o que está normal é outra coisa.",
          "destaque_cor": "verm", "fonte": "Estradiol em homens: Finkelstein e colaboradores, New England Journal of Medicine 2013"})

# 4. Sagoe e vocabulário
S.append({"id": "sagoe", "tipo": "numeros", "eyebrow": "Sagoe e colaboradores, 2014", "titulo": "Não é raro",
          "numeros": [{"n": "3,3%", "x": "uso de anabolizante ao longo da vida, no mundo", "cor": "tinta"},
                      {"n": "6,4%", "x": "entre homens", "cor": "ambar"},
                      {"n": "4,8%", "x": "na América do Sul, acima da média global", "cor": "verm"}],
          "destaque": "Otimização, modulação, protocolo, ciclo, reposição fora de indicação: palavras que tiram a conversa do tratamento e a levam para o aprimoramento.",
          "destaque_cor": "tinta", "fonte": "187 estudos · Annals of Epidemiology 2014"})

# 5. motores
S.append({"id": "motores", "tipo": "cards", "por_linha": 4, "eyebrow": "Por que ele chegou lá", "titulo": "Três motores e o que havia por baixo",
          "cards": [{"t": "O corpo", "x": "insatisfação, comparação, dismorfia muscular", "cor": "ambar"},
                    {"t": "A idade", "x": "“seus hormônios caíram”: verdade parcial, conclusão falsa", "cor": "ambar"},
                    {"t": "O mercado", "x": "consulta, exames, produtos, “níveis ótimos”", "cor": "ambar"},
                    {"t": "O que acontecia", "x": "cinco horas de sono, viagens, álcool, nove quilos, nenhum treino de força", "cor": "petr"}],
          "destaque": "Ele se sentia melhor. Negar isso destrói a conversa: o efeito é real, parte dele viria de dormir e treinar, e o preço está em outro lugar.",
          "destaque_cor": "tinta"})

# 6. riscos
S.append({"id": "riscos", "tipo": "lista", "eyebrow": "Sem suavizar e sem exagerar", "titulo": "Os riscos",
          "itens": [{"t": "Coração", "x": "perfil lipídico, pressão, alterações estruturais em uso longo", "cor": "verm"},
                    {"t": "Eixo e fertilidade", "x": "supressão; recuperação em meses, nem sempre completa", "cor": "verm"},
                    {"t": "Sangue e fígado", "x": "hematócrito e trombose; formas orais e o fígado", "cor": "ambar"},
                    {"t": "Humor", "x": "irritabilidade no uso; depressão na suspensão; dependência descrita", "cor": "ambar"},
                    {"t": "O produto e os peptídeos", "x": "frasco sem rótulo; sem dado de segurança: a pessoa é o estudo", "cor": "tinta"}],
          "gap_itens": 14})

# 7. os três portões
p = [svg_abre(1664, 300, "Três portões em sequência: deficiência específica comprovada, nexo causal com o quadro clínico e benefício cientificamente comprovado levam a tratamento; finalidade estética, de massa muscular ou de desempenho é vedada"),
     "<defs>" + seta_marker("g1", OXID) + seta_marker("g2", FOSF) + "</defs>"]
rs = []
portoes = ["deficiência específica comprovada", "nexo causal com o quadro clínico", "benefício cientificamente comprovado"]
for i, t in enumerate(portoes):
    x = i * 340
    p.append(caixa(x, 20, 290, 160, OXID, OXID_T, esp=3))
    rs.append(rot(x + 16, 46, t, w=258, tam=28, cor=TINTA, peso=700, alinha="center"))
    p.append(f'<line x1="{x+294}" y1="95" x2="{x+334}" y2="95" stroke="{OXID}" stroke-width="4" marker-end="url(#g1)"/>')
p.append(caixa(1020, 20, 260, 160, OXID, OXID, esp=3))
rs.append(rot(1020, 78, "tratamento", w=260, tam=34, cor="#FFFFFF", peso=700, alinha="center"))
p.append(caixa(1320, 30, 344, 250, FOSF, FOSF_T, esp=4))
rs += [rot(1336, 50, "finalidade estética, massa muscular, desempenho", w=312, tam=26, cor=TINTA, peso=600, alinha="center"),
       rot(1336, 200, "vedado", w=312, tam=40, cor=FOSF, peso=700, alinha="center")]
p.append(f'<line x1="0" y1="230" x2="1280" y2="230" stroke="{MUDO}" stroke-width="2" stroke-dasharray="8 8"/>')
p.append("</svg>")
rs.append(rot(0, 246, "o papel dobrado não passava por nenhum portão", w=1280, tam=26, cor=MUDO, peso=600))
S.append({"id": "portoes", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Resolução CFM 2.333, de 2023", "titulo": "A fronteira está escrita",
          "destaque": "Anvisa, 2024: proibidos os implantes hormonais anabolizantes com essas finalidades. Isso não é zona cinzenta, e endossar também pesa.",
          "destaque_cor": "verm", "fonte": "CFM, DOU de 11 de abril de 2023 · Anvisa, RE 4.353/2024"})

# 8. a conversa
S.append({"id": "conversa", "tipo": "lista", "eyebrow": "Como conduzir", "titulo": "Quatro passos",
          "itens": [{"t": "Perguntar sem julgar, como rotina", "x": "“hormônio, peptídeo, algo injetável, algo manipulado?”", "cor": "petr"},
                    {"t": "Nomear o risco específico", "x": "fertilidade, hematócrito, fígado, humor na suspensão", "cor": "petr"},
                    {"t": "Oferecer a avaliação que faltou", "x": "entregar o que o protocolo prometeu: um diagnóstico", "cor": "ambar"},
                    {"t": "Manter a porta aberta", "x": "ele pode não parar; sem porta, some até a complicação", "cor": "ambar"}],
          "destaque": "Específico convence; genérico dispensa.",
          "destaque_cor": "tinta", "gap_itens": 20})

# 9. conivência?
S.append({"id": "fronteira", "tipo": "duas", "eyebrow": "Acompanhar quem não quer parar é conivência?", "titulo": "Cuidar da pessoa, não viabilizar a prática",
          "esq": {"t": "Cuidar", "cor": "petr",
                  "itens": ["acompanhar exames", "monitorar risco", "tratar complicação", "manter a conversa"]},
          "dir": {"t": "Viabilizar", "cor": "verm",
                  "itens": ["prescrever ou ajustar dose", "sugerir substância", "legitimar o protocolo", "ameaçar, humilhar, julgar"]},
          "destaque": "Menor de idade: família e proteção. Dor no peito, pressão muito alta, humor alterado, ideação suicida: encaminhamento imediato.",
          "destaque_cor": "verm"})

# 10. o seguimento
p = [svg_abre(1664, 300, "Linha do tempo do caso ilustrativo: primeira consulta, resultados dos exames, a palavra fertilidade e os meses seguintes")]
rs = []
etapas = [("Primeira consulta", "avaliação feita; exames pedidos e explicados", AZUL, AZUL_T),
          ("Os resultados", "hematócrito alto, lipídios piores, eixo suprimido", FOSF, FOSF_T),
          ("A palavra que mudou", "fertilidade: ninguém tinha falado nisso", GLIC, GLIC_T),
          ("Os meses seguintes", "suspensão acompanhada, psicólogo, força, sono, álcool", OXID, OXID_T)]
p.append(f'<line x1="20" y1="40" x2="1644" y2="40" stroke="{MUDO}" stroke-width="4"/>')
for i, (t, x_, cor, fundo) in enumerate(etapas):
    x = i * 420
    p.append(f'<circle cx="{x+20}" cy="40" r="14" fill="{cor}"/>')
    p.append(caixa(x, 80, 390, 200, cor, fundo, esp=3))
    rs += [rot(x + 18, 100, t, w=354, tam=30, cor=cor, peso=700),
           rot(x + 18, 156, x_, w=354, tam=26, cor=TINTA)]
p.append("</svg>")
S.append({"id": "seguimento", "tipo": "diagrama", "h": 300, "svg": "".join(p), "rotulos": rs,
          "eyebrow": "Caso ilustrativo", "titulo": "Sem virada de mesa",
          "destaque": "Ficou mais fraco do que no auge do protocolo, e disse isso. Alguém tinha olhado os exames dele; ninguém tinha perguntado como ele dormia.",
          "destaque_cor": "tinta"})

# 11. decisão e contribuição
S.append({"id": "niveis", "tipo": "tabela", "eyebrow": "Fecho do módulo", "titulo": "Decisão e contribuição",
          "cab": ["Profissão", "Decide", "Contribui"],
          "larguras": [22, 40, 38],
          "linhas": [["Nutricionista", "suplemento, dose, estratégia; marca e lote no atleta testado", "reconhece o ingrediente de risco no rótulo"],
                     ["Médico", "medicamento, deficiência, reposição, AUT, suspensão", "“você compete sob controle?”, em cinco segundos"],
                     ["Educador físico e preparador", "o treino que dá sentido ao ergogênico", "escuta o vestiário"],
                     ["Fisioterapeuta", "carga no tecido em recuperação", "é quem mais escuta sobre substância"],
                     ["Psicólogo", "corpo, pressão, sofrimento na suspensão", "vê a insatisfação por trás do pedido"]],
          "destaque": "Terapia hormonal com finalidade estética, de massa muscular ou de desempenho não é decisão médica disponível: é conduta vedada.",
          "destaque_cor": "verm"})

# 12. fecho do módulo
S.append({"id": "fecho", "tipo": "fecho", "eyebrow": "Reconhecimento: de todos",
          "titulo": "Quase tudo o que se vende promete substituir o que funciona",
          "regras": ["Dose não declarada, catorze ingredientes, efeito de remédio",
                     "Manipulado “personalizado”, importado sem fabricante, frasco sem rótulo",
                     "Ciclo, protocolo, otimização; e o comprimido que protege de outro"],
          "cards": [{"t": "Decisão", "x": "Cada profissão decide no seu campo, com registro."},
                    {"t": "Contribuição", "x": "O vestiário, o rótulo, a anamnese, a escuta."},
                    {"t": "Reconhecimento", "x": "Não exige a profissão certa. Exige ter aprendido o sinal."}],
          "quem": "E quase tudo o que funciona já estava disponível antes de alguém comprar alguma coisa. Próximo módulo: medicina esportiva clínica."})

spec = {"arquivo": "aulas/MOD05/05-11-hormonios-e-peptideos-fora-de-indicacao.md",
        "modulo": "Suplementação, Ergogênicos e Antidoping", "tema": "ameixa",
        "titulo": "Hormônios e peptídeos fora de indicação", "subtitulo": "Limites clínicos, éticos e legais",
        "nota_capa": "Entra pelo caso ilustrativo.",
        "secoes": {"papel": ["O caso, a lista e o risco.", "capa"],
                   "portoes": ["A fronteira e a conversa.", "portoes"],
                   "seguimento": ["O seguimento e o fecho do módulo.", "seguimento"]},
        "slides": S}
json.dump(spec, open(os.path.join(os.path.dirname(__file__), "05-11.json"), "w"), ensure_ascii=False, indent=1)
print("05-11.json:", len(S), "slides")
