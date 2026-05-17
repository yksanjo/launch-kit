# HN + Product Hunt Launch — mirror-deployer

Single-shot launch playbook for `mirror-deployer` on Show HN + Product Hunt. Goal: front-page exposure → 1k–10k new eyeballs → KOL/trader pickup → audience flows into $SOAG TG + Holder Hunt naturally.

**Critical positioning rule:** $SOAG is **NOT** mentioned in the HN submission, PH submission, or first 3 hours of conversation. HN/PH crowds bounce on "and there's a token." $SOAG comes up in TG and X organically *after* HN traffic lands.

---

## Pre-launch fixes (DONE by me)

- ✅ Removed "ex-Atlantic Records, ex-Warner Music" from `package.json` description
- ✅ Removed LinkedIn link from README footer (identity exposure)
- ✅ Replaced broken Mirror family links (mirror-pilot, mirror-marketplace) with a soft "planned sequence" line

## Pre-launch fixes (YOU need to do — ~10 min)

- [ ] **Verify or set up a live demo URL.** If `mirror-deployer.musicailab.com` or any other public URL serves the live app, add it to the README near the top (replace the Quick Start placeholder). If not, **set up the Cloudflare Tunnel route for port 8083** before HN submit — live demo doubles HN/PH conversion.
- [ ] **Add a screenshot to the repo.** Open the running app, screenshot the leaderboard or a deployer profile, commit as `public/screenshot.png`, reference in README near the top.
- [ ] **Commit + push the README + package.json changes** I made.
- [ ] **Tag a v1.1.0 release** on GitHub so HN sees it as a fresh ship.

---

## Submission timing

| Surface | Best window (UTC) | Why | Avoid |
|---|---|---|---|
| **Show HN** | **Tue or Wed, 13:00–15:00 UTC** | Peak HN US-east-morning + EU-mid-afternoon overlap. Front-page algorithm gives most weight to first 2 hours. | Mondays (HN re-saturation from weekend), Fridays (low engagement) |
| **Product Hunt** | **Tue or Wed, 00:01 PST (08:01 UTC)** | PH launches are day-bucketed; 00:01 PST starts the day-counter clean. Tue/Wed get more viewer activity than Mon/Fri. | Sundays (lowest PH activity), launching mid-day (you start with a deficit) |

**Recommendation: stagger.** Tue 08:01 UTC = Product Hunt launch. Tue 13:00 UTC = Show HN submit. Same day = X thread carries both campaigns. Buy yourself 5 hours of PH momentum before HN hits.

**Next viable Tue/Wed: 2026-05-19 (Tue) or 2026-05-20 (Wed).**

---

## Show HN submission

### Title (≤80 chars, no "Show HN:" prefix — HN adds it automatically)
Pick one — these are A/B variants:

**Variant A (problem-led, RECOMMENDED):**
```
Mirror Deployer – Reputation scoring for pump.fun deployers
```
(60 chars — short, punchy, says exactly what it is)

**Variant B (concrete-tool framing):**
```
Mirror Deployer – Paste a wallet, get the deployer's rug/grad track record
```
(75 chars — slightly more loaded, signals utility)

**Variant C (mechanism-led):**
```
Mirror Deployer – On-chain reputation feed for the pump.fun deployer graph
```
(74 chars — emphasizes data layer)

### URL field
- If live demo exists: paste the demo URL (e.g. `mirror-deployer.musicailab.com`)
- If only GitHub: `https://github.com/yksanjo/mirror-deployer`

### First comment (CRITICAL — post within 30 sec of submitting)

This is the single most important text in the whole launch. HN's algorithm gives weight to author-engaged posts, and 80% of users only read this comment, not the README.

```
Author here.

Built this because doing pump.fun deployer diligence took me 15+ minutes per token — open Solscan, scroll deployer wallet, count graduations vs rugs, eyeball holder distribution, check freeze/mint. Same workflow, every time. So I automated it.

The system pulls deployer history via Helius RPC, parses pump.fun program logs for launch + graduation events, computes a deterministic 0–100 score from five factors (graduation rate, rug rate, holder retention, time-to-bond, sample size). No LLM in the scoring path — every number is reproducible from on-chain data.

The "thesis" generation is the only AI piece — it takes the structured score + history and generates a short natural-language read on the deployer's archetype (Serial Graduate, Rug Pattern, One-Hit Wonder, Fresh Wallet, etc.). That part is genuinely fuzzy.

Honest limitations:
- Reputation lag: a fresh deployer with 1 launch has too small a sample to score reliably. We flag low-confidence explicitly rather than guess.
- Graduation-to-Raydium detection is brittle to pump.fun's PumpSwap migration — currently handles both, but they shipped fast and I might be missing edge cases.
- Holder retention is a snapshot, not time-series. Working on a v2 that tracks decay curves.

Stack: Next.js 14, TypeScript, Helius for RPC, deterministic scoring + GPT-4 for the thesis layer. ~3k lines of TS. Self-hostable; MIT license.

Happy to answer architecture questions or run a profile on any deployer wallet you're curious about — paste it in a reply.
```

### Hour-by-hour playbook after submission

| Time | Action | Why |
|---|---|---|
| **T+0** | Submit + post first comment within 30 sec | Algo weight |
| T+0–10 min | Pin tweet from @yksanjo: "Show HN'd Mirror Deployer — [link]. If you've ever wasted 15 min on solscan for pre-buy diligence on a pump.fun token, this is the same flow in 10 sec." | Drives first wave of votes |
| T+30 min | Reply substantively to every top-level comment, even hostile ones (especially hostile ones — HN respects engagement) | Algo + community trust |
| T+1h | Tweet a screenshot of the leaderboard with current top deployers | Shareable artifact for HN crowd to retweet |
| T+2h | If on front page (rank <30): screenshot HN front page from @yksanjo as "we're on the front page" tweet | Social proof loop |
| T+4h | If front page: post in $SOAG TG and Holder Hunt TG: "mirror-deployer is on HN front page right now. If you're around, drop a comment about your favorite use case." | Audience tap |
| T+8h | Long reply to a substantive comment on HN. Pick the smartest critique and engage deeply with the why. | Tail engagement |
| T+24h | Recap thread on X: "Show HN went [stats] — N upvotes, M comments. Top discussion was [topic]. Here's what I learned." | Closes the loop with audience that didn't catch it live |

### Things that get you banned / ghosted on HN
- Vote manipulation (asking people in Discord/TG to upvote) — HN detects coordinated voting via account graph + IP. Don't.
- Multiple submissions of the same project within 30 days
- Hostile responses to critics — HN respects pushback, ban-flags rudeness
- "Hidden token / pump-and-dump" perception — keep $SOAG OUT of HN

---

## Product Hunt submission

### Name
```
Mirror Deployer
```

### Tagline (≤60 chars)
```
Reputation scoring for every pump.fun deployer wallet
```
(54 chars)

### Description (≤260 chars for the card preview)
```
Paste any pump.fun deployer wallet, get a 0–100 reputation score from on-chain history: graduation rate, rug rate, holder retention. Plus an AI thesis on archetype. Open-source, self-hostable. Helius-powered.
```
(225 chars)

### Long description (the body field)
```
WHY: Pump.fun signal asymmetry lives at the deployer, not the token. Same wallet ships 3 graduates → likely shipping a 4th. Same wallet rugged 5 times this week → don't ape. But there's no public reputation layer.

WHAT: Paste a Solana wallet, get:
• Reputation score (0–100), deterministically computed from on-chain history
• Archetype: Serial Graduate, Rug Pattern, One-Hit Wonder, Spray and Pray, Fresh Wallet
• Per-launch status: live, graduated, rugged, dead
• Risk flags: deployer dump, holder concentration, mint/freeze authority status
• Live feed of recent pump.fun launches with reputation overlay
• Leaderboard of top deployers

HOW: Helius RPC for chain data, pump.fun program ID parsing for launch/grad detection, rule-based score (transparent and reproducible) plus a GPT-4 thesis layer for the narrative read.

LIMITATIONS (because I'd rather you know upfront):
• Fresh deployers (<3 launches) score with low confidence — flagged explicitly
• PumpSwap migration handling is recent; edge cases possible
• Holder retention is snapshot, not time-series (v2 working on this)

OPEN SOURCE: MIT license, GitHub link below. Self-host with your own Helius key.

For anyone doing pre-buy diligence on pump.fun tokens — this is the workflow you're already doing manually, automated.
```

### Topics / Tags (pick 4)
```
Solana, Crypto, AI, Developer Tools
```

### Gallery (4–6 images needed — YOU need to create these)
1. Leaderboard view screenshot
2. Single deployer profile (good reputation example)
3. Single deployer profile (rug pattern example — instructive contrast)
4. Live feed with reputation overlay
5. (Optional) API endpoint demonstration in terminal
6. (Optional) Architecture diagram

### Maker comment (post within 5 min of going live)
```
Maker here. Built this after wasting 15 minutes every time I wanted to dig into a pump.fun token's deployer history.

Open question for the PH crowd: Mirror Deployer is the first of a planned three-tool sequence (next is a trader-marketplace layer, then a streamer/community surface). Curious which would be most useful to ship next — would love opinions if you have a strong take.

(Repo's MIT, link in description. Helius-powered if you want to self-host.)

— @yksanjo
```

### Hunter
If you can find someone with PH hunter status who'd hunt this, ROI is 2–5×. Won't bottleneck without one — many launches self-hunt successfully now.

---

## @yksanjo X launch-day thread

Pre-schedule everything in your scheduler. All times Pacific (PH timezone) — adjust to your local.

### T-12h (Monday evening) — pre-tease
```
Tomorrow morning, Show HN + Product Hunt for something I've been quiet about.

Built it because the same 15-minute pump.fun deployer-diligence ritual was driving me crazy.

Will tag here when live. 0700 PST.
```

### T-0 (Tuesday 00:01 PST / 08:01 UTC) — PH launch
```
Just launched Mirror Deployer on Product Hunt.

Paste any pump.fun deployer wallet → get a 0-100 reputation score from on-chain history. Graduation rate, rug rate, holder retention, time-to-bond. Deterministic scoring, no black-box AI.

If you do pump.fun diligence manually — this is your workflow in 10 seconds.

producthunt.com/products/mirror-deployer [link]

(MIT, self-hostable. Helius-powered.)
```

### T+5h (Tue 06:00 PST / 13:00 UTC) — HN submit
```
Show HN'ing Mirror Deployer now: news.ycombinator.com/item?id=[id]

Same project I PH'd this morning. HN crowd asks harder questions — interested in the methodology critique.

If you're around: would love your thoughts on the scoring breakdown in my first comment.
```

### T+6h — top-of-funnel push
```
The "deployer reputation" thesis in one sentence:

"On pump.fun, the wallet is the through-line — every token is just an instance of a deployer's pattern."

If you've ever pasted a wallet into solscan and counted graduations by hand — Mirror Deployer is that ritual, automated.
```

### T+8h — if on HN/PH front page, screenshot tweet
```
Mirror Deployer just hit [HN front page / PH top 10] 🪞

[screenshot]

If you're seeing this from HN/PH and want to dig into a specific deployer wallet, drop the address in a reply — I'll run the full profile and post it.

Open-sourced: github.com/yksanjo/mirror-deployer
```

### T+24h — recap thread
```
Mirror Deployer launch recap — 24 hours in.

📊 HN: [N upvotes, M comments, front page rank X]
📊 PH: [N upvotes, position X]
📊 GitHub stars: [delta]
📊 [Any KOL pickups, organic mentions]

Top discussion was [topic from comments]. Two things I learned: [insight 1], [insight 2].

Next: shipping [next milestone from feedback].

Thanks to everyone who voted, commented, ran wallets through it. 🪞
```

### Side note — When/how does $SOAG come up?
**On HN/PH: never.** Day 1 is mirror-deployer only.
**On X day 2+:** when someone asks "are you working on more like this?", reply with: "Mirror Deployer is the first of a three-tool sequence on the deployer-reputation thesis. Tools 2 and 3 are funded via $SOAG — agent suite token tied to the same project family. Optional, free to use the tools regardless."
**In TG:** $SOAG is freely discussed (it's already the official community group).

This separation matters. Day 1 is pure product credibility. Day 2+ is when the audience that found you organically gets the token context if they care.

---

## Total bundle of artifacts to commit + ready

| Item | Status | Owner |
|---|---|---|
| package.json identity removed | ✅ done | (me) |
| README LinkedIn removed + family links fixed | ✅ done | (me) |
| Live demo URL added to README | ⏳ pending | YOU (need to confirm hosted URL or set up Cloudflare Tunnel) |
| Screenshot in repo (public/screenshot.png) | ⏳ pending | YOU |
| Commit + push README + package.json changes | ⏳ pending | YOU |
| Tag v1.1.0 release on GitHub | ⏳ pending | YOU |
| Show HN submission (title + first comment) | ✅ drafted | YOU submits |
| Product Hunt submission (title, tagline, desc, maker comment) | ✅ drafted | YOU submits |
| X launch-day thread (5 tweets pre-scheduled) | ✅ drafted | YOU schedules |
| Gallery screenshots for PH (4–6 images) | ⏳ pending | YOU creates |

---

## What I need from you to fully prep

1. **Is mirror-deployer live at a public URL?** If yes, what is it? (so I can update README)
2. **Can you take 4–6 screenshots of the running app?** Or describe what's on each main screen and I'll write the alt-text + ordering for PH gallery.
3. **Pick a submission day:** Tue 2026-05-19 or Wed 2026-05-20?
4. **Do you have a PH "hunter" contact?** Not required, but ROI is 2–5× if so.

After you answer, I'll update the launch doc with the confirmed URL + screenshot references + final submission timestamps.
