import aocd


def solution(input_string):
    return sum({
                   # losses
                   "A X": 0 + 3,
                   "B X": 0 + 1,
                   "C X": 0 + 2,
                   # ties
                   "A Y": 3 + 1,
                   "B Y": 3 + 2,
                   "C Y": 3 + 3,
                   # wins
                   "A Z": 6 + 2,
                   "B Z": 6 + 3,
                   "C Z": 6 + 1,
               }.get(line) for line in input_string.splitlines())


if __name__ == "__main__":
    year, day, part = 2022, 2, 2
    submit = True
    answer = solution(aocd.get_data(year=year, day=day))

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
