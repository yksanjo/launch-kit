#!/usr/bin/env python3
"""Generate the 2-panel chart for the X post: today vs healthy target."""
import json
import os
import urllib.request
from pathlib import Path
import matplotlib.pyplot as plt

CA = "ADue87cPcDhsyGq2hrDsukp7j8AFTSnaYHSanDATpump"
HELIUS_KEY = os.environ.get("HELIUS_KEY", "")
OUT_DIR = Path(__file__).parent

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

COLORS = {
    "pumpswap_lp":  "#7C3AED",
    "meteora_lp":   "#A78BFA",
    "burn":         "#1F2937",
    "lock":         "#10B981",
    "top10":        "#F59E0B",
    "tail":         "#22D3EE",
    "creator":      "#3B82F6",
}

def draw_pie(ax, title, subtitle, slices):
    labels = [f"{lbl}\n{pct:.1f}%" if pct >= 2.5 else "" for lbl, pct, _ in slices]
    values = [pct for _, pct, _ in slices]
    colors = [c for _, _, c in slices]
    wedges, _ = ax.pie(values, labels=labels, colors=colors, startangle=90,
                       wedgeprops={"edgecolor": "white", "linewidth": 2.5},
                       textprops={"fontsize": 11, "fontweight": "bold"})
    ax.set_title(f"{title}\n{subtitle}", fontsize=13, fontweight="bold", pad=18)
    legend_labels = [f"{lbl} — {pct:.1f}%" for lbl, pct, _ in slices]
    ax.legend(wedges, legend_labels, loc="upper center",
              bbox_to_anchor=(0.5, -0.02), frameon=False, fontsize=10, ncol=2)

def make_chart():
    holders = get_top_holders()
    total = 999_990_530.99
    pumpswap_lp = float(holders[0]["uiAmount"]) / total * 100
    meteora_lp  = float(holders[1]["uiAmount"]) / total * 100
    top10_non_lp = sum(float(h["uiAmount"]) for h in holders[2:12]) / total * 100
    creator = 0.42
    tail = 100 - pumpswap_lp - meteora_lp - top10_non_lp - creator

    fig, axes = plt.subplots(1, 2, figsize=(15, 8.5))
    fig.patch.set_facecolor("white")

    today = [
        ("PumpSwap LP",     pumpswap_lp,   COLORS["pumpswap_lp"]),
        ("Meteora LP",      meteora_lp,    COLORS["meteora_lp"]),
        ("Top 10 non-LP",   top10_non_lp,  COLORS["top10"]),
        ("Creator",         creator,       COLORS["creator"]),
        ("Community tail",  tail,          COLORS["tail"]),
    ]
    draw_pie(axes[0], "$SOAG today",
             "246 holders · $10.2k MC · $8.5k LP",
             today)

    # Healthy target — Tier 2 / $200k MC
    target = [
        ("PumpSwap LP",     36.0, COLORS["pumpswap_lp"]),
        ("Meteora LP",      4.0,  COLORS["meteora_lp"]),
        ("Burned (real)",   1.0,  COLORS["burn"]),
        ("Locked 1yr",      5.0,  COLORS["lock"]),
        ("Top 10 non-LP",   20.0, COLORS["top10"]),
        ("Creator",         0.4,  COLORS["creator"]),
        ("Community tail",  33.6, COLORS["tail"]),
    ]
    draw_pie(axes[1], "Healthy target — Tier 2",
             "1,000+ holders · $100-200k MC · $50k LP",
             target)

    fig.suptitle("$SOAG — Token distribution: where we are vs where we're going",
                  fontsize=16, fontweight="bold", y=1.02)
    plt.tight_layout()
    out = OUT_DIR / "soag_2panel.png"
    plt.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
    print(f"saved: {out}")

if __name__ == "__main__":
    make_chart()
