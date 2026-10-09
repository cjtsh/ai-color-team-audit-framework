# Safety Review Template — the plain-English layer

> This is a **section of the report**, not a separate document. Write it into
> `<repo>-colorteam-audit-report-<cycle>.md`, after the technical report. It is the second
> of the report's three sections; the findings ledger is the third.

Every audit produced under this framework has **two audiences**: the engineer who
must verify the evidence, and the person who must decide whether to trust the
software. The technical report serves the first. This template serves the second —
the spouse, trustee, lawyer, accountant, or manager asking one question: *is this
safe to use?*

Fill it in from the completed technical report. Every sentence must trace to a
finding or verified fact in that report — translate, never exceed. If a claim
cannot be supported by the technical report, it does not go in the safety review.

## Companion public statement — required (framework v1.5)

In addition to this full safety-review section, produce a standalone, one-page `<repo>-colorteam-security-statement-<cycle>.md` suitable for an official website. It is a **mandatory audited deliverable**, not a promotional claim. Use this structure: **What was reviewed** (exact version, source commit, named artifacts/hashes and date); **Who reviewed it** (actual AI models/tools, independence and human-review status); **What we checked** (money/authorization path, secrets, devices, dependencies, release integrity, as applicable); **What we found** (grade, material findings, unresolved limitations, release readiness); **What you should verify yourself** (official download and available hash/signature, on-device transaction details); **Read the evidence** (technical report and official release links). Say plainly when a control, binary, or device was not checked. Include the statement below in meaning, not necessarily verbatim:

> This review was carried out using AI agents and the tools identified in the audit record. We made a good-faith effort to examine the stated security risks and document what we found. An audit can reduce uncertainty, but cannot guarantee that software contains no bugs, malware, or vulnerabilities. Please review the findings and verify the official download and transaction details before using it. Trust, but verify.

Never imply a human audit firm or independent certification; do not use 'superintelligence,' 'best available,' '100% safe,' 'approved,' or 'cannot be hacked' without evidence that supports the specific assertion. A BLOCKED result is prominent, not softened. White checks the standalone statement against the technical report before publication.

------

# [Product] — Plain-English Safety Review

**[Product] [version] · [date] · reviewed by [auditor]**

## [VERDICT BOX: CLEARED / CONDITIONAL / BLOCKED — the grade carried over from the technical report / what it means in one line]

This review was written for [the person this software is actually for]. Every
statement here is drawn from — and can be checked against — [N] full technical
reviews completed [dates] by [auditor]. The evidence is public; the last page
tells you where.

## The questions that matter

**Can this [software] [do the unforgivable thing — steal the money / leak the data / seize control]?**
[Answer in customer words, + the protection they can verify THEMSELVES without
trusting anyone. One paragraph.]

**Could it [leak the unspeakable thing]?** [Answer + the concrete reason.]

**Could someone [act invisibly — change behavior without the owner seeing]?** [Answer + how tampering was tested and rejected.]

**What does the grade mean — and not mean?** [Locked rules; NOT a guarantee;
covers THIS version only; your own eyes still matter — name the one thing the
reader must always do themselves.]

## How this review was done

[2-3 sentences: several independent reviews, rules locked before anyone looked
at the code, the grade is the lowest score on the team.]

## The review team

Six independent examiners, each with one job, none seeing the others' work until
the end; the final grade is the *lowest* score on the team.

| Examiner | Their one job | In this review |
|---|---|---|
| [RED · The attacker] | [plain-language job] | [one-line result] |
| [BLUE · The defender] | … | … |
| [ORANGE · The logic specialist] | … | … |
| [COPPER · The edge specialist] | … | … |
| [AMBER · The supply inspector] | … | … |
| [WHITE · The referee] | [distrust everyone; the referee computes the grade and gates publication] | [result] |

## The audit trail

**Read this first:** [the defusing sentence — e.g., "across all reviews, no way
was ever found to [do the unforgivable thing]. The items below are about
manufacturing discipline and safety margins."]

| How serious | What it was, and what happened | Evidence |
|---|---|---|
| [DANGER SIGN] | [if any — else state "None found — in any review."] | [report ref] |
| [IMPORTANT TO FIX — RESOLVED] | [plain story: what it was, why it matters, what was done] | [report ref] |
| [MINOR IMPROVEMENT] | … | … |
| [HOUSEKEEPING] | … | … |

Severity badges for lay readers (translate, never soften and never scare):
- **DANGER SIGN** — could put [the assets] at risk. *State plainly if none were found.*
- **IMPORTANT TO FIX** — a weakness in how the software is built or released, not in what it does when used.
- **MINOR IMPROVEMENT** — extra safety margin; nothing a user could be harmed by.
- **HOUSEKEEPING** — notes for the maintainers.

Rules for the trail: lead with the reassurance that is TRUE (never inflate);
every row ends with a pointer into the technical report; improvements the team
made voluntarily (e.g., taking ownership of unchecked dependencies) are told as
the pride items they are.

## What this review does not cover

[Version-locked; what wasn't tested (hardware? live systems?); AI-panel honesty
("complements, does not replace, a qualified human firm"); "nothing found" means
"within this coverage."]

## Check our homework

[Table: the technical reports + where they live + the framework repo. One line:
"you can read every page of the evidence yourself."]

---

*Prepared [date] by [auditor] from the public reviews of [versions]. Every
statement above traces to those reports. A safety review is evidence about one
version on one day — not a guarantee.*

## Why this template exists

The first plain-English safety review written under this framework (Bitcoin
Easy Signer, October 2026 — see EXAMPLES.md) was produced after the owner
observed that the technical report, however excellent, answered nobody's actual
question. The audience layers are now part of the method: technical report for
the experts, safety review for the decision-maker, ledger for the agents.
