def solution(input_string):
    return sum(
        map(
            len,
            (
                set.intersection(*[set(y) for y in x.split()])
                for x in input_string.split("\n\n")
            ),
        )
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
