from functools import cached_property
from itertools import chain

import aocd


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


class Directory:
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children or []

    @cached_property
    def size(self):
        return sum(c.size for c in self.children)


def build_file_tree(commands):
    root = Directory(name="root")
    current_directory = root
    for line in commands:
        if line.startswith("$"):
            prompt, command, *target = line.split()
            if command == "cd":
                if target == [".."]:
                    current_directory = current_directory.parent
                else:
                    current_directory = next(filter(lambda c: c.name == target[0], current_directory.children))
        else:
            p1, p2 = line.split()
            if p1 == "dir":
                item = Directory(name=p2, parent=current_directory)
            else:
                item = File(name=p2, size=int(p1), parent=current_directory)
            if item.name not in {c.name for c in current_directory.children}:
                current_directory.children.append(item)

    return root


def solution(input_string):
    root = build_file_tree(input_string.splitlines()[1:])

    def find_items(node, comparison):
        dirs = [c for c in node.children if isinstance(c, Directory)]
        node = [node] if comparison(node.size) else []
        return node + list(chain.from_iterable(map(lambda c: find_items(c, comparison), dirs)))

    return sum(i.size for i in find_items(root, comparison=lambda n: n <= 100000))


if __name__ == "__main__":
    year, day, part = 2022, 7, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
