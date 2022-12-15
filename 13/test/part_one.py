import data_reader
import signals


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert signals.sum_of_indices_in_order(data) == 13
