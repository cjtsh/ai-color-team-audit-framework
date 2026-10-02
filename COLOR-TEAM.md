# The Color Team — definitions (v1, locked 2026-10-02)

A security review performed by a named panel of specialist agents, each with one
lens and one job. Two of the colors are borrowed from established security
vocabulary — **red** (attackers) and **blue** (defenders) are industry terms. The
other three lenses and the referee are this project's extensions, chosen so every
major way a Bitcoin application can fail has exactly one agent whose whole job is
to look for it. Together: **five specialists and a referee.**

| Color | Agent | In one sentence |
|---|---|---|
| 🔴 Red | The attacker | Tries to steal the money, the keys, or the operator's decision — by any path. |
| 🔵 Blue | The defender | Proves every stated protection actually holds and is pinned by a test that fails if anyone breaks it. |
| 🟠 Orange | The cryptographer | Checks the mathematics and the money semantics — signatures, addresses, transaction building. |
| 🟤 Copper | The hardware specialist | Checks everything between the app and the physical signing devices — wires, USB, firmware bridges. |
| 🟡 Amber | The supply-chain inspector | Checks how the artifact is born — every dependency, build step, signature, and download in the chain. |
| ⚪ White | The referee | Sees everything, re-verifies every load-bearing claim personally, and gates what gets published. |

---

## 🔴 RED — the attacker

**Role:** offense. Given the application and a hostile world — a malicious
blockchain explorer, a counterfeit USB signer, a hostile wallet file, a malicious
program on the same computer, a compromised dependency — find any path to the
funds, the keys, or the operator's approval. Attack newest code hardest: fixes are
changes, and changes are where new holes live.

**Method:** adversarial code reading, hostile-input construction, attack-path
tracing, abuse of every input the software accepts.

**Deliberately does not read** prior audit conclusions, so it cannot inherit the
lead auditor's blind spots.

**Sub-verdict:** *No breach found* / *Breach found* (with the exact path).

## 🔵 BLUE — the defender

**Role:** defense. Instead of attacking, audit the armor. For every stated
protection — the mainnet opt-in gate, the reviewed-transaction binding, signature
verification, explorer identity checks, fail-closed error handling, local API
authentication — prove it holds end-to-end in code, and prove a regression test
pins it, so no future change can silently break it.

**Method:** control-by-control verification, test-coverage analysis, hunting the
missing test that would let a protection quietly rot.

**Sub-verdict:** *Defenses hold* / *Defenses hold with gaps* / *Defense broken*.

## 🟠 ORANGE — the cryptographer

**Role:** mathematics and money semantics. The cryptography library line by line
(including what changed since the last audit — an upgrade that fixes old bugs can
quietly change behavior the app depends on), signature verification, sighash
handling, key derivation, address encoding, transaction and PSBT semantics,
amount and fee arithmetic.

**Method:** line-by-line library review, validation against Bitcoin's official
test vectors (BIP-32, BIP-143, BIP-173/350), reachability analysis for every
defect found.

**Sub-verdict:** *Cryptography sound as used* / *Defects found* (each marked
reachable or not reachable in this application).

## 🟤 COPPER — the hardware specialist

**Role:** the physical layer. Everything between the application and the signing
devices: the device-communication bridge (HWI), the USB library (libusb —
including which copy actually loads on real machines), device identity and the
moment it is checked, the Jade PIN relay, the frozen binaries' entitlements and
signature posture, and the counterfeit-device question.

**Method:** transport code review, binary inspection, loader-resolution
experiments, device-identity timing analysis.

**Sub-verdict:** *Transport sound* / *Gaps found*.

## 🟡 AMBER — the supply-chain inspector

**Role:** how the artifact is born. Every dependency and its lock (hash-pinned
end-to-end or not), the CI pipeline's step order and secret handling, build
scripts, code signing, Apple notarization and stapling verified on the actual
published download, the software bill of materials, and the guards that keep a
published version immutable.

**Method:** workflow and lock-file audit, artifact re-hashing, signature and
notarization verification, tamper-path analysis (what could reach a released
build without anyone noticing).

**Sub-verdict:** *Chain holds* / *Chain gaps*.

## ⚪ WHITE — the referee

**Role:** verification. Not a perspective — the gate. Re-derives every
load-bearing claim the other five made: reads the same code, runs the same
commands, quotes what is actually there. Attacks false alarms and false clean
bills of health with equal energy. Nothing is published that White could not
verify.

**Sub-verdict:** a claim-by-claim verdict table, a calibration opinion, and the
publication decision: *Publish / Publish with edits / Do not publish.*

---

## How the grades combine

Each agent's sub-verdict prints in the report under its own name and color. The
overall grade — Green / Yellow / Red — is defined in writing **before** the audit
begins (see `PANEL-DESIGN-0.6.3.md`), and is the **floor** of the panel, never
the average: a single Red-grade finding fails the review no matter how strong the
other sections are.

## The rules that make it honest

1. Charters and grade definitions are written before the build is examined and do
   not change afterward.
2. The five specialists work independently and do not see each other's findings
   until the panel merge; the referee sees everything.
3. Every finding carries a stable ID, exact file and line, evidence, and a
   suggested remedy — nothing is asserted without proof attached.
4. The panel format is presentation; the evidence standard is the audit
   framework's, unchanged (read-only, no key material, no mainnet, uncertainty
   is a result, say what was not examined).

---

*Color Team definitions v1 — part of the AI Color Team Audit Framework (this
repository). Red and blue are established security-industry terms; orange, copper,
amber, and white were introduced by the framework's first runs (Bitcoin Easy Signer
audits, October 2026). This page may be reproduced in any report that uses the
format; reproduce it whole and cite the version.*
