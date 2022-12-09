import pytest
import utils


def test_part_one():
    tree_array = utils.get_data('resources/test_data.dat')
    assert utils.get_number_of_visible_trees(tree_array) == 21
