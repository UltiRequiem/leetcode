#!/bin/bash

python3 build_list.py
deno fmt .
git add .
git commit -m "$1"
git push