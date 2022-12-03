from aocd import lines
from aocd import submit

def get_wrong_item(rucksack):
    sz = len(rucksack) // 2
    return set(rucksack[:sz]).intersection(rucksack[sz:]).pop()

def get_priority(item):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(item) + 1

wrong_items = map(get_wrong_item, lines)
submit(sum(map(get_priority, wrong_items)), part="a")

def get_badge(group):
    return set(group[0]).intersection(group[1]).intersection(group[2]).pop()

it = iter(lines)
groups = zip(it, it, it)
badges = map(get_badge, groups)
submit(sum(map(get_priority, badges)), part="b")
