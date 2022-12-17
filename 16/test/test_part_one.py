import data_reader


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.get_max_pressure() == 1651
