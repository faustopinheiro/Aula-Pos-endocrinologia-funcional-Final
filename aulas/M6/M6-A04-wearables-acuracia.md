# M6 · Aula 4 — Wearables de consumo: acurácia métrica por métrica

**Módulo 6 — Avaliação funcional e monitoramento acessível**
Pós-Graduação em Saúde Clínica Aplicada ao Esporte
Duração: 18 minutos · 6 slides

---

📊 **[SLIDE 1 DE 6]**
*Visual: um relógio esportivo com cinco métricas na tela, e cada uma recebendo uma nota diferente ao lado — de A a D.*
*Teleprompter: (entra pelo enquadramento)*

A pergunta que todo mundo faz sobre tecnologia vestível é: **relógio é confiável?**

E ela não tem resposta, porque a pergunta está no nível errado.

Um relógio não é uma medida. É uma caixa com dois ou três sensores físicos que alimentam uma dúzia de métricas — e a acurácia dessas métricas varia enormemente entre elas.

O mesmo aparelho pode ser excelente para uma coisa e péssimo para outra, na mesma tela, no mesmo segundo.

Então a pergunta certa é: **essa métrica específica, nesse aparelho, nessa situação, é confiável para a decisão que eu vou tomar?**

E para responder isso, ajuda saber o que existe de sensor ali dentro, porque tudo o mais é derivado.

Praticamente todo aparelho de pulso tem três coisas: um **acelerômetro**, que detecta movimento em três eixos; um **sensor óptico de frequência cardíaca**, que ilumina a pele e lê a variação da luz refletida conforme o sangue pulsa — a fotopletismografia; e frequentemente um **GPS**.

Todo o resto é cálculo. Gasto calórico é cálculo. Estágio de sono é cálculo. Carga de treino é cálculo. Nível de estresse é cálculo. Idade corporal é cálculo com marketing.

Aquela pergunta da primeira aula — **isso foi medido ou foi calculado?** — resolve a maior parte dos casos aqui.

E vale dizer o que isso não é: não é uma aula contra tecnologia. Esses aparelhos democratizaram acesso a dados que há vinte anos exigiam laboratório, e isso é bom. Eles só precisam ser usados com a mesma disciplina que a gente aplicou aos exames no módulo passado.

Sensor bom com interpretação ruim produz o mesmo dano que exame bom sem pergunta.

E tem uma assimetria de validação que vale conhecer: os fabricantes não são obrigados a publicar dados de acurácia, e a maior parte não publica. O que existe de validação independente vem de grupos acadêmicos que compram os aparelhos e testam por conta própria — e sempre com atraso, porque o modelo testado já saiu de linha quando o artigo é publicado.

Ou seja, você está sempre avaliando a geração anterior. Isso não invalida nada, mas recomenda humildade com o modelo lançado no mês passado.

---

📊 **[SLIDE 2 DE 6]**
*Visual: um pé caminhando com contagem de passos correta, e ao lado a mesma pessoa empurrando um carrinho com a contagem errada.*
*Teleprompter: (tom de dado, métrica por métrica)*

Vamos métrica por métrica, começando pela mais simples.

**Passos.** Essa é a boa notícia. Fuller e colaboradores publicaram em 2020 uma revisão sistemática da confiabilidade e validade de dispositivos comerciais para passos, gasto energético e frequência cardíaca, e a conclusão para passos é favorável: os aparelhos são acurados em ambiente laboratorial, com variação entre fabricantes e modelos.

Onde a contagem de passos erra, na vida real, é previsível: **velocidade muito baixa** — caminhada lenta de idoso, andar dentro de casa — costuma ser subestimada; e **movimento de braço sem deslocamento** — dirigir em estrada de terra, aplaudir, escovar dente com energia — é contado como passo.

Para o uso que interessa, que é acompanhar volume de atividade diária da mesma pessoa ao longo do tempo, passos servem muito bem. É, provavelmente, a métrica mais honesta do aparelho.

**Frequência cardíaca.** Aqui é preciso separar duas situações, porque elas não são a mesma coisa.

**Em repouso e em exercício de intensidade estável**, o sensor óptico de pulso vai razoavelmente bem. A revisão do Fuller sustenta isso.

**Em exercício intenso, intervalado ou com muito movimento de punho**, a acurácia cai — e às vezes cai muito. Musculação, remo, escalada, boxe, crossfit. Os motivos são mecânicos: o sensor precisa de contato estável com a pele, e a contração muscular do antebraço, o suor e o movimento atrapalham a leitura óptica.

Tem ainda um erro clássico e reconhecível: o aparelho perde o sinal e começa a **travar na cadência do passo** em vez da frequência cardíaca real. O valor fica bonito e estável, e está errado.

E um fator que quase ninguém comenta: **tom de pele mais escuro e tatuagens** interferem na leitura óptica, porque afetam a absorção da luz.

A regra prática: para decisão que depende de frequência cardíaca precisa — zona de treino, teste submáximo, prescrição por faixa — use **cinta peitoral**. Ela é eletrocardiográfica, não óptica, e resolve o problema por vinte reais de diferença por mês de uso.

E a **frequência cardíaca de repouso**, medida pelo próprio aparelho durante o sono, é uma das melhores coisas que o relógio entrega — porque a condição de coleta é naturalmente padronizada e a série é longa. Poucos profissionais usam, e ela costuma ser mais informativa que a variabilidade da aula passada.

---

📊 **[SLIDE 3 DE 6]**
*Visual: um hipnograma real ao lado do hipnograma do relógio, com as fases em posições diferentes mas o tempo total parecido.*
*Teleprompter: (tom de dado, com precisão)*

**Sono.** Esta é a métrica mais usada, a mais discutida em consultório, e a que mais precisa de nuance.

Chinoy e colaboradores testaram, em 2021, sete dispositivos de consumo contra polissonografia, o padrão-ouro, em trinta e quatro adultos saudáveis, ao longo de três noites em laboratório de sono.

E o resultado tem duas metades bem diferentes.

**Para distinguir sono de vigília e estimar tempo total de sono**, os dispositivos foram razoáveis — alguns comparáveis à actigrafia de pesquisa.

**Para classificar estágios de sono** — leve, profundo, REM —, o desempenho foi bem mais fraco e variável entre aparelhos.

Isso é o oposto de como o dado é apresentado ao usuário. O aplicativo mostra o gráfico colorido dos estágios com confiança enorme, e é justamente essa parte que menos se sustenta.

O motivo é físico: estágio de sono é definido por atividade elétrica cerebral, movimento ocular e tônus muscular. O relógio não mede nada disso. Ele mede movimento e pulso, e infere o resto por algoritmo.

O que isso significa na sua sala, de forma muito concreta:

**Use a duração e a regularidade.** "Você dormiu em média cinco horas e vinte nas últimas duas semanas, e deitou em horários que variaram três horas" — isso é informação boa, acionável, e o aparelho entrega bem.

**Não use os estágios para nada clínico.** Não diga que a pessoa tem "pouco sono profundo", não trate isso, e desfaça essa preocupação quando ela chegar — porque ela chega com frequência.

E lembra da ortossonia, que a gente viu no Módulo 4: a preocupação com o dado do rastreador piorando o próprio sono. Boa parte dela nasce exatamente da parte da tela que menos tem validade.

Tem um uso bonito do aparelho aqui, e ele não é o número: ele serve para **mostrar à pessoa a janela de oportunidade de sono dela**. Quando alguém vê, preto no branco, que deitou às 00h40 e levantou às 05h50 durante três semanas, a conversa fica muito mais fácil do que com qualquer argumento.

Lembra da aula de sono do Módulo 4: o erro mais caro ali era tratar restrição como insônia, porque remédio não fabrica horas. O rastreador é excelente justamente para desfazer essa confusão, porque ele mostra a janela — e janela curta com poucos despertares é restrição, não insônia.

---

📊 **[SLIDE 4 DE 6]**
*Visual: um prato de comida ao lado da tela do relógio marcando "620 kcal queimadas", com uma margem de erro larga desenhada em volta do número.*
*Teleprompter: (tom firme)*

**Gasto energético.** Esta é a métrica pior, e é a que mais causa dano concreto.

Na revisão do Fuller, a conclusão para gasto energético é francamente desfavorável: é a medida com pior desempenho do conjunto, com erro considerável e inconsistente entre aparelhos e atividades.

E faz sentido, pela física. O aparelho não mede calor, não mede troca gasosa, não mede consumo de oxigênio. Ele estima a partir de movimento e frequência cardíaca, usando equações populacionais com peso, altura, idade e sexo — e a variação individual de economia de movimento e de eficiência metabólica é grande.

O dano é direto: a pessoa vê "queimei seiscentas e vinte calorias" e come com base nisso. Se o erro for de trinta por cento para mais, ela come duzentas calorias a mais por sessão, todo dia — e não entende por que não emagrece.

E tem o dano oposto, que eu vejo em quem restringe: o número baixo do aparelho vira justificativa para comer menos ainda, num contexto em que a conta já está apertada.

Então a orientação é curta: **não use gasto energético do relógio para nenhuma decisão alimentar.** Não é uma questão de calibrar melhor. A medida não tem acurácia para essa finalidade.

Duas outras métricas, rápido.

**Oxigenação por oxímetro de pulso** no relógio: tem valor de tendência em contextos específicos, e não tem acurácia para diagnóstico. Não use para avaliar apneia, e não tranquilize ninguém com base nela — quem tem suspeita de apneia faz rastreio e polissonografia, como a gente montou no Módulo 4.

**Temperatura cutânea**, que vários aparelhos passaram a estimar: mede pele, não mede temperatura central. Como tendência relativa pode sinalizar alguma coisa; como número absoluto, não.

E um aviso que vale por todos: aparelho de consumo **não é dispositivo diagnóstico**, mesmo quando tem função aprovada para algo específico. A notificação de ritmo irregular de alguns relógios, por exemplo, tem valor de alerta e não de diagnóstico — ela manda a pessoa procurar avaliação, e é isso que ela deve fazer. Nem ignorar, nem tratar pela tela.

---

📊 **[SLIDE 5 DE 6]**
*Visual: uma tabela de cinco métricas com uma coluna de "serve para" e outra de "não serve para".*
*Teleprompter: (tom de síntese)*

Consolidando, porque isto é o que o aluno vai levar para a segunda-feira.

**Passos:** bom. Use para volume de atividade diária e tendência.

**Frequência cardíaca em repouso e em intensidade estável:** bom. Use — e a frequência cardíaca de repouso, medida do mesmo jeito todo dia, é uma das melhores variáveis gratuitas que existem.

**Frequência cardíaca em alta intensidade e com movimento de punho:** fraco. Use cinta.

**Duração e regularidade do sono:** bom. Use, e use bastante.

**Estágios de sono:** fraco. Não use clinicamente.

**Gasto energético:** ruim. Não use para decisão alimentar.

**Oxigenação e temperatura:** tendência, no máximo. Não diagnostica nada.

**Índices proprietários** — recuperação, prontidão, carga, estresse, idade corporal: não auditáveis. Trate como opinião de software.

E três regras de uso que valem para todos eles.

**Um: compare a pessoa com ela mesma, sempre no mesmo aparelho.** Quase todas essas métricas têm viés sistemático — erram consistentemente para o mesmo lado. Viés sistemático arruína comparação entre pessoas e **não arruína** acompanhamento da mesma pessoa.

**Dois: trocar de aparelho zera a série.** Quando o paciente muda de marca, a série antiga não continua; ela recomeça.

**Três: atualização de software muda algoritmo sem aviso.** Um degrau na série sem nada ter mudado na vida da pessoa pode ser a versão nova do aplicativo.

E uma quarta, de privacidade, que num curso de pós-graduação precisa estar dita: esses dados são de saúde, ficam em servidor de empresa privada, frequentemente fora do país, sob termos de uso que quase ninguém leu. Se você vai pedir ao paciente que compartilhe a conta dele com você, isso merece uma conversa explícita — e o registro clínico deve ficar no seu prontuário, não na plataforma do fabricante.

---

📊 **[SLIDE 6 DE 6]**
*Visual: duas pessoas olhando a mesma tela de relógio, com uma folha de papel entre elas.*
*Teleprompter: (fecha com o caso e a conduta)*

Como conduzir isso com quem chega cheio de dados.

Não descarte. O paciente que traz seis meses de dados está te oferecendo trabalho voluntário que ninguém mais fez — e desqualificar aquilo custa a relação e custa a informação.

O que eu faço é separar a tela em três pilhas, na frente da pessoa. **Isto aqui é medido e eu vou usar.** **Isto é estimado e eu vou olhar como tendência.** **E isto aqui eu não vou usar para decidir, e vou te explicar por quê.**

Leva três minutos e muda a relação da pessoa com o próprio aparelho para sempre.

Carla, 45 anos, gerente de RH, caminha e faz musculação, queria emagrecer e estava frustrada havia oito meses.

Ela usava o relógio com disciplina. Fechava as metas todo dia, e comia conforme o gasto que o aparelho mostrava — em média oitocentas calorias diárias de exercício, segundo a tela.

O peso não mudava.

Eu não discuti a dieta dela no primeiro momento. Perguntei o que o aparelho media e o que ele calculava — e a gente foi junto ver de onde vinha aquele número.

Quando ficou claro que o gasto era uma estimativa com margem larga, e que a musculação dela provavelmente estava sendo bastante superestimada, o quadro inteiro se explicou sem culpa e sem sermão.

E aí tinha o outro lado, que era o que interessava de verdade. Os dados **bons** do relógio dela contavam uma história que ninguém tinha lido: ela dormia em média cinco horas e quarenta, com horário de deitar variando três horas entre semana e fim de semana. E a frequência cardíaca de repouso dela tinha subido quatro batimentos nos últimos quatro meses.

O aparelho dela já tinha a informação certa. Ela só estava olhando a parte errada da tela.

A conduta saiu dali: parar de comer por cima do número de calorias, encaminhamento nutricional com dado real de ingestão, e sono como primeira intervenção — que é a ordem de prioridade que a gente montou no fim do Módulo 4.

E repara que eu não tirei o relógio dela. Tirar teria sido fácil, teria parecido rigoroso, e teria jogado fora oito meses de dado bom junto com o ruim.

O trabalho aqui quase nunca é retirar tecnologia. É **redistribuir a confiança** dentro dela.

Na próxima aula a gente sai da tecnologia e vai para o campo: testes de limiar e de potência que você aplica com cronômetro, pista e um pouco de método — e que, bem feitos, valem mais do que a maior parte do que a gente viu hoje.

---

## Referências

1. Fuller D, Colwell E, Low J, et al. Reliability and validity of commercially available wearable devices for measuring steps, energy expenditure, and heart rate: systematic review. *JMIR Mhealth Uhealth.* 2020;8(9):e18694. PMID: 32897239
2. Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with polysomnography. *Sleep.* 2021;44(5):zsaa291. PMID: 33378539
3. Buchheit M. Monitoring training status with HR measures: do all roads lead to Rome? *Front Physiol.* 2014;5:73. doi:10.3389/fphys.2014.00073
4. Baron KG, Abbott S, Jao N, Manalo N, Mullen R. Orthosomnia: are some patients taking the quantified self too far? *J Clin Sleep Med.* 2017;13(2):351-354.
5. Hopkins WG. Measures of reliability in sports medicine and science. *Sports Med.* 2000;30(1):1-15. PMID: 10907753

---

## Roteiro Gamma.app

**Slide 1** — A pergunta certa não é "relógio é confiável?"
· Um relógio não é uma medida: é uma caixa com dois ou três sensores e uma dúzia de métricas
· O mesmo aparelho é ótimo para uma coisa e péssimo para outra, na mesma tela
· Sensores reais: acelerômetro, óptico de pulso (fotopletismografia) e GPS
· Todo o resto é cálculo — **"isso foi medido ou calculado?"**
· Sensor bom com interpretação ruim faz o mesmo dano que exame sem pergunta
Visual: relógio com cinco métricas, cada uma com uma nota diferente.

**Slide 2** — Passos e frequência cardíaca
· Fuller 2020: passos são acurados, com variação entre fabricantes
· Erra em velocidade muito baixa e conta movimento de braço sem deslocamento
· FC em repouso e intensidade estável: vai bem
· FC em alta intensidade e com movimento de punho: **cai muito** — e pode travar na cadência
· Pele escura e tatuagem interferem na leitura óptica
· Decisão que depende de FC precisa: **cinta peitoral**
Visual: passo contado certo x carrinho contado errado.

**Slide 3** — Sono: duas metades diferentes
· Chinoy 2021, sete aparelhos contra polissonografia em 34 adultos
· **Sono x vigília e tempo total: razoável.** **Estágios: fraco e variável**
· É o oposto de como a tela apresenta: o gráfico colorido é a parte que menos se sustenta
· O relógio não mede EEG, movimento ocular nem tônus — infere de movimento e pulso
· Use duração e regularidade. Não trate "pouco sono profundo"
· O melhor uso não é o número: é mostrar a janela de oportunidade de sono
Visual: hipnograma real x hipnograma do relógio.

**Slide 4** — Gasto energético e o resto
· É a pior métrica do conjunto, com erro grande e inconsistente
· O aparelho não mede calor nem troca gasosa — estima por equação populacional
· O dano é direto: come por cima de um número errado, ou restringe por causa dele
· **Não use gasto energético para decisão alimentar**
· Oximetria de pulso: tendência, não diagnostica apneia. Temperatura: pele, não central
Visual: prato ao lado de "620 kcal" com margem de erro larga.

**Slide 5** — A tabela que vai para a segunda-feira
· Passos ✔ · FC em repouso e estável ✔ · duração e regularidade do sono ✔
· FC em alta intensidade ✘ · estágios de sono ✘ · gasto energético ✘
· Índices proprietários: opinião de software, não auditáveis
· Viés sistemático não atrapalha acompanhar a mesma pessoa — atrapalha comparar pessoas
· **Trocar de aparelho zera a série**; atualização de software muda algoritmo sem aviso
Visual: tabela de cinco métricas, serve para x não serve para.

**Slide 6** — Carla, 45 anos
· Separe a tela em três pilhas na frente da pessoa: medido · estimado · não usar
· Comia por cima de ~800 kcal diárias de gasto estimado; o peso não mudava
· Os dados **bons** do relógio contavam outra história: 5h40 de sono, horário variando 3h
· E a FC de repouso tinha subido quatro batimentos em quatro meses
· O aparelho já tinha a informação certa — ela olhava a parte errada da tela
Visual: duas pessoas olhando a mesma tela, com uma folha entre elas.
