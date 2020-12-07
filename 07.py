#!/usr/bin/env python

import re

BAG_REGEX = re.compile(r'^(\w+ \w+)')
CONTAINS_REGEX = re.compile(r'(\d+) (\w+ \w+) bag')
SEARCH_BAG = 'shiny gold'

rules = [x.strip() for x in open('07.txt').readlines()]

bag_rules = {}

for rule in rules:
    bag_color = BAG_REGEX.findall(rule)[0]
    can_contain = CONTAINS_REGEX.findall(rule)
    bag_rules[bag_color] = dict((y, int(x)) for x, y in can_contain)


import json
print(json.dumps(bag_rules, indent=2))


# Part 1

def can_contain(bag, term):
    return term in bag_rules[bag] or any(can_contain(x, term) for x in bag_rules[bag])


print(sum(can_contain(bag, SEARCH_BAG) for bag in bag_rules))


# Part 2

def count_subbags(bag):
    count = 0
    for inner_bag, inner_count in bag_rules[bag].items():
        count += inner_count + (inner_count * count_subbags(inner_bag))
    return count


print(count_subbags('shiny gold'))
