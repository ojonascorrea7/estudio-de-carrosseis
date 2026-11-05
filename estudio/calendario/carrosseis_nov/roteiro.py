"""Roteiro dos 24 carrosséis de 07 a 30/11/2026: capa (já pronta em capas_nov/capas) + 5 slides + CTA.
Campos por slide: t = título, x = texto. Extras por família:
  print: chat=[(quem, msg)] com quem em ("ele", "eu")
  tirinha: expr (expressão do personagem), cena (cenário)
Marcação: **x** = destaque."""

R = {}

R["07"] = dict(kw="VOLUME", fam="foto", cta=("Constância que não depende de você.", "a cadência de follow-up pronta"),
    slides=[
        dict(t="O episódio", x="Em outubro, o Alfredo Soares gravou com o Toguro na Mansão Maromba. O vídeo passou de **590 mil views** no YouTube."),
        dict(t="A estratégia", x="Uma das lições do episódio: em vez de caçar o vídeo perfeito, **postar muito**, errar e ajustar."),
        dict(t="O que o feed não mostra", x="Antes do sucesso vieram anos de constância. Quem só vê o post que viralizou acha que foi sorte."),
        dict(t="Na venda é igual", x="Ninguém fecha com a mensagem perfeita. Fecha quem **aparece de novo**: dia 1, dia 3, dia 7."),
        dict(t="Constância no automático", x="No CRM o follow-up roda sozinho. Você mantém o volume até nos dias em que não dá tempo."),
    ],
    legenda="O Toguro não caça viral. Ele posta todo dia.\n\nNo episódio com o Alfredo Soares (mais de 590 mil views no YouTube), uma lição ficou clara: volume e constância batem o post perfeito.\n\nNa venda é a mesma coisa. Quem fecha não é quem manda a mensagem mais bonita, é quem aparece de novo.\n\nComenta VOLUME que eu te mando a cadência de follow-up pronta para usar. Dá para testar a SuaMarca 14 dias grátis.\n\nImagem: canal Alfredo Soares / YouTube.")

R["08"] = dict(kw="CONTRATO", fam="foto", cta=("O que não está registrado não existe.", "o modelo de registro de proposta e combinado"),
    slides=[
        dict(t="1961", x="Ray Kroc compra a parte dos irmãos McDonald por **US$ 2,7 milhões**."),
        dict(t="O combinado de boca", x="Segundo os irmãos, ficou acertado 1% de royalties para sempre. Só no **aperto de mão**, sem contrato."),
        dict(t="O que aconteceu", x="Segundo eles, esse 1% nunca foi pago. E ainda perderam o direito de usar o próprio nome na loja original."),
        dict(t="E no seu negócio?", x="Desconto prometido no WhatsApp, prazo combinado por áudio, proposta enviada e esquecida. Se não está registrado, **é aperto de mão**."),
        dict(t="Tudo no histórico", x="No CRM, cada conversa, proposta e combinado fica no histórico do cliente. Qualquer pessoa do time sabe o que foi prometido."),
    ],
    legenda="O aperto de mão que custou um império.\n\nSegundo os irmãos McDonald, o combinado com Ray Kroc era 1% de royalties para sempre, fechado só de boca. Eles dizem que nunca receberam.\n\nNo seu negócio, quantos combinados estão só no áudio do WhatsApp?\n\nComenta CONTRATO que eu te mando o modelo para registrar proposta e combinado no CRM. 14 dias grátis para testar a SuaMarca.\n\nParte 2 da série Fome de Poder. Foto: Marykdan, Wikimedia Commons (CC BY-SA 4.0).")

R["09"] = dict(kw="HUMANO", fam="glass", cta=("IA + gente, no mesmo atendimento.", "como montar IA + humano no seu WhatsApp"),
    slides=[
        dict(t="O que diz o decreto", x="O Decreto 13.135/2026 vale desde 2/11 para empresas reguladas pelo governo federal: telefonia, energia, aviação, planos de saúde e serviços financeiros digitais."),
        dict(t="Humano das 8h às 20h", x="Atendente de verdade todos os dias nesse horário. Um canal digital precisa funcionar 24h, e esse pode ser **automatizado**."),
        dict(t="A IA continua", x="O decreto permite IA, desde que o cliente consiga chegar em uma pessoa. A opção de falar com humano tem que estar em **todos os menus**."),
        dict(t="Mesmo se não for obrigado", x="Sua empresa pode não estar na lista. Mas o cliente vai se acostumar. Robô que prende o cliente num menu vai virar defeito."),
        dict(t="O modelo certo", x="A IA responde na hora, resolve o simples e passa para uma pessoa quando precisa, **com todo o histórico** da conversa."),
    ],
    legenda="Desde 2 de novembro, empresa grande é obrigada a ter humano no atendimento.\n\nO Decreto 13.135/2026 exige atendente das 8h às 20h, todos os dias, para empresas reguladas pelo governo federal. A IA continua permitida, desde que o cliente consiga falar com uma pessoa.\n\nMesmo que a regra não valha para você, o cliente vai passar a esperar isso.\n\nComenta HUMANO que eu te mostro como montar IA + humano no seu WhatsApp. 14 dias grátis na SuaMarca.\n\nFontes: Conjur, Atlas Público e MobileTime (out/2026).")

R["10"] = dict(kw="ONZE", fam="tweet", cta=("As 3 mensagens, prontas para disparar.", "as 3 mensagens prontas do 11.11"),
    slides=[
        dict(t="O que é o 11.11", x="A data nasceu na China e virou dia de promoção no e-commerce brasileiro. A projeção é de **R$ 3,17 bilhões** em um dia (Confi/Neotrust)."),
        dict(t="Mensagem 1 · hoje", x="\"Amanhã tem oferta só para quem já é cliente. Quer que eu te avise primeiro?\"\n\nQuem responder já entra numa lista."),
        dict(t="Mensagem 2 · amanhã cedo", x="\"Começou. Separei [produto] para você com [x]% até meia-noite.\"\n\nPersonalizada pelo que a pessoa **já comprou**."),
        dict(t="Mensagem 3 · fim da tarde", x="\"Faltam 6 horas. Ainda dá tempo.\"\n\nSó para quem abriu e **não comprou**."),
        dict(t="Sem bloquear o número", x="Disparo só pela API oficial, só para quem autorizou e com opção de sair. Em volume, **número pessoal toma bloqueio**."),
    ],
    legenda="Amanhã é 11.11.\n\nA projeção é de R$ 3,17 bilhões em vendas online em um dia só (Confi/Neotrust). E a maior parte das empresas ainda não mandou nenhuma mensagem para a própria base.\n\nNo carrossel: as 3 mensagens para mandar hoje, amanhã cedo e amanhã à tarde, sem bloquear o seu número.\n\nComenta ONZE que eu te mando as 3 prontas. 14 dias grátis para testar a SuaMarca.")

R["11"] = dict(kw="BRINDE", fam="tirinha", cta=("Follow-up é a sua coqueteleira.", "a régua de follow-up do dia 1, 3 e 7"),
    slides=[
        dict(t="", x="No episódio do Alfredo com o Toguro, a conta foi assim: um **clique** de anúncio custa uns R$ 4 e dura segundos.", expr="pensando", cena="episodio"),
        dict(t="", x="Uma **coqueteleira de brinde** fica um ano na cozinha do cliente. Ele vê a marca todo dia.", expr="sorriso", cena="brinde"),
        dict(t="", x="Agora olha o seu lead: você pagou o clique, ele chamou… e **ninguém** falou mais com ele.", expr="bravo", cena="whatsapp_caos"),
        dict(t="", x="O follow-up é a sua coqueteleira: faz o cliente **lembrar de você** depois do primeiro contato.", expr="apontando", cena="quadro"),
        dict(t="", x="Dia 1, dia 3, dia 7.\nMensagem automática,\nsem você **precisar lembrar**.", expr="risada", cena="crm"),
    ],
    legenda="Você paga R$ 4 num clique e esquece o lead em 2 dias.\n\nNo episódio do Alfredo Soares com o Toguro, a conta ficou clara: o clique dura segundos, a coqueteleira de brinde fica um ano na cozinha do cliente.\n\nO seu follow-up é a sua coqueteleira.\n\nComenta BRINDE que eu te mando a régua de follow-up do dia 1, 3 e 7. 14 dias grátis na SuaMarca.")

R["12"] = dict(kw="RECOMPRA", fam="noticia", cta=("Quem vende de novo, ganha a Black.", "a régua de recompra pronta"),
    slides=[
        dict(t="Os números", x="A projeção da Confi/Neotrust para a Black: **R$ 13,3 bi** no e-commerce, mais pedidos e ticket médio caindo de R$ 309,70 para **R$ 268,20**."),
        dict(t="O que isso quer dizer", x="O cliente vai comprar mais vezes e gastar menos em cada compra. A venda única vai render **menos**."),
        dict(t="Quem ganha", x="Quem vende de novo para o mesmo cliente. Recompra custa muito menos, porque você **não paga o anúncio** outra vez."),
        dict(t="Como fazer", x="Saber quem comprou, o quê e quando. Com isso, a oferta certa chega **na hora em que o produto acaba**."),
        dict(t="Exemplo", x="Comprou um creme de 30 dias? No dia 25, mensagem automática: \"o seu está acabando, separei um com 10% para você\"."),
    ],
    legenda="Na Black deste ano o cliente vai gastar menos por compra.\n\nA projeção da Confi/Neotrust é de ticket médio caindo de R$ 309,70 para R$ 268,20. Mais pedidos, de valor menor.\n\nQuem ganha não é quem vende uma vez. É quem faz o cliente voltar.\n\nComenta RECOMPRA que eu te mando a régua de recompra pronta. 14 dias grátis na SuaMarca.")

R["13"] = dict(kw="VALOR", fam="print", cta=("A resposta que fecha, pronta para usar.", "as respostas prontas para \"qual valor?\""),
    slides=[
        dict(t="❌ Resposta 1: o preço seco", chat=[("ele", "boa tarde, qual valor?"), ("eu", "R$ 350")], x="Sem contexto, o preço vira a **única coisa** para comparar."),
        dict(t="❌ Resposta 2: o textão", chat=[("ele", "qual valor?"), ("eu", "Olá! Tudo bem? Somos uma empresa com 10 anos de mercado, trabalhamos com qualidade e…")], x="Ninguém lê. O cliente perguntou **uma coisa só**."),
        dict(t="❌ Resposta 3: o passo a mais", chat=[("ele", "qual valor?"), ("eu", "me passa seu e-mail que eu mando a tabela")], x="Cada passo extra é uma chance de ele **desistir**."),
        dict(t="✅ A que fecha", chat=[("ele", "qual valor?"), ("eu", "Fica R$ 350 😊 Pra eu te indicar o certo: é pra você ou pra presente?")], x="Preço + **uma pergunta**. Você responde e já abre a conversa."),
        dict(t="E se ele sumir?", chat=[("eu", "Conseguiu ver? Separei a opção mais pedida pra você 👇")], x="Follow-up automático no dia seguinte. Sem você **precisar lembrar**."),
    ],
    legenda="Cliente mandou \"qual valor?\". O que você responde decide a venda.\n\nNo carrossel: 3 respostas que matam a venda e 1 que fecha, com o exemplo pronto.\n\nComenta VALOR que eu te mando as respostas prontas para copiar. 14 dias grátis na SuaMarca.")

R["14"] = dict(kw="NUMERO", fam="tirinha", cta=("Saiba o seu número sem abrir planilha.", "o painel de vendas por canal"),
    slides=[
        dict(t="", x="No episódio com o Alfredo, uma crítica ao Toguro: ninguém sabe **quanto** a Mansão Maromba vende.", expr="pensando", cena="episodio"),
        dict(t="", x="E é o número que faz uma marca ou um investidor **apostar** em você.", expr="serio", cena="quadro"),
        dict(t="", x="Agora você: quanto vendeu mês passado? E de **qual canal** veio cada venda?", expr="desconfiado", cena="planilhas"),
        dict(t="", x="Se a resposta está em 3 planilhas e no seu WhatsApp, você também **não sabe** o seu número.", expr="bravo", cena="whatsapp_caos"),
        dict(t="", x="No CRM, cada venda entra com a origem: Instagram, Google, indicação.\nO painel **fecha o mês sozinho**.", expr="sorriso", cena="crm"),
    ],
    legenda="Quanto você vendeu mês passado? E de qual canal?\n\nNo episódio do Alfredo Soares com o Toguro, uma das críticas foi essa: ninguém sabe quanto a Mansão Maromba vende. E é o número que faz alguém apostar em você.\n\nSe para responder você precisa abrir 3 planilhas, você também não sabe.\n\nComenta NUMERO que eu te mostro o painel de vendas por canal. 14 dias grátis na SuaMarca.")

R["15"] = dict(kw="FILA", fam="glass", cta=("Ninguém fica na fila na sua Black.", "como ligar a IA no WhatsApp antes da Black"),
    slides=[
        dict(t="R$ 13,3 bi", x="É a projeção da Confi/Neotrust para o e-commerce entre 26 e 29 de novembro. Boa parte passa por uma **conversa** antes da compra."),
        dict(t="O pico", x="Na Black, as mensagens chegam à noite, no fim de semana e **todas ao mesmo tempo**. É quando você menos consegue responder."),
        dict(t="Quem espera, vai embora", x="Quem não recebe resposta não espera você acordar. **Abre a próxima loja**."),
        dict(t="O que resolve", x="IA no WhatsApp responde em segundos: preço, estoque, prazo e link de pagamento. Você entra **só no que precisa** de gente."),
        dict(t="Teste antes", x="Liga a IA agora, testa por duas semanas e chega na Black com **tudo rodando**."),
    ],
    legenda="R$ 13,3 bilhões em 4 dias de Black Friday (projeção Confi/Neotrust).\n\nQuanto disso vai ficar sem resposta no seu WhatsApp às 22h47?\n\nNa Black as mensagens chegam todas ao mesmo tempo, e quem espera vai embora.\n\nComenta FILA que eu te mostro como ligar a IA no WhatsApp antes da Black. 14 dias grátis na SuaMarca.")

R["16"] = dict(kw="PROCESSO", fam="foto", cta=("Processo de empresa grande, no bolso do pequeno.", "o kit de processo para pequeno negócio"),
    slides=[
        dict(t="Os números", x="Levantamento divulgado no Dia das Favelas (04/11) estima **R$ 167 bilhões** por ano de potencial de consumo nesses territórios."),
        dict(t="Quem empreende", x="**Mais de 60%** dos negócios analisados são liderados por mulheres. Salão, marmita, conserto de celular, confeitaria."),
        dict(t="O desafio", x="Negócio pequeno costuma ter um WhatsApp só, a dona respondendo tudo e **nenhum registro** de quem já comprou."),
        dict(t="Processo não é luxo", x="Uma lista de clientes, uma resposta automática e um lembrete de retorno **já mudam** o faturamento."),
        dict(t="Quanto custa", x="Ferramenta de empresa grande hoje cabe no bolso do pequeno: a ferramenta certa custa **menos que um funcionário**."),
    ],
    legenda="R$ 167 bilhões por ano. E 6 em cada 10 negócios são liderados por mulheres.\n\nO levantamento divulgado no Dia das Favelas mostra a força econômica desses territórios. O que falta para muito pequeno negócio crescer não é cliente: é processo.\n\nComenta PROCESSO que eu te mando o kit de processo para pequeno negócio. Dá para testar 14 dias grátis.\n\nFoto: chensiyuan, Wikimedia Commons (CC BY-SA 4.0).")

R["17"] = dict(kw="VIEWS", fam="noticia", cta=("Saiba qual post vira venda.", "como medir a origem de cada venda"),
    slides=[
        dict(t="O que aconteceu", x="Em fevereiro, a Cimed anunciou o Toguro como head de comunicação e marketing. Na primeira semana, comemorou **2 bilhões de visualizações**."),
        dict(t="A polêmica", x="Gente de marketing criticou o currículo dele no LinkedIn. O João Adibe, dono da Cimed, defendeu: \"não tem curso para aprender isso\"."),
        dict(t="A pergunta certa", x="Uma análise da YOUPIX resumiu: **view não prova influência**. A dúvida é quantas dessas views viraram venda."),
        dict(t="No seu negócio", x="Post com muita view e caixa vazio é o mesmo problema em escala menor. **Alcance sem conversão é custo**."),
        dict(t="Como medir", x="Cada lead entra no CRM com a origem. No fim do mês você sabe qual post, anúncio ou parceria trouxe **venda de verdade**."),
    ],
    legenda="Toguro virou head de marketing da Cimed e a marca comemorou 2 bilhões de views.\n\nA pergunta que ninguém respondeu: quantas viraram venda?\n\nView não prova influência. No seu negócio também não: alcance sem conversão é custo.\n\nComenta VIEWS que eu te mostro como medir a origem de cada venda. 14 dias grátis na SuaMarca.\n\nFontes: InfoMoney, CidadeMarketing e YOUPIX (2026).")

R["18"] = dict(kw="SUMIU", fam="print", cta=("As 7 mensagens no automático.", "as 7 mensagens de follow-up prontas"),
    slides=[
        dict(t="Mensagem 1 · dia seguinte", chat=[("eu", "Oi Fernanda, conseguiu ver o orçamento? Se quiser, ajusto alguma coisa.")], x="Leve, **sem pressão**."),
        dict(t="Mensagem 2 · dia 3", chat=[("eu", "Separei um caso parecido com o seu, olha como ficou 👇")], x="**Prova social** ajuda a decidir."),
        dict(t="Mensagem 3 · dia 5", chat=[("eu", "Consigo manter esse valor até sexta. Depois a tabela muda.")], x="Prazo **real**, nunca inventado."),
        dict(t="Mensagens 4 e 5 · objeção", chat=[("eu", "Ficou dúvida no pagamento? Dá para dividir em até 10x."), ("eu", "Se o problema for o momento, me fala que te procuro mês que vem.")], x="Tire o motivo do **não** da frente."),
        dict(t="Mensagens 6 e 7 · despedida", chat=[("eu", "Vou parar de te mandar mensagem para não incomodar 🙂"), ("eu", "Se mudar de ideia, é só responder aqui.")], x="A despedida costuma trazer resposta de quem estava **só adiando**."),
    ],
    legenda="Cliente sumiu depois do preço?\n\nNo carrossel: 7 mensagens de follow-up, do dia seguinte até a despedida, prontas para copiar.\n\nE melhor ainda: no CRM elas saem sozinhas, no dia certo.\n\nComenta SUMIU que eu te mando as 7 prontas. 14 dias grátis na SuaMarca.")

R["19"] = dict(kw="BOMDIA", fam="tweet", cta=("A primeira resposta que já vende.", "o modelo de primeira resposta"),
    slides=[
        dict(t="", x="O cliente mandou \"bom dia, tem disponível?\" e recebeu \"bom dia! tudo bem?\".\n\nAgora ele precisa responder **de novo** para ter a resposta."),
        dict(t="", x="Cada ida e volta é uma chance de ele sair da conversa e **chamar outra loja**."),
        dict(t="", x="O certo: cumprimento + resposta + próximo passo **na mesma mensagem**.\n\n\"Bom dia! Tem sim, no M e no G. Quer que eu separe?\""),
        dict(t="", x="Não é ser frio.\n\nÉ **respeitar o tempo** de quem chamou."),
        dict(t="", x="Melhor ainda: a IA já responde assim, em segundos, **até de madrugada**."),
    ],
    legenda="Pare de dar bom dia para cliente no WhatsApp.\n\nCalma: o problema não é o bom dia, é ele vir sozinho. Cumprimento, resposta e próximo passo na mesma mensagem.\n\nComenta BOMDIA que eu te mando o modelo de primeira resposta. 14 dias grátis na SuaMarca.")

R["20"] = dict(kw="FERIADO", fam="tirinha", cta=("Sua empresa descansa. O atendimento, não.", "como deixar a IA atendendo no feriado"),
    slides=[
        dict(t="", x="Feriado chegando. A loja fecha, o time folga…\ne o **celular**?", expr="pensando", cena="feriado"),
        dict(t="", x="O cliente não sabe que é feriado. Ele chama, espera e **compra de quem respondeu**.", expr="bravo", cena="whatsapp_caos"),
        dict(t="", x="A placa de **fechado** na porta não aparece no WhatsApp.", expr="desconfiado", cena="porta_fechada"),
        dict(t="", x="Com a IA, o atendimento continua: responde, tira dúvida e **agenda** para o dia seguinte.", expr="sorriso", cena="quarto"),
        dict(t="", x="Você aproveita o feriado.\nNa volta, as conversas estão **organizadas** no CRM.", expr="risada", cena="sabado"),
    ],
    legenda="Feriado: sua empresa fecha. Seu cliente, não.\n\nEle chama, espera e compra de quem respondeu. A placa de fechado na porta não aparece no WhatsApp.\n\nComenta FERIADO que eu te mostro como deixar a IA atendendo no feriado. 14 dias grátis na SuaMarca.")

R["21"] = dict(kw="CARA", fam="glass", cta=("Você aparece. A IA responde.", "como a IA responde direct e WhatsApp por você"),
    slides=[
        dict(t="O que ele disse", x="Em entrevista à Forbes, o João Adibe, dono da Cimed, disse que o brasileiro gosta de **comprar de quem bota a cara**."),
        dict(t="E funciona", x="Dono que aparece gera confiança. As pessoas compram de gente, **não de logo**."),
        dict(t="O efeito colateral", x="Quem bota a cara recebe mensagem. Muita. Direct, WhatsApp e comentário, **tudo ao mesmo tempo**."),
        dict(t="Onde a venda morre", x="A pessoa vê o seu vídeo, chama no direct e espera. Se você está gravando o próximo, **ela esfria**."),
        dict(t="A divisão certa", x="Você aparece. A IA responde direct e WhatsApp, qualifica e só passa para você **quem está pronto** para comprar."),
    ],
    legenda="\"O brasileiro compra de quem bota a cara.\" Concordo.\n\nMas quem bota a cara recebe 300 DMs. E é no direct sem resposta que a venda morre.\n\nComenta CARA que eu te mostro como a IA responde direct e WhatsApp por você. 14 dias grátis na SuaMarca.\n\nFrase de João Adibe à Forbes (2026).")

R["22"] = dict(kw="RAPIDO", fam="tweet", cta=("Resposta em segundos, até no pico.", "como responder em menos de 5 minutos"),
    slides=[
        dict(t="", x="Na Black, o cliente pergunta a mesma coisa em **3 lojas** ao mesmo tempo."),
        dict(t="", x="A primeira que responde com preço, prazo e link costuma levar.\n\nAs outras recebem \"já comprei, obrigado\"."),
        dict(t="", x="Responder em 5 minutos no pico só é possível com **automação**. Ninguém tem gente para isso."),
        dict(t="", x="Teste hoje: mande uma mensagem para o seu próprio WhatsApp comercial às 22h e **conte quanto tempo** leva a resposta."),
        dict(t="", x="Se passou de 5 minutos, ainda dá tempo de ligar a IA **antes da Black**."),
    ],
    legenda="Na Black, seu concorrente vai responder em 5 minutos. E você?\n\nO cliente pergunta em 3 lojas ao mesmo tempo, e quem responde primeiro costuma levar.\n\nComenta RAPIDO que eu te mostro como responder em menos de 5 minutos. 14 dias grátis na SuaMarca.")

R["23"] = dict(kw="CALENDARIO", fam="print", cta=("As 4 mensagens programadas, sem bloqueio.", "as 4 mensagens da Black prontas"),
    slides=[
        dict(t="Quinta 26 · véspera", chat=[("eu", "A Lista VIP abriu. Amanhã às 8h você recebe as ofertas antes de todo mundo.")], x="**Aquece** quem já é cliente."),
        dict(t="Sexta 27 · o dia", chat=[("eu", "Começou! Seu cupom BLACK15 vale até meia-noite 👇")], x="Curta, **com prazo** e link."),
        dict(t="Sábado 28 · carrinho", chat=[("eu", "Vi que ficou no carrinho. Separei pra você até hoje.")], x="Só para quem **clicou e não comprou**."),
        dict(t="Domingo 29 · última chamada", chat=[("eu", "Últimas horas. Amanhã volta o preço normal.")], x="Escassez **real**."),
        dict(t="Como programar", x="Mensagens programadas e segmentadas no CRM, pela **API oficial**, para não bloquear o número."),
    ],
    legenda="O que mandar em cada dia da Black.\n\nQuinta, sexta, sábado e domingo: 4 mensagens, cada uma com um objetivo, já programadas.\n\nComenta CALENDARIO que eu te mando as 4 prontas. 14 dias grátis na SuaMarca.")

R["24"] = dict(kw="VIRAL", fam="foto", cta=("Transforme viral em cliente.", "o kit de respostas prontas para o pico"),
    slides=[
        dict(t="A ideia", x="Um vídeo com mais de 670 mil views mostrou uma pastelaria comum que viralizou com uma ideia simples: **dividir a massa** do pastel ao meio."),
        dict(t="O que vem depois", x="Viralizar traz fila, comentário e mensagem. Centenas de \"qual o endereço?\", \"entrega?\", **\"até que horas?\"**."),
        dict(t="O risco", x="Se ninguém responde, a onda passa e vira só view. **O viral dura poucos dias**."),
        dict(t="Preparado para o pico", x="Respostas prontas para as perguntas que mais chegam, IA respondendo 24h e **todo contato salvo** para voltar a falar depois."),
        dict(t="A lição", x="Viralizar é sorte.\nTransformar viral em cliente é **processo**."),
    ],
    legenda="Uma pastelaria viralizou só por cortar o pastel ao meio.\n\nO difícil veio depois: atender todo mundo que chamou. O viral dura poucos dias. O contato salvo dura para sempre.\n\nComenta VIRAL que eu te mando o kit de respostas prontas para o pico. 14 dias grátis na SuaMarca.\n\nFoto: Mike Peel, Wikimedia Commons (CC BY-SA 4.0).")

R["25"] = dict(kw="VIP", fam="print", cta=("Sua Lista VIP montada até quinta.", "o passo a passo da Lista VIP"),
    slides=[
        dict(t="Por que lista VIP", x="Quem entra antes **já decidiu comprar**. Você só precisa avisar na hora certa."),
        dict(t="Passo 1 · o convite", chat=[("eu", "Quer receber as ofertas da Black antes de todo mundo? Responde EU QUERO 🙋")], x="Mande para a sua base."),
        dict(t="Passo 2 · a etiqueta", x="Quem respondeu ganha a etiqueta **VIP** no CRM automaticamente. Sem planilha."),
        dict(t="Passo 3 · o aviso", chat=[("eu", "🔒 Lista VIP: as ofertas abrem hoje às 20h, uma hora antes do público.")], x="Exclusividade **de verdade**."),
        dict(t="Passo 4 · o lembrete", chat=[("eu", "Abriu! O link é só seu até meia-noite 👇")], x="E quem não abriu recebe **mais um aviso**."),
    ],
    legenda="Lista VIP: quem entra antes compra primeiro.\n\n4 passos para montar a sua até quinta: convite, etiqueta, aviso e lembrete.\n\nComenta VIP que eu te mando o passo a passo. 14 dias grátis na SuaMarca.")

R["26"] = dict(kw="CHECKLIST", fam="noticia", cta=("Os 10 itens já configurados.", "o checklist completo em PDF"),
    slides=[
        dict(t="Itens 1 e 2", x="**1.** Resposta automática fora do horário.\n**2.** Preço e estoque atualizados no catálogo."),
        dict(t="Itens 3 e 4", x="**3.** Link de pagamento pronto para colar.\n**4.** Respostas salvas para frete, prazo e troca."),
        dict(t="Itens 5 e 6", x="**5.** Lista de clientes separada por interesse.\n**6.** Mensagem da Black programada pela API oficial."),
        dict(t="Itens 7 e 8", x="**7.** Alguém de plantão para o que a IA não resolve.\n**8.** Etiqueta para quem perguntou e não comprou."),
        dict(t="Itens 9 e 10", x="**9.** Mensagem de pós-venda pronta.\n**10.** Follow-up do carrinho abandonado no sábado."),
    ],
    legenda="Amanhã é Black Friday. Confere hoje, porque amanhã não vai dar tempo.\n\nO checklist de 10 itens do seu atendimento, do automático ao pós-venda. Salva esse post.\n\nComenta CHECKLIST que eu te mando o checklist completo. 14 dias grátis na SuaMarca.")

R["27"] = dict(kw="BLACK", fam="glass", cta=("Black Friday SuaMarca.", "o link da oferta"),
    slides=[
        dict(t="O que tem na SuaMarca", x="CRM com funil de vendas, WhatsApp, Instagram e site **num lugar só**, com agentes de IA atendendo 24h."),
        dict(t="15% OFF", x="Em **qualquer plano**, na Black Friday."),
        dict(t="14 dias grátis", x="Para **testar antes** de pagar."),
        dict(t="Plano anual", x="**2 meses grátis** já inclusos."),
        dict(t="Até quando", x="Válido até **30/11/2026** ou enquanto durarem as vagas."),
    ],
    legenda="Hoje é Black Friday. E a SuaMarca também entrou.\n\n15% OFF em qualquer plano, 14 dias grátis para testar e 2 meses grátis no plano anual. Agentes de IA inclusos.\n\nVálido até 30/11 ou enquanto durarem as vagas.\n\nComenta BLACK que eu te mando o link.")

R["28"] = dict(kw="AGENTE", fam="tirinha", cta=("Um agente de IA no seu WhatsApp.", "como configurar o agente de IA"),
    slides=[
        dict(t="", x="Sábado de Black:\n**500 mensagens** desde as 8h.", expr="bravo", cena="whatsapp_caos"),
        dict(t="", x="Contratar alguém só para o fim de semana? Treinar em um dia? **Não dá tempo.**", expr="pensando", cena="dono_faz_tudo"),
        dict(t="", x="O agente de IA aprende com as suas respostas: **preço, prazo, estoque e troca**.", expr="apontando", cena="crm"),
        dict(t="", x="Ele responde todas **ao mesmo tempo** e manda o link de pagamento.", expr="sorriso", cena="sabado"),
        dict(t="", x="O que precisa de gente vem para você,\njá com o **histórico**.", expr="serio", cena="quarto"),
    ],
    legenda="Como responder 500 mensagens num sábado sem contratar ninguém?\n\nCom um agente de IA que aprende com as suas respostas e atende todo mundo ao mesmo tempo. O que precisa de gente vem para você.\n\nComenta AGENTE que eu te mostro como configurar. 14 dias grátis na SuaMarca.")

R["29"] = dict(kw="LEADS", fam="foto", cta=("Quem não comprou na Black ainda pode comprar.", "a sequência pós-Black pronta"),
    slides=[
        dict(t="Não é perda, é lista", x="Quem chamou e não comprou **já mostrou interesse**. É o lead mais barato que você vai ter."),
        dict(t="Mensagem de segunda", x="\"Vi que você olhou o [produto]. Consegui manter o preço da Black **até quarta** para você.\""),
        dict(t="Separe por motivo", x="Achou caro, sem estoque, não respondeu. Cada grupo recebe **uma mensagem diferente**."),
        dict(t="O Natal está logo ali", x="Quem não comprou na Black pode comprar presente em dezembro. **Coloque na lista do Natal**."),
        dict(t="Tudo automático", x="No CRM, cada conversa da Black vira um contato com etiqueta, **pronto** para o próximo disparo."),
    ],
    legenda="300 pessoas te chamaram na Black e não compraram. E agora?\n\nNão é perda, é lista. Quem chamou já mostrou interesse, e o Natal está logo ali.\n\nComenta LEADS que eu te mando a sequência pós-Black pronta. 14 dias grátis na SuaMarca.\n\nFoto: Tony Webster, Wikimedia Commons (CC BY 2.0).")

R["30"] = dict(kw="APAGADA", fam="tweet", cta=("Reative a sua base, sem risco.", "o roteiro para reativar clientes parados"),
    slides=[
        dict(t="", x="Segundo o Alfredo Soares, a ideia veio da esposa: ela mandou cinco mensagens e **apagou**.\n\nEle ligou na hora para saber o que era."),
        dict(t="", x="Ele levou isso para a empresa: mandou mensagem para cerca de **500 mil clientes** e apagou em seguida."),
        dict(t="", x="Os clientes responderam \"o que era?\".\n\nA resposta: \"era um cupom, mas achei que você não queria… e é **só até hoje**\"."),
        dict(t="", x="Segundo ele, a ação vendeu mais de **R$ 10 milhões** em roupas.\n\nO gatilho: curiosidade + escassez."),
        dict(t="", x="O que copiar sem risco: **falar com a base parada**.\n\nDisparo só pela API oficial e para quem autorizou, senão o número cai."),
    ],
    legenda="Uma mensagem apagada vendeu R$ 10 milhões.\n\nA história é do Alfredo Soares: mensagem para a base, apagada em seguida, e um cupom \"só até hoje\" para quem perguntou o que era.\n\nO que dá para copiar sem risco: falar com quem já comprou e está parado.\n\nComenta APAGADA que eu te mando o roteiro para reativar clientes parados. 14 dias grátis na SuaMarca.")


# A automação de comentário manda o vídeo do CRM + o link do teste de 14 dias.
# Por isso todo CTA promete exatamente isso (exceto o BLACK, que manda o link da oferta).
import re as _re
ENTREGA = "o vídeo mostrando como fazer isso na SuaMarca e o link para testar 14 dias grátis"
for _d, _r in R.items():
    if _r["kw"] == "BLACK":
        continue
    _r["cta"] = (_r["cta"][0], "o vídeo mostrando isso na prática e o link do teste")
    _ps = _r["legenda"].split("\n\n")
    _ps = [f"Comenta {_r['kw']} que eu te mando {ENTREGA}." if p.startswith(f"Comenta {_r['kw']}") else p for p in _ps]
    _r["legenda"] = "\n\n".join(_ps)


# Fotos por card (padrão McDonald's: cada card do layout FOTO tem a sua foto). (arquivo, posição, crédito)
IG = "Imagem: @alfredosoares / Instagram"
WM = "Foto: {}, Wikimedia Commons ({})"
FOTOS = {
    "07": [("ig_mansao.jpg", "50% 30%", IG), ("ig_De2q3qJG6H1_0.jpg", "50% 30%", IG), ("ig_obra_topo.jpg", "50% 50%", IG),
           ("ig_alfredo_fala.jpg", "50% 30%", IG), ("yt_alfredo.jpg", "50% 30%", "Imagem: canal Alfredo Soares / YouTube")],
    "08": [("ray_kroc_1976.jpg", "50% 20%", "Foto: Ray Kroc em 1976 / domínio público"),
           ("downey_1953_loja.jpg", "30% 50%", WM.format("Northwalker", "CC0")),
           ("des_plaines_1955_museu.jpg", "78% 50%", WM.format("Cboyles4423", "CC BY-SA 4.0")),
           ("placa_route66_margolies.jpg", "52% 50%", "Foto: John Margolies / Library of Congress (domínio público)"),
           ("downey_1953_placa_speedee.jpg", "50% 8%", WM.format("Northwalker", "CC0"))],
    "16": [("fav_ahln3.jpg", "50% 50%", WM.format("AHLN", "CC BY 2.0")), ("fav_bemvindo.jpg", "50% 40%", WM.format("Carlos Varela", "CC BY 2.0")),
           ("fav_ahln2.jpg", "50% 40%", WM.format("AHLN", "CC BY 2.0")), ("fav_ahln1.jpg", "50% 50%", WM.format("AHLN", "CC BY 2.0")),
           ("fav_noite.jpg", "35% 50%", WM.format("Chensiyuan", "CC BY-SA 3.0"))],
    "24": [("pastel_br.jpg", "50% 50%", WM.format("BuenosAiresPhotographer", "CC BY-SA 2.0")),
           ("pastelaria_celeb.jpg", "40% 40%", WM.format("Eduardo P", "CC BY-SA 3.0")),
           ("pastel_frito.jpg", "50% 50%", WM.format("Túllio F", "CC BY-SA 4.0")),
           ("pastelaria_jac.jpg", "50% 50%", WM.format("Eduardo P", "CC BY-SA 3.0")),
           ("pastel_feira1.jpg", "50% 50%", WM.format("Avelludo", "CC BY-SA 4.0"))],
    "29": [("bf_bestbuy_2020.jpg", "50% 50%", WM.format("DanielPenfield", "CC BY-SA 4.0")),
           ("bf_camping.jpg", "50% 50%", WM.format("Myotus", "CC BY 4.0")),
           ("bf_walmart.jpg", "60% 50%", WM.format("Ildar Sagdejev", "CC BY-SA 4.0")),
           ("bf_exeter.jpg", "50% 60%", WM.format("David Smith", "CC BY-SA 2.0")),
           ("bf_henrietta.jpg", "45% 50%", WM.format("DanielPenfield", "CC BY-SA 4.0"))],
}
for _d, _fs in FOTOS.items():
    for _s, (_f, _p, _c) in zip(R[_d]["slides"], _fs):
        _s.update(f=_f, pos=_p, cr=_c)
