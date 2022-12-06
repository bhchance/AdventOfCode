import aocd


def solution(input_string):
    pass


if __name__ == "__main__":
    year, day, part = 2022, 6, 1
    submit = False
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
