import itertools


def bisect(start, stop):
    mid_index = start + (stop - start) // 2
    return (start, mid_index), (mid_index + 1, stop)


def calculate_seat_id(row, column):
    return row * 8 + column


def create_calc_x(default_range, first_half_action_key, last_half_action_key):
    def calc_x(moves, seat_range=default_range):
        if not moves:
            return seat_range[0]
        first_half, last_half = bisect(*seat_range)
        first, *rest = moves
        if first == first_half_action_key:
            return calc_x(rest, first_half)
        if first == last_half_action_key:
            return calc_x(rest, last_half)

    return calc_x


calculate_row = create_calc_x((0, 127), "F", "B")
calculate_column = create_calc_x((0, 7), "L", "R")


def get_all_seats():
    seats_row_col = list(itertools.product(list(range(0, 127)), list(range(0, 7))))
    return map(lambda rc: calculate_seat_id(*rc), seats_row_col)


def solution(input_string):
    seat_ids = []
    for seat in input_string.split():
        front_back, left_right = seat[:7], seat[7:]
        row = calculate_row(front_back)
        column = calculate_column(left_right)
        seat_ids.append(calculate_seat_id(row, column))

    return (set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)).pop()


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))
