#!/bin/bash

if [ ! -e public/.git ]; then
  rm -rf public
  git clone -b publish git@github.com:insuyun/insuyun.github.io.git public
fi

make

cd public
git add .
git commit -m "$(date)"
git push
