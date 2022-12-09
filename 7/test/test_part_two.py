import os
import pytest
import utils


def test_part_two():
    commands = utils.read_file('resources/test_data.dat')
    file_system = utils.FileSystem()
    file_system.execute_commands(commands)
    assert file_system.get_smallest_directory_to_free() == 24933642
