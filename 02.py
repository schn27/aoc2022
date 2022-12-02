from aocd import data
from aocd import submit

shape_score = {"A": 1, "B": 2, "C": 3}

outcome = {
    "A" : {"A": 3, "B": 6, "C": 0},
    "B" : {"A": 0, "B": 3, "C": 6},
    "C" : {"A": 6, "B": 0, "C": 3}}

def score(he_you):
    shape_coding = {"X": "A", "Y": "B", "Z": "C"}
    he, you = he_you
    you = shape_coding[you]
    return shape_score[you] + outcome[he][you]

def score2(he_result):
    result_coding = {"X": 0, "Y": 3, "Z": 6}
    he, result = he_result
    result = result_coding[result]
    shape = next(filter(lambda e: e[1] == result, outcome[he].items()))[0]
    return shape_score[shape] + result

strategy = list(map(lambda e: e.split(), data.split("\n")))

submit(sum(map(score, strategy)), part="a")
submit(sum(map(score2, strategy)), part="b")
