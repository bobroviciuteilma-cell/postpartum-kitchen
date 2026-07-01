# HANDOVER — Build Postpartum Cook Cards (fresh-chat playbook)

You are building **image-led recipe "Cook Cards"** for Ilma's postpartum kitchen, matching the LOCKED template, then publishing each to GitHub Pages and giving her a `?v=` link to review. Multiple chats run this in parallel — **only build the cards in YOUR batch** (given at the end of the prompt that sent you here).

## 0. Read first (this project's memory + reference cards)
- Memory: **feedback_cook_cards_visual** (design rules), **project_ilma_pantry** (what she has), **feedback_mistakes_log** (what NOT to repeat).
- Reference cards already built — **copy their structure exactly**:
  - `cook-cards/beet-kvass-card.html` — the DISH layout (step photos + a visual guide).
  - `cook-cards/golden-milk-card.html` and `cook-cards/nettle-tea-card.html` — the DRINK layout (When-to-drink band, text steps, "Just for you" note in the right column).

## 1. Pipeline (per card)
1. **Recipe → ingredients + steps.** Use ONLY her pantry (project_ilma_pantry) + what she gave; invent nothing. Flag anything a recipe needs that she may not have.
2. **Images (gpt-image-1).** `cd /tmp/cookcards && set -a; . ./.env; set +a` (sources her key — never print it). Style prompt is locked — copy the `STYLE`/`ING` strings from `/tmp/cookcards/genkvass.py`.
   - **REUSE the library first**: `ls /tmp/cookcards/small/ /tmp/cookcards/*.png` — many ingredients already exist (ginger, turmeric, cinnamon, milk, honey, lemon, water, ghee, red dates, goji, chicken feet/necks, cumin/coriander/fennel, etc.). Only generate NEW ones.
   - Generate at `size 1024x1024, quality medium`; then downscale: `sips -Z 520 X.png --out small/X.png`.
   - **One photo per ingredient AND per step, plus a hero.** Never an emoji placeholder — if there's no photo (e.g. water, honey, lemon), generate one.
3. **Build the HTML** from the template: reuse the entire `<head>` (CSS) from a reference card; write the body (brandbar sprig → head → meta → When-to-drink band → why → leftcol ingredients → steps (+ "Just for you" note) → foot → tabs). Drinks = golden-milk/tea layout; dishes = beet-kvass layout (with step photos).
4. **Embed** every image as base64 into a self-contained file at `cook-cards/<slug>.html` (INSIDE the repo — never leave it in /tmp).
5. **VERIFY** (section 3 — mandatory).
6. **Deploy** (section 4).

## 2. LOCKED design rules (do not deviate)
- **Header:** botanical sprig + *"Your Healing Kitchen"* + tagline (copy the sprig `<svg>` + `.brandbar` from a reference card). **No spiral binding.**
- **NO emoticons/emoji, no ticks** anywhere.
- **Every ingredient + step has a real photo.**
- **Type scale:** body 16.5px · ingredient name 16.5 · qty 14 · title (h1) 46 · labels 11–12.5. Prominence via the 54px photos, not big text.
- **Proportional:** two balanced columns — measure that `.leftcol` height ≈ `.steps` height. Sprig→wordmark gap ≥16px. Eyebrow on ONE line.
- **QUANTIFY every amount** — no vague "a crack/pinch/thumb"; give tsp/tbsp/cup (pepper = ⅛ tsp).
- **MAX-BOOST by default** (memory: feedback_max_boost) — fold every relevant pantry beneficial into the CORE recipe (protein/collagen, omega-3 seeds, minerals, blood-builders), naming what each adds; don't footnote them. She'd rather subtract than not know.
- **Don't strip the recipe** — build the FULL traditional version, not a minimal one. Real omissions caught in batch A: Adrenal Cocktail needs **cream of tartar** (potassium); Meat Stock Latte needs **egg yolks** (protein/froth); Morning Waters = **amla + ajwain** waters, not plain lemon. Check the original before simplifying.
- **Her kit:** 1.6 L clip-top Kilner jar; she uses **beef gelatin**; doesn't mind cold; organic. NOTE: **black pepper is not on her pantry list** (she has cayenne) — flag/confirm.
- **Bottom tabs:** `Main Meals · Snacks · Drinks · Desserts`; highlight the recipe's one in beet `#9c2b4e` (colour only, no tick).
- **Drinks MUST have a "When to drink" band.** Dishes: add a short "when to eat" line where useful.
- **Postpartum reframe:** "Why this heals you" (verified / tradition tags), "Just for you, Mum", honest note. Footer: *Food, not medical advice · non-diagnostic.*
- **SOURCE ATTRIBUTION (locked) — every card must say where the recipe came from + what you boosted.** The `.lineage` "Why we say this" note LEADS with provenance so Ilma can see at a glance *what's original, what's sourced, what's boosted*. Rules:
  - **Evidence only — never invent a source.** Pull it from `index.html` (recipe subtitles carry the creator @handle + IG/blog link), from memory, or from something Ilma has told you. If there is NO source on file, write "your recipe / kitchen" or "traditional [tradition]" — do **not** guess a creator. If genuinely unknown, label it "no source on file" and ask her.
  - **Label each card as one of:** `From @creator` (external, credit the handle + link) · `Traditional` (classic dish, no single author — e.g. Gond Laddu, Til-Gur, golden milk, CCF tea) · `Your recipe` / `Adapted (yours)` (hers/family/kitchen).
  - **A credit MUST hyperlink the EXACT recipe** — the specific IG post/reel or blog-post URL for *that dish*, never a bare handle, a profile link, or the creator's homepage. If you don't have the exact-recipe URL on file, do NOT ship a plain-text handle — get the link from Ilma first (or leave it uncredited and ask).
  - **Name the boost + swaps explicitly:** e.g. "**boosted** with collagen, flax & pumpkin seeds"; "gond & jaggery swapped for dates + gelatin". This is how she tells core-recipe from max-boost additions.
  - **Format:** `From <b>@handle</b> (<a href="…">link</a>) — [what it is] — <b>boosted</b> with […]. [verified/tradition health-claim framing].` Multi-source ("keep both"): `From <b>@base</b> (the recipe); [technique/idea] from <b>@other</b>.`
  - **Source of truth for links = `index.html`** subtitles (each recipe's `<div class="subtitle">` has the @handle + URL). Known corrections Ilma has given override it: **Chicken Liver Pâté = @sokoladassiela** (Lithuanian); the Pâté **Pops** freeze-idea = @wildnutritionist (index.html wrongly credited the whole pâté to @wildnutritionist). When Ilma pastes new source links, add them here and to the card.

## 3. VERIFY before showing Ilma a final link — ASK HER (based on past mistakes)
Do this ONCE up front for your batch, then a quick per-card preview:
1. **Amounts** — all quantified, nothing vague? (you've turned every "pinch/crack" into a tsp)
2. **Pantry** — every ingredient is something she HAS? (flagged anything she might not, e.g. black pepper)
3. **Vessel/quantities** — right for HER kit (e.g. 1.6 L Kilner, beef gelatin)?
4. **When to drink / eat** — included?
5. **Show a screenshot preview** and confirm: no emoticons · on-brand sprig header · columns balanced (say the measured heights) · spacing checked.
→ **Only after she confirms** do you deploy and send the final `?v=` link.

## 3B. SELF-REVIEW & SELF-FIX (mandatory — do this on YOUR OWN cards before showing Ilma anything)
This is the exact review Ilma had to do manually for batch A. Do it yourself and **fix everything before surfacing links** — only present cards that already pass. Loop until clean.

**Automated (render each card in the preview + check):**
- [ ] **No emoji/emoticons** anywhere in the body (grep the body — zero).
- [ ] Sprig header + "Your Healing Kitchen" present; **sprig→wordmark gap ≥16px**.
- [ ] Drinks have a **"When to drink"** band; dishes have a **"When to eat"** line.
- [ ] **Every image embedded** (grep: zero remaining `src="....png"`), and render → **0 broken images** (`img.naturalWidth>0`).
- [ ] **Columns balanced**: measure `.leftcol` vs `.steps` height; if off by >40px, move/add the "Just for you"/boost note into the right column until they match.
- [ ] **Step numbers filled** (1,2,3…), not empty badges.
- [ ] Tabs = Main Meals·Snacks·Drinks·Desserts; the recipe's one highlighted in beet `#9c2b4e` (no tick).

**Content (judgment — fix before presenting):**
- [ ] **Every amount quantified** (no lone "a crack/pinch/thumb").
- [ ] **Full recipe, not stripped** — check the original/library (Adrenal needs cream of tartar; Meat Stock Latte needs egg yolks; Morning Waters = amla+ajwain, not lemon).
- [ ] **MAX-BOOSTED** — pantry beneficials folded into the core, each naming what it adds.
- [ ] **Each ingredient PHOTO matches the ingredient** — no honey-showing-ghee / lemon-showing-beet mismatches; regenerate any wrong or 0-byte photo.
- [ ] **Source attribution present + correct** (§2 SOURCE ATTRIBUTION) — the `.lineage` note leads with origin (`From @creator` + link / `Traditional` / `Your recipe`) and names the boost/swaps. Cross-check the handle/link against `index.html`; use evidence only, never a guessed source.

**Then** redeploy the fixes and present Ilma the `?v=` links with a one-line note: *"self-QA passed: no emoji · balanced · maxed · full recipe · 0 broken images."*

Quick audit snippet (run from repo root, per card):
```python
import re; h=open("cook-cards/SLUG.html",encoding="utf-8").read(); b=h.split("</style>")[-1]
print("emoji:", re.findall(r'[\U0001F000-\U0001FAFF☀-➿]', b) or "none",
      "| whenband:", "whenband" in h, "| unembedded:", len(re.findall(r'src=\"[^\"]+\.png\"', h)),
      "| brand:", "Your Healing Kitchen" in h)
```
(Balance + broken-images must be checked by rendering in the preview, not from static HTML.)

## 4. Deploy without collisions (parallel-safe)
- Each chat owns DISTINCT slugs → no file overlap.
- `git pull --rebase origin main` → `git add cook-cards/<your-slugs>.html` (ONLY yours; never index.html or others' files) → commit → `git push`.
- Verify live: poll `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/cook-cards/<slug>.html?v=N` until HTTP 200 (CDN can lag 1–2 min). Give her the `?v=` link.

If `/tmp/cookcards/.env` is missing (machine rebooted), ask Ilma to recreate it with her OpenAI key.
