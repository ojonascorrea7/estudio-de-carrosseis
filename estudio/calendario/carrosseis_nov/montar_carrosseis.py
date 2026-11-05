"""Monta os 24 carrosséis de novembro: slide_01 = capa aprovada (capas_nov/capas), slides 02-06 = conteúdo
no estilo do layout da capa, slide_07 = CTA. Saída: DD_PALAVRA/slide_NN.png + legenda.txt
Uso: python3 montar_carrosseis.py [07 08 ...]"""
import html, importlib.util, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CAPAS = AQUI.parent / "capas_nov"
spec = importlib.util.spec_from_file_location("mc", CAPAS / "montar_capas.py")
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)
sys.path.insert(0, str(AQUI))
from roteiro import R  # noqa: E402

CHROME = mc.CHROME
HANDLE = "@seuperfil"
ESCURA, BRANCA = mc.ESCURA, mc.BRANCA
mc.CENAS.update({k: v for k, v in mc.eev.CENARIOS.items() if k not in mc.CENAS})
FONTES = mc.FONTES


def m(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(t))


def logo(uri):
    return f'<img src="{uri}" style="height:72px;width:auto;display:block">'


SETA_CLARA = ('<span style="position:absolute;right:64px;bottom:50px;z-index:6;font-family:\'Plus Jakarta Sans\',sans-serif;font-size:26px;'
              'font-weight:800;color:#1B1820;background:#FACC15;border:4px solid #1B1820;border-radius:40px;padding:10px 24px">arrasta →</span>')


def contador(n, cor):
    return (f'<span style="position:absolute;left:64px;bottom:58px;z-index:6;font-family:\'Plus Jakarta Sans\',sans-serif;font-size:24px;'
            f'font-weight:700;color:{cor};opacity:.6">{n:02d}/07</span>')


# ---------------------------------------------------------------- NOTÍCIA
CSS_NOT = """*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#F4F1EA;font-family:'Plus Jakarta Sans',sans-serif;color:#1B1820;position:relative}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.hd span{font-size:26px;font-weight:700;color:#6B6475}
.jornal{position:absolute;top:136px;left:64px;right:64px;border-top:6px solid #1B1820;border-bottom:2px solid #1B1820;padding:14px 0;
 display:flex;justify-content:space-between;font-size:22px;font-weight:800;letter-spacing:3px}
.box{position:absolute;left:64px;right:64px;top:280px;bottom:170px;display:flex;flex-direction:column;justify-content:center}
.num{width:120px;height:120px;border-radius:50%;background:#2563EB;color:#fff;font-size:52px;font-weight:800;display:flex;align-items:center;justify-content:center;border:5px solid #1B1820}
h1{font-family:'Playfair Display',serif;font-weight:900;font-size:86px;line-height:1.04;letter-spacing:-1px;margin-top:40px}
p{margin-top:36px;font-size:42px;line-height:1.38;font-weight:500;color:#2A2533;white-space:pre-line;border-left:8px solid #FACC15;padding-left:28px}
p b{background:linear-gradient(transparent 60%,#FACC15 60%);font-weight:800}
"""


def noticia_int(d, n, s):
    corpo = (f'<div class="hd">{logo(ESCURA)}<span>{HANDLE}</span></div>'
             f'<div class="jornal"><span>PLANTÃO DO EMPRESÁRIO</span><span>{d}/11</span></div>'
             f'<div class="box"><div class="num">{n - 1:02d}</div><h1>{m(s["t"])}</h1><p>{m(s["x"])}</p></div>'
             + contador(n, "#1B1820") + SETA_CLARA)
    return f'<style>{FONTES}{CSS_NOT}</style></head><body>{corpo}</body>'


# ---------------------------------------------------------------- FOTO (cards escuros do padrão Fome de Poder)
def foto_int(d, n, s):
    if s.get("f"):  # card com foto, no padrão Fome de Poder
        mc.fdp.AQUI = mc.AQUI
        body = mc.fdp.montar(dict(tipo="foto", foto=s["f"], pos=s["pos"], chapeu=f"{n - 1:02d} · {s['t'].upper()}",
                                  titulo=s["x"], credito=s["cr"]))
        body = body.replace(mc.MARCA, logo(BRANCA))
        extra = "h1{font-size:60px!important;line-height:1.12!important}h1 b{color:#FACC15}"
        return f'<style>{mc.fdp.CSS}{extra}</style></head>{body}'
    body = mc.fdp.montar(dict(tipo="escuro", chapeu=f"{n - 1:02d}", titulo=s["t"], texto=s["x"], credito=f"{n:02d}/07"))
    body = body.replace(mc.MARCA, logo(BRANCA))
    extra = ".escuro h1{font-size:104px}p{font-size:48px!important;line-height:1.4!important}.escuro .chapeu{font-size:30px}"
    return f'<style>{mc.fdp.CSS}{extra}</style></head>{body}'


# ---------------------------------------------------------------- TWEET
def tweet_int(d, n, s):
    tema = "escuro" if n % 2 == 0 else "claro"
    texto = (f'**{s["t"]}**\n\n' if s["t"] else "") + s["x"]
    fs = 58 if len(texto) < 150 else 52
    doc = mc.tweet(dict(tema=tema, texto=texto, rodape=f"{n:02d}/07", fs=fs))
    return doc.replace(mc.MARCA, logo(BRANCA if tema == "escuro" else ESCURA))


# ---------------------------------------------------------------- PRINT
CSS_PR = """*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#BBF7D0;font-family:'Plus Jakarta Sans',sans-serif;color:#1B1820;position:relative}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.hd span{font-size:26px;font-weight:700;color:#3A6B55}
h1{position:absolute;top:150px;left:64px;right:64px;font-size:74px;line-height:1.05;font-weight:800;letter-spacing:-1.5px}
.chat{position:absolute;left:96px;right:96px;top:420px;background:#EFE7DD;border:8px solid #1B1820;border-radius:44px;padding:36px 30px;display:flex;flex-direction:column;gap:18px}
.msg{max-width:84%;padding:20px 24px 30px;border-radius:22px;font-size:36px;line-height:1.3;font-weight:500;position:relative;box-shadow:0 2px 0 rgba(0,0,0,.08)}
.msg small{position:absolute;right:16px;bottom:6px;font-size:18px;color:#6B6475}
.ele{background:#fff;align-self:flex-start;border-top-left-radius:6px}
.eu{background:#D9FDD3;align-self:flex-end;border-top-right-radius:6px}
.nota{position:absolute;left:64px;right:64px;background:#fff;border:5px solid #1B1820;border-radius:32px;padding:34px 40px;font-size:42px;line-height:1.35;font-weight:600;box-shadow:12px 12px 0 #2563EB;white-space:pre-line}
.nota b{color:#2563EB;font-weight:800}
"""


def print_int(d, n, s):
    corpo = f'<div class="hd">{logo(ESCURA)}<span>{HANDLE}</span></div><h1>{m(s["t"])}</h1>'
    if s.get("chat"):
        msgs = "".join(f'<div class="msg {q}">{html.escape(t)}<small>{"10:1" + str(k) + (" ✓✓" if q == "eu" else "")}</small></div>'
                       for k, (q, t) in enumerate(s["chat"]))
        corpo += f'<div class="chat">{msgs}</div><div class="nota" style="bottom:170px">{m(s["x"])}</div>'
    else:
        corpo += f'<div class="nota" style="top:470px">{m(s["x"])}</div>'
    return f'<style>{FONTES}{CSS_PR}</style></head><body>{corpo}{contador(n, "#1B1820")}{SETA_CLARA}</body>'


# ---------------------------------------------------------------- TIRINHA
def tirinha_int(d, n, s):
    fs = 50 if len(s["x"]) < 90 else 46
    doc = mc.tirinha(dict(expr=s["expr"], cena=s["cena"], tag="", texto=s["x"], fs=fs))
    doc = doc.replace('<div class="capa-tag"></div>', contador(n, "#2A2320"))
    return doc.replace(mc.MARCA, logo(ESCURA))


# ---------------------------------------------------------------- LIQUID GLASS
def glass_int(d, n, s):
    v = (n % 3) + 1
    card = mc._vidro("left:64px;right:64px;top:300px;padding:64px 60px;border-radius:52px",
                     f'<div style="font-size:30px;font-weight:700;letter-spacing:3px;opacity:.75">{n - 1:02d}</div>'
                     f'<div style="font-size:86px;font-weight:800;line-height:1.02;letter-spacing:-2.5px;margin-top:18px">{m(s["t"])}</div>'
                     f'<div style="font-size:42px;line-height:1.38;font-weight:500;margin-top:34px;opacity:.95">{m(s["x"])}</div>')
    corpo = mc.lg.fundo(v) + mc.lg.hd() + card
    corpo += '<div class="vidro seta" style="border-radius:40px;bottom:44px"><span style="position:relative;z-index:2">arrasta →</span></div>'
    corpo += f'<span style="position:absolute;left:64px;bottom:60px;z-index:6;font-size:24px;font-weight:700;opacity:.55">{n:02d}/07</span>'
    return f'<style>{mc.lg.CSS % {"raio": "var(--r,40px)"}}</style></head><body>{mc.lg.SVG_FILTRO}{corpo}</body>'


# ---------------------------------------------------------------- CTA
FEATS = ("CRM com funil de vendas", "IA que responde em segundos", "Follow-up automático no WhatsApp")


def cta(d, r):
    titulo, entregavel = r["cta"]
    kw = r["kw"]
    if r["fam"] == "glass":
        chips = "".join(mc._vidro("position:relative;display:inline-block;margin:0 14px 16px 0;padding:16px 26px;border-radius:30px",
                                  f'<span style="font-size:28px;font-weight:700">{t}</span>') for t in FEATS)
        corpo = (mc.lg.fundo(3) + mc.lg.hd()
                 + mc._vidro("left:64px;right:64px;top:210px;bottom:170px;border-radius:56px;padding:64px 60px",
                             f'<img src="{mc.lg.RAIO_B}" style="height:110px">'
                             f'<div style="font-size:80px;font-weight:800;line-height:1.04;letter-spacing:-2px;margin-top:30px">{m(titulo)}</div>'
                             f'<div style="margin-top:40px">{chips}</div>'
                             '<div style="margin-top:40px;padding:32px 38px;border-radius:999px;background:linear-gradient(135deg,rgba(250,204,21,.95),rgba(250,204,21,.8));color:#0F172A">'
                             f'<div style="font-size:46px;font-weight:800">Comenta {kw}</div>'
                             f'<div style="font-size:26px;font-weight:600;margin-top:6px">que eu te mando {html.escape(entregavel)} · 14 dias grátis</div></div>'))
        return f'<style>{mc.lg.CSS % {"raio": "var(--r,40px)"}}</style></head><body>{mc.lg.SVG_FILTRO}{corpo}</body>'
    escuro = r["fam"] in ("foto", "tweet")
    bg, txt, card, borda = (("#111827", "#fff", "rgba(255,255,255,.06)", "rgba(255,255,255,.14)") if escuro
                            else ("#F4F1EA" if r["fam"] == "noticia" else "#BBF7D0" if r["fam"] == "print" else "#FBF8F2", "#1B1820", "#fff", "#1B1820"))
    lista = "".join(f'<li style="font-size:38px;font-weight:700;padding:18px 0 18px 66px;position:relative;border-bottom:2px solid {borda}">'
                    '<span style="position:absolute;left:0;top:16px;width:46px;height:46px;border-radius:50%;background:#FACC15;color:#111827;'
                    f'font-size:28px;display:flex;align-items:center;justify-content:center">✓</span>{t}</li>' for t in FEATS)
    corpo = (f'<div style="position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center">'
             f'{logo(BRANCA if escuro else ESCURA)}<span style="font-size:26px;font-weight:700;opacity:.7">{HANDLE}</span></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:190px;bottom:150px;background:{card};border:{"2px" if escuro else "6px"} solid {borda};'
             f'border-radius:40px;padding:60px 56px;{"" if escuro else "box-shadow:14px 14px 0 #2563EB;"}display:flex;flex-direction:column">'
             f'<div style="font-size:84px;font-weight:800;line-height:1.04;letter-spacing:-2px">{m(titulo)}</div>'
             f'<div style="font-size:34px;font-weight:600;opacity:.75;margin-top:22px">Na SuaMarca você tem:</div>'
             f'<ul style="list-style:none;margin-top:18px">{lista}</ul>'
             '<div style="margin-top:auto;background:#2563EB;color:#fff;border-radius:28px;padding:34px 40px">'
             f'<div style="font-size:52px;font-weight:800">Comenta <span style="color:#FACC15">{kw}</span></div>'
             f'<div style="font-size:28px;font-weight:600;margin-top:8px;opacity:.95">que eu te mando {html.escape(entregavel)}.<br>14 dias grátis para testar.</div></div></div>')
    return (f'<style>{FONTES}*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1350px;overflow:hidden}}'
            f'body{{background:{bg};color:{txt};font-family:\'Plus Jakarta Sans\',sans-serif;position:relative}}b{{color:#2563EB}}</style></head><body>{corpo}</body>')


FAMILIA = {"noticia": noticia_int, "foto": foto_int, "tweet": tweet_int, "print": print_int, "tirinha": tirinha_int, "glass": glass_int}


def foto_png(doc_body, png):
    doc = f'<!doctype html><html><head><meta charset="utf-8">{doc_body}</html>'
    arq = png.with_suffix(".html")
    arq.write_text(doc, encoding="utf-8")
    for tentativa in range(4):
        r = subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--allow-file-access-from-files", "--force-device-scale-factor=1",
                            "--virtual-time-budget=8000", "--window-size=1080,1350", f"--screenshot={png}", arq.as_uri()], capture_output=True)
        if r.returncode == 0:
            break
    else:
        raise RuntimeError(f"Chrome falhou em {png}")
    arq.unlink()


def montar(d):
    r = R[d]
    pasta = AQUI / f"{d}_{r['kw']}"
    pasta.mkdir(exist_ok=True)
    capa = next((CAPAS / "capas").glob(f"capa_{d}_*.png"))
    shutil.copy(capa, pasta / "slide_01.png")
    for k, s in enumerate(r["slides"], 2):
        foto_png(FAMILIA[r["fam"]](d, k, s), pasta / f"slide_{k:02d}.png")
    foto_png(cta(d, r), pasta / "slide_07.png")
    (pasta / "legenda.txt").write_text(r["legenda"] + "\n", encoding="utf-8")
    return f"OK {pasta.name}"


if __name__ == "__main__":
    dias = sys.argv[1:] or sorted(R)
    with ThreadPoolExecutor(4) as ex:
        for linha in ex.map(montar, dias):
            print(linha)
