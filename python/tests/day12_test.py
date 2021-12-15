import copy
from typing import List, Tuple

from pytest import fixture
from src.day12.day12 import part1, part2

INPUT_TEST: List[Tuple[str, str]] = [
    ("start", "A"),
    ("start", "b"),
    ("A", "c"),
    ("A", "b"),
    ("b", "d"),
    ("A", "end"),
    ("b", "end"),
]

INPUT_TEST2: List[Tuple[str, str]] = [
    ("dc", "end"),
    ("HN", "start"),
    ("start", "kj"),
    ("dc", "start"),
    ("dc", "HN"),
    ("LN", "dc"),
    ("HN", "end"),
    ("kj", "sa"),
    ("kj", "HN"),
    ("kj", "dc"),
]

INPUT_TEST3: List[Tuple[str, str]] = [
    ("fs", "end"),
    ("he", "DX"),
    ("fs", "he"),
    ("start", "DX"),
    ("pj", "DX"),
    ("end", "zg"),
    ("zg", "sl"),
    ("zg", "pj"),
    ("pj", "he"),
    ("RW", "he"),
    ("fs", "DX"),
    ("pj", "RW"),
    ("zg", "RW"),
    ("start", "pj"),
    ("he", "WI"),
    ("zg", "he"),
    ("pj", "fs"),
    ("start", "RW"),
]


@fixture
def input_test() -> List[Tuple[str, str]]:
    return copy.deepcopy(INPUT_TEST)


@fixture
def input_test2() -> List[Tuple[str, str]]:
    return copy.deepcopy(INPUT_TEST2)


@fixture
def input_test3() -> List[Tuple[str, str]]:
    return copy.deepcopy(INPUT_TEST3)


def test_part1(input_test, input_test2, input_test3):
    nb_paths = part1(input_test)
    assert nb_paths == 10

    nb_paths = part1(input_test2)
    assert nb_paths == 19

    nb_paths = part1(input_test3)
    assert nb_paths == 226


def test_part2(input_test, input_test2, input_test3):
    nb_paths = part2(input_test)
    assert nb_paths == 36

    nb_paths = part2(input_test2)
    assert nb_paths == 103

    nb_paths = part2(input_test3)
    assert nb_paths == 3509
