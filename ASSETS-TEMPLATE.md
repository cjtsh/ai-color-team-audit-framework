# ASSETS-TEMPLATE.md — your Asset Declaration

**How this file gets written (the two-agent flow):** you should not have to
author it from scratch. The normal flow is:

1. **The Surveyor drafts it.** One AI agent (any coding tool — ideally a
   *different* model than the one that will run the audit, so the drafter's blind
   spots don't become the panel's) reads the repository — entry points, data
   stores, auth surfaces, dependencies, deployment — and fills in this template
   from what the code actually does. Give it this file plus the repo.
2. **You confirm it.** Read the draft; correct anything the code cannot know
   (business context, contractual obligations, "the real crown jewel is X");
   re-rank if your priorities differ. This confirmation is the one human moment
   the framework insists on — an unconfirmed declaration is unverified scope,
   and a quietly narrowed declaration is a steered audit.
3. **It locks.** Save as `ASSETS.md` in the repo root. The audit's lead agent
   reads it in Phase 0 and locks it with the grade rubric; it does not change
   after the audit begins.

If you prefer, write it yourself from the blank sections below — the Surveyor is
a convenience, your confirmation is the requirement.

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
