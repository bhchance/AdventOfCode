import aocd


def solution(input_string):
    pass


if __name__ == "__main__":
    year, day, part = 2022, _, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
