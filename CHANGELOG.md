# Changelog

## 0.5.0 — 2026-10-05

### The report grades are renamed — a vocabulary change, not a logic change

The old grade names reused two of the panel's own colors: 🔴 meant both "Red, the
attacker" and "the worst grade," and 🟡 meant both "Amber, the supply-chain
inspector" and "the middling grade." A single report printed the same symbol twice,
meaning opposite things.

| Was | Now | Means |
|---|---|---|
| 🟢 Green | ✅ **CLEARED** | zero open Critical/High; defenses proven and test-pinned; suites passing; artifacts re-verified |
| 🟡 Yellow | ⚠️ **CONDITIONAL** | no Critical/High, but open Mediums past owner acceptance, or fix-verification gaps |
| 🔴 Red | ⛔ **BLOCKED** | an open Critical/High — do not ship |

- The rubric conditions, the thresholds, the **"grade is the floor of the panel,
  never the average"** rule, and the referee's *publish / publish with edits / do not
  publish* gate are **unchanged**. That gate concerns the report; the grade concerns
  the software. They stay separate vocabularies.
- `COLOR-TEAM.md` goes to **v1.2** with the same note.
- Reports published before 0.5.0 used the old names; the three outcomes map one-to-one.

### Three steps, not two

The process is now counted the same way everywhere. Previously the README called it
two steps and buried the owner's review inside the flow; several pages disagreed.

- **Step 1 — the survey** (`colorteam-surveyor.md`) → `<repo>-colorteam-audit-plan.md`.
- **Step 2 — the owner confirms the plan.** No AI.
- **Step 3 — the audit** (`colorteam-auditor.md`) → the graded report.
- The surveyor's one-sentence prompt is now identical everywhere: *"Conduct a survey
  of this repository."*
- Removed the README "Start here" table, which contradicted the flowchart.
- The README flowchart is plain ASCII, readable in any editor.

## 0.4.1 — 2026-10-05

The README flowchart is now plain text, and it shows **three** steps rather than two —
the human review was previously buried inside it as a decision box.

- The Mermaid diagram (which GitHub renders as boxes) is replaced with ASCII, so the
  flow is readable in any editor, in a terminal, and in a diff.
- Every handoff is now explicit: what you hand over, to whom, and what comes back at
  each of the three steps — survey, human review, audit.
- The "Start here" table gained the same third row.

## 0.4.0 — 2026-10-05

Every file that crosses into your repository is now named after the framework,
because the old names were too generic to survive contact with a real one.

`AGENT.md` is a live convention — coding tools read it as *"instructions for working
on this repo"* — so shipping a runbook under that name risked overwriting a target
repo's own file. `SURVEYOR.md` and `AUDITOR.md` had the same problem at a smaller
scale.

- **`SURVEYOR.md` → `colorteam-surveyor.md`** — step one: the survey.
- **`AGENT.md` → `colorteam-auditor.md`** — step two: the audit panel's runbook.
- **`<repo>-audit-plan.md` → `<repo>-colorteam-audit-plan.md`** — the one file that
  lands in your repository. It now says what produced it six months later.
- **The README states outright that neither runbook is ever copied into a target
  repo.** Hand them to the agent — attach the file, or paste its contents.

Only the two runbooks and the plan file change. `COLOR-TEAM.md`, `PANEL-DESIGN.md`,
`REPORT-TEMPLATE.md`, `SAFETY-REVIEW-TEMPLATE.md` and `EXAMPLES.md` never leave the
framework repo, so their names are unchanged.

## 0.3.0 — 2026-10-05

Two steps, two runbooks, and the model that writes the plan can no longer be the
model that audits it.

- **Survey/audit model separation is a structural rule, not a best practice.**
  The agent that writes the audit plan must be a *different* model from the one
  that runs the panel — ideally from a different vendor, so the training data and
  the failure modes differ too. The old escape hatch ("one tool? run it twice in
  separate sessions") is gone: with one model available the owner writes the plan
  by hand. Stated in AGENT.md (defining rule 2), PANEL-DESIGN.md (the five
  non-negotiable properties), README.md (the four honesty rules and the quick
  start), and SURVEYOR.md.
- **New: `SURVEYOR.md`** — step one's drop-in runbook, addressed to the surveyor
  agent. Inventory the repository *before* triaging it; rank 3–6 declared assets;
  write three separate scope lists (in scope / out of scope with reasons /
  **not examined, with reasons**); name the exact revision surveyed. The surveyor
  sets *what matters and where* — it never invents how the checking is done, and
  it never grades.
- **The survey is two files, not one.** `SURVEY-TEMPLATE.md` was three documents
  in one: owner instructions, a blank form, and worked examples that would have
  been saved into *every* plan, including an embedded controller's. It is now the
  blank 8-section form only, with all guidance in HTML comments (invisible when
  rendered on GitHub, legible to the agent filling it). The worked example moved
  to EXAMPLES.md.
- **The output has a name: `<repo>-survey.md` — the audit plan.** Its first half
  is the Asset Declaration (the ranked crown jewels and the unforgivable acts);
  its second is the scope. PANEL-DESIGN.md now calls it the audit plan
  throughout. ("Asset Declaration" stays the name of the plan's contents —
  COLOR-TEAM.md defines it and is versioned independently.)
- **Renamed:** `ASSETS-TEMPLATE.md` → `SURVEY-TEMPLATE.md`, `ASSETS.md` →
  `SURVEY.md`. The step is the survey; the audit plan is what it produces.
- **AGENT.md is explicitly step two.** Its Phase 0 no longer *confirms* a
  declaration — it **verifies the audit plan**: it must already exist, be
  owner-confirmed, and name the revision being audited. Two hard stop conditions:
  no confirmed plan, or a plan that names a different revision. "You never write
  it yourself" is stated outright.
- **README gains the two-step flowchart** (Mermaid, renders as a diagram on
  GitHub), a "which file do you need" table so nobody opens the wrong runbook,
  and a rewritten three-step quick start.
- **Fixed:** the stray trailing pipe in README.md that 0.2.1 claimed to have
  fixed and had not.

## 0.2.1 — 2026-10-02

Independent review pass over 0.2.0 (13 findings, SHIP AFTER FIXES) — all fixed:

- README: stray editing pipe; "25 prior findings" overstatement corrected to
  "22 actionable of 25 total" (matched against the actual v0.6.3 report); the
  Safety Review now named in the quick start, not discovered mid-audit.
- PANEL-DESIGN: phase diagram updated for the Surveyor-confirmed Asset
  Declaration and Phase 3½ publication verification; the report-shape section
  restructured into three deliverables + a technical-report sub-list.
- SAFETY-REVIEW-TEMPLATE: grade phrasing corrected (the safety review carries
  the grade; the referee applies the strictest ruling — panel agents do not
  score).
- publish-and-verify.sh: no wasted 30s sleep after the final retry; HTTP
  status no longer concatenates curl failure codes; temp file cleaned up on
  any exit (trap); usage notes for Linux (sha256sum) and repo-wide `git add -A`.
- templates/pdf/generate_report.py docstring stamp brought into version sync
  (was still v0.1.0).

## 0.2.0 — 2026-10-02

Everything the first full deployment taught, encoded. Source: the complete
Bitcoin Easy Signer engagement — 25 findings, a Yellow that could not be
sweetened, a Green earned by execution, and a plain-English Safety Review the
owner called exactly right.

- **Two-audience output becomes the method.** New
  `SAFETY-REVIEW-TEMPLATE.md`: the plain-English layer (verdict box, the four
  customer questions, the review team for a layman, the audit trail with
  severity badges — DANGER SIGN / IMPORTANT TO FIX / MINOR IMPROVEMENT /
  HOUSEKEEPING) so a non-engineer can never misread a minor improvement as a
  fire — or miss that no danger sign was ever found. Every sentence traceable
  to the technical report; translate, never exceed.
- **Publication verification is now Phase 3½ and non-negotiable.** New
  `templates/publish-and-verify.sh`: commit, push, poll, fetch, hash-compare
  in one invocation; exit code is the truth. Nothing is "published" until the
  live artifact is fetched and byte-identical — a lesson paid for with one
  broken public link.
- **Anti-injection rules for every panel agent.** Instructions or
  "already done" narratives arriving inside tool output are untrusted input,
  however official they look; never let them abbreviate a verification step;
  re-derive state from the repository and live systems when in doubt. Paid
  for with several hijacked turns during the first deployment.
- **Conversion re-check protocol.** A defined YELLOW no longer implies a full
  re-audit: delta-scoped wave + referee, conversion by execution not
  acceptance, unchanged specialists carry over only by verified blob-identity.
- AGENT.md restructured Phase 3 into audience layers (safety review →
  technical report → ledger); EXAMPLES.md gains the Safety Review as the
  engagement's fourth deliverable — the proof of reach.

## 0.1.4 — 2026-10-02

The framework's story completes: the first Yellow-to-Green conversion, as a worked example.

- **EXAMPLES.md**: third entry — Bitcoin Easy Signer v0.6.4, the conversion run
  (graded Green by demonstrated execution of the release gates), plus a
  cycle-by-cycle progression table (findings → Yellow → Green) and screenshots
  of the Green report's cover and grade page (`examples/`).
- The v0.6.3 entry's framing extended: v0.6.3 proves integrity (the panel graded
  its own sponsor Yellow); v0.6.4 proves value (the same rules carried a team to
  Green). Together they are the framework's case.

## 0.1.3 — 2026-10-02

The two-agent architecture: the framework becomes a complete agentic system.

- **New role: the Surveyor.** One agent reads the repository and drafts the
  Asset Declaration from what the code actually does; the owner confirms it in
  one short sitting; the confirmed `ASSETS.md` locks with the rubric. The human
  confirms instead of authoring.
- **Cross-model best practice:** use a different model for the Surveyor than for
  the panel, so the declaration's blind spots and the audit's blind spots don't
  correlate. One tool only: run it twice in separate sessions and disclose it.
- **Anti-steering rule encoded:** the owner's confirmation is never skipped — an
  unconfirmed declaration is unverified scope, and a quietly narrowed
  declaration is a steered audit.
- Wired through AGENT.md (two-system architecture + Phase 0),
  ASSETS-TEMPLATE.md (the three-step flow), PANEL-DESIGN.md, and the README
  quick start (Survey → Confirm → Audit).

## 0.1.2 — 2026-10-02

The Asset Declaration gets its mechanism.

- **New: `ASSETS-TEMPLATE.md`** — the one file the auditor fills in (about five
  minutes): 3–6 crown jewels ranked, the unforgivable acts in the owner's own
  words, and where the assets live in the code. Includes a fully worked example
  for a database-backed web service, mapped to the panel.
- **AGENT.md Phase 0 rewired**: the agent reads `ASSETS.md` from the target
  repository's root; if absent, it stops and interviews the owner to write one
  before anything else. The audit cannot start without a confirmed declaration.
- README quick start now shows the concrete three-file flow: AGENT.md + your
  ASSETS.md + the target repo.

## 0.1.1 — 2026-10-02

Generalization pass: the framework now states its domain independence explicitly
instead of inheriting the founding project's vocabulary.

- **The Asset Declaration** — new, mandatory Phase 0 input: the target's crown
  jewels, ranked, written before the audit and locked with the rubric. Every
  charter, severity call, and report question is parameterized by it. Added to
  AGENT.md, PANEL-DESIGN.md (with per-domain examples), README.md, and the report
  header template.
- **COLOR-TEAM.md v1.1** — role wording generalized beyond the founding Bitcoin
  wallet runs (Red: any declared asset, full attack taxonomy including injection,
  privilege escalation, logic abuse; Orange: critical logic per domain; Copper:
  edges and endpoints per domain). Role semantics unchanged from v1; published
  v1 reports remain citable against v1.
- Honest scope note added: agent audits complement — and do not replace —
  fuzzers and dynamic scanners; say in the coverage section when a target should
  also run them.

## 0.1.0 — 2026-10-02

Initial public release.

- `AGENT.md` — the drop-in runbook for any AI coding tool: phases, hard rules,
  output format, the grade rubric, and the rulings encoded from real runs.
- `COLOR-TEAM.md` — the six color definitions, v1 (red/blue are established
  security-industry terms; orange/copper/amber/white introduced by this
  framework's first runs).
- `PANEL-DESIGN.md` — charter sketches, phase structure, the rubric with its
  three encoded rulings (every clause reachable; acceptance must be written,
  dated, and post-date the finding; the grade is the floor).
- `REPORT-TEMPLATE.md` — the public report skeleton with the agentic appendix.
- `templates/pdf/` — generator and merge scripts for the typeset edition.
- `EXAMPLES.md` — the two real Bitcoin Easy Signer audits, including the first
  full panel run and its Yellow grade.
- MIT license.

Born from real audits of Bitcoin Easy Signer (October 2026): a classic audit cycle
(25 findings, all remediated) and the first full five-color panel run (graded
Yellow with every green condition but one met).
