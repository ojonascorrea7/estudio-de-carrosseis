"""Capas dos 24 carrosséis de 07 a 30/11/2026, em 6 layouts:
TIRINHA, NOTICIA, TWEET, FOTO, PRINT e DADOS.
Uso: python3 montar_capas.py          -> todas em capas/capa_DD_PALAVRA.png
     python3 montar_capas.py 07 13    -> só os dias informados
Marcação: **x** = destaque (amarelo ou roxo conforme o layout)."""
import html, importlib.util, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HANDLE = "@seuperfil"


def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


tir = carregar("tir", BASE / "personagem" / "montar_tirinha_cor.py")
eev = carregar("eev", BASE / "carrossel_empresa_e_voce" / "montar.py")
fdp = carregar("fdp", BASE / "carrossel_fome_de_poder" / "montar.py")
TRACO, txt, PAREDE = tir.TRACO, eev.txt, eev.PAREDE
AVATAR = (BASE / "frases_tweet" / "avatar.jpg").as_uri()
FONTES = ("@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800"
          "&family=Playfair+Display:wght@800;900&display=swap');")
MARCA = '<span class="marca"><i>Sua</i><b>Marca</b></span>'


def marcar(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(t))


# =====================================================================
# TIRINHA: cenários próprios de cada tema
# =====================================================================
def c_brinde():
    """Coqueteleira com a marca na prateleira (fica 1 ano) × tela de anúncio R$ 4 com lead esquecido."""
    shaker = (f'<rect x="60" y="640" width="320" height="20" fill="#B9865A" stroke="{TRACO}" stroke-width="6"/>'
              f'<path d="M150 640 l-14 -170 h128 l-14 170z" fill="#2563EB" stroke="{TRACO}" stroke-width="6"/>'
              f'<rect x="146" y="430" width="108" height="44" rx="8" fill="#2A2320" stroke="{TRACO}" stroke-width="5"/>'
              f'<rect x="182" y="404" width="36" height="30" rx="6" fill="#2A2320"/>'
              + txt(200, 560, "SUA", 26, "#fff") + txt(200, 592, "MARCA", 26, "#FACC15")
              + f'<g transform="rotate(-6 300 520)"><rect x="250" y="490" width="120" height="58" rx="8" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>'
              + txt(310, 516, "1 ano", 22) + txt(310, 540, "na cozinha", 16, peso=700) + '</g>')
    tela = (f'<rect x="640" y="420" width="390" height="270" rx="14" fill="#fff" stroke="{TRACO}" stroke-width="7"/>'
            f'<rect x="640" y="420" width="390" height="50" rx="14" fill="#E9E6F7" stroke="{TRACO}" stroke-width="7"/>'
            + txt(835, 455, "Gerenciador de anúncios", 20)
            + txt(835, 530, "Custo por clique", 22, "#6B6475", peso=700)
            + txt(835, 590, "R$ 4,00", 56, "#E5484D")
            + f'<rect x="680" y="615" width="310" height="50" rx="10" fill="#FBF8F2" stroke="{TRACO}" stroke-width="4"/>'
            + txt(835, 648, "lead sem resposta há 2 dias", 18, peso=700)
            + f'<rect x="805" y="690" width="60" height="70" fill="#C99A6B" stroke="{TRACO}" stroke-width="6"/>')
    return PAREDE + shaker + tela + tir.piso()


def c_planilhas():
    """Três planilhas coladas na parede, cada uma com um número diferente, e pontos de interrogação."""
    def planilha(x, y, ang, valor):
        cel = "".join(f'<line x1="{x}" y1="{y+40+k*34}" x2="{x+220}" y2="{y+40+k*34}" stroke="#CFCAC2" stroke-width="3"/>' for k in range(5))
        cel += "".join(f'<line x1="{x+k*73}" y1="{y+40}" x2="{x+k*73}" y2="{y+210}" stroke="#CFCAC2" stroke-width="3"/>' for k in (1, 2))
        return (f'<g transform="rotate({ang} {x+110} {y+110})"><rect x="{x}" y="{y}" width="220" height="210" fill="#fff" stroke="{TRACO}" stroke-width="5"/>'
                f'<rect x="{x}" y="{y}" width="220" height="40" fill="#7DAE5E" stroke="{TRACO}" stroke-width="5"/>{cel}'
                + txt(x + 110, y + 150, valor, 36, "#E5484D") + '</g>')
    pins = "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#E5484D" stroke="{TRACO}" stroke-width="3"/>' for x, y in ((170, 412), (520, 432), (870, 412)))
    interroga = "".join(txt(x, y, "?", t, "#2563EB") for x, y, t in ((330, 690, 120), (720, 700, 110), (1010, 720, 90)))
    return (PAREDE + planilha(60, 420, -5, "R$ 48 mil?") + planilha(410, 440, 3, "R$ 61 mil?")
            + planilha(760, 420, -3, "R$ 39 mil?") + pins + interroga + tir.piso())


def c_feriado():
    """Calendário com 20 NOV FERIADO, placa FECHADO na porta e celular lotado de clientes chamando."""
    cal = (f'<rect x="70" y="420" width="250" height="270" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="7"/>'
           f'<rect x="70" y="420" width="250" height="70" rx="10" fill="#E5484D" stroke="{TRACO}" stroke-width="7"/>'
           + txt(195, 468, "NOVEMBRO", 28, "#fff") + txt(195, 600, "20", 110) + txt(195, 660, "FERIADO", 28, "#E5484D")
           + "".join(f'<circle cx="{x}" cy="414" r="10" fill="{TRACO}"/>' for x in (130, 260)))
    porta = (f'<rect x="700" y="400" width="300" height="580" rx="6" fill="#B9865A" stroke="{TRACO}" stroke-width="7"/>'
             f'<path d="M850 430 l-70 50 M850 430 l70 50" stroke="{TRACO}" stroke-width="4"/>'
             f'<g transform="rotate(5 850 540)"><rect x="755" y="480" width="190" height="100" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
             + txt(850, 540, "FECHADO", 36, "#E5484D") + '</g>'
             + f'<circle cx="725" cy="720" r="12" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>')
    balao = "".join(f'<g transform="rotate({a} {x} {y})"><rect x="{x-80}" y="{y-26}" width="160" height="52" rx="26" fill="#BBF7D0" stroke="{TRACO}" stroke-width="4"/>'
                    + txt(x, y + 8, t, 20) + '</g>'
                    for x, y, a, t in ((470, 780, -4, "tá aberto?"), (420, 860, 3, "quero agendar"), (560, 900, -2, "qual valor?")))
    return PAREDE + cal + porta + tir.piso() + balao


def c_antes_depois():
    """Parede dividida: ANTES (noite, 23:47, papelada) e DEPOIS (dia, 18:00, tudo em ordem)."""
    esq = ('<rect width="540" height="1350" fill="#E4E0EE"/>' + eev.janela_noite(x=80, y=430, hora="23:47")
           + "".join(f'<rect x="{60 + d}" y="{830 - 16*(k+1)}" width="110" height="16" fill="#fff" stroke="{TRACO}" stroke-width="3" '
                     f'transform="rotate({(-1)**k*4} 115 {820 - 16*k})"/>' for k, d in enumerate((0, 5, -4, 6, -3, 2, 0, 4))))
    dir_ = ('<rect x="540" width="540" height="1350" fill="#FBF8F2"/>' + eev.janela_dia(x=780, y=430)
            + f'<rect x="830" y="700" width="160" height="110" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="5"/>'
            + txt(910, 745, "18:00", 34) + txt(910, 785, "fui pra casa", 20, "#7DAE5E"))
    tags = (f'<rect x="60" y="370" width="170" height="52" rx="10" fill="#2A2320"/>' + txt(145, 406, "ANTES", 28, "#fff")
            + f'<rect x="850" y="370" width="180" height="52" rx="10" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>' + txt(940, 406, "DEPOIS", 28))
    return esq + dir_ + f'<line x1="540" y1="0" x2="540" y2="980" stroke="{TRACO}" stroke-width="6" stroke-dasharray="18 14"/>'.replace('y1="0"', 'y1="360"') + tir.piso() + tags


def c_sabado():
    """Sábado de sol: celular grande com 500 conversas e a IA respondendo todas."""
    sol = eev.janela_dia(x=80, y=430)
    cal = (f'<rect x="90" y="700" width="180" height="120" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="5"/>'
           + txt(180, 750, "SÁBADO", 28, "#2563EB") + txt(180, 795, "de Black", 24))
    linhas = ""
    for k, (nome, msg) in enumerate((("Carla", "tem no tamanho M?"), ("Rafael", "parcela em 10x?"), ("Bruna", "entrega amanhã?"))):
        y = 500 + k * 72
        linhas += (f'<circle cx="700" cy="{y+28}" r="22" fill="#2563EB"/>' + txt(700, y + 36, nome[0], 22, "#fff")
                   + txt(735, y + 24, nome, 21, meio=False) + txt(735, y + 50, msg, 17, "#6B6475", meio=False, peso=600)
                   + f'<rect x="910" y="{y+8}" width="100" height="34" rx="17" fill="#BBF7D0" stroke="{TRACO}" stroke-width="3"/>'
                   + txt(960, y + 31, "IA ✓", 17))
    cel = (f'<rect x="660" y="400" width="380" height="440" rx="34" fill="#fff" stroke="{TRACO}" stroke-width="8"/>'
           f'<path d="M660 434 q0 -34 34 -34 h312 q34 0 34 34 v40 h-380z" fill="#BBF7D0" stroke="{TRACO}" stroke-width="8"/>'
           + txt(850, 460, "500 conversas", 26) + linhas
           + f'<rect x="690" y="730" width="320" height="60" rx="14" fill="#2563EB" stroke="{TRACO}" stroke-width="4"/>'
           + txt(850, 768, "🤖 IA respondendo todas", 22, "#fff"))
    return PAREDE + sol + tir.piso() + cal + cel


def c_dms():
    """Quem bota a cara: tripé com ring light gravando e celular explodindo de DMs sem resposta."""
    ring = (f'<line x1="200" y1="700" x2="140" y2="975" stroke="{TRACO}" stroke-width="7"/><line x1="200" y1="700" x2="260" y2="975" stroke="{TRACO}" stroke-width="7"/>'
            f'<line x1="200" y1="560" x2="200" y2="720" stroke="{TRACO}" stroke-width="8"/>'
            f'<circle cx="200" cy="500" r="95" fill="none" stroke="#FFF6C9" stroke-width="34"/><circle cx="200" cy="500" r="95" fill="none" stroke="{TRACO}" stroke-width="5"/>'
            f'<circle cx="200" cy="500" r="112" fill="none" stroke="{TRACO}" stroke-width="5"/>'
            f'<rect x="175" y="455" width="50" height="90" rx="8" fill="#3A3442" stroke="{TRACO}" stroke-width="4"/><circle cx="200" cy="472" r="6" fill="#E5484D"/>'
            + txt(200, 640, "● REC", 22, "#E5484D"))
    dms = ""
    for k, (n, m) in enumerate((("ana.estetica", "quanto custa?"), ("marcos_bjj", "atende minha cidade?"), ("loja.bela", "tem parceria?"), ("dra.carla", "como funciona?"))):
        y = 470 + k * 66
        dms += (f'<circle cx="720" cy="{y+28}" r="22" fill="#FACC15" stroke="{TRACO}" stroke-width="3"/>'
                + txt(752, y + 24, n, 19, meio=False) + txt(752, y + 50, m, 17, "#6B6475", meio=False, peso=600)
                + f'<circle cx="1000" cy="{y+30}" r="9" fill="#2563EB"/>')
    cel = (f'<rect x="680" y="400" width="360" height="400" rx="34" fill="#fff" stroke="{TRACO}" stroke-width="8"/>'
           + txt(860, 450, "Directs", 26) + dms
           + f'<rect x="710" y="740" width="300" height="44" rx="12" fill="#E5484D"/>' + txt(860, 770, "300 sem resposta", 22, "#fff")
           + f'<circle cx="1030" cy="404" r="34" fill="#E5484D" stroke="{TRACO}" stroke-width="5"/>' + txt(1030, 414, "300", 22, "#fff"))
    return PAREDE + tir.piso() + ring + cel


CENAS = {"brinde": c_brinde, "planilhas": c_planilhas, "feriado": c_feriado, "antes_depois": c_antes_depois, "sabado": c_sabado, "dms": c_dms}


def tirinha(c):
    fs = c.get("fs", 54)
    vars_ = {"fs": fs, "bw": 860, "bx": 110, "cauda": 400, "incl": 15}
    svg = f'<svg class="cena" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{CENAS[c["cena"]]()}</svg>'
    hd = f'<div class="hd">{MARCA}<span class="arroba">{HANDLE}</span></div>'
    if c["expr"] == "corpo":
        linhas = c["texto"].count("\n") + 1
        img, _ = tir.personagem("corpo", 110 + 64 + linhas * fs * 1.15 + 80)
    else:
        img, _ = tir.personagem(c["expr"], 0)
    rod = f'<div class="capa-tag">{html.escape(c["tag"])}</div><div class="seta">arrasta →</div>'
    corpo = f'{hd}<div class="bal" style="top:110px">{tir.marcar(c["texto"])}</div>{img}{rod}'
    return f'<style>{eev.FONTE}{tir.CSS % vars_}{eev.CSS_EXTRA}</style></head><body>{svg}{corpo}</body>'


# =====================================================================
# NOTICIA: página de jornal da própria marca (sem imitar veículo real)
# =====================================================================
CSS_NOT = """
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#F4F1EA;font-family:'Plus Jakarta Sans',sans-serif;color:#1B1820;position:relative}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.marca{font-size:34px;letter-spacing:-.5px}.marca i{font-style:normal;font-weight:500}.marca b{font-weight:800}
.arroba{font-size:26px;font-weight:700;color:#6B6475}
.jornal{position:absolute;top:120px;left:64px;right:64px;border-top:6px solid #1B1820;border-bottom:2px solid #1B1820;padding:14px 0;
 display:flex;justify-content:space-between;font-size:22px;font-weight:800;letter-spacing:3px}
.tag{display:inline-block;margin-top:60px;background:#E5484D;color:#fff;font-size:26px;font-weight:800;letter-spacing:3px;padding:10px 20px}
.box{position:absolute;top:190px;left:64px;right:64px}
h1{font-family:'Playfair Display',serif;font-weight:900;font-size:%(fs)spx;line-height:1.06;letter-spacing:-1px;margin-top:26px}
h1 b{background:linear-gradient(transparent 62%%,#FACC15 62%%);font-weight:900}
.sub{margin-top:28px;font-size:36px;line-height:1.35;font-weight:600;color:#3A3442;border-left:8px solid #2563EB;padding-left:24px}
.ilus{position:absolute;left:64px;right:64px;bottom:130px;height:%(ih)spx}
.rod{position:absolute;left:64px;right:64px;bottom:50px;display:flex;justify-content:space-between;align-items:center;font-size:20px;color:#6B6475;font-weight:600}
.seta{font-size:26px;font-weight:800;color:#1B1820;background:#FACC15;border:4px solid #1B1820;border-radius:40px;padding:10px 24px}
"""


def ilus_bebida():
    garrafa = lambda x, ang: (f'<g transform="rotate({ang} {x} 300)"><path d="M{x-45} 330 v-150 q0 -40 30 -60 v-50 h30 v50 q30 20 30 60 v150z" fill="#2F7BF5" stroke="#1B1820" stroke-width="6"/>'
                              f'<path d="M{x-25} 70 l25 -70 l25 70z" fill="#E5484D" stroke="#1B1820" stroke-width="5"/>'
                              f'<rect x="{x-35}" y="220" width="70" height="60" rx="6" fill="#fff" stroke="#1B1820" stroke-width="4"/></g>')
    return (f'<svg viewBox="0 0 952 330" width="952" height="330">'
            f'<rect x="0" y="300" width="952" height="30" fill="#1B1820"/>'
            + garrafa(180, -8) + garrafa(330, 0) + garrafa(480, 6)
            + f'<g><rect x="600" y="90" width="320" height="180" rx="20" fill="#fff" stroke="#1B1820" stroke-width="5"/>'
            + txt(760, 150, "nome curto", 30, "#1B1820") + txt(760, 195, "cor que ninguém usa", 26, "#2563EB")
            + txt(760, 240, "um personagem", 26, "#E5484D") + '</g></svg>')


def ilus_sac():
    return (f'<svg viewBox="0 0 952 330" width="952" height="330">'
            f'<rect x="20" y="40" width="420" height="250" rx="24" fill="#fff" stroke="#1B1820" stroke-width="6"/>'
            + txt(230, 100, "ATENDIMENTO", 26, extra="letter-spacing:3px")
            + f'<circle cx="140" cy="190" r="56" fill="#BBF7D0" stroke="#1B1820" stroke-width="5"/>' + txt(140, 210, "🧑", 56)
            + txt(140, 275, "humano", 22) + txt(230, 205, "+", 50, "#2563EB")
            + f'<circle cx="320" cy="190" r="56" fill="#E9E6F7" stroke="#1B1820" stroke-width="5"/>' + txt(320, 210, "🤖", 56)
            + txt(320, 275, "IA", 22)
            + f'<rect x="500" y="80" width="430" height="170" rx="24" fill="#1B1820"/>'
            + txt(715, 160, "8h → 20h", 74, "#FACC15") + txt(715, 215, "todos os dias", 28, "#fff", peso=600) + '</svg>')


def ilus_favela():
    casas = ""
    cores = ["#FACC15", "#2563EB", "#BBF7D0", "#E5484D", "#F4A259", "#7DAE5E", "#fff", "#2563EB", "#FACC15"]
    for k, cor in enumerate(cores):
        x = 10 + k * 104
        h = 140 + (k * 47) % 120
        casas += (f'<rect x="{x}" y="{300-h}" width="96" height="{h}" fill="{cor}" stroke="#1B1820" stroke-width="5"/>'
                  f'<rect x="{x+18}" y="{300-h+24}" width="26" height="26" fill="#CFE3F5" stroke="#1B1820" stroke-width="3"/>'
                  f'<rect x="{x+52}" y="{300-h+24}" width="26" height="26" fill="#CFE3F5" stroke="#1B1820" stroke-width="3"/>')
    placas = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="6" fill="#1B1820"/>' + txt(x + w / 2, y + 24, t, 18, "#fff")
                     for x, y, w, t in ((20, 250, 180, "SALÃO DA JU"), (330, 250, 190, "MARMITA DA TIA"), (650, 250, 200, "CONSERTO CEL")))
    return f'<svg viewBox="0 0 952 330" width="952" height="330"><rect x="0" y="300" width="952" height="30" fill="#1B1820"/>{casas}{placas}</svg>'


def ilus_views():
    return (f'<svg viewBox="0 0 952 330" width="952" height="330">'
            f'<rect x="10" y="40" width="560" height="260" rx="24" fill="#1B1820"/>'
            + txt(290, 105, "VISUALIZAÇÕES EM 7 DIAS", 24, "#fff", extra="letter-spacing:3px")
            + txt(290, 205, "2 bilhões", 96, "#FACC15") + txt(290, 260, "▲ comemorado pela empresa", 24, "#BBF7D0", peso=700)
            + f'<rect x="610" y="40" width="330" height="260" rx="24" fill="#fff" stroke="#1B1820" stroke-width="6"/>'
            + txt(775, 105, "VENDAS", 24, extra="letter-spacing:3px") + txt(775, 220, "?", 130, "#E5484D") + '</svg>')


ILUS = {"bebida": ilus_bebida, "sac": ilus_sac, "favela": ilus_favela, "views": ilus_views}


def noticia(c):
    css = CSS_NOT % {"fs": c.get("fs", 80), "ih": 330}
    corpo = (f'<div class="hd">{MARCA}<span class="arroba">{HANDLE}</span></div>'
             f'<div class="jornal"><span>PLANTÃO DO EMPRESÁRIO</span><span>{c["data"]}</span></div>'
             f'<div class="box"><span class="tag">{c["tag"]}</span><h1>{marcar(c["titulo"])}</h1>'
             f'<div class="sub">{marcar(c["sub"])}</div></div>'
             f'<div class="ilus">{ILUS[c["ilus"]]()}</div>'
             f'<div class="rod"><span>{html.escape(c["fonte"])}</span><span class="seta">arrasta →</span></div>')
    return f'<style>{FONTES}{css}</style></head><body>{corpo}</body>'


# =====================================================================
# TWEET
# =====================================================================
CSS_TW = """
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:%(bg)s;font-family:-apple-system,'SF Pro Text','Helvetica Neue',Arial,sans-serif;position:relative;
 display:flex;align-items:center;justify-content:center}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;color:%(txt)s;font-family:'Plus Jakarta Sans',sans-serif}
.marca{font-size:34px;letter-spacing:-.5px}.marca i{font-style:normal;font-weight:500}.marca b{font-weight:800}
.arroba{font-size:26px;font-weight:700;color:%(sub)s}
.card{width:936px;background:%(card)s;border:1px solid %(borda)s;border-radius:36px;padding:56px 60px 48px;box-shadow:0 30px 60px -36px rgba(0,0,0,.35)}
.top{display:flex;align-items:center;gap:22px}.av{width:104px;height:104px;border-radius:50%%;object-fit:cover}
.nm{font-size:38px;font-weight:700;color:%(txt)s}.hh{font-size:31px;color:%(sub)s;margin-top:2px}
.tx{margin-top:40px;font-size:%(fs)spx;line-height:1.26;color:%(txt)s;letter-spacing:-.6px;white-space:pre-line;font-weight:500}
.tx b{font-weight:800;color:%(dest)s}
.rod{margin-top:44px;padding-top:28px;border-top:1px solid %(borda)s;display:flex;justify-content:space-between;font-size:26px;color:%(sub)s}
.seta{position:absolute;right:64px;bottom:50px;font-family:'Plus Jakarta Sans',sans-serif;font-size:26px;font-weight:800;color:#1B1820;
 background:#FACC15;border:4px solid #1B1820;border-radius:40px;padding:10px 24px}
"""
TEMAS = {"claro": dict(bg="#F2F2F2", card="#FFFFFF", txt="#0F1419", sub="#536471", borda="#E6E6E6", dest="#2563EB"),
         "escuro": dict(bg="#111827", card="#211C2B", txt="#F5F4F8", sub="#9B95A8", borda="#2E283A", dest="#FACC15")}


def tweet(c):
    css = CSS_TW % dict(TEMAS[c["tema"]], fs=c.get("fs", 66))
    corpo = (f'<div class="hd">{MARCA}<span class="arroba">{HANDLE}</span></div><div class="card">'
             f'<div class="top"><img class="av" src="{AVATAR}"><div><div class="nm">Seu Nome</div><div class="hh">{HANDLE}</div></div></div>'
             f'<div class="tx">{marcar(c["texto"])}</div>'
             f'<div class="rod"><span>{c["rodape"]}</span><span>💬 🔁 ❤️</span></div></div><span class="seta">arrasta →</span>')
    return f'<style>{FONTES}{css}</style></head><body>{corpo}</body>'


# =====================================================================
# FOTO (reaproveita o visual Fome de Poder)
# =====================================================================
def foto(c):
    s = dict(tipo="foto", capa=True, **c["slide"])
    body = fdp.montar(s)
    if c.get("split"):  # duas fotos lado a lado
        u1 = (BASE / "carrossel_fome_de_poder" / "fotos" / c["split"][0]).as_uri()
        u2 = (BASE / "carrossel_fome_de_poder" / "fotos" / c["split"][1]).as_uri()
        body = re.sub(r'<div class="foto"[^>]*></div>',
                      f'<div class="foto" style="right:50%;background-image:url(\'{u1}\');background-position:50% 20%"></div>'
                      f'<div class="foto" style="left:50%;background-image:url(\'{u2}\');background-position:30% 50%"></div>'
                      '<div class="vs">VS</div>', body)
    extra = (".vs{position:absolute;left:50%;top:430px;transform:translateX(-50%);z-index:2;width:130px;height:130px;border-radius:50%;"
             "background:#FACC15;color:#111827;font-size:54px;font-weight:800;display:flex;align-items:center;justify-content:center;border:6px solid #111827}"
             ".foto+.foto{border-left:6px solid #111827}")
    return f'<style>{fdp.CSS}{extra}</style></head>{body}'


# =====================================================================
# PRINT de WhatsApp
# =====================================================================
CSS_PR = """
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#BBF7D0;font-family:'Plus Jakarta Sans',sans-serif;color:#1B1820;position:relative}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.marca{font-size:34px;letter-spacing:-.5px}.marca i{font-style:normal;font-weight:500}.marca b{font-weight:800}
.arroba{font-size:26px;font-weight:700;color:#3A6B55}
h1{position:absolute;top:130px;left:64px;right:64px;font-size:%(fs)spx;line-height:1.06;font-weight:800;letter-spacing:-1.5px;white-space:pre-line}
h1 b{color:#2563EB}
.sub{display:block;margin-top:18px;font-size:36px;font-weight:600;letter-spacing:0;color:#2F5546}
.cel{position:absolute;left:150px;right:150px;top:%(ct)spx;bottom:-60px;background:#EFE7DD;border:10px solid #1B1820;border-radius:60px 60px 0 0;overflow:hidden}
.bar{background:#1F7A5C;color:#fff;padding:30px 34px 22px;display:flex;align-items:center;gap:18px;font-size:28px;font-weight:700}
.bar .av{width:60px;height:60px;border-radius:50%%;background:#FACC15;color:#1B1820;display:flex;align-items:center;justify-content:center;font-weight:800}
.bar small{display:block;font-size:20px;font-weight:500;opacity:.85}
.msgs{padding:24px 28px;display:flex;flex-direction:column;gap:16px}
.m{max-width:78%%;padding:16px 20px 26px;border-radius:18px;font-size:29px;line-height:1.3;font-weight:500;position:relative;box-shadow:0 2px 0 rgba(0,0,0,.08)}
.m small{position:absolute;right:14px;bottom:6px;font-size:17px;color:#6B6475}
.m.ele{background:#fff;align-self:flex-start;border-top-left-radius:4px}
.m.eu{background:#D9FDD3;align-self:flex-end;border-top-right-radius:4px}
.sep{align-self:center;background:#FFF6C9;color:#5E5530;font-size:21px;font-weight:700;padding:8px 18px;border-radius:12px}
.lista .it{display:flex;align-items:center;gap:16px;padding:14px 0;border-bottom:2px solid #E2D9CC}
.lista .ci{width:58px;height:58px;border-radius:50%%;background:#2563EB;color:#fff;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center}
.lista .nm{flex:1;font-size:26px;font-weight:700}.lista .nm small{display:block;font-size:21px;font-weight:500;color:#6B6475}
.lista .bd{background:#9B95A8;color:#fff;font-size:18px;font-weight:800;padding:6px 12px;border-radius:14px}
.seta{position:absolute;right:64px;bottom:50px;z-index:3;font-size:26px;font-weight:800;color:#1B1820;background:#FACC15;border:4px solid #1B1820;border-radius:40px;padding:10px 24px}
"""


def print_(c):
    css = CSS_PR % {"fs": c.get("fs", 74), "ct": c.get("ct", 520)}
    if c.get("lista"):
        itens = "".join(f'<div class="it"><div class="ci">{n[0]}</div><div class="nm">{n}<small>{m}</small></div><span class="bd">{b}</span></div>'
                        for n, m, b in c["lista"])
        miolo = f'<div class="msgs lista">{itens}</div>'
    else:
        partes = []
        for quem, t, h in c["msgs"]:
            partes.append(f'<div class="sep">{t}</div>' if quem == "sep" else f'<div class="m {quem}">{html.escape(t)}<small>{h}</small></div>')
        miolo = f'<div class="msgs">{"".join(partes)}</div>'
    corpo = (f'<div class="hd">{MARCA}<span class="arroba">{HANDLE}</span></div>'
             f'<h1>{marcar(c["titulo"])}<span class="sub">{marcar(c["sub"])}</span></h1>'
             f'<div class="cel"><div class="bar"><div class="av">{c["contato"][0]}</div><div>{c["contato"]}<small>{c["status"]}</small></div></div>{miolo}</div>'
             '<span class="seta">arrasta →</span>')
    return f'<style>{FONTES}{css}</style></head><body>{corpo}</body>'


# =====================================================================
# DADOS: card escuro com número grande
# =====================================================================
CSS_DD = """
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:radial-gradient(900px 700px at 100%% 0%%,rgba(37,99,235,.4),transparent 60%%),%(bg)s;font-family:'Plus Jakarta Sans',sans-serif;color:#fff;position:relative}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.marca{font-size:34px;letter-spacing:-.5px}.marca i{font-style:normal;font-weight:500}.marca b{font-weight:800}
.arroba{font-size:26px;font-weight:700;opacity:.8}
.box{position:absolute;left:64px;right:64px;top:170px;bottom:150px;display:flex;flex-direction:column;justify-content:center}
.chapeu{align-self:flex-start;font-size:26px;font-weight:800;letter-spacing:3px;background:#2563EB;padding:10px 20px;border-radius:8px}
.num{font-size:%(ns)spx;font-weight:800;letter-spacing:-6px;line-height:1;color:#FACC15;margin-top:30px}
.num s{color:rgba(255,255,255,.4);text-decoration-thickness:10px;font-size:.55em;letter-spacing:-2px;margin-right:24px}
h1{font-size:%(fs)spx;line-height:1.1;font-weight:800;letter-spacing:-1.5px;margin-top:30px;white-space:pre-line}
h1 b{color:#FACC15}
.vis{margin-top:44px}
.dias{display:flex;gap:18px}.dias div{flex:1;background:#fff;color:#111827;border-radius:18px;padding:18px 0;text-align:center;font-size:24px;font-weight:700;box-shadow:8px 8px 0 #2563EB}
.dias div b{display:block;font-size:66px;color:#111827}
.chk{display:grid;grid-template-columns:1fr 1fr;gap:14px 30px;font-size:28px;font-weight:600;opacity:.9}
.chk span:before{content:'';display:inline-block;width:30px;height:30px;border:4px solid #FACC15;border-radius:6px;margin-right:14px;vertical-align:-6px}
.barras{display:flex;align-items:flex-end;gap:16px;height:150px}.barras i{flex:1;background:rgba(255,255,255,.18);border-radius:10px 10px 0 0}
.barras i.f{background:#FACC15}
.oferta{display:flex;gap:16px;flex-wrap:wrap}.oferta span{font-size:30px;font-weight:800;border:3px solid #FACC15;color:#FACC15;border-radius:40px;padding:12px 26px}
.rod{position:absolute;left:64px;right:64px;bottom:50px;display:flex;justify-content:space-between;align-items:center;font-size:20px;opacity:.85}
.seta{font-size:26px;font-weight:800;color:#111827;background:#FACC15;border-radius:40px;padding:12px 26px}
"""


def dados(c):
    css = CSS_DD % {"bg": c.get("bg", "#111827"), "ns": c.get("ns", 210), "fs": c.get("fs", 64)}
    num = f'<div class="num">{c["num"]}</div>' if c.get("num") else ""
    corpo = (f'<div class="hd">{MARCA}<span class="arroba">{HANDLE}</span></div>'
             f'<div class="box"><span class="chapeu">{c["chapeu"]}</span>{num}<h1>{marcar(c["titulo"])}</h1>'
             f'<div class="vis">{c.get("vis", "")}</div></div>'
             f'<div class="rod"><span>{html.escape(c.get("fonte", ""))}</span><span class="seta">arrasta →</span></div>')
    return f'<style>{FONTES}{css}</style></head><body>{corpo}</body>'


# =====================================================================
# LIQUID GLASS (fundo futurista transparente aprovado em 05/11)
# =====================================================================
lg = carregar("lg", BASE / "referencias_layout" / "liquid_glass" / "montar.py")
lg.TEMA = "futurista"


def _vidro(estilo, miolo, extra=""):
    return f'<div class="vidro" style="{estilo}"{extra}><div style="position:relative;z-index:2">{miolo}</div></div>'


def liquid(c):
    v = c.get("variante", 1)
    corpo = lg.fundo(v) + lg.hd() + c["miolo"]()
    corpo += '<div class="vidro seta" style="border-radius:40px;bottom:44px"><span style="position:relative;z-index:2">arrasta →</span></div>'
    return f'<style>{lg.CSS % {"raio": "var(--r,40px)"}}</style></head><body>{lg.SVG_FILTRO}{corpo}</body>'


TIT = 'position:absolute;left:64px;right:64px;z-index:3;text-shadow:0 4px 30px rgba(0,0,30,.35)'
CHAP = '<div style="font-size:28px;font-weight:700;letter-spacing:3px;opacity:.85">{}</div>'


def lg_calendario():
    dias = "".join(_vidro(f"position:relative;flex:1;padding:34px 0 30px;border-radius:34px;text-align:center",
                          f'<div style="font-size:96px;font-weight:800;letter-spacing:-3px;line-height:1">{d}</div>'
                          f'<div style="font-size:26px;font-weight:600;opacity:.8;margin-top:8px">{w}</div>'
                          f'<div style="font-size:44px;font-weight:800;color:#FACC15;margin-top:14px">?</div>')
                   for d, w in (("26", "quinta"), ("27", "sexta"), ("28", "sábado"), ("29", "domingo")))
    return (f'<div style="{TIT};top:250px">' + CHAP.format("BLACK FRIDAY · 26 A 29/11")
            + '<div style="font-size:104px;font-weight:800;line-height:1;letter-spacing:-3px;margin-top:22px">O que mandar<br>em <b>cada dia</b><br>da Black.</div></div>'
            f'<div style="position:absolute;left:64px;right:64px;top:820px;display:flex;gap:18px;z-index:3">{dias}</div>')


def lg_checklist():
    itens = [("Resposta automática fora do horário", True), ("Estoque e preço no catálogo", True), ("Link de pagamento pronto", False),
             ("Mensagem de pós-venda", False), ("Lista de quem não comprou", False)]
    linhas = "".join(f'<div style="display:flex;align-items:center;gap:22px;padding:18px 0;border-top:1px solid rgba(255,255,255,{0 if k == 0 else .14})">'
                     f'<span style="width:44px;height:44px;border-radius:12px;flex:none;border:3px solid {"#FACC15" if ok else "rgba(255,255,255,.6)"};'
                     f'background:{"#FACC15" if ok else "transparent"};color:#0F172A;font-size:30px;font-weight:900;display:flex;align-items:center;justify-content:center">{"✓" if ok else ""}</span>'
                     f'<span style="font-size:32px;font-weight:600">{t}</span></div>' for k, (t, ok) in enumerate(itens))
    return (f'<div style="{TIT};top:190px">' + CHAP.format("AMANHÃ É BLACK FRIDAY")
            + '<div style="font-size:92px;font-weight:800;line-height:1.02;letter-spacing:-2.5px;margin-top:20px">Checklist de <b>10 itens</b><br>do seu atendimento.</div></div>'
            + _vidro("left:64px;right:64px;top:600px;padding:26px 44px;border-radius:44px", linhas
                     + '<div style="font-size:26px;font-weight:700;opacity:.7;padding-top:10px">+ 5 itens no carrossel · salva esse</div>'))


def lg_black():
    chips = "".join(_vidro("position:relative;display:inline-block;margin:0 14px 16px 0;padding:18px 30px;border-radius:40px",
                           f'<span style="font-size:32px;font-weight:800">{t}</span>') for t in ("15% OFF", "14 dias grátis", "2 meses grátis no anual"))
    return (f'<div style="{TIT};top:200px">' + CHAP.format("SEXTA · 27/11")
            + '<div style="font-size:190px;font-weight:900;line-height:.9;letter-spacing:-7px;margin-top:24px">BLACK<br>FRIDAY</div></div>'
            + _vidro("left:64px;right:64px;top:760px;padding:44px 48px;border-radius:48px",
                     '<div style="font-size:60px;font-weight:800;line-height:1.08;letter-spacing:-1.5px">Hoje é Black Friday.<br>E a SuaMarca <b>também entrou</b>.</div>'
                     f'<div style="margin-top:34px">{chips}</div>'))


def lg_agente():
    def n(nome, txt, hora, y):
        return _vidro(f"left:96px;right:96px;top:{y}px;padding:24px 30px;border-radius:36px",
                      '<div style="display:flex;gap:22px;align-items:center">'
                      '<div style="width:74px;height:74px;border-radius:20px;background:#2563EB;display:flex;align-items:center;justify-content:center;font-size:38px;flex:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.5)">🤖</div>'
                      f'<div style="flex:1"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:700"><span>IA respondeu {nome}</span><span style="opacity:.7;font-weight:500">{hora}</span></div>'
                      f'<div style="font-size:27px;margin-top:4px;opacity:.9">{txt}</div></div></div>')
    return (f'<div style="{TIT};top:170px;text-align:center"><div style="font-size:34px;font-weight:600;opacity:.9">sábado de Black</div>'
            '<div style="font-size:160px;font-weight:800;letter-spacing:-6px;line-height:1;margin-top:6px">500</div>'
            '<div style="font-size:34px;font-weight:600;opacity:.9">mensagens desde as 8h</div></div>'
            + n("Carla", "tem no M, sim! Te mando o link do pix 😉", "agora", 510)
            + n("Rafael", "parcela em até 10x sem juros. Fechamos?", "1 min", 650)
            + n("Bruna", "entrega amanhã no seu CEP ✅", "2 min", 790)
            + _vidro("left:64px;right:64px;top:960px;padding:34px 40px;border-radius:44px;background:linear-gradient(135deg,rgba(15,23,42,.82),rgba(15,23,42,.6))",
                     '<div style="font-size:54px;font-weight:800;line-height:1.08;letter-spacing:-1px">Como responder <b>500 mensagens</b><br>num sábado sem contratar ninguém?</div>'))


def ilus_ticket():
    def etq(x, y, ang, valor, cor, risco=False):
        r = f'<line x1="{x+30}" y1="{y+95}" x2="{x+300}" y2="{y+85}" stroke="#E5484D" stroke-width="10" stroke-linecap="round"/>' if risco else ""
        return (f'<g transform="rotate({ang} {x+170} {y+90})"><path d="M{x} {y} h300 l40 90 l-40 90 h-300z" fill="{cor}" stroke="#1B1820" stroke-width="6"/>'
                f'<circle cx="{x+300}" cy="{y+90}" r="14" fill="#F4F1EA" stroke="#1B1820" stroke-width="5"/>'
                + txt(x + 150, y + 112, valor, 62, "#1B1820") + r + '</g>')
    return (f'<svg viewBox="0 0 952 330" width="952" height="330">' + etq(40, 60, -6, "R$ 309", "#fff", True)
            + txt(476, 175, "→", 90, "#2563EB") + etq(560, 70, 5, "R$ 268", "#FACC15")
            + txt(476, 315, "ticket médio previsto por pedido", 26, "#3A3442", peso=600) + '</svg>')


ILUS["ticket"] = ilus_ticket


def lg_humano():
    def n(ic, cor, tit, txt, hora, y):
        return _vidro(f"left:96px;right:96px;top:{y}px;padding:24px 30px;border-radius:36px",
                      '<div style="display:flex;gap:22px;align-items:center">'
                      f'<div style="width:74px;height:74px;border-radius:20px;background:{cor};display:flex;align-items:center;justify-content:center;font-size:38px;flex:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.5)">{ic}</div>'
                      f'<div style="flex:1"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:700"><span>{tit}</span><span style="opacity:.7;font-weight:500">{hora}</span></div>'
                      f'<div style="font-size:27px;margin-top:4px;opacity:.9">{txt}</div></div></div>')
    return (f'<div style="{TIT};top:190px">' + CHAP.format("NOVA REGRA DO SAC · DESDE 2/11")
            + '<div style="font-size:84px;font-weight:800;line-height:1.02;letter-spacing:-2.5px;margin-top:20px">IA atende.<br>Mas agora tem que ter<br><b>humano</b> das 8h às 20h.</div></div>'
            + n("🤖", "#2563EB", "IA respondeu em 4 s", "Seu pedido sai hoje. Quer falar com alguém?", "09:12", 640)
            + n("🙋", "#25D366", "Ana (atendimento) entrou", "Oi! Sou a Ana, vou te ajudar daqui ✋", "09:13", 780)
            + _vidro("left:64px;right:64px;top:950px;padding:34px 40px;border-radius:44px;background:linear-gradient(135deg,rgba(15,23,42,.82),rgba(15,23,42,.6))",
                     '<div style="font-size:50px;font-weight:800;line-height:1.1;letter-spacing:-1px">O jeito certo agora é <b>IA + gente</b>.<br>E a passagem tem que ser invisível.</div>')
            + '<div style="position:absolute;left:64px;bottom:58px;z-index:4;font-size:19px;opacity:.6">Fonte: MobileTime, 16/10/2026 (Decreto 13.135/2026)</div>')


def lg_cara():
    def dm(user, msg, hora, y):
        return _vidro(f"left:96px;right:96px;top:{y}px;padding:22px 30px;border-radius:34px",
                      '<div style="display:flex;gap:22px;align-items:center">'
                      '<div style="width:70px;height:70px;border-radius:50%;background:linear-gradient(135deg,#F58529,#DD2A7B,#8134AF);flex:none"></div>'
                      f'<div style="flex:1"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:700"><span>{user}</span><span style="opacity:.7;font-weight:500">{hora}</span></div>'
                      f'<div style="font-size:27px;margin-top:4px;opacity:.9">{msg}</div></div></div>')
    return (f'<div style="{TIT};top:170px;text-align:center"><div style="font-size:34px;font-weight:600;opacity:.9">Directs</div>'
            '<div style="font-size:170px;font-weight:800;letter-spacing:-6px;line-height:1;margin-top:4px">300</div>'
            '<div style="font-size:34px;font-weight:600;opacity:.9">sem resposta</div></div>'
            + dm("ana.estetica", "quanto custa?", "agora", 500) + dm("marcos_bjj", "atende minha cidade?", "4 min", 630)
            + dm("loja.bela", "tem parceria?", "9 min", 760)
            + _vidro("left:64px;right:64px;top:920px;padding:34px 40px;border-radius:44px;background:linear-gradient(135deg,rgba(15,23,42,.82),rgba(15,23,42,.6))",
                     '<div style="font-size:50px;font-weight:800;line-height:1.1;letter-spacing:-1px">"O brasileiro compra de quem<br><b>bota a cara</b>." Concordo.<br>Mas quem responde as 300 DMs?</div>'
                     '<div style="font-size:22px;font-weight:600;opacity:.7;margin-top:14px">João Adibe, dono da Cimed, à Forbes</div>'))


def lg_fila():
    return lg.slide1().replace('sexta-feira, 28 de novembro', 'na semana da Black Friday')


def liquid_raw(c):
    return f'<style>{lg.CSS % {"raio": "var(--r,40px)"}}</style></head><body>{lg.SVG_FILTRO}{c["miolo"]()}</body>'


def ilus_checklist():
    itens = [("Resposta automática", True), ("Link de pagamento", True), ("Estoque no catálogo", False), ("Pós-venda pronto", False)]
    linhas = "".join(f'<rect x="{110}" y="{70 + k*56}" width="34" height="34" rx="6" fill="{"#FACC15" if ok else "#fff"}" stroke="#1B1820" stroke-width="4"/>'
                     + (txt(127, 98 + k*56, "✓", 30) if ok else "") + txt(160, 98 + k*56, t, 28, meio=False, peso=700)
                     for k, (t, ok) in enumerate(itens))
    return (f'<svg viewBox="0 0 952 330" width="952" height="330">'
            f'<rect x="70" y="20" width="480" height="300" rx="18" fill="#fff" stroke="#1B1820" stroke-width="6"/>'
            f'<rect x="230" y="6" width="160" height="34" rx="10" fill="#2563EB" stroke="#1B1820" stroke-width="5"/>{linhas}'
            f'<rect x="600" y="70" width="320" height="200" rx="20" fill="#1B1820"/>' + txt(760, 160, "10", 96, "#FACC15")
            + txt(760, 220, "itens para checar hoje", 24, "#fff", peso=600) + '</svg>')


ILUS["checklist"] = ilus_checklist


def foto_topo(c):
    """Foto horizontal no alto (sem cortar ninguém) + texto em fundo escuro da marca embaixo."""
    uri = (AQUI / "fotos" / c["foto"]).as_uri()
    css = fdp.CSS + """
.topo{position:absolute;left:0;right:0;top:0;height:600px;background-size:cover;background-position:50% 20%;filter:saturate(.95) contrast(1.05)}
.topo:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,24,39,.55) 0%,rgba(17,24,39,0) 22%,rgba(17,24,39,0) 62%,#111827 100%)}
.txt{bottom:auto;top:660px}
"""
    hd = f'<div class="hd">{MARCA}<span>{HANDLE}</span></div>'
    bloco = (f'<div class="txt"><div class="chapeu">{html.escape(c["chapeu"])}</div><h1>{marcar(c["titulo"])}</h1>'
             + (f'<p>{marcar(c["texto"])}</p>' if c.get("texto") else "") + '</div>')
    rod = f'<div class="rod"><span>{html.escape(c["credito"])}</span><span class="seta">arrasta →</span></div>'
    return (f'<style>{css}</style></head><body class="capa"><div class="fundo"></div>{fdp.GRAO}'
            f'<div class="topo" style="background-image:url(\'{uri}\')"></div>{hd}{bloco}{rod}</body>')


def foto_nova(c):
    fdp.AQUI = AQUI  # fotos em capas_nov/fotos
    return foto(c)


# =====================================================================
# As 24 capas
# =====================================================================
CONFI = "Fonte: projeção Confi/Neotrust para o e-commerce (out/2026)"
CAPAS = [
    ("07", "VOLUME", foto_topo, dict(foto="toguro_alfredo_topo.jpg", chapeu="ALFREDO SOARES × TOGURO",
        titulo="O Toguro não caça viral.\nEle posta **todo dia**.",
        texto="A lição do episódio que passou de 590 mil views.",
        credito="Imagem: episódio \"O que aprendi sobre marketing com o Toguro\", canal Alfredo Soares / YouTube")),
    ("08", "CONTRATO", foto_nova, dict(slide=dict(foto="san_bernardino_local_original.jpg", pos="38% 50%",
        chapeu="FOME DE PODER · PARTE 2", titulo="O aperto de mão que\ncustou um **império**.",
        credito="Foto: local da 1ª loja / Marykdan, Wikimedia Commons (CC BY-SA 4.0)"))),
    ("09", "HUMANO", liquid, dict(variante=1, miolo=lg_humano)),
    ("10", "ONZE", tweet, dict(tema="claro", fs=62, texto="Amanhã é 11.11.\n\nR$ 3,17 bilhões em um dia só. E você ainda não mandou **nenhuma mensagem** para a sua base.",
        rodape="3 mensagens para mandar hoje no carrossel")),
    ("11", "BRINDE", tirinha, dict(expr="desconfiado", cena="brinde", tag="A LIÇÃO DA COQUETELEIRA",
        texto="Você paga **R$ 4** num clique\ne esquece o lead **em 2 dias**.")),
    ("12", "RECOMPRA", noticia, dict(data="QUI · 12 NOV 2026", tag="BLACK FRIDAY", fs=68,
        titulo="Na Black deste ano, o cliente vai gastar **menos** por compra.",
        sub="Quem ganha não é quem vende uma vez. É quem faz ele voltar.", ilus="ticket",
        fonte="Fonte: projeção Confi/Neotrust (out/2026)")),
    ("13", "VALOR", print_, dict(titulo='Cliente mandou\n**"qual valor?"**', sub="3 respostas que matam a venda e 1 que fecha.",
        contato="Cliente novo", status="online",
        msgs=[("ele", "boa tarde, qual valor?", "14:02"), ("eu", "R$ 350", "14:30 ✓✓"),
              ("ele", "ok", "14:31"), ("sep", "visto por último hoje às 14:31", "")])),
    ("14", "NUMERO", tirinha, dict(expr="pensando", cena="planilhas", tag="SE PRECISOU ABRIR 3 PLANILHAS…",
        texto="Quanto você vendeu\nmês passado?\nDe **qual canal**?")),
    ("15", "FILA", liquid_raw, dict(miolo=lg_fila)),
    ("16", "PROCESSO", foto_nova, dict(slide=dict(foto="favela_rocinha_close.jpg", pos="50% 30%",
        chapeu="DIA DAS FAVELAS", titulo="R$ 167 bi por ano.\nE 6 em cada 10 negócios\nsão de **mulheres**.",
        credito="Foto: Rocinha / chensiyuan, Wikimedia Commons (CC BY-SA 4.0)"))),
    ("17", "VIEWS", noticia, dict(data="TER · 17 NOV 2026", tag="POLÊMICA", fs=62,
        titulo="Toguro virou head de marketing da Cimed e a marca comemorou **2 bilhões** de views.",
        sub="A pergunta que ninguém respondeu: quantas viraram venda?", ilus="views",
        fonte="Fontes: InfoMoney, CidadeMarketing e YOUPIX (2026)")),
    ("18", "SUMIU", print_, dict(titulo="Cliente **sumiu**\ndepois do preço?", sub="7 mensagens para copiar e colar.",
        contato="Fernanda", status="visto por último ontem",
        msgs=[("ele", "me passa o orçamento?", "10:02"), ("eu", "Claro! Fica R$ 1.890 em até 10x 😊", "10:14 ✓✓"),
              ("sep", "3 DIAS DEPOIS", ""), ("eu", "Oi Fernanda, conseguiu ver?", "09:40 ✓✓")])),
    ("19", "BOMDIA", tweet, dict(tema="claro", texto="Pare de dar **bom dia** para cliente no WhatsApp.\n\nExplico no próximo slide.",
        rodape="Discorda? Arrasta antes de comentar.")),
    ("20", "FERIADO", tirinha, dict(expr="serio", cena="feriado", tag="20/11", fs=58,
        texto="Feriado: sua empresa **fecha**.\nSeu cliente, **não**.")),
    ("21", "CARA", liquid, dict(variante=3, miolo=lg_cara)),
    ("22", "RAPIDO", tweet, dict(tema="escuro", texto="Na Black, seu concorrente vai responder em **5 minutos**.\n\nE você?",
        rodape="Faltam 5 dias para a Black Friday")),
    ("23", "CALENDARIO", print_, dict(titulo="O que mandar\nem **cada dia** da Black.", sub="As 4 mensagens já programadas.", fs=72,
        contato="Lista de clientes", status="4 mensagens programadas",
        msgs=[("eu", "🕗 Qui 26 · 20h · A Lista VIP abriu. Você vê antes de todo mundo.", "programada"),
              ("eu", "🕗 Sex 27 · 08h · Começou! Seu cupom vale até meia-noite.", "programada"),
              ("eu", "🕗 Sáb 28 · 10h · Ficou no carrinho? Separei pra você.", "programada"),
              ("eu", "🕗 Dom 29 · 18h · Últimas horas. Depois volta o preço.", "programada")])),
    ("24", "VIRAL", foto_nova, dict(slide=dict(foto="pastel_queijo.jpg", pos="50% 15%",
        chapeu="VIRALIZOU", titulo="Uma pastelaria viralizou.\nO difícil foi **atender**\ntodo mundo que chamou.",
        credito="Foto: Mike Peel, Wikimedia Commons (CC BY-SA 4.0)"))),
    ("25", "VIP", print_, dict(titulo="Lista VIP: quem entra\n**antes** compra **primeiro**.", sub="Como montar a sua até quinta.", fs=68,
        contato="Lista VIP · Black", status="248 participantes",
        msgs=[("eu", "🔒 Você entrou na Lista VIP! Dia 26, às 20h, as ofertas chegam aqui antes de todo mundo.", "18:00 ✓✓"),
              ("ele", "já tô esperando 👀", "18:03"), ("ele", "vai ter o kit de presente?", "18:05")])),
    ("26", "CHECKLIST", noticia, dict(data="QUI · 26 NOV 2026", tag="AMANHÃ É BLACK", fs=72,
        titulo="O checklist de **10 itens** do seu atendimento.",
        sub="Confere hoje, porque amanhã não vai dar tempo. Salva esse.", ilus="checklist",
        fonte="Black Friday: sexta, 27/11")),
    ("27", "BLACK", liquid, dict(variante=1, miolo=lg_black)),
    ("28", "AGENTE", tirinha, dict(expr="risada", cena="sabado", tag="SÁBADO DE BLACK", fs=48,
        texto="Como responder\n**500 mensagens** num sábado\nsem contratar ninguém?")),
    ("29", "LEADS", foto_nova, dict(slide=dict(foto="bf_kohls.jpg", pos="50% 85%",
        chapeu="DEPOIS DA BLACK", titulo="300 pessoas te chamaram\ne **não compraram**.\nE agora?",
        credito="Foto: Tony Webster, Wikimedia Commons (CC BY 2.0)"))),
    ("30", "APAGADA", tweet, dict(tema="escuro", texto="Uma mensagem **apagada** vendeu R$ 10 milhões.\n\nO Alfredo Soares contou a história. O que dá para copiar está no carrossel.",
        rodape="O corte passou de 2,2 mi de views")),
]


ESCURA = (BASE / "marca" / "logo_horizontal_escura.png").as_uri()
BRANCA = (BASE / "marca" / "logo_horizontal_branca.png").as_uri()


def logo_para(fn, c):
    claro = fn in (tirinha, noticia, print_) or (fn is tweet and c.get("tema") == "claro")
    return ESCURA if claro else BRANCA


def render(dia, kw, fn, c, saida):
    doc = f'<!doctype html><html><head><meta charset="utf-8">{fn(c)}</html>'
    doc = doc.replace(MARCA, f'<img class="logo" src="{logo_para(fn, c)}" style="height:72px;width:auto;display:block">')
    arq = saida / f"capa_{dia}_{kw}.html"
    arq.write_text(doc, encoding="utf-8")
    png = saida / f"capa_{dia}_{kw}.png"
    subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--force-device-scale-factor=1", "--virtual-time-budget=8000", "--window-size=1080,1350",
                    f"--screenshot={png}", arq.as_uri()], check=True, capture_output=True)
    arq.unlink()
    print("OK", png.name)


def main():
    saida = AQUI / "capas"
    saida.mkdir(exist_ok=True)
    so = set(sys.argv[1:])
    for dia, kw, fn, c in CAPAS:
        if not so or dia in so:
            render(dia, kw, fn, c, saida)


if __name__ == "__main__":
    main()
