#!/usr/bin/env bash
# Build all weekly module/assignment PDFs plus the end-of-semester papers.
# Non-destructive: do not remove tracked output files or hide build failures.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-$REPO_ROOT/.venv/bin/python}"
if [[ ! -x "$PYTHON" ]]; then
  echo 'Create .venv and install requirements.txt first (see README.md).' >&2
  exit 1
fi
cd "$REPO_ROOT"
"$PYTHON" - <<'PY'
import sys
sys.path.insert(0, 'tools')
from common import register_fonts, make_seal, make_shield, make_wordmark
register_fonts()
make_seal(); make_shield(); make_wordmark()
PY
"$PYTHON" - <<'PY'
import importlib
import sys
sys.path.insert(0, 'tools')
for week in range(1, 17):
    visuals = importlib.import_module('visuals' if week == 1 else f'week{week}_visuals')
    for fn in visuals.ALL:
        fn()
    if week == 1:
        import build_pdf
        print(build_pdf.build())
    else:
        module = importlib.import_module(f'w{week}_pdf')
        print(module.build(module.CFG, module.story))
    assignment = importlib.import_module(f'w{week}_assignment_pdf')
    print(assignment.build(assignment.CFG, assignment.story))
PY
"$PYTHON" tools/build_exam_docs.py
printf '\nAll weekly and examination PDFs built under %s/output\n' "$REPO_ROOT"
printf 'Review intentional changes, rebuild Word/PowerPoint copies, and refresh checksums before committing.\n'
