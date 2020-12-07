import re


def solution(input_string):
    print(
        sum(
            (password.count(char) in range(int(start), int(stop) + 1))
            for (_, start, _, stop, _, char, _, password, _) in [
                re.compile(r"(\d+)(-)(\d+)( )(\w)(: )(\w+)").split(i)
                for i in input_string.split("\n")
            ]
        )
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        solution(f.read().strip())
