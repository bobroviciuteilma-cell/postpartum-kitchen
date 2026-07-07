# -*- coding: utf-8 -*-
"""Batch 2 — the tonic milks. Carries the two sensitive rewrites from
TAXONOMY-SYNERGY.md A.1: ashwagandha = the honest judgment-call copy (no 'safe',
no 'dangerous'; culinary pinch ≠ extract; thyroid + bed-sharing flags), and
golden milk drops the debunked '~20×' multiplier (mechanism kept, rb via
PMC5358025). Collagen wording softened to building-blocks (A.2)."""

from data_teas import USDA, ODS_CAL, BANYAN

PMC_CURCUMIN = '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5358025/" target="_blank" rel="noopener">PMC5358025 — curcumin bioavailability: piperine &amp; fat (review)</a>'
LACTMED_TURMERIC = '<a href="https://www.ncbi.nlm.nih.gov/books/NBK501846/" target="_blank" rel="noopener">LactMed (NIH) — Turmeric: food amounts</a>'
LACTMED_ASH = '<a href="https://www.ncbi.nlm.nih.gov/books/NBK501905/" target="_blank" rel="noopener">LactMed (NIH) — Ashwagandha</a>'
ELACT_ASH = '<a href="https://e-lactancia.org/breastfeeding/ashwagandha/product/" target="_blank" rel="noopener">e-lactancia — ashwagandha risk assessment</a>'
PP_THYROID = '<a href="https://www.ncbi.nlm.nih.gov/books/NBK557646/" target="_blank" rel="noopener">StatPearls (NIH) — postpartum thyroiditis (~5% of mothers, often silent)</a>'
ODS_VITE = '<a href="https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/" target="_blank" rel="noopener">NIH — Vitamin E fact sheet</a>'
PURUSHA = '<a href="https://www.purushaayurveda.com/articles/supporting-a-healthy-pregnancy-and-postpartum-with-dashamoola" target="_blank" rel="noopener">Purusha Ayurveda — dashamoola in pregnancy &amp; postpartum (traditional-use reference)</a>'
APOLLO_ARISHTA = '<a href="https://www.apollo247.com/health-topics/general-medical-consultation/dashmularishta-uses-benefits-and-side-effects" target="_blank" rel="noopener">Apollo 24/7 — Dashmularishta (the fermented form) contains self-generated alcohol</a>'

ASH_HONEST = ("Breastfeeding note — the honest picture, not a verdict. No study has shown ashwagandha harms a "
              "breastfed baby; none has shown it's safe either — nobody has measured whether it passes into milk, "
              "so the databases say 'avoid' mostly because the evidence box is empty. Dose and form are the crux: "
              "a culinary pinch of root in warm milk is a world away from a 300–600 mg standardised extract, which "
              "is where the two real cautions live — rare liver reactions, and thyroid stimulation (postpartum "
              "thyroiditis touches ~5% of mothers, often silently). Any thyroid history: clear it with your "
              "clinician first. Skip it if you're bed-sharing — it's mildly sedating. Our steer: an unknown, "
              "not a poison — start low, watch your baby.")

DRINKS = [

# ---------------------------------------------------------------- golden milk
{
 "slug": "golden-milk-card",
 "name": "Golden Milk",
 "eyebrow": "Tonic milk <span class='dot'>·</span> Calm &amp; lift your mood <span class='dot'>·</span> The golden cup",
 "sub": "A warm, soothing turmeric milk — the traditional golden cup, with collagen folded in for repair.",
 "hero_alt": "A golden cup of turmeric milk",
 "time": "about 5 min",
 "makes": "1 mug",
 "keep": "best fresh and warm",
 "when": "Daytime — with or after a meal. The ghee and black pepper are there to help the turmeric along.",
 "why": [
  {"text": "Turmeric — the classic golden anti-inflammatory cup, by long tradition", "chip": "t", "ev": "turmeric"},
  {"text": "Black pepper + ghee — help your body absorb the turmeric", "chip": "rb", "ev": "absorb"},
  {"text": "Collagen — a scoop of the building blocks your body uses to repair", "chip": "rb", "ev": "collagen"},
  {"text": "Ginger, cardamom &amp; cinnamon — warming and kind to digestion", "chip": "t", "ev": "spices"},
  {"text": "Caffeine-free — the cup to reach for instead of a second coffee"},
 ],
 "bfnote": {"text": "Turmeric as a kitchen spice — a spoonful in a warm cup — is considered fine while feeding. It's concentrated curcumin supplements that sit outside kitchen territory.", "ev": "bf"},
 "ev": {
  "turmeric": {"cls": "t", "chip": "tradition", "title": "Turmeric — the golden cup",
   "meaning": "Tradition, honestly labelled. Golden milk (haldi doodh) is South Asia's everyday healing cup, and turmeric's anti-inflammatory reputation at supplement doses has real research behind it. At a cosy ½ tsp in milk, we call it what it is: a warming tradition worth keeping.",
   "src": ["Traditional South-Asian practice — haldi doodh, the everyday golden milk", LACTMED_TURMERIC]},
  "absorb": {"cls": "rb", "chip": "research-backed", "title": "Black pepper + fat — the absorption pair",
   "meaning": "Research-backed mechanism. Curcumin on its own is poorly absorbed; piperine (black pepper) and dietary fat measurably improve its uptake. That's why the pepper and ghee are in the recipe — no exaggerated multipliers, just the mechanism.",
   "src": [PMC_CURCUMIN]},
  "collagen": {"cls": "rb", "chip": "research-backed", "title": "Collagen — building blocks for repair",
   "meaning": "Research-backed on composition. A collagen scoop is measurable protein rich in glycine and proline — amino acids your body uses in tissue repair. Whether extra collagen speeds specific repairs is still early-stage science, so we claim the building blocks, not the outcome.",
   "src": [USDA("collagen peptides (protein &amp; amino-acid data)")]},
  "spices": {"cls": "t", "chip": "tradition", "title": "The warming spices",
   "meaning": "Tradition, honestly labelled. Ginger, cardamom and cinnamon are the warming, digestion-friendly trio of the traditional cup. (We don't carry a blood-sugar claim for cinnamon — human evidence is mixed.)",
   "src": ["Traditional warming-spice practice across South-Asian kitchens", BANYAN]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Turmeric while breastfeeding",
   "meaning": "Breastfeeding note — a care flag, not a grade. Kitchen amounts of turmeric are considered compatible with breastfeeding. High-dose curcumin supplements are a different thing and haven't been studied in nursing mothers — stay at food doses, which this cup is.",
   "src": [LACTMED_TURMERIC]},
  "ashboost": {"cls": "b", "chip": "breastfeeding note", "title": "The evening ashwagandha pinch — the honest picture",
   "meaning": ASH_HONEST,
   "src": [LACTMED_ASH, ELACT_ASH, PP_THYROID]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "saffron", "label": "a few saffron threads", "small": "the calming tradition", "on": True},
   {"k": "honey", "label": "honey, off the heat", "small": "to taste", "on": True},
   {"k": "ash", "label": "an evening pinch of ashwagandha", "small": "an unknown, not a poison — read its note first", "on": False},
  ], "note": "Your cup only. The ashwagandha pinch carries its own honest note — the beet-pink label on the bedtime card."},
 "when_opts": {"label": "For", "opts": ["Mid-morning", "Afternoon", "Early evening"], "sel": "Afternoon"},
 "ings": [
  {"k": "milk", "n": "Milk of choice", "q": "1 cup", "img": "img/golden-milk-card/ing-01-milk-of-choice.jpg"},
  {"k": "turmeric", "n": "Turmeric", "q": "½ tsp", "img": "img/golden-milk-card/ing-02-turmeric.jpg"},
  {"k": "ginger", "n": "Ginger", "q": "½ tsp", "img": "img/golden-milk-card/ing-03-ginger.jpg", "prep": "or a thumb, grated"},
  {"k": "pepper", "n": "Black pepper", "q": "a good pinch", "img": "img/golden-milk-card/ing-04-black-pepper.jpg"},
  {"k": "cinnamon", "n": "Ceylon cinnamon", "q": "a pinch", "img": "img/golden-milk-card/ing-05-ceylon-cinnamon.jpg"},
  {"k": "cardamom", "n": "Cardamom", "q": "a pinch", "img": "img/golden-milk-card/ing-06-cardamom.jpg"},
  {"k": "ghee", "n": "Ghee", "q": "1 tsp", "img": "img/golden-milk-card/ing-07-ghee.jpg", "prep": "the absorption fat"},
  {"k": "collagen", "n": "Collagen", "q": "1 scoop", "img": "img/golden-milk-card/ing-08-collagen.jpg", "prep": "in off the heat"},
 ],
 "method": [
  {"ic": "Warm the milk", "verb": "Warm the milk — gently",
   "detail": "Warm <b>1 cup milk</b> in a small pot — steaming, <b>not boiling</b>.",
   "done": "wisps of steam, no bubbles.",
   "say": "Step 1. Gently warm the milk in a small pot. Steaming, not boiling."},
  {"ic": "Whisk in the spices", "verb": "Spices in — simmer 3 min",
   "detail": "Whisk in the <b>turmeric, ginger, cinnamon, cardamom</b>, a good pinch of <b>black pepper</b> and the <b>ghee</b>. Keep it at the gentlest simmer.",
   "timer": [{"label": "Simmer", "min": 3}],
   "done": "an even golden colour, smelling warm.",
   "say": "Step 2. Whisk in the spices, the pepper and the ghee, and keep it at the gentlest simmer."},
  {"ic": "Collagen, off the heat", "verb": "Off the heat — collagen in",
   "detail": "Take the pot <b>off the heat</b>, then whisk in the <b>collagen scoop</b> (and honey, if Mum asked) until smooth.",
   "done": "smooth, golden, no clumps.",
   "say": "Step 3. Take the pot off the heat, then whisk in the collagen until smooth."},
 ],
 "overview_method": [
  "Warm the milk — not boiling.",
  "Whisk in spices + ghee; simmer 3 min.",
  "Off the heat: collagen (+ honey).",
 ],
 "nutri": [
  {"v": "Collagen", "k": "a scoop · repair blocks"},
  {"v": "Caffeine", "k": "none"},
  {"v": "Golden", "k": "pepper + ghee carry it"},
 ],
},

# ---------------------------------------------------------------- almond date saffron
{
 "slug": "almond-date-saffron",
 "name": "Almond, Date & Saffron Milk",
 "eyebrow": "Nourishing milk <span class='dot'>·</span> Calm &amp; lift your mood <span class='dot'>·</span> Restoring",
 "sub": "A creamy, golden milk of soaked almonds, dates and saffron — rich, restoring, lightly sweet.",
 "hero_alt": "A creamy glass of almond, date and saffron milk",
 "time": "about 10 min",
 "makes": "1 large mug",
 "keep": "best fresh",
 "when": "Daytime or early evening — a rich cup between meals, or instead of dessert.",
 "why": [
  {"text": "Almonds — protein, good fats &amp; vitamin E", "chip": "rb", "ev": "almonds"},
  {"text": "Saffron — the classic warming, mood-lifting thread of the postpartum kitchen", "chip": "t", "ev": "saffron"},
  {"text": "Dates — all the sweetness this cup needs, the whole-food way"},
  {"text": "Cardamom — aromatic and kind to digestion", "chip": "t", "ev": "saffron"},
 ],
 "bfnote": {"text": "A pinch of saffron is the right amount — culinary saffron is a food. Megadose saffron supplements are a different thing; this cup stays in the kitchen.", "ev": "bf"},
 "ev": {
  "almonds": {"cls": "rb", "chip": "research-backed", "title": "Almonds — protein, fats &amp; vitamin E",
   "meaning": "Research-backed on composition. Almonds measurably carry protein, monounsaturated fats and vitamin E — a genuinely nourishing base for a milk, soaked so they blend silky.",
   "src": [USDA("almonds (nutrient data)"), ODS_VITE]},
  "saffron": {"cls": "t", "chip": "tradition", "title": "Saffron &amp; cardamom — the restoring pair",
   "meaning": "Tradition, honestly labelled. Saffron milk is the celebratory restoring cup across South-Asian and Persian postpartum kitchens — warming, golden, given to new mothers for mood and strength. A lovely tradition we label as one.",
   "src": ["Traditional South-Asian &amp; Persian postpartum practice — saffron milk for new mothers", BANYAN]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Saffron while breastfeeding",
   "meaning": "Breastfeeding note — a care flag, not a grade. A culinary pinch of saffron in warm milk is a normal food use and fine while feeding. Concentrated saffron supplements are the thing to leave alone — the kitchen pinch is the dose.",
   "src": ["Culinary-dose principle — food amounts, not supplement doses, while nursing"]},
 },
 "boost": {"label": "Make it PP Gold (for yourself)", "items": [
   {"k": "ghee", "label": "1 tsp ghee in the warm milk", "small": "richer, the classic way", "on": False},
   {"k": "extra-date", "label": "a third date", "small": "sweeter still", "on": False},
   {"k": "coconut", "label": "a splash of coconut milk", "small": "silkier", "on": False},
  ], "note": "This cup is already a treat — the boosts just take it further."},
 "when_opts": {"label": "For", "opts": ["Mid-morning", "Afternoon", "Early evening"], "sel": "Early evening"},
 "ings": [
  {"k": "almonds", "n": "Almonds", "q": "8, soaked", "img": "img/almond-date-saffron/ing-01-almonds.jpg", "prep": "skins slipped off"},
  {"k": "dates", "n": "Medjool dates", "q": "2, pitted", "img": "img/almond-date-saffron/ing-02-medjool-dates.jpg"},
  {"k": "saffron", "n": "Saffron threads", "q": "a pinch", "img": "img/almond-date-saffron/ing-03-saffron-threads.jpg"},
  {"k": "cardamom", "n": "Cardamom", "q": "a pinch", "img": "img/almond-date-saffron/ing-04-cardamom.jpg"},
  {"k": "milk", "n": "Milk of choice", "q": "1 cup", "img": "img/almond-date-saffron/ing-05-milk-of-choice.jpg"},
 ],
 "method": [
  {"ic": "Soak", "verb": "Soak the almonds — 10 min hot",
   "detail": "Soak <b>8 almonds</b> in hot water for <b>10 min</b> (or overnight, if planned ahead), then slip the skins off.",
   "timer": [{"label": "Soak", "min": 10}],
   "done": "pale, naked almonds.",
   "say": "Step 1. Soak the almonds in hot water, then slip off the skins."},
  {"ic": "Blend", "verb": "Blend it silky — 1 min",
   "detail": "Blend the <b>almonds</b>, <b>2 dates</b>, the <b>cardamom</b> and <b>1 cup milk</b> until completely smooth.",
   "done": "creamy, no bits.",
   "say": "Step 2. Blend the almonds, dates, cardamom and milk until completely smooth."},
  {"ic": "Warm with saffron", "verb": "Warm it golden — 2 min",
   "detail": "Pour into a small pot, warm gently, and crumble in <b>a pinch of saffron</b>. Let it sit 2 min so the gold spreads.",
   "timer": [{"label": "Steep", "min": 2}],
   "done": "cream turning gold in threads.",
   "say": "Step 3. Warm it gently, crumble in the saffron, and give the gold a couple of minutes to spread."},
 ],
 "overview_method": [
  "Soak 10 min; skins off.",
  "Blend almonds, dates, cardamom, milk.",
  "Warm; saffron in; 2 min to turn gold.",
 ],
 "nutri": [
  {"v": "Protein", "k": "almonds · food-level"},
  {"v": "Sweet", "k": "dates only · no sugar"},
  {"v": "Caffeine", "k": "none"},
 ],
},

# ---------------------------------------------------------------- ashwagandha milk
{
 "slug": "ashwagandha-milk",
 "name": "Ashwagandha Milk",
 "eyebrow": "Moon milk <span class='dot'>·</span> Calm &amp; lift your mood <span class='dot'>·</span> Bedtime",
 "sub": "A warm, spiced moon milk for the wired-but-tired evenings — with the honest read on its famous root.",
 "hero_alt": "A warm mug of spiced ashwagandha moon milk",
 "time": "about 5 min",
 "makes": "1 mug",
 "keep": "best fresh, before bed",
 "when": "Evening, 30–60 min before bed — after the last feed is the classic slot.",
 "why": [
  {"text": "Ashwagandha — Ayurveda's rejuvenating root, taken in warm milk for centuries", "chip": "t", "ev": "ash"},
  {"text": "Warm milk — calcium &amp; protein, and the ritual itself settles", "chip": "rb", "ev": "milknutr"},
  {"text": "Cinnamon &amp; cardamom — the warming bedtime spices", "chip": "t", "ev": "ash"},
  {"text": "Caffeine-free — a true wind-down cup"},
 ],
 "bfnote": {"text": "This is the one card where the honest answer is genuinely 'we don't know'. Read the full picture before you make it a nightly habit — culinary pinch versus extract is the whole question.", "linktext": "Read the honest ashwagandha note", "ev": "bf"},
 "ev": {
  "ash": {"cls": "t", "chip": "tradition", "title": "Ashwagandha — the rejuvenating root",
   "meaning": "Tradition, honestly labelled. Ayurveda has given ashwagandha in warm milk with ghee as a postpartum rejuvenating tonic for centuries — for exactly the exhausted-but-wired state new mothers know. Modern stress-relief trials used standardised extracts, not the culinary pinch — so on this card, the label is tradition.",
   "src": ["Classical Ayurvedic practice — ashwagandha in warm milk as a postpartum rasayana", BANYAN]},
  "milknutr": {"cls": "rb", "chip": "research-backed", "title": "Warm milk — calcium &amp; protein",
   "meaning": "Research-backed on composition. A cup of milk carries measurable calcium and protein — worth having daily while breastfeeding draws calcium from your stores.",
   "src": [USDA("milk, whole (nutrient data)"), ODS_CAL]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Ashwagandha while breastfeeding — the honest picture",
   "meaning": ASH_HONEST,
   "src": [LACTMED_ASH, ELACT_ASH, PP_THYROID]},
 },
 "boost": {"label": "Your instructions for tonight", "items": [
   {"k": "low", "label": "start at ¼ tsp", "small": "start low, watch your baby", "on": True},
   {"k": "ghee", "label": "1 tsp ghee", "small": "the classical carrier", "on": True},
   {"k": "skip", "label": "skip the root tonight — keep the spiced milk", "small": "still a lovely cup", "on": False},
  ], "note": "Not while bed-sharing, and clear it with your clinician if you have any thyroid history — the honest note above has the sources."},
 "when_opts": {"label": "For", "opts": ["After the last feed", "An hour before bed"], "sel": "After the last feed"},
 "ings": [
  {"k": "milk", "n": "Milk of choice", "q": "1 cup", "img": "img/ashwagandha-milk/ing-01-milk-of-choice.jpg"},
  {"k": "ash", "n": "Ashwagandha powder", "q": "¼–½ tsp", "img": "img/ashwagandha-milk/ing-02-ashwagandha-powder.jpg", "prep": "a culinary pinch, not an extract"},
  {"k": "cinnamon", "n": "Ceylon cinnamon", "q": "a pinch", "img": "img/ashwagandha-milk/ing-03-ceylon-cinnamon.jpg"},
  {"k": "cardamom", "n": "Cardamom", "q": "a pinch", "img": "img/ashwagandha-milk/ing-04-cardamom.jpg"},
  {"k": "honey", "n": "Honey", "q": "1 tsp", "img": "img/ashwagandha-milk/ing-05-honey.jpg", "opt": True},
  {"k": "ghee", "n": "Ghee", "q": "1 tsp", "img": "img/ashwagandha-milk/ing-06-ghee.jpg", "opt": True},
 ],
 "method": [
  {"ic": "Warm the milk", "verb": "Warm the milk — gently",
   "detail": "Warm <b>1 cup milk</b> in a small pot — steaming, <b>not boiling</b>.",
   "done": "wisps of steam, no bubbles.",
   "say": "Step 1. Gently warm the milk. Steaming, not boiling."},
  {"ic": "Whisk in", "verb": "Whisk in the root &amp; spices — 3 min",
   "detail": "Whisk in the <b>ashwagandha</b> (start at <b>¼ tsp</b> — Mum's card says how much tonight), the <b>cinnamon, cardamom</b> and <b>ghee</b>. Simmer at the gentlest bubble.",
   "timer": [{"label": "Simmer", "min": 3}],
   "warn": {"b": "The amount matters.", "text": "This is a kitchen pinch of the root, not a supplement dose. Use what Mum's card says — no heaping."},
   "done": "smooth, warm-spiced, faintly earthy.",
   "say": "Step 2. Whisk in the powder Mum asked for, with the spices and ghee, and simmer at the gentlest bubble."},
  {"ic": "Sweeten & take it up", "verb": "Off the heat — honey, then up to Mum",
   "detail": "Off the heat, stir in <b>honey</b> if Mum asked. Take it to her warm, 30–60 min before her sleep.",
   "done": "a warm mug on its way to bed.",
   "say": "Step 3. Off the heat, stir in honey if Mum asked, and take it to her warm."},
 ],
 "overview_method": [
  "Warm the milk — not boiling.",
  "Whisk in the pinch of root + spices; 3 min.",
  "Honey off the heat; take it up.",
 ],
 "nutri": [
  {"v": "Caffeine", "k": "none"},
  {"v": "Calcium", "k": "from the milk"},
  {"v": "¼–½ tsp", "k": "culinary, not extract"},
 ],
},

# ---------------------------------------------------------------- dashamoola
{
 "slug": "dashamoola-decoction",
 "name": "Dashamoola Bedtime Decoction",
 "eyebrow": "Ten-root tonic <span class='dot'>·</span> Calm &amp; lift your mood <span class='dot'>·</span> The 42-day window",
 "sub": "The classic ten-root Ayurvedic postpartum tonic — simmered small, taken warm in the evening. Tradition, honestly labelled.",
 "hero_alt": "A small cup of dark dashamoola decoction",
 "time": "about 15 min",
 "makes": "1 small cup (30–60 ml)",
 "keep": "make it fresh each time",
 "when": "Evening, after the last feed — a small warm cup, once or twice a day at most.",
 "why": [
  {"text": "Ten roots — THE classic Ayurvedic formula for the 42-day postpartum window", "chip": "t", "ev": "dash"},
  {"text": "Vata-settling — traditionally taken to ground a wired-but-tired nervous system", "chip": "t", "ev": "dash"},
  {"text": "Warm milk &amp; ghee — the classical evening carrier for the bitter roots", "chip": "t", "ev": "dash"},
  {"text": "A cordial-sized cup — kitchen dose, not a megadose"},
 ],
 "bfnote": {"text": "You bought the powder — that's the right form while nursing. The common bottled form, Dashmularishta, is fermented and carries self-generated alcohol; your powder decoction doesn't.", "ev": "bf"},
 "ev": {
  "dash": {"cls": "t", "chip": "tradition", "title": "Dashamoola — the ten-root postpartum formula",
   "meaning": "Tradition, honestly labelled — and this one is genuinely core canon: unlike most herbs, dashamoola is specifically a postpartum formula, given through the 42-day window for strength, aches and a frayed nervous system. Its own literature says it plainly: the safety profile has not been established in modern clinical studies. Centuries of use, no trials — so every line on this card is tradition, and no milk-supply claim is made.",
   "src": [PURUSHA, "Classical Ayurvedic postpartum canon — the 42-day (sutika) window"]},
  "bf": {"cls": "b", "chip": "breastfeeding note", "title": "Powder, not the arishta",
   "meaning": "Breastfeeding note — a care flag, not a grade. Dashamoola the powder, simmered into a small decoction, is the traditional nursing-window form with no reported harms in centuries of use (and no modern studies — we say that plainly). The flag is the FORM: Dashmularishta, the common bottled preparation, is fermented and contains self-generated alcohol — not for now. Your jar is the powder. Keep it that way.",
   "src": [APOLLO_ARISHTA, PURUSHA]},
 },
 "boost": {"label": "Make it bedtime (for yourself)", "items": [
   {"k": "milk", "label": "top with ½ cup warm milk", "small": "the classic evening way", "on": True},
   {"k": "ghee", "label": "½ tsp ghee", "small": "the classical carrier", "on": True},
   {"k": "honey", "label": "1 tsp honey, off the heat", "small": "softens the bitterness", "on": True},
  ], "note": "The dose is the small cup itself — 30–60 ml, once or twice a day, made fresh."},
 "when_opts": {"label": "For", "opts": ["After the last feed", "Early evening"], "sel": "After the last feed"},
 "ings": [
  {"k": "powder", "n": "Dashamoola powder", "q": "1–2 tsp", "img": "img/dashamoola-decoction/ing-01-dashamoola-powder.jpg", "prep": "the powder, not the arishta"},
  {"k": "water", "n": "Water", "q": "½ cup / 120 ml", "img": "img/dashamoola-decoction/ing-02-water.jpg"},
  {"k": "milk", "n": "Warm milk", "q": "½ cup", "img": "img/dashamoola-decoction/ing-03-warm-milk.jpg", "opt": True},
  {"k": "ghee", "n": "Ghee", "q": "½ tsp", "img": "img/dashamoola-decoction/ing-04-ghee.jpg", "opt": True},
  {"k": "honey", "n": "Honey", "q": "1 tsp", "img": "img/dashamoola-decoction/ing-05-honey.jpg", "opt": True, "prep": "off the heat"},
 ],
 "method": [
  {"ic": "Simmer down", "verb": "Simmer it small — 10–12 min",
   "detail": "Stir <b>1–2 tsp dashamoola powder</b> into <b>120 ml water</b> in the smallest pan. Simmer gently, uncovered, until it reduces by about half.",
   "timer": [{"label": "Simmer", "min": 11}],
   "done": "a dark liquid, half what you started with.",
   "say": "Step 1. Stir the powder into the water in a small pan, and simmer gently until it reduces by about half."},
  {"ic": "Strain small", "verb": "Strain — a cordial-sized cup",
   "detail": "Strain through a fine sieve into a small cup: <b>30–60 ml</b> of dark decoction. That little cup <b>is</b> the dose — once or twice a day, no more.",
   "warn": {"b": "Small is the point.", "text": "A cordial-sized pour, made fresh each time — never a mug of it."},
   "done": "a small, dark, cordial-sized cup.",
   "say": "Step 2. Strain into a small cup. That cordial-sized pour is the dose."},
  {"ic": "Make it bedtime", "verb": "Milk, ghee &amp; honey — if asked",
   "detail": "If Mum asked: top with <b>½ cup warm milk</b> and <b>½ tsp ghee</b>; stir in <b>honey off the heat</b>.",
   "done": "a warm, milky evening cup.",
   "say": "Step 3. If Mum asked, top it with warm milk and ghee, and stir in honey off the heat."},
  {"ic": "Take it up", "verb": "Warm, after the last feed",
   "detail": "Take it to Mum warm, after the last feed of the evening.",
   "done": "Mum settled, small cup in hand.",
   "say": "Step 4. Take it to Mum warm, after the last feed of the evening."},
 ],
 "overview_method": [
  "Simmer the powder in water — reduce by half.",
  "Strain small: 30–60 ml is the dose.",
  "Warm milk, ghee, honey — if asked.",
  "Up to Mum, after the last feed.",
 ],
 "nutri": [
  {"v": "30–60 ml", "k": "the whole dose"},
  {"v": "Caffeine", "k": "none"},
  {"v": "Alcohol", "k": "none · powder form"},
 ],
 "nutri_label": "In this small cup",
 "instr_note": "Made to its small cup — the 30–60 ml pour IS the measure. Nothing to scale.",
},
]
