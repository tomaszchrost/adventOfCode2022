import enum
import terrain

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Direction(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Scanner:

    sand_origin = Coordinate(500, 0)

    def __init__(self):
        self.rock_structure = []
        self.sand = Coordinate(None, None)

    def simulate_sand_falling(self):

        def fall():
            self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.AIR
            self.rock_structure[self.sand.y+1][self.sand.x] = terrain.Terrain.SAND
            self.sand.y += 1

        def at_bottom():
            return self.sand.y == len(self.rock_structure) - 1

        def move(direction):
            if direction == Direction.LEFT:
                self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.AIR
                self.sand.x += -1
                self.sand.y += 1
                self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.SAND
            elif direction == Direction.RIGHT:
                self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.AIR
                self.sand.x += 1
                self.sand.y += 1
                self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.SAND

        units_of_sand_resting = 0
        while True:
            if self.rock_structure[self.sand_origin.y][self.sand_origin.x] == terrain.Terrain.SAND:
                break
            self.sand.x = self.sand_origin.x
            self.sand.y = self.sand_origin.y
            self.rock_structure[self.sand.y][self.sand.x] = terrain.Terrain.SAND
            settled = False
            while True:
                if self.sand.x + 1 == len(self.rock_structure[0]):
                    self.extend_grid()
                if self.rock_structure[self.sand.y+1][self.sand.x] == terrain.Terrain.AIR:
                    fall()
                elif self.rock_structure[self.sand.y+1][self.sand.x-1] == terrain.Terrain.AIR:
                    move(Direction.LEFT)
                elif self.rock_structure[self.sand.y+1][self.sand.x+1] == terrain.Terrain.AIR:
                    move(Direction.RIGHT)
                else:
                    settled = True

                if settled or at_bottom():
                    break

            if at_bottom():
                break
            #self.print_out_state()
            units_of_sand_resting += 1

        return units_of_sand_resting

    def print_out_state(self):
        to_print = [y_array[450:] for y_array in self.rock_structure]
        print()
        for line in to_print:
            for item in line:
                if item == terrain.Terrain.AIR:
                    print('.', end='')
                elif item == terrain.Terrain.SAND:
                    print('o', end='')
                elif item == terrain.Terrain.ROCK:
                    print('#', end='')
            print()

    def extend_grid(self):
        for i in range(len(self.rock_structure) - 1):
            self.rock_structure[i].append(terrain.Terrain.AIR)
        if self.rock_structure[len(self.rock_structure) - 1][0] == terrain.Terrain.ROCK:
            self.rock_structure[len(self.rock_structure) - 1].append(terrain.Terrain.ROCK)
        else:
            self.rock_structure[len(self.rock_structure) - 1].append(terrain.Terrain.AIR)

    def add_floor(self):
        len_x = len(self.rock_structure[0])
        self.rock_structure.append([terrain.Terrain.AIR] * len_x)
        self.rock_structure.append([terrain.Terrain.ROCK] * len_x)
