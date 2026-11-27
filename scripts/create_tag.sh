#!/usr/bin/env bash

set -euo pipefail

latest=$(git tag --list 'v*' --sort=-version:refname | awk '/^v[0-9]+\.[0-9]+\.[0-9]+$/ && !found {print; found=1}')

if [[ -z "$latest" ]]; then
    latest="v0.0.0"
fi

IFS=. read -r major minor patch <<< "${latest#v}"

next="v${major}.${minor}.$((patch + 1))"

echo "Current version: $latest"
echo "Next version: $next"

if [[ "${1:-}" == "--dry-run" ]]; then
    exit 0
fi

if [[ -n $(git tag --list 'v*' --points-at HEAD) ]]; then
    echo "This commit already has a version tag."
    exit 0
fi

git tag -a "$next" -m "MarketPulse $next"
git push origin "refs/tags/$next"
