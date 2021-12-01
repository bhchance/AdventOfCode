def solution(input_string):
    nums = list(map(int, input_string.split()))
    return sum(1 for x in range(len(nums[:-1])) if nums[x + 1] > nums[x])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
