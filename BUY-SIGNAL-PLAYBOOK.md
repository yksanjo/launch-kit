# Buy-Signal Tokenomics — what $SOAG needs to hit

How sophisticated Solana buyers actually decide. Concrete thresholds, your current state, and the math behind each target.

**Updated:** 2026-05-17 — based on live on-chain state.

---

## The 10-point checklist sophisticated buyers run

Every serious buyer of a sub-$1M Solana token runs this checklist (some explicitly via RugCheck/Birdeye/DexScreener filters, some by gut). A token that fails 2+ items gets skipped. **Tokens that pass all 10 are rare and stand out.**

| # | Signal | Threshold | Your state | Status |
|---|---|---|---|---|
| 1 | RugCheck normalised score | ≤100 (green) | 16 | ✅ |
| 2 | Mint authority revoked | null | null | ✅ |
| 3 | Freeze authority revoked | null | null | ✅ |
| 4 | LP locked or burned | yes | yes (graduation lock) | ✅ |
| 5 | Creator wallet holdings | <5% of supply | 0.42% | ✅ |
| 6 | Holder count | >200 | **239** | ✅ (just over the line) |
| 7 | Top 10 holders % | <50% (healthy), <30% (premium) | **99.3%** | ❌ |
| 8 | Top non-LP single holder | <10% | **20.7%** (the 207M vault) | ❌ |
| 9 | Total liquidity | >$10k | **$8.5k** | 🟡 marginal |
| 10 | 24h volume / liquidity | >0.5 | 0.56 | ✅ |

**Current grade: 7/10 pass, 2 fail, 1 marginal.** The 2 fails are concentration; the marginal is liquidity depth. Closing those is the unlock.

---

## What "buy signal" actually means at each tier

### Tier 0 — sub-$10k MC (where you are)
**Profile:** Brand new pump.fun graduate, thin liquidity, concentrated holders, no track record. Buyer assumption is "lottery ticket" not "investment."

What gets buyers in: vibes + creator narrative + community access. Mechanics don't matter much because the bet is on the human, not the token.

### Tier 1 — $30k–$100k MC (next 2–4 weeks target)
**Profile:** Survived the post-graduation dump, has a small dedicated holder base, some utility starting to ship.

What buyers check:
- Top 10 ≤ 70% (some distribution happened)
- 400+ holders
- $15k–$30k liquidity
- Visible burn proof (on-chain `spl-token burn` tx)
- Visible lock proof (Streamflow URL with countdown)
- 7-day holder count chart trending up

At this stage you get on DexScreener "trending" lists. Bot aggregators pick you up. Volume increases automatically.

### Tier 2 — $100k–$500k MC (3–6 months out)
**Profile:** Real micro-cap. Has product, has community, has weekly news. Becomes a "watch" coin, not a "skip" coin.

What buyers check:
- Top 10 ≤ 50%
- 1,000+ holders
- $50k+ liquidity
- Active utility loops (Holder Hunt + SOAG Vault paying out continuously)
- 30-day holder count up
- No single non-LP wallet >8%

Daily volume $5k+ becomes self-sustaining. You stop having to "push." Word-of-mouth + ecosystem traffic carries it.

### Tier 3 — $1M+ MC (the real prize)
**Profile:** Established ecosystem token. Cross-chain bridges become possible. Listing conversations open up.

What buyers check:
- Top 10 ≤ 40%
- 3,000+ holders
- $200k+ liquidity
- Daily volume $20k+
- No single non-LP wallet >5%
- Multiple active utility products
- KOL coverage organic, not paid

---

## The math behind each target

### Circulation — how much should be moving freely?

Not a single number — it's a **ratio of (LP + locked + burned) to total supply** that matters.

**Healthy structure for a $10k–$100k MC pump.fun graduate:**

| Bucket | % of supply | Why |
|---|---|---|
| LP (functionally locked) | 30–45% | Pump.fun graduation typically locks ~38% — yours is at 42% across both DEXes ✓ |
| Locked (Streamflow / vault, public unlock date) | 5–20% | Signals long-term skin in the game |
| Burned (on-chain `spl-token burn`) | 0.5–5% | Trust signal; permanent supply reduction |
| Creator wallet | <2% | <5% is fine, <2% is excellent |
| **Circulating (free float)** | **35–55%** | Enough for organic trading, not so much that any single sell crashes chart |

**Your stated model:** 42% LP + 3.5% locked + 0.3% burn + 0.4% creator = **53.8% free float**. Right in the healthy band.

**Your actual on-chain model:** 42% LP + ~21% in 207M vault + 0% real burn + 0.4% creator = **36.6% free float** (the rest is in 8 mystery wallets that *act* circulating but you don't know if they will).

That gap (54% vs 37%) is the trust gap. Closing it on-chain closes the buyer's mental model gap.

### Liquidity — how much SOL needs to be in the pool?

Think in terms of **what size buy can someone place without moving the chart more than 5%.**

| Liquidity | Max ~5%-impact buy | Buyer profile this attracts |
|---|---|---|
| **$5k** | ~$100 | "Memecoin gambler" — fine with 10–20% impact |
| **$10k** | ~$200 | Casual buyers; today's $SOAG threshold |
| **$25k** | ~$500 | Serious community members |
| **$50k** | ~$1,000 | Crypto Twitter mid-influencers |
| **$100k** | ~$2,500 | Small KOLs with paid promo budget |
| **$250k** | ~$6,000 | Sophisticated bag-builders, larger plays |
| **$1M** | ~$25,000 | Whales / institutional toes-in-water |

**Buy-signal threshold:** **$25k+ liquidity** is when a serious holder can confidently buy $500 without crashing the chart. Below that you're stuck in "lottery" mode.

**Math to get there:** going from $8.5k → $25k means adding $16.5k of liquidity. That's $8.25k of SOL (~50 SOL at current price) + matching SOAG from your wallet. **Cost: about 50 SOL** to get from "barely tradeable" to "buy-signal tradeable."

### Distribution — how spread out should holders be?

The key metric is **Gini-like concentration**, but the practical proxies are:

**Top N % targets at each tier:**

| | Tier 0 (current) | Tier 1 (~$30k MC) | Tier 2 (~$200k) | Tier 3 ($1M+) |
|---|---|---|---|---|
| Top 1 (LP-excluded) | 20.7% | <15% | <8% | <5% |
| Top 10 | 99.3% | <70% | <50% | <40% |
| Top 50 | ~99.5% | <90% | <75% | <65% |
| Holder count | 239 | 400+ | 1,000+ | 3,000+ |

The single biggest move: **break up holders #3–#10 (290M combined, 29% of supply).** If those 8 wallets distributed even half their holdings to 200+ new wallets via airdrops or rewards, you'd land in Tier 1 distribution in one move.

### Volume — what's "real" market activity?

**Volume / liquidity per day:**
- <0.2 → zombie chart, looks dead
- 0.2–0.5 → quiet but alive
- **0.5–2.0 → healthy, organic activity** (yours: 0.56 ✓)
- 2.0–5.0 → momentum push
- >5.0 → "something is happening" (FOMO or sell pressure)

Yours is already in the healthy band. The unlock isn't more volume — it's **bigger volume on more liquidity** so each unit of trading moves the chart less dramatically.

### Holder growth — leading indicator

Stagnant holder count = no organic flow. The chart can pump but if holders aren't growing, every uptick is a setup for a dump because existing holders are selling into thin demand.

**Healthy holder growth rates:**
- Tier 0–1: +5–20 holders/day (you're here)
- Tier 2: +20–100/day
- Tier 3: +100–500/day

Need to track this. RugCheck doesn't expose holder count history, but Birdeye and Dune do. Easy to script a daily snapshot from `getProgramAccounts`.

---

## How to actually get there — the next 4 weeks

### Week 1 (this week) — close the trust gaps

| Action | Effort | Impact |
|---|---|---|
| Real burn 3M SOAG via `spl-token burn` from your wallet | 2 min | Top 10 unchanged but on-chain proof unlocks "real burn" narrative |
| Identify what the 207M Meteora vault actually is (Streamflow? DAMM full-range LP?) and publish a one-pager | 1 hr | Removes the single biggest concentration unknown |
| If 35M lock isn't actually on-chain yet: lock 35M of community-held SOAG via Streamflow with 1-year unlock, post the link | 30 min | Tier 1 requirement for "visible lock proof" |
| Publish this playbook + the tokenomics report as a public musicailab.com/tokenomics page | 30 min | Beats sophisticated buyers to the punch — they read your tokenomics page instead of running RugCheck adversarially |

### Week 2 — break up holders #3–#10

The 8 holders with 290M (29%) are the single biggest concentration. Each one is yours to influence — they're early supporters / friends / sniper-bots from launch.

**Option A — voluntary partial distribution:** ask 3–4 of the friendly holders to airdrop, say, 10M each (40M total) to the top 100 Holder Hunt players + $SOAG TG members. Net effect: 4 wallets shrink by 80M total → 400+ wallets grow.

**Option B — incentivized re-distribution:** "Lock 50% of your bag in Streamflow for 6 months, get a Gold バルタン badge (2× Holder Hunt multiplier) + verified-OG status." Some of holders #3–#10 will take this trade.

**Option C — passive thinning:** as price runs up, holders #3–#10 will partially sell. Each sell is into the open market, which expands the buyer pool. This already started — today's 65% green day moved tokens from concentrated holders to new buyers.

You probably get to Tier 1 distribution by Week 2-end via A + C even if B doesn't land.

### Week 3 — deepen liquidity

**Path 1 — your SOL:** Add 10–20 SOL of your own from holdings to deepen PumpSwap LP. Cost: ~$2k. Effect: LP goes from $8.5k to ~$15-20k. Doesn't reach $25k target but gets close.

**Path 2 — community LP contributions:** offer "LP contributor" tier with badges (similar to Bronze/Silver/Gold from SOAG Vault). Pool community SOL into a multisig that adds to LP. Permanent benefit: those LP contributors share LP fees. **This is what serious community tokens do.** Requires building or finding a multisig LP pooling contract.

**Path 3 — wait:** if Tier 1 distribution + burn + lock all execute, MC grows organically to $30-50k, which lifts LP TVL passively. At $30k MC the LP would naturally be ~$25-30k without adding a single SOL.

Path 3 is free but slow. Path 1 is fast and small-cost. Path 2 is the right long-term answer.

### Week 4 — close on Tier 1

Goal state by 2026-06-14 (4 weeks out):
- Total supply: 997,000,000 (3M real burned)
- Top 10: ≤70%
- Top 1 (non-LP): ≤15%
- Holders: 400+
- LP: $20k+
- Active Streamflow lock visible
- Public tokenomics page

That state would get you on DexScreener trending (which auto-flows to bot aggregators), opening the next round of organic growth without paid promo.

---

## What buyers actually do — the mental model

When a $10k MC token shows up on a sophisticated buyer's screen, this is the literal 30-second decision tree:

```
1. RugCheck score?
   > 200  → SKIP
   ≤ 100  → continue
   
2. Mint/freeze revoked + LP locked?
   No     → SKIP
   Yes    → continue

3. Top 10 holders?
   > 80%  → "this is one whale + dust, dump risk too high" → SKIP
   60–80% → "concentrated but maybe early" → tentative
   ≤ 60%  → "distributed enough to play" → continue

4. Creator wallet?
   > 10%  → "dev rug risk" → SKIP
   ≤ 5%   → continue

5. Liquidity?
   < $5k  → "I'll move the chart 50% buying $500" → SKIP
   $5–25k → "small bet only" → tentative
   > $25k → "playable" → continue

6. Holder count vs age?
   < 100 holders, >7 days old → "dead, no organic flow" → SKIP
   > 200 holders → "alive" → continue

7. Volume / liquidity?
   < 0.2 → "no activity, will get stuck" → SKIP  
   ≥ 0.5 → "tradeable" → continue

→ At this point ~5% of all $10–50k MC tokens pass. The buyer reads
  the token's narrative, checks their Twitter, decides.
```

**You currently pass 1, 2, 4, 6, 7. You fail 3, are marginal on 5.** That's it — those are the only two blocks between you and the "playable" filter that gates ~95% of buyer attention.

---

## Single most important insight

**At your scale, concentration is the leverage point, not volume or marketing.** You can spend $1k on marketing and add ~100 holders. Or you can ask 4 friendly large holders to split their bags and add ~400 holders the same week, for free.

Distribution is the cheapest way to manufacture a buy signal. Burn + lock + LP depth are the cheapest *proofs* that what you're saying is true.

Everything else (Holder Hunt growth, badge tiers, weekly content) is downstream of these mechanics.
