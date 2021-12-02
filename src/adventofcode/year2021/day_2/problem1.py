def solution(input_string):
    x = y = 0

    for line in input_string.split("\n"):
        direction, distance = line.split()
        distance = int(distance)
        if direction == "forward":
            x += distance
        if direction == "up":
            y -= distance
        if direction == "down":
            y += distance

    return x * y


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
