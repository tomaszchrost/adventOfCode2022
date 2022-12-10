import os

RESOURCES = os.path.abspath('resources/')
COMMANDS_FILE_PATH = os.path.join(RESOURCES, 'commands.dat')


def get_commands(file_path):
    with open(file_path, 'r') as f:
        commands = f.readlines()

    formatted_commands = []
    for command in commands:
        formatted_commands.append(command.strip().split())

    return formatted_commands

class CalculateSignalStrength():

    def __init__(self, screen_length=40):
        self.x = 0
        self.array_to_print = []
        self.screen_length = screen_length

    def calculate_signal_strength(self, commands):
        cycle = 0
        self.x = 1
        signal_strength = 0

        def addx(value):
            self.x += value

        for command in commands:
            if command[0] == 'noop':
                cycle_length = 1
                run = None
                args = None
            elif command[0] == 'addx':
                cycle_length = 2
                run = addx
                args = int(command[1])
            else:
                cycle_length = 0
                run = None
                args = None

            for i in range(cycle_length):
                cycle += 1

                if (cycle - 20) % 40 == 0:
                    signal_strength += self.x * cycle

                if i == cycle_length - 1:
                    if run is not None:
                        run(args)

        return signal_strength

    def calculate_signal_strength_part_two(self, commands):
        cycle = 0
        self.x = 1

        def addx(value):
            self.x += value
            #self.x = self.x % self.screen_length

        for command in commands:
            if command[0] == 'noop':
                cycle_length = 1
                run = None
                args = None
            elif command[0] == 'addx':
                cycle_length = 2
                run = addx
                args = int(command[1])
            else:
                cycle_length = 0
                run = None
                args = None

            for i in range(cycle_length):
                if cycle % self.screen_length in (self.x - 1, self.x, self.x + 1):
                    self.array_to_print.append('#')
                else:
                    self.array_to_print.append('.')

                if i == cycle_length - 1:
                    if run is not None:
                        run(args)

                cycle += 1

    def print_array(self):
        for i in range(len(self.array_to_print)):
            if (i + 1) % self.screen_length == 0:
                print(self.array_to_print[i])
            else:
                print(self.array_to_print[i], end="")
