# Changelog

## 1.1.7 — 2026-10-05

### The quick start moved above the fold

It was the second-to-last section of the README, which is where a quick start goes to die.
It now sits directly after *What you get at the end* and immediately before *The panel* —
what you receive, how to get it, then what does the work. Each of the four steps is its own
visual block, separated by a horizontal rule.

- Quick start moved from below *The four rules* to above *The panel*.
- The four steps no longer run together as consecutive paragraphs.
- The two copy-paste prompts point at this tag.

No definitions changed — `COLOR-TEAM.md` stays v2.2.

## 1.1.6 — 2026-10-05

### The quick start you can actually follow

The quick start was four paragraphs of prose with one quoted sentence in the middle of
them. It is now two prompts you paste as they are — the runbook's URL at a pinned tag, and
one line of instruction — plus the two steps a human does. Nothing in either block needs
editing.

- The runbooks are handed over by **tagged URL** instead of a file copied into your
  repository. An attachment still works; a `main` URL does not, because the report has to
  name which version of the definitions was in force.
- The README head now says the two things apart, which it never did: the *runbooks* are
  never copied into your repository, and the framework's *artifacts* — the plan, the scope
  lock, and the report — are written into its root.

No definitions changed — `COLOR-TEAM.md` stays v2.2.

## 1.1.5 — 2026-10-05

### One report, and a timestamp if you want one

The 1.1.3 revert left one line behind: the README still promised "a grade, and three
documents." It is a grade and **one report**, carrying three sections.

The lock's honest limit now names its own remedy. Two hashes prove the scope did not move,
but not when it was written, because one operator holds both. If you want a timestamp no
one can rewrite — including the operator — a public blockchain will hold the plan's hash
before the run, or the report's hash after, memorialised with a time that depends on no
one's word. The framework does not build this and does not need it; it is there for anyone
who wants the order of events provable to a third party.

No definitions changed — `COLOR-TEAM.md` stays v2.2.

## 1.1.4 — 2026-10-05

### The rubric's authority catches up with the rubric

`PANEL-DESIGN.md` → *The rubric* is the document the runbook defers to, and it was the one
copy still carrying the pre-Blue wording: CLEARED was "stated defenses held and
regression-tested", CONDITIONAL had no cap clause, and BLOCKED named only open
Critical/High. The README and the operator's checklist had both moved on; the authority
they point at had not.

The three grades now match the seven rulings below them, so the runbook's "if the two ever
disagree, `PANEL-DESIGN.md` wins" resolves to the right answer. No definitions changed —
`COLOR-TEAM.md` stays v2.2.

## 1.1.3 — 2026-10-05

### One report, three sections

1.1.2 named the report and then split it in two, inventing a separate published document
called `<repo>-colorteam-audit-safety-review.md`. That was not the design and it is
reverted. The report was always **one file with three sections** — the technical report
for engineers, the safety review for everyone else, and the findings ledger for agents —
and it is `<repo>-colorteam-audit-report.md`.

`SAFETY-REVIEW-TEMPLATE.md` is a section template, not a document template. The naming
convention now covers the three artifacts that exist: the plan, the scope lock, and the
report. The owner's private full report — everything, verbatim evidence — is still never
published.

White's charter in `COLOR-TEAM.md` said the three sections were "assembled from the
technical report" and never said they land in one file, which is what let 1.1.2 read them
as three documents. The definitions now say so, and the footer and the README's version
reference follow: `COLOR-TEAM.md` moves to **v2.2**.

## 1.1.2 — 2026-10-05

### The report has a name, and it is step four

> **Superseded by 1.1.3.** The two-file split described below was wrong and has been
> reverted — the report is one file, `<repo>-colorteam-audit-report.md`, with three
> sections. The naming table here records what 1.1.2 shipped, not the current convention.

The flow diagram showed three steps and ended at "the graded report" — an unnamed
artifact, produced by a step that had already been counted. Step 3 now ends where the
audit actually ends: each lane's sub-verdict and the grade computed from them. Step 4 is
the report, and it is named.

Every artifact the framework writes now follows one convention,
`<repo>-colorteam-audit-<what>.md`:

| Artifact | Name |
|---|---|
| The audit plan | `<repo>-colorteam-audit-plan.md` |
| The scope lock | `<repo>-colorteam-audit-lock.md` |
| The technical report | `<repo>-colorteam-audit-report.md` |
| The safety review | `<repo>-colorteam-audit-safety-review.md` |
| The private full report | `<repo>-colorteam-audit-full-report.md` |

The findings ledger is not a sixth file: it is the Appendix of the technical report, so
there is one source of truth and nothing that can drift out of step with it.

`colorteam-surveyor.md` and `colorteam-auditor.md` now say four steps, and the README
naming paragraph no longer claims the plan is the only file that lands in your repo.

## 1.1.1 — 2026-10-05

### The runbooks catch up with the panel they run

`colorteam-auditor.md` carried its own copy of the grade rubric, and the copy stopped
being updated at v1.6. It knew about open Critical/High findings and nothing else: none of
the five automatic blocks from rulings 4, none of the CONDITIONAL cap from ruling 5, and
it never named a single color or cited `PANEL-DESIGN.md`. A Red breach demonstrated with
no Critical/High finding would have graded CLEARED or CONDITIONAL under the file the
operator actually executes. `PANEL-DESIGN.md` is now named as the authority, the runbook
keeps the operational checklist, and where the two disagree the authority wins.

Also in the auditor: the charters are the `COLOR-TEAM.md` definitions reproduced whole
rather than "suggested" sketches, which is the wording v1.3 retired; the hard rules grant
the **disposable local copy** that makes Blue's break-and-watch legal and stop
contradicting Phase 0's instruction to run the suite; the header names the framework files
the runbook needs instead of claiming the target repository is enough; and Phase 2 asks
for White's artifacts — the mechanical definition of load-bearing, the per-claim
CONFIRMED / CORRECTED / UNVERIFIABLE record, and the coverage section — rather than only
the verbs.

In `colorteam-surveyor.md`, the locked-scope block is now actually written out in full.
Sections 1 through 8 are working detail; section 0 is the frozen statement and governs if
they disagree. The block the owner signs now contains the asset table, the unforgivable
acts, the rubric, the revision, and the exclusion and gap lists, instead of three "repeat
section N" pointers.

No definitions changed; `COLOR-TEAM.md` stays v2.1.

## 1.1.0 — 2026-10-05

### The scope is frozen, and the lock has a fingerprint

Every audit already claimed its rubric and scope were locked before anyone looked at the
build. Nothing proved it. The plan could be narrowed after the fact — and a hash held only
by the person who could drift the scope proves nothing either.

The plan now opens with a **Locked-scope block** (section 0) written out in full — the
declared assets, the definitions in force, the rubric as adapted to this target, the exact
revision, and the exclusions — ending in a dated owner signature. Before the first
specialist is dispatched, the auditor takes the SHA-256 of that signed file and records it
in a companion `<repo>-colorteam-audit-lock.md`; the referee re-hashes the plan at the end
and appends the end hash.

Equal hashes mean the scope never moved. Unequal means the plan and the findings describe
different audits, and the audit is **void**: DO NOT PUBLISH, no grade, no partial credit
(`PANEL-DESIGN.md` ruling 7). The lock is never written into the plan itself, because that
would change the bytes it was taken over.

The owner is asked for nothing new: signing is the same sitting as reading the plan, and
the hashing is the agents' job. Publishing the hash before the panel runs — a commit, a
gist, an issue comment — stays optional, and closes the one gap two hashes cannot: they
show that the scope did not move, not when it was written relative to the findings.

Definitions in `COLOR-TEAM.md` move to **v2.1**; rule 1 now carries the lock.

## 1.0.1 — 2026-10-05

### The CONDITIONAL cap is tied to what actually ships

Ruling 5 said anything a lane leaves unproven holds the grade at ⚠️ CONDITIONAL. That is
right for what reaches users, and noisy for what cannot: a documentation-only dependency,
an example in its own directory, or a dev tool that never runs in the build would cap a
whole audit over something no user can be affected by. A grade that everything gets stops
carrying information.

The cap now applies when the unproven thing is **on the path to a declared asset**. A
thing that provably cannot reach one — with the exclusion demonstrated rather than
asserted — is recorded in the coverage section and does not cap.

What this does not soften: **an artifact whose build cannot be reproduced is on that path
by definition, and still caps.** If you cannot reproduce what you shipped, no one can tell
you what is in it, and "we could not check" is not "it is clean." CLEARED has to mean
verified, or it means nothing.

No definitions changed; `COLOR-TEAM.md` remains v2.0.

## 1.0.0 — 2026-10-05

### White gets a mechanical gate, and the panel is complete

White was the last lane to be treated, and it had the same three holes the other five had,
plus one of its own: "every load-bearing claim" was a scope White chose for itself, the
re-derivation left no record, and a "calibration opinion" let the referee decide the grade
— which quietly made the floor rule optional.

**"Load-bearing" is now mechanical.** A claim is load-bearing when it determined a
sub-verdict or the grade, and every one of those is re-derived. A lane that reported
nothing is making a claim too — *"I found nothing"* — and it is re-derived with the same
energy, because a false clean bill of health is more dangerous than a false alarm.

**Every re-derived claim is recorded** as **CONFIRMED**, **CORRECTED**, or
**UNVERIFIABLE**, with the file or command White used. Nothing is published on the
strength of an unverifiable claim: a finding that cannot be reproduced does not stand as a
finding, and a lane that cannot be reproduced does not stand as clean.

**White calibrates severities; White does not calibrate the grade.** The grade is computed
from the rubric and the rulings with the arithmetic shown — which lane set the floor,
which ruling bound it. The referee never raises or lowers a lane's sub-verdict, and a
disagreement is recorded as a dissent while the grade stands. A referee with discretion
over the floor has made the floor optional.

**The publication decision is computed too:** PUBLISH / PUBLISH WITH STATED GAPS / DO NOT
PUBLISH. The old middle state, "publish with edits," was a judgment call with no
conditions attached; each new state is defined by what is true of the work.

**White does not originate findings**, and now owns the coverage section and the facts the
published report must carry, plus the final finding numbering — kept stable across cycles.

**Ruling 6** was added: *the grade is computed, not calibrated.*

`COLOR-TEAM.md` is **v2.0**. All six definitions — five specialists and the referee — now
carry the same three things: a scope derived from the target instead of chosen by the
agent, a demonstrated-evidence rule, and an outcome computed from tests rather than
chosen. That is what the whole 0.x series was building toward, and why this is 1.0.0.

**Also settled here:** every lane's failure state forces a ⛔ BLOCKED (ruling 4), and
anything a lane leaves unproven holds the grade at ⚠️ CONDITIONAL (ruling 5) — including a
chain link that is UNVERIFIED. That last clause is the strictest rule in the framework:
software that cannot reproduce its own build cannot reach CLEARED. It is deliberate.

## 0.9.0 — 2026-10-05

### Amber gets a defined chain, and the fifth lane joins the merged ruling

Amber kept the panel's sharpest line — *a package that installs cleanly is not proof of
legitimacy, because that is exactly what an attacker-registered squatter provides* — but
it had the same three holes the other four lanes had. Its scope was self-chosen ("how the
artifact is born"), its methods were stated as tools rather than as evidence, and its
sub-verdict (*"Chain holds" / "Chain gaps"*) was a judgment call.

**The chain is now defined:** every step that turns source the owner wrote into an
artifact someone runs — dependencies and their transitive closure, the build and the
secrets it can see, packaging, signing, publication, and whether a published version can
change under you. The scope is derived from the target instead of chosen by the agent.

**The chain inventory is published before verification.** Every link with its exact
version and hash. An artifact that reaches a user through a step the inventory does not
list is itself a finding — and so is an empty inventory, which is a claim to check rather
than a clean result.

**Five questions at every link, all requiring evidence:** **Named** (it is on the
inventory), **Pinned** (a content hash, a fixed action or runner version, a base image
digest, a signed tag — "latest" is not a pin, and a version range is not a pin), **Real**
(the project it claims to be, at the version claimed, established from the registry
rather than from the import statement), **Read** (Amber inspected what it does at that
pinned version), and **Matched** (the published artifact re-downloaded and re-hashed
against the audited source).

**What cannot be verified is recorded, never assumed.** No lockfile, a dependency with no
readable source, a build that cannot be reproduced, a signature with no key: Amber writes
**UNVERIFIED** against that link and states what would close it.

**The verdict is computed:** CHAIN HOLDS / CHAIN UNVERIFIED / CHAIN BROKEN, itemized per
link, worst link wins. NOT APPLICABLE — nothing to build, nothing published — is a
coverage statement, not a verdict.

**The merged ruling absorbed Amber as one bullet**, which is what merging the rulings in
0.8.0 was for: Red, Blue, Orange, Copper and Amber all force a block when they prove
their own failure state, and that is now stated in one place instead of five.

**A seam note** separates Amber from Orange, since both read dependencies: identity,
provenance and integrity are Amber's question; arithmetic and semantics are Orange's.

`COLOR-TEAM.md` is v1.9. Amber is the fifth of the five specialists to get a fixed
standard and a computed verdict; only White, the referee, remains.

## 0.8.0 — 2026-10-05

### Copper gets a defined edge, and the rulings get merged

Copper had the mirror of Blue's problem, in the worst possible place. Its scope was
**self-chosen** — "the boundary layer" — so a repository with no browser, no device and
no frozen binary still received a clean **"Edges sound."** That is a review that never
happened, printed as reassurance, which is the exact failure this framework exists to
catch. The lane also stated its methods as tools ("binary inspection",
"loader-resolution experiments") rather than as evidence, and the question that matters
most to it — *can a fake edge device or client deceive the core?* — sat in a
parenthetical. The sub-verdict (*"Edges sound" / "Gaps found"*) was a judgment call.

**The edge is now defined:** everything the core trusts but does not control. Not "the
parts outside the repo" — what the core depends on and cannot see, verify, or replace.
That makes Copper's scope derived rather than chosen.

**NOT APPLICABLE is a real answer.** A lane with no subject reports it, with the reason,
in the coverage section. It contributes nothing to the grade, and the report must show
that it contributed nothing.

**Every edge is assumed hostile or broken:** it **lies** (returns a value the core did
not earn), **dies** (disconnects mid-operation), **stalls** (hangs or answers
arbitrarily slowly), **repeats** (replays or reorders), or **gets substituted**
(counterfeit device, patched client, older binary). The core passes an interface only
if it survives all five. Copper is not auditing the browser; it is auditing what the
core does when its edge betrays it.

**Version identity** is promoted from a parenthetical to a first-class check: how does
the core know which version, vendor, or build it is talking to, and can it tell at all?
If it cannot, that is the counterfeit finding.

**Evidence, or it did not happen.** Every edge carries a named artifact — path, binary
hash, version string, wire format — and a named observation. "Reviewed the client" is
not an observation. Where there is no source to read, Copper gives the hash and the tool
and states plainly what it could not establish. It reuses the shared standard rather
than restating it: a test that exists is not evidence; a test that can fail is.

**The verdict is computed:** EDGE TRUST HOLDS / EDGE TRUST UNPROVEN / EDGE TRUST
BROKEN, itemized per interface, one broken interface failing the lane.

**The rulings were merged.** `PANEL-DESIGN.md` rulings 4, 5 and 6 were the same rule
written out three times — *a lane that proves its own failure state forces a block* —
each also repeating the same sentence about unproven work capping the grade. They are
now one ruling with the four lane failure states as a list, plus one ruling for the
unproven case. Shared logic is stated once; what each failure state *means* stays in
that lane's own definition in `COLOR-TEAM.md`, inside its own confinement. Amber and
White now join a list instead of adding rulings 7 and 8.

`COLOR-TEAM.md` is v1.8. Red, Blue and Orange are unchanged in substance: their failure
states still force a block, and are now stated once instead of three times.

## 0.7.0 — 2026-10-05

### Orange gets an oracle, because reading the code is the test it was built to pass

Orange had the same three holes Blue had, and one of them was the most dangerous in
the panel: its method was **line-by-line review**. That is precisely what
AI-generated code is optimized to survive. Code that looks right is the expected
output of the generator, so an auditor who decides correctness by reading is testing
the one property the code was built to have.

"Critical" was also undefined — no rule said where Orange's lane started or stopped,
so Orange chose its own scope — and the sub-verdict (*"critical logic sound as used"*)
was a judgment call.

**Orange now works from invariants.** Its lane is the logic that enforces a named
invariant: *this must always be true*. Every signature verifies. Amounts sum. A nonce
never repeats. A session cannot be replayed. The balance never goes negative. Orange
publishes that list **before** testing, and a critical path with no written invariant
is itself a finding — if nobody ever said what correct means, nobody can say the code
is correct.

**The oracle rule.** Every invariant is established against a definition of correct
that lives **outside the implementation**: a specification or standard (RFC, BIP,
NIST/FIPS, the protocol contract), official test vectors, an independent reference
implementation, published analysis, or the mathematics written out and shown. The
code's own comments, its own docs, its own tests, and "it looks right" are **not**
oracles — an implementation and a comment generated by the same model come from the
same source, so they cannot corroborate each other.

**Five tests per invariant:** stated, derived independently (the expected answer is
written down *before* the implementation is read), matched by execution,
boundary-covered (zero, one, negative, maximum, exactly-at-limit, just-over-limit,
empty, duplicate, replayed, out-of-order, non-canonical encodings), and pinned.

**Sub-verdict computed, never chosen:**

| What Orange found | Sub-verdict |
|---|---|
| An invariant the oracle shows the code violating | **LOGIC WRONG** |
| An invariant that cannot be established — no independent statement of correct, an oracle that could not be matched to execution, or a match with nothing pinning it | **LOGIC UNPROVEN** |
| Every invariant stated, derived independently, matched, boundary-covered and pinned | **LOGIC PROVEN** |

Itemized per invariant, and the report must say *which* of the three reasons made
something unproven. One wrong or unproven invariant fails the whole sub-verdict; the
rest do not offset it.

**Grade link (`PANEL-DESIGN.md` ruling 6):** LOGIC WRONG is an automatic ⛔ BLOCKED —
clean defensive coding cannot compensate for computing a declared asset's arithmetic
incorrectly. LOGIC UNPROVEN holds the grade no higher than ⚠️ CONDITIONAL: CLEARED
requires the critical logic to be proven.

**The seam with Red and Blue**, now written down because three colors touch
authorization and only the question separates them: Red asks whether the gate can be
got through, Blue asks whether the gate is present, enforced on every path, effective,
fail-closed and pinned, and Orange asks whether the gate computes the right answer.

**The dependency delta gets a standard.** For every critical dependency: the version
pinned, what changed since the last audited version, and whether that change touches a
named invariant. Read the diff — the changelog is a claim, not evidence. With no
previous audit there is no delta, and Orange says so instead of implying one.

`COLOR-TEAM.md` is v1.7. The README gains the Orange panel row and an **🟠 Orange, in
more detail** section.

## 0.6.0 — 2026-10-05

### Red and Blue stop being advisory

Until now the panel produced six sub-verdicts that did not connect to the grade. A
report could print "no breach found" and "defenses hold" and still end ⛔ BLOCKED
with nothing explaining why that is not a contradiction — and the reverse: a
sub-verdict that sounded clean while the lane behind it had proved nothing.

Red and Blue are now the two colors that can decide the grade by themselves.

**Red is contained, and binary.** Red attacks the repository, everything it ships,
and every declared dependency — *not* the machine it runs on. A missing firewall is
not a finding; "get root" is in scope only as *this software escaping its own
process*. Every hop of a claimed path must be inside that boundary, and a path that
needs a hop outside is recorded as an exclusion with the missing hop named. Its win
conditions are five verbs applied to the declared assets — read it, change it,
destroy it, act as the owner, escape the process — and its verdict is **BREACH
DEMONSTRATED / NO BREACH DEMONSTRATED**, itemized per declared asset. One breach
fails the whole sub-verdict; five clean assets do not offset it. A demonstrated
breach is an automatic ⛔ BLOCKED (`PANEL-DESIGN.md` ruling 4).

**Blue gets a standard instead of a lens.** It starts from every protection the
artifact claims about itself, publishes that inventory, and judges each control on
five tests: present, reachable where it matters, effective, fail-closed, and
pinned. *A test that exists is not evidence; a test that can fail is* — so Blue
breaks the control in a disposable copy, runs the suite, and watches. A test that
stays green is itself the finding; a suite that will not run is a gap, never a
pass. The sub-verdict is computed from the tests, and the worst control on the
table wins: **DEFENSES HOLD / DEFENSES HOLD WITH GAPS / DEFENSE BROKEN**. A
control that does not hold is an automatic ⛔ BLOCKED; an unpinned one caps the
grade at ⚠️ CONDITIONAL (`PANEL-DESIGN.md` ruling 5). Rule 4's read-only
requirement gained the disposable-local-copy carve-out that check needs.

### The six definitions get one home

`COLOR-TEAM.md` and `PANEL-DESIGN.md` both defined the six agents, in different
words (17–53% shared vocabulary) and with opposite instructions: `COLOR-TEAM.md` is
frozen and citable, while `PANEL-DESIGN.md` opens by telling the reader to adapt
everything in it. `COLOR-TEAM.md` now owns the definitions — it is the file whose
whole subject is "what the six agents are," and published audits already cite it
whole — and `PANEL-DESIGN.md` keeps a pointer. Each entry is now
Role / Method / Output / Sub-verdict. `COLOR-TEAM.md` is v1.6.

The "must not be adapted away" list previously protected five process properties
but **not the six lenses**, so a charter could be rewritten into something
toothless while still citing the standard. The definitions themselves now lead that
list.

### Also

- The README defines the three grades and the three deliverables for the first
  time, and gains **🔴 Red, in more detail** and **🔵 Blue, in more detail**.
- The report-shape list in `PANEL-DESIGN.md` — broken since before 0.2.1, whose
  changelog entry claimed to have fixed it — now nests properly and starts at 1.
- Two grade rulings rendered the stop sign as the wrong character; fixed.

## 0.5.1 — 2026-10-05

### The parallel wave is explained, and stops being sold as a speed purchase

The framework already required Phase 1 to dispatch five specialists in parallel, but
nowhere said **why** — so a reader could not tell which part of "parallel" is
load-bearing, and the cost note read as though the wave were an optimization you
could trade for money.

The mechanism, now stated in `colorteam-auditor.md` and `PANEL-DESIGN.md`, is
**drift**. A single agent working down a checklist feeds on its own prior output: by
the fifth lane it is reasoning from the conclusions and blind spots of the first
four, and an early wrong call propagates to the end instead of being contradicted by
a fresh reader.

- The requirement is **one fresh context per specialist**, not simultaneous
  wall-clock. Running each color as its own isolated session keeps the independence
  and gives up only the speed — an acceptable trade.
- Running all five lanes in one shared session is **not** a cheaper version of the
  wave; it is a different, weaker method, and the grade it produces is not
  comparable. Disclose it in the coverage section if you do it.
- `PANEL-DESIGN.md`'s cost note is reframed, defining rule 1 in
  `colorteam-auditor.md` now names the drift mechanism, and the README no longer
  offers one-session sequential as the fallback.
- No other rule changed.

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
