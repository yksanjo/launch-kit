# Buy-Signal Tokenomics — what $SOAG needs to hit

How sophisticated Solana buyers actually decide. Concrete thresholds, your current state, and the math behind each target.

**Updated:** 2026-05-17 — based on live on-chain state via Helius RPC.

> *Note: an earlier version of this doc used RugCheck's stale holder data and incorrectly flagged a 20.7% concentrated holder. Live `getTokenLargestAccounts` data shows the actual distribution is much flatter — top 10 non-LP = 30.2%, top non-LP holder = 3.3%. This corrected version reflects on-chain reality.*

---

## The 10-point checklist sophisticated buyers run

Every serious buyer of a sub-$1M Solana token runs this checklist. A token that fails 2+ items gets skipped.

| # | Signal | Threshold | Your state | Status |
|---|---|---|---|---|
| 1 | RugCheck normalised score | ≤100 (green) | 16 | ✅ |
| 2 | Mint authority revoked | null | null | ✅ |
| 3 | Freeze authority revoked | null | null | ✅ |
| 4 | LP locked or burned | yes | yes (graduation lock) | ✅ |
| 5 | Creator wallet holdings | <5% of supply | 0.42% | ✅ |
| 6 | Holder count | >200 | 239 | ✅ |
| 7 | Top 10 non-LP % | <50% (healthy), <30% (premium) | **30.2%** | ✅ |
| 8 | Top non-LP single holder | <10% | **3.3%** | ✅ |
| 9 | Total liquidity | >$10k | $8.5k | 🟡 marginal |
| 10 | 24h volume / liquidity | >0.5 | 0.56 | ✅ |

**Current grade: 9/10 pass, 1 marginal.** The marginal is absolute liquidity depth. Closing that single gap moves you to 10/10 and unlocks DexScreener trending + bot aggregator pickup.

---

## What "buy signal" actually means at each tier

### Tier 0 — sub-$10k MC (where you are mechanically)
**Profile:** Brand new pump.fun graduate. Mechanics don't matter much — bet is on the human.

### Tier 1 — $30k–$100k MC (next 2–4 weeks target)
**Profile:** Survived post-graduation, dedicated holder base, utility starting to ship.

What buyers check:
- Top 10 non-LP ≤ 50% ← **you already pass at 30%**
- 400+ holders
- $15k–$30k liquidity ← **your one gap**
- Visible burn proof (on-chain `spl-token burn` tx)
- Visible lock proof (Streamflow URL with countdown)
- 7-day holder count trending up

At this tier you get on DexScreener "trending" lists. Bot aggregators pick you up.

### Tier 2 — $100k–$500k MC (3–6 months out)
- Top 10 non-LP ≤ 35%
- 1,000+ holders
- $50k+ liquidity
- Active utility loops (Holder Hunt + SOAG Vault paying out continuously)
- No single non-LP wallet >8%
- 30-day holder count up

### Tier 3 — $1M+ MC (the real prize)
- Top 10 non-LP ≤ 25%
- 3,000+ holders
- $200k+ liquidity
- Daily volume $20k+
- No single non-LP wallet >5%

---

## The math behind each target

### Circulation — how much should be moving freely?

| Bucket | % of supply | Yours today |
|---|---|---|
| LP (functionally locked) | 30–45% | **42%** (387M PumpSwap + 33M Meteora) ✓ |
| Locked (Streamflow, public unlock) | 5–20% | Pending verification |
| Burned (`spl-token burn`) | 0.5–5% | 0% on-chain (3M not actually burned yet) |
| Creator wallet | <2% | 0.42% ✓ |
| **Circulating free float** | **35–55%** | ~58% currently |

Your structure is right in the healthy band. Once the 3M is actually burned and 35M is locked, free float drops to ~54% — still healthy, and the lock/burn proofs become public trust signals.

### Liquidity — the single most important number for your tier

| Liquidity | Max ~5%-impact buy | Buyer profile |
|---|---|---|
| **$5k** | ~$100 | "Memecoin gambler" |
| **$10k** | ~$200 | Casual buyers |
| **$25k** | ~$500 | **Serious community members** |
| **$50k** | ~$1,000 | Crypto Twitter mid-influencers |
| **$100k** | ~$2,500 | Small KOLs |
| **$250k** | ~$6,000 | Sophisticated bag-builders |
| **$1M** | ~$25,000 | Whales |

**Your target: $25k.** Going from $8.5k → $25k means adding $16.5k of liquidity. At current price that's ~50 SOL plus matching SOAG (which you have).

Cheapest path: add 10–20 SOL of your own to PumpSwap. Cost ~$2k. Gets you to ~$15-18k LP. Organic MC growth lifts the rest.

### Distribution — already strong

**Top N % targets at each tier (non-LP):**

| | Tier 0 (current) | Tier 1 (~$30k MC) | Tier 2 (~$200k) | Tier 3 ($1M+) |
|---|---|---|---|---|
| Top 1 non-LP | **3.3%** ✓ | <8% | <6% | <5% |
| Top 10 non-LP | **30.2%** ✓ | <50% | <35% | <25% |
| Holder count | 239 | 400+ | 1,000+ | 3,000+ |

**You already meet Tier 2 distribution targets at Tier 0 MC.** This is unusual — most pump.fun graduates have to grow holder count and break up whale concentration simultaneously. You only need to grow holders. The flatness is already there.

### Volume — already healthy

Volume / liquidity per day:
- <0.2 → zombie
- 0.2–0.5 → quiet but alive
- **0.5–2.0 → healthy** (yours: 0.56 ✓)
- 2.0–5.0 → momentum push
- >5.0 → FOMO or sell pressure

You're solidly in the healthy band. Don't try to manufacture more volume — focus on growing the liquidity floor so existing volume creates less chart noise.

### Holder growth — leading indicator

- Tier 0–1: +5–20 holders/day (track this; aim for steady positive)
- Tier 2: +20–100/day
- Tier 3: +100–500/day

Easy to script: daily snapshot of `getTokenAccountsByOwner` count from Helius. I can build this into the weekly recap.

---

## The actual path to Tier 1 (2-4 weeks)

The good news: **the only mechanical lever you need to pull is liquidity.** Distribution is already there. Holder count is borderline acceptable. Burns + locks are credibility plays, not concentration plays.

### Week 1 (this week) — close credibility gaps

| Action | Effort | Cost | Impact |
|---|---|---|---|
| **Real burn 3M via `spl-token burn`** | 2 min | ~$0.01 fee | Supply drops to 996.99M. Tweet tx. "Burn" claim becomes real. |
| **Lock 35M via Streamflow with public link** | 30 min | ~$0.50 fee | "Lock" claim becomes real, with countdown URL. |
| **Add 10–20 SOL to PumpSwap LP** | 5 min | ~50% of 20 SOL impermanent loss risk (low for locked LP) | LP $8k → $15-18k. Doubles serious-buyer threshold. |
| **Publish tokenomics report as musicailab.com/tokenomics** | 30 min | $0 | Pre-empts sophisticated buyers running RugCheck adversarially |

### Week 2 — close Meteora dead-pool

Meteora has $660 of liquidity — too thin to route through. Either:
- **Deepen it to $5k+** (add ~$2k SOL + matching SOAG)
- **Close it** (withdraw your LP position, consolidate into PumpSwap)

Pick one. Two pools with one dead is worse optics than one healthy pool.

### Week 3 — grow holder count

The math: at 239 holders today, going to 400 in 2 weeks = need ~12 new holders/day.

Routes:
- **Holder Hunt acquisition loop**: every payout creates a new $SOAG holder. If Holder Hunt averages 5 winners/day, that's 35/week → easily 70+ new holders/week if winners haven't held before. Just verify they don't already hold.
- **Airdrop to Pump.fun community engagement**: holders of related pump.fun tokens, or members of your Holder Hunt TG, get 1k–10k $SOAG airdrops. Easy to script via existing sol-agent-wallet.
- **Cross-promo with other community tokens**: trade airdrop allocations with one or two friendly community tokens of similar size.

### Week 4 — close on Tier 1

Goal state by 2026-06-14:
- Total supply: 996,990,531 (3M real burned)
- Top 10 non-LP: still ~30% (no action needed)
- Holders: 400+
- LP: $20k+
- Active Streamflow lock visible at public URL
- Public tokenomics page live
- DexScreener trending eligibility unlocked

---

## What buyers actually do — the 30-second decision tree

```
1. RugCheck score?
   > 200  → SKIP
   ≤ 100  → continue                                  YOU: 16 ✓

2. Mint/freeze revoked + LP locked?
   No     → SKIP
   Yes    → continue                                  YOU: ✓

3. Top 10 non-LP holders?
   > 60%  → SKIP (whale + dust)
   40–60% → tentative
   ≤ 40%  → continue                                  YOU: 30% ✓

4. Creator wallet?
   > 10%  → SKIP
   ≤ 5%   → continue                                  YOU: 0.42% ✓

5. Liquidity?
   < $5k  → SKIP
   $5–25k → small bet only                           YOU: $8.5k 🟡
   > $25k → playable

6. Holder count?
   < 100 holders, >7 days old → SKIP
   > 200 holders → continue                          YOU: 239 ✓

7. Volume / liquidity?
   < 0.2 → SKIP
   ≥ 0.5 → tradeable                                  YOU: 0.56 ✓

→ At this point ~5% of all $10–50k MC tokens pass.
```

**You currently pass 1, 2, 3, 4, 6, 7. You're marginal on 5.** That's it — one gap between you and the "playable" filter that gates ~95% of buyer attention.

---

## Single most important insight (revised)

**You don't have a distribution problem. You have a liquidity-depth problem.**

The earlier read that you needed to break up whales was wrong — top 10 non-LP at 30% with no holder over 3.3% is structurally healthier than most $100k MC tokens. **Don't break up holders, deepen the LP.**

The other lever is credibility: the on-chain reality of the 3M burn and 35M lock doesn't match your public messaging yet. Closing that gap is cheap, fast, and converts buyer skepticism into buyer trust.

Everything else (Holder Hunt growth, badge tiers, weekly content) compounds on top of these two moves.
