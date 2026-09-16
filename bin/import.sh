#!/bin/bash
set -euo pipefail

PUBS_REPO="https://github.com/kaist-hacking/kaist-hacking.github.io.git"
CSCONF_REPO="https://github.com/emeryberger/csconferences.git"

# Run from the repository root (this script lives in bin/)
cd "$(dirname "$0")/.."

REPO_DIR="repo"
mkdir -p "${REPO_DIR}"

# Clone the repository on first use, otherwise pull the latest changes
sync_repo() {
    local url=$1
    local dir=$2

    if [ -d "${dir}/.git" ]; then
        echo "Updating ${dir}"
        git -C "${dir}" pull --ff-only
    else
        echo "Cloning ${url} into ${dir}"
        git clone --depth 1 "${url}" "${dir}"
    fi
}

PUBS_DIR="${REPO_DIR}/kaist-hacking.github.io"
CSCONF_DIR="${REPO_DIR}/csconferences"

sync_repo "${PUBS_REPO}" "${PUBS_DIR}"
sync_repo "${CSCONF_REPO}" "${CSCONF_DIR}"

# Create target directories if they don't exist
mkdir -p assets/pubs
mkdir -p static/pubs

# Sync assets/pubs
rsync -av "${PUBS_DIR}/assets/pubs/" "assets/pubs/"

# Sync static/pubs
rsync -av "${PUBS_DIR}/static/pubs/" "static/pubs/"

# Copy conference metadata
cp "${CSCONF_DIR}/csconferences.csv" bin/csconferences.csv

make
