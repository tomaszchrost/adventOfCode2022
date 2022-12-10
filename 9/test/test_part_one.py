import pytest
import utils


def test_part_one():
    commands = utils.get_commands('resources/test_data.dat')
    rope_bridge = utils.RopeBridge()
    rope_bridge.execute_commands(commands)
    assert rope_bridge.get_locations_visited_count() == 13
