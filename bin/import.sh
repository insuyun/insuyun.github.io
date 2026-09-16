#!/bin/bash
set -euo pipefail

PUBS_ZIP_URL="https://github.com/kaist-hacking/kaist-hacking.github.io/archive/refs/heads/main.zip"
CSCONF_URL="https://raw.githubusercontent.com/emeryberger/csconferences/main/csconferences.csv"

# Run from the repository root (this script lives in bin/)
cd "$(dirname "$0")/.."

TMP_DIR=$(mktemp -d)
trap 'rm -rf "${TMP_DIR}"' EXIT

# Fetch and unpack the kaist-hacking site archive
echo "Downloading ${PUBS_ZIP_URL}"
curl -fsSL -o "${TMP_DIR}/main.zip" "${PUBS_ZIP_URL}"
unzip -q "${TMP_DIR}/main.zip" -d "${TMP_DIR}"

SOURCE_DIR=$(find "${TMP_DIR}" -maxdepth 1 -mindepth 1 -type d | head -1)
if [ -z "${SOURCE_DIR}" ]; then
    echo "Failed to locate the extracted archive directory" >&2
    exit 1
fi

# Create target directories if they don't exist
mkdir -p assets/pubs
mkdir -p static/pubs

# Sync assets/pubs
rsync -av "${SOURCE_DIR}/assets/pubs/" "assets/pubs/"

# Sync static/pubs
rsync -av "${SOURCE_DIR}/static/pubs/" "static/pubs/"

# Fetch conference metadata
echo "Downloading ${CSCONF_URL}"
curl -fsSL -o "${TMP_DIR}/csconferences.csv" "${CSCONF_URL}"
mv "${TMP_DIR}/csconferences.csv" bin/csconferences.csv

make
