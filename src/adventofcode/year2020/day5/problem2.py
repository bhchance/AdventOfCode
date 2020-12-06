import math


def find_trees(course, x_move, y_move):
    course_height = len(course)
    course_width = len(course[0])

    x = 0
    trees = 0
    for y in range(0, course_height, y_move):
        if course[y][x % course_width] == "#":
            trees += 1
        x += x_move

    return trees


def solution(input_string):
    course = [list(line) for line in input_string.split("\n")]

    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    print(
        math.prod(
            map(lambda i: find_trees(course, *i), slopes)
        )
    )




if __name__ == '__main__':
    with open("input.txt") as f:
        solution(f.read().strip())

