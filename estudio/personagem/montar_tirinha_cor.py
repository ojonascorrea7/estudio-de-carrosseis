"""Tirinha estilo A (colorida): suas expressões recortadas (recortes/, gerados por recortar.py)
dentro de um cenário desenhado, com balão de fala por cima, .
Uso: python3 montar_tirinha_cor.py   -> gera tirinha_black/slide_NN.png (1080x1350)
Marcação no texto: **x** = destaque amarelo, __x__ = roxo."""
import html, re, subprocess
from pathlib import Path
from PIL import Image

AQUI = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HANDLE = "@seuperfil"
TRACO = "#2A2320"

# (expressão, cenário, fala); expressão None = slide final
SLIDES = [
    ("corpo", "sala", "Passando para te contar em primeira mão:\na **Black Friday da Sua Marca** chegou! 🖤🔥"),
    ("pensando", "escritorio", "Você ainda paga uma ferramenta para CRM, outra para WhatsApp, outra para o site…?"),
    ("bravo", "sala", "E nenhuma conversa com a outra.\nNo fim do mês, **a conta chega igual**."),
    ("sorriso", "escritorio", "E se fosse **tudo num lugar só**?\nCRM, automações, WhatsApp, agentes de IA e site."),
    ("apontando", "sala", "Na Black Friday:\n✅ **15% OFF** em qualquer plano\n✅ **14 dias grátis** para testar"),
    ("serio", "escritorio", "No plano anual tem mais:\n✅ **2 meses grátis** já inclusos"),
    ("risada", "sala", "E os __agentes de IA__ trabalhando por você vêm **nos dois planos**. 🤖"),
    ("desconfiado", "escritorio", "⏰ Mas corre:\nvale só **até 30/11/2026**\nou enquanto durarem as vagas."),
    (None, "sala", "Black Friday\n**Sua Marca**\n\n15% OFF · 14 dias grátis\n2 meses grátis no anual\nAgentes de IA inclusos\n\nComenta **BLACK** que eu te mando o link."),
]

PISO_Y = 980


def piso():
    linhas = [f'<rect x="0" y="{PISO_Y}" width="1080" height="{1350-PISO_Y}" fill="#ECE8E1"/>']
    for k in range(-8, 17):  # linhas de fuga dos azulejos
        x = 540 + k * 150
        linhas.append(f'<line x1="{540 + (x-540)*0.35:.0f}" y1="{PISO_Y}" x2="{x:.0f}" y2="1350" stroke="#CFCAC2" stroke-width="3"/>')
    for y in (1040, 1120, 1220, 1340):
        linhas.append(f'<line x1="0" y1="{y}" x2="1080" y2="{y}" stroke="#CFCAC2" stroke-width="3"/>')
    linhas.append(f'<rect x="-10" y="{PISO_Y-26}" width="1100" height="26" fill="#FFFFFF" stroke="{TRACO}" stroke-width="5"/>')
    return "".join(linhas)


def planta(x, y):
    folhas = "".join(
        f'<path d="M{x} {y} q{dx*0.4} {-dy*0.6} {dx} {-dy} q{-dx*0.6} {dy*0.1} {-dx} {dy}z" fill="#7DAE5E" stroke="{TRACO}" stroke-width="5"/>'
        for dx, dy in ((-90, 170), (-40, 230), (20, 250), (80, 200), (120, 130), (-130, 100)))
    return (folhas + f'<path d="M{x-75} {y} h150 l-20 150 h-110z" fill="#C9774A" stroke="{TRACO}" stroke-width="6"/>'
            f'<rect x="{x-85}" y="{y-12}" width="170" height="30" rx="6" fill="#D88A5C" stroke="{TRACO}" stroke-width="6"/>')


CENARIOS = {
    "sala": lambda: (
        '<rect width="1080" height="1350" fill="#FBF8F2"/>'
        # janela
        f'<rect x="70" y="430" width="250" height="300" rx="8" fill="#CFE3F5" stroke="{TRACO}" stroke-width="7"/>'
        f'<line x1="195" y1="430" x2="195" y2="730" stroke="{TRACO}" stroke-width="6"/>'
        f'<line x1="70" y1="580" x2="320" y2="580" stroke="{TRACO}" stroke-width="6"/>'
        '<path d="M95 520 q30 -25 60 0" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round"/>'
        f'<rect x="55" y="728" width="280" height="22" rx="4" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
        # quadro roxo com raio amarelo
        f'<rect x="800" y="420" width="190" height="240" rx="6" fill="#2563EB" stroke="{TRACO}" stroke-width="7"/>'
        f'<path d="M905 460 l-55 95 h40 l-25 75 l75 -110 h-42 l32 -60z" fill="#FACC15" stroke="{TRACO}" stroke-width="5"/>'
        + piso() + planta(930, 860)),
    "escritorio": lambda: (
        '<rect width="1080" height="1350" fill="#FBF8F2"/>'
        # prateleira com livros
        f'<rect x="60" y="560" width="300" height="20" fill="#B9865A" stroke="{TRACO}" stroke-width="6"/>'
        + "".join(f'<rect x="{x}" y="{560-h}" width="34" height="{h}" fill="{c}" stroke="{TRACO}" stroke-width="5"/>'
                  for x, h, c in ((80, 110, "#2563EB"), (116, 90, "#FACC15"), (152, 120, "#2A2320"), (188, 100, "#BBF7D0"), (224, 85, "#2563EB")))
        + f'<circle cx="300" cy="525" r="30" fill="#7DAE5E" stroke="{TRACO}" stroke-width="5"/>'
        # relógio de parede
        f'<circle cx="880" cy="500" r="80" fill="#fff" stroke="{TRACO}" stroke-width="8"/>'
        f'<line x1="880" y1="500" x2="880" y2="450" stroke="{TRACO}" stroke-width="7" stroke-linecap="round"/>'
        f'<line x1="880" y1="500" x2="915" y2="520" stroke="#2563EB" stroke-width="7" stroke-linecap="round"/>'
        + piso() +
        # mesa com notebook à direita
        f'<rect x="760" y="820" width="340" height="26" fill="#C99A6B" stroke="{TRACO}" stroke-width="6"/>'
        f'<rect x="790" y="846" width="22" height="200" fill="#B9865A" stroke="{TRACO}" stroke-width="6"/>'
        f'<path d="M840 820 l20 -110 h170 l-15 110z" fill="#3A3442" stroke="{TRACO}" stroke-width="6"/>'
        f'<circle cx="940" cy="765" r="12" fill="#FACC15"/>'),
}

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@700;800&family=Bangers&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:'Baloo 2',cursive;position:relative}
svg.cena{position:absolute;inset:0}
.hd{position:absolute;top:30px;left:0;right:0;text-align:center;font-size:28px;color:#8A857C;font-weight:700}
.bal{position:absolute;left:%(bx)spx;width:%(bw)spx;background:#fff;border:6px solid #2A2320;border-radius:34px;
 padding:26px 34px;font-size:%(fs)spx;line-height:1.15;color:#2A2320;white-space:pre-line;text-align:center;font-weight:800;z-index:3}
.bal:after{content:'';position:absolute;bottom:-50px;left:%(cauda)spx;border-width:50px 22px 0 22px;border-style:solid;
 border-color:#2A2320 transparent transparent transparent;transform:skewX(%(incl)sdeg)}
.bal:before{content:'';position:absolute;bottom:-36px;left:calc(%(cauda)spx + 8px);border-width:40px 14px 0 14px;border-style:solid;
 border-color:#fff transparent transparent transparent;z-index:2;transform:skewX(%(incl)sdeg)}
b{font-weight:800;background:linear-gradient(transparent 58%%,#FACC15 58%%,#FACC15 92%%,transparent 92%%);padding:0 4px}
i{font-style:normal;color:#2563EB}
.pers{position:absolute;z-index:2}
.fim{position:absolute;left:90px;right:90px;top:170px;bottom:170px;background:#fff;border:7px solid #2A2320;border-radius:34px;
 box-shadow:14px 14px 0 #2563EB;display:flex;align-items:center;justify-content:center;text-align:center;white-space:pre-line;
 font-size:52px;line-height:1.2;color:#2A2320;padding:50px;font-weight:800;z-index:3}
.fim .t{font-family:'Bangers',cursive;font-size:96px;letter-spacing:2px;line-height:1;font-weight:400}
"""


def marcar(texto):
    t = html.escape(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"__(.+?)__", r"<i>\1</i>", t)


def personagem(nome, topo):
    """Devolve (html da imagem, y do topo da imagem)."""
    arq = AQUI / "recortes" / f"{nome}.png"
    w, h = Image.open(arq).size
    if nome == "corpo":  # corpo inteiro em pé no piso
        alt = 1300 - topo
        larg = w * alt / h
        return f'<img class="pers" src="{arq.as_uri()}" style="height:{alt:.0f}px;left:{540-larg/2:.0f}px;top:{topo:.0f}px">', topo
    larg = min(w * 860 / h, 900)  # busto encostado na borda de baixo, como close de quadrinho
    alt = h * larg / w
    return f'<img class="pers" src="{arq.as_uri()}" style="width:{larg:.0f}px;left:{540-larg/2:.0f}px;bottom:0">', 1350 - alt


def main():
    saida = AQUI / "tirinha_black"
    saida.mkdir(exist_ok=True)
    for velho in saida.glob("slide_*.png"):
        velho.unlink()
    for n, (expr, cena, texto) in enumerate(SLIDES, 1):
        fs = 50 if len(texto) < 80 else 44
        svg = f'<svg class="cena" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{CENARIOS[cena]()}</svg>'
        esquerda = n % 2 == 1
        vars_ = {"fs": fs, "bw": 760, "bx": 70 if esquerda else 250,
                 "cauda": 520 if esquerda else 200, "incl": 20 if esquerda else -20}
        if expr:
            linhas = texto.count("\n") + 1 + len(texto) // 30
            alt_bal = 64 + linhas * fs * 1.15
            if expr == "corpo":
                topo_bal = 110
                img, _ = personagem(expr, topo_bal + alt_bal + 70)
            else:
                img, topo_img = personagem(expr, 0)
                topo_bal = max(100, topo_img - alt_bal - 40)
            corpo = f'<div class="hd">{HANDLE}</div><div class="bal" style="top:{topo_bal:.0f}px">{marcar(texto)}</div>' + img
        else:
            linhas = marcar(texto).split("\n")
            linhas[0] = f'<span class="t">{linhas[0]}</span>'
            linhas[1] = f'<span class="t">{linhas[1]}</span>'
            corpo = f'<div class="hd">{HANDLE}</div><div class="fim"><div>{chr(10).join(linhas)}</div></div>'
        doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % vars_}</style>'
               f'</head><body>{svg}{corpo}</body></html>')
        arq = saida / f"slide_{n:02d}.html"
        arq.write_text(doc, encoding="utf-8")
        png = saida / f"slide_{n:02d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", "--force-device-scale-factor=1",
                        "--virtual-time-budget=8000", "--window-size=1080,1350",
                        f"--screenshot={png}", arq.as_uri()], check=True, capture_output=True)
        arq.unlink()
        print("OK", png.name)


if __name__ == "__main__":
    main()
