"""Ícones e pictogramas dos decks, a partir de dois conjuntos de licença MIT:
Health Icons (Resolve to Save Lives), prefixo "h:", e Tabler Icons (Paweł Kuna), prefixo "t:".

Os desenhos usados ficam copiados em icones.json, ao lado deste arquivo, para o gerador
não depender de rede. Para acrescentar ícones:
    npm i @iconify-json/healthicons @iconify-json/tabler   (numa pasta qualquer)
    python3 icones.py <pasta_com_node_modules> h:running t:brain ...
"""
import json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(AQUI, "icones.json")
CONJ = {"h": "healthicons", "t": "tabler"}
_cache = None

def _reg():
    global _cache
    if _cache is None:
        _cache = json.load(open(ARQ, encoding="utf-8")) if os.path.exists(ARQ) else {}
    return _cache

def icone(nome, x, y, tam, cor):
    """Devolve o ícone como <g> posicionado (x, y = canto superior esquerdo; tam = lado em px)."""
    r = _reg().get(nome)
    if not r:
        raise SystemExit(f"ícone {nome} não está em icones.json: rode icones.py para acrescentar")
    s = tam / max(r["w"], r["h"])
    corpo = r["body"].replace("currentColor", cor)
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.4f})">{corpo}</g>'

def svg_icone(nome, tam, cor, alt=None):
    """Um ícone sozinho, como <svg> de fluxo (largura e altura iguais ao viewBox)."""
    alt = alt or nome.split(":")[1].replace("-", " ")
    return (f'<svg aria-label="{alt}" width="{tam}" height="{tam}" viewBox="0 0 {tam} {tam}">'
            + icone(nome, 0, 0, tam, cor) + '</svg>')

def extrair(pasta, nomes):
    reg = _reg()
    dados = {}
    for pre, conj in CONJ.items():
        p = os.path.join(pasta, "node_modules", "@iconify-json", conj, "icons.json")
        if os.path.exists(p):
            dados[pre] = json.load(open(p, encoding="utf-8"))
    faltam = []
    for n in nomes:
        pre, nome = n.split(":", 1)
        d = dados.get(pre)
        if not d:
            faltam.append(n); continue
        ic = d["icons"].get(nome)
        if not ic and nome in d.get("aliases", {}):
            ic = d["icons"][d["aliases"][nome]["parent"]]
        if not ic:
            faltam.append(n); continue
        reg[n] = {"w": ic.get("width", d.get("width", 24)), "h": ic.get("height", d.get("height", 24)), "body": ic["body"]}
    json.dump(dict(sorted(reg.items())), open(ARQ, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"{len(reg)} ícones em icones.json; faltaram: {faltam}")

if __name__ == "__main__":
    extrair(sys.argv[1], sys.argv[2:])
