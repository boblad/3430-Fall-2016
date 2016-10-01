#!/usr/bin/python3
import sys
import re

sorted_lines = sorted([line.split() for line in sys.stdin.readlines()],
                      key=lambda x: int(x[1]), reverse=True)
[sys.stdout.write('{} {} \n'.format(ip, value)) for ip, value in sorted_lines]

sys.stdout.flush()
