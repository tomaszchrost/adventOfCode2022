import data_reader


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.simulate_sand_falling() == 24
