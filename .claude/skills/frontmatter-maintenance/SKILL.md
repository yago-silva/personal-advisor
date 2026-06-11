---
name: frontmatter-maintenance
description: Keep YAML frontmatter on raw/ wiki notes correct per the CLAUDE.md schema — bump `updated:` to today and scaffold missing frontmatter (type/domain/created/updated/lang). A git pre-commit hook does this automatically for files in each commit; this skill is the manual entry point and documents the mechanism. Triggers when Yago asks to fill/normalize/refresh frontmatter, fix `updated:` dates, or asks how the commit-time frontmatter automation works.
---

# Frontmatter maintenance — automatic at commit, manual on demand

`raw/` notes must carry the CLAUDE.md frontmatter (`type, domain, created, updated, lang`, plus optional `entity/relation/links`). Keeping `updated:` honest by hand is easy to forget, so it's automated.

## Automatic (the real mechanism): git pre-commit hook

A tracked hook fills frontmatter on **only the files added/modified in each commit**, then re-stages them — so every commit lands with correct metadata regardless of who runs `git commit`.

- **Logic (versioned):** `.githooks/fill-frontmatter.py` + `.githooks/pre-commit` — live in the repo so the rules travel with it.
- **Trigger (classic, NOT versioned):** `.git/hooks/pre-commit` — a thin wrapper that `exec`s `.githooks/pre-commit`. This is the standard git hook location; `core.hooksPath` is intentionally left unset.
- **Scope:** `raw/**/*.md` only. Files outside `raw/` (e.g. `.claude/skills/*/SKILL.md`, root `README.md`/`CLAUDE.md`) are deliberately ignored — their frontmatter is a different schema and must not be touched.

### Re-installing after a fresh clone

Git never runs versioned hooks automatically (security), and `.git/hooks/` isn't cloned — so each new clone needs the wrapper installed once:

```bash
# from the repo root, after cloning:
printf '#!/usr/bin/env bash\nexec "$(git rev-parse --show-toplevel)/.githooks/pre-commit"\n' \
  > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

(A symlink works too: `ln -sf ../../.githooks/pre-commit .git/hooks/pre-commit`.) This is a deliberate, repo-local choice — no global git config is touched.

Per-file behavior:
- Always rewrites `updated:` to today (inserts the key if absent).
- Newly **added** files with no `created:` get `created: <today>`.
- Files with **no frontmatter at all** get a scaffold: `type: note`, `domain:` inferred from `raw/<Top>/…`, `created` (today if new, else `unknown`), `updated: today`, `lang: pt`.
- Existing keys, values, and key order are preserved — only `updated` is overwritten.
- The hook never blocks a commit: on any error it warns and exits 0.

**Defaults worth correcting by hand:** scaffolded `lang: pt` (Yago's primary) and inferred `domain` are best-guesses. If a note is EN or sits in an unusual path, fix those two fields after the scaffold lands.

## Manual run (this skill)

To normalize files without committing — e.g. a batch you just authored, or to preview what the hook will do:

```bash
# from repo root; pass specific files (only raw/*.md are acted on; index untouched)
python3 .githooks/fill-frontmatter.py raw/Health/"Some Note.md" raw/Self/Identity.md
```

Manual mode rewrites files in place but does **not** `git add` them and does **not** infer "new" (so it won't invent a `created:` — it uses `unknown` when scaffolding). Use it to tidy, then stage as usual; the pre-commit hook will still bump `updated:` at commit time.

## Notes

- Date comes from the system clock at run time (`date`/`date.today()`), never hardcoded — so it's correct whenever it fires.
- Enforces CLAUDE.md convention #4. Complements [[consult-linked-sources]] / [[finance-wiki-references]] which govern *content*, not metadata.
