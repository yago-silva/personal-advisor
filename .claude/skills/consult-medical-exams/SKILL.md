---
name: consult-medical-exams
description: Use whenever you need Yago's medical lab exams (blood work, hormone panels, lipids, hepatic/renal, PSA, etc.) — values, dates, reference ranges, or trends. The exams are PDF lab reports stored in Google Drive under "histórico de exames/Yago". Always read the PDF LIVE via the Drive MCP instead of trusting values transcribed in the wiki or earlier in the conversation. Triggers on any query, evaluation, or ingest about Yago's blood/lab/hormone exam results.
---

# Medical exams live in Google Drive (PDF lab reports)

Yago's medical lab exams are **PDF reports** (from labs like *Labi Saúde*) stored in Google Drive. They are the **source of truth** for blood work, hormone panels, lipids, hepatic/renal markers, PSA, etc. They are distinct from the manually-curated notes in `raw/Health/` (`Basic Infos.md` = current meds/hormones/goals; `Diagnostics History/` = Yago's own dated diagnostic summaries). When a query needs an actual exam value, **read the PDF live**; use `raw/Health/` for context (his stack, baselines, goals).

**Rule:** resolve the value **live via the Drive MCP** by reading the PDF. Don't answer from numbers copied into the wiki, an older summary, or earlier in the conversation.

## Where the files are

- **Path:** `histórico de exames/Yago`
- **Link:** https://drive.google.com/drive/folders/1xv3Po21QT-8JkpBbfxPcTNybZZx_lYt-
- **Known folder IDs:**
  - `histórico de exames` (parent): `18clbiP-SVolbM8mRFZ5rSYTeZ7RVjjyb`
  - `Yago` (link target): `1xv3Po21QT-8JkpBbfxPcTNybZZx_lYt-`
- **Known file (example):** `labi_exame2.pdf` (`1x5mXkib4d-hVxRjfHKoDjsNe_t8eYYeL`) — Labi Saúde, coleta 04/10/2025: hemograma, estradiol, prolactina, testo total/livre, leptina, serotonina.

## Procedure

### 1. Find the exam file(s)

⚠️ **`'<FOLDER_ID>' in parents` is UNRELIABLE here** — it returns 0 files for this folder (the items are shared/owned externally and don't enumerate by parent). **Use keyword search instead:**

- `gdrive_search` with a content/name keyword: `exame`, `labi`, the lab name, or an exam term (`hemograma`, `colesterol`, `testosterona`). Searches are flaky for these shared PDFs (scanned PDFs don't always index fulltext) — try a few keywords.
- If a specific file still can't be surfaced, **ask Yago to drop the PDF into a local path** (or paste the Drive link to the exact file) and read it from disk.

### 2. Read the PDF (it comes back base64-encoded — must decode)

`gdrive_read_file` on a PDF returns `Contents of <name>.pdf:\n\n<BASE64>` (the binary PDF, base64-encoded, starting `JVBERi0` = `%PDF`). For multi-page reports this **exceeds the token cap**, so the harness saves it to a `tool-results/*.txt` file and gives you the path. Either way, decode it to a real PDF, then Read it:

```bash
# $SRC = the saved tool-results txt (or capture the inline output to a file)
python3 -c "
import base64
d=open('$SRC').read()
b=d.split('\n\n',1)[1].strip()          # drop the 'Contents of ...:' header line
open('/tmp/exam.pdf','wb').write(base64.b64decode(b))
print('ok')
"
```

Then `Read /tmp/exam.pdf` with the `pages` parameter (e.g. `pages: "1-7"`; max 20/request) to view the report.

### 3. Interpret honestly

- Flag each value **High / Low / Normal vs. the printed reference range** (Brazilian notation: `,` is the decimal separator).
- **Cross-reference `raw/Health/Basic Infos.md`** (current hormones, controlled meds, substances, goals) — e.g. high hematocrit/hemoglobin is expected on testosterone; low leptin tracks a cutting phase + GLP-1; estradiol near the ceiling means the AI dose is at its limit.
- Note **what the panel does NOT cover** (lipids, hepatic, renal, glucose/HbA1c, PSA) so gaps are explicit.
- **Boundary:** give the raw reading and the points to raise with his doctor. Dose/conduct decisions belong to the prescribing physician — don't give definitive medical advice (see CLAUDE.md tone/boundaries).
- To persist an evaluation, write a dated note in `raw/Health/Diagnostics History/<YYYY-MM-DD>.md` (date = coleta date) following that folder's pattern: **don't edit old entries; add a new one.**

## Gotchas

- **Don't use `gsheets_read`** — these are PDFs, not Sheets. Use `gdrive_read_file`.
- **Folder enumeration by parent fails** — search by keyword (see step 1).
- **OAuth token expiry → `403 "Method doesn't allow unregistered callers"`.** Same Drive MCP credentials as [[consult-health-sync]] / [[consult-linked-sources]] — follow the re-auth procedure documented in `consult-health-sync` (move stale token aside, run the no-timeout `local-auth` flow).
