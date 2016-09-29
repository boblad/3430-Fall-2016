#!/usr/bin/python
import sys
import re

for line in sys.stdin.readlines():
    numberList = re.findall('\d+', line)
    ip = line.split(' ', 1)[0]
    sys.stdout.write('{} {} \n'.format(ip, numberList[-1]))
sys.stdout.flush()
