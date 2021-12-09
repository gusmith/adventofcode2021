from src.day8.day8 import day8_part1, day8_part2

INPUT_TEST = [
    (
        [
            "be",
            "cfbegad",
            "cbdgef",
            "fgaecd",
            "cgeb",
            "fdcge",
            "agebfd",
            "fecdb",
            "fabcd",
            "edb",
        ],
        ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
    ),
    (
        [
            "edbfga",
            "begcd",
            "cbg",
            "gc",
            "gcadebf",
            "fbgde",
            "acbgfd",
            "abcde",
            "gfcbed",
            "gfec",
        ],
        ["fcgedb", "cgb", "dgebacf", "gc"],
    ),
    (
        [
            "fgaebd",
            "cg",
            "bdaec",
            "gdafb",
            "agbcfd",
            "gdcbef",
            "bgcad",
            "gfac",
            "gcb",
            "cdgabef",
        ],
        ["cg", "cg", "fdcagb", "cbg"],
    ),
    (
        [
            "fbegcd",
            "cbd",
            "adcefb",
            "dageb",
            "afcb",
            "bc",
            "aefdc",
            "ecdab",
            "fgdeca",
            "fcdbega",
        ],
        ["efabcd", "cedba", "gadfec", "cb"],
    ),
    (
        [
            "aecbfdg",
            "fbg",
            "gf",
            "bafeg",
            "dbefa",
            "fcge",
            "gcbea",
            "fcaegb",
            "dgceab",
            "fcbdga",
        ],
        ["gecf", "egdcabf", "bgf", "bfgea"],
    ),
    (
        [
            "fgeab",
            "ca",
            "afcebg",
            "bdacfeg",
            "cfaedg",
            "gcfdb",
            "baec",
            "bfadeg",
            "bafgc",
            "acf",
        ],
        ["gebdcfa", "ecba", "ca", "fadegcb"],
    ),
    (
        [
            "dbcfg",
            "fgd",
            "bdegcaf",
            "fgec",
            "aegbdf",
            "ecdfab",
            "fbedc",
            "dacgb",
            "gdcebf",
            "gf",
        ],
        ["cefg", "dcbef", "fcge", "gbcadfe"],
    ),
    (
        [
            "bdfegc",
            "cbegaf",
            "gecbf",
            "dfcage",
            "bdacg",
            "ed",
            "bedf",
            "ced",
            "adcbefg",
            "gebcd",
        ],
        ["ed", "bcgafe", "cdgba", "cbgef"],
    ),
    (
        [
            "egadfb",
            "cdbfeg",
            "cegd",
            "fecab",
            "cgb",
            "gbdefca",
            "cg",
            "fgcdab",
            "egfdb",
            "bfceg",
        ],
        ["gbdfcae", "bgc", "cg", "cgb"],
    ),
    (
        [
            "gcafb",
            "gcf",
            "dcaebfg",
            "ecagb",
            "gf",
            "abcdeg",
            "gaef",
            "cafbge",
            "fdbac",
            "fegbdc",
        ],
        ["fgae", "cfgab", "fg", "bagce"],
    ),
]


def test_part1():
    sol_test = day8_part1(INPUT_TEST)
    assert sol_test == 26


def test_part2():
    sol = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    computed_part2 = day8_part2(INPUT_TEST)
    assert computed_part2 == sol
