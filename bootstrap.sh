#!/usr/bin/env bash
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$ROOT"
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 required"; exit 1; }
echo "[1/5] Build"
rm -rf dist
python3 scripts/build.py
echo "[2/5] Test"
python3 tests/test_build.py
echo "[3/5] Verify JSON"
python3 -c 'import json,pathlib; [json.loads(p.read_text()) for p in pathlib.Path("dist").glob("*.json")]; print("PASS: JSON valid")'
echo "[4/5] Package"
python3 scripts/package.py
echo "[5/5] SHA256"
python3 scripts/hash_artifact.py
printf '%s
' "READY" "Local: python3 -m http.server 8787 -d dist" "Deploy: point every iam.<domain> at the SAME deployment. Canonical remains https://iam.movingwithclarity.com/"
