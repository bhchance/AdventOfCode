import aocd

from adventofcode.helpers import sliding_window


def solution(input_string):
    size = 4
    return next((i, w) for i, w in enumerate(sliding_window(input_string, size), start=size) if len(set(w)) == size)[0]


if __name__ == "__main__":
    year, day, part = 2022, 6, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
