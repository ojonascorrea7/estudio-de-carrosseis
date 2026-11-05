// animar.js · utilitários de movimento para slides animados.
// Regra de ouro: tudo é função pura do tempo t (em segundos). Nenhum estado entre quadros,
// nenhum setTimeout e nenhum Math.random sem semente. O renderizador chama window.seek(t)
// em qualquer ordem e fotografa o resultado.
(function () {
  const M = {};
  M.limita = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  M.trecho = (t, ini, fim) => M.limita((t - ini) / (fim - ini));        // 0 → 1 dentro de [ini, fim]
  M.mistura = (a, b, u) => a + (b - a) * u;

  // curvas de suavidade
  M.saida = (u) => 1 - Math.pow(1 - u, 3);                              // desacelera
  M.entrada = (u) => u * u * u;                                         // acelera
  M.suave = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
  M.passa = (u, forca = 1.5) => 1 + (forca + 1) * Math.pow(u - 1, 3) + forca * Math.pow(u - 1, 2); // passa do ponto e volta
  M.vai_e_volta = (u) => Math.pow(Math.sin(Math.PI * M.limita(u)), 2);   // 0 → 1 → 0, zero exato nas pontas

  // mola que zera exatamente no fim (o loop fecha sem tranco)
  M.mola = (dt, dur = 0.45, freq = 2.4) => (dt < 0 || dt >= dur ? 0 : Math.pow(1 - dt / dur, 2) * Math.cos(2 * Math.PI * freq * dt));
  // carimbo: achata no impacto e volta, mantendo o volume visual
  M.carimbo = (t, t0, forca = 0.14) => { const a = -forca * M.mola(t - t0); return { sx: 1 / (1 + a), sy: 1 + a }; };
  M.pulo = (t, t0, forca = 0.12) => 1 + forca * M.mola(t - t0);

  // aplica transform só quando muda (o quadro de repouso fica idêntico ao estático)
  M.transforma = (el, valor, origem) => {
    if (el.style.transform !== valor) el.style.transform = valor;
    if (origem && el.style.transformOrigin !== origem) el.style.transformOrigin = origem;
  };

  // registra o slide: duração em segundos (4, 6 ou 8 = compassos inteiros a 120 BPM)
  M.slide = (duracao, seek) => {
    window.__duracao = duracao;
    window.seek = (t) => seek(((t % duracao) + duracao) % duracao);
  };
  // espera fontes e imagens antes de liberar o render
  M.pronto = async (montar) => {
    await document.fonts.ready;
    await Promise.all([...document.images].map((i) => (i.complete ? 0 : new Promise((r) => (i.onload = i.onerror = r)))));
    montar();
    window.seek(0);
    window.__pronto = true;
    if (location.search.includes('play')) { const t0 = performance.now(); const f = () => { window.seek((performance.now() - t0) / 1000); requestAnimationFrame(f); }; f(); }
  };
  window.ANIMAR = M;
})();
