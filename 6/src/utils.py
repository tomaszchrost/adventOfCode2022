import os

RESOURCES = os.path.abspath('resources/')
SIGNAL_FILE_PATH = os.path.join(RESOURCES, 'signal.dat')


def read_file():
    with open(SIGNAL_FILE_PATH, 'r') as f:
        signal = f.readline()
    return signal


def get_signal_value(stream):
    for i in range(3, len(stream)):
        current_value = i + 1
        subset_to_check = stream[i-3:current_value]
        valid = True
        for j in range(len(subset_to_check)):
            smaller_subset = subset_to_check[:j]
            if subset_to_check[j] in smaller_subset:
                valid = False
                break
        if valid:
            return current_value


def get_signal_value_part_two(stream):
    for i in range(13, len(stream)):
        current_value = i + 1
        subset_to_check = stream[i-13:current_value]
        valid = True
        for j in range(len(subset_to_check)):
            smaller_subset = subset_to_check[:j]
            if subset_to_check[j] in smaller_subset:
                valid = False
                break
        if valid:
            return current_value
