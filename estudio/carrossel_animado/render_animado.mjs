// render_animado.mjs · transforma slides HTML animados em MP4 (1080x1350, 30 fps, loop).
// Uso: node render_animado.mjs slides/slide-01.html [slides/slide-02.html ...] [--audio trilha.mp3]
// Requer: npm i playwright (usa o Google Chrome instalado) e ffmpeg no PATH.
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';

const args = process.argv.slice(2);
const iAudio = args.indexOf('--audio');
const audio = iAudio >= 0 ? args.splice(iAudio, 2)[1] : null;
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const FPS = 30;

const browser = await chromium.launch({ executablePath: fs.existsSync(CHROME) ? CHROME : undefined });
let inicioAudio = 0;
for (const arq of args) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(arq));
  await page.waitForFunction(() => window.__pronto === true, null, { timeout: 30000 });
  const dur = await page.evaluate(() => window.__duracao);
  const saida = arq.replace(/\.html$/, '.mp4');
  const ff = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-'];
  if (audio) ff.push('-ss', String(inicioAudio), '-t', String(dur), '-i', audio, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k');
  ff.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-r', String(FPS), '-t', String(dur), '-movflags', '+faststart', saida);
  const proc = spawn('ffmpeg', ff);
  for (let i = 0; i < Math.round(dur * FPS); i++) {
    await page.evaluate((t) => window.seek(t), i / FPS);
    const png = await page.screenshot({ clip: { x: 0, y: 0, width: 1080, height: 1350 } });
    if (!proc.stdin.write(png)) await new Promise((r) => proc.stdin.once('drain', r));
  }
  proc.stdin.end();
  await new Promise((r) => proc.on('close', r));
  await page.close();
  inicioAudio += dur; // o próximo slide continua a mesma música
  console.log('ok', saida, dur + 's');
}
await browser.close();
