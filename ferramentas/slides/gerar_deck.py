#!/usr/bin/env python3
"""Gera um deck do tipo Slides (project/deck.json + project/slides/<id>.html)
a partir de um spec JSON da aula, no padrão visual do curso (docs/08).

Uso: python3 gerar_deck.py slides/MOD01/01-01.json <pasta_saida>

As notas do apresentador de cada slide de conteúdo vêm do texto falado da
aula (o bloco entre um marcador de slide e o próximo), na mesma ordem.
Nenhum número de aula ou de módulo aparece na tela.
"""
import json, re, sys, os, html, datetime

TINTA, PAPEL, QUENTE, CARD = "#12202E", "#F7F6F2", "#EDEAE2", "#FDFCF9"
VERM, PETR, AMBAR = "#A8322A", "#1F6F6B", "#C8922F"
APOIO, APOIO2, RODAPE = "#4A5A68", "#3A4A57", "#6B7A87"
SERIF = "'Libre Baskerville', Georgia, serif"

# Cor da capa e do fecho por módulo (spec["tema"]). O miolo não muda.
# fundo, card escuro, filete, eyebrow, subtítulo/título de card, texto de apoio
TEMAS = {
    "tinta":    {"fundo": TINTA,     "card": "#1B2E3F", "linha": "#2E4053", "eyebrow": "#7FC4BE", "sub": "#E88C7D", "apoio": "#BFD0DA"},
    "bordo":    {"fundo": "#3A1A22", "card": "#4A2530", "linha": "#5E3844", "eyebrow": "#7FC4BE", "sub": "#E6C08A", "apoio": "#E3CDCF"},
    "petroleo": {"fundo": "#0F3432", "card": "#184442", "linha": "#2A5A57", "eyebrow": "#E6C08A", "sub": "#F2A58F", "apoio": "#C9DDDA"},
    "ameixa":   {"fundo": "#2B1E38", "card": "#3A2B48", "linha": "#4E3E5E", "eyebrow": "#E6C08A", "sub": "#7FC4BE", "apoio": "#D9CFE3"},
}
SANS = "'IBM Plex Sans', Arial, sans-serif"

SIMBOLO = ('<path d="M75.9,28.5 A34,34 0 1,0 75.9,67.5" stroke-width="7"/>'
           '<path d="M40,48 L62,48 L67,37 L72,60 L77,43 L82,48 L91,48" stroke-width="6.5"/>')

def simbolo(escuro):
    if escuro:
        cor, tam, op = PAPEL, 72, "0.7"
    else:
        cor, tam, op = "#97A4AE", 40, "1"
    return (f'<svg aria-label="Símbolo do curso" width="96" height="96" viewBox="0 0 96 96" '
            f'style="position:absolute; right:128px; top:{128 - (4 if not escuro else 8)}px; width:{tam}px; height:{tam}px; opacity:{op}">'
            f'<g fill="none" stroke="{cor}" stroke-linecap="round" stroke-linejoin="round">{SIMBOLO}</g></svg>')

def esc_nota(t):
    return html.escape(t, quote=False)

def eyebrow(t, escuro=False, cor=None):
    cor = cor or ("#7FC4BE" if escuro else VERM)
    return f'<p style="font-size:26px; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; color:{cor}; width:1500px">{t}</p>'

def titulo(t, escuro=False):
    cor = PAPEL if escuro else TINTA
    return f'<h2 style="font-family:{SERIF}; font-size:60px; font-weight:700; line-height:1.15; color:{cor}">{t}</h2>'

def rodape(esq, n, total, escuro=False):
    return (f'<p style="position:absolute; left:128px; bottom:64px; width:1300px; font-size:24px; color:{RODAPE}">{esq}</p>'
            f'<p style="position:absolute; right:128px; bottom:64px; width:200px; text-align:right; font-size:24px; color:{RODAPE}">{n} / {total}</p>')

def secao(sid, bg, corpo, gap=36, just=None, cor=TINTA):
    j = f"; justify-content:{just}" if just else ""
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg}; color:{cor}; font-family:{SANS}; '
            f'padding:128px 128px 160px; display:flex; flex-direction:column; gap:{gap}px{j}">\n{corpo}\n')

def card(c, borda=None, escuro=False, tema=None):
    tema = tema or TEMAS["tinta"]
    fundo = tema["card"] if escuro else CARD
    b = f"border-top:8px solid {borda}; " if borda else ("" if escuro else "border:1px solid #DDD8CC; ")
    ct = tema["sub"] if escuro else TINTA
    cx = "#DCE6EC" if escuro else APOIO2
    h = f'<h3 style="font-size:36px; font-weight:600; line-height:1.2; color:{ct}">{c["t"]}</h3>' if c.get("t") else ""
    x = f'<p style="font-size:28px; line-height:1.45; color:{cx}">{c["x"]}</p>' if c.get("x") else ""
    return f'<div style="flex:1; {b}background:{fundo}; border-radius:16px; padding:32px; display:flex; flex-direction:column; gap:14px">{h}{x}</div>'

def destaque(t, cor=PETR, escuro=False):
    fundo = "#1B2E3F" if escuro else CARD
    tc = PAPEL if escuro else TINTA
    return f'<div style="background:{fundo}; border-left:8px solid {cor}; border-radius:8px; padding:24px 30px"><p style="font-size:30px; line-height:1.4; color:{tc}">{t}</p></div>'

CORES = {"verm": VERM, "petr": PETR, "ambar": AMBAR, "tinta": TINTA}

def miolo(s, bg):
    """Corpo de um slide de conteúdo conforme o tipo."""
    tipo = s["tipo"]
    out = []
    if tipo == "cards":
        linhas = s["cards"]
        por = s.get("por_linha", len(linhas))
        for i in range(0, len(linhas), por):
            fila = linhas[i:i + por]
            out.append('<div style="display:flex; gap:24px">' +
                       "".join(card(c, CORES.get(c.get("cor"))) for c in fila) + '</div>')
    elif tipo == "numeros":
        blocos = []
        for n in s["numeros"]:
            cor = CORES.get(n.get("cor"), VERM)
            blocos.append(
                f'<div style="flex:1; display:flex; flex-direction:column; gap:10px; border-top:6px solid {cor}; padding:24px 0 0">'
                f'<p style="font-family:{SERIF}; font-size:96px; font-weight:700; line-height:1.05; color:{cor}">{n["n"]}</p>'
                f'<p style="font-size:28px; line-height:1.4; color:{APOIO2}">{n["x"]}</p></div>')
        out.append('<div style="display:flex; gap:48px">' + "".join(blocos) + '</div>')
    elif tipo == "lista":
        itens = []
        for i, it in enumerate(s["itens"], 1):
            marca = it.get("m", str(i))
            cor = CORES.get(it.get("cor"), PETR)
            corpo = f'<h3 style="font-size:36px; font-weight:600; line-height:1.25; color:{TINTA}">{it["t"]}</h3>'
            if it.get("x"):
                corpo += f'<p style="font-size:28px; line-height:1.45; color:{APOIO2}">{it["x"]}</p>'
            itens.append(
                f'<div style="display:flex; gap:28px; align-items:start">'
                f'<p style="flex:none; width:64px; height:64px; border-radius:50%; background:{cor}; color:{PAPEL}; font-size:30px; font-weight:600; line-height:64px; text-align:center">{marca}</p>'
                f'<div style="flex:1; display:flex; flex-direction:column; gap:6px">{corpo}</div></div>')
        out.append(f'<div style="display:flex; flex-direction:column; gap:{s.get("gap_itens", 28)}px">' + "".join(itens) + '</div>')
    elif tipo == "duas":
        cols = []
        for c in (s["esq"], s["dir"]):
            cor = CORES.get(c.get("cor"), PETR)
            lis = "".join(f'<li>{x}</li>' for x in c["itens"])
            cols.append(
                f'<div style="flex:1; background:{CARD}; border-top:8px solid {cor}; border-radius:16px; padding:32px; display:flex; flex-direction:column; gap:18px">'
                f'<h3 style="font-size:38px; font-weight:600; line-height:1.2; color:{cor}">{c["t"]}</h3>'
                f'<ul style="font-size:28px; line-height:1.5; color:{APOIO2}">{lis}</ul></div>')
        out.append('<div style="display:flex; gap:32px">' + "".join(cols) + '</div>')
    elif tipo == "tabela":
        larg = s.get("larguras")
        cab = s["cab"]
        w = lambda i: f' style="width:{larg[i]}%"' if larg else ""
        linhas = ['<tr>' + "".join(f'<th{w(i)}>{h}</th>' for i, h in enumerate(cab)) + '</tr>']
        for ln in s["linhas"]:
            linhas.append('<tr>' + "".join(f'<td>{c}</td>' for c in ln) + '</tr>')
        out.append(f'<table style="font-size:{s.get("tam", 28)}px; color:{APOIO2}; background:{CARD}; border-radius:12px">' + "".join(linhas) + '</table>')
    elif tipo == "html":
        out.append(s["corpo"])
    elif tipo == "diagrama":
        w, h = s.get("w", 1664), s["h"]
        partes = [f'<div style="position:relative; width:{w}px; height:{h}px">']
        svg = s["svg"]
        if 'style="' not in svg[:200]:
            svg = svg.replace("<svg ", '<svg style="position:absolute; left:0px; top:0px" ', 1)
        partes.append(svg)
        for r in s.get("rotulos", []):
            estilo = (f'position:absolute; left:{r["x"]}px; top:{r["y"]}px; width:{r.get("w", 300)}px; '
                      f'font-size:{r.get("tam", 26)}px; line-height:{r.get("lh", 1.25)}; font-weight:{r.get("peso", 400)}; '
                      f'color:{r.get("cor", APOIO2)}; text-align:{r.get("alinha", "left")}')
            if r.get("serif"):
                estilo += f"; font-family:{SERIF}"
            partes.append(f'<p style="{estilo}">{r["t"]}</p>')
        partes.append('</div>')
        if len(s.get("rotulos", [])) + 1 > 24:
            raise SystemExit(f"slide {s['id']}: mais de 24 elementos fixados no diagrama")
        out.append("".join(partes))
    else:
        raise SystemExit(f"tipo desconhecido: {tipo}")
    if s.get("destaque"):
        out.append(destaque(s["destaque"], CORES.get(s.get("destaque_cor"), PETR)))
    if s.get("fonte"):
        out.append(f'<p style="font-size:24px; color:{RODAPE}">{s["fonte"]}</p>')
    return "\n".join(out)

def notas_da_aula(md_path):
    txt = open(md_path, encoding="utf-8").read().split("## Referências")[0]
    blocos = re.split(r"^📊 \*\*\[SLIDE \d+ DE \d+\]\*\*\s*$", txt, flags=re.M)[1:]
    notas = []
    for b in blocos:
        ls = [l.strip() for l in b.split("\n")]
        ls = [l for l in ls if l and not l.startswith("*Visual") and not l.startswith("*Teleprompter") and l != "---"]
        t = " ".join(ls).replace("**", "")
        if len(t) > 3900:
            corte = t[:3900].rfind(". ")
            t = t[:corte + 1] + " (continua no teleprompter)"
        notas.append(t)
    return notas

def gerar(spec_path, saida):
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    spec = json.load(open(spec_path, encoding="utf-8"))
    notas = notas_da_aula(os.path.join(raiz, spec["arquivo"]))
    slides = spec["slides"]
    if len(slides) != len(notas):
        raise SystemExit(f"spec tem {len(slides)} slides de conteúdo e a aula tem {len(notas)}")
    total = len(slides) + 1
    rod = spec["titulo"]
    tema = TEMAS[spec.get("tema", "tinta")]
    pasta = os.path.join(saida, "project", "slides")
    os.makedirs(pasta, exist_ok=True)
    ordem = ["capa"]

    # Capa
    corpo = (simbolo(True) +
             f'<p style="font-size:28px; font-weight:500; letter-spacing:0.06em; text-transform:uppercase; color:{tema["eyebrow"]}; width:1400px">Pós-Graduação em Ciências do Esporte Aplicadas à Saúde</p>'
             f'<div style="display:flex; flex-direction:column; gap:24px">'
             f'<h1 style="font-family:{SERIF}; font-size:92px; font-weight:700; line-height:1.1; color:{PAPEL}">{spec["titulo"]}</h1>'
             + (f'<h2 style="font-family:{SERIF}; font-size:52px; font-weight:400; font-style:italic; line-height:1.2; color:{tema["sub"]}">{spec["subtitulo"]}</h2>' if spec.get("subtitulo") else "")
             + '</div>'
             f'<div style="display:flex; gap:64px; border-top:2px solid {tema["linha"]}; padding:32px 0 0">'
             f'<p style="font-size:30px; color:{tema["apoio"]}">{spec["modulo"]}</p></div>')
    capa = (f'<section id="capa" data-transition="fade" style="background:{tema["fundo"]}; color:{PAPEL}; font-family:{SANS}; padding:128px; '
            f'display:flex; flex-direction:column; justify-content:space-between; gap:48px">\n{corpo}\n'
            f'<aside>{esc_nota(spec.get("nota_capa", "Capa. Entra com calma e segue para o primeiro slide."))}</aside>\n</section>\n')
    open(os.path.join(pasta, "capa.html"), "w", encoding="utf-8").write(capa)

    alterna = 0
    for i, s in enumerate(slides):
        n = i + 2
        sid = s["id"]
        ordem.append(sid)
        nota = f'<aside>{esc_nota(notas[i])}</aside>\n</section>\n'
        if s["tipo"] == "frase":
            bg = CORES.get(s.get("fundo"), PETR)
            corpo = (simbolo(True) + eyebrow(s.get("eyebrow", ""), True) +
                     f'<div style="flex:1"></div>'
                     f'<p style="font-family:{SERIF}; font-size:{s.get("tam", 64)}px; font-weight:700; line-height:1.25; color:{PAPEL}; width:1560px">{s["frase"]}</p>'
                     + (f'<p style="font-size:30px; line-height:1.4; color:#DCE6EC; width:1500px">{s["apoio"]}</p>' if s.get("apoio") else "")
                     + '<div style="flex:1"></div>' + rodape(rod, n, total, True))
            html_s = secao(sid, bg, corpo, gap=32, cor=PAPEL) + nota
        elif s["tipo"] == "fecho":
            regras = "".join(f"<li>{r}</li>" for r in s["regras"])
            cartoes = ('<div style="display:flex; gap:24px">' + "".join(card(c, None, escuro=True, tema=tema) for c in s["cards"]) + '</div>') if s.get("cards") else ""
            corpo = (simbolo(True) + eyebrow(s.get("eyebrow", "O que fica"), True, tema["eyebrow"]) + titulo(s["titulo"], True) +
                     f'<ol style="font-size:30px; line-height:1.5; color:{PAPEL}">{regras}</ol>' + cartoes
                     + (f'<p style="font-size:26px; line-height:1.45; color:{tema["apoio"]}">{s["quem"]}</p>' if s.get("quem") else "")
                     + f'<p style="position:absolute; right:128px; bottom:64px; width:200px; text-align:right; font-size:24px; color:#9FB0BD">{n} / {total}</p>')
            html_s = secao(sid, tema["fundo"], corpo, gap=30, cor=PAPEL) + nota
        else:
            bg = PAPEL if alterna % 2 == 0 else QUENTE
            alterna += 1
            corpo = (simbolo(False) + eyebrow(s.get("eyebrow", "")) + titulo(s["titulo"]) + miolo(s, bg) + rodape(rod, n, total))
            html_s = secao(sid, bg, corpo, gap=s.get("gap", 34)) + nota
        open(os.path.join(pasta, f"{sid}.html"), "w", encoding="utf-8").write(html_s)

    agora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    secoes = {}
    for k, v in spec.get("secoes", {}).items():
        secoes[k] = {"description": v[0], "start": v[1]}
    if not secoes:
        secoes = {"aula": {"description": spec["titulo"], "start": "capa"}}
    deck = {
        "v": 4,
        "createdOnFiles": {"v": 1, "at": agora},
        "title": spec["titulo"],
        "order": ordem,
        "sections": secoes,
        "faces": {
            "libre-baskerville": {"family": "Libre Baskerville", "href": "https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap"},
            "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap"},
        },
        "designSystems": [],
    }
    json.dump(deck, open(os.path.join(saida, "project", "deck.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{spec['titulo']}: {total} slides em {saida}")
    return ordem

if __name__ == "__main__":
    gerar(sys.argv[1], sys.argv[2])
