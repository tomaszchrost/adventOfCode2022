import utils


def main():
    commands = utils.get_commands(utils.COMMANDS_FILE_PATH)
    calculator = utils.CalculateSignalStrength()

    calculator.calculate_signal_strength_part_two(commands)
    calculator.print_array()


if __name__ == '__main__':
    main()
