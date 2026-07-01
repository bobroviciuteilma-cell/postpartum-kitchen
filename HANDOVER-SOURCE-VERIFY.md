# HANDOVER — Verify Batch D's source-verification output (fresh-chat, independent audit)

Another chat ("**batch D**") is doing **source verification** — resolving the original recipe link
for the cards / catalogue. Your job is an **independent second pass**: check that every credit it
produced actually **hyperlinks the EXACT recipe** (the specific IG reel or blog post for THAT dish),
that the link resolves, and that the creator is correct. You are the fresh set of eyes Ilma asked
for. Don't trust batch D's output — verify it.

Ilma is due any day. Be fast, be skeptical, don't invent sources.

## 0. Locate batch D's output first
It may be a new/updated file — look for it before doing anything:
```bash
git log --oneline -15
git status --short
ls -la *.md recipe-catalog-data/ 2>/dev/null
grep -rln "instagram.com/p/\|instagram.com/reel/" *.md cook-cards/*.html | head
```
Batch D likely produced one of: a source-link table in a `.md`, edits to the `.lineage` credits in
`cook-cards/*.html`, or additions to `RECIPE-CATALOG.md`. If you can't find it, ask Ilma where batch
D wrote its results (she said she'd "wait to see what it has done").

## 1. The one rule you're enforcing
**A credit MUST hyperlink the EXACT recipe.** Reject and fix any of these:
- a bare `@handle` with no link;
- a link to the creator's **profile** (`instagram.com/handle/`) or **homepage** instead of the post;
- a link to the wrong post / a different dish;
- a **dead or removed** post (404, "sorry this page isn't available");
- an **invented** source (a handle/URL with no evidence behind it) — the worst failure.

A credit is only ✅ if the URL is the specific `instagram.com/p/…` or `/reel/…` (or exact blog-post
URL) for that dish, it resolves, and the creator matches.

## 2. How to verify each link (evidence only)
Cross-check every credit against the evidence on disk, then confirm it live:
1. **`index.html`** subtitles — the source of truth for library recipes (@handle + exact URL).
2. **`recipe-catalog-data/ig-food-index.md`** — all 1,313 IG saves with captions + permalinks; grep
   the dish/handle to find/confirm the exact reel URL.
3. **`RECIPE-CATALOG.md`** — the audit chat's resolved card→link mappings.
4. **Confirm the link resolves + shows the right dish/creator.** Prefer the Apify Instagram scraper
   (`apify/instagram-scraper`, `resultsType: posts`, `resultsLimit: 1` on the permalink) to read the
   caption + author without a login; or Chrome MCP if a browser is open. Flag anything that 404s.
Known corrections that override everything: **Chicken Liver Pâté = @sokoladassiela**; the Pâté
**Pops** freeze-idea = @wildnutritionist. `Traditional` dishes (golden milk, CCF tea, Gond Laddu,
borscht, etc.) legitimately have **no** author — don't force a credit onto them.

## 3. Output — a verdict table Ilma can act on
Produce `SOURCE-VERIFY-REPORT.md`:
`recipe · credit batch D gave · verdict (✅ exact / ⚠ profile-only / ⚠ wrong-post / ✗ dead / ✗ invented / — traditional) · the CORRECT exact URL (or "none on file — ask Ilma")`.
- Do NOT edit the cards yourself (the card-review chat owns card edits — avoid collisions). Your
  deliverable is the corrected link table + a short summary: how many of batch D's credits were
  exact vs needed fixing, and any it invented (call these out loudly).
- Any recipe where no exact link exists anywhere on file → list under **"Ask Ilma for the link."**

## 4. Rules
- Evidence only — never guess a creator or URL. "No source on file" is a valid, honest verdict.
- Traditional/family dishes don't need a creator credit; don't manufacture one.
- Food-first, non-diagnostic framing; this pass is about provenance, not health claims.
