# HANDOVER — Recipe Audit & Two-Bucket Catalogue

Build ONE complete, categorised catalogue of Ilma's food recipes, pulled from **two sources**, and sort every recipe into **two buckets**. This is a *cataloguing / research* task, not card-building — the output is a list Ilma reviews and picks from.

## The two buckets (the whole point)
- **A · Postpartum-beneficial** — sort each A recipe under **our defined "What it heals" categories: Rebuild blood · Energy · Calm & sleep · Milk supply · Gut-healing · Mood · Immunity** (a recipe can sit under more than one). Add a one-line *why-it-heals* + a **max-boost** from her pantry (`feedback_max_boost`). **If a recipe is clearly beneficial but doesn't fit any of the 7 → propose a NEW category** (name it + one line why) and flag it for Ilma to approve — don't force-fit.
- **B · Everyday / other** — good recipes that aren't specifically postpartum (treats, very light salads). Catalogue them by dish type; no boost.

**Every recipe (A and B) must carry its ORIGINAL source link** — `@handle` + permalink for Instagram; the blog URL or library `#anchor` otherwise. Verify each resolves; flag dead/removed links (`feedback_source_verification`).

**Pull ALL of these explicitly (she wants them):** every **salad**, every **dressing**, every **waffle** recipe (she just bought a waffle machine).

## Source 1 — her library (this repo)
Parse `index.html` recipe sections (title + ingredients + any `@source` link). ~67 recipes already curated. Many already sorted implicitly by the "What it heals" shelves — reuse that judgement.

## Source 2 — her Instagram "Saved → food" collection (via Chrome)
Ilma will **open Chrome, logged into Instagram, on her Saved food collection**. Use the **Chrome MCP** (`mcp__Claude_in_Chrome__*`: `navigate`, `get_page_text`, `read_page`, `scroll`, `find`) to:
1. Read the Saved collection page; **scroll to the bottom** so the whole grid loads.
2. Extract every post: **creator @handle · permalink · the dish** (from thumbnail/caption).
3. For any recipe you need the detail of, open the post and read the caption — or run the **Apify `apify/instagram-scraper`** on the permalink (`resultsType: posts`, `resultsLimit: 1`) to get caption + author.
4. **Verify each source** (per `feedback_source_verification`): confirm the link resolves + the creator; flag dead/removed posts. Don't invent.

## Output → `RECIPE-CATALOG.md`
- **Bucket A** — grouped by **healing category** (Rebuild blood · Energy · Calm & sleep · Milk supply · Gut-healing · Mood · Immunity · + any NEW category you propose). Per recipe: `Name · type (salad/dressing/waffle/…) · original source (@handle + link) · why-it-heals · boost`.
- **Bucket B** — grouped by dish type. Per recipe: `Name · type · original source link`.
- A **"Proposed new categories"** list (name + one line why) for Ilma to approve.
- Running counts per type (e.g. "Salads 6 · Dressings 2 · Waffles 4") + a **"what's missing / worth adding"** note.

## Rules
- Reference memory: `project_ilma_pantry`, `feedback_max_boost`, `feedback_source_verification`, `reference_ancient_remedies_knowledgebank`, `feedback_healing_positioning`.
- Pull only from her library + her Saved collection — nothing invented.
- Food-first, non-diagnostic framing; label health claims verified-or-tradition.
- End with a short **"what's missing / worth adding"** note (e.g. more dressings, a waffle for each need) so Ilma can decide what to source next.

## Then
Hand Ilma the catalogue. She picks which recipes become full Cook Cards (built per `HANDOVER-CARDS.md`).

---
*Context: Ilma is building this for herself now (due any day); after birth she returns to Healing Kitchen as a product. This catalogue seeds both.*
