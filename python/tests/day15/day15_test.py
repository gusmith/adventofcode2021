from pathlib import Path

from pytest import fixture
from src.day15.day15 import Mapie, build_map_part2, load_input, part1, part2

path_input = Path(__file__).parent.joinpath("input.txt")
path_input2 = Path(__file__).parent.joinpath("input2.txt")


@fixture
def input_test_part1() -> Mapie:
    return load_input(path_input)


def test_part1(input_test_part1):
    risks = part1(input_test_part1)
    assert risks == 40


def test_mapie_2(input_test_part1):
    mapie_loaded = load_input(path_input2)
    mapie_computed = build_map_part2(input_test_part1)
    assert mapie_computed.max_x == mapie_loaded.max_x
    assert mapie_computed.max_y == mapie_loaded.max_y
    for key, value in mapie_loaded.mapie.items():
        assert value == mapie_computed.mapie[key], f"""Wrong at key {key}, loaded = {value},
         computed = {mapie_computed.mapie[key]}"""


def test_part2(input_test_part1):
    risks = part2(input_test_part1)
    assert risks == 315
