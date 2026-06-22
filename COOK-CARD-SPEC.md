# The Cook Card — Build Spec
*Merged from GPT-5.2 + Gemini 3.1 Pro (both independently picked this as the killer feature). Placement decided: **sibling feature, both entry points.** Status: spec for review, no code yet.*

---

## 1. What it is (the wow)
A postpartum mum's deepest exhaustion isn't cooking — it's the **mental load of managing the person who cooks for her** (husband / confinement nanny / her own mum). The Cook Card kills that load: she taps **one button**, and her symptom-driven plan becomes a **dummy-proof, high-contrast kitchen brief** she WhatsApps straight to whoever cooks. She stops thinking about food and simply gets fed what she needs — without saying a word.

The shareable moment: *"I stopped thinking about food and started feeling human — here, steal my Cook Card."* The helper sees a beautiful, easy app and shows other employers → **viral loop inside the Sentosa mum/helper network.**

---

## 2. Placement (DECIDED: sibling, both entry points)
Reachable from **two places**, not buried behind the Clock:
- **A. Symptom Check-in result screen** — "Turn today's plan into a Cook Card →" (free users taste it)
- **B. Recovery Clock unlocked plan** — "Send this week to your helper →" (premium continuation)

Free vs paid split (recommended — adjustable):
- **Free:** generate + share a **2–3 day** Cook Card from today's check-in. Enough to feel the relief and forward it.
- **$9 unlock (bundled with the Recovery Clock):** full **7-day** plan, unlimited regenerations + swaps, saved shopping list, and a **"Recalibrate" link** refresh as her symptoms shift.
- Optional later (only if traction): **$4 micro-txn** to regenerate a fresh helper link at a new stage (~3 months, when symptoms shift to hair loss / deep fatigue).

> Rationale: sibling reach means non-payers still spread it (the viral vector is the *helper*, not the mum); the 7-day + regenerations is the utility that justifies $9. Gemini's line: paying for the handoff is a *utility* buy, not a *curiosity* buy.

---

## 3. The mechanism — a Base64 "magic link" (ZERO backend)
The whole point: this fits a self-contained HTML app with no server, no accounts.

1. Mum taps **"Make a Cook Card."**
2. App takes her current local state → builds a **truncated payload** (see §5 privacy) → `JSON.stringify` → `btoa()` Base64 → appends to a URL hash:
   `postpartumkitchen.com/cook#p=eyJ3ZWVrIjpbeyJ...`
3. She shares that link via the native share sheet / WhatsApp.
4. Helper taps it → loads **one new view** (`/cook` or a routed `#cook` screen) → JS reads `location.hash`, `atob()` decodes, renders the Caregiver Dashboard.

No data ever leaves her phone except what's encoded in the link she chooses to send. **Build cost: one new screen + an encoder + a decoder/renderer.**

---

## 4. Data shapes (minimal additions to what exists)

**4a. Recipe tags** (add 2–3 fields to existing recipe objects):
```js
{ id, title, keywords:[],
  tags:["iron","zinc","calcium","broth-base","5min","freezer-friendly"],
  helperFriendly:true, time:15, pantryLevel:"low" }
```

**4b. The shared payload** (what gets Base64'd — note: NO raw symptoms/mood, see §5):
```js
{
  v:1,
  focus:["iron","magnesium"],          // 2 priority nutrients, max
  weekLabel:"Iron rebuild week",       // culinary framing, not medical
  prep:[ {day:"Mon", recipeId:"meatstock", note:"batch — base for the week"} ],
  menu:[ {day, recipeId, title} ],     // base-recipe pattern: 1 base → many soups
  rules:["Iron meal + a vitamin-C source (lime/orange)","No tea/coffee within 1 hr of iron meals"],
  shopping:{ produce:[], protein:[], pantry:[] },
  avoids:["seafood"]                    // dietary only, not medical
}
```

**4c. Locally-stored plan** (mum's side, localStorage — full fidelity, never shared):
```js
{ createdAt, seed:{symptoms:[],nutrients:[],prefs:{}}, days:[...], shoppingList:{...} }
```

**4d. SHOPPING_MAP** (new, tiny — canonical staples so the list is "good enough"):
```js
{ "bone broth":["chicken bones OR boxed broth","ginger","spring onion"],
  "vitamin c":["kiwi OR orange","capsicum"], ... }
```

---

## 5. The credibility / privacy rule (NON-NEGOTIABLE)
Both models flagged the same risk: the helper is often her **employee**, and she may have tapped "low mood" or "heavy bleeding."
- **The payload strips ALL symptom + mood + medical data.** It carries only the *culinary focus* ("This week: iron-rich meals") and recipes.
- The helper dashboard is titled **"Postpartum Kitchen — Prep Sheet,"** never anything clinical. It never says "anemic," "depressed," "low supply."
- All medical content, the red-flag triage, and the symptom history stay **on the mum's phone only.**

---

## 6. Generation logic (reuse the existing engine)
1. Take the nutrient focus the **Symptom Check-in Engine** already computes. Cap at **2 priority nutrients** (avoid overfitting).
2. Pick the week's **base recipe** (broth / meat stock / pho) → use the **base-recipe pattern** so one batch-cook (Mon) yields the week's derivatives.
3. Each day: anchor (from recipe library, tagged to focus + easy + helperFriendly) + a booster (from NUTRI "in a pinch" fixes) + an absorption pair (from Healing Guide **Power Pairs** → rendered as a "Golden Rule").
4. Shopping list = union of SHOPPING_MAP staples for the chosen recipes.

---

## 7. Screens

**Mum side (2 screens):**
- **Setup (30 sec):** pre-filled from check-in/Clock. Three toggles only — *Time (10/20/30 min)*, *Kitchen reality (stove / microwave-only)*, *Avoids (seafood/dairy/spicy)*. CTA "Make my Cook Card."
- **Share:** preview + native share sheet ("Send to your helper"). Free = 2–3 days; unlock prompt for full week.

**Helper side (1 new view — the magic-link target):**
- High-contrast **Caregiver Dashboard** (aesthetic shifts from calm herbarium → clean, legible utility for a messy kitchen):
  1. **Prep List** (batch tasks, from base recipes)
  2. **The Menu** (per-day, simple)
  3. **The Golden Rules** (absorption pairs, visually dominant — lemon+spinach icon, "always serve with…")
  4. **Shopping list** grouped by aisle (+ optional NTUC/FairPrice/RedMart keyword text for Singapore)

---

## 8. Credibility guardrails (recap)
- Frame everything **food + education, not medical**: "may support," "a common nutrition approach" — never "will fix" / "will increase supply."
- Reuse the **red-flag triage strip** on the mum's setup screen.
- Keep a one-tap **"How we source this"** (AAD/ACOG/NHS/WHO) link.

---

## 9. MVP build order (solo founder)
1. Add the 3 recipe tags + a small SHOPPING_MAP for existing recipes.
2. Write the payload encoder (state → truncated JSON → Base64 → URL) and the decoder/renderer.
3. Build the **Helper Dashboard** view (`#cook`) — this is the one genuinely new screen.
4. Add the mum-side Setup + Share screens, wired to the existing check-in result.
5. Gate the 7-day / regenerations behind the existing $9 unlock; leave 2–3 days free.

---

## 10. Decisions still open for Ilma
- **Free vs paid line:** is 2–3 days free / 7 days paid the right split? (recommended)
- **Recalibrate micro-txn ($4):** include at launch or defer?
- **Singapore shopping shortcuts:** include NTUC/FairPrice/RedMart keywords now, or later?
- **Runner-up — "Midnight SOS Mode"** (3am amber-moon → dark mode → no-cook fixes): build alongside, or separately? (cheap, slots into existing night-mode work)
