from collections import Counter


def solution(input_string):
    fish = Counter({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0})
    fish.update(Counter(map(int, input_string.split(','))))
    for iteration in range(256):
        new_fish = 0
        for lifecycle, count in sorted(fish.items()):
            if lifecycle == 0:
                new_fish = count
            else:
                fish[lifecycle - 1] = count

        fish[8] = new_fish
        fish[6] += new_fish

    return sum(fish.values())


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
