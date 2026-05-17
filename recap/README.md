# Weekly Recap System

How to produce a clean, link-embedded PDF recap of the $SOAG ecosystem every week — and keep an archive.

## Files

```
recap/
├── README.md                 ← this file
├── PROMPT.md                 ← what to capture each week (the checklist)
├── template.html             ← shared design (don't touch unless redesigning)
├── build.py                  ← generator: JSON + template → PDF
├── SOAG-WEEKLY.pdf           ← always the latest week (overwritten each run)
└── weeks/
    ├── 2026-W20.json         ← week's data (edit this each Sunday)
    ├── 2026-W20.pdf          ← that week's archived PDF
    ├── 2026-W20.rendered.html ← intermediate, can delete
    ├── 2026-W21.json         ← (next week)
    └── …
```

## Run

```bash
cd ~/launch-kit/recap
python3 build.py weeks/2026-W21.json
# or just:
python3 build.py            # picks the newest weeks/*.json
```

Output:
- `weeks/<weekId>.pdf` — that week's archive
- `SOAG-WEEKLY.pdf` — overwritten to always point at the newest

Open with:
```bash
open ~/launch-kit/recap/SOAG-WEEKLY.pdf
```

## Each week, the easy path

1. **Sunday night**: open a Claude session.
2. Paste the prompt block from `PROMPT.md`.
3. Tell Claude what shipped + what's next.
4. Claude:
   - copies `weeks/<previous>.json` → `weeks/<new>.json`
   - updates only what changed
   - auto-refreshes on-chain stats (holders, RugCheck, LP, etc.) via WebFetch
   - runs `python3 build.py weeks/<new>.json`
5. PDF is at `~/launch-kit/recap/SOAG-WEEKLY.pdf`. Send/share/post.

## Why JSON not Markdown for the per-week data

- Easier to substitute into the template (no parsing)
- Easier for Claude to edit programmatically without changing layout
- Tradeoff: less human-friendly to hand-edit, but you don't need to — Claude updates it

If you ever want to edit by hand: the JSON shape is documented in `weeks/2026-W20.json` (the first one). Copy it, change values, run build.

## Customising the design

The `template.html` uses CSS only (no JS), prints to A4, and embeds all assets inline. To redesign:

1. Edit `template.html` directly
2. Run `python3 build.py` — same data, new look
3. If you add new sections, add the `{{PLACEHOLDER}}` to template and the matching key+renderer to `build.py`

## Archive growth plan

After 13 weeks: run a quarterly-recap by concatenating timelines. Easy retrofit — the JSON shapes are designed for this.
