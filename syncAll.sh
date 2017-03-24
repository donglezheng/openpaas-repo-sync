#!/bin/bash
echo */ | tr ' ' '\n' | while read x; do (
    cd $x
    python ../gsync.py
) done
