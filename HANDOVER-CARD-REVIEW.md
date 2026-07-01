# HANDOVER — Review & Fix ALL existing Cook Cards (fresh-chat playbook)

You are doing a **quality pass over every Cook Card already built** in `cook-cards/`. This is NOT
new-card building — the cards exist and are live. Your job: **open each one, check it against the
rules, fix what's wrong, redeploy.** Only surface a card to Ilma once it passes. Multiple chats may
split this — **own whole cards** (never two chats editing the same file), take a GROUP from §2.

Ilma is due any day and breastfeeding. Keep it fast and correct; don't ask her to re-review things
you can verify yourself.

## 0. Read first
- `HANDOVER-CARDS.md` — the full build/design/deploy playbook. **§2 (LOCKED design rules)** and
  **§3B (self-review checklist)** are your review criteria. Don't restate them; apply them.
- Memory: **feedback_cook_cards_visual** (locked design), **project_ilma_pantry** (what she HAS —
  she confirmed she has every card ingredient; don't re-flag), **feedback_max_boost** (fold boosts
  into the core, don't footnote), **feedback_mistakes_log** (what not to repeat).
- `RECIPE-CATALOG.md` + `recipe-catalog-data/ig-food-index.md` — **the source-link lookup** (see §3).

## 1. What "review" means — the 5 things to check per card
For EACH card, in the preview (`python3 -m http.server 8878 --directory cook-cards`, or the
`cookcards` launch config), verify and FIX:

1. **MAX-BOOST** — is every relevant pantry beneficial folded into the CORE recipe (not a footnote)?
   Protein/collagen (beef gelatin), omega-3 seeds (flax/chia/pumpkin), minerals, blood-builders.
   If a boost is missing or buried, add it into the ingredient list + name what it adds. She'd
   rather subtract than not know.
2. **ACCURACY** — is the recipe the FULL correct version, not stripped or wrong? Cross-check the
   original (index.html / the IG caption in ig-food-index.md). Known past misses: Adrenal needs
   cream of tartar; Meat Stock Latte needs egg yolks; Morning Waters = amla+ajwain (not lemon);
   Veggie Patties binder = almond flour (not breadcrumbs). Quantities sane for HER kit (1.6 L
   Kilner, beef gelatin). Every amount quantified — no lone "pinch/crack/thumb".
3. **BALANCE** — render it: measure `.leftcol` height vs `.steps` height. If off by >40px, move or
   add the "Just for you"/boost note into the shorter column until they're within 40px. Sprig→
   wordmark gap ≥16px. Eyebrow on ONE line.
4. **SOURCE ATTRIBUTION (the big one this pass)** — the `.lineage` note must LEAD with provenance
   and **any creator credit must hyperlink the EXACT recipe** (the specific IG reel / blog post for
   THAT dish) — never a bare `@handle`, a profile link, or a homepage. See §3 for how to find the
   exact link. Label as `From @creator (link)` / `Traditional` / `Your recipe`, then name the boost.
   **Evidence only — never invent a source.** If you can't find the exact URL, leave it as
   `Traditional`/`Your recipe` or flag "no source on file" — do NOT ship a plain handle.
5. **CLEAN** — no emoji/emoticons, no ✓ ticks; every ingredient + step has a real photo (0 broken
   images: `img.naturalWidth>0`); step numbers filled; tabs = Main Meals·Snacks·Drinks·Desserts
   with the one category in beet `#9c2b4e`; drinks have a "When to drink" band, dishes a "when to
   eat" line.

Run this static pre-check per card first (catches the cheap failures), then render for balance:
```python
import re; h=open("cook-cards/SLUG.html",encoding="utf-8").read(); b=h.split("</style>")[-1]
print("emoji:", re.findall(r'[\U0001F000-\U0001FAFF☀-➿]', b) or "none",
      "| unembedded:", len(re.findall(r'src=\"[^\"]+\.png\"', h)),
      "| brand:", "Your Healing Kitchen" in h,
      "| lineage-link:", ("href" in (re.search(r'class="lineage".*?</div>', h, re.S) or type('',(),{'group':lambda s,*a:""})()).group(0) if 'lineage' in h else "NO lineage"))
```

## 2. The inventory — 38 cards, grouped (take a group per chat)
**A · Drinks & tonics (14)** — beet-kvass-card, golden-milk-card, caraway-tea-card, fennel-tea-card,
nettle-tea-card, jujube-goji-tea, ccf-tea, chai-tea, adrenal-cocktail, ashwagandha-milk,
almond-date-saffron, power-smoothie, meat-stock-latte, morning-waters. *(indexed by `drinks.html`)*

**B · Soups / stews / broths (8)** — chicken-bone-broth-card, borscht, oxtail-heart-stew,
clams-garlic-broth, short-rib-pho, magic-chicken-soup, mushroom-soup, lemon-egg-chicken-soup.

**C · Snacks / bites / pâté (5)** — nut-date-balls, sesame-date-bites, date-oat-bites,
liver-pate-pops, chicken-liver-pate-card.

**D · Mains / dishes / salads (6)** — greek-chicken-burgers, chicken-potato-cutlets,
veggie-patties-card, sardine-tahini-salad, iron-orzo-salad, grain-bowls.

**E · Cottage cheese / oats / waffles (5)** — cottage-cheese-bake, cottage-cheese-pancakes,
cottage-cheese-set, soaked-mineral-oats-card, blueberry-waffles.

> Origin of each group (for context on likely defects): A = batch-A drinks chat (several were under-
> maxed/stripped and already fixed once — re-verify). B = batch-E soups chat (NOT yet reviewed by
> Ilma — check carefully). C/D/E = later dish/snack chats. Ilma's own hand-built: beet-kvass, the 3
> teas, chicken-bone-broth, soaked-oats, golden-milk, chicken-liver-pate, veggie-patties (lighter
> touch, but still check source links).

## 3. Finding the EXACT recipe link (do this right — it's why this pass exists)
A credit like "From @raquels.pantry" with no link, or linking her profile, is WRONG. Find the
specific post:
1. **`index.html`** — each library recipe's `<div class="subtitle">` carries the creator @handle +
   the exact IG/blog URL. This is the primary source of truth for library recipes.
2. **`recipe-catalog-data/ig-food-index.md`** — all 1,313 of Ilma's IG saves, each with its caption
   snippet + **permalink**. Grep it for the dish name / handle to find the exact reel URL:
   `grep -in "sardine\|tahini" recipe-catalog-data/ig-food-index.md`. The permalink IS the canonical
   source (opening it shows the creator + full recipe).
3. **`RECIPE-CATALOG.md`** — the audit chat already resolved many card→exact-link mappings in its
   Bucket A tables (e.g. Iron Orzo → `@raquels.pantry` → `instagram.com/p/DY1t5GJoO_9/`). Reuse them.
4. If none of the above has it and Ilma hasn't given the link: do NOT guess. Label `Traditional`
   (classic dish, no single author) or `Your recipe`, or flag "no source on file — ask Ilma".
5. **Verify the link resolves** and matches the dish before writing it in. Flag dead/removed posts.

Format (from HANDOVER-CARDS.md §2):
`From <b>@handle</b> (<a href="EXACT-URL">link</a>) — [what it is] — <b>boosted</b> with […]. [tradition/verified framing].`
Multi-source ("keep both"): `From <b>@base</b> (recipe); [idea] from <b>@other</b> (link).`
Known correction: **Chicken Liver Pâté = @sokoladassiela**; the Pâté **Pops** freeze-idea =
@wildnutritionist ("keep both").

## 4. Deploy (parallel-safe — same as HANDOVER-CARDS.md §4)
- `git pull --rebase origin main` → `git add cook-cards/<only-the-cards-you-fixed>.html` → commit
  (msg ends `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`) → `git push`.
- **Never** `git add` a card another chat owns, or `index.html`.
- Poll `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/cook-cards/<slug>.html?v=N` until
  HTTP 200 (Pages/CDN lags 1–5 min; parallel chats queue builds). Bump `?v=` on every change.

## 5. Report back to Ilma
Give her a compact table per group: `card · what you fixed (or "clean") · new ?v= link`. Lead with a
one-liner: *"reviewed N cards — fixed max-boost on X, source links on Y, balance on Z; all self-QA
passed (no emoji · balanced · maxed · full recipe · exact source links · 0 broken images)."* Only
list links for cards that pass.

---
*If `/tmp/cookcards/.env` (her OpenAI key) is missing you can still review/fix text + source links
and rebalance columns; you only need it to regenerate a wrong/missing photo.*
