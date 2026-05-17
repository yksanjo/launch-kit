# $SOAG Tokenomics Report — 2026-05-17

**CA:** `ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump`
**Decimals:** 6
**Pulled from:** RugCheck full report, DexScreener pairs API, Solana mainnet RPC
**Slot at pull:** 420,428,588

---

## TL;DR

| Field | Value |
|---|---|
| Total supply | **999,990,530.99 SOAG** (~1B, hard cap; mint authority null) |
| Mint authority | ✅ Revoked (null) — **no more SOAG can ever be minted** |
| Freeze authority | ✅ Revoked (null) — **no wallets can be frozen** |
| Metadata mutable | ✅ False — name/symbol/uri locked |
| Price | **$0.00001016** (PumpSwap) · $0.00001033 (Meteora) |
| FDV / Market cap | **~$10.2k** (FDV = MC since supply is fully diluted at mint) |
| 24h volume | **$4,765** ($4,640 PumpSwap + $125 Meteora) |
| 24h price | **+65.7%** PumpSwap, +63.0% Meteora (green day) |
| Total liquidity | **$8,568** ($7,907 + $661) |
| Holders ≥1% of supply | **10 wallets** holding ~99.3% combined |

**Hard read:** mint/freeze/metadata locked = trustless on the contract level. Concentration is extreme but most of it is locked-in mechanics (LPs + locked vault), not insider dumps. Price action this week is constructive but volume is still micro-cap thin.

---

## Supply distribution (verified on-chain)

| Wallet purpose | Address (token account / owner) | SOAG | % of supply |
|---|---|---:|---:|
| **PumpSwap LP** | `FvNrSc7...` / `8mqQqir...` | 386,985,013 | **38.70%** |
| **Meteora vault** (program `6EF8rrecthR5...`) ⚠️ | `aqdpUXM...` / `EcQSXKDEdw9J...` | 206,900,000 | **20.69%** |
| Unknown holder #3 | `Hsuo4mD...` / `6r6KkV4...` | 96,546,723 | 9.65% |
| Unknown holder #4 | `3fgehSx...` / `J4HfsbbfSHBZ...` | 52,421,876 | 5.24% |
| Unknown holder #5 | `9wj2yxR...` / `BM9CcyErJcu2...` | 46,405,959 | 4.64% |
| Unknown holder #6 | `HhVQYvq...` / `68oNcwFhBELR...` | 43,551,069 | 4.36% |
| Unknown holder #7 | `TzHHdmB...` / `Gw4pXupLbavW...` | 43,399,238 | 4.34% |
| Unknown holder #8 | `BAXUKW9...` / `2gMbnq9jh3zS...` | 39,866,147 | 3.99% |
| Unknown holder #9 | `coYjDfE...` / `9YSPXeHq6gdo...` | 39,015,753 | 3.90% |
| Unknown holder #10 | `4cSFEAz...` / `DGYvEpt76uRp...` | 37,926,234 | 3.79% |
| **Creator wallet** | `k6NEzyNUJRDjYydTZsnJSm8oBXTW59MmUF1wwJd2eyf` | 4,230,769 | 0.42% |

**Top 10 control ~99.3% of supply.** Of that:
- 38.7% is the PumpSwap LP token (functionally locked — LP can't withdraw on a pump.fun-graduated token)
- 20.7% sits in a Meteora program-owned vault (see ⚠️ below)
- 8 remaining unknown holders together control 39.9%

---

## ⚠️ Discrepancy vs your stated tokenomics

You told me:
- 3M SOAG burned
- ~35M locked for 1 year
- ~33M on Meteora LP

What I can verify on-chain:

| You said | Verified state | Status |
|---|---|---|
| 33M on Meteora LP | **32.1M** in the live Meteora DAMM v2 pair (`AayfP3k...`) | ✅ Matches (rounding) |
| ~35M locked 1 year | Largest single non-LP holder is **207M** in a Meteora-program-owned vault. No obvious 35M holder. | ❌ Doesn't match — either the lock is ~207M (6× what you said) or this 207M vault is something else |
| 3M burned | Total supply is **999,990,530.99** — i.e. only ~9,470 SOAG missing from a 1B cap. **The 3M burn does not appear in supply.** | ❌ Either the burn didn't go to the standard incinerator (so it's in a wallet, not removed from supply), or it hasn't been executed |

**Most likely explanations (best to test):**
1. The 207M holder = some combination of (a) lockup, (b) Meteora full-range provider position, (c) treasury. Owner program is `6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P` — that's a Meteora-family program, not Streamflow. If you used Streamflow for the lock, **the lock is elsewhere and may not have happened yet** — worth confirming in your Streamflow dashboard.
2. The 3M "burn" probably went to a custom dead-address wallet (not the canonical `1nc1nerator11111...`). That doesn't reduce supply — it just hides tokens in a wallet you don't control. On-chain `getSupply` still counts them. **To actually reduce supply, you have to call SPL Burn; sending to a dead address is not a burn.**

This is fixable — if you want a real burn, we can build a tx that calls `spl-token burn` and removes tokens from total supply. The market reads the on-chain supply, not the destination wallet.

---

## Effective circulating supply scenarios

### Scenario A — your stated numbers (35M lock + 3M burn)
```
Total                         1,000,000,000
- PumpSwap LP (functional)     -386,985,013
- Meteora LP                    -32,095,562
- Stated lock                   -35,000,000
- Stated burn                    -3,000,000
Circulating (your model)       ≈ 542,919,425 (54.3%)
```

### Scenario B — on-chain reality (treating 207M Meteora vault as locked, no burn)
```
Total                         1,000,000,000
- PumpSwap LP                  -386,985,013
- Meteora LP                    -32,095,562
- 207M Meteora vault            -206,900,000
- Creator (you, k6NEzy)          -4,230,769
Circulating (on-chain model)  ≈ 369,788,656 (37.0%)
```

**Either way the float is between 370M and 543M.** The market cap math is FDV-equivalent because supply is fixed and there are no future unlocks beyond what's in #2's vault.

---

## Liquidity & market microstructure

| Pair | DEX | SOAG side | SOL side | TVL | 24h volume | 24h price Δ |
|---|---|---:|---:|---:|---:|---:|
| `8mqQqir...` | **PumpSwap** | 386.99M | 45.74 SOL | $7,908 | $4,640 | +65.7% |
| `AayfP3k...` | **Meteora DAMM v2** | 32.10M | 3.80 SOL | $661 | $125 | +63.0% |
| **Total** | | | | **$8,568** | **$4,765** | |

**Slippage math:**
- A $200 buy on PumpSwap moves price ~2.5% (TVL/buy ratio).
- A $200 buy on Meteora moves price ~30% (very thin).
- Realistic max market-impact-free buy is ~$300 today.

**RugCheck normalised score:** 16/100 (lower = lower risk). One warn: "Low amount of LP Providers" — there is only 1 LP provider on the PumpSwap side (you, via graduation lock). That's structurally fine but adds a one-line concentration flag.

---

## Strengths

1. **Mint and freeze authority are revoked.** This is the single highest-leverage trust signal — you cannot rug-print, you cannot freeze a holder. Many memecoins this size still have these powers.
2. **Metadata locked.** Name/symbol/image cannot be changed.
3. **LP on PumpSwap is functionally permanent.** Graduation-locked LP tokens cannot be withdrawn by anyone. Whatever depth is there stays there.
4. **Volume is non-trivial relative to TVL.** 24h vol / TVL = 56% — for a $10k cap that's healthy turnover, not zombie chart.
5. **Two-DEX listing.** Most $10k caps are single-DEX. Being on PumpSwap + Meteora adds aggregator/index legibility (Jupiter routing, DexScreener trending eligibility).
6. **Creator (you) holds only 0.42%.** Compare to typical pump.fun graduates where the creator dumps 5–20%. You're well below threshold for "dev dump" suspicion.

## Weaknesses

1. **The "3M burn" isn't a real burn yet.** Total supply hasn't decreased. If you marketed it as a burn, the on-chain receipt doesn't support the claim — sophisticated buyers will check `getSupply` and call it out.
2. **The "35M lock" doesn't have an obvious on-chain proof.** Either the lock didn't happen, the number is wrong, or it's the 207M Meteora vault (in which case the marketing under-states it 6×).
3. **Holder #3–#10 are unidentified.** 290M (29% of supply) is in 8 wallets you presumably know but haven't documented. Some may be friends/community, some may be sniper-bots that bought at graduation. Worth labelling so the community can see "this is friend X, vested 6 months" vs "this is a sniper from launch."
4. **Liquidity is thin.** $8.5k is enough for community buyers but a single $1k buy moves the chart visibly. That's both a feature (low cap = upside) and a risk (any sell-side panic from holder #3 dumps the chart).
5. **Meteora pool has $660 of liquidity.** Too thin to be useful — anyone routing through Jupiter will use PumpSwap. Either deepen Meteora (more SOL) or close it to avoid the "two pools, one ghost" optic.

---

## What you can do this week

| Priority | Action | Why |
|---|---|---|
| **P0** | **Make the 3M burn real.** Call `spl-token burn` on 3M SOAG from your creator wallet (or any wallet you control). On-chain `getSupply` will drop to 997M. Tweet the SPL burn tx as proof. | Without this, "3M burned" is marketing not reality |
| **P0** | **Document the 207M Meteora vault.** Confirm what it is — if it's a 1-year lock you own, screenshot the Meteora vault UI showing the unlock date and post it. If it's a regular Meteora full-range LP, call it that. | This is 21% of supply with no public explanation |
| **P1** | **Label the other 8 top holders.** Drop a pinned tweet/TG post with "Holder X (43M) = friend, no plans to sell. Holder Y (39M) = vested 6mo." | Removes the "secret cabal" anxiety from new buyers |
| **P1** | **Deepen or close the Meteora pool.** $660 of liquidity attracts no real routing. Either add 10 SOL to bring it to a useful size, or wind it down. | Two pools with one tiny is a worse optic than one healthy pool |
| **P2** | **Publish this tokenomics report as a public doc.** Sophisticated buyers RugCheck before they buy. Beat them to the punch — link your own tokenomics page in the pump.fun description. | Trust signal; differentiates you from 99% of $10k caps |
| **P2** | **Wire a real lock if 35M isn't already locked.** SOAG Vault uses Streamflow — use the same infrastructure to lock another 35M of your own creator allocation (you have 4.23M, not enough — would need to source from somewhere). | Walks the "skin in the game" talk |

---

## What this report cannot tell you

- **Whether holders 3–10 are organic or sniper-bots from launch.** Possible to dig wallet-by-wallet (first-tx timestamp, source-of-funds, behavior pattern). Each one is ~10 minutes of work.
- **What the 207M Meteora vault unlock schedule is.** Depends on which Meteora primitive — DLMM, DAMM, Dynamic Vaults, AlphaVault each have different unlock semantics. Worth pulling the program account data to decode.
- **Whether the 24h +66% pump is organic or self-bought.** Looking at tx patterns (buy:sell ratio, wallet distribution of buyers) would tell you. Today it's 104 buys / 93 sells on PumpSwap — that's a *real* market with two-sided activity, not pure self-buying.

---

## Bottom line

$SOAG at $10k MC is **mechanically clean** (revoked authorities, locked LP, fixed supply) but has a **narrative-vs-reality gap** on the burn and the lock. Closing that gap with on-chain proof is the single highest-trust move you can make before the next push. Everything else (concentration, thin liquidity) is normal-for-stage and improves with growth.

> *Snapshot at slot 420,428,588. Re-run this report weekly during pushes to track holder churn and lock progress.*
