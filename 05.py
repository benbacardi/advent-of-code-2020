#!/usr/bin/env python


from itertools import dropwhile


def logic(ref, size, end_token):
    potential = list(range(size))
    for token in ref:
        start, end = None, len(potential) // 2
        if token == end_token:
            start, end = end, start
        potential = potential[start:end]
    return potential[0]


def calc_seat(ref):
    row = logic(ref[:7], 128, 'B')
    col = logic(ref[7:], 8, 'R')
    return row, col, row * 8 + col


data = [x.strip() for x in open('05.txt').readlines()]

ids = []
found = dict(((x, y), False) for x in range(128) for y in range(8))

for ref in data:
    row, col, sid = calc_seat(ref)
    ids.append(sid)
    found[(row, col)] = True

print(max(ids))

my_row, my_col = next(dropwhile(lambda x: x[1], dropwhile(lambda x: not x[1], reversed(list(dropwhile(lambda x: not x[1], found.items()))))))[0]
print(my_row * 8 + my_col)
