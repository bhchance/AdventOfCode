import itertools


def process_vertical(coord):
    coord = sorted(coord)
    points_to_update = []
    for i in range(coord[0][1], coord[1][1] + 1):
        points_to_update.append((coord[0][0], i))
    return points_to_update


def process_diagonal(coord):
    ((x1, y1), (x2, y2)) = coord
    m = (y1 - y2) / (x1 - x2)
    b = (x1 * y2 - x2 * y1) / (x1 - x2)

    points_to_update = []
    if x1 < x2:
        for x in range(x1, x2 + 1):
            y = m * x + b
            points_to_update.append((int(x), int(y)))
    if x1 > x2:
        for x in range(x1, x2 - 1, -1):
            y = m * x + b
            points_to_update.append((int(x), int(y)))
    return points_to_update


def solution(input_string):
    coords = []
    for line in input_string.split("\n"):
        start, stop = line.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        stop_x, stop_y = map(int, stop.split(","))
        coords.append(
            ((start_x, start_y), (stop_x, stop_y))
        )

    matrix_width = max([coord[0][0] for coord in coords] + [coord[1][0] for coord in coords]) + 1
    matrix_height = max([coord[0][1] for coord in coords] + [coord[1][1] for coord in coords]) + 1
    matrix = [[0] * matrix_width for _ in range(matrix_height)]

    for coord in coords:
        if coord[0][0] == coord[1][0]:
            points_to_update = process_vertical(coord)
        else:
            points_to_update = process_diagonal(coord)
        for (x, y) in points_to_update:
            matrix[x][y] += 1
    return sum(1 for x in itertools.chain.from_iterable(matrix) if x > 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
