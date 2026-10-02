# Worked Examples

Real audits run with this framework, with their real grades — including the ones
that were not green. Evidence beats marketing; every link below is a complete,
public, citable report.

## Bitcoin Easy Signer (October 2026)

A macOS application that guides non-technical operators (spouses, trustees,
lawyers) through payments from an existing 2-of-3 multisig Bitcoin wallet —
inheritance-recovery software, where "who did you annoy" includes the entire
Bitcoin threat model.

1. **[v0.6.2 — single-lead audit with specialist sub-agents](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.2.md)**
   25 findings (1 High supply-chain, 6 Medium, rest Low/Info), zero Critical, and
   four plain-language answers for a trustee audience. Every finding carried a
   stable ID and a written remedy; the remediation work order for the next release
   was generated directly from it. A
   [typeset PDF edition](https://cjtsh.github.io/bitcoin-easy-multisig-signer/audits/ZAI-Security-Audit-v0.6.2.pdf)
   was published on the product site.

2. **[v0.6.3 — the first full Color Team run](https://github.com/cjtsh/bitcoin-easy-multisig-signer/blob/main/releases/AUDIT-ZAI-0.6.3.md)**
   The remediation release, audited by the full panel: the attacker found no
   breach; the defender verified all 22 actionable prior findings fixed and pinned
   by reverting regression tests; the cryptographer proved the project's vendored
   library was upstream plus exactly two declared lines (one of them a fix upstream
   still hasn't merged); the hardware specialist verified the USB-stack fix on a
   real machine; the supply-chain inspector verified every pipeline claim — and
   found that the release had been published manually, so the project's own new
   automated gates never executed. **Grade: Yellow.** All five green conditions
   were otherwise met. The referee refused to resolve the rubric's ambiguity in
   green's favor, refused to invent owner acceptance, and defined the one-step
   conversion path in the report itself.
   [Typeset PDF edition](https://cjtsh.github.io/bitcoin-easy-multisig-signer/audits/ZAI-Security-Audit-v0.6.3.pdf).

The v0.6.3 report is the framework's proof of integrity: the panel graded its own
sponsor Yellow on a process finding when a green was available for the asking. If
a framework can do that, its greens are worth something.

---

Ran a Color Team audit with this framework — whatever grade you got? Open a PR
adding it here. Non-green results are especially welcome; they are the format's
credibility.
