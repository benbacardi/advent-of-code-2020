#!/usr/bin/env python

data = open('06.txt').read().split('\n\n')

# Part 1
print(sum(len(set(x.replace('\n', ''))) for x in data))

# Part 2
print(sum(len(set.intersection(*[set(y) for y in x.splitlines()])) for x in data))
