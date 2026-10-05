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
                         owner-confirmed audit plan (stop if absent), run suites,
                         read the project's claims, write charters, LOCK THE RUBRIC
Phase 1  The wave      — five specialists dispatched in parallel, each in its own
                         fresh context and seeing only its own charter (no
                         cross-visibility, no priors for Red)
Phase 2  The referee   — White re-derives load-bearing claims, merges the ledger,
                         calibrates severity, applies the rubric mechanically, gates
Phase 3  Consolidation — lead applies the grade, writes the three deliverables
                         (safety review + technical report + ledger)
Phase 3½ Verification — nothing is published until the live artifact is fetched
                         and hash-matched (publish-and-verify.sh)
```

## The audit plan (produced before Phase 0, mandatory)

The audit's single input parameter is **the audit plan** (`<repo>-colorteam-audit-plan.md`),
produced by the survey — step one, which runs *before* this runbook is opened
at all. It has two halves:

- **The Asset Declaration** — the target's crown jewels, ranked: what must not be
  stolen, destroyed, altered, or acted upon without authorization.
- **The scope** — what is in, what is out and why, and what the surveyor did not
  examine.

Written before anyone examines the build, locked with the rubric, and cited in the
report header. It parameterizes every charter, every severity call, and the central
questions.

**How it is produced (two agents, three steps):** a Surveyor agent (`colorteam-surveyor.md`)
reads the repository and writes the plan from what the code actually does; the owner
confirms or corrects it in one short sitting; the confirmed file locks. **Phase 0
does not produce it — Phase 0 verifies** that it exists, is owner-confirmed, and
names the revision being audited.

**The Surveyor must never be the model that runs the audit.** This is a structural
requirement, not a preference. The Surveyor decides what is even in scope. If one
model writes the plan and then audits against it, the same blind spot sits on both
sides of the handoff: the panel works faithfully from an incomplete scope, finds
nothing wrong with what it can see, and grades it CLEARED on software nobody actually
examined. Two different models — ideally from different vendors, so the training
data and the failure modes differ too — is the only thing that breaks that circuit.

If you have only one model available, skip the Surveyor: the owner writes
`<repo>-colorteam-audit-plan.md` by hand using the skeleton in `colorteam-surveyor.md`. The Surveyor is a
convenience; **never reusing the audit model is the rule.** The owner's
confirmation is never skipped either — it is the framework's defense against a
steered (narrowed) plan.

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
  assets for users of the audited version); every prior-cycle finding verified
  fixed or closed by dated owner acceptance; stated defenses held and
  regression-tested; suites passing, artifacts re-verified; no new Critical/High.
- ⚠️ **CONDITIONAL** — no Critical/High, but open Mediums beyond owner acceptance, or
  fix-verification gaps. Label honestly: good software with work remaining.
- ⛔ **BLOCKED** — any open Critical/High. Do not ship; say what and why.

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

## Report shape — three deliverables, three audiences

Every engagement produces three deliverables, one per audience — written in this order:

1. **The technical report** — for the engineers and the next auditor (the source of truth;
   everything else translates from it).
2. **The plain-English Safety Review** (`SAFETY-REVIEW-TEMPLATE.md`) — for the decision-maker:
   verdict, the questions they actually ask, the team in layman's words, the trail with
   severity badges. Translate from the technical report; never exceed it.
3. **The findings ledger** — for agents and future audits (stable IDs, exact locations,
   machine-checkable).

The technical report contains: grade and why; the four questions (or the target's
   equivalent: can it do the unforgivable thing? can it leak the unspeakable thing?
   can anyone act invisibly? what to fix first?); the path forward if not CLEARED.
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

When a cycle ends CONDITIONAL with a defined conversion path, the follow-up is a light re-check, not a full audit: Phase 0 baseline on the new version → a delta-scoped wave covering only the domains the delta touches (unchanged domains carry over by VERIFIED blob-identity, never assumption) → the referee rules the conversion criterion met *by execution* (a demonstrated fix, a machine-enforced gate that actually ran) and that the delta introduced no new Critical/High. Grade converts if and only if both hold.

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
