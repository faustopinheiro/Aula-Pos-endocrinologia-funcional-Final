# E-books

Linha de e-books e capítulos no padrão editorial do piloto *Fisiologia da obesidade*: A4, uma ideia por
página, figura com legenda "Leia a figura", caixas de conceito e de prática, caso comentado, atalhos que
enganam, questões com respostas comentadas e referências com DOI clicável.

| Pasta | Conteúdo |
|---|---|
| [`_motor`](_motor) | Estilo, script de página, gerador de PDF e fontes (Inter e Source Serif 4, licença OFL) |
| [`fisiologia-da-obesidade`](fisiologia-da-obesidade) | Capítulo piloto: `ebook.html` (fonte), `imagens/` e o PDF gerado |

## Gerar o PDF

```bash
node ebooks/_motor/gerar.js ebooks/fisiologia-da-obesidade              # gera o PDF
node ebooks/_motor/gerar.js ebooks/fisiologia-da-obesidade --previa /tmp/previa   # e salva um PNG por página
```

O gerador usa o Chromium do Playwright e audita o layout antes de entregar. Ele sai com erro quando
encontra conteúdo transbordando a página, texto sobre texto, traço ou forma cruzando um rótulo de figura,
texto fora da figura, imagem que não carregou, fonte ausente ou citação sem referência. Também avisa sobre
páginas com menos de 80% de ocupação e referências não citadas.

## Fazer um e-book novo

1. Copie a pasta `fisiologia-da-obesidade` com o nome do tema e edite `ebook.html`.
2. No `<body>`, ajuste `data-area`, `data-autor`, `data-edicao` e `data-arquivo` (nome do PDF).
3. Cada `<section class="pagina" data-rotulo="03 • Controle central">` é uma página A4. Cabeçalho,
   rodapé e número da página são colocados pelo motor.
4. Rode o gerador e corrija o que a auditoria apontar.

### Componentes

| Marcação | Uso |
|---|---|
| `<h1>` + `<p class="linha-fina">` | Título-tese da página e subtítulo |
| `<div class="caixa">` com `<span class="tit">` | Conceito (verde-azulado) |
| `<div class="caixa pratica">` | Aplicação clínica, fala ao paciente (terracota) |
| `<div class="caixa numero">` | Número de estudo com seu limite (ouro) |
| `<figure class="fig">` com `.fig-num` e `.fig-tit` + `<p class="leia">` | Figura numerada automaticamente e sua legenda; `fig clara` para figuras com ilustração |
| `<cite>chave1, chave2</cite>` | Citação; vira `[1,2]` pela ordem da primeira aparição, com link para a referência |
| `<a class="xpag" href="#id" data-ate="#id2"></a>` | Remissão de páginas, preenchida pelo motor |
| `<ol class="objetivos">`, `<ol class="relacoes">` | Objetivos de aprendizagem e lista numerada grande |
| `<table class="compacta">` | Tabela com linhas mais baixas |
| `<div class="duas-colunas">` com `.questao` ou `.gabarito-item` | Questões e respostas comentadas |
| `<ol class="refs"></ol>` | Bibliografia; o motor distribui entre as páginas e preenche `{faixa}` no rótulo |
| `<div class="empurra"></div>` | Empurra o que vem depois (uma nota, por exemplo) para o pé da página |

As referências ficam no `<script type="application/json" id="referencias">` ao final do arquivo,
cada uma com `texto` e `doi`.

### Cor por área

O destaque fica em `--destaque` e `--destaque-claro` no `:root` de [`_motor/estilo.css`](_motor/estilo.css).
Para dar a cada área sua cor, sobrescreva as duas variáveis num `<style>` do próprio `ebook.html`.

## Anatomia do capítulo

| Bloco | Páginas | Função |
|---|---|---|
| Abertura | 1 | Ilustração, paradoxo de abertura e objetivos de aprendizagem |
| Mapa | 1 | Tabela de navegação, cinco relações para saber explicar, pergunta-guia |
| Mecanismo | 6 a 8 | Uma ideia por página: título-tese, figura com "Leia a figura", caixa de aplicação |
| Clínica | 3 a 4 | Relato → o que explorar → o que evitar; avaliação; pontes terapêuticas; caso comentado |
| Revisão | 3 | Atalhos que enganam, oito questões, respostas comentadas com síntese para o consultório |
| Referências | 1 a 2 | Numeradas por ordem de citação, com DOI |
