import string

import aocd



def solution_part1(input_string):
    return sum(int(line[0] + line[-1]) for line in "".join(filter(lambda c: c in string.digits + "\n", input_string)).splitlines())


def solution_part2(input_string):
    mapping = {d: d for d in string.digits} | {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    line_values = []
    for line in input_string.splitlines():
        first_finds = {index: item for item in mapping.keys() if (index := line.find(item) != -1)}
        last_finds = {index: item for item in mapping.keys() if (index := line.rfind(item) != -1)}
        line_values.append(mapping[first_finds[min(first_finds)]] + mapping[last_finds[max(last_finds)]])
    return sum(map(int, line_values))


if __name__ == "__main__":
    year, day, part = 2023, 1, 2
    submit = True

    answer = solution_part2(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
