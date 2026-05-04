---
title: Fluencypass
type: career
tags: [employer, equity, income, role, partnership, ai-llm, edtech]
created: 2026-05-02
updated: 2026-05-04
sources:
  - "[[Source: Finances]]"
  - "[[Source: Career]]"
  - "[[Source: Investment Thesis]]"
---

# Fluencypass

Yago's current employer. EdTech: English courses + live conversation + study abroad + AI learning tools.

## Operating metrics (Q1 2026)

First documented in [[Source: Investment Thesis]] (2026-05-04). Growth data added later same day from CEO pitch.

| Metric | Value | Source |
| --- | --- | --- |
| Headcount | ~120 employees | Yago |
| MRR | ~R$ 1.25M (≈ R$ 15M ARR) | Yago |
| **MRR growth YoY (Mar 2025 → Mar 2026)** | **13%** | CEO pitch (general meet) |
| **Sales per seller (YoY)** | **+26%** | CEO pitch (general meet) |
| Revenue mix | 82% B2C / 10% study abroad / 8% B2B | Yago |
| LTV (B2C) | 8-12 months | Yago |
| Churn B2C | 9-11% / month | Yago |
| Active B2B subscriptions | ~10,000 | Yago |
| B2B contracts | ~55 | Yago |
| B2B launch | Nov/2025 | Yago |
| 2026 B2B target | 30% of revenue (from 8% today) | Yago / company plan |

### Advisor observations on these metrics

- **B2C churn 9-11%/month is high**. Compounded annually, retention drops to ~28%; LTV of 8-12 months is consistent. This is the structural pressure behind the B2B pivot.
- **B2B at 8% of revenue today, target 30% in 2026**: the rest of the business must hold flat while B2B revenue ~4x in 12 months. Aggressive but plausible given Nov/2025 launch + Yago's auth/multi-tenant work in [[Source: Career]].
- **Revenue per employee ≈ R$ 125k/year** — low for SaaS (US benchmark $200k+); signals high-touch services component, not a pure software P&L.
- **Per Yago in [[Source: Investment Thesis]]: "the company does not have a clear vision about other markers, for example: churn rate"** — instrumentation gap that would surface in any future M&A diligence.
- **13% YoY MRR growth is the most important new data point for the equity decision.** SaaS exits at 5-10x typically require 40-80% YoY growth. At 13%, FP compounds to:
  - 3 years: R$ 15M → ~R$ 21.6M ARR (1.44x)
  - 5 years: R$ 15M → ~R$ 27.6M ARR (1.84x)
  
  This means a **5x or 10x outcome on Yago's stake would have to come almost entirely from multiple expansion** (e.g., AI premium, strategic premium) rather than from underlying business growth. That's a much narrower, riskier path than "the company grows into the valuation." See [[Investment Thesis]] for full reasoning.
- **+26% sales per seller** is a real efficiency win. It tells you the engine works — it just hasn't scaled. The B2B 4x plan, if it lands, could push blended growth toward 30-40% YoY. Watch the next 2-3 quarters for evidence.

## Yago's role

- **Title**: Staff Software Engineer + Partner
- **Tenure**: Nov 2023 – present (2y 7m as of May 2026 — current longest tenure of the past decade)
- **Scope**: owns software architecture and platform evolution — e-commerce, auth, payments, video streaming, LMS, AI features. Technical reference for system design, scalability, HA decisions.

## Compensation structure (clarified 2026-05-03)

| Component | R$/mo | Notes |
| --- | --- | --- |
| PJ invoice gross | 31,500 | full PJ contract value |
| Equity buy-in (auto) | −2,500 | voluntary opt-in; partnership program |
| Effective gross | 29,000 | what reaches Yago's hands |
| Net (after PJ taxes) | **26,500** | this is the inflow used in [[Finances]] |

### Equity position

- **Cumulative bought**: R$ 72,500 (since Nov 2023, ~30 months × R$ 2,500)
- **Vesting**: none — Yago owns each month's purchase day-one
- **Cliff**: none — leaving Fluencypass does not forfeit the equity
- **Liquidity**: illiquid until a Fluencypass liquidity event (sale, IPO, etc.)
- **Per Yago's standing rule** ([[Finances]]): treat as zero for decision-grade net worth

### Math check

30 months × R$ 2,500 = R$ 75,000 bought; current value R$ 72,500. Two possibilities (worth confirming):

- Yago started ~29 months ago (1 month after Nov 2023 start) → R$ 72,500 ≈ 29 × R$ 2,500
- ~3% unrealized loss on the position

If it's the second case, that's data for Yago's open Q2 in [[Source: Career]] ("is Fluencypass equity better than working abroad?").

## PJ structure

Yago invoices via "Yago Silva Sistemas" — PJ entity. Generates ISS + INSS obligations (~R$ 1,780–1,930/month combined per [[Finances]]).

## Key shipped work (per [[Source: Career]])

- **B2B product unlock**: re-architected auth (Keycloak/OAuth2, zero-downtime migration) + multi-tenant billing with dependent accounts and license-based pricing. B2B reached 5% of total revenue within 4 months.
- **Custom video streaming platform** (FFmpeg-based): replaced third-party with zero downtime; enabled proprietary LMS scaling without linear infra cost.
- **AI course generation pipeline**: orchestrates LLMs + audio/video synthesis + RAG to produce complete courses (video lessons, quizzes, flashcards, writing exercises) language-agnostic. Made multi-language courses viable.
- **AI English Tutor** (own initiative): designed and shipped end-to-end. LLMs + RAG + MCP. Expanded Fluencypass into a new market segment.

## Strategic role in Yago's plan

- **Single income source** — central risk on [[Finances]].
- **All-BRL income** — no FX hedge while [[International Relocation]] is the active thesis.
- **Equity treatment**: per Yago's standing instructions on [[Finances]], do not count Fluencypass equity as decision-grade net worth.
- **Partnership lock-in tension**: Yago accepted Staff IC step-back specifically to access the partnership/equity. He explicitly asks (in [[Source: Career]]): *is this equity better than working abroad?* — open decision.
- **Sole "growth" position in portfolio**: per [[Investment Thesis]], FP equity is the entire growth bucket. Pausing the R$ 2,500/mo buy-in pauses the growth thesis as a whole.

## Valuation framing (advisor note, 2026-05-04 — updated with growth data)

ARR ~R$ 15M (MRR R$ 1.25M × 12), growing **13% YoY**. Realistic BR EdTech sale multiples land at 2-3x revenue (typical) up to 5-10x (rare premium / strategic / AI hype).

### Decomposing the path to 5-10x on Yago's stake

For Yago's R$ 75k to become R$ 750k (10x), FP's **valuation** must grow 10x between buy-in and exit. That valuation can grow via two levers:

1. **Revenue growth** (organic, fundamentals)
2. **Multiple expansion** (the market values each R$ of revenue more highly at exit)

Projected revenue at 13% YoY:

| Horizon | Revenue (multiple of today) |
| --- | --- |
| 3 years | 1.44x |
| 5 years | 1.84x |
| 7 years | 2.35x |

**To hit 10x on the stake from a 5-year exit, multiple expansion would need to do the remaining work** — i.e. the market would need to value FP at ~5.4x today's multiple (10x ÷ 1.84x growth). Possible only via AI premium / strategic acquirer / category-leader narrative.

To hit 5x on the stake at 5y: multiple needs to expand ~2.7x. More plausible but still requires a premium re-rating — base BR EdTech multiples don't move that much without a story.

**If B2B target lands** (30% of revenue, requires B2B 4x in 2026): blended growth could lift toward 30-40% YoY. At 35% YoY, 5-year revenue grows 4.5x — that path **does** support 5x on the stake even at flat multiple, and 10x with modest expansion. But that's the plan, not the track record.

### Critical missing data point

FP's current internal valuation used to set the buy-in price is still not documented. Without it, % ownership and absolute exit math cannot be sized concretely. Open follow-up below.

## Notable financial reconciliation (resolved 2026-05-03)

The R$ 2,500/mo equity buy-in was a meaningful line not initially broken out in [[Finances]]. **Resolved**: the buy-in is taken at source before cash reaches Yago, so it is **not** in the burn — the cash-flow profile in [[Finances]] (now at the replanned R$ 17,320.70/mo burn) is correct as written. Buy-in is forced savings into illiquid equity, not a recurring outflow.

## Open follow-ups

- [ ] Document equity terms (vesting, cliff, liquidity events) — flagged in [[Financial Goals]]
- [ ] **Get current internal valuation used for buy-in pricing** — required to size % ownership and exit math (added 2026-05-04)
- [x] ~~Get growth rate trajectory~~ — partially answered 2026-05-04: **13% YoY MRR (Mar 2025 → Mar 2026)**. Still open: B2B trajectory toward 30% target — track quarterly through 2026.
- [ ] **Get B2C churn trend** (improving / stable / worsening) — Yago's source notes FP itself lacks visibility here; still the most material missing input.
- [ ] **Watch B2B revenue trajectory through 2026** — if B2B share doesn't visibly accelerate by Q3 2026, the "blended 30-40% growth" scenario for the stake math weakens significantly.
- [x] ~~Confirm whether R$ 2,500/mo equity buy-in is inside or on-top-of the existing R$ 20k burn~~ — resolved 2026-05-03 (taken at source, not in burn)
- [ ] (Yago to journal) "What has Fluencypass taught me? What frustrates me? Why am I looking now?" — placeholder in [[Source: Career]]

## Resolved (2026-05-03)

- ~~No record of role, tenure, or company~~ — all documented per [[Source: Career]]
