import itertools
from collections import Counter
from copy import copy

import aocd


def solution(input_string):
    def sets_fully_overlap(set1, set2):
        return bool(set1 & set2)

    def pair_to_set(p):
        start, end = map(int, p.split("-"))
        return set(range(start, end + 1))

    counter = Counter()
    for pair in input_string.splitlines():
        sec1, sec2 = map(pair_to_set, pair.split(","))
        counter[sets_fully_overlap(sec1, sec2)] += 1

    return counter[True]


if __name__ == "__main__":
    year, day, part = 2022, 4, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
