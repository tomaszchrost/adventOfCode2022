import utils


def main():
    elf_calories = utils.get_elf_calories()
    print(sum(utils.max_n_values(elf_calories, 3)))


if __name__ == '__main__':
    main()
