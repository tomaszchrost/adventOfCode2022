import data_reader


def test_part_two():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    data.add_floor()
    assert data.simulate_sand_falling() == 93
