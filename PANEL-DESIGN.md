# Panel Design — charters, phases, rubric, report shape

Everything here is a starting point to adapt to your target. What must NOT be
adapted away: independence of the wave, the pre-locked rubric, floor-of-panel
grading, the referee's publication gate, and **survey/audit model separation** —
the model that writes the survey is never the model that runs the
audit. Those five properties are the framework; everything else is configuration.

## Phase structure

```
Phase 0  Baseline      — lead only: verify target/commit/artifacts, confirm the
                         owner-confirmed survey, run suites, read the project's claims,
                         write charters, LOCK THE RUBRIC
Phase 1  The wave      — five specialists dispatched simultaneously, each seeing
                         only its own charter (no cross-visibility, no priors for Red)
Phase 2  The referee   — White re-derives load-bearing claims, merges the ledger,
                         calibrates severity, applies the rubric mechanically, gates
Phase 3  Consolidation — lead applies the grade, writes the three deliverables
                         (safety review + technical report + ledger)
Phase 3½ Verification — nothing is published until the live artifact is fetched
                         and hash-matched (publish-and-verify.sh)
```

## The survey (Phase 0, mandatory)

The survey is the audit's single input parameter. Its content is the **Asset
Declaration**: the target's crown jewels, ranked — what must not be stolen,
destroyed, altered, or acted upon without authorization. Written before anyone
examines the build, locked with the rubric, and cited in the report header. It
parameterizes every charter, every severity call, and the central questions.

**How it is produced (the two-agent architecture):** a Surveyor agent reads the
repository and drafts the survey from what the code actually does; the owner
confirms or corrects it in one short sitting; the confirmed file (`SURVEY.md`)
locks.

**The Surveyor must never be the model that runs the audit.** This is a structural
requirement, not a preference. The Surveyor decides what is even in scope. If one
model writes the survey and then audits against it, the same blind spot sits
on both sides of the handoff: the panel works faithfully from an incomplete scope,
finds nothing wrong with what it can see, and grades green on software nobody
actually examined. Two different models — ideally from different vendors, so the
training data and the failure modes differ too — is the only thing that breaks
that circuit.

If you have only one model available, skip the Surveyor: the owner writes
`SURVEY.md` by hand from `SURVEY-TEMPLATE.md`. The Surveyor is a convenience;
**never reusing the audit model is the rule.** The owner's confirmation is never
skipped either — it is the framework's defense against a steered (narrowed)
survey.

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

## Charter sketches (adapt lanes, keep the colors)

**🔴 Red — offense.** You are an attacker. Given the software and a hostile world,
find any path to the declared assets: seizing, destroying, or altering them, or
acting on the user's behalf without authorization. Hunt the full attack taxonomy
against the declaration's domain — injection of every kind (SQL, command, path,
template, deserialization), authentication bypass, privilege escalation, logic
abuse, race conditions, spoofing, memory-safety where the stack exposes it. Attack
the newest code hardest: fixes are changes, and changes are where new holes live.
You do NOT read prior audit conclusions. Output: attack log (attempt → outcome),
findings, sub-verdict: *No breach found / Breach found (with the path).*

*Would this find a zero-day-style SQL injection or a root-access bug?* Against a
declared asset of "data integrity and privilege boundaries," yes — Red's charter
becomes exactly that hunt (unsanitized query construction → extraction or
escalation paths; Blue's becomes parameterization and least-privilege controls
plus the regression tests pinning them; Orange's becomes the auth/session logic).
Agent audits read code adversarially and run the target's own tests; they
complement, and do not replace, fuzzers and dynamic scanners — a thorough target
runs both and says so in the coverage section.

**🔵 Blue — defense.** Audit the armor, not the attacks. For every stated control,
prove it holds end-to-end in code AND is pinned by a regression test that fails if
anyone breaks it. An unfixed control and an untested one both count as gaps. If a
remediation work order exists, verify every item against its acceptance criteria.
Output: control-by-control table, fix ledger, sub-verdict: *Defenses hold /
hold with gaps / broken.*

**🟠 Orange — critical logic.** The logic your target cannot afford to get wrong,
chosen by the Asset Declaration (for a wallet: signatures, derivation, encoding,
transaction semantics; for a web app: auth tokens, session logic, authorization
arithmetic; for a data platform: query and privilege semantics). Diff every
dependency against its last-audited version — upgrades fix old bugs and quietly
change behavior. Validate primitives against official test vectors and standards
where they exist. Output: delta tables, vector results, sub-verdict: *Sound as
used / defects found (reachable?).*.

**🟤 Copper — edges & endpoints.** Everything between the core and the outside
world, chosen by the Asset Declaration: the browser and native clients, mobile
and desktop runtimes, devices, drivers and transports, embedded and frozen
binaries — and the counterfeit-component question for each. Verify loader and
client behavior on real machines where possible. Output: edge findings with
runtime evidence where possible, sub-verdict: *Edges sound / gaps found.*

**🟡 Amber — supply chain & pipeline.** How the artifact is born: dependencies and
lockfiles (hash-pinned end to end?), CI step order and secret scoping, build
scripts, signing/notarization verified on the actual published artifact, SBOM
accuracy, release immutability. Always ask: could compromised upstream code reach a
released build without a deliberate version bump? Output: claim-by-claim
verification, residual-risk inventory, sub-verdict: *Chain holds / chain gaps.*

**⚪ White — the referee.** Not a perspective; the gate. Re-derive every
load-bearing claim personally. Attack false alarms and clean bills of health with
equal energy. Merge the specialists' colliding finding IDs into the final ledger.
Apply the rubric mechanically. List the mandatory facts for the public report and
issue the gate: *publish / publish with edits / do not publish.*

## The rubric (adapt, then lock, then never touch mid-audit)

- 🟢 **GREEN** — requires ALL of: zero open Critical/High (as affects the declared
  assets for users of the audited version); every prior-cycle finding verified
  fixed or closed by dated owner acceptance; stated defenses held and
  regression-tested; suites green, artifacts re-verified; no new Critical/High.
- 🟡 **YELLOW** — no Critical/High, but open Mediums beyond owner acceptance, or
  fix-verification gaps. Label honestly: good software with work remaining.
- 🔴 **RED** — any open Critical/High. Do not ship; say what and why.

**Rulings encoded from real runs (keep these):**

1. *Every clause of the rubric must be reachable.* If the green list and the yellow
   clause can both be read to apply, resolve so yellow can bind — ambiguity is
   never resolved in green's favor. (First encoded after the v0.6.3 Bitcoin Easy
   Signer ruling: five green conditions met, one open Medium held the grade at
   Yellow.)
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
   can anyone act invisibly? what to fix first?); the path forward if not green.
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

When a cycle ends YELLOW with a defined conversion path, the follow-up is a light re-check, not a full audit: Phase 0 baseline on the new version → a delta-scoped wave covering only the domains the delta touches (unchanged domains carry over by VERIFIED blob-identity, never assumption) → the referee rules the conversion criterion met *by execution* (a demonstrated fix, a machine-enforced gate that actually ran) and that the delta introduced no new Critical/High. Grade converts if and only if both hold.

## Cost note

Five deep specialists plus a referee is a real compute spend. The wave buys
wall-clock speed AND structural independence; if cost matters more than speed, run
the colors sequentially in isolated sessions and disclose the weaker independence
in the coverage section.
