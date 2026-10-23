#!/usr/bin/env python3
"""Raio-x do material de um vídeo antes de escolher a receita de edição.

Uso:
    python3 analisar.py <PASTA ou VÍDEO> [--json]

Olha só o que dá para medir sem transcrever (rápido, segundos):
  - cada vídeo: orientação (16:9, 9:16...), duração, resolução, quadros por segundo, áudio;
  - os outros arquivos da pasta: PowerPoint, PDF, imagens (fundo, exames, prints), música;
  - o PowerPoint: título e texto de cada slide, se o slide tem imagem/gráfico/tabela, e as anotações.

Só usa a biblioteca padrão do Python e o ffprobe (o instalador do Chip põe em ~/.editor-video/bin).
A transcrição e a medida de ruído ficam com os helpers do Chip (transcribe_batch.py, noise_check.py).
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

VIDEO = {".mp4", ".mov", ".m4v", ".mkv", ".webm"}
IMAGEM = {".png", ".jpg", ".jpeg", ".webp", ".heic"}
AUDIO = {".mp3", ".wav", ".m4a", ".aac"}


def achar_ffprobe() -> str | None:
    achado = shutil.which("ffprobe")
    if achado:
        return achado
    for cand in (Path.home() / ".editor-video" / "bin" / "ffprobe", Path.home() / ".editor-video" / "bin" / "ffprobe.exe"):
        if cand.is_file():
            return str(cand)
    return None


def medir_video(caminho: Path, ffprobe: str | None) -> dict:
    info = {"arquivo": caminho.name, "tamanho_mb": round(caminho.stat().st_size / 1e6, 1)}
    if not ffprobe:
        info["aviso"] = "sem ffprobe: instale o Chip ou o ffmpeg"
        return info
    r = subprocess.run([ffprobe, "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(caminho)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        info["aviso"] = "o ffprobe não conseguiu ler este arquivo"
        return info
    d = json.loads(r.stdout or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), None)
    a = next((s for s in d.get("streams", []) if s.get("codec_type") == "audio"), None)
    dur = float(d.get("format", {}).get("duration") or 0)
    info["duracao_s"] = round(dur, 1)
    if v:
        w, h = int(v.get("width") or 0), int(v.get("height") or 0)
        rot = 0
        for sd in v.get("side_data_list", []) or []:
            if "rotation" in sd:
                rot = int(float(sd["rotation"]))
        if abs(rot) in (90, 270):
            w, h = h, w
        num, _, den = (v.get("r_frame_rate") or "0/1").partition("/")
        fps = float(num) / float(den or 1) if float(den or 1) else 0
        info.update(largura=w, altura=h, fps=round(fps, 2), codec=v.get("codec_name"))
        razao = w / h if h else 0
        info["orientacao"] = ("deitado (16:9)" if razao > 1.3 else "em pé (9:16)" if razao < 0.8
                              else "quadrado ou 4:5")
        # webcam costuma gravar 1080p com bitrate baixo e áudio a 16 ou 32 kHz
        br = int(d.get("format", {}).get("bit_rate") or 0)
        info["bitrate_mbps"] = round(br / 1e6, 1)
    if a:
        sr = int(a.get("sample_rate") or 0)
        info["audio_hz"] = sr
        if sr and sr <= 32000:
            info["dica_audio"] = "áudio de 16 ou 32 kHz: típico de webcam; rode o noise_check e espere chiado ou eco"
    else:
        info["dica_audio"] = "sem áudio"
    return info


def texto_xml(xml: str) -> list[str]:
    """os parágrafos de texto de um slide (cada <a:p> vira uma linha)"""
    linhas = []
    for par in re.findall(r"<a:p>.*?</a:p>", xml, flags=re.S):
        t = "".join(re.findall(r"<a:t>([^<]*)</a:t>", par)).strip()
        if t:
            linhas.append(t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))
    return linhas


def ler_pptx(caminho: Path) -> dict:
    out = {"arquivo": caminho.name, "slides": []}
    try:
        z = zipfile.ZipFile(caminho)
    except zipfile.BadZipFile:
        out["aviso"] = "não é um .pptx válido"
        return out
    nomes = z.namelist()
    tam = re.search(r'<p:sldSz[^>]*cx="(\d+)"[^>]*cy="(\d+)"', z.read("ppt/presentation.xml").decode("utf-8", "replace")) \
        if "ppt/presentation.xml" in nomes else None
    area_slide = int(tam.group(1)) * int(tam.group(2)) if tam else 0
    slides = sorted((n for n in nomes if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                    key=lambda n: int(re.search(r"(\d+)", n.rsplit("/", 1)[1]).group(1)))
    for n in slides:
        num = int(re.search(r"slide(\d+)\.xml", n).group(1))
        xml = z.read(n).decode("utf-8", "replace")
        linhas = texto_xml(xml)
        # imagem que conta é a grande (desenho, foto, print); a logo pequena do canto, repetida em todo slide, não conta
        tem_imagem = False
        for pic in re.findall(r"<p:pic>.*?</p:pic>", xml, flags=re.S):
            ext = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', pic)
            if not ext or not area_slide or int(ext.group(1)) * int(ext.group(2)) > 0.12 * area_slide:
                tem_imagem = True
        tem_grafico = "graphicData" in xml and "chart" in xml
        tem_tabela = "<a:tbl>" in xml
        nota = []
        rel = f"ppt/slides/_rels/slide{num}.xml.rels"
        if rel in nomes:
            alvo = re.search(r'Target="\.\./notesSlides/(notesSlide\d+\.xml)"', z.read(rel).decode("utf-8", "replace"))
            if alvo and f"ppt/notesSlides/{alvo.group(1)}" in nomes:
                nota = [l for l in texto_xml(z.read(f"ppt/notesSlides/{alvo.group(1)}").decode("utf-8", "replace"))
                        if not l.isdigit()]
        visual = tem_imagem or tem_grafico or tem_tabela
        out["slides"].append({
            "slide": num,
            "textos": linhas[:14],
            "tem_imagem_grafico_ou_tabela": visual,
            # slide só de texto curto vira janela lateral; com desenho, entra o slide inteiro
            "sugestao": "slide inteiro (tem desenho)" if visual else "texto ao lado (janela lateral)",
            "anotacao": " ".join(nota)[:400],
        })
    out["total_slides"] = len(out["slides"])
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    alvo = Path(sys.argv[1]).expanduser()
    como_json = "--json" in sys.argv
    if not alvo.exists():
        print(f"não achei {alvo}")
        return 2
    pasta = alvo if alvo.is_dir() else alvo.parent
    arquivos = [alvo] if alvo.is_file() else sorted(p for p in pasta.iterdir() if p.is_file() and not p.name.startswith("."))
    if alvo.is_file():   # o vídeo veio sozinho: olha os vizinhos também (slides e fundo costumam estar junto)
        arquivos += sorted(p for p in pasta.iterdir() if p.is_file() and p != alvo and not p.name.startswith("."))
    ffprobe = achar_ffprobe()
    rel = {"pasta": str(pasta), "videos": [], "powerpoints": [], "pdfs": [], "imagens": [], "audios": [], "outros": []}
    for p in arquivos:
        ext = p.suffix.lower()
        if ext in VIDEO:
            rel["videos"].append(medir_video(p, ffprobe))
        elif ext == ".pptx":
            rel["powerpoints"].append(ler_pptx(p))
        elif ext == ".pdf":
            rel["pdfs"].append(p.name)
        elif ext in IMAGEM:
            rel["imagens"].append(p.name)
        elif ext in AUDIO:
            rel["audios"].append(p.name)
        else:
            rel["outros"].append(p.name)
    nomes = [v["arquivo"].lower() for v in rel["videos"]]
    rel["varios_videos"] = len(rel["videos"]) > 1
    rel["parece_blocos_de_uma_aula"] = rel["varios_videos"] and any(re.search(r"(bloco|parte|take|_\d+\.)", n) for n in nomes)
    durs = [v.get("duracao_s", 0) for v in rel["videos"]]
    rel["parece_varias_cameras"] = (rel["varios_videos"] and len(durs) >= 2
                                    and max(durs) > 0 and min(durs) / max(durs) > 0.85 and not rel["parece_blocos_de_uma_aula"])
    if como_json:
        print(json.dumps(rel, ensure_ascii=False, indent=1))
        return 0
    print(f"Pasta: {rel['pasta']}")
    for v in rel["videos"]:
        print(f"- vídeo {v['arquivo']}: {v.get('orientacao', '?')}, {v.get('duracao_s', '?')} s, "
              f"{v.get('largura', '?')}x{v.get('altura', '?')} a {v.get('fps', '?')} fps, "
              f"{v.get('bitrate_mbps', '?')} Mb/s, áudio {v.get('audio_hz', '?')} Hz"
              + (f" · {v['dica_audio']}" if v.get("dica_audio") else "") + (f" · {v['aviso']}" if v.get("aviso") else ""))
    for pp in rel["powerpoints"]:
        print(f"- PowerPoint {pp['arquivo']}: {pp.get('total_slides', 0)} slides")
        for s in pp["slides"]:
            print(f"    slide {s['slide']:>2} · {s['sugestao']} · " + " | ".join(s["textos"][:4])[:160])
    for k, rot in (("pdfs", "PDF"), ("imagens", "imagem"), ("audios", "áudio"), ("outros", "outro")):
        for n in rel[k]:
            print(f"- {rot}: {n}")
    if rel["parece_blocos_de_uma_aula"]:
        print("- vários arquivos com nome de bloco/parte: provável aula gravada em blocos (junta na ordem)")
    if rel["parece_varias_cameras"]:
        print("- vários vídeos com a mesma duração: provável gravação com mais de uma câmera (sincronizar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
