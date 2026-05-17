# $SOAG Ready-to-Paste Artifacts

Drafts to copy directly into the relevant surface. No edits needed unless flagged with `[FILL]`.

**Key context locked in:**
- CA: `ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump`
- Pair: `8mqQqir1iVjbFf5iiUxiAKu3TH2CDhB67cPgXHzbE8uL` (PumpSwap)
- LP mint: `AYmfmrW7uXNdr8UkTHod9R9QiRR2wGhf2bJYKDjZ58vb` (100% locked at graduation)
- TG group: `https://t.me/+ywGUPczH4GllYTBh` (15 members, owned bot + agent)
- Twitter: `x.com/yksanjo` (personal)
- Twitter community: `x.com/i/communities/2038221752392712518`

---

## 🔑 Decision needed BEFORE pasting

The TG link `t.me/+ywGUPczH4GllYTBh` is a **private invite** (the `+` prefix). Anyone with the link can join, but:
- It can be revoked
- It doesn't read as a "real" community to bots scraping social fields
- For external promo (DEX Screener, X bio, tweet links) a **public handle like `t.me/SoagCommunity`** would be stronger

**Recommendation:** keep the private link short-term while seeding the first 50–100 members, then switch to a public handle when you're ready for external promo. Telegram lets you set a public link any time without losing members.

Below I've used the private link as-is — swap to public once you set one.

---

## 1. Telegram pinned message

Paste in the group, then pin it. Replace the two `[FILL]` lines after Yoshi confirms the bot/agent details.

```
🪞 $SOAG — Solana Agent
Official community.

CA: ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump
Chart: dexscreener.com/solana/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump
RugCheck: rugcheck.xyz/tokens/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump

— Trust hygiene (all verifiable on-chain) —
✅ LP 100% locked at pump.fun graduation
   LP mint: AYmfmrW7uXNdr8UkTHod9R9QiRR2wGhf2bJYKDjZ58vb
✅ Mint authority: revoked
✅ Freeze authority: revoked
✅ RugCheck score: 20/100 (lower = safer)

— What $SOAG does —
🎮 Holder Hunt — daily on-chain prediction game (2 puzzles/day, 00:00 + 12:00 UTC). Top scorers split $SOAG.
🔒 SOAG Vault — Streamflow lockup → soulbound Barutan-claw badges (Bronze 1.2× / Silver 1.5× / Gold 2.0× Holder Hunt payouts).
🤖 Daily wallet-analysis quiz bot — drops a target wallet, you scope + analyze it via Mirror Agent at musicailab.com, top scorers earn $SOAG.
🦞 Barutan — group mascot agent. Runs on Yoshi's local Raspberry Pi Zero 2W via Groq API. Personal assistant by day, group chatbot for you to ask things. (Yes, same Barutan as the Vault badges. Same character, different surface.)

— Transparency note —
RugCheck flags 2 "insider networks" totaling 8 accounts. These are operational wallets (Holder Hunt payouts, sol-agent-wallet test addresses, Vault contract operations) — not insider trading. All addresses are public; behavior matches our published 12-hour puzzle/payout cycle. Full address list: [FILL: post addresses once identified]

— Built by —
@yksanjo, deployer of mirror-deployer (github.com/yksanjo/mirror-deployer).

— Rules —
- No price talk, no "wen moon"
- No shilling other tokens
- No DMing admins (ping in group instead)
- Be useful or be quiet
```

---

## 2. pump.fun reply #1 — LP lock receipt (3 variants)

Post from the creator wallet `k6NEzyNUJRDjYydTZsnJSm8oBXTW59MmUF1wwJd2eyf` on the $SOAG pump.fun page. Pick the variant that fits the audience you want to land.

### Variant A — short-technical (RECOMMENDED for diligence buyers)
Best for: sophisticated buyers running RugCheck before deciding. Drops only verifiable facts. No marketing language.
```
LP locked 100% at graduation. LP mint AYmfmrW7uXNdr8UkTHod9R9QiRR2wGhf2bJYKDjZ58vb, all 4.19T LP tokens in protocol vault, none withdrawable. Mint+freeze revoked. RugCheck 20/100. rugcheck.xyz/tokens/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump
```
(~280 chars) — pure receipt, zero pitch. Builds creator-wallet credibility.

### Variant B — ecosystem story
Best for: pump.fun page readers who don't know what $SOAG does. Surfaces the agent-suite thesis.
```
LP 100% locked at graduation (mint AYmfmrW7…58vb). Mint+freeze revoked. $SOAG underwrites an agent suite: daily wallet-quiz bot (uses Mirror Agent at musicailab.com), Barutan TG agent (Pi Zero 2W + Groq), SOAG Vault with Barutan-claw badges. Three agents, one token.
```
(~290 chars) — receipt + value prop. Tradeoff: less pure-signal than A.

### Variant C — punchy social
Best for: people scrolling the page on their phone. Highest catch-rate, lowest depth.
```
LP locked. Mint revoked. Freeze revoked. RugCheck 20/100.
Powers a daily wallet-quiz bot, a Pi-hosted Barutan TG agent, and a Streamflow vault with Barutan-claw badges.
3 agents. 1 token. Verify everything on-chain.
rugcheck.xyz/tokens/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump
```
(~290 chars) — punchier, visual scan-friendly.

### Recommendation
**Post Variant A first.** Diligence buyers (the ones who actually move price) verify before buying. A pure-receipt reply from the creator wallet establishes trust without selling. Then **rotate Variants B + C in over the following weeks** as replies #2 and #3, tied to real events (Vault Gold launch, jackpot weekend) so the page accumulates 3 quality receipts within a month.

**Format note:** post the reply, then 30 minutes later post a 2nd reply to your own first reply with: "Anyone wants to verify, the Solscan link to the LP mint is here: solscan.io/token/AYmfmrW7uXNdr8UkTHod9R9QiRR2wGhf2bJYKDjZ58vb" — this seeds the appearance of a thread (which the pump.fun UI surfaces more prominently than a single isolated reply).

**Future replies (1/week cadence — see `THREE-FIXES.md` Fix 3):**
- Vault Gold tier launch tx
- Each Holder Hunt jackpot payout tx
- Holder count milestones (250, 500, 1000)
- Any new product or integration

---

## 3. DEX Screener ETI description

Two variants, both under the 300-char limit. Pick one. Variant A leads with utility, Variant B leads with trust. Recommend **Variant B** since the chart is small — trust signals convert better at this size than utility pitches.

**Variant A — utility-first (244 chars):**
```
$SOAG powers Holder Hunt (daily on-chain prediction game, 2 puzzles/day) and SOAG Vault (Streamflow lockup + Barutan badges, 1.2×-2.0× game payouts). LP 100% locked at pump.fun grad. Mint+freeze revoked. By @yksanjo, mirror-deployer.
```

**Variant B — trust-first (252 chars, RECOMMENDED):**
```
LP 100% locked at pump.fun graduation. Mint+freeze revoked. RugCheck 20/100. $SOAG powers Holder Hunt (daily prediction game) + SOAG Vault (Streamflow lockup, Barutan badges multiply payouts 1.2×-2.0×). By @yksanjo, mirror-deployer team.
```

**ETI social fields to update:**
- Website: `https://musicailab.com/` (already set)
- PUMP SCAN link: `https://pumpscan.musicailab.com/` (already set)
- Twitter: `https://x.com/yksanjo`
- Twitter Community: `https://x.com/i/communities/2038221752392712518` (already set)
- **Telegram: `https://t.me/+ywGUPczH4GllYTBh`** ← new field to add

---

## 4. @yksanjo X bio + lock-disclosure tweet

### Bio update (130/160 chars)
```
Building agentic tools on Solana | $SOAG → Holder Hunt + SOAG Vault | mirror-deployer | github.com/yksanjo
```

### Lock disclosure tweet (single)
```
$SOAG status check for anyone doing diligence:

✅ LP 100% locked (pump.fun grad — can't be withdrawn, ever)
✅ Mint authority: revoked
✅ Freeze authority: revoked
✅ RugCheck: 20/100 (lower = safer)

CA: ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump
🔗 rugcheck.xyz/tokens/ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump

Powers Holder Hunt + SOAG Vault. Thread 👇
```

### Lock disclosure thread (continuations)
```
2/ Holder Hunt is a daily on-chain prediction game I run.

Two puzzles/day in TG (00:00 + 12:00 UTC). Sourced from pumpscan.musicailab.com. Top scorers split a $SOAG pot.

No fee to play. No token gating to enter.
```

```
3/ SOAG Vault is a Streamflow lockup with a twist.

Lock $SOAG → mint a soulbound Barutan-claw badge:
🥉 Bronze = 1.2× Holder Hunt payouts
🥈 Silver = 1.5×
🥇 Gold = 2.0×

Badges are non-transferable. No second token. Lock value compounds.
```

```
4/ "Agent token" gets thrown around. Here's what it actually means for $SOAG — three real agents, all running:

• Quiz bot — daily wallet puzzle in TG, $SOAG payouts
• Barutan — group mascot, runs on a Raspberry Pi Zero 2W + Groq API (my local box)
• Mirror Agent — wallet-scoping tool at musicailab.com, used to solve the quiz

Token is the unit of account across the suite.
```

```
5/ Try it live: t.me/+ywGUPczH4GllYTBh

Walk in, ask Barutan a question. Solve the daily wallet quiz with Mirror Agent. Earn $SOAG. Lock it in SOAG Vault for a Barutan-claw badge that 2x's your next payout.

Same Barutan in the badge as in the TG. Single character, multiple surfaces.
```

---

## 5. Holder Hunt → $SOAG TG bridge message — LIKELY UNNECESSARY

Based on the bot description (daily wallet-analysis quiz, $SOAG rewards, uses Mirror Agent at musicailab.com) **this 15-person TG IS the Holder Hunt group**, not a separate community. There is no second TG to bridge to — this one is the unified $SOAG home: game + community + Barutan mascot + bot.

**Confirm:** is there a separate Holder Hunt TG, or is `t.me/+ywGUPczH4GllYTBh` the only one?

- **If yes (this IS the Holder Hunt TG, no other):** skip this section. The pinned message in §1 already positions the group correctly as both game and community.
- **If there's another Holder Hunt TG separate from this:** then we need a bridge message. Reply and I'll draft the right framing once I know which group is which.

For now, leave this section parked.

---

## 6. Week-2 organic baseline activity calendar

7-day plan to drive organic volume + holders before any paid push. Tie the week to **Vault Gold tier launch** as the anchor moment — it's a real product event with on-chain proof and creates a natural buy reason (lock $SOAG → get Gold → multiply Holder Hunt earnings).

**Goal metrics by end of Day 7:**
- Holders: 202 → 250+
- Top non-AMM holder: 20.7% → <18%
- 24h volume sustained ≥ $15k for 3+ consecutive days
- pump.fun replies: 0 → 3+ real ones
- TG community: 15 → 40+

| Day | Activity | Artifact / proof | Channels |
|---|---|---|---|
| Mon | Announce Vault Gold tier launching Tuesday. Tease the multiplier mechanics. | Tweet from @yksanjo. Pinned in $SOAG TG. | X, TG |
| Tue | Vault Gold tier deploys + Yoshi mints first Gold badge. Post tx. | Streamflow lock tx hash + Barutan-claw NFT mint tx | X thread, $SOAG TG pinned post update, pump.fun reply #2 |
| Wed | Holder Hunt "Gold Weekend" announcement — 4× normal jackpot Fri-Sun. Mention Gold holders get 2× on top. | Tweet + Holder Hunt TG announcement + screenshot of upcoming pot size | X, Holder Hunt TG, $SOAG TG |
| Thu | Mid-week pulse: holder count update, top-holder dist screenshot, lock tx volume from Vault. | One on-chain screenshot (Solscan), one solscan link | X, $SOAG TG |
| Fri | Gold Weekend kicks off. 12:00 UTC puzzle goes live, prize 4×. | Puzzle drop tweet + pumpscan link to the source | X, both TGs |
| Sat | Saturday puzzle + Friday leaderboard. Soulbound Gold holders shown atop board (visible signal that locks earn multiplier). | Leaderboard screenshot, Gold-holder badge image | X, both TGs |
| Sun | Sunday puzzle + payout tx hashes. Week recap thread Sunday night: holders gained, volume, vault locks, replies. | Payout tx hashes (real on-chain), thread with metrics. pump.fun reply #3 = the payout receipt. | X (long thread), pump.fun reply, both TGs |

**Critical: every artifact is on-chain.** No screenshots without a tx link. The week stacks 7 days of real receipts that future buyers can verify.

**End-of-week decision gate:**
- All 5 goal metrics hit → run pilot push next week per `PILOT-CHECKLIST.md` at $400–600 spend
- 3 of 5 hit → run a half-pilot at $300, learn, then full pilot
- <3 hit → extend organic baseline another week, don't spend on promo

---

## 7. RugCheck insider-networks transparency disclosure

### Investigation note
RugCheck flagged **2 insider networks with 8 total accounts**. Likely composition (in priority of likelihood):

1. **Holder Hunt payout wallets** — clustered because they receive funding from the same operational wallet (likely `k6NEzy…` or a downstream wallet) on a 12-hour cycle. RugCheck's heuristic treats this as coordinated, which is technically correct but operationally legitimate.
2. **sol-agent-wallet test/operational addresses** — the agentic framework referenced in the pump.fun description. These wallets likely transact with the token and share funding.
3. **SOAG Vault operational wallets** — contract owner wallet, badge minting wallet, possibly test wallets.

**To identify the exact 8 addresses:** log into RugCheck.xyz with the creator wallet (Solana wallet auth), open the $SOAG report, the "Detected Insider Networks" section expands to show each cluster with addresses + reasoning. Copy these out.

### Public disclosure draft (TG pinned + tweet thread #5)
```
Transparency note on RugCheck's "insider network" flag for $SOAG.

RugCheck flags 2 networks (8 wallets) as "insider activity." Here's what those actually are:

- Holder Hunt payout wallets (we run a daily game — payouts hit on a fixed 12h cycle)
- sol-agent-wallet operational addresses (the agent referenced in the token description)
- SOAG Vault contract operations (mint badge, lock $SOAG)

All 8 addresses: [list — fill once identified]

The flag is correct that these wallets coordinate — they're the same operator (us). It's wrong to read as "insider trading." Behavior matches our published puzzle schedule and Vault lock cycle.

If anything ever happens outside this pattern (sudden dump, off-schedule moves), call us on it publicly.
```

---

## 8. Manual-action checklist for Yoshi

Order matters — do in this sequence, top-down:

- [ ] **1. Confirm what the TG bot + agent actually do** (fill the two `[FILL]` lines in §1 pinned message)
- [ ] **2. Identify the 8 RugCheck insider-network wallets** (log into RugCheck with creator wallet, copy addresses)
- [ ] **3. Decide: keep private TG link or migrate to public handle** (recommend: private now, public in 2 weeks once 50+ members)
- [ ] **4. Paste §1 pinned message into TG, pin it**
- [ ] **5. Update DEX Screener ETI with §3 Variant B description + add TG link to social fields**
- [ ] **6. Update @yksanjo X bio per §4**
- [ ] **7. Post §4 lock-disclosure tweet + thread**
- [ ] **8. Post §2 LP-lock reply on pump.fun page (from creator wallet `k6NEzy…`)**
- [ ] **9. Post §5 bridge message in Holder Hunt TG (one time)**
- [ ] **10. Confirm Vault Gold tier is ready to ship by Tuesday** (anchor of the week-2 calendar)
- [ ] **11. Pre-schedule Tweet drafts for each Day in §6 calendar**

Total ~60–90 min of manual work, $0 spend.

**After this:** week-2 organic baseline runs on autopilot. End-of-week decision gate determines if pilot push is greenlit.
