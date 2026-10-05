# SURVEY-TEMPLATE.md — the survey

**What this is:** the survey — the audit's single input. Its substance is the
**Asset Declaration**: your crown jewels, ranked, and the unforgivable acts.

**How this file gets written (the two-agent flow):** you should not have to
author it from scratch. The normal flow is:

1. **The Surveyor drafts it.** One AI agent running a *different* model than the
   one that will run the audit — ideally from a different vendor — reads the
   repository (entry points, data stores, auth surfaces, dependencies,
   deployment) and fills in this template from what the code actually does. Give
   it this file plus the repo. **This separation is a structural requirement, not
   a preference:** the Surveyor decides what is even in scope, so a model that
   drafts the declaration and then audits it carries the same blind spot on both
   sides of the handoff, and can grade green on software nobody examined.
2. **You confirm it.** Read the draft; correct anything the code cannot know
   (business context, contractual obligations, "the real crown jewel is X");
   re-rank if your priorities differ. This confirmation is the one human moment
   the framework insists on — an unconfirmed declaration is unverified scope,
   and a quietly narrowed declaration is a steered audit.
3. **It locks.** Save as `SURVEY.md` in the repo root. The audit's lead agent
   reads it in Phase 0 and locks it with the grade rubric; it does not change
   after the audit begins.

Write it yourself from the blank sections below whenever you prefer — and
whenever you have only one model available, since the same model must not do the
survey and then the audit. The Surveyor is a convenience; your confirmation is
the requirement.

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
