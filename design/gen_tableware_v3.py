#!/usr/bin/env python3
"""Tableware v3 per Ilma (2026-07-10 late):
- GLASS LOCKED = optic wavy. 4 more styles of it (short stem, tall, small, jug),
  generated with her liked glass-3 image as the reference.
- CERAMICS: less flowery, more cool vintage (Parisian atelier / vintage ironstone,
  quiet luxury). 4 shape characters x plates / bowls / cups, hero plate as reference,
  satin rule everywhere.
16 images, sequential, 16s gaps."""
import base64
import json
import os
import subprocess
import time

S = os.path.dirname(os.path.abspath(__file__))
REF_PLATE = os.path.join(S, 'anchors', 'the-hero-plate.jpeg')
REF_GLASS = os.path.join(S, 'tableware2', 'glass-3-optic-wavy.jpg')
OUT = os.path.join(S, 'tableware3')
os.makedirs(OUT, exist_ok=True)
KEY = subprocess.check_output(
    ['security', 'find-generic-password', '-w', '-s', 'healing-kitchen-openai']).decode().strip()

STYLE = (" Editorial still-life photography in a bright Provencal farmhouse kitchen. Soft diffused"
         " morning window light, gentle shadows, crisp fresh airy feel. Rumpled natural oatmeal linen"
         " cloth on a pale stone surface. Styling sparse and uncluttered: one small loose posy of"
         " wildflowers in soft focus to the side; plenty of breathing room. Palette: warm paper-cream,"
         " muted sage green, soft honey-amber. Shallow depth of field, 50mm lens look, luxury in"
         " simplicity, photorealistic, no people, no hands, no text, no watermark, no food."
         " Framed close on the subject — it fills most of the frame.")

CER = ("Keep the glaze and mood of the reference photo: warm cream with a soft satin vintage glaze,"
       " never glossy, never new-looking — quiet-luxury cool vintage, like handmade Parisian atelier"
       " ceramics and old French ironstone. ")

SHAPES = {
    's1-scallop-sprigs': "with the gently lobed scalloped rim and the sparse hand-painted sage-green wildflower sprigs, exactly like the reference plate",
    's2-scallop-plain':  "with the gently lobed scalloped rim but completely PLAIN — no painted pattern at all, pure satin cream",
    's3-atelier-organic': "with a softly irregular, organic handmade rim (no scallops, no pattern), white-cream glaze with the faintest darker clay showing at the edge, Parisian atelier style",
    's4-embossed-rim':   "with a plain round rim carrying a delicate tone-on-tone EMBOSSED botanical line (raised in the clay, no paint)",
}
PIECES = [('plate', 'one dinner plate '), ('bowl', 'one wide soup bowl '), ('cup', 'one cup with a small handle ')]

CERAMICS = []
for pslug, pdesc in PIECES:
    for sslug, sdesc in SHAPES.items():
        CERAMICS.append((pslug + '-' + sslug, CER + 'Create ' + pdesc + sdesc + ', photographed alone.' + STYLE))

GL = ("Using the EXACT optic wavy vintage pressed-glass character of the glass in the reference"
      " photo — the same soft ripple, slightly irregular and old, never crystal-polished — create ")
GLASSES = [
    ('glass-stem',  GL + "the same glass on a SHORT STEM, a little goblet of water." + STYLE),
    ('glass-tall',  GL + "a TALL slim version, a highball glass of water." + STYLE),
    ('glass-small', GL + "a SMALL low version, a little juice glass of water." + STYLE),
    ('glass-jug',   GL + "a small JUG / carafe of water with the same optic wavy ripple." + STYLE),
]

def save(slug, raw):
    try:
        data = json.loads(raw)
    except Exception:
        print('BADJSON', slug, raw[:200]); return False
    if 'data' not in data:
        print('FAIL', slug, str(data)[:250]); return False
    png = base64.b64decode(data['data'][0]['b64_json'])
    open(os.path.join(OUT, slug + '.png'), 'wb').write(png)
    print('OK', slug, len(png) // 1024, 'KB', flush=True)
    return True

def call_edit(ref, prompt):
    return subprocess.run(['curl', '-s', 'https://api.openai.com/v1/images/edits',
                           '-H', 'Authorization: Bearer ' + KEY,
                           '-F', 'model=gpt-image-2-2026-04-21',
                           '-F', 'image[]=@' + ref,
                           '-F', 'prompt=' + prompt,
                           '-F', 'size=1024x1024', '-F', 'quality=high'],
                          capture_output=True, timeout=600).stdout

jobs = [(s, p, REF_PLATE) for s, p in CERAMICS] + [(s, p, REF_GLASS) for s, p in GLASSES]
print('jobs:', len(jobs), flush=True)
for slug, prompt, ref in jobs:
    for attempt in range(4):
        try:
            if save(slug, call_edit(ref, prompt)):
                break
        except Exception as e:
            print('ERR', slug, e, flush=True)
        time.sleep(30)
    time.sleep(16)
print('ALL DONE', flush=True)
