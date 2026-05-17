# $SOAG Ops Dashboard — Bot Activation + Callouts, No Boost Spend

One-page operational scan. Read top-to-bottom every Monday.

---

## 1. KPI Benchmark Dashboard

**Current snapshot (2026-05-15) → 7d → 14d → 30d targets**

| Metric | NOW | 7-day target | 14-day target | 30-day target | Triggers what when hit |
|---|---|---|---|---|---|
| Market cap | $4.5k | **$10k** | **$25k** | **$75k** | $25k = CoinGecko submission viable; $75k = Tier 3 MM conversations possible |
| 24h volume | $5k | **$15k** sustained 3d | **$30k** sustained 5d | **$75k** sustained | $15k = bot min-volume filters pass; $30k = DEX Screener trending eligible; $75k = Birdeye trending eligible |
| LP depth | $5.3k (locked) | $7k | **$15k** | $30k | $15k = passes BONKbot/Trojan/Maestro liquidity filters |
| Holders | 202 | **250** | **350** | **600** | 100 already passed; 500+ = "established" tier on most bots |
| Top non-AMM holder % | 20.7% | <19% | <17% | <14% | <15% = distribution-flag heuristics relax |
| Unique buyers/24h | ~70 | 100 | 150 | 250 | 150+ = "active" tag on most aggregators |
| TG members | 15 | **40** | **80** | **200** | 100+ = community-signal triggers; 200+ = group becomes self-sustaining |
| Verified — Jupiter | ❌ | ✅ | ✅ | ✅ | Verified-only bot filters unlock |
| Verified — Birdeye | ❌ | ✅ | ✅ | ✅ | Birdeye trending eligibility unlocks |
| Verified — GeckoTerminal | ❌ | ✅ | ✅ | ✅ | CoinGecko aggregation pipeline unlocks |
| Solana FM listing | ❌ | ✅ | ✅ | ✅ | Alternative-explorer surface |
| Solscan metadata updated | partial | ✅ | ✅ | ✅ | Explorer-default trust signal |
| Solana Foundation directory | ❌ | submitted | listed | featured | Ecosystem-level discovery |
| KOL mentions/week (any tier) | 0 | **1** | **3** | **8** | Each mention = audience-tap event |
| Tier-S platform callout | 0 | 0 | 1 | 2 | LunarCrush surface, Solana Daily mention, etc. |
| Hummingbot self-MM running | ❌ | optional | ✅ | ✅ | Volume floor maintained mechanically |
| Cross-promo partnerships active | 0 | 1 negotiated | 2 live | 4 live | Compounding audience exchange |

**Refresh cadence:** Mondays. Paste current numbers in `~/launch-kit/kpi-log.csv` (create on first refresh). Trend > absolute — flat or down for 2 weeks = strategy reset.

---

## 2. Bot Activation Matrix

For each bot/aggregator, the activation threshold + the **free** action that triggers it. Ordered by leverage (highest impact first).

### Tier-A: Free verified-list unlocks (do this week, single biggest unlock)

| Bot / surface | Activation requirement | $SOAG status | Free unlock action | Time |
|---|---|---|---|---|
| **Jupiter aggregator UI** | On Jupiter Strict / Verified token list | ❌ Not listed | Open PR at `github.com/jup-ag/token-list` with logo, ticker, decimals, tags | 1h |
| **Phantom Wallet trending** | Token has Jupiter Verified status (Phantom reads Jupiter list) | ❌ | Same as Jupiter — one fix unlocks both | (see above) |
| **Birdeye verified filter** | Submitted token info, logo, socials verified | ❌ | birdeye.so → token page → "Update info" → fill form | 30min |
| **GeckoTerminal verified** | Submit token info form | ❌ | geckoterminal.com → token page → "Submit info" | 20min |
| **Solscan trust badge** | Submit metadata with creator-wallet signature | ⚠️ partial | solscan.io → token page → "Update info" → sign with `k6NEzy…` | 15min |
| **Bubble Maps cluster annotations** | Submit transparency labels for operational wallets | ❌ | bubblemaps.io → submit cluster context for your payout/agent wallets | 30min |

**Net effect of this row alone: $SOAG appears in 4 major aggregators' verified filters that currently exclude it. Every sniper bot using these as data sources gets you for free.**

### Tier-B: Threshold-gated bot pipelines (unlock as metrics grow)

| Bot | Threshold | Currently | Unlock path (free or near-free) |
|---|---|---|---|
| **BONKbot trending pool** | Verified + $25k LP + 100 holders + 100 buyers 24h | Fails LP + verified | Verify (Tier A) + Hummingbot floor + Holder Hunt buys |
| **Trojan trending tier** | Verified + $20k LP + 200 holders | Fails LP + verified | Same — verify + LP via organic + self-MM |
| **Maestro alerts** | $10k LP + mint/freeze revoked | Fails LP only | Add LP organically (Vault locks pull SOL in over time) |
| **Photon "user-boosted only" surface** | Verified + $5k LP | Fails verified | Verify on Jupiter — single fix |
| **Bullx trending** | $50k 24h vol | Fails | Hummingbot self-MM + Vault Gold weekend |
| **DEX Screener trending (algorithmic)** | 24h vol $30k + unique buyers >100 + age >24h | Fails vol + buyers | Vol via self-MM, buyers via Holder Hunt expansion |
| **Birdeye trending** | Top X by buy pressure (algorithmic) | Not trending | Real buy pressure from Vault Gold launch + jackpot weekend |

### Tier-C: Specialty surfaces (organic discovery, harder to engineer)

| Surface | What it does | How to get featured (free) |
|---|---|---|
| **GMGN.ai smart-money tracker** | Tracks "smart money" wallets; if they buy → algorithm surfaces | Get a smart-money wallet to buy organically (don't engineer; let Holder Hunt do it — if a smart-money wallet wins the puzzle, they hold $SOAG, GMGN picks up) |
| **DEX Screener "watchlist count"** | Tokens with high watchlist adds get surfaced | Ask Holder Hunt players to watchlist — single-line ask in TG |
| **LunarCrush galaxy score** | Social volume × engagement × influencer mentions | Drive @yksanjo posting cadence + cross-promo mentions (free) |
| **Jupiter trending (by Jupiter swap volume)** | Once verified, swap activity on Jupiter surfaces | Run a small portion of your Hummingbot orders through Jupiter (not direct PumpSwap) |
| **CoinGecko trending** | Page views + watchlists + portfolio adds | Listed first (need $50k liquidity typical) — then organic |

### Tier-D: Manual outreach surfaces (popular accounts who do callouts)

See Callout Targets section below.

---

## 3. Callout Target List — Popular Platforms & Users

Specific named accounts/platforms + the exact hook to pitch. All free / organic — no paid promo.

### Tier-S: Ecosystem-level (highest leverage if landed, hardest to crack)

| Target | Why they'd care | Hook | Channel |
|---|---|---|---|
| **@pumpdotfun** (official) | Reward builders shipping pump.fun-native tools | "Built Mirror Deployer — pump.fun deployer reputation feed. Built Holder Hunt — daily wallet-analysis game using pump.fun data via pumpscan. Both ship $SOAG rewards." | X DM, also @-mention with both repos linked |
| **Solana Foundation @SolanaFndn** | Highlight ecosystem builders | Submit at solana.com/ecosystem; tag in posts about agent suite | Submission form + X tag |
| **@SuperteamJP / Superteam Japan** | Tokyo-based Solana hub; Yoshi is Tokyo | "Tokyo-based, shipping 3-agent suite on Solana under $SOAG. Open to Superteam involvement." | DM + visit a Superteam JP meetup if held |
| **@aeyakovenko** (Anatoly) | Founder of Solana; reposts builders | One-shot tweet quoting his recent agent/pump.fun take + showing $SOAG agent suite as proof | Tweet with @mention, low expectation reply |

### Tier-A: pump.fun ecosystem analysts + Solana alpha accounts (most reachable)

| Target | Why they'd care | Hook |
|---|---|---|
| **@aplaceofmind1** | pump.fun analytics, posts about deployer behavior | "Built Mirror Deployer for the exact deployer-rep workflow you've covered. Want a free run on any deployer wallet you're curious about?" |
| **@gmgnaiagent** (GMGN) | Smart-money + on-chain analysis tool | "Mirror Deployer complements GMGN — you do post-buy tracking; I do pre-buy deployer rep. Cross-promo?" |
| **@notthreadguy** | Solana alpha; tries new tools | "Daily wallet-analysis quiz with $SOAG rewards. You'd be top of the leaderboard. Free to play." |
| **@ansiblelabs** | On-chain dev + Solana ecosystem | Mirror Deployer angle — they care about tooling |
| **@cyrii_mp** | Solana micro-cap alpha | Three-agent suite framing — fits the niche they cover |
| **@lupusvk** | Pump.fun trader, mid-tier | Holder Hunt game angle |
| **@kanyewesteros** | Solana commentary | Mirror Deployer demo on any wallet they pick |

### Tier-B: AI × Solana intersection (small audiences but high signal-to-noise)

| Target | Why they'd care | Hook |
|---|---|---|
| **@virtuals_io** ecosystem accounts | Agent tokens are their thesis | "Running Barutan agent locally on a Pi Zero 2W + Groq. Sovereign infra, $SOAG-gated TG access. Different stack from Virtuals — possible cross-feature?" |
| **@ai_agentcoin / Olas / Autonolas team** | Agent-token narrative | "Comparing infra approaches — would you want to feature Barutan as a sovereign-Pi example?" |
| **@YOPCommunity** | DeFi + agent intersect | Barutan + Holder Hunt as live agent demo |

### Tier-C: Solana newsletters + content platforms (free submission, weekly cadence)

| Platform | Submission path | What they want |
|---|---|---|
| **Solana Daily newsletter** | Submit at soldaily.io or DM editor | Newsworthy ships — Vault Gold tier launch is one |
| **The Daily Drop** | DM editor | New product launches |
| **BUIDLs on Solana** | Submit form | Open source repos with traction |
| **Solana Compass** | solanacompass.com | Ecosystem listing, free submission |
| **Helius blog** | Tag @heliuslabs with technical post | Dev content (agent infra on Pi) — they love this stuff |
| **QuickNode blog** | DM editor | Technical case studies |
| **The Block / Decrypt / CoinDesk small-scale section** | Cold pitch to ecosystem reporter | News hook needed (Vault Gold launch, agent suite milestone) |

### Tier-D: Live event surfaces (X Spaces, Discord/TG AMAs)

| Type | Examples | How to get on |
|---|---|---|
| **X Spaces (Solana-focused)** | Solana Builders Space, daily ecosystem spaces by mid-tier hosts | Reply to space host's tweet pitching your topic; DM host for guest slot |
| **Twitter community AMAs** | Your existing @yksanjo Twitter community + others | Host your own AMA in the SOAG community; ask to guest in others |
| **Telegram AMAs** | Pump.fun community TGs, Solana alpha TGs | Soft-ask admins after providing value in their group for 1–2 weeks first |
| **Podcast guest spots** | Lightspeed (Solana podcast), small Solana-focused shows | DM hosts when you have a launch news hook |

---

## 4. Weekly Rhythm — what to do every week to keep bots warm + callouts flowing

### Mondays
- [ ] Refresh KPI dashboard (paste current numbers in `kpi-log.csv`)
- [ ] Check Jupiter / Birdeye / Gecko / Solscan verification status (resubmit if rejected)
- [ ] Review Tier-A bot activation matrix — any new threshold crossed?

### Tuesdays
- [ ] Send 5 fresh KOL DMs using Pitch 2 from `SIGNALING-STRATEGY.md`
- [ ] Track responses in a sheet (column: name, date sent, response, follow-up)

### Wednesdays
- [ ] Cross-promo outreach — 2 fresh project DMs using Pitch 3
- [ ] Submit to 1 newsletter or Solana directory from Tier-C list

### Thursdays
- [ ] @yksanjo content: 1 thread per week tied to a real product event (lock tx, badge mint, payout tx)
- [ ] Repost / engage with anyone who mentioned $SOAG or any of the products

### Fridays
- [ ] Holder Hunt jackpot weekend kickoff (if running)
- [ ] One technical / dev post — agent infra, Barutan stack, Mirror Deployer methodology — for the Helius/QuickNode/dev-Twitter audience

### Saturdays
- [ ] Community engagement day: reply to every comment in $SOAG TG, host informal voice chat
- [ ] Post Saturday puzzle results + leaderboard

### Sundays
- [ ] Sunday puzzle + payout txs
- [ ] Week recap thread Sunday night with KPI deltas: holders +X, vol +Y, replies +Z
- [ ] Sunday night = best time for next-week KOL DM seeds (Monday morning replies)

---

## 5. The 5 highest-leverage actions you can take this afternoon

In priority order. Each one's free or under $50, takes <2 hours.

1. **Submit Jupiter token list PR** — `github.com/jup-ag/token-list` → fork → add `tokens/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump.json` with logo, symbol, decimals (6), tags `["solana", "agent", "pumpfun"]`. Most impactful single action available. Unlocks Phantom + Jupiter + multiple bot pipelines simultaneously. (45min including fork/PR mechanics)

2. **Submit Birdeye token info update** — birdeye.so/token/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump?chain=solana → "Update info" → fill in logo, X handle, TG link, description (Variant B from ARTIFACTS.md §3). (20min)

3. **Submit GeckoTerminal info** — geckoterminal.com → search token → "Submit info" link. Logo, socials, description. (15min)

4. **Submit Solana ecosystem directory** — solana.com/ecosystem → submit project. Lead with Mirror Deployer (most "useful tool" angle for ecosystem voters). (30min)

5. **Send Tier-A KOL DMs (3 of them)** — pick 3 from the Tier-A list (e.g. @aplaceofmind1, @notthreadguy, @cyrii_mp). Use Pitch 2 from SIGNALING-STRATEGY.md, customized per recipient. (30min for 3)

**Total time: ~2.5 hours. Total spend: $0. Net result: $SOAG visibility surface roughly 5× larger by tomorrow morning.**

---

## 6. What's deliberately NOT in this dashboard

- Paid Boosts on DEX Screener, Birdeye, Dextools — explicitly declined (you asked for the way around)
- Paid trending TG channel pushes — same
- Paid KOL tweets — replaced by product-led free KOL outreach in Pitch 2
- Wash trading via clustered wallets — declined (wash-tag risk on Mirror family cluster)
- Sybil holder farming — declined (RugCheck would catch + brand burns)

Everything in this dashboard is within the lines. The "find the way around" answer is **product depth + transparent infrastructure + free aggregator distribution + organic outreach** — not synthesized signal.
