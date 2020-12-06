#!/usr/bin/env python

import re

POLICY_REGEX = re.compile(r'(\d+)-(\d+) ([a-z])')

data = [map(str.strip, x.split(':')) for x in open('02.txt').readlines()]

valid = 0

for policy, password in data:
    pos_1, pos_2, letter = POLICY_REGEX.findall(policy)[0]
    letters = password[int(pos_1)-1] + password[int(pos_2)-1]
    if letter in letters and letters != f'{letter}{letter}':
        valid += 1

print(valid)
