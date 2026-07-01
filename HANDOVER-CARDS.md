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
- **Her kit:** 1.6 L clip-top Kilner jar; she uses **beef gelatin**; doesn't mind cold; organic. NOTE: **black pepper is not on her pantry list** (she has cayenne) — flag/confirm.
- **Bottom tabs:** `Main Meals · Snacks · Drinks · Desserts`; highlight the recipe's one in beet `#9c2b4e` (colour only, no tick).
- **Drinks MUST have a "When to drink" band.** Dishes: add a short "when to eat" line where useful.
- **Postpartum reframe:** "Why this heals you" (verified / tradition tags), "Just for you, Mum", honest note. Footer: *Food, not medical advice · non-diagnostic.*

## 3. VERIFY before showing Ilma a final link — ASK HER (based on past mistakes)
Do this ONCE up front for your batch, then a quick per-card preview:
1. **Amounts** — all quantified, nothing vague? (you've turned every "pinch/crack" into a tsp)
2. **Pantry** — every ingredient is something she HAS? (flagged anything she might not, e.g. black pepper)
3. **Vessel/quantities** — right for HER kit (e.g. 1.6 L Kilner, beef gelatin)?
4. **When to drink / eat** — included?
5. **Show a screenshot preview** and confirm: no emoticons · on-brand sprig header · columns balanced (say the measured heights) · spacing checked.
→ **Only after she confirms** do you deploy and send the final `?v=` link.

## 4. Deploy without collisions (parallel-safe)
- Each chat owns DISTINCT slugs → no file overlap.
- `git pull --rebase origin main` → `git add cook-cards/<your-slugs>.html` (ONLY yours; never index.html or others' files) → commit → `git push`.
- Verify live: poll `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/cook-cards/<slug>.html?v=N` until HTTP 200 (CDN can lag 1–2 min). Give her the `?v=` link.

If `/tmp/cookcards/.env` is missing (machine rebooted), ask Ilma to recreate it with her OpenAI key.
