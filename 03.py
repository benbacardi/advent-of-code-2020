#!/usr/bin/env python

GRID = [l.strip() for l in open('03.txt').read().strip().split()]
COL_REPEAT = len(GRID[0])

SLOPES = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

INC_ROW = 1
INC_COL = 3

total = 1

for INC_ROW, INC_COL in SLOPES:

    row = 0
    col = 0

    trees = 0

    while row < len(GRID) - 1:
        row = row + INC_ROW
        col = col + INC_COL
        if GRID[row][col % COL_REPEAT] == '#':
            trees += 1

    total *= trees

print(total)
