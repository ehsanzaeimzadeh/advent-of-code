#/bin/bash
set -e
python3 -m venv .venv || rmm -rf .venv
source ./.venv/bin/activate
pip install -r requirement_dev.txt
echo "Activate python environment"
