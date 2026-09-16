#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <source_directory>"
    exit 1
fi

SOURCE_DIR=$1

# Create target directories if they don't exist
mkdir -p assets/pubs
mkdir -p static/pubs

# Sync assets/pubs
rsync -av "${SOURCE_DIR}/assets/pubs/" "assets/pubs/"

# Sync static/pubs
rsync -av "${SOURCE_DIR}/static/pubs/" "static/pubs/"

make
