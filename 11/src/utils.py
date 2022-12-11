from keep_away import KeepAway
from monkey import Monkey

def part_one_monkey_setup():
    keep_away = KeepAway()
    monkeys = [Monkey(
        [74, 64, 74, 63, 53],
        lambda old: old * 7,
        5,
        1,
        6), Monkey(
        [69, 99, 95, 62],
        lambda old: old * old,
        17,
        2,
        5
    ), Monkey(
        [59, 81],
        lambda old: old + 8,
        7,
        4,
        3
    ), Monkey(
        [50, 67, 63, 57, 63, 83, 97],
        lambda old: old + 4,
        13,
        0,
        7
    ), Monkey(
        [61, 94, 85, 52, 81, 90, 94, 70],
        lambda old: old + 3,
        19,
        7,
        3
    ), Monkey(
        [69],
        lambda old: old + 5,
        3,
        4,
        2
    ), Monkey(
        [54, 55, 58],
        lambda old: old + 7,
        11,
        1,
        5
    ), Monkey(
        [79, 51, 83, 88, 93, 76],
        lambda old: old * 3,
        2,
        0,
        6
    )]

    keep_away.monkeys = monkeys
    keep_away.calculate_lcm()
    return keep_away
