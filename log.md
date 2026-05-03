# Log

Chronological record of wiki activity. Append-only. Each entry starts with `## [YYYY-MM-DD] <op> | <subject>` for greppability.

## [2026-05-02] bootstrap
- created CLAUDE.md (schema)
- created directory structure: raw/{articles,journal,transcripts,assets}, wiki/{self,career,people,concepts,projects,sources}
- created index.md and log.md
- notes: Personal Advisor wiki initialized as hybrid personal life + career advisor. Language: English. Source types optimized for: web articles (Obsidian Web Clipper), personal journal entries, podcast/video transcripts. User: Yago Silva (FluencyPass).

## [2026-05-02] ingest | Identity, Health, Goals, Finances (4 files)
- pages created (sources): [[Source: Identity]], [[Source: Health]], [[Source: Goals]], [[Source: Finances]]
- pages created (wiki): [[Profile]], [[Health]], [[Finances]], [[Financial Goals]], [[Fluencypass]], [[Lorena]], [[Stephanie]], [[International Relocation]]
- pages updated: [[Index]]
- notes:
  - All 4 source files were placed in `raw/assets/` but per CLAUDE.md belong in `raw/journal/` (raw/assets is for images/PDFs). Misplacement noted; move pending user approval.
  - [[Source: Goals]] and [[Source: Finances]] partially overlap on financial goals. Goals.md sets aspirational R$ 45k/mo passive; Finances.md is more conservative (~R$ 27k/mo eventually). Tension recorded on [[Financial Goals]].
  - [[Stephanie]] page is mostly lint — her role in household finances is the largest unstated assumption; flagged.
  - [[Fluencypass]] page is data-thin: no role, tenure, or company description. Worth a journal entry.
  - [[Health]] page is sparse despite ~R$ 1.5–2k/month wellness spend. Lint flagged.
  - From [[Source: Finances]] "Things to push back on": four standing instructions (don't run zero-reserve past 6mo; no equity buys before reserve; no <90d apartment sale assumption; don't count Fluencypass equity as decision-grade) — durably recorded on [[Finances]].
  - 4 open questions from [[Source: Finances]] preserved as a tracked list on [[Finances]] and surfaced on the relevant entity pages.

## [2026-05-02] move | raw/assets/ → raw/journal/
- moved: Identity.md, Goals.md, Health.md, Finances.md
- updated source_path in: [[Source: Identity]], [[Source: Goals]], [[Source: Health]], [[Source: Finances]]
- notes: corrected misplacement (raw/assets is for images/PDFs per CLAUDE.md). Original filenames preserved (PascalCase) since these are user-authored source files.

## [2026-05-03] modify | raw/journal/Finances.md — Rico schedule added
- inserted "### Rico — cronograma de faturas (Mai/2026 → Mar/2027)" subsection after Liabilities table
- 11-month empty table for Yago to fill (fatura, saldo restante, notas)
- IMPORTANT: this is a write to a raw/ file, which CLAUDE.md flags as immutable. Pattern violation acknowledged. Future similar updates should consider creating a dated snapshot (e.g. raw/journal/Finances-2026-05.md) instead.
- KEY FACTUAL UPDATE: Rico debt is **parcelada**, not pure revolving. This invalidates the assumption used in the 2026-05-02 query analysis ("Cartão ou reserva primeiro"). [[Finances]] still labels Rico as "Revolving" — needs correction. Parcelado rates (typically 8–12% a.a.) are an order of magnitude lower than revolving (~12–15% a.m.), which materially changes the urgency calculus.

## [2026-05-03] re-ingest | raw/journal/Finances.md (Rico schedule filled + burn revised)
- pages updated: [[Source: Finances]], [[Finances]], [[Financial Goals]], [[International Relocation]]
- notes:
  - Yago filled the 11-month Rico fatura schedule (Mai/2026 → Mar/2027), total R$ 40,924.34. Source-of-truth answers the "structural or one-off" open question: parcelada with fixed schedule.
  - Yago revised monthly burn from R$ 27k → R$ 20k (now excludes Rico, tracked separately).
  - Material analytical implications:
    - The 2026-05-02 cartão-vs-reserva analysis (which assumed revolving rates) is superseded — Rico is no longer an active decision, just a tracked commitment.
    - May/2026 has a ~R$ 7k cash deficit from the R$ 13.4k Rico spike. New "Medium" severity risk added.
    - Cumulative surplus Jun/2026 → Mar/2027 ~R$ 37k makes the R$ 30k reserve goal cash-flow feasible without portfolio liquidation. Significant strategic shift.
    - 6-month reserve target re-baselined: ~R$ 120k (was R$ 160k) at the new R$ 20k burn.
    - Rico downgraded to Low risk (was Medium); thin-surplus risk removed.
    - Mar/2027 emerges as a meaningful date-anchor for [[International Relocation]] timing — added as new tracked decision item there.
  - Total scheduled (R$ 40,924) is ~R$ 1.7k under current balance (R$ 42,600) — possible residual interest accruing; flagged for Yago to confirm on next actual fatura.
