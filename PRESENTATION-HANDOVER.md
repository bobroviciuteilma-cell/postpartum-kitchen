# New-session prompt — Postpartum Kitchen: the Presentation & Experience overhaul

> Open a fresh Claude Code session with `cwd = /Users/Enki/code/postpartum-kitchen`, then paste everything
> below the line. **Ilma will paste example images (printouts of recipe books she loves) at the start —
> study those before proposing anything.**

---

You're picking up **Postpartum Kitchen**. **First, read `AGENTS.md` in this folder end to end** — it is the
canonical context (what it is, the public `index.html` / private-gist split, the `build.py` → push → gist
deploy workflow, the design system, the app-router/search/tags JS, the 18-category taxonomy, the owner
profile, and the running backlog). Everything below assumes you've read it. Don't skip it.

## Who this is for
Owner is **Ilma** — a solo technical builder who has **just had (or is about to have) her baby**. She's very
visual, decisive on scope, defers on technical detail, and wants **crisp structured choices, not walls of
prose**. She reads in glances, often one-handed. Be warm, be brief, show don't tell.

## What this product is now
A **Mediterranean × Chinese-confinement postpartum recovery kitchen** — one self-contained HTML file that
renders as a calm phone app (home → category → recipe) on two live links + a PDF. ~**64 recipes across 18
specific food-type categories**, with: search, a **PP Gold ✦** powerhouse filter, "How are you feeling?" /
"Where are you?" (phase) filters, Today's rhythm, favourites, a shopping list, and a **Helper Prep** page
(deep-link `…/#helper`). The brand is **natural healing foods**; *this* edition is **postpartum-specific**
(others may follow — e.g. a Sick Kiddos edition).

## The mission this session: make the presentation world-class for tired mums
We've nailed *what's* in it. Now make **how it's presented** maximally satisfying for a foggy, busy new mum:
**informative but never overwhelming, calm, gorgeous, and web-native** (we are NOT a printed book — use
highlights, tap-to-reveal, tooltips, expandable sections, progressive disclosure). The north star: a tired
mum feels *understood, calm, and a little delighted*, and can get exactly what she needs in seconds — with
depth available *on demand*, not dumped on her.

**Ilma will share example printouts** (recipe-book pages she loves). **Study them first**: pull out what
works — the labelling, the hierarchy, the voice, the white space, the "at a glance" cues — then propose how
we adapt that to web (where we can do better than print).

## The recipe presentation system we ALREADY locked (build on this, don't discard)
Every recipe card follows the same skeleton, same order, so the eye learns it once:
1. **Name** — plain English; any traditional name small & grey (e.g. "Rice & Lentil Porridge (Khichdi)").
2. **The hook** — one warm line, **benefit first, then yield** (e.g. *"Deep iron & collagen — sip a cup a day · makes ~3 L"*).
3. **Tags** — consistent chips, consistent order: **PP Gold ✦ · GF · Make-ahead ·** then nutrients (Iron, Protein…).
4. **What you need** — quantity **bold** left, ingredient after.
5. **How to make it** — numbered steps; each = **Bold action.** + one short sentence + a time chip; verb-first.
6. **✦ PP Gold version** — gold `.box.ppgold` box, *only if it has one*: "Add: X *(when)* · Y *(when)*." Lives in ONE place — never repeated in the ingredients or steps. (Ilma's words: *"stick to PP Gold"*, NOT "Golden Boost"; keep it crisp, no duplicate callouts.)
7. **Good to know** — cream `.box` box: the honest "why it helps" + how to keep/use it.
8. **From** — `@creator →` (or *Kitchen recipe / Tori's*). Always credited.

**Voice:** warm, second-person, brief; verb-first present-tense steps; honest, never clinical ("food, not
medicine"); short lines. **Signposts (identical everywhere):** ✦ gold = PP Gold (tag *and* upgrade box);
gold box = PP Gold version; cream box = Good to know; rust step-numbers, bold quantities, time chips.

The **Chicken Bone Broth** card (Soups & Bowls) is the living reference — match it.

## New things to design & add this overhaul
- **Visual theme — LOCKED: Provence apothecary / herbarium.** Reference: *The Fine Cheese Co.* (Bath,
  England) packaging — soft **linen/oatmeal paper** (faint woven texture), delicate **watercolor botanicals**
  (rosemary sprig, little lavender flowers, amber olive-oil drops), refined **engraved serif caps + a flowing
  script logotype**. Restrained, organic, heritage — calm and *very* legible, never busy or twee. A built
  reference mock is at **`provence-reference.html` (in this folder)** (render it to see the target).
  **Design tokens (Google Fonts):** titles = **Cormorant Garamond** (elegant high-contrast serif); labels /
  small-caps = **Marcellus** (Trajan-like engraved caps, wide letter-spacing); body/prose = **EB Garamond**;
  script logotype/flourishes = **Pinyon Script**. *(This replaces the old Fraunces + Inter.)*
  **Palette (muted, desaturated):** linen `#efe8d7`/`#f6f0e2`, warm-charcoal ink `#4a4035`/`#6f6353`, sage
  green `#7a895a`/`#5f6e44` (rosemary), soft lavender `#9c8cb6`, amber `#c39a47`/`#a87f2f` (oil drops — and
  the PP Gold ✦). Hairline rules `#d9cdb6`, dotted ingredient separators, ornamental botanical dividers.
  **Illustrations:** SVG line-botanicals as the consistent baseline; for true watercolor richness use Ilma's
  ChatGPT gouache art OR **public-domain vintage botanical prints** (old herbals / Biodiversity Heritage
  Library — freely usable and perfect for this aesthetic). **In-session AI image gen is NOT available** — drop
  any art files in `assets/`, commit/push, reference by **absolute Pages URL** (resolves on both links).
- **Web-native depth without overwhelm:** highlights, **tap an ingredient → why it's there** (popover),
  expandable "why it works", glossary-on-tap, a calm "at a glance" strip. Progressive disclosure: surface the
  essentials, hide the depth behind a tap.
- **Child suitability (NEW data field on every recipe).** Ilma wants to know **is this suitable for a child,
  from what age, and any tweak** (e.g. "from 1 yr; skip the honey", "purée for 6 mo+", "adults only — has
  liquor/liver in excess"). Design how this surfaces — a clear **tag/badge + a short "For little ones" note
  or mini-card** — consistent across all recipes. This is the headline new feature; get the model right
  (badge states + the note), then apply.

## The consumer journey (LOCKED 2026-06-21) — this is a recovery companion, not a cookbook
The product is **5 screens** that carry a tired, one-handed mum from *"I'm wrecked, what do I eat"* to *eating*:
1. **Home** — calm entry: greeting, one search box, "How are you feeling?" + "Where are you? (week)" + Today's rhythm. Not a wall of recipes.
2. **Pick a way in** — three doors, never all at once: a **feeling** (low iron / low milk / constipated), her **week**, or a **food type**. This turns 64 recipes into "here are 4 for *you*."
3. **Recipe page** — the locked Provence card (hook · tags · what-you-need · steps · ✦ PP Gold version · Good to know · **child-suitability** · tap-ingredient→why).
4. **Save & gather** — favourites + a shopping list that pools across recipes.
5. **Helper Prep** (`/#helper`) — send one link to mum/partner; they cook, she eats. No app to learn.
North star: **remove a decision at the worst moment** (3am, foggy, starving, one hand). Visual map: `/tmp/journey.html` (rebuild to view).

### Four mom-first upgrades — APPROVED (all 4, 2026-06-21)
- **"Feed me now"** — one button on **Home**; knows her week + the hour, picks **one** recipe, says "have this." Zero browsing. The headline feature.
- **Time & energy filter + 3am set** — on **screen 2**: "5 min / 20 min / someone's cooking," plus a **one-handed night-feed snacks** shelf for bedside grazing.
- **Week-by-week companion** — woven into the **Week chip**: "Week 2: iron's low, tissue's healing — lean on these 3." A guide, not a menu.
- **Freezer batch-prep plan** — its own track + shared into **Helper**: cook-ahead checklist + freezer list; *do it now while pregnant*, eat through the foggy weeks. (For the APP this overrides the personal PDF's "cook-fresh-not-batch" stance.)

Build order not yet chosen — propose a sane sequence (likely: convert one real recipe to Provence in the live app first, then Home + "Feed me now", then the rest).

## How to work with Ilma (important)
- **Study her example printouts first, then come back with a crisp, prioritised proposal** (the presentation
  system + the botanical direction + the child-suitability model) as **structured multiple-choice questions**,
  one decision at a time, recommendation first. Don't dump a huge plan; don't start big execution before she
  picks the direction.
- Once she gives direction, **apply it and render the result** — don't re-ask the same thing.
- **Verify visually.** She can't preview HTML in her IDE: headless-Chrome **screenshot** static/recipe views
  and Read them back; open the **real browser** for interactive bits (search, filters, popovers, helper flow).
  Screenshot before saying it's done. Window width **≥ 520** (macOS Chrome clamps below ~500 and crops).
- **Plain absolute file paths, never markdown links for files** (her IDE workspace ≠ where the code lives).
  Web URLs as links are fine.
- **Top-tier image/video models only** — never silently downgrade to fast/flash variants.
- Stay inside the Claude environment — don't punt her to ChatGPT/Google for things the tools can do.
- **Deploy every change to BOTH links:** edit `master.private.html` → `python3 build.py` → commit & push
  `index.html` (public) **AND** re-upload the noindex copy to the secret gist (private) — see AGENTS §4. PDF
  is print-media and unaffected by the screen-only app.
- A note on **sources:** 9 older "foundational" recipes (Khichdi, bone broth, the laddu/til-gur, bedtime
  milk, smoothie, tonics, liver pâté, teas) currently have **no source link** and their origin is genuinely
  unknown — do **not** invent sources. Ilma's private IG saved folders can only be read if the
  **Claude-in-Chrome extension is reconnected** (Apify can't see private folders; it scrapes public post URLs
  only). Leave the 9 as-is unless she provides links or reconnects.

## Definition of done
A **coherent, premium, botanical, web-native** recipe experience: every card follows the locked skeleton +
voice + signposts; **child-suitability** is surfaced clearly and consistently; depth is available on tap
without overwhelming; it feels calm, informative and a touch delightful. Applied across the recipes, **shipped
to both links, and screenshot-verified.**

**Begin by reading `AGENTS.md`, then study Ilma's example printouts, then propose the presentation system as
crisp prioritised choices — before any big execution.**
