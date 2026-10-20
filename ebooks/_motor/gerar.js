#!/usr/bin/env node
/* Gera o PDF de um e-book e audita o layout.
   Uso: node ebooks/_motor/gerar.js <pasta-do-ebook> [--previa <pasta-png>]
   A pasta precisa ter ebook.html; o PDF sai na mesma pasta com o nome de data-arquivo do <body>.
   Termina com código 1 se a auditoria encontrar problema. */
const path = require("path");
const fs = require("fs");

function carregarPlaywright() {
  for (const p of ["playwright", "/opt/node22/lib/node_modules/playwright"]) {
    try { return require(p); } catch (e) { /* tenta o próximo */ }
  }
  throw new Error("Playwright não encontrado. Instale com: npm i -g playwright");
}

(async () => {
  const args = process.argv.slice(2);
  const pasta = path.resolve(args[0] || ".");
  const iPrev = args.indexOf("--previa");
  const previa = iPrev >= 0 ? path.resolve(args[iPrev + 1]) : null;
  const html = path.join(pasta, "ebook.html");
  if (!fs.existsSync(html)) throw new Error(`Não achei ${html}`);

  const { chromium } = carregarPlaywright();
  const opts = fs.existsSync("/opt/pw-browsers/chromium") ? { executablePath: "/opt/pw-browsers/chromium" } : {};
  const nav = await chromium.launch(opts);
  const pg = await nav.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  pg.on("pageerror", (e) => console.error("Erro na página:", e.message));
  await pg.emulateMedia({ media: "print" });
  await pg.goto("file://" + html, { waitUntil: "networkidle" });
  await pg.waitForSelector("body[data-pronto='1']", { state: "attached", timeout: 20000 });

  const qa = await pg.evaluate(() => window.ebookQA());
  const arquivo = await pg.evaluate(() => document.body.dataset.arquivo || "ebook");

  console.log("Ocupação por página (%):");
  console.log(qa.paginas.map((p) => `${String(p.pagina).padStart(2, "0")}:${p.ocupacao}`).join("  "));
  const vazias = qa.paginas.filter((p) => p.ocupacao < 80);
  if (vazias.length) console.log("Aviso: páginas abaixo de 80% →", vazias.map((p) => p.pagina).join(", "));
  if (qa.citacoesSemReferencia.length) qa.problemas.push({ pagina: "-", tipo: "citação sem referência", el: qa.citacoesSemReferencia.join(", ") });
  if (qa.referenciasNaoCitadas.length) console.log("Aviso: referências não citadas →", qa.referenciasNaoCitadas.join(", "));
  qa.fontes.filter(([, ok]) => !ok).forEach(([f]) => qa.problemas.push({ pagina: "-", tipo: "fonte não carregou", el: f }));

  if (previa) {
    fs.mkdirSync(previa, { recursive: true });
    const secoes = await pg.$$(".pagina");
    for (let i = 0; i < secoes.length; i++)
      await secoes[i].screenshot({ path: path.join(previa, `p${String(i + 1).padStart(2, "0")}.png`) });
    console.log(`Prévias: ${previa}`);
  }

  const saida = path.join(pasta, `${arquivo}.pdf`);
  await pg.pdf({ path: saida, preferCSSPageSize: true, printBackground: true });
  await nav.close();
  console.log(`PDF: ${saida}`);

  if (qa.problemas.length) {
    console.log(`\n${qa.problemas.length} problema(s):`);
    qa.problemas.forEach((p) => console.log(` p.${p.pagina}  ${p.tipo}: ${p.el}`));
    process.exit(1);
  }
  console.log("Auditoria limpa.");
})().catch((e) => { console.error(e); process.exit(2); });
