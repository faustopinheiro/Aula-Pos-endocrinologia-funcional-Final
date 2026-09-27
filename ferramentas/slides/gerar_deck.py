#!/usr/bin/env python3
"""Gera um deck do tipo Slides (project/deck.json + project/slides/<id>.html)
a partir de um spec JSON da aula, no padrão visual do curso (docs/08).

Uso: python3 gerar_deck.py slides/MOD01/01-01.json <pasta_saida>

As notas do apresentador de cada slide de conteúdo vêm do texto falado da
aula (o bloco entre um marcador de slide e o próximo), na mesma ordem.
Nenhum número de aula ou de módulo aparece na tela.
"""
import json, re, sys, os, html, datetime, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icones import icone, svg_icone

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
    "anil":     {"fundo": "#1C2340", "card": "#283056", "linha": "#3A426C", "eyebrow": "#E6C08A", "sub": "#8FD3C8", "apoio": "#D2D6EA"},
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
    if c.get("ic"):
        h = svg_icone(c["ic"], 72, ct if escuro else (borda or PETR)) + h
    x = f'<p style="font-size:28px; line-height:1.45; color:{cx}">{c["x"]}</p>' if c.get("x") else ""
    return f'<div style="flex:1; {b}background:{fundo}; border-radius:16px; padding:32px; display:flex; flex-direction:column; gap:14px">{h}{x}</div>'

def destaque(t, cor=PETR, escuro=False):
    fundo = "#1B2E3F" if escuro else CARD
    tc = PAPEL if escuro else TINTA
    return f'<div style="background:{fundo}; border-left:8px solid {cor}; border-radius:8px; padding:24px 30px"><p style="font-size:30px; line-height:1.4; color:{tc}">{t}</p></div>'

CORES = {"verm": VERM, "petr": PETR, "ambar": AMBAR, "tinta": TINTA}
LIMITE_PALAVRAS = 45

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
            ic_n = svg_icone(n["ic"], 110, cor) if n.get("ic") else ""
            blocos.append(
                f'<div style="flex:1; display:flex; flex-direction:column; gap:10px; border-top:6px solid {cor}; padding:24px 0 0">'
                + ic_n +
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


# ---------------------------------------------------------------------------
# Layouts visuais (segunda versão): menos texto na tela, uma figura por slide
# e composições diferentes entre si. O texto longo fica nas notas.
# ---------------------------------------------------------------------------

CLARO = {"verm": "#F2DEDA", "petr": "#DCEBE9", "ambar": "#F4E8D2", "tinta": "#DDE3E8"}
ESCURO_TXT = {"verm": VERM, "petr": PETR, "ambar": "#9A6A12", "tinta": TINTA}

def cor_de(c, padrao="petr"):
    return CORES.get(c or padrao, PETR)

def claro_de(c, padrao="petr"):
    return CLARO.get(c or padrao, CLARO["petr"])

def desenho(w, h, partes, rotulos, alt):
    """Host relativo com um svg (partes = conteúdo interno) e rótulos em <p> fixados."""
    svg = (f'<svg aria-label="{alt}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
           f'style="position:absolute; left:0px; top:0px">' + "".join(partes) + '</svg>')
    ps = []
    for r in rotulos:
        est = (f'position:absolute; left:{round(r["x"])}px; top:{round(r["y"])}px; width:{round(r.get("w", 300))}px; '
               f'font-size:{r.get("tam", 28)}px; line-height:{r.get("lh", 1.25)}; font-weight:{r.get("peso", 400)}; '
               f'color:{r.get("cor", APOIO2)}; text-align:{r.get("alinha", "left")}')
        if r.get("serif"):
            est += f"; font-family:{SERIF}"
        ps.append(f'<p style="{est}">{r["t"]}</p>')
    if len(ps) + 1 > 24:
        raise SystemExit(f"desenho '{alt}': mais de 24 rótulos")
    return f'<div style="position:relative; width:{w}px; height:{h}px; flex:none">' + svg + "".join(ps) + '</div>'

def R(x, y, t, w=300, tam=28, cor=APOIO2, peso=400, alinha="left", serif=False, lh=1.25):
    return {"x": x, "y": y, "t": t, "w": w, "tam": tam, "cor": cor, "peso": peso, "alinha": alinha, "serif": serif, "lh": lh}

def circulo_icone(nome, d, cor, fundo):
    """Ícone dentro de um círculo colorido, como svg de fluxo."""
    m = d * 0.24
    return (f'<svg aria-label="{nome.split(":")[1].replace("-", " ")}" width="{d}" height="{d}" viewBox="0 0 {d} {d}">'
            f'<circle cx="{d/2}" cy="{d/2}" r="{d/2}" fill="{fundo}"/>' + icone(nome, m, m, d - 2 * m, cor) + '</svg>')

def cabeca(s, escuro=False):
    out = ""
    if s.get("eyebrow"):
        out += eyebrow(s["eyebrow"], escuro)
    if s.get("titulo"):
        out += titulo(s["titulo"], escuro)
    return out

def pe(s):
    out = ""
    if s.get("destaque"):
        out += destaque(s["destaque"], cor_de(s.get("destaque_cor"), "tinta"))
    if s.get("fonte"):
        out += f'<p style="font-size:24px; color:{RODAPE}">{s["fonte"]}</p>'
    return out

def v_icones(s):
    itens = s["itens"]
    d = s.get("d", 220 if len(itens) <= 3 else 190)
    cols = []
    for it in itens:
        c = it.get("cor", "petr")
        x = (f'<p style="font-size:28px; line-height:1.4; color:{APOIO2}; text-align:center">{it["x"]}</p>' if it.get("x") else "")
        cols.append(f'<div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:22px">'
                    + circulo_icone(it["ic"], d, cor_de(c), claro_de(c))
                    + f'<h3 style="font-size:40px; font-weight:600; line-height:1.2; color:{ESCURO_TXT.get(c, TINTA)}; text-align:center">{it["t"]}</h3>'
                    + x + '</div>')
    return cabeca(s) + '<div style="flex:1"></div><div style="display:flex; gap:48px; align-items:start">' + "".join(cols) + '</div><div style="flex:1"></div>' + pe(s)

def v_checklist(s):
    itens = s["itens"]
    por = s.get("colunas", 2 if len(itens) > 3 else 1)
    linhas_ = []
    for i in range(0, len(itens), por):
        fila = []
        for it in itens[i:i + por]:
            c = it.get("cor", "petr")
            txt = f'<h3 style="font-size:40px; font-weight:600; line-height:1.25; color:{TINTA}">{it["t"]}</h3>'
            if it.get("x"):
                txt += f'<p style="font-size:28px; line-height:1.4; color:{APOIO2}">{it["x"]}</p>'
            fila.append(f'<div style="flex:1; display:flex; gap:32px; align-items:center; background:{CARD}; border-radius:24px; padding:32px 36px">'
                        + circulo_icone(it["ic"], 136, cor_de(c), claro_de(c))
                        + f'<div style="flex:1; display:flex; flex-direction:column; gap:6px">{txt}</div></div>')
        linhas_.append('<div style="display:flex; gap:28px">' + "".join(fila) + '</div>')
    return cabeca(s) + '<div style="flex:1"></div><div style="display:flex; flex-direction:column; gap:28px">' + "".join(linhas_) + '</div><div style="flex:1"></div>' + pe(s)

def v_pictograma(s):
    total, k = s.get("total", 100), s["marcados"]
    cols = s.get("colunas", 10)
    linhas_n = math.ceil(total / cols)
    tam, passo = s.get("tam", 46), s.get("passo", 56)
    w, h = cols * passo, linhas_n * passo
    c = s.get("cor", "verm")
    partes = []
    for i in range(total):
        x, y = (i % cols) * passo, (i // cols) * passo
        partes.append(icone(s.get("ic", "h:person"), x, y, tam, cor_de(c) if i < k else "#C9CFD4"))
    figura = desenho(w, h, partes, [], s.get("alt", f"{k} de {total} destacados"))
    lado = (f'<div style="flex:1; display:flex; flex-direction:column; gap:20px; justify-content:center">'
            f'<p style="font-family:{SERIF}; font-size:{s.get("tam_numero", 150)}px; font-weight:700; line-height:1; color:{cor_de(c)}">{s["numero"]}</p>'
            f'<p style="font-size:36px; line-height:1.35; color:{TINTA}; font-weight:500">{s["legenda"]}</p>'
            + (f'<p style="font-size:28px; line-height:1.4; color:{APOIO2}">{s["x"]}</p>' if s.get("x") else "") + '</div>')
    return cabeca(s) + f'<div style="display:flex; gap:96px; align-items:center">{figura}{lado}</div>' + pe(s)

def v_hero(s):
    c = s.get("cor", "verm")
    esq = (f'<div style="flex:1; display:flex; flex-direction:column; gap:24px; justify-content:center">'
           f'<p style="font-family:{SERIF}; font-size:{s.get("tam", 200)}px; font-weight:700; line-height:1; color:{cor_de(c)}">{s["valor"]}</p>'
           f'<p style="font-size:40px; line-height:1.3; color:{TINTA}; font-weight:500; width:900px">{s["texto"]}</p>'
           + (f'<p style="font-size:28px; line-height:1.4; color:{APOIO2}; width:900px">{s["x"]}</p>' if s.get("x") else "") + '</div>')
    return (cabeca(s) + '<div style="flex:1"></div><div style="display:flex; gap:64px; align-items:center">' + esq
            + circulo_icone(s["ic"], s.get("d", 440), cor_de(c), claro_de(c)) + '</div><div style="flex:1"></div>' + pe(s))

def v_fluxo(s):
    passos = s["passos"]
    k = len(passos)
    w, d = 1664, s.get("d", 210 if k <= 4 else 170)
    passo = w / k
    c = s.get("cor", "petr")
    partes = ['<defs>' + seta_mk("fx", MUDO_) + '</defs>']
    rots = []
    for i, p in enumerate(passos):
        cx = passo * i + passo / 2
        cc = p.get("cor", c)
        partes.append(f'<circle cx="{cx:.1f}" cy="{d/2}" r="{d/2}" fill="{claro_de(cc)}"/>')
        partes.append(icone(p["ic"], cx - d * 0.3, d * 0.2, d * 0.6, cor_de(cc)))
        if i < k - 1:
            x1, x2 = cx + d / 2 + 18, cx + passo - d / 2 - 26
            partes.append(f'<line x1="{x1:.1f}" y1="{d/2}" x2="{x2:.1f}" y2="{d/2}" stroke="{MUDO_}" stroke-width="4" marker-end="url(#fx)"/>')
        rots.append(R(cx - passo / 2 + 12, d + 28, p["t"], w=passo - 24, tam=38, cor=ESCURO_TXT.get(cc, TINTA), peso=700, alinha="center"))
        if p.get("x"):
            rots.append(R(cx - passo / 2 + 12, d + 28 + 54 * (1 + (len(p["t"]) > 16)), p["x"], w=passo - 24, tam=28, cor=APOIO2, alinha="center", lh=1.35))
    h = d + 28 + 54 * 2 + 40 * 3
    return cabeca(s) + '<div style="flex:1"></div>' + desenho(w, h, partes, rots, s.get("alt", "Fluxo em etapas")) + '<div style="flex:1"></div>' + pe(s)

def v_espectro(s):
    w, h = 1664, 420
    marcas = s["marcas"]
    x0, x1, y = 60, w - 60, 200
    c0, c1 = (VERM, PETR) if s.get("inverter") else (PETR, VERM)
    partes = ['<defs><linearGradient id="esp" x1="0" x2="1" y1="0" y2="0">'
              f'<stop offset="0" stop-color="{c0}"/><stop offset="0.5" stop-color="{AMBAR}"/><stop offset="1" stop-color="{c1}"/></linearGradient></defs>',
              f'<rect x="{x0}" y="{y - 14}" width="{x1 - x0}" height="28" rx="14" fill="url(#esp)"/>']
    rots = [R(x0, y + 34, s["extremos"][0], w=420, tam=28, cor=c0, peso=600),
            R(x1 - 420, y + 34, s["extremos"][1], w=420, tam=28, cor=c1, peso=600, alinha="right")]
    k = len(marcas)
    for i, m in enumerate(marcas):
        pos = m.get("pos", (i + 0.5) / k)
        cx = x0 + pos * (x1 - x0)
        partes.append(f'<circle cx="{cx:.1f}" cy="{y}" r="22" fill="{PAPEL}" stroke="{TINTA}" stroke-width="5"/>')
        partes.append(icone(m["ic"], cx - 65, 10, 130, cor_de(m.get("cor"), "tinta")))
        rots.append(R(cx - 180, y + 84, m["t"], w=360, tam=36, cor=TINTA, peso=700, alinha="center"))
        if m.get("x"):
            rots.append(R(cx - 180, y + 136, m["x"], w=360, tam=28, cor=APOIO2, alinha="center"))
    return cabeca(s) + '<div style="flex:1"></div>' + desenho(w, h, partes, rots, s.get("alt", "Espectro contínuo")) + '<div style="flex:1"></div>' + pe(s)

def v_ciclo(s):
    nos = s["nos"]
    k = len(nos)
    w, h = 1664, s.get("h", 580)
    cx, cy, r, d = w / 2, h / 2, s.get("r", 205), 140
    partes = ['<defs>' + seta_mk("cc", MUDO_) + '</defs>']
    rots = []
    ang = [(-90 + 360 * i / k) for i in range(k)]
    for i, a in enumerate(ang):
        a1, a2 = math.radians(a + 360 / k * 0.25), math.radians(a + 360 / k * 0.75)
        partes.append(f'<path d="M {cx + r*math.cos(a1):.1f} {cy + r*math.sin(a1):.1f} A {r} {r} 0 0 1 {cx + r*math.cos(a2):.1f} {cy + r*math.sin(a2):.1f}" '
                      f'fill="none" stroke="{MUDO_}" stroke-width="5" marker-end="url(#cc)"/>')
    for i, (a, nd) in enumerate(zip(ang, nos)):
        px, py = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        c = nd.get("cor", "petr")
        partes.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{d/2}" fill="{claro_de(c)}" stroke="{PAPEL}" stroke-width="6"/>')
        partes.append(icone(nd["ic"], px - d * 0.3, py - d * 0.3, d * 0.6, cor_de(c)))
        direita = math.cos(math.radians(a)) > -0.2
        vert = abs(math.cos(math.radians(a))) < 0.3
        lx = px + d / 2 + (70 if vert else 24) if direita else px - d / 2 - 24 - 440
        al = "left" if direita else "right"
        ty = py - (44 if nd.get("x") else 22)
        rots.append(R(lx, ty, nd["t"], w=440, tam=36, cor=ESCURO_TXT.get(c, TINTA), peso=700, alinha=al))
        if nd.get("x"):
            rots.append(R(lx, ty + 48, nd["x"], w=440, tam=26, cor=APOIO2, alinha=al))
    if s.get("centro"):
        rots.append(R(cx - 115, cy - 40, s["centro"], w=230, tam=26, cor=TINTA, peso=700, alinha="center", serif=True))
    return cabeca(s) + '<div style="flex:1"></div>' + desenho(w, h, partes, rots, s.get("alt", "Ciclo")) + '<div style="flex:1"></div>' + pe(s)

def v_matriz(s):
    q = s["quadrantes"]  # 4 itens: sup-esq, sup-dir, inf-esq, inf-dir
    caixas = []
    for it in q:
        c = it.get("cor", "petr")
        caixas.append(f'<div style="background:{claro_de(c)}; border-radius:18px; padding:26px 30px; display:flex; gap:26px; align-items:center">'
                      + svg_icone(it["ic"], 96, cor_de(c))
                      + f'<div style="flex:1; display:flex; flex-direction:column; gap:6px"><h3 style="font-size:34px; font-weight:600; line-height:1.2; color:{ESCURO_TXT.get(c, TINTA)}">{it["t"]}</h3>'
                      + (f'<p style="font-size:26px; line-height:1.35; color:{APOIO2}">{it["x"]}</p>' if it.get("x") else "") + '</div></div>')
    eixo_x, eixo_y = s.get("eixos", ["", ""])
    grade = (f'<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px">' + "".join(caixas) + '</div>')
    rotulos_eixo = (f'<div style="display:flex; justify-content:space-between"><p style="font-size:26px; color:{MUDO_}; font-weight:600">{eixo_y}</p>'
                    f'<p style="font-size:26px; color:{MUDO_}; font-weight:600">{eixo_x}</p></div>') if eixo_x or eixo_y else ""
    return cabeca(s) + grade + rotulos_eixo + pe(s)

def v_linha_tempo(s):
    marcos = s["marcos"]
    k = len(marcos)
    w, h = 1664, 520
    y = 190
    partes = [f'<line x1="30" y1="{y}" x2="{w-30}" y2="{y}" stroke="{GRADE_}" stroke-width="6" stroke-linecap="round"/>']
    rots = []
    passo = (w - 60) / k
    for i, m in enumerate(marcos):
        cx = 30 + passo * i + passo / 2
        c = m.get("cor", "petr")
        partes.append(f'<circle cx="{cx:.1f}" cy="{y}" r="84" fill="{claro_de(c)}" stroke="{PAPEL}" stroke-width="8"/>')
        partes.append(icone(m["ic"], cx - 50, y - 50, 100, cor_de(c)))
        rots.append(R(cx - passo / 2 + 10, 30, m["quando"], w=passo - 20, tam=36, cor=cor_de(c), peso=700, alinha="center", serif=True))
        rots.append(R(cx - passo / 2 + 10, y + 104, m["t"], w=passo - 20, tam=36, cor=TINTA, peso=600, alinha="center"))
        if m.get("x"):
            rots.append(R(cx - passo / 2 + 10, y + 104 + 50 * (1 + (len(m["t"]) > 20)), m["x"], w=passo - 20, tam=28, cor=APOIO2, alinha="center"))
    return cabeca(s) + '<div style="flex:1"></div>' + desenho(w, h, partes, rots, s.get("alt", "Linha do tempo")) + '<div style="flex:1"></div>' + pe(s)

def v_barras(s):
    """Barras horizontais simples com ícone à esquerda. itens = [{ic, t, v, rot}] com v de 0 a vmax."""
    itens = s["itens"]
    vmax = s.get("vmax", max(i["v"] for i in itens))
    w = 1664
    passo, bh = s.get("passo", 118), 64
    h = passo * len(itens)
    xl, xb = 560, 580
    bw = w - xb - 180
    partes, rots = [], []
    for i, it in enumerate(itens):
        y = i * passo
        c = it.get("cor", "petr")
        partes.append(icone(it["ic"], 0, y + (bh - 72) / 2, 72, cor_de(c)))
        rots.append(R(96, y + bh / 2 - 20, it["t"], w=xl - 110, tam=30, cor=TINTA, peso=600))
        ww = bw * it["v"] / vmax
        partes.append(f'<rect x="{xb}" y="{y}" width="{bw}" height="{bh}" rx="8" fill="{GRADE_}" opacity="0.5"/>')
        partes.append(f'<rect x="{xb}" y="{y}" width="{ww:.1f}" height="{bh}" rx="8" fill="{cor_de(c)}"/>')
        rots.append(R(xb + ww + 20, y + bh / 2 - 24, it.get("rot", f'{it["v"]:g}'), w=260, tam=36, cor=cor_de(c), peso=700, serif=True))
    return cabeca(s) + '<div style="flex:1"></div>' + desenho(w, h, partes, rots, s.get("alt", "Barras")) + '<div style="flex:1"></div>' + pe(s)

VISUAIS = {"icones": v_icones, "checklist": v_checklist, "pictograma": v_pictograma, "hero": v_hero,
           "fluxo": v_fluxo, "espectro": v_espectro, "ciclo": v_ciclo, "matriz": v_matriz,
           "linha_tempo": v_linha_tempo, "barras": v_barras}

def seta_mk(id_, cor):
    return (f'<marker id="{id_}" orient="auto" markerWidth="5" markerHeight="5" refX="0.8" refY="2" overflow="visible">'
            f'<path d="M-3.2 -1.7 L0.8 0 L-3.2 1.7" transform="translate(0 2)" fill="none" stroke="{cor}" '
            f'stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/></marker>')

MUDO_, GRADE_ = "#6B7A87", "#D9D4C8"

def s_painel(s, n, total, rod):
    """Painel colorido de altura inteira de um lado, com a figura; texto curto do outro."""
    lado = s.get("lado", "esq")
    c = s.get("cor", "petr")
    fundo_p = cor_de(c) if s.get("forte", True) else claro_de(c)
    cor_ic = PAPEL if s.get("forte", True) else cor_de(c)
    pw = 760
    left = 0 if lado == "esq" else 1920 - pw
    back = f'<div style="position:absolute; left:{left}px; top:0px; width:{pw}px; height:1080px; background:{fundo_p}"></div>'
    ic_t = s.get("ic_tam", 440)
    ic_top = 180 if s.get("grande") else (1080 - ic_t) / 2
    fig = (f'<svg aria-label="{s.get("alt", s["ic"].split(":")[1])}" width="{ic_t}" height="{ic_t}" viewBox="0 0 {ic_t} {ic_t}" '
           f'style="position:absolute; left:{left + (pw - ic_t) / 2:.0f}px; top:{ic_top:.0f}px; width:{ic_t}px; height:{ic_t}px">'
           + icone(s["ic"], 0, 0, ic_t, cor_ic) + '</svg>')
    grande = ""
    if s.get("grande"):
        grande = (f'<p style="position:absolute; left:{left + 60}px; top:{ic_top + ic_t + 40:.0f}px; width:{pw - 120}px; text-align:center; '
                  f'font-family:{SERIF}; font-size:{s.get("tam_grande", 96)}px; font-weight:700; line-height:1.1; color:{cor_ic}">{s["grande"]}</p>')
    itens = ""
    if s.get("itens"):
        ls = []
        for it in s["itens"]:
            ic_it = svg_icone(it["ic"], 56, cor_de(it.get("cor", c))) if it.get("ic") else ""
            ls.append(f'<div style="display:flex; gap:24px; align-items:center">{ic_it}'
                      f'<p style="flex:1; font-size:32px; line-height:1.35; color:{TINTA}">{it["t"]}</p></div>')
        itens = '<div style="display:flex; flex-direction:column; gap:28px">' + "".join(ls) + '</div>'
    texto = (f'<p style="font-size:34px; line-height:1.45; color:{APOIO2}">{s["texto"]}</p>' if s.get("texto") else "")
    pad = "128px 128px 160px 888px" if lado == "esq" else "128px 888px 160px 128px"
    fundo = PAPEL
    rod_x = 888 if lado == "esq" else 128
    simb = simbolo(lado == "dir") if lado == "dir" else simbolo(False)
    corpo = (back + fig + grande + simb + eyebrow(s.get("eyebrow", "")) + titulo(s["titulo"]) + '<div style="flex:1"></div>' + texto + itens
             + '<div style="flex:1"></div>' + pe(s)
             + f'<p style="position:absolute; left:{rod_x}px; bottom:64px; width:600px; font-size:24px; color:{RODAPE}">{rod}</p>'
             + (f'<p style="position:absolute; right:128px; bottom:64px; width:200px; text-align:right; font-size:24px; color:{RODAPE if lado == "esq" else "#E8EEF2"}">{n} / {total}</p>'))
    return (f'<section id="{s["id"]}" data-transition="fade" style="background:{fundo}; color:{TINTA}; font-family:{SANS}; '
            f'padding:{pad}; display:flex; flex-direction:column; gap:32px">\n{corpo}\n')

def s_versus(s, n, total, rod):
    """Tela dividida ao meio, cada metade com a sua cor, figura e três palavras."""
    metades, cores = [], []
    for i, lado in enumerate((s["esq"], s["dir"])):
        c = lado.get("cor", "petr" if i == 0 else "verm")
        cores.append(claro_de(c))
        lis = "".join(f'<p style="font-size:34px; line-height:1.35; color:{TINTA}; text-align:center">{x}</p>' for x in lado.get("itens", []))
        metades.append(f'<div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:24px">'
                       + svg_icone(lado["ic"], lado.get("tam", 230), cor_de(c))
                       + f'<h3 style="font-family:{SERIF}; font-size:60px; font-weight:700; line-height:1.15; color:{ESCURO_TXT.get(c, TINTA)}; text-align:center">{lado["t"]}</h3>'
                       + lis + '</div>')
    bg = f"linear-gradient(90deg, {cores[0]} 50%, {cores[1]} 50%)"
    corpo = (simbolo(False) + eyebrow(s.get("eyebrow", "")) + titulo(s["titulo"]) + '<div style="flex:1"></div>'
             + '<div style="display:flex; gap:256px">' + "".join(metades) + '</div><div style="flex:1"></div>' + pe(s) + rodape(rod, n, total))
    return secao(s["id"], bg, corpo, gap=28)

def s_pergunta(s, n, total, rod):
    c = s.get("fundo", "tinta")
    bg = cor_de(c) if c != "tinta" else TINTA
    marca = ""
    if s.get("ic"):
        t = 620
        marca = (f'<svg aria-label="" width="{t}" height="{t}" viewBox="0 0 {t} {t}" style="position:absolute; right:60px; bottom:40px; '
                 f'width:{t}px; height:{t}px; opacity:0.14">' + icone(s["ic"], 0, 0, t, PAPEL) + '</svg>')
    corpo = (marca + simbolo(True) + eyebrow(s.get("eyebrow", ""), True) + '<div style="flex:1"></div>'
             + f'<p style="font-family:{SERIF}; font-size:{s.get("tam", 80)}px; font-weight:700; line-height:1.2; color:{PAPEL}; width:1300px">{s["pergunta"]}</p>'
             + (f'<p style="font-size:32px; line-height:1.45; color:#DCE6EC; width:1150px">{s["apoio"]}</p>' if s.get("apoio") else "")
             + '<div style="flex:1"></div>' + rodape(rod, n, total, True))
    return secao(s["id"], bg, corpo, gap=32, cor=PAPEL)

TELAS = {"painel": s_painel, "versus": s_versus, "pergunta": s_pergunta}

def palavras_visiveis(html_s):
    corpo = re.sub(r"<aside>.*?</aside>", "", html_s, flags=re.S)
    corpo = re.sub(r"<svg.*?</svg>", "", corpo, flags=re.S)
    return len(re.sub(r"<[^>]+>", " ", corpo).split())

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
        if s["tipo"] in TELAS:
            html_s = TELAS[s["tipo"]](s, n, total, rod) + nota
        elif s["tipo"] in VISUAIS:
            bg = PAPEL if alterna % 2 == 0 else QUENTE
            alterna += 1
            corpo = simbolo(False) + VISUAIS[s["tipo"]](s) + rodape(rod, n, total)
            html_s = secao(sid, bg, corpo, gap=s.get("gap", 32)) + nota
        elif s["tipo"] == "frase":
            bg = CORES.get(s.get("fundo"), PETR)
            marca = ""
            if s.get("ic"):
                t = s.get("ic_tam", 560)
                marca = (f'<svg aria-label="" width="{t}" height="{t}" viewBox="0 0 {t} {t}" style="position:absolute; right:80px; bottom:60px; '
                         f'width:{t}px; height:{t}px; opacity:0.13">' + icone(s["ic"], 0, 0, t, PAPEL) + '</svg>')
            corpo = (marca + simbolo(True) + eyebrow(s.get("eyebrow", ""), True) +
                     f'<div style="flex:1"></div>'
                     f'<p style="font-family:{SERIF}; font-size:{s.get("tam", 64)}px; font-weight:700; line-height:1.25; color:{PAPEL}; width:1560px">{s["frase"]}</p>'
                     + (f'<p style="font-size:30px; line-height:1.4; color:#DCE6EC; width:1500px">{s["apoio"]}</p>' if s.get("apoio") else "")
                     + '<div style="flex:1"></div>' + rodape(rod, n, total, True))
            html_s = secao(sid, bg, corpo, gap=32, cor=PAPEL) + nota
        elif s["tipo"] == "fecho":
            regras = "".join(f'<div style="display:flex; gap:22px; align-items:center">' + svg_icone("t:check", 44, tema["eyebrow"])
                             + f'<p style="flex:1; font-size:32px; line-height:1.35; color:{PAPEL}">{r}</p></div>' for r in s["regras"])
            cartoes = ('<div style="display:flex; gap:24px">' + "".join(card(c, None, escuro=True, tema=tema) for c in s["cards"]) + '</div>') if s.get("cards") else ""
            corpo = (simbolo(True) + eyebrow(s.get("eyebrow", "O que fica"), True, tema["eyebrow"]) + titulo(s["titulo"], True) +
                     f'<div style="display:flex; flex-direction:column; gap:14px">{regras}</div>' + '<div style="flex:1"></div>' + cartoes
                     + (f'<p style="font-size:26px; line-height:1.45; color:{tema["apoio"]}">{s["quem"]}</p>' if s.get("quem") else "")
                     + f'<p style="position:absolute; right:128px; bottom:64px; width:200px; text-align:right; font-size:24px; color:#9FB0BD">{n} / {total}</p>')
            html_s = secao(sid, tema["fundo"], corpo, gap=30, cor=PAPEL) + nota
        else:
            bg = PAPEL if alterna % 2 == 0 else QUENTE
            alterna += 1
            corpo = (simbolo(False) + eyebrow(s.get("eyebrow", "")) + titulo(s["titulo"]) + miolo(s, bg) + rodape(rod, n, total))
            html_s = secao(sid, bg, corpo, gap=s.get("gap", 34)) + nota
        pv = palavras_visiveis(html_s) - len(rod.split()) - 2
        if pv > (70 if s["tipo"] == "fecho" else LIMITE_PALAVRAS):
            print(f"  aviso: {sid} tem {pv} palavras na tela (limite {LIMITE_PALAVRAS})")
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
