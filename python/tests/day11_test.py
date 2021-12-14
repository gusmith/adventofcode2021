import copy
from typing import List

from pytest import fixture
from src.day11.day11 import one_step, part1, part2

INPUT_TEST = [
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
]


@fixture
def input_test() -> List[List[int]]:
    return copy.deepcopy(INPUT_TEST)


def test_part1(input_test):
    new_step, nb_explosion = one_step(input_test)
    after_step_1 = [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
    ]
    assert new_step == after_step_1
    assert nb_explosion == 0

    after_step_2 = [
        [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
        [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
        [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
        [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
        [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
        [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
        [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
        [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
        [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
        [8, 7, 0, 0, 0, 0, 6, 8, 4, 8],
    ]
    new_step, nb_explosion = one_step(after_step_1)
    assert new_step == after_step_2
    assert nb_explosion == 35

    after_step_3 = [
        [0, 0, 5, 0, 9, 0, 0, 8, 6, 6],
        [8, 5, 0, 0, 8, 0, 0, 5, 7, 5],
        [9, 9, 0, 0, 0, 0, 0, 0, 3, 9],
        [9, 7, 0, 0, 0, 0, 0, 0, 4, 1],
        [9, 9, 3, 5, 0, 8, 0, 0, 6, 3],
        [7, 7, 1, 2, 3, 0, 0, 0, 0, 0],
        [7, 9, 1, 1, 2, 5, 0, 0, 0, 9],
        [2, 2, 1, 1, 1, 3, 0, 0, 0, 0],
        [0, 4, 2, 1, 1, 2, 5, 0, 0, 0],
        [0, 0, 2, 1, 1, 1, 9, 0, 0, 0],
    ]
    new_step, nb_explosion = one_step(after_step_2)
    assert new_step == after_step_3
    assert nb_explosion == 45

    after_step_4 = [
        [2, 2, 6, 3, 0, 3, 1, 9, 7, 7],
        [0, 9, 2, 3, 0, 3, 1, 6, 9, 7],
        [0, 0, 3, 2, 2, 2, 1, 1, 5, 0],
        [0, 0, 4, 1, 1, 1, 1, 1, 6, 3],
        [0, 0, 7, 6, 1, 9, 1, 1, 7, 4],
        [0, 0, 5, 3, 4, 1, 1, 1, 2, 2],
        [0, 0, 4, 2, 3, 6, 1, 1, 2, 0],
        [5, 5, 3, 2, 2, 4, 1, 1, 2, 2],
        [1, 5, 3, 2, 2, 4, 7, 2, 1, 1],
        [1, 1, 3, 2, 2, 3, 0, 2, 1, 1],
    ]
    new_step, nb_explosion = one_step(after_step_3)
    assert new_step == after_step_4
    assert nb_explosion == 16

    total_nb_explosions = part1(input_test, 100)
    assert total_nb_explosions == 1656


def test_part2(input_test):
    sol = part2(input_test, 200)
    assert sol == 195
