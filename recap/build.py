#!/usr/bin/env python3
"""
Weekly recap builder.

Usage:
    python3 build.py weeks/2026-W20.json
    python3 build.py weeks/latest        # alias for the newest json in weeks/
    python3 build.py                     # picks newest by default

Reads template.html + a per-week JSON file, substitutes placeholders, and
renders an A4 PDF next to the JSON: weeks/<weekId>.pdf
"""

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
TEMPLATE = HERE / "template.html"
WEEKS_DIR = HERE / "weeks"

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]


def pick_chrome():
    for c in CHROME_CANDIDATES:
        if c and Path(c).exists():
            return c
    sys.exit("error: no Chrome/Chromium binary found")


def latest_week_json():
    files = sorted(WEEKS_DIR.glob("*.json"))
    if not files:
        sys.exit("error: no week JSON files in weeks/")
    return files[-1]


def render_stats(items):
    out = []
    for it in items:
        tone = it.get("tone", "")
        out.append(
            f'<div class="stat {tone}">'
            f'  <div class="k">{it["label"]}</div>'
            f'  <div class="v">{it["value"]}</div>'
            f'  <div class="x">{it["note"]}</div>'
            f"</div>"
        )
    return "\n".join(out)


def render_flow(items):
    out = []
    for i, it in enumerate(items, 1):
        tone = it.get("tone", "")
        out.append(
            f'<div class="step {tone}">'
            f'  <div class="num">{i}</div>'
            f'  <div class="icon">{it["icon"]}</div>'
            f'  <div class="label">{it["label"]}</div>'
            f'  <div class="desc">{it["desc"]}</div>'
            f"</div>"
        )
    return "\n".join(out)


def render_token_facts(items):
    out = []
    for it in items:
        out.append(
            f'<li><span class="lab">{it["lab"]}</span>{it["val"]}</li>'
        )
    return "\n".join(out)


def render_verify_links(items):
    out = []
    for it in items:
        out.append(
            f'<li style="border-color:#333">'
            f'<span class="lab" style="color:#aaa">{it["lab"]}</span>'
            f'<a href="{it["url"]}">{it["text"]}</a>'
            f"</li>"
        )
    return "\n".join(out)


def render_family(items):
    out = []
    for it in items:
        status = it.get("status", "live")
        label = it.get("statusLabel", status.capitalize())
        out.append(
            f'<div class="fam {status}">'
            f'  <span class="badge">{label}</span>'
            f'  <h4>{it["icon"]} {it["name"]}</h4>'
            f'  <p>{it["desc"]}</p>'
            f'  <div class="lnk"><a href="{it["url"]}">{it["urlText"]}</a></div>'
            f"</div>"
        )
    return "\n".join(out)


def render_tiers(items):
    out = []
    for it in items:
        out.append(
            f'<div class="tier {it["tone"]}">'
            f'  <div class="medal">{it["medal"]}</div>'
            f'  <div class="name">{it["name"]}</div>'
            f'  <div class="mul">{it["mul"]}</div>'
            f'  <div class="desc">{it["desc"]}</div>'
            f"</div>"
        )
    return "\n".join(out)


def render_timeline(items):
    out = []
    for it in items:
        out.append(
            f'<div class="tl-item">'
            f'  <div class="date">{it["date"]}</div>'
            f'  <div class="title">{it["title"]}</div>'
            f'  <div class="note">{it["note"]}</div>'
            f"</div>"
        )
    return "\n".join(out)


def render_next(items):
    out = []
    for it in items:
        tone = it.get("tone", "")
        out.append(
            f'<li class="{tone}"><b>{it["title"]}</b>{it["desc"]}</li>'
        )
    return "\n".join(out)


def render_daily_loop(items):
    return "\n".join(f"<li>{x}</li>" for x in items)


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg == "latest" or arg is None:
        data_path = latest_week_json()
    else:
        data_path = Path(arg)
        if not data_path.exists():
            sys.exit(f"error: {data_path} not found")

    with data_path.open() as f:
        data = json.load(f)

    tpl = TEMPLATE.read_text()

    substitutions = {
        "TITLE": data["title"],
        "SUBTITLE": data["subtitle"],
        "DATE_RANGE": data["dateRange"],
        "GEN_DATE": data["genDate"],
        "STATS_HTML": render_stats(data["stats"]),
        "FLOW_HTML": render_flow(data["flow"]),
        "FLOW_NOTE": data["flowNote"],
        "TOKEN_FACTS_HTML": render_token_facts(data["tokenFacts"]),
        "VERIFY_LINKS_HTML": render_verify_links(data["verifyLinks"]),
        "FAMILY_HTML": render_family(data["family"]),
        "TIERS_HTML": render_tiers(data["tiers"]),
        "TIERS_NOTE": data["tiersNote"],
        "TIMELINE_HTML": render_timeline(data["timeline"]),
        "NEXT_HTML": render_next(data["next"]),
        "TG_URL": data["tgUrl"],
        "TG_URL_DISPLAY": data["tgUrlDisplay"],
        "TG_DESC": data["tgDesc"],
        "TG_META": data["tgMeta"],
        "DAILY_LOOP_HTML": render_daily_loop(data["dailyLoop"]),
        "FOOTER_NOTE": data["footerNote"],
    }

    html = tpl
    for k, v in substitutions.items():
        html = html.replace("{{" + k + "}}", v)

    leftovers = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if leftovers:
        sys.exit(f"error: unsubstituted placeholders remain: {sorted(set(leftovers))}")

    week_id = data["weekId"]
    out_html = WEEKS_DIR / f"{week_id}.rendered.html"
    out_pdf = WEEKS_DIR / f"{week_id}.pdf"
    out_html.write_text(html)

    chrome = pick_chrome()
    subprocess.run(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={out_pdf}",
            f"file://{out_html.resolve()}",
        ],
        check=True,
        stderr=subprocess.DEVNULL,
    )

    # also overwrite the canonical SOAG-WEEKLY.pdf as the latest
    latest_pdf = HERE / "SOAG-WEEKLY.pdf"
    shutil.copy2(out_pdf, latest_pdf)

    print(f"✓ rendered {out_pdf}")
    print(f"✓ latest:   {latest_pdf}")


if __name__ == "__main__":
    main()
