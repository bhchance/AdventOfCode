import pytest
from year2019.day1.problem1 import calculate_fuel_requirement
from year2019.day1.problem2 import calculate_fuel_for_fuel


@pytest.mark.parametrize("mass,fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583), ])
def test_calculate_fuel_requirement(mass, fuel):
    assert calculate_fuel_requirement(mass) == fuel


@pytest.mark.parametrize("mass,fuel", [(14, 2), (1969, 966), (100756, 50346), ])
def test_calculate_fuel_requirement(mass, fuel):
    assert calculate_fuel_for_fuel(mass) == fuel
