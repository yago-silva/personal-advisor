---
name: health-analyses
description: Use when Yago wants a health/fitness analysis or evaluation that draws on more than one data source — "avalie minha saúde", "como estou", "avalie meus exames/treino", a check-up, a progress review, or any cross-cutting question about his body, training, or trajectory. Orchestrates three live sources — medical exams, the Samsung Health device feed, and the training program — reads them LIVE, and synthesizes an honest, cited assessment. For a single isolated value, use the underlying source skill directly instead.
---

# Holistic health analysis — combine three live sources

When Yago asks for a health/fitness **assessment** (not just one number), pull from all three sources below, read each **live**, and synthesize. Never trust numbers transcribed in the wiki or earlier in the conversation — they go stale.

## The three sources

1. **Medical exams (lab/blood/hormone PDFs)** → use [[consult-medical-exams]].
   Blood work, hormone panels, lipids, hepatic/renal, PSA. In Drive under `histórico de exames/Yago`. Read the PDF live (base64 → decode → Read).

2. **Device feed (Samsung Health via Health Sync)** → use [[consult-health-sync]].
   Weight/body composition, heart rate, steps, sleep, activities/workouts. Five Drive CSV folders, multiple granularities. Only the `Peso` column is reliably populated by the scale; other body-comp columns are often `0.0` (not measured) — don't report zeros as real.

3. **Training program & adherence** → `raw/Health/Workout History/` + its linked Sheet.
   The note (e.g. `raw/Health/Workout History/May - Jun 2026.md`) holds the program structure and reading notes; the **control spreadsheet** (live source of truth, e.g. `https://docs.google.com/spreadsheets/d/1q7dF-CTRqfGMQ71Wft20UyIbxq0mmfllyzVzKgNbWGo`) holds the per-week logged Volume × Carga. Read the Sheet live via the Drive MCP (`gsheets_read`, targeted ranges) for actual loads and which days were logged. Cross-check planned days vs. logged days for adherence.

## Context to anchor against (read first)

- `raw/Health/Basic Infos.md` — current **hormones, controlled meds, substances, height/weight, the stated goal** (e.g. "hipertrofia com menor ganho de gordura"). This frames every number: many "abnormal" labs are *expected* given the stack.
- `raw/Health/Body Measures History.md` — composition baselines/trend.
- `raw/Health/Diet History/` — nutrition context.
- `raw/Health/Diagnostics History/` — prior dated diagnostic notes (Yago's own + earlier analyses).

## Method

1. **Read the anchor notes** (Basic Infos = stack + goal) so you interpret data in context, not in a vacuum.
2. **Pull each relevant source live** — exams, device feed, training Sheet — scoped to what the question needs.
3. **Cross-reference, don't silo.** The value is in the connections: e.g. hematocrit vs. testosterone use; estradiol vs. anastrozole dose; leptin vs. cutting + GLP-1; training adherence vs. the hypertrophy goal; weight trend vs. logged volume.
4. **Be honest and specific.** Flag each value High/Low/Normal vs. its reference range or vs. the stated goal/threshold. State what the data does **not** cover. Brevity over completeness — one true thing plus the source beats ten vague ones.
5. **Cite sources** — file/note path, Sheet, or exam name + coleta date — so every claim is verifiable. Note read time for time-sensitive values.
6. **Persist when asked:** write a dated note in `raw/Health/Diagnostics History/<YYYY-MM-DD>.md`, following that folder's pattern — **don't edit old entries; add a new one.**

## Boundary

Give the raw reading and the concrete points to raise with his doctor. **Dose/treatment/conduct decisions belong to the prescribing physician — don't give definitive medical advice** (CLAUDE.md tone/boundaries). Yago has asked not to be judged on the hormone decision; respect that — be sincere about the data, not about the choice.

## Gotchas

- All three Drive reads share the **same OAuth token**; on `403 "unregistered callers"` re-auth per the procedure in [[consult-health-sync]].
- Exams enumerate poorly by parent folder — search by keyword (see [[consult-medical-exams]]).
- Pick **one granularity** per device-feed metric (daily/weekly/monthly overlap → double-counting).
