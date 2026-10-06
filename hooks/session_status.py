#!/usr/bin/env python3
"""Book Skills SessionStart hook: one compact pipeline status line.

Resolves the workspace like shared/workspace.md section 1 (./.book-skills,
$BOOK_SKILLS_HOME, ~/.book-skills). No workspace, or nothing notable -> prints
nothing. Stdlib only. Never raises, never blocks: any problem -> exit 0 silently.
"""
import json
import os
import re
import sys

MAX_CHARS = 400
REVIEW_STALE_DAYS = 14
STAGE_WEIGHT = {"lead": 0.1, "discovery": 0.2, "proposal": 0.5,
                "negotiation": 0.7, "nurture": 0.05}
CLOSED = {"won", "lost"}
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
REVIEW_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\b")


def read_stdin_json():
    try:
        if sys.stdin is None or sys.stdin.isatty():
            return {}
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def resolve_workspace(cwd):
    candidates = [os.path.join(cwd or os.getcwd(), ".book-skills"),
                  os.environ.get("BOOK_SKILLS_HOME", ""),
                  os.path.join(os.path.expanduser("~"), ".book-skills")]
    for d in candidates:
        if d and os.path.isdir(d):
            return d
    return None


def clean_value(v):
    v = v.strip()
    if v[:1] in ("'", '"'):
        q = v[0]
        end = v.find(q, 1)
        return v[1:end] if end > 0 else v[1:]
    if " #" in v:
        v = v.split(" #", 1)[0]
    return v.strip()


def parse_frontmatter(path):
    fm = {}
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:200]:
        if line.strip() == "---":
            break
        if "example: delete" in line or ":" not in line or line.startswith((" ", "\t", "#")):
            continue
        key, _, val = line.partition(":")
        fm[key.strip().lower()] = clean_value(val)
    return fm


def to_date(s):
    import datetime
    m = DATE_RE.match((s or "").strip())
    if not m:
        return None
    try:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def to_number(s):
    try:
        return float(re.sub(r"[^\d.\-]", "", s or "") or "x")
    except ValueError:
        return None


def last_review(ws):
    path = os.path.join(ws, "memory", "outreach-learnings.md")
    latest = None
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if "example" in line:
                    continue
                m = REVIEW_RE.match(line.strip())
                if m:
                    d = to_date(m.group(1))
                    if d and (latest is None or d > latest):
                        latest = d
    except Exception:
        return None
    return latest


def fmt_money(v):
    if v >= 10000:
        return "%dk" % round(v / 1000.0)
    return "{:,}".format(int(round(v)))


def build(ws):
    import datetime
    today = datetime.date.today()
    deals_dir = os.path.join(ws, "deals")
    open_deals, overdue, no_next = [], [], []
    weighted, currencies, value_seen = 0.0, set(), False
    names = sorted(os.listdir(deals_dir)) if os.path.isdir(deals_dir) else []
    for name in names:
        if not name.endswith(".md") or name.startswith((".", "_")):
            continue
        try:
            fm = parse_frontmatter(os.path.join(deals_dir, name))
        except Exception:
            continue
        if not fm:
            continue
        stage = fm.get("stage", "").lower()
        if stage in CLOSED or "|" in stage:
            continue
        slug = fm.get("slug") or name[:-3]
        company = fm.get("company") or slug
        open_deals.append(slug)
        val = to_number(fm.get("value", ""))
        if val is not None:
            value_seen = True
            weighted += val * STAGE_WEIGHT.get(stage, 0.2)
            if fm.get("currency"):
                currencies.add(fm["currency"].upper())
        nsd = to_date(fm.get("next_step_date", ""))
        if not fm.get("next_step") or nsd is None:
            no_next.append(slug)
        elif nsd < today:
            overdue.append(((today - nsd).days, company, slug))

    review = last_review(ws)
    review_days = (today - review).days if review else None

    review_stale = review_days is not None and review_days > REVIEW_STALE_DAYS
    if not (overdue or no_next or review_stale):
        return ""

    parts = []
    if open_deals:
        p = "%d open" % len(open_deals)
        if value_seen:
            cur = next(iter(currencies)) + " " if len(currencies) == 1 else ""
            p += " (weighted %s%s)" % (cur, fmt_money(weighted))
        parts.append(p)
    overdue.sort(reverse=True)
    if overdue:
        items = ", ".join("%s %dd" % (c[:28], d) for d, c, _ in overdue[:3])
        more = " +%d" % (len(overdue) - 3) if len(overdue) > 3 else ""
        parts.append("overdue: " + items + more)
    if no_next:
        parts.append("no next step: " + ", ".join(s[:24] for s in no_next[:3])
                     + (" +%d" % (len(no_next) - 3) if len(no_next) > 3 else ""))
    if review_days is None:
        if open_deals:
            parts.append("no outreach review yet")
    elif review_days > REVIEW_STALE_DAYS:
        parts.append("outreach review %dd ago" % review_days)

    if overdue:
        hint = "/book-skills:deals rescue %s" % overdue[0][2]
    elif no_next:
        hint = "/book-skills:deals rescue %s" % no_next[0]
    else:
        hint = "/book-skills:outreach review"
    text = "Book Skills pipeline: " + "; ".join(parts) + ". Suggest: " + hint
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS - 1] + "~"
    return text


def main():
    data = read_stdin_json()
    cwd = data.get("cwd") if isinstance(data, dict) else None
    ws = resolve_workspace(cwd)
    if not ws:
        return
    text = build(ws)
    if not text:
        return
    sys.stdout.write(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart", "additionalContext": text}}))


if __name__ == "__main__":
    try:
        import signal
        if hasattr(signal, "SIGALRM"):
            signal.signal(signal.SIGALRM, lambda *_: os._exit(0))
            signal.alarm(4)
        main()
    except BaseException:
        pass
    sys.exit(0)
