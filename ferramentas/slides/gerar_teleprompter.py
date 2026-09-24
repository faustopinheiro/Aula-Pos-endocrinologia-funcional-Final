#!/usr/bin/env python3
"""Gera o texto de teleprompter de uma aula: só a fala, com a marcação
[INÍCIO DO SLIDE N DE T · título] e [FIM DO SLIDE N DE T] em volta de cada
trecho. N é o número do slide no deck (a capa é o slide 1), o mesmo que
aparece no rodapé. O trecho entre as marcações é exatamente o que está nas
anotações daquele slide.

Uso: python3 gerar_teleprompter.py slides/MOD01/01-01.json teleprompter/MOD01
"""
import json, os, re, sys

def limpa(t):
    return re.sub(r"<[^>]+>", "", t).replace("“", "\"").replace("”", "\"").strip()

def titulo_do_slide(s):
    return limpa(s.get("titulo") or s.get("eyebrow") or s.get("frase", ""))

def blocos_de_fala(md_path):
    txt = open(md_path, encoding="utf-8").read().split("## Referências")[0]
    partes = re.split(r"^📊 \*\*\[SLIDE \d+ DE \d+\]\*\*\s*$", txt, flags=re.M)[1:]
    saida = []
    for b in partes:
        paras = []
        for l in b.split("\n"):
            l = l.strip()
            if not l or l == "---" or l.startswith("*Visual") or l.startswith("*Teleprompter"):
                continue
            paras.append(l.replace("**", ""))
        saida.append(paras)
    return saida

def gerar(spec_path, pasta):
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    spec = json.load(open(spec_path, encoding="utf-8"))
    blocos = blocos_de_fala(os.path.join(raiz, spec["arquivo"]))
    slides = spec["slides"]
    if len(slides) != len(blocos):
        raise SystemExit(f"spec tem {len(slides)} slides e a aula tem {len(blocos)} blocos")
    total = len(slides) + 1
    linhas = [f"# {spec['titulo']}", "", f"[SLIDE 1 DE {total} · CAPA · abrir a aula com ela na tela]", ""]
    for i, (s, paras) in enumerate(zip(slides, blocos), start=2):
        linhas.append(f"[INÍCIO DO SLIDE {i} DE {total} · {titulo_do_slide(s)}]")
        linhas.append("")
        for p in paras:
            linhas += [p, ""]
        linhas.append(f"[FIM DO SLIDE {i} DE {total}]")
        linhas += ["", ""]
    os.makedirs(pasta, exist_ok=True)
    nome = os.path.basename(spec["arquivo"])
    destino = os.path.join(pasta, nome)
    open(destino, "w", encoding="utf-8").write("\n".join(linhas).rstrip() + "\n")
    print(destino)

if __name__ == "__main__":
    gerar(sys.argv[1], sys.argv[2])
