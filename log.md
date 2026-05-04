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

## [2026-05-03] query | Cartão vs reserva — re-asked after Rico schedule update
- pages consulted: [[Finances]], [[Financial Goals]], [[Source: Finances]]
- output: chat (offer to file as `wiki/projects/reserva-2026-jan2027.md` pending user decision)
- notes:
  - SAME question as the 2026-05-02 query, but the answer **inverted** — Rico is parcelada (not rotativo), implicit rate ~zero (sum of faturas R$ 40,924 ≈ balance R$ 42,600). No material benefit to prepaying.
  - New recommendation: build reserve from cash-flow surplus, don't touch portfolio. Plan: reserve-piso R$ 5k by Jul/2026; "6-month rule" satisfied at R$ 21k by Nov/2026; R$ 30k goal reached Jan/2027.
  - Mai/2026 R$ 7k deficit: cover with R$ 5k buffer + R$ 2k discretionary cut (NOT from reserve).
  - Demonstrates a load-bearing wiki property: when source data changes, the right answer can fully invert. Yesterday's advice would now be actively wrong.

## [2026-05-03] query | Pontos bons e ruins da situação financeira atual
- pages consulted: [[Finances]], [[Financial Goals]], [[International Relocation]], [[Fluencypass]], [[Stephanie]], [[Lorena]], [[Health]], [[Source: Finances]]
- output: chat (offer to file as `wiki/self/strengths-weaknesses-2026-05.md` pending user decision)
- notes:
  - Bons: 4 categories (estrutura, execução, dívida controlada, trajetória). Highlight: auto-consciência financeira do próprio Yago, parcelamento Rico controlado, surplus crescente.
  - Ruins: 5 categories (liquidez crítica, concentração tripla, lacunas de informação, lifestyle desproporcional, estratégia frouxa).
  - **NEW observations not yet in wiki** (worth filing if Yago confirms):
    - Lifestyle disproportion: iFood ~10% of burn vs R$ 2k reserve; BMW R$ 88k vs reserve R$ 2k as implicit trade-off
    - Education savings gap: Lorena R$ 3k/mo present spend, zero future-savings — orthogonal blind spot
    - Apartment financing horizon not documented (how many years left on the parcela?)
    - Pattern observation: Rico provisão accumulated without extinguishing → possible structural postponement habit
  - Top-3 leverage actions surfaced: reserve to R$ 5k by Jul/2026; Stephanie conversation + journal entry; FX hedge R$ 1k/mo from Jun/2026.

## [2026-05-03] ingest | 6 raw files (Career.md + Family/* tree)
- pages created (sources): [[Source: Career]], [[Source: Stephanie's Identity]], [[Source: Stephanie's Career]], [[Source: Lorena's Identity]], [[Source: Lorena's Education]]
- pages updated (sources): [[Source: Identity]] (Lorena birthdate corrected, wikilinks added)
- pages created (wiki): [[Career History]], [[Stephanie Career]], [[Lorena Education]], [[Joint Plans]]
- pages updated (wiki): [[Profile]], [[Stephanie]], [[Lorena]], [[Fluencypass]], [[International Relocation]], [[Financial Goals]], [[Index]]
- key resolutions:
  - **Stephanie aligned with relocation** — biggest prior unknown closed. She wants to work abroad; flexible on initial role.
  - **Yago's career fully documented** — Staff SWE @ Fluencypass 2y7m, partner with R$ 2.5k/mo equity buy-in (NEW info, not currently broken out in [[Finances]]), Java/Spring/AWS + AI/LLM, B1 English, Bachelor's only, active job search at R$ 45k+/mo floor.
  - **Lorena birthdate corrected**: 2015-03-22 (was 2015-03-23 in original [[Source: Identity]]).
  - **EB2-NIW eligibility analysis updated** in [[International Relocation]] — easily meets experience prong; dossier light on publications/OSS/talks; English B1 is biggest gap.
- new boundaries / durable rules:
  - **Advisor does NOT advise on Stephanie's career.** Boundary explicitly set in [[Source: Stephanie's Career]]. Saved as feedback memory.
  - **Joint decisions live in [[Joint Plans]]**, not in individual person pages.
- new financial reconciliation flagged:
  - R$ 2,500/mo Fluencypass equity buy-in is NEW info not separately broken out in [[Finances]]. May or may not be inside the R$ 20k burn — confirmation needed; could shift surplus profile by R$ 2.5k/mo if on top.
- file organization observation:
  - User created `Family/Wife/` and `Family/Daughter/` sub-folders in raw/journal/. This is a useful pattern — should be reflected in the schema if it recurs (Family/ as a sub-category alongside the flat journal entries).

## [2026-05-03] re-ingest | Fluencypass salary structure clarified
- pages updated: [[Fluencypass]], [[Finances]], [[Career History]], [[Financial Goals]], [[International Relocation]], [[Source: Finances]], [[Source: Career]]
- raw/journal/Finances.md inflow table updated (with Yago's permission)
- key clarification:
  - Real PJ contract: R$ 31,500/month
  - R$ 2,500/mo voluntary equity buy-in (auto-deducted at source); no vesting, no cliff
  - Cumulative bought: R$ 72,500 since Nov 2023 (~30 months)
- resolution:
  - The R$ 2,500/mo is taken at SOURCE before cash reaches Yago — NOT in the R$ 20k burn ex-Rico.
  - Cash flow profile and surplus calculations in [[Finances]] are correct as written.
  - The buy-in is essentially forced savings into illiquid equity that Yago himself rules as zero for planning — paradox worth surfacing in future discussions.
- new framing: the buy-in decision is now a clear actionable monthly choice (continue / pause / unwind), directly mapped to Yago's open Q2 in [[Source: Career]]: "is Fluencypass equity better than working abroad?"
- math note: 30 months × R$ 2,500 = R$ 75,000 bought; current value R$ 72,500 — small ~R$ 2,500 (~3%) gap. Either ~29-month effective start window or modest unrealized loss. Worth Yago verifying.

## [2026-05-03] re-ingest | Finances.md revised by Yago (15:18)
- raw/journal/Finances.md changes detected: 6 items
  - NEW risk "Fees for liquidating stock portfolio" (R$ 20k/mo IR exemption rule documented)
  - NEW section "Family intersections" — Stephanie BR earning potential ~R$ 3k/mo, costs to enable her return to work (transport + Lorena meals R$ 500)
  - removed obsolete "Provisões R$ 9,200" line from outflows
  - downgraded "Credit card revolving" risk to Low
  - 6-month reserve target updated to R$ 120k (now matches wiki)
  - removed "Open questions for me to answer" section
- pages updated: [[Source: Finances]] (modifications log), [[Finances]] (new risk row), [[Joint Plans]] (major: family intersections)
- key new insight: with R$ 3k BR earning estimate vs ~R$ 700-1k enabling costs, Stephanie returning to work in BR would add ~R$ 2-2.3k/mo to household cash flow. Boundary respected — flagged as joint-plan input, not advised on.
- pattern noted: Yago's raw `Finances.md` is the canonical living planning doc. Strong convention. Future ingest workflow should always re-read this file specifically when Yago says "update wiki based on raw."
- pages consulted: [[International Relocation]], [[Finances]], [[Profile]], [[Lorena]], [[Stephanie]], [[Fluencypass]]
- web research used: BLS, PayScale, Colombo&Hurd, Numbeo (cost of living)
- output: chat (offer to file as `wiki/projects/eb2-niw-research-2026-05.md`)
- key findings:
  - US software dev salary 2026: median $133k base (BLS); senior total comp $180-280k typical; FAANG senior $250-400k+.
  - EB2-NIW realistic for Yago's profile IF: Bachelor's + 5y progressive exp, plus dossier (publications/awards/impact). Self-petitioned, $8-15k legal.
  - **CRITICAL UNVERIFIED FACT**: Jan 21, 2026 — US paused immigrant visa issuance for ~75 countries including Brazil per one source. I-140 filing still possible but consular processing halted. Yago must verify with immigration lawyer before acting. Single-source finding flagged.
  - Cost-of-living adjustment: SP ~58% cheaper than NYC, ~65% cheaper than Seattle ex-rent. Not a simple salary multiplier.
- 7 wiki data gaps surfaced that block personalized recommendation: Yago's role/seniority/stack at [[Fluencypass]], English level, education credential, NIW dossier evidence (publications/awards), [[Stephanie]] alignment + career, motivation (push vs pull), [[Lorena]] English level.
- timing-coincidence flagged: NIW realistic timeline (18-30 months from filing) approximately aligns with Mar/2027 end of Rico parcelamento — financial readiness and visa readiness can converge.
- recommendation: not a single decision, a multi-fase project. Phase 0 → answer the 7 gap questions (zero cost, weeks). Don't file I-140 yet.

## [2026-05-04] ingest | raw/journal/Investment Thesis.md (NEW) + Finances.md revision
- pages created (sources): [[Source: Investment Thesis]]
- pages created (wiki): [[Investment Thesis]] (in wiki/self/)
- pages updated: [[Fluencypass]] (operating metrics block + valuation framing + open follow-ups), [[Finances]] (Mai/2026 fatura, Rico total, portfolio thesis link, risk table), [[Source: Finances]] (modifications log)
- key new factual data (first wiki documentation):
  - Fluencypass MRR ~R$ 1.25M (≈ R$ 15M ARR), ~120 employees, 82% B2C / 10% study abroad / 8% B2B
  - B2C churn 9-11%/month, LTV 8-12 months — high churn structurally drives B2B pivot
  - B2B launched Nov 2025; target 30% of revenue by end of 2026 (from 8% today, requires ~4x B2B revenue)
  - Investment philosophy explicit: Barsi/AGF dividend methodology for the public bucket; growth thesis applies only to FP
- corrections to wiki framing:
  - Stock portfolio concentration was previously framed neutrally as "risk" — now reframed as **intentional methodology** per [[Investment Thesis]]; concentration is a deliberate Barsi-style choice, not an oversight. Risk row retained but annotated.
  - Mai/2026 Rico fatura up R$ 1,356 (R$ 13,444.48 → R$ 14,800.48); cash deficit grows from R$ 7k to R$ 8.3k. Rico schedule total now R$ 42,280.34 — closes gap to balance to ~R$ 320 (was R$ 1.7k).
- analytical insight surfaced: with concrete FP metrics now documented, the "10x exit" framing used in earlier conversations gets sharper. Realistic BR EdTech multiples (2-3x revenue) give FP enterprise value R$ 30-45M today; for Yago's R$ 75k buy-in to reach R$ 750k (10x), the **valuation itself must grow 10x** — not just the multiple at exit. Documented in [[Fluencypass#Valuation framing]] and [[Investment Thesis]].
- new open questions surfaced:
  - FP's current internal valuation used to set buy-in price (blocks % ownership math)
  - MRR growth trajectory + B2B pivot trajectory (blocks P(exit) calibration)
  - B2C churn trend (Yago's source notes FP itself lacks visibility)
- thesis-orphan tension flagged in [[Investment Thesis]]: building USD savings for [[International Relocation]] FX hedge does not fit either of Yago's two existing buckets (dividend or insider growth) — a third bucket would need to be named.
