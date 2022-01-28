from src.day17.day17 import brute_force, compute_part1

test_target_area = {"x": (20, 30), "y": (-10, -5)}


def test_part1():
    expected = 45
    working_speeds = brute_force(test_target_area["x"], test_target_area["y"])
    assert compute_part1(working_speeds) == expected


def test_part2():
    expected = 112
    working_speeds = brute_force(test_target_area["x"], test_target_area["y"])
    assert len(working_speeds) == expected
