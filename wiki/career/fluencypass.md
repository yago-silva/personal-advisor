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

First documented in [[Source: Investment Thesis]] (2026-05-04).

| Metric | Value |
| --- | --- |
| Headcount | ~120 employees |
| MRR | ~R$ 1.25M (≈ R$ 15M ARR) |
| Revenue mix | 82% B2C / 10% study abroad / 8% B2B |
| LTV (B2C) | 8-12 months |
| Churn B2C | 9-11% / month |
| Active B2B subscriptions | ~10,000 |
| B2B contracts | ~55 |
| B2B launch | Nov/2025 |
| 2026 B2B target | 30% of revenue (from 8% today) |

### Advisor observations on these metrics

- **B2C churn 9-11%/month is high**. Compounded annually, retention drops to ~28%; LTV of 8-12 months is consistent. This is the structural pressure behind the B2B pivot.
- **B2B at 8% of revenue today, target 30% in 2026**: the rest of the business must hold flat while B2B revenue ~4x in 12 months. Aggressive but plausible given Nov/2025 launch + Yago's auth/multi-tenant work in [[Source: Career]].
- **Revenue per employee ≈ R$ 125k/year** — low for SaaS (US benchmark $200k+); signals high-touch services component, not a pure software P&L.
- **Per Yago in [[Source: Investment Thesis]]: "the company does not have a clear vision about other markers, for example: churn rate"** — instrumentation gap that would surface in any future M&A diligence.

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

## Valuation framing (advisor note, 2026-05-04)

ARR ~R$ 15M (MRR R$ 1.25M × 12). Realistic BR EdTech sale multiples land at 2-3x revenue (typical) up to 5-10x (rare premium / strategic / AI hype). At today's revenue, that maps to FP valuations between ~R$ 30M (2x) and ~R$ 150M (10x).

**Key correction to prior multiplier reasoning**: the "10x on Yago's investment" framing requires FP's **valuation** to grow 10x between Yago's buy-ins and the exit — not just for the company to be sold at a 10x revenue multiple. The buy-in price is set at FP's current valuation (no insider discount, per the math check above). For R$ 75k to become R$ 750k, the underlying valuation must grow 10x — combination of revenue growth + multiple expansion. Pure "sold at 10x revenue" without underlying revenue growth would mostly deliver multiple-expansion gains, not the headline 10x.

**Critical missing data point**: FP's current internal valuation used to set the buy-in price is not documented. Without it, % ownership and exit math cannot be sized concretely. Open follow-up below.

## Notable financial reconciliation needed

The R$ 2,500/mo equity buy-in is a meaningful line **not separately broken out in [[Finances]]**. Either it sits inside one of the existing budget categories or it's missing entirely. **Worth confirming**: is it inside the ~R$ 20k burn ex-Rico, or on top? If on top, real burn = ~R$ 22.5k and the surplus profile in [[Finances]] shifts ~R$ 2.5k/mo down — which materially affects the reserve-build timeline.

## Open follow-ups

- [ ] Document equity terms (vesting, cliff, liquidity events) — flagged in [[Financial Goals]]
- [ ] **Get current internal valuation used for buy-in pricing** — required to size % ownership and exit math (added 2026-05-04)
- [ ] **Get growth rate trajectory** (MRR YoY, B2B trajectory toward 30% target) — material for any P(exit) calibration
- [ ] **Get B2C churn trend** — Yago's source notes FP itself lacks visibility here
- [x] ~~Confirm whether R$ 2,500/mo equity buy-in is inside or on-top-of the existing R$ 20k burn~~ — resolved 2026-05-03 (taken at source, not in burn)
- [ ] (Yago to journal) "What has Fluencypass taught me? What frustrates me? Why am I looking now?" — placeholder in [[Source: Career]]

## Resolved (2026-05-03)

- ~~No record of role, tenure, or company~~ — all documented per [[Source: Career]]
