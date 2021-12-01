def solution(input_string):
    nums = list(map(int, input_string.split()))
    chunks_summed = list(map(sum, [nums[i:i + 3] for i in range(len(nums[:-2]))]))
    return sum(1 for x in range(len(chunks_summed[:-1])) if chunks_summed[x + 1] > chunks_summed[x])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
