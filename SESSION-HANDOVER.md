# SESSION HANDOVER — Your Healing Kitchen
*Written 2026-07-03 for a fresh chat to continue seamlessly.*

## What this project is
A postpartum-recovery food app, **Singapore-first**, for a fourth-trimester breastfeeding mother
(Ilma, the founder — building solo with AI agents, due any day, **faceless brand**). It turns her
verified "Cook Cards" into a smart kitchen: daily check-in → tonight's dinner chosen for her recovery
AND the family → sent to the helper/nanny who cooks it → Cooked ✓ back → a library that grows with her
across life stages. **Trust is the product** (every health claim verified or honestly labelled).

## Read these first (in order)
1. **MASTER-PLAN.md** — the consolidated decision sheet (taxonomy, pricing, fixes, build order).
2. **docs/VISION.md** → **docs/product-vision.md** → **docs/prd.md** → **docs/product-roadmap.md** — the
   full BuilderOS spec chain (vision → PRD 26 tables/73 FRs → 105-task roadmap). Awaiting Ilma's
   line-by-line review; every judgment call marked ⚑.
3. **docs/validation-report.md** (idea-validator: STRONG 25/30) + **docs/CONFIDENCE-REVIEW.md** (red-team:
   Conditional GO; all 17 patches applied to the specs).
4. **Project memory** (`~/.claude/projects/-Users-Enki-code-postpartum-kitchen/memory/`) — MEMORY.md is the
   index; the load-bearing ones for this work: `feedback_card_language_standard`, `feedback_vision_steers`,
   `project_singapore_market`, `project_taxonomy_synergy`, `feedback_source_verification`,
   `feedback_healing_positioning`, `feedback_cook_cards_visual`, `project_ilma_pantry`.

## Locked decisions (do not re-litigate)
- **Market:** Singapore first. **Pricing:** Rescue S$39 · **Season Pass S$168 / gift S$188** · Nourish Pool
  S$288; 6-mo membership included → **S$96/yr renewal** (card auto-renew; PayNow buyers get a month-5
  add-card invite). Web checkout via Stripe + PayNow (no in-app purchase — login-to-unlock, Flo pattern).
- **Stack:** Expo (RN + web, one codebase), Supabase, Stripe. Claude Code builds it via `build-mvp`.
- **Taxonomy:** 7 verb-led shelves (Rebuild your blood · Heal your gut · Steady energy · Keep your milk
  flowing · Strengthen bones & repair · Calm & lift your mood · Steady immunity).
- **Label standard (3 only):** **Research-backed** (green, tap → Sources) · **Tradition** (amber) ·
  **Breastfeeding note** (soft beet). Sources sheet = real dated sources, real links, NO "Knowledge Bank
  (in-app)" jargon. Full rules in `feedback_card_language_standard`.
- **Mother-only mode is first-class** (FR-073): full value with zero helper; delegation = multiplier.
- **Helpers are phone-only, no computers** — WhatsApp link → kitchen-mode in browser, photo-led,
  big type, one step at a time, checkbox ticks (no "In" badge), contextual warnings only.
- **Faceless brand** — no founder face, no founder-story marketing. **Creator recipes:** transform fully
  (own prose/photos/scaling/boosts) + rename coined titles + NEVER name creators publicly.
- **Design NOT locked** — significant UX/UI elevation is an explicit workstream; run the `design-system`
  skill (needs Ilma's 4–6 inspiration screenshots) to produce `docs/design.md` before UI build.

## Content state — 49 live Cook Cards
GitHub Pages: `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/cook-cards/` (main-meals · snacks ·
drinks · desserts). 38 original + 11 new (Salmon, Sardines 3-ways, Liver Cutlets [Neringa's],
Gelatin Set, Dashamoola, Fermented Cucumbers, Khichdi, Chia Pudding, Lactation Balls, Spinach-Egg Wraps,
Iron Dips). The 11 new are on the new label standard; the original 38 still need the chip-name retrofit.
Index/inventory: **CARDS-AUDIT.md**.

## The design artifact (the centrepiece)
**mom-helper-split-preview.html** (live on Pages) — Borscht rendered two ways: the mum card (with the
"Your instructions" configurator: what-you-have scaling dial, tickable serve-with + PP-Gold boosts that
live-rebuild the helper card) beside the helper phone kitchen-mode (3-line ask → gather grid → step pager
with timers → Mum's-bowl step → Cooked ✓, + mastered "Short version"). This is where the card-language
standard was hammered out; it's also the design-session and pilot reference.

## ACTIVE THREAD — the Phase −1 pilot started 2026-07-03 (TONIGHT)
Ilma is testing the helper workflow with her real helper tonight, on two recipes: **Beet Kvass** and
**Neringa's Liver Cutlets ("liver patties")**. Deliverable being generated: **pilot/index.html** +
**pilot/kvass.html** + **pilot/liver-cutlets.html** — standalone helper kitchen-mode pages she opens on
her phone or WhatsApps to her helper. Watch-fors: does the helper open the link, cook from it, tap the
finish button, what confused her. Under-60%-cooked = redesign kitchen-mode. (Roadmap Phase −1 also adds a
mother-side check-in arm; Phase −1b is the acquisition workstream, proxy-ownable.)

## Second workstream — the Smart Pantry (built in a parallel chat)
A separate chat built the **smart pantry** feature. Its brief is **HANDOVER-SMART-PANTRY.md** (read it
alongside this). Live previews: `pantry-preview.html` (steady state) + `pantry-onboarding-preview.html`;
file map: `smart-pantry-map.html`. Locked pantry standards there: Apothecary naming, 4 evidence labels
(note: THIS chat later simplified card labels to **3** — reconcile the two in the Unify session),
notify-never-order, she-picks, the date model. Data facts: amla is 1-of-49 (a hook), a base64-grep gotcha,
torbangun. **These two workstreams (cook-card/helper kitchen-mode + smart pantry) are two halves of ONE
product and must be merged — see the plan below.**

## Strategy decisions locked 2026-07-03 (full detail in memory `project_strategy_decisions`)
- **Pantry scope = DURABLE ONLY** (spices/powders/grains/gelatin — track; fresh meat/fish/veg — do NOT
  inventory, handle via shopping list + "what do you have tonight?" quick-pick). Whole-kitchen value,
  pantry-only effort.
- **The moat = a data network effect**: every check-in/Cooked✓/verdict makes the kitchen smarter per
  household AND across households ("mums at week 3 with low energy cooked X"). This is the answer to the
  network-effect question.
- **Beat overwhelm with progressive disclosure**, not fewer features: ship the ONE loop beautifully, reveal
  smart features as she uses them. Postpartum = the wedge, not the ceiling.
- **Money + time made visible** in the weekly recap (meals handled, waste avoided). Revenue follows the
  loop working, not feature count. 2-weeks-free → Season Pass S$168 (locked).

## THE ACTION PLAN (revised 2026-07-03 after Fable's review against Ilma's concerns)
Paste THIS file first in every session. Parallelism: **A∥B on day one → C (needs B) → D (needs C)**;
Track 0 runs throughout.

- **Track 0 · Real-world, alongside everything (NOT a Claude chat):** (1) tonight's helper-pilot debrief —
  findings go to `docs/pilot-findings.md` and feed Session C's kitchen-mode decisions; (2) **start
  Phase −1b acquisition NOW** (roadmap ACQ-01..04: 10 partner conversations, group seeding with live
  cards + waitlist, gift pre-sale page, capped ad test) — proxy-ownable (husband/friend), time-sensitive,
  and it is THE growth answer (market/distribution = the review's weakest dimension, 40%). No chat
  session replaces this.
- **A · Tidy the house** — reorg repo per `smart-pantry-map.html`, BUT keep pantry + card previews at their
  current root paths (moving them breaks live Pages URLs); docs→docs/, screenshots→media/, dead→archive/.
- **B · Nail the vision** — rewrite VISION.md + MASTER-PLAN.md into ONE tight page each (repetitive/
  unfinished today). **Also DECIDE the free-model conflict** (currently unresolved): spec says free = one
  full loop then paywall; Ilma said "first two weeks free." Recommendation on the table: keep the
  one-loop paywall as the permanent model + make "2 weeks free" a founding-cohort launch promo (first N
  households, code, end date). One decision, then C and D build one thing.
- **C · Unify the product** — four NAMED deliverables (not just a merge): (1) pantry ↔ Tonight's-cards
  wiring + durable-vs-fresh scope + reconcile 3-vs-4 evidence labels; (2) **Learning Loop spec** — Ilma's
  "unique feature": exact V1 signals (check-ins, Cooked✓, verdicts, flags, pantry deltas — already in
  schema), which insights surface to HER in V1 (the weekly recap), what waits for scale (cross-household
  patterns); (3) **network-effect build sheet** — aggregate-data design, PDPA answer, cold-start plan
  ("every mum makes the kitchen smarter for the next" must be a feature, not a slide); (4) **money/time-
  saved metrics into the recap spec (FR-067)** — "meals handled · waste avoided · $ saved," the visible
  number people renew for. Update the PRD with all four.
- **D · Build — the BuilderOS completion map** (his sequence: idea✓ → validate✓ → plan✓ → design → build →
  launch): (1) after B+C, tell the chat **"regenerate the three docs from the updated VISION.md"**
  (product-planner regeneration = the "files need updating" step); (2) run **design-system** with Ilma's
  4–6 inspiration screenshots → docs/design.md; (3) fresh chat: **"build the full app using the build-mvp
  skill"**; (4) run **launch-checklist** when built. Spend the Fable budget on (3) — the one-shot build is
  where Fable pays off.

## Immediate next steps (the board)
1. **Run tonight's pilot** (cards being generated — links will be on Pages under `/pilot/`).
2. **Ilma's line-by-line review** of the four docs/ spec files.
3. **Design session** — Ilma brings 4–6 inspiration screenshots → run `design-system` → `docs/design.md`.
4. **Build window** (fresh chat, Fable 5): "Read docs/product-vision.md, docs/prd.md,
   docs/product-roadmap.md, docs/design.md — then build the full app using the build-mvp skill."
5. **Card-language cascade:** apply the 3-label rename + Sources cleanup + "Your instructions" pattern
   across the 49 live cards and the PRD copy (waiting on Ilma's "cascade" go-ahead).
6. **Ongoing:** Ilma hand-selects archive recipes + sends links; build each as a card, same house method
   (playbook + chips + permalinks + no creator names + rename coined titles).

## Working notes
- **BuilderOS skills** installed in `.agents/skills/` (product-planner ✓used, design-system, idea-validator
  ✓used, build-mvp, build-loop-claude-code, launch-checklist, idea-generator). From
  `github.com/BuildGreatProducts/builder-os` (the YouTube video's kit).
- **Deploys:** if a push "doesn't show" on the live URL, it's usually the GitHub Pages deploy queue —
  check `gh run list` and re-trigger; watch the live URL for the new content, not just the commit.
- **Model:** Ilma wants **Fable 5** for this work; the session has drifted to Opus 4.8 a few times (a
  safeguards auto-switch once, and manual `/model` switches). Re-set with `/model claude-fable-5` if needed.
- **codex CLI** reinstalled (`npm install -g @openai/codex`) so `/consensus` works again. The 4-model
  `/consensus` orchestrator script is NOT synced on this machine (Grok slot unavailable).
- **Two small open captures:** the Neringa liver-cutlets Instagram permalink; creator handles for the
  gelatin/chia/lactation archive saves (links are exact, names weren't in the index — never guessed).

## One honest strategic flag
The confidence review's weakest dimension is **market/distribution (40%)**: a faceless brand in a ~27k-births/yr
market with no installed audience. The mother-only mode + pilot protect the *product*; the funnel is the
real risk. After the first retention data, the parked **B2B2C confinement channel** (nanny agencies, doulas,
TCM halls, clinics) is the highest-leverage decision to revisit — it's recorded as parked, not rejected.
