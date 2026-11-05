---
name: estudio-de-carrosseis
description: >
  Cria carrosséis de Instagram prontos para postar, da pauta ao PNG 1080x1350, em 7 layouts
  (notícia, foto, tweet, print de WhatsApp, dados, tirinha e Liquid Glass), com slides internos,
  CTA por palavra-chave, legenda e, se pedido, versão animada em MP4. Também monta o calendário
  do mês sem repetir layout em dias seguidos. Use SEMPRE que o pedido envolver carrossel,
  "post em slides", capa de carrossel, calendário de posts, "faz um carrossel sobre X",
  "monta a semana/o mês de conteúdo", "transforma essa notícia em post", "carrossel animado"
  ou revisar um carrossel pronto, mesmo que a skill não seja citada.
---

# Estúdio de Carrosséis

Um carrossel é uma conversa em 7 tempos: a **capa** faz a pessoa querer algo, o **slide 2** paga essa promessa, o **meio** sustenta com uma ideia por slide, a **virada** liga o assunto ao que a marca resolve e o **CTA** pede um próximo passo que a automação consegue entregar.

Esta skill usa os motores do repositório (pasta `estudio/`). Os guias completos estão em `docs/`. Leia o guia do passo antes de executar.

## Antes de começar: a marca
Procure um `marca.md` na pasta de trabalho. Se não houver, crie um a partir de `modelo_marca.md` e pergunte só o essencial:
- nome e @ do perfil
- produto e oferta (preço público, teste grátis)
- palavra que a automação de comentários entende
- o que a automação entrega
- cores, logos e personagem da tirinha
- assuntos proibidos e regras do cliente (por exemplo, nunca citar o fornecedor de uma ferramenta white label)

Grave as respostas no `marca.md` e use em todo post.

## O fluxo (com paradas)

### 1. Pauta (`docs/05_pesquisa_de_pautas.md`)
- Busque o que está em alta no nicho: notícia da semana, regra nova, número novo, data, conteúdo de criador que gerou comentário.
- Para cada pauta, escreva a **ponte em uma frase** ("o assunto X mostra que o seu cliente precisa de Y").
- **Valide a fonte:** se a única fonte diz que algo viralizou mas não traz número, não use o número. Troque o ângulo ou a pauta.
- **Fora sempre:** política, aposta e polêmica pessoal.

### 2. Capas (`docs/04_copy_e_cta.md` e `docs/02_layouts.md`)
- Escolha o layout pela pauta:

  | Pauta | Layout |
  |---|---|
  | Fato ou estudo | notícia |
  | Mundo real | foto |
  | Opinião | tweet |
  | Conversa | print |
  | Número que choca | dados |
  | Situação do dono | tirinha |
  | Notificação, tela ou IA | Liquid Glass |

- Escreva a capa: até 12 palavras na linha principal, uma em destaque.
- Renderize com `estudio/calendario/capas_nov/montar_capas.py` (configure a lista `CAPAS`) e gere a folha de visão geral.
- **PARADA:** mostre as capas e espere aprovação antes de montar os slides.

### 3. Grade do mês (`docs/03_sequencia_e_grade.md`)
- Distribua os layouts em partes iguais (por exemplo, 6 layouts × 4 posts).
- Nunca o mesmo layout em dias seguidos.
- Espalhe o layout mais forte ao longo do mês, sem concentrar no fim.
- Temas presos a data ficam no dia. Os atemporais podem trocar de dia para fechar a grade.
- Mostre a sequência em tabela antes de seguir.

### 4. Roteiro dos 7 slides
Escreva no `roteiro.py` (veja o exemplo em `estudio/calendario/carrosseis_nov/roteiro.py`): 5 slides de conteúdo, CTA e legenda.
- Uma ideia por slide: título curto e 1 a 3 frases.
- Use o concreto: a mensagem exata, o horário, o valor.
- Prefira a **prova em par** (ruim × bom, antes × depois): é a mais barata e a mais forte.
- Toda frase de terceiro leva quem disse e onde. Relato fica com "segundo ele".
- **CTA:** "Comenta PALAVRA", prometendo exatamente o que a automação entrega.
- Uma palavra única por post.

### 5. Slides no estilo da capa
Rode `estudio/calendario/carrosseis_nov/montar_carrosseis.py`. Regras por layout:
- **Foto:** **cada card tem a sua foto**, não só a capa. Busque 5 ou 6 fotos por post antes de montar, com licença livre (Wikimedia Commons pela API, com autor e licença) ou próprias. Anote o crédito no rodapé do card.
- **Tirinha:** o cenário e a expressão mudam a cada slide, e o cenário conta o assunto da fala. Use todas as poses disponíveis do personagem, não só o busto.
- **Print:** título + mini-conversa + nota explicando o porquê.
- **Liquid Glass:** fundo futurista bem transparente, e vidro com desfoque e brilho na borda.

### 6. Crítica antes de mostrar
Monte a folha de contato (todas as capas e todos os slides) e **olhe para ela**. Confira cada item:
- [ ] A capa se lê em miniatura?
- [ ] O slide 2 paga a capa?
- [ ] Há uma virada clara para o produto?
- [ ] Todo número tem fonte e toda foto tem crédito?
- [ ] Nada importante nos cantos do Instagram (contador em cima à direita, som embaixo à direita) e margem de 64 a 72 px?
- [ ] A logo está na versão certa para o fundo, com o @ no alto à direita?
- [ ] O CTA promete só o que a automação entrega?
- [ ] Algum layout ficou repetido em dias seguidos?

Corrija o que falhar e renderize de novo. **PARADA:** mostre a folha final e a legenda.

### 7. Entrega e agendamento
- Entregue a pasta `DD_PALAVRA/` com `slide_01..07.png` e `legenda.txt`.
- Agende só com aprovação explícita do usuário.
- Depois de agendar, confira no painel se todas as imagens do carrossel subiram. Alguns agendadores mostram só a primeira na API.
- Para corrigir um post já agendado, **edite o mesmo post** em vez de criar outro, para não duplicar.
- Liste para o usuário as palavras-chave novas que precisam entrar na automação de comentários.

### 8. Versão animada (só quando pedirem) (`docs/06_carrossel_animado.md`)
- Um HTML por slide, com `window.seek(t)` e `estudio/carrossel_animado/animar.js`.
- Renderize com `render_animado.mjs`.
- O quadro 0 é o PNG estático aprovado. O loop fecha no repouso, e a duração é 4, 6 ou 8 segundos.
- Não anime todos os posts: use só nos de destaque.

## Regras que nunca mudam
- **Texto é desenhado pelo código.** Nunca imagem gerada com letras.
- **Imagem de IA só com aprovação de custo.** Prefira foto real com licença.
- **Uma cor de destaque por slide, numa palavra.** Proibido texto em degradê e neon.
- **Proporção do mês:** 80% dor, história e educação, 20% oferta.
- **Nada externo sem OK:** nunca publique, agende ou apague sem aprovação do usuário.
- **Conflito entre regras:**
  1. verdade
  2. clareza
  3. estética
