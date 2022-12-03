import string

import aocd

from adventofcode.helpers import chunk


def solution(input_string):
    sames = (set.intersection(*map(set, chunk(line, len(line)//2))).pop() for line in input_string.splitlines())
    return sum(string.ascii_letters.index(same) + 1 for same in sames)


if __name__ == "__main__":
    year, day, part = 2022, 3, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
