# AI Color Team Audit Framework

**The new standard for software audits using agentic tools.**

Version 0.2.1 · MIT License

Maintained by **Bitseeker LLC**.

Five specialist AI agents and a White referee independently audit your software —
with a grade rubric locked in writing **before** the audit begins, applied
mechanically after, and a publication gate nothing unfair survives. The whole
method ships as a drop-in agent file: paste it into any AI coding tool and run.

| | |
|---|---|
| 🔴 Red | The attacker — tries to seize, destroy, or alter the declared assets (credentials, personal or payment data, funds, control, availability — whatever your software must protect), by any path. Reads no prior conclusions, so it inherits no one's blind spots. |
| 🔵 Blue | The defender — proves every stated protection holds and is pinned by a test that fails if anyone breaks it. |
| 🟠 Orange | The critical-logic specialist — the logic a wrong byte breaks irrecoverably: cryptographic math, money and authorization arithmetic, session semantics — including what changed in every dependency since the last audit. |
| 🟤 Copper | The edge specialist — everything between the software and the edges of the system: browsers and clients, devices and drivers, transports and frozen binaries. |
| 🟡 Amber | The supply-chain inspector — how the artifact is born: every dependency, build step, signature and download in the chain. |
| ⚪ White | The referee — sees everything, re-derives every load-bearing claim personally, and gates what gets published. |

The audit is parameterized by a **survey** you confirm before anyone looks at
the code. Its **Asset Declaration** is the crown jewels, ranked: what must not
be stolen, destroyed, altered, or done without authorization. A wallet declares
funds, keys, and the operator's decision. A web service declares credentials,
personal and payment data, and session control. An embedded controller declares
safety and availability. Every charter reads from that declaration. |

The lanes adapt to your stack (a web app's Orange might be auth and session logic;
its Copper might be the browser and mobile clients). The colors — and the rules —
are the standard.

## The four rules that make it honest

1. **The rubric is locked before the audit.** Green/Yellow/Red are defined in
   writing before any agent examines the build, and applied mechanically afterward.
   Ambiguity is never resolved in green's favor.
2. **The grade is the floor of the panel, never the average.** One bad finding
   fails the audit no matter how glowing the rest.
3. **The referee gates publication.** Nothing is published that one agent could
   not personally re-derive. False alarms and false clean bills of health are
   attacked with equal energy.
4. **The surveyor is never the auditor.** The survey is drafted by a
   *different* model than the one that runs the panel. The surveyor decides what
   is in scope: if one model sets the scope and then audits it, the same blind
   spot sits on both sides of the handoff, and the audit grades green on software
   nobody examined. Only one model available? Write `SURVEY.md` yourself.

## Quick start

1. **Survey:** give **[SURVEY-TEMPLATE.md](SURVEY-TEMPLATE.md)** plus your
   repository to an AI coding tool running a *different* model than the one that
   will run the audit — the *Surveyor*. It reads the code and drafts your survey:
   the crown jewels, ranked (the Asset Declaration), and the unforgivable acts in
   plain words. This separation is required, not a preference: the model that
   declares the scope must not be the model that audits it. Only one model
   available? Write `SURVEY.md` yourself from the template instead.
2. **Confirm:** read the draft, correct anything only you know, and save it as
   `SURVEY.md` in the repo. Five minutes — and the one human moment the
   framework insists on.
3. **Audit:** point **[AGENT.md](AGENT.md)** (in your AI coding tool, or dropped
   into the repo as an agents file) at the repository. The agent runs the
   phases: baseline → the five-agent wave → the referee → the graded report.
   Read **[PANEL-DESIGN.md](PANEL-DESIGN.md)** to see (or tailor) the charters
   and rubric; **[REPORT-TEMPLATE.md](REPORT-TEMPLATE.md)** shows what you get;
   **[templates/pdf/](templates/pdf/)** generates the typeset edition.

Requires an AI coding tool that can spawn parallel sub-agents. If yours runs only
one agent, run the colors sequentially in separate sessions — you lose structural
independence, so say so in the report's coverage section.

## What this is not

Not a guarantee, not a certification, and not a replacement for a qualified human
security engineer. An audit is evidence about one revision on one day; "no finding"
means "none found within the stated coverage." The framework's own first full run
graded its sponsor **Yellow** on a process finding with every green condition
otherwise met — that report is linked below, and it is the best evidence the grade
cannot be sweetened.

## Worked examples (real audits, real grades)

The framework was born in production: three audits of a real Bitcoin-inheritance
tool in one day, each carrying the grade its evidence supported. Full stories in
[EXAMPLES.md](EXAMPLES.md); the shape of the arc:

| Cycle | What happened | Grade |
|---|---|---|
| v0.6.2 | [Classic audit](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.2.md) — 25 findings, none critical, every remedy written down | findings → fix them |
| v0.6.3 | [First full Color Team run](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.3.md) — all 25 fixed and regression-pinned; one process gap remained | 🟡 Yellow |
| v0.6.4 | [The conversion run](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.4.md) — the release published itself through its own automated gates | 🟢 Green |

![A Green report produced by this framework — the grade page](examples/v0.6.4-grade.png)

*The grade page of the v0.6.4 report (typeset edition). Full PDF:
[bitcoineasysigner.com/audits/ZAI-Security-Audit-v0.6.4.pdf](https://bitcoineasysigner.com/audits/ZAI-Security-Audit-v0.6.4.pdf).*

- **[Bitcoin Easy Signer v0.6.2 — classic single-lead audit](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.2.md)**
  25 findings, none critical — including two library defects proven unreachable,
  and the supply-chain gap that became the next cycle's headline fix.
- **[Bitcoin Easy Signer v0.6.3 — the first full Color Team run](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.3.md)**
  All 22 actionable prior findings (of 25 total) verified fixed, no breach found, cryptography re-proven
  against official test vectors — graded **Yellow** because the release was
  published through a manual path that bypassed the project's own new automated
  gates. The grade, the reasoning, and the one-step path to green are all in the
  report. A [typeset PDF edition](https://cjtsh.github.io/bitcoin-easy-multisig-signer/audits/ZAI-Security-Audit-v0.6.3.pdf) is also published.

## Repository contents

| File | What it is |
|---|---|
| `AGENT.md` | **The product.** The complete drop-in runbook for any AI coding tool. |
| `SURVEY-TEMPLATE.md` | **The one file you fill in.** The survey: your crown jewels, ranked, and the unforgivable acts — the audit's single input, consumed in Phase 0. |
| `COLOR-TEAM.md` | The color definitions, versioned (v1.1) — reproducible in any report using the format. |
| `PANEL-DESIGN.md` | Charters, phases, rubric, and the report shape; adapt to your target. |
| `REPORT-TEMPLATE.md` | The public technical report skeleton with the agentic appendix. |
| `SAFETY-REVIEW-TEMPLATE.md` | The plain-English layer: verdict, the four customer questions, the review team, and the audit trail with layman severity badges — every sentence traceable to the technical report. |
| `templates/publish-and-verify.sh` | The anti-"already done" tool: commit, push, poll, fetch, and hash-compare in one invocation. Nothing is published until it says VERIFIED. |
| `templates/pdf/` | A ReportLab generator for the typeset report edition. |
| `EXAMPLES.md` | The worked case studies. |
| `CHANGELOG.md` | Version history. |

## Contributing and versioning

The framework is versioned, and **every version reference stays in sync**: the
README version line, the PDF template's version stamp, and the changelog entry
all carry the current release version at every release. (`COLOR-TEAM.md`'s
definitions version — currently v1.1 — is deliberately independent: it changes
only when the role definitions change, so published reports stay citable against
the version they were written under.)

**Release checklist** (in order): update the change → `CHANGELOG.md` entry →
README version line → PDF template version stamp → commit → tag → release.
A version line that lags the tags is a documentation-mismatch finding in any
Color Team report — hold this repo to its own standard.

Propose changes by issue or pull request. If your team runs a Color Team audit —
whatever the grade — you are invited to link it in EXAMPLES.md as evidence.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, ship safer software.
