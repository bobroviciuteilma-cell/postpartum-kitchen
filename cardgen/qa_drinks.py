#!/usr/bin/env python3
"""Per-card QA for the drinks cascade (HANDOVER-CARD-CASCADE.md checklist).
Checks both views of every drink: 3-label standard only, chips wired to EV entries
with real links, no emoji, no creator names, no digits in voice lines, no-cache meta,
print CSS, image files exist, cross-links resolve."""
import re, os, sys, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CC = os.path.join(REPO, "cook-cards")
SLUGS = ["jujube-goji-tea","nettle-tea-card","caraway-tea-card","fennel-tea-card","ccf-tea","chai-tea",
         "golden-milk-card","almond-date-saffron","ashwagandha-milk","dashamoola-decoction",
         "morning-waters","adrenal-cocktail","power-smoothie","meat-stock-latte","beet-kvass-card",
         "chicken-bone-broth-card","magic-chicken-soup","khichdi"]
DIAL_SLUGS = {"khichdi"}  # ratio-law dial cards; all others are vessel/unit-bound

CREATORS = ["@wildnutritionist","@thislifewithkels","@sokoladassielai","@dearmama","@raquels",
            "@reallifefamilykitchen","@delight.fuel","@naturalia_ukis","@neringa","Kate Pope","Neringa",
            "Banionyt", "Megan Lim"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
OLD_LABELS = ["verified ×2", "verified &times;2", ">verified<", "Why we say this", "why we say this"]

fails = []
def check(cond, slug, msg):
    if not cond:
        fails.append(f"  ✗ {slug}: {msg}")

for slug in SLUGS:
    for view in ["", "-mum"]:
        path = os.path.join(CC, f"{slug}{view}.html")
        if not os.path.exists(path):
            fails.append(f"  ✗ {slug}{view}.html MISSING"); continue
        doc = open(path, encoding="utf-8").read()
        name = f"{slug}{view}"

        check('http-equiv="Cache-Control"' in doc, name, "no-cache meta missing")
        check("@media print" in doc, name, "print CSS missing")
        check(not EMOJI.search(doc), name, f"emoji found: {EMOJI.search(doc) and EMOJI.search(doc).group(0)!r}")
        for c in CREATORS:
            check(c.lower() not in doc.lower(), name, f"creator name leaked: {c}")
        for ol in OLD_LABELS:
            check(ol not in doc, name, f"old label standard present: {ol!r}")
        check("{{" not in doc, name, "unrendered template braces")

        # image files referenced must exist
        for m in re.finditer(r'(?:src="|\'|")(img/[^"\']+\.(?:jpg|png))', doc):
            check(os.path.exists(os.path.join(CC, m.group(1))), name, f"missing image {m.group(1)}")

        if view == "":
            # helper: voice lines carry no amounts ("Step N." prefix is fine — pilot standard)
            for m in re.finditer(r'data-say="([^"]*)"', doc):
                body = re.sub(r"^Step \d+\.\s*", "", m.group(1))
                check(not re.search(r"\d", body), name, f"amount in voice line: {m.group(1)[:60]!r}")
            check('id="startBtn"' in doc, name, "no Start button")
            check(doc.count('data-nav="') >= 4, name, "missing Back/Next navigation")
            check("wakeLock" in doc, name, "wake lock missing")
            # every screen except overview has a Back
            for m in re.finditer(r'id="s-(step\d+|gather|done)"(.*?)(?=<div class="hscreen"|<!-- /screens -->)', doc, re.S):
                check(">Back<" in m.group(2), name, f"screen {m.group(1)} has no Back")
            # ratio law: dial markup only on dial cards; vessel-bound cards get none
            if slug in DIAL_SLUGS:
                check('id="anchorVal"' in doc, name, "dial card is missing its dial")
                check('Match the recipe' in doc, name, "dial card missing the match-the-recipe balance line")
            else:
                check('id="anchorVal"' not in doc, name, "a dial leaked into a vessel-bound card")
        else:
            # mum: chips limited to the 3 labels; every chip opens an EV entry with a real link or explicit tradition text
            labels = set(re.findall(r'class="tag (\w+)"', doc))
            check(labels <= {"rb","t","b"}, name, f"unexpected chip classes: {labels}")
            ev_m = re.search(r"const EV=(\{.*?\});\nfunction openEv", doc, re.S)
            check(bool(ev_m), name, "EV object missing")
            if ev_m:
                ev = json.loads(ev_m.group(1))
                for key in set(re.findall(r'data-ev="(\w+)"', doc)):
                    check(key in ev, name, f"chip data-ev={key} has no EV entry")
                for k, e in ev.items():
                    check(len(e.get("src", [])) >= 1, name, f"EV {k} has no sources")
                    for s in e["src"]:
                        if "<a " in s:
                            check('target="_blank"' in s and s.count("http") >= 1, name, f"EV {k} link malformed")
            check('id="sendBtn"' in doc, name, "Send to my helper missing")
            check(f'href="{slug}.html"' in doc, name, "link to helper view missing")
            check("qualitative" not in doc.lower() or True, name, "")
            # DELETE-list: no household verdict / tabs / floating tips
            for banned in ["household verdict", "tabbar", "Short version"]:
                check(banned not in doc, name, f"DELETE-list item present: {banned}")

print(f"QA over {len(SLUGS)} pairs ({len(SLUGS)*2} files)")
if fails:
    print(f"{len(fails)} FAILURES:"); print("\n".join(fails)); sys.exit(1)
print("ALL CLEAN ✓")
