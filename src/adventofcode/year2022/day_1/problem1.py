from collections import defaultdict

import aocd


def solution(input_string):
    total_for_each_elf = [sum(map(int, x.split("\n"))) for x in input_string.split("\n\n")]
    return max(total_for_each_elf)


if __name__ == "__main__":
    year, day, part = 2022, 1, 1
    submit = True
    answer = solution(aocd.get_data(year=year, day=day))

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
