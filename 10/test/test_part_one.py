import pytest
import utils


def test_part_one():
    commands = utils.get_commands('resources/test_data.dat')
    calculator = utils.CalculateSignalStrength()

    assert calculator.calculate_signal_strength(commands) == 13140
