import enum
import math
import os

RESOURCES = os.path.abspath('resources/')
TREE_FILE_PATH = os.path.join(RESOURCES, 'trees.dat')


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_data(file_path):
    with open(file_path, 'r') as f:
        trees = f.readlines()

    tree_array = []
    for line in trees:
        tree_array.append([int(tree_height) for tree_height in line.strip()])

    return tree_array


def get_number_of_visible_trees(tree_array):
    tree_visible = []
    for _ in range(len(tree_array)):
        tree_visible.append([0] * len(tree_array[0]))

    for row in range(len(tree_array)):
        height = -1
        for column in range(len(tree_array[0])):
            if height < tree_array[row][column]:
                height = tree_array[row][column]
                tree_visible[row][column] = 1
        height = -1
        for column in range(len(tree_array[0]) - 1, -1, -1):
            if height < tree_array[row][column]:
                height = tree_array[row][column]
                tree_visible[row][column] = 1

    for column in range(len(tree_array[0])):
        height = -1
        for row in range(len(tree_array)):
            if height < tree_array[row][column]:
                height = tree_array[row][column]
                tree_visible[row][column] = 1
        height = -1
        for row in range(len(tree_array) - 1, -1, -1):
            if height < tree_array[row][column]:
                height = tree_array[row][column]
                tree_visible[row][column] = 1

    return sum([sum(array) for array in tree_visible])


def get_tree_scenic_score_direction(row, column, tree_array, direction):
    if direction == Direction.UP:
        row_move = -1
        column_move = 0
    elif direction == Direction.DOWN:
        row_move = 1
        column_move = 0
    elif direction == Direction.RIGHT:
        row_move = 0
        column_move = 1
    elif direction == Direction.LEFT:
        row_move = 0
        column_move = -1
    else:
        row_move = -1
        column_move = -1

    tree_height = tree_array[row][column]

    scenic_score = 0

    row += row_move
    column += column_move
    while -1 < row < len(tree_array) and -1 < column < len(tree_array[0]):
        scenic_score += 1

        if tree_array[row][column] >= tree_height:
            return scenic_score

        row += row_move
        column += column_move

    return scenic_score


def get_tree_scenic_score(row, column, tree_array):
    return math.prod((get_tree_scenic_score_direction(row, column, tree_array, Direction.UP),
                      get_tree_scenic_score_direction(row, column, tree_array, Direction.DOWN),
                      get_tree_scenic_score_direction(row, column, tree_array, Direction.LEFT),
                      get_tree_scenic_score_direction(row, column, tree_array, Direction.RIGHT)))


def get_highest_scenic_score(tree_array):
    max_score = 0
    for row in range(len(tree_array)):
        for column in range(len(tree_array[0])):
            scenic_score = get_tree_scenic_score(row, column, tree_array)
            max_score = max(max_score, scenic_score)
    return max_score
