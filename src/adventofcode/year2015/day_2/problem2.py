import math
from itertools import combinations


def solution(input_string):
    gifts = (list(map(int, g.split("x"))) for g in input_string.split("\n"))
    return sum(
        sum(min(combinations(gift, 2)))*2 + math.prod(gift)
        for gift in gifts
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
