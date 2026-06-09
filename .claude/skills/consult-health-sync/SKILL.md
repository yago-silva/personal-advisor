---
name: consult-health-sync
description: Use whenever you need health or fitness data about Yago — weight/body composition, heart rate, steps, sleep, or workouts/activities. The Health Sync app (Android) exports Samsung Health data live to five Google Drive folders. Always read those folders LIVE via the Drive MCP for current values instead of trusting numbers transcribed in the wiki or earlier in the conversation. Triggers on any query or ingest about Yago's body metrics, vitals, activity, sleep, or training where a current/dated value is needed.
---

# Health & fitness data lives in Google Drive (Health Sync → Samsung Health)

Yago runs the **Health Sync** app on Android, which continuously exports his **Samsung Health** data to Google Drive as CSV files. This is the **raw device-level feed** — the source of truth for body metrics, vitals, activity, and sleep. It is distinct from the manually-curated notes/Sheets in `raw/Health/` (`Body Measures History.md`, `Basic Infos.md`, Diet/Workout histories), which are Yago's own summaries. When a query needs a *current or dated* health value, read the Drive feed live; use `raw/Health/` for context, baselines, and Yago's own narrative.

**Rule:** resolve the value **live via the Drive MCP**. Don't answer from numbers copied into the wiki, an older summary, or earlier in the conversation — the feed updates continuously.

## The five folders (one per metric)

All live under the same shared-drive root (`0AHCHyp5zQtmNUk9PVA`).

| Metric (PT) | Folder name | Folder ID | CSV columns |
| --- | --- | --- | --- |
| **Peso / composição** | `Health Sync Peso` | `1gL11Trw_F3ZfgyDo-8msMnsr9rZgtl6I` | `Data, Hora, Peso, Porcentagem de gordura corporal, Massa de gordura corporal, Porcentagem livre de gordura, Massa livre de gordura, Porcentagem de músculo esquelético, Massa muscular esquelética, Porcentagem de massa muscular, Massa muscular, Massa óssea, Água corporal total, Taxa metabólica básica` |
| **Frequência cardíaca** | `Health Sync Frequência Cardíaca` | `1PLOgw63WVpb7SdcemYabcScwxDnbMY7z` | `Data, Hora, Frequência Cardíaca, Origem` (1 row ≈ every 10 min) |
| **Passos** | `Health Sync Passos` | `11vtdoDt-keig0WxCrI9xkUNNRONPJkOy` | `Data, Hora, Passos` (per intraday interval) |
| **Sono** | `Health Sync Dormir` | `1_vRM4RrZWw1EmOb5wV-XTx6SRgexuUn4` | `Data, Hora, Duração em segundos, Fase do sono` (`light`/`deep`/`rem`/`awake`) — one file per sleep session |
| **Atividades / treinos** | `Health Sync Atividades` | `1iUV7Syp2yPJWO-Qfvo03XYEkgzM32srD` | `Aplicação de origem, Tipo de atividade, Nome da atividade, Data, Hora, Tempo decorrido, Tempo ativo, Distância (km)` — one file per workout |

## File naming & granularity

Health Sync writes the **same metric at multiple granularities** — pick the file that matches the question:

- **Daily:** `<Métrica> 2026.06.08 Samsung Health.csv`
- **Weekly:** `<Métrica> 23-2026 Samsung Health.csv` (`<ISO-week>-<year>`)
- **Monthly:** `<Métrica> maio 2026 Samsung Health.csv` (PT month name)
- **Sleep:** `Dormir 2026.06.07 01:56:00 Samsung Health.csv` (one per session, stamped with bedtime)
- **Activity:** `<TYPE> 2026.06.08 18.51 Samsung Health.csv` — e.g. `CYCLING`, `WALKING`. Each workout also has binary `.fit` and `.tcx` companions (GPS/HR tracks) — **ignore those for data reads; use the `.csv`.**

Date format inside files is `YYYY.MM.DD HH:MM:SS`. Values use `.` as decimal separator and are often quoted.

## Procedure

1. **Choose the folder** for the metric (table above) and the **granularity** that fits the question (a single day → daily file; a trend → weekly/monthly).
2. **List the folder live** to find the right file — its contents change as new data syncs:
   - `gdrive_search` with a query scoped to the folder, e.g. `'<FOLDER_ID>' in parents and name contains 'maio 2026'`, or list recent files and pick the latest by name/date.
3. **Read the CSV live** with `gdrive_read_file` by file ID (returns the CSV text).
4. **Parse the relevant columns**, compute what's asked (latest value, daily total, average, sleep-stage breakdown…), and **cite the file name + folder** so the read is verifiable. Note the read time for time-sensitive values.
5. For weight/body-composition: only `Peso` is reliably populated by a smart scale; the other body-comp columns are frequently `0.0` (not measured) — don't report zeros as real.

## Gotchas

- **Files report `mimeType: text/troff`** (Drive mis-sniffs them) but they are **plain CSV** — read with `gdrive_read_file`, not `gsheets_read` (these are not Google Sheets).
- **Don't read whole large folders/files blindly.** Monthly heart-rate/steps files have hundreds–thousands of rows; scope by file and, if needed, summarize rather than dumping every row into context.
- **Multiple granularities overlap** — a given day appears in the daily, weekly, and monthly file. Pick one to avoid double-counting.
- **OAuth token expiry → `403 "Method doesn't allow unregistered callers"`.** The Drive MCP token lasts ~2 days and the auto-refresh is unreliable. When the MCP starts returning 403, re-authenticate (interactive browser login required):
  ```bash
  # 1. Move the stale token aside
  mv ~/.config/gdrive-mcp/.gdrive-server-credentials.json{,.expired}
  # 2. Run the package's auth flow with NO timeout (the bundled flow caps at 30s, too short):
  BASE=$(find ~/.npm/_npx -type d -name "mcp-gdrive" | head -1)/../..
  cat > "$BASE/reauth.mjs" <<'JS'
  import { authenticate } from "@google-cloud/local-auth";
  import { google } from "googleapis"; import fs from "fs";
  const D="/home/yago/.config/gdrive-mcp";
  const a=await authenticate({keyfilePath:D+"/gcp-oauth.keys.json",
    scopes:["https://www.googleapis.com/auth/drive.readonly","https://www.googleapis.com/auth/spreadsheets"]});
  const {credentials}=await a.refreshAccessToken();
  fs.writeFileSync(D+"/.gdrive-server-credentials.json",JSON.stringify(credentials,null,2));
  console.error("AUTH_OK"); process.exit(0);
  JS
  cd "$BASE" && node "$BASE/reauth.mjs"   # opens browser; Yago completes the Google login
  ```
  Then the MCP reconnect picks up the fresh token. (Same creds dir/scopes power `consult-linked-sources` finance Sheets.)
- This shares the connected-account scopes with the finance Sheets — see [[consult-linked-sources]] for the general live-read pattern and finance file IDs.
