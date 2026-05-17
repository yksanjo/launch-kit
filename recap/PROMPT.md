# Weekly Recap Prompt — what to capture every Friday/Sunday

When it's time to make next week's PDF, paste this into a Claude session along with your raw answers. Claude will produce the new `weeks/YYYY-Www.json` and run the build.

> **Make this week's $SOAG recap PDF. Same format as `weeks/2026-W20.json`. Here's what happened this week.**
>
> 1. **Week ID** — ISO week like `2026-W21` and the date range, e.g. "May 17 → May 23"
>
> 2. **Headline stats** — give me the 4 numbers you want on top. Holders count, LP locked %, RugCheck score, 24h volume — or change them if a different 4 matter this week (e.g. "TG members", "Vault locks", "Holder Hunt payouts paid", "active deployers tracked")
>
> 3. **Shipped this week** — bullet list with dates. Things like:
>    - new product/feature ships (with tx hash or commit hash or URL)
>    - new partnerships, AMAs, KOL mentions
>    - infra changes (Vercel migration, new Pi service)
>    - on-chain milestones (graduation, holder count crossings)
>    - content posted (X threads, pump.fun replies)
>
> 4. **Next week priorities** — top 4–6 things. Mark each `high/med/low`. Examples:
>    - "Ship Vault Gold tier" (high)
>    - "Migrate mirror-deployer off Pi" (high)
>    - "Run jackpot weekend" (med)
>    - "5 more KOL DMs" (med)
>
> 5. **Mirror Family status changes** — anything moved from queued→live, or new tool added, or status flipped? Skip if no changes (keep last week's family block).
>
> 6. **Anything to remove** from last week's recap that's no longer accurate?
>
> Take the previous week's JSON as the base, only change what's different.

---

## What I capture without being asked (auto-pulled)

Each week the assistant should automatically refresh these if no answer given:

| Field | Source | How to refresh |
|---|---|---|
| Holders count | `api.dexscreener.com/latest/dex/tokens/<CA>` → `txns.h24` or RugCheck holders | WebFetch the DexScreener API |
| MC + 24h vol | DexScreener API | same |
| LP locked % | RugCheck `/v1/tokens/<CA>/report` | WebFetch |
| Top holder % | RugCheck full report | same |
| Mint/freeze authority | RugCheck `mintAuthority`, `freezeAuthority` | same |
| pump.fun reply count | `frontend-api-v3.pump.fun/coins/<CA>` | WebFetch |
| GitHub commits (mirror-deployer, soag-vault, holder-hunt) | `gh api repos/yksanjo/<repo>/commits` | gh CLI |
| Pi service status | `ssh yojinbot@<pi-host> 'systemctl is-active …'` | SSH |
| Pi free RAM / load | same SSH | SSH |

So the minimum input for next week's recap is just:
- What you shipped (with links)
- What's next (with priorities)
- Anything qualitative you want highlighted (community wins, KOL replies, surprises)

Everything else can be auto-pulled.

---

## Variations / future formats

The same template can carry different framings without changing the system:

- **Weekly recap** (current) — what shipped, what's next
- **Investor update** — same data but front-loaded with traction numbers
- **Community update** — drop the token facts, expand the daily-loop section
- **Quarterly review** — concat 13 weeks of timelines into one document

To use a variant: copy `template.html` to `template-<variant>.html`, edit the JSON shape, and pass `--template template-<variant>.html` to build.py (TODO: add that flag).

---

## Cadence

**Suggested:** Sunday night. Run after the week's last activity, before next week's first.

Why Sunday: gives you a coherent week-bucket. Why not Friday: weekend activity often produces the best on-chain receipts to include.
