import utils


def main():
    supplies = utils.get_supplies()
    supply_groups = utils.group_supplies(supplies, 3)
    priority_sum = 0
    for supply_group in supply_groups:
        item_type = utils.find_common_item_type(supply_group)
        priority_sum += utils.get_item_priority(item_type)
    print(priority_sum)


if __name__ == '__main__':
    main()
