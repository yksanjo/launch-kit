# $SOAG Signaling Strategy — Without Burning Cash

The "find the way around" doc. Three goals, ranked by cost-efficiency:

1. **Get into bot/aggregator pipelines for free** (clean source data → bots scrape you for free, forever)
2. **Generate real price/volume signal without paid promo** (DIY self-MM + product-driven organic flow)
3. **Reach KOLs/MMs through product, not promotion** (response rates 10× higher than paid pitches)

Spend ceiling for this whole plan: ~$200 in optional listing/verification fees + ~$1k–5k in SOL working capital for self-MM (which stays liquid, not spent).

---

## Part 1 — Free signaling paths (where bots scrape from)

Every sniper/copy-trade bot scrapes the same 5–8 aggregators. Get into each one cleanly = perpetual free discovery. Each line below is a one-time submission, cost ≤ $50 or $0.

### Tier-A submissions (highest leverage, do this week)

| Surface | Cost | Submission path | What it unlocks |
|---|---|---|---|
| **Jupiter strong-pairs / token list** | $0 | github.com/jup-ag/token-list — open PR adding $SOAG with logo, ticker, decimals, tags | Verified badge in Jupiter swap UI. Every Solana wallet that uses Jupiter sees the verified mark instead of "unverified". Massive trust signal. |
| **Birdeye verification** | $0 | birdeye.so → token page → "Update info" → submit social links + logo | Verified badge on Birdeye + appears in their "verified tokens" filter. Bots filtering for verified-only see you. |
| **GeckoTerminal verification** | $0 | geckoterminal.com → submit token info form (linked from token page) | Verified mark + appears in CoinGecko aggregation pipeline. |
| **Solscan token metadata** | $0 | solscan.io → token page → "Update info" via creator-wallet signature | Logo + socials on the explorer most Solana traders use first. |
| **CoinGecko submission** | $0 | coingecko.com/en/coins/new → submit form | Liquidity threshold may block at $5k LP. Submit anyway; resubmit when LP grows. |
| **DexCheck.ai** | $0 | dexcheck.ai → "Add Token" form | Smaller aggregator but reads by some sniper bots. |
| **Bubble Maps** | $0 | bubblemaps.io → token analyzer auto-indexes; submit cluster annotations for transparency | Lets you proactively label your operational wallets (Holder Hunt payouts, sol-agent-wallet) — reduces the "insider network" interpretation. |

**One-shot DM I'll write you for any aggregator with no public submission form.**

### Tier-B submissions (medium leverage, do week 2)

- **Solana Foundation ecosystem directory** (solana.com/ecosystem) — free submission, takes 2–4 weeks to approve. Adds you to the official ecosystem list, which is what mid-tier KOLs scan for new projects.
- **CMC submission** (coinmarketcap.com/request) — liquidity threshold typically $50k. Submit when you cross.
- **Token Sniffer / GoPlus Security** — already auto-indexed, but verify your security badges are showing correctly.

### Why this stack matters

Sniper bots like **BONKbot, Trojan, Maestro, Photon, Bullx** all have a "verified-token-only" filter their power users enable. Tokens not on Jupiter/Birdeye/GeckoTerminal verified lists get filtered out before any human sees them. Currently $SOAG fails this filter on Jupiter and Birdeye — that's a massive invisible audience you're losing.

---

## Part 2 — Bot pipeline thresholds you currently miss (and how to cross them organically)

Sniper bots have minimum-liquidity, minimum-volume, minimum-holder filters. Once you cross each threshold, you appear in that bot's surfaced pool for free.

| Threshold | Typical value | $SOAG now | How to cross without paid promo |
|---|---|---|---|
| Min liquidity | $10k–25k | $5.3k | Add to LP yourself if PumpSwap allows post-grad adds; or wait for organic via Holder Hunt buys; or open secondary Raydium pool |
| Min 24h volume | $5k–25k | $5k | Holder Hunt + Vault generate ~$2–5k/day organic; self-MM (Part 4) adds floor |
| Min holders | 100–500 | 202 | Holder Hunt rewards distribute across new wallets; Vault locks create new holders |
| Min token age | 24h–7d | Already aged | ✅ Already passes |
| Min unique buyers 24h | 30–80 | ~70 | Already passes when game runs |
| Mint+freeze revoked | required | ✅ both revoked | ✅ Passes |
| LP locked | required | ✅ 100% locked | ✅ Passes |

**Honest read: you're passing 3 of 7 thresholds. The 4 you're missing are all liquidity-and-volume related, all addressable through Part 4 (self-MM) + Part 3 (organic from Vault/Holder Hunt).**

---

## Part 3 — KOL & cross-promo outreach (product-led, not token-led)

The standard pitch ("promote my token") gets ignored unless paid. The product-led pitch ("I built something you'd find useful — try it") response rate is 5–10× higher and creates organic token mentions naturally.

### Your three product hooks (in order of KOL-appeal)

1. **Mirror Deployer** — wallet reputation feed for pump.fun. Every alpha trader on Solana already manually checks deployer history. Mirror Deployer is the automated version. Strong KOL hook because **it makes their job easier**.
2. **Holder Hunt** — daily wallet-analysis game with $SOAG rewards. KOL hook: "interactive content my audience can participate in" — they tweet a screenshot of their score, audience engages, you get free distribution.
3. **Barutan agent** — Pi-hosted Groq-API agent in TG. KOL hook for AI-x-crypto accounts: "running on a $15 Raspberry Pi, fully local except inference." Novelty + dev-cred.

### Target KOL profile

- **5k–50k followers** (responds to DMs, not famous enough to charge premium rates)
- **Active engagement** (real replies, real ratios, not bots)
- **Posts about on-chain analysis or Solana ecosystem regularly**
- **NOT a paid-promo channel** (their feed isn't 90% sponsored — those don't move retail)

### Where to find them

- **GMGN.ai "smart money" wallets** → trace to X handles → check who's actually posting
- **Pump.fun "About to graduate" tab** → engaged commenters become candidates
- **Solana Daily / SolFlare / Solana ecosystem newsletter mentions** → people in the digest are reachable
- **Birdeye Top Traders weekly leaderboard** → many doxx X handles

### The cold DM (product-led, see also §Outreach Pitches below for the full template)

Lead with: "I built X. Here's the link. Free. If useful, would love a mention."

Never lead with: "Want to do a paid promotion?" — that filters out the 80% who'd organically tweet about it if you'd just shipped something good.

---

## Part 4 — Market Maker landscape + the workaround

### Realistic tiers at $5k MC

| Tier | Examples | Engages at $5k MC? | Cost if they did |
|---|---|---|---|
| **Tier 1** institutional | Wintermute, GSR, Cumberland, Jump, Jane Street | No | $50k+/mo retainer + 1%+ supply |
| **Tier 2** mid-market | Auros, Flowdesk, Amber, Kairon Labs, Pulsar | No | $20–50k/mo + token alloc |
| **Tier 3** growth/boutique | Empirical, Sigil, smaller Solana-focused | Unlikely (usually $100k+ MC min) | $5–15k/mo + 2–5% supply |
| **Tier 4** freelance MM operators | Found in Hummingbot Discord, MM TG groups, X DMs | Yes — they need clients | 3–10% supply + small SOL working capital + ~$500–2k/mo, often token-only |
| **Tier 5** DIY (self-MM) | You + Hummingbot on your Pi | Yes | ~$1–5k SOL working capital + 4–8h setup time |

**For $SOAG at current state: tier 1–3 won't engage. Choice is between tier 4 (cheap relative to size) and tier 5 (free, but you operate it). Tier 5 = "the way around" you asked for.**

### Tier 5: DIY Hummingbot self-MM — full setup

**What it does:** runs a market-making bot from your own server that places small 2-sided buy/sell orders on $SOAG continuously. Generates real volume, balances buy/sell pressure, keeps the chart "alive" so bot filters pass.

**What it costs:**
- Hummingbot software: $0 (open source, hummingbot.org)
- Infrastructure: $0 (use your existing Pi cluster or any VPS you have)
- Working capital: $1–5k worth of SOL + matched $SOAG (capital stays liquid in your wallets, not "spent")
- Time: 4–8 hours to configure + ongoing monitoring

**Critical wash-trading avoidance rules** (this is the line between MM and market manipulation):
1. **Use separate wallets for buy and sell sides.** Buy-side wallet only buys; sell-side only sells. Different funding sources.
2. **Tight spreads (0.3–1% each side).** Tight spreads = providing real liquidity. Wide spreads with quick fills = self-trading pattern.
3. **Small order sizes relative to LP depth.** Max 1–2% of LP per order. Larger = looks like a single actor.
4. **Realistic frequency.** Re-quote every 30–60 sec, not every second. Vary the cadence.
5. **Time-of-day variation.** Slower at 04:00 UTC (Asia overnight), busier at 14:00–22:00 UTC (US/EU active).
6. **Never close the round-trip on the same wallet within minutes.** Buy A, sell A from a different wallet, never re-buy with A.
7. **Document the operation publicly.** If asked, "yes, we run continuous MM via Hummingbot on disclosed wallets X and Y" is legitimate; hiding it and getting outed isn't.

**What it accomplishes:**
- 24h volume goes from $5k → $20–40k consistently
- Buys-to-sells ratio stays balanced (~50/50)
- Bot filters (volume, activity, recency) all pass
- Chart looks "alive" — no dead 6-hour gaps
- Sniper bots' minimum-volume thresholds clear

**What it does NOT accomplish:**
- Doesn't create real holder growth (you have to drive that via Holder Hunt + Vault)
- Doesn't move price up — MM is neutral by design; you'd need real buy pressure on top
- Can be detected if you're sloppy with wallet hygiene → wash-tag risk → which would propagate to the Mirror family cluster (see [[project-pumpfun-mirror-family]] reputation risk)

**Whether to do it:** I'd recommend **only after the foundation fixes from THREE-FIXES.md are done and Vault Gold tier ships**. Self-MM on a thin token with a dead community looks bad. Self-MM as one component of an active product-driven ecosystem with real Holder Hunt + Vault flow is normal MM behavior.

### Tier 4 alternative: freelance MM operator

If you don't want to operate Hummingbot yourself, hire someone who already does. They run their own Hummingbot setup, paid in token allocation + small SOL working capital. Cheaper than Tier 3 boutiques, faster setup than DIY.

**Where to find them:**
- **Hummingbot Discord** (#mm-services channel) — operators advertise services
- **TG groups: "Solana MM Services", "Crypto Market Makers"**
- **X DM**: search "Hummingbot operator" or "market maker for hire" — small operators post offers
- **Direct ask in Solana builder Discord channels** — Solana Builders, Superteam Discord

**Vet them:**
- Ask for past client list. Verifiable wallets, ideally tokens still alive
- Check their referenced wallets haven't been wash-tagged
- Ask for the exact wallet addresses they'll use for MM (so you can monitor)
- 30-day trial agreement before locking in 6 months

---

## Part 5 — Outreach pitches (paste-ready)

### Pitch 1 — Freelance / growth MM cold DM

For sending to Hummingbot operators, small MM boutiques, or X-found freelancers.

```
Hi [name],

Looking for a growth MM partner for $SOAG on Solana (PumpSwap pair).

Current state:
- MC: $4.5k, 202 holders, $5.3k LP — 100% locked at pump.fun graduation
- Mint authority + freeze authority both revoked
- RugCheck score 20/100 (lower = safer)
- Real product layer: Mirror Agent (wallet reputation tool), Holder Hunt (daily wallet-analysis game with $SOAG rewards), SOAG Vault (Streamflow lockup with soulbound Barutan-claw badges that multiply game payouts)
- Token CA: ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump

Looking for:
- 2-sided MM on PumpSwap pair
- ~$15–25k baseline daily volume floor
- Spreads ≤1% each side
- Wallet-disclosure to me (so I can monitor + publicly disclose MM ops)
- 30-day trial → 6-month if working

What I can offer:
- 3–5% token allocation, vested 6–12 months
- 5–10 SOL working capital from my side
- Performance bonus in token if we cross $50k MC

What's your rate card and minimum engagement?

— @yksanjo
```

### Pitch 2 — KOL product-led DM (Mirror Deployer hook)

For sending to small-to-mid Solana alpha accounts (5k–50k followers).

```
Hey [name],

Saw your thread on [recent on-chain analysis they posted]. Genuinely useful — bookmarked.

I built a tool you might want to add to your stack:

Mirror Deployer — paste a pump.fun deployer wallet, get a full reputation profile: token graveyard, success ratio, rug history, time-to-dump distribution. Free, no signup.

Link: github.com/yksanjo/mirror-deployer (or musicailab.com/mirror-deployer if hosted there)

I built it because diligence on pump.fun deployers takes 15+ minutes of solscan crawling per token. This is the same workflow in 10 seconds.

If it saves you time, would appreciate a mention — but only if it actually saves you time. No paid promo expected.

(Building a 3-agent suite on Solana under $SOAG — Mirror Deployer is the first. Token is incidental to the tool. Tool stays free regardless.)

— @yksanjo
```

### Pitch 3 — Cross-promo to other Solana micro-cap founder

For founders of other sub-$50k MC Solana projects with real products. Found via pump.fun "about to graduate" tab or DEX Screener boosted-tab filters.

```
Hey [name],

Caught [project name] on [where you found it]. Real product, real shipping — rare combo at this size.

I'm building $SOAG on Solana — three-agent suite (wallet rep tool, daily wallet-analysis game, vault with soulbound multiplier badges). Currently ~$5k MC like you, focused on product-led growth over paid promo.

Up for a cross-promo? Two formats:

1. Joint X space, 30–60 min, on a topic both our communities care about (on-chain alpha, agent tools, pump.fun ecosystem — pick one). We co-host, both communities show up, organic mention exchange.

2. Mutual tweet trade — I write a real thread about your project for my followers, you do the same for mine. Genuine threads only, no shilling.

No token swap, no money, no obligation. Just audience overlap because we're both shipping for the same kind of user.

Interested? If yes, what's your preferred channel for further discussion (DM, TG, Discord)?

— @yksanjo
musicailab.com | $SOAG
```

---

## Part 6 — Prioritized 14-day action list

What to actually do, in order.

### Week 1 (this week)
**Day 1 (free signaling foundation):**
- [ ] Submit to Jupiter token list (PR on GitHub)
- [ ] Submit Birdeye verification
- [ ] Submit GeckoTerminal verification
- [ ] Update Solscan token metadata
- [ ] Submit Bubble Maps cluster annotations for your operational wallets

**Day 2 (KOL outreach round 1):**
- [ ] Identify 10 target KOLs (5k–50k follower range, real engagement, Solana-focused)
- [ ] Send Pitch 2 (KOL product-led, Mirror Deployer hook) to all 10
- [ ] Track responses in a spreadsheet

**Day 3 (cross-promo round 1):**
- [ ] Identify 5 other Solana micro-cap project founders with real products
- [ ] Send Pitch 3 (cross-promo) to all 5
- [ ] Track responses

**Day 4–7 (organic ramp):**
- [ ] Vault Gold tier ships Tuesday — anchors the week
- [ ] Holder Hunt jackpot weekend Fri–Sun — drives buyer activity
- [ ] @yksanjo posts daily on-chain artifacts (lock txs, badge mints, payout txs)
- [ ] Run the week-2 calendar from ARTIFACTS.md §6

### Week 2
**Day 8–10 (MM decision):**
- [ ] Decide: DIY Hummingbot (Tier 5) or freelance MM (Tier 4)?
- [ ] If DIY: spin up Hummingbot config + 2 separate wallets, fund with ~$1k SOL each
- [ ] If freelance: send Pitch 1 to 3–5 candidates from Hummingbot Discord

**Day 11–14 (signaling ramp):**
- [ ] Hummingbot live (if DIY) — start with conservative spreads, monitor for wash-flag risk daily
- [ ] Re-audit DEX Screener and bot pipeline visibility
- [ ] Target: 24h volume floor $20k+, holder count 250+

### End of week 2 — decision gate
- All metrics hit → pilot push viable next week at $400–600 (per `PILOT-CHECKLIST.md`)
- Mixed → another organic week
- Misses → either deepen product layer or reconsider thesis

---

## Part 7 — What NOT to do (recap of declined approaches)

For the record:
- ❌ Wash trading from clustered wallets to fake volume → wash-tag risk, propagates to Mirror family cluster
- ❌ Sybil holder farming → flagged by RugCheck, kills credibility
- ❌ Buying TG bot "members" → tanks engagement ratio, gets group down-ranked
- ❌ Coordinated buys-then-sells timed to a paid push → market manipulation
- ❌ Hiding the self-MM operation → if discovered, kills brand. Disclose it openly.

All paths in this doc are within the lines. The "way around" paid promo is product-led + DIY infrastructure + transparent operations — not synthetic signal.
