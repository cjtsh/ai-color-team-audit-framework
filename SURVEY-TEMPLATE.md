# SURVEY-TEMPLATE.md — the survey form

<!-- Fill this in and save it as <repo>-survey.md in the target repository's root.
     It becomes the audit plan. How to fill it in: SURVEYOR.md. -->

## 1. Target and revision

- **Repository:**
- **Revision surveyed:** <!-- tag or commit hash -->
- **Date:**
- **Surveyed by:** <!-- model/tool. Must NOT be the model that runs the audit. -->

## 2. The declared assets (ranked)

<!-- 3-6, most valuable first. An asset is a thing an attacker could steal,
     destroy, alter, or act upon without authorization. -->

| Rank | Asset | What must NOT happen to it |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

## 3. The unforgivable acts (in plain words)

<!-- The one or two worst outcomes, in the owner's language, not in jargon. -->

1.
2.

## 4. Where the assets live

<!-- Enough for an agent to find them: paths, services, stores. -->

-

## 5. In scope

<!-- What the audit must cover. -->

-

## 6. Out of scope — and why

<!-- Deliberately excluded. Excluding something is fine; excluding it silently is not. -->

-

## 7. Not examined — and why

<!-- Things the surveyor could not or did not look at. This is the gap list the
     report's coverage section is built from. Do not leave it empty unless the
     survey was genuinely exhaustive, and say so if it was. -->

-

## 8. Questions for the owner

<!-- Anything the code cannot answer: business context, contractual obligations,
     which of two things is actually the more valuable. -->

-
