import aocd


def solution(input_string):
    total_for_each_elf = [sum(map(int, x.split("\n"))) for x in input_string.split("\n\n")]
    return sum(sorted(total_for_each_elf)[-3:])


if __name__ == "__main__":
    year, day, part = 2022, 1, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
