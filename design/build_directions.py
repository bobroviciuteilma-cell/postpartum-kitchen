#!/usr/bin/env python3
"""Build the three design-direction previews under design/<slug>/ from the real surfaces.
Sources are copied verbatim (base64 photos included); each copy gets a <style id="direction">
override appended after the original CSS, a switcher bar, rewritten relative links, and a
titled <title>. Original files/URLs are never touched.
Photos: where an approved v2 style anchor exists (design/anchor-images.json, extracted
from photo-anchors-preview.html and downscaled to 800px), it replaces the old card photo
in the copies — so the previews wear the locked photo style. Anchors are framed WIDE;
the real photo pass shoots closer per Ilma's framing rule."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESIGN = os.path.join(ROOT, 'design')

ANCH_PATH = os.path.join(DESIGN, 'anchor-images.json')
ANCHORS = json.load(open(ANCH_PATH)) if os.path.exists(ANCH_PATH) else {}
SWAP_CARD = {'hero': 'the-hero-plate', 'step_cook': 'the-skillet-step',
             'i_liver': 'ingredient-liver', 'i_dill': 'ingredient-the-herbs',
             'i_seeds': 'ingredient-pumpkin-seeds', 'i_veg': 'ingredient-grated-veg'}
SWAP_WEEK1 = {'liver': 'the-hero-plate', 'kvass': 'the-kilner-jar'}

def swap_images(h, mapping):
    for key, slug in mapping.items():
        if slug in ANCHORS:
            h = re.sub('("' + key + '": ")data:image/[^"]+(")',
                       lambda m: m.group(1) + ANCHORS[slug] + m.group(2), h, count=1)
    return h

SRC = {}
for name, path in [
    ('week1.html',             'pilot/week1.html'),
    ('liver-cutlets.html',     'pilot/liver-cutlets.html'),
    ('liver-cutlets-mum.html', 'pilot/liver-cutlets-mum.html'),
    ('index.html',             'cook-cards/index.html'),
]:
    with open(os.path.join(ROOT, path)) as f:
        SRC[name] = f.read()

# ---------------------------------------------------------------- direction CSS
SCALLOP = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='112' height='8' "
           "viewBox='0 0 112 8'><path d='M1 7 Q8 0 15 7 T29 7 T43 7 T57 7 T71 7 T85 7 T99 7 T113 7' "
           "fill='none' stroke='%23A9BCD4' stroke-width='1.2'/></svg>\")")

POSY = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='112' height='26' viewBox='0 0 112 26'>"
        "<g stroke='%236E8A6F' stroke-width='1.1' fill='none' stroke-linecap='round'>"
        "<path d='M54 23 C48 17 40 13 27 11'/><path d='M54 23 C51 17 47 13 46 10'/>"
        "<path d='M54 23 C60 17 66 13 71 10'/><path d='M54 23 C62 19 74 16 86 15'/></g>"
        "<g fill='%237C6E9E'><ellipse cx='25' cy='10' rx='2' ry='3.1' transform='rotate(-38 25 10)'/>"
        "<ellipse cx='20' cy='8' rx='1.8' ry='2.8' transform='rotate(-38 20 8)'/>"
        "<ellipse cx='15.6' cy='6.4' rx='1.6' ry='2.5' transform='rotate(-38 15.6 6.4)'/>"
        "<ellipse cx='11.8' cy='5.2' rx='1.3' ry='2.1' transform='rotate(-38 11.8 5.2)'/></g>"
        "<g fill='%23FFFFFF' stroke='%23DCD0B6' stroke-width='.5'>"
        "<ellipse cx='46' cy='4.2' rx='1.6' ry='2.7'/><ellipse cx='46' cy='13.8' rx='1.6' ry='2.7'/>"
        "<ellipse cx='41.2' cy='9' rx='2.7' ry='1.6'/><ellipse cx='50.8' cy='9' rx='2.7' ry='1.6'/>"
        "<ellipse cx='42.6' cy='5.6' rx='1.5' ry='2.5' transform='rotate(-45 42.6 5.6)'/>"
        "<ellipse cx='49.4' cy='12.4' rx='1.5' ry='2.5' transform='rotate(-45 49.4 12.4)'/>"
        "<ellipse cx='49.4' cy='5.6' rx='1.5' ry='2.5' transform='rotate(45 49.4 5.6)'/>"
        "<ellipse cx='42.6' cy='12.4' rx='1.5' ry='2.5' transform='rotate(45 42.6 12.4)'/></g>"
        "<circle cx='46' cy='9' r='2.4' fill='%23E7C878'/>"
        "<g fill='%236E8FBF'>"
        "<ellipse cx='72' cy='4.6' rx='1.3' ry='2.6'/>"
        "<ellipse cx='72' cy='11.4' rx='1.3' ry='2.6'/>"
        "<ellipse cx='69' cy='6.3' rx='1.3' ry='2.6' transform='rotate(60 69 6.3)'/>"
        "<ellipse cx='75' cy='9.7' rx='1.3' ry='2.6' transform='rotate(60 75 9.7)'/>"
        "<ellipse cx='75' cy='6.3' rx='1.3' ry='2.6' transform='rotate(-60 75 6.3)'/>"
        "<ellipse cx='69' cy='9.7' rx='1.3' ry='2.6' transform='rotate(-60 69 9.7)'/></g>"
        "<circle cx='72' cy='8' r='1.5' fill='%233F5E8C'/>"
        "<path d='M86 15 C91 11 97 11 102 13 C97 17 91 18 86 15 Z' fill='%23DFE7D5' stroke='%236E8A6F' stroke-width='.8'/></svg>\")")

CSS_PORCELAIN = """
/* DIRECTION 1 — PORCELAIN MINIMAL: white porcelain on pale linen, sage-crisp,
   lavender + azure only in the fine print, an azure-glaze scalloped hairline
   under the wordmark (the blue rim line on French porcelain). */
:root{
  --paper:#FCFAF3; --paper2:#FFFFFF; --sage:#7A917C; --sage-d:#546E59; --sage-soft:#E4EBE0;
  --amber:#B98F56; --amber-soft:#F0E5CF; --ink:#3D392F; --ink2:#6F695B; --line:#E9E1D0;
  --beet:#9C2B4E; --beet-soft:#F5E4EA;
  --lav:#8C81A9; --lav-soft:#EDEAF3; --pink:#C98A9B; --pink-soft:#F7E8EC;
  --azure:#7E96B8; --azure-soft:#E7EDF5;
}
body{background:#EFE9DB;}
.brandtag{color:var(--lav);}
.eyebrow{color:var(--lav);}
.tkind{color:var(--azure);}
.dots i.on{background:var(--azure);}
.sech,.blockh,.hkicker,.ovscale-lab{color:var(--sage-d);}
h1,.tname,.askname{color:var(--ink);}
.tile{background:#FFFFFF; border-radius:15px; box-shadow:0 8px 20px rgba(88,78,56,.10);}
.tile:hover{box-shadow:0 12px 26px rgba(88,78,56,.15);}
.tile img{box-shadow:none; border:1px solid var(--line);}
.more a{background:#FFFFFF;}
.card{box-shadow:0 18px 44px rgba(88,78,56,.16);}
.hero{border:6px solid #fff; border-radius:16px; box-shadow:0 10px 22px rgba(88,78,56,.16);}
.step .img{border:3px solid #fff;}
.phone{box-shadow:0 22px 44px rgba(70,60,40,.30);}
.rule,.brandrule{width:112px; height:8px; background:SCALLOP_SVG center/contain no-repeat;}
.tag.b{background:var(--pink-soft); color:#9A4B62;}
"""

CSS_GARDEN = """
/* DIRECTION 2 — PROVENCE GARDEN: lavender headings, a wildflower posy (now with a
   cornflower) under the wordmark, pink in the warm notes, azure in the when-band
   and the arrows, and the send action tried in deep iris. */
:root{
  --paper:#FAF5E8; --paper2:#FFFDF5; --sage:#6E8A6F; --sage-d:#4D6852; --sage-soft:#DFE7D5;
  --amber:#C08A43; --amber-soft:#EDDFC2; --ink:#3B362C; --ink2:#6B6456; --line:#E3D9C3;
  --beet:#6D5F92; --beet-soft:#E9E4F2;
  --lav:#7C6E9E; --lav-d:#5D5382; --lav-soft:#E9E4F2; --pink:#C97F92; --pink-soft:#F5DFE5;
  --azure:#46608A; --azure-mid:#6E8FBF; --azure-soft:#E3EBF5;
}
body{background:#DADEC7; background-image:radial-gradient(circle at 25% 10%, rgba(255,255,255,.4), transparent 55%);}
.sech,.blockh,.hkicker,.ovscale-lab,.ctl-lab{color:var(--lav-d);}
.controls .blockh{color:var(--lav-d);}
.eyebrow{color:#B06A7E;}
.brandtag{color:var(--lav);}
.tkind{color:var(--lav-d);}
.whenband{background:var(--azure-soft); color:var(--azure);}
.whenband b{color:var(--azure);}
.tarrow{color:var(--azure-mid);}
.controls{border-color:#B7AECD; box-shadow:0 10px 26px rgba(108,95,146,.13);}
.ovscale{border-color:#B7AECD; box-shadow:0 6px 16px rgba(108,95,146,.10);}
.dots i.on{background:var(--lav-d);}
.step .n{background:var(--lav-d);}
.tag.b{background:#f3dee5; color:#8d3a5c;}
.cooknote{background:var(--pink-soft); color:#8A4457;}
.cooknote b{color:#8E2A47;}
.tile{box-shadow:0 12px 30px rgba(110,80,100,.16);}
.tile:hover{border-color:#DDBAC4;}
.hero{border-color:#FBEFF2;}
.beetbtn:hover{background:#5C4F80;}
.rule,.brandrule{width:104px; height:26px; background:POSY_SVG center/contain no-repeat;}
"""

CSS_APOTHECARY = """
/* DIRECTION 3 — LINEN APOTHECARY: deep oatmeal linen with a woven texture,
   label-frame double rules like a hand-labelled jar, amber small-caps,
   lavender-ink eyebrow with a wax-seal pink dot, azure as the written ink
   (the numbers and counts, like blue ink on a jar label). */
:root{
  --paper:#F7F0E1; --paper2:#FCF7E9; --sage:#6C8268; --sage-d:#4E634E; --sage-soft:#DFE4D1;
  --amber:#B27E35; --amber-soft:#ECDCBE; --ink:#39342A; --ink2:#6B6456; --line:#DCCFB4;
  --beet:#8E2A47; --beet-soft:#F1DDE3;
  --lav:#8678A2; --lav-soft:#EAE6F0; --pink:#C2848F; --pink-soft:#F3E2E4;
  --azure-ink:#5E739B;
}
body{background-color:#C9BFA9; background-image:
  repeating-linear-gradient(0deg, rgba(255,255,255,.05) 0 1px, transparent 1px 3px),
  repeating-linear-gradient(90deg, rgba(107,88,58,.05) 0 1px, transparent 1px 3px);}
.card{position:relative;}
.card::after{content:""; position:absolute; inset:9px; border:1px solid rgba(178,126,53,.5); border-radius:9px; pointer-events:none; z-index:5;}
.blockh,.sech,.hkicker,.ovscale-lab{color:var(--amber); letter-spacing:.2em;}
.eyebrow{color:var(--lav);}
.eyebrow::after{content:""; display:inline-block; width:7px; height:7px; border-radius:50%; background:var(--pink); margin-left:9px; vertical-align:1px;}
h1,.tname,.askname{color:var(--ink);}
.brandmark{color:#4E634E;}
.step .n{background:var(--amber);}
.metarow b{color:var(--azure-ink);}
.ovmeta b{color:var(--azure-ink);}
.ct{color:var(--azure-ink);}
.tarrow{color:var(--azure-ink);}
.tile{border-radius:11px; box-shadow:inset 0 0 0 3px var(--paper), inset 0 0 0 4px rgba(178,126,53,.45), 0 12px 26px rgba(60,50,30,.16);}
.tile img{border-radius:9px;}
.more a{box-shadow:inset 0 0 0 2px var(--paper2), inset 0 0 0 3px rgba(178,126,53,.35);}
.nutri .cell{box-shadow:inset 0 0 0 2px var(--paper2), inset 0 0 0 3px rgba(178,126,53,.3);}
.hero{border-radius:10px;}
.why{border-color:#D3C4A4;}
.rule,.brandrule{width:76px; height:7px; opacity:.55; background:
  linear-gradient(var(--amber),var(--amber)) center top/76px 1px no-repeat,
  linear-gradient(var(--amber),var(--amber)) center bottom/44px 1px no-repeat;}
.tag.b{background:var(--pink-soft); color:#8d3a5c;}
"""

COMMON_CSS = """
/* preview chrome + house callout rule (tinted, no side-stripes) */
.dxn-bar{width:min(600px,100%); margin:14px auto 10px; display:flex; flex-wrap:wrap; gap:4px 16px;
  align-items:center; justify-content:center; font-family:'Marcellus',serif; font-size:10.5px;
  letter-spacing:.13em; text-transform:uppercase; color:#7a7263; text-align:center; padding:0 12px;}
.dxn-bar a{color:#5b5344; text-decoration:underline; text-underline-offset:3px;}
.dxn-bar .dxn-name{color:#3b362c;}
.masteryband{border:1px solid var(--line); border-radius:11px; background:var(--amber-soft);}
.cookwarn{border:1px solid var(--line); border-radius:12px; background:var(--beet-soft,#F4E3E9);}
@media print{.dxn-bar{display:none !important;}}
"""

CSS_PORCELAIN = CSS_PORCELAIN.replace('SCALLOP_SVG', SCALLOP)
CSS_GARDEN = CSS_GARDEN.replace('POSY_SVG', POSY)

DIRECTIONS = [
    ('porcelain',  'Porcelain minimal', CSS_PORCELAIN),
    ('garden',     'Provence garden',   CSS_GARDEN),
    ('apothecary', 'Linen apothecary',  CSS_APOTHECARY),
]

NOCACHE = ('<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n'
           '<meta http-equiv="Pragma" content="no-cache">\n'
           '<meta http-equiv="Expires" content="0">')

for i, (slug, name, css) in enumerate(DIRECTIONS):
    outdir = os.path.join(DESIGN, slug)
    os.makedirs(outdir, exist_ok=True)
    others = [(s, n) for s, n, _ in DIRECTIONS if s != slug]
    for fname, html in SRC.items():
        h = html
        h = h.replace('<title>', '<title>' + name + ' · ', 1)
        if fname == 'week1.html':
            h = h.replace('../cook-cards/index.html?v=w1', 'index.html?v=d1')
            h = h.replace('../cook-cards/', '../../cook-cards/')
            h = h.replace('liver-cutlets.html?v=w1', 'liver-cutlets.html?v=d1')
        elif fname == 'liver-cutlets.html':
            h = h.replace('<a href="index.html">', '<a href="week1.html?v=d1">')
        elif fname == 'liver-cutlets-mum.html':
            h = h.replace('href="index.html"', 'href="week1.html?v=d1"')
        elif fname == 'index.html':
            for t in ['main-meals.html', 'drinks.html', 'snacks.html', 'desserts.html']:
                h = h.replace('href="' + t + '"', 'href="../../cook-cards/' + t + '"')
            h = h.replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                          '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + NOCACHE)
        if fname == 'week1.html':
            h = swap_images(h, SWAP_WEEK1)
        elif fname in ('liver-cutlets.html', 'liver-cutlets-mum.html'):
            h = swap_images(h, SWAP_CARD)
        h = h.replace('</head>', '<style id="direction">' + css + COMMON_CSS + '</style>\n'
                      '<!-- photos: approved v2 anchors where available -->\n</head>', 1)
        links = ' · '.join('<a href="../' + s + '/' + fname + '?v=d1">' + n + '</a>' for s, n in others)
        bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; All directions</a>'
               '<span class="dxn-name">Direction ' + str(i + 1) + ' · ' + name + '</span>'
               '<span>See in: ' + links + '</span></div>')
        h = h.replace('<body>', '<body>\n' + bar, 1)
        with open(os.path.join(outdir, fname), 'w') as f:
            f.write(h)
        print(slug + '/' + fname, len(h), 'bytes')

# ------------------------------------------------------------------ pantry × garden
# Ilma (2026-07-09 eve): "look at the pantry — how would you match that in provence
# garden style — give me 3 options". The pantry preview has its OWN chrome (parallel
# chat), so these are class-level literal overrides, not the card token swap.
# Content (incl. its 4 labels) is untouched — the 3-label reconcile is the Unify session.
PANTRY_SRC = open(os.path.join(ROOT, 'pantry-preview.html')).read()

PANTRY_COMMON = """
.dxn-bar{width:100%; margin:0 auto 6px; display:flex; flex-wrap:wrap; gap:4px 16px;
  align-items:center; justify-content:center; font-family:'Marcellus',serif; font-size:10.5px;
  letter-spacing:.13em; text-transform:uppercase; color:#7a7263; text-align:center; padding:0 12px;}
.dxn-bar a{color:#5b5344; text-decoration:underline; text-underline-offset:3px;}
.dxn-bar .dxn-name{color:#3b362c;}
@media print{.dxn-bar{display:none !important;}}
/* house label harmony: bf note = soft beet, tradition = amber (full reconcile in Unify) */
.lbl.w{background:rgba(156,43,78,.10); color:#8d3a5c;}
.lbl.t{background:rgba(192,138,67,.16); color:#8a6326;}
/* the garden posy under each screen title */
.h1::after{content:""; display:block; width:96px; height:20px; margin:5px auto 0;
  background:POSY_SVG center/contain no-repeat;}
"""

CSS_PANTRY_A = """
/* PANTRY OPTION A — SAME COAT: the pantry wears exactly the garden card chrome —
   cream paper, lavender headings, azure counts, iris actions, posy under the title. */
body{background:#DADEC7; background-image:radial-gradient(circle at 25% 10%, rgba(255,255,255,.4), transparent 55%);}
.scr{background:#FAF5E8;}
.scr .bg{background:radial-gradient(130% 24% at 50% 0%, #EFE9F5, rgba(239,233,245,0)), #FAF5E8;}
.h1,.cap .tt,.row .nm,.hrow .nm,.dtop .nm,.note h3{color:#3B362C;}
.kick,.dsec,.hintbox .tk,.hintbox p b{color:#5D5382;}
.cap .no{background:#5D5382;}
.shf .nm{color:#4D6852;}
.row .cc b{color:#46608A;}
.doors button.on{color:#5D5382;}
.gobtn,.elsebox button,.restock .rr .ord{background:#6D5F92;}
.mic{background:radial-gradient(circle at 35% 30%, #9C8FC0, #6D5F92); box-shadow:0 8px 24px rgba(109,95,146,.4);}
.mic:after{border-color:rgba(109,95,146,.35);}
.hintbox{border-color:#CFC7E0; background:rgba(124,110,158,.08);}
.dots i.on{background:#5D5382;}
.dtop .sub{color:#7C6E9E;}
.rl{color:#46608A; border-bottom-color:#8FA6C8;}
.sheet{background:#FFFDF5;}
.st.full i{background:#6E8A6F;}
.seg3 button.on.s-full{background:#6E8A6F;}
"""

CSS_PANTRY_B = """
/* PANTRY OPTION B — THE AMBER SHELF: the pantry keeps its own apothecary-amber
   character (gold buttons, amber kickers) but moves into the garden — garden ground,
   posy, azure counts, lavender whispers. A distinct room in the same house. */
body{background:#DADEC7; background-image:radial-gradient(circle at 25% 10%, rgba(255,255,255,.4), transparent 55%);}
.scr{background:#F7F0E1;}
.row .cc b{color:#5E739B;}
.hintbox{border-color:#CFC7E0;}
.dtop .sub{color:#8678A2;}
.dots i.on{background:#8678A2;}
"""

CSS_PANTRY_C = """
/* PANTRY OPTION C — THE FRESH LARDER: the brightest room in the garden house —
   porcelain-white screens, sage headings & actions, lavender fine print, azure counts. */
body{background:#DADEC7; background-image:radial-gradient(circle at 25% 10%, rgba(255,255,255,.4), transparent 55%);}
.scr{background:#FCFAF3;}
.scr .bg{background:radial-gradient(130% 24% at 50% 0%, #FFFFFF, rgba(255,255,255,0)), #FCFAF3;}
.h1,.cap .tt,.row .nm,.hrow .nm,.dtop .nm,.note h3{color:#3D392F;}
.kick{color:#8C81A9;}
.dsec,.hintbox .tk,.hintbox p b{color:#546E59;}
.cap .no{background:#546E59;}
.shf .nm{color:#546E59;}
.row .cc b{color:#7E96B8;}
.gobtn,.elsebox button,.restock .rr .ord{background:#546E59;}
.mic{background:radial-gradient(circle at 35% 30%, #8FA893, #546E59); box-shadow:0 8px 24px rgba(84,110,89,.4);}
.mic:after{border-color:rgba(84,110,89,.35);}
.hintbox{border-color:#DCE3DC; background:rgba(84,110,89,.07);}
.dots i.on{background:#7E96B8;}
.dtop .sub{color:#7C6E9E;}
.rl{color:#546E59;}
.sheet{background:#FFFFFF;}
.st.full i{background:#6E8A6F;}
.seg3 button.on.s-full{background:#6E8A6F;}
"""

PANTRY_OPTS = [
    ('pantry-a', 'A', 'Same coat as the cards', CSS_PANTRY_A),
    ('pantry-b', 'B', 'The amber shelf', CSS_PANTRY_B),
    ('pantry-c', 'C', 'The fresh larder', CSS_PANTRY_C),
]
for slug, letter, name, css in PANTRY_OPTS:
    h = PANTRY_SRC
    h = h.replace('<title>', '<title>Pantry in Garden ' + letter + ' — ' + name + ' · ', 1)
    common = PANTRY_COMMON.replace('POSY_SVG', POSY)
    h = h.replace('</head>', '<style id="direction">' + css + common + '</style>\n</head>', 1)
    others = ' · '.join('<a href="' + s + '.html?v=d1">' + l + ' — ' + n + '</a>'
                        for s, l, n, _ in PANTRY_OPTS if s != slug)
    bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; All directions</a>'
           '<span class="dxn-name">Pantry &times; Provence garden &middot; Option ' + letter +
           ' &middot; ' + name + '</span><span>Also: ' + others + '</span></div>')
    h = h.replace('<body>', '<body>\n' + bar, 1)
    with open(os.path.join(DESIGN, 'garden', slug + '.html'), 'w') as f:
        f.write(h)
    print('garden/' + slug + '.html', len(h), 'bytes')

# ------------------------------------------------------------- golden light options
# Ilma (2026-07-10, on pantry B): "LIKE THE GOLDEN FROM TOP DOWN — how to make the
# whole app consistent with this background — give me options."
# The golden = pantry-B's morning-light wash (#F6E8C7 radial from the screen top).
# Three treatments over the Garden direction, at the same depth as design/garden/
# so all relative link rewrites stay valid.
GOLD_ROOMS = """
/* GOLDEN 1 — LIGHT INSIDE THE ROOMS: cool green garden page; every card, screen and
   tile glows gold from its top. Green outside, golden inside. */
body{background:#D6DCC2; background-image:radial-gradient(circle at 25% 10%, rgba(255,255,255,.4), transparent 55%);}
.card{background-image:radial-gradient(140% 30% at 50% 0%, #F3DFA8, rgba(243,223,168,0) 72%);}
.pscreen{background-image:radial-gradient(140% 26% at 50% 0%, #F3DFA8, rgba(243,223,168,0) 72%);}
.tile{background-image:radial-gradient(160% 80% at 50% 0%, rgba(243,223,168,.6), rgba(243,223,168,0) 80%);}
.more a{background-image:radial-gradient(160% 90% at 50% 0%, rgba(243,223,168,.45), rgba(243,223,168,0) 80%);}
"""
GOLD_GROUND = """
/* GOLDEN 2 — GOLDEN MORNING GROUND: the page itself is unmistakably golden, lit from
   above; cards, tiles and screens stay clean cool cream. Golden outside, cream inside. */
body{background:#DCCFA4; background-image:radial-gradient(120% 42% at 50% 0%, rgba(246,229,183,1), rgba(246,229,183,0) 70%);}
"""
GOLD_FULL = """
/* GOLDEN 3 — FULL GOLDEN HOUR: both at once — golden page AND golden light inside
   every room and tile. The warmest, most enveloping read. */
body{background:#DCCFA4; background-image:radial-gradient(120% 42% at 50% 0%, rgba(246,229,183,1), rgba(246,229,183,0) 70%);}
.card{background-image:radial-gradient(140% 30% at 50% 0%, #F3DFA8, rgba(243,223,168,0) 72%);}
.pscreen{background-image:radial-gradient(140% 26% at 50% 0%, #F3DFA8, rgba(243,223,168,0) 72%);}
.tile{background-image:radial-gradient(160% 80% at 50% 0%, rgba(243,223,168,.6), rgba(243,223,168,0) 80%);}
.more a{background-image:radial-gradient(160% 90% at 50% 0%, rgba(243,223,168,.45), rgba(243,223,168,0) 80%);}
"""
GOLD_PANTRY_GROUND = """
body{background:#DCCFA4; background-image:radial-gradient(120% 42% at 50% 0%, rgba(246,229,183,1), rgba(246,229,183,0) 70%);}
"""

GOLDEN = [
    ('golden1', '1', 'Gold inside the rooms', GOLD_ROOMS, ''),
    ('golden2', '2', 'Golden morning ground', GOLD_GROUND, GOLD_PANTRY_GROUND),
    ('golden3', '3', 'Full golden hour', GOLD_FULL, GOLD_PANTRY_GROUND),
]
for gslug, gnum, gname, gcss, gpantry in GOLDEN:
    outdir = os.path.join(DESIGN, gslug)
    os.makedirs(outdir, exist_ok=True)
    others = [(s, n) for s, _, n, _, _ in GOLDEN if s != gslug]
    # the four card surfaces, garden direction + golden treatment
    for fname, html in SRC.items():
        h = html
        h = h.replace('<title>', '<title>Golden ' + gnum + ' — ' + gname + ' · ', 1)
        if fname == 'week1.html':
            h = h.replace('../cook-cards/index.html?v=w1', 'index.html?v=d1')
            h = h.replace('../cook-cards/', '../../cook-cards/')
            h = h.replace('liver-cutlets.html?v=w1', 'liver-cutlets.html?v=d1')
        elif fname == 'liver-cutlets.html':
            h = h.replace('<a href="index.html">', '<a href="week1.html?v=d1">')
        elif fname == 'liver-cutlets-mum.html':
            h = h.replace('href="index.html"', 'href="week1.html?v=d1"')
        elif fname == 'index.html':
            for t in ['main-meals.html', 'drinks.html', 'snacks.html', 'desserts.html']:
                h = h.replace('href="' + t + '"', 'href="../../cook-cards/' + t + '"')
            h = h.replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                          '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + NOCACHE)
        if fname == 'week1.html':
            h = swap_images(h, SWAP_WEEK1)
        elif fname in ('liver-cutlets.html', 'liver-cutlets-mum.html'):
            h = swap_images(h, SWAP_CARD)
        h = h.replace('</head>', '<style id="direction">' + CSS_GARDEN + gcss + COMMON_CSS + '</style>\n'
                      '<!-- photos: approved v2 anchors where available -->\n</head>', 1)
        links = ' · '.join('<a href="../' + s + '/' + fname + '?v=d1">' + n + '</a>' for s, n in others)
        bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; All directions</a>'
               '<span class="dxn-name">Golden ' + gnum + ' · ' + gname + ' (on Garden)</span>'
               '<span>Also: ' + links + ' · <a href="../garden/' + fname + '?v=d1">No gold</a></span></div>')
        h = h.replace('<body>', '<body>\n' + bar, 1)
        with open(os.path.join(outdir, fname), 'w') as f:
            f.write(h)
        print(gslug + '/' + fname, len(h), 'bytes')
    # the pantry, option B + golden treatment
    h = PANTRY_SRC
    h = h.replace('<title>', '<title>Golden ' + gnum + ' — pantry (amber shelf) · ', 1)
    common = PANTRY_COMMON.replace('POSY_SVG', POSY)
    h = h.replace('</head>', '<style id="direction">' + CSS_PANTRY_B + gpantry + common + '</style>\n</head>', 1)
    links = ' · '.join('<a href="../' + s + '/pantry.html?v=d1">' + n + '</a>' for s, n in others)
    bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; All directions</a>'
           '<span class="dxn-name">Golden ' + gnum + ' · ' + gname + ' · pantry B</span>'
           '<span>Also: ' + links + '</span></div>')
    h = h.replace('<body>', '<body>\n' + bar, 1)
    with open(os.path.join(outdir, 'pantry.html'), 'w') as f:
        f.write(h)
    print(gslug + '/pantry.html', len(h), 'bytes')

# --------------------------------------------------------------- THE PICK (Apple discipline)
# Ilma (2026-07-10): "if it was apple design how would they do it? too much going on for me."
# One assembled design from her revealed taste — no more parallel option sets:
# white rooms + air, ONE quiet label ink, faint golden dawn at the page top (the wash she
# loved, demoted to light), posy as the single signature motif, sage+beet functional,
# lavender/azure/pink live in content (chips, posy, photos) not chrome.
CSS_APPLE = """
/* THE PICK — Apple discipline x her Provence */
:root{
  --paper:#FFFFFF; --paper2:#FDFBF6; --sage:#7A917C; --sage-d:#54705A; --sage-soft:#E9EFE7;
  --amber:#B08A50; --amber-soft:#F1E7D2; --ink:#37332B; --ink2:#75705F; --line:#ECE5D6;
  --beet:#9C2B4E; --beet-soft:#F6E7EC;
  --lav:#8C81A9; --lav-soft:#EEEBF4; --pink:#C98A9B; --pink-soft:#F7E9ED; --azure:#7E96B8;
}
body{background:#FAF6EC; background-image:radial-gradient(120% 20% at 50% 0%, rgba(246,232,199,.55), rgba(246,232,199,0) 70%);}
.sech,.blockh,.hkicker,.ovscale-lab,.tkind,.metarow b,.eyebrow,.brandtag,.ctl-lab{color:#8B8371;}
h1,.tname,.askname{color:var(--ink);}
.tile{background:#FFFFFF; border:1px solid var(--line); border-radius:16px;
      box-shadow:0 1px 2px rgba(60,50,30,.05), 0 10px 28px rgba(60,50,30,.07);}
.tile:hover{transform:none; box-shadow:0 1px 2px rgba(60,50,30,.06), 0 14px 32px rgba(60,50,30,.10);}
.tile img{box-shadow:none; border:1px solid var(--line);}
.more a{background:#FFFFFF;}
.card{box-shadow:0 1px 2px rgba(60,50,30,.05), 0 22px 48px rgba(60,50,30,.10);}
.pscreen{background:#FDFBF6;}
.hero{border:6px solid #fff; box-shadow:0 10px 24px rgba(60,50,30,.12);}
.whenband{background:var(--sage-soft); color:#48604E;}
.whenband b{color:#48604E;}
.rule,.brandrule{width:104px; height:26px; background:POSY_SVG center/contain no-repeat;}
.step .n{background:var(--sage-d);}
.dots i.on{background:var(--sage-d);}
.cooknote{background:var(--beet-soft); color:#7a2740;}
.tag.b{background:var(--pink-soft); color:#9A4B62;}
.gqty{background:var(--sage-soft);}
"""
CSS_APPLE = CSS_APPLE.replace('POSY_SVG', POSY)

CSS_APPLE_PANTRY = """
body{background:#FAF6EC; background-image:radial-gradient(120% 20% at 50% 0%, rgba(246,232,199,.55), rgba(246,232,199,0) 70%);}
.scr{background:#FDFBF6;}
.scr .bg{background:radial-gradient(130% 22% at 50% 0%, #F6E8C7, rgba(246,232,199,0) 65%), #FDFBF6;}
.kick,.dsec,.hintbox .tk{color:#8B8371;}
.h1,.cap .tt,.row .nm,.hrow .nm,.dtop .nm,.note h3{color:#37332B;}
.cap .no{background:#54705A;}
.shf .nm{color:#37332B;}
.row .cc b{color:#75705F;}
.gobtn,.elsebox button,.restock .rr .ord{background:#54705A;}
.mic{background:radial-gradient(circle at 35% 30%, #8FA893, #54705A); box-shadow:0 8px 24px rgba(84,112,90,.4);}
.mic:after{border-color:rgba(84,112,90,.35);}
.hintbox{border-color:#ECE5D6; background:#FDFBF6;}
.hintbox p b{color:#54705A;}
.dots i.on{background:#54705A;}
.dtop .sub{color:#8B8371;}
.rl{color:#54705A;}
.sheet{background:#FFFFFF;}
.st.full i{background:#7A917C;}
.seg3 button.on.s-full{background:#7A917C;}
"""

outdir = os.path.join(DESIGN, 'apple')
os.makedirs(outdir, exist_ok=True)
for fname, html in SRC.items():
    h = html
    h = h.replace('<title>', '<title>The Pick · ', 1)
    if fname == 'week1.html':
        h = h.replace('../cook-cards/index.html?v=w1', 'index.html?v=d1')
        h = h.replace('../cook-cards/', '../../cook-cards/')
        h = h.replace('liver-cutlets.html?v=w1', 'liver-cutlets.html?v=d1')
    elif fname == 'liver-cutlets.html':
        h = h.replace('<a href="index.html">', '<a href="week1.html?v=d1">')
    elif fname == 'liver-cutlets-mum.html':
        h = h.replace('href="index.html"', 'href="week1.html?v=d1"')
    elif fname == 'index.html':
        for t in ['main-meals.html', 'drinks.html', 'snacks.html', 'desserts.html']:
            h = h.replace('href="' + t + '"', 'href="../../cook-cards/' + t + '"')
        h = h.replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                      '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + NOCACHE)
    if fname == 'week1.html':
        h = swap_images(h, SWAP_WEEK1)
    elif fname in ('liver-cutlets.html', 'liver-cutlets-mum.html'):
        h = swap_images(h, SWAP_CARD)
    h = h.replace('</head>', '<style id="direction">' + CSS_APPLE + COMMON_CSS + '</style>\n'
                  '<!-- photos: approved v2 anchors where available -->\n</head>', 1)
    bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; The parts library</a>'
           '<span class="dxn-name">The Pick · assembled, Apple discipline</span></div>')
    h = h.replace('<body>', '<body>\n' + bar, 1)
    with open(os.path.join(outdir, fname), 'w') as f:
        f.write(h)
    print('apple/' + fname, len(h), 'bytes')
h = PANTRY_SRC
h = h.replace('<title>', '<title>The Pick · pantry · ', 1)
common = PANTRY_COMMON.replace('POSY_SVG', POSY)
h = h.replace('</head>', '<style id="direction">' + CSS_APPLE_PANTRY + common + '</style>\n</head>', 1)
bar = ('<div class="dxn-bar"><a href="../index.html?v=d1">&larr; The parts library</a>'
       '<span class="dxn-name">The Pick · pantry</span></div>')
h = h.replace('<body>', '<body>\n' + bar, 1)
with open(os.path.join(outdir, 'pantry.html'), 'w') as f:
    f.write(h)
print('apple/pantry.html', len(h), 'bytes')
print('done')
