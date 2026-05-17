# $SOAG Re-Push Playbook

Overlay on `LAUNCH.md`. Re-push of an existing token, not a fresh launch — different mechanics.

**Why this is different from a graduation launch:**
- No deploy / graduation attention concentration moment to capture
- Chart already has history — buyers see prior pumps/dumps before deciding
- Holder distribution is already what it is
- Existing community baseline (Holder Hunt players, Vault stakers)
- ETI / RugCheck / Birdeye listing may already exist — check before paying twice

**Why a re-push works for $SOAG specifically:**
- Real product utility live: Holder Hunt (daily game) + SOAG Vault (Streamflow lockup, Barutan badges)
- Cross-product flywheel ready to amplify any push
- yksanjo / mirror-deployer reputation cluster intact

---

## Phase 0 — Audit current state (do this BEFORE spending anything)

Manual checks — paste results back:

- [ ] **Current MC + 24h volume** — `dexscreener.com/solana/<SOAG-CA>` — screenshot
- [ ] **Holder count + top 10 concentration** — `solscan.io/token/<SOAG-CA>#holders` — top 10 % of supply
- [ ] **Existing ETI status** — does the token page on DEX Screener show logo, socials, description? If yes, ETI already paid. If no, $299 line item.
- [ ] **RugCheck score** — `rugcheck.xyz/tokens/<SOAG-CA>` — green/yellow/red
- [ ] **GoPlus status** — `gopluslabs.io/token-security/sol/<SOAG-CA>` — flagged fields
- [ ] **Birdeye listing** — `birdeye.so/token/<SOAG-CA>?chain=solana` — present + has logo?
- [ ] **Jupiter strong-pairs** — is it listed in Jupiter UI as a strong pair, or buried in unverified?
- [ ] **Active holders making moves last 7d** — solscan transfer count. If 90% of holders are dormant, push will fizzle.
- [ ] **Existing Boost count visible on DEX Screener** — if there's any rocket, note it. Snipers see momentum stacking.

Anything red here gets fixed before promo spend. RugCheck/GoPlus red = no paid push works.

---

## Phase 1 — Pick a synthetic moment

A re-push without a narrative reason reads as a desperate pump. Tie the push to a real event so the chart action has context. Candidates ranked by leverage:

1. **Vault badge tier launch / new tier** — "Gold badges now live, multiplier 2.0× active for Holder Hunt." Forces existing holders to lock more $SOAG to upgrade. Drives buy pressure organically.
2. **Holder Hunt jackpot round** — "10× pot weekend, top 3 split 50k $SOAG." Drives both buys (to enter) and existing-holder retention.
3. **mirror-deployer reputation feed milestone** — "X deployers indexed, top-rated deployer reveal." Cross-product attention bleed into $SOAG.
4. **Partnership / integration** — only if real (e.g., another pump.fun tool indexing into Holder Hunt). Don't fake.
5. **On-chain milestone** — "X% of supply locked in vault" or "Y holders." Only works if numbers are genuinely impressive.

**Recommendation: option 1 or 2.** Both are 100% in your control, both produce real on-chain activity, both create a story for KOLs/channels to actually post about (not just "buy this token").

---

## Phase 2 — Pilot push ($500–800)

Calibrate before committing. Single tight test, measure response.

### Pilot spec
- **30 DEX Screener Boosts**: ~$240
- **1× TG channel push (best-scoring channel from `channel-tracker.csv`, or test one cold)**: $200–400
- **1× mid-tier KOL tweet (5–20k followers, real engagement)**: $150–300
- **Pre-warmed X thread from `@yksanjo`** tying the synthetic moment to the moment of paid spend

Total: ~$590–940

### Pilot timing
Fire all three in a 15-min window. Synthetic moment (e.g., badge launch tx, jackpot announcement) happens 5 min before paid spend goes live so the narrative is on-chain first, paid amplification second.

### Pilot success criteria (measure at T+2h)
| Metric | Pass | Fail |
|---|---|---|
| Volume in pilot 2h vs 24h prior avg | ≥ 5× | < 3× |
| Unique buyers | ≥ 40 new wallets | < 20 |
| Holder count change | +20 or more | flat/negative |
| TG community joins | +15 | < 5 |
| X impressions on thread | ≥ 8k | < 3k |
| Top 1 buyer % of pilot volume | ≤ 15% | > 30% (concentrated = manipulation-looking) |

**3+ pass → scale to Standard ($5k) tier on same setup, different channels.**
**2 pass, 4 fail → fix the synthetic moment (the story isn't landing) before spending more.**
**0–1 pass → stop. The audience isn't there right now; spend goes to community/product instead.**

---

## Phase 3 — Scaled push (only if pilot passes)

Use the master LAUNCH.md timing playbook with these adjustments:

- **No T-0 graduation moment** → use the synthetic moment time as your T-0
- **Pre-tease 24h ahead from @yksanjo** — the synthetic moment is announced, buyers self-position
- **First Boost wave fires at synthetic-moment timestamp**, not deploy timestamp
- **Reserve a third of budget for T+24h re-push** if first wave holds — re-push of a re-push works once if the first held its chart, signals sustained momentum

---

## Phase 4 — Cross-product handoff (compounds for free)

Already-live products = free amplification surface:

- **Holder Hunt puzzle on push day** references the synthetic moment in the puzzle theme. Game players see it organically in TG.
- **SOAG Vault dashboard banner** highlights the moment. Existing stakers see it on session start.
- **Mirror Deployer feed** — if applicable, surface that the $SOAG deployer is the same as mirror-deployer's deployer (you), with the clean track record.
- **yksanjo X handle** runs the narrative in parallel — vault locks visible on-chain, screenshot the lock tx, post it.

The point: paid promo gets attention to the token page; your own products convert that attention into action. Without the product layer, paid promo is a leaky bucket.

---

## $SOAG-specific timing options

Pick based on where the audience-overlap is strongest:

| Window | UTC | Why | Tradeoffs |
|---|---|---|---|
| **Sat 18:00 UTC** | Sat 18:00 | Peak global retail; US afternoon, EU evening, JP Sun morning. Sniper bots fully active. | High KOL competition for slots; expensive |
| **Sun 14:00 UTC** | Sun 14:00 | Lower KOL competition; US Sun morning coffee; quieter chart, easier to dominate trending | Lower total retail volume; bot-heavy |
| **Tue 20:00 UTC** | Tue 20:00 | Mid-week serious-buyer window; less degen, more "real" capital | Lower meme-energy; not ideal for $SOAG vibe |
| **Asia window 02:00 UTC** | Sun-Mon 02:00 | JP/KR awake; SOUNDRAW network adjacency; almost no western sniper competition | Smaller addressable audience |

**Recommendation for $SOAG: Sun 14:00 UTC.** Holder Hunt is a daily game with global players already in TG; Sun midday US gives the synthetic moment full Sunday attention and lets the chart hold into Monday US open without being immediately dumped.
