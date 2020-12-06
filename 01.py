#!/usr/bin/env python

from itertools import combinations
from math import prod

COUNT = 3

data = [int(x) for x in open('01.txt').readlines()]

for parts in combinations(data, COUNT):
    if sum(parts) == 2020:
        print(prod(parts))
