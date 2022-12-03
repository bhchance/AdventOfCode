import string
from functools import reduce

import aocd

from adventofcode.helpers import chunk

reduce


def solution(input_string):
    chunks = chunk(input_string.splitlines(), 3)
    total = 0
    for c in chunks:
        same = reduce(lambda x, y: x & y, map(set, c), set(string.ascii_letters)).pop()
        if same in string.ascii_lowercase:
            total += ord(same) - 96
        if same in string.ascii_uppercase:
            total += ord(same) - 38
    return total


if __name__ == "__main__":
    year, day, part = 2022, 3, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
