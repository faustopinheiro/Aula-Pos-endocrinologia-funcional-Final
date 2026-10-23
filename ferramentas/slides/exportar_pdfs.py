#!/usr/bin/env python3
"""Exporta os slides de todas as aulas em PDF, uma pasta por módulo.
Uso: python3 ferramentas/slides/exportar_pdfs.py <pasta_temporaria> [MOD02 ...]
Gera apresentacoes/Modulo NN - Nome/Aula N.M - Título.pdf a partir de slides/MODNN/*.json."""
import glob, json, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TMP = sys.argv[1]
FILTRO = sys.argv[2:]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
CAB = ('<!doctype html><html><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">'
       '<style>@page{size:1920px 1080px;margin:0}*{margin:0;box-sizing:border-box}'
       'html{-webkit-print-color-adjust:exact;print-color-adjust:exact}body{width:1920px}'
       'section{position:relative;width:1920px;height:1080px;overflow:hidden;break-after:page}'
       'aside{display:none}ol,ul{padding-left:44px}svg{display:block;flex:none}</style></head><body>')

mapa = open(os.path.join(RAIZ, "docs/07-mapa-das-aulas-escritas.md"), encoding="utf-8").read()
MODS = {int(n): nome.strip() for n, nome in re.findall(r"^## Módulo (\d+) — (.+?) · \d+ aulas", mapa, re.M)}


def limpa(t):
    return re.sub(r'[\\/:*?"<>|]', "", t.replace(": ", " - ")).strip()


for js in sorted(glob.glob(os.path.join(RAIZ, "slides/MOD*/*.json"))):
    mod = os.path.basename(os.path.dirname(js))
    if FILTRO and mod not in FILTRO:
        continue
    slot = os.path.basename(js)[:-5]                      # 02-02
    m, a = (int(x) for x in slot.split("-"))
    roteiro = glob.glob(os.path.join(RAIZ, f"aulas/{mod}/{slot}-*.md"))
    titulo = re.match(r"# .*?Aula [\d.]+ — (.+)", open(roteiro[0], encoding="utf-8").readline())[1]
    deck = os.path.join(TMP, slot)
    subprocess.run([sys.executable, os.path.join(RAIZ, "ferramentas/slides/gerar_deck.py"), js, deck],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ordem = json.load(open(os.path.join(deck, "project", "deck.json")))["order"]
    corpo = "".join(open(os.path.join(deck, "project", "slides", f"{i}.html"), encoding="utf-8").read() for i in ordem)
    html = os.path.join(TMP, f"{slot}.html")
    open(html, "w", encoding="utf-8").write(CAB + corpo + "</body></html>")
    pasta = os.path.join(RAIZ, "apresentacoes", limpa(f"Módulo {m:02d} - {MODS[m]}"))
    os.makedirs(pasta, exist_ok=True)
    pdf = os.path.join(pasta, limpa(f"Aula {m}.{a:02d} - {titulo}")[:150] + ".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    "--virtual-time-budget=8000", f"--print-to-pdf={pdf}", "file://" + html],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{slot}  {len(ordem)} slides  {os.path.relpath(pdf, RAIZ)}")
