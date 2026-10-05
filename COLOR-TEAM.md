# The Color Team — definitions (v1.4)

A security review performed by a named panel of specialist agents, each with one
lens and one job. Two of the colors are borrowed from established security
vocabulary — **red** (attackers) and **blue** (defenders) are industry terms. The
other three lenses and the referee are this framework's extensions, chosen so every
major way software can fail has exactly one agent whose whole job is to look for
it. Together: **five specialists and a referee.**

The panel is parameterized by one input supplied before the audit begins: the
**Asset Declaration** — the target's crown jewels, in order of value (see
`PANEL-DESIGN.md`). Every definition below reads "the declared assets" wherever the
founding runs said "funds and keys."

**This page is the standard.** These six definitions — role, method, output, and
sub-verdict — are what a Color Team audit *is*. The lanes adapt to the target (a web
service's Orange is not a wallet's Orange); the colors never do. An audit that
rewrites what a color hunts is not a Color Team audit, and must not cite this page.

| Color | Agent | In one sentence |
|---|---|---|
| 🔴 Red | The attacker | Tries to seize, destroy, or alter the declared assets — credentials, personal or payment data, funds, control, availability, whatever was declared — by any path. |
| 🔵 Blue | The defender | Proves every stated protection actually holds and is pinned by a test that fails if anyone breaks it. |
| 🟠 Orange | The critical-logic specialist | Checks the logic the software cannot afford to get wrong — cryptographic math, money and authorization arithmetic, session semantics — including what changed in every dependency since the last audit. |
| 🟤 Copper | The edge specialist | Checks everything between the software and the edges of the system — clients and browsers, devices and drivers, transports and frozen binaries. |
| 🟡 Amber | The supply-chain inspector | Checks how the artifact is born — every dependency, build step, signature, and download in the chain. |
| ⚪ White | The referee | Sees everything, re-verifies every load-bearing claim personally, and gates what gets published. |

---

## 🔴 RED — the attacker

**Scope.** The repository, everything it ships, and every declared dependency. Red
attacks *the software*, not the machine it runs on. A missing firewall, an unpatched
operating system, a careless owner, or a third party's own flaws are not findings —
they are outside the artifact.

**The hop rule.** Every hop of a Red path must be inside the repository or a declared
dependency. A path that needs a hop outside is out of scope: record it as an
exclusion, with the missing hop named. It is neither a breach nor a finding.

**Role:** offense. Given the software and a hostile world — malicious inputs,
counterfeit clients and devices, hostile configuration and files, untrusted local
processes, compromised dependencies, lying network services — find any path to the
declared assets. Work the whole attack taxonomy — injection of every kind (SQL,
command, path, template, deserialization), authentication bypass, privilege
escalation, logic abuse, race conditions, spoofing, and memory-safety where the stack
exposes it — against the enumerated surface, never as a checklist. The taxonomy
says how to attack; the surface says what to attack; the hop rule says where to stop.

**Win conditions.** Red wins by demonstrating any one of these against a declared
asset:

1. **Read it** — secret material the software holds reaches someone who should not
   have it.
2. **Change it** — data or state is altered without authorization.
3. **Destroy it** — data or availability is lost.
4. **Act as the owner** — the software does something on their behalf that they did
   not authorize.
5. **Escape the process** — code runs with more authority than the software should
   have.

The declaration names the assets. These five say what winning means.

**Surface first.** Before attacking, Red enumerates every input the artifact accepts
and every trust boundary it crosses, and puts the list in the report. An input that
exists and is not on that list is itself a finding.

**Demonstrated means** an exact path: from an input Red can supply, to a named
declared asset, with the code at every hop, and no hop outside the repository. A
plausible chain Red could not close is logged as an attempt with its missing hop
named. It is not a breach, and it does not fill the verdict.

**Method:** adversarial code reading, hostile-input construction, attack-path
tracing, abuse of every input the software accepts. Attack the newest code hardest:
fixes are changes, and changes are where new holes live. Red attacks the repository's
*use* of a dependency — the wrong call, the unvalidated argument, the trusted return
value. A dependency's own known-bad version is Amber's lane; what changed inside it
is Orange's.

**Deliberately does not read** prior audit conclusions, so it cannot inherit the
lead auditor's blind spots.

**Output:** the surface enumeration, then an attack log in which every attempt's
outcome is one of *demonstrated*, *not demonstrated*, *blocked by a control*, or *out
of scope*; then findings.

**Sub-verdict:** **BREACH DEMONSTRATED** / **NO BREACH DEMONSTRATED** — stated once
for the audit and itemized per declared asset, so the owner sees which crown jewel
fell and which held. One breach fails the whole sub-verdict; five clean assets do not
offset it.

## 🔵 BLUE — the defender

**Role:** defense. Instead of attacking, audit the armor. Enumerate the software's
stated protections — whatever the Asset Declaration implies must hold:
authentication, authorization and session handling, input validation, transaction
or workflow integrity, secret handling, fail-closed behavior — and for each, prove
it holds end-to-end in code, and prove a regression test pins it, so no future
change can silently break it. An unfixed control and an untested one both count as
gaps.

**Method:** control-by-control verification, test-coverage analysis, hunting the
missing test that would let a protection quietly rot. If a remediation work order
exists, verify every item against its acceptance criteria.

**Output:** a control-by-control table, then the fix ledger.

**Sub-verdict:** *Defenses hold* / *Defenses hold with gaps* / *Defense broken*.

## 🟠 ORANGE — the critical-logic specialist

**Role:** the logic a wrong byte breaks irrecoverably. For a payments wallet that
is signatures, derivation, address encoding, transaction semantics, amount
arithmetic. For a web service it is authentication and token logic, session
semantics, authorization math, cryptographic usage. For a data platform it is query
semantics and privilege evaluation. For all of them it is the critical dependencies
line by line — including a diff against the last-audited version, because an upgrade
that fixes old bugs can quietly change behavior the software depends on.

**Method:** line-by-line review of the critical path, validation against official
test vectors and standards where they exist, reachability analysis for every defect
found.

**Output:** delta tables and vector results; every defect marked reachable or not
reachable in this software.

**Sub-verdict:** *Critical logic sound as used* / *Defects found*.

## 🟤 COPPER — the edge specialist

**Role:** the boundary layer. Everything between the core software and the outside
world, chosen by the Asset Declaration: browser and native clients, mobile and
desktop runtimes, hardware devices and their drivers and transports, embedded and
frozen binaries — and the counterfeit-component question for each (can a fake edge
device or client deceive the core?).

**Method:** boundary code review, binary inspection, loader-resolution experiments,
runtime verification on real machines where possible.

**Output:** edge findings with runtime evidence where it could be obtained.

**Sub-verdict:** *Edges sound* / *Gaps found*.

## 🟡 AMBER — the supply-chain inspector

**Role:** how the artifact is born. Every dependency and its lock (hash-pinned
end-to-end or not), the CI pipeline's step order and secret handling, build scripts,
code signing and notarization verified on the actual published artifact, the
software bill of materials, and the guards that keep a published version immutable.
The standing question: could compromised upstream code reach a released build
without a deliberate, reviewable version bump?

**Method:** workflow and lock-file audit, artifact re-hashing, signature and
platform verification, tamper-path analysis.

**Output:** claim-by-claim verification and a residual-risk inventory.

**Sub-verdict:** *Chain holds* / *Chain gaps*.

## ⚪ WHITE — the referee

**Role:** verification. Not a perspective — the gate. Re-derives every load-bearing
claim the other five made: reads the same code, runs the same commands, quotes what
is actually there. Attacks false alarms and false clean bills of health with equal
energy. Nothing is published that White could not verify.

**Method:** personal re-derivation of every load-bearing claim; merging the
specialists' colliding finding IDs into one ledger; applying the rubric
mechanically; listing the facts the public report must carry.

**Output:** a claim-by-claim verdict table, a calibration opinion, and the
publication decision: *Publish / Publish with edits / Do not publish.*

---

## What the panel is, and is not

Because the definitions are parameterized by the Asset Declaration, the same color
hunts different things on different targets. Declare "data integrity and privilege
boundaries" and Red's job becomes exactly the classic injection-to-extraction hunt
(unsanitized query construction → extraction or escalation), Blue's becomes
parameterization and least-privilege controls plus the regression tests pinning
them, and Orange's becomes the auth and session logic.

Agent audits read code adversarially and run the target's own tests. They
complement — and do not replace — fuzzers and dynamic scanners. A thorough target
runs both, and says so in the coverage section.

## How the grades combine

Each agent's sub-verdict prints in the report under its own name and color. The
overall grade — CLEARED / CONDITIONAL / BLOCKED — is defined in writing **before**
the audit begins (see `PANEL-DESIGN.md`), and is the **floor** of the panel, never
the average: a single BLOCKED-grade finding fails the review no matter how strong
the other sections are.

## The rules that make it honest

1. The Asset Declaration, the six definitions on this page, and the grade
   definitions are written before the build is examined and do not change
   afterward.
2. The five specialists work independently and do not see each other's findings
   until the panel merge; the referee sees everything.
3. Every finding carries a stable ID, exact file and line, evidence, and a
   suggested remedy — nothing is asserted without proof attached.
4. The panel format is presentation; the evidence standard is unchanged whatever
   the target: read-only auditing, no production side effects, no real secrets
   handled, uncertainty is a result, and the report says what was not examined.

---

*Color Team definitions v1.4 — part of the AI Color Team Audit Framework (this
repository). v1.1 generalizes the founding wording (written for a Bitcoin wallet)
to the Asset Declaration model; role semantics are unchanged from v1. v1.2 renames
the report grades from Green/Yellow/Red to **CLEARED / CONDITIONAL / BLOCKED**,
because the old names reused two of the panel's own colors — 🔴 meant both "Red,
the attacker" and "the worst grade." v1.3 makes this page the single home of the six
agent definitions, which had been written out twice — here, and again as "charter
sketches" in PANEL-DESIGN.md — and says outright that the definitions themselves are
the standard, not a starting point. v1.4 tightens Red: the audit attacks the software
and not the machine it runs on, the hop rule makes the repository boundary explicit,
the five win conditions are named, demonstration is defined, and Red's verdict is
itemized per declared asset. The outcomes, the rubric, and the floor rule are
all unchanged; reports published before v1.2 used the old grade names. Red and blue
are established security-industry terms; orange, copper, amber, and white were
introduced by the framework's first runs (Bitcoin Easy Signer audits, October 2026).
This page may be reproduced in any report that uses the format; reproduce it whole
and cite the version.*
