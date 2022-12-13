from aocd import lines
from aocd import submit
import json
from itertools import zip_longest
from functools import cmp_to_key

LESS, EQUAL, GREATER = -1, 0, 1

def compare(a, b):
    for a, b in zip_longest(a, b):
        if a is None:
            return EQUAL if b is None else LESS
        elif b is None:
            return GREATER
        elif isinstance(a, int) and isinstance(b, int) and a != b:
            return LESS if a < b else GREATER
        elif isinstance(a, list) or isinstance(b, list):
            a = [a] if isinstance(a, int) else a
            b = [b] if isinstance(b, int) else b
            res = compare(a, b)
            if res != EQUAL:
                return res

    return EQUAL

packets = list(map(lambda e: json.loads(e), filter(lambda e: len(e) > 0, lines)))

sum_indexes = 0

for i, pair in enumerate(zip(* [iter(packets)] * 2)):
    if compare(*pair) == LESS:
        sum_indexes += (i + 1)

submit(sum_indexes, part='a')

div_1, div_2 = [[2]], [[6]]

packets.append(div_1)
packets.append(div_2)

packets.sort(key=cmp_to_key(compare))

submit((packets.index(div_1) + 1) * (packets.index(div_2) + 1), part='b')
