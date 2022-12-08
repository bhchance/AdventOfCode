import functools

import aocd
import math


def calculate_scenic_score_direction(direction, coords, matrix):
    def process_sight_line(sight_line):
        first, *rest = sight_line
        for i, height in enumerate(rest, start=1):
            if height >= first:
                return i
        return len(rest)

    x, y = coords
    if direction == "up":
        return process_sight_line(reversed([matrix[i][x] for i in range(0, y + 1)]))

    if direction == "down":
        return process_sight_line([matrix[i][x] for i in range(y, len(matrix))])

    if direction == "left":
        return process_sight_line(reversed(matrix[y][0:x + 1]))

    if direction == "right":
        return process_sight_line(matrix[y][x:len(matrix[0])])


def calculate_scenic_score(coords, matrix):
    func = functools.partial(calculate_scenic_score_direction, coords=coords, matrix=matrix)
    return math.prod(map(func, ("up", "down", "left", "right")))


def solution(input_string):
    tree_matrix = [list(line) for line in input_string.splitlines()]

    calculate_scenic_score((2, 1), tree_matrix)

    scores = {0}
    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[0])):
            scores.add(calculate_scenic_score((i, j), tree_matrix))
    return max(scores)


if __name__ == "__main__":
    year, day, part = 2022, 8, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
