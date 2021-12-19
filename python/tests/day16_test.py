from src.day16.day16 import get_version_and_id, handle_literal_bits, part1, part2


def test_get_version_and_id():
    example_test = "110100101111111000101000"
    version, p_id, _ = get_version_and_id(example_test)
    assert version == 6
    assert p_id == 4


def test_handle_literal():
    example_test = "101111111000101000"
    val, remaining = handle_literal_bits(example_test)
    assert val == 2021
    assert remaining == "000"


def test_part1():
    expected = {
        "8A004A801A8002F478": 16,
        "620080001611562C8802118E34": 12,
        "C0015000016115A2E0802F182340": 23,
        "A0016C880162017C3686B18A3D4780": 31,
    }
    for key, value in expected.items():
        sum_versions = part1(key)
        assert sum_versions == value


def test_part2():
    expected = {
        "C200B40A82": 3,
        "04005AC33890": 54,
        "880086C3E88112": 7,
        "CE00C43D881120": 9,
        "D8005AC2A8F0": 1,
        "F600BC2D8F": 0,
        "9C005AC2F8F0": 0,
        "9C0141080250320F1802104A08": 1,
    }
    for key, value in expected.items():
        sum_versions = part2(key)
        assert sum_versions == value
