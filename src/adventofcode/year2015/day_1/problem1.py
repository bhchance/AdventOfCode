def solution(input_string):
    return sum([-1, 1][x == "("] for x in input_string)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
