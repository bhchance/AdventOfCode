import itertools

import aocd

from adventofcode.helpers import transpose_matrix, rotate_matrix, flip_matrix


def solution(input_string):
    tree_matrix = [list(line) for line in input_string.splitlines()]
    visibility_matrix = [[False for _ in row] for row in tree_matrix]

    def process_side(matrix):
        for i, row in enumerate(tree_matrix):
            highest_tree_seen = row[0]
            visibility_matrix[i][0] = True
            for j, tree in enumerate(row[1:], start=1):
                if tree > highest_tree_seen:
                    visibility_matrix[i][j] = True
                    highest_tree_seen = tree

    for _ in range(4):
        tree_matrix = rotate_matrix(tree_matrix)
        visibility_matrix = rotate_matrix(visibility_matrix)
        process_side(tree_matrix)

    flattened_matrix = list(itertools.chain.from_iterable(visibility_matrix))
    return sum(flattened_matrix)


if __name__ == "__main__":
    year, day, part = 2022, 8, 1
    submit = True
    answer = solution("""30373
25512
65332
33549
35390""")
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
