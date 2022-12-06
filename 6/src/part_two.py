import utils


def main():
    signal = utils.read_file()
    print(utils.get_signal_value_part_two(signal))


if __name__ == '__main__':
    main()
