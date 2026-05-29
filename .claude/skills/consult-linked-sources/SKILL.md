---
name: consult-linked-sources
description: Use whenever you need data that a raw/ source references through an external file link (Google Drive / Google Sheets today; more file types in the Drive in the future). Always open and read that linked file LIVE via the Drive MCP to get current values, instead of relying on numbers transcribed elsewhere in the wiki or in chat history. Triggers on any query or ingest where the answer depends on a value that lives in a linked external file.
---

# Linked files are the source of truth — read them live

Yago's raw notes increasingly act as **thin pointers**: instead of holding data inline, they link external files in his Drive. `raw/journal/Finances.md` is the first example (it links three Google Sheets), but the pattern generalizes — expect more Drive files (sheets, docs, etc.) referenced this way over time.

**Rule:** when a raw source points to an external file and you need a value from it, **resolve the link live via MCP**. Do not answer from numbers copied into the wiki, an older summary, or earlier in the conversation — those drift. The linked file is canonical.

## Procedure

1. **Find the link** in the relevant `raw/` file (look for `https://docs.google.com/...` or `https://drive.google.com/...`).
2. **Extract the file ID** — the long token after `/d/` in the URL. A `gid=` in the URL is the tab/sheet ID.
3. **Read it live:**
   - Google Sheet → `gsheets_read` with targeted A1 `ranges` (full-sheet reads overflow context — always range-scope). Pass `sheetId` for a specific tab.
   - Quick whole-tab glance → `gdrive_read_file` (returns a compact CSV of the first/default tab).
   - Other Drive file → `gdrive_read_file` by ID; `gdrive_search` to locate by name if the link is missing.
4. **Use the live value** in your answer, and **cite the sheet/file** (and tab) so the reader can verify.
5. If filing anything financial back to the wiki, follow the companion skill `finance-wiki-references` (reference the sheet, don't hardcode the value).

## Known links (finance — will grow)

| Raw reference | File ID | Notes |
| --- | --- | --- |
| 2026 Cash Flow | `15qSiPTHYmzh1_ItzET0VZStiVu32KEodbBxU30Sl78w` | one tab per month |
| Net worth | `13cod5YUveCILRhjTISBC6xe8za1xNRLSjFkRw4edFxg` | `Resumo` summary tab |
| Stock portfolio | `1v6eTPtx7KzHi77kn6KMjG9nQtfHwXY2nbbhMBzrzgSY` | per-ticker `Carteira de ações` |

## Gotchas learned in practice

- The **Google Sheets API must be enabled** on the connected GCP project for `gsheets_read`; if it errors with an "API not enabled" message, `gdrive_read_file` (CSV export) still works as a fallback.
- **Full-sheet `gsheets_read` overflows** the context (thousands of empty rows). Always pass `ranges`, or read the saved tool-result file in chunks.
- **Live B3 quotes drift intraday** — the same portfolio can read slightly differently minutes apart. Treat sheet values as a live snapshot, note the read time, don't over-precision.
- Different `gid`s in a URL can resolve to the **same tab** (e.g. two finance links both land on `Resumo`). Verify the `sheetName` in the response.
