import utils


def main():
    supplies = utils.get_supplies()
    priority_sum = 0
    for supply in supplies:
        first_compartment, second_compartment = utils.split_supplies(supply)
        item_type = utils.get_shared_item(first_compartment, second_compartment)
        priority_sum += utils.get_item_priority(item_type)
    print(priority_sum)


if __name__ == '__main__':
    main()
