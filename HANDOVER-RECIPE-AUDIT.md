# HANDOVER — Recipe Audit & Two-Bucket Catalogue

Build ONE complete, categorised catalogue of Ilma's food recipes, pulled from **two sources**, and sort every recipe into **two buckets**. This is a *cataloguing / research* task, not card-building — the output is a list Ilma reviews and picks from.

## The two buckets (the whole point)
- **A · Postpartum-beneficial** — mark A if it delivers any of: iron/blood-building · protein/collagen · healthy fats/omega-3 · minerals (zinc/calcium/magnesium) · gut/ferments · warming & easy-to-digest · milk support. For each A recipe add a **one-line "why it heals" + a boost** (from `project_ilma_pantry`, MAX-boost per `feedback_max_boost`).
- **B · Everyday / other** — good recipes that aren't specifically postpartum (treats, very light salads, etc.). Still catalogue them — just no boost needed.

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
Two sections (A and B). Within each, group by type (Salads · Dressings · Waffles · Soups & Broths · Mains · Snacks · Drinks · Breakfast · Desserts). Per recipe, one row:
`Name · type · source (@handle + link) · [A only: why-it-heals + boost]`

Keep a running count per type so gaps are visible (e.g. "Salads: 6 · Dressings: 2 · Waffles: 4").

## Rules
- Reference memory: `project_ilma_pantry`, `feedback_max_boost`, `feedback_source_verification`, `reference_ancient_remedies_knowledgebank`, `feedback_healing_positioning`.
- Pull only from her library + her Saved collection — nothing invented.
- Food-first, non-diagnostic framing; label health claims verified-or-tradition.
- End with a short **"what's missing / worth adding"** note (e.g. more dressings, a waffle for each need) so Ilma can decide what to source next.

## Then
Hand Ilma the catalogue. She picks which recipes become full Cook Cards (built per `HANDOVER-CARDS.md`).

---
*Context: Ilma is building this for herself now (due any day); after birth she returns to Healing Kitchen as a product. This catalogue seeds both.*
