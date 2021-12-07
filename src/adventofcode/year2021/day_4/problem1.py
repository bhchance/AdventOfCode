from itertools import chain


def check_board(board, move):
    for line in board:
        if all(isinstance(x, int) for x in line):
            return sum(map(int, filter(lambda x: isinstance(x, str), chain.from_iterable(board)))) * move
    for line in zip(*board):
        if all(isinstance(x, int) for x in line):
            return sum(map(int, filter(lambda x: isinstance(x, str), chain.from_iterable(board)))) * move


def solution(input_string):
    moves, *boards = input_string.split("\n\n")
    moves = moves.split(",")
    boards = [[line.split() for line in board.split("\n")] for board in boards]

    for move in moves:
        for board in boards:
            for line in board:
                for i, cell in enumerate(line):
                    if cell == move:
                        line[i] = int(cell)
            score = check_board(board, int(move))
            if score:
                return score


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
