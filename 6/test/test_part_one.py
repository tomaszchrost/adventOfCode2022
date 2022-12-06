import pytest
import utils


def test_part_one_1():
    assert utils.get_signal_value('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5


def test_part_one_2():
    assert utils.get_signal_value('nppdvjthqldpwncqszvftbrmjlhg') == 6


def test_part_one_3():
    assert utils.get_signal_value('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10


def test_part_one_4():
    assert utils.get_signal_value('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

