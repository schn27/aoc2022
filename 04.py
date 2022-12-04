from aocd import lines
from aocd import submit
import re

fully_contain = 0
overlap = 0

for line in lines:
    a, b, c, d = map(int, re.findall("\d+", line))
    fully_contain += int((a >= c and b <= d) or (c >= a and d <= b))
    overlap += int((a >= c and a <= d) or (c >= a and c <= b))

submit(fully_contain, part="a")
submit(overlap, part="b")
