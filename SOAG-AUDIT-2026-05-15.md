# $SOAG Phase 0 Audit — 2026-05-15

**CA:** `ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump`
**Pair:** `8mqQqir1iVjbFf5iiUxiAKu3TH2CDhB67cPgXHzbE8uL` (PumpSwap)
**Creator:** `k6NEzyNUJRDjYydTZsnJSm8oBXTW59MmUF1wwJd2eyf`

## Snapshot

| Field | Value | Read |
|---|---|---|
| Market cap | $4,531 | Micro-cap |
| FDV | $4,459 | Same as MC (full supply circulating) |
| 24h volume | $5,003 | Dead-token range |
| Liquidity (DEX Screener) | $5,307 | Below most sniper bot floors |
| Liquidity (RugCheck) | $2,676 | Discrepancy — may be LP-only vs combined |
| 24h price change | -5.23% | Slow bleed |
| 6h price change | +13.44% | Recent uptick |
| 1h price change | +12.73% | Possibly already-live pump? |
| 24h txns | 70 buys / 64 sells | Balanced, low absolute count |
| DEX | PumpSwap | Graduated, but not to Raydium |
| Raydium pool | null | Not on Raydium |
| Active Boosts | none | |
| ETI | logo present, website + community link set | Partially configured |
| Twitter | x.com/yksanjo (personal) | No project handle |
| Twitter community | i/communities/2038221752392712518 | Set |
| Telegram | **null** | **Not configured** |
| pump.fun replies | **0** | **Zero community engagement on launch surface** |
| KOTH | never hit | |
| pump.fun complete (graduated) | true | Already off bonding curve |
| Total supply | 1,000,000,000 | Standard pump.fun |
| LP locked % | ~~**0%**~~ → **100%** (corrected, see THREE-FIXES.md) | locked via pump.fun graduation |
| Mint authority | (not retrieved — Solscan gated) | |
| Holder count | (not retrieved — Solscan gated) | |
| RugCheck normalized score | 20 / 100 | Lower is better. 20 = low risk overall, but flags below |

### RugCheck flags
- **Low LP providers** (warn)
- **Low liquidity** $2,676 (warn)
- LP locked %: **0**

## Verdict — paid push is the wrong move RIGHT NOW

The pilot spec in `PILOT-CHECKLIST.md` assumed a baseline that doesn't exist. At current state:

1. **Sniper bots will filter $SOAG out automatically.** Most have minimum liquidity gates ($10k–25k) and require LP locked or burned. $5k LP + 0% locked = autoexcluded. Boosts will show the rocket on the chart but the bot pipeline they feed won't bite. Spend on Boosts here is largely wasted.

2. **A $940 pilot would move price 100–300% on $5k liquidity.** That looks like a single-wallet pump-and-dump to every aggregator's wash heuristic. Wash-flag risk on the chart, and worse, on the deployer wallet `k6NEzy…` — which is the same wallet running [[project-holder-hunt]] payouts and likely tied to [[project-mirror-deployer]]. **That's a Mirror family cluster contamination risk.**

3. **No Telegram + zero pump.fun replies + no project X handle.** Even if a Boost lands attention, there's nowhere to convert it. Buyers click through to a chart with $5k MC and no community, bounce immediately.

4. **Description is dev-personal, not product.** "I build agentic solutions for solana everyday" tells nobody why to hold $SOAG. Holder Hunt and SOAG Vault aren't mentioned. The two live products that should anchor the buy thesis are invisible.

5. **Token graduated to PumpSwap, not Raydium.** Most TG sniper bots and trending channels favor Raydium pairs. PumpSwap-only reduces the addressable bot audience by ~40%.

The pilot test would fail on Phase 0. Running it anyway burns $940 + signals weakness on-chain.

## Fix-first sequence (before any paid push)

Punch list in priority order. Spend on these first.

### F1. Add liquidity to LP — target $20k floor (CRITICAL)
- Current LP ≈ $5k. Bots filter under $10k–20k.
- Add ~$15k worth of paired liquidity (50/50 SOL + SOAG) to PumpSwap
- **Cost: ~$15k of capital, but it's still your capital in the LP — not spend**
- Risk: impermanent loss if SOAG drops further. Mitigate by deploying LP after F2 (lock) and F4 (community fixes) so the lock makes the buy-in real
- Alternative if you don't want to commit $15k: stage to $10k floor (~$5k additional), accept reduced bot coverage but still passes some filters

### F2. ~~Lock or burn the LP~~ — ALREADY DONE (CORRECTION)
- Full RugCheck report shows **LP 100% locked** via pump.fun graduation mechanism (LP mint `AYmfmrW7uXNdr8UkTHod9R9QiRR2wGhf2bJYKDjZ58vb`, all 4.19T LP tokens held by AMM, none withdrawable)
- The summary endpoint's `lpLockedPct: 0` was misleading. See `THREE-FIXES.md` for full explanation.
- **No action needed on locking.** Action shifts to: surface this everywhere (ETI, TG, X bio) since it's a strong buy signal you're currently hiding.

### F3. Create the Telegram community group (CRITICAL)
- pump.fun field is null. This is the #1 conversion surface for any future paid push.
- Required: a Group (not Channel) so members can talk, with a moderation bot (Combot or Rose)
- Pre-populate with: pinned message including CA, chart link, Holder Hunt link, Vault link, LP burn/lock tx, no-shill rules
- Bridge to existing Holder Hunt TG audience — they're already $SOAG-adjacent. **Do this first, free amplification.**
- Update pump.fun token + DEX Screener ETI with the TG link

### F4. Rewrite the token description (HIGH)
Current: "I build agentic solution for solana everyday https://github.com/yksanjo/sol-agent-wallet"

Suggested:
```
$SOAG powers Holder Hunt (daily on-chain prediction game) and SOAG Vault (Streamflow lockup + Barutan badges that multiply game payouts). Built by yksanjo, deployer of mirror-deployer. LP locked. Game live: t.me/<HOLDER_HUNT_TG>.
```

Update on: pump.fun page (if editable), DEX Screener ETI, Birdeye listing, the new TG pinned post.

### F5. Project X handle — keep yksanjo as dev brand, but consider a project handle (MEDIUM)
- Pros of separate handle: easier KOL referencing, clean "follow $SOAG for token news" surface, doesn't burn personal feed with promotional posts
- Cons: another account to maintain; yksanjo already has the credibility moat
- **Compromise: use the Twitter Community (already set, 2038221752392712518) as the project surface. Pin a single-source-of-truth tweet on the community.**

### F6. Verify on aggregators (MEDIUM)
- Apply for verified status on:
  - Jupiter strong-pairs list (free, submission form)
  - Birdeye verification (free)
  - GeckoTerminal listing
- Each adds a verification badge that snipers' filters pass

### F7. Generate organic activity for 7 days before any paid push (HIGH)
Even after F1–F6 the chart is currently silent. Build a baseline of organic buyers/holders so the pilot push has a starting platform to amplify.

- Run a **Holder Hunt special jackpot week** — drives game-driven buying
- Launch **Vault Gold tier** — drives lockup-driven buying
- Post daily from @yksanjo with on-chain artifacts (lock tx, badge mints, puzzle results)
- Target: 24h volume to $25k+ floor and holder count visible growth for 5+ consecutive days before paid push

## Revised sequence

1. **This week:** F1, F2, F3, F4 (the four CRITICAL/HIGH items that cost <$15k LP + $0 ops)
2. **Week 2:** F5, F6, F7 (organic activity baseline week)
3. **End of week 2:** Re-audit. If 24h volume sustains >$25k organically and holder count > 200 with top-10 < 35%, foundation is ready.
4. **Week 3:** Run the pilot push per `PILOT-CHECKLIST.md` against the now-healthy baseline.
5. **Week 4:** Scale if pilot passes.

This is slower but the dollar efficiency is 5–10× better. A pilot on the fixed baseline can pass. A pilot now will fail and waste $940.

## If you want to push anyway

I'd advise against, but if there's a deadline or strategic reason (e.g. you need a chart event this weekend for a presentation/community moment), the minimum-viable version:

- Skip Boosts entirely (waste on this LP depth)
- Spend the $940 on: $400 to add to LP, $300 single mid-tier KOL who'll mention the Holder Hunt/Vault story (not just the chart), $240 reserved for second post 48h later
- Accept this is brand-building spend, not chart-pumping spend
- Don't trigger any wash heuristics with timed buys from related wallets
