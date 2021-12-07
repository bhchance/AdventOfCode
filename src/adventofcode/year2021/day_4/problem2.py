from itertools import chain


def check_board(board, move):
    for line in board:
        if all(isinstance(x, int) for x in line):
            return sum(map(int, filter(lambda x: isinstance(x, str), chain.from_iterable(board)))) * move
    for line in zip(*board):
        if all(isinstance(x, int) for x in line):
            return sum(map(int, filter(lambda x: isinstance(x, str), chain.from_iterable(board)))) * move
    return 0


def solution(input_string):
    moves, *boards = input_string.split("\n\n")
    moves = moves.split(",")
    boards = [[line.split() for line in board.split("\n")] for board in boards]

    winning_boards = []
    scores = []
    for move in moves:
        for board_index, board in enumerate(boards):
            if board_index in winning_boards:
                continue
            for line in board:
                for i, cell in enumerate(line):
                    if cell == move:
                        line[i] = int(cell)
            score = check_board(board, int(move))
            if score:
                scores.append(score)
                winning_boards.append(board_index)
    return scores[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
