---
name: finance-wiki-references
description: Use whenever creating or updating ANY financial content in the Personal Advisor wiki (net worth, balances, portfolio, burn, income, reserves, provisions, Rico/debt, passive income, etc.). Enforces the rule that living wiki pages must NOT hardcode literal currency values — they reference the canonical Google Sheets and read them live via the Drive MCP. Triggers on edits to wiki/self/finances.md, financial-goals.md, investment-thesis.md, or any page stating a financial figure.
---

# Financial wiki = references, not literal values

**Core rule (set by Yago, 2026-05-29):** living wiki pages must **not** contain transcribed currency figures. Numbers live in the spreadsheets (single source of truth); the wiki holds the *analysis, structure, risk framing, and cross-links*, and **points to the sheet** for any actual value.

Why: balance-sheet numbers go stale the moment they're copied. Analysis doesn't. Copying a snapshot into the wiki creates contradictions across pages and forces re-transcription on every refresh. Referencing the sheet keeps the wiki durable and the numbers always-live.

## Canonical sheets

| Sheet | File ID | Holds |
| --- | --- | --- |
| `2026 - Planejamento de Gastos` | `15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w` | monthly cash flow (one tab/month; e.g. `Jan` = gid 1968085387), burn, income, itemized outflows, reserve-build plan (`Investimentos Planejados`) |
| `Patrimônio Líquido` | `13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg` | net worth, assets, liabilities, CC sinking-fund provision, estimated/projected passive income. Summary = `Resumo` tab (gids 606320972 & 1857567584 both resolve here) |
| `Carteira de ações` | `1v6eTPtx7KzHi77kn6KMjG9nQtfHwXY2nbbhMBzrzgSY` | per-ticker positions, weights, sectors, dividends (proventos), ROE/DYOC |

These are the live targets the raw (`raw/journal/Finances.md`) points to. See the companion skill `consult-linked-sources` for the read mechanics.

## What to strip vs. keep in wiki pages

**Strip (reference the sheet instead):** current/actual state that a sheet tracks and that drifts —
net worth, gross assets, total liabilities, per-asset/per-liability balances, portfolio total & per-ticker R$ values & weights, Rico/credit-card balances and schedules, CC provision amount, monthly/projected passive income, monthly burn amount, derived reserve-target amounts.

**Keep (these are not live sheet state):**
- Qualitative analysis & risk framing ("reserve covers well under a month of burn — see the sheet"; "concentration is intentional under Barsi/AGF"; "the Banco do Brasil group is roughly half the book").
- Risk severities and the reasoning behind them.
- Methodology, cross-links (`[[wikilinks]]`), structure (ticker symbols + sectors, "single income source", "100% BRL").
- Goal *thresholds* that define the goal (e.g. "reserve = 1 / 6 / 12 × full monthly burn", "diversify single-country below 70%", aspirational "R$ 45k/mo passive").
- Contractual terms and tax rules from non-sheet sources (Yandeh PJ structure, "up to 6× salaries", "R$ 20k/mo sale tax-exempt, 15% above").

When you'd reach for a R$ figure of current state, write the qualitative claim + a link to the sheet/tab instead:
> "Emergency reserve is still a critical gap — under half a month of burn (see [Patrimônio Líquido](https://docs.google.com/spreadsheets/d/13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg/) → `Resumo`)."

## Answering financial questions in chat

Different surface, different rule. When Yago *asks* a number, read the sheet live and give the exact figure in chat (that's the point of having MCP access). The no-literals rule governs what gets **filed into the wiki**, not what you say in conversation. If you file the answer back, file the reference + analysis, not the snapshot.

## Source pages are the exception

`wiki/sources/*` modification logs are append-only historical ledgers — point-in-time figures are allowed there as dated history (they record "what changed when"). Even so, prefer recording *deltas and references* over re-pasting the full balance sheet.

## Reading mechanics (quick)

- `gsheets_read` with targeted A1 `ranges` (e.g. `["Resumo!A1:G19"]`) — a full-sheet read overflows context; always range-scope it.
- `gdrive_read_file` returns a compact CSV of the first/default tab — good for a quick whole-tab glance.
- Requires the Google Sheets API enabled on the connected GCP project.
