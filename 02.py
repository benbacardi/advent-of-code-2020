#!/usr/bin/env python

import re
from collections import Counter

POLICY_REGEX = re.compile(r'(\d+)-(\d+) ([a-z])')

data = [x.split(':') for x in open('02.txt').readlines()]

valid = 0

for policy, password in data:
    letters = Counter(password)
    i_from, i_to, num = POLICY_REGEX.findall(policy)[0]
    if letters[num] in range(int(i_from), int(i_to)+1):
        valid += 1

print(valid)
