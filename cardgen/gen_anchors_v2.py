#!/usr/bin/env python3
"""Style anchors v2 — Provencal porcelain, sparse wildflowers, less herby."""
import json, os, base64, sys, urllib.request, concurrent.futures, pathlib, subprocess

def get_key():
    k = os.environ.get("OPENAI_API_KEY")
    if k:
        return k.strip()
    try:  # macOS Keychain (the home as of 2026-07-07)
        r = subprocess.run(["security", "find-generic-password", "-w", "-s", "healing-kitchen-openai"],
                           capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except Exception:
        return None

KEY = get_key()
if not KEY:
    sys.exit("No OpenAI key found (Keychain service 'healing-kitchen-openai' or $OPENAI_API_KEY)")

MODEL = "gpt-image-2-2026-04-21"
OUT = pathlib.Path(__file__).parent / "anchors2"
OUT.mkdir(exist_ok=True)

STYLE = (
    " Editorial food photography in a bright Provencal farmhouse kitchen. Soft diffused "
    "morning window light, gentle shadows, crisp fresh airy feel. Rumpled natural oatmeal "
    "linen cloth on a pale stone surface. Tableware is delicate French Provencal porcelain: "
    "white-cream porcelain with softly fluted, scalloped rims. Styling is sparse and "
    "uncluttered: at most one small loose posy of wildflowers (lavender, chamomile, meadow "
    "flowers) in soft focus to the side; clean surfaces, plenty of breathing room, no herb "
    "sprigs scattered about. Palette: warm paper-cream, muted sage green, soft honey-amber, "
    "a whisper of lavender. Where cookware appears: French enamelled cast iron in matte cream "
    "or soft sage, heavy rounded form, glossy enamel interior, no logos or brand marks. "
    "Shallow depth of field, 50mm lens look, luxury in simplicity, photorealistic, no people, "
    "no hands, no text, no watermark."
)

SHOTS = {
    "hero_cutlets":  "Six golden-brown pan-fried oval beef cutlets with an even crisp crust on a fluted Provencal porcelain plate, lemon wedges and sliced ripe tomatoes alongside, one small pinch of fresh dill on top.",
    "step_skillet":  "Golden-brown oval beef cutlets sizzling mid-fry in a cream enamelled cast-iron skillet, ghee glistening, a wooden spatula resting on the rim.",
    "step_dutchoven":"Deep ruby beetroot borscht simmering in a sage-green enamelled cast-iron round Dutch oven, lid set ajar, soft steam rising.",
    "ing_liver":     "Fresh raw beef liver pieces in a small fluted Provencal porcelain bowl.",
    "ing_herbs":     "A modest bundle of fresh dill, chives and coriander tied with kitchen twine, laid on the linen.",
    "ing_seeds":     "Raw green pumpkin seeds in a tiny fluted porcelain pinch bowl.",
    "ing_veg":       "Freshly grated zucchini, carrot and onion in a fluted Provencal porcelain bowl, the three colours distinct.",
    "jar_kvass":     "A 1.6 litre glass clip-top preserving jar with an orange rubber seal and steel wire clamp, filled two-thirds with deep ruby beet kvass, diced beets settled at the bottom.",
}

def gen(item):
    name, subject = item
    body = json.dumps({"model": MODEL, "prompt": subject + STYLE,
                       "size": "1024x1024", "quality": "high", "n": 1}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations", data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
        (OUT / f"{name}.png").write_bytes(base64.b64decode(data["data"][0]["b64_json"]))
        return f"{name}: ok"
    except urllib.error.HTTPError as e:
        return f"{name}: HTTP {e.code}: {e.read().decode()[:200]}"
    except Exception as e:
        return f"{name}: ERR {e}"

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for line in ex.map(gen, SHOTS.items()):
            print(line, flush=True)
