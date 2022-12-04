import itertools
from collections import Counter
from copy import copy

import aocd


def solution(input_string):
    def sets_overlap(set1, set2):
        return bool(set1 & set2)

    def pair_to_set(p):
        start, end = map(int, p.split("-"))
        return set(range(start, end + 1))

    pairs = (map(pair_to_set, pair.split(",")) for pair in input_string.splitlines())
    pairs_overlapping = filter(lambda p: sets_overlap(*p), pairs)

    return len(list(pairs_overlapping))


if __name__ == "__main__":
    year, day, part = 2022, 4, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
