"""Gera o HTML do projeto pedagógico atualizado. Uso: python3 gerar_projeto.py <repo> <saida.html>"""
import glob, html, re, sys

REPO, SAIDA = sys.argv[1], sys.argv[2]
G = open(f"{REPO}/docs/_grade-400h-original.txt", encoding="utf-8").read().split("\n")
e = html.escape


def limpa(t):
    return t.replace(" — ", ", ").replace("—", ",").strip()


# ---------- módulos do projeto original ----------
mods = {}
idx = [i for i, l in enumerate(G) if re.match(r"^Módulo \d+ — ", l)]
for k, i in enumerate(idx):
    fim = idx[k + 1] if k + 1 < len(idx) else next(j for j, l in enumerate(G) if l.startswith("7. Metodologia"))
    bloco = G[i:fim]
    n = int(re.match(r"Módulo (\d+)", G[i])[1])
    nome = G[i].split(" — ", 1)[1].strip()
    ch = re.match(r"(\d+) horas", G[i + 1])[1]
    ie = bloco.index("Ementa"); ic = bloco.index("Competências desenvolvidas"); ig = bloco.index("Grade de aulas")
    ii = bloco.index("Integração multiprofissional")
    mods[n] = dict(nome=nome, ch=int(ch), ementa=bloco[ie + 1].strip(),
                   comp=[c.strip() for c in bloco[ic + 1:ig] if c.strip()],
                   integ=" ".join(c.strip() for c in bloco[ii + 1:] if c.strip()))

# ---------- aulas escritas ----------
for n in mods:
    aulas = []
    for f in sorted(glob.glob(f"{REPO}/aulas/MOD{n:02d}/*.md"), key=lambda p: [int(x) for x in re.findall(r"/(\d+)-(\d+)-", p)[0]]):
        t = open(f, encoding="utf-8").read(800).split("\n")
        m = re.match(r"# Módulo \d+ · Aula ([\d.]+) — (.+)", t[0])
        d = re.search(r"Duração: (\d+) minutos · (\d+) slides · Arquitetura: (\S+)", "\n".join(t[:6]))
        aulas.append((m[1], m[2].strip(), int(d[1]), int(d[2]), d[3]))
    mods[n]["aulas"] = aulas
    mods[n]["min"] = sum(a[2] for a in aulas)
    mods[n]["slides"] = sum(a[3] for a in aulas)

hm = lambda m: f"{m // 60}h{m % 60:02d}"
TOT_A = sum(len(m["aulas"]) for m in mods.values()); TOT_M = sum(m["min"] for m in mods.values())
TOT_S = sum(m["slides"] for m in mods.values()); TOT_CH = sum(m["ch"] for m in mods.values())
ARQ = {}
for m in mods.values():
    for a in m["aulas"]:
        ARQ[a[4]] = ARQ.get(a[4], 0) + 1
assert TOT_CH == 400, TOT_CH

# ---------- fontes ----------
i0 = G.index("Fontes consultadas")
fontes = [l.strip() for l in G[i0 + 2:] if l.strip()]


def secao_txt(ini, fim):
    a = next(i for i, l in enumerate(G) if l.startswith(ini)); b = next(i for i, l in enumerate(G) if l.startswith(fim))
    return [l.strip() for l in G[a + 1:b] if l.strip()]


apres = secao_txt("1. Apresentação", "2. Objetivos")
obj = secao_txt("2. Objetivos", "3. Público-alvo")
pub = secao_txt("3. Público-alvo", "4. Estrutura curricular")
proj = secao_txt("9. Projeto aplicado", "10. Perfil")
doc = secao_txt("10. Perfil", "11. Observações")
reg = secao_txt("11. Observações", "Fontes consultadas")

P = lambda t: f"<p>{e(limpa(t))}</p>"
UL = lambda xs: "<ul>" + "".join(f"<li>{e(limpa(x))}</li>" for x in xs) + "</ul>"

h = []
# capa
h.append(f"""<section class="capa">
<div class="selo">Pós-graduação lato sensu</div>
<h1>Ciências do Esporte<br>Aplicadas à Saúde</h1>
<div class="sub">Formação multiprofissional integrada</div>
<div class="tipo">Matriz curricular e projeto pedagógico · versão atualizada</div>
<div class="nums"><div><b>400</b><span>horas</span></div><div><b>{len(mods)}</b><span>módulos</span></div><div><b>{TOT_A}</b><span>aulas</span></div><div><b>{TOT_M // 60}h{TOT_M % 60:02d}</b><span>de videoaula</span></div></div>
<div class="coord"><span>Coordenação acadêmica</span><b>Dr. Fausto Pinheiro de Farias</b>Medicina de Família e Comunidade · Medicina do Esporte · Endocrinologia do Exercício</div>
<div class="data">Modalidade a distância · outubro de 2026</div>
</section>""")

# sumário
itens = ["Apresentação", "Objetivos", "Público-alvo e lógica multiprofissional", "Estrutura curricular", "Formato didático das aulas",
         "Detalhamento dos módulos", "Metodologia", "Sistema de avaliação", "Projeto aplicado de conclusão", "Perfil do corpo docente",
         "Observações regulatórias", "Fontes consultadas"]
h.append('<section class="sumario"><h2>Sumário</h2><ol>' + "".join(f"<li>{x}</li>" for x in itens) + "</ol>"
         '<div class="nota"><b>O que mudou nesta versão.</b> Esta versão substitui a grade planejada pela grade das aulas efetivamente '
         f'roteirizadas: {TOT_A} aulas, com títulos, durações e formato finais. Ementas, competências, níveis de responsabilidade, '
         'avaliação e projeto aplicado seguem o projeto original de 400 horas. As aulas-mestras de 75 minutos previstas no projeto '
         'original não foram mantidas: cada tema estruturante foi distribuído em aulas de duração padrão, ligadas entre si.</div></section>')

# 1-3
h.append('<section><h2><span>1</span>Apresentação</h2>' + "".join(P(x) for x in apres) + "</section>")
ig = obj.index("Objetivo geral"); ie_ = obj.index("Objetivos específicos")
h.append('<section class="cont"><h2><span>2</span>Objetivos</h2><h3>Objetivo geral</h3>' + P(obj[ig + 1]) +
         "<h3>Objetivos específicos</h3>" + UL(obj[ie_ + 1:]) + "</section>")
it = pub.index("Nível")
niveis = pub[it + 2:]
h.append('<section class="cont"><h2><span>3</span>Público-alvo e lógica multiprofissional</h2>' + "".join(P(x) for x in pub[:it]) +
         '<table class="niveis"><tr><th>Nível</th><th>O que se espera do profissional</th></tr>' +
         "".join(f"<tr><td><b>{e(niveis[j])}</b></td><td>{e(niveis[j + 1])}</td></tr>" for j in range(0, len(niveis) - 1, 2)) + "</table></section>")

# 4 estrutura
linhas = "".join(f"<tr><td>{n}</td><td>{e(m['nome'])}</td><td class='n'>{len(m['aulas'])}</td><td class='n'>{hm(m['min'])}</td><td class='n'>{m['slides']}</td><td class='n'>{m['ch']} h</td></tr>" for n, m in mods.items())
h.append(f"""<section><h2><span>4</span>Estrutura curricular</h2>
<p>O curso é composto por {len(mods)} módulos e {TOT_A} aulas, totalizando 400 horas de carga horária. A carga excede o mínimo regulatório de 360 horas exigido para cursos de especialização, com folga destinada aos módulos de populações específicas, de integração e ao projeto aplicado.</p>
<table class="estr"><tr><th>Nº</th><th>Módulo</th><th class='n'>Aulas</th><th class='n'>Videoaula</th><th class='n'>Slides</th><th class='n'>CH total</th></tr>{linhas}
<tr class="tot"><td></td><td>Total</td><td class='n'>{TOT_A}</td><td class='n'>{hm(TOT_M)}</td><td class='n'>{TOT_S}</td><td class='n'>400 h</td></tr></table>
<p>A sequência foi organizada em cinco blocos lógicos: fundamentos e fisiologia (módulos 1 a 3), nutrição e recursos ergogênicos (4 e 5), clínica, lesão e reabilitação (6 a 8), carga e comportamento (9 e 10), populações específicas (11 a 13), fechando com o módulo de integração e projeto aplicado (14). O bloco de populações específicas percorre todo o espectro da prática: a atleta mulher, os extremos etários e o praticante amador, que é numericamente majoritário e clinicamente o mais frequente na rotina da maior parte dos egressos.</p>
<p>A carga horária total não corresponde a tempo de vídeo. Em conformidade com a modalidade a distância, ela reúne videoaula, leitura dirigida, estudos de caso, fóruns, encontros síncronos, avaliação e projeto aplicado. A videoaula soma {hm(TOT_M)}, cerca de {round(TOT_M / 60 / 400 * 100)}% da carga total; as demais horas de cada módulo são distribuídas entre essas atividades.</p></section>""")

# 5 formato
arq = [("NÚMERO", "Abre com um dado que não fecha com a intuição e passa a aula desmontando-o: de onde veio, em quem foi medido e o que sobra de verdadeiro.", "Epidemiologia, dose, evidência de intervenção."),
       ("ERRO", "Abre com uma conduta plausível, difundida e errada, e disseca por que ela parece certa.", "Mitos consolidados, exame desnecessário, protocolo mal transposto."),
       ("PROCEDIMENTO", "Percorre um raciocínio estruturado do começo ao fim, em ordem: o que se pergunta, o que se examina, o que se pede, o que se conclui.", "Avaliação, triagem, interpretação de exame, fluxo de emergência."),
       ("DECISÃO", "Apresenta uma encruzilhada real com duas ou três saídas defensáveis e percorre cada uma até as consequências.", "Retorno ao esporte, suspender ou manter treino, encaminhar ou conduzir."),
       ("CASO", "Um paciente, uma linha do tempo e o percurso do raciocínio. Uso raro e proposital, no máximo dois por módulo.", "Quando o erro só aparece ao longo do tempo; aulas integradoras.")]
h.append(f"""<section><h2><span>5</span>Formato didático das aulas</h2>
<p>Cada aula tem duração definida pelo conteúdo, entre 7 e 25 minutos, com roteiro escrito para teleprompter a 118 palavras por minuto e apresentação de slides desenhados para aquela aula. Cada aula segue uma de cinco arquiteturas, em rodízio dentro do módulo, de modo que duas aulas seguidas nunca repetem o mesmo formato.</p>
<table class="arq"><tr><th>Arquitetura</th><th>Como a aula se organiza</th><th>Usada para</th><th class='n'>Aulas</th></tr>""" +
         "".join(f"<tr><td><b>{a}</b></td><td>{e(d)}</td><td>{e(u)}</td><td class='n'>{ARQ.get(a, 0)}</td></tr>" for a, d, u in arq) + """</table>
<p>Os casos são, em regra, perfis típicos sem nome e sem desfecho; o caso clínico com linha do tempo é exceção justificada. Cada aula termina com três regras práticas e com a indicação de quem faz o quê na equipe. A última aula de cada módulo fecha o módulo inteiro nos três níveis de responsabilidade (Decisão, Contribuição e Reconhecimento), e cada aula traz notas de produção com os números conferidos nas fontes e as referências.</p></section>""")

# 6 módulos
h.append('<section class="abre"><h2><span>6</span>Detalhamento dos módulos</h2><p>Cada módulo é descrito por ementa, competências desenvolvidas, grade das aulas roteirizadas, com duração e arquitetura de cada uma, e pela camada de integração multiprofissional, que explicita o nível de responsabilidade esperado de cada área.</p></section>')
for n, m in mods.items():
    grade = "".join(f"<tr><td class='num'>{a[0]}</td><td>{e(a[1])}</td><td class='arqc'>{a[4].capitalize()}</td><td class='n'>{a[2]} min</td></tr>" for a in m["aulas"])
    h.append(f"""<section class="mod"><div class="modtopo"><div class="modn">Módulo {n}</div><h2 class="modh">{e(m['nome'])}</h2>
<div class="modinfo">{m['ch']} horas de carga horária · {len(m['aulas'])} aulas · {hm(m['min'])} de videoaula · {m['slides']} slides</div></div>
<h3>Ementa</h3>{P(m['ementa'])}<h3>Competências desenvolvidas</h3>{UL(m['comp'])}
<h3>Grade de aulas</h3><table class="grade"><tr><th>Nº</th><th>Aula</th><th>Formato</th><th class='n'>Duração</th></tr>{grade}</table>
<h3>Integração multiprofissional</h3>{P(m['integ'])}</section>""")

# 7-11
h.append(f"""<section><h2><span>7</span>Metodologia</h2>
<p>O curso é ofertado na modalidade a distância, com estrutura assíncrona de videoaulas roteirizadas, slides próprios por aula, estudos de caso, fóruns de discussão multiprofissional e encontros síncronos periódicos de integração.</p>
<h3>Recursos didáticos por módulo</h3><ul>
<li>Videoaulas de 7 a 25 minutos, cada uma com roteiro, slides próprios e referências conferidas.</li>
<li>Casos integrados, retomados em módulos diferentes sob perspectivas distintas, e um módulo final dedicado a casos que exigem várias profissões.</li>
<li>Leitura dirigida de documentos de consenso e diretrizes, com roteiro de leitura crítica.</li>
<li>Fóruns de discussão com composição multiprofissional obrigatória.</li>
<li>Encontros síncronos de integração ao término de cada bloco temático, que também concentram a discussão aprofundada dos temas estruturantes.</li></ul>
<h2 class="seg"><span>8</span>Sistema de avaliação</h2>
<p>A avaliação combina verificação de conteúdo por módulo e avaliação integrada de desempenho, com peso maior atribuído à capacidade de aplicação e de decisão compartilhada.</p>
<table class="aval"><tr><th>Instrumento</th><th>Descrição</th><th class='n'>Peso</th></tr>
<tr><td><b>Avaliação por módulo</b></td><td>Prova objetiva ao final de cada módulo, com questões de aplicação e não de memorização.</td><td class='n'>30%</td></tr>
<tr><td><b>Estudos de caso</b></td><td>Resolução escrita de casos, com justificativa de conduta e identificação de encaminhamentos.</td><td class='n'>25%</td></tr>
<tr><td><b>Participação nos fóruns</b></td><td>Contribuição técnica qualificada em discussões multiprofissionais.</td><td class='n'>10%</td></tr>
<tr><td><b>Projeto aplicado</b></td><td>Trabalho de conclusão com defesa, conforme a seção 9.</td><td class='n'>35%</td></tr></table>
<p>Aprovação condicionada a aproveitamento mínimo de 70% e frequência mínima de 75% nas atividades registradas no ambiente virtual.</p></section>""")
ie2 = proj.index("Elementos obrigatórios")
h.append('<section><h2><span>9</span>Projeto aplicado de conclusão</h2>' + "".join(P(x) for x in proj[:ie2]) +
         "<h3>Elementos obrigatórios</h3>" + UL(proj[ie2 + 1:-1]) + P(proj[-1]) +
         "<p>O método do projeto é ensinado nas três últimas aulas do curso: a definição do problema numa frase, com lugar, pessoas, situação atual medida, meta e motivo; os indicadores de processo, de resultado e de equilíbrio, com linha de base, ciclos de teste pequeno e gráfico de sequência; e a estrutura da defesa diante da banca multiprofissional.</p>"
         '<h2 class="seg"><span>10</span>Perfil do corpo docente</h2>' + P(doc[0]) + UL(doc[1:]) +
         '<h2 class="seg"><span>11</span>Observações regulatórias</h2>' + "".join(P(x) for x in reg) + "</section>")
h.append('<section class="fontes"><h2><span>12</span>Fontes consultadas</h2><p>Documentos de consenso, diretrizes e normativas utilizados na construção desta matriz curricular. As referências específicas de cada aula constam no respectivo roteiro.</p><ol>' +
         "".join(f"<li>{e(limpa(f))}</li>" for f in fontes[1:] if not f.startswith("Documentos de consenso")) + "</ol></section>")

CSS = open(__file__.replace("gerar_projeto.py", "estilo.css"), encoding="utf-8").read()
open(SAIDA, "w", encoding="utf-8").write(f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Ciências do Esporte Aplicadas à Saúde: projeto pedagógico</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>{CSS}</style></head><body>{''.join(h)}</body></html>""")
print("ok", TOT_A, hm(TOT_M), TOT_S, ARQ)
