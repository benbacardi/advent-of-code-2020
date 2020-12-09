#!/usr/bin/env python

from itertools import combinations


LENGTH = 25
INPUT = [int(x.strip()) for x in open('09.txt').readlines() if x.strip()]

previous = INPUT[:LENGTH]

for num in INPUT[LENGTH:]:
    possibles = map(sum, combinations(previous, 2))
    if num not in possibles:
        break
    previous = previous[1:] + [num]

# Part 1
print(num)

# Part 2
INPUT_SIZE = len(INPUT)
final_result = None
for start in range(INPUT_SIZE):
    for length in range(INPUT_SIZE-start):
        query_range = INPUT[start:start+length]
        result = sum(query_range)
        if result == num:
            final_result = min(query_range) + max(query_range)
            break
        elif result > num:
            break
    if final_result:
        break
print(final_result)
