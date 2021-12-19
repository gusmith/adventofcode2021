from functools import reduce
from pathlib import Path
from typing import List, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")

HEX_TO_BITS = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def load_input() -> str:
    with open(path_input, "r") as f:
        sol = f.readline().strip()
    return sol


def transform_hexa_to_bits(str_hexa: str):
    return "".join([HEX_TO_BITS[c] for c in str_hexa])


def get_version_and_id(str_bits: str) -> Tuple[int, int, str]:
    """Get the version, the packet id, and the remaining bits."""
    version = int(str_bits[0:3], 2)
    p_id = int(str_bits[3:6], 2)
    return version, p_id, str_bits[6:]


def handle_literal_bits(bits_str: str) -> Tuple[int, str]:
    sol = []
    i = 0
    for i in range(0, len(bits_str), 5):
        sol.append(bits_str[i + 1 : i + 5])
        if bits_str[i] == "0":
            break
    remaining_string = bits_str[i + 5 :]
    return int("".join(sol), 2), remaining_string


def handle_operator_type_0(bits_str: str) -> Tuple[int, List[int], str]:
    total_length_in_bits = int(bits_str[0:15], 2)
    expected_remaining_length = len(bits_str) - 15 - total_length_in_bits
    remaining_str = bits_str[15:]

    packets: List[int] = []
    versions = 0
    while len(remaining_str) > expected_remaining_length:
        sum_versions, val, remaining_str = get_next_packet(remaining_str)
        packets.append(val)
        versions += sum_versions
    return versions, packets, remaining_str


def handle_operator_type_1(bits_str: str) -> Tuple[int, List[int], str]:
    packets: List[int] = []
    versions = 0
    nb_sub_packets = int(bits_str[0:11], 2)
    remaining_str = bits_str[11:]
    for _ in range(nb_sub_packets):
        sum_versions, val, remaining_str = get_next_packet(remaining_str)
        packets.append(val)
        versions += sum_versions
    # Do the operation on the list of ints
    return versions, packets, remaining_str


def handle_operator_bits(packet_id: int, bits_str: str) -> Tuple[int, int, str]:
    if bits_str[0] == "0":
        sum_versions, list_vals, remaining = handle_operator_type_0(bits_str[1:])
    else:
        sum_versions, list_vals, remaining = handle_operator_type_1(bits_str[1:])

    if packet_id == 0:
        return sum_versions, sum(list_vals), remaining
    if packet_id == 1:
        return sum_versions, reduce(lambda x, y: x * y, list_vals), remaining
    if packet_id == 2:
        return sum_versions, min(list_vals), remaining
    if packet_id == 3:
        return sum_versions, max(list_vals), remaining
    if packet_id == 5:
        return sum_versions, 1 if list_vals[0] > list_vals[1] else 0, remaining
    if packet_id == 6:
        return sum_versions, 1 if list_vals[0] < list_vals[1] else 0, remaining
    if packet_id == 7:
        return sum_versions, 1 if list_vals[0] == list_vals[1] else 0, remaining
    raise ValueError(f"Unknown packet id {packet_id}")


def get_next_packet(str_bits: str) -> Tuple[int, int, str]:
    version, p_id, remaining = get_version_and_id(str_bits)
    sum_versions = 0
    if p_id == 4:
        val, remaining = handle_literal_bits(remaining)
    else:
        sum_versions, val, remaining = handle_operator_bits(p_id, remaining)
    return version + sum_versions, val, remaining


def part1(str_hexa: str) -> int:
    str_bits = transform_hexa_to_bits(str_hexa)
    sum_versions, val, remaining = get_next_packet(str_bits)
    if int(remaining) > 0:
        raise ValueError("ohoh, the padding is too long or is not 0...")
    return sum_versions


def part2(str_hexa: str) -> int:
    str_bits = transform_hexa_to_bits(str_hexa)
    sum_versions, val, remaining = get_next_packet(str_bits)
    if len(remaining) > 0 and int(remaining) > 0:
        raise ValueError("ohoh, the padding is too long or is not 0...")
    return val


if __name__ == "__main__":
    str_hexa_input = load_input()

    print("# Part 1")
    sol_part1 = part1(str_hexa_input)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2(str_hexa_input)
    print(f"Solution {sol_part2}")
