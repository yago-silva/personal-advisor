#!/usr/bin/env python3
"""Fill / refresh YAML frontmatter on raw/ wiki notes per CLAUDE.md schema.

Two modes:
  - No args  -> "staged" mode: operates on git-staged (A/C/M) raw/*.md files,
                rewrites them and re-stages the result. Used by the pre-commit hook.
  - File args -> "manual" mode: operates on the given paths, rewrites in place,
                 does NOT touch the git index. Used by the frontmatter-maintenance skill.

Behavior per file (only under raw/, only *.md):
  - Always sets `updated:` to today (YYYY-MM-DD), inserting the key if absent.
  - If the file is newly ADDED and has no `created:`, inserts `created: <today>`.
  - If the file has NO frontmatter at all, prepends a scaffold:
        type: note
        domain: <inferred from raw/<Top>/...>
        created: <today if new else unknown>
        updated: <today>
        lang: pt        # default — Yago's primary language; correct per-note if wrong
Existing keys/values and key order are preserved; only `updated` is rewritten.
Never blocks a commit: on any unexpected error it warns and exits 0.
"""
import os
import re
import subprocess
import sys
from datetime import date

DOMAIN_BY_TOP = {
    "Career": "career", "Family": "family", "Finances": "finances",
    "Health": "health", "Plans": "plans", "Self": "self", "library": "library",
}
# Frontmatter block: opening '---' line, body, closing '---' line.
FM_RE = re.compile(r"^(---[ \t]*\n)(.*?\n)(---[ \t]*\n?)", re.DOTALL)


def repo_root():
    return subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"]).decode().strip()


def staged_files(diff_filter):
    out = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only",
         f"--diff-filter={diff_filter}", "-z", "--", "raw"]
    ).decode()
    return [f for f in out.split("\0") if f.endswith(".md")]


def infer_domain(rel):
    parts = rel.split("/")
    if len(parts) >= 2 and parts[0] == "raw":
        return DOMAIN_BY_TOP.get(parts[1], parts[1].lower())
    return None


def _find_key(lines, key):
    for i, ln in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", ln):
            return i
    return -1


def edit_fm_body(fm_body, today, is_new):
    """Return new frontmatter body text (no surrounding '---')."""
    lines = fm_body.split("\n")
    while lines and lines[-1] == "":
        lines.pop()

    ui = _find_key(lines, "updated")
    if ui >= 0:
        lines[ui] = f"updated: {today}"
    else:
        ci = _find_key(lines, "created")
        lines.insert(ci + 1 if ci >= 0 else len(lines), f"updated: {today}")

    if is_new and _find_key(lines, "created") < 0:
        ui = _find_key(lines, "updated")
        lines.insert(ui, f"created: {today}")

    return "\n".join(lines) + "\n"


def scaffold(rel, today, is_new):
    dom = infer_domain(rel)
    out = ["type: note"]
    if dom:
        out.append(f"domain: {dom}")
    out.append(f"created: {today if is_new else 'unknown'}")
    out.append(f"updated: {today}")
    out.append("lang: pt")
    return "---\n" + "\n".join(out) + "\n---\n\n"


def process_text(text, rel, today, is_new):
    bom = ""
    if text.startswith("﻿"):
        bom, text = "﻿", text[1:]
    m = FM_RE.match(text)
    if m:
        new_body = edit_fm_body(m.group(2), today, is_new)
        return bom + m.group(1) + new_body + m.group(3) + text[m.end():]
    return bom + scaffold(rel, today, is_new) + text


def main():
    today = date.today().isoformat()
    try:
        root = repo_root()
    except Exception as e:  # not a git repo / git missing
        print(f"frontmatter: skipped ({e})", file=sys.stderr)
        return 0

    manual = len(sys.argv) > 1
    if manual:
        rels = [os.path.relpath(os.path.abspath(p), root) for p in sys.argv[1:]]
        rels = [r for r in rels if r.startswith("raw" + os.sep) and r.endswith(".md")]
        added = set()
    else:
        rels = staged_files("ACM")
        added = set(staged_files("A"))

    changed = []
    for rel in rels:
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            new = process_text(text, rel.replace(os.sep, "/"), today, rel in added)
            if new != text:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
                changed.append(rel)
        except Exception as e:
            print(f"frontmatter: skipped {rel} ({e})", file=sys.stderr)

    if changed and not manual:
        subprocess.call(["git", "add", "--"] + changed)
    if changed:
        verb = "updated" if not manual else "rewrote"
        print("frontmatter: " + verb + " " + ", ".join(changed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
