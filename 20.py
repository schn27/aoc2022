from aocd import numbers
from aocd import submit

def mix(numbers, key=1, repeats=1):
    numbers = [v * key for v in numbers]
    sequence = [i for i in range(len(numbers))]

    for _ in range(repeats):
        for i in range(len(numbers)):
            pos = sequence.index(i)
            v = numbers[pos]
            new_pos = (pos + v) % (len(numbers) - 1)

            numbers.pop(pos)
            numbers.insert(new_pos, v)

            sequence.pop(pos)
            sequence.insert(new_pos, i)

    zero = numbers.index(0)
    return sum(map(lambda e: numbers[(zero + e) % len(numbers)], [1000, 2000, 3000]))

submit(mix(numbers), part='a')
submit(mix(numbers, 811589153, 10), part='b')
