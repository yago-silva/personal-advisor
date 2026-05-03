---
name: Personal Advisor — LLM Wiki Schema
description: Configuration for Claude Code when operating on this knowledge base
---

# Personal Advisor

A personal + career knowledge base maintained by Claude. The user, **Yago Silva** (yago.silva@fluencypass.com, FluencyPass), curates raw sources; Claude reads them, integrates them into this wiki, and keeps the structure consistent over time.

The wiki is the LLM-built compounding artifact between Yago and his raw sources. Yago's job: source, direct, ask. Claude's job: read, summarize, cross-link, file, maintain.

## Three layers

- **`raw/`** — immutable source documents. Read-only.
- **`wiki/`** — Claude-generated and maintained pages. Claude owns this entire layer.
- **`CLAUDE.md`** (this file) — schema and conventions. Co-evolved with Yago over time.

Plus two index files at the root: `index.md` (catalog) and `log.md` (chronological).

## Directory layout

```
.
├── CLAUDE.md
├── index.md
├── log.md
├── raw/
│   ├── articles/       web clips (Obsidian Web Clipper, .md)
│   ├── journal/        first-person notes by Yago (.md)
│   ├── transcripts/    podcast / video transcripts (.md)
│   └── assets/         images, PDFs, attachments
└── wiki/
    ├── self/           identity, values, goals, psychology, health, habits, decisions
    ├── career/         FluencyPass, LinkedIn, professional strategy, skills, network
    ├── people/         one page per recurring person in life or career
    ├── concepts/       mental models, frameworks, recurring ideas
    ├── projects/       active initiatives and decisions-in-progress
    └── sources/        one canonical summary page per ingested source
```

Pages do not need to live exactly under these top-level folders if a more specific subfolder helps. Create subfolders when a category grows past ~10 pages.

## Page conventions

1. **Language**: English, always. Even when sources are Portuguese, summarize and discuss in English. Preserve original-language quotes verbatim.
2. **Filenames**: kebab-case ASCII, e.g. `linkedin-strategy.md`, `paul-graham-bus-ticket.md`. No spaces, no accents.
3. **Wikilinks**: use `[[Page Title]]` (Obsidian-compatible). Cross-link aggressively — entity mentions, concept references, related sources. The wiki's value compounds with links.
4. **Frontmatter**: every wiki page starts with YAML frontmatter:
   ```yaml
   ---
   title: <human-readable title>
   type: self | career | people | concept | project | source
   tags: [<short tags>]
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   sources:
     - "[[Source Page 1]]"
     - "[[Source Page 2]]"
   ---
   ```
   Use the multi-line list form for `sources:` — it's unambiguous YAML and renders cleanly in Obsidian Properties.
   Bump `updated:` whenever you modify the page. Append new entries to `sources:` as they accumulate.
5. **Headings**: H1 matches the title. Use H2/H3 for structure.
6. **Citations**: when a claim comes from a specific source, link the source page inline:
   "He values long-horizon bets ([[Source: Paul Graham — The Bus Ticket Theory]])."
7. **Contradictions**: never silently overwrite. Note explicitly:
   "Earlier journals (2026-Q1) framed this as X; the 2026-04 reflection reframed it as Y ([[Journal: 2026-04-12]])."

## Source page convention

Every file in `raw/` gets a corresponding page in `wiki/sources/`. Frontmatter:
```yaml
---
title: <source title>
type: source
source_type: article | journal | transcript
source_path: raw/articles/whatever.md
source_url: <if web>
source_date: YYYY-MM-DD     # publish or recording date
ingested: YYYY-MM-DD
author: <if known>
tags: [...]
---
```
Body structure:
- 1-paragraph summary
- Key takeaways (bullets)
- Notable direct quotes worth preserving
- **Wiki updates** section listing which other pages this source touched

## Workflows

### Ingest

Trigger: Yago drops a file in `raw/` and says "ingest" / names a path / asks Claude to process it.

1. Read the source in full.
2. Discuss 3–5 key takeaways and ask which threads to emphasize. Skip this step if Yago says "go" or "just ingest."
3. Create `wiki/sources/<slug>.md` per the source-page convention.
4. Walk wiki pages this source touches. For each:
   - Integrate the new info.
   - Add the source to `sources:` frontmatter.
   - Bump `updated:`.
   - Flag any contradiction inline rather than overwriting.
5. Create new entity / concept / project pages where warranted.
6. Update `index.md`: add new pages, refresh one-line summaries on materially changed pages.
7. Append a log entry to `log.md`.
8. Report back: "ingested X, touched N wiki pages, created M new pages, K contradictions flagged."

#### Source-type-specific notes

- **Articles** (`raw/articles/`): typically Obsidian Web Clipper output. Strip boilerplate (cookie banners, related-posts, ads). If images are downloaded to `raw/assets/`, view them when visual context matters.
- **Journal** (`raw/journal/`): first-person from Yago. Treat as primary self-evidence. These mainly update `wiki/self/*`. Quote Yago's words directly with date attribution. Do not paraphrase first-person reflections into third-person observation.
- **Transcripts** (`raw/transcripts/`): can be long. Extract entities (every person and concept mentioned), themes, and quotes worth preserving. If the transcript covers multiple topics, include a mini-TOC in the source page.

### Query

Trigger: Yago asks a question.

1. Read `index.md` first to find candidate pages.
2. Read those pages (and source pages they cite if needed).
3. Synthesize an answer with inline citations: "Based on [[Linkedin Strategy]] and [[Source: That Talk]], ..."
4. If the answer surfaces a new connection, comparison, or analysis worth keeping, **offer** to file it back as a wiki page (typically `wiki/concepts/` or `wiki/self/`). Do not file unprompted unless Yago says "file useful answers automatically."
5. Append a query entry to `log.md` if the work was substantive (skip for trivial lookups).

### Lint

Trigger: Yago says "lint" or "health check."

Walk the wiki and report:
- Contradictions between pages
- Stale claims newer sources have superseded
- Orphan pages (no inbound `[[wikilinks]]`)
- Important entities/concepts mentioned but lacking their own page
- Missing cross-references (page A clearly should link page B but doesn't)
- Data gaps that could be filled with web search

Then propose a plan. Do not auto-fix — wait for approval.

## index.md format

Catalog organized by category. Each entry: `- [[Page Title]] — one-line summary (N sources)`.

Sections, in this order: **Self**, **Career**, **People**, **Concepts**, **Projects**, **Sources** (latest-first within Sources).

Keep entries skimmable; this file is loaded into context on every query.

## log.md format

Append-only. Each entry starts with a parseable header so `grep "^## \[" log.md | tail -10` works.

```
## [YYYY-MM-DD] ingest | <Source Title>
- pages created: X, Y
- pages updated: A, B, C
- notes: <noteworthy items — contradictions surfaced, entity created, etc.>

## [YYYY-MM-DD] query | <one-line question>
- pages consulted: A, B
- output: chat-only / filed as [[New Page]]
- notes: <if useful>

## [YYYY-MM-DD] lint
- findings: <count>
- actions: <list>
```

## Output formats beyond markdown

Default: markdown wiki pages.

On request:
- **Comparison** → markdown table.
- **Slide deck** → Marp markdown at `wiki/decks/<slug>.md` with Marp frontmatter (Marp Obsidian plugin not yet installed; flag that the plugin is needed when first used).
- **Chart** → matplotlib script at `wiki/charts/<slug>.py` plus the rendered PNG at `wiki/charts/<slug>.png`. Reference the PNG from the relevant wiki page.
- **Canvas** → Obsidian `.canvas` file (JSON) under `wiki/canvases/`.

## Tone and voice

- Wiki pages: neutral, structured, concrete, third-person — except `wiki/self/*` which can quote Yago's first-person journal text directly with date attribution.
- No filler. No "in conclusion." No "it's important to note." Claims and citations only.
- When uncertain, say so explicitly: "Two journal entries from 2026-03 suggest X, but no other sources confirm."
- Brevity beats completeness. A page that says one true thing and links to three others is better than a page that says ten vague things.

## Operating principles

- The wiki is a compounding artifact. Every ingest should leave it richer than it was — at minimum, one new cross-link.
- Yago directs; Claude maintains. Never invent claims about Yago that aren't grounded in a source.
- When a question opens up a useful framing, offer to file it. The wiki should grow from queries too, not just ingests.
- The schema is co-evolved. If a workflow recurs (e.g. weekly review), Yago and Claude formalize it in this file.

## Optional tooling (not yet installed)

- **Obsidian Web Clipper** browser extension for fast article ingest into `raw/articles/`.
- **Dataview** plugin to run frontmatter queries (e.g., recent updates, source counts per page).
- **Marp** plugin for slide-deck rendering.
- **qmd** (https://github.com/tobi/qmd) — local hybrid BM25/vector search if `index.md` outgrows being readable in one pass (~200 sources).

Mention these only when their absence becomes a friction point.
