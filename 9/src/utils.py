import enum
import math
import os

RESOURCES = os.path.abspath('resources/')
ACTIONS_FILE_PATH = os.path.join(RESOURCES, 'actions.dat')


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Command:
    def __init__(self, direction: Direction, move: int):
        self.direction = direction
        self.move = move


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return 'Position(%s, %s)' % (self.x, self.y)


class RopeBridge:

    def __init__(self):
        self.head = Position(0, 0)
        self.tail = Position(0, 0)
        self.visited_locations = set()
        self.visited_locations.add(Position(self.head.x, self.head.y))

    def execute_command(self, command: Command):
        for i in range(command.move):
            move_x = 0
            move_y = 0
            if command.direction == Direction.UP:
                move_y += 1
            elif command.direction == Direction.DOWN:
                move_y -= 1
            elif command.direction == Direction.RIGHT:
                move_x += 1
            elif command.direction == Direction.LEFT:
                move_x -= 1

            self.head.x += move_x
            self.head.y += move_y

            # location is now diagonally away
            if abs(self.head.x - self.tail.x) > 1 or abs(self.head.y - self.tail.y) > 1:
                if abs(self.head.x != self.tail.x and self.head.y != self.tail.y):
                    if move_x:
                        self.tail.y = self.head.y
                    else:
                        self.tail.x = self.head.x
                    self.tail.x += move_x
                    self.tail.y += move_y
                else:
                    self.tail.x += move_x
                    self.tail.y += move_y

            self.visited_locations.add(Position(self.tail.x, self.tail.y))

    def execute_commands(self, commands):
        for command in commands:
            self.execute_command(command)

    def get_locations_visited_count(self):
        return len(self.visited_locations)


def get_commands(file_path):
    with open(file_path, 'r') as f:
        commands = f.readlines()

    formatted_commands = []
    for command in commands:
        command_array = command.strip().split()
        direction = command_array[0]
        if direction == 'U':
            direction = Direction.UP
        elif direction == 'D':
            direction = Direction.DOWN
        elif direction == 'R':
            direction = Direction.RIGHT
        elif direction == 'L':
            direction = Direction.LEFT

        move_number = int(command_array[1])

        formatted_commands.append(Command(direction, move_number))
    return formatted_commands
