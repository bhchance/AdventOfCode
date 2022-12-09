import itertools

import aocd
import math


def process_sight_line(sight_line):
    first, *rest = sight_line
    for i, height in enumerate(rest, start=1):
        if height >= first:
            return i
    return len(rest)


def calculate_scenic_score(coords, matrix):
    x, y = coords
    sight_line_right = matrix[y][x:len(matrix[0])]
    sight_line_left = reversed(matrix[y][0:x + 1])
    sight_line_up = reversed([matrix[i][x] for i in range(0, y + 1)])
    sight_line_down = [matrix[i][x] for i in range(y, len(matrix))]
    return math.prod(map(process_sight_line, (sight_line_right, sight_line_left, sight_line_up, sight_line_down)))


def solution(input_string):
    tree_matrix = [list(line) for line in input_string.splitlines()]

    pairs = itertools.product(range(len(tree_matrix[0])), range(len(tree_matrix)))
    return max(map(lambda p: calculate_scenic_score(p, tree_matrix), pairs))


if __name__ == "__main__":
    year, day, part = 2022, 8, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
