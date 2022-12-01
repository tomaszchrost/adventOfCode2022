import os.path

RESOURCES = os.path.abspath('resources/')
CALORIES_FILE_PATH = os.path.join(RESOURCES, 'calories.dat')


def get_elf_calories():
    elf_calories = [0]
    with open(CALORIES_FILE_PATH, 'r') as f:
        calorie_list = f.readlines()

    for line in calorie_list:
        line = line.strip()
        if line:
            elf_calories[-1] += int(line)
        else:
            elf_calories.append(0)

    return elf_calories


def max_n_values(iterable, n):
    max_values = []
    min_value = None
    for item in iterable:
        if len(max_values) < n:
            max_values.append(item)
            min_value = min(max_values)
        elif min_value < item:
            max_values[max_values.index(min_value)] = item
            min_value = min(max_values)
    return max_values
