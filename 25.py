from aocd import lines
from aocd import submit
from itertools import zip_longest

def snafu_sum(a, b):
    carry = 0
    res = []

    for da, db in zip_longest(reversed(a), reversed(b), fillvalue=0):
        x = da + db + carry
        carry = -1 if x < -2 else 1 if x > 2 else 0
        res.append(x - carry * 5)

    if carry != 0:
        res.append(carry)

    return list(reversed(res))

SNAFU = ['=', '-', '0', '1', '2']

result = [0]

for line in lines:
    result = snafu_sum(result, list(map(lambda c: SNAFU.index(c) - 2, line)))

submit(''.join(map(lambda d: SNAFU[d + 2], result)), part='a')
