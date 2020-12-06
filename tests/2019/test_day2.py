import pytest

from year2019.day2.problem1 import IntcodeProgram


@pytest.mark.parametrize(
    "numbers,exit_value",
    [
        ([1, 0, 0, 0, 99], 2),
        ([2,3,0,3,99], 6),
        ([2, 4, 4, 5, 99, 0], 9801),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], 30),
    ]
)
def test_intcode_program(numbers, exit_value):
    assert IntcodeProgram(numbers).run() == exit_value
