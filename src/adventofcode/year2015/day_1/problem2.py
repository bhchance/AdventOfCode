import functools
import sys


def solution(input_string):
    def move(moves, curr_floor=0):
        if curr_floor < 0:
            return len(input_string) - len(moves)
        else:
            func = functools.partial(
                move,
                moves=moves[1:],
                curr_floor=(curr_floor + [-1, 1][moves[0] == "("])
            )

            try:
                return func()
            except RecursionError:
                sys.setrecursionlimit(len(moves))
                return func()

    return move(input_string)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
