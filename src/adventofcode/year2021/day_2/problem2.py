def solution(input_string):
    x = y = aim = 0

    for line in input_string.split("\n"):
        direction, distance = line.split()
        X = int(distance)
        if direction == "forward":
            x += X
            y += aim * X
        if direction == "up":
            aim -= X
        if direction == "down":
            aim += X

    return x * y


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
