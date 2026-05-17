# mirror-marketplace — Honest Audit Report (2026-05-16)

> **📌 Status update — 2026-05-17:** The headline finding below ("no SOL payment processing in this codebase") was **fixed in [commit `2b788fa`](https://github.com/yksanjo/mirror-marketplace/commit/2b788fa)**. `/api/subscribe` now requires a `paymentSignature`, fetches the parsed tx via `@solana/web3.js`, verifies a `SystemProgram.transfer` to both the creator wallet and the platform fee wallet at the tier's listed price, enforces a 10-minute freshness window, and prevents replay via `data/used_signatures.json`. `/api/listings` POST now requires an ed25519 signed wallet-ownership proof. Backend is now correct end-to-end; the open follow-up is wiring `@solana/wallet-adapter` on the frontend so the in-app Subscribe button builds + signs the dual-transfer tx automatically (tracked in the repo's README Roadmap). The audit below is kept as the historical record of the gap and the fix's rationale.

---

User asked 5 questions on a live product taking customers. Reporting straight, no padding.

**Source of report:** code review of `~/mirror-marketplace` (local) + **live SSH check of deployed Pi** (`yojinbot@100.109.137.47` via Tailscale, 2026-05-16 05:24 UTC).

---

## ✅ Live state — confirmed via SSH

| Field | Reality on the Pi |
|---|---|
| **Real subscriptions** | **0** — the only `subscriptions.json` entry is `TEST_SUB_WALLET_XYZ` (a literal test placeholder, not a Solana address). One test record from when you were developing. |
| **Real listings added by users** | **0** — only the 3 hardcoded seeds (mirror_seed_1/2/3) exist. No real users have added themselves. |
| **The "volume" you saw in the UI** | **59.3 SOL = hardcoded seed data** (12.4 + 5.1 + 41.8 from `marketplace.ts:17–59`). Nobody has actually paid SOL through the system. |
| **Service status** | Both `mirror-marketplace` and `mirror-deployer` active for 2 days. Caddy active. |
| **Pi load** | Idle (load avg 0.00) — confirms zero traffic right now. |
| **Pi RAM** | **680 MB / 991 MB used, 351 MB swap actively in use**. You're already 68% memory + swap thrash with zero users. Adding real traffic = immediate degradation. |
| **Pi disk** | 12 GB / 29 GB used (44%). OK. |
| **Git on deployed dir** | **Not a git repo** — deploy is rsync-snapshot, not git-tracked. My local README + package.json edits HAVE NOT propagated to the Pi yet. The live version still contains the "ex-Atlantic Records, ex-Warner Music" identity leak in package.json. |
| **Recent journalctl** | Empty (no recent requests) — confirms no user traffic. |

### What this actually means

1. **No one has been harmed.** No SOL has been mistakenly paid through the marketplace because no real users have tried. The 1 "subscription" is your own test from development.
2. **The 59.3 SOL "volume" is purely cosmetic.** It's what's hardcoded into the source. Not real platform activity.
3. **You are in the cheapest-possible position to fix this.** No users to refund, no community to apologize to, no public claims to retract. Just engineering or copy edits.
4. **Pi is already memory-constrained.** Even before traffic. The audit's scaling concerns are real — you're swapping at idle.

### Two immediate housekeeping items

- ⚠️ **Deployed `package.json` still has the identity leak** ("ex-Atlantic Records, ex-Warner Music"). My local fix hasn't shipped. Needs an rsync deploy.
- ⚠️ **Delete the TEST_SUB_WALLET_XYZ record** from `data/subscriptions.json` on the Pi before anyone screenshots the stats card and thinks it's a real subscription.

---

## Original audit follows — applies regardless of live state being zero-users

**Source of report:** code review of `~/mirror-marketplace` (the local repo, presumably what's deployed under the musicailab.com subdomain).

---

## 🚨 The headline finding

**There is no SOL payment processing in this codebase.**

Specifically:
- `package.json` has **zero Solana dependencies** — no `@solana/web3.js`, no wallet-adapter, no anchor. The codebase literally cannot construct, sign, send, or verify a Solana transaction.
- `/api/subscribe` (the "pay to subscribe" endpoint) takes a JSON body with `subscriberWallet`, `creatorWallet`, `tier` — and **writes a record to a local JSON file**. That's the entire flow. No signature is checked. No tx is requested. No SOL is moved.
- `/api/listings` POST endpoint accepts any listing body and writes it to disk. No authentication, no signature verification.
- The "volume" numbers visible in the UI (e.g. 12.4 SOL, 5.1 SOL, 41.8 SOL on the three seed creators) are **hardcoded in `src/lib/marketplace.ts` lines 17–59** as `SEED_LISTINGS`. They are not aggregated from real transactions.

Code reference (`src/lib/marketplace.ts:108–139`):
```typescript
export async function subscribe(subscriberWallet, creatorWallet, tier) {
  const sub = { id: ..., subscriberWallet, creatorWallet, tier, active: true, ... };
  const subs = await loadSubs();
  userSubs.push(sub);
  await saveSubs();      // ← just writes JSON file
  // increments followers count
  return sub;            // ← no tx, no verification
}
```

---

## Your 5 questions, answered honestly

### Q1. Where the SOL people pay is going

**Nowhere via this system.** No SOL is being processed by mirror-marketplace.

If users believe they're paying you SOL through this site, they aren't — they're clicking a button that records a JSON entry. Unless they're separately sending SOL to creator wallets via a wallet app outside the marketplace, no SOL has moved.

If the "volume" you saw refers to:
- **The number on the marketplace stats card** → that's `12.4 + 5.1 + 41.8 = 59.3 SOL` hardcoded in seed data, not real
- **Real SOL in the deployer wallet** `k6NEzy…` or any listed wallet → that's from your $SOAG operations or unrelated, not from marketplace flow

### Q2. Is it working properly?

**As a UI:** yes. Listings render, the subscribe button doesn't error, the stats card shows numbers.

**As a marketplace:** no. There's no payment rail, no signature verification, no SOL handling. Calling it a "marketplace" when no value is exchanging is the central issue.

**As a data pipeline:** brittle. Storage is a flat JSON file rewritten on every POST. Concurrent writes can corrupt. There's no schema validation beyond a basic null check. No rate limiting. Anyone can spam `POST /api/listings` and `POST /api/subscribe` from cURL.

### Q3. Are people happy?

**Unknown from the codebase** — there's no telemetry, no feedback form, no error logging beyond Node.js defaults, no view counts, no retention metric.

What I'd predict:
- Users who clicked "subscribe" expecting to pay SOL and unlock content: confused/disappointed when nothing happens.
- Users who tried to add a listing and post their wallet: may be confused that no verification happens.
- Users who never tried to transact and just browsed: probably fine, looks legit on the surface.

**You may have a trust issue brewing if anyone publicly claims they were going to "subscribe" and nothing happened.** Worth checking now before it amplifies.

### Q4. Can it scale to 10,000 users?

**No. Not even close.** Hard architectural limits:

| Bottleneck | Current state | 10k user reality |
|---|---|---|
| **Storage** | JSON file (`data/subscriptions.json`, rewritten on every POST) | Each subscribe = rewrite full file. At 10k subs × even 10 ops/sec = constant write contention, corruption likely. Read latency grows linearly with file size. |
| **Concurrency** | Node.js Next.js, single process, no clustering | Default Next.js handles ~100–500 concurrent requests on small hardware before tail latency spikes |
| **Helius RPC calls** | `getListings()` fetches `getDeployerRep` per wallet, every request | 10k users × 10 page loads × 10 listings × 1 Helius call = 1M RPC calls/day. Helius free tier is 10k/day. You'd hit $50–500/day Helius bills, or rate-limit out entirely |
| **No caching layer** | Each request rebuilds the listing list from disk | Trivially fixable but currently O(N) per request |
| **No CDN** | All traffic hits the origin | At 10k users your Pi becomes the bottleneck, not the network |
| **Auth** | None | Spam/abuse vector at scale — anyone can flood the JSON files with garbage listings |

**Realistic current capacity: 10–50 simultaneous active users before degradation. 100 concurrent users probably starts crashing.**

### Q5. Can the Raspberry Pi handle it?

**No, even less so when you factor what else is on that Pi.**

Per `memory/pi-fleet.md`, your Pi 5 manager (1GB RAM, the same box `mirror-marketplace` is deployed to as `User=yojinbot` per the systemd unit) is already running:

- EarnApp (passive income)
- Honeygain (passive income)
- Mysterium (residential proxy)
- BOINC (CPU-burning compute)
- picoclaw (Telegram gateway, systemd)
- bitcoin_hunters.py (Python script)
- mirror-deployer (port 3032, Next.js Node)
- mirror-marketplace (port 3033, Next.js Node) ← this

**That's 8 services on a 1GB Pi 5.**

Realistic ceilings:
- **RAM:** Each Next.js prod server idles around 80–150MB. Two of them = 200–300MB. Add Docker overhead (EarnApp, Honeygain, Mysterium are containers, each 50–100MB). BOINC chews variable CPU. You're probably running at 70–85% RAM usage **at idle**, with very little headroom for traffic.
- **Disk:** SD card. Random writes ~1MB/s sustained. Caddy logs + watchdog cron + bitcoin_hunters.py + JSON-file persistence = SD saturation under load. Also a long-term SD lifespan risk (writes wear cells).
- **CPU:** BOINC will burn 100% of any CPU you give it. Even with throttling, web traffic latency degrades when BOINC is busy.
- **Network:** Mysterium turns the Pi into a residential proxy. Real users' marketplace traffic competes with proxy traffic for bandwidth.

**At 10k users, this Pi will OOM-kill or crash within minutes.** Practical ceiling for a Next.js Node service on this hardware coexisting with the income stack is roughly **50–100 active users** before things visibly degrade.

---

## What I recommend (priority order)

### 🔴 P0 — Before any more users find the site

These are fix-now items:

1. **Decide: is mirror-marketplace meant to actually process SOL, or is it currently a demo/showcase?**
   - If demo: change all UI copy from "Subscribe" + price-in-SOL to "Request access" / "Waitlist" / "Coming soon." Honest framing — and you keep the listings as a discovery surface without false payment expectations.
   - If real: implement the actual payment flow (Section "Implementing real SOL payment" below).

2. **If anyone has paid SOL manually to a creator wallet under the impression they "subscribed":** check your DMs/TG for confusion, refund or clarify.

3. **Add a banner if real:** "Currently in beta — payment flow under construction. Subscribe button records interest only; no SOL is charged yet." This is honest and protects you legally + reputationally.

### 🟡 P1 — Architectural fixes before scaling past 100 users

4. **Migrate JSON storage to SQLite.** Drop-in via `better-sqlite3`, same schema, atomic writes, handles thousands of concurrent users easily. ~2 hours of refactor.
5. **Add an in-memory cache for `getListings()`** with 30–60 sec TTL. Helius calls drop from per-request to per-minute.
6. **Add minimal rate limiting** (`express-rate-limit` equivalent in Next.js middleware) — 10 req/min per IP on the POST endpoints.
7. **Verify wallet signature on `POST /api/listings`** — require the listing creator to sign a message proving they own the wallet they're listing. Stops spam listings.

### 🟢 P2 — Before 10k users

8. **Move off the Pi 5.** Realistic options:
   - **Vercel** (free tier handles 100k pageviews/mo, $20/mo for more) — Next.js native, zero ops
   - **Fly.io** ($5–20/mo) — closer to Pi feel, more control
   - **Hetzner CX22** (~€4/mo, 4GB RAM, 2 vCPU) — way more headroom for any custom needs
   - Keep the Pi for the passive-income stack only; web services go to a real host
9. **Move storage from SQLite to Postgres** (Neon / Supabase free tier) when subs cross ~1000.
10. **CDN your assets** — already mostly free if you host on Vercel/Cloudflare; helps offload static asset load.

---

## Implementing real SOL payment (if Q1 answer is "yes, make it real")

Two patterns, pick one:

### Pattern A — Off-chain price posting, on-chain payment verify (RECOMMENDED, simpler)

1. UI: "Pay X SOL to `<creator_wallet>` from your wallet, then paste the tx signature here"
2. Backend: `POST /api/subscribe` takes `{ subscriberWallet, creatorWallet, tier, txSignature }`
3. Backend uses `@solana/web3.js` to:
   - Look up the tx by signature
   - Verify it transferred ≥ tier price from subscriberWallet to creatorWallet
   - Verify it's recent (within last 60 sec to prevent replay)
   - Activate subscription only if all checks pass
4. Platform fee (5%, per your README): you become the actual recipient OR creators escrow a portion. Simpler: platform fee is a separate small tx to your platform wallet, verified the same way.

**Dependencies needed:** `@solana/web3.js` (~200KB). Helius RPC already in use.

**Effort:** ~6–10 hours for a clean implementation including UI updates, error states, replay protection.

### Pattern B — Wallet-adapter direct-buy (slicker UX, more code)

1. User clicks "Subscribe" → Solana Wallet Adapter pops up → user signs a SOL transfer
2. Tx submits → backend gets signature in webhook → backend verifies + activates

**Dependencies:** `@solana/wallet-adapter-base`, `@solana/wallet-adapter-react`, `@solana/wallet-adapter-react-ui`, `@solana/web3.js`. ~500KB total.

**Effort:** ~2–3 days for a polished version.

**Recommendation for your stage:** Pattern A. Faster to ship, easier to debug, perfectly fine for sub-1000 users.

---

## What's verified by this audit vs. what I haven't checked

✅ Verified from code:
- No SOL payment processing anywhere in the codebase
- JSON-file storage architecture
- Seed data is hardcoded (the "volume" you see)
- No authentication on POST endpoints

❌ Not verified (need live access):
- Whether the deployed `data/listings.json` and `data/subscriptions.json` on the Pi have many real records (could tell us how many users actually clicked subscribe)
- Real-time Pi load (CPU, RAM, disk I/O)
- Whether the deployed code is actually identical to the local repo, or if you have unmerged changes on the Pi
- The public URL of mirror-marketplace under musicailab.com

**Want me to SSH to `yojinbot@100.109.137.47` (Tailscale, per `pi-fleet.md`) and check live state?** I can:
- Read `data/listings.json` + `data/subscriptions.json` to see real activity
- `systemctl status mirror-marketplace` to confirm it's running
- `journalctl -u mirror-marketplace -n 200` for recent activity
- `free -h`, `df -h`, `uptime`, `top -bn1` for current resource state
- `git status` / `git log -5` on the deployed repo to confirm it matches local

I won't change anything. Just read. Confirm if you want me to.

---

## Recommendation for HN/PH plan

**Don't launch mirror-deployer on HN/PH until mirror-marketplace is either:**
- Honestly relabeled (waitlist / beta / coming soon), OR
- Actually processing payments

HN crowd will dig into your repos. If they find a marketplace claiming SOL subscriptions with no payment code, your credibility on mirror-deployer takes collateral damage. The two ship together in the public eye.

ETA on the relabel-or-fix: half a day at most. Then HN/PH launch is safe.
