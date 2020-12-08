#!/usr/bin/env python


# Part 1
def run(instructions, nop=None, jmp=None):

    seen = set()
    infinite = False
    line_ref = 0
    acc = 0

    while line_ref < len(instructions):
        if line_ref in seen:
            infinite = True
            break
        seen.add(line_ref)
        instruction, value = instructions[line_ref].split()
        value = int(value)
        if line_ref == nop:
            instruction = 'nop'
        elif line_ref == 'jmp':
            instruction == 'jmp'
        if instruction == 'acc':
            acc += value
            line_ref += 1
        elif instruction == 'nop':
            line_ref += 1
        elif instruction == 'jmp':
            line_ref += value

    return acc, not infinite


# Part 2
def fix(instructions):

    nops = [i for i, line in enumerate(instructions) if line.startswith('nop')]
    for nop in nops:
        acc, fixed = run(instructions, jmp=nop)
        if fixed:
            return acc

    jmps = [i for i, line in enumerate(instructions) if line.startswith('jmp')]
    for jmp in reversed(jmps):
        acc, fixed = run(instructions, nop=jmp)
        if fixed:
            return acc


instructions = [x.strip() for x in open('08.txt').readlines()]
print(run(instructions))
print(fix(instructions))
