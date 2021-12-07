def solution(input_string):
    fish = list(map(int, input_string.split(',')))
    for iteration in range(80):
        new_fish = 0
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                new_fish += 1
                continue
            fish[i] = f - 1
        fish.extend(new_fish * [8])
    return (len(fish))


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
