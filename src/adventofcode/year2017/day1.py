new_dir_mapping = {
    ("N", "R"): "E",
    ("N", "L"): "W",
    ("E", "R"): "S",
    ("E", "L"): "N",
    ("S", "R"): "W",
    ("S", "L"): "E",
    ("W", "R"): "N",
    ("W", "L"): "S",
}


def calculate_distance(directions):
    current_direction = "N"
    distance = 0
    for direction in directions:
        turn_direction, blocks_to_travel = direction[0]
        blocks_to_travel = int(direction[1:])

        current_direction = new_dir_mapping[(current_direction, turn_direction)]

        if current_direction in ("N", "E"):
            distance += blocks_to_travel

        if current_direction in ("S", "W"):
            distance -= blocks_to_travel

    return abs(distance)


def test_scenario_1():
    assert calculate_distance(["R2", "L3"]) == 5


def test_scenario_2():
    assert calculate_distance(["R2", "R2", "R2"]) == 2


def test_scenario_3():
    assert calculate_distance(["R5", "L5", "R5", "R3"]) == 12
