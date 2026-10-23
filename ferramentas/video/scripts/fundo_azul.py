"""Fundo de estúdio azul-marinho 1920x1080: degradê radial, brilho atrás da cabeça, grade de pontos e vinheta."""
import sys

import numpy as np
from PIL import Image, ImageFilter

W, H = 1920, 1080
out = sys.argv[1]

y, x = np.mgrid[0:H, 0:W].astype(np.float32)

# base: azul-marinho mais claro no centro, mais escuro nas bordas
base_c = np.array([14, 28, 60], np.float32)
base_e = np.array([4, 8, 20], np.float32)
d = np.sqrt(((x - W * 0.5) / (W * 0.62)) ** 2 + ((y - H * 0.42) / (H * 0.75)) ** 2)
t = np.clip(d, 0, 1)[..., None] ** 1.3
img = base_c * (1 - t) + base_e * t

# brilho suave azul atrás da cabeça (centro e lado direito, onde a pessoa fica)
for cx, cy, r, k in ((0.5, 0.30, 0.30, 0.55), (0.70, 0.30, 0.24, 0.35)):
    g = np.exp(-(((x - W * cx) ** 2 + (y - H * cy) ** 2) / (2 * (W * r) ** 2)))
    img += g[..., None] * np.array([22, 42, 80], np.float32) * k

# faixas verticais de luz bem discretas (painel ripado de estúdio)
for fx in (0.16, 0.84):
    g = np.exp(-((x - W * fx) ** 2) / (2 * 6.0 ** 2)) * np.clip(1 - y / H * 0.6, 0, 1)
    img += g[..., None] * np.array([60, 105, 180], np.float32) * 0.22

# grade de pontos (como o estilo "noite")
dots = ((x.astype(int) % 36 >= 17) & (x.astype(int) % 36 <= 18) & (y.astype(int) % 36 >= 17) & (y.astype(int) % 36 <= 18)).astype(np.float32)
img += dots[..., None] * np.array([28, 44, 78], np.float32) * 0.55

# chão: leve escurecimento embaixo
img *= (1 - 0.35 * np.clip((y / H - 0.75) / 0.25, 0, 1))[..., None]

# ruído fino para não formar degraus no degradê
img += np.random.default_rng(7).normal(0, 1.2, img.shape).astype(np.float32)

im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB").filter(ImageFilter.GaussianBlur(0.6))
im.save(out)
print(out)
