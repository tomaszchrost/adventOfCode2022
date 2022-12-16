import data_reader
from sensor_beacon import *


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.cannot_contain_beacon_position_count(10) == 26
    assert data.cannot_contain_beacon_position_count(9) == 25
    assert data.cannot_contain_beacon_position_count(11) == 28
