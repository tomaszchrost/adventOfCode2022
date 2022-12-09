import os
import pytest
import utils


def test_part_one_1():
    commands = utils.read_file('resources/test_data.dat')
    file_system = utils.FileSystem()
    file_system.execute_commands(commands)
    assert file_system.get_directories_smaller_than(100000) == 95437


def test_part_one_2():
    commands = utils.read_file('resources/test_data_2.dat')
    file_system = utils.FileSystem()
    file_system.execute_commands(commands)
    assert file_system.get_directories_smaller_than(100000) == 53000
