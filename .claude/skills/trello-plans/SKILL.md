---
name: trello-plans
description: Use when Yago wants to turn a goal, project, or multi-step intent into a structured plan in Trello — an epic plus its subtasks — in the Familia workspace. Creates the epic on the shared "Compartilhado" board's Épicos list, creates each subtask as a card, links them under the epic via Hello Epics (card-link attachment on the epic), and assigns a responsible member so the native Butler automation mirrors the card to that person's personal board. Triggers on "criar um plano", "monta um épico", "plano pra <objetivo> no Trello", or any request to break work into Trello tasks for the family.
---

# Structured plans in Trello (Familia workspace)

Turn an intent into an **epic + subtasks** on the shared board, wired into Hello Epics, with responsibles assigned so they mirror to personal boards automatically.

## Fixed facts about this workspace (verify with MCP if anything looks off)

Workspace **Familia** — `60cbd753986f23844f35d84b`.

| Board | Board ID | Role |
| --- | --- | --- |
| **Compartilhado** | `6488fd89c99393966251bd84` | All epics + the canonical (source) subtask cards live here |
| **Pessoal - Yago** | `61ba00a22e8ae9245fa25ce4` | Mirror target — never write here directly |
| **Pessoal - Stephanie** | `6a25e12b14b92430d07eca40` | Mirror target — never write here directly |

**Compartilhado lists** (workflow order):

| List | List ID | Use |
| --- | --- | --- |
| Épicos | `6488fd91d5fd1f9c23cac8bf` | **Epics only** |
| Pendências | `6a259bf768b9d226d877deba` | **Default landing list for new subtasks** (backlog) |
| Essa Semana | `649204d66adc797f4cae42fd` | Subtask the plan marks for this week |
| Fazendo | `6492051e7165bbce5291dad4` | In progress |
| Feito | `6492051729072f88da92b6e1` | Done |
| Histórico | `6a25f65dbb688bc4f48d819c` | Archive |

**Members** (the responsible drives the mirror automation):

| Person | Member ID |
| --- | --- |
| Yago | `5788559e14779b440c74ae3e` |
| Stephanie | `5d3c5f235ae4f07e11273a35` |

**Labels on Compartilhado** (apply only when clearly relevant):

| Label | ID | Color |
| --- | --- | --- |
| apartamento | `6488fd89eaa9d8e931386a54` | green |
| carros | `6488fd89eaa9d8e931386a64` | purple |
| Lorena | `661bf8df2f0f4fb2bbdf7f4a` | pink |

> IDs are a cache. If `get_lists` / `get_board_labels` / `get_board_members` ever disagree with this table, the live MCP result wins — re-read and proceed (and update this table if a list/label was renamed).

## The two non-obvious mechanics

1. **Hello Epics hierarchy = a card-link attachment on the epic.** To make a subtask a child of the epic, attach the **subtask's URL** to the **epic card** with `attach_file_to_card` (use the subtask's `shortUrl`, e.g. `https://trello.com/c/<shortLink>`). The attachment goes on the *parent epic*, pointing at the child. The child needs nothing extra. Trello renders any `trello.com/c/...` attachment as a card link, which Hello Epics reads as the parent→child relationship.

2. **Mirroring is automatic — never create cards on personal boards.** Yago's Butler automation mirrors a card to a member's personal board the moment that member is assigned. So: create every subtask on **Compartilhado**, then `assign_member_to_card`. Do not call `add_card_to_list` against a personal board, and do not try to manage the mirror — `mirrorSourceId` cards are downstream copies.

## Workflow

### 1. Gather the plan
From Yago's request, draft:
- **Epic**: short imperative name + one-line outcome (goes in the epic's description).
- **Subtasks**: each with a name, the responsible member (Yago / Stephanie / shared-unassigned), target list (default **Pendências**; promote to **Essa Semana** only if Yago flags it for now), optional label, optional due date.

If responsibles or scope are ambiguous, ask before drafting — don't guess who owns what. Respect the boundary: don't prescribe direction for Stephanie's own work; if a subtask is hers, it's because Yago assigned it (see `[[feedback-stephanie-career-boundary]]` in memory).

### 2. Show the plan and confirm (required)
Present the full structure as a compact table — epic, then each subtask with responsible / list / label — and wait for Yago's go-ahead. **Do not touch Trello before approval.** This keeps the shared board clean. Adjust on feedback, re-show if materially changed.

### 3. Execute (after approval)
In order:
1. `set_active_board` → Compartilhado (`6488fd89c99393966251bd84`).
2. **Create the epic**: `add_card_to_list` on list `6488fd91d5fd1f9c23cac8bf` (Épicos), with name + description. Capture its `id` and `shortUrl`.
3. For **each subtask**:
   a. `add_card_to_list` on its target list (default Pendências `6a259bf768b9d226d877deba`), with name, description, labels, due/start if any. Capture its `id` and `shortUrl`.
   b. `assign_member_to_card` with the responsible's member ID (triggers the mirror). Skip if the subtask is intentionally unassigned/shared.
   c. `attach_file_to_card` on the **epic** card (`cardId` = epic id), `fileUrl` = the **subtask's** `shortUrl`, `name` = subtask name → registers it under the epic in Hello Epics.

Create subtasks sequentially so each `shortUrl` is captured before attaching. Independent reads can be parallel, but the create→assign→attach chain per card is ordered.

### 4. Report back
Summarize: epic created (with link), N subtasks created, who each is assigned to (and therefore which personal board it mirrored to), any labels applied. Give the epic's `shortUrl` so Yago can open it.

## Gotchas

- **Epic description carries the context.** Cards are terse; put the plan's intent/acceptance in the epic description (and subtask descriptions when non-obvious), since the board is the shared family surface.
- **Don't re-attach** an already-linked subtask — check the epic's existing `attachments` if extending an epic that already has children.
- **Adding to an existing epic**: find it in the Épicos list (`get_cards_by_list_id`), reuse its id, then run step 3.c per new subtask. Don't create a duplicate epic.
- **No literal financial values** in card descriptions if a sheet tracks the number — reference the sheet instead (repo convention #8 / `[[feedback-no-literal-financial-values]]`).
- The MCP `attach_file_to_card` needs the file URL reachable as a Trello card link — always pass the `c/<shortLink>` form returned on card creation, not the long `/c/<id>/<slug>` path.
