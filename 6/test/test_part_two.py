import pytest
import utils


def test_part_two_1():
    assert utils.get_signal_value_part_two('nppdvjthqldpwncqszvftbrmjlhg') == 23


def test_part_two_2():
    assert utils.get_signal_value_part_two('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29


def test_part_two_3():
    assert utils.get_signal_value_part_two('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

