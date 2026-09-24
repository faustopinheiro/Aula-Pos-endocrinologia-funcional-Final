#!/usr/bin/env python3
"""Prévia local de um deck gerado: um PNG por slide (960x540), só para conferir
sobreposição e encaixe. Não publica nada.
Uso: python3 previa.py <pasta_do_deck> <pasta_png> [id1 id2 ...]"""
import json, os, subprocess, sys
deck, saida = sys.argv[1], sys.argv[2]
ids = sys.argv[3:]
os.makedirs(saida, exist_ok=True)
ordem = json.load(open(os.path.join(deck, "project", "deck.json")))["order"]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
cab = ('<!doctype html><html><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">'
       '<style>*{margin:0;box-sizing:border-box}body{width:1920px;height:1080px;overflow:hidden}'
       'section{position:relative;width:1920px;height:1080px;overflow:hidden}aside{display:none}'
       'ol,ul{padding-left:44px}svg{display:block;flex:none}</style></head><body>')
for i in (ids or ordem):
    html = open(os.path.join(deck, "project", "slides", f"{i}.html"), encoding="utf-8").read()
    arq = os.path.join(saida, f"{i}.html")
    open(arq, "w", encoding="utf-8").write(cab + html + "</body></html>")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--force-device-scale-factor=0.5", "--window-size=1920,1080", "--virtual-time-budget=3000",
                    f"--screenshot={os.path.join(saida, i + '.png')}", "file://" + os.path.abspath(arq)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(os.path.join(saida, i + ".png"))
