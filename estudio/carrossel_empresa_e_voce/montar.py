"""Carrossel "Se a sua empresa é você": tirinha com o personagem em cena + balão,
reaproveitando recortes de ../personagem. Cada slide tem um cenário que conta o assunto da fala.
Cabeçalho SuaMarca à esquerda e @ à direita.
Uso: python3 montar.py        -> slides/slide_NN.png
     python3 montar.py 1 4    -> só os slides 1 e 4
Marcação no texto: **x** = destaque amarelo, __x__ = roxo."""
import subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "personagem"))
from montar_tirinha_cor import CSS, CHROME, HANDLE, TRACO, marcar, personagem, piso  # noqa: E402

F = "font-family:Plus Jakarta Sans,sans-serif;font-weight:800"
PAREDE = '<rect width="1080" height="1350" fill="#FBF8F2"/>'


def txt(x, y, texto, tam, cor=TRACO, meio=True, peso=800, extra=""):
    ancora = ' text-anchor="middle"' if meio else ""
    return (f'<text x="{x}" y="{y}"{ancora} style="font-family:Plus Jakarta Sans,sans-serif;font-weight:{peso};'
            f'font-size:{tam}px;{extra}" fill="{cor}">{texto}</text>')


def caixa(x, y, w, cargo, nome="EU", cor="#fff", cor_txt=TRACO, tam=30):
    """Caixinha do organograma: cargo em cima, quem faz embaixo."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="78" rx="10" fill="{cor}" stroke="{TRACO}" stroke-width="5"/>'
            + txt(x + w / 2, y + 30, cargo, 17, cor_txt, extra="letter-spacing:1px;opacity:.75")
            + txt(x + w / 2, y + 64, nome, tam, cor_txt))


def janela_noite(x=780, y=430, hora="23:47"):
    return (f'<rect x="{x}" y="{y}" width="230" height="230" rx="8" fill="#2E2A5C" stroke="{TRACO}" stroke-width="7"/>'
            f'<circle cx="{x+170}" cy="{y+60}" r="26" fill="#FACC15"/><circle cx="{x+182}" cy="{y+50}" r="24" fill="#2E2A5C"/>'
            + "".join(f'<circle cx="{x+dx}" cy="{y+dy}" r="3.5" fill="#fff"/>' for dx, dy in ((80, 90), (120, 30), (50, 170), (200, 170)))
            + f'<line x1="{x+115}" y1="{y}" x2="{x+115}" y2="{y+230}" stroke="{TRACO}" stroke-width="6"/>'
            f'<line x1="{x}" y1="{y+115}" x2="{x+230}" y2="{y+115}" stroke="{TRACO}" stroke-width="6"/>'
            f'<rect x="{x+15}" y="{y+15}" width="86" height="36" rx="6" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>'
            + txt(x + 58, y + 41, hora, 22))


def janela_dia(x=790, y=430, sol=True):
    return (f'<rect x="{x}" y="{y}" width="220" height="220" rx="8" fill="#CFE3F5" stroke="{TRACO}" stroke-width="7"/>'
            + (f'<circle cx="{x+150}" cy="{y+70}" r="34" fill="#FACC15" stroke="{TRACO}" stroke-width="5"/>' if sol else "")
            + f'<path d="M{x+30} {y+170} q30 -25 60 0 q25 -18 50 0z" fill="#fff" stroke="{TRACO}" stroke-width="4"/>'
            f'<line x1="{x+110}" y1="{y}" x2="{x+110}" y2="{y+220}" stroke="{TRACO}" stroke-width="6"/>'
            f'<line x1="{x}" y1="{y+110}" x2="{x+220}" y2="{y+110}" stroke="{TRACO}" stroke-width="6"/>')


def mesa(x=740):
    return (f'<rect x="{x}" y="830" width="{1100-x}" height="26" fill="#C99A6B" stroke="{TRACO}" stroke-width="6"/>'
            f'<rect x="{x+30}" y="856" width="22" height="190" fill="#B9865A" stroke="{TRACO}" stroke-width="6"/>')


def celular(x, y, badge="99+", ang=-8, tela="#BBF7D0"):
    return (f'<g transform="rotate({ang} {x+45} {y+70})"><rect x="{x}" y="{y}" width="90" height="140" rx="14" fill="#3A3442" stroke="{TRACO}" stroke-width="6"/>'
            f'<rect x="{x+15}" y="{y+22}" width="60" height="80" rx="4" fill="{tela}"/></g>'
            + (f'<circle cx="{x+88}" cy="{y+4}" r="30" fill="#E5484D" stroke="{TRACO}" stroke-width="5"/>' + txt(x + 88, y + 14, badge, 24, "#fff") if badge else ""))


# ---------- cenários: cada um conta o assunto do slide ----------

def c_dono_faz_tudo():
    """Organograma em que todo cargo é EU, janela de noite 23:47, celular 99+, papelada."""
    org = ('<g transform="translate(20,-15) scale(.92)">'
           f'<rect x="50" y="425" width="560" height="270" rx="8" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
           + txt(330, 458, "ORGANOGRAMA", 20, extra="letter-spacing:3px")
           + caixa(250, 470, 160, "DONO", cor="#FACC15")
           + f'<path d="M330 548 v22 M125 570 h410 M125 570 v14 M330 570 v14 M535 570 v14" stroke="{TRACO}" stroke-width="4" fill="none"/>'
           + caixa(65, 584, 120, "VENDAS") + caixa(270, 584, 120, "ATENDIM.") + caixa(475, 584, 120, "FINANÇAS", cor="#2563EB", cor_txt="#fff")
           + '</g>')
    papel = "".join(f'<rect x="{1000 + d}" y="{828 - 14*(k+1)}" width="70" height="14" fill="#fff" stroke="{TRACO}" stroke-width="3" '
                    f'transform="rotate({(-1)**k*3} 1035 {820 - 14*k})"/>' for k, d in enumerate((0, 4, -3, 5, -2, 2, 0)))
    cafe = (f'<path d="M940 800 h44 v30 h-44z" fill="#fff" stroke="{TRACO}" stroke-width="5"/>'
            f'<path d="M984 806 q16 0 16 10 q0 10 -16 10" fill="none" stroke="{TRACO}" stroke-width="5"/>')
    return PAREDE + org + janela_noite() + piso() + mesa() + papel + celular(830, 700) + cafe


def c_episodio():
    """TV na parede passando o episódio (play, barra de progresso, views) e pipoca na prateleira."""
    tv = (f'<rect x="520" y="440" width="510" height="280" rx="14" fill="#2A2320" stroke="{TRACO}" stroke-width="7"/>'
          f'<rect x="540" y="458" width="470" height="244" rx="6" fill="#3A3442"/>'
          + txt(560, 490, "INTERCÂMBIO INTELECTUAL", 20, "#FACC15", meio=False, extra="letter-spacing:2px")
          + txt(560, 516, "episódio com o Toguro", 18, "#fff", meio=False, peso=500)
          + f'<circle cx="775" cy="590" r="40" fill="#FACC15" stroke="{TRACO}" stroke-width="5"/>'
          f'<path d="M763 570 l32 20 l-32 20z" fill="{TRACO}"/>'
          f'<rect x="560" y="660" width="430" height="10" rx="5" fill="#6B6475"/><rect x="560" y="660" width="250" height="10" rx="5" fill="#2563EB"/>'
          f'<circle cx="810" cy="665" r="11" fill="#fff"/>'
          + txt(990, 692, "590 mil views", 18, "#fff", meio=False, peso=700, extra="text-anchor:end"))
    prateleira = (f'<rect x="60" y="600" width="300" height="20" fill="#B9865A" stroke="{TRACO}" stroke-width="6"/>'
                  f'<path d="M110 600 l-14 -110 h108 l-14 110z" fill="#E5484D" stroke="{TRACO}" stroke-width="5"/>'
                  f'<path d="M124 600 l-8 -110 M148 600 v-110 M172 600 l8 -110" stroke="#fff" stroke-width="9"/>'
                  + "".join(f'<circle cx="{x}" cy="{y}" r="16" fill="#FFF6D6" stroke="{TRACO}" stroke-width="4"/>'
                            for x, y in ((112, 482), (138, 470), (166, 478), (190, 486), (150, 458)))
                  + f'<rect x="250" y="520" width="70" height="80" rx="8" fill="#2563EB" stroke="{TRACO}" stroke-width="5"/>')
    return PAREDE + tv + prateleira + piso()


def c_porta_fechada():
    """Loja com placa FECHADO porque o dono ficou doente; vitrine apagada."""
    porta = (f'<rect x="60" y="400" width="300" height="580" rx="6" fill="#B9865A" stroke="{TRACO}" stroke-width="7"/>'
             f'<rect x="95" y="430" width="230" height="200" rx="4" fill="#CFE3F5" stroke="{TRACO}" stroke-width="5"/>'
             f'<circle cx="320" cy="720" r="12" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>'
             f'<path d="M210 455 l-70 60 M210 455 l70 60" stroke="{TRACO}" stroke-width="4"/>'
             f'<g transform="rotate(-6 210 560)"><rect x="110" y="505" width="200" height="110" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
             + txt(210, 555, "FECHADO", 36, "#E5484D") + txt(210, 590, "o dono ficou doente", 17, peso=700) + '</g>')
    vitrine = (f'<rect x="560" y="470" width="470" height="230" rx="6" fill="#3A3442" stroke="{TRACO}" stroke-width="7"/>'
               f'<path d="M560 470 h470 l-30 -40 h-410z" fill="#2563EB" stroke="{TRACO}" stroke-width="6"/>'
               + "".join(f'<path d="M{x} 430 l-10 40" stroke="#fff" stroke-width="10"/>' for x in (640, 720, 800, 880, 960))
               + txt(795, 575, "LUZES APAGADAS", 26, "#8A857C", extra="letter-spacing:3px")
               + txt(795, 615, "ninguém sabe abrir o caixa", 20, "#8A857C", peso=600))
    return PAREDE + porta + vitrine + piso()


def c_whatsapp_caos():
    """Tela de conversas lotada (cliente 22h, vendedor, financeiro) e post-its na parede."""
    linhas = [("Cliente", "oi, ainda tem? preciso hoje", "22:14", "3"),
              ("Vendedor", "chefe, que preço eu passo?", "22:09", "5"),
              ("Financeiro", "o boleto do fornecedor venceu", "21:58", "2"),
              ("Funcionário", "posso sair mais cedo amanhã?", "21:40", "1")]
    tela = (f'<rect x="560" y="400" width="470" height="350" rx="22" fill="#fff" stroke="{TRACO}" stroke-width="7"/>'
            f'<path d="M560 422 q0 -22 22 -22 h426 q22 0 22 22 v40 h-470z" fill="#BBF7D0" stroke="{TRACO}" stroke-width="7"/>'
            + txt(585, 445, "Conversas", 24, meio=False) + txt(1005, 445, "47 não lidas", 18, "#E5484D", meio=False, extra="text-anchor:end"))
    for k, (nome, prev, hora, b) in enumerate(linhas):
        y = 470 + k * 68
        tela += (f'<circle cx="600" cy="{y+32}" r="22" fill="#2563EB"/>' + txt(600, y + 40, nome[0], 22, "#fff")
                 + txt(635, y + 28, nome, 21, meio=False) + txt(635, y + 52, prev, 17, "#6B6475", meio=False, peso=600)
                 + txt(1005, y + 26, hora, 15, "#6B6475", meio=False, peso=600, extra="text-anchor:end")
                 + f'<circle cx="992" cy="{y+46}" r="13" fill="#E5484D"/>' + txt(992, y + 52, b, 15, "#fff"))
    postits = "".join(f'<g transform="rotate({a} {x+70} {y+60})"><rect x="{x}" y="{y}" width="140" height="120" fill="#FACC15" stroke="{TRACO}" stroke-width="4"/>'
                      + txt(x + 70, y + 52, l1, 20) + txt(x + 70, y + 80, l2, 20) + '</g>'
                      for x, y, a, l1, l2 in ((60, 420, -5, "ligar p/", "Ana"), (220, 440, 4, "cobrar", "boleto"), (120, 560, 2, "responder", "47 msgs")))
    return PAREDE + tela + postits + piso()


def c_chapeus():
    """Cabideiro com um chapéu para cada função e calendário sem nenhuma folga."""
    cab = (f'<rect x="150" y="470" width="16" height="510" fill="#B9865A" stroke="{TRACO}" stroke-width="5"/>'
           f'<path d="M110 980 h96" stroke="{TRACO}" stroke-width="10" stroke-linecap="round"/>')
    for k, (rot, cor) in enumerate((("VENDAS", "#2563EB"), ("SAC", "#FACC15"), ("COBRANÇA", "#E5484D"), ("MARKETING", "#BBF7D0"))):
        lado = -1 if k % 2 == 0 else 1
        y = 500 + k * 95
        x = 158 + lado * 70
        cab += (f'<path d="M158 {y+20} L{x} {y+30}" stroke="{TRACO}" stroke-width="5"/>'
                f'<path d="M{x-45} {y+40} q45 -60 90 0z" fill="{cor}" stroke="{TRACO}" stroke-width="5"/>'
                f'<rect x="{x-55}" y="{y+36}" width="110" height="12" rx="6" fill="{cor}" stroke="{TRACO}" stroke-width="4"/>'
                f'<rect x="{x-50}" y="{y+52}" width="100" height="26" rx="5" fill="#fff" stroke="{TRACO}" stroke-width="3"/>'
                + txt(x, y + 71, rot, 14))
    cal = (f'<rect x="770" y="430" width="260" height="260" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
           f'<rect x="770" y="430" width="260" height="50" rx="10" fill="#E5484D" stroke="{TRACO}" stroke-width="6"/>'
           + txt(900, 464, "NOVEMBRO", 22, "#fff", extra="letter-spacing:2px"))
    for i in range(5):
        for j in range(4):
            x, y = 790 + i * 46, 495 + j * 40
            cal += f'<path d="M{x+8} {y+6} l22 22 M{x+30} {y+6} l-22 22" stroke="#E5484D" stroke-width="4" stroke-linecap="round"/>'
    cal += txt(900, 720, "folgas: 0", 24)
    return PAREDE + cab + cal + piso()


def c_quadro():
    """Quadro branco: EMPRESA = processo que roda sem você."""
    q = (f'<rect x="50" y="410" width="600" height="270" rx="10" fill="#fff" stroke="{TRACO}" stroke-width="7"/>'
         f'<rect x="40" y="680" width="620" height="14" rx="4" fill="#B9865A" stroke="{TRACO}" stroke-width="4"/>'
         + txt(80, 470, "EMPRESA =", 40, meio=False)
         + "".join(f'<rect x="{x}" y="500" width="120" height="56" rx="10" fill="{c}" stroke="{TRACO}" stroke-width="4"/>' + txt(x + 60, 536, t, 19, ct)
                   for x, t, c, ct in ((75, "lead", "#BBF7D0", TRACO), (215, "resposta", "#FACC15", TRACO),
                                       (355, "proposta", "#fff", TRACO), (495, "venda", "#2563EB", "#fff")))
         + "".join(f'<path d="M{x} 528 h18 m-8 -8 l8 8 l-8 8" stroke="{TRACO}" stroke-width="4" fill="none"/>' for x in (196, 336, 476))
         + txt(350, 615, "rodando sem depender de você", 26, "#2563EB")
         + f'<path d="M150 635 q200 18 400 0" stroke="#2563EB" stroke-width="5" fill="none"/>')
    return PAREDE + q + janela_dia() + piso()


def c_crm():
    """Monitor com o funil (kanban) organizado e caneca, de dia."""
    mon = (f'<rect x="540" y="430" width="500" height="300" rx="14" fill="#2A2320" stroke="{TRACO}" stroke-width="7"/>'
           f'<rect x="558" y="446" width="464" height="268" rx="6" fill="#fff"/>'
           + txt(575, 474, "Funil de vendas", 20, meio=False)
           + f'<rect x="770" y="802" width="40" height="30" fill="#3A3442" stroke="{TRACO}" stroke-width="5"/>'
           f'<rect x="740" y="720" width="100" height="84" fill="#3A3442" stroke="{TRACO}" stroke-width="5"/>')
    cols = (("Novo", ("Ana · Insta", "Rui · site")), ("Atendido", ("Bia · IA 2min",)),
            ("Proposta", ("Leo · R$2.400",)), ("Ganho", ("Carla ✓",)))
    for k, (nome, cards) in enumerate(cols):
        x = 572 + k * 112
        mon += (f'<rect x="{x}" y="484" width="102" height="222" rx="8" fill="#F4F1FA"/>' + txt(x + 51, 506, nome, 15, "#6B6475"))
        for i, c in enumerate(cards):
            cor = "#FACC15" if nome == "Ganho" else ("#2563EB" if nome == "Atendido" else "#fff")
            ct = "#fff" if nome == "Atendido" else TRACO
            mon += (f'<rect x="{x+6}" y="{518 + i*58}" width="90" height="48" rx="6" fill="{cor}" stroke="{TRACO}" stroke-width="3"/>'
                    + txt(x + 51, 548 + i * 58, c, 12.5, ct))
    caneca = (f'<path d="M960 790 h50 v40 h-50z" fill="#2563EB" stroke="{TRACO}" stroke-width="5"/>'
              f'<path d="M1010 798 q18 0 18 12 q0 12 -18 12" fill="none" stroke="{TRACO}" stroke-width="5"/>')
    relogio = (f'<circle cx="200" cy="520" r="80" fill="#fff" stroke="{TRACO}" stroke-width="8"/>'
               f'<line x1="200" y1="520" x2="200" y2="465" stroke="{TRACO}" stroke-width="7" stroke-linecap="round"/>'
               f'<line x1="200" y1="520" x2="160" y2="520" stroke="#2563EB" stroke-width="7" stroke-linecap="round"/>'
               + txt(200, 640, "9h da manhã", 22))
    return PAREDE + relogio + piso() + mesa(700) + mon + caneca


def c_quarto():
    """Quarto de manhã: sol na janela, despertador 07:30, celular avisando reuniões marcadas pela IA."""
    cama = (f'<rect x="180" y="690" width="720" height="300" rx="30" fill="#2563EB" stroke="{TRACO}" stroke-width="7"/>'
            f'<rect x="160" y="940" width="760" height="60" rx="14" fill="#fff" stroke="{TRACO}" stroke-width="6"/>')
    criado = (f'<rect x="900" y="780" width="160" height="200" rx="8" fill="#C99A6B" stroke="{TRACO}" stroke-width="6"/>'
              f'<rect x="930" y="740" width="100" height="40" rx="8" fill="#fff" stroke="{TRACO}" stroke-width="5"/>'
              + txt(980, 768, "07:30", 22))
    aviso = (f'<rect x="650" y="430" width="380" height="200" rx="22" fill="#fff" stroke="{TRACO}" stroke-width="6"/>'
             f'<circle cx="690" cy="475" r="20" fill="#2563EB"/>' + txt(690, 482, "IA", 15, "#fff")
             + txt(722, 482, "Agente de IA · 23:52", 18, "#6B6475", meio=False, peso=700)
             + txt(672, 530, "3 reuniões marcadas", 28, meio=False)
             + txt(672, 568, "leads da noite atendidos", 20, "#6B6475", meio=False, peso=600)
             + txt(672, 604, "em até 2 min ✓", 20, "#2563EB", meio=False))
    return PAREDE + janela_dia(70, 420) + piso() + cama + criado + aviso


def c_organograma_novo():
    """O mesmo organograma da capa, agora com cada função na mão certa."""
    o = (f'<rect x="70" y="440" width="940" height="470" rx="12" fill="#fff" stroke="{TRACO}" stroke-width="7"/>'
         + txt(540, 495, "ORGANOGRAMA 2.0", 28, extra="letter-spacing:4px")
         + caixa(395, 525, 290, "DONO", "EU (pensando o negócio)", cor="#FACC15", tam=22)
         + f'<path d="M540 603 v40 M200 643 h680 M200 643 v30 M540 643 v30 M880 643 v30" stroke="{TRACO}" stroke-width="5" fill="none"/>'
         + caixa(90, 673, 220, "ATENDIMENTO", "IA 24h", cor="#2563EB", cor_txt="#fff")
         + caixa(430, 673, 220, "VENDAS", "EQUIPE + CRM")
         + caixa(770, 673, 220, "FOLLOW-UP", "AUTOMÁTICO", cor="#BBF7D0")
         + txt(540, 830, "o mesmo dono. outra empresa.", 30, "#2563EB"))
    return PAREDE + piso() + o


def c_final():
    return PAREDE + janela_dia(70, 300) + piso() + mesa(780) + celular(860, 690, badge="", ang=6)


CENARIOS = {"dono_faz_tudo": c_dono_faz_tudo, "episodio": c_episodio, "porta_fechada": c_porta_fechada,
            "whatsapp_caos": c_whatsapp_caos, "chapeus": c_chapeus, "quadro": c_quadro, "crm": c_crm,
            "quarto": c_quarto, "organograma_novo": c_organograma_novo, "final": c_final}

# (expressão ou None, cenário, fala). Expressão "corpo" = corpo inteiro; None = slide sem personagem.
SLIDES = [
    ("desconfiado", "dono_faz_tudo", "Se a sua empresa é **você**,\nvocê não tem uma empresa.\nVocê tem um **emprego**."),
    ("pensando", "episodio", "Vi o episódio do Alfredo Soares\ncom o Toguro. Uma frase ficou:\n**\"Hoje a Mansão Maromba é o Toguro.\"**"),
    ("serio", "porta_fechada", "Marca gigante.\nMilhões de seguidores.\nMas tudo passa por **um só**.\nSe ele para, **para tudo**."),
    ("bravo", "whatsapp_caos", "Agora troca o Toguro por **você**.\nCliente chamou às 22h? Você.\nVendedor com dúvida? Você.\nBoleto venceu? **Você.**"),
    ("corpo", "chapeus", "Você não é o dono.\nÉ o funcionário que **mais trabalha**\ne o único que **não pode faltar**."),
    ("apontando", "quadro", "Empresa de verdade é a que\n**funciona quando você não está olhando**."),
    ("sorriso", "crm", "Primeiro passo: tirar a empresa\nda sua cabeça e do seu WhatsApp.\nTodo cliente num **funil só**."),
    ("risada", "quarto", "O lead das 22h?\nA __IA__ responde, qualifica\ne marca a reunião.\nVocê vê **de manhã**."),
    (None, "organograma_novo", "Mesmo organograma.\n**Outra empresa.**"),
    (None, "final", "Tire a empresa\nda sua cabeça.\n\nNa **SuaMarca** você tem\nCRM com funil de vendas,\n__IA__ que atende 24h\ne follow-up automático.\n\nComenta **DONO** que eu te mando o link.\n14 dias grátis."),
]

CSS_EXTRA = """
.hd{left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;color:#2A2320}
.marca{font-family:'Plus Jakarta Sans',sans-serif;font-size:34px;letter-spacing:-.5px}
.marca i{font-style:normal;font-weight:500;color:#2A2320}
.marca b{background:none;padding:0;font-weight:800}
.hd .arroba{font-size:28px;font-weight:700;color:#8A857C}
.capa-tag{position:absolute;left:64px;bottom:44px;z-index:4;font-family:'Plus Jakarta Sans',sans-serif;font-size:22px;font-weight:800;
 letter-spacing:2px;color:#fff;background:#2563EB;border:4px solid #2A2320;border-radius:12px;padding:10px 18px}
.seta{position:absolute;right:64px;bottom:44px;z-index:4;font-family:'Plus Jakarta Sans',sans-serif;font-size:26px;font-weight:800;
 color:#2A2320;background:#FACC15;border:4px solid #2A2320;border-radius:40px;padding:10px 24px}
.semcauda:after,.semcauda:before{display:none}
.fim{top:150px;bottom:140px;font-size:44px;line-height:1.22;padding:46px}
.fim .t{font-size:92px}
.credito{position:absolute;left:64px;right:64px;bottom:52px;z-index:4;font-family:'Plus Jakarta Sans',sans-serif;font-size:19px;
 font-weight:600;color:#6B6475;text-align:center}
"""
FONTE = "@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');"
CREDITO = "Inspirado no episódio \"O que aprendi sobre marketing com o Toguro\", do canal Alfredo Soares."


def main():
    saida = AQUI / "slides"
    saida.mkdir(exist_ok=True)
    so = {int(a) for a in sys.argv[1:]}
    total = len(SLIDES)
    for n, (expr, cena, texto) in enumerate(SLIDES, 1):
        if so and n not in so:
            continue
        fs = {1: 56, 2: 46, 3: 46, 4: 48, 5: 44, 6: 52, 7: 46}.get(n, 52 if len(texto) < 95 else 46)
        esquerda = n % 2 == 1
        vars_ = {"fs": fs, "bw": 820, "bx": 60 if esquerda else 200,
                 "cauda": 540 if esquerda else 240, "incl": 20 if esquerda else -20}
        svg = f'<svg class="cena" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{CENARIOS[cena]()}</svg>'
        hd = f'<div class="hd"><span class="marca"><i>Sua</i><b>Marca</b></span><span class="arroba">{HANDLE}</span></div>'
        linhas = texto.count("\n") + 1 + len(texto) // 34
        alt_bal = 64 + linhas * fs * 1.15
        if n == total:  # cartão final no estilo da Black Friday
            partes = marcar(texto).split("\n")
            partes[0] = f'<span class="t">{partes[0]}</span>'
            partes[1] = f'<span class="t">{partes[1]}</span>'
            corpo = f'{hd}<div class="fim"><div>{chr(10).join(partes)}</div></div><div class="credito">{CREDITO}</div>'
        else:
            if expr is None:
                img, classe = "", "bal semcauda"
            elif expr == "corpo":
                img, _ = personagem("corpo", 110 + alt_bal + 70)
                classe = "bal"
            else:
                img, _ = personagem(expr, 0)
                classe = "bal"
            rod = ('<div class="capa-tag">VOCÊ É O DONO OU O FUNCIONÁRIO?</div>' if n == 1 else "") + '<div class="seta">arrasta →</div>'
            corpo = f'{hd}<div class="{classe}" style="top:110px">{marcar(texto)}</div>{img}{rod}'
        doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTE}{CSS % vars_}{CSS_EXTRA}</style>'
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
