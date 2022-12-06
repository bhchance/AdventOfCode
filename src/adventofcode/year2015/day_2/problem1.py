import math
from itertools import combinations


def solution(input_string):
    gifts = (g.split("x") for g in input_string.split("\n"))
    gift_sides = (list(map(math.prod, combinations(map(int, gift), 2))) for gift in gifts)
    return sum(sum(sides)*2 + min(sides) for sides in gift_sides)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
