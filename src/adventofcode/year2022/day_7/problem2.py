from functools import cached_property
from itertools import chain

import aocd


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

        @cached_property
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

    def find_items(node, limit):
        dirs = [c for c in node.children if isinstance(c, Directory)]
        node = [node] if node.size >= limit else []
        return node + list(chain.from_iterable(map(lambda c: find_items(c, limit), dirs)))

    free_space = 70000000 - root.size
    need_to_free = 30000000 - free_space

    return min(find_items(root, need_to_free), key=lambda x: x.size).size


if __name__ == "__main__":
    year, day, part = 2022, 7, 2
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
