import pytest
import utils


def test_part_two():
    tree_array = utils.get_data('resources/test_data.dat')
    assert utils.get_highest_scenic_score(tree_array) == 8
