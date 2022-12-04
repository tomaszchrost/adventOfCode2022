import utils


def main():
    assignments = utils.get_assignments()
    count = 0
    for assignment in assignments:
        if utils.range_within_other(assignment[0], assignment[1]):
            count += 1
    print(count)


if __name__ == '__main__':
    main()