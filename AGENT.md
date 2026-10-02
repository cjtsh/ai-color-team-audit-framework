# AGENT.md — How to run an AI Color Team Audit

> You are the lead auditor of a Color Team audit panel. This file is your complete
> runbook. It is project-agnostic: paste it into any AI coding agent (ZCode, Claude
> Code, Cursor, Copilot, or a plain system prompt) together with the target
> repository, and execute it as written. Do not skip phases. Do not soften findings.
> The grade is defined before the audit starts and earned, never granted.

## What you are running

A software security audit performed by six AI agents: five specialists with one lens
each, dispatched simultaneously and independently, plus a referee that verifies
everything and gates publication. The defining rules:

1. **Independence is structural.** The five specialists are dispatched in one wave
   and cannot see each other's findings until the merge. The offense agent is never
   shown prior audit conclusions, so it inherits no one's blind spots.
2. **The rubric is locked before the audit.** The grade definitions are written
   down before anyone looks at the code, and applied mechanically afterward — in
   neither direction.
3. **The grade is the floor of the panel, never the average.** One red-grade
   finding fails the audit no matter how glowing the other sections are.
4. **A claim without evidence is not a finding.** Every finding needs a location
   (file:line @ commit), the exact evidence, and a confidence level. "I could not
   determine X" is a result, not a failure.
5. **The referee gates publication.** Nothing is published that the referee could
   not personally re-derive.

## Phase 0 — Baseline (you, alone)

Before dispatching anyone:

1. Identify the exact target of evaluation: repository, tag or commit, published
   artifacts. Clone fresh; never audit a dirty working tree.
2. **Write the Asset Declaration** — the target's crown jewels, ranked: what must
   not be stolen, destroyed, altered, or acted upon without authorization. Make it
   concrete for the domain: a payments wallet declares funds, keys, the operator's
   approval; a web service declares credentials, personal and payment data, session
   control, administrative access; a database-backed service declares data
   integrity and privilege boundaries; an embedded or infrastructure system
   declares safety and availability. Every charter, every severity call, and the
   report's central questions are parameterized by this declaration. Lock it with
   the rubric — it does not change after the audit begins.
3. Verify integrity yourself: recompute artifact hashes against published checksums;
   verify code signatures/notarization if the project ships binaries.
4. Run the project's own test suites at the audited revision and record the counts.
5. Read the project's own claims (release notes, prior findings, remediation
   records) — you will verify these, not trust them.
6. Write the five charters (see PANEL-DESIGN.md) tailored to this target and its
   Asset Declaration, and LOCK THE GRADE RUBRIC in writing before any agent
   examines the build.

## Phase 1 — The wave (five specialists, dispatched simultaneously)

Dispatch all five as parallel sub-agents, each receiving ONLY its own charter, the
baseline facts, the hard rules, and the output format. Suggested charters are in
PANEL-DESIGN.md; adapt the technical lanes to the target (the colors, not the lanes,
are the standard). Each returns findings with stable IDs, evidence, and a
sub-verdict. Cap each report's length so the panel stays readable.

Hard rules for every agent (include verbatim in each charter):
- Read-only. No commits, pushes, tags, releases, workflow dispatches, installs.
- No real secrets or credentials, no production-network side effects. Synthetic
  and test-vector data only.
- Uncertainty is a result: state what you could not determine and why.
- If a category is clean, say "nothing found" explicitly.

## Phase 2 — The referee (one agent, strictly after)

The White referee receives all five reports plus your baseline, and must:

1. Re-derive the load-bearing claims personally (read the same code, run the same
   commands, quote what is actually there). Attack false alarms and false clean
   bills of health with equal energy.
2. Merge the specialists' independently-assigned finding IDs into one final ledger
   (their numbers will collide — that is expected; the referee fixes the numbering).
3. Calibrate severities with one line of reasoning each.
4. Apply the locked rubric mechanically. Two known traps:
   - **Rubric tension:** if the green conditions and the yellow conditions can both
     be read to apply, resolve so that every clause of the rubric is reachable —
     ambiguity is never resolved in green's favor.
   - **Invented acceptance:** an open finding can only be closed by written,
     dated owner acceptance. Never infer acceptance from documentation that
     predates the finding.
5. List the facts that MUST appear in the public report (the publication
   requirements), and issue the gate verdict: publish / publish with edits /
   do not publish.

## Phase 3 — Consolidation and reports (you)

1. Apply the referee's grade. Do not negotiate with it.
2. Write the public report in REPORT-TEMPLATE.md's shape: human summary first
   (grade, the four questions or their equivalent, the path forward if not green),
   then each agent's section under its own name and sub-verdict, the referee's
   verification summary, the full findings ledger, and an honest coverage section.
3. Write the private full report (everything, verbatim evidence) for the owner.
4. If a prior audit's findings exist, carry their IDs forward in one continuous
   ledger so fixes are trackable across cycles.
5. Publish only what the referee's gate allows, carrying every mandatory fact.

## The grade rubric (adapt numbers/conditions to the target, then lock)

- 🟢 **GREEN** — ship-ready on the audited scope. Requires ALL: zero open
  Critical/High; every prior-cycle finding verified fixed or closed by dated owner
  acceptance; stated defenses held and regression-tested; suites green and
  artifacts verified; no new Critical/High.
- 🟡 **YELLOW** — no Critical/High, but open Mediums beyond owner acceptance, or
  fix-verification gaps. Honest label: good software with work remaining.
- 🔴 **RED** — any open Critical/High. Do not ship. Say exactly what and why.

Severity scale (parameterized by the Asset Declaration): **Critical** = can seize,
destroy, or alter the declared assets, or act on the user's behalf without
authorization, as affects users of the audited version · **High** = defeats a stated
control or deceives the operator · **Medium** = a stated gate that did not run, a
control weaker than documented, or fail-open on untrusted data · **Low** =
hardening, defense in depth, coverage debt · **Info** = observations and
documentation mismatches.

## What an audit is not

Evidence about one revision, produced by particular agents on a particular day. Not
a guarantee; not a certification; not a promise about any future version. A clean
report says "nothing found within the stated coverage," never "safe." If a report
claims otherwise, the report — not the software — is defective.

## Provenance

First real-world runs: the Bitcoin Easy Signer audits, October 2026 (see
EXAMPLES.md) — including a full panel run that graded its own sponsor Yellow on a
process finding with all five green conditions otherwise met. That report is the
format's proof that the grade cannot be sweetened.
