import utils


def main():
    tree_array = utils.get_data(utils.TREE_FILE_PATH)
    print(utils.get_highest_scenic_score(tree_array))


if __name__ == '__main__':
    main()
