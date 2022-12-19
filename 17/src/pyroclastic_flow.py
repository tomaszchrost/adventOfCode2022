import copy
import enum
from typing import List


class Direction(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Shape:
    def __init__(self, shape_array: List[List[bool]], name: str):
        self.shape_array = shape_array
        self.name = name
        self.height = len(self.shape_array)
        self.length = len(self.shape_array[0])

    def __repr__(self):
        return self.name


class MinusShape(Shape):
    MINUS_SHAPE = [[True, True, True, True]]

    def __init__(self):
        super().__init__(self.MINUS_SHAPE, 'Minus')


class PlusShape(Shape):
    PLUS_SHAPE = list(reversed([[False, True, False],
                                [True, True, True],
                                [False, True, False]]))

    def __init__(self):
        super().__init__(self.PLUS_SHAPE, 'Plus')


class LShape(Shape):
    L_SHAPE = list(reversed([[False, False, True],
                             [False, False, True],
                             [True, True, True]]))

    def __init__(self):
        super().__init__(self.L_SHAPE, 'L')


class IShape(Shape):
    I_SHAPE = [[True],
               [True],
               [True],
               [True]]

    def __init__(self):
        super().__init__(self.I_SHAPE, 'I')


class SquareShape(Shape):
    SQUARE_SHAPE = [[True, True],
                    [True, True]]

    def __init__(self):
        super().__init__(self.SQUARE_SHAPE, 'Square')


class PyroclasticFlow:
    shape_cycle = [MinusShape(), PlusShape(), LShape(), IShape(), SquareShape()]
    chamber_width = 7

    def __init__(self, directions):
        self.directions: List[Direction] = directions
        self.chamber: List[List[int]] = []
        self.shape_index: int = 0
        self.direction_index: int = 0
        self.y_offset: int = 3
        self.x_offset: int = 2

    def get_height(self):
        for i in range(len(self.chamber), 0, -1):
            if True in self.chamber[i - 1]:
                return i
        return 0

    def intersects_with_bottom(self, current_position: Coordinates, shape: Shape):
        if current_position.y == -1:
            return True
        for x in range(shape.length):
            for y in range(shape.height):
                # if shape is full and chamber is full return True
                if shape.shape_array[y][x]:
                    if self.chamber[current_position.y + y][current_position.x + x]:
                        return True
                    else:
                        break
        return False

    def intersects_with_sides(self, current_position: Coordinates, shape: Shape):
        if current_position.x == -1 or current_position.x + shape.length - 1 == self.chamber_width:
            return True
        for y in range(shape.height):
            # check left of shape
            for x in range(shape.length):
                if shape.shape_array[y][x]:
                    if self.chamber[current_position.y + y][current_position.x + x]:
                        return True
                    else:
                        break
            # check right of shape
            for x in range(shape.length - 1, -1, -1):
                if shape.shape_array[y][x]:
                    if self.chamber[current_position.y + y][current_position.x + x]:
                        return True
                    else:
                        break
        return False

    def create_and_drop_shape(self):
        shape = self.shape_cycle[self.shape_index]
        self.shape_index = (self.shape_index + 1) % (len(self.shape_cycle))
        height = self.get_height()
        length = len(self.chamber)
        starting_height = height + self.y_offset + shape.height

        for _ in range(length, starting_height):
            self.chamber.append([False] * self.chamber_width)

        bottom_left_coordinate = Coordinates(2, height + self.y_offset)

        previous_position = None
        current_position = bottom_left_coordinate
        while not self.intersects_with_bottom(current_position, shape):
            previous_position = copy.copy(current_position)
            direction = self.directions[self.direction_index]
            self.direction_index = (self.direction_index + 1) % (len(self.directions))
            if direction == Direction.RIGHT:
                current_position.x += 1
            elif direction == Direction.LEFT:
                current_position.x -= 1
            if self.intersects_with_sides(current_position, shape):
                current_position = copy.copy(previous_position)
            previous_position = copy.copy(current_position)
            current_position.y -= 1
        current_position = previous_position
        self.add_shape_to_chamber(current_position, shape)
        #self.print_chamber()

    def add_shape_to_chamber(self, current_position: Coordinates, shape: Shape):
        for y in range(shape.height):
            for x in range(shape.length):
                if shape.shape_array[y][x]:
                    self.chamber[current_position.y + y][current_position.x + x] = True

    def simulate_flow(self):
        for _ in range(2022):
            self.create_and_drop_shape()

    def simulate_big_flow(self):
        for _ in range(1000000000000):
            self.create_and_drop_shape()

    def print_chamber(self):
        print()
        for array in reversed(self.chamber):
            string = ''
            for value in array:
                string += '#' if value else '.'
            print(string)
