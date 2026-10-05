# The Color Team — definitions (v1.8)

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

**The panel's scope is the repository.** Every agent works on the repository, what it
ships, and its declared dependencies — the software, not the machine it runs on. A
missing firewall, an unpatched operating system, a careless owner, or a third party's
own flaws are outside the artifact and are not findings. **The hop rule:** every hop of
any claimed path must be inside that boundary, and a chain that needs a hop outside is
recorded as an exclusion, with the missing hop named.

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

**Scope.** Red attacks *the software*, not the machine it runs on — the boundary is
the panel's, above. Red is the only color that attacks, so it is the only one that
builds paths, and the only one where a hop outside the boundary can look like a
breach. Record such a path as an exclusion with the missing hop named: neither a
breach nor a finding.

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

**Role:** defense. Instead of attacking, audit the armor. For every protection the
software claims about itself — authentication, authorization and session handling,
input validation, transaction or workflow integrity, secret handling, fail-closed
behavior — prove it holds, and prove it still holds after the next change. An
unfixed control and an untested one both count as gaps. So does a control that should
exist: check the audit plan's declared assets against the claims, and report a
required protection that nothing claims.

**Claims first.** Blue's list is not invented; it is every protection the artifact
claims about itself — in its README, docs, comments, docstrings, configuration, and
the audit plan. Publish the inventory. A claimed protection that is not on it is
itself a finding.

**The five tests.** Every control in the inventory is judged against all five:

1. **Present** — the code that enforces it exists; file and line named.
2. **Reachable where it matters** — it runs on every path that touches the asset it
   protects, not just the happy path.
3. **Effective** — it stops what it claims to stop. *"Validation exists"* is not the
   claim; *"validation rejects X"* is.
4. **Fail-closed** — when it errors, it denies. A control that fails open protects
   nothing.
5. **Pinned** — a test exists, and Blue has watched that test fail when the control
   was broken. See below.

**Break-and-watch — the demonstrated standard.** *A test that exists is not
evidence; a test that can fail is.* Blue breaks the control in a **disposable local
copy**, runs the suite, watches the result, and reverts. Only a red test is a pass:

- **The test goes red** — pinned.
- **The test stays green** — the finding is *a control claimed to be tested that
  cannot fail*.
- **The suite cannot run** (no build, no dependencies, unsupported platform) —
  *unpinned, not demonstrated*. A gap, never a pass.

**Method:** control-by-control verification, operating-effectiveness testing, hunting
the missing test that would let a protection quietly rot. If a remediation work order
exists, verify every item against its acceptance criteria.

**Output:** the claims inventory, then a control-by-control table — control, where it
is claimed, where it is enforced, the test that pins it, the break-and-watch result —
then the fix ledger.

**Sub-verdict:** **DEFENSES HOLD** / **DEFENSES HOLD WITH GAPS** / **DEFENSE
BROKEN** — computed, never chosen. Any control failing tests 1–4 makes it DEFENSE
BROKEN; all controls passing 1–4 with some failing test 5 makes it DEFENSES HOLD
WITH GAPS; all five on every control makes it DEFENSES HOLD. The sub-verdict is set by the
worst control on the table, never by the average.

## 🟠 ORANGE — the critical-logic specialist

**Role:** the logic that enforces a named invariant — a statement of the form *"this
must always be true."* Every signature verifies. Amounts sum. A nonce never repeats. A
session cannot be replayed. The balance never goes negative. An authorization decision
cannot be bypassed by a crafted role. Where a wrong answer is silent and irrecoverable,
Orange owns it — for a payments system: signatures, derivation, address encoding,
transaction semantics, amount arithmetic; for a web service: authentication and token
logic, session semantics, authorization math, cryptographic usage; for a data platform:
query semantics and privilege evaluation. Orange also owns the critical dependencies
line by line, because an upgrade that fixes old bugs can quietly change behavior the
software depends on.

**Invariants first.** Orange publishes the invariant list before testing: every "must
always be true" the software relies on, and where each one is enforced. A critical path
with no written invariant is itself a finding — if nobody ever said what correct means,
nobody can say the code is correct.

**The oracle rule — the demonstrated standard.** Every invariant is established against
a definition of correct that lives **outside this implementation**. Acceptable oracles,
best first: the specification or standard (RFC, BIP, NIST/FIPS, the protocol contract);
official test vectors published with it; an independent reference implementation;
published analysis; or the mathematics, written out and shown. The code's own comments,
its own docs, its own tests, and "it looks right" are **not** oracles — an
implementation and a comment generated by the same model come from the same source, so
they cannot corroborate each other.

Every invariant is then judged on all five:

1. **Stated** — a definition of correct exists outside this implementation. Name it.
2. **Derived independently** — Orange writes down what the correct output is *before*
   reading the implementation. An expectation written after reading the code is not
   independent.
3. **Matched by execution** — the code is run against the official vector, the value
   computed from the oracle, or a constructed case whose expected result was derived
   first. Reading the implementation and agreeing with it is not a test.
4. **Boundary-covered** — exercised at zero, one, negative, maximum,
   exactly-at-limit, just-over-limit, empty, duplicate, replayed, out-of-order, and
   non-canonical encodings, wherever each case can occur.
5. **Pinned** — a test enforces it, and Orange has watched that test fail when the
   logic was broken. *A test that exists is not evidence; a test that can fail is.*

**The seam with Red and Blue.** Three colors touch authorization, and only the question
separates them. Red asks whether the gate can be got through. Blue asks whether the gate
is present, enforced on every path, effective, fail-closed, and pinned. Orange asks
whether the gate computes the right answer. Red reaches the code through the real entry
points; Orange calls the critical logic directly with constructed values.

**The dependency delta.** For every critical dependency: the version pinned, what
changed since the last audited version, and whether that change touches a named
invariant. **Read the diff — the changelog is a claim, not evidence.** If there was no
previous audit, say so: the delta is unavailable, and this is a full-scope review, not a
delta review.

**Method:** line-by-line review of the critical path, independent re-derivation, vector
and boundary execution, reachability analysis for every defect found.

**Output:** the invariant list; a delta table for the critical dependencies; a
vector-and-boundary results table; and every defect marked reachable or not reachable in
this software.

**Sub-verdict:** **LOGIC PROVEN** / **LOGIC UNPROVEN** / **LOGIC WRONG** — computed,
never chosen, and itemized per invariant. Any invariant the oracle shows the code
violating makes it LOGIC WRONG. Any invariant that cannot be established — no
independent statement of correct, an oracle that could not be matched to execution, or a
match with nothing pinning it — makes it LOGIC UNPROVEN, and the report must say which
of those three it was. Every invariant stated, derived independently, matched by
execution, boundary-covered, and pinned makes it LOGIC PROVEN. One wrong or unproven
invariant fails the whole sub-verdict; the rest do not offset it.

## 🟤 COPPER — the edge specialist

**Role:** the boundary layer — everything the core **trusts but does not control**.
Not "the parts outside the repository": what the core depends on and cannot see,
verify, or replace. Clients (browser, native, mobile), transports and whatever
answers at the other end, devices and their drivers, the host runtime surface the
software leans on, and frozen or adopted binaries shipped but not built here.

**Applicability first.** Copper's universe comes from the audit plan's declared
assets: for each one, does the core trust it without controlling it? If that is false
everywhere, Copper reports **NOT APPLICABLE** — with the reason and what it examined
to reach that conclusion — in the coverage section, never as a clean verdict. A lane
with no subject contributes nothing to the grade, and the report must show that it
contributed nothing. "Edges sound" is not an available answer to an empty lane.

**Every edge is assumed hostile or broken.** Copper is not auditing the browser or
the device; it is auditing what the core does when its edge betrays it. Five
behaviours, at every interface:

1. **Lies** — returns a value the core did not earn: forged, downgraded, out of range,
   wrong type, or from a different party than the core believes.
2. **Dies** — disconnects, closes, or returns nothing mid-operation.
3. **Stalls** — hangs, or answers arbitrarily slowly.
4. **Repeats** — replays a previously valid message, or delivers it out of order.
5. **Is substituted** — a different implementation is in its place: a counterfeit
   device, a patched client, an older binary, a swapped library.

The core passes an interface only if it survives all five.

**Version identity.** For every edge: how does the core know *which* version, vendor,
or build it is talking to — and can it tell at all? If it cannot, that is the
counterfeit finding, and it is a first-class result, never a footnote.

**Evidence, or it did not happen.** Every edge Copper names carries the exact artifact
— path, binary hash, version string, wire format — and the exact observation:
disassembly address, loader resolution, constructed message, captured traffic, or the
test that shows it. "Reviewed the client" is not an observation. Where there is no
source to read — a frozen binary, a device, a third-party service — Copper gives the
hash and the tool and **states plainly what it could not establish**. The shared
evidence standard applies unchanged: a test that exists is not evidence; a test that
can fail is. Runtime verification where it can be obtained; where it cannot, say so
rather than imply it. Copper never runs against production or real user data.

**Method:** boundary code review, binary inspection with hashes and addresses,
loader-resolution experiments, adversarial interface construction, runtime
verification on disposable machines where possible.

**Output:** the applicability finding; then, per edge interface, the artifact
examined, the outcomes of the five behaviours, and the version-identity result; then
the fix ledger.

**Sub-verdict:** **EDGE TRUST HOLDS** / **EDGE TRUST UNPROVEN** / **EDGE TRUST
BROKEN** — computed, never chosen, and itemized per interface. The core can be
deceived, hung, or corrupted at a named interface → EDGE TRUST BROKEN. An interface
that could not be established — no evidence of what the edge does, no version
identity, no runtime verification where one was needed, or nothing pinning the
behaviour → EDGE TRUST UNPROVEN. Every interface surviving all five behaviours, with
evidence, and pinned → EDGE TRUST HOLDS. One broken interface fails the whole
sub-verdict; four clean interfaces do not offset it. **NOT APPLICABLE is not a
sub-verdict** — it is a coverage statement.

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
   handled, uncertainty is a result, and the report says what was not examined. A
   **disposable local copy** is not the target — running the suite there, or
   breaking a control there and reverting it, is verification, not a side effect.

---

*Color Team definitions v1.7 — part of the AI Color Team Audit Framework (this
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
itemized per declared asset. v1.5 states that scope — the repository and its
declared dependencies, not the machine it runs on — once, in the preamble, where
all six colors read it, and leaves Red only the attack-specific consequences. v1.6
gives Blue a fixed five-test standard — present, reachable where it matters,
effective, fail-closed, pinned — makes break-and-watch the demonstrated standard
for any control claimed to be tested, and computes Blue's sub-verdict from those
tests instead of leaving it to taste. v1.7 gives Orange the same treatment: an
invariant list published before testing, the oracle rule — correctness established
from outside the implementation, because a model's code and a model's comments
cannot corroborate each other — and a computed verdict of LOGIC PROVEN / LOGIC
UNPROVEN / LOGIC WRONG. v1.8 gives Copper the same treatment: the edge is everything
the core trusts but does not control, NOT APPLICABLE is a real answer instead of a
clean bill of health, every edge is assumed hostile or broken across five behaviours,
evidence means a named artifact and a named observation, and the verdict is EDGE
TRUST HOLDS / EDGE TRUST UNPROVEN / EDGE TRUST BROKEN. The outcomes, the rubric, and
the floor rule are all unchanged; reports published before v1.2 used the old grade
names. Red and blue are established security-industry terms; orange, copper, amber,
and white were
introduced by the framework's first runs (Bitcoin Easy Signer audits, October 2026).
This page may be reproduced in any report that uses the format; reproduce it whole
and cite the version.*
