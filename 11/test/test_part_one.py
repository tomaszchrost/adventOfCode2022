from keep_away import KeepAway
from monkey import Monkey
import pytest
import utils


def test_part_one():
    keep_away = KeepAway()
    monkeys = [Monkey([79, 98],
                      lambda old: old * 19,
                      23,
                      2,
                      3),
               Monkey([54, 65, 75, 74],
                      lambda old: old + 6,
                      19,
                      2,
                      0),
               Monkey([79, 60, 97],
                      lambda old: old * old,
                      13,
                      1,
                      3),
               Monkey([74],
                      lambda old: old + 3,
                      17,
                      0,
                      1)]

    keep_away.monkeys = monkeys
    assert keep_away.get_monkey_business() == 10605
