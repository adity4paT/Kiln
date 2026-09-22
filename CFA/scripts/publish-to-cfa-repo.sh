#!/usr/bin/env bash
#
# Publish this course to a standalone GitHub repository.
#
# The course was built inside another repository, so it lives in a subdirectory.
# This script copies it out into its own repository with a single clean commit
# and pushes it.
#
# Usage:
#   1. Create an EMPTY private repo on GitHub named CFA (no README, no .gitignore,
#      no licence — the "Add a README" checkbox must stay unchecked).
#   2. From the directory containing this script's parent:
#        ./scripts/publish-to-cfa-repo.sh <github-username>
#      or, to name the repo something else:
#        ./scripts/publish-to-cfa-repo.sh <github-username> <repo-name>
#
# Re-running the script is safe: it force-pushes a fresh single-commit history,
# so the target repo ends up matching this directory exactly.

set -euo pipefail

USER_NAME="${1:-}"
REPO_NAME="${2:-CFA}"
BRANCH="main"

if [[ -z "$USER_NAME" ]]; then
  echo "usage: $0 <github-username> [repo-name]" >&2
  echo "" >&2
  echo "example: $0 octocat" >&2
  echo "         $0 octocat cfa-level-1" >&2
  exit 64
fi

# Resolve the course root (the directory holding this script's parent).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURSE_ROOT="$(dirname "$SCRIPT_DIR")"

if [[ ! -f "$COURSE_ROOT/curriculum.json" ]]; then
  echo "error: $COURSE_ROOT does not look like the course root (no curriculum.json)" >&2
  exit 1
fi

REMOTE="${REMOTE_OVERRIDE:-git@github.com:${USER_NAME}/${REPO_NAME}.git}"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

echo "==> Course root : $COURSE_ROOT"
echo "==> Target      : $REMOTE"
echo "==> Branch      : $BRANCH"
echo ""

# Copy the course, excluding any git metadata and Python caches.
echo "==> Staging files"
tar -cf - -C "$COURSE_ROOT" \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='.DS_Store' \
    . | tar -xf - -C "$STAGE"

FILE_COUNT="$(find "$STAGE" -type f | wc -l | tr -d ' ')"
MODULE_COUNT="$(find "$STAGE/docs/topics" -name 'lm-*.md' | wc -l | tr -d ' ')"
echo "    $FILE_COUNT files, $MODULE_COUNT learning modules"

if [[ "$MODULE_COUNT" -ne 102 ]]; then
  echo "warning: expected 102 learning modules, found $MODULE_COUNT" >&2
fi

echo "==> Initialising repository"
git -C "$STAGE" init -q -b "$BRANCH"
git -C "$STAGE" add -A
git -C "$STAGE" -c user.useConfigOnly=false commit -q -m "CFA Level I: complete 150-day, 750-hour learning course

102 learning modules across 10 topic areas, keyed to the 2027 CFA Institute
Level I topic outlines and sequenced to a 150-day / 750-hour study plan.

  docs/orientation   exam overview, study method, calculator guide
  docs/study-plan    master plan, five month schedules, revision phase
  docs/topics        102 modules, 10 topic guides
  trackers           progress, daily log, weak areas
  resources          formula sheet, glossary, mock exam tracker
  scripts            progress.py"

echo "==> Pushing to $REMOTE"
git -C "$STAGE" remote add origin "$REMOTE"

# Retry the push on transient network failures: 2s, 4s, 8s, 16s.
DELAY=2
for ATTEMPT in 1 2 3 4 5; do
  if git -C "$STAGE" push -u --force origin "$BRANCH"; then
    echo ""
    echo "==> Done. https://github.com/${USER_NAME}/${REPO_NAME}"
    exit 0
  fi
  if [[ "$ATTEMPT" -eq 5 ]]; then
    break
  fi
  echo "    push failed (attempt $ATTEMPT) — retrying in ${DELAY}s" >&2
  sleep "$DELAY"
  DELAY=$(( DELAY * 2 ))
done

echo "" >&2
echo "error: push failed after 5 attempts." >&2
echo "" >&2
echo "Check that:" >&2
echo "  - the repo ${USER_NAME}/${REPO_NAME} exists and is empty" >&2
echo "  - your SSH key is registered with GitHub (ssh -T git@github.com)" >&2
echo "" >&2
echo "To use HTTPS instead of SSH, re-run with:" >&2
echo "  REMOTE_OVERRIDE=https://github.com/${USER_NAME}/${REPO_NAME}.git $0 $USER_NAME $REPO_NAME" >&2
exit 1
