# Log

Chronological record of wiki activity. Append-only. Each entry starts with `## [YYYY-MM-DD] <op> | <subject>` for greppability.

## [2026-05-02] bootstrap
- created CLAUDE.md (schema)
- created directory structure: raw/{articles,journal,transcripts,assets}, wiki/{self,career,people,concepts,projects,sources}
- created index.md and log.md
- notes: Personal Advisor wiki initialized as hybrid personal life + career advisor. Language: English. Source types optimized for: web articles (Obsidian Web Clipper), personal journal entries, podcast/video transcripts. User: Yago Silva (FluencyPass).

## [2026-05-02] ingest | Identity, Health, Goals, Finances (4 files)
- pages created (sources): [[Source: Identity]], [[Source: Health]], [[Source: Goals]], [[Source: Finances]]
- pages created (wiki): [[Profile]], [[wiki/self/health]], [[Finances]], [[Financial Goals]], [[Fluencypass]], [[Lorena]], [[Stephanie]], [[International Relocation]]
- pages updated: [[Index]]
- notes:
  - All 4 source files were placed in `raw/assets/` but per CLAUDE.md belong in `raw/journal/` (raw/assets is for images/PDFs). Misplacement noted; move pending user approval.
  - [[Source: Goals]] and [[Source: Finances]] partially overlap on financial goals. Goals.md sets aspirational R$ 45k/mo passive; Finances.md is more conservative (~R$ 27k/mo eventually). Tension recorded on [[Financial Goals]].
  - [[Stephanie]] page is mostly lint — her role in household finances is the largest unstated assumption; flagged.
  - [[Fluencypass]] page is data-thin: no role, tenure, or company description. Worth a journal entry.
  - [[wiki/self/health]] page is sparse despite ~R$ 1.5–2k/month wellness spend. Lint flagged.
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
- pages consulted: [[Finances]], [[Financial Goals]], [[International Relocation]], [[Fluencypass]], [[Stephanie]], [[Lorena]], [[wiki/self/health]], [[Source: Finances]]
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

## [2026-05-04 13:31] re-ingest | Investment Thesis.md (CEO pitch growth data added)
- raw/journal/Investment Thesis.md: Yago appended "Data from CEO pitch in general meet" section
  - **MRR growth: 13% YoY (Mar 2025 → Mar 2026)**
  - **+26% sales per seller** YoY
- pages updated: [[Source: Investment Thesis]] (modifications log + metrics table + observations), [[Fluencypass]] (growth row + revised valuation framing + closed one open question), [[Investment Thesis]] (new "Growth-trajectory analysis" section)
- key analytical update: 13% YoY MRR is **the single most important new data point** for evaluating the growth thesis. SaaS exits at 5-10x typically require 40-80% YoY growth. At 13%, FP compounds to only 1.44x in 3y / 1.84x in 5y, so the 5-10x stake math depends almost entirely on multiple expansion (AI premium / strategic acquirer) rather than fundamentals — a much narrower, riskier path.
- new framing introduced: the growth thesis is now better articulated as **"a bet on the B2B pivot landing"** rather than "a bet on FP being a great company." This produces falsifiable quarterly checkpoints through 2026:
  - Q2 2026: B2B share above 12-15%?
  - Q3 2026: above 18-22%?
  - Q4 2026: at/near 30% (the company plan)?
- consistency check: this new data is **consistent with**, not in contradiction to, the conversation-level "10x is cauda, 2-3x is realistic" framing converged earlier in the day. Strengthens the case the wiki was already pointing toward.
- one open question closed (MRR growth trajectory partially answered); two new open questions added (B2B trajectory tracking; whether 13% is accelerating or decelerating QoQ).

## [2026-05-04] re-ingest | Finances.md replanned outflows + consistency pass
- raw/journal/Finances.md: Yago replaced the prior aggregate ~R$ 20k/mo burn estimate with an itemized **R$ 17,320.70/mo** budget split into essential (R$ 8,454) + discretionary (R$ 8,866.70). Added explicit reserve-target table (quarterly/semiannual/annual × essential/discretionary). Mai/2026 Rico fatura revised to R$ 15,500.48 (was 14,800.48); new total Rico schedule R$ 42,980.34 (now ~R$ 180 above current balance). Numerical-consistency pass: net worth R$ 484,615.81 (was 479,233.55), liabilities R$ 255,800 (was 261,800 / 255,789.03), liquid investable R$ 137,398.21 (was 135,067.24), Rico balance R$ 42,800 throughout (was R$ 42,600 in prose), emergency-reserve formatting normalized. Effective liquid NW recomputed to ~R$ 102,000 (was ~R$ 98,000 — the old number used a stale R$ 135k portfolio figure). Cash runway updated to ~8 months. Near-term reserve goal updated to R$ 17,320.70 (1 month, was R$ 30k). 6-month reserve target updated to R$ 103,924 (was R$ 120k).
- pages updated: [[Source: Finances]] (modifications log + key takeaways + quotes), [[Finances]] (snapshot + assets + liabilities + Rico schedule + new replanned outflows section + new reserve-targets table + recomputed surplus profile), [[Financial Goals]] (near-term + medium-term + long-term re-baselined to new burn), [[International Relocation]] (Mar/2027 surplus updated to ~R$ 9.2k, was ~R$ 6.5k), [[Joint Plans]] (Stephanie cash-flow effect now ~13% of the new burn, was ~10%), [[Fluencypass]] (resolved buy-in reconciliation note rewritten in past tense)
- key analytical implications:
  - Surplus profile widens materially: Jun/2026 → Mar/2027 cumulative now **~R$ 64k** (was ~R$ 37k). Reserve-build timeline accelerates substantially without portfolio liquidation.
  - Mai/2026 deficit shrinks from R$ 8.3k to **R$ 6.3k** even with the higher R$ 15.5k Rico fatura — burn cut more than offsets the Rico revision.
  - 6-month reserve goal at the new burn is reachable from cash-flow surplus alone in ~14 months from Jun/2026 (≈ Aug/2027) — first time this milestone has been within reach without portfolio sale.
  - Long-term passive-income floor explicitly tied to **essential-only** (R$ 8,454/mo) per the new bucket split, not full burn — meaningful softening of the long-term target.
- consistency note: total Rico scheduled now slightly **exceeds** balance (R$ 42,980 vs R$ 42,800 = ~R$ 180 over). Previously schedule was under balance by ~R$ 1.7k. Worth confirming on next actual fatura whether this is interest-absorbed or a small estimation gap.

## [2026-05-17] re-ingest | Finances.md refreshed from XLSX (Patrimônio + Planejamento de Gastos) + consistency pass
- raw/journal/Finances.md updated from two spreadsheets (`Patrimônio Líquido.xlsx`, `2026 - Planejamento de Gastos.xls (2).xlsx`); subsequent review pass corrected 9 inline inconsistencies
- pages updated: [[Source: Finances]], [[Finances]], [[Financial Goals]], [[Investment Thesis]], [[Fluencypass]], [[International Relocation]], [[Joint Plans]], [[Index]]
- key factual updates:
  - **Net worth R$ 491,227.23** (was R$ 484,615.81). Gross assets R$ 751,893.95 / liabilities R$ 260,666.72.
  - **Stock portfolio R$ 131,402.17** (was R$ 137,398.21 — down ~R$ 6k). Per-ticker breakdown flagged as stale (spreadsheets carry only aggregate).
  - **FP equity at par**: cumulative R$ 75,000 = current value R$ 75,000 (30 × R$ 2,500 Dez/2023 → Mai/2026 per Aportes sheet). Resolves the prior "~3% loss or timing mismatch" math-check open question on [[Fluencypass]].
  - **CC provision R$ 18,910.73** (was R$ 5,017.60) — significantly larger sinking fund vs Rico; 40% provisionado.
  - **Rico balance R$ 47,666.72** (was R$ 42,800); cronograma refreshed against new balance (Mai R$ 18,031.45, Jun R$ 7,720, rest unchanged); total R$ 47,763.35.
  - **New asset row**: investment account cash R$ 847.11.
  - **Burn replanned R$ 17,970.70/mo** (was R$ 17,320.70; +R$ 650). Changes: Suplementos R$ 600 → R$ 1,000 (disc.); new Remédios R$ 250 (essential). New split: essential R$ 8,704 / discretionary R$ 9,266.70.
  - **Reserve targets bumped**: 3m R$ 26,112 / R$ 53,912; 6m R$ 52,224 / R$ 107,824; 12m R$ 104,448 / R$ 215,648.
  - **Planned Jul/2026 salary jump**: PJ Invoice 31,500 → 40,000, buy-in 2,500 → 0, net R$ 26,500 → R$ 36,500 (⚠️ R$ 800/mo reconciliation gap pending vs documented Gross R$ 39,200).
  - **2026 reserve-build plan**: R$ 107,500 earmarked (per `Investimentos Planejados` sheet) — Jul–Dez at R$ 14,800–18,500/mo. Conditional on income jump landing.
  - **Effective NW ex-apt/FP**: R$ ~102k → **R$ ~111.3k**.
- consistency-pass corrections applied to the raw file:
  - "0.48% of net worth" → "0.48% of stock portfolio (0.13% of net worth)" — the percentage refers to portfolio yield, not NW.
  - Concentration: "72% in two financial-sector names" listing 3 tickers → "~83% in three financial-sector names" (BBAS3 + CXSE3 + BBSE3).
  - Cumulative buy-in "R$ 75.5k" → "R$ 75,000" (matches Aportes sheet exactly).
  - Reserve targets column "Discretionary" had values matching full-burn math → renamed to "Full burn".
  - Risk row "R$ 7600" → "R$ 7,834"; "R$ 42k... partially provisioned" → "R$ 47,7k gross; R$ 18,9k provisionado (40%)"; "Thin monthly surplus" scoped to Mai–Jun/2026 only.
  - Long-term FI: "essential monthly burn" → "full monthly burn" (aligned with `feedback-passive-income-full-burn` memory).
  - Inline ⚠️ added at the unreconciled R$ 800/mo gap for Jul/2026+.
- analytical implications:
  - Surplus capacity nearly doubles from Jul/2026 (planned): R$ 8.5k/mo → R$ 18.5k/mo ex-Rico. The 6-month reserve target becomes reachable Q1/2027 (vs Ago/2027 in the [[International Relocation]] locked plan, which still holds as conservative fallback).
  - With buy-in stopping Jul/2026, the [[Investment Thesis|growth bucket]] adds zero new monthly capital — "continue buy-in until exit" decision is effectively executed by contract restructuring rather than by Yago's unilateral choice.
  - Mai/2026 cash deficit widens to R$ 9.5k after Rico Mai revision; covered by the larger CC provision (R$ 18.9k) without portfolio liquidation.
- new risk added: **Income-jump dependency (Jul/2026)** at Medium — the 2026 reserve-build plan is conditional on the R$ 36.5k net materializing.

## [2026-05-04] ingest | raw/journal/Plans/Relocation.md (NEW — comprehensive 30-month relocation plan)
- pages created (sources): [[Source: Relocation Plan]]
- pages updated (wiki): [[International Relocation]] (full integration: 6 phases, decision gates, decisions locked, top-3 actions, salary calibration to $130-150k initial, gaps revised), [[Joint Plans]] (Stephanie path lock-in date Mar/2027 + apartment strategy locked rent year 1), [[Financial Goals]] (FX hedge milestones table, landing capital target, reserve trajectory aligned to phases), [[Lorena Education]] (Praktika decision gate Set/2026 + English ramp plan + ESL adaptation expectations), [[Stephanie Career]] (NCLEX-RN bridge / retreinamento / non-clinical options + CGFNS requirement noted), [[Index]] (new source pointer)
- key resolutions (decisions locked 2026-05-04):
  - **Target landing: Outubro/2028.** Anchored to 4 converging constraints — fim Rico Mar/2027, reserva 6m Ago/2027, IELTS B2 Mar/2027, Lorena 13.5 anos no pouso (final janela 11-13)
  - **US primário, Canadá fallback paralelo** (Express Entry filed Q3/2026 como hedge ~R$ 6k)
  - **Apartamento alugado durante ano 1** abroad; decisão de venda Set/2029 (não vender pré-mudança)
  - **Buy-in FP mantido até saída da empresa** (~Mai/2028) — sinalização partnership, não decisão financeira pura
  - **Inglês**: Fluencypass curriculum + Praktika para adultos (R$ 600/ano cada); Lorena tem decisão gate Set/2026 entre minimal vs. imersão presencial
  - **IELTS Academic**, não TOEFL — cobre Canadá EE (obrigatório) + dossiê US num único teste
  - **Sem pós-graduação só para credentialing** (ROI ruim vs. inglês/network/dossiê); exceção opcional Georgia Tech OMSCS se houver disciplina genuína
  - **Cidade alvo: médio-tier** (Austin/Tampa/Charlotte/Raleigh/Denver/Phoenix/Dallas); HCOL descartado a $130k inicial
  - **Família viaja junta** — sem split-departure
- new gating items descobertos durante a sessão de planejamento:
  - **Diploma não retirado há 10+ anos** — gating do I-140 filing; lead time 3-6 meses (universidade → apostila → tradução → WES). Adicionado como Top-3 ação Phase 0
  - **Vacinação família incompleta** — Hep B série leva 6 meses (0-1-6), gating do panel physician medical exam pré-visa stamping. Adicionado como Top-3 ação Phase 0
- Top 3 ações esta semana (semana 1 de Mai/2026):
  1. Marcar consulta com advogado de imigração US (USD 300-600) — gating do plano inteiro
  2. Solicitar emissão do diploma na universidade — gating do dossiê
  3. Levantar carteirinhas de vacinação + consulta médica — Hep B lead time crítico
- analytical conversations leading to the plan (filed only as conversation, not as separate wiki pages):
  - "Análise sincera da carteira" → identificou 3 problemas estruturais (concentração financeira, growth bucket FP super-dimensionado vs 13% YoY, ausência de RF) e R$ 7.6k reserva como risco maior que qualquer item de portfolio
  - "Faz sentido financeiramente mudar vs FP exit?" → resposta: salário US composto 5 anos > qualquer cenário plausível de exit FP para stake atual; B2B em ritmo reforça FP mas não inverte ranking
  - "$130k é viável e como fica QoL?" → break-even ano 1 em cidade médio-tier, positivo ano 2-3; HCOL inviável a $130k
  - "B1 → C1 timeline + TOEFL vs IELTS" → C1 24-30 meses realista; chega nos EUA B2-forte/C1-emergente; IELTS é dominant choice por cobrir Canadá EE também
  - "Pós-graduação atrapalha?" → não materialmente; bacharel + 15 anos cobre EB2 trivialmente; pós ranqueia 4º-5º em ROI vs. alternativas
- new feedback memory considered: passive-income floor já capturado em sessão anterior (full burn vs essential-only)
- pattern noted: a sessão de hoje converteu múltiplas conversas analíticas em um único living planning doc no raw/, espelhando a convenção do Finances.md. Este pattern (consolidação de análise em planning doc raw → single source page no wiki) deve ser repetido para futuros planos multi-fase.

## [2026-05-17] re-ingest | raw/journal/Health/ (directory restructure + Retatrutide + diet + 8-week training)
- pages updated: [[Source: Health]] (source_path → directory; ingested 2026-05-17; full body rewritten), [[wiki/self/health]] (added pharmacological stack table, diet table, training-cycle table; lint trimmed to measurement/labs gap), [[Index]] (Health one-liner + Source: Health one-liner refreshed)
- factual deltas vs prior snapshot:
  - **Retatrutide 2 mg/week** added to `Basic Infos.md` under a new "Other Substances Used" section — first GLP-1/GIP/glucagon triple agonist on record in the wiki.
  - **Planned diet May–Jun 2026** populated: ~3,500 kcal, 476 g C / 62 g F / 198 g P (~2.83 g/kg), creatine 5 g, multivitamin, omega-3, 3–4 L water.
  - **Workout plan** renamed `May - Jun 2026.md` → `15 May - 15 Jun 2026.md` and now contains a full 8-week / 5-day program (Seg–Sex), with Week 1 starting loads logged for chest/back/arms days; legs (Qua) and Fri shoulders empty pending execution.
  - **Body-measures folder** created but empty.
- analytical notes:
  - Cardiovascular co-medication (pitavastatina + nebivolol + natokinase) lines up with mitigating known TRT side effects (lipids/hematocrit/BP); supports the "medical supervision" framing as operationalised.
  - Calorie target ~3,500 kcal at 70 kg is well above maintenance — paired with Retatrutide, the intent (clean lean-gain vs. recomposition) is not stated in source; flagged as open question, not assumed.
  - Filename "15 May - 15 Jun 2026" describes an 8-week block; if the program truly runs 8 weeks, end date is ~10 Jul 2026 (1-month filename / cycle-length mismatch flagged on [[wiki/self/health]]).
- lint state: prior "data-thin" lint is largely resolved on protocol/diet/training; remaining gaps recorded on both [[Source: Health]] and [[wiki/self/health]] are (a) no body-measures cadence yet, (b) no lab markers documented, (c) Qua + Sex load tables empty, (d) Retatrutide context (indication, prescriber, duration, exit) not yet captured.

## [2026-05-22] ingest | raw/assets/yandeh-proposta-pj-2026-05-22.pdf + raw/journal/Plans/Job-Change-2026-06.md (NEW — job change FP → Yandeh)
- pages created (sources): [[Source: Yandeh PJ Proposal]], [[Source: Job Change 2026-06]]
- pages created (wiki): [[Yandeh]]
- pages updated (wiki): [[Fluencypass]] (closed Jun/2026; open follow-ups pared to stake-relevant items; R$ 800 reconciliation gap moot), [[Career History]] (Yandeh at top, FP closed 2y 7m, search closed, Q2 resolved by market decision), [[Finances]] (salary structure restated Yandeh PJ R$ 42k → ~R$ 35–36k net est.; surplus profile recomputed; risk table rebalanced — income-jump dependency resolved, first-invoice validation now Low), [[Investment Thesis]] (growth bucket frozen at R$ 75k parked; insider visibility decays from Jun/2026; third-bucket question more urgent), [[International Relocation]] (2026-05-22 update banner; decisão locked #3 superseded inline; Q2 resolved; Yandeh as bridge vs terminal flagged for 90-day signal; gates downstream unaffected), [[Financial Goals]] (active search closed at Yandeh; buy-in decision closed; reserve targets still on track but ~R$ 1k/mo lower surplus vs prior FP-jump assumption), [[Profile]] (current role = Yandeh incoming), [[Index]] (Yandeh + 2 new sources; one-liners refreshed across Self/Career/Projects/Sources)
- key facts captured (raw):
  - Last day Fluencypass: 2026-06-12
  - Start Yandeh: 2026-06-15 (proposal letter said 01/06; renegotiated after issuance)
  - Yandeh role: Staff Product Engineer (per Yago's edit in raw/journal/Career.md 2026-05-22)
  - Yandeh comp: PJ R$ 42.000 base + bonus up to 6× salaries conditional on metrics + permanence at payment
  - Yandeh address: Av. Santo Amaro, 48 — Itaim, SP; presencial; currently hybrid 4d/week as agreed
  - Yandeh benefits: Flash R$ 1.100, Wellhub (8 plans), SulAmérica Saúde Executivo R1 Apto (titular + deps, no monthly fee, coparticipation only), Allya, Day Off in birthday month, parental leave (gestation 180d / paternity 30d / adoption 180-120-30d by age), mobility R$ 360 (hybrid + RMSP), 24d annual vacation (per Yago, not in letter)
- contradictions surfaced and resolved inline (not overwritten):
  - **"Saída FP ~Mai/2028"** assumption in [[International Relocation]] / [[Source: Relocation Plan]] — invalidated; exit happened 2026-06. Flagged inline on [[International Relocation]] with update banner; [[Source: Relocation Plan]] left untouched (source-of-record convention).
  - **"From Jul/2026 buy-in stops per PJ restructuring"** in [[Finances]] / [[Investment Thesis]] — superseded; buy-in actually ended Mai/2026 (last aporte before exit). Decision locked 2026-05-04 ("manter buy-in até saída") is honored, just via job change, not via the planned PJ restructuring.
  - **"R$ 800/mo Jul/2026 reconciliation gap"** flagged in [[Finances]] and [[Fluencypass]] — moot (the planned PJ R$ 40k structure never executed).
  - **Q2 open question** ("Is FP equity better than working abroad?") in [[Source: Career]] / [[Career History]] / [[International Relocation]] — effectively resolved by market decision when Yago accepted Yandeh cash PJ without equity ~2 years ahead of plan.
- analytical implications:
  - Surplus capacity Jul/2026+ is **~R$ 1k/month lower** than the prior FP-jump assumption (Yandeh net ~R$ 35–36k vs planned FP ~R$ 36.5k), but reserve trajectory still lands within the 2026 plan because (a) buy-in stopped Jun/2026 cleanly, (b) benefits offset ~R$ 1.5–2.5k of burn once settled, (c) bonus is pure upside.
  - Yandeh base R$ 42k landed R$ 3k below the search-time R$ 45k floor; Yago made the trade against bonus + benefits + role context. Narrative to be unpacked once Yago fills the "why am I leaving" placeholder in [[Source: Job Change 2026-06]].
  - [[Investment Thesis]] growth bucket frozen creates an explicit "third bucket" gap that [[International Relocation]]'s FX hedge ramp may force resolving (insider-knowledge growth bet is gone; USD index-tracking remains thesis-orphaned).
  - Yandeh is the **single income source** going forward — same concentration risk shape as FP was, at higher base + bonus optionality.
- placeholders left open (Yago to fill):
  - "Why I'm leaving Fluencypass" + "What Fluencypass taught me" (in [[Source: Job Change 2026-06]]) — handoff window May–Jun 2026
  - Yandeh scope, team, tech stack, charter, first-90-day deliverables (~Q3/2026 when onboarded)
  - Yandeh bonus mechanics — metric definitions, cadence, payment schedule
  - Yandeh first-invoice net validation against R$ 35–36k estimate
  - "Yandeh as bridge or terminal?" decision — default bridge; 90-day signal pulls forward in [[International Relocation]]
- pattern noted: this was a "live decision invalidates locked plan" ingest — handled by flag-in-place inline updates with explicit "Update 2026-05-22" banners rather than rewriting the locked plan. Preserves history; respects the decision-locked convention; lets Yago see when a downstream gate needs re-pricing without losing the prior reasoning.

## [2026-05-29] ingest | Finances raw restructured to sheet-pointer + live MCP refresh
- pages updated: Finances, Financial Goals, Investment Thesis, Source: Finances, index.md
- pages created: none
- source: raw/journal/Finances.md restructured by Yago into a thin pointer (3 Google Sheets links + reserve/CC-provision goal tabs + Family intersections + push-backs); numeric balance sheet now lives in the sheets, not the note. Google Sheets API enabled this session → read all three sheets live via Drive MCP (`2026 - Planejamento de Gastos`, `Patrimônio Líquido`, `Carteira de ações`).
- live snapshot deltas vs 2026-05-22:
  - net worth R$ 491,227.23 → **R$ 487,843.29** (market drift); gross R$ 734,436.21; liabilities R$ 246,592.92
  - **Rico R$ 47,666.72 → R$ 33,592.92** (Mai/2026 fatura R$ 18,031.45 settled)
  - **CC provision R$ 18,910.73 → R$ 33,189.56** (~92% of gross card debt) → **net card liability R$ 3,045.04** (was ~R$ 28.8k)
  - **portfolio per-ticker now live** (was "aggregate only, broker refresh needed"): BBAS3 37.0% / CXSE3 34.4% / ISAE4 16.4% / BBSE3 12.2%; total ~R$ 130.6k; **BB-group (BBAS3+BBSE3) ≈ 49%**; proventos R$ 24,705.81 (DYOC 28.99%)
  - passive income R$ 629.54/mo (0.48%); projected R$ 769.74 (0.59%); reserve unchanged R$ 7,833.94
- risk reassessment (2026-05-29): CC revolving **near-neutralized** (Low); portfolio concentration **Medium → High** (BB-group exposure made explicit); added **"total dependence on active income"** (passive ≈ 3.5% of burn); Mai/2026 cash-deficit risk closed (played out as planned)
- goals restructure: reserve ladder now 1→6→12 months (R$ 17,970.70 / 107,824 / 215,648); explicit "complete the credit-card provision" goal added (~92% done)
- notes: intraday B3 drift observed between two reads in-session (portfolio R$ 129,810 vs R$ 130,615) — flagged inline. Rico forward cronograma now ~R$ 3.9k below current balance → flagged as needing refresh against the new balance. Two-tab gids in raw (606320972 / 1857567584) both resolve to the `Resumo` summary tab, not separate detail tabs.

## [2026-05-29] ingest | Wiki convention: reference sheets, no literal financial values + 2 skills
- pages updated: Finances, Financial Goals, Investment Thesis (rewritten reference-based), Source: Finances, index.md, CLAUDE.md
- skills created: .claude/skills/finance-wiki-references (write side), .claude/skills/consult-linked-sources (read side)
- trigger: Yago — "na Wiki não quero valores literais no financeiro, e sim referencias as planilhas" + create two skills (always use the sheets instead of fixing values; always consult linked Drive files referenced in raw)
- convention: living wiki pages carry no transcribed currency state — qualitative claim + link to the sheet; numbers read live via Drive MCP. Goal thresholds / contract terms / tax rules may stay literal. Source-page logs exempt (append-only history). Encoded as CLAUDE.md page-convention #8 + new "Linked external files" section.
- notes: stripped net worth / balances / portfolio R$ & weights / burn amount / reserve target amounts / passive income / Rico balances from the three living pages; reserve targets re-expressed as multiples of full burn. FP valuation analysis kept (growth-thesis input from a source, not finance-sheet state) but flagged as such. index.md one-liners de-literalized.

## [2026-05-29] ingest | Health journal refactored to thin-pointer sheets
- pages updated: Source: Health, wiki/self/health, index.md
- trigger: Yago — "Atualize a wiki com as mudanças feitas no RAW"
- raw changes: workout `15 May - 15 Jun 2026.md` renamed → `May - Jun 2026.md` and inline 8-week tables replaced with a link to the "Treino yago 21" sheet; empty `body measures history/` folder replaced by `Body measures history.md` (links a sheet); `Basic Infos.md` gained an "Important References" section.
- read live (Drive MCP): workout sheet shows Weeks 1–3 logged with real load progression (Semana 3 dated 25/05). "Body measures" sheet's only tab is a daily habit-adherence tracker (Workout/Cardio/English/AI, 0–10), not measurements.
- notes: de-transcribed literal training loads from the living page (now reference the sheet, per the finance refactor pattern). New "Habit adherence" section added — workout high (8–10) but cardio + English Lesson at 0 every day, AI Lesson decaying. Flagged sheet name/content mismatch (named "Body measures" but holds habits → still no body-composition data). Filename mismatch lint (15 May–15 Jun vs 8-week cycle) resolved by the rename.
