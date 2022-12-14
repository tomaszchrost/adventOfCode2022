import data_reader
import height_map
import pytest


def test_part_two():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.best_starting_location() == 29
