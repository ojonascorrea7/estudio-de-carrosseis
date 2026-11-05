# Estúdio de Carrosséis

Sistema para criar carrosséis de Instagram em código: da pauta ao PNG pronto para postar. Também gera a versão animada, em MP4 com loop.

Tudo é HTML desenhado por código e fotografado pelo Chrome em 1080x1350. O texto é texto de verdade, nítido, sem imagem gerada por IA com letras tortas. Uma mesma pauta pode virar 7 layouts diferentes.

## Use como skill do Claude Code
Este repositório já é uma skill: o `SKILL.md` na raiz ensina o Claude a seguir o método inteiro (pauta → capas → grade → 7 slides → crítica → entrega).

```bash
git clone https://github.com/ojonascorrea7/estudio-de-carrosseis.git ~/.claude/skills/estudio-de-carrosseis
```

Depois é só pedir no Claude Code: "faz um carrossel sobre X" ou "monta os carrosséis do mês". Na primeira vez, ele cria o `marca.md` a partir do `modelo_marca.md`, com as informações do seu perfil.

## O que tem aqui

| Pasta | O que faz |
|---|---|
| `SKILL.md` · `modelo_marca.md` | A skill (fluxo com paradas de aprovação, regras e checklist) e o modelo de configuração da marca |
| `docs/` | O método: pesquisa de pauta, layouts, sequência da grade, copy e CTA, carrossel animado |
| `estudio/calendario/capas_nov/montar_capas.py` | Gera capas em 7 layouts (notícia, foto, tweet, print de WhatsApp, dados, tirinha, Liquid Glass) |
| `estudio/calendario/carrosseis_nov/` | `roteiro.py` (conteúdo de um mês inteiro, como exemplo) e `montar_carrosseis.py` (gera os slides internos e o CTA no estilo de cada capa) |
| `estudio/referencias_layout/liquid_glass/` | Layout de vidro líquido, com 4 fundos (futurista, claro, escuro, roxo) |
| `estudio/personagem/` | Motor de tirinha: o personagem recortado entra num cenário desenhado em SVG, com balão de fala |
| `estudio/carrossel_animado/` | Motor de carrossel em movimento: `animar.js` + `render_animado.mjs` (HTML → MP4) |
| `estudio/marca/` | Logos de exemplo. Troque pelos seus |

## Começo rápido

```bash
pip install pillow
cd estudio/calendario/capas_nov
python3 montar_capas.py 10 12 13 27     # gera algumas capas em capas/
cd ../carrosseis_nov
python3 montar_carrosseis.py 10 13       # gera os carrosséis completos (7 slides + legenda)
```

**Requisitos:**
- Google Chrome instalado (o caminho fica em `CHROME`, no topo dos scripts).
- Python 3 com Pillow.
- Para o animado: Node com `playwright` e `ffmpeg`.

## Personalize

1. **Marca:** troque `estudio/marca/logo_horizontal_*.png` e, no Liquid Glass, os arquivos `logo_*` e o raio. Busque nos scripts `@seuperfil`, `SuaMarca` e as cores (`#2563EB` principal, `#FACC15` destaque, `#111827` escuro).
2. **Fotos:** coloque as fotos em `estudio/calendario/capas_nov/fotos/`, com licença livre ou próprias, e anote os créditos.
3. **Personagem da tirinha:** coloque os seus recortes PNG (fundo transparente) em `estudio/personagem/recortes/`. São 8 expressões em busto (`pensando`, `sorriso`, `bravo`, `serio`, `desconfiado`, `apontando`, `risada`) e um de corpo inteiro (`corpo`).
4. **Conteúdo:** edite `roteiro.py`. Cada dia tem palavra-chave, layout, 5 slides, CTA e legenda.

## Licença
Código e textos autorais deste repositório. Fotos e marcas de terceiros não estão incluídas.
