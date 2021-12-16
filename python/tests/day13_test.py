import copy
from typing import Set, Tuple

from pytest import fixture
from src.day13.day13 import part1

INPUT_TEST: Set[Tuple[int, int]] = {
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
}
INPUT_FOLD_1: Tuple[str, int] = ("y", 7)
INPUT_FOLD_2: Tuple[str, int] = ("x", 5)


@fixture
def input_test() -> Set[Tuple[int, int]]:
    return copy.deepcopy(INPUT_TEST)


@fixture
def input_fold_1():
    return copy.deepcopy(INPUT_FOLD_1)


@fixture
def input_fold_2():
    return copy.deepcopy(INPUT_FOLD_2)


def test_part1(input_test, input_fold_1):
    list_points = part1(input_test, input_fold_1)
    assert len(list_points) == 17
