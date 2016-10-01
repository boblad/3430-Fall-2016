#!/usr/bin/python3
import sys
import re

for line in sys.stdin.readlines():
    match = re.findall('\d+', line)
    sys.stdout.write(match[-1] + '\n')
sys.stdout.flush()
