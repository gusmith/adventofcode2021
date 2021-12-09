from src.day7.day7 import day7, day7_part2_brute_force

test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part1():
    optimal, fuel_consumption = day7(test_input)
    assert optimal == 2
    assert fuel_consumption == 37


def test_part2():
    optimal, fuel_consumption = day7_part2_brute_force(test_input)
    assert optimal == 5
    assert fuel_consumption == 168
