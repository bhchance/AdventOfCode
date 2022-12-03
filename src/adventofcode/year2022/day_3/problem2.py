import string
from functools import reduce

import aocd

from adventofcode.helpers import chunk


def solution(input_string):
    chunks = chunk(input_string.splitlines(), 3)
    sames = (set.intersection(*map(set, c)).pop() for c in chunks)
    return sum(string.ascii_letters.index(same) + 1 for same in sames)


if __name__ == "__main__":
    year, day, part = 2022, 3, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
