"""Ajudantes comuns aos decks do Módulo 11 (A Atleta Mulher)."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL, CINZA, BORDA = "#FDFCF9", "#F7F6F2", "#C9CFD4", "#D9D4C8"
TRACO = ' stroke-dasharray="10 8"'
MODULO = "A Atleta Mulher"


def caixa(x, y, w, h, cor, fundo=CARTAO, esp=4, rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fundo}" stroke="{cor}" stroke-width="{esp}"/>'


def seta(x1, y1, x2, y2, cor, mk, esp=4):
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{cor}" stroke-width="{esp}" marker-end="url(#{mk})"/>'


def defs(*cores):
    return "<defs>" + "".join(seta_marker(f"m{i}", c) for i, c in enumerate(cores)) + "</defs>"


def diagrama(S, id_, h, p, rs, **k):
    S.append({"id": id_, "tipo": "diagrama", "h": h, "svg": "".join(p) + "</svg>", "rotulos": rs, **k})


def salvar(nome, spec):
    spec.setdefault("modulo", MODULO)
    spec.setdefault("tema", "terra")
    json.dump(spec, open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), nome), "w"), ensure_ascii=False, indent=1)
    print(nome + ":", len(spec["slides"]), "slides")
