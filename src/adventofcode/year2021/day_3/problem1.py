from collections import Counter


def solution(input_string):
    matrix = [list(x) for x in input_string.split()]
    transposed_matrix = list(zip(*matrix))
    gamma = epsilon = ""

    for row in transposed_matrix:
        two_most_common = Counter(row).most_common(2)
        gamma += str(two_most_common[0][0])
        epsilon += str(two_most_common[-1][0])
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
