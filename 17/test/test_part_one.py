import data_reader


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    data.simulate_flow()
    assert data.get_height() == 3068
