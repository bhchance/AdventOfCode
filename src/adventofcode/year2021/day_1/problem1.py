def solution(input_string):
    nums = list(map(int, input_string.split()))
    return sum(1 for x, y in zip(nums[:-1], nums[1:]) if y > x)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
