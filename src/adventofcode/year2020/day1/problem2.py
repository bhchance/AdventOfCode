def calculate_fuel_requirement(mass):
    if mass <= 0:
        return 0
    return mass + calculate_fuel_requirement(mass // 3 - 2)


def calculate_fuel_for_fuel(mass):
    return calculate_fuel_requirement(mass) - mass


assert calculate_fuel_for_fuel(14) == 2
assert calculate_fuel_for_fuel(1969) == 966
assert calculate_fuel_for_fuel(100756) == 50346


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = map(int, f.read().split())

    print(sum(map(calculate_fuel_for_fuel, numbers)))
