# 6. Carrossel animado

Cada slide vira um MP4 curto em loop, no lugar da imagem parada. Use em posts de destaque, não em todos.

## Como funciona
- **Um HTML por slide**, com `window.seek(t)` controlando tudo o que se mexe em função do tempo.
- **O renderizador** (`estudio/carrossel_animado/render_animado.mjs`) abre o HTML no Chrome sem janela, chama `seek(t)` quadro a quadro (30 fps), fotografa e envia os quadros para o ffmpeg.
- **Sem framework de vídeo:** por isso o texto fica nítido e cada movimento cai onde foi programado.

## Regras
- **Duração em compassos inteiros a 120 BPM** (4, 6 ou 8 s), para a música emendar de um slide para o outro.
- **O quadro 0 é o design estático pronto:** é a capa do slide e o primeiro quadro que aparece. Assim o mesmo trabalho entrega o PNG e o MP4.
- **No fim, tudo volta ao repouso:** o último quadro emenda no primeiro, sem tranco.
- **Nada linear:** use as curvas de `animar.js` (`saida`, `suave`, `passa`) e o `carimbo` para impacto.
- **Algo novo a cada 2 a 4 segundos**, e cada acerto numa batida (a cada 0,5 s).
- **Função pura do tempo:** sem `setTimeout`, sem estado entre quadros, sem aleatório sem semente.

## Exemplo
`estudio/carrossel_animado/exemplo/slide-01.html`: um número que some, conta de 0 até o valor e carimba, com barras que crescem uma por batida.

```bash
cd estudio/carrossel_animado
npm i playwright
node render_animado.mjs exemplo/slide-01.html                # gera exemplo/slide-01.mp4
node render_animado.mjs exemplo/*.html --audio trilha.mp3     # com música contínua entre os slides
```

## Publicar
- Carrossel com os MP4 na ordem.
- Sem música do Instagram por cima, porque o som já está no vídeo.
- Confira no celular se nada fica embaixo do contador "1/7" nem do ícone de som.
