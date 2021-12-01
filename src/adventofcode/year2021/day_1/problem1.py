def solution(input_string):
    nums = list(map(int, input_string.split()))
    return sum(1 for _ in filter(lambda xs: xs[1] > xs[0], zip(nums[:-1], nums[1:])))


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
