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

    def __init__(self, knot_count):
        self.visited_locations = set()

        self.rope_knots = []
        for i in range(knot_count):
            self.rope_knots.append(Position(0, 0))
        self.visited_locations.add(Position(self.rope_knots[-1].x, self.rope_knots[-1].y))

    def execute_command(self, command: Command):
        for _ in range(command.move):
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

            self.rope_knots[0].x += move_x
            self.rope_knots[0].y += move_y

            for i in range(1, len(self.rope_knots)):
                head = self.rope_knots[i - 1]
                tail = self.rope_knots[i]
                # location is now diagonally away
                if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
                    diff_x = head.x - tail.x
                    diff_y = head.y - tail.y
                    move_x = int(math.copysign(1, diff_x)) if diff_x else 0
                    move_y = int(math.copysign(1, diff_y)) if diff_y else 0
                    tail.x += move_x
                    tail.y += move_y

            self.visited_locations.add(Position(self.rope_knots[-1].x, self.rope_knots[-1].y))

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
