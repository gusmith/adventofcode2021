import copy
from typing import Dict

from pytest import fixture
from src.day14.day14 import part1, split_str_into_map_binoms

INPUT_TEST_PART1 = "NNCB"
INPUT_TEST_PART2: Dict[str, str] = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}


@fixture
def input_test_part1() -> str:
    return INPUT_TEST_PART1


@fixture
def input_test_part2() -> Dict[str, str]:
    return copy.deepcopy(INPUT_TEST_PART2)


def test_splitter(input_test_part1):
    expected = {"NN": 1, "NC": 1, "CB": 1}
    assert split_str_into_map_binoms(input_test_part1) == expected


def test_part1(input_test_part1, input_test_part2):
    counts = part1(input_test_part1, input_test_part2, 10)
    assert counts == 1588


def test_part2(input_test_part1, input_test_part2):
    counts = part1(input_test_part1, input_test_part2, 40)
    assert counts == 2188189693529
