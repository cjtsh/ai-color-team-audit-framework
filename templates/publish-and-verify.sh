#!/usr/bin/env bash
# publish-and-verify.sh — the anti-"going in circles" tool.
#
# Why this exists: during the framework's first real deployment, an agent
# claimed a document was published when the push had silently failed, and
# separately, injected text in tool output repeatedly asserted work was
# "already done and verified," causing the real verification to be skipped
# and re-skipped. Both failure modes are cured by one rule:
#
#   NOTHING IS PUBLISHED UNTIL THIS SCRIPT SAYS VERIFIED.
#
# What it does — all in one invocation, so no step can be interrupted
# halfway and reported as complete:
#   1. commit + push the current tree
#   2. poll the live URL until it serves
#   3. fetch the live bytes and compare SHA-256 to the local file
#   4. print VERIFIED or FAILED — the only two acceptable outcomes
#
# Usage:
#   ./publish-and-verify.sh <local-file> <public-url> [poll-seconds]
#
# Notes: macOS (shasum); on Linux substitute sha256sum. Commits the ENTIRE
# current tree (git add -A) — run from a clean tree or adjust to taste.
#
# Exit 0 = verified live and byte-identical. Anything else = not published.

set -euo pipefail

LOCAL_FILE="${1:?usage: publish-and-verify.sh <local-file> <public-url> [poll-seconds]}"
PUBLIC_URL="${2:?usage: publish-and-verify.sh <local-file> <public-url> [poll-seconds]}"
POLL_SECONDS="${3:-90}"

LOCAL_HASH="$(shasum -a 256 "$LOCAL_FILE" | awk '{print $1}')"
echo "local sha256: $LOCAL_HASH"

git add -A
git diff --cached --quiet && echo "nothing new to commit" || \
  git commit -m "Publish $(basename "$LOCAL_FILE")"
git push origin HEAD

echo "waiting ${POLL_SECONDS}s for the CDN..."
sleep "$POLL_SECONDS"

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
for attempt in 1 2 3; do
  STATUS="$(curl -sL -o "$TMP" -w '%{http_code}' "$PUBLIC_URL")" || STATUS=000
  LIVE_HASH="$(shasum -a 256 "$TMP" | awk '{print $1}')"
  if [ "$STATUS" = "200" ] && [ "$LIVE_HASH" = "$LOCAL_HASH" ]; then
    echo "VERIFIED: live ($PUBLIC_URL) is byte-identical to $LOCAL_FILE"
    rm -f "$TMP"; exit 0
  fi
  echo "attempt $attempt: HTTP $STATUS, live sha256 $LIVE_HASH"
  if [ "$attempt" -lt 3 ]; then echo "retrying in 30s"; sleep 30; fi
done

echo "FAILED: $PUBLIC_URL did not serve the local bytes (last: HTTP $STATUS, sha256 $LIVE_HASH)"
echo "The artifact is NOT verified as published. Do not report success."
rm -f "$TMP"; exit 1
