# ASSETS-TEMPLATE.md — your Asset Declaration

**This is the one thing you fill in before an audit can run.** Copy this file to
`ASSETS.md` in the repository being audited (or paste it into the conversation with
your agent) and complete the three sections below. It takes about five minutes.
The lead auditor reads `ASSETS.md` in Phase 0, locks it with the grade rubric, and
every agent charter is built from it. If no `ASSETS.md` exists, the agent's first
act is to interview you and write one — with your confirmation — before anything
else happens.

Guidance: 3–6 assets, ranked most-valuable-first. An asset is a thing an attacker
could steal, destroy, alter, or act upon without authorization. Be specific to
YOUR software; vague declarations produce vague audits.

---

## 1. The declared assets (ranked)

| Rank | Asset | What must NOT happen to it |
|---|---|---|
| 1 | [e.g., User credentials and session tokens] | [e.g., stolen, forged, replayed, or used without the user's action] |
| 2 | [e.g., Stored personal and payment data] | [e.g., extracted by injection or access-control failure; silently altered] |
| 3 | [e.g., Administrative control of the service] | [e.g., obtained through privilege escalation] |
| 4 | [e.g., Availability of the service] | [e.g., destroyed or degraded by unauthenticated action] |

## 2. The unforgivable acts (in plain words)

1. [The one-sentence worst outcome, e.g., "An attacker reads or modifies the
   customer database without a valid account."]
2. [Second worst, e.g., "An attacker gains admin without stealing a password."]

## 3. Where the assets live (so the agents know where to look)

- [e.g., PostgreSQL via SQLAlchemy models in `app/models/`; sessions in Redis;
  secrets in environment variables injected by the CI]
- [e.g., Client-side: React SPA in `web/` calling the API in `api/`]

---

## Worked example (filled in) — a database-backed web service

> **1. Declared assets (ranked):** (1) User credentials and session control — must
> not be stolen, forged, or replayed. (2) Stored personal and payment data — must
> not be extracted via injection or broken access control, or silently altered.
> (3) Administrative access — must not be reachable through privilege escalation.
> (4) Service availability — must not be degradable by unauthenticated actions.
>
> **2. Unforgivable acts:** (1) "An attacker reads or modifies the customer
> database without a valid account." (2) "An attacker becomes admin without
> stealing a credential."
>
> **3. Where they live:** PostgreSQL reached through SQLAlchemy (`app/models/`);
> session tokens issued in `app/auth/` and stored in Redis; card data handled by
> `app/billing/`; admin endpoints under `app/admin/`; browser client in `web/`.

With that one page, the panel maps itself: Red hunts injection-to-extraction and
privilege-escalation paths against assets 2–3; Blue demands parameterization and
access-control proofs with regression tests; Orange takes `app/auth/` session and
token logic; Copper takes the `web/` client; Amber takes the dependency chain —
and the report's central questions become your two unforgivable acts.

*(For contrast, the founding run — a Bitcoin wallet — declared: funds; key
material; the operator's approval of a transaction. Same five colors, completely
different hunt. See EXAMPLES.md.)*
