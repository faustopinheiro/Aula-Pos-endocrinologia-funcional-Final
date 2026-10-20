/* Motor de e-books: roda dentro da página (navegador ou Playwright).
   Monta cabeçalho e rodapé, numera figuras, citações e páginas, distribui a bibliografia
   e expõe window.ebookQA() com a auditoria de layout. */
(function () {
  const $$ = (sel, raiz = document) => Array.from(raiz.querySelectorAll(sel));
  function montarPaginas() {
    const corpo = document.body.dataset;
    $$(".pagina").forEach((pg, i) => {
      if (!pg.querySelector(":scope > .corpo")) {
        const c = document.createElement("div");
        c.className = "corpo";
        while (pg.firstChild) c.appendChild(pg.firstChild);
        pg.appendChild(c);
      }
      pg.dataset.num = i + 1;
      const cab = document.createElement("div");
      cab.className = "cabeca";
      cab.innerHTML = `<span class="rotulo"></span><span class="area">${corpo.area || ""}</span>`;
      cab.querySelector(".rotulo").textContent = pg.dataset.rotulo || "";
      const pe = document.createElement("div");
      pe.className = "pe";
      pe.innerHTML = `<span>${corpo.autor || ""} &nbsp;•&nbsp; ${corpo.edicao || ""}</span><span class="num">${String(i + 1).padStart(2, "0")}</span>`;
      pg.prepend(cab);
      pg.appendChild(pe);
    });
  }

  function numerarFiguras() {
    $$("figure.fig").forEach((f, i) => {
      const n = i + 1;
      if (!f.id) f.id = `figura-${n}`;
      f.dataset.n = n;
      const num = f.querySelector(".fig-num");
      if (num) num.textContent = `Figura ${n}`;
    });
    $$("a.xfig").forEach((a) => {
      const alvo = document.querySelector(a.getAttribute("href"));
      a.textContent = alvo ? `Figura ${alvo.dataset.n}` : "Figura ??";
    });
  }

  function faixas(nums) {
    nums = [...new Set(nums)].sort((a, b) => a - b);
    const out = [];
    for (let i = 0; i < nums.length; i++) {
      let j = i;
      while (j + 1 < nums.length && nums[j + 1] === nums[j] + 1) j++;
      if (j - i >= 2) out.push([nums[i], nums[j]]);
      else for (let k = i; k <= j; k++) out.push([nums[k]]);
      i = j;
    }
    return out;
  }

  function citacoes() {
    const fonte = document.getElementById("referencias");
    const refs = fonte ? JSON.parse(fonte.textContent) : {};
    const ordem = [];
    const faltando = [];
    $$("cite").forEach((c) => {
      const chaves = c.textContent.split(",").map((s) => s.trim()).filter(Boolean);
      const nums = chaves.map((k) => {
        if (!refs[k]) { faltando.push(k); return null; }
        if (!ordem.includes(k)) ordem.push(k);
        return ordem.indexOf(k) + 1;
      }).filter((n) => n);
      c.innerHTML = "[" + faixas(nums).map((f) =>
        f.length === 1 ? `<a href="#ref-${f[0]}">${f[0]}</a>` : `<a href="#ref-${f[0]}">${f[0]}-${f[1]}</a>`
      ).join(",") + "]";
    });
    const naoCitadas = Object.keys(refs).filter((k) => !ordem.includes(k));
    return { refs, ordem, faltando, naoCitadas };
  }

  function bibliografia({ refs, ordem }) {
    const caixas = $$("ol.refs");
    if (!caixas.length) return;
    const itens = ordem.map((k, i) => {
      const r = refs[k];
      const li = document.createElement("li");
      li.id = `ref-${i + 1}`;
      li.dataset.n = i + 1;
      li.innerHTML = `<span class="n">${String(i + 1).padStart(2, "0")}.</span>${r.texto}` +
        (r.doi ? `<br><a href="https://doi.org/${r.doi}">doi: ${r.doi}</a>` : "");
      return li;
    });
    let atual = 0;
    for (const li of itens) {
      caixas[atual].appendChild(li);
      const c = caixas[atual].closest(".corpo");
      if (c.scrollHeight > c.clientHeight + 1 && atual + 1 < caixas.length) {
        atual++;
        caixas[atual].appendChild(li);
      }
    }
    caixas.forEach((ol) => {
      const ns = $$("li", ol).map((li) => +li.dataset.n);
      const pg = ol.closest(".pagina");
      const txt = ns.length ? `${String(ns[0]).padStart(2, "0")}-${String(ns[ns.length - 1]).padStart(2, "0")}` : "";
      const rot = pg.querySelector(".cabeca .rotulo");
      rot.textContent = rot.textContent.replace("{faixa}", txt);
    });
  }

  function paginasCruzadas() {
    const pag = (sel) => {
      const el = document.querySelector(sel);
      return el ? +el.closest(".pagina").dataset.num : NaN;
    };
    $$("a.xpag").forEach((a) => {
      const de = pag(a.getAttribute("href"));
      const ate = a.dataset.ate ? pag(a.dataset.ate) : de;
      a.textContent = de === ate ? `p. ${de}` : `pp. ${de}-${ate}`;
    });
  }

  /* ---------------- auditoria ---------------- */
  function sobrepoe(a, b, folga = 0) {
    const w = Math.min(a.right, b.right) - Math.max(a.left, b.left) - folga;
    const h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) - folga;
    return w > 0 && h > 0 ? w * h : 0;
  }
  const contem = (fora, dentro) =>
    dentro.left >= fora.left - 0.5 && dentro.right <= fora.right + 0.5 &&
    dentro.top >= fora.top - 0.5 && dentro.bottom <= fora.bottom + 0.5;
  const desc = (el) => (el.id ? `#${el.id}` : "") + ` "${(el.textContent || el.tagName).trim().slice(0, 40)}"`;

  function pontosDoTraco(el) {
    const pts = [];
    if (typeof el.getTotalLength !== "function") return pts;
    const total = el.getTotalLength();
    const ctm = el.getScreenCTM();
    const svg = el.ownerSVGElement;
    for (let d = 0; d <= total; d += 1.5) {
      const p = el.getPointAtLength(d);
      const q = svg.createSVGPoint();
      q.x = p.x; q.y = p.y;
      const t = q.matrixTransform(ctm);
      pts.push(t);
    }
    return pts;
  }

  function auditarSVG(svg, pg, problemas) {
    const ignorar = (el) => el.closest("defs, marker, [data-qa=ignorar]");
    const textos = $$("text", svg).filter((t) => !ignorar(t) && t.textContent.trim());
    const formas = $$("rect, circle, ellipse, image, polygon", svg).filter((e) => !ignorar(e) && !e.classList.contains("fundo"));
    const tracos = $$("path, line, polyline", svg).filter((e) => !ignorar(e) && !e.classList.contains("fundo"));
    const caixa = svg.getBoundingClientRect();
    const rt = textos.map((t) => t.getBoundingClientRect());
    textos.forEach((t, i) => {
      const r = rt[i];
      if (!contem(caixa, r)) problemas.push({ pagina: pg, tipo: "texto fora da figura", el: desc(t) });
      for (let j = i + 1; j < textos.length; j++)
        if (sobrepoe(r, rt[j], 0.5) > 1) problemas.push({ pagina: pg, tipo: "texto sobre texto", el: desc(t) + " x " + desc(textos[j]) });
      formas.forEach((f) => {
        const rf = f.getBoundingClientRect();
        const area = sobrepoe(r, rf, 0.5);
        if (!area) return;
        if (f.tagName === "image" || !contem(rf, r))
          problemas.push({ pagina: pg, tipo: "texto sobre forma", el: desc(t) + " x <" + f.tagName + (f.id ? "#" + f.id : "") + ">" });
      });
      tracos.forEach((l) => {
        const pts = l.tagName === "line"
          ? (() => { // linha: amostra a reta em coordenadas de tela
              const ctm = l.getScreenCTM(), s = l.ownerSVGElement.createSVGPoint(), e = l.ownerSVGElement.createSVGPoint();
              s.x = l.x1.baseVal.value; s.y = l.y1.baseVal.value; e.x = l.x2.baseVal.value; e.y = l.y2.baseVal.value;
              const a = s.matrixTransform(ctm), b = e.matrixTransform(ctm), n = 60;
              return Array.from({ length: n + 1 }, (_, k) => ({ x: a.x + (b.x - a.x) * k / n, y: a.y + (b.y - a.y) * k / n }));
            })()
          : pontosDoTraco(l);
        const pad = 0.6;
        if (pts.some((p) => p.x > r.left + pad && p.x < r.right - pad && p.y > r.top + pad && p.y < r.bottom - pad))
          problemas.push({ pagina: pg, tipo: "traço cruza texto", el: desc(t) + " x <" + l.tagName + (l.id ? "#" + l.id : "") + ">" });
      });
    });
  }

  window.ebookQA = function () {
    const problemas = [];
    const paginas = [];
    $$(".pagina").forEach((pg) => {
      const n = +pg.dataset.num;
      const c = pg.querySelector(".corpo");
      const altura = c.clientHeight;
      const usado = Array.from(c.children).filter((e) => !e.classList.contains("empurra")).reduce((s, e) => {
        const cs = getComputedStyle(e);
        return s + e.getBoundingClientRect().height + parseFloat(cs.marginTop) + parseFloat(cs.marginBottom);
      }, 0);
      const transborda = c.scrollHeight - c.clientHeight;
      paginas.push({ pagina: n, ocupacao: Math.round((usado / altura) * 100) });
      if (transborda > 1) problemas.push({ pagina: n, tipo: "conteúdo transborda", el: `${Math.round(transborda)}px` });
      if (c.scrollWidth > c.clientWidth + 1) problemas.push({ pagina: n, tipo: "conteúdo largo demais", el: `${c.scrollWidth - c.clientWidth}px` });
      $$("svg", pg).forEach((s) => auditarSVG(s, n, problemas));
      $$("img", pg).forEach((im) => { if (!im.complete || !im.naturalWidth) problemas.push({ pagina: n, tipo: "imagem não carregou", el: im.src }); });
    });
    return { problemas, paginas, ...window.ebookInfo };
  };

  async function iniciar() {
    await document.fonts.ready;
    montarPaginas();
    numerarFiguras();
    const cit = citacoes();
    bibliografia(cit);
    paginasCruzadas();
    window.ebookInfo = {
      citacoesSemReferencia: [...new Set(cit.faltando)],
      referenciasNaoCitadas: cit.naoCitadas,
      fontes: ["Inter", "Source Serif 4"].map((f) => [f, document.fonts.check(`700 12px "${f}"`)]),
    };
    document.body.dataset.pronto = "1";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
