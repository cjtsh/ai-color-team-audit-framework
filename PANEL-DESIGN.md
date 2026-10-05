# Panel Design — phases, rubric, report shape

Everything here is a starting point to adapt to your target. What must NOT be
adapted away: **the six agent definitions themselves** — they are the standard, they
live in `COLOR-TEAM.md`, and you adapt the lanes, never the colors — independence of
the wave (a fresh context per specialist), the pre-locked rubric, floor-of-panel
grading, the referee's publication gate, and **survey/audit model separation** — the
model that writes the audit plan is never the model that runs the audit. Those are
the framework; everything else is configuration.

## Phase structure

```
Phase 0  Baseline      — lead only: verify target/commit/artifacts, verify the
                         owner-signed audit plan (stop if absent), run suites,
                         read the project's claims, write charters, LOCK THE RUBRIC
Phase 1  The wave      — five specialists dispatched in parallel, each in its own
                         fresh context and seeing only its own charter (no
                         cross-visibility, no priors for Red)
Phase 2  The referee   — White re-derives load-bearing claims, merges the ledger,
                         calibrates severity, applies the rubric mechanically, gates
Phase 3  Consolidation — lead applies the grade, writes the report's sections
                         (safety review + technical report + ledger)
Phase 3½ Verification — nothing is published until the live artifact is fetched
                         and hash-matched (publish-and-verify.sh)
Phase 4  The next cycle — when the grade is BLOCKED or CONDITIONAL: the report names
                         what to fix; fix it, cut a new revision, and run the audit
                         again. Each cycle keeps its own plan, lock, and report, and
                         appends one row to the index.
```

## The audit plan (produced before Phase 0, mandatory)

The audit's single input parameter is **the audit plan**
(`<repo>-colorteam-audit-plan-<cycle>.md`), produced by the survey — step one, which runs
*before* this runbook is opened at all. It has two halves:

- **The Asset Declaration** — the target's crown jewels, ranked: what must not be
  stolen, destroyed, altered, or acted upon without authorization.
- **The scope** — what is in, what is out and why, and what the surveyor did not
  examine.

Written before anyone examines the build, locked with the rubric, and cited in the
report header. It parameterizes every charter, every severity call, and the central
questions.

**The plan opens with a locked-scope block (section 0), written out in full and not by
reference** — a pointer to this page freezes nothing. It carries the declared assets, the
definitions in force, the rubric as adapted to this target, the exact revision, and what
is excluded. The owner signs it with an identity and a date, and that signature is the lock.

**The signature identifies; it does not publish a person.** A handle, a role, an
organization, or a named team is a complete sign-off, and all four are better than a
personal name: nothing in the lock needs an individual's legal identity, and a published
name is a disclosure nobody asked for. What is *not* a sign-off is a blank, an
"anonymous", or the surveyor, the auditor, or the operator of either — a scope nobody
accepted is a scope the auditor chose, which is the one thing this structure exists to
prevent. The plan and the lock are local working files; the published report carries the
hashes and the sign-off identity, never a person unless the signer put one there.

**What the signature means: the scope, not the results.** The findings are produced after
the signature, so signing cannot be an endorsement of them — it accepts the scope the
audit runs against. That is the whole of what the owner agrees to.

**How it is produced (two agents, five steps):** a Surveyor agent (`colorteam-surveyor.md`)
reads the repository and writes the plan from what the code actually does; the owner
corrects anything only they know and signs the locked-scope block; the signed
file locks. **Phase 0 does not produce it — Phase 0 verifies** that it exists, is
owner-signed, and names the revision being audited.

**And the lock leaves a fingerprint.** Before the first specialist is dispatched, the
auditor computes the SHA-256 of the signed plan and records it — with the plan's filename,
the target revision, and the sign-off date — in a companion file
`<repo>-colorteam-audit-lock-<cycle>.md`, never inside the plan itself, because writing the
hash into the file would change the bytes it was taken over. The referee re-hashes the plan
at the end and compares. Equal hashes mean the scope never moved and the panel graded what
it said it graded. Unequal means the plan and the findings describe different audits: the
audit is **void**, the publication decision is **DO NOT PUBLISH**, and there is no grade to
argue about. Both hashes appear in the report.

**Two hashes prove the scope did not move during the audit; they do not prove when it was
written relative to the findings**, because one operator holds both. Closing that gap takes
one thing outside that operator's control: publishing the hash before the panel runs — a
commit, a gist, an issue comment. It is optional and it takes one line. **The owner does
nothing new either way:** they already read and check the plan; signing it is the same
sitting, and the hashing is the agents' job.

**If you want a timestamp no one can rewrite — including the operator**, a public
blockchain is one place to put it: the plan's hash before the run, or the report's hash
after, written into a transaction and memorialised with a time that depends on no one's
word. The framework does not build this and does not need it. It is there for anyone who
wants the order of events provable to a third party.

**The Surveyor must never be the model that runs the audit.** This is a structural
requirement, not a preference. The Surveyor decides what is even in scope. If one
model writes the plan and then audits against it, the same blind spot sits on both
sides of the handoff: the panel works faithfully from an incomplete scope, finds
nothing wrong with what it can see, and grades it CLEARED on software nobody actually
examined. Two different models — ideally from different vendors, so the training
data and the failure modes differ too — is the only thing that breaks that circuit.

If you have only one model available, skip the Surveyor: the owner writes
`<repo>-colorteam-audit-plan-<cycle>.md` by hand using the skeleton in
`colorteam-surveyor.md`. The Surveyor is a convenience; **never reusing the audit model is
the rule.** The owner's sign-off is never skipped either — it is the framework's defense
against a steered (narrowed) plan.

Examples by domain:

- **Payments wallet:** funds; key material; the operator's approval of a
  transaction.
- **Web service:** user credentials and session control; personal and payment
  data; administrative access; the integrity of stored data.
- **Database-backed service:** privilege boundaries; data integrity;
  injection-to-extraction paths as the attack class against those boundaries.
- **Embedded / infrastructure:** safety interlocks; availability; control-plane
  authentication.

The lanes adapt with the declaration (the colors do not). Orange for a wallet is
signature math; for a web service it is auth, session, and token logic; for a data
platform it is query semantics and privilege evaluation. Copper for a wallet is
signing devices; for a web service it is the browser client and native apps; for
infrastructure it is agents and edges. Say in the report which lanes you mapped
where.

## The charters

The six agent definitions live in **[COLOR-TEAM.md](COLOR-TEAM.md)** — role, method,
output, and sub-verdict for each. That page is the standard, not a sketch, and it is
not adapted: the lanes bend to your target (see above), the colors do not. Phase 1
gives each specialist the full text of its own definition as its charter.

## The rubric (adapt, then lock, then never touch mid-audit)

- ✅ **CLEARED** — requires ALL of: zero open Critical/High (as affects the declared
  assets for users of the audited version); every prior-cycle finding verified fixed
  or closed by dated owner acceptance; every lane's claims proven and pinned — each
  defense present, reachable where it matters, effective, fail-closed, and held by a
  test that can fail; suites passing, artifacts re-verified; no new Critical/High.
- ⚠️ **CONDITIONAL** — no Critical/High, but open Mediums beyond owner acceptance,
  fix-verification gaps, or **anything a lane leaves unproven** — an unpinned control,
  **LOGIC UNPROVEN**, **EDGE TRUST UNPROVEN**, **CHAIN UNVERIFIED**. The cap applies
  when the unproven thing is on the path to a declared asset; something that provably
  cannot reach one, with the exclusion demonstrated, is a coverage note and does not
  cap. Label honestly: good software with work remaining.
- ⛔ **BLOCKED** — any open Critical/High, **or any lane that proved its own failure
  state** (ruling 4). Do not ship; say what and why.

**Rulings encoded from real runs (keep these):**

1. *Every clause of the rubric must be reachable.* If the CLEARED list and the
   CONDITIONAL clause can both be read to apply, resolve so CONDITIONAL can bind —
   ambiguity is never resolved in CLEARED's favor. (First encoded after the v0.6.3
   Bitcoin Easy Signer ruling: five CLEARED conditions met, one open Medium held the
   grade at CONDITIONAL.)
2. *Acceptance must be written, dated, and post-date the finding.* A documented
   procedure is not acceptance of a risk; disclosure is not acceptance; never
   invent owner acceptance.
3. *The grade is the floor.* No averaging, no trading a strong section against a
   bad one.
4. *A lane that proves its own failure state forces a block.* The grade is ⛔
   BLOCKED — no severity calibration, no rubric judgment, no weighing it against
   clean lanes — when a lane proves:

   - **Red** — **BREACH DEMONSTRATED** against any declared asset.
   - **Blue** — a claimed control that is not present, not reachable where it
     matters, not effective, or fails open.
   - **Orange** — **LOGIC WRONG** against a named invariant.
   - **Copper** — **EDGE TRUST BROKEN** at a named interface.
   - **Amber** — **CHAIN BROKEN** at a named link.

   Each lane's own definition in `COLOR-TEAM.md` says what its failure state means
   and what demonstrates it, within that lane's area of expertise. A lane that does
   not prove its failure state forces nothing, and the grade is then decided by the
   rest of the panel.
5. *Anything a lane leaves unproven holds the grade at CONDITIONAL.* An unpinned
   control, an invariant that is **LOGIC UNPROVEN**, an edge that is **EDGE TRUST
   UNPROVEN**, a chain link that is **UNVERIFIED**: CLEARED requires every claim to be
   proven and pinned, and ambiguity is never resolved in the software's favor. The cap
   applies when the unproven thing is on the path to a declared asset. Something that
   provably cannot reach one — a dev-only tool that never runs in the build,
   documentation, an example in a separate directory, with the exclusion demonstrated —
   is a coverage note and does not cap. What this does not soften: an artifact whose
   build cannot be reproduced is on that path by definition, and still caps.
6. *The grade is computed, not calibrated.* White applies the rubric and the rulings to
   the surviving sub-verdicts and shows the arithmetic — which lane set the floor and
   which ruling bound it. The referee never raises or lowers a lane's sub-verdict, and a
   disagreement with the outcome is recorded as a dissent while the grade stands: a
   referee with discretion over the floor has made the floor optional.
7. *A drifted scope voids the audit.* The signed plan is hashed before the first
   specialist runs and re-hashed by the referee at the end, and both hashes are printed in
   the report. Equal hashes mean the scope never moved. Unequal — a plan edited mid-audit,
   a missing lock, a hash that cannot be produced — means the findings and the scope no
   longer describe the same audit: **DO NOT PUBLISH**, no grade, no partial credit. It is
   not a finding to be weighed and it is never resolved in the software's favor. Regrade
   against a re-signed plan or not at all.
8. *Every prior finding is accounted for.* The fix ledger is a round trip, not a summary.
   Cycle N's report cites cycle N−1's report file and its SHA-256, and the referee
   enumerates the prior report's ledger and confirms that **every ID it carried appears
   in this cycle's ledger** — not merely that the fixes listed are genuine. A prior
   finding absent from the ledger is itself a finding, and a grade reached by letting one
   drop is not earned. The scope lock proves the scope did not move *within* a cycle; only
   this check proves the ledger did not shrink *between* cycles.

## Report shape — one report, three sections, three audiences

Every engagement produces **one report**, `<repo>-colorteam-audit-report-<cycle>.md`,
carrying three sections, one per audience, written in this order:

1. **The technical report** — for the engineers and the next auditor (the source of truth;
   everything else translates from it).
2. **The plain-English Safety Review** (`SAFETY-REVIEW-TEMPLATE.md`) — for the decision-maker:
   verdict, the questions they actually ask, the team in layman's words, the trail with
   severity badges. Translate from the technical report; never exceed it.
3. **The findings ledger** — for agents and future audits (stable IDs, exact locations,
   machine-checkable). It is the report's Appendix.

The three are assembled from the technical report, each translating from the one before
it and never exceeding it. White owns what they must contain and whether they may go
out, including the coverage section — a report that does not say where the audit
stopped is claiming more than it did.

The one thing that does not go in it is the owner's private full report — everything,
verbatim evidence — which is never published.

**The technical report contains:**

1. **The grade, and why.** The four questions (or the target's equivalent: can it do
   the unforgivable thing? can it leak the unspeakable thing? can anyone act
   invisibly? what to fix first?) and the path forward if the grade is not CLEARED.
2. **The fix ledger:** prior findings → status at this commit, with evidence.
3. **The color sections:** each agent's charter summary, what it did, findings,
   sub-verdict — named, in language a non-engineer can follow.
4. **The referee's section:** what was re-derived and held, what was corrected,
   the grade ruling with its reasoning.
5. **Coverage and limits:** what was not examined and why. An audit that does not
   say what it failed to examine tells you very little.
6. **Agentic appendix:** the full findings ledger with stable IDs and exact
   locations, structured so a future auditor — human or AI — can verify the work
   without re-deriving it.

## Conversion re-checks

When a cycle ends CONDITIONAL with a defined conversion path, the follow-up is a light
re-check, not a full audit: Phase 0 baseline on the new version → a delta-scoped wave
covering only the domains the delta touches (unchanged domains carry over by VERIFIED
blob-identity, never assumption) → the referee rules the conversion criterion met *by
execution* (a demonstrated fix, a machine-enforced gate that actually ran) and that the
delta introduced no new Critical/High. Grade converts if and only if both hold. A light
re-check is a lighter audit, not a footnote to the previous one: it still writes its own
plan, its own lock, and its own report file, and it still appends its own row to the index.

## The cycle index

The audit is a loop, and the loop needs a scoreboard. Every engagement produces **one
report per cycle** and **one index across cycles**: `<repo>-colorteam-audit-index.md`, in
the repository root, appended at the end of each cycle and never overwritten. One row per
cycle — the revision, the date, the grade, the auditor, and which prior findings remain
open — so the arc is visible in a single file instead of scattered across N reports that
may not even survive each other.

The index is not decoration. A framework that produces a BLOCKED report and stops has told
you what is wrong and left you there. The index is the record that the previous cycle's
findings were fixed and the grade moved — or that they were not, and it did not.

It is gated with the report: it may not claim a grade the report did not earn.

## Why the wave cannot be a checklist, and what it costs

Five deep specialists plus a referee is a real compute spend. It buys wall-clock
speed, but speed is the side effect — the product is **independence**. One agent
working five lanes in sequence feeds on its own output: everything lane five
"notices" is filtered through what lanes one to four already concluded, and an early
wrong call propagates to the end instead of being contradicted by a fresh reader.
The wave is how the panel gets five genuinely separate first impressions of the same
code.

So the requirement is **one fresh context per specialist**, not simultaneous
wall-clock. If cost matters more, run each color as its own isolated session — you
keep the independence and lose only the parallelism, which is fine. Running all five
lanes in one shared session is not a cheaper version of the wave; it is a different,
weaker method, and the grade it produces is not comparable. Any weaker arrangement
must be disclosed in the report's coverage section.
