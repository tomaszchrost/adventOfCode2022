import pytest
import utils


def test_part_two_1():
    commands = utils.get_commands('resources/test_data.dat')
    rope_bridge = utils.RopeBridge(10)
    rope_bridge.execute_commands(commands)
    assert rope_bridge.get_locations_visited_count() == 1


def test_part_two_2():
    commands = utils.get_commands('resources/test_data_2.dat')
    rope_bridge = utils.RopeBridge(10)
    rope_bridge.execute_commands(commands)
    assert rope_bridge.get_locations_visited_count() == 36