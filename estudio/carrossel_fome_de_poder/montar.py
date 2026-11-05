"""Carrossel Fome de Poder: foto histórica (licença livre, fotos/) + texto, 1080x1350.
Uso: python3 montar.py        -> todos os slides em slides/slide_NN.png
     python3 montar.py 3 7    -> só os slides 3 e 7
Marcação no texto: **x** = destaque amarelo."""
import html, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HANDLE = "@seuperfil"

CC0_DOWNEY = "Foto: Northwalker / Wikimedia Commons (CC0)"

# tipo "foto": foto + recorte + chapéu + título + texto + crédito | tipo "escuro": fundo da marca + bloco extra (html)
SLIDES = [
    dict(tipo="foto", foto="downey_1953_placa_speedee.jpg", pos="50% 8%", chapeu="FOME DE PODER · A HISTÓRIA DO McDONALD'S",
         titulo="O McDonald's nunca teve o melhor hambúrguer.\nTeve o melhor **sistema.**", credito=CC0_DOWNEY, capa=True),
    dict(tipo="foto", foto="ray_kroc_1976.jpg", pos="50% 20%", chapeu="1954",
         titulo="Um vendedor de 52 anos recebe um pedido estranho.",
         texto="Ray Kroc vendia máquinas de milk-shake de porta em porta. Uma lanchonete na Califórnia comprou **8 de uma vez**. Ninguém comprava 8.",
         credito="Foto: Ray Kroc em 1976 / domínio público"),
    dict(tipo="foto", foto="san_bernardino_local_original.jpg", pos="38% 50%", chapeu="SAN BERNARDINO, CALIFÓRNIA",
         titulo="Ele foi ver de perto.\nE viu **fila**.",
         texto="Cardápio com só 9 itens. Hambúrguer a 15 centavos. Pedido na mão em segundos, sem garçom e sem prato.",
         credito="Foto: local da 1ª loja / Marykdan, Wikimedia Commons (CC BY-SA 4.0)"),
    dict(tipo="foto", foto="downey_1953_loja.jpg", pos="30% 50%", chapeu="O SEGREDO",
         titulo="Não era a receita.\nEra o **processo**.",
         texto="Os irmãos McDonald desenharam a cozinha com giz numa quadra de tênis e ensaiaram cada movimento. Cada funcionário com uma função, numa ordem. Chamaram de Speedee System.",
         credito=CC0_DOWNEY),
    dict(tipo="foto", foto="des_plaines_1955_museu.jpg", pos="78% 50%", chapeu="1955 · DES PLAINES, ILLINOIS",
         titulo="Se é um sistema,\ndá para **copiar**.",
         texto="Kroc viu o que os irmãos não viram: o mesmo processo funcionaria em qualquer cidade. Abriu a primeira franquia dele e começou a replicar.",
         credito="Foto: réplica da loja de 1955 / Cboyles4423, Wikimedia Commons (CC BY-SA 4.0)"),
    dict(tipo="foto", foto="placa_route66_margolies.jpg", pos="52% 50%", chapeu="A VIRADA",
         titulo="O dinheiro não estava no **hambúrguer**.",
         texto="As taxas de franquia mal pagavam as contas. Então a empresa passou a comprar o terreno de cada loja e alugar para o franqueado. O ativo de verdade era outro.",
         credito="Foto: John Margolies / Library of Congress (domínio público)"),
    dict(tipo="escuro", chapeu="E O SEU NEGÓCIO?",
         titulo="Se amanhã você contratar 3 vendedores…",
         texto="eles sabem exatamente o que fazer com cada lead que chega?\n\nOu cada um atende do seu jeito, no próprio WhatsApp, quando dá tempo?",
         extra='<div class="interroga">?</div>'),
    dict(tipo="escuro", chapeu="O SPEEDEE DA SUA EMPRESA",
         titulo="Tem nome:\n**CRM**.",
         texto="Cada lead entra no funil, recebe resposta em minutos e ninguém fica esquecido.",
         extra=('<div class="funil">'
                '<div class="col"><span>Novo lead</span><div class="card">Chegou 22h14 · Instagram</div></div>'
                '<div class="col"><span>Respondido</span><div class="card roxo">IA respondeu em 2 min</div></div>'
                '<div class="col"><span>Proposta</span><div class="card">Enviada · R$ 2.400</div></div>'
                '<div class="col"><span>Fechado</span><div class="card amarelo">Ganho ✓</div></div></div>'
                '<div class="chips"><em>Follow-up automático</em><i>dia 1</i><i>dia 3</i><i>dia 7</i></div>')),
    dict(tipo="escuro", chapeu="E O SEU TERRENO?",
         titulo="É a sua **base de clientes**.",
         texto="Quem tem isso organizado escala. Quem guarda tudo no WhatsApp pessoal começa do zero todo mês.",
         extra=('<div class="ficha"><div class="topo"><div class="av">M</div><div><strong>Mariana Souza</strong>'
                '<small>Clínica Sorriso</small></div></div>'
                '<div class="lin"><span>Origem</span><b>Anúncio no Instagram</b></div>'
                '<div class="lin"><span>Etapa</span><b>Proposta enviada</b></div>'
                '<div class="lin"><span>Último contato</span><b>há 2 dias</b></div>'
                '<div class="lin"><span>Próximo passo</span><b>Follow-up amanhã, 9h</b></div></div>')),
    dict(tipo="escuro", final=True, chapeu="O SEU SPEEDEE SYSTEM",
         titulo="Na <span class=\"marca\"><i>Sua</i><b>Marca</b></span> o sistema já vem montado.",
         extra=('<ul class="lista"><li>CRM com funil de vendas</li><li>IA que responde o lead em minutos</li>'
                '<li>Follow-up automático no WhatsApp</li></ul>'
                '<div class="cta">Comenta <b>SISTEMA</b> que eu te mando o link.<small>14 dias grátis para testar.</small></div>'),
         credito=("Fotos: Wikimedia Commons. Marykdan e Cboyles4423 (CC BY-SA 4.0), Northwalker (CC0), "
                  "John Margolies/Library of Congress e Ray Kroc 1976 (domínio público).")),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#111827}
body{font-family:'Plus Jakarta Sans',sans-serif;position:relative;color:#fff}
.foto{position:absolute;inset:0;background-size:cover;filter:sepia(.35) saturate(.85) contrast(1.08) brightness(.92)}
.grao{position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay}
.sombra{position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,24,39,.7) 0%,rgba(17,24,39,0) 20%,rgba(17,24,39,0) 36%,rgba(17,24,39,.9) 58%,#111827 100%)}
.capa .sombra{background:linear-gradient(180deg,rgba(17,24,39,.7) 0%,rgba(17,24,39,0) 20%,rgba(17,24,39,0) 42%,rgba(17,24,39,.88) 66%,#111827 100%)}
.fundo{position:absolute;inset:0;background:radial-gradient(900px 700px at 100% 0%,rgba(37,99,235,.35),transparent 60%),#111827}
.hd{position:absolute;top:44px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;z-index:3}
.hd .marca{opacity:1;font-size:34px;letter-spacing:-.5px;text-shadow:0 1px 8px rgba(0,0,0,.45)}
.marca b{color:#fff;font-weight:800}
.marca i{font-style:normal;font-weight:500}
.hd span{font-size:26px;font-weight:700;letter-spacing:.5px;opacity:.92}
.txt{position:absolute;left:64px;right:64px;bottom:150px;z-index:2}
.escuro .txt{top:150px;bottom:150px;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}
.chapeu{display:inline-block;font-size:24px;font-weight:800;letter-spacing:3px;color:#111827;background:#FACC15;padding:10px 18px;border-radius:6px;margin-bottom:34px}
.escuro .chapeu{background:#2563EB;color:#fff}
h1{font-size:72px;line-height:1.06;font-weight:800;letter-spacing:-1.5px;white-space:pre-line}
.capa h1{font-size:84px;line-height:1.04}
.escuro h1{font-size:80px}
h1 .marca{font-size:inherit}
p{margin-top:28px;font-size:36px;line-height:1.38;font-weight:500;color:rgba(255,255,255,.86);white-space:pre-line}
b{color:#FACC15;font-weight:800}
.rod{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;align-items:center;gap:30px;font-size:19px;opacity:.75;z-index:3}
.rod span:first-child{max-width:700px;line-height:1.35}
.seta{font-size:26px;font-weight:700;opacity:1;color:#fff;border:2px solid rgba(255,255,255,.6);border-radius:40px;padding:10px 24px;white-space:nowrap}
.interroga{position:fixed;right:70px;bottom:130px;z-index:-1;font-size:440px;line-height:1;font-weight:800;color:#2563EB;opacity:.3}
.funil,.ficha,.lista,.cta,.chips{align-self:stretch}
.funil{display:flex;gap:14px;margin-top:54px}
.col{flex:1;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.12);border-radius:20px;padding:18px 14px;min-height:300px}
.col span{display:block;font-size:25px;font-weight:700;opacity:.7;margin-bottom:16px}
.card{background:#fff;color:#111827;border-radius:14px;padding:18px 16px;font-size:26px;font-weight:700;line-height:1.3}
.card.roxo{background:#2563EB;color:#fff}
.card.amarelo{background:#FACC15}
.chips{display:flex;gap:12px;align-items:center;margin-top:30px;font-size:26px}
.chips em{font-style:normal;font-weight:700;margin-right:8px}
.chips i{font-style:normal;font-weight:800;background:rgba(250,204,21,.15);color:#FACC15;border:2px solid #FACC15;border-radius:30px;padding:8px 20px}
.ficha{margin-top:54px;background:#fff;color:#111827;border-radius:26px;padding:34px 38px;box-shadow:14px 14px 0 #2563EB}
.ficha .topo{display:flex;gap:20px;align-items:center;margin-bottom:22px}
.av{width:72px;height:72px;border-radius:50%;background:#2563EB;color:#fff;font-size:34px;font-weight:800;display:flex;align-items:center;justify-content:center}
.ficha strong{display:block;font-size:34px}
.ficha small{font-size:24px;opacity:.6}
.lin{display:flex;justify-content:space-between;border-top:2px solid #EEE9F7;padding:16px 0;font-size:27px}
.lin span{opacity:.6}
.lin b{color:#111827}
.lista{list-style:none;margin-top:46px}
.lista li{font-size:38px;font-weight:700;padding:18px 0 18px 64px;position:relative;border-bottom:2px solid rgba(255,255,255,.1)}
.lista li:before{content:'✓';position:absolute;left:0;top:14px;width:44px;height:44px;border-radius:50%;background:#FACC15;color:#111827;font-size:28px;display:flex;align-items:center;justify-content:center}
.cta{margin-top:54px;background:#2563EB;border-radius:26px;padding:34px 38px;font-size:40px;font-weight:800;line-height:1.25}
.cta small{display:block;margin-top:10px;font-size:28px;font-weight:600;opacity:.9}
"""

GRAO = ('<svg class="grao" width="1080" height="1350"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" '
        'numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')


def marcar(texto):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(texto))


def montar(s):
    hd = f'<div class="hd"><span class="marca"><i>Sua</i><b>Marca</b></span><span>{HANDLE}</span></div>'
    titulo = s["titulo"] if s.get("final") else marcar(s["titulo"])
    texto = f'<p>{marcar(s["texto"])}</p>' if s.get("texto") else ""
    bloco = f'<div class="txt"><div class="chapeu">{html.escape(s["chapeu"])}</div><h1>{titulo}</h1>{texto}{s.get("extra", "")}</div>'
    seta = "" if s.get("final") else '<span class="seta">arrasta →</span>'
    rod = f'<div class="rod"><span>{html.escape(s.get("credito", ""))}</span>{seta}</div>'
    if s["tipo"] == "foto":
        uri = (AQUI / "fotos" / s["foto"]).as_uri()
        fundo = (f'<div class="foto" style="background-image:url(\'{uri}\');background-position:{s["pos"]}"></div>'
                 f'{GRAO}<div class="sombra"></div>')
    else:
        fundo = f'<div class="fundo"></div>{GRAO}'
    classe = "capa" if s.get("capa") else s["tipo"]
    return f'<body class="{classe}">{fundo}{hd}{bloco}{rod}</body>'


def main():
    saida = AQUI / "slides"
    saida.mkdir(exist_ok=True)
    so = {int(a) for a in sys.argv[1:]}
    for n, s in enumerate(SLIDES, 1):
        if so and n not in so:
            continue
        doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>{montar(s)}</html>'
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
