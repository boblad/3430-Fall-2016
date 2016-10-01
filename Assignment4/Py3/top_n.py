#!/usr/bin/python3
import sys
import re

index = 0
n = int(sys.argv[1])
for line in sys.stdin.readlines():
    sys.stdout.write(line)
    if index == n - 1:
        break
    index = index + 1
sys.stdout.flush()
