# Panel Design — charters, phases, rubric, report shape

Everything here is a starting point to adapt to your target. What must NOT be
adapted away: independence of the wave, the pre-locked rubric, floor-of-panel
grading, and the referee's publication gate. Those four properties are the
framework; everything else is configuration.

## Phase structure

```
Phase 0  Baseline      — lead only: verify target/commit/artifacts, run suites,
                         read the project's claims, write charters, LOCK THE RUBRIC
Phase 1  The wave      — five specialists dispatched simultaneously, each seeing
                         only its own charter (no cross-visibility, no priors for Red)
Phase 2  The referee   — White re-derives load-bearing claims, merges the ledger,
                         calibrates severity, applies the rubric mechanically, gates
Phase 3  Consolidation — lead applies the grade, writes private + public reports,
                         publishes only what the gate allows
```

## Charter sketches (adapt lanes, keep the colors)

**🔴 Red — offense.** You are an attacker. Given the software and a hostile world,
find any path to the assets — funds, keys, data, or the operator's decision. Attack
the newest code hardest: fixes are changes, and changes are where new holes live.
You do NOT read prior audit conclusions. Output: attack log (attempt → outcome),
findings, sub-verdict: *No breach found / Breach found (with the path).*

**🔵 Blue — defense.** Audit the armor, not the attacks. For every stated control,
prove it holds end-to-end in code AND is pinned by a regression test that fails if
anyone breaks it. An unfixed control and an untested one both count as gaps. If a
remediation work order exists, verify every item against its acceptance criteria.
Output: control-by-control table, fix ledger, sub-verdict: *Defenses hold /
hold with gaps / broken.*

**🟠 Orange — cryptography & critical logic.** The mathematics and semantics your
target cannot afford to get wrong (for a wallet: signatures, derivation, encoding,
transaction semantics; for a web app: auth tokens, session logic, crypto usage).
Diff every dependency against its last-audited version — upgrades fix old bugs and
quietly change behavior. Validate primitives against official test vectors.
Output: delta tables, vector results, sub-verdict: *Sound as used / defects found
(reachable?).*.

**🟤 Copper — hardware & endpoints.** Everything between the software and the
physical world: device transports and drivers, the browser and native clients,
frozen/embedded binaries. Verify loader behavior on real machines, not just in
theory. Output: transport findings with runtime evidence where possible,
sub-verdict: *Transport sound / gaps found.*

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

- 🟢 **GREEN** — requires ALL of: zero open Critical/High; every prior-cycle
  finding verified fixed or closed by dated owner acceptance; stated defenses held
  and regression-tested; suites green, artifacts re-verified; no new Critical/High.
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

## Report shape

1. **For humans, first:** grade and why; the four questions (or the target's
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

## Cost note

Five deep specialists plus a referee is a real compute spend. The wave buys
wall-clock speed AND structural independence; if cost matters more than speed, run
the colors sequentially in isolated sessions and disclose the weaker independence
in the coverage section.
