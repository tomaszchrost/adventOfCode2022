import os
from collections.abc import Iterable

RESOURCES = os.path.abspath('resources/')
SUPPLIES_FILE_PATH = os.path.join(RESOURCES, 'supplies.dat')

UPPERCASE_A_IN_ASCII = ord('A')
UPPERCASE_A_PRIORITY = 27
LOWERCASE_A_IN_ASCII = ord('a')
LOWERCASE_A_PRIORITY = 1

ASCII_TO_PRIORITY_UPPER = UPPERCASE_A_PRIORITY - UPPERCASE_A_IN_ASCII
ASCII_TO_PRIORITY_LOWER = LOWERCASE_A_PRIORITY - LOWERCASE_A_IN_ASCII


def get_shared_item(first_compartment, second_compartment):
    for item in first_compartment:
        if item in second_compartment:
            return item


def get_shared_items(*args: Iterable):
    item_set = set(args[0])
    for i in args[1:]:
        item_set = item_set.intersection(i)
    return list(item_set)


def split_supplies(supplies):
    length = len(supplies)
    middle_index = int(length / 2)
    return supplies[:middle_index], supplies[middle_index:]


def find_common_item_type(supply_group):
    shared_items = get_shared_items(supply_group[0], supply_group[1], supply_group[2])
    return shared_items[0]


def get_item_priority(item_type):
    ascii_item = ord(item_type)
    return ascii_item + ASCII_TO_PRIORITY_UPPER if item_type.isupper() else ascii_item + ASCII_TO_PRIORITY_LOWER


def get_supplies():
    with open(SUPPLIES_FILE_PATH) as f:
        supplies = f.readlines()

    return [supply.strip() for supply in supplies]


def group_supplies(supplies, groups_of):
    supply_groups = []
    for i in range(0, len(supplies), groups_of):
        supply_groups.append(supplies[i:i+groups_of])
    return supply_groups
