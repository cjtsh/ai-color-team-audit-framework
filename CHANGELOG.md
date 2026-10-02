# Changelog

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
