import dataclasses
from itertools import groupby
from typing import List

import aocd
from attr import attr


def solution(input_string):
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

        @property
        def size(self):
            return sum(c.size for c in self.children)

    root, *rest = input_string.splitlines()
    root = Directory(name="root")
    current_directory = root
    for line in rest:
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

    def count_items(node, limit=100000):
        dirs = [c for c in node.children if isinstance(c, Directory)]
        size = node.size if node.size <= limit else 0
        return size + sum(map(lambda c: count_items(c, limit), dirs))

    return count_items(root)


if __name__ == "__main__":
    year, day, part = 2022, 7, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
