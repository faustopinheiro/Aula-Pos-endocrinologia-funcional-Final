#!/usr/bin/env python3
"""Cenas do Reels classudo da profissão ("aula magna"), feitas para o Reels "PRP funciona?" no auditório.

Tudo no peito, abaixo do queixo (selfie com o rosto grande): frases em Playfair com a palavra principal em dourado
itálico, rótulo em caixa alta espaçada com fios dourados, pílula de seção no alto, passo a passo com ícones de traço
dourado que se desenham, listas com selo (✓ ✕ ≈), documento oficial com itens em grade, placa de nome no alto e o
fecho em tipografia com a assinatura. Sem medidor (ele não cabe no tom sério).

  python3 cenas_reels_classudo.py PROJETO EDIT

Para outro vídeo, troque a lista de cenas em main(): cada cena tem de/ate em segundos do cut.mp4 e cada peça o
tempo e a palavra em que entra (o tempo acerta pela fala do corte, com folga de 0,45 s). Lê o face_layout.json do
EDIT e o zoom de cada bloco do projeto.json para pôr o conteúdo abaixo do queixo. Grava compositions/cenas/<id>.html
e cenas_proprias.json (copie para "cenas_proprias" do projeto.json). Precisa de assets/fontes/PlayfairDisplay.ttf e
PlayfairDisplay-Italic.ttf no projeto (Google Fonts, licença OFL).
"""
import json
import os
import sys
from html import escape

W, H = 1080, 1920
# o corte mudou depois dos tempos medidos? CORTE = onde mudou, DELTA = quanto encurtou (s); os tempos passam por sh().
# No Reels do PRP o corte encurtou 0,167 s depois de 39,9 s.
CORTE, DELTA = 39.9, 0.167


def sh(t):
    return round(t - DELTA, 3) if t > CORTE else t
OURO = '#e2c27e'

ICONES = {
    # traço dourado, viewBox 0 0 100 100
    'coleta': '<path d="M50 10 C50 10 24 42 24 60 A26 26 0 0 0 76 60 C76 42 50 10 50 10 Z"/>'
              '<path d="M38 64 A12 12 0 0 0 50 74"/>',
    'centrifuga': '<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="6"/>'
                  '<path d="M50 44 L50 20"/><path d="M55 53 L76 65"/><path d="M45 53 L24 65"/>'
                  '<circle cx="50" cy="18" r="5"/><circle cx="78" cy="66" r="5"/><circle cx="22" cy="66" r="5"/>',
    'plaquetas': '<ellipse cx="34" cy="38" rx="12" ry="8"/><ellipse cx="62" cy="32" rx="11" ry="7"/>'
                 '<ellipse cx="54" cy="58" rx="13" ry="8"/><ellipse cx="28" cy="66" rx="9" ry="6"/>'
                 '<ellipse cx="74" cy="64" rx="9" ry="6"/><ellipse cx="46" cy="80" rx="8" ry="5"/>',
    'seringa': '<path d="M42 8 L58 8"/><path d="M50 8 L50 22"/><rect x="40" y="22" width="20" height="44" rx="3"/>'
               '<path d="M40 34 L48 34"/><path d="M40 44 L48 44"/><path d="M40 54 L48 54"/>'
               '<path d="M50 66 L50 90"/>',
    'joelho': '<path d="M38 6 L38 34 Q38 46 50 46 Q62 46 62 34 L62 6"/>'
              '<path d="M36 94 L38 62 Q50 55 62 62 L64 94"/><path d="M40 53 Q50 50 60 53"/>',
    'coluna': '<rect x="33" y="6" width="34" height="16" rx="6"/><rect x="33" y="30" width="34" height="16" rx="6"/>'
              '<rect x="33" y="54" width="34" height="16" rx="6"/><rect x="33" y="78" width="34" height="16" rx="6"/>'
              '<path d="M40 26 L60 26"/><path d="M40 50 L60 50"/><path d="M40 74 L60 74"/>',
    'cotovelo': '<path d="M12 36 L44 66 L86 44"/><circle cx="44" cy="66" r="7"/>'
                '<circle cx="78" cy="20" r="11"/><path d="M69 15 Q78 22 87 15"/><path d="M69 26 Q78 19 87 26"/>',
    'menisco': '<path d="M46 30 A20 20 0 1 0 46 70"/><path d="M54 30 A20 20 0 1 1 54 70"/>'
               '<path d="M46 30 Q40 50 46 70"/><path d="M54 30 Q60 50 54 70"/>',
}

CSS = '''@font-face{font-family:Montserrat;src:url("assets/fontes/Montserrat.ttf") format("truetype");font-weight:100 900;font-display:block}
@font-face{font-family:Playfair;src:url("assets/fontes/PlayfairDisplay.ttf") format("truetype");font-weight:400 900;font-display:block}
@font-face{font-family:PlayfairI;src:url("assets/fontes/PlayfairDisplay-Italic.ttf") format("truetype");font-weight:400 900;font-display:block}
#root{position:absolute;inset:0;overflow:hidden;font-family:Montserrat}
.cx-band{position:absolute;left:0;right:0;bottom:0;opacity:0;
  background:linear-gradient(to bottom,rgba(8,6,4,0) 0%,rgba(8,6,4,.5) 32%,rgba(8,6,4,.8) 100%)}
.cx-lab{position:absolute;left:60px;right:60px;text-align:center;font-weight:600;font-size:24px;line-height:30px;letter-spacing:.3em;
  color:#e2c27e;opacity:0;white-space:nowrap}
.cx-lab:before,.cx-lab:after{content:"";display:inline-block;width:46px;height:1.5px;background:rgba(226,194,126,.75);vertical-align:middle;margin:0 18px 4px}
.cx-l{position:absolute;left:30px;right:30px;text-align:center;font-family:Playfair;font-weight:500;color:#fbfaf7;white-space:nowrap;
  text-shadow:0 2px 18px rgba(0,0,0,.45)}
.cx-l span{display:inline-block;opacity:0}
.cx-l .o{font-family:PlayfairI;font-weight:500;color:#e2c27e}
.cx-pw{position:absolute;left:0;width:1080px;display:flex;justify-content:center}
.cx-pill{padding:14px 40px 15px;border-radius:40px;background:rgba(14,12,9,.7);box-shadow:0 0 0 1.5px rgba(226,194,126,.7);
  font-weight:600;font-size:23px;letter-spacing:.3em;color:#e2c27e;white-space:nowrap;opacity:0}
.cx-np{text-align:center;opacity:0}
.cx-np .n{font-family:Playfair;font-weight:500;font-size:58px;line-height:66px;color:#fbfaf7;text-shadow:0 2px 16px rgba(0,0,0,.5)}
.cx-np .r{width:300px;height:1.5px;margin:10px auto 12px;background:#e2c27e}
.cx-np .p{font-weight:600;font-size:22px;letter-spacing:.42em;color:#e2c27e;margin-left:.42em}
.cx-t{position:absolute;width:240px;text-align:center;opacity:0}
.cx-disc{position:relative;width:150px;height:150px;margin:0 auto;border-radius:50%;background:rgba(14,12,9,.72);
  box-shadow:0 0 0 1.5px rgba(226,194,126,.75),0 14px 30px rgba(0,0,0,.4)}
.cx-ic{position:absolute;left:33px;top:33px;width:84px;height:84px}
.cx-ic svg{width:84px;height:84px;fill:none;stroke:#e2c27e;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.cx-tl{margin-top:16px;font-weight:600;font-size:23px;line-height:29px;letter-spacing:.12em;text-transform:uppercase;color:#fbfaf7}
.cx-n{position:absolute;top:-6px;left:-6px;width:40px;height:40px;border-radius:50%;background:#e2c27e;color:#1a1307;
  font-family:Playfair;font-weight:700;font-size:24px;line-height:40px;text-align:center}
.cx-con{position:absolute;height:1.5px;background:rgba(226,194,126,.8);transform-origin:0 50%;opacity:0}
.cx-pan{position:absolute;left:110px;width:860px;padding:26px 44px 30px;border-radius:30px;background:rgba(14,12,9,.74);
  box-shadow:0 0 0 1.5px rgba(226,194,126,.7),0 20px 44px rgba(0,0,0,.42);opacity:0;box-sizing:border-box}
.cx-pan .h{text-align:center;font-weight:600;font-size:23px;letter-spacing:.3em;color:#e2c27e;margin-bottom:14px}
.cx-row{display:flex;align-items:center;height:76px;opacity:0}
.cx-b{flex:0 0 auto;width:48px;height:48px;border-radius:50%;margin-right:24px;display:flex;align-items:center;justify-content:center;
  font-weight:900;font-size:27px}
.cx-ok{background:#58c98d;color:#06210f}
.cx-no{background:#e5484d;color:#ffffff}
.cx-q{background:#e2c27e;color:#1a1307}
.cx-rt{font-family:Playfair;font-weight:500;font-size:46px;color:#fbfaf7;white-space:nowrap}
.cx-doc .t{text-align:center;font-family:Playfair;font-weight:500;font-size:50px;line-height:60px;color:#fbfaf7;margin-bottom:20px;opacity:0}
.cx-doc .t .o{font-family:PlayfairI;color:#e2c27e}
.cx-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px 20px}
.cx-it{display:flex;align-items:center;height:84px;padding:0 18px;border-radius:20px;background:rgba(226,194,126,.07);
  box-shadow:inset 0 0 0 1px rgba(226,194,126,.35);opacity:0}
.cx-it svg{flex:0 0 auto;width:56px;height:56px;margin-right:16px;fill:none;stroke:#e2c27e;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}
.cx-it span{font-weight:600;font-size:25px;line-height:30px;color:#fbfaf7}'''


def svg(nome):
    return f'<svg viewBox="0 0 100 100">{ICONES[nome]}</svg>'


class Cena:
    def __init__(self, sid, de, ate, topo=None, banda=True):
        de, ate = sh(de), sh(ate)
        self.sid, self.de, self.ate = sid, de, ate
        self.dur = round(ate - de, 3)
        self.html, self.acts = [], []
        self.topo = topo          # topo do conteúdo do peito (px); None = calculado pelo rosto
        self.banda = banda
        self.n = 0

    def r(self, t):
        return round(t - self.de, 3)

    def novo_id(self, p):
        self.n += 1
        return f'{self.sid}-{p}{self.n}'

    def act(self, sel, kind, t, palavra=None, **kw):
        self.acts.append(dict(sel=sel, kind=kind, t=self.r(sh(t)), w=palavra, **kw))

    # ---- peças
    def pilula(self, texto, t, palavra=None, y=112):
        i = self.novo_id('p')
        self.html.append(f'<div class="cx-pw" style="top:{y}px"><div class="cx-pill" id="{i}">{escape(texto)}</div></div>')
        self.act('#' + i, 'down', t, palavra)

    def rotulo(self, texto, t, y, palavra=None):
        i = self.novo_id('r')
        self.html.append(f'<div class="cx-lab" id="{i}" style="top:{y}px">{escape(texto)}</div>')
        self.act('#' + i, 'in', t, palavra)
        return i

    def linha(self, partes, y, tam=80):
        """partes: (texto, dourado, t, palavra). Cada parte entra na sua palavra."""
        i = self.novo_id('l')
        spans = []
        for k, (txt, ouro, t, pal) in enumerate(partes):
            sid = f'{i}s{k}'
            spans.append(f'<span id="{sid}" class="{"o" if ouro else ""}">{escape(txt)}</span>')
            self.act('#' + sid, 'word', t, pal)
        sep = '<span style="opacity:1;width:.28em"></span>'
        self.html.append(f'<div class="cx-l" id="{i}" style="top:{y}px;font-size:{tam}px;line-height:{round(tam * 1.18)}px">'
                         + sep.join(spans) + '</div>')
        return i

    def placa_nome(self, t, y=96):
        i = self.novo_id('n')
        self.html.append(f'<div class="cx-pw" style="top:{y}px"><div class="cx-np" id="{i}"><div class="n">Dr. Fausto Farias</div>'
                         '<div class="r"></div><div class="p">MEDICINA DO ESPORTE</div></div></div>')
        self.act('#' + i, 'down', t)

    def passos(self, itens, y):
        """itens: (icone, rotulo com \\n, t, palavra)"""
        n = len(itens)
        larg, passo = 240, (W - 2 * 30) / n
        xs = [30 + passo * k + (passo - larg) / 2 for k in range(n)]
        for k, (ic, rot, t, pal) in enumerate(itens):
            i = self.novo_id('t')
            rot_html = '<br>'.join(escape(p) for p in rot.split('\n'))
            self.html.append(f'<div class="cx-t" id="{i}" style="left:{round(xs[k])}px;top:{y}px"><div class="cx-disc">'
                             f'<div class="cx-ic" id="{i}i">{svg(ic)}</div><div class="cx-n">{k + 1}</div></div>'
                             f'<div class="cx-tl">{rot_html}</div></div>')
            self.act('#' + i, 'in', t, pal)
            self.act(f'#{i}i', 'draw', t + 0.12, pal)
            if k:
                c = self.novo_id('c')
                x0, x1 = xs[k - 1] + larg / 2 + 82, xs[k] + larg / 2 - 82
                self.html.append(f'<div class="cx-con" id="{c}" style="left:{round(x0)}px;width:{round(x1 - x0)}px;top:{y + 75}px"></div>')
                self.act('#' + c, 'line', t - 0.05, pal)

    def lista(self, titulo, t_tit, itens, y, pal_tit=None):
        """itens: (selo ok/no/q, texto, t, palavra)"""
        i = self.novo_id('pan')
        linhas = []
        for k, (selo, txt, t, pal) in enumerate(itens):
            ch, cl = {'ok': ('✓', 'cx-ok'), 'no': ('✕', 'cx-no'), 'q': ('≈', 'cx-q')}[selo]
            rid = f'{i}r{k}'
            linhas.append(f'<div class="cx-row" id="{rid}"><div class="cx-b {cl}" id="{rid}b">{ch}</div>'
                          f'<div class="cx-rt">{escape(txt)}</div></div>')
            self.act('#' + rid, 'row', t, pal)
            self.act(f'#{rid}b', 'badge', t + 0.18, pal)
        self.html.append(f'<div class="cx-pan" id="{i}" style="top:{y}px"><div class="h">{escape(titulo)}</div>{"".join(linhas)}</div>')
        self.act('#' + i, 'in', t_tit, pal_tit)

    def documento(self, cab, t_cab, titulo, t_tit, itens, y, pal_cab=None, pal_tit=None):
        """titulo: partes (texto, dourado, t, palavra); itens: (icone, texto, t, palavra)"""
        i = self.novo_id('doc')
        tit = []
        for k, (txt, ouro, t, pal) in enumerate(titulo):
            sid = f'{i}w{k}'
            tit.append(f'<span id="{sid}" class="{"o" if ouro else ""}" style="display:inline-block;opacity:0">{escape(txt)}</span>')
            self.act('#' + sid, 'word', t, pal)
        grade = []
        for k, (ic, txt, t, pal) in enumerate(itens):
            gid = f'{i}g{k}'
            grade.append(f'<div class="cx-it" id="{gid}">{svg(ic)}<span>{escape(txt)}</span></div>')
            self.act('#' + gid, 'row', t, pal)
        self.html.append(f'<div class="cx-pan cx-doc" id="{i}" style="top:{y}px"><div class="h">{escape(cab)}</div>'
                         f'<div class="t" id="{i}t">{"&nbsp;".join(tit)}</div><div class="cx-grid">{"".join(grade)}</div></div>')
        self.act('#' + i, 'in', t_cab, pal_cab)
        self.act(f'#{i}t', 'show', titulo[0][2], titulo[0][3])

    # ---- arquivo
    def gravar(self, pasta):
        band = (f'<div class="cx-band" id="{self.sid}-band" style="height:{H - (self.topo or 1300) + 260}px"></div>'
                if self.banda else '')
        corpo = '\n  '.join([band] + self.html) if band else '\n  '.join(self.html)
        js = f'''(function () {{
  const C = (window.__cenas || {{}})["{self.sid}"] || {{ palavras: [], duracao: {self.dur} }};
  const DUR = C.duracao, fim = DUR - 0.3;
  const sem = (s) => s.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]/g, "");
  // o tempo da palavra na fala, perto do tempo medido; sem a palavra, o tempo medido
  const em = (t, w) => {{
    if (!w) return t;
    let m = null;
    (C.palavras || []).forEach((p) => {{
      if (sem(p.texto).startsWith(sem(w)) && Math.abs(p.t - t) < 0.45 && (m === null || Math.abs(p.t - t) < Math.abs(m - t))) m = p.t;
    }});
    return m === null ? t : m;
  }};
  const A = {json.dumps(self.acts, ensure_ascii=False)};
  const tl = gsap.timeline({{ paused: true }});
  {"tl.fromTo('#" + self.sid + "-band', { opacity: 0 }, { opacity: 1, duration: 0.5, ease: 'power1.out' }, 0.02);" if self.banda else ""}
  A.forEach((a) => {{
    const t = Math.max(0.02, Math.min(fim - 0.25, em(a.t, a.w) - 0.05));
    if (a.kind === "in") tl.fromTo(a.sel, {{ opacity: 0, y: 26 }}, {{ opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }}, t);
    else if (a.kind === "down") tl.fromTo(a.sel, {{ opacity: 0, y: -22 }}, {{ opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }}, t);
    else if (a.kind === "word") tl.fromTo(a.sel, {{ opacity: 0, y: 22 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, t);
    else if (a.kind === "show") tl.fromTo(a.sel, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.01 }}, t);
    else if (a.kind === "row") tl.fromTo(a.sel, {{ opacity: 0, x: -24 }}, {{ opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }}, t);
    else if (a.kind === "badge") tl.fromTo(a.sel, {{ opacity: 0, scale: 0.2 }}, {{ opacity: 1, scale: 1, duration: 0.32, ease: "back.out(3)" }}, t);
    else if (a.kind === "draw") tl.fromTo(a.sel, {{ opacity: 1, clipPath: "inset(100% 0% 0% 0%)" }}, {{ opacity: 1, clipPath: "inset(0% 0% 0% 0%)", duration: 0.7, ease: "power2.out" }}, t);
    else if (a.kind === "line") tl.fromTo(a.sel, {{ opacity: 1, scaleX: 0 }}, {{ opacity: 1, scaleX: 1, duration: 0.45, ease: "power2.inOut" }}, t);
    else if (a.kind === "out") tl.to(a.sel, {{ opacity: 0, y: -14, duration: 0.35, ease: "power2.in" }}, t);
  }});
  tl.to("#root > *", {{ opacity: 0, duration: 0.3, ease: "power2.in" }}, fim);
  window.__timelines["{self.sid}"] = tl;
}})();'''
        doc = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8"/><title>{self.sid} · Reels PRP classudo</title></head>
<body>
<!-- Gerada por scripts/cenas_prp_classudo.py: troque lá e gere de novo. -->
<template id="{self.sid}-template">
<style>
{CSS}
</style>
<div id="root" data-composition-id="{self.sid}" data-width="1080" data-height="1920" data-duration="{self.dur}">
  {corpo}
</div>
<script>
{js}
</script>
</template>
</body>
</html>
'''
        with open(os.path.join(pasta, self.sid + '.html'), 'w', encoding='utf-8') as f:
            f.write(doc)


def queixo(layout, blocos, de, ate):
    """o y mais baixo do queixo na tela entre de e ate, com o zoom do bloco (conta do build.py: rosto a 42% da
    altura, sem mostrar borda)"""
    pior = 0
    for s in layout['segments']:
        if s['end'] <= de or s['start'] >= ate:
            continue
        f = s['face']
        z = next((b['zoom'] for b in blocos if b['de'] <= max(de, s['start']) < (b.get('ate') or 1e9)), 1.08)
        cy = (f['y0'] + f['y1']) / 2 * H
        y = min(0.0, max(H - z * H, 0.42 * H - z * cy))
        pior = max(pior, y + z * f['y1'] * H)
    return pior


def main():
    proj, edit = sys.argv[1:3]
    layout = json.load(open(os.path.join(edit, 'face_layout.json')))
    blocos = json.load(open(os.path.join(proj, 'projeto.json')))['blocos']
    pasta = os.path.join(proj, 'compositions', 'cenas')
    os.makedirs(pasta, exist_ok=True)

    def topo(de, ate, minimo=1330, maximo=1480):
        return int(min(maximo, max(minimo, queixo(layout, blocos, sh(de), sh(ate)) + 60)))

    cenas = []

    c = Cena('c_gancho', 0.0, 2.98); y = topo(0, 2.98); c.topo = y
    c.rotulo('A PERGUNTA QUE EU MAIS RECEBI', 0.32, y, 'pergunta')
    c.linha([('Funciona?', True, 2.30, 'funciona')], y + 50, tam=124)
    cenas.append(c)

    c = Cena('c_sim', 3.0, 4.36); y = topo(3.0, 4.36); c.topo = y
    c.linha([('Sim,', False, 3.03, 'sim'), ('pode funcionar', True, 3.49, 'pode')], y + 20, tam=92)
    cenas.append(c)

    c = Cena('c_indicacao', 4.39, 8.28); y = topo(4.39, 8.28); c.topo = y
    c.rotulo('O RESULTADO COMEÇA ANTES DA APLICAÇÃO', 5.27, y, 'comeca')
    c.linha([('com a', False, 7.34, 'com'), ('indicação correta', True, 7.65, 'indicacao')], y + 50, tam=78)
    cenas.append(c)

    c = Cena('c_nome', 3.0, 7.9, banda=False)
    c.placa_nome(3.1)
    cenas.append(c)

    c = Cena('c_oque', 8.30, 16.37); y = topo(8.30, 16.37); c.topo = y
    c.pilula('O QUE É PRP', 8.44, 'prp')
    c.linha([('Plasma rico em', False, 9.16, 'plasma'), ('plaquetas', True, 9.89, 'plaquetas')], y + 10, tam=70)
    c.passos([('coleta', 'Coleta\no sangue', 11.14, 'coleta'), ('centrifuga', 'Centrifuga', 12.34, 'centrifuga'),
              ('plaquetas', 'Concentra as\nplaquetas', 12.97, 'concentra'), ('seringa', 'Devolve\nao tecido', 14.39, 'devolve')],
             y + 120)
    cenas.append(c)

    c = Cena('c_acao', 16.40, 21.55); y = topo(16.40, 21.55); c.topo = y
    c.rotulo('AS PLAQUETAS LIBERAM SUBSTÂNCIAS', 17.20, y, 'liberar')
    c.linha([('Regulação da', False, 18.93, 'regulacao'), ('inflamação', True, 19.52, 'inflamacao')], y + 50, tam=70)
    c.linha([('e', False, 20.16, 'e'), ('reparo dos tecidos', True, 20.76, 'reparo')], y + 140, tam=70)
    cenas.append(c)

    c = Cena('c_joelho', 21.58, 26.30); y = topo(21.58, 26.30); c.topo = y
    c.pilula('A CONDIÇÃO MAIS ESTUDADA', 21.95, 'condicoes')
    c.linha([('Artrose de', False, 24.05, 'artrose'), ('joelho', True, 24.45, 'joelho')], y + 10, tam=88)
    c.rotulo('LEVE E MODERADA', 25.41, y + 130, 'leve')
    cenas.append(c)

    c = Cena('c_estudos', 26.32, 31.22); y = topo(26.32, 31.22); c.topo = y
    c.lista('OS ESTUDOS MOSTRAM', 26.73, [('ok', 'Melhora da dor', 28.50, 'dor'),
                                          ('ok', 'Melhora dos movimentos', 29.32, 'movimentos'),
                                          ('q', 'Resultados variam muito', 30.32, 'variam')], y, 'estudos')
    cenas.append(c)

    c = Cena('c_promessa', 31.24, 35.62); y = topo(31.24, 35.62); c.topo = y
    c.lista('NINGUÉM DEVE PROMETER', 31.73, [('no', 'Cartilagem nova', 32.74, 'cartilagem'),
                                             ('no', 'Resultado garantido', 34.76, 'resultado')], y, 'ninguem')
    cenas.append(c)

    c = Cena('c_cfm', 35.66, 44.70); y = topo(35.66, 44.70, maximo=1360); c.topo = y
    c.documento('CFM · JULHO DE 2026', 35.69,
                [('Liberado como tratamento', False, 38.35, 'liberou'), ('complementar', True, 39.40, 'complementar')],
                38.35,
                [('joelho', 'Artrose de joelho', 40.33, 'artrose'), ('coluna', 'Discopatia lombar', 41.30, 'discopatia'),
                 ('cotovelo', 'Cotovelo de tenista', 42.21, 'cotovelo'), ('menisco', 'Reparo de menisco', 43.61, 'reparo')],
                y, pal_cab='julho')
    cenas.append(c)

    c = Cena('c_atencao', 44.72, 48.34); y = topo(44.72, 48.34); c.topo = y
    c.rotulo('PRESTE ATENÇÃO NA PALAVRA', 45.03, y + 40, 'preste')
    c.linha([('complementar', True, 47.54, 'complementar')], y + 92, tam=120)
    cenas.append(c)

    c = Cena('c_naosubst', 48.36, 54.92); y = topo(48.36, 54.92); c.topo = y
    c.lista('O PRP NÃO SUBSTITUI', 49.23, [('no', 'Fortalecimento', 50.45, 'fortalecimento'),
                                           ('no', 'Reabilitação', 52.69, 'reabilitacao'),
                                           ('no', 'Acompanhamento', 54.50, 'acompanhamento')], y, 'nao')
    cenas.append(c)

    c = Cena('c_competir', 54.95, 59.90); y = topo(54.95, 59.90); c.topo = y
    c.rotulo('PARA QUEM PRATICA ESPORTE', 55.11, y, 'quem')
    c.linha([('Sentir menos dor', False, 56.11, 'sentir')], y + 46, tam=70)
    c.linha([('não significa estar', False, 57.00, 'nao')], y + 132, tam=70)
    c.linha([('pronto para competir', True, 58.57, 'pronto')], y + 218, tam=76)
    cenas.append(c)

    c = Cena('c_antes', 59.92, 66.45); y = topo(59.92, 66.45); c.topo = y
    c.lista('ANTES DE INDICAR', 60.51, [('ok', 'A origem da dor', 62.74, 'origem'),
                                        ('ok', 'O que já foi tentado', 63.52, 'que'),
                                        ('ok', 'Qual benefício buscar', 64.77, 'qual')], y, 'antes')
    cenas.append(c)

    c = Cena('c_avaliacao', 66.47, 71.10); y = topo(66.47, 71.10); c.topo = y
    c.rotulo('SE A DOR ESTÁ LIMITANDO SEU TREINO', 67.19, y, 'limitando')
    c.linha([('Procure uma', False, 70.17, 'procurar'), ('avaliação', True, 70.58, 'avaliacao')], y + 50, tam=84)
    cenas.append(c)

    c = Cena('c_fim', 71.12, 77.67); y = topo(71.12, 77.67); c.topo = y
    c.rotulo('A DECISÃO MAIS IMPORTANTE', 71.39, y, 'decisao')
    l1 = c.linha([('vem', False, 73.00, 'vem'), ('antes do procedimento', True, 73.36, 'antes')], y + 50, tam=74)
    c.act('#' + l1, 'out', 74.50)
    c.linha([('escolher o tratamento', False, 74.70, 'escolher')], y + 50, tam=70)
    c.linha([('adequado pra você', True, 76.77, 'adequado')], y + 138, tam=88)
    c.rotulo('DR. FAUSTO FARIAS · MEDICINA DO ESPORTE', 76.95, 1800)
    cenas.append(c)

    for c in cenas:
        c.gravar(pasta)
    linhas = []
    for c in cenas:
        esconde = c.sid not in ('c_nome',)
        linhas.append({'arquivo': f'compositions/cenas/{c.sid}.html', 'de': c.de, 'ate': c.ate, 'nome': c.sid,
                       **({'esconde_legenda': True} if esconde else {})})
        print(f'{c.sid:12s} {c.de:6.2f}-{c.ate:6.2f} topo {c.topo}')
    json.dump(linhas, open(os.path.join(proj, 'cenas_proprias.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
