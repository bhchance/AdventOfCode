import aocd


def solution(input_string):
    nums = list(map(int, input_string.split()))
    chunks_summed = list(map(sum, zip(nums[:-2], nums[1:-1], nums[2:])))
    return sum(1 for _ in filter(lambda xs: xs[1] > xs[0], zip(chunks_summed[:-1], chunks_summed[1:])))


if __name__ == "__main__":
    year, day, part = 2022, 2, 2
    submit = False
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)
