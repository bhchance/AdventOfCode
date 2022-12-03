import string

import aocd


def solution(input_string):
    total = 0
    for line in input_string.splitlines():
        same = (set(line[:len(line) // 2]) & set(line[len(line) // 2:])).pop()
        if same in string.ascii_lowercase:
            total += ord(same) - 96
        if same in string.ascii_uppercase:
            total += ord(same) - 38
    return total


if __name__ == "__main__":
    year, day, part = 2022, 3, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
