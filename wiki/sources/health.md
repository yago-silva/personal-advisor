---
title: "Source: Health"
type: source
source_type: journal
source_path: raw/journal/Health/
source_date: 2026-05-15
ingested: 2026-05-17
author: Yago Silva
tags: [health, body-metrics, protocol, training, nutrition]
---

# Source: Health

Restructured from a single `Health.md` into a directory (`raw/journal/Health/`) on commit 2743ce9 (2026-05-15). On 2026-05-29 the directory was refactored to the **thin-pointer pattern** (same move as `Finances.md`): the inline workout tables and the empty body-measures folder were replaced by raw notes that link Google Sheets, which are now the source of truth (read live via the Drive MCP — see [[consult-linked-sources]]). Current contents:

- `Basic Infos.md` — height/weight, controlled medications, hormones, other substances; gained an "Important References" section linking the two sheets below.
- `planned diets history/May - Jun 2026.md` — current diet target (kcal + macros + supps + water). Unchanged.
- `workout history/May - Jun 2026.md` — **renamed** from `15 May - 15 Jun 2026.md` and gutted of its inline tables; now a thin pointer to the "Treino yago 21" Google Sheet (`1q7dF-CTRqfGMQ71Wft20UyIbxq0mmfllyzVzKgNbWGo`). The sheet has per-day tabs with the 8-week table; as of 2026-05-29, **Weeks 1–3 are logged with real progression** (Semana 3 dated 25/05/2026).
- `Body measures history.md` — **new**, replaces the empty `body measures history/` folder. Thin pointer to a Google Sheet (`1UN2SAj1kk9DJUJp6f-BMcDKiGx95vCri7n7KgGwrB-c`). Despite the filename, its only tab ("Daily") is currently a **habit-adherence tracker** (Workout / Cardio / English Lesson / AI Lesson scored 0–10 per day), not body measurements.

Under explicit medical supervision; Yago opens `Basic Infos.md` with a premise asking not to judge the decision to use hormones.

## Key takeaways

- **Body baseline**: 1.61 m, ~70 kg (unchanged since 2026-05-02 snapshot).
- **Anabolic protocol**: Testosterone enanthate 250 mg/week + Anastrozole 1.5 mg/week.
- **Metabolic/weight protocol (NEW 2026-05-17)**: Retatrutide 2 mg/week — GLP-1 / GIP / glucagon triple agonist, still in late-stage trials at the time of journal. Treated as "Other Substances Used," separate from the hormone block.
- **Cardiovascular co-medication**: Pitavastatina 4 mg/day (statin), Nebivolol 5 mg/day (beta-blocker, β1-selective), Natokinase 200 mg/day (fibrinolytic). Consistent with mitigating known TRT side-effects (hematocrit, lipid shift, BP), suggesting the medical supervision claim is operationalised, not nominal.
- **Diet target (May–Jun 2026)**: ~3,500 kcal/day with macro split 476 g C / 62 g F / 198 g P. Protein at ~2.83 g/kg bodyweight — clear hypertrophy/recomp bias. Whey, creatine 5 g, multivitamin, omega-3 daily. 3–4 L water/day.
- **Training plan (May–Jun 2026, 8 weeks)**: 5-day push/pull/legs-style split — Seg Peito+Ombro ant., Ter Costas+Ombro post., Qua Pernas, Qui Peito+Tríceps+Bíceps (Week 1 marked "casa"/home), Sex Peito+Ombro lat./post. Each exercise prescribes warm-up + 2–4 work sets with rep-range targets and CLUSTER SET as a finisher technique. The full per-set table now lives in the "Treino yago 21" sheet; **Weeks 1–3 logged** as of 2026-05-29, with loads progressing week over week (e.g. the Monday block shows weights climbing across the three logged weeks). Read the sheet live rather than transcribing loads.
- **Habit-adherence tracking (NEW 2026-05-29)**: the "Body measures history" sheet's "Daily" tab scores four behaviors 0–10 per day from 25/05. Early signal: Workout high (8–10), but **Cardio = 0 and English Lesson = 0 every logged day**, and AI Lesson trending down (8 → 0). Discipline is concentrated on training; cardio and study are not happening.

## Notable direct quotes

> "Premise: I've decided to use hormones to build muscle. I know it can affect my health, but I'm under medical supervision. Please don't judge my decision." — `Basic Infos.md`

> "CLUSTER SET = série em cluster (pausas curtas dentro da mesma série)" — workout legend (now in the "Treino yago 21" sheet)

## Wiki updates

- Refreshed (2026-05-29): [[wiki/sources/health]] (this page) — recorded the thin-pointer refactor of the Health directory; file list, takeaways, and lint updated.
- Updated (2026-05-29): [[wiki/self/health]] — training section de-transcribed to reference the live sheet (Weeks 1–3 now logged); body-metrics note corrected (sheet exists but is a habit tracker, not measures); new habit-adherence section added.
- Earlier (2026-05-17): expanded [[wiki/self/health]] from body-baseline-only stub to protocol/diet/training sections.
- Linked from: [[Profile]] (unchanged), [[Finances]] (wellness spend lines unchanged but now have a referent).

## Open questions / lint

- **Sheet named "Body measures history" tracks habits, not measures.** The only tab is a daily 0–10 adherence log — useful, but the wiki still has **no weight trend or circumferences**. With protein at ~2.83 g/kg, a ~R$ 1.7k/mo wellness spend, and a metabolic agent (Retatrutide) in the stack, body-composition data is still the missing input to evaluate whether the regime works. Either rename the sheet or add a measures tab.
- **Cardio and English at 0.** The habit tracker shows both flatlined since 25/05. If they're intended habits, this is a live adherence gap; if not, the columns are noise.
- **No lab markers.** Pitavastatina + Nebivolol + Natokinase + TRT + Retatrutide is a non-trivial pharmacological stack; lipid panel, hematocrit, BP, HbA1c, estradiol would be the minimum cadence to support the "under medical supervision" claim with evidence.
- **Wednesday / Friday loads still blank in the sheet.** Pernas and Sex remain templates — backfill during execution.
- **Retatrutide context not documented.** Indication (weight loss vs. metabolic), prescribing physician, expected duration, and exit plan would be worth a one-paragraph note. Flagged, not invented.
