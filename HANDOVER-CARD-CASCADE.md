# HANDOVER — Cook-Card Finalization & the 49-Card Cascade
*Written 2026-07-04 by the cards/mom+helper session (8 feedback rounds + Fable review).
Paste SESSION-HANDOVER.md first, then this. **Ilma's live feedback always wins over any doc, including this one.***

## ✅ STATUS — 2026-07-07 evening (items 1–3 of the urgent list DONE, live-verified)
1. **`pilot/week1.html` is LIVE** — the WhatsApp door. Hand the helper:
   `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/pilot/week1.html?v=w1`
2. **All 15 DRINKS cascaded** to the mum+helper pair format (per-card QA clean; `drinks.html`
   offers Your card / Helper's kitchen card per recipe, `?v=c1`). Claims corrections per
   TAXONOMY-SYNERGY carried (fennel dose note, ashwagandha honest rewrite, Mineral Refresher
   rename, golden-milk 20× dropped, kvass folate-first + safety…) — full list in CARDS-AUDIT.md.
3. **Gentle mains cascaded**: bone broth (collagen-honest reframe) · magic soup · **khichdi with
   the first ratio-law dial** (rice anchors, lentils follow 1:1, Match-the-recipe balance line).
   `main-meals.html` updated for those three tiles only. **18/49 recipes are now pairs.**
   Build system: `cardgen/` (generator + per-drink data + QA script) — extend `data_*.py` for
   the remaining batches; khichdi is the dial reference.
4. **Photo pass UNBLOCKED (2026-07-07 eve)**: the OpenAI key is now live in Keychain, service
   `healing-kitchen-openai` account `openai` (164 chars, verified HTTP 200). Read it in any script
   with `security find-generic-password -w -s healing-kitchen-openai` (same `security` binary stores
   + reads, so NO GUI prompt). **v2 style anchors GENERATED + live** at `photo-anchors-preview.html`
   (gpt-image-2, snapshot 2026-04-21): the locked steer = delicate **French Provençal porcelain**
   (fluted/scalloped rims), **sparse wildflower posy** (lavender/chamomile) not scattered herbs,
   crisp/light/uncluttered, cream+sage enamelled cast iron, golden-brown oval cutlets. Prompt lives
   in `<scratchpad>/gen_anchors_v2.py`. **SIGNED OFF by Ilma 2026-07-09 ("yes i love this style")** —
   the prompt below is LOCKED for the full pass (mind the gpt-image-2 rate limit: 5/min — throttle
   or retry-on-429, as `regen_liver.py` does).

### 🔒 THE LOCKED PHOTO STYLE (signed off 2026-07-09 — use verbatim on every image)
Model **`gpt-image-2-2026-04-21`** (pinned; never the alias) · size 1024×1024 · quality high ·
subject line first, then append this style suffix VERBATIM:
> " Editorial food photography in a bright Provencal farmhouse kitchen. Soft diffused morning
> window light, gentle shadows, crisp fresh airy feel. Rumpled natural oatmeal linen cloth on a
> pale stone surface. Tableware is delicate French Provencal porcelain: white-cream porcelain with
> softly fluted, scalloped rims. Styling is sparse and uncluttered: at most one small loose posy of
> wildflowers (lavender, chamomile, meadow flowers) in soft focus to the side; clean surfaces,
> plenty of breathing room, no herb sprigs scattered about. Palette: warm paper-cream, muted sage
> green, soft honey-amber, a whisper of lavender. Where cookware appears: French enamelled cast
> iron in matte cream or soft sage, heavy rounded form, glossy enamel interior, no logos or brand
> marks. Shallow depth of field, 50mm lens look, luxury in simplicity, photorealistic, no people,
> no hands, no text, no watermark."
Subject rules: cutlets/patties = golden-brown ovals · ferments = the 1.6 L clip-top Kilner (orange
seal) · pots = sage or cream enamelled cast iron · ingredient shots = small fluted porcelain bowls.
**FRAMING (Ilma, 2026-07-09): shoot CLOSER — on the cards these render small** (ingredient circles
44–60px, steps/heroes ~84–160px). The subject fills **~70–80% of the frame**; ingredients = tight
close-up on the bowl (posy/context only at the edges or out of frame); heroes/steps = close crop on
the food/pot, the airy Provence context in the margins, never the center. Append to every prompt:
*"Framed close on the subject — it fills most of the frame; context stays at the edges."* The v2
anchors are style-true but framed WIDE — do not copy their framing. **QA: check the first 3 batch
images at 60px thumbnail size before running the rest.**
Output into the shared `cook-cards/img/<slug>/` dirs (cardgen architecture) — heroes + ingredient
library DEDUPED across cards (shoot turmeric once, reuse everywhere), throttled ≤4/min.
5. Old pilot cards remain live but `week1.html` now points the kvass tile at the NEW
   `cook-cards/beet-kvass-card.html` (upgraded, ferment-shaped). `pilot/kvass.html` +
   `pilot/index.html` upgrades stay on the before-FINAL checklist.

## 🎨 DESIGN SESSION — Deliverable 1 SHIPPED 2026-07-09 eve, awaiting Ilma's pick
**Three directions live** (same DNA, three intensities), each applied to REAL surfaces
(week1 door · liver-cutlets mum card · liver-cutlets helper card · card index), with a
switcher bar on every page. Originals untouched. Chooser: `design/index.html?v=d1`.
1. **Porcelain minimal** (`design/porcelain/`) — quietest: white porcelain + pale linen,
   sage headings, lavender fine-print, scalloped hairline. Beet action.
2. **Provence garden** (`design/garden/`) — freshest: lavender headings, wildflower-posy
   divider, pink notes/hovers. **Trial: mum's "Send to my helper" in deep iris, not beet.**
3. **Linen apothecary** (`design/apothecary/`) — warmest: woven oatmeal texture,
   label-frame double rules, amber small-caps, lavender eyebrow + wax-seal pink dot. Beet action.
All three: destriped callouts (tinted, per the house ban), 3-label chips untouched, big-type
helper preserved.
**Azure added (Ilma, 2026-07-09 eve: "i like azure — think of wild flower colours"):**
cornflower/chicory azure is now in all three, direction-weighted — porcelain: azure glaze
scallop + fine-print kickers · garden: cornflower in the posy + chicory-azure when-band +
azure arrows · apothecary: azure-ink numbers/meta labels. How MUCH azure = one of the
post-pick sub-choices. Build script: `design/build_directions.py` (regenerates all
12 pages from the live pilot/cook-cards sources — rerun after any source-card change).
**Next: her pick → sub-choices as ≥3 options each (palette mixes, divider motif, accent
strength) on the same surfaces → docs/design.md → batch-apply cascade (Deliverable 2).**

### (original brief below — steer locked 2026-07-09)
Ilma: seed the design system **from the approved photo anchors** (no screenshots needed). Her words:
*"love the fresh crispy style — sage, purple, pink, herby wild flowers, lavender, lilies, chamomile —
design it all and give me options to approve."*
- **Seed:** `photo-anchors-preview.html` (the LOCKED PHOTO STYLE below) + the card language standard.
- **Palette direction:** paper-cream + sage lead · **lavender/purple + soft pink accents (NEW)** ·
  honey-amber whisper · beet stays the action colour unless an option shows something better.
- **Motifs:** oatmeal linen, fluted/scalloped porcelain shapes, sparse wildflower posies
  (lavender, chamomile, **lilies**) — sparse like the anchors, never cluttered.
- **Fixed:** apothecary fonts (Cormorant Garamond / EB Garamond / Marcellus / Pinyon Script — never
  Fraunces/Mulish) · "keep it simple, never overwhelm" · helper surfaces big-type phone-first ·
  3-label chips · no emoji on cards · no creator names.
- **STANDING RULE (Ilma, 2026-07-09): every aesthetic decision = ASK her, with ≥3 OPTIONS** —
  palettes, type scales, motifs, component shapes, photo looks — always shown on REAL surfaces with
  live links, never abstract swatches. ("Don't ask what you can decide" applies to MECHANICAL work
  only — deploys, QA, extraction, scaling math. Taste always goes back to her as options.)
- **Deliverable 1:** THREE design directions as live Pages previews (same DNA, different intensity —
  e.g. porcelain-minimal / Provence-garden / linen-apothecary), each applied to REAL surfaces:
  `pilot/week1.html`, one mum card, one helper card, an index tile. Fresh `?v` links → Ilma picks.
  Within the winning direction, sub-choices (exact palette, accent intensity, divider motif…) also
  come as ≥3 options each — e.g. three lavender/pink palette mixes side by side.
- **Deliverable 2 (after her pick):** write **`docs/design.md`** (type scale, spacing, palette incl.
  the lavender/pink accents, components, photo treatment, motion) as the single source of truth,
  then apply across week1 + live pairs + index/tab pages + printables, batch by batch, live-confirmed.

## ⚡ REALITY CHANGE — 2026-07-07
**Emil was born 2026-07-05.** Ilma is week-1 postpartum NOW and could not yet cook/delegate from
the recipes. Priorities are FLIPPED — usefulness today beats finalization:
1. **TODAY — the helper cooks from what EXISTS.** Working links (all verified live 2026-07-07):
   pilot liver-cutlets helper card + mum card, pilot kvass, `cook-cards/drinks.html` (15 drinks),
   `cook-cards/index.html` (everything). First deliverable of the next session = **`pilot/week1.html`**,
   one phone-friendly WhatsApp-able page linking: Tonight = Liver Cutlets (pilot helper card) ·
   Start today = Beet Kvass · week-1 drinks (jujube-goji, golden milk, nettle, caraway, meat-stock
   latte) · gentle mains (chicken bone broth, magic chicken soup, khichdi). No new content — just the door.
2. **Cascade DRINKS first** (what a breastfeeding week-1 mum uses most), then gentle recovery
   mains (broths/soups/khichdi), then the rest. Same per-card QA as below.
3. **Template polish only when it blocks cooking. Photo pass background-only** — anchors v2 steer:
   delicate Provençal porcelain (fluted/scalloped rims), much less herby, sparse wildflower posy
   (lavender/chamomile), cream+sage cast iron stays, golden-brown oval cutlets. Generator script ready:
   `<session-scratchpad>/gen_anchors_v2.py` (reads key from **macOS Keychain**, service
   `healing-kitchen-openai`, via `security find-generic-password -w`; no GUI prompt, verified).
   v1 anchors live at `photo-anchors-preview.html`.
4. The pre-birth "before-FINAL checklist" below still applies, but AFTER the above.

**Paste-ready prompt (URGENT version — supersedes the one at the bottom):**
> Read SESSION-HANDOVER.md, then HANDOVER-CARD-CASCADE.md including the REALITY CHANGE block —
> Emil was born 2026-07-05; I'm week-1 postpartum and my helper must cook from these cards NOW.
> Work in this order, push + live-confirm after each, don't ask me anything you can decide:
> (1) build pilot/week1.html per the block above and give me the link to WhatsApp my helper;
> (2) cascade the 15 DRINKS to the finalized mum+helper format (vessel-bound = no dial), per-card
> QA, fresh ?v links per batch; (3) gentle recovery mains next; (4) photo pass background-only,
> key in macOS Keychain (service healing-kitchen-openai); (5) my feedback wins, never name creators, every health
> line keeps its 3-label chips + real sources.

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
