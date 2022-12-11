from aocd import data
from aocd import submit
from copy import deepcopy
import re

def parse_monkey(data):
    lines = data.split('\n')
    items = list(map(int, re.findall(r'\d+', lines[1])))
    op = lines[2].split()[-2:]
    test_div = int(lines[3].split()[-1])
    throw_to = [int(lines[4].split()[-1]), int(lines[5].split()[-1])]
    return {'items': items, 'op': op, 'test_div': test_div, 'throw_to': throw_to, 'count': 0}

monkeys = data.split('\n\n')
monkeys = list(map(parse_monkey, monkeys))

def game(monkeys, turns, *, div_3):
    monkeys = deepcopy(monkeys)

    total_div = 1
    for div in map(lambda e: e['test_div'], monkeys):
        total_div *= div

    for turn in range(turns):
        for m in monkeys:
            items = m['items']
            m['items'] = []

            for item in items:
                m['count'] += 1

                arg = item if m['op'][1] == 'old' else int(m['op'][1])
                if m['op'][0] == '*':
                    item *= arg
                else:
                    item += arg

                if div_3:
                    item //= 3
                else:
                    item %= total_div

                test = item % m['test_div'] == 0

                monkeys[m['throw_to'][int(not test)]]['items'].append(item)

    monkeys.sort(reverse=True, key=lambda e: e['count'])
    return monkeys[0]['count'] * monkeys[1]['count']

submit(game(monkeys, 20, div_3=True), part='a')
submit(game(monkeys, 10000, div_3=False), part='b')
