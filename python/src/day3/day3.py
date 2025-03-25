from pathlib import Path
from typing import List

from src.utils import get_csv_line_iterator

path_input = Path(__file__).parent.joinpath("input.csv")


def _bit_list_to_int(bit_list: List[int]):
    val = 0
    for bit in bit_list:
        val = (val << 1) | bit
    return val


def day3_1():
    counter_bits = None
    counter_words = 0
    for row in get_csv_line_iterator(path_input):
        value = row[0]
        if counter_bits is None:
            counter_bits = [0] * len(value)
        for index, character in enumerate(value):
            if character == "1":
                counter_bits[index] += 1
        counter_words += 1
    gamma_list = [1 if 2 * e > counter_words else 0 for e in counter_bits]
    epsilon_list = [1 - e for e in gamma_list]
    gamma = _bit_list_to_int(gamma_list)
    epsilon = _bit_list_to_int(epsilon_list)
    power = gamma * epsilon
    return gamma, epsilon, power


def _bit_criteria(row: str, index: int, bit: bool) -> bool:
    return row[index] == "1" if bit else row[index] == "0"


def _most_common_value(rows, index) -> bool:
    counter_1 = 0
    counter_0 = 0
    for row in rows:
        if row[index] == "1":
            counter_1 += 1
        else:
            counter_0 += 1
    return counter_1 >= counter_0


def _get_value(computation_type: str) -> int:
    filtered_rows = [a[0] for a in list(get_csv_line_iterator(path_input))]
    use_most_common_value = computation_type == "oxygen"
    for i in range(len(filtered_rows[0])):
        most_common_value = _most_common_value(filtered_rows, i)
        value_to_use = most_common_value if use_most_common_value else not most_common_value
        filtered_rows = [row for row in filtered_rows if _bit_criteria(row, i, value_to_use)]
        if len(filtered_rows) <= 1:
            break
    assert len(filtered_rows) == 1
    return int(filtered_rows[0], 2)


def day3_2():
    oxygen = _get_value("oxygen")
    co2 = _get_value("co2")
    life_support = oxygen * co2
    return oxygen, co2, life_support


if __name__ == "__main__":
    print("# Part 1")
    _gamma, _epsilon, _power = day3_1()
    print(f"gamma {_gamma}, epsilon {_epsilon}, power {_power}")

    print("# Part 2")
    _oxygen, _co2, _life_support = day3_2()
    print(f"oxygen {_oxygen}, co2 {_co2}, life support {_life_support}")
