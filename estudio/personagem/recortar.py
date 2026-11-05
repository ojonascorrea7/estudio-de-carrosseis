"""Recorta as expressões de folha_A_colorida.png e tira o fundo claro (vira PNG transparente).
Uso: python3 recortar.py   -> recortes/<nome>.png"""
from collections import deque
from pathlib import Path
from PIL import Image

AQUI = Path(__file__).resolve().parent

# (x, y, largura, altura) na folha original 2752x1536, por dentro da borda de cada quadrinho
EXPR = {
    "corpo": (120, 50, 620, 1460),
    "serio": (815, 54, 555, 440),
    "sorriso": (1455, 54, 572, 440),
    "bravo": (2099, 54, 578, 680),
    "risada": (812, 547, 558, 440),
    "pensando": (812, 1042, 558, 440),
    "desconfiado": (1452, 798, 575, 685),
    "apontando": (2099, 798, 578, 685),
}


def claro(p, lim=222):
    r, g, b = p[:3]
    return min(r, g, b) > lim and max(r, g, b) - min(r, g, b) < 30


def tirar_fundo(im, busto=True):
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    fundo = bytearray(w * h)
    fila = deque((x, y) for x in range(w) for y in (0, h - 1)) + deque((x, y) for y in range(h) for x in (0, w - 1))
    while fila:
        x, y = fila.popleft()
        i = y * w + x
        if fundo[i] or not claro(px[x, y]):
            continue
        fundo[i] = 1
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not fundo[ny * w + nx]:
                fila.append((nx, ny))
    # áreas claras fechadas grandes (vão entre braço e corpo) também são fundo; olho e dente são pequenos
    visto = bytearray(w * h)
    for y0 in range(h):
        for x0 in range(w):
            i0 = y0 * w + x0
            if fundo[i0] or visto[i0] or not claro(px[x0, y0]):
                continue
            regiao, fila2 = [], deque([(x0, y0)])
            visto[i0] = 1
            while fila2:
                x, y = fila2.popleft()
                regiao.append(y * w + x)
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        j = ny * w + nx
                        if not visto[j] and not fundo[j] and claro(px[nx, ny]):
                            visto[j] = 1
                            fila2.append((nx, ny))
            if len(regiao) > 2500:
                for j in regiao:
                    fundo[j] = 1
    # meio-tom da borda: pixel claro encostado no fundo também sai, com transparência parcial
    for y in range(h):
        for x in range(w):
            i = y * w + x
            if fundo[i]:
                px[x, y] = (0, 0, 0, 0)
            elif claro(px[x, y], 170) and any(
                    0 <= nx < w and 0 <= ny < h and fundo[ny * w + nx]
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))):
                r, g, b, _ = px[x, y]
                px[x, y] = (r, g, b, int(255 * (255 - min(r, g, b)) / 85))
    im = im.crop(im.getbbox())
    if not busto:
        return im
    # busto: corta na altura em que o corpo encosta na lateral, para o corte ficar só embaixo
    w, h = im.size
    a = im.getchannel("A").load()
    for y in range(int(h * 0.35), h):
        if any(a[x, y] > 128 for x in (0, 1, 2, w - 3, w - 2, w - 1)):
            return im.crop((0, 0, w, y))
    return im


def main():
    folha = Image.open(AQUI / "folha_A_colorida.png")
    saida = AQUI / "recortes"
    saida.mkdir(exist_ok=True)
    for nome, (x, y, w, h) in EXPR.items():
        tirar_fundo(folha.crop((x, y, x + w, y + h)), busto=nome != "corpo").save(saida / f"{nome}.png")
        print("OK", nome)


if __name__ == "__main__":
    main()
