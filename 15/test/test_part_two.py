import data_reader
from sensor_beacon import *


def test_part_two():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.get_tuning_frequency(max_range=20) == 56000011
