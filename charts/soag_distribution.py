#!/usr/bin/env python3
"""Generate SOAG distribution pie charts — today vs Week 4 vs Week 8 targets.

Run with the matplotlib-bundled Python:
  /opt/homebrew/opt/python-matplotlib/libexec/bin/python3 soag_distribution.py
"""
import json
import os
import urllib.request
from pathlib import Path
import matplotlib.pyplot as plt

CA = "ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump"
HELIUS_KEY = os.environ.get("HELIUS_KEY", "")
OUT_DIR = Path(__file__).parent

# --- Pull live data ---

def get_top_holders():
    url = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_KEY}"
    payload = json.dumps({
        "jsonrpc": "2.0", "id": 1,
        "method": "getTokenLargestAccounts", "params": [CA],
    }).encode()
    req = urllib.request.Request(url, data=payload,
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["result"]["value"]

# Brand palette
COLORS = {
    "pumpswap_lp":  "#7C3AED",  # purple
    "meteora_lp":   "#A78BFA",  # light purple
    "burn":         "#1F2937",  # near-black
    "lock":         "#10B981",  # emerald
    "top10":        "#F59E0B",  # amber
    "tail":         "#22D3EE",  # cyan — distinct from lock
    "creator":      "#3B82F6",  # blue
}

def draw_pie(ax, title, subtitle, slices):
    """slices: list of (label, pct, color). pct should sum to 100."""
    labels = [f"{lbl}\n{pct:.1f}%" if pct >= 1 else f"{lbl} {pct:.1f}%"
              for lbl, pct, _ in slices]
    values = [pct for _, pct, _ in slices]
    colors = [c for _, _, c in slices]
    # Use only labels for slices >=2% to avoid overlap on tiny slices
    inline = [labels[i] if values[i] >= 2 else "" for i in range(len(values))]
    wedges, _ = ax.pie(values, labels=inline, colors=colors,
                       startangle=90,
                       wedgeprops={"edgecolor": "white", "linewidth": 2},
                       textprops={"fontsize": 9})
    ax.set_title(f"{title}\n{subtitle}", fontsize=11, fontweight="bold", pad=14)
    # Legend for tiny slices (or all slices) outside the pie
    legend_labels = [f"{lbl} — {pct:.1f}%" for lbl, pct, _ in slices]
    ax.legend(wedges, legend_labels,
              loc="upper center", bbox_to_anchor=(0.5, -0.05),
              frameon=False, fontsize=9, ncol=2)

def make_chart():
    holders = get_top_holders()
    total = 999_990_530.99
    pumpswap_lp = float(holders[0]["uiAmount"]) / total * 100
    meteora_lp  = float(holders[1]["uiAmount"]) / total * 100
    top10_non_lp = sum(float(h["uiAmount"]) for h in holders[2:12]) / total * 100
    creator = 0.42
    tail = 100 - pumpswap_lp - meteora_lp - top10_non_lp - creator

    fig, axes = plt.subplots(1, 3, figsize=(20, 8))
    fig.patch.set_facecolor("white")

    # --- Panel 1: TODAY (2026-05-18) ---
    today = [
        ("PumpSwap LP",     pumpswap_lp,   COLORS["pumpswap_lp"]),
        ("Meteora LP",      meteora_lp,    COLORS["meteora_lp"]),
        ("Top 10 non-LP",   top10_non_lp,  COLORS["top10"]),
        ("Creator",         creator,       COLORS["creator"]),
        ("Community tail",  tail,          COLORS["tail"]),
    ]
    draw_pie(axes[0], "TODAY (2026-05-18)",
             "$10.2k MC · 246 holders · $8.5k LP",
             today)

    # --- Panel 2: WEEK 4 (Tier 1) ---
    # Real 3M burn (0.3%), 35M lock visible on Streamflow (3.5%),
    # LP deepened to $20k+ (PumpSwap %share stays ~38), 400+ holders means tail grows slightly
    # (need to redistribute from top 10 OR organic growth via Holder Hunt + airdrops).
    # Net of redistribution + lock + burn: top 10 falls from 29.5% to ~26%, tail grows
    week4 = [
        ("PumpSwap LP",     38.0, COLORS["pumpswap_lp"]),
        ("Meteora LP",      3.3,  COLORS["meteora_lp"]),
        ("Burned (real)",   0.3,  COLORS["burn"]),
        ("Locked (1yr)",    3.5,  COLORS["lock"]),
        ("Top 10 non-LP",   26.0, COLORS["top10"]),
        ("Creator",         0.4,  COLORS["creator"]),
        ("Community tail",  28.5, COLORS["tail"]),
    ]
    draw_pie(axes[1], "WEEK 4 — Tier 1 target",
             "$30–50k MC · 400+ holders · $20k LP",
             week4)

    # --- Panel 3: WEEK 8 (Tier 2 approach) ---
    # Top 10 down further to ~20% via Holder Hunt airdrops + community LP grants
    # Tail expands to 33% (1000+ holders), more burn, deeper LP
    week8 = [
        ("PumpSwap LP",     36.0, COLORS["pumpswap_lp"]),
        ("Meteora LP",      4.0,  COLORS["meteora_lp"]),
        ("Burned (real)",   1.0,  COLORS["burn"]),
        ("Locked (1yr)",    5.0,  COLORS["lock"]),
        ("Top 10 non-LP",   20.0, COLORS["top10"]),
        ("Creator",         0.4,  COLORS["creator"]),
        ("Community tail",  33.6, COLORS["tail"]),
    ]
    draw_pie(axes[2], "WEEK 8 — Tier 2 approach",
             "$100–200k MC · 1,000+ holders · $50k LP",
             week8)

    fig.suptitle("$SOAG — Token distribution roadmap (today → 8 weeks)",
                  fontsize=16, fontweight="bold", y=1.02)
    plt.tight_layout()
    out = OUT_DIR / "soag_distribution.png"
    plt.savefig(out, dpi=140, bbox_inches="tight", facecolor="white")
    print(f"saved: {out}")

    return {
        "today": {"pumpswap_lp": pumpswap_lp, "meteora_lp": meteora_lp,
                  "top10_non_lp": top10_non_lp, "creator": creator,
                  "community_tail": tail},
    }

if __name__ == "__main__":
    print(json.dumps(make_chart(), indent=2))
