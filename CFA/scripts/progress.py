#!/usr/bin/env python3
"""Progress reporting for the CFA Level I course.

Reads curriculum.json for the plan and trackers/progress-tracker.md for what you have
ticked, then prints completion by topic. No dependencies beyond the standard library.

    python3 scripts/progress.py              completion summary
    python3 scripts/progress.py --next       what to study next
    python3 scripts/progress.py --day 47     what the plan says for a given day
    python3 scripts/progress.py --remaining  hours left, and days at 4h/day
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM = os.path.join(ROOT, "curriculum.json")
TRACKER = os.path.join(ROOT, "trackers", "progress-tracker.md")

# "| [x] | 03 | [Name](path) | 8 | [x] | [ ] | [ ] |"
ROW = re.compile(
    r"^\|\s*\[(?P<done>[ xX])\]\s*\|\s*(?P<lm>\d+)\s*\|\s*\[(?P<name>[^\]]+)\]"
    r"[^|]*\|\s*(?P<hours>\d+)\s*\|"
    r"\s*\[(?P<p1>[ xX])\]\s*\|\s*\[(?P<p2>[ xX])\]\s*\|\s*\[(?P<p3>[ xX])\]\s*\|"
)
HEADING = re.compile(r"^##\s+(?P<order>\d+)\.\s+(?P<name>.+?)\s+·")


def load_curriculum():
    with open(CURRICULUM, encoding="utf-8") as fh:
        return json.load(fh)


def load_ticks():
    """Return {topic_name: {lm: {'done':bool,'p1':bool,'p2':bool,'p3':bool}}}."""
    if not os.path.exists(TRACKER):
        return {}
    ticks, current = {}, None
    with open(TRACKER, encoding="utf-8") as fh:
        for line in fh:
            head = HEADING.match(line)
            if head:
                current = head.group("name").strip()
                ticks.setdefault(current, {})
                continue
            row = ROW.match(line)
            if row and current:
                ticks[current][int(row.group("lm"))] = {
                    "done": row.group("done").lower() == "x",
                    "p1": row.group("p1").lower() == "x",
                    "p2": row.group("p2").lower() == "x",
                    "p3": row.group("p3").lower() == "x",
                }
    return ticks


def bar(pct, width=24):
    filled = int(round(pct / 100 * width))
    return "█" * filled + "·" * (width - filled)


def cmd_summary(cur, ticks):
    print()
    print(f"  CFA Level I · {cur['curriculum_year']} curriculum")
    print(f"  {cur['totals']['modules']} modules · {cur['totals']['hours']} hours · "
          f"{cur['plan']['days']} days\n")
    print(f"  {'Topic':<38} {'Done':>7}  {'Hours':>11}  Progress")
    print("  " + "-" * 76)

    tot_mod = tot_done = 0
    tot_hrs = tot_hrs_done = 0
    for t in cur["topics"]:
        tk = ticks.get(t["name"], {})
        done = sum(1 for m in t["modules"] if tk.get(m["lm"], {}).get("done"))
        hrs_done = sum(m["hours"] for m in t["modules"] if tk.get(m["lm"], {}).get("done"))
        n, hrs = t["module_count"], t["hours"]
        pct = 100 * done / n if n else 0
        tot_mod += n; tot_done += done; tot_hrs += hrs; tot_hrs_done += hrs_done
        print(f"  {t['name'][:37]:<38} {done:>3}/{n:<3} {hrs_done:>5}/{hrs:<5}  "
              f"{bar(pct)} {pct:5.1f}%")

    print("  " + "-" * 76)
    pct = 100 * tot_done / tot_mod if tot_mod else 0
    print(f"  {'TOTAL':<38} {tot_done:>3}/{tot_mod:<3} {tot_hrs_done:>5}/{tot_hrs:<5}  "
          f"{bar(pct)} {pct:5.1f}%")

    p2 = sum(1 for t in cur["topics"] for m in t["modules"]
             if ticks.get(t["name"], {}).get(m["lm"], {}).get("p2"))
    p3 = sum(1 for t in cur["topics"] for m in t["modules"]
             if ticks.get(t["name"], {}).get(m["lm"], {}).get("p3"))
    print(f"\n  Retrieval (P2): {p2}/{tot_mod}    Consolidation (P3): {p3}/{tot_mod}")
    if p2 < tot_done * 0.6 and tot_done > 5:
        print("  ! P2 is lagging P1. Re-reading without retrieval builds familiarity, not recall.")
    print()


def cmd_next(cur, ticks):
    for t in cur["topics"]:
        if t.get("parallel"):
            continue
        tk = ticks.get(t["name"], {})
        for m in t["modules"]:
            if not tk.get(m["lm"], {}).get("done"):
                print(f"\n  Next up  ·  {t['name']}  (LM{m['lm']:02d})")
                print(f"  {m['name']}")
                print(f"  Budget: {m['hours']} hours")
                print(f"  File:   {m['file']}\n")
                eth = next((x for x in cur["topics"] if x.get("parallel")), None)
                if eth:
                    etk = ticks.get(eth["name"], {})
                    nxt = next((e for e in eth["modules"]
                                if not etk.get(e["lm"], {}).get("done")), None)
                    if nxt:
                        print(f"  Parallel (1h/day) · Ethics LM{nxt['lm']:02d}: {nxt['name']}\n")
                return
    print("\n  All core modules complete. Move to docs/study-plan/revision-phase.md\n")


def cmd_day(cur, day):
    print()
    hit = False
    for t in cur["topics"]:
        if t["day_start"] <= day <= t["day_end"]:
            if t.get("split"):
                for s in t["split"]:
                    if s["day_start"] <= day <= s["day_end"]:
                        print(f"  Day {day}  ·  {t['name']} ({s['label']})  "
                              f"— block days {s['day_start']}–{s['day_end']}")
                        hit = True
            else:
                tag = " [parallel, 1h/day]" if t.get("parallel") else ""
                print(f"  Day {day}  ·  {t['name']}{tag}  "
                      f"— block days {t['day_start']}–{t['day_end']}")
                hit = True
    if not hit:
        print(f"  Day {day} is outside the 150-day plan.")
    print()


def cmd_remaining(cur, ticks):
    left = [(t, m) for t in cur["topics"] for m in t["modules"]
            if not ticks.get(t["name"], {}).get(m["lm"], {}).get("done")]
    core = [(t, m) for t, m in left if not t.get("parallel")]
    eth = [(t, m) for t, m in left if t.get("parallel")]
    ch = sum(m["hours"] for _, m in core)
    eh = sum(m["hours"] for _, m in eth)
    print()
    print(f"  Core modules remaining:   {len(core):>3}   {ch:>4} hours"
          f"   ≈ {ch / 4:>5.1f} days at 4h/day")
    print(f"  Ethics modules remaining: {len(eth):>3}   {eh:>4} hours"
          f"   ≈ {eh / 1:>5.1f} days at 1h/day")
    print(f"  Total:                    {len(left):>3}   {ch + eh:>4} hours")
    print(f"\n  At 5h/day the remaining work is ~{max(ch / 4, eh):.0f} calendar days.\n")


def main():
    ap = argparse.ArgumentParser(description="CFA Level I course progress")
    ap.add_argument("--next", action="store_true", help="what to study next")
    ap.add_argument("--day", type=int, metavar="N", help="what the plan says for day N")
    ap.add_argument("--remaining", action="store_true", help="hours left")
    args = ap.parse_args()

    try:
        cur = load_curriculum()
    except FileNotFoundError:
        sys.exit(f"curriculum.json not found at {CURRICULUM}")
    ticks = load_ticks()

    if args.day is not None:
        cmd_day(cur, args.day)
    elif args.next:
        cmd_next(cur, ticks)
    elif args.remaining:
        cmd_remaining(cur, ticks)
    else:
        cmd_summary(cur, ticks)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:  # e.g. piped into `head`
        try:
            sys.stdout.close()
        finally:
            os._exit(0)
