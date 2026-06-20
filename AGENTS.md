# Postpartum Kitchen — Agent Context / Handover

Canonical context for this project. **Read this first in any new session.** Last updated after the
typography + navigation + illustration + recipe-additions pass.

## 1. What this is
A Mediterranean × Chinese-confinement **postpartum recovery plan** — meals, tonics, recipes, a phased
recovery timeline, a supplement guide (private only), and an ingredient glossary. Built for energy,
fast repair and minimal postpartum hair loss. It is **one self-contained HTML file** that renders to
a responsive **web page** (GitHub Pages + a private gist) and to a **PDF**. Owner is exploring turning
it into a commercial product after getting feedback from other mums.

## 2. Links
- **Public (depersonalised, share with mums):** https://bobroviciuteilma-cell.github.io/postpartum-kitchen/
- **Private full version (unguessable secret-gist link, no login, noindex):**
  https://gist.githack.com/bobroviciuteilma-cell/4f79377838cb2d3da94912e48ee8eb14/raw/postpartum-kitchen-full.html
  (secret gist id `4f79377838cb2d3da94912e48ee8eb14`, file `postpartum-kitchen-full.html`)
- **Repo:** https://github.com/bobroviciuteilma-cell/postpartum-kitchen
- **Personal PDF (full version):** /Users/Enki/Desktop/Ilma_Postpartum_Kitchen.pdf
- `gh` is authenticated as **bobroviciuteilma-cell** (token scopes: gist, repo, workflow, read:org).

## 3. Two versions
- **Private master = `master.private.html`** (gitignored, NEVER published). Full personal version:
  the owner's supplement stack, candida/hemorrhoid notes, vaginal-birth specifics, "for you" notes,
  the Supplement Protocol page. This is the SOURCE OF TRUTH — edit this.
- **Public = `index.html`**, generated from the master by `build.py`, which: strips personal/medical
  detail, removes the Supplement Protocol page, renames "From Your Saved Feed" → "Community Recipes",
  renumbers the cover, and injects responsive `@media screen` CSS + a viewport tag.

## 4. Workflow (how to change ANYTHING)
1. Edit `master.private.html`.
2. `cd /Users/Enki/code/postpartum-kitchen && python3 build.py` → regenerates `index.html`.
3. `git add index.html [build.py] && git commit -m "..." && git push` → GitHub Pages updates ~1 min.
4. **Update the PRIVATE link** (re-upload to the secret gist):
   `python3 -c "h=open('master.private.html').read().replace('<meta charset=\"utf-8\">','<meta charset=\"utf-8\">\n<meta name=\"robots\" content=\"noindex, nofollow\">',1); open('/tmp/postpartum-kitchen-full.html','w').write(h)"`
   `gh gist edit 4f79377838cb2d3da94912e48ee8eb14 /tmp/postpartum-kitchen-full.html`
5. **Personal PDF:** render the master with headless Chrome:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=OUT.pdf "file://$PWD/master.private.html"`
6. **Always Read the rendered PDF pages back to verify** before declaring done. For web-only features
   (nav, tags) verify with `--dump-dom` or a `--screenshot` (screen media), NOT the print PDF.

## 5. Design system
- Palette: rust accent `#b0481f`, cream callout boxes `#fdf3ea`, **white page background baked in**
  (dark-mode safe — this fixed an invisible-text bug). Divider colours: plan `#b0481f`, meals
  `#c0633a`, kitchen `#3f7d6e`, community `#bb8a3a`.
- **Fonts (Google Fonts):** `Fraunces` (display serif — all titles/h1/h2) + `Inter` (body).
- Recipe cards: two-column `.twocol` ("WHAT YOU NEED" / "HOW TO MAKE IT"), numbered rust `.step .badge`,
  footer line. Content-heavy cards use `class="page dense"`.
- A4 print pages (`width:210mm`, `@page`) for PDF; `@media screen` makes it responsive on web.
- **Intro hero** (`.page.hero`): line-art SVG bowl-and-sprigs motif + Fraunces title + emoji pills.
- **Category dividers** (`.page.divider.{plan|meals|kitchen|community}`): full-colour break pages with
  white line-art SVG icon (compass / bowl / teacup / three bowls), `dnum`/`h2`/`dsub`.
- **Colour-coded tags**: `.tag.{iron|calcium|omega|protein|milk|gut|afterbirth}`.
- Cover contents: 2-column `.coverwrap`, **manually numbered** (renumber when adding sections; build.py
  also renumbers the public copy after removing the Supplement row).
- Section anchors (`id="..."`) power internal links; `<a>` handles link to original IG posts.

## 6. Self-building JS (three `<script>`s before `</body>`)
- **Contents nav**: a floating ☰ button → a drawer with a search box + category groups (legacy; hidden
  in app mode via `body.app #navBtn,#navPanel{display:none}`).
- **Auto-tagger**: scans each recipe/meal card's text and injects colour tags after the subtitle.
- **App router (primary UX, screen-only):** turns the doc into a calm home → category → recipe app.
  Adds `body.app`; hides all `section.page` and shows `#appHome` (cloned hero + **search bar** + a 2-col
  tile grid). Tap a tile → `#catList` (recipe list for that category); tap a recipe → that one
  `section.page.appActive` shows. **Search** (`#qq`) does full-text (`title+sub+textContent`, AND of
  terms) across a flat `ALL[]`, hides tiles, shows results tagged with their category colour.
  Categories live in the `CATS` array (7 food-type buckets: Plan & Meals, Salads, Soups & Bowls,
  Drinks & Tonics, Bakes & Breakfast, Snacks & Sweets, Glossary & Guide); `catFor(title)` matches by
  keyword, default catch-all is `CATS[5]` (Snacks). **No "Mains"/"Community" buckets — owner rejected
  source-based & vague labels; keep categories food-type and obvious.** `@media print` shows all
  sections so the PDF stays full & linear.
- All three run in the BROWSER only (they appear on the links but NOT in the printed PDF — that's fine).

## 7. Content map (current order; ~53 public pages, ~55 private)
Intro hero · Cover · **[Plan divider]** · Recovery Plan · Your Day Top to Bottom · Recovery Timeline ·
**[Meals divider]** · Breakfast · Lunch · Dinner · Snacks & Drinks · **[Tonics & Recipes divider]** ·
Bone Broth · Postpartum Teas · Ashwagandha Milk · Gond Laddu · Power Smoothie · Khichdi · Til-Gur Bites ·
Quick Tonics & Bites · Seeded Flax & Almond Loaf · Major Milk Makin' Cookies · Soothing Chai Tea ·
Sattvic Noodle Bowl · Best Foods for Recovery · Keto Rolls · Beef Bone Broth · Vedic Porridge ·
Chicken Liver Pâté · Postpartum Banana Bread · **[Supplement Protocol — PRIVATE ONLY]** · Helper Cook List ·
**[Community Recipes divider]** · Community Recipes index + 16 community cards · Glossary.

## 8. Conventions
- **"Tori's recipes"**: the owner's physical-collection additions are credited to Tori — Seeded Loaf,
  Major Milk Makin' Cookies (Tori's collection / Kathleen Major), Chai Tea, Sattvic Noodle Bowl,
  Best Foods, Keto Rolls, Beef Bone Broth, Vedic Porridge.
- **Gated recipes** (creator hides the recipe behind "comment for link") → rebuilt as a clearly-labelled
  *"My version"* (`.box.warn`) + link to the original. Still gated (real recipe to swap in when owner
  fetches it): Magic Chicken Soup (DWRc8g-E2-9, comment MAGIC), Cottage Cheese Bake (DXRnHuVjH0a, in
  comments), Blueberry Waffles (DY2pdDcPaKs, comment YUM), Cottage Cheese Truffle Balls (DX_GledxTIj,
  comment CHOC).
- **Credit + link** every web recipe to its creator (`saved from @handle →`).
- **Render gotcha:** headless Chrome here does NOT render CJK glyphs — keep text English-only.
- Health content is educational, NOT medical advice — keep that framing.
- Reformat recipes from owner's photos in your own concise wording + attribution (don't copy verbatim).

## 9. Owner profile
Ilma (GitHub bobroviciuteilma-cell). Solo technical builder (also runs espr-site on Vercel, Pleb Finance).
Third trimester ~mid-2026, planning a **vaginal birth**, has **hemorrhoids** and **candida**,
eats Mediterranean + keto-leaning. Decisive on scope, defers on tech detail, prefers crisp structured
choices, and is **VERY visual**. Supplement core: Thorne prenatal, CALM magnesium glycinate, choline,
Fem-Dophilus, + adding Nordic omega-3 and creatine, Plant-D3+K2. Has organic MCT oil. Doing bloods
(ferritin, 25-OH D, thyroid+TPO, hs-CRP) before adding zinc/iron.

## 10. Backlog / outstanding
1. **Painted illustrations (HIGH — in flight):** owner is generating warm hand-painted gouache art in
   the ChatGPT app (house-style prompt provided) for the hero + 4 dividers (+ optional per-category
   recipe icons). When she sends image files: put them in `assets/` in the repo, commit/push, and
   reference by **absolute URL** (`https://bobroviciuteilma-cell.github.io/postpartum-kitchen/assets/X.png`)
   so BOTH the Pages site and the githack gist resolve them. They replace/augment the current vector
   line-art on the hero + dividers. NOTE: in-session AI image generation (nano-banana) is NOT available.
2. **MCT oil** — add to the Glossary + a "+ ½ tsp MCT" line on the Power Smoothie card (offered, not yet done).
3. **Swap the 4 gated "My version" cards** for the real recipes once owner fetches them.
   - ✅ DONE (2026-06-20): added **13 recipes** from the 14 saved IG posts Ilma listed (2 pho posts merged).
     Recipe count 46 → **60**. Lithuanian/Spanish captions translated. **19 specific categories (2026-06-20):**
     The Plan · Sandwiches & Wraps · Salads · Burgers & Patties · Liver & Organs · Soups & Bowls · Cookies ·
     Pancakes · Waffles · Fritters · Porridge · Breads · Drinks & Tonics · Bites & Balls · Treats · Dips &
     Crackers · Bakes & Tarts · Ferments · Glossary & Guide. (Replaced the "Bakes & Breakfast"/"Snacks &
     Sweets" grab-bags.) CATEGORY PHILOSOPHY (Ilma, emphatic): **call things what they are; "Mains"/"Meals"
     are NOT categories** — specific food types, singletons OK (they grow), split freely (Pancakes≠Waffles).
     **"Treats" is a valid category** (treating yourself = real morale need). Every recipe needs a real
     postpartum "why". `CATS` order matters (catFor = first match wins): sandwiches before breads, drinks
     before bites. **GF tag**: curated title list in the auto-tagger (`var GF=[...]`) — conservative, wheat/
     pasta/tortilla recipes left unmarked; `.tag.gf` is green.
     Renamed "Plan & Meals" → "The Plan"; added "Sandwiches" (the Zucchini Bread Sandwich = her "tuna melt",
     moved out of Bakes — Sandwiches sits before Bakes in `CATS` so `sandwich` wins routing). Every recipe MUST
     show a **source hyperlink** (`@handle →` in the subtitle). Only add **nutrition / postpartum-appropriate**
     recipes from HER links — don't pull arbitrary content.
   - **IG scraping:** individual public post URLs → Apify `apify/instagram-scraper` (`directUrls`, `resultsType:posts`)
     works without a browser. But Ilma's **private saved folder** (`instagram.com/ilmabob/saved/food/...`) is NOT
     reachable that way — to add "the rest" of her saved collection, need the Claude-in-Chrome extension re-authed
     (it errored this session) OR Ilma pastes more post URLs. The `Control_Chrome` MCP listed tabs but errored on
     `get_page_content`/`execute_javascript` ("Chrome is not running").
4. **Functionality roadmap:**
   - ✅ DONE (2026-06-20): warm app **hero front door**; **goal-filter chips** ("How are you feeling?" →
     keyword filter via `GOALS` array in the app-router script); **Today's rhythm** (tickable daily
     checklist, `PLAN` array, saved to `localStorage` key `pk_today_<date>`); **Favourites** (♥, key
     `pk_favs`); **Shopping list** (bag icon harvests each recipe's `.ing` lines, key `pk_shop`);
     richer gradient category cards + "Start here" feature tile. Top bar = two icon buttons (heart=Picks,
     bag=List) with count badges. App bar is a 3-col grid (`auto | 1fr | auto`) so recipe actions never
     overflow; show via `bar.style.display='grid'` (do NOT use `display:…!important` on `#appBar` — it
     overrides the inline `display:none` used to hide it on home). Goal filter is **keyword-based**, so
     results are approximate (e.g. Glossary can match "iron") — tune `GOALS[].kw` if needed.
   - ✅ DONE (2026-06-20, batch 2): **Phase view** ("Where are you?" Week 1–2 / 3–4 / 5–6 pills via `PHASES`
     array, reuses `toggleGoal`/`goalHits`, shows a `.phasefocus` line); **Make-ahead flag** (auto-tagger
     rule: `freez`/`make ahead`/`meal prep` → `.tag.makeahead`).
   - ❌ REMOVED (2026-06-20): **Night mode** — Ilma: "i dont care about the night mode". Don't re-add.
   - **DIRECTION (2026-06-20):** Ilma chose **keep building the WEB version** — NOT a PWA/installable app yet.
     Focus on content + structure + the recovery flow; it stays a shareable link. PWA/app-icon (her gouache art)
     comes later. Personalisation quiz still deferred. To add more recipes/categories, need her saved-folder
     access (re-auth Claude-in-Chrome) or more pasted links.
   - Still open: Download-PDF button, feedback link for mum testers, per-category recipe icons, servings scaler.
5. **Commercial strategy session** (DEFERRED by owner until after birth + her own version is finalised):
   the real product = the **personalisation** (a guided "build your postpartum kitchen" quiz → tailored
   plan, done manually via Q&A). The goal-filter chips are a lightweight seed of this.
6. **Cover maintenance:** cover is manually numbered — renumber when adding sections (consider a more
   sustainable approach; print PDF needs static numbers so pure-JS numbering won't show in PDF).

## 11. How to resume
Open a new session with cwd = `/Users/Enki/code/postpartum-kitchen` (auto-loads CLAUDE.md → this file),
or paste the handover briefing. Then: edit `master.private.html` → `build.py` → push → update gist.
