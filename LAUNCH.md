# Launch Kit — pump.fun → Raydium graduation playbook

Drop-in playbook for any Mirror family / $SOAG-adjacent launch. Fill placeholders, work top-down on launch day. Designed for sanctioned promo only.

**Placeholders to fill before T-24h:**
- `{{TICKER}}` — token ticker (e.g. SOAG, MIRR2)
- `{{CA}}` — contract address (post-deploy)
- `{{PUMPFUN_URL}}` — pump.fun/<CA>
- `{{X_HANDLE}}` — project X handle
- `{{TG_GROUP}}` — community TG link
- `{{ONE_LINER}}` — 80-char positioning line
- `{{TARGET_GRAD_TIME}}` — UTC datetime you're aiming for graduation
- `{{LAUNCH_WALLET}}` — clean burner wallet funded for promo spend
- `{{TOTAL_BUDGET_SOL}}` — total promo SOL allocated

---

## 1. T-minus checklist

### T-7d (pre-deploy, brand + infra)
- [ ] Decide ticker, ensure no collision on pump.fun search + Solscan
- [ ] Reserve X handle, set bio + pinned post placeholder
- [ ] Create TG community group (not just channel) with bot moderation
- [ ] Logo at 512×512 PNG transparent — keep file path here: `~/launch-kit/assets/{{TICKER}}-logo.png`
- [ ] Banner 1500×500 for X
- [ ] Generate clean burner wallet `{{LAUNCH_WALLET}}` — never touched by personal funds; fund only from a fresh CEX withdrawal or a wallet with no Mirror family history (protects [[mirror-deployer]] reputation cluster)
- [ ] Test-fund with 0.1 SOL, verify in Phantom, then top up to `{{TOTAL_BUDGET_SOL}}`

### T-48h (positioning lock)
- [ ] Final `{{ONE_LINER}}` (see Section 4 for templates)
- [ ] Pin tweet on `{{X_HANDLE}}` previewing the drop — no CA yet, just thesis
- [ ] DM 3–5 KOLs to lock in timing (see Section 5 KOL DM)
- [ ] DM 2–3 TG channels to lock paid slots at T-0 and T+15min (see Section 5 TG pitch)
- [ ] Pre-write the launch X thread, leave only CA + pump link blank
- [ ] Draft RugCheck + GoPlus submission packets (you submit them at T-0 once CA exists)

### T-24h (final pre-flight)
- [ ] Confirm wallet has SOL: ETI ~1.7 SOL ($299), 200 Boosts ~2 SOL, Birdeye ~1 SOL, KOL fees, TG slots, +20% buffer
- [ ] Confirm KOLs received final copy and assets
- [ ] Confirm TG channels confirmed time + paid (most want payment upfront)
- [ ] Set 3 alarms: T-1h, T-0, T+15min
- [ ] Close out unrelated tabs/sessions — launch day is a 4-hour focus block

### T-6h (warming)
- [ ] Soft tease tweet from `{{X_HANDLE}}` — no CA, just "today"
- [ ] Re-confirm KOL + TG window with one-line ping
- [ ] Verify pump.fun bonding curve target (~$69k MC for Raydium grad — check current threshold, it changes)
- [ ] If launching token now: deploy to pump.fun. If already on curve: monitor MC

### T-1h (final checks)
- [ ] Have these 6 tabs open and tested:
  1. pump.fun token page
  2. DEX Screener (will show post-grad)
  3. Birdeye token page
  4. dexscreener.com/boost
  5. RugCheck submission form
  6. X compose window with thread pre-loaded
- [ ] Phantom unlocked, wallet selected
- [ ] Reply-guy friends pinged to be online at T-0

### T-0 — GRADUATION MOMENT
- [ ] Submit RugCheck + GoPlus (do this FIRST — sniper bots check these before buying)
- [ ] Pay DEX Screener ETI ($299) — unlocks logo, socials, description
- [ ] Buy 100 Boosts on DEX Screener
- [ ] Buy Birdeye trending boost (parallel tab)
- [ ] Post launch X thread with CA + pump link + DEX Screener link
- [ ] KOL tweets fire (you confirmed timing T-1h)
- [ ] First TG channel push fires
- [ ] Pin CA in TG community

### T+15min
- [ ] Second 100 Boost wave on DEX Screener
- [ ] Second TG channel push (different channel — see Section 6 scorecard)
- [ ] Reply to top 3 X replies on launch thread
- [ ] Screenshot the chart for the "we're trending" follow-up tweet

### T+60min — DECISION GATE
**Read the chart honestly. If unique buyers > 80, organic replies on the thread, holder count growing without single-wallet concentration → continue. If not → stop spending.**
- [ ] If green: third Boost wave + second KOL tweet
- [ ] If red: stop promo spend, focus on community + product. The product (Holder Hunt, Vault) carries from here

### T+4h
- [ ] Trending placement on Dextools or Birdeye if momentum sustained
- [ ] Long-form tweet with chart screenshot + product roadmap reminder
- [ ] AMA scheduled in TG for T+24h

### T+24h
- [ ] Boost decay complete — evaluate re-up vs hold
- [ ] Begin cross-product audience handoff (see Section 7)

---

## 2. Wallet hygiene (protect the Mirror family cluster)

Your reputation moat is that wallets traceable to your launches stay clean. Wash-tag on one wallet propagates to every wallet in its funding graph.

**Rules:**
1. `{{LAUNCH_WALLET}}` is single-use. Burn after launch — don't reuse for next launch.
2. Fund it from: (a) a fresh CEX withdrawal, or (b) a wallet that has zero on-chain connection to Mirror family operations
3. Never bridge from a wallet that's a holder of any Mirror family token — that connects the graph
4. Never use the deployer wallet to buy your own boosts or pay TG channels — buy-side flow from deployer is the #1 wash-flag heuristic
5. After launch, drain remaining SOL to a fresh wallet, not back to the source

**Three-wallet pattern for clean ops:**
- **Deployer wallet** — only deploys, nothing else. Receives only the deploy fee.
- **Promo wallet** (`{{LAUNCH_WALLET}}`) — buys Boosts, pays channels, pays KOLs. Burned after.
- **Team/treasury wallet** — receives any team allocation. Cold storage, no activity.

---

## 3. Budget allocation templates

### Conservative ($3k = ~17 SOL @ $175)
- ETI: $299 (1.7 SOL)
- DEX Screener Boosts (200 total, two waves): ~1.6k (9 SOL)
- Birdeye Boost: ~$400 (2.3 SOL)
- 2× TG channel pushes: ~$400 (2.3 SOL)
- 1× KOL tweet: ~$300 (1.7 SOL)

### Standard ($5k = ~28 SOL)
- ETI: $299
- DEX Screener Boosts (300, three waves): ~$2.4k
- Birdeye Boost: ~$500
- 3× TG channel pushes: ~$800
- 2× KOL tweets: ~$700
- Reserve for trending placement: ~$300

### Aggressive ($8k = ~46 SOL)
- ETI: $299
- DEX Screener Boosts (500, three waves): ~$4k
- Birdeye Boost: ~$800
- 4× TG channel pushes: ~$1.2k
- 3× KOL tweets: ~$1k
- Dextools Hot Pairs slot: ~$500
- Reserve: ~$200

**Gate rule: half the budget reserved past T+60min decision gate.** If the launch is dead, the second half doesn't go anywhere.

---

## 4. Positioning one-liners (pick one, edit)

For Mirror family / reputation tokens:
- `{{TICKER}} — the on-chain receipt for [specific behavior]. Built by the team behind mirror-deployer.`
- `Reputation has weight. {{TICKER}} makes it tradeable.`
- `If you've used mirror-deployer, you already know why {{TICKER}} matters.`

For utility tokens with product:
- `{{TICKER}} powers [specific product]. Hold to [specific benefit]. No promises about price.`

For meta-riding:
- `[Meta name] needs an index. {{TICKER}} is it.`

**Avoid:** "revolutionary", "first ever", "to the moon", "100x", any price talk. Snipers and trusted KOLs filter these out.

---

## 5. Copy templates

### KOL DM (cold)
```
Hey [name], launching {{TICKER}} on Sunday around [time] UTC.

It's [one-liner]. Built by the team behind mirror-deployer (github.com/yksanjo/mirror-deployer).

Looking to lock in a tweet at graduation. Your rate?

Happy to send the thread copy + assets ahead of time so you can preview.
```

### KOL DM (warm — they've engaged with Mirror family)
```
[name] — you've been around the mirror-deployer launch. Doing the next one Sunday.

{{TICKER}} — [one-liner].

Want first dibs on a paid post? Rate + slot?
```

### TG channel pitch
```
Hi, looking to book a paid push for {{TICKER}} launch on [date] at [time] UTC.

Context: token from the team behind mirror-deployer (github.com/yksanjo/mirror-deployer). Built-in audience from prior launches.

Need: T-0 slot + T+15min reslot if available.
What's your rate card? Do you have a recent push that converted well I can reference?
```

### X launch thread (T-0)
```
{{TICKER}} is live.

CA: {{CA}}
Pump: {{PUMPFUN_URL}}
Chart: dexscreener.com/solana/{{CA}}

[One-liner about what it is]

Why now: [1 sentence on meta/timing]
Why us: shipped mirror-deployer, holder-hunt, soag-vault — receipts in bio.

(thread 👇)
```

Follow-ups in thread:
2. What `{{TICKER}}` does in one paragraph
3. How it ties to the Mirror family (audience bridge)
4. LP burn / lock tx link
5. Roadmap — only commit to things you'll actually ship in 30 days

### DEX Screener ETI fields
```
Description (max 300 chars):
{{TICKER}} — [one-liner]. From the team behind mirror-deployer + holder-hunt + soag-vault. LP burned. Community-driven. Build receipts: github.com/yksanjo/mirror-deployer

Website: [project site if exists, else musicailab.com or X profile]
Twitter: x.com/{{X_HANDLE}}
Telegram: {{TG_GROUP}}
Discord: [optional]
```

### TG pinned post (community group)
```
🪞 {{TICKER}} — official community group

CA: {{CA}}
Chart: dexscreener.com/solana/{{CA}}
Pump: {{PUMPFUN_URL}}
Twitter: x.com/{{X_HANDLE}}

Read this before asking:
- LP: [burned/locked — paste tx]
- Top holder %: [pull from solscan]
- Roadmap: [link to thread or doc]

No price talk. No shilling other tokens. No DM to admins.
```

---

## 6. TG channel evaluation scorecard

Before paying any channel, score it /10. Don't pay any channel scoring under 5.

| Metric | Weight | How to score |
|---|---|---|
| View/member ratio | 2 | <30% = 2pts. 30-50% = 1pt. >50% = 0pts (dead list) |
| Comment ratio on free posts | 2 | Real engagement on non-paid content = 2. None = 0 |
| Last 10 paid pushes — did they spike? | 3 | Pull token charts. 7+ of 10 spiked = 3. 4-6 = 2. 0-3 = 0 |
| Cross-mentioned in trader chats organically | 2 | Yes = 2. No = 0 |
| Admin transparent (rate card, contact, identity-ish) | 1 | Public rate card = 1. Sketchy DM-only = 0 |

**Auto-disqualify:**
- Cold-DMed you unsolicited
- Won't show recent push results
- Admins are themselves dumping pushed tokens (check their wallets)
- Member count grew >50% in last 30d (suspicious bot inflation)

Track results in a spreadsheet — channel name, paid amount, push timestamp, volume spike T+5min, T+30min, T+2h. After 3 launches you have your own data.

---

## 7. Cross-product audience handoff

The Mirror family's actual moat — each launch warms the next.

```
[mirror-deployer users]
  ↓ (they trust the deployer brand)
[holder-hunt players] — daily TG game keeps them present
  ↓ (they hold $SOAG to play)
[soag-vault stakers] — lock $SOAG for badges
  ↓ (badges multiply next-launch eligibility)
[{{TICKER}} early buyers] — vault stakers get first allocation / whitelist
  ↓
[loop: vault stakers from {{TICKER}} feed the next launch]
```

**Operational asks per launch:**
- Whitelist/priority for SOAG Vault Silver+ badges (compounds vault demand)
- 24h post-launch: Holder Hunt puzzle references {{TICKER}} (cross-audience exposure)
- 48h post-launch: mirror-deployer feed shows your own deployer wallet with the {{TICKER}} deploy — adds to your public track record

---

## 8. Risk register (kill-switch criteria)

Stop the launch / hold spend if:
- [ ] RugCheck flags red (fix contract, re-launch)
- [ ] Top holder > 35% after first 5min (bot or sniper concentration — likely dead)
- [ ] X thread under 50 impressions in first 10 min (audience signal broken)
- [ ] TG community joins under 30 in first 30min (no organic interest)
- [ ] Single wallet > 8% of volume in first hour (wash-flag risk you didn't create — abort to avoid being blamed)

---

## 9. Post-launch — 7-day cadence

Day 1: Stabilize. AMA in TG. Reply to every X reply.
Day 2: Long-form thread on "what we shipped this week" — tie to Mirror family.
Day 3: First Holder Hunt puzzle that references {{TICKER}}.
Day 4: Vault staker update — show locked %.
Day 5: Roadmap update (only what you actually shipped).
Day 6: Community contest (best meme, fan tool, etc.) — generates unfakeable signal.
Day 7: Week-1 recap thread with chart, holder count, product progress.

The compound win isn't the launch chart — it's that the next launch starts with a 7-day-warmer audience.
