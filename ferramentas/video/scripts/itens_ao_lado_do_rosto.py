#!/usr/bin/env python3
"""Itens que aparecem ao lado do rosto quando a fala cita cada um (padrão aprovado no Shorts do Legacy, 9:16, tela
cheia, sem moldura). Cada item entra num cartão escuro com fio dourado (figura redonda, nome em Playfair e uma frase
curta da fala), ganha um selo (✓ sentiu ou tem, ✕ não, ? não sabe, ≈ misturado) na palavra do veredito e some. Um
título em pílula no alto ("Pirâmide olfativa · Notas de topo") fica enquanto a seção dura.

Serve para qualquer lista falada: notas de um perfume, exercícios, suplementos, sintomas, exames. Troque SECOES
abaixo (o exemplo é o do Legacy) e as figuras em assets/notas/<n>.png do projeto (PNG quadrado; a figura é cortada
em círculo). Tempos em segundos do cut.mp4; a palavra entre aspas acerta o tempo pela fala do corte.

  python3 itens_ao_lado_do_rosto.py PROJETO EDIT

Lê o face_layout.json do EDIT para saber onde o rosto está em cada tomada e põe o cartão no lado livre (com o
ZOOM do bloco, igual à conta do build.py). Grava compositions/cenas/<id>.html de cada seção e fim_legacy.html (o
nome do produto embaixo do frasco no zoom final) no PROJETO. Ligue cada cena em "cenas_proprias" do projeto.json.
Precisa de assets/fontes/PlayfairDisplay.ttf no projeto (Google Fonts, licença OFL).
"""
import json
import os
import sys

W, H = 1080, 1920
CARD = 262                 # largura do cartão
SLOT_Y = (392, 768)        # topo do cartão: vaga de cima e de baixo, ao lado do rosto
FOLGA = 42                 # distância mínima do rosto (orelha e cabelo passam da caixa do rosto)

SECOES = [
    dict(id='n_topo', de=17.30, ate=26.45, titulo='Notas de <b>topo</b>', titulo_em=('falam', 17.52),
         grupos=[
             dict(sai=20.12, notas=[
                 dict(n='tomilho', nome='Tomilho', em=('tomilho', 18.24)),
                 dict(n='galbano', nome='Gálbano', em=('galbano', 18.85)),
                 dict(n='artemisia', nome='Artemísia', em=('artemisia', 19.37))]),
             dict(sai=23.98, notas=[
                 dict(n='tomilho', nome='Tomilho', em=('tomilho', 20.30), selo='no', selo_em=('nao', 20.80),
                      sub=[('não senti', ('senti', 20.97))]),
                 dict(n='galbano', nome='Gálbano', em=('galbano', 21.49), selo='no', selo_em=('nao', 22.70),
                      sub=[('não dá pra sentir', ('sequer', 22.88))]),
                 dict(n='artemisia', nome='Artemísia', em=('artemisia', 22.35), selo='no', selo_em=('nao', 22.70),
                      sub=[('não dá pra sentir', ('sequer', 22.88))])]),
             dict(sai=26.35, notas=[
                 dict(n='bergamota', nome='Bergamota', em=('bergamota', 24.10), selo='ok', selo_em=('sentir', 25.83),
                      sub=[('dá pra sentir', ('sentir', 25.83))]),
                 dict(n='limao', nome='Limão', em=('limao', 24.71), selo='ok', selo_em=('sentir', 25.83),
                      sub=[('dá pra sentir', ('sentir', 25.83))])]),
         ]),
    dict(id='n_coracao', de=28.45, ate=39.22, titulo='Notas de <b>coração</b>', titulo_em=('o', 28.53),
         grupos=[
             dict(sai=30.88, notas=[
                 dict(n='vetiver', nome='Vetiver', em=('vetiver', 28.84), selo='ok', selo_em=('madeira', 30.12),
                      sub=[('madeira gostosa', ('madeira', 30.12))])]),
             dict(sai=33.00, notas=[
                 dict(n='groselha', nome='Groselha<br>preta', em=('groselha', 30.93), selo='q', selo_em=('sei', 32.14),
                      sub=[('não sei o cheiro', ('sei', 32.14))])]),
             dict(sai=36.45, notas=[
                 dict(n='pimenta_rosa', nome='Pimenta<br>rosa', em=('apimentar', 34.99), selo='ok',
                      selo_em=('rosa', 35.50), sub=[('uma apimentada', ('rosa', 35.50))])]),
             dict(sai=39.15, notas=[
                 dict(n='rosa', nome='Rosa', em=('rosa', 37.30), selo='ok', selo_em=('rosa', 37.45),
                      sub=[('dá pra sentir', ('rosa', 37.45))]),
                 dict(n='cedro', nome='Cedro', em=('cedro', 38.19), selo='ok', selo_em=('muito', 38.77),
                      sub=[('muito bom', ('muito', 38.77))])]),
         ]),
    dict(id='n_fundo', de=46.30, ate=56.15, titulo='Notas de <b>fundo</b>', titulo_em=('fundo', 46.54),
         grupos=[
             dict(sai=51.65, notas=[
                 dict(n='couro', nome='Couro', em=('couro', 47.44), selo='ok', selo_em=('couro', 50.97),
                      sub=[('também', ('couro', 50.97))]),
                 dict(n='ladano', nome='Ládano', em=('landano', 48.02), sai_antes=('ambar', 48.70)),
                 dict(n='ambar', nome='Âmbar', em=('ambar', 48.70), selo='ok', selo_em=('da', 49.71),
                      sub=[('dá pra sentir bem', ('da', 49.71))])]),
             dict(sai=56.10, notas=[
                 dict(n='benjoim', nome='Benjoim', em=('beijoim', 51.95), selo='aprox', selo_em=('misturado', 55.53),
                      sub=[('não consegui diferenciar', ('consegui', 53.05)),
                           ('misturado com couro', ('misturado', 55.53))])]),
         ]),
]

SELO = {'ok': ('✓', 'nt-ok'), 'no': ('✕', 'nt-no'), 'q': ('?', 'nt-q'), 'aprox': ('≈', 'nt-q')}


def rosto_em(layout, t):
    for s in layout['segments']:
        if s['start'] - 1e-3 <= t < s['end'] + 1e-3:
            return s['face']['x0'], s['face']['x1']
    return 0.32, 0.66


ZOOM = 1.15                # zoom do bloco nos trechos das notas (projeto.json)


def rosto_na_tela(face, z=ZOOM):
    """x0 e x1 do rosto na tela com o zoom do bloco, na conta do build.py (rosto no meio, sem mostrar borda)"""
    cx = (face['x0'] + face['x1']) / 2 * W
    x = min(0.0, max(W - z * W, W / 2 - z * cx))
    return x + z * face['x0'] * W, x + z * face['x1'] * W


def lados_livres(layout, t0, t1):
    """espaço livre (px) à esquerda e à direita do rosto, no pior momento entre t0 e t1"""
    esq, dir_ = W, W
    for s in layout['segments']:
        if s['end'] > t0 and s['start'] < t1:
            x0, x1 = rosto_na_tela(s['face'])
            esq = min(esq, x0 - FOLGA)
            dir_ = min(dir_, W - x1 - FOLGA)
    return esq, dir_


def posicionar(secao, layout):
    """escolhe lado e vaga de cada nota; devolve a lista plana com x, y, escala, entrada e saída (s absolutos)"""
    plano = []
    lado_pref = 'esq'
    for g in secao['grupos']:
        vagas = {('esq', 0): None, ('esq', 1): None, ('dir', 0): None, ('dir', 1): None}
        for nt in g['notas']:
            t_in = nt['em'][1]
            esq, dir_ = lados_livres(layout, t_in, g['sai'])
            cabe = {'esq': esq >= CARD * 0.86, 'dir': dir_ >= CARD * 0.86}
            ordem = [lado_pref, 'dir' if lado_pref == 'esq' else 'esq']
            ordem = [l for l in ordem if cabe[l]] or ['dir' if dir_ >= esq else 'esq']
            escolha = None
            for lado in ordem:                     # vaga livre, de cima para baixo
                for k in (0, 1):
                    if vagas[(lado, k)] is None:
                        escolha = (lado, k)
                        break
                if escolha:
                    break
            if not escolha:                        # tudo ocupado: a nota mais antiga do lado preferido sai
                lado = ordem[0]
                k = min((0, 1), key=lambda kk: vagas[(lado, kk)]['em'][1])
                vagas[(lado, k)]['sai_em'] = t_in - 0.06
                escolha = (lado, k)
            lado, k = escolha
            livre = esq if lado == 'esq' else dir_
            esc = round(min(1.0, max(0.78, livre / (CARD + 16))), 3)
            larg = CARD * esc
            if lado == 'esq':
                cx = max(larg / 2 + 14, min(livre / 2 + 6, livre - larg / 2))
            else:
                cx = W - max(larg / 2 + 14, min(livre / 2 + 6, livre - larg / 2))
            item = dict(nt, lado=lado, vaga=k, x=round(cx - CARD / 2), y=SLOT_Y[k], esc=esc, sai_em=g['sai'])
            vagas[escolha] = item
            plano.append(item)
            if nt.get('sai_antes'):                # sai quando a próxima chega, e a próxima entra no lugar dela
                item['sai_em'] = nt['sai_antes'][1] - 0.06
                vagas[escolha] = None
                continue
            lado_pref = 'dir' if lado == 'esq' else 'esq'
    return plano


CSS = '''@font-face{font-family:Montserrat;src:url("assets/fontes/Montserrat.ttf") format("truetype");font-weight:100 900;font-display:block}
@font-face{font-family:Playfair;src:url("assets/fontes/PlayfairDisplay.ttf") format("truetype");font-weight:400 900;font-display:block}
#root{position:absolute;inset:0;overflow:hidden;font-family:Montserrat}
.nt-hw{position:absolute;left:0;top:104px;width:1080px;display:flex;justify-content:center}
.nt-h{padding:16px 52px 20px;border-radius:44px;background:rgba(16,13,10,.76);text-align:center;white-space:nowrap;opacity:0;
  box-shadow:0 0 0 1.5px rgba(226,194,126,.72),0 18px 40px rgba(0,0,0,.42)}
.nt-k{font-weight:700;font-size:20px;letter-spacing:.34em;color:#e2c27e;margin-left:.34em}
.nt-t{font-family:Playfair;font-weight:600;font-size:58px;line-height:68px;color:#fbfaf7}
.nt-t b{color:#e2c27e;font-weight:600}
.nt-c{position:absolute;width:262px;padding:22px 0 20px;border-radius:32px;background:rgba(16,13,10,.76);text-align:center;opacity:0;
  box-shadow:0 0 0 1.5px rgba(226,194,126,.66),0 20px 44px rgba(0,0,0,.42)}
.nt-md{position:relative;width:150px;height:150px;margin:0 auto}
.nt-im{width:150px;height:150px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 3px #e2c27e,0 0 0 8px rgba(226,194,126,.18)}
.nt-im img{display:block;width:150px;height:150px;transform:scale(1.16)}
.nt-b{position:absolute;right:-10px;top:-10px;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-weight:900;font-size:31px;opacity:0;box-shadow:0 0 0 3px #16120d,0 6px 14px rgba(0,0,0,.45)}
.nt-ok{background:#58c98d;color:#06210f}
.nt-no{background:#e5484d;color:#ffffff}
.nt-q{background:#e2c27e;color:#1a1307}
.nt-nm{margin-top:16px;font-family:Playfair;font-weight:600;font-size:42px;line-height:48px;color:#fbfaf7}
.nt-ss{position:relative;height:56px;margin:8px 12px 0}
.nt-s{position:absolute;left:0;right:0;top:0;font-weight:700;font-size:22px;line-height:27px;letter-spacing:.1em;text-transform:uppercase;
  color:#e2c27e;opacity:0}'''


def html_secao(sec, plano):
    sid = sec['id']
    rel = lambda t: round(t - sec['de'], 3)
    partes = [f'<div class="nt-hw"><div class="nt-h" id="{sid}-h"><div class="nt-k">PIRÂMIDE OLFATIVA</div>'
              f'<div class="nt-t">{sec["titulo"]}</div></div></div>']
    dados = []
    for i, it in enumerate(plano):
        selo = ''
        if it.get('selo'):
            ch, cl = SELO[it['selo']]
            selo = f'<span class="nt-b {cl}" id="{sid}-b{i}">{ch}</span>'
        subs = ''.join(f'<div class="nt-s" id="{sid}-s{i}_{j}">{txt}</div>' for j, (txt, _) in enumerate(it.get('sub', [])))
        ss = f'<div class="nt-ss">{subs}</div>' if subs else ''
        alt = it['nome'].replace('<br>', ' ')
        partes.append(
            f'<div class="nt-c" id="{sid}-c{i}" style="left:{it["x"]}px;top:{it["y"]}px">'
            f'<div class="nt-md"><div class="nt-im"><img src="assets/notas/{it["n"]}.png" alt="{alt}"/></div>{selo}</div>'
            f'<div class="nt-nm">{it["nome"]}</div>{ss}</div>')
        dados.append({
            'em': [it['em'][0], 0, rel(it['em'][1])],
            'sai': rel(it['sai_em']),
            'esc': it['esc'],
            'lado': it['lado'],
            'selo': [it['selo_em'][0], 0, rel(it['selo_em'][1])] if it.get('selo') else None,
            'subs': [[w, 0, rel(t)] for _, (w, t) in it.get('sub', [])],
        })
    titulo_em = [sec['titulo_em'][0], 0, rel(sec['titulo_em'][1])]
    dur = round(sec['ate'] - sec['de'], 3)
    corpo = '\n  '.join(partes)
    js = f'''(function () {{
  const C = (window.__cenas || {{}})["{sid}"] || {{ palavras: [], duracao: {dur} }};
  const DUR = C.duracao;
  const sem = (s) => s.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase().replace(/[^a-z0-9]/g, "");
  // tempo da palavra na fala (perto do tempo medido); sem a palavra, o tempo medido
  const em = (q) => {{
    const [texto, , padrao] = q;
    let melhor = null;
    (C.palavras || []).forEach((w) => {{
      if (sem(w.texto).startsWith(sem(texto)) && Math.abs(w.t - padrao) < 0.45 &&
          (melhor === null || Math.abs(w.t - padrao) < Math.abs(melhor - padrao))) melhor = w.t;
    }});
    return melhor === null ? padrao : melhor;
  }};
  const NOTAS = {json.dumps(dados, ensure_ascii=False)};
  const fim = DUR - 0.32;
  const tl = gsap.timeline({{ paused: true }});
  const th = Math.max(0.02, em({json.dumps(titulo_em, ensure_ascii=False)}) - 0.05);
  tl.fromTo("#{sid}-h", {{ opacity: 0, y: -26, scale: 0.94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "power3.out" }}, th);
  tl.to("#{sid}-h", {{ opacity: 0, y: -16, duration: 0.3, ease: "power2.in" }}, fim);
  NOTAS.forEach((n, i) => {{
    const c = "#{sid}-c" + i, e = n.esc;
    const t0 = Math.max(0.02, em(n.em) - 0.06), t1 = Math.min(n.sai, fim);
    const dx = n.lado === "esq" ? -1 : 1;
    tl.fromTo(c, {{ opacity: 0, scale: e * 0.55, y: 40, x: dx * 26 }},
      {{ opacity: 1, scale: e, y: 0, x: 0, duration: 0.42, ease: "back.out(1.7)" }}, t0);
    tl.fromTo(c + " img", {{ scale: 1.34 }}, {{ scale: 1.16, duration: Math.max(0.3, t1 - t0), ease: "none" }}, t0);
    if (n.selo) {{
      const ts = Math.max(t0 + 0.32, em(n.selo) - 0.04);
      tl.fromTo("#{sid}-b" + i, {{ opacity: 0, scale: 0 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(3)" }}, ts);
      tl.to(c, {{ scale: e * 1.06, duration: 0.12, ease: "power2.out", yoyo: true, repeat: 1 }}, ts);
    }}
    n.subs.forEach((q, j) => {{
      const tq = Math.max(t0 + 0.3, em(q) - 0.04);
      tl.fromTo("#{sid}-s" + i + "_" + j, {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, tq);
      if (j > 0) tl.to("#{sid}-s" + i + "_" + (j - 1), {{ opacity: 0, y: -8, duration: 0.2, ease: "power2.in" }}, tq - 0.05);
    }});
    tl.to(c, {{ opacity: 0, scale: e * 0.9, y: -22, duration: 0.3, ease: "power2.in" }}, t1);
  }});
  window.__timelines["{sid}"] = tl;
}})();'''
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8"/><title>{sid} · notas que aparecem na fala</title></head>
<body>
<!-- Gerada por scripts/gera_notas_v2.py: troque lá e gere de novo. -->
<template id="{sid}-template">
<style>
{CSS}
</style>
<div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920" data-duration="{dur}">
  {corpo}
</div>
<script>
{js}
</script>
</template>
</body>
</html>
'''


def html_fim(de, ate):
    """o nome do perfume embaixo do frasco, no zoom final"""
    sid = 'fim_legacy'
    dur = round(ate - de, 3)
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8"/><title>{sid} · nome do perfume no fim</title></head>
<body>
<!-- Gerada por scripts/gera_notas_v2.py. -->
<template id="{sid}-template">
<style>
@font-face{{font-family:Montserrat;src:url("assets/fontes/Montserrat.ttf") format("truetype");font-weight:100 900;font-display:block}}
@font-face{{font-family:Playfair;src:url("assets/fontes/PlayfairDisplay.ttf") format("truetype");font-weight:400 900;font-display:block}}
#root{{position:absolute;inset:0;overflow:hidden;font-family:Montserrat}}
#fl-v{{position:absolute;left:0;right:0;bottom:0;height:640px;opacity:0;
  background:linear-gradient(to bottom,rgba(10,8,6,0) 0%,rgba(10,8,6,.62) 45%,rgba(10,8,6,.86) 100%)}}
#fl-n{{position:absolute;left:0;width:1080px;top:1500px;text-align:center;font-family:Playfair;font-weight:600;font-size:118px;
  line-height:130px;letter-spacing:.16em;color:#e2c27e;opacity:0;margin-left:.08em}}
#fl-l{{position:absolute;left:340px;width:400px;top:1654px;height:2px;background:#e2c27e;opacity:0;transform-origin:50% 50%}}
#fl-m{{position:absolute;left:0;width:1080px;top:1682px;text-align:center;font-weight:600;font-size:30px;letter-spacing:.42em;
  color:#fbfaf7;opacity:0;margin-left:.21em}}
</style>
<div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920" data-duration="{dur}">
  <div id="fl-v"></div>
  <div id="fl-n">LEGACY</div>
  <div id="fl-l"></div>
  <div id="fl-m">MAISON VIEGAS</div>
</div>
<script>
(function () {{
  const tl = gsap.timeline({{ paused: true }});
  tl.fromTo("#fl-v", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power1.out" }}, 0.02);
  tl.fromTo("#fl-n", {{ opacity: 0, y: 30, scale: 1.1 }},
    {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "power3.out" }}, 0.08);
  tl.fromTo("#fl-l", {{ opacity: 0, scaleX: 0 }}, {{ opacity: 1, scaleX: 1, duration: 0.45, ease: "power2.out" }}, 0.3);
  tl.fromTo("#fl-m", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }}, 0.4);
  window.__timelines["{sid}"] = tl;
}})();
</script>
</template>
</body>
</html>
'''


def main():
    proj, edit = sys.argv[1:3]
    layout = json.load(open(os.path.join(edit, 'face_layout.json')))
    pasta = os.path.join(proj, 'compositions', 'cenas')
    for sec in SECOES:
        plano = posicionar(sec, layout)
        for it in plano:
            print(f"{sec['id']:10s} {it['n']:13s} {it['em'][1]:6.2f}->{it['sai_em']:6.2f} {it['lado']} vaga {it['vaga']} "
                  f"x={it['x']} esc={it['esc']}")
        with open(os.path.join(pasta, sec['id'] + '.html'), 'w', encoding='utf-8') as f:
            f.write(html_secao(sec, plano))
    with open(os.path.join(pasta, 'fim_legacy.html'), 'w', encoding='utf-8') as f:
        f.write(html_fim(71.5, 72.067))


if __name__ == '__main__':
    main()
