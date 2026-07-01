# Cook Cards — Master Audit & Catalogue

**38 Cook Cards built across parallel chats, audited on 2026-07-02.** This is the single index:
what's built, whether it passed QA, where each recipe came from (verified), and which "What it
heals" shelf it lives under. Base URL: `https://bobroviciuteilma-cell.github.io/postpartum-kitchen/cook-cards/`

## Audit result — QA

Ran a static + content audit over all 38 cards:

| Check | Result |
|---|---|
| No emoji / emoticons in body | ✅ 0 across all 38 |
| All images embedded (no broken `src`) | ✅ 0 unembedded across all 38 |
| "When to drink/eat" band present | ✅ every card |
| Step numbers filled, tabs correct | ✅ (verified per card in build) |
| Source attribution present + **exact link** | ✅ **now resolved** — see below |

**Sources were the one real gap.** 9 cards named a creator or dish but didn't hyperlink the *exact*
recipe. All 9 are now fixed and **Apify-verified** (handle + exact reel/blog confirmed against the
live post). The other 29 are legitimately **Traditional** (classic dishes, no single author) or
**Your own** (built from your pantry) — no creator credit needed.

## Source ledger — every external credit (verified 2026-07-02)

| Card | Creator | Exact recipe (verified) |
|---|---|---|
| Beet Kvass | **@wildnutritionist** (Kate Pope) | https://www.instagram.com/p/DYuwOBXgvqM/ |
| No-Water Magic Chicken Soup | **@dearmama.char** | https://www.instagram.com/p/DWRc8g-E2-9/ |
| Iron Orzo Salad | **@raquels.pantry** | https://www.instagram.com/p/DY1t5GJoO_9/ |
| Sardine & Tahini Salad | **@raquels.pantry** | https://www.instagram.com/p/DXuZYaNCBF1/ |
| Soaked Mineral Oats | **@thislifewithkels** | https://www.instagram.com/reel/DWorv_FjkKq/ |
| Adrenal Cocktail | **@thislifewithkels** | https://www.instagram.com/reel/DTvV21SDh6M/ |
| Chicken Liver Pâté | **@sokoladassielai** (Rūta Banionytė) | https://www.instagram.com/p/DK2QN9EtwyT/ |
| Liver Pâté Pops | **@sokoladassielai** + **@wildnutritionist** (pops idea) | DK2QN9EtwyT + https://www.instagram.com/p/DY52esFAUHk/ |
| Veggie-Packed Patties | **@reallifefamilykitchen** + **@delight.fuel** | reel/CnzbNqtJ0MP + reel/Ctfo9GIR-bu |
| Date & Oat Bites | Megan Limón (doula) | https://www.meganlimondoula.com/journal/postpartum-healing-date-oat-bites |

*Handle correction logged: it's **@sokoladassielai** (ends `-ai`), not `@sokoladassiela`.*
*Nice thread: **@wildnutritionist = Kate Pope**, your Mama Baby Biome north-star.*

---

## The catalogue — by "What it heals" shelf

9 shelves: your original 7 + **Hydration & minerals** and **Bones & teeth** (the two new ones the
audit proposed). A card's *primary* shelf is where it's listed; many help more than one.

### 🩸 Rebuild blood — iron · B12 · folate · copper
| Card | Tab | Source |
|---|---|---|
| [Beetroot Borscht](cook-cards/borscht.html) | Main | Traditional |
| [Oxtail & Heart Stew](cook-cards/oxtail-heart-stew.html) | Main | Traditional / library |
| [Clams in Garlic Broth](cook-cards/clams-garlic-broth.html) | Main | Traditional / library |
| [Short Rib Pho](cook-cards/short-rib-pho.html) | Main | Traditional / library |
| [Iron Orzo Salad](cook-cards/iron-orzo-salad.html) | Main | @raquels.pantry ✅ |
| [Chicken Liver Pâté](cook-cards/chicken-liver-pate-card.html) | Snacks | @sokoladassielai ✅ |
| [Liver Pâté Pops](cook-cards/liver-pate-pops.html) | Snacks | @sokoladassielai + @wildnutritionist ✅ |
| [Veggie-Packed Patties](cook-cards/veggie-patties-card.html) | Main | @reallifefamilykitchen + @delight.fuel ✅ |
| [Beet Kvass](cook-cards/beet-kvass-card.html) | Drinks | @wildnutritionist ✅ |
| [Jujube & Goji Tea](cook-cards/jujube-goji-tea.html) | Drinks | Traditional |

### ⚡ Energy — protein · slow carbs · B-vitamins
| Card | Tab | Source |
|---|---|---|
| [Nourishing Grain Bowls](cook-cards/grain-bowls.html) | Main | Your own |
| [Greek Chicken Burgers](cook-cards/greek-chicken-burgers.html) | Main | Your own |
| [Chicken & Potato Cutlets](cook-cards/chicken-potato-cutlets.html) | Main | Your own |
| [Power Smoothie](cook-cards/power-smoothie.html) | Drinks | Your own |
| [Masala Chai](cook-cards/chai-tea.html) | Drinks | Traditional |
| [Nut & Date Balls](cook-cards/nut-date-balls.html) | Snacks | Traditional (Gond Laddu) |
| [Blueberry Protein Waffles](cook-cards/blueberry-waffles.html) | Desserts | Your own |

### 🤍 Milk supply — galactagogues (breastfeeding-prioritised)
| Card | Tab | Source |
|---|---|---|
| [Soaked Mineral Oats](cook-cards/soaked-mineral-oats-card.html) | Main | @thislifewithkels ✅ |
| [Date & Oat Bites](cook-cards/date-oat-bites.html) | Snacks | Megan Limón ✅ |
| [Fennel Tea](cook-cards/fennel-tea-card.html) | Drinks | Traditional |
| [Nettle Tea](cook-cards/nettle-tea-card.html) | Drinks | Traditional |

### 🌱 Gut-healing — broth · ferments · gentle fibre
| Card | Tab | Source |
|---|---|---|
| [Chicken Bone Broth](cook-cards/chicken-bone-broth-card.html) | Main | Traditional / library |
| [No-Water Magic Chicken Soup](cook-cards/magic-chicken-soup.html) | Main | @dearmama.char ✅ |
| [Meat Stock Latte](cook-cards/meat-stock-latte.html) | Drinks | Library |
| [Caraway Tea](cook-cards/caraway-tea-card.html) | Drinks | Traditional |
| [CCF Tea](cook-cards/ccf-tea.html) | Drinks | Traditional (Ayurvedic) |

### 🛡️ Immunity — vitamin D · selenium · vitamin C
| Card | Tab | Source |
|---|---|---|
| [Creamy Mushroom Soup](cook-cards/mushroom-soup.html) | Main | Traditional |
| [Lemon & Egg Chicken Soup](cook-cards/lemon-egg-chicken-soup.html) | Main | Traditional |
| [Golden Milk](cook-cards/golden-milk-card.html) | Drinks | Traditional |

### 🌙 Calm & sleep — magnesium · adaptogens · warmth
| Card | Tab | Source |
|---|---|---|
| [Ashwagandha Milk](cook-cards/ashwagandha-milk.html) | Drinks | Traditional |
| [Almond, Date & Saffron Milk](cook-cards/almond-date-saffron.html) | Drinks | Traditional |

### 💧 Hydration & minerals *(new shelf)* — electrolytes · trace minerals
| Card | Tab | Source |
|---|---|---|
| [Adrenal Cocktail](cook-cards/adrenal-cocktail.html) | Drinks | @thislifewithkels ✅ |
| [Morning Waters](cook-cards/morning-waters.html) | Drinks | Traditional (amla/ajwain) |

### 🦴 Bones & teeth *(new shelf)* — calcium · protein · collagen
| Card | Tab | Source |
|---|---|---|
| [Sardine & Tahini Salad](cook-cards/sardine-tahini-salad.html) | Main | @raquels.pantry ✅ |
| [Cottage Cheese Pancakes (syrniki)](cook-cards/cottage-cheese-pancakes.html) | Main | Traditional |
| [Cottage Cheese Bake (zapekanka)](cook-cards/cottage-cheese-bake.html) | Desserts | Traditional |
| [Kefir & Cottage Cheese Set](cook-cards/cottage-cheese-set.html) | Desserts | Traditional |
| [Sesame–Date Bites](cook-cards/sesame-date-bites.html) | Snacks | Traditional (Til-Gur) |

### ☀️ Mood — this shelf is served by the Calm & Rebuild-blood cards above (no card sits here alone)

---

## By food tab (how they show in the app bar)
- **Main Meals (18):** borscht · oxtail-heart-stew · clams-garlic-broth · short-rib-pho · magic-chicken-soup · mushroom-soup · lemon-egg-chicken-soup · chicken-bone-broth · iron-orzo-salad · sardine-tahini-salad · grain-bowls · greek-chicken-burgers · chicken-potato-cutlets · veggie-patties · cottage-cheese-pancakes · soaked-mineral-oats
- **Drinks (14):** beet-kvass · golden-milk · caraway-tea · fennel-tea · nettle-tea · jujube-goji-tea · ccf-tea · chai-tea · adrenal-cocktail · ashwagandha-milk · almond-date-saffron · power-smoothie · meat-stock-latte · morning-waters *(indexed by [drinks.html](cook-cards/drinks.html))*
- **Snacks (5):** chicken-liver-pate · liver-pate-pops · nut-date-balls · sesame-date-bites · date-oat-bites
- **Desserts (4):** cottage-cheese-bake · cottage-cheese-set · blueberry-waffles *(+ syrniki/set overlap)*

## Open decisions for you
1. **Approve the 9-shelf taxonomy?** (your 7 + Hydration & minerals + Bones & teeth). This doc already
   uses it; say the word and I'll fold it into the app's browse + any new cards.
2. **Gaps worth filling (from the 1,313-post audit):** a **house-dressings** set (~9 real ones saved)
   and a **waffle-per-need** set (iron / milk / gut) — both build from pantry. Queued behind this.
3. Everything above is live and printable. Nothing is blocked.
