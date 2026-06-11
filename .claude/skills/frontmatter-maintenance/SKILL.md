---
name: frontmatter-maintenance
description: Keep YAML frontmatter on raw/ wiki notes correct per the CLAUDE.md schema — bump `updated:` to today and scaffold missing frontmatter (type/domain/created/updated/lang). A git pre-commit hook does this automatically for files in each commit; this skill is the manual entry point and documents the mechanism. Triggers when Yago asks to fill/normalize/refresh frontmatter, fix `updated:` dates, or asks how the commit-time frontmatter automation works.
---

# Frontmatter maintenance — automatic at commit, manual on demand

`raw/` notes must carry the CLAUDE.md frontmatter (`type, domain, created, updated, lang`, plus optional `entity/relation/links`). Keeping `updated:` honest by hand is easy to forget, so it's automated.

## Automatic (the real mechanism): git pre-commit hook

A tracked hook fills frontmatter on **only the files added/modified in each commit**, then re-stages them — so every commit lands with correct metadata regardless of who runs `git commit`.

- **Hook:** `.githooks/pre-commit` → runs `.githooks/fill-frontmatter.py` with no args (staged mode).
- **Scope:** `raw/**/*.md` only. Files outside `raw/` (e.g. `.claude/skills/*/SKILL.md`, root `README.md`/`CLAUDE.md`) are deliberately ignored — their frontmatter is a different schema and must not be touched.

### How it gets armed (two layers)

Git never runs versioned hooks automatically (security), so the repo's `.githooks/` has to be wired up. Two mechanisms cover that:

1. **This clone:** `git config core.hooksPath .githooks` (local config — already set here).
2. **Every *future* clone on this machine, zero-touch:** a global git template seeds a dispatcher into each new clone's `.git/hooks/`:
   - `~/.config/git/template/hooks/pre-commit` — a generic dispatcher that `exec`s `<repo>/.githooks/<hookname>` when present, else no-ops.
   - Armed with `git config --global init.templateDir ~/.config/git/template`.
   - On `git clone`, git copies that dispatcher into `.git/hooks/`; since a clone has no local `core.hooksPath`, the dispatcher runs and delegates to this repo's `.githooks/`. Verified working.

**On a brand-new machine** (where the global template doesn't exist yet), re-create those two pieces, or just run `git config core.hooksPath .githooks` in the clone. The dispatcher is safe for all repos — it only acts when a repo ships `.githooks/`.

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
