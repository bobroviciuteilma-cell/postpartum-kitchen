# HANDOVER — Cook-Card Finalization & the 49-Card Cascade
*Written 2026-07-04 by the cards/mom+helper session (8 feedback rounds + Fable review).
Paste SESSION-HANDOVER.md first, then this. **Ilma's live feedback always wins over any doc, including this one.***

## What this is
The mom+helper card format was hammered out on the **liver-cutlets pilot pair** through 8 rounds of
Ilma's live feedback (2026-07-04). This file holds: (1) the locked card standard, (2) the checklist
still open before Ilma declares **FINAL**, (3) the cascade plan for converting all 49 live cook-cards
— for her approval before execution.

## Read first
- `SESSION-HANDOVER.md` — project context, locked decisions (do not re-litigate)
- Memories: `feedback_card_language_standard` · `feedback_cook_cards_visual` (incl. the **Le Creuset
  cookware rule**, added 2026-07-04) · `feedback_recipe_scaling_proportion` (**LOCKED ratio law**) ·
  `feedback_source_verification` · `feedback_max_boost` · `project_ilma_pantry`
- `CARDS-AUDIT.md` — the 49-card index + verified source ledger

## State of play (all live on Pages)
Base URL: `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/`

| File | What it is |
|---|---|
| `pilot/liver-cutlets.html` | **HELPER card — the living template.** Carries all 8 rounds. |
| `pilot/liver-cutlets-mum.html` | **MUM card — the living template.** Finalized format, built 2026-07-04. |
| `pilot/kvass.html` | Helper-only, **pre-dates the 8 rounds** ("Short version"×3, old gather tiles, no Back, no no-cache meta). |
| `pilot/index.html` | 2 tiles, helper links only — **no Mum's-view links yet**. |
| `mom-helper-split-preview.html` | The original design artifact — **superseded by the pilot pair** (pending Ilma's confirm; archive, don't back-port). |
| `cook-cards/*.html` (49) | 11 "new" cards on the old 4-chip standard; 38 originals older still. **All 49 need the retrofit.** |

**Deploy quirk (recurring):** Pages runs randomly fail or wedge on "queued". `gh run rerun` often stays
wedged — the reliable fix is `git commit --allow-empty -m "Nudge Pages build" && git push`. Verify by
polling the **live URL** for the new content (curl with a random query param), never just the run status.
**Browser cache:** cards carry no-cache meta now, but still hand Ilma a **fresh `?v=N`** she hasn't opened.

---

## THE LOCKED CARD STANDARD

### Helper card (kitchen mode, phone-first)
Screens: **Overview → Gather → Steps 1..N → [Mum's plate, only if boosts ticked] → Finish.**
Progress dots track position; **every screen has Back**; no-cache meta + fresh `?v` links.

1. **The overview IS the short version** (no separate "mastered" mode; the words "Short version" appear
   nowhere): hero photo → dish name → ONE quiet meta line ("Ready by 6:30 · about 35 min · makes ~N")
   → What-you-have dial(s) → full ingredient list (name + qty rows) → 5-line method → single button
   **"Start — gather ingredients"**.
2. **Scaling obeys the LOCKED ratio law** (`feedback_recipe_scaling_proportion`): *the ratio that
   defines a recipe must survive scaling — never two free dials.* Batch-driver main = the dial;
   secondary main **auto-follows at the recipe ratio**; nudging allowed but shows a live balance line
   ("Balanced to the recipe — …" / amber "More/Less X than the recipe — [effect]" + one-tap **"Match
   the recipe"**). Supporting cast + "makes ~N" scale off the total. Rounding: g → nearest 10, tbsp →
   nearest ¼, eggs whole, counts get "~". Fixed items ("to season", garnish sides) never scale.
   **Vessel-bound recipes get NO dial** (kvass: the jar fill-level is the measure).
3. **One count source only**: "makes ~N" in the overview meta. Steps never assert a count a fixed photo
   can contradict ("a tray of even ovals, all a similar size"). **No scalable numbers in donelines,
   captions, or the Listen voice scripts** — spoken lines carry no amounts.
4. **Gather tiles**: photo + name + qty chip + a **worded tick bar** ("Tap when you have it" → filled
   sage "Got it" with a drawn check). "Out of this" = quiet italic secondary action (flags to Mum,
   amber state, "Never mind — found it" undo). Counter "N of M in · K flagged to Mum". **Start cooking**
   gates on required items; **Back** sits beside it.
5. **Step screens**: kicker "Method · step n of N" → photo → verb headline with time → short detail
   (scalable spans) → "Done looks like:" line. Cautions are **contextual and inline** (cook-through
   lives in the cook step; stains at the stain step) — never a banner on page 1. "Confused by this
   step?" → noted for Mum. **Timers**: label above (SIDE 1 / SIDE 2), tap to start / pause / resume,
   a Reset link once running, one hint line.
6. **Finish**: "All served?" → optional photo → "Note for Mum" → ONE primary **"Cooked — tell Mum"**
   (+ caption "Mum gets a note on her phone that dinner's ready."). After: "Beautiful." → "Sent to Mum —
   she knows dinner's ready." → her thanks. *(Pilot = simulated send — Ilma's decision 2026-07-04;
   the real app wires this button to the backend push. UI unchanged.)*
7. House rules: no emoji (drawn SVG/CSS ticks are fine) · Cormorant Garamond / EB Garamond / Marcellus /
   Pinyon Script · house palette · wake-lock · print CSS.

### Mum card (the why + her instructions)
Order: **masthead** (sprig, wordmark, tagline, one-line eyebrow, thin rule) → **title + subtitle +
linen-matted hero** → **meta** ("Time to cook:" / "Keep in the fridge:" — both amber labels, colons) →
**When to eat** band (her NEED phrasing) → **Why this heals you** (bulleted; chips ONLY on health
claims — research-backed (green) / tradition (amber) / breastfeeding note (soft beet); every chip taps
open the **Sources** sheet with real, dated, openable links; kitchen-craft lines carry no chip; the
BF note attaches to its subject as an italic line + "Read the breastfeeding note") → **Your
instructions** (What-you-have dials with the same auto-balance law · "Your plate — serve with" ticks ·
"Make it PP Gold (for yourself)" ticks each with a one-line why · "These go on your plate only — the
family's stays as it is." · Ready-by select + beet **"Send to my helper"** → sent-preview listing
exactly what lands on the helper card + link to the helper view) → **Ingredients** (2-col, photos,
qty, prep note) → **Method** (numbered, photos, contextual cook-note callout) → nutrition band
(**qualitative until verified**) → disclaimer. Footer: "See your helper's view →" · index link.
The DELETE list stands: no household verdict, no "why we say this" footer, no tab bar, no floating
craft tips, no duplicated info.

### Both cards
**Never name recipe creators publicly.** Every health line chip-labelled with real tappable sources
(verify or soften — no invented sources, exact permalinks or nothing). Max-boost philosophy per her
pantry. **Le Creuset cookware rule** for all generated photos. **No side-stripe borders** — tinted
callouts instead (house CSS ban, adopted 2026-07-04).

---

## Open before Ilma can say FINAL
- [ ] Ilma reads the Fable review (2026-07-04) and steers on: Mum-card fold (rec: **don't** fold),
      balance-bar visual (rec: **skip**), split-preview archived (rec: **yes**), cascade image
      architecture (rec: **shared `cook-cards/img/`**)
- [ ] **Kvass helper card** upgraded to the standard — overview-first, tick-bar gather tiles, Back
      buttons, no-cache meta, pause/reset where sensible; **NO dial** (vessel-bound); keep the
      ferment-specific shape: day-chips, day-5 reminder, safety rules band, "Jar started"
- [ ] **Kvass Mum card** built (why/chips/Sources; instructions without a dial)
- [ ] **pilot/index.html** — each recipe offers "Mum's view / Helper's view"
- [ ] **Claims pass on Mum's liver-cutlets card** — verify or soften the nutrition band ("~28 g
      protein", "B12 very high") and boost sub-labels; chips' NIH/USDA links are already real
- [ ] Template-finalization polish, once: subtle linen texture, sprig section dividers, colour
      discipline (sage leads, amber = warmth accents only), hero mat — **subtle, or not at all**
- [ ] Ilma says the word: **FINAL**

## The cascade (proposal — Ilma approves before anything rolls)

**Decision 0 — image architecture.** Embedded base64 (status quo) vs shared `cook-cards/img/`.
Recommendation: **shared folder** — cards shrink ~10×, the Le Creuset photo regen becomes a file swap
instead of re-embedding 98 HTML files, the browser caches ingredients across cards. WhatsApp-link and
print flows are unaffected. (Embedded only matters if she ever needs single-file email attachments.)

**Phase 1 — photo style anchors** *(needs a fresh OpenAI key — the old one was flagged for rotation)*:
regenerate 6–8 reference photos (1 hero, 2 Le-Creuset pan steps, 3 ingredients on linen, the 1.6 L
Kilner jar) in the locked Provence style → Ilma signs off → the exact prompt template gets appended
to this file and governs the whole batch.

**Phase 2 — convert in batches by tab, simplest → hardest:**
**Drinks (15)** → **Snacks (7)** → **Desserts (~5)** → **Main Meals (22)**.
Drinks first: mostly vessel/cup recipes, few dials, fastest wins. Mains last: dials + ratio anchors +
the most judgment. Per batch: convert (mum + helper pair per recipe) → per-card QA (below) → push →
live-check → **Ilma spot-checks 2–3 cards** → tab page updated once → `CARDS-AUDIT.md` updated.

**Automated per card** (mechanical): template scaffold · 3-label renames · Sources-sheet shell ·
meta-line rewrites · no-cache meta · footer/tab/index links · cache-bust · no-emoji sweep · image wiring.

**Judgment per card** (never automated): batch-driver + ratio anchor (**the LAW**) · which mains get
dials at all · the ONE contextual warning (only what's true for this dish) · serve-with + PP-Gold sets
(pantry-aware, max-boost) · BF-note subjects · Sources content (verify EVERY claim; exact creator
permalinks or no credit) · photo gaps for the Le Creuset pass.

**Per-card QA checklist** (run on every card, both views):
labels = 3 only, tappable, real dated sources · ratio law wired, balance line correct · one count
source, no orphan/contradicting numbers incl. voice scripts · warnings contextual only · no emoji ·
no creator names · Le Creuset cookware (or queued for regen) · links live (tab ↔ card ↔ mum ↔ helper
↔ index) · no-cache meta + fresh `?v` · print OK · the Ilma-delete-list respected.

**Link survival:** existing filenames/URLs never change; Mum views are NEW `<slug>-mum.html` files;
the 4 tab pages and index keep working throughout; `CARDS-AUDIT.md` stays the ledger.

## Risks & gotchas
Pages queue flakiness → the empty-commit nudge (above) · browser cache → fresh `?v` discipline ·
base64 makes files unreadable/grep-noisy → strip images into scratchpad copies before reading ·
OpenAI key must be rotated + supplied before the photo pass · never ship a bare @handle as a source ·
the kvass day-5 reminder is UI-only in the pilot (real reminders = app backend).

## Paste-ready prompt (next session)
> Read SESSION-HANDOVER.md, then HANDOVER-CARD-CASCADE.md. Work the "Open before FINAL" checklist in
> order (kvass pair → index → claims pass → template polish), pushing and live-confirming after each,
> then stop for my FINAL. After FINAL: execute the cascade exactly as written — Decision 0 first, then
> Phase 1 style anchors for my sign-off, then batches by tab with the per-card QA on every card, and
> stop for my spot-check between batches.
