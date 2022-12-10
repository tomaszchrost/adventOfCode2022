import utils


def main():
    commands = utils.get_commands(utils.COMMANDS_FILE_PATH)
    calculator = utils.CalculateSignalStrength()

    print(calculator.calculate_signal_strength(commands))


if __name__ == '__main__':
    main()
