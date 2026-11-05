"""Modelo Liquid Glass (vidro líquido, estilo do iOS 26) para a Sua Marca: 3 slides 1080x1350.
Fundo com manchas de cor da marca + raio gigante; painéis de vidro com desfoque, saturação, refração (SVG) e brilho na borda.
Uso: python3 montar.py  -> slides/slide_01..03.png"""
import subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LOGO = (AQUI / "logo_horizontal_branca.png").as_uri()
RAIO = (AQUI / "BB_I1.png").as_uri()
RAIO_B = (AQUI / "BB_I2.png").as_uri()

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:-apple-system,'SF Pro Display','SF Pro Text','Helvetica Neue',sans-serif;color:#fff;position:relative;-webkit-font-smoothing:antialiased;background:#0E0D2E}
.fundo{position:absolute;inset:0;overflow:hidden}
.fundo .m{position:absolute;border-radius:50%%;filter:blur(70px)}
.fundo img.raio{position:absolute;filter:drop-shadow(0 40px 80px rgba(0,0,0,.35))}
.grao{position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;z-index:5}
.hd img{height:72px}
.hd span{font-size:26px;font-weight:600;opacity:.9}
/* o vidro */
.vidro{position:absolute;z-index:3;border-radius:%(raio)s;
 background:linear-gradient(135deg,rgba(255,255,255,.22),rgba(255,255,255,.06) 45%%,rgba(255,255,255,.12));
 backdrop-filter:url(#refracao) blur(22px) saturate(190%%) brightness(1.08);
 -webkit-backdrop-filter:blur(22px) saturate(190%%) brightness(1.08);
 box-shadow:inset 0 1.5px 0 rgba(255,255,255,.75),inset 0 -1px 0 rgba(255,255,255,.18),inset 1px 0 0 rgba(255,255,255,.25),
  0 30px 60px -20px rgba(6,6,30,.55),0 2px 6px rgba(6,6,30,.2)}
.vidro:before{content:'';position:absolute;inset:0;border-radius:inherit;padding:1.5px;pointer-events:none;
 background:linear-gradient(160deg,rgba(255,255,255,.9),rgba(255,255,255,.1) 35%%,rgba(255,255,255,0) 60%%,rgba(255,255,255,.45));
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude}
.vidro:after{content:'';position:absolute;left:8%%;right:8%%;top:0;height:42%%;border-radius:inherit;pointer-events:none;
 background:linear-gradient(180deg,rgba(255,255,255,.18),rgba(255,255,255,0))}
b{font-weight:800;color:#FACC15}
.seta{position:absolute;right:64px;bottom:50px;z-index:6;font-size:26px;font-weight:700;padding:14px 28px;border-radius:40px}
"""

SVG_FILTRO = """<svg width="0" height="0" style="position:absolute"><filter id="refracao" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="0.008 0.012" numOctaves="2" seed="7" result="r"/>
<feDisplacementMap in="SourceGraphic" in2="r" scale="38" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/></filter></svg>"""
GRAO = '<svg class="grao" width="1080" height="1350"><rect width="100%" height="100%" filter="url(#n)"/></svg>'


TEMA = "futurista"  # padrão aprovado em 05/11 · outras: claro | escuro | roxo
FUNDO = "minimal"  # "minimal" (padrão aprovado) ou "colorido" (primeira versão)


TEMAS = {
    "claro":  dict(bg="#F3F3F7", linha="rgba(15,23,42,.07)", brilho=("#2563EB", .14), logo="logo_horizontal_escura.png"),
    "escuro": dict(bg="#0B0B1C", linha="rgba(255,255,255,.045)", brilho=None, logo="logo_horizontal_branca.png"),
    "futurista": dict(bg="#070719", linha="rgba(255,255,255,.04)", brilho=None, logo="logo_horizontal_branca.png"),
    "roxo":   dict(bg="#4F55E6", linha="rgba(255,255,255,.09)", brilho=None, logo="logo_horizontal_branca.png"),
}
CSS_CLARO = """
body{color:#0F172A}
.vidro{background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(255,255,255,.45));
 box-shadow:inset 0 1.5px 0 #fff,inset 0 -1px 0 rgba(15,23,42,.06),0 24px 50px -24px rgba(15,23,42,.28),0 2px 6px rgba(15,23,42,.08)}
.vidro:before{background:linear-gradient(160deg,#fff,rgba(255,255,255,.2) 40%,rgba(15,23,42,.08) 70%,rgba(255,255,255,.8))}
b{color:#2563EB}
.escuro-sempre{color:#fff}
.escuro-sempre b{color:#FACC15}
"""


def fundo_minimal(variante):
    """Fundo minimalista: cor lisa + quadriculado suave que some nas bordas (+ brilho discreto só no tema claro)."""
    t = TEMAS[TEMA]
    grade = ('<div style="position:absolute;inset:0;'
             f'background-image:linear-gradient({t["linha"]} 1px,transparent 1px),linear-gradient(90deg,{t["linha"]} 1px,transparent 1px);'
             'background-size:60px 60px;background-position:-1px -1px;'
             '-webkit-mask-image:radial-gradient(ellipse 80% 70% at 50% 45%,#000 35%,transparent 100%)"></div>')
    brilho = ""
    if t["brilho"]:
        x, y, d = {1: (380, -320, 820), 2: (-300, 420, 820), 3: (260, 760, 820)}[variante]
        brilho = f'<div class="m" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;background:{t["brilho"][0]};opacity:{t["brilho"][1]};filter:blur(140px)"></div>'
    if TEMA == "futurista":
        return f'<div class="fundo" style="background:{t["bg"]}">{futuro(variante)}</div>'
    return f'<div class="fundo" style="background:{t["bg"]}">{brilho}{grade}</div>'


def futuro(variante):
    """Futurista e bem transparente: piso em perspectiva com grade fina, linha do horizonte com luz suave,
    anéis concêntricos finos, pontos de dados e arcos de órbita. Tudo entre 3% e 14% de opacidade."""
    cx, cy = {1: (860, 300), 2: (180, 360), 3: (880, 260)}[variante]
    piso = ('<div style="position:absolute;left:-540px;right:-540px;top:840px;height:900px;transform-origin:50% 0;'
            'transform:perspective(520px) rotateX(62deg);'
            'background-image:linear-gradient(rgba(140,146,255,.16) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(140,146,255,.16) 1.5px,transparent 1.5px);'
            'background-size:90px 90px;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 30%,#000 70%,transparent 100%)"></div>')
    horizonte = ('<div style="position:absolute;left:0;right:0;top:820px;height:2px;background:linear-gradient(90deg,transparent,rgba(160,165,255,.35),transparent)"></div>'
                 '<div style="position:absolute;left:140px;right:140px;top:700px;height:240px;border-radius:50%;background:#2563EB;opacity:.16;filter:blur(90px)"></div>')
    aneis = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,{o})" stroke-width="1.2" {d}/>'
                    for r, o, d in ((120, .12, ""), (210, .08, 'stroke-dasharray="2 10"'), (320, .06, ""), (450, .04, 'stroke-dasharray="40 18"')))
    arcos = (f'<path d="M{cx-520} {cy+40} A 560 180 -12 0 1 {cx+380} {cy-160}" fill="none" stroke="rgba(160,165,255,.14)" stroke-width="1.5"/>'
             f'<circle cx="{cx+300}" cy="{cy-128}" r="4" fill="rgba(200,205,255,.5)"/>')
    import random
    rnd = random.Random(variante * 31)
    pontos = "".join(f'<circle cx="{rnd.randint(0,1080)}" cy="{rnd.randint(0,820)}" r="{rnd.choice((1,1,1.5,2))}" fill="rgba(255,255,255,{rnd.choice((.08,.12,.18))})"/>' for _ in range(70))
    marcas = "".join(f'<path d="M{x} {y} h18 M{x} {y} v18" stroke="rgba(255,255,255,.12)" stroke-width="1.5" fill="none"/>'
                     for x, y in ((48, 150), (1014, 150)))
    svg = f'<svg width="1080" height="1350" style="position:absolute;inset:0">{aneis}{arcos}{pontos}{marcas}</svg>'
    return piso + horizonte + svg


def hd():
    logo = (AQUI / TEMAS[TEMA]["logo"]).as_uri()
    return f'<div class="hd"><img src="{logo}"><span>@seuperfil</span></div>'


def op(c):
    return '.55' if c == '#E5484D' else '.85'


def fundo(variante):
    if FUNDO == "minimal":
        return fundo_minimal(variante)
    manchas = {
        1: [(-180, 120, 760, "#2563EB"), (520, -160, 700, "#1E293B"), (640, 640, 560, "#FACC15"), (-160, 860, 560, "#BBF7D0"), (300, 420, 520, "#3B82F6")],
        2: [(560, 100, 760, "#2563EB"), (-200, -100, 680, "#1E293B"), (-160, 760, 620, "#FACC15"), (700, 980, 520, "#BBF7D0"), (200, 520, 460, "#E5484D")],
        3: [(240, 300, 800, "#2563EB"), (-260, 900, 640, "#FACC15"), (720, -80, 560, "#BBF7D0"), (680, 980, 560, "#1E293B")],
    }[variante]
    html = "".join(f'<div class="m" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;background:{c};opacity:{op(c)}"></div>' for x, y, d, c in manchas)
    raio = {1: (RAIO_B, 560, 120, 760, 14), 2: (RAIO, -120, 260, 720, -10), 3: (RAIO_B, 300, 180, 640, 6)}[variante]
    html += f'<img class="raio" src="{raio[0]}" style="left:{raio[1]}px;top:{raio[2]}px;height:{raio[3]}px;transform:rotate({raio[4]}deg);opacity:.95">'
    return f'<div class="fundo">{html}</div>{GRAO}'


HD = f'<div class="hd"><img src="{LOGO}"><span>@seuperfil</span></div>'


def notif(app, cor, titulo, texto, hora, y, empilha=False):
    sombra = ' style="transform:scale(.94);opacity:.8"' if empilha else ""
    return (f'<div class="vidro" style="left:96px;right:96px;top:{y}px;padding:26px 30px;--r:38px"{sombra}>'
            f'<div style="display:flex;gap:22px;align-items:center;position:relative;z-index:2">'
            f'<div style="width:78px;height:78px;border-radius:20px;background:{cor};display:flex;align-items:center;justify-content:center;font-size:40px;flex:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.5)">{app}</div>'
            f'<div style="flex:1"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:700"><span>{titulo}</span><span style="opacity:.7;font-weight:500">{hora}</span></div>'
            f'<div style="font-size:28px;margin-top:4px;opacity:.92">{texto}</div></div></div></div>')


def slide1():
    corpo = (fundo(1) + hd()
             + '<div style="position:absolute;top:170px;left:0;right:0;text-align:center;z-index:2;text-shadow:0 4px 30px rgba(0,0,30,.35)">'
               '<div style="font-size:36px;font-weight:600;opacity:.92">sexta-feira, 28 de novembro</div>'
               '<div style="font-size:250px;font-weight:700;letter-spacing:-8px;line-height:1;margin-top:6px">22:47</div></div>'
             + notif("💬", "#25D366", "Carla", "ainda tem no tamanho M?", "agora", 520)
             + notif("💬", "#25D366", "Rafael", "parcela em 10x? to esperando", "3 min", 668)
             + notif("📸", "linear-gradient(135deg,#F58529,#DD2A7B,#8134AF)", "Novo direct", "quanto fica no pix?", "12 min", 816)
             + '<div class="vidro" style="left:200px;right:200px;top:964px;padding:16px;text-align:center;border-radius:30px;font-size:26px;font-weight:700;z-index:3"><span style="position:relative;z-index:2">+ 47 mensagens sem resposta</span></div>'
             + '<div style="left:64px;right:64px;top:1060px;padding:34px 40px;border-radius:44px;background:linear-gradient(135deg,rgba(15,23,42,.82),rgba(15,23,42,.6))" class="vidro escuro-sempre">'
               '<div style="position:relative;z-index:2;font-size:54px;font-weight:800;line-height:1.08;letter-spacing:-1px">R$ 13,3 bi em 4 dias de Black.<br>Quanto vai ficar <b>sem resposta</b>?</div></div>'
             + '<div class="vidro seta" style="border-radius:40px;bottom:36px"><span style="position:relative;z-index:2">arrasta →</span></div>')
    return corpo


def slide2():
    linhas = [("22:47", "O cliente chama no WhatsApp", "#25D366"), ("22:59", "Ninguém responde. Ele chama o concorrente", "#E5484D"),
              ("23:04", "O concorrente responde em 5 minutos", "#FACC15"), ("09:12", "Você responde: \"bom dia! ainda tem interesse?\"", "#9B95A8")]
    itens = ""
    for k, (h, t, c) in enumerate(linhas):
        itens += (f'<div class="vidro" style="left:64px;right:64px;top:{560 + k*150}px;padding:28px 34px;border-radius:34px">'
                  f'<div style="position:relative;z-index:2;display:flex;gap:28px;align-items:center">'
                  f'<span style="font-size:44px;font-weight:800;font-variant-numeric:tabular-nums;min-width:150px">{h}</span>'
                  f'<span style="width:14px;height:14px;border-radius:50%;background:{c};flex:none;box-shadow:0 0 0 6px rgba(255,255,255,.15)"></span>'
                  f'<span style="font-size:32px;font-weight:600;line-height:1.25">{t}</span></div></div>')
    return (fundo(2) + hd()
            + '<div style="position:absolute;top:190px;left:64px;right:64px;z-index:2;text-shadow:0 4px 30px rgba(0,0,30,.35)">'
              '<div style="font-size:30px;font-weight:700;letter-spacing:3px;opacity:.85">O QUE ACONTECE NA SUA BLACK</div>'
              '<div style="font-size:84px;font-weight:800;line-height:1.02;letter-spacing:-2px;margin-top:18px">O problema não é<br>o anúncio. É a <b>hora</b><br>da resposta.</div></div>'
            + itens
            + '<div class="vidro seta" style="border-radius:40px"><span style="position:relative;z-index:2">arrasta →</span></div>')


def slide3():
    chips = "".join(f'<div class="vidro" style="position:relative;display:inline-block;margin:0 14px 16px 0;padding:16px 26px;border-radius:30px;font-size:28px;font-weight:700"><span style="position:relative;z-index:2">{t}</span></div>'
                    for t in ("IA responde em segundos", "Funil de vendas", "Follow-up automático", "Tudo num lugar só"))
    return (fundo(3) + hd()
            + '<div class="vidro" style="left:64px;right:64px;top:210px;bottom:200px;border-radius:56px;padding:64px 60px">'
              '<div style="position:relative;z-index:2;display:flex;flex-direction:column;height:100%">'
              f'<img src="{RAIO if TEMA == "claro" else RAIO_B}" style="height:120px;align-self:flex-start;filter:drop-shadow(0 10px 20px rgba(0,0,40,.3))">'
              '<div style="font-size:88px;font-weight:800;line-height:1.02;letter-spacing:-2px;margin-top:34px">Na Black,<br>quem responde<br><b>primeiro</b> vende.</div>'
              f'<div style="margin-top:44px">{chips}</div>'
              '<div style="margin-top:auto" class="cta">'
              '<div class="vidro" style="position:relative;padding:30px 36px;border-radius:999px;display:flex;justify-content:space-between;align-items:center;background:linear-gradient(135deg,rgba(250,204,21,.95),rgba(250,204,21,.78))">'
              '<span style="position:relative;z-index:2;font-size:40px;font-weight:800;color:#0F172A">Comenta FILA</span>'
              '<span style="position:relative;z-index:2;font-size:28px;font-weight:700;color:#0F172A">14 dias grátis →</span></div></div>'
              '</div></div>')


def main():
    global TEMA
    temas = sys.argv[1:] or [TEMA]
    for TEMA in temas:
        saida = AQUI / ("slides" if len(temas) == 1 and TEMA == "futurista" else f"slides_{TEMA}")
        saida.mkdir(exist_ok=True)
        for n, fn in enumerate((slide1, slide2, slide3), 1):
            css = CSS % {"raio": "var(--r,40px)"} + (CSS_CLARO if TEMA == "claro" else "")
            doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{SVG_FILTRO}{fn()}</body></html>'
            arq = saida / f"slide_{n:02d}.html"
            arq.write_text(doc, encoding="utf-8")
            png = saida / f"slide_{n:02d}.png"
            subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--allow-file-access-from-files", "--force-device-scale-factor=1",
                            "--virtual-time-budget=6000", "--window-size=1080,1350", f"--screenshot={png}", arq.as_uri()], check=True, capture_output=True)
            arq.unlink()
            print("OK", saida.name, png.name)


if __name__ == "__main__":
    main()
