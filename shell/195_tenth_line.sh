#!/bin/sh
sed -n '10p' file.txt
# Alternative
# awk 'NR==10' file.txt
