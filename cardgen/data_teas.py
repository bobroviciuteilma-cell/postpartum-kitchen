# -*- coding: utf-8 -*-
"""Batch 1 — the six teas. Claims follow TAXONOMY-SYNERGY.md verdicts:
fennel dose note (A.1 #4), tea-iron softened (A.2), galactagogue evidence honest
(PMC6567188), chai caffeine per LactMed NBK501467 (fetched & verified 2026-07-07).
Chips: rb = research-backed · t = tradition · b = breastfeeding note. Chips only on
health claims; kitchen-craft lines carry none."""

# ---- shared, verified source snippets (every link real; see TAXONOMY-SYNERGY Phase D) ----
ODS_IRON = '<a href="https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/" target="_blank" rel="noopener">NIH — Iron fact sheet: vitamin C &amp; absorption (2023)</a>'
CAMBRIDGE_VITC = '<a href="https://www.cambridge.org/core/journals/proceedings-of-the-nutrition-society/article/regulation-of-dietary-iron-bioavailability-by-vitamin-c-a-systematic-review-and-metaanalysis/013552A920BF94D2BEFA94133AA6AB29" target="_blank" rel="noopener">Proc. Nutrition Society — vitamin C &amp; iron bioavailability, systematic review &amp; meta-analysis</a>'
USDA = lambda what: f'<a href="https://fdc.nal.usda.gov/" target="_blank" rel="noopener">USDA FoodData Central — {what}</a>'
ODS_MAG = '<a href="https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/" target="_blank" rel="noopener">NIH — Magnesium fact sheet</a>'
ODS_CAL = '<a href="https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/" target="_blank" rel="noopener">NIH — Calcium fact sheet</a>'
GAL_PMC = '<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6567188/" target="_blank" rel="noopener">PMC6567188 — galactagogue evidence review (modest at best)</a>'
GAL_BFN = '<a href="https://www.breastfeedingnetwork.org.uk/factsheet/increasing-milk-supply-use-of-galactagogues/" target="_blank" rel="noopener">Breastfeeding Network — galactagogues factsheet</a>'
LACTMED_FENNEL = '<a href="https://www.ncbi.nlm.nih.gov/books/NBK501793/" target="_blank" rel="noopener">LactMed (NIH) — Fennel</a>'
DRUGS_FENNEL = '<a href="https://www.drugs.com/breastfeeding/fennel.html" target="_blank" rel="noopener">Drugs.com — fennel &amp; breastfeeding</a>'
LACTMED_CAFFEINE = '<a href="https://www.ncbi.nlm.nih.gov/books/NBK501467/" target="_blank" rel="noopener">LactMed (NIH) — Caffeine: ~300 mg/day generally compatible; Europe suggests 200 mg</a>'
FFD = '<a href="https://restorativeroots.com/blogs/postpartum-blog/the-first-forty-days-review" target="_blank" rel="noopener">The First Forty Days — the confinement-food tradition (review)</a>'
BANYAN = '<a href="https://www.banyanbotanicals.com/blogs/wellness/birthing-ayurveda-postpartum-nurturing-the-mother" target="_blank" rel="noopener">Banyan Botanicals — Ayurvedic postpartum nourishment</a>'

MILK_MEANING = ("Breastfeeding note — a care flag, not a grade. This is a traditional nursing tea, and it earns "
                "its place as warmth, hydration and ritual. The honest read on ALL herb teas: studies of milk-boosting "
                "herbs show modest effects at best — frequent feeding and rest move supply far more than any cup.")

DRINKS = [

# ---------------------------------------------------------------- jujube & goji
{
 "slug": "jujube-goji-tea",
 "name": "Jujube & Goji Tea",
 "eyebrow": "Tea <span class='dot'>·</span> Rebuild your blood <span class='dot'>·</span> Warming tradition",
 "sub": "A sweet, ruby tea of red dates and goji — the classic confinement brew, warm through the day.",
 "hero_alt": "A ruby-red cup of jujube and goji tea",
 "time": "about 20 min",
 "makes": "3 cups",
 "keep": "holds in the pot — gently reheat through the day",
 "when": "Daytime — a warm cup mid-morning or afternoon. Naturally sweet, caffeine-free, gentle every day of week one.",
 "why": [
  {"text": "Red dates (jujube) — the heart of the East-Asian confinement kitchen, brewed for warmth &amp; energy after birth", "chip": "t", "ev": "jujube"},
  {"text": "Goji berries — gently sweet, a nutrient-dense berry in food-level amounts", "chip": "t", "ev": "goji"},
  {"text": "Warm &amp; caffeine-free — easy on a depleted system"},
  {"text": "Naturally sweet — the fruit does it, no sugar needed"},
 ],
 "bfnote": None,
 "ev": {
  "jujube": {"cls": "t", "chip": "tradition", "title": "Red dates — the confinement brew",
   "meaning": "Tradition, honestly labelled. Red-date (jujube) tea is a centuries-old East-Asian postpartum staple, brewed through the confinement month for warmth and energy. The heritage is real; it has not been measured in modern trials — so we say tradition, not proof.",
   "src": [FFD, "Traditional East-Asian postpartum practice — red-date brews through the confinement month"]},
  "goji": {"cls": "t", "chip": "tradition", "title": "Goji berries",
   "meaning": "Tradition, honestly labelled. Goji is a nutrient-dense berry as a food, and the classic partner to jujube in postpartum brews. A light tea draws out only some of what the berry holds — we don't claim more than the cup delivers.",
   "src": [USDA("goji berries, dried (nutrient data)"), "Traditional pairing with jujube in East-Asian postpartum kitchens"]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "dates", "label": "2 extra dates", "small": "sweeter, still no sugar", "on": True},
   {"k": "ginger", "label": "a few slices of ginger", "small": "extra warmth", "on": False},
  ], "note": "The whole pot is yours — sip it through the day, and eat the softened fruit too."},
 "when_opts": {"label": "For", "opts": ["Morning", "Mid-morning", "Afternoon"], "sel": "Morning"},
 "ings": [
  {"k": "dates", "n": "Red dates (jujube)", "q": "6, split", "img": "img/jujube-goji-tea/ing-01-red-dates.jpg", "prep": "torn open"},
  {"k": "goji", "n": "Goji berries", "q": "1 tbsp", "img": "img/jujube-goji-tea/ing-02-goji-berries.jpg"},
  {"k": "water", "n": "Filtered water", "q": "3 cups", "img": "img/jujube-goji-tea/ing-03-filtered-water.jpg"},
  {"k": "ginger", "n": "Fresh ginger", "q": "2 slices", "img": "img/jujube-goji-tea/ing-04-fresh-ginger.jpg", "opt": True},
 ],
 "method": [
  {"ic": "Split the dates", "verb": "Tear the dates open — 2 min",
   "detail": "Tear or slit <b>6 red dates</b> so each one falls open — this lets the sweetness out into the water.",
   "done": "every date torn open.",
   "say": "Step 1. Tear or slit the red dates so they fall open. This lets the sweetness out."},
  {"ic": "Simmer", "verb": "Simmer the dates — 15 min",
   "detail": "Drop the dates (and the <b>ginger</b>, if Mum asked) into <b>3 cups water</b>. Bring to a gentle simmer, lid half on.",
   "timer": [{"label": "Simmer", "min": 15}],
   "done": "the water blushed red, dates soft.",
   "say": "Step 2. Add the dates and ginger to the water and let it simmer gently."},
  {"ic": "Add the goji", "verb": "Goji in — 5 min more",
   "detail": "Stir in <b>1 tbsp goji berries</b> and simmer <b>5 min</b> more. Pour a cup warm — the softened fruit is for eating too.",
   "timer": [{"label": "Simmer", "min": 5}],
   "done": "a ruby tea, plump goji floating.",
   "say": "Step 3. Stir in the goji berries, simmer a little longer, and pour a cup warm."},
 ],
 "overview_method": [
  "Tear the dates open.",
  "Simmer them in the water — 15 min.",
  "Goji in, 5 min more; pour warm.",
 ],
 "nutri": [
  {"v": "Sweet", "k": "from the fruit · no sugar"},
  {"v": "Caffeine", "k": "none"},
  {"v": "Warm", "k": "the confinement way"},
 ],
 "nutri_label": "In this pot",
 "instr_note": "Made to its pot — nothing to scale. Your helper's card matches this one.",
},

# ---------------------------------------------------------------- nettle
{
 "slug": "nettle-tea-card",
 "name": "Nettle Tea",
 "eyebrow": "Herbal tea <span class='dot'>·</span> Keep your milk flowing <span class='dot'>·</span> Minerals",
 "sub": "A deep-green mineral tea — the everyday sip that quietly carries iron, calcium &amp; magnesium.",
 "hero_alt": "A cup of deep-green nettle tea",
 "time": "about 15 min",
 "makes": "1 cup",
 "keep": "brew fresh — the same leaves take a second steep",
 "when": "Any time, every day. The longer it steeps, the more minerals end up in the cup.",
 "why": [
  {"text": "Nettle leaf — genuinely mineral-dense: iron, calcium &amp; magnesium at food level", "chip": "rb", "ev": "minerals"},
  {"text": "A squeeze of lemon — vitamin C helps the iron absorb", "chip": "rb", "ev": "vitc"},
  {"text": "One of the classic nursing-mother teas", "chip": "t", "ev": "milk"},
  {"text": "Caffeine-free — an all-day habit"},
 ],
 "bfnote": {"text": "Nettle is a food-level herb in tea amounts and a long-standing nursing tea. The honest read: herbs move milk far less than frequent feeding does — enjoy the cup for its minerals and let the feeding do the heavy lifting.", "ev": "bf"},
 "ev": {
  "minerals": {"cls": "rb", "chip": "research-backed", "title": "Nettle — a mineral-dense leaf",
   "meaning": "Research-backed on composition. Nettle leaf measurably carries iron, calcium and magnesium — a gentle food-level dose per cup, not a supplement. A long, covered steep pulls more of them into the water.",
   "src": [USDA("stinging nettles, blanched (nutrient data)"), ODS_MAG]},
  "vitc": {"cls": "rb", "chip": "research-backed", "title": "Lemon — vitamin C unlocks plant iron",
   "meaning": "Research-backed. Vitamin C taken alongside plant (non-heme) iron reliably increases how much of it your body absorbs — the squeeze of lemon is working, not garnish.",
   "src": [CAMBRIDGE_VITC, ODS_IRON]},
  "milk": {"cls": "t", "chip": "tradition", "title": "Nettle as a nursing tea",
   "meaning": "Tradition, honestly labelled. Nettle appears in nursing-tea blends across Europe. Trials of milk-boosting herbs show modest effects at best — we keep this as tradition, not a promise.",
   "src": [GAL_PMC, GAL_BFN]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Nettle while breastfeeding",
   "meaning": MILK_MEANING,
   "src": [GAL_PMC, GAL_BFN]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "steep", "label": "the long steep — 15 min", "small": "more minerals in the cup", "on": True},
   {"k": "lemon", "label": "a squeeze of lemon", "small": "unlocks the iron", "on": True},
  ], "note": "Both happen in your cup — nothing changes for anyone else."},
 "when_opts": {"label": "For", "opts": ["Morning", "Mid-morning", "Afternoon"], "sel": "Mid-morning"},
 "ings": [
  {"k": "nettle", "n": "Dried nettle", "q": "1–2 tsp", "img": "img/nettle-tea-card/ing-01-dried-nettle.jpg", "prep": "or 1 tea bag"},
  {"k": "water", "n": "Just-boiled water", "q": "1 cup", "img": "img/nettle-tea-card/ing-02-just-boiled-water.jpg"},
  {"k": "lemon", "n": "Lemon", "q": "a squeeze", "img": "img/nettle-tea-card/ing-03-a-squeeze-of-lemon.jpg", "opt": True},
 ],
 "method": [
  {"ic": "Steep, covered", "verb": "Steep, covered — 10–15 min",
   "detail": "Pour <b>1 cup just-boiled water</b> over <b>1–2 tsp dried nettle</b>. Cover the cup and let it steep — longer pulls more minerals.",
   "timer": [{"label": "Steep", "min": 10}],
   "cap": "Covering the cup keeps the goodness in the water.",
   "done": "deep green, almost like a light broth.",
   "say": "Step 1. Pour just-boiled water over the nettle, cover the cup, and let it steep."},
  {"ic": "Strain", "verb": "Strain",
   "detail": "Strain into Mum's cup. The spent leaves will take a second steep later.",
   "done": "a clear, deep-green cup.",
   "say": "Step 2. Strain into the cup. Keep the leaves for a second steep."},
  {"ic": "Lemon & take it up", "verb": "Lemon, then take it to Mum",
   "detail": "Add <b>a squeeze of lemon</b> if Mum asked — it helps the iron absorb. Take it to her warm.",
   "done": "a warm green cup, on its way.",
   "say": "Step 3. Add a squeeze of lemon if Mum asked, and take the cup to her warm."},
 ],
 "overview_method": [
  "Cover &amp; steep the nettle — 10–15 min.",
  "Strain.",
  "A squeeze of lemon; take it up warm.",
 ],
 "nutri": [
  {"v": "Iron", "k": "food-level · plant"},
  {"v": "Ca + Mg", "k": "the mineral pair"},
  {"v": "Caffeine", "k": "none"},
 ],
},

# ---------------------------------------------------------------- caraway
{
 "slug": "caraway-tea-card",
 "name": "Caraway Tea",
 "eyebrow": "Herbal tea <span class='dot'>·</span> Heal your gut <span class='dot'>·</span> After meals",
 "sub": "A warm seed tea that settles a bloated tummy — the after-dinner cup.",
 "hero_alt": "A cup of golden caraway seed tea",
 "time": "about 10 min",
 "makes": "1 cup",
 "keep": "the seeds take a second steep",
 "when": "After meals — especially when you feel bloated or windy.",
 "why": [
  {"text": "Caraway — a classic carminative seed: eases bloating &amp; wind after meals", "chip": "t", "ev": "digest"},
  {"text": "Same seed family as fennel — a traditional nursing ally", "chip": "t", "ev": "milk"},
  {"text": "Warm and gentle on a tender gut"},
  {"text": "Caffeine-free"},
 ],
 "bfnote": {"text": "Caraway is a kitchen spice at tea doses and a traditional nursing seed. Herbs move milk far less than feeding often does — this cup earns its place by settling dinner.", "ev": "bf"},
 "ev": {
  "digest": {"cls": "t", "chip": "tradition", "title": "Caraway — the carminative seed",
   "meaning": "Tradition, honestly labelled. Caraway is one of Europe's oldest wind-easing (carminative) seeds, brewed after heavy meals for centuries — including through the postpartum weeks. Kitchen-dose tradition, not a clinical claim.",
   "src": ["Traditional European carminative use — caraway seed tea after meals", "Long-standing postpartum kitchen practice in Central &amp; Eastern Europe"]},
  "milk": {"cls": "t", "chip": "tradition", "title": "Caraway as a nursing seed",
   "meaning": "Tradition, honestly labelled. Caraway sits in the same traditional nursing-seed family as fennel and anise. Trials of milk-boosting herbs show modest effects at best — tradition, not a promise.",
   "src": [GAL_PMC, GAL_BFN]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Caraway while breastfeeding",
   "meaning": MILK_MEANING,
   "src": [GAL_PMC, GAL_BFN]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "fresh", "label": "crush the seeds just before", "small": "more of the settling oils", "on": True},
   {"k": "honey", "label": "a little honey", "small": "if you fancy it", "on": False},
  ], "note": "Your cup, your call — nothing here changes the family's anything."},
 "when_opts": {"label": "For", "opts": ["After lunch", "After dinner", "Anytime"], "sel": "After dinner"},
 "ings": [
  {"k": "seeds", "n": "Caraway seeds", "q": "1 tsp", "img": "img/caraway-tea-card/ing-01-caraway-seeds.jpg", "prep": "lightly crushed"},
  {"k": "water", "n": "Just-boiled water", "q": "1 cup", "img": "img/caraway-tea-card/ing-02-just-boiled-water.jpg"},
  {"k": "honey", "n": "Honey", "q": "a little", "img": "img/caraway-tea-card/ing-03-a-little-honey.jpg", "opt": True},
 ],
 "method": [
  {"ic": "Crush", "verb": "Crush the seeds — 1 min",
   "detail": "Lightly crush <b>1 tsp caraway seeds</b> with the back of a spoon — just cracked open, not powder.",
   "done": "seeds cracked, smelling warm and nutty.",
   "say": "Step 1. Lightly crush the caraway seeds with the back of a spoon. Just cracked, not powder."},
  {"ic": "Steep, covered", "verb": "Steep, covered — 10 min",
   "detail": "Pour over <b>1 cup just-boiled water</b>, cover, and steep.",
   "timer": [{"label": "Steep", "min": 10}],
   "done": "a pale golden tea.",
   "say": "Step 2. Pour just-boiled water over the seeds, cover, and let it steep."},
  {"ic": "Strain & take it up", "verb": "Strain, then take it to Mum",
   "detail": "Strain into her cup — <b>a little honey</b> only if Mum asked. Take it up warm.",
   "done": "a clear golden cup, on its way.",
   "say": "Step 3. Strain into the cup, honey only if Mum asked, and take it to her warm."},
 ],
 "overview_method": [
  "Crush the seeds.",
  "Cover &amp; steep — 10 min.",
  "Strain; honey if asked; take it up.",
 ],
 "nutri": [
  {"v": "Caffeine", "k": "none"},
  {"v": "Warm", "k": "after meals"},
  {"v": "Seeds", "k": "good for a 2nd steep"},
 ],
},

# ---------------------------------------------------------------- fennel
{
 "slug": "fennel-tea-card",
 "name": "Fennel Tea",
 "eyebrow": "Herbal tea <span class='dot'>·</span> Keep your milk flowing <span class='dot'>·</span> After meals",
 "sub": "A sweet, soothing seed tea — digestion first, milk by tradition.",
 "hero_alt": "A cup of pale golden fennel tea",
 "time": "about 10 min",
 "makes": "1 cup",
 "keep": "the seeds take a second steep",
 "when": "After meals. A cup or two a day is the sweet spot — not by the litre.",
 "why": [
  {"text": "Fennel — soothes digestion, eases bloating after meals", "chip": "t", "ev": "digest"},
  {"text": "THE classic milk tea — a tradition we label honestly", "chip": "t", "ev": "milk"},
  {"text": "Naturally sweet &amp; caffeine-free"},
 ],
 "bfnote": {"text": "A cup or two is lovely — not by the litre. Very heavy fennel/anise tea (over two litres a day) has twice been linked to sleepy, poorly-feeding newborns; normal cups are nowhere near that.", "ev": "bf"},
 "ev": {
  "digest": {"cls": "t", "chip": "tradition", "title": "Fennel — the after-dinner seed",
   "meaning": "Tradition, honestly labelled. Fennel seed tea is the classic gentle digestive across Mediterranean, Middle-Eastern and South-Asian kitchens — sweet, settling, brewed after meals for centuries.",
   "src": ["Traditional carminative use across Mediterranean &amp; South-Asian kitchens", LACTMED_FENNEL]},
  "milk": {"cls": "t", "chip": "tradition", "title": "Fennel as THE milk tea",
   "meaning": "Tradition, honestly labelled. Fennel is the most famous nursing tea there is — and the science stays modest: LactMed notes fennel does not measurably raise prolactin, and trials of milk herbs are small and mixed. So the label is tradition, and the cup still earns its place.",
   "src": [LACTMED_FENNEL, GAL_BFN]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Fennel while breastfeeding — the dose note",
   "meaning": "Breastfeeding note — a care flag, not a grade. Fennel tea in normal amounts (a cup or two a day) is a well-worn tradition. The flag: anethole, fennel's aromatic oil, was implicated when mothers drank MORE THAN 2 LITRES of strong fennel/anise tea daily — two newborns became drowsy and fed poorly, and recovered once the tea stopped. Cups, not litres.",
   "src": [LACTMED_FENNEL, DRUGS_FENNEL]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "fresh", "label": "crush the seeds just before", "small": "more of the sweet oils", "on": True},
   {"k": "honey", "label": "a little honey", "small": "if you fancy it", "on": False},
  ], "note": "Your cup only — and remember the house rule: cups, not litres."},
 "when_opts": {"label": "For", "opts": ["After lunch", "After dinner", "Anytime"], "sel": "After dinner"},
 "ings": [
  {"k": "seeds", "n": "Fennel seeds", "q": "1 tsp", "img": "img/fennel-tea-card/ing-01-fennel-seeds.jpg", "prep": "lightly crushed"},
  {"k": "water", "n": "Just-boiled water", "q": "1 cup", "img": "img/fennel-tea-card/ing-02-just-boiled-water.jpg"},
  {"k": "honey", "n": "Honey", "q": "a little", "img": "img/fennel-tea-card/ing-03-a-little-honey.jpg", "opt": True},
 ],
 "method": [
  {"ic": "Crush", "verb": "Crush the seeds — 1 min",
   "detail": "Lightly crush <b>1 tsp fennel seeds</b> with the back of a spoon — just cracked, not powder.",
   "done": "seeds cracked, smelling sweet like anise.",
   "say": "Step 1. Lightly crush the fennel seeds with the back of a spoon."},
  {"ic": "Steep, covered", "verb": "Steep, covered — 10 min",
   "detail": "Pour over <b>1 cup just-boiled water</b>, cover, and steep.",
   "timer": [{"label": "Steep", "min": 10}],
   "done": "a pale golden tea, sweet-smelling.",
   "say": "Step 2. Pour just-boiled water over the seeds, cover, and let it steep."},
  {"ic": "Strain & take it up", "verb": "Strain, then take it to Mum",
   "detail": "Strain into her cup — <b>honey</b> only if Mum asked. One or two cups a day is the house rule.",
   "done": "a clear, sweet cup on its way.",
   "say": "Step 3. Strain into the cup and take it to Mum warm."},
 ],
 "overview_method": [
  "Crush the seeds.",
  "Cover &amp; steep — 10 min.",
  "Strain; take it up warm.",
 ],
 "nutri": [
  {"v": "Caffeine", "k": "none"},
  {"v": "Sweet", "k": "naturally · no sugar"},
  {"v": "1–2 cups", "k": "a day — the dose note"},
 ],
},

# ---------------------------------------------------------------- ccf
{
 "slug": "ccf-tea",
 "name": "CCF Tea",
 "eyebrow": "Ayurvedic tea <span class='dot'>·</span> Heal your gut <span class='dot'>·</span> After meals",
 "sub": "Cumin, coriander &amp; fennel — the classic Ayurvedic digestive, kept warm in a flask.",
 "hero_alt": "A glass cup of pale CCF tea with whole seeds",
 "time": "about 10 min",
 "makes": "4 cups (a day flask)",
 "keep": "in a flask, warm, through the day",
 "when": "After meals or between them, warm — especially when you feel bloated.",
 "why": [
  {"text": "Cumin — the warming seed of the trio; traditionally eases gas &amp; sluggish digestion", "chip": "t", "ev": "trio"},
  {"text": "Coriander — the cooling balance", "chip": "t", "ev": "trio"},
  {"text": "Fennel — calms bloating; a traditional nursing seed", "chip": "t", "ev": "trio"},
  {"text": "Caffeine-free — hydration that counts toward your day"},
 ],
 "bfnote": {"text": "The fennel here is half a teaspoon across a whole flask — a food dose, fine while feeding. As with any seed tea: cups, not litres.", "ev": "bf"},
 "ev": {
  "trio": {"cls": "t", "chip": "tradition", "title": "CCF — the Ayurvedic digestive trio",
   "meaning": "Tradition, honestly labelled. Equal parts cumin, coriander and fennel is THE standard post-meal digestive tea of Ayurveda, and a fixture of its postpartum (42-day) kitchen. Kitchen-spice doses, centuries of use — not measured in modern trials, and we say so.",
   "src": [BANYAN, "Classical Ayurvedic kitchen practice — equal seeds, simmered and strained"]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "CCF while breastfeeding",
   "meaning": "Breastfeeding note — a care flag, not a grade. All three seeds are everyday kitchen spices at these doses (½ tsp each across 4 cups). The only flag worth carrying is fennel's litre-rule: normal cups are fine; don't brew it by the jug.",
   "src": [LACTMED_FENNEL, GAL_BFN]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "flask", "label": "flask it for the day", "small": "warm sips between feeds", "on": True},
   {"k": "ginger", "label": "2 slices fresh ginger in the pot", "small": "extra warmth", "on": False},
  ], "note": "The flask lives next to your feeding chair — that's the whole trick."},
 "when_opts": {"label": "For", "opts": ["The whole day", "After lunch", "After dinner"], "sel": "The whole day"},
 "ings": [
  {"k": "cumin", "n": "Cumin seeds", "q": "½ tsp", "img": "img/ccf-tea/ing-01-cumin-seeds.jpg"},
  {"k": "coriander", "n": "Coriander seeds", "q": "½ tsp", "img": "img/ccf-tea/ing-02-coriander-seeds.jpg"},
  {"k": "fennel", "n": "Fennel seeds", "q": "½ tsp", "img": "img/ccf-tea/ing-03-fennel-seeds.jpg"},
  {"k": "water", "n": "Filtered water", "q": "4 cups", "img": "img/ccf-tea/ing-04-filtered-water.jpg"},
 ],
 "method": [
  {"ic": "Measure", "verb": "Measure the seeds — 1 min",
   "detail": "<b>½ tsp each</b>: cumin, coriander, fennel — into a small pot.",
   "done": "three little heaps of seeds in the pot.",
   "say": "Step 1. Measure half a teaspoon each of cumin, coriander and fennel into the pot."},
  {"ic": "Simmer", "verb": "Boil, then simmer — 5 min",
   "detail": "Add <b>4 cups water</b>. Bring to a boil, then turn down and simmer gently.",
   "timer": [{"label": "Simmer", "min": 5}],
   "done": "pale golden water, seeds dancing.",
   "say": "Step 2. Add the water, bring to a boil, then simmer gently."},
  {"ic": "Strain & flask", "verb": "Strain into the flask",
   "detail": "Strain the seeds out and pour into <b>a flask</b>. Put it where Mum sits to feed — she sips it warm all day.",
   "done": "a full warm flask by Mum's chair.",
   "say": "Step 3. Strain the seeds out, fill the flask, and put it next to where Mum feeds the baby."},
 ],
 "overview_method": [
  "Measure the three seeds.",
  "Boil, then simmer — 5 min.",
  "Strain into a flask; keep it by Mum.",
 ],
 "nutri": [
  {"v": "Caffeine", "k": "none"},
  {"v": "Hydration", "k": "counts all day"},
  {"v": "Seeds", "k": "kitchen doses"},
 ],
 "nutri_label": "In this flask",
 "instr_note": "Made to its flask — nothing to scale. Your helper's card matches this one.",
},

# ---------------------------------------------------------------- masala chai
{
 "slug": "chai-tea",
 "name": "Masala Chai",
 "eyebrow": "Spiced chai <span class='dot'>·</span> Steady energy <span class='dot'>·</span> A morning treat",
 "sub": "Black tea simmered with whole spices and milk — the slow-morning cup.",
 "hero_alt": "A cup of milky masala chai with whole spices",
 "time": "about 10 min",
 "makes": "2 cups",
 "keep": "best fresh and hot",
 "when": "Morning or early afternoon — it carries caffeine, so keep it clear of bedtime and the last feeds of the day.",
 "why": [
  {"text": "Ginger, cardamom, cinnamon, cloves &amp; pepper — the warming masala, whole and simmered", "chip": "t", "ev": "masala"},
  {"text": "Milk — calcium &amp; protein riding in the cup", "chip": "rb", "ev": "milknutr"},
  {"text": "Black tea — a gentle, real lift (that's the caffeine, named honestly)"},
 ],
 "bfnote": {"text": "Caffeine passes into milk in small amounts. Up to about 300 mg a day is generally considered compatible with breastfeeding — a cup of this chai carries well under a coffee's worth. Tiny and premature babies clear caffeine slowly, so go gentler in the earliest weeks.", "ev": "bf"},
 "ev": {
  "masala": {"cls": "t", "chip": "tradition", "title": "The masala — warming spices",
   "meaning": "Tradition, honestly labelled. The chai masala — ginger, cardamom, cinnamon, cloves, black pepper — is South Asia's everyday warming blend, simmered whole for aroma and comfort. Warming and digestive framing is tradition, not a trial result.",
   "src": ["Traditional South-Asian kitchen practice — whole-spice masala chai", BANYAN]},
  "milknutr": {"cls": "rb", "chip": "research-backed", "title": "Milk — calcium &amp; protein",
   "meaning": "Research-backed on composition. Half a cup of milk in your chai carries measurable calcium and protein — small, real, and worth having while breastfeeding draws calcium from your stores.",
   "src": [USDA("milk, whole (nutrient data)"), ODS_CAL]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Caffeine while breastfeeding",
   "meaning": "Breastfeeding note — a care flag, not a grade. LactMed's read: a maternal intake around 300 mg/day (Europe suggests a more cautious 200 mg) appears compatible with breastfeeding for most full-term babies; preterm and very young newborns metabolise caffeine slowly. One morning chai sits well inside that — stacking it with coffees is what to watch.",
   "src": [LACTMED_CAFFEINE]},
 },
 "boost": {"label": "Make it yours", "items": [
   {"k": "half", "label": "half the tea", "small": "gentler lift, full flavour", "on": False},
   {"k": "nocaf", "label": "skip the tea leaves entirely", "small": "a caffeine-free spiced milk", "on": False},
   {"k": "honey", "label": "honey in the cup", "small": "sweet, off the heat", "on": True},
  ], "note": "The spices are the point — the tea is adjustable."},
 "when_opts": {"label": "For", "opts": ["Morning", "Early afternoon"], "sel": "Morning"},
 "ings": [
  {"k": "tea", "n": "Loose black tea", "q": "1 tsp", "img": "img/chai-tea/ing-01-loose-black-tea.jpg"},
  {"k": "water", "n": "Filtered water", "q": "1 cup", "img": "img/chai-tea/ing-02-filtered-water.jpg"},
  {"k": "milk", "n": "Milk of choice", "q": "½ cup", "img": "img/chai-tea/ing-03-milk-of-choice.jpg"},
  {"k": "ginger", "n": "Fresh ginger", "q": "3 slices", "img": "img/chai-tea/ing-04-fresh-ginger.jpg"},
  {"k": "cardamom", "n": "Cardamom pods", "q": "3", "img": "img/chai-tea/ing-05-cardamom.jpg"},
  {"k": "cinnamon", "n": "Ceylon cinnamon", "q": "1 stick", "img": "img/chai-tea/ing-06-ceylon-cinnamon.jpg"},
  {"k": "cloves", "n": "Cloves", "q": "3", "img": "img/chai-tea/ing-07-cloves.jpg"},
  {"k": "pepper", "n": "Black peppercorns", "q": "2", "img": "img/chai-tea/ing-08-black-peppercorns.jpg"},
 ],
 "method": [
  {"ic": "Crush the spices", "verb": "Crush the whole spices — 1 min",
   "detail": "Lightly crush the <b>cardamom pods, cloves, peppercorns</b> and <b>ginger</b> — just cracked open.",
   "done": "spices cracked, smelling loud already.",
   "say": "Step 1. Lightly crush the cardamom, cloves, peppercorns and ginger."},
  {"ic": "Simmer the spices", "verb": "Simmer the spices — 3 min",
   "detail": "Into <b>1 cup water</b> with the <b>cinnamon stick</b>. Boil, then simmer so the water takes the spice.",
   "timer": [{"label": "Simmer", "min": 3}],
   "done": "fragrant, lightly coloured water.",
   "say": "Step 2. Add the spices and cinnamon to the water. Boil, then simmer."},
  {"ic": "Tea & milk", "verb": "Tea in, milk in — 3 min",
   "detail": "Stir in <b>1 tsp black tea</b> and <b>½ cup milk</b>. Simmer gently to the colour Mum likes.",
   "timer": [{"label": "Simmer", "min": 3}],
   "cap": "Watch the pot — milk loves to boil over.",
   "done": "a warm caramel colour.",
   "say": "Step 3. Stir in the tea and the milk, and simmer gently. Watch the pot, milk boils over fast."},
  {"ic": "Strain & serve", "verb": "Strain, sweeten, take it up",
   "detail": "Strain into cups. <b>Honey</b> off the heat, only if Mum asked. Morning or early afternoon is its time.",
   "done": "two strained, steaming cups.",
   "say": "Step 4. Strain into cups, add honey if Mum asked, and take it to her."},
 ],
 "overview_method": [
  "Crush the whole spices.",
  "Simmer them in water — 3 min.",
  "Add tea &amp; milk — 3 min more.",
  "Strain; honey if asked.",
 ],
 "nutri": [
  {"v": "Caffeine", "k": "some · morning cup"},
  {"v": "Calcium", "k": "from the milk"},
  {"v": "Spices", "k": "whole &amp; warming"},
 ],
},
]
