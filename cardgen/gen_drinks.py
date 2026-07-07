#!/usr/bin/env python3
"""Render the mum+helper Cook-Card pair for every drink from cardgen/data_*.py.

The templates are the locked pilot pair (pilot/liver-cutlets{,-mum}.html, 8 feedback
rounds, 2026-07-04), adapted for vessel-bound drinks: NO scaling dial anywhere
(feedback_recipe_scaling_proportion — vessel-bound recipes get no dial).

Writes cook-cards/<slug>.html (helper kitchen-mode) + cook-cards/<slug>-mum.html.
Images come from the shared cook-cards/img/<slug>/ folder.
"""
import os, sys, json

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "cook-cards")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Ccircle cx='8' cy='8' r='7' fill='%239c2b4e'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Marcellus&family=Pinyon+Script&display=swap" rel="stylesheet">
"""

SPRIG = """<svg class="sprig" width="66" height="42" viewBox="0 0 120 80" aria-hidden="true"><g stroke="#6f7d54" stroke-width="1.5" stroke-linecap="round" fill="none"><path d="M60 74 C62 56 60 34 60 20"/><path d="M60 52 C52 48 46 42 43 35 M60 52 C68 48 74 42 77 35"/><path d="M60 38 C53 34 48 29 46 23 M60 38 C67 34 72 29 74 23"/></g><g fill="#9c8cb6"><ellipse cx="60" cy="16" rx="3" ry="5"/><ellipse cx="54" cy="22" rx="2.4" ry="4"/><ellipse cx="66" cy="22" rx="2.4" ry="4"/></g><g><circle cx="86" cy="34" r="5" fill="#e7c878"/><circle cx="95" cy="42" r="3.6" fill="#e7c878"/></g></svg>"""

HELPER_CSS = """<style>
  :root{
    --paper:#F8F2E7; --paper2:#FBF7EE; --sage:#6E8A6F; --sage-d:#4F6A54; --sage-soft:#DDE6D8;
    --amber:#C0843A; --amber-soft:#E9D9BD; --ink:#3B362C; --ink2:#6B6456; --line:#E2D8C5;
    --beet:#9c2b4e;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  [hidden]{display:none !important;}
  html{-webkit-text-size-adjust:100%;}
  body{background:#cdc4b2; font-family:'EB Garamond',serif; color:var(--ink); min-height:100vh;}
  button{font:inherit; color:inherit; background:none; border:none; cursor:pointer;}
  a{text-decoration:none; color:inherit;}
  img{max-width:100%;}
  :focus-visible{outline:2px solid var(--amber); outline-offset:2px; border-radius:6px;}

  .pane-lab{font-family:'Marcellus',serif; letter-spacing:.16em; text-transform:uppercase; font-size:11.5px;
            color:#7a7263; text-align:center; margin:22px 0 10px;}

  .phone{width:min(384px,100%); margin:0 auto; background:#2b251d; border-radius:48px; padding:14px 12px 16px;
         box-shadow:0 30px 60px rgba(40,32,18,.4);}
  .slit{width:88px; height:6px; border-radius:4px; background:#171310; margin:2px auto 10px;}
  .pscreen{background:var(--paper); border-radius:34px; overflow:hidden; display:flex; flex-direction:column;
           height:min(78vh,760px); min-height:560px; position:relative;}
  .pbar{display:flex; align-items:center; justify-content:space-between; gap:8px; padding:12px 16px 6px;}
  .pbrand{font-family:'Pinyon Script',cursive; font-size:21px; color:var(--sage-d); line-height:1;}
  .dots{display:flex; gap:7px; justify-content:center; padding:4px 0 8px;}
  .dots i{width:7px; height:7px; border-radius:50%; background:#d8cfbc; display:block;}
  .dots i.on{background:var(--sage-d); transform:scale(1.25);}
  .screens{flex:1; position:relative; min-height:0;}
  .hscreen{position:absolute; inset:0; overflow-y:auto; -webkit-overflow-scrolling:touch; padding:6px 18px 24px; display:none;}
  .hscreen.on{display:block;}
  .hkicker{font-family:'Marcellus',serif; letter-spacing:.14em; text-transform:uppercase; font-size:11px; color:var(--amber); margin-bottom:6px;}
  .hbtn{display:block; width:100%; min-height:56px; background:var(--sage-d); color:#fff; border-radius:14px;
        font-family:'Marcellus',serif; letter-spacing:.07em; text-transform:uppercase; font-size:14.5px; padding:12px 16px; margin-top:14px;}
  .hbtn:disabled{opacity:.42; cursor:default;}
  .hbtn.ghost{background:var(--paper2); color:var(--sage-d); border:1.5px solid var(--sage-d);}
  .hcap{font-size:12.5px; color:#a59c8a; font-style:italic; text-align:center; margin-top:10px;}
  .phonecap{text-align:center; font-size:13.5px; color:#6d6553; font-style:italic; margin:12px 0 40px;}

  .askhero{width:100%; height:184px; object-fit:cover; border-radius:16px; box-shadow:0 8px 20px rgba(60,50,30,.2);}
  .askname{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:29px; color:var(--ink); margin-top:12px; line-height:1.05;}
  .ovmeta{font-size:14.5px; color:var(--ink2); margin-top:8px; line-height:1.4;}
  .ovmeta b{font-family:'Marcellus',serif; font-weight:400; letter-spacing:.03em; color:var(--sage-d);}
  .ovlist .mrow{min-height:0; padding:6px 2px;}

  .gcount{font-size:14.5px; color:var(--ink2); margin:2px 0 10px;}
  .ggrid{display:grid; grid-template-columns:1fr 1fr; gap:10px;}
  .gtile{position:relative; background:var(--paper2); border:1px solid var(--line); border-radius:14px; overflow:hidden;}
  .gmain{display:flex; flex-direction:column; align-items:center; gap:5px; width:100%; padding:12px 8px 8px; min-height:112px; text-align:center;}
  .gmain img{width:52px; height:52px; border-radius:50%; object-fit:cover; box-shadow:0 2px 8px rgba(60,50,30,.14);}
  .gname{font-size:14px; line-height:1.15;}
  .gqty{font-family:'Marcellus',serif; font-size:15px; color:var(--sage-d); background:var(--sage-soft); border-radius:8px; padding:2px 10px;}
  .gtick{display:flex; align-items:center; justify-content:center; gap:8px; width:100%; min-height:46px;
         border-top:1px solid var(--line); background:#fff;
         font-family:'Marcellus',serif; letter-spacing:.03em; font-size:12.5px; color:var(--sage-d); padding:7px 8px; text-align:center;}
  .gtickbox{width:22px; height:22px; flex:none; border:2px solid var(--sage); border-radius:6px;
            background:#fff center/14px 14px no-repeat;}
  .gticklabel{line-height:1.12;}
  .gout{display:block; width:100%; min-height:30px; font-size:11.5px; color:#a79e8c; font-style:italic; letter-spacing:.01em; padding:5px 6px 8px;}
  .gtile.got{border-color:var(--sage-d);}
  .gtile.got .gmain{background:var(--sage-soft);}
  .gtile.got .gtick{background:var(--sage-d); color:#fff; border-top-color:var(--sage-d);}
  .gtile.got .gtickbox{border-color:#fff; background-color:#fff;
          background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%234F6A54' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6 9 17l-5-5'/></svg>");}
  .gtile.flag{border-color:var(--amber);}
  .gtile.flag .gmain{background:#f2e3c8;}
  .gtile.flag .gtick{opacity:.35;}
  .gtile.flag .gout{color:var(--amber); font-style:normal; font-family:'Marcellus',serif; letter-spacing:.04em;}

  .stephead{display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:8px;}
  .listen{font-family:'Marcellus',serif; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--sage-d);
          border:1px solid var(--sage); border-radius:999px; padding:8px 14px; min-height:34px; background:#fff;}
  .stepimg{width:100%; height:168px; object-fit:cover; border-radius:14px; box-shadow:0 8px 18px rgba(60,50,30,.18);}
  .stepverb{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:25px; line-height:1.14; color:var(--ink); margin:12px 0 6px;}
  .stepdetail{font-size:17.5px; line-height:1.45; color:var(--ink);}
  .stepdetail b{font-weight:500; color:var(--sage-d);}
  .doneline{font-size:15px; font-style:italic; color:var(--sage-d); margin-top:8px;}
  .stepcap{font-size:13.5px; color:#a5722e; font-style:italic; margin-top:6px;}
  .timerow{display:flex; gap:9px; margin-top:12px; flex-wrap:wrap;}
  .timerunit{flex:1; min-width:140px; display:flex; flex-direction:column; gap:5px;}
  .timerlab{font-family:'Marcellus',serif; letter-spacing:.08em; text-transform:uppercase; font-size:11px; color:var(--ink2); text-align:center;}
  .timerbtn{width:100%; min-height:52px; border:1.5px solid var(--sage-d); color:var(--sage-d); background:#fff;
            border-radius:12px; font-family:'Marcellus',serif; font-size:16.5px; letter-spacing:.03em; padding:8px 12px;}
  .timerbtn.run{background:var(--sage-d); color:#fff;}
  .timerbtn.paused{background:var(--amber-soft); border-color:var(--amber); color:#7c531f;}
  .timerbtn.tdone{background:var(--beet); border-color:var(--beet); color:#fff;}
  .timerreset{min-height:34px; font-size:12.5px; color:var(--amber); font-style:italic; letter-spacing:.02em;}
  .timerhint{font-size:12px; color:#a59c8a; font-style:italic; margin-top:8px;}
  .timerdone{font-size:14.5px; color:var(--beet); font-style:italic; margin-top:7px;}
  .confused{display:block; margin:12px 0 0 auto; font-size:13.5px; color:var(--amber); font-style:italic; padding:8px 2px; min-height:34px;}
  .stepnav{display:flex; gap:10px; margin-top:8px;}
  .stepnav .hbtn{flex:1; margin-top:6px;}
  .cookwarn{margin-top:12px; background:#fff; border:1px solid var(--line); border-left:4px solid var(--beet); border-radius:0 12px 12px 0; padding:12px 14px; font-size:15px; line-height:1.45;}
  .cookwarn b{color:var(--beet); font-weight:500;}
  .daychips{display:flex; gap:7px; margin-top:12px; flex-wrap:wrap;}
  .daychip{border:1.5px solid var(--sage); border-radius:999px; background:var(--paper2); color:var(--sage-d);
           font-family:'Marcellus',serif; font-size:12.5px; letter-spacing:.04em; padding:9px 13px; min-height:40px;}
  .daychip.on{background:var(--sage-d); border-color:var(--sage-d); color:#fff;}

  .cookedbtn{display:block; width:100%; min-height:70px; background:var(--sage-d); color:#fff; border-radius:18px;
             font-family:'Cormorant Garamond',serif; font-weight:600; font-size:26px; margin-top:16px; box-shadow:0 10px 24px rgba(79,106,84,.3);}
  .aftercooked h3{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:30px; color:var(--sage-d); margin:14px 0 6px;}
  .donesent{font-size:17px; color:var(--ink2); line-height:1.42; margin-bottom:2px;}
  .notefield{width:100%; margin-top:12px; background:#fff; border:1px solid var(--line); border-radius:12px; padding:11px 13px;
             font:inherit; font-size:15.5px; color:var(--ink); resize:none;}
  .thanks{margin-top:14px; font-size:18px; font-style:italic; color:var(--beet); opacity:0; transition:opacity .9s;}
  .thanks.show{opacity:1;}

  .mrow{display:flex; align-items:center; justify-content:space-between; gap:8px; width:100%; min-height:48px;
        border-bottom:1px dashed var(--line); font-size:16px; text-align:left; padding:7px 2px;}
  .mrow .mq{font-family:'Marcellus',serif; font-size:15px; color:var(--sage-d); flex:none;}
  .mstep{display:flex; align-items:baseline; gap:10px; padding:7px 2px; border-bottom:1px dashed var(--line); font-size:16px; line-height:1.4;}
  .mstep b{font-family:'Marcellus',serif; font-weight:400; font-size:13px; color:var(--sage-d); flex:none; width:20px;}

  .toast{position:absolute; left:50%; bottom:22px; transform:translate(-50%,14px); background:var(--ink); color:var(--paper);
         font-family:'Marcellus',serif; font-size:13px; letter-spacing:.04em; padding:12px 18px; border-radius:11px;
         opacity:0; pointer-events:none; transition:.35s; max-width:86%; text-align:center; z-index:40;}
  .toast.show{opacity:1; transform:translate(-50%,0);}

  .backlink{display:block; text-align:center; font-size:13px; color:#6d6553; font-style:italic; margin:0 0 34px;}
  .backlink a{color:var(--sage-d); text-decoration:underline; text-underline-offset:2px;}

  @media (max-width:420px){ .phone{border-radius:42px; padding:10px 8px 12px;} .pscreen{height:min(82vh,760px);} }

  @media print{
    body{background:#fff;}
    .phone{box-shadow:none; background:#fff; width:100%; padding:0;}
    .pscreen{height:auto; min-height:0; overflow:visible;}
    .slit,.dots,.hbtn,.confused,.listen,.timerbtn,.timerreset,.toast,.cookedbtn,.aftercooked,.backlink,.daychips{display:none !important;}
    .hscreen{position:static; display:block !important; page-break-inside:avoid; padding:8px 0;}
    .stepimg,.askhero{height:auto; max-height:150px;}
  }
</style>
"""


def helper_card(d):
    steps = d["method"]
    n = len(steps)
    dots = "".join('<i class="on"></i>' if i == 0 else "<i></i>" for i in range(n + 2))

    ov_ings = ""  # rendered by JS into #mlist
    ov_method = "".join(
        f'<div class="mstep"><b>{i+1}</b><span>{s}</span></div>'
        for i, s in enumerate(d["overview_method"])
    )

    screens = []
    # --- overview
    screens.append(f"""
      <!-- 1 · overview -->
      <div class="hscreen on" id="s-overview">
        <img class="askhero" src="img/{d['slug']}/hero.jpg" alt="{d['hero_alt']}">
        <div class="askname">{d['name']}</div>
        <p class="ovmeta">{d['meta_line']}</p>
        <div class="hkicker" style="margin-top:16px;">Ingredients</div>
        <div id="mlist" class="ovlist">{ov_ings}</div>
        <div class="hkicker" style="margin-top:14px;">Method</div>
        {ov_method}
        <button class="hbtn" id="startBtn">Start &mdash; gather ingredients</button>
        <p class="hcap">Screen stays on while you make it</p>
      </div>""")

    # --- gather
    screens.append("""
      <!-- 2 · gather -->
      <div class="hscreen" id="s-gather">
        <div class="hkicker">Ingredients &middot; gather everything first</div>
        <p class="gcount" id="gcount"></p>
        <div class="ggrid" id="ggrid"></div>
        <div class="stepnav">
          <button class="hbtn ghost" data-nav="overview">Back</button>
          <button class="hbtn" id="cookStartBtn" disabled>Start</button>
        </div>
        <p class="hcap">Tick each one as you find it &middot; Start opens once they&rsquo;re in</p>
      </div>""")

    # --- steps
    for i, s in enumerate(steps):
        idx = i + 1
        back = "gather" if i == 0 else f"step{i}"
        if i == n - 1:
            nxt = f'<button class="hbtn" data-nav="done">{d.get("last_next", "Done")}</button>'
        else:
            nxt = f'<button class="hbtn" data-nav="step{idx+1}">Next</button>'
        timers = ""
        if s.get("timer"):
            units = ""
            for t in s["timer"]:
                units += f"""
          <div class="timerunit">
            <div class="timerlab">{t['label']}</div>
            <button class="timerbtn" data-min="{t['min']}">Start &middot; {t['min']} min</button>
            <button class="timerreset" hidden>Reset</button>
          </div>"""
            timers = f"""
        <div class="timerow">{units}
        </div>
        <p class="timerhint">Tap a running timer to pause &middot; Reset starts it over.</p>
        <p class="timerdone" hidden>Timer finished &mdash; check it.</p>"""
        warn = ""
        if s.get("warn"):
            warn = f'\n        <div class="cookwarn"><b>{s["warn"]["b"]}</b> {s["warn"]["text"]}</div>'
        cap = f'\n        <p class="stepcap">{s["cap"]}</p>' if s.get("cap") else ""
        days = ""
        if s.get("days"):
            chips = "".join(f'<button class="daychip" data-day="{x}">Day {x}</button>' for x in range(1, 6))
            days = f'\n        <div class="daychips" aria-label="Tick off the days">{chips}</div>\n        <p class="timerhint">Tap each day as it passes &mdash; taste from day 3. (A real reminder comes with the app.)</p>'
        img = ""
        if s.get("img"):
            img = f'\n        <img class="stepimg" src="img/{d["slug"]}/{s["img"]}" alt="{s.get("img_alt","")}">'
        screens.append(f"""
      <div class="hscreen" id="s-step{idx}">
        <div class="stephead"><span class="hkicker">Method &middot; step {idx} of {n}</span><button class="listen" hidden data-say="{s['say']}">Listen</button></div>{img}
        <h2 class="stepverb">{s['verb']}</h2>
        <p class="stepdetail">{s['detail']}</p>{cap}{timers}{warn}{days}
        <p class="doneline">Done looks like: {s['done']}</p>
        <button class="confused" data-step="{idx}">Confused by this step?</button>
        <div class="stepnav"><button class="hbtn ghost" data-nav="{back}">Back</button>{nxt}</div>
        <p class="hcap">Screen stays on while you make it</p>
      </div>""")

    # --- finish
    screens.append(f"""
      <!-- finish -->
      <div class="hscreen" id="s-done">
        <div id="doneForm">
          <h2 class="stepverb" style="margin-top:8px">{d['finish_head']}</h2>
          <textarea class="notefield" id="noteField" rows="2" placeholder="Note for Mum"></textarea>
          <button class="cookedbtn" id="cookedBtn">{d['finish_btn']}</button>
          <p class="hcap">{d['finish_cap']}</p>
          <div class="stepnav"><button class="hbtn ghost" data-nav="step{n}">Back</button></div>
        </div>
        <div class="aftercooked" id="afterCooked" hidden>
          <h3>Beautiful.</h3>
          <p class="donesent">{d['after_line']}</p>
          <p class="thanks" id="thanks">From Mum: &ldquo;Thank you.&rdquo;</p>
        </div>
      </div>""")

    ing_js = json.dumps([
        {"k": it["k"], "n": it["n"], "q": it["q"], "img": it["img"], "opt": bool(it.get("opt"))}
        for it in d["ings"]
    ], ensure_ascii=False)

    dotmap = {"overview": 0, "gather": 1}
    for i in range(1, n + 1):
        dotmap[f"step{i}"] = i + 1
    dotmap["done"] = n + 1
    dot_js = json.dumps(dotmap)

    return (HEAD.format(title=f"{d['name']} — kitchen card · Your Healing Kitchen")
            + HELPER_CSS + f"""</head>
<body>

<p class="pane-lab">The helper&rsquo;s kitchen card</p>
<div class="phone" id="phone">
  <div class="slit"></div>
  <div class="pscreen">
    <div class="pbar">
      <span class="pbrand">Your Healing Kitchen</span>
    </div>
    <div class="dots" id="dots" aria-hidden="true">{dots}</div>

    <div class="screens">
{''.join(screens)}

    </div><!-- /screens -->
    <div class="toast" id="htoast" role="status"></div>
  </div>
</div>
<p class="phonecap">A helper&rsquo;s phone &mdash; big type, one step at a time</p>
<p class="backlink"><a href="drinks.html">&larr; All drinks</a> &middot; <a href="index.html">Everything</a></p>

<script>
const ING = {ing_js};
const state = {{ gathered:new Set(), flagged:new Set(), screen:'overview' }};
const $  = (s,c)=>(c||document).querySelector(s);
const $$ = (s,c)=>Array.from((c||document).querySelectorAll(s));

let hT=null;
function toastH(m){{ const el=$('#htoast'); el.textContent=m; el.classList.add('show'); clearTimeout(hT); hT=setTimeout(()=>el.classList.remove('show'),2300); }}

/* overview ingredient list */
const mlist=$('#mlist');
ING.forEach(it=>{{
  const row=document.createElement('div'); row.className='mrow';
  row.innerHTML='<span>'+it.n+'</span><span class="mq">'+it.q+'</span>';
  mlist.appendChild(row);
}});

/* gather tiles */
const ggrid=$('#ggrid');
ING.forEach(it=>{{
  const tile=document.createElement('div'); tile.className='gtile'; tile.id='gt-'+it.k;
  tile.innerHTML =
    '<button class="gmain" aria-label="I have '+it.n+'">'+
      '<img src="'+it.img+'" alt="">'+
      '<span class="gname">'+it.n+'</span>'+
      '<span class="gqty">'+it.q+'</span>'+
    '</button>'+
    '<button class="gtick"><span class="gtickbox" aria-hidden="true"></span><span class="gticklabel">Tap when you have it</span></button>'+
    '<button class="gout">Out of this</button>';
  ggrid.appendChild(tile);
  const toggle=()=>{{
    if(state.flagged.has(it.k)) state.flagged.delete(it.k);
    state.gathered.has(it.k) ? state.gathered.delete(it.k) : state.gathered.add(it.k);
    renderGather();
  }};
  tile.querySelector('.gmain').addEventListener('click', toggle);
  tile.querySelector('.gtick').addEventListener('click', toggle);
  tile.querySelector('.gout').addEventListener('click',(e)=>{{
    e.stopPropagation();
    state.gathered.delete(it.k);
    if(state.flagged.has(it.k)){{ state.flagged.delete(it.k); }}
    else {{ state.flagged.add(it.k); toastH('Flagged to Mum: '+it.n.toLowerCase()); }}
    renderGather();
  }});
}});
function renderGather(){{
  ING.forEach(it=>{{
    const tile=$('#gt-'+it.k), got=state.gathered.has(it.k), fl=state.flagged.has(it.k);
    tile.classList.toggle('got',got); tile.classList.toggle('flag',fl);
    const lbl=tile.querySelector('.gticklabel'); if(lbl) lbl.textContent = got ? 'Got it' : 'Tap when you have it';
    tile.querySelector('.gout').textContent = fl ? 'Never mind — found it' : 'Out of this';
  }});
  const got = state.gathered.size;
  $('#gcount').textContent = got+' of '+ING.length+' in'+(state.flagged.size?' · '+state.flagged.size+' flagged to Mum':'');
  $('#cookStartBtn').disabled = !ING.every(it => it.opt || state.gathered.has(it.k) || state.flagged.has(it.k));
}}
renderGather();

/* flow */
const DOT = {dot_js};
function show(name){{
  state.screen=name;
  $$('.hscreen').forEach(s=>s.classList.remove('on'));
  $('#s-'+name).classList.add('on');
  const dd=DOT[name]; if(dd!==undefined) $$('#dots i').forEach((el,i)=>el.classList.toggle('on', i===dd));
  const sc=$('#s-'+name); if(sc) sc.scrollTop=0;
}}
$('#startBtn').addEventListener('click', ()=>show('gather'));
$('#cookStartBtn').addEventListener('click', ()=>show('step1'));
$$('[data-nav]').forEach(b=> b.addEventListener('click', ()=>show(b.dataset.nav)));

/* timers — tap to start / pause / resume; Reset runs the minutes over */
$$('.timerbtn').forEach(btn=>{{
  const secs0=Math.round(parseFloat(btn.dataset.min)*60);
  const idle=btn.textContent;
  const unit=btn.closest('.timerunit');
  const resetBtn=unit&&unit.querySelector('.timerreset');
  const scr=btn.closest('.hscreen'); const dl=scr&&scr.querySelector('.timerdone');
  const o={{ rem:secs0, iv:null, running:false, paused:false, done:false,
    fmt(){{ const m=Math.floor(o.rem/60), s=o.rem%60; return m+':'+String(s).padStart(2,'0'); }},
    tick(){{ o.rem--; if(o.rem<=0) o.finish(); else btn.textContent=o.fmt(); }},
    start(){{ o.running=true; o.paused=false; btn.classList.add('run'); btn.classList.remove('paused');
      if(resetBtn) resetBtn.hidden=false; btn.textContent=o.fmt(); o.iv=setInterval(o.tick,1000); }},
    pause(){{ clearInterval(o.iv); o.iv=null; o.running=false; o.paused=true;
      btn.classList.remove('run'); btn.classList.add('paused'); btn.textContent='Paused · '+o.fmt(); }},
    finish(){{ clearInterval(o.iv); o.iv=null; o.running=false; o.paused=false; o.done=true; o.rem=0;
      btn.classList.remove('run','paused'); btn.classList.add('tdone'); btn.textContent='Done — check it'; if(dl) dl.hidden=false; }},
    reset(){{ clearInterval(o.iv); o.iv=null; o.rem=secs0; o.running=false; o.paused=false; o.done=false;
      btn.classList.remove('run','paused','tdone'); btn.textContent=idle; if(resetBtn) resetBtn.hidden=true; }}
  }};
  btn.addEventListener('click', ()=>{{ if(o.done) o.reset(); else if(o.running) o.pause(); else o.start(); }});
  if(resetBtn) resetBtn.addEventListener('click', ()=>o.reset());
}});

/* day chips (ferments) */
$$('.daychip').forEach(c=> c.addEventListener('click', ()=> c.classList.toggle('on')));

/* confused */
$$('.confused').forEach(b=> b.addEventListener('click', ()=>toastH('Noted for Mum')));

/* listen */
if('speechSynthesis' in window){{
  $$('.listen').forEach(b=>{{ b.hidden=false;
    b.addEventListener('click', ()=>{{ try{{ speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(b.dataset.say); u.rate=.95; speechSynthesis.speak(u);}}catch(e){{}} }});
  }});
}}

/* done */
$('#cookedBtn').addEventListener('click', ()=>{{
  show('done');
  $('#doneForm').hidden=true; $('#afterCooked').hidden=false;
  setTimeout(()=>$('#thanks').classList.add('show'),1400);
}});

/* screen awake */
let wakeLock=null;
async function keepAwake(){{ try{{ if('wakeLock' in navigator){{ wakeLock=await navigator.wakeLock.request('screen'); }} }}catch(e){{}} }}
document.addEventListener('click', keepAwake, {{once:true}});
</script>
</body>
</html>
""")


MUM_CSS = """<style>
  :root{
    --paper:#F8F2E7; --paper2:#FBF7EE; --sage:#6E8A6F; --sage-d:#4F6A54; --sage-soft:#DDE6D8;
    --amber:#C0843A; --amber-soft:#EEDFC4; --ink:#3B362C; --ink2:#6B6456; --line:#E4DAC7;
    --beet:#9c2b4e; --beet-soft:#f3dee5;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  [hidden]{display:none !important;}
  html{-webkit-text-size-adjust:100%;}
  body{background:#cbc2af; font-family:'EB Garamond',serif; color:var(--ink); min-height:100vh;
       padding:28px 16px 60px;
       background-image:radial-gradient(circle at 30% 20%, rgba(255,255,255,.18), transparent 60%);}
  button{font:inherit; color:inherit; background:none; border:none; cursor:pointer;}
  a{text-decoration:none; color:inherit;}
  img{max-width:100%; display:block;}
  :focus-visible{outline:2px solid var(--amber); outline-offset:2px; border-radius:6px;}

  .pane-lab{font-family:'Marcellus',serif; letter-spacing:.18em; text-transform:uppercase; font-size:11px;
            color:#7a7263; text-align:center; margin:0 0 14px;}

  .card{width:min(680px,100%); margin:0 auto; background:var(--paper); border-radius:20px; overflow:hidden;
        box-shadow:0 30px 70px rgba(60,50,30,.28), 0 2px 0 rgba(255,255,255,.5) inset;}

  .brandbar{text-align:center; padding:30px 30px 6px;}
  .sprig{display:block; margin:0 auto 12px;}
  .brandmark{font-family:'Pinyon Script',cursive; font-size:40px; color:var(--sage-d); line-height:1;}
  .brandtag{font-family:'Marcellus',serif; letter-spacing:.26em; text-transform:uppercase; font-size:10px; color:var(--amber); margin-top:7px;}
  .eyebrow{font-family:'Marcellus',serif; letter-spacing:.16em; text-transform:uppercase; font-size:10.5px; color:var(--ink2); margin-top:6px;}
  .eyebrow .dot{color:var(--amber); margin:0 2px;}
  .brandrule{width:60px; height:1px; background:var(--line); margin:12px auto 0;}

  .head{padding:14px 30px 4px; display:flex; gap:22px; align-items:center;}
  .head .htext{flex:1; min-width:0;}
  h1{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:40px; line-height:1.02; color:var(--sage-d); margin:2px 0 6px;}
  .sub{font-style:italic; font-size:17px; color:var(--ink2); line-height:1.4;}
  .hero{width:158px; height:158px; border-radius:14px; object-fit:cover; flex:none;
        box-shadow:0 12px 26px rgba(60,50,30,.26); border:5px solid #fff;}

  .meta{display:flex; flex-wrap:wrap; gap:8px 26px; padding:16px 30px 0;}
  .metarow{font-size:15.5px; color:var(--ink); line-height:1.35;}
  .metarow b{font-family:'Marcellus',serif; font-weight:400; letter-spacing:.08em; text-transform:uppercase; font-size:10.5px; color:var(--amber); margin-right:7px;}
  .whenband{margin:14px 30px 0; background:var(--sage-soft); border-radius:12px; padding:12px 18px; font-size:15.5px; color:var(--sage-d); line-height:1.4;}
  .whenband b{font-family:'Marcellus',serif; letter-spacing:.08em; text-transform:uppercase; font-size:10.5px; color:var(--sage-d); margin-right:8px;}

  .section{padding:20px 30px 0;}
  .blockh{font-family:'Marcellus',serif; letter-spacing:.14em; text-transform:uppercase; font-size:12px; color:var(--amber); margin-bottom:11px;}

  .why{background:var(--paper2); border:1px solid var(--line); border-radius:14px; padding:18px 20px;}
  .why ul{list-style:none;}
  .why li{font-size:16.5px; line-height:1.45; position:relative; padding-left:18px; margin-bottom:10px;}
  .why li:last-child{margin-bottom:0;}
  .why li::before{content:""; position:absolute; left:2px; top:9px; width:6px; height:6px; border-radius:50%; background:var(--sage);}
  .tag{display:inline-block; font-family:'Marcellus',serif; font-size:10px; letter-spacing:.05em;
       padding:3px 9px; border-radius:999px; vertical-align:middle; margin-left:5px; transform:translateY(-1px);
       border:1px solid transparent;}
  button.tag{cursor:pointer; min-height:22px;}
  button.tag:hover{filter:brightness(.97);}
  .tag.rb{background:#dfeada; color:#3f6a45;}
  .tag.t{background:#efe2cb; color:#8a6326;}
  .tag.b{background:var(--beet-soft); color:#8d3a5c;}
  .bfnote{margin-top:12px; font-size:14.5px; color:var(--ink2); font-style:italic; line-height:1.45;}
  .lnk{background:none; border:none; padding:0; font:inherit; color:var(--sage-d); text-decoration:underline; text-underline-offset:2px; cursor:pointer;}
  .whykey{font-size:12.5px; color:#a89f8c; font-style:italic; margin-top:10px;}

  .controls{margin-top:8px; background:#fff; border:1.5px solid var(--sage); border-radius:16px; padding:18px 20px 16px;
            box-shadow:0 10px 26px rgba(79,106,84,.10);}
  .controls .blockh{color:var(--sage-d); margin-bottom:3px;}
  .panel-sub{font-size:14px; color:var(--ink2); font-style:italic; margin-bottom:6px;}
  .ctl-row{padding:14px 0; border-bottom:1px solid var(--line);}
  .ctl-row.last{border-bottom:none; padding-bottom:2px;}
  .ctl-lab{font-family:'Marcellus',serif; letter-spacing:.06em; text-transform:uppercase; font-size:11.5px; color:var(--ink2); margin-bottom:10px;}

  .tickrow{display:flex; flex-wrap:wrap; gap:9px;}
  .tick{border:1.5px solid var(--sage); border-radius:999px; background:var(--paper2); color:var(--ink);
        font-size:15px; line-height:1.25; padding:10px 16px 10px 14px; min-height:46px; text-align:left;
        display:inline-flex; align-items:center; gap:10px; transition:background .2s, border-color .2s;}
  .tick small{display:block; font-size:12.5px; color:var(--ink2); font-style:italic; margin-top:1px;}
  .tick:hover{border-color:var(--sage-d);}
  .tick::before{content:""; width:20px; height:20px; flex:none; border:2px solid var(--sage); border-radius:6px;
             background:#fff center/13px 13px no-repeat; transition:background-color .15s, border-color .15s;}
  .tick.on{background:var(--sage-soft); border-color:var(--sage-d);}
  .tick.on::before{border-color:var(--sage-d); background-color:var(--sage-d);
             background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6 9 17l-5-5'/></svg>");}
  .ctl-note{font-size:13.5px; color:var(--ink2); font-style:italic; margin:10px 0 0; line-height:1.45;}

  .sendrow{display:flex; gap:11px; align-items:center; flex-wrap:wrap; margin-top:4px;}
  .bywhen{display:flex; align-items:center; gap:9px; font-size:15px; color:var(--ink2);}
  .bywhen select{font:inherit; font-family:'Marcellus',serif; font-size:15px; color:var(--sage-d); background:var(--paper2);
                 border:1px solid var(--line); border-radius:10px; padding:11px 9px; min-height:48px;}
  .beetbtn{flex:1; min-width:200px; min-height:52px; background:var(--beet); color:#fff; border-radius:13px;
           font-family:'Marcellus',serif; letter-spacing:.06em; text-transform:uppercase; font-size:13.5px; padding:11px 16px;
           transition:background .25s;}
  .beetbtn:hover{background:#872444;}
  .beetbtn.sent{background:var(--sage-d);}
  .sentcard{margin-top:13px; background:var(--paper2); border:1px solid var(--line); border-radius:12px; padding:14px 16px; display:none;}
  .sentcard.show{display:block;}
  .sentcard .sl{font-family:'Marcellus',serif; letter-spacing:.1em; text-transform:uppercase; font-size:10.5px; color:var(--amber); margin-bottom:7px;}
  .sentcard ul{list-style:none;}
  .sentcard li{font-size:15px; color:var(--ink); line-height:1.5; padding-left:16px; position:relative;}
  .sentcard li::before{content:""; position:absolute; left:2px; top:9px; width:5px; height:5px; border-radius:50%; background:var(--beet);}
  .sentcard a{color:var(--sage-d); text-decoration:underline; text-underline-offset:2px; font-style:italic;}

  .ings-grid{display:grid; grid-template-columns:1fr 1fr; gap:2px 24px;}
  .ing{display:flex; align-items:center; gap:12px; padding:9px 0; border-bottom:1px solid var(--line);}
  .ing img{width:46px; height:46px; border-radius:50%; object-fit:cover; flex:none; box-shadow:0 2px 8px rgba(60,50,30,.14);}
  .ing .q{font-family:'Marcellus',serif; font-size:13px; color:var(--sage-d); width:78px; flex:none; line-height:1.25;}
  .ing .n{font-size:15.5px; line-height:1.25;}
  .ing .n i{font-size:12.5px; color:#a89f8c; font-style:normal; display:block;}

  .step{display:flex; gap:14px; margin-bottom:16px; align-items:flex-start;}
  .step .n{width:25px; height:25px; border-radius:50%; background:var(--sage-d); color:#fff; flex:none;
           font-family:'Marcellus',serif; font-size:13px; display:flex; align-items:center; justify-content:center; margin-top:3px;}
  .step .b{flex:1; min-width:0;}
  .step .ic{font-size:11.5px; color:var(--amber); font-family:'Marcellus',serif; letter-spacing:.08em; text-transform:uppercase; display:block; margin-bottom:3px;}
  .step p{font-size:16px; line-height:1.42;}
  .step p b{color:var(--sage-d); font-weight:500;}
  .cooknote{margin-top:6px; background:var(--beet-soft); border-radius:11px; padding:11px 14px; font-size:14.5px; line-height:1.42; color:#7a2740;}
  .cooknote b{color:var(--beet); font-weight:600;}

  .nutri{display:grid; grid-template-columns:repeat(auto-fit,minmax(120px,1fr)); gap:10px; margin-top:2px;}
  .nutri .cell{background:var(--paper2); border:1px solid var(--line); border-radius:12px; padding:12px 14px;}
  .nutri .v{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:24px; color:var(--sage-d); line-height:1;}
  .nutri .k{font-family:'Marcellus',serif; letter-spacing:.06em; text-transform:uppercase; font-size:10px; color:var(--ink2); margin-top:5px;}
  .disc{padding:22px 30px 26px; font-size:12.5px; color:#a89f8c; font-style:italic; text-align:center; line-height:1.5;}

  .footlinks{text-align:center; margin:22px 0 0; font-size:14px; color:#6d6553; font-style:italic;}
  .footlinks a{color:var(--sage-d); text-decoration:underline; text-underline-offset:2px;}

  .evwrap{position:fixed; inset:0; z-index:120; display:none;}
  body.evopen .evwrap{display:block;}
  .evback{position:absolute; inset:0; background:rgba(43,37,29,.46);}
  .evsheet{position:absolute; left:50%; bottom:0; transform:translate(-50%,105%); width:min(460px,96vw);
           background:var(--paper); border-radius:22px 22px 0 0; padding:24px 26px 28px; box-shadow:0 -18px 50px rgba(40,32,18,.35);
           transition:transform .4s cubic-bezier(.22,.9,.28,1); max-height:84vh; overflow-y:auto;}
  body.evopen .evsheet{transform:translate(-50%,0);}
  .evgrab{width:44px; height:4px; border-radius:3px; background:var(--line); margin:0 auto 16px;}
  .evsheet h3{font-family:'Cormorant Garamond',serif; font-weight:600; font-size:24px; line-height:1.18; color:var(--ink); margin:10px 0 8px;}
  .evmeaning{font-size:15.5px; line-height:1.5; color:var(--ink);}
  .evsrc{margin:14px 0 0; background:var(--paper2); border:1px solid var(--line); border-radius:12px; padding:13px 16px;}
  .evsrc .sl{font-family:'Marcellus',serif; letter-spacing:.1em; text-transform:uppercase; font-size:10.5px; color:var(--amber); margin-bottom:7px;}
  .evsrc ul{list-style:none;}
  .evsrc li{font-size:14.5px; line-height:1.45; padding-left:14px; position:relative; margin-bottom:6px;}
  .evsrc li::before{content:""; position:absolute; left:2px; top:8px; width:5px; height:5px; border-radius:50%; background:var(--sage);}
  .evsrc a{color:var(--sage-d); text-decoration:underline; text-underline-offset:2px;}
  .evkey{margin-top:16px; border-top:1px solid var(--line); padding-top:13px; display:flex; flex-wrap:wrap; gap:7px; align-items:center;}
  .evkey .kx{font-size:12.5px; color:var(--ink2); margin-right:2px;}
  .evclose{display:block; width:100%; min-height:50px; margin-top:16px; border:1.5px solid var(--sage-d); color:var(--sage-d);
           border-radius:13px; font-family:'Marcellus',serif; letter-spacing:.08em; text-transform:uppercase; font-size:13px; background:#fff;}

  @media (max-width:600px){
    body{padding:16px 12px 50px;}
    .head{flex-direction:row; gap:14px; padding:12px 20px 4px;}
    .hero{width:104px; height:104px; border-width:4px;}
    h1{font-size:31px;}
    .brandbar,.meta,.whenband,.section,.disc{padding-left:20px; padding-right:20px;}
    .whenband{margin-left:20px; margin-right:20px;}
    .ings-grid{grid-template-columns:1fr; gap:0;}
  }

  @media print{
    body{background:#fff; padding:0;}
    .card{box-shadow:none; width:100%;}
    .controls{box-shadow:none;}
    .pane-lab,.footlinks,.beetbtn,.bywhen{display:none !important;}
  }
</style>
"""


def mum_card(d):
    slug = d["slug"]

    why_lis = ""
    for w in d["why"]:
        chip = ""
        if w.get("chip"):
            cls = w["chip"]
            label = {"rb": "research-backed", "t": "tradition", "b": "breastfeeding note"}[cls]
            chip = f' <button class="tag {cls}" data-ev="{w["ev"]}">{label}</button>'
        why_lis += f"        <li>{w['text']}{chip}</li>\n"

    bf = ""
    if d.get("bfnote"):
        bf = f'\n      <p class="bfnote">{d["bfnote"]["text"]} <button class="lnk" data-ev="{d["bfnote"]["ev"]}">{d["bfnote"].get("linktext","Read the breastfeeding note")}</button>.</p>'

    serve_row = ""
    if d.get("serve"):
        ticks = "".join(
            f'\n          <button class="tick{" on" if it.get("on") else ""}" data-serve="{it["k"]}" aria-pressed="{"true" if it.get("on") else "false"}">{it["label"]}</button>'
            for it in d["serve"]["items"])
        serve_row = f"""
      <div class="ctl-row">
        <div class="ctl-lab">{d['serve']['label']}</div>
        <div class="tickrow">{ticks}
        </div>
      </div>"""

    boost_row = ""
    if d.get("boost"):
        ticks = ""
        for it in d["boost"]["items"]:
            small = f'<small>{it["small"]}</small>' if it.get("small") else ""
            ticks += f'\n          <button class="tick{" on" if it.get("on") else ""}" data-boost="{it["k"]}" aria-pressed="{"true" if it.get("on") else "false"}">{it["label"]}{small}</button>'
        note = f'\n        <p class="ctl-note">{d["boost"]["note"]}</p>' if d["boost"].get("note") else ""
        boost_row = f"""
      <div class="ctl-row">
        <div class="ctl-lab">{d['boost']['label']}</div>
        <div class="tickrow">{ticks}
        </div>{note}
      </div>"""

    opts = "".join(
        f'<option{" selected" if o == d["when_opts"]["sel"] else ""}>{o}</option>'
        for o in d["when_opts"]["opts"])

    ings = ""
    for it in d["ings"]:
        prep = f"<i>{it['prep']}</i>" if it.get("prep") else ""
        ings += f'      <div class="ing"><img src="{it["img"]}" alt="{it["n"]}"><span class="q">{it["q"]}</span><span class="n">{it["n"]}{prep}</span></div>\n'

    steps = ""
    for i, s in enumerate(d["method"]):
        note = ""
        if s.get("warn"):
            note = f'<div class="cooknote"><b>{s["warn"]["b"]}</b> {s["warn"]["text"]}</div>'
        text = s.get("mum") or s["detail"]
        steps += f'    <div class="step"><div class="n">{i+1}</div><div class="b"><span class="ic">{s["ic"]}</span><p>{text}</p>{note}</div></div>\n'

    nutri = "".join(
        f'\n      <div class="cell"><div class="v">{c["v"]}</div><div class="k">{c["k"]}</div></div>'
        for c in d["nutri"])

    ev_js = json.dumps(d["ev"], ensure_ascii=False)
    serve_js = json.dumps({it["k"]: it["label"] for it in (d.get("serve", {}) or {}).get("items", [])}, ensure_ascii=False)
    serve_state = json.dumps({it["k"]: bool(it.get("on")) for it in (d.get("serve", {}) or {}).get("items", [])})
    boost_js = json.dumps({it["k"]: it["label"] for it in (d.get("boost", {}) or {}).get("items", [])}, ensure_ascii=False)
    boost_state = json.dumps({it["k"]: bool(it.get("on")) for it in (d.get("boost", {}) or {}).get("items", [])})

    return (HEAD.format(title=f"{d['name']} — Mum's card · Your Healing Kitchen")
            + MUM_CSS + f"""</head>
<body>

<p class="pane-lab">Mum&rsquo;s card &middot; the why &amp; your instructions</p>

<div class="card">
  <div class="brandbar">
    {SPRIG}
    <div class="brandmark">Your Healing Kitchen</div>
    <div class="brandtag">Natural Healing &middot; Fourth Trimester</div>
    <div class="eyebrow">{d['eyebrow']}</div>
    <div class="brandrule"></div>
  </div>

  <div class="head">
    <div class="htext">
      <h1>{d['name']}</h1>
      <div class="sub">{d['sub']}</div>
    </div>
    <img class="hero" src="img/{slug}/hero.jpg" alt="{d['hero_alt']}">
  </div>

  <div class="meta">
    <div class="metarow"><b>Time to make</b> {d['time']}</div>
    <div class="metarow"><b>Keep</b> {d['keep']}</div>
  </div>

  <div class="whenband"><b>{d['when_label']}</b> {d['when']}</div>

  <!-- WHY -->
  <div class="section">
    <div class="why">
      <div class="blockh">Why this heals you</div>
      <ul>
{why_lis}      </ul>{bf}
      <p class="whykey">Tap a label to see the sources behind it.</p>
    </div>
  </div>

  <!-- YOUR INSTRUCTIONS -->
  <div class="section">
    <div class="controls">
      <div class="blockh">Your instructions</div>
      <p class="panel-sub">{d['instr_note']}</p>
{serve_row}{boost_row}
      <div class="ctl-row last">
        <div class="sendrow">
          <label class="bywhen">{d['when_opts']['label']}
            <select id="timeSel" aria-label="{d['when_opts']['label']}">{opts}</select>
          </label>
          <button id="sendBtn" class="beetbtn">Send to my helper</button>
        </div>
        <div class="sentcard" id="sentCard">
          <div class="sl">On your helper&rsquo;s card now</div>
          <ul id="sentList"></ul>
        </div>
      </div>
    </div>
  </div>

  <!-- INGREDIENTS -->
  <div class="section">
    <div class="blockh">Ingredients</div>
    <div class="ings-grid">
{ings}    </div>
  </div>

  <!-- METHOD -->
  <div class="section">
    <div class="blockh">Method</div>
{steps}  </div>

  <!-- NUTRITION -->
  <div class="section">
    <div class="blockh">{d['nutri_label']}</div>
    <div class="nutri">{nutri}
    </div>
  </div>

  <div class="disc">Food, not medical advice &middot; non-diagnostic &middot; made for this season of motherhood</div>
</div>

<p class="footlinks"><a href="{slug}.html">See your helper&rsquo;s view &rarr;</a> &middot; <a href="drinks.html">All drinks</a></p>

<!-- evidence sheet -->
<div class="evwrap" id="evWrap">
  <div class="evback" id="evBack"></div>
  <div class="evsheet" role="dialog" aria-modal="true" aria-labelledby="evTitle" id="evSheet" tabindex="-1">
    <div class="evgrab"></div>
    <span class="tag rb" id="evChip">research-backed</span>
    <h3 id="evTitle"></h3>
    <p class="evmeaning" id="evMeaning"></p>
    <div class="evsrc"><div class="sl">Sources</div><ul id="evSources"></ul></div>
    <div class="evkey">
      <span class="kx">Labels:</span>
      <span class="tag rb">research-backed</span><span class="tag t">tradition</span><span class="tag b">breastfeeding note</span>
    </div>
    <button class="evclose" id="evClose">Close</button>
  </div>
</div>

<script>
const $=(s,c)=>(c||document).querySelector(s);
const $$=(s,c)=>Array.from((c||document).querySelectorAll(s));

/* ---------- ticks ---------- */
const state={{ serve:{serve_state}, boost:{boost_state} }};
$$('.tick').forEach(btn=>btn.addEventListener('click',()=>{{
  const on=!btn.classList.contains('on'); btn.classList.toggle('on',on); btn.setAttribute('aria-pressed',String(on));
  if(btn.dataset.serve) state.serve[btn.dataset.serve]=on;
  if(btn.dataset.boost) state.boost[btn.dataset.boost]=on;
}}));

/* ---------- send to helper (simulated preview) ---------- */
const SERVE={serve_js};
const BOOST={boost_js};
$('#sendBtn').addEventListener('click',()=>{{
  const b=$('#sendBtn'); b.textContent='Sent to your helper'; b.classList.add('sent');
  const items=[];
  items.push('For: <b>'+$('#timeSel').value+'</b>');
  const sv=Object.keys(SERVE).filter(k=>state.serve[k]).map(k=>SERVE[k]); if(sv.length) items.push('With: '+sv.join(', '));
  const bo=Object.keys(BOOST).filter(k=>state.boost[k]).map(k=>BOOST[k]); if(bo.length) items.push('In your cup: '+bo.join(', '));
  items.push('<a href="{slug}.html">Open the helper&rsquo;s card &rarr;</a>');
  $('#sentList').innerHTML=items.map(t=>'<li>'+t+'</li>').join('');
  $('#sentCard').classList.add('show');
}});

/* ---------- evidence sheet ---------- */
const EV={ev_js};
function openEv(id){{ const e=EV[id]; if(!e) return;
  const chip=$('#evChip'); chip.className='tag '+e.cls; chip.textContent=e.chip;
  $('#evTitle').textContent=e.title; $('#evMeaning').textContent=e.meaning;
  $('#evSources').innerHTML=e.src.map(s=>'<li>'+s+'</li>').join('');
  document.body.classList.add('evopen'); $('#evSheet').focus();
}}
$$('[data-ev]').forEach(b=>b.addEventListener('click',()=>openEv(b.dataset.ev)));
function closeEv(){{ document.body.classList.remove('evopen'); }}
$('#evClose').addEventListener('click',closeEv); $('#evBack').addEventListener('click',closeEv);
document.addEventListener('keydown',e=>{{ if(e.key==='Escape') closeEv(); }});
</script>
</body>
</html>
""")


def defaults(d):
    d.setdefault("meta_line", f"{d['time'][:1].upper()}{d['time'][1:]} &middot; makes <b>{d['makes']}</b>")
    d.setdefault("finish_head", "All made?")
    d.setdefault("finish_btn", "Made &mdash; tell Mum")
    d.setdefault("finish_cap", "Mum gets a note on her phone that it&rsquo;s ready.")
    d.setdefault("after_line", "Sent to Mum &mdash; she knows it&rsquo;s ready.")
    d.setdefault("last_next", "Done")
    d.setdefault("when_label", "When to drink")
    d.setdefault("nutri_label", "In a cup, roughly")
    d.setdefault("instr_note", "Made to the cup &mdash; nothing to scale. Your helper&rsquo;s card matches this one.")
    return d


def main(only=None):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import data_teas, data_milks, data_mineral
    drinks = data_teas.DRINKS + data_milks.DRINKS + data_mineral.DRINKS
    for d in drinks:
        if only and d["slug"] not in only:
            continue
        d = defaults(d)
        with open(os.path.join(OUT, d["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(helper_card(d))
        with open(os.path.join(OUT, d["slug"] + "-mum.html"), "w", encoding="utf-8") as f:
            f.write(mum_card(d))
        print("rendered", d["slug"], "+ mum view")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
