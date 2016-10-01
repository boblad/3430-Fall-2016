#!/usr/bin/python3
import sys
import re

for line in sys.stdin.readlines():
    numberList = re.findall('\d+', line)
    ip = line.split(' ', 1)[0]
    if numberList[-2] == sys.argv[1]:
        sys.stdout.write(line)
sys.stdout.flush()
