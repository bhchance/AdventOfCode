import itertools
import math


def solution(input_string):
    return math.prod(
        {
            sum(xs): xs
            for xs in itertools.combinations((map(int, input_string.split("\n"))), 2)
        }.get(2020)
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
