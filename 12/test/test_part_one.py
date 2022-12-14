import data_reader
import height_map
import pytest


def test_part_one():
    data = data_reader.DataReader().get_data('resources/test_data.dat')
    assert data.dijkstras() == 31
