# HANDOVER — Smart Apothecary (pantry feature)

**Session date:** 2026-07-03 · **Built by:** Claude (Fable/Opus) with Ilma
**Purpose:** paste this into a new chat to continue the Smart Apothecary and wire it into the rest of Your Healing Kitchen.

---

## 0 · Live links (GitHub Pages, `main` branch)

Both previews are self-contained HTML, committed and served from GitHub Pages:

- **Steady-state pantry (4 phones):**
  https://bobroviciuteilma-cell.github.io/postpartum-kitchen/pantry-preview.html
- **First-setup date flow (3 phones):**
  https://bobroviciuteilma-cell.github.io/postpartum-kitchen/pantry-onboarding-preview.html

The recipe names **inside** the previews are live links into the existing cook-cards
(`…/cook-cards/<name>.html`), which were already on Pages.

> Cache tip: append `?v=2` to bust the CDN cache if you re-push and see a stale version.

---

## 1 · What was built

### `pantry-preview.html` — the steady-state Apothecary (4 phones)
1. **Your Apothecary** — one pantry, **two doors**:
   - *Where it lives* (physical, **default/first**): Spice drawer · Potted fresh herbs · Powders & adaptogens · Tea tin · Seeds, nuts & butters · Sweet & blood-builders · Grains, flours & pasta · Fats & oils · Protein & collagen · Ferments & vinegars.
   - *What it does* (the **7 verb-led recipe shelves**): Rebuild your blood · Heal your gut · Steady energy · Keep your milk flowing · Strengthen bones & repair · Calm & lift your mood · Steady immunity.
   - Rotating **"Today's insight"** carousel + a **Restock list** (requests from the helper, one place, with amount + retailer + price).
2. **A jar, opened** — What it does (with honesty labels) · In your recipes (hyperlinked) · **Could also boost** (opens a suggestion card, meant to be bidirectional) · How much · discreet dose note · freshness line · **Buy block** (organic + non-organic as equals, amount + retailer + price, direct links only).
3. **Helper's view** — EN/BM/TA/MY chrome · big **Plenty/Low/Out** taps that **notify mum (never order)** · "Something else finished?" free-text → mum's restock · "Ma'am has been told."
4. **Add what you have** — **Photo** (scan the drawer, recognise + add new jars) · **Voice** (parse spoken updates) · **Type**. Mum or helper, ~20 seconds.

### `pantry-onboarding-preview.html` — the first-setup date model (3 phones)
1. **Just get it all in** — estimate-by-default landing; summary *34 in · 8 label dates · 26 estimated*; sealed-vs-estimated confidence shown honestly; dismissible **"Ask my helper"** precision offer.
2. **Helper's date check** — scoped to the **~8 spoilers only**; *Scan best-before* (exact) or fuzzy fallback for oils; *Fresh / Ageing / Replant* for potted herbs (no date exists for a living plant); progress bar to 8/8.
3. **It sharpens itself** — confidence climbs **8 → 22 of 34**; **ghee** alert framed as *a recipe to cook* (Golden Milk); **turmeric** stays a quiet estimate (no alarm); **goji** auto-upgraded from a restock.

---

## 2 · Locked standards this session — **do not re-litigate**

| Decision | Standard |
|---|---|
| **Name** | "**Apothecary**" everywhere. Mum = *Your Apothecary*; helper = *Ma'am's Apothecary*. Killed: "larder", "pantry" as a label, "the kitchen shelves". |
| **Word for recipes** | "**recipes**", never "cards", in UI. Recipe names are **hyperlinks** to the live cook-cards. |
| **Evidence labels** | Text only, **no emoticons**. Standard set + colours: **verified** (sage) · **nutrient fact** (amber) · **tradition** (lavender) · **bf note** (rust). Rule (from MASTER-PLAN): verified/nutrient-fact mark what's *in* the food; healing *outcomes* stay **tradition** unless clinically supported. |
| **Two doors** | *Where it lives* first (default), *What it does* second. |
| **Restock flow** | **Notify, never order.** Helper taps → mum is told. All requests land in **ONE place** (mum's Restock list) with **amount + retailer + price**. Mum orders or ignores. |
| **Buy links** | **Direct-order links only** (RedMart, iHerb SG, Scoop, Little Farms, Lazada, Far East Flora). Walk-ins (Mustafa, Little India, medical hall) shown as **marked alternatives, never linked**. |
| **She picks** | No "our pick". Organic + non-organic presented as **equals** with amounts; she chooses. |
| **Dates** | Estimate by default at bulk upload (**never fake "today"**). Alerts stay **silent until a real signal**. Precision is an **opt-in delegation** scoped to the ~8 spoilers. **Never claim 100%** — ceiling is "exact where the label shows it". Self-corrects on restock. Alert framed as **a recipe to cook**. |
| **Potted herbs** | Own shelf; **herb-sprig visuals**, not jars. Wording "**fresh from your pots**" (not "windowsill" — could be a balcony). |
| **Ghost pantry stays dead** | State only changes on **human declaration** (tap/photo/voice). No AI guessing inventory. |
| **Free vs Pass** | **Free:** jar pages + helper taps + add-flow (they serve the dinner loop). **Season Pass:** AI price-hunting, voice-parse, "could also boost" suggestions. |

---

## 3 · Data facts established (real, measured — not invented)

- **49 built cook cards** (grew 38 → 49; live under `cook-cards/`).
- **The amla hook:** amla appears in **1 of 49 recipes**; **collagen in 29**. She owns the iron-unlock and barely uses it — this became the demo's opening insight.
- **Per-ingredient recipe counts** power the "in X recipes" line. Highlights: collagen 29 · ghee 19 · honey 16 · cinnamon 15 · pumpkin 14 · dates 14 · flax 13 · gelatin 12 · ginger 12 · hemp 11 · tahini 10 … down to zeros: **quinoa 0**, **Cuban oregano 0**.
- **⚠️ GREP GOTCHA:** recipe images are **base64-embedded**, so naive text search **lies** — random base64 strings match ingredient names (amla "matched" 47 cards until stripped; "clove: 16" was *garlic cloves*, real spice-clove = 1). **Always strip** `[A-Za-z0-9+/=]{60,}` before counting ingredients across the cards.
- **Cuban oregano = torbangun** (*Coleus amboinicus*), a SE-Asian postpartum milk herb — surfaced this session; its jar card suggests boosting **Magic Chicken Soup**.

---

## 4 · Ilma's insights / steers this session

- Simpler, clearer visuals over decorative colour blocks.
- Wording matters and must be **consistent mum ↔ helper**; "larder" is unfamiliar to many.
- **Physical door before benefit door.**
- "recipes" not "cards"; **she picks** (no "our pick").
- **Restock must show amounts** to justify the price (raised twice).
- **Only direct-buy links.**
- **Separate** orzo / pasta; **separate** flours (not "all kinds").
- **Potted herbs** as their own category (sprigs).
- Add-what-you-have via **photo / voice / type** — helper can do it, mum too.
- Helper should also report **non-apothecary** shortages.
- Freshness motivation = "alert & save you money" — resolved to: **show after a win, tie to a recipe, never nag.**
- Raised the hard date question ("how would you know at bulk upload?") → resolved to **estimate-default + helper-precision opt-in**.

---

## 5 · Mistakes & learnings (candid)

- Shipped **"our pick" + "quality first"** nudge when she'd rather choose — corrected to neutral.
- **Restock rows lacked amounts** through two rounds before I fixed it — should've caught the first ask.
- **Over-promised** "best-before read off the labels" in the first freshness build and stamped "today" on *existing* stock — that was **ghost-pantry-wrong**; forced the estimate/confidence model (which is better).
- First pass used decorative colour blocks; she wanted simple/clear → moved to flat jar shapes + herb sprigs (still **placeholders** for real ingredient photos).
- Illustrative prices + demo-grade translations shipped knowingly — **flagged**, must be real before ship.
- Caught a live bug mid-build (fuzzy-oil fallback mislabeled as a best-before date) by driving the JS headlessly — **verify interactions, don't just eyeball the render.**

---

## 6 · Open items / NOT done (next chat's backlog)

- [ ] **Real SG prices + direct product URLs** per item (currently illustrative ≈S$).
- [ ] **Native-speaker check** of BM / TA / MY strings (demo-grade).
- [ ] **Per-ingredient shelf-life** values from a checked source (currently sensible defaults).
- [ ] **"Could also boost" bidirectionality** — the 3 target cook-cards don't yet carry the reciprocal boost bar (cook-card pipeline task).
- [ ] **Thread confidence tags** (est. vs known) + freshness into the *main* pantry-preview jar rows (only in the onboarding preview today).
- [ ] **Real ingredient photography** to replace jar/sprig placeholders (reuse the cook-card image library).
- [ ] **Wire into the Kitchen tab** (`app/`) and connect the Restock list to the real order/shopping surface.
- [ ] Raised-but-unbuilt: **"Cook from what's here"** (pantry ∩ recipes), **stage stocking lists**, **registry/gifting** angle.

---

## 7 · How it wires to the rest of the app

- Lives in the **Kitchen tab** (locked app structure = *Today · Kitchen · You*; the apothecary folds **into** Kitchen — don't make a depleted mum manage two food "places").
- The **jar → recipe / recipe → jar** graph is the knowledge-graph moat; taxonomy is **shared** with the cook cards (one system, two doors).
- The **Restock list** should feed the same order/shopping surface as the rest of the app.
- **Freshness alerts** should surface through the **Today** tab's dinner suggestion (the recipe-nudge), not as standalone nags.

---

## 8 · File map (this session)

**Created (mine, 2026-07-03):**
- `pantry-preview.html` — steady-state Apothecary (4 phones)
- `pantry-onboarding-preview.html` — first-setup date flow (3 phones)
- `HANDOVER-SMART-PANTRY.md` — this file
- `smart-pantry-map.html` — visual map of session output + a proposed clean folder structure

**References I read (context, not modified):**
- Memory: `project_ilma_pantry`, `project_app_structure` (+ taxonomy/cards memories)
- `MASTER-PLAN.md` (label standard + 7-shelf taxonomy), `TAXONOMY-SYNERGY.md` (§B.2 shelves)
- `cook-cards/*.html` (49 recipes — source of every ingredient count) + `cook-cards/adrenal-cocktail.html` (verified cream-of-tartar claim)
- `spice-scan-preview.html` (existing "your everyday apothecary" prototype this builds on)

> **Project hygiene note:** the repo root currently holds **31 `.html`** and **22 `.md`** files loose. There are already `Previews/` (screenshots) and `References/` (source docs) folders. See `smart-pantry-map.html` for a proposed clean structure — planned for a separate cleanup session.
