import pytest
import utils


def test_part_two():
    commands = utils.get_commands('resources/test_data.dat')
    calculator = utils.CalculateSignalStrength()
    print()
    calculator.calculate_signal_strength_part_two(commands)
    calculator.print_array()
