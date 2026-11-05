"""Frases de impacto em template estilo tweet (1080x1350), tema claro ou escuro.
Uso: python3 montar.py            -> renderiza todas as frases de FRASES
     python3 montar.py 2 6 13     -> renderiza só essas (numeração 1..N)"""
import html, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AVATAR = (AQUI / "avatar.jpg").as_uri()
NOME, HANDLE = "Seu Nome", "@seuperfil"

# (frase, tema)
FRASES = [
    ("Empreender é trocar um chefe por todos os seus clientes.", "claro"),
    ("A 6x1 acabou para o funcionário.\n\nPara o dono, ela nunca existiu.", "escuro"),
    ("O empresário posta o faturamento.\n\nNunca posta a madrugada que custou.", "claro"),
    ("Seu concorrente não é melhor que você.\n\nEle só responde o WhatsApp mais rápido.", "escuro"),
    ("Ninguém aplaude o empresário que pagou a folha em dia.\n\nDevia.", "claro"),
    ("Quem diz que dinheiro não traz felicidade nunca pagou o 13º de dez funcionários.", "escuro"),
    ("Você não tem problema de tráfego.\n\nVocê tem problema de atendimento.", "claro"),
    ("Lead barato que ninguém atende é o lead mais caro da sua empresa.", "escuro"),
    ("Se o seu vendedor precisa lembrar de fazer follow-up, você não tem processo.\n\nTem sorte.", "claro"),
    ("Empresa que só funciona com o dono presente não é empresa.\n\nÉ emprego com CNPJ.", "escuro"),
    ("“Vou pensar” é só um não com educação.\n\nOu um sim sem follow-up.", "claro"),
    ("Você não precisa de mais seguidores.\n\nPrecisa responder quem já te chamou.", "escuro"),
    ("Todo empresário quer escalar.\n\nQuase nenhum quer organizar.", "claro"),
    ("Cliente que pede desconto antes de ouvir o preço nunca foi seu cliente.", "escuro"),
]

TEMAS = {
    "claro": {"bg": "#F2F2F2", "card": "#FFFFFF", "txt": "#0F1419", "sub": "#536471", "borda": "#E6E6E6", "marca": "#2563EB"},
    "escuro": {"bg": "#111827", "card": "#211C2B", "txt": "#F5F4F8", "sub": "#9B95A8", "borda": "#2E283A", "marca": "#8D91F8"},
}

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:%(bg)s;font-family:-apple-system,'SF Pro Text','Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;
 display:flex;align-items:center;justify-content:center;position:relative}
.card{width:936px;background:%(card)s;border:1px solid %(borda)s;border-radius:36px;padding:56px 60px 48px;
 box-shadow:0 30px 60px -36px rgba(0,0,0,.35)}
.top{display:flex;align-items:center;gap:22px}
.av{width:104px;height:104px;border-radius:50%%;object-fit:cover}
.nm{font-size:38px;font-weight:700;color:%(txt)s;letter-spacing:-.3px}
.hd{font-size:31px;color:%(sub)s;margin-top:2px}
.tx{margin-top:40px;font-size:%(fs)spx;line-height:1.28;color:%(txt)s;letter-spacing:-.6px;white-space:pre-line;font-weight:500}
.rod{margin-top:44px;padding-top:28px;border-top:1px solid %(borda)s;display:flex;justify-content:space-between;font-size:26px;color:%(sub)s}
.rod b{color:%(marca)s;font-weight:600}
"""


def tamanho(frase):
    n = len(frase)
    return 66 if n < 70 else 60 if n < 100 else 54


def main():
    saida = AQUI / "png"
    saida.mkdir(exist_ok=True)
    escolha = {int(a) for a in sys.argv[1:]} or set(range(1, len(FRASES) + 1))
    for n, (frase, tema) in enumerate(FRASES, 1):
        if n not in escolha:
            continue
        cfg = dict(TEMAS[tema], fs=tamanho(frase))
        doc = ('<!doctype html><html><head><meta charset="utf-8">'
               f'<style>{CSS % cfg}</style></head><body><div class="card">'
               f'<div class="top"><img class="av" src="{AVATAR}"><div><div class="nm">{NOME}</div>'
               f'<div class="hd">{HANDLE}</div></div></div>'
               f'<div class="tx">{html.escape(frase)}</div>'
               '<div class="rod"><span>Compartilhe com quem precisa ler isso</span><b>Sua Marca</b></div>'
               '</div></body></html>')
        arq = saida / f"frase_{n:02d}.html"
        arq.write_text(doc, encoding="utf-8")
        png = saida / f"frase_{n:02d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", "--force-device-scale-factor=1",
                        "--window-size=1080,1350", f"--screenshot={png}", arq.as_uri()],
                       check=True, capture_output=True)
        arq.unlink()
        print("OK", png.name)


if __name__ == "__main__":
    main()
