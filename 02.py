from aocd import lines
from aocd import submit

shape_score = {"A": 1, "B": 2, "C": 3}

outcome = {
    "A" : {"A": 3, "B": 6, "C": 0},
    "B" : {"A": 0, "B": 3, "C": 6},
    "C" : {"A": 6, "B": 0, "C": 3}}

def score(line):
    shape_coding = {"X": "A", "Y": "B", "Z": "C"}
    he, you = line.split()
    you = shape_coding[you]
    return shape_score[you] + outcome[he][you]

def score2(line):
    result_coding = {"X": 0, "Y": 3, "Z": 6}
    he, result = line.split()
    result = result_coding[result]
    shape = next(filter(lambda e: e[1] == result, outcome[he].items()))[0]
    return shape_score[shape] + result

submit(sum(map(score, lines)), part="a")
submit(sum(map(score2, lines)), part="b")
