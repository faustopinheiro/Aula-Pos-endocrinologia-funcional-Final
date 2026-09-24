"""Funções de desenho para os decks: gráficos e esquemas em SVG com rótulos em <p>.

Tudo devolve (svg, rotulos): o svg ocupa o host inteiro (mesmo tamanho do viewBox)
e os rótulos são posicionados nas mesmas coordenadas. Texto nunca vai dentro do svg.
Cores de dado validadas (dataviz, modo claro, todas as checagens PASS):
FOSF #A8322A · GLIC #B07A1C · OXID #008A7E · AZUL #3A6EA5.
"""
import math

FOSF, GLIC, OXID, AZUL = "#A8322A", "#B07A1C", "#008A7E", "#3A6EA5"
TINTA, APOIO2, MUDO, GRADE, PAUSA = "#12202E", "#3A4A57", "#6B7A87", "#D9D4C8", "#C3CBD1"

def rot(x, y, t, w=300, tam=26, cor=APOIO2, peso=400, alinha="left", lh=1.25, serif=False):
    r = {"x": round(x), "y": round(y), "w": round(w), "t": t, "tam": tam, "cor": cor, "peso": peso, "alinha": alinha, "lh": lh}
    if serif:
        r["serif"] = True
    return r

def svg_abre(w, h, alt):
    return f'<svg aria-label="{alt}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'

def seta_marker(id_, cor):
    return (f'<marker id="{id_}" orient="auto" markerWidth="5" markerHeight="5" refX="0.8" refY="2" overflow="visible">'
            f'<path d="M-3.2 -1.7 L0.8 0 L-3.2 1.7" transform="translate(0 2)" fill="none" stroke="{cor}" '
            f'stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/></marker>')

def linhas(w, h, alt, series, xmin, xmax, ymin, ymax, xticks, yticks, xlog=False,
           margem=(110, 30, 70, 30), yfmt=lambda v: f"{v:g}%", xlabel=None, destaques=()):
    """Gráfico de linhas. series = [{nome, cor, pts:[(x,y)], rotulo_em: índice do ponto para o nome}].
    margem = (esquerda, topo, baixo, direita)."""
    ml, mt, mb, mr = margem
    pw, ph = w - ml - mr, h - mt - mb
    fx = (lambda v: ml + (math.log10(v) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * pw) if xlog \
        else (lambda v: ml + (v - xmin) / (xmax - xmin) * pw)
    fy = lambda v: mt + ph - (v - ymin) / (ymax - ymin) * ph
    partes, rots = [svg_abre(w, h, alt)], []
    for v in yticks:
        y = fy(v)
        partes.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{w-mr}" y2="{y:.1f}" stroke="{GRADE}" stroke-width="2"/>')
        rots.append(rot(0, y - 17, yfmt(v), w=ml - 16, tam=24, cor=MUDO, alinha="right"))
    for v, txt in xticks:
        x = fx(v)
        partes.append(f'<line x1="{x:.1f}" y1="{mt+ph}" x2="{x:.1f}" y2="{mt+ph+10}" stroke="{MUDO}" stroke-width="2"/>')
        rots.append(rot(x - 80, mt + ph + 16, txt, w=160, tam=24, cor=MUDO, alinha="center"))
    for d in destaques:
        x = fx(d["x"])
        partes.append(f'<line x1="{x:.1f}" y1="{mt}" x2="{x:.1f}" y2="{mt+ph}" stroke="{TINTA}" stroke-width="2" stroke-dasharray="8 8"/>')
        if d.get("t"):
            rots.append(rot(x + 12, mt + 4, d["t"], w=d.get("w", 260), tam=d.get("tam", 28), cor=TINTA, peso=600))
    partes.append(f'<line x1="{ml}" y1="{mt+ph}" x2="{w-mr}" y2="{mt+ph}" stroke="{MUDO}" stroke-width="2"/>')
    for s in series:
        pts = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in s["pts"])
        partes.append(f'<polyline points="{pts}" fill="none" stroke="{s["cor"]}" stroke-width="{s.get("esp", 6)}" '
                      f'stroke-linecap="round" stroke-linejoin="round"/>')
        for x, y in s.get("marcas", []):
            partes.append(f'<circle cx="{fx(x):.1f}" cy="{fy(y):.1f}" r="11" fill="{s["cor"]}" stroke="#F7F6F2" stroke-width="3"/>')
        if s.get("nome"):
            lx, ly = s["rotulo_xy"]
            rots.append(rot(fx(lx) + s.get("dx", 14), fy(ly) + s.get("dy", -20), s["nome"], w=s.get("rw", 300),
                            tam=28, cor=TINTA, peso=600))
            partes.append(f'<circle cx="{fx(lx) + s.get("dx", 14) - 14:.1f}" cy="{fy(ly) + s.get("dy", -20) + 18:.1f}" r="0"/>')
    if xlabel:
        rots.append(rot(ml, h - 34, xlabel, w=pw, tam=24, cor=MUDO, alinha="right"))
    partes.append("</svg>")
    return "".join(partes), rots

def barras_empilhadas(w, alt, linhas_, cores, larg_rotulo=420, alt_barra=64, passo=92, topo=10, min_txt=90):
    """Barras horizontais 100% empilhadas. linhas_ = [(rotulo, [v1, v2, ...])], valores somando 100."""
    h = topo + passo * len(linhas_)
    x0, bw = larg_rotulo + 24, w - larg_rotulo - 24
    partes, rots = [svg_abre(w, h, alt)], []
    for i, (nome, vals) in enumerate(linhas_):
        y = topo + i * passo
        rots.append(rot(0, y + alt_barra / 2 - 18, nome, w=larg_rotulo, tam=28, cor=TINTA, peso=500, alinha="right"))
        x = x0
        for j, v in enumerate(vals):
            ww = bw * v / 100
            gap = 2 if j < len(vals) - 1 else 0
            partes.append(f'<rect x="{x:.1f}" y="{y}" width="{max(ww-gap,0):.1f}" height="{alt_barra}" rx="4" fill="{cores[j]}"/>')
            if ww >= min_txt:
                rots.append(rot(x, y + alt_barra / 2 - 18, f"{v:g}%", w=ww, tam=28, cor="#F7F6F2", peso=600, alinha="center"))
            x += ww
    partes.append("</svg>")
    return "".join(partes), rots, h
