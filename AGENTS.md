# Postpartum Kitchen — Agent Context

Canonical context for this project. Read this first in any new session.

## What this is
A Mediterranean × Chinese-confinement **postpartum recovery plan** — meals, tonics, recipes,
a phased recovery timeline, a supplement guide (private only), and a glossary. Built for energy,
fast repair, and minimal postpartum hair loss. Currently a single self-contained HTML doc that
renders to both a **web page** (GitHub Pages) and a **PDF**.

- **Live (public, shareable):** https://bobroviciuteilma-cell.github.io/postpartum-kitchen/
- **Private full version (unguessable secret-gist link, no login, noindex):**
  https://gist.githack.com/bobroviciuteilma-cell/4f79377838cb2d3da94912e48ee8eb14/raw/postpartum-kitchen-full.html
  (secret gist id `4f79377838cb2d3da94912e48ee8eb14`, file `postpartum-kitchen-full.html`)
- **Repo:** https://github.com/bobroviciuteilma-cell/postpartum-kitchen

## Two versions
- **Private master** = `master.private.html` (gitignored, NEVER published). Full personal version:
  the owner's supplement stack, candida/hemorrhoid notes, vaginal-birth specifics, "for you" notes.
  Render this to PDF for the owner's personal copy.
- **Public** = `index.html`, generated from the master by `build.py`, which strips personal/medical
  detail, removes the Supplement Protocol page, renames "From Your Saved Feed" → "Community Recipes",
  renumbers the cover, and injects responsive screen CSS.

## Workflow (how to change anything)
1. Edit `master.private.html` (the source of truth).
2. `cd /Users/Enki/code/postpartum-kitchen && python3 build.py`  → regenerates `index.html`.
3. `git add index.html build.py && git commit -m "..." && git push` → GitHub Pages updates ~1 min.
3b. Update the PRIVATE link (re-upload full version to the secret gist):
    `python3 -c "h=open('master.private.html').read().replace('<meta charset=\"utf-8\">','<meta charset=\"utf-8\">\n<meta name=\"robots\" content=\"noindex, nofollow\">',1); open('/tmp/postpartum-kitchen-full.html','w').write(h)"`
    `gh gist edit 4f79377838cb2d3da94912e48ee8eb14 /tmp/postpartum-kitchen-full.html`
4. Personal PDF: render the master with headless Chrome:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --no-pdf-header-footer --print-to-pdf=OUT.pdf "file://$PWD/master.private.html"`
   (Public PDF: same command on index.html.)
   Always Read the rendered PDF pages back to visually verify.

## Design system
- Rust accent `#b0481f`; cream callout boxes `#fdf3ea`; white page background (baked in — dark-mode safe).
- Recipe cards: two-column "WHAT YOU NEED / HOW TO MAKE IT", numbered rust step badges, footer line.
- A4 print pages (`width:210mm`, `@page`) for PDF; `@media screen` makes it responsive on web.
- Content-heavy pages use `class="page dense"`. Cover contents use a 2-column `.coverwrap`.
- Section anchors (`id="..."`) power internal links; `<a>` handles link to original IG posts.

## Conventions
- **Gated recipes** (creator hides the recipe behind "comment for the link"): rebuild as a clearly
  labelled *"My version"* with a `.box.warn`, and link to the original post. Currently labelled:
  Magic Chicken Soup, Cottage Cheese Bake, Blueberry Waffles, Cottage Cheese Truffle Balls.
- **Credit + link** every web recipe to its creator (`saved from @handle →`).
- **Render gotcha:** headless Chrome here does NOT render CJK glyphs — keep text English-only.
- Health content is educational, not medical advice — keep that framing.

## Outstanding / backlog
- Collect the 4 gated recipes (owner will fetch): DWRc8g-E2-9 (MAGIC), DXRnHuVjH0a (comments),
  DY2pdDcPaKs (YUM), DX_GledxTIj (CHOC) — swap "My version" cards for the real recipe when received.
- Add MCT oil to the glossary + a "+ ½ tsp MCT" line on the Power Smoothie card.
- Functionality roadmap (web): sticky contents nav, recipe tags/filter, Download-PDF button,
  feedback link for mom testers, favourites (localStorage), shopping-list generator, servings scaler.
- Commercial direction (post mom-feedback): the real product is the **personalisation** — a guided
  "build your postpartum kitchen" quiz → tailored plan (this was done manually via Q&A in the
  original build). Validate with moms first.

## Owner
Solo technical builder (also runs espr-site on Vercel, Pleb Finance). Prefers crisp structured
choices for decisions; defers on tech detail; decisive on scope.
