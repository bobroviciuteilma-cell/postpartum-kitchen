#!/usr/bin/env python3
"""
Build the PUBLIC, shareable version of the Postpartum Kitchen from the private master.
- Removes the personal Supplement Protocol page (your specific stack).
- Genericises personal/medical references (hemorrhoids, candida, "your helper", etc.).
- Renames "From Your Saved Feed" -> "Community Recipes".
- Adds a viewport tag + responsive (mobile-friendly) screen styles.
- Renumbers the cover contents.

Usage:  python3 build.py [MASTER_HTML] [OUTPUT_HTML]
Master defaults to the private file; output defaults to ./index.html
"""
import re, sys

MASTER = sys.argv[1] if len(sys.argv) > 1 else "master.private.html"
OUT    = sys.argv[2] if len(sys.argv) > 2 else "index.html"

html = open(MASTER, encoding="utf-8").read()

# 1) Remove the personal Supplement Protocol section entirely
html = re.sub(
    r'<!-- =+ 13\. SUPPLEMENT PROTOCOL =+ -->.*?(?=<!-- =+ 14\. HELPER)',
    '', html, flags=re.S)

# 2) Depersonalise phrases (order matters: specific before general)
repl = [
    ("you already have hemorrhoids, so ", ""),
    ("Stitches &amp; hemorrhoids:", "Stitches &amp; comfort:"),
    ("your candida", "gut &amp; candida"),
    ("you like keto", "you lean lower-carb"),
    ("Your Helper's Cook List", "Helper Cook List"),
    ("your helper", "a helper"),
    ("a vaginal birth", "birth"),
    ("vaginal birth", "birth"),
    ("From Your Saved Feed", "Community Recipes"),
    ("Your Instagram picks, built into recipe cards", "Great recipes from around the web, built into cards"),
    ("your Instagram picks as cards", "great recipes from around the web"),
    ("your Instagram picks, built into recipe cards", "great recipes from around the web"),
    ("For you:", "Good to know:"),
]
for a, b in repl:
    html = html.replace(a, b)

# 3) Remove the Supplement Protocol row from the cover, then renumber every cover row
html = re.sub(
    r'\s*<div class="row"><div class="n">\d+\.</div><div class="t"><b>Supplement Protocol</b>.*?</div></div></div>',
    '', html, flags=re.S)
_n = [0]
def _renum(m):
    _n[0] += 1
    return f'<div class="n">{_n[0]}.</div>'
html = re.sub(r'<div class="n">\d+\.</div>', _renum, html)

# 4) Add viewport meta
html = html.replace('<meta charset="utf-8">',
                    '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">')

# 5) Responsive screen styles (print/@page rules are untouched -> PDF still works)
responsive = """
  /* ---- screen / responsive (does not affect print/PDF) ---- */
  @media screen {
    body{ background:#ece8e3; }
    .page{ width:210mm; margin:18px auto; box-shadow:0 1px 8px rgba(0,0,0,.12); }
  }
  @media screen and (max-width: 840px){
    .page{ width:auto; max-width:100%; min-height:auto; margin:0 0 10px; padding:30px 18px; box-shadow:none; border-bottom:6px solid #ece8e3; }
    .twocol{ grid-template-columns:1fr !important; gap:6px !important; }
    .coverwrap, .glosswrap{ column-count:1 !important; }
    .rhythm .r{ grid-template-columns:90px 1fr !important; }
    .days{ grid-template-columns:1fr !important; }
    h1.title{ font-size:21px; }
    .cover h1{ font-size:27px; }
    .cover{ padding-top:24px; }
    .inside{ max-width:100%; }
    table.stack td.k{ width:34%; } table.stack td.w{ width:30%; }
  }
"""
html = html.replace('</style>', responsive + '</style>')

open(OUT, "w", encoding="utf-8").write(html)
print(f"built {OUT} ({len(html)} bytes)")
