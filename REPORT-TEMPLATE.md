# Report Template — public technical report (Color Team)

> This is the engineer/expert layer. The decision-maker layer is
> `SAFETY-REVIEW-TEMPLATE.md` — write both; each audience reads only its own.

Replace bracketed values. Keep the structure and the honesty; the format is part of
the standard. Delete any section that genuinely has no content — never invent any.

---

# [Auditor] Security Audit — [Product] [version] — The Color Team Report

| | |
|---|---|
| **Version examined** | Tag `[tag]`, commit `[full SHA]`, published [date] |
| **Assets declared** | [The crown jewels this audit protected, ranked — e.g., user credentials, personal and payment data, session control; or funds, key material, operator approval] |
| **Auditor** | [Who] — a five-specialist Color Team panel plus a referee; asset declaration, charters and grade rules locked in writing **before** the build was examined |
| **Prior audit** | [Prior cycle summary, or "first audit"] |
| **Verification** | [What was independently re-derived: artifact hashes, signatures/notarization, test suites re-run, etc.] |
| **Scope lock** | Plan `[<repo>-colorteam-audit-plan.md]`, SHA-256 `[H_start]` before the first agent ran and `[H_end]` at the end — [equal: the scope never moved / **MISMATCH: the audit is void and this report must not be published**]. Owner-signed [name, date]. [Hash published before the panel ran at [where] / order not witnessed.] |

## The grade: [✅ CLEARED / ⚠️ CONDITIONAL / ⛔ BLOCKED] — [one-line reason]

[If not CLEARED: the finding(s) holding the grade, stated plainly with severity and
the exact path to CLEARED. If CLEARED: what was verified to earn it. The rubric tension
rule applies: if any clause of the rubric could be read to bind, it binds.]

## The four questions that matter

(Parameterized by the Asset Declaration — ask them about the declared assets.)

1. Could this software [do the unforgivable thing to the declared assets — seize,
   destroy, or alter them, or act without authorization]? — **[verdict + evidence]**
2. Could it [leak the unspeakable thing — the declared secrets / personal data /
   credentials]? — **[verdict]**
3. Could a remote party, a dependency, or a local process [act invisibly — alter
   behavior or data without the operator seeing it]? — **[verdict]**
4. What should be fixed first? — **[answer]**

## The prior audit's findings: [status summary]

[Fix ledger: every prior-cycle finding → verified fixed / partially / open, with
evidence and which tests pin each fix.]

## The panel

**🔴 Red — [sub-verdict].** [2–4 sentences: what was attacked, what held, residuals with bounds.]
**🔵 Blue — [sub-verdict].** [The claims inventory; for each control, present /
reachable / effective / fail-closed, and what the break-and-watch showed. Name what is
unpinned.]
**🟠 Orange — [sub-verdict].** [The invariant list; for each: the oracle, the
independently-derived expectation, and the execution result — plus the dependency deltas
and the maintenance obligations created.]
**🟤 Copper — [sub-verdict], or NOT APPLICABLE with the reason.** [Per edge
interface: the artifact examined, the outcomes of the five behaviours it was assumed
to exhibit, and the version-identity result.]
**🟡 Amber — [sub-verdict], or NOT APPLICABLE with the reason.** [The chain
inventory; per link: named / pinned / real / read / matched, with the evidence, and
anything marked UNVERIFIED — plus the residual-risk inventory.]
**⚪ White — [PUBLISH / PUBLISH WITH STATED GAPS / DO NOT PUBLISH].** [What was
re-derived and held, what was corrected, what stayed unverifiable, the computed grade
with the lane that set the floor, any dissent, and the mandatory facts.]

## What this audit did not do

[No hardware? No live network? Never-executed paths? State it. "No finding" means
"none found within this coverage," not "none exist."]

## Appendix — findings ledger

[Prior-cycle IDs → status at this commit. New findings: final IDs (fixed by the
referee after the specialists' independent counts collided), severity, one-line
claim each, exact locations where publishable.]

---

*[Audit date, auditor, scope disclaimer: performed on the public repository and
published artifacts only; the grade rules were locked before the audit began and
applied as written; no [sensitive material] appears in this report; an audit is not
a certification of safety; coverage limits stated above.]*
