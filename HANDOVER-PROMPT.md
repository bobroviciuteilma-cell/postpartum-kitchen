# New-session prompt — Postpartum Kitchen

> Paste everything below into a fresh Claude Code session opened with
> `cwd = /Users/Enki/code/postpartum-kitchen` (so CLAUDE.md → AGENTS.md auto-loads).

---

You're picking up **Postpartum Kitchen**. **First, read `AGENTS.md` in this folder end to end** — it's the
canonical context (what it is, the public/private split, build & deploy workflow, design system,
conventions, the self-building app router + search, content map, owner profile, and backlog). Don't
skip it; everything below assumes you've read it.

## Who this is for and what she wants

Owner is **Ilma** — a solo technical builder, third trimester (baby due ~mid-2026), planning a vaginal
birth, has hemorrhoids and candida, eats Mediterranean + keto-leaning. She is **very visual**, decisive
on scope, defers on technical detail, and wants **crisp structured choices, not walls of prose**.

**Her two goals — hold both at once:**
1. **Personal:** the fastest, fullest postpartum recovery — maximum energy, "zero depletion," strong
   immunity, and minimal hair loss — through a Mediterranean × Chinese-confinement, **keto-leaning**
   plan that protects ferritin / protein / zinc / vitamin D and respects her specifics (soft-stool
   priority for hemorrhoids, candida, her supplement stack). Be honest, not over-promising (some
   shedding is hormonal).
2. **Commercial:** grow this from her private plan into a **product other mums want and would pay for.**
   The real product is **not the recipes — it's the personalisation**: a guided "build your postpartum
   kitchen" quiz that turns each mum's situation (birth type, diet, deficiencies, budget, helper or not,
   cultural foods) into a plan tailored to *her*. That bespoke flow was done manually via Q&A to build
   Ilma's own version; productising it is the prize.

## Your mission this session

**Elevate it from "a beautiful personal recipe doc" to "a product a new mum would be excited to use and
share."** It must become more *useful* (to Ilma's recovery), more *commercially compelling*, and more
*clear, warm, exciting and enticing* for other mums. **There is a lot of work still** — don't treat this
as finished polish; treat it as a product you're shaping.

Concretely, the opportunity areas (audit the live site first, then prioritise — don't blindly do all):

- **Positioning & emotional pull.** Right now it opens straight into utility. A new, exhausted mum needs
  to instantly feel *"this is for me, it's calm, it will help."* Consider a real landing/hero with a
  clear promise, the "why this works" in one breath, and a warm voice throughout. Make it feel premium
  and reassuring, magazine-grade, never clinical or overwhelming.
- **The personalisation engine (the commercial core).** Design and prototype the guided quiz → tailored
  plan. Even a smart client-side version (branching questions → filtered/reordered recipes + a custom
  "your day" + flagged supplements) would validate the concept with mum testers. This is the highest-
  leverage thing to make "commercially interesting."
- **Content depth & correctness.** Fill the 4 gated "My version" placeholder cards with real recipes;
  add MCT oil to the glossary + Power Smoothie; re-verify every recipe is hyperlinked, attributed, and
  internally consistent (amounts, alternatives). Make sure nothing reads as thin.
- **Trust & shareability.** A feedback path for mum testers, credibility framing (educational, not
  medical advice — keep that), and the warmth that makes someone forward it to a pregnant friend.
- **Useful product mechanics.** Download-PDF button, favourites (localStorage), a shopping-list
  generator, servings scaler — pick what actually serves the goals, not everything.
- **The painted illustration set** (in flight — Ilma is generating warm hand-painted gouache art in the
  ChatGPT app for the hero + dividers). When she sends image files: drop them in `assets/`, commit/push,
  reference by **absolute Pages URL** so both the Pages site and the githack gist resolve them. (In-
  session AI image generation is NOT available here.)

## How to work with Ilma (important)

- **Start by auditing the two live links and the content, then come back with a crisp, prioritised
  roadmap and let her choose** — use structured multiple-choice questions (the AskUserQuestion style),
  one decision at a time, recommendation first. Don't dump a 2,000-word plan. Don't start big
  execution before she's picked the direction.
- Once she gives specific direction, **apply it directly and render the result** — don't re-ask the same
  thing wrapped in another question.
- She can't preview HTML in her IDE: **verify visually** — for static/brochure views render with headless
  Chrome to PNG and Read it back; for interactive UI (hover, search, the app router) open it in the
  browser. Screenshot the actual result before saying it's done.
- **Plain absolute file paths, never markdown links for files** (her workspace ≠ where the code lives).
  Web URLs as links are fine.
- **Top-tier models only** for any image/video work — never silently downgrade to fast/flash variants.
- Stay inside the Claude environment — don't punt her to ChatGPT/Google for things skills/tools can do.
- **Deploy workflow every change:** edit `master.private.html` → `python3 build.py` → commit & push
  `index.html` (public) AND re-upload the noindex copy to the secret gist (private). Both links must
  stay in sync. PDF is print-media and unaffected by the screen-only app router.

## Definition of done for this push

The site should make a tired new mum feel *understood, calm, and a little excited* within ten seconds;
there should be a working (even if prototype) **personalisation flow** that proves the commercial idea;
and the content should be complete and consistent enough to put in front of real mum testers for
feedback. Ship to both links and screenshot-verify.

Begin by reading `AGENTS.md`, then audit the live site and propose the prioritised roadmap.
