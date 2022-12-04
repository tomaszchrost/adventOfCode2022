import os

RESOURCES = os.path.abspath('resources/')
ASSIGNMENTS_FILE_PATH = os.path.join(RESOURCES, 'assignments.dat')


def get_assignments():
    with open(ASSIGNMENTS_FILE_PATH) as f:
        assignments = f.readlines()

    formatted_assignments = format_assignments(assignments)

    return formatted_assignments


def format_assignments(assignments):
    temp_assignments = (assignment.strip().split(',') for assignment in assignments)
    formatted_assignments = []
    for assignment in temp_assignments:
        range_values = [unformatted_ranges.split('-') for unformatted_ranges in assignment]
        formatted_ranges = [[int(range_value[0]), int(range_value[1])] for range_value in range_values]
        formatted_assignments.append(formatted_ranges)

    return formatted_assignments


def range_within_other(range_value, other):
    return ((range_value[0] <= other[0] and range_value[1] >= other[1])
            or (range_value[0] >= other[0] and range_value[1] <= other[1]))


def range_overlap_at_all(range_value, other):
    return ((other[0] <= range_value[0] <= other[1])
            or (other[0] <= range_value[1] <= other[1])
            or (range_value[0] <= other[0] <= range_value[1])
            or (range_value[0] <= other[1] <= range_value[1]))
