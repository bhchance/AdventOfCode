import itertools


def solution(input_string):
    nums = list(map(int, input_string.split(',')))
    xs = [itertools.product(nums, [num]) for num in range(max(nums)+1)]
    return min(sum((lambda x, y: abs(x - y))(x, y) for (x, y) in x) for x in xs)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
