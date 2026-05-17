# $SOAG Pilot Push — Single-Page Run Sheet

> ⚠️ **2026-05-15 audit run.** Foundation not ready for a pilot push at current state ($4.5k MC, $5.3k LP, 0% LP locked, no TG, 0 pump.fun replies). See `SOAG-AUDIT-2026-05-15.md` for diagnosis + fix-first sequence. **Do F1–F4 + F7 first, then revisit this checklist in ~2 weeks.**

Print or pin this. Total spend cap: $940.

## Pre-pilot (T-24h)

### Phase 0 audit — paste results below
- [ ] $SOAG CA: ____________________________________________
- [ ] Current MC: _________ | 24h vol: _________
- [ ] Holder count: _______ | Top 10 % of supply: _______
- [ ] ETI already paid? Y / N
- [ ] RugCheck score: Green / Yellow / Red
- [ ] GoPlus flagged fields: __________________
- [ ] On Birdeye w/ logo? Y / N
- [ ] Existing Boost count: _______
- [ ] Active holders (7d transfers > 0): _______ of _______ total

### Anything red → fix first
- [ ] If ETI not paid: pay $299 to DEX Screener (still useful even pre-pilot)
- [ ] If RugCheck red: fix and resubmit before any spend
- [ ] If concentrated (top 10 > 40%): pilot will be hard to land — note risk

### Synthetic moment locked
- [ ] Moment: __________________________ (e.g. "Vault Gold tier launch")
- [ ] On-chain tx required at T-5min: __________________________
- [ ] Pre-tease tweet drafted from @yksanjo
- [ ] Pre-tease scheduled for T-24h

### Slots booked
- [ ] TG channel: _____________ | rate: $_____ | confirmed time: _____ UTC
- [ ] KOL: _____________ | followers: _____ | rate: $_____ | confirmed time: _____ UTC
- [ ] Promo wallet funded with: _______ SOL (covers all line items + 20% buffer)
- [ ] Promo wallet is CLEAN (no Mirror family on-chain link)

---

## Pilot execution (T-15min → T+2h)

### T-15min
- [ ] Phantom unlocked, promo wallet selected
- [ ] dexscreener.com/boost open
- [ ] X compose window open with launch-moment tweet pre-loaded
- [ ] Solscan tab open on $SOAG to verify the synthetic-moment tx lands

### T-5min — synthetic moment goes on-chain
- [ ] Execute moment tx (e.g. badge mint, jackpot fund tx)
- [ ] Verify tx confirmed on solscan
- [ ] Screenshot tx hash for thread

### T-0 — paid spend goes live
- [ ] Buy 30 DEX Screener Boosts (~$240)
- [ ] TG channel admin posts push (you sent payment + copy earlier)
- [ ] KOL tweets (you confirmed timing earlier)
- [ ] Post X thread from @yksanjo — moment + tx screenshot + CA + chart link

### T+15min
- [ ] Reply to top 5 X replies on the thread
- [ ] Pin moment-tx in TG community
- [ ] Note any KOL/sniper accounts that quoted/retweeted — these are warm for next push

### T+30min — first read
- [ ] Volume vs 24h prior avg: _____× (need ≥5× to pass)
- [ ] Holder count delta: +_____
- [ ] TG community joins: +_____

### T+2h — pilot scorecard
| Metric | Result | Pass? |
|---|---|---|
| Volume vs 24h prior avg | _____× | ≥5× |
| Unique new buyers | _____ | ≥40 |
| Holder count Δ | _____ | ≥+20 |
| TG joins | _____ | ≥+15 |
| X thread impressions | _____ | ≥8k |
| Top 1 buyer % of pilot volume | _____% | ≤15% |

**Passes (≥3): SCALE** → run Standard $5k playbook within 48h on different channels.
**Mixed (2): FIX STORY** → synthetic moment didn't land. Try different moment.
**Fails (≤1): STOP & REINVEST** → audience not there. Push budget into product (next vault tier, Holder Hunt feature) instead.

---

## Post-pilot

- [ ] Log every TG channel + KOL result in `~/launch-kit/channel-tracker.csv`
- [ ] Update positioning if any line landed unusually well in replies
- [ ] Decide scale vs hold within 24h while data is fresh
