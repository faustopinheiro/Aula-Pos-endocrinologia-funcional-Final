"""Ajudantes comuns aos decks do Módulo 13 (O Atleta Amador e o Praticante Recreacional)."""
import json, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ferramentas", "slides"))
from desenho import *
from icones import icone

FOSF_T, OXID_T, GLIC_T, AZUL_T = "#F3E1DE", "#DDEFEC", "#F4EAD6", "#DEE7F1"
CARTAO, PAPEL, CINZA, BORDA = "#FDFCF9", "#F7F6F2", "#C9CFD4", "#D9D4C8"
TRACO = ' stroke-dasharray="10 8"'
MODULO = "O Atleta Amador e o Praticante Recreacional"


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
    spec.setdefault("tema", "grafite")
    json.dump(spec, open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), nome), "w"), ensure_ascii=False, indent=1)
    print(nome + ":", len(spec["slides"]), "slides")


# Figuras reutilizadas no módulo
def corredor(x, y, s, cor):
    """Corredor em passada, de perfil, num quadrado de lado s com canto em (x, y)."""
    k = s / 100
    def P(a, b):
        return f"{x + a * k:.0f} {y + b * k:.0f}"
    w = max(4, 9 * k)
    return (f'<circle cx="{x + 58 * k:.0f}" cy="{y + 12 * k:.0f}" r="{10 * k:.0f}" fill="{cor}"/>'
            f'<path d="M {P(55, 24)} L {P(45, 55)} M {P(45, 55)} L {P(62, 75)} L {P(55, 98)} M {P(45, 55)} L {P(30, 72)} L {P(14, 70)} '
            f'M {P(52, 32)} L {P(70, 44)} L {P(80, 34)} M {P(52, 32)} L {P(36, 42)} L {P(30, 56)}" '
            f'stroke="{cor}" stroke-width="{w:.0f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


def menino(x, base, alt, cor):
    """Silhueta simples de pé: cabeça e corpo, alt em px."""
    r = alt * 0.09
    return (f'<circle cx="{x}" cy="{base - alt + r:.0f}" r="{r:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.12:.0f}" y="{base - alt + 2 * r + 6:.0f}" width="{alt * 0.24:.0f}" height="{alt * 0.45:.0f}" rx="{alt * 0.05:.0f}" fill="{cor}"/>'
            f'<rect x="{x - alt * 0.1:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>'
            f'<rect x="{x + alt * 0.02:.0f}" y="{base - alt * 0.38:.0f}" width="{alt * 0.08:.0f}" height="{alt * 0.38:.0f}" rx="6" fill="{cor}"/>')


def camisa(x, y, s, cor):
    """Camisa de jogo vista de frente, num quadrado de lado s."""
    k = s / 100
    pts = [(30, 0), (70, 0), (100, 20), (88, 42), (78, 36), (78, 100), (22, 100), (22, 36), (12, 42), (0, 20)]
    d = " ".join(f"{x + a * k:.0f},{y + b * k:.0f}" for a, b in pts)
    return f'<polygon points="{d}" fill="{cor}"/>'
