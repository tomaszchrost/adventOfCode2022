import utils
from keep_away import KeepAway


def main():
    keep_away: KeepAway = utils.part_one_monkey_setup()
    print(keep_away.get_monkey_business())


if __name__ == '__main__':
    main()
