#!/usr/bin/env python

import re


PASSPORTS = [
    dict(map(lambda x: x.split(':'), pp.split())) for pp in
    open('04.txt').read().split('\n\n')
    if pp.strip()
]


def validate_height(height):
    try:
        num, unit = re.findall(r'^(\d+)(cm|in)$', height)[0]
    except IndexError:
        return False
    num = int(num)
    return (unit == 'cm' and 150 <= num <= 193) or (unit == 'in' and 59 <= num <= 76)


REQUIRED_FIELDS = {
    'byr': [
        lambda x: x.isdigit(),
        lambda x: 1920 <= int(x) <= 2002,
    ],
    'iyr': [
        lambda x: x.isdigit(),
        lambda x: 2010 <= int(x) <= 2020,
    ],
    'eyr': [
        lambda x: x.isdigit(),
        lambda x: 2020 <= int(x) <= 2030,
    ],
    'hgt': [
        validate_height,
    ],
    'hcl': [
        re.compile(r'^#[0-9a-f]{6}$').match,
    ],
    'ecl': [
        lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    ],
    'pid': [
        lambda x: len(x) == 9 and x.isdigit(),
    ],
}

valid = 0

DEBUG = False

for pp in PASSPORTS:

    if not REQUIRED_FIELDS.keys() - set(pp.keys()) == set():
        continue

    if all(test(pp[field]) for field, tests in REQUIRED_FIELDS.items() for test in tests):
        valid += 1
    else:
        if DEBUG:
            print(f'INVALID! {pp=}')
            for field, tests in REQUIRED_FIELDS.items():
                for test in tests:
                    if not test(pp[field]):
                        print(f'{field}: {pp[field]}')
            input()

print(valid)

print(sum(REQUIRED_FIELDS.keys() - set(pp.keys()) == set() for pp in PASSPORTS))
