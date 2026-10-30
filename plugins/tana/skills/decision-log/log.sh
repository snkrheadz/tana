#!/usr/bin/env bash
# Append one row to a decision-log TSV.
# usage: log.sh FILE PHASE DECISION WHY EVIDENCE RESULT
set -eu

[ "$#" -eq 6 ] || { echo "usage: log.sh FILE PHASE DECISION WHY EVIDENCE RESULT" >&2; exit 2; }

file=$1; shift
mkdir -p "$(dirname "$file")"
[ -s "$file" ] || printf 'ts\tphase\tdecision\twhy\tevidence\tresult\n' >> "$file"

# Flatten whitespace controls; neutralise spreadsheet formula starters.
cell() {
  out=$(printf '%s' "$1" | tr '\t\r\n' '   ')
  case $out in
    [=+@-]*) out="'$out" ;;
  esac
  printf '%s' "$out"
}

row=$(date -u +%Y-%m-%dT%H:%M:%SZ)
for c in "$@"; do row="$row	$(cell "$c")"; done
printf '%s\n' "$row" >> "$file"
