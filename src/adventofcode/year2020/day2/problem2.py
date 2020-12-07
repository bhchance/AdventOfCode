import re


def solution(input_string):
    return sum(
        (sum((password[int(start) - 1] == char, password[int(stop) - 1] == char)) == 1)
        for (_, start, _, stop, _, char, _, password, _) in [
            re.compile(r"(\d+)(-)(\d+)( )(\w)(: )(\w+)").split(i)
            for i in input_string.split("\n")
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
