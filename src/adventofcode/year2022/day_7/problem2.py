import aocd

from adventofcode.year2022.day_7.problem1 import build_file_tree, find_items


def solution(input_string):
    root = build_file_tree(input_string.splitlines()[1:])

    free_space = 70000000 - root.size
    need_to_free = 30000000 - free_space

    return min(find_items(root, lambda n: n >= need_to_free), key=lambda x: x.size).size


if __name__ == "__main__":
    year, day, part = 2022, 7, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
