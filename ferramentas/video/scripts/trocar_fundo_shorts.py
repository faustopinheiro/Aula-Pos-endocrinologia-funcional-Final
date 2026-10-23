#!/usr/bin/env python3
"""Troca o fundo de um vídeo em pé (9:16) por uma foto de cenário, no padrão aprovado do Shorts do Legacy.

A pessoa recortada vai na frente da foto em escala natural (os objetos do cenário pequenos perto dela), com a luz
e a cor do cenário, e a mesa da gravação fica na frente como um balcão, para a pessoa não "flutuar".

  uv run --directory '<SKILL>' python '<REPO>/ferramentas/video/scripts/trocar_fundo_shorts.py' \\
      --foto '<FOTO>' --edit '<EDIT>' --pessoa '<PESSOA_INTEIRA.webm>' --saida '<EDIT_NOVO>'

<SKILL> é a pasta da skill editor-video (o Python dela tem numpy e Pillow). Use caminhos completos.
--pessoa: o recorte do vídeo inteiro, feito antes com
  python3 ferramentas/pessoa_recortada.py --edit '<EDIT>' --saida '<PASTA>/pessoa_inteira.webm' --crf 12
--saida: uma pasta edit nova (copia a transcrição e o corte do <EDIT> e grava ali o cut.mp4 com o fundo novo).
Aponte o "edit" do projeto.json para ela.

Opções:
  --centro-x   o x da foto (px) que fica atrás da cabeça: a parte com menos coisa. Padrão: o meio da foto
  --cobre      quanto da altura da tela a foto ocupa, de cima (padrão 0.71, o aprovado). Menor = cenário menor
  --desfoque   desfoque da foto (padrão 4)
  --mesa       "y_esq,y_dir" da borda da mesa em px de 1080x1920, quando a busca automática não acha
  --sem-mesa   não põe a mesa na frente
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

W, H = 1080, 1920
# luz e cor da pessoa no cenário quente da loja (receita do LEIA da biblioteca)
AJUSTE = 'eq=brightness=-0.05:contrast=1.06:saturation=0.92:gamma=0.94,colorbalance=rm=0.03:bm=-0.04'
AJUSTE_MESA = 'eq=brightness=-0.07:saturation=0.9:gamma=0.95'


def rodar(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def fundo(foto, saida, cobre, cx, sigma):
    """a foto na largura da tela com escala menor que a de encher a altura; embaixo, a própria foto espelhada e
    escurecida (fica atrás do tronco e da mesa)"""
    im = Image.open(foto).convert('RGB')
    fw, fh = im.size
    esc = cobre * H / fh
    larg = W / esc
    if larg > fw:                      # foto estreita: usa a largura toda e a escala de encher a largura
        esc, larg = W / fw, fw
    cx = fw / 2 if cx is None else cx
    x0 = max(0, min(fw - larg, cx - 0.49 * larg))     # a cabeça fica em uns 49% da largura
    rec = im.crop((round(x0), 0, round(x0 + larg), fh)).resize((W, round(fh * esc)), Image.LANCZOS)
    tela = Image.new('RGB', (W, H))
    tela.paste(rec.crop((0, 0, W, min(H, rec.height))), (0, 0))
    falta = H - rec.height
    if falta > 0:
        esp = rec.crop((0, max(0, rec.height - falta), W, rec.height)).transpose(Image.FLIP_TOP_BOTTOM)
        tela.paste(ImageEnhance.Brightness(esp).enhance(0.55), (0, rec.height))
    tela = ImageEnhance.Brightness(tela.filter(ImageFilter.GaussianBlur(sigma))).enhance(0.96)
    tela.save(saida)
    print(f'fundo: recorte x {x0:.0f} a {x0 + larg:.0f} de {fw} px da foto, escala {esc:.2f}')


def quadro(caminho, t, alfa=False):
    cmd = ['ffmpeg', '-v', 'error'] + (['-c:v', 'libvpx-vp9'] if alfa else [])
    cmd += ['-ss', f'{t:.3f}', '-i', caminho, '-frames:v', '1']
    if alfa:
        cmd += ['-vf', 'alphaextract', '-f', 'rawvideo', '-pix_fmt', 'gray', '-']
        return np.frombuffer(rodar(cmd, capture_output=True).stdout, np.uint8).reshape(H, W)
    cmd += ['-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    return np.frombuffer(rodar(cmd, capture_output=True).stdout, np.uint8).reshape(H, W, 3)


def borda_mesa(cut, pessoa, dur, n=48):
    """a borda de cima da mesa clara: a câmera fica parada, então é uma reta. Em cada coluna, o ponto mais alto em
    que a mesa aparece em algum quadro (a pessoa se mexe e mostra a mesa), e uma reta nesses pontos. None sem mesa"""
    todos = []
    for i in range(n):
        t = 0.3 + (dur - 0.6) * i / (n - 1)
        rgb, a = quadro(cut, t), quadro(pessoa, t, alfa=True)
        r, g, b = (rgb[..., k].astype(np.int16) for k in range(3))
        mesa = (r > 185) & (g > 168) & (b > 135) & (r - b > 18) & (r - b < 60) & (g - b > 6) & (g - b < 36) & (a < 30)
        y0 = int(H * 0.70)
        c = np.cumsum(np.vstack([np.zeros((1, W), np.int32), mesa[y0:].astype(np.int32)]), axis=0)
        corrida = (c[8:] - c[:-8]) == 8
        ys = np.full(W, np.nan)
        tem = corrida.any(axis=0)
        ys[tem] = y0 + corrida.argmax(axis=0)[tem]
        todos.append(ys)
    env = np.nanpercentile(np.array(todos), 5, axis=0)
    xs = np.arange(W)
    ok = ~np.isnan(env)
    if ok.sum() < 300:
        return None
    m, c = np.polyfit(xs[ok], env[ok], 1)
    perto = ok & (np.abs(env - (m * xs + c)) < 12)
    if perto.sum() < 300:
        return None
    m, c = np.polyfit(xs[perto], env[perto], 1)
    return float(c), float(m * W + c)


def main():
    ap = argparse.ArgumentParser(description='troca o fundo do Shorts por uma foto de cenário')
    ap.add_argument('--foto', required=True)
    ap.add_argument('--edit', required=True)
    ap.add_argument('--pessoa', required=True)
    ap.add_argument('--saida', required=True)
    ap.add_argument('--centro-x', type=float, default=None)
    ap.add_argument('--cobre', type=float, default=0.71)
    ap.add_argument('--desfoque', type=float, default=4.0)
    ap.add_argument('--mesa', default=None)
    ap.add_argument('--sem-mesa', action='store_true')
    a = ap.parse_args()
    cut = os.path.join(a.edit, 'cut.mp4')
    if not os.path.exists(cut):
        sys.exit(f'não achei {cut}')
    os.makedirs(a.saida, exist_ok=True)
    trab = os.path.join(a.saida, 'fundo_trocado')
    os.makedirs(trab, exist_ok=True)
    dur = float(rodar(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', cut],
                      capture_output=True, text=True).stdout)

    bg = os.path.join(trab, 'fundo.png')
    fundo(a.foto, bg, a.cobre, a.centro_x, a.desfoque)

    linha = None
    if not a.sem_mesa:
        linha = tuple(float(v) for v in a.mesa.split(',')) if a.mesa else borda_mesa(cut, a.pessoa, dur)
        if linha:
            print(f'mesa: borda de y {linha[0]:.0f} (esquerda) a {linha[1]:.0f} (direita)')
            m = Image.new('L', (W, H), 0)
            ImageDraw.Draw(m).polygon([(0, linha[0]), (W, linha[1]), (W, H), (0, H)], fill=255)
            m.filter(ImageFilter.GaussianBlur(1.6)).save(os.path.join(trab, 'mesa.png'))
        else:
            print('aviso: não achei mesa clara na gravação; a pessoa vai direto sobre o fundo. Confira a borda de '
                  'baixo, ou passe --mesa "y_esq,y_dir"')
    json.dump({'foto': os.path.abspath(a.foto), 'cobre': a.cobre, 'centro_x': a.centro_x, 'desfoque': a.desfoque,
               'mesa': linha}, open(os.path.join(trab, 'fundo.json'), 'w'), indent=1)

    # pessoa: cor do corte com a luz do cenário e nitidez; máscara afinada. Tudo preso ao número do quadro
    # (setpts) para não perder quadro no fim
    entradas = ['-loop', '1', '-framerate', '30', '-i', bg, '-i', cut, '-c:v', 'libvpx-vp9', '-i', a.pessoa]
    grafo = (f'[1:v]setpts=N/30/TB,format=rgb24,{AJUSTE},unsharp=5:5:0.9:3:3:0,split=2[c1][c2];'
             '[2:v]setpts=N/30/TB,alphaextract,erosion,erosion,gblur=sigma=1.2[pa];[c1][pa]alphamerge[pes];'
             '[0:v]setpts=N/30/TB[bg];')
    if linha:
        entradas += ['-loop', '1', '-framerate', '30', '-i', os.path.join(trab, 'mesa.png')]
        grafo += (f'[c2]{AJUSTE_MESA}[ct];[3:v]setpts=N/30/TB,format=gray[mt];[ct][mt]alphamerge[tab];'
                  '[bg][tab]overlay=shortest=1[b1];[b1][pes]overlay=shortest=1,format=yuv420p[v]')
    else:
        grafo += '[c2]nullsink;[bg][pes]overlay=shortest=1,format=yuv420p[v]'
    novo = os.path.join(a.saida, 'cut.mp4')
    rodar(['ffmpeg', '-v', 'error', '-y'] + entradas + ['-filter_complex', grafo, '-map', '[v]', '-map', '1:a?',
          '-c:v', 'libx264', '-crf', '12', '-preset', 'medium', '-fps_mode', 'cfr', '-r', '30', '-c:a', 'copy',
          '-movflags', '+faststart', novo])
    # o resto da pasta edit (transcrição, linha do tempo do corte, rosto): igual ao original
    for nome in os.listdir(a.edit):
        if nome in ('cut.mp4', 'renders'):
            continue
        orig, dest = os.path.join(a.edit, nome), os.path.join(a.saida, nome)
        if os.path.isdir(orig):
            shutil.copytree(orig, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(orig, dest)
    q = lambda p: rodar(['ffprobe', '-v', 'error', '-select_streams', 'v', '-count_packets', '-show_entries',  # noqa: E731
                         'stream=nb_read_packets', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout.strip()
    print(f'ok: {novo} ({q(novo)} quadros; o corte original tem {q(cut)})')


if __name__ == '__main__':
    main()
