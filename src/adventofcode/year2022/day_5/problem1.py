import aocd
from parse import parse

from adventofcode.helpers import chunk


def solution(input_string):
    map_input, moves_list = map(lambda x: x.splitlines(), input_string.split("\n\n"))
    map_matrix = reversed([list(chunk(line, 4)) for line in map_input])
    transposed_map_matrix = list(zip(*map_matrix))

    # strip "empty" cells ('    ') from matrix
    list_of_stacks = [[cell.strip() for cell in row if cell.strip()] for row in transposed_map_matrix]
    for move in moves_list:
        count, source, dest = map(int, parse("move {} from {} to {}", move).fixed)
        for _ in range(count):
            list_of_stacks[dest - 1].append(list_of_stacks[source - 1].pop())

    return ''.join(stack[-1] for stack in list_of_stacks).replace("[", "").replace("]", "")


if __name__ == "__main__":
    year, day, part = 2022, 5, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
