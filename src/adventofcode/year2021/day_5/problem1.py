import itertools


def process_vertical(coord, matrix):
    for i in range(coord[0][1], coord[1][1] + 1):
        matrix[i][coord[0][0]] += 1


def process_horizontal(coord, matrix):
    for i in range(coord[0][0], coord[1][0] + 1):
        matrix[coord[0][1]][i] += 1


def solution(input_string):
    coords = []
    for line in input_string.split("\n"):
        start, stop = line.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        stop_x, stop_y = map(int, stop.split(","))
        coords.append(
            sorted(
                ((start_x, start_y), (stop_x, stop_y))
            )
        )

    matrix_width = max([coord[0][0] for coord in coords] + [coord[1][0] for coord in coords]) + 1
    matrix_height = max([coord[0][1] for coord in coords] + [coord[1][1] for coord in coords]) + 1
    matrix = [[0] * matrix_width for _ in range(matrix_height)]

    for coord in coords:
        if coord[0][0] == coord[1][0]:
            process_vertical(coord, matrix)
        if coord[0][1] == coord[1][1]:
            process_horizontal(coord, matrix)

    return sum([1 for x in itertools.chain.from_iterable(matrix) if x > 1])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
