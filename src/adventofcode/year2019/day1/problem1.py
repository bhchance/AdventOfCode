def calculate_fuel_requirement(mass):
    return (mass // 3) - 2


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = map(int, f.read().split())

    print(sum(map(calculate_fuel_requirement, numbers)))
